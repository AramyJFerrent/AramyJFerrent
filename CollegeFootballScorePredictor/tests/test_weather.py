import numpy as np
import pandas as pd
import pytest

from cfbpredictor import weather
from cfbpredictor.model import wind_excess
from cfbpredictor.weather import kickoff_wind, parse_wind, update_weather, venue_points

VENUES = pd.DataFrame({"team": ["Iowa", "Syracuse"], "venue_id": [3842, 3765], "latitude": [41.66, 43.04],
                       "longitude": [-91.55, -76.14], "timezone": "America/New_York", "dome": [False, True],
                       "elevation": [200.0, 120.0]})


class Session:
    """Answers every request with the same hourly wind, and counts them."""

    def __init__(self, speeds):
        self.speeds, self.calls = speeds, 0

    def get(self, url, params=None, timeout=None):
        self.calls += 1
        times = [f"{params['start_date']}T{h:02d}:00" for h in range(len(self.speeds))]
        speeds = self.speeds
        return type("R", (), {"raise_for_status": lambda self: None,
                              "json": lambda self: {"hourly": {"time": times, "wind_speed_10m": speeds}}})()


def test_parse_wind_averages_the_kickoff_hour_and_the_next_two():
    payload = {"hourly": {"time": ["2025-10-04T16:00", "2025-10-04T17:00", "2025-10-04T18:00", "2025-10-04T19:00",
                                   "2025-10-04T20:00"], "wind_speed_10m": [5.0, 12.0, 14.0, 16.0, 30.0]}}
    assert parse_wind(payload, pd.Timestamp("2025-10-04 17:30", tz="UTC")) == 14.0
    assert parse_wind({}, pd.Timestamp("2025-10-04", tz="UTC")) is None


def test_only_outdoor_venues_with_coordinates_get_wind():
    games = pd.DataFrame({"game_id": [1, 2, 3], "venue_id": [3842, 3765, 9999],
                          "kickoff": pd.to_datetime(["2025-10-04 17:00"] * 3, utc=True)})
    pts = venue_points(games, VENUES)
    assert pts["latitude"].notna().tolist() == [True, True, False] and pts["dome"].tolist()[:2] == [False, True]
    session = Session([10.0] * 17 + [20.0, 22.0, 24.0] + [0.0] * 4)
    wind = kickoff_wind(games, VENUES, session=session)
    assert wind[0] == 22.0 and np.isnan(wind[1]) and np.isnan(wind[2]) and session.calls == 1


def test_measured_wind_is_filled_once_for_recent_finished_outdoor_games(tmp_path, monkeypatch):
    monkeypatch.setattr(weather, "WEATHER_PATH", tmp_path / "weather.csv")
    monkeypatch.setattr(weather, "kickoff_wind", lambda g, v, url: pd.Series(18.0, index=g.index))
    games = pd.DataFrame({"game_id": [1, 2, 3, 4], "season": [2025, 2025, 2025, 2022], "venue_id": [3842] * 4,
                          "completed": [True, True, False, True],
                          "kickoff": pd.to_datetime(["2025-10-04", "2025-10-30", "2025-11-08", "2022-10-01"], utc=True)})
    out = update_weather(games, VENUES, now=pd.Timestamp("2025-11-01", tz="UTC"))
    # Game 2 is too recent for the archive, game 3 not played, game 4 too old to retry.
    assert out["game_id"].tolist() == [1] and out["wind"].tolist() == [18.0]
    assert pd.read_csv(tmp_path / "weather.csv")["wind_source"].tolist() == ["open-meteo archive"]


def test_wind_only_counts_above_the_threshold():
    f = pd.DataFrame({"wind": [5.0, 14.0, np.nan]})
    assert wind_excess(f).tolist() == [0.0, 4.0, 0.0]
    assert wind_excess(f, pd.Series([25.0, 0.0, 12.0])).tolist() == pytest.approx([15.0, 0.0, 2.0])
    assert wind_excess(pd.DataFrame({"x": [1]})).tolist() == [0.0]
