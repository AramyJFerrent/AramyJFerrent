# Walk-forward backtest

Seasons 2015-16 to 2025-26. Every game is predicted using only earlier days of its season plus the preseason priors, with the points map, blend and simulator fitted on earlier seasons only. Who played is known (the final injury report); minutes are projected. Benchmarks are scored on the same games, all of which have an archived closing line.

## 2015-16 to 2025-26

| Predictor | Games | Margin MAE | Margin RMSE | Total MAE | Team-points MAE | Log loss | Brier | Winners |
|---|---|---|---|---|---|---|---|---|
| Final (model + market + simulator) | 13332 | 10.12 | 12.97 | 14.22 | 8.82 | 0.600 | 0.207 | 67.5% |
| Model only | 13332 | 10.29 | 13.14 | 14.47 | 8.95 | 0.607 | 0.210 | 67.0% |
| Team ratings only | 13332 | 10.51 | 13.41 | 14.59 | 9.07 | 0.623 | 0.217 | 65.3% |
| Elo | 13332 | 10.53 | 13.44 | 15.84 | 9.58 | 0.624 | 0.217 | 65.0% |
| Closing line | 13332 | 10.11 | 12.97 | 14.20 | 8.81 | 0.600 | 0.207 | 67.7% |

## 2016-17 on (seasons not used for tuning)

| Predictor | Games | Margin MAE | Margin RMSE | Total MAE | Team-points MAE | Log loss | Brier | Winners |
|---|---|---|---|---|---|---|---|---|
| Final (model + market + simulator) | 12016 | 10.22 | 13.10 | 14.28 | 8.86 | 0.604 | 0.208 | 67.3% |
| Model only | 12016 | 10.39 | 13.27 | 14.54 | 9.00 | 0.611 | 0.211 | 66.6% |
| Team ratings only | 12016 | 10.62 | 13.55 | 14.67 | 9.13 | 0.627 | 0.219 | 64.9% |
| Elo | 12016 | 10.64 | 13.58 | 15.92 | 9.63 | 0.628 | 0.219 | 64.5% |
| Closing line | 12016 | 10.20 | 13.10 | 14.26 | 8.85 | 0.603 | 0.208 | 67.4% |

## 2020-21 on (the report's test seasons)

| Predictor | Games | Margin MAE | Margin RMSE | Total MAE | Team-points MAE | Log loss | Brier | Winners |
|---|---|---|---|---|---|---|---|---|
| Final (model + market + simulator) | 6940 | 10.51 | 13.44 | 14.23 | 8.92 | 0.604 | 0.209 | 67.2% |
| Model only | 6940 | 10.69 | 13.63 | 14.56 | 9.10 | 0.611 | 0.212 | 66.5% |
| Team ratings only | 6940 | 10.97 | 13.96 | 14.69 | 9.24 | 0.630 | 0.220 | 64.7% |
| Elo | 6940 | 11.00 | 14.01 | 15.85 | 9.71 | 0.633 | 0.221 | 64.3% |
| Closing line | 6940 | 10.50 | 13.44 | 14.22 | 8.91 | 0.605 | 0.209 | 67.5% |

## Is the difference real?

Paired bootstrap of the per-game absolute margin error (negative favors the first).

| Comparison | Mean difference | 95% interval |
|---|---|---|
| Model only vs closing line | +0.182 | +0.141 to +0.223 |
| Model only vs team ratings only | -0.227 | -0.271 to -0.183 |
| Final vs closing line | +0.016 | +0.003 to +0.028 |

## Win-probability calibration

| Predicted home win | Games | Mean predicted | Actual |
|---|---|---|---|
| 0-10% | 18 | 8.5% | 5.6% |
| 10-20% | 327 | 16.3% | 10.7% |
| 20-30% | 1076 | 25.5% | 22.7% |
| 30-40% | 1811 | 35.3% | 35.7% |
| 40-50% | 1939 | 44.5% | 45.3% |
| 50-60% | 2144 | 55.8% | 54.6% |
| 60-70% | 2935 | 65.0% | 65.7% |
| 70-80% | 2390 | 74.6% | 75.6% |
| 80-90% | 1369 | 84.1% | 85.0% |
| 90-100% | 159 | 92.0% | 94.3% |

## Score distribution checks

- 80% ranges contained each team's points 81.4% of the time, the margin 80.7% and the total 81.3%.
- Overtime (regular season): predicted 5.1%, actual 5.4%.
- Spread of real results around the prediction: margin 13.1 points, total 18.0.
- The headline score picked the winner 67.6% of the time.

## Betting edges

Every side of each market is checked for expected value with the model's own chances (its simulated scores before blending with the line), and the best side is bet, 1 unit flat, whenever its EV is 3% or more. The archives carry moneylines but no spread or total prices, so those are assumed to be -110 on both sides. ROI is units won per unit bet, with a 95% bootstrap range over the bets.

| Lines | Market | Edges | Record (W-L-P) | Units | ROI | 95% range | Line moved toward the edge |
|---|---|---|---|---|---|---|---|
| Closing line | Spread | 7928 | 3946-3862-120 | -274.7 | -3.5% | -5.5% to -1.3% | – |
| Closing line | Moneyline | 8837 | 3137-5700-0 | +119.2 | +1.3% | -2.2% to +4.9% | – |
| Closing line | Total | 8133 | 4036-3995-102 | -325.9 | -4.0% | -6.1% to -2.0% | – |
| Opening line, 2015-16 to 2021-22, knowing who played | Spread | 5225 | 2700-2436-89 | +18.5 | +0.4% | -2.3% to +2.8% | 71.8% of 4482 |
| Opening line, 2015-16 to 2021-22, knowing who played | Moneyline | no historical prices | | | | | |
| Opening line, 2015-16 to 2021-22, knowing who played | Total | 5342 | 2884-2398-60 | +223.8 | +4.2% | +1.7% to +6.9% | – |
| Closing line, same games | Spread | 5035 | 2483-2469-83 | -211.7 | -4.2% | -6.9% to -1.7% | – |
| Closing line, same games | Moneyline | 5732 | 2057-3675-0 | +93.4 | +1.6% | -2.8% to +6.1% | – |
| Closing line, same games | Total | 5197 | 2557-2565-75 | -240.5 | -4.6% | -7.2% to -2.2% | – |
| Opening line, 2015-16 to 2021-22, assuming each team's previous lineup | Spread | 5151 | 2656-2407-88 | +7.5 | +0.1% | -2.3% to +2.8% | 62.6% of 4401 |
| Opening line, 2015-16 to 2021-22, assuming each team's previous lineup | Moneyline | no historical prices | | | | | |
| Opening line, 2015-16 to 2021-22, assuming each team's previous lineup | Total | 5249 | 2778-2414-57 | +111.5 | +2.1% | -0.4% to +4.7% | – |

## Knowing who plays

- Model-only margin MAE 10.288 knowing who played, 10.355 assuming each team's previous lineup (difference +0.067, 95% interval +0.035 to +0.099).
- Final prediction 10.122 against 10.114 with the same closing lines.
