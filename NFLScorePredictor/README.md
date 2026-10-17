# NFL Score Predictor

Predicts the final score of every NFL game, with win probabilities and a
realistic range for each team, and keeps itself current through the season.
A scheduled GitHub Action pulls new results, lines and play-by-play every day,
refits the model, re-predicts the upcoming games, and grades each prediction
once the game is final.

**Latest predictions: [`predictions/README.md`](predictions/README.md)**
· Backtest: [`predictions/backtest.md`](predictions/backtest.md)

The design follows the *NFL Score Prediction: Techniques Report*: it models
each team's expected points from opponent-adjusted efficiency, blends with the
betting market, and turns expected points into a full score distribution.

## How it stays up to date

`.github/workflows/nfl-score-predictor.yml` runs `python -m nflpredictor update`:

| When (ET) | Why |
|---|---|
| Every morning, about 9 AM | New final scores, updated lines, overnight play-by-play |
| Sunday about noon | Inactives, final lines and weather before the 1 PM games |
| Sunday, Monday and Thursday about 7 PM | Same, before the night games |

Each run:

1. Downloads the nflverse schedule (scores, current lines, projected starting
   QBs) and this season's play-by-play, and rebuilds this season's efficiency
   summary in `data/epa/`.
2. Refits the ratings-to-points map, home field, rest and QB effects, the
   market blend weight, the wind adjustment and the score simulator on the last
   six seasons plus every game played so far this season.
3. Predicts every game in the next two weeks that has not kicked off.
4. Writes the predictions to `predictions/log.csv`, replacing earlier ones for
   the same game. A game's prediction stops changing at kickoff, so the logged
   one is always the last made before the game.
5. Fills in final scores and grades the season so far against the betting line.
6. Commits the results back to the repo (only when something besides a
   timestamp changed).

Nothing needs to be done between seasons. In March the predictor rolls over to
the new season, the finished season's summary stays in `data/epa/` as history,
and predictions resume once the schedule is out. If it starts mid-season (as it
did in Week 6 of 2026) it backfills the weeks already played with walk-forward
predictions, labeled as such, so the season grading starts populated.

**To turn the schedule on**, merge this folder and the workflow into the
repository's default branch (GitHub only runs scheduled workflows from there),
make sure Actions are enabled, and optionally start a first run from the
Actions tab with **Run workflow**.

## How it works

| Stage | What it does | Code |
|---|---|---|
| Data | nflverse schedules and play-by-play since 2009, reduced to one row per team-game and QB-game | `data.py` |
| Ratings engine | Ridge regression of each offense's EPA per play on offense, opposing defense and home edge. Lopsided-score plays are down-weighted and lost fumbles count half. Each team is pulled toward a preseason prior (60% of last year's offense, 45% of its defense) with the strength of 600 offensive and 1,200 defensive plays, so the prior carries the early weeks and fades by midseason. | `ratings.py` |
| Special teams | Net EPA per game on kickoffs, punts, field goals and extra points, rated the same way but pulled much harder toward the prior because it is noisy week to week. It is the one extra rating that held up out of sample: the market underweights it. | `ratings.py` |
| Quarterbacks | Each QB's EPA per dropback above league average, shrunk toward a replacement-level prior. When the projected starter differs from the QBs behind the team's rating, the offense is adjusted. | `qb.py` |
| Elo | Margin-of-victory Elo, kept as the sanity-check baseline | `elo.py` |
| Points map | Linear map from ratings to each team's points on top of the current league scoring level, with special teams, home field (smaller in division games), rest and QB terms | `model.py` |
| Market blend | `final = w × model + (1 − w) × line` for margin and total, with `w` fitted on recent seasons | `model.py` |
| Weather | Kickoff wind forecast (Open-Meteo) for open-air games lowers the total by the amount the market has historically missed | `weather.py`, `model.py` |
| Score simulator | 10,000 simulated games per matchup. Each team's scoring chances end in a touchdown (then a kick or two-point try), a field goal or nothing, with overtime and ties. Dispersion is calibrated to real prediction errors and key margins (3, 7, 10, 14) to real frequencies. | `simulate.py` |
| Backtest | Walk-forward by week, scored next to the closing line | `backtest.py` |

Ratings knobs were tuned on 2013–2018 (`python -m nflpredictor tune`).
Everything else is refitted on every run.

## Backtest, 2015–2025

Every game is predicted from earlier weeks of its season plus the preseason
prior, with the points map, blend and simulator fitted on earlier seasons only.

| Predictor | Margin MAE | Total MAE | Team-score MAE | Brier | Winners |
|---|---|---|---|---|---|
| Final (model + market + simulator) | 9.82 | 10.43 | 7.27 | 0.212 | 66.0% |
| Model only | 10.08 | 10.75 | 7.47 | 0.220 | 64.6% |
| Elo baseline | 10.18 | 10.98 | 7.59 | 0.221 | 64.3% |
| Closing line | 9.81 | 10.44 | 7.27 | 0.212 | 66.0% |

- On its own the model gets within 0.3 points of the closing line on the
  margin and edges out Elo.
- The final prediction does not beat the closing line on error. For games
  with a line, the fitted blend puts most of the weight on the line, so the
  final number tracks it. Games without a line yet use the model alone.
- Win probabilities are about as well calibrated as de-vigged moneylines, and
  the 80% ranges contain the actual score 82% of the time.

## Can it beat the betting line?

Picking a side whenever the model's own spread and the line differ by half a
point or more. Starting QBs here are each team's previous starter, so nothing
is used that a Wednesday line could not know. Break-even at standard −110 odds
is 52.4%.

| Picks against | Record (W-L-P) | Cover rate | 95% range |
|---|---|---|---|
| Wednesday line, 2015–2020 (Westgate SuperContest lines) | 687-593-39 | 53.7% | 50.9%–56.4% |
| Closing line, same 2015–2020 games | 683-608-34 | 52.9% | 50.2%–55.6% |
| Closing line, 2015–2025 | 1308-1224-65 | 51.7% | 49.7%–53.6% |

What this means:

- Against Wednesday lines the model has a small, real edge (better than a coin
  flip in five of six seasons). It is just above break-even, and the 95% range
  still includes it, so it is not a proven money-maker.
- Against closing lines it has no edge that pays: 51.7% overall, and about 50%
  in 2021–2025. The line at kickoff already knows what the model knows.
- The special-teams rating is where the edge comes from. Without it, picks
  covered 52.9% against Wednesday lines. Lines did not move toward its picks
  before kickoff, which suggests the market underweights special teams rather
  than catching up to them.
- Things tried that did not hold up out of sample: separate passing and rushing
  ratings, success rate, pace, and adjustments for home underdogs, big
  favorites, divisional games, rest, primetime, temperature and the level of the
  total. Wind trims totals error slightly but only with measured game-day wind.

So the honest answer is: better than the line early in the week, by a margin
too thin to count on yet, and not better than the closing line. The predictions
page tracks the model's picks live against the first line each game had, and
how often the line then moves toward the pick, so this keeps being tested on
games the model has never seen.

Full tables, calibration buckets and bootstrap intervals are in
[`predictions/backtest.md`](predictions/backtest.md). The backtest's remaining
optimism: totals use measured rather than forecast wind, and the error table
uses closing lines and actual starting QBs.

## Running it yourself

Python 3.11 or newer.

```bash
cd NFLScorePredictor
pip install -r requirements.txt

python -m nflpredictor update            # refresh and predict the next two weeks
python -m nflpredictor update --weeks 1 --no-weather
python -m nflpredictor ratings           # current ratings (EPA per play; special teams per game)
python -m nflpredictor backtest          # walk-forward 2015-2025 plus pick records, writes predictions/backtest.md
python -m nflpredictor tune --save       # re-tune the ratings engine on 2013-2018
python -m pytest -q tests
```

Downloads are cached in `.cache/` (ignored by git).

## Outputs

| File | Contents |
|---|---|
| `predictions/README.md` | Upcoming games, season grading, last week's results, power ratings |
| `predictions/latest.json` | The same upcoming predictions as JSON |
| `predictions/log.csv` | Every prediction (last one before kickoff) with the final score once known |
| `predictions/ratings.csv` | Team ratings in points per game |
| `predictions/model.json` | The fitted coefficients, blend weights and simulator settings |
| `data/epa/` | Per-season team-game and QB-game efficiency summaries |

## Not modeled yet

- Non-QB injuries. QB changes are covered through the projected starters in
  the nflverse schedule, but other injuries reach the prediction only through
  the betting line.
- A live odds feed. Lines come from the nflverse schedule, which is updated
  several times a week; a commercial odds API would make them fresher.
- The report's gradient-boosting residual layer. With about 285 games a
  season, the linear rest, wind and QB terms are what earned a place.

## Data

Schedules, lines and play-by-play from [nflverse](https://github.com/nflverse).
Weather data by [Open-Meteo.com](https://open-meteo.com/) (CC BY 4.0).
