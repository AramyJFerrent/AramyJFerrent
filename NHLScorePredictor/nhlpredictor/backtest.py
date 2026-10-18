"""Walk-forward backtest, scored on probabilities against simple baselines.

Each game is predicted from ratings built on earlier days of its season plus
the preseason prior, and the goal-rate model and simulator are fitted only on
the seasons before it. Nothing from the season being scored leaks in except
the actual starting goalies (a game-day run knows them once they are
confirmed; a separate pass projects them instead, as a morning run would).

No free source has a long history of NHL betting lines, so the market
benchmark comes from the live log: every prediction records the line it was
made against, and the predictions page grades both.
"""

from __future__ import annotations

import itertools
import logging
import os
from concurrent.futures import ProcessPoolExecutor
from dataclasses import replace

import numpy as np
import pandas as pd
from scipy.stats import poisson

from .config import Hyperparams
from .features import FeatureBuilder
from .model import GoalModel, team_view

log = logging.getLogger(__name__)

BASELINE_FEATURES = ["goals_off", "goals_def", "home"]
MAX_GOALS = 15


def outcome(f: pd.DataFrame) -> np.ndarray:
    return (f["home_score"] > f["away_score"]).astype(float).to_numpy()


def poisson_summary(home_rate: np.ndarray, away_rate: np.ndarray) -> dict:
    """Independent-Poisson regulation outcomes; regulation ties are split by rate."""
    k = np.arange(MAX_GOALS)
    ph = poisson.pmf(k[None, :], np.asarray(home_rate)[:, None])
    pa = poisson.pmf(k[None, :], np.asarray(away_rate)[:, None])
    joint = ph[:, :, None] * pa[:, None, :]
    tie = np.einsum("nii->n", joint)
    home_reg = np.array([np.tril(j, -1).sum() for j in joint])
    one_goal = np.array([np.trace(j, 1) + np.trace(j, -1) for j in joint])
    share = home_rate / (home_rate + away_rate)
    return {"home_win_prob": home_reg + tie * share, "tie_prob": tie, "one_goal_prob": one_goal}


def total_rps(totals: np.ndarray, actual: np.ndarray) -> np.ndarray:
    """Ranked probability score of each game's total-goals distribution (lower is better)."""
    edges = np.arange(MAX_GOALS)
    cdf = (totals[:, :, None] <= edges[None, None, :]).mean(axis=1)
    obs = (np.asarray(actual)[:, None] <= edges[None, :]).astype(float)
    return np.mean((cdf - obs) ** 2, axis=1)


def predict_seasons(features: pd.DataFrame, states: pd.DataFrame, seasons, window: int,
                    n_sims: int = 2000) -> pd.DataFrame:
    """Out-of-sample predictions for every completed game in ``seasons``."""
    out = []
    for season in seasons:
        train = features[(features["season"] >= season - window) & (features["season"] < season)]
        test = features[(features["season"] == season) & features["completed"]].reset_index(drop=True)
        if test.empty or train.empty:
            continue
        model = GoalModel.fit(train, states[states["season"] < season])
        pred, sim = model.predict(test, n_sims=n_sims, seed=season)
        pred["rps_total"] = total_rps(sim["home"] + sim["away"], test["home_score"] + test["away_score"])
        base = GoalModel.fit(train, features=BASELINE_FEATURES, calibrate_sim=False)
        b = base.rates(test)
        indep = poisson_summary(b["home"], b["away"])
        pred["baseline_home_prob"] = indep["home_win_prob"]
        pred["baseline_home_rate"] = b["home"]
        pred["baseline_away_rate"] = b["away"]
        # The same expected total spread as an independent Poisson, to show what
        # the simulator's shape adds.
        edges = np.arange(MAX_GOALS)
        actual = (test["home_score"] + test["away_score"]).to_numpy()
        pred["poisson_rps_total"] = np.mean(
            (poisson.cdf(edges[None, :], pred["sim_total"].to_numpy()[:, None])
             - (actual[:, None] <= edges[None, :])) ** 2, axis=1)
        own = poisson_summary(pred["model_home_rate"].to_numpy(), pred["model_away_rate"].to_numpy())
        pred["indep_tie_prob"] = own["tie_prob"]
        pred["indep_one_goal_prob"] = own["one_goal_prob"]
        out.append(pd.concat([test, pred.drop(columns="game_id")], axis=1))
        log.info("Backtested %s: %d games", season, len(test))
    return pd.concat(out, ignore_index=True)


def _log_loss(p: np.ndarray, y: np.ndarray) -> np.ndarray:
    p = np.clip(np.asarray(p, dtype=float), 1e-4, 1 - 1e-4)
    return -(y * np.log(p) + (1 - y) * np.log(1 - p))


def score(bt: pd.DataFrame) -> pd.DataFrame:
    """Probability and goal accuracy of the model and the baselines on the same games."""
    y = outcome(bt)
    home_share = float(y.mean())
    tv_goals = np.concatenate([bt["home_score"], bt["away_score"]])
    total = (bt["home_score"] + bt["away_score"]).to_numpy()
    candidates = {
        "Model + simulator": (bt["home_win_prob"], np.concatenate([bt["sim_home"], bt["sim_away"]]),
                              bt["rps_total"]),
        "Goals-only Poisson": (bt["baseline_home_prob"], None, None),
        "Elo": (bt["elo_home_prob"], None, None),
        "Home team every time": (np.full(len(bt), home_share), None, None),
    }
    rows = []
    for name, (p, goals, rps) in candidates.items():
        p = np.asarray(p, dtype=float)
        row = {
            "predictor": name, "games": len(bt),
            "log_loss": float(_log_loss(p, y).mean()),
            "brier": float(np.mean((p - y) ** 2)),
            "winner_pct": float(np.mean((p >= 0.5) == (y == 1))),
            "goals_mae": float(np.mean(np.abs(tv_goals - goals))) if goals is not None else np.nan,
            "total_mae": float(np.mean(np.abs(total - (bt["sim_home"] + bt["sim_away"])))) if goals is not None else np.nan,
            "rps_total": float(np.mean(rps)) if rps is not None else np.nan,
        }
        rows.append(row)
    return pd.DataFrame(rows)


def distribution_checks(bt: pd.DataFrame) -> dict:
    """Calibration of win probabilities and ranges, and the shape of final scores."""
    y = outcome(bt)
    p = bt["home_win_prob"].to_numpy()
    bins = np.linspace(0, 1, 11)
    which = np.clip(np.digitize(p, bins) - 1, 0, 9)
    calib = pd.DataFrame({"bin": which, "p": p, "won": y}).groupby("bin").agg(
        games=("p", "size"), predicted=("p", "mean"), actual=("won", "mean"))
    calib.index = [f"{int(bins[i] * 100)}-{int(bins[i + 1] * 100)}%" for i in calib.index]
    inside = np.concatenate([
        (bt["home_score"] >= bt["home_low"]) & (bt["home_score"] <= bt["home_high"]),
        (bt["away_score"] >= bt["away_low"]) & (bt["away_score"] <= bt["away_high"]),
    ])
    reg = bt[~bt["playoff"]]
    reg_margin = (reg["home_reg"] + reg["home_en"]) - (reg["away_reg"] + reg["away_en"])
    no_en_margin = (reg["home_reg"] - reg["away_reg"]).abs()
    return {
        "calibration": calib,
        "range_coverage": float(np.mean(inside)),
        "headline_exact": float(np.mean((bt["headline_home"] == bt["home_score"])
                                        & (bt["headline_away"] == bt["away_score"]))),
        "ot_predicted": float(reg["ot_prob"].mean()), "ot_actual": float((reg["periods"] > 3).mean()),
        "ot_indep": float(reg["indep_tie_prob"].mean()),
        "one_goal_predicted": float(reg["one_goal_reg_prob"].mean()),
        "one_goal_actual": float(np.mean(reg_margin.abs() == 1)),
        "one_goal_indep": float(reg["indep_one_goal_prob"].mean()),
        "one_goal_no_en_actual": float(np.mean(no_en_margin == 1)),
        "en_predicted": float(reg["empty_net_prob"].mean()),
        "en_actual": float(np.mean((reg["home_en"] + reg["away_en"]) > 0)),
        "rps_sim": float(bt["rps_total"].mean()), "rps_poisson": float(bt["poisson_rps_total"].mean()),
        "home_cover_predicted": float(bt["home_cover_prob"].mean()),
        "home_cover_actual": float(np.mean(bt["home_score"] - bt["away_score"] >= 2)),
    }


def paired_bootstrap(loss_a: np.ndarray, loss_b: np.ndarray, n: int = 5000, seed: int = 0) -> tuple:
    """Mean of (a - b) and its 95% interval over resampled games."""
    rng = np.random.default_rng(seed)
    diff = np.asarray(loss_a) - np.asarray(loss_b)
    means = np.array([diff[rng.integers(0, len(diff), len(diff))].mean() for _ in range(n)])
    return float(diff.mean()), float(np.percentile(means, 2.5)), float(np.percentile(means, 97.5))


def log_losses(bt: pd.DataFrame) -> dict[str, np.ndarray]:
    y = outcome(bt)
    return {"model": _log_loss(bt["home_win_prob"], y), "baseline": _log_loss(bt["baseline_home_prob"], y),
            "elo": _log_loss(bt["elo_home_prob"], y)}


def starter_accuracy(blind: pd.DataFrame, known: pd.DataFrame) -> float:
    """Share of starts where the projected goalie was the one who started."""
    k = known.set_index("game_id")
    b = blind.set_index("game_id").reindex(k.index)
    hits, n = 0, 0
    for side in ("home", "away"):
        mask = k[f"{side}_goalie_status"].eq("known") & b[f"{side}_goalie_id"].notna()
        hits += int((b.loc[mask, f"{side}_goalie_id"].astype("int64") == k.loc[mask, f"{side}_goalie_id"].astype("int64")).sum())
        n += int(mask.sum())
    return hits / n if n else float("nan")


# ---- tuning ------------------------------------------------------------

def _evaluate(args) -> dict:
    games, summaries, hp, seasons = args
    fb = FeatureBuilder(games, summaries, hp)
    first = min(seasons)
    feats = fb.walk_forward(range(max(first - hp.fit_window_seasons, int(games["season"].min())), max(seasons) + 1))
    nll, wl = [], []
    for season in seasons:
        train = feats[(feats["season"] >= season - hp.fit_window_seasons) & (feats["season"] < season)]
        test = feats[(feats["season"] == season) & feats["completed"]].reset_index(drop=True)
        model = GoalModel.fit(train, calibrate_sim=False)
        r = model.rates(test)
        tv = team_view(test)
        nll.append(-poisson.logpmf(tv["goals"].to_numpy(), np.concatenate([r["home"], r["away"]])))
        wl.append(_log_loss(poisson_summary(r["home"], r["away"])["home_win_prob"], outcome(test)))
    return {"goal_nll": float(np.concatenate(nll).mean()), "win_log_loss": float(np.concatenate(wl).mean())}


def tune(games, summaries, seasons, grid: dict, base: Hyperparams | None = None,
         workers: int | None = None) -> pd.DataFrame:
    """Grid search over the ratings settings, scored on model-only accuracy
    (Poisson log-likelihood of each team's goals plus win log loss).

    Only the ratings engine is tuned; the goal-rate model is refitted on prior
    seasons inside each fold, as in production.
    """
    base = base or Hyperparams()
    keys = list(grid)
    combos = list(itertools.product(*(grid[k] for k in keys)))
    jobs = [(games, summaries, replace(base, **dict(zip(keys, c))), list(seasons)) for c in combos]
    workers = workers or min(4, os.cpu_count() or 1)
    with ProcessPoolExecutor(max_workers=workers) as pool:
        scores = list(pool.map(_evaluate, jobs))
    results = []
    for combo, sc in zip(combos, scores):
        results.append({**dict(zip(keys, combo)), **sc, "objective": sc["goal_nll"] + sc["win_log_loss"]})
        log.info("%s -> %s", dict(zip(keys, combo)), sc)
    return pd.DataFrame(results).sort_values("objective", ignore_index=True)
