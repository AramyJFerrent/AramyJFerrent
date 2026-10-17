"""Opponent-adjusted offensive and defensive efficiency ratings.

Each team-game contributes the offense's EPA per play, modeled as

    EPA/play = league level + offense rating + opposing defense rating + home edge

and fitted by weighted ridge regression. The ridge pulls every rating toward a
preseason prior (last season's final rating, partly regressed to average) with
a strength measured in plays, so the prior dominates early in the season and
fades as games accumulate. Recent games count more through an exponential
decay. Ratings are in EPA per play: positive offense is good, positive defense
is bad (it allows more).
"""

from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np
import pandas as pd

from .config import Hyperparams

# The league level and home edge are nearly free parameters; these only keep
# them stable when a season has just a handful of games.
LEAGUE_PRIOR_PLAYS = 50.0
HOME_PRIOR_PLAYS = 3000.0
DEFAULT_HOME_EPA = 0.02


@dataclass
class Ratings:
    off: dict[str, float] = field(default_factory=dict)
    deff: dict[str, float] = field(default_factory=dict)
    mu: float = 0.0
    hfa: float = DEFAULT_HOME_EPA
    plays: dict[str, float] = field(default_factory=dict)

    def regressed(self, off_keep: float, def_keep: float) -> "Ratings":
        return Ratings(
            off={t: v * off_keep for t, v in self.off.items()},
            deff={t: v * def_keep for t, v in self.deff.items()},
            mu=self.mu, hfa=self.hfa,
        )

    def table(self) -> pd.DataFrame:
        teams = sorted(set(self.off) | set(self.deff))
        return pd.DataFrame({
            "team": teams,
            "off": [self.off.get(t, 0.0) for t in teams],
            "def": [self.deff.get(t, 0.0) for t in teams],
            "net": [self.off.get(t, 0.0) - self.deff.get(t, 0.0) for t in teams],
        }).sort_values("net", ascending=False, ignore_index=True)


@dataclass(frozen=True)
class Target:
    """One measure to rate offenses and defenses on.

    ``value`` is a team-game column summed over plays and ``weight`` the
    matching play weight, so the rated quantity is value per play; with no
    weight column the value is used per game. Prior strengths are in the same
    units as the weight (plays, or games).
    """

    name: str
    value: str
    weight: str | None
    off_prior: float
    def_prior: float
    off_keep: float
    def_keep: float
    league_prior: float = LEAGUE_PRIOR_PLAYS
    home_prior: float = HOME_PRIOR_PLAYS


def targets(hp: Hyperparams) -> dict[str, Target]:
    """The main EPA rating and the special-teams rating.

    Special teams (kickoffs, punts, field goals and extra points, as net EPA
    per game) are noisy week to week, so they are pulled hard toward the prior.
    In walk-forward tests they were the one extra rating that the betting
    market underweights: picks with it covered 53.7% against midweek lines.
    Separate passing and rushing, success-rate and pace ratings were tried and
    did not hold up out of sample.
    """
    per_game = 60.0  # plays per game, to express the home prior in games
    return {
        "epa": Target("epa", "epa", "w", hp.off_prior_plays, hp.def_prior_plays,
                      hp.off_carryover, hp.def_carryover),
        "st": Target("st", "st_epa", None, 12.0, 12.0, 0.5, 0.5,
                     league_prior=1.0, home_prior=HOME_PRIOR_PLAYS / per_game),
    }


def prepare_rows(team_games: pd.DataFrame, games: pd.DataFrame, target: Target) -> pd.DataFrame:
    """Team-game rows with the rated value, its weight and a home indicator."""
    neutral = set(games.loc[games["neutral"], "game_id"])
    if target.weight:
        rows = team_games[team_games[target.weight] > 0].copy()
        rows["y"] = rows[target.value] / rows[target.weight]
        rows["w"] = rows[target.weight]
    else:
        rows = team_games[team_games["plays"] > 0].copy()
        rows["y"] = rows[target.value].astype(float)
        rows["w"] = 1.0
    rows["h"] = np.where(rows["game_id"].isin(neutral), 0.0, np.where(rows["home"] == 1, 1.0, -1.0))
    rows = rows[rows["y"].notna()]  # summaries written before a column existed
    return rows[["game_id", "season", "week", "team", "opp", "h", "y", "w"]].reset_index(drop=True)


def fit(rows: pd.DataFrame, ref_week: float, prior: Ratings, target: Target,
        half_life_weeks: float) -> Ratings:
    """Ridge fit of one season's rows toward ``prior``."""
    seen = set(rows["team"]) | set(rows["opp"]) if len(rows) else set()
    teams = sorted(set(prior.off) | seen)
    index = {t: i for i, t in enumerate(teams)}
    n_teams = len(teams)
    n_params = 2 + 2 * n_teams

    lam = np.concatenate([[target.league_prior, target.home_prior],
                          np.full(n_teams, target.off_prior), np.full(n_teams, target.def_prior)])
    beta0 = np.concatenate([[prior.mu, prior.hfa],
                            [prior.off.get(t, 0.0) for t in teams],
                            [prior.deff.get(t, 0.0) for t in teams]])
    A = np.diag(lam)
    b = lam * beta0
    plays = {t: 0.0 for t in teams}
    if len(rows):
        n = len(rows)
        X = np.zeros((n, n_params))
        X[:, 0] = 1.0
        X[:, 1] = rows["h"].to_numpy()
        X[np.arange(n), 2 + rows["team"].map(index).to_numpy()] = 1.0
        X[np.arange(n), 2 + n_teams + rows["opp"].map(index).to_numpy()] = 1.0
        recency = 0.5 ** ((ref_week - rows["week"].to_numpy()) / half_life_weeks)
        wts = rows["w"].to_numpy() * recency
        Xw = X * wts[:, None]
        A = A + Xw.T @ X
        b = b + Xw.T @ rows["y"].to_numpy()
        for team, weight in pd.Series(wts).groupby(rows["team"].to_numpy()).sum().items():
            plays[team] = float(weight)
    beta = np.linalg.solve(A, b)
    return Ratings(
        off={t: float(beta[2 + i]) for t, i in index.items()},
        deff={t: float(beta[2 + n_teams + i]) for t, i in index.items()},
        mu=float(beta[0]), hfa=float(beta[1]), plays=plays,
    )


class RatingsEngine:
    """Fits ratings for any point in any season, chaining preseason priors."""

    def __init__(self, rows: pd.DataFrame, target: Target, half_life_weeks: float):
        self.target = target
        self.half_life_weeks = half_life_weeks
        self.by_season = {s: r.reset_index(drop=True) for s, r in rows.groupby("season")}
        self.first_season = min(self.by_season) if self.by_season else None
        self._final: dict[int, Ratings] = {}

    def _fit(self, rows, ref_week, prior) -> Ratings:
        return fit(rows, ref_week, prior, self.target, self.half_life_weeks)

    def prior(self, season: int) -> Ratings:
        if self.first_season is None or season - 1 < self.first_season:
            return Ratings(hfa=DEFAULT_HOME_EPA if self.target.weight else 0.0)
        return self.final(season - 1).regressed(self.target.off_keep, self.target.def_keep)

    def final(self, season: int) -> Ratings:
        if season not in self._final:
            rows = self.by_season.get(season, pd.DataFrame(columns=["week"]))
            ref = rows["week"].max() + 1 if len(rows) else 1
            self._final[season] = self._fit(rows, ref, self.prior(season))
        return self._final[season]

    def before(self, season: int, week: int, ref_week: float | None = None) -> Ratings:
        """Ratings using only ``season`` games played before ``week``."""
        rows = self.by_season.get(season)
        rows = rows[rows["week"] < week] if rows is not None else pd.DataFrame(columns=["week"])
        return self._fit(rows, week if ref_week is None else ref_week, self.prior(season))
