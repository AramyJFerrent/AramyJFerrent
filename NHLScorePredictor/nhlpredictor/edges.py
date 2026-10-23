"""Betting edges: expected value of each side of the puck line, moneyline and total.

Probabilities come from the final prediction: the model's goal rates blended
with the market's (backed out of its moneyline and total), simulated against
the posted lines, and anchored to the market's own chances so the simulator's
shape cannot pose as an edge (``market.edge_chances``). A side is an edge when
one unit staked at the posted price is expected to return at least
``EDGE_MIN_EV``:

    EV = p_win * (decimal odds - 1) - p_loss        (a push returns the stake)

and it is staked at a fraction of the Kelly stake, one game's edges sharing a
cap (``bettingcore.edges``). A projected starting goalie is wrong about a
third of the time, and the market prices the real one, so edges are only
priced once both starters are confirmed (or known, for finished games).

Every market here includes overtime and the shootout, which the simulator
plays out (the shootout winner gets one goal), so the puck line and total are
graded on the official final score. A total without posted prices is assumed
to be -110 on both sides; the puck line and moneyline are never assumed,
because they are rarely priced near -110. The model's own chances before the
blend (``model_*``) can be priced the same way for comparison.
"""

from __future__ import annotations

import numpy as np
import pandas as pd
from bettingcore import EDGE_FIELDS, best_side, empty_pick_fields, format_american, settle, stake_picks, summarize

ASSUMED_PRICE = -110.0
PUCK_LINE = 1.5
MARKETS = ("spread", "moneyline", "total")
EDGE_COLUMNS = [f"{m}_edge_{f}" for m in MARKETS for f in EDGE_FIELDS]
# The columns each rule reads its chances from: the final prediction's anchored
# chances, or the model's own before the blend.
CHANCES = {
    "final": {"win": "edge_home_ml_prob", "home_cover": "edge_home_cover_prob",
              "away_cover": "edge_away_cover_prob", "spread_push": "edge_spread_push_prob",
              "over": "edge_over_prob", "under": "edge_under_prob", "total_push": "edge_total_push_prob"},
    "model": {"win": "model_home_prob", "home_cover": "model_home_cover_prob",
              "away_cover": "model_away_cover_prob", "spread_push": "model_spread_push_prob",
              "over": "model_over_prob", "under": "model_under_prob", "total_push": "model_total_push_prob"},
}
# Goalie statuses an edge can be priced on: confirmed by ESPN, or known after the game.
SETTLED_GOALIE = ("confirmed", "known")


def _missing(x) -> bool:
    return x is None or bool(pd.isna(x))


def _no_price(american) -> bool:
    """Missing, or not a valid American price (those are never between -100 and +100)."""
    return _missing(american) or abs(float(american)) < 100


def format_price(american) -> str:
    return format_american(american)


def price_assumed(r, market: str) -> bool:
    """Whether a logged edge was bet at the assumed -110 (a total whose side had no posted price)."""
    if market != "total" or _missing(getattr(r, "total_edge_side", None)):
        return False
    return _no_price(r.over_price if r.total_edge_side == "over" else r.under_price)


def format_line(line: float) -> str:
    return f"{line:+g}"


def goalies_settled(r) -> bool:
    """Whether both starting goalies are confirmed (or known), so an edge can be priced."""
    def ok(status) -> bool:
        return isinstance(status, str) and any(word in status.lower() for word in SETTLED_GOALIE)
    return ok(getattr(r, "home_goalie_status", None)) and ok(getattr(r, "away_goalie_status", None))


def puck_line(home_line, model_home_prob) -> float:
    """The posted puck line (home team's), or -1.5 on the model's favorite when none is posted."""
    if not _missing(home_line):
        return float(home_line)
    return -PUCK_LINE if _missing(model_home_prob) or model_home_prob >= 0.5 else PUCK_LINE


def spread_sides(r, c: dict) -> list[dict]:
    """Both sides of the puck line at the posted line (from ``home_spread_line``)."""
    if _missing(r.home_spread_line):
        return []
    line = float(r.home_spread_line)
    push = getattr(r, c["spread_push"])
    return [{"side": "home", "label": f"{r.home_team} {format_line(line)}", "line": line,
             "price": r.home_spread_price, "prob": getattr(r, c["home_cover"]), "push": push, "assumed": False},
            {"side": "away", "label": f"{r.away_team} {format_line(-line)}", "line": -line,
             "price": r.away_spread_price, "prob": getattr(r, c["away_cover"]), "push": push, "assumed": False}]


def moneyline_sides(r, c: dict) -> list[dict]:
    p = getattr(r, c["win"])
    return [{"side": "home", "label": r.home_team, "price": r.home_moneyline, "prob": p, "push": 0.0},
            {"side": "away", "label": r.away_team, "price": r.away_moneyline,
             "prob": np.nan if _missing(p) else 1.0 - p, "push": 0.0}]


def total_sides(r, c: dict) -> list[dict]:
    """Over and under at the posted total; missing prices are assumed -110."""
    if _missing(r.total_line):
        return []
    line = float(r.total_line)
    sides = []
    for side, price, prob in (("over", r.over_price, getattr(r, c["over"])),
                              ("under", r.under_price, getattr(r, c["under"]))):
        assumed = _no_price(price)
        sides.append({"side": side, "label": f"{side.title()} {line:g}", "line": line,
                      "price": ASSUMED_PRICE if assumed else price, "prob": prob,
                      "push": getattr(r, c["total_push"]), "assumed": assumed})
    return sides


SIDES = {"spread": spread_sides, "moneyline": moneyline_sides, "total": total_sides}


def game_edges(r, chances: str = "final") -> dict:
    """The ``{market}_edge_*`` columns for one game (a row with the prices and chances).

    No edges until both starting goalies are confirmed (``goalies_settled``).
    """
    c = CHANCES[chances]
    settled = goalies_settled(r)
    picks = stake_picks({m: best_side(sides(r, c)) if settled else None for m, sides in SIDES.items()})
    out = {}
    for m, pick in picks.items():
        fields = empty_pick_fields() if pick is None else pick
        out.update({f"{m}_edge_{f}": fields[f] for f in EDGE_FIELDS})
        if pick is None:
            out[f"{m}_edge_pick"] = None
    return out


def add_edges(rows: pd.DataFrame, chances: str = "final") -> pd.DataFrame:
    """``rows`` with the edge columns filled in for every game."""
    out = rows.copy()
    edges = pd.DataFrame([game_edges(r, chances) for r in out.itertuples(index=False)], index=out.index,
                         columns=EDGE_COLUMNS)
    for col in edges:
        out[col] = edges[col]
    return out


def grade_edge(market: str, side, line, price, home_score, away_score) -> tuple[str | None, float]:
    """``W``, ``L`` or ``P`` and profit per unit staked, from the final score
    (overtime and the shootout goal included). ``(None, nan)`` when not gradable."""
    if _missing(side) or side == "" or _no_price(price) or _missing(home_score) or _missing(away_score):
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
    return settle(diff, price)


def graded(entries: pd.DataFrame, market: str) -> pd.DataFrame:
    """Each finished game's staked ``market`` edge: result, stake, profit, game and EV.

    Edges logged without a stake (before edges were priced from the final
    prediction and Kelly-sized) are left out.
    """
    stake_col = f"{market}_edge_stake"
    picked = entries[entries[f"{market}_edge_side"].notna() & entries[f"{market}_edge_side"].astype(str).ne("")]
    if stake_col in picked:
        picked = picked[picked[stake_col].notna()]
    else:
        picked = picked.iloc[0:0]
    rows = []
    for _, r in picked.iterrows():
        res, per_unit = grade_edge(market, r[f"{market}_edge_side"], r[f"{market}_edge_line"],
                                   r[f"{market}_edge_price"], r["home_score"], r["away_score"])
        if res is None:
            continue
        s = float(r[stake_col])
        rows.append({"result": res, "stake": s, "profit": s * per_unit, "game": r.get("game_id"),
                     "ev": r[f"{market}_edge_ev"]})
    return pd.DataFrame(rows, columns=["result", "stake", "profit", "game", "ev"])


def edge_record(entries: pd.DataFrame, market: str, n_boot: int = 5000, seed: int = 0) -> dict:
    """Bets, W-L-P, units staked and won, ROI with its 95% range over games, and expected ROI."""
    return summarize(graded(entries, market), n_boot=n_boot, seed=seed)
