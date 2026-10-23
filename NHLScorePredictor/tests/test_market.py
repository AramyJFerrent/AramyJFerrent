import numpy as np
import pandas as pd

from nhlpredictor.market import PRIOR_WEIGHT, MarketInverter, devig, fit_blend
from nhlpredictor.simulate import SimParams, over_prob, simulate


def test_devig_removes_the_margin():
    assert np.isclose(devig(-150, 130), (150 / 250) / (150 / 250 + 100 / 230))
    assert np.isclose(devig(-110, -110), 0.5)
    assert np.isnan(devig(np.nan, 120))


def test_inverter_recovers_the_rates_behind_a_line():
    params = SimParams()
    inv = MarketInverter(params, n_sims=3000)
    sim = simulate([3.3], [2.5], params, n_sims=40000, seed=5)
    p_home = float((sim["home"] > sim["away"]).mean())
    p_over = float(over_prob(sim, np.array([6.5]))[0])
    h, a = inv.invert(p_home, 6.5, p_over)
    assert abs(h - 3.3) < 0.2 and abs(a - 2.5) < 0.2
    lines = pd.DataFrame({"home_moneyline": [-160, np.nan], "away_moneyline": [140, np.nan],
                          "total_line": [6.0, np.nan], "over_price": [np.nan, np.nan],
                          "under_price": [np.nan, np.nan]})
    rates = inv.rates(lines)
    assert rates.loc[0, "market_home_rate"] > rates.loc[0, "market_away_rate"]
    assert rates.loc[1].isna().all()


def test_blend_weight_trusts_the_better_source_and_starts_at_the_prior():
    rng = np.random.default_rng(0)
    n = 3000
    true_h, true_a = rng.normal(3.0, 0.4, n), rng.normal(2.8, 0.4, n)
    gh, ga = rng.poisson(true_h), rng.poisson(true_a)
    sharp_h, sharp_a = true_h + rng.normal(0, 0.05, n), true_a + rng.normal(0, 0.05, n)
    noisy_h, noisy_a = true_h + rng.normal(0, 0.6, n), true_a + rng.normal(0, 0.6, n)
    w, games = fit_blend(noisy_h.clip(0.5), noisy_a.clip(0.5), sharp_h, sharp_a, gh, ga)
    assert games == n and w < 0.35                     # mostly the sharp market
    w0, games0 = fit_blend([], [], [], [], [], [])
    assert games0 == 0 and w0 == PRIOR_WEIGHT
