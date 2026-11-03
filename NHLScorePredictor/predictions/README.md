# NHL score predictions

Updated Tue Nov 03, 2026 03:14 PM ET. Refreshed automatically several times a day during the season; each game's prediction is locked at puck drop and graded once the final score is in.

Each game is simulated 10,000 times minute by minute, with pulled goalies, empty-net goals, overtime and shootouts. The predicted score is the most common final score in which the likelier winner wins; as in the official result, a shootout winner gets one extra goal. Hockey is low-scoring and luck-heavy, so read the win chance and the ranges (80% of simulated outcomes for each team) before the single score.

Goalies marked with a percentage are projected from recent starts (the share is the chance he starts); "probable" or "confirmed" ones come from ESPN and replace the projection when available.

The fair moneyline is the American odds that match the win chance exactly, with no bookmaker margin: -150 means risk $150 to win $100, +150 means risk $100 to win $150. A sportsbook's price is a little worse on both sides because of its cut, so a book only offers value on a team when its price beats the fair line. The puck line is the favorite's chance to win by two or more.

The edge columns price each side of the puck line, moneyline and total with the final prediction: the model's goal rates blended with the market's, simulated against the posted lines, overtime and shootout included (the shootout winner gets one goal), and anchored to the market's own chances so only what the blend moves off the market counts. Each cell shows the side with the best expected value (EV) per $1 bet at the posted price. A side is an edge only if its EV is at least 3%: a pick shows its price, EV, its chance of winning the bet and its stake, a 25% share of the Kelly stake in units of 1% of the bankroll, with at most 3 units on one game; "no edge" means neither side clears the bar. A projected starting goalie is wrong about a third of the time and the market prices the real one, so edges wait until both starters are confirmed. A total with no posted price is assumed to be -110 (marked \*); the puck line and moneyline are never assumed, so without a price the cell shows the model's fair odds instead. Treat the edges as an experiment, not betting advice; see the backtest for how they have done on past seasons. Their record is tracked live below.

## Tuesday, November 3

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected goals | 80% range | Overtime | Puck line | Total: model / line | Goalies | Posted moneyline | Puck line edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 7:00 PM | UTA @ TOR | UTA 4, TOR 3 | UTA 58% | UTA -140 / TOR +140 | 3.6 – 3.1 | 1–6 / 1–5 | 21% | UTA -1.5 37% | 6.7 / 6.5 (over 52%) | Sebastian Cossa (confirmed) / Sergei Bobrovsky (confirmed) | UTA -142 / TOR +120 | no edge | no edge | Under 6.5 (+114): EV +3.0%, 48%, stake 0.7u |
| 7:00 PM | WPG @ MTL | WPG 2, MTL 3 | MTL 60% | WPG +150 / MTL -150 | 2.7 – 3.4 | 1–5 / 1–6 | 22% | MTL -1.5 39% | 6.1 / 5.5 (over 55%) | Stuart Skinner (expected) / Jacob Fowler (confirmed) | WPG +145 / MTL -175 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 7:00 PM | DET @ TBL | DET 3, TBL 4 | TBL 68% | DET +215 / TBL -215 | 2.5 – 3.8 | 1–5 / 1–6 | 20% | TBL -1.5 47% | 6.3 / 6.5 (over 47%) | John Gibson (expected) / Andrei Vasilevskiy (expected) | DET +225 / TBL -278 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 7:00 PM | STL @ NYR | STL 2, NYR 3 | NYR 50% | STL +100 / NYR -100 | 3.1 – 3.1 | 1–5 / 1–5 | 23% | NYR -1.5 29% | 6.2 / 5.5 (over 55%) | Joel Hofer (confirmed) / Dylan Garand (confirmed) | STL +100 / NYR -120 | no edge | no edge | no edge |
| 7:00 PM | MIN @ PHI | MIN 3, PHI 2 | MIN 63% | MIN -165 / PHI +165 | 3.4 – 2.6 | 1–6 / 1–5 | 22% | MIN -1.5 40% | 6.1 / 5.5 (over 53%) | Jesper Wallstedt (confirmed) / Dan Vladar (confirmed) | MIN -185 / PHI +154 | no edge | no edge | no edge |
| 7:00 PM | VGK @ PIT | VGK 3, PIT 4 | PIT 53% | VGK +115 / PIT -115 | 3.1 – 3.3 | 1–5 / 1–6 | 22% | PIT -1.5 33% | 6.5 / 6.5 (over 49%) | Adin Hill (expected) / Arturs Silovs (confirmed) | VGK -105 / PIT -115 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 7:00 PM | DAL @ WSH | DAL 2, WSH 3 | WSH 51% | DAL +105 / WSH -105 | 2.9 – 3.0 | 1–5 / 1–5 | 23% | WSH -1.5 30% | 5.9 / 5.5 (over 51%) | Jake Oettinger (confirmed) / Logan Thompson (confirmed) | DAL -108 / WSH -112 | no edge | no edge | no edge |
| 7:00 PM | COL @ CBJ | COL 4, CBJ 3 | COL 55% | COL -120 / CBJ +120 | 3.4 – 3.1 | 1–6 / 1–6 | 22% | COL -1.5 34% | 6.5 / 6.5 (over 50%) | Scott Wedgewood (confirmed) / Cam Talbot (confirmed) | COL -125 / CBJ +105 | no edge | no edge | no edge |
| 7:30 PM | EDM @ NJD | EDM 2, NJD 3 | NJD 59% | EDM +145 / NJD -145 | 2.8 – 3.4 | 1–5 / 1–6 | 21% | NJD -1.5 38% | 6.2 / 6.5 (over 46%) | Tristan Jarry (confirmed) / Connor Hellebuyck (confirmed) | EDM +136 / NJD -162 | no edge | no edge | no edge |
| 8:00 PM | CAR @ NSH | CAR 4, NSH 3 | CAR 66% | CAR -195 / NSH +195 | 3.7 – 2.7 | 1–6 / 1–5 | 20% | CAR -1.5 44% | 6.4 / 6.5 (over 48%) | Pyotr Kochetkov (expected) / Juuse Saros (confirmed) | CAR -198 / NSH +164 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 9:00 PM | ANA @ VAN | ANA 4, VAN 3 | ANA 61% | ANA -155 / VAN +155 | 3.9 – 3.2 | 1–6 / 1–6 | 20% | ANA -1.5 41% | 7.1 / 6.5 (over 59%) | Laurent Brossoit (confirmed) / Kevin Lankinen (confirmed) | ANA -155 / VAN +130 | no edge | no edge | no edge |

## Wednesday, November 4

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected goals | 80% range | Overtime | Puck line | Total: model / line | Goalies | Posted moneyline | Puck line edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 7:30 PM | OTT @ BUF | OTT 3, BUF 4 | BUF 55% | OTT +120 / BUF -120 | 3.1 – 3.4 | 1–5 / 1–6 | 21% | BUF -1.5 34% | 6.5 / 6.5 (over 50%) | Samuel Ersson (expected) / Colten Ellis (expected) | OTT +114 / BUF -135 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 7:30 PM | CHI @ FLA | CHI 3, FLA 4 | FLA 68% | CHI +215 / FLA -215 | 2.5 – 3.7 | 1–5 / 1–6 | 20% | FLA -1.5 46% | 6.3 / 5.5 (over 58%) | Spencer Knight (expected) / Jacob Markstrom (expected) | CHI +205 / FLA -250 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 10:00 PM | SJS @ LAK | SJS 3, LAK 4 | LAK 63% | SJS +170 / LAK -170 | 2.8 – 3.6 | 1–5 / 1–6 | 21% | LAK -1.5 42% | 6.4 / 6.5 (over 48%) | Yaroslav Askarov (expected) / Darcy Kuemper (expected) | SJS +130 / LAK -155 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 10:00 PM | CGY @ SEA | CGY 3, SEA 4 | SEA 57% | CGY +130 / SEA -130 | 3.0 – 3.4 | 1–5 / 1–6 | 21% | SEA -1.5 36% | 6.4 / 6.5 (over 47%) | Dustin Wolf (expected) / Philipp Grubauer (expected) | CGY +130 / SEA -155 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |

## Thursday, November 5

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected goals | 80% range | Overtime | Puck line | Total: model / line | Goalies | Posted moneyline | Puck line edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 7:00 PM | UTA @ MTL | UTA 4, MTL 3 | UTA 52% | UTA -110 / MTL +110 | 3.2 – 3.1 | 1–6 / 1–5 | 22% | UTA -1.5 31% | 6.3 | Karel Vejmelka (expected) / Jacob Fowler (expected) | – | no line yet (model fair MTL +1.5 -225 / UTA -1.5 +225) | no line yet | no line yet |
| 7:00 PM | VGK @ DET | VGK 3, DET 2 | VGK 55% | VGK -120 / DET +120 | 3.1 – 2.8 | 1–5 / 1–5 | 22% | VGK -1.5 33% | 6.0 | Carter Hart (expected) / John Gibson (expected) | – | no line yet (model fair DET +1.5 -205 / VGK -1.5 +205) | no line yet | no line yet |
| 7:00 PM | CHI @ TBL | CHI 2, TBL 5 | TBL 80% | CHI +405 / TBL -405 | 2.3 – 4.5 | 0–4 / 2–7 | 15% | TBL -1.5 62% | 6.8 | Arvid Soderblom (expected) / Andrei Vasilevskiy (expected) | – | no line yet (model fair TBL -1.5 -165 / CHI +1.5 +165) | no line yet | no line yet |
| 7:00 PM | STL @ NJD | STL 2, NJD 3 | NJD 56% | STL +125 / NJD -125 | 2.8 – 3.2 | 1–5 / 1–6 | 22% | NJD -1.5 35% | 6.0 | Joel Hofer (expected) / Connor Hellebuyck (expected) | – | no line yet (model fair NJD -1.5 +190 / STL +1.5 -190) | no line yet | no line yet |
| 7:00 PM | CAR @ NYI | CAR 3, NYI 2 | CAR 62% | CAR -160 / NYI +160 | 3.5 – 2.7 | 1–6 / 1–5 | 22% | CAR -1.5 40% | 6.2 | Pyotr Kochetkov (expected) / Ilya Sorokin (expected) | – | no line yet (model fair NYI +1.5 -150 / CAR -1.5 +150) | no line yet | no line yet |
| 7:00 PM | PHI @ NYR | PHI 3, NYR 4 | NYR 58% | PHI +135 / NYR -135 | 2.9 – 3.3 | 1–5 / 1–6 | 22% | NYR -1.5 37% | 6.2 | Dan Vladar (expected) / James Reimer (expected) | – | no line yet (model fair NYR -1.5 +175 / PHI +1.5 -175) | no line yet | no line yet |
| 7:00 PM | BOS @ PIT | BOS 3, PIT 4 | PIT 53% | BOS +115 / PIT -115 | 3.2 – 3.4 | 1–6 / 1–6 | 22% | PIT -1.5 33% | 6.6 | Jeremy Swayman (expected) / Arturs Silovs (expected) | – | no line yet (model fair PIT -1.5 +205 / BOS +1.5 -205) | no line yet | no line yet |
| 7:00 PM | DAL @ CBJ | DAL 3, CBJ 2 | DAL 56% | DAL -125 / CBJ +125 | 3.0 – 2.7 | 1–5 / 1–5 | 24% | DAL -1.5 32% | 5.7 | Jake Oettinger (expected) / Jet Greaves (expected) | – | no line yet (model fair CBJ +1.5 -210 / DAL -1.5 +210) | no line yet | no line yet |
| 7:00 PM | VAN @ WPG | VAN 3, WPG 4 | WPG 66% | VAN +190 / WPG -190 | 2.8 – 3.8 | 1–5 / 1–6 | 20% | WPG -1.5 44% | 6.5 | Leevi Meriläinen (expected) / Stuart Skinner (expected) | – | no line yet (model fair WPG -1.5 +125 / VAN +1.5 -125) | no line yet | no line yet |
| 8:00 PM | ANA @ EDM | ANA 3, EDM 4 | EDM 61% | ANA +160 / EDM -160 | 3.1 – 3.9 | 1–6 / 1–6 | 20% | EDM -1.5 41% | 7.0 | Lukas Dostal (expected) / Tristan Jarry (expected) | – | no line yet (model fair EDM -1.5 +145 / ANA +1.5 -145) | no line yet | no line yet |
| 9:30 PM | NSH @ COL | NSH 3, COL 4 | COL 65% | NSH +190 / COL -190 | 2.8 – 3.9 | 1–5 / 1–6 | 20% | COL -1.5 45% | 6.7 | Juuse Saros (expected) / Mackenzie Blackwood (expected) | – | no line yet (model fair COL -1.5 +125 / NSH +1.5 -125) | no line yet | no line yet |

\* price not posted; assumed -110.

## How the 2026-27 predictions have done

| Predictor | Games | Log loss | Brier | Winners | Goals MAE | Total MAE | 80% range hit |
|---|---|---|---|---|---|---|---|
| Final prediction | 235 | 0.6505 | 0.2293 | 61.3% | 1.40 | 1.79 | 89.4% |
| Model only (before blending) | 235 | 0.6516 | 0.2299 | 60.0% | – | – | – |
| Elo | 235 | 0.6646 | 0.2360 | 61.3% | – | – | – |
| Final prediction, games with a line | 101 | 0.6570 | 0.2324 | 58.4% | 1.40 | 1.84 | 89.1% |
| Model only, games with a line | 101 | 0.6597 | 0.2338 | 55.4% | – | – | – |
| Betting market (de-vigged moneyline) | 101 | 0.6599 | 0.2338 | 59.4% | – | 1.81 | – |

Log loss and Brier score the win chances (lower is better; a coin flip scores 0.693 and 0.250). Hockey is close to a coin flip, so differences in the third decimal matter, and only over hundreds of games. Goals MAE is the average miss on each team's goals.

Overtime: predicted in 21.6% of regular-season games, happened in 22.1%.

134 of these games were played before the predictor went live. They are backfilled walk-forward (each day predicted from earlier days only) with the actual starting goalies and no betting line. Every game since is graded on the prediction logged before puck drop.

### Betting edges

| Market | Edges | Record (W-L-P) | Staked | Units won | ROI | Expected ROI |
|---|---|---|---|---|---|---|
| Puck line | 1 | 0-1-0 | 1.3 | -1.29 | -100.0% | +11.8% |
| Moneyline | 8 | 4-4-0 | 8.7 | +1.83 | +21.2% | +6.4% |
| Total | 1 | 0-1-0 | 0.9 | -0.89 | -100.0% | +3.0% |

Moneyline moved toward the model's edge on the first line seen before puck drop: 18 of 21 games (86%).

Each edge at the stake and price logged with the last prediction before puck drop (edges logged before edges were priced from the final prediction are left out); pushes return the stake. Units are 1% of the bankroll; ROI is units won per unit staked, and expected ROI is what the edges' EVs promised. The moneyline moving toward the model's edge (closing line value) is the quickest sign that it knows something the market doesn't yet.

### Results, Monday, November 2

| Game | Predicted | Final | Win chance for winner | Inside 80% ranges | Goalies |
|---|---|---|---|---|---|
| VGK @ BOS | 4–3 | 2–3 (SO) | 48% | yes | Carter Hart / Jeremy Swayman |
| DET @ FLA | 2–3 | 5–3 | 39% | yes | Daniil Tarasov / Jacob Markstrom |
| COL @ CHI | 4–3 | 5–2 | 68% | yes | Mackenzie Blackwood / Spencer Knight |
| CGY @ SJS | 4–3 | 2–1 | 52% | yes | Dustin Wolf / Yaroslav Askarov |

## Power ratings

Goals per game better than an average team, from the goal-rate model: offense and defense combine 5-on-5 expected goals (score and venue adjusted), special teams and actual goals, each weighted against a preseason prior. Defense is positive when it holds opponents below average. Goaltending is rated separately below.

| # | Team | Net | Offense | Defense | 5v5 xGF/60 | 5v5 xGA/60 | PP xGF/60 | PK xGA/60 | Elo |
|---|---|---|---|---|---|---|---|---|---|
| 1 | CAR | +0.70 | +0.43 | +0.27 | 3.39 | 2.39 | 8.39 | 6.90 | 1585 |
| 2 | UTA | +0.45 | +0.22 | +0.22 | 3.11 | 2.35 | 7.95 | 8.39 | 1509 |
| 3 | TBL | +0.35 | +0.20 | +0.15 | 2.91 | 2.50 | 8.19 | 7.84 | 1538 |
| 4 | VGK | +0.34 | +0.06 | +0.28 | 2.71 | 2.33 | 8.93 | 7.37 | 1524 |
| 5 | MIN | +0.33 | +0.14 | +0.19 | 2.98 | 2.47 | 9.18 | 8.13 | 1545 |
| 6 | COL | +0.32 | +0.30 | +0.02 | 2.98 | 2.70 | 7.75 | 7.96 | 1556 |
| 7 | PIT | +0.26 | +0.22 | +0.03 | 3.07 | 2.62 | 8.00 | 7.67 | 1495 |
| 8 | NJD | +0.26 | +0.03 | +0.22 | 2.83 | 2.38 | 9.03 | 7.82 | 1511 |
| 9 | FLA | +0.24 | +0.01 | +0.23 | 2.64 | 2.39 | 9.39 | 7.68 | 1502 |
| 10 | DAL | +0.21 | -0.11 | +0.31 | 2.46 | 2.31 | 9.27 | 7.32 | 1527 |
| 11 | STL | +0.10 | +0.01 | +0.10 | 2.64 | 2.57 | 6.88 | 7.41 | 1508 |
| 12 | EDM | +0.10 | +0.12 | -0.02 | 2.60 | 2.70 | 9.70 | 8.00 | 1535 |
| 13 | BUF | +0.10 | +0.10 | -0.01 | 2.78 | 2.69 | 7.89 | 8.34 | 1521 |
| 14 | WSH | +0.07 | +0.12 | -0.04 | 2.90 | 2.75 | 7.75 | 8.03 | 1517 |
| 15 | OTT | +0.07 | -0.03 | +0.10 | 2.64 | 2.56 | 8.00 | 8.29 | 1514 |
| 16 | LAK | +0.02 | -0.11 | +0.13 | 2.57 | 2.54 | 8.09 | 8.22 | 1471 |
| 17 | DET | -0.00 | -0.06 | +0.06 | 2.68 | 2.59 | 8.49 | 8.66 | 1488 |
| 18 | NYR | -0.01 | +0.01 | -0.02 | 2.70 | 2.74 | 8.56 | 7.74 | 1487 |
| 19 | MTL | -0.03 | +0.05 | -0.08 | 2.82 | 2.80 | 7.11 | 8.30 | 1534 |
| 20 | BOS | -0.04 | +0.03 | -0.07 | 2.72 | 2.82 | 7.70 | 8.11 | 1532 |
| 21 | CBJ | -0.08 | -0.09 | +0.01 | 2.60 | 2.66 | 7.70 | 8.53 | 1488 |
| 22 | NYI | -0.08 | -0.07 | -0.01 | 2.69 | 2.73 | 7.50 | 8.51 | 1490 |
| 23 | TOR | -0.12 | -0.00 | -0.11 | 2.51 | 2.82 | 8.78 | 8.22 | 1486 |
| 24 | NSH | -0.14 | -0.05 | -0.09 | 2.63 | 2.79 | 7.83 | 7.53 | 1482 |
| 25 | WPG | -0.16 | -0.14 | -0.02 | 2.52 | 2.73 | 8.17 | 9.04 | 1460 |
| 26 | CGY | -0.22 | -0.10 | -0.12 | 2.59 | 2.83 | 7.20 | 8.09 | 1468 |
| 27 | SEA | -0.26 | -0.10 | -0.16 | 2.43 | 2.87 | 7.19 | 8.51 | 1478 |
| 28 | PHI | -0.27 | -0.26 | -0.01 | 2.32 | 2.69 | 7.73 | 7.51 | 1477 |
| 29 | ANA | -0.37 | -0.00 | -0.37 | 2.73 | 3.08 | 7.99 | 8.49 | 1480 |
| 30 | CHI | -0.70 | -0.27 | -0.43 | 2.35 | 3.16 | 7.18 | 8.28 | 1426 |
| 31 | VAN | -0.73 | -0.22 | -0.51 | 2.29 | 3.24 | 7.65 | 8.76 | 1411 |
| 32 | SJS | -0.81 | -0.25 | -0.55 | 2.30 | 3.30 | 7.23 | 8.80 | 1458 |

## Goalies

Each team's likeliest next starter. GSAx is goals saved above expected (from this predictor's own shot model), shrunk hard toward a slightly below-average prior, since goaltending repeats poorly from season to season.

| Team | Likely next starter | Share of recent starts | GSAx per 100 shots | Goals per game vs average |
|---|---|---|---|---|
| WSH | Logan Thompson | 68% | +0.42 | +0.17 |
| NYI | Ilya Sorokin | 71% | +0.39 | +0.16 |
| BOS | Jeremy Swayman | 74% | +0.32 | +0.14 |
| MTL | Jacob Fowler | 62% | +0.30 | +0.13 |
| MIN | Jesper Wallstedt | 87% | +0.22 | +0.09 |
| CGY | Devin Cooley | 47% | +0.21 | +0.09 |
| COL | Mackenzie Blackwood | 52% | +0.17 | +0.07 |
| OTT | Linus Ullmark | 40% | +0.14 | +0.06 |
| DAL | Jake Oettinger | 80% | +0.14 | +0.06 |
| TBL | Andrei Vasilevskiy | 77% | +0.13 | +0.05 |
| CHI | Spencer Knight | 81% | +0.12 | +0.05 |
| CBJ | Jet Greaves | 57% | +0.10 | +0.04 |
| CAR | Pyotr Kochetkov | 69% | +0.05 | +0.02 |
| STL | Joel Hofer | 73% | +0.00 | +0.00 |
| WPG | Stuart Skinner | 66% | -0.01 | -0.01 |
| PHI | Dan Vladar | 52% | -0.03 | -0.01 |
| NJD | Jake Allen | 54% | -0.06 | -0.02 |
| NYR | Dylan Garand | 67% | -0.06 | -0.03 |
| BUF | Ukko-Pekka Luukkonen | 63% | -0.13 | -0.05 |
| SJS | Yaroslav Askarov | 61% | -0.13 | -0.06 |
| DET | John Gibson | 77% | -0.16 | -0.07 |
| FLA | Akira Schmid | 51% | -0.16 | -0.07 |
| TOR | Sergei Bobrovsky | 61% | -0.16 | -0.07 |
| ANA | Lukas Dostal | 57% | -0.17 | -0.07 |
| SEA | Philipp Grubauer | 63% | -0.19 | -0.08 |
| LAK | Darcy Kuemper | 58% | -0.20 | -0.09 |
| UTA | Karel Vejmelka | 74% | -0.21 | -0.09 |
| NSH | Juuse Saros | 66% | -0.24 | -0.10 |
| PIT | Arturs Silovs | 64% | -0.29 | -0.12 |
| VAN | Leevi Meriläinen | 65% | -0.29 | -0.12 |
| EDM | Tristan Jarry | 51% | -0.32 | -0.14 |
| VGK | Adin Hill | 69% | -0.35 | -0.15 |

## Current model fit

- Fitted on 5827 games from 2022-23 to 2026-27.
- Home ice: +3.0% goals for the home team relative to the visitor.
- Second night of a back-to-back: -5.7% goals scored, +3.3% goals allowed.
- Starting goalie: each goal per game he saves above average lowers the opponent's rate by 23%.
- Blend: 48% on the betting line wherever there is one (fitted on 101 logged games, shrunk toward the backtest value).
- Simulator: 22.3% of recent regular-season games reached overtime; trailing teams usually have the goalie pulled with 2 minutes left when down one and 3 when down two; empty-net goals come at 0.40 a minute with the net empty; three-on-three overtime produces 1.03 goals per five minutes.
