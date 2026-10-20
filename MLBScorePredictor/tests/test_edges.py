import numpy as np
import pandas as pd
import pytest

from mlbpredictor.edges import (EDGE_COLUMNS, EDGE_MIN_EV, add_edges, best_side, decimal_odds, edge_record,
                                expected_value, fair_american, grade_pick, implied_prob, market_options)


def game(**kw):
    row = {"home_team": "NYY", "away_team": "BOS", "model_home_prob": 0.6, "home_moneyline": np.nan,
           "away_moneyline": np.nan, "home_run_line": np.nan, "home_run_line_price": np.nan,
           "away_run_line_price": np.nan, "model_home_cover_prob": np.nan, "model_away_cover_prob": np.nan,
           "total_line": np.nan, "over_price": np.nan, "under_price": np.nan, "model_over_prob": np.nan,
           "model_under_prob": np.nan, "model_total_push_prob": np.nan, "home_score": np.nan, "away_score": np.nan}
    row.update(kw)
    return row


def test_odds_math_with_pushes():
    assert decimal_odds(150) == 2.5 and decimal_odds(-125) == 1.8 and decimal_odds(100) == 2.0
    assert np.isclose(implied_prob(-150), 0.6) and np.isclose(implied_prob(150), 0.4)
    assert fair_american(0.6) == -150 and fair_american(0.4) == 150 and fair_american(0.5) == 100
    assert np.isclose(expected_value(0.5, 0.0, 100), 0.0)
    assert np.isclose(expected_value(0.55, 0.0, -110), 0.55 * 100 / 110 - 0.45)
    # A push returns the stake: 45% win, 10% push, 45% loss at even money breaks even.
    assert np.isclose(expected_value(0.45, 0.10, 100), 0.0)
    assert np.isclose(expected_value(0.45, 0.10, -110), 0.45 * 100 / 110 - 0.45)


def test_best_side_needs_three_percent():
    opts = [{"label": "NYY", "side": "home", "price": -120, "p_win": 0.56, "p_push": 0.0},
            {"label": "BOS", "side": "away", "price": 110, "p_win": 0.44, "p_push": 0.0}]
    assert best_side(opts) is None                                      # EV +2.7% and -7.6%
    opts[0]["p_win"], opts[1]["p_win"] = 0.50, 0.50
    pick = best_side(opts)
    assert pick["label"] == "BOS" and np.isclose(pick["ev"], 0.05)      # 0.5 × 1.1 − 0.5
    assert best_side(opts, min_ev=0.06) is None
    assert expected_value(0.5, 0, 106) == pytest.approx(EDGE_MIN_EV)
    assert best_side([{**opts[1], "price": 106}]) is not None             # exactly at the bar counts


def test_run_line_uses_posted_side_and_never_assumes_a_price():
    # Away team favored: home +1.5 at -170, away -1.5 at +150.
    r = game(home_run_line=1.5, home_run_line_price=-170, away_run_line_price=150, model_home_cover_prob=0.55,
             model_away_cover_prob=0.45)
    opts = market_options(r)["spread"]
    assert [o["label"] for o in opts] == ["NYY +1.5", "BOS -1.5"] and opts[1]["line"] == -1.5
    pick = best_side(opts)
    assert pick["label"] == "BOS -1.5" and np.isclose(pick["ev"], 0.45 * 1.5 - 0.55)
    # Without a price there is nothing to bet: no option, so no edge.
    assert market_options(game(home_run_line=-1.5, model_home_cover_prob=0.5, model_away_cover_prob=0.5))[
        "spread"] == []
    assert market_options(game(model_home_prob=0.7))["moneyline"] == []


def test_total_price_assumed_only_when_missing():
    r = game(total_line=8.0, model_over_prob=0.50, model_under_prob=0.42, model_total_push_prob=0.08)
    opts = market_options(r)["total"]
    assert all(o["assumed"] and o["price"] == -110 for o in opts) and opts[0]["p_push"] == 0.08
    pick = best_side(opts)
    assert pick["label"] == "Over 8" and np.isclose(pick["ev"], 0.5 * 100 / 110 - 0.42)
    posted = market_options(game(total_line=8.5, over_price=-105, under_price=-115, model_over_prob=0.5,
                                 model_under_prob=0.5))["total"]
    assert [o["price"] for o in posted] == [-105, -115] and not any(o["assumed"] for o in posted)


def test_add_edges_grading_and_record():
    rows = pd.DataFrame([
        game(home_moneyline=110, away_moneyline=-130, model_home_prob=0.55, home_score=5, away_score=3),
        game(home_moneyline=-150, away_moneyline=130, model_home_prob=0.6, home_score=2, away_score=3),
        game(total_line=8.0, over_price=-110, under_price=-110, model_over_prob=0.56, model_under_prob=0.37,
             model_total_push_prob=0.07, home_score=5, away_score=3),
        game(home_run_line=-1.5, home_run_line_price=140, away_run_line_price=-160, model_home_cover_prob=0.45,
             model_away_cover_prob=0.55, home_score=4, away_score=3),
    ])
    out = add_edges(rows)
    assert set(EDGE_COLUMNS) <= set(out.columns)
    assert out.loc[0, "moneyline_edge_pick"] == "NYY" and out.loc[0, "moneyline_edge_price"] == 110
    assert out.loc[1, "moneyline_edge_pick"] == ""                       # -150 on a 60% team is break-even
    assert out.loc[2, "total_edge_pick"] == "Over 8" and out.loc[2, "total_edge_side"] == "over"
    assert out.loc[3, "spread_edge_pick"] == "NYY -1.5" and np.isclose(out.loc[3, "spread_edge_ev"], 0.08)
    ml, tot, rl = (edge_record(out, m) for m in ("moneyline", "total", "spread"))
    assert (ml["bets"], ml["wins"], ml["units"]) == (1, 1, pytest.approx(1.1))
    assert (tot["wins"], tot["losses"], tot["pushes"], tot["units"]) == (0, 0, 1, 0.0)
    assert (rl["wins"], rl["losses"], rl["roi"]) == (0, 1, -1.0)                 # won by one: no cover


def test_grade_pick():
    assert grade_pick("spread", "away", 1.5, -180, 4, 3) == ("W", pytest.approx(100 / 180))
    assert grade_pick("spread", "home", -1.5, 130, 4, 3) == ("L", -1.0)
    assert grade_pick("total", "under", 9.0, -110, 5, 4) == ("P", 0.0)
    assert grade_pick("total", "under", 9.5, 105, 5, 4) == ("W", pytest.approx(1.05))
    assert grade_pick("moneyline", "away", np.nan, 120, 2, 6) == ("W", pytest.approx(1.2))


def test_backtest_edges_on_historical_prices():
    from mlbpredictor.backtest import edge_backtest, roi_interval
    from mlbpredictor.report import backtest_edge_table

    test = pd.DataFrame({"game_id": ["a", "b"], "home_team": "NYY", "away_team": "BOS", "home_score": [5, 2],
                         "away_score": [3, 4], "home_moneyline": [110, -150], "away_moneyline": [-130, 130],
                         "open_home_moneyline": [-140, -150], "open_away_moneyline": [120, 130],
                         "total_line": [8.0, 7.5], "over_price": [-110, 105], "under_price": [-110, -125]})
    own = pd.DataFrame({"home_win_prob": [0.55, 0.6], "model_over_prob": [0.46, 0.40],
                        "model_under_prob": [0.46, 0.60], "model_total_push_prob": [0.08, 0.0]})
    out = edge_backtest(test, own)
    assert out["Run line"] is None
    close, opening, total = out["Moneyline, closing line"], out["Moneyline, opening line"], out["Total, closing line"]
    assert (close["bets"], close["wins"], close["units"]) == (1, 1, pytest.approx(1.1))
    assert opening["bets"] == 0 and np.isnan(opening["roi_low"])
    # Game a's total: 46% over, 8% push at -110 is EV -5.2%; game b: Under 7.5 at -125, 60% is EV +8%, and it won.
    assert (total["bets"], total["wins"], total["units"]) == (1, 1, pytest.approx(0.8))
    lo, hi = roi_interval([1.0, -1.0, 1.0, -1.0])
    assert -1.0 <= lo < 0 < hi <= 1.0
    table = backtest_edge_table(out)
    assert "| Moneyline, closing line | 1 | 1-0-0 | +1.10 | +110.0% | +110.0% to +110.0% |" in table
    assert "| Moneyline, opening line | 0 | 0-0-0 | +0.00 | – | – |" in table
    assert "| Run line | no historical prices | | | | |" in table
