import datetime as dt

import numpy as np
import pandas as pd

from mlbpredictor.config import current_season
from mlbpredictor.data import load_summaries, prepare_games


def test_season_rolls_over_in_december():
    assert current_season(dt.date(2026, 10, 19)) == 2026
    assert current_season(dt.date(2026, 11, 3)) == 2026
    assert current_season(dt.date(2026, 12, 1)) == 2027
    assert current_season(dt.date(2027, 2, 15)) == 2027


def test_neutral_sites_and_completion():
    g = pd.DataFrame({"game_id": list("abcd"), "season": 2025, "game_type": ["R", "R", "R", "W"],
                      "date": ["2025-04-01", "2025-04-02", "2025-03-18", "2025-10-25"],
                      "start": ["2025-04-01T23:05:00+00:00"] * 4, "game_number": 0,
                      "home_team": ["NYY", "NYY", "NYY", "LAD"], "away_team": "BOS",
                      "status": ["final", "final", "final", "scheduled"], "home_score": [3, 2, 1, np.nan],
                      "away_score": [1, 4, 0, np.nan], "innings": 9, "sched_innings": 9, "tiebreaker": 1,
                      "park_id": ["NYC21", "NYC21", "TOK01", "LOS03"], "dome": 0, "htbf": 0})
    p = prepare_games(g).set_index("game_id")
    assert not p.loc["a", "neutral"] and p.loc["c", "neutral"] and not p.loc["d", "neutral"]
    assert p.loc["a", "completed"] and not p.loc["d", "completed"] and p.loc["d", "playoff"]


def test_committed_history_loads():
    s = load_summaries(2024, 2025)
    g = s["games"]
    assert len(g) > 4800 and g["completed"].all()
    runs = s["pitching"].groupby("game_id")["r"].sum()
    totals = (g.set_index("game_id")["home_score"] + g.set_index("game_id")["away_score"]).reindex(runs.index)
    assert (runs == totals).mean() > 0.99            # every run is charged to some pitcher
    assert s["players"]["throws"].isin(["L", "R"]).mean() > 0.95
