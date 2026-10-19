"""Walk-forward backtest, scored on probabilities against baselines and the market.

Each game is predicted from ratings built on earlier days only (player and
team ratings, park factors from earlier seasons), and the run model and
simulator are fitted on the seasons before it. Lineups and starting
pitchers are the actual ones, which a game-day run knows once lineups post;
a second pass projects the lineups instead, as a morning run would. Weather
is the recorded game-time weather, a little better than a forecast.

Pinnacle's complete 2016 line history is the market benchmark: its closing
moneyline is scored on the same games, the model is blended with it, and the
blend weight found there seeds the live predictor's.
"""

from __future__ import annotations

import logging

import numpy as np
import pandas as pd
from scipy.optimize import minimize
from scipy.stats import nbinom, poisson

from .config import PINNACLE_PATH
from .features import FeatureBuilder
from .market import MarketInverter, blend, devig, fit_blend
from .model import RunModel

log = logging.getLogger(__name__)

MAX_RUNS = 30


def outcome(f: pd.DataFrame) -> np.ndarray:
    return (f["home_score"] > f["away_score"]).astype(float).to_numpy()


def _log_loss(p, y) -> np.ndarray:
    p = np.clip(np.asarray(p, dtype=float), 1e-4, 1 - 1e-4)
    return -(y * np.log(p) + (1 - y) * np.log(1 - p))


def rps(dist_cdf: np.ndarray, actual) -> np.ndarray:
    """Ranked probability score of each distribution (rows of CDF values at 0..MAX_RUNS-1)."""
    edges = np.arange(dist_cdf.shape[1])
    obs = (np.asarray(actual)[:, None] <= edges[None, :]).astype(float)
    return np.mean((dist_cdf - obs) ** 2, axis=1)


def _logit_fit(x: np.ndarray, y: np.ndarray) -> np.ndarray:
    X = np.column_stack([np.ones(len(x)), x])

    def nll(b):
        return float(_log_loss(1 / (1 + np.exp(-(X @ b))), y).mean())
    return minimize(nll, np.zeros(X.shape[1])).x


def team_only(train: pd.DataFrame, test: pd.DataFrame) -> np.ndarray:
    """Baseline: each team's runs-scored and runs-allowed ratings (no players), plus home field."""
    def x(f):
        edge = (f["home_team_off"] + f["home_team_def"]) - (f["away_team_off"] + f["away_team_def"])
        return np.column_stack([edge, np.where(f["neutral"], 0.0, 1.0)])
    b = _logit_fit(x(train), outcome(train))
    X = np.column_stack([np.ones(len(test)), x(test)])
    return 1 / (1 + np.exp(-(X @ b)))


def predict_seasons(feats: pd.DataFrame, fb: FeatureBuilder, seasons, window: int,
                    n_sims: int = 2000) -> pd.DataFrame:
    """Out-of-sample predictions for every completed game in ``seasons``."""
    out = []
    for season in seasons:
        train = feats[feats["season"].between(season - window, season - 1) & feats["completed"]]
        test = feats[(feats["season"] == season) & feats["completed"]].reset_index(drop=True)
        if test.empty or train.empty:
            continue
        model = RunModel.fit(train, fb.chain(season))
        pred, sim = model.predict(test, n_sims=n_sims, seed=season)
        team_cdf = lambda runs: np.stack([(runs <= k).mean(axis=1) for k in range(MAX_RUNS)], axis=1)
        pred["rps_home"] = rps(team_cdf(sim["home"]), test["home_score"])
        pred["rps_away"] = rps(team_cdf(sim["away"]), test["away_score"])
        pred["rps_total"] = rps(team_cdf(sim["home"] + sim["away"]), test["home_score"] + test["away_score"])
        # The same mean runs as plain Poisson and as a negative binomial with
        # variance 2.26 times the mean, to show what the simulator's shape adds.
        for name, cdf in (("poisson", lambda m: poisson.cdf(np.arange(MAX_RUNS)[None, :], m[:, None])),
                          ("nbinom", lambda m: nbinom.cdf(np.arange(MAX_RUNS)[None, :], m[:, None] / 1.26,
                                                          1 / 2.26))):
            pred[f"{name}_rps"] = 0.5 * (rps(cdf(pred["sim_home"].to_numpy()), test["home_score"])
                                         + rps(cdf(pred["sim_away"].to_numpy()), test["away_score"]))
        pred["team_only_prob"] = team_only(train, test)
        pred["coef_x_sp"] = model.coef["x_sp"]
        out.append(pd.concat([test, pred.drop(columns="game_id")], axis=1))
        log.info("Backtested %s: %d games", season, len(test))
    return pd.concat(out, ignore_index=True)


def score(bt: pd.DataFrame) -> pd.DataFrame:
    """Probability and run accuracy of the model and the baselines on the same games."""
    y = outcome(bt)
    total = (bt["home_score"] + bt["away_score"]).to_numpy()
    runs = np.concatenate([bt["home_score"], bt["away_score"]])
    candidates = {
        "Model + simulator": bt["home_win_prob"],
        "Elo with starting pitchers": bt["elo_home_prob"],
        "Team runs ratings only": bt["team_only_prob"],
        "Home team every time": np.full(len(bt), y.mean()),
    }
    rows = []
    for name, p in candidates.items():
        p = np.asarray(p, dtype=float)
        model = name == "Model + simulator"
        rows.append({
            "predictor": name, "games": len(bt),
            "log_loss": float(_log_loss(p, y).mean()), "brier": float(np.mean((p - y) ** 2)),
            "winner_pct": float(np.mean((p >= 0.5) == (y == 1))),
            "runs_mae": float(np.mean(np.abs(runs - np.concatenate([bt["sim_home"], bt["sim_away"]])))) if model else np.nan,
            "total_mae": float(np.mean(np.abs(total - bt["sim_total"]))) if model else np.nan,
        })
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
    reg = bt[bt["game_type"] == "R"]
    nine = bt[bt["sched_innings"] == 9]
    lines = nine["home_line"].fillna("").str.split()
    batted = lines.map(lambda s: len(s) > 0 and s[-1] != "x")
    walkoff = batted & (nine["home_score"] > nine["away_score"]) & (lines.map(len) >= 9)
    margin = (bt["home_score"] - bt["away_score"]).abs()
    return {
        "calibration": calib,
        "range_coverage": float(np.mean(inside)),
        "headline_exact": float(np.mean((bt["headline_home"] == bt["home_score"])
                                        & (bt["headline_away"] == bt["away_score"]))),
        "extra_predicted": float(reg["extra_prob"].mean()),
        "extra_actual": float((reg["innings"] > reg["sched_innings"]).mean()),
        "one_run_predicted": float(bt["one_run_prob"].mean()), "one_run_actual": float(np.mean(margin == 1)),
        "shutout_predicted": float(np.mean(np.concatenate([bt["home_shutout_prob"], bt["away_shutout_prob"]]))),
        "shutout_actual": float(np.mean(np.concatenate([bt["away_score"] == 0, bt["home_score"] == 0]))),
        "skip_predicted": float(nine["skip_bottom_prob"].mean()), "skip_actual": float((~batted).mean()),
        "walkoff_predicted": float(nine["walkoff_prob"].mean()), "walkoff_actual": float(walkoff.mean()),
        "home_cover_predicted": float(bt["home_cover_prob"].mean()),
        "home_cover_actual": float(np.mean(bt["home_score"] - bt["away_score"] >= 2)),
        "rps_sim": float(0.5 * (bt["rps_home"] + bt["rps_away"]).mean()),
        "rps_poisson": float(bt["poisson_rps"].mean()), "rps_nbinom": float(bt["nbinom_rps"].mean()),
        "total_predicted": float(bt["sim_total"].mean()),
        "total_actual": float((bt["home_score"] + bt["away_score"]).mean()),
    }


def paired_bootstrap(loss_a, loss_b, n: int = 5000, seed: int = 0) -> tuple:
    """Mean of (a - b) and its 95% interval over resampled games."""
    rng = np.random.default_rng(seed)
    diff = np.asarray(loss_a) - np.asarray(loss_b)
    means = np.array([diff[rng.integers(0, len(diff), len(diff))].mean() for _ in range(n)])
    return float(diff.mean()), float(np.percentile(means, 2.5)), float(np.percentile(means, 97.5))


def load_pinnacle() -> pd.DataFrame:
    if not PINNACLE_PATH.exists():
        return pd.DataFrame()
    return pd.read_csv(PINNACLE_PATH, dtype={"game_id": str})


def market_comparison(bt: pd.DataFrame, feats: pd.DataFrame, fb: FeatureBuilder, window: int,
                      n_sims: int = 2000) -> dict | None:
    """The model next to Pinnacle's 2016 closing (and opening) lines, and blended with them."""
    lines = load_pinnacle()
    if lines.empty or not (bt["season"] == 2016).any():
        return None
    test = bt[bt["season"] == 2016].merge(lines, on="game_id", how="inner", suffixes=("", "_line"))
    if test.empty:
        return None
    train = feats[feats["season"].between(2016 - window, 2015) & feats["completed"]]
    model = RunModel.fit(train, fb.chain(2016))
    test = test.reset_index(drop=True)
    own = model.expected_runs(test)
    inv = MarketInverter(model.sim, np.exp(np.asarray(model.inning)), ghost=False)
    market = inv.rates(test)
    first8 = lambda side: test[f"{side}_line"].fillna("").str.split().map(
        lambda s: sum(int(v) for v in s[:8] if v != "x"))
    raw, _, n = fit_blend(own["home"], own["away"], market["market_home_runs"], market["market_away_runs"],
                          first8("home"), first8("away"), prior_games=0.0)
    home = blend(own["home"], market["market_home_runs"], raw)
    away = blend(own["away"], market["market_away_runs"], raw)
    blended, _ = model.predict(test, home / own["home"], away / own["away"], n_sims=n_sims, seed=7)
    y = outcome(test)
    p_close = devig(test["home_moneyline"], test["away_moneyline"])
    p_open = devig(test["open_home_moneyline"], test["open_away_moneyline"])
    losses = {"model": _log_loss(test["home_win_prob"], y), "close": _log_loss(p_close, y),
              "open": _log_loss(p_open, y), "blend": _log_loss(blended["home_win_prob"], y),
              "elo": _log_loss(test["elo_home_prob"], y)}
    total = test["home_score"] + test["away_score"]
    has_total = test["total_line"].notna()
    return {
        "games": len(test), "weight": raw, "losses": losses,
        "brier": {"model": float(np.mean((test["home_win_prob"] - y) ** 2)),
                  "close": float(np.mean((p_close - y) ** 2)),
                  "blend": float(np.mean((blended["home_win_prob"] - y) ** 2))},
        "total_mae": {"model": float(np.mean(np.abs(total - test["sim_total"]))),
                      "close": float(np.mean(np.abs(total - test["total_line"])[has_total])),
                      "blend": float(np.mean(np.abs(total - blended["sim_total"])))},
        "bootstrap": {"Model vs closing line": paired_bootstrap(losses["model"], losses["close"]),
                      "Blend vs closing line": paired_bootstrap(losses["blend"], losses["close"]),
                      "Model vs opening line": paired_bootstrap(losses["model"], losses["open"])},
    }


def lineup_comparison(fb: FeatureBuilder, feats: pd.DataFrame, seasons, window: int, n_sims: int) -> dict:
    """Known lineups against lineups projected from earlier games, on the same games."""
    games = fb.games[fb.games["season"].isin(list(seasons)) & fb.games["completed"]]
    blind = fb.build(games, known_lineups=False)
    known_rows, blind_rows = [], []
    for season in seasons:
        train = feats[feats["season"].between(season - window, season - 1) & feats["completed"]]
        model = RunModel.fit(train, fb.chain(season))
        for frame, rows in ((feats, known_rows), (blind, blind_rows)):
            test = frame[(frame["season"] == season) & frame["completed"]].reset_index(drop=True)
            pred, _ = model.predict(test, n_sims=n_sims, seed=season)
            rows.append(pd.DataFrame({"game_id": test["game_id"], "p": pred["home_win_prob"], "y": outcome(test)}))
    k = pd.concat(known_rows).set_index("game_id")
    b = pd.concat(blind_rows).set_index("game_id").reindex(k.index)
    lk, lb = _log_loss(k["p"], k["y"]), _log_loss(b["p"], k["y"])
    return {"games": len(k), "known": float(lk.mean()), "projected": float(lb.mean()),
            "bootstrap": paired_bootstrap(lb, lk)}
