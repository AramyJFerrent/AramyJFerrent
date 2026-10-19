import numpy as np
import pandas as pd

from nbapredictor.availability import build, full_strength, play_probability
from nbapredictor.players import DEBUT_MINUTES


class FakeBuilder:
    """Just what availability.build needs: listed player-games, names and expected minutes."""

    def __init__(self):
        start = pd.Timestamp("2026-11-01 00:00", tz="UTC")
        rows = []
        for i, (pid, team, mins) in enumerate([(1, "BOS", 36), (2, "BOS", 30), (3, "BOS", 10), (4, "MIA", 34),
                                               (5, "BOS", 20)]):
            rows.append({"player_id": pid, "team": team, "start": start, "exp_after": float(mins)})
        # Player 5 has since moved from Boston to Miami.
        rows.append({"player_id": 5, "team": "MIA", "start": start + pd.Timedelta(days=2), "exp_after": 22.0})
        self.minutes = pd.DataFrame(rows)
        self.names = pd.Series({1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five"})

    def latest_minutes(self, before):
        m = self.minutes[self.minutes["start"] < before].sort_values("start")
        return m.drop_duplicates("player_id", keep="last").set_index("player_id")["exp_after"]


def test_statuses_become_chances_of_playing():
    assert play_probability("Out") == 0.0 and play_probability("Out For Season") == 0.0
    assert play_probability("Doubtful") < play_probability("Questionable") < play_probability("Probable") < 1
    assert play_probability(None) == 1.0 and play_probability("Suspension") == 0.0


def test_build_uses_the_roster_injuries_and_recent_minutes():
    fb = FakeBuilder()
    games = pd.DataFrame({"game_id": [10], "home_team": ["BOS"], "away_team": ["MIA"]})
    roster = pd.DataFrame({"team": ["BOS"] * 9, "player_id": [1, 2, 3, 6, 7, 8, 9, 10, 11]})
    injuries = pd.DataFrame({"team": ["BOS", "BOS"], "player_id": [1, 2], "status": ["Out", "Questionable"],
                             "detail": ["Knee", "Ankle"]})
    a = build(games, fb, pd.Timestamp("2026-11-05").date(), roster, injuries)
    bos = a[a["team"] == "BOS"].set_index("player_id")
    assert bos.loc[1, "play_prob"] == 0.0 and bos.loc[2, "play_prob"] == 0.55 and bos.loc[3, "play_prob"] == 1.0
    assert bos.loc[1, "proj_minutes"] == 36 and bos.loc[6, "proj_minutes"] == DEBUT_MINUTES
    # Miami has no roster listed, so it falls back to players whose latest game was for Miami.
    mia = a[a["team"] == "MIA"]
    assert sorted(mia["player_id"]) == [4, 5]
    assert np.isclose(mia.set_index("player_id").loc[5, "proj_minutes"], 22.0)
    assert (full_strength(a)["play_prob"] == 1.0).all()
