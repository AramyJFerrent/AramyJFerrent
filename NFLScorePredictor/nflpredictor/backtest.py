"""Walk-forward backtest, scored side by side with the closing line.

Week W of season S is predicted from ratings built on weeks 1 to W-1 plus the
preseason prior, and the points map, blend and simulator are fitted only on
the seasons before S. Nothing from the season being scored leaks in except the
closing lines and starting quarterbacks recorded in the schedule (see README).
"""

from __future__ import annotations

import itertools
import logging
from dataclasses import replace

import numpy as np
import pandas as pd
from scipy.stats import norm

from .config import CACHE_DIR, TEAM_ALIASES, Hyperparams
from .data import fetch
from .edges import edge_frame, edge_record, has_edge
from .features import FeatureBuilder
from .model import ScoreModel

# Westgate SuperContest lines: posted on Wednesday and never moved, 2013-2020.
MIDWEEK_LINES_URL = "https://raw.githubusercontent.com/nflverse/nfldata/master/data/sc_lines.csv"

log = logging.getLogger(__name__)


def moneyline_prob(home_ml: pd.Series, away_ml: pd.Series) -> pd.Series:
    """De-vigged home win probability from American moneylines."""
    def implied(ml):
        return np.where(ml < 0, -ml / (-ml + 100.0), 100.0 / (ml + 100.0))
    with np.errstate(divide="ignore", invalid="ignore"):
        h, a = implied(home_ml.to_numpy(float)), implied(away_ml.to_numpy(float))
        return pd.Series(h / (h + a), index=home_ml.index)


def predict_seasons(features: pd.DataFrame, seasons, window: int, n_sims: int = 4000) -> pd.DataFrame:
    """Out-of-sample predictions for every completed game in ``seasons``."""
    out = []
    for season in seasons:
        train = features[(features["season"] >= season - window) & (features["season"] < season)]
        test = features[(features["season"] == season) & features["completed"]].reset_index(drop=True)
        if test.empty or train.empty:
            continue
        model = ScoreModel.fit(train)
        pred = model.predict(test, n_sims=n_sims, seed=season)
        sd = float(np.std(
            (train.loc[train.completed, "home_score"] - train.loc[train.completed, "away_score"]).to_numpy()
            - model.model_means(train[train.completed])["margin"]))
        pred["model_home_prob"] = norm.cdf(pred["pred_model_margin"] / sd)
        out.append(pd.concat([test, pred.drop(columns="game_id")], axis=1))
        log.info("Backtested %s: %d games", season, len(test))
    return pd.concat(out, ignore_index=True)


def _win_metrics(prob: np.ndarray, outcome: np.ndarray) -> tuple[float, float]:
    p = np.clip(prob, 1e-4, 1 - 1e-4)
    brier = float(np.mean((p - outcome) ** 2))
    logloss = float(-np.mean(outcome * np.log(p) + (1 - outcome) * np.log(1 - p)))
    return brier, logloss


def score(bt: pd.DataFrame) -> pd.DataFrame:
    """Accuracy of the final prediction, its parts and the benchmarks on the same games."""
    bt = bt[bt["spread_line"].notna() & bt["total_line"].notna()]
    margin = (bt["home_score"] - bt["away_score"]).to_numpy()
    total = (bt["home_score"] + bt["away_score"]).to_numpy()
    outcome = np.where(margin > 0, 1.0, np.where(margin < 0, 0.0, 0.5))
    market_prob = moneyline_prob(bt["home_moneyline"], bt["away_moneyline"])
    market_prob = market_prob.fillna(pd.Series(norm.cdf(bt["spread_line"] / 12.7), index=bt.index))
    env_total = 2 * bt["env_points"].to_numpy()
    candidates = {
        "Final (model + market + sim)": (bt["pred_margin"], bt["pred_total"],
                                         bt["home_win_prob"] + 0.5 * bt["tie_prob"]),
        "Model only": (bt["pred_model_margin"], bt["pred_model_total"], bt["model_home_prob"]),
        "Elo baseline": (bt["elo_spread"], pd.Series(env_total, index=bt.index), bt["elo_home_prob"]),
        "Closing line": (bt["spread_line"], bt["total_line"], market_prob),
    }
    rows = []
    for name, (m, t, p) in candidates.items():
        m, t, p = (np.asarray(x, dtype=float) for x in (m, t, p))
        home, away = (t + m) / 2, (t - m) / 2
        team_err = np.concatenate([np.abs(bt["home_score"] - home), np.abs(bt["away_score"] - away)])
        brier, logloss = _win_metrics(p, outcome)
        picks = np.sign(m) == np.sign(margin)
        rows.append({
            "predictor": name,
            "games": len(bt),
            "margin_mae": np.mean(np.abs(margin - m)),
            "margin_rmse": np.sqrt(np.mean((margin - m) ** 2)),
            "total_mae": np.mean(np.abs(total - t)),
            "team_score_mae": np.mean(team_err),
            "brier": brier,
            "log_loss": logloss,
            "winner_pct": np.mean(picks[margin != 0]),
        })
    return pd.DataFrame(rows)


def distribution_checks(bt: pd.DataFrame) -> dict:
    """Calibration of win probabilities and 80% ranges, and key-number match."""
    margin = (bt["home_score"] - bt["away_score"]).to_numpy()
    p = (bt["home_win_prob"] + 0.5 * bt["tie_prob"]).to_numpy()
    outcome = np.where(margin > 0, 1.0, np.where(margin < 0, 0.0, 0.5))
    bins = np.linspace(0, 1, 11)
    which = np.clip(np.digitize(p, bins) - 1, 0, 9)
    calib = pd.DataFrame({"bin": which, "p": p, "won": outcome}).groupby("bin").agg(
        games=("p", "size"), predicted=("p", "mean"), actual=("won", "mean"))
    calib.index = [f"{int(bins[i] * 100)}-{int(bins[i + 1] * 100)}%" for i in calib.index]
    inside = np.concatenate([
        (bt["home_score"] >= bt["home_low"]) & (bt["home_score"] <= bt["home_high"]),
        (bt["away_score"] >= bt["away_low"]) & (bt["away_score"] <= bt["away_high"]),
    ])
    headline_exact = np.mean((bt["headline_home"] == bt["home_score"]) & (bt["headline_away"] == bt["away_score"]))
    return {
        "calibration": calib,
        "range_coverage": float(np.mean(inside)),
        "headline_exact": float(headline_exact),
        "one_score_predicted": float(bt["one_score_prob"].mean()),
        "one_score_actual": float(np.mean(np.abs(margin) <= 8)),
    }


def paired_bootstrap(errors_a: np.ndarray, errors_b: np.ndarray, n: int = 5000, seed: int = 0) -> tuple:
    """Mean of (a - b) and its 95% interval over resampled games."""
    rng = np.random.default_rng(seed)
    diff = np.asarray(errors_a) - np.asarray(errors_b)
    idx = rng.integers(0, len(diff), size=(n, len(diff)))
    means = diff[idx].mean(axis=1)
    return float(diff.mean()), float(np.percentile(means, 2.5)), float(np.percentile(means, 97.5))


def load_midweek_lines(games: pd.DataFrame, max_age_hours: float = 24.0) -> pd.Series:
    """Wednesday lines as expected home margins, indexed by game_id."""
    path = fetch(MIDWEEK_LINES_URL, CACHE_DIR / "sc_lines.csv", max_age_hours)
    sc = pd.read_csv(path).drop(columns=["home_team", "away_team"])
    sc["side"] = sc["side"].replace(TEAM_ALIASES)
    ids = games[["old_game_id", "game_id", "home_team"]].rename(columns={"game_id": "gid"})
    matched = sc.merge(ids, left_on="game_id", right_on="old_game_id")
    matched = matched[matched["side"] == matched["home_team"]]
    return pd.Series(-matched["line"].to_numpy(), index=matched["gid"].to_numpy(), name="midweek_line")


def without_starters(games: pd.DataFrame) -> pd.DataFrame:
    """Schedule with the recorded starting QBs removed, so each team is assumed to
    start whoever started its previous game: what is known by Wednesday."""
    games = games.copy()
    for col in ("home_qb_id", "away_qb_id", "home_qb_name", "away_qb_name"):
        games[col] = pd.Series([None] * len(games), index=games.index, dtype=object)
    return games


def model_only_probs(features: pd.DataFrame, seasons, window: int, n_sims: int = 4000) -> pd.DataFrame:
    """Out-of-sample model-only win, cover and over chances for finished games.

    Each season's model (points map, blend and simulator) is fitted on earlier
    seasons; the chances come from simulating its own expected points, before
    the market blend, against the closing lines and, where ``features`` has a
    ``midweek_line``, against the Wednesday line too.
    """
    out = []
    for season in seasons:
        train = features[(features["season"] >= season - window) & (features["season"] < season)]
        test = features[(features["season"] == season) & features["completed"]].reset_index(drop=True)
        if test.empty or train.empty:
            continue
        model = ScoreModel.fit(train)
        own = model.model_only_means(test)
        probs = model.model_only(test, n_sims=n_sims, seed=season)
        test = test.assign(model_margin=own["margin"], model_total=own["total"],
                           **{f"model_{c}": probs[c].to_numpy() for c in probs})
        if "midweek_line" in test:
            mid = model.model_only(test, n_sims=n_sims, seed=season, spread_line=test["midweek_line"])
            test["midweek_home_cover_prob"] = mid["home_cover_prob"].to_numpy()
            test["midweek_spread_push_prob"] = mid["spread_push_prob"].to_numpy()
        out.append(test)
        log.info("Model-only chances for %s: %d games", season, len(test))
    return pd.concat(out, ignore_index=True)


def closing_edges(df: pd.DataFrame) -> pd.DataFrame:
    """Edges in every market at the closing lines and the prices posted with them."""
    rows = df.rename(columns={"home_spread_odds": "home_spread_price", "away_spread_odds": "away_spread_price",
                              "over_odds": "over_price", "under_odds": "under_price"})
    return pd.concat([rows, edge_frame(rows)], axis=1)


def midweek_edges(df: pd.DataFrame) -> pd.DataFrame:
    """Spread edges at the Wednesday line. Those lines carry no prices, so -110 is assumed."""
    rows = df[df["midweek_line"].notna()].assign(
        closing_line=lambda d: d["spread_line"], spread_line=lambda d: d["midweek_line"],
        home_spread_price=np.nan, away_spread_price=np.nan,
        model_home_cover_prob=lambda d: d["midweek_home_cover_prob"],
        model_spread_push_prob=lambda d: d["midweek_spread_push_prob"])
    return pd.concat([rows, edge_frame(rows, markets=("spread",))], axis=1)


def edge_summary(df: pd.DataFrame, market: str, closing_col: str | None = None, n_boot: int = 5000,
                 seed: int = 0) -> dict:
    """Edge record in ``market`` with a 95% bootstrap range on ROI and, for spreads graded at an
    early line, how often the line then moved toward the edge by ``closing_col``."""
    rec = edge_record(df, market)
    units = rec.pop("unit_results")
    rec["roi_low"] = rec["roi_high"] = float("nan")
    if len(units):
        idx = np.random.default_rng(seed).integers(0, len(units), size=(n_boot, len(units)))
        rois = units[idx].mean(axis=1)
        rec["roi_low"], rec["roi_high"] = float(np.percentile(rois, 2.5)), float(np.percentile(rois, 97.5))
    if closing_col:
        picked = df[df[f"{market}_edge_pick"].map(has_edge)]
        move = picked[closing_col] - picked["spread_line"]
        sign = np.where(picked[f"{market}_edge_side"] == "home", 1.0, -1.0)
        moved = (move != 0).to_numpy()
        rec["moved_toward"] = float((np.sign(move.to_numpy()[moved]) == sign[moved]).mean()) \
            if moved.any() else float("nan")
        rec["moved_games"] = int(moved.sum())
    return rec


def tune(games, team_games, qbs, seasons, grid: dict, base: Hyperparams | None = None) -> pd.DataFrame:
    """Grid search over ratings hyperparameters, scored on model-only accuracy.

    Only the ratings engine is tuned; the points map and blend are refitted on
    prior seasons inside each fold, as in production.
    """
    base = base or Hyperparams()
    keys = list(grid)
    results = []
    first = min(seasons)
    for combo in itertools.product(*(grid[k] for k in keys)):
        hp = replace(base, **dict(zip(keys, combo)))
        fb = FeatureBuilder(games, team_games, qbs, hp)
        feats = fb.walk_forward(range(first - hp.fit_window_seasons, max(seasons) + 1))
        errs_m, errs_t = [], []
        for season in seasons:
            train = feats[(feats["season"] >= season - hp.fit_window_seasons) & (feats["season"] < season)]
            test = feats[(feats["season"] == season) & feats["completed"]]
            model = ScoreModel.fit(train, calibrate_scores=False)
            pred = model.model_means(test)
            errs_m.append(np.abs((test["home_score"] - test["away_score"]).to_numpy() - pred["margin"]))
            errs_t.append(np.abs((test["home_score"] + test["away_score"]).to_numpy() - pred["total"]))
        m, t = np.concatenate(errs_m).mean(), np.concatenate(errs_t).mean()
        results.append({**dict(zip(keys, combo)), "margin_mae": m, "total_mae": t, "objective": m + t})
        log.info("%s -> margin %.3f total %.3f", dict(zip(keys, combo)), m, t)
    return pd.DataFrame(results).sort_values("objective", ignore_index=True)
