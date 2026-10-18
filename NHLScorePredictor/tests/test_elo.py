import pandas as pd

from nhlpredictor.elo import run_elo


def test_winner_gains_and_home_ice_applies():
    g = pd.DataFrame([
        dict(game_id=1, season=2026, start=pd.Timestamp("2025-10-10", tz="UTC"), home_team="A", away_team="B",
             home_score=5, away_score=1, neutral=False, completed=True),
        dict(game_id=2, season=2026, start=pd.Timestamp("2025-10-12", tz="UTC"), home_team="B", away_team="A",
             home_score=None, away_score=None, neutral=True, completed=False),
    ])
    frame, ratings = run_elo(g)
    assert ratings["A"] > ratings["B"]
    first, second = frame.set_index("game_id").loc[1], frame.set_index("game_id").loc[2]
    assert first.elo_home_prob > 0.5          # home ice before any games
    assert second.elo_home_prob < 0.5         # A is now better and the site is neutral
