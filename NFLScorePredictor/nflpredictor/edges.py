"""Betting edges: expected value of each side of the spread, moneyline and total.

Probabilities come from the model alone, before it is blended with the betting
line (a model-only simulation of each game, see ``ScoreModel.model_only``), so
an edge is a place where the model disagrees with the market by enough to pay
for the bookmaker's cut. A side is an edge when its expected value at the
posted price is at least ``EDGE_MIN_EV`` per unit staked. Pushes (integer
spreads and totals, and regular-season ties on the moneyline) return the stake.
"""

from __future__ import annotations

import math
from dataclasses import dataclass

import numpy as np
import pandas as pd

# Smallest expected value per unit staked that counts as an edge.
EDGE_MIN_EV = 0.03
# Spreads and totals are priced near -110; when the schedule has the line but
# not the price, both sides are assumed to be -110. Moneylines are never assumed.
ASSUMED_PRICE = -110.0
MARKETS = ("spread", "moneyline", "total")
EDGE_FIELDS = ("pick", "side", "line", "price", "prob", "ev")
EDGE_COLUMNS = [f"{m}_edge_{f}" for m in MARKETS for f in EDGE_FIELDS]


def decimal_odds(american: float) -> float:
    """Decimal odds (total return per unit staked, stake included) for an American price."""
    return 1.0 + american / 100.0 if american > 0 else 1.0 + 100.0 / abs(american)


def implied_prob(american: float) -> float:
    """Break-even win probability of an American price (with the bookmaker's cut left in)."""
    return 1.0 / decimal_odds(american)


def fair_american(p: float) -> int:
    """Fair (no-vig) American odds for win probability ``p``, rounded to 5."""
    p = min(max(p, 0.01), 0.99)
    raw = -100.0 * p / (1.0 - p) if p > 0.5 else 100.0 * (1.0 - p) / p
    return int(5 * math.floor(raw / 5 + 0.5))


def format_american(odds: float) -> str:
    return f"+{odds:.0f}" if odds > 0 else f"{odds:.0f}"


def expected_value(p_win: float, p_push: float, american: float) -> float:
    """Expected profit per unit staked: wins pay the price, pushes return the stake."""
    return p_win * (decimal_odds(american) - 1.0) - (1.0 - p_win - p_push)


@dataclass
class Edge:
    label: str          # what to bet, e.g. "KC -3.5", "Over 44.5", "KC"
    side: str           # home, away, over or under
    line: float         # the picked side's handicap (spread), the total, or NaN (moneyline)
    price: float        # American price the EV is computed at
    assumed: bool       # price not posted; ASSUMED_PRICE used
    prob: float         # model chance the bet wins
    push: float         # model chance the bet pushes
    ev: float           # expected profit per unit staked


def best_side(sides: list[tuple]) -> Edge | None:
    """The side with the highest EV if it clears ``EDGE_MIN_EV``, else None.

    Each side is ``(label, side, line, price, assumed, p_win, p_push)``; sides
    without a price are skipped.
    """
    best = None
    for label, side, line, price, assumed, p_win, p_push in sides:
        if pd.isna(price) or pd.isna(p_win):
            continue
        p_push = 0.0 if pd.isna(p_push) else p_push
        ev = expected_value(p_win, p_push, price)
        if best is None or ev > best.ev:
            best = Edge(label, side, line, float(price), assumed, float(p_win), float(p_push), ev)
    return best if best is not None and best.ev >= EDGE_MIN_EV else None


def _handicap(points: float) -> str:
    return "PK" if abs(points) < 0.05 else f"{points:+.1f}"


def _spread_price(price: float) -> tuple[float, bool]:
    return (ASSUMED_PRICE, True) if pd.isna(price) else (float(price), False)


def spread_edge(r: dict) -> Edge | None:
    """Best side against the spread. ``spread_line`` is the expected home margin (home -3 is +3)."""
    line = r["spread_line"]
    if pd.isna(line) or pd.isna(r["model_home_cover_prob"]):
        return None
    push = r["model_spread_push_prob"]
    push = 0.0 if pd.isna(push) else push
    home_p, away_p = r["model_home_cover_prob"], 1.0 - r["model_home_cover_prob"] - push
    home_price, home_assumed = _spread_price(r["home_spread_price"])
    away_price, away_assumed = _spread_price(r["away_spread_price"])
    return best_side([
        (f"{r['home_team']} {_handicap(-line)}", "home", -line, home_price, home_assumed, home_p, push),
        (f"{r['away_team']} {_handicap(line)}", "away", line, away_price, away_assumed, away_p, push),
    ])


def moneyline_edge(r: dict) -> Edge | None:
    """Best moneyline side; a tie refunds both. Needs posted prices: none are assumed."""
    tie = r["model_tie_prob"]
    tie = 0.0 if pd.isna(tie) else tie
    return best_side([
        (r["home_team"], "home", np.nan, r["home_moneyline"], False, r["model_home_win_prob"], tie),
        (r["away_team"], "away", np.nan, r["away_moneyline"], False, r["model_away_win_prob"], tie),
    ])


def total_edge(r: dict) -> Edge | None:
    line = r["total_line"]
    if pd.isna(line) or pd.isna(r["model_over_prob"]):
        return None
    push = r["model_total_push_prob"]
    push = 0.0 if pd.isna(push) else push
    over_price, over_assumed = _spread_price(r["over_price"])
    under_price, under_assumed = _spread_price(r["under_price"])
    return best_side([
        (f"Over {line:g}", "over", line, over_price, over_assumed, r["model_over_prob"], push),
        (f"Under {line:g}", "under", line, under_price, under_assumed, 1.0 - r["model_over_prob"] - push, push),
    ])


MARKET_EDGES = {"spread": spread_edge, "moneyline": moneyline_edge, "total": total_edge}


def game_edges(r: dict, markets=MARKETS) -> dict:
    """The ``{market}_edge_*`` log columns for one game (pick text empty when there is no edge)."""
    out = {}
    for m in markets:
        e = MARKET_EDGES[m](r)
        values = ("", "", np.nan, np.nan, np.nan, np.nan) if e is None else \
            (e.label, e.side, e.line, e.price, e.prob, e.ev)
        out.update({f"{m}_edge_{f}": v for f, v in zip(EDGE_FIELDS, values)})
    return out


def edge_frame(rows: pd.DataFrame, markets=MARKETS) -> pd.DataFrame:
    """``game_edges`` for every row, aligned with ``rows``."""
    cols = [f"{m}_edge_{f}" for m in markets for f in EDGE_FIELDS]
    return pd.DataFrame([game_edges(r, markets) for r in rows.to_dict("records")],
                        index=rows.index, columns=cols)


def has_edge(pick) -> bool:
    return isinstance(pick, str) and pick != ""


def grade_edge(market: str, side: str, line: float, price: float, home_score: float,
               away_score: float) -> tuple[str, float]:
    """Result (win, loss or push) and units won on a 1-unit flat stake."""
    margin, total = home_score - away_score, home_score + away_score
    if market == "spread":
        diff = (margin if side == "home" else -margin) + line
    elif market == "moneyline":
        diff = margin if side == "home" else -margin
    else:
        diff = total - line if side == "over" else line - total
    if diff > 0:
        return "win", decimal_odds(price) - 1.0
    if diff < 0:
        return "loss", -1.0
    return "push", 0.0


def graded_bets(df: pd.DataFrame, market: str) -> pd.DataFrame:
    """One row per edge in ``market`` with a final score: result and units."""
    has = df[f"{market}_edge_pick"].map(has_edge) & df["home_score"].notna() & df["away_score"].notna()
    bets = df[has]
    graded = [grade_edge(market, r[f"{market}_edge_side"], r[f"{market}_edge_line"], r[f"{market}_edge_price"],
                         r["home_score"], r["away_score"]) for r in bets.to_dict("records")]
    return pd.DataFrame(graded, index=bets.index, columns=["result", "units"])


def edge_record(df: pd.DataFrame, market: str) -> dict:
    """Edges, wins, losses, pushes, units and ROI (units per unit staked) in ``market``."""
    g = graded_bets(df, market)
    n = len(g)
    units = float(g["units"].sum()) if n else 0.0
    return {"bets": n, "wins": int((g["result"] == "win").sum()), "losses": int((g["result"] == "loss").sum()),
            "pushes": int((g["result"] == "push").sum()), "units": units,
            "roi": units / n if n else float("nan"), "unit_results": g["units"].to_numpy()}
