import numpy as np
import pandas as pd

from nbapredictor.pipeline import LOG_COLUMNS, select_upcoming, update_log
from bettingcore import fair_american
from nbapredictor.report import fair_moneyline, grade, spread_text


def schedule():
    k = pd.Timestamp("2026-10-20 23:30", tz="UTC")
    rows = []
    for gid, offset, done, hs, as_, periods in ((1, -1, True, 112.0, 108.0, 5.0), (2, 0, False, np.nan, np.nan, np.nan),
                                                (3, 1, False, np.nan, np.nan, np.nan),
                                                (4, 2, False, np.nan, np.nan, np.nan)):
        start = k + pd.Timedelta(days=offset)
        rows.append({"game_id": gid, "season": 2027, "start": start,
                     "date": start.tz_convert("America/New_York").date(), "completed": done,
                     "home_score": hs, "away_score": as_, "periods": periods})
    return pd.DataFrame(rows)


def entry(game_id, start, home_prob=0.6, **kw):
    row = {c: np.nan for c in LOG_COLUMNS}
    row.update(game_id=game_id, season=2027, game_type="R", start=start, date=str(start.date()),
               away_team="BOS", home_team="NYK", pred_home=113.0, pred_away=109.0, pred_margin=4.0,
               pred_total=222.0, model_margin=5.0, model_total=224.0, home_win_prob=home_prob,
               away_win_prob=1 - home_prob, model_home_prob=home_prob, ot_prob=0.06,
               home_low=100, home_high=126, away_low=96, away_high=122, elo_spread=3.0, elo_home_prob=0.6,
               predicted_at=pd.Timestamp("2026-10-15", tz="UTC"), source="live")
    row.update(kw)
    return row


def test_select_upcoming_skips_started_games_and_far_days():
    g = schedule()
    up = select_upcoming(g, 2027, pd.Timestamp("2026-10-20 12:00", tz="UTC"), days=2)
    assert list(up["game_id"]) == [2, 3]
    later = select_upcoming(g, 2027, pd.Timestamp("2026-10-21 00:00", tz="UTC"), days=1)
    assert list(later["game_id"]) == [3]


def test_log_overwrites_before_tipoff_keeps_the_first_line_and_attaches_results():
    g = schedule()
    old = pd.DataFrame([entry(1, g.start[0]), entry(2, g.start[1], spread=3.0, first_spread=3.0,
                                                    first_model_margin=6.0, first_total=220.0)])
    new = pd.DataFrame([entry(2, g.start[1], home_prob=0.65, spread=4.5, first_spread=4.5, first_model_margin=5.5)])
    merged = update_log(old, new, g).set_index("game_id")
    assert merged.loc[2, "home_win_prob"] == 0.65 and merged.loc[2, "spread"] == 4.5
    assert merged.loc[2, "first_spread"] == 3.0 and merged.loc[2, "first_model_margin"] == 6.0
    assert merged.loc[1, "home_score"] == 112.0 and merged.loc[1, "periods"] == 5
    assert np.isnan(merged.loc[2, "home_score"])


def test_grade_compares_the_prediction_and_the_line():
    g = schedule()
    log = update_log(pd.DataFrame([entry(1, g.start[0], spread=2.0, total=219.0, market_home_prob=0.57)]),
                     pd.DataFrame(columns=LOG_COLUMNS), g)
    table = grade(log).set_index("Predictor")
    assert np.isclose(table.loc["Final prediction", "Margin MAE"], 0.0)       # predicted 4, won by 4
    assert np.isclose(table.loc["Final prediction", "Total MAE"], 2.0)
    assert np.isclose(table.loc["Betting line", "Margin MAE"], 2.0)
    assert np.isclose(table.loc["Final prediction", "Log loss"], -np.log(0.6))
    assert table.loc["Final prediction", "80% range hit"] == 1.0


def test_spreads_and_moneylines_read_like_a_sportsbook():
    assert spread_text(4.46, "NYK", "BOS") == "NYK -4.5" and spread_text(-3.0, "NYK", "BOS") == "BOS -3"
    assert spread_text(0.1, "NYK", "BOS") == "pick'em"
    assert fair_american(0.6) == -150 and fair_american(0.4) == 150
    assert fair_moneyline(0.6, "NYK", "BOS") == "BOS +150 / NYK -150"
