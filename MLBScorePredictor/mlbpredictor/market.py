"""Betting lines: remove the margin, back out the market's expected runs, blend.

Baseball markets price the winner (moneyline) and the total; the market's
expected score has to be backed out of those prices. The inverter simulates
a grid of home and away run levels (expected runs over nine innings, spread
across innings like an average game) with the same simulator as the model,
then finds for each game the pair whose win probability matches the
de-vigged moneyline and whose chance of going over matches the de-vigged
total. The two views are blended on the log scale, as the techniques report
recommends:

    log runs = w × log model runs + (1 − w) × log market runs

and the model's own inning-by-inning profile is scaled to the blended level.
The weight ``w`` is fitted by Poisson likelihood of each team's runs in
innings 1-8, on Pinnacle's 2016 closing lines in the backtest and on logged
live games as they accumulate, shrunk toward the backtest value until a few
hundred live games exist.
"""

from __future__ import annotations

import numpy as np
import pandas as pd
from scipy.interpolate import RectBivariateSpline
from scipy.stats import poisson

from .edges import implied_prob
from .simulate import TOTAL_LINES, SimParams, simulate

GRID = np.round(np.arange(2.0, 8.01, 0.25), 2)
FINE = np.round(np.arange(2.0, 8.0001, 0.02), 3)
# Weight on the model when no fitted value exists, worth this many games.
PRIOR_WEIGHT = 0.3
PRIOR_GAMES = 400.0


def devig(price_a, price_b) -> np.ndarray:
    """Probability of side A from two American prices, with the margin removed."""
    a, b = implied_prob(price_a), implied_prob(price_b)
    with np.errstate(divide="ignore", invalid="ignore"):
        return a / (a + b)


class MarketInverter:
    def __init__(self, params: SimParams, profile: np.ndarray, ghost: bool = True, n_sims: int = 8000,
                 seed: int = 11):
        """``profile``: each inning's share of nine-inning runs (innings 1-9),
        the last also used for extra innings."""
        profile = np.asarray(profile, dtype=float) / np.sum(profile)
        hh, aa = np.meshgrid(GRID, GRID, indexing="ij")
        h9, a9 = hh.ravel(), aa.ravel()
        sim = simulate(h9[:, None] * profile, a9[:, None] * profile, h9 * profile[-1], a9 * profile[-1], params,
                       n_sims=n_sims, ghost=ghost, seed=seed)
        home_win = (sim["home"] > sim["away"]).mean(axis=1).reshape(hh.shape)
        total = sim["home"] + sim["away"]
        self.win = RectBivariateSpline(GRID, GRID, home_win)(FINE, FINE)
        self.over = {}
        for line in TOTAL_LINES:
            p = ((total > line).mean(axis=1) + 0.5 * (total == line).mean(axis=1)).reshape(hh.shape)
            self.over[float(line)] = RectBivariateSpline(GRID, GRID, p)(FINE, FINE)

    def invert(self, p_home: float, total_line: float, p_over: float) -> tuple[float, float]:
        """Home and away nine-inning run levels matching a win probability and an over probability."""
        if np.isnan(p_home) or np.isnan(total_line) or float(total_line) not in self.over:
            return np.nan, np.nan
        p_over = 0.5 if np.isnan(p_over) else p_over
        err = (self.win - p_home) ** 2 + (self.over[float(total_line)] - p_over) ** 2
        i, j = np.unravel_index(int(np.argmin(err)), err.shape)
        return float(FINE[i]), float(FINE[j])

    def rates(self, lines: pd.DataFrame) -> pd.DataFrame:
        """Market run levels for rows with moneylines and a total (NaN otherwise)."""
        p_home = devig(lines["home_moneyline"], lines["away_moneyline"])
        p_over = devig(lines["over_price"], lines["under_price"])
        pairs = [self.invert(ph, tl, po) for ph, tl, po in zip(p_home, lines["total_line"].astype(float), p_over)]
        return pd.DataFrame({"market_home_runs": [p[0] for p in pairs], "market_away_runs": [p[1] for p in pairs],
                             "market_home_prob": p_home}, index=lines.index)


def blend(model: np.ndarray, market: np.ndarray, weight: float) -> np.ndarray:
    """Log-scale blend; the model alone where there is no market number."""
    model, market = np.asarray(model, dtype=float), np.asarray(market, dtype=float)
    mixed = np.exp(weight * np.log(model) + (1 - weight) * np.log(np.where(np.isnan(market), model, market)))
    return np.where(np.isnan(market), model, mixed)


def fit_blend(model_home, model_away, market_home, market_away, runs_home, runs_away,
              share8: float = 8.0 / 9.0, prior: float = PRIOR_WEIGHT,
              prior_games: float = PRIOR_GAMES) -> tuple[float, float, int]:
    """Weight on the model's run levels that best predicted each team's runs in
    innings 1-8 (Poisson likelihood), and the same shrunk toward ``prior``.
    Returns the raw fit, the shrunk weight and the number of games behind it."""
    arrays = [np.asarray(x, dtype=float) for x in (model_home, model_away, market_home, market_away,
                                                   runs_home, runs_away)]
    ok = np.all([np.isfinite(a) for a in arrays], axis=0)
    mh, ma, kh, ka, rh, ra = (a[ok] for a in arrays)
    n = int(ok.sum())
    if n == 0:
        return float("nan"), prior, 0
    weights = np.linspace(0.0, 1.0, 101)
    nll = []
    for w in weights:
        lh, la = blend(mh, kh, w) * share8, blend(ma, ka, w) * share8
        scale = (rh.sum() + ra.sum()) / (lh.sum() + la.sum())
        nll.append(-(poisson.logpmf(rh, lh * scale) + poisson.logpmf(ra, la * scale)).sum())
    best = float(weights[int(np.argmin(nll))])
    return best, (n * best + prior_games * prior) / (n + prior_games), n
