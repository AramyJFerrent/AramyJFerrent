"""Betting edges: expected value of each side of the puck line, moneyline and total.

Probabilities come from the model alone, before it is blended with the
market, so an edge is the model disagreeing with the price rather than the
blend echoing it. A side is an edge when one unit staked at the posted price
is expected to return at least ``EDGE_MIN_EV``:

    EV = p_win * (decimal odds - 1) - p_loss        (a push returns the stake)

Every market here includes overtime and the shootout, which the simulator
plays out (the shootout winner gets one goal), so the puck line and total are
graded on the official final score. A total without posted prices is assumed
to be -110 on both sides; the puck line and moneyline are never assumed,
because they are rarely priced near -110.
"""

from __future__ import annotations

import math

import numpy as np
import pandas as pd

EDGE_MIN_EV = 0.03
ASSUMED_PRICE = -110.0
PUCK_LINE = 1.5
MARKETS = ("spread", "moneyline", "total")
EDGE_FIELDS = ("pick", "side", "line", "price", "prob", "ev")
EDGE_COLUMNS = [f"{m}_edge_{f}" for m in MARKETS for f in EDGE_FIELDS]


def _missing(x) -> bool:
    return x is None or bool(pd.isna(x))


def _no_price(american) -> bool:
    """Missing, or not a valid American price (those are never between -100 and +100)."""
    return _missing(american) or abs(float(american)) < 100


def decimal_odds(american: float) -> float:
    """Total return per unit staked at an American price, the stake included."""
    a = float(american)
    return 1.0 + a / 100.0 if a > 0 else 1.0 + 100.0 / abs(a)


def implied_prob(american: float) -> float:
    """Break-even win probability at an American price (margin included)."""
    return 1.0 / decimal_odds(american)


def fair_american(p: float) -> int:
    """Fair (no-vig) American odds for win probability ``p``, rounded to 5."""
    p = min(max(p, 0.01), 0.99)
    raw = -100.0 * p / (1.0 - p) if p > 0.5 else 100.0 * (1.0 - p) / p
    return int(5 * math.floor(raw / 5 + 0.5))


def format_price(american) -> str:
    if _missing(american):
        return "–"
    a = int(round(float(american)))
    return f"+{a}" if a > 0 else str(a)


def price_assumed(r, market: str) -> bool:
    """Whether a logged edge was bet at the assumed -110 (a total whose side had no posted price)."""
    if market != "total" or _missing(getattr(r, "total_edge_side", None)):
        return False
    return _no_price(r.over_price if r.total_edge_side == "over" else r.under_price)


def format_line(line: float) -> str:
    return f"{line:+g}"


def expected_value(p_win: float, p_push: float, american: float) -> float:
    """Expected profit per unit staked; a push returns the stake."""
    return p_win * (decimal_odds(american) - 1.0) - (1.0 - p_win - p_push)


def best_side(sides: list[dict], min_ev: float = EDGE_MIN_EV) -> dict | None:
    """The side with the highest EV if it clears ``min_ev``.

    Each side is a dict with ``side`` (key), ``label`` (e.g. ``MTL -1.5``),
    ``line``, ``price``, ``prob`` (win), ``push`` and ``assumed``. Sides
    without a price or a probability are skipped. The pick adds ``ev``.
    """
    best = None
    for s in sides:
        if _no_price(s.get("price")) or _missing(s.get("prob")):
            continue
        push = 0.0 if _missing(s.get("push")) else float(s["push"])
        ev = expected_value(float(s["prob"]), push, float(s["price"]))
        if best is None or ev > best["ev"]:
            best = {**s, "ev": ev}
    return best if best is not None and best["ev"] >= min_ev else None


def puck_line(home_line, model_home_prob) -> float:
    """The posted puck line (home team's), or -1.5 on the model's favorite when none is posted."""
    if not _missing(home_line):
        return float(home_line)
    return -PUCK_LINE if _missing(model_home_prob) or model_home_prob >= 0.5 else PUCK_LINE


def spread_sides(r) -> list[dict]:
    """Both sides of the puck line at the posted line (from ``home_spread_line``)."""
    if _missing(r.home_spread_line):
        return []
    line = float(r.home_spread_line)
    push = r.model_spread_push_prob
    return [{"side": "home", "label": f"{r.home_team} {format_line(line)}", "line": line,
             "price": r.home_spread_price, "prob": r.model_home_cover_prob, "push": push, "assumed": False},
            {"side": "away", "label": f"{r.away_team} {format_line(-line)}", "line": -line,
             "price": r.away_spread_price, "prob": r.model_away_cover_prob, "push": push, "assumed": False}]


def moneyline_sides(r) -> list[dict]:
    p = r.model_home_prob
    return [{"side": "home", "label": r.home_team, "line": np.nan, "price": r.home_moneyline, "prob": p,
             "push": 0.0, "assumed": False},
            {"side": "away", "label": r.away_team, "line": np.nan, "price": r.away_moneyline,
             "prob": np.nan if _missing(p) else 1.0 - p, "push": 0.0, "assumed": False}]


def total_sides(r) -> list[dict]:
    """Over and under at the posted total; missing prices are assumed -110."""
    if _missing(r.total_line):
        return []
    line = float(r.total_line)
    sides = []
    for side, price, prob in (("over", r.over_price, r.model_over_prob), ("under", r.under_price, r.model_under_prob)):
        assumed = _no_price(price)
        sides.append({"side": side, "label": f"{side.title()} {line:g}", "line": line,
                      "price": ASSUMED_PRICE if assumed else price, "prob": prob,
                      "push": r.model_total_push_prob, "assumed": assumed})
    return sides


SIDES = {"spread": spread_sides, "moneyline": moneyline_sides, "total": total_sides}


def game_edges(r) -> dict:
    """The ``{market}_edge_*`` columns for one game (a row with the prices and model-only probabilities)."""
    out = {}
    for market, sides in SIDES.items():
        pick = best_side(sides(r))
        out[f"{market}_edge_pick"] = pick["label"] if pick else None
        for f in EDGE_FIELDS[1:]:
            out[f"{market}_edge_{f}"] = pick[f] if pick else np.nan
    return out


def add_edges(rows: pd.DataFrame) -> pd.DataFrame:
    """``rows`` with the edge columns filled in for every game."""
    out = rows.copy()
    edges = pd.DataFrame([game_edges(r) for r in out.itertuples(index=False)], index=out.index,
                         columns=EDGE_COLUMNS)
    for col in edges:
        out[col] = edges[col]
    return out


def grade_edge(market: str, side, line, price, home_score, away_score) -> tuple[str | None, float]:
    """``W``, ``L`` or ``P`` and units won on a one-unit bet, from the final score
    (overtime and the shootout goal included). ``(None, nan)`` when not gradable."""
    if _missing(side) or _no_price(price) or _missing(home_score) or _missing(away_score):
        return None, np.nan
    margin = float(home_score) - float(away_score)
    if market == "moneyline":
        diff = margin if side == "home" else -margin
    elif market == "spread":
        diff = (margin if side == "home" else -margin) + float(line)
    elif market == "total":
        total = float(home_score) + float(away_score)
        diff = total - float(line) if side == "over" else float(line) - total
    else:
        raise ValueError(f"unknown market {market}")
    if diff > 0:
        return "W", decimal_odds(price) - 1.0
    if diff < 0:
        return "L", -1.0
    return "P", 0.0


def edge_record(entries: pd.DataFrame, market: str) -> dict:
    """Edges, W-L-P, units and return per bet for one market over finished games."""
    picked = entries[entries[f"{market}_edge_side"].notna()]
    graded = [grade_edge(market, r[f"{market}_edge_side"], r[f"{market}_edge_line"], r[f"{market}_edge_price"],
                         r["home_score"], r["away_score"]) for _, r in picked.iterrows()]
    graded = [(res, u) for res, u in graded if res is not None]
    units = np.array([u for _, u in graded], dtype=float)
    results = [res for res, _ in graded]
    return {"bets": len(graded), "wins": results.count("W"), "losses": results.count("L"),
            "pushes": results.count("P"), "units": float(units.sum()),
            "roi": float(units.mean()) if len(units) else float("nan"), "per_bet": units}


def roi_interval(units: np.ndarray, n: int = 5000, seed: int = 0) -> tuple[float, float]:
    """95% bootstrap range of the return per bet."""
    units = np.asarray(units, dtype=float)
    if len(units) == 0:
        return float("nan"), float("nan")
    rng = np.random.default_rng(seed)
    means = np.array([units[rng.integers(0, len(units), len(units))].mean() for _ in range(n)])
    return float(np.percentile(means, 2.5)), float(np.percentile(means, 97.5))
