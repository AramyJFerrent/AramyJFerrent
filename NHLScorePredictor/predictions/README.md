# NHL score predictions

Updated Thu Nov 05, 2026 03:46 PM ET. Refreshed automatically several times a day during the season; each game's prediction is locked at puck drop and graded once the final score is in.

Each game is simulated 10,000 times minute by minute, with pulled goalies, empty-net goals, overtime and shootouts. The predicted score is the most common final score in which the likelier winner wins; as in the official result, a shootout winner gets one extra goal. Hockey is low-scoring and luck-heavy, so read the win chance and the ranges (80% of simulated outcomes for each team) before the single score.

Goalies marked with a percentage are projected from recent starts (the share is the chance he starts); "probable" or "confirmed" ones come from ESPN and replace the projection when available.

The fair moneyline is the American odds that match the win chance exactly, with no bookmaker margin: -150 means risk $150 to win $100, +150 means risk $100 to win $150. A sportsbook's price is a little worse on both sides because of its cut, so a book only offers value on a team when its price beats the fair line. The puck line is the favorite's chance to win by two or more.

The edge columns price each side of the puck line, moneyline and total with the final prediction: the model's goal rates blended with the market's, simulated against the posted lines, overtime and shootout included (the shootout winner gets one goal), and anchored to the market's own chances so only what the blend moves off the market counts. Each cell shows the side with the best expected value (EV) per $1 bet at the posted price. A side is an edge only if its EV is at least 3%: a pick shows its price, EV, its chance of winning the bet and its stake, a 25% share of the Kelly stake in units of 1% of the bankroll, with at most 3 units on one game; "no edge" means neither side clears the bar. A projected starting goalie is wrong about a third of the time and the market prices the real one, so edges wait until both starters are confirmed. A total with no posted price is assumed to be -110 (marked \*); the puck line and moneyline are never assumed, so without a price the cell shows the model's fair odds instead. Treat the edges as an experiment, not betting advice; see the backtest for how they have done on past seasons. Their record is tracked live below.

## Thursday, November 5

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected goals | 80% range | Overtime | Puck line | Total: model / line | Goalies | Posted moneyline | Puck line edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 7:00 PM | UTA @ MTL | UTA 4, MTL 3 | UTA 53% | UTA -115 / MTL +115 | 3.3 – 3.1 | 1–6 / 1–5 | 22% | UTA -1.5 33% | 6.5 / 6.5 (over 49%) | Sebastian Cossa (confirmed) / Jakub Dobes (confirmed) | UTA -122 / MTL +102 | no edge | no edge | no edge |
| 7:00 PM | VGK @ DET | VGK 3, DET 2 | VGK 56% | VGK -125 / DET +125 | 3.2 – 2.8 | 1–6 / 1–5 | 22% | VGK -1.5 34% | 6.1 / 5.5 (over 54%) | Carter Hart (expected) / Daniil Tarasov (expected) | VGK -142 / DET +120 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 7:00 PM | CHI @ TBL | CHI 2, TBL 5 | TBL 80% | CHI +405 / TBL -405 | 2.2 – 4.3 | 0–4 / 2–7 | 16% | TBL -1.5 61% | 6.6 / 6.5 (over 50%) | Arvid Soderblom (expected) / Andrei Vasilevskiy (expected) | CHI +350 / TBL -455 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 7:00 PM | STL @ NJD | STL 2, NJD 3 | NJD 63% | STL +170 / NJD -170 | 2.7 – 3.5 | 1–5 / 1–6 | 21% | NJD -1.5 41% | 6.1 / 5.5 (over 55%) | Jordan Binnington (confirmed) / Connor Hellebuyck (confirmed) | STL +180 / NJD -218 | no edge | STL (+180): EV +4.4%, 37%, stake 0.6u | no edge |
| 7:00 PM | CAR @ NYI | CAR 4, NYI 3 | CAR 65% | CAR -185 / NYI +185 | 3.6 – 2.7 | 1–6 / 1–5 | 22% | CAR -1.5 43% | 6.3 / 6.5 (over 46%) | Pyotr Kochetkov (expected) / Semyon Varlamov (confirmed) | CAR -198 / NYI +164 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 7:00 PM | PHI @ NYR | PHI 2, NYR 3 | NYR 58% | PHI +140 / NYR -140 | 2.8 – 3.3 | 1–5 / 1–6 | 23% | NYR -1.5 36% | 6.1 / 5.5 (over 54%) | Joseph Woll (confirmed) / Dylan Garand (confirmed) | PHI +124 / NYR -148 | no edge | no edge | no edge |
| 7:00 PM | BOS @ PIT | BOS 3, PIT 4 | PIT 50% | BOS +100 / PIT -100 | 3.3 – 3.3 | 1–6 / 1–6 | 22% | PIT -1.5 30% | 6.5 / 6.5 (over 50%) | Jeremy Swayman (expected) / Arturs Silovs (confirmed) | BOS -108 / PIT -112 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 7:00 PM | DAL @ CBJ | DAL 3, CBJ 2 | DAL 54% | DAL -115 / CBJ +115 | 3.1 – 2.9 | 1–5 / 1–5 | 22% | DAL -1.5 33% | 6.0 / 5.5 (over 52%) | Casey DeSmith (confirmed) / Cam Talbot (confirmed) | DAL -130 / CBJ +110 | no edge | no edge | no edge |
| 7:00 PM | VAN @ WPG | VAN 3, WPG 4 | WPG 65% | VAN +190 / WPG -190 | 2.7 – 3.8 | 1–5 / 1–6 | 20% | WPG -1.5 44% | 6.5 / 6.5 (over 49%) | Leevi Meriläinen (confirmed) / Stuart Skinner (confirmed) | VAN +180 / WPG -218 | no edge | no edge | no edge |
| 8:00 PM | ANA @ EDM | ANA 3, EDM 4 | EDM 63% | ANA +175 / EDM -175 | 3.0 – 3.9 | 1–5 / 1–6 | 20% | EDM -1.5 43% | 6.9 / 6.5 (over 56%) | Laurent Brossoit (confirmed) / Matt Tomkins (confirmed) | ANA +160 / EDM -192 | no edge | no edge | no edge |
| 9:30 PM | NSH @ COL | NSH 3, COL 4 | COL 65% | NSH +185 / COL -185 | 2.8 – 3.8 | 1–5 / 1–6 | 20% | COL -1.5 44% | 6.5 / 6.5 (over 51%) | Juuse Saros (expected) / Mackenzie Blackwood (confirmed) | NSH +180 / COL -218 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |

## Friday, November 6

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected goals | 80% range | Overtime | Puck line | Total: model / line | Goalies | Posted moneyline | Puck line edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 7:00 PM | CBJ @ BUF | CBJ 3, BUF 4 | BUF 61% | CBJ +155 / BUF -155 | 2.9 – 3.6 | 1–5 / 1–6 | 21% | BUF -1.5 39% | 6.5 / 6.5 (over 49%) | Cam Talbot (expected) / Ukko-Pekka Luukkonen (expected) | CBJ +150 / BUF -180 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 8:00 PM | SJS @ MIN | SJS 3, MIN 4 | MIN 73% | SJS +275 / MIN -275 | 2.5 – 4.1 | 1–5 / 2–7 | 19% | MIN -1.5 52% | 6.5 / 6.5 (over 50%) | Yaroslav Askarov (expected) / Jesper Wallstedt (expected) | SJS +210 / MIN -258 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 8:00 PM | ANA @ CGY | ANA 3, CGY 4 | CGY 56% | ANA +125 / CGY -125 | 3.1 – 3.5 | 1–6 / 1–6 | 22% | CGY -1.5 35% | 6.6 / 6.5 (over 51%) | Ville Husso (expected) / Dustin Wolf (expected) | ANA +102 / CGY -122 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |

## Saturday, November 7

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected goals | 80% range | Overtime | Puck line | Total: model / line | Goalies | Posted moneyline | Puck line edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 12:30 PM | FLA @ WSH | FLA 2, WSH 3 | WSH 53% | FLA +110 / WSH -110 | 3.0 – 3.2 | 1–5 / 1–6 | 22% | WSH -1.5 32% | 6.2 | Jacob Markstrom (expected) / Logan Thompson (expected) | – | no line yet (model fair WSH -1.5 +210 / FLA +1.5 -210) | no line yet | no line yet |
| 1:00 PM | STL @ NSH | STL 3, NSH 2 | STL 53% | STL -115 / NSH +115 | 3.2 – 3.0 | 1–6 / 1–5 | 23% | STL -1.5 32% | 6.2 | Joel Hofer (expected) / Juuse Saros (expected) | – | no line yet (model fair NSH +1.5 -210 / STL -1.5 +210) | no line yet | no line yet |
| 5:00 PM | NYR @ SEA | NYR 4, SEA 3 | NYR 53% | NYR -115 / SEA +115 | 3.4 – 3.1 | 1–6 / 1–6 | 22% | NYR -1.5 33% | 6.5 | Dylan Garand (expected) / Philipp Grubauer (expected) | – | no line yet (model fair SEA +1.5 -200 / NYR -1.5 +200) | no line yet | no line yet |
| 7:00 PM | MTL @ TOR | MTL 4, TOR 3 | MTL 52% | MTL -110 / TOR +110 | 3.4 – 3.2 | 1–6 / 1–6 | 21% | MTL -1.5 32% | 6.6 | Jacob Fowler (expected) / Sergei Bobrovsky (expected) | – | no line yet (model fair TOR +1.5 -210 / MTL -1.5 +210) | no line yet | no line yet |
| 7:00 PM | UTA @ OTT | UTA 4, OTT 3 | UTA 57% | UTA -130 / OTT +130 | 3.4 – 3.0 | 1–6 / 1–5 | 22% | UTA -1.5 35% | 6.3 | Karel Vejmelka (expected) / Samuel Ersson (expected) | – | no line yet (model fair OTT +1.5 -185 / UTA -1.5 +185) | no line yet | no line yet |
| 7:00 PM | NJD @ NYI | NJD 3, NYI 2 | NJD 53% | NJD -115 / NYI +115 | 3.1 – 2.8 | 1–5 / 1–5 | 24% | NJD -1.5 31% | 5.9 | Connor Hellebuyck (expected) / Ilya Sorokin (expected) | – | no line yet (model fair NYI +1.5 -220 / NJD -1.5 +220) | no line yet | no line yet |
| 8:00 PM | CHI @ CAR | CHI 2, CAR 5 | CAR 80% | CHI +400 / CAR -400 | 2.3 – 4.4 | 0–4 / 2–7 | 16% | CAR -1.5 60% | 6.6 | Spencer Knight (expected) / Pyotr Kochetkov (expected) | – | no line yet (model fair CAR -1.5 -155 / CHI +1.5 +155) | no line yet | no line yet |
| 8:00 PM | SJS @ DAL | SJS 2, DAL 4 | DAL 76% | SJS +320 / DAL -320 | 2.2 – 4.0 | 0–4 / 2–7 | 17% | DAL -1.5 56% | 6.2 | Alex Nedeljkovic (expected) / Jake Oettinger (expected) | – | no line yet (model fair DAL -1.5 -130 / SJS +1.5 +130) | no line yet | no line yet |
| 8:00 PM | TBL @ MIN | TBL 4, MIN 3 | TBL 56% | TBL -130 / MIN +130 | 3.3 – 3.0 | 1–6 / 1–5 | 22% | TBL -1.5 35% | 6.3 | Andrei Vasilevskiy (expected) / Calvin Pickard (expected) | – | no line yet (model fair MIN +1.5 -190 / TBL -1.5 +190) | no line yet | no line yet |
| 9:00 PM | DET @ COL | DET 3, COL 4 | COL 62% | DET +165 / COL -165 | 2.9 – 3.7 | 1–5 / 1–6 | 21% | COL -1.5 41% | 6.5 | John Gibson (expected) / Mackenzie Blackwood (expected) | – | no line yet (model fair COL -1.5 +145 / DET +1.5 -145) | no line yet | no line yet |
| 9:00 PM | PIT @ LAK | PIT 2, LAK 3 | LAK 50% | PIT +100 / LAK -100 | 3.1 – 3.1 | 1–5 / 1–5 | 22% | LAK -1.5 29% | 6.2 | Arturs Silovs (expected) / Anton Forsberg (expected) | – | no line yet (model fair LAK -1.5 +240 / PIT +1.5 -240) | no line yet | no line yet |
| 10:00 PM | VAN @ EDM | VAN 3, EDM 4 | EDM 70% | VAN +230 / EDM -230 | 2.8 – 4.2 | 1–5 / 2–7 | 19% | EDM -1.5 50% | 6.9 | Leevi Meriläinen (expected) / Tristan Jarry (expected) | – | no line yet (model fair EDM -1.5 +100 / VAN +1.5 -100) | no line yet | no line yet |

\* price not posted; assumed -110.

## How the 2026-27 predictions have done

| Predictor | Games | Log loss | Brier | Winners | Goals MAE | Total MAE | 80% range hit |
|---|---|---|---|---|---|---|---|
| Final prediction | 250 | 0.6495 | 0.2289 | 61.2% | 1.39 | 1.81 | 89.4% |
| Model only (before blending) | 250 | 0.6517 | 0.2300 | 59.6% | – | – | – |
| Elo | 250 | 0.6661 | 0.2367 | 60.8% | – | – | – |
| Final prediction, games with a line | 116 | 0.6542 | 0.2311 | 58.6% | 1.40 | 1.87 | 89.2% |
| Model only, games with a line | 116 | 0.6588 | 0.2334 | 55.2% | – | – | – |
| Betting market (de-vigged moneyline) | 116 | 0.6554 | 0.2317 | 59.5% | – | 1.85 | – |

Log loss and Brier score the win chances (lower is better; a coin flip scores 0.693 and 0.250). Hockey is close to a coin flip, so differences in the third decimal matter, and only over hundreds of games. Goals MAE is the average miss on each team's goals.

Overtime: predicted in 21.6% of regular-season games, happened in 22.0%.

134 of these games were played before the predictor went live. They are backfilled walk-forward (each day predicted from earlier days only) with the actual starting goalies and no betting line. Every game since is graded on the prediction logged before puck drop.

### Betting edges

| Market | Edges | Record (W-L-P) | Staked | Units won | ROI | Expected ROI |
|---|---|---|---|---|---|---|
| Puck line | 1 | 0-1-0 | 1.3 | -1.29 | -100.0% | +11.8% |
| Moneyline | 8 | 4-4-0 | 8.7 | +1.83 | +21.2% | +6.4% |
| Total | 1 | 0-1-0 | 0.9 | -0.89 | -100.0% | +3.0% |

Moneyline moved toward the model's edge on the first line seen before puck drop: 20 of 24 games (83%).

Each edge at the stake and price logged with the last prediction before puck drop (edges logged before edges were priced from the final prediction are left out); pushes return the stake. Units are 1% of the bankroll; ROI is units won per unit staked, and expected ROI is what the edges' EVs promised. The moneyline moving toward the model's edge (closing line value) is the quickest sign that it knows something the market doesn't yet.

### Results, Wednesday, November 4

| Game | Predicted | Final | Win chance for winner | Inside 80% ranges | Goalies |
|---|---|---|---|---|---|
| OTT @ BUF | 3–4 | 2–1 | 45% | yes | Samuel Ersson / Colten Ellis |
| CHI @ FLA | 2–3 | 3–5 | 69% | yes | Spencer Knight / Jacob Markstrom |
| SJS @ LAK | 3–4 | 2–7 | 64% | no | Yaroslav Askarov / Darcy Kuemper |
| CGY @ SEA | 3–4 | 1–2 (OT) | 55% | yes | Dustin Wolf / Joey Daccord |

## Power ratings

Goals per game better than an average team, from the goal-rate model: offense and defense combine 5-on-5 expected goals (score and venue adjusted), special teams and actual goals, each weighted against a preseason prior. Defense is positive when it holds opponents below average. Goaltending is rated separately below.

| # | Team | Net | Offense | Defense | 5v5 xGF/60 | 5v5 xGA/60 | PP xGF/60 | PK xGA/60 | Elo |
|---|---|---|---|---|---|---|---|---|---|
| 1 | CAR | +0.69 | +0.41 | +0.28 | 3.37 | 2.36 | 8.62 | 7.17 | 1578 |
| 2 | UTA | +0.46 | +0.23 | +0.23 | 3.13 | 2.34 | 8.14 | 8.37 | 1512 |
| 3 | TBL | +0.39 | +0.21 | +0.18 | 2.94 | 2.47 | 8.21 | 7.80 | 1541 |
| 4 | VGK | +0.33 | +0.05 | +0.28 | 2.69 | 2.33 | 9.08 | 7.25 | 1527 |
| 5 | MIN | +0.31 | +0.14 | +0.17 | 2.97 | 2.49 | 9.13 | 8.14 | 1548 |
| 6 | PIT | +0.28 | +0.22 | +0.06 | 3.06 | 2.58 | 7.89 | 7.82 | 1492 |
| 7 | NJD | +0.28 | +0.02 | +0.26 | 2.79 | 2.32 | 9.13 | 7.78 | 1513 |
| 8 | COL | +0.26 | +0.30 | -0.04 | 2.99 | 2.76 | 7.74 | 7.98 | 1548 |
| 9 | DAL | +0.25 | -0.08 | +0.33 | 2.49 | 2.27 | 9.28 | 7.33 | 1530 |
| 10 | FLA | +0.24 | -0.01 | +0.25 | 2.58 | 2.36 | 9.51 | 7.66 | 1505 |
| 11 | EDM | +0.10 | +0.09 | +0.01 | 2.54 | 2.67 | 9.67 | 8.09 | 1532 |
| 12 | OTT | +0.08 | -0.02 | +0.11 | 2.67 | 2.55 | 8.11 | 8.29 | 1517 |
| 13 | STL | +0.08 | -0.01 | +0.09 | 2.62 | 2.58 | 6.91 | 7.59 | 1503 |
| 14 | BUF | +0.06 | +0.09 | -0.03 | 2.76 | 2.71 | 7.91 | 8.46 | 1517 |
| 15 | WSH | +0.03 | +0.11 | -0.08 | 2.87 | 2.77 | 7.74 | 8.05 | 1514 |
| 16 | LAK | +0.03 | -0.09 | +0.12 | 2.56 | 2.55 | 8.24 | 8.26 | 1477 |
| 17 | NYR | +0.01 | +0.01 | -0.01 | 2.71 | 2.72 | 8.74 | 7.78 | 1491 |
| 18 | CBJ | -0.04 | -0.03 | -0.00 | 2.67 | 2.67 | 7.72 | 8.52 | 1496 |
| 19 | DET | -0.04 | -0.07 | +0.03 | 2.66 | 2.62 | 8.45 | 8.67 | 1485 |
| 20 | BOS | -0.04 | +0.03 | -0.07 | 2.72 | 2.81 | 7.74 | 8.14 | 1532 |
| 21 | MTL | -0.05 | +0.06 | -0.11 | 2.81 | 2.83 | 7.15 | 8.39 | 1530 |
| 22 | NYI | -0.09 | -0.07 | -0.02 | 2.70 | 2.73 | 7.54 | 8.56 | 1490 |
| 23 | NSH | -0.13 | -0.06 | -0.07 | 2.60 | 2.77 | 8.12 | 7.77 | 1489 |
| 24 | TOR | -0.14 | -0.02 | -0.12 | 2.49 | 2.83 | 8.75 | 8.41 | 1483 |
| 25 | WPG | -0.16 | -0.13 | -0.03 | 2.55 | 2.73 | 8.25 | 9.07 | 1464 |
| 26 | CGY | -0.23 | -0.10 | -0.13 | 2.60 | 2.83 | 7.24 | 8.06 | 1466 |
| 27 | PHI | -0.26 | -0.25 | -0.01 | 2.34 | 2.68 | 7.74 | 7.47 | 1473 |
| 28 | SEA | -0.29 | -0.11 | -0.18 | 2.43 | 2.89 | 7.16 | 8.55 | 1481 |
| 29 | ANA | -0.37 | -0.01 | -0.36 | 2.68 | 3.06 | 8.07 | 8.45 | 1482 |
| 30 | CHI | -0.66 | -0.27 | -0.39 | 2.32 | 3.10 | 7.17 | 8.43 | 1423 |
| 31 | VAN | -0.71 | -0.22 | -0.49 | 2.27 | 3.20 | 7.62 | 8.82 | 1409 |
| 32 | SJS | -0.81 | -0.25 | -0.56 | 2.31 | 3.28 | 7.27 | 8.93 | 1452 |

## Goalies

Each team's likeliest next starter. GSAx is goals saved above expected (from this predictor's own shot model), shrunk hard toward a slightly below-average prior, since goaltending repeats poorly from season to season.

| Team | Likely next starter | Share of recent starts | GSAx per 100 shots | Goals per game vs average |
|---|---|---|---|---|
| NYI | Ilya Sorokin | 71% | +0.39 | +0.16 |
| WSH | Logan Thompson | 72% | +0.36 | +0.15 |
| BOS | Jeremy Swayman | 74% | +0.32 | +0.14 |
| MTL | Jacob Fowler | 66% | +0.30 | +0.12 |
| MIN | Jesper Wallstedt | 88% | +0.24 | +0.10 |
| COL | Mackenzie Blackwood | 66% | +0.16 | +0.07 |
| OTT | Linus Ullmark | 36% | +0.14 | +0.06 |
| TBL | Andrei Vasilevskiy | 80% | +0.14 | +0.06 |
| CBJ | Jet Greaves | 50% | +0.10 | +0.04 |
| CHI | Spencer Knight | 65% | +0.10 | +0.04 |
| DAL | Jake Oettinger | 82% | +0.09 | +0.04 |
| CAR | Pyotr Kochetkov | 72% | +0.05 | +0.02 |
| STL | Joel Hofer | 76% | +0.04 | +0.02 |
| NYR | Dylan Garand | 71% | -0.01 | -0.01 |
| WPG | Stuart Skinner | 70% | -0.03 | -0.01 |
| PHI | Dan Vladar | 57% | -0.04 | -0.02 |
| NJD | Jake Allen | 48% | -0.06 | -0.02 |
| BUF | Ukko-Pekka Luukkonen | 55% | -0.13 | -0.05 |
| TOR | Sergei Bobrovsky | 65% | -0.14 | -0.06 |
| ANA | Lukas Dostal | 51% | -0.17 | -0.07 |
| DET | John Gibson | 67% | -0.17 | -0.07 |
| LAK | Darcy Kuemper | 63% | -0.18 | -0.08 |
| NSH | Juuse Saros | 70% | -0.19 | -0.08 |
| SEA | Philipp Grubauer | 55% | -0.19 | -0.08 |
| SJS | Yaroslav Askarov | 65% | -0.20 | -0.09 |
| UTA | Karel Vejmelka | 66% | -0.21 | -0.09 |
| CGY | Dustin Wolf | 49% | -0.23 | -0.10 |
| VAN | Leevi Meriläinen | 58% | -0.29 | -0.12 |
| PIT | Arturs Silovs | 68% | -0.29 | -0.12 |
| FLA | Jacob Markstrom | 47% | -0.30 | -0.12 |
| EDM | Tristan Jarry | 56% | -0.31 | -0.13 |
| VGK | Adin Hill | 52% | -0.33 | -0.14 |

## Current model fit

- Fitted on 5842 games from 2022-23 to 2026-27.
- Home ice: +3.1% goals for the home team relative to the visitor.
- Second night of a back-to-back: -5.8% goals scored, +3.4% goals allowed.
- Starting goalie: each goal per game he saves above average lowers the opponent's rate by 22%.
- Blend: 49% on the betting line wherever there is one (fitted on 116 logged games, shrunk toward the backtest value).
- Simulator: 22.3% of recent regular-season games reached overtime; trailing teams usually have the goalie pulled with 2 minutes left when down one and 3 when down two; empty-net goals come at 0.40 a minute with the net empty; three-on-three overtime produces 1.03 goals per five minutes.
