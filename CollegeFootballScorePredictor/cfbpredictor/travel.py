"""Where teams play from and how far they travel.

Each FBS and FCS team's home stadium (location, time zone, dome) comes from
the cfbfastR team-info files and is committed as ``data/venues.csv``. A game's
venue is looked up by its venue id; neutral sites that are nobody's home
stadium have no coordinates, so their games get no travel features.
"""

from __future__ import annotations

import datetime as dt
from zoneinfo import ZoneInfo

import numpy as np
import pandas as pd

from .config import VENUES_PATH
from .data import load_team_info

VENUE_COLUMNS = ["team", "venue_id", "latitude", "longitude", "timezone", "dome", "elevation"]
EARTH_MILES = 3958.8


def build_venues(seasons) -> pd.DataFrame:
    frames = [load_team_info(s).assign(season=s) for s in seasons]
    t = pd.concat(frames, ignore_index=True)
    t = t[t["classification"].isin(["fbs", "fcs"])]
    tz = t.dropna(subset=["timezone"]).groupby("school")["timezone"].agg(lambda s: s.value_counts().index[0])
    latest = t.sort_values("season").dropna(subset=["latitude", "longitude"]).groupby("school").last()
    out = pd.DataFrame({
        "team": latest.index, "venue_id": latest["venue_id"].astype("Int64"),
        "latitude": latest["latitude"].astype(float).round(4), "longitude": latest["longitude"].astype(float).round(4),
        "timezone": latest.index.map(tz), "dome": latest["dome"].fillna(False).astype(bool),
        "elevation": pd.to_numeric(latest["elevation"], errors="coerce").round(0),
    })
    return out[VENUE_COLUMNS].reset_index(drop=True)


def load_venues() -> pd.DataFrame:
    if not VENUES_PATH.exists():
        return pd.DataFrame(columns=VENUE_COLUMNS)
    return pd.read_csv(VENUES_PATH)


def _miles(lat1, lon1, lat2, lon2) -> np.ndarray:
    lat1, lon1, lat2, lon2 = (np.radians(np.asarray(x, dtype=float)) for x in (lat1, lon1, lat2, lon2))
    a = np.sin((lat2 - lat1) / 2) ** 2 + np.cos(lat1) * np.cos(lat2) * np.sin((lon2 - lon1) / 2) ** 2
    return 2 * EARTH_MILES * np.arcsin(np.sqrt(a))


def _offset_hours(tz: str, when: pd.Timestamp) -> float:
    if not isinstance(tz, str) or pd.isna(when):
        return np.nan
    off = when.to_pydatetime().astimezone(ZoneInfo(tz)).utcoffset() or dt.timedelta(0)
    return off.total_seconds() / 3600.0


def travel_features(games: pd.DataFrame, venues: pd.DataFrame) -> pd.DataFrame:
    """Miles traveled and hours of time zone shifted (positive = eastward) per side.

    The home team of a non-neutral game travels nowhere. Missing locations give
    zero travel, so a game is never dropped for want of coordinates.
    """
    by_team = venues.set_index("team")
    by_venue = venues.dropna(subset=["venue_id"]).drop_duplicates("venue_id").set_index("venue_id")
    vid = pd.to_numeric(games["venue_id"], errors="coerce")
    v_lat = vid.map(by_venue["latitude"])
    v_lon = vid.map(by_venue["longitude"])
    v_tz = vid.map(by_venue["timezone"])
    # An unknown venue for a home game is the home team's own stadium.
    home_site = ~games["neutral"].astype(bool)
    v_lat = v_lat.where(v_lat.notna() | ~home_site, games["home_team"].map(by_team["latitude"]))
    v_lon = v_lon.where(v_lon.notna() | ~home_site, games["home_team"].map(by_team["longitude"]))
    v_tz = v_tz.where(v_tz.notna() | ~home_site, games["home_team"].map(by_team["timezone"]))
    out = pd.DataFrame(index=games.index)
    for side in ("home", "away"):
        team = games[f"{side}_team"]
        miles = _miles(team.map(by_team["latitude"]), team.map(by_team["longitude"]), v_lat, v_lon)
        venue_off = np.array([_offset_hours(z, k) for z, k in zip(v_tz, games["kickoff"])])
        team_off = np.array([_offset_hours(z, k) for z, k in zip(team.map(by_team["timezone"]), games["kickoff"])])
        out[f"{side}_miles"] = np.nan_to_num(miles)
        out[f"{side}_tz_shift"] = np.nan_to_num(venue_off - team_off)
    out.loc[home_site, ["home_miles", "home_tz_shift"]] = 0.0
    out["dome"] = vid.map(by_venue["dome"]).astype("boolean").fillna(False).astype(bool)
    return out
