# NHL score predictions

Updated Tue Nov 10, 2026 03:32 PM ET. Refreshed automatically several times a day during the season; each game's prediction is locked at puck drop and graded once the final score is in.

Each game is simulated 10,000 times minute by minute, with pulled goalies, empty-net goals, overtime and shootouts. The predicted score is the most common final score in which the likelier winner wins; as in the official result, a shootout winner gets one extra goal. Hockey is low-scoring and luck-heavy, so read the win chance and the ranges (80% of simulated outcomes for each team) before the single score.

Goalies marked with a percentage are projected from recent starts (the share is the chance he starts); "probable" or "confirmed" ones come from ESPN and replace the projection when available.

The fair moneyline is the American odds that match the win chance exactly, with no bookmaker margin: -150 means risk $150 to win $100, +150 means risk $100 to win $150. A sportsbook's price is a little worse on both sides because of its cut, so a book only offers value on a team when its price beats the fair line. The puck line is the favorite's chance to win by two or more.

The edge columns price each side of the puck line, moneyline and total with the final prediction: the model's goal rates blended with the market's, simulated against the posted lines, overtime and shootout included (the shootout winner gets one goal), and anchored to the market's own chances so only what the blend moves off the market counts. Each cell shows the side with the best expected value (EV) per $1 bet at the posted price. A side is an edge only if its EV is at least 3%: a pick shows its price, EV, its chance of winning the bet and its stake, a 25% share of the Kelly stake in units of 1% of the bankroll, with at most 3 units on one game; "no edge" means neither side clears the bar. A projected starting goalie is wrong about a third of the time and the market prices the real one, so edges wait until both starters are confirmed. A total with no posted price is assumed to be -110 (marked \*); the puck line and moneyline are never assumed, so without a price the cell shows the model's fair odds instead. Treat the edges as an experiment, not betting advice; see the backtest for how they have done on past seasons. Their record is tracked live below.

## Tuesday, November 10

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected goals | 80% range | Overtime | Puck line | Total: model / line | Goalies | Posted moneyline | Puck line edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 7:00 PM | COL @ TOR | COL 4, TOR 3 | COL 62% | COL -160 / TOR +160 | 3.7 – 3.0 | 1–6 / 1–5 | 20% | COL -1.5 41% | 6.6 / 6.5 (over 52%) | Mackenzie Blackwood (confirmed) / Sergei Bobrovsky (confirmed) | COL -175 / TOR +145 | no edge | no edge | no edge |
| 7:00 PM | MIN @ MTL | MIN 3, MTL 2 | MIN 53% | MIN -115 / MTL +115 | 3.2 – 3.0 | 1–6 / 1–5 | 22% | MIN -1.5 32% | 6.2 / 6.5 (over 44%) | Jesper Wallstedt (confirmed) / Jacob Fowler (confirmed) | MIN -125 / MTL +105 | no edge | no edge | no edge |
| 7:00 PM | WSH @ OTT | WSH 4, OTT 3 | WSH 51% | WSH -105 / OTT +105 | 3.3 – 3.2 | 1–6 / 1–6 | 22% | WSH -1.5 31% | 6.4 / 6.5 (over 48%) | Logan Thompson (expected) / Samuel Ersson (confirmed) | WSH -112 / OTT -108 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 7:00 PM | NJD @ WPG | NJD 4, WPG 3 | NJD 55% | NJD -125 / WPG +125 | 3.3 – 2.9 | 1–6 / 1–5 | 22% | NJD -1.5 34% | 6.3 / 6.5 (over 46%) | Jake Allen (confirmed) / Nico Daws (confirmed) | NJD -148 / WPG +124 | no edge | no edge | no edge |
| 7:30 PM | FLA @ CBJ | FLA 3, CBJ 2 | FLA 51% | FLA -105 / CBJ +105 | 3.1 – 3.1 | 1–5 / 1–5 | 22% | FLA -1.5 30% | 6.2 / 5.5 (over 55%) | Jacob Markstrom (confirmed) / Cam Talbot (confirmed) | FLA -120 / CBJ +100 | no edge | no edge | no edge |
| 8:00 PM | DET @ STL | DET 2, STL 3 | STL 57% | DET +135 / STL -135 | 2.8 – 3.3 | 1–5 / 1–6 | 22% | STL -1.5 35% | 6.0 / 5.5 (over 53%) | John Gibson (confirmed) / Joel Hofer (confirmed) | DET +120 / STL -142 | no edge | no edge | no edge |
| 10:00 PM | NSH @ LAK | NSH 2, LAK 3 | LAK 55% | NSH +125 / LAK -125 | 2.9 – 3.2 | 1–5 / 1–6 | 23% | LAK -1.5 34% | 6.1 / 6.5 (over 44%) | Juuse Saros (expected) / Anton Forsberg (confirmed) | NSH +110 / LAK -130 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |

## Wednesday, November 11

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected goals | 80% range | Overtime | Puck line | Total: model / line | Goalies | Posted moneyline | Puck line edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 7:00 PM | TBL @ BUF | TBL 4, BUF 3 | TBL 55% | TBL -120 / BUF +120 | 3.4 – 3.1 | 1–6 / 1–6 | 21% | TBL -1.5 34% | 6.5 / 6.5 (over 49%) | Andrei Vasilevskiy (expected) / Ukko-Pekka Luukkonen (expected) | TBL -125 / BUF +105 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 7:30 PM | NYR @ CGY | NYR 4, CGY 3 | NYR 55% | NYR -120 / CGY +120 | 3.3 – 3.0 | 1–6 / 1–5 | 22% | NYR -1.5 34% | 6.3 / 5.5 (over 56%) | Dylan Garand (expected) / Dustin Wolf (expected) | NYR -135 / CGY +114 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 9:00 PM | PHI @ EDM | PHI 2, EDM 3 | EDM 63% | PHI +170 / EDM -170 | 2.6 – 3.5 | 1–5 / 1–6 | 21% | EDM -1.5 42% | 6.1 / 6.5 (over 44%) | Dan Vladar (expected) / Devon Levi (expected) | PHI +180 / EDM -218 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 9:30 PM | UTA @ VGK | UTA 3, VGK 4 | VGK 52% | UTA +105 / VGK -105 | 3.1 – 3.2 | 1–6 / 1–6 | 22% | VGK -1.5 31% | 6.3 / 6.5 (over 46%) | Karel Vejmelka (expected) / Carter Hart (expected) | UTA +105 / VGK -125 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 10:00 PM | NSH @ ANA | NSH 3, ANA 4 | ANA 55% | NSH +125 / ANA -125 | 3.1 – 3.5 | 1–6 / 1–6 | 21% | ANA -1.5 35% | 6.6 / 6.5 (over 52%) | Justus Annunen (expected) / Laurent Brossoit (expected) | NSH +124 / ANA -148 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 10:00 PM | PIT @ SJS | PIT 4, SJS 3 | PIT 60% | PIT -155 / SJS +155 | 3.8 – 3.0 | 1–6 / 1–5 | 21% | PIT -1.5 40% | 6.8 / 6.5 (over 54%) | Arturs Silovs (expected) / Yaroslav Askarov (expected) | PIT -130 / SJS +110 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |

## Thursday, November 12

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected goals | 80% range | Overtime | Puck line | Total: model / line | Goalies | Posted moneyline | Puck line edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 12:00 PM | CAR @ SEA | CAR 4, SEA 3 | CAR 74% | CAR -280 / SEA +280 | 4.2 – 2.6 | 2–7 / 1–5 | 18% | CAR -1.5 53% | 6.8 | Pyotr Kochetkov (expected) / Philipp Grubauer (expected) | – | no line yet (model fair SEA +1.5 +115 / CAR -1.5 -115) | no line yet | no line yet |
| 7:00 PM | MTL @ BOS | MTL 3, BOS 4 | BOS 55% | MTL +120 / BOS -120 | 3.0 – 3.3 | 1–5 / 1–6 | 22% | BOS -1.5 34% | 6.2 | Jacob Fowler (expected) / Jeremy Swayman (expected) | – | no line yet (model fair BOS -1.5 +200 / MTL +1.5 -200) | no line yet | no line yet |
| 7:00 PM | MIN @ TOR | MIN 3, TOR 2 | MIN 60% | MIN -150 / TOR +150 | 3.4 – 2.8 | 1–6 / 1–5 | 21% | MIN -1.5 38% | 6.2 | Jesper Wallstedt (expected) / Sergei Bobrovsky (expected) | – | no line yet (model fair TOR +1.5 -165 / MIN -1.5 +165) | no line yet | no line yet |
| 7:00 PM | COL @ OTT | COL 4, OTT 3 | COL 52% | COL -110 / OTT +110 | 3.2 – 3.1 | 1–6 / 1–5 | 22% | COL -1.5 31% | 6.4 | Mackenzie Blackwood (expected) / Linus Ullmark (expected) | – | no line yet (model fair OTT +1.5 -220 / COL -1.5 +220) | no line yet | no line yet |
| 7:00 PM | WSH @ NJD | WSH 2, NJD 3 | NJD 53% | WSH +115 / NJD -115 | 2.9 – 3.2 | 1–5 / 1–6 | 23% | NJD -1.5 32% | 6.1 | Logan Thompson (expected) / Connor Hellebuyck (expected) | – | no line yet (model fair NJD -1.5 +215 / WSH +1.5 -215) | no line yet | no line yet |
| 7:00 PM | TBL @ CBJ | TBL 3, CBJ 2 | TBL 53% | TBL -115 / CBJ +115 | 3.2 – 3.0 | 1–6 / 1–5 | 21% | TBL -1.5 33% | 6.2 | Dennis Hildeby (expected) / Jet Greaves (expected) | – | no line yet (model fair CBJ +1.5 -205 / TBL -1.5 +205) | no line yet | no line yet |
| 7:30 PM | DET @ FLA | DET 2, FLA 3 | FLA 54% | DET +115 / FLA -115 | 2.9 – 3.2 | 1–5 / 1–6 | 23% | FLA -1.5 33% | 6.1 | John Gibson (expected) / Jacob Markstrom (expected) | – | no line yet (model fair FLA -1.5 +205 / DET +1.5 -205) | no line yet | no line yet |
| 8:00 PM | BUF @ CHI | BUF 4, CHI 3 | BUF 62% | BUF -160 / CHI +160 | 3.6 – 2.8 | 1–6 / 1–5 | 21% | BUF -1.5 40% | 6.4 | Colten Ellis (expected) / Spencer Knight (expected) | – | no line yet (model fair CHI +1.5 -150 / BUF -1.5 +150) | no line yet | no line yet |
| 8:00 PM | WPG @ DAL | WPG 2, DAL 3 | DAL 61% | WPG +155 / DAL -155 | 2.6 – 3.2 | 1–5 / 1–6 | 22% | DAL -1.5 38% | 5.8 | Stuart Skinner (expected) / Jake Oettinger (expected) | – | no line yet (model fair DAL -1.5 +165 / WPG +1.5 -165) | no line yet | no line yet |
| 9:00 PM | STL @ UTA | STL 2, UTA 3 | UTA 53% | STL +110 / UTA -110 | 3.0 – 3.2 | 1–5 / 1–6 | 22% | UTA -1.5 32% | 6.2 | Joel Hofer (expected) / Sebastian Cossa (expected) | – | no line yet (model fair UTA -1.5 +215 / STL +1.5 -215) | no line yet | no line yet |
| 10:00 PM | NYI @ LAK | NYI 2, LAK 3 | LAK 51% | NYI +105 / LAK -105 | 3.0 – 3.1 | 1–5 / 1–5 | 22% | LAK -1.5 30% | 6.1 | Ilya Sorokin (expected) / Darcy Kuemper (expected) | – | no line yet (model fair LAK -1.5 +235 / NYI +1.5 -235) | no line yet | no line yet |

\* price not posted; assumed -110.

## How the 2026-27 predictions have done

| Predictor | Games | Log loss | Brier | Winners | Goals MAE | Total MAE | 80% range hit |
|---|---|---|---|---|---|---|---|
| Final prediction | 285 | 0.6448 | 0.2267 | 62.5% | 1.36 | 1.78 | 90.2% |
| Model only (before blending) | 285 | 0.6478 | 0.2283 | 60.7% | – | – | – |
| Elo | 285 | 0.6600 | 0.2338 | 61.8% | – | – | – |
| Final prediction, games with a line | 151 | 0.6441 | 0.2265 | 61.6% | 1.33 | 1.81 | 90.7% |
| Model only, games with a line | 151 | 0.6499 | 0.2294 | 58.3% | – | – | – |
| Betting market (de-vigged moneyline) | 151 | 0.6433 | 0.2261 | 61.6% | – | 1.80 | – |

Log loss and Brier score the win chances (lower is better; a coin flip scores 0.693 and 0.250). Hockey is close to a coin flip, so differences in the third decimal matter, and only over hundreds of games. Goals MAE is the average miss on each team's goals.

Overtime: predicted in 21.5% of regular-season games, happened in 22.1%.

134 of these games were played before the predictor went live. They are backfilled walk-forward (each day predicted from earlier days only) with the actual starting goalies and no betting line. Every game since is graded on the prediction logged before puck drop.

### Betting edges

| Market | Edges | Record (W-L-P) | Staked | Units won | ROI | Expected ROI |
|---|---|---|---|---|---|---|
| Puck line | 2 | 0-2-0 | 2.2 | -2.16 | -100.0% | +9.4% |
| Moneyline | 8 | 4-4-0 | 8.7 | +1.83 | +21.2% | +6.4% |
| Total | 1 | 0-1-0 | 0.9 | -0.89 | -100.0% | +3.0% |

Moneyline moved toward the model's edge on the first line seen before puck drop: 27 of 33 games (82%).

Each edge at the stake and price logged with the last prediction before puck drop (edges logged before edges were priced from the final prediction are left out); pushes return the stake. Units are 1% of the bankroll; ROI is units won per unit staked, and expected ROI is what the edges' EVs promised. The moneyline moving toward the model's edge (closing line value) is the quickest sign that it knows something the market doesn't yet.

### Results, Monday, November 9

| Game | Predicted | Final | Win chance for winner | Inside 80% ranges | Goalies |
|---|---|---|---|---|---|
| NYR @ EDM | 3–4 | 1–3 | 57% | yes | Dylan Garand / Devon Levi |
| PHI @ VAN | 3–2 | 3–1 | 56% | yes | Joseph Woll / Leevi Meriläinen |
| NYI @ SJS | 4–3 | 2–3 (SO) | 40% | yes | Ilya Sorokin / Yaroslav Askarov |

## Power ratings

Goals per game better than an average team, from the goal-rate model: offense and defense combine 5-on-5 expected goals (score and venue adjusted), special teams and actual goals, each weighted against a preseason prior. Defense is positive when it holds opponents below average. Goaltending is rated separately below.

| # | Team | Net | Offense | Defense | 5v5 xGF/60 | 5v5 xGA/60 | PP xGF/60 | PK xGA/60 | Elo |
|---|---|---|---|---|---|---|---|---|---|
| 1 | CAR | +0.78 | +0.49 | +0.28 | 3.48 | 2.38 | 8.66 | 7.25 | 1585 |
| 2 | UTA | +0.45 | +0.25 | +0.21 | 3.17 | 2.39 | 8.21 | 8.78 | 1506 |
| 3 | TBL | +0.40 | +0.19 | +0.21 | 2.93 | 2.44 | 8.13 | 8.01 | 1544 |
| 4 | VGK | +0.28 | +0.04 | +0.25 | 2.67 | 2.40 | 9.20 | 7.28 | 1536 |
| 5 | MIN | +0.27 | +0.09 | +0.17 | 2.87 | 2.52 | 9.29 | 8.16 | 1549 |
| 6 | PIT | +0.24 | +0.17 | +0.07 | 3.00 | 2.58 | 7.83 | 8.02 | 1487 |
| 7 | COL | +0.23 | +0.27 | -0.04 | 2.97 | 2.79 | 7.82 | 8.02 | 1549 |
| 8 | DAL | +0.22 | -0.07 | +0.30 | 2.54 | 2.34 | 9.63 | 7.42 | 1529 |
| 9 | NJD | +0.22 | +0.04 | +0.17 | 2.84 | 2.47 | 9.24 | 7.94 | 1525 |
| 10 | BUF | +0.13 | +0.13 | -0.00 | 2.89 | 2.70 | 8.07 | 8.51 | 1516 |
| 11 | FLA | +0.12 | -0.02 | +0.15 | 2.60 | 2.52 | 9.73 | 7.65 | 1498 |
| 12 | STL | +0.10 | +0.01 | +0.09 | 2.70 | 2.60 | 7.04 | 7.78 | 1497 |
| 13 | OTT | +0.09 | -0.01 | +0.11 | 2.71 | 2.57 | 8.16 | 8.33 | 1521 |
| 14 | WSH | +0.09 | +0.14 | -0.06 | 2.96 | 2.78 | 7.95 | 8.16 | 1516 |
| 15 | EDM | +0.08 | +0.06 | +0.03 | 2.53 | 2.67 | 9.58 | 8.37 | 1534 |
| 16 | LAK | +0.05 | -0.09 | +0.15 | 2.58 | 2.53 | 8.37 | 8.27 | 1471 |
| 17 | BOS | +0.05 | +0.07 | -0.02 | 2.80 | 2.78 | 7.66 | 8.34 | 1543 |
| 18 | NYR | +0.04 | +0.02 | +0.02 | 2.75 | 2.71 | 9.03 | 7.79 | 1493 |
| 19 | MTL | -0.04 | +0.07 | -0.11 | 2.83 | 2.86 | 7.63 | 8.55 | 1537 |
| 20 | DET | -0.06 | -0.10 | +0.04 | 2.66 | 2.64 | 8.43 | 8.82 | 1477 |
| 21 | CBJ | -0.08 | -0.02 | -0.06 | 2.74 | 2.77 | 7.76 | 8.77 | 1494 |
| 22 | WPG | -0.11 | -0.11 | +0.00 | 2.57 | 2.71 | 8.40 | 8.93 | 1472 |
| 23 | TOR | -0.11 | -0.05 | -0.07 | 2.50 | 2.77 | 8.86 | 8.55 | 1473 |
| 24 | NSH | -0.11 | -0.08 | -0.04 | 2.61 | 2.76 | 8.38 | 7.80 | 1496 |
| 25 | NYI | -0.16 | -0.02 | -0.14 | 2.80 | 2.91 | 7.59 | 8.67 | 1480 |
| 26 | PHI | -0.22 | -0.25 | +0.03 | 2.36 | 2.66 | 7.83 | 7.44 | 1472 |
| 27 | CGY | -0.24 | -0.12 | -0.12 | 2.57 | 2.84 | 7.27 | 8.12 | 1464 |
| 28 | SEA | -0.31 | -0.12 | -0.20 | 2.45 | 2.93 | 7.30 | 8.70 | 1478 |
| 29 | ANA | -0.36 | +0.00 | -0.36 | 2.69 | 3.10 | 8.14 | 8.51 | 1495 |
| 30 | CHI | -0.68 | -0.29 | -0.39 | 2.30 | 3.11 | 7.27 | 8.54 | 1416 |
| 31 | VAN | -0.71 | -0.27 | -0.44 | 2.21 | 3.16 | 7.76 | 8.80 | 1398 |
| 32 | SJS | -0.74 | -0.25 | -0.49 | 2.35 | 3.23 | 7.39 | 9.35 | 1450 |

## Goalies

Each team's likeliest next starter. GSAx is goals saved above expected (from this predictor's own shot model), shrunk hard toward a slightly below-average prior, since goaltending repeats poorly from season to season.

| Team | Likely next starter | Share of recent starts | GSAx per 100 shots | Goals per game vs average |
|---|---|---|---|---|
| NYI | Ilya Sorokin | 70% | +0.41 | +0.17 |
| WSH | Logan Thompson | 75% | +0.37 | +0.15 |
| BOS | Jeremy Swayman | 69% | +0.37 | +0.15 |
| MTL | Jacob Fowler | 64% | +0.33 | +0.14 |
| MIN | Jesper Wallstedt | 81% | +0.25 | +0.10 |
| COL | Mackenzie Blackwood | 73% | +0.20 | +0.09 |
| TBL | Andrei Vasilevskiy | 76% | +0.14 | +0.06 |
| CBJ | Jet Greaves | 50% | +0.11 | +0.05 |
| DAL | Jake Oettinger | 76% | +0.08 | +0.04 |
| STL | Joel Hofer | 71% | +0.05 | +0.02 |
| EDM | Devon Levi | 43% | +0.04 | +0.02 |
| CAR | Pyotr Kochetkov | 69% | +0.03 | +0.01 |
| CHI | Spencer Knight | 77% | +0.03 | +0.01 |
| NYR | Dylan Garand | 70% | -0.02 | -0.01 |
| WPG | Stuart Skinner | 75% | -0.06 | -0.02 |
| NJD | Jake Allen | 44% | -0.07 | -0.03 |
| PHI | Dan Vladar | 51% | -0.08 | -0.03 |
| BUF | Ukko-Pekka Luukkonen | 54% | -0.11 | -0.05 |
| NSH | Juuse Saros | 66% | -0.16 | -0.07 |
| TOR | Sergei Bobrovsky | 62% | -0.16 | -0.07 |
| DET | John Gibson | 55% | -0.17 | -0.07 |
| SJS | Yaroslav Askarov | 65% | -0.19 | -0.08 |
| SEA | Joey Daccord | 51% | -0.19 | -0.08 |
| ANA | Lukas Dostal | 46% | -0.20 | -0.08 |
| UTA | Karel Vejmelka | 63% | -0.22 | -0.09 |
| LAK | Darcy Kuemper | 67% | -0.23 | -0.10 |
| CGY | Dustin Wolf | 49% | -0.26 | -0.11 |
| VGK | Adin Hill | 52% | -0.27 | -0.11 |
| FLA | Jacob Markstrom | 48% | -0.30 | -0.13 |
| VAN | Leevi Meriläinen | 69% | -0.38 | -0.16 |
| PIT | Arturs Silovs | 68% | -0.40 | -0.17 |
| OTT | Samuel Ersson | 40% | -0.49 | -0.20 |

## Current model fit

- Fitted on 5877 games from 2022-23 to 2026-27.
- Home ice: +3.0% goals for the home team relative to the visitor.
- Second night of a back-to-back: -5.9% goals scored, +3.5% goals allowed.
- Starting goalie: each goal per game he saves above average lowers the opponent's rate by 21%.
- Blend: 48% on the betting line wherever there is one (fitted on 151 logged games, shrunk toward the backtest value).
- Simulator: 22.3% of recent regular-season games reached overtime; trailing teams usually have the goalie pulled with 2 minutes left when down one and 3 when down two; empty-net goals come at 0.40 a minute with the net empty; three-on-three overtime produces 1.03 goals per five minutes.
