import numpy as np
import pandas as pd
import pytest
from bettingcore import EDGE_MIN_EV, median_price

from cfbpredictor import pipeline
from cfbpredictor.backtest import edge_record
from cfbpredictor.edges import ASSUMED_PRICE, edge_columns, game_edges, grade_edge, market_price
from cfbpredictor.model import ScoreModel, market_probs
from cfbpredictor.pipeline import LOG_COLUMNS, prediction_rows, update_log
from cfbpredictor.report import edge_cell, edge_table, upcoming_table
from cfbpredictor.simulate import ScoringModel, simulate


def test_median_price_straddles_even_money():
    assert median_price([-105, 105]) == pytest.approx(100, abs=1)    # not 0
    assert median_price([-110, -110, -120]) == -110
    assert median_price([-280, np.nan, 50]) == -280                  # invalid quotes ignored
    assert np.isnan(median_price([np.nan, None]))
    assert EDGE_MIN_EV == 0.03


def test_minus_110_is_assumed_only_for_spreads_and_totals():
    assert market_price(np.nan, "spread") == (ASSUMED_PRICE, True)
    assert market_price(np.nan, "total") == (ASSUMED_PRICE, True)
    assert market_price(-105, "spread") == (-105.0, False)
    price, assumed = market_price(np.nan, "moneyline")
    assert np.isnan(price) and not assumed


def game(**kw):
    row = {"home_team": "LSU", "away_team": "Auburn", "spread_line": 7.0, "total_line": 50.5,
           "home_spread_price": np.nan, "away_spread_price": np.nan, "over_price": -105.0, "under_price": -115.0,
           "home_moneyline": np.nan, "away_moneyline": np.nan, "home_win_prob": 0.8, "home_ml_prob": 0.8,
           "home_cover_prob": 0.55, "spread_push_prob": 0.05, "over_prob": 0.45, "total_push_prob": 0.0,
           "model_home_win_prob": 0.9, "model_home_cover_prob": 0.30, "model_spread_push_prob": 0.05,
           "model_over_prob": 0.45, "model_total_push_prob": 0.0}
    row.update(kw)
    return row


def test_game_edges_label_each_market():
    e = game_edges(game())
    assert e["spread_edge_pick"] == "LSU -7.0" and e["spread_edge_price"] == -110
    assert e["spread_edge_side"] == "home" and e["spread_edge_line"] == -7.0
    assert e["spread_edge_ev"] == pytest.approx(0.55 * 100 / 110 - 0.40)
    assert e["moneyline_edge_pick"] == "" and np.isnan(e["moneyline_edge_ev"])      # no moneyline posted
    assert e["total_edge_pick"] == ""                                            # under at -115 is EV +2.8%
    assert e["spread_edge_stake"] > 0
    e = game_edges(game(over_prob=0.40, home_moneyline=-250.0, away_moneyline=200.0, home_ml_prob=0.6))
    assert e["total_edge_pick"] == "Under 50.5" and e["total_edge_price"] == -115
    assert e["moneyline_edge_pick"] == "Auburn" and e["moneyline_edge_prob"] == pytest.approx(0.4)
    # The away side's cover chance is what is left after the home cover and the push.
    e = game_edges(game(home_cover_prob=0.35, spread_push_prob=0.05))
    assert e["spread_edge_pick"] == "Auburn +7.0" and e["spread_edge_prob"] == pytest.approx(0.60)
    # The model-only rule reads the model's own chances.
    e = game_edges(game(), prefix="model_")
    assert e["spread_edge_pick"] == "Auburn +7.0" and e["spread_edge_prob"] == pytest.approx(0.65)


def test_no_edges_in_bowls_outside_the_playoff():
    e = game_edges(game(bowl=True))
    assert all(e[f"{m}_edge_pick"] == "" for m in ("spread", "moneyline", "total"))
    assert game_edges(game(bowl=False))["spread_edge_pick"] == "LSU -7.0"
    assert game_edges(game(bowl=np.nan))["spread_edge_pick"] == "LSU -7.0"      # older log rows


def test_grade_edge():
    assert grade_edge("spread", "home", -7.0, -110, 31, 24) == ("P", 0.0)
    assert grade_edge("spread", "home", -6.5, -110, 31, 24) == ("W", pytest.approx(100 / 110))
    assert grade_edge("spread", "away", 6.5, -110, 31, 24) == ("L", -1.0)
    assert grade_edge("moneyline", "away", np.nan, 200, 20, 23) == ("W", 2.0)
    assert grade_edge("total", "over", 50.5, -105, 28, 21) == ("L", -1.0)
    assert grade_edge("total", "under", 50.5, -115, 28, 21) == ("W", pytest.approx(100 / 115))


def test_market_probs_from_simulated_scores():
    home = np.array([[30, 24, 20, 17]])
    away = np.array([[20, 17, 20, 24]])
    p = market_probs(home, away, np.array([7.0]), np.array([np.nan]), ScoringModel())
    assert p["model_home_win_prob"][0] == 0.5
    assert p["model_home_cover_prob"][0] == 0.25 and p["model_spread_push_prob"][0] == 0.25
    assert np.isnan(p["model_over_prob"][0]) and np.isnan(p["model_total_push_prob"][0])


def features(spread=0.0, total=50.0, off_home=1.4, off_away=0.0):
    return pd.DataFrame({
        "game_id": [1], "neutral": [False], "conference_game": [True], "home_division": ["fbs"],
        "away_division": ["fbs"], "off_home": [off_home], "off_away": [off_away], "def_home": [0.0],
        "def_away": [0.0], "off_st_home": [0.0], "off_st_away": [0.0], "def_st_home": [0.0], "def_st_away": [0.0],
        "elo_spread": [0.0], "env_points": [25.0], "home_score": [np.nan], "away_score": [np.nan],
        "spread_line": [spread], "total_line": [total],
    })


def test_edge_chances_follow_the_blend_and_model_chances_ignore_it():
    # Model margin +14, line PK; the blend (half market) expects +7.
    model = ScoreModel(coef={"off": 10.0}, total_coef={}, total_intercept=0.0, margin_weight=0.5, total_weight=0.5)
    f = features()
    out = model.predict(f, n_sims=20000, seed=1).iloc[0]
    assert out.pred_margin == pytest.approx(7.0) and out.pred_model_margin == pytest.approx(14.0)
    home, away = simulate([32.0], [18.0], model.scoring, n_sims=20000, seed=1)
    assert out.model_home_win_prob == pytest.approx(np.mean(home > away), abs=1e-9)
    assert out.model_home_win_prob > 0.75 and out.home_win_prob < out.model_home_win_prob
    assert out.model_home_cover_prob == pytest.approx(out.model_home_win_prob)        # line is PK
    assert 0.3 < out.model_over_prob < 0.7 and 0 < out.model_total_push_prob < 0.1   # total 50 on 50
    # Anchored: an even -110 market at PK, moved by the blend's +7 points.
    no_push = out.home_cover_prob / (1 - out.spread_push_prob)
    assert 0.6 < no_push < out.model_home_cover_prob
    assert out.over_prob / (1 - out.total_push_prob) == pytest.approx(0.5, abs=0.01)   # blended total 50 on 50
    assert np.isnan(out.home_ml_prob)                                          # no moneyline posted
    nolines = model.predict(features(spread=np.nan, total=np.nan), n_sims=2000).iloc[0]
    assert np.isnan(nolines.model_home_cover_prob) and nolines.model_home_win_prob > 0.75
    assert np.isnan(nolines.home_cover_prob)


def test_edge_chances_match_the_market_on_the_line():
    model = ScoreModel(coef={"off": 10.0}, total_coef={}, total_intercept=0.0, margin_weight=0.0, total_weight=0.0)
    f = features(spread=3.0, total=55.5).assign(home_spread_price=-120.0, away_spread_price=100.0,
                                                home_moneyline=-160.0, away_moneyline=135.0)
    out = model.predict(f, n_sims=4000, seed=3).iloc[0]
    from bettingcore import market_chance
    assert out.home_cover_prob / (1 - out.spread_push_prob) == pytest.approx(market_chance(-120, 100))
    assert out.home_ml_prob == pytest.approx(market_chance(-160, 135))


def log_row(game_id=1, **kw):
    row = {c: np.nan for c in LOG_COLUMNS}
    row.update(game_id=game_id, season=2026, week=8, kickoff=pd.Timestamp("2026-10-24 19:30", tz="UTC"),
               start_time_tbd=False, away_team="Auburn", home_team="LSU", away_division="fbs",
               home_division="fbs", neutral=False, pred_home=30.0, pred_away=24.0, pred_margin=6.0,
               pred_total=54.0, model_margin=9.0, model_total=50.0, headline_home=31, headline_away=24,
               home_win_prob=0.65, away_win_prob=0.35, one_score_prob=0.4, home_low=17, home_high=44,
               away_low=10, away_high=38, predicted_at=pd.Timestamp("2026-10-20", tz="UTC"), source="live",
               **{k: v for k, v in game().items() if k not in ("home_team", "away_team", "home_win_prob")})
    row.update(kw)
    row.update(game_edges(row))
    return row


def test_log_round_trip_keeps_edges_and_reads_old_logs(tmp_path, monkeypatch):
    monkeypatch.setattr(pipeline, "LOG_PATH", tmp_path / "log.csv")
    log = update_log(pd.DataFrame([log_row()]), pd.DataFrame(columns=LOG_COLUMNS), pd.DataFrame(
        {"game_id": [1], "completed": [True], "home_score": [31.0], "away_score": [20.0]}))
    log.to_csv(pipeline.LOG_PATH, index=False, float_format="%.4f")
    again = pipeline.load_log().iloc[0]
    assert again.spread_edge_pick == "LSU -7.0" and again.spread_edge_side == "home"
    assert again.spread_edge_ev == pytest.approx(log.iloc[0].spread_edge_ev, abs=1e-4)
    assert again.moneyline_edge_pick == "" and again.home_score == 31.0

    old_columns = [c for c in LOG_COLUMNS if c not in pipeline.PRICE_COLUMNS + pipeline.MODEL_PROB_COLUMNS
                   + pipeline.EDGE_PROBS + edge_columns()]
    log[old_columns].to_csv(pipeline.LOG_PATH, index=False)
    old = pipeline.load_log()
    assert list(old.columns) == LOG_COLUMNS
    assert old.iloc[0].spread_edge_pick == "" and np.isnan(old.iloc[0].over_price)
    assert old.iloc[0].pred_margin == 6.0


def test_prediction_rows_log_prices_chances_and_edges():
    k = pd.Timestamp("2026-10-24 19:30", tz="UTC")
    feats = pd.DataFrame({"game_id": [1, 2], "season": 2026, "week": 8, "kickoff": [k, k], "start_time_tbd": False,
                          "away_team": ["Auburn", "B"], "home_team": ["LSU", "A"], "away_division": "fbs",
                          "home_division": "fbs", "neutral": False, "spread_line": [7.0, np.nan],
                          "total_line": [50.5, np.nan], "elo_spread": 5.0, "line_source": ["ESPN", np.nan],
                          "home_moneyline": [-300.0, np.nan], "away_moneyline": [240.0, np.nan],
                          "home_spread_price": [-105.0, np.nan], "away_spread_price": [-115.0, np.nan],
                          "over_price": [np.nan, np.nan], "under_price": [np.nan, np.nan]})
    preds = pd.DataFrame({"pred_away": [22.0, 20.0], "pred_home": [30.0, 24.0], "pred_margin": [8.0, 4.0],
                          "pred_total": [52.0, 44.0], "pred_model_margin": [11.0, 4.0],
                          "pred_model_total": [49.0, 44.0], "headline_away": [21, 20], "headline_home": [31, 24],
                          "home_win_prob": [0.72, 0.6], "away_win_prob": [0.28, 0.4], "one_score_prob": [0.3, 0.5],
                          "away_low": [10, 10], "away_high": [35, 30], "home_low": [17, 14], "home_high": [42, 35],
                          "home_ml_prob": [0.82, np.nan], "home_cover_prob": [0.62, np.nan],
                          "spread_push_prob": [0.06, np.nan], "over_prob": [0.40, np.nan],
                          "total_push_prob": [0.0, np.nan],
                          "model_home_win_prob": [0.9, 0.6], "model_home_cover_prob": [0.7, np.nan],
                          "model_spread_push_prob": [0.06, np.nan], "model_over_prob": [0.30, np.nan],
                          "model_total_push_prob": [0.0, np.nan]})
    rows = prediction_rows(feats, preds, k - pd.Timedelta(days=2)).set_index("game_id")
    assert rows.loc[1, "spread_edge_pick"] == "LSU -7.0" and rows.loc[1, "spread_edge_price"] == -105
    assert rows.loc[1, "total_edge_pick"] == "Under 50.5" and rows.loc[1, "total_edge_price"] == -110
    assert rows.loc[1, "moneyline_edge_pick"] == "LSU"           # 82% at -300 is EV +9%
    assert rows.loc[2, "spread_edge_pick"] == "" and rows.loc[2, "moneyline_edge_pick"] == ""

    text = upcoming_table(rows.reset_index())
    assert "| Spread edge | Moneyline edge | Total edge |" in text
    assert "LSU -7.0 (-105): EV +" in text and "Under 50.5 (-110*): EV +" in text
    assert "* price not posted; assumed -110" in text
    assert "no line yet (fair: A -150)" in text


def test_edge_cells():
    r = pd.DataFrame([log_row()]).iloc[0:1]
    row = next(r.itertuples(index=False))
    assert edge_cell(row, "spread") == "LSU -7.0 (-110*): EV +10.0%, 55%, stake 2.9u"
    assert edge_cell(row, "moneyline") == "no line yet (fair: LSU -185)"
    row = next(pd.DataFrame([log_row(over_prob=0.48)]).itertuples(index=False))
    assert edge_cell(row, "total") == "no edge"
    row = next(pd.DataFrame([log_row(spread_line=np.nan)]).itertuples(index=False))
    assert edge_cell(row, "spread") == "no line yet"


def test_season_edge_record():
    rows = pd.DataFrame([
        log_row(1, home_score=31.0, away_score=20.0),          # LSU -7 wins at -110
        log_row(2, home_score=27.0, away_score=20.0),          # pushes
        log_row(3, home_score=20.0, away_score=24.0, home_moneyline=-250.0, away_moneyline=200.0,
                home_ml_prob=0.6),                              # Auburn +200 wins
        log_row(4, home_score=40.0, away_score=0.0, source="backfill"),
        {**log_row(5, home_score=40.0, away_score=0.0), "spread_edge_stake": np.nan},  # before stakes: left out
    ])
    text = edge_table(rows)
    assert "| Spread | 3 | 1-1-1 |" in text
    ml = rows.loc[2, "moneyline_edge_stake"]
    assert f"| Moneyline | 1 | 1-0-0 | {ml:.1f} | {2 * ml:+.2f} | +200.0% |" in text
    assert "3 of these edges were priced at an assumed -110" in text


def test_backtest_edge_record_splits_posted_and_assumed_prices():
    bt = pd.DataFrame([
        {**log_row(1, home_score=31.0, away_score=20.0, home_spread_price=-110.0, away_spread_price=-110.0)},
        {**log_row(2, home_score=20.0, away_score=24.0)},
    ])
    bt = bt.drop(columns=edge_columns())
    out = {(r["chances"], r["lines"], r["market"], r["prices"]): r for r in edge_record(bt, n_boot=200)}
    posted, assumed = out[("final", "closing", "spread", "posted")], out[("final", "closing", "spread", "assumed -110")]
    assert posted["games"] == 1 and (posted["wins"], posted["losses"]) == (1, 0)
    assert assumed["games"] == 1 and (assumed["wins"], assumed["losses"]) == (0, 1)
    assert assumed["roi"] == -1.0 and np.isnan(assumed["roi_low"])            # one game: no range
    assert out[("final", "closing", "moneyline", "posted")]["games"] == 0
    # The model-only rule takes the other side of both spreads.
    model = out[("model only", "closing", "spread", "posted")]
    assert (model["wins"], model["losses"]) == (0, 1)


def test_backtest_edges_at_the_opener():
    bt = pd.DataFrame([{**log_row(1, home_score=31.0, away_score=20.0), "spread_open": 6.5, "total_open": 52.0,
                        "open_home_cover_prob": 0.58, "open_spread_push_prob": 0.0, "open_over_prob": 0.5,
                        "open_total_push_prob": 0.0, "open_home_ml_prob": np.nan,
                        "open_model_home_cover_prob": 0.4, "open_model_spread_push_prob": 0.0,
                        "open_model_over_prob": 0.5, "open_model_total_push_prob": 0.0,
                        "open_model_home_win_prob": 0.9}]).drop(columns=edge_columns())
    out = {(r["chances"], r["lines"], r["market"]): r for r in edge_record(bt, n_boot=100)}
    at_open = out[("final", "opening", "spread")]
    assert at_open["prices"] == "assumed -110" and (at_open["bets"], at_open["wins"]) == (1, 1)   # LSU -6.5
    assert out[("model only", "opening", "spread")]["losses"] == 1                               # Auburn +6.5
    assert out[("final", "opening", "total")]["bets"] == 0
