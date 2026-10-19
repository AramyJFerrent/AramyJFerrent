"""Historical betting lines, matched to games.

Two public archives, converted once into ``data/lines.csv``:

- The sportsbookreview.com archive (2011-12 to 2021-22): opening and
  closing spreads and totals and closing moneylines. About 7% of its rows
  swap the closing spread and total (the total sits in the spread field,
  signed like the home team's line, and the spread's size in the total
  field); those are put back.
- The database in the NBA-Machine-Learning-Sports-Betting repository, for
  the seasons the first archive does not cover (2007-08 to 2010-11 and
  2022-23 to January 2026). Through 2021-22 its spreads and totals are the
  sportsbookreview *opening* numbers (they match in 99% of games) and its
  spreads carry no sign, so the favorite is taken from the moneyline; from
  2022-23 the spreads are signed.

``spread`` is always the home team's expected margin (positive when the home
team is favored), the convention used everywhere in this predictor, and is
the closing line wherever the archives have one.
"""

from __future__ import annotations

import json
import logging
import sqlite3

import numpy as np
import pandas as pd

from .config import CACHE_DIR, KYLESKOM_ODDS_URL, LINES_PATH, SBR_ARCHIVE_URL
from .data import fetch

log = logging.getLogger(__name__)

LINE_COLUMNS = ["date", "home_team", "away_team", "spread", "total", "home_moneyline", "away_moneyline",
                "open_spread", "open_total"]

FULL_NAMES = {
    "Atlanta Hawks": "ATL", "Boston Celtics": "BOS", "Brooklyn Nets": "BKN", "New Jersey Nets": "BKN",
    "Charlotte Bobcats": "CHA", "Charlotte Hornets": "CHA", "Chicago Bulls": "CHI",
    "Cleveland Cavaliers": "CLE", "Dallas Mavericks": "DAL", "Denver Nuggets": "DEN",
    "Detroit Pistons": "DET", "Golden State Warriors": "GSW", "Houston Rockets": "HOU",
    "Indiana Pacers": "IND", "LA Clippers": "LAC", "Los Angeles Clippers": "LAC",
    "Los Angeles Lakers": "LAL", "Memphis Grizzlies": "MEM", "Miami Heat": "MIA",
    "Milwaukee Bucks": "MIL", "Minnesota Timberwolves": "MIN", "New Orleans Pelicans": "NOP",
    "New Orleans Hornets": "NOP", "New York Knicks": "NYK", "Oklahoma City Thunder": "OKC",
    "Seattle SuperSonics": "OKC", "Orlando Magic": "ORL", "Philadelphia 76ers": "PHI",
    "Phoenix Suns": "PHX", "Portland Trail Blazers": "POR", "Sacramento Kings": "SAC",
    "San Antonio Spurs": "SAS", "Toronto Raptors": "TOR", "Utah Jazz": "UTA", "Washington Wizards": "WAS",
}
SBR_NAMES = {
    "Hawks": "ATL", "Celtics": "BOS", "Nets": "BKN", "NewJersey": "BKN", "Hornets": "CHA", "Bulls": "CHI",
    "Cavaliers": "CLE", "Mavericks": "DAL", "Nuggets": "DEN", "Pistons": "DET", "Golden State": "GSW",
    "Warriors": "GSW", "Rockets": "HOU", "Pacers": "IND", "Clippers": "LAC", "LA Clippers": "LAC",
    "Lakers": "LAL", "Grizzlies": "MEM", "Heat": "MIA", "Bucks": "MIL", "Timberwolves": "MIN",
    "Pelicans": "NOP", "Knicks": "NYK", "Oklahoma City": "OKC", "Thunder": "OKC", "Magic": "ORL",
    "Seventysixers": "PHI", "Suns": "PHX", "Trailblazers": "POR", "Kings": "SAC", "Spurs": "SAS",
    "Raptors": "TOR", "Jazz": "UTA", "Wizards": "WAS",
}
# Tables in the closing-line database, by season; where a season has two, the
# one with real dates and the most games is used.
KYLESKOM_TABLES = [f"odds_{y}-{str(y + 1)[-2:]}_new" for y in range(2007, 2023)] + ["2023-24", "2024-25",
                                                                                    "odds_2025-26"]
# The last season whose spreads are stored without a sign.
UNSIGNED_THROUGH = "2022-06-30"


def _kyleskom(path) -> pd.DataFrame:
    con = sqlite3.connect(path)
    frames = []
    for table in KYLESKOM_TABLES:
        try:
            frames.append(pd.read_sql(f'select Date, Home, Away, OU, Spread, ML_Home, ML_Away from "{table}"', con))
        except Exception as exc:  # a table renamed upstream: skip it, the rest still loads
            log.warning("Odds table %s unavailable: %s", table, exc)
    con.close()
    k = pd.concat(frames, ignore_index=True)
    out = pd.DataFrame({
        "date": pd.to_datetime(k["Date"], errors="coerce").dt.strftime("%Y-%m-%d"),
        "home_team": k["Home"].map(FULL_NAMES), "away_team": k["Away"].map(FULL_NAMES),
        "total": pd.to_numeric(k["OU"], errors="coerce"),
        "spread": pd.to_numeric(k["Spread"], errors="coerce"),
        "home_moneyline": pd.to_numeric(k["ML_Home"], errors="coerce"),
        "away_moneyline": pd.to_numeric(k["ML_Away"], errors="coerce"),
    })
    unsigned = out["date"] <= UNSIGNED_THROUGH
    home_fav = out["home_moneyline"] < out["away_moneyline"]
    out.loc[unsigned, "spread"] = np.where(home_fav[unsigned], 1.0, -1.0) * out.loc[unsigned, "spread"].abs()
    ok = out["date"].notna() & out["home_team"].notna() & out["away_team"].notna()
    ok &= out["total"].between(150, 300) & out["spread"].abs().le(30)
    return out[ok].drop_duplicates(["date", "home_team", "away_team"], keep="last")


def _sbr(path) -> pd.DataFrame:
    s = pd.DataFrame(json.loads(path.read_text()))
    s = s[s["home_team"].astype(str).isin(SBR_NAMES) & s["away_team"].astype(str).isin(SBR_NAMES)].copy()
    num = {c: pd.to_numeric(s[c], errors="coerce") for c in ("home_open_spread", "home_close_spread", "open_over_under",
                                                            "close_over_under", "home_close_ml", "away_close_ml")}
    line, total = num["home_close_spread"], num["close_over_under"]
    swapped = line.abs().between(150, 300) & total.between(0, 30)
    fixed_line = np.where(swapped, np.sign(line) * total, line)
    fixed_total = np.where(swapped, line.abs(), total)
    out = pd.DataFrame({
        "date": pd.to_datetime(s["date"].astype(int).astype(str), format="%Y%m%d", errors="coerce")
        .dt.strftime("%Y-%m-%d"),
        "home_team": s["home_team"].astype(str).map(SBR_NAMES), "away_team": s["away_team"].astype(str).map(SBR_NAMES),
        "close_spread": -fixed_line, "close_total": fixed_total,
        "open_spread": -num["home_open_spread"], "open_total": num["open_over_under"],
        "close_home_ml": num["home_close_ml"], "close_away_ml": num["away_close_ml"],
    })
    for col, ok in (("close_spread", out["close_spread"].abs().le(30)), ("open_spread", out["open_spread"].abs().le(30)),
                    ("close_total", out["close_total"].between(150, 300)),
                    ("open_total", out["open_total"].between(150, 300))):
        out.loc[~ok, col] = np.nan
    return out.dropna(subset=["date"]).drop_duplicates(["date", "home_team", "away_team"], keep="last")


def build_lines(max_age_hours: float = 24.0 * 30) -> pd.DataFrame:
    """Download both archives and write ``data/lines.csv``."""
    k = _kyleskom(fetch(KYLESKOM_ODDS_URL, CACHE_DIR / "OddsData.sqlite", max_age_hours))
    s = _sbr(fetch(SBR_ARCHIVE_URL, CACHE_DIR / "nba_archive_10Y.json", max_age_hours))
    m = k.merge(s, on=["date", "home_team", "away_team"], how="outer")
    has_close = m["close_spread"].notna() & m["close_total"].notna()
    # Where the closing numbers exist, the other archive's spread and total are the opening ones.
    m["open_spread"] = m["open_spread"].where(m["open_spread"].notna(), m["spread"].where(has_close))
    m["open_total"] = m["open_total"].where(m["open_total"].notna(), m["total"].where(has_close))
    m["spread"] = m["close_spread"].where(has_close, m["spread"])
    m["total"] = m["close_total"].where(has_close, m["total"])
    m["home_moneyline"] = m["home_moneyline"].fillna(m["close_home_ml"])
    m["away_moneyline"] = m["away_moneyline"].fillna(m["close_away_ml"])
    lines = m.sort_values(["date", "home_team"])[LINE_COLUMNS]
    LINES_PATH.parent.mkdir(parents=True, exist_ok=True)
    lines.to_csv(LINES_PATH, index=False)
    log.info("Wrote %d games of lines (%d with closing spreads from sportsbookreview, %d with opening spreads)",
             len(lines), int(has_close.sum()), int(lines["open_spread"].notna().sum()))
    return lines


def load_lines() -> pd.DataFrame:
    if not LINES_PATH.exists():
        return pd.DataFrame(columns=LINE_COLUMNS)
    return pd.read_csv(LINES_PATH)


def attach_lines(games: pd.DataFrame, lines: pd.DataFrame) -> pd.DataFrame:
    """Add historical lines to ``games`` by date and teams, allowing the
    archive's date to be a day off (late games are sometimes filed under the
    next day)."""
    out = games.copy()
    cols = [c for c in LINE_COLUMNS if c not in ("date", "home_team", "away_team")]
    for col in cols:
        out[col] = np.nan
    if lines.empty:
        return out
    keyed = lines.set_index(["date", "home_team", "away_team"])
    keyed = keyed[~keyed.index.duplicated(keep="last")]
    dates = pd.to_datetime(out["date"])
    for shift in (0, 1, -1):
        need = out["spread"].isna() & out["open_spread"].isna()
        if not need.any():
            break
        keys = pd.MultiIndex.from_arrays([(dates + pd.Timedelta(days=shift)).dt.strftime("%Y-%m-%d"),
                                          out["home_team"], out["away_team"]])
        found = keyed.reindex(keys)
        for col in cols:
            vals = found[col].to_numpy()
            out[col] = np.where(need & pd.isna(out[col]), vals, out[col])
    return out
