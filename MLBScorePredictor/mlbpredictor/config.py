"""Paths, data sources, team codes and model hyperparameters."""

from __future__ import annotations

import datetime as dt
import json
from dataclasses import asdict, dataclass, fields
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
GAMES_DIR = DATA_DIR / "games"
PLAYERS_PATH = DATA_DIR / "players.csv"
PINNACLE_PATH = DATA_DIR / "pinnacle_2016.csv"
CACHE_DIR = ROOT / ".cache"
OUTPUT_DIR = ROOT / "predictions"
PARAMS_PATH = ROOT / "params.json"

# Retrosheet play-by-play, as mirrored by the Chadwick Baseball Bureau. A
# season appears there a few months after it ends; until then the season is
# read from the MLB Stats API instead.
RETRO_URL = "https://raw.githubusercontent.com/chadwickbureau/retrosheet/master/seasons/{season}/{name}"
REGISTER_URL = "https://raw.githubusercontent.com/chadwickbureau/register/master/data/people-{part}.csv"
STATSAPI_URL = "https://statsapi.mlb.com/api/v1"
PINNACLE_URL = "https://raw.githubusercontent.com/marcoblume/pinnacle.data/master/data/MLB2016.rda"

# First season summarized. Player ratings need a few seasons of history before
# the backtest window, so the first backtest season is 2016.
FIRST_SEASON = 2012
# Extra innings start with a runner on second in the regular season from 2020.
GHOST_RUNNER_SEASON = 2020
# Pitch clock, shift limits and bigger bases: a new scoring and running level.
RULES_2023_SEASON = 2023

# Start times are stored in UTC; pages and game dates use US Eastern.
DISPLAY_TZ = "America/New_York"

TEAMS = ["ARI", "ATH", "ATL", "BAL", "BOS", "CHC", "CIN", "CLE", "COL", "CWS", "DET", "HOU", "KC", "LAA",
         "LAD", "MIA", "MIL", "MIN", "NYM", "NYY", "PHI", "PIT", "SD", "SEA", "SF", "STL", "TB", "TEX",
         "TOR", "WSH"]
# Retrosheet team codes. Oakland and Sacramento are one franchise (ATH), as
# are the Florida and Miami Marlins.
RETRO_TEAMS = {"ANA": "LAA", "ARI": "ARI", "ATH": "ATH", "OAK": "ATH", "ATL": "ATL", "BAL": "BAL",
               "BOS": "BOS", "CHA": "CWS", "CHN": "CHC", "CIN": "CIN", "CLE": "CLE", "COL": "COL",
               "DET": "DET", "HOU": "HOU", "KCA": "KC", "LAN": "LAD", "MIA": "MIA", "FLO": "MIA",
               "MIL": "MIL", "MIN": "MIN", "NYA": "NYY", "NYN": "NYM", "PHI": "PHI", "PIT": "PIT",
               "SDN": "SD", "SEA": "SEA", "SFN": "SF", "SLN": "STL", "TBA": "TB", "TEX": "TEX",
               "TOR": "TOR", "WAS": "WSH"}
# MLB Stats API team ids.
MLB_TEAM_IDS = {108: "LAA", 109: "ARI", 110: "BAL", 111: "BOS", 112: "CHC", 113: "CIN", 114: "CLE",
                115: "COL", 116: "DET", 117: "HOU", 118: "KC", 119: "LAD", 120: "WSH", 121: "NYM",
                133: "ATH", 134: "PIT", 135: "SD", 136: "SEA", 137: "SF", 138: "STL", 139: "TB",
                140: "TEX", 141: "TOR", 142: "MIN", 143: "PHI", 144: "ATL", 145: "CWS", 146: "MIA",
                147: "NYY", 158: "MIL"}
# Time zone of each team's home park, for Retrosheet's local start times.
TEAM_TZ = {
    "ARI": "America/Phoenix", "ATH": "America/Los_Angeles", "ATL": "America/New_York",
    "BAL": "America/New_York", "BOS": "America/New_York", "CHC": "America/Chicago",
    "CIN": "America/New_York", "CLE": "America/New_York", "COL": "America/Denver",
    "CWS": "America/Chicago", "DET": "America/New_York", "HOU": "America/Chicago",
    "KC": "America/Chicago", "LAA": "America/Los_Angeles", "LAD": "America/Los_Angeles",
    "MIA": "America/New_York", "MIL": "America/Chicago", "MIN": "America/Chicago",
    "NYM": "America/New_York", "NYY": "America/New_York", "PHI": "America/New_York",
    "PIT": "America/New_York", "SD": "America/Los_Angeles", "SEA": "America/Los_Angeles",
    "SF": "America/Los_Angeles", "STL": "America/Chicago", "TB": "America/New_York",
    "TEX": "America/Chicago", "TOR": "America/Toronto", "WSH": "America/New_York",
}
# Home parks that changed after the latest Retrosheet season, by team and
# first season, as Retrosheet park ids. The Rays played 2025 in Tampa while
# Tropicana Field was repaired.
PARK_MOVES = {"TB": {2025: "TAM02", 2026: "STP01"}, "ATH": {2025: "SAC01"}}
# MLB Stats API game types: R regular season; F wild card, D division
# series, L league championship, W World Series.
POSTSEASON_TYPES = ("F", "D", "L", "W")
GAME_TYPES = ("R",) + POSTSEASON_TYPES


def current_season(today: dt.date | None = None) -> int:
    """The MLB season in play: the calendar year, or next year's from December."""
    today = today or dt.date.today()
    return today.year + 1 if today.month == 12 else today.year


@dataclass
class Hyperparams:
    """Ratings settings chosen by walk-forward tuning (see ``tune``).

    Everything fitted by regression (the run model, home field, park and
    weather effects, the market blend and the simulator) is re-estimated on
    every run from recent seasons, so only these structural knobs are fixed.
    """

    # Half-life, in days of the season, of the weight on a player's past
    # plate appearances. Off-seasons do not count as time.
    batter_half_life: float = 300.0
    pitcher_half_life: float = 250.0
    # Multiplier on each event's empirical-Bayes shrinkage (its
    # stabilization point, measured from history). Above 1 trusts the
    # player's own record less.
    batter_shrink: float = 1.0
    pitcher_shrink: float = 1.0
    # Starts of evidence before a pitcher's own innings per start outweighs
    # the league average, and the half-life (days) of old starts.
    starter_outs_prior: float = 4.0
    starter_outs_half_life: float = 60.0
    # Seasons of park history behind each park factor, and how many games of
    # evidence it takes for a park's own record to outweigh 1.0.
    park_seasons: int = 3
    park_prior_games: float = 120.0
    # Team ratings on runs: games of evidence before a team's own record
    # outweighs its preseason prior, the share of last season's rating kept
    # as that prior, and the half-life (days) of old games.
    team_prior_games: float = 40.0
    team_carryover: float = 0.6
    team_half_life: float = 60.0
    # Weight on the model's run levels against the betting market's, fitted
    # on Pinnacle's 2016 closing lines by the backtest; live games refine it.
    market_weight: float = 0.3
    # Seasons of history used to fit the run model, blend and simulator.
    fit_window_seasons: int = 3

    @classmethod
    def load(cls, path: Path = PARAMS_PATH) -> "Hyperparams":
        if not path.exists():
            return cls()
        raw = json.loads(path.read_text())
        known = {f.name for f in fields(cls)}
        return cls(**{k: v for k, v in raw.items() if k in known})

    def save(self, path: Path = PARAMS_PATH) -> None:
        path.write_text(json.dumps(asdict(self), indent=2) + "\n")
