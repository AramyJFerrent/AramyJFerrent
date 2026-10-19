import numpy as np
import pandas as pd

from ufcpredictor import odds as odds_mod
from ufcpredictor.odds import append_odds_log, attach_dataset_odds, attach_logged_odds, devig_methods


def bouts():
    return pd.DataFrame({"date": pd.to_datetime(["2025-03-01", "2025-03-01", "2026-05-02"]),
                         "fighter_a": ["Ann Lee", "Cal Poe", "Eve Fox"], "fighter_b": ["Bea Cruz", "Dee Oak", "Gus Hil"]})


def test_dataset_odds_follow_our_corners():
    ds = pd.DataFrame({"date": pd.to_datetime(["2025-03-01", "2025-02-28"]), "r": ["Bea Cruz", "Cal Poe"],
                       "b": ["Ann Lee", "Dee Oak"], "r_odds": [-200.0, 120.0], "b_odds": [170.0, -140.0],
                       "r_ko": [300.0, 400.0], "r_sub": [800.0, 900.0], "r_dec": [150.0, 250.0],
                       "b_ko": [500.0, 350.0], "b_sub": [1200.0, 700.0], "b_dec": [350.0, 200.0]})
    out = attach_dataset_odds(bouts(), ds)
    assert (out.loc[0, "odds_a"], out.loc[0, "odds_b"]) == (170.0, -200.0)    # flipped to Ann's side
    assert out.loc[0, "odds_a_ko"] == 500.0 and out.loc[0, "odds_b_dec"] == 150.0
    assert out.loc[1, "odds_a"] == 120.0                                       # a day apart still matches
    assert np.isnan(out.loc[2, "odds_a"])
    six = devig_methods(out.iloc[:2])
    assert np.allclose(six.sum(axis=1), 1.0)


def test_odds_log_records_changes_only(tmp_path, monkeypatch):
    monkeypatch.setattr(odds_mod, "ODDS_LOG_PATH", tmp_path / "odds_log.csv")
    monkeypatch.setattr(odds_mod, "DATA_DIR", tmp_path)
    card = pd.DataFrame({"bout_key": ["k1"], "date": [pd.Timestamp("2026-05-02")], "fighter_a": ["Gus Hil"],
                         "fighter_b": ["Eve Fox"], "odds_a": [-150.0], "odds_b": [130.0], "odds_source": ["ESPN"]})
    t0 = pd.Timestamp("2026-04-28", tz="UTC")
    append_odds_log(card, t0)
    append_odds_log(card, t0 + pd.Timedelta(hours=6))                         # unchanged: not logged again
    lg = append_odds_log(card.assign(odds_a=-170.0, odds_b=145.0), t0 + pd.Timedelta(days=1))
    assert len(lg) == 2
    filled = attach_logged_odds(bouts(), attach_dataset_odds(bouts(), pd.DataFrame()), lg)
    assert (filled.loc[2, "odds_a"], filled.loc[2, "odds_b"]) == (145.0, -170.0)   # last price, Eve's side
    assert filled.loc[2, "odds_source"] == "ESPN"
