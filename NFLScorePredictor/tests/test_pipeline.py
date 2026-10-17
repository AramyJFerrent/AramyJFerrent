import numpy as np
import pandas as pd

from nflpredictor.pipeline import LOG_COLUMNS, select_upcoming, update_log
from nflpredictor.report import grade


def schedule():
    k = pd.Timestamp("2026-10-18 17:00", tz="UTC")
    return pd.DataFrame([
        {"game_id": "a", "season": 2026, "week": 6, "kickoff": k - pd.Timedelta(days=3),
         "completed": True, "home_score": 24.0, "away_score": 20.0},
        {"game_id": "b", "season": 2026, "week": 6, "kickoff": k, "completed": False,
         "home_score": np.nan, "away_score": np.nan},
        {"game_id": "c", "season": 2026, "week": 7, "kickoff": k + pd.Timedelta(days=7),
         "completed": False, "home_score": np.nan, "away_score": np.nan},
        {"game_id": "d", "season": 2026, "week": 8, "kickoff": k + pd.Timedelta(days=14),
         "completed": False, "home_score": np.nan, "away_score": np.nan},
    ])


def entry(game_id, kickoff, margin=3.0, **kw):
    row = {c: np.nan for c in LOG_COLUMNS}
    row.update(game_id=game_id, season=2026, week=6, kickoff=kickoff, away_team="X", home_team="Y",
               pred_home=23.0, pred_away=20.0, pred_margin=margin, pred_total=43.0,
               model_margin=5.0, model_total=40.0,
               home_win_prob=0.6, away_win_prob=0.39, tie_prob=0.01, home_low=13, home_high=34,
               away_low=10, away_high=31, spread_line=2.5, total_line=44.0,
               predicted_at=pd.Timestamp("2026-10-15", tz="UTC"), source="live")
    row.update(kw)
    return row


def test_select_upcoming_skips_started_and_far_weeks():
    g = schedule()
    now = pd.Timestamp("2026-10-17", tz="UTC")
    up = select_upcoming(g, 2026, now, weeks=2)
    assert list(up["game_id"]) == ["b", "c"]
    later = select_upcoming(g, 2026, pd.Timestamp("2026-10-19", tz="UTC"), weeks=1)
    assert list(later["game_id"]) == ["c"]


def test_log_overwrites_pre_kickoff_and_attaches_results():
    g = schedule()
    old = pd.DataFrame([entry("a", g.kickoff[0]), entry("b", g.kickoff[1], margin=1.0)])
    new = pd.DataFrame([entry("b", g.kickoff[1], margin=4.0)])
    merged = update_log(old, new, g).set_index("game_id")
    assert merged.loc["b", "pred_margin"] == 4.0          # refreshed before kickoff
    assert merged.loc["a", "home_score"] == 24.0          # graded once final
    assert np.isnan(merged.loc["b", "home_score"])


def test_grade_compares_model_and_line():
    g = schedule()
    log = update_log(pd.DataFrame([entry("a", g.kickoff[0])]), pd.DataFrame(columns=LOG_COLUMNS), g)
    table = grade(log).set_index("Predictor")
    assert table.loc["Final prediction", "Margin MAE"] == 1.0    # predicted +3, actual +4
    assert table.loc["Betting line when predicted", "Margin MAE"] == 1.5
    assert table.loc["Final prediction", "Winners"] == 1.0
    assert table.loc["Model only (before blending)", "Margin MAE"] == 1.0   # +5 vs +4
    assert table.loc["Model only (before blending)", "Total MAE"] == 4.0
