# NHL score predictions

Updated Thu Nov 12, 2026 03:59 PM ET. Refreshed automatically several times a day during the season; each game's prediction is locked at puck drop and graded once the final score is in.

Each game is simulated 10,000 times minute by minute, with pulled goalies, empty-net goals, overtime and shootouts. The predicted score is the most common final score in which the likelier winner wins; as in the official result, a shootout winner gets one extra goal. Hockey is low-scoring and luck-heavy, so read the win chance and the ranges (80% of simulated outcomes for each team) before the single score.

Goalies marked with a percentage are projected from recent starts (the share is the chance he starts); "probable" or "confirmed" ones come from ESPN and replace the projection when available.

The fair moneyline is the American odds that match the win chance exactly, with no bookmaker margin: -150 means risk $150 to win $100, +150 means risk $100 to win $150. A sportsbook's price is a little worse on both sides because of its cut, so a book only offers value on a team when its price beats the fair line. The puck line is the favorite's chance to win by two or more.

The edge columns price each side of the puck line, moneyline and total with the final prediction: the model's goal rates blended with the market's, simulated against the posted lines, overtime and shootout included (the shootout winner gets one goal), and anchored to the market's own chances so only what the blend moves off the market counts. Each cell shows the side with the best expected value (EV) per $1 bet at the posted price. A side is an edge only if its EV is at least 3%: a pick shows its price, EV, its chance of winning the bet and its stake, a 25% share of the Kelly stake in units of 1% of the bankroll, with at most 3 units on one game; "no edge" means neither side clears the bar. A projected starting goalie is wrong about a third of the time and the market prices the real one, so edges wait until both starters are confirmed. A total with no posted price is assumed to be -110 (marked \*); the puck line and moneyline are never assumed, so without a price the cell shows the model's fair odds instead. Treat the edges as an experiment, not betting advice; see the backtest for how they have done on past seasons. Their record is tracked live below.

## Thursday, November 12

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected goals | 80% range | Overtime | Puck line | Total: model / line | Goalies | Posted moneyline | Puck line edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 7:00 PM | MTL @ BOS | MTL 2, BOS 3 | BOS 54% | MTL +120 / BOS -120 | 3.0 – 3.2 | 1–5 / 1–6 | 22% | BOS -1.5 33% | 6.2 / 6.5 (over 45%) | Jacob Fowler (confirmed) / Jeremy Swayman (confirmed) | MTL +105 / BOS -125 | no edge | no edge | no edge |
| 7:00 PM | MIN @ TOR | MIN 4, TOR 3 | MIN 59% | MIN -145 / TOR +145 | 3.4 – 2.8 | 1–6 / 1–5 | 21% | MIN -1.5 38% | 6.2 / 6.5 (over 45%) | Jesper Wallstedt (confirmed) / Anthony Stolarz (confirmed) | MIN -170 / TOR +142 | no edge | no edge | no edge |
| 7:00 PM | COL @ OTT | COL 3, OTT 4 | OTT 50% | COL +100 / OTT -100 | 3.2 – 3.2 | 1–6 / 1–6 | 22% | OTT -1.5 30% | 6.4 / 6.5 (over 47%) | Scott Wedgewood (confirmed) / Linus Ullmark (confirmed) | COL -108 / OTT -112 | no edge | no edge | no edge |
| 7:00 PM | WSH @ NJD | WSH 2, NJD 3 | NJD 55% | WSH +125 / NJD -125 | 2.9 – 3.3 | 1–5 / 1–6 | 22% | NJD -1.5 34% | 6.2 / 6.5 (over 45%) | Logan Thompson (expected) / Connor Hellebuyck (confirmed) | WSH +136 / NJD -162 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 7:00 PM | TBL @ CBJ | TBL 4, CBJ 3 | TBL 51% | TBL -105 / CBJ +105 | 3.2 – 3.1 | 1–6 / 1–5 | 22% | TBL -1.5 30% | 6.3 / 6.5 (over 47%) | Dennis Hildeby (expected) / Jet Greaves (confirmed) | TBL -115 / CBJ -105 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 7:30 PM | DET @ FLA | DET 2, FLA 3 | FLA 58% | DET +140 / FLA -140 | 2.8 – 3.3 | 1–5 / 1–6 | 22% | FLA -1.5 37% | 6.1 / 5.5 (over 53%) | John Gibson (confirmed) / Akira Schmid (confirmed) | DET +142 / FLA -170 | no edge | no edge | no edge |
| 8:00 PM | BUF @ CHI | BUF 4, CHI 3 | BUF 60% | BUF -145 / CHI +145 | 3.6 – 2.9 | 1–6 / 1–5 | 21% | BUF -1.5 39% | 6.5 / 6.5 (over 50%) | Colten Ellis (expected) / Spencer Knight (expected) | BUF -155 / CHI +130 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 8:00 PM | WPG @ DAL | WPG 2, DAL 3 | DAL 61% | WPG +160 / DAL -160 | 2.6 – 3.3 | 1–5 / 1–6 | 23% | DAL -1.5 38% | 5.9 / 5.5 (over 51%) | Stuart Skinner (confirmed) / Jake Oettinger (confirmed) | WPG +145 / DAL -175 | no edge | no edge | no edge |
| 9:00 PM | STL @ UTA | STL 3, UTA 2 | STL 53% | STL -115 / UTA +115 | 3.2 – 3.0 | 1–6 / 1–5 | 23% | STL -1.5 32% | 6.2 / 5.5 (over 55%) | Joel Hofer (confirmed) / Karel Vejmelka (expected) | STL -130 / UTA +110 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 10:00 PM | NYI @ LAK | NYI 2, LAK 3 | LAK 52% | NYI +105 / LAK -105 | 3.0 – 3.1 | 1–5 / 1–5 | 22% | LAK -1.5 31% | 6.2 / 5.5 (over 55%) | Ilya Sorokin (expected) / Darcy Kuemper (confirmed) | NYI +105 / LAK -125 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |

## Friday, November 13

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected goals | 80% range | Overtime | Puck line | Total: model / line | Goalies | Posted moneyline | Puck line edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 9:00 PM | NYR @ VAN | NYR 4, VAN 3 | NYR 67% | NYR -200 / VAN +200 | 3.8 – 2.7 | 1–6 / 1–5 | 20% | NYR -1.5 45% | 6.5 / 6.5 (over 49%) | Dylan Garand (expected) / Leevi Meriläinen (expected) | NYR -225 / VAN +185 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 10:00 PM | NSH @ VGK | NSH 2, VGK 3 | VGK 62% | NSH +160 / VGK -160 | 2.7 – 3.4 | 1–5 / 1–6 | 22% | VGK -1.5 40% | 6.2 / 5.5 (over 56%) | Juuse Saros (expected) / Adin Hill (expected) | NSH +160 / VGK -192 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |

## Saturday, November 14

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected goals | 80% range | Overtime | Puck line | Total: model / line | Goalies | Posted moneyline | Puck line edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1:00 PM | SEA @ CAR | SEA 3, CAR 4 | CAR 74% | SEA +290 / CAR -290 | 2.5 – 4.2 | 1–5 / 2–7 | 18% | CAR -1.5 54% | 6.7 | Joey Daccord (expected) / Pyotr Kochetkov (expected) | – | no line yet (model fair CAR -1.5 -120 / SEA +1.5 +120) | no line yet | no line yet |
| 3:30 PM | WPG @ CHI | WPG 3, CHI 2 | WPG 61% | WPG -160 / CHI +160 | 3.4 – 2.7 | 1–6 / 1–5 | 21% | WPG -1.5 39% | 6.2 | Stuart Skinner (expected) / Spencer Knight (expected) | – | no line yet (model fair CHI +1.5 -155 / WPG -1.5 +155) | no line yet | no line yet |
| 7:00 PM | MIN @ BOS | MIN 3, BOS 2 | MIN 52% | MIN -105 / BOS +105 | 3.1 – 3.0 | 1–5 / 1–5 | 23% | MIN -1.5 31% | 6.1 | Jesper Wallstedt (expected) / Jeremy Swayman (expected) | – | no line yet (model fair BOS +1.5 -225 / MIN -1.5 +225) | no line yet | no line yet |
| 7:00 PM | EDM @ TOR | EDM 4, TOR 3 | EDM 56% | EDM -125 / TOR +125 | 3.4 – 3.0 | 1–6 / 1–5 | 22% | EDM -1.5 35% | 6.4 | Devon Levi (expected) / Sergei Bobrovsky (expected) | – | no line yet (model fair TOR +1.5 -185 / EDM -1.5 +185) | no line yet | no line yet |
| 7:00 PM | COL @ MTL | COL 4, MTL 3 | COL 53% | COL -115 / MTL +115 | 3.3 – 3.2 | 1–6 / 1–6 | 21% | COL -1.5 32% | 6.5 | Mackenzie Blackwood (expected) / Jacob Fowler (expected) | – | no line yet (model fair MTL +1.5 -215 / COL -1.5 +215) | no line yet | no line yet |
| 7:00 PM | DET @ TBL | DET 2, TBL 3 | TBL 66% | DET +190 / TBL -190 | 2.6 – 3.6 | 1–5 / 1–6 | 20% | TBL -1.5 44% | 6.1 | John Gibson (expected) / Andrei Vasilevskiy (expected) | – | no line yet (model fair TBL -1.5 +130 / DET +1.5 -130) | no line yet | no line yet |
| 7:00 PM | OTT @ PIT | OTT 3, PIT 4 | PIT 53% | OTT +115 / PIT -115 | 3.1 – 3.3 | 1–6 / 1–6 | 22% | PIT -1.5 33% | 6.5 | Samuel Ersson (expected) / Arturs Silovs (expected) | – | no line yet (model fair PIT -1.5 +210 / OTT +1.5 -210) | no line yet | no line yet |
| 7:00 PM | NJD @ WSH | NJD 2, WSH 3 | WSH 53% | NJD +115 / WSH -115 | 2.9 – 3.1 | 1–5 / 1–5 | 22% | WSH -1.5 32% | 6.1 | Connor Hellebuyck (expected) / Logan Thompson (expected) | – | no line yet (model fair WSH -1.5 +215 / NJD +1.5 -215) | no line yet | no line yet |
| 7:00 PM | PHI @ CBJ | PHI 2, CBJ 3 | CBJ 56% | PHI +130 / CBJ -130 | 2.8 – 3.2 | 1–5 / 1–6 | 22% | CBJ -1.5 35% | 6.0 | Dan Vladar (expected) / Jet Greaves (expected) | – | no line yet (model fair CBJ -1.5 +190 / PHI +1.5 -190) | no line yet | no line yet |
| 7:00 PM | FLA @ STL | FLA 2, STL 3 | STL 56% | FLA +125 / STL -125 | 2.8 – 3.2 | 1–5 / 1–6 | 22% | STL -1.5 34% | 6.0 | Jacob Markstrom (expected) / Joel Hofer (expected) | – | no line yet (model fair STL -1.5 +195 / FLA +1.5 -195) | no line yet | no line yet |
| 8:00 PM | BUF @ DAL | BUF 2, DAL 3 | DAL 56% | BUF +130 / DAL -130 | 2.9 – 3.3 | 1–5 / 1–6 | 23% | DAL -1.5 34% | 6.1 | Ukko-Pekka Luukkonen (expected) / Jake Oettinger (expected) | – | no line yet (model fair DAL -1.5 +190 / BUF +1.5 -190) | no line yet | no line yet |
| 9:00 PM | SJS @ UTA | SJS 3, UTA 4 | UTA 70% | SJS +235 / UTA -235 | 2.6 – 4.0 | 1–5 / 2–7 | 19% | UTA -1.5 50% | 6.6 | Yaroslav Askarov (expected) / Karel Vejmelka (expected) | – | no line yet (model fair UTA -1.5 +100 / SJS +1.5 -100) | no line yet | no line yet |
| 10:00 PM | NYI @ ANA | NYI 4, ANA 3 | NYI 54% | NYI -120 / ANA +120 | 3.5 – 3.2 | 1–6 / 1–6 | 20% | NYI -1.5 34% | 6.7 | Ilya Sorokin (expected) / Laurent Brossoit (expected) | – | no line yet (model fair ANA +1.5 -195 / NYI -1.5 +195) | no line yet | no line yet |
| 10:00 PM | CGY @ LAK | CGY 2, LAK 3 | LAK 57% | CGY +135 / LAK -135 | 2.9 – 3.3 | 1–5 / 1–6 | 22% | LAK -1.5 36% | 6.2 | Dustin Wolf (expected) / Darcy Kuemper (expected) | – | no line yet (model fair LAK -1.5 +175 / CGY +1.5 -175) | no line yet | no line yet |

\* price not posted; assumed -110.

## How the 2026-27 predictions have done

| Predictor | Games | Log loss | Brier | Winners | Goals MAE | Total MAE | 80% range hit |
|---|---|---|---|---|---|---|---|
| Final prediction | 298 | 0.6444 | 0.2265 | 63.1% | 1.35 | 1.79 | 90.3% |
| Model only (before blending) | 298 | 0.6470 | 0.2278 | 61.1% | – | – | – |
| Elo | 298 | 0.6606 | 0.2341 | 60.7% | – | – | – |
| Final prediction, games with a line | 164 | 0.6435 | 0.2261 | 62.8% | 1.32 | 1.82 | 90.9% |
| Model only, games with a line | 164 | 0.6483 | 0.2286 | 59.1% | – | – | – |
| Betting market (de-vigged moneyline) | 164 | 0.6430 | 0.2259 | 62.8% | – | 1.80 | – |

Log loss and Brier score the win chances (lower is better; a coin flip scores 0.693 and 0.250). Hockey is close to a coin flip, so differences in the third decimal matter, and only over hundreds of games. Goals MAE is the average miss on each team's goals.

Overtime: predicted in 21.5% of regular-season games, happened in 22.5%.

134 of these games were played before the predictor went live. They are backfilled walk-forward (each day predicted from earlier days only) with the actual starting goalies and no betting line. Every game since is graded on the prediction logged before puck drop.

### Betting edges

| Market | Edges | Record (W-L-P) | Staked | Units won | ROI | Expected ROI |
|---|---|---|---|---|---|---|
| Puck line | 3 | 0-3-0 | 3.3 | -3.29 | -100.0% | +8.7% |
| Moneyline | 10 | 5-5-0 | 11.3 | +2.30 | +20.4% | +6.0% |
| Total | 2 | 1-1-0 | 1.7 | +0.04 | +2.4% | +3.4% |

Moneyline moved toward the model's edge on the first line seen before puck drop: 29 of 36 games (81%).

Each edge at the stake and price logged with the last prediction before puck drop (edges logged before edges were priced from the final prediction are left out); pushes return the stake. Units are 1% of the bankroll; ROI is units won per unit staked, and expected ROI is what the edges' EVs promised. The moneyline moving toward the model's edge (closing line value) is the quickest sign that it knows something the market doesn't yet.

### Results, Wednesday, November 11

| Game | Predicted | Final | Win chance for winner | Inside 80% ranges | Goalies |
|---|---|---|---|---|---|
| TBL @ BUF | 4–3 | 8–3 | 53% | no | Andrei Vasilevskiy / Ukko-Pekka Luukkonen |
| NYR @ CGY | 4–3 | 3–1 | 54% | yes | Joonas Korpisalo / Devin Cooley |
| PHI @ EDM | 2–3 | 2–3 (OT) | 60% | yes | Dan Vladar / Tristan Jarry |
| UTA @ VGK | 3–4 | 3–5 | 54% | yes | Sebastian Cossa / Carter Hart |
| NSH @ ANA | 3–4 | 4–2 | 46% | yes | Justus Annunen / Laurent Brossoit |
| PIT @ SJS | 4–3 | 3–2 (SO) | 62% | yes | Sergei Murashov / Yaroslav Askarov |

## Power ratings

Goals per game better than an average team, from the goal-rate model: offense and defense combine 5-on-5 expected goals (score and venue adjusted), special teams and actual goals, each weighted against a preseason prior. Defense is positive when it holds opponents below average. Goaltending is rated separately below.

| # | Team | Net | Offense | Defense | 5v5 xGF/60 | 5v5 xGA/60 | PP xGF/60 | PK xGA/60 | Elo |
|---|---|---|---|---|---|---|---|---|---|
| 1 | CAR | +0.78 | +0.49 | +0.29 | 3.48 | 2.38 | 8.65 | 7.25 | 1585 |
| 2 | TBL | +0.43 | +0.22 | +0.21 | 2.93 | 2.45 | 8.11 | 8.02 | 1551 |
| 3 | UTA | +0.43 | +0.24 | +0.18 | 3.17 | 2.42 | 8.25 | 8.86 | 1502 |
| 4 | VGK | +0.32 | +0.06 | +0.26 | 2.71 | 2.39 | 9.27 | 7.31 | 1539 |
| 5 | MIN | +0.26 | +0.09 | +0.18 | 2.88 | 2.53 | 9.18 | 8.23 | 1552 |
| 6 | PIT | +0.25 | +0.17 | +0.08 | 3.01 | 2.57 | 7.83 | 8.02 | 1490 |
| 7 | COL | +0.24 | +0.28 | -0.03 | 2.96 | 2.80 | 7.87 | 7.98 | 1554 |
| 8 | DAL | +0.23 | -0.07 | +0.30 | 2.54 | 2.35 | 9.62 | 7.43 | 1529 |
| 9 | NJD | +0.21 | +0.03 | +0.19 | 2.81 | 2.45 | 9.15 | 7.92 | 1520 |
| 10 | STL | +0.14 | +0.03 | +0.11 | 2.76 | 2.59 | 7.04 | 8.14 | 1499 |
| 11 | OTT | +0.13 | -0.01 | +0.13 | 2.75 | 2.54 | 8.08 | 8.17 | 1518 |
| 12 | BUF | +0.12 | +0.13 | -0.01 | 2.89 | 2.70 | 8.08 | 8.48 | 1509 |
| 13 | FLA | +0.12 | -0.02 | +0.14 | 2.61 | 2.54 | 9.73 | 7.66 | 1504 |
| 14 | BOS | +0.06 | +0.07 | -0.01 | 2.80 | 2.78 | 7.66 | 8.34 | 1543 |
| 15 | EDM | +0.05 | +0.05 | -0.01 | 2.53 | 2.72 | 9.75 | 8.33 | 1536 |
| 16 | WSH | +0.04 | +0.13 | -0.08 | 2.93 | 2.82 | 7.78 | 8.10 | 1519 |
| 17 | NYR | +0.02 | -0.00 | +0.02 | 2.71 | 2.72 | 8.92 | 7.84 | 1498 |
| 18 | LAK | +0.01 | -0.11 | +0.12 | 2.59 | 2.58 | 8.31 | 8.24 | 1465 |
| 19 | MTL | -0.05 | +0.06 | -0.11 | 2.85 | 2.87 | 7.70 | 8.45 | 1534 |
| 20 | NSH | -0.08 | -0.04 | -0.04 | 2.69 | 2.78 | 8.24 | 7.78 | 1507 |
| 21 | CBJ | -0.09 | -0.03 | -0.06 | 2.76 | 2.77 | 7.78 | 8.77 | 1488 |
| 22 | TOR | -0.09 | -0.04 | -0.06 | 2.51 | 2.76 | 8.81 | 8.59 | 1468 |
| 23 | WPG | -0.10 | -0.12 | +0.03 | 2.54 | 2.69 | 8.38 | 8.83 | 1476 |
| 24 | DET | -0.11 | -0.11 | -0.00 | 2.66 | 2.70 | 8.78 | 8.80 | 1475 |
| 25 | NYI | -0.16 | -0.03 | -0.13 | 2.81 | 2.91 | 7.60 | 8.68 | 1480 |
| 26 | PHI | -0.20 | -0.24 | +0.04 | 2.41 | 2.66 | 7.81 | 7.61 | 1470 |
| 27 | CGY | -0.22 | -0.13 | -0.09 | 2.57 | 2.81 | 7.32 | 8.01 | 1459 |
| 28 | SEA | -0.31 | -0.12 | -0.19 | 2.45 | 2.94 | 7.31 | 8.69 | 1478 |
| 29 | ANA | -0.39 | +0.01 | -0.39 | 2.71 | 3.14 | 8.17 | 8.41 | 1490 |
| 30 | CHI | -0.68 | -0.30 | -0.39 | 2.30 | 3.11 | 7.28 | 8.53 | 1416 |
| 31 | VAN | -0.71 | -0.27 | -0.44 | 2.21 | 3.17 | 7.76 | 8.79 | 1398 |
| 32 | SJS | -0.74 | -0.25 | -0.49 | 2.35 | 3.24 | 7.40 | 9.34 | 1447 |

## Goalies

Each team's likeliest next starter. GSAx is goals saved above expected (from this predictor's own shot model), shrunk hard toward a slightly below-average prior, since goaltending repeats poorly from season to season.

| Team | Likely next starter | Share of recent starts | GSAx per 100 shots | Goals per game vs average |
|---|---|---|---|---|
| NYI | Ilya Sorokin | 70% | +0.40 | +0.17 |
| WSH | Logan Thompson | 78% | +0.38 | +0.16 |
| BOS | Jeremy Swayman | 69% | +0.36 | +0.15 |
| MTL | Jacob Fowler | 67% | +0.33 | +0.14 |
| MIN | Jesper Wallstedt | 83% | +0.30 | +0.12 |
| COL | Mackenzie Blackwood | 75% | +0.19 | +0.08 |
| CGY | Devin Cooley | 49% | +0.18 | +0.08 |
| TBL | Andrei Vasilevskiy | 58% | +0.13 | +0.06 |
| STL | Joel Hofer | 74% | +0.09 | +0.04 |
| DAL | Jake Oettinger | 76% | +0.08 | +0.03 |
| CAR | Pyotr Kochetkov | 69% | +0.03 | +0.01 |
| CHI | Spencer Knight | 77% | +0.02 | +0.01 |
| NYR | Dylan Garand | 63% | -0.03 | -0.01 |
| WPG | Stuart Skinner | 68% | -0.06 | -0.03 |
| PHI | Dan Vladar | 55% | -0.08 | -0.03 |
| NJD | Jake Allen | 49% | -0.10 | -0.04 |
| NSH | Juuse Saros | 63% | -0.10 | -0.04 |
| VGK | Carter Hart | 53% | -0.13 | -0.05 |
| DET | John Gibson | 59% | -0.16 | -0.07 |
| BUF | Colten Ellis | 65% | -0.16 | -0.07 |
| SJS | Yaroslav Askarov | 68% | -0.17 | -0.07 |
| CBJ | Cam Talbot | 55% | -0.18 | -0.08 |
| SEA | Joey Daccord | 51% | -0.20 | -0.08 |
| TOR | Sergei Bobrovsky | 66% | -0.20 | -0.08 |
| ANA | Lukas Dostal | 42% | -0.20 | -0.08 |
| UTA | Karel Vejmelka | 78% | -0.22 | -0.09 |
| LAK | Darcy Kuemper | 59% | -0.23 | -0.10 |
| FLA | Jacob Markstrom | 53% | -0.26 | -0.11 |
| EDM | Tristan Jarry | 47% | -0.28 | -0.12 |
| VAN | Leevi Meriläinen | 69% | -0.38 | -0.16 |
| PIT | Arturs Silovs | 61% | -0.40 | -0.17 |
| OTT | Samuel Ersson | 46% | -0.52 | -0.22 |

## Current model fit

- Fitted on 5890 games from 2022-23 to 2026-27.
- Home ice: +3.0% goals for the home team relative to the visitor.
- Second night of a back-to-back: -5.9% goals scored, +3.5% goals allowed.
- Starting goalie: each goal per game he saves above average lowers the opponent's rate by 21%.
- Blend: 46% on the betting line wherever there is one (fitted on 164 logged games, shrunk toward the backtest value).
- Simulator: 22.3% of recent regular-season games reached overtime; trailing teams usually have the goalie pulled with 2 minutes left when down one and 3 when down two; empty-net goals come at 0.40 a minute with the net empty; three-on-three overtime produces 1.04 goals per five minutes.
