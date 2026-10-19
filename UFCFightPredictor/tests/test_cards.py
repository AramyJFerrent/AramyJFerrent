import numpy as np
import pandas as pd

from ufcpredictor.cards import (attach_espn, fallback_start, five_rounds, parse_espn, parse_event_page,
                                parse_upcoming_list, resolve_card_ids)

UPCOMING = """
<table class="b-statistics__table-events"><tbody>
<tr class="b-statistics__table-row"><td class="b-statistics__table-col b-statistics__table-col_type_clear"></td></tr>
<tr class="b-statistics__table-row">
  <td class="b-statistics__table-col">
    <i class="b-statistics__table-content">
      <a href="http://ufcstats.com/event-details/aaa111" class="b-link b-link_style_white">
        UFC Fight Night: Smith vs. Jones
      </a>
      <span class="b-statistics__date">
        October 24, 2026
      </span>
    </i>
  </td>
  <td class="b-statistics__table-col b-statistics__table-col_style_big-top-padding">
    Las Vegas, Nevada, USA
  </td>
</tr>
<tr class="b-statistics__table-row">
  <td class="b-statistics__table-col">
    <i class="b-statistics__table-content">
      <a href="http://ufcstats.com/event-details/bbb222" class="b-link b-link_style_black">
        UFC 333: Kim vs. Lee
      </a>
      <span class="b-statistics__date">November 07, 2026</span>
    </i>
  </td>
  <td class="b-statistics__table-col b-statistics__table-col_style_big-top-padding">Sydney, New South Wales, Australia</td>
</tr>
</tbody></table>
"""

EVENT = """
<h2 class="b-content__title"><span class="b-content__title-highlight">
  UFC Fight Night: Smith vs. Jones
</span></h2>
<ul class="b-list__box-list">
  <li class="b-list__box-list-item"><i class="b-list__box-item-title">Date:</i> October 24, 2026 </li>
  <li class="b-list__box-list-item"><i class="b-list__box-item-title">Location:</i> Las Vegas, Nevada, USA </li>
</ul>
<table class="b-fight-details__table"><tbody class="b-fight-details__table-body">
<tr class="b-fight-details__table-row b-fight-details__table-row__hover js-fight-details-click"
    data-link="http://ufcstats.com/fight-details/f001" onclick="doNav('http://ufcstats.com/fight-details/f001')">
  <td class="b-fight-details__table-col"><p class="b-fight-details__table-text"></p></td>
  <td class="b-fight-details__table-col l-page_align_left">
    <p class="b-fight-details__table-text"><a href="http://ufcstats.com/fighter-details/id-smith" class="b-link b-link_style_black">John Smith</a></p>
    <p class="b-fight-details__table-text"><a href="http://ufcstats.com/fighter-details/id-jones" class="b-link b-link_style_black">Jon Jones Jr.</a></p>
  </td>
  <td class="b-fight-details__table-col l-page_align_left">
    <p class="b-fight-details__table-text">Light Heavyweight
      <img src="http://1e49bc5171d173577ecd-1323f4090557a33db01577564f60846c.r80.cf1.rackcdn.com/belt.png" style="width: 20px">
    </p>
  </td>
</tr>
<tr class="b-fight-details__table-row b-fight-details__table-row__hover js-fight-details-click"
    data-link="http://ufcstats.com/fight-details/f002">
  <td class="b-fight-details__table-col l-page_align_left">
    <p class="b-fight-details__table-text"><a href="http://ufcstats.com/fighter-details/id-ana" class="b-link b-link_style_black">Ana Souza</a></p>
    <p class="b-fight-details__table-text"><a href="http://ufcstats.com/fighter-details/id-bea" class="b-link b-link_style_black">Bea Lima</a></p>
  </td>
  <td class="b-fight-details__table-col l-page_align_left"><p class="b-fight-details__table-text">Women's Strawweight</p></td>
</tr>
</tbody></table>
"""


def espn_payload(odds=None, home_first=True, competitors_extra=None):
    smith = {"id": "11", "order": 1, "athlete": {"id": "11", "displayName": "John Smith"},
             "records": [{"summary": "20-3-0"}]}
    jones = {"id": "22", "order": 2, "athlete": {"id": "22", "displayName": "Jon Jones"},
             "records": [{"summary": "27-1-0"}]}
    if home_first:
        smith["homeAway"], jones["homeAway"] = "home", "away"
    if competitors_extra:
        competitors_extra(smith, jones)
    comp = {"id": "401", "date": "2026-10-25T02:00Z", "competitors": [smith, jones],
            "type": {"text": "Light Heavyweight - Title Fight"}, "format": {"regulation": {"periods": 5}},
            "status": {"type": {"state": "pre"}}}
    if odds is not None:
        comp["odds"] = [odds]
    prelim = {"id": "400", "date": "2026-10-24T23:00Z", "type": {"text": "Women's Strawweight"},
              "competitors": [{"order": 1, "athlete": {"displayName": "Ana Souza"}},
                              {"order": 2, "athlete": {"displayName": "Bea Lima"}}]}
    return {"events": [{"id": "9", "name": "UFC Fight Night: Smith vs. Jones", "date": "2026-10-24T23:00Z",
                        "competitions": [prelim, comp]}]}


def test_upcoming_list_and_event_page():
    events = parse_upcoming_list(UPCOMING)
    assert list(events["url"]) == ["http://ufcstats.com/event-details/aaa111", "http://ufcstats.com/event-details/bbb222"]
    assert events["event"][0] == "UFC Fight Night: Smith vs. Jones"
    assert events["date"][1] == pd.Timestamp("2026-11-07")
    assert events["location"][1].endswith("Australia")

    info, bouts = parse_event_page(EVENT)
    assert info == {"event": "UFC Fight Night: Smith vs. Jones", "date": "October 24, 2026",
                    "location": "Las Vegas, Nevada, USA"}
    assert list(bouts["bout_id"]) == ["f001", "f002"]
    first = bouts.iloc[0]
    assert (first.a_id, first.fighter_a, first.b_id, first.fighter_b) == ("id-smith", "John Smith", "id-jones",
                                                                          "Jon Jones Jr.")
    assert first.division == "Light Heavyweight" and bool(first.title)
    second = bouts.iloc[1]
    assert second.division == "Women's Strawweight" and second.gender == "F" and not second.title


def test_espn_odds_need_a_known_side():
    oriented = parse_espn(espn_payload({"provider": {"name": "DraftKings"}, "details": "Jones -250",
                                        "homeAthleteOdds": {"moneyLine": 200}, "awayAthleteOdds": {"moneyLine": -250}}))
    main = oriented.set_index("espn_id").loc["401"]
    assert (main.odds_a, main.odds_b) == (200.0, -250.0)
    assert main.odds_source == "ESPN (DraftKings)"
    assert main.division == "Light Heavyweight" and main.title and main.rounds_espn == 5
    assert main.a_record == "20-3-0" and main.espn_order == 0       # last listed is the main event

    # No home/away flags and no athlete ids on the prices: refuse rather than guess.
    blind = parse_espn(espn_payload({"homeAthleteOdds": {"moneyLine": 200}, "awayAthleteOdds": {"moneyLine": -250}},
                                    home_first=False))
    assert np.isnan(blind.set_index("espn_id").loc["401", "odds_a"])

    # Athlete ids on the prices orient them even without home/away flags.
    by_id = parse_espn(espn_payload({"homeAthleteOdds": {"moneyLine": -250, "athlete": {"id": "22"}},
                                     "awayAthleteOdds": {"moneyLine": 200, "athlete": {"id": "11"}}},
                                    home_first=False))
    row = by_id.set_index("espn_id").loc["401"]
    assert (row.odds_a, row.odds_b) == (200.0, -250.0)

    # A summary naming the other fighter as favorite means the flags are wrong: drop.
    wrong = parse_espn(espn_payload({"details": "Smith -250", "homeAthleteOdds": {"moneyLine": 200},
                                     "awayAthleteOdds": {"moneyLine": -250}}))
    assert np.isnan(wrong.set_index("espn_id").loc["401", "odds_a"])

    # The newer nested format.
    nested = parse_espn(espn_payload({"moneyline": {"home": {"close": {"odds": "+180"}},
                                                    "away": {"close": {"odds": "-220"}}}}))
    row = nested.set_index("espn_id").loc["401"]
    assert (row.odds_a, row.odds_b) == (180.0, -220.0)


def test_attach_espn_matches_names_and_flips_prices():
    _, card = parse_event_page(EVENT)
    card = card.rename(columns={"bout_id": "bout_key"})
    card["date"] = pd.Timestamp("2026-10-24")
    # ESPN lists Jones first this time and drops the suffix.
    espn = parse_espn(espn_payload({"homeAthleteOdds": {"moneyLine": -250}, "awayAthleteOdds": {"moneyLine": 200}},
                                   competitors_extra=lambda s, j: (s.update(order=2), j.update(order=1))))
    out = attach_espn(card, espn).set_index("bout_key")
    assert (out.loc["f001", "odds_a"], out.loc["f001", "odds_b"]) == (-250.0, 200.0)   # Smith home at -250
    assert out.loc["f001", "start"] == pd.Timestamp("2026-10-25T02:00Z")
    assert out.loc["f001", "a_record"] == "20-3-0"
    assert np.isnan(out.loc["f002", "odds_a"]) and out.loc["f002", "start"] == pd.Timestamp("2026-10-24T23:00Z")


def test_rounds_and_lock_time_fallbacks():
    assert five_rounds(0, False, "UFC Fight Night: A vs. B", "x", "y")
    assert five_rounds(4, True, "UFC 330: A vs. B", "x", "y")
    assert five_rounds(3, False, "UFC 330: Smith vs. Jones", "Jon Jones", "John Smith")
    assert not five_rounds(3, False, "UFC 330: Smith vs. Jones", "Ana Souza", "Bea Lima")
    assert fallback_start(pd.Timestamp("2026-11-07"), "Sydney, New South Wales, Australia").hour == 4
    assert fallback_start(pd.Timestamp("2026-10-24"), "Las Vegas, Nevada, USA").hour == 20
    assert fallback_start(pd.Timestamp("2026-10-24"), "Abu Dhabi, Abu Dhabi, United Arab Emirates").hour == 13


def test_card_ids_prefer_history():
    known = pd.Series({"h-smith": "John Smith", "x-jon-jones": "Jon Jones"})
    card = pd.DataFrame({"a_id": ["h-smith", None], "fighter_a": ["John Smith", "New Guy"],
                         "b_id": ["id-jones", "id-new"], "fighter_b": ["Jon Jones Jr.", "Other Guy"]})
    out = resolve_card_ids(card, known)
    assert list(out["a_id"]) == ["h-smith", "x-new-guy"]
    assert list(out["b_id"]) == ["x-jon-jones", "id-new"]        # history keyed by name; debutant keeps card id


def test_fetch_card_merges_sources_and_survives_failures(monkeypatch, tmp_path):
    import requests

    from ufcpredictor import cards

    _, bouts = parse_event_page(EVENT)
    bouts = bouts.rename(columns={"bout_id": "bout_key"})
    bouts["event"], bouts["date"] = "UFC Fight Night: Smith vs. Jones", pd.Timestamp("2026-10-24")
    bouts["location"], bouts["order"], bouts["source"] = "Las Vegas, Nevada, USA", [0, 1], "UFCStats"
    espn = parse_espn(espn_payload({"homeAthleteOdds": {"moneyLine": 200}, "awayAthleteOdds": {"moneyLine": -250}}))
    monkeypatch.setattr(cards, "MANUAL_PATH", tmp_path / "manual_card.csv")
    monkeypatch.setattr(cards, "ufcstats_cards", lambda now, days, session: bouts.copy())
    monkeypatch.setattr(cards, "espn_cards", lambda now, days, session: espn)
    now = pd.Timestamp("2026-10-22", tz="UTC")
    known = pd.Series({"id-smith": "John Smith", "id-ana": "Ana Souza"})
    card = cards.fetch_card(now, 15, known, {"id-ana": "Women's Strawweight"}).set_index("bout_key")
    assert list(card.index) == ["f001", "f002"]
    assert card.loc["f001", "rounds"] == 5 and card.loc["f002", "rounds"] == 3
    assert card.loc["f001", "odds_a"] == 200.0 and card.loc["f001", "gender"] == "M"
    assert card.loc["f002", "start"] == pd.Timestamp("2026-10-24T23:00Z")

    # UFCStats down: ESPN alone still gives a card, with names matched to known ids.
    def down(*args):
        raise requests.ConnectionError("down")
    monkeypatch.setattr(cards, "ufcstats_cards", down)
    alone = cards.fetch_card(now, 15, known, {"id-ana": "Women's Strawweight"})
    assert len(alone) == 2 and set(alone["a_id"]) == {"id-smith", "id-ana"}
    assert alone.set_index("a_id").loc["id-smith", "rounds"] == 5

    # Everything down and no manual card: an empty card, not an error.
    monkeypatch.setattr(cards, "espn_cards", down)
    assert cards.fetch_card(now, 15, known, {}).empty


def test_event_rows_without_fight_links_still_parse():
    page = EVENT.replace('data-link="http://ufcstats.com/fight-details/f002"', "")
    _, bouts = parse_event_page(page)
    assert list(bouts["bout_id"]) == ["f001", "id-ana-id-bea"]
