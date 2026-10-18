import numpy as np
import pandas as pd

from nhlpredictor.config import Hyperparams
from nhlpredictor.goalies import GoalieModel, starter_columns


def goalie_games():
    rows = []
    dates = pd.date_range("2025-10-01", periods=40, freq="2D")
    for i, d in enumerate(dates):
        starter = 2 if i % 5 == 4 else 1       # goalie 1 starts four of every five games
        for gid, start in ((1, starter == 1), (2, starter == 2)):
            if not start:
                continue
            ga = 1 if gid == 1 else 4
            rows.append({"game_id": i, "season": 2026, "date": d.strftime("%Y-%m-%d"), "team": "AAA",
                         "goalie_id": gid, "goalie_name": f"Goalie {gid}", "starter": True, "toi": 60.0,
                         "shots": 40, "xga": 3.0, "ga": ga})
        rows.append({"game_id": i, "season": 2026, "date": d.strftime("%Y-%m-%d"), "team": "BBB",
                     "goalie_id": 9, "goalie_name": "Goalie 9", "starter": True, "toi": 60.0,
                     "shots": 40, "xga": 3.0, "ga": 3})
    return pd.DataFrame(rows)


def test_values_are_shrunk_toward_the_prior():
    hp = Hyperparams()
    model = GoalieModel(goalie_games(), hp)
    v = model.values(int(model.g["dix"].max()) + 1)
    assert v[1] > v[9] and v[1] > v[2]
    raw_gap = 100 * (3.0 - 1.0) / 40          # goalie 1 saves 2 goals per 40 shots more than goalie 9
    assert 0 < v[1] - v[9] < raw_gap
    assert model.value_of(v, 12345) == hp.goalie_prior_value


def test_start_probabilities_favor_the_regular_and_mark_down_back_to_backs():
    model = GoalieModel(goalie_games(), Hyperparams())
    aaa = model.g[model.g["team"] == "AAA"]
    last = int(aaa["dix"].max())
    last_starter = int(aaa.loc[aaa["dix"].idxmax(), "goalie_id"])
    rested = model.start_probabilities("AAA", last + 2)
    assert rested[1] > 0.6 and abs(rested.sum() - 1) < 1e-9
    model.repeat_factor = 0.2
    tired = model.start_probabilities("AAA", last + 1)
    assert tired[last_starter] < rested[last_starter]


def test_starter_columns_use_known_starters_or_project():
    model = GoalieModel(goalie_games(), Hyperparams())
    games = pd.DataFrame({"home_team": ["AAA", "AAA"], "away_team": ["BBB", "BBB"],
                          "home_goalie_id": [2, np.nan], "away_goalie_id": [np.nan, 9],
                          "date": ["2026-01-01", "2026-01-01"]})
    dix = int(model.g["dix"].max()) + 5
    out = starter_columns(model, games, 2026, dix, 60.0)
    assert out.loc[0, "home_goalie_status"] == "known" and out.loc[0, "home_goalie_name"] == "Goalie 2"
    assert out.loc[1, "home_goalie_status"].startswith("projected")
    assert out.loc[0, "home_goalie_value"] < out.loc[1, "home_goalie_value"]   # the backup is worse
