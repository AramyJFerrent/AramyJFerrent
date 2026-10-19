"""Betting lines for upcoming games, from ESPN's public scoreboard.

ESPN's scoreboard needs no key and lists, for each game, the line from its
odds provider: moneylines, the total and the run line. One request per game
day. Any failure leaves the affected games without a line, and the
prediction falls back to the model alone.
"""

from __future__ import annotations

import logging
import re

import numpy as np
import pandas as pd
import requests

from .config import DISPLAY_TZ

log = logging.getLogger(__name__)

SCOREBOARD = "https://site.api.espn.com/apis/site/v2/sports/baseball/mlb/scoreboard"
# ESPN abbreviations that differ from the predictor's.
ESPN_TEAMS = {"CHW": "CWS", "OAK": "ATH", "AZ": "ARI", "WAS": "WSH", "SDP": "SD", "SFG": "SF", "TBR": "TB",
              "KCR": "KC", "LV": "ATH"}
COLUMNS = ["date", "start", "home_team", "away_team", "home_moneyline", "away_moneyline", "total_line",
           "over_price", "under_price", "line_source"]
NUMERIC = ["home_moneyline", "away_moneyline", "total_line", "over_price", "under_price"]


def _num(x) -> float:
    if isinstance(x, str):
        x = x.strip().lower()
        if x in ("even", "ev"):
            return 100.0
        x = re.sub(r"^[ou]", "", x)
    try:
        v = float(x)
    except (TypeError, ValueError):
        return np.nan
    return v if np.isfinite(v) else np.nan


def _dig(d, *keys):
    for k in keys:
        if not isinstance(d, dict):
            return None
        d = d.get(k)
    return d


def _price(odds: dict, side: str) -> float:
    """A side's moneyline: the current format nests open and close prices
    under ``moneyline``; the older one puts it on the team odds."""
    for path in (("moneyline", side, "close", "odds"), ("moneyline", side, "current", "odds"),
                 (f"{side}TeamOdds", "moneyLine"), ("moneyline", side, "open", "odds")):
        v = _num(_dig(odds, *path))
        if not np.isnan(v):
            return v
    return np.nan


def _total(odds: dict) -> tuple[float, float, float]:
    line = _num(odds.get("overUnder"))
    if np.isnan(line):
        line = _num(_dig(odds, "total", "over", "close", "line"))
    over = _num(_dig(odds, "total", "over", "close", "odds"))
    under = _num(_dig(odds, "total", "under", "close", "odds"))
    if np.isnan(over):
        over, under = _num(odds.get("overOdds")), _num(odds.get("underOdds"))
    return line, over, under


def _team(code) -> str:
    code = str(code or "").upper()
    return ESPN_TEAMS.get(code, code)


def parse_scoreboard(payload: dict) -> pd.DataFrame:
    rows = []
    for event in payload.get("events") or []:
        comp = (event.get("competitions") or [{}])[0]
        sides = {c.get("homeAway"): c for c in comp.get("competitors") or []}
        if "home" not in sides or "away" not in sides:
            continue
        start = pd.to_datetime(event.get("date") or comp.get("date"), utc=True, errors="coerce")
        row = {"date": start.tz_convert(DISPLAY_TZ).date() if not pd.isna(start) else None, "start": start,
               "home_team": _team(_dig(sides["home"], "team", "abbreviation")),
               "away_team": _team(_dig(sides["away"], "team", "abbreviation"))}
        odds = (comp.get("odds") or [None])[0] or {}
        row["home_moneyline"] = _price(odds, "home")
        row["away_moneyline"] = _price(odds, "away")
        row["total_line"], row["over_price"], row["under_price"] = _total(odds)
        provider = _dig(odds, "provider", "name")
        row["line_source"] = ("ESPN" + (f" ({provider})" if provider else "")) if odds else None
        rows.append(row)
    out = pd.DataFrame(rows, columns=COLUMNS)
    out[NUMERIC] = out[NUMERIC].astype(float)
    return out


def fetch_scoreboards(dates, session: requests.Session | None = None) -> pd.DataFrame:
    """Scoreboard rows for each ET date; days that fail are skipped with a warning."""
    session = session or requests.Session()
    frames, errors = [], []
    for day in sorted(set(dates)):
        try:
            resp = session.get(SCOREBOARD, params={"dates": pd.Timestamp(day).strftime("%Y%m%d")}, timeout=30)
            resp.raise_for_status()
            frames.append(parse_scoreboard(resp.json()))
        except (requests.RequestException, ValueError, KeyError, TypeError, AttributeError) as exc:
            errors.append(f"{day}: {exc}")
    if errors:
        log.warning("ESPN scoreboard failed for %d day(s): %s", len(errors), "; ".join(errors[:3]))
    frames = [f for f in frames if len(f)]
    if not frames:
        return pd.DataFrame(columns=COLUMNS).astype({c: float for c in NUMERIC})
    return pd.concat(frames, ignore_index=True)


def attach(games: pd.DataFrame, board: pd.DataFrame) -> pd.DataFrame:
    """Add lines from ``board`` to upcoming ``games``, matching teams and date,
    and the nearest start time for doubleheaders."""
    out = games.copy()
    for col in NUMERIC:
        out[col] = np.nan
    out["line_source"] = None
    if board.empty:
        return out
    used = set()
    for idx, g in out.iterrows():
        cand = board[(board["date"] == g["date"]) & (board["home_team"] == g["home_team"])
                     & (board["away_team"] == g["away_team"])]
        cand = cand[~cand.index.isin(used)]
        if cand.empty:
            continue
        if len(cand) > 1 and pd.notna(g.get("start")):
            gap = (cand["start"] - pd.Timestamp(g["start"])).abs()
            row = cand.loc[gap.idxmin()]
        else:
            row = cand.iloc[0]
        used.add(row.name)
        for col in NUMERIC + ["line_source"]:
            out.at[idx, col] = row[col]
    log.info("ESPN lines for %d of %d games", int(out["home_moneyline"].notna().sum()), len(out))
    return out
