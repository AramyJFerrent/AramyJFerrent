import numpy as np
import pandas as pd

from nhlpredictor.shots import FEATURES, ShotModel, design, fit_logistic, shot_events


def ev(idx, secs, kind, side, **kw):
    base = dict(game_id=1, event_idx=idx, game_seconds=secs, period=1, period_type="REGULAR",
                event_type=kind, event_team_type=side, home_score=0, away_score=0, home_skaters=5,
                away_skaters=5, empty_net=False, extra_attacker=False, x=60.0, shot_distance=30.0,
                shot_angle=10.0, secondary_type="wrist", season_type="R")
    base.update(kw)
    return base


def test_shot_context_flags():
    pbp = pd.DataFrame([
        ev(1, 100, "FACEOFF", "home", x=-60.0),
        ev(2, 103, "SHOT", "home", x=70.0),                                  # rush: came from the other end
        ev(3, 105, "SHOT", "home", x=80.0, shot_distance=8.0, shot_angle=30.0),   # rebound
        ev(4, 200, "GOAL", "away", home_score=0, away_score=1, x=-75.0, home_skaters=4),   # power play
        ev(5, 300, "MISSED_SHOT", "away", away_score=1, empty_net=True),
        ev(6, 310, "SHOT", "home", away_score=1, extra_attacker=True, home_skaters=6),
        ev(7, 3900, "GOAL", "home", period=5, period_type="SHOOTOUT"),
    ])
    s = shot_events(pbp).set_index("event_idx")
    assert 7 not in s.index                                       # shootout attempts are left out
    assert s.loc[2, "rush"] == 1 and s.loc[3, "rebound"] == 1 and s.loc[3, "rush"] == 0
    assert s.loc[4, "strength"] == "pp" and s.loc[4, "home_lead"] == 0   # score before the goal
    assert s.loc[5, "strength"] == "empty_net" and s.loc[6, "strength"] == "extra_attacker"
    assert s.loc[6, "home_lead"] == -1


def test_logistic_fit_learns_distance():
    rng = np.random.default_rng(0)
    n = 20000
    shots = pd.DataFrame({"shot_distance": rng.uniform(5, 70, n), "shot_angle": rng.uniform(0, 80, n),
                          "secondary_type": "wrist", "rebound": 0, "rush": 0, "angle_change": 0.0,
                          "strength": "ev"})
    p = 1 / (1 + np.exp(-(0.5 - 0.08 * shots["shot_distance"])))
    y = (rng.random(n) < p).astype(float)
    coef = fit_logistic(design(shots), y)
    model = ShotModel(coef, {s: 1.0 for s in range(-3, 4)}, {s: 1.0 for s in range(-3, 4)})
    near = model.xg(shots.assign(shot_distance=10.0).head(1))[0]
    far = model.xg(shots.assign(shot_distance=60.0).head(1))[0]
    assert near > 3 * far


def test_score_weights_apply_only_at_five_on_five():
    model = ShotModel(np.zeros(1 + len(FEATURES)), {s: 1.0 + 0.1 * s for s in range(-3, 4)},
                      {s: 1.0 - 0.1 * s for s in range(-3, 4)})
    shots = pd.DataFrame({"home_lead": [2, 2, -5, 1], "side": ["home", "away", "home", "home"],
                          "strength": ["ev", "ev", "ev", "pp"]})
    assert np.allclose(model.score_weight(shots), [1.2, 0.8, 0.7, 1.0])
