"""Skater availability: regulars missing from a team's lineup.

A run before puck drop cannot see tonight's lineup, so availability comes
from the box scores of games already played. For each team and game, a
skater is a regular when he played at least ``REGULAR_MIN`` of the team's
last ``REGULAR_WINDOW`` games; a regular who was not in the team's most
recent game is taken to be out (injured, ill, suspended or scratched). Each
absent regular counts by his role over those games:

    lost_f    forwards' average ice time, as a share of the game (a top-line
              center at 20 minutes is 0.33)
    lost_d    the same for defensemen
    lost_pts  their points per game

Absences that last a while also reach the team ratings, which weigh recent
games most; these features catch the first games of an absence, which the
ratings have not seen yet, and the goal-rate model weighs them (``model.py``).
Each season starts over: before a team's third game nobody is a regular.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

SKATER_COLUMNS = ["game_id", "team", "lost_f", "lost_d", "lost_pts"]
LOSS_COLUMNS = ["lost_f", "lost_d", "lost_pts"]
REGULAR_WINDOW = 5
REGULAR_MIN = 3
FORWARDS = {"C", "L", "R", "F", "LW", "RW"}
DEFENSE = {"D"}


def toi_minutes(toi: pd.Series) -> pd.Series:
    """'MM:SS' strings (or minutes already) as minutes."""
    if pd.api.types.is_numeric_dtype(toi):
        return toi.astype(float)
    parts = toi.astype(str).str.split(":", n=1, expand=True)
    if parts.shape[1] < 2:
        return pd.to_numeric(parts[0], errors="coerce")
    return pd.to_numeric(parts[0], errors="coerce") + pd.to_numeric(parts[1], errors="coerce") / 60.0


def appearances(box: pd.DataFrame, games: pd.DataFrame) -> pd.DataFrame:
    """One row per skater-game with the team code from the schedule, his position group,
    ice time in minutes and points."""
    g = games.set_index("game_id")
    b = box[box["game_id"].isin(g.index) & box["position"].isin(FORWARDS | DEFENSE)]
    home = b["home_away"].eq("home")
    team = np.where(home, b["game_id"].map(g["home_team"]), b["game_id"].map(g["away_team"]))
    return pd.DataFrame({"game_id": b["game_id"].to_numpy(), "team": team, "player_id": b["player_id"].to_numpy(),
                         "d": b["position"].isin(DEFENSE).to_numpy(), "toi": toi_minutes(b["toi"]).to_numpy(),
                         "points": pd.to_numeric(b["points"], errors="coerce").fillna(0).to_numpy()})


def losses(box: pd.DataFrame, games: pd.DataFrame) -> pd.DataFrame:
    """``SKATER_COLUMNS`` for every game in ``games`` (played or not) and both teams, from the
    box scores of each team's earlier games."""
    apps = appearances(box, games)
    by_game = {k: grp for k, grp in apps.groupby(["game_id", "team"])}
    order = games.sort_values(["start", "game_id"])
    rows = []
    for team in pd.unique(order[["home_team", "away_team"]].to_numpy().ravel()):
        mine = order[(order["home_team"] == team) | (order["away_team"] == team)]
        played: list[pd.DataFrame] = []
        for gid in mine["game_id"]:
            lost = dict.fromkeys(LOSS_COLUMNS, 0.0)
            if len(played) >= REGULAR_MIN:
                window = pd.concat(played[-REGULAR_WINDOW:])
                stats = window.groupby("player_id").agg(n=("toi", "size"), toi=("toi", "mean"), pts=("points", "mean"),
                                                        d=("d", "first"))
                regulars = stats[stats["n"] >= REGULAR_MIN]
                out = regulars[~regulars.index.isin(played[-1]["player_id"])]
                lost = {"lost_f": float(out.loc[~out["d"], "toi"].sum() / 60.0),
                        "lost_d": float(out.loc[out["d"], "toi"].sum() / 60.0),
                        "lost_pts": float(out["pts"].sum())}
            rows.append({"game_id": gid, "team": team, **lost})
            grp = by_game.get((gid, team))
            if grp is not None and len(grp):
                played.append(grp)
    out = pd.DataFrame(rows, columns=SKATER_COLUMNS)
    out[LOSS_COLUMNS] = out[LOSS_COLUMNS].round(4)
    return out
