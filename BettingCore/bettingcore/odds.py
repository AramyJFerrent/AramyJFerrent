"""Price math: American odds, break-even probabilities and expected value.

Every function accepts a scalar or an array. Scalars come back as plain
floats, arrays as arrays, and anything that is not a usable price (missing,
or between -100 and +100, which American odds never are) comes back as NaN.
"""

from __future__ import annotations

import math

import numpy as np


def _float_or_array(out: np.ndarray):
    return float(out) if np.ndim(out) == 0 else out


def valid_price(american) -> bool:
    """A usable American price: a finite number at least 100 in size."""
    try:
        a = float(american)
    except (TypeError, ValueError):
        return False
    return math.isfinite(a) and abs(a) >= 100


def decimal_odds(american):
    """Total return per unit staked, stake included: -110 -> 1.909, +150 -> 2.5."""
    a = np.asarray(american, dtype=float)
    with np.errstate(divide="ignore", invalid="ignore"):
        out = np.where(a >= 100, 1.0 + a / 100.0, np.where(a <= -100, 1.0 + 100.0 / np.abs(a), np.nan))
    return _float_or_array(out)


def implied_prob(american):
    """Break-even win probability of an American price, bookmaker margin included."""
    with np.errstate(divide="ignore", invalid="ignore"):
        return _float_or_array(1.0 / np.asarray(decimal_odds(american), dtype=float))


def american_from_prob(p):
    """Exact (unrounded) American odds whose break-even probability is ``p``."""
    p = np.asarray(p, dtype=float)
    with np.errstate(divide="ignore", invalid="ignore"):
        out = np.where(p > 0.5, -100.0 * p / (1.0 - p), 100.0 * (1.0 - p) / p)
    return _float_or_array(out)


def fair_american(p: float) -> int:
    """Fair (no-vig) American odds for win probability ``p``, rounded to 5."""
    p = min(max(float(p), 0.01), 0.99)
    raw = float(american_from_prob(p))
    return int(5 * math.floor(raw / 5 + 0.5))


def format_american(american, assumed: bool = False) -> str:
    """``+150``, ``-110`` (``-110*`` when assumed), or a dash when there is no price."""
    if not valid_price(american):
        return "–"
    a = int(round(float(american)))
    return (f"+{a}" if a > 0 else str(a)) + ("*" if assumed else "")


def median_price(values) -> float:
    """Median of American prices, taken on break-even probability and rounded to a whole price.

    American odds jump from -100 to +100, so a plain median of quotes on both
    sides of even money (-105 and +105) would land on 0. Invalid quotes are
    ignored; NaN when none is left.
    """
    probs = [implied_prob(v) for v in values if valid_price(v)]
    if not probs:
        return float("nan")
    return float(np.round(american_from_prob(float(np.median(probs)))))


def devig(price_a, price_b):
    """Chance of side A from the two sides' American prices, margin removed proportionally."""
    a = np.asarray(implied_prob(price_a), dtype=float)
    b = np.asarray(implied_prob(price_b), dtype=float)
    with np.errstate(divide="ignore", invalid="ignore"):
        return _float_or_array(a / (a + b))


def expected_value(p_win, p_push, american):
    """Expected profit per unit staked: a win pays ``decimal - 1``, a push returns the stake."""
    p_win, p_push = np.asarray(p_win, dtype=float), np.asarray(p_push, dtype=float)
    out = p_win * (np.asarray(decimal_odds(american), dtype=float) - 1.0) - (1.0 - p_win - p_push)
    return _float_or_array(out)
