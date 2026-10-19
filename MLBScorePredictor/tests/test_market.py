import numpy as np
import pandas as pd

from mlbpredictor.data import GAMES_DIR, TRANSITION_COLUMNS, read_summary
from mlbpredictor.market import MarketInverter, blend, devig, fit_blend
from mlbpredictor.simulate import MarkovChain, SimParams, over_prob, simulate


def test_devig_removes_the_margin():
    assert np.isclose(devig(-150, 130), (150 / 250) / (150 / 250 + 100 / 230))
    assert np.isclose(devig(-110, -110), 0.5)
    assert np.isnan(devig(np.nan, 120))


def test_inverter_recovers_the_runs_behind_a_line():
    chain = MarkovChain(read_summary(GAMES_DIR / "2025_transitions.csv.gz", TRANSITION_COLUMNS))
    params = SimParams(tables=chain.tables(), frailty=30.0)
    profile = np.ones(9)
    inv = MarketInverter(params, profile, n_sims=3000)
    sim = simulate(np.full((1, 9), 5.2 / 9), np.full((1, 9), 4.0 / 9), np.array([5.2 / 9]), np.array([4.0 / 9]),
                   params, n_sims=40000, seed=5)
    p_home = float((sim["home"] > sim["away"]).mean())
    p_over = float(over_prob(sim, np.array([8.5]))[0])
    h, a = inv.invert(p_home, 8.5, p_over)
    assert abs(h - 5.2) < 0.3 and abs(a - 4.0) < 0.3
    lines = pd.DataFrame({"home_moneyline": [-160, np.nan], "away_moneyline": [140, np.nan],
                          "total_line": [8.5, np.nan], "over_price": [np.nan, np.nan], "under_price": [np.nan, np.nan]})
    rates = inv.rates(lines)
    assert rates.loc[0, "market_home_runs"] > rates.loc[0, "market_away_runs"]
    assert rates.loc[1, ["market_home_runs", "market_away_runs"]].isna().all()


def test_blend_is_log_scale_and_falls_back_to_the_model():
    out = blend(np.array([4.0, 4.0]), np.array([9.0, np.nan]), 0.5)
    assert np.isclose(out[0], 6.0) and out[1] == 4.0


def test_blend_weight_trusts_the_better_source():
    rng = np.random.default_rng(0)
    n = 4000
    true_h, true_a = rng.normal(4.5, 0.6, n).clip(2), rng.normal(4.3, 0.6, n).clip(2)
    rh, ra = rng.poisson(true_h * 8 / 9), rng.poisson(true_a * 8 / 9)
    sharp_h, sharp_a = true_h * np.exp(rng.normal(0, 0.03, n)), true_a * np.exp(rng.normal(0, 0.03, n))
    noisy_h, noisy_a = true_h * np.exp(rng.normal(0, 0.25, n)), true_a * np.exp(rng.normal(0, 0.25, n))
    raw, shrunk, games = fit_blend(noisy_h, noisy_a, sharp_h, sharp_a, rh, ra, prior=0.3)
    assert games == n and raw < 0.3 and shrunk < 0.3
    nan, prior, none = fit_blend([], [], [], [], [], [], prior=0.3)
    assert none == 0 and prior == 0.3
