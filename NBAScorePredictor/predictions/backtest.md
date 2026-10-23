# Walk-forward backtest

Seasons 2015-16 to 2025-26. Every game is predicted using only earlier days of its season plus the preseason priors, with the points map, blend and simulator fitted on earlier seasons only. Who played is known (the final injury report); minutes are projected. Benchmarks are scored on the same games, all of which have an archived closing line.

## 2015-16 to 2025-26

| Predictor | Games | Margin MAE | Margin RMSE | Total MAE | Team-points MAE | Log loss | Brier | Winners |
|---|---|---|---|---|---|---|---|---|
| Final (model + market + simulator) | 13332 | 10.12 | 12.97 | 14.22 | 8.82 | 0.600 | 0.207 | 67.6% |
| Model only | 13332 | 10.29 | 13.14 | 14.47 | 8.95 | 0.607 | 0.210 | 67.0% |
| Team ratings only | 13332 | 10.51 | 13.41 | 14.59 | 9.07 | 0.623 | 0.217 | 65.3% |
| Elo | 13332 | 10.53 | 13.44 | 15.84 | 9.58 | 0.624 | 0.217 | 65.0% |
| Closing line | 13332 | 10.11 | 12.97 | 14.20 | 8.81 | 0.600 | 0.207 | 67.7% |

## 2016-17 on (seasons not used for tuning)

| Predictor | Games | Margin MAE | Margin RMSE | Total MAE | Team-points MAE | Log loss | Brier | Winners |
|---|---|---|---|---|---|---|---|---|
| Final (model + market + simulator) | 12016 | 10.21 | 13.10 | 14.28 | 8.86 | 0.603 | 0.208 | 67.4% |
| Model only | 12016 | 10.39 | 13.27 | 14.54 | 9.00 | 0.611 | 0.211 | 66.6% |
| Team ratings only | 12016 | 10.62 | 13.55 | 14.67 | 9.13 | 0.627 | 0.219 | 64.9% |
| Elo | 12016 | 10.64 | 13.58 | 15.92 | 9.63 | 0.628 | 0.219 | 64.5% |
| Closing line | 12016 | 10.20 | 13.10 | 14.26 | 8.85 | 0.603 | 0.208 | 67.4% |

## 2020-21 on (the report's test seasons)

| Predictor | Games | Margin MAE | Margin RMSE | Total MAE | Team-points MAE | Log loss | Brier | Winners |
|---|---|---|---|---|---|---|---|---|
| Final (model + market + simulator) | 6940 | 10.50 | 13.44 | 14.23 | 8.92 | 0.604 | 0.209 | 67.3% |
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
| Final vs closing line | +0.014 | +0.002 to +0.025 |

## Win-probability calibration

| Predicted home win | Games | Mean predicted | Actual |
|---|---|---|---|
| 0-10% | 18 | 8.5% | 5.6% |
| 10-20% | 334 | 16.3% | 11.1% |
| 20-30% | 1079 | 25.5% | 22.6% |
| 30-40% | 1829 | 35.3% | 35.7% |
| 40-50% | 1903 | 44.5% | 45.6% |
| 50-60% | 2140 | 55.8% | 54.4% |
| 60-70% | 2922 | 65.0% | 65.7% |
| 70-80% | 2411 | 74.6% | 75.5% |
| 80-90% | 1372 | 84.1% | 85.0% |
| 90-100% | 160 | 92.0% | 94.4% |

## Score distribution checks

- 80% ranges contained each team's points 81.4% of the time, the margin 80.6% and the total 81.3%.
- Overtime (regular season): predicted 5.1%, actual 5.4%.
- Spread of real results around the prediction: margin 13.1 points, total 18.0.
- The headline score picked the winner 67.7% of the time.

## Betting edges

Every side of each market is checked for expected value with the final prediction's chances (the model blended with the line being bet, by the weights fitted on earlier seasons, simulated and anchored to the market's own chances), and the best side is bet whenever its EV is 3% or more, at 25% of the Kelly stake with at most 3 units (1% of the bankroll each) on one game. The model-only rows price the same bets with the model's own simulated scores before the blend, the rule the predictor used before, for comparison. The archives carry moneylines but no spread or total prices, so those are assumed to be -110 on both sides. ROI is units won per unit staked, with a 95% bootstrap range over games; expected ROI is what the edges' EVs promised.

| Lines | Chances | Market | Edges | Record (W-L-P) | Staked | Units won | ROI | 95% range | Expected ROI | Line moved toward the edge |
|---|---|---|---|---|---|---|---|---|---|---|
| Closing line | final prediction | Spread | 800 | 403-390-7 | 1060.8 | -36.9 | -3.5% | -10.3% to +3.4% | +6.4% | – |
| Closing line | final prediction | Moneyline | 1973 | 627-1346-0 | 1418.8 | +162.5 | +11.5% | +3.4% to +19.1% | +9.9% | – |
| Closing line | final prediction | Total | 526 | 267-253-6 | 769.9 | -13.0 | -1.7% | -10.4% to +6.7% | +6.9% | – |
| Opening line, 2015-16 to 2021-22, knowing who played | final prediction | Spread | 775 | 417-344-14 | 1244.3 | +53.5 | +4.3% | -2.9% to +11.4% | +7.4% | 76.1% of 694 |
| Opening line, 2015-16 to 2021-22, knowing who played | final prediction | Moneyline | no historical prices | | | | | | | |
| Opening line, 2015-16 to 2021-22, knowing who played | final prediction | Total | 595 | 333-255-7 | 899.9 | +74.2 | +8.2% | +0.0% to +16.4% | +6.9% | – |
| Closing line, same games | final prediction | Spread | 689 | 347-337-5 | 923.0 | -39.6 | -4.3% | -11.8% to +3.0% | +6.6% | – |
| Closing line, same games | final prediction | Moneyline | 1420 | 468-952-0 | 1133.5 | +110.4 | +9.7% | +0.8% to +18.8% | +10.4% | – |
| Closing line, same games | final prediction | Total | 525 | 266-253-6 | 768.9 | -13.9 | -1.8% | -11.0% to +6.7% | +7.0% | – |
| Opening line, 2015-16 to 2021-22, assuming each team's previous lineup | final prediction | Spread | 479 | 244-225-10 | 722.9 | +6.7 | +0.9% | -8.3% to +9.8% | +6.8% | 60.7% of 425 |
| Opening line, 2015-16 to 2021-22, assuming each team's previous lineup | final prediction | Moneyline | no historical prices | | | | | | | |
| Opening line, 2015-16 to 2021-22, assuming each team's previous lineup | final prediction | Total | 283 | 158-124-1 | 386.6 | +32.0 | +8.3% | -3.2% to +19.9% | +5.8% | – |
| Closing line | model only | Spread | 7932 | 3947-3863-122 | 9861.1 | -351.4 | -3.6% | -5.8% to -1.4% | +13.4% | – |
| Closing line | model only | Moneyline | 8838 | 3136-5702-0 | 8987.8 | +256.9 | +2.9% | -0.5% to +6.2% | +24.5% | – |
| Closing line | model only | Total | 8134 | 4036-3996-102 | 13075.7 | -603.1 | -4.6% | -6.9% to -2.3% | +14.6% | – |
| Opening line, 2015-16 to 2021-22, knowing who played | model only | Spread | 5229 | 2703-2437-89 | 9604.7 | +95.0 | +1.0% | -1.9% to +3.8% | +14.7% | 71.8% of 4485 |
| Opening line, 2015-16 to 2021-22, knowing who played | model only | Moneyline | no historical prices | | | | | | | |
| Opening line, 2015-16 to 2021-22, knowing who played | model only | Total | 5341 | 2884-2397-60 | 9765.8 | +465.8 | +4.8% | +2.0% to +7.5% | +14.3% | – |
| Closing line, same games | model only | Spread | 5036 | 2482-2469-85 | 6295.0 | -316.4 | -5.0% | -7.8% to -2.3% | +12.9% | – |
| Closing line, same games | model only | Moneyline | 5733 | 2056-3677-0 | 5914.9 | +179.1 | +3.0% | -1.1% to +7.2% | +23.7% | – |
| Closing line, same games | model only | Total | 5198 | 2557-2566-75 | 8348.2 | -474.3 | -5.7% | -8.5% to -2.8% | +13.5% | – |
| Opening line, 2015-16 to 2021-22, assuming each team's previous lineup | model only | Spread | 5146 | 2655-2403-88 | 9469.0 | +25.5 | +0.3% | -2.4% to +3.0% | +14.9% | 62.6% of 4396 |
| Opening line, 2015-16 to 2021-22, assuming each team's previous lineup | model only | Moneyline | no historical prices | | | | | | | |
| Opening line, 2015-16 to 2021-22, assuming each team's previous lineup | model only | Total | 5249 | 2777-2415-57 | 9553.1 | +296.1 | +3.1% | +0.3% to +5.9% | +14.0% | – |

## Knowing who plays

- Model-only margin MAE 10.288 knowing who played, 10.355 assuming each team's previous lineup (difference +0.067, 95% interval +0.035 to +0.099).
- Final prediction 10.120 against 10.113 with the same closing lines.
