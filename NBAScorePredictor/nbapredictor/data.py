"""Download NBA data and reduce it to per-game summaries.

Raw play-by-play is about 20 MB a season, so the raw files are downloaded to
a local cache and boiled down to four small tables per season that are
committed to the repo (finished seasons gzipped):

- ``data/games/{season}_games``: the schedule with final scores, overtimes
  and neutral sites.
- ``data/games/{season}_teams``: one row per team per game with points,
  possessions and shooting, plus the same with garbage time removed.
- ``data/games/{season}_players``: one row per player per game played, with
  minutes, plus-minus and the box score.
- ``data/games/{season}_stints``: every stretch of a game with the same ten
  players on the floor, with each side's points and possessions and a
  garbage-time flag; the player ratings are fitted on these.

Only the current season is re-downloaded on routine updates.
"""

from __future__ import annotations

import datetime as dt
import logging
import os
import time
from pathlib import Path

import numpy as np
import pandas as pd
import requests

from .config import (
    CACHE_DIR,
    DISPLAY_TZ,
    FIRST_SEASON,
    GAMES_DIR,
    NBA_TEAMS,
    OT_MINUTES,
    PBP_URL,
    PLAYER_BOX_URL,
    PLAYERS_PATH,
    REG_MINUTES,
    ROSTERS_URL,
    SCHEDULE_URL,
    TEAM_ALIASES,
    TEAM_BOX_URL,
)

log = logging.getLogger(__name__)

GAME_COLUMNS = ["game_id", "season", "game_type", "start", "home_team", "away_team", "home_score", "away_score",
                "periods", "neutral", "venue", "city", "state"]
TEAM_COLUMNS = ["game_id", "season", "date", "team", "opp", "home", "minutes", "pts", "opp_pts", "poss",
                "fga", "fg3a", "fg3m", "fta", "ftm", "oreb", "dreb", "tov",
                "clean_pts", "clean_opp_pts", "clean_poss", "garbage_poss"]
PLAYER_COLUMNS = ["game_id", "team", "player_id", "status", "starter", "minutes", "plus_minus", "pts", "fgm",
                  "fga", "fg3m", "fg3a", "ftm", "fta", "oreb", "dreb", "ast", "stl", "blk", "tov", "pf"]
# A player in the box score either played, sat as a healthy scratch (coach's
# decision) or was out (injury, illness, rest, suspension, personal reasons).
PLAYED, DNP, OUT = "played", "dnp", "out"
STINT_COLUMNS = ["game_id", "period", "start", "seconds", "home_ids", "away_ids", "home_pts", "away_pts",
                 "home_poss", "away_poss", "garbage", "valid"]
NAME_COLUMNS = ["player_id", "name", "position"]
# ESPN season types: 2 regular season (NBA Cup games included), 3 playoffs, 5 play-in.
GAME_TYPES = {2: "R", 3: "P", 5: "I"}
# Event types that can name a player who is not on the floor.
OFF_COURT = ("Technical", "Ejection", "Timeout", "Challenge", "Review", "End Period", "End Game", "Delay")
# Bubble games in 2020 were played at one site for every team.
BUBBLE_CITY = "Lake Buena Vista"


def current_season(today: dt.date | None = None) -> int:
    """The NBA season in progress (named by the year it ends), or the next one
    from August, when the new schedule is out."""
    today = today or dt.date.today()
    return today.year + 1 if today.month >= 8 else today.year


def fetch(url: str, path: Path, max_age_hours: float = 6.0, retries: int = 4) -> Path:
    """Download ``url`` to ``path`` unless a fresh enough copy exists."""
    if path.exists() and (time.time() - path.stat().st_mtime) < max_age_hours * 3600:
        return path
    path.parent.mkdir(parents=True, exist_ok=True)
    delay = 2.0
    for attempt in range(retries):
        try:
            with requests.get(url, timeout=120, stream=True) as resp:
                resp.raise_for_status()
                tmp = path.with_suffix(path.suffix + ".part")
                with open(tmp, "wb") as fh:
                    for chunk in resp.iter_content(chunk_size=1 << 20):
                        fh.write(chunk)
                os.replace(tmp, path)
            return path
        except requests.RequestException as exc:
            if isinstance(exc, requests.HTTPError) and exc.response is not None \
                    and exc.response.status_code == 404:
                raise
            if attempt == retries - 1:
                if path.exists():
                    log.warning("Using stale %s after download failed: %s", path.name, exc)
                    return path
                raise
            log.warning("Download of %s failed (%s); retrying in %.0fs", url, exc, delay)
            time.sleep(delay)
            delay *= 2
    return path


def team_code(series: pd.Series) -> pd.Series:
    return series.astype(str).replace(TEAM_ALIASES)


RAW_SOURCES = {
    "schedule": (SCHEDULE_URL, "nba_schedule_{season}.parquet"),
    "team_box": (TEAM_BOX_URL, "team_box_{season}.parquet"),
    "player_box": (PLAYER_BOX_URL, "player_box_{season}.parquet"),
    "pbp": (PBP_URL, "play_by_play_{season}.parquet"),
    "rosters": (ROSTERS_URL, "rosters_{season}.parquet"),
}


def load_raw(kind: str, season: int, max_age_hours: float = 6.0) -> pd.DataFrame:
    url, name = RAW_SOURCES[kind]
    path = fetch(url.format(season=season), CACHE_DIR / name.format(season=season), max_age_hours)
    return pd.read_parquet(path)


def _neutral(s: pd.DataFrame) -> pd.Series:
    """ESPN's neutral-site flag, the 2020 bubble, and games away from the home
    team's state in a city no team calls home (Mexico City, Europe, the NBA Cup
    in Las Vegas). The Spurs' games in Austin stay home games, and seasons with
    garbled venue names (2010-11) are left alone."""
    def mode(v):
        v = v.dropna()
        return v.mode().iloc[0] if len(v) else None
    home_city = s.groupby("home_team")["city"].transform(mode)
    home_state = s.groupby("home_team")["state"].transform(mode)
    team_cities = set(s.groupby("home_team")["city"].agg(mode).dropna())
    away = s["city"].notna() & (s["city"] != home_city) & (s["state"] != home_state) & ~s["city"].isin(team_cities)
    return s["neutral_site"].fillna(False).astype(bool) | s["city"].eq(BUBBLE_CITY) | away


def reduce_schedule(raw: pd.DataFrame) -> pd.DataFrame:
    """Regular-season, play-in and playoff games between NBA teams."""
    s = raw[raw["season_type"].isin(list(GAME_TYPES))].copy()
    s["home_team"] = team_code(s["home_abbreviation"])
    s["away_team"] = team_code(s["away_abbreviation"])
    s = s[s["home_team"].isin(NBA_TEAMS) & s["away_team"].isin(NBA_TEAMS)].copy()
    s = s[~s["status_type_name"].isin(["STATUS_POSTPONED", "STATUS_CANCELED"])].copy()
    s["game_type"] = s["season_type"].map(GAME_TYPES)
    s["start"] = pd.to_datetime(s["date"], utc=True, errors="coerce")
    s["city"] = s["venue_address_city"]
    s["state"] = s["venue_address_state"] if "venue_address_state" in s else None
    s["venue"] = s["venue_full_name"]
    done = s["status_type_completed"].fillna(False).astype(bool)
    s["home_score"] = pd.to_numeric(s["home_score"], errors="coerce").where(done)
    s["away_score"] = pd.to_numeric(s["away_score"], errors="coerce").where(done)
    s["periods"] = pd.to_numeric(s["status_period"], errors="coerce").where(done)
    s["neutral"] = _neutral(s)
    s["season"] = s["season"].astype(int)
    s["game_id"] = s["game_id"].astype("int64")
    return s[GAME_COLUMNS].sort_values(["start", "game_id"]).reset_index(drop=True)


def prepare_games(sched: pd.DataFrame) -> pd.DataFrame:
    """Add the columns the model uses to the committed schedule."""
    g = sched.copy()
    g["start"] = pd.to_datetime(g["start"], utc=True, format="ISO8601")
    g["date"] = g["start"].dt.tz_convert(DISPLAY_TZ).dt.date
    g["playoff"] = g["game_type"].eq("P")
    g["completed"] = g["home_score"].notna() & g["away_score"].notna()
    g["neutral"] = g["neutral"].fillna(False).astype(bool)
    return g.sort_values(["start", "game_id"]).reset_index(drop=True)


def game_minutes(periods) -> np.ndarray:
    p = np.asarray(periods, dtype=float)
    return REG_MINUTES + OT_MINUTES * np.clip(np.nan_to_num(p, nan=4.0) - 4, 0, None)


def _possessions(fga, oreb, tov, fta) -> np.ndarray:
    return np.asarray(fga, float) - np.asarray(oreb, float) + np.asarray(tov, float) + 0.44 * np.asarray(fta, float)


# ---- stints ------------------------------------------------------------

def _period_length(period: int) -> float:
    return 720.0 if period <= 4 else 300.0


def _period_start(period: int) -> float:
    return 720.0 * min(period - 1, 4) + 300.0 * max(period - 5, 0)


def _garbage_threshold(seconds_left: np.ndarray) -> np.ndarray:
    """Cleaning the Glass: a lead of 25 with 12 to 9 minutes left in the fourth,
    20 with 9 to 6, or 10 with 6 or fewer."""
    return np.where(seconds_left > 540, 25, np.where(seconds_left > 360, 20, 10))


def game_stints(ev: pd.DataFrame, home_id: int, starters: set, team_of: dict) -> list[dict]:
    """Stints with the same ten players on the floor, from one game's events.

    Substitutions are logged, but changes between periods are not, so each
    period's opening five are the players whose first appearance in the period
    is anything but entering as a substitute. A player who stays on through a
    whole period without an event is carried over from the end of the period
    before. Periods that cannot be resolved to five players a side are kept
    but marked invalid.
    """
    typ = ev["type_text"].fillna("").to_numpy()
    per = ev["period_number"].to_numpy(int)
    left = ev["start_quarter_seconds_remaining"].to_numpy(float)
    team = ev["team_id"].to_numpy(float)
    a = ev[["athlete_id_1", "athlete_id_2", "athlete_id_3"]].to_numpy(float)
    hs = ev["home_score"].to_numpy(float)
    as_ = ev["away_score"].to_numpy(float)
    shooting = ev["shooting_play"].fillna(False).to_numpy(bool)
    is_sub = typ == "Substitution"
    is_ft = np.char.startswith(typ.astype(str), "Free Throw")
    fga = shooting & ~is_ft
    oreb = (typ == "Offensive Rebound") & ~np.isnan(a[:, 0])
    tov = np.char.find(typ.astype(str), "Turnover") >= 0
    tov &= typ != "No Turnover"
    on_court_event = np.array([not any(k in t for k in OFF_COURT) for t in typ])

    stints: list[dict] = []
    end_of_last: dict[int, set] = {}
    prev_h, prev_a = 0.0, 0.0
    for period in np.unique(per):
        idx = np.flatnonzero(per == period)
        first: dict[float, str] = {}
        for i in idx:
            if is_sub[i]:
                for pid, role in ((a[i, 0], "in"), (a[i, 1], "on")):
                    if not np.isnan(pid) and pid not in first:
                        first[pid] = role
            elif on_court_event[i]:
                for pid in a[i]:
                    if not np.isnan(pid) and pid not in first:
                        first[pid] = "on"
        lineup: dict[int, set] = {}
        for pid, role in first.items():
            t = team_of.get(pid)
            if role == "on" and t is not None:
                lineup.setdefault(t, set()).add(pid)
        valid = True
        for t in set(team_of.values()):
            cur = lineup.setdefault(t, set())
            if len(cur) < 5:
                pool = end_of_last.get(t) if period > 1 else {p for p in starters if team_of.get(p) == t}
                extra = [p for p in (pool or ()) if p not in cur and first.get(p) != "in"]
                if len(cur) + len(extra) == 5:
                    cur.update(extra)
            if len(cur) != 5:
                valid = False
        teams = sorted(lineup, key=lambda t: t != home_id)
        if len(teams) != 2:
            continue
        home_t, away_t = teams
        on = {home_t: set(lineup[home_t]), away_t: set(lineup[away_t])}
        start = _period_start(period)
        plen = _period_length(period)
        acc = {"start": start, "h_pts": 0.0, "a_pts": 0.0, "h": np.zeros(4), "a": np.zeros(4), "events": 0}

        def close(at: float):
            secs = at - acc["start"]
            if secs > 0 or acc["events"]:
                stints.append({
                    "period": int(period), "start": acc["start"], "seconds": secs,
                    "home_ids": " ".join(str(int(p)) for p in sorted(on[home_t])),
                    "away_ids": " ".join(str(int(p)) for p in sorted(on[away_t])),
                    "home_pts": acc["h_pts"], "away_pts": acc["a_pts"],
                    "home_poss": float(_possessions(*acc["h"])), "away_poss": float(_possessions(*acc["a"])),
                    "home_score": prev_h - acc["h_pts"], "away_score": prev_a - acc["a_pts"],
                    "valid": valid and len(on[home_t]) == 5 and len(on[away_t]) == 5,
                })
            acc.update(start=at, h_pts=0.0, a_pts=0.0, h=np.zeros(4), a=np.zeros(4), events=0)

        for i in idx:
            at = start + plen - left[i]
            if is_sub[i]:
                close(at)
                t = team_of.get(a[i, 0], team_of.get(a[i, 1]))
                if t in on:
                    if a[i, 1] in on[t]:
                        on[t].discard(a[i, 1])
                    else:
                        valid = False
                    on[t].add(a[i, 0])
                continue
            dh, da = hs[i] - prev_h, as_[i] - prev_a
            if dh or da:
                acc["h_pts"] += dh
                acc["a_pts"] += da
                prev_h, prev_a = hs[i], as_[i]
            side = "h" if team[i] == home_id else ("a" if team[i] in on else None)
            if side:
                acc[side] += np.array([fga[i], oreb[i], tov[i], is_ft[i]], dtype=float)
            acc["events"] += 1
        close(start + plen)
        end_of_last = {t: set(v) for t, v in on.items()}
    _flag_garbage(stints, starters)
    return stints


def _flag_garbage(stints: list[dict], starters: set) -> None:
    """Mark fourth-quarter stints from the point the game turned into garbage
    time and stayed that way: the lead clears the threshold for the time left
    with two or fewer starters on the floor, and stays above it to the end."""
    for s in stints:
        s["garbage"] = False
    q4 = [s for s in stints if s["period"] == 4]
    if not q4:
        return
    left = np.array([2880.0 - s["start"] for s in q4])
    lead = np.array([abs(s["home_score"] - s["away_score"]) for s in q4])
    last = q4[-1]
    final_lead = abs(last["home_score"] + last["home_pts"] - last["away_score"] - last["away_pts"])
    above = lead >= _garbage_threshold(left)
    stays = np.logical_and.accumulate((above & (final_lead >= 10))[::-1])[::-1]
    n_starters = np.array([sum(int(p) in starters for p in (s["home_ids"] + " " + s["away_ids"]).split())
                           for s in q4])
    begins = np.flatnonzero(above & stays & (n_starters <= 2))
    if len(begins):
        for s in q4[begins[0]:]:
            s["garbage"] = True


def summarize_stints(pbp: pd.DataFrame, player_box: pd.DataFrame, games: pd.DataFrame) -> pd.DataFrame:
    """Stints for every finished game with play-by-play.

    ``player_box`` is the raw box score, every listed player included, so a
    player credited with no minutes can still be placed on his team."""
    p = pbp[pbp["game_id"].isin(games["game_id"])]
    p = p.sort_values(["game_id", "period_number", "start_quarter_seconds_remaining", "sequence_number"],
                      ascending=[True, True, False, True])
    box = player_box[player_box["game_id"].isin(games["game_id"]) & player_box["athlete_id"].notna()]
    starters = box[box["starter"].fillna(False).astype(bool)].groupby("game_id")["athlete_id"].agg(
        lambda s: set(s.astype("int64")))
    team_ids = box.groupby("game_id").apply(
        lambda d: dict(zip(d["athlete_id"].astype(float), d["team_id"].astype(int))), include_groups=False)
    home_ids = p.groupby("game_id")["home_team_id"].first()
    rows = []
    for gid, ev in p.groupby("game_id", sort=False):
        if gid not in team_ids.index:
            continue
        for s in game_stints(ev, int(home_ids[gid]), starters.get(gid, set()), team_ids[gid]):
            s["game_id"] = gid
            rows.append(s)
    out = pd.DataFrame(rows)
    if out.empty:
        return pd.DataFrame(columns=STINT_COLUMNS)
    out["garbage"] = out["garbage"].astype(int)
    out["valid"] = out["valid"].astype(int)
    for col in ("home_pts", "away_pts"):
        out[col] = out[col].astype(int)
    return out[STINT_COLUMNS]


# ---- box scores ----------------------------------------------------------

def reduce_players(raw: pd.DataFrame, games: pd.DataFrame) -> pd.DataFrame:
    """One row per player listed in each box score: who played, who sat as a
    healthy scratch and who was out. Older seasons list few non-players."""
    b = raw[raw["game_id"].isin(games["game_id"]) & raw["athlete_id"].notna()].copy()
    b["minutes"] = pd.to_numeric(b["minutes"], errors="coerce").fillna(0)
    played = b["minutes"] > 0
    reason = b["reason"] if "reason" in b else pd.Series("", index=b.index)
    healthy = reason.fillna("").astype(str).str.upper().str.contains("COACH")
    b["status"] = np.where(played, PLAYED, np.where(b["did_not_play"].fillna(False).astype(bool) & healthy, DNP, OUT))
    # Box scores also list players who were never active; only keep the ones with a stated reason.
    b = b[played | b["did_not_play"].fillna(False).astype(bool)]
    b["team"] = team_code(b["team_abbreviation"])
    b["player_id"] = b["athlete_id"].astype("int64")
    b["plus_minus"] = pd.to_numeric(b["plus_minus"].astype(str).str.replace("+", "", regex=False),
                                    errors="coerce")
    ren = {"points": "pts", "field_goals_made": "fgm", "field_goals_attempted": "fga",
           "three_point_field_goals_made": "fg3m", "three_point_field_goals_attempted": "fg3a",
           "free_throws_made": "ftm", "free_throws_attempted": "fta", "offensive_rebounds": "oreb",
           "defensive_rebounds": "dreb", "assists": "ast", "steals": "stl", "blocks": "blk",
           "turnovers": "tov", "fouls": "pf"}
    b = b.rename(columns=ren)
    for col in ren.values():
        b[col] = pd.to_numeric(b[col], errors="coerce").fillna(0).astype(int)
    b["starter"] = b["starter"].fillna(False).astype(bool)
    b["minutes"] = b["minutes"].astype(int)
    b = b.drop_duplicates(["game_id", "player_id"])
    return b[PLAYER_COLUMNS + ["team_id", "athlete_display_name", "athlete_position_abbreviation"]]


def reduce_teams(raw: pd.DataFrame, games: pd.DataFrame, stints: pd.DataFrame) -> pd.DataFrame:
    """One row per team per game: box totals, possessions, and the same with
    garbage time removed (from the stints; the full game when a game has none)."""
    t = raw[raw["game_id"].isin(games["game_id"])].copy()
    t["team"] = team_code(t["team_abbreviation"])
    t["opp"] = team_code(t["opponent_team_abbreviation"])
    g = games.set_index("game_id")
    t["home"] = (t["team"] == t["game_id"].map(g["home_team"])).astype(int)
    t["date"] = t["game_id"].map(pd.to_datetime(g["start"], utc=True).dt.tz_convert(DISPLAY_TZ)
                                 .dt.strftime("%Y-%m-%d"))
    t["minutes"] = game_minutes(t["game_id"].map(g["periods"]))
    ren = {"team_score": "pts", "opponent_team_score": "opp_pts", "field_goals_attempted": "fga",
           "three_point_field_goals_attempted": "fg3a", "three_point_field_goals_made": "fg3m",
           "free_throws_attempted": "fta", "free_throws_made": "ftm", "offensive_rebounds": "oreb",
           "defensive_rebounds": "dreb"}
    t = t.rename(columns=ren)
    # Older seasons repeat the player turnovers under team turnovers; team
    # turnovers (shot clock, eight seconds) are only added when they look real.
    tov = pd.to_numeric(t["turnovers"], errors="coerce").fillna(0)
    team_tov = pd.to_numeric(t.get("team_turnovers"), errors="coerce")
    t["tov"] = tov + np.where(team_tov.notna() & (team_tov < 0.5 * tov), team_tov, 0)
    own = pd.Series(_possessions(t["fga"], t["oreb"], t["tov"], t["fta"]),
                    index=pd.MultiIndex.from_arrays([t["game_id"], t["team"]]))
    opp = pd.Series(list(zip(t["game_id"], t["opp"]))).map(own).to_numpy()
    t["poss"] = 0.5 * (own.to_numpy() + opp)

    # Possessions counted from play-by-play where there is one (they agree
    # with the box-score estimate within about 1%), so the full game and the
    # garbage-free part are on the same footing.
    t["clean_pts"] = np.nan
    t["clean_opp_pts"] = np.nan
    t["clean_poss"] = np.nan
    t["garbage_poss"] = 0.0
    if len(stints):
        s = stints.copy()
        s["poss"] = 0.5 * (s["home_poss"] + s["away_poss"])
        full = s.groupby("game_id")["poss"].sum()
        clean = s[s["garbage"] == 0].groupby("game_id")[["home_pts", "away_pts", "poss"]].sum()
        junk = s[s["garbage"] == 1].groupby("game_id")["poss"].sum()
        home = t["home"] == 1
        gid = t["game_id"]
        t["poss"] = gid.map(full).fillna(t["poss"])
        t["clean_pts"] = np.where(home, gid.map(clean["home_pts"]), gid.map(clean["away_pts"]))
        t["clean_opp_pts"] = np.where(home, gid.map(clean["away_pts"]), gid.map(clean["home_pts"]))
        t["clean_poss"] = gid.map(clean["poss"])
        t["garbage_poss"] = gid.map(junk).fillna(0.0)
    missing = t["clean_poss"].isna() | (t["clean_poss"] <= 0)
    t.loc[missing, "clean_pts"] = t.loc[missing, "pts"]
    t.loc[missing, "clean_opp_pts"] = t.loc[missing, "opp_pts"]
    t.loc[missing, "clean_poss"] = t.loc[missing, "poss"]
    t["season"] = t["game_id"].map(g["season"])
    t = t.drop_duplicates(["game_id", "team"])
    return t[TEAM_COLUMNS].sort_values(["date", "game_id", "home"], ascending=[True, True, False])


def summarize_season(sched: pd.DataFrame, team_box: pd.DataFrame, player_box: pd.DataFrame,
                     pbp: pd.DataFrame | None) -> dict[str, pd.DataFrame]:
    played = sched[sched["home_score"].notna()]
    players = reduce_players(player_box, played)
    stints = summarize_stints(pbp, player_box, played) if pbp is not None else pd.DataFrame(columns=STINT_COLUMNS)
    teams = reduce_teams(team_box, played, stints)
    names = (players.rename(columns={"athlete_display_name": "name", "athlete_position_abbreviation": "position"})
             .drop_duplicates("player_id", keep="last")[NAME_COLUMNS])
    players = players.sort_values(["game_id", "team", "status", "minutes"], ascending=[True, True, False, False])
    return {"teams": teams.reset_index(drop=True), "players": players[PLAYER_COLUMNS].reset_index(drop=True),
            "stints": stints, "names": names}


# ---- committed summaries --------------------------------------------------

KINDS = ("games", "teams", "players", "stints")
COLUMNS = {"games": GAME_COLUMNS, "teams": TEAM_COLUMNS, "players": PLAYER_COLUMNS, "stints": STINT_COLUMNS}
FLOAT_FORMAT = {"teams": "%.2f", "players": None, "stints": "%.2f", "games": None}


def summary_path(season: int, kind: str, gz: bool) -> Path:
    return GAMES_DIR / f"{season}_{kind}.csv{'.gz' if gz else ''}"


def read_summary(season: int, kind: str) -> pd.DataFrame | None:
    for gz in (False, True):
        path = summary_path(season, kind, gz)
        if path.exists():
            return pd.read_csv(path)
    return None


def write_summary(df: pd.DataFrame, season: int, kind: str, finished: bool) -> None:
    """Finished seasons are stored gzipped; the season in progress as plain
    CSV, so each day's commit is a small diff."""
    path = summary_path(season, kind, finished)
    other = summary_path(season, kind, not finished)
    df.to_csv(path, index=False, float_format=FLOAT_FORMAT[kind])
    if other.exists():
        other.unlink()


def update_names(names: pd.DataFrame) -> None:
    old = pd.read_csv(PLAYERS_PATH) if PLAYERS_PATH.exists() else pd.DataFrame(columns=NAME_COLUMNS)
    merged = pd.concat([old, names], ignore_index=True).drop_duplicates("player_id", keep="last")
    merged = merged.sort_values("player_id")
    if PLAYERS_PATH.exists() and merged.reset_index(drop=True).equals(old.sort_values("player_id")
                                                                       .reset_index(drop=True)):
        return
    merged.to_csv(PLAYERS_PATH, index=False)


def update_summaries(seasons: list[int], refresh: set[int] = frozenset(), max_age_hours: float = 6.0) -> None:
    """Build missing season summaries and rebuild the ones in ``refresh``."""
    GAMES_DIR.mkdir(parents=True, exist_ok=True)
    latest = current_season()
    for season in seasons:
        have = all(read_summary(season, k) is not None for k in KINDS)
        if have and season not in refresh:
            continue
        finished = season < latest
        try:
            sched = reduce_schedule(load_raw("schedule", season, max_age_hours))
        except requests.HTTPError as exc:
            log.info("No schedule for %s yet (%s)", season, exc)
            continue
        write_summary(sched, season, "games", finished)
        if sched["home_score"].notna().sum() == 0:
            for kind in ("teams", "players", "stints"):
                write_summary(pd.DataFrame(columns=COLUMNS[kind]), season, kind, finished)
            log.info("Saved the %s schedule; no games played yet", season)
            continue
        try:
            team_box = load_raw("team_box", season, max_age_hours)
            player_box = load_raw("player_box", season, max_age_hours)
        except requests.HTTPError as exc:
            log.info("No box scores for %s yet (%s)", season, exc)
            continue
        try:
            pbp = load_raw("pbp", season, max_age_hours)
        except requests.HTTPError as exc:
            log.warning("No play-by-play for %s (%s); stints skipped", season, exc)
            pbp = None
        parts = summarize_season(sched, team_box, player_box, pbp)
        for kind in ("teams", "players", "stints"):
            write_summary(parts[kind], season, kind, finished)
        update_names(parts["names"])
        log.info("Summarized %s: %d games, %d player-games, %d stints", season, len(parts["teams"]) // 2,
                 len(parts["players"]), len(parts["stints"]))


def load_summaries(first: int = FIRST_SEASON, last: int | None = None) -> dict[str, pd.DataFrame]:
    """All committed summaries, oldest first, keyed by kind, plus player names."""
    frames: dict[str, list] = {k: [] for k in KINDS}
    for season in range(first, (last or current_season()) + 1):
        for kind in KINDS:
            df = read_summary(season, kind)
            if df is not None and len(df):
                if kind != "games":
                    df["season"] = season
                frames[kind].append(df)
    out = {}
    for kind in KINDS:
        cols = COLUMNS[kind] + ([] if kind == "games" or "season" in COLUMNS[kind] else ["season"])
        out[kind] = pd.concat(frames[kind], ignore_index=True).reindex(columns=cols) if frames[kind] \
            else pd.DataFrame(columns=cols)
    out["games"] = prepare_games(out["games"])
    out["names"] = pd.read_csv(PLAYERS_PATH) if PLAYERS_PATH.exists() else pd.DataFrame(columns=NAME_COLUMNS)
    return out
