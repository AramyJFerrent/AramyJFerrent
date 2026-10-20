"""From pre-fight features to one consistent outcome distribution per bout.

Fitted on recent years each time it runs:

1. **Win model.** Ridge logistic regression on the A-minus-B feature
   differences, with no intercept (see features.py), so the two fighters'
   chances always add up to one.
2. **Calibration and market blend.** Out-of-fold model log-odds (each year
   predicted by a model fitted on the other years) are recalibrated, and where
   a moneyline exists, blended with the de-vigged market on the log-odds scale:
   ``logit p = a * logit p_model + c * logit p_market``. The blend weight is
   ``a / (a + c)``; a total slope ``a + c`` above one corrects the
   favorite-longshot bias by stretching favorites further.
3. **Method given a win.** Multinomial logistic regression over KO/TKO,
   submission and decision for the winner, starting from the division's base
   rates and adjusted by the winner's finishing record, the loser's
   durability and how big a favorite the winner was.
4. **Round.** A finish hazard per round from the division-wide history of
   three- and five-round fights, shifted so the chance of a finish matches the
   method model. Strong finishers finish earlier as well as more often.

The win probability is settled first; each fighter's method chances are that
probability times the method split, so the six outcomes always sum to one.

The same method and round machinery is also run on the model's own win chance
(``p_model``, before the market blend), giving ``model_a_ko`` ... ``model_b_dec``,
``model_distance`` and ``model_r1`` ... ``model_r5``: the model-alone view that
betting edges are measured with (see edges.py).
"""

from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np
import pandas as pd
from scipy.optimize import minimize

from .features import WIN_FEATURES
from .odds import devig
from .ratings import logit, sigmoid

METHODS = ["ko", "sub", "dec"]
METHOD_FEATURES = ["w_ko_win", "w_sub_win", "w_dec_win", "l_ko_loss", "l_sub_loss", "w_kd15", "l_kdabs15",
                   "w_sub15", "w_td15", "l_td_def", "w_slpm", "l_sapm", "w_logit", "five", "title"]
# Prior strength, in fights, of the gender-wide method split behind each division's.
DIVISION_PRIOR_FIGHTS = 60.0
MAX_ROUNDS = 5
# Model-alone outcome columns (method and round machinery run on ``p_model``).
MODEL_ONLY = ([f"model_{s}_{m}" for s in "ab" for m in METHODS] + ["model_distance"]
              + [f"model_r{r}" for r in range(1, MAX_ROUNDS + 1)])


# ---- fitting helpers ------------------------------------------------------

def fit_logistic(X: np.ndarray, y: np.ndarray, ridge: float = 0.0) -> np.ndarray:
    """Logistic regression with no intercept and an L2 penalty."""
    def loss(beta):
        z = X @ beta
        p = sigmoid(z)
        val = np.sum(np.logaddexp(0.0, z) - y * z) + 0.5 * ridge * beta @ beta
        return val, X.T @ (p - y) + ridge * beta
    res = minimize(loss, np.zeros(X.shape[1]), jac=True, method="L-BFGS-B")
    return res.x


def fit_multinomial(X: np.ndarray, Y: np.ndarray, offset: np.ndarray, ridge: float) -> np.ndarray:
    """Multinomial logit with the first class as reference: logits = offset + X @ B."""
    n, d = X.shape
    k = Y.shape[1] - 1

    def loss(flat):
        B = flat.reshape(d, k)
        z = np.column_stack([np.zeros(n), offset + X @ B])
        zmax = z.max(axis=1, keepdims=True)
        lse = zmax[:, 0] + np.log(np.exp(z - zmax).sum(axis=1))
        P = np.exp(z - lse[:, None])
        val = np.sum(lse - (Y * z).sum(axis=1)) + 0.5 * ridge * flat @ flat
        grad = X.T @ (P[:, 1:] - Y[:, 1:])
        return val, grad.ravel() + ridge * flat
    res = minimize(loss, np.zeros(d * k), jac=True, method="L-BFGS-B")
    return res.x.reshape(d, k)


def decided(f: pd.DataFrame) -> pd.DataFrame:
    return f[f["winner"].isin(["a", "b"])]


def market_prob(f: pd.DataFrame) -> np.ndarray:
    if "odds_a" not in f:
        return np.full(len(f), np.nan)
    return np.asarray(devig(f["odds_a"], f["odds_b"]), dtype=float)


# ---- win model ------------------------------------------------------------

@dataclass
class WinModel:
    features: list = field(default_factory=lambda: list(WIN_FEATURES))
    scale: list = field(default_factory=list)
    coef: list = field(default_factory=list)

    @classmethod
    def fit(cls, f: pd.DataFrame, ridge: float, features: list | None = None) -> "WinModel":
        features = list(features or WIN_FEATURES)
        X = f[features].to_numpy(float)
        # Scale without centering: centering would break the A/B symmetry.
        scale = np.sqrt(np.mean(X ** 2, axis=0))
        scale[scale == 0] = 1.0
        y = (f["winner"] == "a").to_numpy(float)
        beta = fit_logistic(X / scale, y, ridge)
        return cls(features, scale.tolist(), beta.tolist())

    def logit(self, f: pd.DataFrame) -> np.ndarray:
        X = f[self.features].to_numpy(float) / np.asarray(self.scale)
        return X @ np.asarray(self.coef)

    def weights(self) -> dict:
        """Log-odds per one standard deviation of each feature."""
        return dict(zip(self.features, self.coef))


def oof_logits(f: pd.DataFrame, ridge: float, features: list | None = None) -> np.ndarray:
    """Out-of-fold win-model log-odds: each year predicted by the other years."""
    years = f["date"].dt.year.to_numpy()
    out = np.zeros(len(f))
    for y in np.unique(years):
        test = years == y
        if test.all():
            out[test] = WinModel.fit(f, ridge, features).logit(f)
            continue
        out[test] = WinModel.fit(f[~test], ridge, features).logit(f[test])
    return out


@dataclass
class Calibration:
    model_slope: float = 1.0
    blend_model: float = 0.0
    blend_market: float = 1.0
    market_fights: int = 0

    @classmethod
    def fit(cls, z_model: np.ndarray, z_market: np.ndarray, y: np.ndarray) -> "Calibration":
        slope = float(fit_logistic(z_model[:, None], y, 1e-3)[0])
        has = ~np.isnan(z_market)
        if has.sum() < 200:
            return cls(slope, 0.0, 1.0, int(has.sum()))
        a, c = fit_logistic(np.column_stack([z_model[has], z_market[has]]), y[has], 1e-3)
        return cls(slope, float(a), float(c), int(has.sum()))

    def apply(self, z_model: np.ndarray, z_market: np.ndarray) -> np.ndarray:
        blended = self.blend_model * z_model + self.blend_market * np.nan_to_num(z_market)
        return np.where(np.isnan(z_market), self.model_slope * z_model, blended)

    @property
    def market_weight(self) -> float:
        total = self.blend_model + self.blend_market
        return self.blend_market / total if total else 1.0


# ---- method model ---------------------------------------------------------

def division_method_rates(f: pd.DataFrame) -> dict:
    """KO/SUB/DEC shares of wins by division, shrunk toward the gender-wide shares."""
    d = decided(f)
    d = d[d["method"].isin(["KO", "SUB", "DEC"])]
    counts = pd.crosstab(d["division"], d["method"]).reindex(columns=["KO", "SUB", "DEC"], fill_value=0)
    gender = pd.crosstab(d["gender"], d["method"]).reindex(columns=["KO", "SUB", "DEC"], fill_value=0)
    gshare = gender.div(gender.sum(axis=1), axis=0)
    out = {}
    for g in ("M", "F"):
        share = gshare.loc[g] if g in gshare.index else pd.Series({"KO": 0.33, "SUB": 0.18, "DEC": 0.49})
        out[f"_{g}"] = share.to_dict()
    for div, row in counts.iterrows():
        g = "F" if div.startswith("Women") else "M"
        prior = pd.Series(out[f"_{g}"])
        out[div] = ((row + DIVISION_PRIOR_FIGHTS * prior) / (row.sum() + DIVISION_PRIOR_FIGHTS)).to_dict()
    return out


def winner_view(f: pd.DataFrame, side: str, win_logit: np.ndarray) -> pd.DataFrame:
    """Method features with ``side`` as the (hypothetical) winner."""
    w, l = ("a_", "b_") if side == "a" else ("b_", "a_")
    return pd.DataFrame({
        "w_ko_win": f[w + "ko_win"].to_numpy(), "w_sub_win": f[w + "sub_win"].to_numpy(),
        "w_dec_win": f[w + "dec_win"].to_numpy(),
        "l_ko_loss": f[l + "ko_loss"].to_numpy(), "l_sub_loss": f[l + "sub_loss"].to_numpy(),
        "w_kd15": f[w + "kd15"].to_numpy(), "l_kdabs15": f[l + "kdabs15"].to_numpy(),
        "w_sub15": f[w + "sub15"].to_numpy(), "w_td15": f[w + "td15"].to_numpy(),
        "l_td_def": f[l + "td_def"].to_numpy(),
        "w_slpm": f[w + "slpm"].to_numpy(), "l_sapm": f[l + "sapm"].to_numpy(),
        "w_logit": win_logit if side == "a" else -win_logit,
        "five": (f["rounds"].to_numpy() >= 5).astype(float),
        "title": f["title"].astype(float).to_numpy(),
    })


@dataclass
class MethodModel:
    rates: dict = field(default_factory=dict)
    mean: list = field(default_factory=list)
    scale: list = field(default_factory=list)
    coef: list = field(default_factory=list)

    def _offset(self, f: pd.DataFrame) -> np.ndarray:
        rows = []
        for div, g in zip(f["division"], f["gender"]):
            r = self.rates.get(div) or self.rates.get(f"_{g}") or self.rates["_M"]
            rows.append([np.log(r["KO"] / r["DEC"]), np.log(r["SUB"] / r["DEC"])])
        return np.asarray(rows)

    @classmethod
    def fit(cls, f: pd.DataFrame, win_logit: np.ndarray, ridge: float = 5.0) -> "MethodModel":
        m = cls(rates=division_method_rates(f))
        keep = f["winner"].isin(["a", "b"]).to_numpy() & f["method"].isin(["KO", "SUB", "DEC"]).to_numpy()
        f, z = f[keep], win_logit[keep]
        parts = [winner_view(f[f["winner"] == s], s, z[(f["winner"] == s).to_numpy()]) for s in ("a", "b")]
        X = pd.concat(parts, ignore_index=True)[METHOD_FEATURES].to_numpy(float)
        meth = pd.concat([f.loc[f["winner"] == s, "method"] for s in ("a", "b")], ignore_index=True)
        Y = np.column_stack([(meth == k).to_numpy(float) for k in ("DEC", "KO", "SUB")])
        offset = m._offset(pd.concat([f[f["winner"] == s] for s in ("a", "b")], ignore_index=True))
        m.mean = X.mean(axis=0).tolist()
        sd = X.std(axis=0)
        sd[sd == 0] = 1.0
        m.scale = sd.tolist()
        m.coef = fit_multinomial((X - m.mean) / sd, Y, offset, ridge).tolist()
        return m

    def split(self, f: pd.DataFrame, side: str, win_logit: np.ndarray) -> np.ndarray:
        """P(KO), P(SUB), P(DEC) given that ``side`` wins; one row per bout."""
        X = (winner_view(f, side, win_logit)[METHOD_FEATURES].to_numpy(float) - self.mean) / np.asarray(self.scale)
        z = self._offset(f) + X @ np.asarray(self.coef)
        z = np.column_stack([z, np.zeros(len(f))])        # KO, SUB, DEC
        z -= z.max(axis=1, keepdims=True)
        p = np.exp(z)
        return p / p.sum(axis=1, keepdims=True)


# ---- round model ----------------------------------------------------------

@dataclass
class RoundModel:
    hazards: dict = field(default_factory=dict)   # scheduled rounds -> per-round finish hazard

    @classmethod
    def fit(cls, f: pd.DataFrame) -> "RoundModel":
        d = decided(f)
        d = d[d["method"].isin(["KO", "SUB", "DEC"])]
        out = {}
        for rounds, default in ((3, [0.25, 0.22, 0.17]), (5, [0.22, 0.17, 0.14, 0.12, 0.12])):
            g = d[d["rounds"] == rounds]
            fin = g[g["method"] != "DEC"]["end_round"].clip(upper=rounds)
            counts = np.array([(fin == r).sum() for r in range(1, rounds + 1)], dtype=float)
            at_risk = len(g) - np.concatenate([[0.0], np.cumsum(counts)[:-1]])
            # Shrink each hazard toward the default with 20 fights of weight.
            h = (counts + 20 * np.array(default)) / (at_risk + 20)
            out[str(rounds)] = h.tolist()
        return cls(out)

    def split(self, finish: np.ndarray, rounds: np.ndarray) -> np.ndarray:
        """P(finish in round r) for r = 1..5, matching each bout's total finish chance."""
        finish = np.clip(np.asarray(finish, float), 1e-4, 1 - 1e-4)
        rounds = np.where(np.asarray(rounds) >= 5, 5, 3)
        out = np.zeros((len(finish), MAX_ROUNDS))
        for r_count in (3, 5):
            sel = rounds == r_count
            if not sel.any():
                continue
            base = logit(np.asarray(self.hazards[str(r_count)]))
            lo, hi = np.full(sel.sum(), -10.0), np.full(sel.sum(), 10.0)
            target = finish[sel]
            for _ in range(60):
                mid = (lo + hi) / 2
                h = sigmoid(base[None, :] + mid[:, None])
                total = 1 - np.prod(1 - h, axis=1)
                lo = np.where(total < target, mid, lo)
                hi = np.where(total < target, hi, mid)
            h = sigmoid(base[None, :] + ((lo + hi) / 2)[:, None])
            survive = np.cumprod(np.column_stack([np.ones(sel.sum()), 1 - h[:, :-1]]), axis=1)
            out[sel, :r_count] = survive * h
        return out


# ---- everything together --------------------------------------------------

@dataclass
class FightModel:
    win: WinModel = field(default_factory=WinModel)
    calibration: Calibration = field(default_factory=Calibration)
    method: MethodModel = field(default_factory=MethodModel)
    rounds: RoundModel = field(default_factory=RoundModel)
    glicko_slope: float = 1.0
    ridge: float = 1.0
    fit_fights: int = 0
    fit_years: tuple = ()

    @classmethod
    def fit(cls, f: pd.DataFrame, ridge: float = 1.0, features: list | None = None) -> "FightModel":
        d = decided(f).reset_index(drop=True)
        y = (d["winner"] == "a").to_numpy(float)
        z_oof = oof_logits(d, ridge, features)
        z_market = logit(market_prob(d))
        z_market[np.isnan(market_prob(d))] = np.nan
        calib = Calibration.fit(z_oof, z_market, y)
        win = WinModel.fit(d, ridge, features)
        z_final = calib.apply(z_oof, z_market)
        glicko = float(fit_logistic(d[["glicko_logit"]].to_numpy(float), y, 1e-3)[0])
        return cls(win=win, calibration=calib, method=MethodModel.fit(d, z_final), rounds=RoundModel.fit(d),
                   glicko_slope=glicko, ridge=ridge, fit_fights=len(d), fit_years=tuple(sorted(d["date"].dt.year.unique().tolist())))

    def predict(self, f: pd.DataFrame) -> pd.DataFrame:
        f = f.reset_index(drop=True)
        z_raw = self.win.logit(f)
        p_mkt = market_prob(f)
        z_mkt = np.where(np.isnan(p_mkt), np.nan, logit(p_mkt))
        z = self.calibration.apply(z_raw, z_mkt)
        z_own = self.calibration.model_slope * z_raw
        p_a = sigmoid(z)
        out = pd.DataFrame({
            "p_a": p_a,
            "p_model": sigmoid(z_own),
            "p_market": p_mkt,
            # The rating alone, rescaled to a win chance: the baseline the full model has to beat.
            "p_glicko": sigmoid(self.glicko_slope * f["glicko_logit"].to_numpy(float)),
        })
        out = out.join(self.outcomes(f, z))
        # The same split on the model alone: the method model takes the win
        # log-odds as an input, so it is rerun rather than rescaled.
        own = self.outcomes(f, z_own)
        out = out.join(own.rename(columns=lambda c: "model_distance" if c == "p_distance" else f"model_{c}"))
        six = out[[f"{s}_{m}" for s in "ab" for m in METHODS]].to_numpy()
        best = six.argmax(axis=1)
        out["best_side"] = np.where(best < 3, "a", "b")
        out["best_method"] = [METHODS[i % 3] for i in best]
        out["best_prob"] = six.max(axis=1)
        return out

    def outcomes(self, f: pd.DataFrame, z: np.ndarray) -> pd.DataFrame:
        """Six-way method chances, the distance and the finish round for win log-odds ``z``."""
        p_a = sigmoid(z)
        split_a = self.method.split(f, "a", z)
        split_b = self.method.split(f, "b", z)
        out = pd.DataFrame(index=f.index)
        for i, m in enumerate(METHODS):
            out[f"a_{m}"] = p_a * split_a[:, i]
        for i, m in enumerate(METHODS):
            out[f"b_{m}"] = (1 - p_a) * split_b[:, i]
        out["p_distance"] = out["a_dec"] + out["b_dec"]
        by_round = self.rounds.split(1 - out["p_distance"].to_numpy(), f["rounds"].to_numpy())
        for r in range(MAX_ROUNDS):
            out[f"r{r + 1}"] = by_round[:, r]
        return out

    # ---- persistence ---------------------------------------------------------
    def to_dict(self) -> dict:
        return {
            "win": {"features": self.win.features, "scale": self.win.scale, "coef": self.win.coef},
            "calibration": self.calibration.__dict__,
            "method": {"rates": self.method.rates, "features": METHOD_FEATURES, "mean": self.method.mean,
                       "scale": self.method.scale, "coef": self.method.coef},
            "round_hazards": self.rounds.hazards, "glicko_slope": self.glicko_slope,
            "ridge": self.ridge, "fit_fights": self.fit_fights, "fit_years": list(self.fit_years),
        }

