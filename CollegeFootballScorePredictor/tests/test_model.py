import numpy as np
import pandas as pd

from cfbpredictor.elo import run_elo
from cfbpredictor.model import ScoreModel


def synthetic_features(n=1600, seed=0, market_noise=6.0, rating_noise=0.0):
    rng = np.random.default_rng(seed)
    off_h, off_a = rng.normal(0, 0.12, n), rng.normal(0, 0.12, n)
    def_h, def_a = rng.normal(0, 0.10, n), rng.normal(0, 0.10, n)
    pace = rng.normal(0, 4, n)
    true_home = 27 + 60 * off_h + 60 * def_a + 1.5 + 0.3 * pace
    true_away = 27 + 60 * off_a + 60 * def_h - 1.5 + 0.3 * pace
    home_score = np.maximum(0, np.rint(true_home + rng.normal(0, 11, n)))
    away_score = np.maximum(0, np.rint(true_away + rng.normal(0, 11, n)))
    return pd.DataFrame({
        "game_id": np.arange(n), "season": 2020 + (np.arange(n) // 400),
        "completed": True, "neutral": False, "conference_game": False,
        "home_division": "fbs", "away_division": "fbs",
        "off_st_home": 0.0, "off_st_away": 0.0, "def_st_home": 0.0, "def_st_away": 0.0,
        "off_pace_home": pace / 2, "off_pace_away": pace / 2, "def_pace_home": pace / 2, "def_pace_away": pace / 2,
        "off_home": off_h + rng.normal(0, rating_noise, n), "off_away": off_a + rng.normal(0, rating_noise, n),
        "def_home": def_h + rng.normal(0, rating_noise, n), "def_away": def_a + rng.normal(0, rating_noise, n),
        "elo_spread": 0.0, "env_points": 27.0,
        "home_score": home_score, "away_score": away_score,
        "spread_line": (true_home - true_away) + rng.normal(0, market_noise, n),
        "total_line": (true_home + true_away) + rng.normal(0, market_noise, n),
    })


def test_points_maps_recover_coefficients():
    m = ScoreModel.fit(synthetic_features(n=6000), calibrate_scores=False)
    assert 50 < m.coef["off"] < 70 and 50 < m.coef["def_opp"] < 70
    assert 2.0 < m.coef["home"] < 4.0
    assert 50 < m.total_coef["off"] < 70
    assert 0.3 < m.total_coef["pace"] < 0.9


def test_blend_trusts_the_better_source():
    noisy = ScoreModel.fit(synthetic_features(market_noise=14.0, rating_noise=0.05), calibrate_scores=False)
    sharp = ScoreModel.fit(synthetic_features(market_noise=0.5, rating_noise=0.05), calibrate_scores=False)
    assert noisy.margin_weight > sharp.margin_weight
    assert 0.0 <= sharp.margin_weight <= 1.0


def test_missing_lines_fall_back_to_model():
    f = synthetic_features()
    m = ScoreModel.fit(f, calibrate_scores=False)
    upcoming = f.head(3).copy()
    upcoming[["spread_line", "total_line"]] = np.nan
    means = m.means(upcoming)
    assert np.allclose(means["margin"], means["model_margin"])
    assert np.allclose(means["home"] + means["away"], means["total"])
    assert (means["away"] > 0).all() and (means["home"] > 0).all()


def test_predict_and_round_trip():
    f = synthetic_features(n=800)
    m = ScoreModel.fit(f)
    pred = m.predict(f.head(4), n_sims=2000)
    assert {"home_win_prob", "headline_home", "pred_margin"} <= set(pred.columns)
    assert np.allclose(pred["home_win_prob"] + pred["away_win_prob"], 1.0)
    again = ScoreModel.from_dict(m.to_dict())
    assert np.allclose(again.means(f.head(4))["margin"], m.means(f.head(4))["margin"])


def test_elo_winner_gains_and_fcs_starts_lower():
    g = pd.DataFrame([
        dict(game_id=1, season=2020, week=1, kickoff=pd.Timestamp("2020-09-05", tz="UTC"), home_team="A",
             away_team="B", home_division="fbs", away_division="fbs", home_score=35, away_score=10,
             neutral=False, completed=True),
        dict(game_id=2, season=2020, week=2, kickoff=pd.Timestamp("2020-09-12", tz="UTC"), home_team="B",
             away_team="C", home_division="fbs", away_division="fcs", home_score=np.nan, away_score=np.nan,
             neutral=True, completed=False),
    ])
    frame, ratings = run_elo(g)
    assert ratings["A"] > ratings["B"] > ratings["C"]
    assert frame.set_index("game_id").loc[2, "elo_spread"] > 10       # FBS over FCS on a neutral field
