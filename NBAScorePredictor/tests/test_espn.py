import numpy as np
import pandas as pd

from nbapredictor.espn import attach_lines, parse_injuries, parse_roster, parse_scoreboard


def competitor(side, abbr):
    return {"homeAway": side, "team": {"abbreviation": abbr}}


def payload():
    return {"events": [
        {"id": "1", "date": "2026-10-20T23:30Z", "competitions": [{
            "competitors": [competitor("home", "NY"), competitor("away", "BOS")],
            "odds": [{"provider": {"name": "DraftKings"}, "details": "NY -4.5", "overUnder": 224.5, "spread": -4.5,
                      "moneyline": {"home": {"open": {"odds": "-160"}, "close": {"odds": "-185"}},
                                    "away": {"open": {"odds": "+135"}, "close": {"odds": "+155"}}},
                      "pointSpread": {"home": {"open": {"line": "-3.5", "odds": "-110"},
                                               "close": {"line": "-4.5", "odds": "-110"}},
                                      "away": {"open": {"line": "+3.5"}, "close": {"line": "+4.5"}}},
                      "total": {"over": {"open": {"line": "o222.5"}, "close": {"line": "o224.5", "odds": "-110"}},
                                "under": {"open": {"line": "u222.5"}, "close": {"line": "u224.5"}}}}],
        }]},
        {"id": "2", "date": "2026-10-21T02:30Z", "competitions": [{
            "competitors": [competitor("home", "GS"), competitor("away", "LAL")],
            "odds": [{"provider": {"name": "ESPN BET"}, "details": "LAL -2", "overUnder": 230.0, "spread": 2.0,
                      "homeTeamOdds": {"moneyLine": 110}, "awayTeamOdds": {"moneyLine": -130}}],
        }]},
        {"id": "3", "date": "2026-10-21T00:00Z", "competitions": [{
            "competitors": [competitor("home", "UTAH"), competitor("away", "SA")]}]},
    ]}


def test_parses_both_odds_formats_with_the_home_margin_convention():
    board = parse_scoreboard(payload()).set_index("home_team")
    ny = board.loc["NYK"]
    assert ny.away_team == "BOS" and ny.spread == 4.5 and ny.total == 224.5
    assert ny.home_moneyline == -185 and ny.away_moneyline == 155
    assert ny.open_spread == 3.5 and ny.open_total == 222.5 and ny.line_source == "ESPN (DraftKings)"
    gs = board.loc["GSW"]
    assert gs.away_team == "LAL" and gs.spread == -2.0 and gs.home_moneyline == 110
    assert str(gs.date) == "2026-10-20"                    # 10:30 PM Eastern
    assert np.isnan(gs.open_spread)
    ut = board.loc["UTA"]
    assert ut.away_team == "SAS" and np.isnan(ut.spread) and pd.isna(ut.line_source)


def test_attach_lines_matches_date_and_teams():
    games = pd.DataFrame({"game_id": [7, 8], "date": [pd.Timestamp("2026-10-20").date()] * 2,
                          "home_team": ["NYK", "MIA"], "away_team": ["BOS", "ORL"]})
    out = attach_lines(games, parse_scoreboard(payload())).set_index("game_id")
    assert out.loc[7, "spread"] == 4.5 and np.isnan(out.loc[8, "spread"])


def test_injury_report_reads_ids_from_links_and_uids():
    report = {"injuries": [
        {"id": "2", "displayName": "Boston Celtics", "injuries": [
            {"status": "Out", "shortComment": "Achilles", "details": {"returnDate": "2027-02-01"},
             "athlete": {"displayName": "Jayson Tatum",
                         "links": [{"href": "https://www.espn.com/nba/player/_/id/4065648/jayson-tatum"}]}},
            {"type": {"description": "questionable"}, "athlete": {"displayName": "Derrick White",
                                                                  "uid": "s:40~l:46~a:3078576"}},
        ]},
        {"id": "18", "injuries": [{"status": "Day-To-Day", "athlete": {"id": "3934672", "displayName": "Jalen Brunson"}}]},
    ]}
    inj = parse_injuries(report, {"2": "BOS", "18": "NYK"}).set_index("player_id")
    assert inj.loc[4065648, "team"] == "BOS" and inj.loc[4065648, "status"] == "Out"
    assert inj.loc[4065648, "return_date"] == "2027-02-01"
    assert inj.loc[3078576, "status"] == "questionable"
    assert inj.loc[3934672, "team"] == "NYK"


def test_roster_lists_players_and_their_injuries_in_either_layout():
    flat = {"athletes": [{"id": "1", "displayName": "A", "position": {"abbreviation": "G"}},
                         {"id": "2", "displayName": "B", "injuries": [{"status": "Out"}]}]}
    grouped = {"athletes": [{"position": "guards", "items": [{"id": "3", "displayName": "C"}]}]}
    roster, hurt = parse_roster(flat, "MIA")
    assert list(roster["player_id"]) == [1, 2] and list(hurt["player_id"]) == [2]
    roster, hurt = parse_roster(grouped, "MIA")
    assert list(roster["player_id"]) == [3] and hurt.empty
