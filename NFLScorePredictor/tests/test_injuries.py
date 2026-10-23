import numpy as np
import pandas as pd
import pytest

from nflpredictor.injuries import LOSS_COLUMNS, MISS_RATE, losses, roles
from nflpredictor.model import team_view


def snap(week, player, position, off=0.0, de=0.0, team="KC", season=2023):
    return {"season": season, "week": week, "game_type": "REG", "team": team, "player": player,
            "position": position, "offense_pct": off, "defense_pct": de}


def report(week, name, position, status, team="KC", season=2023):
    return {"season": season, "week": week, "game_type": "REG", "team": team, "full_name": name,
            "position": position, "report_status": status}


def test_role_is_the_recent_snap_share_on_the_right_side_of_the_ball():
    snaps = pd.DataFrame([snap(1, "Chris Jones", "DT", de=0.8), snap(2, "Chris Jones", "DT", de=0.6),
                          snap(1, "Travis Kelce", "TE", off=0.9, de=0.1), snap(1, "Harrison Butker", "K", off=0.0)])
    r = roles(snaps).set_index(["key", "t"])
    assert r.loc[("chrisjones", 2023 * 25 + 2), "role"] == pytest.approx(0.7)
    assert r.loc[("traviskelce", 2023 * 25 + 1), "role"] == 0.9 and r.loc[("traviskelce", 2023 * 25 + 1), "group"] == "skill"
    assert "harrisonbutker" not in r.index.get_level_values(0)          # kickers are in no group


def test_losses_weigh_each_listed_player_by_role_and_status():
    snaps = pd.DataFrame([snap(1, "Trent Williams", "T", off=1.0, team="SF"), snap(2, "Trent Williams", "T", off=1.0, team="SF"),
                          snap(1, "Deebo Samuel", "WR", off=0.8, team="SF"), snap(1, "Brock Purdy", "QB", off=1.0, team="SF"),
                          snap(1, "Fred Warner", "LB", de=1.0, team="SF")])
    injuries = pd.DataFrame([report(3, "Trent Williams", "T", "Out", team="SF"),
                             report(3, "Deebo Samuel", "WR", "Questionable", team="SF"),
                             report(3, "Brock Purdy", "QB", "Out", team="SF"),                # QBs have their own term
                             report(3, "Fred Warner", "LB", None, team="SF"),                 # practiced: no status
                             report(3, "Nobody Known", "CB", "Out", team="SF")])              # no snaps: no role
    out = losses(injuries, snaps).set_index(["season", "week", "team"])
    row = out.loc[(2023, 3, "SF")]
    assert row["inj_ol"] == pytest.approx(MISS_RATE["Out"])
    assert row["inj_skill"] == pytest.approx(0.8 * MISS_RATE["Questionable"])
    assert row["inj_front"] == 0.0 and row["inj_back"] == 0.0
    # The report for week 2 can only use week 1's snaps (none here before week 1).
    early = losses(pd.DataFrame([report(1, "Trent Williams", "T", "Out", team="SF")]), snaps)
    assert early.empty or early[LOSS_COLUMNS].to_numpy().sum() == 0.0


def test_points_map_takes_own_offense_and_opposing_defense_losses():
    games = pd.DataFrame({"game_id": ["g"], "season": [2023], "week": [3], "home_team": ["SF"], "away_team": ["KC"]})
    f = games.assign(neutral=False, home_rest=7, away_rest=7, div_game=0, env_points=22.0, home_score=20, away_score=17,
                     off_home=0.0, off_away=0.0, def_home=0.0, def_away=0.0, off_st_home=0.0, off_st_away=0.0,
                     def_st_home=0.0, def_st_away=0.0, home_qb_adj=0.0, away_qb_adj=0.0,
                     home_inj_ol=1.0, home_inj_skill=0.2, home_inj_front=0.5, home_inj_back=0.0)
    tv = team_view(f).set_index("side")
    assert tv.loc["home", "inj_ol"] == 1.0 and tv.loc["away", "inj_front_opp"] == 0.5
    assert tv.loc["away", "inj_ol"] == 0.0                                 # missing columns count as no loss
    assert np.isfinite(tv[["inj_skill", "inj_back_opp"]].to_numpy()).all()
