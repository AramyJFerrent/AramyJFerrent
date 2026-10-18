"""Paths, data sources and model hyperparameters."""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass, fields
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
TEAM_GAMES_DIR = DATA_DIR / "team_games"
PRODUCTION_DIR = DATA_DIR / "production"
LINES_PATH = DATA_DIR / "lines.csv"
RETURNING_PATH = DATA_DIR / "returning.csv"
VENUES_PATH = DATA_DIR / "venues.csv"
CACHE_DIR = ROOT / ".cache"
OUTPUT_DIR = ROOT / "predictions"
PARAMS_PATH = ROOT / "params.json"

# cfbfastR-data (sportsdataverse) keeps schedules, rosters, team info and the
# multi-book betting file in its repository tree, refreshed daily in season.
CFBFASTR_RAW = "https://raw.githubusercontent.com/sportsdataverse/cfbfastR-data/main"
SCHEDULE_URL = CFBFASTR_RAW + "/schedules/csv/cfb_schedules_{season}.csv"
ROSTER_URL = CFBFASTR_RAW + "/rosters/csv/cfb_rosters_{season}.csv"
TEAM_INFO_URL = CFBFASTR_RAW + "/team_info/parquet/cfb_team_info_{season}.parquet"
LINES_URL = CFBFASTR_RAW + "/betting/csv/cfb_line_odds.csv.gz"
# Play-by-play with EPA is published as release assets, 2014 onward.
PBP_URL = (
    "https://github.com/sportsdataverse/sportsdataverse-data/releases/download/"
    "cfbfastR_cfb_pbp/play_by_play_{season}.parquet"
)

# First season with EPA play-by-play. It only seeds the ratings; predictions
# and the backtest start once a season has a preseason prior behind it.
FIRST_SEASON = 2014
# Schedules (scores only) go back further, which gives the Elo baseline and the
# very first preseason prior some history to start from.
ELO_FIRST_SEASON = 2005

# Kickoff times are stored in UTC; pages show US Eastern.
DISPLAY_TZ = "America/New_York"

# Postseason games are numbered week 1 in the source schedules. They are moved
# after the regular season (week 17 on), one week per seven days of bowls.
POSTSEASON_FIRST_WEEK = 17


@dataclass
class Hyperparams:
    """Ratings-engine settings chosen by walk-forward tuning (see `tune`).

    Everything fitted by regression (the preseason prior, the ratings-to-points
    map, home field, the market blend and the score dispersion) is re-estimated
    on every run from recent seasons, so only these structural knobs are fixed.
    """

    # Ridge strength, in plays, pulling each team toward its preseason prior.
    off_prior_plays: float = 400.0
    def_prior_plays: float = 600.0
    # Ridge strength, in plays, pulling each conference's average toward its
    # preseason level. Small values let a whole conference move together when
    # its nonconference results say it was misjudged; in walk-forward tests
    # that never beat letting teams move one at a time, so it is set high.
    conf_prior_plays: float = 15000.0
    # Half-life, in weeks, of the recency weight on current-season games.
    half_life_weeks: float = 30.0
    # Weight on plays in garbage time (CFBD definition: a lead of more than 38
    # points in the second quarter, 28 in the third or 22 in the fourth).
    garbage_weight: float = 0.0
    # Seasons of history used to fit the points map, blend and dispersion.
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
