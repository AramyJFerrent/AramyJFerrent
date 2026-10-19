"""Betting lines, injury reports and rosters for upcoming games, from ESPN.

ESPN's public endpoints need no key:

- The scoreboard lists, for each game, the line from its odds provider: the
  spread, the total and both moneylines, with the opening numbers once the
  closing ones exist. One request per game day.
- The injury report lists every player each team has reported, with a status
  (out, doubtful, questionable, probable or day-to-day). One request.
- Each team's roster lists its current players, so trades and signings count
  from the day they happen. One request per team.

Any failure leaves the affected games without a line, or teams without
injury news, and the prediction falls back to the model alone and to the
players who played the team's recent games.
"""

from __future__ import annotations

import logging
import re

import numpy as np
import pandas as pd
import requests

from .config import DISPLAY_TZ, TEAM_ALIASES

log = logging.getLogger(__name__)

BASE = "https://site.api.espn.com/apis/site/v2/sports/basketball/nba"
SCOREBOARD = BASE + "/scoreboard"
INJURIES = BASE + "/injuries"
ROSTER = BASE + "/teams/{team_id}/roster"
COLUMNS = ["date", "start", "home_team", "away_team", "spread", "total", "home_moneyline", "away_moneyline",
           "open_spread", "open_total", "line_source"]
NUMERIC = ["spread", "total", "home_moneyline", "away_moneyline", "open_spread", "open_total"]
INJURY_COLUMNS = ["team", "player_id", "name", "status", "detail", "return_date"]
ROSTER_COLUMNS = ["team", "player_id", "name", "position", "status"]


def _num(x) -> float:
    if isinstance(x, str):
        x = x.strip().lower()
        if x in ("even", "ev", "pk", "pick"):
            return 0.0 if x in ("pk", "pick") else 100.0
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


def team_code(code) -> str:
    code = str(code or "").upper()
    return TEAM_ALIASES.get(code, code)


def _price(odds: dict, side: str, when: str = "close") -> float:
    """A side's moneyline: the current format nests open and close prices
    under ``moneyline``; the older one puts it on the team odds."""
    paths = [("moneyline", side, when, "odds")]
    if when == "close":
        paths += [("moneyline", side, "current", "odds"), (f"{side}TeamOdds", "moneyLine")]
    for path in paths:
        v = _num(_dig(odds, *path))
        if not np.isnan(v):
            return v
    return np.nan


def _home_spread(odds: dict, home: str, away: str, when: str = "close") -> float:
    """The home team's expected margin: minus its point spread. The spread is
    read from the point-spread block, else ESPN's ``spread`` field (the home
    team's line); ``details`` ("BOS -5.5") names the favorite and settles the sign."""
    line = _num(_dig(odds, "pointSpread", "home", when, "line"))
    if np.isnan(line) and when == "close":
        line = _num(_dig(odds, "pointSpread", "home", "current", "line"))
        if np.isnan(line):
            line = _num(odds.get("spread"))
    if when == "open" and np.isnan(line):
        return np.nan
    details = str(odds.get("details") or "").strip()
    match = re.match(r"^([A-Za-z]+)\s+([+-]?\d+(?:\.\d+)?)$", details)
    if match and when == "close":
        fav, size = team_code(match.group(1)), abs(float(match.group(2)))
        if fav == home:
            return size
        if fav == away:
            return -size
    if details.upper() in ("EVEN", "PK", "PICK"):
        return 0.0
    return -line if not np.isnan(line) else np.nan


def _total(odds: dict, when: str = "close") -> float:
    line = _num(_dig(odds, "total", "over", when, "line"))
    if np.isnan(line) and when == "close":
        line = _num(odds.get("overUnder"))
    return line


def parse_scoreboard(payload: dict) -> pd.DataFrame:
    rows = []
    for event in payload.get("events") or []:
        comp = (event.get("competitions") or [{}])[0]
        sides = {c.get("homeAway"): c for c in comp.get("competitors") or []}
        if "home" not in sides or "away" not in sides:
            continue
        start = pd.to_datetime(event.get("date") or comp.get("date"), utc=True, errors="coerce")
        home = team_code(_dig(sides["home"], "team", "abbreviation"))
        away = team_code(_dig(sides["away"], "team", "abbreviation"))
        row = {"date": start.tz_convert(DISPLAY_TZ).date() if not pd.isna(start) else None, "start": start,
               "home_team": home, "away_team": away}
        odds = (comp.get("odds") or [None])[0] or {}
        row["spread"] = _home_spread(odds, home, away) if odds else np.nan
        row["total"] = _total(odds) if odds else np.nan
        row["home_moneyline"] = _price(odds, "home")
        row["away_moneyline"] = _price(odds, "away")
        row["open_spread"] = _home_spread(odds, home, away, "open") if odds else np.nan
        row["open_total"] = _total(odds, "open") if odds else np.nan
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


def attach_lines(games: pd.DataFrame, board: pd.DataFrame) -> pd.DataFrame:
    """Add lines from ``board`` to upcoming ``games``, matching date and teams."""
    out = games.copy()
    for col in NUMERIC:
        out[col] = np.nan
    out["line_source"] = None
    if board.empty:
        return out
    key = board.drop_duplicates(["date", "home_team", "away_team"]).set_index(["date", "home_team", "away_team"])
    for idx, g in out.iterrows():
        k = (g["date"], g["home_team"], g["away_team"])
        if k in key.index:
            for col in NUMERIC + ["line_source"]:
                out.at[idx, col] = key.at[k, col]
    log.info("ESPN lines for %d of %d games", int(out["spread"].notna().sum()), len(out))
    return out


# ---- injuries and rosters ------------------------------------------------

def _athlete_id(athlete: dict) -> int | None:
    for value in (athlete.get("id"), athlete.get("uid")):
        if value:
            m = re.search(r"(\d+)$", str(value))
            if m:
                return int(m.group(1))
    for link in athlete.get("links") or []:
        m = re.search(r"/id/(\d+)", str(link.get("href", "")))
        if m:
            return int(m.group(1))
    return None


def parse_injuries(payload: dict, team_ids: dict[str, str]) -> pd.DataFrame:
    """One row per reported player. ``team_ids`` maps ESPN team ids to team codes."""
    rows = []
    for block in payload.get("injuries") or []:
        team = team_ids.get(str(block.get("id")))
        for item in block.get("injuries") or []:
            athlete = item.get("athlete") or {}
            code = team or team_code(_dig(athlete, "team", "abbreviation"))
            status = item.get("status") or _dig(item, "type", "description") or _dig(item, "type", "name")
            rows.append({
                "team": code, "player_id": _athlete_id(athlete), "name": athlete.get("displayName"),
                "status": str(status or ""),
                "detail": item.get("shortComment") or _dig(item, "details", "type"),
                "return_date": _dig(item, "details", "returnDate"),
            })
    return pd.DataFrame(rows, columns=INJURY_COLUMNS)


def fetch_injuries(team_ids: dict[str, str], session: requests.Session | None = None) -> pd.DataFrame | None:
    """The league-wide injury report, or None when it cannot be read."""
    session = session or requests.Session()
    try:
        resp = session.get(INJURIES, timeout=30)
        resp.raise_for_status()
        return parse_injuries(resp.json(), team_ids)
    except (requests.RequestException, ValueError, KeyError, TypeError, AttributeError) as exc:
        log.warning("ESPN injury report failed: %s", exc)
        return None


def parse_roster(payload: dict, team: str) -> tuple[pd.DataFrame, pd.DataFrame]:
    """A team's current players, and any injury status listed with them."""
    rows, hurt = [], []
    athletes = payload.get("athletes") or []
    # Some responses group players by position.
    if athletes and isinstance(athletes[0], dict) and "items" in athletes[0]:
        athletes = [a for group in athletes for a in group.get("items") or []]
    for a in athletes:
        pid = _athlete_id(a)
        if pid is None:
            continue
        rows.append({"team": team, "player_id": pid, "name": a.get("displayName") or a.get("fullName"),
                     "position": _dig(a, "position", "abbreviation"),
                     "status": _dig(a, "status", "type") or _dig(a, "status", "name")})
        for inj in a.get("injuries") or []:
            status = inj.get("status") or _dig(inj, "type", "description")
            if status:
                hurt.append({"team": team, "player_id": pid, "name": rows[-1]["name"], "status": str(status),
                             "detail": _dig(inj, "details", "type"), "return_date": _dig(inj, "details", "returnDate")})
                break
    return pd.DataFrame(rows, columns=ROSTER_COLUMNS), pd.DataFrame(hurt, columns=INJURY_COLUMNS)


def fetch_rosters(team_ids: dict[str, str], session: requests.Session | None = None):
    """Current rosters (and roster-listed injuries) for every team; teams that
    fail are left out with a warning."""
    session = session or requests.Session()
    rosters, hurt, errors = [], [], []
    for espn_id, team in sorted(team_ids.items(), key=lambda kv: kv[1]):
        try:
            resp = session.get(ROSTER.format(team_id=espn_id), timeout=30)
            resp.raise_for_status()
            r, h = parse_roster(resp.json(), team)
            rosters.append(r)
            hurt.append(h)
        except (requests.RequestException, ValueError, KeyError, TypeError, AttributeError) as exc:
            errors.append(f"{team}: {exc}")
    if errors:
        log.warning("ESPN rosters failed for %d team(s): %s", len(errors), "; ".join(errors[:3]))
    roster = pd.concat([r for r in rosters if len(r)], ignore_index=True) if any(len(r) for r in rosters) \
        else pd.DataFrame(columns=ROSTER_COLUMNS)
    injuries = pd.concat([h for h in hurt if len(h)], ignore_index=True) if any(len(h) for h in hurt) \
        else pd.DataFrame(columns=INJURY_COLUMNS)
    return roster, injuries
