import numpy as np
import pandas as pd
import pytest

from mlbpredictor.players import blend_expected
from mlbpredictor.statcast import (X_COLUMNS, ExpectedHits, calibrated, calibration, league_daily, outcomes,
                                   spray_angle, summarize)


def balls(n, ev, la, event, date="2023-05-01", batter=1, pitcher=9, stand="R", hc=(125.42, 100.0)):
    return pd.DataFrame({"game_date": date, "game_pk": 1, "batter": batter, "pitcher": pitcher, "stand": stand,
                         "events": event, "launch_speed": ev, "launch_angle": la, "hc_x": hc[0], "hc_y": hc[1]},
                        index=range(n))


def test_spray_angle_is_mirrored_for_left_handed_batters():
    b = pd.concat([balls(1, 90, 10, "single", hc=(60.0, 140.0)), balls(1, 90, 10, "single", stand="L", hc=(60.0, 140.0))])
    a = spray_angle(b)
    assert a[0] < -15 and a[1] > 15          # to left field: pulled by a righty, opposite field for a lefty


def test_expected_hits_learn_the_outcome_of_each_contact_type():
    b = pd.concat([balls(200, 108, 28, "home_run"), balls(200, 108, 28, "field_out"),
                   balls(400, 70, -20, "field_out"), balls(100, 70, -20, "single")], ignore_index=True)
    m = ExpectedHits.fit(b)
    x = m.predict(pd.concat([balls(1, 108, 28, "x"), balls(1, 70, -20, "x"), balls(1, np.nan, 10, "x")]))
    assert x[0, 3] == pytest.approx(0.5, abs=0.03) and x[1, 0] == pytest.approx(0.2, abs=0.02)
    assert np.allclose(x[2], outcomes(b).mean(axis=0))          # no exit velocity: the league mix
    assert np.allclose(ExpectedHits.from_frame(m.to_frame()).predict(b), m.predict(b), atol=1e-4)


def test_calibration_scales_to_the_league_over_earlier_days_only():
    m = ExpectedHits(np.zeros((29, 47, 3, 4)), np.array([0.2, 0.05, 0.005, 0.03]))   # every ball: the league mix
    days = [f"2023-05-{d:02d}" for d in (1, 2, 3)]
    b = pd.concat([balls(100, np.nan, np.nan, "field_out", date=d) for d in days], ignore_index=True)
    b.loc[b.index[:40], "events"] = "single"                              # 40% singles on day one
    league = league_daily(b, m.predict(b))
    r = calibration(league)
    assert r.loc["2023-05-01", "s"] == 1.0                                # nothing before the first day
    assert r.loc["2023-05-02", "s"] == pytest.approx((40 + 1) / (20 + 1))   # day one: 40 actual, 20 expected
    players = summarize(b, m.predict(b), "batter")
    out = calibrated(players, r).set_index("date")
    assert out.loc["2023-05-02", "x_s"] == pytest.approx(players.set_index("date").loc["2023-05-02", "x_s"] * 41 / 21)


def test_ratings_mix_expected_hits_on_covered_player_days():
    rows = pd.DataFrame({"player_id": ["1", "1", "2"], "date": ["2023-05-01", "2023-05-01", "2023-05-01"],
                         "s": [2, 0, 1], "d": 0, "t": 0, "hr": [0, 1, 0], "out": [2, 3, 3]})
    for h in ("s", "d", "t", "hr"):
        rows[h + "_adj"] = rows[h].astype(float)
    sc = pd.DataFrame({"player_id": ["1"], "date": ["2023-05-01"], "bip": [8], "x_s": [2.0], "x_d": [0.8],
                       "x_t": [0.0], "x_hr": [0.4]})
    covered = blend_expected(rows, sc, 0.5)
    assert covered.tolist() == [True, True, False]
    # Row 0 had 4 of the day's 8 balls in play: half of 2 expected singles, mixed half and half with 2 actual.
    assert rows.loc[0, "s_adj"] == pytest.approx(0.5 * 2 + 0.5 * 1.0)
    assert rows.loc[1, "hr_adj"] == pytest.approx(0.5 * 1 + 0.5 * 0.2)
    assert rows.loc[2, "s_adj"] == 1.0                                    # no Statcast for player 2
    assert list(sc.columns[-4:]) == X_COLUMNS
