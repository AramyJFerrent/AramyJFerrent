# NBA Score Predictor

Predicts the final score of every NBA game, with win probabilities, the
chance of overtime, the spread and total, the players each team will be
missing and a realistic range for each team, and keeps itself current
through the season. A scheduled GitHub Action pulls the newest box scores,
play-by-play, lines, injury reports and rosters several times a day, refits
the model, re-predicts the next two days of games, and grades each
prediction once the game is final.

**Latest predictions: [`predictions/README.md`](predictions/README.md)**
· Backtest: [`predictions/backtest.md`](predictions/backtest.md)

The design follows the *NBA Score Prediction: Techniques Report*: it rates
every player from the lineups on the floor, projects who will play tonight
and for how many minutes from the injury report, turns that lineup into each
team's expected possessions and points per possession, blends the result
with the betting line, and simulates the game, overtime included, to get
each team's score distribution.

## How it stays up to date

`.github/workflows/nba-score-predictor.yml` runs `python -m nbapredictor update`
from October through June, timed around the injury report (statuses are due
by 5 PM local the day before a game and between 11 AM and 1 PM on game day):

| When (ET) | Why |
|---|---|
| Every morning, about 9:30 AM | Last night's box scores and play-by-play, new ratings |
| About 1:45 PM | After the game-day injury report |
| About 5:30 PM | Updated statuses and lines before the 7 PM games |
| About 7:15 PM | Late scratches before the 7:30 and 8 PM games |
| About 9 PM | Before the late West Coast games |

Each run:

1. Downloads this season's schedule, box scores and play-by-play and
   rebuilds this season's summaries in `data/games/`: every lineup stint,
   with garbage time flagged, and every player's minutes.
2. Refits the efficiency and pace maps, the market blend and the score
   simulator on the last four seasons plus every game played so far this
   season.
3. Reads ESPN's injury report, current rosters and lines for the next two
   game days, and projects each team's lineup and minutes.
4. Predicts every game in that window that has not started, checks the
   spread, moneyline and total for a betting edge, and writes the
   predictions to `predictions/log.csv`, replacing earlier ones for the same
   game. A game's prediction stops changing at tip-off, so the logged one is
   always the last made before the game, with the injury news, line, prices
   and edges it was made against.
5. Fills in final scores and grades the season so far against the betting
   line and Elo, and grades the edges.
6. Commits the results back to the repo (only when something changed).

Nothing needs to be done between seasons. A weekly off-season run picks up
the finished season's last data and next season's schedule, which comes out
in August, and in August the predictor rolls over to the new season: the
finished season's files are gzipped and stay in `data/games/` as history.
If the predictor starts mid-season (or misses days), it backfills the games
already played with walk-forward predictions, labeled as such, so the season
grading starts populated. It went live on the eve of the 2026-27 opener.

**To turn the schedule on**, merge this folder and the workflow into the
repository's default branch (GitHub only runs scheduled workflows from there),
make sure Actions are enabled, and optionally start a first run from the
Actions tab with **Run workflow**.

## How it works

| Stage | What it does | Code |
|---|---|---|
| Data | ESPN schedules, box scores and play-by-play since 2007-08, compiled by sportsdataverse, reduced to one row per game, team-game and player-game (healthy scratches and injury absences included), plus every **stint**: a stretch of a game with the same ten players on the floor, rebuilt from the substitutions. Changes between quarters are not logged, so each period's opening five are inferred from who appears in it. Reconstructed minutes match the box score within a minute for 99.97% of player-games, and stint points add up to the final score in 99.9% of games. Possessions are counted from the play-by-play (they agree with the box-score estimate within 1%). | `data.py` |
| Garbage time | Cleaning the Glass's rule: fourth-quarter stints from the moment the lead reaches 25 with 9 to 12 minutes left, 20 with 6 to 9, or 10 under 6, with two or fewer starters on the floor between the two teams, and only if the game stays that lopsided to the end. About 3.5% of possessions. It is left out of every rating. | `data.py` |
| Player ratings | Regularized adjusted plus-minus on the stints: each side's points per 100 possessions in a stint is the league level plus home court plus the five offensive ratings plus the five opposing defensive ratings, fitted by ridge regression weighted by possessions. Each player is pulled toward a prior worth 3,000 possessions on offense and 4,000 on defense: 85% of last season's rating, or a newcomer value of −6 net points per 100 for a player with no rating yet. Stints have a 365-day half-life, so a player's rating moves through the season without forgetting his last one. | `players.py` |
| Minutes and availability | Each player's minutes are projected from his recent games for any team (1.5-game half-life), both minutes when he plays and expected minutes counting healthy scratches as zero. A team's lineup strength is the minutes-weighted sum of its players' ratings, with minutes rescaled to 240 and no one above 42; minutes left by an absent player go to the others in proportion to how far each is below 42, so the bench absorbs most of them. Live, the candidates are ESPN's current roster (falling back to recent box scores, then the preseason roster), and the injury report turns each status into a chance of playing: out 0, doubtful 15%, questionable 55%, day-to-day 70%, probable 95%. A questionable star counts with about half his minutes, which weighs the two scenarios by how likely each is. | `players.py`, `availability.py` |
| Team ratings | Ridge ratings of each offense's and defense's points per 100 possessions (garbage time removed, opponent-adjusted, 30-day half-life) and of pace (15-day half-life, since pace changes faster than quality), each pulled toward 60% of last season's rating | `ratings.py` |
| Points map | Points per 100 possessions for each offense from both teams' lineup strength and efficiency ratings, home court, back-to-backs and playoffs, on top of the league's current level; possessions from both teams' pace ratings. Expected points are pace times efficiency. Refitted on the last four seasons every run. | `model.py` |
| Market blend | `final = w × model + (1 − w) × line`, separately for the margin and the total, with `w` fitted on past closing lines | `model.py` |
| Simulator | 10,000 games per matchup. Each team's regulation points come from a bivariate normal around its expected points, with the spread and correlation fitted so simulated margins and totals scatter like real ones (about 11 points per team, correlation about 0.23 in recent seasons) and growing with the expected total. Real games are tied after 48 minutes twice as often as a smooth distribution says (the trailing team plays for the tie) and end 1-4 points apart less often, so each simulated game is weighted by its regulation margin to match; tied games play five-minute overtimes at each team's regulation scoring rate until one leads. | `simulate.py` |
| Elo | FiveThirtyEight-style margin-of-victory Elo, the baseline | `elo.py` |
| Backtest | Walk-forward by day over 2015-16 to 2025-26, scored next to the closing line, team ratings alone and Elo | `backtest.py` |

Ratings knobs were tuned on 2012-13 to 2015-16 (`python -m nbapredictor tune`).
Everything else is refitted on every run.

## Backtest, 2015-16 to 2025-26

Every game is predicted from earlier days of its season plus the preseason
priors, with the points map, blend and simulator fitted on the four seasons
before. Who played is known (what the final injury report says at tip-off),
but minutes are always projected from earlier games, never taken from the
box score. All 13,332 games have an archived closing line; a coin flip scores
0.693 log loss and 0.250 Brier.

| Predictor | Margin MAE | Total MAE | Team-points MAE | Log loss | Brier | Winners |
|---|---|---|---|---|---|---|
| Final (model + market + simulator) | 10.12 | 14.22 | 8.82 | 0.600 | 0.207 | 67.5% |
| Model only | 10.29 | 14.47 | 8.95 | 0.607 | 0.210 | 67.0% |
| Team ratings only | 10.51 | 14.59 | 9.07 | 0.623 | 0.217 | 65.3% |
| Elo | 10.53 | 15.84 | 9.58 | 0.624 | 0.217 | 65.0% |
| Closing line | 10.11 | 14.20 | 8.81 | 0.600 | 0.207 | 67.7% |

- The player layer is where the model's skill comes from, as the report
  predicts. Rating the players who will actually be on the floor cuts the
  margin error by 0.23 points against team efficiency ratings alone (95%
  interval 0.18 to 0.27). Once lineup strength is in, the team efficiency
  ratings keep only a small weight (about 0.15, against about 0.75 for the
  lineup ratings): the players already carry most of what they know.
- On the report's own test seasons (2020-21 on), team ratings alone miss by
  10.97 against the closing line's 10.50, almost exactly the report's 11.0
  against 10.5; the full model closes most of that gap (10.69).
- On its own the model trails the closing line by 0.18 points a game (95%
  interval 0.14 to 0.22). The final prediction tracks the line, as the fitted
  blend puts most of the weight on it, and ends up 0.016 behind it on the
  margin and 0.02 on the total: the closing line already knows what the
  model knows, injuries included.
- Win probabilities are well calibrated: games given 60–70% were won 65.7%
  of the time (predicted 65.0%), and 40–50% games 45.3% (predicted 44.5%).
  80% ranges contain each team's points 81.4% of the time, the margin 80.7%
  and the total 81.3%. The simulator sends 5.1% of regular-season games to
  overtime, against 5.4% in reality.
- Knowing who plays matters: assuming each team's previous lineup instead
  (a morning run before injury news) raises the model's margin error by
  0.07 points (95% interval 0.04 to 0.10). That is why the schedule reruns
  around every injury-report deadline.
- Things that did not earn a place, tested on the same games: travel distance
  and time zones crossed, and rest beyond the back-to-back flag.

Full tables, calibration buckets and bootstrap intervals are in
[`predictions/backtest.md`](predictions/backtest.md). The archived lines for
2011-12 to 2021-22 come with opening numbers, and the "closing" spreads and
totals in the other archive turned out to be those opening numbers for
those seasons (they match in 99% of games), so the closing benchmark uses
sportsbookreview's own closing lines there: 10.11 points of margin error
from 2015-16 on, against 10.2 in the report.

## Betting edges

For every game the predictions page checks each side of three markets, the
spread, the moneyline and the total, for expected value: the profit per $1
bet at the posted price,

    EV = P(win) × (decimal odds − 1) − P(lose)

where a push returns the stake. The chances come from the model alone,
before it is blended with the line: the model-only simulation that gives
its own win chance also gives its chance of covering, landing exactly on
the spread, going over and landing on the total. The best side is an edge
when its EV is 3% or more (`EDGE_MIN_EV` in `nbapredictor/edges.py`), and
the page shows it as `NYK -4.5 (-110): EV +5.0%, model 55%`, or "no edge",
or "no line yet".

Prices come from ESPN's odds: both moneylines and the price of each side of
the spread and the total. When a spread or total price is missing it is
assumed to be −110 and marked `-110*`; a moneyline is never assumed. The
edge of each market is logged with every prediction, so the one that counts
is the last before tip-off, and it is graded once the game is final: 1 unit
flat, at the logged price. The page keeps a season record per market
(edges, W-L-P, units, ROI) and how often the spread moved toward the
model's first spread edge before tip-off.

The backtest (`python -m nbapredictor backtest`) computes the same edges
walk-forward against the archived closing lines (closing moneylines;
spreads and totals at an assumed −110, since the archives have no prices
for them) and against opening spreads and totals, and writes the record of
each market with a 95% bootstrap range on its ROI to
[`predictions/backtest.md`](predictions/backtest.md).

## Can it beat the betting line?

Before the edges were based on expected value, the predictor picked a side
whenever the model's own spread (before blending) and the line differed by a
point or more. The walk-forward test of those picks, against break-even of
52.4% at standard −110 odds:

| Picks against | Record (W-L-P) | Cover rate | 95% range | Line then moved toward the pick |
|---|---|---|---|---|
| Opening line, 2015-16 to 2021-22, assuming each team's previous lineup | 2926-2743-94 | 51.6% | 50.3%–52.9% | 59.0% of 4,860 moves |
| Opening line, same seasons, knowing who played | 2984-2774-97 | 51.8% | 50.5%–53.1% | 68.0% of 4,964 moves |
| Closing line, same games | 2811-2862-97 | 49.6% | 48.2%–50.9% | – |
| Closing line, 2015-16 to 2025-26 | 4447-4465-131 | 49.9% | 48.9%–50.9% | – |

What this means:

- Against opening lines the model has a small, real edge: its picks beat
  the opener more often than not even without any injury news (the first
  row assumes each team's previous lineup, which is all a morning run
  knows), and the line then moved toward the pick 59% of the time. It is
  still below break-even, and the 95% range includes it, so it is not a
  proven money-maker.
- Against closing lines there is no edge at all: 49.9%. By tip-off the
  market has priced in what the model knows, injuries included.

So the honest answer is the same as the NFL predictor's: better than the
line early, by a margin too thin to count on, and not better than the
closing line. The predictions page now tracks the expected-value edges
live, with how often the spread moves toward the model's first spread edge,
so this keeps being tested on games the model has never seen.

## Running it yourself

Python 3.11 or newer.

```bash
cd NBAScorePredictor
pip install -r requirements.txt

python -m nbapredictor update              # refresh and predict the next two game days
python -m nbapredictor update --days 1 --no-espn
python -m nbapredictor ratings             # current team ratings and the top players
python -m nbapredictor check               # read ESPN's lines, injuries and rosters once and print them
python -m nbapredictor backtest            # walk-forward 2015-16 to 2025-26, writes predictions/backtest.md
python -m nbapredictor tune --save         # re-tune the ratings engines on 2012-13 to 2015-16
python -m nbapredictor summarize --all     # rebuild every season's summaries from the raw data
python -m nbapredictor lines               # rebuild data/lines.csv from the line archives
python -m pytest -q tests
```

Seasons are named by the year they end on the command line (2027 is 2026-27).
Downloads are cached in `.cache/` (ignored by git).

## Outputs

| File | Contents |
|---|---|
| `predictions/README.md` | Upcoming games with missing players and betting edges, season grading, edge record, latest results, power ratings, top players |
| `predictions/latest.json` | The same upcoming predictions as JSON |
| `predictions/log.csv` | Every prediction (last one before tip-off), with the line, prices, model-only chances against the line, betting edges and injury news it was made against, and the final score once known |
| `predictions/ratings.csv` | Team power ratings in points per 100 possessions, with today's injury cost |
| `predictions/players.csv` | The top-rated players and their expected minutes |
| `predictions/model.json` | The fitted coefficients, blend weights and simulator settings |
| `data/games/` | Per-season games, team-games, player-games and stints (finished seasons gzipped) |
| `data/lines.csv` | Archived opening and closing lines, 2007-08 to January 2026 |
| `data/players.csv`, `data/arenas.csv` | Player names; arena locations for travel |

## Not modeled yet

- Box-score priors for player ratings. A rookie starts from a flat
  below-average prior and earns his rating on the floor; a box-score prior
  (the way EPM and DARKO seed theirs) would let young players' ratings settle
  faster.
- Shot quality. Hot and cold shooting is regressed only through the ridge
  priors, not through shot-quality or attempt-rate measures.
- Season stage: tanking, locked seeds and resting stars reach the prediction
  only through the injury report and the line. Playoff rotations tighten,
  but the model knows the playoffs only as a lower-scoring, slower setting.
- The official NBA injury report itself. Statuses come from ESPN's injury
  feed, which follows it; a status posted minutes before tip-off can miss
  the last scheduled run.
- Live, in-game predictions.

## Data

Schedules, box scores, play-by-play and season rosters from ESPN, compiled
daily by [sportsdataverse](https://github.com/sportsdataverse/hoopR-nba-data)
(hoopR). Lines, injury reports and current rosters from ESPN's public site
API. Historical lines from the
[sportsbookreview.com archive](https://github.com/flancast90/sportsbookreview-scraper)
and the [NBA-Machine-Learning-Sports-Betting](https://github.com/kyleskom/NBA-Machine-Learning-Sports-Betting)
repository. Garbage time as defined by
[Cleaning the Glass](https://cleaningtheglass.com/stats/guide/garbage_time).
