"""Goal-margin Elo: the win-probability baseline every other stage must beat."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd


@dataclass
class EloParams:
    k: float = 8.0
    home_ice: float = 30.0          # Elo points, about a 54% home win rate
    season_revert: float = 0.5      # share of the gap to the mean erased each offseason
    mean: float = 1500.0
    elo_per_goal: float = 100.0


def run_elo(games: pd.DataFrame, params: EloParams = EloParams()) -> tuple[pd.DataFrame, dict]:
    """Pregame Elo goal edge and win probability for every game, in start order.

    Completed games update ratings (overtime and shootout wins count as wins,
    the shootout decider as a one-goal margin); upcoming games are rated with
    the latest ratings. Returns per-game columns and each team's current rating.
    """
    ratings: dict[str, float] = {}
    season = None
    out = []
    for g in games.sort_values(["start", "game_id"]).itertuples(index=False):
        if g.season != season:
            season = g.season
            ratings = {t: r + (params.mean - r) * params.season_revert for t, r in ratings.items()}
        home = ratings.setdefault(g.home_team, params.mean)
        away = ratings.setdefault(g.away_team, params.mean)
        hfa = 0.0 if g.neutral else params.home_ice
        diff = home - away + hfa
        prob = 1.0 / (1.0 + 10 ** (-diff / 400.0))
        out.append((g.game_id, diff / params.elo_per_goal, prob))
        if g.completed:
            margin = g.home_score - g.away_score
            outcome = 1.0 if margin > 0 else 0.0
            winner_diff = diff if margin > 0 else -diff
            mult = np.log(abs(margin) + 1.0) * 2.2 / (winner_diff * 0.001 + 2.2)
            shift = params.k * mult * (outcome - prob)
            ratings[g.home_team] = home + shift
            ratings[g.away_team] = away - shift
    frame = pd.DataFrame(out, columns=["game_id", "elo_edge", "elo_home_prob"])
    return frame, ratings
