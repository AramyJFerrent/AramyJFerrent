import numpy as np
import pandas as pd

from nhlpredictor.pipeline import LOG_COLUMNS, result_label, select_upcoming, update_log
from nhlpredictor.report import american_odds, fair_moneyline, grade, model_pick, pick_record, pick_table


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


def test_fair_moneyline_and_picks():
    assert american_odds(0.6) == -150 and american_odds(0.4) == 150 and american_odds(0.5) == 100
    assert fair_moneyline(0.6, "BOS", "NYR") == "NYR +150 / BOS -150"
    assert model_pick(0.62, 0.55, -120, 100, "BOS", "NYR") == "BOS -120 (7%)"
    assert model_pick(0.50, 0.56, -130, 110, "BOS", "NYR") == "NYR +110 (6%)"
    assert model_pick(0.56, 0.55, -120, 100, "BOS", "NYR") == "no edge"
    assert result_label(3, 0) == "REG" and result_label(4, 0) == "OT" and result_label(5, -1) == "SO"


def test_pick_record_counts_units():
    d = pd.DataFrame({"home_score": [4, 1, 3], "away_score": [2, 3, 2],
                      "model": [0.60, 0.40, 0.51], "market": [0.50, 0.50, 0.50],
                      "hml": [110, -120, -110], "aml": [-130, 100, -110]})
    rec = pick_record(d, "model", "market", "hml", "aml")
    assert rec["bets"] == 2 and rec["wins"] == 2
    assert np.isclose(rec["units"], 1.10 + 1.00)


def test_pick_table_reports_market_moves():
    g = schedule()
    log = update_log(pd.DataFrame([entry("a", g.start[0], model_home_prob=0.62, market_home_prob=0.6,
                                         home_moneyline=-150, away_moneyline=130,
                                         first_model_home_prob=0.62, first_market_home_prob=0.55,
                                         first_home_moneyline=-120, first_away_moneyline=100)]),
                     pd.DataFrame(columns=LOG_COLUMNS), g)
    text = pick_table(log)
    assert "| First line seen | 1 | 1-0 | +0.83 | +83.3% |" in text
    assert "1 of 1 games" in text
