"""Betting edges: expected value of each side of the run line, moneyline and total.

Every edge uses the model's own chances, before any blending with the
betting market: the model-only win probability for the moneyline, and the
model-only simulation's chance of covering the posted run line and of going
over or under the posted total (a whole-number total can push, which returns
the stake). For a bet at American price ``A`` the decimal price is
``d = 1 + A/100`` (``A > 0``) or ``1 + 100/|A|``, and with win, push and loss
chances ``p``, ``q`` and ``1 - p - q`` the expected profit per unit staked is

    EV = p (d - 1) - (1 - p - q)

A side is an edge when its EV is at least ``EDGE_MIN_EV``; each market
reports its best side. Posted prices are used wherever ESPN gives them. A
total without a price is assumed to be -110 on both sides (marked as
assumed); the run line and the moneyline are never priced near -110, so
without a price they get no edge.
"""

from __future__ import annotations

import math

import numpy as np
import pandas as pd

EDGE_MIN_EV = 0.03
ASSUMED_PRICE = -110.0
MARKETS = ("spread", "moneyline", "total")
MARKET_NAMES = {"spread": "Run line", "moneyline": "Moneyline", "total": "Total"}
EDGE_FIELDS = ("pick", "side", "line", "price", "prob", "ev")
EDGE_COLUMNS = [f"{m}_edge_{f}" for m in MARKETS for f in EDGE_FIELDS]
# The run line the model quotes when none is posted: the model's favorite at -1.5.
DEFAULT_RUN_LINE = 1.5


def decimal_odds(american):
    """Decimal price (stake included) of an American price."""
    a = np.asarray(american, dtype=float)
    with np.errstate(divide="ignore", invalid="ignore"):
        out = np.where(a > 0, 1.0 + a / 100.0, 1.0 + 100.0 / np.abs(a))
    return float(out) if out.ndim == 0 else out


def implied_prob(american) -> np.ndarray:
    """Break-even win chance of an American price (margin included)."""
    ml = np.asarray(american, dtype=float)
    with np.errstate(divide="ignore", invalid="ignore"):
        return np.where(ml < 0, -ml / (-ml + 100.0), 100.0 / (ml + 100.0))


def fair_american(p: float) -> int:
    """Fair (no-vig) American price for win probability ``p``, rounded to 5."""
    p = min(max(p, 0.01), 0.99)
    raw = -100.0 * p / (1.0 - p) if p > 0.5 else 100.0 * (1.0 - p) / p
    return int(5 * math.floor(raw / 5 + 0.5))


def expected_value(p_win, p_push, american):
    """Expected profit per unit staked, with pushes returning the stake."""
    p_win, p_push = np.asarray(p_win, dtype=float), np.asarray(p_push, dtype=float)
    out = p_win * (decimal_odds(american) - 1.0) - (1.0 - p_win - p_push)
    return float(out) if np.ndim(out) == 0 else out


def american(price) -> str:
    if price is None or pd.isna(price):
        return "–"
    price = int(round(float(price)))
    return f"+{price}" if price > 0 else str(price)


def _ok(x) -> bool:
    return x is not None and not pd.isna(x)


def market_options(r) -> dict[str, list[dict]]:
    """Both sides of each market for one game (a log row): label, side, line,
    price, whether the price was assumed, and the model's win and push chances.
    A market with no line has no options; a side with no price is left out."""
    home, away = r["home_team"], r["away_team"]
    out = {m: [] for m in MARKETS}
    hl = r.get("home_run_line")
    if _ok(hl):
        p_home, p_away = r.get("model_home_cover_prob"), r.get("model_away_cover_prob")
        push = max(0.0, 1.0 - p_home - p_away) if _ok(p_home) and _ok(p_away) else 0.0
        for side, team, line, price, p in (("home", home, hl, r.get("home_run_line_price"), p_home),
                                           ("away", away, -hl, r.get("away_run_line_price"), p_away)):
            if _ok(price) and _ok(p):
                out["spread"].append({"label": f"{team} {line:+g}", "side": side, "line": float(line),
                                      "price": float(price), "assumed": False, "p_win": float(p), "p_push": push})
    p = r.get("model_home_prob")
    if _ok(p):
        for side, team, price, pw in (("home", home, r.get("home_moneyline"), p),
                                      ("away", away, r.get("away_moneyline"), 1.0 - p)):
            if _ok(price):
                out["moneyline"].append({"label": team, "side": side, "line": np.nan, "price": float(price),
                                         "assumed": False, "p_win": float(pw), "p_push": 0.0})
    tl = r.get("total_line")
    if _ok(tl):
        push = r.get("model_total_push_prob")
        push = float(push) if _ok(push) else 0.0
        for side, price, pw in (("over", r.get("over_price"), r.get("model_over_prob")),
                                ("under", r.get("under_price"), r.get("model_under_prob"))):
            if _ok(pw):
                out["total"].append({"label": f"{side.title()} {tl:g}", "side": side, "line": float(tl),
                                     "price": float(price) if _ok(price) else ASSUMED_PRICE,
                                     "assumed": not _ok(price), "p_win": float(pw), "p_push": push})
    return out


def best_side(options: list[dict], min_ev: float = EDGE_MIN_EV) -> dict | None:
    """The side with the highest expected value, if it clears ``min_ev``."""
    best = None
    for o in options:
        ev = expected_value(o["p_win"], o["p_push"], o["price"])
        if np.isfinite(ev) and (best is None or ev > best["ev"]):
            best = {**o, "ev": ev}
    return best if best is not None and best["ev"] >= min_ev else None


def add_edges(frame: pd.DataFrame) -> pd.DataFrame:
    """``frame`` with the best side of each market filled into the ``*_edge_*`` columns
    (pick empty and the rest NaN where no side clears the bar)."""
    out = frame.copy()
    values = {c: [] for c in EDGE_COLUMNS}
    for _, r in out.iterrows():
        opts = market_options(r)
        for m in MARKETS:
            pick = best_side(opts[m])
            values[f"{m}_edge_pick"].append(pick["label"] if pick else "")
            values[f"{m}_edge_side"].append(pick["side"] if pick else "")
            for f, key in (("line", "line"), ("price", "price"), ("prob", "p_win"), ("ev", "ev")):
                values[f"{m}_edge_{f}"].append(pick[key] if pick else np.nan)
    for c, v in values.items():
        out[c] = pd.Series(v, index=out.index, dtype=object if c.endswith(("_pick", "_side")) else float)
    return out


def grade_pick(market: str, side: str, line: float, price: float, home_score: float,
               away_score: float) -> tuple[str, float]:
    """Result (W, L or P) and units won on a one-unit bet, from the final score."""
    if market == "total":
        diff = (home_score + away_score - line) * (1 if side == "over" else -1)
    else:
        own, other = (home_score, away_score) if side == "home" else (away_score, home_score)
        diff = own - other + (0.0 if market == "moneyline" or pd.isna(line) else line)
    if diff > 0:
        return "W", decimal_odds(price) - 1.0
    if diff < 0:
        return "L", -1.0
    return "P", 0.0


def graded_edges(frame: pd.DataFrame, market: str) -> pd.DataFrame:
    """Each finished game's ``market`` edge with its result and units."""
    pick = frame[f"{market}_edge_pick"]
    d = frame[pick.notna() & pick.astype(str).ne("") & frame["home_score"].notna() & frame["away_score"].notna()]
    graded = [grade_pick(market, r[f"{market}_edge_side"], r[f"{market}_edge_line"], r[f"{market}_edge_price"],
                         r["home_score"], r["away_score"]) for _, r in d.iterrows()]
    return pd.DataFrame({"result": [g[0] for g in graded], "units": [g[1] for g in graded]}, index=d.index)


def edge_record(frame: pd.DataFrame, market: str) -> dict:
    """Bets, wins, losses, pushes, units and return per bet on ``market``'s edges."""
    g = graded_edges(frame, market)
    n = len(g)
    units = float(g["units"].sum()) if n else 0.0
    return {"bets": n, "wins": int((g["result"] == "W").sum()), "losses": int((g["result"] == "L").sum()),
            "pushes": int((g["result"] == "P").sum()), "units": units, "roi": units / n if n else float("nan"),
            "per_bet": g["units"].to_numpy(float)}
