"""Expected goals: the chance each unblocked shot becomes a goal.

A logistic regression on where the shot came from (distance and angle, as
piecewise-linear terms), how it was taken (wrist, slap, tip-in and so on),
whether it was a rebound or came off the rush, and the strength state. It is
fitted once on the 2010-11 to 2014-15 seasons and frozen in
``data/shot_model.json``, so no later season (and none of the backtest) is
scored by a model that saw its results.

The same file holds score-and-venue weights for 5-on-5 shots: trailing teams
outshoot leading ones, so each team's xG is reweighted by how its share in the
current score state differs from its overall share (McCurdy's method).
"""

from __future__ import annotations

import json
import logging
from pathlib import Path

import numpy as np
import pandas as pd

from .config import SHOT_MODEL_PATH

log = logging.getLogger(__name__)

FENWICK = ["SHOT", "MISSED_SHOT", "GOAL"]
SHOT_TYPES = ["slap", "snap", "backhand", "tip-in", "deflected", "wrap-around"]
# Types the NHL began recording after the fit seasons, mapped to the nearest old one.
TYPE_MAP = {"bat": "deflected", "poke": "backhand", "between-legs": "wrap-around", "cradle": "wrap-around"}
DIST_KNOTS = [8.0, 15.0, 25.0, 40.0, 60.0]
STRENGTHS = ["pp", "sh", "four_on_four", "extra_attacker"]
FEATURES = (["dist", "log_dist"] + [f"dist_{int(k)}" for k in DIST_KNOTS] + ["angle", "angle_sq"]
            + [f"type_{t}" for t in SHOT_TYPES] + ["rebound", "rush", "rebound_angle"]
            + [f"str_{s}" for s in STRENGTHS])
PENALTY_SHOT_XG = 0.32
SCORE_STATES = list(range(-3, 4))
REBOUND_SECONDS = 3
RUSH_SECONDS = 4
RUSH_FEET = 60.0


def shot_events(pbp: pd.DataFrame) -> pd.DataFrame:
    """Unblocked shots outside the shootout with shooter-side context.

    Columns added: ``side`` (home or away), ``strength`` (ev, pp, sh,
    four_on_four, extra_attacker, empty_net or penalty_shot), ``goal``,
    ``home_lead`` (the score before the shot, home minus away) and the
    rebound and rush flags.
    """
    p = pbp[pbp["period_type"].ne("SHOOTOUT")].sort_values(["game_id", "event_idx"])
    prev = p.groupby(["game_id", "period"])
    p = p.assign(prev_type=prev["event_type"].shift(), prev_side=prev["event_team_type"].shift(),
                 prev_secs=prev["game_seconds"].shift(), prev_x=prev["x"].shift(),
                 prev_angle=prev["shot_angle"].shift())
    s = p[p["event_type"].isin(FENWICK) & p["event_team_type"].isin(["home", "away"])].copy()
    home = s["event_team_type"].eq("home")
    s["side"] = np.where(home, "home", "away")
    s["goal"] = s["event_type"].eq("GOAL").astype(int)
    sk_for = np.where(home, s["home_skaters"], s["away_skaters"]).astype(float)
    sk_ag = np.where(home, s["away_skaters"], s["home_skaters"]).astype(float)
    empty = s["empty_net"].fillna(False).astype(bool).to_numpy()
    extra = s["extra_attacker"].fillna(False).astype(bool).to_numpy()
    s["strength"] = np.select(
        [sk_ag == 0, empty, extra, sk_for > sk_ag, sk_for < sk_ag, (sk_for == 5) & (sk_ag == 5)],
        ["penalty_shot", "empty_net", "extra_attacker", "pp", "sh", "ev"], "four_on_four")
    scored_home = (s["goal"] == 1) & home
    scored_away = (s["goal"] == 1) & ~home
    s["home_lead"] = (s["home_score"] - scored_home) - (s["away_score"] - scored_away)
    gap = s["game_seconds"] - s["prev_secs"]
    s["rebound"] = (s["prev_type"].isin(["SHOT", "MISSED_SHOT"]) & (s["prev_side"] == s["event_team_type"])
                    & (gap <= REBOUND_SECONDS)).astype(int)
    s["rush"] = ((gap <= RUSH_SECONDS) & ((s["x"] - s["prev_x"]).abs() >= RUSH_FEET)
                 & s["rebound"].eq(0)).astype(int)
    s["angle_change"] = np.where(s["rebound"] == 1, (s["shot_angle"] - s["prev_angle"]).abs(), 0.0)
    return s


def design(shots: pd.DataFrame) -> np.ndarray:
    dist = shots["shot_distance"].astype(float).fillna(35.0).clip(0.0, 100.0).to_numpy()
    angle = shots["shot_angle"].astype(float).abs().fillna(25.0).clip(0.0, 120.0).to_numpy()
    kind = shots["secondary_type"].replace(TYPE_MAP).to_numpy()
    cols = [dist, np.log1p(dist)] + [np.maximum(dist - k, 0.0) for k in DIST_KNOTS]
    cols += [angle / 10.0, (angle / 10.0) ** 2]
    cols += [(kind == t).astype(float) for t in SHOT_TYPES]
    change = np.nan_to_num(shots["angle_change"].astype(float).to_numpy()).clip(0.0, 90.0) / 10.0
    cols += [shots["rebound"].to_numpy(float), shots["rush"].to_numpy(float), change]
    cols += [(shots["strength"] == st).to_numpy(float) for st in STRENGTHS]
    return np.column_stack([np.ones(len(shots))] + cols)


def fit_logistic(X: np.ndarray, y: np.ndarray, l2: float = 1.0, iters: int = 25) -> np.ndarray:
    """Logistic regression by iteratively reweighted least squares."""
    beta = np.zeros(X.shape[1])
    beta[0] = np.log(y.mean() / (1 - y.mean()))
    penalty = np.full(X.shape[1], l2)
    penalty[0] = 0.0
    for _ in range(iters):
        p = 1.0 / (1.0 + np.exp(-(X @ beta)))
        w = np.clip(p * (1 - p), 1e-6, None)
        grad = X.T @ (y - p) - penalty * beta
        hess = (X * w[:, None]).T @ X + np.diag(penalty)
        step = np.linalg.solve(hess, grad)
        beta += step
        if np.max(np.abs(step)) < 1e-7:
            break
    return beta


class ShotModel:
    def __init__(self, coef: np.ndarray, home_weights: dict, away_weights: dict, meta: dict | None = None):
        self.coef = np.asarray(coef, dtype=float)
        self.home_weights = {int(k): float(v) for k, v in home_weights.items()}
        self.away_weights = {int(k): float(v) for k, v in away_weights.items()}
        self.meta = meta or {}

    def xg(self, shots: pd.DataFrame) -> np.ndarray:
        """Goal probability for each shot from ``shot_events``. Shots on an
        empty net get the model value too; callers leave them out of ratings."""
        if shots.empty:
            return np.zeros(0)
        p = 1.0 / (1.0 + np.exp(-(design(shots) @ self.coef)))
        return np.where(shots["strength"].eq("penalty_shot"), PENALTY_SHOT_XG, p)

    def score_weight(self, shots: pd.DataFrame) -> np.ndarray:
        """Score-and-venue weight for each shot (1 outside 5-on-5)."""
        lead = shots["home_lead"].clip(-3, 3).to_numpy()
        home = shots["side"].eq("home").to_numpy()
        hw = np.array([self.home_weights[int(v)] for v in lead]) if len(lead) else np.zeros(0)
        aw = np.array([self.away_weights[int(v)] for v in lead]) if len(lead) else np.zeros(0)
        return np.where(shots["strength"].eq("ev"), np.where(home, hw, aw), 1.0)

    def to_dict(self) -> dict:
        return {"features": ["intercept"] + FEATURES, "coef": [round(float(c), 6) for c in self.coef],
                "home_weights": {str(k): round(v, 4) for k, v in self.home_weights.items()},
                "away_weights": {str(k): round(v, 4) for k, v in self.away_weights.items()},
                **self.meta}

    def save(self, path: Path = SHOT_MODEL_PATH) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(self.to_dict(), indent=2) + "\n")

    @classmethod
    def load(cls, path: Path = SHOT_MODEL_PATH) -> "ShotModel":
        d = json.loads(path.read_text())
        if d["features"][1:] != FEATURES:
            raise ValueError(f"{path} was fitted with different features; rerun `fit-shots`")
        meta = {k: v for k, v in d.items() if k not in ("features", "coef", "home_weights", "away_weights")}
        return cls(d["coef"], d["home_weights"], d["away_weights"], meta)


def score_venue_weights(shots: pd.DataFrame, xg: np.ndarray) -> tuple[dict, dict]:
    """McCurdy weights from each side's 5-on-5 xG share by score state."""
    ev = shots["strength"].eq("ev").to_numpy()
    frame = pd.DataFrame({"lead": shots["home_lead"].clip(-3, 3).to_numpy()[ev],
                          "home": shots["side"].eq("home").to_numpy()[ev], "xg": xg[ev]})
    by = frame.groupby(["lead", "home"])["xg"].sum().unstack()
    share = by[True] / (by[True] + by[False])
    overall = frame.loc[frame["home"], "xg"].sum() / frame["xg"].sum()
    home_w = {int(s): float(overall / share[s]) for s in SCORE_STATES}
    away_w = {int(s): float((1 - overall) / (1 - share[s])) for s in SCORE_STATES}
    return home_w, away_w


def fit_shot_model(pbps: list[pd.DataFrame], seasons: tuple[int, int]) -> ShotModel:
    shots = pd.concat([shot_events(p) for p in pbps], ignore_index=True)
    regular = shots[shots["season_type"].eq("R")]
    train = regular[~regular["strength"].isin(["empty_net", "penalty_shot"])]
    X, y = design(train), train["goal"].to_numpy(float)
    coef = fit_logistic(X, y)
    model = ShotModel(coef, {s: 1.0 for s in SCORE_STATES}, {s: 1.0 for s in SCORE_STATES})
    xg = model.xg(regular)
    home_w, away_w = score_venue_weights(regular, xg)
    p = np.clip(model.xg(train), 1e-6, 1 - 1e-6)
    logloss = float(-np.mean(y * np.log(p) + (1 - y) * np.log(1 - p)))
    base = y.mean()
    base_loss = float(-np.mean(y * np.log(base) + (1 - y) * np.log(1 - base)))
    log.info("Shot model: %d shots, log loss %.4f (constant %.4f)", len(train), logloss, base_loss)
    return ShotModel(coef, home_w, away_w, {
        "fit_seasons": list(seasons), "fit_shots": int(len(train)),
        "log_loss": round(logloss, 4), "constant_log_loss": round(base_loss, 4),
    })
