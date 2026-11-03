# NBA score predictions

Updated Tue Nov 03, 2026 02:32 AM ET. Refreshed automatically several times a day during the season, around the injury report's deadlines; each game's prediction is locked at tip-off and graded once the final score is in.

Each team's expected points are its expected possessions times its expected points per possession, from team efficiency ratings and the ratings of the players expected to play, blended with the betting line. Each game is then simulated 10,000 times, overtime included. The predicted score is the expected points rounded; the 80% range holds 80% of simulated outcomes for each team. Basketball is the most predictable major sport, but a team's score still varies by about ±14 points around the forecast, so read the win chance and the ranges too.

Missing players come from the injury report: out players are left out, and doubtful, questionable and probable ones count with the share of their minutes their chance of playing implies, and their minutes go mostly to the bench. The effect is how many points of margin the team gains or loses against its full-strength roster: negative when it is missing good players, positive when the minutes go to better ones. Predictions are rerun when the report changes, up to tip-off.

The fair moneyline is the American odds that match the win chance exactly, with no bookmaker margin: -150 means risk $150 to win $100, +150 means risk $100 to win $150.

The edge columns check every side of the spread, the moneyline and the total for expected value: the profit per $1 bet at the posted price, using the final prediction's chances (the model blended with the line, simulated against the posted lines, pushes returning the stake, and anchored to the market's own chances so only what the blend moves off the line counts). The model's own spread and total are shown alongside, but the blend keeps only the share of that disagreement the model has earned in past seasons, so edges are rare. A side is an edge when its EV is 3% or more; the best such side is shown with its price, its EV, its chance of winning the bet and its stake, a 25% share of the Kelly stake in units of 1% of the bankroll, with at most 3 units on one game. Where a spread or total price is not posted it is assumed to be -110 (marked \*); a moneyline is never assumed. Edges are logged with each prediction, locked at tip-off and graded below. Treat them as an experiment, not betting advice; see the backtest for how they have done on past seasons.

## Wednesday, November 4

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Spread: model / line | Total: model / line | 80% range | Overtime | Missing (effect on margin) | Spread edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 7:00 PM | PHI @ DET | PHI 109, DET 111 | DET 56% | PHI +130 / DET -130<br>posted PHI +106 / DET -125 | DET -2.2 / DET -1.5 (fav covers 54%) | 219.7 / 219.5 (over 49%) | 95–123 / 97–125 | 5% | PHI: Dominick Barlow (out) (+0.2)<br>DET: Jalen Duren (out) (-0.2) | no edge | no edge | no edge |
| 7:00 PM | ATL @ WAS | ATL 118, WAS 115 | ATL 56% | ATL -130 / WAS +130 | ATL -2.2 | 232.9 | 103–132 / 101–130 | 4% | ATL: Jalen Johnson (day-to-day) (+0.7)<br>WAS: Jamir Watkins (out); Alex Sarr (day-to-day); Justin Champagnie (out); Tristan Vukcevic (out) (+0.2) | no line yet | no line yet | no line yet |
| 7:30 PM | MIL @ BOS | MIL 106, BOS 123 | BOS 89% | MIL +840 / BOS -840 | BOS -17.2 | 228.7 | 91–120 / 109–137 | 2% | BOS: Devin Carter (out); Paul George (day-to-day) (+1.0) | no line yet | no line yet | no line yet |
| 7:30 PM | CHA @ BKN | CHA 108, BKN 106 | CHA 56% | CHA -125 / BKN +125<br>posted CHA -136 / BKN +115 | CHA -2 / CHA -2.5 (fav covers 50%) | 214.6 / 214.5 (over 50%) | 95–122 / 92–121 | 5% | CHA: Kon Knueppel (out); Grant Williams (out) (-0.6)<br>BKN: Egor Demin (out) (+0.7) | no edge | no edge | no edge |
| 7:30 PM | CHI @ NYK | CHI 111, NYK 123 | NYK 82% | CHI +465 / NYK -465 | NYK -12.6 | 234.4 | 96–126 / 109–138 | 4% | CHI: Nic Claxton (out) (+0.1) | no line yet | no line yet | no line yet |
| 8:00 PM | IND @ MEM | IND 112, MEM 117 | MEM 66% | IND +190 / MEM -190 | MEM -5.3 | 228.4 | 97–127 / 102–131 | 5% | IND: Pascal Siakam (day-to-day); Andrew Nembhard (day-to-day); Tyrese Haliburton (out); Aaron Nesmith (day-to-day); Kelly Oubre Jr. (day-to-day); Obi Toppin (out); Johnny Furphy (out); Larry Nance Jr. (day-to-day); Ben Sheppard (out); T.J. McConnell (out); Ivica Zubac (out) (-1.8)<br>MEM: Scotty Pippen Jr. (day-to-day); Quinten Post (day-to-day) (+0.1) | no line yet | no line yet | no line yet |
| 8:00 PM | UTA @ NOP | UTA 113, NOP 119 | NOP 64% | UTA +180 / NOP -180 | NOP -5 | 232.0 | 99–128 / 104–133 | 5% | UTA: Jaren Jackson Jr. (out); Trey Alexander (out); Jusuf Nurkic (out) (-1.0)<br>NOP: Dejounte Murray (out); Yves Missi (out); Jordan Poole (out) (+0.7) | no line yet | no line yet | no line yet |
| 8:00 PM | CLE @ OKC | CLE 114, OKC 113 | CLE 50% | CLE -100 / OKC +100 | pick'em | 226.2 | 99–128 / 99–127 | 6% | CLE: Peyton Watson (day-to-day); Jaylon Tyson (day-to-day) (+0.2)<br>OKC: Chet Holmgren (out); Jalen Williams (out); Alex Caruso (out); Cason Wallace (out) (-2.5) | no line yet | no line yet | no line yet |
| 8:30 PM | MIN @ HOU | MIN 108, HOU 116 | HOU 73% | MIN +265 / HOU -265<br>posted MIN +279 / HOU -348 | HOU -8 / HOU -8.5 (fav covers 49%) | 223.3 / 223.5 (over 49%) | 93–122 / 101–130 | 5% | MIN: Anthony Edwards (out); Terrence Shannon Jr. (day-to-day); Donte DiVincenzo (out) (-0.9)<br>HOU: Steven Adams (out); Clint Capela (out) (-0.6) | no edge | no edge | no edge |
| 9:00 PM | TOR @ DEN | TOR 112, DEN 117 | DEN 63% | TOR +170 / DEN -170 | DEN -4.7 | 229.5 | 98–127 / 103–131 | 5% | TOR: Kawhi Leonard (out); Jakob Poeltl (day-to-day) (-1.9)<br>DEN: Spencer Jones (out) (+1.0) | no line yet | no line yet | no line yet |
| 9:00 PM | POR @ PHX | POR 116, PHX 115 | POR 53% | POR -110 / PHX +110 | POR -0.8 | 230.6 | 101–131 / 100–130 | 5% | POR: Ja Morant (out) (-0.5)<br>PHX: Mark Williams (out); Jordan Goodwin (day-to-day) (+0.3) | no line yet | no line yet | no line yet |
| 9:30 PM | DAL @ SAS | DAL 109, SAS 121 | SAS 81% | DAL +415 / SAS -415<br>posted DAL +503 / SAS -700 | SAS -12 / SAS -12.5 (fav covers 48%) | 229.3 / 229.5 (over 49%) | 94–123 / 106–135 | 4% | DAL: Kyrie Irving (day-to-day); Santi Aldama (out); Max Christie (day-to-day); Dereck Lively II (out); Sergio de Larrea (out) (+0.5)<br>SAS: Tobias Harris (out) (+0.8) | no edge | no edge | no edge |
| 10:00 PM | LAL @ SAC | LAL 123, SAC 114 | LAL 73% | LAL -275 / SAC +275 | LAL -8.9 | 237.2 | 108–138 / 99–129 | 4% | SAC: Maxime Raynaud (out); Keegan Murray (out); Dylan Cardwell (out) (+0.0) | no line yet | no line yet | no line yet |
| 10:30 PM | MIA @ LAC | MIA 117, LAC 115 | MIA 57% | MIA -135 / LAC +135 | MIA -2.5 | 231.5 | 102–132 / 100–129 | 5% | LAC: Rui Hachimura (day-to-day); Derrick Jones Jr. (day-to-day); Brandon Ingram (out); Jordan Miller (out); Bradley Beal (out); Yanic Konan Niederhauser (out) (+0.1) | no line yet | no line yet | no line yet |

## Thursday, November 5

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Spread: model / line | Total: model / line | 80% range | Overtime | Missing (effect on margin) | Spread edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 9:00 PM | ORL @ PHX | ORL 114, PHX 113 | ORL 54% | ORL -115 / PHX +115 | ORL -1.3 | 227.5 | 100–129 / 99–128 | 5% | ORL: Paolo Banchero (out); Jalen Suggs (out); Anthony Black (day-to-day) (+0.6)<br>PHX: Mark Williams (out); Jordan Goodwin (day-to-day) (+0.3) | no line yet | no line yet | no line yet |
| 10:00 PM | MIA @ GSW | MIA 116, GSW 120 | GSW 62% | MIA +165 / GSW -165 | GSW -4 | 236.5 | 101–131 / 105–135 | 5% | GSW: Moses Moody (out); Jimmy Butler III (out); Kristaps Porzingis (out); Brandon Williams (day-to-day); Al Horford (day-to-day); Gui Santos (day-to-day) (-1.2) | no line yet | no line yet | no line yet |

## How the 2026-27 predictions have done

| Predictor | Games | Margin MAE | Total MAE | Team-points MAE | Log loss | Brier | Winners | 80% range hit |
|---|---|---|---|---|---|---|---|---|
| Final prediction | 92 | 11.33 | 15.48 | 9.86 | 0.579 | 0.199 | 68.5% | 79.3% |
| Model only (before blending) | 92 | 11.90 | 15.11 | 10.01 | 0.609 | 0.212 | 65.2% | – |
| Elo | 92 | 12.37 | – | – | 0.650 | 0.230 | 58.7% | – |
| Final prediction, games with a line | 92 | 11.33 | 15.48 | 9.86 | 0.579 | 0.199 | 68.5% | 79.3% |
| Model only, games with a line | 92 | 11.90 | 15.11 | 10.01 | 0.609 | 0.212 | 65.2% | – |
| Betting line | 92 | 11.24 | 15.45 | 9.82 | 0.567 | 0.194 | 68.5% | – |

MAE is the average miss in points; team-points MAE is the average miss on each team's score. Log loss and Brier score the win chances (lower is better; a coin flip scores 0.693 and 0.250). The closing line misses margins by about 10 points and totals by about 14.

Overtime: predicted in 4.8% of games, happened in 4.3%.

### Betting edges

| Market | Edges | Record (W-L-P) | Staked | Units won | ROI | Expected ROI |
|---|---|---|---|---|---|---|
| Spread | 1 | 1-0-0 | 1.0 | +0.90 | +89.3% | +3.6% |
| Moneyline | 5 | 0-5-0 | 1.9 | -1.88 | -100.0% | +8.8% |
| Total | 0 | 0-0-0 | 0.0 | +0.00 | – | – |

Spread moved toward the model's first spread edge before tip-off: 4 of 5 games (80%).

Live predictions only, each edge at the stake and price logged with the last prediction before tip-off (edges logged before edges were priced from the final prediction are left out); a push returns the stake. Units are 1% of the bankroll; ROI is units won per unit staked, and expected ROI is what the edges' EVs promised. The line moving toward the model's edge before tip-off is the quickest sign that it knows something the market doesn't yet.

### Results, Sunday, November 1

| Game | Predicted | Final | Win chance for winner | Spread: model / line | Inside 80% ranges |
|---|---|---|---|---|---|
| BOS @ ORL | 114–107 | 108–97 | 70% | BOS -6.7 / BOS -7.5 | yes |
| BKN @ IND | 114–117 | 98–90 | 40% | IND -3.5 / IND -3.5 | no |
| LAC @ GSW | 110–111 | 112–124 | 55% | GSW -1.6 / GSW -1.5 | yes |
| TOR @ LAL | 110–114 | 125–131 | 61% | LAL -3.6 / LAL -3.5 | no |

## Power ratings

Points per 100 possessions better than an average team on a neutral floor, combining opponent-adjusted team efficiency (garbage time removed) with the ratings of the team's healthy roster, through the fitted points map. Net per game uses the team's pace. Injury effect now is what its current injury report does to its margin, in points.

| # | Team | Net per 100 | Net per game | Offense | Defense | Pace | Injury effect now | Elo |
|---|---|---|---|---|---|---|---|---|
| 1 | HOU | +7.0 | +7.0 | +3.6 | +3.4 | 100.1 | -0.6 | 1623 |
| 2 | SAS | +6.8 | +7.0 | +2.2 | +4.6 | 102.2 | +0.8 | 1692 |
| 3 | BOS | +6.1 | +6.0 | +3.3 | +2.8 | 98.5 | +1.0 | 1629 |
| 4 | DET | +5.8 | +5.8 | +1.5 | +4.3 | 100.3 | -0.2 | 1647 |
| 5 | NYK | +4.0 | +4.0 | +1.3 | +2.8 | 99.0 | +0.0 | 1686 |
| 6 | MIN | +3.6 | +3.7 | +1.4 | +2.1 | 104.4 | -0.9 | 1598 |
| 7 | POR | +2.9 | +2.9 | +1.8 | +1.1 | 102.2 | -0.6 | 1537 |
| 8 | OKC | +2.6 | +2.7 | -0.8 | +3.4 | 100.6 | -2.5 | 1660 |
| 9 | LAL | +2.5 | +2.5 | +2.7 | -0.2 | 102.7 | +0.3 | 1578 |
| 10 | PHI | +2.3 | +2.4 | -0.2 | +2.5 | 102.0 | +0.2 | 1570 |
| 11 | CLE | +2.0 | +2.0 | +2.3 | -0.3 | 102.3 | +0.2 | 1585 |
| 12 | GSW | +2.0 | +2.0 | +1.6 | +0.4 | 101.1 | -1.2 | 1501 |
| 13 | TOR | +1.8 | +1.9 | +0.5 | +1.4 | 105.1 | -2.0 | 1547 |
| 14 | DEN | +1.6 | +1.6 | +2.9 | -1.3 | 99.1 | +1.0 | 1579 |
| 15 | MIA | +0.9 | +0.9 | +1.9 | -1.1 | 106.8 | +0.0 | 1501 |
| 16 | ORL | +0.4 | +0.4 | -1.3 | +1.7 | 100.5 | +0.6 | 1526 |
| 17 | DAL | -0.3 | -0.3 | -0.2 | -0.1 | 103.0 | +0.5 | 1456 |
| 18 | PHX | -0.6 | -0.6 | +1.5 | -2.1 | 101.6 | +0.3 | 1498 |
| 19 | MEM | -0.8 | -0.8 | +0.5 | -1.2 | 103.3 | +0.1 | 1426 |
| 20 | ATL | -1.0 | -1.0 | -0.5 | -0.5 | 107.0 | +0.8 | 1533 |
| 21 | IND | -2.2 | -2.2 | -0.1 | -2.1 | 101.1 | -1.8 | 1357 |
| 22 | CHA | -3.1 | -3.0 | -3.4 | +0.3 | 95.3 | -0.6 | 1523 |
| 23 | NOP | -3.6 | -3.8 | -1.8 | -1.8 | 107.4 | +0.7 | 1434 |
| 24 | LAC | -3.7 | -3.7 | -1.7 | -1.9 | 99.7 | +0.1 | 1489 |
| 25 | WAS | -4.5 | -4.6 | -2.5 | -2.0 | 102.5 | +0.2 | 1325 |
| 26 | UTA | -4.9 | -5.0 | -3.4 | -1.5 | 102.4 | -0.9 | 1309 |
| 27 | CHI | -6.0 | -6.8 | -3.0 | -3.0 | 113.1 | +0.1 | 1363 |
| 28 | BKN | -6.2 | -6.4 | -3.5 | -2.7 | 103.6 | +0.8 | 1304 |
| 29 | MIL | -7.4 | -7.9 | -2.8 | -4.6 | 106.5 | +0.0 | 1347 |
| 30 | SAC | -8.0 | -8.5 | -3.6 | -4.4 | 106.4 | +0.0 | 1325 |

## Top players

Regularized adjusted plus-minus from every lineup this season and past ones: points per 100 possessions a player adds on offense and saves on defense, against an average player, shrunk toward last season's rating. Players expected to play 20 minutes or more.

| # | Player | Team | Net impact per 100 | Offense | Defense | Expected minutes |
|---|---|---|---|---|---|---|
| 1 | Victor Wembanyama | SAS | +6.4 | +1.7 | +4.7 | 34 |
| 2 | Shai Gilgeous-Alexander | OKC | +5.8 | +5.0 | +0.8 | 31 |
| 3 | Nikola Jokic | DEN | +5.1 | +5.4 | -0.3 | 37 |
| 4 | Kawhi Leonard | TOR | +4.5 | +3.6 | +0.9 | 30 |
| 5 | Luka Doncic | LAL | +4.1 | +5.2 | -1.1 | 36 |
| 6 | Giannis Antetokounmpo | MIA | +3.8 | +3.9 | -0.1 | 31 |
| 7 | Kyrie Irving | DAL | +3.5 | +3.3 | +0.1 | 31 |
| 8 | Joel Embiid | PHI | +3.1 | +1.5 | +1.6 | 35 |
| 9 | Herbert Jones | NOP | +2.6 | -0.3 | +2.8 | 23 |
| 10 | Fred VanVleet | HOU | +2.5 | +1.8 | +0.7 | 32 |
| 11 | Marcus Smart | HOU | +2.5 | +1.3 | +1.2 | 24 |
| 12 | Franz Wagner | ORL | +2.4 | +1.1 | +1.3 | 37 |
| 13 | Jimmy Butler III | GSW | +2.2 | +2.1 | +0.1 | 27 |
| 14 | Chet Holmgren | OKC | +2.1 | +0.0 | +2.0 | 30 |
| 15 | Lauri Markkanen | UTA | +2.0 | +1.7 | +0.2 | 26 |
| 16 | Jarrett Allen | CLE | +2.0 | +1.2 | +0.7 | 27 |
| 17 | Ausar Thompson | DET | +2.0 | -0.3 | +2.2 | 27 |
| 18 | Ty Jerome | MEM | +1.9 | +3.3 | -1.4 | 28 |
| 19 | Derrick White | BOS | +1.8 | +0.2 | +1.6 | 31 |
| 20 | Bam Adebayo | MIA | +1.8 | +1.4 | +0.4 | 32 |
| 21 | Rudy Gobert | MIN | +1.8 | -3.3 | +5.1 | 28 |
| 22 | Cade Cunningham | DET | +1.8 | +1.6 | +0.1 | 33 |
| 23 | Neemias Queta | BOS | +1.7 | +0.8 | +0.9 | 22 |
| 24 | Dyson Daniels | ATL | +1.7 | +0.7 | +1.0 | 28 |
| 25 | LaMelo Ball | MIN | +1.6 | +3.8 | -2.1 | 25 |
| 26 | Kevin Durant | HOU | +1.5 | +3.2 | -1.7 | 32 |
| 27 | Donovan Mitchell | CLE | +1.5 | +2.3 | -0.8 | 30 |
| 28 | Pascal Siakam | IND | +1.5 | +1.6 | -0.2 | 33 |
| 29 | Stephen Curry | GSW | +1.4 | +4.1 | -2.7 | 30 |
| 30 | Dean Wade | PHI | +1.3 | -0.2 | +1.5 | 26 |

## Current model fit

- Fitted on 5374 games from 2022-23 to 2026-27.
- Home court: +2.0 points per 100 possessions for the home team over the visitor (about 2.0 points a game).
- Second night of a back-to-back: -0.7 points per 100 scored, +1.2 allowed.
- Weights: team efficiency ratings 0.16 (offense) and 0.15 (defense); player lineup ratings 0.76 and 0.76.
- Blend: 82% on the betting line for the margin and 100% for the total, wherever there is a line (fitted on past closing lines).
- Simulator: each team's points vary by 11.0 with correlation 0.23; 5.1% of recent games went to overtime.
