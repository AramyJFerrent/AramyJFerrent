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
likelihood of each team's goals), shrunk toward the weight fitted on
sportsbookreview's archived 2012-13 to 2021-22 closing lines (57% model, see
the backtest) until a few hundred such games have been played.
"""

from __future__ import annotations

import numpy as np
import pandas as pd
from bettingcore import anchored, devig, market_chance, no_push, with_push
from scipy.interpolate import RectBivariateSpline
from scipy.stats import poisson

from .simulate import SimParams, line_probs, simulate

GRID = np.round(np.arange(1.0, 5.01, 0.2), 2)
FINE = np.round(np.arange(1.0, 5.0001, 0.02), 3)
TOTAL_LINES = (4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5)
# Blend prior: the weight fitted on the archived lines in the backtest, worth this many games.
PRIOR_WEIGHT = 0.57
PRIOR_GAMES = 400.0
# Each side's chance against the posted lines, anchored to the market's (see
# ``edge_chances``), which the betting edges use.
EDGE_PROBS = ["edge_home_ml_prob", "edge_home_cover_prob", "edge_away_cover_prob", "edge_spread_push_prob",
              "edge_over_prob", "edge_under_prob", "edge_total_push_prob"]


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


def fit_blend(model_home, model_away, market_home, market_away, goals_home, goals_away,
              prior: float = PRIOR_WEIGHT, prior_games: float = PRIOR_GAMES) -> tuple[float, int]:
    """Weight on the model's rates that best predicted each team's goals, shrunk
    toward ``prior`` with the strength of ``prior_games`` games. Returns the weight
    and the number of games behind it."""
    arrays = [np.asarray(x, dtype=float) for x in (model_home, model_away, market_home, market_away,
                                                   goals_home, goals_away)]
    ok = np.all([~np.isnan(a) for a in arrays], axis=0)
    mh, ma, kh, ka, gh, ga = (a[ok] for a in arrays)
    n = int(ok.sum())
    if n == 0:
        return prior, 0
    weights = np.linspace(0.0, 1.0, 101)
    nll = [-(poisson.logpmf(gh, w * mh + (1 - w) * kh) + poisson.logpmf(ga, w * ma + (1 - w) * ka)).sum()
           for w in weights]
    best = float(weights[int(np.argmin(nll))])
    return (n * best + prior_games * prior) / (n + prior_games), n


def edge_chances(f: pd.DataFrame, pred: pd.DataFrame, sim: dict, ref: pd.DataFrame, ref_sim: dict,
                 home_lines) -> pd.DataFrame:
    """Each side's chance against the posted lines, anchored to the market (``bettingcore.anchor``).

    ``pred``/``sim`` are the final (blended) prediction, ``ref``/``ref_sim``
    the same simulation (same seed) at the market's own goal rates. Each side
    gets the market's de-vigged chance plus the difference between the two, so
    only what the blend moved off the market can make an edge, whatever the
    simulator's shape. A total without prices counts as an even -110 market;
    puck lines and moneylines need prices.
    """
    def col(name):
        return f[name].to_numpy(float) if name in f else np.full(len(f), np.nan)

    total = col("total_line")
    p, r = line_probs(sim, home_lines, total), line_probs(ref_sim, home_lines, total)
    win = anchored(market_chance(col("home_moneyline"), col("away_moneyline"), default=np.nan),
                   pred["home_win_prob"].to_numpy(float), ref["home_win_prob"].to_numpy(float))
    cover = anchored(market_chance(col("home_spread_price"), col("away_spread_price"), default=np.nan),
                     no_push(p["model_home_cover_prob"], p["model_spread_push_prob"]),
                     no_push(r["model_home_cover_prob"], r["model_spread_push_prob"]))
    over = anchored(market_chance(col("over_price"), col("under_price")),
                    no_push(p["model_over_prob"], p["model_total_push_prob"]),
                    no_push(r["model_over_prob"], r["model_total_push_prob"]))
    sp, tp = p["model_spread_push_prob"].to_numpy(float), p["model_total_push_prob"].to_numpy(float)
    return pd.DataFrame({
        "edge_home_ml_prob": win,
        "edge_home_cover_prob": with_push(cover, sp), "edge_away_cover_prob": with_push(1 - cover, sp),
        "edge_spread_push_prob": sp,
        "edge_over_prob": with_push(over, tp), "edge_under_prob": with_push(1 - over, tp),
        "edge_total_push_prob": tp,
    }, index=f.index)
