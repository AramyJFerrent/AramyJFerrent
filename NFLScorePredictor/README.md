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
   QBs), this season's play-by-play, injury reports and snap counts, and
   rebuilds this season's efficiency summary in `data/epa/` and injury losses
   in `data/injuries/`.
2. Refits the ratings-to-points map, home field, rest and QB effects, the
   market blend weight, the wind adjustment and the score simulator on the last
   six seasons plus every game played so far this season.
3. Predicts every game in the next two weeks that has not kicked off.
4. Writes the predictions to `predictions/log.csv`, replacing earlier ones for
   the same game. A game's prediction stops changing at kickoff, so the logged
   one is always the last made before the game.
5. Fills in final scores and grades the season so far against the betting line,
   including every betting edge logged before kickoff.
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
| Other injuries | Every non-QB player on the week's injury report counts by his recent snap share (last three games with the team) times the chance his status means he sits (Out 99.9%, Doubtful 99.2%, Questionable 33%, Probable 4%, measured on 2013-2025), summed for the offensive line, skill players, defensive front and defensive backs. Players on injured reserve are already out of the recent snaps and the ratings, so only fresh absences count. | `injuries.py` |
| Elo | Margin-of-victory Elo, kept as the sanity-check baseline | `elo.py` |
| Points map | Linear map from ratings to each team's points on top of the current league scoring level, with special teams, home field (smaller in division games), rest, QB and injury terms (its own offense's losses, the opponent's defense's) | `model.py` |
| Market blend | `final = w × model + (1 − w) × line` for margin and total, with `w` fitted on recent seasons out of sample: each season's points map is refitted without it, so the weight reflects how the model does on games it has not seen | `model.py` |
| Weather | Kickoff wind forecast (Open-Meteo) for open-air games lowers the total by the amount the market has historically missed | `weather.py`, `model.py` |
| Score simulator | 10,000 simulated games per matchup. Each team's scoring chances end in a touchdown (then a kick or two-point try), a field goal or nothing, with overtime and ties. Dispersion is calibrated to real prediction errors and key margins (3, 7, 10, 14) to real frequencies. | `simulate.py` |
| Betting edges | Expected value of each side of the spread, moneyline and total at the posted price, from the final prediction anchored to the market: the market's de-vigged chance plus the difference between the simulator at the blend and at the line (same random draws). An edge needs EV of at least +3% and is staked at a quarter of the Kelly stake, at most 3 units a game (shared [BettingCore](../BettingCore) package). | `edges.py`, `model.py` |
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

The predictions page shows a betting edge for the spread, moneyline and total
of every game. Each side is priced with the final prediction, the one on the
page: the model blended with the line, simulated, and anchored to the
market's own chances, so only the blend's disagreement with the line can make
an edge. The expected value of a side is `p × (decimal odds − 1) − (1 − p −
push)` per unit staked at the posted price, and a side is an edge when that
is at least +3%, staked at a quarter of the Kelly stake. Prices are the ones
in the nflverse schedule (`home_spread_odds`, `away_spread_odds`,
`over_odds`, `under_odds`, `home_moneyline`, `away_moneyline`); when a spread
or total has no price it is assumed to be −110 (shown as `-110*`), and a
missing moneyline means no edge. Ties refund moneyline bets and whole-number
lines can push. Each game's edges are logged with its prediction, frozen at
kickoff and graded once it is final; edges logged before this rule (from the
model alone, one unit each) are left out of the record.

Walk-forward backtest, Kelly stakes. Starting QBs here are each team's
previous starter and the injury report is left out, so nothing is used that
a Wednesday line could not know; early lines are also priced without the
game's measured wind. Opening spreads and totals come from sportsbookreview's
archive, matched by date, teams and final score (openers more than 7 points
from the close, or across zero by 4 or more, are archive sign errors and are
dropped).

| Market | Lines | Chances | Edges | Record (W-L-P) | ROI | 95% range | Expected ROI |
|---|---|---|---|---|---|---|---|
| Spread | Closing, 2015–2025 | final (live rule) | 141 | 67-70-4 | −9.5% | −25.6% to +7.7% | +5.6% |
| Moneyline | Closing, 2015–2025 | final (live rule) | 325 | 79-245-1 | −8.4% | −26.3% to +9.9% | +7.3% |
| Total | Closing, 2015–2025 | final (live rule) | 299 | 165-131-3 | +7.9% | −3.9% to +19.6% | +8.2% |
| Spread | Opening, 2015–2021 (−110 assumed) | final | 31 | 17-14-0 | +5.6% | −29.8% to +39.8% | +5.9% |
| Total | Opening, 2015–2021 (−110 assumed) | final | 39 | 19-20-0 | −2.8% | −33.5% to +27.5% | +4.8% |
| Spread | Closing, 2015–2025 | model alone (old rule) | 2279 | 1153-1071-55 | +0.1% | −4.0% to +4.2% | +18.1% |
| Moneyline | Closing, 2015–2025 | model alone (old rule) | 2329 | 820-1500-9 | −4.2% | −9.8% to +1.6% | +28.2% |
| Total | Closing, 2015–2025 | model alone (old rule) | 2206 | 1087-1099-20 | −2.4% | −7.1% to +2.2% | +17.3% |
| Spread | Wednesday, 2015–2020 (−110 assumed) | model alone | 1017 | 523-467-27 | +0.6% | −5.6% to +6.6% | +16.6% |

What this means:

- The model's own spread and total often sit several points from the line,
  so the old rule found an edge in most games and promised +17% or more; it
  broke even at best. The blend weight on the model, fitted out of sample,
  has been close to zero since 2019, so the final prediction rarely
  disagrees with the line by enough to bet: about 70 edges a season.
- None of the final prediction's records is clearly different from zero.
  Totals came out ahead, but the backtest knows each game's measured wind,
  which the live page only has as a forecast, so that is optimistic: priced
  without wind against the opener, the totals edges disappeared (they had
  been almost all windy-game unders at +28%).
- Non-QB injuries make the model's own forecast better (margin error 10.075
  to 10.052, log loss 0.631 to 0.629), but the closing line already prices
  them: regressed on the line, the injury losses explain nothing more, so
  they do not change the final prediction or the edges.
- In earlier tests of the model's spread against the line, the special-teams
  rating was where the signal came from: the market underweights it. Things
  tried that did not hold up out of sample: separate passing and rushing
  ratings, success rate, pace, and adjustments for home underdogs, big
  favorites, divisional games, rest, primetime, temperature and the level of
  the total.

So the honest answer is no edge to count on. The predictions page tracks
every logged edge live, with units staked and won, ROI and expected ROI per
market, and how often the spread line moves toward the model's early spread
edge, so this keeps being tested on games the model has never seen.

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
python -m nflpredictor backtest          # walk-forward 2015-2025 plus edge records, writes predictions/backtest.md
python -m nflpredictor tune --save       # re-tune the ratings engine on 2013-2018
python -m pytest -q tests
```

Downloads are cached in `.cache/` (ignored by git).

## Outputs

| File | Contents |
|---|---|
| `predictions/README.md` | Upcoming games with spread, moneyline and total edges, season grading and edge record, last week's results, power ratings |
| `predictions/latest.json` | The same upcoming predictions as JSON |
| `predictions/log.csv` | Every prediction (last one before kickoff) with the posted prices, the final (anchored) and model-only win/cover/over chances and the edge in each market (pick, side, line, price, chance, EV and stake in units), and the final score once known |
| `predictions/ratings.csv` | Team ratings in points per game |
| `predictions/model.json` | The fitted coefficients, blend weights and simulator settings |
| `data/epa/` | Per-season team-game and QB-game efficiency summaries |
| `data/injuries/` | Per-season non-QB injury losses by team and week (snap shares, by position group) |

## Not modeled yet

- Injuries before the game's report. Statuses come out late in the week, so
  a run earlier in the week has no injury terms for the coming game yet.
- A live odds feed. Lines come from the nflverse schedule, which is updated
  several times a week; a commercial odds API would make them fresher.
- The report's gradient-boosting residual layer. With about 285 games a
  season, the linear rest, wind and QB terms are what earned a place.

## Data

Schedules, lines, play-by-play, injury reports and snap counts (from Pro
Football Reference) from [nflverse](https://github.com/nflverse); 2011-2021
opening lines from sportsbookreview.com's archive, as collected by
[sportsbookreview-scraper](https://github.com/flancast90/sportsbookreview-scraper).
Weather data by [Open-Meteo.com](https://open-meteo.com/) (CC BY 4.0).
