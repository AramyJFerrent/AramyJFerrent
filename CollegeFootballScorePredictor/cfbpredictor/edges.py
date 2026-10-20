"""Betting edges: expected value of each side of a market at the posted price.

Probabilities come from the model alone (its own expected points run through
the score simulator, before any blending with the line), so an edge is a
disagreement between the model and the market, priced at what a bet would
actually pay. A side is an edge when its expected value per unit staked is at
least ``EDGE_MIN_EV``. Pushes return the stake.

Spreads and totals whose price is not posted are assumed to be -110 on both
sides (the standard price for those markets) and marked as assumed;
moneylines are never assumed.
"""

from __future__ import annotations

import math

import numpy as np
import pandas as pd

EDGE_MIN_EV = 0.03
ASSUMED_PRICE = -110.0
MARKETS = ("spread", "moneyline", "total")
EDGE_FIELDS = ("pick", "side", "line", "price", "prob", "ev")
TEXT_FIELDS = ("pick", "side")
# Markets normally priced near -110, where a missing price may be assumed.
STANDARD_MARKETS = {"spread", "total"}


def edge_columns(fields=EDGE_FIELDS) -> list[str]:
    return [f"{m}_edge_{f}" for m in MARKETS for f in fields]


def valid_price(american) -> bool:
    """A usable American price: a finite number at least 100 in size."""
    try:
        a = float(american)
    except (TypeError, ValueError):
        return False
    return math.isfinite(a) and abs(a) >= 100


def decimal_odds(american: float) -> float:
    """Total return per unit staked, stake included (-110 -> 1.909, +150 -> 2.5)."""
    a = float(american)
    return 1.0 + a / 100.0 if a > 0 else 1.0 + 100.0 / abs(a)


def implied_prob(american: float) -> float:
    """Break-even win probability at ``american`` (bookmaker margin included)."""
    return 1.0 / decimal_odds(american)


def fair_american(p: float) -> int:
    """Fair (no-vig) American odds for win probability ``p``, rounded to 5."""
    p = min(max(p, 0.01), 0.99)
    raw = -100.0 * p / (1.0 - p) if p > 0.5 else 100.0 * (1.0 - p) / p
    return int(5 * math.floor(raw / 5 + 0.5))


def american_text(american: float) -> str:
    a = int(round(float(american)))
    return f"+{a}" if a > 0 else str(a)


def _american_from_prob(p: float) -> float:
    """Exact American odds whose break-even probability is ``p`` (unrounded)."""
    return -100.0 * p / (1.0 - p) if p > 0.5 else 100.0 * (1.0 - p) / p


def median_price(values) -> float:
    """Median of American prices, taken on break-even probability and rounded to a whole price.

    American odds jump from -100 to +100, so a plain median of quotes on both
    sides of even money (-105 and +105) would land on 0. Invalid quotes are
    ignored; NaN when none is left.
    """
    probs = [implied_prob(v) for v in values if valid_price(v)]
    if not probs:
        return np.nan
    return float(np.round(_american_from_prob(float(np.median(probs)))))


def expected_value(p_win: float, p_push: float, american: float) -> float:
    """Expected profit per unit staked: win pays ``d - 1``, push returns the stake, loss loses it."""
    d = decimal_odds(american)
    return p_win * (d - 1.0) - (1.0 - p_win - p_push)


def market_price(price, market: str) -> tuple[float, bool]:
    """The price to evaluate and whether it was assumed (-110 for an unposted spread or total)."""
    if valid_price(price):
        return float(price), False
    if market in STANDARD_MARKETS:
        return ASSUMED_PRICE, True
    return np.nan, False


def best_side(sides: list[dict], min_ev: float = EDGE_MIN_EV) -> dict | None:
    """The side with the highest expected value if it clears ``min_ev``, else None.

    Each side is a dict with ``label``, ``side``, ``line``, ``price``,
    ``assumed``, ``p_win`` and ``p_push``; sides without a price or a
    probability are skipped.
    """
    best = None
    for s in sides:
        if not valid_price(s["price"]) or pd.isna(s["p_win"]):
            continue
        ev = expected_value(s["p_win"], 0.0 if pd.isna(s["p_push"]) else s["p_push"], s["price"])
        if best is None or ev > best["ev"]:
            best = {"pick": s["label"], "side": s["side"], "line": s["line"], "price": float(s["price"]),
                    "assumed": bool(s["assumed"]), "prob": float(s["p_win"]), "ev": float(ev)}
    return best if best is not None and best["ev"] >= min_ev else None


def _team_line(points: float) -> str:
    return "PK" if abs(points) < 0.05 else f"{points:+.1f}"


def game_sides(r) -> dict[str, list[dict]]:
    """Both sides of each market for one game (a log row or anything with the same fields).

    ``spread_line`` is the expected home margin (positive when the home team is
    favored), so the home team's spread is its negative. Probabilities are the
    model-only ones; the away side's are what is left after the home side and
    the push.
    """
    home, away = r["home_team"], r["away_team"]
    sides = {m: [] for m in MARKETS}
    spread = r["spread_line"]
    if pd.notna(spread):
        p_home, push = r["model_home_cover_prob"], r["model_spread_push_prob"]
        push = 0.0 if pd.isna(push) else push
        for side, team, line, p, price in (
                ("home", home, -spread, p_home, r["home_spread_price"]),
                ("away", away, spread, 1.0 - p_home - push, r["away_spread_price"])):
            price, assumed = market_price(price, "spread")
            sides["spread"].append({"label": f"{team} {_team_line(line)}", "side": side, "line": float(line),
                                    "price": price, "assumed": assumed, "p_win": p, "p_push": push})
    p_home = r["model_home_win_prob"]
    for side, team, p, price in (("home", home, p_home, r["home_moneyline"]),
                                 ("away", away, 1.0 - p_home, r["away_moneyline"])):
        price, assumed = market_price(price, "moneyline")
        if valid_price(price):
            sides["moneyline"].append({"label": team, "side": side, "line": np.nan, "price": price,
                                       "assumed": assumed, "p_win": p, "p_push": 0.0})
    total = r["total_line"]
    if pd.notna(total):
        p_over, push = r["model_over_prob"], r["model_total_push_prob"]
        push = 0.0 if pd.isna(push) else push
        for side, p, price in (("over", p_over, r["over_price"]), ("under", 1.0 - p_over - push, r["under_price"])):
            price, assumed = market_price(price, "total")
            sides["total"].append({"label": f"{side.title()} {total:g}", "side": side, "line": float(total),
                                   "price": price, "assumed": assumed, "p_win": p, "p_push": push})
    return sides


def game_edges(r, min_ev: float = EDGE_MIN_EV) -> dict:
    """The ``{market}_edge_*`` fields for one game; empty pick and NaNs where there is no edge."""
    out = {}
    for market, sides in game_sides(r).items():
        pick = best_side(sides, min_ev)
        out.update({f"{market}_edge_{f}": (pick[f] if pick else ("" if f in TEXT_FIELDS else np.nan))
                    for f in EDGE_FIELDS})
    return out


def edge_frame(df: pd.DataFrame, min_ev: float = EDGE_MIN_EV) -> pd.DataFrame:
    """``game_edges`` for every row, indexed like ``df``."""
    rows = [game_edges(r, min_ev) for _, r in df.iterrows()]
    return pd.DataFrame(rows, index=df.index, columns=edge_columns())


def priced(r, market: str) -> bool:
    """Whether the market had a line and a price (posted, or assumed where allowed) for this game."""
    if market == "moneyline":
        return valid_price(r["home_moneyline"]) or valid_price(r["away_moneyline"])
    return pd.notna(r["spread_line" if market == "spread" else "total_line"])


def assumed_price(r, market: str) -> bool:
    """Whether the logged edge in ``market`` was evaluated at an assumed -110."""
    side = r[f"{market}_edge_side"]
    col = {("spread", "home"): "home_spread_price", ("spread", "away"): "away_spread_price",
           ("total", "over"): "over_price", ("total", "under"): "under_price"}.get((market, side))
    return col is not None and not valid_price(r[col])


def grade_edge(market: str, side: str, line: float, price: float, home_score: float,
               away_score: float) -> tuple[str, float]:
    """Result ('W', 'L' or 'P') and units won for a 1-unit bet, from the final score."""
    margin, total = home_score - away_score, home_score + away_score
    if market == "spread":
        res = (margin if side == "home" else -margin) + line
    elif market == "moneyline":
        res = margin if side == "home" else -margin
    else:
        res = total - line if side == "over" else line - total
    if res > 0:
        return "W", decimal_odds(price) - 1.0
    if res < 0:
        return "L", -1.0
    return "P", 0.0


def edge_results(df: pd.DataFrame, market: str) -> pd.DataFrame:
    """Graded edges in ``market`` from rows with final scores: result, units and whether the price was assumed."""
    pick = df[f"{market}_edge_pick"].fillna("").astype(str)
    done = df[(pick != "") & df["home_score"].notna() & df["away_score"].notna()]
    rows = []
    for _, r in done.iterrows():
        result, units = grade_edge(market, r[f"{market}_edge_side"], r[f"{market}_edge_line"],
                                   r[f"{market}_edge_price"], r["home_score"], r["away_score"])
        rows.append({"result": result, "units": units, "assumed": assumed_price(r, market),
                     "season": r.get("season", np.nan)})
    return pd.DataFrame(rows, columns=["result", "units", "assumed", "season"])


def record(results: pd.DataFrame) -> dict:
    """Edges, wins, losses, pushes, units and ROI (units per unit staked) of graded edges."""
    n = len(results)
    units = float(results["units"].sum()) if n else 0.0
    count = results["result"].value_counts() if n else pd.Series(dtype=int)
    return {"edges": n, "wins": int(count.get("W", 0)), "losses": int(count.get("L", 0)),
            "pushes": int(count.get("P", 0)), "units": units, "roi": units / n if n else np.nan}
