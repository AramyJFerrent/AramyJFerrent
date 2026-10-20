import numpy as np
import pandas as pd

from mlbpredictor.espn import attach, parse_scoreboard


def event(home, away, start, odds):
    return {"date": start, "competitions": [{
        "competitors": [{"homeAway": "home", "team": {"abbreviation": home}},
                        {"homeAway": "away", "team": {"abbreviation": away}}],
        "odds": [odds]}]}


def test_both_odds_formats_and_team_codes():
    payload = {"events": [
        event("CHW", "OAK", "2026-05-01T23:10Z", {"provider": {"name": "DraftKings"}, "overUnder": 8.5,
                                                   "homeTeamOdds": {"moneyLine": -135}, "awayTeamOdds": {"moneyLine": 115}}),
        event("NYY", "BOS", "2026-05-01T23:05Z", {"moneyline": {"home": {"close": {"odds": "-150"}},
                                                                 "away": {"close": {"odds": "+130"}}},
                                                   "total": {"over": {"close": {"line": "o9", "odds": "-110"}},
                                                             "under": {"close": {"odds": "-110"}}}}),
    ]}
    b = parse_scoreboard(payload).set_index("home_team")
    assert b.loc["CWS", "away_team"] == "ATH" and b.loc["CWS", "home_moneyline"] == -135
    assert b.loc["CWS", "total_line"] == 8.5 and b.loc["CWS", "line_source"] == "ESPN (DraftKings)"
    assert b.loc["NYY", "away_moneyline"] == 130 and b.loc["NYY", "total_line"] == 9 and b.loc["NYY", "over_price"] == -110


def test_doubleheaders_match_by_start_time():
    board = parse_scoreboard({"events": [
        event("NYY", "BOS", "2026-05-02T17:05Z", {"homeTeamOdds": {"moneyLine": -110}, "awayTeamOdds": {"moneyLine": -110}}),
        event("NYY", "BOS", "2026-05-02T23:05Z", {"homeTeamOdds": {"moneyLine": -160}, "awayTeamOdds": {"moneyLine": 140}}),
    ]})
    games = pd.DataFrame({"game_id": ["g2", "g1"], "home_team": "NYY", "away_team": "BOS",
                          "date": pd.Timestamp("2026-05-02").date(),
                          "start": pd.to_datetime(["2026-05-02T23:05Z", "2026-05-02T17:05Z"], utc=True)})
    out = attach(games, board).set_index("game_id")
    assert out.loc["g1", "home_moneyline"] == -110 and out.loc["g2", "home_moneyline"] == -160
    assert np.isnan(attach(games, board.iloc[:0])["home_moneyline"]).all()


def test_run_line_and_prices_in_both_formats():
    payload = {"events": [
        # Current format: the away team gives the 1.5 runs; close prices win over open ones.
        event("NYY", "BOS", "2026-05-01T23:05Z", {
            "pointSpread": {"home": {"open": {"line": "+1.5", "odds": "-165"},
                                     "close": {"line": "+1.5", "odds": "-180"}},
                            "away": {"open": {"line": "-1.5", "odds": "+140"},
                                     "close": {"line": "-1.5", "odds": "+155"}}},
            "total": {"over": {"open": {"line": "o8.5", "odds": "-105"}, "close": {"line": "o8", "odds": "-120"}},
                      "under": {"close": {"line": "u8", "odds": "EVEN"}}}}),
        # Older format: the home team's spread and each team's spreadOdds, with over and under odds.
        event("LAD", "SD", "2026-05-01T02:10Z", {"spread": -1.5, "overUnder": 7.5, "overOdds": -115,
                                                  "underOdds": -105,
                                                  "homeTeamOdds": {"moneyLine": -170, "spreadOdds": 120},
                                                  "awayTeamOdds": {"moneyLine": 150, "spreadOdds": -140}}),
        # Older format with an unsigned spread: the flagged favorite gives the runs.
        event("CHC", "STL", "2026-05-01T02:10Z", {"spread": 1.5, "homeTeamOdds": {"favorite": True, "spreadOdds": 130},
                                                  "awayTeamOdds": {"favorite": False, "spreadOdds": -150}}),
        # Only the away side's line, no prices: the line is kept and the prices stay missing.
        event("SEA", "TEX", "2026-05-01T02:10Z", {"pointSpread": {"away": {"close": {"line": "+1.5"}}}}),
        event("MIA", "ATL", "2026-05-01T02:10Z", {}),
    ]}
    b = parse_scoreboard(payload).set_index("home_team")
    assert tuple(b.loc["NYY", ["home_run_line", "home_run_line_price", "away_run_line_price"]]) == (1.5, -180, 155)
    assert tuple(b.loc["NYY", ["total_line", "over_price", "under_price"]]) == (8, -120, 100)
    assert tuple(b.loc["LAD", ["home_run_line", "home_run_line_price", "away_run_line_price"]]) == (-1.5, 120, -140)
    assert tuple(b.loc["LAD", ["total_line", "over_price", "under_price"]]) == (7.5, -115, -105)
    assert tuple(b.loc["CHC", ["home_run_line", "home_run_line_price", "away_run_line_price"]]) == (-1.5, 130, -150)
    assert b.loc["SEA", "home_run_line"] == -1.5 and np.isnan(b.loc["SEA", "home_run_line_price"])
    assert b.loc[["MIA"], ["home_run_line", "total_line", "home_moneyline"]].isna().all(axis=None)
    games = pd.DataFrame({"game_id": ["g"], "home_team": "NYY", "away_team": "BOS",
                          "date": pd.Timestamp("2026-05-01").date(), "start": pd.NaT})
    assert attach(games, parse_scoreboard(payload)).loc[0, "away_run_line_price"] == 155


def test_raw_odds_lists_each_game():
    from mlbpredictor.espn import raw_odds

    odds = {"spread": -1.5}
    payload = {"events": [{**event("NYY", "BOS", "2026-05-01T23:05Z", odds), "shortName": "BOS @ NYY"}]}
    assert raw_odds(payload) == [("BOS @ NYY", odds)]
