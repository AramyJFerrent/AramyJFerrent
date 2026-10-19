import numpy as np
import pandas as pd

from ufcpredictor.data import build_bouts, build_fighters, build_stats, parse_time_format, parse_weightclass
from ufcpredictor.names import match_name, normalize_name, pair_key


def raw_tables():
    events = pd.DataFrame({
        "EVENT": ["UFC Fight Night: A vs. B", "UFC 300: C vs. D"],
        "URL": ["e1", "e2"], "DATE": ["October 17, 2026", "April 13, 2024"],
        "LOCATION": ["Edmonton, Alberta, Canada", "Las Vegas, Nevada, USA"],
    })
    results = pd.DataFrame({
        "EVENT": ["UFC Fight Night: A vs. B ", "UFC Fight Night: A vs. B ", "Noche UFC: A vs. B ", "UFC 300: C vs. D"],
        "BOUT": ["Bruno Silva vs. Ann Ray", "Cal Poe vs. Dee Oak", "Cal Poe vs. Dee Oak", "Bruno Silva vs. Eve Fox"],
        "OUTCOME": ["L/W", "W/L", "W/L", "D/D"],
        "WEIGHTCLASS": ["Middleweight Bout", "UFC Women's Flyweight Title Bout", "UFC Women's Flyweight Title Bout",
                        "Flyweight Bout"],
        "METHOD": ["KO/TKO ", "Decision - Split ", "Decision - Split ", "Decision - Majority "],
        "ROUND": ["2", "5", "5", "3"], "TIME": ["2:32", "5:00", "5:00", "5:00"],
        "TIME FORMAT": ["3 Rnd (5-5-5)", "5 Rnd (5-5-5-5-5)", "5 Rnd (5-5-5-5-5)", "3 Rnd (5-5-5)"],
        "REFEREE": ["Marc Goddard"] * 4, "DETAILS": [""] * 4,
        "URL": ["http://ufcstats.com/fight-details/b1", "http://ufcstats.com/fight-details/b2",
                "http://ufcstats.com/fight-details/b2", "http://ufcstats.com/fight-details/b3"],
    })
    tott = pd.DataFrame({
        "FIGHTER": ["Bruno Silva", "Bruno Silva", "Ann Ray"],
        "HEIGHT": ["5' 4\"", "6' 0\"", "--"], "WEIGHT": ["125 lbs.", "185 lbs.", "185 lbs."],
        "REACH": ["65\"", "74\"", "--"], "STANCE": ["Orthodox", "Orthodox", ""],
        "DOB": ["Mar 16, 1990", "Jul 13, 1989", "--"],
        "URL": ["http://ufcstats.com/fighter-details/fly", "http://ufcstats.com/fighter-details/mid",
                "http://ufcstats.com/fighter-details/ann"],
    })
    stats = pd.DataFrame({
        "EVENT": ["UFC Fight Night: A vs. B"] * 4 + ["Noche UFC: A vs. B"],
        "BOUT": ["Bruno Silva vs. Ann Ray"] * 4 + ["Cal Poe vs. Dee Oak"],
        "ROUND": ["Round 1", "Round 2", "Round 1", "Round 2", "Round 1"],
        "FIGHTER": ["Bruno Silva", "Bruno Silva", "Ann Ray", "Ann Ray", "Cal Poe"],
        "KD": ["0", "0", "1", "1", "0"], "SIG.STR.": ["9 of 37", "5 of 16", "10 of 20", "4 of 8", "1 of 2"],
        "SIG.STR. %": [""] * 5, "TOTAL STR.": ["9 of 37", "11 of 22", "10 of 20", "4 of 8", "1 of 2"],
        "TD": ["0 of 0", "1 of 3", "0 of 1", "0 of 0", "0 of 0"], "TD %": [""] * 5,
        "SUB.ATT": ["0", "1", "0", "0", "0"], "REV.": ["0"] * 5, "CTRL": ["0:00", "1:08", "0:10", "0:00", "0:00"],
        **{c: ["0 of 0"] * 5 for c in ("HEAD", "BODY", "LEG", "DISTANCE", "CLINCH", "GROUND")},
    })
    return events, results, tott, stats


def test_field_parsers():
    assert parse_weightclass("UFC Women's Flyweight Title Bout") == ("Women's Flyweight", "F", True)
    assert parse_weightclass("Light Heavyweight Bout") == ("Light Heavyweight", "M", False)
    assert parse_weightclass("Heavyweight Bout") == ("Heavyweight", "M", False)
    assert parse_weightclass("Ultimate Fighter 33 Welterweight Tournament Title Bout") == ("Welterweight", "M", False)
    assert parse_weightclass("Catch Weight Bout")[0] == "Catch Weight"
    assert parse_time_format("5 Rnd (5-5-5-5-5)") == (5, [5, 5, 5, 5, 5])
    assert parse_time_format("No Time Limit") == (0, [])


def test_bouts_dedupe_order_and_shared_names():
    events, results, tott, stats = raw_tables()
    fighters = build_fighters(tott)
    bouts = build_bouts(results, events, fighters)
    assert len(bouts) == 3                                   # renamed event copy dropped
    assert list(bouts["bout_id"]) == ["b3", "b2", "b1"]      # by date; within a card, main event last
    b1 = bouts.set_index("bout_id").loc["b1"]
    assert (b1.winner, b1.method, b1.end_round, b1.fight_seconds) == ("b", "KO", 2, 452.0)
    assert b1.a_id == "mid"                                  # Bruno Silva at middleweight
    b3 = bouts.set_index("bout_id").loc["b3"]
    assert b3.a_id == "fly" and b3.winner == "draw" and b3.method == "DRAW"
    b2 = bouts.set_index("bout_id").loc["b2"]
    assert b2.title and b2.rounds == 5 and b2.decision == "split" and b2.a_id == "x-cal-poe"

    s = build_stats(stats, results, bouts).set_index(["bout_id", "side"])
    assert s.loc[("b1", "a"), "sig_l"] == 14 and s.loc[("b1", "a"), "sig_a"] == 53
    assert s.loc[("b1", "a"), "ctrl"] == 68 and s.loc[("b1", "b"), "kd"] == 2
    assert s.loc[("b2", "a"), "sig_l"] == 1                  # stats filed under the renamed event still join
    assert np.isnan(build_fighters(tott).set_index("fighter_id").loc["ann", "reach"])


def test_names():
    assert normalize_name("Waldo Cortes-Acosta") == "waldo cortes acosta"
    assert normalize_name("Sean King III") == "sean king"
    assert normalize_name("José Aldo") == "jose aldo"
    pool = pd.Series({"1": "Waldo Cortes-Acosta", "2": "Kai Kara-France", "3": "Bruno Silva", "4": "Jean Silva"})
    assert match_name("Waldo Cortes Acosta", pool) == "1"
    assert match_name("Kai Kara France", pool) == "2"
    assert match_name("B. Silva", pool) == "3"
    assert match_name("Silva", pool) is None                 # ambiguous surname
    assert match_name("Totally New", pool) is None
    assert pair_key("B b", "A a") == pair_key("a a", "b b")
