"""Walk-forward backtest, scored on probabilities against baselines and the market.

Each game is predicted from ratings built on earlier days only (player and
team ratings, park factors from earlier seasons), and the run model and
simulator are fitted on the seasons before it. Lineups and starting
pitchers are the actual ones, which a game-day run knows once lineups post;
a second pass projects the lineups instead, as a morning run would. Weather
is the recorded game-time weather, a little better than a forecast.

Two market benchmarks. Pinnacle's complete 2016 line history, the sharpest
book's, is scored on the same games and blended with the model. And
sportsbookreview's archive (2011 to 2021: opening and closing moneylines,
closing run lines with their prices, opening and closing totals), matched to
the games by date, teams and final score, gives six seasons of the model next
to the market: the blend weight is fitted, for each season, on the archive's
earlier seasons only (fitted on all of it, it seeds the live predictor's), and
the betting edges are priced as on the live page, from the final prediction
anchored to the market, Kelly-staked, at the archive's prices (totals, whose
price it does not record usably, at -110). The model alone is priced the same
way for comparison.
"""

from __future__ import annotations

import logging

import numpy as np
import pandas as pd
from scipy.optimize import minimize
from scipy.stats import nbinom, poisson

from bettingcore import paired_bootstrap, sbr

from .config import CACHE_DIR, PINNACLE_PATH
from .edges import DEFAULT_RUN_LINE, add_edges, edge_record
from .features import FeatureBuilder
from .market import EDGE_PROBS, MarketInverter, blend, devig, edge_chances, fit_blend
from .model import RunModel
from .simulate import line_probs

log = logging.getLogger(__name__)

MAX_RUNS = 30
# sportsbookreview's team names, mapped to this predictor's codes.
SBR_NAMES = {
    "Diamondbacks": "ARI", "Athletics": "ATH", "Braves": "ATL", "Orioles": "BAL", "Red Sox": "BOS",
    "Cubs": "CHC", "CUB": "CHC", "Reds": "CIN", "Indians": "CLE", "Rockies": "COL", "White Sox": "CWS",
    "Tigers": "DET", "Astros": "HOU", "KAN": "KC", "Angels": "LAA", "Dodgers": "LAD", "LOS": "LAD",
    "Marlins": "MIA", "Brewers": "MIL", "Twins": "MIN", "Mets": "NYM", "Yankees": "NYY", "Phillies": "PHI",
    "Pirates": "PIT", "SDG": "SD", "Mariners": "SEA", "SFO": "SF", "Cardinals": "STL", "TAM": "TB",
    "Rangers": "TEX", "Blue Jays": "TOR", "Nationals": "WSH",
}


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


def load_pinnacle() -> pd.DataFrame:
    if not PINNACLE_PATH.exists():
        return pd.DataFrame()
    return pd.read_csv(PINNACLE_PATH, dtype={"game_id": str})


def market_comparison(bt: pd.DataFrame, feats: pd.DataFrame, fb: FeatureBuilder, window: int,
                      n_sims: int = 8000) -> dict | None:
    """The model next to Pinnacle's 2016 closing (and opening) lines, and blended with them.

    Uses more simulations than the rest of the backtest, so the blend is not
    graded on simulation noise."""
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


# ---- sportsbookreview's archive ---------------------------------------------

def archive_lines(games: pd.DataFrame, max_age_hours: float = 24.0 * 30) -> pd.DataFrame:
    """Archived lines for ``games``, indexed by ``game_id``, in the live log's column names."""
    try:
        archive = sbr.load_archive("mlb", CACHE_DIR, max_age_hours)
    except Exception as exc:                       # the backtest still runs without this section
        log.warning("Line archive unavailable: %s", exc)
        return pd.DataFrame()
    m = sbr.match(archive, games, SBR_NAMES, date="date")
    priced = m["home_close_spread_odds"].notna() & m["away_close_spread_odds"].notna() \
        & m["home_close_spread"].abs().eq(1.5)
    return pd.DataFrame({
        "home_moneyline": m["home_close_ml"], "away_moneyline": m["away_close_ml"],
        "open_home_moneyline": m["home_open_ml"], "open_away_moneyline": m["away_open_ml"],
        "home_run_line": m["home_close_spread"].where(priced),
        "home_run_line_price": m["home_close_spread_odds"].where(priced),
        "away_run_line_price": m["away_close_spread_odds"].where(priced),
        "total_line": m["close_total"], "open_total_line": m["open_total"],
    }, index=m.index)


def _market_runs(model: RunModel, *frames: pd.DataFrame) -> list[pd.DataFrame]:
    """Each game's run levels backed out of its moneyline and total (NaN without both), for
    each of ``frames``: the same games under different lines."""
    profile = np.exp(np.asarray(model.inning))
    outs = [pd.DataFrame(np.nan, index=f.index, columns=["market_home_runs", "market_away_runs"]) for f in frames]
    ghost_games = (frames[0]["tiebreaker"].fillna(0).astype(int) == 1).to_numpy()
    for ghost in (True, False):
        rows = ghost_games == ghost
        if not rows.any():
            continue
        inv = MarketInverter(model.sim, profile, ghost=ghost)
        for f, out in zip(frames, outs):
            out.loc[rows] = inv.rates(f[rows])[["market_home_runs", "market_away_runs"]].to_numpy()
    return outs


def _season_games(feats: pd.DataFrame, lines: pd.DataFrame, season: int, window: int):
    """Training games for ``season`` and its nine-inning games with an archived line."""
    train = feats[feats["season"].between(season - window, season - 1) & feats["completed"]]
    test = feats[(feats["season"] == season) & feats["completed"] & feats["game_id"].isin(lines.index)
                 & feats["sched_innings"].fillna(9).eq(9)].reset_index(drop=True)
    return train, test


def _blend_fit(rates: pd.DataFrame) -> tuple[float, int]:
    """Blend weight (no prior) on ``rates`` and the games behind it."""
    raw, _, n = fit_blend(rates["model_home_runs"], rates["model_away_runs"], rates["market_home_runs"],
                          rates["market_away_runs"], rates["home_r8"], rates["away_r8"], prior_games=0.0)
    return raw, n


def market_backtest(feats: pd.DataFrame, fb: FeatureBuilder, lines: pd.DataFrame, seasons, window: int,
                    start: int, n_sims: int = 2000) -> dict:
    """The model next to the archived market.

    For every season in ``seasons``, each game's run levels (the model's,
    out of sample, and the closing and opening lines', backed out through the
    simulator) are kept for fitting the blend weight. From ``start`` on, each
    season is also blended with the weight fitted on the earlier seasons only
    and scored: log loss of the model, the lines and the blend, and the
    betting edges of the final prediction and of the model alone at the
    closing and the opening lines. The weight fitted on every season is
    returned too; it seeds the live predictor's.
    """
    rates, rows, weights = [], [], {}
    for season in seasons:
        train, test = _season_games(feats, lines, season, window)
        if test.empty or train.empty:
            continue
        model = RunModel.fit(train, fb.chain(season))
        own = model.expected_runs(test)
        lt = lines.reindex(test["game_id"]).reset_index(drop=True)
        base = test.drop(columns=[c for c in lt.columns if c in test]).join(lt).assign(
            over_price=np.nan, under_price=np.nan)
        opening = base.assign(home_moneyline=lt["open_home_moneyline"], away_moneyline=lt["open_away_moneyline"],
                              total_line=lt["open_total_line"], home_run_line=np.nan, home_run_line_price=np.nan,
                              away_run_line_price=np.nan)
        markets = dict(zip(("closing", "opening"), _market_runs(model, base, opening)))
        past = pd.concat(rates) if rates else pd.DataFrame()
        rates.append(pd.DataFrame({
            "season": season, "model_home_runs": own["home"], "model_away_runs": own["away"],
            "market_home_runs": markets["closing"]["market_home_runs"].to_numpy(),
            "market_away_runs": markets["closing"]["market_away_runs"].to_numpy(),
            "home_r8": test["home_r8"].to_numpy(float), "away_r8": test["away_r8"].to_numpy(float)}))
        if season < start or past.empty:
            log.info("Market runs for %s: %d games", season, len(test))
            continue
        w, _ = _blend_fit(past)
        weights[season] = w
        own_pred, own_sim = model.predict(base, n_sims=n_sims, seed=season)
        for kind, frame in (("closing", base), ("opening", opening)):
            mh = markets[kind]["market_home_runs"].to_numpy()
            ma = markets[kind]["market_away_runs"].to_numpy()
            has = ~np.isnan(mh)
            home, away = blend(own["home"], mh, w), blend(own["away"], ma, w)
            pred, sim = model.predict(frame, home / own["home"], away / own["away"], n_sims=n_sims, seed=season)
            # The same simulation at the market's own run levels anchors the edges' chances.
            ref, ref_sim = model.predict(frame, np.where(has, mh, home) / own["home"],
                                         np.where(has, ma, away) / own["away"], n_sims=n_sims, seed=season)
            chances = edge_chances(frame, pred, sim, ref, ref_sim, frame["home_run_line"])
            del ref_sim, sim
            run_line = frame["home_run_line"].to_numpy(float)
            run_line = np.where(np.isnan(run_line), np.where(own_pred["home_win_prob"] >= 0.5, -DEFAULT_RUN_LINE,
                                                             DEFAULT_RUN_LINE), run_line)
            own_lines = line_probs(own_sim, run_line, frame["total_line"])
            rows.append(frame[["game_id", "season", "home_team", "away_team", "home_score", "away_score",
                               "home_moneyline", "away_moneyline", "home_run_line", "home_run_line_price",
                               "away_run_line_price", "total_line", "over_price", "under_price"]].assign(
                kind=kind, blend_home_prob=pred["home_win_prob"].to_numpy(),
                model_home_prob=own_pred["home_win_prob"].to_numpy(),
                **{c: chances[c].to_numpy() for c in EDGE_PROBS},
                **{c: own_lines[c].to_numpy() for c in own_lines}))
        del own_sim
        log.info("Market backtest %s: %d games, weight %.2f", season, len(test), w)
    if not rates:
        return {}
    all_weight, all_games = _blend_fit(pd.concat(rates))
    out = {"all_weight": all_weight, "all_games": all_games, "rate_seasons": (rates[0]["season"].iloc[0],
                                                                             rates[-1]["season"].iloc[0])}
    if not rows:
        return out
    d = pd.concat(rows, ignore_index=True)
    close, opened = d[d["kind"] == "closing"], d[d["kind"] == "opening"]
    y = outcome(close)
    p_close = devig(close["home_moneyline"], close["away_moneyline"])
    p_open = devig(opened["home_moneyline"], opened["away_moneyline"])
    ok = ~(np.isnan(p_close) | np.isnan(p_open))
    losses = {"model": _log_loss(close["model_home_prob"], y)[ok], "close": _log_loss(p_close, y)[ok],
              "open": _log_loss(p_open, y)[ok], "blend": _log_loss(close["blend_home_prob"], y)[ok]}
    edges = {}
    for kind, frame in (("closing", close), ("opening", opened)):
        for rule in ("final", "model"):
            priced = add_edges(frame, chances=rule)
            for market in ("spread", "moneyline", "total"):
                if not (kind == "opening" and market == "spread"):
                    edges[(kind, rule, market)] = edge_record(priced, market)
    used = sorted(int(x) for x in close["season"].unique())
    return {**out, "games": int(ok.sum()), "seasons": (used[0], used[-1]), "losses": losses, "weights": weights,
            "edges": edges,
            "bootstrap": {"Model vs closing line": paired_bootstrap(losses["model"], losses["close"]),
                          "Blend vs closing line": paired_bootstrap(losses["blend"], losses["close"]),
                          "Model vs opening line": paired_bootstrap(losses["model"], losses["open"])}}
