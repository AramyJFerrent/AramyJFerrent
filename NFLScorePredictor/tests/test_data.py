import datetime as dt

import numpy as np
import pandas as pd

from nflpredictor.data import LOPSIDED_WEIGHT, current_season, prepare_games, summarize_pbp


def test_current_season_rolls_over_in_march():
    assert current_season(dt.date(2026, 10, 17)) == 2026
    assert current_season(dt.date(2027, 1, 20)) == 2026
    assert current_season(dt.date(2027, 3, 1)) == 2027


def play(**kw):
    base = dict(game_id="2025_01_AAA_BBB", season=2025, week=1, season_type="REG",
                home_team="BBB", away_team="AAA", posteam="AAA", defteam="BBB",
                play_type="pass", epa=0.5, wp=0.5, success=1.0, fumble_lost=0, qb_dropback=1,
                id="QB1", name="A.Passer", td_team=None, field_goal_result=None,
                extra_point_attempt=0, extra_point_result=None, two_point_attempt=0,
                two_point_conv_result=None, safety=0, fixed_drive=1)
    base.update(kw)
    return base


def test_summarize_counts_efficiency_and_scoring():
    pbp = pd.DataFrame([
        play(),
        play(epa=-1.0, success=0.0, wp=0.95),                       # lopsided: down-weighted
        play(play_type="run", qb_dropback=0, epa=0.2, id="RB1", name="R.Back"),
        play(epa=-4.0, fumble_lost=1, success=0.0),                 # lost fumble counts half
        play(td_team="AAA", epa=3.0),
        play(play_type="extra_point", epa=0.2, extra_point_attempt=1, extra_point_result="good"),
        play(posteam="BBB", defteam="AAA", play_type="field_goal", epa=0.1,
             field_goal_result="made", id=None, qb_dropback=0, fixed_drive=2),
        play(epa=0.3, fixed_drive=3),
    ])
    teams, qbs = summarize_pbp(pbp)
    aaa = teams.set_index("team").loc["AAA"]
    bbb = teams.set_index("team").loc["BBB"]
    assert aaa.plays == 6 and aaa.home == 0 and bbb.home == 1
    assert aaa.drives == 2 and bbb.drives == 0
    assert np.isclose(aaa.st_epa, 0.2 - 0.1) and np.isclose(bbb.st_epa, -aaa.st_epa)
    assert np.isclose(aaa.rush_w + aaa.pass_w, aaa.w) and aaa.rush_w == 1.0
    assert aaa.tds == 1 and aaa.xp_made == 1 and bbb.fgs == 1
    expected_w = 5 + LOPSIDED_WEIGHT
    assert np.isclose(aaa.w, expected_w)
    expected_epa = 0.5 + (-1.0 * LOPSIDED_WEIGHT) + 0.2 + (-2.0) + 3.0 + 0.3
    assert np.isclose(aaa.epa, expected_epa)
    assert bbb.plays == 0
    qb = qbs.set_index("qb_id").loc["QB1"]
    assert qb.dropbacks == 5 and qb.team == "AAA"


def test_prepare_games_normalizes_teams_and_kickoff():
    raw = pd.DataFrame([{
        "game_id": "2012_01_SD_OAK", "season": 2012, "game_type": "REG", "week": 1,
        "gameday": "2012-09-10", "gametime": "22:15", "away_team": "SD", "home_team": "OAK",
        "away_score": 22, "home_score": 14, "location": "Home", "div_game": 1,
        "home_rest": 7, "away_rest": 7,
    }])
    g = prepare_games(raw).iloc[0]
    assert g.home_team == "LV" and g.away_team == "LAC"
    assert g.completed and not g.neutral and not g.playoff
    assert g.kickoff == pd.Timestamp("2012-09-11 02:15", tz="UTC")
