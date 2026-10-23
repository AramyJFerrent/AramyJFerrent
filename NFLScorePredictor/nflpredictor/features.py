"""Pregame features for every game, using only what was known beforehand.

For historical games this is a walk-forward pass: the features for week W of a
season come from ratings fitted on that season's weeks 1 to W-1 plus the
preseason prior. For upcoming games the same features come from every game
played so far.
"""

from __future__ import annotations

import pandas as pd

from .config import Hyperparams
from .elo import run_elo
from .injuries import LOSS_COLUMNS
from .qb import WEEKS_PER_SEASON, QBModel, adjustments
from .ratings import RatingsEngine, Ratings, prepare_rows, targets

# League scoring drifts, so the baseline is a recency-weighted average of
# recent games rather than a fixed number.
ENV_HALF_LIFE_WEEKS = 20.0
ENV_PRIOR_POINTS = 22.0
ENV_PRIOR_GAMES = 20.0

GAME_COLUMNS = [
    "game_id", "season", "week", "game_type", "playoff", "neutral", "div_game", "kickoff",
    "home_team", "away_team", "roof", "wind", "temp", "stadium_id", "home_rest", "away_rest",
    "spread_line", "total_line", "home_moneyline", "away_moneyline",
    "home_spread_odds", "away_spread_odds", "over_odds", "under_odds",
    "completed", "home_score", "away_score",
]


class FeatureBuilder:
    def __init__(self, games: pd.DataFrame, team_games: pd.DataFrame, qbs: pd.DataFrame,
                 hp: Hyperparams, injuries: pd.DataFrame | None = None):
        """``injuries``: non-QB injury losses by season, week and team (``injuries.losses``);
        without them every loss is zero."""
        self.games = games
        self.hp = hp
        self.injuries = (injuries.drop_duplicates(["season", "week", "team"]).set_index(["season", "week", "team"])
                         if injuries is not None and len(injuries) else None)
        self.engines = {
            name: RatingsEngine(prepare_rows(team_games, games, target), target, hp.half_life_weeks)
            for name, target in targets(hp).items()
        }
        self.qb = QBModel(qbs, hp)
        elo, self.elo_ratings = run_elo(games)
        self.elo = elo.set_index("game_id")
        done = games[games["completed"]]
        self._env_widx = (done["season"] * WEEKS_PER_SEASON + done["week"]).to_numpy()
        self._env_pts = ((done["home_score"] + done["away_score"]) / 2).to_numpy()
        self._summary_weeks = team_games.groupby("season")["week"].max().to_dict()

    def scoring_environment(self, season: int, week: int) -> float:
        ref = season * WEEKS_PER_SEASON + week
        mask = self._env_widx < ref
        decay = 0.5 ** ((ref - self._env_widx[mask]) / ENV_HALF_LIFE_WEEKS)
        return float((decay @ self._env_pts[mask] + ENV_PRIOR_GAMES * ENV_PRIOR_POINTS)
                     / (decay.sum() + ENV_PRIOR_GAMES))

    def ratings(self, season: int, week: int) -> dict[str, Ratings]:
        return {name: engine.before(season, week) for name, engine in self.engines.items()}

    def _rows(self, games: pd.DataFrame, ratings: dict[str, Ratings], season: int, week: int,
              ref_week: float) -> pd.DataFrame:
        out = games[GAME_COLUMNS].copy()
        main = ratings["epa"]
        for side in ("home", "away"):
            team = games[f"{side}_team"]
            out[f"off_{side}"] = team.map(main.off).fillna(0.0)
            out[f"def_{side}"] = team.map(main.deff).fillna(0.0)
            out[f"plays_{side}"] = team.map(main.plays).fillna(0.0)
            for name, r in ratings.items():
                if name != "epa":
                    out[f"off_{name}_{side}"] = team.map(r.off).fillna(0.0)
                    out[f"def_{name}_{side}"] = team.map(r.deff).fillna(0.0)
        out["league_epa"] = main.mu
        for side in ("home", "away"):
            if self.injuries is None:
                for col in LOSS_COLUMNS:
                    out[f"{side}_{col}"] = 0.0
                continue
            keys = pd.MultiIndex.from_arrays([games["season"], games["week"], games[f"{side}_team"]])
            lost = self.injuries.reindex(keys)
            for col in LOSS_COLUMNS:
                out[f"{side}_{col}"] = lost[col].fillna(0.0).to_numpy()
        out = out.join(adjustments(self.qb, games, season, week, ref_week))
        out["env_points"] = self.scoring_environment(season, week)
        out = out.join(self.elo, on="game_id")
        return out

    def walk_forward(self, seasons) -> pd.DataFrame:
        """Features for every game in ``seasons``, each built from earlier weeks only."""
        frames = []
        for season in seasons:
            season_games = self.games[self.games["season"] == season]
            for week, week_games in season_games.groupby("week"):
                frames.append(self._rows(week_games, self.ratings(season, week), season, week, week))
        return pd.concat(frames, ignore_index=True) if frames else pd.DataFrame()

    def current(self, games: pd.DataFrame, season: int) -> tuple[pd.DataFrame, dict[str, Ratings]]:
        """Features for upcoming ``games`` from every game played so far this season."""
        cutoff = int(self._summary_weeks.get(season, 0)) + 1
        ratings = self.ratings(season, cutoff)
        return self._rows(games, ratings, season, cutoff, cutoff), ratings
