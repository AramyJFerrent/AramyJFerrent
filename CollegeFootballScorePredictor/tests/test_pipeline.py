import numpy as np
import pandas as pd

from cfbpredictor.backtest import is_power, pick_record
from cfbpredictor.pipeline import LOG_COLUMNS, select_upcoming, update_log, with_live_lines
from cfbpredictor.report import american_odds, fair_moneyline, grade, model_pick, pick_table, render


def schedule():
    k = pd.Timestamp("2026-10-24 19:30", tz="UTC")
    return pd.DataFrame([
        {"game_id": 1, "season": 2026, "week": 8, "kickoff": k - pd.Timedelta(days=3),
         "completed": True, "home_score": 31.0, "away_score": 24.0},
        {"game_id": 2, "season": 2026, "week": 8, "kickoff": k, "completed": False,
         "home_score": np.nan, "away_score": np.nan},
        {"game_id": 3, "season": 2026, "week": 9, "kickoff": k + pd.Timedelta(days=7),
         "completed": False, "home_score": np.nan, "away_score": np.nan},
        {"game_id": 4, "season": 2026, "week": 10, "kickoff": k + pd.Timedelta(days=14),
         "completed": False, "home_score": np.nan, "away_score": np.nan},
    ])


def entry(game_id, kickoff, margin=3.0, **kw):
    row = {c: np.nan for c in LOG_COLUMNS}
    row.update(game_id=game_id, season=2026, week=8, kickoff=kickoff, start_time_tbd=False,
               away_team="Away U", home_team="Home U", away_division="fbs", home_division="fbs", neutral=False,
               pred_home=30.0, pred_away=27.0, pred_margin=margin, pred_total=57.0,
               model_margin=5.0, model_total=55.0, headline_home=31, headline_away=27,
               home_win_prob=0.6, away_win_prob=0.4, one_score_prob=0.4, home_low=17, home_high=44,
               away_low=14, away_high=41, spread_line=2.5, total_line=58.5,
               predicted_at=pd.Timestamp("2026-10-20", tz="UTC"), source="live")
    row.update(kw)
    return row


def test_select_upcoming_skips_started_and_far_weeks():
    g = schedule()
    up = select_upcoming(g, 2026, pd.Timestamp("2026-10-21", tz="UTC"), weeks=2)
    assert list(up["game_id"]) == [2, 3]
    later = select_upcoming(g, 2026, pd.Timestamp("2026-10-25", tz="UTC"), weeks=1)
    assert list(later["game_id"]) == [3]


def test_log_overwrites_pre_kickoff_and_attaches_results():
    g = schedule()
    old = pd.DataFrame([entry(1, g.kickoff[0]), entry(2, g.kickoff[1], margin=1.0)])
    new = pd.DataFrame([entry(2, g.kickoff[1], margin=4.0)])
    merged = update_log(old, new, g).set_index("game_id")
    assert merged.loc[2, "pred_margin"] == 4.0          # refreshed before kickoff
    assert merged.loc[1, "home_score"] == 31.0          # graded once final
    assert np.isnan(merged.loc[2, "home_score"])


def test_first_line_is_kept_and_fills_in_once_a_line_appears():
    g = schedule()
    first = pd.DataFrame([entry(2, g.kickoff[1], spread_line=1.0, first_spread_line=1.0, first_model_margin=3.0,
                                first_predicted_at=pd.Timestamp("2026-10-19", tz="UTC"))])
    later = pd.DataFrame([entry(2, g.kickoff[1], margin=4.0, spread_line=2.5, first_spread_line=2.5,
                                first_model_margin=4.0, first_predicted_at=pd.Timestamp("2026-10-21", tz="UTC"))])
    row = update_log(first, later, g).set_index("game_id").loc[2]
    assert row.spread_line == 2.5 and row.pred_margin == 4.0
    assert row.first_spread_line == 1.0 and row.first_model_margin == 3.0
    assert row.first_predicted_at == pd.Timestamp("2026-10-19", tz="UTC")

    no_line = pd.DataFrame([entry(3, g.kickoff[2], spread_line=np.nan, first_spread_line=np.nan)])
    with_line = pd.DataFrame([entry(3, g.kickoff[2], spread_line=3.0, first_spread_line=3.0, first_model_margin=5.0)])
    row = update_log(no_line, with_line, g).set_index("game_id").loc[3]
    assert row.first_spread_line == 3.0 and row.first_model_margin == 5.0


def test_grade_compares_model_and_line():
    g = schedule()
    log = update_log(pd.DataFrame([entry(1, g.kickoff[0])]), pd.DataFrame(columns=LOG_COLUMNS), g)
    table = grade(log).set_index("Predictor")
    assert table.loc["Final prediction", "Margin MAE"] == 4.0                 # predicted +3, actual +7
    assert table.loc["Betting line when predicted", "Margin MAE"] == 4.5
    assert table.loc["Model only (before blending)", "Margin MAE"] == 2.0
    assert table.loc["Final prediction", "Winners"] == 1.0


def test_fair_moneyline_matches_win_chance():
    assert american_odds(0.75) == -300 and american_odds(0.25) == 300
    assert american_odds(0.5) == 100 and american_odds(0.999) == -9900
    assert fair_moneyline(0.75, 0.25, "Ohio State", "Purdue") == "Purdue +300 / Ohio State -300"


def test_model_pick_names_the_side_and_gap():
    assert model_pick(9.0, 7.0, "LSU", "Auburn") == "LSU -7.0 (2.0)"
    assert model_pick(4.0, 7.5, "LSU", "Auburn") == "Auburn +7.5 (3.5)"
    assert model_pick(-5.0, -1.5, "LSU", "Auburn") == "Auburn -1.5 (3.5)"
    assert model_pick(3.2, 3.0, "A", "B") == "no edge"
    assert model_pick(3.0, np.nan, "A", "B") == "–"


def test_pick_grading_and_line_movement():
    g = schedule()
    graded = update_log(pd.DataFrame([entry(1, g.kickoff[0], spread_line=3.5, model_margin=5.0,
                                            first_spread_line=2.5, first_model_margin=5.0)]),
                        pd.DataFrame(columns=LOG_COLUMNS), g)
    text = pick_table(graded)
    assert "| Early-week line (first prediction with a line) | 1-0-0 | 100.0% |" in text
    assert "1 of 1 games" in text
    rec = pick_record(pd.DataFrame({"home_score": [24, 20, 17], "away_score": [20, 20, 21],
                                    "model_margin": [5.0, 2.0, 0.2], "line": [2.5, 1.0, 0.0],
                                    "close": [3.5, 1.0, 0.0]}), "line", closing_col="close")
    assert (rec["wins"], rec["losses"], rec["pushes"]) == (1, 1, 0)
    assert rec["moved_toward"] == 1.0 and rec["moved_games"] == 1


def test_live_lines_replace_stale_ones():
    lines = pd.DataFrame({"game_id": [2, 3], "season": [2026, 2026], "spread_line": [1.0, 2.0],
                          "total_line": [50.0, 51.0], "books": [0, 0]})
    live = pd.DataFrame({"game_id": [2], "spread_line": [3.5], "total_line": [52.5], "home_moneyline": [-160],
                         "away_moneyline": [135], "line_source": ["ESPN"]})
    out = with_live_lines(lines, live, schedule()).set_index("game_id")
    assert out.loc[2, "spread_line"] == 3.5 and out.loc[3, "spread_line"] == 2.0


def test_power_conferences_by_season():
    conf = pd.Series(["Pac-12", "Pac-12", "SEC", "FBS Independents", "Mountain West"])
    team = pd.Series(["Oregon", "Oregon State", "LSU", "Notre Dame", "Boise State"])
    season = pd.Series([2023, 2024, 2024, 2024, 2024])
    assert list(is_power(conf, team, season)) == [True, False, True, True, False]


def test_render_handles_an_empty_season():
    from cfbpredictor.model import ScoreModel

    model = ScoreModel(coef={"home": 3.0, "home_conf": -1.5, "fcs": 7.0, "elo": 0.2}, fit_games=10,
                       fit_seasons=(2025,))
    ratings = pd.DataFrame(columns=["team", "conference", "net_pts", "off_pts", "def_pts", "st_pts",
                                    "elo_pts", "elo"])
    text = render(pd.DataFrame(columns=LOG_COLUMNS), pd.DataFrame(columns=LOG_COLUMNS), ratings, model,
                  pd.Timestamp("2027-03-05", tz="UTC"), 2027)
    assert "No upcoming games" in text and "Nothing graded yet" in text
