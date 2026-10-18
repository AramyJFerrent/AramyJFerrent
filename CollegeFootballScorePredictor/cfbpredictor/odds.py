"""Current betting lines for upcoming games.

Two sources, tried in order:

1. CollegeFootballData (CFBD) lines, the median across its books, when a
   ``CFBD_API_KEY`` environment variable is set (free keys allow 1,000 calls a
   month; each update uses one or two).
2. ESPN's public scoreboard, which needs no key and lists the line ESPN
   shows for every FBS game.

Game ids are shared by cfbfastR, CFBD and ESPN, so lines join on them
directly. Any failure leaves the affected games without a line, and the
prediction falls back to the model alone.
"""

from __future__ import annotations

import logging
import os
import re

import numpy as np
import pandas as pd
import requests

log = logging.getLogger(__name__)

ESPN_SCOREBOARD = "https://site.api.espn.com/apis/site/v2/sports/football/college-football/scoreboard"
CFBD_LINES = "https://api.collegefootballdata.com/lines"
FBS_GROUP = "80"
ODDS_COLUMNS = ["game_id", "spread_line", "total_line", "home_moneyline", "away_moneyline", "line_source"]


def _num(x) -> float:
    try:
        v = float(x)
    except (TypeError, ValueError):
        return np.nan
    return v if np.isfinite(v) else np.nan


def _espn_home_margin(odds: dict, home_abbr: str, away_abbr: str) -> float:
    """Expected home margin from one ESPN odds entry (positive = home favored)."""
    details = str(odds.get("details") or "").strip()
    if details.upper() in ("EVEN", "PK", "PICK", "PICK'EM"):
        return 0.0
    size = abs(_num(odds.get("spread")))
    match = re.match(r"^(\S+)\s+([+-]?\d+(?:\.\d+)?)$", details)
    if np.isnan(size) and match:
        size = abs(float(match.group(2)))
    if np.isnan(size):
        return np.nan
    home_fav = (odds.get("homeTeamOdds") or {}).get("favorite")
    away_fav = (odds.get("awayTeamOdds") or {}).get("favorite")
    if home_fav is True:
        return size
    if away_fav is True:
        return -size
    if match:
        team = match.group(1)
        if team == home_abbr:
            return size
        if team == away_abbr:
            return -size
    # ESPN's spread number is the home team's line: negative when it is favored.
    raw = _num(odds.get("spread"))
    return -raw if not np.isnan(raw) else np.nan


def parse_espn(payload: dict) -> pd.DataFrame:
    rows = []
    for event in payload.get("events") or []:
        comps = event.get("competitions") or [{}]
        comp = comps[0]
        teams = {c.get("homeAway"): (c.get("team") or {}) for c in comp.get("competitors") or []}
        odds_list = comp.get("odds") or []
        if not odds_list or "home" not in teams or "away" not in teams:
            continue
        odds = odds_list[0]
        home, away = teams["home"], teams["away"]
        rows.append({
            "game_id": int(event.get("id") or comp.get("id")),
            "spread_line": _espn_home_margin(odds, home.get("abbreviation", ""), away.get("abbreviation", "")),
            "total_line": _num(odds.get("overUnder")),
            "home_moneyline": _num((odds.get("homeTeamOdds") or {}).get("moneyLine")),
            "away_moneyline": _num((odds.get("awayTeamOdds") or {}).get("moneyLine")),
            "line_source": "ESPN" + (f" ({odds['provider']['name']})" if (odds.get("provider") or {}).get("name") else ""),
        })
    return pd.DataFrame(rows, columns=ODDS_COLUMNS)


def parse_cfbd(payload: list) -> pd.DataFrame:
    rows = []
    for game in payload or []:
        books = game.get("lines") or []
        spread = [-_num(b.get("spread")) for b in books]      # CFBD spreads are the home line
        total = [_num(b.get("overUnder")) for b in books]
        home_ml = [_num(b.get("homeMoneyline")) for b in books]
        away_ml = [_num(b.get("awayMoneyline")) for b in books]

        def median(values):
            v = [x for x in values if not np.isnan(x)]
            return float(np.median(v)) if v else np.nan
        rows.append({"game_id": int(game["id"]), "spread_line": median(spread), "total_line": median(total),
                     "home_moneyline": median(home_ml), "away_moneyline": median(away_ml),
                     "line_source": f"CFBD ({len(books)} books)"})
    return pd.DataFrame(rows, columns=ODDS_COLUMNS)


def _espn_lines(games: pd.DataFrame, session: requests.Session) -> pd.DataFrame:
    """One scoreboard request per game day (ESPN rejects date ranges for college)."""
    days = sorted(set(games["kickoff"].dropna().dt.tz_convert("America/New_York").dt.strftime("%Y%m%d")))
    frames, errors = [], []
    for day in days:
        try:
            resp = session.get(ESPN_SCOREBOARD, params={"dates": day, "groups": FBS_GROUP, "limit": 300},
                               timeout=30)
            resp.raise_for_status()
            frames.append(parse_espn(resp.json()))
        except requests.ConnectionError:
            raise
        except (requests.RequestException, ValueError) as exc:
            errors.append(f"{day}: {exc}")
    if errors:
        log.warning("ESPN scoreboard failed for %d of %d days: %s", len(errors), len(days), "; ".join(errors[:3]))
    if not frames:
        return pd.DataFrame(columns=ODDS_COLUMNS)
    return pd.concat(frames, ignore_index=True).drop_duplicates("game_id")


def _cfbd_lines(games: pd.DataFrame, session: requests.Session, key: str) -> pd.DataFrame:
    frames = []
    for (season, kind), _ in games.groupby(["season", "season_type"]):
        resp = session.get(CFBD_LINES, params={"year": int(season), "seasonType": kind},
                           headers={"Authorization": f"Bearer {key}"}, timeout=30)
        resp.raise_for_status()
        frames.append(parse_cfbd(resp.json()))
    return pd.concat(frames, ignore_index=True) if frames else pd.DataFrame(columns=ODDS_COLUMNS)


def live_lines(games: pd.DataFrame, session: requests.Session | None = None) -> pd.DataFrame:
    """Current lines for ``games`` (upcoming), best source first; empty on failure."""
    session = session or requests.Session()
    found = []
    key = os.environ.get("CFBD_API_KEY", "").strip()
    sources = ([("CFBD", lambda: _cfbd_lines(games, session, key))] if key else []) + \
        [("ESPN", lambda: _espn_lines(games, session))]
    for name, get in sources:
        try:
            lines = get()
        except (requests.RequestException, ValueError, KeyError, TypeError) as exc:
            log.warning("No lines from %s: %s", name, exc)
            continue
        lines = lines[lines["game_id"].isin(set(games["game_id"]))]
        lines = lines[lines["spread_line"].notna() | lines["total_line"].notna()]
        log.info("%s lines for %d of %d games", name, len(lines), len(games))
        found.append(lines)
    if not found:
        return pd.DataFrame(columns=ODDS_COLUMNS)
    return pd.concat(found, ignore_index=True).drop_duplicates("game_id", keep="first").reset_index(drop=True)
