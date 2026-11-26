# NHL score predictions

Updated Thu Nov 26, 2026 05:30 PM ET. Refreshed automatically several times a day during the season; each game's prediction is locked at puck drop and graded once the final score is in.

Each game is simulated 10,000 times minute by minute, with pulled goalies, empty-net goals, overtime and shootouts. The predicted score is the most common final score in which the likelier winner wins; as in the official result, a shootout winner gets one extra goal. Hockey is low-scoring and luck-heavy, so read the win chance and the ranges (80% of simulated outcomes for each team) before the single score.

Goalies marked with a percentage are projected from recent starts (the share is the chance he starts); "probable" or "confirmed" ones come from ESPN and replace the projection when available.

The fair moneyline is the American odds that match the win chance exactly, with no bookmaker margin: -150 means risk $150 to win $100, +150 means risk $100 to win $150. A sportsbook's price is a little worse on both sides because of its cut, so a book only offers value on a team when its price beats the fair line. The puck line is the favorite's chance to win by two or more.

The edge columns price each side of the puck line, moneyline and total with the final prediction: the model's goal rates blended with the market's, simulated against the posted lines, overtime and shootout included (the shootout winner gets one goal), and anchored to the market's own chances so only what the blend moves off the market counts. Each cell shows the side with the best expected value (EV) per $1 bet at the posted price. A side is an edge only if its EV is at least 3%: a pick shows its price, EV, its chance of winning the bet and its stake, a 25% share of the Kelly stake in units of 1% of the bankroll, with at most 3 units on one game; "no edge" means neither side clears the bar. A projected starting goalie is wrong about a third of the time and the market prices the real one, so edges wait until both starters are confirmed. A total with no posted price is assumed to be -110 (marked \*); the puck line and moneyline are never assumed, so without a price the cell shows the model's fair odds instead. Treat the edges as an experiment, not betting advice; see the backtest for how they have done on past seasons. Their record is tracked live below.

## Friday, November 27

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected goals | 80% range | Overtime | Puck line | Total: model / line | Goalies | Posted moneyline | Puck line edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1:00 PM | TOR @ BOS | TOR 3, BOS 4 | BOS 59% | TOR +145 / BOS -145 | 2.9 – 3.6 | 1–5 / 1–6 | 21% | BOS -1.5 39% | 6.5 / 6.5 (over 50%) | Anthony Stolarz (confirmed) / Jeremy Swayman (expected) | TOR +140 / BOS -166 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 1:00 PM | CGY @ NJD | CGY 2, NJD 3 | NJD 67% | CGY +200 / NJD -200 | 2.6 – 3.7 | 1–5 / 1–6 | 21% | NJD -1.5 45% | 6.2 / 6.5 (over 45%) | Dustin Wolf (expected) / Connor Hellebuyck (expected) | CGY +215 / NJD -265 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 1:00 PM | UTA @ NSH | UTA 4, NSH 3 | UTA 50% | UTA -100 / NSH +100 | 3.3 – 3.2 | 1–6 / 1–6 | 23% | UTA -1.5 30% | 6.5 / 6.5 (over 49%) | Karel Vejmelka (expected) / Juuse Saros (expected) | UTA -112 / NSH -108 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 2:00 PM | DAL @ STL | DAL 3, STL 2 | DAL 55% | DAL -125 / STL +125 | 3.1 – 2.8 | 1–5 / 1–5 | 23% | DAL -1.5 33% | 6.0 / 5.5 (over 52%) | Jake Oettinger (expected) / Joel Hofer (expected) | DAL -142 / STL +120 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 3:00 PM | OTT @ TBL | OTT 2, TBL 3 | TBL 56% | OTT +125 / TBL -125 | 2.9 – 3.3 | 1–5 / 1–6 | 23% | TBL -1.5 35% | 6.1 / 5.5 (over 55%) | Linus Ullmark (expected) / Andrei Vasilevskiy (expected) | OTT +114 / TBL -135 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 3:00 PM | VAN @ PHI | VAN 3, PHI 4 | PHI 67% | VAN +205 / PHI -205 | 2.7 – 3.8 | 1–5 / 1–6 | 20% | PHI -1.5 45% | 6.4 / 6.5 (over 48%) | Leevi Meriläinen (expected) / Dan Vladar (expected) | VAN +190 / PHI -230 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 3:00 PM | FLA @ WSH | FLA 3, WSH 4 | WSH 52% | FLA +110 / WSH -110 | 3.2 – 3.3 | 1–6 / 1–6 | 21% | WSH -1.5 32% | 6.5 / 6.5 (over 50%) | Jacob Markstrom (expected) / Logan Thompson (expected) | FLA -112 / WSH -108 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 3:00 PM | DET @ CBJ | DET 2, CBJ 3 | CBJ 56% | DET +125 / CBJ -125 | 2.9 – 3.2 | 1–5 / 1–6 | 23% | CBJ -1.5 33% | 6.2 / 5.5 (over 55%) | John Gibson (expected) / Jet Greaves (confirmed) | DET +110 / CBJ -130 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 4:00 PM | COL @ MIN | COL 3, MIN 4 | MIN 54% | COL +115 / MIN -115 | 3.0 – 3.3 | 1–5 / 1–6 | 21% | MIN -1.5 33% | 6.3 / 6.5 (over 47%) | Mackenzie Blackwood (expected) / Jesper Wallstedt (expected) | COL +110 / MIN -130 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 4:00 PM | LAK @ ANA | LAK 4, ANA 3 | LAK 51% | LAK -105 / ANA +105 | 3.2 – 3.2 | 1–6 / 1–6 | 22% | LAK -1.5 30% | 6.4 / 6.5 (over 48%) | Darcy Kuemper (expected) / Laurent Brossoit (confirmed) | LAK -115 / ANA -105 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 4:00 PM | VGK @ SJS | VGK 4, SJS 3 | VGK 66% | VGK -190 / SJS +190 | 3.8 – 2.8 | 1–6 / 1–5 | 21% | VGK -1.5 44% | 6.6 / 6.5 (over 51%) | Carter Hart (expected) / Yaroslav Askarov (expected) | VGK -205 / SJS +170 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 5:30 PM | NYR @ CHI | NYR 4, CHI 3 | NYR 61% | NYR -160 / CHI +160 | 3.5 – 2.8 | 1–6 / 1–5 | 21% | NYR -1.5 40% | 6.3 / 6.5 (over 47%) | Dylan Garand (expected) / Spencer Knight (expected) | NYR -175 / CHI +145 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 7:30 PM | WPG @ NYI | WPG 3, NYI 4 | NYI 54% | WPG +120 / NYI -120 | 3.0 – 3.3 | 1–5 / 1–6 | 23% | NYI -1.5 33% | 6.3 / 6.5 (over 47%) | Stuart Skinner (expected) / Ilya Sorokin (expected) | WPG +114 / NYI -135 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 8:00 PM | PIT @ BUF | PIT 3, BUF 4 | BUF 57% | PIT +130 / BUF -130 | 3.1 – 3.5 | 1–5 / 1–6 | 21% | BUF -1.5 36% | 6.6 / 6.5 (over 51%) | Arturs Silovs (expected) / Alex Lyon (expected) | PIT +130 / BUF -155 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 8:00 PM | SEA @ EDM | SEA 3, EDM 4 | EDM 63% | SEA +175 / EDM -175 | 2.8 – 3.7 | 1–5 / 1–6 | 21% | EDM -1.5 43% | 6.5 / 6.5 (over 50%) | Philipp Grubauer (expected) / Devon Levi (expected) | SEA +170 / EDM -205 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |

## Saturday, November 28

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected goals | 80% range | Overtime | Puck line | Total: model / line | Goalies | Posted moneyline | Puck line edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 4:00 PM | MTL @ VGK | MTL 2, VGK 3 | VGK 54% | MTL +120 / VGK -120 | 2.9 – 3.2 | 1–5 / 1–6 | 22% | VGK -1.5 33% | 6.2 | Jakub Dobes (expected) / Adin Hill (expected) | – | no line yet (model fair VGK -1.5 +200 / MTL +1.5 -200) | no line yet | no line yet |
| 6:00 PM | TBL @ FLA | TBL 3, FLA 2 | TBL 56% | TBL -125 / FLA +125 | 3.2 – 2.8 | 1–6 / 1–5 | 22% | TBL -1.5 34% | 6.0 | Dennis Hildeby (expected) / Akira Schmid (expected) | – | no line yet (model fair FLA +1.5 -195 / TBL -1.5 +195) | no line yet | no line yet |
| 7:00 PM | NSH @ DET | NSH 3, DET 2 | NSH 52% | NSH -110 / DET +110 | 3.2 – 3.0 | 1–6 / 1–5 | 22% | NSH -1.5 31% | 6.2 | Justus Annunen (expected) / John Gibson (expected) | – | no line yet (model fair DET +1.5 -225 / NSH -1.5 +225) | no line yet | no line yet |
| 7:00 PM | WPG @ NJD | WPG 2, NJD 3 | NJD 59% | WPG +145 / NJD -145 | 2.7 – 3.3 | 1–5 / 1–6 | 23% | NJD -1.5 37% | 6.0 | Nico Daws (expected) / Jake Allen (expected) | – | no line yet (model fair NJD -1.5 +170 / WPG +1.5 -170) | no line yet | no line yet |
| 7:00 PM | CGY @ NYR | CGY 2, NYR 3 | NYR 58% | CGY +135 / NYR -135 | 2.8 – 3.3 | 1–5 / 1–6 | 23% | NYR -1.5 36% | 6.0 | Devin Cooley (expected) / Joonas Korpisalo (expected) | – | no line yet (model fair NYR -1.5 +180 / CGY +1.5 -180) | no line yet | no line yet |
| 7:00 PM | TOR @ PIT | TOR 3, PIT 4 | PIT 57% | TOR +130 / PIT -130 | 2.9 – 3.4 | 1–5 / 1–6 | 22% | PIT -1.5 36% | 6.3 | Sergei Bobrovsky (confirmed) / Sergei Murashov (expected) | – | no line yet (model fair PIT -1.5 +180 / TOR +1.5 -180) | no line yet | no line yet |
| 7:00 PM | OTT @ CAR | OTT 3, CAR 4 | CAR 70% | OTT +230 / CAR -230 | 2.5 – 3.9 | 1–5 / 1–6 | 20% | CAR -1.5 49% | 6.4 | Samuel Ersson (expected) / Pyotr Kochetkov (expected) | – | no line yet (model fair CAR -1.5 +105 / OTT +1.5 -105) | no line yet | no line yet |
| 7:00 PM | WSH @ STL | WSH 4, STL 3 | WSH 52% | WSH -110 / STL +110 | 3.4 – 3.2 | 1–6 / 1–6 | 22% | WSH -1.5 32% | 6.6 | Charlie Lindgren (expected) / Jordan Binnington (expected) | – | no line yet (model fair STL +1.5 -215 / WSH -1.5 +215) | no line yet | no line yet |
| 7:30 PM | NYI @ PHI | NYI 3, PHI 2 | NYI 50% | NYI -100 / PHI +100 | 3.0 – 3.0 | 1–5 / 1–5 | 23% | NYI -1.5 29% | 6.0 | Semyon Varlamov (expected) / Joseph Woll (expected) | – | no line yet (model fair PHI +1.5 -245 / NYI -1.5 +245) | no line yet | no line yet |
| 8:00 PM | UTA @ DAL | UTA 2, DAL 3 | DAL 52% | UTA +105 / DAL -105 | 2.9 – 3.0 | 1–5 / 1–5 | 22% | DAL -1.5 31% | 6.0 | Sebastian Cossa (expected) / Casey DeSmith (expected) | – | no line yet (model fair DAL -1.5 +225 / UTA +1.5 -225) | no line yet | no line yet |
| 9:00 PM | SJS @ COL | SJS 3, COL 4 | COL 74% | SJS +285 / COL -285 | 2.6 – 4.2 | 1–5 / 2–7 | 18% | COL -1.5 54% | 6.8 | Alex Nedeljkovic (expected) / Scott Wedgewood (expected) | – | no line yet (model fair COL -1.5 -115 / SJS +1.5 +115) | no line yet | no line yet |
| 9:00 PM | ANA @ LAK | ANA 2, LAK 3 | LAK 58% | ANA +140 / LAK -140 | 2.8 – 3.3 | 1–5 / 1–6 | 22% | LAK -1.5 37% | 6.2 | Ville Husso (expected) / Anton Forsberg (expected) | – | no line yet (model fair LAK -1.5 +175 / ANA +1.5 -175) | no line yet | no line yet |
| 10:00 PM | EDM @ SEA | EDM 4, SEA 3 | EDM 56% | EDM -130 / SEA +130 | 3.4 – 2.9 | 1–6 / 1–5 | 22% | EDM -1.5 35% | 6.3 | Tristan Jarry (expected) / Joey Daccord (expected) | – | no line yet (model fair SEA +1.5 -185 / EDM -1.5 +185) | no line yet | no line yet |

\* price not posted; assumed -110.

## Sunday, November 29

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected goals | 80% range | Overtime | Puck line | Total: model / line | Goalies | Posted moneyline | Puck line edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2:00 PM | MIN @ CHI | MIN 3, CHI 2 | MIN 70% | MIN -235 / CHI +235 | 3.7 – 2.4 | 1–6 / 0–4 | 20% | MIN -1.5 49% | 6.1 | Jesper Wallstedt (expected) / Spencer Knight (expected) | – | no line yet (model fair CHI +1.5 -105 / MIN -1.5 +105) | no line yet | no line yet |
| 5:00 PM | VAN @ BOS | VAN 3, BOS 4 | BOS 75% | VAN +300 / BOS -300 | 2.5 – 4.3 | 1–5 / 2–7 | 17% | BOS -1.5 56% | 6.8 | Leevi Meriläinen (expected) / Jeremy Swayman (expected) | – | no line yet (model fair BOS -1.5 -125 / VAN +1.5 +125) | no line yet | no line yet |

\* price not posted; assumed -110.

## How the 2026-27 predictions have done

| Predictor | Games | Log loss | Brier | Winners | Goals MAE | Total MAE | 80% range hit |
|---|---|---|---|---|---|---|---|
| Final prediction | 399 | 0.6603 | 0.2339 | 62.2% | 1.38 | 1.82 | 89.5% |
| Model only (before blending) | 399 | 0.6628 | 0.2352 | 60.2% | – | – | – |
| Elo | 399 | 0.6731 | 0.2401 | 58.6% | – | – | – |
| Final prediction, games with a line | 265 | 0.6667 | 0.2369 | 60.8% | 1.38 | 1.86 | 89.4% |
| Model only, games with a line | 265 | 0.6705 | 0.2389 | 57.7% | – | – | – |
| Betting market (de-vigged moneyline) | 265 | 0.6649 | 0.2361 | 61.1% | – | 1.85 | – |

Log loss and Brier score the win chances (lower is better; a coin flip scores 0.693 and 0.250). Hockey is close to a coin flip, so differences in the third decimal matter, and only over hundreds of games. Goals MAE is the average miss on each team's goals.

Overtime: predicted in 21.5% of regular-season games, happened in 21.6%.

134 of these games were played before the predictor went live. They are backfilled walk-forward (each day predicted from earlier days only) with the actual starting goalies and no betting line. Every game since is graded on the prediction logged before puck drop.

### Betting edges

| Market | Edges | Record (W-L-P) | Staked | Units won | ROI | Expected ROI |
|---|---|---|---|---|---|---|
| Puck line | 6 | 1-5-0 | 5.9 | -4.30 | -72.3% | +7.5% |
| Moneyline | 14 | 8-6-0 | 15.6 | +4.52 | +29.0% | +5.4% |
| Total | 2 | 1-1-0 | 1.7 | +0.04 | +2.4% | +3.4% |

Moneyline moved toward the model's edge on the first line seen before puck drop: 43 of 58 games (74%).

Each edge at the stake and price logged with the last prediction before puck drop (edges logged before edges were priced from the final prediction are left out); pushes return the stake. Units are 1% of the bankroll; ROI is units won per unit staked, and expected ROI is what the edges' EVs promised. The moneyline moving toward the model's edge (closing line value) is the quickest sign that it knows something the market doesn't yet.

### Results, Wednesday, November 25

| Game | Predicted | Final | Win chance for winner | Inside 80% ranges | Goalies |
|---|---|---|---|---|---|
| WPG @ BOS | 3–4 | 4–2 | 41% | yes | Nico Daws / Jeremy Swayman |
| NYR @ BUF | 3–4 | 1–5 | 53% | yes | Joonas Korpisalo / Ukko-Pekka Luukkonen |
| CAR @ TBL | 4–3 | 3–1 | 52% | yes | Brandon Bussi / Andrei Vasilevskiy |
| OTT @ FLA | 2–3 | 3–5 | 52% | yes | Linus Ullmark / Jacob Markstrom |
| STL @ NYI | 2–3 | 2–3 (SO) | 52% | yes | Joel Hofer / Ilya Sorokin |
| CGY @ PIT | 3–4 | 6–3 | 39% | no | Dustin Wolf / Arturs Silovs |
| PHI @ WSH | 3–4 | 3–7 | 58% | no | Joseph Woll / Logan Thompson |
| NJD @ CBJ | 4–3 | 3–2 (SO) | 57% | yes | Connor Hellebuyck / Cam Talbot |
| VAN @ DET | 3–4 | 1–5 | 69% | yes | Leevi Meriläinen / Daniil Tarasov |
| NSH @ DAL | 2–3 | 3–1 | 39% | yes | Juuse Saros / Jake Oettinger |
| UTA @ MIN | 3–4 | 4–3 | 43% | yes | Karel Vejmelka / Jesper Wallstedt |
| MTL @ COL | 3–4 | 0–6 | 54% | no | Jacob Fowler / Mackenzie Blackwood |
| CHI @ SEA | 3–4 | 3–1 | 43% | yes | Spencer Knight / Joey Daccord |
| SJS @ ANA | 3–4 | 0–7 | 57% | no | Alex Nedeljkovic / Laurent Brossoit |

## Power ratings

Goals per game better than an average team, from the goal-rate model: offense and defense combine 5-on-5 expected goals (score and venue adjusted), special teams and actual goals, each weighted against a preseason prior. Defense is positive when it holds opponents below average. Goaltending is rated separately below.

| # | Team | Net | Offense | Defense | 5v5 xGF/60 | 5v5 xGA/60 | PP xGF/60 | PK xGA/60 | Elo |
|---|---|---|---|---|---|---|---|---|---|
| 1 | CAR | +0.81 | +0.48 | +0.32 | 3.39 | 2.30 | 8.37 | 6.96 | 1602 |
| 2 | TBL | +0.47 | +0.22 | +0.24 | 2.97 | 2.37 | 7.87 | 7.85 | 1545 |
| 3 | UTA | +0.37 | +0.21 | +0.17 | 3.08 | 2.41 | 8.10 | 8.49 | 1500 |
| 4 | VGK | +0.30 | +0.08 | +0.21 | 2.71 | 2.41 | 9.13 | 7.02 | 1529 |
| 5 | MIN | +0.29 | +0.08 | +0.22 | 2.75 | 2.44 | 8.61 | 7.72 | 1568 |
| 6 | COL | +0.28 | +0.26 | +0.03 | 2.89 | 2.70 | 7.80 | 7.91 | 1562 |
| 7 | OTT | +0.25 | +0.04 | +0.21 | 2.79 | 2.40 | 7.78 | 8.10 | 1526 |
| 8 | NJD | +0.21 | +0.05 | +0.17 | 2.76 | 2.43 | 9.00 | 7.62 | 1527 |
| 9 | WSH | +0.17 | +0.21 | -0.04 | 3.02 | 2.69 | 7.95 | 7.98 | 1500 |
| 10 | PIT | +0.15 | +0.13 | +0.02 | 2.95 | 2.61 | 7.69 | 7.84 | 1467 |
| 11 | DAL | +0.15 | -0.10 | +0.25 | 2.53 | 2.39 | 9.20 | 7.07 | 1529 |
| 12 | FLA | +0.12 | -0.03 | +0.15 | 2.54 | 2.50 | 9.42 | 7.50 | 1511 |
| 13 | STL | +0.08 | +0.07 | +0.01 | 2.75 | 2.68 | 7.11 | 7.91 | 1511 |
| 14 | BOS | +0.08 | +0.07 | +0.01 | 2.77 | 2.69 | 7.55 | 8.09 | 1526 |
| 15 | BUF | +0.08 | +0.11 | -0.03 | 2.76 | 2.69 | 7.91 | 8.34 | 1517 |
| 16 | EDM | +0.07 | +0.04 | +0.03 | 2.45 | 2.62 | 9.43 | 8.06 | 1533 |
| 17 | NYR | +0.03 | -0.01 | +0.04 | 2.67 | 2.66 | 8.62 | 7.55 | 1497 |
| 18 | LAK | +0.01 | -0.16 | +0.17 | 2.46 | 2.48 | 8.05 | 7.90 | 1468 |
| 19 | NSH | -0.04 | +0.01 | -0.04 | 2.78 | 2.74 | 7.89 | 7.53 | 1508 |
| 20 | MTL | -0.04 | +0.02 | -0.06 | 2.80 | 2.77 | 7.45 | 8.31 | 1523 |
| 21 | NYI | -0.08 | -0.03 | -0.06 | 2.72 | 2.78 | 7.06 | 8.60 | 1496 |
| 22 | TOR | -0.10 | -0.06 | -0.04 | 2.47 | 2.69 | 8.63 | 8.32 | 1455 |
| 23 | DET | -0.14 | -0.10 | -0.04 | 2.62 | 2.70 | 8.44 | 8.49 | 1475 |
| 24 | WPG | -0.14 | -0.11 | -0.04 | 2.47 | 2.74 | 8.40 | 9.02 | 1495 |
| 25 | CBJ | -0.16 | -0.09 | -0.07 | 2.58 | 2.74 | 7.66 | 8.37 | 1477 |
| 26 | PHI | -0.22 | -0.22 | -0.00 | 2.35 | 2.65 | 7.81 | 7.47 | 1473 |
| 27 | CGY | -0.26 | -0.12 | -0.14 | 2.57 | 2.85 | 6.96 | 7.68 | 1459 |
| 28 | ANA | -0.33 | +0.02 | -0.36 | 2.70 | 3.04 | 7.74 | 7.98 | 1483 |
| 29 | SEA | -0.36 | -0.16 | -0.20 | 2.35 | 2.90 | 7.11 | 8.48 | 1469 |
| 30 | CHI | -0.60 | -0.27 | -0.33 | 2.26 | 3.01 | 7.08 | 8.31 | 1434 |
| 31 | SJS | -0.70 | -0.23 | -0.46 | 2.35 | 3.14 | 7.14 | 9.26 | 1441 |
| 32 | VAN | -0.83 | -0.26 | -0.57 | 2.23 | 3.26 | 7.51 | 8.69 | 1395 |

## Goalies

Each team's likeliest next starter. GSAx is goals saved above expected (from this predictor's own shot model), shrunk hard toward a slightly below-average prior, since goaltending repeats poorly from season to season.

| Team | Likely next starter | Share of recent starts | GSAx per 100 shots | Goals per game vs average |
|---|---|---|---|---|
| NYI | Ilya Sorokin | 72% | +0.43 | +0.18 |
| COL | Mackenzie Blackwood | 70% | +0.29 | +0.12 |
| BOS | Jeremy Swayman | 76% | +0.28 | +0.12 |
| WSH | Logan Thompson | 73% | +0.27 | +0.11 |
| MIN | Jesper Wallstedt | 83% | +0.27 | +0.11 |
| MTL | Jacob Fowler | 65% | +0.24 | +0.10 |
| OTT | Linus Ullmark | 57% | +0.20 | +0.09 |
| STL | Joel Hofer | 73% | +0.19 | +0.08 |
| TBL | Andrei Vasilevskiy | 74% | +0.18 | +0.07 |
| DAL | Jake Oettinger | 82% | +0.17 | +0.07 |
| NJD | Connor Hellebuyck | 64% | +0.10 | +0.04 |
| CHI | Spencer Knight | 81% | +0.08 | +0.04 |
| WPG | Stuart Skinner | 68% | +0.04 | +0.02 |
| TOR | Anthony Stolarz | 56% | +0.02 | +0.01 |
| NYR | Dylan Garand | 63% | -0.00 | -0.00 |
| CAR | Pyotr Kochetkov | 59% | -0.01 | -0.00 |
| EDM | Devon Levi | 54% | -0.05 | -0.02 |
| NSH | Juuse Saros | 71% | -0.07 | -0.03 |
| BUF | Ukko-Pekka Luukkonen | 53% | -0.08 | -0.03 |
| PHI | Joseph Woll | 54% | -0.14 | -0.06 |
| CBJ | Cam Talbot | 66% | -0.17 | -0.07 |
| LAK | Darcy Kuemper | 63% | -0.19 | -0.08 |
| UTA | Karel Vejmelka | 55% | -0.19 | -0.08 |
| VGK | Carter Hart | 53% | -0.20 | -0.08 |
| SEA | Joey Daccord | 52% | -0.20 | -0.08 |
| DET | John Gibson | 51% | -0.21 | -0.09 |
| SJS | Yaroslav Askarov | 60% | -0.22 | -0.09 |
| FLA | Jacob Markstrom | 61% | -0.23 | -0.10 |
| CGY | Dustin Wolf | 57% | -0.24 | -0.10 |
| ANA | Lukas Dostal | 42% | -0.29 | -0.12 |
| VAN | Leevi Meriläinen | 70% | -0.37 | -0.16 |
| PIT | Arturs Silovs | 62% | -0.39 | -0.16 |

## Current model fit

- Fitted on 5991 games from 2022-23 to 2026-27.
- Home ice: +2.9% goals for the home team relative to the visitor.
- Second night of a back-to-back: -5.8% goals scored, +3.0% goals allowed.
- Starting goalie: each goal per game he saves above average lowers the opponent's rate by 21%.
- Blend: 55% on the betting line wherever there is one (fitted on 265 logged games, shrunk toward the backtest value).
- Simulator: 22.3% of recent regular-season games reached overtime; trailing teams usually have the goalie pulled with 2 minutes left when down one and 3 when down two; empty-net goals come at 0.40 a minute with the net empty; three-on-three overtime produces 1.02 goals per five minutes.
