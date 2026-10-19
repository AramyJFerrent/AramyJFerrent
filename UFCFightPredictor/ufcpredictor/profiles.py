"""Style profiles: striking, grappling and finishing rates from earlier fights.

A fighter with three UFC fights has very noisy rates, so every rate is shrunk
toward the division average: the division's rate counts as ``prior_minutes``
of cage time (or ``prior_attempts`` attempts, or ``prior_fights`` fights) of
evidence. Older fights fade with a half-life of ``profile_half_life_years``.

The main offense and defense rates are also opponent-adjusted: each fight
records what the opponent usually allows (or lands), and the fighter's rate is
scaled by how far they beat that expectation. Landing 5 strikes a minute on
someone who usually absorbs 3 counts for more than on someone who absorbs 6.
"""

from __future__ import annotations

import numpy as np

from .config import DIVISIONS, Hyperparams

KEYS = [
    "fights", "minutes", "sig_l", "sig_a", "sig_abs", "sig_opp_a", "td_l", "td_a", "td_abs", "td_opp_a",
    "sub_att", "ctrl", "ctrl_opp", "kd", "kd_abs", "sig_l_exp", "sig_abs_exp", "td_l_exp", "td_abs_exp",
    "win_ko", "win_sub", "win_dec", "loss_ko", "loss_sub", "loss_dec",
]
IDX = {k: i for i, k in enumerate(KEYS)}
# Division-level sums, undecayed: per fighter appearance.
DIV_KEYS = ["fights", "minutes", "sig_l", "sig_a", "td_l", "td_a", "sub_att", "kd",
            "win_ko", "win_sub", "win_dec"]
DIV_IDX = {k: i for i, k in enumerate(DIV_KEYS)}

PROFILE_FIELDS = [
    "slpm", "sapm", "sig_acc", "sig_def", "td15", "tdabs15", "td_acc", "td_def", "sub15", "ctrl",
    "kd15", "kdabs15", "ko_win", "sub_win", "dec_win", "ko_loss", "sub_loss",
]


class Profiles:
    def __init__(self, hp: Hyperparams):
        self.hp = hp
        self.half_life_days = hp.profile_half_life_years * 365.25
        self.sums: dict[str, np.ndarray] = {}
        self.day: dict[str, float] = {}
        self.div: dict[str, np.ndarray] = {}
        self.total = np.zeros(len(DIV_KEYS))

    # ---- division priors --------------------------------------------------
    def division_rates(self, division: str | None) -> dict:
        s = self.div.get(division) if division in DIVISIONS else None
        if s is None or s[DIV_IDX["minutes"]] < 200:
            s = self.total
        m = max(s[DIV_IDX["minutes"]], 1.0)
        f = max(s[DIV_IDX["fights"]], 1.0)
        return {
            "spm": s[DIV_IDX["sig_l"]] / m if s[DIV_IDX["sig_l"]] > 0 else 3.5,
            "acc": s[DIV_IDX["sig_l"]] / s[DIV_IDX["sig_a"]] if s[DIV_IDX["sig_a"]] > 0 else 0.45,
            "tdpm": s[DIV_IDX["td_l"]] / m if s[DIV_IDX["td_l"]] > 0 else 0.1,
            "tdacc": s[DIV_IDX["td_l"]] / s[DIV_IDX["td_a"]] if s[DIV_IDX["td_a"]] > 0 else 0.38,
            "subpm": s[DIV_IDX["sub_att"]] / m if s[DIV_IDX["sub_att"]] > 0 else 0.04,
            "kdpm": s[DIV_IDX["kd"]] / m if s[DIV_IDX["kd"]] > 0 else 0.03,
            # Per appearance: half of all fighters win, split by method.
            "ko": s[DIV_IDX["win_ko"]] / f if s[DIV_IDX["win_ko"]] > 0 else 0.16,
            "sub": s[DIV_IDX["win_sub"]] / f if s[DIV_IDX["win_sub"]] > 0 else 0.09,
            "dec": s[DIV_IDX["win_dec"]] / f if s[DIV_IDX["win_dec"]] > 0 else 0.25,
        }

    # ---- fighter profiles -------------------------------------------------
    def _sums(self, fid: str, day: float) -> np.ndarray:
        s = self.sums.get(fid)
        if s is None:
            return np.zeros(len(KEYS))
        return s * 0.5 ** ((day - self.day[fid]) / self.half_life_days)

    def profile(self, fid: str, day: float, division: str | None) -> dict:
        s = self._sums(fid, day)
        r = self.division_rates(division)
        km, ka, kf = self.hp.prior_minutes, self.hp.prior_attempts, self.hp.prior_fights
        kt = ka / 4.0
        g = lambda k: s[IDX[k]]  # noqa: E731
        m = g("minutes")
        spm_prior, td_prior = km * r["spm"], km * r["tdpm"]
        return {
            "slpm": r["spm"] * (g("sig_l") + spm_prior) / (g("sig_l_exp") + spm_prior),
            "sapm": r["spm"] * (g("sig_abs") + spm_prior) / (g("sig_abs_exp") + spm_prior),
            "sig_acc": (g("sig_l") + ka * r["acc"]) / (g("sig_a") + ka),
            "sig_def": 1 - (g("sig_abs") + ka * r["acc"]) / (g("sig_opp_a") + ka),
            "td15": 15 * r["tdpm"] * (g("td_l") + td_prior) / (g("td_l_exp") + td_prior),
            "tdabs15": 15 * r["tdpm"] * (g("td_abs") + td_prior) / (g("td_abs_exp") + td_prior),
            "td_acc": (g("td_l") + kt * r["tdacc"]) / (g("td_a") + kt),
            "td_def": 1 - (g("td_abs") + kt * r["tdacc"]) / (g("td_opp_a") + kt),
            "sub15": 15 * (g("sub_att") + km * r["subpm"]) / (m + km),
            "ctrl": (g("ctrl") - g("ctrl_opp")) / 60.0 / (m + km),
            "kd15": 15 * (g("kd") + km * r["kdpm"]) / (m + km),
            "kdabs15": 15 * (g("kd_abs") + km * r["kdpm"]) / (m + km),
            "ko_win": (g("win_ko") + kf * r["ko"]) / (g("fights") + kf),
            "sub_win": (g("win_sub") + kf * r["sub"]) / (g("fights") + kf),
            "dec_win": (g("win_dec") + kf * r["dec"]) / (g("fights") + kf),
            "ko_loss": (g("loss_ko") + kf * r["ko"]) / (g("fights") + kf),
            "sub_loss": (g("loss_sub") + kf * r["sub"]) / (g("fights") + kf),
        }

    # ---- updates ------------------------------------------------------------
    def _add(self, fid: str, day: float, vec: np.ndarray) -> None:
        self.sums[fid] = self._sums(fid, day) + vec
        self.day[fid] = day

    def update(self, ids: tuple[str, str], day: float, division: str, result: tuple[str, str],
               stats: tuple[dict | None, dict | None], minutes: float, pre: tuple[dict, dict]) -> None:
        """Add one bout. ``result`` is each side's ('win'|'loss'|'other', method)."""
        has_stats = stats[0] is not None and stats[1] is not None and minutes == minutes and minutes > 0
        div_vec = np.zeros(len(DIV_KEYS))
        for i in (0, 1):
            j = 1 - i
            v = np.zeros(len(KEYS))
            v[IDX["fights"]] = 1.0
            outcome, method = result[i]
            if outcome == "win" and method in ("KO", "SUB", "DEC"):
                v[IDX[f"win_{method.lower()}"]] = 1.0
                div_vec[DIV_IDX[f"win_{method.lower()}"]] += 1.0
            elif outcome == "loss" and method in ("KO", "SUB", "DEC"):
                v[IDX[f"loss_{method.lower()}"]] = 1.0
            div_vec[DIV_IDX["fights"]] += 1.0
            if has_stats:
                me, opp = stats[i], stats[j]
                v[IDX["minutes"]] = minutes
                v[IDX["sig_l"]], v[IDX["sig_a"]] = me["sig_l"], me["sig_a"]
                v[IDX["sig_abs"]], v[IDX["sig_opp_a"]] = opp["sig_l"], opp["sig_a"]
                v[IDX["td_l"]], v[IDX["td_a"]] = me["td_l"], me["td_a"]
                v[IDX["td_abs"]], v[IDX["td_opp_a"]] = opp["td_l"], opp["td_a"]
                v[IDX["sub_att"]], v[IDX["kd"]], v[IDX["kd_abs"]] = me["sub_att"], me["kd"], opp["kd"]
                v[IDX["ctrl"]], v[IDX["ctrl_opp"]] = me["ctrl"], opp["ctrl"]
                # What this opponent usually allows or lands, per minute, before the fight.
                v[IDX["sig_l_exp"]] = pre[j]["sapm"] * minutes
                v[IDX["sig_abs_exp"]] = pre[j]["slpm"] * minutes
                v[IDX["td_l_exp"]] = pre[j]["tdabs15"] / 15 * minutes
                v[IDX["td_abs_exp"]] = pre[j]["td15"] / 15 * minutes
                div_vec[DIV_IDX["minutes"]] += minutes
                for k in ("sig_l", "sig_a", "td_l", "td_a", "sub_att", "kd"):
                    div_vec[DIV_IDX[k]] += me[k]
            self._add(ids[i], day, np.nan_to_num(v))
        div_vec = np.nan_to_num(div_vec)
        if division in DIVISIONS:
            self.div[division] = self.div.get(division, np.zeros(len(DIV_KEYS))) + div_vec
        self.total = self.total + div_vec
