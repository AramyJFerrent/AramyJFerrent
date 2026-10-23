"""Paths, data sources and model hyperparameters."""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass, fields
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
GAMES_DIR = DATA_DIR / "games"
SHOT_MODEL_PATH = DATA_DIR / "shot_model.json"
LINES_PATH = DATA_DIR / "lines.csv"
CACHE_DIR = ROOT / ".cache"
OUTPUT_DIR = ROOT / "predictions"
PARAMS_PATH = ROOT / "params.json"

# sportsdataverse compiles the NHL web API (api-web.nhle.com) into season files
# every morning during the season and commits them to this repository. Seasons
# are named by the year they end: 2027 is 2026-27.
NHL_DATA_RAW = "https://raw.githubusercontent.com/sportsdataverse/fastRhockey-nhl-data/main/nhl"
SCHEDULE_URL = NHL_DATA_RAW + "/schedules/parquet/nhl_schedule_{season}.parquet"
PBP_URL = NHL_DATA_RAW + "/pbp_lite/parquet/play_by_play_lite_{season}.parquet"
GOALIE_BOX_URL = NHL_DATA_RAW + "/goalie_box/parquet/goalie_box_{season}.parquet"
SKATER_BOX_URL = NHL_DATA_RAW + "/skater_box/parquet/skater_box_{season}.parquet"

# First season summarized from play-by-play (2009-10). Ratings need a few
# seasons of burn-in before the backtest window so preseason priors mean something.
FIRST_SEASON = 2010
# The shot (expected-goals) model is fitted once on these seasons and frozen,
# so every later season, the backtest included, is scored by a model that never
# saw it, and an upstream change cannot shift old and new seasons apart.
SHOT_MODEL_SEASONS = (2011, 2015)
# Three-on-three overtime started in 2015-16; earlier overtimes were 4-on-4.
THREE_ON_THREE_SEASON = 2016

# Relocated franchises keep one code across seasons so priors carry over.
# Utah took over Arizona's roster in 2024 and Winnipeg is the former Atlanta club.
TEAM_ALIASES = {"ATL": "WPG", "PHX": "UTA", "ARI": "UTA"}

# Start times are stored in UTC; pages and game dates use US Eastern.
DISPLAY_TZ = "America/New_York"


def season_label(season: int) -> str:
    """2027 -> '2026-27'."""
    return f"{season - 1}-{str(season)[-2:]}"


@dataclass
class Hyperparams:
    """Ratings-engine settings chosen by walk-forward tuning (see `tune`).

    Everything fitted by regression (the goal-rate model, home ice, rest, the
    goalie weight, the market blend and the simulator) is re-estimated on every
    run from recent seasons, so only these structural knobs are fixed.
    """

    # Ridge strength pulling each team toward its preseason prior, in the
    # rating's own units: 5-on-5 minutes, power-play minutes, or games.
    ev_prior_minutes: float = 900.0
    pp_prior_minutes: float = 250.0
    goals_prior_games: float = 40.0
    # Share of last season's final rating kept as this season's prior. Team
    # strength carries over less in hockey than in any other major league.
    carryover: float = 0.5
    # Half-life, in days, of the recency weight on current-season games.
    half_life_days: float = 60.0
    # Goalies: unblocked shots of evidence before a goalie's own record
    # outweighs the prior, the prior for an unproven goalie (goals saved above
    # expected per 100 unblocked shots), and the half-life in days of old shots.
    goalie_prior_shots: float = 3000.0
    goalie_prior_value: float = -0.15
    goalie_half_life_days: float = 500.0
    # Seasons of history used to fit the goal-rate model, blend and simulator.
    fit_window_seasons: int = 4

    @classmethod
    def load(cls, path: Path = PARAMS_PATH) -> "Hyperparams":
        if not path.exists():
            return cls()
        raw = json.loads(path.read_text())
        known = {f.name for f in fields(cls)}
        return cls(**{k: v for k, v in raw.items() if k in known})

    def save(self, path: Path = PARAMS_PATH) -> None:
        path.write_text(json.dumps(asdict(self), indent=2) + "\n")
