import numpy as np
import pandas as pd

from ufcpredictor.config import Hyperparams
from ufcpredictor.data import STAT_COLUMNS
from ufcpredictor.features import WIN_FEATURES, FeatureBuilder


def history():
    rows = []
    dates = pd.date_range("2020-01-04", periods=6, freq="90D")
    pairs = [("ann", "bea"), ("ann", "cal"), ("bea", "cal"), ("ann", "bea"), ("cal", "dee"), ("ann", "dee")]
    for i, (d, (a, b)) in enumerate(zip(dates, pairs)):
        rows.append({"bout_id": f"b{i}", "event": f"E{i}", "date": d, "location": "Las Vegas", "order": 0,
                     "fighter_a": a.title(), "fighter_b": b.title(), "a_id": a, "b_id": b,
                     "division": "Lightweight", "gender": "M", "title": False, "rounds": 3,
                     "winner": "a", "method": "KO" if i % 2 else "DEC", "decision": None if i % 2 else "unanimous",
                     "end_round": 1 if i % 2 else 3, "end_seconds": 100.0, "fight_seconds": 100.0 if i % 2 else 900.0,
                     "referee": "x"})
    bouts = pd.DataFrame(rows)
    stats = []
    for b in rows:
        for side in "ab":
            row = {c: 0.0 for c in STAT_COLUMNS}
            row.update(bout_id=b["bout_id"], side=side, sig_l=40.0 if side == "a" else 20.0, sig_a=80.0,
                       td_l=2.0 if side == "a" else 0.0, td_a=4.0)
            stats.append(row)
    fighters = pd.DataFrame({"fighter_id": ["ann", "bea", "cal"], "name": ["Ann", "Bea", "Cal"],
                             "height": [70.0, 68.0, np.nan], "reach": [72.0, 70.0, np.nan],
                             "stance": ["Southpaw", "Orthodox", "Orthodox"],
                             "dob": pd.to_datetime(["1990-01-01", "1985-01-01", None]), "weight": [155.0] * 3})
    return bouts, pd.DataFrame(stats), fighters


def test_features_use_only_earlier_fights():
    bouts, stats, fighters = history()
    feats = FeatureBuilder(bouts, stats, fighters, Hyperparams()).build()
    assert feats.loc[0, "a_fights"] == 0 and feats.loc[0, "glicko_logit"] == 0.0
    assert feats.loc[1, "a_fights"] == 1 and feats.loc[1, "glicko_logit"] > 0
    # Rewriting a later result changes nothing before it.
    flipped = bouts.copy()
    flipped.loc[4, "winner"] = "b"
    again = FeatureBuilder(flipped, stats, fighters, Hyperparams()).build()
    pd.testing.assert_frame_equal(feats.loc[:4, WIN_FEATURES], again.loc[:4, WIN_FEATURES])
    assert not np.isclose(feats.loc[5, "glicko_logit"], again.loc[5, "glicko_logit"])
    assert feats[WIN_FEATURES].notna().all().all()


def test_upcoming_matches_build_and_handles_debutants():
    bouts, stats, fighters = history()
    fb = FeatureBuilder(bouts, stats, fighters, Hyperparams())
    fb.build()
    card = pd.DataFrame({"a_id": ["ann", "new"], "b_id": ["bea", "ann"], "date": [pd.Timestamp("2021-08-01")] * 2,
                         "division": ["Lightweight", "Lightweight"]})
    up = fb.upcoming(card)
    assert up.loc[0, "a_fights"] == 4 and up.loc[1, "a_fights"] == 0
    assert up.loc[1, "d_debut"] == 1.0 and up.loc[1, "glicko_logit"] < 0
    assert up.loc[0, "d_southpaw"] == 1.0                 # southpaw Ann against orthodox Bea
    assert up.loc[0, "d_slpm"] > 0                         # Ann out-landed everyone
    assert up[WIN_FEATURES].notna().all().all()
