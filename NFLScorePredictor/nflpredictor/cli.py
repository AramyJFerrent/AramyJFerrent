"""Command-line entry point: ``python -m nflpredictor <command>``."""

from __future__ import annotations

import argparse
import logging

import numpy as np
import pandas as pd

from .config import FIRST_SEASON, OUTPUT_DIR, Hyperparams


def cmd_update(args) -> None:
    from .pipeline import README_PATH, run_update

    new = run_update(weeks=args.weeks, n_sims=args.sims, use_weather=not args.no_weather,
                     max_age_hours=args.max_age_hours)
    print(f"Predicted {len(new)} upcoming games. See {README_PATH}")


def cmd_backtest(args) -> None:
    from . import backtest, report
    from .data import load_games, load_summaries
    from .features import FeatureBuilder

    hp = Hyperparams.load()
    games = load_games(args.max_age_hours)
    team_games, qbs = load_summaries(FIRST_SEASON, args.end)
    fb = FeatureBuilder(games, team_games, qbs, hp)
    feats = fb.walk_forward(range(max(args.start - hp.fit_window_seasons, FIRST_SEASON + 1), args.end + 1))
    bt = backtest.predict_seasons(feats, range(args.start, args.end + 1), hp.fit_window_seasons)
    bt = bt[bt["spread_line"].notna() & bt["total_line"].notna()]
    scores = {f"{args.start}–{args.end}": backtest.score(bt)}
    if args.holdout and args.start < args.holdout <= args.end:
        scores[f"{args.holdout}–{args.end} (seasons not used for tuning)"] = backtest.score(
            bt[bt["season"] >= args.holdout])
    margin = (bt["home_score"] - bt["away_score"]).to_numpy()
    err = {k: np.abs(margin - bt[c].to_numpy()) for k, c in
           [("final", "pred_margin"), ("model", "pred_model_margin"), ("elo", "elo_spread"), ("line", "spread_line")]}
    boot = {
        "Final vs closing line": backtest.paired_bootstrap(err["final"], err["line"]),
        "Model only vs Elo": backtest.paired_bootstrap(err["model"], err["elo"]),
        "Model only vs closing line": backtest.paired_bootstrap(err["model"], err["line"]),
    }
    checks = backtest.distribution_checks(bt)
    path = OUTPUT_DIR / "backtest.md"
    path.write_text(report.render_backtest(scores, checks, boot, (args.start, args.end)))
    for label, df in scores.items():
        print(label)
        print(df.round(3).to_string(index=False))
    print(f"Wrote {path}")


def cmd_tune(args) -> None:
    from . import backtest
    from .data import load_games, load_summaries

    games = load_games(args.max_age_hours)
    team_games, qbs = load_summaries(FIRST_SEASON, args.end)
    grid = {
        "off_prior_plays": [400.0, 600.0, 900.0],
        "def_prior_plays": [800.0, 1200.0, 1800.0],
        "half_life_weeks": [15.0, 30.0, 60.0],
    }
    results = backtest.tune(games, team_games, qbs, list(range(args.start, args.end + 1)), grid,
                            Hyperparams.load())
    print(results.round(4).to_string(index=False))
    if args.save:
        best = results.iloc[0]
        hp = Hyperparams.load()
        for key in grid:
            setattr(hp, key, float(best[key]))
        hp.save()
        print("Saved best settings to params.json")


def cmd_ratings(args) -> None:
    from .data import current_season, load_games, load_summaries
    from .features import FeatureBuilder

    hp = Hyperparams.load()
    season = current_season()
    games = load_games(args.max_age_hours)
    team_games, qbs = load_summaries(FIRST_SEASON, season)
    fb = FeatureBuilder(games, team_games, qbs, hp)
    _, ratings = fb.current(games.iloc[:0], season)
    table = ratings.table()
    table["elo"] = table["team"].map(fb.elo_ratings)
    with pd.option_context("display.float_format", "{:.3f}".format):
        print(table.to_string(index=False))


def main(argv=None) -> None:
    parser = argparse.ArgumentParser(prog="nflpredictor", description=__doc__)
    parser.add_argument("-v", "--verbose", action="store_true")
    parser.add_argument("--max-age-hours", type=float, default=1.0,
                        help="reuse downloaded data younger than this (default 1)")
    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("update", help="refresh data, predict upcoming games, grade results")
    p.add_argument("--weeks", type=int, default=2, help="upcoming weeks to predict (default 2)")
    p.add_argument("--sims", type=int, default=10000, help="simulations per game (default 10000)")
    p.add_argument("--no-weather", action="store_true", help="skip wind forecasts")
    p.set_defaults(func=cmd_update)

    p = sub.add_parser("backtest", help="walk-forward backtest against the closing line")
    p.add_argument("--start", type=int, default=2015)
    p.add_argument("--end", type=int, default=2025)
    p.add_argument("--holdout", type=int, default=2019,
                   help="also report seasons from this one on separately (default 2019)")
    p.set_defaults(func=cmd_backtest)

    p = sub.add_parser("tune", help="grid-search the ratings engine settings")
    p.add_argument("--start", type=int, default=2013)
    p.add_argument("--end", type=int, default=2018)
    p.add_argument("--save", action="store_true", help="write the best settings to params.json")
    p.set_defaults(func=cmd_tune)

    p = sub.add_parser("ratings", help="print current team ratings (EPA per play)")
    p.set_defaults(func=cmd_ratings)

    args = parser.parse_args(argv)
    logging.basicConfig(level=logging.INFO if args.verbose else logging.WARNING,
                        format="%(levelname)s %(name)s: %(message)s")
    args.func(args)
