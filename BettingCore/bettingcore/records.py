"""Betting records: W-L-P, units staked and won, ROI and its uncertainty.

ROI is profit per unit staked. Its 95% range is a bootstrap that resamples
whole games rather than single bets, because the edges of one game (a spread
and a moneyline on the same team, say) win and lose together; resampling bets
one at a time would treat them as independent and make the range too narrow.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

# ``ev`` (expected profit per unit at the time of the bet) is optional; with it
# the summary also gives the ROI the bets expected, to set against the one they got.
RESULT_COLUMNS = ["result", "stake", "profit", "game", "ev"]


def roi_interval(profit, stake, groups=None, n: int = 5000, seed: int = 0,
                 chunk: int = 250) -> tuple[float, float]:
    """95% range of total profit over total stake, resampling ``groups`` (default: each bet)."""
    profit = np.asarray(profit, dtype=float)
    stake = np.asarray(stake, dtype=float)
    if len(profit) == 0 or stake.sum() <= 0:
        return float("nan"), float("nan")
    if groups is None:
        p, s = profit, stake
    else:
        codes, _ = pd.factorize(pd.Series(groups).astype(str))
        p = np.bincount(codes, weights=profit)
        s = np.bincount(codes, weights=stake)
    k = len(p)
    if k < 2:
        return float("nan"), float("nan")
    rng = np.random.default_rng(seed)
    rois = []
    for start in range(0, n, chunk):
        idx = rng.integers(0, k, size=(min(chunk, n - start), k))
        with np.errstate(divide="ignore", invalid="ignore"):
            rois.append(p[idx].sum(axis=1) / s[idx].sum(axis=1))
    rois = np.concatenate(rois)
    rois = rois[np.isfinite(rois)]
    return float(np.percentile(rois, 2.5)), float(np.percentile(rois, 97.5))


def summarize(results: pd.DataFrame, n_boot: int = 5000, seed: int = 0) -> dict:
    """Totals of settled bets (``RESULT_COLUMNS``): bets, wins, losses, pushes,
    units staked and won, ROI and its 95% range by game, and (with ``ev``) the
    stake-weighted ROI the bets expected."""
    r = results[results["result"].isin(["W", "L", "P"])] if len(results) else results
    n = len(r)
    staked = float(r["stake"].sum()) if n else 0.0
    units = float(r["profit"].sum()) if n else 0.0
    counts = r["result"].value_counts() if n else pd.Series(dtype=int)
    low, high = roi_interval(r["profit"], r["stake"], r["game"] if "game" in r else None, n_boot, seed) \
        if n else (float("nan"), float("nan"))
    expected = float((r["stake"] * r["ev"]).sum() / staked) if n and "ev" in r and staked > 0 else float("nan")
    return {"bets": n, "wins": int(counts.get("W", 0)), "losses": int(counts.get("L", 0)),
            "pushes": int(counts.get("P", 0)), "staked": staked, "units": units,
            "roi": units / staked if staked > 0 else float("nan"), "roi_low": low, "roi_high": high,
            "expected_roi": expected}


def paired_bootstrap(a, b, n: int = 5000, seed: int = 0, chunk: int = 250) -> tuple[float, float, float]:
    """Mean of ``a - b`` and its 95% interval over resampled games."""
    diff = np.asarray(a, dtype=float) - np.asarray(b, dtype=float)
    rng = np.random.default_rng(seed)
    means = []
    for start in range(0, n, chunk):
        idx = rng.integers(0, len(diff), size=(min(chunk, n - start), len(diff)))
        means.append(diff[idx].mean(axis=1))
    means = np.concatenate(means)
    return float(diff.mean()), float(np.percentile(means, 2.5)), float(np.percentile(means, 97.5))
