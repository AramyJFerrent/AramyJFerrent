"""From pregame features to expected points and full score distributions.

Fitted on recent seasons each time it runs:

1. Two linear maps from ratings to points: one for the margin (offense and
   defense ratings, net special teams, home field and its conference-game
   version, the FBS-vs-FCS gap and Elo) and one for the total (offense,
   defense and pace, on top of the current scoring level).
   Fitting them separately lets the total lean on ratings less than the
   margin does, which is what out-of-sample results ask for.
2. Market blend weights for margin and total against the betting line, fitted
   on out-of-fold predictions (each training season predicted by maps fitted
   on the others), so the model is not trusted for its fit to games it was
   fitted on.
3. The score simulator's dispersion and key-number weights, so ranges and win
   probabilities match how far real results land from the prediction.
"""

from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np
import pandas as pd
from bettingcore import anchored, market_chance, no_push, with_push

from .qb import DROPBACKS_PER_GAME
from .simulate import ScoringModel, calibrate, fit_margin_weights, simulate, summarize

MARGIN_FEATURES = ["off", "def_opp", "st", "home", "home_conf", "fcs", "elo"]
# The final prediction's chances against the posted lines, anchored to the market's
# (see ``ScoreModel.edge_chances``), which the betting edges use.
EDGE_PROBS = ["home_cover_prob", "spread_push_prob", "over_prob", "total_push_prob", "home_ml_prob"]
TOTAL_FEATURES = ["off", "def_opp", "pace"]
# Candidates evaluated in the backtest (see README); they did not earn a place.
OPTIONAL_FEATURES = ["travel", "tz_west", "tz_east", "rest"]


def team_view(f: pd.DataFrame) -> pd.DataFrame:
    """Two rows per game, one from each team's side, with the point features."""
    sides = []
    n = len(f)
    neutral = f["neutral"].astype(bool).to_numpy()
    conf_game = f["conference_game"].astype(bool).to_numpy()
    pace = ((f["off_pace_home"] + f["def_pace_away"] + f["off_pace_away"] + f["def_pace_home"]) / 4).to_numpy() \
        if "off_pace_home" in f else np.zeros(n)
    for side, other, sign in (("home", "away", 1.0), ("away", "home", -1.0)):
        home = np.where(neutral, 0.0, 0.5 * sign)
        div, opp_div = f[f"{side}_division"].to_numpy(), f[f"{other}_division"].to_numpy()
        fcs = np.where((div == "fbs") & (opp_div == "fcs"), 1.0, np.where((div == "fcs") & (opp_div == "fbs"), -1.0, 0.0))
        rest = sign * np.clip(f["home_rest"].fillna(7) - f["away_rest"].fillna(7), -7, 7).to_numpy() / 2.0 \
            if "home_rest" in f else np.zeros(n)
        shift = f[f"{side}_tz_shift"].fillna(0.0).to_numpy() if f"{side}_tz_shift" in f else np.zeros(n)
        miles = f[f"{side}_miles"].fillna(0.0).to_numpy() if f"{side}_miles" in f else np.zeros(n)
        qb = f[f"{side}_qb_adj"].fillna(0.0).to_numpy() * DROPBACKS_PER_GAME if f"{side}_qb_adj" in f else np.zeros(n)
        sides.append(pd.DataFrame({
            "game_id": f["game_id"].to_numpy(),
            "side": side,
            "off": f[f"off_{side}"].to_numpy(),
            "def_opp": f[f"def_{other}"].to_numpy(),
            # Net special-teams edge: own units against the opponent's. The two
            # ratings mirror each other, so they enter as one number.
            "st": (f[f"off_st_{side}"] + f[f"def_st_{other}"]).to_numpy(),
            "home": home,
            "home_conf": home * conf_game,
            "fcs": fcs,
            "elo": sign * f["elo_spread"].fillna(0.0).to_numpy() / 2.0,
            "pace": pace,
            "travel": miles / 1000.0,
            "tz_west": np.clip(-shift, 0, None),
            "tz_east": np.clip(shift, 0, None),
            "rest": rest,
            "qb": qb,
            "env": f["env_points"].to_numpy(),
            "points": f[f"{side}_score"].to_numpy(),
        }))
    return pd.concat(sides, ignore_index=True)


def game_view(f: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame, np.ndarray]:
    """Home-minus-away and home-plus-away versions of the side features, and 2 x env."""
    tv = team_view(f)
    n = len(f)
    cols = [c for c in tv.columns if c not in ("game_id", "side", "env", "points")]
    home, away = tv.iloc[:n][cols].reset_index(drop=True), tv.iloc[n:][cols].reset_index(drop=True)
    return home - away, home + away, 2 * tv["env"].to_numpy()[:n]


def market_probs(home: np.ndarray, away: np.ndarray, spread_line: np.ndarray, total_line: np.ndarray,
                 scoring: ScoringModel, prefix: str = "model_") -> dict:
    """Win, cover and over chances (with pushes) from simulated scores, against each game's lines.

    ``spread_line`` is the expected home margin; the home team covers when it
    wins by more. Simulations carry the key-number weights, as in ``summarize``.
    Games without a line get NaN for that market. Keys start with ``prefix``.
    """
    w = scoring.weights(home, away)
    w = w / w.sum(axis=1, keepdims=True)
    margin, total = home - away, home + away
    spread, tot = spread_line[:, None], total_line[:, None]

    def share(mask, line=None):
        p = (w * mask).sum(axis=1)
        return p if line is None else np.where(np.isnan(line), np.nan, p)
    return {
        f"{prefix}home_win_prob": share(margin > 0),
        f"{prefix}home_cover_prob": share(margin > spread, spread_line),
        f"{prefix}spread_push_prob": share(margin == spread, spread_line),
        f"{prefix}over_prob": share(total > tot, total_line),
        f"{prefix}total_push_prob": share(total == tot, total_line),
    }


def _convex_weight(model: np.ndarray, market: np.ndarray, actual: np.ndarray) -> float:
    gap = model - market
    denom = float(gap @ gap)
    return float(np.clip(gap @ (actual - market) / denom, 0.0, 1.0)) if denom > 0 else 0.0


@dataclass
class ScoreModel:
    coef: dict = field(default_factory=dict)            # margin, points per unit of each feature
    total_coef: dict = field(default_factory=dict)
    total_intercept: float = 0.0
    margin_weight: float = 1.0
    total_weight: float = 1.0
    scoring: ScoringModel = field(default_factory=ScoringModel)
    fit_games: int = 0
    fit_seasons: tuple = ()

    # ---- fitting -------------------------------------------------------
    @classmethod
    def fit(cls, f: pd.DataFrame, calibrate_scores: bool = True,
            margin_features: list[str] | None = None,
            total_features: list[str] | None = None) -> "ScoreModel":
        margin_features = margin_features or MARGIN_FEATURES
        total_features = total_features or TOTAL_FEATURES
        f = f[f["completed"]].reset_index(drop=True)
        actual_margin = (f["home_score"] - f["away_score"]).to_numpy()
        actual_total = (f["home_score"] + f["away_score"]).to_numpy()
        m = cls._points_maps(f, margin_features, total_features)

        oof = cls._out_of_fold_means(f, margin_features, total_features)
        lines = (f["spread_line"].notna() & f["total_line"].notna()).to_numpy()
        if lines.sum() > 100:
            m.margin_weight = _convex_weight(oof["margin"][lines], f.loc[lines, "spread_line"].to_numpy(),
                                             actual_margin[lines])
            m.total_weight = _convex_weight(oof["total"][lines], f.loc[lines, "total_line"].to_numpy(),
                                            actual_total[lines])
        if calibrate_scores:
            final = m.means(f)
            scoring = calibrate(ScoringModel(), float(np.std(actual_margin - final["margin"])),
                                float(np.std(actual_total - final["total"])),
                                mean_points=float(np.mean(final["total"]) / 2))
            m.scoring = fit_margin_weights(scoring, final["home"], final["away"], actual_margin)
        return m

    @classmethod
    def _points_maps(cls, f: pd.DataFrame, margin_features: list[str], total_features: list[str]) -> "ScoreModel":
        """The margin and total maps from ratings to points, fitted on ``f`` (completed games)."""
        diff, both, env2 = game_view(f)
        actual_margin = (f["home_score"] - f["away_score"]).to_numpy()
        actual_total = (f["home_score"] + f["away_score"]).to_numpy()
        a, *_ = np.linalg.lstsq(diff[margin_features].to_numpy(float), actual_margin, rcond=None)
        X = np.column_stack([np.ones(len(f)), both[total_features].to_numpy(float)])
        b, *_ = np.linalg.lstsq(X, actual_total - env2, rcond=None)
        return cls(coef=dict(zip(margin_features, map(float, a))),
                   total_coef=dict(zip(total_features, map(float, b[1:]))), total_intercept=float(b[0]),
                   fit_games=len(f), fit_seasons=tuple(sorted(f["season"].unique().tolist())))

    @classmethod
    def _out_of_fold_means(cls, f: pd.DataFrame, margin_features: list[str], total_features: list[str]) -> dict:
        """The model's margin and total for each game from maps fitted on the other seasons.

        With fewer than three seasons there is nothing to hold out, and the
        in-sample means are returned.
        """
        seasons = f["season"].to_numpy()
        pred = cls._points_maps(f, margin_features, total_features).model_means(f)
        if len(np.unique(seasons)) < 3:
            return pred
        out = {k: np.array(v, dtype=float, copy=True) for k, v in pred.items()}
        for season in np.unique(seasons):
            held = seasons == season
            fold = cls._points_maps(f[~held], margin_features, total_features).model_means(f[held])
            for k in out:
                out[k][held] = fold[k]
        return out

    # ---- prediction ----------------------------------------------------
    def model_means(self, f: pd.DataFrame) -> dict:
        diff, both, env2 = game_view(f)
        margin = diff[list(self.coef)].to_numpy(float) @ np.array(list(self.coef.values()))
        total = env2 + self.total_intercept + both[list(self.total_coef)].to_numpy(float) @ np.array(
            list(self.total_coef.values()))
        # Neither team can be expected to score less than a field goal's worth.
        total = np.maximum(total, np.abs(margin) + 6.0)
        home, away = (total + margin) / 2, (total - margin) / 2
        return {"home": home, "away": away, "margin": margin, "total": total}

    def blend(self, f: pd.DataFrame, pred: dict) -> dict:
        """The margin blended with the spread and the total with the total line, each where posted."""
        spread, total = f["spread_line"].to_numpy(float), f["total_line"].to_numpy(float)
        has_spread, has_total = ~np.isnan(spread), ~np.isnan(total)
        margin = np.where(has_spread, self.margin_weight * pred["margin"] + (1 - self.margin_weight) * spread,
                          pred["margin"])
        tot = np.where(has_total, self.total_weight * pred["total"] + (1 - self.total_weight) * total,
                       pred["total"])
        return {"margin": margin, "total": tot, "has_market": has_spread & has_total}

    def means(self, f: pd.DataFrame) -> dict:
        """Final expected points: the model blended with the market."""
        pred = self.model_means(f)
        b = self.blend(f, pred)
        margin = b["margin"]
        total = np.maximum(b["total"], np.abs(margin) + 6.0)
        return {
            "home": (total + margin) / 2, "away": (total - margin) / 2,
            "margin": margin, "total": total,
            "model_margin": pred["margin"], "model_total": pred["total"],
            "has_market": b["has_market"],
        }

    def predict(self, f: pd.DataFrame, n_sims: int = 10000, seed: int = 0) -> pd.DataFrame:
        """Final prediction per game. Its win, cover and over chances against the posted
        lines (``home_cover_prob`` ...) price the betting edges; the ``model_*`` chances
        are the model's own, before the blend, for comparison."""
        means = self.means(f)
        home, away = simulate(means["home"], means["away"], self.scoring, n_sims=n_sims, seed=seed)
        out = summarize(home, away, means["home"], means["away"], self.scoring)
        out.insert(0, "game_id", f["game_id"].to_numpy())
        for key in ("home", "away", "margin", "total", "model_margin", "model_total"):
            out[f"pred_{key}"] = means[key]
        edges = self.edge_chances(f, means, home, away, n_sims=n_sims, seed=seed)
        for key in EDGE_PROBS:
            out[key] = edges[key]
        # The same simulator run on the model's own expected points, before any blending with the line.
        own = self.model_means(f)
        home, away = simulate(own["home"], own["away"], self.scoring, n_sims=n_sims, seed=seed)
        probs = market_probs(home, away, f["spread_line"].to_numpy(float), f["total_line"].to_numpy(float),
                             self.scoring)
        for key, values in probs.items():
            out[key] = values
        return out

    def edge_chances(self, f: pd.DataFrame, means: dict, home: np.ndarray, away: np.ndarray,
                     n_sims: int = 10000, seed: int = 0) -> dict:
        """Each side's chance against the posted lines, anchored to the market (``bettingcore.anchor``).

        The final prediction's simulated chances (``home``, ``away``) are set
        against a second simulation, with the same seed, centered on the lines
        themselves; each side gets the market's de-vigged chance plus the
        difference, so only what the blend moved off the line can make an edge.
        Unpriced spreads and totals count as an even -110 market; moneylines
        need prices. Pushes come from the final prediction.
        """
        spread, total = f["spread_line"].to_numpy(float), f["total_line"].to_numpy(float)
        ref_margin = np.where(np.isnan(spread), means["margin"], spread)
        ref_total = np.maximum(np.where(np.isnan(total), means["total"], total), np.abs(ref_margin) + 6.0)
        rh, ra = simulate((ref_total + ref_margin) / 2, (ref_total - ref_margin) / 2, self.scoring,
                          n_sims=n_sims, seed=seed)
        pred = market_probs(home, away, spread, total, self.scoring, prefix="")
        ref = market_probs(rh, ra, spread, total, self.scoring, prefix="")

        def col(name):
            return f[name].to_numpy(float) if name in f else np.full(len(f), np.nan)

        cover = anchored(market_chance(col("home_spread_price"), col("away_spread_price")),
                         no_push(pred["home_cover_prob"], pred["spread_push_prob"]),
                         no_push(ref["home_cover_prob"], ref["spread_push_prob"]))
        over = anchored(market_chance(col("over_price"), col("under_price")),
                        no_push(pred["over_prob"], pred["total_push_prob"]),
                        no_push(ref["over_prob"], ref["total_push_prob"]))
        win = anchored(market_chance(col("home_moneyline"), col("away_moneyline"), default=np.nan),
                       pred["home_win_prob"], ref["home_win_prob"])
        return {"home_cover_prob": with_push(cover, pred["spread_push_prob"]),
                "spread_push_prob": pred["spread_push_prob"],
                "over_prob": with_push(over, pred["total_push_prob"]),
                "total_push_prob": pred["total_push_prob"], "home_ml_prob": win}

    # ---- persistence ---------------------------------------------------
    def to_dict(self) -> dict:
        return {
            "coef": self.coef, "total_coef": self.total_coef, "total_intercept": self.total_intercept,
            "margin_weight": self.margin_weight, "total_weight": self.total_weight,
            "scoring": self.scoring.to_dict(),
            "fit_games": self.fit_games, "fit_seasons": list(self.fit_seasons),
        }

    @classmethod
    def from_dict(cls, d: dict) -> "ScoreModel":
        d = dict(d)
        d["scoring"] = ScoringModel.from_dict(d["scoring"])
        d["fit_seasons"] = tuple(d.get("fit_seasons", ()))
        return cls(**d)
