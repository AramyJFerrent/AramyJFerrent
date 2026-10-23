"""Betting edges: the final prediction's chances against the posted prices.

Each game has three markets: the spread, the moneyline and the total. For
every side of each market the expected value of a 1-unit bet at the posted
American price is

    EV = p_win * (decimal odds - 1) - p_loss

with ``p_win``, ``p_push`` and ``p_loss = 1 - p_win - p_push`` taken from the
final prediction (the model blended with the line, simulated against the
posted lines and anchored to the market's own chances, see
``ScoreModel.edge_chances``); a push returns the stake. The side with the
highest EV is the market's edge when its EV is at least ``EDGE_MIN_EV``, and
it is staked at a fraction of the Kelly stake, one game's edges sharing a cap
(``bettingcore.edges``). The model's own chances before the blend (the
``model_*`` columns) can be priced the same way for comparison.

Spreads and totals are standard -110 markets, so a side whose price was not
posted is assumed to be -110 (and marked as assumed); a moneyline without a
price is never guessed.
"""

from __future__ import annotations

import math

import numpy as np
import pandas as pd
from bettingcore import EDGE_FIELDS, best_side, empty_pick_fields, settle, stake_picks, summarize

ASSUMED_PRICE = -110.0
# Markets priced near -110 on both sides, where a missing price may be assumed.
ASSUMABLE = ("spread", "total")
MARKETS = ("spread", "moneyline", "total")
EDGE_COLUMNS = [f"{m}_edge_{f}" for m in MARKETS for f in EDGE_FIELDS]
# The price each side of each market is posted at, by log column.
PRICE_COLUMNS = {
    ("spread", "home"): "home_spread_price", ("spread", "away"): "away_spread_price",
    ("moneyline", "home"): "home_moneyline", ("moneyline", "away"): "away_moneyline",
    ("total", "over"): "over_price", ("total", "under"): "under_price",
}
# The columns each rule reads its chances from: the final prediction's anchored
# chances, or the model's own before the blend.
CHANCES = {
    "final": {"cover": "edge_home_cover_prob", "spread_push": "edge_spread_push_prob", "over": "edge_over_prob",
              "total_push": "edge_total_push_prob", "win": "edge_home_ml_prob"},
    "model": {"cover": "model_home_cover_prob", "spread_push": "model_spread_push_prob", "over": "model_over_prob",
              "total_push": "model_total_push_prob", "win": "model_home_prob"},
}


def _missing(x) -> bool:
    return x is None or (isinstance(x, float) and math.isnan(x)) or pd.isna(x)


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


def market_options(row, market: str, chances: str = "final") -> list[dict]:
    """Both sides of ``market`` for one game, with the chosen rule's chances. ``row``
    carries the line columns (``spread`` is the home team's expected margin),
    the prices and the chances (``CHANCES``)."""
    c = CHANCES[chances]
    home, away = _get(row, "home_team"), _get(row, "away_team")
    out = []
    if market == "spread":
        spread, cover, push = _get(row, "spread"), _get(row, c["cover"]), _get(row, c["spread_push"])
        if _missing(spread) or _missing(cover):
            return []
        push = 0.0 if _missing(push) else push
        for side, team, line, p in (("home", home, -spread, cover), ("away", away, spread, 1.0 - cover - push)):
            price, assumed = _price(row, market, side)
            out.append({"label": f"{team} {line_text(line)}", "side": side, "line": float(line), "price": price,
                        "assumed": assumed, "prob": p, "push": push})
    elif market == "moneyline":
        p_home = _get(row, c["win"])
        if _missing(p_home):
            return []
        for side, team, p in (("home", home, p_home), ("away", away, 1.0 - p_home)):
            price, assumed = _price(row, market, side)
            out.append({"label": f"{team} ML", "side": side, "price": price, "assumed": assumed, "prob": p,
                        "push": 0.0})
    elif market == "total":
        total, over, push = _get(row, "total"), _get(row, c["over"]), _get(row, c["total_push"])
        if _missing(total) or _missing(over):
            return []
        push = 0.0 if _missing(push) else push
        for side, p in (("over", over), ("under", 1.0 - over - push)):
            price, assumed = _price(row, market, side)
            out.append({"label": f"{side.title()} {total:g}", "side": side, "line": float(total), "price": price,
                        "assumed": assumed, "prob": p, "push": push})
    return out


def has_market(row, market: str) -> bool:
    """Whether the game has a line (or a price) for ``market`` yet."""
    if market == "moneyline":
        return not (_missing(_get(row, "home_moneyline")) and _missing(_get(row, "away_moneyline")))
    return not _missing(_get(row, market))


def edge_columns(df: pd.DataFrame, chances: str = "final") -> pd.DataFrame:
    """The ``{market}_edge_*`` columns for every row of ``df`` (empty pick when there is no edge)."""
    out = {c: [] for c in EDGE_COLUMNS}
    for row in df.to_dict("records"):
        picks = stake_picks({m: best_side(market_options(row, m, chances)) for m in MARKETS})
        for m, pick in picks.items():
            fields = empty_pick_fields() if pick is None else pick
            for f in EDGE_FIELDS:
                out[f"{m}_edge_{f}"].append(fields[f])
    res = pd.DataFrame(out, index=df.index)
    for m in MARKETS:
        for f in EDGE_FIELDS:
            res[f"{m}_edge_{f}"] = res[f"{m}_edge_{f}"].astype(object if f in ("pick", "side") else float)
    return res


def price_assumed(row, market: str) -> bool:
    """Whether the logged edge's price was assumed rather than posted."""
    side = _get(row, f"{market}_edge_side")
    if market not in ASSUMABLE or not isinstance(side, str) or not side:
        return False
    return _missing(_get(row, PRICE_COLUMNS[(market, side)]))


def grade_edge(market: str, side: str, line: float, price: float, home_score: float, away_score: float):
    """Result (``W``, ``L`` or ``P``) and profit per unit staked, or (None, nan) before the result."""
    if _missing(home_score) or _missing(away_score) or not isinstance(side, str) or not side:
        return None, np.nan
    if market == "total":
        res = (home_score + away_score - line) * (1 if side == "over" else -1)
    else:
        res = (home_score - away_score) * (1 if side == "home" else -1)
        if market == "spread":
            res += line
    return settle(res, price)


def graded(df: pd.DataFrame, market: str) -> pd.DataFrame:
    """Every finished game with a staked edge in ``market``: result, stake, profit, game and EV.

    Edges logged without a stake (before edges were priced from the final
    prediction and Kelly-sized) are left out.
    """
    pick = df[f"{market}_edge_pick"]
    stake = df[f"{market}_edge_stake"] if f"{market}_edge_stake" in df else pd.Series(np.nan, index=df.index)
    d = df[pick.notna() & (pick.astype(str) != "") & df["home_score"].notna() & df["away_score"].notna()
           & stake.notna()]
    res = [grade_edge(market, r[f"{market}_edge_side"], r[f"{market}_edge_line"], r[f"{market}_edge_price"],
                      r["home_score"], r["away_score"]) for r in d.to_dict("records")]
    stakes = d[f"{market}_edge_stake"].to_numpy(float) if len(d) else np.array([])
    return pd.DataFrame({"result": [r[0] for r in res], "stake": stakes,
                         "profit": stakes * np.array([r[1] for r in res], dtype=float),
                         "game": d["game_id"].to_numpy() if "game_id" in d else None,
                         "ev": d[f"{market}_edge_ev"].to_numpy(float)}, index=d.index)


def record(df: pd.DataFrame, market: str, n_boot: int = 5000, seed: int = 0) -> dict:
    """Bets, W-L-P, units staked and won, ROI with its 95% range over games, and expected ROI in ``market``."""
    return summarize(graded(df, market), n_boot=n_boot, seed=seed)


def moved_toward(side: pd.Series, first_spread: pd.Series, last_spread: pd.Series) -> tuple[int, int]:
    """Of the games whose spread moved between two lines with a spread edge
    on the first, how many moved toward the edge's ``side`` (a home edge
    wants the home team's expected margin to grow), and how many moved."""
    move = last_spread - first_spread
    moved = side.isin(["home", "away"]) & move.notna() & (move != 0)
    toward = np.where(side[moved] == "home", move[moved] > 0, move[moved] < 0)
    return int(toward.sum()), int(moved.sum())
