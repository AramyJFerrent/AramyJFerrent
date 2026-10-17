import pandas as pd

from nflpredictor.weather import forecast_wind, parse_wind


def test_parse_wind_averages_kickoff_window():
    payload = {"hourly": {
        "time": ["2026-10-18T16:00", "2026-10-18T17:00", "2026-10-18T18:00", "2026-10-18T19:00",
                 "2026-10-18T20:00"],
        "wind_speed_10m": [5.0, 12.0, 14.0, 16.0, 30.0],
    }}
    kickoff = pd.Timestamp("2026-10-18 13:00", tz="America/New_York")   # 17:00 UTC
    assert parse_wind(payload, kickoff) == 14.0


def test_parse_wind_handles_empty_payload():
    assert parse_wind({}, pd.Timestamp("2026-10-18", tz="UTC")) is None


class FakeSession:
    def __init__(self):
        self.calls = []

    def get(self, url, params, timeout):
        self.calls.append(params)

        class Resp:
            def raise_for_status(self):
                pass

            def json(self):
                return {"hourly": {"time": ["2026-10-18T17:00"], "wind_speed_10m": [20.0]}}
        return Resp()


def test_forecast_only_for_open_air_games_in_horizon():
    kickoff = pd.Timestamp("2026-10-18 13:00", tz="America/New_York").tz_convert("UTC")
    games = pd.DataFrame([
        {"game_id": "a", "roof": "outdoors", "stadium_id": "GNB00", "kickoff": kickoff},
        {"game_id": "b", "roof": "dome", "stadium_id": "DET00", "kickoff": kickoff},
        {"game_id": "c", "roof": "outdoors", "stadium_id": "GNB00",
         "kickoff": kickoff + pd.Timedelta(days=30)},
    ])
    session = FakeSession()
    wind = forecast_wind(games, now=pd.Timestamp("2026-10-17", tz="UTC"), session=session)
    assert wind.iloc[0] == 20.0
    assert wind.iloc[1:].isna().all()
    assert len(session.calls) == 1
