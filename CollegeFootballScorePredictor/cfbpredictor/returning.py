"""Returning production: how much of last season's output is on this season's roster.

For each team, every player on this season's roster is credited with what he
produced last season, wherever he played, so incoming transfers count and
departures (graduation, the NFL, the portal) do not. Transfers up from a lower
division count half. Each share is that credit over the team's own production
last season, so a team that lost its quarterback and added a better one can be
above 100% at the position.

The offensive share weights passing, receiving and rushing yards the way
returning-production research does (22.3, 35.0 and 3.1 of the 60.4 points they
carry; offensive line snaps, the rest of that scheme, are not in the data).
The defensive share counts sacks, interceptions, pass breakups and forced
fumbles.
"""

from __future__ import annotations

import logging

import numpy as np
import pandas as pd

from .config import FIRST_SEASON, RETURNING_PATH
from .data import load_production, load_roster, load_team_info, team_divisions

log = logging.getLogger(__name__)

STATS = ["pass_yds", "rec_yds", "rush_yds", "def_plays"]
OFF_WEIGHTS = {"pass_yds": 22.3, "rec_yds": 35.0, "rush_yds": 3.1}
LOWER_DIVISION_CREDIT = 0.5
MAX_SHARE = 2.0
RETURNING_COLUMNS = ["season", "team", "ret_pass", "ret_rec", "ret_rush", "ret_def", "ret_off",
                     "transfers_in"]


def returning_production(prev_prod: pd.DataFrame, roster: pd.DataFrame,
                         prev_divisions: pd.Series, divisions: pd.Series, season: int) -> pd.DataFrame:
    """Shares of last season's production on each team's ``season`` roster."""
    prev = prev_prod.copy()
    totals = prev.groupby("team")[STATS].sum()
    # A player's output last season, credited to the team he played for most.
    prev["size"] = prev[STATS[:3]].sum(axis=1) + 25 * prev["def_plays"]
    main = prev.sort_values("size").groupby("athlete_id")["team"].last()
    player = prev.groupby("athlete_id")[STATS].sum().join(main.rename("prev_team"))

    r = roster.dropna(subset=["athlete_id"]).drop_duplicates(["athlete_id", "team"])
    r = r.assign(athlete_id=r["athlete_id"].astype("int64")).join(player, on="athlete_id", how="inner")
    up = r["prev_team"].map(prev_divisions).ne("fbs") & r["team"].map(divisions).eq("fbs")
    credit = np.where(up, LOWER_DIVISION_CREDIT, 1.0)
    num = (r[STATS].mul(credit, axis=0)).groupby(r["team"]).sum()
    moved = r["prev_team"] != r["team"]
    transfers = r[moved & (r[STATS].sum(axis=1) > 0)].groupby("team").size()

    # Teams missing from either season (no roster published, new to the data)
    # get no shares rather than zero.
    rostered = set(roster["team"])
    teams = totals.index[totals.index.isin(rostered) & (totals.sum(axis=1) > 0).to_numpy()]
    num, den = num.reindex(teams).fillna(0.0), totals.reindex(teams)
    share = (num / den.where(den > 0)).clip(upper=MAX_SHARE)
    out = pd.DataFrame({
        "season": season, "team": teams,
        "ret_pass": share["pass_yds"].to_numpy(), "ret_rec": share["rec_yds"].to_numpy(),
        "ret_rush": share["rush_yds"].to_numpy(), "ret_def": share["def_plays"].to_numpy(),
    })
    # The composite only uses parts the team had last season.
    w = pd.DataFrame({k: np.where(share[k].notna(), v, 0.0) for k, v in OFF_WEIGHTS.items()}, index=teams)
    parts = share[list(OFF_WEIGHTS)].fillna(0.0)
    out["ret_off"] = ((parts * w).sum(axis=1) / w.sum(axis=1).replace(0, np.nan)).to_numpy()
    out["transfers_in"] = transfers.reindex(teams).fillna(0).astype(int).to_numpy()
    return out[RETURNING_COLUMNS].reset_index(drop=True)


def build_returning(seasons, max_age_hours: float = 6.0) -> pd.DataFrame:
    frames = []
    for season in seasons:
        prev = load_production(season - 1)
        if prev.empty:
            continue
        try:
            roster = load_roster(season, max_age_hours)
        except Exception as exc:  # no roster published yet
            log.info("No %s roster yet (%s)", season, exc)
            continue
        prev_div = team_divisions(load_team_info(season - 1, max_age_hours))["division"]
        div = team_divisions(load_team_info(season, max_age_hours))["division"]
        frames.append(returning_production(prev, roster, prev_div, div, season))
    return pd.concat(frames, ignore_index=True) if frames else pd.DataFrame(columns=RETURNING_COLUMNS)


def update_returning(season: int, started: bool, max_age_hours: float = 6.0) -> pd.DataFrame:
    """Load the committed table, (re)building ``season`` from its latest roster.

    Rosters change through the offseason (the spring portal window, signing
    day), so the season is rebuilt on every run until its first game has been
    played and kept fixed after that, so the preseason prior never moves once
    games count.
    """
    table = load_returning()
    if started and season in set(table["season"]):
        return table
    new = build_returning([season], max_age_hours)
    if len(new):
        table = pd.concat([table[table["season"] != season], new], ignore_index=True)
        table.to_csv(RETURNING_PATH, index=False, float_format="%.3f")
        log.info("Built %s returning production for %d teams", season, len(new))
    return table


def load_returning() -> pd.DataFrame:
    if not RETURNING_PATH.exists():
        return pd.DataFrame(columns=RETURNING_COLUMNS)
    return pd.read_csv(RETURNING_PATH)


def rebuild(last: int, max_age_hours: float = 6.0) -> pd.DataFrame:
    table = build_returning(range(FIRST_SEASON + 1, last + 1), max_age_hours)
    table.to_csv(RETURNING_PATH, index=False, float_format="%.3f")
    return table
