from types import SimpleNamespace

import numpy as np
import pandas as pd
import pytest

from nhlpredictor import pipeline
from nhlpredictor.edges import (ASSUMED_PRICE, EDGE_COLUMNS, EDGE_MIN_EV, add_edges, best_side, decimal_odds,
                                edge_record, expected_value, fair_american, game_edges, grade_edge, implied_prob,
                                puck_line, roi_interval)
from nhlpredictor.pipeline import LOG_COLUMNS, load_log, prediction_rows
from nhlpredictor.report import backtest_edge_table, edge_cell, upcoming_table
from nhlpredictor.simulate import SimParams, line_probs, simulate


def game(**kw):
    """A logged game with prices and model-only chances; override any field."""
    row = {c: np.nan for c in LOG_COLUMNS}
    row.update(game_id=1, season=2027, game_type="R", date="2026-10-20",
               start=pd.Timestamp("2026-10-20 23:00", tz="UTC"), away_team="SJS", home_team="MTL",
               away_goalie="A", home_goalie="B", pred_away=2.7, pred_home=3.8, pred_total=6.5,
               headline_away=3, headline_home=4, home_win_prob=0.66, away_win_prob=0.34, ot_prob=0.2,
               home_cover_prob=0.45, away_cover_prob=0.2, away_low=1, away_high=5, home_low=1, home_high=6,
               model_home_prob=0.66,
               home_moneyline=-205, away_moneyline=170, total_line=6.5, over_price=-110, under_price=-110,
               home_spread_line=-1.5, home_spread_price=150, away_spread_price=-180,
               model_home_cover_prob=0.45, model_away_cover_prob=0.55, model_spread_push_prob=0.0,
               model_over_prob=0.49, model_under_prob=0.51, model_total_push_prob=0.0)
    row.update(kw)
    return row


def ns(**kw):
    return SimpleNamespace(**game(**kw))


# ---- odds math ---------------------------------------------------------

def test_decimal_implied_and_fair_odds():
    assert decimal_odds(150) == 2.5 and np.isclose(decimal_odds(-200), 1.5)
    assert np.isclose(implied_prob(-110), 110 / 210) and np.isclose(implied_prob(100), 0.5)
    assert fair_american(0.6) == -150 and fair_american(0.4) == 150 and fair_american(0.5) == 100


def test_expected_value_counts_pushes_as_stake_returned():
    assert np.isclose(expected_value(0.5, 0.0, 100), 0.0)
    assert np.isclose(expected_value(0.45, 0.0, 150), 0.45 * 1.5 - 0.55)
    # Same win chance, but a push instead of a loss on 10% of outcomes.
    assert np.isclose(expected_value(0.5, 0.1, -110), 0.5 * 100 / 110 - 0.4)
    assert expected_value(0.5, 0.1, -110) > expected_value(0.5, 0.0, -110)


def test_best_side_picks_the_highest_ev_above_the_bar():
    sides = [{"side": "home", "label": "MTL -1.5", "line": -1.5, "price": 150, "prob": 0.45, "push": 0.0},
             {"side": "away", "label": "SJS +1.5", "line": 1.5, "price": -180, "prob": 0.55, "push": 0.0}]
    pick = best_side(sides)
    assert pick["side"] == "home" and np.isclose(pick["ev"], 0.125)
    sides[0]["prob"] = 0.41                                  # EV +2.5%: below the bar
    assert best_side(sides) is None
    assert best_side(sides, min_ev=0.02)["side"] == "home"
    sides[0]["price"] = np.nan                               # unpriced sides are skipped
    assert best_side(sides, min_ev=-1)["side"] == "away"
    assert EDGE_MIN_EV == 0.03


def test_puck_line_defaults_to_the_models_favorite():
    assert puck_line(1.5, 0.7) == 1.5
    assert puck_line(np.nan, 0.6) == -1.5 and puck_line(np.nan, 0.4) == 1.5


# ---- edges per market ----------------------------------------------------

def test_game_edges_for_each_market():
    e = game_edges(ns())
    assert e["spread_edge_pick"] == "MTL -1.5" and e["spread_edge_price"] == 150
    assert e["spread_edge_line"] == -1.5 and np.isclose(e["spread_edge_ev"], 0.45 * 1.5 - 0.55)
    # Model 66% at -205: EV = 0.66 * 100/205 - 0.34 < 0; SJS +170: 0.34 * 1.7 - 0.66 < 0.
    assert e["moneyline_edge_pick"] is None and np.isnan(e["moneyline_edge_ev"])
    assert e["total_edge_pick"] is None
    under = game_edges(ns(model_over_prob=0.42, model_under_prob=0.58))
    assert under["total_edge_pick"] == "Under 6.5" and under["total_edge_side"] == "under"


def test_away_favored_puck_line():
    # The away team gives the goal and a half: home is +1.5.
    e = game_edges(ns(home_spread_line=1.5, home_spread_price=-250, away_spread_price=200,
                      model_home_cover_prob=0.62, model_away_cover_prob=0.38))
    assert e["spread_edge_pick"] == "SJS -1.5" and e["spread_edge_line"] == -1.5
    assert np.isclose(e["spread_edge_ev"], 0.38 * 2.0 - 0.62)


def test_minus_110_is_assumed_only_for_the_total():
    r = ns(over_price=np.nan, under_price=np.nan, model_over_prob=0.58, model_under_prob=0.42,
           home_spread_price=np.nan, away_spread_price=np.nan, model_home_cover_prob=0.9, model_away_cover_prob=0.1,
           home_moneyline=np.nan, away_moneyline=np.nan, model_home_prob=0.99)
    e = game_edges(r)
    assert e["total_edge_pick"] == "Over 6.5" and e["total_edge_price"] == ASSUMED_PRICE
    assert e["spread_edge_pick"] is None and e["moneyline_edge_pick"] is None
    r = SimpleNamespace(**{**vars(r), **e})
    assert edge_cell(r, "total").startswith("Over 6.5 (-110*): EV +10.7%, model 58%")
    assert edge_cell(r, "spread").startswith("no price (model fair MTL -1.5 -900 / SJS +1.5 +900")
    assert edge_cell(r, "moneyline") == "no line yet"


def test_integer_total_pushes_lower_the_risk():
    # 52% over, 8% push, 40% under at -110: EV = 0.52 * 0.909 - 0.40 = +7.3%.
    e = game_edges(ns(total_line=6.0, model_over_prob=0.52, model_under_prob=0.40, model_total_push_prob=0.08))
    assert e["total_edge_pick"] == "Over 6" and np.isclose(e["total_edge_ev"], 0.52 / 1.1 - 0.40)


# ---- model-only chances from the simulator ------------------------------

def test_line_probs_follow_the_line_and_count_pushes():
    sim = simulate([3.4, 2.6], [2.5, 3.3], SimParams(), n_sims=20000, seed=4)
    p = line_probs(sim, [-1.5, 1.5], [6.0, np.nan])
    margin = sim["home"] - sim["away"]
    assert np.isclose(p.loc[0, "model_home_cover_prob"], np.mean(margin[0] >= 2))
    assert np.isclose(p.loc[1, "model_away_cover_prob"], np.mean(margin[1] <= -2))
    assert p.loc[0, "model_spread_push_prob"] == 0.0
    total = sim["home"][0] + sim["away"][0]
    assert np.isclose(p.loc[0, "model_total_push_prob"], np.mean(total == 6)) and p.loc[0, "model_total_push_prob"] > 0
    assert np.isclose(p.loc[0, ["model_over_prob", "model_under_prob", "model_total_push_prob"]].sum(), 1.0)
    assert p.loc[1, ["model_over_prob", "model_under_prob"]].isna().all()
    # Shootout winners get one goal, so a tied regulation game is never a -1.5 cover.
    so = sim["ended"][0] == 2
    assert not (margin[0][so] >= 2).any()


def test_prediction_rows_price_edges_from_the_model_only_chances():
    feats = pd.DataFrame([{k: v for k, v in game().items()}])
    feats["home_goalie_name"], feats["away_goalie_name"] = "B", "A"
    feats["home_goalie_status"], feats["away_goalie_status"] = "known", "known"
    feats["elo_home_prob"] = 0.6
    preds = pd.DataFrame([game(home_win_prob=0.6)]).assign(
        sim_home=3.5, sim_away=2.8, sim_total=6.3, model_home_rate=3.6, model_away_rate=2.6, home_rate=3.5,
        away_rate=2.8)
    model_only = pd.DataFrame({"home_win_prob": [0.66]})
    chances = pd.DataFrame([{c: game()[c] for c in pipeline.LINE_PROB_COLUMNS}])
    rows = prediction_rows(feats, preds, model_only, pd.Timestamp("2026-10-20", tz="UTC"), chances)
    r = rows.iloc[0]
    assert r.home_win_prob == 0.6 and r.model_home_prob == 0.66
    assert r.spread_edge_pick == "MTL -1.5" and r.model_home_cover_prob == 0.45
    assert list(rows.columns) == LOG_COLUMNS


# ---- grading and records -------------------------------------------------

@pytest.mark.parametrize("market,side,line,price,score,expected", [
    ("spread", "home", -1.5, 150, (4, 2), ("W", 1.5)),
    ("spread", "home", -1.5, 150, (3, 2), ("L", -1.0)),
    ("spread", "away", 1.5, -180, (3, 2), ("W", 100 / 180)),
    ("moneyline", "away", np.nan, 170, (2, 3), ("W", 1.7)),
    ("total", "over", 5.5, -110, (3, 3), ("W", 100 / 110)),
    ("total", "under", 6.0, -110, (4, 2), ("P", 0.0)),
    ("total", "under", 6.5, -120, (4, 3), ("L", -1.0)),
])
def test_grade_edge(market, side, line, price, score, expected):
    result, units = grade_edge(market, side, line, price, *score)
    assert result == expected[0] and np.isclose(units, expected[1])


def test_ungraded_and_record():
    assert grade_edge("total", np.nan, 6.5, -110, 3, 2)[0] is None
    assert grade_edge("total", "over", 6.5, -110, np.nan, np.nan)[0] is None
    d = pd.DataFrame({"home_score": [4, 1, 3, np.nan], "away_score": [2, 3, 3, np.nan],
                      "total_edge_side": ["over", "over", "under", "over"], "total_edge_line": [5.5, 5.5, 6.0, 5.5],
                      "total_edge_price": [-110, 100, -110, -110]})
    rec = edge_record(d, "total")
    assert (rec["bets"], rec["wins"], rec["losses"], rec["pushes"]) == (3, 1, 1, 1)
    assert np.isclose(rec["units"], 100 / 110 - 1.0)
    lo, hi = roi_interval(rec["per_bet"])
    assert lo <= rec["roi"] <= hi
    assert all(np.isnan(roi_interval(np.array([]))))


def test_backtest_edge_table_lists_markets_without_prices():
    text = backtest_edge_table({"spread": None, "moneyline": None, "total": None})
    assert "| Puck line | no historical prices |" in text and "| Total | no historical prices |" in text


# ---- log and page --------------------------------------------------------

def test_log_round_trip_with_edges_and_old_logs(tmp_path, monkeypatch):
    path = tmp_path / "log.csv"
    monkeypatch.setattr(pipeline, "LOG_PATH", path)
    rows = add_edges(pd.DataFrame([game(predicted_at=pd.Timestamp("2026-10-20", tz="UTC"), source="live")]))
    rows[LOG_COLUMNS].to_csv(path, index=False, float_format="%.4f")
    back = load_log()
    assert list(back.columns) == LOG_COLUMNS
    assert back.loc[0, "spread_edge_pick"] == "MTL -1.5" and back.loc[0, "spread_edge_price"] == 150
    assert back.loc[0, "home_spread_line"] == -1.5 and pd.isna(back.loc[0, "moneyline_edge_pick"])
    # A log written before the edge columns existed still loads, with them missing.
    old = [c for c in LOG_COLUMNS if c not in EDGE_COLUMNS + pipeline.LINE_PROB_COLUMNS
           and c not in ("home_spread_line", "home_spread_price", "away_spread_price")]
    rows[old].to_csv(path, index=False)
    back = load_log()
    assert list(back.columns) == LOG_COLUMNS and back[EDGE_COLUMNS].isna().all().all()
    r = next(back.itertuples(index=False))
    assert edge_cell(r, "spread") == "no line yet" and edge_cell(r, "moneyline") == "no edge"


def test_upcoming_table_shows_edge_columns():
    rows = add_edges(pd.DataFrame([game(), game(game_id=2, home_moneyline=np.nan, away_moneyline=np.nan,
                                             total_line=np.nan, home_spread_line=np.nan, over_price=np.nan,
                                             model_home_cover_prob=0.45, model_away_cover_prob=0.55)]))
    text = upcoming_table(rows)
    header = text.splitlines()[0]
    assert "| Puck line edge | Moneyline edge | Total edge |" in header and "model pick" not in header
    assert "| SJS +170 / MTL -205 | MTL -1.5 (+150): EV +12.5%, model 45% | no edge | no edge |" in text
    assert "| – | no line yet (model fair MTL -1.5 +120 / SJS +1.5 -120) | no line yet | no line yet |" in text
    assert "assumed -110" not in text
