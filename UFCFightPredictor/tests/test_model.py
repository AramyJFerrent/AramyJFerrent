import numpy as np
import pandas as pd

from ufcpredictor.config import Hyperparams
from ufcpredictor.features import SIDE_FIELDS, WIN_FEATURES
from ufcpredictor.model import METHODS, Calibration, FightModel, RoundModel, WinModel
from ufcpredictor.odds import devig
from ufcpredictor.ratings import Glicko2, winner_score


def synthetic(n=1200, seed=0):
    """Fights where the first feature drives the winner and finishes follow durability."""
    rng = np.random.default_rng(seed)
    f = pd.DataFrame({c: rng.normal(size=n) for c in WIN_FEATURES})
    p = 1 / (1 + np.exp(-(0.8 * f["glicko_logit"] - 0.3 * f["d_age"])))
    win_a = rng.random(n) < p
    f["winner"] = np.where(win_a, "a", "b")
    for side in "ab":
        for k in SIDE_FIELDS:
            f[f"{side}_{k}"] = rng.random(n)
    loser_dur = np.where(win_a, f["b_ko_loss"], f["a_ko_loss"])
    f["method"] = np.where(rng.random(n) < 0.2 + 0.5 * loser_dur, "KO",
                           np.where(rng.random(n) < 0.3, "SUB", "DEC"))
    f["end_round"] = np.where(f["method"] == "DEC", 3, rng.integers(1, 4, n))
    f["rounds"] = np.where(rng.random(n) < 0.1, 5, 3)
    f["division"] = rng.choice(["Lightweight", "Heavyweight", "Women's Strawweight"], n)
    f["gender"] = np.where(f["division"].str.startswith("Women"), "F", "M")
    f["title"] = False
    f["date"] = pd.to_datetime("2015-01-01") + pd.to_timedelta(rng.integers(0, 3000, n), unit="D")
    f["odds_a"] = np.where(p > 0.5, -100 * p / (1 - p), 100 * (1 - p) / p) * 1.0
    f["odds_b"] = np.where(p > 0.5, 100 * p / (1 - p), -100 * (1 - p) / p) * 1.0
    return f


def mirror(f):
    g = f.copy()
    for c in WIN_FEATURES:
        g[c] = -f[c]
    for k in SIDE_FIELDS:
        g[f"a_{k}"], g[f"b_{k}"] = f[f"b_{k}"], f[f"a_{k}"]
    g["odds_a"], g["odds_b"] = f["odds_b"], f["odds_a"]
    return g


def test_win_model_is_corner_symmetric():
    f = synthetic()
    m = WinModel.fit(f, ridge=10.0)
    assert np.allclose(m.logit(f), -m.logit(mirror(f)))
    assert m.weights()["glicko_logit"] > 0 > m.weights()["d_age"]


def test_outcomes_form_one_consistent_distribution():
    f = synthetic()
    model = FightModel.fit(f, ridge=10.0)
    out = model.predict(f.head(200))
    six = out[[f"{s}_{m}" for s in "ab" for m in METHODS]]
    assert np.allclose(six.sum(axis=1), 1.0)
    assert np.allclose(out[["a_ko", "a_sub", "a_dec"]].sum(axis=1), out["p_a"])
    rounds = out[[f"r{r}" for r in range(1, 6)]].sum(axis=1)
    assert np.allclose(rounds, 1 - out["p_distance"], atol=1e-3)
    assert (out.loc[f.head(200)["rounds"].to_numpy() == 3, ["r4", "r5"]] == 0).all().all()
    # Swapping corners swaps every answer.
    swapped = model.predict(mirror(f.head(200)))
    assert np.allclose(swapped["p_a"], 1 - out["p_a"])
    assert np.allclose(swapped["a_ko"], out["b_ko"])
    # Fragile losers get knocked out more often.
    fragile = f.head(200).assign(b_ko_loss=0.95, a_ko_loss=0.95)
    sturdy = f.head(200).assign(b_ko_loss=0.05, a_ko_loss=0.05)
    assert model.predict(fragile)["a_ko"].mean() > model.predict(sturdy)["a_ko"].mean()


def test_calibration_leans_on_a_sharp_market():
    rng = np.random.default_rng(1)
    truth = rng.normal(scale=1.0, size=4000)
    y = (rng.random(4000) < 1 / (1 + np.exp(-truth))).astype(float)
    model_z = truth + rng.normal(scale=1.0, size=4000)
    market_z = truth + rng.normal(scale=0.3, size=4000)
    cal = Calibration.fit(model_z, market_z, y)
    assert cal.market_weight > 0.7
    no_market = cal.apply(np.array([1.0]), np.array([np.nan]))
    assert np.isclose(no_market[0], cal.model_slope)


def test_round_split_shifts_earlier_for_finishers():
    rm = RoundModel({"3": [0.25, 0.2, 0.15], "5": [0.2, 0.15, 0.12, 0.1, 0.1]})
    split = rm.split(np.array([0.3, 0.8]), np.array([3, 3]))
    assert np.allclose(split.sum(axis=1), [0.3, 0.8], atol=1e-4)
    share_r1 = split[:, 0] / split.sum(axis=1)
    assert share_r1[1] > share_r1[0]


def test_glicko_basics():
    hp = Hyperparams()
    g = Glicko2(hp)
    assert g.win_logit("a", "b", 0.0) == 0.0
    g.update("a", "b", 1.0, 0.0)
    assert g.win_logit("a", "b", 1.0) > 0 and np.isclose(g.win_logit("a", "b", 1.0), -g.win_logit("b", "a", 1.0))
    _, rd_now, fights = g.state("a", 1.0)
    _, rd_later, _ = g.state("a", 1000.0)
    assert fights == 1 and rd_later > rd_now
    assert rd_later <= hp.glicko_debut_rd + 1e-9
    assert winner_score("a", "KO", None, hp) == 1.0
    assert winner_score("b", "DEC", "split", hp) == 1 - hp.score_split
    assert winner_score("nc", "NC", None, hp) is None


def test_devig():
    p = devig(np.array([-200.0]), np.array([170.0]))
    assert 0.64 < p[0] < 0.66
