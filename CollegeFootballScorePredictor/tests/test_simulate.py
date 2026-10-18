import numpy as np

from cfbpredictor.simulate import (
    OT_MARGINS, ScoringModel, calibrate, fit_margin_weights, headline_score, simulate, summarize,
)


def test_simulated_means_match_expected_points():
    home, away = simulate([34.0, 17.0], [20.0, 31.0], ScoringModel(), n_sims=60000, seed=3)
    assert abs(home[0].mean() - 34.0) < 0.5
    assert abs(away[0].mean() - 20.0) < 0.5
    assert abs(home[1].mean() - 17.0) < 0.5
    assert abs(away[1].mean() - 31.0) < 0.5


def test_scores_are_real_football_scores():
    home, away = simulate([28.0], [24.0], ScoringModel(), n_sims=20000, seed=1)
    assert (home >= 0).all() and (away >= 0).all()
    assert not (home == 1).any() and not (away == 1).any()


def test_college_games_never_end_tied():
    home, away = simulate([27.0], [27.0], ScoringModel(), n_sims=50000, seed=2)
    assert not (home == away).any()
    # Overtime adds a small set of margins; the most common is a field goal.
    margins = np.abs(home - away)
    assert set(OT_MARGINS) <= set(np.unique(margins))


def test_mismatches_produce_blowouts():
    home, away = simulate([52.0], [10.0], ScoringModel(), n_sims=20000, seed=4)
    assert np.mean(home - away >= 28) > 0.5
    assert np.mean(home > away) > 0.95


def test_high_scoring_games_are_more_volatile():
    m = ScoringModel()
    lo_h, lo_a = simulate([20.0], [20.0], m, n_sims=40000, seed=6)
    hi_h, hi_a = simulate([38.0], [38.0], m, n_sims=40000, seed=6)
    assert np.std(hi_h + hi_a) > np.std(lo_h + lo_a)


def test_calibration_hits_target_spread():
    model = calibrate(ScoringModel(), target_margin_sd=15.9, target_total_sd=16.5)
    home, away = simulate([27.0], [27.0], model, n_sims=60000, seed=5)
    assert abs(np.std(home - away) - 15.9) < 0.8
    assert abs(np.std(home + away) - 16.5) < 1.0


def test_margin_weights_reproduce_key_numbers():
    rng = np.random.default_rng(0)
    n = 1500
    home_mean, away_mean = rng.normal(30, 6, n), rng.normal(24, 6, n)
    base = ScoringModel()
    h, a = simulate(home_mean, away_mean, base, n_sims=1, seed=11)
    margins = (h - a)[:, 0]
    flip = rng.random(n) < 0.08
    margins = np.where(flip, 7 * np.sign(rng.normal(size=n)), margins)
    fitted = fit_margin_weights(base, home_mean, away_mean, margins, n_sims=400)
    assert fitted.margin_weights[7] > 1.2


def test_headline_and_summary():
    model = ScoringModel()
    home, away = simulate([20.0], [31.0], model, n_sims=20000, seed=9)
    h, a = headline_score(home[0], away[0], 20.0, 31.0)
    assert a > h and abs((h - a) - (20.0 - 31.0)) <= 5
    s = summarize(home, away, [20.0], [31.0], model).iloc[0]
    assert abs(s.home_win_prob + s.away_win_prob - 1) < 1e-9
    assert s.away_win_prob > 0.6
    assert s.away_low < 31 < s.away_high


def test_scoring_model_round_trips():
    model = ScoringModel(chances=12.5, margin_weights={3: 1.4, 7: 1.2})
    again = ScoringModel.from_dict(model.to_dict())
    assert again.chances == 12.5 and again.margin_weights[3] == 1.4
    assert again.ot_margins == model.ot_margins
