"""Command-line entry point: ``python -m mlbpredictor <command>``."""

from __future__ import annotations

import argparse
import logging

import pandas as pd

from .config import DISPLAY_TZ, FIRST_SEASON, OUTPUT_DIR, Hyperparams, current_season


def cmd_update(args) -> None:
    from .pipeline import README_PATH, run_update

    new = run_update(days=args.days, n_sims=args.sims, use_web=not args.offline)
    print(f"Predicted {len(new)} upcoming games. See {README_PATH}")


def cmd_backtest(args) -> None:
    from . import backtest, report
    from .data import load_summaries
    from .features import FeatureBuilder

    hp = Hyperparams.load()
    summaries = load_summaries(FIRST_SEASON, args.end)
    fb = FeatureBuilder(summaries, hp)
    games = fb.games
    first = args.start - hp.fit_window_seasons
    feats = fb.build(games[games["season"].between(first, args.end) & games["completed"]])
    seasons = range(args.start, args.end + 1)
    bt = backtest.predict_seasons(feats, fb, seasons, hp.fit_window_seasons, n_sims=args.sims)
    scores = {f"{args.start} to {args.end}": backtest.score(bt)}
    if args.holdout and args.start < args.holdout <= args.end:
        scores[f"{args.holdout} on"] = backtest.score(bt[bt["season"] >= args.holdout])
    y = backtest.outcome(bt)
    losses = {k: backtest._log_loss(bt[c], y) for k, c in
              (("model", "home_win_prob"), ("elo", "elo_home_prob"), ("team", "team_only_prob"))}
    boot = {"Model vs Elo with starting pitchers": backtest.paired_bootstrap(losses["model"], losses["elo"]),
            "Model vs team runs ratings only": backtest.paired_bootstrap(losses["model"], losses["team"])}
    checks = backtest.distribution_checks(bt)
    market = backtest.market_comparison(bt, feats, fb, hp.fit_window_seasons, n_sims=args.sims)
    lineup_seasons = [s for s in range(max(args.start, args.end - 2), args.end + 1)]
    lineups = backtest.lineup_comparison(fb, feats, lineup_seasons, hp.fit_window_seasons, args.sims) \
        if not args.skip_lineups else None
    path = OUTPUT_DIR / "backtest.md"
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    path.write_text(report.render_backtest(scores, checks, boot, (args.start, args.end), market, lineups))
    for label, df in scores.items():
        print(label)
        print(df.round(4).to_string(index=False))
    if market:
        print("2016 market:", {k: round(float(v.mean()), 4) for k, v in market["losses"].items()},
              "blend weight", round(market["weight"], 2))
        if args.save_weight:
            hp.market_weight = round(float(market["weight"]), 2)
            hp.save()
            print("Saved the blend weight to params.json")
    if lineups:
        print("Lineups:", lineups)
    print(f"Wrote {path}")


def cmd_summarize(args) -> None:
    from .data import build_retro_seasons, retrosheet_has

    last = current_season()
    seasons = [s for s in range(args.start or FIRST_SEASON, (args.end or last) + 1) if retrosheet_has(s)]
    build_retro_seasons(seasons)
    print(f"Rebuilt {len(seasons)} seasons from Retrosheet.")


def cmd_ratings(args) -> None:
    from .data import load_summaries
    from .features import FeatureBuilder
    from .model import RunModel
    from .pipeline import power_ratings

    hp = Hyperparams.load()
    season = current_season()
    summaries = load_summaries(FIRST_SEASON, season)
    fb = FeatureBuilder(summaries, hp)
    today = pd.Timestamp.now(tz=DISPLAY_TZ).date()
    games = fb.games
    feats = fb.build(games[games["season"].between(season - hp.fit_window_seasons, season) & games["completed"]
                           & (pd.to_datetime(games["date"]) < pd.Timestamp(today))])
    model = RunModel.fit(feats, calibrate_sim=False)
    with pd.option_context("display.float_format", "{:.2f}".format, "display.width", 200):
        print(power_ratings(fb, model, season, today).to_string(index=False))


def cmd_check(args) -> None:
    """Read each live source once and print what was parsed, without predicting."""
    from . import espn, statsapi, weather
    from .data import GAME_COLUMNS, read_summary, summary_paths

    today = pd.Timestamp.now(tz=DISPLAY_TZ).normalize()
    start, end = (today - pd.Timedelta(days=args.back)).date(), (today + pd.Timedelta(days=args.ahead)).date()
    sched = statsapi.fetch_schedule(start, end, hydrate=statsapi.UPCOMING_HYDRATE)
    print(f"MLB Stats API schedule {start} to {end}: {len(sched)} games")
    if len(sched):
        cols = ["game_id", "date", "game_type", "status", "away_team", "home_team", "away_score", "home_score",
                "away_starter_name", "home_starter_name", "venue_name", "temp", "dome", "wind", "wind_speed",
                "away_line", "home_line"]
        with pd.option_context("display.width", 250, "display.max_columns", 30):
            print(sched[cols].to_string(index=False))
            print("Posted lineups:", int(sum(len(x) >= 9 for x in sched["home_lineup_ids"])
                                         + sum(len(x) >= 9 for x in sched["away_lineup_ids"])))
        final = sched[sched["status"] == "final"]
        if len(final):
            box = statsapi.fetch_boxscores(final["game_id"].head(1).tolist())
            for gid, b in box.items():
                bat, pit = pd.DataFrame(b["batting"]), pd.DataFrame(b["pitching"])
                print(f"Box score {gid}: starters {b['starters']}, weather {b['weather']}")
                print(bat.to_string(index=False))
                print(pit.to_string(index=False))
                runs = {t: int(pit[pit["team"] != t]["r"].sum()) for t in pit["team"].unique()}
                print("Runs allowed by the other side's pitchers:", runs)
        people = statsapi.fetch_people(sched["home_starter"].dropna().head(3).tolist())
        print(people.to_string(index=False))
    board = espn.fetch_scoreboards(pd.date_range(today, today + pd.Timedelta(days=args.ahead)).date)
    print(f"ESPN lines: {len(board)} games")
    print(board.to_string(index=False))
    upcoming = sched[sched["status"] == "scheduled"].copy() if len(sched) else sched
    if len(upcoming):
        history = pd.concat([read_summary(summary_paths(s)["games"], GAME_COLUMNS)
                             for s in range(current_season() - 2, current_season() + 1)], ignore_index=True)
        upcoming["park_id"] = statsapi.assign_parks(upcoming, history)
        upcoming["start"] = pd.to_datetime(upcoming["start"], utc=True)
        print("Temperature forecasts:")
        print(pd.concat([upcoming[["home_team", "park_id", "start"]], weather.forecast(upcoming)], axis=1)
              .to_string(index=False))


def main(argv=None) -> None:
    parser = argparse.ArgumentParser(prog="mlbpredictor", description=__doc__)
    parser.add_argument("-v", "--verbose", action="store_true")
    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("update", help="refresh data, predict upcoming games, grade results")
    p.add_argument("--days", type=int, default=2, help="upcoming game days to predict (default 2)")
    p.add_argument("--sims", type=int, default=10000, help="simulations per game (default 10000)")
    p.add_argument("--offline", action="store_true",
                   help="use only committed data: no downloads, lines, lineups or forecasts")
    p.set_defaults(func=cmd_update)

    p = sub.add_parser("backtest", help="walk-forward backtest against the baselines and 2016 lines")
    p.add_argument("--start", type=int, default=2016)
    p.add_argument("--end", type=int, default=2025)
    p.add_argument("--holdout", type=int, default=2021, help="also report seasons from this one on")
    p.add_argument("--sims", type=int, default=2000, help="simulations per game (default 2000)")
    p.add_argument("--skip-lineups", action="store_true", help="skip the projected-lineup comparison")
    p.add_argument("--save-weight", action="store_true", help="save the 2016 blend weight to params.json")
    p.set_defaults(func=cmd_backtest)

    p = sub.add_parser("summarize", help="rebuild season summaries from Retrosheet play-by-play")
    p.add_argument("--start", type=int)
    p.add_argument("--end", type=int)
    p.set_defaults(func=cmd_summarize)

    p = sub.add_parser("ratings", help="print current power ratings by unit")
    p.set_defaults(func=cmd_ratings)

    p = sub.add_parser("check", help="read the live sources once and print what was parsed")
    p.add_argument("--back", type=int, default=2, help="days back to read (default 2)")
    p.add_argument("--ahead", type=int, default=2, help="days ahead to read (default 2)")
    p.set_defaults(func=cmd_check)

    args = parser.parse_args(argv)
    logging.basicConfig(level=logging.INFO if args.verbose else logging.WARNING,
                        format="%(levelname)s %(name)s: %(message)s")
    args.func(args)
