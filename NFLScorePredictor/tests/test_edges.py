import numpy as np
import pandas as pd
import pytest

from nflpredictor import pipeline
from nflpredictor.backtest import closing_edges, edge_summary, midweek_edges
from nflpredictor.data import prepare_games
from nflpredictor.edges import (
    EDGE_MIN_EV, best_side, decimal_odds, edge_record, expected_value, fair_american, game_edges, grade_edge,
    implied_prob,
)
from nflpredictor.model import ScoreModel
from nflpredictor.pipeline import LOG_COLUMNS, update_log
from nflpredictor.report import edge_cell, edge_table, line_moves, upcoming_table
from nflpredictor.simulate import ScoringModel, line_probs

from test_model import synthetic_features
from test_pipeline import entry, schedule


def game(**kw):
    """One logged game, KC (home) -3 vs LV, with model-only chances and posted prices."""
    r = {
        "home_team": "KC", "away_team": "LV", "spread_line": 3.0, "total_line": 44.5,
        "home_spread_price": -110.0, "away_spread_price": -110.0, "over_price": -110.0, "under_price": -110.0,
        "home_moneyline": -160.0, "away_moneyline": 140.0,
        "model_home_win_prob": 0.60, "model_away_win_prob": 0.39, "model_tie_prob": 0.01,
        "model_home_cover_prob": 0.46, "model_spread_push_prob": 0.08,
        "model_over_prob": 0.50, "model_total_push_prob": 0.0,
    }
    r.update(kw)
    return r


def test_odds_conversions():
    assert decimal_odds(-110) == pytest.approx(1 + 100 / 110)
    assert decimal_odds(150) == 2.5
    assert decimal_odds(100) == 2.0
    assert implied_prob(-110) == pytest.approx(110 / 210)
    assert implied_prob(300) == 0.25
    assert fair_american(0.6) == -150 and fair_american(0.4) == 150


def test_expected_value_counts_pushes_as_stake_returned():
    assert expected_value(0.5, 0.0, 100) == 0.0
    assert expected_value(110 / 210, 0.0, -110) == pytest.approx(0.0)
    # 48% win, 8% push, 44% loss at -110: 0.48 * 100/110 - 0.44
    assert expected_value(0.48, 0.08, -110) == pytest.approx(0.48 / 1.1 - 0.44)
    assert expected_value(0.40, 0.0, 200) == pytest.approx(0.2)


def test_best_side_needs_three_percent():
    # 54% at -110 is EV +3.1%; 53.9% at -110 is just under the bar.
    assert expected_value(0.54, 0, -110) > EDGE_MIN_EV > expected_value(0.539, 0, -110)
    pick = best_side([("A", "home", -3.0, -110, False, 0.54, 0.0), ("B", "away", 3.0, -110, False, 0.46, 0.0)])
    assert pick.label == "A" and pick.side == "home" and pick.ev == pytest.approx(0.54 / 1.1 - 0.46)
    assert best_side([("A", "home", -3.0, -110, False, 0.539, 0.0),
                      ("B", "away", 3.0, -110, False, 0.461, 0.0)]) is None
    # The higher EV wins, not the higher probability.
    pick = best_side([("fav", "home", np.nan, -300, False, 0.74, 0.0), ("dog", "away", np.nan, 300, False, 0.26, 0.0)])
    assert pick.label == "dog" and pick.ev == pytest.approx(0.04)
    # Sides without a price are skipped.
    assert best_side([("A", "home", np.nan, np.nan, False, 0.9, 0.0)]) is None


def test_game_edges_pick_sides_and_lines():
    e = game_edges(game(model_home_cover_prob=0.30, model_spread_push_prob=0.08,     # LV +3 wins 62%
                        model_over_prob=0.60, model_home_win_prob=0.5, model_away_win_prob=0.49))
    assert e["spread_edge_pick"] == "LV +3.0" and e["spread_edge_side"] == "away" and e["spread_edge_line"] == 3.0
    assert e["spread_edge_prob"] == pytest.approx(0.62)
    assert e["total_edge_pick"] == "Over 44.5" and e["total_edge_line"] == 44.5
    assert e["moneyline_edge_pick"] == "LV" and e["moneyline_edge_price"] == 140
    assert e["moneyline_edge_ev"] == pytest.approx(0.49 * 1.4 - 0.5)              # the 1% tie is refunded
    none = game_edges(game())
    assert none["spread_edge_pick"] == "" and np.isnan(none["spread_edge_ev"])
    home = game_edges(game(spread_line=-2.5, model_home_cover_prob=0.60, model_spread_push_prob=0.0))
    assert home["spread_edge_pick"] == "KC +2.5" and home["spread_edge_line"] == 2.5


def test_assumed_price_only_for_spread_and_total():
    r = game(home_spread_price=np.nan, away_spread_price=np.nan, over_price=np.nan, under_price=np.nan,
             home_moneyline=np.nan, away_moneyline=np.nan, model_home_cover_prob=0.60, model_spread_push_prob=0.0,
             model_over_prob=0.40, model_home_win_prob=0.9, model_away_win_prob=0.09)
    e = game_edges(r)
    assert e["spread_edge_pick"] == "KC -3.0" and e["spread_edge_price"] == -110
    assert e["total_edge_pick"] == "Under 44.5" and e["total_edge_price"] == -110
    assert e["moneyline_edge_pick"] == ""                                        # never assumed
    row = pd.Series({**r, **e, "kickoff": pd.NaT})
    assert edge_cell(row, "spread") == "KC -3.0 (-110*): EV +14.5%, model 60%"
    assert edge_cell(row, "moneyline") == "no line yet"
    posted = pd.Series({**game(model_home_cover_prob=0.6, model_spread_push_prob=0.0),
                        **game_edges(game(model_home_cover_prob=0.6, model_spread_push_prob=0.0))})
    assert edge_cell(posted, "spread") == "KC -3.0 (-110): EV +14.5%, model 60%"
    assert edge_cell(posted, "total") == "no edge"
    no_line = pd.Series({**game(spread_line=np.nan, total_line=np.nan), **game_edges(game(spread_line=np.nan))})
    assert edge_cell(no_line, "spread") == "no line yet"


def test_grading():
    assert grade_edge("spread", "home", -3.0, -110, 24, 20) == ("win", pytest.approx(100 / 110))
    assert grade_edge("spread", "home", -3.0, -110, 23, 20) == ("push", 0.0)
    assert grade_edge("spread", "away", 3.0, -110, 23, 21) == ("win", pytest.approx(100 / 110))
    assert grade_edge("spread", "away", 2.5, 120, 24, 21) == ("loss", -1.0)
    assert grade_edge("moneyline", "away", np.nan, 140, 17, 20) == ("win", pytest.approx(1.4))
    assert grade_edge("moneyline", "home", np.nan, -160, 20, 20) == ("push", 0.0)
    assert grade_edge("total", "over", 44.5, -105, 24, 21) == ("win", pytest.approx(100 / 105))
    assert grade_edge("total", "under", 44.0, -110, 24, 20) == ("push", 0.0)
    df = pd.DataFrame([
        {"spread_edge_pick": "KC -3.0", "spread_edge_side": "home", "spread_edge_line": -3.0,
         "spread_edge_price": -110, "home_score": 24, "away_score": 20},
        {"spread_edge_pick": "LV +3.0", "spread_edge_side": "away", "spread_edge_line": 3.0,
         "spread_edge_price": 100, "home_score": 27, "away_score": 20},
        {"spread_edge_pick": "KC -3.0", "spread_edge_side": "home", "spread_edge_line": -3.0,
         "spread_edge_price": -110, "home_score": 23, "away_score": 20},
        {"spread_edge_pick": np.nan, "spread_edge_side": np.nan, "spread_edge_line": np.nan,
         "spread_edge_price": np.nan, "home_score": 30, "away_score": 0},
        {"spread_edge_pick": "KC -3.0", "spread_edge_side": "home", "spread_edge_line": -3.0,
         "spread_edge_price": -110, "home_score": np.nan, "away_score": np.nan},           # not played yet
    ])
    rec = edge_record(df, "spread")
    assert (rec["bets"], rec["wins"], rec["losses"], rec["pushes"]) == (3, 1, 1, 1)
    assert rec["units"] == pytest.approx(100 / 110 - 1) and rec["roi"] == pytest.approx((100 / 110 - 1) / 3)
    table = edge_table(df.assign(moneyline_edge_pick=np.nan, total_edge_pick=np.nan))
    assert "| Spread | 3 | 1-1-1 | -0.09 | -3.0% |" in table
    assert "| Moneyline | 0 | 0-0-0 | +0.00 | – |" in table


def test_line_probs_count_wins_covers_and_pushes():
    home = np.array([[24, 20, 17, 27]])
    away = np.array([[21, 20, 20, 10]])
    p = line_probs(home, away, ScoringModel(), [3.0], [41.0]).iloc[0]
    assert (p.home_win_prob, p.tie_prob, p.away_win_prob) == (0.5, 0.25, 0.25)
    assert p.home_cover_prob == 0.25 and p.spread_push_prob == 0.25        # 27-10 covers, 24-21 pushes
    assert p.over_prob == 0.25 and p.total_push_prob == 0.0                 # totals 45, 40, 37, 37 vs 41
    missing = line_probs(home, away, ScoringModel(), [np.nan], [np.nan]).iloc[0]
    assert np.isnan(missing.home_cover_prob) and np.isnan(missing.over_prob) and missing.home_win_prob == 0.5


def test_model_only_chances_ignore_the_market():
    f = synthetic_features(n=600)
    m = ScoreModel.fit(f)
    m.margin_weight = m.total_weight = 0.0           # final prediction = the line
    g = f.head(2).copy()
    g["spread_line"], g["total_line"] = [-10.0, 10.0], [30.0, 60.0]
    g[["off_home", "off_away", "def_home", "def_away"]] = 0.0     # model: an even game near 44 points
    pred = m.predict(g, n_sims=20000)
    assert pred["pred_margin"].tolist() == [-10.0, 10.0]
    own = m.model_only_means(g)
    assert np.allclose(pred["pred_model_margin"], own["margin"]) and abs(own["margin"][0]) < 3
    # The model sees a near-even game, so the home side is likely to beat -10 / +10 lines one way or the other.
    assert pred.loc[0, "model_home_cover_prob"] > 0.7 > 0.3 > pred.loc[1, "model_home_cover_prob"]
    assert pred.loc[0, "model_over_prob"] > 0.8 and pred.loc[1, "model_over_prob"] < 0.2
    assert 0.3 < pred.loc[0, "model_home_win_prob"] < 0.7 and pred.loc[0, "home_win_prob"] < 0.3
    for _, r in pred.iterrows():
        assert r.model_home_win_prob + r.model_away_win_prob + r.model_tie_prob == pytest.approx(1)


def test_prepare_games_keeps_posted_prices():
    raw = pd.DataFrame([{
        "game_id": "2026_07_LV_KC", "season": 2026, "week": 7, "game_type": "REG", "gameday": "2026-10-25",
        "gametime": "13:00", "home_team": "KC", "away_team": "OAK", "location": "Home", "div_game": 1,
        "home_score": np.nan, "away_score": np.nan, "home_rest": 7, "away_rest": 7,
        "spread_line": 3.5, "home_spread_odds": -105, "away_spread_odds": -115, "total_line": 44.5,
        "over_odds": -110, "under_odds": -110, "home_moneyline": -180, "away_moneyline": 150,
    }])
    g = prepare_games(raw).iloc[0]
    assert (g.home_spread_odds, g.away_spread_odds, g.home_moneyline, g.away_team) == (-105, -115, -180, "LV")
    old = prepare_games(raw.drop(columns=["over_odds", "under_odds"])).iloc[0]
    assert np.isnan(old.over_odds) and np.isnan(old.under_odds)


def test_log_round_trip_keeps_edges_and_reads_old_logs(tmp_path, monkeypatch):
    monkeypatch.setattr(pipeline, "LOG_PATH", tmp_path / "log.csv")
    g = schedule()
    e = game_edges(game(model_home_cover_prob=0.30))
    row = entry("b", g.kickoff[1], **game(), **e, first_spread_edge_side="away")
    pd.DataFrame([row])[LOG_COLUMNS].to_csv(pipeline.LOG_PATH, index=False)
    back = pipeline.load_log().iloc[0]
    assert back.spread_edge_pick == "LV +3.0" and back.spread_edge_side == "away"
    assert back.spread_edge_ev == pytest.approx(e["spread_edge_ev"]) and back.first_spread_edge_side == "away"
    assert pd.isna(back.total_edge_pick) and back.home_moneyline == -160
    # A log written before edges existed loads with the new columns empty.
    old_cols = [c for c in LOG_COLUMNS if "edge" not in c and not c.startswith("model_") and "price" not in c
                and c not in ("home_moneyline", "away_moneyline")] + ["model_margin", "model_total"]
    pd.DataFrame([entry("a", g.kickoff[0])])[list(dict.fromkeys(old_cols))].to_csv(pipeline.LOG_PATH, index=False)
    old = pipeline.load_log()
    assert list(old.columns) == LOG_COLUMNS
    assert old[["spread_edge_pick", "model_home_cover_prob", "first_spread_edge_side"]].isna().all().all()
    # Old rows grade as no edges; a new prediction with text edges merges into the old log.
    later = pd.DataFrame([entry("b", g.kickoff[1], **game(), **e, first_spread_edge_side="away",
                                first_spread_line=3.0, first_predicted_at=pd.Timestamp("2026-10-15", tz="UTC"))])
    later = later[LOG_COLUMNS]
    merged = update_log(old, later, g)
    assert edge_record(merged, "spread")["bets"] == 0
    assert merged.set_index("game_id").loc["b", "spread_edge_pick"] == "LV +3.0"


def test_first_spread_edge_is_frozen_and_line_moves_measured():
    g = schedule()
    first = pd.DataFrame([entry("a", g.kickoff[0], spread_line=2.5, first_spread_line=2.5,
                                first_spread_edge_side="home", spread_edge_side="home")])[LOG_COLUMNS]
    later = pd.DataFrame([entry("a", g.kickoff[0], spread_line=3.5, first_spread_line=3.5,
                                first_spread_edge_side=np.nan, spread_edge_side=np.nan)])[LOG_COLUMNS]
    row = update_log(first, later, g).set_index("game_id").loc["a"]
    assert row.first_spread_edge_side == "home" and row.first_spread_line == 2.5
    # Home edge at +2.5, line moved to +3.5 (home favored more): toward the edge.
    log = pd.DataFrame({"first_spread_edge_side": ["home", "away", "away", np.nan],
                        "first_spread_line": [2.5, 2.5, 2.5, 1.0], "spread_line": [3.5, 3.5, 2.5, 7.0]})
    assert line_moves(log) == (1, 2)


def test_upcoming_table_shows_edge_columns():
    g = schedule()
    r = entry("b", g.kickoff[1], **game(model_home_cover_prob=0.30), headline_away=20, headline_home=23,
              one_score_prob=0.5, away_qb="A", home_qb="B", wind_forecast=np.nan)
    r.update(game_edges(r))
    text = upcoming_table(pd.DataFrame([r]))
    assert "| Spread edge | Moneyline edge | Total edge |" in text
    assert "| LV +3.0 (-110): EV +26.4%, model 62% | no edge | no edge |" in text
    assert "Model pick" not in text


def test_backtest_edges_at_closing_and_midweek_lines():
    df = pd.DataFrame([{**game(model_home_cover_prob=0.62, model_spread_push_prob=0.0, model_over_prob=0.62),
                        "home_spread_odds": -110.0, "away_spread_odds": -110.0, "over_odds": -110.0,
                        "under_odds": -110.0, "home_score": 27.0, "away_score": 20.0, "game_id": "g",
                        "midweek_line": 2.5, "midweek_home_cover_prob": 0.65, "midweek_spread_push_prob": 0.0}])
    df = df.drop(columns=["home_spread_price", "away_spread_price", "over_price", "under_price"])
    closing = closing_edges(df)
    assert closing.loc[0, "spread_edge_pick"] == "KC -3.0" and closing.loc[0, "total_edge_pick"] == "Over 44.5"
    rec = edge_summary(closing, "spread")
    assert (rec["wins"], rec["roi"]) == (1, pytest.approx(100 / 110)) and rec["roi_low"] == rec["roi_high"]
    mid = midweek_edges(df)
    assert mid.loc[0, "spread_edge_pick"] == "KC -2.5" and mid.loc[0, "closing_line"] == 3.0
    assert "total_edge_pick" not in mid
    rec = edge_summary(mid, "spread", closing_col="closing_line")
    assert rec["moved_toward"] == 1.0 and rec["moved_games"] == 1     # 2.5 -> 3.0 toward KC
