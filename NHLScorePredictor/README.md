# NHL Score Predictor

Predicts the final score of every NHL game, with win probabilities, the chance
of overtime and a realistic range for each team, and keeps itself current
through the season. A scheduled GitHub Action pulls the newest results,
play-by-play, lines and probable goalies several times a day, refits the
model, re-predicts the next few days of games, and grades each prediction once
the game is final.

**Latest predictions: [`predictions/README.md`](predictions/README.md)**
· Backtest: [`predictions/backtest.md`](predictions/backtest.md)

The design follows the *NHL Score Prediction: Techniques Report*: it estimates
two goal rates per game from score-adjusted expected goals, the starting
goalie and game context, blends them with rates backed out of the betting
line, then simulates the game minute by minute, empty nets, overtime and
shootouts included, to get each team's score distribution.

## How it stays up to date

`.github/workflows/nhl-score-predictor.yml` runs `python -m nhlpredictor update`
from September through June:

| When (ET) | Why |
|---|---|
| Every morning, about 9:30 AM | Last night's results and play-by-play, new ratings |
| About 12:30 PM | Morning skates done, starters starting to be named; afternoon games |
| About 6 PM | Confirmed goalies and late lines before the 7 PM games |
| About 9 PM | Same, before the late West Coast games |

Each run:

1. Downloads this season's schedule, play-by-play and goalie box scores and
   rebuilds this season's summaries in `data/games/`.
2. Refits the goal-rate model and the score simulator on the last four seasons
   plus every game played so far this season.
3. Fetches moneylines, the puck line, totals (with their prices) and probable
   starting goalies from ESPN for the next three game days.
4. Predicts every game in that window that has not started, looks for betting
   edges on the puck line, moneyline and total, and writes the predictions and
   edges to `predictions/log.csv`, replacing earlier ones for the same game. A
   game's prediction stops changing at puck drop, so the logged one is always
   the last made before the game.
5. Fills in final scores and grades the season so far, against the betting
   line once lines are logged, and grades each logged edge.
6. Commits the results back to the repo (only when something besides a
   timestamp changed).

Nothing needs to be done between seasons. In August the predictor rolls over
to the new season, the finished season's summaries stay in `data/games/` as
history, and predictions resume when the schedule starts. If it starts
mid-season (as it did about three weeks into 2026-27) it backfills the games
already played with walk-forward predictions, labeled as such, so the season
grading starts populated.

**To turn the schedule on**, merge this folder and the workflow into the
repository's default branch (GitHub only runs scheduled workflows from there),
make sure Actions are enabled, and optionally start a first run from the
Actions tab with **Run workflow**.

## How it works

| Stage | What it does | Code |
|---|---|---|
| Data | NHL play-by-play, schedules and goalie box scores since 2009-10, reduced to one row per team-game and goalie-game plus minute-by-minute game-state tables | `data.py` |
| Expected goals | A logistic shot model (distance, angle, shot type, rebounds, rush chances, strength state) fitted once on 2010-11 to 2014-15 and frozen, so no later season is scored by a model that saw it. It also holds score-and-venue weights: trailing teams outshoot leaders, so 5-on-5 shots are reweighted by score state (McCurdy's method). | `shots.py` |
| Ratings | Ridge regression of each team's 5-on-5 xG per 60 for and against on team, opponent and home indicators, plus a goals-per-game rating that catches finishing xG misses. Each team is pulled toward a preseason prior built from last season, and recent games count more (90-day half-life). Power-play and penalty ratings are built too and shown on the page. | `ratings.py` |
| Goalies | Goals saved above expected per 100 unblocked shots, relative to the league that season and shrunk hard toward a slightly below-average prior. Starters come from ESPN's probable goalies when listed. Otherwise each goalie's chance of starting comes from his recent share of starts, marked down on the second night of a back-to-back by the factor seen historically. | `goalies.py` |
| Elo | Goal-margin Elo, the win-probability baseline. Its result-based edge is also one input to the goal-rate model, because it held up out of sample. | `elo.py` |
| Goal rates | Poisson regression of each team's regulation goals (both goalies in) on the ratings, the opposing starter, Elo, home ice, back-to-backs and playoffs, on top of the current league scoring level | `model.py` |
| Market | Backs each team's goal rate out of the de-vigged moneyline and total, through the same simulator, and blends `w × model + (1 − w) × market`. `w` is fitted on logged games with lines (an even split until a few hundred exist). | `market.py` |
| Simulator | 10,000 games per matchup, minute by minute. Score effects (tied teams play for overtime late; trailing teams press), goalie pulls at the rate teams really pull at each deficit and minute, empty-net and six-on-five goals, three-on-three overtime and shootouts, or sudden-death playoff overtime. Fitted on recent seasons' game states and tuned so the overtime rate matches history. | `simulate.py` |
| Edges | Expected value of each side of the puck line, moneyline and total at the posted price, from the model's own numbers before the blend (see below) | `edges.py` |
| Backtest | Walk-forward by day, scored against Elo and a goals-only Poisson model | `backtest.py` |

Ratings knobs were tuned on 2013-14 to 2016-17 (`python -m nhlpredictor tune`).
Everything else is refitted on every run.

## Backtest, 2016-17 to 2025-26

Every game is predicted from earlier days of its season plus the preseason
prior, with the goal-rate model and simulator fitted on earlier seasons only.
13,175 games; a coin flip scores 0.693 log loss and 0.250 Brier.

| Predictor | Log loss | Brier | Winners |
|---|---|---|---|
| Model + simulator | 0.6672 | 0.237 | 59.0% |
| Elo | 0.6707 | 0.239 | 58.4% |
| Goals-only Poisson | 0.6721 | 0.240 | 58.0% |
| Home team every time | 0.6900 | 0.248 | 54.0% |

- The model beats Elo by 0.0035 log loss per game (95% interval 0.0021 to
  0.0049) and a goals-only Poisson model by 0.0049, and holds up on the
  seasons not used for tuning (0.6667 from 2017-18 on). Elo is also one of the
  model's inputs; the Elo row is Elo on its own.
- Hockey edges are thin, as the report warns: the gap between this model and
  always picking the home team is 0.023, and between it and Elo 0.0035.
- Win probabilities are well calibrated: games given 60–70% were won 64.0%
  of the time (predicted 64.1%), and 40–50% games 44.0% (predicted 45.8%).
- The simulator gets the shape of hockey scores right where independent
  Poisson does not: 21.8% of games tied after regulation (actual 22.5%,
  independent Poisson 17.2%) and 19.7% one-goal regulation finishes, empty-net
  goals counted (actual 20.6%, Poisson 31.1%). It undercounts games with an
  empty-net goal (27.7% against 30.3%), because coaches pull the goalie earlier
  every season and the simulator is fitted on the seasons before.
- 80% ranges contain each team's goals 89% of the time (goals are whole
  numbers, so a range covers a bit more than 80%). The headline score is
  exactly right in 7.6% of games, so read the win chance first.

What mattered, judged on the tuning seasons before looking at later ones:

- 5-on-5 expected goals were the most useful input, then the actual-goals
  rating, back-to-backs and the Elo edge.
- Power-play and penalty-drawing ratings added nothing once the goals rating,
  which already contains power-play goals, was in. They are still shown on
  the predictions page.
- Knowing the actual starting goalie did not beat projecting him from recent
  starts: log loss 0.6672 with the actual starter against 0.6667 with the
  projection, a difference within noise. The projection names the right
  goalie 65.5% of the time. After the heavy shrinkage that goaltending's poor
  repeatability calls for, a team's two goalies are usually rated close
  together, so the swap rarely moves the win chance much. Confirmed starters
  are still used when ESPN lists them, since an unknown or struggling backup
  does shift the numbers.

Full tables and calibration buckets are in
[`predictions/backtest.md`](predictions/backtest.md).

## Can it beat the betting line?

Not known yet. No free source has a long history of NHL lines, so the model
could not be backtested against the market. Instead every live prediction
logs the lines and prices it was made against, and the predictions page
grades the model, the market and the blend on the same games.

It also shows and tracks betting edges on three markets: the puck line
(±1.5), the moneyline and the total, all including overtime and the shootout
(the shootout winner is credited with one goal, as in the official score).
Each side is priced with the model's own numbers, before blending with the
market: the win chance from the model's goal rates, and the puck-line cover
and over/under chances from a separate simulation of those same rates, at the
posted line and with pushes on whole-number totals. A side is an edge when
its expected value per unit staked at the posted price is at least 3%:

    EV = p_win × (decimal odds − 1) − p_loss      (a push returns the stake)

and the side with the highest EV is shown. A total whose prices are missing
is assumed to be -110 (marked `-110*`); the puck line and moneyline are never
assumed, so without a price the page shows the model's fair odds instead.
Edges are refreshed with every run until puck drop, frozen there, graded on
the final score, and summed per market (W-L-P, units, return per bet) at the
logged price; the page also counts how often the moneyline moves toward the
edge the model saw on the first line. The blend weight starts at an even
split and is refitted from these games as they accumulate.

## Running it yourself

Python 3.11 or newer.

```bash
cd NHLScorePredictor
pip install -r requirements.txt

python -m nhlpredictor update              # refresh and predict the next three game days
python -m nhlpredictor update --days 1 --no-espn
python -m nhlpredictor ratings             # current ratings and likely starting goalies
python -m nhlpredictor check --raw         # print ESPN's parsed lines and the raw odds objects
python -m nhlpredictor backtest            # walk-forward 2016-17 to 2025-26, writes predictions/backtest.md
python -m nhlpredictor tune --save         # re-tune the ratings engine on 2013-14 to 2016-17
python -m nhlpredictor summarize --all     # rebuild every season's summaries from play-by-play
python -m nhlpredictor fit-shots           # refit the frozen expected-goals model (then summarize --all)
python -m pytest -q tests
```

Seasons are named by the year they end on the command line (2027 is 2026-27).
Downloads are cached in `.cache/` (ignored by git).

## Outputs

| File | Contents |
|---|---|
| `predictions/README.md` | Upcoming games with puck-line, moneyline and total edges, season grading, edge record, latest results, power ratings, goalies |
| `predictions/latest.json` | The same upcoming predictions as JSON |
| `predictions/log.csv` | Every prediction (last one before puck drop), with the lines and prices it was made against, the model-only cover and over/under chances, each market's edge (`{spread,moneyline,total}_edge_{pick,side,line,price,prob,ev}`) and the final score once known |
| `predictions/ratings.csv` | Team ratings in goals per game |
| `predictions/model.json` | The fitted coefficients, blend weight and simulator settings |
| `data/games/` | Per-season schedules, team-game, goalie-game and game-state summaries |
| `data/shot_model.json` | The frozen expected-goals model and score-and-venue weights |

## Not modeled yet

- Skater injuries and lineup changes. They reach the prediction only through
  the betting line and, after a few games, the ratings.
- Travel and time zones. Rest is modeled through back-to-backs, which carried
  the signal in testing; a time-zone feature is the next candidate.
- A history of betting lines. No free source has one for the NHL, so the blend
  weight starts at an even split and is fitted as the live log fills, and the
  model's edges against the line are tested live, not in the backtest.
- Goalie news before ESPN lists it. Until a starter is named, the prediction
  uses the probability-weighted value of the likely starters.

## Data

Schedules, play-by-play and box scores from the NHL's own API, compiled daily
by [sportsdataverse](https://github.com/sportsdataverse/fastRhockey-nhl-data)
(fastRhockey). Expected goals come from this project's own shot model, not
the source's. Betting lines and probable goalies from ESPN's public
scoreboard.
