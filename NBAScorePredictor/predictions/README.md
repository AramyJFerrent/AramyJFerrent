# NBA score predictions

Updated Wed Nov 11, 2026 10:48 PM ET. Refreshed automatically several times a day during the season, around the injury report's deadlines; each game's prediction is locked at tip-off and graded once the final score is in.

Each team's expected points are its expected possessions times its expected points per possession, from team efficiency ratings and the ratings of the players expected to play, blended with the betting line. Each game is then simulated 10,000 times, overtime included. The predicted score is the expected points rounded; the 80% range holds 80% of simulated outcomes for each team. Basketball is the most predictable major sport, but a team's score still varies by about ±14 points around the forecast, so read the win chance and the ranges too.

Missing players come from the injury report: out players are left out, and doubtful, questionable and probable ones count with the share of their minutes their chance of playing implies, and their minutes go mostly to the bench. The effect is how many points of margin the team gains or loses against its full-strength roster: negative when it is missing good players, positive when the minutes go to better ones. Predictions are rerun when the report changes, up to tip-off.

The fair moneyline is the American odds that match the win chance exactly, with no bookmaker margin: -150 means risk $150 to win $100, +150 means risk $100 to win $150.

The edge columns check every side of the spread, the moneyline and the total for expected value: the profit per $1 bet at the posted price, using the final prediction's chances (the model blended with the line, simulated against the posted lines, pushes returning the stake, and anchored to the market's own chances so only what the blend moves off the line counts). The model's own spread and total are shown alongside, but the blend keeps only the share of that disagreement the model has earned in past seasons, so edges are rare. A side is an edge when its EV is 3% or more; the best such side is shown with its price, its EV, its chance of winning the bet and its stake, a 25% share of the Kelly stake in units of 1% of the bankroll, with at most 3 units on one game. Where a spread or total price is not posted it is assumed to be -110 (marked \*); a moneyline is never assumed. Edges are logged with each prediction, locked at tip-off and graded below. Treat them as an experiment, not betting advice; see the backtest for how they have done on past seasons.

## Thursday, November 12

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Spread: model / line | Total: model / line | 80% range | Overtime | Missing (effect on margin) | Spread edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 7:00 PM | TOR @ PHI | TOR 109, PHI 117 | PHI 72% | TOR +260 / PHI -260 | PHI -7.8 | 225.5 | 94–124 / 103–131 | 4% | TOR: Scottie Barnes (out); Kawhi Leonard (out) (-2.8)<br>PHI: LeBron James (day-to-day); Joel Embiid (day-to-day); Adem Bona (out); Dominick Barlow (out) (-0.6) | no line yet | no line yet | no line yet |
| 7:00 PM | DET @ WAS | DET 115, WAS 105 | DET 77% | DET -335 / WAS +335<br>posted DET -369 / WAS +293 | DET -9.8 / DET -9.5 (fav covers 51%) | 220.5 / 220.5 (over 49%) | 101–129 / 91–120 | 4% | DET: Jalen Duren (out) (+0.1)<br>WAS: Jamir Watkins (out); Justin Champagnie (out); Tristan Vukcevic (out) (+0.0) | no edge | no edge | no edge |
| 8:00 PM | DAL @ MIN | DAL 111, MIN 116 | MIN 65% | DAL +190 / MIN -190<br>posted DAL +164 / MIN -196 | MIN -5.3 / MIN -5.5 (fav covers 51%) | 226.6 / 226.5 (over 50%) | 96–125 / 102–130 | 5% | DAL: Morez Johnson Jr. (day-to-day); Dereck Lively II (out); Sergio de Larrea (out) (+1.3)<br>MIN: Anthony Edwards (out); Donte DiVincenzo (out) (-0.7) | no edge | no edge | no edge |
| 9:00 PM | CHA @ PHX | CHA 103, PHX 111 | PHX 72% | CHA +260 / PHX -260<br>posted CHA +202 / PHX -245 | PHX -7.7 / PHX -7.5 (fav covers 51%) | 213.3 / 213.5 (over 49%) | 89–117 / 96–124 | 4% | CHA: Moussa Diabate (day-to-day); Dennis Schroder (out); Brandon Miller (out); Kon Knueppel (out); Grant Williams (out) (-1.3)<br>PHX: Mark Williams (out) (+0.4) | no edge | no edge | no edge |

## Friday, November 13

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Spread: model / line | Total: model / line | 80% range | Overtime | Missing (effect on margin) | Spread edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 7:00 PM | NYK @ IND | NYK 111, IND 107 | NYK 63% | NYK -165 / IND +165 | NYK -4.2 | 218.3 | 97–125 / 93–121 | 6% | IND: Tyrese Haliburton (out); Aaron Nesmith (day-to-day); Johnny Furphy (out); Ben Sheppard (out) (-0.3) | no line yet | no line yet | no line yet |
| 7:00 PM | MIL @ ORL | MIL 106, ORL 117 | ORL 80% | MIL +400 / ORL -400 | ORL -11.2 | 223.2 | 91–121 / 103–131 | 4% | MIL: Myles Turner (out); Ryan Rollins (day-to-day) (-0.8)<br>ORL: Paolo Banchero (out); Jalen Suggs (out); Tristan da Silva (out); Jamal Cain (out) (+1.9) | no line yet | no line yet | no line yet |
| 8:00 PM | CLE @ MIA | CLE 116, MIA 118 | MIA 57% | CLE +130 / MIA -130 | MIA -2.1 | 234.7 | 102–131 / 104–133 | 5% | CLE: Sam Merrill (out) (-0.7) | no line yet | no line yet | no line yet |
| 8:00 PM | ATL @ CHI | ATL 126, CHI 120 | ATL 65% | ATL -185 / CHI +185 | ATL -5.3 | 246.3 | 111–141 / 105–136 | 5% | ATL: Keshon Gilbert (out) (+2.0)<br>CHI: Caleb Wilson (day-to-day); Norman Powell (out) (-0.2) | no line yet | no line yet | no line yet |
| 8:00 PM | MEM @ NOP | MEM 117, NOP 116 | MEM 54% | MEM -115 / NOP +115 | MEM -1.3 | 233.6 | 103–132 / 101–131 | 5% | MEM: Scotty Pippen Jr. (out) (+0.9)<br>NOP: Trey Murphy III (out); Yves Missi (out); Trendon Watford (out); Bennedict Mathurin (out) (+0.4) | no line yet | no line yet | no line yet |
| 8:30 PM | UTA @ HOU | UTA 102, HOU 118 | HOU 88% | UTA +710 / HOU -710 | HOU -15.5 | 220.2 | 88–117 / 104–131 | 3% | UTA: Lauri Markkanen (out); Jaren Jackson Jr. (out); Jusuf Nurkic (out) (-3.0)<br>HOU: Steven Adams (out); Clint Capela (out) (-0.6) | no line yet | no line yet | no line yet |
| 9:30 PM | GSW @ SAS | GSW 109, SAS 116 | SAS 71% | GSW +245 / SAS -245 | SAS -7.2 | 225.1 | 95–124 / 102–130 | 5% | GSW: Moses Moody (out); Stephen Curry (day-to-day); Jimmy Butler III (out); Kristaps Porzingis (out); Gary Payton II (out); Brandon Williams (out) (-1.4)<br>SAS: Tobias Harris (out); Devin Vassell (out) (+0.0) | no line yet | no line yet | no line yet |
| 10:00 PM | POR @ SAC | POR 119, SAC 110 | POR 73% | POR -275 / SAC +275 | POR -8.5 | 229.2 | 105–133 / 96–125 | 4% | POR: Ja Morant (out); Chris Youngblood (out) (+0.5)<br>SAC: Maxime Raynaud (out); Precious Achiuwa (day-to-day) (+0.6) | no line yet | no line yet | no line yet |
| 10:30 PM | OKC @ LAC | OKC 114, LAC 111 | OKC 60% | OKC -145 / LAC +145 | OKC -3.3 | 224.6 | 100–128 / 96–126 | 6% | OKC: Chet Holmgren (out); Jalen Williams (out); Ajay Mitchell (out); Jaylin Williams (out); Cason Wallace (out) (-1.0)<br>LAC: Brandon Ingram (out); Jordan Miller (out); Bradley Beal (out); Yanic Konan Niederhauser (out) (+0.4) | no line yet | no line yet | no line yet |

## How the 2026-27 predictions have done

| Predictor | Games | Margin MAE | Total MAE | Team-points MAE | Log loss | Brier | Winners | 80% range hit |
|---|---|---|---|---|---|---|---|---|
| Final prediction | 160 | 11.20 | 14.17 | 9.33 | 0.555 | 0.188 | 71.9% | 81.2% |
| Model only (before blending) | 160 | 11.57 | 14.02 | 9.42 | 0.579 | 0.198 | 70.0% | – |
| Elo | 160 | 11.97 | – | – | 0.598 | 0.208 | 65.0% | – |
| Final prediction, games with a line | 160 | 11.20 | 14.17 | 9.33 | 0.555 | 0.188 | 71.9% | 81.2% |
| Model only, games with a line | 160 | 11.57 | 14.02 | 9.42 | 0.579 | 0.198 | 70.0% | – |
| Betting line | 160 | 11.15 | 14.18 | 9.32 | 0.545 | 0.184 | 71.9% | – |

MAE is the average miss in points; team-points MAE is the average miss on each team's score. Log loss and Brier score the win chances (lower is better; a coin flip scores 0.693 and 0.250). The closing line misses margins by about 10 points and totals by about 14.

Overtime: predicted in 4.7% of games, happened in 5.0%.

### Betting edges

| Market | Edges | Record (W-L-P) | Staked | Units won | ROI | Expected ROI |
|---|---|---|---|---|---|---|
| Spread | 1 | 1-0-0 | 1.0 | +0.90 | +89.3% | +3.6% |
| Moneyline | 9 | 0-9-0 | 3.5 | -3.47 | -100.0% | +8.3% |
| Total | 0 | 0-0-0 | 0.0 | +0.00 | – | – |

Spread moved toward the model's first spread edge before tip-off: 5 of 6 games (83%).

Live predictions only, each edge at the stake and price logged with the last prediction before tip-off (edges logged before edges were priced from the final prediction are left out); a push returns the stake. Units are 1% of the bankroll; ROI is units won per unit staked, and expected ROI is what the edges' EVs promised. The line moving toward the model's edge before tip-off is the quickest sign that it knows something the market doesn't yet.

### Results, Tuesday, November 10

| Game | Predicted | Final | Win chance for winner | Spread: model / line | Inside 80% ranges |
|---|---|---|---|---|---|
| MIL @ NYK | 103–119 | 85–117 | 87% | NYK -15.4 / NYK -15.5 | no |
| BOS @ PHI | 110–108 | 123–101 | 55% | BOS -1.7 / BOS -1.5 | yes |
| LAC @ PHX | 110–113 | 110–133 | 60% | PHX -3.1 / PHX -3.5 | no |
| MIA @ UTA | 118–110 | 115–109 | 72% | MIA -7.7 / MIA -8.5 | yes |
| ORL @ SAC | 114–109 | 107–100 | 65% | ORL -5.3 / ORL -5.5 | yes |
| OKC @ POR | 114–113 | 103–123 | 47% | OKC -1.1 / OKC -1.5 | yes |

## Power ratings

Points per 100 possessions better than an average team on a neutral floor, combining opponent-adjusted team efficiency (garbage time removed) with the ratings of the team's healthy roster, through the fitted points map. Net per game uses the team's pace. Injury effect now is what its current injury report does to its margin, in points.

| # | Team | Net per 100 | Net per game | Offense | Defense | Pace | Injury effect now | Elo |
|---|---|---|---|---|---|---|---|---|
| 1 | BOS | +7.7 | +7.4 | +4.3 | +3.4 | 95.5 | -0.2 | 1663 |
| 2 | SAS | +7.5 | +7.6 | +3.2 | +4.3 | 101.0 | +0.0 | 1723 |
| 3 | HOU | +7.4 | +7.3 | +3.2 | +4.3 | 98.4 | -0.6 | 1620 |
| 4 | DET | +6.1 | +6.2 | +2.3 | +3.8 | 101.6 | +0.1 | 1645 |
| 5 | MIN | +5.6 | +5.8 | +2.5 | +3.2 | 102.7 | -0.7 | 1622 |
| 6 | LAL | +5.3 | +5.4 | +4.8 | +0.5 | 102.0 | -2.7 | 1620 |
| 7 | NYK | +3.9 | +3.7 | +1.3 | +2.7 | 94.1 | +0.0 | 1703 |
| 8 | DEN | +3.7 | +3.6 | +4.1 | -0.4 | 97.4 | +0.2 | 1575 |
| 9 | GSW | +3.5 | +3.5 | +2.1 | +1.3 | 101.0 | -1.4 | 1539 |
| 10 | OKC | +3.3 | +3.3 | -0.5 | +3.7 | 101.4 | -1.0 | 1664 |
| 11 | POR | +2.8 | +2.9 | +2.5 | +0.4 | 102.1 | +0.5 | 1565 |
| 12 | PHI | +1.6 | +1.6 | -0.2 | +1.8 | 100.9 | -0.6 | 1559 |
| 13 | DAL | +0.6 | +0.6 | +0.4 | +0.1 | 101.6 | +1.3 | 1450 |
| 14 | TOR | +0.2 | +0.2 | -0.1 | +0.3 | 103.0 | -2.8 | 1525 |
| 15 | CLE | +0.1 | +0.2 | +1.2 | -1.0 | 102.1 | -0.7 | 1565 |
| 16 | PHX | -0.1 | -0.1 | +0.7 | -0.8 | 101.4 | +0.4 | 1501 |
| 17 | MIA | -0.5 | -0.6 | +0.5 | -1.0 | 105.0 | +0.0 | 1495 |
| 18 | ORL | -1.5 | -1.5 | -2.8 | +1.3 | 100.4 | +1.9 | 1495 |
| 19 | MEM | -1.7 | -1.7 | +0.0 | -1.7 | 101.7 | +0.9 | 1428 |
| 20 | IND | -2.0 | -2.1 | -0.6 | -1.4 | 103.3 | -0.3 | 1355 |
| 21 | ATL | -2.2 | -2.3 | -0.9 | -1.2 | 108.1 | +2.0 | 1539 |
| 22 | LAC | -3.5 | -3.6 | -1.5 | -2.0 | 101.4 | +0.4 | 1471 |
| 23 | UTA | -3.6 | -3.7 | -3.6 | +0.0 | 102.2 | -3.1 | 1293 |
| 24 | NOP | -4.5 | -4.7 | -1.4 | -3.1 | 103.2 | +0.4 | 1412 |
| 25 | WAS | -5.3 | -5.4 | -3.2 | -2.1 | 101.9 | +0.0 | 1330 |
| 26 | CHA | -5.5 | -5.3 | -4.4 | -1.1 | 96.4 | -1.3 | 1481 |
| 27 | BKN | -6.3 | -6.4 | -3.7 | -2.5 | 102.2 | +1.6 | 1306 |
| 28 | CHI | -7.0 | -7.8 | -3.2 | -3.8 | 110.8 | -0.2 | 1351 |
| 29 | SAC | -7.7 | -7.9 | -3.8 | -3.9 | 102.2 | +0.6 | 1328 |
| 30 | MIL | -8.0 | -8.0 | -3.1 | -4.8 | 100.8 | -0.8 | 1327 |

## Top players

Regularized adjusted plus-minus from every lineup this season and past ones: points per 100 possessions a player adds on offense and saves on defense, against an average player, shrunk toward last season's rating. Players expected to play 20 minutes or more.

| # | Player | Team | Net impact per 100 | Offense | Defense | Expected minutes |
|---|---|---|---|---|---|---|
| 1 | Victor Wembanyama | SAS | +7.9 | +2.3 | +5.5 | 27 |
| 2 | Shai Gilgeous-Alexander | OKC | +5.8 | +5.0 | +0.8 | 31 |
| 3 | Nikola Jokic | DEN | +5.2 | +4.9 | +0.3 | 36 |
| 4 | Luka Doncic | LAL | +4.6 | +5.3 | -0.7 | 37 |
| 5 | Kawhi Leonard | TOR | +4.5 | +3.6 | +0.9 | 30 |
| 6 | Kyrie Irving | DAL | +4.1 | +3.9 | +0.2 | 33 |
| 7 | Giannis Antetokounmpo | MIA | +3.9 | +3.7 | +0.2 | 33 |
| 8 | Joel Embiid | PHI | +2.9 | +1.4 | +1.4 | 30 |
| 9 | Stephen Curry | GSW | +2.8 | +4.7 | -1.9 | 28 |
| 10 | Donovan Mitchell | CLE | +2.6 | +3.1 | -0.5 | 30 |
| 11 | Herbert Jones | NOP | +2.3 | -0.5 | +2.8 | 23 |
| 12 | Fred VanVleet | HOU | +2.3 | +1.4 | +1.0 | 30 |
| 13 | LaMelo Ball | MIN | +2.2 | +4.2 | -1.9 | 31 |
| 14 | Jimmy Butler III | GSW | +2.2 | +2.1 | +0.1 | 27 |
| 15 | Franz Wagner | ORL | +2.1 | +0.9 | +1.2 | 38 |
| 16 | Chet Holmgren | OKC | +2.1 | +0.0 | +2.1 | 30 |
| 17 | Dyson Daniels | ATL | +2.0 | +0.6 | +1.5 | 32 |
| 18 | Ty Jerome | MEM | +2.0 | +3.1 | -1.1 | 30 |
| 19 | Neemias Queta | BOS | +1.9 | +1.0 | +0.9 | 22 |
| 20 | Ausar Thompson | DET | +1.8 | -0.4 | +2.2 | 28 |
| 21 | Rudy Gobert | MIN | +1.8 | -3.2 | +5.0 | 29 |
| 22 | Derrick White | BOS | +1.8 | +0.5 | +1.2 | 26 |
| 23 | De'Aaron Fox | SAS | +1.7 | +1.6 | +0.1 | 27 |
| 24 | Pascal Siakam | IND | +1.6 | +1.5 | +0.1 | 33 |
| 25 | Jrue Holiday | POR | +1.5 | +0.9 | +0.6 | 25 |
| 26 | Dean Wade | PHI | +1.5 | +0.3 | +1.2 | 22 |
| 27 | Paul George | BOS | +1.4 | +0.5 | +0.9 | 29 |
| 28 | Cade Cunningham | DET | +1.3 | +1.5 | -0.1 | 32 |
| 29 | Lauri Markkanen | UTA | +1.3 | +1.1 | +0.2 | 33 |
| 30 | Damian Lillard | POR | +1.3 | +2.0 | -0.7 | 27 |

## Current model fit

- Fitted on 5442 games from 2022-23 to 2026-27.
- Home court: +2.0 points per 100 possessions for the home team over the visitor (about 2.0 points a game).
- Second night of a back-to-back: -0.8 points per 100 scored, +1.2 allowed.
- Weights: team efficiency ratings 0.16 (offense) and 0.15 (defense); player lineup ratings 0.76 and 0.76.
- Blend: 82% on the betting line for the margin and 100% for the total, wherever there is a line (fitted on past closing lines).
- Simulator: each team's points vary by 10.9 with correlation 0.23; 5.1% of recent games went to overtime.
