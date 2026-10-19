"""The season in progress from the MLB Stats API.

MLB's public data service (statsapi.mlb.com, no key needed) gives the
schedule with line scores, probable pitchers, posted lineups and weather, and
a box score for every game. Each update reads the season's schedule in one
request, then the box scores of games finished since the last run (the first
run of a season reads them all), and writes the same summary files as the
Retrosheet seasons: games, batting and pitching. Box scores carry no
play-by-play, so these seasons have no base-out transition or platoon tables;
the simulator and platoon factors use the latest Retrosheet seasons instead.
"""

from __future__ import annotations

import concurrent.futures as cf
import logging
import re
import time

import numpy as np
import pandas as pd
import requests

from .config import GAME_TYPES, GHOST_RUNNER_SEASON, MLB_TEAM_IDS, PARK_MOVES, STATSAPI_URL

log = logging.getLogger(__name__)

SCHEDULE_URL = STATSAPI_URL + "/schedule"
BOXSCORE_URL = STATSAPI_URL + "/game/{pk}/boxscore"
PEOPLE_URL = STATSAPI_URL + "/people"
SEASON_HYDRATE = "probablePitcher,linescore,venue,weather"
UPCOMING_HYDRATE = "probablePitcher,lineups,venue,weather"
DONE_STATES = {"Postponed", "Cancelled", "Canceled"}
ROOF_CONDITIONS = {"dome", "roof closed"}
WORKERS = 8


def get_json(url: str, params: dict | None = None, session: requests.Session | None = None,
             retries: int = 4) -> dict:
    getter = session or requests
    delay = 2.0
    for attempt in range(retries):
        try:
            resp = getter.get(url, params=params, timeout=60)
            resp.raise_for_status()
            return resp.json()
        except (requests.RequestException, ValueError) as exc:
            if attempt == retries - 1:
                raise
            log.warning("MLB Stats API request %s failed (%s); retrying in %.0fs", url, exc, delay)
            time.sleep(delay)
            delay *= 2
    return {}


def _dig(d, *keys):
    for k in keys:
        if not isinstance(d, dict):
            return None
        d = d.get(k)
    return d


def _team(side: dict) -> str | None:
    return MLB_TEAM_IDS.get(_dig(side, "team", "id"))


def _status(game: dict) -> str:
    st = game.get("status") or {}
    detailed = str(st.get("detailedState") or "")
    if detailed in DONE_STATES:
        return "postponed"
    if detailed.startswith("Suspended"):
        return "suspended"
    abstract = st.get("abstractGameState")
    if abstract == "Final":
        return "final"
    if abstract == "Live":
        return "live"
    return "scheduled"


def _line(linescore: dict, side: str, final: bool) -> str | None:
    """Runs by inning (``"0 1 0 x"``) once the game is final."""
    innings = (linescore or {}).get("innings") or []
    if not innings:
        return None
    parts = []
    for inn in innings:
        runs = _dig(inn, side, "runs")
        parts.append(str(int(runs)) if runs is not None else "x")
    return " ".join(parts) if final else None


def parse_weather(weather: dict | None) -> dict:
    """Temperature, roof and wind from ``{"condition": "Partly Cloudy", "temp": "72",
    "wind": "8 mph, Out To CF"}``."""
    weather = weather or {}
    condition = str(weather.get("condition") or "").strip().lower()
    temp = pd.to_numeric(str(weather.get("temp") or "").strip(), errors="coerce")
    wind_text = str(weather.get("wind") or "").lower()
    speed = re.match(r"\s*(\d+)\s*mph", wind_text)
    if "out to" in wind_text:
        wind = "out"
    elif "in from" in wind_text:
        wind = "in"
    elif "l to r" in wind_text or "r to l" in wind_text:
        wind = "cross"
    elif "calm" in wind_text or "none" in wind_text:
        wind = "none"
    else:
        wind = None
    return {"temp": float(temp) if pd.notna(temp) else np.nan,
            "dome": int(condition in ROOF_CONDITIONS) if condition else np.nan,
            "wind": wind, "wind_speed": float(speed.group(1)) if speed else np.nan}


def parse_schedule(payload: dict) -> pd.DataFrame:
    """One row per game in the predictor's game format, plus venue, probable
    pitchers and posted lineups."""
    rows = []
    for day in payload.get("dates") or []:
        for g in day.get("games") or []:
            home, away = (g.get("teams") or {}).get("home") or {}, (g.get("teams") or {}).get("away") or {}
            if _team(home) is None or _team(away) is None or g.get("gameType") not in GAME_TYPES:
                continue
            status = _status(g)
            final = status == "final"
            ls = g.get("linescore") or {}
            season = int(g.get("season") or str(g.get("officialDate", "0"))[:4])
            weather = parse_weather(g.get("weather"))
            row = {
                "game_id": str(g.get("gamePk")), "season": season, "game_type": g.get("gameType"),
                "date": g.get("officialDate") or str(day.get("date")),
                "start": pd.Timestamp(g.get("gameDate")).isoformat() if g.get("gameDate") else None,
                "game_number": int(g.get("gameNumber") or 1) if g.get("doubleHeader") in ("Y", "S") else 0,
                "home_team": _team(home), "away_team": _team(away), "status": status,
                "home_score": home.get("score") if final else np.nan,
                "away_score": away.get("score") if final else np.nan,
                "innings": ls.get("currentInning") if final else np.nan,
                "sched_innings": ls.get("scheduledInnings") or g.get("scheduledInnings") or 9,
                "tiebreaker": int(g.get("gameType") == "R" and season >= GHOST_RUNNER_SEASON),
                "venue_id": _dig(g, "venue", "id"), "venue_name": _dig(g, "venue", "name"),
                "daynight": g.get("dayNight"), **weather,
                "home_starter": _dig(home, "probablePitcher", "id"),
                "away_starter": _dig(away, "probablePitcher", "id"),
                "home_starter_name": _dig(home, "probablePitcher", "fullName"),
                "away_starter_name": _dig(away, "probablePitcher", "fullName"),
                "home_line": _line(ls, "home", final), "away_line": _line(ls, "away", final),
                "htbf": int(bool(g.get("reverseHomeAwayStatus"))), "source": "statsapi",
            }
            lineups = g.get("lineups") or {}
            for side, key in (("home", "homePlayers"), ("away", "awayPlayers")):
                players = lineups.get(key) or []
                row[f"{side}_lineup_ids"] = [str(p.get("id")) for p in players if p.get("id")]
                row[f"{side}_lineup_pos"] = [str(_dig(p, "primaryPosition", "code") or "") for p in players]
            rows.append(row)
    out = pd.DataFrame(rows)
    if out.empty:
        return out
    for col in ("home_starter", "away_starter"):
        out[col] = out[col].map(lambda x: str(int(x)) if pd.notna(x) else None)
    # A postponed game reappears on its new date under the same id: keep one row,
    # the played one when there is one.
    rank = out["status"].map({"final": 0, "live": 1, "suspended": 2, "scheduled": 3, "postponed": 4})
    out = out.assign(_r=rank).sort_values(["game_id", "_r", "date"], ascending=[True, True, False])
    return out.drop_duplicates("game_id").drop(columns="_r").reset_index(drop=True)


def fetch_schedule(start, end, hydrate: str = SEASON_HYDRATE, session: requests.Session | None = None) -> pd.DataFrame:
    params = {"sportId": 1, "startDate": str(start), "endDate": str(end), "gameType": ",".join(GAME_TYPES),
              "hydrate": hydrate}
    return parse_schedule(get_json(SCHEDULE_URL, params, session))


def _stat(stats: dict, *keys) -> int:
    for k in keys:
        v = stats.get(k)
        if v is not None:
            try:
                return int(v)
            except (TypeError, ValueError):
                continue
    return 0


def parse_boxscore(payload: dict, game_id: str) -> dict:
    """Batting and pitching rows, the starting pitchers and the weather from one box score."""
    batting, pitching, starters = [], [], {}
    teams = payload.get("teams") or {}
    for side in ("home", "away"):
        t = teams.get(side) or {}
        team = _team(t)
        players = t.get("players") or {}
        for pl in players.values():
            pid = _dig(pl, "person", "id")
            stats = _dig(pl, "stats", "batting") or {}
            order = str(pl.get("battingOrder") or "")
            slot = int(order) // 100 if order.isdigit() and int(order) % 100 == 0 else 0
            pa = _stat(stats, "plateAppearances")
            if pid is None or (pa == 0 and slot == 0):
                continue
            k, bb, ibb, hbp = (_stat(stats, "strikeOuts"), _stat(stats, "baseOnBalls"),
                               _stat(stats, "intentionalWalks"), _stat(stats, "hitByPitch"))
            d, tr, hr = _stat(stats, "doubles"), _stat(stats, "triples"), _stat(stats, "homeRuns")
            s = _stat(stats, "hits") - d - tr - hr
            code = str(_dig(pl, "position", "code") or "")
            batting.append({"game_id": game_id, "team": team, "player_id": str(pid), "slot": slot,
                            "pos": int(code) if code.isdigit() else 0, "pa": pa, "k": k, "bb": bb, "ibb": ibb,
                            "hbp": hbp, "s": s, "d": d, "t": tr, "hr": hr,
                            "out": max(pa - (k + bb + hbp + s + d + tr + hr), 0)})
        for seq, pid in enumerate(t.get("pitchers") or []):
            stats = _dig(players, f"ID{pid}", "stats", "pitching") or {}
            d, tr, hr = _stat(stats, "doubles"), _stat(stats, "triples"), _stat(stats, "homeRuns")
            row = {"game_id": game_id, "team": team, "player_id": str(pid), "starter": int(seq == 0), "seq": seq,
                   "outs": _stat(stats, "outs"), "bf": _stat(stats, "battersFaced"),
                   "pitches": _stat(stats, "numberOfPitches", "pitchesThrown"), "k": _stat(stats, "strikeOuts"),
                   "bb": _stat(stats, "baseOnBalls"), "ibb": _stat(stats, "intentionalWalks"),
                   "hbp": _stat(stats, "hitByPitch", "hitBatsmen"), "s": _stat(stats, "hits") - d - tr - hr,
                   "d": d, "t": tr, "hr": hr, "r": _stat(stats, "runs"), "er": _stat(stats, "earnedRuns")}
            row["out"] = max(row["bf"] - sum(row[e] for e in ("k", "bb", "hbp", "s", "d", "t", "hr")), 0)
            pitching.append(row)
            if seq == 0:
                starters[side] = str(pid)
    info = {str(i.get("label")): str(i.get("value") or "") for i in payload.get("info") or [] if i.get("label")}
    weather = {}
    m = re.match(r"\s*(-?\d+)\s*degrees,?\s*(.*?)\.?\s*$", info.get("Weather", ""))
    if m:
        weather = parse_weather({"temp": m.group(1), "condition": m.group(2), "wind": info.get("Wind", "")})
    return {"batting": batting, "pitching": pitching, "starters": starters, "weather": weather}


def fetch_boxscores(game_ids, session: requests.Session | None = None) -> dict[str, dict]:
    """Parsed box scores by game id; games that fail are left out with a warning."""
    session = session or requests.Session()
    out, errors = {}, []

    def one(gid):
        return gid, parse_boxscore(get_json(BOXSCORE_URL.format(pk=gid), session=session), gid)

    with cf.ThreadPoolExecutor(max_workers=WORKERS) as pool:
        futures = [pool.submit(one, gid) for gid in game_ids]
        for fut in cf.as_completed(futures):
            try:
                gid, parsed = fut.result()
                out[gid] = parsed
            except (requests.RequestException, ValueError, KeyError, TypeError) as exc:
                errors.append(str(exc))
    if errors:
        log.warning("%d box scores failed: %s", len(errors), "; ".join(errors[:3]))
    return out


def fetch_people(ids, session: requests.Session | None = None) -> pd.DataFrame:
    """Name, batting side, throwing hand and birth year for MLB player ids."""
    ids = [str(i) for i in ids if i]
    rows = []
    for chunk in range(0, len(ids), 150):
        try:
            payload = get_json(PEOPLE_URL, {"personIds": ",".join(ids[chunk:chunk + 150])}, session)
        except (requests.RequestException, ValueError) as exc:
            log.warning("Player lookup failed: %s", exc)
            continue
        for p in payload.get("people") or []:
            birth = str(p.get("birthDate") or "")[:4]
            rows.append({"player_id": str(p.get("id")), "name": p.get("fullName"),
                         "bats": _dig(p, "batSide", "code"), "throws": _dig(p, "pitchHand", "code"),
                         "birth_year": int(birth) if birth.isdigit() else None, "retro_id": None})
    return pd.DataFrame(rows, columns=["player_id", "name", "bats", "throws", "birth_year", "retro_id"])


def assign_parks(games: pd.DataFrame, history: pd.DataFrame) -> pd.Series:
    """Retrosheet-style park ids for MLB API games, so park factors carry over.

    Each team's usual venue this season is taken to be the park it used most
    in the latest earlier season (or the park in ``PARK_MOVES`` when it has
    moved since); other venues (London, Mexico City and the like) keep an id
    of their own.
    """
    out = pd.Series([f"MLB{v}" if pd.notna(v) else None for v in games["venue_id"]], index=games.index, dtype=object)
    if games.empty:
        return out
    usual = games.groupby(["season", "home_team"])["venue_id"].agg(
        lambda s: s.mode().iloc[0] if s.notna().any() else None)
    hist = history[history["park_id"].notna() & ~history["park_id"].astype(str).str.startswith("MLB")]
    for idx, g in games.iterrows():
        team, season = g["home_team"], int(g["season"])
        if pd.isna(g["venue_id"]) or g["venue_id"] != usual.get((season, team)):
            continue
        moves = {s: p for s, p in PARK_MOVES.get(team, {}).items() if s <= season}
        before = hist[(hist["home_team"] == team) & (hist["season"] < season)]
        if moves and (before.empty or max(moves) > int(before["season"].max())):
            out[idx] = moves[max(moves)]
        elif len(before):
            last = before[before["season"] == before["season"].max()]
            out[idx] = last["park_id"].mode().iloc[0]
    return out
