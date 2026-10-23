"""Betting edges: expected value of each market's sides from the final prediction.

Three markets per bout: the moneyline, the round total (over/under x.5
rounds) and the method of victory (each fighter by KO/TKO, submission or
decision). Every side is valued at its posted American price with the final
prediction's chances (``CHANCES["final"]``): the win chance blended with the
de-vigged moneyline, which already corrects the market's favorite-longshot
bias, and method and round chances anchored to their own props (the props'
de-vigged chances, moved by what the blend's win chance changes in the method
and round models; see ``FightModel.edge_chances``). A side is an edge when its
expected value per unit staked is at least ``EDGE_MIN_EV``; the best such side
of each market is the pick, staked at a fraction of the Kelly stake with one
bout's picks sharing a cap (``bettingcore.edges``). Two other sets of chances
can be priced the same way for comparison: the blended forecast's own method
and round split (``"blend"``) and the model alone before the blend
(``"model"``, the rule used before).

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
from bettingcore import best_side as _best_side
from bettingcore import fair_american, format_american, payout, stake_picks, summarize

EDGE_MIN_EV = 0.03
MARKETS = ["moneyline", "rounds", "method"]
MARKET_NAMES = {"moneyline": "Moneyline", "rounds": "Round total", "method": "Method of victory"}
EDGE_FIELDS = ["pick", "side", "line", "price", "prob", "ev", "stake"]
EDGE_COLUMNS = [f"{m}_edge_{k}" for m in MARKETS for k in EDGE_FIELDS]
METHODS = ["ko", "sub", "dec"]
METHOD_NAMES = {"ko": "KO/TKO", "sub": "submission", "dec": "decision"}
SIX = [f"{s}_{m}" for s in "ab" for m in METHODS]
MAX_ROUNDS = 5
# Where each rule's chances live: fighter A's win chance, the six method
# chances, and the over chance at the posted round line (None: worked out from
# the rule's round-by-round chances).
CHANCES = {
    "final": {"win": "p_a", "method": "edge_", "over": "edge_over_prob"},
    "blend": {"win": "p_a", "method": "", "over": None},
    "model": {"win": "p_model", "method": "model_", "over": "model_over_prob"},
}


def fmt_american(odds) -> str:
    return format_american(odds)


# ---- picking a side -------------------------------------------------------

@dataclass
class Pick:
    label: str              # e.g. "Volkanovski by KO/TKO", "Over 1.5 rounds"
    side: str               # "a"/"b", "over"/"under", "a_ko" ... "b_dec"
    line: float             # the round line, NaN for moneyline and method
    price: float            # American price
    assumed: bool           # price assumed (never for UFC markets)
    prob: float             # chance the side wins
    ev: float               # expected profit per unit
    stake: float = float("nan")    # units of 1% of the bankroll

    def cell(self) -> str:
        price = fmt_american(self.price) + ("*" if self.assumed else "")
        stake = "" if pd.isna(self.stake) else f", stake {self.stake:.1f}u"
        return f"{self.label} ({price}): EV {100 * self.ev:+.1f}%, {100 * self.prob:.0f}%{stake}"

    def to_log(self, market: str) -> dict:
        return {f"{market}_edge_pick": self.label, f"{market}_edge_side": self.side,
                f"{market}_edge_line": self.line, f"{market}_edge_price": self.price,
                f"{market}_edge_prob": self.prob, f"{market}_edge_ev": self.ev,
                f"{market}_edge_stake": self.stake}


def best_side(options: list[dict], min_ev: float = EDGE_MIN_EV) -> Pick | None:
    """The side with the highest expected value if it clears ``min_ev``, else None.

    Each option needs ``label``, ``side``, ``prob`` and ``price``, and may carry
    ``push`` (chance the stake comes back), ``line`` and ``assumed``. Options
    without a price or probability are skipped.
    """
    pick = _best_side(options, min_ev)
    if pick is None:
        return None
    return Pick(pick["pick"], pick["side"], pick["line"], pick["price"], pick["assumed"], pick["prob"], pick["ev"])


def settle(outcome: str, price: float) -> float:
    """Profit per unit staked: ``outcome`` is win, loss or push."""
    return payout({"win": "W", "loss": "L", "push": "P"}.get(outcome), price)


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


def _rounds_of(r, prefix: str = "model_") -> tuple[list, float, int]:
    """Round-by-round finish chances, the distance and the scheduled rounds: the model
    alone's (``model_``) or the final prediction's (``""``)."""
    distance = "model_distance" if prefix else "p_distance"
    return ([getattr(r, f"{prefix}r{k}", np.nan) for k in range(1, MAX_ROUNDS + 1)],
            getattr(r, distance, np.nan), getattr(r, "rounds", np.nan))


# ---- the three UFC markets --------------------------------------------------

def _surname(name) -> str:
    return str(name).split()[-1] if isinstance(name, str) and name.split() else str(name)


def _has(r, col) -> bool:
    v = getattr(r, col, np.nan)
    return v is not None and not pd.isna(v)


def moneyline_pick(r, chances: str = "final") -> Pick | None:
    """Each fighter at his moneyline, valued with the rule's win chance.

    Draws are rare and not modeled; books refund moneylines on a draw, so
    they would be pushes.
    """
    p = getattr(r, CHANCES[chances]["win"], np.nan)
    return best_side([
        {"label": _surname(r.fighter_a), "side": "a", "prob": p, "price": getattr(r, "odds_a", np.nan)},
        {"label": _surname(r.fighter_b), "side": "b", "prob": 1 - p, "price": getattr(r, "odds_b", np.nan)},
    ])


def method_pick(r, chances: str = "final") -> Pick | None:
    """Each fighter by KO/TKO, submission or decision, at the method props' prices."""
    prefix = CHANCES[chances]["method"]
    opts = []
    for s in "ab":
        name = _surname(getattr(r, f"fighter_{s}"))
        for m in METHODS:
            opts.append({"label": f"{name} by {METHOD_NAMES[m]}", "side": f"{s}_{m}",
                         "prob": getattr(r, f"{prefix}{s}_{m}", np.nan), "price": getattr(r, f"odds_{s}_{m}", np.nan)})
    return best_side(opts)


def rounds_over(r, chances: str = "final") -> float:
    """The rule's chance of going over the posted round line."""
    col = CHANCES[chances]["over"]
    line = getattr(r, "rounds_line", np.nan)
    if col is not None:
        return getattr(r, col, np.nan)
    return over_prob(*_rounds_of(r, ""), line)


def rounds_pick(r, chances: str = "final") -> Pick | None:
    """Over and under the posted round line."""
    line = getattr(r, "rounds_line", np.nan)
    p = rounds_over(r, chances)
    if p is None or pd.isna(p):
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


def bout_picks(r, chances: str = "final") -> dict:
    """Each market's pick for one bout, staked: the three share one bout's cap."""
    picks = {m: picker(r, chances) for m, picker in PICKERS.items()}
    staked = stake_picks({m: None if p is None else {"prob": p.prob, "push": 0.0, "price": p.price}
                          for m, p in picks.items()})
    for m, p in picks.items():
        if p is not None:
            p.stake = staked[m]["stake"]
    return picks


def attach_edges(rows: pd.DataFrame, chances: str = "final") -> pd.DataFrame:
    """Fill ``model_over_prob`` and the ``{market}_edge_*`` columns of log-shaped rows,
    priced with the rule's chances (see ``CHANCES``)."""
    rows = rows.copy()
    for col in EDGE_COLUMNS:
        rows[col] = None if col.endswith(("_pick", "_side")) else np.nan
    rows["model_over_prob"] = [over_prob(*_rounds_of(r), getattr(r, "rounds_line", np.nan))
                               for r in rows.itertuples(index=False)]
    for idx, r in zip(rows.index, rows.itertuples(index=False)):
        for market, pick in bout_picks(r, chances).items():
            if pick is not None:
                for col, v in pick.to_log(market).items():
                    rows.at[idx, col] = v
    return rows


def edge_cell(r, market: str) -> str:
    """Display text for one market of one bout."""
    pick = getattr(r, f"{market}_edge_pick", None)
    if isinstance(pick, str) and pick:
        return Pick(pick, getattr(r, f"{market}_edge_side"), getattr(r, f"{market}_edge_line"),
                    getattr(r, f"{market}_edge_price"), False, getattr(r, f"{market}_edge_prob"),
                    getattr(r, f"{market}_edge_ev"), getattr(r, f"{market}_edge_stake", np.nan)).cell()
    if priced(r, market):
        return "no edge"
    if market == "moneyline":
        return "no line yet"
    if market == "rounds":
        line, p = fair_round_line(*_rounds_of(r, ""))
        if np.isnan(p):
            return "no line yet"
        return (f"no price yet; fair Over {line:g} {fmt_american(fair_american(p))}, "
                f"Under {fmt_american(fair_american(1 - p))}")
    probs = [getattr(r, c, np.nan) for c in SIX]
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


def graded(entries: pd.DataFrame, market: str) -> pd.DataFrame:
    """One market's logged, staked picks that have been settled: result, stake, profit, bout and EV.

    Picks logged without a stake (before edges were priced from the final
    prediction and Kelly-sized) are left out.
    """
    cols = ["result", "stake", "profit", "game", "ev"]
    col, stake_col = f"{market}_edge_pick", f"{market}_edge_stake"
    if col not in entries or stake_col not in entries:
        return pd.DataFrame(columns=cols)
    g = entries[entries[col].notna() & entries[col].astype(str).ne("") & entries[stake_col].notna()]
    rows = []
    for r in g.itertuples(index=False):
        res = outcome(market, getattr(r, f"{market}_edge_side"), getattr(r, f"{market}_edge_line"), r.status,
                      r.winner, r.method, r.end_round, getattr(r, "end_seconds", np.nan))
        if res is None:
            continue
        stake = float(getattr(r, stake_col))
        rows.append({"result": {"win": "W", "loss": "L", "push": "P"}[res], "stake": stake,
                     "profit": stake * settle(res, getattr(r, f"{market}_edge_price")),
                     "game": getattr(r, "bout_key", None), "ev": getattr(r, f"{market}_edge_ev")})
    return pd.DataFrame(rows, columns=cols)


def record(entries: pd.DataFrame, market: str, n_boot: int = 5000, seed: int = 0) -> dict:
    """Bets, W-L-P, units staked and won, ROI with its 95% range over bouts, and expected ROI."""
    return summarize(graded(entries, market), n_boot=n_boot, seed=seed)
