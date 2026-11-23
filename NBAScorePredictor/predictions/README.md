# NBA score predictions

Updated Mon Nov 23, 2026 03:33 AM ET. Refreshed automatically several times a day during the season, around the injury report's deadlines; each game's prediction is locked at tip-off and graded once the final score is in.

Each team's expected points are its expected possessions times its expected points per possession, from team efficiency ratings and the ratings of the players expected to play, blended with the betting line. Each game is then simulated 10,000 times, overtime included. The predicted score is the expected points rounded; the 80% range holds 80% of simulated outcomes for each team. Basketball is the most predictable major sport, but a team's score still varies by about ±14 points around the forecast, so read the win chance and the ranges too.

Missing players come from the injury report: out players are left out, and doubtful, questionable and probable ones count with the share of their minutes their chance of playing implies, and their minutes go mostly to the bench. The effect is how many points of margin the team gains or loses against its full-strength roster: negative when it is missing good players, positive when the minutes go to better ones. Predictions are rerun when the report changes, up to tip-off.

The fair moneyline is the American odds that match the win chance exactly, with no bookmaker margin: -150 means risk $150 to win $100, +150 means risk $100 to win $150.

The edge columns check every side of the spread, the moneyline and the total for expected value: the profit per $1 bet at the posted price, using the final prediction's chances (the model blended with the line, simulated against the posted lines, pushes returning the stake, and anchored to the market's own chances so only what the blend moves off the line counts). The model's own spread and total are shown alongside, but the blend keeps only the share of that disagreement the model has earned in past seasons, so edges are rare. A side is an edge when its EV is 3% or more; the best such side is shown with its price, its EV, its chance of winning the bet and its stake, a 25% share of the Kelly stake in units of 1% of the bankroll, with at most 3 units on one game. Where a spread or total price is not posted it is assumed to be -110 (marked \*); a moneyline is never assumed. Edges are logged with each prediction, locked at tip-off and graded below. Treat them as an experiment, not betting advice; see the backtest for how they have done on past seasons.

## Monday, November 23

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Spread: model / line | Total: model / line | 80% range | Overtime | Missing (effect on margin) | Spread edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 7:00 PM | MEM @ CHA | MEM 110, CHA 106 | MEM 62% | MEM -160 / CHA +160<br>posted MEM -162 / CHA +136 | MEM -3.7 / MEM -3.5 (fav covers 53%) | 216.6 / 216.5 (over 49%) | 96–124 / 92–121 | 5% | MEM: Cameron Boozer (out); Jerami Grant (out); Scotty Pippen Jr. (out) (+2.1)<br>CHA: Brandon Miller (day-to-day); Grayson Allen (out); Dennis Schroder (out); Grant Williams (out); Kon Knueppel (out) (-1.2) | no edge | no edge | no edge |
| 7:00 PM | POR @ PHI | POR 113, PHI 117 | PHI 61% | POR +155 / PHI -155<br>posted POR +142 / PHI -169 | PHI -3.7 / PHI -4.5 (fav covers 49%) | 230.7 / 230.5 (over 50%) | 99–128 / 103–132 | 5% | POR: Ja Morant (out); Chris Youngblood (out) (+0.6)<br>PHI: Jaylen Brown (day-to-day); Dean Wade (day-to-day); Adem Bona (out) (+0.2) | no edge | no edge | no edge |
| 7:30 PM | OKC @ IND | OKC 113, IND 110 | OKC 60% | OKC -145 / IND +145<br>posted OKC -191 / IND +160 | OKC -3.3 / OKC -4.5 (fav covers 48%) | 222.7 / 222.5 (over 50%) | 99–127 / 96–124 | 5% | OKC: Shai Gilgeous-Alexander (out); Chet Holmgren (out); Jalen Williams (out); Aday Mara (out); Cason Wallace (out); Alex Caruso (out); Jaylin Williams (out) (-4.6)<br>IND: Tyrese Haliburton (out); Johnny Furphy (out); Ben Sheppard (out); T.J. McConnell (out) (+0.2) | no edge | IND ML (+160): EV +4.2%, 40%, stake 0.7u | no edge |
| 7:30 PM | MIL @ TOR | MIL 107, TOR 117 | TOR 76% | MIL +325 / TOR -325<br>posted MIL +378 / TOR -494 | TOR -9.9 / TOR -10.5 (fav covers 47%) | 223.4 / 223.5 (over 49%) | 92–122 / 102–131 | 4% | TOR: RJ Barrett (out); Kawhi Leonard (out); Collin Murray-Boyles (day-to-day) (-2.4) | no edge | MIL ML (+378): EV +3.2%, 22%, stake 0.2u | no edge |
| 7:30 PM | BKN @ MIN | BKN 106, MIN 117 | MIN 81% | BKN +420 / MIN -420<br>posted BKN +455 / MIN -620 | MIN -11.6 / MIN -11.5 (fav covers 49%) | 223.2 / 223.5 (over 49%) | 91–120 / 103–131 | 3% | BKN: Nolan Traore (out) (+0.8)<br>MIN: Anthony Edwards (out); Donte DiVincenzo (out); Jaylen Clark (out) (-0.6) | no edge | no edge | no edge |
| 8:00 PM | CLE @ CHI | CLE 124, CHI 116 | CLE 71% | CLE -245 / CHI +245<br>posted CLE -337 / CHI +271 | CLE -7.7 / CLE -8.5 (fav covers 48%) | 240.4 / 240.5 (over 49%) | 109–139 / 101–131 | 4% | CLE: Evan Mobley (out); Jaylon Tyson (out) (-0.1)<br>CHI: Norman Powell (out); Caleb Wilson (out); Nic Claxton (out) (+0.4) | no edge | no edge | no edge |
| 8:00 PM | PHX @ NOP | PHX 119, NOP 115 | PHX 59% | PHX -145 / NOP +145<br>posted PHX -155 / NOP +131 | PHX -3.6 / PHX -3.5 (fav covers 51%) | 233.7 / 233.5 (over 50%) | 104–133 / 100–130 | 5% | PHX: Mark Williams (out); Ryan Dunn (day-to-day) (+0.5)<br>NOP: Zion Williamson (day-to-day); Trey Murphy III (day-to-day); Dejounte Murray (out); Trendon Watford (out); Bennedict Mathurin (out); Bryce McGowens (out) (+0.0) | no edge | no edge | no edge |
| 8:30 PM | LAC @ HOU | LAC 107, HOU 119 | HOU 82% | LAC +460 / HOU -460<br>posted LAC +471 / HOU -650 | HOU -12.2 / HOU -12.5 (fav covers 47%) | 225.2 / 225.5 (over 49%) | 92–121 / 105–133 | 4% | LAC: Jordan Miller (out); Bradley Beal (out) (+0.5) | no edge | no edge | no edge |
| 10:00 PM | UTA @ LAL | UTA 107, LAL 120 | LAL 83% | UTA +475 / LAL -475<br>posted UTA +554 / LAL -790 | LAL -12.8 / LAL -13.5 (fav covers 46%) | 227.1 / 227.5 (over 48%) | 92–122 / 106–134 | 4% | UTA: Lauri Markkanen (out); Jaxson Hayes (out); Jaren Jackson Jr. (out); Jusuf Nurkic (out) (-2.2)<br>LAL: Austin Reaves (out) (-1.3) | no edge | UTA ML (+554): EV +4.8%, 16%, stake 0.2u | no edge |
| 10:00 PM | SAS @ SAC | SAS 117, SAC 107 | SAS 79% | SAS -370 / SAC +370<br>posted SAS -484 / SAC +371 | SAS -10.6 / SAS -10.5 (fav covers 50%) | 224.2 / 224.5 (over 49%) | 103–131 / 92–121 | 4% | SAS: Dylan Harper (out); Victor Wembanyama (day-to-day); Tobias Harris (out); De'Aaron Fox (day-to-day); Jordan McLaughlin (day-to-day) (-1.9)<br>SAC: Maxime Raynaud (out) (+0.7) | no edge | no edge | no edge |

## Tuesday, November 24

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Spread: model / line | Total: model / line | 80% range | Overtime | Missing (effect on margin) | Spread edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 7:00 PM | DET @ ORL | DET 109, ORL 107 | DET 53% | DET -115 / ORL +115 | DET -1.1 | 215.9 | 95–123 / 93–122 | 5% | DET: Duncan Robinson (out); Jalen Duren (out) (-0.2)<br>ORL: Paolo Banchero (out) (+1.7) | no line yet | no line yet | no line yet |
| 8:00 PM | BOS @ WAS | BOS 115, WAS 106 | BOS 76% | BOS -320 / WAS +320 | BOS -9.4 | 220.7 | 101–129 / 91–120 | 4% | BOS: Paul George (out); Mitchell Robinson (out) (-0.4)<br>WAS: Jamir Watkins (out); Justin Champagnie (out); Tristan Vukcevic (out) (+0.1) | no line yet | no line yet | no line yet |
| 10:00 PM | DAL @ DEN | DAL 111, DEN 119 | DEN 72% | DAL +255 / DEN -255 | DEN -7.8 | 230.3 | 97–126 / 104–133 | 5% | DAL: P.J. Washington (out); Dereck Lively II (out); Sergio de Larrea (out) (+0.8) | no line yet | no line yet | no line yet |

## How the 2026-27 predictions have done

| Predictor | Games | Margin MAE | Total MAE | Team-points MAE | Log loss | Brier | Winners | 80% range hit |
|---|---|---|---|---|---|---|---|---|
| Final prediction | 241 | 11.00 | 14.38 | 9.32 | 0.570 | 0.194 | 70.5% | 81.1% |
| Model only (before blending) | 241 | 11.24 | 14.31 | 9.39 | 0.586 | 0.201 | 70.1% | – |
| Elo | 241 | 11.59 | – | – | 0.610 | 0.211 | 65.6% | – |
| Final prediction, games with a line | 241 | 11.00 | 14.38 | 9.32 | 0.570 | 0.194 | 70.5% | 81.1% |
| Model only, games with a line | 241 | 11.24 | 14.31 | 9.39 | 0.586 | 0.201 | 70.1% | – |
| Betting line | 241 | 10.97 | 14.39 | 9.31 | 0.567 | 0.193 | 70.5% | – |

MAE is the average miss in points; team-points MAE is the average miss on each team's score. Log loss and Brier score the win chances (lower is better; a coin flip scores 0.693 and 0.250). The closing line misses margins by about 10 points and totals by about 14.

Overtime: predicted in 4.7% of games, happened in 5.0%.

### Betting edges

| Market | Edges | Record (W-L-P) | Staked | Units won | ROI | Expected ROI |
|---|---|---|---|---|---|---|
| Spread | 1 | 1-0-0 | 1.0 | +0.90 | +89.3% | +3.6% |
| Moneyline | 15 | 2-13-0 | 5.6 | -2.59 | -46.2% | +6.5% |
| Total | 0 | 0-0-0 | 0.0 | +0.00 | – | – |

Spread moved toward the model's first spread edge before tip-off: 5 of 6 games (83%).

Live predictions only, each edge at the stake and price logged with the last prediction before tip-off (edges logged before edges were priced from the final prediction are left out); a push returns the stake. Units are 1% of the bankroll; ROI is units won per unit staked, and expected ROI is what the edges' EVs promised. The line moving toward the model's edge before tip-off is the quickest sign that it knows something the market doesn't yet.

### Results, Saturday, November 21

| Game | Predicted | Final | Win chance for winner | Spread: model / line | Inside 80% ranges |
|---|---|---|---|---|---|
| MIL @ PHI | 108–121 | 129–132 | 82% | PHI -12.5 / PHI -12.5 | no |
| POR @ NYK | 107–108 | 96–97 | 54% | NYK -1.4 / NYK -1.5 | yes |
| LAC @ DAL | 113–118 | 100–110 | 63% | DAL -4.5 / DAL -4.5 | yes |
| MEM @ MIN | 112–117 | 95–104 | 65% | MIN -5.2 / MIN -5.5 | no |
| NOP @ SAS | 105–123 | 91–114 | 91% | SAS -18.4 / SAS -18.5 | yes |
| BOS @ SAC | 113–102 | 96–97 | 20% | BOS -11.4 / BOS -11.5 | no |

## Power ratings

Points per 100 possessions better than an average team on a neutral floor, combining opponent-adjusted team efficiency (garbage time removed) with the ratings of the team's healthy roster, through the fitted points map. Net per game uses the team's pace. Injury effect now is what its current injury report does to its margin, in points.

| # | Team | Net per 100 | Net per game | Offense | Defense | Pace | Injury effect now | Elo |
|---|---|---|---|---|---|---|---|---|
| 1 | SAS | +7.7 | +7.6 | +2.8 | +4.8 | 99.9 | -1.9 | 1718 |
| 2 | BOS | +7.2 | +6.9 | +2.7 | +4.4 | 96.8 | -0.4 | 1639 |
| 3 | HOU | +5.9 | +5.8 | +3.8 | +2.1 | 98.5 | +0.0 | 1613 |
| 4 | DET | +5.4 | +5.2 | +2.5 | +2.9 | 97.6 | -0.2 | 1640 |
| 5 | MIN | +5.1 | +5.2 | +0.7 | +4.4 | 103.5 | -0.6 | 1612 |
| 6 | DEN | +4.5 | +4.5 | +4.2 | +0.3 | 100.2 | +0.2 | 1582 |
| 7 | NYK | +4.0 | +3.7 | +0.4 | +3.6 | 92.4 | -1.8 | 1694 |
| 8 | LAL | +3.6 | +3.7 | +3.3 | +0.4 | 101.7 | -1.3 | 1604 |
| 9 | OKC | +3.2 | +3.2 | -0.3 | +3.5 | 102.1 | -4.5 | 1641 |
| 10 | POR | +2.9 | +3.0 | +1.5 | +1.4 | 102.4 | +0.6 | 1576 |
| 11 | PHI | +1.9 | +1.9 | +1.6 | +0.3 | 100.7 | +0.2 | 1583 |
| 12 | PHX | +0.6 | +0.6 | +1.1 | -0.5 | 100.4 | +0.5 | 1534 |
| 13 | ORL | +0.5 | +0.5 | -1.1 | +1.6 | 99.2 | +1.7 | 1521 |
| 14 | CLE | +0.4 | +0.4 | +1.8 | -1.5 | 101.7 | -0.1 | 1570 |
| 15 | MIA | +0.3 | +0.3 | +1.9 | -1.6 | 105.2 | -3.4 | 1548 |
| 16 | TOR | +0.2 | +0.2 | +0.1 | +0.2 | 97.3 | -2.3 | 1500 |
| 17 | MEM | -0.8 | -0.8 | +1.3 | -2.1 | 100.3 | +2.2 | 1487 |
| 18 | GSW | -1.0 | -1.0 | -0.9 | -0.1 | 99.9 | -3.5 | 1468 |
| 19 | UTA | -1.2 | -1.2 | -2.0 | +0.8 | 100.5 | -2.2 | 1346 |
| 20 | IND | -1.4 | -1.5 | -0.3 | -1.1 | 104.0 | +0.2 | 1362 |
| 21 | DAL | -1.7 | -1.7 | -1.0 | -0.7 | 100.9 | +0.8 | 1456 |
| 22 | ATL | -2.1 | -2.2 | -2.0 | -0.1 | 106.5 | +1.0 | 1549 |
| 23 | LAC | -3.4 | -3.5 | -1.3 | -2.1 | 101.1 | +0.5 | 1433 |
| 24 | CHI | -4.0 | -4.3 | -2.3 | -1.6 | 107.3 | +0.4 | 1399 |
| 25 | CHA | -5.2 | -5.0 | -4.7 | -0.5 | 95.4 | -1.2 | 1460 |
| 26 | WAS | -5.3 | -5.3 | -2.6 | -2.6 | 100.3 | +0.1 | 1325 |
| 27 | NOP | -5.4 | -5.5 | -1.6 | -3.8 | 102.9 | +0.0 | 1359 |
| 28 | BKN | -6.9 | -6.9 | -2.5 | -4.3 | 100.9 | +0.8 | 1308 |
| 29 | SAC | -7.6 | -7.6 | -4.2 | -3.4 | 101.1 | +0.7 | 1315 |
| 30 | MIL | -7.6 | -7.8 | -2.8 | -4.8 | 103.0 | +0.2 | 1308 |

## Top players

Regularized adjusted plus-minus from every lineup this season and past ones: points per 100 possessions a player adds on offense and saves on defense, against an average player, shrunk toward last season's rating. Players expected to play 20 minutes or more.

| # | Player | Team | Net impact per 100 | Offense | Defense | Expected minutes |
|---|---|---|---|---|---|---|
| 1 | Victor Wembanyama | SAS | +8.5 | +2.6 | +5.9 | 32 |
| 2 | Shai Gilgeous-Alexander | OKC | +5.7 | +5.1 | +0.6 | 35 |
| 3 | Nikola Jokic | DEN | +5.0 | +4.7 | +0.3 | 38 |
| 4 | Kawhi Leonard | TOR | +4.6 | +3.6 | +0.9 | 30 |
| 5 | Giannis Antetokounmpo | MIA | +4.4 | +4.3 | +0.1 | 31 |
| 6 | Luka Doncic | LAL | +3.7 | +4.8 | -1.1 | 37 |
| 7 | Kyrie Irving | DAL | +3.6 | +3.6 | +0.1 | 33 |
| 8 | Joel Embiid | PHI | +2.8 | +1.9 | +0.9 | 33 |
| 9 | Franz Wagner | ORL | +2.7 | +1.7 | +1.0 | 37 |
| 10 | Neemias Queta | BOS | +2.7 | +0.8 | +1.9 | 26 |
| 11 | Derrick White | BOS | +2.6 | +0.6 | +2.0 | 31 |
| 12 | Herbert Jones | NOP | +2.4 | -0.7 | +3.1 | 28 |
| 13 | Dyson Daniels | ATL | +2.3 | +0.3 | +2.0 | 34 |
| 14 | Jimmy Butler III | GSW | +2.2 | +2.1 | +0.1 | 27 |
| 15 | Paul Reed | DET | +2.1 | +0.8 | +1.4 | 25 |
| 16 | Chet Holmgren | OKC | +2.1 | +0.0 | +2.1 | 30 |
| 17 | LaMelo Ball | MIN | +2.1 | +3.4 | -1.4 | 31 |
| 18 | Pascal Siakam | IND | +2.1 | +1.5 | +0.6 | 32 |
| 19 | Bam Adebayo | MIA | +2.0 | +1.4 | +0.6 | 29 |
| 20 | Marcus Smart | HOU | +2.0 | +0.5 | +1.4 | 20 |
| 21 | Javonte Green | DET | +2.0 | +0.1 | +1.8 | 24 |
| 22 | Fred VanVleet | HOU | +1.9 | +1.6 | +0.3 | 30 |
| 23 | Donovan Mitchell | CLE | +1.9 | +3.0 | -1.2 | 32 |
| 24 | Damian Lillard | POR | +1.8 | +1.8 | +0.1 | 32 |
| 25 | Ausar Thompson | DET | +1.8 | +0.0 | +1.8 | 31 |
| 26 | Jrue Holiday | POR | +1.8 | +1.1 | +0.7 | 30 |
| 27 | De'Aaron Fox | SAS | +1.7 | +1.4 | +0.3 | 28 |
| 28 | Ty Jerome | MEM | +1.7 | +2.6 | -0.9 | 29 |
| 29 | Dean Wade | PHI | +1.7 | +0.9 | +0.8 | 30 |
| 30 | Karl-Anthony Towns | NYK | +1.6 | +1.7 | +0.0 | 35 |

## Current model fit

- Fitted on 5523 games from 2022-23 to 2026-27.
- Home court: +2.0 points per 100 possessions for the home team over the visitor (about 2.0 points a game).
- Second night of a back-to-back: -0.8 points per 100 scored, +1.2 allowed.
- Weights: team efficiency ratings 0.14 (offense) and 0.15 (defense); player lineup ratings 0.77 and 0.76.
- Blend: 82% on the betting line for the margin and 100% for the total, wherever there is a line (fitted on past closing lines).
- Simulator: each team's points vary by 11.0 with correlation 0.23; 5.1% of recent games went to overtime.
