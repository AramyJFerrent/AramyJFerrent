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
    from bettingcore import paired_bootstrap

    from . import backtest, report
    from .data import load_summaries
    from .features import FeatureBuilder

    hp = Hyperparams.load()
    summaries = load_summaries(FIRST_SEASON, args.end)
    fb = FeatureBuilder(summaries, hp)
    games = fb.games
    # The archived lines start in 2011; the first season the model can predict needs fit_window earlier ones.
    archive_first = max(2011, FIRST_SEASON + hp.fit_window_seasons)
    first = min(args.start, archive_first) - hp.fit_window_seasons
    feats = fb.build(games[games["season"].between(first, args.end) & games["completed"]])
    seasons = range(args.start, args.end + 1)
    bt = backtest.predict_seasons(feats, fb, seasons, hp.fit_window_seasons, n_sims=args.sims)
    scores = {f"{args.start} to {args.end}": backtest.score(bt)}
    if args.holdout and args.start < args.holdout <= args.end:
        scores[f"{args.holdout} on"] = backtest.score(bt[bt["season"] >= args.holdout])
    y = backtest.outcome(bt)
    losses = {k: backtest._log_loss(bt[c], y) for k, c in
              (("model", "home_win_prob"), ("elo", "elo_home_prob"), ("team", "team_only_prob"))}
    boot = {"Model vs Elo with starting pitchers": paired_bootstrap(losses["model"], losses["elo"]),
            "Model vs team runs ratings only": paired_bootstrap(losses["model"], losses["team"])}
    checks = backtest.distribution_checks(bt)
    market = backtest.market_comparison(bt, feats, fb, hp.fit_window_seasons, n_sims=max(args.sims, 8000))
    archive = None
    if not args.skip_archive:
        lines = backtest.archive_lines(feats)
        if len(lines):
            archive = backtest.market_backtest(feats, fb, lines, range(archive_first, args.end + 1),
                                               hp.fit_window_seasons, args.start, n_sims=args.sims)
    lineup_seasons = [s for s in range(max(args.start, args.end - 2), args.end + 1)]
    lineups = backtest.lineup_comparison(fb, feats, lineup_seasons, hp.fit_window_seasons, args.sims) \
        if not args.skip_lineups else None
    path = OUTPUT_DIR / "backtest.md"
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    path.write_text(report.render_backtest(scores, checks, boot, (args.start, args.end), market, lineups, archive))
    for label, df in scores.items():
        print(label)
        print(df.round(4).to_string(index=False))
    if market:
        print("Pinnacle 2016:", {k: round(float(v.mean()), 4) for k, v in market["losses"].items()},
              "blend weight", round(market["weight"], 2))
    if archive:
        if archive.get("losses"):
            print("Archived market:", {k: round(float(v.mean()), 4) for k, v in archive["losses"].items()},
                  "walk-forward weights", {s: round(w, 2) for s, w in archive["weights"].items()})
            for key, r in archive["edges"].items():
                print(report.archive_edge_label(*key) + ":", r["bets"], "edges, ROI",
                      f"{r['roi']:+.1%} ({r['roi_low']:+.1%} to {r['roi_high']:+.1%}), expected",
                      f"{r['expected_roi']:+.1%}" if r["bets"] else "")
        print("Blend weight on all archived seasons:", round(archive["all_weight"], 2), f"({archive['all_games']} games)")
        if args.save_weight:
            hp.market_weight = round(float(archive["all_weight"]), 2)
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
    days = pd.date_range(today, today + pd.Timedelta(days=args.ahead)).date
    board = espn.fetch_scoreboards(days)
    print(f"ESPN lines: {len(board)} games")
    with pd.option_context("display.width", 250, "display.max_columns", 30):
        print(board.to_string(index=False))
    if args.raw:
        import json

        # The raw odds objects behind those lines, to check the fields the parser reads.
        for day in days:
            try:
                odds = espn.raw_odds(espn.fetch_payload(day))
            except Exception as exc:
                print(f"ESPN raw odds {day}: {exc}")
                continue
            for name, raw in odds[:args.raw]:
                print(f"ESPN raw odds {day} {name}:")
                print(json.dumps(raw, indent=1, default=str)[:6000])
    upcoming = sched[sched["status"] == "scheduled"].copy() if len(sched) else sched
    if len(upcoming):
        history = pd.concat([read_summary(summary_paths(s)["games"], GAME_COLUMNS)
                             for s in range(current_season() - 2, current_season() + 1)], ignore_index=True)
        upcoming["park_id"] = statsapi.assign_parks(upcoming, history)
        upcoming["start"] = pd.to_datetime(upcoming["start"], utc=True)
        print("Temperature forecasts:")
        print(pd.concat([upcoming[["home_team", "park_id", "start"]], weather.forecast(upcoming)], axis=1)
              .to_string(index=False))


def audit_season(summaries: dict, season: int) -> dict:
    """Consistency checks on one season's summaries (each should be near 100%)."""
    import numpy as np

    g = summaries["games"]
    g = g[(g["season"] == season) & g["completed"]]
    bat = summaries["batting"][summaries["batting"]["game_id"].isin(g["game_id"])]
    pit = summaries["pitching"][summaries["pitching"]["game_id"].isin(g["game_id"])]
    players = summaries["players"].drop_duplicates("player_id").set_index("player_id")
    line_sum = {side: g[f"{side}_line"].fillna("").str.split().map(lambda p: sum(int(v) for v in p if v != "x"))
                for side in ("home", "away")}
    sides = []
    for side, other in (("home", "away"), ("away", "home")):
        sides.append(pd.DataFrame({"game_id": g["game_id"], "team": g[f"{side}_team"], "opp": g[f"{other}_team"],
                                   "score": g[f"{side}_score"]}))
    tg = pd.concat(sides, ignore_index=True)
    b = bat.groupby(["game_id", "team"])[["pa", "k", "bb", "hr"]].sum()
    p = pit.groupby(["game_id", "team"])[["bf", "k", "bb", "hr", "r", "outs"]].sum()
    tg = tg.join(b, on=["game_id", "team"]).join(p.add_prefix("opp_"), on=["game_id", "opp"])
    starters = bat[bat["slot"].between(1, 9)].groupby(["game_id", "team"])["slot"].nunique()
    sp = pit.groupby(["game_id", "team"])["starter"].sum()
    known = lambda ids: float(pd.Series(ids).map(players["throws"]).isin(["L", "R"]).mean())
    open_air = g[g["dome"].fillna(0).eq(0)]
    return {
        "finished games": len(g),
        "line score adds up to the final": float((line_sum["home"] == g["home_score"]).mean()
                                                  * (line_sum["away"] == g["away_score"]).mean()),
        "innings recorded": float(g["innings"].notna().mean()),
        "plate appearances match batters faced": float((tg["pa"] == tg["opp_bf"]).mean()),
        "strikeouts, walks and homers match": float(((tg["k"] == tg["opp_k"]) & (tg["bb"] == tg["opp_bb"])
                                                     & (tg["hr"] == tg["opp_hr"])).mean()),
        "runs charged match the score": float((tg["opp_r"] == tg["score"]).mean()),
        "outs per team-game": float(tg["opp_outs"].mean()),
        "nine-man starting lineups": float((starters == 9).mean()),
        "one starting pitcher per team": float((sp == 1).mean()),
        "starters named in the schedule": float(g[["home_starter", "away_starter"]].notna().all(axis=1).mean()),
        "batters with a known hand": known(bat["player_id"].unique()),
        "pitchers with a known hand": known(pit["player_id"].unique()),
        "temperature at open-air games": float(open_air["temp"].notna().mean()) if len(open_air) else np.nan,
        "games under a roof": float(g["dome"].fillna(0).mean()),
        "neutral-site games": int(g["neutral"].sum()),
        "parks": int(g["park_id"].nunique()),
        "extra-inning games (regular season)": float((g.loc[g["game_type"] == "R", "innings"] > 9).mean()),
        "runs per game": float((g["home_score"] + g["away_score"]).mean()),
    }


def cmd_audit(args) -> None:
    from .data import load_summaries

    season = args.season or current_season()
    summaries = load_summaries(season - 1, season)
    rows = {s: audit_season(summaries, s) for s in (season - 1, season)}
    table = pd.DataFrame(rows)
    with pd.option_context("display.float_format", "{:.3f}".format, "display.width", 200):
        print(table.to_string())
    g = summaries["games"]
    g = g[g["season"] == season]
    print(g.groupby("home_team")["park_id"].agg(lambda s: s.value_counts().to_dict()).to_string())


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

    p = sub.add_parser("backtest", help="walk-forward backtest against the baselines and archived lines")
    p.add_argument("--start", type=int, default=2016)
    p.add_argument("--end", type=int, default=2025)
    p.add_argument("--holdout", type=int, default=2021, help="also report seasons from this one on")
    p.add_argument("--sims", type=int, default=2000, help="simulations per game (default 2000)")
    p.add_argument("--skip-lineups", action="store_true", help="skip the projected-lineup comparison")
    p.add_argument("--skip-archive", action="store_true", help="skip the archived-lines market backtest")
    p.add_argument("--save-weight", action="store_true",
                   help="save the blend weight fitted on the archived lines to params.json")
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
    p.add_argument("--raw", type=int, nargs="?", const=3, default=0,
                   help="also print the raw ESPN odds objects of the first N games each day (default 3)")
    p.set_defaults(func=cmd_check)

    p = sub.add_parser("audit", help="consistency checks on a season's data, next to the season before")
    p.add_argument("--season", type=int)
    p.set_defaults(func=cmd_audit)

    args = parser.parse_args(argv)
    logging.basicConfig(level=logging.INFO if args.verbose else logging.WARNING,
                        format="%(levelname)s %(name)s: %(message)s")
    args.func(args)
