# NHL score predictions

Updated Tue Oct 27, 2026 04:50 PM ET. Refreshed automatically several times a day during the season; each game's prediction is locked at puck drop and graded once the final score is in.

Each game is simulated 10,000 times minute by minute, with pulled goalies, empty-net goals, overtime and shootouts. The predicted score is the most common final score in which the likelier winner wins; as in the official result, a shootout winner gets one extra goal. Hockey is low-scoring and luck-heavy, so read the win chance and the ranges (80% of simulated outcomes for each team) before the single score.

Goalies marked with a percentage are projected from recent starts (the share is the chance he starts); "probable" or "confirmed" ones come from ESPN and replace the projection when available.

The fair moneyline is the American odds that match the win chance exactly, with no bookmaker margin: -150 means risk $150 to win $100, +150 means risk $100 to win $150. A sportsbook's price is a little worse on both sides because of its cut, so a book only offers value on a team when its price beats the fair line. The puck line is the favorite's chance to win by two or more.

The edge columns price each side of the puck line, moneyline and total with the final prediction: the model's goal rates blended with the market's, simulated against the posted lines, overtime and shootout included (the shootout winner gets one goal), and anchored to the market's own chances so only what the blend moves off the market counts. Each cell shows the side with the best expected value (EV) per $1 bet at the posted price. A side is an edge only if its EV is at least 3%: a pick shows its price, EV, its chance of winning the bet and its stake, a 25% share of the Kelly stake in units of 1% of the bankroll, with at most 3 units on one game; "no edge" means neither side clears the bar. A projected starting goalie is wrong about a third of the time and the market prices the real one, so edges wait until both starters are confirmed. A total with no posted price is assumed to be -110 (marked \*); the puck line and moneyline are never assumed, so without a price the cell shows the model's fair odds instead. Treat the edges as an experiment, not betting advice; see the backtest for how they have done on past seasons. Their record is tracked live below.

## Tuesday, October 27

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected goals | 80% range | Overtime | Puck line | Total: model / line | Goalies | Posted moneyline | Puck line edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 7:00 PM | CBJ @ PHI | CBJ 3, PHI 2 | CBJ 51% | CBJ -105 / PHI +105 | 3.0 – 2.9 | 1–5 / 1–5 | 23% | CBJ -1.5 31% | 6.0 / 5.5 (over 52%) | Cam Talbot (confirmed) / Dan Vladar (confirmed) | CBJ -120 / PHI +100 | no edge | no edge | no edge |
| 8:00 PM | BOS @ CAR | BOS 3, CAR 4 | CAR 62% | BOS +160 / CAR -160 | 2.8 – 3.6 | 1–5 / 1–6 | 22% | CAR -1.5 40% | 6.4 / 6.5 (over 47%) | Jeremy Swayman (confirmed) / Pyotr Kochetkov (expected) | BOS +160 / CAR -192 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 8:00 PM | LAK @ CHI | LAK 3, CHI 2 | LAK 54% | LAK -115 / CHI +115 | 3.1 – 2.9 | 1–5 / 1–5 | 23% | LAK -1.5 32% | 6.0 / 5.5 (over 52%) | Anton Forsberg (expected) / Spencer Knight (confirmed) | LAK -108 / CHI -112 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 8:00 PM | MTL @ STL | MTL 3, STL 4 | STL 50% | MTL +100 / STL -100 | 3.1 – 3.2 | 1–6 / 1–6 | 23% | STL -1.5 29% | 6.3 / 6.5 (over 46%) | Jacob Fowler (confirmed) / Jordan Binnington (confirmed) | MTL -115 / STL -105 | no edge | no edge | no edge |
| 8:00 PM | NYI @ NSH | NYI 2, NSH 3 | NSH 51% | NYI +100 / NSH -100 | 3.1 – 3.1 | 1–5 / 1–5 | 22% | NSH -1.5 30% | 6.1 / 5.5 (over 55%) | Semyon Varlamov (confirmed) / Juuse Saros (confirmed) | NYI +102 / NSH -122 | no edge | no edge | no edge |
| 8:00 PM | NJD @ DAL | NJD 2, DAL 3 | DAL 52% | NJD +110 / DAL -110 | 2.8 – 2.9 | 1–5 / 1–5 | 23% | DAL -1.5 30% | 5.7 / 5.5 (over 48%) | Connor Hellebuyck (confirmed) / Casey DeSmith (confirmed) | NJD -105 / DAL -115 | no edge | no edge | no edge |
| 8:00 PM | FLA @ WPG | FLA 3, WPG 2 | FLA 54% | FLA -120 / WPG +120 | 3.2 – 2.9 | 1–6 / 1–5 | 22% | FLA -1.5 33% | 6.1 / 6.5 (over 43%) | Akira Schmid (confirmed) / Clay Stevenson (confirmed) | FLA -130 / WPG +110 | no edge | no edge | no edge |
| 9:00 PM | MIN @ UTA | MIN 3, UTA 4 | UTA 52% | MIN +110 / UTA -110 | 3.1 – 3.2 | 1–5 / 1–6 | 21% | UTA -1.5 32% | 6.4 / 6.5 (over 48%) | Jesper Wallstedt (confirmed) / Karel Vejmelka (confirmed) | MIN +102 / UTA -122 | no edge | no edge | no edge |
| 10:00 PM | OTT @ VGK | OTT 3, VGK 4 | VGK 57% | OTT +135 / VGK -135 | 2.9 – 3.4 | 1–5 / 1–6 | 22% | VGK -1.5 35% | 6.3 / 6.5 (over 46%) | Jonas Johansson (confirmed) / Adin Hill (confirmed) | OTT +136 / VGK -162 | no edge | OTT (+136): EV +4.0%, 44%, stake 0.7u | Under 6.5 (-105): EV +3.9%, 53%, stake 1.0u |
| 10:00 PM | VAN @ ANA | VAN 3, ANA 4 | ANA 65% | VAN +190 / ANA -190 | 3.0 – 4.0 | 1–5 / 2–7 | 19% | ANA -1.5 45% | 7.1 / 6.5 (over 59%) | Kevin Lankinen (expected) / Lukas Dostal (confirmed) | VAN +180 / ANA -218 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 10:30 PM | BUF @ SJS | BUF 4, SJS 3 | BUF 59% | BUF -145 / SJS +145 | 3.7 – 3.0 | 1–6 / 1–5 | 20% | BUF -1.5 39% | 6.7 / 6.5 (over 53%) | Colten Ellis (confirmed) / Yaroslav Askarov (confirmed) | BUF -148 / SJS +124 | no edge | no edge | no edge |

## Wednesday, October 28

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected goals | 80% range | Overtime | Puck line | Total: model / line | Goalies | Posted moneyline | Puck line edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 7:30 PM | PHI @ WSH | PHI 2, WSH 3 | WSH 67% | PHI +200 / WSH -200 | 2.6 – 3.6 | 1–5 / 1–6 | 20% | WSH -1.5 45% | 6.2 / 6.5 (over 44%) | Joseph Woll (expected) / Logan Thompson (expected) | PHI +190 / WSH -230 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 8:30 PM | CGY @ EDM | CGY 3, EDM 4 | EDM 60% | CGY +150 / EDM -150 | 3.0 – 3.6 | 1–5 / 1–6 | 21% | EDM -1.5 39% | 6.6 / 6.5 (over 51%) | Devin Cooley (expected) / Tristan Jarry (expected) | CGY +180 / EDM -218 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 9:00 PM | NJD @ COL | NJD 3, COL 4 | COL 60% | NJD +150 / COL -150 | 2.8 – 3.4 | 1–5 / 1–6 | 22% | COL -1.5 38% | 6.2 / 6.5 (over 45%) | Jake Allen (expected) / Mackenzie Blackwood (expected) | NJD +154 / COL -185 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 10:00 PM | TOR @ SEA | TOR 4, SEA 3 | TOR 51% | TOR -105 / SEA +105 | 3.4 – 3.3 | 1–6 / 1–6 | 22% | TOR -1.5 32% | 6.7 / 6.5 (over 53%) | Sergei Bobrovsky (expected) / Philipp Grubauer (expected) | TOR -115 / SEA -105 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |

## Thursday, October 29

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected goals | 80% range | Overtime | Puck line | Total: model / line | Goalies | Posted moneyline | Puck line edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 7:00 PM | WPG @ TBL | WPG 2, TBL 3 | TBL 63% | WPG +170 / TBL -170 | 2.6 – 3.5 | 1–5 / 1–6 | 22% | TBL -1.5 40% | 6.1 | Stuart Skinner (expected) / Andrei Vasilevskiy (expected) | – | no line yet (model fair TBL -1.5 +145 / WPG +1.5 -145) | no line yet | no line yet |
| 7:00 PM | UTA @ PIT | UTA 4, PIT 3 | UTA 56% | UTA -125 / PIT +125 | 3.4 – 3.1 | 1–6 / 1–5 | 21% | UTA -1.5 35% | 6.5 | Karel Vejmelka (expected) / Arturs Silovs (expected) | – | no line yet (model fair PIT +1.5 -185 / UTA -1.5 +185) | no line yet | no line yet |
| 7:00 PM | CBJ @ CAR | CBJ 3, CAR 4 | CAR 65% | CBJ +185 / CAR -185 | 2.7 – 3.6 | 1–5 / 1–6 | 21% | CAR -1.5 43% | 6.3 | Jet Greaves (expected) / Pyotr Kochetkov (expected) | – | no line yet (model fair CAR -1.5 +130 / CBJ +1.5 -130) | no line yet | no line yet |
| 7:30 PM | CHI @ DET | CHI 2, DET 3 | DET 65% | CHI +185 / DET -185 | 2.6 – 3.6 | 1–5 / 1–6 | 21% | DET -1.5 42% | 6.2 | Spencer Knight (expected) / John Gibson (expected) | – | no line yet (model fair DET -1.5 +135 / CHI +1.5 -135) | no line yet | no line yet |
| 8:00 PM | BOS @ STL | BOS 2, STL 3 | STL 51% | BOS +100 / STL -100 | 3.1 – 3.1 | 1–5 / 1–5 | 22% | STL -1.5 30% | 6.1 | Jeremy Swayman (expected) / Joel Hofer (expected) | – | no line yet (model fair STL -1.5 +235 / BOS +1.5 -235) | no line yet | no line yet |
| 8:00 PM | WSH @ NSH | WSH 3, NSH 4 | NSH 54% | WSH +115 / NSH -115 | 3.1 – 3.4 | 1–6 / 1–6 | 22% | NSH -1.5 34% | 6.5 | Charlie Lindgren (expected) / Juuse Saros (expected) | – | no line yet (model fair NSH -1.5 +200 / WSH +1.5 -200) | no line yet | no line yet |
| 8:00 PM | MTL @ DAL | MTL 2, DAL 3 | DAL 59% | MTL +145 / DAL -145 | 2.7 – 3.2 | 1–5 / 1–6 | 22% | DAL -1.5 36% | 5.9 | Jacob Fowler (expected) / Jake Oettinger (expected) | – | no line yet (model fair DAL -1.5 +175 / MTL +1.5 -175) | no line yet | no line yet |
| 8:00 PM | NYI @ MIN | NYI 2, MIN 3 | MIN 61% | NYI +160 / MIN -160 | 2.7 – 3.4 | 1–5 / 1–6 | 22% | MIN -1.5 39% | 6.1 | Ilya Sorokin (expected) / Jesper Wallstedt (expected) | – | no line yet (model fair MIN -1.5 +155 / NYI +1.5 -155) | no line yet | no line yet |
| 10:00 PM | BUF @ ANA | BUF 4, ANA 3 | BUF 56% | BUF -125 / ANA +125 | 3.6 – 3.2 | 1–6 / 1–6 | 21% | BUF -1.5 36% | 6.7 | Ukko-Pekka Luukkonen (expected) / Lukas Dostal (expected) | – | no line yet (model fair ANA +1.5 -180 / BUF -1.5 +180) | no line yet | no line yet |
| 10:00 PM | OTT @ LAK | OTT 2, LAK 3 | LAK 51% | OTT +105 / LAK -105 | 2.9 – 3.1 | 1–5 / 1–5 | 24% | LAK -1.5 30% | 6.0 | Samuel Ersson (expected) / Darcy Kuemper (expected) | – | no line yet (model fair LAK -1.5 +230 / OTT +1.5 -230) | no line yet | no line yet |
| 10:00 PM | VAN @ SJS | VAN 3, SJS 4 | SJS 57% | VAN +130 / SJS -130 | 3.3 – 3.8 | 1–6 / 1–6 | 20% | SJS -1.5 37% | 7.1 | Leevi Meriläinen (expected) / Yaroslav Askarov (expected) | – | no line yet (model fair SJS -1.5 +170 / VAN +1.5 -170) | no line yet | no line yet |

\* price not posted; assumed -110.

## How the 2026-27 predictions have done

| Predictor | Games | Log loss | Brier | Winners | Goals MAE | Total MAE | 80% range hit |
|---|---|---|---|---|---|---|---|
| Final prediction | 187 | 0.6540 | 0.2310 | 61.5% | 1.39 | 1.76 | 89.3% |
| Model only (before blending) | 187 | 0.6549 | 0.2315 | 60.4% | – | – | – |
| Elo | 187 | 0.6675 | 0.2373 | 63.1% | – | – | – |
| Final prediction, games with a line | 53 | 0.6755 | 0.2412 | 56.6% | 1.38 | 1.78 | 88.7% |
| Model only, games with a line | 53 | 0.6787 | 0.2429 | 52.8% | – | – | – |
| Betting market (de-vigged moneyline) | 53 | 0.6812 | 0.2439 | 56.6% | – | 1.73 | – |

Log loss and Brier score the win chances (lower is better; a coin flip scores 0.693 and 0.250). Hockey is close to a coin flip, so differences in the third decimal matter, and only over hundreds of games. Goals MAE is the average miss on each team's goals.

Overtime: predicted in 21.6% of regular-season games, happened in 23.0%.

134 of these games were played before the predictor went live. They are backfilled walk-forward (each day predicted from earlier days only) with the actual starting goalies and no betting line. Every game since is graded on the prediction logged before puck drop.

### Betting edges

| Market | Edges | Record (W-L-P) | Staked | Units won | ROI | Expected ROI |
|---|---|---|---|---|---|---|
| Puck line | 1 | 0-1-0 | 1.3 | -1.29 | -100.0% | +11.8% |
| Moneyline | 2 | 2-0-0 | 2.6 | +2.77 | +104.8% | +6.2% |
| Total | 0 | 0-0-0 | 0.0 | +0.00 | – | – |

Moneyline moved toward the model's edge on the first line seen before puck drop: 6 of 9 games (67%).

Each edge at the stake and price logged with the last prediction before puck drop (edges logged before edges were priced from the final prediction are left out); pushes return the stake. Units are 1% of the bankroll; ROI is units won per unit staked, and expected ROI is what the edges' EVs promised. The moneyline moving toward the model's edge (closing line value) is the quickest sign that it knows something the market doesn't yet.

### Results, Monday, October 26

| Game | Predicted | Final | Win chance for winner | Inside 80% ranges | Goalies |
|---|---|---|---|---|---|
| LAK @ NYR | 2–3 | 6–3 | 46% | no | Darcy Kuemper / James Reimer |
| TOR @ CGY | 4–3 | 2–5 | 49% | yes | Sergei Bobrovsky / Devin Cooley |
| DET @ EDM | 3–4 | 4–3 (SO) | 42% | yes | Michal Postava / Tristan Jarry |

## Power ratings

Goals per game better than an average team, from the goal-rate model: offense and defense combine 5-on-5 expected goals (score and venue adjusted), special teams and actual goals, each weighted against a preseason prior. Defense is positive when it holds opponents below average. Goaltending is rated separately below.

| # | Team | Net | Offense | Defense | 5v5 xGF/60 | 5v5 xGA/60 | PP xGF/60 | PK xGA/60 | Elo |
|---|---|---|---|---|---|---|---|---|---|
| 1 | CAR | +0.66 | +0.42 | +0.25 | 3.43 | 2.44 | 8.12 | 6.82 | 1576 |
| 2 | UTA | +0.50 | +0.28 | +0.22 | 3.21 | 2.38 | 8.05 | 8.27 | 1516 |
| 3 | MIN | +0.37 | +0.16 | +0.21 | 3.10 | 2.47 | 9.17 | 8.13 | 1537 |
| 4 | TBL | +0.34 | +0.18 | +0.16 | 2.94 | 2.53 | 7.83 | 7.82 | 1538 |
| 5 | VGK | +0.32 | +0.07 | +0.24 | 2.73 | 2.41 | 8.71 | 7.27 | 1529 |
| 6 | NJD | +0.28 | +0.04 | +0.24 | 2.93 | 2.38 | 8.86 | 7.57 | 1500 |
| 7 | PIT | +0.27 | +0.23 | +0.05 | 3.10 | 2.64 | 7.94 | 7.66 | 1500 |
| 8 | DAL | +0.26 | -0.03 | +0.29 | 2.62 | 2.38 | 9.13 | 7.21 | 1538 |
| 9 | FLA | +0.23 | -0.00 | +0.24 | 2.67 | 2.42 | 8.92 | 7.42 | 1496 |
| 10 | COL | +0.23 | +0.24 | -0.01 | 2.92 | 2.77 | 7.54 | 7.75 | 1544 |
| 11 | OTT | +0.08 | -0.05 | +0.12 | 2.64 | 2.56 | 7.83 | 7.89 | 1522 |
| 12 | BOS | +0.07 | +0.09 | -0.03 | 2.85 | 2.80 | 7.81 | 8.08 | 1536 |
| 13 | BUF | +0.06 | +0.05 | +0.01 | 2.71 | 2.69 | 7.56 | 8.32 | 1511 |
| 14 | STL | +0.06 | -0.04 | +0.10 | 2.56 | 2.60 | 7.06 | 7.45 | 1504 |
| 15 | EDM | +0.05 | +0.11 | -0.05 | 2.60 | 2.76 | 9.83 | 8.13 | 1518 |
| 16 | NYR | +0.04 | +0.03 | +0.01 | 2.74 | 2.72 | 8.53 | 7.70 | 1493 |
| 17 | LAK | +0.01 | -0.14 | +0.15 | 2.52 | 2.54 | 7.71 | 7.94 | 1473 |
| 18 | WSH | +0.01 | +0.09 | -0.08 | 2.88 | 2.83 | 7.73 | 8.11 | 1516 |
| 19 | DET | -0.01 | -0.11 | +0.10 | 2.63 | 2.57 | 8.41 | 8.58 | 1481 |
| 20 | MTL | -0.02 | +0.04 | -0.06 | 2.86 | 2.80 | 7.16 | 8.38 | 1521 |
| 21 | CBJ | -0.04 | -0.06 | +0.02 | 2.68 | 2.67 | 7.58 | 8.47 | 1490 |
| 22 | NYI | -0.09 | -0.06 | -0.03 | 2.72 | 2.79 | 7.51 | 8.71 | 1490 |
| 23 | WPG | -0.11 | -0.10 | -0.02 | 2.61 | 2.78 | 7.99 | 7.99 | 1479 |
| 24 | TOR | -0.13 | +0.02 | -0.15 | 2.58 | 2.90 | 8.65 | 8.17 | 1485 |
| 25 | NSH | -0.18 | -0.10 | -0.08 | 2.57 | 2.82 | 7.87 | 7.50 | 1484 |
| 26 | CGY | -0.21 | -0.08 | -0.13 | 2.67 | 2.87 | 7.28 | 8.18 | 1467 |
| 27 | SEA | -0.32 | -0.09 | -0.23 | 2.49 | 2.99 | 7.29 | 8.43 | 1482 |
| 28 | ANA | -0.34 | -0.01 | -0.33 | 2.83 | 3.07 | 7.74 | 8.24 | 1480 |
| 29 | PHI | -0.35 | -0.30 | -0.06 | 2.27 | 2.78 | 7.84 | 7.59 | 1478 |
| 30 | SJS | -0.65 | -0.19 | -0.46 | 2.41 | 3.21 | 7.31 | 8.75 | 1470 |
| 31 | CHI | -0.68 | -0.30 | -0.38 | 2.28 | 3.12 | 6.99 | 8.21 | 1433 |
| 32 | VAN | -0.81 | -0.22 | -0.59 | 2.29 | 3.35 | 7.48 | 8.68 | 1414 |

## Goalies

Each team's likeliest next starter. GSAx is goals saved above expected (from this predictor's own shot model), shrunk hard toward a slightly below-average prior, since goaltending repeats poorly from season to season.

| Team | Likely next starter | Share of recent starts | GSAx per 100 shots | Goals per game vs average |
|---|---|---|---|---|
| WSH | Logan Thompson | 68% | +0.45 | +0.19 |
| NYI | Ilya Sorokin | 71% | +0.42 | +0.18 |
| BOS | Jeremy Swayman | 73% | +0.32 | +0.13 |
| CGY | Devin Cooley | 62% | +0.22 | +0.09 |
| TBL | Andrei Vasilevskiy | 69% | +0.18 | +0.08 |
| MTL | Jacob Fowler | 60% | +0.17 | +0.07 |
| MIN | Jesper Wallstedt | 82% | +0.15 | +0.06 |
| DAL | Jake Oettinger | 84% | +0.15 | +0.06 |
| OTT | Linus Ullmark | 63% | +0.14 | +0.06 |
| COL | Mackenzie Blackwood | 62% | +0.13 | +0.05 |
| CBJ | Jet Greaves | 51% | +0.11 | +0.05 |
| CHI | Spencer Knight | 86% | +0.05 | +0.02 |
| WPG | Stuart Skinner | 75% | +0.03 | +0.01 |
| STL | Joel Hofer | 75% | +0.01 | +0.00 |
| CAR | Pyotr Kochetkov | 57% | -0.05 | -0.02 |
| PHI | Joseph Woll | 54% | -0.06 | -0.02 |
| NJD | Jake Allen | 64% | -0.06 | -0.02 |
| NYR | Dylan Garand | 63% | -0.06 | -0.03 |
| EDM | Devon Levi | 55% | -0.07 | -0.03 |
| SEA | Philipp Grubauer | 52% | -0.08 | -0.03 |
| TOR | Sergei Bobrovsky | 65% | -0.12 | -0.05 |
| LAK | Anton Forsberg | 54% | -0.12 | -0.05 |
| DET | John Gibson | 63% | -0.13 | -0.05 |
| ANA | Lukas Dostal | 70% | -0.15 | -0.06 |
| UTA | Karel Vejmelka | 77% | -0.16 | -0.07 |
| BUF | Ukko-Pekka Luukkonen | 76% | -0.17 | -0.07 |
| VGK | Carter Hart | 61% | -0.18 | -0.08 |
| VAN | Leevi Meriläinen | 51% | -0.21 | -0.09 |
| NSH | Juuse Saros | 67% | -0.23 | -0.09 |
| FLA | Akira Schmid | 46% | -0.23 | -0.10 |
| SJS | Yaroslav Askarov | 53% | -0.25 | -0.10 |
| PIT | Arturs Silovs | 69% | -0.29 | -0.12 |

## Current model fit

- Fitted on 5779 games from 2022-23 to 2026-27.
- Home ice: +3.2% goals for the home team relative to the visitor.
- Second night of a back-to-back: -5.6% goals scored, +3.2% goals allowed.
- Starting goalie: each goal per game he saves above average lowers the opponent's rate by 23%.
- Blend: 38% on the betting line wherever there is one (fitted on 53 logged games, shrunk toward the backtest value).
- Simulator: 22.3% of recent regular-season games reached overtime; trailing teams usually have the goalie pulled with 2 minutes left when down one and 3 when down two; empty-net goals come at 0.41 a minute with the net empty; three-on-three overtime produces 1.03 goals per five minutes.
