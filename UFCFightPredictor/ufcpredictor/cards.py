"""Upcoming fight cards: who fights whom, when, and at what price.

Three sources, merged:

1. **UFCStats** lists every announced bout with the same fighter ids as the
   history, so matching is exact. Its pages give the division and title belt
   but not start times or rounds; the main event and title fights are five
   rounds, everything else three.
2. **ESPN's** public scoreboard (no key needed) adds each card segment's start
   time and moneylines from its odds provider, and stands in for UFCStats if
   that site is down. ESPN names are matched to UFCStats names.
3. **``data/manual_card.csv``**, if present, adds or overrides bouts by hand
   (for example a late replacement either site has not caught up with).

Any source can fail; the others still produce a card, and a bout without a
price is predicted from the model alone.
"""

from __future__ import annotations

import html
import logging
import re

import numpy as np
import pandas as pd
import requests

from .config import DATA_DIR, DISPLAY_TZ, DIVISIONS, ESPN_SCOREBOARD_URL, UFCSTATS_UPCOMING_URL
from .data import parse_weightclass
from .names import match_name, normalize_name, pair_key

log = logging.getLogger(__name__)

MANUAL_PATH = DATA_DIR / "manual_card.csv"
CARD_COLUMNS = [
    "bout_key", "event", "date", "start", "location", "order", "fighter_a", "fighter_b", "a_id", "b_id",
    "division", "gender", "title", "rounds", "odds_a", "odds_b", "odds_source", "a_record", "b_record",
    "source",
]
HEADERS = {"User-Agent": "Mozilla/5.0 (UFCFightPredictor; +https://github.com)"}
# Without a start time from ESPN, lock predictions at this hour UTC on fight
# day: cards in Asia and Oceania start early, the Americas late.
FALLBACK_LOCK_HOUR = {"asia": 4, "europe": 13, "americas": 20}
ASIA_OCEANIA = ("Australia", "New Zealand", "China", "Japan", "Singapore", "Korea", "Macau", "Philippines",
                "Thailand", "India", "Indonesia")
EUROPE_MIDEAST = ("United Kingdom", "England", "Scotland", "Ireland", "France", "Germany", "Sweden", "Poland",
                  "Netherlands", "Denmark", "Czech", "Spain", "Italy", "Russia", "Azerbaijan", "United Arab Emirates",
                  "Abu Dhabi", "Saudi Arabia", "Qatar", "Kuwait", "Croatia", "Belgium", "Switzerland", "Austria",
                  "Turkey", "Israel")


def _get(session: requests.Session, url: str, **kw) -> requests.Response:
    resp = session.get(url, headers=HEADERS, timeout=30, **kw)
    resp.raise_for_status()
    return resp


def _text(fragment: str) -> str:
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", fragment))).strip()


def fallback_start(date, location) -> pd.Timestamp:
    loc = str(location or "")
    region = "asia" if any(c in loc for c in ASIA_OCEANIA) else \
        "europe" if any(c in loc for c in EUROPE_MIDEAST) else "americas"
    return pd.Timestamp(date).tz_localize("UTC") + pd.Timedelta(hours=FALLBACK_LOCK_HOUR[region])


def five_rounds(order, title, event, a, b) -> bool:
    """Main events and title fights are scheduled for five rounds."""
    if title or order == 0:
        return True
    # "UFC 330: Smith vs. Jones" names its main event.
    def surname(name) -> str:
        parts = normalize_name(name).split()
        return parts[-1] if parts else ""
    head = str(event).split(":", 1)[-1]
    billed = {surname(x) for x in re.split(r"\s+vs\.?\s+", head)} - {""}
    return len(billed) == 2 and {surname(a), surname(b)} == billed


# ---- UFCStats -------------------------------------------------------------

def parse_upcoming_list(page: str) -> pd.DataFrame:
    """Events on the UFCStats upcoming page: url, name, date, location."""
    rows = []
    for block in re.split(r"<tr[^>]*>", page)[1:]:
        m = re.search(r'href="(https?://(?:www\.)?ufcstats\.com/event-details/[\w-]+)"[^>]*>(.*?)</a>', block, re.S)
        if not m:
            continue
        date = re.search(r'b-statistics__date[^>]*>(.*?)</span>', block, re.S)
        cells = re.findall(r"<td[^>]*>(.*?)</td>", block, re.S)
        rows.append({"url": m.group(1), "event": _text(m.group(2)),
                     "date": pd.to_datetime(_text(date.group(1)), errors="coerce") if date else pd.NaT,
                     "location": _text(cells[-1]) if len(cells) > 1 else None})
    return pd.DataFrame(rows, columns=["url", "event", "date", "location"])


def parse_event_page(page: str) -> tuple[dict, pd.DataFrame]:
    """Event details and bouts (fight id, fighter ids and names, division, belt)."""
    info = {}
    title = re.search(r'b-content__title-highlight[^>]*>(.*?)</span>', page, re.S)
    info["event"] = _text(title.group(1)) if title else None
    for label in ("Date", "Location"):
        m = re.search(label + r":\s*</i>(.*?)</li>", page, re.S)
        info[label.lower()] = _text(m.group(1)) if m else None
    rows = []
    for m in re.finditer(r"<tr([^>]*)>(.*?)</tr>", page, re.S):
        attrs, row = m.group(1), m.group(2)
        fighters = re.findall(r'href="https?://(?:www\.)?ufcstats\.com/fighter-details/([\w-]+)"[^>]*>(.*?)</a>', row, re.S)
        if len(fighters) < 2:
            continue
        link = re.search(r"fight-details/([\w-]+)", attrs)
        fight_id = link.group(1) if link else f"{fighters[0][0]}-{fighters[1][0]}"
        text = _text(row)
        division, gender, _ = parse_weightclass(text)
        rows.append({"bout_id": fight_id, "a_id": fighters[0][0], "fighter_a": _text(fighters[0][1]),
                     "b_id": fighters[1][0], "fighter_b": _text(fighters[1][1]),
                     "division": division, "gender": gender, "title": "belt.png" in row})
    return info, pd.DataFrame(rows)


def ufcstats_cards(now: pd.Timestamp, days: int, session: requests.Session | None = None) -> pd.DataFrame:
    session = session or requests.Session()
    page = _get(session, UFCSTATS_UPCOMING_URL).text
    if "Checking your browser" in page or "requires JavaScript" in page:
        log.warning("UFCStats answered with a browser check instead of the event list")
        return pd.DataFrame()
    listed = parse_upcoming_list(page)
    today = now.tz_convert(DISPLAY_TZ).normalize().tz_localize(None)
    events = listed[(listed["date"] >= today - pd.Timedelta(days=1))
                    & (listed["date"] <= today + pd.Timedelta(days=days))]
    log.info("UFCStats lists %d upcoming events, %d in the next %d days", len(listed), len(events), days)
    frames = []
    for ev in events.itertuples(index=False):
        info, bouts = parse_event_page(_get(session, ev.url).text)
        if bouts.empty:
            log.warning("UFCStats page for %s lists no bouts", ev.event)
            continue
        date = pd.to_datetime(info.get("date"), errors="coerce")
        bouts["event"] = info.get("event") or ev.event
        bouts["date"] = date if not pd.isna(date) else ev.date
        bouts["location"] = info.get("location") or ev.location
        bouts["order"] = range(len(bouts))
        frames.append(bouts)
    if not frames:
        return pd.DataFrame()
    out = pd.concat(frames, ignore_index=True)
    out["bout_key"] = out.pop("bout_id")
    out["source"] = "UFCStats"
    log.info("UFCStats: %d upcoming bouts on %d cards", len(out), out["event"].nunique())
    return out


# ---- ESPN -----------------------------------------------------------------

def _num(x) -> float:
    if isinstance(x, str):
        x = x.strip().lower().replace("+", "")
        if x in ("even", "ev"):
            return 100.0
    try:
        v = float(x)
    except (TypeError, ValueError):
        return np.nan
    return v if np.isfinite(v) and abs(v) >= 100 else np.nan


def _dig(d, *keys):
    for k in keys:
        if isinstance(d, list):
            d = d[k] if isinstance(k, int) and len(d) > k else None
        elif isinstance(d, dict):
            d = d.get(k)
        else:
            return None
    return d


def _side_price(odds: dict, side: str) -> float:
    for path in ((f"{side}AthleteOdds", "moneyLine"), (f"{side}TeamOdds", "moneyLine"),
                 ("moneyline", side, "close", "odds"), ("moneyline", side, "current", "odds"),
                 ("moneyline", side, "open", "odds")):
        v = _num(_dig(odds, *path))
        if not np.isnan(v):
            return v
    return np.nan


def _ids(competitor: dict) -> set:
    return {str(x) for x in (competitor.get("id"), _dig(competitor, "athlete", "id")) if x is not None}


def _orient(odds: dict, people: list[dict], names: tuple[str, str]) -> tuple[float, float]:
    """Moneylines for the two competitors in ``people`` order.

    ESPN keys prices home/away. A side is tied to a fighter by the athlete id
    on the price when there is one, otherwise by the competitor's home/away
    flag, and the favorite named in the odds summary ("Smith -250") must
    agree. Anything ambiguous is dropped rather than risk swapping prices.
    """
    price = {side: _side_price(odds, side) for side in ("home", "away")}
    if any(np.isnan(v) for v in price.values()):
        return np.nan, np.nan
    owner = {}
    for side in ("home", "away"):
        pid = _dig(odds, f"{side}AthleteOdds", "athlete", "id") or _dig(odds, f"{side}AthleteOdds", "id")
        for i, person in enumerate(people):
            if pid is not None and str(pid) in _ids(person):
                owner[side] = i
    if len(set(owner.values())) != 2:
        flags = [person.get("homeAway") for person in people]
        if set(flags) != {"home", "away"}:
            return np.nan, np.nan
        owner = {flag: i for i, flag in enumerate(flags)}
    ab = [np.nan, np.nan]
    for side, i in owner.items():
        ab[i] = price[side]
    a, b = ab
    details = normalize_name(odds.get("details") or "").split()
    if details and a != b:
        fav = 0 if a < b else 1
        named = [bool(normalize_name(n).split()) and normalize_name(n).split()[-1] in details for n in names]
        if named[1 - fav] and not named[fav]:
            log.warning("ESPN odds summary %r disagrees with the prices; dropping them", odds.get("details"))
            return np.nan, np.nan
    return a, b


def _espn_division(kind: str) -> str | None:
    """Division named in ESPN's bout description, if any."""
    if not kind:
        return None
    division, _, _ = parse_weightclass(kind)
    return division if division != "Catch Weight" or "Catch" in kind else None


def parse_espn(payload: dict) -> pd.DataFrame:
    rows = []
    for event in payload.get("events") or []:
        comps = event.get("competitions") or []
        for i, comp in enumerate(comps):
            people = comp.get("competitors") or []
            if len(people) != 2:
                continue
            people = sorted(people, key=lambda c: c.get("order", 0) or 0)
            names = tuple(_dig(c, "athlete", "displayName") or _dig(c, "athlete", "fullName") or "" for c in people)
            if not all(names):
                continue
            odds = _dig(comp, "odds", 0) or {}
            a, b = _orient(odds, people, names) if odds else (np.nan, np.nan)
            provider = _dig(odds, "provider", "name")
            notes = [n.get("headline") for n in comp.get("notes") or [] if isinstance(n, dict)]
            kind = " ".join(str(x) for x in (_dig(comp, "type", "text"), _dig(comp, "type", "abbreviation"),
                                              comp.get("note"), *notes) if x)
            rows.append({
                "espn_id": str(comp.get("id") or f"{event.get('id')}-{i}"),
                "event": event.get("name"),
                "start": pd.to_datetime(comp.get("date") or comp.get("startDate") or event.get("date"),
                                        utc=True, errors="coerce"),
                "fighter_a": names[0], "fighter_b": names[1],
                "odds_a": a, "odds_b": b,
                "odds_source": ("ESPN" + (f" ({provider})" if provider else "")) if not np.isnan(a) else None,
                "a_record": _dig(people[0], "records", 0, "summary"),
                "b_record": _dig(people[1], "records", 0, "summary"),
                "division": _espn_division(kind),
                "title": "title" in kind.lower() or "championship" in kind.lower(),
                "rounds_espn": _dig(comp, "format", "regulation", "periods"),
                "state": _dig(comp, "status", "type", "state"),
                # ESPN lists the card from the first prelim to the main event.
                "espn_order": len(comps) - 1 - i,
            })
    return pd.DataFrame(rows)


def espn_cards(now: pd.Timestamp, days: int, session: requests.Session | None = None) -> pd.DataFrame:
    """ESPN bouts on cards in the next ``days`` days."""
    session = session or requests.Session()
    first = _get(session, ESPN_SCOREBOARD_URL).json()
    dates = set()
    for entry in _dig(first, "leagues", 0, "calendar") or []:
        start = pd.to_datetime(entry.get("startDate") if isinstance(entry, dict) else entry, utc=True, errors="coerce")
        if not pd.isna(start) and now - pd.Timedelta(days=1) <= start <= now + pd.Timedelta(days=days):
            dates.add(start.tz_convert(DISPLAY_TZ).strftime("%Y%m%d"))
    frames = [parse_espn(first)]
    for day in sorted(dates):
        try:
            frames.append(parse_espn(_get(session, ESPN_SCOREBOARD_URL, params={"dates": day}).json()))
        except (requests.RequestException, ValueError) as exc:
            log.warning("ESPN scoreboard for %s failed: %s", day, exc)
    out = pd.concat([f for f in frames if len(f)], ignore_index=True) if any(len(f) for f in frames) else pd.DataFrame()
    if out.empty:
        return out
    out = out.drop_duplicates("espn_id")
    out = out[(out["start"] >= now - pd.Timedelta(hours=12)) & (out["start"] <= now + pd.Timedelta(days=days))]
    log.info("ESPN: %d upcoming bouts, %d with moneylines", len(out), int(out["odds_a"].notna().sum()))
    return out.reset_index(drop=True)


# ---- merging --------------------------------------------------------------

def _flip_odds(row: pd.Series) -> pd.Series:
    row = row.copy()
    row["odds_a"], row["odds_b"] = row["odds_b"], row["odds_a"]
    row["a_record"], row["b_record"] = row["b_record"], row["a_record"]
    return row


def attach_espn(card: pd.DataFrame, espn: pd.DataFrame) -> pd.DataFrame:
    """Add ESPN start times and prices to UFCStats bouts, matching names within each date."""
    card = card.copy()
    for col in ("start", "odds_a", "odds_b", "odds_source", "a_record", "b_record"):
        if col not in card:
            card[col] = np.nan if col in ("odds_a", "odds_b") else None
    if espn.empty or card.empty:
        return card
    espn = espn.assign(day=espn["start"].dt.tz_convert(DISPLAY_TZ).dt.tz_localize(None).dt.normalize())
    matched = 0
    for idx, bout in card.iterrows():
        near = espn[(espn["day"] - pd.Timestamp(bout["date"])).abs() <= pd.Timedelta(days=1)]
        if near.empty:
            continue
        names = pd.concat([near["fighter_a"], near["fighter_b"]])
        names.index = [f"{i}:a" for i in near.index] + [f"{i}:b" for i in near.index]
        hit_a, hit_b = match_name(bout["fighter_a"], names), match_name(bout["fighter_b"], names)
        if not hit_a or not hit_b or hit_a.split(":")[0] != hit_b.split(":")[0] or hit_a == hit_b:
            continue
        row = near.loc[int(hit_a.split(":")[0])]
        if hit_a.endswith(":b"):
            row = _flip_odds(row)
        for col in ("start", "odds_a", "odds_b", "odds_source", "a_record", "b_record"):
            card.at[idx, col] = row[col]
        matched += 1
    log.info("Matched %d of %d bouts to ESPN", matched, len(card))
    return card


def resolve_card_ids(card: pd.DataFrame, known: pd.Series) -> pd.DataFrame:
    """Use history ids for card fighters: ``known`` maps id -> name for fighters with UFC bouts.

    A UFCStats id from the card is kept when the history has it; otherwise the
    name is matched (the history keys a few fighters by name), and a fighter
    with no match is a UFC debutant under the card's id.
    """
    card = card.copy()
    for side in ("a", "b"):
        ids = []
        for fid, name in zip(card.get(f"{side}_id", pd.Series([None] * len(card))), card[f"fighter_{side}"]):
            if isinstance(fid, str) and fid in known.index:
                ids.append(fid)
                continue
            hit = match_name(name, known)
            ids.append(hit if hit is not None else (fid if isinstance(fid, str) else
                                                    "x-" + normalize_name(name).replace(" ", "-")))
        card[f"{side}_id"] = ids
    new = sorted({n for s in "ab" for n, i in zip(card[f"fighter_{s}"], card[f"{s}_id"]) if i not in known.index})
    log.info("Matched %d of %d card fighters to UFC history; no UFC bouts yet: %s",
             2 * len(card) - len(new), 2 * len(card), ", ".join(new) or "none")
    return card


def settle_division(division, last_a, last_b) -> str:
    """The bout's division, using the fighters' last UFC divisions where the source is vague.

    ESPN sometimes names a women's bout by the bare weight ("Flyweight"), so a
    bout between fighters last seen in a women's division is a women's bout.
    """
    known = [d for d in (last_a, last_b) if isinstance(d, str) and d]
    if not isinstance(division, str) or not division:
        return known[0] if known else "Catch Weight"
    if any(d.startswith("Women's") for d in known) and not division.startswith("Women's"):
        women = "Women's " + division
        return women if women in DIVISIONS else next(d for d in known if d.startswith("Women's"))
    return division


def load_manual(today: pd.Timestamp) -> pd.DataFrame:
    if not MANUAL_PATH.exists():
        return pd.DataFrame()
    m = pd.read_csv(MANUAL_PATH, comment="#")
    if m.empty:
        return m
    m["date"] = pd.to_datetime(m["date"])
    m = m[m["date"] >= today - pd.Timedelta(days=1)].copy()
    for col, default in (("division", "Catch Weight"), ("title", False), ("rounds", np.nan), ("odds_a", np.nan),
                         ("odds_b", np.nan), ("location", None), ("event", "Manual card"), ("start", pd.NaT)):
        if col not in m:
            m[col] = default
    m["gender"] = np.where(m["division"].astype(str).str.startswith("Women"), "F", "M")
    m["title"] = m["title"].fillna(False).astype(bool)
    m["order"] = m.groupby("event").cumcount()
    m["odds_source"] = np.where(m["odds_a"].notna(), "manual", None)
    m["source"] = "manual"
    return m


def fetch_card(now: pd.Timestamp, days: int, known: pd.Series, last_division: dict,
               use_ufcstats: bool = True, use_espn: bool = True) -> pd.DataFrame:
    """Every bout on cards in the next ``days`` days, with ids, rounds, start time and prices."""
    session = requests.Session()
    card = pd.DataFrame()
    if use_ufcstats:
        try:
            card = ufcstats_cards(now, days, session)
        except (requests.RequestException, ValueError, KeyError, AttributeError) as exc:
            log.warning("UFCStats upcoming cards failed: %s", exc)
    espn = pd.DataFrame()
    if use_espn:
        try:
            espn = espn_cards(now, days, session)
        except (requests.RequestException, ValueError, KeyError, TypeError, AttributeError) as exc:
            log.warning("ESPN scoreboard failed: %s", exc)
    if card.empty and not espn.empty:
        card = espn.rename(columns={"espn_id": "bout_key", "espn_order": "order"}).copy()
        card["bout_key"] = "espn-" + card["bout_key"]
        card["date"] = card["start"].dt.tz_convert(DISPLAY_TZ).dt.tz_localize(None).dt.normalize()
        card["location"] = None
        card["source"] = "ESPN"
        card["gender"] = None
    elif not card.empty:
        card = attach_espn(card, espn)
    manual = load_manual(now.tz_convert(DISPLAY_TZ).normalize().tz_localize(None))
    if not manual.empty:
        keys = {pair_key(a, b) for a, b in zip(manual["fighter_a"], manual["fighter_b"])}
        if not card.empty:
            card = card[[pair_key(a, b) not in keys for a, b in zip(card["fighter_a"], card["fighter_b"])]]
        manual["bout_key"] = "manual-" + manual["date"].dt.strftime("%Y%m%d") + "-" + \
            [pair_key(a, b).replace(" ", "-").replace("|", "-vs-") for a, b in zip(manual["fighter_a"], manual["fighter_b"])]
        card = pd.concat([card, manual], ignore_index=True) if len(card) else manual
    if card.empty:
        return pd.DataFrame(columns=CARD_COLUMNS)
    card = resolve_card_ids(card.reset_index(drop=True), known)
    card["division"] = [settle_division(d, last_division.get(a), last_division.get(b))
                        for d, a, b in zip(card["division"], card["a_id"], card["b_id"])]
    card["gender"] = np.where(card["division"].astype(str).str.startswith("Women"), "F", "M")
    card["title"] = card["title"].fillna(False).astype(bool)
    for col in ("rounds_espn", "rounds", "start", "location"):
        if col not in card:
            card[col] = np.nan
    five = [five_rounds(o, t, e, a, b) for o, t, e, a, b in
            zip(card["order"], card["title"], card["event"], card["fighter_a"], card["fighter_b"])]
    card["rounds"] = card["rounds"].fillna(pd.to_numeric(card["rounds_espn"], errors="coerce"))
    card["rounds"] = card["rounds"].fillna(pd.Series(np.where(five, 5, 3), index=card.index)).astype(int)
    card["start"] = pd.to_datetime(card["start"], utc=True, errors="coerce")
    fallback = pd.Series([fallback_start(d, loc) for d, loc in zip(card["date"], card["location"])], index=card.index)
    card["start"] = card["start"].fillna(fallback)
    card["date"] = pd.to_datetime(card["date"]).dt.normalize()
    for col in CARD_COLUMNS:
        if col not in card:
            card[col] = None
    return card[CARD_COLUMNS].sort_values(["date", "event", "order"], ignore_index=True)
