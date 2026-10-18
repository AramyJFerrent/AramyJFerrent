import numpy as np
import pandas as pd

from cfbpredictor.config import Hyperparams
from cfbpredictor.prior import PriorModel
from cfbpredictor.ratings import Ratings, RatingsEngine, fit, prepare_rows, targets

EPA = targets(Hyperparams())["epa"]


def synthetic_rows(n_weeks=10, seed=0, season=2020, conf_shift=0.0):
    """Two conferences that play each other now and then; team strength is known."""
    rng = np.random.default_rng(seed)
    teams = [f"A{i}" for i in range(6)] + [f"B{i}" for i in range(6)]
    conf = {t: t[0] for t in teams}
    off = dict(zip(teams, np.linspace(-0.15, 0.15, 12) + np.where(np.arange(12) < 6, conf_shift, 0)))
    deff = dict(zip(teams, np.linspace(0.1, -0.1, 12)))
    rows = []
    for week in range(1, n_weeks + 1):
        order = rng.permutation(teams)
        for a, b in zip(order[::2], order[1::2]):
            for team, opp, h in ((a, b, 1.0), (b, a, -1.0)):
                y = off[team] + deff[opp] + 0.02 * h + rng.normal(0, 0.12)
                rows.append({"game_id": f"{week}_{a}_{b}", "season": season, "week": week, "team": team,
                             "opp": opp, "conf": conf[team], "opp_conf": conf[opp], "division": "fbs",
                             "h": h, "g": 0.0, "y": y, "w": 65.0})
    return pd.DataFrame(rows), off, deff, conf


def test_ridge_recovers_team_strength():
    rows, off, deff, conf = synthetic_rows(n_weeks=16)
    r = fit(rows, ref_week=17, prior=Ratings(), target=EPA, half_life_weeks=1000, conferences=conf)
    teams = sorted(off)
    assert np.corrcoef([r.off[t] for t in teams], [off[t] for t in teams])[0, 1] > 0.9
    assert np.corrcoef([r.deff[t] for t in teams], [deff[t] for t in teams])[0, 1] > 0.8
    assert 0.0 < r.hfa < 0.05


def test_no_games_returns_the_prior():
    prior = Ratings(off={"A": 0.1, "B": -0.1}, deff={"A": 0.0, "B": 0.05}, mu=0.01, hfa=0.02)
    empty = pd.DataFrame(columns=["team", "opp", "conf", "opp_conf", "week", "h", "g", "y", "w"])
    r = fit(empty, 1, prior, EPA, 30.0, conferences={"A": "X", "B": "Y"})
    assert np.allclose([r.off["A"], r.off["B"]], [0.1, -0.1])
    assert np.allclose([r.deff["A"], r.deff["B"]], [0.0, 0.05])


def test_prior_dominates_early_and_fades():
    rows, off, _, conf = synthetic_rows(n_weeks=16)
    prior = Ratings(off={t: 0.0 for t in off}, deff={t: 0.0 for t in off})
    early = fit(rows[rows.week <= 1], 2, prior, EPA, 30.0, conf)
    late = fit(rows, 17, prior, EPA, 30.0, conf)
    assert np.std(list(early.off.values())) < np.std(list(late.off.values()))


def test_loose_conference_prior_moves_a_whole_conference():
    # Conference A is 0.1 EPA better than everyone thought; a loose conference
    # prior lets its teams that played little move with it.
    rows, off, _, conf = synthetic_rows(n_weeks=6, conf_shift=0.1)
    prior = Ratings(off={t: v - (0.1 if t.startswith("A") else 0.0) for t, v in off.items()},
                    deff={t: 0.0 for t in off})
    tight = fit(rows, 7, prior, EPA, 30.0, conf)
    loose_target = EPA.__class__(**{**EPA.__dict__, "conf_prior": 50.0})
    loose = fit(rows, 7, prior, loose_target, 30.0, conf)
    gain = lambda r: np.mean([r.off[t] - prior.off[t] for t in off if t.startswith("A")])
    assert gain(loose) > gain(tight) > 0


def test_prepare_rows_marks_home_neutral_and_fcs():
    tg = pd.DataFrame([
        dict(game_id=1, season=2025, week=1, team="X", opp="Y", home=1, neutral=False, division="fbs",
             opp_division="fcs", conference="SEC", opp_conference="Big Sky", plays=60, w=50.0, epa=5.0,
             g_plays=10, g_epa=-1.0, st_epa=1.0),
        dict(game_id=2, season=2025, week=2, team="X", opp="Z", home=0, neutral=True, division="fbs",
             opp_division="fbs", conference="SEC", opp_conference=None, plays=60, w=60.0, epa=6.0,
             g_plays=0, g_epa=0.0, st_epa=0.0),
    ])
    rows = prepare_rows(tg, EPA).set_index("game_id")
    assert rows.loc[1, "h"] == 1.0 and rows.loc[2, "h"] == 0.0
    assert rows.loc[1, "g"] == 1.0 and rows.loc[2, "g"] == 0.0
    assert np.isclose(rows.loc[1, "y"], 0.1)                     # garbage time excluded by default
    assert rows.loc[2, "opp_conf"] == "FBS Independents"


def test_prior_regression_learns_carryover():
    seasons = []
    rng = np.random.default_rng(3)
    base, _, _, conf = synthetic_rows(n_weeks=12, season=2015)
    strength = {t: rng.normal(0, 0.1) for t in conf}
    for s in range(2015, 2022):
        rows = base.assign(season=s)
        rows["y"] = rows["y"] + rows["team"].map(strength)
        seasons.append(rows)
        strength = {t: 0.7 * v + rng.normal(0, 0.05) for t, v in strength.items()}   # persistent
    rows = pd.concat(seasons, ignore_index=True)
    members = {s: {t: (c, "fbs") for t, c in conf.items()} for s in range(2015, 2023)}
    pm = PriorModel(rows, EPA, None, members)
    coefs = pm.coefficients(2022)["off"]
    assert 0.2 < coefs["last_off"] + coefs["hist_off"] < 1.2
    engine = RatingsEngine(rows, EPA, 30.0, pm, members)
    week1 = engine.before(2021, 1)
    prior = pm.prior(2021)
    assert np.isclose(week1.off["A0"], prior.off["A0"], atol=1e-6)
