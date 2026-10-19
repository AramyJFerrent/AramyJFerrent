"""Team offense and run-prevention ratings from runs scored.

The player ratings price each lineup, starter and bullpen, but some of what
wins games sits between the players: fielding, baserunning, catcher framing,
how a staff is managed. These team ratings catch it. Each team-game is one
observation of

    runs in innings 1-8 = league level + offense + opposing defense + home edge

fitted by weighted ridge regression, with every team pulled toward a
preseason prior (a share of last season's final rating) and recent games
counting more. Positive offense is good; positive defense is bad (it allows
more). The run model decides how much weight they get next to the player
ratings.

Fits for every day of a season come from running sums: the recency weight
``0.5 ** ((ref - day) / half_life)`` factors into a part that depends only on
the game day and one that depends only on the reference day.
"""

from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np
import pandas as pd

LEAGUE_PRIOR_GAMES = 2.0
HOME_PRIOR_GAMES = 400.0


@dataclass
class Ratings:
    off: dict[str, float] = field(default_factory=dict)
    deff: dict[str, float] = field(default_factory=dict)
    mu: float = 0.0
    hfa: float = 0.0

    def regressed(self, keep: float) -> "Ratings":
        return Ratings(off={t: v * keep for t, v in self.off.items()},
                       deff={t: v * keep for t, v in self.deff.items()}, mu=self.mu, hfa=self.hfa)


def season_day(dates, season: int) -> np.ndarray:
    """Days since March 1 of the season."""
    return (pd.to_datetime(pd.Series(dates).reset_index(drop=True)) - pd.Timestamp(f"{season}-03-01")).dt.days.to_numpy()


def team_rows(games: pd.DataFrame) -> pd.DataFrame:
    """One row per team per finished game: runs in the innings both teams bat, per eight innings."""
    g = games[games["completed"]]
    rows = []
    for side, other in (("home", "away"), ("away", "home")):
        n = (g["sched_innings"] - 1).to_numpy()
        runs = [sum(int(v) for v in str(line).split()[:k] if v != "x") for line, k in zip(g[f"{side}_line"], n)]
        rows.append(pd.DataFrame({"season": g["season"].to_numpy(), "date": g["date"].to_numpy(),
                                  "team": g[f"{side}_team"].to_numpy(), "opp": g[f"{other}_team"].to_numpy(),
                                  "h": np.where(g["neutral"], 0.0, 1.0 if side == "home" else -1.0),
                                  "y": np.asarray(runs, dtype=float) * 8.0 / n, "w": n / 8.0}))
    out = pd.concat(rows, ignore_index=True)
    out["day"] = 0
    for season, idx in out.groupby("season").groups.items():
        out.loc[idx, "day"] = season_day(out.loc[idx, "date"], season)
    return out


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

    def solve(self, day: float, prior: Ratings, strength: float) -> Ratings:
        """Ratings from games before ``day``, with recency measured from ``day``."""
        k = int(np.searchsorted(self.days, day, side="left"))
        n = len(self.teams)
        lam = np.concatenate([[LEAGUE_PRIOR_GAMES, HOME_PRIOR_GAMES], np.full(2 * n, strength)])
        beta0 = np.concatenate([[prior.mu, prior.hfa], [prior.off.get(t, 0.0) for t in self.teams],
                                [prior.deff.get(t, 0.0) for t in self.teams]])
        c = 2.0 ** (-day / self.half_life)
        beta = np.linalg.solve(np.diag(lam) + c * self.A[k], lam * beta0 + c * self.b[k])
        return Ratings(off={t: float(beta[2 + i]) for t, i in self.index.items()},
                       deff={t: float(beta[2 + n + i]) for t, i in self.index.items()},
                       mu=float(beta[0]), hfa=float(beta[1]))


class TeamRatings:
    """Team ratings for any day of any season, chaining preseason priors."""

    def __init__(self, games: pd.DataFrame, prior_games: float, carryover: float, half_life: float):
        rows = team_rows(games)
        self.prior_games = prior_games
        self.carryover = carryover
        self.half_life = half_life
        self.by_season = {s: r.reset_index(drop=True) for s, r in rows.groupby("season")}
        self.first_season = min(self.by_season) if self.by_season else None
        self.teams = sorted(set(rows["team"]) | set(rows["opp"]))
        self._sums: dict[int, SeasonSums] = {}
        self._final: dict[int, Ratings] = {}

    def prior(self, season: int) -> Ratings:
        if self.first_season is None or season - 1 < self.first_season:
            rows = self.by_season.get(self.first_season)
            return Ratings(mu=float(np.average(rows["y"], weights=rows["w"]))) if rows is not None else Ratings()
        return self.final(season - 1).regressed(self.carryover)

    def sums(self, season: int) -> SeasonSums:
        if season not in self._sums:
            rows = self.by_season.get(season, pd.DataFrame(columns=["day", "team", "opp", "h", "y", "w"]))
            self._sums[season] = SeasonSums(rows, self.teams, self.half_life)
        return self._sums[season]

    def final(self, season: int) -> Ratings:
        if season not in self._final:
            sums = self.sums(season)
            ref = float(sums.days.max() + 1) if len(sums.days) else 1.0
            self._final[season] = sums.solve(ref, self.prior(season), self.prior_games)
        return self._final[season]

    def before(self, season: int, date) -> Ratings:
        """Ratings using only ``season`` games played before ``date``."""
        day = float(season_day([date], season)[0])
        return self.sums(season).solve(day, self.prior(season), self.prior_games)
