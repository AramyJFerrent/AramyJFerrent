"""Betting edges: expected value of each side of the run line, moneyline and total.

Every edge uses the final prediction's chances: the model's runs blended with
the market's (backed out of its moneyline and total), simulated against the
posted run line and total, and anchored to the market's own chances so the
simulator's shape cannot pose as an edge (``market.edge_chances``). For a bet
at American price ``A`` the decimal price is ``d = 1 + A/100`` (``A > 0``) or
``1 + 100/|A|``, and with win, push and loss chances ``p``, ``q`` and
``1 - p - q`` the expected profit per unit staked is

    EV = p (d - 1) - (1 - p - q)

A side is an edge when its EV is at least ``EDGE_MIN_EV``; each market
reports its best side, staked at a fraction of the Kelly stake with one
game's edges sharing a cap (``bettingcore.edges``). The model's own chances
before the blend (``model_*`` columns) can be priced the same way for
comparison. Posted prices are used wherever ESPN gives them. A total without
a price is assumed to be -110 on both sides (marked as assumed); the run line
and the moneyline are never priced near -110, so without a price they get no
edge.
"""

from __future__ import annotations

import numpy as np
import pandas as pd
from bettingcore import EDGE_FIELDS, best_side, empty_pick_fields, format_american, settle, stake_picks, summarize

ASSUMED_PRICE = -110.0
MARKETS = ("spread", "moneyline", "total")
MARKET_NAMES = {"spread": "Run line", "moneyline": "Moneyline", "total": "Total"}
EDGE_COLUMNS = [f"{m}_edge_{f}" for m in MARKETS for f in EDGE_FIELDS]
# The run line the model quotes when none is posted: the model's favorite at -1.5.
DEFAULT_RUN_LINE = 1.5
# The columns each rule reads its chances from: the final prediction's anchored
# chances, or the model's own before the blend.
CHANCES = {
    "final": {"win": "edge_home_ml_prob", "home_cover": "edge_home_cover_prob",
              "away_cover": "edge_away_cover_prob", "over": "edge_over_prob", "under": "edge_under_prob",
              "total_push": "edge_total_push_prob"},
    "model": {"win": "model_home_prob", "home_cover": "model_home_cover_prob",
              "away_cover": "model_away_cover_prob", "over": "model_over_prob", "under": "model_under_prob",
              "total_push": "model_total_push_prob"},
}


def american(price) -> str:
    return format_american(price)


def _ok(x) -> bool:
    return x is not None and not pd.isna(x)


def market_options(r, chances: str = "final") -> dict[str, list[dict]]:
    """Both sides of each market for one game (a log row): label, side, line,
    price, whether the price was assumed, and the chosen rule's win and push
    chances. A market with no line has no options; a side with no price is left out."""
    c = CHANCES[chances]
    home, away = r["home_team"], r["away_team"]
    out = {m: [] for m in MARKETS}
    hl = r.get("home_run_line")
    if _ok(hl):
        p_home, p_away = r.get(c["home_cover"]), r.get(c["away_cover"])
        push = max(0.0, 1.0 - p_home - p_away) if _ok(p_home) and _ok(p_away) else 0.0
        for side, team, line, price, p in (("home", home, hl, r.get("home_run_line_price"), p_home),
                                           ("away", away, -hl, r.get("away_run_line_price"), p_away)):
            if _ok(price) and _ok(p):
                out["spread"].append({"label": f"{team} {line:+g}", "side": side, "line": float(line),
                                      "price": float(price), "assumed": False, "prob": float(p), "push": push})
    p = r.get(c["win"])
    if _ok(p):
        for side, team, price, pw in (("home", home, r.get("home_moneyline"), p),
                                      ("away", away, r.get("away_moneyline"), 1.0 - p)):
            if _ok(price):
                out["moneyline"].append({"label": team, "side": side, "price": float(price), "assumed": False,
                                         "prob": float(pw), "push": 0.0})
    tl = r.get("total_line")
    if _ok(tl):
        push = r.get(c["total_push"])
        push = float(push) if _ok(push) else 0.0
        for side, price, pw in (("over", r.get("over_price"), r.get(c["over"])),
                                ("under", r.get("under_price"), r.get(c["under"]))):
            if _ok(pw):
                out["total"].append({"label": f"{side.title()} {tl:g}", "side": side, "line": float(tl),
                                     "price": float(price) if _ok(price) else ASSUMED_PRICE,
                                     "assumed": not _ok(price), "prob": float(pw), "push": push})
    return out


def add_edges(frame: pd.DataFrame, chances: str = "final") -> pd.DataFrame:
    """``frame`` with the best side of each market filled into the ``*_edge_*`` columns
    (pick empty and the rest NaN where no side clears the bar), priced with the
    chosen rule's chances."""
    out = frame.copy()
    values = {c: [] for c in EDGE_COLUMNS}
    for _, r in out.iterrows():
        opts = market_options(r, chances)
        picks = stake_picks({m: best_side(opts[m]) for m in MARKETS})
        for m, pick in picks.items():
            fields = empty_pick_fields() if pick is None else pick
            for f in EDGE_FIELDS:
                values[f"{m}_edge_{f}"].append(fields[f])
    for c, v in values.items():
        out[c] = pd.Series(v, index=out.index, dtype=object if c.endswith(("_pick", "_side")) else float)
    return out


def grade_pick(market: str, side: str, line: float, price: float, home_score: float,
               away_score: float) -> tuple[str | None, float]:
    """Result (W, L or P) and profit per unit staked, from the final score."""
    if market == "total":
        diff = (home_score + away_score - line) * (1 if side == "over" else -1)
    else:
        own, other = (home_score, away_score) if side == "home" else (away_score, home_score)
        diff = own - other + (0.0 if market == "moneyline" or pd.isna(line) else line)
    return settle(diff, price)


def graded_edges(frame: pd.DataFrame, market: str) -> pd.DataFrame:
    """Each finished game's staked ``market`` edge with its result, stake, profit, game and EV.

    Edges logged without a stake (before edges were priced from the final
    prediction and Kelly-sized) are left out.
    """
    pick = frame[f"{market}_edge_pick"]
    stake = frame[f"{market}_edge_stake"] if f"{market}_edge_stake" in frame else pd.Series(np.nan, index=frame.index)
    d = frame[pick.notna() & pick.astype(str).ne("") & frame["home_score"].notna() & frame["away_score"].notna()
              & stake.notna()]
    graded = [grade_pick(market, r[f"{market}_edge_side"], r[f"{market}_edge_line"], r[f"{market}_edge_price"],
                         r["home_score"], r["away_score"]) for _, r in d.iterrows()]
    stakes = d[f"{market}_edge_stake"].to_numpy(float) if len(d) else np.array([])
    return pd.DataFrame({"result": [g[0] for g in graded], "stake": stakes,
                         "profit": stakes * np.array([g[1] for g in graded], dtype=float),
                         "game": d["game_id"].to_numpy() if "game_id" in d else None,
                         "ev": d[f"{market}_edge_ev"].to_numpy(float)}, index=d.index)


def edge_record(frame: pd.DataFrame, market: str, n_boot: int = 5000, seed: int = 0) -> dict:
    """Bets, W-L-P, units staked and won, ROI with its 95% range over games, and expected ROI."""
    return summarize(graded_edges(frame, market), n_boot=n_boot, seed=seed)
