# NBA score predictions

Updated Sat Nov 07, 2026 01:48 AM ET. Refreshed automatically several times a day during the season, around the injury report's deadlines; each game's prediction is locked at tip-off and graded once the final score is in.

Each team's expected points are its expected possessions times its expected points per possession, from team efficiency ratings and the ratings of the players expected to play, blended with the betting line. Each game is then simulated 10,000 times, overtime included. The predicted score is the expected points rounded; the 80% range holds 80% of simulated outcomes for each team. Basketball is the most predictable major sport, but a team's score still varies by about ±14 points around the forecast, so read the win chance and the ranges too.

Missing players come from the injury report: out players are left out, and doubtful, questionable and probable ones count with the share of their minutes their chance of playing implies, and their minutes go mostly to the bench. The effect is how many points of margin the team gains or loses against its full-strength roster: negative when it is missing good players, positive when the minutes go to better ones. Predictions are rerun when the report changes, up to tip-off.

The fair moneyline is the American odds that match the win chance exactly, with no bookmaker margin: -150 means risk $150 to win $100, +150 means risk $100 to win $150.

The edge columns check every side of the spread, the moneyline and the total for expected value: the profit per $1 bet at the posted price, using the final prediction's chances (the model blended with the line, simulated against the posted lines, pushes returning the stake, and anchored to the market's own chances so only what the blend moves off the line counts). The model's own spread and total are shown alongside, but the blend keeps only the share of that disagreement the model has earned in past seasons, so edges are rare. A side is an edge when its EV is 3% or more; the best such side is shown with its price, its EV, its chance of winning the bet and its stake, a 25% share of the Kelly stake in units of 1% of the bankroll, with at most 3 units on one game. Where a spread or total price is not posted it is assumed to be -110 (marked \*); a moneyline is never assumed. Edges are logged with each prediction, locked at tip-off and graded below. Treat them as an experiment, not betting advice; see the backtest for how they have done on past seasons.

## Saturday, November 7

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Spread: model / line | Total: model / line | 80% range | Overtime | Missing (effect on margin) | Spread edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 5:00 PM | DEN @ IND | DEN 118, IND 111 | DEN 70% | DEN -235 / IND +235<br>posted DEN -268 / IND +220 | DEN -7 / DEN -7.5 (fav covers 49%) | 229.5 / 229.5 (over 50%) | 104–133 / 97–126 | 4% | DEN: DeMar DeRozan (day-to-day) (+0.3)<br>IND: Tyrese Haliburton (out); Johnny Furphy (out); Ben Sheppard (out); T.J. McConnell (out); Kelly Oubre Jr. (day-to-day) (-0.4) | no edge | no edge | no edge |
| 7:30 PM | BKN @ ATL | BKN 109, ATL 115 | ATL 68% | BKN +210 / ATL -210<br>posted BKN +212 / ATL -258 | ATL -6.3 / ATL -6.5 (fav covers 50%) | 224.7 / 224.5 (over 50%) | 94–124 / 101–130 | 5% | BKN: Day'Ron Sharpe (day-to-day); Egor Demin (out) (+0.4)<br>ATL: Jalen Johnson (out); Keshon Gilbert (out) (+2.2) | no edge | no edge | no edge |
| 8:00 PM | NYK @ CLE | NYK 115, CLE 111 | NYK 63% | NYK -170 / CLE +170<br>posted NYK -191 / CLE +160 | NYK -4.3 / NYK -4.5 (fav covers 51%) | 225.7 / 225.5 (over 49%) | 101–129 / 96–125 | 5% | NYK: Josh Hart (out) (-0.3)<br>CLE: Sam Merrill (out); Jarrett Allen (out); Jaylon Tyson (out) (-2.1) | no edge | no edge | no edge |
| 8:00 PM | WAS @ OKC | WAS 104, OKC 116 | OKC 81% | WAS +425 / OKC -425<br>posted WAS +373 / OKC -486 | OKC -11.5 / OKC -11.5 (fav covers 48%) | 220.4 / 220.5 (over 49%) | 90–119 / 102–130 | 4% | WAS: Anthony Davis (out); Jamir Watkins (out); Justin Champagnie (out); Tristan Vukcevic (out) (-2.3)<br>OKC: Chet Holmgren (out); Jalen Williams (out); Jaylin Williams (out); Cason Wallace (out) (-0.1) | no edge | no edge | no edge |
| 8:30 PM | ORL @ GSW | ORL 108, GSW 114 | GSW 68% | ORL +210 / GSW -210<br>posted ORL +212 / GSW -258 | GSW -6.1 / GSW -6.5 (fav covers 50%) | 221.5 / 221.5 (over 49%) | 93–122 / 100–128 | 5% | ORL: Paolo Banchero (out); Jalen Suggs (out) (+0.3)<br>GSW: Moses Moody (out); Jimmy Butler III (out); Draymond Green (day-to-day); Kristaps Porzingis (out); Gui Santos (day-to-day); Gary Payton II (day-to-day) (-1.1) | no edge | no edge | no edge |
| 9:00 PM | HOU @ PHX | HOU 114, PHX 107 | HOU 70% | HOU -235 / PHX +235<br>posted HOU -308 / PHX +249 | HOU -6.9 / HOU -7.5 (fav covers 50%) | 220.4 / 220.5 (over 49%) | 100–127 / 93–121 | 4% | HOU: Steven Adams (out); Clint Capela (out) (-0.6)<br>PHX: Mark Williams (out); Jordan Goodwin (day-to-day) (+0.4) | no edge | no edge | no edge |
| 10:00 PM | SAS @ POR | SAS 116, POR 113 | SAS 59% | SAS -140 / POR +140<br>posted SAS -152 / POR +128 | SAS -3.1 / SAS -3.5 (fav covers 50%) | 228.7 / 228.5 (over 49%) | 101–130 / 98–127 | 5% | SAS: Tobias Harris (out) (+0.7)<br>POR: Ja Morant (out) (+0.0) | no edge | no edge | no edge |

## Sunday, November 8

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Spread: model / line | Total: model / line | 80% range | Overtime | Missing (effect on margin) | Spread edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 3:30 PM | PHI @ CHI | PHI 123, CHI 112 | PHI 79% | PHI -370 / CHI +370 | PHI -11 | 235.5 | 109–138 / 97–127 | 4% | PHI: Adem Bona (out); Dominick Barlow (out) (+0.8)<br>CHI: Nic Claxton (out); Jalen Smith (day-to-day) (-0.5) | no line yet | no line yet | no line yet |
| 6:00 PM | LAL @ DET | LAL 111, DET 115 | DET 62% | LAL +160 / DET -160 | DET -4 | 226.5 | 97–126 / 101–130 | 5% | DET: Jalen Duren (out) (-0.1) | no line yet | no line yet | no line yet |
| 7:00 PM | UTA @ MIN | UTA 105, MIN 118 | MIN 83% | UTA +470 / MIN -470 | MIN -12.6 | 223.2 | 91–120 / 104–132 | 4% | UTA: Jaren Jackson Jr. (out); Trey Alexander (out); Jusuf Nurkic (out) (-0.7)<br>MIN: Anthony Edwards (out); Terrence Shannon Jr. (out); Donte DiVincenzo (out); Joan Beringer (out) (+0.5) | no line yet | no line yet | no line yet |
| 7:30 PM | BKN @ DAL | BKN 108, DAL 117 | DAL 76% | BKN +315 / DAL -315 | DAL -9.4 | 224.5 | 93–122 / 103–131 | 4% | BKN: Day'Ron Sharpe (day-to-day); Egor Demin (out) (+0.4)<br>DAL: Dereck Lively II (out); Sergio de Larrea (out) (+0.8) | no line yet | no line yet | no line yet |
| 8:00 PM | BOS @ MIL | BOS 118, MIL 106 | BOS 81% | BOS -430 / MIL +430 | BOS -12 | 224.0 | 104–132 / 91–121 | 4% | BOS: Devin Carter (out) (+1.2)<br>MIL: Kam Jones (day-to-day) (+0.2) | no line yet | no line yet | no line yet |
| 9:00 PM | NOP @ LAC | NOP 114, LAC 115 | LAC 53% | NOP +115 / LAC -115 | LAC -1.2 | 228.9 | 99–128 / 100–130 | 5% | NOP: Yves Missi (out) (+0.5)<br>LAC: Brandon Ingram (out); Jordan Miller (out); Bradley Beal (out); Yanic Konan Niederhauser (out) (+0.5) | no line yet | no line yet | no line yet |
| 9:00 PM | MIA @ SAC | MIA 121, SAC 116 | MIA 65% | MIA -190 / SAC +190 | MIA -5.2 | 237.7 | 107–136 / 101–131 | 5% | SAC: De'Andre Hunter (out); Maxime Raynaud (out); Keegan Murray (out) (-0.1) | no line yet | no line yet | no line yet |

## How the 2026-27 predictions have done

| Predictor | Games | Margin MAE | Total MAE | Team-points MAE | Log loss | Brier | Winners | 80% range hit |
|---|---|---|---|---|---|---|---|---|
| Final prediction | 123 | 10.96 | 14.49 | 9.34 | 0.578 | 0.198 | 69.1% | 81.3% |
| Model only (before blending) | 123 | 11.41 | 14.25 | 9.46 | 0.605 | 0.211 | 66.7% | – |
| Elo | 123 | 11.78 | – | – | 0.639 | 0.227 | 60.2% | – |
| Final prediction, games with a line | 123 | 10.96 | 14.49 | 9.34 | 0.578 | 0.198 | 69.1% | 81.3% |
| Model only, games with a line | 123 | 11.41 | 14.25 | 9.46 | 0.605 | 0.211 | 66.7% | – |
| Betting line | 123 | 10.88 | 14.48 | 9.32 | 0.567 | 0.194 | 69.1% | – |

MAE is the average miss in points; team-points MAE is the average miss on each team's score. Log loss and Brier score the win chances (lower is better; a coin flip scores 0.693 and 0.250). The closing line misses margins by about 10 points and totals by about 14.

Overtime: predicted in 4.7% of games, happened in 5.7%.

### Betting edges

| Market | Edges | Record (W-L-P) | Staked | Units won | ROI | Expected ROI |
|---|---|---|---|---|---|---|
| Spread | 1 | 1-0-0 | 1.0 | +0.90 | +89.3% | +3.6% |
| Moneyline | 6 | 0-6-0 | 2.1 | -2.06 | -100.0% | +8.3% |
| Total | 0 | 0-0-0 | 0.0 | +0.00 | – | – |

Spread moved toward the model's first spread edge before tip-off: 4 of 5 games (80%).

Live predictions only, each edge at the stake and price logged with the last prediction before tip-off (edges logged before edges were priced from the final prediction are left out); a push returns the stake. Units are 1% of the bankroll; ROI is units won per unit staked, and expected ROI is what the edges' EVs promised. The line moving toward the model's edge before tip-off is the quickest sign that it knows something the market doesn't yet.

### Results, Thursday, November 5

| Game | Predicted | Final | Win chance for winner | Spread: model / line | Inside 80% ranges |
|---|---|---|---|---|---|
| ORL @ PHX | 111–112 | 104–117 | 54% | PHX -1.2 / PHX -1.5 | yes |
| MIA @ GSW | 116–120 | 100–120 | 59% | GSW -3.5 / GSW -3.5 | no |

## Power ratings

Points per 100 possessions better than an average team on a neutral floor, combining opponent-adjusted team efficiency (garbage time removed) with the ratings of the team's healthy roster, through the fitted points map. Net per game uses the team's pace. Injury effect now is what its current injury report does to its margin, in points.

| # | Team | Net per 100 | Net per game | Offense | Defense | Pace | Injury effect now | Elo |
|---|---|---|---|---|---|---|---|---|
| 1 | HOU | +7.0 | +7.0 | +3.8 | +3.2 | 99.1 | -0.6 | 1620 |
| 2 | DET | +6.4 | +6.4 | +2.2 | +4.2 | 101.1 | -0.1 | 1653 |
| 3 | SAS | +6.4 | +6.5 | +1.9 | +4.5 | 102.6 | +0.7 | 1695 |
| 4 | BOS | +6.0 | +5.8 | +3.2 | +2.8 | 96.5 | +1.1 | 1619 |
| 5 | MIN | +5.1 | +5.3 | +2.2 | +2.9 | 103.3 | +0.5 | 1615 |
| 6 | LAL | +4.3 | +4.4 | +4.0 | +0.3 | 101.9 | +0.0 | 1593 |
| 7 | POR | +4.0 | +4.1 | +2.8 | +1.3 | 101.4 | +0.0 | 1563 |
| 8 | NYK | +3.6 | +3.5 | +1.3 | +2.4 | 96.6 | -0.3 | 1690 |
| 9 | PHI | +3.6 | +3.6 | +0.5 | +3.1 | 101.4 | +0.7 | 1588 |
| 10 | OKC | +3.2 | +3.2 | -0.2 | +3.4 | 100.8 | -0.1 | 1672 |
| 11 | GSW | +2.7 | +2.7 | +1.8 | +0.9 | 101.7 | -1.1 | 1517 |
| 12 | DEN | +2.1 | +2.1 | +3.5 | -1.4 | 97.6 | +0.3 | 1577 |
| 13 | CLE | +1.2 | +1.2 | +2.1 | -0.9 | 103.0 | -2.2 | 1573 |
| 14 | TOR | +0.7 | +0.7 | +0.3 | +0.4 | 105.4 | -4.5 | 1544 |
| 15 | PHX | -0.4 | -0.4 | +1.4 | -1.8 | 102.1 | +0.4 | 1492 |
| 16 | MIA | -0.6 | -0.6 | +0.8 | -1.4 | 106.2 | +0.0 | 1485 |
| 17 | MEM | -0.9 | -0.9 | +0.5 | -1.4 | 102.5 | -0.1 | 1412 |
| 18 | DAL | -1.1 | -1.1 | -0.7 | -0.3 | 101.7 | +0.8 | 1431 |
| 19 | ORL | -1.5 | -1.5 | -2.4 | +0.9 | 99.8 | +0.3 | 1495 |
| 20 | ATL | -1.7 | -1.8 | -1.0 | -0.7 | 106.6 | +2.3 | 1546 |
| 21 | IND | -2.6 | -2.7 | -1.1 | -1.5 | 102.7 | -0.4 | 1362 |
| 22 | NOP | -2.6 | -2.8 | -1.1 | -1.5 | 105.6 | +0.5 | 1443 |
| 23 | LAC | -3.4 | -3.4 | -1.8 | -1.7 | 100.1 | +0.5 | 1476 |
| 24 | UTA | -4.0 | -4.1 | -3.5 | -0.5 | 102.7 | -0.7 | 1304 |
| 25 | CHA | -4.5 | -4.4 | -4.0 | -0.6 | 96.2 | -1.7 | 1488 |
| 26 | WAS | -4.9 | -4.9 | -3.0 | -1.9 | 100.3 | -2.3 | 1337 |
| 27 | BKN | -6.0 | -6.0 | -3.4 | -2.5 | 100.9 | +0.4 | 1319 |
| 28 | MIL | -7.1 | -7.3 | -2.7 | -4.3 | 104.0 | +0.2 | 1343 |
| 29 | SAC | -7.4 | -7.8 | -3.4 | -4.0 | 104.5 | -0.1 | 1344 |
| 30 | CHI | -7.5 | -8.4 | -3.8 | -3.7 | 111.8 | -0.5 | 1356 |

## Top players

Regularized adjusted plus-minus from every lineup this season and past ones: points per 100 possessions a player adds on offense and saves on defense, against an average player, shrunk toward last season's rating. Players expected to play 20 minutes or more.

| # | Player | Team | Net impact per 100 | Offense | Defense | Expected minutes |
|---|---|---|---|---|---|---|
| 1 | Victor Wembanyama | SAS | +6.7 | +1.8 | +4.9 | 32 |
| 2 | Shai Gilgeous-Alexander | OKC | +5.7 | +5.1 | +0.6 | 35 |
| 3 | Nikola Jokic | DEN | +5.4 | +5.5 | -0.1 | 34 |
| 4 | Kawhi Leonard | TOR | +4.5 | +3.6 | +0.9 | 30 |
| 5 | Luka Doncic | LAL | +4.4 | +5.4 | -1.0 | 36 |
| 6 | Kyrie Irving | DAL | +3.5 | +3.4 | +0.1 | 33 |
| 7 | Giannis Antetokounmpo | MIA | +3.5 | +3.5 | +0.0 | 34 |
| 8 | Joel Embiid | PHI | +3.4 | +1.6 | +1.8 | 32 |
| 9 | Herbert Jones | NOP | +3.3 | +0.0 | +3.3 | 29 |
| 10 | Stephen Curry | GSW | +2.4 | +4.5 | -2.1 | 30 |
| 11 | Marcus Smart | HOU | +2.3 | +1.2 | +1.1 | 21 |
| 12 | Fred VanVleet | HOU | +2.3 | +1.8 | +0.5 | 30 |
| 13 | Jimmy Butler III | GSW | +2.2 | +2.1 | +0.1 | 27 |
| 14 | LaMelo Ball | MIN | +2.2 | +4.0 | -1.8 | 29 |
| 15 | Chet Holmgren | OKC | +2.1 | +0.0 | +2.1 | 30 |
| 16 | Ausar Thompson | DET | +2.1 | +0.0 | +2.1 | 29 |
| 17 | Dean Wade | PHI | +2.0 | +0.5 | +1.6 | 24 |
| 18 | Franz Wagner | ORL | +1.9 | +0.8 | +1.1 | 38 |
| 19 | Donovan Mitchell | CLE | +1.9 | +2.7 | -0.8 | 33 |
| 20 | Rudy Gobert | MIN | +1.9 | -3.2 | +5.1 | 31 |
| 21 | Cade Cunningham | DET | +1.8 | +1.6 | +0.2 | 34 |
| 22 | Ty Jerome | MEM | +1.8 | +3.1 | -1.3 | 30 |
| 23 | Lauri Markkanen | UTA | +1.7 | +1.5 | +0.2 | 32 |
| 24 | Dyson Daniels | ATL | +1.7 | +0.5 | +1.2 | 31 |
| 25 | Bam Adebayo | MIA | +1.7 | +1.3 | +0.3 | 34 |
| 26 | Neemias Queta | BOS | +1.7 | +0.7 | +1.0 | 26 |
| 27 | Derrick White | BOS | +1.6 | +0.2 | +1.4 | 33 |
| 28 | Jrue Holiday | POR | +1.6 | +0.6 | +1.0 | 28 |
| 29 | Paul Reed | DET | +1.6 | +0.2 | +1.4 | 29 |
| 30 | Pascal Siakam | IND | +1.6 | +1.4 | +0.2 | 32 |

## Current model fit

- Fitted on 5405 games from 2022-23 to 2026-27.
- Home court: +2.0 points per 100 possessions for the home team over the visitor (about 2.0 points a game).
- Second night of a back-to-back: -0.7 points per 100 scored, +1.2 allowed.
- Weights: team efficiency ratings 0.16 (offense) and 0.15 (defense); player lineup ratings 0.76 and 0.76.
- Blend: 82% on the betting line for the margin and 100% for the total, wherever there is a line (fitted on past closing lines).
- Simulator: each team's points vary by 10.9 with correlation 0.23; 5.2% of recent games went to overtime.
