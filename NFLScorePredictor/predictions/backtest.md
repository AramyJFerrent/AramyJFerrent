# Walk-forward backtest

Seasons 2015–2025. Every game is predicted using only earlier weeks of its season plus the preseason prior, with the points map, market blend and simulator fitted on earlier seasons only. Benchmarks are scored on the same games.

## 2015–2025

| Predictor | Games | Margin MAE | Margin RMSE | Total MAE | Team-score MAE | Brier | Log loss | Winners |
|---|---|---|---|---|---|---|---|---|
| Final (model + market + sim) | 3028 | 9.81 | 12.72 | 10.43 | 7.26 | 0.212 | 0.61 | 66.0% |
| Model only | 3028 | 10.05 | 12.96 | 10.75 | 7.46 | 0.219 | 0.63 | 64.6% |
| Elo baseline | 3028 | 10.18 | 13.11 | 10.98 | 7.59 | 0.221 | 0.64 | 64.3% |
| Closing line | 3028 | 9.81 | 12.72 | 10.44 | 7.27 | 0.212 | 0.61 | 66.0% |

## 2019–2025 (seasons not used for tuning)

| Predictor | Games | Margin MAE | Margin RMSE | Total MAE | Team-score MAE | Brier | Log loss | Winners |
|---|---|---|---|---|---|---|---|---|
| Final (model + market + sim) | 1960 | 9.83 | 12.73 | 10.36 | 7.26 | 0.211 | 0.61 | 66.2% |
| Model only | 1960 | 10.11 | 13.03 | 10.65 | 7.45 | 0.219 | 0.63 | 64.2% |
| Elo baseline | 1960 | 10.20 | 13.14 | 10.95 | 7.60 | 0.222 | 0.64 | 63.8% |
| Closing line | 1960 | 9.82 | 12.72 | 10.38 | 7.26 | 0.210 | 0.61 | 66.3% |

## Is the difference real?

Paired bootstrap of the per-game absolute margin error (negative favors the first).

| Comparison | Mean difference | 95% interval |
|---|---|---|
| Final vs closing line | +0.001 | -0.017 to +0.019 |
| Model only vs Elo | -0.125 | -0.221 to -0.027 |
| Model only vs closing line | +0.245 | +0.148 to +0.342 |

## Betting edges

Each side of each market priced with the final prediction (the model blended with the line being bet, by the weight fitted on earlier seasons, run through the score simulator), betting the best side whenever its expected value is at least +3% at the price, at 25% of the Kelly stake with at most 3 units (1% of the bankroll each) on one game. Pushes return the stake. Starting QBs here are each team's previous starter, so nothing is used that a Wednesday line could not know. Closing lines and prices come from the nflverse schedule. The Wednesday lines (Westgate SuperContest spreads) and the opening spreads and totals (sportsbookreview's archive, matched by date, teams and final score) carry no prices, so -110 is assumed for them; the opening moneyline is not archived. ROI is units won per unit staked, with a 95% bootstrap range over games; expected ROI is what the edges' EVs promised, so a gap between the two shows how far the chances behind the edges are off. The model-only rows price the same bets with the model before the blend, the rule the predictor used before, for comparison.

| Market | Lines | Chances | Edges | Record (W-L-P) | Staked | Units won | ROI | 95% range | Expected ROI | Line moved toward edge by kickoff |
|---|---|---|---|---|---|---|---|---|---|---|
| Spread | Wednesday, 2015–2020 (-110 assumed) | final | 39 | 14-23-2 | 56.2 | -16.0 | -28.4% | -58.3% to +3.0% | +6.0% | 58.1% of 31 |
| Spread | closing, same 2015–2020 games | final | 118 | 57-59-2 | 148.5 | -16.1 | -10.8% | -28.2% to +7.4% | +5.8% | – |
| Spread | opening, 2015–2021 (-110 assumed) | final | 31 | 17-14-0 | 45.2 | +2.5 | +5.6% | -29.8% to +39.8% | +5.9% | 66.7% of 27 |
| Total | opening, 2015–2021 (-110 assumed) | final | 39 | 19-20-0 | 48.3 | -1.4 | -2.8% | -33.5% to +27.5% | +4.8% | 78.4% of 37 |
| Total | closing, same 2015–2021 games | final | 209 | 112-96-1 | 313.0 | +9.8 | +3.1% | -12.0% to +17.4% | +7.7% | – |
| Spread | closing, 2015–2025 | final | 141 | 67-70-4 | 172.9 | -16.3 | -9.5% | -25.6% to +7.7% | +5.6% | – |
| Moneyline | closing, 2015–2025 | final | 325 | 79-245-1 | 181.3 | -15.3 | -8.4% | -26.3% to +9.9% | +7.3% | – |
| Total | closing, 2015–2025 | final | 299 | 165-131-3 | 473.9 | +37.4 | +7.9% | -3.9% to +19.6% | +8.2% | – |
| Spread | Wednesday, 2015–2020 (-110 assumed) | model only | 1017 | 523-467-27 | 2562.0 | +14.2 | +0.6% | -5.6% to +6.6% | +16.6% | 49.1% of 780 |
| Spread | closing, same 2015–2020 games | model only | 1193 | 623-540-30 | 1427.8 | +48.5 | +3.4% | -2.4% to +9.1% | +18.4% | – |
| Spread | opening, 2015–2021 (-110 assumed) | model only | 1159 | 593-535-31 | 2084.3 | +19.8 | +0.9% | -5.0% to +7.0% | +17.1% | 55.9% of 951 |
| Total | opening, 2015–2021 (-110 assumed) | model only | 1240 | 620-598-22 | 2259.2 | -65.5 | -2.9% | -8.7% to +2.8% | +16.9% | 69.6% of 1121 |
| Total | closing, same 2015–2021 games | model only | 1338 | 657-671-10 | 1878.1 | -61.5 | -3.3% | -9.3% to +2.6% | +17.9% | – |
| Spread | closing, 2015–2025 | model only | 2279 | 1153-1071-55 | 2836.1 | +2.4 | +0.1% | -4.0% to +4.2% | +18.1% | – |
| Moneyline | closing, 2015–2025 | model only | 2329 | 820-1500-9 | 2187.4 | -91.7 | -4.2% | -9.8% to +1.6% | +28.2% | – |
| Total | closing, 2015–2025 | model only | 2206 | 1087-1099-20 | 3096.6 | -73.2 | -2.4% | -7.1% to +2.2% | +17.3% | – |

## Win-probability calibration

| Predicted | Games | Mean predicted | Actual |
|---|---|---|---|
| 0-10% | 2 | 9.8% | 0.0% |
| 10-20% | 44 | 15.7% | 20.5% |
| 20-30% | 151 | 26.3% | 20.5% |
| 30-40% | 375 | 35.5% | 28.3% |
| 40-50% | 560 | 43.7% | 45.2% |
| 50-60% | 615 | 56.7% | 55.2% |
| 60-70% | 682 | 64.5% | 64.8% |
| 70-80% | 425 | 74.2% | 76.4% |
| 80-90% | 149 | 84.5% | 91.9% |
| 90-100% | 25 | 91.8% | 88.0% |

## Score distribution checks

- 80% ranges contained the team's actual score 82.6% of the time.
- Predicted chance of a one-score game (8 or fewer): 50.8%; actual: 53.2%.
- Headline score exactly right: 1.3% of games.
