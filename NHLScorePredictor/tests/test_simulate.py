import numpy as np

from nhlpredictor.simulate import SimParams, calibrate, headline_score, over_prob, simulate, summarize


def test_both_goalies_in_goals_match_the_rates():
    sim = simulate([3.2, 2.4], [2.6, 3.0], SimParams(gamma=0.0), n_sims=40000, seed=3)
    assert abs(sim["even_home"][0].mean() - 3.2) < 0.08
    assert abs(sim["even_away"][1].mean() - 3.0) < 0.08


def test_every_game_has_a_winner_and_shootouts_add_one_goal():
    sim = simulate([2.8], [2.8], SimParams(), n_sims=20000, seed=1)
    assert not (sim["home"] == sim["away"]).any()
    so = sim["ended"][0] == 2
    assert so.any()
    margin = np.abs(sim["home"][0] - sim["away"][0])
    assert (margin[sim["ended"][0] > 0] == 1).all()
    assert (sim["reg_home"][0][so] == sim["reg_away"][0][so]).all()


def test_playoff_overtime_never_reaches_a_shootout():
    sim = simulate([2.8], [2.8], SimParams(), n_sims=20000, playoff=True, seed=2)
    assert not (sim["ended"] == 2).any() and (sim["ended"] == 1).any()


def test_pulled_goalies_produce_empty_net_goals_and_fewer_one_goal_finishes():
    pulls = simulate([2.8], [2.8], SimParams(), n_sims=40000, seed=4)
    never = simulate([2.8], [2.8], SimParams(pull={1: [0.0] * 6, 2: [0.0] * 6, 3: [0.0] * 6}),
                     n_sims=40000, seed=4)
    assert pulls["empty_net"].mean() > 0.15 and not never["empty_net"].any()
    def share(s, k):
        return np.mean(np.abs(s["reg_home"] - s["reg_away"]) == k)
    assert share(pulls, 1) < share(never, 1) and share(pulls, 3) > share(never, 3)


def test_late_ties_are_stickier_with_score_effects():
    flat = simulate([2.8], [2.8], SimParams(gamma=0.0), n_sims=40000, seed=5)
    sticky = SimParams(state_mult={"early": {"tie": 0.95, "lead": 1.0, "trail": 1.05},
                                   "third": {"tie": 0.85, "lead": 0.95, "trail": 1.0},
                                   "late": {"tie": 0.8, "lead": 1.0, "trail": 0.95}}, gamma=2.0)
    tied = simulate([2.8], [2.8], sticky, n_sims=40000, seed=5)
    assert (tied["reg_home"] == tied["reg_away"]).mean() > (flat["reg_home"] == flat["reg_away"]).mean()


def test_calibration_hits_the_tie_rate_and_keeps_the_rates():
    params = SimParams(state_mult={"early": {"tie": 0.95, "lead": 1.0, "trail": 1.05},
                                   "third": {"tie": 0.9, "lead": 0.95, "trail": 1.0},
                                   "late": {"tie": 0.85, "lead": 1.0, "trail": 0.95}})
    rng = np.random.default_rng(0)
    h, a = rng.normal(2.8, 0.3, 800), rng.normal(2.6, 0.3, 800)
    fitted = calibrate(params, h, a, tie_rate=0.21, n_sims=200, max_games=800)
    sim = simulate(h, a, fitted, n_sims=200, seed=9)
    assert abs((sim["reg_home"] == sim["reg_away"]).mean() - 0.21) < 0.02
    assert abs((sim["even_home"] + sim["even_away"]).mean() - (h + a).mean()) < 0.1


def test_summary_and_headline():
    sim = simulate([3.4], [2.3], SimParams(), n_sims=20000, seed=8)
    s = summarize(sim).iloc[0]
    assert s.home_win_prob > 0.6 and abs(s.home_win_prob + s.away_win_prob - 1) < 1e-9
    assert s.home_reg_win_prob + s.away_reg_win_prob + s.ot_prob == 1.0 or \
        abs(s.home_reg_win_prob + s.away_reg_win_prob + s.ot_prob - 1) < 1e-9
    assert s.headline_home > s.headline_away
    assert s.home_low <= 3 <= s.home_high
    assert 0 < s.home_cover_prob < s.home_win_prob
    h, a = headline_score(sim["home"][0], sim["away"][0], home_wins=False)
    assert a > h
    p = over_prob(sim, np.array([5.5]))[0]
    assert 0.3 < p < 0.8


def test_params_round_trip():
    params = SimParams(gamma=2.0, pull={1: [0, 0, 0.1, 0.3, 0.7, 0.9], 2: [0.1] * 6, 3: [0.0] * 6})
    again = SimParams.from_dict(params.to_dict())
    assert again.gamma == 2.0 and again.pull[1][5] == 0.9
