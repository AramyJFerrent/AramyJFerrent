# Walk-forward backtest

Seasons 2016–2025. Every game is predicted using only earlier weeks of its season plus the preseason prior, with the prior regression, points map, market blend and simulator fitted on earlier seasons only. Benchmarks are scored on the same games.

## FBS vs FBS, 2016–2025

| Predictor | Games | Margin MAE | Margin RMSE | Total MAE | Team-score MAE | Brier | Log loss | Winners |
|---|---|---|---|---|---|---|---|---|
| Final (model + market + sim) | 7270 | 12.29 | 15.58 | 12.84 | 8.97 | 0.173 | 0.515 | 73.5% |
| Model only | 7270 | 12.85 | 16.21 | 13.31 | 9.35 | 0.180 | 0.533 | 72.3% |
| Elo baseline | 7270 | 13.42 | 16.90 | 14.04 | 9.85 | 0.188 | 0.554 | 70.6% |
| Closing line | 7270 | 12.28 | 15.58 | 12.85 | 8.97 | 0.172 | 0.514 | 73.3% |

## All games with a line (FCS opponents included), 2016–2025

| Predictor | Games | Margin MAE | Margin RMSE | Total MAE | Team-score MAE | Brier | Log loss | Winners |
|---|---|---|---|---|---|---|---|---|
| Final (model + market + sim) | 8284 | 12.27 | 15.53 | 12.80 | 8.93 | 0.157 | 0.472 | 76.0% |
| Model only | 8284 | 12.96 | 16.34 | 13.29 | 9.36 | 0.164 | 0.492 | 75.0% |
| Elo baseline | 8284 | 13.62 | 17.13 | 13.96 | 9.87 | 0.172 | 0.513 | 73.4% |
| Closing line | 8284 | 12.26 | 15.53 | 12.82 | 8.93 | 0.157 | 0.472 | 75.9% |

## FBS vs FBS, 2021–2025 (seasons not used for tuning)

| Predictor | Games | Margin MAE | Margin RMSE | Total MAE | Team-score MAE | Brier | Log loss | Winners |
|---|---|---|---|---|---|---|---|---|
| Final (model + market + sim) | 3864 | 12.13 | 15.29 | 12.50 | 8.75 | 0.177 | 0.526 | 72.7% |
| Model only | 3864 | 12.73 | 15.97 | 12.99 | 9.14 | 0.185 | 0.546 | 71.2% |
| Elo baseline | 3864 | 13.30 | 16.69 | 13.54 | 9.57 | 0.192 | 0.564 | 69.4% |
| Closing line | 3864 | 12.12 | 15.29 | 12.51 | 8.75 | 0.177 | 0.526 | 72.5% |

## By kind of game

Mean absolute error in points on games with a closing line.

| Segment | Games | Model margin | Final margin | Line margin | Elo margin | Final total | Line total |
|---|---|---|---|---|---|---|---|
| FBS vs FBS | 7270 | 12.85 | 12.29 | 12.28 | 13.42 | 12.84 | 12.85 |
| FBS vs FCS | 1014 | 13.78 | 12.13 | 12.09 | 15.08 | 12.57 | 12.61 |
| Weeks 1-4 | 1850 | 13.15 | 12.38 | 12.37 | 13.99 | 12.89 | 12.89 |
| Week 5 to end of regular season | 5286 | 12.73 | 12.26 | 12.26 | 13.21 | 12.80 | 12.82 |
| Bowls and playoff | 134 | 13.63 | 11.92 | 11.90 | 13.63 | 13.47 | 13.51 |
| Power 4 vs Power 4 | 3234 | 12.69 | 12.28 | 12.28 | 13.19 | 12.70 | 12.73 |
| Group of 5 vs Group of 5 | 3069 | 12.89 | 12.31 | 12.31 | 13.31 | 13.16 | 13.17 |
| Power 4 vs Group of 5 | 967 | 13.25 | 12.21 | 12.19 | 14.55 | 12.27 | 12.26 |
| Conference games | 5224 | 12.68 | 12.24 | 12.24 | 13.17 | 12.79 | 12.81 |
| Nonconference games | 2046 | 13.28 | 12.41 | 12.39 | 14.06 | 12.94 | 12.94 |

## Is the difference real?

Paired bootstrap of the per-game absolute margin error, FBS vs FBS games (negative favors the first).

| Comparison | Mean difference | 95% interval |
|---|---|---|
| Final vs closing line | +0.005 | -0.003 to +0.012 |
| Model only vs Elo | -0.569 | -0.673 to -0.467 |
| Model only vs closing line | +0.570 | +0.465 to +0.669 |

## Betting edges

Every game with a line, priced with the final prediction (the model blended with the line being bet, by the weights fitted on earlier seasons, run through the score simulator and anchored to the market's own chances). A bet is an edge when its expected value is at least 3% per unit staked, staked at 25% of the Kelly stake with at most 3 units (1% of the bankroll each) on one game; pushes return the stake. Closing prices are the median of the books quoting the consensus line; the odds file has spread and total prices only through 2019, so later seasons are scored at an assumed -110 and shown separately. Opening lines are the median opener across books and carry no prices, so -110 is assumed there and the moneyline is left out. ROI is units won per unit staked, with a 95% bootstrap range over games; expected ROI is what the edges' EVs promised. The model-only rows price the same bets with the model before the blend, the rule the predictor used before, for comparison.

| Market | Chances | Lines | Prices | Seasons | Games | Edges | Record (W-L-P) | Staked | Units won | ROI | 95% range | Expected ROI |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Spread | final | closing | posted | 2016–2019 | 2876 | 1 | 0-1-0 | 1.0 | -1.0 | -100.0% | +nan% to +nan% | +3.9% |
| Spread | final | closing | assumed -110 | 2016–2025 | 5408 | 156 | 82-71-3 | 234.3 | -9.1 | -3.9% | -19.3% to +12.2% | +7.3% |
| Moneyline | final | closing | posted | 2016–2025 | 7072 | 575 | 73-502-0 | 172.8 | +23.8 | +13.7% | -27.1% to +76.3% | +17.8% |
| Total | final | closing | posted | 2016–2019 | 3196 | 367 | 195-171-1 | 687.0 | +18.0 | +2.6% | -7.6% to +13.4% | +10.1% |
| Total | final | closing | assumed -110 | 2016–2025 | 5088 | 172 | 84-85-3 | 235.4 | -13.4 | -5.7% | -20.3% to +9.3% | +6.1% |
| Spread | final | opening | assumed -110 | 2016–2025 | 7447 | 143 | 67-75-1 | 223.1 | -28.5 | -12.8% | -29.2% to +3.6% | +7.3% |
| Total | final | opening | assumed -110 | 2016–2025 | 7448 | 297 | 151-143-3 | 426.5 | +2.7 | +0.6% | -10.8% to +12.1% | +6.1% |
| Spread | model only | closing | posted | 2016–2019 | 2876 | 2094 | 1018-1032-44 | 2720.8 | -113.9 | -4.2% | -8.6% to +0.1% | +19.4% |
| Spread | model only | closing | assumed -110 | 2016–2025 | 5408 | 3966 | 1956-1939-71 | 5921.6 | -215.7 | -3.6% | -6.7% to -0.5% | +23.7% |
| Moneyline | model only | closing | posted | 2016–2025 | 7072 | 4392 | 1634-2758-0 | 3997.9 | +25.6 | +0.6% | -4.9% to +7.2% | +30.2% |
| Total | model only | closing | posted | 2016–2019 | 3196 | 2379 | 1220-1128-31 | 3768.3 | -80.0 | -2.1% | -6.4% to +2.2% | +21.4% |
| Total | model only | closing | assumed -110 | 2016–2025 | 5088 | 3600 | 1877-1674-49 | 5559.8 | +82.9 | +1.5% | -2.0% to +5.1% | +20.1% |
| Spread | model only | opening | assumed -110 | 2016–2025 | 7447 | 5314 | 2688-2539-87 | 9681.1 | -250.8 | -2.6% | -5.1% to +0.2% | +22.1% |
| Total | model only | opening | assumed -110 | 2016–2025 | 7448 | 5318 | 2833-2423-62 | 9419.6 | +291.2 | +3.1% | +0.3% to +5.9% | +20.1% |

### Final-prediction edges by kind of game

The same edges, split where college markets are thought to be softest. Each cell is edges, ROI and its 95% range; opening lines have no moneyline.

| Segment | Lines | Games | Spread | Moneyline | Total |
|---|---|---|---|---|---|
| FBS vs FBS | closing | 7270 | 96: +2.2% (-17.6% to +22.1%) | 485: -7.0% (-27.9% to +14.4%) | 447: -0.1% (-9.6% to +9.3%) |
| FBS vs FBS | opening | 7270 | 97: -7.0% (-27.0% to +14.3%) | – | 239: -4.3% (-16.8% to +8.8%) |
| FBS vs FCS | closing | 1014 | 61: -11.9% (-37.3% to +13.4%) | 90: +249.3% (-100.0% to +1110.7%) | 92: +3.9% (-18.5% to +24.6%) |
| FBS vs FCS | opening | 1014 | 46: -22.0% (-51.3% to +6.6%) | – | 58: +21.6% (-3.2% to +45.3%) |
| Weeks 1-4 | closing | 1850 | 48: +0.9% (-26.4% to +29.7%) | 178: -4.9% (-46.7% to +37.4%) | 94: -1.4% (-21.9% to +18.5%) |
| Weeks 1-4 | opening | 1850 | 48: -9.9% (-37.3% to +19.7%) | – | 56: -3.1% (-28.1% to +21.4%) |
| Week 5 to end of regular season | closing | 5286 | 48: +3.7% (-23.4% to +32.2%) | 307: -8.2% (-30.2% to +15.5%) | 353: +0.2% (-10.4% to +10.5%) |
| Week 5 to end of regular season | opening | 5286 | 49: -3.7% (-33.3% to +23.3%) | – | 183: -4.6% (-18.9% to +10.0%) |
| Bowls and playoff | closing | 134 | 0 | 0 | 0 |
| Bowls and playoff | opening | 134 | 0 | – | 0 |
| Power 4 vs Power 4 | closing | 3234 | 16: -4.3% (-51.0% to +43.1%) | 183: -13.4% (-43.1% to +16.5%) | 201: +8.9% (-5.4% to +23.3%) |
| Power 4 vs Power 4 | opening | 3234 | 17: -14.6% (-57.0% to +31.4%) | – | 87: +2.4% (-18.8% to +23.8%) |
| Group of 5 vs Group of 5 | closing | 3069 | 49: +4.0% (-24.2% to +32.6%) | 176: -8.3% (-35.5% to +20.5%) | 199: -9.8% (-24.5% to +5.1%) |
| Group of 5 vs Group of 5 | opening | 3069 | 49: -3.5% (-30.3% to +25.9%) | – | 129: -7.0% (-24.6% to +11.0%) |
| Power 4 vs Group of 5 | closing | 967 | 31: +2.2% (-32.4% to +38.4%) | 126: +9.4% (-55.0% to +76.2%) | 47: +0.4% (-30.1% to +30.4%) |
| Power 4 vs Group of 5 | opening | 967 | 31: -9.0% (-42.3% to +24.2%) | – | 23: -11.5% (-52.1% to +29.5%) |
| Conference games | closing | 5224 | 44: +0.1% (-27.7% to +29.8%) | 302: +1.1% (-22.3% to +26.4%) | 329: +2.6% (-8.6% to +14.1%) |
| Conference games | opening | 5224 | 46: +2.1% (-29.2% to +28.6%) | – | 163: -2.4% (-18.1% to +13.1%) |
| Nonconference games | closing | 2046 | 52: +3.6% (-24.7% to +32.2%) | 183: -23.6% (-59.2% to +18.6%) | 118: -7.8% (-26.2% to +11.4%) |
| Nonconference games | opening | 2046 | 51: -13.5% (-39.2% to +13.5%) | – | 76: -8.2% (-29.0% to +13.3%) |

## Win-probability calibration

| Predicted | Games | Mean predicted | Actual |
|---|---|---|---|
| 0-10% | 288 | 5.4% | 8.7% |
| 10-20% | 456 | 15.7% | 14.5% |
| 20-30% | 514 | 25.0% | 23.3% |
| 30-40% | 758 | 34.8% | 36.8% |
| 40-50% | 831 | 43.7% | 45.5% |
| 50-60% | 966 | 56.3% | 54.2% |
| 60-70% | 955 | 65.3% | 68.3% |
| 70-80% | 772 | 75.0% | 76.9% |
| 80-90% | 965 | 84.9% | 87.2% |
| 90-100% | 1779 | 96.7% | 96.6% |

## Score distribution checks

- 80% ranges contained the team's actual score 82.1% of the time.
- Predicted chance of a one-score game (8 or fewer): 33.7%; actual: 34.3%.
- Headline score exactly right: 0.6% of games.
