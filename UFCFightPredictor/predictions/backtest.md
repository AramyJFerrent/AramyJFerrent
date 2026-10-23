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

The live page's edges, valued the same way: every side of each market at the dataset's price (approximate closing lines, bookmaker margin left in), betting the best side of each market per fight when its expected value is at least 3%, at 25% of the Kelly stake with at most 3 units (1% of the bankroll each) on one bout. Three sets of chances: the final prediction the live page uses (the blended win chance, and method chances anchored to the method props), the blended forecast's own method split (blended win chance run through the method model, not anchored to the props), and the model alone before the blend (the rule the predictor used before). ROI is units won per unit staked, with a 95% range that resamples bouts; expected ROI is what the edges' EVs promised.

| Market | Chances | Fights with prices | Edges | Record (W-L-P) | Staked | Units won | ROI | 95% range | Expected ROI | On underdogs |
|---|---|---|---|---|---|---|---|---|---|---|
| Moneyline | final (live) | 4986 | 886 | 494-388-4 | 1577.0 | +80.2 | +5.1% | -1.3% to +11.4% | +7.8% | 39% |
| Round total | final (live) | no historical prices | – | – | – | – | – | – | – | – |
| Method of victory | final (live) | 4488 | 100 | 13-87-0 | 21.1 | +10.5 | +49.9% | -32.5% to +147.9% | +11.5% | 100% |
| Moneyline | blended split | 4986 | 886 | 494-388-4 | 1265.8 | +63.1 | +5.0% | -1.5% to +11.5% | +7.8% | 39% |
| Round total | blended split | no historical prices | – | – | – | – | – | – | – | – |
| Method of victory | blended split | 4488 | 3952 | 627-3317-8 | 6180.6 | -280.6 | -4.5% | -13.0% to +4.1% | +61.0% | 100% |
| Moneyline | model only | 4986 | 3972 | 1476-2480-16 | 7831.4 | -470.6 | -6.0% | -10.5% to -1.7% | +41.0% | 78% |
| Round total | model only | no historical prices | – | – | – | – | – | – | – | – |
| Method of victory | model only | 4488 | 4244 | 554-3681-9 | 4614.6 | -526.9 | -11.4% | -19.4% to -3.1% | +68.7% | 100% |

- Expected ROI is what the bets were expected to make per unit staked; ROI is what they made. The gap is how much the chances behind them overrate their own edges.
- Method props whose six prices add up to less than 100% implied (no bookmaker margin, so not prices anyone could bet; about a third of the dataset's 2025–26 props) are left out.
- Caveats: the dataset does not say when its prices were captured or whether they are one book's or the best available, and real stakes would move real prices. The blend that the final chances use was designed on these same years, so its edges here are somewhat optimistic. The live page tracks these edges on the prices it logged before each fight, which is the test that counts.
