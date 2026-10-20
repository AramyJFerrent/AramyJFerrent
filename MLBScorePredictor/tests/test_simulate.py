import numpy as np
import pandas as pd
import pytest

from mlbpredictor.data import read_summary, GAMES_DIR, TRANSITION_COLUMNS
from mlbpredictor.simulate import (THETAS, MarkovChain, SimParams, headline_score, line_probs, over_prob, simulate,
                                   summarize)


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


def test_line_probs_handle_either_favorite_and_pushes():
    sim = {"home": np.array([[5, 3, 4, 2], [1, 1, 1, 1]]), "away": np.array([[2, 3, 3, 4], [0, 0, 0, 0]])}
    p = line_probs(sim, np.array([-1.5, 1.5]), np.array([7.0, np.nan]))
    # Home -1.5 covers only the 5-2 game; home +1.5 covers every 1-0 game.
    assert p.loc[0, "model_home_cover_prob"] == 0.25 and p.loc[0, "model_away_cover_prob"] == 0.75
    assert p.loc[1, "model_home_cover_prob"] == 1.0 and p.loc[1, "model_away_cover_prob"] == 0.0
    # Totals 7, 6, 7, 6 against 7: half push, half under.
    assert tuple(p.loc[0, ["model_over_prob", "model_under_prob", "model_total_push_prob"]]) == (0.0, 0.5, 0.5)
    assert p.loc[[1], ["model_over_prob", "model_under_prob", "model_total_push_prob"]].isna().all(axis=None)
    assert np.isnan(line_probs(sim, np.array([np.nan, 1.5]), np.array([7.0, 7.0])).loc[0, "model_home_cover_prob"])


def test_model_only_cover_and_over_follow_the_models_runs(params):
    # The live pipeline simulates the model's own runs (no market scaling) for the edges: more home
    # runs mean a better home cover chance at -1.5 and a higher over chance, from the same simulator.
    lo = simulate(profile(4.5), profile(4.5), np.array([0.5]), np.array([0.5]), params, n_sims=20000, seed=6)
    hi = simulate(profile(5.5), profile(4.5), np.array([0.6]), np.array([0.5]), params, n_sims=20000, seed=6)
    a, b = (line_probs(s, np.array([-1.5]), np.array([9.0])).iloc[0] for s in (lo, hi))
    assert b.model_home_cover_prob > a.model_home_cover_prob + 0.05 and b.model_over_prob > a.model_over_prob
    assert 0.03 < a.model_total_push_prob < 0.15
    assert np.isclose(a.model_home_cover_prob, summarize(lo).loc[0, "home_cover_prob"])
