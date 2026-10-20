"""Markdown pages for the predictions folder."""

from __future__ import annotations

import math

import numpy as np
import pandas as pd

from .config import DISPLAY_TZ
from .edges import (DEFAULT_RUN_LINE, EDGE_MIN_EV, MARKET_NAMES, MARKETS, american, best_side, edge_record,
                    fair_american)

SERIES = {"F": "Wild Card Series", "D": "Division Series", "L": "League Championship Series", "W": "World Series"}


def _time(ts) -> str:
    if ts is None or pd.isna(ts):
        return "TBD"
    t = pd.Timestamp(ts).tz_convert(DISPLAY_TZ)
    return t.strftime("%I:%M %p").lstrip("0")


def _day(date) -> str:
    return pd.Timestamp(date).strftime("%A, %B %d").replace(" 0", " ")


def _num(x, fmt="{:.1f}") -> str:
    return "–" if x is None or pd.isna(x) else fmt.format(x)


def fair_moneyline(home_win: float, home: str, away: str) -> str:
    return f"{away} {american(fair_american(1 - home_win))} / {home} {american(fair_american(home_win))}"


def _has(x) -> bool:
    return x is not None and not pd.isna(x)


def _assumed(r, market: str) -> bool:
    """Whether the logged edge's price was assumed (-110 on a total with no posted price)."""
    if market != "total":
        return False
    return not _has(getattr(r, "over_price" if r.total_edge_side == "over" else "under_price"))


def _run_line_fair(r) -> str:
    """The model's fair odds on both sides of the posted run line, or of its favorite's -1.5."""
    hl = r.home_run_line if _has(r.home_run_line) else (
        -DEFAULT_RUN_LINE if r.model_home_prob >= 0.5 else DEFAULT_RUN_LINE)
    if not (_has(r.model_home_cover_prob) and _has(r.model_away_cover_prob)):
        return ""
    return (f"fair {r.home_team} {hl:+g} {american(fair_american(r.model_home_cover_prob))}, "
            f"{r.away_team} {-hl:+g} {american(fair_american(r.model_away_cover_prob))}")


def edge_cell(r, market: str) -> str:
    """One market's edge for an upcoming game: the pick with its price, EV and the model's
    chance; "no edge" when no priced side clears the bar; otherwise why there is none."""
    pick = getattr(r, f"{market}_edge_pick")
    if _has(pick) and str(pick):
        price = american(getattr(r, f"{market}_edge_price")) + ("*" if _assumed(r, market) else "")
        return (f"{pick} ({price}): EV {getattr(r, f'{market}_edge_ev'):+.1%}, "
                f"model {getattr(r, f'{market}_edge_prob'):.0%}")
    if market == "spread":
        priced = _has(r.home_run_line) and (_has(r.home_run_line_price) or _has(r.away_run_line_price))
        if priced:
            return "no edge"
        fair = _run_line_fair(r)
        reason = "no price yet" if _has(r.home_run_line) else "no line yet"
        return f"{reason}; {fair}" if fair else reason
    if market == "moneyline":
        return "no edge" if _has(r.home_moneyline) or _has(r.away_moneyline) else "no line yet"
    return "no edge" if _has(r.total_line) else "no line yet"


def _lineups(away: str, home: str) -> str:
    def mark(s):
        return "✓" if s == "confirmed" else "proj."
    return f"{mark(away)} / {mark(home)}"


def upcoming_table(rows: pd.DataFrame) -> str:
    lines = [
        "| Time (ET) | Game | Starting pitchers | Predicted score | Win chance | Fair moneyline | Moneyline "
        "| Expected runs | 80% range | Run line | Total: model / line | Extra innings | Lineups "
        "| Run line edge | Moneyline edge | Total edge |",
        "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|",
    ]
    for r in rows.itertuples(index=False):
        fav, p = (r.home_team, r.home_win_prob) if r.home_win_prob >= 0.5 else (r.away_team, r.away_win_prob)
        cover = (f"{r.home_team} -1.5 {r.home_cover_prob:.0%}" if r.home_win_prob >= 0.5
                 else f"{r.away_team} -1.5 {r.away_cover_prob:.0%}")
        total = f"{r.pred_total:.1f}"
        if not pd.isna(r.total_line):
            total += f" / {r.total_line:g}" + (f" (over {r.over_prob:.0%})" if not pd.isna(r.over_prob) else "")
        posted = (f"{r.away_team} {american(r.away_moneyline)} / {r.home_team} {american(r.home_moneyline)}"
                  if _has(r.home_moneyline) or _has(r.away_moneyline) else "–")
        edges = " | ".join(edge_cell(r, m) for m in MARKETS)
        lines.append(
            f"| {_time(r.start)} | {r.away_team} @ {r.home_team} | {r.away_starter} / {r.home_starter} "
            f"| {r.away_team} {int(r.headline_away)}, {r.home_team} {int(r.headline_home)} "
            f"| {fav} {p:.0%} | {fair_moneyline(r.home_win_prob, r.home_team, r.away_team)} | {posted} "
            f"| {r.pred_away:.1f} – {r.pred_home:.1f} "
            f"| {int(r.away_low)}–{int(r.away_high)} / {int(r.home_low)}–{int(r.home_high)} "
            f"| {cover} | {total} | {r.extra_prob:.0%} | {_lineups(r.away_lineup, r.home_lineup)} | {edges} |"
        )
    return "\n".join(lines)


def _log_loss(p, y) -> float:
    p = np.clip(np.asarray(p, dtype=float), 1e-4, 1 - 1e-4)
    return float(-np.mean(y * np.log(p) + (1 - y) * np.log(1 - p)))


def grade(entries: pd.DataFrame) -> pd.DataFrame:
    """Accuracy of logged predictions, next to the market and Elo on the same games."""
    g = entries.dropna(subset=["home_score", "away_score"])
    if g.empty:
        return pd.DataFrame()

    def row(name, d, prob, runs=True):
        y = (d["home_score"] > d["away_score"]).astype(float).to_numpy()
        p = np.asarray(prob, dtype=float)
        out = {"Predictor": name, "Games": len(d), "Log loss": _log_loss(p, y),
               "Brier": float(np.mean((p - y) ** 2)), "Winners": float(np.mean((p >= 0.5) == (y == 1))),
               "Runs MAE": np.nan, "Total MAE": np.nan, "80% range hit": np.nan}
        if runs:
            out["Runs MAE"] = float(np.mean(np.abs(np.concatenate([d["home_score"] - d["pred_home"],
                                                                   d["away_score"] - d["pred_away"]]))))
            out["Total MAE"] = float(np.mean(np.abs(d["home_score"] + d["away_score"] - d["pred_total"])))
            out["80% range hit"] = float(np.mean(np.concatenate([
                d["home_score"].between(d["home_low"], d["home_high"]),
                d["away_score"].between(d["away_low"], d["away_high"])])))
        return out

    rows = [row("Final prediction", g, g["home_win_prob"])]
    lined = g[g["market_home_prob"].notna()]
    if len(lined):
        rows.append(row("Model only (before blending)", g, g["model_home_prob"], runs=False))
    rows.append(row("Elo with starting pitchers", g, g["elo_home_prob"], runs=False))
    if len(lined):
        rows += [row("Final prediction, games with a line", lined, lined["home_win_prob"]),
                 row("Model only, games with a line", lined, lined["model_home_prob"], runs=False)]
        market = row("Betting market (de-vigged moneyline)", lined, lined["market_home_prob"], runs=False)
        has_total = lined["total_line"].notna()
        market["Total MAE"] = float(np.mean(np.abs(
            (lined["home_score"] + lined["away_score"] - lined["total_line"])[has_total]))) if has_total.any() else np.nan
        rows.append(market)
    return pd.DataFrame(rows)


def record_row(label: str, r: dict) -> str:
    roi = f"{r['roi']:+.1%}" if r["bets"] else "–"
    return f"| {label} | {r['bets']} | {r['wins']}-{r['losses']}-{r['pushes']} | {r['units']:+.2f} | {roi} |"


def first_moneyline_moves(entries: pd.DataFrame) -> tuple[int, int]:
    """Of the games with a moneyline edge at the first line seen whose market then moved, how many
    moved toward that edge's side before first pitch (closing line value)."""
    e = entries.dropna(subset=["first_market_home_prob", "market_home_prob", "first_model_home_prob"])
    toward = moved = 0
    for r in e.itertuples(index=False):
        p = r.first_model_home_prob
        pick = best_side([{"side": "home", "price": r.first_home_moneyline, "p_win": p, "p_push": 0.0},
                          {"side": "away", "price": r.first_away_moneyline, "p_win": 1 - p, "p_push": 0.0}])
        move = r.market_home_prob - r.first_market_home_prob
        if pick is None or abs(move) < 0.005:
            continue
        moved += 1
        toward += int((move > 0) == (pick["side"] == "home"))
    return toward, moved


def edge_table(entries: pd.DataFrame) -> str:
    """Record of each market's edges on live predictions, at the price logged before first pitch."""
    live = entries[entries["source"] == "live"]
    lines = ["| Market | Edges | Record (W-L-P) | Units | ROI |", "|---|---|---|---|---|"]
    lines += [record_row(MARKET_NAMES[m], edge_record(live, m)) for m in MARKETS]
    toward, moved = first_moneyline_moves(live)
    lines += ["", f"Moneyline moved toward the model's edge at the first line seen, before first pitch: {toward} of "
              f"{moved} games" + (f" ({toward / moved:.0%})." if moved else ".")]
    return "\n".join(lines)


def metrics_table(df: pd.DataFrame) -> str:
    cols = list(df.columns)
    out = ["| " + " | ".join(cols) + " |", "|" + "---|" * len(cols)]
    for _, r in df.iterrows():
        cells = []
        for c in cols:
            v = r[c]
            if c in ("Winners", "80% range hit"):
                cells.append(_num(v, "{:.1%}"))
            elif c in ("Brier", "Log loss", "Total-runs RPS"):
                cells.append(_num(v, "{:.4f}"))
            elif c == "Games":
                cells.append(str(int(v)))
            elif isinstance(v, (float, np.floating)):
                cells.append(_num(v, "{:.2f}"))
            else:
                cells.append(str(v))
        out.append("| " + " | ".join(cells) + " |")
    return "\n".join(out)


def results_table(rows: pd.DataFrame) -> str:
    lines = ["| Game | Starting pitchers | Predicted | Final | Win chance for winner | Inside 80% ranges |",
             "|---|---|---|---|---|---|"]
    for r in rows.itertuples(index=False):
        home_won = r.home_score > r.away_score
        winner_p = r.home_win_prob if home_won else r.away_win_prob
        inside = (r.home_low <= r.home_score <= r.home_high) and (r.away_low <= r.away_score <= r.away_high)
        extra = f" ({int(r.innings)})" if not pd.isna(r.innings) and r.innings > 9 else ""
        lines.append(
            f"| {r.away_team} @ {r.home_team} | {r.away_starter} / {r.home_starter} "
            f"| {int(r.headline_away)}–{int(r.headline_home)} | {int(r.away_score)}–{int(r.home_score)}{extra} "
            f"| {winner_p:.0%} | {'yes' if inside else 'no'} |"
        )
    return "\n".join(lines)


def ratings_table(table: pd.DataFrame) -> str:
    lines = ["| # | Team | Net | Lineup | Rotation | Bullpen | Fielding and the rest | Starter innings | Elo |",
             "|---|---|---|---|---|---|---|---|---|"]
    for i, r in enumerate(table.itertuples(index=False), 1):
        lines.append(f"| {i} | {r.team} | {r.net:+.2f} | {r.offense:+.2f} | {r.rotation:+.2f} | {r.bullpen:+.2f} "
                     f"| {r.fielding_etc:+.2f} | {r.starter_innings:.1f} | {_num(r.elo, '{:.0f}')} |")
    return "\n".join(lines)


def render(entries: pd.DataFrame, upcoming: pd.DataFrame, ratings: pd.DataFrame, model, weight: float,
           lined_games: int, now, season: int, next_game=None) -> str:
    stamp = pd.Timestamp(now).tz_convert(DISPLAY_TZ).strftime("%a %b %d, %Y %I:%M %p ET")
    parts = [
        "# MLB score predictions",
        "",
        f"Updated {stamp}. Refreshed automatically several times a day during the season; each game's "
        "prediction is locked at first pitch and graded once the final score is in.",
        "",
        "Each game is simulated 10,000 times inning by inning from tonight's starting pitchers, lineups and "
        "bullpens, with the home team skipping the bottom of the ninth when ahead, walk-offs, and the runner on "
        "second in regular-season extra innings. The predicted score is a common final score in which the "
        "likelier winner wins. Baseball is the most luck-driven of the major sports, so read the win chance "
        "and the ranges (80% of simulated outcomes for each team) before the single score.",
        "",
        "Lineups marked ✓ are the posted ones; \"proj.\" is the lineup the team last used against a starter "
        "of the same hand, replaced once the real one posts (usually a few hours before first pitch).",
        "",
        "The fair moneyline is the American odds that match the win chance exactly, with no bookmaker "
        "margin: -150 means risk $150 to win $100, +150 means risk $100 to win $150. A sportsbook's price "
        "is a little worse on both sides because of its cut, so a book only offers value on a team when its "
        "price beats the fair line. The run line is the favorite's chance to win by two or more.",
        "",
        "The edge columns give the expected value of a bet per $1 staked at the posted price, from the "
        "model's own numbers before they are blended with the betting line: its win chance for the "
        "moneyline, and its own simulation's chance of covering the posted run line and of going over or "
        "under the total (a push on a whole-number total returns the stake). A side counts as an edge when "
        f"its EV is {EDGE_MIN_EV:.0%} or more; each market shows its best side, as \"pick (price): EV, the "
        "model's chance\". A total with no posted price is assumed to be -110 on both sides and marked "
        "-110*; run-line and moneyline prices are never assumed, so without one the run line shows the "
        "model's fair odds instead. Treat the edges as an experiment: the model alone was 0.003 log loss "
        "behind Pinnacle's 2016 closing moneyline, and in the backtest its moneyline edges against those "
        "closing prices lost 4.5% per bet (95% range -10.8% to +1.7%) while its total edges broke even, so an "
        "apparent edge against a sharp line is more often the model's error than the market's. Their record "
        "is tracked live below.",
        "",
    ]
    if len(upcoming):
        for date, rows in upcoming.groupby("date", sort=True):
            kinds = sorted(set(rows["game_type"]) - {"R"})
            title = _day(date) + (f" — {', '.join(SERIES[k] for k in kinds if k in SERIES)}" if kinds else "")
            parts += [f"## {title}", "", upcoming_table(rows), ""]
            if any(_assumed(r, "total") for r in rows.itertuples(index=False) if _has(r.total_edge_pick)
                   and str(r.total_edge_pick)):
                parts += ["\\* price not posted; assumed -110.", ""]
    elif next_game is not None and not pd.isna(next_game):
        parts += [f"No games in the next few days. The next scheduled game is on {_day(next_game)}; predictions "
                  "resume a couple of days before it.", ""]
    else:
        parts += ["No games on the schedule yet. Predictions resume once next season's schedule is out "
                  "(MLB publishes it in the summer, and play starts in late March).", ""]

    season_log = entries[entries["season"] == season]
    graded = season_log.dropna(subset=["home_score", "away_score"])
    parts += [f"## How the {season} predictions have done", ""]
    if len(graded):
        parts += [metrics_table(grade(season_log)), "",
                  "Log loss and Brier score the win chances (lower is better; a coin flip scores 0.693 and "
                  "0.250, and Pinnacle's closing moneyline scored 0.673 in 2016). Baseball edges are thin, so "
                  "differences in the third decimal matter, and only over hundreds of games. Runs MAE is the "
                  "average miss on each team's runs.", ""]
        reg = graded[graded["game_type"] == "R"]
        if len(reg) and reg["innings"].notna().any():
            parts += [f"Extra innings: predicted in {reg['extra_prob'].mean():.1%} of regular-season games, "
                      f"happened in {(reg['innings'] > 9).mean():.1%}.", ""]
        backfilled = int((graded["source"] == "backfill").sum())
        if backfilled:
            parts += [f"{backfilled} of these games were played before the predictor went live (or while it "
                      "was not running). They are backfilled walk-forward (each day predicted from earlier days "
                      "only, with the run model fitted on earlier seasons) with the actual lineups and starting "
                      "pitchers and no betting line. Every other game is graded on the prediction logged before "
                      "first pitch.", ""]
        if graded["market_home_prob"].notna().any():
            parts += ["### Betting edges", "", edge_table(season_log), "",
                      "One unit on each edge at the price logged with the last prediction before first pitch "
                      "(live predictions only; ROI is units per bet). The market moving toward the model's side "
                      "(closing line value) is the quickest sign that it knows something the market doesn't yet.",
                      ""]
        last_day = graded["date"].max()
        parts += [f"### Results, {_day(last_day)}", "", results_table(graded[graded["date"] == last_day]), ""]
    else:
        parts += ["Nothing graded yet; results appear here after the first predicted games finish.", ""]

    if len(ratings):
        parts += ["## Power ratings", "",
                  "Runs per game better than an average team against an average opponent at a neutral park, "
                  "from the run model. The lineup is the team's latest one against average pitching; the "
                  "rotation is its last five starters, weighted by how deep they go, and the bullpen its "
                  "relievers by recent use; \"fielding and the rest\" is what the team's runs allowed say "
                  "beyond its pitchers' own numbers. Positive is better on every side of the ball.", "",
                  ratings_table(ratings), ""]

    c = model.coef
    blend = (f"{1 - weight:.0%} on the betting line wherever there is one (fitted on {lined_games} logged "
             "games, shrunk toward the 2016 backtest value)" if lined_games else
             f"{1 - weight:.0%} on the betting line wherever there is one (the value fitted on Pinnacle's 2016 "
             "closing lines, until enough logged games with lines exist to refit it)")
    seasons = model.fit_seasons
    parts += [
        "## Current model fit", "",
        f"- Fitted on {model.fit_games} games from {seasons[0]} to {seasons[-1]}." if seasons else "",
        f"- Home field: {math.exp(c.get('h', 0.0)) - 1:+.1%} runs for the home team relative to the visitor.",
        f"- Park: each 10% of park run factor moves runs by {1.1 ** c.get('log_pf', 1.0) - 1:+.1%}.",
        f"- Weather: {math.exp(c.get('temp_x', 0.0)) - 1:+.1%} runs per 10°F above 70°F, "
        f"{math.exp(c.get('wind_x', 0.0)) - 1:+.1%} per 10 mph of wind blowing out (open-air parks).",
        f"- Matchups: a lineup's edge over the starter counts {c.get('x_sp', 1.0):.2f} times its face value "
        f"and over the bullpen {c.get('x_bp', 1.0):.2f} times.",
        f"- Blend: {blend}.",
        f"- Simulator: games share a hot-or-cold factor with spread 1/√{model.sim.frailty:.0f}, and "
        f"{model.sim.walkoff_hr:.0%} of walk-offs are home runs that count in full.",
        "",
    ]
    return "\n".join(p for p in parts if p is not None)


def backtest_edge_table(edges: dict) -> str:
    """Edge records by market with a range on ROI; a market without prices says so."""
    lines = ["| Market | Edges | Record (W-L-P) | Units | ROI | 95% range on ROI |", "|---|---|---|---|---|---|"]
    for label, r in edges.items():
        if r is None:
            lines.append(f"| {label} | no historical prices | | | | |")
            continue
        span = f"{r['roi_low']:+.1%} to {r['roi_high']:+.1%}" if r["bets"] else "–"
        lines.append(record_row(label, r) + f" {span} |")
    return "\n".join(lines)


def render_backtest(scores: dict, checks: dict, bootstrap: dict, seasons: tuple, market: dict | None,
                    lineups: dict | None) -> str:
    parts = [
        "# Walk-forward backtest",
        "",
        f"Seasons {seasons[0]} to {seasons[-1]}, postseason included. Every game is predicted using only earlier "
        "days' results (player and team ratings, with park factors from earlier seasons), with the run model and "
        "simulator fitted on the three seasons before. Lineups and starting pitchers are the actual ones, as a "
        "game-day run knows them once lineups post; weather is the recorded game-time weather. Baselines are "
        "scored on the same games.",
        "",
    ]
    for label, df in scores.items():
        df = df.rename(columns={
            "predictor": "Predictor", "games": "Games", "log_loss": "Log loss", "brier": "Brier",
            "winner_pct": "Winners", "runs_mae": "Runs MAE", "total_mae": "Total MAE",
        })
        parts += [f"## {label}", "", metrics_table(df), ""]
    parts += ["## Is the difference real?", "",
              "Paired bootstrap of the per-game log loss (negative favors the first).", "",
              "| Comparison | Mean difference | 95% interval |", "|---|---|---|"]
    for name, (mean, lo, hi) in bootstrap.items():
        parts.append(f"| {name} | {mean:+.4f} | {lo:+.4f} to {hi:+.4f} |")
    if market:
        l = market["losses"]
        parts += ["", "## Against the betting market, 2016", "",
                  f"Pinnacle's complete 2016 line history ({market['games']} games), de-vigged. The blend backs "
                  "each team's expected runs out of the closing moneyline and total through the simulator and "
                  f"mixes them with the model's on the log scale, {market['weight']:.0%} model; that weight, fitted "
                  "on these games, is where the live predictor's blend starts.", "",
                  "| Predictor | Log loss | Brier | Total MAE |", "|---|---|---|---|",
                  f"| Model + simulator | {l['model'].mean():.4f} | {market['brier']['model']:.4f} "
                  f"| {market['total_mae']['model']:.2f} |",
                  f"| Elo with starting pitchers | {l['elo'].mean():.4f} | – | – |",
                  f"| Opening line | {l['open'].mean():.4f} | – | – |",
                  f"| Closing line | {l['close'].mean():.4f} | {market['brier']['close']:.4f} "
                  f"| {market['total_mae']['close']:.2f} |",
                  f"| Model blended with the closing line | {l['blend'].mean():.4f} | {market['brier']['blend']:.4f} "
                  f"| {market['total_mae']['blend']:.2f} |", "",
                  "| Comparison | Mean difference | 95% interval |", "|---|---|---|"]
        for name, (mean, lo, hi) in market["bootstrap"].items():
            parts.append(f"| {name} | {mean:+.4f} | {lo:+.4f} to {hi:+.4f} |")
    calib = checks["calibration"]
    parts += ["", "## Win-probability calibration", "",
              "| Predicted home win | Games | Mean predicted | Actual |", "|---|---|---|---|"]
    for idx, r in calib.iterrows():
        parts.append(f"| {idx} | {int(r.games)} | {r.predicted:.1%} | {r.actual:.1%} |")
    c = checks
    parts += ["", "## Score distribution checks", "",
              "| Check | Simulator | Actual |", "|---|---|---|",
              f"| Runs per game, both teams | {c['total_predicted']:.2f} | {c['total_actual']:.2f} |",
              f"| Team shut out | {c['shutout_predicted']:.1%} | {c['shutout_actual']:.1%} |",
              f"| Decided by one run | {c['one_run_predicted']:.1%} | {c['one_run_actual']:.1%} |",
              f"| Extra innings (regular season) | {c['extra_predicted']:.1%} | {c['extra_actual']:.1%} |",
              f"| Home team skips the bottom of the ninth | {c['skip_predicted']:.1%} | {c['skip_actual']:.1%} |",
              f"| Walk-off win | {c['walkoff_predicted']:.1%} | {c['walkoff_actual']:.1%} |",
              f"| Home team wins by 2+ | {c['home_cover_predicted']:.1%} | {c['home_cover_actual']:.1%} |",
              "",
              "Each team's runs scored against its full simulated distribution (ranked probability score, lower "
              "is better), next to a plain Poisson and a negative binomial (variance 2.26 times the mean, the "
              "league-wide ratio) with the same expected runs:", "",
              "| Simulator | Negative binomial | Poisson |", "|---|---|---|",
              f"| {c['rps_sim']:.4f} | {c['rps_nbinom']:.4f} | {c['rps_poisson']:.4f} |", "",
              f"- 80% ranges contained the team's actual runs {c['range_coverage']:.1%} of the time "
              "(runs are whole numbers, so a range covers a little more than 80%).",
              f"- Headline score exactly right: {c['headline_exact']:.1%} of games.", ""]
    if market and market.get("edges"):
        parts += ["## Betting edges against Pinnacle, 2016", "",
                  "The same edges as the predictions page, walk-forward: the model's own chances before any "
                  "blending (its win chance, and its simulation's chance of going over or under the total, with "
                  f"pushes on whole-number totals), against Pinnacle's posted prices; an edge needs EV of "
                  f"{EDGE_MIN_EV:.0%} or more per $1, and each game bets the market's best side for one unit. "
                  "The ROI range is a 95% bootstrap interval over the bets.", "",
                  backtest_edge_table(market["edges"]), ""]
    if lineups:
        mean, lo, hi = lineups["bootstrap"]
        parts += ["## Posted lineups against projected ones", "",
                  f"On {lineups['games']} games, log loss with the actual lineups is {lineups['known']:.4f}; with "
                  "each team's lineup projected from its last game against a starter of the same hand (what a "
                  f"morning run uses) it is {lineups['projected']:.4f} (difference {mean:+.4f}, 95% interval "
                  f"{lo:+.4f} to {hi:+.4f}).", ""]
    return "\n".join(parts)
