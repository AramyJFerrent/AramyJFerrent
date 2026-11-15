# NBA score predictions

Updated Sun Nov 15, 2026 02:30 AM ET. Refreshed automatically several times a day during the season, around the injury report's deadlines; each game's prediction is locked at tip-off and graded once the final score is in.

Each team's expected points are its expected possessions times its expected points per possession, from team efficiency ratings and the ratings of the players expected to play, blended with the betting line. Each game is then simulated 10,000 times, overtime included. The predicted score is the expected points rounded; the 80% range holds 80% of simulated outcomes for each team. Basketball is the most predictable major sport, but a team's score still varies by about ±14 points around the forecast, so read the win chance and the ranges too.

Missing players come from the injury report: out players are left out, and doubtful, questionable and probable ones count with the share of their minutes their chance of playing implies, and their minutes go mostly to the bench. The effect is how many points of margin the team gains or loses against its full-strength roster: negative when it is missing good players, positive when the minutes go to better ones. Predictions are rerun when the report changes, up to tip-off.

The fair moneyline is the American odds that match the win chance exactly, with no bookmaker margin: -150 means risk $150 to win $100, +150 means risk $100 to win $150.

The edge columns check every side of the spread, the moneyline and the total for expected value: the profit per $1 bet at the posted price, using the final prediction's chances (the model blended with the line, simulated against the posted lines, pushes returning the stake, and anchored to the market's own chances so only what the blend moves off the line counts). The model's own spread and total are shown alongside, but the blend keeps only the share of that disagreement the model has earned in past seasons, so edges are rare. A side is an edge when its EV is 3% or more; the best such side is shown with its price, its EV, its chance of winning the bet and its stake, a 25% share of the Kelly stake in units of 1% of the bankroll, with at most 3 units on one game. Where a spread or total price is not posted it is assumed to be -110 (marked \*); a moneyline is never assumed. Edges are logged with each prediction, locked at tip-off and graded below. Treat them as an experiment, not betting advice; see the backtest for how they have done on past seasons.

## Sunday, November 15

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Spread: model / line | Total: model / line | 80% range | Overtime | Missing (effect on margin) | Spread edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1:00 PM | IND @ PHI | IND 109, PHI 116 | PHI 69% | IND +220 / PHI -220<br>posted IND +235 / PHI -288 | PHI -6.6 / PHI -7.5 (fav covers 48%) | 224.7 / 224.5 (over 49%) | 94–124 / 102–130 | 5% | IND: Andrew Nembhard (day-to-day); Tyrese Haliburton (out); Aaron Nesmith (day-to-day); Johnny Furphy (out); Ben Sheppard (out); T.J. McConnell (day-to-day) (+0.0)<br>PHI: Joel Embiid (out); Adem Bona (out); Dominick Barlow (out) (-2.0) | no edge | IND ML (+235): EV +4.2%, 31%, stake 0.4u | no edge |
| 4:00 PM | LAL @ PHX | LAL 114, PHX 112 | LAL 57% | LAL -135 / PHX +135<br>posted LAL -148 / PHX +124 | LAL -2.2 / LAL -2.5 (fav covers 52%) | 226.7 / 226.5 (over 49%) | 100–129 / 98–127 | 5% | LAL: Austin Reaves (out); Collin Sexton (day-to-day) (-0.9)<br>PHX: Mark Williams (out) (+0.6) | no edge | no edge | no edge |
| 4:30 PM | CHA @ LAC | CHA 107, LAC 109 | LAC 57% | CHA +130 / LAC -130<br>posted CHA +100 / LAC -118 | LAC -2.1 / LAC -1.5 (fav covers 54%) | 215.7 / 215.5 (over 50%) | 93–121 / 95–123 | 5% | CHA: Dennis Schroder (out); Kon Knueppel (out) (-0.3)<br>LAC: Brandon Ingram (out); Jordan Miller (out); Bradley Beal (out); Yanic Konan Niederhauser (out) (+0.6) | no edge | no edge | no edge |
| 5:00 PM | SAS @ UTA | SAS 120, UTA 104 | SAS 89% | SAS -830 / UTA +830<br>posted SAS -1460 / UTA +850 | SAS -16.9 / SAS -17.5 (fav covers 47%) | 223.9 / 224.5 (over 48%) | 106–134 / 89–118 | 2% | SAS: Tobias Harris (out) (+0.7)<br>UTA: Lauri Markkanen (out); Jaren Jackson Jr. (out); Jaxson Hayes (out); Trey Alexander (out); Jusuf Nurkic (out) (-2.6) | no edge | UTA ML (+850): EV +7.3%, 11%, stake 0.2u | no edge |
| 6:00 PM | DAL @ BOS | DAL 102, BOS 115 | BOS 84% | DAL +535 / BOS -535<br>posted DAL +558 / BOS -800 | BOS -13.3 / BOS -13.5 (fav covers 48%) | 217.2 / 217.5 (over 49%) | 88–116 / 102–129 | 4% | DAL: Daniel Gafford (out); Dereck Lively II (out); Sergio de Larrea (out) (+0.4) | no edge | no edge | no edge |
| 6:00 PM | NYK @ TOR | NYK 111, TOR 107 | NYK 63% | NYK -170 / TOR +170<br>posted NYK -192 / TOR +160 | NYK -4.5 / NYK -4.5 (fav covers 52%) | 217.5 / 217.5 (over 50%) | 97–125 / 92–121 | 5% | TOR: Scottie Barnes (out); Kawhi Leonard (out) (-2.9) | no edge | no edge | no edge |
| 7:00 PM | HOU @ WAS | HOU 116, WAS 107 | HOU 75% | HOU -305 / WAS +305<br>posted HOU -420 / WAS +329 | HOU -8.9 / HOU -9.5 (fav covers 47%) | 222.6 / 222.5 (over 49%) | 102–130 / 92–121 | 4% | HOU: Fred VanVleet (out); Marcus Smart (suspension); Steven Adams (out); Clint Capela (out) (-3.2)<br>WAS: Alex Sarr (day-to-day); Jamir Watkins (out); Tre Johnson (day-to-day); Justin Champagnie (out); Bub Carrington (day-to-day); Tristan Vukcevic (out) (+0.6) | no edge | no edge | no edge |
| 8:00 PM | ATL @ MIL | ATL 121, MIL 114 | ATL 70% | ATL -235 / MIL +235<br>posted ATL -310 / MIL +251 | ATL -7.3 / ATL -7.5 (fav covers 50%) | 234.3 / 234.5 (over 49%) | 106–135 / 99–128 | 5% | ATL: Kingston Flemings (out); Keshon Gilbert (out) (+3.5) | no edge | no edge | no edge |
| 9:00 PM | OKC @ SAC | OKC 116, SAC 106 | OKC 78% | OKC -355 / SAC +355<br>posted OKC -467 / SAC +360 | OKC -10.2 / OKC -10.5 (fav covers 47%) | 222.3 / 222.5 (over 49%) | 102–130 / 92–121 | 4% | OKC: Chet Holmgren (out); Jalen Williams (out); Ajay Mitchell (day-to-day); Jaylin Williams (out); Cason Wallace (out) (-0.2)<br>SAC: Maxime Raynaud (out); Keegan Murray (day-to-day); Precious Achiuwa (day-to-day) (+0.4) | no edge | no edge | no edge |

## Monday, November 16

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Spread: model / line | Total: model / line | 80% range | Overtime | Missing (effect on margin) | Spread edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 7:00 PM | ORL @ BOS | ORL 104, BOS 111 | BOS 72% | ORL +255 / BOS -255 | BOS -7.4 | 214.9 | 90–118 / 97–125 | 5% | ORL: Paolo Banchero (out) (+1.2) | no line yet | no line yet | no line yet |
| 7:00 PM | CHI @ CLE | CHI 117, CLE 120 | CLE 58% | CHI +140 / CLE -140 | CLE -2.8 | 236.5 | 102–132 / 105–134 | 5% | CHI: Jalen Smith (out); Caleb Wilson (out); Nic Claxton (out) (-0.6)<br>CLE: Donovan Mitchell (out); James Harden (out); Evan Mobley (out); Peyton Watson (out); Jarrett Allen (out); Sam Merrill (out) (-5.8) | no line yet | no line yet | no line yet |
| 7:00 PM | MEM @ WAS | MEM 116, WAS 115 | MEM 53% | MEM -115 / WAS +115 | MEM -1 | 230.8 | 101–131 / 100–130 | 5% | MEM: Ty Jerome (out); Jerami Grant (out); Zach Edey (out); GG Jackson (out); Scotty Pippen Jr. (out) (-2.3)<br>WAS: Alex Sarr (day-to-day); Jamir Watkins (out); Tre Johnson (day-to-day); Justin Champagnie (out); Bub Carrington (day-to-day); Tristan Vukcevic (out) (+0.6) | no line yet | no line yet | no line yet |
| 7:30 PM | PHI @ BKN | PHI 113, BKN 111 | PHI 57% | PHI -130 / BKN +130 | PHI -2.2 | 224.1 | 99–128 / 96–126 | 6% | PHI: Joel Embiid (out); Adem Bona (out); Dominick Barlow (out) (-2.0)<br>BKN: Michael Porter Jr. (out) (-1.1) | no line yet | no line yet | no line yet |
| 7:30 PM | HOU @ MIA | HOU 115, MIA 116 | MIA 52% | HOU +110 / MIA -110 | MIA -0.7 | 230.4 | 100–130 / 101–130 | 5% | HOU: Fred VanVleet (out); Marcus Smart (suspension); Steven Adams (out); Clint Capela (out) (-3.3)<br>MIA: Pelle Larsson (out) (+0.6) | no line yet | no line yet | no line yet |
| 8:00 PM | POR @ MIN | POR 113, MIN 116 | MIN 58% | POR +135 / MIN -135 | MIN -2.8 | 229.8 | 99–128 / 102–131 | 5% | POR: Ja Morant (out); Chris Youngblood (day-to-day) (+0.2)<br>MIN: Anthony Edwards (out); Jaylen Clark (out); Donte DiVincenzo (out) (-0.7) | no line yet | no line yet | no line yet |
| 8:00 PM | GSW @ NOP | GSW 116, NOP 114 | GSW 57% | GSW -130 / NOP +130 | GSW -2.4 | 230.1 | 102–131 / 99–129 | 6% | GSW: Moses Moody (out); Jimmy Butler III (out); Kristaps Porzingis (out); Stephen Curry (out); Brandon Williams (out) (-2.8)<br>NOP: Trey Murphy III (out); Dejounte Murray (out); Trendon Watford (out); Bennedict Mathurin (out); Bryce McGowens (out) (-0.2) | no line yet | no line yet | no line yet |
| 9:00 PM | PHX @ DEN | PHX 111, DEN 118 | DEN 71% | PHX +245 / DEN -245 | DEN -7.5 | 229.2 | 96–126 / 104–133 | 5% | PHX: Mark Williams (out) (+0.5) | no line yet | no line yet | no line yet |

## How the 2026-27 predictions have done

| Predictor | Games | Margin MAE | Total MAE | Team-points MAE | Log loss | Brier | Winners | 80% range hit |
|---|---|---|---|---|---|---|---|---|
| Final prediction | 183 | 11.13 | 14.05 | 9.28 | 0.550 | 0.185 | 72.7% | 81.4% |
| Model only (before blending) | 183 | 11.44 | 13.92 | 9.35 | 0.568 | 0.193 | 71.0% | – |
| Elo | 183 | 11.90 | – | – | 0.597 | 0.207 | 65.0% | – |
| Final prediction, games with a line | 183 | 11.13 | 14.05 | 9.28 | 0.550 | 0.185 | 72.7% | 81.4% |
| Model only, games with a line | 183 | 11.44 | 13.92 | 9.35 | 0.568 | 0.193 | 71.0% | – |
| Betting line | 183 | 11.10 | 14.05 | 9.27 | 0.543 | 0.183 | 72.7% | – |

MAE is the average miss in points; team-points MAE is the average miss on each team's score. Log loss and Brier score the win chances (lower is better; a coin flip scores 0.693 and 0.250). The closing line misses margins by about 10 points and totals by about 14.

Overtime: predicted in 4.7% of games, happened in 5.5%.

### Betting edges

| Market | Edges | Record (W-L-P) | Staked | Units won | ROI | Expected ROI |
|---|---|---|---|---|---|---|
| Spread | 1 | 1-0-0 | 1.0 | +0.90 | +89.3% | +3.6% |
| Moneyline | 11 | 1-10-0 | 4.0 | -2.68 | -67.2% | +7.7% |
| Total | 0 | 0-0-0 | 0.0 | +0.00 | – | – |

Spread moved toward the model's first spread edge before tip-off: 5 of 6 games (83%).

Live predictions only, each edge at the stake and price logged with the last prediction before tip-off (edges logged before edges were priced from the final prediction are left out); a push returns the stake. Units are 1% of the bankroll; ROI is units won per unit staked, and expected ROI is what the edges' EVs promised. The line moving toward the model's edge before tip-off is the quickest sign that it knows something the market doesn't yet.

### Results, Friday, November 13

| Game | Predicted | Final | Win chance for winner | Spread: model / line | Inside 80% ranges |
|---|---|---|---|---|---|
| NYK @ IND | 114–106 | 104–106 | 28% | NYK -7.5 / NYK -8.5 | yes |
| MIL @ ORL | 108–117 | 99–107 | 76% | ORL -9.4 / ORL -9.5 | yes |
| CLE @ MIA | 117–120 | 121–133 | 57% | MIA -2.4 / MIA -2.5 | yes |
| ATL @ CHI | 126–119 | 117–125 (OT) | 31% | ATL -6.9 / ATL -7.5 | yes |
| MEM @ NOP | 119–116 | 142–111 | 59% | MEM -3.3 / MEM -3.5 | no |
| UTA @ HOU | 102–118 | 118–125 | 88% | HOU -15.5 / HOU -15.5 | no |
| GSW @ SAS | 102–114 | 85–123 | 81% | SAS -11.9 / SAS -12.5 | no |
| POR @ SAC | 120–109 | 120–107 | 78% | POR -10.3 / POR -10.5 | yes |
| OKC @ LAC | 114–108 | 112–113 | 32% | OKC -6 / OKC -6.5 | yes |

## Power ratings

Points per 100 possessions better than an average team on a neutral floor, combining opponent-adjusted team efficiency (garbage time removed) with the ratings of the team's healthy roster, through the fitted points map. Net per game uses the team's pace. Injury effect now is what its current injury report does to its margin, in points.

| # | Team | Net per 100 | Net per game | Offense | Defense | Pace | Injury effect now | Elo |
|---|---|---|---|---|---|---|---|---|
| 1 | BOS | +7.9 | +7.5 | +3.9 | +4.0 | 95.2 | +0.0 | 1669 |
| 2 | SAS | +7.4 | +7.4 | +3.1 | +4.2 | 100.0 | +0.7 | 1732 |
| 3 | HOU | +6.8 | +6.7 | +3.4 | +3.4 | 97.9 | -3.1 | 1625 |
| 4 | DET | +6.2 | +6.2 | +2.7 | +3.4 | 100.6 | +0.1 | 1647 |
| 5 | MIN | +5.3 | +5.5 | +2.2 | +3.1 | 103.6 | -0.7 | 1631 |
| 6 | LAL | +4.7 | +4.9 | +4.1 | +0.6 | 102.3 | -0.9 | 1624 |
| 7 | DEN | +3.8 | +3.7 | +4.3 | -0.5 | 97.4 | +0.2 | 1580 |
| 8 | OKC | +3.7 | +3.8 | -0.4 | +4.1 | 101.6 | -0.2 | 1647 |
| 9 | NYK | +3.6 | +3.5 | +1.0 | +2.7 | 94.9 | +0.0 | 1676 |
| 10 | POR | +3.6 | +3.7 | +2.9 | +0.7 | 101.9 | +0.2 | 1582 |
| 11 | PHI | +1.8 | +1.8 | +0.1 | +1.7 | 100.9 | -2.0 | 1566 |
| 12 | GSW | +1.2 | +1.2 | +0.6 | +0.6 | 100.7 | -2.8 | 1526 |
| 13 | CLE | +0.4 | +0.4 | +1.8 | -1.5 | 100.3 | -5.6 | 1569 |
| 14 | TOR | +0.1 | +0.1 | -0.2 | +0.3 | 101.5 | -3.0 | 1513 |
| 15 | MIA | -0.1 | -0.1 | +1.1 | -1.1 | 104.2 | +0.6 | 1508 |
| 16 | PHX | -0.2 | -0.2 | +0.3 | -0.5 | 101.2 | +0.6 | 1506 |
| 17 | DAL | -1.1 | -1.1 | -0.7 | -0.4 | 102.5 | +0.4 | 1441 |
| 18 | MEM | -1.1 | -1.2 | +0.6 | -1.7 | 103.1 | -2.3 | 1447 |
| 19 | IND | -1.2 | -1.2 | -0.3 | -0.8 | 103.1 | +0.0 | 1373 |
| 20 | ORL | -1.2 | -1.2 | -2.5 | +1.3 | 100.1 | +1.2 | 1506 |
| 21 | ATL | -2.2 | -2.4 | -1.5 | -0.8 | 107.6 | +3.6 | 1525 |
| 22 | LAC | -3.2 | -3.2 | -1.4 | -1.8 | 101.3 | +0.6 | 1477 |
| 23 | UTA | -3.8 | -3.9 | -3.1 | -0.7 | 101.7 | -2.7 | 1284 |
| 24 | WAS | -5.1 | -5.1 | -2.7 | -2.3 | 100.5 | +0.6 | 1319 |
| 25 | CHI | -5.4 | -5.8 | -2.3 | -3.1 | 108.3 | -0.6 | 1363 |
| 26 | CHA | -5.5 | -5.3 | -4.8 | -0.6 | 96.8 | -0.3 | 1476 |
| 27 | BKN | -5.5 | -5.6 | -3.0 | -2.5 | 101.6 | -1.1 | 1347 |
| 28 | NOP | -5.6 | -5.8 | -1.8 | -3.8 | 103.9 | -0.3 | 1348 |
| 29 | SAC | -7.6 | -7.8 | -3.9 | -3.7 | 101.9 | +0.4 | 1323 |
| 30 | MIL | -7.8 | -7.8 | -3.3 | -4.5 | 100.7 | +0.2 | 1320 |

## Top players

Regularized adjusted plus-minus from every lineup this season and past ones: points per 100 possessions a player adds on offense and saves on defense, against an average player, shrunk toward last season's rating. Players expected to play 20 minutes or more.

| # | Player | Team | Net impact per 100 | Offense | Defense | Expected minutes |
|---|---|---|---|---|---|---|
| 1 | Victor Wembanyama | SAS | +8.4 | +2.6 | +5.8 | 26 |
| 2 | Shai Gilgeous-Alexander | OKC | +5.6 | +5.1 | +0.5 | 35 |
| 3 | Alex Caruso | OKC | +5.1 | +0.2 | +4.9 | 24 |
| 4 | Nikola Jokic | DEN | +5.1 | +4.9 | +0.2 | 37 |
| 5 | Luka Doncic | LAL | +4.6 | +5.3 | -0.7 | 35 |
| 6 | Kawhi Leonard | TOR | +4.6 | +3.6 | +0.9 | 30 |
| 7 | Giannis Antetokounmpo | MIA | +3.7 | +3.6 | +0.1 | 32 |
| 8 | Kyrie Irving | DAL | +3.5 | +3.5 | +0.0 | 31 |
| 9 | Joel Embiid | PHI | +3.0 | +1.6 | +1.5 | 29 |
| 10 | Donovan Mitchell | CLE | +2.6 | +3.4 | -0.8 | 33 |
| 11 | Fred VanVleet | HOU | +2.5 | +1.7 | +0.8 | 32 |
| 12 | LaMelo Ball | MIN | +2.5 | +4.2 | -1.7 | 29 |
| 13 | Franz Wagner | ORL | +2.5 | +1.4 | +1.1 | 38 |
| 14 | Neemias Queta | BOS | +2.4 | +1.0 | +1.4 | 25 |
| 15 | Jimmy Butler III | GSW | +2.2 | +2.1 | +0.1 | 27 |
| 16 | Jarrett Allen | CLE | +2.2 | +2.1 | +0.2 | 27 |
| 17 | Chet Holmgren | OKC | +2.1 | +0.0 | +2.1 | 30 |
| 18 | Dyson Daniels | ATL | +2.0 | +0.4 | +1.7 | 33 |
| 19 | Derrick White | BOS | +2.0 | +0.3 | +1.7 | 31 |
| 20 | Rudy Gobert | MIN | +1.9 | -3.1 | +5.1 | 27 |
| 21 | Pascal Siakam | IND | +1.9 | +1.5 | +0.4 | 32 |
| 22 | Bam Adebayo | MIA | +1.9 | +1.4 | +0.4 | 36 |
| 23 | Ty Jerome | MEM | +1.8 | +2.9 | -1.1 | 30 |
| 24 | Ausar Thompson | DET | +1.8 | +0.0 | +1.8 | 33 |
| 25 | Jrue Holiday | POR | +1.8 | +0.9 | +0.9 | 27 |
| 26 | De'Aaron Fox | SAS | +1.8 | +1.8 | +0.0 | 24 |
| 27 | Herbert Jones | NOP | +1.8 | -1.0 | +2.8 | 27 |
| 28 | Paul Reed | DET | +1.7 | +0.4 | +1.3 | 29 |
| 29 | Damian Lillard | POR | +1.6 | +2.3 | -0.6 | 30 |
| 30 | Day'Ron Sharpe | BKN | +1.5 | +0.5 | +1.1 | 22 |

## Current model fit

- Fitted on 5465 games from 2022-23 to 2026-27.
- Home court: +2.0 points per 100 possessions for the home team over the visitor (about 2.0 points a game).
- Second night of a back-to-back: -0.8 points per 100 scored, +1.2 allowed.
- Weights: team efficiency ratings 0.15 (offense) and 0.15 (defense); player lineup ratings 0.77 and 0.76.
- Blend: 82% on the betting line for the margin and 100% for the total, wherever there is a line (fitted on past closing lines).
- Simulator: each team's points vary by 10.9 with correlation 0.23; 5.2% of recent games went to overtime.
