import numpy as np
import pandas as pd

from nhlpredictor.config import Hyperparams
from nhlpredictor.ratings import Ratings, RatingsEngine, SeasonSums, targets

EV = targets(Hyperparams())["ev"]


def synthetic_rows(n_days=120, seed=0, season=2020):
    """Round-robin games where team strength is known (xG per 60 at 5-on-5)."""
    rng = np.random.default_rng(seed)
    teams = [f"T{i}" for i in range(8)]
    off = dict(zip(teams, np.linspace(-0.4, 0.4, 8)))
    deff = dict(zip(teams, np.linspace(0.3, -0.3, 8)))
    rows = []
    for day in range(70, 70 + n_days, 2):
        order = rng.permutation(teams)
        for a, b in zip(order[::2], order[1::2]):
            for team, opp, h in ((a, b, 1.0), (b, a, -1.0)):
                y = 2.5 + off[team] + deff[opp] + 0.05 * h + rng.normal(0, 0.8)
                rows.append({"game_id": f"{day}_{a}_{b}", "season": season, "day": day,
                             "team": team, "opp": opp, "h": h, "y": y, "w": 48.0})
    return pd.DataFrame(rows), off, deff


def fit_direct(rows, day, prior, target, half_life):
    """Plain weighted ridge, to check the running sums against."""
    teams = sorted(set(rows["team"]) | set(rows["opp"]))
    idx = {t: i for i, t in enumerate(teams)}
    n = len(teams)
    use = rows[rows["day"] < day]
    X = np.zeros((len(use), 2 + 2 * n))
    X[:, 0] = 1.0
    X[:, 1] = use["h"]
    X[np.arange(len(use)), 2 + use["team"].map(idx).to_numpy()] = 1.0
    X[np.arange(len(use)), 2 + n + use["opp"].map(idx).to_numpy()] = 1.0
    w = use["w"].to_numpy() * 0.5 ** ((day - use["day"].to_numpy()) / half_life)
    lam = np.concatenate([[target.league_prior, target.home_prior], np.full(2 * n, target.prior)])
    beta0 = np.concatenate([[prior.mu, prior.hfa], np.zeros(2 * n)])
    beta = np.linalg.solve(np.diag(lam) + (X * w[:, None]).T @ X, lam * beta0 + (X * w[:, None]).T @ use["y"])
    return {t: beta[2 + i] for t, i in idx.items()}


def test_running_sums_match_a_direct_fit():
    rows, off, _ = synthetic_rows()
    sums = SeasonSums(rows, sorted(off), half_life=30.0)
    prior = Ratings(mu=2.5)
    for day in (75, 120, 200):
        fast = sums.solve(day, prior, EV)
        slow = fit_direct(rows, day, prior, EV, 30.0)
        assert np.allclose([fast.off[t] for t in sorted(off)], [slow[t] for t in sorted(off)])


def test_ridge_recovers_team_strength():
    rows, off, deff = synthetic_rows(n_days=180)
    r = SeasonSums(rows, sorted(off), half_life=10000.0).solve(300, Ratings(mu=2.5), EV)
    teams = sorted(off)
    assert np.corrcoef([r.off[t] for t in teams], [off[t] for t in teams])[0, 1] > 0.9
    assert np.corrcoef([r.deff[t] for t in teams], [deff[t] for t in teams])[0, 1] > 0.8


def test_no_games_returns_the_prior_and_the_prior_fades():
    rows, off, _ = synthetic_rows(n_days=180)
    prior = Ratings(off={t: 0.0 for t in off}, deff={t: 0.0 for t in off}, mu=2.5)
    sums = SeasonSums(rows, sorted(off), half_life=60.0)
    assert sums.solve(10, prior, EV).off == prior.off
    early = np.std(list(sums.solve(80, prior, EV).off.values()))
    late = np.std(list(sums.solve(250, prior, EV).off.values()))
    assert early < late


def test_engine_chains_preseason_priors():
    first, off, _ = synthetic_rows(season=2020)
    second = synthetic_rows(season=2021, seed=1)[0]
    engine = RatingsEngine(pd.concat([first, second]), EV, 60.0)
    best = max(off, key=off.get)
    assert np.isclose(engine.prior(2021).off[best], engine.final(2020).off[best] * EV.keep)
    assert np.isclose(engine.before(2021, 1).off[best], engine.prior(2021).off[best])
