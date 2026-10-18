"""Betting lines: remove the margin, back out the market's goal rates, blend.

Hockey markets price the winner (moneyline, overtime and shootout included)
and the total, not a point spread, so the market's expected score has to be
backed out of the prices. The inverter simulates a grid of home and away goal
rates with the same simulator as the model, then finds for each game the pair
of rates whose win probability matches the de-vigged moneyline and whose
chance of going over matches the de-vigged total. Those rates are in the
model's own units, ready to blend:

    rate = w * model rate + (1 - w) * market rate

The weight ``w`` is fitted on logged games that had a line (Poisson
likelihood of each team's goals), shrunk toward an even split until a few
hundred such games have been played.
"""

from __future__ import annotations

import numpy as np
import pandas as pd
from scipy.interpolate import RectBivariateSpline
from scipy.stats import poisson

from .simulate import SimParams, simulate

GRID = np.round(np.arange(1.0, 5.01, 0.2), 2)
FINE = np.round(np.arange(1.0, 5.0001, 0.02), 3)
TOTAL_LINES = (4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5)
# Blend prior: an even split, worth this many games of evidence.
PRIOR_WEIGHT = 0.5
PRIOR_GAMES = 400.0


def implied_prob(american) -> np.ndarray:
    ml = np.asarray(american, dtype=float)
    with np.errstate(divide="ignore", invalid="ignore"):
        return np.where(ml < 0, -ml / (-ml + 100.0), 100.0 / (ml + 100.0))


def devig(price_a, price_b) -> np.ndarray:
    """Probability of side A from two American prices, with the margin removed."""
    a, b = implied_prob(price_a), implied_prob(price_b)
    with np.errstate(divide="ignore", invalid="ignore"):
        return a / (a + b)


class MarketInverter:
    def __init__(self, params: SimParams, n_sims: int = 2000, seed: int = 11):
        hh, aa = np.meshgrid(GRID, GRID, indexing="ij")
        sim = simulate(hh.ravel(), aa.ravel(), params, n_sims=n_sims, seed=seed)
        home_win = (sim["home"] > sim["away"]).mean(axis=1).reshape(hh.shape)
        total = sim["home"] + sim["away"]
        self.win = RectBivariateSpline(GRID, GRID, home_win)(FINE, FINE)
        self.over = {}
        for line in TOTAL_LINES:
            p = ((total > line).mean(axis=1) + 0.5 * (total == line).mean(axis=1)).reshape(hh.shape)
            self.over[line] = RectBivariateSpline(GRID, GRID, p)(FINE, FINE)

    def invert(self, p_home: float, total_line: float, p_over: float) -> tuple[float, float]:
        """Home and away goal rates matching a win probability and an over probability."""
        if np.isnan(p_home) or np.isnan(total_line) or float(total_line) not in self.over:
            return np.nan, np.nan
        p_over = 0.5 if np.isnan(p_over) else p_over
        err = (self.win - p_home) ** 2 + (self.over[float(total_line)] - p_over) ** 2
        i, j = np.unravel_index(int(np.argmin(err)), err.shape)
        return float(FINE[i]), float(FINE[j])

    def rates(self, lines: pd.DataFrame) -> pd.DataFrame:
        """Market goal rates for rows with moneylines and a total (NaN otherwise)."""
        p_home = devig(lines["home_moneyline"], lines["away_moneyline"])
        p_over = devig(lines["over_price"], lines["under_price"])
        pairs = [self.invert(ph, tl, po) for ph, tl, po in zip(p_home, lines["total_line"].astype(float), p_over)]
        return pd.DataFrame({"market_home_rate": [p[0] for p in pairs],
                             "market_away_rate": [p[1] for p in pairs],
                             "market_home_prob": p_home}, index=lines.index)


def fit_blend(model_home, model_away, market_home, market_away, goals_home, goals_away) -> tuple[float, int]:
    """Weight on the model's rates that best predicted each team's goals, shrunk
    toward an even split. Returns the weight and the number of games behind it."""
    arrays = [np.asarray(x, dtype=float) for x in (model_home, model_away, market_home, market_away,
                                                   goals_home, goals_away)]
    ok = np.all([~np.isnan(a) for a in arrays], axis=0)
    mh, ma, kh, ka, gh, ga = (a[ok] for a in arrays)
    n = int(ok.sum())
    if n == 0:
        return PRIOR_WEIGHT, 0
    weights = np.linspace(0.0, 1.0, 101)
    nll = [-(poisson.logpmf(gh, w * mh + (1 - w) * kh) + poisson.logpmf(ga, w * ma + (1 - w) * ka)).sum()
           for w in weights]
    best = float(weights[int(np.argmin(nll))])
    return (n * best + PRIOR_GAMES * PRIOR_WEIGHT) / (n + PRIOR_GAMES), n
