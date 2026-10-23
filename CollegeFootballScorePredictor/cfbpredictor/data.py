"""Download cfbfastR data and reduce play-by-play to per-game summaries.

Raw play-by-play is 60-70 MB a season, so it is downloaded to a local cache
and boiled down to small CSVs per season that are committed to the repo:

- ``data/team_games/{season}.csv``: one row per team per game with the team's
  offensive efficiency, special teams, pace and field goals.
- ``data/team_games/{season}_lines.csv``: the betting line attached to each
  game's play-by-play.
- ``data/production/{season}.csv``: each player's season production, which
  next season's rosters turn into returning production.

Games between two FBS or FCS teams are kept, so FCS teams get ratings of their
own rather than being treated as one generic opponent. Only the current season
is re-downloaded on routine updates.
"""

from __future__ import annotations

import datetime as dt
import logging
from pathlib import Path

import numpy as np
import pandas as pd
import requests
from bettingcore import fetch as _fetch

from .config import (
    CACHE_DIR,
    FIRST_SEASON,
    PBP_URL,
    POSTSEASON_FIRST_WEEK,
    PRODUCTION_DIR,
    ROSTER_URL,
    SCHEDULE_URL,
    TEAM_GAMES_DIR,
    TEAM_INFO_URL,
)

log = logging.getLogger(__name__)

DIVISIONS = ("fbs", "fcs")
# CFBD garbage time: plays where the lead exceeds these margins, by quarter.
GARBAGE_MARGINS = {2: 38, 3: 28, 4: 22}
# Who recovers a fumble is mostly luck, so lost fumbles count half.
FUMBLE_LOST_EPA_SCALE = 0.5
LOST_FUMBLE_TYPES = {"Fumble Recovery (Opponent)", "Fumble Recovery (Opponent) Touchdown",
                     "Fumble Return Touchdown"}
# Plays on which a fumble ends a run or pass but the source left both the
# rush and pass flags unset.
FUMBLE_TYPES = LOST_FUMBLE_TYPES | {"Fumble Recovery (Own)", "Fumble"}
SPECIAL_TEAMS = {
    "Kickoff", "Kickoff Return (Offense)", "Kickoff Return Touchdown", "Punt",
    "Punt Return Touchdown", "Blocked Punt", "Blocked Punt Touchdown", "Field Goal Good",
    "Field Goal Missed", "Blocked Field Goal", "Blocked Field Goal Touchdown",
    "Missed Field Goal Return", "Missed Field Goal Return Touchdown", "Punt Team Fumble Recovery",
}

TEAM_COLUMNS = [
    "game_id", "season", "week", "season_type", "team", "opp", "home", "neutral",
    "division", "opp_division", "conference", "opp_conference",
    "plays", "w", "epa", "success", "pass_w", "pass_epa", "rush_w", "rush_epa",
    "st_epa", "drives", "fgs", "g_plays", "g_epa",
]
PRODUCTION_COLUMNS = ["athlete_id", "team", "pass_yds", "rec_yds", "rush_yds", "def_plays"]
GAME_COLUMNS = [
    "game_id", "season", "week", "season_type", "kickoff", "start_time_tbd", "completed",
    "neutral", "conference_game", "venue_id", "venue", "home_team", "away_team",
    "home_division", "away_division", "home_conference", "away_conference",
    "home_score", "away_score", "notes", "bowl", "playoff",
]


def fetch(url: str, path: Path, max_age_hours: float = 6.0, retries: int = 4) -> Path:
    """Download ``url`` to ``path`` unless a fresh enough copy exists (``bettingcore.fetch``)."""
    return _fetch(url, path, max_age_hours, retries, timeout=180)


def current_season(today: dt.date | None = None) -> int:
    """The season in progress, or the next one during the offseason.

    Bowls and the playoff finish in January, so the season rolls over in March.
    """
    today = today or dt.date.today()
    return today.year if today.month >= 3 else today.year - 1


def _age(season: int, current: int, max_age_hours: float) -> float:
    """Finished seasons never change, so their downloads are reused for a month."""
    return max_age_hours if season >= current else 24.0 * 30


def season_weeks(season_type: pd.Series, week: pd.Series, kickoff: pd.Series,
                 season: pd.Series) -> pd.Series:
    """Regular-season week, or a postseason week after it (17, 18, ...)."""
    post = season_type.eq("postseason")
    weeks = week.astype(int).copy()
    if post.any():
        first = kickoff[post].groupby(season[post]).transform("min")
        days = (kickoff[post] - first).dt.days
        weeks[post] = POSTSEASON_FIRST_WEEK + (days // 7).astype(int)
    return weeks


def prepare_games(raw: pd.DataFrame) -> pd.DataFrame:
    """Normalize a cfbfastR schedule into the columns the model uses.

    Keeps games involving at least one FBS team whose opponent is FBS or FCS.
    """
    g = raw.copy()
    g = g[g["home_division"].isin(DIVISIONS) & g["away_division"].isin(DIVISIONS)
          & (g["home_division"].eq("fbs") | g["away_division"].eq("fbs"))].copy()
    g["kickoff"] = pd.to_datetime(g["start_date"], utc=True, errors="coerce")
    g["season_type"] = g["season_type"].fillna("regular")
    g["week"] = season_weeks(g["season_type"], g["week"], g["kickoff"], g["season"])
    g["neutral"] = g["neutral_site"].fillna(False).astype(bool)
    g["conference_game"] = g["conference_game"].fillna(False).astype(bool)
    g["start_time_tbd"] = g["start_time_tbd"].fillna(False).astype(bool)
    g["home_score"] = pd.to_numeric(g["home_points"], errors="coerce")
    g["away_score"] = pd.to_numeric(g["away_points"], errors="coerce")
    g["completed"] = g["completed"].fillna(False).astype(bool) & g["home_score"].notna() \
        & g["away_score"].notna()
    notes = g["notes"].fillna("").astype(str) if "notes" in g else pd.Series("", index=g.index)
    g["notes"] = notes
    g["playoff"] = notes.str.contains("College Football Playoff", case=False)
    g["bowl"] = g["season_type"].eq("postseason") & ~g["playoff"]
    g["game_id"] = g["game_id"].astype(int)
    return g.sort_values(["season", "week", "kickoff", "game_id"]).reset_index(drop=True)[GAME_COLUMNS]


def load_games(first: int, last: int, max_age_hours: float = 6.0) -> pd.DataFrame:
    current = current_season()
    frames = []
    for season in range(first, last + 1):
        try:
            path = fetch(SCHEDULE_URL.format(season=season), CACHE_DIR / f"schedule_{season}.csv",
                         _age(season, current, max_age_hours))
        except requests.HTTPError as exc:
            log.info("No schedule for %s yet (%s)", season, exc)
            continue
        frames.append(prepare_games(pd.read_csv(path, low_memory=False)))
    return pd.concat(frames, ignore_index=True)


def load_team_info(season: int, max_age_hours: float = 6.0) -> pd.DataFrame:
    path = fetch(TEAM_INFO_URL.format(season=season), CACHE_DIR / f"team_info_{season}.parquet",
                 _age(season, current_season(), max_age_hours))
    return pd.read_parquet(path)


def load_roster(season: int, max_age_hours: float = 6.0) -> pd.DataFrame:
    path = fetch(ROSTER_URL.format(season=season), CACHE_DIR / f"roster_{season}.csv",
                 _age(season, current_season(), max_age_hours))
    return pd.read_csv(path, usecols=["athlete_id", "team", "position", "season"], low_memory=False)


def load_pbp(season: int, max_age_hours: float = 6.0) -> pd.DataFrame:
    path = fetch(PBP_URL.format(season=season), CACHE_DIR / f"pbp_{season}.parquet",
                 _age(season, current_season(), max_age_hours))
    return pd.read_parquet(path)


def team_divisions(team_info: pd.DataFrame) -> pd.DataFrame:
    """Division (fbs, fcs, ...) and conference for every team in one season."""
    t = team_info.drop_duplicates("school").set_index("school")
    return pd.DataFrame({"division": t["classification"], "conference": t["conference"]})


def _ids(series: pd.Series) -> pd.Series:
    return pd.to_numeric(series, errors="coerce").astype("Int64")


def summarize_pbp(pbp: pd.DataFrame, teams: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Collapse one season of play-by-play into team-game and player rows.

    ``teams`` gives each team's division and conference (``team_divisions``),
    used where the play-by-play leaves them blank (most FCS-only games).
    Efficiency columns exclude garbage time; garbage-time plays and EPA are
    kept separately (``g_plays``, ``g_epa``) so their weight can be tuned.
    """
    p = pbp.copy()
    p["kickoff"] = pd.to_datetime(p["start_date"], utc=True, errors="coerce")
    p["season_type"] = p["season_type"].fillna("regular")
    p["week"] = season_weeks(p["season_type"], p["week"], p["kickoff"], p["season"])
    for side in ("home", "away"):
        p[f"{side}_div"] = p[f"{side}_team_division"].fillna(p[side].map(teams["division"]))
        p[f"{side}_conf"] = p[f"{side}_team_conference"].fillna(p[side].map(teams["conference"]))

    games = (
        p.dropna(subset=["home", "away"])
        .groupby("game_id", as_index=False)
        .agg(season=("season", "first"), week=("week", "first"), season_type=("season_type", "first"),
             home_team=("home", "first"), away_team=("away", "first"),
             neutral=("neutral_site", "first"), home_div=("home_div", "first"),
             away_div=("away_div", "first"), home_conf=("home_conf", "first"),
             away_conf=("away_conf", "first"))
    )
    games = games[games["home_div"].isin(DIVISIONS) & games["away_div"].isin(DIVISIONS)]
    games["neutral"] = games["neutral"].fillna(False).astype(bool)
    sides = pd.concat([
        games.assign(team=games.home_team, opp=games.away_team, home=1,
                     division=games.home_div, opp_division=games.away_div,
                     conference=games.home_conf, opp_conference=games.away_conf),
        games.assign(team=games.away_team, opp=games.home_team, home=0,
                     division=games.away_div, opp_division=games.home_div,
                     conference=games.away_conf, opp_conference=games.home_conf),
    ])[TEAM_COLUMNS[:12]]

    p = p[p["game_id"].isin(games["game_id"]) & p["pos_team"].notna()].copy()
    margin = p["pos_score_diff_start"].abs()
    limit = p["period"].map(GARBAGE_MARGINS)
    garbage = limit.notna() & (margin > limit)
    p["w"] = np.where(garbage, 0.0, 1.0)
    text = p["play_text"].fillna("")
    kneel = text.str.contains("kneel", case=False)
    is_fumble = p["play_type"].isin(FUMBLE_TYPES) & text.str.contains(r" rush | pass |sacked", regex=True)
    scrimmage = ((p["pass"].eq(1) | p["rush"].eq(1) | is_fumble) & ~kneel & p["EPA"].notna())

    plays = p[scrimmage].copy()
    epa = plays["EPA"].where(~plays["play_type"].isin(LOST_FUMBLE_TYPES),
                             plays["EPA"] * FUMBLE_LOST_EPA_SCALE)
    plays["epa_w"] = epa * plays["w"]
    plays["g_w"] = 1.0 - plays["w"]
    plays["g_epa"] = epa * plays["g_w"]
    plays["success_w"] = plays["success"].fillna(0) * plays["w"]
    plays["dropback"] = plays["pass"].fillna(0).eq(1).astype(float)   # passes and sacks
    plays["pass_w"] = plays["w"] * plays["dropback"]
    plays["pass_epa"] = plays["epa_w"] * plays["dropback"]
    plays["rush_w"] = plays["w"] - plays["pass_w"]
    plays["rush_epa"] = plays["epa_w"] - plays["pass_epa"]
    offense = plays.groupby(["game_id", "pos_team"]).agg(
        plays=("EPA", "size"), w=("w", "sum"), epa=("epa_w", "sum"),
        success=("success_w", "sum"), pass_w=("pass_w", "sum"), pass_epa=("pass_epa", "sum"),
        rush_w=("rush_w", "sum"), rush_epa=("rush_epa", "sum"),
        g_plays=("g_w", "sum"), g_epa=("g_epa", "sum"),
    ).rename_axis(["game_id", "team"])

    # Special teams: kicking and return units together, as net EPA for the team.
    st = p[p["play_type"].isin(SPECIAL_TEAMS) & p["EPA"].notna()].copy()
    st["epa_w"] = st["EPA"] * st["w"]
    st_epa = pd.concat([
        st.groupby(["game_id", "pos_team"])["epa_w"].sum().rename_axis(["game_id", "team"]),
        -st.groupby(["game_id", "def_pos_team"])["epa_w"].sum().rename_axis(["game_id", "team"]),
    ]).groupby(level=[0, 1]).sum().rename("st_epa")

    # Possessions: drives with a snap, punt or field goal try.
    poss = p[scrimmage | p["play_type"].isin(SPECIAL_TEAMS - {"Kickoff", "Kickoff Return (Offense)",
                                                               "Kickoff Return Touchdown"})]
    drives = poss.groupby(["game_id", "pos_team"])["drive_id"].nunique().rename_axis(
        ["game_id", "team"]).rename("drives")
    fgs = p[p["play_type"].eq("Field Goal Good")].groupby(["game_id", "pos_team"]).size().rename_axis(
        ["game_id", "team"]).rename("fgs")

    out = (sides.join(offense, on=["game_id", "team"]).join(st_epa, on=["game_id", "team"])
           .join(drives, on=["game_id", "team"]).join(fgs, on=["game_id", "team"]))
    counts = ["plays", "drives", "fgs", "g_plays"]
    out[counts] = out[counts].fillna(0).astype(int)
    sums = ["w", "epa", "success", "pass_w", "pass_epa", "rush_w", "rush_epa", "st_epa", "g_epa"]
    out[sums] = out[sums].fillna(0.0)
    out["game_id"] = out["game_id"].astype(int)
    out = out[TEAM_COLUMNS].sort_values(["week", "game_id", "team"]).reset_index(drop=True)

    return out, player_production(p[p["w"] > 0])


def player_production(p: pd.DataFrame) -> pd.DataFrame:
    """Each player's passing, receiving and rushing yards and defensive plays made."""
    parts = []
    for id_col, value, team_col, name in (
        ("completion_player_id", "completion_yds", "pos_team", "pass_yds"),
        ("reception_player_id", "reception_yds", "pos_team", "rec_yds"),
        ("rush_player_id", "rush_yds", "pos_team", "rush_yds"),
    ):
        d = p[[id_col, value, team_col]].dropna(subset=[id_col])
        parts.append(d.assign(athlete_id=_ids(d[id_col]), team=d[team_col],
                              v=pd.to_numeric(d[value], errors="coerce").fillna(0.0))
                     .groupby(["athlete_id", "team"])["v"].sum().rename(name))
    defense = []
    for id_col in ("sack_player_id", "interception_player_id", "pass_breakup_player_id",
                   "fumble_forced_player_id"):
        d = p[[id_col, "def_pos_team"]].dropna(subset=[id_col])
        defense.append(pd.DataFrame({"athlete_id": _ids(d[id_col]), "team": d["def_pos_team"]}))
    d = pd.concat(defense, ignore_index=True)
    parts.append(d.groupby(["athlete_id", "team"]).size().rename("def_plays").astype(float))
    prod = pd.concat(parts, axis=1).fillna(0.0).reset_index()
    prod = prod[prod["athlete_id"].notna()]
    # The long tail of a few yards here and there barely moves team shares.
    keep = (prod[["pass_yds", "rec_yds", "rush_yds"]].abs().sum(axis=1) >= 20) | (prod["def_plays"] > 0)
    prod = prod[keep]
    prod[["pass_yds", "rec_yds", "rush_yds", "def_plays"]] = prod[
        ["pass_yds", "rec_yds", "rush_yds", "def_plays"]].round().astype(int)
    return prod[PRODUCTION_COLUMNS].sort_values(["team", "athlete_id"]).reset_index(drop=True)


def pbp_lines(pbp: pd.DataFrame) -> pd.DataFrame:
    """The one line attached to each game's play-by-play, as home margin and total."""
    g = pbp.groupby("game_id").agg(season=("season", "first"), spread=("spread", "first"),
                                   total=("over_under", "first")).reset_index()
    out = pd.DataFrame({
        "game_id": g["game_id"].astype(int), "season": g["season"].astype(int),
        "spread_line": -pd.to_numeric(g["spread"], errors="coerce"),
        "total_line": pd.to_numeric(g["total"], errors="coerce"),
    })
    out.loc[out["total_line"] <= 0, "total_line"] = np.nan
    return out[out["spread_line"].notna() | out["total_line"].notna()].reset_index(drop=True)


def summary_paths(season: int) -> tuple[Path, Path, Path]:
    """Team-game, player-production and line files for one season."""
    return (TEAM_GAMES_DIR / f"{season}.csv", PRODUCTION_DIR / f"{season}.csv",
            TEAM_GAMES_DIR / f"{season}_lines.csv")


def update_summaries(seasons: list[int], refresh: set[int] = frozenset(),
                     max_age_hours: float = 6.0, keep_raw: bool = True) -> None:
    """Build missing season summaries and rebuild the ones in ``refresh``."""
    TEAM_GAMES_DIR.mkdir(parents=True, exist_ok=True)
    PRODUCTION_DIR.mkdir(parents=True, exist_ok=True)
    for season in seasons:
        paths = summary_paths(season)
        if all(p.exists() for p in paths) and season not in refresh:
            continue
        try:
            pbp = load_pbp(season, max_age_hours)
        except requests.HTTPError as exc:
            log.info("No play-by-play for %s yet (%s)", season, exc)
            continue
        teams = team_divisions(load_team_info(season, max_age_hours))
        team_games, prod = summarize_pbp(pbp, teams)
        team_games.to_csv(paths[0], index=False, float_format="%.4f")
        prod.to_csv(paths[1], index=False)
        pbp_lines(pbp).to_csv(paths[2], index=False, float_format="%.1f")
        log.info("Summarized %s: %d team-games, %d players", season, len(team_games), len(prod))
        if not keep_raw:
            (CACHE_DIR / f"pbp_{season}.parquet").unlink(missing_ok=True)


def load_summaries(first: int = FIRST_SEASON, last: int | None = None) -> pd.DataFrame:
    """All committed team-game summaries, oldest first."""
    teams = [pd.read_csv(path) for season in range(first, (last or current_season()) + 1)
             if (path := summary_paths(season)[0]).exists()]
    if not teams:
        return pd.DataFrame(columns=TEAM_COLUMNS)
    return pd.concat(teams, ignore_index=True).reindex(columns=TEAM_COLUMNS)


def load_production(season: int) -> pd.DataFrame:
    path = summary_paths(season)[1]
    return pd.read_csv(path) if path.exists() else pd.DataFrame(columns=PRODUCTION_COLUMNS)
