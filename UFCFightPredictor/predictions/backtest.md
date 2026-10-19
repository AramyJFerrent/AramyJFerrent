# Walk-forward backtest

Fights from 2015 to 2026. Every fight is predicted from ratings and profiles built on earlier fights only, with the win model, calibration, market blend, method and round models fitted on the ten years before its year. Benchmarks are scored on the same fights. Prices are the Ultimate UFC Dataset's moneylines (approximate closing prices) with the margin removed proportionally.

## Who wins

| Predictor | Fights | Log loss | Brier | Winners |
|---|---|---|---|---|
| Final (model + market) | 4941 | 0.6065 | 0.210 | 66.5% |
| Model only | 4941 | 0.6432 | 0.226 | 63.0% |
| Betting market (de-vigged) | 4941 | 0.6089 | 0.211 | 65.8% |
| Glicko-2 rating alone | 4941 | 0.6788 | 0.243 | 56.5% |
| Elo, UFC results only | 4941 | 0.6825 | 0.245 | 55.2% |

## Is the difference real?

Paired bootstrap of the per-fight log loss (negative favors the first).

| Comparison | Mean difference | 95% interval |
|---|---|---|
| Final vs market | -0.0024 | -0.0043 to -0.0005 |
| Model only vs market | +0.0342 | +0.0268 to +0.0417 |
| Model only vs Glicko-2 alone | -0.0356 | -0.0423 to -0.0288 |

## How and when

Six-way log loss over each fighter winning by KO/TKO, submission or decision, on fights with method props. Distance: the chance the fight goes to the judges.

| Predictor | Fights | Six-way log loss | Predicted | Actual | Distance log loss |
|---|---|---|---|---|---|
| Final | 4689 | 1.571 | 49.4% | 49.6% | 0.676 |
| Division base rates × market win chance | 4689 | 1.613 | 49.0% | 49.6% | 0.683 |
| Method props (de-vigged) | 4689 | 1.546 | 45.0% | 49.6% | 0.666 |
| Uniform guess | 4689 | 1.792 | 50.0% | 49.6% | 0.693 |

Round: log loss over finishing in each round or going the distance.

| Scheduled rounds | Predictor | Fights | Log loss |
|---|---|---|---|
| 3 | Final | 5216 | 1.1744 |
| 3 | Division base rates | 5216 | 1.1857 |
| 5 | Final | 564 | 1.5324 |
| 5 | Division base rates | 564 | 1.5391 |

## Win-chance calibration

Chance given to the predicted favorite against how often favorites won.

| Favorite's chance | Fights | Predicted | Actual |
|---|---|---|---|
| 50–55% | 943 | 52.5% | 52.4% |
| 55–60% | 1006 | 57.5% | 58.2% |
| 60–65% | 987 | 62.5% | 57.6% |
| 65–70% | 881 | 67.4% | 65.9% |
| 70–75% | 732 | 72.4% | 73.2% |
| 75–80% | 583 | 77.4% | 77.4% |
| 80–85% | 388 | 82.4% | 85.6% |
| 85–90% | 210 | 87.2% | 92.4% |
| 90–100% | 64 | 91.7% | 90.6% |

## Can it beat the price?

One-unit moneyline bets on a fighter whenever a win chance beats the chance the price implies by at least the edge shown, at the dataset's prices with the bookmaker margin left in. The live page flags the final win chance at a 2-point edge.

| Win chance used | Edge | Bets | Return per bet | 95% range | Units | On underdogs |
|---|---|---|---|---|---|---|
| Final win chance | 0 pts | 2269 | +2.6% | -1.4% to +6.7% | +59 | 30% |
| Final win chance | 2 pts | 734 | +7.5% | +0.7% to +14.2% | +55 | 27% |
| Final win chance | 3 pts | 387 | +13.4% | +3.8% to +23.0% | +52 | 31% |
| Final win chance | 5 pts | 113 | +19.4% | +0.1% to +38.2% | +22 | 40% |
| Final win chance | 8 pts | 19 | +47.3% | -6.2% to +106.7% | +9 | 42% |
| Model alone | 0 pts | 4376 | -7.1% | -11.0% to -3.2% | -312 | 75% |
| Model alone | 2 pts | 3810 | -7.1% | -11.4% to -2.8% | -269 | 78% |
| Model alone | 3 pts | 3546 | -7.3% | -11.8% to -2.9% | -260 | 79% |
| Model alone | 5 pts | 3039 | -6.1% | -11.0% to -1.2% | -186 | 82% |
| Model alone | 8 pts | 2313 | -4.6% | -10.3% to +1.3% | -106 | 85% |

- The model alone loses money against the price: what it knows that the market does not is outweighed by what the market knows that it does not (debutants' regional records, injuries, camp news). Its edges are mostly on underdogs.
- The final win chance, which keeps most of the market's view and stretches favorites, made money at every edge, mostly on favorites the market underrates: the favorite-longshot bias.
- Caveats: the edge thresholds were compared after the fact; the dataset does not say when its prices were captured or whether they are one book's or the best available; and real stakes would move real prices. The live page tracks these bets on the prices it logged before each fight, which is the test that counts.
