"""Kickoff wind for outdoor games.

Wind is the weather factor that moves totals, and in college football the
closing total under-prices it (each mph above 10 has meant about 0.2 points
fewer than the line expected). The model learns its effect from measured
wind (``model.py``), and upcoming games get a forecast:

- Finished games up to 2025 carry the nearest weather station's measured
  wind (Meteostat's hourly archive), committed in ``data/weather.csv``.
- Later finished games are filled in from Open-Meteo's historical archive at
  the venue, once its data has caught up (about five days).
- Upcoming games get Open-Meteo's forecast for kickoff.

Each is the mean wind (mph) from the kickoff hour through the next two. Domes
and venues without coordinates (some neutral sites) get no wind, so no
adjustment. Any failure leaves a game without wind.
"""

from __future__ import annotations

import datetime as dt
import logging

import numpy as np
import pandas as pd
import requests

from .config import DATA_DIR

log = logging.getLogger(__name__)

FORECAST_URL = "https://api.open-meteo.com/v1/forecast"
ARCHIVE_URL = "https://archive-api.open-meteo.com/v1/archive"
WEATHER_PATH = DATA_DIR / "weather.csv"
WEATHER_COLUMNS = ["game_id", "wind", "wind_source"]
HORIZON_DAYS = 10
ARCHIVE_LAG_DAYS = 6
KICKOFF_HOURS = 3


def venue_points(games: pd.DataFrame, venues: pd.DataFrame) -> pd.DataFrame:
    """Latitude, longitude and dome flag of each game's venue (NaN where unknown)."""
    by_id = venues.dropna(subset=["venue_id"]).drop_duplicates("venue_id").set_index("venue_id")
    vid = pd.to_numeric(games["venue_id"], errors="coerce")
    out = pd.DataFrame({c: vid.map(by_id[c]) for c in ("latitude", "longitude", "dome")}, index=games.index)
    out["dome"] = out["dome"].astype("boolean")
    return out


def parse_wind(payload: dict, kickoff: pd.Timestamp, hours: int = KICKOFF_HOURS) -> float | None:
    """Mean wind (mph) from the kickoff hour over the next ``hours`` hours of an Open-Meteo answer."""
    hourly = payload.get("hourly") or {}
    times, speeds = hourly.get("time"), hourly.get("wind_speed_10m")
    if not times or not speeds:
        return None
    stamps = pd.to_datetime(pd.Series(times)).dt.tz_localize("UTC")
    start = kickoff.tz_convert("UTC").floor("h")
    window = (stamps >= start) & (stamps < start + pd.Timedelta(hours=hours))
    values = pd.Series(speeds, dtype=float)[window.to_numpy()].dropna()
    return float(values.mean()) if len(values) else None


def kickoff_wind(games: pd.DataFrame, venues: pd.DataFrame, url: str = FORECAST_URL,
                 session: requests.Session | None = None) -> pd.Series:
    """Open-Meteo wind at kickoff for each outdoor game (NaN where unknown or indoors)."""
    session = session or requests.Session()
    points = venue_points(games, venues)
    wind = pd.Series(np.nan, index=games.index, dtype=float)
    for idx, g in games.iterrows():
        p = points.loc[idx]
        if pd.isna(p["latitude"]) or bool(p["dome"]) or pd.isna(g["kickoff"]):
            continue
        kickoff = pd.Timestamp(g["kickoff"])
        day = kickoff.tz_convert("UTC").date()
        params = {"latitude": p["latitude"], "longitude": p["longitude"], "hourly": "wind_speed_10m",
                  "wind_speed_unit": "mph", "timezone": "UTC", "start_date": day.isoformat(),
                  "end_date": (day + dt.timedelta(days=1)).isoformat()}
        try:
            resp = session.get(url, params=params, timeout=20)
            resp.raise_for_status()
            value = parse_wind(resp.json(), kickoff)
        except requests.ConnectionError as exc:
            log.warning("Weather service unreachable, skipping wind: %s", exc)
            break
        except (requests.RequestException, ValueError) as exc:
            log.warning("No wind for %s: %s", g["game_id"], exc)
            continue
        if value is not None:
            wind[idx] = value
    return wind


def forecast_wind(games: pd.DataFrame, venues: pd.DataFrame, now: dt.datetime | None = None) -> pd.Series:
    """Forecast kickoff wind for upcoming games within the forecast horizon."""
    now = pd.Timestamp(now or dt.datetime.now(dt.timezone.utc))
    soon = games["kickoff"].between(now, now + pd.Timedelta(days=HORIZON_DAYS))
    wind = pd.Series(np.nan, index=games.index, dtype=float)
    if soon.any():
        wind[soon] = kickoff_wind(games[soon], venues, FORECAST_URL)
    return wind


def load_weather() -> pd.DataFrame:
    if not WEATHER_PATH.exists():
        return pd.DataFrame(columns=WEATHER_COLUMNS)
    return pd.read_csv(WEATHER_PATH).reindex(columns=WEATHER_COLUMNS)


def update_weather(games: pd.DataFrame, venues: pd.DataFrame, now: dt.datetime | None = None,
                   limit: int = 400) -> pd.DataFrame:
    """Fill in measured wind (Open-Meteo's archive) for finished outdoor games that lack it, at most
    ``limit`` a run, and save ``data/weather.csv``. Returns the whole file."""
    now = pd.Timestamp(now or dt.datetime.now(dt.timezone.utc))
    known = load_weather()
    points = venue_points(games, venues)
    recent = games["season"] >= games["season"].max() - 1        # older gaps are not retried every run
    todo = games[recent & games["completed"] & ~games["game_id"].isin(known["game_id"]) & points["latitude"].notna()
                 & ~points["dome"].fillna(True).astype(bool)
                 & (games["kickoff"] < now - pd.Timedelta(days=ARCHIVE_LAG_DAYS))].head(limit)
    if todo.empty:
        return known
    wind = kickoff_wind(todo, venues, ARCHIVE_URL)
    got = wind.notna()
    if got.any():
        new = pd.DataFrame({"game_id": todo.loc[got, "game_id"].to_numpy(), "wind": wind[got].round(1).to_numpy(),
                            "wind_source": "open-meteo archive"})
        known = pd.concat([known, new], ignore_index=True) if len(known) else new
        known.sort_values("game_id").to_csv(WEATHER_PATH, index=False)
        log.info("Measured wind for %d games", int(got.sum()))
    return known
