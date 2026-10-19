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
