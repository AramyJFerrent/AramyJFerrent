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

from bettingcore import fetch, sbr

from .config import CACHE_DIR, TEAM_ALIASES, Hyperparams
from .edges import edge_frame, edge_record, has_edge
from .features import FeatureBuilder
from .model import FINAL_LINE_PROBS, ScoreModel

# Westgate SuperContest lines: posted on Wednesday and never moved, 2013-2020.
MIDWEEK_LINES_URL = "https://raw.githubusercontent.com/nflverse/nfldata/master/data/sc_lines.csv"
# sportsbookreview's archive names (nicknames, and city names in some seasons), mapped to nflverse codes.
# "LosAngeles" and "NewYork" could be either of two teams, so their few games go unmatched.
SBR_NAMES = {
    "Bears": "CHI", "Bengals": "CIN", "Bills": "BUF", "BuffaloBills": "BUF", "Broncos": "DEN", "Browns": "CLE",
    "Buccaneers": "TB", "Tampa": "TB", "Cardinals": "ARI", "Chargers": "LAC", "SanDiego": "LAC", "Chiefs": "KC",
    "KCChiefs": "KC", "Kansas": "KC", "Colts": "IND", "Commanders": "WAS", "Washingtom": "WAS", "Cowboys": "DAL",
    "Dolphins": "MIA", "Eagles": "PHI", "Falcons": "ATL", "Fortyniners": "SF", "Giants": "NYG", "Jaguars": "JAX",
    "Jets": "NYJ", "Lions": "DET", "Oakland": "LV", "Raiders": "LV", "LVRaiders": "LV", "Packers": "GB",
    "Panthers": "CAR", "Patriots": "NE", "Rams": "LA", "St.Louis": "LA", "Ravens": "BAL", "Saints": "NO",
    "Seahawks": "SEA", "Steelers": "PIT", "Texans": "HOU", "Titans": "TEN", "Vikings": "MIN",
}
# Lines posted before the closing line that the backtest also bets into: each one's spread column (an
# expected home margin, like ``spread_line``) and total column, if it has totals. None carries prices.
EARLY_LINES = {"midweek": ("midweek_line", None), "open": ("open_line", "open_total")}

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


def load_midweek_lines(games: pd.DataFrame, max_age_hours: float = 24.0) -> pd.Series:
    """Wednesday lines as expected home margins, indexed by game_id."""
    path = fetch(MIDWEEK_LINES_URL, CACHE_DIR / "sc_lines.csv", max_age_hours)
    sc = pd.read_csv(path).drop(columns=["home_team", "away_team"])
    sc["side"] = sc["side"].replace(TEAM_ALIASES)
    ids = games[["old_game_id", "game_id", "home_team"]].rename(columns={"game_id": "gid"})
    matched = sc.merge(ids, left_on="game_id", right_on="old_game_id")
    matched = matched[matched["side"] == matched["home_team"]]
    return pd.Series(-matched["line"].to_numpy(), index=matched["gid"].to_numpy(), name="midweek_line")


def load_opening_lines(games: pd.DataFrame, max_age_hours: float = 24.0 * 30) -> pd.DataFrame:
    """Opening spreads (as expected home margins) and totals from sportsbookreview's archive
    (2011-2021), indexed by game_id.

    Some archived openers have the wrong sign (most of 2021's week 10, for one),
    so an opening spread more than 7 points from the closing one, or on the other
    side of zero by 4 or more, is dropped (under 1% of games, a few of them real
    moves on quarterback news); so is an opening total outside 25-70 points or
    more than 10 from the closing one.
    """
    try:
        archive = sbr.load_archive("nfl", CACHE_DIR, max_age_hours)
    except Exception as exc:                        # the backtest still runs without these rows
        log.warning("Line archive unavailable: %s", exc)
        return pd.DataFrame(columns=["open_line", "open_total"])
    m = sbr.match(archive, games, SBR_NAMES, date="gameday")
    close = games.set_index("game_id").reindex(m.index)
    line, total = -m["home_open_spread"], m["open_total"]
    gap = (line - close["spread_line"]).abs()
    bad_line = (gap > 7) | ((np.sign(line) * np.sign(close["spread_line"]) < 0) & (gap >= 4))
    bad_total = ~total.between(25, 70) | ((total - close["total_line"]).abs() > 10)
    return pd.DataFrame({"open_line": line.mask(bad_line), "open_total": total.mask(bad_total)})


def without_starters(games: pd.DataFrame) -> pd.DataFrame:
    """Schedule with the recorded starting QBs removed, so each team is assumed to
    start whoever started its previous game: what is known by Wednesday."""
    games = games.copy()
    for col in ("home_qb_id", "away_qb_id", "home_qb_name", "away_qb_name"):
        games[col] = pd.Series([None] * len(games), index=games.index, dtype=object)
    return games


# Chances each edge rule prices bets with: the final prediction's, or the model's own before the blend.
CHANCES = {"final": "", "model": "model_"}


def edge_probs(features: pd.DataFrame, seasons, window: int, n_sims: int = 4000) -> pd.DataFrame:
    """Out-of-sample win, cover and over chances for finished games, final and model-only.

    Each season's model (points map, blend and simulator) is fitted on earlier
    seasons. Against the closing lines the final prediction is the live one.
    For each early line (``EARLY_LINES``) in ``features``, the same game is
    predicted again with that line in place of the closing spread and total
    (no total where the source has none) and without the game's measured wind,
    which a line posted days ahead could not know, giving ``midweek_*`` and
    ``open_*`` chances; those lines carry no prices, so they count as even
    -110 markets.
    """
    out = []
    for season in seasons:
        train = features[(features["season"] >= season - window) & (features["season"] < season)]
        test = features[(features["season"] == season) & features["completed"]].reset_index(drop=True)
        if test.empty or train.empty:
            continue
        model = ScoreModel.fit(train)
        pred = model.predict(test, n_sims=n_sims, seed=season)
        keep = FINAL_LINE_PROBS + ["home_win_prob", "away_win_prob", "tie_prob"]
        test = test.assign(model_margin=pred["pred_model_margin"], model_total=pred["pred_model_total"],
                           **{c: pred[c].to_numpy() for c in keep},
                           **{c: pred[c].to_numpy() for c in pred if c.startswith("model_")})
        for early, (line_col, total_col) in EARLY_LINES.items():
            if line_col not in test:
                continue
            # An early line comes days before kickoff, before the game's wind is known.
            pred = model.predict(test.assign(spread_line=test[line_col],
                                             total_line=test[total_col] if total_col else np.nan,
                                             home_spread_odds=np.nan, away_spread_odds=np.nan, over_odds=np.nan,
                                             under_odds=np.nan, wind=np.nan), n_sims=n_sims, seed=season)
            for prefix in CHANCES.values():
                for c in ("home_cover_prob", "spread_push_prob", "over_prob", "total_push_prob"):
                    test[f"{early}_{prefix}{c}"] = pred[f"{prefix}{c}"].to_numpy()
        out.append(test)
        log.info("Edge chances for %s: %d games", season, len(test))
    return pd.concat(out, ignore_index=True)


def _with_chances(df: pd.DataFrame, chances: str) -> pd.DataFrame:
    """``df`` with the chosen rule's chances in the columns the edges read."""
    if chances == "final":
        return df
    cols = ["home_cover_prob", "spread_push_prob", "over_prob", "total_push_prob", "tie_prob"]
    return df.assign(**{c: df[f"model_{c}"] for c in cols}, home_ml_prob=df["model_home_win_prob"],
                     away_ml_prob=df["model_away_win_prob"])


def closing_edges(df: pd.DataFrame, chances: str = "final") -> pd.DataFrame:
    """Edges in every market at the closing lines and the prices posted with them."""
    rows = _with_chances(df, chances).rename(columns={
        "home_spread_odds": "home_spread_price", "away_spread_odds": "away_spread_price",
        "over_odds": "over_price", "under_odds": "under_price"})
    return pd.concat([rows, edge_frame(rows)], axis=1)


def early_edges(df: pd.DataFrame, early: str = "midweek", chances: str = "final") -> pd.DataFrame:
    """Edges at an early line (``EARLY_LINES``): the spread, and the total where the source has
    one. Those lines carry no prices, so -110 is assumed; the closing lines are kept as
    ``closing_line`` and ``closing_total``."""
    line_col, total_col = EARLY_LINES[early]
    p = f"{early}_{CHANCES[chances]}"
    markets = ("spread", "total") if total_col else ("spread",)
    chance_cols = ["home_cover_prob", "spread_push_prob"] + (["over_prob", "total_push_prob"] if total_col else [])
    rows = df[df[line_col].notna()].assign(
        closing_line=lambda d: d["spread_line"], closing_total=lambda d: d["total_line"],
        spread_line=lambda d: d[line_col], total_line=lambda d: d[total_col] if total_col else np.nan,
        home_spread_price=np.nan, away_spread_price=np.nan, over_price=np.nan, under_price=np.nan,
        **{c: (lambda d, c=c: d[p + c]) for c in chance_cols})
    return pd.concat([rows, edge_frame(rows, markets=markets)], axis=1)


def edge_summary(df: pd.DataFrame, market: str, closing_col: str | None = None, n_boot: int = 5000,
                 seed: int = 0) -> dict:
    """Edge record in ``market`` (Kelly stakes, ROI with a 95% bootstrap range over games) and,
    for edges graded at an early line, how often the line then moved toward the edge by
    ``closing_col`` (a spread toward the side picked, a total toward over or under)."""
    rec = edge_record(df, market, n_boot=n_boot, seed=seed)
    if closing_col:
        picked = df[df[f"{market}_edge_pick"].map(has_edge)]
        move = picked[closing_col] - picked["total_line" if market == "total" else "spread_line"]
        sign = np.where(picked[f"{market}_edge_side"].isin(["home", "over"]), 1.0, -1.0)
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
