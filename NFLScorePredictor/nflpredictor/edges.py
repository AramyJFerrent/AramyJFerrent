"""Betting edges: expected value of each side of the spread, moneyline and total.

Probabilities come from the final prediction, the model blended with the
betting line by the weight that has predicted best in recent seasons, run
through the score simulator against the posted lines and anchored to the
market's own chances (``ScoreModel.edge_chances``). The model's own numbers
(before the blend) disagree with the line in almost every game, but in
walk-forward tests most of that disagreement was noise; the blend keeps only
the share of it the model has earned, and the anchoring keeps the simulator's
shape from posing as an edge. A side is an edge when its expected
value at the posted price is at least ``EDGE_MIN_EV`` per unit staked, and it
is staked at a quarter of the Kelly stake, with one game's edges sharing a cap
(``bettingcore.edges``). Pushes (integer spreads and totals, and
regular-season ties on the moneyline) return the stake.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from bettingcore import EDGE_FIELDS, best_side, empty_pick_fields, settle, stake_picks, summarize

# Spreads and totals are priced near -110; when the schedule has the line but
# not the price, both sides are assumed to be -110. Moneylines are never assumed.
ASSUMED_PRICE = -110.0
MARKETS = ("spread", "moneyline", "total")
EDGE_COLUMNS = [f"{m}_edge_{f}" for m in MARKETS for f in EDGE_FIELDS]


def _price(price) -> tuple[float, bool]:
    return (ASSUMED_PRICE, True) if pd.isna(price) else (float(price), False)


def _handicap(points: float) -> str:
    return "PK" if abs(points) < 0.05 else f"{points:+.1f}"


def market_sides(r: dict, market: str) -> list[dict]:
    """Both sides of ``market`` for one game, with the final prediction's chances.

    ``spread_line`` is the expected home margin (home -3 is +3), so the home
    side's handicap is its negative.
    """
    if market == "spread":
        line, cover = r["spread_line"], r["home_cover_prob"]
        if pd.isna(line) or pd.isna(cover):
            return []
        push = 0.0 if pd.isna(r["spread_push_prob"]) else r["spread_push_prob"]
        out = []
        for side, team, handicap, p in (("home", r["home_team"], -line, cover),
                                        ("away", r["away_team"], line, 1.0 - cover - push)):
            price, assumed = _price(r[f"{side}_spread_price"])
            out.append({"label": f"{team} {_handicap(handicap)}", "side": side, "line": handicap,
                        "price": price, "assumed": assumed, "prob": p, "push": push})
        return out
    if market == "moneyline":
        tie = 0.0 if pd.isna(r["tie_prob"]) else r["tie_prob"]
        return [{"label": r[f"{side}_team"], "side": side, "price": r[f"{side}_moneyline"],
                 "prob": r[f"{side}_ml_prob"], "push": tie} for side in ("home", "away")]
    line, over = r["total_line"], r["over_prob"]
    if pd.isna(line) or pd.isna(over):
        return []
    push = 0.0 if pd.isna(r["total_push_prob"]) else r["total_push_prob"]
    out = []
    for side, p in (("over", over), ("under", 1.0 - over - push)):
        price, assumed = _price(r[f"{side}_price"])
        out.append({"label": f"{side.title()} {line:g}", "side": side, "line": line,
                    "price": price, "assumed": assumed, "prob": p, "push": push})
    return out


def game_edges(r: dict, markets=MARKETS) -> dict:
    """The ``{market}_edge_*`` log columns for one game (pick text empty when there is no edge)."""
    picks = stake_picks({m: best_side(market_sides(r, m)) for m in markets})
    out = {}
    for m, pick in picks.items():
        fields = empty_pick_fields() if pick is None else pick
        out.update({f"{m}_edge_{f}": fields[f] for f in EDGE_FIELDS})
    return out


def edge_frame(rows: pd.DataFrame, markets=MARKETS) -> pd.DataFrame:
    """``game_edges`` for every row, aligned with ``rows``."""
    cols = [f"{m}_edge_{f}" for m in markets for f in EDGE_FIELDS]
    return pd.DataFrame([game_edges(r, markets) for r in rows.to_dict("records")],
                        index=rows.index, columns=cols)


def has_edge(pick) -> bool:
    return isinstance(pick, str) and pick != ""


def grade_edge(market: str, side: str, line: float, price: float, home_score: float,
               away_score: float) -> tuple[str | None, float]:
    """Result (``W``, ``L`` or ``P``) and profit per unit staked."""
    margin, total = home_score - away_score, home_score + away_score
    if market == "spread":
        diff = (margin if side == "home" else -margin) + line
    elif market == "moneyline":
        diff = margin if side == "home" else -margin
    else:
        diff = total - line if side == "over" else line - total
    return settle(diff, price)


def graded_bets(df: pd.DataFrame, market: str) -> pd.DataFrame:
    """One row per staked edge in ``market`` with a final score: result, stake, profit, game and EV.

    Edges logged without a stake (before edges were priced from the final
    prediction and Kelly-sized) are left out.
    """
    stake_col = f"{market}_edge_stake"
    stake = df[stake_col] if stake_col in df else pd.Series(np.nan, index=df.index)
    has = df[f"{market}_edge_pick"].map(has_edge) & df["home_score"].notna() & df["away_score"].notna() \
        & stake.notna()
    bets = df[has]
    rows = []
    for r in bets.to_dict("records"):
        result, per_unit = grade_edge(market, r[f"{market}_edge_side"], r[f"{market}_edge_line"],
                                      r[f"{market}_edge_price"], r["home_score"], r["away_score"])
        s = float(r[stake_col])
        rows.append({"result": result, "stake": s, "profit": s * per_unit, "game": r.get("game_id"),
                     "ev": r[f"{market}_edge_ev"]})
    return pd.DataFrame(rows, index=bets.index, columns=["result", "stake", "profit", "game", "ev"])


def edge_record(df: pd.DataFrame, market: str, n_boot: int = 5000, seed: int = 0) -> dict:
    """Bets, W-L-P, units staked and won, ROI with its 95% range, and the ROI the bets expected."""
    return summarize(graded_bets(df, market), n_boot=n_boot, seed=seed)
