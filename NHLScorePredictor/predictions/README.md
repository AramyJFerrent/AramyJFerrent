# NHL score predictions

Updated Tue Nov 17, 2026 06:36 PM ET. Refreshed automatically several times a day during the season; each game's prediction is locked at puck drop and graded once the final score is in.

Each game is simulated 10,000 times minute by minute, with pulled goalies, empty-net goals, overtime and shootouts. The predicted score is the most common final score in which the likelier winner wins; as in the official result, a shootout winner gets one extra goal. Hockey is low-scoring and luck-heavy, so read the win chance and the ranges (80% of simulated outcomes for each team) before the single score.

Goalies marked with a percentage are projected from recent starts (the share is the chance he starts); "probable" or "confirmed" ones come from ESPN and replace the projection when available.

The fair moneyline is the American odds that match the win chance exactly, with no bookmaker margin: -150 means risk $150 to win $100, +150 means risk $100 to win $150. A sportsbook's price is a little worse on both sides because of its cut, so a book only offers value on a team when its price beats the fair line. The puck line is the favorite's chance to win by two or more.

The edge columns price each side of the puck line, moneyline and total with the final prediction: the model's goal rates blended with the market's, simulated against the posted lines, overtime and shootout included (the shootout winner gets one goal), and anchored to the market's own chances so only what the blend moves off the market counts. Each cell shows the side with the best expected value (EV) per $1 bet at the posted price. A side is an edge only if its EV is at least 3%: a pick shows its price, EV, its chance of winning the bet and its stake, a 25% share of the Kelly stake in units of 1% of the bankroll, with at most 3 units on one game; "no edge" means neither side clears the bar. A projected starting goalie is wrong about a third of the time and the market prices the real one, so edges wait until both starters are confirmed. A total with no posted price is assumed to be -110 (marked \*); the puck line and moneyline are never assumed, so without a price the cell shows the model's fair odds instead. Treat the edges as an experiment, not betting advice; see the backtest for how they have done on past seasons. Their record is tracked live below.

## Tuesday, November 17

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected goals | 80% range | Overtime | Puck line | Total: model / line | Goalies | Posted moneyline | Puck line edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 7:00 PM | LAK @ BOS | LAK 2, BOS 3 | BOS 60% | LAK +150 / BOS -150 | 2.8 – 3.4 | 1–5 / 1–6 | 22% | BOS -1.5 38% | 6.2 / 6.5 (over 44%) | Darcy Kuemper (confirmed) / Michael DiPietro (confirmed) | LAK +140 / BOS -166 | no edge | no edge | no edge |
| 7:00 PM | EDM @ FLA | EDM 2, FLA 3 | FLA 52% | EDM +110 / FLA -110 | 3.0 – 3.2 | 1–5 / 1–6 | 23% | FLA -1.5 31% | 6.2 / 6.5 (over 45%) | Devon Levi (confirmed) / Jacob Markstrom (confirmed) | EDM +105 / FLA -125 | no edge | no edge | no edge |
| 7:00 PM | CBJ @ NYI | CBJ 2, NYI 3 | NYI 56% | CBJ +125 / NYI -125 | 2.8 – 3.2 | 1–5 / 1–6 | 23% | NYI -1.5 34% | 6.0 / 5.5 (over 53%) | Cam Talbot (confirmed) / Ilya Sorokin (confirmed) | CBJ +114 / NYI -135 | no edge | no edge | no edge |
| 7:00 PM | BUF @ PHI | BUF 4, PHI 3 | BUF 55% | BUF -120 / PHI +120 | 3.3 – 3.0 | 1–6 / 1–5 | 22% | BUF -1.5 34% | 6.3 / 6.5 (over 46%) | Alex Lyon (confirmed) / Joseph Woll (confirmed) | BUF -125 / PHI +105 | no edge | no edge | no edge |
| 7:00 PM | OTT @ WPG | OTT 3, WPG 2 | OTT 53% | OTT -115 / WPG +115 | 3.1 – 2.9 | 1–5 / 1–5 | 23% | OTT -1.5 32% | 6.0 / 5.5 (over 53%) | Linus Ullmark (confirmed) / Stuart Skinner (confirmed) | OTT -130 / WPG +110 | no edge | no edge | no edge |
| 7:30 PM | WSH @ TBL | WSH 3, TBL 4 | TBL 57% | WSH +135 / TBL -135 | 2.9 – 3.4 | 1–5 / 1–6 | 21% | TBL -1.5 36% | 6.3 / 6.5 (over 47%) | Logan Thompson (confirmed) / Andrei Vasilevskiy (confirmed) | WSH +136 / TBL -162 | no edge | no edge | no edge |
| 7:30 PM | TOR @ CHI | TOR 4, CHI 3 | TOR 57% | TOR -135 / CHI +135 | 3.5 – 3.0 | 1–6 / 1–5 | 22% | TOR -1.5 37% | 6.4 / 6.5 (over 49%) | Sergei Bobrovsky (confirmed) / Spencer Knight (confirmed) | TOR -142 / CHI +120 | no edge | no edge | no edge |
| 8:00 PM | ANA @ STL | ANA 3, STL 4 | STL 57% | ANA +130 / STL -130 | 3.1 – 3.5 | 1–6 / 1–6 | 21% | STL -1.5 36% | 6.7 / 6.5 (over 52%) | Ville Husso (expected) / Jordan Binnington (confirmed) | ANA +105 / STL -125 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 8:00 PM | NSH @ MIN | NSH 3, MIN 4 | MIN 63% | NSH +170 / MIN -170 | 2.8 – 3.6 | 1–5 / 1–6 | 21% | MIN -1.5 41% | 6.3 / 6.5 (over 48%) | Juuse Saros (expected) / Jesper Wallstedt (confirmed) | NSH +170 / MIN -205 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 10:00 PM | DAL @ VGK | DAL 2, VGK 3 | VGK 52% | DAL +110 / VGK -110 | 2.9 – 3.0 | 1–5 / 1–5 | 23% | VGK -1.5 30% | 6.0 / 5.5 (over 52%) | Jake Oettinger (confirmed) / Adin Hill (confirmed) | DAL +105 / VGK -125 | no edge | no edge | no edge |
| 10:00 PM | CGY @ SJS | CGY 4, SJS 3 | CGY 51% | CGY -105 / SJS +105 | 3.2 – 3.2 | 1–6 / 1–6 | 22% | CGY -1.5 30% | 6.4 / 5.5 (over 58%) | Dustin Wolf (confirmed) / Yaroslav Askarov (confirmed) | CGY +110 / SJS -130 | no edge | CGY (+110): EV +3.7%, 49%, stake 0.8u | no edge |

## Wednesday, November 18

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected goals | 80% range | Overtime | Puck line | Total: model / line | Goalies | Posted moneyline | Puck line edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 7:30 PM | BOS @ DET | BOS 2, DET 3 | DET 51% | BOS +100 / DET -100 | 3.0 – 3.1 | 1–5 / 1–5 | 23% | DET -1.5 30% | 6.1 / 5.5 (over 54%) | Jeremy Swayman (expected) / Daniil Tarasov (confirmed) | BOS +102 / DET -122 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 7:30 PM | MTL @ NJD | MTL 2, NJD 3 | NJD 59% | MTL +140 / NJD -140 | 2.8 – 3.3 | 1–5 / 1–6 | 21% | NJD -1.5 37% | 6.1 / 6.5 (over 44%) | Jacob Fowler (expected) / Connor Hellebuyck (expected) | MTL +136 / NJD -162 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 10:00 PM | COL @ UTA | COL 3, UTA 4 | UTA 51% | COL +105 / UTA -105 | 3.2 – 3.3 | 1–6 / 1–6 | 22% | UTA -1.5 31% | 6.5 / 6.5 (over 50%) | Mackenzie Blackwood (expected) / Karel Vejmelka (expected) | COL -112 / UTA -108 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |

## Thursday, November 19

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected goals | 80% range | Overtime | Puck line | Total: model / line | Goalies | Posted moneyline | Puck line edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 7:00 PM | LAK @ TOR | LAK 2, TOR 3 | TOR 53% | LAK +110 / TOR -110 | 3.0 – 3.1 | 1–5 / 1–6 | 23% | TOR -1.5 31% | 6.1 | Darcy Kuemper (expected) / Sergei Bobrovsky (expected) | – | no line yet (model fair TOR -1.5 +220 / LAK +1.5 -220) | no line yet | no line yet |
| 7:00 PM | PHI @ OTT | PHI 2, OTT 3 | OTT 62% | PHI +165 / OTT -165 | 2.5 – 3.3 | 1–5 / 1–6 | 23% | OTT -1.5 39% | 5.8 | Dan Vladar (expected) / Linus Ullmark (expected) | – | no line yet (model fair OTT -1.5 +155 / PHI +1.5 -155) | no line yet | no line yet |
| 7:00 PM | STL @ PIT | STL 3, PIT 4 | PIT 51% | STL +100 / PIT -100 | 3.1 – 3.1 | 1–5 / 1–6 | 22% | PIT -1.5 30% | 6.2 | Joel Hofer (expected) / Arturs Silovs (expected) | – | no line yet (model fair PIT -1.5 +235 / STL +1.5 -235) | no line yet | no line yet |
| 7:00 PM | BUF @ WSH | BUF 3, WSH 4 | WSH 56% | BUF +125 / WSH -125 | 3.1 – 3.4 | 1–5 / 1–6 | 21% | WSH -1.5 35% | 6.5 | Alex Lyon (expected) / Logan Thompson (expected) | – | no line yet (model fair WSH -1.5 +185 / BUF +1.5 -185) | no line yet | no line yet |
| 7:00 PM | MTL @ CAR | MTL 3, CAR 4 | CAR 73% | MTL +275 / CAR -275 | 2.4 – 4.0 | 0–5 / 2–7 | 19% | CAR -1.5 52% | 6.4 | Jakub Dobes (expected) / Pyotr Kochetkov (expected) | – | no line yet (model fair CAR -1.5 -110 / MTL +1.5 +110) | no line yet | no line yet |
| 7:00 PM | NYI @ WPG | NYI 2, WPG 3 | WPG 52% | NYI +105 / WPG -105 | 3.0 – 3.2 | 1–5 / 1–6 | 22% | WPG -1.5 31% | 6.2 | Ilya Sorokin (expected) / Stuart Skinner (expected) | – | no line yet (model fair WPG -1.5 +225 / NYI +1.5 -225) | no line yet | no line yet |
| 7:30 PM | EDM @ TBL | EDM 2, TBL 3 | TBL 58% | EDM +135 / TBL -135 | 2.8 – 3.3 | 1–5 / 1–6 | 22% | TBL -1.5 36% | 6.1 | Devon Levi (expected) / Andrei Vasilevskiy (expected) | – | no line yet (model fair TBL -1.5 +175 / EDM +1.5 -175) | no line yet | no line yet |
| 8:00 PM | CBJ @ CHI | CBJ 4, CHI 3 | CBJ 58% | CBJ -140 / CHI +140 | 3.4 – 2.9 | 1–6 / 1–5 | 22% | CBJ -1.5 37% | 6.3 | Jet Greaves (expected) / Spencer Knight (expected) | – | no line yet (model fair CHI +1.5 -170 / CBJ -1.5 +170) | no line yet | no line yet |
| 8:00 PM | MIN @ CGY | MIN 4, CGY 3 | MIN 64% | MIN -175 / CGY +175 | 3.6 – 2.7 | 1–6 / 1–5 | 21% | MIN -1.5 42% | 6.3 | Jesper Wallstedt (expected) / Dustin Wolf (expected) | – | no line yet (model fair CGY +1.5 -135 / MIN -1.5 +135) | no line yet | no line yet |
| 9:00 PM | ANA @ COL | ANA 3, COL 4 | COL 60% | ANA +150 / COL -150 | 3.1 – 3.8 | 1–6 / 1–6 | 20% | COL -1.5 39% | 6.9 | Lukas Dostal (expected) / Scott Wedgewood (expected) | – | no line yet (model fair COL -1.5 +155 / ANA +1.5 -155) | no line yet | no line yet |
| 9:40 PM | VAN @ SEA | VAN 3, SEA 4 | SEA 62% | VAN +165 / SEA -165 | 3.0 – 3.8 | 1–5 / 1–6 | 20% | SEA -1.5 41% | 6.8 | Leevi Meriläinen (expected) / Philipp Grubauer (expected) | – | no line yet (model fair SEA -1.5 +140 / VAN +1.5 -140) | no line yet | no line yet |
| 10:00 PM | DAL @ VGK | DAL 2, VGK 3 | VGK 50% | DAL +100 / VGK -100 | 2.9 – 2.9 | 1–5 / 1–5 | 23% | VGK -1.5 29% | 5.9 | Jake Oettinger (expected) / Carter Hart (expected) | – | no line yet (model fair VGK -1.5 +245 / DAL +1.5 -245) | no line yet | no line yet |

\* price not posted; assumed -110.

## How the 2026-27 predictions have done

| Predictor | Games | Log loss | Brier | Winners | Goals MAE | Total MAE | 80% range hit |
|---|---|---|---|---|---|---|---|
| Final prediction | 332 | 0.6544 | 0.2312 | 62.7% | 1.38 | 1.82 | 90.1% |
| Model only (before blending) | 332 | 0.6580 | 0.2330 | 60.5% | – | – | – |
| Elo | 332 | 0.6681 | 0.2377 | 58.7% | – | – | – |
| Final prediction, games with a line | 198 | 0.6590 | 0.2333 | 61.1% | 1.37 | 1.86 | 90.4% |
| Model only, games with a line | 198 | 0.6650 | 0.2363 | 57.6% | – | – | – |
| Betting market (de-vigged moneyline) | 198 | 0.6559 | 0.2319 | 61.6% | – | 1.85 | – |

Log loss and Brier score the win chances (lower is better; a coin flip scores 0.693 and 0.250). Hockey is close to a coin flip, so differences in the third decimal matter, and only over hundreds of games. Goals MAE is the average miss on each team's goals.

Overtime: predicted in 21.5% of regular-season games, happened in 22.3%.

134 of these games were played before the predictor went live. They are backfilled walk-forward (each day predicted from earlier days only) with the actual starting goalies and no betting line. Every game since is graded on the prediction logged before puck drop.

### Betting edges

| Market | Edges | Record (W-L-P) | Staked | Units won | ROI | Expected ROI |
|---|---|---|---|---|---|---|
| Puck line | 4 | 0-4-0 | 3.9 | -3.91 | -100.0% | +8.2% |
| Moneyline | 11 | 6-5-0 | 12.3 | +3.56 | +28.8% | +5.9% |
| Total | 2 | 1-1-0 | 1.7 | +0.04 | +2.4% | +3.4% |

Moneyline moved toward the model's edge on the first line seen before puck drop: 36 of 47 games (77%).

Each edge at the stake and price logged with the last prediction before puck drop (edges logged before edges were priced from the final prediction are left out); pushes return the stake. Units are 1% of the bankroll; ROI is units won per unit staked, and expected ROI is what the edges' EVs promised. The moneyline moving toward the model's edge (closing line value) is the quickest sign that it knows something the market doesn't yet.

### Results, Monday, November 16

| Game | Predicted | Final | Win chance for winner | Inside 80% ranges | Goalies |
|---|---|---|---|---|---|
| MTL @ NYR | 3–2 | 1–3 | 50% | yes | Jacob Fowler / Joonas Korpisalo |
| VAN @ UTA | 3–4 | 3–2 | 23% | yes | Nikita Tolopilo / Karel Vejmelka |

## Power ratings

Goals per game better than an average team, from the goal-rate model: offense and defense combine 5-on-5 expected goals (score and venue adjusted), special teams and actual goals, each weighted against a preseason prior. Defense is positive when it holds opponents below average. Goaltending is rated separately below.

| # | Team | Net | Offense | Defense | 5v5 xGF/60 | 5v5 xGA/60 | PP xGF/60 | PK xGA/60 | Elo |
|---|---|---|---|---|---|---|---|---|---|
| 1 | CAR | +0.83 | +0.50 | +0.33 | 3.47 | 2.30 | 8.70 | 7.13 | 1593 |
| 2 | TBL | +0.43 | +0.21 | +0.22 | 2.93 | 2.41 | 8.05 | 7.97 | 1549 |
| 3 | UTA | +0.39 | +0.24 | +0.15 | 3.16 | 2.44 | 8.20 | 8.99 | 1492 |
| 4 | DAL | +0.26 | -0.03 | +0.29 | 2.64 | 2.34 | 9.43 | 7.49 | 1526 |
| 5 | COL | +0.25 | +0.24 | +0.02 | 2.88 | 2.71 | 8.16 | 7.91 | 1557 |
| 6 | VGK | +0.25 | +0.06 | +0.19 | 2.71 | 2.46 | 9.24 | 7.27 | 1527 |
| 7 | PIT | +0.24 | +0.16 | +0.08 | 2.99 | 2.54 | 7.70 | 7.92 | 1484 |
| 8 | MIN | +0.24 | +0.09 | +0.16 | 2.83 | 2.54 | 9.02 | 8.09 | 1563 |
| 9 | NJD | +0.17 | +0.03 | +0.14 | 2.76 | 2.49 | 9.18 | 7.91 | 1531 |
| 10 | OTT | +0.15 | -0.02 | +0.17 | 2.68 | 2.47 | 7.92 | 8.12 | 1526 |
| 11 | STL | +0.13 | +0.00 | +0.12 | 2.71 | 2.55 | 7.21 | 8.07 | 1496 |
| 12 | FLA | +0.12 | -0.03 | +0.15 | 2.54 | 2.51 | 9.60 | 7.60 | 1510 |
| 13 | BOS | +0.10 | +0.09 | +0.01 | 2.84 | 2.71 | 7.58 | 8.23 | 1530 |
| 14 | WSH | +0.10 | +0.16 | -0.06 | 2.97 | 2.75 | 7.79 | 8.15 | 1508 |
| 15 | NYR | +0.08 | +0.02 | +0.06 | 2.71 | 2.64 | 8.87 | 7.70 | 1507 |
| 16 | BUF | +0.05 | +0.08 | -0.04 | 2.80 | 2.71 | 7.96 | 8.36 | 1502 |
| 17 | EDM | +0.03 | +0.03 | -0.00 | 2.48 | 2.70 | 9.73 | 8.34 | 1543 |
| 18 | LAK | +0.02 | -0.12 | +0.13 | 2.56 | 2.53 | 8.22 | 8.06 | 1457 |
| 19 | MTL | -0.04 | +0.03 | -0.08 | 2.77 | 2.81 | 7.61 | 8.55 | 1530 |
| 20 | NSH | -0.08 | -0.01 | -0.07 | 2.74 | 2.79 | 8.15 | 7.69 | 1505 |
| 21 | WPG | -0.08 | -0.08 | -0.00 | 2.55 | 2.70 | 8.54 | 8.82 | 1488 |
| 22 | DET | -0.09 | -0.10 | +0.00 | 2.65 | 2.67 | 8.64 | 8.69 | 1479 |
| 23 | CBJ | -0.11 | -0.04 | -0.07 | 2.71 | 2.76 | 7.86 | 8.64 | 1481 |
| 24 | NYI | -0.12 | -0.03 | -0.09 | 2.72 | 2.84 | 7.49 | 8.66 | 1493 |
| 25 | TOR | -0.13 | -0.07 | -0.06 | 2.46 | 2.75 | 8.62 | 8.46 | 1461 |
| 26 | PHI | -0.18 | -0.22 | +0.04 | 2.40 | 2.63 | 7.77 | 7.73 | 1468 |
| 27 | CGY | -0.30 | -0.14 | -0.16 | 2.53 | 2.88 | 7.20 | 7.80 | 1456 |
| 28 | ANA | -0.31 | +0.03 | -0.34 | 2.73 | 3.05 | 8.01 | 8.34 | 1489 |
| 29 | SEA | -0.37 | -0.16 | -0.21 | 2.35 | 2.93 | 7.21 | 8.77 | 1470 |
| 30 | CHI | -0.64 | -0.30 | -0.33 | 2.23 | 3.03 | 7.27 | 8.48 | 1417 |
| 31 | VAN | -0.71 | -0.23 | -0.48 | 2.26 | 3.19 | 7.80 | 8.80 | 1406 |
| 32 | SJS | -0.76 | -0.23 | -0.53 | 2.33 | 3.27 | 7.38 | 9.36 | 1455 |

## Goalies

Each team's likeliest next starter. GSAx is goals saved above expected (from this predictor's own shot model), shrunk hard toward a slightly below-average prior, since goaltending repeats poorly from season to season.

| Team | Likely next starter | Share of recent starts | GSAx per 100 shots | Goals per game vs average |
|---|---|---|---|---|
| NYI | Ilya Sorokin | 66% | +0.41 | +0.17 |
| WSH | Logan Thompson | 72% | +0.34 | +0.14 |
| MIN | Jesper Wallstedt | 86% | +0.33 | +0.14 |
| MTL | Jacob Fowler | 67% | +0.30 | +0.13 |
| BOS | Jeremy Swayman | 76% | +0.26 | +0.11 |
| COL | Mackenzie Blackwood | 71% | +0.21 | +0.09 |
| NJD | Connor Hellebuyck | 47% | +0.16 | +0.07 |
| TBL | Andrei Vasilevskiy | 73% | +0.14 | +0.06 |
| CGY | Devin Cooley | 49% | +0.14 | +0.06 |
| OTT | Linus Ullmark | 42% | +0.14 | +0.06 |
| STL | Joel Hofer | 79% | +0.11 | +0.05 |
| DAL | Jake Oettinger | 73% | +0.08 | +0.03 |
| CBJ | Jet Greaves | 56% | +0.05 | +0.02 |
| CAR | Pyotr Kochetkov | 65% | +0.03 | +0.01 |
| CHI | Spencer Knight | 82% | +0.01 | +0.01 |
| NYR | Dylan Garand | 60% | +0.00 | +0.00 |
| WPG | Stuart Skinner | 74% | -0.07 | -0.03 |
| NSH | Juuse Saros | 70% | -0.09 | -0.04 |
| PHI | Dan Vladar | 55% | -0.12 | -0.05 |
| VGK | Carter Hart | 53% | -0.17 | -0.07 |
| BUF | Ukko-Pekka Luukkonen | 48% | -0.17 | -0.07 |
| SJS | Yaroslav Askarov | 65% | -0.18 | -0.08 |
| EDM | Tristan Jarry | 48% | -0.19 | -0.08 |
| UTA | Karel Vejmelka | 68% | -0.19 | -0.08 |
| TOR | Sergei Bobrovsky | 54% | -0.20 | -0.08 |
| DET | John Gibson | 57% | -0.21 | -0.09 |
| FLA | Jacob Markstrom | 48% | -0.22 | -0.09 |
| SEA | Joey Daccord | 51% | -0.23 | -0.10 |
| ANA | Lukas Dostal | 43% | -0.27 | -0.11 |
| LAK | Darcy Kuemper | 57% | -0.28 | -0.12 |
| VAN | Leevi Meriläinen | 68% | -0.37 | -0.16 |
| PIT | Arturs Silovs | 55% | -0.40 | -0.17 |

## Current model fit

- Fitted on 5924 games from 2022-23 to 2026-27.
- Home ice: +2.7% goals for the home team relative to the visitor.
- Second night of a back-to-back: -6.0% goals scored, +3.3% goals allowed.
- Starting goalie: each goal per game he saves above average lowers the opponent's rate by 21%.
- Blend: 53% on the betting line wherever there is one (fitted on 198 logged games, shrunk toward the backtest value).
- Simulator: 22.3% of recent regular-season games reached overtime; trailing teams usually have the goalie pulled with 2 minutes left when down one and 3 when down two; empty-net goals come at 0.40 a minute with the net empty; three-on-three overtime produces 1.03 goals per five minutes.
