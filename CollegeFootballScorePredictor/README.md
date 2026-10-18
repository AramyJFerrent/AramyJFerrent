# College Football Score Predictor

Predicts the final score of every FBS game, with win probabilities and a
realistic range for each team, and keeps itself current through the season.
A scheduled GitHub Action pulls new results, play-by-play and betting lines
every day (several times on Saturdays), refits the model, re-predicts the
upcoming games, and grades each prediction once the game is final.

**Latest predictions: [`predictions/README.md`](predictions/README.md)**
· Backtest: [`predictions/backtest.md`](predictions/backtest.md)

The design follows the *College Football Score Prediction: Techniques Report*
and the companion [NFL Score Predictor](../NFLScorePredictor): a preseason
prior built from last season, program history and portal-aware returning
production; opponent-adjusted EPA ratings with garbage time removed; separate
ratings for FCS teams; a blend with the betting market; and a drive
simulation that turns expected points into full score distributions.

## How it stays up to date

`.github/workflows/cfb-score-predictor.yml` runs `python -m cfbpredictor update`:

| When (ET) | Why |
|---|---|
| Every morning, about 9 AM | New final scores, Sunday and Monday play-by-play, updated lines |
| Tuesday to Saturday, about 6 PM | Final lines before the weeknight and Saturday night games |
| Saturday, about 11:45 AM and 2:45 PM | Before the noon and 3:30 PM kickoffs |
| Saturday, about 9:45 PM | Before the late West Coast games |

Each run:

1. Downloads the cfbfastR schedules and scores and this season's play-by-play,
   and rebuilds this season's efficiency summary in `data/team_games/`.
2. Rebuilds this season's returning production from the latest rosters, until
   the season's first game is played (then it stays fixed).
3. Fetches current lines for the games ahead: CollegeFootballData (median
   across books) if a `CFBD_API_KEY` secret is set, otherwise ESPN's public
   scoreboard. If neither answers, games are predicted from the model alone.
4. Refits the preseason prior, the margin and total models, the market blend
   and the score simulator on the last four seasons plus every game played so
   far this season.
5. Predicts every game in the next two weeks that has not kicked off.
6. Writes the predictions to `predictions/log.csv`, replacing earlier ones for
   the same game. A game's prediction stops changing at kickoff, so the logged
   one is always the last made before the game.
7. Fills in final scores and grades the season so far against the betting line.
8. Commits the results back to the repo (only when something besides a
   timestamp changed).

Nothing needs to be done between seasons. In March the predictor rolls over to
the new season. Once cfbfastR publishes the new rosters it computes each team's
returning production, transfers included, and keeps recomputing it as rosters
change through the portal windows until the first game; the preseason prior is
refitted on all seasons so far. Predictions resume once
the schedule is out. It started mid-season (Week 7 of 2026), so it backfilled
the weeks already played with walk-forward predictions, labeled as such, so
the season grading starts populated.

**To turn the schedule on**, merge this folder and the workflow into the
repository's default branch (GitHub only runs scheduled workflows from there)
and make sure Actions are enabled. Optionally add a free
[CollegeFootballData API key](https://collegefootballdata.com/key) as a
repository secret named `CFBD_API_KEY` for multi-book lines; each run uses one
or two of the free tier's 1,000 monthly calls. Then start a first run from the
Actions tab with **Run workflow** so the upcoming games pick up their lines.

## How it works

| Stage | What it does | Code |
|---|---|---|
| Data | cfbfastR schedules (2005 on) and play-by-play with EPA (2014 on), reduced to one row per team-game. Games between two FBS or FCS teams are kept, so FCS opponents get ratings of their own. | `data.py` |
| Preseason prior | A regression, fitted on earlier seasons, of each team's season rating on last season's rating, program history (the three seasons before), returning production and their interaction, separately for offense and defense. Returning production credits every player on this season's roster with last season's yards and defensive plays wherever he played, so transfers count, at half credit when moving up from FCS. | `prior.py`, `returning.py` |
| Ratings engine | Ridge regression of each offense's EPA per play on offense, opposing defense, home edge and an FBS-vs-FCS edge, with garbage time (CFBD definition) removed and lost fumbles counted half. Each team is pulled toward its prior with the strength of 400 offensive and 600 defensive plays (about six and nine games), so the prior carries September and still holds 40% (offense) to 50% (defense) of the weight in November. Ratings are split into a conference level and a team deviation. | `ratings.py` |
| Special teams and pace | Net EPA per game on kickoffs, punts and field goals, and snaps per game, rated the same way | `ratings.py` |
| Elo | Margin-of-victory Elo from 2005, kept as the baseline and also used as an input | `elo.py` |
| Margin and total models | Two linear maps fitted separately: the margin from offense, defense, net special teams, home field (smaller in conference games), the FBS-vs-FCS gap and Elo; the total from offense, defense and pace on top of the current scoring level | `model.py` |
| Market blend | `final = w × model + (1 − w) × line` for margin and total, with `w` fitted on recent seasons | `model.py` |
| Score simulator | 10,000 simulated games per matchup. Each team's scoring chances end in a touchdown (then a kick or two-point try), a field goal or nothing; tied games go to overtime, which always produces a winner, with margins drawn from real overtime games. Dispersion is calibrated to real prediction errors and key margins to real frequencies. | `simulate.py` |
| Lines | History: the median across books of closing and opening lines (2013–2025), else the line in the play-by-play. Live: CFBD or ESPN. | `lines.py`, `odds.py` |
| Backtest | Walk-forward by week, scored next to the closing line, broken out by kind of game | `backtest.py` |

Ratings knobs were tuned on 2016–2020 (`python -m cfbpredictor tune`), and
2021–2025 is reported separately as seasons the tuning never saw. Everything
else is refitted on every run.

## Backtest, 2016–2025

Every game is predicted from earlier weeks of its season plus the preseason
prior, with the prior regression, points maps, blend and simulator fitted on
earlier seasons only. FBS-vs-FBS games with a closing line:

| Predictor | Margin MAE | Total MAE | Team-score MAE | Brier | Winners |
|---|---|---|---|---|---|
| Final (model + market + simulator) | 12.29 | 12.85 | 8.98 | 0.173 | 73.5% |
| Model only | 12.85 | 13.31 | 9.35 | 0.180 | 72.3% |
| Elo baseline | 13.42 | 14.04 | 9.85 | 0.188 | 70.6% |
| Closing line | 12.28 | 12.85 | 8.97 | 0.174 | 73.3% |

- On its own the model beats Elo by 0.57 points of margin error (95% interval
  0.47 to 0.67) and trails the closing line by the same amount. In the
  seasons tuning never saw (2021–2025) it misses by 12.73 against the line's
  12.12.
- The final prediction matches the closing line on error (12.29 vs 12.28) and
  its win probabilities score slightly better (Brier 0.173 vs 0.174 for the
  market's own). For games with a line the fitted blend puts about 90% of the
  margin weight and 80–90% of the total weight on the line, so the final
  number tracks it; games without a line yet use the model alone.
- Win probabilities are well calibrated, the 80% ranges contain the actual
  score 82% of the time, and one-score games are predicted at 33.7% against
  34.3% actual.

By kind of game (margin MAE; the full table is in the backtest file):

| Segment | Games | Model | Final | Line |
|---|---|---|---|---|
| Weeks 1–4 | 1,850 | 13.15 | 12.39 | 12.37 |
| Week 5 to end of regular season | 5,286 | 12.73 | 12.26 | 12.26 |
| Power 4 vs Group of 5 | 967 | 13.25 | 12.22 | 12.19 |
| Nonconference | 2,046 | 13.28 | 12.41 | 12.39 |
| FBS vs FCS | 1,014 | 13.78 | 12.14 | 12.09 |

The model is weakest where the report says college models struggle: early in
the season, across conferences and against FCS teams, where its ratings have
the least connected evidence. The market is about equally sharp everywhere,
and the blend keeps the final prediction level with it in every segment.

## What earned a place, and what did not

Each stage was kept only if it improved the model's out-of-sample margin or
total error over 2016–2025:

- **Returning production** is worth 0.10 to 0.14 points of margin error
  (2021–2025 and 2016–2020) and 0.19 in Weeks 1–4, the biggest single gain in
  the prior.
- **Elo as an input** to the margin model cut error by about 0.2 points, and
  by 0.44 in Weeks 1–4: a rating with a long memory of results carries program
  strength the play-by-play prior misses.
- **Pace** improves the model's totals by about 0.15 points. In one shared
  points map it made margins worse, so margins and totals are fitted as
  separate models and pace sits only in the total.
- **Special teams** helps a little (about 0.02 points).
- Tried and dropped: letting whole conferences shift in-season (it never beat
  rating teams one at a time, so that pull is set high), travel distance,
  time zones crossed, rest days, partial weight on garbage-time plays and
  faster recency weighting. Each was within noise.

## Can it beat the betting line?

Picking a side whenever the model's own spread and the line differ by half a
point or more, on FBS-vs-FBS games. Break-even at standard −110 odds is 52.4%.

| Picks against | Record (W-L-P) | Cover rate | 95% range |
|---|---|---|---|
| Opening line, 2016–2025 (games with one) | 3014-2896-103 | 51.0% | 49.7%–52.3% |
| Closing line, same games | 2935-3010-114 | 49.4% | 48.1%–50.6% |
| Closing line, 2016–2025 | 3227-3263-127 | 49.7% | 48.5%–50.9% |

No. The model does not cover often enough to profit against either line. It
does see something the market later agrees with: when the opening line and
the model disagreed, the line moved toward the model's side before kickoff
55.5% of the time (5,188 games). The predictions page tracks the live picks
against the first line each game had, and that line movement, so this keeps
being tested on games the model has never seen.

## Running it yourself

Python 3.11 or newer.

```bash
cd CollegeFootballScorePredictor
pip install -r requirements.txt

python -m cfbpredictor update            # refresh and predict the next two weeks
python -m cfbpredictor update --weeks 1 --no-lines
python -m cfbpredictor ratings           # current FBS ratings (add --all for FCS)
python -m cfbpredictor backtest          # walk-forward 2016-2025, writes predictions/backtest.md
python -m cfbpredictor tune --save       # re-tune the ratings engine on 2016-2020
python -m cfbpredictor build-data        # rebuild every file in data/ from the sources
python -m pytest -q tests
```

Downloads are cached in `.cache/` (ignored by git). A backtest needs only the
committed `data/` files plus the schedules, which it downloads.

## Outputs

| File | Contents |
|---|---|
| `predictions/README.md` | Upcoming games, season grading, last week's results, FBS power ratings |
| `predictions/latest.json` | The same upcoming predictions as JSON |
| `predictions/log.csv` | Every prediction (last one before kickoff) with the final score once known |
| `predictions/ratings.csv` | FBS ratings in points per game |
| `predictions/model.json` | The fitted coefficients, prior regression, blend weights and simulator settings |
| `predictions/backtest.md`, `backtest_summary.json` | The latest backtest |
| `data/team_games/` | Per-season team-game efficiency summaries and play-by-play lines |
| `data/production/`, `data/returning.csv` | Player production and returning production by team |
| `data/lines.csv`, `data/venues.csv` | Consensus historical lines; home stadiums |

## Not modeled yet

- **Injuries and quarterback availability.** College availability reports are
  new and not in the free data, so injuries reach the prediction only through
  the betting line.
- **Talent and recruiting rankings, and coaching changes**, two of the
  report's prior ingredients, are not in the free cfbfastR data. Returning
  production also lacks offensive line snaps.
- **Weather.** There was no historical wind data reachable to fit a college
  wind effect, and the NFL predictor found it small, so totals are not
  adjusted for forecasts.
- **Bowl opt-outs.** The schedule files have no postseason games before 2023,
  so bowls are backtested on 2023–2025 only (134 games). With a line, bowl
  predictions lean on it as usual.
- The report's gradient-boosting residual layer. The inputs it would use are
  either not in the data (weather, availability) or did not help as linear
  terms (travel, rest).

## Data

Schedules, play-by-play, rosters, team information and historical lines from
[cfbfastR](https://github.com/sportsdataverse/cfbfastR-data)
(sportsdataverse), which builds on
[CollegeFootballData](https://collegefootballdata.com/). Live lines from
CollegeFootballData (with a key) or ESPN's public scoreboard.
