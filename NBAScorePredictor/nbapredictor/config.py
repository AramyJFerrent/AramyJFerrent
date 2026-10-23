"""Paths, data sources and model hyperparameters."""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass, fields
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
GAMES_DIR = DATA_DIR / "games"
LINES_PATH = DATA_DIR / "lines.csv"
PLAYERS_PATH = DATA_DIR / "players.csv"
ARENAS_PATH = DATA_DIR / "arenas.csv"
CACHE_DIR = ROOT / ".cache"
OUTPUT_DIR = ROOT / "predictions"
PARAMS_PATH = ROOT / "params.json"

# sportsdataverse compiles ESPN's NBA schedules, box scores and play-by-play
# into season files every morning during the season (about 3 AM ET) and
# commits them to this repository. Seasons are named by the year they end:
# 2027 is 2026-27.
HOOPR_RAW = "https://raw.githubusercontent.com/sportsdataverse/hoopR-nba-data/main/nba"
SCHEDULE_URL = HOOPR_RAW + "/schedules/parquet/nba_schedule_{season}.parquet"
TEAM_BOX_URL = HOOPR_RAW + "/team_box/parquet/team_box_{season}.parquet"
PLAYER_BOX_URL = HOOPR_RAW + "/player_box/parquet/player_box_{season}.parquet"
PBP_URL = HOOPR_RAW + "/pbp/parquet/play_by_play_{season}.parquet"
ROSTERS_URL = HOOPR_RAW + "/rosters/parquet/rosters_{season}.parquet"

# Closing spreads, totals and moneylines for 2007-08 to January 2026, the
# dataset the techniques report's benchmarks were computed on, and opening and
# closing lines for 2011-12 to 2021-22 from sportsbookreview.com.
KYLESKOM_ODDS_URL = ("https://raw.githubusercontent.com/kyleskom/NBA-Machine-Learning-Sports-Betting/"
                     "master/Data/OddsData.sqlite")
SBR_ARCHIVE_URL = ("https://raw.githubusercontent.com/flancast90/sportsbookreview-scraper/"
                   "main/data/nba_archive_10Y.json")

# First season summarized (2007-08). Ratings need a few seasons of burn-in
# before the backtest window so preseason priors mean something.
FIRST_SEASON = 2008

# ESPN's codes, mapped to the NBA's own, with relocated franchises kept under
# one code across seasons so priors carry over.
TEAM_ALIASES = {"GS": "GSW", "NY": "NYK", "SA": "SAS", "NO": "NOP", "NOH": "NOP", "NOK": "NOP",
                "UTAH": "UTA", "WSH": "WAS", "NJ": "BKN", "SEA": "OKC"}
NBA_TEAMS = ("ATL", "BOS", "BKN", "CHA", "CHI", "CLE", "DAL", "DEN", "DET", "GSW", "HOU", "IND", "LAC",
             "LAL", "MEM", "MIA", "MIL", "MIN", "NOP", "NYK", "OKC", "ORL", "PHI", "PHX", "POR", "SAC",
             "SAS", "TOR", "UTA", "WAS")

# ESPN's team ids, for its injury report and roster endpoints.
ESPN_TEAM_IDS = {"1": "ATL", "2": "BOS", "3": "NOP", "4": "CHI", "5": "CLE", "6": "DAL", "7": "DEN", "8": "DET",
                 "9": "GSW", "10": "HOU", "11": "IND", "12": "LAC", "13": "LAL", "14": "MIA", "15": "MIL",
                 "16": "MIN", "17": "BKN", "18": "NYK", "19": "ORL", "20": "PHI", "21": "PHX", "22": "POR",
                 "23": "SAC", "24": "SAS", "25": "OKC", "26": "UTA", "27": "WAS", "28": "TOR", "29": "MEM",
                 "30": "CHA"}

# Start times are stored in UTC; pages and game dates use US Eastern.
DISPLAY_TZ = "America/New_York"

# Regulation length and each overtime, in minutes.
REG_MINUTES = 48.0
OT_MINUTES = 5.0


def season_label(season: int) -> str:
    """2027 -> '2026-27'."""
    return f"{season - 1}-{str(season)[-2:]}"


@dataclass
class Hyperparams:
    """Ratings-engine settings chosen by walk-forward tuning (see `tune`).

    Everything fitted by regression (the efficiency and pace maps, home court,
    rest and travel, the weight on player availability, the market blend and
    the score simulator) is re-estimated on every run from recent seasons, so
    only these structural knobs are fixed.
    """

    # Team ratings: ridge strength pulling each team toward its preseason
    # prior, in possessions for efficiency and in games for pace, and the
    # share of last season's final rating kept as this season's prior.
    team_prior_poss: float = 1500.0
    pace_prior_games: float = 10.0
    team_carryover: float = 0.6
    # Half-life, in days, of the recency weight on current-season games, for
    # efficiency and for pace (pace changes faster than quality does).
    half_life_days: float = 60.0
    pace_half_life_days: float = 15.0
    # Player ratings (RAPM): ridge strength in possessions toward each
    # player's prior, offense and defense separately, the share of last
    # season's rating kept, and the half-life in days of this season's stints.
    player_off_prior_poss: float = 3000.0
    player_def_prior_poss: float = 4000.0
    player_carryover: float = 0.85
    player_half_life_days: float = 120.0
    # Prior for a player with no rating yet (a rookie or a newcomer to the
    # league), in net points per 100 possessions, split between offense and
    # defense.
    newcomer_net: float = -2.0
    # Box-score prior: the minutes this season after which a player's prior is
    # halfway from its anchor to his box-score (SPM) ratings, for newcomers and
    # for players rated last season; 0 leaves the prior at its anchor.
    box_prior_minutes_new: float = 0.0
    box_prior_minutes: float = 0.0
    # Minutes projection: half-life, in games, of a player's recent minutes.
    minutes_half_life_games: float = 6.0
    # Seasons of history used to fit the points map, blend and simulator.
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
