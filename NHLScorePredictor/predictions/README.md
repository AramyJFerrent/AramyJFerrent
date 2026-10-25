# NHL score predictions

Updated Sat Oct 24, 2026 08:20 PM ET. Refreshed automatically several times a day during the season; each game's prediction is locked at puck drop and graded once the final score is in.

Each game is simulated 10,000 times minute by minute, with pulled goalies, empty-net goals, overtime and shootouts. The predicted score is the most common final score in which the likelier winner wins; as in the official result, a shootout winner gets one extra goal. Hockey is low-scoring and luck-heavy, so read the win chance and the ranges (80% of simulated outcomes for each team) before the single score.

Goalies marked with a percentage are projected from recent starts (the share is the chance he starts); "probable" or "confirmed" ones come from ESPN and replace the projection when available.

The fair moneyline is the American odds that match the win chance exactly, with no bookmaker margin: -150 means risk $150 to win $100, +150 means risk $100 to win $150. A sportsbook's price is a little worse on both sides because of its cut, so a book only offers value on a team when its price beats the fair line. The puck line is the favorite's chance to win by two or more.

The edge columns price each side of the puck line, moneyline and total with the final prediction: the model's goal rates blended with the market's, simulated against the posted lines, overtime and shootout included (the shootout winner gets one goal), and anchored to the market's own chances so only what the blend moves off the market counts. Each cell shows the side with the best expected value (EV) per $1 bet at the posted price. A side is an edge only if its EV is at least 3%: a pick shows its price, EV, its chance of winning the bet and its stake, a 25% share of the Kelly stake in units of 1% of the bankroll, with at most 3 units on one game; "no edge" means neither side clears the bar. A projected starting goalie is wrong about a third of the time and the market prices the real one, so edges wait until both starters are confirmed. A total with no posted price is assumed to be -110 (marked \*); the puck line and moneyline are never assumed, so without a price the cell shows the model's fair odds instead. Treat the edges as an experiment, not betting advice; see the backtest for how they have done on past seasons. Their record is tracked live below.

## Saturday, October 24

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected goals | 80% range | Overtime | Puck line | Total: model / line | Goalies | Posted moneyline | Puck line edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 9:00 PM | TBL @ UTA | TBL 3, UTA 4 | UTA 58% | TBL +140 / UTA -140 | 2.9 – 3.5 | 1–5 / 1–6 | 21% | UTA -1.5 36% | 6.4 / 6.5 (over 48%) | Dennis Hildeby (expected) / Karel Vejmelka (confirmed) | TBL +124 / UTA -148 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 10:00 PM | DET @ CGY | DET 4, CGY 3 | DET 53% | DET -110 / CGY +110 | 3.2 – 3.0 | 1–6 / 1–5 | 22% | DET -1.5 32% | 6.2 / 5.5 (over 55%) | John Gibson (confirmed) / Devin Cooley (confirmed) | DET -130 / CGY +110 | no edge | no edge | no edge |
| 10:00 PM | MIN @ SEA | MIN 4, SEA 3 | MIN 60% | MIN -150 / SEA +150 | 3.5 – 2.8 | 1–6 / 1–5 | 21% | MIN -1.5 39% | 6.3 / 6.5 (over 47%) | Jesper Wallstedt (confirmed) / Joey Daccord (confirmed) | MIN -175 / SEA +145 | no edge | no edge | no edge |

## Sunday, October 25

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected goals | 80% range | Overtime | Puck line | Total: model / line | Goalies | Posted moneyline | Puck line edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 3:00 PM | FLA @ CHI | FLA 4, CHI 3 | FLA 61% | FLA -160 / CHI +160 | 3.5 – 2.7 | 1–6 / 1–5 | 22% | FLA -1.5 40% | 6.2 / 6.5 (over 45%) | Akira Schmid (confirmed) / Spencer Knight (expected) | FLA -180 / CHI +150 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 6:00 PM | NYI @ DAL | NYI 2, DAL 3 | DAL 59% | NYI +145 / DAL -145 | 2.6 – 3.1 | 1–5 / 1–5 | 23% | DAL -1.5 36% | 5.7 / 5.5 (over 47%) | Ilya Sorokin (expected) / Jake Oettinger (expected) | NYI +164 / DAL -198 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 7:00 PM | MTL @ WPG | MTL 3, WPG 2 | MTL 51% | MTL -105 / WPG +105 | 3.1 – 3.0 | 1–5 / 1–5 | 22% | MTL -1.5 30% | 6.1 / 5.5 (over 53%) | Jakub Dobes (expected) / Stuart Skinner (expected) | MTL -115 / WPG -105 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 8:00 PM | COL @ NSH | COL 4, NSH 3 | COL 65% | COL -185 / NSH +185 | 3.8 – 2.8 | 1–6 / 1–5 | 20% | COL -1.5 44% | 6.6 / 6.5 (over 51%) | Mackenzie Blackwood (expected) / Justus Annunen (expected) | COL -230 / NSH +190 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 10:00 PM | MIN @ VAN | MIN 4, VAN 3 | MIN 64% | MIN -175 / VAN +175 | 3.7 – 2.8 | 1–6 / 1–5 | 20% | MIN -1.5 43% | 6.5 / 6.5 (over 49%) | Calvin Pickard (confirmed) / Leevi Meriläinen (expected) | MIN -180 / VAN +150 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |

## Monday, October 26

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected goals | 80% range | Overtime | Puck line | Total: model / line | Goalies | Posted moneyline | Puck line edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 7:00 PM | LAK @ NYR | LAK 2, NYR 3 | NYR 54% | LAK +120 / NYR -120 | 2.9 – 3.1 | 1–5 / 1–5 | 23% | NYR -1.5 32% | 6.0 | Darcy Kuemper (expected) / Dylan Garand (expected) | – | no line yet (model fair NYR -1.5 +210 / LAK +1.5 -210) | no line yet | no line yet |
| 8:30 PM | TOR @ CGY | TOR 4, CGY 3 | TOR 53% | TOR -110 / CGY +110 | 3.4 – 3.2 | 1–6 / 1–6 | 22% | TOR -1.5 32% | 6.5 | Sergei Bobrovsky (expected) / Dustin Wolf (expected) | – | no line yet (model fair CGY +1.5 -210 / TOR -1.5 +210) | no line yet | no line yet |
| 9:30 PM | DET @ EDM | DET 3, EDM 4 | EDM 57% | DET +135 / EDM -135 | 3.0 – 3.5 | 1–5 / 1–6 | 21% | EDM -1.5 37% | 6.5 | John Gibson (expected) / Tristan Jarry (expected) | – | no line yet (model fair EDM -1.5 +175 / DET +1.5 -175) | no line yet | no line yet |

\* price not posted; assumed -110.

## How the 2026-27 predictions have done

| Predictor | Games | Log loss | Brier | Winners | Goals MAE | Total MAE | 80% range hit |
|---|---|---|---|---|---|---|---|
| Final prediction | 167 | 0.6542 | 0.2311 | 61.7% | 1.38 | 1.73 | 89.8% |
| Model only (before blending) | 167 | 0.6553 | 0.2317 | 61.7% | – | – | – |
| Elo | 167 | 0.6666 | 0.2369 | 62.3% | – | – | – |
| Final prediction, games with a line | 33 | 0.6896 | 0.2480 | 54.5% | 1.33 | 1.62 | 90.9% |
| Model only, games with a line | 33 | 0.6951 | 0.2509 | 54.5% | – | – | – |
| Betting market (de-vigged moneyline) | 33 | 0.6905 | 0.2484 | 54.5% | – | 1.53 | – |

Log loss and Brier score the win chances (lower is better; a coin flip scores 0.693 and 0.250). Hockey is close to a coin flip, so differences in the third decimal matter, and only over hundreds of games. Goals MAE is the average miss on each team's goals.

Overtime: predicted in 21.6% of regular-season games, happened in 22.8%.

134 of these games were played before the predictor went live. They are backfilled walk-forward (each day predicted from earlier days only) with the actual starting goalies and no betting line. Every game since is graded on the prediction logged before puck drop.

### Betting edges

| Market | Edges | Record (W-L-P) | Staked | Units won | ROI | Expected ROI |
|---|---|---|---|---|---|---|
| Puck line | 0 | 0-0-0 | 0.0 | +0.00 | – | – |
| Moneyline | 0 | 0-0-0 | 0.0 | +0.00 | – | – |
| Total | 0 | 0-0-0 | 0.0 | +0.00 | – | – |

Moneyline moved toward the model's edge on the first line seen before puck drop: 3 of 6 games (50%).

Each edge at the stake and price logged with the last prediction before puck drop (edges logged before edges were priced from the final prediction are left out); pushes return the stake. Units are 1% of the bankroll; ROI is units won per unit staked, and expected ROI is what the edges' EVs promised. The moneyline moving toward the model's edge (closing line value) is the quickest sign that it knows something the market doesn't yet.

### Results, Friday, October 23

| Game | Predicted | Final | Win chance for winner | Inside 80% ranges | Goalies |
|---|---|---|---|---|---|
| MTL @ CHI | 4–3 | 4–1 | 61% | yes | Jacob Fowler / Spencer Knight |
| TBL @ COL | 3–4 | 3–6 | 52% | yes | Andrei Vasilevskiy / Mackenzie Blackwood |

## Power ratings

Goals per game better than an average team, from the goal-rate model: offense and defense combine 5-on-5 expected goals (score and venue adjusted), special teams and actual goals, each weighted against a preseason prior. Defense is positive when it holds opponents below average. Goaltending is rated separately below.

| # | Team | Net | Offense | Defense | 5v5 xGF/60 | 5v5 xGA/60 | PP xGF/60 | PK xGA/60 | Elo |
|---|---|---|---|---|---|---|---|---|---|
| 1 | CAR | +0.64 | +0.41 | +0.24 | 3.40 | 2.44 | 8.05 | 6.75 | 1570 |
| 2 | UTA | +0.50 | +0.26 | +0.24 | 3.18 | 2.35 | 7.99 | 8.10 | 1514 |
| 3 | TBL | +0.35 | +0.17 | +0.18 | 2.91 | 2.49 | 7.66 | 7.76 | 1540 |
| 4 | VGK | +0.29 | +0.10 | +0.19 | 2.75 | 2.47 | 8.70 | 7.25 | 1532 |
| 5 | COL | +0.27 | +0.27 | -0.01 | 2.96 | 2.76 | 7.62 | 7.62 | 1552 |
| 6 | PIT | +0.27 | +0.23 | +0.04 | 3.06 | 2.63 | 7.86 | 7.64 | 1498 |
| 7 | MIN | +0.26 | +0.09 | +0.17 | 2.94 | 2.51 | 8.89 | 8.19 | 1527 |
| 8 | NJD | +0.25 | +0.05 | +0.20 | 2.94 | 2.42 | 8.71 | 7.60 | 1497 |
| 9 | FLA | +0.24 | -0.00 | +0.25 | 2.66 | 2.39 | 8.91 | 7.27 | 1493 |
| 10 | DAL | +0.19 | -0.08 | +0.27 | 2.54 | 2.41 | 9.07 | 7.18 | 1533 |
| 11 | EDM | +0.13 | +0.16 | -0.03 | 2.68 | 2.72 | 9.59 | 8.21 | 1530 |
| 12 | STL | +0.10 | -0.02 | +0.12 | 2.56 | 2.56 | 6.99 | 7.36 | 1510 |
| 13 | OTT | +0.08 | -0.06 | +0.15 | 2.63 | 2.52 | 7.78 | 7.68 | 1517 |
| 14 | LAK | +0.08 | -0.11 | +0.18 | 2.59 | 2.49 | 7.67 | 7.78 | 1470 |
| 15 | BUF | +0.07 | +0.08 | -0.00 | 2.77 | 2.69 | 7.57 | 8.23 | 1513 |
| 16 | NYR | +0.00 | -0.01 | +0.01 | 2.65 | 2.73 | 8.33 | 7.57 | 1504 |
| 17 | NYI | -0.02 | -0.05 | +0.03 | 2.76 | 2.71 | 7.49 | 8.66 | 1494 |
| 18 | MTL | -0.04 | +0.04 | -0.08 | 2.84 | 2.80 | 7.10 | 8.20 | 1519 |
| 19 | BOS | -0.04 | +0.03 | -0.07 | 2.71 | 2.85 | 7.66 | 8.06 | 1533 |
| 20 | CBJ | -0.04 | -0.03 | -0.01 | 2.74 | 2.70 | 7.55 | 8.46 | 1487 |
| 21 | WSH | -0.04 | +0.10 | -0.14 | 2.88 | 2.89 | 7.64 | 8.12 | 1514 |
| 22 | DET | -0.06 | -0.08 | +0.02 | 2.67 | 2.66 | 8.49 | 8.30 | 1483 |
| 23 | WPG | -0.11 | -0.08 | -0.03 | 2.61 | 2.78 | 7.80 | 7.93 | 1481 |
| 24 | TOR | -0.13 | -0.00 | -0.12 | 2.53 | 2.85 | 8.57 | 8.19 | 1481 |
| 25 | NSH | -0.23 | -0.12 | -0.11 | 2.55 | 2.84 | 7.79 | 7.57 | 1479 |
| 26 | CGY | -0.24 | -0.08 | -0.16 | 2.67 | 2.89 | 7.26 | 8.10 | 1456 |
| 27 | SEA | -0.27 | -0.07 | -0.20 | 2.51 | 2.95 | 7.30 | 8.19 | 1488 |
| 28 | ANA | -0.34 | -0.02 | -0.32 | 2.82 | 3.05 | 7.46 | 8.36 | 1477 |
| 29 | PHI | -0.37 | -0.31 | -0.06 | 2.24 | 2.79 | 7.96 | 7.33 | 1481 |
| 30 | SJS | -0.52 | -0.18 | -0.34 | 2.45 | 3.07 | 7.28 | 8.61 | 1473 |
| 31 | CHI | -0.68 | -0.31 | -0.37 | 2.26 | 3.10 | 6.83 | 8.20 | 1435 |
| 32 | VAN | -0.70 | -0.21 | -0.49 | 2.29 | 3.24 | 7.46 | 8.57 | 1417 |

## Goalies

Each team's likeliest next starter. GSAx is goals saved above expected (from this predictor's own shot model), shrunk hard toward a slightly below-average prior, since goaltending repeats poorly from season to season.

| Team | Likely next starter | Share of recent starts | GSAx per 100 shots | Goals per game vs average |
|---|---|---|---|---|
| NYI | Ilya Sorokin | 67% | +0.47 | +0.20 |
| WSH | Logan Thompson | 79% | +0.45 | +0.19 |
| BOS | Jeremy Swayman | 70% | +0.36 | +0.15 |
| TBL | Andrei Vasilevskiy | 60% | +0.18 | +0.08 |
| DAL | Jake Oettinger | 82% | +0.17 | +0.07 |
| OTT | Linus Ullmark | 71% | +0.14 | +0.06 |
| MIN | Jesper Wallstedt | 91% | +0.13 | +0.06 |
| COL | Mackenzie Blackwood | 71% | +0.13 | +0.05 |
| CBJ | Jet Greaves | 61% | +0.11 | +0.05 |
| MTL | Jacob Fowler | 54% | +0.09 | +0.04 |
| CHI | Spencer Knight | 84% | +0.05 | +0.02 |
| PHI | Dan Vladar | 52% | +0.02 | +0.01 |
| WPG | Stuart Skinner | 71% | +0.02 | +0.01 |
| STL | Joel Hofer | 72% | +0.02 | +0.01 |
| NYR | Dylan Garand | 67% | +0.02 | +0.01 |
| NJD | Jake Allen | 58% | -0.07 | -0.03 |
| EDM | Devon Levi | 72% | -0.07 | -0.03 |
| SEA | Philipp Grubauer | 60% | -0.08 | -0.03 |
| DET | John Gibson | 67% | -0.08 | -0.03 |
| CAR | Pyotr Kochetkov | 51% | -0.11 | -0.05 |
| ANA | Lukas Dostal | 65% | -0.13 | -0.05 |
| TOR | Sergei Bobrovsky | 68% | -0.13 | -0.05 |
| UTA | Karel Vejmelka | 73% | -0.16 | -0.07 |
| BUF | Ukko-Pekka Luukkonen | 72% | -0.16 | -0.07 |
| LAK | Darcy Kuemper | 76% | -0.17 | -0.07 |
| VGK | Carter Hart | 56% | -0.18 | -0.07 |
| NSH | Juuse Saros | 73% | -0.25 | -0.11 |
| SJS | Yaroslav Askarov | 60% | -0.25 | -0.11 |
| FLA | Jacob Markstrom | 49% | -0.26 | -0.11 |
| CGY | Dustin Wolf | 52% | -0.28 | -0.12 |
| PIT | Arturs Silovs | 64% | -0.30 | -0.13 |
| VAN | Kevin Lankinen | 56% | -0.63 | -0.26 |

## Current model fit

- Fitted on 5759 games from 2022-23 to 2026-27.
- Home ice: +3.2% goals for the home team relative to the visitor.
- Second night of a back-to-back: -5.8% goals scored, +3.2% goals allowed.
- Starting goalie: each goal per game he saves above average lowers the opponent's rate by 23%.
- Blend: 40% on the betting line wherever there is one (fitted on 33 logged games, shrunk toward the backtest value).
- Simulator: 22.3% of recent regular-season games reached overtime; trailing teams usually have the goalie pulled with 2 minutes left when down one and 3 when down two; empty-net goals come at 0.40 a minute with the net empty; three-on-three overtime produces 1.03 goals per five minutes.
