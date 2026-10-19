import numpy as np
import pandas as pd

from mlbpredictor.pipeline import LOG_COLUMNS, lineup_frame, select_upcoming, update_log
from mlbpredictor.report import american_odds, fair_moneyline, grade, model_pick, pick_record, pick_table


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


def test_fair_moneyline_and_picks():
    assert american_odds(0.6) == -150 and american_odds(0.4) == 150 and american_odds(0.5) == 100
    assert fair_moneyline(0.6, "NYY", "BOS") == "BOS +150 / NYY -150"
    assert model_pick(0.62, 0.55, -120, 100, "NYY", "BOS") == "NYY -120 (7%)"
    assert model_pick(0.50, 0.56, -130, 110, "NYY", "BOS") == "BOS +110 (6%)"
    assert model_pick(0.56, 0.55, -120, 100, "NYY", "BOS") == "no edge"


def test_pick_record_and_table():
    d = pd.DataFrame({"home_score": [4, 1, 3], "away_score": [2, 3, 2], "model": [0.60, 0.40, 0.51],
                      "market": [0.50, 0.50, 0.50], "hml": [110, -120, -110], "aml": [-130, 100, -110]})
    rec = pick_record(d, "model", "market", "hml", "aml")
    assert rec["bets"] == 2 and rec["wins"] == 2 and np.isclose(rec["units"], 1.10 + 1.00)
    g = schedule()
    log = update_log(pd.DataFrame([entry("a", g.start[0], model_home_prob=0.62, market_home_prob=0.6,
                                         home_moneyline=-150, away_moneyline=130, first_model_home_prob=0.62,
                                         first_market_home_prob=0.55, first_home_moneyline=-120,
                                         first_away_moneyline=100)]), pd.DataFrame(columns=LOG_COLUMNS), g)
    text = pick_table(log)
    assert "| First line seen | 1 | 1-0 | +0.83 | +83.3% |" in text and "1 of 1 games" in text
