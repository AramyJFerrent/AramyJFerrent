# Walk-forward backtest

Seasons 2016–2025. Every game is predicted using only earlier weeks of its season plus the preseason prior, with the prior regression, points map, market blend and simulator fitted on earlier seasons only. Benchmarks are scored on the same games.

## FBS vs FBS, 2016–2025

| Predictor | Games | Margin MAE | Margin RMSE | Total MAE | Team-score MAE | Brier | Log loss | Winners |
|---|---|---|---|---|---|---|---|---|
| Final (model + market + sim) | 7270 | 12.29 | 15.58 | 12.85 | 8.97 | 0.173 | 0.515 | 73.5% |
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
| Final (model + market + sim) | 3864 | 12.13 | 15.29 | 12.50 | 8.75 | 0.177 | 0.526 | 72.7% |
| Model only | 3864 | 12.73 | 15.97 | 12.99 | 9.14 | 0.185 | 0.546 | 71.2% |
| Elo baseline | 3864 | 13.30 | 16.69 | 13.54 | 9.57 | 0.192 | 0.564 | 69.4% |
| Closing line | 3864 | 12.12 | 15.29 | 12.51 | 8.75 | 0.177 | 0.526 | 72.5% |

## By kind of game

Mean absolute error in points on games with a closing line.

| Segment | Games | Model margin | Final margin | Line margin | Elo margin | Final total | Line total |
|---|---|---|---|---|---|---|---|
| FBS vs FBS | 7270 | 12.85 | 12.29 | 12.28 | 13.42 | 12.85 | 12.85 |
| FBS vs FCS | 1014 | 13.78 | 12.13 | 12.09 | 15.08 | 12.57 | 12.61 |
| Weeks 1-4 | 1850 | 13.15 | 12.38 | 12.37 | 13.99 | 12.89 | 12.89 |
| Week 5 to end of regular season | 5286 | 12.73 | 12.26 | 12.26 | 13.21 | 12.82 | 12.82 |
| Bowls and playoff | 134 | 13.63 | 11.92 | 11.90 | 13.63 | 13.48 | 13.51 |
| Power 4 vs Power 4 | 3234 | 12.69 | 12.28 | 12.28 | 13.19 | 12.73 | 12.73 |
| Group of 5 vs Group of 5 | 3069 | 12.89 | 12.31 | 12.31 | 13.31 | 13.16 | 13.17 |
| Power 4 vs Group of 5 | 967 | 13.25 | 12.21 | 12.19 | 14.55 | 12.28 | 12.26 |
| Conference games | 5224 | 12.68 | 12.24 | 12.24 | 13.17 | 12.82 | 12.81 |
| Nonconference games | 2046 | 13.28 | 12.41 | 12.39 | 14.06 | 12.95 | 12.94 |

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
| Spread | final | closing | posted | 2016–2019 | 2876 | 0 | 0-0-0 | 0.0 | +0.0 | – | – | – |
| Spread | final | closing | assumed -110 | 2016–2025 | 5408 | 149 | 70-75-4 | 232.3 | -19.4 | -8.4% | -24.0% to +7.7% | +7.4% |
| Moneyline | final | closing | posted | 2016–2025 | 7072 | 561 | 73-488-0 | 164.2 | +19.8 | +12.0% | -28.9% to +76.7% | +18.2% |
| Total | final | closing | posted | 2016–2019 | 3196 | 158 | 70-88-0 | 227.0 | -28.0 | -12.3% | -28.5% to +3.2% | +6.0% |
| Total | final | closing | assumed -110 | 2016–2025 | 5088 | 178 | 98-78-2 | 240.9 | +3.8 | +1.6% | -13.7% to +16.1% | +6.0% |
| Spread | final | opening | assumed -110 | 2016–2025 | 7447 | 140 | 64-75-1 | 218.7 | -32.4 | -14.8% | -31.4% to +2.6% | +7.3% |
| Total | final | opening | assumed -110 | 2016–2025 | 7448 | 296 | 156-138-2 | 416.2 | +4.8 | +1.2% | -10.1% to +11.5% | +6.0% |
| Spread | model only | closing | posted | 2016–2019 | 2876 | 2096 | 1023-1031-42 | 2748.8 | -109.3 | -4.0% | -8.2% to +0.6% | +19.3% |
| Spread | model only | closing | assumed -110 | 2016–2025 | 5408 | 4081 | 2003-2006-72 | 6044.1 | -266.0 | -4.4% | -7.5% to -1.2% | +23.7% |
| Moneyline | model only | closing | posted | 2016–2025 | 7072 | 4429 | 1652-2777-0 | 4039.8 | +2.2 | +0.1% | -5.1% to +5.9% | +30.3% |
| Total | model only | closing | posted | 2016–2019 | 3196 | 2362 | 1212-1122-28 | 3737.8 | -94.3 | -2.5% | -6.9% to +2.0% | +21.0% |
| Total | model only | closing | assumed -110 | 2016–2025 | 5088 | 3691 | 1926-1722-43 | 5712.1 | +96.3 | +1.7% | -1.8% to +5.1% | +20.4% |
| Spread | model only | opening | assumed -110 | 2016–2025 | 7447 | 5435 | 2743-2601-91 | 9886.6 | -265.4 | -2.7% | -5.4% to +0.3% | +22.1% |
| Total | model only | opening | assumed -110 | 2016–2025 | 7448 | 5393 | 2871-2462-60 | 9516.3 | +314.3 | +3.3% | +0.5% to +6.0% | +20.1% |

### Final-prediction edges by kind of game

The same edges, split where college markets are thought to be softest. Each cell is edges, ROI and its 95% range; opening lines have no moneyline.

| Segment | Lines | Games | Spread | Moneyline | Total |
|---|---|---|---|---|---|
| FBS vs FBS | closing | 7270 | 89: -6.5% (-28.0% to +15.0%) | 477: -11.5% (-32.0% to +10.1%) | 267: -9.3% (-22.1% to +3.1%) |
| FBS vs FBS | opening | 7270 | 94: -10.3% (-30.5% to +11.3%) | – | 245: -5.1% (-16.7% to +7.5%) |
| FBS vs FCS | closing | 1014 | 60: -10.4% (-35.7% to +14.0%) | 84: +273.1% (-84.8% to +1093.0%) | 69: +13.0% (-11.3% to +35.7%) |
| FBS vs FCS | opening | 1014 | 46: -22.0% (-51.3% to +6.6%) | – | 51: +31.7% (+4.2% to +56.6%) |
| Weeks 1-4 | closing | 1850 | 42: -8.5% (-39.3% to +24.3%) | 197: -30.4% (-63.5% to +5.2%) | 60: +14.3% (-11.1% to +38.4%) |
| Weeks 1-4 | opening | 1850 | 47: -11.4% (-38.9% to +19.0%) | – | 66: -10.6% (-33.3% to +13.3%) |
| Week 5 to end of regular season | closing | 5286 | 47: -4.1% (-31.0% to +23.3%) | 280: +0.2% (-23.6% to +24.7%) | 205: -17.1% (-30.1% to -3.7%) |
| Week 5 to end of regular season | opening | 5286 | 47: -8.8% (-37.9% to +18.8%) | – | 179: -3.3% (-18.3% to +11.4%) |
| Bowls and playoff | closing | 134 | 0 | 0 | 2: +90.9% (+90.9% to +90.9%) |
| Bowls and playoff | opening | 134 | 0 | – | 0 |
| Power 4 vs Power 4 | closing | 3234 | 15: -30.3% (-72.8% to +19.7%) | 181: -16.6% (-46.3% to +16.4%) | 94: -7.2% (-27.0% to +13.1%) |
| Power 4 vs Power 4 | opening | 3234 | 15: -26.1% (-72.9% to +24.8%) | – | 81: -2.6% (-23.8% to +19.4%) |
| Group of 5 vs Group of 5 | closing | 3069 | 49: +9.0% (-17.5% to +35.8%) | 170: -10.7% (-37.6% to +16.6%) | 151: -12.6% (-27.5% to +3.3%) |
| Group of 5 vs Group of 5 | opening | 3069 | 48: -6.8% (-36.0% to +21.6%) | – | 140: -6.8% (-24.3% to +9.0%) |
| Power 4 vs Group of 5 | closing | 967 | 25: -22.9% (-59.3% to +17.2%) | 126: -4.0% (-61.6% to +56.3%) | 22: +8.9% (-30.6% to +46.7%) |
| Power 4 vs Group of 5 | opening | 967 | 31: -9.0% (-42.3% to +24.3%) | – | 24: -2.4% (-43.6% to +35.4%) |
| Conference games | closing | 5224 | 43: -9.0% (-37.9% to +20.9%) | 286: +2.1% (-21.8% to +28.1%) | 189: -12.1% (-26.7% to +2.2%) |
| Conference games | opening | 5224 | 43: -5.3% (-34.4% to +24.0%) | – | 169: -0.5% (-17.0% to +15.9%) |
| Nonconference games | closing | 2046 | 46: -4.9% (-34.6% to +24.9%) | 191: -35.8% (-68.6% to +0.5%) | 78: -3.0% (-24.7% to +18.7%) |
| Nonconference games | opening | 2046 | 51: -13.5% (-39.2% to +13.5%) | – | 76: -15.5% (-37.8% to +6.4%) |

## Win-probability calibration

| Predicted | Games | Mean predicted | Actual |
|---|---|---|---|
| 0-10% | 293 | 5.4% | 8.9% |
| 10-20% | 463 | 15.7% | 14.9% |
| 20-30% | 500 | 25.0% | 23.0% |
| 30-40% | 776 | 34.8% | 36.6% |
| 40-50% | 811 | 43.7% | 46.1% |
| 50-60% | 971 | 56.3% | 54.7% |
| 60-70% | 960 | 65.4% | 68.1% |
| 70-80% | 750 | 75.1% | 76.4% |
| 80-90% | 972 | 84.9% | 86.7% |
| 90-100% | 1788 | 96.7% | 96.6% |

## Score distribution checks

- 80% ranges contained the team's actual score 82.0% of the time.
- Predicted chance of a one-score game (8 or fewer): 33.7%; actual: 34.3%.
- Headline score exactly right: 0.5% of games.
