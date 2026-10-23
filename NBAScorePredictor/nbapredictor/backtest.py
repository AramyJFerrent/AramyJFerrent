"""Walk-forward backtest, scored side by side with the closing line.

Each game is predicted from ratings built on earlier days of its season plus
the preseason priors, and the points map, market blend and simulator are
fitted only on the seasons before it. Nothing from the season being scored
leaks in except the closing lines and who played (the final injury report at
tip-off); minutes are always projected, never taken from the box score. A
second pass projects availability from each team's previous game instead, as
a morning run before injury news would.
"""

from __future__ import annotations

import itertools
import logging
import os
from concurrent.futures import ProcessPoolExecutor
from dataclasses import replace

import numpy as np
import pandas as pd
from bettingcore import devig
from scipy.stats import norm

from . import edges
from .config import Hyperparams
from .features import FeatureBuilder
from .model import EDGE_PROBS, ScoreModel
from .simulate import line_probs

log = logging.getLogger(__name__)

TEAM_ONLY_FEATURES = ["eff_off", "eff_def", "home", "b2b", "b2b_opp", "playoff"]
OPEN_PRICES = ["home_moneyline", "away_moneyline", "home_spread_price", "away_spread_price", "over_price",
               "under_price"]
MODEL_LINE_COLUMNS = ["model_home_cover_prob", "model_spread_push_prob", "model_over_prob", "model_total_push_prob"]


def predict_seasons(features: pd.DataFrame, seasons, window: int, n_sims: int = 2000) -> pd.DataFrame:
    """Out-of-sample predictions for every completed game in ``seasons``."""
    out = []
    for season in seasons:
        train = features[(features["season"] >= season - window) & (features["season"] < season)]
        test = features[(features["season"] == season) & features["completed"]].reset_index(drop=True)
        if test.empty or train.empty:
            continue
        model = ScoreModel.fit(train)
        pred, sim = model.predict(test, n_sims=n_sims, seed=season)
        own, own_sim = model.predict(test, n_sims=n_sims, seed=season, market=False)
        pred["model_home_prob"] = own["home_win_prob"]
        # The final prediction's anchored chances against the closing line, and against the
        # opening one (predicted again with the opener in place of the close, unpriced).
        for col, v in model.edge_chances(test, sim, n_sims=n_sims, seed=season).items():
            pred[col] = v
        opened = test.assign(spread=test["open_spread"], total=test["open_total"],
                             **{c: np.nan for c in OPEN_PRICES})
        _, open_sim = model.predict(opened, n_sims=n_sims, seed=season)
        for col, v in model.edge_chances(opened, open_sim, n_sims=n_sims, seed=season).items():
            pred[f"open_{col}"] = v
        # The model's own chances against the same lines, for the old rule.
        for col, v in line_probs(own_sim, test["spread"], test["total"]).items():
            pred[col] = v
        for col, v in line_probs(own_sim, test["open_spread"], test["open_total"]).items():
            pred[f"open_{col}"] = v
        team = ScoreModel.fit(train, eff_features=TEAM_ONLY_FEATURES, calibrate_sim=False, use_market=False)
        tm = team.model_means(test)
        pred["team_margin"] = tm["margin"]
        pred["team_total"] = tm["final_total"]
        sd = float(np.std(own["sim_home"] - own["sim_away"] - (test["home_score"] - test["away_score"])))
        pred["team_home_prob"] = norm.cdf(tm["margin"] / max(sd, 1.0))
        pred["margin_weight"] = model.margin_weight
        pred["total_weight"] = model.total_weight
        out.append(pd.concat([test, pred.drop(columns="game_id")], axis=1))
        log.info("Backtested %s: %d games (market weight %.2f on the margin, %.2f on the total)", season,
                 len(test), 1 - model.margin_weight, 1 - model.total_weight)
    return pd.concat(out, ignore_index=True)


def _log_loss(p, y) -> np.ndarray:
    p = np.clip(np.asarray(p, dtype=float), 1e-4, 1 - 1e-4)
    return -(y * np.log(p) + (1 - y) * np.log(1 - p))


def outcome(bt: pd.DataFrame) -> np.ndarray:
    return (bt["home_score"] > bt["away_score"]).astype(float).to_numpy()


def market_prob(bt: pd.DataFrame) -> np.ndarray:
    """De-vigged closing moneyline, or the spread through a normal where the
    moneyline is missing."""
    p = devig(bt["home_moneyline"], bt["away_moneyline"])
    return np.where(np.isnan(p), norm.cdf(bt["spread"].to_numpy(float) / 13.0), p)


def score(bt: pd.DataFrame) -> pd.DataFrame:
    """Accuracy of the final prediction, its parts and the benchmarks on the same games (with a line)."""
    bt = bt[bt["spread"].notna() & bt["total"].notna()]
    margin = (bt["home_score"] - bt["away_score"]).to_numpy(float)
    total = (bt["home_score"] + bt["away_score"]).to_numpy(float)
    y = outcome(bt)
    env_total = 2 * bt["env_ppp"].to_numpy() * bt["env_pace"].to_numpy() / 100.0
    candidates = {
        "Final (model + market + simulator)": (bt["sim_home"] - bt["sim_away"], bt["sim_total"], bt["home_win_prob"]),
        "Model only": (bt["pred_model_margin"], bt["pred_model_total"], bt["model_home_prob"]),
        "Team ratings only": (bt["team_margin"], bt["team_total"], bt["team_home_prob"]),
        "Elo": (bt["elo_spread"], pd.Series(env_total, index=bt.index), bt["elo_home_prob"]),
        "Closing line": (bt["spread"], bt["total"], market_prob(bt)),
    }
    rows = []
    for name, (m, t, p) in candidates.items():
        m, t, p = (np.asarray(x, dtype=float) for x in (m, t, p))
        home, away = (t + m) / 2, (t - m) / 2
        team_err = np.concatenate([np.abs(bt["home_score"] - home), np.abs(bt["away_score"] - away)])
        rows.append({
            "predictor": name, "games": len(bt),
            "margin_mae": float(np.mean(np.abs(margin - m))),
            "margin_rmse": float(np.sqrt(np.mean((margin - m) ** 2))),
            "total_mae": float(np.mean(np.abs(total - t))),
            "team_points_mae": float(np.mean(team_err)),
            "log_loss": float(np.mean(_log_loss(p, y))),
            "brier": float(np.mean((p - y) ** 2)),
            "winner_pct": float(np.mean((m > 0) == (margin > 0))),
        })
    return pd.DataFrame(rows)


def errors(bt: pd.DataFrame) -> dict[str, np.ndarray]:
    """Per-game absolute margin errors, for paired comparisons."""
    bt = bt[bt["spread"].notna() & bt["total"].notna()]
    margin = (bt["home_score"] - bt["away_score"]).to_numpy(float)
    return {"final": np.abs(margin - (bt["sim_home"] - bt["sim_away"]).to_numpy()),
            "model": np.abs(margin - bt["pred_model_margin"].to_numpy()),
            "team": np.abs(margin - bt["team_margin"].to_numpy()),
            "line": np.abs(margin - bt["spread"].to_numpy(float))}


def distribution_checks(bt: pd.DataFrame) -> dict:
    """Calibration of win probabilities and ranges, and the shape of scores."""
    y = outcome(bt)
    p = bt["home_win_prob"].to_numpy()
    bins = np.linspace(0, 1, 11)
    which = np.clip(np.digitize(p, bins) - 1, 0, 9)
    calib = pd.DataFrame({"bin": which, "p": p, "won": y}).groupby("bin").agg(
        games=("p", "size"), predicted=("p", "mean"), actual=("won", "mean"))
    calib.index = [f"{int(bins[i] * 100)}-{int(bins[i + 1] * 100)}%" for i in calib.index]
    margin = (bt["home_score"] - bt["away_score"]).to_numpy()
    total = (bt["home_score"] + bt["away_score"]).to_numpy()
    inside = np.concatenate([
        (bt["home_score"] >= bt["home_low"]) & (bt["home_score"] <= bt["home_high"]),
        (bt["away_score"] >= bt["away_low"]) & (bt["away_score"] <= bt["away_high"]),
    ])
    reg = bt[bt["game_type"] != "P"]
    sim_margin = (bt["sim_home"] - bt["sim_away"]).to_numpy()
    return {
        "calibration": calib,
        "range_coverage": float(np.mean(inside)),
        "margin_coverage": float(np.mean((margin >= bt["margin_low"]) & (margin <= bt["margin_high"]))),
        "total_coverage": float(np.mean((total >= bt["total_low"]) & (total <= bt["total_high"]))),
        "ot_predicted": float(reg["ot_prob"].mean()), "ot_actual": float((reg["periods"] > 4).mean()),
        "margin_sd": float(np.std(margin - sim_margin)), "total_sd": float(np.std(total - bt["sim_total"])),
        "headline_winner": float(np.mean((bt["headline_home"] > bt["headline_away"]) == (margin > 0))),
    }


def edge_records(bt: pd.DataFrame, lines: str = "close", chances: str = "final") -> dict:
    """Walk-forward record of the betting edges in each market, against the
    closing lines or the opening ones (``lines="open"``), priced with the
    final prediction's anchored chances or the model's own (``chances="model"``).

    The archives have closing moneylines but no spread or total prices, so
    those are assumed to be -110; opening lines have no moneyline, so that
    market is left out there. Opening-line spread edges also report how often
    the line then moved toward the edge's side by the close.
    """
    cols = EDGE_PROBS + MODEL_LINE_COLUMNS
    d = bt[["game_id", "home_team", "away_team", "home_score", "away_score", "model_home_prob"]].copy()
    if lines == "open":
        d["spread"], d["total"] = bt["open_spread"], bt["open_total"]
        for col in cols:
            d[col] = bt[f"open_{col}"]
        d["home_moneyline"] = d["away_moneyline"] = np.nan
    else:
        for col in ["spread", "total", "home_moneyline", "away_moneyline", *cols]:
            d[col] = bt[col]
    d = pd.concat([d, edges.edge_columns(d, chances)], axis=1)
    out = {}
    for m in edges.MARKETS:
        if m == "moneyline" and lines == "open":
            continue
        r = edges.record(d, m)
        if m == "spread" and lines == "open":
            toward, moved = edges.moved_toward(d["spread_edge_side"], bt["open_spread"], bt["spread"])
            r["moved_toward"] = toward / moved if moved else np.nan
            r["moved_games"] = moved
        out[m] = r
    return out


# ---- tuning ------------------------------------------------------------

def _evaluate(args) -> dict:
    summaries, lines, hp, seasons, features = args
    fb = FeatureBuilder(summaries, hp, lines)
    first = int(summaries["games"]["season"].min()) + 1
    feats = fb.walk_forward(range(first, max(seasons) + 1))
    m_err, t_err = [], []
    for season in seasons:
        train = feats[(feats["season"] >= season - hp.fit_window_seasons) & (feats["season"] < season)]
        test = feats[(feats["season"] == season) & feats["completed"]].reset_index(drop=True)
        model = ScoreModel.fit(train, eff_features=features, calibrate_sim=False, use_market=False)
        pred = model.model_means(test)
        m_err.append(np.abs((test["home_score"] - test["away_score"]).to_numpy() - pred["margin"]))
        t_err.append(np.abs((test["home_score"] + test["away_score"]).to_numpy() - pred["final_total"]))
    m, t = float(np.concatenate(m_err).mean()), float(np.concatenate(t_err).mean())
    return {"margin_mae": m, "total_mae": t}


def tune(summaries, lines, seasons, grid: dict, base: Hyperparams | None = None, features=None,
         workers: int | None = None) -> pd.DataFrame:
    """Grid search over the ratings settings, scored on model-only accuracy
    (margin plus total mean absolute error).

    Only the ratings engines are tuned; the points map is refitted on prior
    seasons inside each fold, as in production.
    """
    from .model import EFF_FEATURES

    base = base or Hyperparams()
    keys = list(grid)
    combos = list(itertools.product(*(grid[k] for k in keys)))
    jobs = [(summaries, lines, replace(base, **dict(zip(keys, c))), list(seasons), features or EFF_FEATURES)
            for c in combos]
    workers = workers or min(4, os.cpu_count() or 1)
    with ProcessPoolExecutor(max_workers=workers) as pool:
        scores = list(pool.map(_evaluate, jobs))
    results = []
    for combo, sc in zip(combos, scores):
        results.append({**dict(zip(keys, combo)), **sc, "objective": sc["margin_mae"] + sc["total_mae"]})
        log.info("%s -> %s", dict(zip(keys, combo)), sc)
    return pd.DataFrame(results).sort_values("objective", ignore_index=True)
