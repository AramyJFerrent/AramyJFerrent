# Walk-forward backtest

Seasons 2016–2025. Every game is predicted using only earlier weeks of its season plus the preseason prior, with the prior regression, points map, market blend and simulator fitted on earlier seasons only. Benchmarks are scored on the same games.

## FBS vs FBS, 2016–2025

| Predictor | Games | Margin MAE | Margin RMSE | Total MAE | Team-score MAE | Brier | Log loss | Winners |
|---|---|---|---|---|---|---|---|---|
| Final (model + market + sim) | 7270 | 12.29 | 15.58 | 12.85 | 8.98 | 0.173 | 0.515 | 73.5% |
| Model only | 7270 | 12.85 | 16.21 | 13.31 | 9.35 | 0.180 | 0.533 | 72.3% |
| Elo baseline | 7270 | 13.42 | 16.90 | 14.04 | 9.85 | 0.188 | 0.554 | 70.6% |
| Closing line | 7270 | 12.28 | 15.58 | 12.85 | 8.97 | 0.172 | 0.514 | 73.3% |

## All games with a line (FCS opponents included), 2016–2025

| Predictor | Games | Margin MAE | Margin RMSE | Total MAE | Team-score MAE | Brier | Log loss | Winners |
|---|---|---|---|---|---|---|---|---|
| Final (model + market + sim) | 8284 | 12.27 | 15.53 | 12.82 | 8.93 | 0.157 | 0.472 | 76.0% |
| Model only | 8284 | 12.96 | 16.34 | 13.29 | 9.36 | 0.164 | 0.492 | 75.0% |
| Elo baseline | 8284 | 13.62 | 17.13 | 13.96 | 9.87 | 0.172 | 0.513 | 73.4% |
| Closing line | 8284 | 12.26 | 15.53 | 12.82 | 8.93 | 0.157 | 0.472 | 75.9% |

## FBS vs FBS, 2021–2025 (seasons not used for tuning)

| Predictor | Games | Margin MAE | Margin RMSE | Total MAE | Team-score MAE | Brier | Log loss | Winners |
|---|---|---|---|---|---|---|---|---|
| Final (model + market + sim) | 3864 | 12.13 | 15.29 | 12.50 | 8.76 | 0.177 | 0.527 | 72.7% |
| Model only | 3864 | 12.73 | 15.97 | 12.99 | 9.14 | 0.185 | 0.546 | 71.2% |
| Elo baseline | 3864 | 13.30 | 16.69 | 13.54 | 9.57 | 0.192 | 0.564 | 69.4% |
| Closing line | 3864 | 12.12 | 15.29 | 12.51 | 8.75 | 0.177 | 0.526 | 72.5% |

## By kind of game

Mean absolute error in points on games with a closing line.

| Segment | Games | Model margin | Final margin | Line margin | Elo margin | Final total | Line total |
|---|---|---|---|---|---|---|---|
| FBS vs FBS | 7270 | 12.85 | 12.29 | 12.28 | 13.42 | 12.85 | 12.85 |
| FBS vs FCS | 1014 | 13.78 | 12.14 | 12.09 | 15.08 | 12.57 | 12.61 |
| Weeks 1-4 | 1850 | 13.15 | 12.39 | 12.37 | 13.99 | 12.89 | 12.89 |
| Week 5 to end of regular season | 5286 | 12.73 | 12.26 | 12.26 | 13.21 | 12.82 | 12.82 |
| Bowls and playoff | 134 | 13.63 | 11.93 | 11.90 | 13.63 | 13.46 | 13.51 |
| Power 4 vs Power 4 | 3234 | 12.69 | 12.28 | 12.28 | 13.19 | 12.72 | 12.73 |
| Group of 5 vs Group of 5 | 3069 | 12.89 | 12.32 | 12.31 | 13.31 | 13.16 | 13.17 |
| Power 4 vs Group of 5 | 967 | 13.25 | 12.22 | 12.19 | 14.55 | 12.29 | 12.26 |
| Conference games | 5224 | 12.68 | 12.24 | 12.24 | 13.17 | 12.81 | 12.81 |
| Nonconference games | 2046 | 13.28 | 12.41 | 12.39 | 14.06 | 12.95 | 12.94 |

## Is the difference real?

Paired bootstrap of the per-game absolute margin error, FBS vs FBS games (negative favors the first).

| Comparison | Mean difference | 95% interval |
|---|---|---|
| Final vs closing line | +0.007 | -0.003 to +0.016 |
| Model only vs Elo | -0.569 | -0.673 to -0.467 |
| Model only vs closing line | +0.570 | +0.465 to +0.669 |

## Betting edges against closing lines

The model's own numbers (no market blend), run through the same score simulator, priced at the consensus closing line on every game with one. A bet is an edge when its expected value is at least 3% per unit staked; one unit on each, pushes returning the stake. Prices are the median of the books quoting the consensus line; the odds file has spread and total prices only through 2019, so later seasons are scored at an assumed -110 and shown separately. The 95% range on ROI is a bootstrap over bets.

| Market | Prices | Seasons | Games priced | Edges | Record (W-L-P) | Units | ROI | 95% range |
|---|---|---|---|---|---|---|---|---|
| Spread | posted | 2016–2019 | 2876 | 2089 | 1008-1037-44 | -116.0 | -5.6% | -9.5% to -1.5% |
| Spread | assumed -110 | 2016–2025 | 5408 | 4069 | 2005-1993-71 | -170.3 | -4.2% | -6.9% to -1.2% |
| Moneyline | posted | 2016–2025 | 7072 | 4463 | 1659-2804-0 | +332.8 | +7.5% | -9.4% to +35.4% |
| Total | posted | 2016–2019 | 3196 | 2367 | 1204-1137-26 | -40.6 | -1.7% | -5.2% to +2.0% |
| Total | assumed -110 | 2016–2025 | 5088 | 3693 | 1928-1722-43 | +30.7 | +0.8% | -2.2% to +3.8% |

## Win-probability calibration

| Predicted | Games | Mean predicted | Actual |
|---|---|---|---|
| 0-10% | 284 | 5.3% | 8.8% |
| 10-20% | 459 | 15.7% | 14.2% |
| 20-30% | 514 | 25.0% | 23.7% |
| 30-40% | 754 | 34.8% | 35.9% |
| 40-50% | 830 | 43.7% | 46.3% |
| 50-60% | 974 | 56.3% | 54.7% |
| 60-70% | 954 | 65.3% | 68.3% |
| 70-80% | 775 | 75.0% | 76.5% |
| 80-90% | 964 | 84.9% | 86.7% |
| 90-100% | 1776 | 96.7% | 96.6% |

## Score distribution checks

- 80% ranges contained the team's actual score 82.3% of the time.
- Predicted chance of a one-score game (8 or fewer): 33.7%; actual: 34.3%.
- Headline score exactly right: 0.6% of games.
