"""Historical betting lines from the sportsbookreview.com archive.

The flancast90/sportsbookreview-scraper repository publishes about ten
seasons (2011-12 to 2021-22) of sportsbookreview's odds archive per sport as
JSON: opening and closing moneylines, the closing spread (the puck line or
run line in hockey and baseball) with its prices, and opening and closing
totals, next to each game's final score. Teams are named by nickname
("Bruins"), so each predictor maps them to its own codes.

Three quirks are handled here. Missing values are stored as 0, so a zero
price, spread price or total becomes NaN (a zero spread can be a real pick'em
and is kept when it has prices). Each total carries a single price whose side
is not recorded, so total prices are dropped and totals are treated as
unpriced. And in the baseball file every row pairs one game's visitors (in the
``home_*`` fields, with the game's date and total) with the previous game's
home team (in the ``away_*`` fields); ``realign`` puts each game back together
(checked against Retrosheet: about 99% of 2012-2021 games then match, and the
two moneylines' implied chances sum to the usual 102-104%).

``match`` joins archive rows to a predictor's games on the date (a day either
way, for time zones), both teams and the final score, which also tells
doubleheaders apart and drops rows whose score the archive got wrong.
"""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pandas as pd

from .io import fetch

SBR_URL = ("https://raw.githubusercontent.com/flancast90/sportsbookreview-scraper/main/data/"
           "{sport}_archive_10Y.json")
PRICES = ["home_open_ml", "away_open_ml", "home_close_ml", "away_close_ml", "home_close_spread_odds",
          "away_close_spread_odds"]
LINES = ["home_open_spread", "home_close_spread", "open_total", "close_total"]
COLUMNS = ["date", "sbr_season", "home", "away", "home_final", "away_final", *PRICES, *LINES]
# Files whose rows carry the home team one row late (see ``realign``).
SHIFTED = ("mlb",)


def realign(raw: pd.DataFrame) -> pd.DataFrame:
    """Raw archive rows of a shifted file as one row per game: each row's ``home_*`` fields
    are its game's visitors, and the next row's (same season) ``away_*`` fields its home team."""
    home = [c for c in raw.columns if c.startswith("home_")]
    away = [c for c in raw.columns if c.startswith("away_")]
    later = raw.groupby("season", sort=False)[away].shift(-1) if "season" in raw else raw[away].shift(-1)
    out = raw.drop(columns=home + away)
    for c in home:
        out["away_" + c[5:]] = raw[c]
    for c in away:
        out["home_" + c[5:]] = later[c]
    return out


def parse(rows: list[dict], shifted: bool = False) -> pd.DataFrame:
    """Archive rows as a frame with ``COLUMNS`` (whatever the sport's file has; the rest NaN),
    realigned first when the file is ``shifted``."""
    raw = pd.DataFrame(rows)
    if shifted:
        raw = realign(raw)
    raw = raw.dropna(subset=["home_team", "away_team"]).reset_index(drop=True)
    out = pd.DataFrame({
        "date": pd.to_datetime(raw["date"].astype("Int64").astype(str), format="%Y%m%d", errors="coerce"),
        "sbr_season": pd.to_numeric(raw.get("season"), errors="coerce"),
        "home": raw["home_team"].astype(str).str.strip(), "away": raw["away_team"].astype(str).str.strip(),
        "home_final": pd.to_numeric(raw["home_final"], errors="coerce"),
        "away_final": pd.to_numeric(raw["away_final"], errors="coerce"),
    })
    for col in PRICES:
        v = pd.to_numeric(raw[col], errors="coerce") if col in raw else pd.Series(np.nan, index=raw.index)
        out[col] = v.where(v.abs() >= 100)
    spread_priced = out["home_close_spread_odds"].notna() | out["away_close_spread_odds"].notna()
    for col, src in (("home_open_spread", "home_open_spread"), ("home_close_spread", "home_close_spread")):
        v = pd.to_numeric(raw[src], errors="coerce") if src in raw else pd.Series(np.nan, index=raw.index)
        keep = v.ne(0) | (spread_priced if col == "home_close_spread" else False)
        out[col] = v.where(keep)
    for col, src in (("open_total", "open_over_under"), ("close_total", "close_over_under")):
        v = pd.to_numeric(raw[src], errors="coerce") if src in raw else pd.Series(np.nan, index=raw.index)
        out[col] = v.where(v > 0)
    return out[COLUMNS]


def load_archive(sport: str, cache_dir: Path, max_age_hours: float = 24.0 * 30) -> pd.DataFrame:
    """The archive for ``sport`` (``nhl``, ``mlb``, ``nfl`` or ``nba``), downloaded once a month."""
    path = fetch(SBR_URL.format(sport=sport), Path(cache_dir) / f"sbr_{sport}.json", max_age_hours)
    return parse(json.loads(Path(path).read_text()), shifted=sport in SHIFTED)


def match(sbr: pd.DataFrame, games: pd.DataFrame, names: dict, date: str = "date", home: str = "home_team",
          away: str = "away_team", home_score: str = "home_score", away_score: str = "away_score",
          key: str = "game_id") -> pd.DataFrame:
    """Archive lines for ``games``, indexed by ``key``.

    ``names`` maps archive nicknames to the predictor's team codes (a
    nickname missing from it leaves its games unmatched). A game matches a
    row with the same teams and final score dated the same day or a day
    either side; when several rows qualify, the nearest date wins, and each
    row is used once.
    """
    s = sbr.assign(home_code=sbr["home"].map(names), away_code=sbr["away"].map(names))
    s = s.dropna(subset=["home_code", "away_code", "date", "home_final", "away_final"]).reset_index(drop=True)
    g = games[[key, date, home, away, home_score, away_score]].dropna().copy()
    day = pd.to_datetime(g[date])
    if day.dt.tz is not None:
        day = day.dt.tz_localize(None)
    g["_day"] = day.dt.normalize()
    s["_row"] = np.arange(len(s))
    cands = []
    for shift in (0, -1, 1):
        t = s.assign(_day=s["date"] + pd.Timedelta(days=shift), _shift=abs(shift))
        m = g.merge(t, left_on=["_day", home, away, home_score, away_score],
                    right_on=["_day", "home_code", "away_code", "home_final", "away_final"])
        cands.append(m)
    m = pd.concat(cands, ignore_index=True).sort_values(["_shift", "_row"])
    m = m.drop_duplicates("_row").drop_duplicates(key)
    return m.set_index(key)[[c for c in COLUMNS if c not in ("date", "home", "away", "home_final", "away_final")]]
