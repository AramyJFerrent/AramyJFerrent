# Walk-forward backtest

Seasons 2015–2025. Every game is predicted using only earlier weeks of its season plus the preseason prior, with the points map, market blend and simulator fitted on earlier seasons only. Benchmarks are scored on the same games.

## 2015–2025

| Predictor | Games | Margin MAE | Margin RMSE | Total MAE | Team-score MAE | Brier | Log loss | Winners |
|---|---|---|---|---|---|---|---|---|
| Final (model + market + sim) | 3028 | 9.81 | 12.72 | 10.43 | 7.27 | 0.212 | 0.61 | 66.1% |
| Model only | 3028 | 10.09 | 13.03 | 10.74 | 7.48 | 0.220 | 0.63 | 64.3% |
| Elo baseline | 3028 | 10.18 | 13.11 | 10.98 | 7.59 | 0.221 | 0.64 | 64.3% |
| Closing line | 3028 | 9.81 | 12.72 | 10.44 | 7.27 | 0.212 | 0.61 | 66.0% |

## 2019–2025 (seasons not used for tuning)

| Predictor | Games | Margin MAE | Margin RMSE | Total MAE | Team-score MAE | Brier | Log loss | Winners |
|---|---|---|---|---|---|---|---|---|
| Final (model + market + sim) | 1960 | 9.83 | 12.73 | 10.36 | 7.26 | 0.211 | 0.61 | 66.3% |
| Model only | 1960 | 10.14 | 13.10 | 10.64 | 7.47 | 0.220 | 0.63 | 64.1% |
| Elo baseline | 1960 | 10.20 | 13.14 | 10.95 | 7.60 | 0.222 | 0.64 | 63.8% |
| Closing line | 1960 | 9.82 | 12.72 | 10.38 | 7.26 | 0.210 | 0.61 | 66.3% |

## Is the difference real?

Paired bootstrap of the per-game absolute margin error (negative favors the first).

| Comparison | Mean difference | 95% interval |
|---|---|---|
| Final vs closing line | +0.007 | -0.006 to +0.020 |
| Model only vs Elo | -0.089 | -0.188 to +0.010 |
| Model only vs closing line | +0.280 | +0.184 to +0.378 |

## Win-probability calibration

| Predicted | Games | Mean predicted | Actual |
|---|---|---|---|
| 0-10% | 2 | 9.7% | 0.0% |
| 10-20% | 47 | 15.7% | 19.1% |
| 20-30% | 158 | 26.5% | 22.2% |
| 30-40% | 360 | 35.5% | 27.8% |
| 40-50% | 570 | 43.6% | 44.9% |
| 50-60% | 650 | 57.0% | 55.5% |
| 60-70% | 656 | 64.8% | 65.9% |
| 70-80% | 412 | 74.2% | 76.6% |
| 80-90% | 148 | 84.7% | 89.9% |
| 90-100% | 25 | 91.9% | 88.0% |

## Score distribution checks

- 80% ranges contained the team's actual score 82.4% of the time.
- Predicted chance of a one-score game (8 or fewer): 50.7%; actual: 53.2%.
- Headline score exactly right: 1.3% of games.
