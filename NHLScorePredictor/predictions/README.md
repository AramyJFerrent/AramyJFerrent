# NHL score predictions

Updated Wed Nov 25, 2026 12:00 AM ET. Refreshed automatically several times a day during the season; each game's prediction is locked at puck drop and graded once the final score is in.

Each game is simulated 10,000 times minute by minute, with pulled goalies, empty-net goals, overtime and shootouts. The predicted score is the most common final score in which the likelier winner wins; as in the official result, a shootout winner gets one extra goal. Hockey is low-scoring and luck-heavy, so read the win chance and the ranges (80% of simulated outcomes for each team) before the single score.

Goalies marked with a percentage are projected from recent starts (the share is the chance he starts); "probable" or "confirmed" ones come from ESPN and replace the projection when available.

The fair moneyline is the American odds that match the win chance exactly, with no bookmaker margin: -150 means risk $150 to win $100, +150 means risk $100 to win $150. A sportsbook's price is a little worse on both sides because of its cut, so a book only offers value on a team when its price beats the fair line. The puck line is the favorite's chance to win by two or more.

The edge columns price each side of the puck line, moneyline and total with the final prediction: the model's goal rates blended with the market's, simulated against the posted lines, overtime and shootout included (the shootout winner gets one goal), and anchored to the market's own chances so only what the blend moves off the market counts. Each cell shows the side with the best expected value (EV) per $1 bet at the posted price. A side is an edge only if its EV is at least 3%: a pick shows its price, EV, its chance of winning the bet and its stake, a 25% share of the Kelly stake in units of 1% of the bankroll, with at most 3 units on one game; "no edge" means neither side clears the bar. A projected starting goalie is wrong about a third of the time and the market prices the real one, so edges wait until both starters are confirmed. A total with no posted price is assumed to be -110 (marked \*); the puck line and moneyline are never assumed, so without a price the cell shows the model's fair odds instead. Treat the edges as an experiment, not betting advice; see the backtest for how they have done on past seasons. Their record is tracked live below.

## Wednesday, November 25

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected goals | 80% range | Overtime | Puck line | Total: model / line | Goalies | Posted moneyline | Puck line edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 7:00 PM | WPG @ BOS | WPG 3, BOS 4 | BOS 60% | WPG +145 / BOS -145 | 2.9 – 3.5 | 1–5 / 1–6 | 21% | BOS -1.5 39% | 6.4 / 6.5 (over 48%) | Stuart Skinner (expected) / Jeremy Swayman (expected) | WPG +136 / BOS -162 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 7:00 PM | NYR @ BUF | NYR 3, BUF 4 | BUF 54% | NYR +115 / BUF -115 | 3.1 – 3.3 | 1–6 / 1–6 | 22% | BUF -1.5 33% | 6.4 / 6.5 (over 48%) | Joonas Korpisalo (expected) / Alex Lyon (expected) | NYR +114 / BUF -135 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 7:00 PM | CAR @ TBL | CAR 4, TBL 3 | CAR 54% | CAR -120 / TBL +120 | 3.3 – 3.0 | 1–6 / 1–5 | 23% | CAR -1.5 33% | 6.3 / 6.5 (over 46%) | Pyotr Kochetkov (expected) / Andrei Vasilevskiy (expected) | CAR -130 / TBL +110 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 7:00 PM | OTT @ FLA | OTT 2, FLA 3 | FLA 52% | OTT +110 / FLA -110 | 2.9 – 3.0 | 1–5 / 1–5 | 22% | FLA -1.5 30% | 5.9 / 5.5 (over 52%) | Linus Ullmark (expected) / Jacob Markstrom (expected) | OTT +110 / FLA -130 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 7:00 PM | STL @ NYI | STL 2, NYI 3 | NYI 51% | STL +105 / NYI -105 | 3.0 – 3.1 | 1–5 / 1–6 | 22% | NYI -1.5 30% | 6.2 / 5.5 (over 55%) | Joel Hofer (expected) / Ilya Sorokin (expected) | STL +100 / NYI -120 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 7:00 PM | CGY @ PIT | CGY 3, PIT 4 | PIT 61% | CGY +155 / PIT -155 | 2.8 – 3.5 | 1–5 / 1–6 | 21% | PIT -1.5 39% | 6.4 / 6.5 (over 47%) | Dustin Wolf (expected) / Arturs Silovs (expected) | CGY +136 / PIT -162 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 7:00 PM | PHI @ WSH | PHI 3, WSH 4 | WSH 59% | PHI +145 / WSH -145 | 2.9 – 3.5 | 1–5 / 1–6 | 22% | WSH -1.5 38% | 6.3 / 6.5 (over 47%) | Dan Vladar (expected) / Logan Thompson (expected) | PHI +136 / WSH -162 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 7:00 PM | NJD @ CBJ | NJD 4, CBJ 3 | NJD 58% | NJD -140 / CBJ +140 | 3.4 – 2.9 | 1–6 / 1–5 | 22% | NJD -1.5 36% | 6.3 / 6.5 (over 46%) | Connor Hellebuyck (expected) / Cam Talbot (expected) | NJD -155 / CBJ +130 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 7:30 PM | VAN @ DET | VAN 3, DET 4 | DET 68% | VAN +210 / DET -210 | 2.6 – 3.8 | 1–5 / 1–6 | 19% | DET -1.5 47% | 6.4 / 6.5 (over 48%) | Leevi Meriläinen (expected) / Daniil Tarasov (confirmed) | VAN +180 / DET -218 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 8:00 PM | NSH @ DAL | NSH 2, DAL 3 | DAL 61% | NSH +155 / DAL -155 | 2.7 – 3.3 | 1–5 / 1–6 | 22% | DAL -1.5 39% | 6.0 / 5.5 (over 51%) | Juuse Saros (expected) / Jake Oettinger (expected) | NSH +142 / DAL -170 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 8:00 PM | UTA @ MIN | UTA 2, MIN 3 | MIN 57% | UTA +130 / MIN -130 | 2.9 – 3.4 | 1–5 / 1–6 | 22% | MIN -1.5 36% | 6.3 / 6.5 (over 45%) | Karel Vejmelka (expected) / Jesper Wallstedt (expected) | UTA +130 / MIN -155 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 9:30 PM | MTL @ COL | MTL 3, COL 4 | COL 56% | MTL +130 / COL -130 | 3.0 – 3.4 | 1–5 / 1–6 | 22% | COL -1.5 35% | 6.4 / 6.5 (over 49%) | Jacob Fowler (expected) / Mackenzie Blackwood (expected) | MTL +105 / COL -125 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 9:40 PM | CHI @ SEA | CHI 3, SEA 4 | SEA 59% | CHI +145 / SEA -145 | 2.9 – 3.5 | 1–5 / 1–6 | 21% | SEA -1.5 38% | 6.5 / 6.5 (over 49%) | Spencer Knight (expected) / Philipp Grubauer (expected) | CHI +140 / SEA -166 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |
| 10:00 PM | SJS @ ANA | SJS 3, ANA 4 | ANA 58% | SJS +140 / ANA -140 | 3.2 – 3.7 | 1–6 / 1–6 | 21% | ANA -1.5 38% | 6.9 / 6.5 (over 55%) | Yaroslav Askarov (expected) / Lukas Dostal (expected) | SJS +124 / ANA -148 | waiting for confirmed goalies | waiting for confirmed goalies | waiting for confirmed goalies |

## Friday, November 27

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected goals | 80% range | Overtime | Puck line | Total: model / line | Goalies | Posted moneyline | Puck line edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1:00 PM | TOR @ BOS | TOR 3, BOS 4 | BOS 63% | TOR +170 / BOS -170 | 2.8 – 3.6 | 1–5 / 1–6 | 22% | BOS -1.5 41% | 6.4 | Sergei Bobrovsky (expected) / Jeremy Swayman (expected) | – | no line yet (model fair BOS -1.5 +140 / TOR +1.5 -140) | no line yet | no line yet |
| 1:00 PM | CGY @ NJD | CGY 2, NJD 3 | NJD 66% | CGY +190 / NJD -190 | 2.6 – 3.6 | 1–5 / 1–6 | 21% | NJD -1.5 44% | 6.2 | Dustin Wolf (expected) / Connor Hellebuyck (expected) | – | no line yet (model fair NJD -1.5 +130 / CGY +1.5 -130) | no line yet | no line yet |
| 1:00 PM | UTA @ NSH | UTA 4, NSH 3 | UTA 54% | UTA -115 / NSH +115 | 3.4 – 3.1 | 1–6 / 1–5 | 21% | UTA -1.5 33% | 6.5 | Karel Vejmelka (expected) / Juuse Saros (expected) | – | no line yet (model fair NSH +1.5 -200 / UTA -1.5 +200) | no line yet | no line yet |
| 2:00 PM | DAL @ STL | DAL 3, STL 2 | DAL 51% | DAL -105 / STL +105 | 3.0 – 2.9 | 1–5 / 1–5 | 22% | DAL -1.5 30% | 5.9 | Jake Oettinger (expected) / Joel Hofer (expected) | – | no line yet (model fair STL +1.5 -235 / DAL -1.5 +235) | no line yet | no line yet |
| 3:00 PM | OTT @ TBL | OTT 2, TBL 3 | TBL 56% | OTT +125 / TBL -125 | 2.8 – 3.2 | 1–5 / 1–5 | 23% | TBL -1.5 34% | 6.0 | Linus Ullmark (expected) / Andrei Vasilevskiy (expected) | – | no line yet (model fair TBL -1.5 +195 / OTT +1.5 -195) | no line yet | no line yet |
| 3:00 PM | VAN @ PHI | VAN 3, PHI 4 | PHI 70% | VAN +230 / PHI -230 | 2.6 – 3.9 | 1–5 / 1–6 | 20% | PHI -1.5 48% | 6.4 | Leevi Meriläinen (expected) / Dan Vladar (expected) | – | no line yet (model fair PHI -1.5 +105 / VAN +1.5 -105) | no line yet | no line yet |
| 3:00 PM | FLA @ WSH | FLA 3, WSH 4 | WSH 53% | FLA +115 / WSH -115 | 3.1 – 3.3 | 1–5 / 1–6 | 22% | WSH -1.5 32% | 6.3 | Jacob Markstrom (expected) / Logan Thompson (expected) | – | no line yet (model fair WSH -1.5 +215 / FLA +1.5 -215) | no line yet | no line yet |
| 3:00 PM | DET @ CBJ | DET 3, CBJ 4 | CBJ 52% | DET +110 / CBJ -110 | 3.1 – 3.2 | 1–5 / 1–6 | 21% | CBJ -1.5 32% | 6.3 | John Gibson (expected) / Cam Talbot (expected) | – | no line yet (model fair CBJ -1.5 +215 / DET +1.5 -215) | no line yet | no line yet |
| 4:00 PM | COL @ MIN | COL 3, MIN 4 | MIN 53% | COL +110 / MIN -110 | 3.0 – 3.2 | 1–5 / 1–6 | 22% | MIN -1.5 32% | 6.2 | Mackenzie Blackwood (expected) / Jesper Wallstedt (expected) | – | no line yet (model fair MIN -1.5 +215 / COL +1.5 -215) | no line yet | no line yet |
| 4:00 PM | LAK @ ANA | LAK 4, ANA 3 | LAK 52% | LAK -110 / ANA +110 | 3.3 – 3.1 | 1–6 / 1–6 | 23% | LAK -1.5 32% | 6.4 | Darcy Kuemper (expected) / Lukas Dostal (expected) | – | no line yet (model fair ANA +1.5 -215 / LAK -1.5 +215) | no line yet | no line yet |
| 4:00 PM | VGK @ SJS | VGK 4, SJS 3 | VGK 68% | VGK -215 / SJS +215 | 3.9 – 2.7 | 1–6 / 1–5 | 20% | VGK -1.5 47% | 6.6 | Carter Hart (expected) / Yaroslav Askarov (expected) | – | no line yet (model fair SJS +1.5 -110 / VGK -1.5 +110) | no line yet | no line yet |
| 5:30 PM | NYR @ CHI | NYR 4, CHI 3 | NYR 61% | NYR -155 / CHI +155 | 3.5 – 2.8 | 1–6 / 1–5 | 21% | NYR -1.5 39% | 6.4 | Dylan Garand (expected) / Spencer Knight (expected) | – | no line yet (model fair CHI +1.5 -155 / NYR -1.5 +155) | no line yet | no line yet |
| 7:30 PM | WPG @ NYI | WPG 3, NYI 4 | NYI 57% | WPG +130 / NYI -130 | 2.9 – 3.3 | 1–5 / 1–6 | 22% | NYI -1.5 36% | 6.2 | Stuart Skinner (expected) / Ilya Sorokin (expected) | – | no line yet (model fair NYI -1.5 +180 / WPG +1.5 -180) | no line yet | no line yet |
| 8:00 PM | PIT @ BUF | PIT 3, BUF 4 | BUF 54% | PIT +115 / BUF -115 | 3.2 – 3.4 | 1–6 / 1–6 | 21% | BUF -1.5 34% | 6.6 | Arturs Silovs (expected) / Alex Lyon (expected) | – | no line yet (model fair BUF -1.5 +200 / PIT +1.5 -200) | no line yet | no line yet |
| 8:00 PM | SEA @ EDM | SEA 3, EDM 4 | EDM 63% | SEA +170 / EDM -170 | 2.8 – 3.6 | 1–5 / 1–6 | 21% | EDM -1.5 42% | 6.4 | Philipp Grubauer (expected) / Devon Levi (expected) | – | no line yet (model fair EDM -1.5 +140 / SEA +1.5 -140) | no line yet | no line yet |

\* price not posted; assumed -110.

## Saturday, November 28

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected goals | 80% range | Overtime | Puck line | Total: model / line | Goalies | Posted moneyline | Puck line edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 4:00 PM | MTL @ VGK | MTL 2, VGK 3 | VGK 52% | MTL +110 / VGK -110 | 3.0 – 3.1 | 1–5 / 1–5 | 22% | VGK -1.5 30% | 6.1 | Jacob Fowler (expected) / Adin Hill (expected) | – | no line yet (model fair VGK -1.5 +230 / MTL +1.5 -230) | no line yet | no line yet |
| 6:00 PM | TBL @ FLA | TBL 3, FLA 2 | TBL 55% | TBL -125 / FLA +125 | 3.2 – 2.8 | 1–5 / 1–5 | 24% | TBL -1.5 33% | 6.0 | Dennis Hildeby (expected) / Akira Schmid (expected) | – | no line yet (model fair FLA +1.5 -200 / TBL -1.5 +200) | no line yet | no line yet |
| 7:00 PM | NSH @ DET | NSH 2, DET 3 | DET 51% | NSH +100 / DET -100 | 3.0 – 3.1 | 1–5 / 1–5 | 23% | DET -1.5 30% | 6.1 | Justus Annunen (expected) / Daniil Tarasov (expected) | – | no line yet (model fair DET -1.5 +235 / NSH +1.5 -235) | no line yet | no line yet |
| 7:00 PM | WPG @ NJD | WPG 2, NJD 3 | NJD 59% | WPG +145 / NJD -145 | 2.7 – 3.3 | 1–5 / 1–6 | 22% | NJD -1.5 37% | 6.0 | Nico Daws (expected) / Jake Allen (expected) | – | no line yet (model fair NJD -1.5 +170 / WPG +1.5 -170) | no line yet | no line yet |
| 7:00 PM | CGY @ NYR | CGY 2, NYR 3 | NYR 58% | CGY +140 / NYR -140 | 2.8 – 3.3 | 1–5 / 1–6 | 23% | NYR -1.5 36% | 6.1 | Devin Cooley (expected) / Joonas Korpisalo (expected) | – | no line yet (model fair NYR -1.5 +175 / CGY +1.5 -175) | no line yet | no line yet |
| 7:00 PM | TOR @ PIT | TOR 2, PIT 3 | PIT 57% | TOR +135 / PIT -135 | 2.9 – 3.4 | 1–5 / 1–6 | 22% | PIT -1.5 35% | 6.2 | Anthony Stolarz (expected) / Sergei Murashov (expected) | – | no line yet (model fair PIT -1.5 +180 / TOR +1.5 -180) | no line yet | no line yet |
| 7:00 PM | OTT @ CAR | OTT 3, CAR 4 | CAR 69% | OTT +225 / CAR -225 | 2.5 – 3.8 | 1–5 / 1–6 | 20% | CAR -1.5 48% | 6.3 | Samuel Ersson (expected) / Pyotr Kochetkov (expected) | – | no line yet (model fair CAR -1.5 +110 / OTT +1.5 -110) | no line yet | no line yet |
| 7:00 PM | WSH @ STL | WSH 3, STL 4 | STL 52% | WSH +110 / STL -110 | 3.3 – 3.4 | 1–6 / 1–6 | 21% | STL -1.5 32% | 6.7 | Charlie Lindgren (expected) / Jordan Binnington (expected) | – | no line yet (model fair STL -1.5 +210 / WSH +1.5 -210) | no line yet | no line yet |
| 7:30 PM | NYI @ PHI | NYI 2, PHI 3 | PHI 50% | NYI +100 / PHI -100 | 3.0 – 3.0 | 1–5 / 1–5 | 23% | PHI -1.5 29% | 6.0 | Semyon Varlamov (expected) / Joseph Woll (expected) | – | no line yet (model fair PHI -1.5 +240 / NYI +1.5 -240) | no line yet | no line yet |
| 8:00 PM | UTA @ DAL | UTA 2, DAL 3 | DAL 53% | UTA +115 / DAL -115 | 2.8 – 3.0 | 1–5 / 1–5 | 23% | DAL -1.5 32% | 5.9 | Sebastian Cossa (expected) / Casey DeSmith (expected) | – | no line yet (model fair DAL -1.5 +215 / UTA +1.5 -215) | no line yet | no line yet |
| 9:00 PM | SJS @ COL | SJS 3, COL 4 | COL 73% | SJS +270 / COL -270 | 2.5 – 4.1 | 1–5 / 2–7 | 18% | COL -1.5 53% | 6.6 | Alex Nedeljkovic (expected) / Scott Wedgewood (expected) | – | no line yet (model fair COL -1.5 -115 / SJS +1.5 +115) | no line yet | no line yet |
| 9:00 PM | ANA @ LAK | ANA 2, LAK 3 | LAK 58% | ANA +140 / LAK -140 | 2.8 – 3.4 | 1–5 / 1–6 | 22% | LAK -1.5 36% | 6.2 | Ville Husso (expected) / Anton Forsberg (expected) | – | no line yet (model fair LAK -1.5 +180 / ANA +1.5 -180) | no line yet | no line yet |
| 10:00 PM | EDM @ SEA | EDM 4, SEA 3 | EDM 56% | EDM -125 / SEA +125 | 3.4 – 3.0 | 1–6 / 1–5 | 23% | EDM -1.5 35% | 6.3 | Tristan Jarry (expected) / Joey Daccord (expected) | – | no line yet (model fair SEA +1.5 -190 / EDM -1.5 +190) | no line yet | no line yet |

\* price not posted; assumed -110.

## How the 2026-27 predictions have done

| Predictor | Games | Log loss | Brier | Winners | Goals MAE | Total MAE | 80% range hit |
|---|---|---|---|---|---|---|---|
| Final prediction | 384 | 0.6590 | 0.2333 | 62.0% | 1.38 | 1.83 | 89.7% |
| Model only (before blending) | 384 | 0.6616 | 0.2346 | 60.2% | – | – | – |
| Elo | 384 | 0.6713 | 0.2392 | 58.6% | – | – | – |
| Final prediction, games with a line | 250 | 0.6652 | 0.2362 | 60.4% | 1.37 | 1.88 | 89.8% |
| Model only, games with a line | 250 | 0.6691 | 0.2382 | 57.6% | – | – | – |
| Betting market (de-vigged moneyline) | 250 | 0.6632 | 0.2353 | 60.8% | – | 1.87 | – |

Log loss and Brier score the win chances (lower is better; a coin flip scores 0.693 and 0.250). Hockey is close to a coin flip, so differences in the third decimal matter, and only over hundreds of games. Goals MAE is the average miss on each team's goals.

Overtime: predicted in 21.5% of regular-season games, happened in 21.9%.

134 of these games were played before the predictor went live. They are backfilled walk-forward (each day predicted from earlier days only) with the actual starting goalies and no betting line. Every game since is graded on the prediction logged before puck drop.

### Betting edges

| Market | Edges | Record (W-L-P) | Staked | Units won | ROI | Expected ROI |
|---|---|---|---|---|---|---|
| Puck line | 6 | 1-5-0 | 5.9 | -4.30 | -72.3% | +7.5% |
| Moneyline | 13 | 8-5-0 | 14.7 | +5.40 | +36.8% | +5.5% |
| Total | 2 | 1-1-0 | 1.7 | +0.04 | +2.4% | +3.4% |

Moneyline moved toward the model's edge on the first line seen before puck drop: 42 of 56 games (75%).

Each edge at the stake and price logged with the last prediction before puck drop (edges logged before edges were priced from the final prediction are left out); pushes return the stake. Units are 1% of the bankroll; ROI is units won per unit staked, and expected ROI is what the edges' EVs promised. The moneyline moving toward the model's edge (closing line value) is the quickest sign that it knows something the market doesn't yet.

### Results, Monday, November 23

| Game | Predicted | Final | Win chance for winner | Inside 80% ranges | Goalies |
|---|---|---|---|---|---|
| CBJ @ NJD | 3–4 | 2–3 | 62% | yes | Jet Greaves / Connor Hellebuyck |
| LAK @ MTL | 3–4 | 2–1 | 43% | yes | Darcy Kuemper / Jacob Fowler |
| CGY @ OTT | 2–3 | 1–2 | 67% | yes | Dustin Wolf / Linus Ullmark |
| TOR @ NYI | 3–4 | 4–2 | 41% | yes | Sergei Bobrovsky / Ilya Sorokin |
| UTA @ WPG | 4–3 | 2–4 | 47% | yes | Karel Vejmelka / Stuart Skinner |
| ANA @ SEA | 3–4 | 2–3 | 53% | yes | Lukas Dostal / Joey Daccord |
| MIN @ SJS | 4–3 | 5–2 | 65% | yes | Filip Gustavsson / Yaroslav Askarov |

## Power ratings

Goals per game better than an average team, from the goal-rate model: offense and defense combine 5-on-5 expected goals (score and venue adjusted), special teams and actual goals, each weighted against a preseason prior. Defense is positive when it holds opponents below average. Goaltending is rated separately below.

| # | Team | Net | Offense | Defense | 5v5 xGF/60 | 5v5 xGA/60 | PP xGF/60 | PK xGA/60 | Elo |
|---|---|---|---|---|---|---|---|---|---|
| 1 | CAR | +0.82 | +0.50 | +0.32 | 3.43 | 2.30 | 8.46 | 6.98 | 1598 |
| 2 | TBL | +0.44 | +0.23 | +0.21 | 2.96 | 2.40 | 7.89 | 7.94 | 1549 |
| 3 | UTA | +0.39 | +0.21 | +0.17 | 3.11 | 2.39 | 8.21 | 8.76 | 1496 |
| 4 | VGK | +0.29 | +0.08 | +0.21 | 2.73 | 2.41 | 9.30 | 7.17 | 1524 |
| 5 | MIN | +0.26 | +0.07 | +0.19 | 2.74 | 2.47 | 8.86 | 7.83 | 1572 |
| 6 | OTT | +0.26 | +0.03 | +0.23 | 2.77 | 2.36 | 7.93 | 8.16 | 1530 |
| 7 | COL | +0.25 | +0.22 | +0.03 | 2.84 | 2.68 | 7.96 | 7.99 | 1555 |
| 8 | PIT | +0.21 | +0.15 | +0.06 | 2.98 | 2.55 | 7.65 | 8.00 | 1474 |
| 9 | DAL | +0.21 | -0.07 | +0.27 | 2.56 | 2.34 | 9.31 | 7.18 | 1534 |
| 10 | NJD | +0.20 | +0.06 | +0.14 | 2.78 | 2.45 | 9.09 | 7.80 | 1524 |
| 11 | FLA | +0.12 | -0.04 | +0.16 | 2.50 | 2.47 | 9.47 | 7.65 | 1507 |
| 12 | WSH | +0.11 | +0.16 | -0.05 | 2.95 | 2.70 | 8.14 | 8.03 | 1494 |
| 13 | STL | +0.10 | +0.08 | +0.02 | 2.76 | 2.65 | 7.24 | 8.06 | 1514 |
| 14 | BOS | +0.09 | +0.09 | +0.00 | 2.82 | 2.70 | 7.63 | 8.22 | 1531 |
| 15 | EDM | +0.06 | +0.04 | +0.02 | 2.45 | 2.63 | 9.56 | 8.22 | 1538 |
| 16 | NYR | +0.05 | +0.02 | +0.04 | 2.70 | 2.65 | 8.79 | 7.63 | 1503 |
| 17 | BUF | +0.04 | +0.10 | -0.06 | 2.76 | 2.72 | 7.99 | 8.50 | 1511 |
| 18 | MTL | +0.01 | +0.03 | -0.02 | 2.78 | 2.72 | 7.52 | 8.47 | 1529 |
| 19 | LAK | +0.00 | -0.16 | +0.16 | 2.45 | 2.48 | 8.14 | 7.99 | 1468 |
| 20 | NSH | -0.08 | -0.00 | -0.08 | 2.73 | 2.77 | 8.01 | 7.64 | 1503 |
| 21 | NYI | -0.10 | -0.03 | -0.07 | 2.69 | 2.80 | 7.22 | 8.74 | 1494 |
| 22 | TOR | -0.11 | -0.06 | -0.05 | 2.46 | 2.69 | 8.71 | 8.39 | 1455 |
| 23 | DET | -0.13 | -0.12 | -0.01 | 2.59 | 2.66 | 8.54 | 8.65 | 1471 |
| 24 | CBJ | -0.15 | -0.08 | -0.07 | 2.61 | 2.74 | 7.84 | 8.47 | 1480 |
| 25 | PHI | -0.17 | -0.21 | +0.05 | 2.36 | 2.59 | 7.86 | 7.64 | 1478 |
| 26 | WPG | -0.17 | -0.10 | -0.07 | 2.48 | 2.77 | 8.53 | 9.12 | 1489 |
| 27 | CGY | -0.31 | -0.14 | -0.17 | 2.53 | 2.88 | 7.11 | 7.64 | 1453 |
| 28 | SEA | -0.33 | -0.14 | -0.18 | 2.36 | 2.87 | 7.37 | 8.62 | 1474 |
| 29 | ANA | -0.34 | +0.01 | -0.35 | 2.70 | 3.02 | 7.85 | 8.11 | 1476 |
| 30 | CHI | -0.62 | -0.27 | -0.34 | 2.23 | 3.02 | 7.20 | 8.55 | 1428 |
| 31 | SJS | -0.69 | -0.23 | -0.46 | 2.32 | 3.15 | 7.26 | 9.37 | 1448 |
| 32 | VAN | -0.81 | -0.27 | -0.55 | 2.19 | 3.23 | 7.64 | 8.79 | 1399 |

## Goalies

Each team's likeliest next starter. GSAx is goals saved above expected (from this predictor's own shot model), shrunk hard toward a slightly below-average prior, since goaltending repeats poorly from season to season.

| Team | Likely next starter | Share of recent starts | GSAx per 100 shots | Goals per game vs average |
|---|---|---|---|---|
| NYI | Ilya Sorokin | 69% | +0.43 | +0.18 |
| MIN | Jesper Wallstedt | 82% | +0.32 | +0.13 |
| BOS | Jeremy Swayman | 74% | +0.30 | +0.13 |
| MTL | Jacob Fowler | 62% | +0.30 | +0.12 |
| WSH | Logan Thompson | 70% | +0.28 | +0.12 |
| COL | Mackenzie Blackwood | 67% | +0.24 | +0.10 |
| OTT | Linus Ullmark | 53% | +0.20 | +0.08 |
| TBL | Andrei Vasilevskiy | 71% | +0.17 | +0.07 |
| STL | Joel Hofer | 70% | +0.15 | +0.06 |
| DAL | Jake Oettinger | 80% | +0.14 | +0.06 |
| NJD | Connor Hellebuyck | 60% | +0.09 | +0.04 |
| CHI | Spencer Knight | 79% | +0.05 | +0.02 |
| WPG | Stuart Skinner | 74% | +0.04 | +0.02 |
| TOR | Anthony Stolarz | 56% | +0.02 | +0.01 |
| EDM | Devon Levi | 50% | +0.00 | +0.00 |
| NYR | Dylan Garand | 64% | -0.00 | -0.00 |
| CAR | Pyotr Kochetkov | 65% | -0.01 | -0.00 |
| NSH | Juuse Saros | 67% | -0.09 | -0.04 |
| BUF | Ukko-Pekka Luukkonen | 49% | -0.09 | -0.04 |
| PHI | Dan Vladar | 50% | -0.11 | -0.05 |
| SEA | Philipp Grubauer | 54% | -0.14 | -0.06 |
| UTA | Karel Vejmelka | 51% | -0.18 | -0.08 |
| LAK | Darcy Kuemper | 63% | -0.18 | -0.08 |
| CBJ | Cam Talbot | 63% | -0.19 | -0.08 |
| DET | John Gibson | 56% | -0.21 | -0.09 |
| SJS | Yaroslav Askarov | 65% | -0.22 | -0.09 |
| FLA | Jacob Markstrom | 57% | -0.25 | -0.10 |
| CGY | Dustin Wolf | 53% | -0.25 | -0.11 |
| VGK | Adin Hill | 51% | -0.29 | -0.12 |
| ANA | Lukas Dostal | 46% | -0.29 | -0.12 |
| VAN | Leevi Meriläinen | 67% | -0.33 | -0.14 |
| PIT | Arturs Silovs | 58% | -0.34 | -0.14 |

## Current model fit

- Fitted on 5976 games from 2022-23 to 2026-27.
- Home ice: +2.8% goals for the home team relative to the visitor.
- Second night of a back-to-back: -5.8% goals scored, +3.0% goals allowed.
- Starting goalie: each goal per game he saves above average lowers the opponent's rate by 21%.
- Blend: 60% on the betting line wherever there is one (fitted on 250 logged games, shrunk toward the backtest value).
- Simulator: 22.3% of recent regular-season games reached overtime; trailing teams usually have the goalie pulled with 2 minutes left when down one and 3 when down two; empty-net goals come at 0.40 a minute with the net empty; three-on-three overtime produces 1.02 goals per five minutes.
