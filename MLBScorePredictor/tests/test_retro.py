from mlbpredictor.retro import END, advance, parse_events, parse_play, state_code


def run(event, bases, pitcher="p1"):
    return advance(bases, parse_play(event), pitcher)


def test_hits_walks_and_home_runs_move_runners():
    bases, outs, scored = run("S8/L.2-H;1-3", {1: "a", 2: "b"})
    assert bases == {1: "p1", 3: "a"} and outs == 0 and scored == ["b"]
    bases, outs, scored = run("W", {1: "a", 2: "b"})          # forced runners move up when not listed
    assert bases == {1: "p1", 2: "a", 3: "b"} and scored == []
    bases, outs, scored = run("HR/F7", {1: "a", 3: "c"})       # unmentioned runners score on a homer
    assert bases == {} and sorted(scored) == ["a", "c", "p1"]
    bases, outs, scored = run("D7/L.1-3", {1: "a"})
    assert bases == {2: "p1", 3: "a"}


def test_outs_double_plays_and_force_plays():
    assert run("63/G", {}) == ({}, 1, [])
    bases, outs, _ = run("64(1)3/GDP", {1: "a"})
    assert bases == {} and outs == 2
    bases, outs, _ = run("64(1)/FO/G6.B-1", {1: "a"})          # force at second, batter safe
    assert bases == {1: "p1"} and outs == 1
    bases, outs, _ = run("2E3/G.B-2", {})                      # throwing error: batter not out
    assert bases == {2: "p1"} and outs == 0
    bases, outs, _ = run("63!/G", {})                          # exceptional-play mark
    assert outs == 1


def test_strikeouts_steals_and_errors_that_cancel_outs():
    bases, outs, _ = run("K+SB2", {1: "a"})
    assert bases == {2: "a"} and outs == 1
    bases, outs, _ = run("K+WP.B-1", {})
    assert bases == {1: "p1"} and outs == 0
    bases, outs, _ = run("CS2(24)", {1: "a"})
    assert bases == {} and outs == 1
    bases, outs, _ = run("CS2(2E4).1-3", {1: "a"})
    assert bases == {3: "a"} and outs == 0
    bases, outs, scored = run("S9.2XH(92)", {2: "b"})          # thrown out at home
    assert outs == 1 and scored == []
    bases, outs, scored = run("S9.2XH(E2)", {2: "b"})          # error on the throw: safe
    assert outs == 0 and scored == ["b"]
    bases, outs, scored = run("7/SF.3-H(UR);1XH(82)(E3/TH)", {1: "a", 3: "c"})  # error came first, out stands
    assert outs == 2 and scored == ["c"]
    bases, outs, _ = run("PO1(13)", {1: "a"})
    assert bases == {} and outs == 1


def test_state_codes():
    assert state_code({}, 0) == 0 and state_code({1: "a", 3: "c"}, 2) == 5 + 16


GAME = """id,NYA202504010
version,2
info,visteam,BOS
info,hometeam,NYA
info,site,NYC21
info,date,2025/04/01
info,number,0
info,starttime,7:05PM
info,daynight,night
info,innings,9
info,tiebreaker,2
info,temp,61
info,winddir,tocf
info,windspeed,9
info,sky,cloudy
start,awayp,"Away Pitcher",0,0,1
start,a1,"A One",0,1,8
start,homep,"Home Pitcher",1,0,1
start,h1,"H One",1,1,6
play,1,0,a1,10,BX,S8/G
play,1,0,a1,00,,NP
play,1,0,a2,22,BBSSX,HR/F8.1-H
play,1,0,a3,01,CX,8/F
play,1,0,a4,12,CFBS,K
play,1,0,a5,00,X,63/G
play,1,1,h1,32,BBCBFB,W
play,1,1,h2,00,X,64(1)3/GDP
sub,relief,"Home Reliever",1,0,1
play,1,1,h3,02,CSS,K
play,2,0,a6,00,X,43/G
play,2,0,a7,00,X,53/G
play,2,0,a8,00,X,13/G
play,2,1,h4,11,BCX,HR/F7
play,2,1,h5,00,X,8/F
play,2,1,h6,00,X,7/F
play,2,1,h7,00,X,9/F
data,er,homep,2
"""


def test_a_game_parses_into_lines_players_and_transitions():
    hands = {"a1": ("L", "R"), "homep": ("R", "R"), "relief": ("L", "L"), "h1": ("R", "R")}
    games, transitions, platoon = parse_events(GAME, 2025, hands)
    g = games[0]["game"]
    assert (g["home_team"], g["away_team"], g["park_id"]) == ("NYY", "BOS", "NYC21")
    assert g["away_line"] == "2 0" and g["home_line"] == "0 1"
    assert (g["away_score"], g["home_score"]) == (2, 1)
    assert g["wind"] == "out" and g["temp"] == 61 and g["tiebreaker"] == 1 and g["dome"] == 0
    assert g["start"].startswith("2025-04-01T23:05")
    pitching = {r["player_id"]: r for r in games[0]["pitching"]}
    assert pitching["homep"]["starter"] == 1 and pitching["homep"]["r"] == 2 and pitching["homep"]["er"] == 2
    assert pitching["homep"]["outs"] == 3 and pitching["homep"]["bf"] == 5 and pitching["homep"]["hr"] == 1
    assert pitching["awayp"]["outs"] == 6 and pitching["awayp"]["k"] == 1
    assert pitching["homep"]["pitches"] == 2 + 5 + 2 + 4 + 1
    batting = {r["player_id"]: r for r in games[0]["batting"]}
    assert batting["a1"]["slot"] == 1 and batting["a1"]["s"] == 1 and batting["a1"]["pa"] == 1
    assert batting["h2"]["out"] == 1 and batting["h2"]["slot"] == 0
    # Single from empty bases, then the homer that scored two with a runner on first.
    assert transitions[(0, "s", 1, 0)] == 1 and transitions[(1, "hr", 0, 2)] == 1
    assert transitions[(16, "out", END, 0)] == 3 and transitions[(16, "k", END, 0)] == 1
    assert platoon[("L", "R", "s")] == 1
