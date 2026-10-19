import numpy as np
import pandas as pd

from nbapredictor.data import game_stints, reduce_players, reduce_schedule, reduce_teams


def raw_schedule():
    base = {"season": 2026, "season_type": 2, "status_type_name": "STATUS_FINAL", "status_type_completed": True,
            "neutral_site": False, "status_period": 4.0}
    rows = [
        dict(base, game_id=1, date="2025-11-01T23:30Z", home_abbreviation="SA", away_abbreviation="GS",
             home_score=110, away_score=100, venue_full_name="Frost Bank Center", venue_address_city="San Antonio",
             venue_address_state="TX"),
        dict(base, game_id=2, date="2025-11-03T23:30Z", home_abbreviation="SA", away_abbreviation="NY",
             home_score=99, away_score=101, venue_full_name="Moody Center", venue_address_city="Austin",
             venue_address_state="TX", status_period=5.0),
        dict(base, game_id=3, date="2025-11-05T02:00Z", home_abbreviation="GS", away_abbreviation="SA",
             home_score=120, away_score=118, venue_full_name="Chase Center", venue_address_city="San Francisco",
             venue_address_state="CA"),
        dict(base, game_id=7, date="2025-11-05T03:00Z", home_abbreviation="GS", away_abbreviation="NY",
             home_score=101, away_score=95, venue_full_name="Chase Center", venue_address_city="San Francisco",
             venue_address_state="CA"),
        dict(base, game_id=4, date="2025-11-06T02:00Z", home_abbreviation="GS", away_abbreviation="NY",
             home_score=0, away_score=0, venue_full_name="Arena CDMX", venue_address_city="Mexico City",
             venue_address_state=None, status_type_completed=False, status_type_name="STATUS_SCHEDULED"),
        dict(base, game_id=5, date="2026-02-15T01:00Z", home_abbreviation="STARS", away_abbreviation="STRIPES",
             home_score=50, away_score=48, venue_full_name="Intuit Dome", venue_address_city="Inglewood",
             venue_address_state="CA"),
        dict(base, game_id=6, date="2025-11-08T01:00Z", home_abbreviation="NY", away_abbreviation="GS",
             home_score=0, away_score=0, venue_full_name="MSG", venue_address_city="New York",
             venue_address_state="NY", status_type_name="STATUS_POSTPONED", status_type_completed=False),
    ]
    return pd.DataFrame(rows)


def test_schedule_codes_neutral_sites_and_unfinished_games():
    s = reduce_schedule(raw_schedule()).set_index("game_id")
    assert list(s.index) == [1, 2, 3, 7, 4]                   # all-star and postponed games dropped
    assert s.loc[1, "home_team"] == "SAS" and s.loc[1, "away_team"] == "GSW"
    assert not s.loc[2, "neutral"]                            # the Spurs' Austin games stay home games
    assert s.loc[4, "neutral"]                                # Mexico City is no team's home
    assert s.loc[2, "periods"] == 5 and np.isnan(s.loc[4, "home_score"])


def game(events):
    """Events as (period, seconds left, type, team, player 1, player 2, points); scores carried forward."""
    rows, hs, as_ = [], 0, 0
    for period, left, typ, team, a1, a2, pts in events:
        if pts:
            hs, as_ = (hs + pts, as_) if team == 1 else (hs, as_ + pts)
        rows.append({"period_number": period, "start_quarter_seconds_remaining": left, "type_text": typ,
                     "team_id": team, "athlete_id_1": a1, "athlete_id_2": a2, "athlete_id_3": None,
                     "home_score": hs, "away_score": as_,
                     "shooting_play": typ.endswith("Shot") or typ.startswith("Free Throw")})
    return pd.DataFrame(rows)


def two_period_game():
    """Home team 1 (players 1-6), away team 2 (players 11-15). Player 6 subs in
    for 5 in the first period. Between periods 5 comes back for 4 without a
    logged substitution; 3 records nothing in period 2, and 4 later re-enters."""
    ev = game([
        (1, 720, "Jumpball", 1, 1, 11, 0),
        (1, 700, "Jump Shot", 1, 2, None, 2),
        (1, 690, "Jump Shot", 2, 12, None, 0),
        (1, 688, "Offensive Rebound", 2, 13, None, 0),
        (1, 680, "Layup Shot", 2, 13, None, 2),
        (1, 650, "Lost Ball Turnover", 1, 3, None, 0),
        (1, 600, "Substitution", 1, 6, 5, 0),
        (1, 500, "Free Throw - 1 of 2", 2, 14, None, 1),
        (1, 500, "Free Throw - 2 of 2", 2, 14, None, 1),
        (1, 400, "Dunk Shot", 1, 4, None, 2),
        (1, 400, "Technical Foul", 2, 99, None, 0),            # a bench technical names no one on the floor
        (1, 0, "End Period", None, None, None, 0),
        (2, 700, "Jump Shot", 1, 5, None, 3),
        (2, 690, "Jump Shot", 2, 15, None, 0),
        (2, 680, "Defensive Rebound", 1, 6, None, 0),
        (2, 650, "Jump Shot", 1, 1, None, 2),
        (2, 600, "Substitution", 1, 4, 6, 0),
        (2, 590, "Jump Shot", 1, 2, None, 0),
        (2, 580, "Defensive Rebound", 2, 11, None, 0),
        (2, 400, "Jump Shot", 2, 12, None, 2),
    ])
    team_of = {float(p): 1 for p in range(1, 7)} | {float(p): 2 for p in range(11, 16)} | {99.0: 2}
    return ev, team_of


def test_stints_track_substitutions_and_period_starts():
    ev, team_of = two_period_game()
    stints = game_stints(ev, home_id=1, starters={1, 2, 3, 4, 5, 11, 12, 13, 14, 15}, team_of=team_of)
    assert [s["home_ids"] for s in stints] == ["1 2 3 4 5", "1 2 3 4 6", "1 2 3 5 6", "1 2 3 4 5"]
    assert all(s["away_ids"] == "11 12 13 14 15" for s in stints)
    assert [s["seconds"] for s in stints] == [120.0, 600.0, 120.0, 600.0]
    assert sum(s["home_pts"] for s in stints) == 9 and sum(s["away_pts"] for s in stints) == 6
    first = stints[0]
    # Home: 1 FGA + 1 turnover; away: 2 FGA - 1 offensive rebound.
    assert first["home_poss"] == 2.0 and first["away_poss"] == 1.0
    assert np.isclose(stints[1]["away_poss"], 0.88)           # two free throws
    assert all(s["valid"] for s in stints)


def test_garbage_time_needs_a_big_lead_and_the_bench():
    from nbapredictor.data import _flag_garbage

    def stint(start, ids, hs, as_):
        return {"period": 4, "start": start, "home_ids": ids, "away_ids": "11 12 13 14 15",
                "home_score": hs, "away_score": as_, "home_pts": 0, "away_pts": 0}
    starters = {1, 2, 3, 4, 5}
    bench = "6 7 8 9 10"
    stints = [stint(2160, "1 2 3 4 5", 90, 60), stint(2400, bench, 95, 62), stint(2600, bench, 100, 70)]
    _flag_garbage(stints, starters | {11, 12, 13, 14, 15})
    assert [s["garbage"] for s in stints] == [False, False, False]  # the away starters never sat
    stints = [stint(2160, "1 2 3 4 5", 90, 60), stint(2400, bench, 95, 62), stint(2600, bench, 100, 70)]
    _flag_garbage(stints, starters)
    assert [s["garbage"] for s in stints] == [False, True, True]


def test_turnovers_are_not_double_counted_and_possessions_average_both_teams():
    games = pd.DataFrame({"game_id": [1], "home_team": ["BOS"], "start": ["2010-11-01T23:00Z"],
                          "periods": [4.0], "season": [2011]})
    raw = pd.DataFrame({
        "game_id": [1, 1], "team_abbreviation": ["BOS", "NY"], "opponent_team_abbreviation": ["NY", "BOS"],
        "team_score": [100, 90], "opponent_team_score": [90, 100], "field_goals_attempted": [80, 84],
        "three_point_field_goals_attempted": [20, 25], "three_point_field_goals_made": [8, 9],
        "free_throws_attempted": [25, 20], "free_throws_made": [20, 15], "offensive_rebounds": [10, 12],
        "defensive_rebounds": [30, 28], "turnovers": [14, 12],
        "team_turnovers": [14, 1],                              # the old format repeats player turnovers
    })
    t = reduce_teams(raw, games, pd.DataFrame()).set_index("team")
    assert t.loc["BOS", "tov"] == 14 and t.loc["NYK", "tov"] == 13
    bos = 80 - 10 + 14 + 0.44 * 25
    nyk = 84 - 12 + 13 + 0.44 * 20
    assert np.isclose(t.loc["BOS", "poss"], (bos + nyk) / 2)
    assert t.loc["BOS", "clean_poss"] == t.loc["BOS", "poss"]   # no stints: the full game counts


def test_players_keep_healthy_scratches_apart_from_injuries():
    games = pd.DataFrame({"game_id": [1]})
    raw = pd.DataFrame({
        "game_id": [1] * 4, "athlete_id": [10.0, 11.0, 12.0, 13.0], "team_abbreviation": ["GS"] * 4,
        "minutes": [30.0, np.nan, np.nan, np.nan], "plus_minus": ["+5", None, None, None],
        "did_not_play": [False, True, True, False],
        "reason": ["COACH'S DECISION", "COACH'S DECISION", "LEFT ANKLE SPRAIN", None],
        "starter": [True, False, False, False], "athlete_display_name": list("ABCD"),
        "athlete_position_abbreviation": ["G"] * 4, "team_id": [9] * 4,
        **{c: [1, 0, 0, 0] for c in ("points", "field_goals_made", "field_goals_attempted",
                                     "three_point_field_goals_made", "three_point_field_goals_attempted",
                                     "free_throws_made", "free_throws_attempted", "offensive_rebounds",
                                     "defensive_rebounds", "assists", "steals", "blocks", "turnovers", "fouls")},
    })
    p = reduce_players(raw, games).set_index("player_id")
    assert list(p.index) == [10, 11, 12]                      # never-active players are dropped
    assert p.loc[10, "status"] == "played" and p.loc[10, "plus_minus"] == 5 and p.loc[10, "team"] == "GSW"
    assert p.loc[11, "status"] == "dnp" and p.loc[12, "status"] == "out"
