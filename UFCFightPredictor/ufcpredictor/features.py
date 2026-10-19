"""Pre-fight features for every bout, built strictly from earlier fights.

``FeatureBuilder.build`` walks through UFC history in fight order. Before each
bout it snapshots both fighters (ratings, style profiles, age, layoff, tale of
the tape), then feeds the result back into the ratings and profiles. Every
feature is therefore computed from fights before that bout only, which is
what a walk-forward backtest needs. ``upcoming`` snapshots fighters the same
way for bouts that have not happened yet.

Win-model features are differences between the two fighters (A minus B), so
swapping the corners flips every sign. With no intercept, the win model then
gives P(A beats B) = 1 - P(B beats A) exactly, as if trained on both corner
orders, and cannot learn which corner a fighter was in.
"""

from __future__ import annotations

import logging
import math

import numpy as np
import pandas as pd

from .config import DIVISIONS, Hyperparams
from .profiles import PROFILE_FIELDS, Profiles
from .ratings import Elo, Glicko2, sigmoid, winner_score

log = logging.getLogger(__name__)

WIN_FEATURES = [
    "glicko_logit", "d_rd", "d_age", "d_age_decline", "d_reach", "d_height", "d_log_fights", "d_debut",
    "d_layoff", "d_slpm", "d_sapm", "d_strike_matchup", "d_sig_acc", "d_sig_def", "d_td_matchup",
    "d_td_def", "d_sub15", "d_ctrl", "d_kd15", "d_kdabs15", "d_ko_loss", "d_last_ko_loss", "d_streak",
    "d_southpaw", "d_move",
]
SIDE_FIELDS = PROFILE_FIELDS + ["rating", "rd", "fights", "age", "reach", "height", "layoff_days",
                                "last_ko_loss", "streak"]
CONTEXT = ["bout_id", "date", "event", "order", "fighter_a", "fighter_b", "a_id", "b_id", "division",
           "gender", "title", "rounds"]
OUTCOME = ["winner", "method", "decision", "end_round"]
AGE_DECLINE_FROM = 33.0
DEFAULT_AGE = 29.5


def _day(ts) -> float:
    return pd.Timestamp(ts).value / 86_400e9


class FeatureBuilder:
    def __init__(self, bouts: pd.DataFrame, stats: pd.DataFrame, fighters: pd.DataFrame, hp: Hyperparams):
        self.bouts = bouts
        self.hp = hp
        self.stats = {(b, s): row for b, s, row in zip(stats["bout_id"], stats["side"],
                                                       stats.to_dict("records"))}
        f = fighters.set_index("fighter_id")
        self.dob = f["dob"].to_dict()
        self.reach = f["reach"].to_dict()
        self.height = f["height"].to_dict()
        self.stance = f["stance"].to_dict()
        # Division means for missing reach and height.
        app = pd.concat([bouts[["a_id", "division"]].rename(columns={"a_id": "id"}),
                         bouts[["b_id", "division"]].rename(columns={"b_id": "id"})])
        app["reach"], app["height"] = app["id"].map(self.reach), app["id"].map(self.height)
        self.div_reach = app.groupby("division")["reach"].mean().to_dict()
        self.div_height = app.groupby("division")["height"].mean().to_dict()
        self.mean_reach = float(app["reach"].mean())
        self.mean_height = float(app["height"].mean())
        self.reset()

    def reset(self) -> None:
        self.glicko = Glicko2(self.hp)
        self.elo = Elo()
        self.profiles = Profiles(self.hp)
        self.last_div: dict[str, str] = {}
        self.last_ko_loss: dict[str, float] = {}
        self.streak: dict[str, int] = {}
        self.last_date: dict[str, pd.Timestamp] = {}
        self.names: dict[str, str] = {}

    # ---- snapshots ----------------------------------------------------------
    def _prior_division(self, fid: str, division: str) -> str | None:
        if division in DIVISIONS:
            return division
        return self.last_div.get(fid)

    def side(self, fid: str, date: pd.Timestamp, division: str) -> dict:
        day = _day(date)
        rating, rd, fights = self.glicko.state(fid, day)
        prof = self.profiles.profile(fid, day, self._prior_division(fid, division))
        dob = self.dob.get(fid)
        age = (date - dob).days / 365.25 if dob is not None and not pd.isna(dob) else np.nan
        pdiv = self._prior_division(fid, division)
        reach = self.reach.get(fid, np.nan)
        height = self.height.get(fid, np.nan)
        last = self.last_date.get(fid)
        return {
            **prof, "rating": rating, "rd": rd, "fights": fights,
            "age": age if not np.isnan(age) else np.nan,
            "reach": reach if not pd.isna(reach) else self.div_reach.get(pdiv, self.mean_reach),
            "height": height if not pd.isna(height) else self.div_height.get(pdiv, self.mean_height),
            "layoff_days": (date - last).days if last is not None else np.nan,
            "last_ko_loss": self.last_ko_loss.get(fid, 0.0),
            "streak": self.streak.get(fid, 0),
            "stance": self.stance.get(fid),
            "last_div": self.last_div.get(fid),
        }

    def pair_features(self, a_id: str, b_id: str, date: pd.Timestamp, division: str,
                      sa: dict | None = None, sb: dict | None = None) -> dict:
        sa = sa or self.side(a_id, date, division)
        sb = sb or self.side(b_id, date, division)
        day = _day(date)
        rates = self.profiles.division_rates(self._prior_division(a_id, division))
        out = {"glicko_logit": self.glicko.win_logit(a_id, b_id, day),
               "elo_prob": self.elo.prob(a_id, b_id)}

        def age(s):
            return s["age"] if not np.isnan(s["age"]) else DEFAULT_AGE

        def layoff(s):
            return math.log1p(s["layoff_days"] / 365.0) if not np.isnan(s["layoff_days"]) else 0.0

        def move(s):
            prev = DIVISIONS.get(s["last_div"])
            now = DIVISIONS.get(division)
            return (now - prev) / 10.0 if prev and now else 0.0

        def southpaw(s, o):
            return float(s["stance"] == "Southpaw" and o["stance"] == "Orthodox")

        spm, tdpm = rates["spm"], rates["tdpm"]
        out.update({
            "d_rd": (sa["rd"] - sb["rd"]) / 100.0,
            "d_age": age(sa) - age(sb),
            "d_age_decline": max(age(sa) - AGE_DECLINE_FROM, 0) - max(age(sb) - AGE_DECLINE_FROM, 0),
            "d_reach": sa["reach"] - sb["reach"],
            "d_height": sa["height"] - sb["height"],
            "d_log_fights": math.log1p(sa["fights"]) - math.log1p(sb["fights"]),
            "d_debut": float(sa["fights"] == 0) - float(sb["fights"] == 0),
            "d_layoff": layoff(sa) - layoff(sb),
            "d_slpm": sa["slpm"] - sb["slpm"],
            "d_sapm": sa["sapm"] - sb["sapm"],
            "d_strike_matchup": (sa["slpm"] * sb["sapm"] - sb["slpm"] * sa["sapm"]) / spm,
            "d_sig_acc": sa["sig_acc"] - sb["sig_acc"],
            "d_sig_def": sa["sig_def"] - sb["sig_def"],
            "d_td_matchup": (sa["td15"] * sb["tdabs15"] - sb["td15"] * sa["tdabs15"]) / (15 * tdpm),
            "d_td_def": sa["td_def"] - sb["td_def"],
            "d_sub15": sa["sub15"] - sb["sub15"],
            "d_ctrl": sa["ctrl"] - sb["ctrl"],
            "d_kd15": sa["kd15"] - sb["kd15"],
            "d_kdabs15": sa["kdabs15"] - sb["kdabs15"],
            "d_ko_loss": sa["ko_loss"] - sb["ko_loss"],
            "d_last_ko_loss": sa["last_ko_loss"] - sb["last_ko_loss"],
            "d_streak": float(np.clip(sa["streak"], -3, 3) - np.clip(sb["streak"], -3, 3)),
            "d_southpaw": southpaw(sa, sb) - southpaw(sb, sa),
            "d_move": move(sa) - move(sb),
        })
        for prefix, s in (("a_", sa), ("b_", sb)):
            for k in SIDE_FIELDS:
                out[prefix + k] = s[k]
        out["glicko_prob"] = float(sigmoid(out["glicko_logit"]))
        return out

    # ---- history ------------------------------------------------------------
    def _update(self, b) -> None:
        a_id, b_id, date = b.a_id, b.b_id, b.date
        day = _day(date)
        score = winner_score(b.winner, b.method, b.decision, self.hp)
        pre = (self.profiles.profile(a_id, day, self._prior_division(a_id, b.division)),
               self.profiles.profile(b_id, day, self._prior_division(b_id, b.division)))
        if score is not None:
            self.glicko.update(a_id, b_id, score, day)
            self.elo.update(a_id, b_id, 1.0 if b.winner == "a" else 0.0 if b.winner == "b" else 0.5)
        res_a = ("win" if b.winner == "a" else "loss" if b.winner == "b" else "other", b.method)
        res_b = ("win" if b.winner == "b" else "loss" if b.winner == "a" else "other", b.method)
        minutes = b.fight_seconds / 60.0
        self.profiles.update((a_id, b_id), day, b.division, (res_a, res_b),
                             (self.stats.get((b.bout_id, "a")), self.stats.get((b.bout_id, "b"))),
                             minutes, pre)
        for fid, (res, method), name in ((a_id, res_a, b.fighter_a), (b_id, res_b, b.fighter_b)):
            self.names[fid] = name
            self.last_date[fid] = date
            if b.division in DIVISIONS:
                self.last_div[fid] = b.division
            if score is None:
                continue
            self.last_ko_loss[fid] = float(res == "loss" and method == "KO")
            st = self.streak.get(fid, 0)
            if res == "win":
                self.streak[fid] = st + 1 if st > 0 else 1
            elif res == "loss":
                self.streak[fid] = st - 1 if st < 0 else -1

    def build(self, until: pd.Timestamp | None = None) -> pd.DataFrame:
        """Pre-fight features for every bout (before ``until`` if given)."""
        self.reset()
        rows = []
        bouts = self.bouts if until is None else self.bouts[self.bouts["date"] < until]
        for b in bouts.itertuples(index=False):
            feats = self.pair_features(b.a_id, b.b_id, b.date, b.division)
            rows.append(feats)
            self._update(b)
        feats = pd.DataFrame(rows, index=bouts.index)
        out = pd.concat([bouts[CONTEXT + OUTCOME], feats], axis=1)
        log.info("Built features for %d bouts", len(out))
        return out.reset_index(drop=True)

    def upcoming(self, card: pd.DataFrame) -> pd.DataFrame:
        """Features for bouts not yet fought, from everything already in the history.

        ``card`` needs a_id, b_id, date and division (and the context columns
        it has). Call after ``build``.
        """
        rows = [self.pair_features(r.a_id, r.b_id, pd.Timestamp(r.date), r.division)
                for r in card.itertuples(index=False)]
        feats = pd.DataFrame(rows, index=card.index)
        return pd.concat([card, feats], axis=1)
