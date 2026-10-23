import numpy as np
import pandas as pd

from nhlpredictor.pipeline import LOG_COLUMNS, result_label, select_upcoming, update_log
from nhlpredictor.report import edge_table, fair_moneyline, grade


def schedule():
    k = pd.Timestamp("2026-10-18 23:00", tz="UTC")
    rows = []
    for gid, offset, done, hs, as_ in (("a", -1, True, 4.0, 2.0), ("b", 0, False, np.nan, np.nan),
                                       ("c", 1, False, np.nan, np.nan), ("d", 2, False, np.nan, np.nan)):
        start = k + pd.Timedelta(days=offset)
        rows.append({"game_id": gid, "season": 2027, "start": start,
                     "date": start.tz_convert("America/New_York").date(), "completed": done,
                     "home_score": hs, "away_score": as_})
    return pd.DataFrame(rows)


def entry(game_id, start, home_prob=0.6, **kw):
    row = {c: np.nan for c in LOG_COLUMNS}
    row.update(game_id=game_id, season=2027, game_type="R", start=start, date=str(start.date()),
               away_team="X", home_team="Y", pred_home=3.2, pred_away=2.7, pred_total=5.9,
               home_win_prob=home_prob, away_win_prob=1 - home_prob, model_home_prob=home_prob,
               ot_prob=0.22, home_low=1, home_high=6, away_low=1, away_high=5,
               elo_home_prob=0.55, predicted_at=pd.Timestamp("2026-10-15", tz="UTC"), source="live")
    row.update(kw)
    return row


def test_select_upcoming_skips_started_games_and_far_days():
    g = schedule()
    up = select_upcoming(g, 2027, pd.Timestamp("2026-10-18 12:00", tz="UTC"), days=2)
    assert list(up["game_id"]) == ["b", "c"]
    later = select_upcoming(g, 2027, pd.Timestamp("2026-10-19 00:00", tz="UTC"), days=1)
    assert list(later["game_id"]) == ["c"]


def test_log_overwrites_before_puck_drop_and_attaches_results():
    g = schedule()
    old = pd.DataFrame([entry("a", g.start[0]), entry("b", g.start[1], home_prob=0.5)])
    new = pd.DataFrame([entry("b", g.start[1], home_prob=0.58)])
    outcomes = pd.DataFrame({"periods": [4], "shootout": [1]}, index=["a"])
    merged = update_log(old, new, g, outcomes).set_index("game_id")
    assert merged.loc["b", "home_win_prob"] == 0.58
    assert merged.loc["a", "home_score"] == 4.0 and merged.loc["a", "result"] == "SO"
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
    log = update_log(pd.DataFrame([entry("a", g.start[0], market_home_prob=0.7, total_line=5.5)]),
                     pd.DataFrame(columns=LOG_COLUMNS), g)
    table = grade(log).set_index("Predictor")
    assert np.isclose(table.loc["Final prediction", "Log loss"], -np.log(0.6))
    assert np.isclose(table.loc["Betting market (de-vigged moneyline)", "Log loss"], -np.log(0.7))
    assert np.isclose(table.loc["Final prediction", "Total MAE"], 0.1)
    assert table.loc["Final prediction", "80% range hit"] == 1.0


def test_fair_moneyline_and_result_labels():
    assert fair_moneyline(0.6, "BOS", "NYR") == "NYR +150 / BOS -150"
    assert result_label(3, 0) == "REG" and result_label(4, 0) == "OT" and result_label(5, -1) == "SO"


def test_edge_table_records_each_market_and_moneyline_moves():
    g = schedule()
    # Final 4-2 home: home -1.5 at +150 wins, the away moneyline loses, under 6.0 pushes.
    log = update_log(pd.DataFrame([entry("a", g.start[0], model_home_prob=0.62, market_home_prob=0.6,
                                         home_moneyline=-150, away_moneyline=130,
                                         first_model_home_prob=0.62, first_market_home_prob=0.55,
                                         first_home_moneyline=-120, first_away_moneyline=100,
                                         spread_edge_side="home", spread_edge_line=-1.5, spread_edge_price=150,
                                         moneyline_edge_side="away", moneyline_edge_price=130,
                                         total_edge_side="under", total_edge_line=6.0, total_edge_price=-110,
                                         spread_edge_stake=1.0, moneyline_edge_stake=0.5, total_edge_stake=1.5,
                                         spread_edge_ev=0.1, moneyline_edge_ev=0.05, total_edge_ev=0.04)]),
                     pd.DataFrame(columns=LOG_COLUMNS), g)
    text = edge_table(log)
    assert "| Puck line | 1 | 1-0-0 | 1.0 | +1.50 | +150.0% | +10.0% |" in text
    assert "| Moneyline | 1 | 0-1-0 | 0.5 | -0.50 | -100.0% | +5.0% |" in text
    assert "| Total | 1 | 0-0-1 | 1.5 | +0.00 | +0.0% | +4.0% |" in text
    assert "1 of 1 games" in text                        # first-line edge on the home side, line moved toward it
