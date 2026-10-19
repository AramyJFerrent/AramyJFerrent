"""Team Elo with a starting-pitcher adjustment: the baseline every other stage must beat.

Close to FiveThirtyEight's MLB model: margin-aware team Elo with home field
and an offseason pull toward the mean, plus an adjustment for the day's
starter. Each pitcher carries a rolling game score; the starter's edge over
his team's usual starters moves the win chance.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd


@dataclass
class EloParams:
    k: float = 4.0
    home_field: float = 24.0        # Elo points, about a 53.5% home win rate
    season_revert: float = 0.33     # share of the gap to the mean erased each offseason
    mean: float = 1500.0
    pitcher_weight: float = 4.7     # Elo points per point of rolling game score
    pitcher_decay: float = 0.94     # weight of a pitcher's earlier starts
    team_decay: float = 0.98
    prior_starts: float = 3.0
    league_game_score: float = 50.0


def game_scores(pitching: pd.DataFrame) -> pd.DataFrame:
    """Each start's game score (FiveThirtyEight's version)."""
    st = pitching[pitching["starter"] == 1].copy()
    hits = st["s"] + st["d"] + st["t"] + st["hr"]
    st["gs"] = 47.4 + 1.5 * st["outs"] + 2 * st["k"] - 2 * st["bb"] - 2 * hits - 3 * st["r"] - 4 * st["hr"]
    return st[["game_id", "team", "player_id", "gs"]]


def run_elo(games: pd.DataFrame, pitching: pd.DataFrame, params: EloParams = EloParams(),
            starters: pd.DataFrame | None = None) -> tuple[pd.DataFrame, dict]:
    """Pregame Elo win probability for every game, in start order.

    ``starters`` (game_id -> home_starter, away_starter) overrides the
    starters in ``games`` (probable pitchers for upcoming games).
    Returns per-game columns and each team's current rating.
    """
    gs = game_scores(pitching).set_index(["game_id", "team"])["gs"].to_dict()
    ratings: dict[str, float] = {}
    pitcher: dict[str, tuple[float, float]] = {}     # weighted sum, weight
    team_rgs: dict[str, float] = {}
    season = None
    out = []
    starters = starters.set_index("game_id") if starters is not None else None
    for g in games.itertuples(index=False):
        if g.season != season:
            season = g.season
            ratings = {t: r + (params.mean - r) * params.season_revert for t, r in ratings.items()}
        home = ratings.setdefault(g.home_team, params.mean)
        away = ratings.setdefault(g.away_team, params.mean)
        sp = {"home": g.home_starter, "away": g.away_starter}
        if starters is not None and g.game_id in starters.index:
            row = starters.loc[g.game_id]
            sp = {s: row[f"{s}_starter"] if pd.notna(row[f"{s}_starter"]) else sp[s] for s in sp}
        adj = {}
        for side, team in (("home", g.home_team), ("away", g.away_team)):
            num, den = pitcher.get(sp[side], (0.0, 0.0))
            rgs = (num + params.prior_starts * params.league_game_score) / (den + params.prior_starts)
            adj[side] = params.pitcher_weight * (rgs - team_rgs.get(team, params.league_game_score))
        hfa = 0.0 if g.neutral else params.home_field
        diff = home - away + hfa + adj["home"] - adj["away"]
        prob = 1.0 / (1.0 + 10 ** (-diff / 400.0))
        out.append((g.game_id, prob, diff))
        if not g.completed:
            continue
        margin = g.home_score - g.away_score
        outcome = 1.0 if margin > 0 else 0.0
        mult = np.log(abs(margin) + 1.0) * 2.2 / ((diff if margin > 0 else -diff) * 0.001 + 2.2)
        shift = params.k * mult * (outcome - prob)
        ratings[g.home_team] = home + shift
        ratings[g.away_team] = away - shift
        for side, team in (("home", g.home_team), ("away", g.away_team)):
            score = gs.get((g.game_id, team))
            pid = g.home_starter if side == "home" else g.away_starter
            if score is None or pd.isna(pid):
                continue
            num, den = pitcher.get(pid, (0.0, 0.0))
            pitcher[pid] = (params.pitcher_decay * num + score, params.pitcher_decay * den + 1.0)
            team_rgs[team] = params.team_decay * team_rgs.get(team, params.league_game_score) \
                + (1 - params.team_decay) * score
    frame = pd.DataFrame(out, columns=["game_id", "elo_home_prob", "elo_diff"])
    return frame, ratings
