"""Paths, data sources, divisions and model hyperparameters."""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass, fields
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
CACHE_DIR = ROOT / ".cache"
OUTPUT_DIR = ROOT / "predictions"
PARAMS_PATH = ROOT / "params.json"

# UFCStats scrape, refreshed by its maintainer after every event.
SCRAPE_URL = "https://raw.githubusercontent.com/Greco1899/scrape_ufc_stats/main/{name}.csv"
SCRAPE_FILES = ["ufc_event_details", "ufc_fight_results", "ufc_fight_stats", "ufc_fighter_tott"]
# Moneyline and method odds for UFC fights since 2010 (Ultimate UFC Dataset).
ODDS_URL = "https://raw.githubusercontent.com/shortlikeafox/ultimate_ufc_dataset/master/ufc-master.csv"

# Upcoming cards: UFCStats lists every announced bout with the same fighter ids
# as the history; ESPN adds bout start times and moneylines.
UFCSTATS_UPCOMING_URL = "http://ufcstats.com/statistics/events/upcoming"
ESPN_SCOREBOARD_URL = "https://site.api.espn.com/apis/site/v2/sports/mma/ufc/scoreboard"

DISPLAY_TZ = "America/New_York"

# Division name -> weight limit in pounds. Women's divisions carry the prefix.
DIVISIONS = {
    "Flyweight": 125, "Bantamweight": 135, "Featherweight": 145, "Lightweight": 155,
    "Welterweight": 170, "Middleweight": 185, "Light Heavyweight": 205, "Heavyweight": 265,
    "Women's Strawweight": 115, "Women's Flyweight": 125, "Women's Bantamweight": 135,
    "Women's Featherweight": 145,
}
DIVISION_ABBR = {
    "Flyweight": "FLW", "Bantamweight": "BW", "Featherweight": "FW", "Lightweight": "LW",
    "Welterweight": "WW", "Middleweight": "MW", "Light Heavyweight": "LHW", "Heavyweight": "HW",
    "Women's Strawweight": "W-SW", "Women's Flyweight": "W-FLW", "Women's Bantamweight": "W-BW",
    "Women's Featherweight": "W-FW", "Catch Weight": "CW", "Open Weight": "OW",
}

# Smallest gap between the final win chance and the chance a price implies
# (bookmaker margin included) that counts as a value side.
VALUE_EDGE = 0.02

# First year scored in backtests, and the first year whose fights train models.
# Ratings and profiles are built from every fight since 1994.
FIRST_TRAIN_YEAR = 2005


@dataclass
class Hyperparams:
    """Structural settings chosen by walk-forward tuning (see `tune`).

    Everything fitted by regression (win-model coefficients, calibration, the
    market weight, method and round models) is re-estimated on every run, so
    only these knobs are fixed.
    """

    # Glicko-2: rating deviation for a UFC debutant, volatility and its
    # constraint, and the days that make one rating period (deviation grows
    # with each period of inactivity).
    glicko_debut_rd: float = 320.0
    glicko_vol: float = 0.06
    glicko_tau: float = 0.5
    glicko_period_days: float = 60.0
    # Score credited to the winner: decisions and split decisions count as
    # narrower wins than finishes.
    score_decision: float = 0.8
    score_split: float = 0.6
    # Style profiles: minutes (or attempts) of evidence before a fighter's own
    # rates outweigh the division average, and the half-life in years of older
    # fights.
    prior_minutes: float = 8.0
    prior_attempts: float = 40.0
    prior_fights: float = 3.0
    profile_half_life_years: float = 3.0
    # Win model ridge strength and the years of fights it is fitted on.
    ridge: float = 100.0
    fit_window_years: int = 10

    @classmethod
    def load(cls, path: Path = PARAMS_PATH) -> "Hyperparams":
        if not path.exists():
            return cls()
        raw = json.loads(path.read_text())
        known = {f.name for f in fields(cls)}
        return cls(**{k: v for k, v in raw.items() if k in known})

    def save(self, path: Path = PARAMS_PATH) -> None:
        path.write_text(json.dumps(asdict(self), indent=2) + "\n")
