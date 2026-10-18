import numpy as np
import pandas as pd

from nhlpredictor.model import GoalModel, fit_poisson


def synthetic_features(n=3000, seed=0):
    rng = np.random.default_rng(seed)
    f = pd.DataFrame({
        "game_id": np.arange(n), "season": 2020 + np.arange(n) // 1000, "completed": True,
        "playoff": False, "neutral": False, "env_goals": 2.8, "home_rest": 2.0, "away_rest": 2.0,
    })
    for side in ("home", "away"):
        for name in ("ev", "pp", "draw", "goals"):
            f[f"off_{name}_{side}"] = rng.normal(0, 0.2, n)
            f[f"def_{name}_{side}"] = rng.normal(0, 0.2, n)
        f[f"{side}_goalie_value"] = rng.normal(0, 0.3, n)
        f[f"{side}_goalie_adj"] = 0.0
    f["elo_edge"] = rng.normal(0, 0.3, n)
    lam_h = 2.8 * np.exp(0.04 + 0.5 * f["off_ev_home"] + 0.5 * f["def_ev_away"])
    lam_a = 2.8 * np.exp(-0.04 + 0.5 * f["off_ev_away"] + 0.5 * f["def_ev_home"])
    f["home_reg"] = rng.poisson(lam_h)
    f["away_reg"] = rng.poisson(lam_a)
    f["periods"] = np.where(f["home_reg"] == f["away_reg"], 4, 3)
    return f


def test_poisson_regression_recovers_coefficients():
    rng = np.random.default_rng(1)
    X = np.column_stack([np.ones(20000), rng.normal(size=20000)])
    y = rng.poisson(np.exp(0.3 + 0.4 * X[:, 1]))
    beta = fit_poisson(X, y, np.zeros(20000), ridge=0.0)
    assert np.allclose(beta, [0.3, 0.4], atol=0.03)


def test_goal_model_learns_ratings_and_home_ice():
    m = GoalModel.fit(synthetic_features(), calibrate_sim=False)
    assert 0.4 < m.coef["ev_off"] < 0.6 and 0.4 < m.coef["ev_def"] < 0.6
    assert 0.03 < m.coef["home"] < 0.13          # +0.04 / -0.04 per side, coded as +-0.5
    assert abs(m.coef["elo"]) < 0.1 and abs(m.coef["goals_off"]) < 0.1


def test_predict_and_round_trip():
    f = synthetic_features(n=600)
    m = GoalModel.fit(f, calibrate_sim=False)
    pred, sim = m.predict(f.head(4), n_sims=2000)
    assert {"home_win_prob", "headline_home", "ot_prob", "home_rate"} <= set(pred.columns)
    assert np.allclose(pred["home_win_prob"] + pred["away_win_prob"], 1.0)
    again = GoalModel.from_dict(m.to_dict())
    assert np.allclose(again.rates(f.head(4))["home"], m.rates(f.head(4))["home"])
