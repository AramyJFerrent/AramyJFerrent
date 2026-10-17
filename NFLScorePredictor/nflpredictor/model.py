"""From pregame features to expected points and full score distributions.

Fitted on recent seasons each time it runs:

1. A linear map from ratings to each team's points (offense rating, opposing
   defense rating, home field, divisional home field, rest and QB adjustment),
   on top of the current league scoring level.
2. Market blend weights for margin and total against the betting line.
3. A wind adjustment to totals for outdoor games, fitted on what the blend
   still misses.
4. The score simulator's dispersion and key-number weights, so ranges and win
   probabilities match how far real results land from the prediction.
"""

from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np
import pandas as pd

from .qb import DROPBACKS_PER_GAME
from .simulate import ScoringModel, calibrate, fit_margin_weights, simulate, summarize

POINT_FEATURES = ["off", "def_opp", "home", "home_div", "rest", "qb"]
WIND_THRESHOLD_MPH = 10.0
OUTDOOR_ROOFS = {"outdoors", "open"}


def team_view(f: pd.DataFrame) -> pd.DataFrame:
    """Two rows per game, one from each team's side, with the point features."""
    sides = []
    for side, other, sign in (("home", "away", 1.0), ("away", "home", -1.0)):
        home = np.where(f["neutral"], 0.0, 0.5 * sign)
        rest = sign * np.clip(f["home_rest"] - f["away_rest"], -7, 7) / 2.0
        sides.append(pd.DataFrame({
            "game_id": f["game_id"].to_numpy(),
            "side": side,
            "off": f[f"off_{side}"].to_numpy(),
            "def_opp": f[f"def_{other}"].to_numpy(),
            "home": home,
            "home_div": home * f["div_game"].to_numpy(),
            "rest": rest,
            "qb": f[f"{side}_qb_adj"].fillna(0.0).to_numpy() * DROPBACKS_PER_GAME,
            "env": f["env_points"].to_numpy(),
            "points": f[f"{side}_score"].to_numpy(),
        }))
    return pd.concat(sides, ignore_index=True)


def wind_excess(f: pd.DataFrame, wind: pd.Series | None = None) -> np.ndarray:
    wind = f["wind"] if wind is None else wind
    outdoor = f["roof"].isin(OUTDOOR_ROOFS)
    return np.where(outdoor, np.clip(wind.fillna(0.0) - WIND_THRESHOLD_MPH, 0, None), 0.0)


def _convex_weight(model: np.ndarray, market: np.ndarray, actual: np.ndarray) -> float:
    gap = model - market
    denom = float(gap @ gap)
    return float(np.clip(gap @ (actual - market) / denom, 0.0, 1.0)) if denom > 0 else 0.0


def _through_origin(x: np.ndarray, y: np.ndarray) -> float:
    denom = float(x @ x)
    return float(min(x @ y / denom, 0.0)) if denom > 0 else 0.0


@dataclass
class ScoreModel:
    coef: dict = field(default_factory=dict)
    intercept: float = 0.0
    margin_weight: float = 1.0
    total_weight: float = 1.0
    wind_blend: float = 0.0
    wind_model: float = 0.0
    scoring: ScoringModel = field(default_factory=ScoringModel)
    fit_games: int = 0
    fit_seasons: tuple = ()

    # ---- fitting -------------------------------------------------------
    @classmethod
    def fit(cls, f: pd.DataFrame, calibrate_scores: bool = True) -> "ScoreModel":
        f = f[f["completed"]].reset_index(drop=True)
        tv = team_view(f)
        X = np.column_stack([np.ones(len(tv)), tv[POINT_FEATURES].to_numpy()])
        beta, *_ = np.linalg.lstsq(X, (tv["points"] - tv["env"]).to_numpy(), rcond=None)
        m = cls(coef=dict(zip(POINT_FEATURES, map(float, beta[1:]))), intercept=float(beta[0]),
                fit_games=len(f), fit_seasons=tuple(sorted(f["season"].unique().tolist())))

        pred = m.model_means(f)
        actual_margin = (f["home_score"] - f["away_score"]).to_numpy()
        actual_total = (f["home_score"] + f["away_score"]).to_numpy()
        lines = f["spread_line"].notna() & f["total_line"].notna()
        if lines.sum() > 100:
            lf = lines.to_numpy()
            m.margin_weight = _convex_weight(pred["margin"][lf], f.loc[lines, "spread_line"].to_numpy(),
                                             actual_margin[lf])
            m.total_weight = _convex_weight(pred["total"][lf], f.loc[lines, "total_line"].to_numpy(),
                                            actual_total[lf])
        wind = wind_excess(f)
        blended = m.blend(f, pred)
        m.wind_blend = _through_origin(wind[lines], (actual_total - blended["total"])[lines])
        m.wind_model = _through_origin(wind, actual_total - pred["total"])

        if calibrate_scores:
            final = m.means(f)
            scoring = calibrate(ScoringModel(), float(np.std(actual_margin - final["margin"])),
                                float(np.std(actual_total - final["total"])),
                                mean_points=float(np.mean(final["total"]) / 2))
            m.scoring = fit_margin_weights(scoring, final["home"], final["away"], actual_margin,
                                           playoff=f["playoff"].to_numpy())
        return m

    # ---- prediction ----------------------------------------------------
    def model_means(self, f: pd.DataFrame) -> dict:
        tv = team_view(f)
        beta = np.array([self.coef[k] for k in POINT_FEATURES])
        pts = tv["env"].to_numpy() + self.intercept + tv[POINT_FEATURES].to_numpy() @ beta
        n = len(f)
        home, away = pts[:n], pts[n:]
        return {"home": home, "away": away, "margin": home - away, "total": home + away}

    def blend(self, f: pd.DataFrame, pred: dict) -> dict:
        spread, total = f["spread_line"].to_numpy(), f["total_line"].to_numpy()
        has = ~np.isnan(spread) & ~np.isnan(total)
        margin = np.where(has, self.margin_weight * pred["margin"] + (1 - self.margin_weight) * spread,
                          pred["margin"])
        tot = np.where(has, self.total_weight * pred["total"] + (1 - self.total_weight) * total,
                       pred["total"])
        return {"margin": margin, "total": tot, "has_market": has}

    def means(self, f: pd.DataFrame, wind: pd.Series | None = None) -> dict:
        """Final expected points: model, blended with the market, wind-adjusted."""
        pred = self.model_means(f)
        b = self.blend(f, pred)
        excess = wind_excess(f, wind)
        total = b["total"] + excess * np.where(b["has_market"], self.wind_blend, self.wind_model)
        margin = b["margin"]
        return {
            "home": (total + margin) / 2, "away": (total - margin) / 2,
            "margin": margin, "total": total,
            "model_margin": pred["margin"], "model_total": pred["total"],
            "has_market": b["has_market"],
        }

    def predict(self, f: pd.DataFrame, n_sims: int = 10000, wind: pd.Series | None = None,
                seed: int = 0) -> pd.DataFrame:
        means = self.means(f, wind)
        home, away = simulate(means["home"], means["away"], self.scoring, n_sims=n_sims,
                              playoff=f["playoff"].to_numpy(), seed=seed)
        out = summarize(home, away, means["home"], means["away"], self.scoring)
        out.insert(0, "game_id", f["game_id"].to_numpy())
        for key in ("home", "away", "margin", "total", "model_margin", "model_total"):
            out[f"pred_{key}"] = means[key]
        return out

    # ---- persistence ---------------------------------------------------
    def to_dict(self) -> dict:
        return {
            "coef": self.coef, "intercept": self.intercept,
            "margin_weight": self.margin_weight, "total_weight": self.total_weight,
            "wind_blend": self.wind_blend, "wind_model": self.wind_model,
            "scoring": self.scoring.to_dict(),
            "fit_games": self.fit_games, "fit_seasons": list(self.fit_seasons),
        }

    @classmethod
    def from_dict(cls, d: dict) -> "ScoreModel":
        d = dict(d)
        d["scoring"] = ScoringModel.from_dict(d["scoring"])
        d["fit_seasons"] = tuple(d.get("fit_seasons", ()))
        return cls(**d)
