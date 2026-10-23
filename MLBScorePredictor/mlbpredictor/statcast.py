"""Statcast quality of contact: expected hits on every ball in play.

Hits on balls in play are the slowest outcomes to stabilize (``players.py``):
whether a line drive finds a glove is mostly luck, so a hitter's or a
pitcher's singles, doubles and triples take thousands of plate appearances to
mean much. Statcast measures every ball in play since 2015, and how hard and
at what angle a ball was hit says more, sooner. For each ball in play the
chance it became a single, double, triple or home run is read from a table of
outcomes by exit velocity, launch angle and spray direction (pulled, center,
opposite field), fitted once on 2015 and frozen, so no later season is scored
by a table that saw it.

The baseball itself changes between seasons (the livelier ball of 2017 and
2019), which a frozen table cannot know. So each day's expected counts are
scaled, outcome by outcome, so that the league's expected hits over the
previous ``CALIBRATION_DAYS`` game days match its actual ones: what is left is
each player's contact quality relative to the league at the time.

Each season is kept as expected hits by player and day for batters and
pitchers, and the league's expected and actual hits by day for the
calibration (``data/statcast/``). The calibrated expected hits stand in,
partly, for the actual hits in the ratings (``players.py``, weighted by
``Hyperparams.statcast_weight``).
"""

from __future__ import annotations

import io
import logging
import time
from datetime import date, timedelta
from pathlib import Path

import numpy as np
import pandas as pd
import requests

from .config import DATA_DIR

log = logging.getLogger(__name__)

STATCAST_DIR = DATA_DIR / "statcast"
MODEL_PATH = DATA_DIR / "statcast_model.csv"

SAVANT_URL = (
    "https://baseballsavant.mlb.com/statcast_search/csv?all=true&hfPT=&hfAB=&hfBBT=fly%5C.%5C.ball%7Cline%5C.%5C."
    "drive%7Cground%5C.%5C.ball%7Cpopup%7C&hfPR=&hfZ=&stadium=&hfBBL=&hfNewZones=&hfGT=R%7CPO%7C&hfSea=&hfSit="
    "&player_type=pitcher&hfOuts=&opponent=&pitcher_throws=&batter_stands=&hfSA=&game_date_gt={start}"
    "&game_date_lt={end}&team=&position=&hfRO=&home_road=&hfFlag=&metric_1=&hfInn=&min_pitches=0&min_results=0"
    "&group_by=name&sort_col=pitches&player_event_sort=h_launch_speed&sort_order=desc&min_abs=0&type=details")
BIP_COLUMNS = ["game_date", "game_pk", "batter", "pitcher", "stand", "events", "launch_speed", "launch_angle",
               "hc_x", "hc_y"]
FIRST_STATCAST_SEASON = 2015
HITS = ["s", "d", "t", "hr"]
EVENT_HITS = {"single": "s", "double": "d", "triple": "t", "home_run": "hr"}
EV_EDGES = np.arange(40.0, 122.0, 3.0)
LA_EDGES = np.arange(-90.0, 92.0, 4.0)
SPRAY_EDGES = np.array([-15.0, 15.0])
# Smoothing toward the cell's exit-velocity-and-angle outcome mix, in balls in play.
SMOOTH = 20.0
CALIBRATION_DAYS = 30
X_COLUMNS = [f"x_{h}" for h in HITS]
Y_COLUMNS = [f"y_{h}" for h in HITS]
SUMMARY_COLUMNS = ["player_id", "date", "bip", *X_COLUMNS]
LEAGUE_COLUMNS = ["date", "bip", *X_COLUMNS, *Y_COLUMNS]


def spray_angle(bip: pd.DataFrame) -> np.ndarray:
    """Degrees from center field toward the batter's pull side (negative) or opposite field (positive)."""
    angle = np.degrees(np.arctan2(bip["hc_x"].to_numpy(float) - 125.42, 198.27 - bip["hc_y"].to_numpy(float)))
    return np.where(bip["stand"].eq("L").to_numpy(), -angle, angle)


def _cells(bip: pd.DataFrame) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    ev = np.digitize(bip["launch_speed"].to_numpy(float), EV_EDGES)
    la = np.digitize(bip["launch_angle"].to_numpy(float), LA_EDGES)
    spray = np.digitize(np.nan_to_num(spray_angle(bip), nan=0.0), SPRAY_EDGES)
    ok = bip["launch_speed"].notna().to_numpy() & bip["launch_angle"].notna().to_numpy()
    return ev, la, spray, ok


def outcomes(bip: pd.DataFrame) -> np.ndarray:
    """(n, 4) indicators of single, double, triple and home run."""
    hit = bip["events"].map(EVENT_HITS)
    return np.column_stack([(hit == h).to_numpy(float) for h in HITS])


class ExpectedHits:
    """Chances of each hit type by exit velocity, launch angle and spray direction."""

    def __init__(self, table: np.ndarray, base: np.ndarray):
        self.table, self.base = table, base         # (ev, la, spray, 4) and the league mix (4,)

    @classmethod
    def fit(cls, bip: pd.DataFrame) -> "ExpectedHits":
        ev, la, spray, ok = _cells(bip)
        y = outcomes(bip)
        shape = (len(EV_EDGES) + 1, len(LA_EDGES) + 1, len(SPRAY_EDGES) + 1)
        n = np.zeros(shape)
        hits = np.zeros(shape + (len(HITS),))
        np.add.at(n, (ev[ok], la[ok], spray[ok]), 1.0)
        np.add.at(hits, (ev[ok], la[ok], spray[ok]), y[ok])
        base = y[ok].mean(axis=0)
        # Each cell is pulled toward its exit-velocity-and-angle cell over all directions, and that toward the league.
        n2, hits2 = n.sum(axis=2), hits.sum(axis=2)
        coarse = (hits2 + SMOOTH * base) / (n2 + SMOOTH)[..., None]
        table = (hits + SMOOTH * coarse[:, :, None, :]) / (n + SMOOTH)[..., None]
        return cls(table, base)

    def predict(self, bip: pd.DataFrame) -> np.ndarray:
        """(n, 4) chances of each hit type; the league mix where exit velocity or angle is missing."""
        ev, la, spray, ok = _cells(bip)
        out = np.tile(self.base, (len(bip), 1))
        out[ok] = self.table[ev[ok], la[ok], spray[ok]]
        return out

    def to_frame(self) -> pd.DataFrame:
        idx = np.indices(self.table.shape[:3]).reshape(3, -1).T
        df = pd.DataFrame(idx, columns=["ev_bin", "la_bin", "spray_bin"])
        for i, h in enumerate(HITS):
            df[f"p_{h}"] = self.table.reshape(-1, len(HITS))[:, i].round(5)
        return pd.concat([df, pd.DataFrame([{"ev_bin": -1, "la_bin": -1, "spray_bin": -1,
                                             **{f"p_{h}": round(float(b), 5) for h, b in zip(HITS, self.base)}}])],
                         ignore_index=True)

    @classmethod
    def from_frame(cls, df: pd.DataFrame) -> "ExpectedHits":
        base_row = df[df["ev_bin"] < 0].iloc[0]
        cells = df[df["ev_bin"] >= 0]
        shape = (len(EV_EDGES) + 1, len(LA_EDGES) + 1, len(SPRAY_EDGES) + 1)
        table = np.zeros(shape + (len(HITS),))
        for i, h in enumerate(HITS):
            table[cells["ev_bin"], cells["la_bin"], cells["spray_bin"], i] = cells[f"p_{h}"].to_numpy()
        return cls(table, base_row[[f"p_{h}" for h in HITS]].to_numpy(float))


def league_daily(bip: pd.DataFrame, x: np.ndarray) -> pd.DataFrame:
    """The league's balls in play, expected hits (``x``, uncalibrated) and actual hits by day."""
    y = outcomes(bip)
    d = pd.DataFrame({"date": pd.to_datetime(bip["game_date"]).dt.strftime("%Y-%m-%d").to_numpy(), "bip": 1.0,
                      **{c: x[:, i] for i, c in enumerate(X_COLUMNS)}, **{c: y[:, i] for i, c in enumerate(Y_COLUMNS)}})
    out = d.groupby("date", as_index=False).sum()
    out[X_COLUMNS] = out[X_COLUMNS].round(3)
    out[["bip", *Y_COLUMNS]] = out[["bip", *Y_COLUMNS]].astype(int)
    return out[LEAGUE_COLUMNS]


def calibration(league: pd.DataFrame) -> pd.DataFrame:
    """For each game day, the ratio of actual to expected hits of each type over the previous
    ``CALIBRATION_DAYS`` game days (indexed by date, columns as ``HITS``)."""
    d = league.groupby("date")[[*X_COLUMNS, *Y_COLUMNS]].sum().sort_index()
    trailing = d.rolling(CALIBRATION_DAYS, min_periods=1).sum().shift(1)
    ratio = (trailing[Y_COLUMNS].to_numpy() + 1.0) / (trailing[X_COLUMNS].to_numpy() + 1.0)
    return pd.DataFrame(np.nan_to_num(ratio, nan=1.0), index=d.index, columns=HITS)


def calibrated(players: pd.DataFrame, ratios: pd.DataFrame) -> pd.DataFrame:
    """``players`` (``SUMMARY_COLUMNS``) with its expected hits scaled by each day's calibration."""
    r = ratios.reindex(players["date"]).fillna(1.0).to_numpy()
    return players.assign(**{c: players[c].to_numpy() * r[:, i] for i, c in enumerate(X_COLUMNS)})


def summarize(bip: pd.DataFrame, x: np.ndarray, role: str) -> pd.DataFrame:
    """Balls in play and expected hits by player (``batter`` or ``pitcher``) and day."""
    d = pd.DataFrame({"player_id": bip[role].astype("Int64").astype(str).to_numpy(),
                      "date": pd.to_datetime(bip["game_date"]).dt.strftime("%Y-%m-%d").to_numpy(), "bip": 1.0,
                      **{c: x[:, i] for i, c in enumerate(X_COLUMNS)}})
    out = d.groupby(["player_id", "date"], as_index=False).sum()
    out[X_COLUMNS] = out[X_COLUMNS].round(4)
    out["bip"] = out["bip"].astype(int)
    return out[SUMMARY_COLUMNS]


def fetch_bip(start: date, end: date, session: requests.Session | None = None, depth: int = 0) -> pd.DataFrame:
    """Statcast's balls in play (regular season and postseason) from ``start`` to ``end``, a week at a
    time; a range Savant refuses as too large is split in two."""
    session = session or requests.Session()
    parts, a = [], start
    while a <= end:
        b = min(a + timedelta(days=6), end)
        parts.append(_fetch_window(a, b, session, depth))
        a = b + timedelta(days=1)
    return pd.concat(parts, ignore_index=True) if parts else pd.DataFrame(columns=BIP_COLUMNS)


def _fetch_window(a: date, b: date, session: requests.Session, depth: int) -> pd.DataFrame:
    for attempt in range(4):
        try:
            r = session.get(SAVANT_URL.format(start=a, end=b), timeout=180)
            text = r.content.decode("utf-8-sig")
            if r.status_code == 200 and not text.startswith('"error"'):
                d = pd.read_csv(io.StringIO(text), low_memory=False) if text.strip() else pd.DataFrame()
                return d.reindex(columns=BIP_COLUMNS)
            if text.startswith('"error"') and a < b and depth < 4:
                mid = a + (b - a) // 2
                return pd.concat([_fetch_window(a, mid, session, depth + 1),
                                  _fetch_window(mid + timedelta(days=1), b, session, depth + 1)], ignore_index=True)
        except requests.RequestException as exc:
            log.warning("Savant request %s to %s failed: %s", a, b, exc)
        time.sleep(5 * (attempt + 1))
    raise RuntimeError(f"Baseball Savant gave no data for {a} to {b}")


# ---- storage ------------------------------------------------------------------

def season_paths(season: int) -> dict[str, Path]:
    """The season's batter, pitcher and league files: gzipped once the season is over, plain while it
    is updated."""
    out = {}
    for kind in ("batting", "pitching", "league"):
        plain = STATCAST_DIR / f"{season}_{kind}.csv"
        packed = plain.with_suffix(".csv.gz")
        out[kind] = packed if packed.exists() else plain
    return out


def load_model() -> ExpectedHits | None:
    return ExpectedHits.from_frame(pd.read_csv(MODEL_PATH)) if MODEL_PATH.exists() else None


def write_season(season: int, bip: pd.DataFrame, model: ExpectedHits, compress: bool = False) -> None:
    """Summarize a season's balls in play into its three files."""
    STATCAST_DIR.mkdir(parents=True, exist_ok=True)
    x = model.predict(bip)
    frames = {"batting": summarize(bip, x, "batter"), "pitching": summarize(bip, x, "pitcher"),
              "league": league_daily(bip, x)}
    for kind, df in frames.items():
        plain = STATCAST_DIR / f"{season}_{kind}.csv"
        path = plain.with_suffix(".csv.gz") if compress else plain
        df.to_csv(path, index=False)
        (plain if compress else plain.with_suffix(".csv.gz")).unlink(missing_ok=True)


def update_season(season: int, today: date | None = None) -> None:
    """Add the days since the season's files were last written (re-reading the last one, which may
    have been partial). Nothing happens before 2015 or without the frozen table."""
    model = load_model()
    if model is None or season < FIRST_STATCAST_SEASON:
        return
    today = today or date.today()
    paths = season_paths(season)
    old = {k: pd.read_csv(p, dtype={"player_id": str}) if p.exists() else pd.DataFrame() for k, p in paths.items()}
    start = date(season, 3, 15)
    if len(old["league"]):
        start = max(start, date.fromisoformat(str(old["league"]["date"].max())))
    end = min(today - timedelta(days=1), date(season, 11, 15))
    if end < start:
        return
    bip = fetch_bip(start, end)
    x = model.predict(bip)
    new = {"batting": summarize(bip, x, "batter"), "pitching": summarize(bip, x, "pitcher"),
           "league": league_daily(bip, x)}
    STATCAST_DIR.mkdir(parents=True, exist_ok=True)
    for kind, df in new.items():
        prev = old[kind]
        if len(prev):
            prev = prev[prev["date"] < start.isoformat()]
            df = pd.concat([prev, df], ignore_index=True)
        df.to_csv(STATCAST_DIR / f"{season}_{kind}.csv", index=False)
    log.info("Statcast %s: %d balls in play from %s to %s", season, len(bip), start, end)


def load(first: int, last: int) -> dict[str, pd.DataFrame]:
    """Calibrated expected hits by player and day for batters (``statcast_batting``) and pitchers
    (``statcast_pitching``), every season from ``first`` to ``last`` that has them."""
    frames = {"batting": [], "pitching": [], "league": []}
    for season in range(max(first, FIRST_STATCAST_SEASON), last + 1):
        for kind, path in season_paths(season).items():
            if path.exists():
                frames[kind].append(pd.read_csv(path, dtype={"player_id": str}))
    if not frames["league"]:
        empty = pd.DataFrame(columns=SUMMARY_COLUMNS)
        return {"statcast_batting": empty, "statcast_pitching": empty.copy()}
    ratios = calibration(pd.concat(frames["league"], ignore_index=True))
    return {f"statcast_{kind}": calibrated(pd.concat(frames[kind], ignore_index=True), ratios)
            for kind in ("batting", "pitching")}
