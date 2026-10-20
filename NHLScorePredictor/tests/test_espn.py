import numpy as np
import pandas as pd

from nhlpredictor.espn import attach, match_goalie, parse_scoreboard


def competitor(side, abbr, goalie=None, status="Probable", **odds):
    c = {"homeAway": side, "team": {"abbreviation": abbr}}
    if goalie:
        c["probables"] = [{"name": "probableStartingGoalie", "athlete": {"displayName": goalie},
                           "status": {"name": status}}]
    return c


def payload():
    return {"events": [
        {"id": "1", "date": "2026-10-19T23:00Z", "competitions": [{
            "competitors": [competitor("home", "NJ", "Jake Allen", "Confirmed"),
                            competitor("away", "TB", "Andrei Vasilevskiy")],
            "odds": [{"provider": {"name": "DraftKings"}, "details": "TB -140", "overUnder": 5.5,
                      "moneyline": {"home": {"close": {"odds": "+120"}}, "away": {"close": {"odds": "-140"}}},
                      "total": {"over": {"close": {"line": "o5.5", "odds": "-115"}},
                                "under": {"close": {"line": "u5.5", "odds": "-105"}}}}],
        }]},
        {"id": "2", "date": "2026-10-20T02:00Z", "competitions": [{
            "competitors": [competitor("home", "UTAH"), competitor("away", "LA")],
            "odds": [{"provider": {"name": "ESPN BET"}, "overUnder": 6.0,
                      "homeTeamOdds": {"moneyLine": -175, "favorite": True},
                      "awayTeamOdds": {"moneyLine": 150}}],
        }]},
        {"id": "3", "date": "2026-10-20T00:00Z", "competitions": [{
            "competitors": [competitor("home", "BOS"), competitor("away", "NYR")]}]},
    ]}


def test_parses_both_odds_formats_and_probables():
    board = parse_scoreboard(payload()).set_index("home_team")
    nj = board.loc["NJD"]
    assert nj.away_team == "TBL" and nj.home_moneyline == 120 and nj.away_moneyline == -140
    assert nj.total_line == 5.5 and nj.over_price == -115 and nj.under_price == -105
    assert nj.home_probable == "Jake Allen" and nj.home_probable_status == "Confirmed"
    assert nj.line_source == "ESPN (DraftKings)"
    uta = board.loc["UTA"]
    assert uta.away_team == "LAK" and uta.home_moneyline == -175 and uta.total_line == 6.0
    assert str(uta.date) == "2026-10-19"                  # 10 PM Eastern
    assert np.isnan(board.loc["BOS"].home_moneyline) and pd.isna(board.loc["BOS"].line_source)


def test_goalie_names_match_with_accents_and_initials():
    names = pd.Series({1: "Jake Allen", 2: "Andrei Vasilevskiy", 3: "Juuse Saros"})
    assert match_goalie("Andréi Vasilevskiy", names) == 2
    assert match_goalie("J. Allen", names) == 1
    assert match_goalie("Unknown Guy", names) is None


def test_attach_adds_lines_and_starters_to_matching_games():
    games = pd.DataFrame({"game_id": [10, 11], "date": [pd.Timestamp("2026-10-19").date()] * 2,
                          "home_team": ["NJD", "UTA"], "away_team": ["TBL", "LAK"]})
    names = pd.Series({1: "Jake Allen", 2: "Andrei Vasilevskiy"})
    out = attach(games, parse_scoreboard(payload()), names, {"NJD": names.loc[[1]]}).set_index("game_id")
    assert out.loc[10, "home_goalie_id"] == 1 and out.loc[10, "home_goalie_source"] == "ESPN confirmed"
    assert out.loc[10, "away_goalie_id"] == 2              # matched across the league
    assert out.loc[11, "home_moneyline"] == -175 and np.isnan(out.loc[11, "home_goalie_id"])


def odds_board(*odds_list):
    return {"events": [{"id": str(i), "date": "2026-10-19T23:00Z", "competitions": [{
        "competitors": [competitor("home", "BOS"), competitor("away", f"T{i}")], "odds": [odds]}]}
        for i, odds in enumerate(odds_list)]}


def test_parses_the_puck_line_in_new_and_old_formats():
    new = {"pointSpread": {
        "home": {"open": {"line": "-1.5", "odds": "+160"}, "close": {"line": "-1.5", "odds": "+145"}},
        "away": {"open": {"line": "+1.5", "odds": "-190"}, "close": {"line": "+1.5", "odds": "-175"}}}}
    away_fav = {"pointSpread": {"away": {"current": {"line": "-1.5", "odds": "+210"}},
                                "home": {"current": {"odds": "-260"}}}}
    old = {"spread": 1.5, "homeTeamOdds": {"moneyLine": 150, "spreadOdds": -200.0},
           "awayTeamOdds": {"moneyLine": -170, "spreadOdds": 165.0}}
    opening = {"pointSpread": {"home": {"open": {"line": "+1.5", "odds": "EVEN"}},
                               "away": {"open": {"line": "-1.5", "odds": "-120"}}}}
    board = parse_scoreboard(odds_board(new, away_fav, old, opening, {})).set_index("away_team")
    assert tuple(board.loc["T0", ["home_spread_line", "home_spread_price", "away_spread_price"]]) == (-1.5, 145, -175)
    assert tuple(board.loc["T1", ["home_spread_line", "home_spread_price", "away_spread_price"]]) == (1.5, -260, 210)
    assert tuple(board.loc["T2", ["home_spread_line", "home_spread_price", "away_spread_price"]]) == (1.5, -200, 165)
    assert board.loc["T2", "home_moneyline"] == 150
    assert tuple(board.loc["T3", ["home_spread_line", "home_spread_price", "away_spread_price"]]) == (1.5, 100, -120)
    assert board.loc["T4", ["home_spread_line", "home_spread_price", "away_spread_price"]].isna().all()


def test_total_prices_fall_back_from_close_to_current_and_old_fields():
    current = {"total": {"over": {"current": {"line": "o6.5", "odds": "+100"}},
                         "under": {"current": {"line": "u6.5", "odds": "-120"}}}}
    old = {"overUnder": 5.5, "overOdds": -105.0, "underOdds": -115.0}
    no_prices = {"overUnder": 6.0}
    board = parse_scoreboard(odds_board(current, old, no_prices)).set_index("away_team")
    assert tuple(board.loc["T0", ["total_line", "over_price", "under_price"]]) == (6.5, 100, -120)
    assert tuple(board.loc["T1", ["total_line", "over_price", "under_price"]]) == (5.5, -105, -115)
    assert board.loc["T2", "total_line"] == 6.0 and board.loc["T2", ["over_price", "under_price"]].isna().all()
