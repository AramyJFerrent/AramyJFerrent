import numpy as np
import pandas as pd

from ufcpredictor.edges import fair_american
from ufcpredictor.pipeline import LOG_COLUMNS, grade, update_log
from ufcpredictor.report import grade as grade_table

NOW = pd.Timestamp("2026-10-22 12:00", tz="UTC")
FIGHT_NIGHT = pd.Timestamp("2026-10-24")
START = pd.Timestamp("2026-10-24 23:00", tz="UTC")


def entry(a, b, p=0.6, date=FIGHT_NIGHT, start=START, **kw):
    row = {c: np.nan for c in LOG_COLUMNS}
    row.update(bout_key=f"{a}-{b}", event="UFC Fight Night", order=0, date=date, start=start, division="Lightweight",
               rounds=3, title=False, fighter_a=a, fighter_b=b, a_id=a, b_id=b, p_a=p, p_model=p, p_market=np.nan,
               a_ko=0.2, a_sub=0.1, a_dec=p - 0.3, b_ko=0.15, b_sub=0.05, b_dec=0.8 - p, p_distance=0.5,
               best_side="a", best_method="dec", best_prob=p - 0.3, predicted_at=NOW, source="live",
               status="upcoming")
    row.update(kw)
    return row


def frame(*rows):
    return pd.DataFrame(list(rows), columns=LOG_COLUMNS)


def card_of(*pairs, date=FIGHT_NIGHT):
    return pd.DataFrame({"date": [date] * len(pairs), "fighter_a": [a for a, _ in pairs],
                         "fighter_b": [b for _, b in pairs]})


def test_refresh_before_start_and_lock_after():
    old = frame(entry("Ann", "Bea", p=0.55))
    new = frame(entry("Ann", "Bea", p=0.62))
    merged = update_log(old, new, card_of(("Ann", "Bea")), NOW)
    assert len(merged) == 1 and merged["p_a"].iloc[0] == 0.62

    after = START + pd.Timedelta(minutes=5)
    locked = update_log(merged, frame(entry("Ann", "Bea", p=0.70)), card_of(("Ann", "Bea")), after)
    assert locked["p_a"].iloc[0] == 0.62            # the pre-fight prediction stands


def test_replacement_drops_the_old_bout():
    old = frame(entry("Ann", "Bea"), entry("Cal", "Dee"))
    new = frame(entry("Ann", "Eve"), entry("Cal", "Dee"))
    merged = update_log(old, new, card_of(("Ann", "Eve"), ("Cal", "Dee")), NOW)
    assert sorted(merged["fighter_b"]) == ["Dee", "Eve"]
    # A card that was not read this run (another date) leaves its bouts alone.
    other = frame(entry("Gus", "Hal", date=pd.Timestamp("2026-10-31"), start=START + pd.Timedelta(days=7)))
    kept = update_log(pd.concat([merged, other]), frame(), card_of(("Ann", "Eve"), ("Cal", "Dee")), NOW)
    assert "Gus" in set(kept["fighter_a"])


def test_same_bout_from_another_source_is_one_bout():
    old = frame(entry("Jose Aldo", "Max Holloway", bout_key="ufcstats-1"))
    new = frame(entry("Max Holloway", "José Aldo", p=0.3, bout_key="espn-9"))
    merged = update_log(old, new, card_of(("Max Holloway", "José Aldo")), NOW)
    assert len(merged) == 1 and merged["bout_key"].iloc[0] == "espn-9"


def test_first_price_is_kept_in_the_original_orientation():
    first = frame(entry("Ann", "Bea", odds_a=-150, odds_b=130, first_odds_a=-150, first_odds_b=130,
                        first_p_model=0.6, first_predicted_at=NOW - pd.Timedelta(days=2)))
    later = frame(entry("Bea", "Ann", p=0.35, odds_a=150, odds_b=-170, first_odds_a=150, first_odds_b=-170,
                        first_p_model=0.35, first_predicted_at=NOW))
    row = update_log(first, later, card_of(("Bea", "Ann")), NOW).iloc[0]
    assert row.fighter_a == "Bea" and row.odds_a == 150
    assert (row.first_odds_a, row.first_odds_b) == (130, -150)      # Bea's first price
    assert abs(row.first_p_model - 0.4) < 1e-9


def test_grading_flips_to_the_logged_corner_and_marks_cancellations():
    log = frame(entry("Ann", "Bea"), entry("Cal", "Dee"))
    bouts = pd.DataFrame({"date": [FIGHT_NIGHT], "fighter_a": ["Bea"], "fighter_b": ["Ann"], "a_id": ["Bea"],
                          "b_id": ["Ann"], "winner": ["a"], "method": ["KO"], "end_round": [2]})
    graded = grade(log, bouts).set_index("fighter_a")
    assert graded.loc["Ann", "winner"] == "b" and graded.loc["Ann", "method"] == "KO"
    assert graded.loc["Ann", "status"] == "final"
    assert graded.loc["Cal", "status"] == "cancelled"      # card is in the results, this bout is not


def test_grading_uses_ids_before_spellings():
    log = frame(entry("Alex Volkanovski", "Bea", a_id="volk", b_id="bea"))
    bouts = pd.DataFrame({"date": [FIGHT_NIGHT], "fighter_a": ["Bea"], "fighter_b": ["Alexander Volkanovski"],
                          "a_id": ["bea"], "b_id": ["volk"], "winner": ["b"], "method": ["DEC"], "end_round": [5]})
    row = grade(log, bouts).iloc[0]
    assert row.status == "final" and row.winner == "a"           # Volkanovski won, logged in corner A
    # Without ids, a close spelling still finds the right corner.
    log = frame(entry("Waldo Cortes Acosta", "Bea", a_id="x-1", b_id="x-2"))
    bouts = bouts.assign(fighter_b="Waldo Cortes-Acosta Jr.", a_id="p", b_id="q")
    row = grade(log, bouts).iloc[0]
    assert row.status == "final" and row.winner == "a"


def test_results_from_a_day_later_still_match():
    log = frame(entry("Ann", "Bea", date=pd.Timestamp("2026-11-06")))     # US date of a Sydney card
    bouts = pd.DataFrame({"date": [pd.Timestamp("2026-11-07")], "fighter_a": ["Ann"], "fighter_b": ["Bea"],
                          "a_id": ["Ann"], "b_id": ["Bea"], "winner": ["b"], "method": ["DEC"], "end_round": [3]})
    row = grade(log, bouts).iloc[0]
    assert row.winner == "b" and row.status == "final"


def test_grade_table_and_fair_odds():
    log = frame(entry("Ann", "Bea", p=0.7, p_market=0.65, status="final", winner="a"),
                entry("Cal", "Dee", p=0.6, status="final", winner="b"))
    table = grade_table(log).set_index("Predictor")
    expected = -(np.log(0.7) + np.log(0.4)) / 2
    assert abs(table.loc["Final prediction", "Log loss"] - expected) < 1e-9
    assert table.loc["Market price when predicted", "Fights"] == 1
    assert fair_american(0.75) == -300 and fair_american(0.25) == 300 and fair_american(0.5) == 100
