# NHL score predictions

Updated Wed Nov 18, 2026 10:27 PM ET. Refreshed automatically several times a day during the season; each game's prediction is locked at puck drop and graded once the final score is in.

Each game is simulated 10,000 times minute by minute, with pulled goalies, empty-net goals, overtime and shootouts. The predicted score is the most common final score in which the likelier winner wins; as in the official result, a shootout winner gets one extra goal. Hockey is low-scoring and luck-heavy, so read the win chance and the ranges (80% of simulated outcomes for each team) before the single score.

Goalies marked with a percentage are projected from recent starts (the share is the chance he starts); "probable" or "confirmed" ones come from ESPN and replace the projection when available.

The fair moneyline is the American odds that match the win chance exactly, with no bookmaker margin: -150 means risk $150 to win $100, +150 means risk $100 to win $150. A sportsbook's price is a little worse on both sides because of its cut, so a book only offers value on a team when its price beats the fair line. The puck line is the favorite's chance to win by two or more.

The edge columns price each side of the puck line, moneyline and total with the final prediction: the model's goal rates blended with the market's, simulated against the posted lines, overtime and shootout included (the shootout winner gets one goal), and anchored to the market's own chances so only what the blend moves off the market counts. Each cell shows the side with the best expected value (EV) per $1 bet at the posted price. A side is an edge only if its EV is at least 3%: a pick shows its price, EV, its chance of winning the bet and its stake, a 25% share of the Kelly stake in units of 1% of the bankroll, with at most 3 units on one game; "no edge" means neither side clears the bar. A projected starting goalie is wrong about a third of the time and the market prices the real one, so edges wait until both starters are confirmed. A total with no posted price is assumed to be -110 (marked \*); the puck line and moneyline are never assumed, so without a price the cell shows the model's fair odds instead. Treat the edges as an experiment, not betting advice; see the backtest for how they have done on past seasons. Their record is tracked live below.

## Thursday, November 19

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected goals | 80% range | Overtime | Puck line | Total: model / line | Goalies | Posted moneyline | Puck line edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 7:00 PM | LAK @ TOR | LAK 3, TOR 4 | TOR 51% | LAK +105 / TOR -105 | 3.1 – 3.2 | 1–5 / 1–6 | 22% | TOR -1.5 31% | 6.3 / 6.5 (over 47%) | Darcy Kuemper (expected) / Sergei Bobrovsky (expected) | LAK -110 / TOR -110 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 7:00 PM | PHI @ OTT | PHI 2, OTT 3 | OTT 63% | PHI +170 / OTT -170 | 2.6 – 3.4 | 1–5 / 1–6 | 21% | OTT -1.5 41% | 5.9 / 5.5 (over 51%) | Dan Vladar (expected) / Linus Ullmark (expected) | PHI +150 / OTT -180 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 7:00 PM | STL @ PIT | STL 3, PIT 4 | PIT 51% | STL +105 / PIT -105 | 3.2 – 3.2 | 1–6 / 1–6 | 22% | PIT -1.5 30% | 6.3 / 6.5 (over 48%) | Joel Hofer (expected) / Arturs Silovs (expected) | STL -108 / PIT -112 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 7:00 PM | BUF @ WSH | BUF 3, WSH 4 | WSH 56% | BUF +130 / WSH -130 | 3.1 – 3.5 | 1–6 / 1–6 | 22% | WSH -1.5 35% | 6.7 / 6.5 (over 53%) | Ukko-Pekka Luukkonen (expected) / Logan Thompson (expected) | BUF +114 / WSH -135 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 7:00 PM | MTL @ CAR | MTL 3, CAR 4 | CAR 72% | MTL +255 / CAR -255 | 2.5 – 4.0 | 1–5 / 2–7 | 18% | CAR -1.5 51% | 6.5 / 6.5 (over 50%) | Jakub Dobes (confirmed) / Pyotr Kochetkov (expected) | MTL +215 / CAR -265 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 7:00 PM | NYI @ WPG | NYI 4, WPG 3 | NYI 51% | NYI -105 / WPG +105 | 3.1 – 3.1 | 1–5 / 1–6 | 23% | NYI -1.5 30% | 6.3 / 5.5 (over 56%) | Ilya Sorokin (expected) / Stuart Skinner (expected) | NYI -105 / WPG -115 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 7:30 PM | EDM @ TBL | EDM 3, TBL 4 | TBL 58% | EDM +135 / TBL -135 | 2.9 – 3.3 | 1–5 / 1–6 | 22% | TBL -1.5 36% | 6.2 / 6.5 (over 45%) | Devon Levi (expected) / Andrei Vasilevskiy (expected) | EDM +120 / TBL -142 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 8:00 PM | CBJ @ CHI | CBJ 3, CHI 2 | CBJ 58% | CBJ -140 / CHI +140 | 3.4 – 2.8 | 1–6 / 1–5 | 21% | CBJ -1.5 37% | 6.2 / 5.5 (over 56%) | Jet Greaves (expected) / Spencer Knight (expected) | CBJ -162 / CHI +136 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 8:00 PM | MIN @ CGY | MIN 4, CGY 3 | MIN 66% | MIN -190 / CGY +190 | 3.6 – 2.6 | 1–6 / 1–5 | 21% | MIN -1.5 43% | 6.2 / 6.5 (over 46%) | Jesper Wallstedt (expected) / Dustin Wolf (expected) | MIN -218 / CGY +180 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 9:00 PM | ANA @ COL | ANA 3, COL 4 | COL 61% | ANA +155 / COL -155 | 3.1 – 3.8 | 1–5 / 1–6 | 20% | COL -1.5 40% | 6.8 / 6.5 (over 55%) | Lukas Dostal (expected) / Scott Wedgewood (expected) | ANA +124 / COL -148 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 9:40 PM | VAN @ SEA | VAN 3, SEA 4 | SEA 62% | VAN +165 / SEA -165 | 3.0 – 3.8 | 1–5 / 1–6 | 20% | SEA -1.5 41% | 6.7 / 6.5 (over 53%) | Leevi Meriläinen (expected) / Philipp Grubauer (expected) | VAN +154 / SEA -185 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 10:00 PM | DAL @ VGK | DAL 2, VGK 3 | VGK 53% | DAL +110 / VGK -110 | 2.9 – 3.1 | 1–5 / 1–5 | 23% | VGK -1.5 32% | 6.0 / 5.5 (over 52%) | Jake Oettinger (expected) / Carter Hart (expected) | DAL +105 / VGK -125 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |

## Saturday, November 21

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected goals | 80% range | Overtime | Puck line | Total: model / line | Goalies | Posted moneyline | Puck line edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1:00 PM | EDM @ CAR | EDM 3, CAR 4 | CAR 67% | EDM +205 / CAR -205 | 2.6 – 3.8 | 1–5 / 1–6 | 19% | CAR -1.5 46% | 6.4 | Devon Levi (expected) / Pyotr Kochetkov (expected) | – | no line yet (model fair CAR -1.5 +120 / EDM +1.5 -120) | no line yet | no line yet |
| 3:30 PM | CHI @ CGY | CHI 3, CGY 4 | CGY 58% | CHI +140 / CGY -140 | 2.9 – 3.5 | 1–5 / 1–6 | 21% | CGY -1.5 37% | 6.4 | Spencer Knight (expected) / Dustin Wolf (expected) | – | no line yet (model fair CGY -1.5 +165 / CHI +1.5 -165) | no line yet | no line yet |
| 6:00 PM | BUF @ FLA | BUF 3, FLA 4 | FLA 54% | BUF +115 / FLA -115 | 3.0 – 3.2 | 1–5 / 1–6 | 22% | FLA -1.5 32% | 6.2 | Alex Lyon (expected) / Jacob Markstrom (expected) | – | no line yet (model fair FLA -1.5 +215 / BUF +1.5 -215) | no line yet | no line yet |
| 6:00 PM | PIT @ NSH | PIT 4, NSH 3 | PIT 51% | PIT -100 / NSH +100 | 3.3 – 3.3 | 1–6 / 1–6 | 22% | PIT -1.5 31% | 6.6 | Arturs Silovs (expected) / Juuse Saros (expected) | – | no line yet (model fair NSH +1.5 -225 / PIT -1.5 +225) | no line yet | no line yet |
| 7:00 PM | WSH @ BOS | WSH 3, BOS 4 | BOS 53% | WSH +115 / BOS -115 | 3.1 – 3.3 | 1–5 / 1–6 | 22% | BOS -1.5 33% | 6.4 | Logan Thompson (expected) / Jeremy Swayman (expected) | – | no line yet (model fair BOS -1.5 +205 / WSH +1.5 -205) | no line yet | no line yet |
| 7:00 PM | CBJ @ TOR | CBJ 3, TOR 4 | TOR 52% | CBJ +105 / TOR -105 | 3.1 – 3.3 | 1–6 / 1–6 | 22% | TOR -1.5 31% | 6.4 | Jet Greaves (expected) / Sergei Bobrovsky (expected) | – | no line yet (model fair TOR -1.5 +225 / CBJ +1.5 -225) | no line yet | no line yet |
| 7:00 PM | PHI @ MTL | PHI 2, MTL 3 | MTL 57% | PHI +135 / MTL -135 | 2.8 – 3.2 | 1–5 / 1–6 | 22% | MTL -1.5 35% | 6.0 | Dan Vladar (expected) / Jacob Fowler (expected) | – | no line yet (model fair MTL -1.5 +180 / PHI +1.5 -180) | no line yet | no line yet |
| 7:00 PM | LAK @ OTT | LAK 2, OTT 3 | OTT 61% | LAK +155 / OTT -155 | 2.6 – 3.2 | 1–5 / 1–6 | 23% | OTT -1.5 38% | 5.8 | Darcy Kuemper (expected) / Linus Ullmark (expected) | – | no line yet (model fair OTT -1.5 +165 / LAK +1.5 -165) | no line yet | no line yet |
| 7:00 PM | NYI @ DET | NYI 3, DET 2 | NYI 52% | NYI -105 / DET +105 | 3.2 – 3.1 | 1–6 / 1–5 | 23% | NYI -1.5 31% | 6.3 | Ilya Sorokin (expected) / John Gibson (expected) | – | no line yet (model fair DET +1.5 -225 / NYI -1.5 +225) | no line yet | no line yet |
| 7:00 PM | NJD @ STL | NJD 2, STL 3 | STL 52% | NJD +110 / STL -110 | 3.0 – 3.1 | 1–5 / 1–5 | 23% | STL -1.5 30% | 6.0 | Connor Hellebuyck (expected) / Joel Hofer (expected) | – | no line yet (model fair STL -1.5 +230 / NJD +1.5 -230) | no line yet | no line yet |
| 7:00 PM | VGK @ WPG | VGK 3, WPG 2 | VGK 54% | VGK -120 / WPG +120 | 3.2 – 2.9 | 1–6 / 1–5 | 23% | VGK -1.5 33% | 6.1 | Adin Hill (expected) / Stuart Skinner (expected) | – | no line yet (model fair WPG +1.5 -205 / VGK -1.5 +205) | no line yet | no line yet |
| 9:00 PM | ANA @ UTA | ANA 3, UTA 4 | UTA 70% | ANA +230 / UTA -230 | 2.8 – 4.2 | 1–5 / 2–7 | 19% | UTA -1.5 50% | 7.0 | Lukas Dostal (expected) / Karel Vejmelka (expected) | – | no line yet (model fair UTA -1.5 +100 / ANA +1.5 -100) | no line yet | no line yet |
| 10:00 PM | MIN @ VAN | MIN 4, VAN 3 | MIN 73% | MIN -275 / VAN +275 | 4.1 – 2.5 | 2–7 / 1–5 | 18% | MIN -1.5 54% | 6.6 | Jesper Wallstedt (expected) / Leevi Meriläinen (expected) | – | no line yet (model fair VAN +1.5 +115 / MIN -1.5 -115) | no line yet | no line yet |
| 10:00 PM | SEA @ SJS | SEA 4, SJS 3 | SEA 56% | SEA -125 / SJS +125 | 3.6 – 3.2 | 1–6 / 1–6 | 21% | SEA -1.5 35% | 6.8 | Philipp Grubauer (expected) / Yaroslav Askarov (expected) | – | no line yet (model fair SJS +1.5 -185 / SEA -1.5 +185) | no line yet | no line yet |

\* price not posted; assumed -110.

## Sunday, November 22

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected goals | 80% range | Overtime | Puck line | Total: model / line | Goalies | Posted moneyline | Puck line edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 12:30 PM | CAR @ NYR | CAR 4, NYR 3 | CAR 59% | CAR -145 / NYR +145 | 3.4 – 2.9 | 1–6 / 1–5 | 22% | CAR -1.5 37% | 6.3 | Brandon Bussi (expected) / Dylan Garand (expected) | – | no line yet (model fair NYR +1.5 -170 / CAR -1.5 +170) | no line yet | no line yet |
| 5:00 PM | BUF @ TBL | BUF 3, TBL 4 | TBL 65% | BUF +190 / TBL -190 | 2.6 – 3.6 | 1–5 / 1–6 | 21% | TBL -1.5 43% | 6.3 | Ukko-Pekka Luukkonen (expected) / Andrei Vasilevskiy (expected) | – | no line yet (model fair TBL -1.5 +130 / BUF +1.5 -130) | no line yet | no line yet |
| 7:00 PM | EDM @ STL | EDM 2, STL 3 | STL 52% | EDM +110 / STL -110 | 3.0 – 3.2 | 1–5 / 1–6 | 22% | STL -1.5 31% | 6.2 | Tristan Jarry (expected) / Jordan Binnington (expected) | – | no line yet (model fair STL -1.5 +220 / EDM +1.5 -220) | no line yet | no line yet |
| 7:00 PM | PIT @ DAL | PIT 2, DAL 3 | DAL 61% | PIT +160 / DAL -160 | 2.6 – 3.4 | 1–5 / 1–6 | 22% | DAL -1.5 39% | 6.0 | Sergei Murashov (expected) / Jake Oettinger (expected) | – | no line yet (model fair DAL -1.5 +155 / PIT +1.5 -155) | no line yet | no line yet |
| 8:00 PM | CHI @ VAN | CHI 4, VAN 3 | CHI 52% | CHI -110 / VAN +110 | 3.4 – 3.3 | 1–6 / 1–6 | 22% | CHI -1.5 32% | 6.7 | Drew Commesso (expected) / Kevin Lankinen (expected) | – | no line yet (model fair VAN +1.5 -215 / CHI -1.5 +215) | no line yet | no line yet |

\* price not posted; assumed -110.

## How the 2026-27 predictions have done

| Predictor | Games | Log loss | Brier | Winners | Goals MAE | Total MAE | 80% range hit |
|---|---|---|---|---|---|---|---|
| Final prediction | 343 | 0.6554 | 0.2317 | 62.4% | 1.38 | 1.83 | 89.8% |
| Model only (before blending) | 343 | 0.6585 | 0.2332 | 60.6% | – | – | – |
| Elo | 343 | 0.6686 | 0.2379 | 58.6% | – | – | – |
| Final prediction, games with a line | 209 | 0.6604 | 0.2340 | 60.8% | 1.38 | 1.88 | 90.0% |
| Model only, games with a line | 209 | 0.6654 | 0.2365 | 57.9% | – | – | – |
| Betting market (de-vigged moneyline) | 209 | 0.6577 | 0.2328 | 60.8% | – | 1.87 | – |

Log loss and Brier score the win chances (lower is better; a coin flip scores 0.693 and 0.250). Hockey is close to a coin flip, so differences in the third decimal matter, and only over hundreds of games. Goals MAE is the average miss on each team's goals.

Overtime: predicted in 21.5% of regular-season games, happened in 21.9%.

134 of these games were played before the predictor went live. They are backfilled walk-forward (each day predicted from earlier days only) with the actual starting goalies and no betting line. Every game since is graded on the prediction logged before puck drop.

### Betting edges

| Market | Edges | Record (W-L-P) | Staked | Units won | ROI | Expected ROI |
|---|---|---|---|---|---|---|
| Puck line | 4 | 0-4-0 | 3.9 | -3.91 | -100.0% | +8.2% |
| Moneyline | 12 | 7-5-0 | 13.2 | +4.49 | +34.1% | +5.7% |
| Total | 2 | 1-1-0 | 1.7 | +0.04 | +2.4% | +3.4% |

Moneyline moved toward the model's edge on the first line seen before puck drop: 38 of 49 games (78%).

Each edge at the stake and price logged with the last prediction before puck drop (edges logged before edges were priced from the final prediction are left out); pushes return the stake. Units are 1% of the bankroll; ROI is units won per unit staked, and expected ROI is what the edges' EVs promised. The moneyline moving toward the model's edge (closing line value) is the quickest sign that it knows something the market doesn't yet.

### Results, Tuesday, November 17

| Game | Predicted | Final | Win chance for winner | Inside 80% ranges | Goalies |
|---|---|---|---|---|---|
| LAK @ BOS | 2–3 | 3–0 | 40% | no | Darcy Kuemper / Michael DiPietro |
| EDM @ FLA | 2–3 | 5–2 | 48% | yes | Devon Levi / Jacob Markstrom |
| CBJ @ NYI | 2–3 | 1–5 | 56% | yes | Cam Talbot / Ilya Sorokin |
| BUF @ PHI | 4–3 | 3–4 | 45% | yes | Alex Lyon / Joseph Woll |
| OTT @ WPG | 3–2 | 2–1 | 53% | yes | Linus Ullmark / Stuart Skinner |
| WSH @ TBL | 3–4 | 2–5 | 57% | yes | Logan Thompson / Andrei Vasilevskiy |
| TOR @ CHI | 4–3 | 3–6 | 42% | no | Sergei Bobrovsky / Spencer Knight |
| ANA @ STL | 3–4 | 6–8 | 57% | no | Ville Husso / Jordan Binnington |
| NSH @ MIN | 3–4 | 3–7 | 63% | no | Juuse Saros / Jesper Wallstedt |
| DAL @ VGK | 2–3 | 4–3 (OT) | 48% | yes | Jake Oettinger / Adin Hill |
| CGY @ SJS | 4–3 | 5–2 | 51% | yes | Dustin Wolf / Yaroslav Askarov |

## Power ratings

Goals per game better than an average team, from the goal-rate model: offense and defense combine 5-on-5 expected goals (score and venue adjusted), special teams and actual goals, each weighted against a preseason prior. Defense is positive when it holds opponents below average. Goaltending is rated separately below.

| # | Team | Net | Offense | Defense | 5v5 xGF/60 | 5v5 xGA/60 | PP xGF/60 | PK xGA/60 | Elo |
|---|---|---|---|---|---|---|---|---|---|
| 1 | CAR | +0.83 | +0.50 | +0.33 | 3.47 | 2.30 | 8.69 | 7.12 | 1593 |
| 2 | TBL | +0.47 | +0.22 | +0.25 | 2.94 | 2.37 | 7.98 | 7.98 | 1553 |
| 3 | UTA | +0.39 | +0.24 | +0.15 | 3.16 | 2.44 | 8.19 | 8.97 | 1492 |
| 4 | MIN | +0.29 | +0.13 | +0.16 | 2.87 | 2.53 | 8.95 | 8.03 | 1568 |
| 5 | VGK | +0.27 | +0.05 | +0.22 | 2.68 | 2.42 | 9.10 | 7.22 | 1524 |
| 6 | COL | +0.25 | +0.24 | +0.02 | 2.87 | 2.71 | 8.15 | 7.90 | 1557 |
| 7 | DAL | +0.24 | -0.05 | +0.30 | 2.60 | 2.32 | 9.38 | 7.35 | 1529 |
| 8 | PIT | +0.24 | +0.16 | +0.08 | 2.99 | 2.55 | 7.70 | 7.91 | 1484 |
| 9 | STL | +0.19 | +0.05 | +0.14 | 2.78 | 2.52 | 7.12 | 8.14 | 1500 |
| 10 | OTT | +0.18 | -0.01 | +0.19 | 2.70 | 2.44 | 8.07 | 8.11 | 1529 |
| 11 | NJD | +0.17 | +0.03 | +0.14 | 2.76 | 2.49 | 9.17 | 7.89 | 1531 |
| 12 | FLA | +0.13 | -0.05 | +0.18 | 2.50 | 2.47 | 9.59 | 7.63 | 1504 |
| 13 | BOS | +0.10 | +0.06 | +0.03 | 2.80 | 2.68 | 7.65 | 8.13 | 1523 |
| 14 | NYR | +0.08 | +0.02 | +0.06 | 2.71 | 2.64 | 8.85 | 7.69 | 1507 |
| 15 | WSH | +0.06 | +0.13 | -0.08 | 2.92 | 2.77 | 7.80 | 8.09 | 1504 |
| 16 | EDM | +0.04 | +0.02 | +0.02 | 2.44 | 2.66 | 9.77 | 8.32 | 1549 |
| 17 | BUF | +0.04 | +0.07 | -0.03 | 2.76 | 2.70 | 7.96 | 8.50 | 1499 |
| 18 | LAK | +0.03 | -0.13 | +0.16 | 2.54 | 2.50 | 8.11 | 8.13 | 1464 |
| 19 | MTL | -0.05 | +0.03 | -0.08 | 2.76 | 2.80 | 7.60 | 8.54 | 1530 |
| 20 | NYI | -0.08 | -0.01 | -0.08 | 2.76 | 2.82 | 7.41 | 8.65 | 1499 |
| 21 | DET | -0.09 | -0.09 | +0.00 | 2.65 | 2.66 | 8.62 | 8.68 | 1479 |
| 22 | NSH | -0.12 | -0.01 | -0.11 | 2.74 | 2.82 | 8.08 | 7.62 | 1501 |
| 23 | WPG | -0.12 | -0.10 | -0.02 | 2.52 | 2.73 | 8.53 | 8.98 | 1485 |
| 24 | TOR | -0.15 | -0.06 | -0.09 | 2.49 | 2.77 | 8.72 | 8.43 | 1455 |
| 25 | CBJ | -0.16 | -0.05 | -0.11 | 2.70 | 2.80 | 7.85 | 8.55 | 1475 |
| 26 | PHI | -0.16 | -0.22 | +0.06 | 2.39 | 2.60 | 7.90 | 7.72 | 1471 |
| 27 | CGY | -0.30 | -0.14 | -0.16 | 2.51 | 2.88 | 7.07 | 7.73 | 1462 |
| 28 | SEA | -0.37 | -0.16 | -0.21 | 2.35 | 2.93 | 7.20 | 8.76 | 1470 |
| 29 | ANA | -0.39 | +0.03 | -0.42 | 2.71 | 3.12 | 8.08 | 8.25 | 1485 |
| 30 | CHI | -0.64 | -0.28 | -0.36 | 2.25 | 3.06 | 7.22 | 8.57 | 1423 |
| 31 | VAN | -0.72 | -0.23 | -0.49 | 2.26 | 3.19 | 7.80 | 8.79 | 1406 |
| 32 | SJS | -0.77 | -0.23 | -0.54 | 2.33 | 3.26 | 7.33 | 9.24 | 1449 |

## Goalies

Each team's likeliest next starter. GSAx is goals saved above expected (from this predictor's own shot model), shrunk hard toward a slightly below-average prior, since goaltending repeats poorly from season to season.

| Team | Likely next starter | Share of recent starts | GSAx per 100 shots | Goals per game vs average |
|---|---|---|---|---|
| NYI | Ilya Sorokin | 69% | +0.43 | +0.18 |
| WSH | Logan Thompson | 75% | +0.32 | +0.14 |
| MIN | Jesper Wallstedt | 87% | +0.32 | +0.13 |
| MTL | Jacob Fowler | 67% | +0.31 | +0.13 |
| BOS | Jeremy Swayman | 85% | +0.27 | +0.11 |
| COL | Mackenzie Blackwood | 71% | +0.22 | +0.09 |
| NJD | Connor Hellebuyck | 47% | +0.16 | +0.07 |
| OTT | Linus Ullmark | 47% | +0.16 | +0.07 |
| TBL | Andrei Vasilevskiy | 76% | +0.14 | +0.06 |
| STL | Joel Hofer | 72% | +0.12 | +0.05 |
| EDM | Devon Levi | 46% | +0.10 | +0.04 |
| DAL | Jake Oettinger | 75% | +0.06 | +0.03 |
| CBJ | Jet Greaves | 50% | +0.06 | +0.02 |
| CHI | Spencer Knight | 83% | +0.04 | +0.02 |
| CAR | Pyotr Kochetkov | 65% | +0.03 | +0.01 |
| NYR | Dylan Garand | 60% | +0.01 | +0.00 |
| WPG | Stuart Skinner | 76% | -0.03 | -0.01 |
| NSH | Juuse Saros | 63% | -0.08 | -0.03 |
| PHI | Dan Vladar | 50% | -0.11 | -0.05 |
| BUF | Ukko-Pekka Luukkonen | 43% | -0.17 | -0.07 |
| UTA | Karel Vejmelka | 68% | -0.19 | -0.08 |
| DET | John Gibson | 57% | -0.21 | -0.09 |
| SJS | Yaroslav Askarov | 68% | -0.21 | -0.09 |
| CGY | Dustin Wolf | 50% | -0.22 | -0.09 |
| SEA | Joey Daccord | 51% | -0.22 | -0.09 |
| LAK | Darcy Kuemper | 62% | -0.23 | -0.10 |
| TOR | Sergei Bobrovsky | 58% | -0.25 | -0.10 |
| ANA | Lukas Dostal | 39% | -0.26 | -0.11 |
| FLA | Jacob Markstrom | 53% | -0.26 | -0.11 |
| VGK | Adin Hill | 52% | -0.29 | -0.12 |
| VAN | Leevi Meriläinen | 68% | -0.36 | -0.15 |
| PIT | Arturs Silovs | 55% | -0.39 | -0.17 |

## Current model fit

- Fitted on 5935 games from 2022-23 to 2026-27.
- Home ice: +2.8% goals for the home team relative to the visitor.
- Second night of a back-to-back: -6.0% goals scored, +3.2% goals allowed.
- Starting goalie: each goal per game he saves above average lowers the opponent's rate by 21%.
- Blend: 51% on the betting line wherever there is one (fitted on 209 logged games, shrunk toward the backtest value).
- Simulator: 22.3% of recent regular-season games reached overtime; trailing teams usually have the goalie pulled with 2 minutes left when down one and 3 when down two; empty-net goals come at 0.40 a minute with the net empty; three-on-three overtime produces 1.03 goals per five minutes.
