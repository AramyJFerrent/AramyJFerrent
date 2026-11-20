# NHL score predictions

Updated Fri Nov 20, 2026 02:50 AM ET. Refreshed automatically several times a day during the season; each game's prediction is locked at puck drop and graded once the final score is in.

Each game is simulated 10,000 times minute by minute, with pulled goalies, empty-net goals, overtime and shootouts. The predicted score is the most common final score in which the likelier winner wins; as in the official result, a shootout winner gets one extra goal. Hockey is low-scoring and luck-heavy, so read the win chance and the ranges (80% of simulated outcomes for each team) before the single score.

Goalies marked with a percentage are projected from recent starts (the share is the chance he starts); "probable" or "confirmed" ones come from ESPN and replace the projection when available.

The fair moneyline is the American odds that match the win chance exactly, with no bookmaker margin: -150 means risk $150 to win $100, +150 means risk $100 to win $150. A sportsbook's price is a little worse on both sides because of its cut, so a book only offers value on a team when its price beats the fair line. The puck line is the favorite's chance to win by two or more.

The edge columns price each side of the puck line, moneyline and total with the final prediction: the model's goal rates blended with the market's, simulated against the posted lines, overtime and shootout included (the shootout winner gets one goal), and anchored to the market's own chances so only what the blend moves off the market counts. Each cell shows the side with the best expected value (EV) per $1 bet at the posted price. A side is an edge only if its EV is at least 3%: a pick shows its price, EV, its chance of winning the bet and its stake, a 25% share of the Kelly stake in units of 1% of the bankroll, with at most 3 units on one game; "no edge" means neither side clears the bar. A projected starting goalie is wrong about a third of the time and the market prices the real one, so edges wait until both starters are confirmed. A total with no posted price is assumed to be -110 (marked \*); the puck line and moneyline are never assumed, so without a price the cell shows the model's fair odds instead. Treat the edges as an experiment, not betting advice; see the backtest for how they have done on past seasons. Their record is tracked live below.

## Saturday, November 21

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected goals | 80% range | Overtime | Puck line | Total: model / line | Goalies | Posted moneyline | Puck line edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1:00 PM | EDM @ CAR | EDM 3, CAR 4 | CAR 68% | EDM +210 / CAR -210 | 2.6 – 3.8 | 1–5 / 1–6 | 20% | CAR -1.5 46% | 6.4 | Devon Levi (expected) / Pyotr Kochetkov (expected) | – | no line yet (model fair CAR -1.5 +115 / EDM +1.5 -115) | no line yet | no line yet |
| 3:30 PM | CHI @ CGY | CHI 3, CGY 4 | CGY 58% | CHI +140 / CGY -140 | 2.9 – 3.5 | 1–5 / 1–6 | 21% | CGY -1.5 37% | 6.4 | Spencer Knight (expected) / Dustin Wolf (expected) | – | no line yet (model fair CGY -1.5 +170 / CHI +1.5 -170) | no line yet | no line yet |
| 6:00 PM | BUF @ FLA | BUF 3, FLA 4 | FLA 53% | BUF +110 / FLA -110 | 3.0 – 3.2 | 1–5 / 1–6 | 22% | FLA -1.5 32% | 6.3 | Alex Lyon (expected) / Jacob Markstrom (expected) | – | no line yet (model fair FLA -1.5 +215 / BUF +1.5 -215) | no line yet | no line yet |
| 6:00 PM | PIT @ NSH | PIT 4, NSH 3 | PIT 50% | PIT -100 / NSH +100 | 3.3 – 3.3 | 1–6 / 1–6 | 21% | PIT -1.5 31% | 6.6 | Arturs Silovs (expected) / Juuse Saros (expected) | – | no line yet (model fair NSH +1.5 -225 / PIT -1.5 +225) | no line yet | no line yet |
| 7:00 PM | WSH @ BOS | WSH 3, BOS 4 | BOS 54% | WSH +115 / BOS -115 | 3.1 – 3.3 | 1–5 / 1–6 | 21% | BOS -1.5 33% | 6.4 | Logan Thompson (expected) / Jeremy Swayman (expected) | – | no line yet (model fair BOS -1.5 +200 / WSH +1.5 -200) | no line yet | no line yet |
| 7:00 PM | CBJ @ TOR | CBJ 3, TOR 4 | TOR 52% | CBJ +110 / TOR -110 | 3.1 – 3.3 | 1–6 / 1–6 | 22% | TOR -1.5 31% | 6.4 | Jet Greaves (expected) / Sergei Bobrovsky (expected) | – | no line yet (model fair TOR -1.5 +220 / CBJ +1.5 -220) | no line yet | no line yet |
| 7:00 PM | PHI @ MTL | PHI 2, MTL 3 | MTL 59% | PHI +140 / MTL -140 | 2.7 – 3.3 | 1–5 / 1–6 | 22% | MTL -1.5 37% | 6.0 | Dan Vladar (expected) / Jacob Fowler (expected) | – | no line yet (model fair MTL -1.5 +170 / PHI +1.5 -170) | no line yet | no line yet |
| 7:00 PM | LAK @ OTT | LAK 2, OTT 3 | OTT 60% | LAK +150 / OTT -150 | 2.6 – 3.3 | 1–5 / 1–6 | 22% | OTT -1.5 37% | 5.9 | Darcy Kuemper (expected) / Linus Ullmark (expected) | – | no line yet (model fair OTT -1.5 +165 / LAK +1.5 -165) | no line yet | no line yet |
| 7:00 PM | NYI @ DET | NYI 4, DET 3 | NYI 52% | NYI -110 / DET +110 | 3.2 – 3.1 | 1–6 / 1–5 | 23% | NYI -1.5 31% | 6.3 | Ilya Sorokin (expected) / John Gibson (expected) | – | no line yet (model fair DET +1.5 -220 / NYI -1.5 +220) | no line yet | no line yet |
| 7:00 PM | NJD @ STL | NJD 2, STL 3 | STL 50% | NJD +100 / STL -100 | 3.0 – 3.0 | 1–5 / 1–5 | 23% | STL -1.5 30% | 6.0 | Connor Hellebuyck (expected) / Joel Hofer (expected) | – | no line yet (model fair STL -1.5 +240 / NJD +1.5 -240) | no line yet | no line yet |
| 7:00 PM | VGK @ WPG | VGK 3, WPG 2 | VGK 55% | VGK -120 / WPG +120 | 3.2 – 2.9 | 1–6 / 1–5 | 22% | VGK -1.5 34% | 6.1 | Adin Hill (expected) / Stuart Skinner (expected) | – | no line yet (model fair WPG +1.5 -195 / VGK -1.5 +195) | no line yet | no line yet |
| 9:00 PM | ANA @ UTA | ANA 3, UTA 4 | UTA 69% | ANA +225 / UTA -225 | 2.8 – 4.2 | 1–5 / 2–7 | 19% | UTA -1.5 49% | 7.0 | Lukas Dostal (expected) / Karel Vejmelka (expected) | – | no line yet (model fair UTA -1.5 +105 / ANA +1.5 -105) | no line yet | no line yet |
| 10:00 PM | MIN @ VAN | MIN 4, VAN 3 | MIN 74% | MIN -280 / VAN +280 | 4.1 – 2.5 | 2–7 / 1–5 | 17% | MIN -1.5 54% | 6.6 | Jesper Wallstedt (expected) / Leevi Meriläinen (expected) | – | no line yet (model fair VAN +1.5 +120 / MIN -1.5 -120) | no line yet | no line yet |
| 10:00 PM | SEA @ SJS | SEA 4, SJS 3 | SEA 56% | SEA -130 / SJS +130 | 3.6 – 3.2 | 1–6 / 1–6 | 21% | SEA -1.5 36% | 6.8 | Philipp Grubauer (expected) / Yaroslav Askarov (expected) | – | no line yet (model fair SJS +1.5 -175 / SEA -1.5 +175) | no line yet | no line yet |

\* price not posted; assumed -110.

## Sunday, November 22

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected goals | 80% range | Overtime | Puck line | Total: model / line | Goalies | Posted moneyline | Puck line edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 12:30 PM | CAR @ NYR | CAR 4, NYR 3 | CAR 59% | CAR -145 / NYR +145 | 3.4 – 2.9 | 1–6 / 1–5 | 22% | CAR -1.5 37% | 6.3 | Brandon Bussi (expected) / Dylan Garand (expected) | – | no line yet (model fair NYR +1.5 -170 / CAR -1.5 +170) | no line yet | no line yet |
| 5:00 PM | BUF @ TBL | BUF 2, TBL 3 | TBL 66% | BUF +195 / TBL -195 | 2.6 – 3.6 | 1–5 / 1–6 | 21% | TBL -1.5 44% | 6.2 | Ukko-Pekka Luukkonen (expected) / Andrei Vasilevskiy (expected) | – | no line yet (model fair TBL -1.5 +125 / BUF +1.5 -125) | no line yet | no line yet |
| 7:00 PM | EDM @ STL | EDM 2, STL 3 | STL 52% | EDM +105 / STL -105 | 3.1 – 3.2 | 1–5 / 1–6 | 22% | STL -1.5 31% | 6.2 | Tristan Jarry (expected) / Jordan Binnington (expected) | – | no line yet (model fair STL -1.5 +230 / EDM +1.5 -230) | no line yet | no line yet |
| 7:00 PM | PIT @ DAL | PIT 2, DAL 3 | DAL 61% | PIT +155 / DAL -155 | 2.7 – 3.3 | 1–5 / 1–6 | 22% | DAL -1.5 38% | 6.0 | Sergei Murashov (expected) / Jake Oettinger (expected) | – | no line yet (model fair DAL -1.5 +160 / PIT +1.5 -160) | no line yet | no line yet |
| 8:00 PM | CHI @ VAN | CHI 4, VAN 3 | CHI 52% | CHI -110 / VAN +110 | 3.4 – 3.3 | 1–6 / 1–6 | 21% | CHI -1.5 32% | 6.7 | Drew Commesso (expected) / Kevin Lankinen (expected) | – | no line yet (model fair VAN +1.5 -215 / CHI -1.5 +215) | no line yet | no line yet |

\* price not posted; assumed -110.

## Monday, November 23

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected goals | 80% range | Overtime | Puck line | Total: model / line | Goalies | Posted moneyline | Puck line edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 7:00 PM | CBJ @ NJD | CBJ 2, NJD 3 | NJD 62% | CBJ +160 / NJD -160 | 2.7 – 3.4 | 1–5 / 1–6 | 21% | NJD -1.5 40% | 6.1 | Jet Greaves (expected) / Connor Hellebuyck (expected) | – | no line yet (model fair NJD -1.5 +150 / CBJ +1.5 -150) | no line yet | no line yet |
| 7:30 PM | LAK @ MTL | LAK 2, MTL 3 | MTL 58% | LAK +135 / MTL -135 | 2.8 – 3.3 | 1–5 / 1–6 | 22% | MTL -1.5 36% | 6.0 | Darcy Kuemper (expected) / Jacob Fowler (expected) | – | no line yet (model fair MTL -1.5 +180 / LAK +1.5 -180) | no line yet | no line yet |
| 7:30 PM | CGY @ OTT | CGY 2, OTT 3 | OTT 65% | CGY +190 / OTT -190 | 2.6 – 3.6 | 1–5 / 1–6 | 21% | OTT -1.5 44% | 6.2 | Dustin Wolf (expected) / Linus Ullmark (expected) | – | no line yet (model fair OTT -1.5 +130 / CGY +1.5 -130) | no line yet | no line yet |
| 7:30 PM | TOR @ NYI | TOR 3, NYI 4 | NYI 60% | TOR +150 / NYI -150 | 2.9 – 3.6 | 1–5 / 1–6 | 21% | NYI -1.5 39% | 6.5 | Sergei Bobrovsky (expected) / Ilya Sorokin (expected) | – | no line yet (model fair NYI -1.5 +160 / TOR +1.5 -160) | no line yet | no line yet |
| 7:30 PM | UTA @ WPG | UTA 4, WPG 3 | UTA 57% | UTA -135 / WPG +135 | 3.4 – 3.0 | 1–6 / 1–5 | 21% | UTA -1.5 36% | 6.4 | Karel Vejmelka (expected) / Stuart Skinner (expected) | – | no line yet (model fair WPG +1.5 -175 / UTA -1.5 +175) | no line yet | no line yet |
| 9:40 PM | ANA @ SEA | ANA 3, SEA 4 | SEA 54% | ANA +120 / SEA -120 | 3.3 – 3.6 | 1–6 / 1–6 | 22% | SEA -1.5 34% | 6.9 | Lukas Dostal (expected) / Philipp Grubauer (expected) | – | no line yet (model fair SEA -1.5 +195 / ANA +1.5 -195) | no line yet | no line yet |
| 10:00 PM | MIN @ SJS | MIN 4, SJS 3 | MIN 72% | MIN -260 / SJS +260 | 4.1 – 2.6 | 2–7 / 1–5 | 19% | MIN -1.5 52% | 6.6 | Jesper Wallstedt (expected) / Yaroslav Askarov (expected) | – | no line yet (model fair SJS +1.5 +105 / MIN -1.5 -105) | no line yet | no line yet |

\* price not posted; assumed -110.

## How the 2026-27 predictions have done

| Predictor | Games | Log loss | Brier | Winners | Goals MAE | Total MAE | 80% range hit |
|---|---|---|---|---|---|---|---|
| Final prediction | 346 | 0.6563 | 0.2321 | 62.1% | 1.38 | 1.82 | 89.9% |
| Model only (before blending) | 346 | 0.6592 | 0.2335 | 60.4% | – | – | – |
| Elo | 346 | 0.6693 | 0.2383 | 58.4% | – | – | – |
| Final prediction, games with a line | 212 | 0.6618 | 0.2347 | 60.4% | 1.38 | 1.87 | 90.1% |
| Model only, games with a line | 212 | 0.6665 | 0.2370 | 57.5% | – | – | – |
| Betting market (de-vigged moneyline) | 212 | 0.6593 | 0.2336 | 60.4% | – | 1.86 | – |

Log loss and Brier score the win chances (lower is better; a coin flip scores 0.693 and 0.250). Hockey is close to a coin flip, so differences in the third decimal matter, and only over hundreds of games. Goals MAE is the average miss on each team's goals.

Overtime: predicted in 21.5% of regular-season games, happened in 21.7%.

134 of these games were played before the predictor went live. They are backfilled walk-forward (each day predicted from earlier days only) with the actual starting goalies and no betting line. Every game since is graded on the prediction logged before puck drop.

### Betting edges

| Market | Edges | Record (W-L-P) | Staked | Units won | ROI | Expected ROI |
|---|---|---|---|---|---|---|
| Puck line | 4 | 0-4-0 | 3.9 | -3.91 | -100.0% | +8.2% |
| Moneyline | 12 | 7-5-0 | 13.2 | +4.49 | +34.1% | +5.7% |
| Total | 2 | 1-1-0 | 1.7 | +0.04 | +2.4% | +3.4% |

Moneyline moved toward the model's edge on the first line seen before puck drop: 37 of 49 games (76%).

Each edge at the stake and price logged with the last prediction before puck drop (edges logged before edges were priced from the final prediction are left out); pushes return the stake. Units are 1% of the bankroll; ROI is units won per unit staked, and expected ROI is what the edges' EVs promised. The moneyline moving toward the model's edge (closing line value) is the quickest sign that it knows something the market doesn't yet.

### Results, Wednesday, November 18

| Game | Predicted | Final | Win chance for winner | Inside 80% ranges | Goalies |
|---|---|---|---|---|---|
| BOS @ DET | 2–3 | 4–1 | 49% | yes | Jeremy Swayman / Daniil Tarasov |
| MTL @ NJD | 2–3 | 3–2 | 41% | yes | Jacob Fowler / Connor Hellebuyck |
| COL @ UTA | 3–4 | 1–4 | 52% | yes | Mackenzie Blackwood / Sebastian Cossa |

## Power ratings

Goals per game better than an average team, from the goal-rate model: offense and defense combine 5-on-5 expected goals (score and venue adjusted), special teams and actual goals, each weighted against a preseason prior. Defense is positive when it holds opponents below average. Goaltending is rated separately below.

| # | Team | Net | Offense | Defense | 5v5 xGF/60 | 5v5 xGA/60 | PP xGF/60 | PK xGA/60 | Elo |
|---|---|---|---|---|---|---|---|---|---|
| 1 | CAR | +0.83 | +0.50 | +0.33 | 3.46 | 2.30 | 8.69 | 7.13 | 1593 |
| 2 | TBL | +0.47 | +0.22 | +0.25 | 2.93 | 2.37 | 7.99 | 7.99 | 1553 |
| 3 | UTA | +0.40 | +0.23 | +0.17 | 3.14 | 2.42 | 8.37 | 8.89 | 1498 |
| 4 | MIN | +0.28 | +0.13 | +0.16 | 2.87 | 2.53 | 8.96 | 8.04 | 1568 |
| 5 | VGK | +0.27 | +0.05 | +0.22 | 2.68 | 2.42 | 9.10 | 7.23 | 1524 |
| 6 | COL | +0.25 | +0.22 | +0.03 | 2.86 | 2.68 | 8.07 | 8.09 | 1551 |
| 7 | DAL | +0.24 | -0.05 | +0.29 | 2.60 | 2.32 | 9.38 | 7.37 | 1529 |
| 8 | PIT | +0.24 | +0.16 | +0.08 | 2.99 | 2.55 | 7.71 | 7.91 | 1484 |
| 9 | STL | +0.19 | +0.05 | +0.13 | 2.78 | 2.52 | 7.13 | 8.15 | 1500 |
| 10 | OTT | +0.18 | -0.01 | +0.19 | 2.71 | 2.44 | 8.07 | 8.12 | 1529 |
| 11 | NJD | +0.16 | +0.03 | +0.13 | 2.75 | 2.50 | 9.18 | 7.88 | 1528 |
| 12 | FLA | +0.12 | -0.05 | +0.18 | 2.50 | 2.47 | 9.59 | 7.63 | 1504 |
| 13 | BOS | +0.12 | +0.07 | +0.05 | 2.83 | 2.66 | 7.70 | 8.11 | 1528 |
| 14 | NYR | +0.08 | +0.02 | +0.06 | 2.71 | 2.64 | 8.86 | 7.71 | 1507 |
| 15 | WSH | +0.05 | +0.13 | -0.08 | 2.92 | 2.77 | 7.81 | 8.10 | 1504 |
| 16 | EDM | +0.04 | +0.02 | +0.02 | 2.44 | 2.66 | 9.78 | 8.33 | 1549 |
| 17 | BUF | +0.04 | +0.07 | -0.03 | 2.76 | 2.70 | 7.97 | 8.50 | 1499 |
| 18 | LAK | +0.04 | -0.12 | +0.16 | 2.54 | 2.50 | 8.12 | 8.14 | 1464 |
| 19 | MTL | -0.03 | +0.04 | -0.07 | 2.77 | 2.79 | 7.58 | 8.56 | 1533 |
| 20 | NYI | -0.09 | -0.01 | -0.08 | 2.76 | 2.82 | 7.42 | 8.66 | 1499 |
| 21 | NSH | -0.12 | -0.01 | -0.11 | 2.74 | 2.82 | 8.08 | 7.64 | 1501 |
| 22 | WPG | -0.12 | -0.10 | -0.02 | 2.52 | 2.72 | 8.53 | 8.98 | 1485 |
| 23 | DET | -0.12 | -0.11 | -0.02 | 2.63 | 2.69 | 8.60 | 8.73 | 1474 |
| 24 | TOR | -0.15 | -0.05 | -0.09 | 2.49 | 2.77 | 8.73 | 8.44 | 1455 |
| 25 | CBJ | -0.16 | -0.05 | -0.11 | 2.70 | 2.80 | 7.85 | 8.56 | 1475 |
| 26 | PHI | -0.16 | -0.22 | +0.06 | 2.39 | 2.60 | 7.91 | 7.72 | 1471 |
| 27 | CGY | -0.30 | -0.14 | -0.16 | 2.51 | 2.88 | 7.09 | 7.75 | 1462 |
| 28 | SEA | -0.37 | -0.16 | -0.22 | 2.35 | 2.93 | 7.21 | 8.76 | 1470 |
| 29 | ANA | -0.39 | +0.03 | -0.42 | 2.71 | 3.12 | 8.09 | 8.26 | 1485 |
| 30 | CHI | -0.64 | -0.28 | -0.36 | 2.25 | 3.06 | 7.23 | 8.58 | 1423 |
| 31 | VAN | -0.72 | -0.23 | -0.49 | 2.26 | 3.19 | 7.81 | 8.79 | 1406 |
| 32 | SJS | -0.77 | -0.23 | -0.54 | 2.34 | 3.25 | 7.34 | 9.23 | 1449 |

## Goalies

Each team's likeliest next starter. GSAx is goals saved above expected (from this predictor's own shot model), shrunk hard toward a slightly below-average prior, since goaltending repeats poorly from season to season.

| Team | Likely next starter | Share of recent starts | GSAx per 100 shots | Goals per game vs average |
|---|---|---|---|---|
| NYI | Ilya Sorokin | 69% | +0.43 | +0.18 |
| MTL | Jacob Fowler | 70% | +0.33 | +0.14 |
| WSH | Logan Thompson | 75% | +0.32 | +0.13 |
| MIN | Jesper Wallstedt | 87% | +0.31 | +0.13 |
| BOS | Jeremy Swayman | 71% | +0.29 | +0.12 |
| COL | Mackenzie Blackwood | 74% | +0.23 | +0.10 |
| OTT | Linus Ullmark | 47% | +0.15 | +0.06 |
| NJD | Connor Hellebuyck | 52% | +0.15 | +0.06 |
| TBL | Andrei Vasilevskiy | 76% | +0.14 | +0.06 |
| STL | Joel Hofer | 72% | +0.11 | +0.05 |
| EDM | Devon Levi | 46% | +0.10 | +0.04 |
| DAL | Jake Oettinger | 75% | +0.06 | +0.03 |
| CBJ | Jet Greaves | 50% | +0.05 | +0.02 |
| CHI | Spencer Knight | 83% | +0.04 | +0.02 |
| CAR | Pyotr Kochetkov | 65% | +0.03 | +0.01 |
| NYR | Dylan Garand | 60% | +0.01 | +0.00 |
| WPG | Stuart Skinner | 76% | -0.03 | -0.01 |
| NSH | Juuse Saros | 63% | -0.08 | -0.03 |
| PHI | Dan Vladar | 50% | -0.11 | -0.05 |
| BUF | Ukko-Pekka Luukkonen | 43% | -0.17 | -0.07 |
| UTA | Karel Vejmelka | 62% | -0.19 | -0.08 |
| DET | John Gibson | 52% | -0.21 | -0.09 |
| SJS | Yaroslav Askarov | 68% | -0.22 | -0.09 |
| CGY | Dustin Wolf | 50% | -0.22 | -0.09 |
| SEA | Joey Daccord | 51% | -0.22 | -0.09 |
| LAK | Darcy Kuemper | 62% | -0.23 | -0.10 |
| TOR | Sergei Bobrovsky | 58% | -0.25 | -0.10 |
| ANA | Lukas Dostal | 39% | -0.26 | -0.11 |
| FLA | Jacob Markstrom | 53% | -0.26 | -0.11 |
| VGK | Adin Hill | 52% | -0.29 | -0.12 |
| VAN | Leevi Meriläinen | 68% | -0.37 | -0.15 |
| PIT | Arturs Silovs | 55% | -0.40 | -0.17 |

## Current model fit

- Fitted on 5938 games from 2022-23 to 2026-27.
- Home ice: +2.8% goals for the home team relative to the visitor.
- Second night of a back-to-back: -5.9% goals scored, +3.2% goals allowed.
- Starting goalie: each goal per game he saves above average lowers the opponent's rate by 21%.
- Blend: 51% on the betting line wherever there is one (fitted on 212 logged games, shrunk toward the backtest value).
- Simulator: 22.3% of recent regular-season games reached overtime; trailing teams usually have the goalie pulled with 2 minutes left when down one and 3 when down two; empty-net goals come at 0.40 a minute with the net empty; three-on-three overtime produces 1.03 goals per five minutes.
