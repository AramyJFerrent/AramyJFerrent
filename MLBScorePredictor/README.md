# MLB Score Predictor

Predicts the final score of every MLB game, postseason included, with win
probabilities, the run line, the chance of extra innings, a realistic range
for each team and any betting edge on the run line, moneyline and total,
and keeps itself current through the season. A
scheduled GitHub Action pulls the newest box scores, probable pitchers,
posted lineups, weather and lines several times a day, refits the model,
re-predicts the next two days of games, and grades each prediction once the
game is final.

**Latest predictions: [`predictions/README.md`](predictions/README.md)**
· Backtest: [`predictions/backtest.md`](predictions/backtest.md)

The design follows the *MLB Score Prediction: Techniques Report*: it builds
each team's expected runs from tonight's personnel (the starting pitcher,
the lineup against his hand and the bullpen that is actually available),
adjusts for the park and the weather, blends with runs backed out of the
betting line, and simulates the game half-inning by half-inning, with the
skipped bottom of the ninth, walk-offs and the extra-inning runner, to get
each team's run distribution.

## How it stays up to date

`.github/workflows/mlb-score-predictor.yml` runs `python -m mlbpredictor update`
from March through November:

| When (ET) | Why |
|---|---|
| Every morning, about 9:30 AM | Last night's box scores, new ratings, the day's probable pitchers |
| About 12:30 PM | Lineups for the afternoon games |
| About 4:30 PM | Lineups and late lines for the 7 PM games |
| About 6:30 PM | The rest of the evening lineups |
| About 9 PM | Before the late West Coast games |

Each run:

1. Reads this season's schedule, line scores and probable pitchers from the
   MLB Stats API in one request, plus the box score of every game finished
   since the last run, and updates this season's files in `data/games/`.
2. Refits the run model and the simulator on the last three seasons plus
   every game played so far this season.
3. Reads the next two game days: probable pitchers, posted lineups and
   game-time weather from the MLB Stats API, first-pitch temperature
   forecasts from Open-Meteo for the rest, and moneylines, run lines and
   totals, with their prices, from ESPN.
4. Predicts every game in that window that has not started, works out the
   betting edge (if any) on each market, and writes the predictions to
   `predictions/log.csv`, replacing earlier ones for the same game. A game's
   prediction stops changing at first pitch, so the logged one is always the
   last made before the game, with the lineups, lines, prices and edges it
   was made against.
5. Fills in final scores and grades the season so far, against Elo and, once
   lines are logged, the betting market, and grades each logged edge.
6. Commits the results back to the repo (only when something besides a
   timestamp changed).

Nothing needs to be done between seasons. A weekly off-season run picks up
next season's schedule in December, and when Retrosheet publishes the
finished season's play-by-play (usually that winter), it replaces the box
score version of that season, so the simulator and platoon tables get the
new season too. If the predictor starts mid-season (as it did during the
2026 postseason) it backfills the games already played with walk-forward
predictions, labeled as such, so the season grading starts populated.

**To turn the schedule on**, merge this folder and the workflow into the
repository's default branch (GitHub only runs scheduled workflows from there),
make sure Actions are enabled, and optionally start a first run from the
Actions tab with **Run workflow**. The first run reads the whole season's box
scores, which takes a few minutes; later runs read only new games.

## How it works

| Stage | What it does | Code |
|---|---|---|
| Data | Retrosheet play-by-play for 2012-2025, parsed play by play into one row per game, per batter and per pitcher, with base-out transitions and platoon counts (every parsed final score, out and team batting total matches Retrosheet's game logs). The season in progress comes from MLB Stats API box scores in the same format. Player ids are linked across the two through the Chadwick register. | `retro.py`, `statsapi.py`, `data.py` |
| Park factors | Poisson regressions of runs and of each plate-appearance outcome on batting team, fielding team, park and home field over the three seasons before, with parks pulled toward neutral; new parks and one-off neutral sites stay near 1 | `parks.py` |
| Player ratings | Every batter and pitcher rated on strikeouts, walks, hit by pitch, singles, doubles, triples and home runs per plate appearance: park-adjusted, recency-weighted results (time counts only during seasons) shrunk toward the league average for his role by each outcome's stabilization point, measured from history by empirical Bayes (strikeouts settle in about 50 plate appearances; doubles allowed by pitchers take well over a thousand) | `players.py` |
| Matchups | Each of the nine batters meets the probable starter in a log5 plate appearance with the platoon factor for his side and the pitcher's hand, and the same against the bullpen; the outcome probabilities are weighted by each lineup slot's share of plate appearances and valued with linear weights from the base-out chain. Posted lineups are used when available, otherwise the lineup the team last used against a starter of the same hand. | `features.py` |
| Bullpen and workload | The bullpen is every reliever from the team's last 15 games, weighted by recent use and marked down after pitching the day before (more after 25+ pitches), on back-to-back days or three times in four days. The starter's expected outs come from his recent starts, and set his expected share of each inning. | `features.py` |
| Team ratings and Elo | Ridge ratings of each team's runs scored and allowed against a preseason prior catch what the player ratings miss (fielding, baserunning, how a staff is used), and a FiveThirtyEight-style Elo with a starting-pitcher adjustment is both a baseline and an input | `ratings.py`, `elo.py` |
| Run model | Each team's expected runs in each inning: the league's current scoring level times the inning's own level, times the starter's and the bullpen's matchups mixed by the starter's expected share of that inning, times park, home field, temperature, wind, team ratings and Elo. Fitted by Poisson likelihood on the runs of every inning 1-8 in the last three seasons. | `model.py` |
| Market | De-vigs ESPN's moneyline and total, backs each team's expected runs out of them through the same simulator, and blends `log runs = w × model + (1 − w) × market`. `w` starts from the value fitted on Pinnacle's 2016 closing lines and is refitted on logged games as they accumulate. | `market.py` |
| Simulator | 10,000 games per matchup, inning by inning. Innings come from a base-out Markov chain built from Retrosheet's transitions (runner advances, double plays, steals and pickoffs included), scaled to each inning's expected runs, so an inning's run distribution is exact rather than assumed; extra innings start from a runner on second in the regular season. A shared game factor lets whole games run hot or cold, a team trailing by one to three from the ninth on faces the other side's closer, the home team skips the bottom of the ninth when ahead and walk-offs stop at the winning run unless they are home runs. Each setting is tuned so simulated scores match history. | `simulate.py` |
| Edges | Expected value per $1 of each side of the run line, moneyline and total at the posted price, `EV = p × (decimal price − 1) − (1 − p − push)`, from the model's own numbers before blending: its win chance, and a simulation of its own expected runs for the chance of covering the posted run line (whichever side gives the 1.5 runs) and of going over or under the total, pushes on whole-number totals included. A side is an edge at EV ≥ 3%; each market shows its best side. Totals without a posted price are assumed -110 (marked `-110*`); run-line and moneyline prices are never assumed, so without one there is no edge and the run line shows the model's fair odds. | `edges.py` |
| Backtest | Walk-forward by day over 2016-2025, scored against Elo, team ratings alone and Pinnacle's 2016 lines, with the edges graded on Pinnacle's moneylines and totals | `backtest.py` |

## Backtest, 2016 to 2025

Every game is predicted from earlier days' results only (player and team
ratings, with park factors from earlier seasons), with the run model and
simulator fitted on the three seasons before. Lineups and starting pitchers
are the actual ones, as a run knows them once lineups post; weather is the
recorded game-time weather. 23,168 games, postseason included; a coin flip
scores 0.693 log loss and 0.250 Brier.

| Predictor | Log loss | Brier | Winners |
|---|---|---|---|
| Model + simulator | 0.6746 | 0.2409 | 57.6% |
| Elo with starting pitchers | 0.6754 | 0.2413 | 57.6% |
| Team runs ratings only | 0.6785 | 0.2428 | 56.8% |
| Home team every time | 0.6910 | 0.2489 | 53.3% |

- The model beats FiveThirtyEight-style Elo with its starting-pitcher
  adjustment by 0.0009 log loss per game (95% interval 0.0001 to 0.0017) and
  team ratings alone by 0.0040, and holds up on the seasons since 2021
  (0.6759 against Elo's 0.6765). Elo is also one of the model's inputs; the
  Elo row is Elo on its own.
- Baseball edges are as thin as the report warns: everything the model knows
  moves log loss 0.016 from always picking the home team, and its edge over
  Elo is a tenth of a percent.
- Win probabilities are well calibrated: games given 60–70% were won 63.9%
  of the time (predicted 63.9%), and 40–50% games 45.3% (predicted 45.8%).
- The simulator gets the shape of baseball scores right:

  | Check | Simulator | Actual |
  |---|---|---|
  | Runs per game, both teams | 9.08 | 9.03 |
  | Team shut out | 6.2% | 6.2% |
  | Decided by one run | 28.2% | 27.8% |
  | Extra innings (regular season) | 8.5% | 8.5% |
  | Home team skips the bottom of the ninth | 45.1% | 44.7% |
  | Walk-off win | 8.2% | 8.5% |
  | Home team wins by 2+ (run line) | 36.5% | 36.6% |

- 80% ranges contain each team's runs 85.7% of the time (runs are whole
  numbers, so a range covers a bit more than 80%). The headline score is
  exactly right in 2.5% of games, so read the win chance first.

What mattered, from development runs on 2017-2025 (a faster approximation
of the same model, without the simulator):

- The player matchups on their own (lineup against starter and bullpen,
  park, home field, weather) scored 0.6767 against Elo's 0.6751. Adding the
  team ratings brought that to 0.6746 and the Elo edge to 0.6740: some of
  what wins games (fielding, baserunning, how a staff is used) is not in the
  players' outcome rates.
- The ratings' half-lives and shrinkage barely mattered (within ±0.0003),
  and a separate bullpen-workload term added nothing once tired relievers
  are marked down inside the bullpen rating.
- Posted lineups did not beat projected ones: on 2023-2025, log loss 0.6792
  with the actual lineups against 0.6791 with each team's last lineup
  against a starter of the same hand, a difference within noise. Most
  lineups look like the team's last one, and one changed spot moves a
  team's runs by a few percent. The posted lineup is still used once it is
  out.
- Without the closer effect the simulator sent 9.6% of regular-season games
  to extra innings, against 8.5% in reality: a team down a run or two in
  the ninth ties the game less often than an average inning suggests,
  because it faces the other side's closer.

Full tables and calibration buckets are in
[`predictions/backtest.md`](predictions/backtest.md).

## Against the betting market

On Pinnacle's complete 2016 line history (2,461 games, de-vigged):

| Predictor | Log loss | Brier |
|---|---|---|
| Model + simulator | 0.6764 | 0.2417 |
| Elo with starting pitchers | 0.6787 | – |
| Opening line | 0.6770 | – |
| Closing line | 0.6735 | 0.2403 |
| Model blended with the closing line | 0.6740 | 0.2406 |

- The model on its own is as good as the opening line (0.0006 better,
  within noise) and 0.0029 behind the closing line (95% interval 0.0000 to
  +0.0059), as the report expects: the market sharpens as starters and
  lineups are confirmed, and the close already knows what the model knows.
- Blended with the closing line it adds nothing measurable (0.6740 against
  0.6735, a difference within noise): a sharp closing line already holds
  what the model knows. The best weight on the model was 19%, which is
  where the live blend starts; the opening lines and softer books it will
  mostly see live are where a model has more room to help.
- Betting edges on the same games, walk-forward, from the model alone
  (before blending) against Pinnacle's prices: one unit on each market's
  best side whenever its expected value is 3% or more.

  | Market | Edges | Record (W-L-P) | Units | ROI | 95% range on ROI |
  |---|---|---|---|---|---|
  | Moneyline, closing line | 1306 | 544-761-1 | -59.13 | -4.5% | -10.8% to +1.7% |
  | Moneyline, opening line | 1083 | 504-578-1 | +49.31 | +4.6% | -2.1% to +11.5% |
  | Total, closing line | 1628 | 785-769-74 | +2.29 | +0.1% | -4.6% to +5.0% |
  | Run line | no historical prices | | | | |

  Against the close the moneyline edges lose about the margin, and against
  the opening line they win; neither is clear of noise in one season. The
  live log grades the same edges against ESPN's lines.
- No free source has betting lines for the other seasons, so the live log
  keeps testing it: every prediction records the line it was made against,
  and the predictions page grades the model, the market and the blend on the
  same games, and tracks the model's betting edges on the run line,
  moneyline and total (sides whose expected value at the posted price is 3%
  or more, from the model alone) with their record and units won at the
  price logged before first pitch, and how often the moneyline then moves
  toward the model's side. The blend weight is refitted from those games as
  they accumulate. Live lines
  come from ESPN's provider rather than Pinnacle, so the weight may settle
  somewhere else.

## Running it yourself

Python 3.11 or newer.

```bash
cd MLBScorePredictor
pip install -r requirements.txt

python -m mlbpredictor update              # refresh and predict the next two game days
python -m mlbpredictor update --days 1 --offline
python -m mlbpredictor ratings             # power ratings by lineup, rotation, bullpen and the rest
python -m mlbpredictor check --raw         # read the live sources once and print what was parsed (and ESPN's raw odds)
python -m mlbpredictor audit               # consistency checks on this season's data, next to last season's
python -m mlbpredictor backtest            # walk-forward 2016-2025, writes predictions/backtest.md
python -m mlbpredictor summarize           # rebuild the Retrosheet seasons from play-by-play
python -m pytest -q tests
```

Downloads are cached in `.cache/` (ignored by git).

## Outputs

| File | Contents |
|---|---|
| `predictions/README.md` | Upcoming games with run-line, moneyline and total edges, season grading, edge record, latest results, power ratings |
| `predictions/latest.json` | The same upcoming predictions as JSON |
| `predictions/log.csv` | Every prediction (last one before first pitch), with the lineups, lines and prices it was made against, the model's own cover and over chances, each market's edge (`spread_edge_*` for the run line, `moneyline_edge_*`, `total_edge_*`) and the final score once known |
| `predictions/ratings.csv` | Power ratings in runs per game, by unit |
| `predictions/model.json` | The fitted coefficients, blend weight and simulator settings |
| `data/games/` | Per-season games, batting, pitching, transition and platoon summaries (finished seasons gzipped) |
| `data/players.csv` | Names, batting side and throwing hand for every player |
| `data/pinnacle_2016.csv` | Pinnacle's 2016 opening and closing moneylines and totals |

## Not modeled yet

- Injuries and roster moves, except through lineups and the bullpen
  window. A player back from the injured list rejoins the projected lineup
  only once he has played, and before lineups post a missing star is only
  in the betting line.
- Statcast pitch and batted-ball quality. Ratings use outcomes only; pitch
  tracking would make young players' ratings settle faster.
- Wind direction for upcoming games. The wind term is fitted on
  Retrosheet's recorded wind, but forecasts do not say whether it blows in
  or out at each park, so wind only counts once MLB posts game-time
  conditions near first pitch. Retractable roofs are assumed closed below
  60°F or above 85°F until then.
- Aging. A player's prior is his own recency-weighted record, with no aging
  curve, which flatters players in decline and undersells young ones early
  in a season.
- Catcher framing, defensive positioning, umpires and travel, except as far
  as the team ratings catch them.

## Data

Play-by-play from [Retrosheet](https://www.retrosheet.org), via the
[Chadwick Bureau mirror](https://github.com/chadwickbureau/retrosheet), with
player ids from the [Chadwick register](https://github.com/chadwickbureau/register).
The information used here was obtained free of charge from and is
copyrighted by Retrosheet. Interested parties may contact Retrosheet at
www.retrosheet.org.

Schedules, box scores, probable pitchers, lineups and game-time weather from
the MLB Stats API (statsapi.mlb.com); betting lines from ESPN's public
scoreboard; temperature forecasts by [Open-Meteo.com](https://open-meteo.com/)
(CC BY 4.0). Pinnacle's 2016 lines from the
[pinnacle.data](https://github.com/marcoblume/pinnacle.data) R package.
