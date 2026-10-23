import numpy as np
import pandas as pd
from bettingcore import EDGE_MIN_EV, expected_value, market_chance

from nbapredictor import edges
from nbapredictor.backtest import edge_records
from nbapredictor.edges import edge_columns, grade_edge, moved_toward, price_assumed, record
from nbapredictor.pipeline import LOG_COLUMNS, load_log, update_log
from nbapredictor.report import edge_cell, edge_record_table, upcoming_table
from nbapredictor.simulate import SimParams, Simulation, line_probs, simulate


def game(**kw):
    """NYK (home) -4.5 vs BOS with the final prediction's anchored chances and the model's own."""
    row = {"game_id": 1, "home_team": "NYK", "away_team": "BOS", "spread": 4.5, "total": 224.5,
           "home_moneyline": -185.0, "away_moneyline": 155.0,
           "home_spread_price": -110.0, "away_spread_price": -110.0, "over_price": -110.0, "under_price": -110.0,
           "edge_home_ml_prob": 0.64, "edge_home_cover_prob": 0.50, "edge_spread_push_prob": 0.0,
           "edge_over_prob": 0.50, "edge_total_push_prob": 0.0,
           "model_home_prob": 0.66, "model_home_cover_prob": 0.50, "model_spread_push_prob": 0.0,
           "model_over_prob": 0.50, "model_total_push_prob": 0.0}
    row.update(kw)
    return row


def test_three_percent_bar():
    assert expected_value(0.54, 0, -110) > EDGE_MIN_EV > expected_value(0.539, 0, -110)
    assert edge_columns(pd.DataFrame([game(edge_home_cover_prob=0.54)])).iloc[0].spread_edge_pick == "NYK -4.5"
    assert edge_columns(pd.DataFrame([game(edge_home_cover_prob=0.539)])).iloc[0].spread_edge_pick == ""


def test_edges_per_market_stakes_and_the_assumed_price():
    cols = edge_columns(pd.DataFrame([game(edge_home_cover_prob=0.58, edge_over_prob=0.40, edge_home_ml_prob=0.62)]))
    r = cols.iloc[0]
    assert r.spread_edge_pick == "NYK -4.5" and r.spread_edge_side == "home" and r.spread_edge_line == -4.5
    assert np.isclose(r.spread_edge_ev, 0.58 * 100 / 110 - 0.42) and r.spread_edge_prob == 0.58
    assert r.total_edge_pick == "Under 224.5" and np.isclose(r.total_edge_prob, 0.60)
    assert r.moneyline_edge_pick == ""                     # 62% at -185 and 38% at +155 are both below +3%
    assert np.isclose(r.spread_edge_stake + r.total_edge_stake, 3.0, atol=1e-3)   # two edges share the game cap
    assert np.isnan(r.moneyline_edge_stake)
    # The model-only rule reads the model's own chances instead.
    m = edge_columns(pd.DataFrame([game(model_home_cover_prob=0.40)]), chances="model").iloc[0]
    assert m.spread_edge_pick == "BOS +4.5" and m.total_edge_pick == ""
    # Spread and total prices may be assumed at -110; moneylines never are.
    bare = game(home_spread_price=np.nan, away_spread_price=np.nan, over_price=np.nan, under_price=np.nan,
                home_moneyline=np.nan, away_moneyline=np.nan, edge_home_cover_prob=0.40, edge_home_ml_prob=0.9)
    r = pd.concat([pd.DataFrame([bare]), edge_columns(pd.DataFrame([bare]))], axis=1).iloc[0]
    assert r.spread_edge_pick == "BOS +4.5" and r.spread_edge_price == -110 and price_assumed(r, "spread")
    assert r.moneyline_edge_pick == "" and np.isnan(r.moneyline_edge_ev)
    # A push chance comes off the other side: 45% cover, 10% push leaves 45% for the away side.
    r = edge_columns(pd.DataFrame([game(spread=4.0, edge_home_cover_prob=0.45, edge_spread_push_prob=0.10,
                                        away_spread_price=115.0)])).iloc[0]
    assert r.spread_edge_pick == "BOS +4" and np.isclose(r.spread_edge_prob, 0.45)
    assert np.isclose(r.spread_edge_ev, 0.45 * 1.15 - 0.45)


def test_grading_and_staked_record():
    result, units = grade_edge("spread", "home", -4.5, -110, 110, 100)
    assert result == "W" and np.isclose(units, 100 / 110)
    assert grade_edge("spread", "away", 4.0, -110, 110, 106) == ("P", 0.0)
    assert grade_edge("spread", "away", 4.5, -110, 110, 100) == ("L", -1.0)
    result, units = grade_edge("moneyline", "away", np.nan, 155, 100, 104)
    assert result == "W" and np.isclose(units, 1.55)
    assert grade_edge("total", "under", 224.5, -105, 120, 110) == ("L", -1.0)
    assert grade_edge("total", "over", 230, -110, 120, 110) == ("P", 0.0)
    assert grade_edge("total", "over", 230, -110, np.nan, np.nan)[0] is None
    d = pd.DataFrame({"game_id": [1, 2, 3, 4, 5],
                      "spread_edge_pick": ["NYK -4.5", "", "BOS +4", np.nan, "NYK -1"],
                      "spread_edge_side": ["home", "", "away", "", "home"],
                      "spread_edge_line": [-4.5, np.nan, 4.0, np.nan, -1.0],
                      "spread_edge_price": [-110, np.nan, 100, np.nan, -110],
                      "spread_edge_ev": [0.05, np.nan, 0.1, np.nan, 0.05],
                      "spread_edge_stake": [2.0, np.nan, 1.0, np.nan, np.nan],      # last: logged before stakes
                      "home_score": [110, 100, 104, 100, 120], "away_score": [100, 90, 110, 90, 100]})
    r = record(d, "spread")
    assert (r["bets"], r["wins"], r["losses"], r["pushes"]) == (2, 2, 0, 0)
    assert np.isclose(r["staked"], 3.0) and np.isclose(r["units"], 2 * 100 / 110 + 1.0)
    assert np.isclose(r["roi"], r["units"] / 3) and np.isclose(r["expected_roi"], (0.1 + 0.1) / 3)


def test_line_movement_toward_the_edge():
    side = pd.Series(["home", "away", "home", "", "away"])
    first = pd.Series([3.0, 3.0, 3.0, 3.0, 3.0])
    last = pd.Series([4.0, 4.0, 3.0, 5.0, 2.5])
    assert moved_toward(side, first, last) == (2, 3)


def test_line_chances_come_from_the_simulation():
    home = np.array([[110, 104, 100, 120]])
    away = np.array([[100, 100, 104, 110]])
    sim = Simulation(home, away, home - away, np.full(home.shape, 4), np.full(home.shape, 0.25))
    p = line_probs(sim, np.array([4.0]), np.array([210.0]))
    assert np.isclose(p["model_home_cover_prob"][0], 0.5) and np.isclose(p["model_spread_push_prob"][0], 0.25)
    assert np.isclose(p["model_over_prob"][0], 0.25) and np.isclose(p["model_total_push_prob"][0], 0.25)
    none = line_probs(sim, np.array([np.nan]), np.array([np.nan]))
    assert all(np.isnan(v[0]) for v in none.values())
    big = simulate([115.0], [108.0], SimParams(), n_sims=40000, seed=4)
    p = line_probs(big, np.array([7.0]), np.array([223.5]))
    assert abs(p["model_home_cover_prob"][0] + p["model_spread_push_prob"][0] / 2 - 0.5) < 0.04
    assert p["model_spread_push_prob"][0] > 0.01 and p["model_total_push_prob"][0] == 0.0


def test_edge_chances_are_the_market_when_the_blend_is_the_line():
    from nbapredictor.model import ScoreModel
    from test_model import synthetic_features

    f = synthetic_features(n=1200, seed=3)
    m = ScoreModel.fit(f)
    m.margin_weight = m.total_weight = 0.0
    g = f.head(3).assign(spread=[4.5, -2.0, 0.0], total=[224.5, 210.0, 231.5], home_spread_price=-120.0,
                         away_spread_price=100.0, over_price=np.nan, under_price=np.nan,
                         home_moneyline=[-185.0, 110.0, -105.0], away_moneyline=[155.0, -130.0, -115.0])
    _, sim = m.predict(g, n_sims=4000, seed=5)
    e = m.edge_chances(g, sim, n_sims=4000, seed=5)
    q = e["edge_home_cover_prob"] / (1 - e["edge_spread_push_prob"])
    assert np.allclose(q, market_chance(-120, 100))
    assert np.allclose(e["edge_over_prob"] / (1 - e["edge_total_push_prob"]), 0.5)
    assert np.allclose(e["edge_home_ml_prob"], market_chance(g["home_moneyline"], g["away_moneyline"]))
    # Moved toward the home team, the blend moves the home side's chances up.
    m.margin_weight = 0.5
    g2 = g.assign(spread=g["spread"] - 10.0)              # the model likes the home team far more than the line
    _, sim2 = m.predict(g2, n_sims=4000, seed=5)
    e2 = m.edge_chances(g2, sim2, n_sims=4000, seed=5)
    assert (e2["edge_home_cover_prob"] > e["edge_home_cover_prob"]).all()


def log_row(game_id, start, **kw):
    row = {c: np.nan for c in LOG_COLUMNS}
    row.update(game_id=game_id, season=2027, game_type="R", start=start, date=str(start.date()), away_team="BOS",
               home_team="NYK", headline_away=109, headline_home=113, pred_margin=4.0, pred_total=222.0,
               model_margin=5.0, model_total=224.0, home_win_prob=0.6, away_win_prob=0.4, ot_prob=0.06,
               home_low=100, home_high=126, away_low=96, away_high=122,
               predicted_at=pd.Timestamp("2026-10-20 12:00", tz="UTC"), source="live")
    row.update(game(game_id=game_id, **kw))
    edge = edge_columns(pd.DataFrame([row])).iloc[0].to_dict()
    row.update(edge, first_spread=row["spread"], first_spread_edge_side=edge["spread_edge_side"])
    return row


def test_log_round_trip_keeps_edges_and_reads_old_logs(tmp_path, monkeypatch):
    from nbapredictor import pipeline

    start = pd.Timestamp("2026-10-20 23:30", tz="UTC")
    entries = pd.DataFrame([log_row(1, start, edge_home_cover_prob=0.58, home_spread_price=-105.0)])
    monkeypatch.setattr(pipeline, "LOG_PATH", tmp_path / "log.csv")
    entries.to_csv(pipeline.LOG_PATH, index=False)
    back = load_log().iloc[0]
    assert back.spread_edge_pick == "NYK -4.5" and back.home_spread_price == -105
    assert back.first_spread_edge_side == "home" and back.spread_edge_stake > 0
    assert pd.isna(back.moneyline_edge_pick)
    # A log written before the edge columns existed still loads, with them empty.
    old_cols = LOG_COLUMNS[:LOG_COLUMNS.index("periods") + 1]
    entries[old_cols].to_csv(pipeline.LOG_PATH, index=False)
    old = load_log()
    assert list(old.columns) == LOG_COLUMNS and old["spread_edge_pick"].isna().all()
    # The first spread edge is kept while later predictions overwrite the rest.
    later = pd.DataFrame([log_row(1, start, spread=6.5, edge_home_cover_prob=0.40)])
    games = pd.DataFrame({"game_id": [1], "completed": [True], "home_score": [118.0], "away_score": [110.0],
                          "periods": [4.0]})
    merged = update_log(pd.DataFrame([log_row(1, start, edge_home_cover_prob=0.58)]), later, games).iloc[0]
    assert merged.first_spread_edge_side == "home" and merged.spread_edge_side == "away"
    assert merged.spread_edge_pick == "BOS +6.5"


def test_predictions_page_cells_and_season_record():
    start = pd.Timestamp("2026-10-20 23:30", tz="UTC")
    rows = pd.DataFrame([
        log_row(1, start, edge_home_cover_prob=0.58, home_spread_price=np.nan, away_spread_price=np.nan),
        log_row(2, start, edge_home_cover_prob=0.50, edge_home_ml_prob=0.75, edge_over_prob=0.5),
        log_row(3, start, spread=np.nan, total=np.nan, home_moneyline=np.nan, away_moneyline=np.nan,
                edge_home_cover_prob=np.nan, edge_over_prob=np.nan),
    ])
    r1, r2, r3 = rows.itertuples(index=False)
    assert edge_cell(r1, "spread") == "NYK -4.5 (-110*): EV +10.7%, 58%, stake 3.0u"
    assert edge_cell(r2, "spread") == "no edge"
    assert edge_cell(r2, "moneyline").startswith("NYK ML (-185): EV +15.5%, 75%, stake")
    assert all(edge_cell(r3, m) == "no line yet" for m in edges.MARKETS)
    table = upcoming_table(rows)
    assert "| Spread edge | Moneyline edge | Total edge |" in table and "assumed -110" in table
    assert "posted BOS +155 / NYK -185" in table
    done = rows.assign(home_score=[110.0, 100.0, 100.0], away_score=[100.0, 104.0, 99.0],
                       spread=[4.5, 4.5, np.nan], first_spread=[3.5, 4.5, np.nan])
    text = edge_record_table(done)
    s1, s2 = rows.loc[0, "spread_edge_stake"], rows.loc[1, "moneyline_edge_stake"]
    assert f"| Spread | 1 | 1-0-0 | {s1:.1f} | {s1 * 100 / 110:+.2f} | +90.9% |" in text
    assert f"| Moneyline | 1 | 0-1-0 | {s2:.1f} | {-s2:+.2f} | -100.0% |" in text
    assert "1 of 1 games" in text


def test_backtest_edges_assume_minus_110_and_skip_moneylines_at_the_open():
    bt = pd.DataFrame([dict(game(edge_home_cover_prob=0.58, edge_home_ml_prob=0.75), home_score=110, away_score=100,
                            open_spread=3.5, open_total=220.0, open_edge_home_cover_prob=0.6,
                            open_edge_spread_push_prob=0.0, open_edge_over_prob=0.5, open_edge_total_push_prob=0.0,
                            open_edge_home_ml_prob=np.nan, open_model_home_cover_prob=0.3,
                            open_model_spread_push_prob=0.0, open_model_over_prob=0.5, open_model_total_push_prob=0.0)])
    bt = bt.drop(columns=["home_spread_price", "away_spread_price", "over_price", "under_price"])
    close = edge_records(bt)
    assert close["spread"]["bets"] == 1 and close["spread"]["wins"] == 1
    assert np.isclose(close["spread"]["roi"], 100 / 110)
    assert close["moneyline"]["bets"] == 1 and close["total"]["bets"] == 0
    opening = edge_records(bt, "open")
    assert "moneyline" not in opening and opening["spread"]["moved_games"] == 1
    assert opening["spread"]["moved_toward"] == 1.0
    model = edge_records(bt, "open", chances="model")
    assert model["spread"]["losses"] == 1 and model["spread"]["moved_toward"] == 0.0


def test_walk_forward_backtest_carries_both_rules_line_chances():
    from nbapredictor.backtest import predict_seasons
    from test_model import synthetic_features

    f = synthetic_features(n=1600, seed=2, noisy=True)
    f["home_team"], f["away_team"] = "NYK", "BOS"
    f["home_moneyline"], f["away_moneyline"] = -150.0, 130.0
    f["open_spread"], f["open_total"] = f["spread"] - 0.5, np.nan
    bt = predict_seasons(f, [2023], window=3, n_sims=400)
    for col in ("model_home_cover_prob", "model_spread_push_prob", "model_over_prob", "model_total_push_prob",
                "edge_home_cover_prob", "edge_over_prob", "edge_home_ml_prob"):
        assert bt[col].between(0, 1).all()
    assert bt["open_model_over_prob"].isna().all() and bt["open_model_home_cover_prob"].notna().all()
    assert bt["open_edge_over_prob"].isna().all() and bt["open_edge_home_cover_prob"].notna().all()
    close, opening = edge_records(bt, chances="model"), edge_records(bt, "open", chances="model")
    assert close["spread"]["bets"] > 0 and close["moneyline"]["bets"] > 0
    r = close["spread"]
    assert r["wins"] + r["losses"] + r["pushes"] == r["bets"] and r["roi_low"] <= r["roi"] <= r["roi_high"]
    assert opening["total"]["bets"] == 0 and opening["spread"]["moved_games"] > 0
    final = edge_records(bt)
    assert final["spread"]["bets"] <= close["spread"]["bets"]
