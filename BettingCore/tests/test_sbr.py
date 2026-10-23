import numpy as np
import pandas as pd

from bettingcore import sbr


def rows():
    base = {"season": 2016, "home_open_ml": -140, "away_open_ml": 120, "home_close_ml": -150, "away_close_ml": 130,
            "home_close_spread": -1.5, "away_close_spread": 1.5, "home_close_spread_odds": 160,
            "away_close_spread_odds": -180, "open_over_under": 5.5, "open_over_under_odds": -115,
            "close_over_under": 6.0, "close_over_under_odds": -105}
    return [
        {**base, "date": 20161012.0, "home_team": "Bruins", "away_team": "Flyers", "home_final": "3", "away_final": "1"},
        # A doubleheader-style repeat: same teams and day, another score.
        {**base, "date": 20161012.0, "home_team": "Bruins", "away_team": "Flyers", "home_final": "2", "away_final": "4"},
        # Missing values stored as zeros.
        {**base, "date": 20161013.0, "home_team": "Kings", "away_team": "Sharks", "home_final": "1", "away_final": "0",
         "home_close_spread": 0.0, "away_close_spread": 0.0, "home_close_spread_odds": 0.0,
         "away_close_spread_odds": 0.0, "home_open_ml": 0},
    ]


def test_parse_turns_zeros_into_missing_and_drops_total_prices():
    a = sbr.parse(rows())
    assert list(a.columns) == sbr.COLUMNS
    assert a.loc[0, "home_close_ml"] == -150 and a.loc[0, "home_close_spread"] == -1.5
    assert a.loc[0, "open_total"] == 5.5 and "open_over_under_odds" not in a
    assert np.isnan(a.loc[2, "home_close_spread"]) and np.isnan(a.loc[2, "home_close_spread_odds"])
    assert np.isnan(a.loc[2, "home_open_ml"]) and a.loc[2, "date"] == pd.Timestamp("2016-10-13")


def test_match_on_teams_score_and_nearby_date():
    a = sbr.parse(rows())
    names = {"Bruins": "BOS", "Flyers": "PHI", "Kings": "LAK"}             # Sharks unknown: unmatched
    games = pd.DataFrame({
        "game_id": ["g1", "g2", "g3", "g4"],
        "date": pd.to_datetime(["2016-10-12 23:00", "2016-10-13 02:00", "2016-10-13 00:00", "2016-10-20 00:00"], utc=True),
        "home_team": ["BOS", "BOS", "LAK", "BOS"], "away_team": ["PHI", "PHI", "SJS", "PHI"],
        "home_score": [3, 2, 1, 3], "away_score": [1, 4, 0, 1]})
    m = sbr.match(a, games, names)
    assert set(m.index) == {"g1", "g2"}                    # g2's UTC date is a day later; g4 is a week off
    assert m.loc["g1", "home_close_ml"] == -150 and m.loc["g2", "close_total"] == 6.0


def test_realign_rebuilds_games_from_shifted_rows():
    # Each shifted row: one game's visitors (home_* fields, with that game's date and total) and the previous
    # game's home team (away_* fields). Games: STL 1 @ PIT 4, then TOR 5 @ TB 3.
    shifted = [
        {"season": 2016, "date": 20160403, "home_team": "Cardinals", "home_final": 1, "home_close_ml": 109,
         "away_team": None, "away_final": None, "away_close_ml": None, "close_over_under": 6.5},
        {"season": 2016, "date": 20160403, "home_team": "Blue Jays", "home_final": 5, "home_close_ml": 111,
         "away_team": "Pirates", "away_final": 4, "away_close_ml": -119, "close_over_under": 7.0},
        {"season": 2016, "date": 20160403, "home_team": "Mets", "home_final": 3, "home_close_ml": 100,
         "away_team": "TAM", "away_final": 3, "away_close_ml": -121, "close_over_under": 7.5},
        # The next season starts over: its first row has no previous home team, and 2016's last game none of its own.
        {"season": 2017, "date": 20170402, "home_team": "Yankees", "home_final": 3, "home_close_ml": 120,
         "away_team": None, "away_final": None, "away_close_ml": None, "close_over_under": 8.0},
    ]
    a = sbr.parse(shifted, shifted=True)
    assert list(a["home"]) == ["Pirates", "TAM"] and list(a["away"]) == ["Cardinals", "Blue Jays"]
    assert list(a["home_final"]) == [4, 3] and list(a["away_final"]) == [1, 5]
    assert list(a["home_close_ml"]) == [-119, -121] and list(a["away_close_ml"]) == [109, 111]
    assert list(a["close_total"]) == [6.5, 7.0] and (a["date"] == pd.Timestamp("2016-04-03")).all()
