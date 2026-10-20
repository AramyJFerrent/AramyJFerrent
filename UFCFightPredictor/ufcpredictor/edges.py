"""Betting edges: expected value of each market's sides from the model alone.

Three markets per bout: the moneyline, the round total (over/under x.5
rounds) and the method of victory (each fighter by KO/TKO, submission or
decision). Every side is valued with the model's own probabilities, before
the blend with the betting market (``p_model`` and the method and round
splits applied to it), at the posted American price. A side is an edge when
its expected value per unit staked is at least ``EDGE_MIN_EV``; the best such
side of each market is the pick.

UFC props and moneylines are never priced near -110, so a missing price is
never assumed: the market shows the model's fair odds instead.

Round totals: "Over 1.5 rounds" wins when the fight lasts past 2:30 of round
2, and a fight that goes the distance is always over. The model gives the
chance of a finish in each round but not when within the round, so finish
times are assumed to be spread evenly over the five minutes: half of a
round's finishes count before the midpoint. (Since 2015 about 45% of UFC
finishes came in the first half of their round, so this slightly understates
overs on lines inside a likely finishing round.)
"""

from __future__ import annotations

import math
from dataclasses import dataclass

import numpy as np
import pandas as pd

EDGE_MIN_EV = 0.03
MARKETS = ["moneyline", "rounds", "method"]
MARKET_NAMES = {"moneyline": "Moneyline", "rounds": "Round total", "method": "Method of victory"}
EDGE_FIELDS = ["pick", "side", "line", "price", "prob", "ev"]
EDGE_COLUMNS = [f"{m}_edge_{k}" for m in MARKETS for k in EDGE_FIELDS]
METHODS = ["ko", "sub", "dec"]
METHOD_NAMES = {"ko": "KO/TKO", "sub": "submission", "dec": "decision"}
SIX = [f"{s}_{m}" for s in "ab" for m in METHODS]
MAX_ROUNDS = 5


# ---- price math -----------------------------------------------------------

def decimal_odds(american):
    """Decimal odds (stake included) for an American price; arrays work elementwise."""
    ml = np.asarray(american, dtype=float)
    with np.errstate(divide="ignore", invalid="ignore"):
        out = np.where(ml < 0, 1 + 100.0 / -ml, 1 + ml / 100.0)
    return float(out) if out.ndim == 0 else out


def implied_prob(american):
    """Chance an American price implies, bookmaker margin included."""
    ml = np.asarray(american, dtype=float)
    with np.errstate(divide="ignore", invalid="ignore"):
        out = np.where(ml < 0, -ml / (-ml + 100.0), 100.0 / (ml + 100.0))
    return float(out) if out.ndim == 0 else out


def fair_american(p: float) -> int:
    """Fair (no-vig) American odds for win probability ``p``, rounded to 5."""
    p = min(max(p, 0.01), 0.99)
    raw = -100.0 * p / (1.0 - p) if p > 0.5 else 100.0 * (1.0 - p) / p
    return int(5 * math.floor(raw / 5 + 0.5))


def expected_value(p_win: float, p_push: float, american: float) -> float:
    """Expected profit per unit staked: a push returns the stake."""
    d = decimal_odds(american)
    return p_win * (d - 1) - (1 - p_win - p_push)


def fmt_american(odds) -> str:
    if odds is None or pd.isna(odds):
        return "–"
    odds = int(round(float(odds)))
    return f"+{odds}" if odds > 0 else str(odds)


# ---- picking a side -------------------------------------------------------

@dataclass
class Pick:
    label: str              # e.g. "Volkanovski by KO/TKO", "Over 1.5 rounds"
    side: str               # "a"/"b", "over"/"under", "a_ko" ... "b_dec"
    line: float             # the round line, NaN for moneyline and method
    price: float            # American price
    assumed: bool           # price assumed (never for UFC markets)
    prob: float             # model chance the side wins
    ev: float               # expected profit per unit

    def cell(self) -> str:
        price = fmt_american(self.price) + ("*" if self.assumed else "")
        return f"{self.label} ({price}): EV {100 * self.ev:+.1f}%, model {100 * self.prob:.0f}%"

    def to_log(self, market: str) -> dict:
        return {f"{market}_edge_pick": self.label, f"{market}_edge_side": self.side,
                f"{market}_edge_line": self.line, f"{market}_edge_price": self.price,
                f"{market}_edge_prob": self.prob, f"{market}_edge_ev": self.ev}


def best_side(options: list[dict], min_ev: float = EDGE_MIN_EV) -> Pick | None:
    """The side with the highest expected value if it clears ``min_ev``, else None.

    Each option needs ``label``, ``side``, ``prob`` and ``price``, and may carry
    ``push`` (chance the stake comes back), ``line`` and ``assumed``. Options
    without a price or probability are skipped.
    """
    best = None
    for o in options:
        price, prob = o.get("price"), o.get("prob")
        if price is None or prob is None or pd.isna(price) or pd.isna(prob):
            continue
        ev = expected_value(float(prob), float(o.get("push", 0.0) or 0.0), float(price))
        if best is None or ev > best.ev:
            best = Pick(o["label"], o["side"], float(o.get("line", np.nan)), float(price),
                        bool(o.get("assumed", False)), float(prob), float(ev))
    return best if best is not None and best.ev >= min_ev else None


def settle(outcome: str, price: float) -> float:
    """Units won on a one-unit bet: ``outcome`` is win, loss or push."""
    if outcome == "win":
        return float(decimal_odds(price)) - 1
    return -1.0 if outcome == "loss" else 0.0


# ---- round totals ---------------------------------------------------------

def over_prob(by_round, distance: float, rounds: int, line: float) -> float:
    """Chance the fight lasts past the midpoint of round ``floor(line) + 1``.

    ``by_round`` holds the finish chance in rounds 1..5 and ``distance`` the
    chance it goes to the judges. Lines must be x.5 inside the scheduled
    length (0.5 to 2.5 for three rounds, up to 4.5 for five); anything else is
    NaN.
    """
    if pd.isna(line) or pd.isna(distance) or pd.isna(rounds):
        return np.nan
    k = math.floor(float(line))
    if abs(float(line) - k - 0.5) > 1e-9 or not 0 <= k < int(rounds):
        return np.nan
    p = [0.0 if pd.isna(x) else float(x) for x in by_round]
    # Finished in rounds after k+1, or in round k+1 after its midpoint.
    return float(distance) + sum(p[k + 1:int(rounds)]) + 0.5 * p[k]


def fair_round_line(by_round, distance: float, rounds: int) -> tuple[float, float]:
    """The x.5 line whose over chance is closest to 50%, and that chance."""
    lines = [k + 0.5 for k in range(int(rounds))] if not pd.isna(rounds) else []
    probs = [over_prob(by_round, distance, rounds, x) for x in lines]
    ok = [(abs(p - 0.5), x, p) for x, p in zip(lines, probs) if not np.isnan(p)]
    if not ok:
        return np.nan, np.nan
    _, line, p = min(ok)
    return line, p


def _rounds_of(r) -> tuple[list, float, int]:
    return ([getattr(r, f"model_r{k}", np.nan) for k in range(1, MAX_ROUNDS + 1)],
            getattr(r, "model_distance", np.nan), getattr(r, "rounds", np.nan))


# ---- the three UFC markets --------------------------------------------------

def _surname(name) -> str:
    return str(name).split()[-1] if isinstance(name, str) and name.split() else str(name)


def _has(r, col) -> bool:
    v = getattr(r, col, np.nan)
    return v is not None and not pd.isna(v)


def moneyline_pick(r) -> Pick | None:
    """Each fighter at his moneyline, valued with the model-alone win chance.

    Draws are rare and not modeled; books refund moneylines on a draw, so
    they would be pushes.
    """
    p = getattr(r, "p_model", np.nan)
    return best_side([
        {"label": _surname(r.fighter_a), "side": "a", "prob": p, "price": getattr(r, "odds_a", np.nan)},
        {"label": _surname(r.fighter_b), "side": "b", "prob": 1 - p, "price": getattr(r, "odds_b", np.nan)},
    ])


def method_pick(r) -> Pick | None:
    """Each fighter by KO/TKO, submission or decision, at the method props' prices."""
    opts = []
    for s in "ab":
        name = _surname(getattr(r, f"fighter_{s}"))
        for m in METHODS:
            opts.append({"label": f"{name} by {METHOD_NAMES[m]}", "side": f"{s}_{m}",
                         "prob": getattr(r, f"model_{s}_{m}", np.nan), "price": getattr(r, f"odds_{s}_{m}", np.nan)})
    return best_side(opts)


def rounds_pick(r) -> Pick | None:
    """Over and under the posted round line."""
    line = getattr(r, "rounds_line", np.nan)
    p = over_prob(*_rounds_of(r), line)
    if np.isnan(p):
        return None
    return best_side([
        {"label": f"Over {line:g} rounds", "side": "over", "line": line, "prob": p,
         "price": getattr(r, "over_price", np.nan)},
        {"label": f"Under {line:g} rounds", "side": "under", "line": line, "prob": 1 - p,
         "price": getattr(r, "under_price", np.nan)},
    ])


PICKERS = {"moneyline": moneyline_pick, "rounds": rounds_pick, "method": method_pick}


def priced(r, market: str) -> bool:
    """Whether the bout has a price on at least one side of ``market``."""
    if market == "moneyline":
        return _has(r, "odds_a") or _has(r, "odds_b")
    if market == "rounds":
        return _has(r, "rounds_line") and (_has(r, "over_price") or _has(r, "under_price"))
    return any(_has(r, f"odds_{c}") for c in SIX)


def attach_edges(rows: pd.DataFrame) -> pd.DataFrame:
    """Fill ``model_over_prob`` and the ``{market}_edge_*`` columns of log-shaped rows."""
    rows = rows.copy()
    for col in EDGE_COLUMNS:
        rows[col] = None if col.endswith(("_pick", "_side")) else np.nan
    over = []
    for idx, r in zip(rows.index, rows.itertuples(index=False)):
        over.append(over_prob(*_rounds_of(r), getattr(r, "rounds_line", np.nan)))
        for market, picker in PICKERS.items():
            pick = picker(r)
            if pick is not None:
                for col, v in pick.to_log(market).items():
                    rows.at[idx, col] = v
    rows["model_over_prob"] = over
    return rows


def edge_cell(r, market: str) -> str:
    """Display text for one market of one bout."""
    pick = getattr(r, f"{market}_edge_pick", None)
    if isinstance(pick, str) and pick:
        return Pick(pick, getattr(r, f"{market}_edge_side"), getattr(r, f"{market}_edge_line"),
                    getattr(r, f"{market}_edge_price"), False, getattr(r, f"{market}_edge_prob"),
                    getattr(r, f"{market}_edge_ev")).cell()
    if priced(r, market):
        return "no edge"
    if market == "moneyline":
        return "no line yet"
    if market == "rounds":
        line, p = fair_round_line(*_rounds_of(r))
        if np.isnan(p):
            return "no line yet"
        return (f"no price yet; fair Over {line:g} {fmt_american(fair_american(p))}, "
                f"Under {fmt_american(fair_american(1 - p))}")
    probs = [getattr(r, f"model_{c}", np.nan) for c in SIX]
    if any(pd.isna(p) for p in probs):
        return "no line yet"
    fair = [fmt_american(fair_american(p)) for p in probs]
    return ("no prices yet; fair KO / Sub / Dec<br>"
            f"{_surname(r.fighter_a)} {' / '.join(fair[:3])}<br>{_surname(r.fighter_b)} {' / '.join(fair[3:])}")


# ---- grading ----------------------------------------------------------------

def outcome(market: str, side: str, line: float, status: str, winner, method, end_round, end_seconds) -> str | None:
    """win, loss or push for a logged pick once the result is in; None while unknown.

    A no contest voids every bet. A draw refunds the moneyline, loses every
    method bet and settles the round total on the fight's length. A finish
    exactly at the midpoint of the line's round counts as over; one with no
    recorded time stays ungraded.
    """
    if status == "no contest":
        return "push"
    if status not in ("final", "draw"):
        return None
    if market == "moneyline":
        return "push" if status == "draw" else ("win" if winner == side else "loss")
    if market == "method":
        if status == "draw":
            return "loss"
        m = str(method).lower()
        if m not in METHODS:
            return None
        return "win" if f"{winner}_{m}" == side else "loss"
    if market == "rounds":
        if pd.isna(line):
            return None
        if str(method).upper() == "DEC" or status == "draw":
            lasted = math.inf
        elif pd.isna(end_round):
            return None
        else:
            if pd.isna(end_seconds):
                return None
            lasted = int(end_round) - 1 + float(end_seconds) / 300.0
        # In rounds of fighting: over 1.5 needs 2:30 of round 2, i.e. 1.5 rounds.
        won_over = lasted >= float(line)
        return "win" if won_over == (side == "over") else "loss"
    return None


def record(entries: pd.DataFrame, market: str) -> dict:
    """W-L-P, units and ROI of one market's logged picks that have been settled."""
    w = l = p = 0
    units = 0.0
    col = f"{market}_edge_pick"
    if col not in entries:
        return {"edges": 0, "wins": 0, "losses": 0, "pushes": 0, "units": 0.0, "roi": np.nan}
    g = entries[entries[col].notna() & entries[col].astype(str).ne("")]
    for r in g.itertuples(index=False):
        res = outcome(market, getattr(r, f"{market}_edge_side"), getattr(r, f"{market}_edge_line"), r.status,
                      r.winner, r.method, r.end_round, getattr(r, "end_seconds", np.nan))
        if res is None:
            continue
        w, l, p = w + (res == "win"), l + (res == "loss"), p + (res == "push")
        units += settle(res, getattr(r, f"{market}_edge_price"))
    n = w + l + p
    return {"edges": n, "wins": w, "losses": l, "pushes": p, "units": units, "roi": units / n if n else np.nan}
