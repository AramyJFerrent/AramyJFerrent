# NHL score predictions

Updated Tue Oct 20, 2026 09:43 AM ET. Refreshed automatically several times a day during the season; each game's prediction is locked at puck drop and graded once the final score is in.

Each game is simulated 10,000 times minute by minute, with pulled goalies, empty-net goals, overtime and shootouts. The predicted score is the most common final score in which the likelier winner wins; as in the official result, a shootout winner gets one extra goal. Hockey is low-scoring and luck-heavy, so read the win chance and the ranges (80% of simulated outcomes for each team) before the single score.

Goalies marked with a percentage are projected from recent starts (the share is the chance he starts); "probable" or "confirmed" ones come from ESPN and replace the projection when available.

The fair moneyline is the American odds that match the win chance exactly, with no bookmaker margin: -150 means risk $150 to win $100, +150 means risk $100 to win $150. A sportsbook's price is a little worse on both sides because of its cut, so a book only offers value on a team when its price beats the fair line. The puck line is the favorite's chance to win by two or more.

The edge columns price each side of the puck line, moneyline and total with the model's own numbers, before they are blended with the betting line, and show the side with the best expected value (EV) per $1 bet at the posted price, overtime and shootout included (the shootout winner gets one goal). A side is an edge only if its EV is at least 3%: a pick shows its price, EV and the model's chance of winning the bet; "no edge" means neither side clears the bar. A total with no posted price is assumed to be -110 (marked \*); the puck line and moneyline are never assumed, so without a price the cell shows the model's fair odds instead. Treat the edges as an experiment: no free source has a history of NHL lines, so they could not be backtested against the market, and the backtest's margins are thin (the model beats Elo by 0.0035 log loss per game, small next to a sportsbook's cut). Their record is tracked live below.

## Tuesday, October 20

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected goals | 80% range | Overtime | Puck line | Total: model / line | Goalies | Posted moneyline | Puck line edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 7:00 PM | SJS @ MTL | SJS 3, MTL 4 | MTL 66% | SJS +190 / MTL -190 | 2.7 – 3.8 | 1–5 / 1–6 | 20% | MTL -1.5 45% | 6.5 / 6.5 (over 49%) | Alex Nedeljkovic (expected) / Jacob Fowler (expected) | SJS +170 / MTL -205 | no edge | no edge | Under 6.5 (-102): EV +5.8%, model 53% |
| 7:00 PM | COL @ NJD | COL 3, NJD 4 | NJD 52% | COL +110 / NJD -110 | 3.1 – 3.3 | 1–5 / 1–6 | 22% | NJD -1.5 32% | 6.3 / 6.5 (over 47%) | Scott Wedgewood (confirmed) / Jake Allen (expected) | COL -110 / NJD -110 | no edge | no edge | no edge |
| 7:00 PM | ANA @ NYI | ANA 2, NYI 3 | NYI 61% | ANA +155 / NYI -155 | 2.7 – 3.4 | 1–5 / 1–6 | 21% | NYI -1.5 39% | 6.1 / 5.5 (over 54%) | Lukas Dostal (confirmed) / Ilya Sorokin (expected) | ANA +130 / NYI -155 | NYI -1.5 (+160): EV +5.9%, model 41% | no edge | no edge |
| 7:00 PM | LAK @ WSH | LAK 2, WSH 3 | WSH 57% | LAK +135 / WSH -135 | 2.8 – 3.2 | 1–5 / 1–6 | 22% | WSH -1.5 35% | 6.0 / 5.5 (over 52%) | Darcy Kuemper (expected) / Logan Thompson (expected) | LAK +130 / WSH -155 | no edge | no edge | no edge |
| 7:00 PM | TOR @ CBJ | TOR 2, CBJ 3 | CBJ 60% | TOR +150 / CBJ -150 | 2.8 – 3.5 | 1–5 / 1–6 | 21% | CBJ -1.5 39% | 6.3 / 6.5 (over 46%) | Anthony Stolarz (confirmed) / Jet Greaves (expected) | TOR +136 / CBJ -162 | no edge | no edge | no edge |
| 8:00 PM | WPG @ STL | WPG 2, STL 3 | STL 57% | WPG +130 / STL -130 | 2.8 – 3.2 | 1–5 / 1–6 | 22% | STL -1.5 35% | 6.1 / 5.5 (over 54%) | Stuart Skinner (expected) / Joel Hofer (expected) | WPG +124 / STL -148 | no edge | no edge | no edge |
| 8:00 PM | BOS @ DAL | BOS 2, DAL 3 | DAL 58% | BOS +135 / DAL -135 | 2.7 – 3.2 | 1–5 / 1–6 | 22% | DAL -1.5 36% | 5.9 / 5.5 (over 50%) | Jeremy Swayman (expected) / Jake Oettinger (expected) | BOS +142 / DAL -170 | BOS +1.5 (-180): EV +4.1%, model 67% | BOS (+142): EV +8.3%, model 45% | no edge |
| 9:00 PM | MIN @ EDM | MIN 3, EDM 4 | EDM 54% | MIN +115 / EDM -115 | 3.0 – 3.2 | 1–5 / 1–6 | 22% | EDM -1.5 34% | 6.2 / 6.5 (over 45%) | Jesper Wallstedt (expected) / Devon Levi (expected) | MIN +114 / EDM -135 | no edge | no edge | Under 6.5 (-120): EV +5.3%, model 57% |
| 9:40 PM | DET @ SEA | DET 3, SEA 4 | SEA 51% | DET +100 / SEA -100 | 3.2 – 3.3 | 1–6 / 1–6 | 21% | SEA -1.5 31% | 6.5 / 6.5 (over 49%) | Daniil Tarasov (confirmed) / Joey Daccord (expected) | DET -105 / SEA -115 | no edge | no edge | no edge |
| 10:00 PM | CAR @ VAN | CAR 4, VAN 3 | CAR 72% | CAR -250 / VAN +250 | 4.1 – 2.6 | 2–7 / 1–5 | 18% | CAR -1.5 52% | 6.7 / 6.5 (over 52%) | Pyotr Kochetkov (expected) / Leevi Meriläinen (expected) | CAR -298 / VAN +240 | no edge | no edge | Over 6.5 (-108): EV +8.3%, model 56% |
| 10:30 PM | TBL @ VGK | TBL 2, VGK 3 | VGK 52% | TBL +110 / VGK -110 | 3.0 – 3.2 | 1–5 / 1–6 | 23% | VGK -1.5 32% | 6.2 / 6.5 (over 45%) | Andrei Vasilevskiy (expected) / Carter Hart (expected) | TBL -105 / VGK -115 | no edge | no edge | Under 6.5 (-125): EV +3.6%, model 58% |

## Wednesday, October 21

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected goals | 80% range | Overtime | Puck line | Total: model / line | Goalies | Posted moneyline | Puck line edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 7:30 PM | PHI @ BUF | PHI 2, BUF 3 | BUF 62% | PHI +165 / BUF -165 | 2.6 – 3.4 | 1–5 / 1–6 | 21% | BUF -1.5 40% | 6.1 | Dan Vladar (expected) / Ukko-Pekka Luukkonen (expected) | – | no line yet (model fair BUF -1.5 +150 / PHI +1.5 -150) | no line yet | no line yet |
| 7:30 PM | FLA @ OTT | FLA 2, OTT 3 | OTT 50% | FLA +100 / OTT -100 | 2.9 – 2.9 | 1–5 / 1–5 | 23% | OTT -1.5 29% | 5.9 | Jacob Markstrom (expected) / Linus Ullmark (expected) | – | no line yet (model fair OTT -1.5 +245 / FLA +1.5 -245) | no line yet | no line yet |

## Thursday, October 22

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected goals | 80% range | Overtime | Puck line | Total: model / line | Goalies | Posted moneyline | Puck line edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 7:00 PM | NSH @ BOS | NSH 3, BOS 4 | BOS 59% | NSH +145 / BOS -145 | 2.8 – 3.4 | 1–5 / 1–6 | 22% | BOS -1.5 38% | 6.2 | Juuse Saros (expected) / Jeremy Swayman (expected) | – | no line yet (model fair BOS -1.5 +165 / NSH +1.5 -165) | no line yet | no line yet |
| 7:00 PM | NYR @ TOR | NYR 4, TOR 3 | NYR 54% | NYR -115 / TOR +115 | 3.3 – 3.1 | 1–6 / 1–5 | 22% | NYR -1.5 33% | 6.4 | Dylan Garand (expected) / Sergei Bobrovsky (expected) | – | no line yet (model fair TOR +1.5 -200 / NYR -1.5 +200) | no line yet | no line yet |
| 7:00 PM | SJS @ OTT | SJS 3, OTT 4 | OTT 58% | SJS +135 / OTT -135 | 2.9 – 3.4 | 1–5 / 1–6 | 21% | OTT -1.5 36% | 6.3 | Yaroslav Askarov (expected) / Samuel Ersson (expected) | – | no line yet (model fair OTT -1.5 +180 / SJS +1.5 -180) | no line yet | no line yet |
| 7:00 PM | ANA @ NJD | ANA 3, NJD 4 | NJD 60% | ANA +155 / NJD -155 | 2.9 – 3.6 | 1–5 / 1–6 | 21% | NJD -1.5 39% | 6.5 | Lukas Dostal (expected) / Jake Allen (expected) | – | no line yet (model fair NJD -1.5 +155 / ANA +1.5 -155) | no line yet | no line yet |
| 7:00 PM | FLA @ PIT | FLA 3, PIT 4 | PIT 55% | FLA +120 / PIT -120 | 3.0 – 3.3 | 1–5 / 1–6 | 22% | PIT -1.5 34% | 6.4 | Akira Schmid (expected) / Sergei Murashov (expected) | – | no line yet (model fair PIT -1.5 +195 / FLA +1.5 -195) | no line yet | no line yet |
| 7:30 PM | LAK @ NYI | LAK 2, NYI 3 | NYI 53% | LAK +115 / NYI -115 | 2.7 – 2.9 | 1–5 / 1–5 | 24% | NYI -1.5 30% | 5.6 | Darcy Kuemper (expected) / Ilya Sorokin (expected) | – | no line yet (model fair NYI -1.5 +230 / LAK +1.5 -230) | no line yet | no line yet |
| 8:00 PM | VGK @ STL | VGK 3, STL 2 | VGK 52% | VGK -110 / STL +110 | 3.0 – 2.9 | 1–5 / 1–5 | 23% | VGK -1.5 31% | 6.0 | Carter Hart (expected) / Joel Hofer (expected) | – | no line yet (model fair STL +1.5 -225 / VGK -1.5 +225) | no line yet | no line yet |
| 8:00 PM | WPG @ DAL | WPG 2, DAL 3 | DAL 59% | WPG +145 / DAL -145 | 2.7 – 3.2 | 1–5 / 1–6 | 22% | DAL -1.5 37% | 5.9 | Stuart Skinner (expected) / Jake Oettinger (expected) | – | no line yet (model fair DAL -1.5 +165 / WPG +1.5 -165) | no line yet | no line yet |
| 9:00 PM | MIN @ CGY | MIN 4, CGY 3 | MIN 61% | MIN -155 / CGY +155 | 3.5 – 2.8 | 1–6 / 1–5 | 22% | MIN -1.5 39% | 6.3 | Jesper Wallstedt (expected) / Dustin Wolf (expected) | – | no line yet (model fair CGY +1.5 -155 / MIN -1.5 +155) | no line yet | no line yet |
| 9:00 PM | CAR @ EDM | CAR 4, EDM 3 | CAR 54% | CAR -115 / EDM +115 | 3.4 – 3.1 | 1–6 / 1–6 | 22% | CAR -1.5 32% | 6.5 | Brandon Bussi (expected) / Devon Levi (expected) | – | no line yet (model fair EDM +1.5 -210 / CAR -1.5 +210) | no line yet | no line yet |
| 10:00 PM | UTA @ SEA | UTA 4, SEA 3 | UTA 63% | UTA -170 / SEA +170 | 3.8 – 2.9 | 1–6 / 1–5 | 20% | UTA -1.5 43% | 6.7 | Karel Vejmelka (expected) / Joey Daccord (expected) | – | no line yet (model fair SEA +1.5 -130 / UTA -1.5 +130) | no line yet | no line yet |
| 10:00 PM | DET @ VAN | DET 4, VAN 3 | DET 62% | DET -160 / VAN +160 | 3.7 – 3.0 | 1–6 / 1–5 | 21% | DET -1.5 41% | 6.7 | John Gibson (expected) / Kevin Lankinen (expected) | – | no line yet (model fair VAN +1.5 -145 / DET -1.5 +145) | no line yet | no line yet |

## How the 2026-27 predictions have done

| Predictor | Games | Log loss | Brier | Winners | Goals MAE | Total MAE | 80% range hit |
|---|---|---|---|---|---|---|---|
| Final prediction | 140 | 0.6523 | 0.2302 | 64.3% | 1.39 | 1.76 | 90.0% |
| Model only (before blending) | 140 | 0.6516 | 0.2299 | 64.3% | – | – | – |
| Elo | 140 | 0.6601 | 0.2337 | 63.6% | – | – | – |
| Final prediction, games with a line | 6 | 0.6969 | 0.2508 | 66.7% | 1.21 | 1.87 | 100.0% |
| Model only, games with a line | 6 | 0.6802 | 0.2430 | 66.7% | – | – | – |
| Betting market (de-vigged moneyline) | 6 | 0.7108 | 0.2570 | 66.7% | – | 2.00 | – |

Log loss and Brier score the win chances (lower is better; a coin flip scores 0.693 and 0.250). Hockey is close to a coin flip, so differences in the third decimal matter, and only over hundreds of games. Goals MAE is the average miss on each team's goals.

Overtime: predicted in 21.7% of regular-season games, happened in 22.1%.

134 of these games were played before the predictor went live. They are backfilled walk-forward (each day predicted from earlier days only) with the actual starting goalies and no betting line. Every game since is graded on the prediction logged before puck drop.

### Betting edges

| Market | Edges | Record (W-L-P) | Units | ROI |
|---|---|---|---|---|
| Puck line | 0 | 0-0-0 | +0.00 | – |
| Moneyline | 0 | 0-0-0 | +0.00 | – |
| Total | 0 | 0-0-0 | +0.00 | – |

Moneyline moved toward the model's edge on the first line seen before puck drop: 1 of 2 games (50%).

One unit on each edge at the price logged with the last prediction before puck drop; pushes return the stake. The moneyline moving toward the model's edge (closing line value) is the quickest sign that it knows something the market doesn't yet.

### Results, Monday, October 19

| Game | Predicted | Final | Win chance for winner | Inside 80% ranges | Goalies |
|---|---|---|---|---|---|
| ANA @ NYR | 3–4 | 2–5 | 56% | yes | Ville Husso / Dylan Garand |
| COL @ PHI | 4–3 | 2–3 | 34% | yes | Mackenzie Blackwood / Joseph Woll |
| SJS @ TOR | 3–4 | 1–3 | 57% | yes | Yaroslav Askarov / Sergei Bobrovsky |
| PIT @ UTA | 3–4 | 4–5 | 60% | yes | Arturs Silovs / Sebastian Cossa |

## Power ratings

Goals per game better than an average team, from the goal-rate model: offense and defense combine 5-on-5 expected goals (score and venue adjusted), special teams and actual goals, each weighted against a preseason prior. Defense is positive when it holds opponents below average. Goaltending is rated separately below.

| # | Team | Net | Offense | Defense | 5v5 xGF/60 | 5v5 xGA/60 | PP xGF/60 | PK xGA/60 | Elo |
|---|---|---|---|---|---|---|---|---|---|
| 1 | CAR | +0.58 | +0.39 | +0.19 | 3.39 | 2.47 | 7.75 | 6.40 | 1569 |
| 2 | UTA | +0.50 | +0.29 | +0.21 | 3.22 | 2.38 | 7.84 | 7.88 | 1518 |
| 3 | TBL | +0.32 | +0.14 | +0.18 | 2.87 | 2.47 | 7.55 | 7.54 | 1538 |
| 4 | FLA | +0.30 | +0.06 | +0.23 | 2.73 | 2.38 | 8.89 | 7.22 | 1505 |
| 5 | EDM | +0.30 | +0.14 | +0.16 | 2.65 | 2.45 | 9.10 | 8.04 | 1525 |
| 6 | COL | +0.28 | +0.28 | +0.00 | 2.98 | 2.72 | 7.48 | 7.48 | 1550 |
| 7 | VGK | +0.27 | +0.09 | +0.19 | 2.68 | 2.46 | 8.52 | 7.02 | 1545 |
| 8 | PIT | +0.23 | +0.22 | +0.01 | 3.03 | 2.64 | 7.81 | 7.57 | 1492 |
| 9 | NJD | +0.20 | +0.06 | +0.13 | 2.93 | 2.48 | 8.39 | 7.52 | 1489 |
| 10 | MIN | +0.18 | +0.02 | +0.16 | 2.72 | 2.49 | 8.46 | 7.88 | 1533 |
| 11 | LAK | +0.16 | -0.12 | +0.28 | 2.53 | 2.31 | 7.57 | 7.60 | 1460 |
| 12 | DAL | +0.15 | -0.07 | +0.22 | 2.50 | 2.44 | 8.90 | 7.09 | 1529 |
| 13 | BUF | +0.11 | +0.08 | +0.03 | 2.72 | 2.62 | 7.27 | 7.90 | 1519 |
| 14 | STL | +0.09 | -0.03 | +0.12 | 2.54 | 2.52 | 6.79 | 7.29 | 1501 |
| 15 | OTT | +0.03 | -0.09 | +0.12 | 2.53 | 2.53 | 7.56 | 7.60 | 1520 |
| 16 | NYR | +0.03 | +0.00 | +0.02 | 2.66 | 2.68 | 8.21 | 7.37 | 1507 |
| 17 | MTL | -0.03 | +0.04 | -0.07 | 2.80 | 2.76 | 7.02 | 8.15 | 1517 |
| 18 | CBJ | -0.04 | -0.01 | -0.03 | 2.73 | 2.70 | 7.44 | 8.23 | 1495 |
| 19 | WSH | -0.06 | +0.09 | -0.15 | 2.82 | 2.88 | 7.49 | 8.01 | 1521 |
| 20 | NYI | -0.08 | -0.12 | +0.05 | 2.52 | 2.65 | 7.19 | 8.59 | 1495 |
| 21 | WPG | -0.08 | -0.06 | -0.02 | 2.61 | 2.74 | 7.81 | 7.76 | 1486 |
| 22 | BOS | -0.10 | -0.01 | -0.09 | 2.62 | 2.83 | 7.56 | 7.81 | 1529 |
| 23 | DET | -0.12 | -0.08 | -0.04 | 2.66 | 2.72 | 8.18 | 8.23 | 1481 |
| 24 | NSH | -0.14 | -0.10 | -0.04 | 2.52 | 2.73 | 7.54 | 7.46 | 1485 |
| 25 | ANA | -0.19 | +0.05 | -0.23 | 2.91 | 2.92 | 7.42 | 7.98 | 1484 |
| 26 | TOR | -0.22 | -0.03 | -0.19 | 2.52 | 2.91 | 8.30 | 8.11 | 1471 |
| 27 | CGY | -0.25 | -0.04 | -0.20 | 2.72 | 2.91 | 7.05 | 7.65 | 1453 |
| 28 | SEA | -0.31 | -0.04 | -0.27 | 2.57 | 3.00 | 7.08 | 8.04 | 1481 |
| 29 | PHI | -0.40 | -0.33 | -0.07 | 2.15 | 2.77 | 7.64 | 7.07 | 1476 |
| 30 | SJS | -0.46 | -0.22 | -0.24 | 2.33 | 2.92 | 7.16 | 8.53 | 1461 |
| 31 | VAN | -0.63 | -0.17 | -0.46 | 2.35 | 3.18 | 7.43 | 8.12 | 1425 |
| 32 | CHI | -0.67 | -0.27 | -0.40 | 2.28 | 3.11 | 6.75 | 8.03 | 1440 |

## Goalies

Each team's likeliest next starter. GSAx is goals saved above expected (from this predictor's own shot model), shrunk hard toward a slightly below-average prior, since goaltending repeats poorly from season to season.

| Team | Likely next starter | Share of recent starts | GSAx per 100 shots | Goals per game vs average |
|---|---|---|---|---|
| WSH | Logan Thompson | 76% | +0.49 | +0.21 |
| NYI | Ilya Sorokin | 74% | +0.48 | +0.20 |
| BOS | Jeremy Swayman | 77% | +0.34 | +0.14 |
| TBL | Andrei Vasilevskiy | 72% | +0.20 | +0.08 |
| CBJ | Jet Greaves | 53% | +0.17 | +0.07 |
| DAL | Jake Oettinger | 75% | +0.16 | +0.07 |
| MIN | Jesper Wallstedt | 88% | +0.13 | +0.06 |
| OTT | Linus Ullmark | 78% | +0.13 | +0.05 |
| COL | Mackenzie Blackwood | 56% | +0.12 | +0.05 |
| NYR | Dylan Garand | 62% | +0.07 | +0.03 |
| MTL | Jacob Fowler | 55% | +0.07 | +0.03 |
| CHI | Spencer Knight | 81% | +0.06 | +0.03 |
| WPG | Stuart Skinner | 61% | -0.01 | -0.00 |
| STL | Joel Hofer | 61% | -0.03 | -0.01 |
| PHI | Joseph Woll | 55% | -0.04 | -0.02 |
| NJD | Jake Allen | 62% | -0.07 | -0.03 |
| CAR | Pyotr Kochetkov | 52% | -0.07 | -0.03 |
| DET | John Gibson | 73% | -0.08 | -0.03 |
| TOR | Sergei Bobrovsky | 50% | -0.09 | -0.04 |
| VGK | Carter Hart | 58% | -0.10 | -0.04 |
| UTA | Karel Vejmelka | 69% | -0.12 | -0.05 |
| EDM | Devon Levi | 61% | -0.12 | -0.05 |
| SJS | Alex Nedeljkovic | 61% | -0.13 | -0.05 |
| ANA | Lukas Dostal | 87% | -0.16 | -0.07 |
| BUF | Ukko-Pekka Luukkonen | 67% | -0.18 | -0.08 |
| SEA | Joey Daccord | 54% | -0.19 | -0.08 |
| NSH | Juuse Saros | 87% | -0.25 | -0.10 |
| LAK | Darcy Kuemper | 64% | -0.25 | -0.10 |
| FLA | Jacob Markstrom | 65% | -0.26 | -0.11 |
| CGY | Dustin Wolf | 61% | -0.28 | -0.12 |
| PIT | Arturs Silovs | 59% | -0.35 | -0.15 |
| VAN | Kevin Lankinen | 57% | -0.61 | -0.26 |

## Current model fit

- Fitted on 5732 games from 2022-23 to 2026-27.
- Home ice: +3.0% goals for the home team relative to the visitor.
- Second night of a back-to-back: -5.8% goals scored, +3.3% goals allowed.
- Starting goalie: each goal per game he saves above average lowers the opponent's rate by 23%.
- Blend: 49% on the betting line wherever there is one (fitted on 6 logged games, shrunk toward an even split).
- Simulator: 22.3% of recent regular-season games reached overtime; trailing teams usually have the goalie pulled with 2 minutes left when down one and 3 when down two; empty-net goals come at 0.41 a minute with the net empty; three-on-three overtime produces 1.03 goals per five minutes.
