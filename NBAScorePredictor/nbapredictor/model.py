"""From pregame features to expected points and full score distributions.

Fitted on recent seasons each time it runs:

1. Points per 100 possessions for each offense: a weighted linear map from
   its efficiency rating, the opposing defense's, both teams' availability
   adjustments (tonight's lineup against the one behind the rating), home
   court, rest and travel, on top of the league's current level.
2. Possessions per 48 minutes for the game, from both teams' pace ratings.
   Expected points are pace times efficiency.
3. Market blend weights for margin and total against the betting line.
4. The score simulator's spread, correlation and regulation-margin weights,
   so ranges and win probabilities match how far real results land from the
   prediction.
"""

from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np
import pandas as pd

from .config import OT_MINUTES, REG_MINUTES
from .simulate import SimParams, fit_margin_weights, simulate, spread_params, summarize

EFF_FEATURES = ["eff_off", "eff_def", "p_off", "p_def", "home", "b2b", "b2b_opp", "playoff"]
PACE_FEATURES = ["pace", "playoff"]
RIDGE = 1.0
MIN_LINED_GAMES = 200


def team_view(f: pd.DataFrame) -> pd.DataFrame:
    """Two rows per game, one from each team's offense, with the efficiency features."""
    sides = []
    for side, other, sign in (("home", "away", 1.0), ("away", "home", -1.0)):
        rest, rest_opp = f[f"{side}_rest"].to_numpy(float), f[f"{other}_rest"].to_numpy(float)
        sides.append(pd.DataFrame({
            "game_id": f["game_id"].to_numpy(),
            "side": side,
            "eff_off": f[f"off_eff_{side}"].to_numpy(float),
            "eff_def": f[f"def_eff_{other}"].to_numpy(float),
            "adj_off": f[f"adj_off_{side}"].to_numpy(float),
            "adj_def": f[f"adj_def_{other}"].to_numpy(float),
            "p_off": f[f"p_off_{side}"].to_numpy(float),
            "p_def": f[f"p_def_{other}"].to_numpy(float),
            "home": np.where(f["neutral"], 0.0, 0.5 * sign),
            "b2b": (rest <= 1).astype(float),
            "b2b_opp": (rest_opp <= 1).astype(float),
            "rest_diff": np.clip(rest - rest_opp, -3, 3),
            "travel": f[f"{side}_travel"].to_numpy(float) / 1000.0,
            "travel_opp": f[f"{other}_travel"].to_numpy(float) / 1000.0,
            "tz_east": np.clip(f[f"{side}_tz_shift"].to_numpy(float), 0, None),
            "tz_west": np.clip(-f[f"{side}_tz_shift"].to_numpy(float), 0, None),
            "playoff": f["playoff"].astype(float).to_numpy(),
            "elo": sign * f["elo_spread"].to_numpy(float) / 2.0,
            "env": f["env_ppp"].to_numpy(float),
            "points": f[f"{side}_score"].to_numpy(float),
            "poss": f["poss"].to_numpy(float) if "poss" in f else np.nan,
        }))
    return pd.concat(sides, ignore_index=True)


def game_view(f: pd.DataFrame) -> pd.DataFrame:
    """One row per game with the pace features."""
    return pd.DataFrame({
        "pace": (f["off_pace_home"] + f["def_pace_home"] + f["off_pace_away"] + f["def_pace_away"]).to_numpy(float) / 2,
        "playoff": f["playoff"].astype(float).to_numpy(),
        "b2b_any": ((f["home_rest"] <= 1) | (f["away_rest"] <= 1)).astype(float).to_numpy(),
        "env": f["env_pace"].to_numpy(float),
        "y": (f["poss"] / f["minutes"] * REG_MINUTES).to_numpy(float) if "poss" in f else np.nan,
    })


def _wls(X: np.ndarray, y: np.ndarray, w: np.ndarray, ridge: float = RIDGE) -> np.ndarray:
    penalty = np.full(X.shape[1], ridge)
    penalty[0] = 0.0
    Xw = X * w[:, None]
    return np.linalg.solve(Xw.T @ X + np.diag(penalty * w.mean()), Xw.T @ y)


def _convex_weight(model: np.ndarray, market: np.ndarray, actual: np.ndarray) -> float:
    gap = model - market
    denom = float(gap @ gap)
    return float(np.clip(gap @ (actual - market) / denom, 0.0, 1.0)) if denom > 0 else 0.0


@dataclass
class ScoreModel:
    eff_coef: dict = field(default_factory=dict)
    eff_intercept: float = 0.0
    pace_coef: dict = field(default_factory=dict)
    pace_intercept: float = 0.0
    margin_weight: float = 1.0
    total_weight: float = 1.0
    ot_rate: float = 0.055
    sim: SimParams = field(default_factory=SimParams)
    fit_games: int = 0
    fit_seasons: tuple = ()

    # ---- fitting -------------------------------------------------------
    @classmethod
    def fit(cls, f: pd.DataFrame, eff_features=EFF_FEATURES, pace_features=PACE_FEATURES,
            calibrate_sim: bool = True, use_market: bool = True) -> "ScoreModel":
        f = f[f["completed"] & f["poss"].notna()].reset_index(drop=True)
        tv = team_view(f)
        ppp = 100.0 * tv["points"] / tv["poss"]
        X = np.column_stack([np.ones(len(tv)), tv[list(eff_features)].to_numpy(float)])
        beta = _wls(X, (ppp - tv["env"]).to_numpy(float), tv["poss"].to_numpy(float))
        gv = game_view(f)
        Xp = np.column_stack([np.ones(len(gv)), gv[list(pace_features)].to_numpy(float)])
        bp = _wls(Xp, (gv["y"] - gv["env"]).to_numpy(float), np.ones(len(gv)))
        regular = f[f["game_type"] != "P"]
        m = cls(eff_coef=dict(zip(eff_features, map(float, beta[1:]))), eff_intercept=float(beta[0]),
                pace_coef=dict(zip(pace_features, map(float, bp[1:]))), pace_intercept=float(bp[0]),
                ot_rate=float((regular["periods"] > 4).mean()) if len(regular) else 0.055,
                fit_games=len(f), fit_seasons=tuple(sorted(f["season"].unique().tolist())))

        pred = m.model_means(f)
        actual_margin = (f["home_score"] - f["away_score"]).to_numpy(float)
        actual_total = (f["home_score"] + f["away_score"]).to_numpy(float)
        lines = f["spread"].notna() & f["total"].notna() if "spread" in f else pd.Series(False, index=f.index)
        if use_market and lines.sum() >= MIN_LINED_GAMES:
            lf = lines.to_numpy()
            m.margin_weight = _convex_weight(pred["margin"][lf], f.loc[lines, "spread"].to_numpy(float),
                                             actual_margin[lf])
            m.total_weight = _convex_weight(pred["final_total"][lf], f.loc[lines, "total"].to_numpy(float),
                                            actual_total[lf])
        if calibrate_sim:
            final = m.means(f)
            reg = f["home_reg"].notna() & f["away_reg"].notna()
            rh, ra = f.loc[reg, "home_reg"].to_numpy(float), f.loc[reg, "away_reg"].to_numpy(float)
            r = reg.to_numpy()
            margin_sd = float(np.std((rh - ra) - final["margin"][r]))
            total_sd = float(np.std((rh + ra) - final["total"][r]))
            sd, rho = spread_params(margin_sd, total_sd)
            ref = float(np.mean(final["total"]))
            params = SimParams(sd=sd, rho=rho, ref_total=ref)
            m.sim = fit_margin_weights(params, final["home"][r], final["away"][r], rh - ra)
        return m

    # ---- prediction ----------------------------------------------------
    def model_means(self, f: pd.DataFrame) -> dict:
        """The model's own expected regulation points for each side."""
        tv = team_view(f)
        names = list(self.eff_coef)
        ppp = tv["env"].to_numpy(float) + self.eff_intercept + tv[names].to_numpy(float) @ np.array(
            [self.eff_coef[k] for k in names])
        gv = game_view(f)
        pn = list(self.pace_coef)
        pace = gv["env"].to_numpy(float) + self.pace_intercept + gv[pn].to_numpy(float) @ np.array(
            [self.pace_coef[k] for k in pn])
        n = len(f)
        home, away = pace * ppp[:n] / 100.0, pace * ppp[n:] / 100.0
        total = home + away
        return {"home": home, "away": away, "margin": home - away, "total": total,
                "final_total": total * self.ot_factor, "pace": pace, "home_ppp": ppp[:n], "away_ppp": ppp[n:]}

    @property
    def ot_factor(self) -> float:
        """Expected final points relative to regulation points, from overtimes."""
        return 1.0 + self.ot_rate * OT_MINUTES / REG_MINUTES

    def blend(self, f: pd.DataFrame, pred: dict) -> dict:
        spread = f["spread"].to_numpy(float) if "spread" in f else np.full(len(f), np.nan)
        total = f["total"].to_numpy(float) if "total" in f else np.full(len(f), np.nan)
        has = ~np.isnan(spread) & ~np.isnan(total)
        margin = np.where(has, self.margin_weight * pred["margin"] + (1 - self.margin_weight) * spread,
                          pred["margin"])
        final_total = np.where(has, self.total_weight * pred["final_total"] + (1 - self.total_weight) * total,
                               pred["final_total"])
        return {"margin": margin, "total": final_total / self.ot_factor, "has_market": has}

    def means(self, f: pd.DataFrame) -> dict:
        """Final expected regulation points: the model blended with the market."""
        pred = self.model_means(f)
        b = self.blend(f, pred)
        return {
            "home": (b["total"] + b["margin"]) / 2, "away": (b["total"] - b["margin"]) / 2,
            "margin": b["margin"], "total": b["total"],
            "model_margin": pred["margin"], "model_total": pred["final_total"],
            "model_home": pred["home"], "model_away": pred["away"], "pace": pred["pace"],
            "has_market": b["has_market"],
        }

    def predict(self, f: pd.DataFrame, n_sims: int = 10000, seed: int = 0, market: bool = True):
        """Simulated outcomes from the blended means (or the model's own with ``market=False``)."""
        means = self.means(f) if market else self.means(f.drop(columns=["spread", "total"], errors="ignore"))
        sim = simulate(means["home"], means["away"], self.sim, n_sims=n_sims, seed=seed)
        out = summarize(sim)
        out.insert(0, "game_id", f["game_id"].to_numpy())
        for key in ("margin", "model_margin", "model_total", "model_home", "model_away", "pace"):
            out[f"pred_{key}"] = means[key]
        out["pred_total"] = means["total"] * self.ot_factor
        return out, sim

    # ---- persistence ---------------------------------------------------
    def to_dict(self) -> dict:
        return {"eff_coef": self.eff_coef, "eff_intercept": self.eff_intercept,
                "pace_coef": self.pace_coef, "pace_intercept": self.pace_intercept,
                "margin_weight": self.margin_weight, "total_weight": self.total_weight,
                "ot_rate": self.ot_rate, "sim": self.sim.to_dict(),
                "fit_games": self.fit_games, "fit_seasons": list(self.fit_seasons)}

    @classmethod
    def from_dict(cls, d: dict) -> "ScoreModel":
        d = dict(d)
        d["sim"] = SimParams.from_dict(d["sim"])
        d["fit_seasons"] = tuple(d.get("fit_seasons", ()))
        return cls(**d)
