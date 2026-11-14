# NBA score predictions

Updated Sat Nov 14, 2026 02:19 AM ET. Refreshed automatically several times a day during the season, around the injury report's deadlines; each game's prediction is locked at tip-off and graded once the final score is in.

Each team's expected points are its expected possessions times its expected points per possession, from team efficiency ratings and the ratings of the players expected to play, blended with the betting line. Each game is then simulated 10,000 times, overtime included. The predicted score is the expected points rounded; the 80% range holds 80% of simulated outcomes for each team. Basketball is the most predictable major sport, but a team's score still varies by about ±14 points around the forecast, so read the win chance and the ranges too.

Missing players come from the injury report: out players are left out, and doubtful, questionable and probable ones count with the share of their minutes their chance of playing implies, and their minutes go mostly to the bench. The effect is how many points of margin the team gains or loses against its full-strength roster: negative when it is missing good players, positive when the minutes go to better ones. Predictions are rerun when the report changes, up to tip-off.

The fair moneyline is the American odds that match the win chance exactly, with no bookmaker margin: -150 means risk $150 to win $100, +150 means risk $100 to win $150.

The edge columns check every side of the spread, the moneyline and the total for expected value: the profit per $1 bet at the posted price, using the final prediction's chances (the model blended with the line, simulated against the posted lines, pushes returning the stake, and anchored to the market's own chances so only what the blend moves off the line counts). The model's own spread and total are shown alongside, but the blend keeps only the share of that disagreement the model has earned in past seasons, so edges are rare. A side is an edge when its EV is 3% or more; the best such side is shown with its price, its EV, its chance of winning the bet and its stake, a 25% share of the Kelly stake in units of 1% of the bankroll, with at most 3 units on one game. Where a spread or total price is not posted it is assumed to be -110 (marked \*); a moneyline is never assumed. Edges are logged with each prediction, locked at tip-off and graded below. Treat them as an experiment, not betting advice; see the backtest for how they have done on past seasons.

## Saturday, November 14

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Spread: model / line | Total: model / line | 80% range | Overtime | Missing (effect on margin) | Spread edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 7:00 PM | DEN @ NOP | DEN 123, NOP 112 | DEN 79% | DEN -385 / NOP +385<br>posted DEN -556 / NOP +417 | DEN -11.2 / DEN -11.5 (fav covers 48%) | 235.5 / 235.5 (over 50%) | 109–138 / 97–127 | 4% | NOP: Trey Murphy III (out); Dejounte Murray (out); Yves Missi (out); Trendon Watford (out); Bryce McGowens (out) (-0.4) | no edge | no edge | no edge |
| 7:30 PM | DAL @ CLE | DAL 115, CLE 117 | CLE 58% | DAL +135 / CLE -135<br>posted DAL +114 / CLE -135 | CLE -2.7 / CLE -3.5 (fav covers 49%) | 231.7 / 231.5 (over 50%) | 100–129 / 103–132 | 5% | DAL: Dereck Lively II (out); Morez Johnson Jr. (day-to-day); Sergio de Larrea (out) (+1.1)<br>CLE: Evan Mobley (out); Sam Merrill (out) (-1.1) | no edge | no edge | no edge |
| 8:00 PM | DET @ MIA | DET 117, MIA 112 | DET 64% | DET -175 / MIA +175<br>posted DET -191 / MIA +160 | DET -4.8 / DET -4.5 (fav covers 52%) | 228.7 / 228.5 (over 49%) | 102–131 / 98–127 | 5% | DET: Jalen Duren (out) (+0.2)<br>MIA: Klay Thompson (out); Pelle Larsson (out) (+0.7) | no edge | no edge | no edge |
| 8:00 PM | BKN @ MEM | BKN 111, MEM 116 | MEM 64% | BKN +180 / MEM -180<br>posted BKN +186 / MEM -224 | MEM -5 / MEM -5.5 (fav covers 49%) | 226.7 / 226.5 (over 49%) | 96–126 / 101–130 | 5% | BKN: Mikel Brown Jr. (day-to-day); Nolan Traore (day-to-day) (+0.5)<br>MEM: Zach Edey (out); Scotty Pippen Jr. (out) (+0.1) | no edge | no edge | no edge |
| 8:00 PM | CHI @ MIN | CHI 111, MIN 125 | MIN 85% | CHI +590 / MIN -590<br>posted CHI +580 / MIN -840 | MIN -14.7 / MIN -14.5 (fav covers 49%) | 235.9 / 236.5 (over 48%) | 96–126 / 111–140 | 3% | CHI: Jalen Smith (day-to-day); Caleb Wilson (out) (+1.1)<br>MIN: Anthony Edwards (out); Donte DiVincenzo (out) (-0.8) | no edge | no edge | no edge |

## Sunday, November 15

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Spread: model / line | Total: model / line | 80% range | Overtime | Missing (effect on margin) | Spread edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1:00 PM | IND @ PHI | IND 110, PHI 116 | PHI 67% | IND +205 / PHI -205 | PHI -6.1 | 225.7 | 96–125 / 102–130 | 5% | IND: Tyrese Haliburton (out); Aaron Nesmith (day-to-day); Johnny Furphy (out); Ben Sheppard (out) (-0.1)<br>PHI: LeBron James (day-to-day); Adem Bona (out); Dominick Barlow (out) (+0.5) | no line yet | no line yet | no line yet |
| 4:00 PM | LAL @ PHX | LAL 117, PHX 115 | LAL 55% | LAL -120 / PHX +120 | LAL -1.6 | 231.9 | 102–131 / 101–130 | 5% | LAL: Luka Doncic (day-to-day); Austin Reaves (day-to-day); Quentin Grimes (day-to-day); Collin Sexton (day-to-day) (-0.8)<br>PHX: Mark Williams (out) (+0.6) | no line yet | no line yet | no line yet |
| 4:30 PM | CHA @ LAC | CHA 107, LAC 111 | LAC 63% | CHA +170 / LAC -170 | LAC -4.3 | 217.4 | 92–121 / 97–125 | 5% | CHA: Dennis Schroder (out); Brandon Miller (day-to-day); Kon Knueppel (out) (-0.3)<br>LAC: Brandon Ingram (out); Jordan Miller (out); Bradley Beal (out); Yanic Konan Niederhauser (out) (+0.4) | no line yet | no line yet | no line yet |
| 5:00 PM | SAS @ UTA | SAS 118, UTA 105 | SAS 84% | SAS -515 / UTA +515 | SAS -13 | 223.0 | 104–132 / 90–120 | 3% | SAS: Tobias Harris (out) (+0.7)<br>UTA: Lauri Markkanen (out); Jaxson Hayes (day-to-day); Jaren Jackson Jr. (out); Trey Alexander (out); Jusuf Nurkic (out) (-2.8) | no line yet | no line yet | no line yet |
| 6:00 PM | DAL @ BOS | DAL 105, BOS 116 | BOS 80% | DAL +405 / BOS -405 | BOS -11.4 | 221.5 | 91–120 / 103–130 | 4% | DAL: Dereck Lively II (out); Morez Johnson Jr. (day-to-day); Sergio de Larrea (out) (+1.1)<br>BOS: Paul George (day-to-day) (-0.2) | no line yet | no line yet | no line yet |
| 6:00 PM | NYK @ TOR | NYK 110, TOR 106 | NYK 62% | NYK -165 / TOR +165 | NYK -4.3 | 216.2 | 96–124 / 92–120 | 5% | TOR: Scottie Barnes (out); Kawhi Leonard (out) (-2.8) | no line yet | no line yet | no line yet |
| 7:00 PM | HOU @ WAS | HOU 115, WAS 107 | HOU 73% | HOU -275 / WAS +275 | HOU -8.3 | 221.4 | 101–129 / 92–121 | 4% | HOU: Marcus Smart (suspension); Steven Adams (out); Clint Capela (out) (-1.3)<br>WAS: Jamir Watkins (out); Justin Champagnie (out); Bub Carrington (day-to-day); Tristan Vukcevic (out) (+0.4) | no line yet | no line yet | no line yet |
| 8:00 PM | ATL @ MIL | ATL 122, MIL 115 | ATL 68% | ATL -210 / MIL +210 | ATL -6.4 | 236.9 | 107–136 / 100–130 | 5% | ATL: Kingston Flemings (day-to-day); Keshon Gilbert (out) (+2.4) | no line yet | no line yet | no line yet |
| 9:00 PM | OKC @ SAC | OKC 117, SAC 108 | OKC 75% | OKC -300 / SAC +300 | OKC -8.8 | 225.0 | 103–131 / 94–123 | 4% | OKC: Chet Holmgren (out); Jalen Williams (out); Ajay Mitchell (out); Jaylin Williams (out); Cason Wallace (out) (-0.6)<br>SAC: Maxime Raynaud (out); Precious Achiuwa (out) (+0.4) | no line yet | no line yet | no line yet |

## How the 2026-27 predictions have done

| Predictor | Games | Margin MAE | Total MAE | Team-points MAE | Log loss | Brier | Winners | 80% range hit |
|---|---|---|---|---|---|---|---|---|
| Final prediction | 174 | 11.09 | 14.19 | 9.34 | 0.547 | 0.184 | 73.0% | 81.3% |
| Model only (before blending) | 174 | 11.44 | 14.04 | 9.42 | 0.569 | 0.193 | 71.3% | – |
| Elo | 174 | 11.84 | – | – | 0.593 | 0.205 | 66.1% | – |
| Final prediction, games with a line | 174 | 11.09 | 14.19 | 9.34 | 0.547 | 0.184 | 73.0% | 81.3% |
| Model only, games with a line | 174 | 11.44 | 14.04 | 9.42 | 0.569 | 0.193 | 71.3% | – |
| Betting line | 174 | 11.05 | 14.19 | 9.33 | 0.539 | 0.181 | 73.0% | – |

MAE is the average miss in points; team-points MAE is the average miss on each team's score. Log loss and Brier score the win chances (lower is better; a coin flip scores 0.693 and 0.250). The closing line misses margins by about 10 points and totals by about 14.

Overtime: predicted in 4.7% of games, happened in 5.2%.

### Betting edges

| Market | Edges | Record (W-L-P) | Staked | Units won | ROI | Expected ROI |
|---|---|---|---|---|---|---|
| Spread | 1 | 1-0-0 | 1.0 | +0.90 | +89.3% | +3.6% |
| Moneyline | 9 | 0-9-0 | 3.5 | -3.47 | -100.0% | +8.3% |
| Total | 0 | 0-0-0 | 0.0 | +0.00 | – | – |

Spread moved toward the model's first spread edge before tip-off: 5 of 6 games (83%).

Live predictions only, each edge at the stake and price logged with the last prediction before tip-off (edges logged before edges were priced from the final prediction are left out); a push returns the stake. Units are 1% of the bankroll; ROI is units won per unit staked, and expected ROI is what the edges' EVs promised. The line moving toward the model's edge before tip-off is the quickest sign that it knows something the market doesn't yet.

### Results, Thursday, November 12

| Game | Predicted | Final | Win chance for winner | Spread: model / line | Inside 80% ranges |
|---|---|---|---|---|---|
| TOR @ PHI | 108–116 | 112–123 | 72% | PHI -7.5 / PHI -7.5 | yes |
| DET @ WAS | 117–106 | 144–140 (2OT) | 79% | DET -10.7 / DET -10.5 | no |
| DAL @ MIN | 110–115 | 94–133 | 66% | MIN -5.3 / MIN -5.5 | no |
| CHA @ PHX | 104–111 | 96–101 | 69% | PHX -6.7 / PHX -6.5 | yes |

## Power ratings

Points per 100 possessions better than an average team on a neutral floor, combining opponent-adjusted team efficiency (garbage time removed) with the ratings of the team's healthy roster, through the fitted points map. Net per game uses the team's pace. Injury effect now is what its current injury report does to its margin, in points.

| # | Team | Net per 100 | Net per game | Offense | Defense | Pace | Injury effect now | Elo |
|---|---|---|---|---|---|---|---|---|
| 1 | BOS | +7.9 | +7.5 | +3.9 | +4.0 | 95.1 | -0.2 | 1669 |
| 2 | SAS | +7.4 | +7.4 | +3.3 | +4.1 | 99.6 | +0.7 | 1724 |
| 3 | HOU | +7.2 | +7.1 | +3.1 | +4.1 | 98.0 | -1.3 | 1624 |
| 4 | DET | +6.3 | +6.3 | +2.8 | +3.4 | 100.7 | +0.2 | 1647 |
| 5 | MIN | +5.4 | +5.6 | +2.4 | +3.1 | 103.5 | -0.8 | 1631 |
| 6 | LAL | +4.9 | +5.0 | +4.2 | +0.6 | 102.1 | -0.8 | 1624 |
| 7 | DEN | +4.0 | +3.9 | +4.4 | -0.4 | 97.7 | +0.2 | 1580 |
| 8 | NYK | +3.8 | +3.6 | +1.4 | +2.4 | 93.6 | +0.0 | 1686 |
| 9 | OKC | +3.7 | +3.8 | -0.4 | +4.1 | 101.6 | -0.6 | 1652 |
| 10 | POR | +3.5 | +3.6 | +2.8 | +0.7 | 102.1 | +0.7 | 1577 |
| 11 | GSW | +2.8 | +2.9 | +1.5 | +1.3 | 100.6 | -2.1 | 1534 |
| 12 | PHI | +1.9 | +1.9 | +0.1 | +1.7 | 100.8 | +0.5 | 1566 |
| 13 | CLE | +0.6 | +0.6 | +1.5 | -0.9 | 101.0 | -1.1 | 1581 |
| 14 | TOR | +0.2 | +0.2 | -0.2 | +0.3 | 101.5 | -2.9 | 1513 |
| 15 | PHX | +0.0 | +0.0 | +0.5 | -0.5 | 101.2 | +0.6 | 1506 |
| 16 | MIA | -0.6 | -0.7 | +0.3 | -1.0 | 104.8 | +0.7 | 1495 |
| 17 | DAL | -1.1 | -1.1 | -0.6 | -0.4 | 102.5 | +1.1 | 1441 |
| 18 | IND | -1.5 | -1.6 | -0.3 | -1.2 | 102.2 | -0.1 | 1364 |
| 19 | MEM | -1.6 | -1.6 | +0.3 | -1.9 | 101.9 | +0.1 | 1423 |
| 20 | ORL | -1.6 | -1.6 | -2.6 | +1.0 | 100.5 | +1.0 | 1503 |
| 21 | ATL | -2.2 | -2.4 | -1.1 | -1.1 | 108.3 | +2.5 | 1539 |
| 22 | LAC | -3.7 | -3.7 | -1.6 | -2.0 | 101.4 | +0.4 | 1471 |
| 23 | UTA | -3.9 | -4.0 | -3.6 | -0.2 | 102.0 | -2.8 | 1285 |
| 24 | WAS | -4.9 | -5.0 | -2.7 | -2.3 | 100.3 | +0.4 | 1319 |
| 25 | BKN | -5.3 | -5.4 | -2.9 | -2.4 | 101.8 | +0.5 | 1347 |
| 26 | CHA | -5.4 | -5.2 | -4.7 | -0.6 | 96.7 | -0.3 | 1476 |
| 27 | NOP | -5.4 | -5.5 | -1.7 | -3.6 | 102.8 | -0.4 | 1372 |
| 28 | CHI | -6.4 | -7.0 | -2.7 | -3.7 | 109.2 | +1.1 | 1350 |
| 29 | SAC | -7.9 | -8.1 | -4.0 | -3.9 | 102.2 | +0.4 | 1328 |
| 30 | MIL | -8.0 | -8.1 | -3.4 | -4.7 | 101.2 | +0.0 | 1323 |

## Top players

Regularized adjusted plus-minus from every lineup this season and past ones: points per 100 possessions a player adds on offense and saves on defense, against an average player, shrunk toward last season's rating. Players expected to play 20 minutes or more.

| # | Player | Team | Net impact per 100 | Offense | Defense | Expected minutes |
|---|---|---|---|---|---|---|
| 1 | Victor Wembanyama | SAS | +8.2 | +2.6 | +5.5 | 29 |
| 2 | Shai Gilgeous-Alexander | OKC | +5.7 | +5.0 | +0.7 | 33 |
| 3 | Alex Caruso | OKC | +5.2 | +0.3 | +4.8 | 22 |
| 4 | Nikola Jokic | DEN | +5.1 | +4.9 | +0.2 | 37 |
| 5 | Luka Doncic | LAL | +4.6 | +5.3 | -0.7 | 35 |
| 6 | Kawhi Leonard | TOR | +4.6 | +3.6 | +0.9 | 30 |
| 7 | Giannis Antetokounmpo | MIA | +3.9 | +3.7 | +0.2 | 33 |
| 8 | Kyrie Irving | DAL | +3.5 | +3.5 | -0.1 | 31 |
| 9 | Donovan Mitchell | CLE | +3.1 | +3.3 | -0.2 | 32 |
| 10 | Joel Embiid | PHI | +3.0 | +1.6 | +1.5 | 29 |
| 11 | Fred VanVleet | HOU | +2.6 | +1.5 | +1.1 | 30 |
| 12 | LaMelo Ball | MIN | +2.5 | +4.3 | -1.7 | 29 |
| 13 | Neemias Queta | BOS | +2.4 | +1.0 | +1.4 | 25 |
| 14 | Jarrett Allen | CLE | +2.3 | +2.0 | +0.2 | 24 |
| 15 | Jimmy Butler III | GSW | +2.2 | +2.1 | +0.1 | 27 |
| 16 | Ty Jerome | MEM | +2.1 | +3.2 | -1.1 | 31 |
| 17 | Chet Holmgren | OKC | +2.1 | +0.0 | +2.1 | 30 |
| 18 | Dyson Daniels | ATL | +2.1 | +0.5 | +1.5 | 32 |
| 19 | Franz Wagner | ORL | +2.0 | +1.0 | +1.1 | 39 |
| 20 | Derrick White | BOS | +2.0 | +0.3 | +1.7 | 31 |
| 21 | Rudy Gobert | MIN | +1.9 | -3.1 | +5.0 | 27 |
| 22 | Pascal Siakam | IND | +1.9 | +1.6 | +0.3 | 33 |
| 23 | Herbert Jones | NOP | +1.8 | -1.0 | +2.8 | 24 |
| 24 | Ausar Thompson | DET | +1.8 | +0.0 | +1.8 | 33 |
| 25 | Jrue Holiday | POR | +1.8 | +1.1 | +0.7 | 27 |
| 26 | Damian Lillard | POR | +1.7 | +2.3 | -0.6 | 29 |
| 27 | Paul Reed | DET | +1.7 | +0.4 | +1.3 | 29 |
| 28 | De'Aaron Fox | SAS | +1.7 | +1.7 | -0.1 | 29 |
| 29 | Day'Ron Sharpe | BKN | +1.6 | +0.5 | +1.1 | 22 |
| 30 | Jaden McDaniels | MIN | +1.5 | +0.4 | +1.1 | 31 |

## Current model fit

- Fitted on 5456 games from 2022-23 to 2026-27.
- Home court: +2.0 points per 100 possessions for the home team over the visitor (about 2.0 points a game).
- Second night of a back-to-back: -0.8 points per 100 scored, +1.2 allowed.
- Weights: team efficiency ratings 0.15 (offense) and 0.15 (defense); player lineup ratings 0.76 and 0.76.
- Blend: 82% on the betting line for the margin and 100% for the total, wherever there is a line (fitted on past closing lines).
- Simulator: each team's points vary by 10.9 with correlation 0.23; 5.2% of recent games went to overtime.
