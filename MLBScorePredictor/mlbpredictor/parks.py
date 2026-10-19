"""Park factors for runs and for each plate-appearance outcome.

For each season the factors come from the seasons before it (three by
default), so a season is never adjusted with its own results. Each factor is a
Poisson regression of a team-game count (runs, or strikeouts, walks, home
runs and so on per plate appearance) on the batting team, the fielding team,
the park and home field, with the park effects pulled toward neutral by a
ridge penalty worth ``park_prior_games`` games. A park with a long record keeps
nearly its raw factor; a new park or a one-off neutral site stays close to 1.
"""

from __future__ import annotations

import logging

import numpy as np
import pandas as pd

from .config import Hyperparams

log = logging.getLogger(__name__)

COMPONENTS = ["k", "bb", "hbp", "s", "d", "t", "hr"]
FACTORS = ["runs"] + COMPONENTS
TEAM_RIDGE = 1.0


def fit_poisson(X: np.ndarray, y: np.ndarray, offset: np.ndarray, penalty: np.ndarray,
                iters: int = 50) -> np.ndarray:
    """Poisson regression with a log link and a ridge penalty per coefficient,
    by iteratively reweighted least squares."""
    beta = np.zeros(X.shape[1])
    beta[0] = np.log(max(y.sum(), 1e-9) / np.exp(offset).sum())
    P = np.diag(penalty)
    for _ in range(iters):
        eta = offset + X @ beta
        mu = np.exp(eta)
        z = eta - offset + (y - mu) / mu
        XtW = (X * mu[:, None]).T
        new = np.linalg.solve(XtW @ X + P, XtW @ z)
        if np.max(np.abs(new - beta)) < 1e-8:
            return new
        beta = new
    return beta


def team_games(games: pd.DataFrame, batting: pd.DataFrame) -> pd.DataFrame:
    """One row per team per finished game: its batting counts, runs in the
    innings both teams always bat, and where it was played."""
    g = games[games["completed"]]
    counts = batting.groupby(["game_id", "team"])[["pa"] + COMPONENTS].sum()
    rows = []
    for side, other in (("home", "away"), ("away", "home")):
        t = pd.DataFrame({"game_id": g["game_id"].to_numpy(), "season": g["season"].to_numpy(),
                          "team": g[f"{side}_team"].to_numpy(), "opp": g[f"{other}_team"].to_numpy(),
                          "park_id": g["park_id"].to_numpy(),
                          "home": np.where(g["neutral"], 0.0, 1.0 if side == "home" else -1.0)})
        lines = g[f"{side}_line"].fillna("").str.split()
        n = (g["sched_innings"] - 1).to_numpy()
        t["innings"] = n
        t["runs"] = [sum(int(v) for v in parts[:k] if v != "x") for parts, k in zip(lines, n)]
        rows.append(t)
    out = pd.concat(rows, ignore_index=True)
    out = out.join(counts, on=["game_id", "team"])
    return out.dropna(subset=["pa"]).reset_index(drop=True)


def fit_factors(tg: pd.DataFrame, prior_games: float) -> pd.DataFrame:
    """Park factors (one column per count) from team-game rows."""
    parks = sorted(tg["park_id"].dropna().unique())
    tg = tg[tg["park_id"].notna()]
    off = pd.Categorical(tg["season"].astype(str) + tg["team"]).codes.astype(int)
    deff = pd.Categorical(tg["season"].astype(str) + tg["opp"]).codes.astype(int)
    n_off, n_def = off.max() + 1, deff.max() + 1
    pk = pd.Categorical(tg["park_id"], categories=parks).codes.astype(int)
    n = len(tg)
    X = np.zeros((n, 2 + n_off + n_def + len(parks)))
    X[:, 0] = 1.0
    X[:, 1] = tg["home"].to_numpy()
    X[np.arange(n), 2 + off] = 1.0
    X[np.arange(n), 2 + n_off + deff] = 1.0
    X[np.arange(n), 2 + n_off + n_def + pk] = 1.0
    penalty = np.concatenate([[0.0, 1.0], np.full(n_off + n_def, TEAM_RIDGE), np.full(len(parks), 0.0)])
    out = {"park_id": parks}
    for name in FACTORS:
        y = tg[name].to_numpy(float)
        exposure = tg["innings"].to_numpy(float) if name == "runs" else tg["pa"].to_numpy(float)
        # A park's ridge is worth ``prior_games`` games of its typical count.
        per_game = y.mean()
        penalty[2 + n_off + n_def:] = prior_games * max(per_game, 1e-3)
        beta = fit_poisson(X, y, np.log(exposure), penalty)
        out[name] = np.exp(beta[2 + n_off + n_def:])
    return pd.DataFrame(out)


class ParkFactors:
    """Factors for every park in every season, each fitted on earlier seasons."""

    def __init__(self, games: pd.DataFrame, batting: pd.DataFrame, hp: Hyperparams):
        self.hp = hp
        self.tg = team_games(games, batting)
        self._by_season: dict[int, pd.DataFrame] = {}

    def season(self, season: int) -> pd.DataFrame:
        if season not in self._by_season:
            past = self.tg[self.tg["season"].between(season - self.hp.park_seasons, season - 1)]
            if past.empty:
                table = pd.DataFrame(columns=["park_id"] + FACTORS)
            else:
                table = fit_factors(past, self.hp.park_prior_games)
            self._by_season[season] = table.set_index("park_id")
        return self._by_season[season]

    def lookup(self, seasons, parks, name: str) -> np.ndarray:
        """Factor ``name`` for each (season, park); 1 for unknown parks."""
        seasons = np.asarray(seasons)
        parks = pd.Series(parks).to_numpy()
        out = np.ones(len(parks))
        for s in np.unique(seasons):
            table = self.season(int(s))
            if table.empty:
                continue
            mask = seasons == s
            out[mask] = pd.Series(parks[mask]).map(table[name]).fillna(1.0).to_numpy()
        return out
