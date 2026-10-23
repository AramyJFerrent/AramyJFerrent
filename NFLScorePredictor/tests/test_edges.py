import numpy as np
import pandas as pd
import pytest
from bettingcore import EDGE_MIN_EV, expected_value, kelly_stake

from nflpredictor import pipeline
from nflpredictor.backtest import closing_edges, early_edges, edge_summary
from nflpredictor.data import prepare_games
from nflpredictor.edges import edge_record, game_edges, grade_edge
from nflpredictor.model import ScoreModel
from nflpredictor.pipeline import LOG_COLUMNS, update_log
from nflpredictor.report import edge_cell, edge_table, line_moves, upcoming_table
from nflpredictor.simulate import ScoringModel, line_probs

from test_model import synthetic_features
from test_pipeline import entry, schedule


def game(**kw):
    """One logged game, KC (home) -3 vs LV, with the final prediction's chances and posted prices."""
    r = {
        "home_team": "KC", "away_team": "LV", "spread_line": 3.0, "total_line": 44.5,
        "home_spread_price": -110.0, "away_spread_price": -110.0, "over_price": -110.0, "under_price": -110.0,
        "home_moneyline": -160.0, "away_moneyline": 140.0,
        "home_win_prob": 0.60, "away_win_prob": 0.39, "tie_prob": 0.01,
        "home_ml_prob": 0.60, "away_ml_prob": 0.39,
        "home_cover_prob": 0.46, "spread_push_prob": 0.08, "over_prob": 0.50, "total_push_prob": 0.0,
    }
    r.update(kw)
    return r


def test_edges_need_three_percent():
    # 54% at -110 is EV +3.1%; 53.9% is just under the bar.
    assert expected_value(0.54, 0, -110) > EDGE_MIN_EV > expected_value(0.539, 0, -110)
    assert game_edges(game(home_cover_prob=0.54, spread_push_prob=0.0))["spread_edge_pick"] == "KC -3.0"
    assert game_edges(game(home_cover_prob=0.539, spread_push_prob=0.0))["spread_edge_pick"] == ""


def test_game_edges_pick_sides_lines_and_stakes():
    e = game_edges(game(home_cover_prob=0.30, spread_push_prob=0.08,                # LV +3 wins 62%
                        over_prob=0.60, home_ml_prob=0.5, away_ml_prob=0.49))
    assert e["spread_edge_pick"] == "LV +3.0" and e["spread_edge_side"] == "away" and e["spread_edge_line"] == 3.0
    assert e["spread_edge_prob"] == pytest.approx(0.62)
    assert e["total_edge_pick"] == "Over 44.5" and e["total_edge_line"] == 44.5
    assert e["moneyline_edge_pick"] == "LV" and e["moneyline_edge_price"] == 140
    assert e["moneyline_edge_ev"] == pytest.approx(0.49 * 1.4 - 0.5)              # the 1% tie is refunded
    # Three big edges on one game share the 3-unit cap.
    assert e["spread_edge_stake"] + e["moneyline_edge_stake"] + e["total_edge_stake"] == pytest.approx(3.0, abs=1e-3)
    one = game_edges(game(home_cover_prob=0.56, spread_push_prob=0.0))
    assert one["spread_edge_stake"] == pytest.approx(kelly_stake(0.56, 0.0, -110), abs=1e-4)
    none = game_edges(game())
    assert none["spread_edge_pick"] == "" and np.isnan(none["spread_edge_ev"]) and np.isnan(none["spread_edge_stake"])
    home = game_edges(game(spread_line=-2.5, home_cover_prob=0.60, spread_push_prob=0.0))
    assert home["spread_edge_pick"] == "KC +2.5" and home["spread_edge_line"] == 2.5


def test_assumed_price_only_for_spread_and_total():
    r = game(home_spread_price=np.nan, away_spread_price=np.nan, over_price=np.nan, under_price=np.nan,
             home_moneyline=np.nan, away_moneyline=np.nan, home_cover_prob=0.60, spread_push_prob=0.0,
             over_prob=0.40, home_ml_prob=0.9, away_ml_prob=0.09)
    e = game_edges(r)
    assert e["spread_edge_pick"] == "KC -3.0" and e["spread_edge_price"] == -110
    assert e["total_edge_pick"] == "Under 44.5" and e["total_edge_price"] == -110
    assert e["moneyline_edge_pick"] == ""                                        # never assumed
    row = pd.Series({**r, **e, "kickoff": pd.NaT})
    assert edge_cell(row, "spread") == "KC -3.0 (-110*): EV +14.5%, 60%, stake 1.5u"
    assert edge_cell(row, "moneyline") == "no line yet"
    posted = pd.Series({**game(home_cover_prob=0.6, spread_push_prob=0.0),
                        **game_edges(game(home_cover_prob=0.6, spread_push_prob=0.0))})
    assert edge_cell(posted, "spread") == "KC -3.0 (-110): EV +14.5%, 60%, stake 3.0u"
    assert edge_cell(posted, "total") == "no edge"
    no_line = pd.Series({**game(spread_line=np.nan, total_line=np.nan), **game_edges(game(spread_line=np.nan))})
    assert edge_cell(no_line, "spread") == "no line yet"


def test_grading_and_record():
    assert grade_edge("spread", "home", -3.0, -110, 24, 20) == ("W", pytest.approx(100 / 110))
    assert grade_edge("spread", "home", -3.0, -110, 23, 20) == ("P", 0.0)
    assert grade_edge("spread", "away", 3.0, -110, 23, 21) == ("W", pytest.approx(100 / 110))
    assert grade_edge("spread", "away", 2.5, 120, 24, 21) == ("L", -1.0)
    assert grade_edge("moneyline", "away", np.nan, 140, 17, 20) == ("W", pytest.approx(1.4))
    assert grade_edge("moneyline", "home", np.nan, -160, 20, 20) == ("P", 0.0)
    assert grade_edge("total", "over", 44.5, -105, 24, 21) == ("W", pytest.approx(100 / 105))
    assert grade_edge("total", "under", 44.0, -110, 24, 20) == ("P", 0.0)

    def bet(gid, side, line, price, stake, home, away, ev=0.05):
        return {"game_id": gid, "spread_edge_pick": f"{side} {line}", "spread_edge_side": side,
                "spread_edge_line": line, "spread_edge_price": price, "spread_edge_ev": ev,
                "spread_edge_stake": stake, "home_score": home, "away_score": away}
    df = pd.DataFrame([
        bet("a", "home", -3.0, -110, 2.0, 24, 20),                  # win 2 x 0.909
        bet("b", "away", 3.0, 100, 1.0, 27, 20),                    # loss
        bet("c", "home", -3.0, -110, 1.0, 23, 20),                  # push
        {**bet("d", "home", -3.0, -110, np.nan, 30, 0)},            # logged before stakes: left out
        bet("e", "home", -3.0, -110, 1.0, np.nan, np.nan),          # not played yet
        {"game_id": "f", "spread_edge_pick": np.nan, "spread_edge_side": np.nan, "spread_edge_line": np.nan,
         "spread_edge_price": np.nan, "spread_edge_ev": np.nan, "spread_edge_stake": np.nan,
         "home_score": 30, "away_score": 0},
    ])
    rec = edge_record(df, "spread")
    assert (rec["bets"], rec["wins"], rec["losses"], rec["pushes"]) == (3, 1, 1, 1)
    assert rec["staked"] == 4.0 and rec["units"] == pytest.approx(2 * 100 / 110 - 1)
    assert rec["roi"] == pytest.approx((2 * 100 / 110 - 1) / 4) and rec["expected_roi"] == pytest.approx(0.05)
    table = edge_table(df.assign(moneyline_edge_pick=np.nan, total_edge_pick=np.nan))
    assert "| Spread | 3 | 1-1-1 | 4.0 | +0.82 | +20.5% | +5.0% |" in table
    assert "| Moneyline | 0 | 0-0-0 | 0.0 | +0.00 | – | – |" in table


def test_line_probs_count_wins_covers_and_pushes():
    home = np.array([[24, 20, 17, 27]])
    away = np.array([[21, 20, 20, 10]])
    p = line_probs(home, away, ScoringModel(), [3.0], [41.0]).iloc[0]
    assert (p.home_win_prob, p.tie_prob, p.away_win_prob) == (0.5, 0.25, 0.25)
    assert p.home_cover_prob == 0.25 and p.spread_push_prob == 0.25        # 27-10 covers, 24-21 pushes
    assert p.over_prob == 0.25 and p.total_push_prob == 0.0                 # totals 45, 40, 37, 37 vs 41
    missing = line_probs(home, away, ScoringModel(), [np.nan], [np.nan]).iloc[0]
    assert np.isnan(missing.home_cover_prob) and np.isnan(missing.over_prob) and missing.home_win_prob == 0.5


def test_final_chances_follow_the_blend_and_model_chances_ignore_it():
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
    # On the lines with no prices, the anchored chances are an even -110 market's: no edge.
    assert np.allclose(pred["home_cover_prob"], 0.5 * (1 - pred["spread_push_prob"]))
    assert np.allclose(pred["over_prob"], 0.5 * (1 - pred["total_push_prob"]))
    assert pred[["home_ml_prob", "away_ml_prob"]].isna().all().all()          # no moneylines posted
    # The model alone sees a near-even game, far from -10 / +10 and 30 / 60.
    assert pred.loc[0, "model_home_cover_prob"] > 0.7 > 0.3 > pred.loc[1, "model_home_cover_prob"]
    assert pred.loc[0, "model_over_prob"] > 0.8 and pred.loc[1, "model_over_prob"] < 0.2
    assert 0.3 < pred.loc[0, "model_home_win_prob"] < 0.7 and pred.loc[0, "home_win_prob"] < 0.3
    for _, r in pred.iterrows():
        assert r.model_home_win_prob + r.model_away_win_prob + r.model_tie_prob == pytest.approx(1)


def test_blend_uses_whichever_line_is_posted():
    f = synthetic_features(n=600)
    m = ScoreModel.fit(f)
    m.margin_weight, m.total_weight = 0.2, 0.0
    g = f.head(1).copy()
    g["spread_line"], g["total_line"] = 7.0, np.nan
    own = m.model_means(g)
    means = m.means(g)
    assert means["margin"][0] == pytest.approx(0.2 * own["margin"][0] + 0.8 * 7.0)
    assert means["total"][0] == pytest.approx(own["total"][0])


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
    e = game_edges(game(home_cover_prob=0.30))
    row = entry("b", g.kickoff[1], **game(), **e, first_spread_edge_side="away")
    pd.DataFrame([row])[LOG_COLUMNS].to_csv(pipeline.LOG_PATH, index=False)
    back = pipeline.load_log().iloc[0]
    assert back.spread_edge_pick == "LV +3.0" and back.spread_edge_side == "away"
    assert back.spread_edge_ev == pytest.approx(e["spread_edge_ev"]) and back.first_spread_edge_side == "away"
    assert back.spread_edge_stake == pytest.approx(e["spread_edge_stake"])
    assert pd.isna(back.total_edge_pick) and back.home_moneyline == -160
    # A log written before edges existed loads with the new columns empty.
    old_cols = [c for c in LOG_COLUMNS if "edge" not in c and not c.startswith("model_") and "price" not in c
                and not c.endswith("_prob") and c not in ("home_moneyline", "away_moneyline")] \
        + ["model_margin", "model_total", "home_win_prob", "away_win_prob", "tie_prob", "one_score_prob"]
    pd.DataFrame([entry("a", g.kickoff[0])])[list(dict.fromkeys(old_cols))].to_csv(pipeline.LOG_PATH, index=False)
    old = pipeline.load_log()
    assert list(old.columns) == LOG_COLUMNS
    assert old[["spread_edge_pick", "home_cover_prob", "spread_edge_stake", "first_spread_edge_side"]].isna().all().all()
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
    r = entry("b", g.kickoff[1], **game(home_cover_prob=0.30), headline_away=20, headline_home=23,
              one_score_prob=0.5, away_qb="A", home_qb="B", wind_forecast=np.nan)
    r.update(game_edges(r))
    text = upcoming_table(pd.DataFrame([r]))
    assert "| Spread edge | Moneyline edge | Total edge |" in text
    assert "| LV +3.0 (-110): EV +26.4%, 62%, stake 3.0u | no edge | no edge |" in text


def test_backtest_edges_at_closing_and_early_lines():
    df = pd.DataFrame([{**game(home_cover_prob=0.62, spread_push_prob=0.0, over_prob=0.62),
                        "model_home_cover_prob": 0.40, "model_spread_push_prob": 0.0, "model_over_prob": 0.5,
                        "model_total_push_prob": 0.0, "model_home_win_prob": 0.6, "model_away_win_prob": 0.39,
                        "model_tie_prob": 0.01,
                        "home_spread_odds": -110.0, "away_spread_odds": -110.0, "over_odds": -110.0,
                        "under_odds": -110.0, "home_score": 27.0, "away_score": 20.0, "game_id": "g",
                        "midweek_line": 2.5, "midweek_home_cover_prob": 0.65, "midweek_spread_push_prob": 0.0,
                        "midweek_model_home_cover_prob": 0.30, "midweek_model_spread_push_prob": 0.0,
                        "open_line": 2.0, "open_total": 46.0, "open_home_cover_prob": 0.5, "open_spread_push_prob": 0.0,
                        "open_over_prob": 0.40, "open_total_push_prob": 0.0, "open_model_home_cover_prob": 0.5,
                        "open_model_spread_push_prob": 0.0, "open_model_over_prob": 0.6,
                        "open_model_total_push_prob": 0.0}])
    df = df.drop(columns=["home_spread_price", "away_spread_price", "over_price", "under_price"])
    closing = closing_edges(df)
    assert closing.loc[0, "spread_edge_pick"] == "KC -3.0" and closing.loc[0, "total_edge_pick"] == "Over 44.5"
    rec = edge_summary(closing, "spread")
    assert (rec["wins"], rec["roi"]) == (1, pytest.approx(100 / 110)) and np.isnan(rec["roi_low"])
    # The model-only rule reads the model's own chances: it takes the other side.
    assert closing_edges(df, "model").loc[0, "spread_edge_pick"] == "LV +3.0"
    mid = early_edges(df)
    assert mid.loc[0, "spread_edge_pick"] == "KC -2.5" and mid.loc[0, "closing_line"] == 3.0
    assert "total_edge_pick" not in mid
    rec = edge_summary(mid, "spread", closing_col="closing_line")
    assert rec["moved_toward"] == 1.0 and rec["moved_games"] == 1     # 2.5 -> 3.0 toward KC
    assert early_edges(df, "midweek", "model").loc[0, "spread_edge_pick"] == "LV +2.5"
    # The opening line has a total too: Under 46 at 60% (assumed -110), and the total then fell to 44.5.
    opening = early_edges(df, "open")
    assert opening.loc[0, "spread_edge_pick"] == "" and opening.loc[0, "total_edge_pick"] == "Under 46"
    assert opening.loc[0, "closing_total"] == 44.5 and opening.loc[0, "over_price"] != opening.loc[0, "over_price"]
    rec = edge_summary(opening, "total", closing_col="closing_total")
    assert (rec["bets"], rec["losses"], rec["moved_toward"]) == (1, 1, 1.0)          # 47 points: the under lost
    assert early_edges(df, "open", "model").loc[0, "total_edge_pick"] == "Over 46"


def test_opening_lines_drop_archive_sign_errors(monkeypatch):
    from bettingcore import sbr

    from nflpredictor import backtest

    def row(day, home, away, hs, as_, spread, total):
        return {"season": 2021, "date": day, "home_team": home, "away_team": away, "home_final": hs,
                "away_final": as_, "home_open_spread": spread, "home_close_spread": spread, "open_over_under": total,
                "close_over_under": total, "home_close_ml": -150, "away_close_ml": 130}
    rows = [row(20211114, "Jets", "Bills", 17, 45, -13.5, 48.5),       # Jets -13.5, but Bills -13 at the close
            row(20211114, "Packers", "Seahawks", 17, 0, -2.5, 49.5),    # Packers -3 at the close
            row(20211114, "Colts", "Jaguars", 23, 17, 1.5, 8.0)]        # Colts -1 at the close, total 8
    monkeypatch.setattr(sbr, "load_archive", lambda sport, cache_dir, max_age_hours: sbr.parse(rows))
    games = pd.DataFrame({"game_id": ["a", "b", "c"], "gameday": "2021-11-14", "home_team": ["NYJ", "GB", "IND"],
                          "away_team": ["BUF", "SEA", "JAX"], "home_score": [17, 17, 23], "away_score": [45, 0, 17],
                          "spread_line": [-13.0, 3.0, 1.0], "total_line": [47.0, 49.5, 47.5]})
    out = backtest.load_opening_lines(games)
    assert np.isnan(out.loc["a", "open_line"]) and out.loc["a", "open_total"] == 48.5
    assert (out.loc["b", "open_line"], out.loc["b", "open_total"]) == (2.5, 49.5)
    assert out.loc["c", "open_line"] == -1.5 and np.isnan(out.loc["c", "open_total"])   # a small move across zero stays
