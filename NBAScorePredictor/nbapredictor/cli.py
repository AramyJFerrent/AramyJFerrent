"""Command-line entry point: ``python -m nbapredictor <command>``."""

from __future__ import annotations

import argparse
import json
import logging

import pandas as pd

from .config import DISPLAY_TZ, ESPN_TEAM_IDS, FIRST_SEASON, OUTPUT_DIR, Hyperparams, season_label


def cmd_update(args) -> None:
    from .pipeline import README_PATH, run_update

    new = run_update(days=args.days, n_sims=args.sims, use_espn=not args.no_espn, max_age_hours=args.max_age_hours)
    print(f"Predicted {len(new)} upcoming games. See {README_PATH}")


def cmd_backtest(args) -> None:
    from . import backtest, report
    from .data import load_summaries
    from .features import FeatureBuilder
    from .lines import load_lines

    hp = Hyperparams.load()
    summaries = load_summaries(FIRST_SEASON, args.end)
    fb = FeatureBuilder(summaries, hp, load_lines())
    first = max(args.start - hp.fit_window_seasons, FIRST_SEASON + 1)
    seasons = range(args.start, args.end + 1)
    feats = fb.walk_forward(range(first, args.end + 1))
    bt = backtest.predict_seasons(feats, seasons, hp.fit_window_seasons, n_sims=args.sims)
    label = f"{season_label(args.start)} to {season_label(args.end)}"
    scores = {label: backtest.score(bt)}
    for start, note in ((args.holdout, "seasons not used for tuning"), (2021, "the report's test seasons")):
        if start and args.start < start <= args.end:
            scores[f"{season_label(start)} on ({note})"] = backtest.score(bt[bt["season"] >= start])
    err = backtest.errors(bt)
    boot = {
        "Model only vs closing line": backtest.paired_bootstrap(err["model"], err["line"]),
        "Model only vs team ratings only": backtest.paired_bootstrap(err["model"], err["team"]),
        "Final vs closing line": backtest.paired_bootstrap(err["final"], err["line"]),
    }
    checks = backtest.distribution_checks(bt)
    picks = {"Closing line": backtest.pick_record(bt, "spread")}
    has_open = bt["open_spread"].notna()
    open_seasons = sorted(bt.loc[has_open, "season"].unique())
    open_label = f"{season_label(open_seasons[0])} to {season_label(open_seasons[-1])}" if open_seasons else ""
    if has_open.any():
        picks[f"Opening line, {open_label}, knowing who played"] = backtest.pick_record(bt[has_open], "open_spread",
                                                                                      "spread")
        picks["Closing line, same games"] = backtest.pick_record(bt[has_open], "spread")
    extra = {}
    if not args.skip_blind:
        # The same seasons with availability projected from each team's previous game.
        blind_feats = fb.walk_forward(range(first, args.end + 1), availability="previous")
        blind = backtest.predict_seasons(blind_feats, seasons, hp.fit_window_seasons, n_sims=args.sims)
        b = backtest.errors(blind)
        if has_open.any():
            # The fair test against openers: the line did not know tonight's lineups either.
            picks[f"Opening line, {open_label}, assuming each team's previous lineup"] = backtest.pick_record(
                blind[blind["open_spread"].notna()], "open_spread", "spread")
        mean, lo, hi = backtest.paired_bootstrap(b["model"], err["model"])
        extra["Knowing who plays"] = [
            f"Model-only margin MAE {err['model'].mean():.3f} knowing who played, {b['model'].mean():.3f} "
            f"assuming each team's previous lineup (difference {mean:+.3f}, 95% interval {lo:+.3f} to {hi:+.3f}).",
            f"Final prediction {err['final'].mean():.3f} against {b['final'].mean():.3f} with the same closing lines.",
        ]
    path = OUTPUT_DIR / "backtest.md"
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    path.write_text(report.render_backtest(scores, checks, boot, (args.start, args.end), picks, extra))
    with pd.option_context("display.width", 200):
        for label, df in scores.items():
            print(label)
            print(df.round(4).to_string(index=False))
    for name, v in {**boot, **{k: (v["cover"], v["cover_low"], v["cover_high"]) for k, v in picks.items()}}.items():
        print(name, [round(x, 4) for x in v])
    for lines in extra.values():
        print("\n".join(lines))
    print(f"Wrote {path}")


def cmd_tune(args) -> None:
    from . import backtest
    from .data import load_summaries
    from .lines import load_lines

    summaries = load_summaries(FIRST_SEASON, args.end)
    grid = json.loads(args.grid) if args.grid else {
        "player_off_prior_poss": [1500.0, 3000.0, 6000.0],
        "player_def_prior_poss": [2000.0, 4000.0, 8000.0],
        "player_carryover": [0.7, 0.85, 1.0],
    }
    results = backtest.tune(summaries, load_lines(), list(range(args.start, args.end + 1)), grid, Hyperparams.load())
    print(results.round(4).to_string(index=False))
    if args.save:
        best = results.iloc[0]
        hp = Hyperparams.load()
        for key in grid:
            setattr(hp, key, type(getattr(hp, key))(best[key]))
        hp.save()
        print("Saved best settings to params.json")


def cmd_summarize(args) -> None:
    from .data import current_season, update_summaries

    last = current_season()
    seasons = list(range(FIRST_SEASON, last + 1))
    update_summaries(seasons, refresh=set(seasons) if args.all else {last}, max_age_hours=args.max_age_hours)
    print("Summaries are up to date.")


def cmd_lines(args) -> None:
    from .lines import build_lines

    lines = build_lines(max_age_hours=args.max_age_hours)
    print(f"Wrote {len(lines)} games of historical lines.")


def cmd_ratings(args) -> None:
    from .data import current_season, load_summaries
    from .features import FeatureBuilder
    from .lines import load_lines

    hp = Hyperparams.load()
    season = current_season()
    summaries = load_summaries(FIRST_SEASON, season)
    fb = FeatureBuilder(summaries, hp, load_lines())
    today = pd.Timestamp.now(tz=DISPLAY_TZ).date()
    now = fb.ratings_now(season, today)
    table = now["team"]["eff"].table().rename(columns={"off": "off_per100", "def": "def_per100", "net": "net_per100"})
    pace = now["team"]["pace"]
    table["pace"] = table["team"].map(lambda t: pace.mu + pace.off.get(t, 0.0) + pace.deff.get(t, 0.0))
    table["elo"] = table["team"].map(fb.elo_ratings)
    off, de, _ = now["players"]
    players = pd.DataFrame({"off": pd.Series(off), "def": pd.Series(de)})
    players["net"] = players["off"] - players["def"]
    players["name"] = fb.names.reindex(players.index)
    latest = fb.latest_minutes(pd.Timestamp(today, tz=DISPLAY_TZ).tz_convert("UTC"))
    players["minutes"] = latest.reindex(players.index)
    with pd.option_context("display.float_format", "{:.2f}".format, "display.width", 200):
        print(table.to_string(index=False))
        print()
        print(players[players["minutes"] >= 15].sort_values("net", ascending=False).head(40).to_string())


def cmd_check(args) -> None:
    """Read each live source once and print what was parsed, without predicting."""
    from . import espn
    from .pipeline import season_roster
    from .data import current_season

    today = pd.Timestamp.now(tz=DISPLAY_TZ).normalize()
    dates = pd.date_range(today, today + pd.Timedelta(days=args.ahead)).date
    board = espn.fetch_scoreboards(dates)
    print(f"ESPN scoreboard {dates[0]} to {dates[-1]}: {len(board)} games, {int(board['spread'].notna().sum())} "
          "with a spread")
    with pd.option_context("display.width", 250, "display.max_columns", 30):
        print(board.to_string(index=False))
    injuries = espn.fetch_injuries(ESPN_TEAM_IDS)
    print(f"ESPN injury report: {0 if injuries is None else len(injuries)} players")
    if injuries is not None and len(injuries):
        print(injuries["status"].value_counts().to_string())
        print(injuries.head(25).to_string(index=False))
        print("Rows without a player id:", int(injuries["player_id"].isna().sum()))
    roster, hurt = espn.fetch_rosters(ESPN_TEAM_IDS)
    print(f"ESPN rosters: {len(roster)} players on {roster['team'].nunique() if len(roster) else 0} teams; "
          f"{len(hurt)} with an injury status")
    if len(roster):
        print(roster.groupby("team").size().to_string())
    published = season_roster(current_season(), 1.0)
    print(f"Published season roster: {0 if published is None else len(published)} players")
    if args.raw:
        import requests
        for url in (espn.SCOREBOARD, espn.INJURIES, espn.ROSTER.format(team_id="2")):
            try:
                text = requests.get(url, timeout=30).text
                print(f"--- {url}\n{text[:args.raw]}")
            except requests.RequestException as exc:
                print(f"--- {url}: {exc}")


def main(argv=None) -> None:
    parser = argparse.ArgumentParser(prog="nbapredictor", description=__doc__)
    parser.add_argument("-v", "--verbose", action="store_true")
    parser.add_argument("--max-age-hours", type=float, default=1.0,
                        help="reuse downloaded data younger than this (default 1)")
    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("update", help="refresh data, predict upcoming games, grade results")
    p.add_argument("--days", type=int, default=2, help="upcoming game days to predict (default 2)")
    p.add_argument("--sims", type=int, default=10000, help="simulations per game (default 10000)")
    p.add_argument("--no-espn", action="store_true", help="skip ESPN lines, injuries and rosters")
    p.set_defaults(func=cmd_update)

    p = sub.add_parser("backtest", help="walk-forward backtest against the closing line")
    p.add_argument("--start", type=int, default=2016, help="first season, by the year it ends (default 2016)")
    p.add_argument("--end", type=int, default=2026)
    p.add_argument("--holdout", type=int, default=2017,
                   help="also report seasons from this one on separately (default 2017)")
    p.add_argument("--sims", type=int, default=2000, help="simulations per game (default 2000)")
    p.add_argument("--skip-blind", action="store_true", help="skip the previous-lineup comparison")
    p.set_defaults(func=cmd_backtest)

    p = sub.add_parser("tune", help="grid-search the ratings engine settings")
    p.add_argument("--start", type=int, default=2013)
    p.add_argument("--end", type=int, default=2016)
    p.add_argument("--grid", help='JSON grid, e.g. \'{"half_life_days": [30, 60]}\'')
    p.add_argument("--save", action="store_true", help="write the best settings to params.json")
    p.set_defaults(func=cmd_tune)

    p = sub.add_parser("summarize", help="rebuild season summaries from the raw data")
    p.add_argument("--all", action="store_true", help="rebuild every season, not just the current one")
    p.set_defaults(func=cmd_summarize)

    p = sub.add_parser("lines", help="rebuild data/lines.csv from the historical line archives")
    p.set_defaults(func=cmd_lines)

    p = sub.add_parser("ratings", help="print current team and player ratings")
    p.set_defaults(func=cmd_ratings)

    p = sub.add_parser("check", help="read ESPN's lines, injury report and rosters once and print them")
    p.add_argument("--ahead", type=int, default=2, help="days ahead to read (default 2)")
    p.add_argument("--raw", type=int, default=0, help="also print this many characters of each raw response")
    p.set_defaults(func=cmd_check)

    args = parser.parse_args(argv)
    logging.basicConfig(level=logging.INFO if args.verbose else logging.WARNING,
                        format="%(levelname)s %(name)s: %(message)s")
    args.func(args)
