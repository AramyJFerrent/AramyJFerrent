"""Betting edges: the model's own chances against the posted prices.

Each game has three markets: the spread, the moneyline and the total. For
every side of each market the expected value of a 1-unit bet at the posted
American price is

    EV = p_win * (decimal odds - 1) - p_loss

with ``p_win``, ``p_push`` and ``p_loss = 1 - p_win - p_push`` taken from the
model's own score distribution, before blending with the line (a push returns
the stake). The side with the highest EV is the market's edge when its EV is
at least ``EDGE_MIN_EV``.

Spreads and totals are standard -110 markets, so a side whose price was not
posted is assumed to be -110 (and marked as assumed); a moneyline without a
price is never guessed.
"""

from __future__ import annotations

import math

import numpy as np
import pandas as pd

EDGE_MIN_EV = 0.03
ASSUMED_PRICE = -110.0
# Markets priced near -110 on both sides, where a missing price may be assumed.
ASSUMABLE = ("spread", "total")
MARKETS = ("spread", "moneyline", "total")
EDGE_FIELDS = ("pick", "side", "line", "price", "prob", "ev")
EDGE_COLUMNS = [f"{m}_edge_{f}" for m in MARKETS for f in EDGE_FIELDS]
# The price each side of each market is posted at, by log column.
PRICE_COLUMNS = {
    ("spread", "home"): "home_spread_price", ("spread", "away"): "away_spread_price",
    ("moneyline", "home"): "home_moneyline", ("moneyline", "away"): "away_moneyline",
    ("total", "over"): "over_price", ("total", "under"): "under_price",
}


def decimal_odds(american):
    """Decimal odds (stake included) for an American price: -110 -> 1.909, +150 -> 2.5."""
    a = np.asarray(american, dtype=float)
    with np.errstate(divide="ignore", invalid="ignore"):
        out = np.where(a > 0, 1.0 + a / 100.0, 1.0 + 100.0 / np.abs(a))
    return float(out) if out.ndim == 0 else out


def implied_prob(american):
    """Break-even win probability of an American price, margin included."""
    ml = np.asarray(american, dtype=float)
    with np.errstate(divide="ignore", invalid="ignore"):
        out = np.where(ml < 0, -ml / (-ml + 100.0), 100.0 / (ml + 100.0))
    return float(out) if out.ndim == 0 else out


def fair_american(p: float) -> int:
    """Fair (no-vig) American moneyline for win probability ``p``, rounded to 5."""
    p = min(max(p, 0.01), 0.99)
    raw = -100.0 * p / (1.0 - p) if p > 0.5 else 100.0 * (1.0 - p) / p
    return int(5 * math.floor(raw / 5 + 0.5))


def expected_value(p_win, p_push, american):
    """Expected profit per unit staked; a push returns the stake."""
    p_win, p_push = np.asarray(p_win, dtype=float), np.asarray(p_push, dtype=float)
    out = p_win * (decimal_odds(american) - 1.0) - (1.0 - p_win - p_push)
    return float(out) if np.ndim(out) == 0 else out


def _missing(x) -> bool:
    return x is None or (isinstance(x, float) and math.isnan(x)) or pd.isna(x)


def best_side(options: list[dict], min_ev: float = EDGE_MIN_EV) -> dict | None:
    """The option with the highest EV if it reaches ``min_ev``, else None.

    Each option has ``label``, ``side``, ``line``, ``price``, ``assumed``,
    ``p_win`` and ``p_push``; options without a price or probability are skipped.
    """
    best = None
    for o in options:
        if _missing(o["price"]) or _missing(o["p_win"]):
            continue
        ev = expected_value(o["p_win"], 0.0 if _missing(o["p_push"]) else o["p_push"], o["price"])
        if best is None or ev > best["ev"]:
            best = {"pick": o["label"], "side": o["side"], "line": o["line"], "price": float(o["price"]),
                    "assumed": bool(o["assumed"]), "prob": float(o["p_win"]), "ev": float(ev)}
    return best if best is not None and best["ev"] >= min_ev else None


def line_text(line: float) -> str:
    """A side's handicap as a bettor reads it: -4.5, +3, pk."""
    return "pk" if line == 0 else f"{line:+g}"


def price_text(price: float, assumed: bool = False) -> str:
    if _missing(price):
        return "–"
    p = int(round(price))
    return (f"+{p}" if p > 0 else str(p)) + ("*" if assumed else "")


def _get(row, col):
    return row.get(col, np.nan) if isinstance(row, dict) else getattr(row, col, np.nan)


def _price(row, market: str, side: str) -> tuple[float, bool]:
    """A side's posted price, or the assumed -110 where that is allowed and nothing was posted."""
    price = _get(row, PRICE_COLUMNS[(market, side)])
    if _missing(price) and market in ASSUMABLE:
        return ASSUMED_PRICE, True
    return (np.nan, False) if _missing(price) else (float(price), False)


def market_options(row, market: str) -> list[dict]:
    """Both sides of ``market`` for one game, with the model's chances. ``row``
    carries the line columns (``spread`` is the home team's expected margin),
    the prices and the model-only probabilities."""
    home, away = _get(row, "home_team"), _get(row, "away_team")
    out = []
    if market == "spread":
        spread, cover = _get(row, "spread"), _get(row, "model_home_cover_prob")
        push = _get(row, "model_spread_push_prob")
        if _missing(spread) or _missing(cover):
            return []
        push = 0.0 if _missing(push) else push
        for side, team, line, p in (("home", home, -spread, cover), ("away", away, spread, 1.0 - cover - push)):
            price, assumed = _price(row, market, side)
            out.append({"label": f"{team} {line_text(line)}", "side": side, "line": float(line), "price": price,
                        "assumed": assumed, "p_win": p, "p_push": push})
    elif market == "moneyline":
        p_home = _get(row, "model_home_prob")
        if _missing(p_home):
            return []
        for side, team, p in (("home", home, p_home), ("away", away, 1.0 - p_home)):
            price, assumed = _price(row, market, side)
            out.append({"label": f"{team} ML", "side": side, "line": np.nan, "price": price, "assumed": assumed,
                        "p_win": p, "p_push": 0.0})
    elif market == "total":
        total, over, push = _get(row, "total"), _get(row, "model_over_prob"), _get(row, "model_total_push_prob")
        if _missing(total) or _missing(over):
            return []
        push = 0.0 if _missing(push) else push
        for side, p in (("over", over), ("under", 1.0 - over - push)):
            price, assumed = _price(row, market, side)
            out.append({"label": f"{side.title()} {total:g}", "side": side, "line": float(total), "price": price,
                        "assumed": assumed, "p_win": p, "p_push": push})
    return out


def has_market(row, market: str) -> bool:
    """Whether the game has a line (or a price) for ``market`` yet."""
    if market == "moneyline":
        return not (_missing(_get(row, "home_moneyline")) and _missing(_get(row, "away_moneyline")))
    return not _missing(_get(row, market))


def edge_columns(df: pd.DataFrame, min_ev: float = EDGE_MIN_EV) -> pd.DataFrame:
    """The ``{market}_edge_*`` columns for every row of ``df`` (empty pick when there is no edge)."""
    out = {c: [] for c in EDGE_COLUMNS}
    for row in df.to_dict("records"):
        for m in MARKETS:
            e = best_side(market_options(row, m), min_ev)
            for f in EDGE_FIELDS:
                out[f"{m}_edge_{f}"].append(("" if f in ("pick", "side") else np.nan) if e is None else e[f])
    res = pd.DataFrame(out, index=df.index)
    for m in MARKETS:
        for f in ("line", "price", "prob", "ev"):
            res[f"{m}_edge_{f}"] = res[f"{m}_edge_{f}"].astype(float)
        for f in ("pick", "side"):
            res[f"{m}_edge_{f}"] = res[f"{m}_edge_{f}"].astype(object)
    return res


def price_assumed(row, market: str) -> bool:
    """Whether the logged edge's price was assumed rather than posted."""
    side = _get(row, f"{market}_edge_side")
    if market not in ASSUMABLE or not isinstance(side, str) or not side:
        return False
    return _missing(_get(row, PRICE_COLUMNS[(market, side)]))


def grade_edge(market: str, side: str, line: float, price: float, home_score: float, away_score: float):
    """Result (``W``, ``L`` or ``P``) and units won of a 1-unit bet, or (None, nan) before the result."""
    if _missing(home_score) or _missing(away_score) or not isinstance(side, str) or not side:
        return None, np.nan
    if market == "total":
        res = (home_score + away_score - line) * (1 if side == "over" else -1)
    else:
        res = (home_score - away_score) * (1 if side == "home" else -1)
        if market == "spread":
            res += line
    if res > 0:
        return "W", float(decimal_odds(price)) - 1.0
    if res < 0:
        return "L", -1.0
    return "P", 0.0


def graded(df: pd.DataFrame, market: str) -> pd.DataFrame:
    """Every finished game with an edge in ``market``: result and units."""
    pick = df[f"{market}_edge_pick"]
    d = df[pick.notna() & (pick.astype(str) != "") & df["home_score"].notna() & df["away_score"].notna()]
    res = [grade_edge(market, r[f"{market}_edge_side"], r[f"{market}_edge_line"], r[f"{market}_edge_price"],
                      r["home_score"], r["away_score"]) for r in d.to_dict("records")]
    return pd.DataFrame({"result": [r[0] for r in res], "units": [r[1] for r in res]}, index=d.index)


def record(df: pd.DataFrame, market: str) -> dict:
    """Edges, W-L-P, units and ROI (units per unit staked) in ``market``."""
    g = graded(df, market)
    n = len(g)
    units = float(g["units"].sum()) if n else 0.0
    return {"edges": n, "wins": int((g["result"] == "W").sum()), "losses": int((g["result"] == "L").sum()),
            "pushes": int((g["result"] == "P").sum()), "units": units, "roi": units / n if n else np.nan,
            "per_bet": g["units"].to_numpy(float)}


def moved_toward(side: pd.Series, first_spread: pd.Series, last_spread: pd.Series) -> tuple[int, int]:
    """Of the games whose spread moved between two lines with a spread edge
    on the first, how many moved toward the edge's ``side`` (a home edge
    wants the home team's expected margin to grow), and how many moved."""
    move = last_spread - first_spread
    moved = side.isin(["home", "away"]) & move.notna() & (move != 0)
    toward = np.where(side[moved] == "home", move[moved] > 0, move[moved] < 0)
    return int(toward.sum()), int(moved.sum())


def roi_interval(per_bet: np.ndarray, n: int = 2000, seed: int = 0) -> tuple[float, float]:
    """95% bootstrap range of the ROI over resampled bets."""
    per_bet = np.asarray(per_bet, dtype=float)
    if len(per_bet) < 2:
        return np.nan, np.nan
    rng = np.random.default_rng(seed)
    means = np.array([per_bet[rng.integers(0, len(per_bet), len(per_bet))].mean() for _ in range(n)])
    return float(np.percentile(means, 2.5)), float(np.percentile(means, 97.5))
