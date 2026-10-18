import datetime as dt

import numpy as np
import pandas as pd

from nhlpredictor.data import current_season, prepare_games, reduce_schedule, summarize_pbp
from nhlpredictor.shots import FEATURES, SCORE_STATES, ShotModel


def test_current_season_rolls_over_in_august():
    assert current_season(dt.date(2026, 10, 18)) == 2027
    assert current_season(dt.date(2027, 6, 20)) == 2027
    assert current_season(dt.date(2027, 8, 1)) == 2028


def raw_schedule():
    return pd.DataFrame([
        {"game_id": 1, "season": 2027, "game_type": "R", "game_time": "2026-10-10T23:00:00Z",
         "home_team_abbr": "ARI", "away_team_abbr": "ATL", "home_score": 3, "away_score": 2,
         "game_state": "OFF", "venue": "Arena A"},
        {"game_id": 2, "season": 2027, "game_type": "R", "game_time": "2026-10-12T00:00:00Z",
         "home_team_abbr": "NSH", "away_team_abbr": "PIT", "home_score": None, "away_score": None,
         "game_state": "FUT", "venue": "Avicii Arena"},
        {"game_id": 3, "season": 2027, "game_type": "R", "game_time": "2026-10-13T18:00:00Z",
         "home_team_abbr": "PIT", "away_team_abbr": "NSH", "home_score": 1, "away_score": 4,
         "game_state": "LIVE", "venue": "Avicii Arena"},
        {"game_id": 4, "season": 2027, "game_type": "PR", "game_time": "2026-09-20T23:00:00Z",
         "home_team_abbr": "BOS", "away_team_abbr": "NYR", "home_score": 1, "away_score": 0,
         "game_state": "OFF", "venue": "TD Garden"},
    ])


def test_schedule_aliases_teams_and_flags_neutral_sites():
    g = prepare_games(reduce_schedule(raw_schedule())).set_index("game_id")
    assert list(g.index) == [1, 2, 3]                       # preseason dropped
    assert g.loc[1, "home_team"] == "UTA" and g.loc[1, "away_team"] == "WPG"
    assert g.loc[1, "completed"] and not g.loc[3, "completed"]   # live games have no final score yet
    assert np.isnan(g.loc[3, "home_score"])
    assert g.loc[2, "neutral"] and g.loc[3, "neutral"] and not g.loc[1, "neutral"]
    assert g.loc[2, "date"] == dt.date(2026, 10, 11)        # 8 PM Eastern


def event(idx, secs, kind, side=None, **kw):
    base = dict(game_id=10, event_idx=idx, game_seconds=secs, period=min(secs // 1200 + 1, 4),
                period_type="REGULAR" if secs < 3600 else "OVERTIME", event_type=kind,
                event_team_type=side, home_score=0, away_score=0, home_skaters=5, away_skaters=5,
                home_goalie_in=1, away_goalie_in=1, empty_net=False, extra_attacker=False,
                x=60.0, shot_distance=25.0, shot_angle=20.0, secondary_type="wrist",
                event_goalie_id=None, event_goalie_name=None, season=20262027, season_type="R",
                home_abbr="BOS", away_abbr="NYR")
    base.update(kw)
    return base


def flat_model():
    coef = np.zeros(1 + len(FEATURES))
    coef[0] = np.log(0.1 / 0.9)                              # every shot is worth 0.1 xG
    weights = {s: 1.0 for s in SCORE_STATES}
    return ShotModel(coef, weights, weights)


def test_summarize_counts_goals_empty_netters_shootout_and_time():
    pbp = pd.DataFrame([
        event(1, 0, "FACEOFF"),
        event(2, 600, "SHOT", "home", event_goalie_id=2.0, event_goalie_name="Away G"),
        event(3, 700, "GOAL", "home", home_score=1, event_goalie_id=2.0, event_goalie_name="Away G"),
        event(4, 1000, "PENALTY", "away"),
        event(5, 1000, "FACEOFF", home_skaters=5, away_skaters=4),
        event(6, 1060, "GOAL", "home", home_score=2, home_skaters=5, away_skaters=4,
              event_goalie_id=2.0, event_goalie_name="Away G"),
        event(7, 1060, "FACEOFF", home_score=2),
        event(8, 3500, "FACEOFF", home_score=2, away_score=0, away_goalie_in=0, away_skaters=6),
        event(9, 3530, "GOAL", "home", home_score=3, away_goalie_in=0, away_skaters=6, empty_net=True),
        event(10, 3530, "FACEOFF", home_score=3),
        event(11, 3600, "PERIOD_END", home_score=3, period=3, period_type="REGULAR"),
    ])
    box = pd.DataFrame([
        {"game_id": 10, "team_abbrev": "BOS", "player_id": 1, "player_name": "H. Goalie", "toi": "60:00",
         "starter": True, "season": 20262027},
        {"game_id": 10, "team_abbrev": "NYR", "player_id": 2, "player_name": "A. Goalie", "toi": "59:30",
         "starter": True, "season": 20262027},
    ])
    sched = pd.DataFrame({"game_id": [10], "start": [pd.Timestamp("2026-10-10 23:00", tz="UTC")]})
    teams, goalies, states = summarize_pbp(pbp, box, flat_model(), sched)
    home = teams.set_index("team").loc["BOS"]
    away = teams.set_index("team").loc["NYR"]
    assert home.gf == 2 and home.en_gf == 1 and home.reg_gf == 2 and away.ga == 2
    assert home.gf_pp == 1 and away.ga_sh == 1 and home.gf_ev == 1
    assert np.isclose(home.toi_pp, 1.0) and np.isclose(away.toi_sh, 1.0)   # 1000s-1060s on the power play
    assert np.isclose(home.xgf_ev, 0.2) and np.isclose(home.xgf_pp, 0.1)
    assert home.periods == 3 and home.shootout == 0 and home.date == "2026-10-10"
    g = goalies.set_index("goalie_id").loc[2]
    assert g.shots == 3 and g.ga == 2 and g.goalie_name == "Away G"    # the empty-netter is not his
    pulled = states[states["pulled"] == "away"]
    assert pulled["seconds"].sum() == 30 and pulled["home_goals"].sum() == 1
