"""Walk-forward backtest, scored on probabilities against simple baselines.

Each game is predicted from ratings built on earlier days of its season plus
the preseason prior, and the goal-rate model and simulator are fitted only on
the seasons before it. Nothing from the season being scored leaks in except
the actual starting goalies (a game-day run knows them once they are
confirmed; a separate pass projects them instead, as a morning run would).

The market benchmark is sportsbookreview's archive of opening and closing
moneylines, closing puck lines and totals (2011-12 to 2021-22, matched to the
games by date, teams and final score). The weight on the model in the blend
is fitted, for each season, on the archive's earlier seasons only, and the
betting edges are priced as on the live page: the final prediction's chances
anchored to the market, at the archive's prices (totals, whose prices it does
not record usably, at -110), Kelly-staked. The model alone is priced the same
way for comparison.
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

from bettingcore import sbr, summarize

from .config import CACHE_DIR, Hyperparams
from .edges import add_edges, graded, puck_line
from .features import FeatureBuilder
from .market import EDGE_PROBS, MarketInverter, devig, edge_chances, fit_blend
from .model import GoalModel, team_view
from .simulate import line_probs

log = logging.getLogger(__name__)

BASELINE_FEATURES = ["goals_off", "goals_def", "home"]
MAX_GOALS = 15
# sportsbookreview's team names, mapped to this predictor's codes.
SBR_NAMES = {
    "Ducks": "ANA", "Bruins": "BOS", "Sabres": "BUF", "Hurricanes": "CAR", "Blue Jackets": "CBJ",
    "Flames": "CGY", "Blackhawks": "CHI", "Avalanche": "COL", "Stars": "DAL", "Red Wings": "DET",
    "Oilers": "EDM", "Panthers": "FLA", "Kings": "LAK", "Wild": "MIN", "Canadiens": "MTL", "Devils": "NJD",
    "Predators": "NSH", "Islanders": "NYI", "NY Islanders": "NYI", "Rangers": "NYR", "Senators": "OTT",
    "Flyers": "PHI", "Penguins": "PIT", "Sharks": "SJS", "St.Louis": "STL", "Lightning": "TBL",
    "Tampa Bay": "TBL", "Tampa": "TBL", "Maple Leafs": "TOR", "Canucks": "VAN", "Jets": "WPG",
    "WinnipegJets": "WPG", "Capitals": "WSH", "Coyotes": "UTA", "Phoenix": "UTA", "Arizonas": "UTA",
    "Golden Knights": "VGK", "SeattleKraken": "SEA", "Kraken": "SEA",
}


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


# ---- the betting market ---------------------------------------------------

def archive_lines(games: pd.DataFrame, max_age_hours: float = 24.0 * 30) -> pd.DataFrame:
    """Archived lines for ``games``, indexed by ``game_id``, in the live log's column names."""
    try:
        archive = sbr.load_archive("nhl", CACHE_DIR, max_age_hours)
    except Exception as exc:                       # the backtest still runs without the market section
        log.warning("Line archive unavailable: %s", exc)
        return pd.DataFrame()
    m = sbr.match(archive, games.assign(date=games["start"]), SBR_NAMES, date="date")
    priced = m["home_close_spread_odds"].notna() & m["away_close_spread_odds"].notna()
    return pd.DataFrame({
        "home_moneyline": m["home_close_ml"], "away_moneyline": m["away_close_ml"],
        "open_home_moneyline": m["home_open_ml"], "open_away_moneyline": m["away_open_ml"],
        "home_spread_line": m["home_close_spread"].where(priced),
        "home_spread_price": m["home_close_spread_odds"].where(priced),
        "away_spread_price": m["away_close_spread_odds"].where(priced),
        "total_line": m["close_total"], "open_total_line": m["open_total"],
    }, index=m.index)


def market_rates(features: pd.DataFrame, states: pd.DataFrame, lines: pd.DataFrame, seasons, window: int,
                 n_sims: int = 2000) -> pd.DataFrame:
    """For every game with an archived line: the model's own goal rates (out of sample, from a
    model fitted on the seasons before) and the rates backed out of the closing and the opening
    line, with the regulation goals the blend weight is fitted on."""
    out = []
    for season in seasons:
        train = features[(features["season"] >= season - window) & (features["season"] < season)]
        test = features[(features["season"] == season) & features["completed"]
                        & features["game_id"].isin(lines.index)].reset_index(drop=True)
        if test.empty or train.empty:
            continue
        model = GoalModel.fit(train, states[states["season"] < season])
        own = model.rates(test)
        inv = MarketInverter(model.sim, n_sims=n_sims)
        lt = lines.reindex(test["game_id"]).reset_index(drop=True)
        close = inv.rates(lt.assign(over_price=np.nan, under_price=np.nan))
        opened = inv.rates(lt.assign(home_moneyline=lt["open_home_moneyline"],
                                     away_moneyline=lt["open_away_moneyline"], total_line=lt["open_total_line"],
                                     over_price=np.nan, under_price=np.nan))
        out.append(pd.DataFrame({
            "game_id": test["game_id"], "season": season, "model_home_rate": own["home"],
            "model_away_rate": own["away"], "market_home_rate": close["market_home_rate"].to_numpy(),
            "market_away_rate": close["market_away_rate"].to_numpy(),
            "open_market_home_rate": opened["market_home_rate"].to_numpy(),
            "open_market_away_rate": opened["market_away_rate"].to_numpy(),
            "home_reg": test["home_reg"].to_numpy(float), "away_reg": test["away_reg"].to_numpy(float)}))
        log.info("Market rates for %s: %d games", season, len(test))
    return pd.concat(out, ignore_index=True) if out else pd.DataFrame()


def walk_forward_weights(rates: pd.DataFrame, seasons) -> dict[int, tuple[float, int]]:
    """For each season, the blend weight fitted (no prior) on the archive's earlier seasons."""
    out = {}
    for season in seasons:
        past = rates[rates["season"] < season]
        out[season] = fit_blend(past["model_home_rate"], past["model_away_rate"], past["market_home_rate"],
                                past["market_away_rate"], past["home_reg"], past["away_reg"], prior_games=0.0)
    return out


def market_backtest(features: pd.DataFrame, states: pd.DataFrame, lines: pd.DataFrame, rates: pd.DataFrame,
                    seasons, window: int, n_sims: int = 2000) -> dict:
    """The model next to the archived market on the backtest's seasons with lines: log loss of
    the model, the closing line and the walk-forward blend, and the betting edges of the final
    prediction and of the model alone at the closing and the opening lines."""
    weights = walk_forward_weights(rates, seasons)
    rows = []
    for season in seasons:
        train = features[(features["season"] >= season - window) & (features["season"] < season)]
        test = features[(features["season"] == season) & features["completed"]
                        & features["game_id"].isin(lines.index)].reset_index(drop=True)
        if test.empty or train.empty or not weights[season][1]:
            continue
        w = weights[season][0]
        model = GoalModel.fit(train, states[states["season"] < season])
        r = rates.set_index("game_id").reindex(test["game_id"])
        lt = lines.reindex(test["game_id"]).reset_index(drop=True)
        base = test.drop(columns=[c for c in lt.columns if c in test]).join(lt).assign(
            home_goalie_status="known", away_goalie_status="known", over_price=np.nan, under_price=np.nan)
        own_pred, own_sim = model.predict(base, n_sims=n_sims, seed=season)
        for kind, prefix in (("closing", ""), ("opening", "open_")):
            frame = base if kind == "closing" else base.assign(
                home_moneyline=lt["open_home_moneyline"], away_moneyline=lt["open_away_moneyline"],
                total_line=lt["open_total_line"], home_spread_line=np.nan, home_spread_price=np.nan,
                away_spread_price=np.nan)
            mh, ma = r[f"{prefix}market_home_rate"].to_numpy(), r[f"{prefix}market_away_rate"].to_numpy()
            has = ~np.isnan(mh)
            home = np.where(has, w * r["model_home_rate"].to_numpy() + (1 - w) * mh, r["model_home_rate"])
            away = np.where(has, w * r["model_away_rate"].to_numpy() + (1 - w) * ma, r["model_away_rate"])
            pred, sim = model.predict(frame, home, away, n_sims=n_sims, seed=season)
            ref, ref_sim = model.predict(frame, np.where(has, mh, home), np.where(has, ma, away), n_sims=n_sims,
                                         seed=season)
            chances = edge_chances(frame, pred, sim, ref, ref_sim, frame["home_spread_line"])
            del ref_sim
            lines_home = [puck_line(hl, p) for hl, p in zip(frame["home_spread_line"], own_pred["home_win_prob"])]
            own_lines = line_probs(own_sim, lines_home, frame["total_line"])
            rows.append(frame.assign(kind=kind, weight=w, blend_home_prob=pred["home_win_prob"].to_numpy(),
                                     model_home_prob=own_pred["home_win_prob"].to_numpy(),
                                     **{c: chances[c].to_numpy() for c in EDGE_PROBS},
                                     **{c: own_lines[c].to_numpy() for c in own_lines}))
            del sim
        del own_sim
        log.info("Market backtest %s: %d games, weight %.2f", season, len(test), w)
    if not rows:
        return {}
    d = pd.concat(rows, ignore_index=True)
    close = d[d["kind"] == "closing"]
    y = outcome(close)
    p_close = devig(close["home_moneyline"], close["away_moneyline"])
    p_open = devig(close["open_home_moneyline"], close["open_away_moneyline"])
    losses = {"model": _log_loss(close["model_home_prob"], y), "close": _log_loss(p_close, y),
              "open": _log_loss(p_open, y), "blend": _log_loss(close["blend_home_prob"], y)}
    edges = {}
    for kind in ("closing", "opening"):
        frame = d[d["kind"] == kind]
        for rule in ("final", "model"):
            priced = add_edges(frame, chances=rule)
            for market in ("spread", "moneyline", "total"):
                if kind == "opening" and market == "spread":
                    continue
                edges[(kind, rule, market)] = summarize(graded(priced, market))
    seasons_used = sorted(close["season"].unique())
    return {"games": len(close), "seasons": (seasons_used[0], seasons_used[-1]), "losses": losses,
            "weights": {s: w for s, (w, _) in weights.items() if s in seasons_used},
            "edges": edges, "bootstrap": {
                "Model vs closing line": paired_bootstrap(losses["model"], losses["close"]),
                "Blend vs closing line": paired_bootstrap(losses["blend"], losses["close"]),
                "Model vs opening line": paired_bootstrap(losses["model"], losses["open"])}}
