# NHL score predictions

Updated Sat Nov 28, 2026 03:30 AM ET. Refreshed automatically several times a day during the season; each game's prediction is locked at puck drop and graded once the final score is in.

Each game is simulated 10,000 times minute by minute, with pulled goalies, empty-net goals, overtime and shootouts. The predicted score is the most common final score in which the likelier winner wins; as in the official result, a shootout winner gets one extra goal. Hockey is low-scoring and luck-heavy, so read the win chance and the ranges (80% of simulated outcomes for each team) before the single score.

Goalies marked with a percentage are projected from recent starts (the share is the chance he starts); "probable" or "confirmed" ones come from ESPN and replace the projection when available.

The fair moneyline is the American odds that match the win chance exactly, with no bookmaker margin: -150 means risk $150 to win $100, +150 means risk $100 to win $150. A sportsbook's price is a little worse on both sides because of its cut, so a book only offers value on a team when its price beats the fair line. The puck line is the favorite's chance to win by two or more.

The edge columns price each side of the puck line, moneyline and total with the final prediction: the model's goal rates blended with the market's, simulated against the posted lines, overtime and shootout included (the shootout winner gets one goal), and anchored to the market's own chances so only what the blend moves off the market counts. Each cell shows the side with the best expected value (EV) per $1 bet at the posted price. A side is an edge only if its EV is at least 3%: a pick shows its price, EV, its chance of winning the bet and its stake, a 25% share of the Kelly stake in units of 1% of the bankroll, with at most 3 units on one game; "no edge" means neither side clears the bar. A projected starting goalie is wrong about a third of the time and the market prices the real one, so edges wait until both starters are confirmed. A total with no posted price is assumed to be -110 (marked \*); the puck line and moneyline are never assumed, so without a price the cell shows the model's fair odds instead. Treat the edges as an experiment, not betting advice; see the backtest for how they have done on past seasons. Their record is tracked live below.

## Saturday, November 28

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected goals | 80% range | Overtime | Puck line | Total: model / line | Goalies | Posted moneyline | Puck line edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 4:00 PM | MTL @ VGK | MTL 3, VGK 4 | VGK 52% | MTL +110 / VGK -110 | 3.1 – 3.3 | 1–6 / 1–6 | 21% | VGK -1.5 32% | 6.4 / 6.5 (over 48%) | Jakub Dobes (confirmed) / Adin Hill (expected) | MTL +102 / VGK -122 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 6:00 PM | TBL @ FLA | TBL 3, FLA 2 | TBL 53% | TBL -110 / FLA +110 | 3.1 – 3.0 | 1–5 / 1–5 | 23% | TBL -1.5 32% | 6.1 / 6.5 (over 43%) | Andrei Vasilevskiy (expected) / Akira Schmid (expected) | TBL -105 / FLA -115 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 7:00 PM | NSH @ DET | NSH 2, DET 3 | DET 50% | NSH +100 / DET -100 | 3.1 – 3.1 | 1–5 / 1–5 | 22% | DET -1.5 29% | 6.2 / 5.5 (over 56%) | Justus Annunen (expected) / Daniil Tarasov (expected) | NSH -108 / DET -112 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 7:00 PM | WPG @ NJD | WPG 2, NJD 3 | NJD 63% | WPG +175 / NJD -175 | 2.7 – 3.5 | 1–5 / 1–6 | 20% | NJD -1.5 42% | 6.2 / 6.5 (over 45%) | Nico Daws (expected) / Connor Hellebuyck (confirmed) | WPG +170 / NJD -205 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 7:00 PM | CGY @ NYR | CGY 2, NYR 3 | NYR 61% | CGY +155 / NYR -155 | 2.8 – 3.4 | 1–5 / 1–6 | 23% | NYR -1.5 39% | 6.2 / 5.5 (over 56%) | Dustin Wolf (expected) / Joonas Korpisalo (expected) | CGY +154 / NYR -185 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 7:00 PM | TOR @ PIT | TOR 3, PIT 4 | PIT 54% | TOR +120 / PIT -120 | 3.2 – 3.5 | 1–6 / 1–6 | 22% | PIT -1.5 34% | 6.6 / 6.5 (over 52%) | Sergei Bobrovsky (confirmed) / Arturs Silovs (expected) | TOR -102 / PIT -118 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 7:00 PM | OTT @ CAR | OTT 3, CAR 4 | CAR 68% | OTT +215 / CAR -215 | 2.5 – 3.7 | 1–5 / 1–6 | 21% | CAR -1.5 46% | 6.2 / 6.5 (over 45%) | Samuel Ersson (expected) / Pyotr Kochetkov (expected) | OTT +215 / CAR -265 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 7:00 PM | WSH @ STL | WSH 4, STL 3 | WSH 50% | WSH -100 / STL +100 | 3.4 – 3.4 | 1–6 / 1–6 | 20% | WSH -1.5 31% | 6.8 / 6.5 (over 55%) | Charlie Lindgren (expected) / Jordan Binnington (expected) | WSH -108 / STL -112 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 7:30 PM | NYI @ PHI | NYI 3, PHI 2 | NYI 55% | NYI -120 / PHI +120 | 3.1 – 2.9 | 1–6 / 1–5 | 22% | NYI -1.5 33% | 6.0 / 5.5 (over 52%) | Ilya Sorokin (confirmed) / Joseph Woll (expected) | NYI -118 / PHI -102 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 8:00 PM | UTA @ DAL | UTA 2, DAL 3 | DAL 56% | UTA +130 / DAL -130 | 2.9 – 3.2 | 1–5 / 1–6 | 22% | DAL -1.5 34% | 6.1 / 5.5 (over 54%) | Sebastian Cossa (expected) / Jake Oettinger (expected) | UTA +130 / DAL -155 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 9:00 PM | SJS @ COL | SJS 3, COL 4 | COL 70% | SJS +235 / COL -235 | 2.6 – 4.0 | 1–5 / 1–7 | 19% | COL -1.5 49% | 6.6 / 6.5 (over 51%) | Alex Nedeljkovic (expected) / Scott Wedgewood (expected) | SJS +210 / COL -258 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 9:00 PM | ANA @ LAK | ANA 3, LAK 4 | LAK 57% | ANA +135 / LAK -135 | 2.9 – 3.4 | 1–5 / 1–6 | 22% | LAK -1.5 36% | 6.3 / 6.5 (over 48%) | Lukas Dostal (confirmed) / Anton Forsberg (expected) | ANA +120 / LAK -142 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 10:00 PM | EDM @ SEA | EDM 4, SEA 3 | EDM 58% | EDM -140 / SEA +140 | 3.5 – 2.9 | 1–6 / 1–5 | 21% | EDM -1.5 37% | 6.4 / 6.5 (over 48%) | Devon Levi (expected) / Joey Daccord (expected) | EDM -170 / SEA +142 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |

## Sunday, November 29

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected goals | 80% range | Overtime | Puck line | Total: model / line | Goalies | Posted moneyline | Puck line edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2:00 PM | MIN @ CHI | MIN 3, CHI 2 | MIN 70% | MIN -240 / CHI +240 | 3.7 – 2.3 | 1–6 / 0–4 | 20% | MIN -1.5 49% | 6.0 | Jesper Wallstedt (expected) / Spencer Knight (expected) | – | no line yet (model fair CHI +1.5 -105 / MIN -1.5 +105) | no line yet | no line yet |
| 5:00 PM | VAN @ BOS | VAN 3, BOS 4 | BOS 75% | VAN +295 / BOS -295 | 2.5 – 4.3 | 1–5 / 2–7 | 17% | BOS -1.5 55% | 6.8 | Leevi Meriläinen (expected) / Jeremy Swayman (expected) | – | no line yet (model fair BOS -1.5 -125 / VAN +1.5 +125) | no line yet | no line yet |

\* price not posted; assumed -110.

## Monday, November 30

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected goals | 80% range | Overtime | Puck line | Total: model / line | Goalies | Posted moneyline | Puck line edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1:00 PM | OTT @ NSH | OTT 3, NSH 2 | OTT 56% | OTT -125 / NSH +125 | 3.3 – 2.9 | 1–6 / 1–5 | 22% | OTT -1.5 34% | 6.2 | Linus Ullmark (expected) / Juuse Saros (expected) | – | no line yet (model fair NSH +1.5 -190 / OTT -1.5 +190) | no line yet | no line yet |
| 7:00 PM | CAR @ NYR | CAR 4, NYR 3 | CAR 64% | CAR -175 / NYR +175 | 3.7 – 2.7 | 1–6 / 1–5 | 21% | CAR -1.5 43% | 6.4 | Pyotr Kochetkov (expected) / Dylan Garand (expected) | – | no line yet (model fair NYR +1.5 -135 / CAR -1.5 +135) | no line yet | no line yet |
| 7:00 PM | CBJ @ PIT | CBJ 3, PIT 4 | PIT 57% | CBJ +130 / PIT -130 | 3.1 – 3.5 | 1–5 / 1–6 | 21% | PIT -1.5 36% | 6.6 | Cam Talbot (expected) / Arturs Silovs (expected) | – | no line yet (model fair PIT -1.5 +175 / CBJ +1.5 -175) | no line yet | no line yet |
| 7:30 PM | PHI @ TOR | PHI 2, TOR 3 | TOR 55% | PHI +120 / TOR -120 | 2.8 – 3.1 | 1–5 / 1–5 | 24% | TOR -1.5 32% | 5.9 | Dan Vladar (expected) / Anthony Stolarz (expected) | – | no line yet (model fair TOR -1.5 +210 / PHI +1.5 -210) | no line yet | no line yet |
| 7:30 PM | CHI @ WPG | CHI 2, WPG 3 | WPG 72% | CHI +255 / WPG -255 | 2.4 – 3.8 | 0–5 / 1–6 | 20% | WPG -1.5 50% | 6.2 | Drew Commesso (expected) / Stuart Skinner (expected) | – | no line yet (model fair WPG -1.5 -100 / CHI +1.5 +100) | no line yet | no line yet |
| 9:30 PM | MTL @ UTA | MTL 3, UTA 4 | UTA 59% | MTL +145 / UTA -145 | 2.9 – 3.5 | 1–5 / 1–6 | 21% | UTA -1.5 38% | 6.5 | Jacob Fowler (expected) / Karel Vejmelka (expected) | – | no line yet (model fair UTA -1.5 +165 / MTL +1.5 -165) | no line yet | no line yet |

\* price not posted; assumed -110.

## How the 2026-27 predictions have done

| Predictor | Games | Log loss | Brier | Winners | Goals MAE | Total MAE | 80% range hit |
|---|---|---|---|---|---|---|---|
| Final prediction | 414 | 0.6642 | 0.2359 | 60.9% | 1.38 | 1.83 | 89.6% |
| Model only (before blending) | 414 | 0.6666 | 0.2371 | 58.9% | – | – | – |
| Elo | 414 | 0.6772 | 0.2421 | 57.2% | – | – | – |
| Final prediction, games with a line | 280 | 0.6721 | 0.2396 | 58.9% | 1.38 | 1.87 | 89.6% |
| Model only, games with a line | 280 | 0.6757 | 0.2414 | 56.1% | – | – | – |
| Betting market (de-vigged moneyline) | 280 | 0.6701 | 0.2387 | 59.6% | – | 1.86 | – |

Log loss and Brier score the win chances (lower is better; a coin flip scores 0.693 and 0.250). Hockey is close to a coin flip, so differences in the third decimal matter, and only over hundreds of games. Goals MAE is the average miss on each team's goals.

Overtime: predicted in 21.5% of regular-season games, happened in 21.3%.

134 of these games were played before the predictor went live. They are backfilled walk-forward (each day predicted from earlier days only) with the actual starting goalies and no betting line. Every game since is graded on the prediction logged before puck drop.

### Betting edges

| Market | Edges | Record (W-L-P) | Staked | Units won | ROI | Expected ROI |
|---|---|---|---|---|---|---|
| Puck line | 6 | 1-5-0 | 5.9 | -4.30 | -72.3% | +7.5% |
| Moneyline | 14 | 8-6-0 | 15.6 | +4.52 | +29.0% | +5.4% |
| Total | 2 | 1-1-0 | 1.7 | +0.04 | +2.4% | +3.4% |

Moneyline moved toward the model's edge on the first line seen before puck drop: 43 of 62 games (69%).

Each edge at the stake and price logged with the last prediction before puck drop (edges logged before edges were priced from the final prediction are left out); pushes return the stake. Units are 1% of the bankroll; ROI is units won per unit staked, and expected ROI is what the edges' EVs promised. The moneyline moving toward the model's edge (closing line value) is the quickest sign that it knows something the market doesn't yet.

### Results, Friday, November 27

| Game | Predicted | Final | Win chance for winner | Inside 80% ranges | Goalies |
|---|---|---|---|---|---|
| TOR @ BOS | 3–4 | 3–1 | 41% | yes | Anthony Stolarz / Jeremy Swayman |
| CGY @ NJD | 3–4 | 3–5 | 67% | yes | Dustin Wolf / Connor Hellebuyck |
| UTA @ NSH | 4–3 | 6–5 (SO) | 52% | yes | Karel Vejmelka / Juuse Saros |
| DAL @ STL | 3–2 | 3–5 | 45% | yes | Jake Oettinger / Joel Hofer |
| OTT @ TBL | 2–3 | 6–2 | 43% | no | Linus Ullmark / Andrei Vasilevskiy |
| VAN @ PHI | 3–4 | 2–5 | 67% | yes | Leevi Meriläinen / Dan Vladar |
| FLA @ WSH | 3–4 | 3–2 | 48% | yes | Jacob Markstrom / Logan Thompson |
| DET @ CBJ | 2–3 | 2–0 | 46% | no | Daniil Tarasov / Jet Greaves |
| COL @ MIN | 3–4 | 4–3 (SO) | 47% | yes | Mackenzie Blackwood / Jesper Wallstedt |
| LAK @ ANA | 4–3 | 5–3 | 50% | yes | Darcy Kuemper / Laurent Brossoit |
| VGK @ SJS | 4–3 | 1–4 | 34% | yes | Carter Hart / Yaroslav Askarov |
| NYR @ CHI | 4–3 | 1–2 | 38% | yes | Dylan Garand / Spencer Knight |
| WPG @ NYI | 3–4 | 3–1 | 47% | yes | Stuart Skinner / Semyon Varlamov |
| PIT @ BUF | 3–4 | 6–3 | 46% | yes | Sergei Murashov / Ukko-Pekka Luukkonen |
| SEA @ EDM | 3–4 | 4–2 | 36% | yes | Philipp Grubauer / Tristan Jarry |

## Power ratings

Goals per game better than an average team, from the goal-rate model: offense and defense combine 5-on-5 expected goals (score and venue adjusted), special teams and actual goals, each weighted against a preseason prior. Defense is positive when it holds opponents below average. Goaltending is rated separately below.

| # | Team | Net | Offense | Defense | 5v5 xGF/60 | 5v5 xGA/60 | PP xGF/60 | PK xGA/60 | Elo |
|---|---|---|---|---|---|---|---|---|---|
| 1 | CAR | +0.80 | +0.49 | +0.32 | 3.39 | 2.30 | 8.40 | 6.99 | 1602 |
| 2 | TBL | +0.43 | +0.21 | +0.22 | 2.94 | 2.38 | 7.86 | 7.83 | 1537 |
| 3 | UTA | +0.41 | +0.24 | +0.17 | 3.11 | 2.39 | 8.13 | 8.47 | 1503 |
| 4 | MIN | +0.30 | +0.07 | +0.24 | 2.71 | 2.40 | 8.62 | 7.75 | 1565 |
| 5 | OTT | +0.28 | +0.07 | +0.22 | 2.80 | 2.38 | 7.76 | 8.09 | 1534 |
| 6 | COL | +0.27 | +0.23 | +0.05 | 2.85 | 2.66 | 7.81 | 7.94 | 1565 |
| 7 | NJD | +0.22 | +0.08 | +0.14 | 2.80 | 2.44 | 9.03 | 7.63 | 1530 |
| 8 | VGK | +0.22 | +0.05 | +0.16 | 2.65 | 2.47 | 9.40 | 7.19 | 1522 |
| 9 | PIT | +0.17 | +0.14 | +0.03 | 2.92 | 2.57 | 7.65 | 7.98 | 1474 |
| 10 | WSH | +0.15 | +0.19 | -0.05 | 2.98 | 2.69 | 8.02 | 7.98 | 1497 |
| 11 | DAL | +0.15 | -0.10 | +0.24 | 2.50 | 2.38 | 9.42 | 7.21 | 1525 |
| 12 | FLA | +0.14 | -0.02 | +0.16 | 2.54 | 2.47 | 9.41 | 7.55 | 1514 |
| 13 | STL | +0.09 | +0.07 | +0.02 | 2.73 | 2.65 | 7.28 | 8.13 | 1516 |
| 14 | BUF | +0.07 | +0.10 | -0.03 | 2.73 | 2.66 | 8.05 | 8.31 | 1510 |
| 15 | BOS | +0.07 | +0.05 | +0.03 | 2.73 | 2.66 | 7.51 | 8.08 | 1520 |
| 16 | EDM | +0.05 | +0.02 | +0.03 | 2.42 | 2.61 | 9.39 | 8.17 | 1527 |
| 17 | NYR | +0.04 | -0.02 | +0.06 | 2.65 | 2.62 | 8.61 | 7.58 | 1494 |
| 18 | LAK | +0.02 | -0.17 | +0.18 | 2.41 | 2.44 | 8.12 | 7.88 | 1473 |
| 19 | MTL | -0.04 | +0.03 | -0.07 | 2.80 | 2.76 | 7.48 | 8.33 | 1523 |
| 20 | NSH | -0.07 | +0.02 | -0.09 | 2.76 | 2.78 | 7.86 | 7.58 | 1505 |
| 21 | TOR | -0.09 | -0.07 | -0.02 | 2.43 | 2.65 | 8.63 | 8.28 | 1461 |
| 22 | WPG | -0.10 | -0.08 | -0.02 | 2.51 | 2.70 | 8.47 | 8.96 | 1500 |
| 23 | NYI | -0.14 | -0.04 | -0.10 | 2.69 | 2.83 | 7.02 | 8.69 | 1491 |
| 24 | CBJ | -0.15 | -0.09 | -0.07 | 2.61 | 2.72 | 7.62 | 8.40 | 1472 |
| 25 | DET | -0.16 | -0.10 | -0.06 | 2.60 | 2.73 | 8.46 | 8.44 | 1480 |
| 26 | PHI | -0.20 | -0.21 | +0.01 | 2.34 | 2.62 | 7.86 | 7.53 | 1476 |
| 27 | CGY | -0.29 | -0.10 | -0.19 | 2.60 | 2.90 | 6.96 | 7.72 | 1456 |
| 28 | ANA | -0.32 | +0.01 | -0.33 | 2.66 | 3.00 | 7.71 | 8.05 | 1478 |
| 29 | SEA | -0.34 | -0.17 | -0.18 | 2.33 | 2.86 | 7.22 | 8.44 | 1475 |
| 30 | CHI | -0.60 | -0.28 | -0.32 | 2.23 | 2.99 | 7.11 | 8.29 | 1437 |
| 31 | SJS | -0.62 | -0.20 | -0.42 | 2.41 | 3.09 | 7.28 | 9.52 | 1448 |
| 32 | VAN | -0.84 | -0.27 | -0.57 | 2.20 | 3.25 | 7.57 | 8.73 | 1391 |

## Goalies

Each team's likeliest next starter. GSAx is goals saved above expected (from this predictor's own shot model), shrunk hard toward a slightly below-average prior, since goaltending repeats poorly from season to season.

| Team | Likely next starter | Share of recent starts | GSAx per 100 shots | Goals per game vs average |
|---|---|---|---|---|
| NYI | Ilya Sorokin | 83% | +0.43 | +0.18 |
| COL | Mackenzie Blackwood | 51% | +0.28 | +0.12 |
| MIN | Jesper Wallstedt | 85% | +0.26 | +0.11 |
| BOS | Jeremy Swayman | 79% | +0.26 | +0.11 |
| WSH | Logan Thompson | 54% | +0.26 | +0.11 |
| MTL | Jacob Fowler | 65% | +0.24 | +0.10 |
| STL | Joel Hofer | 53% | +0.21 | +0.09 |
| TBL | Andrei Vasilevskiy | 84% | +0.18 | +0.07 |
| DAL | Jake Oettinger | 88% | +0.17 | +0.07 |
| CHI | Spencer Knight | 82% | +0.12 | +0.05 |
| DET | Daniil Tarasov | 63% | +0.11 | +0.05 |
| NJD | Connor Hellebuyck | 74% | +0.10 | +0.04 |
| WPG | Stuart Skinner | 48% | +0.06 | +0.03 |
| CAR | Pyotr Kochetkov | 59% | -0.01 | -0.00 |
| EDM | Devon Levi | 68% | -0.04 | -0.02 |
| SJS | Alex Nedeljkovic | 61% | -0.08 | -0.03 |
| NYR | Joonas Korpisalo | 50% | -0.08 | -0.03 |
| NSH | Juuse Saros | 52% | -0.08 | -0.03 |
| LAK | Anton Forsberg | 57% | -0.09 | -0.04 |
| PHI | Joseph Woll | 72% | -0.14 | -0.06 |
| BUF | Ukko-Pekka Luukkonen | 57% | -0.14 | -0.06 |
| FLA | Akira Schmid | 55% | -0.16 | -0.07 |
| CBJ | Cam Talbot | 60% | -0.17 | -0.07 |
| SEA | Joey Daccord | 70% | -0.17 | -0.07 |
| TOR | Sergei Bobrovsky | 64% | -0.24 | -0.10 |
| CGY | Dustin Wolf | 73% | -0.24 | -0.10 |
| UTA | Sebastian Cossa | 65% | -0.26 | -0.11 |
| VGK | Adin Hill | 66% | -0.29 | -0.12 |
| ANA | Lukas Dostal | 49% | -0.29 | -0.12 |
| PIT | Arturs Silovs | 77% | -0.38 | -0.16 |
| VAN | Leevi Meriläinen | 73% | -0.39 | -0.17 |
| OTT | Samuel Ersson | 45% | -0.59 | -0.25 |

## Current model fit

- Fitted on 6006 games from 2022-23 to 2026-27.
- Home ice: +2.9% goals for the home team relative to the visitor.
- Second night of a back-to-back: -5.8% goals scored, +3.0% goals allowed.
- Starting goalie: each goal per game he saves above average lowers the opponent's rate by 21%.
- Blend: 57% on the betting line wherever there is one (fitted on 280 logged games, shrunk toward the backtest value).
- Simulator: 22.2% of recent regular-season games reached overtime; trailing teams usually have the goalie pulled with 2 minutes left when down one and 3 when down two; empty-net goals come at 0.40 a minute with the net empty; three-on-three overtime produces 1.02 goals per five minutes.
