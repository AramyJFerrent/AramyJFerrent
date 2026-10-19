import numpy as np
import pandas as pd

from mlbpredictor.players import RateEngine, log5, platoon_factors, season_time, stabilization


def test_season_time_skips_the_offseason():
    t = season_time(["2025-09-28", "2026-03-26", "2026-03-27"], [2025, 2026, 2026])
    assert t[2] - t[1] == 1
    assert 30 < t[1] - t[0] < 90          # an offseason counts as a month or two


def test_rate_engine_decays_and_only_looks_back():
    eng = RateEngine(["a", "a", "b"], [10, 20, 15], [4, 4, 5], np.array([[1.0], [2.0], [3.0]]), half_life=10.0)
    s = eng.sums(["a", "a", "a", "b", "c"], [10, 21, 30, 16, 50])
    assert s[0].tolist() == [0.0, 0.0]                         # nothing before the first game
    assert np.allclose(s[1], [4 * 0.5 ** 1.1 + 4 * 0.5 ** 0.1, 1 * 0.5 ** 1.1 + 2 * 0.5 ** 0.1])
    assert np.allclose(s[2], s[1] * 0.5 ** 0.9)
    assert np.allclose(s[3], [5 * 0.5 ** 0.1, 3 * 0.5 ** 0.1]) and s[4].tolist() == [0.0, 0.0]


def test_log5_normalizes_and_combines():
    league = np.array([[0.22, 0.08, 0.01, 0.14, 0.045, 0.004, 0.03]])
    p = log5(league, league, league)
    assert np.isclose(p.sum(), 1.0) and np.allclose(p[0, :7], league[0], atol=1e-9)
    strikeout_pitcher = league.copy()
    strikeout_pitcher[0, 0] = 0.32
    assert log5(league, strikeout_pitcher, league)[0, 0] > 0.3


def test_platoon_factors_favor_the_opposite_hand():
    rows = []
    for bats, throws, hr in (("L", "R", 40), ("L", "L", 20), ("R", "L", 40), ("R", "R", 30)):
        rows += [(bats, throws, "hr", hr), (bats, throws, "out", 1000 - hr)]
    f = platoon_factors(pd.DataFrame(rows, columns=["bats", "throws", "event", "n"]))
    hr = 6
    assert f[("L", "R")][hr] > 1 > f[("L", "L")][hr]


def test_stabilization_grows_with_noise():
    rng = np.random.default_rng(0)
    rows = []
    for i in range(400):
        talent = rng.normal(0.22, 0.04)
        n = 600
        counts = rng.multinomial(n, [talent, 0.08, 0.01, 0.14, 0.045, 0.004, 0.03, 1 - talent - 0.309])
        rows.append({"season": 2020, "player_id": str(i), "pa": n, **dict(zip(["k", "bb", "hbp", "s", "d", "t", "hr"], counts[:7]))})
    k = stabilization(pd.DataFrame(rows), "pa")
    assert 70 < k[0] < 150 and k[5] > 1000      # strikeouts settle fast, triples are mostly noise
