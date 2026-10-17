"""Paths, data sources and model hyperparameters."""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass, fields
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
EPA_DIR = DATA_DIR / "epa"
CACHE_DIR = ROOT / ".cache"
OUTPUT_DIR = ROOT / "predictions"
PARAMS_PATH = ROOT / "params.json"

GAMES_URL = "https://raw.githubusercontent.com/nflverse/nfldata/master/data/games.csv"
PBP_URL = (
    "https://github.com/nflverse/nflverse-data/releases/download/pbp/"
    "play_by_play_{season}.parquet"
)

# First season summarized from play-by-play. Ratings need a few seasons of
# burn-in before the backtest window so preseason priors are meaningful.
FIRST_SEASON = 2009

# Relocated franchises keep one code across seasons so priors carry over.
TEAM_ALIASES = {"OAK": "LV", "SD": "LAC", "STL": "LA"}

# Kickoff times in the nflverse schedule are US Eastern.
KICKOFF_TZ = "America/New_York"


@dataclass
class Hyperparams:
    """Ratings-engine settings chosen by walk-forward tuning (see `tune`).

    Everything fitted by regression (the ratings-to-points map, home field,
    rest, QB weight, market blend, wind, score dispersion) is re-estimated on
    every run from recent seasons, so only these structural knobs are fixed.
    """

    # Ridge strength, in plays, pulling each team toward its preseason prior.
    # Defense is pulled harder because it is less stable than offense.
    off_prior_plays: float = 600.0
    def_prior_plays: float = 1200.0
    # Share of last season's final rating kept as this season's prior.
    off_carryover: float = 0.6
    def_carryover: float = 0.45
    # Half-life, in weeks, of the recency weight on current-season games.
    half_life_weeks: float = 30.0
    # QB value: dropbacks of evidence before a QB's own record outweighs the
    # prior, the prior for an unproven QB (EPA per dropback vs league), and the
    # half-life in weeks for older dropbacks.
    qb_prior_dropbacks: float = 800.0
    qb_prior_value: float = -0.15
    qb_half_life_weeks: float = 80.0
    # Seasons of history used to fit the points map, blend and dispersion.
    fit_window_seasons: int = 6

    @classmethod
    def load(cls, path: Path = PARAMS_PATH) -> "Hyperparams":
        if not path.exists():
            return cls()
        raw = json.loads(path.read_text())
        known = {f.name for f in fields(cls)}
        return cls(**{k: v for k, v in raw.items() if k in known})

    def save(self, path: Path = PARAMS_PATH) -> None:
        path.write_text(json.dumps(asdict(self), indent=2) + "\n")
