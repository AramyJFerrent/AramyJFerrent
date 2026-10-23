import numpy as np
import pandas as pd

from nbapredictor.config import Hyperparams
from nbapredictor.players import (BOX_STATS, SPM, BoxScores, PlayerRatings, box_rates, lineup_strength,
                                  minutes_history, rescale_minutes)


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
    short = [40, 38, 30, 20, 10, 8, 6, 4]                      # 156 minutes: someone is missing
    m = rescale_minutes(short)
    assert np.isclose(m.sum(), 240) and m.max() <= 42 and np.all(np.diff(m) <= 1e-9)
    assert m[0] - 40 < m[-1] - 4                               # the bench absorbs most of the gap
    p = rescale_minutes(short, how="proportional")
    assert np.isclose(p.sum(), 240) and np.isclose(p.max(), 42) and np.isclose(p[1], 42)
    deep = rescale_minutes([36, 34, 32, 30, 28, 24, 20, 16, 12, 8, 6, 4])   # 250 minutes
    assert np.isclose(deep.sum(), 240) and np.isclose(deep[0] / deep[-1], 9.0)
    assert np.allclose(rescale_minutes([30, 20, 10, 5, 5]), 48)  # five players play the whole game
    off = {1: 3.0, 2: -1.0}
    de = {1: -1.0, 2: 0.5}
    o, d = lineup_strength([1, 2, 3], [48, 48, 0], off, de, newcomer=(-1.0, 1.0))
    assert o == 2.0 and d == -0.5


def test_box_scores_total_each_players_games_before_a_day():
    games = pd.DataFrame({"game_id": [1, 2, 3], "season": 2016, "date": ["2015-10-28", "2015-10-30", "2015-11-02"]})
    box = pd.DataFrame({"game_id": [1, 2, 3, 2], "player_id": [7, 7, 7, 9], "minutes": [20, 30, 0, 10],
                        **{c: [2.0, 4.0, 9.0, 1.0] for c in BOX_STATS}})
    b = BoxScores(box, games)
    day_oct30 = (pd.Timestamp("2015-10-30") - pd.Timestamp("2015-08-01")).days
    totals = b.before(2016, day_oct30, [7, 9, 5])            # only game 1 is before the 30th
    assert list(totals[:, 0]) == [20.0, 0.0, 0.0] and totals[0, 1] == 2.0
    late = b.before(2016, np.inf, [7, 9])                   # game 3 (no minutes) is left out
    assert list(late[:, 0]) == [50.0, 10.0] and late[0, 1] == 6.0
    assert np.allclose(box_rates(late)[0], 36 * 6 / 50) and not box_rates(b.before(2016, 0, [7])).any()


def test_spm_recovers_a_linear_box_score_relation():
    rng = np.random.default_rng(1)
    rates = rng.normal(10, 3, size=(400, len(BOX_STATS)))
    minutes = rng.uniform(300, 3000, 400)
    off = 0.5 * (rates[:, 0] - 10) - 0.3 * (rates[:, 9] - 10) + rng.normal(0, 0.1, 400)
    de = -0.2 * (rates[:, 7] - 10) + rng.normal(0, 0.1, 400)
    spm = SPM.fit(rates, minutes, off, de)
    pred = spm.predict(np.array([[12.0] + [10.0] * (len(BOX_STATS) - 1)]))
    assert abs(pred[0, 0] - 1.0) < 0.1 and abs(pred[0, 1]) < 0.1
    assert SPM.fit(rates[:10], minutes[:10], off[:10], de[:10]) is None   # too few player-seasons


def test_box_prior_moves_a_newcomer_toward_his_box_score_ratings(monkeypatch):
    monkeypatch.setattr("nbapredictor.players.SPM_MIN_PLAYERS", 10)
    stints, games = synthetic_stints(n_games=40)
    games = pd.concat([games.assign(season=2015, game_id=games["game_id"] + 1000,
                                    date=pd.to_datetime(games["date"]) - pd.DateOffset(years=1)),
                       games], ignore_index=True)
    stints = pd.concat([stints.assign(game_id=stints["game_id"] + 1000), stints], ignore_index=True)
    rng = np.random.default_rng(2)
    rows = []
    for gid in games["game_id"]:
        for pid in list(range(1, 9)) + list(range(11, 19)):
            # Player 1 (the good scorer in the stints) scores far more than anyone.
            rows.append({"game_id": gid, "player_id": pid, "minutes": 30.0,
                         **{c: float(rng.poisson(30 if (c == "pts" and pid == 1) else 5)) for c in BOX_STATS}})
    box = pd.DataFrame(rows)
    hp = Hyperparams(box_prior_minutes_new=300.0, box_prior_minutes=300.0)
    pr = PlayerRatings(stints, games, hp, box)
    plain = PlayerRatings(stints, games, Hyperparams(), box)
    assert plain.box is None                                 # no box prior unless it is switched on
    pr._spm[2015] = None                                     # the first season has nothing to fit on
    spm = pr.spm(2016)
    assert spm is not None
    sr = pr._season(2016)
    _, at = pr._penalty(2016, sr)
    i = sr.players.index(1)
    first, later = at(float(pr.game_days[2016][0])), at(float(pr.game_days[2016][-1]))
    o0 = pr.prior(2016)[0].get(1, pr.newcomer[0])
    totals = pr.box.before(2016, float(pr.game_days[2016][-1]), [1])
    target, m = spm.predict(box_rates(totals))[0, 0], totals[0, 0]
    assert first[2 + i] == o0                                # no minutes yet: the anchor
    assert m == 30.0 * 38                                    # two games a day, all but the last day's
    assert np.isclose(later[2 + i], o0 + m / (m + 300.0) * (target - o0)) and target > o0
