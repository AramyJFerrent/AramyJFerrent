"""First-pitch temperature forecasts for open-air games, from Open-Meteo (free, no key).

Warm air carries the ball farther, so temperature moves run expectations a
little at open-air parks. Forecasts are fetched for games within the forecast
horizon at parks that can be open; a retractable roof is assumed closed below
60°F or above 85°F. When the MLB Stats API already reports game-time weather
(close to first pitch), that is used instead. Any failure leaves the game at
a neutral temperature.
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
ROOF_OPEN_RANGE = (60.0, 85.0)

# Retrosheet park id -> (latitude, longitude, roof): "open", "retractable" or "dome".
PARKS = {
    "PHO01": (33.4455, -112.0667, "retractable"), "SAC01": (38.5803, -121.5133, "open"),
    "ATL03": (33.8908, -84.4678, "open"), "BAL12": (39.2838, -76.6217, "open"),
    "BOS07": (42.3467, -71.0972, "open"), "CHI11": (41.9484, -87.6553, "open"),
    "CIN09": (39.0975, -84.5066, "open"), "CLE08": (41.4962, -81.6852, "open"),
    "DEN02": (39.7559, -104.9942, "open"), "CHI12": (41.8299, -87.6338, "open"),
    "DET05": (42.3390, -83.0485, "open"), "HOU03": (29.7573, -95.3555, "retractable"),
    "KAN06": (39.0517, -94.4803, "open"), "ANA01": (33.8003, -117.8827, "open"),
    "LOS03": (34.0739, -118.2400, "open"), "MIA02": (25.7781, -80.2197, "retractable"),
    "MIL06": (43.0280, -87.9712, "retractable"), "MIN04": (44.9817, -93.2776, "open"),
    "NYC20": (40.7571, -73.8458, "open"), "NYC21": (40.8296, -73.9262, "open"),
    "PHI13": (39.9061, -75.1665, "open"), "PIT08": (40.4469, -80.0057, "open"),
    "SAN02": (32.7076, -117.1570, "open"), "SEA03": (47.5914, -122.3325, "retractable"),
    "SFO03": (37.7786, -122.3893, "open"), "STL10": (38.6226, -90.1928, "open"),
    "TAM02": (27.9803, -82.5067, "open"), "STP01": (27.7682, -82.6534, "dome"),
    "ARL03": (32.7473, -97.0847, "retractable"), "TOR02": (43.6414, -79.3894, "retractable"),
    "WAS11": (38.8730, -77.0074, "open"),
}


def parse_temperature(payload: dict, start: pd.Timestamp) -> float | None:
    """Forecast temperature (°F) at the hour of first pitch."""
    hourly = payload.get("hourly") or {}
    times, temps = hourly.get("time"), hourly.get("temperature_2m")
    if not times or not temps:
        return None
    stamps = pd.to_datetime(pd.Series(times)).dt.tz_localize("UTC")
    hour = start.tz_convert("UTC").floor("h")
    match = pd.Series(temps, dtype=float)[(stamps == hour).to_numpy()].dropna()
    return float(match.iloc[0]) if len(match) else None


def forecast(games: pd.DataFrame, now: dt.datetime | None = None,
             session: requests.Session | None = None) -> pd.DataFrame:
    """``temp`` and ``dome`` for each upcoming game (NaN temperature where unknown)."""
    now = pd.Timestamp(now or dt.datetime.now(dt.timezone.utc))
    session = session or requests.Session()
    out = pd.DataFrame({"temp": np.nan, "dome": 0.0}, index=games.index)
    for idx, g in games.iterrows():
        park = PARKS.get(g.get("park_id"))
        if park is None:
            continue
        lat, lon, roof = park
        if roof == "dome":
            out.at[idx, "dome"] = 1.0
            continue
        start = pd.Timestamp(g["start"]) if pd.notna(g.get("start")) else None
        if start is None or not (now - pd.Timedelta(hours=6) <= start <= now + pd.Timedelta(days=HORIZON_DAYS)):
            continue
        day = start.tz_convert("UTC").date()
        params = {"latitude": lat, "longitude": lon, "hourly": "temperature_2m", "temperature_unit": "fahrenheit",
                  "timezone": "UTC", "start_date": day.isoformat(), "end_date": (day + dt.timedelta(days=1)).isoformat()}
        try:
            resp = session.get(FORECAST_URL, params=params, timeout=20)
            resp.raise_for_status()
            temp = parse_temperature(resp.json(), start)
        except requests.ConnectionError as exc:
            log.warning("Weather service unreachable, skipping temperature forecasts: %s", exc)
            break
        except (requests.RequestException, ValueError) as exc:
            log.warning("No forecast for %s: %s", g.get("game_id"), exc)
            continue
        if temp is None:
            continue
        if roof == "retractable" and not (ROOF_OPEN_RANGE[0] <= temp <= ROOF_OPEN_RANGE[1]):
            out.at[idx, "dome"] = 1.0
        else:
            out.at[idx, "temp"] = temp
    return out
