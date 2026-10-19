import numpy as np
import pandas as pd

from nbapredictor.config import Hyperparams
from nbapredictor.elo import run_elo
from nbapredictor.ratings import RatingsEngine, prepare_rows, targets


def season_games(season, strength, n_rounds=20, seed=0):
    """Round-robin team games where each team's offense adds ``strength`` points per 100."""
    rng = np.random.default_rng(seed)
    teams = list(strength)
    rows, games = [], []
    gid = season * 10000
    day = pd.Timestamp(f"{season - 1}-10-25")
    for r in range(n_rounds):
        for i, first in enumerate(teams):
            for a in teams[i + 1:]:
                h, a = (a, first) if r % 2 else (first, a)
                gid += 1
                date = (day + pd.Timedelta(days=r * 3 + (gid % 3))).strftime("%Y-%m-%d")
                games.append({"game_id": gid, "neutral": False})
                for team, opp, home in ((h, a, 1), (a, h, 0)):
                    poss = 100.0
                    pts = poss * (1.10 + strength[team] / 100 + (0.015 if home else -0.015)) + rng.normal(0, 8)
                    rows.append({"game_id": gid, "season": season, "date": date, "team": team, "opp": opp,
                                 "home": home, "clean_pts": pts, "clean_poss": poss, "poss": poss,
                                 "minutes": 48.0})
    return pd.DataFrame(rows), pd.DataFrame(games)


def test_efficiency_ratings_recover_strength_and_carry_a_prior():
    strength = {"A": 6.0, "B": 2.0, "C": -2.0, "D": -6.0}
    t1, g1 = season_games(2020, strength, n_rounds=60)
    t2, g2 = season_games(2021, strength, n_rounds=1, seed=1)
    teams, games = pd.concat([t1, t2]), pd.concat([g1, g2])
    hp = Hyperparams(team_prior_poss=500.0, team_carryover=0.5, half_life_days=1e6)
    target = targets(hp)["eff"]
    engine = RatingsEngine(prepare_rows(teams, games, target), target, hp.half_life_days)
    final = engine.final(2020)
    assert final.off["A"] - final.off["D"] > 10 and abs(final.hfa - 1.5) < 0.7
    prior = engine.prior(2021)
    assert np.isclose(prior.off["A"], 0.5 * final.off["A"])
    opening = engine.before(2021, 0.0)
    assert np.isclose(opening.off["A"], prior.off["A"])


def test_elo_rewards_winners_and_reverts_between_seasons():
    games = pd.DataFrame({
        "game_id": [1, 2, 3], "season": [2020, 2020, 2021], "neutral": [False, False, False],
        "start": pd.to_datetime(["2019-11-01", "2019-11-02", "2020-11-01"], utc=True),
        "home_team": ["A", "B", "A"], "away_team": ["B", "A", "B"], "completed": [True, True, False],
        "home_score": [120, 99, np.nan], "away_score": [100, 110, np.nan],
    })
    frame, ratings = run_elo(games)
    assert ratings["A"] > ratings["B"]
    assert frame.loc[2, "elo_home_prob"] > frame.loc[0, "elo_home_prob"]
