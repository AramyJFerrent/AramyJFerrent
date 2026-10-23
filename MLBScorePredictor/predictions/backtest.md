# Walk-forward backtest

Seasons 2016 to 2025, postseason included. Every game is predicted using only earlier days' results (player and team ratings, with park factors from earlier seasons), with the run model and simulator fitted on the three seasons before. Lineups and starting pitchers are the actual ones, as a game-day run knows them once lineups post; weather is the recorded game-time weather. Baselines are scored on the same games.

## 2016 to 2025

| Predictor | Games | Log loss | Brier | Winners | Runs MAE | Total MAE |
|---|---|---|---|---|---|---|
| Model + simulator | 23168 | 0.6743 | 0.2407 | 57.7% | 2.45 | 3.53 |
| Elo with starting pitchers | 23168 | 0.6754 | 0.2413 | 57.6% | – | – |
| Team runs ratings only | 23168 | 0.6785 | 0.2428 | 56.8% | – | – |
| Home team every time | 23168 | 0.6910 | 0.2489 | 53.3% | – | – |

## 2021 on

| Predictor | Games | Log loss | Brier | Winners | Runs MAE | Total MAE |
|---|---|---|---|---|---|---|
| Model + simulator | 12356 | 0.6756 | 0.2414 | 57.3% | 2.44 | 3.51 |
| Elo with starting pitchers | 12356 | 0.6765 | 0.2418 | 57.6% | – | – |
| Team runs ratings only | 12356 | 0.6785 | 0.2428 | 56.8% | – | – |
| Home team every time | 12356 | 0.6912 | 0.2490 | 53.1% | – | – |

## Is the difference real?

Paired bootstrap of the per-game log loss (negative favors the first).

| Comparison | Mean difference | 95% interval |
|---|---|---|
| Model vs Elo with starting pitchers | -0.0012 | -0.0020 to -0.0003 |
| Model vs team runs ratings only | -0.0042 | -0.0055 to -0.0030 |

## Against the betting market, 2016

Pinnacle's complete 2016 line history (2461 games), de-vigged. The blend backs each team's expected runs out of the closing moneyline and total through the simulator and mixes them with the model's on the log scale, 20% model (that weight is fitted on these same games, so the blend's score here flatters it).

| Predictor | Log loss | Brier | Total MAE |
|---|---|---|---|
| Model + simulator | 0.6764 | 0.2418 | 3.48 |
| Elo with starting pitchers | 0.6787 | – | – |
| Opening line | 0.6770 | – | – |
| Closing line | 0.6735 | 0.2403 | 3.46 |
| Model blended with the closing line | 0.6740 | 0.2406 | 3.48 |

| Comparison | Mean difference | 95% interval |
|---|---|---|
| Model vs closing line | +0.0030 | -0.0000 to +0.0059 |
| Blend vs closing line | +0.0005 | -0.0003 to +0.0014 |
| Model vs opening line | -0.0006 | -0.0033 to +0.0021 |

## Against the betting market, 2016 to 2021

Sportsbookreview's archived lines, matched to 12935 nine-inning games by date, teams and final score, de-vigged. The blend backs each team's expected runs out of the moneyline and total, as the live predictor does, and mixes them with the model's; each season's weight on the model is fitted on the archive's earlier seasons only (2016 4%, 2017 13%, 2018 6%, 2019 7%, 2020 6%, 2021 6%). Fitted on all of 2015 to 2021 (15330 games), it is 10%: the live predictor's starting weight.

| Predictor | Log loss |
|---|---|
| Model + simulator | 0.6728 |
| Opening line | 0.6721 |
| Closing line | 0.6702 |
| Model blended with the closing line (walk-forward weight) | 0.6709 |

| Comparison | Mean difference | 95% interval |
|---|---|---|
| Model vs closing line | +0.0026 | +0.0012 to +0.0039 |
| Blend vs closing line | +0.0007 | +0.0002 to +0.0011 |
| Model vs opening line | +0.0007 | -0.0006 to +0.0020 |

### Betting edges at the archived prices

The predictions page's edges, walk-forward: the final prediction's chances (the walk-forward blend, simulated against each line and anchored to the market's own chances), and for comparison the model's own before any blending. A side is an edge at EV of 3% or more per $1, staked at a quarter of the Kelly stake (units are 1% of the bankroll, at most 3 per game). The opening rows blend with, and bet into, the opening moneyline and total; the archive keeps no opening run line. Totals are priced at -110, since the archive does not record which side a total's price belongs to. The ROI range is a 95% bootstrap interval over games.

| Market | Edges | Record (W-L-P) | Staked | Units won | ROI | Expected ROI | 95% range on ROI |
|---|---|---|---|---|---|---|---|
| Run line, closing line, final prediction | 5 | 5-0-0 | 12.2 | +14.95 | +122.4% | +16.9% | +99.4% to +139.3% |
| Moneyline, closing line, final prediction | 16 | 8-8-0 | 13.7 | +7.95 | +58.0% | +14.6% | -38.4% to +147.0% |
| Total (-110 assumed), closing line, final prediction | 2 | 1-1-0 | 2.2 | +0.19 | +8.8% | +3.7% | -100.0% to +90.9% |
| Run line, closing line, model only | 5063 | 2463-2600-0 | 5787.9 | -262.93 | -4.5% | +8.4% | -7.4% to -1.6% |
| Moneyline, closing line, model only | 6684 | 2809-3874-1 | 7029.6 | -139.38 | -2.0% | +10.0% | -5.1% to +1.1% |
| Total (-110 assumed), closing line, model only | 6549 | 3255-2968-326 | 12029.9 | -23.76 | -0.2% | +11.7% | -2.7% to +2.3% |
| Moneyline, opening line, final prediction | 10 | 5-5-0 | 10.6 | +5.95 | +56.1% | +16.0% | -52.2% to +189.0% |
| Total (-110 assumed), opening line, final prediction | 4 | 2-2-0 | 5.0 | -0.26 | -5.2% | +4.3% | -100.0% to +90.9% |
| Moneyline, opening line, model only | 4591 | 2020-2570-1 | 5959.8 | +67.11 | +1.1% | +10.1% | -2.6% to +4.9% |
| Total (-110 assumed), opening line, model only | 6605 | 3390-2906-309 | 13978.3 | +477.37 | +3.4% | +11.7% | +1.0% to +5.8% |


## Win-probability calibration

| Predicted home win | Games | Mean predicted | Actual |
|---|---|---|---|
| 20-30% | 93 | 27.8% | 26.9% |
| 30-40% | 1453 | 36.7% | 37.1% |
| 40-50% | 6443 | 45.8% | 45.3% |
| 50-60% | 9957 | 54.8% | 54.7% |
| 60-70% | 4625 | 63.9% | 64.2% |
| 70-80% | 589 | 72.8% | 75.0% |
| 80-90% | 8 | 81.9% | 37.5% |

## Score distribution checks

| Check | Simulator | Actual |
|---|---|---|
| Runs per game, both teams | 9.09 | 9.03 |
| Team shut out | 6.1% | 6.2% |
| Decided by one run | 28.2% | 27.8% |
| Extra innings (regular season) | 8.6% | 8.5% |
| Home team skips the bottom of the ninth | 45.1% | 44.7% |
| Walk-off win | 8.3% | 8.5% |
| Home team wins by 2+ | 36.5% | 36.6% |

Each team's runs scored against its full simulated distribution (ranked probability score, lower is better), next to a plain Poisson and a negative binomial (variance 2.26 times the mean, the league-wide ratio) with the same expected runs:

| Simulator | Negative binomial | Poisson |
|---|---|---|
| 0.0568 | 0.0568 | 0.0587 |

- 80% ranges contained the team's actual runs 85.7% of the time (runs are whole numbers, so a range covers a little more than 80%).
- Headline score exactly right: 2.5% of games.

## Posted lineups against projected ones

On 7420 games, log loss with the actual lineups is 0.6789; with each team's lineup projected from its last game against a starter of the same hand (what a morning run uses) it is 0.6788 (difference -0.0000, 95% interval -0.0006 to +0.0005).
