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
| Market | De-vigs ESPN's moneyline and total, backs each team's expected runs out of them through the same simulator, and blends `log runs = w × model + (1 − w) × market`. `w` starts from the value fitted on sportsbookreview's archived 2015-2021 closing lines (9%) and is refitted on logged games as they accumulate. | `market.py` |
| Simulator | 10,000 games per matchup, inning by inning. Innings come from a base-out Markov chain built from Retrosheet's transitions (runner advances, double plays, steals and pickoffs included), scaled to each inning's expected runs, so an inning's run distribution is exact rather than assumed; extra innings start from a runner on second in the regular season. A shared game factor lets whole games run hot or cold, a team trailing by one to three from the ninth on faces the other side's closer, the home team skips the bottom of the ninth when ahead and walk-offs stop at the winning run unless they are home runs. Each setting is tuned so simulated scores match history. | `simulate.py` |
| Edges | Expected value per $1 of each side of the run line, moneyline and total at the posted price, `EV = p × (decimal price − 1) − (1 − p − push)`, from the final prediction: the blended runs simulated against the posted run line and total, anchored to the market's own chances (the market's de-vigged chance plus the difference between the simulation at the blend and at the market's runs, same random draws), so only the blend's disagreement with the market can make an edge. A side is an edge at EV ≥ 3%, staked at a quarter of the Kelly stake with at most 3 units a game (shared [BettingCore](../BettingCore) package); each market shows its best side. Totals without a posted price are assumed -110 (marked `-110*`); run-line and moneyline prices are never assumed, so without one there is no edge and the run line shows the model's fair odds. | `edges.py`, `market.py` |
| Backtest | Walk-forward by day over 2016-2025, scored against Elo and team ratings alone; against the market on Pinnacle's 2016 lines and sportsbookreview's 2016-2021 archive, with the edges graded at the archive's prices | `backtest.py` |

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

Two sources of historical lines. Sportsbookreview's archive (via the
[sportsbookreview-scraper](https://github.com/flancast90/sportsbookreview-scraper)
project) has opening and closing moneylines, closing run lines with their
prices, and opening and closing totals for 2011-2021; its baseball rows pair
each game's visitors with the previous game's home team, which the shared
loader puts back together, after which 99% of games match Retrosheet by date,
teams and final score. Pinnacle's complete 2016 line history is the sharpest
single book.

On the archive's 12,935 nine-inning games from 2016 to 2021 with both lines,
de-vigged, the blend weight walk-forward (each season's fitted on earlier
seasons only):

| Predictor | Log loss |
|---|---|
| Model + simulator | 0.6729 |
| Opening line | 0.6721 |
| Closing line | 0.6702 |
| Model blended with the closing line | 0.6708 |

- The model is 0.0027 behind the closing line (95% interval 0.0013 to
  0.0041) and level with the opening line (0.0008 behind, within noise), as
  the report expects: the market sharpens as starters and lineups are
  confirmed, and the close already knows what the model knows.
- Blending the model in makes the closing line slightly worse (0.0006, 95%
  interval 0.0002 to 0.0011). The weight fitted on earlier seasons ran 3% to
  12% on the model; fitted on all of 2015-2021 it is 9%, which is where the
  live blend starts. Pinnacle 2016 tells the same story (model 0.6764,
  closing line 0.6735, blend 0.6740).
- Betting edges at the archive's prices, walk-forward, Kelly-staked
  (totals at an assumed -110, since the archive does not say which side a
  total's price belongs to):

  | Market | Chances | Edges | Record (W-L-P) | ROI | 95% range | Expected ROI |
  |---|---|---|---|---|---|---|
  | Run line, closing | final (live rule) | 5 | 4-1-0 | +66.8% | −29.4% to +136.4% | +17.2% |
  | Moneyline, closing | final (live rule) | 10 | 3-7-0 | +38.9% | −80.1% to +137.2% | +17.2% |
  | Total, closing | final (live rule) | 1 | 1-0-0 | +90.9% | – | +3.9% |
  | Run line, closing | model alone (old rule) | 5247 | 2602-2645-0 | −2.9% | −5.7% to −0.1% | +8.4% |
  | Moneyline, closing | model alone (old rule) | 6824 | 2926-3898-0 | −1.3% | −4.3% to +1.6% | +10.2% |
  | Total, closing | model alone (old rule) | 6593 | 3265-3002-326 | −0.3% | −2.8% to +2.2% | +11.7% |
  | Moneyline, opening | model alone | 4721 | 2122-2598-1 | +2.1% | −1.5% to +5.8% | +10.1% |
  | Total, opening | model alone | 6567 | 3387-2870-310 | +3.4% | +1.0% to +5.8% | +11.7% |

  With the model at a few percent of the blend, the final prediction almost
  never disagrees with the closing price by 3% of EV: 16 edges in six
  seasons, too few to judge. The model alone, the old rule, finds an edge in
  most games at the close and loses about the margin. Against the opening
  line the model alone came out ahead, on totals clearly (with -110
  assumed, which the real prices could move either way), but the
  predictions page bets the last line before first pitch, not the opener.
- The live log keeps testing it: every prediction records the line it was
  made against, the predictions page grades the model, the market and the
  blend on the same games, and tracks the betting edges with their stakes,
  record, units and ROI at the price logged before first pitch, and how
  often the moneyline then moves toward the model's side. The blend weight
  is refitted from those games as they accumulate; live lines come from
  ESPN's provider, so the weight may settle somewhere else.

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
python -m mlbpredictor backtest            # walk-forward 2016-2025 and the archived lines, writes predictions/backtest.md
python -m mlbpredictor backtest --save-weight   # also save the archive's blend weight to params.json
python -m mlbpredictor summarize           # rebuild the Retrosheet seasons from play-by-play
python -m pytest -q tests
```

Downloads are cached in `.cache/` (ignored by git), the line archive for a month.

## Outputs

| File | Contents |
|---|---|
| `predictions/README.md` | Upcoming games with run-line, moneyline and total edges, fair first-five-innings odds, season grading, edge record, latest results, power ratings |
| `predictions/latest.json` | The same upcoming predictions as JSON |
| `predictions/log.csv` | Every prediction (last one before first pitch), with the lineups, lines and prices it was made against, the model's own and the final (anchored) cover and over chances, each market's edge (`spread_edge_*` for the run line, `moneyline_edge_*`, `total_edge_*`: pick, side, line, price, chance, EV and stake in units) and the final score once known |
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
- First-five-innings edges. The page shows fair first-five odds from the
  simulator (the moneyline with ties refunded, and expected runs), but no
  free source has first-five prices to bet or backtest them against.
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
[pinnacle.data](https://github.com/marcoblume/pinnacle.data) R package;
2011-2021 lines from sportsbookreview.com's archive, as collected by
[sportsbookreview-scraper](https://github.com/flancast90/sportsbookreview-scraper).
