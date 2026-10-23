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
| Skaters | Regulars (at least three of the team's last five games) missing from its latest game, weighted by their ice time (forwards and defensemen apart) and points per game, from the skater box scores. A goal-rate input: absent forwards cost goals. | `skaters.py` |
| Elo | Goal-margin Elo, the win-probability baseline. Its result-based edge is also one input to the goal-rate model, because it held up out of sample. | `elo.py` |
| Goal rates | Poisson regression of each team's regulation goals (both goalies in) on the ratings, the opposing starter, missing skaters on both sides, Elo, home ice, back-to-backs and playoffs, on top of the current league scoring level | `model.py` |
| Market | Backs each team's goal rate out of the de-vigged moneyline and total, through the same simulator, and blends `w × model + (1 − w) × market`. `w` starts from the value fitted on sportsbookreview's archived 2012-13 to 2021-22 closing lines (57% model) and is refitted on logged games with lines as they accumulate. | `market.py` |
| Simulator | 10,000 games per matchup, minute by minute. Score effects (tied teams play for overtime late; trailing teams press), goalie pulls at the rate teams really pull at each deficit and minute, empty-net and six-on-five goals, three-on-three overtime and shootouts, or sudden-death playoff overtime. Fitted on recent seasons' game states and tuned so the overtime rate matches history. | `simulate.py` |
| Edges | Expected value of each side of the puck line, moneyline and total at the posted price, from the final prediction anchored to the market, once both starting goalies are confirmed; Kelly-staked (see below) | `edges.py` |
| Backtest | Walk-forward by day, scored against Elo and a goals-only Poisson model, and against sportsbookreview's archived lines for 2016-17 to 2021-22, with the edges graded at their prices | `backtest.py` |

Ratings knobs were tuned on 2013-14 to 2016-17 (`python -m nhlpredictor tune`).
Everything else is refitted on every run.

## Backtest, 2016-17 to 2025-26

Every game is predicted from earlier days of its season plus the preseason
prior, with the goal-rate model and simulator fitted on earlier seasons only.
13,175 games; a coin flip scores 0.693 log loss and 0.250 Brier.

| Predictor | Log loss | Brier | Winners |
|---|---|---|---|
| Model + simulator | 0.6665 | 0.237 | 58.9% |
| Elo | 0.6707 | 0.239 | 58.4% |
| Goals-only Poisson | 0.6721 | 0.240 | 58.0% |
| Home team every time | 0.6900 | 0.248 | 54.0% |

- The model beats Elo by 0.0041 log loss per game (95% interval 0.0027 to
  0.0056) and a goals-only Poisson model by 0.0056, and holds up on the
  seasons not used for tuning (0.6662 from 2017-18 on). Elo is also one of the
  model's inputs; the Elo row is Elo on its own.
- Hockey edges are thin, as the report warns: the gap between this model and
  always picking the home team is 0.024, and between it and Elo 0.0041.
- Win probabilities are well calibrated: games given 60–70% were won 64.9%
  of the time (predicted 64.1%), and 40–50% games 44.6% (predicted 45.8%).
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
  starts: log loss 0.6665 with the actual starter against 0.6666 with the
  projection, a difference within noise. The projection names the right
  goalie 65.5% of the time. After the heavy shrinkage that goaltending's poor
  repeatability calls for, a team's two goalies are usually rated close
  together, so the swap rarely moves the win chance much. Confirmed starters
  are still used when ESPN lists them, since an unknown or struggling backup
  does shift the numbers.
- Regulars missing from the lineup (`skaters.py`, from the skater box
  scores): a skater who played at least three of the team's last five games
  but not its latest counts by his average ice time and points. Absent
  forwards mattered, defensemen less: with them the model's log loss went
  from 0.6672 to 0.6665, and on the archived games from 0.6677 to 0.6668.
  Absent forwards even predicted results given the closing line (about 2.5
  standard errors), so the market seems slow to price a missing forward.

Full tables and calibration buckets are in
[`predictions/backtest.md`](predictions/backtest.md).

## Can it beat the betting line?

Closer than any other sport here, but not clearly. Sportsbookreview's archive
(via the [sportsbookreview-scraper](https://github.com/flancast90/sportsbookreview-scraper)
project) has opening and closing moneylines, closing puck lines with prices
and opening and closing totals through 2021-22. On the 6,903 games of 2016-17
to 2021-22 it covers, matched by date, teams and final score, de-vigged:

| Predictor | Log loss |
|---|---|
| Model + simulator | 0.6668 |
| Opening line | 0.6685 |
| Closing line | 0.6660 |
| Model blended with the closing line | 0.6665 |

- The model is 0.0008 behind the closing line (95% interval −0.0012 to
  +0.0028) and 0.0017 ahead of the opening line, both within noise. Blended
  with the closing line it is within noise of the line alone (+0.0005). The
  weight on the model, fitted each season on the archive's earlier seasons
  only, stayed between 63% and 66%; fitted on every archived season it is 57%, which is where the
  live blend starts. In the other sports the market gets most of the weight.

The predictions page shows and tracks betting edges on three markets: the
puck line (±1.5), the moneyline and the total, all including overtime and the
shootout (the shootout winner is credited with one goal, as in the official
score). Each side is priced with the final prediction: the blended goal
rates simulated against the posted lines, anchored to the market's own
chances (the market's de-vigged chance plus the difference between the
simulation at the blend and at the market's goal rates, same random draws),
so only the blend's disagreement with the market can make an edge. A side is
an edge when its expected value per unit staked at the posted price is at
least 3%:

    EV = p_win × (decimal odds − 1) − p_loss      (a push returns the stake)

and the side with the highest EV is shown, staked at a quarter of the Kelly
stake with at most 3 units (1% of the bankroll each) on one game (shared
[BettingCore](../BettingCore) package). Edges wait until both starting
goalies are confirmed, since a surprise starter moves the line; until then
the page says so. A total whose prices are missing is assumed to be -110
(marked `-110*`); the puck line and moneyline are never assumed, so without a
price the page shows fair odds instead.

The same edges in the backtest, walk-forward, at the archive's prices (totals
at an assumed −110, since the archive does not say which side a total's
price belongs to), with the actual starting goalies:

| Lines | Chances | Market | Edges | Record (W-L-P) | ROI | 95% range | Expected ROI |
|---|---|---|---|---|---|---|---|
| closing | final (live rule) | Puck line | 1616 | 798-818-0 | +1.5% | −3.4% to +6.5% | +6.8% |
| closing | final (live rule) | Moneyline | 2587 | 1075-1512-0 | −2.2% | −6.7% to +2.7% | +8.6% |
| closing | final (live rule) | Total | 1832 | 899-806-127 | +0.0% | −4.5% to +4.5% | +7.0% |
| closing | model alone (old rule) | Puck line | 2463 | 1264-1199-0 | −1.4% | −5.3% to +2.7% | +8.8% |
| closing | model alone (old rule) | Moneyline | 3452 | 1462-1990-0 | +1.0% | −3.2% to +5.2% | +10.8% |
| closing | model alone (old rule) | Total | 2825 | 1391-1245-189 | +1.3% | −2.5% to +5.0% | +8.8% |
| opening | final | Moneyline | 1907 | 838-1069-0 | +8.9% | +1.7% to +16.2% | +10.4% |
| opening | final | Total | 1877 | 955-786-136 | +3.9% | −0.5% to +8.1% | +7.0% |

- At the closing line the edges came out about even after the bookmaker's
  margin, every range including zero, while the EVs promised +7% to +9%:
  the chances behind the edges are still too confident.
- Against the opening moneyline the edges made +8.9%, with a range clear of
  zero. The predictions page bets the last line before puck drop, not the
  opener, so this is not what the live record measures.

Edges are refreshed with every run until puck drop, frozen there, graded on
the final score, and summed per market (W-L-P, units staked and won, ROI and
expected ROI) at the logged price; the page also counts how often the
moneyline moves toward the edge the model saw on the first line. Edges
logged before this rule (from the model alone, one unit each) are left out
of that record.

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
| `predictions/log.csv` | Every prediction (last one before puck drop), with the lines and prices it was made against, the model-only and final (anchored) win, cover and over/under chances, the goalies' confirmation status, each market's edge (`{spread,moneyline,total}_edge_{pick,side,line,price,prob,ev,stake}`) and the final score once known |
| `predictions/ratings.csv` | Team ratings in goals per game |
| `predictions/model.json` | The fitted coefficients, blend weight and simulator settings |
| `data/games/` | Per-season schedules, team-game, goalie-game and game-state summaries, and missing skaters by team-game |
| `data/shot_model.json` | The frozen expected-goals model and score-and-venue weights |

## Not modeled yet

- Tonight's lineup. Absences count once a regular has missed the team's last
  game, so a player out for the first time tonight, or back tonight, is only
  in the betting line until the box score shows it.
- Travel and time zones. Rest is modeled through back-to-backs, which carried
  the signal in testing; a time-zone feature is the next candidate.
- Betting lines after 2021-22. The free archive stops there, so later seasons
  are tested against the market only in the live log.
- Goalie news before ESPN lists it. Until a starter is named, the prediction
  uses the probability-weighted value of the likely starters.

## Data

Schedules, play-by-play and box scores from the NHL's own API, compiled daily
by [sportsdataverse](https://github.com/sportsdataverse/fastRhockey-nhl-data)
(fastRhockey). Expected goals come from this project's own shot model, not
the source's. Betting lines and probable goalies from ESPN's public
scoreboard; 2011-12 to 2021-22 lines from sportsbookreview.com's archive, as
collected by [sportsbookreview-scraper](https://github.com/flancast90/sportsbookreview-scraper).
