# Walk-forward backtest

Seasons 2016 to 2025, postseason included. Every game is predicted using only earlier days' results (player and team ratings, with park factors from earlier seasons), with the run model and simulator fitted on the three seasons before. Lineups and starting pitchers are the actual ones, as a game-day run knows them once lineups post; weather is the recorded game-time weather. Baselines are scored on the same games.

## 2016 to 2025

| Predictor | Games | Log loss | Brier | Winners | Runs MAE | Total MAE |
|---|---|---|---|---|---|---|
| Model + simulator | 23168 | 0.6744 | 0.2408 | 57.9% | 2.45 | 3.53 |
| Elo with starting pitchers | 23168 | 0.6754 | 0.2413 | 57.6% | – | – |
| Team runs ratings only | 23168 | 0.6785 | 0.2428 | 56.8% | – | – |
| Home team every time | 23168 | 0.6910 | 0.2489 | 53.3% | – | – |

## 2021 on

| Predictor | Games | Log loss | Brier | Winners | Runs MAE | Total MAE |
|---|---|---|---|---|---|---|
| Model + simulator | 12356 | 0.6758 | 0.2415 | 57.7% | 2.44 | 3.51 |
| Elo with starting pitchers | 12356 | 0.6765 | 0.2418 | 57.6% | – | – |
| Team runs ratings only | 12356 | 0.6785 | 0.2428 | 56.8% | – | – |
| Home team every time | 12356 | 0.6912 | 0.2490 | 53.1% | – | – |

## Is the difference real?

Paired bootstrap of the per-game log loss (negative favors the first).

| Comparison | Mean difference | 95% interval |
|---|---|---|
| Model vs Elo with starting pitchers | -0.0010 | -0.0018 to -0.0002 |
| Model vs team runs ratings only | -0.0041 | -0.0054 to -0.0029 |

## Against the betting market, 2016

Pinnacle's complete 2016 line history (2461 games), de-vigged. The blend backs each team's expected runs out of the closing moneyline and total through the simulator and mixes them with the model's on the log scale, 22% model; that weight, fitted on these games, is where the live predictor's blend starts.

| Predictor | Log loss | Brier | Total MAE |
|---|---|---|---|
| Model + simulator | 0.6762 | 0.2416 | 3.48 |
| Elo with starting pitchers | 0.6787 | – | – |
| Opening line | 0.6770 | – | – |
| Closing line | 0.6735 | 0.2403 | 3.46 |
| Model blended with the closing line | 0.6734 | 0.2403 | 3.49 |

| Comparison | Mean difference | 95% interval |
|---|---|---|
| Model vs closing line | +0.0027 | -0.0003 to +0.0058 |
| Blend vs closing line | -0.0001 | -0.0013 to +0.0012 |
| Model vs opening line | -0.0008 | -0.0035 to +0.0019 |

## Win-probability calibration

| Predicted home win | Games | Mean predicted | Actual |
|---|---|---|---|
| 10-20% | 2 | 19.2% | 50.0% |
| 20-30% | 98 | 27.8% | 25.5% |
| 30-40% | 1520 | 36.7% | 38.0% |
| 40-50% | 6477 | 45.8% | 44.9% |
| 50-60% | 9859 | 54.8% | 55.0% |
| 60-70% | 4591 | 63.9% | 64.3% |
| 70-80% | 611 | 72.8% | 73.3% |
| 80-90% | 10 | 82.7% | 50.0% |

## Score distribution checks

| Check | Simulator | Actual |
|---|---|---|
| Runs per game, both teams | 9.08 | 9.03 |
| Team shut out | 6.2% | 6.2% |
| Decided by one run | 28.2% | 27.8% |
| Extra innings (regular season) | 8.5% | 8.5% |
| Home team skips the bottom of the ninth | 45.2% | 44.7% |
| Walk-off win | 8.2% | 8.5% |
| Home team wins by 2+ | 36.5% | 36.6% |

Each team's runs scored against its full simulated distribution (ranked probability score, lower is better), next to a plain Poisson and a negative binomial (variance 2.26 times the mean, the league-wide ratio) with the same expected runs:

| Simulator | Negative binomial | Poisson |
|---|---|---|
| 0.0568 | 0.0568 | 0.0587 |

- 80% ranges contained the team's actual runs 85.7% of the time (runs are whole numbers, so a range covers a little more than 80%).
- Headline score exactly right: 2.7% of games.

## Posted lineups against projected ones

On 7420 games, log loss with the actual lineups is 0.6788; with each team's lineup projected from its last game against a starter of the same hand (what a morning run uses) it is 0.6790 (difference +0.0002, 95% interval -0.0003 to +0.0007).
