"""Betting odds: historical prices, the live odds log, and removing the margin.

Historical moneylines and method props come from the Ultimate UFC Dataset
(2010 onward; its capture time is undocumented, so treat them as approximate
closing prices). Live prices seen by the predictor are appended to
``data/odds_log.csv`` with a timestamp, so the record of prices keeps growing
after the dataset stops.
"""

from __future__ import annotations

import logging

import numpy as np
import pandas as pd
import requests

from .config import CACHE_DIR, DATA_DIR, ODDS_URL
from .data import fetch
from .names import normalize_name, pair_key

log = logging.getLogger(__name__)

ODDS_LOG_PATH = DATA_DIR / "odds_log.csv"
ODDS_LOG_COLUMNS = ["captured_at", "bout_key", "date", "fighter_a", "fighter_b", "odds_a", "odds_b", "source"]
METHOD_ODDS = ["odds_a_ko", "odds_a_sub", "odds_a_dec", "odds_b_ko", "odds_b_sub", "odds_b_dec"]
ODDS_COLUMNS = ["odds_a", "odds_b", *METHOD_ODDS, "odds_source"]


def implied_prob(american) -> np.ndarray:
    ml = np.asarray(american, dtype=float)
    with np.errstate(divide="ignore", invalid="ignore"):
        return np.where(ml < 0, -ml / (-ml + 100.0), 100.0 / (ml + 100.0))


def devig(price_a, price_b) -> np.ndarray:
    """Probability of side A from two American prices, margin removed proportionally."""
    a, b = implied_prob(price_a), implied_prob(price_b)
    with np.errstate(divide="ignore", invalid="ignore"):
        return a / (a + b)


def devig_methods(df: pd.DataFrame) -> pd.DataFrame | None:
    """Six-way winner-by-method probabilities (a_ko ... b_dec) from method props, margin removed."""
    if not set(METHOD_ODDS) <= set(df.columns):
        return None
    p = pd.DataFrame({c.removeprefix("odds_"): implied_prob(df[c]) for c in METHOD_ODDS}, index=df.index)
    return p.div(p.sum(axis=1), axis=0)


def decimal(american) -> np.ndarray:
    ml = np.asarray(american, dtype=float)
    with np.errstate(divide="ignore", invalid="ignore"):
        return np.where(ml < 0, 1 + 100.0 / -ml, 1 + ml / 100.0)


def load_dataset_odds(max_age_hours: float = 24.0) -> pd.DataFrame:
    try:
        path = fetch(ODDS_URL, CACHE_DIR / "ufc-master.csv", max_age_hours)
    except requests.RequestException as exc:
        log.warning("Odds dataset download failed: %s", exc)
        return pd.DataFrame()
    m = pd.read_csv(path)
    return pd.DataFrame({
        "date": pd.to_datetime(m["date"], errors="coerce"),
        "r": m["R_fighter"], "b": m["B_fighter"],
        "r_odds": m["R_odds"], "b_odds": m["B_odds"],
        "r_ko": m.get("r_ko_odds"), "r_sub": m.get("r_sub_odds"), "r_dec": m.get("r_dec_odds"),
        "b_ko": m.get("b_ko_odds"), "b_sub": m.get("b_sub_odds"), "b_dec": m.get("b_dec_odds"),
    })


def _match_by_date(bouts: pd.DataFrame, other: pd.DataFrame, max_days: int = 1) -> pd.Series:
    """Index into ``other`` for each bout: same pair of names, date within ``max_days``."""
    if other.empty:
        return pd.Series(np.nan, index=bouts.index)
    left = pd.DataFrame({"key": [pair_key(a, b) for a, b in zip(bouts["fighter_a"], bouts["fighter_b"])],
                         "date": bouts["date"].to_numpy(), "bi": bouts.index})
    right = pd.DataFrame({"key": other["key"].to_numpy(), "odate": other["date"].to_numpy(),
                          "oi": other.index})
    j = left.merge(right, on="key")
    j = j[(j["date"] - j["odate"]).abs() <= pd.Timedelta(days=max_days)]
    j = j.sort_values("oi").drop_duplicates("bi", keep="last")
    return pd.Series(j["oi"].to_numpy(), index=j["bi"].to_numpy()).reindex(bouts.index)


def attach_dataset_odds(bouts: pd.DataFrame, ds: pd.DataFrame) -> pd.DataFrame:
    """Odds columns for each bout in fighter_a / fighter_b order (NaN when unknown)."""
    out = pd.DataFrame(np.nan, index=bouts.index, columns=ODDS_COLUMNS)
    out["odds_source"] = None
    if ds.empty:
        return out
    ds = ds.assign(key=[pair_key(a, b) for a, b in zip(ds["r"], ds["b"])])
    which = _match_by_date(bouts, ds)
    hit = which.notna()
    rows = ds.loc[which[hit].astype(int)].set_index(which.index[hit])
    flipped = rows["r"].map(normalize_name).to_numpy() != bouts.loc[hit, "fighter_a"].map(normalize_name).to_numpy()
    for ours, red, blue in [("odds", "r_odds", "b_odds"), ("ko", "r_ko", "b_ko"), ("sub", "r_sub", "b_sub"),
                            ("dec", "r_dec", "b_dec")]:
        a_col = "odds_a" if ours == "odds" else f"odds_a_{ours}"
        b_col = "odds_b" if ours == "odds" else f"odds_b_{ours}"
        out.loc[hit, a_col] = np.where(flipped, rows[blue], rows[red])
        out.loc[hit, b_col] = np.where(flipped, rows[red], rows[blue])
    out.loc[hit & out["odds_a"].notna(), "odds_source"] = "dataset"
    return out


def load_odds_log() -> pd.DataFrame:
    if not ODDS_LOG_PATH.exists():
        return pd.DataFrame(columns=ODDS_LOG_COLUMNS)
    lg = pd.read_csv(ODDS_LOG_PATH)
    lg["captured_at"] = pd.to_datetime(lg["captured_at"], utc=True)
    lg["date"] = pd.to_datetime(lg["date"])
    return lg


def append_odds_log(rows: pd.DataFrame, now: pd.Timestamp) -> pd.DataFrame:
    """Record live prices, skipping ones unchanged since the last capture of that bout."""
    lg = load_odds_log()
    rows = rows.dropna(subset=["odds_a", "odds_b"])
    if rows.empty:
        return lg
    new = pd.DataFrame({
        "captured_at": now, "bout_key": rows["bout_key"].to_numpy(),
        "date": pd.to_datetime(rows["date"]).to_numpy(),
        "fighter_a": rows["fighter_a"].to_numpy(), "fighter_b": rows["fighter_b"].to_numpy(),
        "odds_a": rows["odds_a"].astype(float).to_numpy(), "odds_b": rows["odds_b"].astype(float).to_numpy(),
        "source": rows["odds_source"].to_numpy(),
    })
    if len(lg):
        last = lg.sort_values("captured_at").drop_duplicates("bout_key", keep="last").set_index("bout_key")
        same = (new["bout_key"].map(last["odds_a"]) == new["odds_a"]) & \
               (new["bout_key"].map(last["odds_b"]) == new["odds_b"]) & \
               (new["bout_key"].map(last["fighter_a"]) == new["fighter_a"])
        new = new[~same]
    if new.empty:
        return lg
    out = pd.concat([lg, new], ignore_index=True) if len(lg) else new
    out["captured_at"] = pd.to_datetime(out["captured_at"], utc=True)
    out = out.sort_values(["captured_at", "bout_key"], ignore_index=True)
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    saved = out.assign(captured_at=out["captured_at"].map(lambda t: t.isoformat()))
    saved.to_csv(ODDS_LOG_PATH, index=False, date_format="%Y-%m-%d")
    return out


def attach_logged_odds(bouts: pd.DataFrame, odds: pd.DataFrame, lg: pd.DataFrame) -> pd.DataFrame:
    """Fill bouts the dataset misses with the last logged live price before the bout."""
    if lg.empty:
        return odds
    last = lg.sort_values("captured_at").drop_duplicates(["bout_key", "date"], keep="last").copy()
    last["key"] = [pair_key(a, b) for a, b in zip(last["fighter_a"], last["fighter_b"])]
    last = last.reset_index(drop=True)
    which = _match_by_date(bouts, last)
    hit = which.notna() & odds["odds_a"].isna()
    rows = last.loc[which[hit].astype(int)].set_index(which.index[hit])
    flipped = rows["fighter_a"].map(normalize_name).to_numpy() != bouts.loc[hit, "fighter_a"].map(normalize_name).to_numpy()
    odds = odds.copy()
    odds.loc[hit, "odds_a"] = np.where(flipped, rows["odds_b"], rows["odds_a"])
    odds.loc[hit, "odds_b"] = np.where(flipped, rows["odds_a"], rows["odds_b"])
    odds.loc[hit, "odds_source"] = rows["source"].to_numpy()
    return odds


def market_odds(bouts: pd.DataFrame, max_age_hours: float = 24.0) -> pd.DataFrame:
    """Odds for every bout from the dataset, then the live log."""
    odds = attach_dataset_odds(bouts, load_dataset_odds(max_age_hours))
    odds = attach_logged_odds(bouts, odds, load_odds_log())
    log.info("Odds for %d of %d bouts", int(odds["odds_a"].notna().sum()), len(bouts))
    return odds
