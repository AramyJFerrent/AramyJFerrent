"""Walk-forward backtest, scored side by side with the closing line.

Week W of season S is predicted from ratings built on weeks 1 to W-1 plus the
preseason prior, and the prior regression, points map, blend and simulator
are fitted only on the seasons before S. Nothing from the season being scored
leaks in except the closing lines themselves (see README).

Every metric is reported by segment as well as overall, because a model can
match the market overall while being badly wrong in one kind of game.

Betting edges are scored the same way as live ones: the final prediction's
chances against each closing line, anchored to the market, at the books'
prices where the odds file has them and at a fractional Kelly stake (see
edges.py and lines.py). The same games are also priced against the opening
line (the odds file's median opener, no prices, so -110), and with the model's
own chances before the blend, the rule the predictor used before.
"""

from __future__ import annotations

import itertools
import logging
from dataclasses import replace

import numpy as np
import pandas as pd
from scipy.stats import norm

from bettingcore import valid_price

from .config import Hyperparams
from .edges import CHANCE_COLUMNS, MARKETS, STANDARD_MARKETS, edge_columns, edge_frame, edge_results, record
from .features import FeatureBuilder
from .model import EDGE_PROBS, ScoreModel

log = logging.getLogger(__name__)

# Power conferences by season (the Pac-12 counts until its 2024 breakup), plus
# Notre Dame.
POWER = {"SEC", "Big Ten", "Big 12", "ACC"}
PAC_12_LAST_POWER_SEASON = 2023
POWER_INDEPENDENTS = {"Notre Dame"}


def is_power(conference: pd.Series, team: pd.Series, season: pd.Series) -> pd.Series:
    pac = conference.eq("Pac-12") & (season <= PAC_12_LAST_POWER_SEASON)
    return conference.isin(POWER) | pac | team.isin(POWER_INDEPENDENTS)


def moneyline_prob(home_ml: pd.Series, away_ml: pd.Series) -> pd.Series:
    """De-vigged home win probability from American moneylines."""
    def implied(ml):
        return np.where(ml < 0, -ml / (-ml + 100.0), 100.0 / (ml + 100.0))
    with np.errstate(divide="ignore", invalid="ignore"):
        h, a = implied(home_ml.to_numpy(float)), implied(away_ml.to_numpy(float))
        return pd.Series(h / (h + a), index=home_ml.index)


# Edge rules: the final prediction's chances (live) and the model's own (the old rule).
EDGE_RULES = {"final": "", "model only": "model_"}
OPEN_PRICES = ["home_spread_price", "away_spread_price", "over_price", "under_price", "home_moneyline",
               "away_moneyline"]


def predict_seasons(features: pd.DataFrame, seasons, window: int, n_sims: int = 4000,
                    first_fit_season: int | None = None) -> pd.DataFrame:
    """Out-of-sample predictions for every completed game in ``seasons``.

    Each game is also predicted against its opening line (``spread_open`` and
    ``total_open``, unpriced), giving ``open_*`` chances for the edges at the
    opener; games without one get NaN there.
    """
    first = first_fit_season if first_fit_season is not None else int(features["season"].min())
    out = []
    for season in seasons:
        train = features[(features["season"] >= max(first, season - window)) & (features["season"] < season)]
        test = features[(features["season"] == season) & features["completed"]].reset_index(drop=True)
        if test.empty or train.empty:
            continue
        model = ScoreModel.fit(train)
        pred = model.predict(test, n_sims=n_sims, seed=season)
        if "spread_open" in test:
            # An opening line is posted days ahead, before the game's wind is known.
            opened = test.assign(spread_line=test["spread_open"], total_line=test["total_open"], wind=np.nan,
                                 **{c: np.nan for c in OPEN_PRICES})
            at_open = model.predict(opened, n_sims=n_sims, seed=season)
            for col in EDGE_PROBS + [c for c in at_open if c.startswith("model_")]:
                pred[f"open_{col}"] = at_open[col].to_numpy()
        done = train[train["completed"]]
        sd = float(np.std((done["home_score"] - done["away_score"]).to_numpy()
                          - model.model_means(done)["margin"]))
        pred["model_home_prob"] = norm.cdf(pred["pred_model_margin"] / sd)
        out.append(pd.concat([test, pred.drop(columns="game_id")], axis=1))
        log.info("Backtested %s: %d games", season, len(test))
    return pd.concat(out, ignore_index=True)


def segments(bt: pd.DataFrame) -> dict[str, pd.Series]:
    """Boolean masks for the kinds of games college models fail on differently."""
    fbs = bt["home_division"].eq("fbs") & bt["away_division"].eq("fbs")
    hp = is_power(bt["home_conference"], bt["home_team"], bt["season"])
    ap = is_power(bt["away_conference"], bt["away_team"], bt["season"])
    regular = bt["week"] < 17
    return {
        "FBS vs FBS": fbs,
        "FBS vs FCS": ~fbs,
        "Weeks 1-4": fbs & (bt["week"] <= 4),
        "Week 5 to end of regular season": fbs & (bt["week"] > 4) & regular,
        "Bowls and playoff": fbs & ~regular,
        "Power 4 vs Power 4": fbs & hp & ap,
        "Group of 5 vs Group of 5": fbs & ~hp & ~ap,
        "Power 4 vs Group of 5": fbs & (hp != ap),
        "Conference games": fbs & bt["conference_game"].astype(bool),
        "Nonconference games": fbs & ~bt["conference_game"].astype(bool),
    }


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
    outcome = np.where(margin > 0, 1.0, 0.0)
    market_prob = moneyline_prob(bt["home_moneyline"], bt["away_moneyline"])
    market_prob = market_prob.fillna(pd.Series(norm.cdf(bt["spread_line"] / 15.9), index=bt.index))
    env_total = 2 * bt["env_points"].to_numpy()
    candidates = {
        "Final (model + market + sim)": (bt["pred_margin"], bt["pred_total"], bt["home_win_prob"]),
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


def segment_table(bt: pd.DataFrame) -> pd.DataFrame:
    """Margin and total MAE of the model, the final prediction and the line, by segment."""
    lined = bt[bt["spread_line"].notna() & bt["total_line"].notna()]
    margin = lined["home_score"] - lined["away_score"]
    total = lined["home_score"] + lined["away_score"]
    rows = []
    for name, mask in segments(lined).items():
        if not mask.any():
            continue
        m, t = margin[mask], total[mask]
        rows.append({
            "Segment": name, "Games": int(mask.sum()),
            "Model margin": np.mean(np.abs(m - lined.loc[mask, "pred_model_margin"])),
            "Final margin": np.mean(np.abs(m - lined.loc[mask, "pred_margin"])),
            "Line margin": np.mean(np.abs(m - lined.loc[mask, "spread_line"])),
            "Elo margin": np.mean(np.abs(m - lined.loc[mask, "elo_spread"])),
            "Final total": np.mean(np.abs(t - lined.loc[mask, "pred_total"])),
            "Line total": np.mean(np.abs(t - lined.loc[mask, "total_line"])),
        })
    return pd.DataFrame(rows)


def distribution_checks(bt: pd.DataFrame) -> dict:
    """Calibration of win probabilities and 80% ranges, and key-number match."""
    margin = (bt["home_score"] - bt["away_score"]).to_numpy()
    p = bt["home_win_prob"].to_numpy()
    outcome = np.where(margin > 0, 1.0, 0.0)
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


def with_edges(bt: pd.DataFrame, prefix: str = "", at_open: bool = False) -> pd.DataFrame:
    """``bt`` with its ``{market}_edge_*`` columns rebuilt for one rule and kind of line.

    ``prefix`` picks the rule's chances ("" final, "model_" model only). At the
    opener, the opening spread and total stand in for the closing ones, with
    the chances priced against them and no prices (so -110 for spreads and
    totals, and no moneyline).
    """
    df = bt.drop(columns=[c for c in edge_columns() if c in bt])
    if at_open:
        chances = {c: f"open_{prefix}{c}" for c in [*CHANCE_COLUMNS.values(), "home_win_prob"]
                   if f"open_{prefix}{c}" in df}
        df = df.assign(spread_line=df["spread_open"], total_line=df["total_open"],
                       **{c: np.nan for c in OPEN_PRICES}, **{f"{prefix}{c}": df[v] for c, v in chances.items()})
    return pd.concat([df, edge_frame(df, prefix)], axis=1)


def _summary_row(games: pd.DataFrame, market: str, n_boot: int, **labels) -> dict:
    res = edge_results(games, market)
    span = f"{int(games['season'].min())}–{int(games['season'].max())}" if len(games) else ""
    return {**labels, "market": market, "span": span, "games": int(len(games)), **record(res, n_boot)}


def edge_record(bt: pd.DataFrame, n_boot: int = 2000) -> list[dict]:
    """Walk-forward betting edges by rule, kind of line, market and kind of price.

    ``bt`` holds out-of-sample predictions (``predict_seasons``), the closing
    and opening lines, the closing prices and final scores. Each row of the
    result is one rule ("final" or "model only"), line ("closing" or
    "opening"), market and kind of price ("posted" or "assumed -110"), with
    the games that had one and the record of the edges among them (Kelly
    stakes; ROI with a 95% bootstrap range over games, and expected ROI).
    """
    out = []
    for rule, prefix in EDGE_RULES.items():
        df = with_edges(bt, prefix)
        posted = {
            "spread": df["home_spread_price"].map(valid_price) & df["away_spread_price"].map(valid_price),
            "total": df["over_price"].map(valid_price) & df["under_price"].map(valid_price),
            "moneyline": df["home_moneyline"].map(valid_price) | df["away_moneyline"].map(valid_price),
        }
        has_line = {"spread": df["spread_line"].notna(), "total": df["total_line"].notna(),
                    "moneyline": posted["moneyline"]}
        for market in MARKETS:
            groups = [("posted", has_line[market] & posted[market])]
            if market in STANDARD_MARKETS:
                groups.append(("assumed -110", has_line[market] & ~posted[market]))
            for prices, mask in groups:
                if prices != "posted" and not mask.any():
                    continue
                out.append(_summary_row(df[mask], market, n_boot, chances=rule, lines="closing", prices=prices))
        if "spread_open" in bt:
            op = with_edges(bt, prefix, at_open=True)
            for market in STANDARD_MARKETS & set(MARKETS):
                line = op["spread_line" if market == "spread" else "total_line"]
                out.append(_summary_row(op[line.notna()], market, n_boot, chances=rule, lines="opening",
                                        prices="assumed -110"))
    order = {m: i for i, m in enumerate(MARKETS)}
    return sorted(out, key=lambda r: (r["chances"] != "final", r["lines"] != "closing", order[r["market"]]))


def segment_edges(bt: pd.DataFrame, n_boot: int = 2000) -> pd.DataFrame:
    """Edges of the final prediction by kind of game, against closing and opening lines.

    One row per segment and kind of line with each market's bets, ROI and its
    95% range: where the market is softest (early season, Group of 5, FCS
    opponents, bowls), edges should show up there first.
    """
    frames = {"closing": with_edges(bt)}
    if "spread_open" in bt:
        frames["opening"] = with_edges(bt, at_open=True)
    rows = []
    for name, mask in segments(bt).items():
        for lines, df in frames.items():
            row = {"Segment": name, "Lines": lines, "Games": int(mask.sum())}
            for market in MARKETS:
                if lines == "opening" and market == "moneyline":
                    continue
                rec = record(edge_results(df[mask.to_numpy()], market), n_boot)
                row[market] = rec
            rows.append(row)
    return pd.DataFrame(rows)


def tune(games, team_games, returning, lines, venues, seasons, grid: dict,
         base: Hyperparams | None = None, first_fit_season: int = 2015) -> pd.DataFrame:
    """Grid search over ratings hyperparameters, scored on model-only accuracy.

    Only the ratings engine is tuned; the prior regression, points map and blend
    are refitted on prior seasons inside each fold, as in production. Scored on
    FBS-vs-FBS games with a closing line.
    """
    base = base or Hyperparams()
    keys = list(grid)
    results = []
    for combo in itertools.product(*(grid[k] for k in keys)):
        hp = replace(base, **dict(zip(keys, combo)))
        fb = FeatureBuilder(games, team_games, returning, lines, venues, hp)
        feats = fb.walk_forward(range(first_fit_season, max(seasons) + 1))
        errs_m, errs_t = [], []
        for season in seasons:
            train = feats[(feats["season"] >= max(first_fit_season, season - hp.fit_window_seasons))
                          & (feats["season"] < season)]
            test = feats[(feats["season"] == season) & feats["completed"] & feats["spread_line"].notna()
                         & feats["home_division"].eq("fbs") & feats["away_division"].eq("fbs")]
            pred = ScoreModel.fit(train, calibrate_scores=False).model_means(test)
            errs_m.append(np.abs((test["home_score"] - test["away_score"]).to_numpy() - pred["margin"]))
            errs_t.append(np.abs((test["home_score"] + test["away_score"]).to_numpy() - pred["total"]))
        m, t = np.concatenate(errs_m).mean(), np.concatenate(errs_t).mean()
        results.append({**dict(zip(keys, combo)), "margin_mae": m, "total_mae": t, "objective": m + t})
        log.info("%s -> margin %.3f total %.3f", dict(zip(keys, combo)), m, t)
    return pd.DataFrame(results).sort_values("objective", ignore_index=True)
