import math

import numpy as np
import pandas as pd
import pytest
import requests

from bettingcore import (
    anchored,
    best_side,
    decimal_odds,
    devig,
    expected_value,
    fair_american,
    fetch,
    format_american,
    implied_prob,
    kelly_fraction,
    kelly_stake,
    market_chance,
    median_price,
    no_push,
    paired_bootstrap,
    payout,
    roi_interval,
    settle,
    stake_picks,
    summarize,
    valid_price,
    with_push,
    write_if_changed,
)


def test_prices():
    assert decimal_odds(-110) == pytest.approx(1.9091, abs=1e-4)
    assert decimal_odds(150) == 2.5
    assert np.allclose(decimal_odds(np.array([-200, 100])), [1.5, 2.0])
    assert math.isnan(decimal_odds(50)) and math.isnan(decimal_odds(float("nan")))
    assert implied_prob(-110) == pytest.approx(110 / 210)
    assert not valid_price(None) and not valid_price("x") and not valid_price(-99) and valid_price(-100)
    assert fair_american(0.6) == -150 and fair_american(0.4) == 150
    assert format_american(120) == "+120" and format_american(-110, assumed=True) == "-110*"
    assert format_american(None) == "–"
    # Quotes either side of even money: the median is near even, not 0.
    assert median_price([-105, 105, 100]) in (100.0, -100.0)
    assert devig(-110, -110) == pytest.approx(0.5)
    assert devig(-200, 170) == pytest.approx((2 / 3) / (2 / 3 + 100 / 270))


def test_expected_value_with_push():
    assert expected_value(0.55, 0.0, -110) == pytest.approx(0.55 * 100 / 110 - 0.45)
    # A push returns the stake: it neither wins nor loses.
    assert expected_value(0.5, 0.1, 100) == pytest.approx(0.5 - 0.4)


def test_best_side_needs_price_and_bar():
    sides = [{"label": "A", "side": "home", "price": -110, "prob": 0.56, "push": 0.0},
             {"label": "B", "side": "away", "price": -110, "prob": 0.44, "push": 0.0},
             {"label": "C", "side": "x", "price": None, "prob": 0.99}]
    pick = best_side(sides)
    assert pick["pick"] == "A" and pick["ev"] == pytest.approx(0.56 * 100 / 110 - 0.44)
    assert best_side(sides, min_ev=0.1) is None
    assert best_side([{"label": "A", "side": "home", "price": 150, "prob": float("nan")}]) is None


def test_kelly():
    # Even money at 55%: full Kelly is 10% of the bankroll.
    assert kelly_fraction(0.55, 0.0, 100) == pytest.approx(0.10)
    assert kelly_fraction(0.45, 0.0, 100) == 0.0
    # Pushes scale the bet up: the same win/loss ratio over fewer live outcomes.
    assert kelly_fraction(0.55 * 0.9, 0.1, 100) == pytest.approx(0.10)
    assert kelly_stake(0.55, 0.0, 100) == pytest.approx(2.5)        # quarter Kelly, in % of bankroll
    assert kelly_fraction(0.6, 0.0, None) == 0.0


def test_stake_picks_share_a_game_cap():
    big = {"prob": 0.7, "push": 0.0, "price": 100}           # full Kelly 40% -> 10 units at quarter
    out = stake_picks({"spread": big, "moneyline": dict(big), "total": None}, cap=3.0)
    assert out["total"] is None
    assert out["spread"]["stake"] + out["moneyline"]["stake"] == pytest.approx(3.0)
    small = stake_picks({"spread": {"prob": 0.55, "push": 0.0, "price": 100}})
    assert small["spread"]["stake"] == pytest.approx(2.5)


def test_settle_and_payout():
    assert settle(3.5, -110) == ("W", pytest.approx(100 / 110))
    assert settle(-0.5, 150) == ("L", -1.0)
    assert settle(0.0, -110) == ("P", 0.0)
    assert settle(float("nan"), -110)[0] is None
    assert payout("W", 200) == 2.0 and payout("P", 200) == 0.0 and math.isnan(payout(None, 200))


def test_summarize_resamples_games():
    res = pd.DataFrame({"result": ["W", "L", "P", "W"], "stake": [1.0, 2.0, 1.0, 0.5],
                        "profit": [0.9, -2.0, 0.0, 0.75], "game": ["g1", "g1", "g2", "g3"]})
    s = summarize(res)
    assert (s["bets"], s["wins"], s["losses"], s["pushes"]) == (4, 2, 1, 1)
    assert s["staked"] == 4.5 and s["units"] == pytest.approx(-0.35)
    assert s["roi"] == pytest.approx(-0.35 / 4.5)
    assert s["roi_low"] <= s["roi"] <= s["roi_high"]
    assert math.isnan(s["expected_roi"])                        # no ``ev`` column
    with_ev = summarize(res.assign(ev=[0.1, 0.0, 0.05, 0.2]))
    assert with_ev["expected_roi"] == pytest.approx((0.1 + 0.0 + 0.05 + 0.1) / 4.5)
    empty = summarize(pd.DataFrame(columns=["result", "stake", "profit", "game"]))
    assert empty["bets"] == 0 and math.isnan(empty["roi"])


def test_roi_interval_clusters_correlated_bets():
    rng = np.random.default_rng(1)
    won = rng.random(400) < 0.5
    profit = np.where(won, 1.0, -1.0)
    # Two identical bets per game: resampling bets alone understates the spread.
    doubled = np.repeat(profit, 2)
    games = np.repeat(np.arange(400), 2)
    lo_b, hi_b = roi_interval(doubled, np.ones(800))
    lo_g, hi_g = roi_interval(doubled, np.ones(800), games)
    assert (hi_g - lo_g) > 1.2 * (hi_b - lo_b)


def test_paired_bootstrap():
    mean, lo, hi = paired_bootstrap(np.ones(50), np.zeros(50))
    assert (mean, lo, hi) == (1.0, 1.0, 1.0)


def test_write_if_changed(tmp_path):
    p = tmp_path / "x.md"
    assert write_if_changed(p, "Updated now\nbody\n", volatile=("Updated",))
    assert not write_if_changed(p, "Updated later\nbody\n", volatile=("Updated",))
    assert write_if_changed(p, "Updated later\nnew body\n", volatile=("Updated",))
    # ``contains`` matches the volatile text anywhere in a line, not just at its start.
    assert write_if_changed(p, 'x "at": 1\nnew body\n', volatile=('"at"',))
    assert write_if_changed(p, 'x "at": 2\nnew body\n', volatile=('"at"',))
    assert not write_if_changed(p, 'x "at": 3\nnew body\n', volatile=('"at"',), contains=True)


def test_fetch_uses_fresh_cache_and_stale_fallback(tmp_path, monkeypatch):
    p = tmp_path / "f.csv"
    p.write_text("cached")
    assert fetch("http://example.invalid/f.csv", p, max_age_hours=1).read_text() == "cached"

    def boom(*a, **k):
        raise requests.ConnectionError("down")
    monkeypatch.setattr(requests, "get", boom)
    monkeypatch.setattr("bettingcore.io.time.sleep", lambda s: None)
    assert fetch("http://example.invalid/f.csv", p, max_age_hours=0, retries=2).read_text() == "cached"
    with pytest.raises(requests.ConnectionError):
        fetch("http://example.invalid/g.csv", tmp_path / "g.csv", max_age_hours=0, retries=2)


def test_anchored_chances_start_from_the_market():
    # A prediction on the line leaves the market's chance unchanged, whatever the simulator's shape.
    assert anchored(0.5, 0.47, 0.47) == pytest.approx(0.5)
    # The prediction moved the simulator's chance up 4 points: so does the edge chance.
    assert anchored(market_chance(-120, 100), 0.51, 0.47) == pytest.approx(market_chance(-120, 100) + 0.04)
    assert anchored(0.99, 0.9, 0.5) == 0.995                      # kept off certainty
    assert np.isnan(anchored(np.nan, 0.5, 0.5))
    assert market_chance(np.nan, -110) == 0.5 and np.isnan(market_chance(np.nan, -110, default=np.nan))
    assert no_push(0.45, 0.1) == pytest.approx(0.5) and with_push(0.5, 0.1) == pytest.approx(0.45)
    assert np.allclose(anchored(np.array([0.5, 0.6]), np.array([0.55, 0.6]), np.array([0.5, 0.6])), [0.55, 0.6])
