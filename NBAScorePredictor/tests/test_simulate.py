import numpy as np

from nbapredictor.simulate import (SimParams, cover_prob, fit_margin_weights, headline_score, over_prob, simulate,
                                   spread_params, summarize)


def test_spread_params_invert_margin_and_total_spreads():
    sd, rho = spread_params(13.1, 17.9)
    assert abs(sd - 11.09) < 0.05 and abs(rho - 0.30) < 0.01
    sim = simulate([112.0], [110.0], SimParams(sd=sd, rho=rho, ref_total=222.0), n_sims=200000, seed=3)
    reg = sim.periods == 4
    margin = (sim.home - sim.away)[reg]
    total = (sim.home + sim.away)[reg]
    assert abs(np.std(margin) - 13.1) < 0.3 and abs(np.std(total) - 17.9) < 0.3
    assert abs(margin.mean() - 2.0) < 0.2


def test_every_game_gets_a_winner_and_overtime_adds_points():
    sim = simulate([105.0, 115.0], [105.0, 100.0], SimParams(), n_sims=50000, seed=1)
    assert (sim.home != sim.away).all()
    ot = sim.periods > 4
    assert 0.02 < ot[0].mean() < 0.05                       # a smooth normal ties about 3% of the time
    assert ot[1].mean() < ot[0].mean()                      # less often when one team is much better
    reg_total = (sim.home + sim.away)[0][~ot[0]].mean()
    assert (sim.home + sim.away)[0][ot[0]].mean() > reg_total


def test_margin_weights_reproduce_the_extra_ties():
    rng = np.random.default_rng(0)
    n = 4000
    home = rng.normal(112, 4, n)
    away = rng.normal(109, 4, n)
    base = SimParams(sd=11.0, rho=0.3, ref_total=221.0)
    # History where ties after regulation happen twice as often as the smooth model says,
    # taken out of one- and two-point margins.
    sim = simulate(home, away, base, n_sims=1, seed=5)
    actual = sim.reg_margin[:, 0].copy()
    close = np.abs(actual) <= 2
    flip = close & (rng.random(n) < 0.35)
    actual[flip] = 0
    fitted = fit_margin_weights(base, home, away, actual, n_sims=400)
    assert fitted.margin_weights[0] > 1.4 and fitted.margin_weights[1] < 0.95
    s0 = summarize(simulate(home[:200], away[:200], base, n_sims=4000, seed=2))
    s1 = summarize(simulate(home[:200], away[:200], fitted, n_sims=4000, seed=2))
    assert s1["ot_prob"].mean() > 1.3 * s0["ot_prob"].mean()


def test_summary_ranges_and_line_probabilities():
    sim = simulate([115.0], [108.0], SimParams(), n_sims=40000, seed=9)
    s = summarize(sim).iloc[0]
    assert s.home_win_prob > 0.65 and abs(s.home_win_prob + s.away_win_prob - 1) < 1e-9
    assert s.home_low < 115 < s.home_high and s.home_high - s.home_low > 20
    assert (s.headline_home, s.headline_away) == headline_score(s.sim_home, s.sim_away)
    assert abs(cover_prob(sim, np.array([7.0]))[0] - 0.5) < 0.04
    assert over_prob(sim, np.array([200.0]))[0] > 0.9
    assert headline_score(110.2, 110.4) == (110, 111)        # never a tied final score
