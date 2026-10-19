import sqlite3

import numpy as np
import pandas as pd

from nbapredictor import lines as L


def test_unsigned_spreads_take_the_moneyline_favorite(tmp_path):
    path = tmp_path / "odds.sqlite"
    con = sqlite3.connect(path)
    pd.DataFrame({"Date": ["2019-11-01", "2019-11-02"], "Home": ["Boston Celtics", "Charlotte Bobcats"],
                  "Away": ["New Jersey Nets", "Los Angeles Lakers"], "OU": [210.5, 220.0], "Spread": [6.5, 4.0],
                  "ML_Home": [-250, 150], "ML_Away": [200, -170]}).to_sql("odds_2019-20_new", con, index=False)
    pd.DataFrame({"Date": ["2023-01-05"], "Home": ["Utah Jazz"], "Away": ["Seattle SuperSonics"], "OU": [230.0],
                  "Spread": [-3.0], "ML_Home": [130], "ML_Away": [-150]}).to_sql("2023-24", con, index=False)
    con.close()
    k = L._kyleskom(path).set_index("home_team")
    assert k.loc["BOS", "spread"] == 6.5 and k.loc["BOS", "away_team"] == "BKN"
    assert k.loc["CHA", "spread"] == -4.0                      # home underdog by the moneyline
    assert k.loc["UTA", "spread"] == -3.0 and k.loc["UTA", "away_team"] == "OKC"   # already signed


def test_lines_match_games_a_day_off():
    games = pd.DataFrame({"game_id": [1, 2], "date": pd.to_datetime(["2020-01-01", "2020-01-02"]).date,
                          "home_team": ["BOS", "LAL"], "away_team": ["NYK", "LAC"]})
    lines = pd.DataFrame({"date": ["2020-01-01", "2020-01-03"], "home_team": ["BOS", "LAL"],
                          "away_team": ["NYK", "LAC"], "spread": [5.0, -2.0], "total": [210.0, 220.0],
                          "home_moneyline": [-200, 110], "away_moneyline": [170, -130],
                          "open_spread": [4.5, np.nan], "open_total": [208.0, np.nan]})
    out = L.attach_lines(games, lines).set_index("game_id")
    assert out.loc[1, "spread"] == 5.0 and out.loc[1, "open_spread"] == 4.5
    assert out.loc[2, "spread"] == -2.0 and out.loc[2, "total"] == 220.0


def test_sportsbookreview_rows_with_swapped_spread_and_total_are_put_back(tmp_path):
    import json
    rows = [
        {"date": 20120105.0, "home_team": "Hawks", "away_team": "Heat", "home_open_spread": -3.0,
         "home_close_spread": -186.0, "open_over_under": 189.0, "close_over_under": 4.0,
         "home_close_ml": -185, "away_close_ml": 165},
        {"date": 20120106.0, "home_team": "Magic", "away_team": "Bulls", "home_open_spread": 2.0,
         "home_close_spread": 2.5, "open_over_under": 181.0, "close_over_under": 182.5,
         "home_close_ml": 120, "away_close_ml": -140},
    ]
    path = tmp_path / "sbr.json"
    path.write_text(json.dumps(rows))
    s = L._sbr(path).set_index("home_team")
    assert s.loc["ATL", "close_spread"] == 4.0 and s.loc["ATL", "close_total"] == 186.0   # home favored by 4
    assert s.loc["ORL", "close_spread"] == -2.5 and s.loc["ORL", "open_spread"] == -2.0
    assert s.loc["ORL", "close_total"] == 182.5 and s.loc["ORL", "open_total"] == 181.0
