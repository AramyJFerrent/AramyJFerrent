import numpy as np
import pandas as pd

from cfbpredictor.lines import consensus_lines
from cfbpredictor.odds import live_lines, parse_cfbd, parse_espn
from cfbpredictor.returning import returning_production


def odds_rows(game_id, desc, home_abbr, away_abbr, books, season=2016):
    rows = []
    for book, line, total, opening in books:
        rows += [
            dict(game_id=game_id, season=season, game_desc=desc, market_type="spread", abbr=home_abbr,
                 lines=line, opening_lines=opening, odds=np.nan, book=book),
            dict(game_id=game_id, season=season, game_desc=desc, market_type="spread", abbr=away_abbr,
                 lines=-line, opening_lines=-opening, odds=np.nan, book=book),
            dict(game_id=game_id, season=season, game_desc=desc, market_type="total", abbr="over",
                 lines=total, opening_lines=np.nan, odds=np.nan, book=book),
            dict(game_id=game_id, season=season, game_desc=desc, market_type="money_line", abbr=home_abbr,
                 lines=np.nan, opening_lines=np.nan, odds=-300 if line < 0 else 240, book=book),
            dict(game_id=game_id, season=season, game_desc=desc, market_type="money_line", abbr=away_abbr,
                 lines=np.nan, opening_lines=np.nan, odds=240 if line < 0 else -300, book=book),
        ]
    return rows


def test_consensus_resolves_book_abbreviations_and_takes_medians():
    rows = (odds_rows(1, "Hawaii@California", "CAL", "HAW",
                      [("A", -22.5, 63.5, -21.0), ("B", -23.0, 64.0, -21.0), ("C", -22.5, 64.5, -20.0)])
            + odds_rows(2, "California@Oregon", "ORE", "CAL", [("A", -7.0, 70.0, -6.5), ("B", -7.5, 70.5, -6.5)])
            + odds_rows(3, "Hawaii@Oregon", "ORE", "HAW", [("A", -30.0, 66.0, -28.0)])
            + odds_rows(4, "Oregon@Hawaii", "HAW", "ORE", [("teamrankings", 50.0, 10.0, 50.0)]))
    out = consensus_lines(pd.DataFrame(rows)).set_index("game_id")
    assert out.loc[1, "spread_line"] == 22.5          # California favored at home by the median 22.5
    assert out.loc[1, "total_line"] == 64.0 and out.loc[1, "spread_open"] == 21.0
    assert out.loc[2, "spread_line"] == 7.0 or out.loc[2, "spread_line"] == 7.5
    assert out.loc[1, "home_moneyline"] == -300 and out.loc[1, "books"] == 3
    assert 4 not in out.index                         # projection sites are not books


ESPN_PAYLOAD = {"events": [
    {"id": "401", "competitions": [{
        "competitors": [{"homeAway": "home", "team": {"abbreviation": "ND"}},
                        {"homeAway": "away", "team": {"abbreviation": "USC"}}],
        "odds": [{"provider": {"name": "ESPN BET"}, "details": "ND -10.5", "overUnder": 60.5, "spread": -10.5,
                  "homeTeamOdds": {"favorite": True, "moneyLine": -400},
                  "awayTeamOdds": {"favorite": False, "moneyLine": 300}}]}]},
    {"id": "402", "competitions": [{
        "competitors": [{"homeAway": "home", "team": {"abbreviation": "KENT"}},
                        {"homeAway": "away", "team": {"abbreviation": "OHIO"}}],
        "odds": [{"details": "OHIO -14", "overUnder": 47.5}]}]},
    {"id": "403", "competitions": [{
        "competitors": [{"homeAway": "home", "team": {"abbreviation": "A"}},
                        {"homeAway": "away", "team": {"abbreviation": "B"}}],
        "odds": [{"details": "EVEN", "overUnder": 50}]}]},
    {"id": "404", "competitions": [{"competitors": [], "odds": []}]},
]}


def test_parse_espn_reads_favorites_from_flags_or_details():
    out = parse_espn(ESPN_PAYLOAD).set_index("game_id")
    assert out.loc[401, "spread_line"] == 10.5 and out.loc[401, "total_line"] == 60.5
    assert out.loc[401, "home_moneyline"] == -400 and "ESPN BET" in out.loc[401, "line_source"]
    assert out.loc[402, "spread_line"] == -14.0       # road favorite
    assert out.loc[403, "spread_line"] == 0.0
    assert 404 not in out.index


def test_parse_cfbd_takes_median_across_books():
    payload = [{"id": 501, "lines": [
        {"provider": "DraftKings", "spread": -7.5, "overUnder": 55.5, "homeMoneyline": -280, "awayMoneyline": 230},
        {"provider": "ESPN Bet", "spread": -6.5, "overUnder": 54.5, "homeMoneyline": None, "awayMoneyline": None},
    ]}]
    out = parse_cfbd(payload).iloc[0]
    assert out.game_id == 501 and out.spread_line == 7.0 and out.total_line == 55.0
    assert out.home_moneyline == -280


class FailingSession:
    def get(self, *args, **kwargs):
        import requests
        raise requests.ConnectionError("offline")


def test_live_lines_fail_soft(monkeypatch):
    monkeypatch.delenv("CFBD_API_KEY", raising=False)
    games = pd.DataFrame({"game_id": [1], "season": [2026], "season_type": ["regular"],
                          "kickoff": [pd.Timestamp("2026-10-24 19:30", tz="UTC")]})
    out = live_lines(games, session=FailingSession())
    assert out.empty


def test_returning_production_counts_transfers_and_departures():
    prev = pd.DataFrame([
        dict(athlete_id=1, team="State", pass_yds=3000, rec_yds=0, rush_yds=200, def_plays=0),     # leaves
        dict(athlete_id=2, team="State", pass_yds=0, rec_yds=800, rush_yds=0, def_plays=0),        # stays
        dict(athlete_id=3, team="Tech", pass_yds=2800, rec_yds=0, rush_yds=100, def_plays=0),      # transfers in
        dict(athlete_id=4, team="Small", pass_yds=0, rec_yds=1000, rush_yds=0, def_plays=0),       # moves up
        dict(athlete_id=5, team="State", pass_yds=0, rec_yds=200, rush_yds=0, def_plays=10),
    ])
    roster = pd.DataFrame({"athlete_id": [2, 3, 4], "team": ["State"] * 3})
    div = pd.Series({"State": "fbs", "Tech": "fbs", "Small": "fcs"})
    out = returning_production(prev, roster, div, div, 2026).set_index("team")
    state = out.loc["State"]
    assert np.isclose(state.ret_pass, 2800 / 3000)
    assert np.isclose(state.ret_rec, (800 + 0.5 * 1000) / 1000)   # FCS transfer at half credit
    assert np.isclose(state.ret_def, 0.0)
    assert state.transfers_in == 2
    assert "Tech" not in out.index                                # no roster this season


def test_returning_rebuilds_until_the_season_starts(monkeypatch, tmp_path):
    from cfbpredictor import returning

    monkeypatch.setattr(returning, "RETURNING_PATH", tmp_path / "returning.csv")
    calls = []

    def fake_build(seasons, max_age_hours=6.0):
        calls.append(list(seasons))
        return pd.DataFrame({"season": [2027], "team": ["State"], "ret_pass": [0.5 + 0.1 * len(calls)],
                             "ret_rec": [0.5], "ret_rush": [0.5], "ret_def": [0.5], "ret_off": [0.5],
                             "transfers_in": [3]})

    monkeypatch.setattr(returning, "build_returning", fake_build)
    first = returning.update_returning(2027, started=False)
    second = returning.update_returning(2027, started=False)      # a newer roster replaces the old rows
    assert len(second) == 1 and second.iloc[0].ret_pass > first.iloc[0].ret_pass
    frozen = returning.update_returning(2027, started=True)        # games have been played: keep it
    assert len(calls) == 2 and frozen.iloc[0].ret_pass == second.iloc[0].ret_pass


class ScoreboardSession:
    """Answers each day's scoreboard request; one day fails."""

    def __init__(self):
        self.days = []

    def get(self, url, params=None, headers=None, timeout=None):
        import requests

        self.days.append(params["dates"])
        day = params["dates"]

        class Resp:
            def raise_for_status(self):
                if day == "20261023":
                    raise requests.HTTPError("400 Client Error")

            def json(self):
                if day == "20261025":
                    return {"events": []}             # a day with no FBS games
                return {"events": [e for e in ESPN_PAYLOAD["events"] if e["id"] == "401"]}
        return Resp()


def test_espn_lines_are_fetched_day_by_day(monkeypatch):
    monkeypatch.delenv("CFBD_API_KEY", raising=False)
    games = pd.DataFrame({"game_id": [401, 402, 403], "season": [2026] * 3, "season_type": ["regular"] * 3,
                          "kickoff": [pd.Timestamp("2026-10-24 23:30", tz="UTC"),       # Saturday ET
                                      pd.Timestamp("2026-10-24 01:00", tz="UTC"),       # Friday night ET
                                      pd.Timestamp("2026-10-25 18:00", tz="UTC")]})     # Sunday
    session = ScoreboardSession()
    out = live_lines(games, session=session)
    assert session.days == ["20261023", "20261024", "20261025"]
    assert list(out["game_id"]) == [401] and out.iloc[0].spread_line == 10.5
    # Empty days must not turn the numbers into objects (the pick table subtracts them).
    assert out["spread_line"].dtype == float and out["total_line"].dtype == float
