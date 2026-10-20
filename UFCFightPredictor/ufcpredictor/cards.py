"""Upcoming fight cards: who fights whom, when, and at what price.

Three sources, merged:

1. **UFCStats** lists every announced bout with the same fighter ids as the
   history, so matching is exact. Its pages give the division and title belt
   but not start times or rounds; the main event and title fights are five
   rounds, everything else three.
2. **ESPN's** public scoreboard (no key needed) adds each card segment's start
   time, and its odds API each bout's moneylines from its sportsbook partner,
   plus the round total and method-of-victory props when it posts them (read
   from the odds items and the ``propBets`` link on them, one extra request a
   bout at most).
   It stands in for UFCStats when that site is down or, as it does for
   GitHub's runners, answers with a browser check. ESPN names are matched to
   UFCStats names.
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

from .config import (DATA_DIR, DISPLAY_TZ, DIVISIONS, ESPN_ODDS_URL, ESPN_SCOREBOARD_URL,
                     UFCSTATS_UPCOMING_URL)
from .data import parse_weightclass
from .edges import implied_prob
from .names import match_name, normalize_name, pair_key
from .odds import METHOD_ODDS, ROUND_ODDS

log = logging.getLogger(__name__)

MANUAL_PATH = DATA_DIR / "manual_card.csv"
CARD_COLUMNS = [
    "bout_key", "event", "date", "start", "location", "order", "fighter_a", "fighter_b", "a_id", "b_id",
    "division", "gender", "title", "rounds", "odds_a", "odds_b", *METHOD_ODDS, *ROUND_ODDS, "odds_source",
    "a_record", "b_record", "source",
]
PROP_COLUMNS = METHOD_ODDS + ROUND_ODDS
# Most prop requests (``propBets`` links) one card read may make.
MAX_PROP_REQUESTS = 40
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


def _line(x) -> float:
    """A round-total line such as 1.5, "o2.5" or "Over 1.5"; NaN unless it is x.5 between 0.5 and 4.5."""
    if isinstance(x, str):
        m = re.search(r"(\d+(?:\.\d+)?)", x)
        x = m.group(1) if m else None
    try:
        v = float(x)
    except (TypeError, ValueError):
        return np.nan
    return v if 0.5 <= v <= 4.5 and abs(v - np.floor(v) - 0.5) < 1e-9 else np.nan


def round_total(odds: dict) -> tuple[float, float, float]:
    """Round-total line and over and under prices from an ESPN odds object (scoreboard or core API).

    Tries the nested ``total.{over,under}.{close,current,open}`` format first,
    then the older ``overUnder`` with ``overOdds``/``underOdds`` and the
    ``current.{over,under}`` blocks. Missing pieces are NaN.
    """
    for when in ("close", "current", "open"):
        line = _line(_dig(odds, "total", "over", when, "line"))
        if np.isnan(line):
            line = _line(_dig(odds, "total", "under", when, "line"))
        over, under = _num(_dig(odds, "total", "over", when, "odds")), _num(_dig(odds, "total", "under", when, "odds"))
        if not np.isnan(line) and not (np.isnan(over) and np.isnan(under)):
            return line, over, under
    line = _line(odds.get("overUnder"))
    if np.isnan(line):
        line = _line(_dig(odds, "current", "total", "alternateDisplayValue"))
    def price(side: str) -> float:
        for path in ((f"{side}Odds",), ("current", side, "american"), ("current", side, "alternateDisplayValue")):
            v = _num(_dig(odds, *path))
            if not np.isnan(v):
                return v
        return np.nan
    return line, price("over"), price("under")


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


def _title_fight(people: list[dict], kind: str, rounds) -> bool:
    """Named a title fight, or five rounds with a fighter holding that weight's belt."""
    if "title" in kind.lower() or "championship" in kind.lower():
        return True
    if rounds != 5 or not kind:
        return False
    division = parse_weightclass(kind)[0].replace("Women's ", "")
    belts = [a.get("name") or "" for c in people for a in _dig(c, "athlete", "accolades") or []
             if isinstance(a, dict) and ("Title" in (a.get("name") or "") or a.get("type") == "Belt")]
    return any(division in b for b in belts)


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
            line, over, under = round_total(odds) if odds else (np.nan, np.nan, np.nan)
            provider = _dig(odds, "provider", "name")
            notes = [n.get("headline") for n in comp.get("notes") or [] if isinstance(n, dict)]
            kind = " ".join(str(x) for x in (_dig(comp, "type", "text"), _dig(comp, "type", "abbreviation"),
                                              comp.get("note"), *notes) if x)
            rows.append({
                "espn_id": str(comp.get("id") or f"{event.get('id')}-{i}"),
                "espn_event": str(event.get("id") or ""),
                "espn_a": str(people[0].get("id") or _dig(people[0], "athlete", "id") or ""),
                "espn_b": str(people[1].get("id") or _dig(people[1], "athlete", "id") or ""),
                "event": event.get("name"),
                "start": pd.to_datetime(comp.get("date") or comp.get("startDate") or event.get("date"),
                                        utc=True, errors="coerce"),
                "fighter_a": names[0], "fighter_b": names[1],
                "odds_a": a, "odds_b": b,
                **{c: np.nan for c in METHOD_ODDS},
                "rounds_line": line, "over_price": over, "under_price": under,
                "odds_source": ("ESPN" + (f" ({provider})" if provider else "")) if not np.isnan(a) else None,
                "a_record": _dig(people[0], "records", 0, "summary"),
                "b_record": _dig(people[1], "records", 0, "summary"),
                "division": _espn_division(kind),
                "title": _title_fight(people, kind, _dig(comp, "format", "regulation", "periods")),
                "rounds_espn": _dig(comp, "format", "regulation", "periods"),
                "state": _dig(comp, "status", "type", "state"),
                # ESPN lists the card from the first prelim to the main event.
                "espn_order": len(comps) - 1 - i,
            })
    return pd.DataFrame(rows)


def parse_core_odds(payload: dict, ids: tuple[str, str]) -> tuple[float, float, str | None]:
    """Moneylines for the two ESPN athlete ``ids`` from ESPN's odds API.

    Each provider's entry names the athlete behind each price, so prices are
    tied to fighters by id; entries that do not name both fighters are skipped.
    The highest-priority provider with both prices wins.
    """
    items = sorted((i for i in payload.get("items") or [] if isinstance(i, dict)),
                   key=lambda i: _dig(i, "provider", "priority") or 99)
    for item in items:
        prices = {}
        for side in ("home", "away"):
            side_odds = item.get(f"{side}AthleteOdds") or {}
            ref = str(_dig(side_odds, "athlete", "$ref") or _dig(side_odds, "athlete", "id") or "")
            m = re.search(r"athletes/(\d+)", ref) or re.fullmatch(r"(\d+)", ref)
            price = _num(side_odds.get("moneyLine"))
            if np.isnan(price):
                price = _num(_dig(side_odds, "current", "moneyLine", "american"))
            if m and not np.isnan(price):
                prices[m.group(1)] = price
        if all(i in prices for i in ids) and ids[0] != ids[1]:
            return prices[ids[0]], prices[ids[1]], _dig(item, "provider", "name")
    return np.nan, np.nan, None


def _athlete(item: dict) -> str | None:
    for path in (("athlete", "$ref"), ("athlete", "id"), ("athleteId",), ("competitor", "$ref"), ("competitor", "id")):
        ref = str(_dig(item, *path) or "")
        m = re.search(r"athletes/(\d+)", ref) or re.search(r"competitors/(\d+)", ref) or re.fullmatch(r"(\d+)", ref)
        if m:
            return m.group(1)
    return None


def _prop_text(item: dict) -> str:
    parts = [_dig(item, "type", "name"), _dig(item, "type", "displayName"), _dig(item, "type", "description"),
             item.get("name"), item.get("displayName"), item.get("shortName"), item.get("description"),
             item.get("details"), _dig(item, "propBet", "name")]
    return " ".join(str(x) for x in parts if isinstance(x, (str, int, float)) and x != "").lower()


def _prop_price(item) -> float:
    if not isinstance(item, dict):
        return _num(item)
    for path in (("odds", "american", "value"), ("odds", "american"), ("current", "american"),
                 ("current", "odds", "american"), ("american", "value"), ("american",), ("price", "american"),
                 ("moneyLine",), ("odds", "value"), ("odds",), ("value",)):
        v = _dig(item, *path)
        if isinstance(v, dict):
            v = v.get("value") or v.get("displayValue")
        v = _num(v)
        if not np.isnan(v):
            return v
    return np.nan


def _prop_line(item: dict, text: str) -> float:
    for path in (("odds", "total", "value"), ("current", "target", "value"), ("target", "value"), ("target",),
                 ("line",), ("total",), ("current", "line")):
        v = _line(_dig(item, *path))
        if not np.isnan(v):
            return v
    m = re.search(r"(\d\.5)", text)
    return _line(m.group(1)) if m else np.nan


METHOD_PATTERNS = {"ko": r"\b(?:t?ko|ko/tko|tko/ko|knockout|ko-tko)\b", "sub": r"\bsubmission\b",
                   "dec": r"\b(?:decision|points)\b"}
# Props that mention a method but are not a plain "fighter wins by method" market.
NOT_METHOD = r"\b(?:round \d|in round|not|draw|split|unanimous|majority|distance|goes|inside|finish)\b"


def parse_props(items: list, ids: tuple[str, str], names: tuple[str, str] = ("", "")) -> dict:
    """Method-of-victory and round-total prices from ESPN prop entries, in ``ids`` order.

    Written against the shapes ESPN uses for other sports' ``propBets`` (a
    market name under ``type`` or ``name``, the athlete as a ``$ref``, the
    American price under ``odds`` or ``current``, the line under ``target`` or
    ``total``), since the UFC payload could not be inspected: anything that
    does not clearly match is ignored. A method price must name its fighter by
    athlete id (or surname); a round total must give a x.5 line and say over
    or under. The first price seen for each outcome wins. Of several round
    lines, the one with both prices closest to even is the main line.
    """
    out = {c: np.nan for c in PROP_COLUMNS}
    surnames = [normalize_name(n).split()[-1] if normalize_name(n).split() else "" for n in names]
    lines: dict[float, dict] = {}
    for item in items or []:
        if not isinstance(item, dict):
            continue
        text = _prop_text(item)
        if not text:
            continue
        who = _athlete(item)
        side = None
        if who is not None and who in ids and ids[0] != ids[1]:
            side = "ab"[ids.index(who)]
        else:
            hits = [i for i, n in enumerate(surnames) if n and re.search(rf"\b{re.escape(n)}\b", normalize_name(text))]
            side = "ab"[hits[0]] if len(hits) == 1 else None
        if "round" in text and side is None and re.search(r"\b(?:total|over|under)\b", text):
            line = _prop_line(item, text)
            if np.isnan(line):
                continue
            got = lines.setdefault(line, {})
            for ou in ("over", "under"):
                block = item.get(ou) if isinstance(item.get(ou), dict) else None
                price = _prop_price(block) if block else _num(item.get(f"{ou}Odds"))
                if np.isnan(price) and re.search(rf"\b{ou}\b", text) and not re.search(
                        r"\bover\b.*\bunder\b|\bunder\b.*\bover\b", text):
                    price = _prop_price(item)
                if not np.isnan(price):
                    got.setdefault(ou, price)
            continue
        if side is None or re.search(NOT_METHOD, text):
            continue
        kinds = [m for m, pat in METHOD_PATTERNS.items() if re.search(pat, text)]
        if len(kinds) != 1:
            continue
        col = f"odds_{side}_{kinds[0]}"
        price = _prop_price(item)
        if np.isnan(out[col]) and not np.isnan(price):
            out[col] = price
    both = [(abs(implied_prob(p["over"]) - implied_prob(p["under"])), line, p)
            for line, p in lines.items() if "over" in p and "under" in p]
    if both:
        _, line, p = min(both)
        out.update(rounds_line=line, over_price=p["over"], under_price=p["under"])
    return out


def parse_core_props(payload: dict, ids: tuple[str, str]) -> tuple[dict, str | None]:
    """Props carried on ESPN's odds API items, and the first ``propBets`` link to follow.

    Takes the round total from the highest-priority provider that has one,
    and any method prices listed inline (``propBets`` given as a list).
    """
    out = {c: np.nan for c in PROP_COLUMNS}
    link = None
    items = sorted((i for i in payload.get("items") or [] if isinstance(i, dict)),
                   key=lambda i: _dig(i, "provider", "priority") or 99)
    for item in items:
        line, over, under = round_total(item)
        if np.isnan(out["rounds_line"]) and not np.isnan(line) and not (np.isnan(over) and np.isnan(under)):
            out.update(rounds_line=line, over_price=over, under_price=under)
        props = item.get("propBets") or item.get("props")
        if isinstance(props, list):
            inline = parse_props(props, ids)
            for c in METHOD_ODDS:
                if np.isnan(out[c]):
                    out[c] = inline[c]
        elif isinstance(props, dict) and props.get("$ref") and link is None:
            link = props["$ref"]
    return out, link


def attach_core_odds(espn: pd.DataFrame, session: requests.Session) -> pd.DataFrame:
    """Fill in prices from ESPN's odds API: moneylines the scoreboard left out, and the props.

    One odds request per bout that has not started, plus at most one
    ``propBets`` request per bout (``MAX_PROP_REQUESTS`` per card read).
    """
    espn = espn.copy()
    for col in PROP_COLUMNS:
        if col not in espn:
            espn[col] = np.nan
    errors = []
    prop_requests = 0
    for idx, r in espn.iterrows():
        if r.get("state") not in (None, "pre") or not r["espn_event"]:
            continue
        url = ESPN_ODDS_URL.format(event=r["espn_event"], competition=r["espn_id"])
        ids = (r["espn_a"], r["espn_b"])
        try:
            payload = _get(session, url).json()
            a, b, provider = parse_core_odds(payload, ids)
            props, link = parse_core_props(payload, ids)
            if link and prop_requests < MAX_PROP_REQUESTS:
                prop_requests += 1
                listed = _get(session, link, params={"limit": 500}).json()
                more = parse_props(listed.get("items") or [], ids, (r["fighter_a"], r["fighter_b"]))
                props = {c: props[c] if not np.isnan(props[c]) else more[c] for c in PROP_COLUMNS}
        except (requests.RequestException, ValueError, AttributeError) as exc:
            errors.append(str(exc))
            continue
        if np.isnan(r["odds_a"]) and not np.isnan(a):
            espn.at[idx, "odds_a"], espn.at[idx, "odds_b"] = a, b
            espn.at[idx, "odds_source"] = "ESPN" + (f" ({provider})" if provider else "")
        for col in METHOD_ODDS:
            if pd.isna(espn.at[idx, col]) and not np.isnan(props[col]):
                espn.at[idx, col] = props[col]
        # The round line and its prices travel together.
        if pd.isna(espn.at[idx, "over_price"]) and pd.isna(espn.at[idx, "under_price"]) \
                and not (np.isnan(props["over_price"]) and np.isnan(props["under_price"])):
            for col in ROUND_ODDS:
                espn.at[idx, col] = props[col]
    if errors:
        log.warning("ESPN odds failed for %d bouts: %s", len(errors), "; ".join(errors[:2]))
    return espn


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
    out = attach_core_odds(out.reset_index(drop=True), session)
    log.info("ESPN: %d upcoming bouts, %d with moneylines, %d with method props, %d with round totals", len(out),
             int(out["odds_a"].notna().sum()), int(out[METHOD_ODDS].notna().any(axis=1).sum()),
             int(out["rounds_line"].notna().sum()))
    return out


# ---- merging --------------------------------------------------------------

def _flip_odds(row: pd.Series) -> pd.Series:
    row = row.copy()
    for a, b in [("odds_a", "odds_b"), ("a_record", "b_record")] + [(f"odds_a_{m}", f"odds_b_{m}")
                                                                   for m in ("ko", "sub", "dec")]:
        if a in row:
            row[a], row[b] = row[b], row[a]
    return row


def attach_espn(card: pd.DataFrame, espn: pd.DataFrame) -> pd.DataFrame:
    """Add ESPN start times and prices to UFCStats bouts, matching names within each date."""
    card = card.copy()
    taken = ["start", "odds_a", "odds_b", *PROP_COLUMNS, "odds_source", "a_record", "b_record"]
    for col in taken:
        if col not in card:
            card[col] = None if col in ("start", "odds_source", "a_record", "b_record") else np.nan
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
        for col in taken:
            if col in row:
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
    for col in PROP_COLUMNS:
        if col not in m:
            m[col] = np.nan
    m["odds_source"] = np.where(m[["odds_a", *METHOD_ODDS, "over_price"]].notna().any(axis=1), "manual", None)
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
    for col in ("odds_a", "odds_b", *PROP_COLUMNS):
        card[col] = pd.to_numeric(card[col], errors="coerce")
    return card[CARD_COLUMNS].sort_values(["date", "event", "order"], ignore_index=True)
