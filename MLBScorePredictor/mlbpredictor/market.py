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
from bettingcore import anchored, devig, market_chance, no_push, with_push
from scipy.interpolate import RectBivariateSpline
from scipy.stats import poisson

from .simulate import TOTAL_LINES, SimParams, line_probs, simulate

GRID = np.round(np.arange(2.0, 8.01, 0.25), 2)
FINE = np.round(np.arange(2.0, 8.0001, 0.02), 3)
# Weight on the model when no fitted value exists, worth this many games.
PRIOR_WEIGHT = 0.3
PRIOR_GAMES = 400.0
# Each side's chance against the posted lines, anchored to the market's (see
# ``edge_chances``), which the betting edges use.
EDGE_PROBS = ["edge_home_ml_prob", "edge_home_cover_prob", "edge_away_cover_prob", "edge_over_prob",
              "edge_under_prob", "edge_total_push_prob"]


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


def edge_chances(f: pd.DataFrame, pred: pd.DataFrame, sim: dict, ref: pd.DataFrame, ref_sim: dict,
                 run_line) -> pd.DataFrame:
    """Each side's chance against the posted lines, anchored to the market (``bettingcore.anchor``).

    ``pred``/``sim`` are the final (blended) prediction, ``ref``/``ref_sim``
    the same simulation (same seed) at the market's own run levels. Each side
    gets the market's de-vigged chance plus the difference between the two, so
    only what the blend moved off the market can make an edge, whatever the
    simulator's shape. A total without prices counts as an even -110 market;
    run lines and moneylines need prices.
    """
    def col(name):
        return f[name].to_numpy(float) if name in f else np.full(len(f), np.nan)

    total = col("total_line")
    p, r = line_probs(sim, run_line, total), line_probs(ref_sim, run_line, total)
    win = anchored(market_chance(col("home_moneyline"), col("away_moneyline"), default=np.nan),
                   pred["home_win_prob"].to_numpy(float), ref["home_win_prob"].to_numpy(float))
    cover = anchored(market_chance(col("home_run_line_price"), col("away_run_line_price"), default=np.nan),
                     no_push(p["model_home_cover_prob"], 1 - p["model_home_cover_prob"] - p["model_away_cover_prob"]),
                     no_push(r["model_home_cover_prob"], 1 - r["model_home_cover_prob"] - r["model_away_cover_prob"]))
    over = anchored(market_chance(col("over_price"), col("under_price")),
                    no_push(p["model_over_prob"], p["model_total_push_prob"]),
                    no_push(r["model_over_prob"], r["model_total_push_prob"]))
    push = p["model_total_push_prob"].to_numpy(float)
    rl_push = (1 - p["model_home_cover_prob"] - p["model_away_cover_prob"]).to_numpy(float)
    return pd.DataFrame({
        "edge_home_ml_prob": win,
        "edge_home_cover_prob": with_push(cover, rl_push), "edge_away_cover_prob": with_push(1 - cover, rl_push),
        "edge_over_prob": with_push(over, push), "edge_under_prob": with_push(1 - over, push),
        "edge_total_push_prob": push,
    }, index=f.index)
