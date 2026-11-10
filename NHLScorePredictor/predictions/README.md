# NHL score predictions

Updated Tue Nov 10, 2026 02:48 AM ET. Refreshed automatically several times a day during the season; each game's prediction is locked at puck drop and graded once the final score is in.

Each game is simulated 10,000 times minute by minute, with pulled goalies, empty-net goals, overtime and shootouts. The predicted score is the most common final score in which the likelier winner wins; as in the official result, a shootout winner gets one extra goal. Hockey is low-scoring and luck-heavy, so read the win chance and the ranges (80% of simulated outcomes for each team) before the single score.

Goalies marked with a percentage are projected from recent starts (the share is the chance he starts); "probable" or "confirmed" ones come from ESPN and replace the projection when available.

The fair moneyline is the American odds that match the win chance exactly, with no bookmaker margin: -150 means risk $150 to win $100, +150 means risk $100 to win $150. A sportsbook's price is a little worse on both sides because of its cut, so a book only offers value on a team when its price beats the fair line. The puck line is the favorite's chance to win by two or more.

The edge columns price each side of the puck line, moneyline and total with the final prediction: the model's goal rates blended with the market's, simulated against the posted lines, overtime and shootout included (the shootout winner gets one goal), and anchored to the market's own chances so only what the blend moves off the market counts. Each cell shows the side with the best expected value (EV) per $1 bet at the posted price. A side is an edge only if its EV is at least 3%: a pick shows its price, EV, its chance of winning the bet and its stake, a 25% share of the Kelly stake in units of 1% of the bankroll, with at most 3 units on one game; "no edge" means neither side clears the bar. A projected starting goalie is wrong about a third of the time and the market prices the real one, so edges wait until both starters are confirmed. A total with no posted price is assumed to be -110 (marked \*); the puck line and moneyline are never assumed, so without a price the cell shows the model's fair odds instead. Treat the edges as an experiment, not betting advice; see the backtest for how they have done on past seasons. Their record is tracked live below.

## Tuesday, November 10

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected goals | 80% range | Overtime | Puck line | Total: model / line | Goalies | Posted moneyline | Puck line edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 7:00 PM | COL @ TOR | COL 4, TOR 3 | COL 60% | COL -150 / TOR +150 | 3.6 – 3.0 | 1–6 / 1–5 | 21% | COL -1.5 39% | 6.6 / 6.5 (over 51%) | Mackenzie Blackwood (expected) / Sergei Bobrovsky (expected) | COL -155 / TOR +130 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 7:00 PM | MIN @ MTL | MIN 3, MTL 2 | MIN 53% | MIN -115 / MTL +115 | 3.2 – 3.0 | 1–6 / 1–5 | 22% | MIN -1.5 33% | 6.2 / 6.5 (over 45%) | Jesper Wallstedt (expected) / Jacob Fowler (expected) | MIN -125 / MTL +105 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 7:00 PM | WSH @ OTT | WSH 2, OTT 3 | OTT 53% | WSH +115 / OTT -115 | 3.0 – 3.2 | 1–5 / 1–6 | 22% | OTT -1.5 32% | 6.3 / 6.5 (over 46%) | Logan Thompson (expected) / Linus Ullmark (expected) | WSH +110 / OTT -130 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 7:00 PM | NJD @ WPG | NJD 3, WPG 2 | NJD 57% | NJD -135 / WPG +135 | 3.3 – 2.9 | 1–6 / 1–5 | 22% | NJD -1.5 35% | 6.2 / 6.5 (over 45%) | Jake Allen (expected) / Nico Daws (expected) | NJD -155 / WPG +130 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 7:30 PM | FLA @ CBJ | FLA 2, CBJ 3 | CBJ 50% | FLA +100 / CBJ -100 | 3.1 – 3.1 | 1–5 / 1–6 | 21% | CBJ -1.5 30% | 6.2 / 5.5 (over 55%) | Jacob Markstrom (expected) / Cam Talbot (expected) | FLA -115 / CBJ -105 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 8:00 PM | DET @ STL | DET 2, STL 3 | STL 58% | DET +140 / STL -140 | 2.8 – 3.3 | 1–5 / 1–6 | 22% | STL -1.5 36% | 6.1 / 5.5 (over 53%) | John Gibson (expected) / Joel Hofer (expected) | DET +124 / STL -148 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 10:00 PM | NSH @ LAK | NSH 2, LAK 3 | LAK 55% | NSH +120 / LAK -120 | 2.9 – 3.2 | 1–5 / 1–6 | 22% | LAK -1.5 33% | 6.2 / 6.5 (over 45%) | Juuse Saros (expected) / Darcy Kuemper (expected) | NSH +114 / LAK -135 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |

## Wednesday, November 11

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected goals | 80% range | Overtime | Puck line | Total: model / line | Goalies | Posted moneyline | Puck line edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 7:00 PM | TBL @ BUF | TBL 4, BUF 3 | TBL 55% | TBL -120 / BUF +120 | 3.3 – 3.0 | 1–6 / 1–5 | 22% | TBL -1.5 34% | 6.4 | Andrei Vasilevskiy (expected) / Ukko-Pekka Luukkonen (expected) | – | no line yet (model fair BUF +1.5 -200 / TBL -1.5 +200) | no line yet | no line yet |
| 7:30 PM | NYR @ CGY | NYR 4, CGY 3 | NYR 54% | NYR -120 / CGY +120 | 3.4 – 3.1 | 1–6 / 1–6 | 22% | NYR -1.5 34% | 6.5 | Dylan Garand (expected) / Dustin Wolf (expected) | – | no line yet (model fair CGY +1.5 -195 / NYR -1.5 +195) | no line yet | no line yet |
| 9:00 PM | PHI @ EDM | PHI 2, EDM 3 | EDM 60% | PHI +150 / EDM -150 | 2.7 – 3.4 | 1–5 / 1–6 | 22% | EDM -1.5 38% | 6.1 | Dan Vladar (expected) / Devon Levi (expected) | – | no line yet (model fair EDM -1.5 +165 / PHI +1.5 -165) | no line yet | no line yet |
| 9:30 PM | UTA @ VGK | UTA 2, VGK 3 | VGK 50% | UTA +100 / VGK -100 | 3.1 – 3.1 | 1–5 / 1–5 | 22% | VGK -1.5 29% | 6.2 | Karel Vejmelka (expected) / Carter Hart (expected) | – | no line yet (model fair VGK -1.5 +245 / UTA +1.5 -245) | no line yet | no line yet |
| 10:00 PM | NSH @ ANA | NSH 3, ANA 4 | ANA 53% | NSH +115 / ANA -115 | 3.2 – 3.4 | 1–6 / 1–6 | 22% | ANA -1.5 32% | 6.6 | Justus Annunen (expected) / Laurent Brossoit (expected) | – | no line yet (model fair ANA -1.5 +210 / NSH +1.5 -210) | no line yet | no line yet |
| 10:00 PM | PIT @ SJS | PIT 4, SJS 3 | PIT 65% | PIT -190 / SJS +190 | 3.9 – 2.9 | 1–6 / 1–5 | 20% | PIT -1.5 45% | 6.9 | Arturs Silovs (expected) / Yaroslav Askarov (expected) | – | no line yet (model fair SJS +1.5 -125 / PIT -1.5 +125) | no line yet | no line yet |

\* price not posted; assumed -110.

## Thursday, November 12

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected goals | 80% range | Overtime | Puck line | Total: model / line | Goalies | Posted moneyline | Puck line edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 12:00 PM | CAR @ SEA | CAR 4, SEA 3 | CAR 74% | CAR -280 / SEA +280 | 4.2 – 2.6 | 2–7 / 1–5 | 18% | CAR -1.5 54% | 6.7 | Pyotr Kochetkov (expected) / Philipp Grubauer (expected) | – | no line yet (model fair SEA +1.5 +120 / CAR -1.5 -120) | no line yet | no line yet |
| 7:00 PM | MTL @ BOS | MTL 3, BOS 4 | BOS 55% | MTL +120 / BOS -120 | 3.0 – 3.3 | 1–5 / 1–6 | 22% | BOS -1.5 34% | 6.3 | Jacob Fowler (expected) / Jeremy Swayman (expected) | – | no line yet (model fair BOS -1.5 +190 / MTL +1.5 -190) | no line yet | no line yet |
| 7:00 PM | MIN @ TOR | MIN 3, TOR 2 | MIN 60% | MIN -150 / TOR +150 | 3.4 – 2.8 | 1–6 / 1–5 | 22% | MIN -1.5 38% | 6.1 | Jesper Wallstedt (expected) / Sergei Bobrovsky (expected) | – | no line yet (model fair TOR +1.5 -160 / MIN -1.5 +160) | no line yet | no line yet |
| 7:00 PM | COL @ OTT | COL 4, OTT 3 | COL 51% | COL -105 / OTT +105 | 3.2 – 3.1 | 1–6 / 1–5 | 23% | COL -1.5 31% | 6.3 | Mackenzie Blackwood (expected) / Linus Ullmark (expected) | – | no line yet (model fair OTT +1.5 -225 / COL -1.5 +225) | no line yet | no line yet |
| 7:00 PM | WSH @ NJD | WSH 2, NJD 3 | NJD 54% | WSH +115 / NJD -115 | 2.9 – 3.2 | 1–5 / 1–6 | 23% | NJD -1.5 33% | 6.1 | Logan Thompson (expected) / Connor Hellebuyck (expected) | – | no line yet (model fair NJD -1.5 +205 / WSH +1.5 -205) | no line yet | no line yet |
| 7:00 PM | TBL @ CBJ | TBL 3, CBJ 2 | TBL 53% | TBL -115 / CBJ +115 | 3.2 – 3.0 | 1–6 / 1–5 | 23% | TBL -1.5 32% | 6.2 | Dennis Hildeby (expected) / Jet Greaves (expected) | – | no line yet (model fair CBJ +1.5 -215 / TBL -1.5 +215) | no line yet | no line yet |
| 7:30 PM | DET @ FLA | DET 2, FLA 3 | FLA 54% | DET +120 / FLA -120 | 2.9 – 3.2 | 1–5 / 1–6 | 22% | FLA -1.5 33% | 6.1 | John Gibson (expected) / Jacob Markstrom (expected) | – | no line yet (model fair FLA -1.5 +205 / DET +1.5 -205) | no line yet | no line yet |
| 8:00 PM | BUF @ CHI | BUF 4, CHI 3 | BUF 61% | BUF -160 / CHI +160 | 3.6 – 2.8 | 1–6 / 1–5 | 21% | BUF -1.5 39% | 6.4 | Colten Ellis (expected) / Spencer Knight (expected) | – | no line yet (model fair CHI +1.5 -155 / BUF -1.5 +155) | no line yet | no line yet |
| 8:00 PM | WPG @ DAL | WPG 2, DAL 3 | DAL 61% | WPG +155 / DAL -155 | 2.6 – 3.2 | 1–5 / 1–6 | 22% | DAL -1.5 38% | 5.9 | Stuart Skinner (expected) / Jake Oettinger (expected) | – | no line yet (model fair DAL -1.5 +165 / WPG +1.5 -165) | no line yet | no line yet |
| 9:00 PM | STL @ UTA | STL 2, UTA 3 | UTA 53% | STL +110 / UTA -110 | 3.0 – 3.2 | 1–5 / 1–6 | 23% | UTA -1.5 32% | 6.2 | Joel Hofer (expected) / Sebastian Cossa (expected) | – | no line yet (model fair UTA -1.5 +215 / STL +1.5 -215) | no line yet | no line yet |
| 10:00 PM | NYI @ LAK | NYI 2, LAK 3 | LAK 51% | NYI +105 / LAK -105 | 3.0 – 3.1 | 1–5 / 1–5 | 22% | LAK -1.5 30% | 6.1 | Ilya Sorokin (expected) / Darcy Kuemper (expected) | – | no line yet (model fair LAK -1.5 +235 / NYI +1.5 -235) | no line yet | no line yet |

\* price not posted; assumed -110.

## How the 2026-27 predictions have done

| Predictor | Games | Log loss | Brier | Winners | Goals MAE | Total MAE | 80% range hit |
|---|---|---|---|---|---|---|---|
| Final prediction | 282 | 0.6443 | 0.2265 | 62.4% | 1.36 | 1.78 | 90.1% |
| Model only (before blending) | 282 | 0.6468 | 0.2278 | 60.6% | – | – | – |
| Elo | 282 | 0.6606 | 0.2341 | 61.7% | – | – | – |
| Final prediction, games with a line | 148 | 0.6432 | 0.2261 | 61.5% | 1.34 | 1.80 | 90.5% |
| Model only, games with a line | 148 | 0.6480 | 0.2286 | 58.1% | – | – | – |
| Betting market (de-vigged moneyline) | 148 | 0.6432 | 0.2261 | 61.5% | – | 1.79 | – |

Log loss and Brier score the win chances (lower is better; a coin flip scores 0.693 and 0.250). Hockey is close to a coin flip, so differences in the third decimal matter, and only over hundreds of games. Goals MAE is the average miss on each team's goals.

Overtime: predicted in 21.5% of regular-season games, happened in 22.0%.

134 of these games were played before the predictor went live. They are backfilled walk-forward (each day predicted from earlier days only) with the actual starting goalies and no betting line. Every game since is graded on the prediction logged before puck drop.

### Betting edges

| Market | Edges | Record (W-L-P) | Staked | Units won | ROI | Expected ROI |
|---|---|---|---|---|---|---|
| Puck line | 1 | 0-1-0 | 1.3 | -1.29 | -100.0% | +11.8% |
| Moneyline | 8 | 4-4-0 | 8.7 | +1.83 | +21.2% | +6.4% |
| Total | 1 | 0-1-0 | 0.9 | -0.89 | -100.0% | +3.0% |

Moneyline moved toward the model's edge on the first line seen before puck drop: 26 of 32 games (81%).

Each edge at the stake and price logged with the last prediction before puck drop (edges logged before edges were priced from the final prediction are left out); pushes return the stake. Units are 1% of the bankroll; ROI is units won per unit staked, and expected ROI is what the edges' EVs promised. The moneyline moving toward the model's edge (closing line value) is the quickest sign that it knows something the market doesn't yet.

### Results, Sunday, November 8

| Game | Predicted | Final | Win chance for winner | Inside 80% ranges | Goalies |
|---|---|---|---|---|---|
| FLA @ BOS | 3–4 | 1–4 | 56% | yes | Jacob Markstrom / Jeremy Swayman |
| VGK @ BUF | 4–3 | 4–1 | 50% | yes | Carter Hart / Colten Ellis |
| TBL @ WPG | 4–3 | 3–4 | 43% | yes | Andrei Vasilevskiy / Stuart Skinner |
| NJD @ TOR | 3–2 | 4–0 | 57% | no | Connor Hellebuyck / Anthony Stolarz |
| PHI @ CGY | 2–3 | 3–4 (OT) | 50% | yes | Dan Vladar / Devin Cooley |
| PIT @ ANA | 3–4 | 2–5 | 51% | yes | Arturs Silovs / Laurent Brossoit |

## Power ratings

Goals per game better than an average team, from the goal-rate model: offense and defense combine 5-on-5 expected goals (score and venue adjusted), special teams and actual goals, each weighted against a preseason prior. Defense is positive when it holds opponents below average. Goaltending is rated separately below.

| # | Team | Net | Offense | Defense | 5v5 xGF/60 | 5v5 xGA/60 | PP xGF/60 | PK xGA/60 | Elo |
|---|---|---|---|---|---|---|---|---|---|
| 1 | CAR | +0.78 | +0.49 | +0.29 | 3.48 | 2.38 | 8.65 | 7.24 | 1585 |
| 2 | UTA | +0.46 | +0.24 | +0.21 | 3.17 | 2.39 | 8.21 | 8.77 | 1506 |
| 3 | TBL | +0.41 | +0.19 | +0.22 | 2.93 | 2.44 | 8.11 | 8.00 | 1544 |
| 4 | VGK | +0.29 | +0.03 | +0.25 | 2.68 | 2.41 | 9.19 | 7.26 | 1536 |
| 5 | MIN | +0.27 | +0.09 | +0.18 | 2.88 | 2.52 | 9.29 | 8.15 | 1549 |
| 6 | PIT | +0.24 | +0.17 | +0.07 | 3.00 | 2.58 | 7.82 | 8.01 | 1487 |
| 7 | COL | +0.23 | +0.27 | -0.03 | 2.98 | 2.80 | 7.81 | 8.01 | 1549 |
| 8 | DAL | +0.23 | -0.08 | +0.30 | 2.54 | 2.34 | 9.62 | 7.41 | 1529 |
| 9 | NJD | +0.22 | +0.04 | +0.18 | 2.84 | 2.47 | 9.23 | 7.93 | 1525 |
| 10 | BUF | +0.13 | +0.13 | -0.00 | 2.89 | 2.70 | 8.05 | 8.50 | 1516 |
| 11 | FLA | +0.13 | -0.03 | +0.15 | 2.61 | 2.53 | 9.73 | 7.64 | 1498 |
| 12 | STL | +0.10 | +0.01 | +0.09 | 2.70 | 2.60 | 7.03 | 7.77 | 1497 |
| 13 | OTT | +0.09 | -0.02 | +0.11 | 2.71 | 2.57 | 8.15 | 8.32 | 1521 |
| 14 | EDM | +0.09 | +0.08 | +0.02 | 2.57 | 2.68 | 9.70 | 8.16 | 1531 |
| 15 | WSH | +0.08 | +0.14 | -0.06 | 2.96 | 2.78 | 7.93 | 8.15 | 1516 |
| 16 | LAK | +0.06 | -0.10 | +0.15 | 2.59 | 2.53 | 8.36 | 8.26 | 1471 |
| 17 | BOS | +0.05 | +0.07 | -0.02 | 2.80 | 2.79 | 7.64 | 8.33 | 1543 |
| 18 | NYR | +0.02 | +0.03 | -0.01 | 2.76 | 2.75 | 8.81 | 7.91 | 1497 |
| 19 | MTL | -0.04 | +0.07 | -0.11 | 2.84 | 2.87 | 7.62 | 8.54 | 1537 |
| 20 | DET | -0.06 | -0.10 | +0.04 | 2.66 | 2.64 | 8.42 | 8.81 | 1477 |
| 21 | CBJ | -0.08 | -0.03 | -0.06 | 2.74 | 2.77 | 7.75 | 8.76 | 1494 |
| 22 | WPG | -0.11 | -0.11 | +0.01 | 2.57 | 2.72 | 8.39 | 8.92 | 1472 |
| 23 | TOR | -0.11 | -0.05 | -0.06 | 2.50 | 2.77 | 8.85 | 8.54 | 1473 |
| 24 | NSH | -0.11 | -0.08 | -0.04 | 2.61 | 2.76 | 8.37 | 7.79 | 1496 |
| 25 | NYI | -0.15 | -0.01 | -0.13 | 2.83 | 2.90 | 7.62 | 8.63 | 1483 |
| 26 | CGY | -0.24 | -0.12 | -0.11 | 2.57 | 2.84 | 7.26 | 8.11 | 1464 |
| 27 | PHI | -0.24 | -0.25 | +0.00 | 2.37 | 2.70 | 7.80 | 7.43 | 1468 |
| 28 | SEA | -0.31 | -0.12 | -0.19 | 2.45 | 2.94 | 7.29 | 8.69 | 1478 |
| 29 | ANA | -0.36 | -0.00 | -0.36 | 2.69 | 3.10 | 8.14 | 8.50 | 1495 |
| 30 | CHI | -0.68 | -0.30 | -0.39 | 2.30 | 3.11 | 7.26 | 8.53 | 1416 |
| 31 | VAN | -0.70 | -0.25 | -0.45 | 2.24 | 3.18 | 7.75 | 8.77 | 1402 |
| 32 | SJS | -0.76 | -0.25 | -0.51 | 2.35 | 3.26 | 7.36 | 9.37 | 1447 |

## Goalies

Each team's likeliest next starter. GSAx is goals saved above expected (from this predictor's own shot model), shrunk hard toward a slightly below-average prior, since goaltending repeats poorly from season to season.

| Team | Likely next starter | Share of recent starts | GSAx per 100 shots | Goals per game vs average |
|---|---|---|---|---|
| NYI | Ilya Sorokin | 67% | +0.38 | +0.16 |
| WSH | Logan Thompson | 75% | +0.37 | +0.15 |
| BOS | Jeremy Swayman | 69% | +0.37 | +0.15 |
| MTL | Jacob Fowler | 64% | +0.33 | +0.14 |
| MIN | Jesper Wallstedt | 81% | +0.25 | +0.11 |
| COL | Mackenzie Blackwood | 73% | +0.21 | +0.09 |
| TBL | Andrei Vasilevskiy | 76% | +0.14 | +0.06 |
| CBJ | Jet Greaves | 50% | +0.11 | +0.05 |
| DAL | Jake Oettinger | 76% | +0.09 | +0.04 |
| STL | Joel Hofer | 71% | +0.05 | +0.02 |
| CAR | Pyotr Kochetkov | 69% | +0.03 | +0.01 |
| CHI | Spencer Knight | 77% | +0.03 | +0.01 |
| NYR | Dylan Garand | 66% | +0.00 | +0.00 |
| WPG | Stuart Skinner | 75% | -0.06 | -0.02 |
| NJD | Jake Allen | 44% | -0.07 | -0.03 |
| PHI | Dan Vladar | 56% | -0.07 | -0.03 |
| BUF | Ukko-Pekka Luukkonen | 54% | -0.11 | -0.04 |
| NSH | Juuse Saros | 66% | -0.16 | -0.07 |
| TOR | Sergei Bobrovsky | 62% | -0.16 | -0.07 |
| DET | John Gibson | 55% | -0.17 | -0.07 |
| SEA | Joey Daccord | 51% | -0.19 | -0.08 |
| ANA | Lukas Dostal | 46% | -0.20 | -0.08 |
| SJS | Yaroslav Askarov | 62% | -0.21 | -0.09 |
| UTA | Karel Vejmelka | 63% | -0.22 | -0.09 |
| LAK | Darcy Kuemper | 67% | -0.23 | -0.10 |
| CGY | Dustin Wolf | 49% | -0.26 | -0.11 |
| VGK | Adin Hill | 52% | -0.27 | -0.11 |
| FLA | Jacob Markstrom | 48% | -0.30 | -0.13 |
| EDM | Tristan Jarry | 46% | -0.32 | -0.13 |
| VAN | Leevi Meriläinen | 66% | -0.38 | -0.16 |
| PIT | Arturs Silovs | 68% | -0.40 | -0.17 |
| OTT | Samuel Ersson | 40% | -0.49 | -0.20 |

## Current model fit

- Fitted on 5874 games from 2022-23 to 2026-27.
- Home ice: +3.0% goals for the home team relative to the visitor.
- Second night of a back-to-back: -6.0% goals scored, +3.5% goals allowed.
- Starting goalie: each goal per game he saves above average lowers the opponent's rate by 22%.
- Blend: 47% on the betting line wherever there is one (fitted on 148 logged games, shrunk toward the backtest value).
- Simulator: 22.3% of recent regular-season games reached overtime; trailing teams usually have the goalie pulled with 2 minutes left when down one and 3 when down two; empty-net goals come at 0.40 a minute with the net empty; three-on-three overtime produces 1.04 goals per five minutes.
