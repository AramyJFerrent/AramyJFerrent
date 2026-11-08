# NBA score predictions

Updated Sun Nov 08, 2026 01:26 PM ET. Refreshed automatically several times a day during the season, around the injury report's deadlines; each game's prediction is locked at tip-off and graded once the final score is in.

Each team's expected points are its expected possessions times its expected points per possession, from team efficiency ratings and the ratings of the players expected to play, blended with the betting line. Each game is then simulated 10,000 times, overtime included. The predicted score is the expected points rounded; the 80% range holds 80% of simulated outcomes for each team. Basketball is the most predictable major sport, but a team's score still varies by about ±14 points around the forecast, so read the win chance and the ranges too.

Missing players come from the injury report: out players are left out, and doubtful, questionable and probable ones count with the share of their minutes their chance of playing implies, and their minutes go mostly to the bench. The effect is how many points of margin the team gains or loses against its full-strength roster: negative when it is missing good players, positive when the minutes go to better ones. Predictions are rerun when the report changes, up to tip-off.

The fair moneyline is the American odds that match the win chance exactly, with no bookmaker margin: -150 means risk $150 to win $100, +150 means risk $100 to win $150.

The edge columns check every side of the spread, the moneyline and the total for expected value: the profit per $1 bet at the posted price, using the final prediction's chances (the model blended with the line, simulated against the posted lines, pushes returning the stake, and anchored to the market's own chances so only what the blend moves off the line counts). The model's own spread and total are shown alongside, but the blend keeps only the share of that disagreement the model has earned in past seasons, so edges are rare. A side is an edge when its EV is 3% or more; the best such side is shown with its price, its EV, its chance of winning the bet and its stake, a 25% share of the Kelly stake in units of 1% of the bankroll, with at most 3 units on one game. Where a spread or total price is not posted it is assumed to be -110 (marked \*); a moneyline is never assumed. Edges are logged with each prediction, locked at tip-off and graded below. Treat them as an experiment, not betting advice; see the backtest for how they have done on past seasons.

## Sunday, November 8

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Spread: model / line | Total: model / line | 80% range | Overtime | Missing (effect on margin) | Spread edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 3:30 PM | PHI @ CHI | PHI 124, CHI 115 | PHI 75% | PHI -300 / CHI +300<br>posted PHI -420 / CHI +329 | PHI -9.5 / PHI -9.5 (fav covers 48%) | 238.7 / 238.5 (over 50%) | 109–139 / 100–130 | 5% | PHI: Joel Embiid (day-to-day); Adem Bona (out); Dominick Barlow (out) (-0.2)<br>CHI: Norman Powell (day-to-day); Nic Claxton (out); Jalen Smith (day-to-day) (-1.0) | no edge | no edge | no edge |
| 6:00 PM | LAL @ DET | LAL 106, DET 113 | DET 70% | LAL +235 / DET -235<br>posted LAL +221 / DET -269 | DET -6.9 / DET -7.5 (fav covers 49%) | 218.4 / 218.5 (over 49%) | 91–120 / 99–126 | 5% | LAL: Luka Doncic (day-to-day) (-0.9)<br>DET: Jalen Duren (out) (-0.1) | no edge | no edge | no edge |
| 7:00 PM | UTA @ MIN | UTA 104, MIN 117 | MIN 83% | UTA +475 / MIN -475<br>posted UTA +470 / MIN -650 | MIN -12.5 / MIN -12.5 (fav covers 48%) | 221.3 / 221.5 (over 50%) | 90–119 / 103–131 | 3% | UTA: Keyonte George (day-to-day); Lauri Markkanen (day-to-day); Jaren Jackson Jr. (out); Jusuf Nurkic (out) (-1.5)<br>MIN: Anthony Edwards (out); Donte DiVincenzo (out) (-0.7) | no edge | no edge | no edge |
| 7:30 PM | BKN @ DAL | BKN 107, DAL 115 | DAL 71% | BKN +250 / DAL -250<br>posted BKN +261 / DAL -324 | DAL -7.5 / DAL -7.5 (fav covers 50%) | 222.4 / 222.5 (over 49%) | 93–122 / 101–129 | 4% | BKN: Mikel Brown Jr. (out); Egor Demin (out) (+1.6)<br>DAL: Dereck Lively II (out); Sergio de Larrea (out) (+0.9) | no edge | no edge | no edge |
| 8:00 PM | BOS @ MIL | BOS 117, MIL 104 | BOS 83% | BOS -485 / MIL +485<br>posted BOS -750 / MIL +530 | BOS -12.4 / BOS -12.5 (fav covers 48%) | 221.1 / 221.5 (over 48%) | 103–131 / 90–119 | 4% | BOS: Mitchell Robinson (day-to-day) (+0.1) | no edge | no edge | no edge |
| 9:00 PM | NOP @ LAC | NOP 114, LAC 113 | NOP 54% | NOP -115 / LAC +115<br>posted NOP -121 / LAC +103 | NOP -1 / NOP -1.5 (fav covers 51%) | 226.7 / 226.5 (over 50%) | 99–128 / 98–127 | 6% | NOP: Yves Missi (out) (+0.5)<br>LAC: Brandon Ingram (out); Jordan Miller (out); Bradley Beal (out); Isaiah Jackson (out); Yanic Konan Niederhauser (out) (+0.3) | no edge | no edge | no edge |
| 9:00 PM | MIA @ SAC | MIA 123, SAC 114 | MIA 76% | MIA -315 / SAC +315<br>posted MIA -446 / SAC +346 | MIA -9.6 / MIA -10.5 (fav covers 46%) | 237.2 / 237.5 (over 48%) | 109–138 / 99–129 | 4% | SAC: Maxime Raynaud (out); Keegan Murray (out) (+0.0) | no edge | SAC ML (+346): EV +3.8%, 23%, stake 0.3u | no edge |

## Monday, November 9

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Spread: model / line | Total: model / line | 80% range | Overtime | Missing (effect on margin) | Spread edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 7:00 PM | LAL @ ATL | LAL 120, ATL 119 | LAL 54% | LAL -120 / ATL +120 | LAL -1.3 | 239.1 | 105–135 / 104–134 | 5% | LAL: Luka Doncic (day-to-day) (-0.9)<br>ATL: Keshon Gilbert (day-to-day) (+1.0) | no line yet | no line yet | no line yet |
| 7:00 PM | CLE @ CHA | CLE 112, CHA 105 | CLE 70% | CLE -235 / CHA +235 | CLE -7 | 217.7 | 98–126 / 91–120 | 5% | CLE: Sam Merrill (day-to-day); Jarrett Allen (day-to-day); Jaylon Tyson (out) (-0.2)<br>CHA: Moussa Diabate (day-to-day); Dennis Schroder (out); Brandon Miller (day-to-day); Kon Knueppel (out); Grant Williams (out) (-1.5) | no line yet | no line yet | no line yet |
| 7:00 PM | WAS @ DET | WAS 104, DET 117 | DET 83% | WAS +495 / DET -495 | DET -12.6 | 220.4 | 89–119 / 103–130 | 4% | WAS: Anthony Davis (day-to-day); Jamir Watkins (out); Justin Champagnie (out); Deandre Ayton (day-to-day); Tristan Vukcevic (out) (-0.6)<br>DET: Jalen Duren (out) (-0.1) | no line yet | no line yet | no line yet |
| 7:30 PM | MEM @ TOR | MEM 115, TOR 118 | TOR 58% | MEM +140 / TOR -140 | TOR -2.7 | 233.7 | 101–130 / 104–133 | 5% | MEM: Isaiah Stewart (out); Scotty Pippen Jr. (out) (+0.3)<br>TOR: Scottie Barnes (day-to-day); Immanuel Quickley (day-to-day); Kawhi Leonard (out) (-2.4) | no line yet | no line yet | no line yet |
| 8:00 PM | IND @ DAL | IND 111, DAL 114 | DAL 59% | IND +140 / DAL -140 | DAL -2.9 | 225.3 | 97–126 / 100–129 | 5% | IND: Tyrese Haliburton (out); Johnny Furphy (out); Ben Sheppard (out) (-0.3)<br>DAL: Dereck Lively II (out); Sergio de Larrea (out) (+0.9) | no line yet | no line yet | no line yet |
| 8:30 PM | DEN @ HOU | DEN 109, HOU 114 | HOU 65% | DEN +185 / HOU -185 | HOU -4.9 | 222.8 | 95–124 / 99–128 | 5% | HOU: Steven Adams (out); Clint Capela (out) (-0.6) | no line yet | no line yet | no line yet |
| 9:00 PM | SAS @ PHX | SAS 117, PHX 112 | SAS 66% | SAS -190 / PHX +190 | SAS -5.2 | 228.4 | 102–131 / 97–126 | 5% | SAS: Tobias Harris (out) (+0.7)<br>PHX: Mark Williams (out); Jordan Goodwin (out) (+0.3) | no line yet | no line yet | no line yet |
| 10:00 PM | NOP @ GSW | NOP 112, GSW 121 | GSW 74% | NOP +285 / GSW -285 | GSW -8.6 | 232.6 | 97–127 / 106–135 | 4% | NOP: Yves Missi (out) (+0.5)<br>GSW: Moses Moody (out); Jimmy Butler III (out); Kristaps Porzingis (out) (-0.8) | no line yet | no line yet | no line yet |

## How the 2026-27 predictions have done

| Predictor | Games | Margin MAE | Total MAE | Team-points MAE | Log loss | Brier | Winners | 80% range hit |
|---|---|---|---|---|---|---|---|---|
| Final prediction | 139 | 10.94 | 14.52 | 9.39 | 0.563 | 0.191 | 71.2% | 81.3% |
| Model only (before blending) | 139 | 11.38 | 14.30 | 9.50 | 0.589 | 0.203 | 69.1% | – |
| Elo | 139 | 11.75 | – | – | 0.611 | 0.213 | 64.0% | – |
| Final prediction, games with a line | 139 | 10.94 | 14.52 | 9.39 | 0.563 | 0.191 | 71.2% | 81.3% |
| Model only, games with a line | 139 | 11.38 | 14.30 | 9.50 | 0.589 | 0.203 | 69.1% | – |
| Betting line | 139 | 10.87 | 14.51 | 9.38 | 0.553 | 0.187 | 71.2% | – |

MAE is the average miss in points; team-points MAE is the average miss on each team's score. Log loss and Brier score the win chances (lower is better; a coin flip scores 0.693 and 0.250). The closing line misses margins by about 10 points and totals by about 14.

Overtime: predicted in 4.7% of games, happened in 5.8%.

### Betting edges

| Market | Edges | Record (W-L-P) | Staked | Units won | ROI | Expected ROI |
|---|---|---|---|---|---|---|
| Spread | 1 | 1-0-0 | 1.0 | +0.90 | +89.3% | +3.6% |
| Moneyline | 7 | 0-7-0 | 2.3 | -2.26 | -100.0% | +8.1% |
| Total | 0 | 0-0-0 | 0.0 | +0.00 | – | – |

Spread moved toward the model's first spread edge before tip-off: 4 of 5 games (80%).

Live predictions only, each edge at the stake and price logged with the last prediction before tip-off (edges logged before edges were priced from the final prediction are left out); a push returns the stake. Units are 1% of the bankroll; ROI is units won per unit staked, and expected ROI is what the edges' EVs promised. The line moving toward the model's edge before tip-off is the quickest sign that it knows something the market doesn't yet.

### Results, Saturday, November 7

| Game | Predicted | Final | Win chance for winner | Spread: model / line | Inside 80% ranges |
|---|---|---|---|---|---|
| DEN @ IND | 119–111 | 114–102 | 72% | DEN -7.9 / DEN -8.5 | yes |
| BKN @ ATL | 110–116 | 121–124 | 68% | ATL -6.3 / ATL -6.5 | yes |
| NYK @ CLE | 114–109 | 109–97 | 63% | NYK -4.2 / NYK -4.5 | yes |
| WAS @ OKC | 106–118 | 75–114 | 82% | OKC -12.7 / OKC -12.5 | no |
| ORL @ GSW | 107–114 | 119–126 (OT) | 70% | GSW -7.3 / GSW -7.5 | yes |
| HOU @ PHX | 115–109 | 99–102 | 32% | HOU -6.2 / HOU -6.5 | no |
| SAS @ POR | 117–112 | 125–103 | 63% | SAS -4.7 / SAS -5.5 | yes |

## Power ratings

Points per 100 possessions better than an average team on a neutral floor, combining opponent-adjusted team efficiency (garbage time removed) with the ratings of the team's healthy roster, through the fitted points map. Net per game uses the team's pace. Injury effect now is what its current injury report does to its margin, in points.

| # | Team | Net per 100 | Net per game | Offense | Defense | Pace | Injury effect now | Elo |
|---|---|---|---|---|---|---|---|---|
| 1 | HOU | +7.0 | +7.0 | +3.3 | +3.8 | 98.7 | -0.6 | 1613 |
| 2 | SAS | +6.9 | +7.1 | +2.9 | +4.1 | 102.3 | +0.7 | 1712 |
| 3 | BOS | +6.6 | +6.4 | +3.4 | +3.2 | 96.8 | +0.1 | 1640 |
| 4 | DET | +6.5 | +6.5 | +2.3 | +4.2 | 100.9 | -0.1 | 1653 |
| 5 | MIN | +5.6 | +5.7 | +2.7 | +3.0 | 102.5 | -0.7 | 1620 |
| 6 | LAL | +4.8 | +4.9 | +4.4 | +0.4 | 102.2 | -0.9 | 1598 |
| 7 | NYK | +4.0 | +3.8 | +1.4 | +2.6 | 95.2 | -0.1 | 1701 |
| 8 | OKC | +3.9 | +3.9 | -0.2 | +4.1 | 102.2 | -0.2 | 1685 |
| 9 | DEN | +3.2 | +3.2 | +4.1 | -0.9 | 97.6 | +0.2 | 1582 |
| 10 | GSW | +3.0 | +3.1 | +2.0 | +1.0 | 102.0 | -0.8 | 1523 |
| 11 | PHI | +2.4 | +2.4 | -0.4 | +2.8 | 102.1 | -0.2 | 1573 |
| 12 | POR | +1.9 | +2.0 | +1.8 | +0.1 | 102.6 | -0.6 | 1544 |
| 13 | CLE | +1.7 | +1.8 | +2.0 | -0.3 | 101.6 | -0.2 | 1578 |
| 14 | TOR | +0.6 | +0.7 | +0.3 | +0.4 | 105.0 | -2.5 | 1552 |
| 15 | PHX | +0.2 | +0.2 | +1.3 | -1.1 | 101.4 | +0.3 | 1498 |
| 16 | MIA | -0.5 | -0.5 | +0.8 | -1.3 | 106.0 | +0.0 | 1485 |
| 17 | DAL | -0.6 | -0.6 | -0.4 | -0.2 | 100.9 | +0.9 | 1436 |
| 18 | ORL | -1.6 | -1.6 | -2.5 | +0.8 | 100.1 | -0.1 | 1489 |
| 19 | ATL | -2.1 | -2.3 | -0.7 | -1.4 | 108.5 | +1.0 | 1549 |
| 20 | IND | -2.5 | -2.5 | -1.0 | -1.4 | 102.2 | -0.3 | 1358 |
| 21 | NOP | -2.5 | -2.6 | -0.8 | -1.7 | 104.6 | +0.5 | 1438 |
| 22 | MEM | -2.6 | -2.7 | -0.7 | -2.0 | 103.7 | +0.3 | 1402 |
| 23 | LAC | -3.2 | -3.2 | -1.7 | -1.5 | 100.1 | +0.3 | 1476 |
| 24 | UTA | -3.9 | -3.9 | -3.5 | -0.3 | 101.7 | -1.5 | 1299 |
| 25 | BKN | -5.3 | -5.4 | -3.0 | -2.3 | 102.6 | +1.6 | 1317 |
| 26 | WAS | -5.4 | -5.5 | -3.2 | -2.2 | 100.9 | -0.6 | 1331 |
| 27 | CHA | -6.1 | -5.8 | -4.8 | -1.3 | 96.1 | -1.4 | 1467 |
| 28 | MIL | -7.2 | -7.5 | -2.8 | -4.4 | 103.9 | +0.0 | 1335 |
| 29 | CHI | -7.4 | -8.2 | -3.7 | -3.7 | 111.8 | -1.0 | 1356 |
| 30 | SAC | -7.6 | -7.8 | -3.2 | -4.3 | 102.8 | +0.0 | 1340 |

## Top players

Regularized adjusted plus-minus from every lineup this season and past ones: points per 100 possessions a player adds on offense and saves on defense, against an average player, shrunk toward last season's rating. Players expected to play 20 minutes or more.

| # | Player | Team | Net impact per 100 | Offense | Defense | Expected minutes |
|---|---|---|---|---|---|---|
| 1 | Victor Wembanyama | SAS | +7.4 | +2.2 | +5.2 | 27 |
| 2 | Shai Gilgeous-Alexander | OKC | +6.0 | +5.2 | +0.8 | 31 |
| 3 | Nikola Jokic | DEN | +5.3 | +5.2 | +0.1 | 35 |
| 4 | Luka Doncic | LAL | +4.6 | +5.5 | -0.9 | 36 |
| 5 | Kawhi Leonard | TOR | +4.5 | +3.6 | +0.9 | 30 |
| 6 | Giannis Antetokounmpo | MIA | +3.5 | +3.5 | +0.0 | 34 |
| 7 | Kyrie Irving | DAL | +3.3 | +3.5 | -0.1 | 31 |
| 8 | Herbert Jones | NOP | +3.2 | -0.1 | +3.3 | 24 |
| 9 | Joel Embiid | PHI | +3.1 | +1.3 | +1.8 | 29 |
| 10 | Donovan Mitchell | CLE | +2.7 | +3.1 | -0.4 | 34 |
| 11 | LaMelo Ball | MIN | +2.6 | +4.4 | -1.8 | 31 |
| 12 | Stephen Curry | GSW | +2.4 | +4.6 | -2.2 | 32 |
| 13 | Fred VanVleet | HOU | +2.4 | +1.7 | +0.7 | 30 |
| 14 | Jimmy Butler III | GSW | +2.2 | +2.1 | +0.1 | 27 |
| 15 | Ausar Thompson | DET | +2.1 | +0.0 | +2.1 | 29 |
| 16 | Chet Holmgren | OKC | +2.1 | +0.0 | +2.0 | 30 |
| 17 | Marcus Smart | HOU | +2.0 | +1.0 | +1.0 | 21 |
| 18 | Franz Wagner | ORL | +2.0 | +1.0 | +1.0 | 39 |
| 19 | Rudy Gobert | MIN | +2.0 | -3.0 | +4.9 | 29 |
| 20 | Dyson Daniels | ATL | +1.9 | +0.4 | +1.5 | 32 |
| 21 | Neemias Queta | BOS | +1.9 | +0.8 | +1.1 | 22 |
| 22 | Cade Cunningham | DET | +1.8 | +1.6 | +0.2 | 34 |
| 23 | Derrick White | BOS | +1.8 | +0.2 | +1.5 | 30 |
| 24 | Pascal Siakam | IND | +1.7 | +1.6 | +0.1 | 32 |
| 25 | Ty Jerome | MEM | +1.7 | +3.0 | -1.3 | 30 |
| 26 | Dean Wade | PHI | +1.7 | +0.3 | +1.4 | 23 |
| 27 | Bam Adebayo | MIA | +1.7 | +1.3 | +0.3 | 34 |
| 28 | Paul Reed | DET | +1.6 | +0.2 | +1.3 | 29 |
| 29 | De'Aaron Fox | SAS | +1.5 | +1.5 | +0.0 | 26 |
| 30 | Lauri Markkanen | UTA | +1.4 | +1.2 | +0.2 | 33 |

## Current model fit

- Fitted on 5421 games from 2022-23 to 2026-27.
- Home court: +2.0 points per 100 possessions for the home team over the visitor (about 2.0 points a game).
- Second night of a back-to-back: -0.7 points per 100 scored, +1.2 allowed.
- Weights: team efficiency ratings 0.16 (offense) and 0.15 (defense); player lineup ratings 0.76 and 0.76.
- Blend: 82% on the betting line for the margin and 100% for the total, wherever there is a line (fitted on past closing lines).
- Simulator: each team's points vary by 10.9 with correlation 0.23; 5.2% of recent games went to overtime.
