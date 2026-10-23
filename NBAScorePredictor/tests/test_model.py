import numpy as np
import pandas as pd

from nbapredictor.model import ScoreModel


def synthetic_features(n=3000, seed=0, noisy=False):
    """Games whose points per 100 follow known coefficients, with a sharp line."""
    rng = np.random.default_rng(seed)
    f = pd.DataFrame({"game_id": np.arange(n), "season": 2020 + np.arange(n) % 4, "game_type": "R",
                      "playoff": False, "neutral": False, "completed": True, "periods": 4})
    for side in ("home", "away"):
        f[f"off_eff_{side}"] = rng.normal(0, 3, n)
        f[f"def_eff_{side}"] = rng.normal(0, 3, n)
        f[f"p_off_{side}"] = rng.normal(0, 2, n)
        f[f"p_def_{side}"] = rng.normal(0, 2, n)
        f[f"off_pace_{side}"] = rng.normal(0, 1.5, n)
        f[f"def_pace_{side}"] = f[f"off_pace_{side}"]
        f[f"{side}_rest"] = rng.choice([1, 2, 3], n)
        f[f"{side}_travel"] = 0.0
        f[f"{side}_tz_shift"] = 0.0
        f[f"adj_off_{side}"] = 0.0
        f[f"adj_def_{side}"] = 0.0
    f["elo_spread"] = 0.0
    f["env_ppp"] = 112.0
    f["env_pace"] = 99.0
    f["minutes"] = 48.0
    pace = 99.0 + 0.9 * (f["off_pace_home"] + f["off_pace_away"]) + rng.normal(0, 3, n)
    f["poss"] = pace
    ppp_h = 112 + 0.5 + 0.8 * f["off_eff_home"] + 0.7 * f["def_eff_away"] + 0.9 * f["p_off_home"] \
        + 0.6 * f["p_def_away"] + 1.0
    ppp_a = 112 + 0.5 + 0.8 * f["off_eff_away"] + 0.7 * f["def_eff_home"] + 0.9 * f["p_off_away"] \
        + 0.6 * f["p_def_home"] - 1.0
    mu_h, mu_a = pace * ppp_h / 100, pace * ppp_a / 100
    if noisy:
        # The model sees the ratings with error; the line below knows the truth.
        for col in [c for c in f if c.startswith(("off_eff", "def_eff", "p_off", "p_def"))]:
            f[col] = f[col] + rng.normal(0, 2.5, n)
    noise = rng.multivariate_normal([0, 0], [[121, 36], [36, 121]], n)
    f["home_score"] = np.rint(mu_h + noise[:, 0])
    f["away_score"] = np.rint(mu_a + noise[:, 1])
    f["home_reg"] = f["home_score"]
    f["away_reg"] = f["away_score"]
    f["spread"] = np.round((mu_h - mu_a) * 2) / 2
    f["total"] = np.round((mu_h + mu_a) * 2) / 2
    return f


def test_fit_recovers_the_efficiency_and_pace_maps():
    f = synthetic_features()
    m = ScoreModel.fit(f, calibrate_sim=False, use_market=False)
    c = m.eff_coef
    assert abs(c["eff_off"] - 0.8) < 0.15 and abs(c["eff_def"] - 0.7) < 0.15
    assert abs(c["p_off"] - 0.9) < 0.2 and abs(c["p_def"] - 0.6) < 0.2
    assert abs(c["home"] - 2.0) < 0.6
    assert abs(m.pace_coef["pace"] - 0.9) < 0.1
    means = m.model_means(f)
    assert abs(np.mean(means["total"]) - np.mean(f["home_score"] + f["away_score"])) < 1.0


def test_blend_leans_on_a_sharp_line_and_simulator_matches_the_scatter():
    f = synthetic_features(noisy=True)
    m = ScoreModel.fit(f)
    assert m.margin_weight < 0.4 and m.total_weight < 0.4
    sd, rho = m.sim.sd, m.sim.rho
    assert 10.0 < sd < 12.0 and 0.2 < rho < 0.4
    pred, sim = m.predict(f.head(50), n_sims=4000)
    decided = pred["pred_margin"] != 0                   # pick'em lines leave nothing to agree with
    agree = (pred["home_win_prob"] > 0.5) == (pred["pred_margin"] > 0)
    assert agree[decided].mean() > 0.95
    assert (pred["home_low"] < pred["sim_home"]).all() and (pred["sim_home"] < pred["home_high"]).all()
    restored = ScoreModel.from_dict(m.to_dict())
    assert restored.sim.sd == m.sim.sd and restored.eff_coef == m.eff_coef
