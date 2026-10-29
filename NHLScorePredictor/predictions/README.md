# NHL score predictions

Updated Wed Oct 28, 2026 10:51 PM ET. Refreshed automatically several times a day during the season; each game's prediction is locked at puck drop and graded once the final score is in.

Each game is simulated 10,000 times minute by minute, with pulled goalies, empty-net goals, overtime and shootouts. The predicted score is the most common final score in which the likelier winner wins; as in the official result, a shootout winner gets one extra goal. Hockey is low-scoring and luck-heavy, so read the win chance and the ranges (80% of simulated outcomes for each team) before the single score.

Goalies marked with a percentage are projected from recent starts (the share is the chance he starts); "probable" or "confirmed" ones come from ESPN and replace the projection when available.

The fair moneyline is the American odds that match the win chance exactly, with no bookmaker margin: -150 means risk $150 to win $100, +150 means risk $100 to win $150. A sportsbook's price is a little worse on both sides because of its cut, so a book only offers value on a team when its price beats the fair line. The puck line is the favorite's chance to win by two or more.

The edge columns price each side of the puck line, moneyline and total with the final prediction: the model's goal rates blended with the market's, simulated against the posted lines, overtime and shootout included (the shootout winner gets one goal), and anchored to the market's own chances so only what the blend moves off the market counts. Each cell shows the side with the best expected value (EV) per $1 bet at the posted price. A side is an edge only if its EV is at least 3%: a pick shows its price, EV, its chance of winning the bet and its stake, a 25% share of the Kelly stake in units of 1% of the bankroll, with at most 3 units on one game; "no edge" means neither side clears the bar. A projected starting goalie is wrong about a third of the time and the market prices the real one, so edges wait until both starters are confirmed. A total with no posted price is assumed to be -110 (marked \*); the puck line and moneyline are never assumed, so without a price the cell shows the model's fair odds instead. Treat the edges as an experiment, not betting advice; see the backtest for how they have done on past seasons. Their record is tracked live below.

## Thursday, October 29

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected goals | 80% range | Overtime | Puck line | Total: model / line | Goalies | Posted moneyline | Puck line edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 7:00 PM | WPG @ TBL | WPG 2, TBL 3 | TBL 64% | WPG +180 / TBL -180 | 2.6 – 3.6 | 1–5 / 1–6 | 21% | TBL -1.5 43% | 6.2 / 6.5 (over 45%) | Stuart Skinner (expected) / Andrei Vasilevskiy (expected) | WPG +195 / TBL -238 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 7:00 PM | UTA @ PIT | UTA 4, PIT 3 | UTA 54% | UTA -120 / PIT +120 | 3.4 – 3.1 | 1–6 / 1–6 | 21% | UTA -1.5 34% | 6.6 / 6.5 (over 51%) | Karel Vejmelka (expected) / Arturs Silovs (expected) | UTA -130 / PIT +110 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 7:00 PM | CBJ @ CAR | CBJ 3, CAR 4 | CAR 68% | CBJ +210 / CAR -210 | 2.6 – 3.7 | 1–5 / 1–6 | 19% | CAR -1.5 46% | 6.3 / 6.5 (over 47%) | Jet Greaves (expected) / Pyotr Kochetkov (expected) | CBJ +190 / CAR -230 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 7:30 PM | CHI @ DET | CHI 3, DET 4 | DET 63% | CHI +170 / DET -170 | 2.7 – 3.5 | 1–5 / 1–6 | 21% | DET -1.5 41% | 6.2 / 5.5 (over 57%) | Spencer Knight (expected) / John Gibson (expected) | CHI +150 / DET -180 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 8:00 PM | BOS @ STL | BOS 2, STL 3 | STL 52% | BOS +110 / STL -110 | 3.0 – 3.1 | 1–5 / 1–5 | 23% | STL -1.5 30% | 6.1 / 5.5 (over 54%) | Jeremy Swayman (expected) / Joel Hofer (expected) | BOS -105 / STL -115 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 8:00 PM | WSH @ NSH | WSH 3, NSH 4 | NSH 52% | WSH +110 / NSH -110 | 3.1 – 3.3 | 1–6 / 1–6 | 22% | NSH -1.5 32% | 6.5 / 6.5 (over 50%) | Charlie Lindgren (expected) / Juuse Saros (expected) | WSH -112 / NSH -108 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 8:00 PM | MTL @ DAL | MTL 2, DAL 3 | DAL 59% | MTL +145 / DAL -145 | 2.7 – 3.3 | 1–5 / 1–6 | 22% | DAL -1.5 37% | 6.0 / 6.5 (over 41%) | Jakub Dobes (confirmed) / Jake Oettinger (expected) | MTL +136 / DAL -162 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 8:00 PM | NYI @ MIN | NYI 2, MIN 3 | MIN 63% | NYI +175 / MIN -175 | 2.6 – 3.4 | 1–5 / 1–6 | 22% | MIN -1.5 41% | 6.0 / 5.5 (over 52%) | Ilya Sorokin (expected) / Jesper Wallstedt (expected) | NYI +160 / MIN -192 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 10:00 PM | BUF @ ANA | BUF 4, ANA 3 | BUF 57% | BUF -130 / ANA +130 | 3.6 – 3.1 | 1–6 / 1–6 | 21% | BUF -1.5 37% | 6.7 / 6.5 (over 53%) | Ukko-Pekka Luukkonen (expected) / Lukas Dostal (expected) | BUF -130 / ANA +110 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 10:00 PM | OTT @ LAK | OTT 2, LAK 3 | LAK 50% | OTT +100 / LAK -100 | 3.0 – 3.1 | 1–5 / 1–5 | 23% | LAK -1.5 30% | 6.0 / 5.5 (over 53%) | Samuel Ersson (expected) / Darcy Kuemper (expected) | OTT -110 / LAK -110 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 10:00 PM | VAN @ SJS | VAN 3, SJS 4 | SJS 57% | VAN +130 / SJS -130 | 3.2 – 3.7 | 1–6 / 1–6 | 21% | SJS -1.5 37% | 6.9 / 6.5 (over 55%) | Leevi Meriläinen (expected) / Yaroslav Askarov (expected) | VAN +154 / SJS -185 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |

## Friday, October 30

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected goals | 80% range | Overtime | Puck line | Total: model / line | Goalies | Posted moneyline | Puck line edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 6:00 PM | NJD @ VGK | NJD 2, VGK 3 | VGK 55% | NJD +120 / VGK -120 | 2.8 – 3.1 | 1–5 / 1–5 | 24% | VGK -1.5 32% | 5.9 | Connor Hellebuyck (expected) / Carter Hart (expected) | – | no line yet (model fair VGK -1.5 +210 / NJD +1.5 -210) | no line yet | no line yet |
| 7:00 PM | WPG @ FLA | WPG 2, FLA 3 | FLA 64% | WPG +180 / FLA -180 | 2.6 – 3.5 | 1–5 / 1–6 | 21% | FLA -1.5 42% | 6.0 | Nico Daws (expected) / Akira Schmid (expected) | – | no line yet (model fair FLA -1.5 +140 / WPG +1.5 -140) | no line yet | no line yet |
| 8:00 PM | SEA @ CGY | SEA 3, CGY 4 | CGY 53% | SEA +115 / CGY -115 | 3.2 – 3.4 | 1–6 / 1–6 | 22% | CGY -1.5 33% | 6.5 | Philipp Grubauer (expected) / Dustin Wolf (expected) | – | no line yet (model fair CGY -1.5 +205 / SEA +1.5 -205) | no line yet | no line yet |

\* price not posted; assumed -110.

## Saturday, October 31

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected goals | 80% range | Overtime | Puck line | Total: model / line | Goalies | Posted moneyline | Puck line edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1:00 PM | CHI @ BOS | CHI 3, BOS 4 | BOS 69% | CHI +220 / BOS -220 | 2.6 – 3.8 | 1–5 / 1–6 | 20% | BOS -1.5 47% | 6.4 | Spencer Knight (expected) / Jeremy Swayman (expected) | – | no line yet (model fair BOS -1.5 +110 / CHI +1.5 -110) | no line yet | no line yet |
| 1:00 PM | STL @ DET | STL 3, DET 2 | STL 50% | STL -100 / DET +100 | 3.0 – 3.0 | 1–5 / 1–5 | 23% | STL -1.5 29% | 5.9 | Joel Hofer (expected) / John Gibson (expected) | – | no line yet (model fair DET +1.5 -245 / STL -1.5 +245) | no line yet | no line yet |
| 2:00 PM | TBL @ NSH | TBL 3, NSH 2 | TBL 59% | TBL -145 / NSH +145 | 3.4 – 2.8 | 1–6 / 1–5 | 22% | TBL -1.5 38% | 6.2 | Andrei Vasilevskiy (expected) / Juuse Saros (expected) | – | no line yet (model fair NSH +1.5 -165 / TBL -1.5 +165) | no line yet | no line yet |
| 2:00 PM | EDM @ NYI | EDM 3, NYI 4 | NYI 53% | EDM +115 / NYI -115 | 3.1 – 3.3 | 1–5 / 1–6 | 23% | NYI -1.5 33% | 6.4 | Tristan Jarry (expected) / Ilya Sorokin (expected) | – | no line yet (model fair NYI -1.5 +205 / EDM +1.5 -205) | no line yet | no line yet |
| 4:00 PM | BUF @ LAK | BUF 3, LAK 2 | BUF 53% | BUF -110 / LAK +110 | 3.1 – 3.0 | 1–6 / 1–5 | 22% | BUF -1.5 32% | 6.1 | Colten Ellis (expected) / Darcy Kuemper (expected) | – | no line yet (model fair LAK +1.5 -215 / BUF -1.5 +215) | no line yet | no line yet |
| 4:00 PM | OTT @ SJS | OTT 4, SJS 3 | OTT 60% | OTT -155 / SJS +155 | 3.7 – 3.0 | 1–6 / 1–5 | 21% | OTT -1.5 40% | 6.6 | Samuel Ersson (expected) / Yaroslav Askarov (expected) | – | no line yet (model fair SJS +1.5 -155 / OTT -1.5 +155) | no line yet | no line yet |
| 7:00 PM | PIT @ MTL | PIT 3, MTL 4 | MTL 54% | PIT +120 / MTL -120 | 3.1 – 3.4 | 1–5 / 1–6 | 22% | MTL -1.5 33% | 6.5 | Arturs Silovs (expected) / Jacob Fowler (expected) | – | no line yet (model fair MTL -1.5 +200 / PIT +1.5 -200) | no line yet | no line yet |
| 7:00 PM | TOR @ VAN | TOR 4, VAN 3 | TOR 64% | TOR -180 / VAN +180 | 4.0 – 3.0 | 1–7 / 1–5 | 20% | TOR -1.5 44% | 6.9 | Sergei Bobrovsky (expected) / Kevin Lankinen (expected) | – | no line yet (model fair VAN +1.5 -125 / TOR -1.5 +125) | no line yet | no line yet |
| 8:00 PM | CBJ @ DAL | CBJ 2, DAL 3 | DAL 60% | CBJ +145 / DAL -145 | 2.6 – 3.1 | 1–5 / 1–5 | 24% | DAL -1.5 36% | 5.7 | Jet Greaves (expected) / Jake Oettinger (expected) | – | no line yet (model fair DAL -1.5 +175 / CBJ +1.5 -175) | no line yet | no line yet |
| 10:00 PM | CGY @ COL | CGY 3, COL 4 | COL 65% | CGY +190 / COL -190 | 2.7 – 3.7 | 1–5 / 1–6 | 20% | COL -1.5 45% | 6.4 | Devin Cooley (expected) / Mackenzie Blackwood (expected) | – | no line yet (model fair COL -1.5 +125 / CGY +1.5 -125) | no line yet | no line yet |

\* price not posted; assumed -110.

## How the 2026-27 predictions have done

| Predictor | Games | Log loss | Brier | Winners | Goals MAE | Total MAE | 80% range hit |
|---|---|---|---|---|---|---|---|
| Final prediction | 198 | 0.6558 | 0.2318 | 60.6% | 1.40 | 1.79 | 89.1% |
| Model only (before blending) | 198 | 0.6571 | 0.2325 | 59.6% | – | – | – |
| Elo | 198 | 0.6713 | 0.2392 | 61.1% | – | – | – |
| Final prediction, games with a line | 64 | 0.6773 | 0.2420 | 54.7% | 1.41 | 1.86 | 88.3% |
| Model only, games with a line | 64 | 0.6814 | 0.2442 | 51.6% | – | – | – |
| Betting market (de-vigged moneyline) | 64 | 0.6803 | 0.2435 | 57.8% | – | 1.86 | – |

Log loss and Brier score the win chances (lower is better; a coin flip scores 0.693 and 0.250). Hockey is close to a coin flip, so differences in the third decimal matter, and only over hundreds of games. Goals MAE is the average miss on each team's goals.

Overtime: predicted in 21.6% of regular-season games, happened in 23.2%.

134 of these games were played before the predictor went live. They are backfilled walk-forward (each day predicted from earlier days only) with the actual starting goalies and no betting line. Every game since is graded on the prediction logged before puck drop.

### Betting edges

| Market | Edges | Record (W-L-P) | Staked | Units won | ROI | Expected ROI |
|---|---|---|---|---|---|---|
| Puck line | 1 | 0-1-0 | 1.3 | -1.29 | -100.0% | +11.8% |
| Moneyline | 3 | 2-1-0 | 3.5 | +1.87 | +52.8% | +5.9% |
| Total | 0 | 0-0-0 | 0.0 | +0.00 | – | – |

Moneyline moved toward the model's edge on the first line seen before puck drop: 9 of 12 games (75%).

Each edge at the stake and price logged with the last prediction before puck drop (edges logged before edges were priced from the final prediction are left out); pushes return the stake. Units are 1% of the bankroll; ROI is units won per unit staked, and expected ROI is what the edges' EVs promised. The moneyline moving toward the model's edge (closing line value) is the quickest sign that it knows something the market doesn't yet.

### Results, Tuesday, October 27

| Game | Predicted | Final | Win chance for winner | Inside 80% ranges | Goalies |
|---|---|---|---|---|---|
| CBJ @ PHI | 3–2 | 4–3 (OT) | 51% | yes | Cam Talbot / Dan Vladar |
| BOS @ CAR | 3–4 | 1–2 | 62% | yes | Jeremy Swayman / Pyotr Kochetkov |
| LAK @ CHI | 3–2 | 1–2 | 46% | yes | Anton Forsberg / Spencer Knight |
| MTL @ STL | 3–4 | 2–0 | 50% | no | Jacob Fowler / Jordan Binnington |
| NYI @ NSH | 2–3 | 4–3 (SO) | 49% | yes | Semyon Varlamov / Juuse Saros |
| NJD @ DAL | 2–3 | 5–1 | 48% | yes | Connor Hellebuyck / Casey DeSmith |
| FLA @ WPG | 3–2 | 5–1 | 54% | yes | Akira Schmid / Clay Stevenson |
| MIN @ UTA | 3–4 | 3–1 | 48% | yes | Jesper Wallstedt / Karel Vejmelka |
| OTT @ VGK | 3–4 | 1–4 | 57% | yes | Jonas Johansson / Adin Hill |
| VAN @ ANA | 3–4 | 6–5 (OT) | 34% | no | Kevin Lankinen / Lukas Dostal |
| BUF @ SJS | 4–3 | 2–0 | 60% | no | Colten Ellis / Yaroslav Askarov |

## Power ratings

Goals per game better than an average team, from the goal-rate model: offense and defense combine 5-on-5 expected goals (score and venue adjusted), special teams and actual goals, each weighted against a preseason prior. Defense is positive when it holds opponents below average. Goaltending is rated separately below.

| # | Team | Net | Offense | Defense | 5v5 xGF/60 | 5v5 xGA/60 | PP xGF/60 | PK xGA/60 | Elo |
|---|---|---|---|---|---|---|---|---|---|
| 1 | CAR | +0.68 | +0.41 | +0.27 | 3.44 | 2.42 | 8.12 | 6.77 | 1578 |
| 2 | UTA | +0.48 | +0.24 | +0.24 | 3.19 | 2.39 | 8.03 | 8.41 | 1512 |
| 3 | MIN | +0.40 | +0.16 | +0.24 | 3.10 | 2.44 | 9.28 | 8.12 | 1541 |
| 4 | VGK | +0.36 | +0.09 | +0.27 | 2.80 | 2.39 | 8.85 | 7.38 | 1534 |
| 5 | TBL | +0.35 | +0.18 | +0.17 | 2.95 | 2.53 | 7.87 | 7.87 | 1538 |
| 6 | NJD | +0.29 | +0.03 | +0.26 | 2.89 | 2.38 | 8.96 | 7.61 | 1508 |
| 7 | PIT | +0.28 | +0.22 | +0.06 | 3.11 | 2.64 | 7.98 | 7.70 | 1500 |
| 8 | DAL | +0.27 | -0.05 | +0.33 | 2.61 | 2.33 | 9.17 | 7.31 | 1530 |
| 9 | COL | +0.24 | +0.24 | -0.00 | 2.94 | 2.77 | 7.58 | 7.79 | 1544 |
| 10 | FLA | +0.23 | +0.00 | +0.23 | 2.66 | 2.45 | 9.14 | 7.43 | 1503 |
| 11 | STL | +0.09 | -0.01 | +0.10 | 2.68 | 2.61 | 6.97 | 7.39 | 1499 |
| 12 | BUF | +0.08 | +0.07 | +0.01 | 2.80 | 2.71 | 7.63 | 8.32 | 1515 |
| 13 | BOS | +0.06 | +0.08 | -0.02 | 2.85 | 2.80 | 7.74 | 8.09 | 1534 |
| 14 | EDM | +0.05 | +0.11 | -0.05 | 2.62 | 2.78 | 9.87 | 8.17 | 1518 |
| 15 | NYR | +0.03 | +0.02 | +0.01 | 2.74 | 2.74 | 8.57 | 7.73 | 1493 |
| 16 | OTT | +0.02 | -0.07 | +0.08 | 2.62 | 2.63 | 7.93 | 8.04 | 1517 |
| 17 | WSH | +0.01 | +0.09 | -0.08 | 2.89 | 2.84 | 7.78 | 8.15 | 1516 |
| 18 | LAK | -0.00 | -0.13 | +0.13 | 2.58 | 2.60 | 7.88 | 8.11 | 1471 |
| 19 | DET | -0.01 | -0.11 | +0.10 | 2.64 | 2.58 | 8.45 | 8.62 | 1481 |
| 20 | MTL | -0.10 | +0.04 | -0.14 | 2.87 | 2.92 | 7.11 | 8.30 | 1526 |
| 21 | WPG | -0.10 | -0.10 | -0.01 | 2.64 | 2.77 | 8.01 | 8.26 | 1472 |
| 22 | NYI | -0.13 | -0.06 | -0.07 | 2.73 | 2.85 | 7.57 | 8.69 | 1493 |
| 23 | TOR | -0.13 | +0.01 | -0.14 | 2.57 | 2.91 | 8.69 | 8.21 | 1485 |
| 24 | CBJ | -0.15 | -0.08 | -0.07 | 2.64 | 2.80 | 7.60 | 8.39 | 1493 |
| 25 | NSH | -0.15 | -0.08 | -0.07 | 2.63 | 2.82 | 7.86 | 7.57 | 1481 |
| 26 | CGY | -0.21 | -0.08 | -0.13 | 2.68 | 2.89 | 7.33 | 8.21 | 1467 |
| 27 | PHI | -0.28 | -0.26 | -0.02 | 2.39 | 2.75 | 7.77 | 7.59 | 1475 |
| 28 | SEA | -0.31 | -0.09 | -0.22 | 2.51 | 3.00 | 7.33 | 8.47 | 1482 |
| 29 | ANA | -0.34 | -0.02 | -0.32 | 2.79 | 3.08 | 7.82 | 8.41 | 1476 |
| 30 | CHI | -0.69 | -0.29 | -0.41 | 2.33 | 3.17 | 7.17 | 8.38 | 1436 |
| 31 | SJS | -0.72 | -0.20 | -0.51 | 2.42 | 3.29 | 7.31 | 8.82 | 1465 |
| 32 | VAN | -0.76 | -0.22 | -0.54 | 2.31 | 3.31 | 7.65 | 8.74 | 1417 |

## Goalies

Each team's likeliest next starter. GSAx is goals saved above expected (from this predictor's own shot model), shrunk hard toward a slightly below-average prior, since goaltending repeats poorly from season to season.

| Team | Likely next starter | Share of recent starts | GSAx per 100 shots | Goals per game vs average |
|---|---|---|---|---|
| WSH | Logan Thompson | 68% | +0.45 | +0.19 |
| NYI | Ilya Sorokin | 62% | +0.42 | +0.17 |
| BOS | Jeremy Swayman | 76% | +0.33 | +0.14 |
| MTL | Jacob Fowler | 65% | +0.31 | +0.13 |
| CGY | Devin Cooley | 62% | +0.21 | +0.09 |
| MIN | Jesper Wallstedt | 84% | +0.18 | +0.08 |
| TBL | Andrei Vasilevskiy | 69% | +0.18 | +0.07 |
| DAL | Jake Oettinger | 74% | +0.14 | +0.06 |
| OTT | Linus Ullmark | 55% | +0.13 | +0.06 |
| COL | Mackenzie Blackwood | 62% | +0.12 | +0.05 |
| CHI | Spencer Knight | 88% | +0.10 | +0.04 |
| WPG | Stuart Skinner | 66% | +0.02 | +0.01 |
| STL | Joel Hofer | 66% | +0.00 | +0.00 |
| CAR | Pyotr Kochetkov | 62% | -0.03 | -0.01 |
| NJD | Jake Allen | 60% | -0.07 | -0.03 |
| PHI | Joseph Woll | 71% | -0.07 | -0.03 |
| NYR | Dylan Garand | 63% | -0.07 | -0.03 |
| EDM | Devon Levi | 55% | -0.08 | -0.03 |
| SEA | Philipp Grubauer | 52% | -0.09 | -0.04 |
| TOR | Sergei Bobrovsky | 65% | -0.13 | -0.05 |
| DET | John Gibson | 63% | -0.14 | -0.06 |
| LAK | Darcy Kuemper | 60% | -0.16 | -0.07 |
| UTA | Karel Vejmelka | 80% | -0.16 | -0.07 |
| BUF | Ukko-Pekka Luukkonen | 66% | -0.18 | -0.07 |
| SJS | Yaroslav Askarov | 59% | -0.18 | -0.07 |
| ANA | Lukas Dostal | 73% | -0.18 | -0.08 |
| FLA | Akira Schmid | 52% | -0.19 | -0.08 |
| VGK | Carter Hart | 54% | -0.19 | -0.08 |
| NSH | Juuse Saros | 71% | -0.23 | -0.10 |
| CBJ | Cam Talbot | 57% | -0.25 | -0.11 |
| VAN | Leevi Meriläinen | 56% | -0.29 | -0.12 |
| PIT | Arturs Silovs | 69% | -0.30 | -0.13 |

## Current model fit

- Fitted on 5790 games from 2022-23 to 2026-27.
- Home ice: +3.1% goals for the home team relative to the visitor.
- Second night of a back-to-back: -5.7% goals scored, +3.2% goals allowed.
- Starting goalie: each goal per game he saves above average lowers the opponent's rate by 23%.
- Blend: 37% on the betting line wherever there is one (fitted on 64 logged games, shrunk toward the backtest value).
- Simulator: 22.3% of recent regular-season games reached overtime; trailing teams usually have the goalie pulled with 2 minutes left when down one and 3 when down two; empty-net goals come at 0.40 a minute with the net empty; three-on-three overtime produces 1.03 goals per five minutes.
