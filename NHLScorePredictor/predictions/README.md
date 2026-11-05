# NHL score predictions

Updated Wed Nov 04, 2026 09:28 PM ET. Refreshed automatically several times a day during the season; each game's prediction is locked at puck drop and graded once the final score is in.

Each game is simulated 10,000 times minute by minute, with pulled goalies, empty-net goals, overtime and shootouts. The predicted score is the most common final score in which the likelier winner wins; as in the official result, a shootout winner gets one extra goal. Hockey is low-scoring and luck-heavy, so read the win chance and the ranges (80% of simulated outcomes for each team) before the single score.

Goalies marked with a percentage are projected from recent starts (the share is the chance he starts); "probable" or "confirmed" ones come from ESPN and replace the projection when available.

The fair moneyline is the American odds that match the win chance exactly, with no bookmaker margin: -150 means risk $150 to win $100, +150 means risk $100 to win $150. A sportsbook's price is a little worse on both sides because of its cut, so a book only offers value on a team when its price beats the fair line. The puck line is the favorite's chance to win by two or more.

The edge columns price each side of the puck line, moneyline and total with the final prediction: the model's goal rates blended with the market's, simulated against the posted lines, overtime and shootout included (the shootout winner gets one goal), and anchored to the market's own chances so only what the blend moves off the market counts. Each cell shows the side with the best expected value (EV) per $1 bet at the posted price. A side is an edge only if its EV is at least 3%: a pick shows its price, EV, its chance of winning the bet and its stake, a 25% share of the Kelly stake in units of 1% of the bankroll, with at most 3 units on one game; "no edge" means neither side clears the bar. A projected starting goalie is wrong about a third of the time and the market prices the real one, so edges wait until both starters are confirmed. A total with no posted price is assumed to be -110 (marked \*); the puck line and moneyline are never assumed, so without a price the cell shows the model's fair odds instead. Treat the edges as an experiment, not betting advice; see the backtest for how they have done on past seasons. Their record is tracked live below.

## Wednesday, November 4

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected goals | 80% range | Overtime | Puck line | Total: model / line | Goalies | Posted moneyline | Puck line edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 10:00 PM | SJS @ LAK | SJS 3, LAK 4 | LAK 64% | SJS +175 / LAK -175 | 2.7 – 3.6 | 1–5 / 1–6 | 21% | LAK -1.5 42% | 6.4 / 6.5 (over 47%) | Yaroslav Askarov (confirmed) / Darcy Kuemper (confirmed) | SJS +140 / LAK -166 | no edge | no edge | no edge |
| 10:00 PM | CGY @ SEA | CGY 3, SEA 4 | SEA 54% | CGY +120 / SEA -120 | 3.1 – 3.3 | 1–5 / 1–6 | 22% | SEA -1.5 33% | 6.4 / 6.5 (over 49%) | Dustin Wolf (confirmed) / Joey Daccord (confirmed) | CGY +110 / SEA -130 | no edge | no edge | no edge |

## Thursday, November 5

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected goals | 80% range | Overtime | Puck line | Total: model / line | Goalies | Posted moneyline | Puck line edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 7:00 PM | UTA @ MTL | UTA 4, MTL 3 | UTA 54% | UTA -120 / MTL +120 | 3.3 – 3.1 | 1–6 / 1–5 | 21% | UTA -1.5 33% | 6.4 / 6.5 (over 48%) | Karel Vejmelka (expected) / Jacob Fowler (expected) | UTA -122 / MTL +102 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 7:00 PM | VGK @ DET | VGK 3, DET 2 | VGK 56% | VGK -130 / DET +130 | 3.3 – 2.9 | 1–6 / 1–5 | 22% | VGK -1.5 34% | 6.1 / 5.5 (over 54%) | Carter Hart (expected) / John Gibson (expected) | VGK -142 / DET +120 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 7:00 PM | CHI @ TBL | CHI 2, TBL 5 | TBL 79% | CHI +385 / TBL -385 | 2.2 – 4.3 | 0–4 / 2–7 | 17% | TBL -1.5 60% | 6.5 / 6.5 (over 48%) | Arvid Soderblom (expected) / Andrei Vasilevskiy (expected) | CHI +320 / TBL -410 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 7:00 PM | STL @ NJD | STL 2, NJD 3 | NJD 60% | STL +150 / NJD -150 | 2.7 – 3.4 | 1–5 / 1–6 | 22% | NJD -1.5 38% | 6.1 / 5.5 (over 53%) | Joel Hofer (expected) / Connor Hellebuyck (expected) | STL +154 / NJD -185 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 7:00 PM | CAR @ NYI | CAR 3, NYI 2 | CAR 62% | CAR -160 / NYI +160 | 3.4 – 2.7 | 1–6 / 1–5 | 21% | CAR -1.5 40% | 6.1 / 5.5 (over 53%) | Pyotr Kochetkov (expected) / Ilya Sorokin (expected) | CAR -166 / NYI +140 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 7:00 PM | PHI @ NYR | PHI 2, NYR 3 | NYR 57% | PHI +135 / NYR -135 | 2.8 – 3.2 | 1–5 / 1–6 | 22% | NYR -1.5 35% | 6.1 / 5.5 (over 53%) | Dan Vladar (expected) / James Reimer (expected) | PHI +130 / NYR -155 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 7:00 PM | BOS @ PIT | BOS 4, PIT 3 | BOS 51% | BOS -105 / PIT +105 | 3.3 – 3.2 | 1–6 / 1–6 | 22% | BOS -1.5 31% | 6.5 / 6.5 (over 49%) | Jeremy Swayman (expected) / Arturs Silovs (expected) | BOS -108 / PIT -112 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 7:00 PM | DAL @ CBJ | DAL 3, CBJ 2 | DAL 52% | DAL -110 / CBJ +110 | 3.0 – 2.9 | 1–5 / 1–5 | 24% | DAL -1.5 31% | 5.9 / 5.5 (over 50%) | Jake Oettinger (expected) / Jet Greaves (expected) | DAL -130 / CBJ +110 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 7:00 PM | VAN @ WPG | VAN 3, WPG 4 | WPG 66% | VAN +195 / WPG -195 | 2.7 – 3.8 | 1–5 / 1–6 | 20% | WPG -1.5 44% | 6.5 / 6.5 (over 50%) | Leevi Meriläinen (expected) / Stuart Skinner (expected) | VAN +180 / WPG -218 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 8:00 PM | ANA @ EDM | ANA 3, EDM 4 | EDM 61% | ANA +160 / EDM -160 | 3.1 – 3.8 | 1–5 / 1–6 | 21% | EDM -1.5 40% | 6.8 / 6.5 (over 55%) | Lukas Dostal (expected) / Tristan Jarry (expected) | ANA +154 / EDM -185 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 9:30 PM | NSH @ COL | NSH 3, COL 4 | COL 65% | NSH +190 / COL -190 | 2.8 – 3.8 | 1–5 / 1–6 | 20% | COL -1.5 44% | 6.5 / 6.5 (over 51%) | Juuse Saros (expected) / Mackenzie Blackwood (expected) | NSH +170 / COL -205 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |

## Friday, November 6

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected goals | 80% range | Overtime | Puck line | Total: model / line | Goalies | Posted moneyline | Puck line edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 7:00 PM | CBJ @ BUF | CBJ 3, BUF 4 | BUF 61% | CBJ +155 / BUF -155 | 2.9 – 3.6 | 1–5 / 1–6 | 20% | BUF -1.5 40% | 6.4 | Cam Talbot (expected) / Ukko-Pekka Luukkonen (expected) | – | no line yet (model fair BUF -1.5 +150 / CBJ +1.5 -150) | no line yet | no line yet |
| 8:00 PM | SJS @ MIN | SJS 3, MIN 4 | MIN 76% | SJS +315 / MIN -315 | 2.4 – 4.2 | 0–5 / 2–7 | 17% | MIN -1.5 56% | 6.6 | Yaroslav Askarov (expected) / Jesper Wallstedt (expected) | – | no line yet (model fair MIN -1.5 -125 / SJS +1.5 +125) | no line yet | no line yet |
| 8:00 PM | ANA @ CGY | ANA 3, CGY 4 | CGY 59% | ANA +145 / CGY -145 | 3.1 – 3.6 | 1–5 / 1–6 | 20% | CGY -1.5 38% | 6.7 | Ville Husso (expected) / Dustin Wolf (expected) | – | no line yet (model fair CGY -1.5 +160 / ANA +1.5 -160) | no line yet | no line yet |

\* price not posted; assumed -110.

## How the 2026-27 predictions have done

| Predictor | Games | Log loss | Brier | Winners | Goals MAE | Total MAE | 80% range hit |
|---|---|---|---|---|---|---|---|
| Final prediction | 246 | 0.6510 | 0.2296 | 61.0% | 1.39 | 1.79 | 89.4% |
| Model only (before blending) | 246 | 0.6532 | 0.2307 | 59.3% | – | – | – |
| Elo | 246 | 0.6672 | 0.2373 | 60.6% | – | – | – |
| Final prediction, games with a line | 112 | 0.6576 | 0.2327 | 58.0% | 1.39 | 1.84 | 89.3% |
| Model only, games with a line | 112 | 0.6624 | 0.2351 | 54.5% | – | – | – |
| Betting market (de-vigged moneyline) | 112 | 0.6588 | 0.2333 | 58.9% | – | 1.82 | – |

Log loss and Brier score the win chances (lower is better; a coin flip scores 0.693 and 0.250). Hockey is close to a coin flip, so differences in the third decimal matter, and only over hundreds of games. Goals MAE is the average miss on each team's goals.

Overtime: predicted in 21.6% of regular-season games, happened in 22.0%.

134 of these games were played before the predictor went live. They are backfilled walk-forward (each day predicted from earlier days only) with the actual starting goalies and no betting line. Every game since is graded on the prediction logged before puck drop.

### Betting edges

| Market | Edges | Record (W-L-P) | Staked | Units won | ROI | Expected ROI |
|---|---|---|---|---|---|---|
| Puck line | 1 | 0-1-0 | 1.3 | -1.29 | -100.0% | +11.8% |
| Moneyline | 8 | 4-4-0 | 8.7 | +1.83 | +21.2% | +6.4% |
| Total | 1 | 0-1-0 | 0.9 | -0.89 | -100.0% | +3.0% |

Moneyline moved toward the model's edge on the first line seen before puck drop: 20 of 23 games (87%).

Each edge at the stake and price logged with the last prediction before puck drop (edges logged before edges were priced from the final prediction are left out); pushes return the stake. Units are 1% of the bankroll; ROI is units won per unit staked, and expected ROI is what the edges' EVs promised. The moneyline moving toward the model's edge (closing line value) is the quickest sign that it knows something the market doesn't yet.

### Results, Tuesday, November 3

| Game | Predicted | Final | Win chance for winner | Inside 80% ranges | Goalies |
|---|---|---|---|---|---|
| UTA @ TOR | 4–3 | 3–2 | 58% | yes | Sebastian Cossa / Sergei Bobrovsky |
| WPG @ MTL | 2–3 | 5–4 (OT) | 40% | yes | Stuart Skinner / Jacob Fowler |
| DET @ TBL | 3–4 | 2–4 | 69% | yes | John Gibson / Andrei Vasilevskiy |
| STL @ NYR | 2–3 | 1–3 | 51% | yes | Joel Hofer / Dylan Garand |
| MIN @ PHI | 3–2 | 4–2 | 62% | yes | Jesper Wallstedt / Dan Vladar |
| VGK @ PIT | 3–4 | 3–2 | 47% | yes | Adin Hill / Arturs Silovs |
| DAL @ WSH | 2–3 | 6–5 | 49% | no | Jake Oettinger / Logan Thompson |
| COL @ CBJ | 4–3 | 2–7 | 46% | no | Scott Wedgewood / Cam Talbot |
| EDM @ NJD | 3–4 | 3–4 (SO) | 59% | yes | Tristan Jarry / Connor Hellebuyck |
| CAR @ NSH | 4–3 | 1–4 | 34% | yes | Pyotr Kochetkov / Juuse Saros |
| ANA @ VAN | 4–3 | 5–4 | 62% | yes | Laurent Brossoit / Kevin Lankinen |

## Power ratings

Goals per game better than an average team, from the goal-rate model: offense and defense combine 5-on-5 expected goals (score and venue adjusted), special teams and actual goals, each weighted against a preseason prior. Defense is positive when it holds opponents below average. Goaltending is rated separately below.

| # | Team | Net | Offense | Defense | 5v5 xGF/60 | 5v5 xGA/60 | PP xGF/60 | PK xGA/60 | Elo |
|---|---|---|---|---|---|---|---|---|---|
| 1 | CAR | +0.69 | +0.41 | +0.28 | 3.37 | 2.36 | 8.61 | 7.16 | 1578 |
| 2 | UTA | +0.46 | +0.23 | +0.23 | 3.13 | 2.34 | 8.13 | 8.35 | 1512 |
| 3 | TBL | +0.39 | +0.21 | +0.18 | 2.94 | 2.47 | 8.20 | 7.78 | 1541 |
| 4 | VGK | +0.33 | +0.05 | +0.28 | 2.69 | 2.33 | 9.07 | 7.23 | 1527 |
| 5 | MIN | +0.31 | +0.14 | +0.17 | 2.97 | 2.49 | 9.12 | 8.12 | 1548 |
| 6 | PIT | +0.28 | +0.22 | +0.06 | 3.06 | 2.58 | 7.87 | 7.81 | 1492 |
| 7 | NJD | +0.27 | +0.01 | +0.26 | 2.79 | 2.32 | 9.12 | 7.77 | 1513 |
| 8 | COL | +0.26 | +0.30 | -0.04 | 2.99 | 2.76 | 7.73 | 7.97 | 1548 |
| 9 | DAL | +0.25 | -0.08 | +0.33 | 2.49 | 2.27 | 9.28 | 7.31 | 1530 |
| 10 | FLA | +0.24 | +0.01 | +0.23 | 2.63 | 2.39 | 9.40 | 7.71 | 1502 |
| 11 | EDM | +0.10 | +0.09 | +0.01 | 2.54 | 2.67 | 9.66 | 8.08 | 1532 |
| 12 | BUF | +0.09 | +0.10 | -0.01 | 2.77 | 2.68 | 7.92 | 8.37 | 1521 |
| 13 | STL | +0.08 | -0.01 | +0.09 | 2.62 | 2.58 | 6.89 | 7.58 | 1503 |
| 14 | OTT | +0.06 | -0.03 | +0.09 | 2.64 | 2.56 | 8.03 | 8.31 | 1514 |
| 15 | WSH | +0.03 | +0.11 | -0.08 | 2.87 | 2.78 | 7.73 | 8.04 | 1514 |
| 16 | LAK | +0.02 | -0.11 | +0.13 | 2.57 | 2.54 | 8.12 | 8.25 | 1471 |
| 17 | NYR | +0.01 | +0.01 | -0.01 | 2.71 | 2.72 | 8.73 | 7.76 | 1491 |
| 18 | CBJ | -0.04 | -0.03 | -0.00 | 2.67 | 2.67 | 7.71 | 8.51 | 1496 |
| 19 | DET | -0.04 | -0.08 | +0.04 | 2.66 | 2.62 | 8.44 | 8.66 | 1485 |
| 20 | BOS | -0.04 | +0.03 | -0.07 | 2.72 | 2.81 | 7.73 | 8.12 | 1532 |
| 21 | MTL | -0.05 | +0.06 | -0.11 | 2.81 | 2.83 | 7.14 | 8.38 | 1530 |
| 22 | NYI | -0.09 | -0.07 | -0.02 | 2.70 | 2.73 | 7.53 | 8.54 | 1490 |
| 23 | NSH | -0.13 | -0.06 | -0.07 | 2.60 | 2.77 | 8.11 | 7.75 | 1489 |
| 24 | TOR | -0.14 | -0.02 | -0.12 | 2.49 | 2.83 | 8.74 | 8.39 | 1483 |
| 25 | WPG | -0.16 | -0.13 | -0.03 | 2.55 | 2.73 | 8.24 | 9.07 | 1464 |
| 26 | CGY | -0.23 | -0.11 | -0.12 | 2.58 | 2.83 | 7.23 | 8.12 | 1468 |
| 27 | PHI | -0.26 | -0.25 | -0.01 | 2.34 | 2.69 | 7.73 | 7.45 | 1473 |
| 28 | SEA | -0.26 | -0.10 | -0.16 | 2.42 | 2.87 | 7.22 | 8.54 | 1478 |
| 29 | ANA | -0.37 | -0.01 | -0.36 | 2.68 | 3.06 | 8.06 | 8.44 | 1482 |
| 30 | CHI | -0.70 | -0.27 | -0.43 | 2.34 | 3.15 | 7.22 | 8.31 | 1426 |
| 31 | VAN | -0.70 | -0.22 | -0.49 | 2.27 | 3.20 | 7.60 | 8.81 | 1409 |
| 32 | SJS | -0.81 | -0.25 | -0.56 | 2.30 | 3.30 | 7.25 | 8.82 | 1458 |

## Goalies

Each team's likeliest next starter. GSAx is goals saved above expected (from this predictor's own shot model), shrunk hard toward a slightly below-average prior, since goaltending repeats poorly from season to season.

| Team | Likely next starter | Share of recent starts | GSAx per 100 shots | Goals per game vs average |
|---|---|---|---|---|
| NYI | Ilya Sorokin | 71% | +0.39 | +0.16 |
| WSH | Logan Thompson | 72% | +0.36 | +0.15 |
| BOS | Jeremy Swayman | 74% | +0.32 | +0.14 |
| MTL | Jacob Fowler | 66% | +0.30 | +0.13 |
| MIN | Jesper Wallstedt | 88% | +0.24 | +0.10 |
| CGY | Devin Cooley | 47% | +0.21 | +0.09 |
| COL | Mackenzie Blackwood | 66% | +0.16 | +0.07 |
| OTT | Linus Ullmark | 40% | +0.14 | +0.06 |
| TBL | Andrei Vasilevskiy | 80% | +0.14 | +0.06 |
| CHI | Spencer Knight | 81% | +0.13 | +0.05 |
| CBJ | Jet Greaves | 50% | +0.10 | +0.04 |
| DAL | Jake Oettinger | 82% | +0.09 | +0.04 |
| CAR | Pyotr Kochetkov | 72% | +0.05 | +0.02 |
| STL | Joel Hofer | 76% | +0.04 | +0.02 |
| NYR | Dylan Garand | 71% | -0.01 | -0.01 |
| WPG | Stuart Skinner | 70% | -0.03 | -0.01 |
| PHI | Dan Vladar | 57% | -0.04 | -0.02 |
| NJD | Jake Allen | 48% | -0.06 | -0.02 |
| BUF | Ukko-Pekka Luukkonen | 63% | -0.13 | -0.05 |
| SJS | Yaroslav Askarov | 61% | -0.13 | -0.05 |
| TOR | Sergei Bobrovsky | 65% | -0.14 | -0.06 |
| FLA | Akira Schmid | 51% | -0.16 | -0.07 |
| ANA | Lukas Dostal | 51% | -0.17 | -0.07 |
| DET | John Gibson | 67% | -0.17 | -0.07 |
| NSH | Juuse Saros | 70% | -0.19 | -0.08 |
| SEA | Philipp Grubauer | 63% | -0.19 | -0.08 |
| LAK | Darcy Kuemper | 58% | -0.20 | -0.09 |
| UTA | Karel Vejmelka | 66% | -0.21 | -0.09 |
| VAN | Leevi Meriläinen | 58% | -0.29 | -0.12 |
| PIT | Arturs Silovs | 68% | -0.29 | -0.12 |
| EDM | Tristan Jarry | 56% | -0.31 | -0.13 |
| VGK | Adin Hill | 52% | -0.33 | -0.14 |

## Current model fit

- Fitted on 5838 games from 2022-23 to 2026-27.
- Home ice: +3.1% goals for the home team relative to the visitor.
- Second night of a back-to-back: -5.8% goals scored, +3.4% goals allowed.
- Starting goalie: each goal per game he saves above average lowers the opponent's rate by 22%.
- Blend: 54% on the betting line wherever there is one (fitted on 112 logged games, shrunk toward the backtest value).
- Simulator: 22.3% of recent regular-season games reached overtime; trailing teams usually have the goalie pulled with 2 minutes left when down one and 3 when down two; empty-net goals come at 0.40 a minute with the net empty; three-on-three overtime produces 1.03 goals per five minutes.
