"""Download MLB data and keep compact per-season summaries.

Two sources feed the same summary files in ``data/games/``:

- Retrosheet play-by-play for every season it has published (it posts a
  season a few months after the World Series). Player ids are translated to
  MLB's own ids through the Chadwick Bureau register.
- The MLB Stats API (schedule, line scores and box scores) for the season in
  progress and any season Retrosheet has not published yet. Each run reads
  only the box scores of games finished since the last one. When Retrosheet
  publishes such a season, it is rebuilt from the play-by-play.

Files per season:

- ``{season}_games.csv``: schedule and results with park, weather, starting
  pitchers and line scores.
- ``{season}_batting.csv``: plate appearances by outcome for each batter in
  each game, with his starting lineup slot.
- ``{season}_pitching.csv``: batters faced by outcome, outs, pitches and runs
  for each pitcher in each game.
- ``{season}_transitions.csv`` and ``{season}_platoon.csv`` (Retrosheet
  seasons only): base-out transition counts for the inning simulator and
  plate-appearance outcomes by batter and pitcher hand.
"""

from __future__ import annotations

import concurrent.futures as cf
import datetime as dt
import logging
import os
import time
from collections import Counter
from pathlib import Path

import numpy as np
import pandas as pd
import requests

from . import retro
from .config import (
    CACHE_DIR,
    DISPLAY_TZ,
    FIRST_SEASON,
    GAMES_DIR,
    PLAYERS_PATH,
    REGISTER_URL,
    RETRO_URL,
    current_season,
)

log = logging.getLogger(__name__)

GAME_COLUMNS = ["game_id", "season", "game_type", "date", "start", "game_number", "home_team", "away_team",
                "status", "home_score", "away_score", "innings", "sched_innings", "tiebreaker", "park_id",
                "daynight", "dome", "temp", "wind", "wind_speed", "home_starter", "away_starter",
                "home_line", "away_line", "htbf", "source"]
EVENT_COLUMNS = ["k", "bb", "ibb", "hbp", "s", "d", "t", "hr", "out"]
BAT_COLUMNS = ["game_id", "team", "player_id", "slot", "pos", "pa"] + EVENT_COLUMNS
PITCH_COLUMNS = ["game_id", "team", "player_id", "starter", "seq", "outs", "bf", "pitches"] + EVENT_COLUMNS \
    + ["r", "er"]
TRANSITION_COLUMNS = ["start", "event", "end", "runs", "n"]
PLATOON_COLUMNS = ["bats", "throws", "event", "n"]
PLAYER_COLUMNS = ["player_id", "name", "bats", "throws", "birth_year", "retro_id"]
KINDS = {"games": GAME_COLUMNS, "batting": BAT_COLUMNS, "pitching": PITCH_COLUMNS,
         "transitions": TRANSITION_COLUMNS, "platoon": PLATOON_COLUMNS}
DTYPES = {"game_id": str, "player_id": str, "home_starter": str, "away_starter": str, "home_line": str,
          "away_line": str, "park_id": str, "retro_id": str}
FINAL = "final"


def fetch(url: str, path: Path, max_age_hours: float = 24.0, retries: int = 4,
          session: requests.Session | None = None) -> Path:
    """Download ``url`` to ``path`` unless a fresh enough copy exists."""
    if path.exists() and (time.time() - path.stat().st_mtime) < max_age_hours * 3600:
        return path
    path.parent.mkdir(parents=True, exist_ok=True)
    getter = session or requests
    delay = 2.0
    for attempt in range(retries):
        try:
            resp = getter.get(url, timeout=120)
            resp.raise_for_status()
            tmp = path.with_suffix(path.suffix + ".part")
            tmp.write_bytes(resp.content)
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


# ---- Retrosheet -----------------------------------------------------------

def retro_text(season: int, name: str, max_age_hours: float = 24.0 * 30) -> str | None:
    """One Retrosheet file for ``season`` (None if it does not exist)."""
    path = CACHE_DIR / "retrosheet" / str(season) / name
    try:
        fetch(RETRO_URL.format(season=season, name=name), path, max_age_hours)
    except requests.HTTPError as exc:
        if exc.response is not None and exc.response.status_code == 404:
            return None
        raise
    return path.read_text(encoding="latin-1")


def retrosheet_has(season: int) -> bool:
    """Whether Retrosheet has published ``season``'s play-by-play."""
    try:
        resp = requests.head(RETRO_URL.format(season=season, name=f"TEAM{season}"), timeout=30)
        return resp.status_code == 200
    except requests.RequestException:
        return False


def register(max_age_hours: float = 24.0 * 90) -> pd.DataFrame:
    """Chadwick register rows that have a Retrosheet id: ids, names and birth year."""
    cols = ["key_mlbam", "key_retro", "name_first", "name_last", "birth_year"]
    frames = []
    for part in "0123456789abcdef":
        path = fetch(REGISTER_URL.format(part=part), CACHE_DIR / "register" / f"people-{part}.csv", max_age_hours)
        frames.append(pd.read_csv(path, usecols=cols, dtype=str))
    reg = pd.concat(frames, ignore_index=True)
    return reg[reg["key_retro"].notna()].drop_duplicates("key_retro").set_index("key_retro")


def summarize_retro(season: int, max_age_hours: float = 24.0 * 30) -> tuple[dict, dict]:
    """Parse a published Retrosheet season. Returns the summary frames (with
    Retrosheet player ids) and each player's (bats, throws, name)."""
    teams = retro.parse_teams(retro_text(season, f"TEAM{season}", max_age_hours) or "")
    if not teams:
        raise FileNotFoundError(f"Retrosheet has no {season} season")
    files = [(f"{season}{code}.EV{league}", "R") for code, league in sorted(teams.items())]
    files += [(f"{season}{series}.EVE", kind) for series, kind in retro.POSTSEASON_FILES.items()]
    rosters = [f"{code}{season}.ROS" for code in sorted(teams)]
    with cf.ThreadPoolExecutor(max_workers=8) as pool:
        texts = dict(zip([f for f, _ in files], pool.map(lambda f: retro_text(season, f[0], max_age_hours), files)))
        roster_texts = list(pool.map(lambda name: retro_text(season, name, max_age_hours), rosters))
    hands: dict[str, tuple] = {}
    for text in roster_texts:
        hands.update(retro.parse_roster(text or ""))
    games, batting, pitching = [], [], []
    transitions, platoon = Counter(), Counter()
    for name, kind in files:
        text = texts.get(name)
        if not text:
            continue
        parsed, trans, plat = retro.parse_events(text, season, {k: v[:2] for k, v in hands.items()}, kind)
        for g in parsed:
            games.append(g["game"])
            batting += g["batting"]
            pitching += g["pitching"]
        transitions.update(trans)
        platoon.update(plat)
    out = {
        "games": pd.DataFrame(games),
        "batting": pd.DataFrame(batting),
        "pitching": pd.DataFrame(pitching),
        "transitions": pd.DataFrame([(*k, n) for k, n in sorted(transitions.items())], columns=TRANSITION_COLUMNS),
        "platoon": pd.DataFrame([(*k, n) for k, n in sorted(platoon.items())], columns=PLATOON_COLUMNS),
    }
    g = out["games"]
    g["status"] = FINAL
    g["source"] = "retrosheet"
    return out, hands


def apply_ids(frames: dict, ids: pd.Series) -> dict:
    """Swap Retrosheet player ids for MLB ids where the register has them."""
    def swap(s: pd.Series) -> pd.Series:
        return s.map(ids).fillna(s)
    frames["batting"]["player_id"] = swap(frames["batting"]["player_id"])
    frames["pitching"]["player_id"] = swap(frames["pitching"]["player_id"])
    for col in ("home_starter", "away_starter"):
        frames["games"][col] = swap(frames["games"][col])
    return frames


# ---- files ----------------------------------------------------------------

def summary_paths(season: int) -> dict[str, Path]:
    """Each summary file of ``season``: gzipped once a season is final on
    Retrosheet, plain CSV while it is being updated (so daily commits stay
    small diffs)."""
    out = {}
    for kind in KINDS:
        plain = GAMES_DIR / f"{season}_{kind}.csv"
        packed = GAMES_DIR / f"{season}_{kind}.csv.gz"
        out[kind] = packed if packed.exists() else plain
    return out


def read_summary(path: Path, columns: list[str]) -> pd.DataFrame:
    if not path.exists():
        return pd.DataFrame(columns=columns)
    df = pd.read_csv(path, dtype={k: v for k, v in DTYPES.items() if k in columns})
    return df.reindex(columns=columns)


def write_summaries(season: int, frames: dict, compress: bool = False) -> None:
    GAMES_DIR.mkdir(parents=True, exist_ok=True)
    for kind in KINDS:
        if kind not in frames:
            continue
        plain = GAMES_DIR / f"{season}_{kind}.csv"
        path = plain.with_suffix(".csv.gz") if compress else plain
        stale = plain if compress else plain.with_suffix(".csv.gz")
        stale.unlink(missing_ok=True)
        df = frames[kind].reindex(columns=KINDS[kind])
        if kind == "games":
            df = df.sort_values(["date", "game_number", "game_id"])
        elif kind in ("batting", "pitching"):
            order = {gid: i for i, gid in enumerate(frames["games"].sort_values(
                ["date", "game_number", "game_id"])["game_id"])}
            df = df.assign(_o=df["game_id"].map(order)).sort_values(
                ["_o", "team", "slot" if kind == "batting" else "seq", "player_id"]).drop(columns="_o")
        df.to_csv(path, index=False, float_format="%.6g",
                  compression={"method": "gzip", "mtime": 0} if compress else None)


def load_players() -> pd.DataFrame:
    if not PLAYERS_PATH.exists():
        return pd.DataFrame(columns=PLAYER_COLUMNS)
    return pd.read_csv(PLAYERS_PATH, dtype={"player_id": str, "retro_id": str}).reindex(columns=PLAYER_COLUMNS)


def save_players(players: pd.DataFrame) -> None:
    players = players.drop_duplicates("player_id", keep="last").sort_values("player_id")
    players["birth_year"] = pd.to_numeric(players["birth_year"], errors="coerce").astype("Int64")
    PLAYERS_PATH.parent.mkdir(parents=True, exist_ok=True)
    players[PLAYER_COLUMNS].to_csv(PLAYERS_PATH, index=False)


def build_retro_seasons(seasons, max_age_hours: float = 24.0 * 30) -> None:
    """Summarize Retrosheet seasons and add their players to ``players.csv``."""
    reg = register()
    ids = reg["key_mlbam"].dropna()
    players = load_players()
    new_rows = []
    for season in seasons:
        frames, hands = summarize_retro(season, max_age_hours)
        frames = apply_ids(frames, ids)
        write_summaries(season, frames, compress=True)
        for rid, (bats, throws, name) in hands.items():
            row = reg.loc[rid] if rid in reg.index else None
            new_rows.append({"player_id": ids.get(rid, rid), "retro_id": rid, "bats": bats, "throws": throws,
                             "name": name if row is None else f"{row['name_first']} {row['name_last']}",
                             "birth_year": None if row is None else row["birth_year"]})
        log.info("Summarized %s from Retrosheet: %d games", season, len(frames["games"]))
    if new_rows:
        save_players(pd.concat([players, pd.DataFrame(new_rows)], ignore_index=True))


def season_source(season: int) -> str | None:
    path = summary_paths(season)["games"]
    if not path.exists():
        return None
    src = pd.read_csv(path, usecols=["source"], nrows=1)["source"]
    return str(src.iloc[0]) if len(src) else None


def update_statsapi_season(season: int, session: requests.Session | None = None) -> None:
    """Bring a season read from the MLB Stats API up to date: the full
    schedule, plus box scores for games finished since the last run."""
    from . import statsapi

    session = session or requests.Session()
    sched = statsapi.fetch_schedule(f"{season}-02-01", f"{season}-11-30", session=session)
    if sched.empty:
        log.info("No %s schedule from the MLB Stats API yet", season)
        return
    paths = {kind: GAMES_DIR / f"{season}_{kind}.csv" for kind in KINDS}
    old = read_summary(paths["games"], GAME_COLUMNS).set_index("game_id")
    batting = read_summary(paths["batting"], BAT_COLUMNS)
    pitching = read_summary(paths["pitching"], PITCH_COLUMNS)
    final = sched["status"].eq(FINAL)
    finals = set(sched.loc[final, "game_id"])
    need = sorted(finals - set(pitching["game_id"]))
    boxes = statsapi.fetch_boxscores(need, session) if need else {}
    log.info("%s: %d finished games, %d new box scores", season, len(finals), len(boxes))
    batting = pd.concat([batting[batting["game_id"].isin(finals)],
                         pd.DataFrame([r for b in boxes.values() for r in b["batting"]], columns=BAT_COLUMNS)],
                        ignore_index=True)
    pitching = pd.concat([pitching[pitching["game_id"].isin(finals)],
                          pd.DataFrame([r for b in boxes.values() for r in b["pitching"]], columns=PITCH_COLUMNS)],
                         ignore_index=True)
    games = sched.copy()
    for side in ("home", "away"):
        stored = games["game_id"].map(old[f"{side}_starter"]) if len(old) else pd.Series(np.nan, index=games.index)
        boxed = games["game_id"].map({gid: b["starters"].get(side) for gid, b in boxes.items()})
        actual = boxed.fillna(stored)
        games[f"{side}_starter"] = np.where(final & actual.notna(), actual, games[f"{side}_starter"])
    for gid, b in boxes.items():
        for col, value in (b.get("weather") or {}).items():
            if value is not None and not (isinstance(value, float) and np.isnan(value)):
                games.loc[games["game_id"] == gid, col] = value
    if len(old):
        for col in ("temp", "dome", "wind", "wind_speed"):
            keep = final & games[col].isna()
            games.loc[keep, col] = games.loc[keep, "game_id"].map(old[col])
    history = pd.concat([read_summary(summary_paths(s)["games"], GAME_COLUMNS) for s in range(FIRST_SEASON, season)],
                        ignore_index=True)
    games["park_id"] = statsapi.assign_parks(games, history)
    unplayed = ~final & games["status"].ne("postponed")
    games = games[final | unplayed]
    write_summaries(season, {"games": games, "batting": batting, "pitching": pitching}, compress=False)

    players = load_players()
    ids = set(batting["player_id"]) | set(pitching["player_id"]) | \
        set(games["home_starter"].dropna()) | set(games["away_starter"].dropna())
    new = sorted(ids - set(players["player_id"]))
    if new:
        found = statsapi.fetch_people(new, session)
        if len(found):
            save_players(pd.concat([players, found], ignore_index=True))
            log.info("Added %d players", len(found))


def update_summaries(season: int, max_age_hours: float = 1.0, retro_first: int = FIRST_SEASON) -> None:
    """Bring every season up to date.

    Missing past seasons come from Retrosheet when it has them; a past season
    read from the MLB Stats API is rebuilt from Retrosheet once it is
    published. The current season is updated from the MLB Stats API.
    """
    pending_retro = []
    for s in range(retro_first, season):
        source = season_source(s)
        if source == "retrosheet":
            continue
        if retrosheet_has(s):
            pending_retro.append(s)
        elif source is None or s == season - 1:
            # Not on Retrosheet yet: keep last season current through its postseason.
            update_statsapi_season(s)
    if pending_retro:
        build_retro_seasons(pending_retro)
    update_statsapi_season(season)


# ---- loading --------------------------------------------------------------

def prepare_games(games: pd.DataFrame) -> pd.DataFrame:
    """Add the columns the model uses to the committed schedule.

    A game is at a neutral site when it is not played at the park that hosts
    most of the home team's games that season (London, Tokyo, Mexico City,
    Williamsport and the like).
    """
    g = games.copy()
    g["start"] = pd.to_datetime(g["start"], utc=True, format="ISO8601")
    g["date"] = pd.to_datetime(g["date"]).dt.date
    g["playoff"] = g["game_type"].ne("R")
    g["completed"] = g["status"].eq(FINAL) & g["home_score"].notna() & g["away_score"].notna()
    main = g.groupby(["season", "home_team"])["park_id"].agg(lambda s: s.mode().iloc[0] if s.notna().any() else None)
    home_park = pd.Series(list(zip(g["season"], g["home_team"])), index=g.index).map(main)
    g["neutral"] = (g["park_id"].notna() & home_park.notna() & g["park_id"].ne(home_park)) | g["htbf"].eq(1)
    for col in ("home_score", "away_score", "innings", "sched_innings", "tiebreaker", "game_number", "htbf", "dome"):
        g[col] = pd.to_numeric(g[col], errors="coerce")
    g["sched_innings"] = g["sched_innings"].fillna(9).astype(int)
    order = g["start"].fillna(pd.to_datetime(g["date"]).dt.tz_localize("UTC"))
    return g.assign(_o=order).sort_values(["_o", "game_number", "game_id"]).drop(columns="_o").reset_index(drop=True)


def load_summaries(first: int = FIRST_SEASON, last: int | None = None) -> dict[str, pd.DataFrame]:
    """All committed summaries, oldest first, keyed by kind (transition and
    platoon tables carry a ``season`` column)."""
    frames: dict[str, list] = {k: [] for k in KINDS}
    for season in range(first, (last or current_season()) + 1):
        for kind, path in summary_paths(season).items():
            df = read_summary(path, KINDS[kind])
            if len(df):
                if kind in ("transitions", "platoon"):
                    df.insert(0, "season", season)
                frames[kind].append(df)
    out = {}
    for kind, cols in KINDS.items():
        cols = (["season"] + cols) if kind in ("transitions", "platoon") else cols
        parts = frames[kind]
        out[kind] = pd.concat(parts, ignore_index=True)[cols] if parts else pd.DataFrame(columns=cols)
    out["games"] = prepare_games(out["games"])
    out["players"] = load_players()
    return out


def line_runs(line: str, inning: int) -> float:
    """Runs a team scored in one inning of a line score (``"0 1 0 x"``)."""
    parts = str(line).split()
    if inning > len(parts) or parts[inning - 1] == "x":
        return np.nan
    return float(parts[inning - 1])


def innings_table(games: pd.DataFrame, max_inning: int = 9) -> pd.DataFrame:
    """Runs by inning for each team-game, from the line scores (NaN when not batted)."""
    rows = {}
    for side in ("home", "away"):
        lines = games[f"{side}_line"].fillna("").str.split()
        mat = np.full((len(games), max_inning), np.nan)
        for i, parts in enumerate(lines):
            for j, v in enumerate(parts[:max_inning]):
                if v != "x":
                    mat[i, j] = float(v)
        rows[side] = mat
    return rows


def today_et() -> dt.date:
    return pd.Timestamp.now(tz=DISPLAY_TZ).date()

