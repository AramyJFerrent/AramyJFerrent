import numpy as np
import pandas as pd

from types import SimpleNamespace

from mlbpredictor import pipeline
from mlbpredictor.edges import EDGE_COLUMNS, add_edges
from mlbpredictor.pipeline import LOG_COLUMNS, lineup_frame, load_log, model_lines, select_upcoming, update_log
from mlbpredictor.report import edge_cell, edge_table, fair_moneyline, grade, render, upcoming_table


def schedule():
    k = pd.Timestamp("2026-05-10 23:05", tz="UTC")
    rows = []
    for gid, offset, status, hs, as_ in (("a", -1, "final", 5.0, 2.0), ("b", 0, "scheduled", np.nan, np.nan),
                                         ("c", 1, "scheduled", np.nan, np.nan), ("d", 2, "scheduled", np.nan, np.nan),
                                         ("e", 1, "postponed", np.nan, np.nan)):
        start = k + pd.Timedelta(days=offset)
        rows.append({"game_id": gid, "season": 2026, "start": start, "status": status,
                     "date": start.tz_convert("America/New_York").date(), "completed": status == "final",
                     "home_score": hs, "away_score": as_, "innings": 9.0 if status == "final" else np.nan})
    return pd.DataFrame(rows)


def entry(game_id, start, home_prob=0.6, **kw):
    row = {c: np.nan for c in LOG_COLUMNS}
    row.update(game_id=game_id, season=2026, game_type="R", start=start, date=str(start.date()),
               away_team="BOS", home_team="NYY", away_starter="A", home_starter="B", pred_home=4.8, pred_away=4.1,
               pred_total=8.9, home_win_prob=home_prob, away_win_prob=1 - home_prob, model_home_prob=home_prob,
               extra_prob=0.09, home_low=2, home_high=8, away_low=1, away_high=7, headline_home=5, headline_away=4,
               elo_home_prob=0.55, predicted_at=pd.Timestamp("2026-05-08", tz="UTC"), source="live")
    row.update(kw)
    return row


def test_select_upcoming_skips_started_and_postponed_games():
    g = schedule()
    up = select_upcoming(g, 2026, pd.Timestamp("2026-05-10 12:00", tz="UTC"), days=2)
    assert list(up["game_id"]) == ["b", "c"]
    later = select_upcoming(g, 2026, pd.Timestamp("2026-05-11 00:00", tz="UTC"), days=1)
    assert list(later["game_id"]) == ["c"]


def test_log_overwrites_before_first_pitch_attaches_results_and_drops_postponed():
    g = schedule()
    old = pd.DataFrame([entry("a", g.start[0]), entry("b", g.start[1], home_prob=0.5), entry("e", g.start[4])])
    new = pd.DataFrame([entry("b", g.start[1], home_prob=0.58)])
    merged = update_log(old, new, g).set_index("game_id")
    assert merged.loc["b", "home_win_prob"] == 0.58 and "e" not in merged.index
    assert merged.loc["a", "home_score"] == 5.0 and merged.loc["a", "innings"] == 9
    assert np.isnan(merged.loc["b", "home_score"])


def test_first_line_is_kept_while_predictions_refresh():
    g = schedule()
    first = pd.DataFrame([entry("b", g.start[1], home_moneyline=-150, first_home_moneyline=-150,
                                first_model_home_prob=0.62, first_market_home_prob=0.58)])
    later = pd.DataFrame([entry("b", g.start[1], home_moneyline=-170, first_home_moneyline=-170,
                                first_model_home_prob=0.61, first_market_home_prob=0.61)])
    row = update_log(first, later, g).set_index("game_id").loc["b"]
    assert row.home_moneyline == -170 and row.first_home_moneyline == -150
    assert row.first_model_home_prob == 0.62


def test_grade_compares_model_market_and_elo():
    g = schedule()
    log = update_log(pd.DataFrame([entry("a", g.start[0], market_home_prob=0.7, total_line=8.5)]),
                     pd.DataFrame(columns=LOG_COLUMNS), g)
    table = grade(log).set_index("Predictor")
    assert np.isclose(table.loc["Final prediction", "Log loss"], -np.log(0.6))
    assert np.isclose(table.loc["Betting market (de-vigged moneyline)", "Log loss"], -np.log(0.7))
    assert np.isclose(table.loc["Final prediction", "Total MAE"], 1.9)
    assert table.loc["Final prediction", "80% range hit"] == 1.0


def test_lineups_need_nine_players():
    fresh = pd.DataFrame([{"game_id": "g", "home_team": "NYY", "away_team": "BOS",
                           "home_lineup_ids": [str(i) for i in range(9)], "home_lineup_pos": ["8"] * 9,
                           "away_lineup_ids": ["1", "2"], "away_lineup_pos": ["8", "9"]}])
    frame = lineup_frame(fresh)
    assert list(frame.index) == [("g", "NYY")] and frame.loc[("g", "NYY"), "p9"] == "8"


def test_fair_moneyline():
    assert fair_moneyline(0.6, "NYY", "BOS") == "BOS +150 / NYY -150"


def priced(game_id, start, **kw):
    """A log row with every line posted and the model's own chances, edges filled in."""
    base = dict(home_moneyline=-120, away_moneyline=110, market_home_prob=0.53, model_home_prob=0.6,
                home_run_line=-1.5, home_run_line_price=150, away_run_line_price=-170, model_home_cover_prob=0.36,
                model_away_cover_prob=0.64, total_line=8.0, over_price=np.nan, under_price=np.nan,
                model_over_prob=0.52, model_under_prob=0.41, model_total_push_prob=0.07)
    base.update(kw)
    return add_edges(pd.DataFrame([entry(game_id, start, **base)]))[LOG_COLUMNS].iloc[0].to_dict()


def test_edge_cells():
    g = schedule()
    rows = pd.DataFrame([priced("b", g.start[1]),
                         priced("c", g.start[2], model_home_prob=0.5, model_over_prob=0.45, model_under_prob=0.48,
                                over_price=-110, under_price=-110),
                         entry("d", g.start[3], model_home_cover_prob=0.38, model_away_cover_prob=0.62)])
    r = list(rows.itertuples(index=False))
    # Moneyline: 60% at -120 is EV +10%; run line: 36% at +150 is -10%, 64% at -170 is +1.6%: no edge.
    assert edge_cell(r[0], "moneyline") == "NYY (-120): EV +10.0%, model 60%"
    assert edge_cell(r[0], "spread") == "no edge"
    # The total had no posted price: -110 assumed and marked.
    assert edge_cell(r[0], "total") == "Over 8 (-110*): EV +6.3%, model 52%"
    assert edge_cell(r[1], "total") == "no edge" and edge_cell(r[1], "moneyline").startswith("BOS (+110): EV +5.0%")
    assert edge_cell(r[2], "moneyline") == "no line yet" and edge_cell(r[2], "total") == "no line yet"
    # No run line posted: the model's fair odds with its favorite at -1.5.
    assert edge_cell(r[2], "spread") == "no line yet; fair NYY -1.5 +165, BOS +1.5 -165"
    no_price = rows.iloc[[0]].assign(home_run_line_price=np.nan, away_run_line_price=np.nan, spread_edge_pick="")
    assert edge_cell(next(no_price.itertuples(index=False)), "spread").startswith("no price yet; fair NYY -1.5 +180")
    table = upcoming_table(rows)
    assert "| Run line edge | Moneyline edge | Total edge |" in table
    assert "| BOS +110 / NYY -120 |" in table and "| no edge | NYY (-120): EV +10.0%, model 60% |" in table
    model = SimpleNamespace(coef={}, fit_seasons=[2023, 2026], fit_games=100,
                            sim=SimpleNamespace(frailty=30.0, walkoff_hr=0.3))
    page = render(pd.DataFrame(columns=LOG_COLUMNS), rows, pd.DataFrame(), model, 0.2, 0,
                  pd.Timestamp("2026-05-10", tz="UTC"), 2026)
    assert "\\* price not posted; assumed -110." in page and "EV is 3% or more" in page


def test_edge_record_table_grades_live_edges():
    g = schedule()
    # Game a finished 2-5 (home won by 3): NYY moneyline wins at -120, Under 8 (-110 assumed) wins, no run-line edge.
    row = priced("a", g.start[0], model_under_prob=0.55, model_over_prob=0.38, first_model_home_prob=0.6,
                 first_market_home_prob=0.5, first_home_moneyline=-105, first_away_moneyline=-105)
    log = update_log(pd.DataFrame([row]), pd.DataFrame(columns=LOG_COLUMNS), g)
    text = edge_table(log)
    assert "| Moneyline | 1 | 1-0-0 | +0.83 | +83.3% |" in text
    assert "| Total | 1 | 1-0-0 | +0.91 | +90.9% |" in text and "| Run line | 0 | 0-0-0 | +0.00 | – |" in text
    assert "1 of 1 games" in text
    assert "| Moneyline | 0 |" in edge_table(log.assign(source="backfill"))


def test_log_round_trip_and_old_logs(tmp_path, monkeypatch):
    g = schedule()
    monkeypatch.setattr(pipeline, "LOG_PATH", tmp_path / "log.csv")
    entries = pd.DataFrame([priced("b", g.start[1]), entry("c", g.start[2])])
    entries.to_csv(pipeline.LOG_PATH, index=False, float_format="%.4f")
    back = load_log().set_index("game_id")
    assert list(back.columns) == LOG_COLUMNS[1:]
    assert back.loc["b", "moneyline_edge_pick"] == "NYY" and back.loc["b", "total_edge_price"] == -110
    assert back.loc["b", "away_run_line_price"] == -170 and np.isclose(back.loc["b", "moneyline_edge_ev"], 0.1)
    assert pd.isna(back.loc["c", "total_edge_pick"])
    # A log written before the edge columns existed still reads, with them empty.
    entries.drop(columns=EDGE_COLUMNS + ["home_run_line", "model_over_prob"]).to_csv(pipeline.LOG_PATH, index=False)
    old = load_log()
    assert list(old.columns) == LOG_COLUMNS and old[EDGE_COLUMNS[0]].isna().all()
    assert edge_table(update_log(old, pd.DataFrame(columns=LOG_COLUMNS), g)).startswith("| Market |")


def test_model_lines_use_the_unblended_simulation():
    feats = pd.DataFrame({"home_run_line": [np.nan, 1.5, np.nan], "total_line": [7.0, np.nan, 7.5]})
    own = {"home": np.array([[5, 1], [3, 3], [2, 2]]), "away": np.array([[2, 2], [4, 5], [1, 1]])}
    blended = {"home": np.array([[9, 9], [9, 9], [9, 9]]), "away": np.zeros((3, 2), dtype=int)}
    out = model_lines(feats, [0.6, 0.4, 0.3], own, blended, has=[True, True, False])
    # No posted run line: game 0 is quoted at home -1.5 (model favorite), from the unblended sims.
    assert out.loc[0, "model_home_cover_prob"] == 0.5 and out.loc[0, "model_total_push_prob"] == 0.5
    assert out.loc[1, "model_home_cover_prob"] == 0.5 and np.isnan(out.loc[1, "model_over_prob"])
    # Game 2 had no market line, so it was never blended: its numbers come from the one simulation it got.
    assert out.loc[2, "model_home_cover_prob"] == 1.0 and out.loc[2, "model_over_prob"] == 1.0
