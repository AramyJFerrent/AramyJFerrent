"""Pregame features for every game, using only what was known beforehand.

For historical games this is a walk-forward pass by date: the features for a
game come from ratings fitted on that season's earlier days plus the preseason
prior. For upcoming games the same features come from every game played
before today.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from .config import Hyperparams
from .elo import run_elo
from .goalies import GoalieModel, day_index, starter_columns
from .ratings import Ratings, RatingsEngine, prepare_rows, season_day, targets
from .skaters import LOSS_COLUMNS

# League scoring drifts, so the baseline is a recency-weighted average of
# recent games rather than a fixed number (regulation goals per team with
# both goalies in).
ENV_HALF_LIFE_DAYS = 120.0
ENV_PRIOR_GOALS = 2.7
ENV_PRIOR_GAMES = 50.0
MAX_REST = 4

GAME_COLUMNS = ["game_id", "season", "game_type", "playoff", "neutral", "start", "date",
                "home_team", "away_team", "venue", "completed", "home_score", "away_score"]
OUTCOME_COLUMNS = ["home_reg", "away_reg", "home_en", "away_en", "periods", "shootout"]


def rest_days(games: pd.DataFrame) -> pd.DataFrame:
    """Days since each side's previous game (capped), including scheduled games."""
    long = pd.concat([
        pd.DataFrame({"game_id": games["game_id"], "team": games["home_team"], "side": "home",
                      "season": games["season"], "dix": day_index(games["date"])}),
        pd.DataFrame({"game_id": games["game_id"], "team": games["away_team"], "side": "away",
                      "season": games["season"], "dix": day_index(games["date"])}),
    ]).sort_values(["team", "dix", "game_id"])
    prev = long.groupby(["team", "season"])["dix"].shift()
    long["rest"] = (long["dix"] - prev).clip(upper=MAX_REST).fillna(MAX_REST)
    wide = long.pivot_table(index="game_id", columns="side", values="rest")
    return wide.rename(columns={"home": "home_rest", "away": "away_rest"})


def outcomes(team_games: pd.DataFrame) -> pd.DataFrame:
    """How each finished game played out, from the home side's summary row."""
    h = team_games[team_games["home"] == 1].set_index("game_id")
    return pd.DataFrame({"home_reg": h["reg_gf"], "away_reg": h["reg_ga"], "home_en": h["en_gf"],
                         "away_en": h["en_ga"], "periods": h["periods"], "shootout": h["shootout"]})


def actual_starters(goalies: pd.DataFrame, games: pd.DataFrame) -> pd.DataFrame:
    st = goalies[goalies["starter"]].drop_duplicates(["game_id", "team"]).set_index(["game_id", "team"])["goalie_id"]
    g = games.set_index("game_id")
    home = pd.Series(list(zip(g.index, g["home_team"])), index=g.index).map(st)
    away = pd.Series(list(zip(g.index, g["away_team"])), index=g.index).map(st)
    return pd.DataFrame({"home_goalie_id": home, "away_goalie_id": away})


class FeatureBuilder:
    def __init__(self, games: pd.DataFrame, summaries: dict, hp: Hyperparams):
        self.games = games
        self.hp = hp
        team_games = summaries["teams"]
        self.engines = {
            name: RatingsEngine(prepare_rows(team_games, games, target), target, hp.half_life_days)
            for name, target in targets(hp).items()
        }
        self.goalies = GoalieModel(summaries["goalies"], hp)
        elo, self.elo_ratings = run_elo(games)
        self.elo = elo.set_index("game_id")
        self.rest = rest_days(games)
        self.outcomes = outcomes(team_games)
        self.starters = actual_starters(summaries["goalies"], games)
        sk = summaries.get("skaters")
        self.skaters = (sk.drop_duplicates(["game_id", "team"]).set_index(["game_id", "team"])
                        if sk is not None and len(sk) else None)
        self._env_dix = day_index(team_games["date"])
        self._env_goals = team_games["reg_gf"].to_numpy(float)

    def scoring_environment(self, dix: int) -> float:
        mask = self._env_dix < dix
        decay = 0.5 ** ((dix - self._env_dix[mask]) / ENV_HALF_LIFE_DAYS)
        return float((decay @ self._env_goals[mask] + ENV_PRIOR_GAMES * ENV_PRIOR_GOALS)
                     / (decay.sum() + ENV_PRIOR_GAMES))

    def ratings(self, season: int, day: float) -> dict[str, Ratings]:
        return {name: engine.before(season, day) for name, engine in self.engines.items()}

    def _rows(self, games: pd.DataFrame, ratings: dict[str, Ratings], season: int, dix: int,
              known_starters: bool) -> pd.DataFrame:
        cols: dict[str, object] = {}
        for side in ("home", "away"):
            teams = games[f"{side}_team"].tolist()
            for name, r in ratings.items():
                cols[f"off_{name}_{side}"] = [r.off.get(t, 0.0) for t in teams]
                cols[f"def_{name}_{side}"] = [r.deff.get(t, 0.0) for t in teams]
        for name, r in ratings.items():
            cols[f"league_{name}"] = r.mu
        for side in ("home", "away"):
            keys = pd.MultiIndex.from_arrays([games["game_id"], games[f"{side}_team"]])
            lost = self.skaters.reindex(keys) if self.skaters is not None else None
            for col in LOSS_COLUMNS:
                cols[f"{side}_{col}"] = lost[col].fillna(0.0).to_numpy() if lost is not None else 0.0
        starters_in = games[["game_id", "date", "home_team", "away_team"]].copy()
        if known_starters:
            given = self.starters.reindex(games["game_id"])
            for col in ("home_goalie_id", "away_goalie_id"):
                own = games[col].to_numpy() if col in games else np.full(len(games), np.nan)
                starters_in[col] = np.where(pd.isna(own), given[col].to_numpy(), own)
        else:
            starters_in["home_goalie_id"] = np.nan
            starters_in["away_goalie_id"] = np.nan
        cols["env_goals"] = self.scoring_environment(dix)
        out = pd.concat([games[GAME_COLUMNS].reset_index(drop=True),
                         pd.DataFrame(cols, index=range(len(games))),
                         starter_columns(self.goalies, starters_in.reset_index(drop=True), season, dix,
                                         self.hp.half_life_days)], axis=1)
        out = out.join(self.rest, on="game_id").join(self.elo, on="game_id").join(self.outcomes, on="game_id")
        out[["home_rest", "away_rest"]] = out[["home_rest", "away_rest"]].fillna(MAX_REST)
        return out

    def walk_forward(self, seasons, known_starters: bool = True, until=None) -> pd.DataFrame:
        """Features for every game in ``seasons``, each built from earlier days only.

        With ``known_starters`` the actual starting goalies are used (what a
        game-day run knows once starters are confirmed); without, each starter
        is projected from usage, as a morning run before confirmations would.
        Dates on or after ``until`` are skipped.
        """
        frames = []
        for season in seasons:
            season_games = self.games[self.games["season"] == season]
            for date, day_games in season_games.groupby("date"):
                if until is not None and date >= until:
                    continue
                day = float(season_day(pd.Series([date]), season)[0])
                dix = int(day_index([date])[0])
                frames.append(self._rows(day_games, self.ratings(season, day), season, dix, known_starters))
        return pd.concat(frames, ignore_index=True) if frames else pd.DataFrame()

    def current(self, games: pd.DataFrame, season: int, today) -> tuple[pd.DataFrame, dict[str, Ratings]]:
        """Features for upcoming ``games`` from every game played before ``today``."""
        day = float(season_day(pd.Series([today]), season)[0])
        dix = int(day_index([today])[0])
        ratings = self.ratings(season, day)
        if games.empty:
            return games.copy(), ratings
        return self._rows(games, ratings, season, dix, known_starters=True), ratings
