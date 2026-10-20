# Walk-forward backtest

Seasons 2015–2025. Every game is predicted using only earlier weeks of its season plus the preseason prior, with the points map, market blend and simulator fitted on earlier seasons only. Benchmarks are scored on the same games.

## 2015–2025

| Predictor | Games | Margin MAE | Margin RMSE | Total MAE | Team-score MAE | Brier | Log loss | Winners |
|---|---|---|---|---|---|---|---|---|
| Final (model + market + sim) | 3028 | 9.82 | 12.72 | 10.43 | 7.27 | 0.212 | 0.61 | 66.0% |
| Model only | 3028 | 10.07 | 13.00 | 10.75 | 7.47 | 0.220 | 0.63 | 64.6% |
| Elo baseline | 3028 | 10.18 | 13.11 | 10.98 | 7.59 | 0.221 | 0.64 | 64.3% |
| Closing line | 3028 | 9.81 | 12.72 | 10.44 | 7.27 | 0.212 | 0.61 | 66.0% |

## 2019–2025 (seasons not used for tuning)

| Predictor | Games | Margin MAE | Margin RMSE | Total MAE | Team-score MAE | Brier | Log loss | Winners |
|---|---|---|---|---|---|---|---|---|
| Final (model + market + sim) | 1960 | 9.84 | 12.74 | 10.36 | 7.26 | 0.211 | 0.61 | 66.2% |
| Model only | 1960 | 10.14 | 13.08 | 10.64 | 7.46 | 0.220 | 0.63 | 64.5% |
| Elo baseline | 1960 | 10.20 | 13.14 | 10.95 | 7.60 | 0.222 | 0.64 | 63.8% |
| Closing line | 1960 | 9.82 | 12.72 | 10.38 | 7.26 | 0.210 | 0.61 | 66.3% |

## Is the difference real?

Paired bootstrap of the per-game absolute margin error (negative favors the first).

| Comparison | Mean difference | 95% interval |
|---|---|---|
| Final vs closing line | +0.009 | -0.017 to +0.036 |
| Model only vs Elo | -0.102 | -0.197 to -0.008 |
| Model only vs closing line | +0.267 | +0.170 to +0.364 |

## Betting edges

Each side of each market priced with the model alone (its own expected points run through the score simulator, before any blend with the line), betting one unit on the best side whenever its expected value is at least +3% at the price. Pushes return the stake. Starting QBs here are each team's previous starter, so nothing is used that a Wednesday line could not know. Closing lines and prices come from the nflverse schedule; the Wednesday lines (Westgate SuperContest) carry no prices, so -110 is assumed for them. The ROI range is a 95% bootstrap over bets.

| Market | Lines | Edges | Record (W-L-P) | Units | ROI | 95% range | Line moved toward edge by kickoff |
|---|---|---|---|---|---|---|---|
| Spread | Wednesday, 2015–2020 (-110 assumed) | 1032 | 537-466-29 | +22.2 | +2.1% | -3.7% to +7.8% | 48.7% of 788 |
| Spread | closing, same 2015–2020 games | 1195 | 622-543-30 | +50.0 | +4.2% | -1.2% to +9.6% | – |
| Spread | closing, 2015–2025 | 2288 | 1156-1075-57 | +15.4 | +0.7% | -3.2% to +4.5% | – |
| Moneyline | closing, 2015–2025 | 2320 | 822-1492-6 | -102.4 | -4.4% | -10.3% to +1.6% | – |
| Total | closing, 2015–2025 | 2197 | 1081-1096-20 | -73.6 | -3.3% | -7.5% to +0.7% | – |
| Moneyline | Wednesday, 2015–2020 | no historical prices | | | | | |
| Total | Wednesday, 2015–2020 | no historical prices | | | | | |

## Win-probability calibration

| Predicted | Games | Mean predicted | Actual |
|---|---|---|---|
| 0-10% | 1 | 10.0% | 0.0% |
| 10-20% | 43 | 16.0% | 18.6% |
| 20-30% | 152 | 26.4% | 21.7% |
| 30-40% | 360 | 35.7% | 27.5% |
| 40-50% | 569 | 44.1% | 45.3% |
| 50-60% | 631 | 56.5% | 54.0% |
| 60-70% | 690 | 64.6% | 66.4% |
| 70-80% | 413 | 74.3% | 75.7% |
| 80-90% | 149 | 84.6% | 91.3% |
| 90-100% | 20 | 92.0% | 90.0% |

## Score distribution checks

- 80% ranges contained the team's actual score 82.6% of the time.
- Predicted chance of a one-score game (8 or fewer): 50.8%; actual: 53.2%.
- Headline score exactly right: 1.4% of games.
