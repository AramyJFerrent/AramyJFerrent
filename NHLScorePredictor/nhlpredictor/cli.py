"""Command-line entry point: ``python -m nhlpredictor <command>``."""

from __future__ import annotations

import argparse
import logging

import pandas as pd

from .config import FIRST_SEASON, OUTPUT_DIR, SHOT_MODEL_PATH, SHOT_MODEL_SEASONS, Hyperparams, season_label


def cmd_update(args) -> None:
    from .pipeline import README_PATH, run_update

    new = run_update(days=args.days, n_sims=args.sims, use_espn=not args.no_espn,
                     max_age_hours=args.max_age_hours)
    print(f"Predicted {len(new)} upcoming games. See {README_PATH}")


def cmd_backtest(args) -> None:
    from . import backtest, report
    from .data import load_summaries
    from .features import FeatureBuilder

    hp = Hyperparams.load()
    summaries = load_summaries(FIRST_SEASON, args.end)
    games = summaries["games"]
    fb = FeatureBuilder(games, summaries, hp)
    first = max(args.start - hp.fit_window_seasons, FIRST_SEASON + 1)
    seasons = range(args.start, args.end + 1)
    feats = fb.walk_forward(range(first, args.end + 1))
    bt = backtest.predict_seasons(feats, summaries["states"], seasons, hp.fit_window_seasons, n_sims=args.sims)
    scores = {f"{season_label(args.start)} to {season_label(args.end)}": backtest.score(bt)}
    if args.holdout and args.start < args.holdout <= args.end:
        scores[f"{season_label(args.holdout)} on (seasons not used for tuning)"] = backtest.score(
            bt[bt["season"] >= args.holdout])
    losses = backtest.log_losses(bt)
    boot = {
        "Model vs Elo": backtest.paired_bootstrap(losses["model"], losses["elo"]),
        "Model vs goals-only Poisson": backtest.paired_bootstrap(losses["model"], losses["baseline"]),
    }
    checks = backtest.distribution_checks(bt)

    # The same seasons with starters projected from usage, as a morning run before confirmations.
    blind_feats = fb.walk_forward(range(first, args.end + 1), known_starters=False)
    blind = backtest.predict_seasons(blind_feats, summaries["states"], seasons, hp.fit_window_seasons,
                                     n_sims=args.sims)
    blind_loss = backtest.log_losses(blind)["model"]
    test_feats = feats[feats["season"].between(args.start, args.end)]
    accuracy = backtest.starter_accuracy(blind_feats[blind_feats["season"].between(args.start, args.end)],
                                         test_feats)
    mean, lo, hi = backtest.paired_bootstrap(losses["model"], blind_loss)
    extra = {"goalie_lines": [
        f"Projected starter was the actual starter {accuracy:.1%} of the time.",
        f"Log loss with projected starters: {blind_loss.mean():.4f}, against {losses['model'].mean():.4f} with "
        f"the confirmed starter (difference {mean:+.4f}, 95% interval {lo:+.4f} to {hi:+.4f}).",
    ]}
    path = OUTPUT_DIR / "backtest.md"
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    path.write_text(report.render_backtest(scores, checks, boot, (args.start, args.end), extra))
    for label, df in scores.items():
        print(label)
        print(df.round(4).to_string(index=False))
    for line in extra["goalie_lines"]:
        print(line)
    print(f"Wrote {path}")


def cmd_tune(args) -> None:
    from . import backtest
    from .data import load_summaries

    summaries = load_summaries(FIRST_SEASON, args.end)
    grid = {
        "ev_prior_minutes": [500.0, 1000.0, 2000.0],
        "goals_prior_games": [25.0, 50.0, 100.0],
        "carryover": [0.4, 0.55, 0.7],
        "half_life_days": [45.0, 120.0, 1000.0],
    }
    results = backtest.tune(summaries["games"], summaries, list(range(args.start, args.end + 1)), grid,
                            Hyperparams.load())
    print(results.round(5).to_string(index=False))
    if args.save:
        best = results.iloc[0]
        hp = Hyperparams.load()
        for key in grid:
            setattr(hp, key, float(best[key]))
        hp.save()
        print("Saved best settings to params.json")


def cmd_fit_shots(args) -> None:
    from .data import load_raw
    from .shots import fit_shot_model

    first, last = SHOT_MODEL_SEASONS
    pbps = [load_raw("pbp", s, args.max_age_hours) for s in range(first, last + 1)]
    model = fit_shot_model(pbps, SHOT_MODEL_SEASONS)
    model.save()
    print(f"Saved {SHOT_MODEL_PATH} (log loss {model.meta['log_loss']}, "
          f"constant {model.meta['constant_log_loss']}). Rebuild summaries with `summarize --all`.")


def cmd_summarize(args) -> None:
    from .data import current_season, update_summaries

    last = current_season()
    seasons = list(range(FIRST_SEASON, last + 1))
    update_summaries(seasons, refresh=set(seasons) if args.all else {last}, max_age_hours=args.max_age_hours)
    print("Summaries are up to date.")


def cmd_ratings(args) -> None:
    from .data import current_season, load_summaries
    from .features import FeatureBuilder
    from .pipeline import goalie_table

    hp = Hyperparams.load()
    season = current_season()
    summaries = load_summaries(FIRST_SEASON, season)
    fb = FeatureBuilder(summaries["games"], summaries, hp)
    today = pd.Timestamp.now(tz="America/New_York").date()
    _, ratings = fb.current(summaries["games"].iloc[:0], season, today)
    table = ratings["ev"].table().rename(columns={"off": "xgf60_vs_avg", "def": "xga60_vs_avg", "net": "ev_net"})
    for name in ("pp", "draw", "goals"):
        table[f"{name}_off"] = table["team"].map(ratings[name].off)
        table[f"{name}_def"] = table["team"].map(ratings[name].deff)
    table["elo"] = table["team"].map(fb.elo_ratings)
    with pd.option_context("display.float_format", "{:.3f}".format, "display.width", 200):
        print(table.to_string(index=False))
        print()
        print(goalie_table(fb, season, today).to_string(index=False))


def main(argv=None) -> None:
    parser = argparse.ArgumentParser(prog="nhlpredictor", description=__doc__)
    parser.add_argument("-v", "--verbose", action="store_true")
    parser.add_argument("--max-age-hours", type=float, default=1.0,
                        help="reuse downloaded data younger than this (default 1)")
    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("update", help="refresh data, predict upcoming games, grade results")
    p.add_argument("--days", type=int, default=3, help="upcoming game days to predict (default 3)")
    p.add_argument("--sims", type=int, default=10000, help="simulations per game (default 10000)")
    p.add_argument("--no-espn", action="store_true", help="skip ESPN lines and probable goalies")
    p.set_defaults(func=cmd_update)

    p = sub.add_parser("backtest", help="walk-forward backtest against the baselines")
    p.add_argument("--start", type=int, default=2017, help="first season, by the year it ends (default 2017)")
    p.add_argument("--end", type=int, default=2026)
    p.add_argument("--holdout", type=int, default=2018,
                   help="also report seasons from this one on separately (default 2018)")
    p.add_argument("--sims", type=int, default=2000, help="simulations per game (default 2000)")
    p.set_defaults(func=cmd_backtest)

    p = sub.add_parser("tune", help="grid-search the ratings engine settings")
    p.add_argument("--start", type=int, default=2014)
    p.add_argument("--end", type=int, default=2017)
    p.add_argument("--save", action="store_true", help="write the best settings to params.json")
    p.set_defaults(func=cmd_tune)

    p = sub.add_parser("fit-shots", help="refit the frozen expected-goals model")
    p.set_defaults(func=cmd_fit_shots)

    p = sub.add_parser("summarize", help="rebuild season summaries from play-by-play")
    p.add_argument("--all", action="store_true", help="rebuild every season, not just the current one")
    p.set_defaults(func=cmd_summarize)

    p = sub.add_parser("ratings", help="print current team ratings and likely starting goalies")
    p.set_defaults(func=cmd_ratings)

    args = parser.parse_args(argv)
    logging.basicConfig(level=logging.INFO if args.verbose else logging.WARNING,
                        format="%(levelname)s %(name)s: %(message)s")
    args.func(args)
