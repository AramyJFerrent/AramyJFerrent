import numpy as np
import pandas as pd

from nflpredictor.config import Hyperparams
from nflpredictor.ratings import Ratings, RatingsEngine, fit


def synthetic_rows(n_weeks=10, seed=0):
    """Round-robin games where team strength is known."""
    rng = np.random.default_rng(seed)
    teams = [f"T{i}" for i in range(8)]
    off = dict(zip(teams, np.linspace(-0.15, 0.15, 8)))
    deff = dict(zip(teams, np.linspace(0.1, -0.1, 8)))
    rows = []
    for week in range(1, n_weeks + 1):
        order = rng.permutation(teams)
        for a, b in zip(order[::2], order[1::2]):
            for team, opp, h in ((a, b, 1.0), (b, a, -1.0)):
                y = 0.0 + off[team] + deff[opp] + 0.02 * h + rng.normal(0, 0.12)
                rows.append({"game_id": f"{week}_{a}_{b}", "season": 2020, "week": week,
                             "team": team, "opp": opp, "h": h, "y": y, "w": 60.0})
    return pd.DataFrame(rows), off, deff


def test_ridge_recovers_team_strength():
    rows, off, deff = synthetic_rows(n_weeks=16)
    r = fit(rows, ref_week=17, prior=Ratings(), hp=Hyperparams(half_life_weeks=1000))
    teams = sorted(off)
    est_off = [r.off[t] for t in teams]
    est_def = [r.deff[t] for t in teams]
    assert np.corrcoef(est_off, [off[t] for t in teams])[0, 1] > 0.9
    assert np.corrcoef(est_def, [deff[t] for t in teams])[0, 1] > 0.8


def test_no_games_returns_the_prior():
    prior = Ratings(off={"A": 0.1, "B": -0.1}, deff={"A": 0.0, "B": 0.05}, mu=0.01, hfa=0.02)
    r = fit(pd.DataFrame(columns=["team", "opp", "week", "h", "y", "w"]), 1, prior, Hyperparams())
    assert r.off == prior.off and r.deff == prior.deff


def test_prior_dominates_early_and_fades():
    rows, off, _ = synthetic_rows(n_weeks=16)
    prior = Ratings(off={t: 0.0 for t in off}, deff={t: 0.0 for t in off})
    hp = Hyperparams()
    early = fit(rows[rows.week <= 1], 2, prior, hp)
    late = fit(rows, 17, prior, hp)
    spread_early = np.std(list(early.off.values()))
    spread_late = np.std(list(late.off.values()))
    assert spread_early < spread_late


def test_engine_chains_preseason_priors():
    rows, off, _ = synthetic_rows(n_weeks=16)
    second = rows.assign(season=2021)
    engine = RatingsEngine(pd.concat([rows, second]), Hyperparams())
    prior = engine.prior(2021)
    final = engine.final(2020)
    best = max(off, key=off.get)
    assert prior.off[best] == final.off[best] * Hyperparams().off_carryover
    week1 = engine.before(2021, 1)
    assert week1.off[best] == prior.off[best]
