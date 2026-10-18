"""Margin-of-victory Elo: the sanity-check baseline every other stage must beat."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd


@dataclass
class EloParams:
    # Tuned on 2015-2025 margins, starting from 2005.
    k: float = 30.0
    home_field: float = 50.0        # Elo points, about 3 points of spread
    season_revert: float = 0.2      # share of the gap to the division mean erased each offseason
    fbs_mean: float = 1500.0
    fcs_mean: float = 1150.0        # FCS teams start (and revert) well below FBS
    elo_per_point: float = 16.0


def run_elo(games: pd.DataFrame, params: EloParams = EloParams()) -> tuple[pd.DataFrame, dict]:
    """Pregame Elo spread and win probability for every game, in kickoff order.

    Completed games update ratings; upcoming games are rated with the latest
    ratings. Returns per-game columns and the current rating of each team.
    """
    ratings: dict[str, float] = {}
    division: dict[str, str] = {}
    season = None
    out = []
    cols = ["season", "week", "kickoff", "game_id"]
    for g in games.sort_values(cols).itertuples(index=False):
        if g.season != season:
            season = g.season
            ratings = {t: r + (_mean(division.get(t), params) - r) * params.season_revert
                       for t, r in ratings.items()}
        division[g.home_team], division[g.away_team] = g.home_division, g.away_division
        home = ratings.setdefault(g.home_team, _mean(g.home_division, params))
        away = ratings.setdefault(g.away_team, _mean(g.away_division, params))
        hfa = 0.0 if g.neutral else params.home_field
        diff = home - away + hfa
        prob = 1.0 / (1.0 + 10 ** (-diff / 400.0))
        out.append((g.game_id, diff / params.elo_per_point, prob))
        if g.completed:
            margin = g.home_score - g.away_score
            outcome = 1.0 if margin > 0 else 0.0 if margin < 0 else 0.5
            winner_diff = diff if margin > 0 else -diff
            mult = np.log(abs(margin) + 1.0) * 2.2 / (winner_diff * 0.001 + 2.2) if margin else 1.0
            shift = params.k * mult * (outcome - prob)
            ratings[g.home_team] = home + shift
            ratings[g.away_team] = away - shift
    frame = pd.DataFrame(out, columns=["game_id", "elo_spread", "elo_home_prob"])
    return frame, ratings


def _mean(division, params: EloParams) -> float:
    return params.fcs_mean if division == "fcs" else params.fbs_mean
