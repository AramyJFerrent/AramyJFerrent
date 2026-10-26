# NBA score predictions

Updated Mon Oct 26, 2026 05:54 PM ET. Refreshed automatically several times a day during the season, around the injury report's deadlines; each game's prediction is locked at tip-off and graded once the final score is in.

Each team's expected points are its expected possessions times its expected points per possession, from team efficiency ratings and the ratings of the players expected to play, blended with the betting line. Each game is then simulated 10,000 times, overtime included. The predicted score is the expected points rounded; the 80% range holds 80% of simulated outcomes for each team. Basketball is the most predictable major sport, but a team's score still varies by about ±14 points around the forecast, so read the win chance and the ranges too.

Missing players come from the injury report: out players are left out, and doubtful, questionable and probable ones count with the share of their minutes their chance of playing implies, and their minutes go mostly to the bench. The effect is how many points of margin the team gains or loses against its full-strength roster: negative when it is missing good players, positive when the minutes go to better ones. Predictions are rerun when the report changes, up to tip-off.

The fair moneyline is the American odds that match the win chance exactly, with no bookmaker margin: -150 means risk $150 to win $100, +150 means risk $100 to win $150.

The edge columns check every side of the spread, the moneyline and the total for expected value: the profit per $1 bet at the posted price, using the final prediction's chances (the model blended with the line, simulated against the posted lines, pushes returning the stake, and anchored to the market's own chances so only what the blend moves off the line counts). The model's own spread and total are shown alongside, but the blend keeps only the share of that disagreement the model has earned in past seasons, so edges are rare. A side is an edge when its EV is 3% or more; the best such side is shown with its price, its EV, its chance of winning the bet and its stake, a 25% share of the Kelly stake in units of 1% of the bankroll, with at most 3 units on one game. Where a spread or total price is not posted it is assumed to be -110 (marked \*); a moneyline is never assumed. Edges are logged with each prediction, locked at tip-off and graded below. Treat them as an experiment, not betting advice; see the backtest for how they have done on past seasons.

## Monday, October 26

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Spread: model / line | Total: model / line | 80% range | Overtime | Missing (effect on margin) | Spread edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 7:00 PM | WAS @ CHA | WAS 112, CHA 115 | CHA 58% | WAS +140 / CHA -140<br>posted WAS +120 / CHA -142 | CHA -2.7 / CHA -2.5 (fav covers 52%) | 227.7 / 227.5 (over 50%) | 98–127 / 101–130 | 6% | WAS: Jamir Watkins (out); Tristan Vukcevic (out) (+0.9)<br>CHA: Naz Reid (day-to-day); Kon Knueppel (out); Coby White (out); Grant Williams (out) (-1.1) | no edge | no edge | no edge |
| 7:00 PM | MIN @ CLE | MIN 116, CLE 119 | CLE 57% | MIN +130 / CLE -130<br>posted MIN +120 / CLE -142 | CLE -2.5 / CLE -2.5 (fav covers 51%) | 234.8 / 234.5 (over 50%) | 101–131 / 104–133 | 5% | MIN: Donte DiVincenzo (out) (-0.2) | no edge | no edge | no edge |
| 7:30 PM | CHI @ BOS | CHI 110, BOS 124 | BOS 84% | CHI +535 / BOS -535<br>posted CHI +525 / BOS -750 | BOS -13.9 / BOS -13.5 (fav covers 50%) | 233.2 / 233.5 (over 48%) | 95–125 / 109–138 | 3% | CHI: Nic Claxton (out); Patrick Williams (out) (+0.5)<br>BOS: Devin Carter (out) (+1.3) | no edge | no edge | no edge |
| 7:30 PM | DAL @ MIA | DAL 117, MIA 124 | MIA 69% | DAL +225 / MIA -225<br>posted DAL +230 / MIA -285 | MIA -7.2 / MIA -7.5 (fav covers 49%) | 241.4 / 241.5 (over 49%) | 102–132 / 109–139 | 5% | DAL: Naji Marshall (out); Santi Aldama (out); Cooper Flagg (day-to-day); Dereck Lively II (out) (-0.7) | no edge | no edge | no edge |
| 8:00 PM | IND @ MIL | IND 121, MIL 117 | IND 62% | IND -160 / MIL +160<br>posted IND -175 / MIL +145 | IND -4 / IND -4.5 (fav covers 50%) | 238.6 / 238.5 (over 50%) | 107–136 / 102–132 | 5% | IND: Andrew Nembhard (day-to-day); Aaron Nesmith (day-to-day); Johnny Furphy (out); Ivica Zubac (out); Ben Sheppard (out); T.J. McConnell (out) (+0.9) | no edge | no edge | no edge |
| 8:00 PM | PHX @ OKC | PHX 107, OKC 115 | OKC 72% | PHX +260 / OKC -260<br>posted PHX +260 / OKC -325 | OKC -7.8 / OKC -8.5 (fav covers 48%) | 221.5 / 221.5 (over 49%) | 92–122 / 101–129 | 5% | PHX: Oso Ighodaro (out); Mark Williams (out) (+0.1)<br>OKC: Chet Holmgren (out); Jalen Williams (out); Cason Wallace (out) (-0.6) | no edge | no edge | no edge |
| 8:30 PM | ATL @ HOU | ATL 113, HOU 117 | HOU 64% | ATL +175 / HOU -175<br>posted ATL +160 / HOU -192 | HOU -4.5 / HOU -4.5 (fav covers 52%) | 229.7 / 229.5 (over 49%) | 98–127 / 103–132 | 5% | HOU: Marcus Smart (out); Steven Adams (out) (-1.2) | no edge | no edge | no edge |
| 9:00 PM | MEM @ UTA | MEM 118, UTA 119 | UTA 53% | MEM +115 / UTA -115<br>posted MEM -110 / UTA -110 | UTA -1.3 / UTA -1.5 (fav covers 51%) | 237.7 / 237.5 (over 50%) | 103–133 / 105–134 | 6% | MEM: Isaiah Stewart (day-to-day) (+0.0)<br>UTA: Jaxson Hayes (day-to-day); Trey Alexander (out); Jusuf Nurkic (out) (+0.1) | no edge | no edge | no edge |
| 10:00 PM | GSW @ DEN | GSW 114, DEN 122 | DEN 71% | GSW +245 / DEN -245<br>posted GSW +220 / DEN -270 | DEN -7.7 / DEN -7.5 (fav covers 51%) | 236.5 / 236.5 (over 49%) | 99–129 / 107–137 | 5% | GSW: Moses Moody (out); Jimmy Butler III (out); Gui Santos (day-to-day); Kristaps Porzingis (out); Brandon Williams (day-to-day) (-1.7)<br>DEN: Spencer Jones (out); Cameron Johnson (day-to-day); Alpha Diallo (out) (+2.1) | no edge | no edge | no edge |

## Tuesday, October 27

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Spread: model / line | Total: model / line | 80% range | Overtime | Missing (effect on margin) | Spread edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 7:30 PM | BKN @ BOS | BKN 105, BOS 119 | BOS 85% | BKN +575 / BOS -575 | BOS -13.9 | 223.2 | 90–119 / 105–132 | 3% | BKN: Mikel Brown Jr. (day-to-day) (+0.6)<br>BOS: Devin Carter (out) (+1.2) | no line yet | no line yet | no line yet |
| 8:00 PM | DET @ NYK | DET 109, NYK 110 | NYK 53% | DET +110 / NYK -110 | NYK -0.8 | 218.5 | 95–123 / 96–124 | 5% | DET: Ausar Thompson (day-to-day); Jalen Duren (out) (-0.6)<br>NYK: Jose Alvarado (out) (-0.3) | no line yet | no line yet | no line yet |
| 8:00 PM | SAC @ SAS | SAC 106, SAS 122 | SAS 88% | SAC +755 / SAS -755 | SAS -16.2 | 227.4 | 91–120 / 107–136 | 3% | SAC: Maxime Raynaud (out); Keegan Murray (day-to-day); Dylan Cardwell (out) (+0.8)<br>SAS: Tobias Harris (out) (+0.7) | no line yet | no line yet | no line yet |
| 11:00 PM | POR @ LAL | POR 113, LAL 116 | LAL 59% | POR +140 / LAL -140 | LAL -2.9 | 229.5 | 99–128 / 101–131 | 5% | POR: Branden Carlson (day-to-day) (+0.6) | no line yet | no line yet | no line yet |

## How the 2026-27 predictions have done

| Predictor | Games | Margin MAE | Total MAE | Team-points MAE | Log loss | Brier | Winners | 80% range hit |
|---|---|---|---|---|---|---|---|---|
| Final prediction | 43 | 11.41 | 14.36 | 9.28 | 0.573 | 0.195 | 72.1% | 79.1% |
| Model only (before blending) | 43 | 12.40 | 14.14 | 9.85 | 0.623 | 0.218 | 62.8% | – |
| Elo | 43 | 12.41 | – | – | 0.660 | 0.235 | 55.8% | – |
| Final prediction, games with a line | 43 | 11.41 | 14.36 | 9.28 | 0.573 | 0.195 | 72.1% | 79.1% |
| Model only, games with a line | 43 | 12.40 | 14.14 | 9.85 | 0.623 | 0.218 | 62.8% | – |
| Betting line | 43 | 11.24 | 14.34 | 9.20 | 0.557 | 0.189 | 72.1% | – |

MAE is the average miss in points; team-points MAE is the average miss on each team's score. Log loss and Brier score the win chances (lower is better; a coin flip scores 0.693 and 0.250). The closing line misses margins by about 10 points and totals by about 14.

Overtime: predicted in 4.8% of games, happened in 2.3%.

### Betting edges

| Market | Edges | Record (W-L-P) | Staked | Units won | ROI | Expected ROI |
|---|---|---|---|---|---|---|
| Spread | 1 | 1-0-0 | 1.0 | +0.90 | +89.3% | +3.6% |
| Moneyline | 3 | 0-3-0 | 1.2 | -1.19 | -100.0% | +11.2% |
| Total | 0 | 0-0-0 | 0.0 | +0.00 | – | – |

Spread moved toward the model's first spread edge before tip-off: 4 of 5 games (80%).

Live predictions only, each edge at the stake and price logged with the last prediction before tip-off (edges logged before edges were priced from the final prediction are left out); a push returns the stake. Units are 1% of the bankroll; ROI is units won per unit staked, and expected ROI is what the edges' EVs promised. The line moving toward the model's edge before tip-off is the quickest sign that it knows something the market doesn't yet.

### Results, Sunday, October 25

| Game | Predicted | Final | Win chance for winner | Spread: model / line | Inside 80% ranges |
|---|---|---|---|---|---|
| LAL @ UTA | 122–116 | 132–123 | 68% | LAL -6.2 / LAL -6.5 | yes |
| IND @ BKN | 119–113 | 136–109 | 66% | IND -5.8 / IND -6.5 | no |
| ORL @ NYK | 109–116 | 111–102 | 30% | NYK -7 / NYK -7.5 | yes |
| TOR @ MIN | 114–115 | 94–117 | 54% | MIN -1.3 / MIN -1.5 | no |
| LAC @ OKC | 104–120 | 101–108 | 87% | OKC -15.2 / OKC -16.5 | yes |
| DET @ PHI | 115–114 | 106–93 | 55% | DET -1.6 / DET -1.5 | no |
| MEM @ SAC | 119–116 | 123–112 | 59% | MEM -2.9 / MEM -3.5 | yes |

## Power ratings

Points per 100 possessions better than an average team on a neutral floor, combining opponent-adjusted team efficiency (garbage time removed) with the ratings of the team's healthy roster, through the fitted points map. Net per game uses the team's pace. Injury effect now is what its current injury report does to its margin, in points.

| # | Team | Net per 100 | Net per game | Offense | Defense | Pace | Injury effect now | Elo |
|---|---|---|---|---|---|---|---|---|
| 1 | SAS | +6.4 | +6.8 | +1.6 | +4.8 | 105.9 | +0.8 | 1682 |
| 2 | BOS | +6.4 | +6.3 | +3.6 | +2.8 | 98.2 | +1.2 | 1609 |
| 3 | HOU | +5.9 | +6.0 | +3.4 | +2.5 | 100.5 | -1.2 | 1598 |
| 4 | OKC | +5.9 | +6.0 | +0.2 | +5.6 | 102.5 | -0.6 | 1710 |
| 5 | DET | +4.9 | +5.0 | +1.8 | +3.1 | 102.0 | -0.6 | 1647 |
| 6 | MIN | +3.7 | +3.8 | +1.3 | +2.3 | 102.7 | -0.2 | 1611 |
| 7 | NYK | +3.5 | +3.6 | +0.6 | +3.0 | 101.6 | -0.3 | 1684 |
| 8 | LAL | +3.2 | +3.3 | +2.9 | +0.3 | 103.3 | +1.2 | 1587 |
| 9 | POR | +3.1 | +3.2 | +2.0 | +1.1 | 103.3 | +0.6 | 1549 |
| 10 | CLE | +2.5 | +2.7 | +1.8 | +0.7 | 107.9 | +0.0 | 1573 |
| 11 | DEN | +1.7 | +1.7 | +2.9 | -1.3 | 101.1 | +2.1 | 1593 |
| 12 | PHI | +1.5 | +1.6 | -0.9 | +2.4 | 106.8 | -0.4 | 1549 |
| 13 | TOR | +1.4 | +1.5 | -0.7 | +2.1 | 106.7 | +0.0 | 1549 |
| 14 | ORL | +1.3 | +1.4 | -1.5 | +2.8 | 106.3 | +0.2 | 1540 |
| 15 | ATL | +1.2 | +1.3 | +0.9 | +0.2 | 107.2 | +0.8 | 1578 |
| 16 | MIA | -0.1 | -0.1 | +0.9 | -1.0 | 106.4 | +0.0 | 1485 |
| 17 | PHX | -0.2 | -0.2 | +1.2 | -1.4 | 101.3 | +0.1 | 1510 |
| 18 | GSW | -1.3 | -1.4 | -0.2 | -1.1 | 102.3 | -1.7 | 1429 |
| 19 | LAC | -1.4 | -1.5 | -0.7 | -0.7 | 103.6 | +1.4 | 1524 |
| 20 | IND | -1.4 | -1.5 | +0.5 | -1.9 | 105.2 | +0.9 | 1391 |
| 21 | CHA | -2.5 | -2.5 | -2.7 | +0.2 | 101.3 | -1.1 | 1559 |
| 22 | MEM | -2.6 | -2.7 | -0.3 | -2.3 | 102.9 | +0.0 | 1372 |
| 23 | DAL | -2.9 | -3.0 | -1.6 | -1.2 | 104.2 | -0.8 | 1400 |
| 24 | UTA | -3.8 | -4.0 | -1.7 | -2.1 | 105.2 | +0.1 | 1329 |
| 25 | NOP | -5.0 | -5.3 | -1.5 | -3.5 | 105.8 | +0.3 | 1414 |
| 26 | WAS | -5.5 | -5.9 | -2.6 | -2.9 | 106.6 | +1.0 | 1304 |
| 27 | MIL | -5.8 | -6.2 | -1.5 | -4.3 | 106.7 | +0.0 | 1361 |
| 28 | CHI | -6.1 | -6.8 | -3.5 | -2.7 | 110.8 | +0.6 | 1374 |
| 29 | BKN | -6.9 | -7.3 | -3.6 | -3.3 | 105.7 | +0.6 | 1294 |
| 30 | SAC | -7.0 | -7.3 | -3.0 | -3.9 | 104.0 | +0.8 | 1347 |

## Top players

Regularized adjusted plus-minus from every lineup this season and past ones: points per 100 possessions a player adds on offense and saves on defense, against an average player, shrunk toward last season's rating. Players expected to play 20 minutes or more.

| # | Player | Team | Net impact per 100 | Offense | Defense | Expected minutes |
|---|---|---|---|---|---|---|
| 1 | Shai Gilgeous-Alexander | OKC | +6.2 | +5.1 | +1.1 | 36 |
| 2 | Victor Wembanyama | SAS | +5.7 | +1.0 | +4.8 | 33 |
| 3 | Nikola Jokic | DEN | +5.1 | +5.5 | -0.4 | 40 |
| 4 | Kawhi Leonard | TOR | +4.5 | +3.7 | +0.8 | 30 |
| 5 | Alex Caruso | OKC | +4.2 | -0.2 | +4.4 | 24 |
| 6 | Giannis Antetokounmpo | MIA | +3.6 | +3.5 | +0.1 | 28 |
| 7 | Joel Embiid | PHI | +3.3 | +1.8 | +1.5 | 34 |
| 8 | Luka Doncic | LAL | +3.2 | +4.2 | -1.1 | 35 |
| 9 | Kyrie Irving | DAL | +2.6 | +2.6 | +0.0 | 26 |
| 10 | Franz Wagner | ORL | +2.5 | +0.9 | +1.6 | 33 |
| 11 | Dyson Daniels | ATL | +2.4 | +1.2 | +1.2 | 27 |
| 12 | Jimmy Butler III | GSW | +2.2 | +2.1 | +0.1 | 27 |
| 13 | Lauri Markkanen | UTA | +2.2 | +2.1 | +0.1 | 34 |
| 14 | Ausar Thompson | DET | +2.2 | +0.1 | +2.1 | 26 |
| 15 | LaMelo Ball | MIN | +2.1 | +4.3 | -2.1 | 24 |
| 16 | Fred VanVleet | HOU | +2.1 | +1.4 | +0.7 | 35 |
| 17 | Chet Holmgren | OKC | +2.1 | +0.1 | +2.0 | 30 |
| 18 | Rudy Gobert | MIN | +2.1 | -2.8 | +4.9 | 30 |
| 19 | Cade Cunningham | DET | +2.0 | +1.8 | +0.2 | 34 |
| 20 | Derrick White | BOS | +2.0 | +0.3 | +1.7 | 36 |
| 21 | Pascal Siakam | IND | +2.0 | +2.0 | +0.0 | 29 |
| 22 | Bam Adebayo | MIA | +1.7 | +1.0 | +0.6 | 31 |
| 23 | Jarrett Allen | CLE | +1.7 | +1.0 | +0.7 | 28 |
| 24 | Ty Jerome | MEM | +1.6 | +3.2 | -1.6 | 30 |
| 25 | Kevin Durant | HOU | +1.6 | +3.1 | -1.5 | 37 |
| 26 | Nickeil Alexander-Walker | ATL | +1.5 | +1.7 | -0.2 | 31 |
| 27 | Dean Wade | PHI | +1.4 | -0.1 | +1.5 | 25 |
| 28 | Jrue Holiday | POR | +1.3 | +0.3 | +1.0 | 30 |
| 29 | Damian Lillard | POR | +1.2 | +1.9 | -0.7 | 27 |
| 30 | Donovan Mitchell | CLE | +1.1 | +1.7 | -0.6 | 35 |

## Current model fit

- Fitted on 5325 games from 2022-23 to 2026-27.
- Home court: +2.0 points per 100 possessions for the home team over the visitor (about 2.0 points a game).
- Second night of a back-to-back: -0.7 points per 100 scored, +1.2 allowed.
- Weights: team efficiency ratings 0.16 (offense) and 0.16 (defense); player lineup ratings 0.76 and 0.75.
- Blend: 82% on the betting line for the margin and 100% for the total, wherever there is a line (fitted on past closing lines).
- Simulator: each team's points vary by 10.9 with correlation 0.23; 5.1% of recent games went to overtime.
