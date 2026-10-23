"""Picking, sizing and settling bets.

An edge is the side of a market whose expected value at the posted price is
at least ``EDGE_MIN_EV`` per unit staked, valued with the predictor's final
(market-blended) chances. Those chances already weigh the model against the
line by how much the model has added in past seasons, so a disagreement the
model has not earned the right to make never reaches the bar.

Each edge is staked at a fraction of the Kelly stake, the bet size that
maximizes long-run bankroll growth if the chances are right. Chances are never
exactly right, and full Kelly is ruinous when they are overstated, so only
``KELLY_FRACTION`` of it is bet. Stakes are in units of 1% of the bankroll,
and the edges of one game (a spread and a moneyline on the same team are
nearly the same bet) share a cap of ``GAME_CAP_UNITS``.
"""

from __future__ import annotations

import math

import numpy as np

from .odds import decimal_odds, expected_value, valid_price

EDGE_MIN_EV = 0.03
# Share of the full Kelly stake that is bet.
KELLY_FRACTION = 0.25
# Largest total stake on one game or bout, in units of 1% of the bankroll.
GAME_CAP_UNITS = 3.0
# Fields of a pick, in the order they are logged as ``{market}_edge_{field}``.
EDGE_FIELDS = ("pick", "side", "line", "price", "prob", "ev", "stake")
TEXT_FIELDS = ("pick", "side")


def _missing(x) -> bool:
    if x is None:
        return True
    try:
        return math.isnan(float(x))
    except (TypeError, ValueError):
        return False


def best_side(options: list[dict], min_ev: float = EDGE_MIN_EV) -> dict | None:
    """The option with the highest expected value, if it reaches ``min_ev``.

    Each option has ``label``, ``side``, ``price`` and ``prob`` (chance the bet
    wins) and may have ``push`` (chance the stake comes back), ``line`` and
    ``assumed`` (the price was not posted). Options without a valid price or a
    probability are skipped. The pick is returned as ``pick``, ``side``,
    ``line``, ``price``, ``assumed``, ``prob``, ``push`` and ``ev``.
    """
    best = None
    for o in options:
        price, prob = o.get("price"), o.get("prob")
        if not valid_price(price) or _missing(prob):
            continue
        push = 0.0 if _missing(o.get("push")) else float(o["push"])
        ev = float(expected_value(float(prob), push, float(price)))
        if best is None or ev > best["ev"]:
            line = o.get("line", float("nan"))
            best = {"pick": o["label"], "side": o["side"], "line": float("nan") if _missing(line) else float(line),
                    "price": float(price), "assumed": bool(o.get("assumed", False)), "prob": float(prob),
                    "push": push, "ev": ev}
    return best if best is not None and best["ev"] >= min_ev else None


def kelly_fraction(p_win: float, p_push: float, american: float) -> float:
    """Share of the bankroll that maximizes expected log growth on one bet (0 if it has no edge).

    With win, push and loss chances ``p``, ``q`` and ``l = 1 - p - q`` and net
    odds ``b``, growth ``p log(1 + f b) + l log(1 - f)`` peaks at
    ``f = (p b - l) / (b (p + l))``; pushes leave the bankroll as it was.
    """
    if not valid_price(american) or _missing(p_win):
        return 0.0
    q = 0.0 if _missing(p_push) else float(p_push)
    p = float(p_win)
    loss = 1.0 - p - q
    b = float(decimal_odds(american)) - 1.0
    if b <= 0 or p + loss <= 0:
        return 0.0
    return max(0.0, (p * b - loss) / (b * (p + loss)))


def kelly_stake(p_win: float, p_push: float, american: float, fraction: float = KELLY_FRACTION) -> float:
    """Stake in units (1% of the bankroll): ``fraction`` of the Kelly stake."""
    return 100.0 * fraction * kelly_fraction(p_win, p_push, american)


def stake_picks(picks: dict, fraction: float = KELLY_FRACTION, cap: float = GAME_CAP_UNITS) -> dict:
    """Add a ``stake`` to each of one game's picks (``{market: pick or None}``).

    Every pick gets its fractional Kelly stake; when the game's stakes add up
    to more than ``cap`` they are scaled down together to fit.
    """
    stakes = {m: kelly_stake(p["prob"], p.get("push", 0.0), p["price"], fraction)
              for m, p in picks.items() if p is not None}
    total = sum(stakes.values())
    scale = cap / total if total > cap else 1.0
    return {m: (None if p is None else {**p, "stake": round(stakes[m] * scale, 4)}) for m, p in picks.items()}


def settle(margin: float, price: float) -> tuple[str | None, float]:
    """Result and profit per unit staked from how far the bet beat its line.

    ``margin`` is positive when the bet wins, negative when it loses and zero
    on a push (the stake comes back). Missing values give ``(None, nan)``.
    """
    if _missing(margin) or not valid_price(price):
        return None, float("nan")
    if margin > 0:
        return "W", float(decimal_odds(price)) - 1.0
    if margin < 0:
        return "L", -1.0
    return "P", 0.0


def payout(result: str | None, price: float) -> float:
    """Profit per unit staked for a ``W``, ``L`` or ``P`` (NaN when unsettled)."""
    if result == "W":
        return float(decimal_odds(price)) - 1.0
    if result == "L":
        return -1.0
    if result == "P":
        return 0.0
    return float("nan")


def empty_pick_fields() -> dict:
    """The logged fields of a market with no edge: empty text and NaN numbers."""
    return {f: ("" if f in TEXT_FIELDS else np.nan) for f in EDGE_FIELDS}
