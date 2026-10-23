import numpy as np
import pandas as pd
import pytest

from cfbpredictor.config import Hyperparams
from cfbpredictor.data import summarize_qbs
from cfbpredictor.qb import QBModel


def qb_game(week, team, qb_id, name, dropbacks, epa, season=2023):
    return {"game_id": season * 100 + week, "season": season, "week": week, "team": team, "qb_id": qb_id,
            "qb_name": name, "dropbacks": dropbacks, "w": float(dropbacks), "epa": epa}


def test_adjustment_follows_the_latest_starter_against_the_season_mix():
    hp = Hyperparams(qb_prior_dropbacks=10.0, qb_prior_value=0.0, qb_half_life_weeks=1e6, half_life_weeks=1e6)
    rows = [qb_game(w, "Ohio State", 1, "Starter", 30, 0.3 * 30) for w in (1, 2, 3)]
    rows += [qb_game(w, "Michigan", 3, "Other", 30, 0.0) for w in (1, 2, 3, 4)]
    rows += [qb_game(4, "Ohio State", 2, "Backup", 30, -0.3 * 30)]       # the starter is hurt in week 4
    model = QBModel(pd.DataFrame(rows), hp)
    games = pd.DataFrame({"home_team": ["Ohio State"], "away_team": ["Michigan"]})
    early = model.adjustments(games, 2023, 4)
    assert early.loc[0, "home_qb_name"] == "Starter" and abs(early.loc[0, "home_qb_adj"]) < 1e-9
    late = model.adjustments(games, 2023, 5)
    assert late.loc[0, "home_qb_name"] == "Backup"
    values = model.values(2023, 5)
    mix = (90 * values[1] + 30 * values[2]) / 120
    assert late.loc[0, "home_qb_adj"] == pytest.approx(values[2] - mix) and late.loc[0, "home_qb_adj"] < 0
    assert abs(late.loc[0, "away_qb_adj"]) < 1e-9
    # Before a team's first game of a season there is no adjustment.
    assert model.adjustments(games, 2024, 1)[["home_qb_adj", "away_qb_adj"]].eq(0).all(axis=None)


def test_summarize_qbs_reads_the_passer_from_how_the_dropback_ended():
    pbp = pd.DataFrame({
        "game_id": 1, "season": 2023, "week": 2, "season_type": "regular", "start_date": "2023-09-09T19:00:00Z",
        "pos_team": "Texas", "pass": 1, "EPA": [0.5, -1.0, 2.0, 0.1],
        "period": [1, 1, 4, 1], "pos_score_diff_start": [0, 0, 30, 0],                # the third is garbage time
        "passer_player_name": ["Q. Ewers", "Q. Ewers", "Q. Ewers", "A. Manning"],
        "completion_player_id": [11, np.nan, 11, np.nan], "incompletion_player_id": [np.nan, np.nan, np.nan, 12],
        "interception_thrown_player_id": np.nan, "sack_taken_player_id": [np.nan, 11, np.nan, np.nan]})
    q = summarize_qbs(pbp).set_index("qb_id")
    assert q.loc[11, "dropbacks"] == 3 and q.loc[11, "w"] == 2.0 and q.loc[11, "epa"] == pytest.approx(-0.5)
    assert q.loc[12, "qb_name"] == "A. Manning" and q.loc[12, "dropbacks"] == 1
