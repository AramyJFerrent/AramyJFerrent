"""Command-line entry point: ``python -m cfbpredictor <command>``."""

from __future__ import annotations

import argparse
import json
import logging

import numpy as np
import pandas as pd

from .config import ELO_FIRST_SEASON, FIRST_SEASON, LINES_PATH, OUTPUT_DIR, VENUES_PATH, Hyperparams


def cmd_update(args) -> None:
    from .pipeline import README_PATH, run_update

    new = run_update(weeks=args.weeks, n_sims=args.sims, use_live_lines=not args.no_lines,
                     max_age_hours=args.max_age_hours)
    print(f"Predicted {len(new)} upcoming games. See {README_PATH}")


def _inputs(args, last: int):
    from .data import load_games, load_summaries
    from .lines import load_lines
    from .returning import load_returning
    from .travel import load_venues

    games = load_games(ELO_FIRST_SEASON, last, args.max_age_hours)
    team_games = load_summaries(FIRST_SEASON, last)
    return games, team_games, load_returning(), load_lines(ELO_FIRST_SEASON, last), load_venues()


def cmd_backtest(args) -> None:
    from . import backtest, report
    from .features import FeatureBuilder
    from .pipeline import FIRST_FIT_SEASON

    hp = Hyperparams.load()
    games, team_games, returning, lines, venues = _inputs(args, args.end)
    fb = FeatureBuilder(games, team_games, returning, lines, venues, hp)
    feats = fb.walk_forward(range(FIRST_FIT_SEASON, args.end + 1))
    seasons = range(args.start, args.end + 1)
    bt = backtest.predict_seasons(feats, seasons, hp.fit_window_seasons, first_fit_season=FIRST_FIT_SEASON)
    bt = bt[bt["spread_line"].notna() & bt["total_line"].notna()]
    fbs = bt[backtest.segments(bt)["FBS vs FBS"]]
    scores = {f"FBS vs FBS, {args.start}–{args.end}": backtest.score(fbs),
              f"All games with a line (FCS opponents included), {args.start}–{args.end}": backtest.score(bt)}
    if args.holdout and args.start < args.holdout <= args.end:
        scores[f"FBS vs FBS, {args.holdout}–{args.end} (seasons not used for tuning)"] = backtest.score(
            fbs[fbs["season"] >= args.holdout])
    margin = (fbs["home_score"] - fbs["away_score"]).to_numpy()
    err = {k: np.abs(margin - fbs[c].to_numpy()) for k, c in
           [("final", "pred_margin"), ("model", "pred_model_margin"), ("elo", "elo_spread"), ("line", "spread_line")]}
    boot = {
        "Final vs closing line": backtest.paired_bootstrap(err["final"], err["line"]),
        "Model only vs Elo": backtest.paired_bootstrap(err["model"], err["elo"]),
        "Model only vs closing line": backtest.paired_bootstrap(err["model"], err["line"]),
    }
    checks = backtest.distribution_checks(bt)

    margins = backtest.model_margins(feats, seasons, hp.fit_window_seasons, FIRST_FIT_SEASON)
    margins = margins[backtest.segments(margins)["FBS vs FBS"] & margins["spread_line"].notna()]
    opened = margins[margins["spread_open"].notna()]
    span = f"{int(opened['season'].min())}–{int(opened['season'].max())}" if len(opened) else ""
    picks = {
        f"Opening line, {span} (games with one)": backtest.pick_record(opened, "spread_open", closing_col="spread_line"),
        f"Closing line, same {span} games": backtest.pick_record(opened, "spread_line"),
        f"Closing line, {args.start}–{args.end}": backtest.pick_record(margins, "spread_line"),
    }
    path = OUTPUT_DIR / "backtest.md"
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    path.write_text(report.render_backtest(scores, backtest.segment_table(bt), checks, boot,
                                           (args.start, args.end), picks))
    opening, _, closing = picks.values()
    summary = {"seasons": [args.start, args.end],
               "picks": {"opening": {**opening, "span": span},
                         "closing": {**closing, "span": f"{args.start}–{args.end}"}},
               "fbs": backtest.score(fbs).set_index("predictor")[["margin_mae", "total_mae"]].round(3).to_dict("index")}
    report.BACKTEST_SUMMARY_PATH.write_text(json.dumps(summary, indent=2) + "\n")
    for label, rec in picks.items():
        print(f"{label}: {rec['wins']}-{rec['losses']}-{rec['pushes']} ({rec['cover']:.1%})"
              + (f", line moved toward pick {rec['moved_toward']:.1%}" if "moved_toward" in rec else ""))
    for label, df in scores.items():
        print(label)
        print(df.round(3).to_string(index=False))
    print(backtest.segment_table(bt).round(2).to_string(index=False))
    print(f"Wrote {path}")


def cmd_tune(args) -> None:
    from . import backtest

    games, team_games, returning, lines, venues = _inputs(args, args.end)
    grid = {
        "off_prior_plays": [250.0, 400.0, 600.0],
        "def_prior_plays": [450.0, 600.0, 800.0],
        "conf_prior_plays": [1000.0, 15000.0],
    }
    results = backtest.tune(games, team_games, returning, lines, venues,
                            list(range(args.start, args.end + 1)), grid, Hyperparams.load())
    print(results.round(4).to_string(index=False))
    if args.save:
        best = results.iloc[0]
        hp = Hyperparams.load()
        for key in grid:
            setattr(hp, key, float(best[key]))
        hp.save()
        print("Saved best settings to params.json")


def cmd_ratings(args) -> None:
    from .data import current_season
    from .features import FeatureBuilder

    hp = Hyperparams.load()
    season = current_season()
    games, team_games, returning, lines, venues = _inputs(args, season)
    fb = FeatureBuilder(games, team_games, returning, lines, venues, hp)
    _, ratings = fb.current([], season)
    table = ratings["epa"].table()
    members = fb.members.get(season, {})
    table["conference"] = table["team"].map({t: c for t, (c, _) in members.items()})
    table["division"] = table["team"].map({t: d for t, (_, d) in members.items()})
    table["st"] = table["team"].map(ratings["st"].off) - table["team"].map(ratings["st"].deff)
    table["elo"] = table["team"].map(fb.elo_ratings)
    if not args.all:
        table = table[table["division"] == "fbs"]
    with pd.option_context("display.float_format", "{:.3f}".format, "display.max_rows", 400):
        print(table.reset_index(drop=True).to_string())


def cmd_build_data(args) -> None:
    """Rebuild every committed data file from scratch (several hundred MB of downloads)."""
    from . import returning
    from .data import current_season, update_summaries
    from .lines import build_consensus
    from .travel import build_venues

    last = current_season()
    seasons = list(range(FIRST_SEASON, last + 1))
    update_summaries(seasons, refresh=set(seasons), max_age_hours=args.max_age_hours, keep_raw=not args.drop_raw)
    build_consensus(args.max_age_hours).to_csv(LINES_PATH, index=False, float_format="%.1f")
    returning.rebuild(last, args.max_age_hours)
    build_venues(seasons).to_csv(VENUES_PATH, index=False)
    print("Rebuilt season summaries, lines, returning production and venues")


def main(argv=None) -> None:
    parser = argparse.ArgumentParser(prog="cfbpredictor", description=__doc__)
    parser.add_argument("-v", "--verbose", action="store_true")
    parser.add_argument("--max-age-hours", type=float, default=1.0,
                        help="reuse downloaded data younger than this (default 1)")
    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("update", help="refresh data, predict upcoming games, grade results")
    p.add_argument("--weeks", type=int, default=2, help="upcoming weeks to predict (default 2)")
    p.add_argument("--sims", type=int, default=10000, help="simulations per game (default 10000)")
    p.add_argument("--no-lines", action="store_true", help="skip fetching live betting lines")
    p.set_defaults(func=cmd_update)

    p = sub.add_parser("backtest", help="walk-forward backtest against the closing line")
    p.add_argument("--start", type=int, default=2016)
    p.add_argument("--end", type=int, default=2025)
    p.add_argument("--holdout", type=int, default=2021,
                   help="also report seasons from this one on separately (default 2021)")
    p.set_defaults(func=cmd_backtest)

    p = sub.add_parser("tune", help="grid-search the ratings engine settings")
    p.add_argument("--start", type=int, default=2016)
    p.add_argument("--end", type=int, default=2020)
    p.add_argument("--save", action="store_true", help="write the best settings to params.json")
    p.set_defaults(func=cmd_tune)

    p = sub.add_parser("ratings", help="print current team ratings (EPA per play; special teams per game)")
    p.add_argument("--all", action="store_true", help="include FCS teams")
    p.set_defaults(func=cmd_ratings)

    p = sub.add_parser("build-data", help="rebuild all committed data files from the sources")
    p.add_argument("--drop-raw", action="store_true", help="delete raw play-by-play after summarizing")
    p.set_defaults(func=cmd_build_data)

    args = parser.parse_args(argv)
    logging.basicConfig(level=logging.INFO if args.verbose else logging.WARNING,
                        format="%(levelname)s %(name)s: %(message)s")
    args.func(args)
