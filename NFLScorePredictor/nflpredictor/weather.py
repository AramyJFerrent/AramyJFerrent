"""Kickoff wind forecasts for outdoor games from Open-Meteo (free, no key).

Wind is the weather factor that moves totals, and the betting market under-
prices it. Forecasts are only fetched for open-air games within the forecast
horizon; any failure simply leaves the game without a wind adjustment.
"""

from __future__ import annotations

import datetime as dt
import logging

import numpy as np
import pandas as pd
import requests

log = logging.getLogger(__name__)

FORECAST_URL = "https://api.open-meteo.com/v1/forecast"
HORIZON_DAYS = 10

# nflverse stadium_id -> (latitude, longitude) for venues that can be open-air.
STADIUMS = {
    "BAL00": (39.2780, -76.6227), "BOS00": (42.0909, -71.2643), "BUF00": (42.7738, -78.7870),
    "CAR00": (35.2258, -80.8528), "CHI98": (41.8623, -87.6167),
    "CIN00": (39.0955, -84.5161), "CLE00": (41.5061, -81.6995), "DEN00": (39.7439, -105.0201),
    "GNB00": (44.5013, -88.0622), "JAX00": (30.3239, -81.6373), "KAN00": (39.0489, -94.4839),
    "MIA00": (25.9580, -80.2389), "NAS00": (36.1665, -86.7713), "NYC01": (40.8135, -74.0745),
    "PHI00": (39.9008, -75.1675), "PIT00": (40.4468, -80.0158), "SEA00": (47.5952, -122.3316),
    "SFO01": (37.4030, -121.9700), "TAM00": (27.9759, -82.5033), "WAS00": (38.9078, -76.8645),
    "LON00": (51.5560, -0.2796), "LON02": (51.6043, -0.0664), "GER00": (50.0686, 8.6455),
    "MUN01": (48.2188, 11.6247), "MEX00": (19.3029, -99.1505), "SAO00": (-23.5453, -46.4742),
    "RIO00": (-22.9122, -43.2302), "MAD01": (40.4531, -3.6883),
    # Retractable roofs, used only when the schedule lists the roof as open.
    "ATL97": (33.7554, -84.4008), "IND00": (39.7601, -86.1639), "HOU00": (29.6847, -95.4107),
    "PHO00": (33.5276, -112.2626), "DAL00": (32.7473, -97.0945),
}
OPEN_ROOFS = {"outdoors", "open"}


def parse_wind(payload: dict, kickoff: pd.Timestamp, hours: int = 3) -> float | None:
    """Mean forecast wind (mph) from kickoff over the next ``hours`` hours."""
    hourly = payload.get("hourly") or {}
    times, speeds = hourly.get("time"), hourly.get("wind_speed_10m")
    if not times or not speeds:
        return None
    stamps = pd.to_datetime(pd.Series(times)).dt.tz_localize("UTC")
    start = kickoff.tz_convert("UTC").floor("h")
    window = (stamps >= start) & (stamps < start + pd.Timedelta(hours=hours))
    values = pd.Series(speeds, dtype=float)[window.to_numpy()].dropna()
    return float(values.mean()) if len(values) else None


def forecast_wind(games: pd.DataFrame, now: dt.datetime | None = None,
                  session: requests.Session | None = None) -> pd.Series:
    """Forecast kickoff wind for each game (NaN where unknown or indoors)."""
    now = pd.Timestamp(now or dt.datetime.now(dt.timezone.utc))
    session = session or requests.Session()
    wind = pd.Series(np.nan, index=games.index, dtype=float)
    for idx, g in games.iterrows():
        if g["roof"] not in OPEN_ROOFS or g["stadium_id"] not in STADIUMS or pd.isna(g["kickoff"]):
            continue
        if not (now <= g["kickoff"] <= now + pd.Timedelta(days=HORIZON_DAYS)):
            continue
        lat, lon = STADIUMS[g["stadium_id"]]
        day = g["kickoff"].tz_convert("UTC").date()
        params = {
            "latitude": lat, "longitude": lon, "hourly": "wind_speed_10m",
            "wind_speed_unit": "mph", "timezone": "UTC",
            "start_date": day.isoformat(), "end_date": (day + dt.timedelta(days=1)).isoformat(),
        }
        try:
            resp = session.get(FORECAST_URL, params=params, timeout=20)
            resp.raise_for_status()
            value = parse_wind(resp.json(), g["kickoff"])
        except requests.ConnectionError as exc:
            log.warning("Weather service unreachable, skipping wind forecasts: %s", exc)
            break
        except (requests.RequestException, ValueError) as exc:
            log.warning("No wind forecast for %s: %s", g["game_id"], exc)
            continue
        if value is not None:
            wind[idx] = value
    return wind
