"""Walk-forward backtest, scored side by side with the betting market.

Every bout in year Y is predicted from features built on earlier fights only,
with the win model, calibration, market blend, method and round models fitted
on the ``fit_window_years`` before Y. Benchmarks are scored on the same fights:
the de-vigged moneyline, Glicko-2 alone and a UFC-only Elo.
"""

from __future__ import annotations

import itertools
import logging
from dataclasses import replace

import numpy as np
import pandas as pd

from .config import FIRST_TRAIN_YEAR, VALUE_EDGE, Hyperparams
from .features import FeatureBuilder
from .model import METHODS, FightModel, RoundModel, WinModel, decided, division_method_rates
from .odds import decimal, devig, devig_methods, implied_prob

log = logging.getLogger(__name__)

SIX = [f"{s}_{m}" for s in "ab" for m in METHODS]


def predict_years(feats: pd.DataFrame, years, window: int, ridge: float,
                  features: list | None = None) -> pd.DataFrame:
    """Out-of-sample predictions for every bout in ``years``."""
    out = []
    year = feats["date"].dt.year
    for y in years:
        train = feats[(year >= max(y - window, FIRST_TRAIN_YEAR)) & (year < y)]
        test = feats[year == y].reset_index(drop=True)
        if test.empty or train.empty:
            continue
        model = FightModel.fit(train, ridge, features)
        pred = model.predict(test)
        base = baseline(train, test)
        out.append(pd.concat([test, pred, base], axis=1))
        log.info("Backtested %s: %d bouts (market weight %.2f, slope %.2f)", y, len(test),
                 model.calibration.market_weight,
                 model.calibration.blend_model + model.calibration.blend_market)
    return pd.concat(out, ignore_index=True)


def baseline(train: pd.DataFrame, test: pd.DataFrame) -> pd.DataFrame:
    """Division base rates for method and round, given the market (or Glicko) win chance."""
    rates = division_method_rates(decided(train))
    p = devig(test["odds_a"], test["odds_b"]) if "odds_a" in test else np.full(len(test), np.nan)
    p = np.where(np.isnan(p), test["glicko_prob"], p)
    rows = [rates.get(d) or rates[f"_{g}"] for d, g in zip(test["division"], test["gender"])]
    share = pd.DataFrame(rows).rename(columns={"KO": "ko", "SUB": "sub", "DEC": "dec"})
    out = pd.DataFrame({f"base_a_{m}": p * share[m] for m in METHODS})
    for m in METHODS:
        out[f"base_b_{m}"] = (1 - p) * share[m]
    dist = out["base_a_dec"] + out["base_b_dec"]
    rounds = RoundModel.fit(train).split(1 - dist.to_numpy(), test["rounds"].to_numpy())
    for r in range(rounds.shape[1]):
        out[f"base_r{r + 1}"] = rounds[:, r]
    return out


def _ll(p: np.ndarray, y: np.ndarray) -> np.ndarray:
    p = np.clip(p, 1e-4, 1 - 1e-4)
    return -(y * np.log(p) + (1 - y) * np.log(1 - p))


def win_scores(bt: pd.DataFrame) -> pd.DataFrame:
    """Winner log loss, Brier and pick rate on fights with a moneyline."""
    d = decided(bt)
    p_mkt = devig(d["odds_a"], d["odds_b"])
    d = d[~np.isnan(p_mkt)]
    p_mkt = p_mkt[~np.isnan(p_mkt)]
    y = (d["winner"] == "a").to_numpy(float)
    rows = []
    for name, p in [("Final (model + market)", d["p_a"]), ("Model only", d["p_model"]),
                    ("Betting market (de-vigged)", p_mkt), ("Glicko-2 rating alone", d["p_glicko"]),
                    ("Elo, UFC results only", d["elo_prob"])]:
        p = np.asarray(p, dtype=float)
        rows.append({"predictor": name, "fights": len(d), "log_loss": float(_ll(p, y).mean()),
                     "brier": float(np.mean((p - y) ** 2)),
                     "winners": float(np.mean((p > 0.5) == (y == 1)))})
    return pd.DataFrame(rows)


def method_scores(bt: pd.DataFrame) -> pd.DataFrame:
    """Six-way winner-by-method log loss on fights with method props."""
    d = decided(bt)
    d = d[d["method"].isin(["KO", "SUB", "DEC"])]
    market = devig_methods(d)
    ok = market.notna().all(axis=1) if market is not None else pd.Series(False, index=d.index)
    d, market = d[ok], market[ok] if market is not None else None
    if d.empty:
        return pd.DataFrame()
    col = (d["winner"] + "_" + d["method"].str.lower()).to_numpy()
    idx = np.array([SIX.index(c) for c in col])

    def ll(P):
        P = np.clip(np.asarray(P, float), 1e-4, 1)
        P = P / P.sum(axis=1, keepdims=True)
        return float(-np.mean(np.log(P[np.arange(len(P)), idx])))

    went = (d["method"] == "DEC").to_numpy(float)
    rows = []
    for name, P, dist in [
        ("Final", d[SIX], d["p_distance"]),
        ("Division base rates × market win chance", d[[f"base_{c}" for c in SIX]],
         d["base_a_dec"] + d["base_b_dec"]),
        ("Method props (de-vigged)", market[["a_ko", "a_sub", "a_dec", "b_ko", "b_sub", "b_dec"]],
         market["a_dec"] + market["b_dec"]),
    ]:
        dist = np.asarray(dist, float)
        rows.append({"predictor": name, "fights": len(d), "six_way_log_loss": ll(P),
                     "distance_predicted": float(dist.mean()), "distance_actual": float(went.mean()),
                     "distance_log_loss": float(_ll(dist, went).mean())})
    rows.append({"predictor": "Uniform guess", "fights": len(d), "six_way_log_loss": float(np.log(6)),
                 "distance_predicted": 0.5, "distance_actual": float(went.mean()),
                 "distance_log_loss": float(np.log(2))})
    return pd.DataFrame(rows)


def round_scores(bt: pd.DataFrame) -> pd.DataFrame:
    """Log loss over 'finished in round r' or 'went the distance', by scheduled rounds."""
    d = decided(bt)
    d = d[d["method"].isin(["KO", "SUB", "DEC"]) & d["rounds"].isin([3, 5])]
    rows = []
    for rounds in (3, 5):
        g = d[d["rounds"] == rounds]
        if g.empty:
            continue
        outcome = np.where(g["method"] == "DEC", rounds, g["end_round"].clip(upper=rounds) - 1).astype(int)
        for name, prefix in (("Final", "r"), ("Division base rates", "base_r")):
            P = np.column_stack([g[f"{prefix}{r}"] for r in range(1, rounds + 1)]
                                + [1 - sum(g[f"{prefix}{r}"] for r in range(1, rounds + 1))])
            P = np.clip(P, 1e-4, 1)
            rows.append({"rounds": rounds, "predictor": name, "fights": len(g),
                         "log_loss": float(-np.mean(np.log(P[np.arange(len(g)), outcome])))})
    return pd.DataFrame(rows)


def calibration(bt: pd.DataFrame, col: str = "p_a") -> pd.DataFrame:
    """Win chance of the predicted favorite against how often favorites won."""
    d = decided(bt)
    p = d[col].to_numpy(float)
    won = (d["winner"] == "a").to_numpy(float)
    fav_p = np.maximum(p, 1 - p)
    fav_won = np.where(p >= 0.5, won, 1 - won)
    bins = [0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 1.0]
    which = np.clip(np.digitize(fav_p, bins) - 1, 0, len(bins) - 2)
    g = pd.DataFrame({"bin": which, "p": fav_p, "won": fav_won}).groupby("bin").agg(
        fights=("p", "size"), predicted=("p", "mean"), actual=("won", "mean"))
    g.index = [f"{int(bins[i] * 100)}–{int(bins[i + 1] * 100)}%" for i in g.index]
    return g


def paired_bootstrap(loss_a: np.ndarray, loss_b: np.ndarray, n: int = 5000, seed: int = 0) -> tuple:
    """Mean of (a - b) and its 95% interval over resampled fights."""
    rng = np.random.default_rng(seed)
    diff = np.asarray(loss_a) - np.asarray(loss_b)
    idx = rng.integers(0, len(diff), size=(n, len(diff)))
    means = diff[idx].mean(axis=1)
    return float(diff.mean()), float(np.percentile(means, 2.5)), float(np.percentile(means, 97.5))


def bootstraps(bt: pd.DataFrame) -> dict:
    d = decided(bt)
    p_mkt = devig(d["odds_a"], d["odds_b"])
    d = d[~np.isnan(p_mkt)]
    p_mkt = p_mkt[~np.isnan(p_mkt)]
    y = (d["winner"] == "a").to_numpy(float)
    final, model = _ll(d["p_a"].to_numpy(float), y), _ll(d["p_model"].to_numpy(float), y)
    market, glicko = _ll(p_mkt, y), _ll(d["p_glicko"].to_numpy(float), y)
    return {
        "Final vs market": paired_bootstrap(final, market),
        "Model only vs market": paired_bootstrap(model, market),
        "Model only vs Glicko-2 alone": paired_bootstrap(model, glicko),
    }


def betting(bt: pd.DataFrame, prob_col: str = "p_a", edge: float = VALUE_EDGE) -> dict:
    """Flat one-unit moneyline bets wherever ``prob_col`` beats the price's implied chance by ``edge``.

    Prices are the dataset's (approximate closing) moneylines with the
    bookmaker's margin left in, so this is what the bets would have returned.
    """
    d = decided(bt).dropna(subset=["odds_a", "odds_b"])
    p = d[prob_col].to_numpy(float)
    rows = []
    for side, ps, odds in (("a", p, d["odds_a"]), ("b", 1 - p, d["odds_b"])):
        implied = implied_prob(odds)
        pick = ps - implied >= edge
        won = (d["winner"] == side).to_numpy()
        profit = np.where(won, decimal(odds) - 1, -1.0)
        rows.append(pd.DataFrame({"profit": profit[pick], "dog": (np.asarray(odds) > 0)[pick]}))
    bets = pd.concat(rows, ignore_index=True)
    if bets.empty:
        return {"bets": 0}
    rng = np.random.default_rng(1)
    idx = rng.integers(0, len(bets), size=(5000, len(bets)))
    roi = bets["profit"].to_numpy()[idx].mean(axis=1)
    return {"bets": len(bets), "roi": float(bets["profit"].mean()), "units": float(bets["profit"].sum()),
            "roi_low": float(np.percentile(roi, 2.5)), "roi_high": float(np.percentile(roi, 97.5)),
            "underdogs": float(bets["dog"].mean()), "fights": len(d)}


def betting_grid(bt: pd.DataFrame, edges=(0.0, 0.02, 0.03, 0.05, 0.08)) -> pd.DataFrame:
    """Betting returns for the final and the model-alone win chances at several edges."""
    rows = []
    for label, col in (("Final win chance", "p_a"), ("Model alone", "p_model")):
        for e in edges:
            r = betting(bt, col, e)
            if r.get("bets"):
                rows.append({"chance": label, "edge": e, **r})
    return pd.DataFrame(rows)


def tune(fb: FeatureBuilder, odds: pd.DataFrame, years, grid: dict, base: Hyperparams) -> pd.DataFrame:
    """Grid search over rating and profile settings, scored on model-only log loss.

    Only the structural settings are tuned; the win model is refitted on the
    years before each scored year, as in production.
    """
    keys = list(grid)
    results = []
    for combo in itertools.product(*(grid[k] for k in keys)):
        hp = replace(base, **dict(zip(keys, combo)))
        fb.hp = hp
        feats = fb.build().join(odds.reset_index(drop=True))
        year = feats["date"].dt.year
        losses = []
        for y in years:
            train = decided(feats[(year >= y - hp.fit_window_years) & (year < y) & (year >= 1998)])
            test = decided(feats[year == y])
            z = WinModel.fit(train, hp.ridge).logit(test)
            losses.append(_ll(1 / (1 + np.exp(-z)), (test["winner"] == "a").to_numpy(float)))
        loss = float(np.concatenate(losses).mean())
        results.append({**dict(zip(keys, combo)), "log_loss": loss})
        log.info("%s -> %.4f", dict(zip(keys, combo)), loss)
    fb.hp = base
    return pd.DataFrame(results).sort_values("log_loss", ignore_index=True)
