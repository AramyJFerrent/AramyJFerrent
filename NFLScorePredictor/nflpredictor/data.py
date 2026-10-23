"""Download nflverse data and reduce play-by-play to per-game summaries.

Raw play-by-play is about 20 MB a season, so it is downloaded to a local cache
and boiled down to two small CSVs per season that are committed to the repo:

- ``data/epa/{season}_teams.csv``: one row per team per game with the team's
  offensive efficiency and scoring events.
- ``data/epa/{season}_qbs.csv``: one row per quarterback per game with
  dropbacks and EPA, for the quarterback adjustment.

Only the current season is re-downloaded on routine updates.
"""

from __future__ import annotations

import datetime as dt
import logging
from pathlib import Path

import numpy as np
import pandas as pd
import requests
from bettingcore import fetch

from .config import (
    CACHE_DIR,
    EPA_DIR,
    FIRST_SEASON,
    GAMES_URL,
    KICKOFF_TZ,
    PBP_URL,
    TEAM_ALIASES,
)

log = logging.getLogger(__name__)

# Plays at a lopsided win probability say less about team quality.
LOPSIDED_WP = (0.10, 0.90)
LOPSIDED_WEIGHT = 0.35
# Who recovers a fumble is mostly luck, so lost fumbles count half.
FUMBLE_LOST_EPA_SCALE = 0.5

TEAM_COLUMNS = [
    "game_id", "season", "week", "season_type", "team", "opp", "home",
    "plays", "w", "epa", "success", "dropbacks",
    "pass_w", "pass_epa", "rush_w", "rush_epa", "st_epa", "drives",
    "tds", "fgs", "xp_att", "xp_made", "two_att", "two_made", "safeties",
]
SPECIAL_TEAMS = ["kickoff", "punt", "field_goal", "extra_point"]
# American prices posted with the closing (or current) lines in the schedule.
ODDS_COLUMNS = ["home_moneyline", "away_moneyline", "home_spread_odds", "away_spread_odds",
                "over_odds", "under_odds"]
QB_COLUMNS = ["game_id", "season", "week", "team", "qb_id", "qb_name", "dropbacks", "w", "epa"]


def current_season(today: dt.date | None = None) -> int:
    """The NFL season in progress, or the next one during the offseason."""
    today = today or dt.date.today()
    return today.year if today.month >= 3 else today.year - 1


def _alias(series: pd.Series) -> pd.Series:
    return series.replace(TEAM_ALIASES)


def prepare_games(raw: pd.DataFrame) -> pd.DataFrame:
    """Normalize the nflverse games file into the columns the model uses."""
    g = raw.copy()
    g["home_team"] = _alias(g["home_team"])
    g["away_team"] = _alias(g["away_team"])
    g["neutral"] = g["location"].eq("Neutral")
    g["playoff"] = g["game_type"].ne("REG")
    g["div_game"] = g["div_game"].fillna(0).astype(int)
    g["completed"] = g["home_score"].notna() & g["away_score"].notna()
    times = g["gametime"].fillna("13:00")
    local = pd.to_datetime(g["gameday"] + " " + times, errors="coerce")
    g["kickoff"] = local.dt.tz_localize(KICKOFF_TZ, ambiguous="NaT", nonexistent="NaT").dt.tz_convert("UTC")
    for col in ("home_rest", "away_rest"):
        g[col] = g[col].fillna(7)
    for col in ODDS_COLUMNS:
        if col not in g:
            g[col] = np.nan
    g = g.sort_values(["season", "week", "kickoff", "game_id"]).reset_index(drop=True)
    return g


def load_games(max_age_hours: float = 6.0) -> pd.DataFrame:
    path = fetch(GAMES_URL, CACHE_DIR / "games.csv", max_age_hours)
    return prepare_games(pd.read_csv(path))


def load_pbp(season: int, max_age_hours: float = 6.0) -> pd.DataFrame:
    path = fetch(PBP_URL.format(season=season), CACHE_DIR / f"pbp_{season}.parquet", max_age_hours)
    return pd.read_parquet(path)


def summarize_pbp(pbp: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Collapse one season of play-by-play into team-game and QB-game rows."""
    p = pbp.copy()
    for col in ("posteam", "defteam", "td_team", "home_team", "away_team"):
        p[col] = _alias(p[col])

    games = (
        p.dropna(subset=["home_team"])
        .groupby("game_id", as_index=False)
        .agg(season=("season", "first"), week=("week", "first"),
             season_type=("season_type", "first"),
             home_team=("home_team", "first"), away_team=("away_team", "first"))
    )
    sides = pd.concat([
        games.assign(team=games.home_team, opp=games.away_team, home=1),
        games.assign(team=games.away_team, opp=games.home_team, home=0),
    ])[["game_id", "season", "week", "season_type", "team", "opp", "home"]]

    plays = p[p["play_type"].isin(["pass", "run"]) & p["epa"].notna() & p["posteam"].notna()].copy()
    lo, hi = LOPSIDED_WP
    plays["w"] = np.where(plays["wp"].between(lo, hi), 1.0, LOPSIDED_WEIGHT)
    epa = plays["epa"].where(plays["fumble_lost"].fillna(0) == 0, plays["epa"] * FUMBLE_LOST_EPA_SCALE)
    plays["epa_w"] = epa * plays["w"]
    plays["success_w"] = plays["success"].fillna(0) * plays["w"]
    plays["dropback"] = plays["qb_dropback"].fillna(0)
    plays["pass_w"] = plays["w"] * plays["dropback"]
    plays["pass_epa"] = plays["epa_w"] * plays["dropback"]
    plays["rush_w"] = plays["w"] - plays["pass_w"]
    plays["rush_epa"] = plays["epa_w"] - plays["pass_epa"]
    offense = plays.groupby(["game_id", "posteam"]).agg(
        plays=("epa", "size"), w=("w", "sum"), epa=("epa_w", "sum"),
        success=("success_w", "sum"), dropbacks=("dropback", "sum"),
        pass_w=("pass_w", "sum"), pass_epa=("pass_epa", "sum"),
        rush_w=("rush_w", "sum"), rush_epa=("rush_epa", "sum"),
        drives=("fixed_drive", "nunique"),
    ).rename_axis(["game_id", "team"])

    # Special teams: kicking and return units together, as net EPA for the team.
    st = p[p["play_type"].isin(SPECIAL_TEAMS) & p["epa"].notna() & p["posteam"].notna()]
    st_epa = pd.concat([
        st.groupby(["game_id", "posteam"])["epa"].sum().rename_axis(["game_id", "team"]),
        -st.groupby(["game_id", "defteam"])["epa"].sum().rename_axis(["game_id", "team"]),
    ]).groupby(level=[0, 1]).sum().rename("st_epa")

    def count(mask: pd.Series, by: str, name: str) -> pd.Series:
        return p[mask.fillna(False)].groupby(["game_id", by]).size().rename_axis(["game_id", "team"]).rename(name)

    events = pd.concat([
        count(p["td_team"].notna(), "td_team", "tds"),
        count(p["field_goal_result"].eq("made"), "posteam", "fgs"),
        count(p["extra_point_attempt"].eq(1), "posteam", "xp_att"),
        count(p["extra_point_result"].eq("good"), "posteam", "xp_made"),
        count(p["two_point_attempt"].eq(1), "posteam", "two_att"),
        count(p["two_point_conv_result"].eq("success"), "posteam", "two_made"),
        count(p["safety"].eq(1), "defteam", "safeties"),
    ], axis=1)

    teams = (sides.join(offense, on=["game_id", "team"]).join(st_epa, on=["game_id", "team"])
             .join(events, on=["game_id", "team"]))
    count_cols = ["plays", "dropbacks", "drives", "tds", "fgs", "xp_att", "xp_made", "two_att",
                  "two_made", "safeties"]
    teams[count_cols] = teams[count_cols].fillna(0).astype(int)
    sums = ["w", "epa", "success", "pass_w", "pass_epa", "rush_w", "rush_epa", "st_epa"]
    teams[sums] = teams[sums].fillna(0.0)
    teams = teams[TEAM_COLUMNS].sort_values(["week", "game_id", "team"]).reset_index(drop=True)

    drops = plays[(plays["dropback"] == 1) & plays["id"].notna()]
    qbs = drops.groupby(["game_id", "posteam", "id"]).agg(
        season=("season", "first"), week=("week", "first"), qb_name=("name", "first"),
        dropbacks=("epa", "size"), w=("w", "sum"), epa=("epa_w", "sum"),
    ).reset_index().rename(columns={"posteam": "team", "id": "qb_id"})
    qbs = qbs[QB_COLUMNS].sort_values(["week", "game_id", "team", "dropbacks"],
                                      ascending=[True, True, True, False]).reset_index(drop=True)
    return teams, qbs


def summary_paths(season: int) -> tuple[Path, Path]:
    return EPA_DIR / f"{season}_teams.csv", EPA_DIR / f"{season}_qbs.csv"


def update_summaries(seasons: list[int], refresh: set[int] = frozenset(),
                     max_age_hours: float = 6.0) -> None:
    """Build missing season summaries and rebuild the ones in ``refresh``."""
    EPA_DIR.mkdir(parents=True, exist_ok=True)
    for season in seasons:
        team_path, qb_path = summary_paths(season)
        if team_path.exists() and qb_path.exists() and season not in refresh:
            continue
        try:
            pbp = load_pbp(season, max_age_hours)
        except requests.HTTPError as exc:
            log.info("No play-by-play for %s yet (%s)", season, exc)
            continue
        teams, qbs = summarize_pbp(pbp)
        teams.to_csv(team_path, index=False, float_format="%.4f")
        qbs.to_csv(qb_path, index=False, float_format="%.4f")
        log.info("Summarized %s: %d team-games, %d QB-games", season, len(teams), len(qbs))


def load_summaries(first: int = FIRST_SEASON, last: int | None = None) -> tuple[pd.DataFrame, pd.DataFrame]:
    """All committed team-game and QB-game summaries, oldest first."""
    teams, qbs = [], []
    for season in range(first, (last or current_season()) + 1):
        team_path, qb_path = summary_paths(season)
        if team_path.exists():
            teams.append(pd.read_csv(team_path))
            qbs.append(pd.read_csv(qb_path))
    if not teams:
        return pd.DataFrame(columns=TEAM_COLUMNS), pd.DataFrame(columns=QB_COLUMNS)
    # Older files may lack newer columns; those values load as missing.
    return (pd.concat(teams, ignore_index=True).reindex(columns=TEAM_COLUMNS),
            pd.concat(qbs, ignore_index=True))
