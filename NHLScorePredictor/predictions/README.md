# NHL score predictions

Updated Sat Nov 21, 2026 03:12 PM ET. Refreshed automatically several times a day during the season; each game's prediction is locked at puck drop and graded once the final score is in.

Each game is simulated 10,000 times minute by minute, with pulled goalies, empty-net goals, overtime and shootouts. The predicted score is the most common final score in which the likelier winner wins; as in the official result, a shootout winner gets one extra goal. Hockey is low-scoring and luck-heavy, so read the win chance and the ranges (80% of simulated outcomes for each team) before the single score.

Goalies marked with a percentage are projected from recent starts (the share is the chance he starts); "probable" or "confirmed" ones come from ESPN and replace the projection when available.

The fair moneyline is the American odds that match the win chance exactly, with no bookmaker margin: -150 means risk $150 to win $100, +150 means risk $100 to win $150. A sportsbook's price is a little worse on both sides because of its cut, so a book only offers value on a team when its price beats the fair line. The puck line is the favorite's chance to win by two or more.

The edge columns price each side of the puck line, moneyline and total with the final prediction: the model's goal rates blended with the market's, simulated against the posted lines, overtime and shootout included (the shootout winner gets one goal), and anchored to the market's own chances so only what the blend moves off the market counts. Each cell shows the side with the best expected value (EV) per $1 bet at the posted price. A side is an edge only if its EV is at least 3%: a pick shows its price, EV, its chance of winning the bet and its stake, a 25% share of the Kelly stake in units of 1% of the bankroll, with at most 3 units on one game; "no edge" means neither side clears the bar. A projected starting goalie is wrong about a third of the time and the market prices the real one, so edges wait until both starters are confirmed. A total with no posted price is assumed to be -110 (marked \*); the puck line and moneyline are never assumed, so without a price the cell shows the model's fair odds instead. Treat the edges as an experiment, not betting advice; see the backtest for how they have done on past seasons. Their record is tracked live below.

## Saturday, November 21

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected goals | 80% range | Overtime | Puck line | Total: model / line | Goalies | Posted moneyline | Puck line edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 3:30 PM | CHI @ CGY | CHI 2, CGY 3 | CGY 60% | CHI +150 / CGY -150 | 2.7 – 3.4 | 1–5 / 1–6 | 22% | CGY -1.5 38% | 6.1 / 5.5 (over 54%) | Spencer Knight (expected) / Dustin Wolf (expected) | CHI +136 / CGY -162 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 6:00 PM | BUF @ FLA | BUF 3, FLA 4 | FLA 55% | BUF +125 / FLA -125 | 3.0 – 3.3 | 1–5 / 1–6 | 22% | FLA -1.5 34% | 6.4 / 6.5 (over 48%) | Alex Lyon (expected) / Jacob Markstrom (confirmed) | BUF +120 / FLA -142 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 6:00 PM | PIT @ NSH | PIT 3, NSH 4 | NSH 51% | PIT +105 / NSH -105 | 3.3 – 3.3 | 1–6 / 1–6 | 21% | NSH -1.5 32% | 6.6 / 6.5 (over 51%) | Arturs Silovs (expected) / Juuse Saros (expected) | PIT +114 / NSH -135 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 7:00 PM | WSH @ BOS | WSH 3, BOS 4 | BOS 56% | WSH +130 / BOS -130 | 3.1 – 3.5 | 1–6 / 1–6 | 21% | BOS -1.5 36% | 6.6 / 6.5 (over 52%) | Charlie Lindgren (confirmed) / Jeremy Swayman (confirmed) | WSH +114 / BOS -135 | no edge | no edge | no edge |
| 7:00 PM | CBJ @ TOR | CBJ 3, TOR 4 | TOR 52% | CBJ +110 / TOR -110 | 3.1 – 3.3 | 1–6 / 1–6 | 23% | TOR -1.5 32% | 6.4 / 6.5 (over 48%) | Cam Talbot (confirmed) / Anthony Stolarz (confirmed) | CBJ -102 / TOR -118 | no edge | no edge | no edge |
| 7:00 PM | PHI @ MTL | PHI 2, MTL 3 | MTL 59% | PHI +145 / MTL -145 | 2.7 – 3.3 | 1–5 / 1–6 | 22% | MTL -1.5 37% | 6.0 / 5.5 (over 52%) | Dan Vladar (confirmed) / Jacob Fowler (confirmed) | PHI +136 / MTL -162 | no edge | no edge | no edge |
| 7:00 PM | LAK @ OTT | LAK 2, OTT 3 | OTT 61% | LAK +160 / OTT -160 | 2.6 – 3.3 | 1–5 / 1–6 | 22% | OTT -1.5 39% | 5.9 / 5.5 (over 51%) | Anton Forsberg (confirmed) / Linus Ullmark (confirmed) | LAK +154 / OTT -185 | no edge | no edge | no edge |
| 7:00 PM | NYI @ DET | NYI 4, DET 3 | NYI 53% | NYI -110 / DET +110 | 3.2 – 3.0 | 1–6 / 1–5 | 23% | NYI -1.5 31% | 6.2 / 5.5 (over 55%) | Ilya Sorokin (expected) / John Gibson (confirmed) | NYI -130 / DET +110 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 7:00 PM | NJD @ STL | NJD 3, STL 2 | NJD 51% | NJD -105 / STL +105 | 3.1 – 3.0 | 1–5 / 1–5 | 23% | NJD -1.5 30% | 6.1 / 5.5 (over 54%) | Connor Hellebuyck (confirmed) / Joel Hofer (expected) | NJD -130 / STL +110 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 7:00 PM | VGK @ WPG | VGK 3, WPG 2 | VGK 57% | VGK -130 / WPG +130 | 3.3 – 2.9 | 1–6 / 1–5 | 22% | VGK -1.5 35% | 6.2 / 6.5 (over 45%) | Carter Hart (confirmed) / Stuart Skinner (confirmed) | VGK -135 / WPG +114 | no edge | no edge | no edge |
| 9:00 PM | ANA @ UTA | ANA 3, UTA 4 | UTA 63% | ANA +170 / UTA -170 | 3.1 – 4.0 | 1–6 / 1–7 | 20% | UTA -1.5 43% | 7.1 / 6.5 (over 58%) | Ville Husso (confirmed) / Sebastian Cossa (confirmed) | ANA +140 / UTA -166 | UTA -1.5 (+136): EV +6.9%, 45%, stake 1.3u | UTA (-166): EV +3.3%, 64%, stake 1.4u | no edge |
| 10:00 PM | MIN @ VAN | MIN 4, VAN 3 | MIN 74% | MIN -280 / VAN +280 | 4.1 – 2.5 | 2–7 / 1–5 | 19% | MIN -1.5 53% | 6.5 / 6.5 (over 50%) | Jesper Wallstedt (confirmed) / Leevi Meriläinen (confirmed) | MIN -298 / VAN +240 | no edge | no edge | no edge |
| 10:00 PM | SEA @ SJS | SEA 4, SJS 3 | SEA 52% | SEA -110 / SJS +110 | 3.4 – 3.2 | 1–6 / 1–6 | 22% | SEA -1.5 31% | 6.6 / 6.5 (over 51%) | Philipp Grubauer (expected) / Alex Nedeljkovic (confirmed) | SEA -102 / SJS -118 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |

## Sunday, November 22

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected goals | 80% range | Overtime | Puck line | Total: model / line | Goalies | Posted moneyline | Puck line edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 12:30 PM | CAR @ NYR | CAR 4, NYR 3 | CAR 57% | CAR -130 / NYR +130 | 3.4 – 2.9 | 1–6 / 1–5 | 21% | CAR -1.5 35% | 6.3 / 6.5 (over 46%) | Brandon Bussi (expected) / Dylan Garand (expected) | CAR -148 / NYR +124 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 5:00 PM | BUF @ TBL | BUF 3, TBL 4 | TBL 66% | BUF +190 / TBL -190 | 2.7 – 3.7 | 1–5 / 1–6 | 20% | TBL -1.5 45% | 6.4 / 6.5 (over 48%) | Ukko-Pekka Luukkonen (expected) / Andrei Vasilevskiy (expected) | BUF +170 / TBL -205 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 7:00 PM | EDM @ STL | EDM 4, STL 3 | EDM 53% | EDM -110 / STL +110 | 3.2 – 3.0 | 1–6 / 1–5 | 22% | EDM -1.5 32% | 6.3 / 6.5 (over 46%) | Tristan Jarry (expected) / Jordan Binnington (expected) | EDM -135 / STL +114 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 7:00 PM | PIT @ DAL | PIT 3, DAL 4 | DAL 64% | PIT +175 / DAL -175 | 2.7 – 3.6 | 1–5 / 1–6 | 21% | DAL -1.5 42% | 6.3 / 6.5 (over 47%) | Sergei Murashov (expected) / Jake Oettinger (expected) | PIT +185 / DAL -225 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 8:00 PM | CHI @ VAN | CHI 3, VAN 4 | VAN 51% | CHI +100 / VAN -100 | 3.2 – 3.2 | 1–6 / 1–6 | 21% | VAN -1.5 30% | 6.4 / 6.5 (over 48%) | Drew Commesso (expected) / Kevin Lankinen (expected) | CHI -108 / VAN -112 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |

## Monday, November 23

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected goals | 80% range | Overtime | Puck line | Total: model / line | Goalies | Posted moneyline | Puck line edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 7:00 PM | CBJ @ NJD | CBJ 2, NJD 3 | NJD 62% | CBJ +160 / NJD -160 | 2.7 – 3.5 | 1–5 / 1–6 | 22% | NJD -1.5 40% | 6.2 | Jet Greaves (expected) / Connor Hellebuyck (expected) | – | no line yet (model fair NJD -1.5 +150 / CBJ +1.5 -150) | no line yet | no line yet |
| 7:30 PM | LAK @ MTL | LAK 2, MTL 3 | MTL 57% | LAK +130 / MTL -130 | 2.8 – 3.2 | 1–5 / 1–6 | 22% | MTL -1.5 35% | 6.0 | Darcy Kuemper (expected) / Jacob Fowler (expected) | – | no line yet (model fair MTL -1.5 +190 / LAK +1.5 -190) | no line yet | no line yet |
| 7:30 PM | CGY @ OTT | CGY 2, OTT 3 | OTT 66% | CGY +195 / OTT -195 | 2.6 – 3.6 | 1–5 / 1–6 | 21% | OTT -1.5 44% | 6.1 | Dustin Wolf (expected) / Linus Ullmark (expected) | – | no line yet (model fair OTT -1.5 +125 / CGY +1.5 -125) | no line yet | no line yet |
| 7:30 PM | TOR @ NYI | TOR 3, NYI 4 | NYI 59% | TOR +140 / NYI -140 | 2.9 – 3.5 | 1–5 / 1–6 | 21% | NYI -1.5 37% | 6.4 | Sergei Bobrovsky (expected) / Ilya Sorokin (expected) | – | no line yet (model fair NYI -1.5 +170 / TOR +1.5 -170) | no line yet | no line yet |
| 7:30 PM | UTA @ WPG | UTA 4, WPG 3 | UTA 57% | UTA -130 / WPG +130 | 3.4 – 3.0 | 1–6 / 1–5 | 22% | UTA -1.5 36% | 6.3 | Karel Vejmelka (expected) / Stuart Skinner (expected) | – | no line yet (model fair WPG +1.5 -180 / UTA -1.5 +180) | no line yet | no line yet |
| 9:40 PM | ANA @ SEA | ANA 3, SEA 4 | SEA 55% | ANA +125 / SEA -125 | 3.3 – 3.7 | 1–6 / 1–6 | 20% | SEA -1.5 36% | 7.0 | Lukas Dostal (expected) / Philipp Grubauer (expected) | – | no line yet (model fair SEA -1.5 +180 / ANA +1.5 -180) | no line yet | no line yet |
| 10:00 PM | MIN @ SJS | MIN 4, SJS 3 | MIN 73% | MIN -270 / SJS +270 | 4.1 – 2.5 | 2–7 / 1–5 | 18% | MIN -1.5 52% | 6.6 | Jesper Wallstedt (expected) / Yaroslav Askarov (expected) | – | no line yet (model fair SJS +1.5 +110 / MIN -1.5 -110) | no line yet | no line yet |

\* price not posted; assumed -110.

## How the 2026-27 predictions have done

| Predictor | Games | Log loss | Brier | Winners | Goals MAE | Total MAE | 80% range hit |
|---|---|---|---|---|---|---|---|
| Final prediction | 358 | 0.6578 | 0.2328 | 62.0% | 1.38 | 1.82 | 89.8% |
| Model only (before blending) | 358 | 0.6605 | 0.2341 | 60.1% | – | – | – |
| Elo | 358 | 0.6701 | 0.2387 | 58.1% | – | – | – |
| Final prediction, games with a line | 224 | 0.6639 | 0.2356 | 60.3% | 1.37 | 1.86 | 90.0% |
| Model only, games with a line | 224 | 0.6682 | 0.2378 | 57.1% | – | – | – |
| Betting market (de-vigged moneyline) | 224 | 0.6622 | 0.2349 | 60.3% | – | 1.85 | – |

Log loss and Brier score the win chances (lower is better; a coin flip scores 0.693 and 0.250). Hockey is close to a coin flip, so differences in the third decimal matter, and only over hundreds of games. Goals MAE is the average miss on each team's goals.

Overtime: predicted in 21.5% of regular-season games, happened in 22.3%.

134 of these games were played before the predictor went live. They are backfilled walk-forward (each day predicted from earlier days only) with the actual starting goalies and no betting line. Every game since is graded on the prediction logged before puck drop.

### Betting edges

| Market | Edges | Record (W-L-P) | Staked | Units won | ROI | Expected ROI |
|---|---|---|---|---|---|---|
| Puck line | 4 | 0-4-0 | 3.9 | -3.91 | -100.0% | +8.2% |
| Moneyline | 12 | 7-5-0 | 13.2 | +4.49 | +34.1% | +5.7% |
| Total | 2 | 1-1-0 | 1.7 | +0.04 | +2.4% | +3.4% |

Moneyline moved toward the model's edge on the first line seen before puck drop: 39 of 51 games (76%).

Each edge at the stake and price logged with the last prediction before puck drop (edges logged before edges were priced from the final prediction are left out); pushes return the stake. Units are 1% of the bankroll; ROI is units won per unit staked, and expected ROI is what the edges' EVs promised. The moneyline moving toward the model's edge (closing line value) is the quickest sign that it knows something the market doesn't yet.

### Results, Thursday, November 19

| Game | Predicted | Final | Win chance for winner | Inside 80% ranges | Goalies |
|---|---|---|---|---|---|
| LAK @ TOR | 3–4 | 4–3 (SO) | 48% | yes | Darcy Kuemper / Anthony Stolarz |
| PHI @ OTT | 2–3 | 6–5 (OT) | 41% | no | Joseph Woll / Samuel Ersson |
| STL @ PIT | 4–3 | 5–2 | 52% | yes | Joel Hofer / Arturs Silovs |
| BUF @ WSH | 3–4 | 6–3 | 43% | yes | Ukko-Pekka Luukkonen / Logan Thompson |
| MTL @ CAR | 3–4 | 2–1 (OT) | 27% | no | Jakub Dobes / Pyotr Kochetkov |
| NYI @ WPG | 3–4 | 3–4 (OT) | 51% | yes | Semyon Varlamov / Nico Daws |
| EDM @ TBL | 2–3 | 1–3 | 58% | yes | Devon Levi / Andrei Vasilevskiy |
| CBJ @ CHI | 4–3 | 4–2 | 58% | yes | Cam Talbot / Spencer Knight |
| MIN @ CGY | 4–3 | 4–1 | 66% | yes | Jesper Wallstedt / Dustin Wolf |
| ANA @ COL | 3–4 | 0–4 | 59% | no | Lukas Dostal / Scott Wedgewood |
| VAN @ SEA | 3–4 | 1–5 | 60% | yes | Leevi Meriläinen / Philipp Grubauer |
| DAL @ VGK | 2–3 | 4–3 (SO) | 48% | yes | Jake Oettinger / Adin Hill |

## Power ratings

Goals per game better than an average team, from the goal-rate model: offense and defense combine 5-on-5 expected goals (score and venue adjusted), special teams and actual goals, each weighted against a preseason prior. Defense is positive when it holds opponents below average. Goaltending is rated separately below.

| # | Team | Net | Offense | Defense | 5v5 xGF/60 | 5v5 xGA/60 | PP xGF/60 | PK xGA/60 | Elo |
|---|---|---|---|---|---|---|---|---|---|
| 1 | CAR | +0.78 | +0.47 | +0.31 | 3.42 | 2.32 | 8.65 | 7.14 | 1589 |
| 2 | TBL | +0.48 | +0.22 | +0.26 | 2.94 | 2.36 | 8.01 | 7.99 | 1557 |
| 3 | UTA | +0.39 | +0.23 | +0.16 | 3.13 | 2.41 | 8.37 | 8.89 | 1498 |
| 4 | VGK | +0.29 | +0.06 | +0.23 | 2.69 | 2.40 | 9.01 | 7.23 | 1521 |
| 5 | MIN | +0.28 | +0.12 | +0.16 | 2.85 | 2.53 | 8.88 | 7.97 | 1572 |
| 6 | COL | +0.25 | +0.21 | +0.03 | 2.84 | 2.68 | 8.00 | 8.02 | 1555 |
| 7 | PIT | +0.22 | +0.18 | +0.05 | 3.04 | 2.58 | 7.72 | 8.09 | 1478 |
| 8 | OTT | +0.22 | +0.01 | +0.21 | 2.72 | 2.40 | 7.99 | 8.13 | 1525 |
| 9 | DAL | +0.22 | -0.05 | +0.27 | 2.58 | 2.34 | 9.37 | 7.29 | 1532 |
| 10 | STL | +0.18 | +0.07 | +0.10 | 2.81 | 2.57 | 7.32 | 8.14 | 1506 |
| 11 | NJD | +0.15 | +0.03 | +0.13 | 2.75 | 2.50 | 9.18 | 7.87 | 1528 |
| 12 | FLA | +0.12 | -0.05 | +0.17 | 2.50 | 2.47 | 9.59 | 7.63 | 1504 |
| 13 | BOS | +0.12 | +0.07 | +0.05 | 2.82 | 2.66 | 7.72 | 8.12 | 1528 |
| 14 | WSH | +0.09 | +0.13 | -0.05 | 2.92 | 2.72 | 8.01 | 8.13 | 1498 |
| 15 | NYR | +0.08 | +0.02 | +0.06 | 2.70 | 2.64 | 8.86 | 7.71 | 1507 |
| 16 | LAK | +0.05 | -0.13 | +0.17 | 2.53 | 2.48 | 8.11 | 8.12 | 1467 |
| 17 | BUF | +0.03 | +0.06 | -0.04 | 2.72 | 2.70 | 7.99 | 8.69 | 1505 |
| 18 | EDM | +0.02 | +0.01 | +0.01 | 2.42 | 2.67 | 9.78 | 8.36 | 1545 |
| 19 | MTL | +0.01 | +0.04 | -0.03 | 2.79 | 2.75 | 7.60 | 8.53 | 1537 |
| 20 | NYI | -0.07 | -0.01 | -0.07 | 2.75 | 2.80 | 7.33 | 8.80 | 1496 |
| 21 | NSH | -0.11 | -0.01 | -0.11 | 2.74 | 2.82 | 8.09 | 7.65 | 1501 |
| 22 | DET | -0.12 | -0.10 | -0.01 | 2.63 | 2.68 | 8.61 | 8.73 | 1474 |
| 23 | WPG | -0.12 | -0.10 | -0.02 | 2.49 | 2.71 | 8.66 | 8.88 | 1488 |
| 24 | TOR | -0.14 | -0.06 | -0.08 | 2.47 | 2.76 | 8.70 | 8.44 | 1452 |
| 25 | CBJ | -0.17 | -0.06 | -0.11 | 2.66 | 2.79 | 7.91 | 8.54 | 1479 |
| 26 | PHI | -0.19 | -0.22 | +0.03 | 2.35 | 2.62 | 7.92 | 7.63 | 1475 |
| 27 | CGY | -0.29 | -0.14 | -0.14 | 2.52 | 2.86 | 7.02 | 7.68 | 1458 |
| 28 | SEA | -0.32 | -0.13 | -0.19 | 2.41 | 2.90 | 7.31 | 8.76 | 1475 |
| 29 | ANA | -0.38 | +0.02 | -0.40 | 2.72 | 3.10 | 8.01 | 8.18 | 1481 |
| 30 | CHI | -0.63 | -0.28 | -0.35 | 2.24 | 3.03 | 7.22 | 8.63 | 1419 |
| 31 | SJS | -0.76 | -0.23 | -0.54 | 2.33 | 3.25 | 7.35 | 9.24 | 1449 |
| 32 | VAN | -0.78 | -0.25 | -0.54 | 2.23 | 3.25 | 7.82 | 8.88 | 1401 |

## Goalies

Each team's likeliest next starter. GSAx is goals saved above expected (from this predictor's own shot model), shrunk hard toward a slightly below-average prior, since goaltending repeats poorly from season to season.

| Team | Likely next starter | Share of recent starts | GSAx per 100 shots | Goals per game vs average |
|---|---|---|---|---|
| NYI | Ilya Sorokin | 62% | +0.43 | +0.18 |
| MIN | Jesper Wallstedt | 88% | +0.34 | +0.14 |
| MTL | Jacob Fowler | 64% | +0.33 | +0.14 |
| BOS | Jeremy Swayman | 71% | +0.29 | +0.12 |
| WSH | Logan Thompson | 77% | +0.28 | +0.12 |
| COL | Mackenzie Blackwood | 67% | +0.23 | +0.10 |
| TBL | Andrei Vasilevskiy | 78% | +0.17 | +0.07 |
| OTT | Linus Ullmark | 43% | +0.15 | +0.06 |
| NJD | Connor Hellebuyck | 52% | +0.15 | +0.06 |
| STL | Joel Hofer | 74% | +0.15 | +0.06 |
| EDM | Devon Levi | 51% | +0.10 | +0.04 |
| DAL | Jake Oettinger | 78% | +0.07 | +0.03 |
| CAR | Pyotr Kochetkov | 69% | +0.05 | +0.02 |
| CHI | Spencer Knight | 85% | +0.02 | +0.01 |
| NYR | Dylan Garand | 60% | +0.01 | +0.00 |
| WPG | Stuart Skinner | 69% | -0.03 | -0.01 |
| NSH | Juuse Saros | 63% | -0.08 | -0.03 |
| PHI | Joseph Woll | 54% | -0.11 | -0.05 |
| SEA | Philipp Grubauer | 55% | -0.12 | -0.05 |
| BUF | Ukko-Pekka Luukkonen | 49% | -0.14 | -0.06 |
| CBJ | Cam Talbot | 55% | -0.18 | -0.08 |
| UTA | Karel Vejmelka | 62% | -0.19 | -0.08 |
| DET | John Gibson | 52% | -0.21 | -0.09 |
| SJS | Yaroslav Askarov | 68% | -0.22 | -0.09 |
| LAK | Darcy Kuemper | 65% | -0.23 | -0.10 |
| CGY | Dustin Wolf | 54% | -0.24 | -0.10 |
| TOR | Sergei Bobrovsky | 53% | -0.25 | -0.10 |
| FLA | Jacob Markstrom | 53% | -0.26 | -0.11 |
| ANA | Lukas Dostal | 44% | -0.29 | -0.12 |
| VGK | Adin Hill | 56% | -0.30 | -0.12 |
| VAN | Leevi Meriläinen | 71% | -0.34 | -0.14 |
| PIT | Arturs Silovs | 60% | -0.39 | -0.16 |

## Current model fit

- Fitted on 5950 games from 2022-23 to 2026-27.
- Home ice: +2.7% goals for the home team relative to the visitor.
- Second night of a back-to-back: -5.9% goals scored, +3.1% goals allowed.
- Starting goalie: each goal per game he saves above average lowers the opponent's rate by 21%.
- Blend: 51% on the betting line wherever there is one (fitted on 224 logged games, shrunk toward the backtest value).
- Simulator: 22.3% of recent regular-season games reached overtime; trailing teams usually have the goalie pulled with 2 minutes left when down one and 3 when down two; empty-net goals come at 0.40 a minute with the net empty; three-on-three overtime produces 1.03 goals per five minutes.
