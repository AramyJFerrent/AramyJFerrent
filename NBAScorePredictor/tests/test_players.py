import numpy as np
import pandas as pd

from nbapredictor.config import Hyperparams
from nbapredictor.players import PlayerRatings, lineup_strength, minutes_history, rescale_minutes


def synthetic_stints(n_games=300, seed=0):
    """Two teams of eight players; player 1 adds 8 points per 100 on offense and
    player 12 gives up 6 more on defense."""
    rng = np.random.default_rng(seed)
    games, stints = [], []
    for g in range(n_games):
        date = pd.Timestamp("2015-10-28") + pd.Timedelta(days=g // 2)
        games.append({"game_id": g, "season": 2016, "date": date.date(), "neutral": False})
        for _ in range(12):
            home = rng.choice(np.arange(1, 9), 5, replace=False)
            away = rng.choice(np.arange(11, 19), 5, replace=False)
            poss = 8.0
            rate_h = 1.10 + 0.08 * (1 in home) + 0.06 * (12 in away)
            rate_a = 1.10 + 0.08 * (1 in away) + 0.06 * (12 in home)
            stints.append({"game_id": g, "home_ids": " ".join(map(str, sorted(home))),
                           "away_ids": " ".join(map(str, sorted(away))),
                           "home_pts": rng.poisson(rate_h * poss), "away_pts": rng.poisson(rate_a * poss),
                           "home_poss": poss, "away_poss": poss, "garbage": 0, "valid": 1, "period": 1})
    return pd.DataFrame(stints), pd.DataFrame(games)


def test_rapm_finds_the_players_who_matter():
    stints, games = synthetic_stints()
    hp = Hyperparams(player_off_prior_poss=200.0, player_def_prior_poss=200.0, player_half_life_days=1e6)
    pr = PlayerRatings(stints, games, hp)
    off, de, mu = pr.final(2016)
    others_off = np.mean([off[p] for p in range(2, 9)])
    assert off[1] - others_off > 4.0
    assert de[12] - np.mean([de[p] for p in range(13, 19)]) > 3.0
    # Early in the season the ratings sit near the priors.
    early_off, _, _ = pr.before(2016, float(pr.game_days[2016][1]))
    assert abs(early_off[1] - hp.newcomer_net / 2) < abs(off[1] - hp.newcomer_net / 2)


def test_minutes_projection_skips_injuries_and_counts_healthy_scratches():
    games = pd.DataFrame({"game_id": range(6), "start": pd.date_range("2025-11-01", periods=6, tz="UTC")})
    players = pd.DataFrame({
        "game_id": range(6), "team": "BOS", "player_id": 7, "starter": True,
        "minutes": [30, 30, 0, 0, 30, 0], "status": ["played", "played", "out", "out", "played", "dnp"],
    })
    m = minutes_history(players, games, half_life_games=1e9).set_index("game_id")
    assert list(m.index) == [0, 1, 4, 5]                       # the injury games are skipped
    assert np.isclose(m.loc[4, "proj_minutes"], (12 + 30 + 30) / 3)
    assert np.isclose(m.loc[5, "avg_after"], (12 + 90) / 4)      # a scratch doesn't change minutes when playing
    assert np.isclose(m.loc[5, "exp_after"], (12 + 90) / 5)      # but lowers expected minutes


def test_rescaled_minutes_fill_240_without_overloading_anyone():
    m = rescale_minutes([40, 38, 30, 20, 10, 8, 6, 4])
    assert np.isclose(m.sum(), 240) and np.isclose(m.max(), 42) and np.isclose(m[1], 42)
    assert m[3] > 20 and np.all(np.diff(m) <= 1e-9)            # the order of the rotation is kept
    assert np.allclose(rescale_minutes([30, 20, 10, 5, 5]), 48)  # five players play the whole game
    off = {1: 3.0, 2: -1.0}
    de = {1: -1.0, 2: 0.5}
    o, d = lineup_strength([1, 2, 3], [48, 48, 0], off, de, newcomer=(-1.0, 1.0))
    assert o == 2.0 and d == -0.5
