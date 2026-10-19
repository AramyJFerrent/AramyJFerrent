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

## Model picks against the spread

Picking a side whenever the model's own spread and the line differ by 1 point or more. Break-even at standard -110 prices is 52.4%.

| Picks against | Record (W-L-P) | Cover rate | 95% range | Line moved toward the pick |
|---|---|---|---|---|
| Closing line | 4447-4465-131 | 49.9% | 48.9%–50.9% | – |
| Opening line, 2015-16 to 2021-22, knowing who played | 2984-2774-97 | 51.8% | 50.5%–53.1% | 68.0% of 4964 |
| Closing line, same games | 2811-2862-97 | 49.6% | 48.2%–50.9% | – |
| Opening line, 2015-16 to 2021-22, assuming each team's previous lineup | 2926-2743-94 | 51.6% | 50.3%–52.9% | 59.0% of 4860 |

## Knowing who plays

- Model-only margin MAE 10.288 knowing who played, 10.355 assuming each team's previous lineup (difference +0.067, 95% interval +0.035 to +0.099).
- Final prediction 10.122 against 10.114 with the same closing lines.
