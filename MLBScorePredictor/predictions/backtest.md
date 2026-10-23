# Walk-forward backtest

Seasons 2016 to 2025, postseason included. Every game is predicted using only earlier days' results (player and team ratings, with park factors from earlier seasons), with the run model and simulator fitted on the three seasons before. Lineups and starting pitchers are the actual ones, as a game-day run knows them once lineups post; weather is the recorded game-time weather. Baselines are scored on the same games.

## 2016 to 2025

| Predictor | Games | Log loss | Brier | Winners | Runs MAE | Total MAE |
|---|---|---|---|---|---|---|
| Model + simulator | 23168 | 0.6746 | 0.2409 | 57.6% | 2.45 | 3.53 |
| Elo with starting pitchers | 23168 | 0.6754 | 0.2413 | 57.6% | – | – |
| Team runs ratings only | 23168 | 0.6785 | 0.2428 | 56.8% | – | – |
| Home team every time | 23168 | 0.6910 | 0.2489 | 53.3% | – | – |

## 2021 on

| Predictor | Games | Log loss | Brier | Winners | Runs MAE | Total MAE |
|---|---|---|---|---|---|---|
| Model + simulator | 12356 | 0.6759 | 0.2415 | 57.3% | 2.44 | 3.51 |
| Elo with starting pitchers | 12356 | 0.6765 | 0.2418 | 57.6% | – | – |
| Team runs ratings only | 12356 | 0.6785 | 0.2428 | 56.8% | – | – |
| Home team every time | 12356 | 0.6912 | 0.2490 | 53.1% | – | – |

## Is the difference real?

Paired bootstrap of the per-game log loss (negative favors the first).

| Comparison | Mean difference | 95% interval |
|---|---|---|
| Model vs Elo with starting pitchers | -0.0009 | -0.0017 to -0.0001 |
| Model vs team runs ratings only | -0.0040 | -0.0052 to -0.0027 |

## Against the betting market, 2016

Pinnacle's complete 2016 line history (2461 games), de-vigged. The blend backs each team's expected runs out of the closing moneyline and total through the simulator and mixes them with the model's on the log scale, 19% model (that weight is fitted on these same games, so the blend's score here flatters it).

| Predictor | Log loss | Brier | Total MAE |
|---|---|---|---|
| Model + simulator | 0.6764 | 0.2417 | 3.49 |
| Elo with starting pitchers | 0.6787 | – | – |
| Opening line | 0.6770 | – | – |
| Closing line | 0.6735 | 0.2403 | 3.46 |
| Model blended with the closing line | 0.6740 | 0.2406 | 3.48 |

| Comparison | Mean difference | 95% interval |
|---|---|---|
| Model vs closing line | +0.0029 | -0.0000 to +0.0059 |
| Blend vs closing line | +0.0005 | -0.0002 to +0.0013 |
| Model vs opening line | -0.0006 | -0.0033 to +0.0021 |

## Against the betting market, 2016 to 2021

Sportsbookreview's archived lines, matched to 12935 nine-inning games by date, teams and final score, de-vigged. The blend backs each team's expected runs out of the moneyline and total, as the live predictor does, and mixes them with the model's; each season's weight on the model is fitted on the archive's earlier seasons only (2016 3%, 2017 12%, 2018 5%, 2019 7%, 2020 5%, 2021 6%). Fitted on all of 2015 to 2021 (15330 games), it is 9%: the live predictor's starting weight.

| Predictor | Log loss |
|---|---|
| Model + simulator | 0.6729 |
| Opening line | 0.6721 |
| Closing line | 0.6702 |
| Model blended with the closing line (walk-forward weight) | 0.6708 |

| Comparison | Mean difference | 95% interval |
|---|---|---|
| Model vs closing line | +0.0027 | +0.0013 to +0.0041 |
| Blend vs closing line | +0.0006 | +0.0002 to +0.0011 |
| Model vs opening line | +0.0008 | -0.0005 to +0.0022 |

### Betting edges at the archived prices

The predictions page's edges, walk-forward: the final prediction's chances (the walk-forward blend, simulated against each line and anchored to the market's own chances), and for comparison the model's own before any blending. A side is an edge at EV of 3% or more per $1, staked at a quarter of the Kelly stake (units are 1% of the bankroll, at most 3 per game). The opening rows blend with, and bet into, the opening moneyline and total; the archive keeps no opening run line. Totals are priced at -110, since the archive does not record which side a total's price belongs to. The ROI range is a 95% bootstrap interval over games.

| Market | Edges | Record (W-L-P) | Staked | Units won | ROI | Expected ROI | 95% range on ROI |
|---|---|---|---|---|---|---|---|
| Run line, closing line, final prediction | 5 | 4-1-0 | 12.0 | +8.01 | +66.8% | +17.2% | -29.4% to +136.4% |
| Moneyline, closing line, final prediction | 10 | 3-7-0 | 11.5 | +4.46 | +38.9% | +17.2% | -80.1% to +137.2% |
| Total (-110 assumed), closing line, final prediction | 1 | 1-0-0 | 1.2 | +1.08 | +90.9% | +3.9% | – |
| Run line, closing line, model only | 5247 | 2602-2645-0 | 5977.1 | -173.17 | -2.9% | +8.4% | -5.7% to -0.1% |
| Moneyline, closing line, model only | 6824 | 2926-3898-0 | 7336.0 | -98.32 | -1.3% | +10.2% | -4.3% to +1.6% |
| Total (-110 assumed), closing line, model only | 6593 | 3265-3002-326 | 11937.8 | -34.45 | -0.3% | +11.7% | -2.8% to +2.2% |
| Moneyline, opening line, final prediction | 7 | 4-3-0 | 9.3 | +8.00 | +86.1% | +18.4% | -47.4% to +297.0% |
| Total (-110 assumed), opening line, final prediction | 4 | 3-1-0 | 4.0 | +1.81 | +44.8% | +3.6% | -54.0% to +90.9% |
| Moneyline, opening line, model only | 4721 | 2122-2598-1 | 6231.3 | +129.80 | +2.1% | +10.1% | -1.5% to +5.8% |
| Total (-110 assumed), opening line, model only | 6567 | 3387-2870-310 | 13726.1 | +466.08 | +3.4% | +11.7% | +1.0% to +5.8% |


## Win-probability calibration

| Predicted home win | Games | Mean predicted | Actual |
|---|---|---|---|
| 20-30% | 101 | 27.9% | 29.7% |
| 30-40% | 1487 | 36.6% | 37.8% |
| 40-50% | 6456 | 45.8% | 45.3% |
| 50-60% | 9880 | 54.8% | 54.8% |
| 60-70% | 4651 | 63.9% | 63.9% |
| 70-80% | 585 | 72.8% | 74.2% |
| 80-90% | 8 | 82.3% | 37.5% |

## Score distribution checks

| Check | Simulator | Actual |
|---|---|---|
| Runs per game, both teams | 9.08 | 9.03 |
| Team shut out | 6.2% | 6.2% |
| Decided by one run | 28.2% | 27.8% |
| Extra innings (regular season) | 8.5% | 8.5% |
| Home team skips the bottom of the ninth | 45.1% | 44.7% |
| Walk-off win | 8.2% | 8.5% |
| Home team wins by 2+ | 36.5% | 36.6% |

Each team's runs scored against its full simulated distribution (ranked probability score, lower is better), next to a plain Poisson and a negative binomial (variance 2.26 times the mean, the league-wide ratio) with the same expected runs:

| Simulator | Negative binomial | Poisson |
|---|---|---|
| 0.0568 | 0.0568 | 0.0587 |

- 80% ranges contained the team's actual runs 85.7% of the time (runs are whole numbers, so a range covers a little more than 80%).
- Headline score exactly right: 2.5% of games.

## Posted lineups against projected ones

On 7420 games, log loss with the actual lineups is 0.6792; with each team's lineup projected from its last game against a starter of the same hand (what a morning run uses) it is 0.6791 (difference -0.0001, 95% interval -0.0006 to +0.0004).
