import datetime as dt

import numpy as np
import pandas as pd

from cfbpredictor.data import (
    FUMBLE_LOST_EPA_SCALE, current_season, pbp_lines, prepare_games, season_weeks, summarize_pbp,
)


def test_current_season_rolls_over_in_march():
    assert current_season(dt.date(2026, 10, 17)) == 2026
    assert current_season(dt.date(2027, 1, 19)) == 2026      # the title game is in January
    assert current_season(dt.date(2027, 3, 1)) == 2027


def test_postseason_weeks_follow_the_regular_season():
    kick = pd.to_datetime(pd.Series(["2025-11-29", "2025-12-13", "2025-12-21", "2026-01-19"]), utc=True)
    weeks = season_weeks(pd.Series(["regular", "postseason", "postseason", "postseason"]),
                         pd.Series([14, 1, 1, 1]), kick, pd.Series([2025] * 4))
    assert list(weeks) == [14, 17, 18, 22]


def schedule_row(**kw):
    base = dict(game_id=1, season=2026, week=1, season_type="regular", start_date="2026-08-29T16:00:00.000Z",
                start_time_tbd=False, completed=True, neutral_site=False, conference_game=True, venue_id=1,
                venue="V", home_team="Home U", away_team="Away U", home_division="fbs", away_division="fbs",
                home_conference="SEC", away_conference="SEC", home_points=31.0, away_points=17.0, notes=None)
    base.update(kw)
    return base


def test_prepare_games_keeps_fbs_games_and_flags_the_playoff():
    raw = pd.DataFrame([
        schedule_row(),
        schedule_row(game_id=2, away_division="fcs"),
        schedule_row(game_id=3, home_division="fcs", away_division="fcs"),       # no FBS team
        schedule_row(game_id=4, away_division="ii"),                             # Division II opponent
        schedule_row(game_id=5, season_type="postseason", start_date="2026-12-20T01:00:00.000Z",
                     notes="College Football Playoff First Round Game", completed=False,
                     home_points=None, away_points=None),
    ])
    g = prepare_games(raw).set_index("game_id")
    assert list(g.index) == [1, 2, 5]
    assert g.loc[1, "completed"] and g.loc[1, "kickoff"] == pd.Timestamp("2026-08-29 16:00", tz="UTC")
    assert g.loc[5, "playoff"] and not g.loc[5, "bowl"] and g.loc[5, "week"] == 17
    assert not g.loc[5, "completed"]


def play(**kw):
    base = dict(game_id=10, season=2026, week=1, season_type="regular", start_date="2026-08-29T16:00:00.000Z",
                home="Home U", away="Away U", neutral_site=False,
                home_team_division="fbs", away_team_division=None, home_team_conference="SEC",
                away_team_conference=None, pos_team="Home U", def_pos_team="Away U", play_type="Rush",
                play_text="J.Back rush for 5 yards", EPA=0.4, success=1.0, period=1, pos_score_diff_start=0,
                drive_id=1.0, spread=-21.5, over_under=55.5,
                completion_player_id=None, completion_player=None, completion_yds=None,
                incompletion_player_id=None, incompletion_player=None,
                interception_thrown_player_id=None, interception_thrown_player=None,
                sack_taken_player_id=None, sack_taken_player=None, reception_player_id=None,
                reception_yds=None, rush_player_id=7.0, rush_yds=5.0, sack_player_id=None,
                interception_player_id=None, pass_breakup_player_id=None, fumble_forced_player_id=None)
    base.update(kw)
    base.setdefault("pass", 0.0)
    base.setdefault("rush", 1.0 if base["play_type"].startswith("Rush") else 0.0)
    return base


def test_summarize_filters_garbage_time_and_counts_units():
    teams = pd.DataFrame({"division": {"Home U": "fbs", "Away U": "fcs"},
                          "conference": {"Home U": "SEC", "Away U": "Big Sky"}})
    pbp = pd.DataFrame([
        play(rush_yds=25.0),
        play(**{"pass": 1.0}, rush=0.0, play_type="Pass Reception", EPA=1.0, completion_player_id=3.0,
             completion_player="Q.Back", completion_yds=20.0, reception_player_id=8.0, reception_yds=20.0,
             rush_player_id=None, rush_yds=None, play_text="Q.Back pass complete to W.Out"),
        play(EPA=-2.0, play_type="Fumble Recovery (Opponent)", rush=0.0,
             play_text="J.Back rush for 2 yards fumbled, recovered by Away U"),       # lost: half EPA
        play(EPA=0.9, period=4, pos_score_diff_start=30),                             # garbage time
        play(play_text="Q.Back kneel down", EPA=-0.1),                                # kneel: ignored
        play(play_type="Field Goal Good", rush=0.0, EPA=1.5, drive_id=2.0, rush_player_id=None),
        play(play_type="Kickoff", rush=0.0, pos_team="Away U", def_pos_team="Home U", EPA=-0.3,
             drive_id=3.0, rush_player_id=None),
        play(pos_team="Away U", def_pos_team="Home U", EPA=-0.5, drive_id=3.0, rush_player_id=9.0),
    ])
    tg, prod = summarize_pbp(pbp, teams)
    home = tg.set_index("team").loc["Home U"]
    away = tg.set_index("team").loc["Away U"]
    assert home.home == 1 and away.home == 0
    assert away.division == "fcs" and away.conference == "Big Sky"      # filled in from team info
    assert home.plays == 4 and home.w == 3 and home.g_plays == 1
    assert np.isclose(home.epa, 0.4 + 1.0 - 2.0 * FUMBLE_LOST_EPA_SCALE)
    assert np.isclose(home.g_epa, 0.9)
    assert np.isclose(home.pass_w, 1) and np.isclose(home.rush_w, 2)
    assert home.fgs == 1 and home.drives == 2
    assert np.isclose(home.st_epa, 1.5 + 0.3) and np.isclose(away.st_epa, -home.st_epa)
    p = prod.set_index("athlete_id")
    assert p.loc[3, "pass_yds"] == 20 and p.loc[8, "rec_yds"] == 20 and p.loc[7, "team"] == "Home U"


def test_pbp_lines_are_home_margins():
    pbp = pd.DataFrame([play(), play(game_id=11, spread=3.0, over_under=0.0)])
    lines = pbp_lines(pbp).set_index("game_id")
    assert lines.loc[10, "spread_line"] == 21.5 and lines.loc[10, "total_line"] == 55.5
    assert lines.loc[11, "spread_line"] == -3.0 and np.isnan(lines.loc[11, "total_line"])
