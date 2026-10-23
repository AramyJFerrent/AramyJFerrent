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
from .lines import LINE_COLUMNS
from .prior import PriorModel, members_from
from .qb import QBModel
from .ratings import Ratings, RatingsEngine, prepare_rows, targets
from .travel import travel_features

# Scoring drifts (FBS totals fell from 58 in 2016 to 52 in 2025), so the
# baseline is a recency-weighted average of recent games, not a fixed number.
ENV_HALF_LIFE_WEEKS = 20.0
ENV_PRIOR_POINTS = 27.0
ENV_PRIOR_GAMES = 30.0
WEEKS_PER_SEASON = 25
# Days since the team's previous game, capped: a bye helps, a long layoff no more.
REST_RANGE = (5, 14)
DEFAULT_REST = 7

LINE_FIELDS = [c for c in LINE_COLUMNS if c not in ("game_id", "season")]


def rest_days(games: pd.DataFrame) -> pd.DataFrame:
    """Days since each side's previous game in the schedule, capped."""
    sides = pd.concat([
        games[["game_id", "season", "kickoff", "home_team"]].rename(columns={"home_team": "team"}).assign(side="home"),
        games[["game_id", "season", "kickoff", "away_team"]].rename(columns={"away_team": "team"}).assign(side="away"),
    ]).sort_values("kickoff")
    prev = sides.groupby(["season", "team"])["kickoff"].shift()
    sides["rest"] = ((sides["kickoff"] - prev).dt.total_seconds() / 86400).round()
    sides["rest"] = sides["rest"].fillna(DEFAULT_REST).clip(*REST_RANGE)
    out = sides.pivot_table(index="game_id", columns="side", values="rest")
    return out.rename(columns={"home": "home_rest", "away": "away_rest"})


class FeatureBuilder:
    def __init__(self, games: pd.DataFrame, team_games: pd.DataFrame, returning: pd.DataFrame,
                 lines: pd.DataFrame, venues: pd.DataFrame, hp: Hyperparams, qbs: pd.DataFrame | None = None):
        """``qbs``: quarterback-game summaries (``data.summarize_qbs``); without them the
        quarterback adjustment is zero."""
        self.hp = hp
        self.qb = QBModel(qbs, hp) if qbs is not None and len(qbs) else None
        self.members = members_from(team_games, games)
        self.engines = {}
        for name, target in targets(hp).items():
            rows = prepare_rows(team_games, target)
            priors = PriorModel(rows, target, returning if name == "epa" else None, self.members)
            self.engines[name] = RatingsEngine(rows, target, hp.half_life_weeks, priors, self.members)
        elo, self.elo_ratings = run_elo(games)
        self.elo = elo.set_index("game_id")
        lines = lines.drop_duplicates("game_id").set_index("game_id")[LINE_FIELDS]
        g = games.join(lines, on="game_id")
        g = g.join(rest_days(games), on="game_id")
        self.games = pd.concat([g, travel_features(g, venues)], axis=1)
        done = games[games["completed"] & games["home_division"].eq("fbs") & games["away_division"].eq("fbs")]
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

    def _rows(self, games: pd.DataFrame, ratings: dict[str, Ratings], season: int, week: int) -> pd.DataFrame:
        out = games.copy()
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
        out["fcs_gap"] = main.fcs_gap
        out["env_points"] = self.scoring_environment(season, week)
        out = out.join(self.elo, on="game_id")
        if self.qb is not None:
            out = out.join(self.qb.adjustments(games, season, week))
        return out

    def walk_forward(self, seasons) -> pd.DataFrame:
        """Features for every game in ``seasons``, each built from earlier weeks only."""
        frames = []
        for season in seasons:
            season_games = self.games[self.games["season"] == season]
            for week, week_games in season_games.groupby("week"):
                frames.append(self._rows(week_games, self.ratings(season, week), season, week))
        return pd.concat(frames, ignore_index=True) if frames else pd.DataFrame()

    def current(self, game_ids, season: int) -> tuple[pd.DataFrame, dict[str, Ratings]]:
        """Features for upcoming games from every game played so far this season."""
        cutoff = int(self._summary_weeks.get(season, 0)) + 1
        ratings = self.ratings(season, cutoff)
        games = self.games[self.games["game_id"].isin(set(game_ids))]
        return self._rows(games, ratings, season, cutoff), ratings
