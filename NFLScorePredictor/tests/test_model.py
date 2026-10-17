import numpy as np
import pandas as pd

from nflpredictor.model import ScoreModel


def synthetic_features(n=1200, seed=0, market_noise=6.0, rating_noise=0.0):
    rng = np.random.default_rng(seed)
    off_h, off_a = rng.normal(0, 0.08, n), rng.normal(0, 0.08, n)
    def_h, def_a = rng.normal(0, 0.06, n), rng.normal(0, 0.06, n)
    true_home = 22 + 55 * off_h + 55 * def_a + 1.0
    true_away = 22 + 55 * off_a + 55 * def_h - 1.0
    home_score = np.maximum(0, np.rint(true_home + rng.normal(0, 9, n)))
    away_score = np.maximum(0, np.rint(true_away + rng.normal(0, 9, n)))
    return pd.DataFrame({
        "game_id": [f"g{i}" for i in range(n)], "season": 2020 + (np.arange(n) // 300),
        "completed": True, "playoff": False, "neutral": False, "div_game": 0,
        "home_rest": 7, "away_rest": 7,
        "off_home": off_h + rng.normal(0, rating_noise, n), "off_away": off_a + rng.normal(0, rating_noise, n),
        "def_home": def_h + rng.normal(0, rating_noise, n), "def_away": def_a + rng.normal(0, rating_noise, n),
        "home_qb_adj": 0.0, "away_qb_adj": 0.0, "env_points": 22.0,
        "home_score": home_score, "away_score": away_score,
        "spread_line": (true_home - true_away) + rng.normal(0, market_noise, n),
        "total_line": (true_home + true_away) + rng.normal(0, market_noise, n),
        "roof": "dome", "wind": np.nan,
    })


def test_points_map_recovers_coefficients():
    f = synthetic_features(n=4000)
    m = ScoreModel.fit(f, calibrate_scores=False)
    assert 45 < m.coef["off"] < 65
    assert 45 < m.coef["def_opp"] < 65
    assert 1.2 < m.coef["home"] < 2.8


def test_blend_trusts_the_better_source():
    noisy_market = ScoreModel.fit(synthetic_features(market_noise=12.0, rating_noise=0.05),
                                  calibrate_scores=False)
    sharp_market = ScoreModel.fit(synthetic_features(market_noise=0.5, rating_noise=0.05),
                                  calibrate_scores=False)
    assert noisy_market.margin_weight > sharp_market.margin_weight
    assert 0.0 <= sharp_market.margin_weight <= 1.0


def test_missing_lines_fall_back_to_model():
    f = synthetic_features()
    m = ScoreModel.fit(f, calibrate_scores=False)
    upcoming = f.head(3).copy()
    upcoming[["spread_line", "total_line"]] = np.nan
    means = m.means(upcoming)
    assert np.allclose(means["margin"], means["model_margin"])
    assert np.allclose(means["home"] + means["away"], means["total"])


def test_predict_and_round_trip():
    f = synthetic_features(n=600)
    m = ScoreModel.fit(f)
    pred = m.predict(f.head(4), n_sims=2000)
    assert {"home_win_prob", "headline_home", "pred_margin"} <= set(pred.columns)
    again = ScoreModel.from_dict(m.to_dict())
    assert np.allclose(again.means(f.head(4))["margin"], m.means(f.head(4))["margin"])
