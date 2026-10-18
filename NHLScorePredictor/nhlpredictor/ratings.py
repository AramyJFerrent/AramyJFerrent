"""Opponent-adjusted offensive and defensive ratings.

Each team-game contributes one observation per rated measure, modeled as

    value = league level + offense rating + opposing defense rating + home edge

and fitted by weighted ridge regression. The ridge pulls every rating toward a
preseason prior (last season's final rating, regressed hard toward average,
since team strength carries over less in hockey than in any other major league)
with a strength measured in the rating's own units, so the prior dominates the
first weeks and fades as games accumulate. Recent games count more through an
exponential decay in days. Positive offense is good; positive defense is bad
(it allows more).

The rated measures:

- ``ev``: 5-on-5 expected goals per 60 minutes, score-and-venue adjusted.
- ``pp``: power-play expected goals per 60 power-play minutes (defense is the
  opponent's penalty kill).
- ``draw``: power-play minutes per game (offense draws penalties, defense takes them).
- ``goals``: regulation goals per game with both goalies in. Actual goals
  carry finishing and goaltending that xG misses, so this is shrunk the hardest.

Fits for every day of a season come from running sums: the recency weight
``0.5 ** ((ref - day) / half_life)`` factors into a part that depends only on
the game day and one that depends only on the reference day.
"""

from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np
import pandas as pd

from .config import Hyperparams

# The league level and home edge are nearly free parameters; these only keep
# them stable when a season has just a handful of games (in each target's units).
LEAGUE_PRIOR_GAMES = 2.0
HOME_PRIOR_GAMES = 200.0
DRAW_PRIOR_GAMES = 25.0


@dataclass
class Ratings:
    off: dict[str, float] = field(default_factory=dict)
    deff: dict[str, float] = field(default_factory=dict)
    mu: float = 0.0
    hfa: float = 0.0

    def regressed(self, keep: float) -> "Ratings":
        return Ratings(off={t: v * keep for t, v in self.off.items()},
                       deff={t: v * keep for t, v in self.deff.items()}, mu=self.mu, hfa=self.hfa)

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

    ``value`` is a team-game column and ``weight`` the matching exposure column
    (minutes), so the rated quantity is ``value / weight * per``; with no weight
    column the value is used per game. Prior strengths are in the weight's units.
    """

    name: str
    value: str
    weight: str | None
    per: float
    prior: float
    keep: float
    unit: float  # weight units per game, to express the league and home priors

    @property
    def league_prior(self) -> float:
        return LEAGUE_PRIOR_GAMES * self.unit

    @property
    def home_prior(self) -> float:
        return HOME_PRIOR_GAMES * self.unit


def targets(hp: Hyperparams) -> dict[str, Target]:
    return {
        "ev": Target("ev", "xgf_ev", "toi_ev", 60.0, hp.ev_prior_minutes, hp.carryover, 48.0),
        "pp": Target("pp", "xgf_pp", "toi_pp", 60.0, hp.pp_prior_minutes, hp.carryover, 5.0),
        "draw": Target("draw", "toi_pp", None, 1.0, DRAW_PRIOR_GAMES, hp.carryover, 1.0),
        "goals": Target("goals", "reg_gf", None, 1.0, hp.goals_prior_games, hp.carryover, 1.0),
    }


def season_day(dates: pd.Series, season: int) -> np.ndarray:
    """Days since August 1 before the season, from ISO date strings or dates."""
    origin = pd.Timestamp(f"{season - 1}-08-01")
    return (pd.to_datetime(dates) - origin).dt.days.to_numpy()


def prepare_rows(team_games: pd.DataFrame, games: pd.DataFrame, target: Target) -> pd.DataFrame:
    """Team-game rows with the rated value, its weight, a home indicator and the day."""
    neutral = set(games.loc[games["neutral"], "game_id"])
    if target.weight:
        rows = team_games[team_games[target.weight] > 0].copy()
        rows["y"] = rows[target.value] / rows[target.weight] * target.per
        rows["w"] = rows[target.weight].astype(float)
    else:
        rows = team_games.copy()
        rows["y"] = rows[target.value].astype(float) * target.per
        rows["w"] = 1.0
    rows["h"] = np.where(rows["game_id"].isin(neutral), 0.0, np.where(rows["home"] == 1, 1.0, -1.0))
    rows = rows[rows["y"].notna()]
    rows["day"] = 0
    for season, idx in rows.groupby("season").groups.items():
        rows.loc[idx, "day"] = season_day(rows.loc[idx, "date"], season)
    return rows[["game_id", "season", "day", "team", "opp", "h", "y", "w"]].reset_index(drop=True)


class SeasonSums:
    """Running ridge sums for one season, so a fit for any day is one solve."""

    def __init__(self, rows: pd.DataFrame, teams: list[str], half_life: float):
        self.teams = teams
        self.index = {t: i for i, t in enumerate(teams)}
        n = len(teams)
        self.n_params = 2 + 2 * n
        self.half_life = half_life
        self.days = np.sort(rows["day"].unique()) if len(rows) else np.zeros(0, dtype=int)
        k = len(self.days)
        A = np.zeros((k + 1, self.n_params, self.n_params))
        b = np.zeros((k + 1, self.n_params))
        if len(rows):
            slot = np.searchsorted(self.days, rows["day"].to_numpy()) + 1
            scale = rows["w"].to_numpy() * 2.0 ** (rows["day"].to_numpy() / half_life)
            idx = np.column_stack([np.zeros(len(rows), dtype=int), np.ones(len(rows), dtype=int),
                                   2 + rows["team"].map(self.index).to_numpy(),
                                   2 + n + rows["opp"].map(self.index).to_numpy()])
            val = np.column_stack([np.ones(len(rows)), rows["h"].to_numpy(), np.ones(len(rows)), np.ones(len(rows))])
            y = rows["y"].to_numpy()
            for i in range(4):
                np.add.at(b, (slot, idx[:, i]), scale * val[:, i] * y)
                for j in range(4):
                    np.add.at(A, (slot, idx[:, i], idx[:, j]), scale * val[:, i] * val[:, j])
            A = np.cumsum(A, axis=0)
            b = np.cumsum(b, axis=0)
        self.A, self.b = A, b

    def solve(self, day: float, prior: "Ratings", target: Target) -> Ratings:
        """Ratings from games before ``day``, with recency measured from ``day``."""
        k = int(np.searchsorted(self.days, day, side="left"))
        n = len(self.teams)
        lam = np.concatenate([[target.league_prior, target.home_prior], np.full(2 * n, target.prior)])
        beta0 = np.concatenate([[prior.mu, prior.hfa], [prior.off.get(t, 0.0) for t in self.teams],
                                [prior.deff.get(t, 0.0) for t in self.teams]])
        c = 2.0 ** (-day / self.half_life)
        beta = np.linalg.solve(np.diag(lam) + c * self.A[k], lam * beta0 + c * self.b[k])
        return Ratings(off={t: float(beta[2 + i]) for t, i in self.index.items()},
                       deff={t: float(beta[2 + n + i]) for t, i in self.index.items()},
                       mu=float(beta[0]), hfa=float(beta[1]))


class RatingsEngine:
    """Fits ratings for any day of any season, chaining preseason priors."""

    def __init__(self, rows: pd.DataFrame, target: Target, half_life_days: float):
        self.target = target
        self.half_life = half_life_days
        self.by_season = {s: r.reset_index(drop=True) for s, r in rows.groupby("season")}
        self.first_season = min(self.by_season) if self.by_season else None
        self._sums: dict[int, SeasonSums] = {}
        self._final: dict[int, Ratings] = {}

    def _league_start(self) -> Ratings:
        rows = self.by_season.get(self.first_season)
        if rows is None or rows.empty:
            return Ratings()
        return Ratings(mu=float(np.average(rows["y"], weights=rows["w"])))

    def prior(self, season: int) -> Ratings:
        if self.first_season is None or season - 1 < self.first_season:
            return self._league_start()
        return self.final(season - 1).regressed(self.target.keep)

    def sums(self, season: int) -> SeasonSums:
        if season not in self._sums:
            rows = self.by_season.get(season, pd.DataFrame(columns=["day", "team", "opp", "h", "y", "w"]))
            teams = sorted(set(self.prior(season).off) | set(rows["team"]) | set(rows["opp"]))
            self._sums[season] = SeasonSums(rows, teams, self.half_life)
        return self._sums[season]

    def final(self, season: int) -> Ratings:
        if season not in self._final:
            sums = self.sums(season)
            ref = float(sums.days.max() + 1) if len(sums.days) else 1.0
            self._final[season] = sums.solve(ref, self.prior(season), self.target)
        return self._final[season]

    def before(self, season: int, day: float) -> Ratings:
        """Ratings using only ``season`` games played before ``day``."""
        return self.sums(season).solve(day, self.prior(season), self.target)
