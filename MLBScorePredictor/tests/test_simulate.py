import numpy as np
import pandas as pd
import pytest

from mlbpredictor.data import read_summary, GAMES_DIR, TRANSITION_COLUMNS
from mlbpredictor.simulate import THETAS, MarkovChain, SimParams, headline_score, over_prob, simulate, summarize


@pytest.fixture(scope="module")
def chain():
    return MarkovChain(read_summary(GAMES_DIR / "2025_transitions.csv.gz", TRANSITION_COLUMNS))


@pytest.fixture(scope="module")
def params(chain):
    return SimParams(tables=chain.tables(), frailty=30.0)


def test_chain_reproduces_real_innings(chain):
    t = chain.tables()
    i = int(np.argmin(np.abs(THETAS - 1.0)))
    assert np.allclose(t["empty"].sum(axis=1), 1.0)
    assert 0.45 < t["mean"][i] < 0.55 and 0.70 < t["empty"][i][0] < 0.75   # about half a run, 72% scoreless
    assert t["ghost_mean"][i] > 2 * t["mean"][i]                              # runner on second to start
    assert np.all(np.diff(t["mean"]) > 0)                                     # more offense, more runs
    lw = chain.linear_weights()
    assert lw["hr"] > lw["t"] > lw["d"] > lw["s"] > lw["bb"] > 0 > lw["k"]
    assert chain.run_expectancy()[0] == pytest.approx(t["mean"][i], abs=0.01)


def profile(total):
    return np.full((1, 9), total / 9.0)


def test_games_have_a_winner_and_a_real_structure(params):
    sim = simulate(profile(4.6), profile(4.4), np.array([0.5]), np.array([0.5]), params, n_sims=20000, seed=1)
    h, a = sim["home"][0], sim["away"][0]
    assert not (h == a).any()
    # The home team skips the bottom of the ninth only when it leads after the top.
    skipped = ~sim["home_batted_last"][0]
    assert (h[skipped] > a[skipped]).all() and 0.35 < skipped.mean() < 0.55
    # Extra innings only from a tie, and walk-offs win by exactly one unless they are home runs.
    extra = sim["innings"][0] > 9
    assert 0.05 < extra.mean() < 0.14
    wo = sim["walkoff"][0]
    assert (h[wo] > a[wo]).all() and np.mean((h - a)[wo] == 1) > 0.6
    assert 0.03 < np.mean(a == 0) < 0.10


def test_runner_on_second_shortens_extra_innings(params):
    ghost = simulate(profile(4.5), profile(4.5), np.array([0.5]), np.array([0.5]), params, n_sims=30000,
                     ghost=True, seed=2)
    plain = simulate(profile(4.5), profile(4.5), np.array([0.5]), np.array([0.5]), params, n_sims=30000,
                     ghost=False, seed=2)
    long_g = (ghost["innings"][0] > 11).mean() / max((ghost["innings"][0] > 9).mean(), 1e-9)
    long_p = (plain["innings"][0] > 11).mean() / max((plain["innings"][0] > 9).mean(), 1e-9)
    assert long_g < long_p


def test_seven_inning_games(params):
    sim = simulate(profile(4.5), profile(4.5), np.array([0.5]), np.array([0.5]), params, n_sims=5000,
                   sched_innings=7, seed=3)
    assert sim["innings"][0].min() >= 7 and np.median(sim["innings"][0]) == 7


def test_summary_headline_and_totals(params):
    sim = simulate(profile(5.5), profile(3.5), np.array([0.6]), np.array([0.4]), params, n_sims=20000, seed=4)
    s = summarize(sim).iloc[0]
    assert s.home_win_prob > 0.6 and abs(s.home_win_prob + s.away_win_prob - 1) < 1e-9
    assert s.headline_home > s.headline_away and s.home_low <= 5 <= s.home_high
    assert 0 < s.home_cover_prob < s.home_win_prob and 0 < s.extra_prob < 0.15
    assert 4.0 < s.f5_total < 6.0
    h, a = headline_score(sim["home"][0], sim["away"][0], home_wins=False)
    assert a > h
    p = over_prob(sim, np.array([8.5]))[0]
    assert 0.35 < p < 0.65
