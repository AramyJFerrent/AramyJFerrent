"""Markdown pages for the predictions folder."""

from __future__ import annotations

import math

import numpy as np
import pandas as pd

from .config import DISPLAY_TZ

# Smallest gap between the model's win chance and the market's that counts as a pick.
PICK_MIN_EDGE = 0.03
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


def american_odds(p: float) -> int:
    """Fair (no-vig) American moneyline for win probability ``p``, rounded to 5."""
    p = min(max(p, 0.01), 0.99)
    raw = -100.0 * p / (1.0 - p) if p > 0.5 else 100.0 * (1.0 - p) / p
    return int(5 * math.floor(raw / 5 + 0.5))


def _moneyline(odds) -> str:
    if odds is None or pd.isna(odds):
        return "–"
    odds = int(round(odds))
    return f"+{odds}" if odds > 0 else str(odds)


def fair_moneyline(home_win: float, home: str, away: str) -> str:
    return f"{away} {_moneyline(american_odds(1 - home_win))} / {home} {_moneyline(american_odds(home_win))}"


def payout(price: float) -> float:
    """Profit on a one-unit winning bet at American odds ``price``."""
    return price / 100.0 if price > 0 else 100.0 / -price


def model_pick(model_prob: float, market_prob: float, home_ml: float, away_ml: float,
               home: str, away: str) -> str:
    """The side the model's own win chance favors against the de-vigged market, with the gap."""
    if pd.isna(market_prob) or pd.isna(model_prob):
        return "–"
    edge = model_prob - market_prob
    if abs(edge) < PICK_MIN_EDGE:
        return "no edge"
    team, price = (home, home_ml) if edge > 0 else (away, away_ml)
    return f"{team} {_moneyline(price)} ({abs(edge):.0%})"


def _lineups(away: str, home: str) -> str:
    def mark(s):
        return "✓" if s == "confirmed" else "proj."
    return f"{mark(away)} / {mark(home)}"


def upcoming_table(rows: pd.DataFrame) -> str:
    lines = [
        "| Time (ET) | Game | Starting pitchers | Predicted score | Win chance | Fair moneyline | Expected runs "
        "| 80% range | Run line | Total: model / line | Extra innings | Lineups | Moneyline / model pick (edge) |",
        "|---|---|---|---|---|---|---|---|---|---|---|---|---|",
    ]
    for r in rows.itertuples(index=False):
        fav, p = (r.home_team, r.home_win_prob) if r.home_win_prob >= 0.5 else (r.away_team, r.away_win_prob)
        cover = (f"{r.home_team} -1.5 {r.home_cover_prob:.0%}" if r.home_win_prob >= 0.5
                 else f"{r.away_team} -1.5 {r.away_cover_prob:.0%}")
        total = f"{r.pred_total:.1f}"
        if not pd.isna(r.total_line):
            total += f" / {r.total_line:g}" + (f" (over {r.over_prob:.0%})" if not pd.isna(r.over_prob) else "")
        market = (f"{r.away_team} {_moneyline(r.away_moneyline)} / {r.home_team} {_moneyline(r.home_moneyline)}; "
                  + model_pick(r.model_home_prob, r.market_home_prob, r.home_moneyline, r.away_moneyline,
                               r.home_team, r.away_team)) if not pd.isna(r.home_moneyline) else "no line yet"
        lines.append(
            f"| {_time(r.start)} | {r.away_team} @ {r.home_team} | {r.away_starter} / {r.home_starter} "
            f"| {r.away_team} {int(r.headline_away)}, {r.home_team} {int(r.headline_home)} "
            f"| {fav} {p:.0%} | {fair_moneyline(r.home_win_prob, r.home_team, r.away_team)} "
            f"| {r.pred_away:.1f} – {r.pred_home:.1f} "
            f"| {int(r.away_low)}–{int(r.away_high)} / {int(r.home_low)}–{int(r.home_high)} "
            f"| {cover} | {total} | {r.extra_prob:.0%} | {_lineups(r.away_lineup, r.home_lineup)} | {market} |"
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


def pick_record(d: pd.DataFrame, model_col: str, market_col: str, home_ml: str, away_ml: str) -> dict:
    """Moneyline record and units won betting one unit on each model pick."""
    d = d.dropna(subset=[model_col, market_col, home_ml, away_ml])
    edge = d[model_col] - d[market_col]
    picked = d[edge.abs() >= PICK_MIN_EDGE]
    edge = edge[picked.index]
    home_won = picked["home_score"] > picked["away_score"]
    won = np.where(edge > 0, home_won, ~home_won)
    price = np.where(edge > 0, picked[home_ml], picked[away_ml])
    units = float(np.sum(np.where(won, [payout(p) for p in price], -1.0))) if len(picked) else 0.0
    return {"bets": len(picked), "wins": int(np.sum(won)), "losses": int(len(picked) - np.sum(won)),
            "units": units, "roi": units / len(picked) if len(picked) else float("nan")}


def pick_table(entries: pd.DataFrame) -> str:
    g = entries.dropna(subset=["home_score", "away_score"])
    first = pick_record(g, "first_model_home_prob", "first_market_home_prob", "first_home_moneyline",
                        "first_away_moneyline")
    last = pick_record(g, "model_home_prob", "market_home_prob", "home_moneyline", "away_moneyline")
    lines = ["| Picks against | Bets | Record (W-L) | Units won | Return per bet |", "|---|---|---|---|---|"]
    for label, r in (("First line seen", first), ("Last line before first pitch", last)):
        roi = f"{r['roi']:+.1%}" if r["bets"] else "–"
        lines.append(f"| {label} | {r['bets']} | {r['wins']}-{r['losses']} | {r['units']:+.2f} | {roi} |")
    e = entries.dropna(subset=["first_market_home_prob", "market_home_prob", "first_model_home_prob"])
    edge = e["first_model_home_prob"] - e["first_market_home_prob"]
    move = e["market_home_prob"] - e["first_market_home_prob"]
    moved = (edge.abs() >= PICK_MIN_EDGE) & (move.abs() >= 0.005)
    toward = int((np.sign(move[moved]) == np.sign(edge[moved])).sum())
    lines += ["", f"Market moved toward the model's first pick before first pitch: {toward} of {int(moved.sum())} games"
              + (f" ({toward / moved.sum():.0%})." if moved.sum() else ".")]
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
        "The model pick is the side where the model's own win chance (before blending with the market) beats "
        f"the de-vigged moneyline by {PICK_MIN_EDGE:.0%} or more. Treat it as an experiment: its record is "
        "tracked live below.",
        "",
    ]
    if len(upcoming):
        for date, rows in upcoming.groupby("date", sort=True):
            kinds = sorted(set(rows["game_type"]) - {"R"})
            title = _day(date) + (f" — {', '.join(SERIES[k] for k in kinds if k in SERIES)}" if kinds else "")
            parts += [f"## {title}", "", upcoming_table(rows), ""]
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
            parts += ["### Model picks against the moneyline", "", pick_table(season_log), "",
                      "One unit on each pick at the logged price. The market moving toward the model's pick "
                      "(closing line value) is the quickest sign that it knows something the market doesn't yet.", ""]
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
    if lineups:
        mean, lo, hi = lineups["bootstrap"]
        parts += ["## Posted lineups against projected ones", "",
                  f"On {lineups['games']} games, log loss with the actual lineups is {lineups['known']:.4f}; with "
                  "each team's lineup projected from its last game against a starter of the same hand (what a "
                  f"morning run uses) it is {lineups['projected']:.4f} (difference {mean:+.4f}, 95% interval "
                  f"{lo:+.4f} to {hi:+.4f}).", ""]
    return "\n".join(parts)
