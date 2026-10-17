import pandas as pd

from nflpredictor.elo import run_elo


def games(rows):
    df = pd.DataFrame(rows)
    df["kickoff"] = pd.to_datetime(df["gameday"], utc=True)
    df["completed"] = df["home_score"].notna()
    return df


def test_winner_gains_and_home_field_applies():
    g = games([
        dict(game_id="g1", season=2020, week=1, gameday="2020-09-13", home_team="A", away_team="B",
             home_score=30, away_score=10, neutral=False),
        dict(game_id="g2", season=2020, week=2, gameday="2020-09-20", home_team="B", away_team="A",
             home_score=None, away_score=None, neutral=True),
    ])
    frame, ratings = run_elo(g)
    assert ratings["A"] > ratings["B"]
    first, second = frame.set_index("game_id").loc["g1"], frame.set_index("game_id").loc["g2"]
    assert first.elo_spread > 0           # home field before any games
    assert second.elo_spread < 0          # A is now better and the site is neutral
