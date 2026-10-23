"""From pregame features to expected points and full score distributions.

Fitted on recent seasons each time it runs:

1. A linear map from ratings to each team's points (offense rating, opposing
   defense rating, home field, divisional home field, rest and QB adjustment),
   on top of the current league scoring level.
2. Market blend weights for margin and total against the betting line, fitted
   on out-of-fold predictions (each training season predicted by a points map
   fitted on the others), so the model is not trusted for its fit to games it
   was fitted on.
3. A wind adjustment to totals for outdoor games, fitted on what the blend
   still misses.
4. The score simulator's dispersion and key-number weights, so ranges and win
   probabilities match how far real results land from the prediction.
"""

from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np
import pandas as pd
from bettingcore import anchored, market_chance, no_push, with_push

from .qb import DROPBACKS_PER_GAME
from .simulate import ScoringModel, calibrate, fit_margin_weights, line_probs, simulate, summarize

POINT_FEATURES = ["off", "def_opp", "st", "st_opp", "home", "home_div", "rest", "qb",
                  "inj_ol", "inj_skill", "inj_front_opp", "inj_back_opp"]
# The final prediction's chances against the posted lines, anchored to the market's
# (see ``edge_chances``), which the betting edges use.
FINAL_LINE_PROBS = ["home_cover_prob", "spread_push_prob", "over_prob", "total_push_prob",
                    "home_ml_prob", "away_ml_prob"]
WIND_THRESHOLD_MPH = 10.0
OUTDOOR_ROOFS = {"outdoors", "open"}


def team_view(f: pd.DataFrame) -> pd.DataFrame:
    """Two rows per game, one from each team's side, with the point features."""
    def col(name):
        return f[name].fillna(0.0).to_numpy() if name in f else np.zeros(len(f))

    sides = []
    for side, other, sign in (("home", "away", 1.0), ("away", "home", -1.0)):
        home = np.where(f["neutral"], 0.0, 0.5 * sign)
        rest = sign * np.clip(f["home_rest"] - f["away_rest"], -7, 7) / 2.0
        sides.append(pd.DataFrame({
            "game_id": f["game_id"].to_numpy(),
            "side": side,
            "off": f[f"off_{side}"].to_numpy(),
            "def_opp": f[f"def_{other}"].to_numpy(),
            "st": f[f"off_st_{side}"].to_numpy(),
            "st_opp": f[f"def_st_{other}"].to_numpy(),
            "home": home,
            "home_div": home * f["div_game"].to_numpy(),
            "rest": rest,
            "qb": f[f"{side}_qb_adj"].fillna(0.0).to_numpy() * DROPBACKS_PER_GAME,
            # Snap shares lost to non-QB injuries: this team's offense, the opponent's defense.
            "inj_ol": col(f"{side}_inj_ol"), "inj_skill": col(f"{side}_inj_skill"),
            "inj_front_opp": col(f"{other}_inj_front"), "inj_back_opp": col(f"{other}_inj_back"),
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
        m = cls._points_map(f)
        pred = m.model_means(f)
        oof = cls._out_of_fold_means(f, pred)
        actual_margin = (f["home_score"] - f["away_score"]).to_numpy()
        actual_total = (f["home_score"] + f["away_score"]).to_numpy()
        lines = f["spread_line"].notna() & f["total_line"].notna()
        if lines.sum() > 100:
            lf = lines.to_numpy()
            m.margin_weight = _convex_weight(oof["margin"][lf], f.loc[lines, "spread_line"].to_numpy(),
                                             actual_margin[lf])
            m.total_weight = _convex_weight(oof["total"][lf], f.loc[lines, "total_line"].to_numpy(),
                                            actual_total[lf])
        wind = wind_excess(f)
        blended = m.blend(f, oof)
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

    @classmethod
    def _points_map(cls, f: pd.DataFrame) -> "ScoreModel":
        """The linear map from ratings to points, fitted on ``f`` (completed games)."""
        tv = team_view(f)
        X = np.column_stack([np.ones(len(tv)), tv[POINT_FEATURES].to_numpy()])
        beta, *_ = np.linalg.lstsq(X, (tv["points"] - tv["env"]).to_numpy(), rcond=None)
        return cls(coef=dict(zip(POINT_FEATURES, map(float, beta[1:]))), intercept=float(beta[0]),
                   fit_games=len(f), fit_seasons=tuple(sorted(f["season"].unique().tolist())))

    @classmethod
    def _out_of_fold_means(cls, f: pd.DataFrame, in_sample: dict) -> dict:
        """The model's expected points for each game from a points map fitted on the other seasons.

        With fewer than three seasons there is nothing to hold out, and the
        in-sample means are returned.
        """
        seasons = f["season"].to_numpy()
        if len(np.unique(seasons)) < 3:
            return in_sample
        out = {k: np.array(v, dtype=float, copy=True) for k, v in in_sample.items()}
        for season in np.unique(seasons):
            held = seasons == season
            pred = cls._points_map(f[~held]).model_means(f[held])
            for k in out:
                out[k][held] = pred[k]
        return out

    # ---- prediction ----------------------------------------------------
    def model_means(self, f: pd.DataFrame) -> dict:
        tv = team_view(f)
        names = list(self.coef)
        beta = np.array([self.coef[k] for k in names])
        pts = tv["env"].to_numpy() + self.intercept + tv[names].to_numpy() @ beta
        n = len(f)
        home, away = pts[:n], pts[n:]
        return {"home": home, "away": away, "margin": home - away, "total": home + away}

    def blend(self, f: pd.DataFrame, pred: dict) -> dict:
        """The margin blended with the spread and the total with the total line, each where posted."""
        spread, total = f["spread_line"].to_numpy(float), f["total_line"].to_numpy(float)
        has_spread, has_total = ~np.isnan(spread), ~np.isnan(total)
        margin = np.where(has_spread, self.margin_weight * pred["margin"] + (1 - self.margin_weight) * spread,
                          pred["margin"])
        tot = np.where(has_total, self.total_weight * pred["total"] + (1 - self.total_weight) * total,
                       pred["total"])
        return {"margin": margin, "total": tot, "has_market": has_spread & has_total,
                "has_total": has_total}

    def means(self, f: pd.DataFrame, wind: pd.Series | None = None) -> dict:
        """Final expected points: model, blended with the market, wind-adjusted."""
        pred = self.model_means(f)
        b = self.blend(f, pred)
        excess = wind_excess(f, wind)
        total = b["total"] + excess * np.where(b["has_total"], self.wind_blend, self.wind_model)
        margin = b["margin"]
        return {
            "home": (total + margin) / 2, "away": (total - margin) / 2,
            "margin": margin, "total": total,
            "model_margin": pred["margin"], "model_total": pred["total"],
            "has_market": b["has_market"],
        }

    def model_only_means(self, f: pd.DataFrame, wind: pd.Series | None = None) -> dict:
        """The model's own expected points with no market blend: what it predicts without a line."""
        pred = self.model_means(f)
        total = pred["total"] + wind_excess(f, wind) * self.wind_model
        return {"home": (total + pred["margin"]) / 2, "away": (total - pred["margin"]) / 2,
                "margin": pred["margin"], "total": total}

    def model_only(self, f: pd.DataFrame, n_sims: int = 10000, wind: pd.Series | None = None, seed: int = 0,
                   spread_line=None, total_line=None) -> pd.DataFrame:
        """Win, cover and over chances from simulating the model's own expected points.

        Same simulator and dispersion as the final prediction, centered on the
        model before blending with the market, against the given lines (default:
        the lines in ``f``). Shown next to the final chances; edges use the final ones.
        """
        means = self.model_only_means(f, wind)
        home, away = simulate(means["home"], means["away"], self.scoring, n_sims=n_sims,
                              playoff=f["playoff"].to_numpy(), seed=seed)
        spread = f["spread_line"] if spread_line is None else spread_line
        total = f["total_line"] if total_line is None else total_line
        return line_probs(home, away, self.scoring, spread, total)

    def predict(self, f: pd.DataFrame, n_sims: int = 10000, wind: pd.Series | None = None,
                seed: int = 0) -> pd.DataFrame:
        """Final prediction per game. Its win, cover and over chances against the posted
        lines (``home_cover_prob`` ...) price the betting edges; the ``model_*`` chances
        are the model's own, before the blend, for comparison."""
        means = self.means(f, wind)
        home, away = simulate(means["home"], means["away"], self.scoring, n_sims=n_sims,
                              playoff=f["playoff"].to_numpy(), seed=seed)
        out = summarize(home, away, means["home"], means["away"], self.scoring)
        out.insert(0, "game_id", f["game_id"].to_numpy())
        for key in ("home", "away", "margin", "total", "model_margin", "model_total"):
            out[f"pred_{key}"] = means[key]
        # Same seed as the final simulation: on the line the two match draw for draw.
        edges = self.edge_chances(f, means, home, away, n_sims=n_sims, seed=seed)
        for col in FINAL_LINE_PROBS:
            out[col] = edges[col].to_numpy()
        own = self.model_only(f, n_sims=n_sims, wind=wind, seed=seed + 1)
        for col in own:
            out[f"model_{col}"] = own[col].to_numpy()
        return out

    def edge_chances(self, f: pd.DataFrame, means: dict, home: np.ndarray, away: np.ndarray,
                     n_sims: int = 10000, seed: int = 0) -> pd.DataFrame:
        """Each side's chance against the posted lines, anchored to the market (``bettingcore.anchor``).

        The final prediction's simulated chances (``home``, ``away``) are set
        against a second simulation centered on the lines themselves; each side
        gets the market's de-vigged chance plus the difference, so only what the
        blend moved off the line can make an edge. Unpriced spreads and totals
        count as an even -110 market; moneylines need prices. Pushes and ties
        come from the final prediction.
        """
        spread, total = f["spread_line"].to_numpy(float), f["total_line"].to_numpy(float)
        ref_margin = np.where(np.isnan(spread), means["margin"], spread)
        ref_total = np.where(np.isnan(total), means["total"], total)
        rh, ra = simulate((ref_total + ref_margin) / 2, (ref_total - ref_margin) / 2, self.scoring,
                          n_sims=n_sims, playoff=f["playoff"].to_numpy(), seed=seed)
        pred = line_probs(home, away, self.scoring, spread, total)
        ref = line_probs(rh, ra, self.scoring, spread, total)

        def col(name, default=np.nan):
            return f[name].to_numpy(float) if name in f else np.full(len(f), default)

        cover = anchored(market_chance(col("home_spread_odds"), col("away_spread_odds")),
                         no_push(pred["home_cover_prob"], pred["spread_push_prob"]),
                         no_push(ref["home_cover_prob"], ref["spread_push_prob"]))
        over = anchored(market_chance(col("over_odds"), col("under_odds")),
                        no_push(pred["over_prob"], pred["total_push_prob"]),
                        no_push(ref["over_prob"], ref["total_push_prob"]))
        win = anchored(market_chance(col("home_moneyline"), col("away_moneyline"), default=np.nan),
                       no_push(pred["home_win_prob"], pred["tie_prob"]),
                       no_push(ref["home_win_prob"], ref["tie_prob"]))
        return pd.DataFrame({
            "home_cover_prob": with_push(cover, pred["spread_push_prob"]),
            "spread_push_prob": pred["spread_push_prob"].to_numpy(),
            "over_prob": with_push(over, pred["total_push_prob"]),
            "total_push_prob": pred["total_push_prob"].to_numpy(),
            "home_ml_prob": with_push(win, pred["tie_prob"]),
            "away_ml_prob": with_push(1.0 - win, pred["tie_prob"]),
        })

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
