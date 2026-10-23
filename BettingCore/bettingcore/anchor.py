"""Market-anchored chances for pricing edges.

A score simulator turns expected points into chances of winning, covering and
going over, but its shape is not the market's: centered exactly on the line,
a simulator of discrete scores rarely splits a spread or total 50/50, and its
conversion of a spread into a win chance differs from the moneyline's. Priced
with those raw chances, edges appear wherever the simulator's shape disagrees
with the market's, even when the prediction agrees with the line. In
walk-forward tests (NFL, 2015-2025) such edges expected +7% to +11% per unit
and returned a fraction of that.

So each side's chance starts from the market's own (the de-vigged price) and
moves only by what the prediction adds: the simulator's chance at the
predicted means minus its chance at the means the line implies. When the
prediction equals the line the market's chance comes back unchanged and no
side can clear the bar.

All chances here are conditional on the bet not pushing; ``with_push`` turns
one back into an unconditional chance.
"""

from __future__ import annotations

import numpy as np

from .odds import devig

# Chances are kept off 0 and 1 so a far-off simulation cannot promise certainty.
CLIP = (0.005, 0.995)


def no_push(p, push):
    """Chance a bet wins given that it does not push."""
    p, push = np.asarray(p, dtype=float), np.nan_to_num(np.asarray(push, dtype=float))
    with np.errstate(divide="ignore", invalid="ignore"):
        out = np.where(push < 1.0, p / (1.0 - push), np.nan)
    return float(out) if np.ndim(out) == 0 else out


def with_push(q, push):
    """Unconditional chance of a win, from the chance given no push."""
    q, push = np.asarray(q, dtype=float), np.nan_to_num(np.asarray(push, dtype=float))
    out = q * (1.0 - push)
    return float(out) if np.ndim(out) == 0 else out


def market_chance(price_a, price_b, default: float = 0.5):
    """De-vigged chance of side A; ``default`` where either price is missing (an even -110 market)."""
    p = np.asarray(devig(price_a, price_b), dtype=float)
    out = np.where(np.isnan(p), default, p)
    return float(out) if np.ndim(out) == 0 else out


def anchored(market, predicted, at_line):
    """The market's chance moved by the prediction's: ``market + predicted - at_line``.

    ``predicted`` and ``at_line`` are the simulator's chances (given no push)
    at the predicted means and at the means the line implies. NaN wherever any
    input is missing.
    """
    market, predicted, at_line = (np.asarray(x, dtype=float) for x in (market, predicted, at_line))
    out = np.clip(market + predicted - at_line, *CLIP)
    out = np.where(np.isnan(market) | np.isnan(predicted) | np.isnan(at_line), np.nan, out)
    return float(out) if np.ndim(out) == 0 else out
