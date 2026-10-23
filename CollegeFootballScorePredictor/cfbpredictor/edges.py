"""Betting edges: expected value of each side of a market at the posted price.

Probabilities come from the final prediction (the model blended with the line
by the weight that has predicted best in recent seasons, run through the score
simulator against the posted lines), anchored to the market's own chances so
the simulator's shape cannot pose as an edge (``ScoreModel.edge_chances``). The model's own numbers disagree with
the line in most games, but in walk-forward tests most of that disagreement
was noise; the blend keeps the share the model has earned. A side is an edge
when its expected value per unit staked is at least ``EDGE_MIN_EV``, and it
is staked at a fraction of the Kelly stake, one game's edges sharing a cap
(``bettingcore.edges``). Pushes return the stake.

Spreads and totals whose price is not posted are assumed to be -110 on both
sides (the standard price for those markets) and marked as assumed;
moneylines are never assumed.

Bowl games other than the playoff get no edges: players sitting out to
prepare for the draft or to transfer move those lines, and no free source
lists who sits, so the model cannot know what the market does.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from bettingcore import (
    EDGE_FIELDS,
    best_side,
    empty_pick_fields,
    settle,
    stake_picks,
    summarize,
    valid_price,
)

ASSUMED_PRICE = -110.0
MARKETS = ("spread", "moneyline", "total")
# Markets normally priced near -110, where a missing price may be assumed.
STANDARD_MARKETS = {"spread", "total"}
# Columns of the chances each rule prices edges with: the final prediction's,
# anchored to the market (``ScoreModel.edge_chances``), or (prefix ``model_``)
# the model's own before the blend, kept for comparison.
CHANCE_COLUMNS = {"cover": "home_cover_prob", "spread_push": "spread_push_prob", "over": "over_prob",
                  "total_push": "total_push_prob", "win": "home_ml_prob"}


def chance_columns(prefix: str = "") -> dict:
    """The columns holding each chance for the rule with ``prefix`` ("" or "model_")."""
    if not prefix:
        return dict(CHANCE_COLUMNS)
    return {**{k: f"{prefix}{v}" for k, v in CHANCE_COLUMNS.items()}, "win": f"{prefix}home_win_prob"}


def edge_columns(fields=EDGE_FIELDS) -> list[str]:
    return [f"{m}_edge_{f}" for m in MARKETS for f in fields]


def market_price(price, market: str) -> tuple[float, bool]:
    """The price to evaluate and whether it was assumed (-110 for an unposted spread or total)."""
    if valid_price(price):
        return float(price), False
    if market in STANDARD_MARKETS:
        return ASSUMED_PRICE, True
    return np.nan, False


def _team_line(points: float) -> str:
    return "PK" if abs(points) < 0.05 else f"{points:+.1f}"


def game_sides(r, prefix: str = "") -> dict[str, list[dict]]:
    """Both sides of each market for one game (a log row or anything with the same fields).

    ``spread_line`` is the expected home margin (positive when the home team is
    favored), so the home team's spread is its negative. Chances are read from
    ``chance_columns(prefix)``: the final prediction's by default, ``model_`` for
    the model's own. The away side's are what is left after the home side and
    the push.
    """
    c = chance_columns(prefix)
    home, away = r["home_team"], r["away_team"]
    sides = {m: [] for m in MARKETS}
    spread = r["spread_line"]
    if pd.notna(spread):
        p_home, push = r[c["cover"]], r[c["spread_push"]]
        push = 0.0 if pd.isna(push) else push
        for side, team, line, p, price in (
                ("home", home, -spread, p_home, r["home_spread_price"]),
                ("away", away, spread, 1.0 - p_home - push, r["away_spread_price"])):
            price, assumed = market_price(price, "spread")
            sides["spread"].append({"label": f"{team} {_team_line(line)}", "side": side, "line": float(line),
                                    "price": price, "assumed": assumed, "prob": p, "push": push})
    p_home = r[c["win"]]
    for side, team, p, price in (("home", home, p_home, r["home_moneyline"]),
                                 ("away", away, 1.0 - p_home, r["away_moneyline"])):
        sides["moneyline"].append({"label": team, "side": side, "price": price, "prob": p, "push": 0.0})
    total = r["total_line"]
    if pd.notna(total):
        p_over, push = r[c["over"]], r[c["total_push"]]
        push = 0.0 if pd.isna(push) else push
        for side, p, price in (("over", p_over, r["over_price"]), ("under", 1.0 - p_over - push, r["under_price"])):
            price, assumed = market_price(price, "total")
            sides["total"].append({"label": f"{side.title()} {total:g}", "side": side, "line": float(total),
                                   "price": price, "assumed": assumed, "prob": p, "push": push})
    return sides


def no_edges(r) -> bool:
    """A game that gets no edges: a bowl outside the playoff (see above)."""
    bowl = r.get("bowl", False)
    return bool(bowl) and not pd.isna(bowl)


def game_edges(r, prefix: str = "") -> dict:
    """The ``{market}_edge_*`` fields for one game; empty pick and NaNs where there is no edge."""
    sides = {m: [] for m in MARKETS} if no_edges(r) else game_sides(r, prefix)
    picks = stake_picks({m: best_side(opts) for m, opts in sides.items()})
    out = {}
    for market, pick in picks.items():
        fields = empty_pick_fields() if pick is None else pick
        out.update({f"{market}_edge_{f}": fields[f] for f in EDGE_FIELDS})
    return out


def edge_frame(df: pd.DataFrame, prefix: str = "") -> pd.DataFrame:
    """``game_edges`` for every row, indexed like ``df``."""
    rows = [game_edges(r, prefix) for _, r in df.iterrows()]
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
               away_score: float) -> tuple[str | None, float]:
    """Result (``W``, ``L`` or ``P``) and profit per unit staked, from the final score."""
    margin, total = home_score - away_score, home_score + away_score
    if market == "spread":
        res = (margin if side == "home" else -margin) + line
    elif market == "moneyline":
        res = margin if side == "home" else -margin
    else:
        res = total - line if side == "over" else line - total
    return settle(res, price)


def edge_results(df: pd.DataFrame, market: str) -> pd.DataFrame:
    """Graded, staked edges in ``market`` from rows with final scores: result, stake, profit, game,
    EV, whether the price was assumed and the season. Edges logged without a stake (before edges
    were priced from the final prediction and Kelly-sized) are left out."""
    cols = ["result", "stake", "profit", "game", "ev", "assumed", "season"]
    pick = df[f"{market}_edge_pick"].astype(object).fillna("").astype(str)
    stake = df[f"{market}_edge_stake"] if f"{market}_edge_stake" in df else pd.Series(np.nan, index=df.index)
    done = df[(pick != "") & df["home_score"].notna() & df["away_score"].notna() & stake.notna()]
    rows = []
    for _, r in done.iterrows():
        result, per_unit = grade_edge(market, r[f"{market}_edge_side"], r[f"{market}_edge_line"],
                                      r[f"{market}_edge_price"], r["home_score"], r["away_score"])
        s = float(r[f"{market}_edge_stake"])
        rows.append({"result": result, "stake": s, "profit": s * per_unit, "game": r.get("game_id"),
                     "ev": r[f"{market}_edge_ev"], "assumed": assumed_price(r, market),
                     "season": r.get("season", np.nan)})
    return pd.DataFrame(rows, columns=cols)


def record(results: pd.DataFrame, n_boot: int = 5000, seed: int = 0) -> dict:
    """Bets, W-L-P, units staked and won, ROI with a 95% range over games, and expected ROI."""
    return summarize(results, n_boot=n_boot, seed=seed)

