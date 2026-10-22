# NHL score predictions

Updated Thu Oct 22, 2026 01:30 AM ET. Refreshed automatically several times a day during the season; each game's prediction is locked at puck drop and graded once the final score is in.

Each game is simulated 10,000 times minute by minute, with pulled goalies, empty-net goals, overtime and shootouts. The predicted score is the most common final score in which the likelier winner wins; as in the official result, a shootout winner gets one extra goal. Hockey is low-scoring and luck-heavy, so read the win chance and the ranges (80% of simulated outcomes for each team) before the single score.

Goalies marked with a percentage are projected from recent starts (the share is the chance he starts); "probable" or "confirmed" ones come from ESPN and replace the projection when available.

The fair moneyline is the American odds that match the win chance exactly, with no bookmaker margin: -150 means risk $150 to win $100, +150 means risk $100 to win $150. A sportsbook's price is a little worse on both sides because of its cut, so a book only offers value on a team when its price beats the fair line. The puck line is the favorite's chance to win by two or more.

The edge columns price each side of the puck line, moneyline and total with the model's own numbers, before they are blended with the betting line, and show the side with the best expected value (EV) per $1 bet at the posted price, overtime and shootout included (the shootout winner gets one goal). A side is an edge only if its EV is at least 3%: a pick shows its price, EV and the model's chance of winning the bet; "no edge" means neither side clears the bar. A total with no posted price is assumed to be -110 (marked \*); the puck line and moneyline are never assumed, so without a price the cell shows the model's fair odds instead. Treat the edges as an experiment: no free source has a history of NHL lines, so they could not be backtested against the market, and the backtest's margins are thin (the model beats Elo by 0.0035 log loss per game, small next to a sportsbook's cut). Their record is tracked live below.

## Thursday, October 22

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected goals | 80% range | Overtime | Puck line | Total: model / line | Goalies | Posted moneyline | Puck line edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 7:00 PM | NSH @ BOS | NSH 2, BOS 3 | BOS 58% | NSH +140 / BOS -140 | 2.8 – 3.3 | 1–5 / 1–6 | 22% | BOS -1.5 36% | 6.1 / 5.5 (over 54%) | Juuse Saros (expected) / Jeremy Swayman (expected) | NSH +130 / BOS -155 | no edge | no edge | no edge |
| 7:00 PM | NYR @ TOR | NYR 4, TOR 3 | NYR 51% | NYR -100 / TOR +100 | 3.2 – 3.2 | 1–6 / 1–6 | 21% | NYR -1.5 30% | 6.4 / 6.5 (over 49%) | Dylan Garand (expected) / Sergei Bobrovsky (expected) | NYR -112 / TOR -108 | no edge | no edge | no edge |
| 7:00 PM | SJS @ OTT | SJS 3, OTT 4 | OTT 56% | SJS +130 / OTT -130 | 3.0 – 3.4 | 1–5 / 1–6 | 22% | OTT -1.5 34% | 6.3 / 6.5 (over 47%) | Yaroslav Askarov (expected) / Samuel Ersson (expected) | SJS +114 / OTT -135 | no edge | no edge | no edge |
| 7:00 PM | ANA @ NJD | ANA 3, NJD 4 | NJD 63% | ANA +175 / NJD -175 | 2.9 – 3.7 | 1–5 / 1–6 | 21% | NJD -1.5 42% | 6.6 / 6.5 (over 51%) | Lukas Dostal (expected) / Jake Allen (expected) | ANA +164 / NJD -198 | no edge | no edge | no edge |
| 7:00 PM | FLA @ PIT | FLA 3, PIT 4 | PIT 53% | FLA +115 / PIT -115 | 3.2 – 3.4 | 1–6 / 1–6 | 21% | PIT -1.5 33% | 6.6 / 6.5 (over 52%) | Jacob Markstrom (65%?) / Sergei Murashov (expected) | FLA -105 / PIT -115 | PIT -1.5 (+205): EV +3.2%, model 34% | PIT (-115): EV +4.2%, model 56% | Under 6.5 (+120): EV +17.0%, model 53% |
| 7:30 PM | LAK @ NYI | LAK 2, NYI 3 | NYI 52% | LAK +110 / NYI -110 | 2.8 – 2.9 | 1–5 / 1–5 | 23% | NYI -1.5 30% | 5.7 / 5.5 (over 47%) | Darcy Kuemper (expected) / Ilya Sorokin (expected) | LAK -105 / NYI -115 | NYI -1.5 (+230): EV +3.9%, model 31% | no edge | no edge |
| 8:00 PM | VGK @ STL | VGK 3, STL 2 | VGK 51% | VGK -105 / STL +105 | 3.1 – 3.0 | 1–5 / 1–5 | 23% | VGK -1.5 29% | 6.1 / 6.5 (over 44%) | Carter Hart (expected) / Joel Hofer (expected) | VGK -120 / STL +100 | no edge | no edge | no edge |
| 8:00 PM | WPG @ DAL | WPG 2, DAL 3 | DAL 62% | WPG +160 / DAL -160 | 2.6 – 3.3 | 1–5 / 1–6 | 22% | DAL -1.5 39% | 5.9 / 5.5 (over 51%) | Stuart Skinner (expected) / Jake Oettinger (expected) | WPG +170 / DAL -205 | WPG +1.5 (-155): EV +4.2%, model 63% | WPG (+170): EV +11.1%, model 41% | no edge |
| 9:00 PM | MIN @ CGY | MIN 4, CGY 3 | MIN 63% | MIN -170 / CGY +170 | 3.6 – 2.7 | 1–6 / 1–5 | 22% | MIN -1.5 41% | 6.3 / 5.5 (over 58%) | Jesper Wallstedt (expected) / Dustin Wolf (expected) | MIN -205 / CGY +170 | no edge | CGY (+170): EV +3.8%, model 38% | Over 5.5 (-130): EV +5.5%, model 60% |
| 9:00 PM | CAR @ EDM | CAR 4, EDM 3 | CAR 54% | CAR -115 / EDM +115 | 3.4 – 3.2 | 1–6 / 1–6 | 21% | CAR -1.5 34% | 6.6 / 6.5 (over 51%) | Brandon Bussi (expected) / Devon Levi (expected) | CAR -118 / EDM -102 | CAR -1.5 (+205): EV +13.9%, model 37% | CAR (-118): EV +6.4%, model 58% | no edge |
| 10:00 PM | UTA @ SEA | UTA 4, SEA 3 | UTA 62% | UTA -160 / SEA +160 | 3.6 – 2.8 | 1–6 / 1–5 | 21% | UTA -1.5 40% | 6.5 / 6.5 (over 49%) | Karel Vejmelka (expected) / Joey Daccord (expected) | UTA -162 / SEA +136 | UTA -1.5 (+150): EV +5.7%, model 42% | no edge | no edge |
| 10:00 PM | DET @ VAN | DET 4, VAN 3 | DET 62% | DET -160 / VAN +160 | 3.7 – 2.9 | 1–6 / 1–5 | 21% | DET -1.5 40% | 6.5 / 6.5 (over 50%) | John Gibson (expected) / Kevin Lankinen (expected) | DET -170 / VAN +142 | no edge | no edge | no edge |

## Friday, October 23

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected goals | 80% range | Overtime | Puck line | Total: model / line | Goalies | Posted moneyline | Puck line edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 8:00 PM | MTL @ CHI | MTL 4, CHI 3 | MTL 62% | MTL -160 / CHI +160 | 3.6 – 2.8 | 1–6 / 1–5 | 21% | MTL -1.5 40% | 6.4 | Jakub Dobes (expected) / Spencer Knight (expected) | – | no line yet (model fair CHI +1.5 -150 / MTL -1.5 +150) | no line yet | no line yet |
| 9:00 PM | TBL @ COL | TBL 3, COL 4 | COL 50% | TBL +100 / COL -100 | 3.2 – 3.2 | 1–6 / 1–6 | 22% | COL -1.5 30% | 6.3 | Andrei Vasilevskiy (expected) / Mackenzie Blackwood (expected) | – | no line yet (model fair COL -1.5 +240 / TBL +1.5 -240) | no line yet | no line yet |

## Saturday, October 24

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected goals | 80% range | Overtime | Puck line | Total: model / line | Goalies | Posted moneyline | Puck line edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1:00 PM | ANA @ PHI | ANA 3, PHI 4 | PHI 50% | ANA +100 / PHI -100 | 3.1 – 3.2 | 1–6 / 1–6 | 21% | PHI -1.5 30% | 6.3 | Lukas Dostal (expected) / Joseph Woll (expected) | – | no line yet (model fair PHI -1.5 +230 / ANA +1.5 -230) | no line yet | no line yet |
| 3:30 PM | LAK @ NJD | LAK 2, NJD 3 | NJD 56% | LAK +125 / NJD -125 | 2.7 – 3.0 | 1–5 / 1–5 | 23% | NJD -1.5 33% | 5.8 | Darcy Kuemper (expected) / Jake Allen (expected) | – | no line yet (model fair NJD -1.5 +205 / LAK +1.5 -205) | no line yet | no line yet |
| 7:00 PM | SJS @ BOS | SJS 3, BOS 4 | BOS 67% | SJS +200 / BOS -200 | 2.6 – 3.7 | 1–5 / 1–6 | 20% | BOS -1.5 45% | 6.3 | Yaroslav Askarov (expected) / Jeremy Swayman (expected) | – | no line yet (model fair BOS -1.5 +125 / SJS +1.5 -125) | no line yet | no line yet |
| 7:00 PM | NYR @ OTT | NYR 2, OTT 3 | OTT 54% | NYR +120 / OTT -120 | 2.8 – 3.1 | 1–5 / 1–5 | 23% | OTT -1.5 32% | 5.9 | Dylan Garand (expected) / Linus Ullmark (expected) | – | no line yet (model fair OTT -1.5 +215 / NYR +1.5 -215) | no line yet | no line yet |
| 7:00 PM | NSH @ PIT | NSH 3, PIT 4 | PIT 59% | NSH +145 / PIT -145 | 3.0 – 3.5 | 1–5 / 1–6 | 21% | PIT -1.5 37% | 6.5 | Juuse Saros (expected) / Arturs Silovs (expected) | – | no line yet (model fair PIT -1.5 +165 / NSH +1.5 -165) | no line yet | no line yet |
| 7:00 PM | BUF @ WSH | BUF 3, WSH 4 | WSH 54% | BUF +115 / WSH -115 | 3.1 – 3.3 | 1–5 / 1–6 | 22% | WSH -1.5 33% | 6.4 | Ukko-Pekka Luukkonen (expected) / Logan Thompson (expected) | – | no line yet (model fair WSH -1.5 +205 / BUF +1.5 -205) | no line yet | no line yet |
| 7:00 PM | VGK @ CBJ | VGK 3, CBJ 2 | VGK 54% | VGK -115 / CBJ +115 | 3.2 – 2.9 | 1–6 / 1–5 | 22% | VGK -1.5 33% | 6.1 | Carter Hart (expected) / Jet Greaves (expected) | – | no line yet (model fair CBJ +1.5 -205 / VGK -1.5 +205) | no line yet | no line yet |
| 7:00 PM | CAR @ STL | CAR 4, STL 3 | CAR 58% | CAR -140 / STL +140 | 3.4 – 2.9 | 1–6 / 1–5 | 22% | CAR -1.5 37% | 6.3 | Brandon Bussi (expected) / Joel Hofer (expected) | – | no line yet (model fair STL +1.5 -175 / CAR -1.5 +175) | no line yet | no line yet |
| 7:00 PM | TOR @ EDM | TOR 3, EDM 4 | EDM 61% | TOR +155 / EDM -155 | 3.0 – 3.7 | 1–5 / 1–6 | 21% | EDM -1.5 40% | 6.7 | Sergei Bobrovsky (expected) / Devon Levi (expected) | – | no line yet (model fair EDM -1.5 +150 / TOR +1.5 -150) | no line yet | no line yet |
| 9:00 PM | TBL @ UTA | TBL 3, UTA 4 | UTA 57% | TBL +135 / UTA -135 | 2.9 – 3.4 | 1–5 / 1–6 | 22% | UTA -1.5 35% | 6.2 | Dennis Hildeby (expected) / Karel Vejmelka (expected) | – | no line yet (model fair UTA -1.5 +180 / TBL +1.5 -180) | no line yet | no line yet |
| 10:00 PM | DET @ CGY | DET 4, CGY 3 | DET 51% | DET -105 / CGY +105 | 3.2 – 3.2 | 1–6 / 1–6 | 22% | DET -1.5 31% | 6.4 | Daniil Tarasov (expected) / Dustin Wolf (expected) | – | no line yet (model fair CGY +1.5 -225 / DET -1.5 +225) | no line yet | no line yet |
| 10:00 PM | MIN @ SEA | MIN 4, SEA 3 | MIN 61% | MIN -160 / SEA +160 | 3.6 – 2.9 | 1–6 / 1–5 | 21% | MIN -1.5 41% | 6.5 | Jesper Wallstedt (expected) / Joey Daccord (expected) | – | no line yet (model fair SEA +1.5 -145 / MIN -1.5 +145) | no line yet | no line yet |

## How the 2026-27 predictions have done

| Predictor | Games | Log loss | Brier | Winners | Goals MAE | Total MAE | 80% range hit |
|---|---|---|---|---|---|---|---|
| Final prediction | 151 | 0.6542 | 0.2311 | 63.6% | 1.37 | 1.72 | 90.1% |
| Model only (before blending) | 151 | 0.6538 | 0.2309 | 63.6% | – | – | – |
| Elo | 151 | 0.6639 | 0.2356 | 62.9% | – | – | – |
| Final prediction, games with a line | 17 | 0.6851 | 0.2457 | 58.8% | 1.14 | 1.50 | 94.1% |
| Model only, games with a line | 17 | 0.6810 | 0.2439 | 58.8% | – | – | – |
| Betting market (de-vigged moneyline) | 17 | 0.6896 | 0.2478 | 58.8% | – | 1.44 | – |

Log loss and Brier score the win chances (lower is better; a coin flip scores 0.693 and 0.250). Hockey is close to a coin flip, so differences in the third decimal matter, and only over hundreds of games. Goals MAE is the average miss on each team's goals.

Overtime: predicted in 21.7% of regular-season games, happened in 23.2%.

134 of these games were played before the predictor went live. They are backfilled walk-forward (each day predicted from earlier days only) with the actual starting goalies and no betting line. Every game since is graded on the prediction logged before puck drop.

### Betting edges

| Market | Edges | Record (W-L-P) | Units | ROI |
|---|---|---|---|---|
| Puck line | 3 | 1-2-0 | -1.44 | -48.1% |
| Moneyline | 1 | 0-1-0 | -1.00 | -100.0% |
| Total | 4 | 1-3-0 | -2.05 | -51.2% |

Moneyline moved toward the model's edge on the first line seen before puck drop: 2 of 3 games (67%).

One unit on each edge at the price logged with the last prediction before puck drop; pushes return the stake. The moneyline moving toward the model's edge (closing line value) is the quickest sign that it knows something the market doesn't yet.

### Results, Tuesday, October 20

| Game | Predicted | Final | Win chance for winner | Inside 80% ranges | Goalies |
|---|---|---|---|---|---|
| SJS @ MTL | 3–4 | 4–3 (OT) | 32% | yes | Alex Nedeljkovic / Jakub Dobes |
| COL @ NJD | 3–4 | 3–4 | 54% | yes | Scott Wedgewood / Jake Allen |
| ANA @ NYI | 2–3 | 2–3 | 60% | yes | Lukas Dostal / Ilya Sorokin |
| LAK @ WSH | 2–3 | 5–2 | 43% | yes | Darcy Kuemper / Logan Thompson |
| TOR @ CBJ | 3–4 | 6–2 | 40% | no | Anthony Stolarz / Jet Greaves |
| WPG @ STL | 2–3 | 1–2 | 57% | yes | Stuart Skinner / Joel Hofer |
| BOS @ DAL | 2–3 | 2–3 (OT) | 58% | yes | Jeremy Swayman / Jake Oettinger |
| MIN @ EDM | 2–3 | 3–4 (OT) | 55% | yes | Jesper Wallstedt / Devon Levi |
| DET @ SEA | 4–3 | 3–4 (SO) | 49% | yes | Daniil Tarasov / Philipp Grubauer |
| CAR @ VAN | 4–3 | 6–3 | 72% | yes | Pyotr Kochetkov / Leevi Meriläinen |
| TBL @ VGK | 2–3 | 6–2 | 49% | no | Andrei Vasilevskiy / Carter Hart |

## Power ratings

Goals per game better than an average team, from the goal-rate model: offense and defense combine 5-on-5 expected goals (score and venue adjusted), special teams and actual goals, each weighted against a preseason prior. Defense is positive when it holds opponents below average. Goaltending is rated separately below.

| # | Team | Net | Offense | Defense | 5v5 xGF/60 | 5v5 xGA/60 | PP xGF/60 | PK xGA/60 | Elo |
|---|---|---|---|---|---|---|---|---|---|
| 1 | CAR | +0.63 | +0.41 | +0.22 | 3.44 | 2.47 | 7.96 | 6.42 | 1573 |
| 2 | UTA | +0.49 | +0.27 | +0.21 | 3.21 | 2.40 | 7.88 | 7.92 | 1518 |
| 3 | TBL | +0.31 | +0.15 | +0.16 | 2.88 | 2.53 | 7.65 | 7.65 | 1545 |
| 4 | FLA | +0.30 | +0.06 | +0.25 | 2.75 | 2.41 | 8.92 | 7.26 | 1505 |
| 5 | VGK | +0.30 | +0.09 | +0.21 | 2.74 | 2.46 | 8.61 | 7.12 | 1538 |
| 6 | COL | +0.28 | +0.26 | +0.01 | 2.99 | 2.74 | 7.51 | 7.60 | 1547 |
| 7 | MIN | +0.26 | +0.13 | +0.13 | 3.01 | 2.57 | 8.51 | 8.04 | 1531 |
| 8 | PIT | +0.23 | +0.22 | +0.02 | 3.05 | 2.67 | 7.87 | 7.62 | 1492 |
| 9 | NJD | +0.21 | +0.06 | +0.16 | 2.95 | 2.49 | 8.51 | 7.55 | 1492 |
| 10 | DAL | +0.16 | -0.07 | +0.23 | 2.54 | 2.46 | 8.97 | 7.12 | 1531 |
| 11 | LAK | +0.14 | -0.13 | +0.26 | 2.53 | 2.37 | 7.58 | 7.64 | 1467 |
| 12 | BUF | +0.12 | +0.07 | +0.05 | 2.74 | 2.63 | 7.32 | 7.95 | 1519 |
| 13 | EDM | +0.11 | +0.16 | -0.05 | 2.72 | 2.76 | 9.26 | 8.11 | 1528 |
| 14 | STL | +0.09 | -0.04 | +0.13 | 2.57 | 2.55 | 6.87 | 7.25 | 1503 |
| 15 | OTT | +0.04 | -0.09 | +0.13 | 2.56 | 2.55 | 7.61 | 7.64 | 1520 |
| 16 | NYR | +0.03 | -0.00 | +0.03 | 2.68 | 2.71 | 8.25 | 7.42 | 1507 |
| 17 | NYI | -0.01 | -0.09 | +0.08 | 2.65 | 2.65 | 7.37 | 8.58 | 1497 |
| 18 | CBJ | -0.03 | -0.03 | -0.00 | 2.74 | 2.69 | 7.44 | 8.36 | 1487 |
| 19 | WSH | -0.04 | +0.09 | -0.14 | 2.88 | 2.90 | 7.53 | 8.01 | 1514 |
| 20 | MTL | -0.07 | +0.05 | -0.12 | 2.88 | 2.86 | 6.98 | 8.18 | 1514 |
| 21 | WPG | -0.08 | -0.07 | -0.01 | 2.66 | 2.76 | 7.75 | 7.83 | 1484 |
| 22 | BOS | -0.10 | -0.02 | -0.07 | 2.62 | 2.85 | 7.59 | 7.88 | 1527 |
| 23 | DET | -0.11 | -0.10 | -0.01 | 2.65 | 2.72 | 8.23 | 8.29 | 1478 |
| 24 | NSH | -0.13 | -0.11 | -0.02 | 2.54 | 2.74 | 7.59 | 7.51 | 1485 |
| 25 | TOR | -0.18 | -0.02 | -0.15 | 2.53 | 2.90 | 8.42 | 8.11 | 1478 |
| 26 | CGY | -0.25 | -0.05 | -0.20 | 2.74 | 2.94 | 7.10 | 7.70 | 1453 |
| 27 | SEA | -0.28 | -0.06 | -0.22 | 2.56 | 2.98 | 7.13 | 8.08 | 1484 |
| 28 | ANA | -0.30 | +0.02 | -0.31 | 2.89 | 3.05 | 7.41 | 8.16 | 1482 |
| 29 | PHI | -0.40 | -0.33 | -0.06 | 2.18 | 2.79 | 7.69 | 7.11 | 1476 |
| 30 | SJS | -0.47 | -0.20 | -0.27 | 2.42 | 2.99 | 7.21 | 8.48 | 1464 |
| 31 | VAN | -0.66 | -0.19 | -0.46 | 2.33 | 3.22 | 7.45 | 8.32 | 1422 |
| 32 | CHI | -0.66 | -0.27 | -0.39 | 2.31 | 3.13 | 6.81 | 8.07 | 1440 |

## Goalies

Each team's likeliest next starter. GSAx is goals saved above expected (from this predictor's own shot model), shrunk hard toward a slightly below-average prior, since goaltending repeats poorly from season to season.

| Team | Likely next starter | Share of recent starts | GSAx per 100 shots | Goals per game vs average |
|---|---|---|---|---|
| NYI | Ilya Sorokin | 78% | +0.47 | +0.20 |
| WSH | Logan Thompson | 79% | +0.46 | +0.19 |
| BOS | Jeremy Swayman | 80% | +0.36 | +0.15 |
| TBL | Andrei Vasilevskiy | 76% | +0.24 | +0.10 |
| MTL | Jakub Dobes | 54% | +0.17 | +0.07 |
| DAL | Jake Oettinger | 79% | +0.17 | +0.07 |
| MIN | Jesper Wallstedt | 89% | +0.14 | +0.06 |
| OTT | Linus Ullmark | 78% | +0.12 | +0.05 |
| COL | Mackenzie Blackwood | 67% | +0.12 | +0.05 |
| CBJ | Jet Greaves | 61% | +0.11 | +0.05 |
| NYR | Dylan Garand | 62% | +0.07 | +0.03 |
| CHI | Spencer Knight | 81% | +0.06 | +0.02 |
| WPG | Stuart Skinner | 67% | +0.01 | +0.00 |
| STL | Joel Hofer | 67% | +0.00 | +0.00 |
| EDM | Devon Levi | 67% | -0.01 | -0.00 |
| PHI | Joseph Woll | 55% | -0.04 | -0.02 |
| NJD | Jake Allen | 68% | -0.07 | -0.03 |
| DET | John Gibson | 62% | -0.08 | -0.03 |
| SEA | Philipp Grubauer | 54% | -0.08 | -0.03 |
| TOR | Sergei Bobrovsky | 64% | -0.09 | -0.04 |
| CAR | Pyotr Kochetkov | 58% | -0.11 | -0.05 |
| UTA | Karel Vejmelka | 69% | -0.12 | -0.05 |
| ANA | Lukas Dostal | 75% | -0.13 | -0.05 |
| VGK | Carter Hart | 63% | -0.18 | -0.07 |
| BUF | Ukko-Pekka Luukkonen | 67% | -0.19 | -0.08 |
| LAK | Darcy Kuemper | 71% | -0.22 | -0.09 |
| NSH | Juuse Saros | 87% | -0.25 | -0.11 |
| VAN | Leevi Meriläinen | 50% | -0.26 | -0.11 |
| FLA | Jacob Markstrom | 65% | -0.26 | -0.11 |
| CGY | Dustin Wolf | 61% | -0.28 | -0.12 |
| SJS | Yaroslav Askarov | 55% | -0.33 | -0.14 |
| PIT | Arturs Silovs | 59% | -0.36 | -0.15 |

## Current model fit

- Fitted on 5743 games from 2022-23 to 2026-27.
- Home ice: +3.0% goals for the home team relative to the visitor.
- Second night of a back-to-back: -5.7% goals scored, +3.3% goals allowed.
- Starting goalie: each goal per game he saves above average lowers the opponent's rate by 23%.
- Blend: 48% on the betting line wherever there is one (fitted on 17 logged games, shrunk toward an even split).
- Simulator: 22.3% of recent regular-season games reached overtime; trailing teams usually have the goalie pulled with 2 minutes left when down one and 3 when down two; empty-net goals come at 0.40 a minute with the net empty; three-on-three overtime produces 1.03 goals per five minutes.
