"""Batter and pitcher ratings: each player's rate of every plate-appearance outcome.

Every player is rated on seven outcomes per plate appearance: strikeout,
walk, hit by pitch, single, double, triple and home run (everything else is
an out in play). A rating is a recency-weighted average of the player's own
park-adjusted results, pulled toward the league average for his role by the
amount of evidence that outcome needs before it becomes reliable. That amount
(the outcome's stabilization point) is estimated from history by empirical
Bayes: strikeout and walk rates settle within a couple of hundred plate
appearances, while hits on balls in play, especially for pitchers, take
thousands. This is the in-season version of a Marcel-style projection: last
season's record is the prior, and each game moves it a little.

Since 2015 a share of each hit count can come from Statcast's expected hits
on the player's balls in play instead (``statcast.py``): how hard and at what
angle he hit them, or allowed them, rather than where they happened to land.
Those settle faster, so their shrinkage is smaller.

Time is measured in days of the season, with each off-season counting as
about two months, so last September weighs a little less than this April.

A batter and a pitcher combine in a plate appearance by the generalized log5
rule, with a platoon factor for the batter's side and the pitcher's hand:

    P(outcome) ∝ batter rate × pitcher rate / league rate × platoon factor
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from .config import FIRST_SEASON, Hyperparams
from .parks import COMPONENTS, ParkFactors
from .statcast import HITS, X_COLUMNS

OUTCOMES = COMPONENTS + ["out"]
# Days from March 1 that one season occupies; the gap between seasons is
# what is left after the World Series.
SEASON_SPAN = 250
TIME_ORIGIN = 2000
# Half-life (days) of the league averages players are pulled toward.
POOL_HALF_LIFE = 150.0
# Seasons used once to measure how fast each outcome stabilizes.
STABILITY_SEASONS = (FIRST_SEASON, FIRST_SEASON + 3)
MIN_SEASON_PA = 300
# Batter pools: position players and pitchers at the plate.
BAT_POOL, PITCHER_BAT_POOL = "_BAT", "_PBAT"
SP_POOL, RP_POOL = "_SP", "_RP"
ALL_POOL = "_ALL"


def season_time(dates, seasons) -> np.ndarray:
    """Days since March 1 of the season, plus ``SEASON_SPAN`` per season since 2000."""
    d = pd.to_datetime(pd.Series(dates).reset_index(drop=True))
    s = np.asarray(seasons, dtype=int)
    origin = pd.to_datetime(pd.Series(s).astype(str) + "-03-01")
    day = (d - origin).dt.days.to_numpy()
    return (s - TIME_ORIGIN) * SEASON_SPAN + np.clip(day, 0, SEASON_SPAN - 1)


class RateEngine:
    """Recency-weighted sums of exposure and outcome counts for any key at any time.

    Each key's rows are sorted by time and accumulated with weight
    ``2 ** (tau / half_life)``; the sum before time ``t`` is then one lookup
    times ``0.5 ** (t / half_life)``.
    """

    def __init__(self, keys, tau, exposure, counts: np.ndarray, half_life: float):
        self.half_life = half_life
        order = np.lexsort((np.asarray(tau), np.asarray(keys)))
        keys = np.asarray(keys)[order]
        tau = np.asarray(tau, dtype=np.int64)[order]
        self.codes = {k: i for i, k in enumerate(pd.unique(keys))}
        code = pd.Series(keys).map(self.codes).to_numpy(np.int64)
        self.key = code * 100_000 + tau
        self.code = code
        w = np.exp2(tau / half_life)
        vals = np.column_stack([np.asarray(exposure, dtype=float)[order], np.asarray(counts, dtype=float)[order]])
        self.cum = pd.DataFrame(vals * w[:, None]).groupby(code).cumsum().to_numpy()

    def sums(self, keys, tau) -> np.ndarray:
        """(n, 1 + outcomes): weighted exposure and counts before each ``tau``."""
        tau = np.asarray(tau, dtype=np.int64)
        code = pd.Series(np.asarray(keys)).map(self.codes).fillna(-1).to_numpy(np.int64)
        pos = np.searchsorted(self.key, code * 100_000 + tau, side="left") - 1
        ok = (code >= 0) & (pos >= 0)
        ok[ok] &= self.code[pos[ok]] == code[ok]
        out = np.zeros((len(tau), self.cum.shape[1]))
        out[ok] = self.cum[pos[ok]] * np.exp2(-tau[ok] / self.half_life)[:, None]
        return out


def stabilization(rows: pd.DataFrame, exposure: str, min_pa: int = MIN_SEASON_PA) -> np.ndarray:
    """Plate appearances of evidence at which each outcome's observed rate is
    half signal, half noise: binomial variance over the spread of true talent."""
    season = rows.groupby(["season", "player_id"])[[exposure] + COMPONENTS].sum()
    season = season[season[exposure] >= min_pa]
    n = season[exposure].to_numpy(float)
    out = []
    for e in COMPONENTS:
        p = season[e].to_numpy(float) / n
        mean = season[e].sum() / n.sum()
        noise = np.mean(mean * (1 - mean) / n)
        true_var = max(np.var(p) - noise, 1e-6 * mean)
        out.append(mean * (1 - mean) / true_var)
    return np.array(out)


def blend_expected(rows: pd.DataFrame, expected: pd.DataFrame, weight: float) -> np.ndarray:
    """Mix Statcast's expected hits into ``rows``' park-adjusted hit columns (``s_adj`` ...) in place,
    ``weight`` expected to ``1 - weight`` actual, on player-days Statcast covers. Each row's share of
    a day's expected hits follows its balls in play. Returns which rows were covered."""
    bip = rows[["s", "d", "t", "hr", "out"]].sum(axis=1).to_numpy(float)
    day = pd.to_datetime(rows["date"]).dt.strftime("%Y-%m-%d")
    sc = expected.groupby(["player_id", "date"])[["bip", *X_COLUMNS]].sum()
    hit = sc.reindex(pd.MultiIndex.from_arrays([rows["player_id"].astype(str), day]))
    n = hit["bip"].to_numpy(float)
    covered = np.nan_to_num(n) > 0
    rate = hit[X_COLUMNS].to_numpy(float) / np.where(covered, n, 1.0)[:, None]
    for i, h in enumerate(HITS):
        col = rows[h + "_adj"].to_numpy(float)
        rows[h + "_adj"] = np.where(covered, (1 - weight) * col + weight * rate[:, i] * bip, col)
    return covered


def platoon_factors(platoon: pd.DataFrame) -> dict[tuple[str, str], np.ndarray]:
    """Outcome multipliers for each batter side and pitcher hand, relative to
    what the batter's and the pitcher's own averages already carry (the
    interaction left after log5). Switch hitters bat from the opposite side."""
    p = platoon[platoon["bats"].isin(["L", "R", "B"]) & platoon["throws"].isin(["L", "R"])]
    t = p.pivot_table(index=["bats", "throws"], columns="event", values="n", aggfunc="sum").reindex(
        columns=OUTCOMES).fillna(0.0)
    rate = t.div(t.sum(axis=1), axis=0)
    by_bat = t.groupby(level=0).sum()
    by_bat = by_bat.div(by_bat.sum(axis=1), axis=0)
    by_throw = t.groupby(level=1).sum()
    by_throw = by_throw.div(by_throw.sum(axis=1), axis=0)
    league = t.sum() / t.sum().sum()
    out = {}
    for (bats, throws), r in rate.iterrows():
        out[(bats, throws)] = (r * league / (by_bat.loc[bats] * by_throw.loc[throws])).to_numpy(float)
    return out


def log5(batter: np.ndarray, pitcher: np.ndarray, league: np.ndarray,
         factor: np.ndarray | None = None) -> np.ndarray:
    """Outcome probabilities (n, 8) from batter, pitcher and league rates (n, 7)."""
    def full(r):
        r = np.clip(r, 1e-5, None)
        return np.column_stack([r, np.clip(1.0 - r.sum(axis=1), 0.05, None)])
    num = full(batter) * full(pitcher) / full(league)
    if factor is not None:
        num = num * factor
    return num / num.sum(axis=1, keepdims=True)


class PlayerRatings:
    """Outcome rates for every batter and pitcher at any point in time."""

    def __init__(self, summaries: dict, parks: ParkFactors, hp: Hyperparams):
        self.hp = hp
        games = summaries["games"].set_index("game_id")
        bat = summaries["batting"].join(games[["date", "season", "park_id"]], on="game_id", how="inner")
        pit = summaries["pitching"].join(games[["date", "season", "park_id"]], on="game_id", how="inner")
        for rows in (bat, pit):
            rows["tau"] = season_time(rows["date"], rows["season"])
            for e in COMPONENTS:
                rows[e + "_adj"] = rows[e] / parks.lookup(rows["season"], rows["park_id"], e)
        adj = [e + "_adj" for e in COMPONENTS]
        self.statcast = hp.statcast_weight > 0 and len(summaries.get("statcast_batting", ())) > 0
        if self.statcast:
            blend_expected(bat, summaries["statcast_batting"], hp.statcast_weight)
            blend_expected(pit, summaries["statcast_pitching"], hp.statcast_weight)
        self.batting = RateEngine(bat["player_id"], bat["tau"], bat["pa"], bat[adj].to_numpy(),
                                  hp.batter_half_life)
        self.pitching = RateEngine(pit["player_id"], pit["tau"], pit["bf"], pit[adj].to_numpy(),
                                   hp.pitcher_half_life)
        pools = pd.concat([
            pd.DataFrame({"key": np.where(bat["pos"].eq(1), PITCHER_BAT_POOL, BAT_POOL), "tau": bat["tau"],
                          "n": bat["pa"], **{e: bat[e] for e in COMPONENTS}}),
            pd.DataFrame({"key": np.where(pit["starter"].eq(1), SP_POOL, RP_POOL), "tau": pit["tau"],
                          "n": pit["bf"], **{e: pit[e] for e in COMPONENTS}}),
            pd.DataFrame({"key": ALL_POOL, "tau": pit["tau"], "n": pit["bf"], **{e: pit[e] for e in COMPONENTS}}),
        ], ignore_index=True)
        self.pools = RateEngine(pools["key"], pools["tau"], pools["n"], pools[COMPONENTS].to_numpy(),
                                POOL_HALF_LIFE)
        early = summaries["batting"].join(games["season"], on="game_id")
        early_p = summaries["pitching"].join(games["season"], on="game_id")
        lo, hi = STABILITY_SEASONS
        if early["season"].between(lo, hi).any():
            early, early_p = early[early["season"].between(lo, hi)], early_p[early_p["season"].between(lo, hi)]
        self.k_batter = stabilization(early, "pa") * hp.batter_shrink
        self.k_pitcher = stabilization(early_p.rename(columns={"bf": "pa"}), "pa") * hp.pitcher_shrink
        if self.statcast:
            hits = [COMPONENTS.index(h) for h in HITS]
            self.k_batter[hits] *= hp.statcast_shrink
            self.k_pitcher[hits] *= hp.statcast_shrink

    def league(self, tau, pool: str = ALL_POOL) -> np.ndarray:
        s = self.pools.sums(np.full(len(np.atleast_1d(tau)), pool), np.atleast_1d(tau))
        return s[:, 1:] / np.maximum(s[:, :1], 1e-9)

    def _rates(self, engine: RateEngine, k: np.ndarray, players, tau, pools) -> tuple[np.ndarray, np.ndarray]:
        own = engine.sums(players, tau)
        prior = self.pools.sums(np.asarray(pools), tau)
        prior = prior[:, 1:] / np.maximum(prior[:, :1], 1e-9)
        n = own[:, :1]
        rates = (own[:, 1:] + k * prior) / (n + k)
        return rates, n[:, 0]

    def batters(self, players, tau, pitcher_batting=None) -> tuple[np.ndarray, np.ndarray]:
        """Outcome rates (n, 7) and weighted plate appearances behind them."""
        pools = np.where(np.asarray(pitcher_batting if pitcher_batting is not None
                                    else np.zeros(len(tau), dtype=bool)), PITCHER_BAT_POOL, BAT_POOL)
        return self._rates(self.batting, self.k_batter, players, tau, pools)

    def pitchers(self, players, tau, starter) -> tuple[np.ndarray, np.ndarray]:
        pools = np.where(np.asarray(starter, dtype=bool), SP_POOL, RP_POOL)
        return self._rates(self.pitching, self.k_pitcher, players, tau, pools)
