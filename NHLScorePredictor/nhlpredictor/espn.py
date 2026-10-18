"""Betting lines and probable starting goalies for upcoming games, from ESPN.

ESPN's public scoreboard needs no key and lists, for each game, the line from
its odds provider (moneylines and the total) and, closer to game time, each
team's probable starting goalie. One request per game day. Any failure leaves
the affected games without a line or a named starter, and the prediction
falls back to the model alone and the projected starter.
"""

from __future__ import annotations

import logging
import re
import unicodedata

import numpy as np
import pandas as pd
import requests

from .config import DISPLAY_TZ

log = logging.getLogger(__name__)

SCOREBOARD = "https://site.api.espn.com/apis/site/v2/sports/hockey/nhl/scoreboard"
# ESPN abbreviations that differ from the NHL's.
ESPN_TEAMS = {"NJ": "NJD", "SJ": "SJS", "TB": "TBL", "LA": "LAK", "UTAH": "UTA", "ARI": "UTA",
              "PHX": "UTA", "VEG": "VGK", "WAS": "WSH", "MON": "MTL", "CLB": "CBJ", "NAS": "NSH"}
COLUMNS = ["date", "home_team", "away_team", "home_moneyline", "away_moneyline", "total_line",
           "over_price", "under_price", "line_source", "home_probable", "away_probable",
           "home_probable_status", "away_probable_status"]
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


def _probable(competitor: dict) -> tuple[str | None, str | None]:
    for p in competitor.get("probables") or []:
        athlete = p.get("athlete") or {}
        name = athlete.get("displayName") or athlete.get("fullName")
        if name:
            status = _dig(p, "status", "name") or _dig(p, "status", "type") or "Probable"
            return name, str(status)
    return None, None


def parse_scoreboard(payload: dict) -> pd.DataFrame:
    rows = []
    for event in payload.get("events") or []:
        comp = (event.get("competitions") or [{}])[0]
        sides = {c.get("homeAway"): c for c in comp.get("competitors") or []}
        if "home" not in sides or "away" not in sides:
            continue
        start = pd.to_datetime(event.get("date") or comp.get("date"), utc=True, errors="coerce")
        row = {"date": start.tz_convert(DISPLAY_TZ).date() if not pd.isna(start) else None,
               "home_team": _team(_dig(sides["home"], "team", "abbreviation")),
               "away_team": _team(_dig(sides["away"], "team", "abbreviation"))}
        odds = (comp.get("odds") or [None])[0] or {}
        row["home_moneyline"] = _price(odds, "home")
        row["away_moneyline"] = _price(odds, "away")
        row["total_line"], row["over_price"], row["under_price"] = _total(odds)
        provider = _dig(odds, "provider", "name")
        row["line_source"] = ("ESPN" + (f" ({provider})" if provider else "")) if odds else None
        for side in ("home", "away"):
            row[f"{side}_probable"], row[f"{side}_probable_status"] = _probable(sides[side])
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


def normalize_name(name) -> str:
    text = unicodedata.normalize("NFKD", str(name or "")).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z ]", "", text.lower()).strip()


def match_goalie(name, candidates: pd.Series) -> int | None:
    """Goalie id whose name matches ``name``; ``candidates`` maps id to full name."""
    target = normalize_name(name)
    if not target:
        return None
    norm = candidates.map(normalize_name)
    exact = norm[norm == target]
    if len(exact):
        return int(exact.index[0])
    last = target.split()[-1]
    first = target[0]
    loose = norm[norm.str.endswith(" " + last) & norm.str.startswith(first)]
    return int(loose.index[0]) if len(loose) == 1 else None


def attach(games: pd.DataFrame, board: pd.DataFrame, goalie_names: pd.Series,
           team_goalies: dict[str, pd.Series]) -> pd.DataFrame:
    """Add lines and probable starters from ``board`` to upcoming ``games``.

    ``team_goalies`` maps each team to the ids and names of goalies who have
    played for it recently, so a probable starter is matched within his team
    first and then across the league (a goalie just traded or called up).
    """
    out = games.copy()
    for col in NUMERIC:
        out[col] = np.nan
    out["line_source"] = None
    for side in ("home", "away"):
        out[f"{side}_goalie_id"] = np.nan
        out[f"{side}_goalie_source"] = None
    if board.empty:
        return out
    key = board.drop_duplicates(["date", "home_team", "away_team"]).set_index(["date", "home_team", "away_team"])
    matched = 0
    for idx, g in out.iterrows():
        k = (g["date"], g["home_team"], g["away_team"])
        if k not in key.index:
            continue
        matched += 1
        row = key.loc[k]
        for col in NUMERIC + ["line_source"]:
            out.at[idx, col] = row[col]
        for side in ("home", "away"):
            name = row[f"{side}_probable"]
            if not name:
                continue
            team = g[f"{side}_team"]
            gid = match_goalie(name, team_goalies.get(team, pd.Series(dtype=object)))
            if gid is None:
                gid = match_goalie(name, goalie_names)
            if gid is not None:
                out.at[idx, f"{side}_goalie_id"] = gid
                out.at[idx, f"{side}_goalie_source"] = f"ESPN {str(row[f'{side}_probable_status']).lower()}"
    log.info("ESPN matched %d of %d games; lines for %d; probable goalies for %d sides", matched, len(out),
             int(out["home_moneyline"].notna().sum()),
             int(out["home_goalie_id"].notna().sum() + out["away_goalie_id"].notna().sum()))
    return out
