import numpy as np
import pandas as pd

from mlbpredictor.statsapi import assign_parks, parse_boxscore, parse_schedule, parse_weather


def game(pk, date, status, home=147, away=111, **kw):
    g = {"gamePk": pk, "gameType": "R", "season": "2026", "officialDate": date,
         "gameDate": f"{date}T23:05:00Z", "status": {"abstractGameState": status, "detailedState": status},
         "teams": {"home": {"team": {"id": home}}, "away": {"team": {"id": away}}},
         "venue": {"id": 3313, "name": "Yankee Stadium"}, "doubleHeader": "N", "gameNumber": 1, "dayNight": "night"}
    g.update(kw)
    return g


def test_schedule_parses_finals_upcoming_and_postponed_games():
    final = game(1, "2026-04-01", "Final", linescore={
        "currentInning": 9, "scheduledInnings": 9,
        "innings": [{"num": i, "home": {"runs": 1 if i == 3 else 0}, "away": {"runs": 0}} for i in range(1, 9)]
        + [{"num": 9, "home": {}, "away": {"runs": 0}}]})
    final["teams"]["home"]["score"], final["teams"]["away"]["score"] = 1, 0
    upcoming = game(2, "2026-04-02", "Preview", weather={"condition": "Roof Closed", "temp": "71", "wind": "0 mph, None"},
                    lineups={"homePlayers": [{"id": 10 + i, "primaryPosition": {"code": str(i + 2)}} for i in range(9)]})
    upcoming["teams"]["home"]["probablePitcher"] = {"id": 543037, "fullName": "Gerrit Cole"}
    postponed = game(3, "2026-04-03", "Postponed")
    replayed = game(3, "2026-04-04", "Preview")
    other = game(4, "2026-04-04", "Preview", home=999)        # not an MLB team: dropped
    payload = {"dates": [{"date": d, "games": gs} for d, gs in
                         (("2026-04-01", [final]), ("2026-04-02", [upcoming]),
                          ("2026-04-03", [postponed]), ("2026-04-04", [replayed, other]))]}
    s = parse_schedule(payload).set_index("game_id")
    assert list(s.index) == ["1", "2", "3"]
    assert s.loc["1", "status"] == "final" and s.loc["1", "home_line"] == "0 0 1 0 0 0 0 0 x"
    assert s.loc["1", "home_score"] == 1 and s.loc["1", "tiebreaker"] == 1 and s.loc["1", "home_team"] == "NYY"
    assert s.loc["2", "status"] == "scheduled" and np.isnan(s.loc["2", "home_score"])
    assert s.loc["2", "home_starter"] == "543037" and s.loc["2", "dome"] == 1 and s.loc["2", "temp"] == 71
    assert s.loc["2", "home_lineup_ids"][0] == "10" and len(s.loc["2", "home_lineup_ids"]) == 9
    assert s.loc["3", "date"] == "2026-04-04" and s.loc["3", "status"] == "scheduled"


def test_weather_text():
    w = parse_weather({"condition": "Partly Cloudy", "temp": "84", "wind": "12 mph, Out To CF"})
    assert w == {"temp": 84.0, "dome": 0, "wind": "out", "wind_speed": 12.0}
    assert parse_weather({"wind": "5 mph, In From LF"})["wind"] == "in"
    assert np.isnan(parse_weather({})["temp"])


def test_boxscore_rows():
    def batter(pid, order, pos, **stats):
        return {"person": {"id": pid}, "battingOrder": order, "position": {"code": pos},
                "stats": {"batting": stats, "pitching": {}}}
    payload = {"teams": {
        "home": {"team": {"id": 147}, "pitchers": [1, 2], "players": {
            "ID1": {"person": {"id": 1}, "position": {"code": "1"}, "stats": {"batting": {}, "pitching": {
                "outs": 18, "battersFaced": 24, "numberOfPitches": 95, "strikeOuts": 7, "baseOnBalls": 2,
                "hits": 5, "doubles": 1, "homeRuns": 1, "runs": 2, "earnedRuns": 2}}},
            "ID2": {"person": {"id": 2}, "position": {"code": "1"}, "stats": {"batting": {}, "pitching": {
                "outs": 9, "battersFaced": 10, "pitchesThrown": 40, "hitByPitch": 1}}},
            "ID3": batter(3, "100", "8", plateAppearances=5, hits=2, doubles=1, homeRuns=1, strikeOuts=1,
                          baseOnBalls=1, intentionalWalks=1),
            "ID4": batter(4, "101", "11", plateAppearances=1),
            "ID5": batter(5, None, "6", plateAppearances=0)}},
        "away": {"team": {"id": 111}, "pitchers": [], "players": {}}},
        "info": [{"label": "Weather", "value": "68 degrees, Clear."}, {"label": "Wind", "value": "7 mph, L To R."}]}
    out = parse_boxscore(payload, "77")
    bat = pd.DataFrame(out["batting"]).set_index("player_id")
    assert set(bat.index) == {"3", "4"}
    assert bat.loc["3", "slot"] == 1 and bat.loc["4", "slot"] == 0 and bat.loc["3", "pos"] == 8
    assert (bat.loc["3", ["s", "d", "hr", "bb", "ibb", "out"]] == [0, 1, 1, 1, 1, 1]).all()
    pit = pd.DataFrame(out["pitching"]).set_index("player_id")
    assert pit.loc["1", "starter"] == 1 and pit.loc["2", "starter"] == 0 and pit.loc["2", "pitches"] == 40
    assert pit.loc["1", "s"] == 3 and pit.loc["1", "out"] == 24 - 7 - 2 - 5
    assert out["starters"] == {"home": "1"} and out["weather"]["wind"] == "cross" and out["weather"]["temp"] == 68


def test_parks_carry_over_from_retrosheet_and_follow_moves():
    history = pd.DataFrame({"season": [2025] * 3, "home_team": ["NYY", "NYY", "TB"],
                            "park_id": ["NYC21", "NYC21", "TAM02"]})
    games = pd.DataFrame({"season": [2026] * 4, "home_team": ["NYY", "NYY", "TB", "NYY"],
                          "venue_id": [3313, 3313, 12, 5000]})
    games = pd.concat([games, games.iloc[[0]]], ignore_index=True)
    parks = assign_parks(games, history)
    assert list(parks[:4]) == ["NYC21", "NYC21", "STP01", "MLB5000"]
