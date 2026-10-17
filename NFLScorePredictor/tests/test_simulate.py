import numpy as np

from nflpredictor.simulate import (
    ScoringModel, calibrate, fit_margin_weights, headline_score, simulate, summarize,
)


def test_simulated_means_match_expected_points():
    model = ScoringModel()
    home, away = simulate([27.0, 17.0], [20.0, 24.0], model, n_sims=60000, seed=3)
    assert abs(home[0].mean() - 27.0) < 0.4
    assert abs(away[0].mean() - 20.0) < 0.4
    assert abs(home[1].mean() - 17.0) < 0.4
    assert abs(away[1].mean() - 24.0) < 0.4


def test_scores_are_real_football_scores():
    home, away = simulate([23.0], [20.0], ScoringModel(), n_sims=20000, seed=1)
    assert (home >= 0).all() and (away >= 0).all()
    # A team can never finish with exactly 1 point.
    assert not (home == 1).any() and not (away == 1).any()


def test_playoff_games_never_end_tied():
    home, away = simulate([21.0], [21.0], ScoringModel(), n_sims=20000, playoff=True, seed=2)
    assert not (home == away).any()


def test_regular_season_ties_are_rare_but_possible():
    home, away = simulate([21.0], [21.0], ScoringModel(), n_sims=200000, seed=2)
    tie_rate = np.mean(home == away)
    assert 0.0005 < tie_rate < 0.01


def test_calibration_hits_target_spread():
    model = calibrate(ScoringModel(), target_margin_sd=12.7, target_total_sd=13.2)
    home, away = simulate([22.5], [22.5], model, n_sims=60000, seed=5)
    assert abs(np.std(home - away) - 12.7) < 0.6
    assert abs(np.std(home + away) - 13.2) < 0.8


def test_margin_weights_reproduce_key_numbers():
    rng = np.random.default_rng(0)
    n = 1500
    home_mean = rng.normal(23.5, 3, n)
    away_mean = rng.normal(21.0, 3, n)
    # Synthetic history where 3-point finishes are twice as common as the raw sim gives.
    base = ScoringModel()
    h, a = simulate(home_mean, away_mean, base, n_sims=1, seed=11)
    margins = (h - a)[:, 0]
    flip = rng.random(n) < 0.08
    margins = np.where(flip, 3 * np.sign(rng.normal(size=n)), margins)
    fitted = fit_margin_weights(base, home_mean, away_mean, margins, n_sims=400)
    assert fitted.margin_weights[3] > 1.2
    hs, as_ = simulate([23.5], [21.0], fitted, n_sims=40000, seed=4)
    w = fitted.weights(hs, as_)
    weighted_three = (w * (np.abs(hs - as_) == 3)).sum() / w.sum()
    raw_three = np.mean(np.abs(hs - as_) == 3)
    assert weighted_three > raw_three


def test_headline_score_picks_the_favorite():
    home, away = simulate([20.0], [27.0], ScoringModel(), n_sims=20000, seed=9)
    h, a = headline_score(home[0], away[0], 20.0, 27.0)
    assert a > h
    assert abs((h - a) - (20.0 - 27.0)) <= 4


def test_summary_probabilities_are_consistent():
    model = ScoringModel()
    home, away = simulate([24.0], [20.0], model, n_sims=20000, seed=8)
    s = summarize(home, away, [24.0], [20.0], model).iloc[0]
    assert abs(s.home_win_prob + s.away_win_prob + s.tie_prob - 1) < 1e-9
    assert s.home_win_prob > 0.55
    assert s.home_low < 24 < s.home_high
    assert s.away_low < 20 < s.away_high


def test_scoring_model_round_trips():
    model = ScoringModel(chances=9.5, margin_weights={3: 1.7, 7: 1.3})
    again = ScoringModel.from_dict(model.to_dict())
    assert again.chances == 9.5
    assert again.margin_weights[3] == 1.7
    assert again.ot_margins == model.ot_margins
