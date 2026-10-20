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

## Betting edges

The live page's edges, valued the same way: every side of each market at the dataset's price (approximate closing lines, bookmaker margin left in), with the model alone, before the market blend. A side is bet, one unit, when its expected value is at least 3%; only the best side of each market per fight. The 95% range resamples the bets.

| Market | Fights with prices | Edges | Record (W-L-P) | Units | ROI | 95% range | Model's average EV | On underdogs |
|---|---|---|---|---|---|---|---|---|
| Moneyline | 4986 | 3972 | 1476-2480-16 | -293.2 | -7.4% | -11.7% to -3.3% | +37.8% | 78% |
| Round total | no historical prices | – | – | – | – | – | – | – |
| Method of victory | 4488 | 4244 | 554-3681-9 | -665.4 | -15.7% | -23.3% to -7.9% | +61.6% | 100% |

- "Model's average EV" is what the model expected to make per unit on the bets it took; the ROI is what they made. The gap is how much the model overrates its own edges: what it knows that the market does not is outweighed by what the market knows that it does not (debutants' regional records, injuries, camp news).
- Method props whose six prices add up to less than 100% implied (no bookmaker margin, so not prices anyone could bet; about a third of the dataset's 2025–26 props) are left out.
- Caveats: the dataset does not say when its prices were captured or whether they are one book's or the best available, and real stakes would move real prices. The live page tracks these edges on the prices it logged before each fight, which is the test that counts.
