"""Command-line entry point: ``python -m ufcpredictor <command>``."""

from __future__ import annotations

import argparse
import logging

import pandas as pd

from .config import OUTPUT_DIR, Hyperparams


def _history(max_age_hours: float, refresh: bool = True):
    from .data import load_data, refresh_data
    from .features import FeatureBuilder
    from .odds import market_odds

    hp = Hyperparams.load()
    if refresh:
        refresh_data(max_age_hours)
    bouts, stats, fighters = load_data()
    odds = market_odds(bouts, max_age_hours=max(max_age_hours, 24.0))
    fb = FeatureBuilder(bouts, stats, fighters, hp)
    return hp, bouts, odds, fb


def cmd_update(args) -> None:
    from .pipeline import README_PATH, run_update

    new = run_update(days=args.days, max_age_hours=args.max_age_hours,
                     use_ufcstats=not args.no_ufcstats, use_espn=not args.no_espn)
    print(f"Predicted {len(new)} upcoming bouts. See {README_PATH}")


def cmd_backtest(args) -> None:
    from . import backtest, report

    hp, bouts, odds, fb = _history(args.max_age_hours)
    feats = fb.build().join(odds.reset_index(drop=True))
    years = (args.start, args.end)
    bt = backtest.predict_years(feats, range(args.start, args.end + 1), hp.fit_window_years, hp.ridge)
    win, method, rounds = backtest.win_scores(bt), backtest.method_scores(bt), backtest.round_scores(bt)
    calib, boot, bets = backtest.calibration(bt), backtest.bootstraps(bt), backtest.edge_summary(bt)
    path = OUTPUT_DIR / "backtest.md"
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    path.write_text(report.render_backtest(win, method, rounds, calib, boot, bets, years))
    with pd.option_context("display.width", 160):
        for df in (win, method, rounds):
            print(df.round(4).to_string(index=False))
        print(bets.round(3).to_string(index=False))
    print(f"Wrote {path}")


def cmd_tune(args) -> None:
    from . import backtest

    hp, bouts, odds, fb = _history(args.max_age_hours)
    grid = {
        "glicko_debut_rd": [320.0, 400.0, 500.0],
        "glicko_period_days": [30.0, 60.0],
        "score_decision": [0.7, 0.8],
        "score_split": [0.5, 0.6],
    }
    results = backtest.tune(fb, odds, range(args.start, args.end + 1), grid, hp)
    print(results.round(4).to_string(index=False))
    if args.save:
        best = results.iloc[0]
        for key in grid:
            setattr(hp, key, float(best[key]))
        hp.save()
        print("Saved best settings to params.json")


def cmd_ratings(args) -> None:
    from .pipeline import ratings_table

    _, bouts, _, fb = _history(args.max_age_hours, refresh=False)
    fb.build()
    table = ratings_table(fb, bouts, pd.Timestamp.now(tz="UTC"))
    if args.division:
        table = table[table["division"].str.lower() == args.division.lower()]
    with pd.option_context("display.float_format", "{:.0f}".format, "display.max_rows", 500):
        print(table.drop(columns="rank_score").head(args.top).to_string(index=False))


def _raw_sources() -> None:
    """Print what the card sources return, for checking the parsers against the live pages."""
    import json
    import re

    import requests

    from .cards import HEADERS, _dig, parse_event_page, parse_upcoming_list, round_total
    from .config import ESPN_ODDS_URL, ESPN_SCOREBOARD_URL, UFCSTATS_UPCOMING_URL

    try:
        page = requests.get(UFCSTATS_UPCOMING_URL, headers=HEADERS, timeout=30)
        print(f"UFCStats upcoming: HTTP {page.status_code}, {len(page.text)} bytes")
        events = parse_upcoming_list(page.text)
        print(events.to_string(index=False) if len(events) else "  no events parsed")
        m = re.search(r".{0,300}event-details.{0,500}", page.text, re.S)
        print("  sample:", repr(m.group(0)) if m else repr(page.text[:800]))
        if len(events):
            ev = requests.get(events["url"].iloc[0], headers=HEADERS, timeout=30)
            info, bouts = parse_event_page(ev.text)
            print(f"  first event page: HTTP {ev.status_code}, {info}, {len(bouts)} bouts")
            m = re.search(r"<tr[^>]*>(?:(?!</tr>).)*fighter-details(?:(?!</tr>).)*</tr>", ev.text, re.S)
            print("  first bout row:", repr(m.group(0)[:1500]) if m else repr(ev.text[:1500]))
    except requests.RequestException as exc:
        print("UFCStats failed:", exc)
    try:
        board = requests.get(ESPN_SCOREBOARD_URL, timeout=30).json()
        cal = (board.get("leagues") or [{}])[0].get("calendar") or []
        print(f"ESPN: {len(board.get('events') or [])} events, calendar entries {len(cal)}:",
              json.dumps(cal[:3])[:600])
        for event in (board.get("events") or [])[:1]:
            comps = event.get("competitions") or []
            print(f"  {event.get('name')}: {len(comps)} competitions")
            for comp in comps[-1:]:
                slim = {k: v for k, v in comp.items() if k not in ("competitors", "odds")}
                print("  competition:", json.dumps(slim)[:1500])
                for c in comp.get("competitors") or []:
                    print("  competitor:", json.dumps({k: v for k, v in c.items() if k != "statistics"})[:800])
                print("  odds:", json.dumps(comp.get("odds"))[:2500])
                print("  scoreboard round total (line, over, under):", round_total(_dig(comp, "odds", 0) or {}))
                url = ESPN_ODDS_URL.format(event=event.get("id"), competition=comp.get("id"))
                try:
                    resp = requests.get(url, timeout=30)
                    payload = resp.json()
                    print(f"  odds API: HTTP {resp.status_code}", json.dumps(payload.get("items"))[:3000])
                    _raw_props(payload, comp)
                except (requests.RequestException, ValueError) as exc:
                    print(f"  odds API failed: {exc}")
    except (requests.RequestException, ValueError) as exc:
        print("ESPN failed:", exc)


def _raw_props(payload: dict, comp: dict) -> None:
    """Print each odds item's fields and links, then one ``propBets`` page, for checking the prop parsers."""
    import json

    import requests

    from .cards import _dig, parse_core_props, parse_props

    people = sorted(comp.get("competitors") or [], key=lambda c: c.get("order", 0) or 0)
    ids = tuple(str(c.get("id") or _dig(c, "athlete", "id") or "") for c in people[:2])
    names = tuple(_dig(c, "athlete", "displayName") or "" for c in people[:2])
    for item in (payload.get("items") or [])[:4]:
        if not isinstance(item, dict):
            continue
        links = {k: v["$ref"] for k, v in item.items() if isinstance(v, dict) and "$ref" in v}
        print(f"  odds item {_dig(item, 'provider', 'name')}: keys {sorted(item)}")
        print("    links:", json.dumps(links)[:1500])
        for key in ("overUnder", "overOdds", "underOdds", "total", "current", "propBets", "props"):
            if key in item:
                print(f"    {key}:", json.dumps(item[key])[:800])
    if len(ids) < 2:
        return
    props, link = parse_core_props(payload, ids)
    print(f"  parsed from odds items for {names}:", {k: v for k, v in props.items() if v == v}, "propBets link:", link)
    if not link:
        return
    try:
        resp = requests.get(link, params={"limit": 500}, timeout=30)
        listed = resp.json()
        items = listed.get("items") or []
        print(f"  propBets: HTTP {resp.status_code}, count {listed.get('count')}, pages {listed.get('pageCount')}")
        print("  propBets items:", json.dumps(items[:12])[:5000])
        kinds = sorted({json.dumps(i.get("type"))[:120] for i in items if isinstance(i, dict)})
        print("  propBets types:", kinds[:40])
        print("  parsed from propBets:", {k: v for k, v in parse_props(items, ids, names).items() if v == v})
    except (requests.RequestException, ValueError, AttributeError) as exc:
        print(f"  propBets failed: {exc}")


def cmd_card(args) -> None:
    from .cards import fetch_card

    if args.raw:
        _raw_sources()

    _, _, _, fb = _history(args.max_age_hours, refresh=False)
    fb.build()
    card = fetch_card(pd.Timestamp.now(tz="UTC"), args.days, pd.Series(fb.names), fb.last_div,
                      use_ufcstats=not args.no_ufcstats, use_espn=not args.no_espn)
    cols = ["date", "start", "event", "fighter_a", "fighter_b", "division", "rounds", "title", "odds_a",
            "odds_b", "source"]
    if args.raw:
        cols += ["odds_a_ko", "odds_a_sub", "odds_a_dec", "odds_b_ko", "odds_b_sub", "odds_b_dec", "rounds_line",
                 "over_price", "under_price"]
    with pd.option_context("display.width", 200, "display.max_rows", 200):
        print(card[cols].to_string(index=False) if len(card) else "No upcoming bouts found.")


def main(argv=None) -> None:
    parser = argparse.ArgumentParser(prog="ufcpredictor", description=__doc__)
    parser.add_argument("-v", "--verbose", action="store_true")
    parser.add_argument("--max-age-hours", type=float, default=1.0,
                        help="reuse downloaded data younger than this (default 1)")
    sub = parser.add_subparsers(dest="command", required=True)

    def sources(p):
        p.add_argument("--days", type=int, default=15, help="look this many days ahead for cards (default 15)")
        p.add_argument("--no-ufcstats", action="store_true", help="skip UFCStats upcoming cards")
        p.add_argument("--no-espn", action="store_true", help="skip ESPN start times and odds")

    p = sub.add_parser("update", help="refresh data, predict upcoming bouts, grade results")
    sources(p)
    p.set_defaults(func=cmd_update)

    p = sub.add_parser("backtest", help="walk-forward backtest against the betting market")
    p.add_argument("--start", type=int, default=2015)
    p.add_argument("--end", type=int, default=2026)
    p.set_defaults(func=cmd_backtest)

    p = sub.add_parser("tune", help="grid-search rating and profile settings")
    p.add_argument("--start", type=int, default=2010)
    p.add_argument("--end", type=int, default=2014)
    p.add_argument("--save", action="store_true", help="write the best settings to params.json")
    p.set_defaults(func=cmd_tune)

    p = sub.add_parser("ratings", help="print current Glicko-2 ratings of active fighters")
    p.add_argument("--division", help="one division, e.g. Lightweight or \"Women's Flyweight\"")
    p.add_argument("--top", type=int, default=200)
    p.set_defaults(func=cmd_ratings)

    p = sub.add_parser("card", help="print the upcoming cards as read from the sources")
    sources(p)
    p.add_argument("--raw", action="store_true",
                   help="also print what each source returned, including ESPN's odds items and prop bets")
    p.set_defaults(func=cmd_card)

    args = parser.parse_args(argv)
    logging.basicConfig(level=logging.INFO if args.verbose else logging.WARNING,
                        format="%(levelname)s %(name)s: %(message)s")
    args.func(args)
