import numpy as np
import pandas as pd
import pytest

from nhlpredictor.model import team_view
from nhlpredictor.skaters import losses, toi_minutes


def schedule(n):
    """BOS at home against MTL, one game a day."""
    return pd.DataFrame({"game_id": range(1, n + 1), "start": pd.date_range("2025-10-01", periods=n, tz="UTC"),
                         "home_team": "BOS", "away_team": "MTL"})


def box(game_id, skaters, side="home"):
    return [{"game_id": game_id, "home_away": side, "player_id": pid, "position": pos, "toi": toi, "points": pts}
            for pid, pos, toi, pts in skaters]


def test_toi_strings_become_minutes():
    assert toi_minutes(pd.Series(["15:30", "0:45"])).tolist() == [15.5, 0.75]
    assert toi_minutes(pd.Series([12.0])).tolist() == [12.0]


def test_a_regular_missing_from_the_last_game_counts_by_his_role():
    star = (88, "R", "21:00", 1)
    dman = (73, "D", "24:00", 0)
    depth = (11, "C", "9:00", 0)
    rows = []
    for gid in (1, 2, 3):
        rows += box(gid, [star, dman, depth])
    rows += box(4, [dman, depth])                     # the star misses game 4
    out = losses(pd.DataFrame(rows), schedule(6)).set_index(["game_id", "team"])
    assert out.loc[(3, "BOS")].sum() == 0.0          # only two games behind it: nobody is a regular yet
    assert out.loc[(4, "BOS")].sum() == 0.0          # everyone played game 3
    after = out.loc[(5, "BOS")]
    assert after["lost_f"] == pytest.approx(21.0 / 60) and after["lost_d"] == 0.0 and after["lost_pts"] == 1.0
    # Game 6 has no box yet (it is upcoming): it is judged on game 4, the last one played.
    assert out.loc[(6, "BOS")]["lost_f"] == pytest.approx(21.0 / 60)
    assert out.loc[(5, "MTL")].sum() == 0.0          # the other team had no box rows at all


def test_goal_model_sees_own_losses_and_the_opponents_ice_time():
    f = pd.DataFrame({"game_id": [1], "home_lost_f": [0.35], "home_lost_d": [0.0], "home_lost_pts": [1.0],
                      "away_lost_f": [0.1], "away_lost_d": [0.4], "away_lost_pts": [0.2]})
    for side in ("home", "away"):
        for name in ("ev", "pp", "draw", "goals"):
            f[f"off_{name}_{side}"] = 0.0
            f[f"def_{name}_{side}"] = 0.0
        f[f"{side}_goalie_value"] = 0.0
        f[f"{side}_goalie_adj"] = 0.0
        f[f"{side}_rest"] = 2
    f = f.assign(elo_edge=0.0, neutral=False, playoff=False, env_goals=3.0)
    tv = team_view(f).set_index("side")
    assert tv.loc["home", "lost_f"] == 0.35 and tv.loc["home", "lost_opp"] == pytest.approx(0.5)
    assert tv.loc["away", "lost_d"] == 0.4 and tv.loc["away", "lost_opp"] == pytest.approx(0.35)
    assert np.isfinite(tv["lost_pts"]).all()
