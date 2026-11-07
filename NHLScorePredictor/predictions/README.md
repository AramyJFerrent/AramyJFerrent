# NHL score predictions

Updated Fri Nov 06, 2026 08:56 PM ET. Refreshed automatically several times a day during the season; each game's prediction is locked at puck drop and graded once the final score is in.

Each game is simulated 10,000 times minute by minute, with pulled goalies, empty-net goals, overtime and shootouts. The predicted score is the most common final score in which the likelier winner wins; as in the official result, a shootout winner gets one extra goal. Hockey is low-scoring and luck-heavy, so read the win chance and the ranges (80% of simulated outcomes for each team) before the single score.

Goalies marked with a percentage are projected from recent starts (the share is the chance he starts); "probable" or "confirmed" ones come from ESPN and replace the projection when available.

The fair moneyline is the American odds that match the win chance exactly, with no bookmaker margin: -150 means risk $150 to win $100, +150 means risk $100 to win $150. A sportsbook's price is a little worse on both sides because of its cut, so a book only offers value on a team when its price beats the fair line. The puck line is the favorite's chance to win by two or more.

The edge columns price each side of the puck line, moneyline and total with the final prediction: the model's goal rates blended with the market's, simulated against the posted lines, overtime and shootout included (the shootout winner gets one goal), and anchored to the market's own chances so only what the blend moves off the market counts. Each cell shows the side with the best expected value (EV) per $1 bet at the posted price. A side is an edge only if its EV is at least 3%: a pick shows its price, EV, its chance of winning the bet and its stake, a 25% share of the Kelly stake in units of 1% of the bankroll, with at most 3 units on one game; "no edge" means neither side clears the bar. A projected starting goalie is wrong about a third of the time and the market prices the real one, so edges wait until both starters are confirmed. A total with no posted price is assumed to be -110 (marked \*); the puck line and moneyline are never assumed, so without a price the cell shows the model's fair odds instead. Treat the edges as an experiment, not betting advice; see the backtest for how they have done on past seasons. Their record is tracked live below.

## Saturday, November 7

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected goals | 80% range | Overtime | Puck line | Total: model / line | Goalies | Posted moneyline | Puck line edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 12:30 PM | FLA @ WSH | FLA 3, WSH 4 | WSH 52% | FLA +110 / WSH -110 | 3.1 – 3.2 | 1–5 / 1–6 | 22% | WSH -1.5 32% | 6.3 / 6.5 (over 47%) | Jacob Markstrom (expected) / Logan Thompson (expected) | FLA +102 / WSH -122 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 1:00 PM | STL @ NSH | STL 3, NSH 2 | STL 51% | STL -105 / NSH +105 | 3.1 – 3.0 | 1–5 / 1–5 | 23% | STL -1.5 30% | 6.1 / 5.5 (over 54%) | Joel Hofer (expected) / Juuse Saros (expected) | STL -110 / NSH -110 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 5:00 PM | NYR @ SEA | NYR 4, SEA 3 | NYR 55% | NYR -120 / SEA +120 | 3.3 – 3.0 | 1–6 / 1–5 | 22% | NYR -1.5 34% | 6.3 / 6.5 (over 46%) | Dylan Garand (expected) / Philipp Grubauer (expected) | NYR -130 / SEA +110 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 7:00 PM | MTL @ TOR | MTL 4, TOR 3 | MTL 52% | MTL -110 / TOR +110 | 3.4 – 3.2 | 1–6 / 1–6 | 22% | MTL -1.5 32% | 6.6 / 6.5 (over 51%) | Jacob Fowler (expected) / Sergei Bobrovsky (expected) | MTL -115 / TOR -105 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 7:00 PM | UTA @ OTT | UTA 4, OTT 3 | UTA 54% | UTA -115 / OTT +115 | 3.4 – 3.1 | 1–6 / 1–5 | 22% | UTA -1.5 33% | 6.5 / 6.5 (over 50%) | Karel Vejmelka (expected) / Samuel Ersson (expected) | UTA -115 / OTT -105 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 7:00 PM | NJD @ NYI | NJD 3, NYI 2 | NJD 56% | NJD -130 / NYI +130 | 3.2 – 2.8 | 1–6 / 1–5 | 22% | NJD -1.5 34% | 6.1 / 5.5 (over 53%) | Connor Hellebuyck (expected) / Ilya Sorokin (expected) | NJD -148 / NYI +124 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 8:00 PM | CHI @ CAR | CHI 2, CAR 4 | CAR 78% | CHI +360 / CAR -360 | 2.3 – 4.2 | 0–4 / 2–7 | 17% | CAR -1.5 58% | 6.5 / 6.5 (over 49%) | Spencer Knight (expected) / Pyotr Kochetkov (expected) | CHI +320 / CAR -410 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 8:00 PM | SJS @ DAL | SJS 2, DAL 3 | DAL 74% | SJS +285 / DAL -285 | 2.3 – 3.9 | 0–5 / 2–6 | 19% | DAL -1.5 53% | 6.3 / 6.5 (over 46%) | Alex Nedeljkovic (expected) / Jake Oettinger (expected) | SJS +235 / DAL -290 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 8:00 PM | TBL @ MIN | TBL 4, MIN 3 | TBL 57% | TBL -130 / MIN +130 | 3.3 – 2.9 | 1–6 / 1–5 | 22% | TBL -1.5 35% | 6.2 / 6.5 (over 45%) | Andrei Vasilevskiy (expected) / Calvin Pickard (confirmed) | TBL -142 / MIN +120 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 9:00 PM | DET @ COL | DET 3, COL 4 | COL 64% | DET +175 / COL -175 | 2.8 – 3.7 | 1–5 / 1–6 | 21% | COL -1.5 43% | 6.5 / 6.5 (over 49%) | John Gibson (expected) / Mackenzie Blackwood (expected) | DET +185 / COL -225 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 9:00 PM | PIT @ LAK | PIT 3, LAK 4 | LAK 52% | PIT +110 / LAK -110 | 3.1 – 3.2 | 1–5 / 1–6 | 22% | LAK -1.5 32% | 6.3 / 6.5 (over 46%) | Arturs Silovs (expected) / Anton Forsberg (expected) | PIT +110 / LAK -130 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 10:00 PM | VAN @ EDM | VAN 3, EDM 4 | EDM 74% | VAN +280 / EDM -280 | 2.7 – 4.3 | 1–5 / 2–7 | 18% | EDM -1.5 54% | 7.0 / 6.5 (over 58%) | Leevi Meriläinen (expected) / Tristan Jarry (expected) | VAN +270 / EDM -340 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |

## Sunday, November 8

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected goals | 80% range | Overtime | Puck line | Total: model / line | Goalies | Posted moneyline | Puck line edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1:00 PM | FLA @ BOS | FLA 2, BOS 3 | BOS 58% | FLA +135 / BOS -135 | 2.8 – 3.2 | 1–5 / 1–6 | 22% | BOS -1.5 35% | 6.0 | Akira Schmid (expected) / Jeremy Swayman (expected) | – | no line yet (model fair BOS -1.5 +185 / FLA +1.5 -185) | no line yet | no line yet |
| 3:30 PM | VGK @ BUF | VGK 4, BUF 3 | VGK 53% | VGK -110 / BUF +110 | 3.2 – 3.0 | 1–6 / 1–5 | 21% | VGK -1.5 32% | 6.2 | Carter Hart (expected) / Ukko-Pekka Luukkonen (expected) | – | no line yet (model fair BUF +1.5 -210 / VGK -1.5 +210) | no line yet | no line yet |
| 6:00 PM | TBL @ WPG | TBL 3, WPG 2 | TBL 54% | TBL -115 / WPG +115 | 3.2 – 3.0 | 1–6 / 1–5 | 22% | TBL -1.5 33% | 6.2 | Dennis Hildeby (expected) / Stuart Skinner (expected) | – | no line yet (model fair WPG +1.5 -205 / TBL -1.5 +205) | no line yet | no line yet |
| 7:00 PM | NJD @ TOR | NJD 3, TOR 2 | NJD 54% | NJD -120 / TOR +120 | 3.2 – 2.9 | 1–6 / 1–5 | 23% | NJD -1.5 33% | 6.1 | Jake Allen (expected) / Anthony Stolarz (expected) | – | no line yet (model fair TOR +1.5 -200 / NJD -1.5 +200) | no line yet | no line yet |
| 7:00 PM | PHI @ CGY | PHI 2, CGY 3 | CGY 53% | PHI +110 / CGY -110 | 3.0 – 3.1 | 1–5 / 1–5 | 23% | CGY -1.5 31% | 6.1 | Joseph Woll (expected) / Dustin Wolf (expected) | – | no line yet (model fair CGY -1.5 +225 / PHI +1.5 -225) | no line yet | no line yet |
| 8:00 PM | PIT @ ANA | PIT 4, ANA 3 | PIT 53% | PIT -115 / ANA +115 | 3.5 – 3.3 | 1–6 / 1–6 | 21% | PIT -1.5 33% | 6.9 | Sergei Murashov (expected) / Laurent Brossoit (expected) | – | no line yet (model fair ANA +1.5 -205 / PIT -1.5 +205) | no line yet | no line yet |

\* price not posted; assumed -110.

## Monday, November 9

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected goals | 80% range | Overtime | Puck line | Total: model / line | Goalies | Posted moneyline | Puck line edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 8:00 PM | NYR @ EDM | NYR 3, EDM 4 | EDM 54% | NYR +120 / EDM -120 | 3.1 – 3.4 | 1–5 / 1–6 | 21% | EDM -1.5 34% | 6.6 | Dylan Garand (expected) / Tristan Jarry (expected) | – | no line yet (model fair EDM -1.5 +195 / NYR +1.5 -195) | no line yet | no line yet |
| 9:30 PM | PHI @ VAN | PHI 4, VAN 3 | PHI 53% | PHI -115 / VAN +115 | 3.3 – 3.1 | 1–6 / 1–5 | 22% | PHI -1.5 32% | 6.4 | Dan Vladar (expected) / Leevi Meriläinen (expected) | – | no line yet (model fair VAN +1.5 -210 / PHI -1.5 +210) | no line yet | no line yet |
| 10:00 PM | NYI @ SJS | NYI 4, SJS 3 | NYI 63% | NYI -170 / SJS +170 | 3.7 – 2.8 | 1–6 / 1–5 | 20% | NYI -1.5 42% | 6.6 | Ilya Sorokin (expected) / Yaroslav Askarov (expected) | – | no line yet (model fair SJS +1.5 -140 / NYI -1.5 +140) | no line yet | no line yet |

\* price not posted; assumed -110.

## How the 2026-27 predictions have done

| Predictor | Games | Log loss | Brier | Winners | Goals MAE | Total MAE | 80% range hit |
|---|---|---|---|---|---|---|---|
| Final prediction | 261 | 0.6490 | 0.2286 | 61.3% | 1.39 | 1.82 | 89.8% |
| Model only (before blending) | 261 | 0.6511 | 0.2297 | 59.4% | – | – | – |
| Elo | 261 | 0.6650 | 0.2362 | 61.3% | – | – | – |
| Final prediction, games with a line | 127 | 0.6526 | 0.2304 | 59.1% | 1.38 | 1.89 | 90.2% |
| Model only, games with a line | 127 | 0.6571 | 0.2327 | 55.1% | – | – | – |
| Betting market (de-vigged moneyline) | 127 | 0.6534 | 0.2308 | 59.1% | – | 1.87 | – |

Log loss and Brier score the win chances (lower is better; a coin flip scores 0.693 and 0.250). Hockey is close to a coin flip, so differences in the third decimal matter, and only over hundreds of games. Goals MAE is the average miss on each team's goals.

Overtime: predicted in 21.5% of regular-season games, happened in 22.6%.

134 of these games were played before the predictor went live. They are backfilled walk-forward (each day predicted from earlier days only) with the actual starting goalies and no betting line. Every game since is graded on the prediction logged before puck drop.

### Betting edges

| Market | Edges | Record (W-L-P) | Staked | Units won | ROI | Expected ROI |
|---|---|---|---|---|---|---|
| Puck line | 1 | 0-1-0 | 1.3 | -1.29 | -100.0% | +11.8% |
| Moneyline | 8 | 4-4-0 | 8.7 | +1.83 | +21.2% | +6.4% |
| Total | 1 | 0-1-0 | 0.9 | -0.89 | -100.0% | +3.0% |

Moneyline moved toward the model's edge on the first line seen before puck drop: 22 of 27 games (81%).

Each edge at the stake and price logged with the last prediction before puck drop (edges logged before edges were priced from the final prediction are left out); pushes return the stake. Units are 1% of the bankroll; ROI is units won per unit staked, and expected ROI is what the edges' EVs promised. The moneyline moving toward the model's edge (closing line value) is the quickest sign that it knows something the market doesn't yet.

### Results, Thursday, November 5

| Game | Predicted | Final | Win chance for winner | Inside 80% ranges | Goalies |
|---|---|---|---|---|---|
| UTA @ MTL | 4–3 | 4–5 (OT) | 46% | yes | Sebastian Cossa / Jakub Dobes |
| VGK @ DET | 3–2 | 2–1 | 55% | yes | Carter Hart / Daniil Tarasov |
| CHI @ TBL | 2–5 | 1–4 | 79% | yes | Arvid Soderblom / Andrei Vasilevskiy |
| STL @ NJD | 2–3 | 4–5 (OT) | 63% | yes | Jordan Binnington / Connor Hellebuyck |
| CAR @ NYI | 4–3 | 5–3 | 64% | yes | Brandon Bussi / Semyon Varlamov |
| PHI @ NYR | 2–3 | 2–3 | 58% | yes | Joseph Woll / Dylan Garand |
| BOS @ PIT | 4–3 | 6–2 | 50% | yes | Jeremy Swayman / Arturs Silovs |
| DAL @ CBJ | 3–2 | 1–2 (SO) | 46% | yes | Casey DeSmith / Cam Talbot |
| VAN @ WPG | 3–4 | 2–6 | 65% | yes | Leevi Meriläinen / Stuart Skinner |
| ANA @ EDM | 3–4 | 5–4 | 36% | yes | Laurent Brossoit / Matt Tomkins |
| NSH @ COL | 3–4 | 3–2 (OT) | 35% | yes | Justus Annunen / Mackenzie Blackwood |

## Power ratings

Goals per game better than an average team, from the goal-rate model: offense and defense combine 5-on-5 expected goals (score and venue adjusted), special teams and actual goals, each weighted against a preseason prior. Defense is positive when it holds opponents below average. Goaltending is rated separately below.

| # | Team | Net | Offense | Defense | 5v5 xGF/60 | 5v5 xGA/60 | PP xGF/60 | PK xGA/60 | Elo |
|---|---|---|---|---|---|---|---|---|---|
| 1 | CAR | +0.71 | +0.44 | +0.27 | 3.44 | 2.40 | 8.62 | 7.20 | 1581 |
| 2 | UTA | +0.47 | +0.24 | +0.24 | 3.14 | 2.35 | 8.21 | 8.78 | 1510 |
| 3 | TBL | +0.38 | +0.20 | +0.18 | 2.92 | 2.48 | 8.27 | 7.84 | 1544 |
| 4 | VGK | +0.33 | +0.04 | +0.29 | 2.70 | 2.34 | 9.15 | 7.29 | 1530 |
| 5 | MIN | +0.31 | +0.13 | +0.18 | 2.97 | 2.50 | 9.16 | 8.17 | 1548 |
| 6 | NJD | +0.25 | +0.03 | +0.22 | 2.83 | 2.39 | 9.14 | 7.87 | 1516 |
| 7 | PIT | +0.25 | +0.19 | +0.06 | 3.02 | 2.59 | 7.88 | 7.85 | 1486 |
| 8 | FLA | +0.24 | -0.01 | +0.26 | 2.59 | 2.37 | 9.53 | 7.70 | 1505 |
| 9 | COL | +0.23 | +0.28 | -0.04 | 2.97 | 2.78 | 7.73 | 8.09 | 1545 |
| 10 | DAL | +0.23 | -0.08 | +0.31 | 2.52 | 2.32 | 9.30 | 7.33 | 1527 |
| 11 | EDM | +0.10 | +0.10 | -0.01 | 2.60 | 2.70 | 9.72 | 8.07 | 1528 |
| 12 | OTT | +0.09 | -0.03 | +0.12 | 2.67 | 2.55 | 8.15 | 8.32 | 1517 |
| 13 | STL | +0.09 | +0.02 | +0.07 | 2.69 | 2.62 | 6.99 | 7.61 | 1501 |
| 14 | BUF | +0.06 | +0.08 | -0.02 | 2.77 | 2.71 | 7.94 | 8.48 | 1517 |
| 15 | WSH | +0.04 | +0.10 | -0.07 | 2.87 | 2.78 | 7.78 | 8.09 | 1514 |
| 16 | LAK | +0.03 | -0.10 | +0.13 | 2.57 | 2.56 | 8.27 | 8.30 | 1477 |
| 17 | BOS | +0.02 | +0.04 | -0.02 | 2.73 | 2.77 | 7.78 | 8.13 | 1539 |
| 18 | NYR | +0.00 | +0.02 | -0.02 | 2.74 | 2.74 | 8.71 | 7.80 | 1494 |
| 19 | CBJ | -0.04 | -0.03 | -0.01 | 2.72 | 2.70 | 7.72 | 8.54 | 1498 |
| 20 | DET | -0.04 | -0.09 | +0.04 | 2.66 | 2.63 | 8.50 | 8.73 | 1482 |
| 21 | MTL | -0.05 | +0.06 | -0.11 | 2.83 | 2.85 | 7.56 | 8.46 | 1533 |
| 22 | NSH | -0.10 | -0.06 | -0.04 | 2.63 | 2.75 | 8.23 | 7.74 | 1492 |
| 23 | NYI | -0.13 | -0.06 | -0.07 | 2.74 | 2.81 | 7.57 | 8.57 | 1486 |
| 24 | WPG | -0.13 | -0.12 | -0.01 | 2.57 | 2.73 | 8.23 | 9.09 | 1468 |
| 25 | TOR | -0.14 | -0.02 | -0.12 | 2.49 | 2.83 | 8.77 | 8.43 | 1483 |
| 26 | CGY | -0.23 | -0.11 | -0.12 | 2.61 | 2.84 | 7.28 | 8.09 | 1466 |
| 27 | PHI | -0.27 | -0.25 | -0.02 | 2.37 | 2.71 | 7.76 | 7.45 | 1471 |
| 28 | SEA | -0.29 | -0.11 | -0.18 | 2.44 | 2.90 | 7.19 | 8.58 | 1481 |
| 29 | ANA | -0.39 | +0.01 | -0.40 | 2.72 | 3.12 | 8.05 | 8.50 | 1486 |
| 30 | CHI | -0.64 | -0.28 | -0.36 | 2.33 | 3.08 | 7.21 | 8.50 | 1420 |
| 31 | VAN | -0.72 | -0.23 | -0.49 | 2.26 | 3.20 | 7.65 | 8.80 | 1404 |
| 32 | SJS | -0.81 | -0.25 | -0.56 | 2.32 | 3.29 | 7.31 | 8.95 | 1452 |

## Goalies

Each team's likeliest next starter. GSAx is goals saved above expected (from this predictor's own shot model), shrunk hard toward a slightly below-average prior, since goaltending repeats poorly from season to season.

| Team | Likely next starter | Share of recent starts | GSAx per 100 shots | Goals per game vs average |
|---|---|---|---|---|
| NYI | Ilya Sorokin | 62% | +0.38 | +0.16 |
| WSH | Logan Thompson | 72% | +0.36 | +0.15 |
| BOS | Jeremy Swayman | 66% | +0.32 | +0.14 |
| MTL | Jacob Fowler | 59% | +0.29 | +0.12 |
| MIN | Jesper Wallstedt | 88% | +0.24 | +0.10 |
| COL | Mackenzie Blackwood | 70% | +0.17 | +0.07 |
| TBL | Andrei Vasilevskiy | 82% | +0.16 | +0.07 |
| OTT | Linus Ullmark | 36% | +0.14 | +0.06 |
| CBJ | Jet Greaves | 68% | +0.10 | +0.04 |
| CHI | Spencer Knight | 75% | +0.10 | +0.04 |
| DAL | Jake Oettinger | 73% | +0.09 | +0.04 |
| CAR | Pyotr Kochetkov | 65% | +0.05 | +0.02 |
| STL | Joel Hofer | 68% | +0.04 | +0.01 |
| NYR | Dylan Garand | 74% | +0.01 | +0.00 |
| WPG | Stuart Skinner | 73% | -0.04 | -0.01 |
| PHI | Dan Vladar | 51% | -0.04 | -0.02 |
| NJD | Jake Allen | 43% | -0.06 | -0.02 |
| VGK | Carter Hart | 53% | -0.12 | -0.05 |
| BUF | Ukko-Pekka Luukkonen | 55% | -0.13 | -0.05 |
| TOR | Sergei Bobrovsky | 65% | -0.14 | -0.06 |
| ANA | Lukas Dostal | 56% | -0.17 | -0.07 |
| DET | John Gibson | 60% | -0.17 | -0.07 |
| LAK | Darcy Kuemper | 63% | -0.19 | -0.08 |
| NSH | Juuse Saros | 62% | -0.19 | -0.08 |
| SEA | Philipp Grubauer | 55% | -0.19 | -0.08 |
| SJS | Yaroslav Askarov | 65% | -0.21 | -0.09 |
| UTA | Karel Vejmelka | 59% | -0.21 | -0.09 |
| CGY | Dustin Wolf | 49% | -0.23 | -0.10 |
| FLA | Jacob Markstrom | 47% | -0.30 | -0.12 |
| EDM | Tristan Jarry | 51% | -0.31 | -0.13 |
| VAN | Leevi Meriläinen | 62% | -0.36 | -0.15 |
| PIT | Arturs Silovs | 72% | -0.37 | -0.15 |

## Current model fit

- Fitted on 5853 games from 2022-23 to 2026-27.
- Home ice: +3.1% goals for the home team relative to the visitor.
- Second night of a back-to-back: -5.8% goals scored, +3.4% goals allowed.
- Starting goalie: each goal per game he saves above average lowers the opponent's rate by 22%.
- Blend: 47% on the betting line wherever there is one (fitted on 127 logged games, shrunk toward the backtest value).
- Simulator: 22.3% of recent regular-season games reached overtime; trailing teams usually have the goalie pulled with 2 minutes left when down one and 3 when down two; empty-net goals come at 0.40 a minute with the net empty; three-on-three overtime produces 1.03 goals per five minutes.
