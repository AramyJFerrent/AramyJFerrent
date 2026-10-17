import numpy as np
import pandas as pd

from nflpredictor.backtest import pick_record
from nflpredictor.pipeline import LOG_COLUMNS, select_upcoming, update_log
from nflpredictor.report import grade, model_pick, pick_table


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


def test_fair_moneyline_matches_win_chance():
    from nflpredictor.report import american_odds, fair_moneyline

    assert american_odds(0.75) == -300
    assert american_odds(0.25) == 300
    assert american_odds(0.5) == 100
    assert american_odds(0.6) == -150
    assert american_odds(0.73) == -270          # -270.4 rounds to the nearest 5
    assert american_odds(0.999) == -9900        # capped at 99%
    assert fair_moneyline(0.75, 0.25, "NE", "NYJ") == "NYJ +300 / NE -300"
    # Ties are refunded, so the 2% tie chance is spread over both sides.
    assert fair_moneyline(0.588, 0.392, "KC", "LV") == "LV +150 / KC -150"


def test_first_line_is_kept_while_predictions_refresh():
    g = schedule()
    first = pd.DataFrame([entry("b", g.kickoff[1], margin=3.0, spread_line=1.0,
                                first_spread_line=1.0, first_model_margin=3.0)])
    later = pd.DataFrame([entry("b", g.kickoff[1], margin=4.0, spread_line=2.5,
                                first_spread_line=2.5, first_model_margin=4.0)])
    row = update_log(first, later, g).set_index("game_id").loc["b"]
    assert row.spread_line == 2.5 and row.pred_margin == 4.0       # latest prediction
    assert row.first_spread_line == 1.0 and row.first_model_margin == 3.0


def test_first_line_fills_in_once_a_line_appears():
    g = schedule()
    no_line = pd.DataFrame([entry("c", g.kickoff[2], spread_line=np.nan, first_spread_line=np.nan,
                                  first_model_margin=np.nan)])
    with_line = pd.DataFrame([entry("c", g.kickoff[2], spread_line=3.0, first_spread_line=3.0,
                                    first_model_margin=5.0)])
    row = update_log(no_line, with_line, g).set_index("game_id").loc["c"]
    assert row.first_spread_line == 3.0 and row.first_model_margin == 5.0


def test_model_pick_names_the_side_and_gap():
    assert model_pick(9.0, 7.0, "IND", "TEN") == "IND -7.0 (2.0)"     # model likes the favorite
    assert model_pick(4.0, 7.5, "NE", "NYJ") == "NYJ +7.5 (3.5)"      # model likes the dog
    assert model_pick(-2.0, 1.5, "CLE", "BAL") == "BAL +1.5 (3.5)"    # home favored, model likes away
    assert model_pick(-5.0, -1.5, "CLE", "BAL") == "BAL -1.5 (3.5)"   # away favorite
    assert model_pick(3.2, 3.0, "A", "B") == "no edge"
    assert model_pick(3.0, np.nan, "A", "B") == "–"


def test_pick_grading_and_line_movement():
    g = schedule()
    # Home won by 4. Early line home -2.5, model said +5: a win. Line closed at -3.5 (moved toward the pick).
    graded = update_log(pd.DataFrame([entry("a", g.kickoff[0], spread_line=3.5, model_margin=5.0,
                                            first_spread_line=2.5, first_model_margin=5.0)]),
                        pd.DataFrame(columns=LOG_COLUMNS), g)
    text = pick_table(graded)
    assert "| Early-week line (first prediction with a line) | 1-0-0 | 100.0% |" in text
    assert "1 of 1 games" in text
    rec = pick_record(pd.DataFrame({"home_score": [24, 20, 17], "away_score": [20, 20, 21],
                                    "model_margin": [5.0, 2.0, 0.2], "line": [2.5, 1.0, 0.0],
                                    "close": [3.5, 1.0, 0.0]}), "line", closing_col="close")
    assert (rec["wins"], rec["losses"], rec["pushes"]) == (1, 1, 0)   # third game: edge under 0.5
    assert rec["moved_toward"] == 1.0 and rec["moved_games"] == 1
