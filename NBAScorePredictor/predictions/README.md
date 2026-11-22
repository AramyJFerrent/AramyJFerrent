# NBA score predictions

Updated Sun Nov 22, 2026 03:26 PM ET. Refreshed automatically several times a day during the season, around the injury report's deadlines; each game's prediction is locked at tip-off and graded once the final score is in.

Each team's expected points are its expected possessions times its expected points per possession, from team efficiency ratings and the ratings of the players expected to play, blended with the betting line. Each game is then simulated 10,000 times, overtime included. The predicted score is the expected points rounded; the 80% range holds 80% of simulated outcomes for each team. Basketball is the most predictable major sport, but a team's score still varies by about ±14 points around the forecast, so read the win chance and the ranges too.

Missing players come from the injury report: out players are left out, and doubtful, questionable and probable ones count with the share of their minutes their chance of playing implies, and their minutes go mostly to the bench. The effect is how many points of margin the team gains or loses against its full-strength roster: negative when it is missing good players, positive when the minutes go to better ones. Predictions are rerun when the report changes, up to tip-off.

The fair moneyline is the American odds that match the win chance exactly, with no bookmaker margin: -150 means risk $150 to win $100, +150 means risk $100 to win $150.

The edge columns check every side of the spread, the moneyline and the total for expected value: the profit per $1 bet at the posted price, using the final prediction's chances (the model blended with the line, simulated against the posted lines, pushes returning the stake, and anchored to the market's own chances so only what the blend moves off the line counts). The model's own spread and total are shown alongside, but the blend keeps only the share of that disagreement the model has earned in past seasons, so edges are rare. A side is an edge when its EV is 3% or more; the best such side is shown with its price, its EV, its chance of winning the bet and its stake, a 25% share of the Kelly stake in units of 1% of the bankroll, with at most 3 units on one game. Where a spread or total price is not posted it is assumed to be -110 (marked \*); a moneyline is never assumed. Edges are logged with each prediction, locked at tip-off and graded below. Treat them as an experiment, not betting advice; see the backtest for how they have done on past seasons.

## Sunday, November 22

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Spread: model / line | Total: model / line | 80% range | Overtime | Missing (effect on margin) | Spread edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 3:30 PM | DET @ ATL | DET 114, ATL 111 | DET 59% | DET -140 / ATL +140<br>posted DET -135 / ATL +114 | DET -2.9 / DET -2.5 (fav covers 53%) | 224.8 / 224.5 (over 50%) | 99–128 / 97–125 | 5% | DET: Duncan Robinson (out); Jalen Duren (out) (+0.0)<br>ATL: CJ McCollum (out); Jock Landale (out) (+1.0) | no edge | no edge | no edge |
| 6:00 PM | OKC @ MIA | OKC 114, MIA 117 | MIA 59% | OKC +145 / MIA -145<br>posted OKC +146 / MIA -173 | MIA -3.1 / MIA -3.5 (fav covers 50%) | 231.7 / 231.5 (over 49%) | 99–129 / 103–132 | 5% | OKC: Shai Gilgeous-Alexander (day-to-day); Chet Holmgren (out); Jalen Williams (out); Cason Wallace (out); Alex Caruso (out); Jaylin Williams (out) (-2.9)<br>MIA: Giannis Antetokounmpo (day-to-day); Myron Gardner (day-to-day) (-0.8) | no edge | no edge | no edge |
| 7:00 PM | ORL @ WAS | ORL 113, WAS 108 | ORL 64% | ORL -175 / WAS +175<br>posted ORL -197 / WAS +165 | ORL -4.6 / ORL -4.5 (fav covers 52%) | 220.5 / 220.5 (over 49%) | 99–127 / 94–122 | 5% | ORL: Paolo Banchero (out) (+1.7)<br>WAS: Jamir Watkins (out); Justin Champagnie (out); Tristan Vukcevic (out) (+0.3) | no edge | no edge | no edge |
| 7:00 PM | DEN @ CHI | DEN 122, CHI 113 | DEN 75% | DEN -300 / CHI +300<br>posted DEN -437 / CHI +340 | DEN -9.1 / DEN -9.5 (fav covers 48%) | 235.4 / 235.5 (over 49%) | 108–137 / 98–128 | 5% | CHI: Norman Powell (out); Jalen Smith (day-to-day); Caleb Wilson (out); Nic Claxton (day-to-day); Patrick Williams (day-to-day) (+0.0) | no edge | no edge | no edge |
| 7:00 PM | DAL @ UTA | DAL 113, UTA 112 | DAL 53% | DAL -110 / UTA +110<br>posted DAL -130 / UTA +110 | DAL -1.1 / DAL -1.5 (fav covers 50%) | 225.6 / 225.5 (over 50%) | 99–128 / 98–126 | 5% | DAL: P.J. Washington (day-to-day); Walter Clayton Jr. (day-to-day); Dereck Lively II (out); Sergio de Larrea (out) (+1.3)<br>UTA: Lauri Markkanen (out); Jaren Jackson Jr. (out); Jusuf Nurkic (out) (-2.3) | no edge | no edge | no edge |
| 8:00 PM | IND @ NYK | IND 103, NYK 110 | NYK 70% | IND +235 / NYK -235<br>posted IND +240 / NYK -296 | NYK -6.7 / NYK -7.5 (fav covers 48%) | 213.7 / 213.5 (over 50%) | 90–118 / 96–124 | 6% | IND: Pascal Siakam (day-to-day); Tyrese Haliburton (out); Johnny Furphy (out); Ben Sheppard (out); T.J. McConnell (out) (-0.5)<br>NYK: OG Anunoby (out); Karl-Anthony Towns (day-to-day) (-1.9) | no edge | no edge | no edge |
| 8:30 PM | BOS @ GSW | BOS 109, GSW 101 | BOS 75% | BOS -290 / GSW +290<br>posted BOS -344 / GSW +276 | BOS -8.3 / BOS -8.5 (fav covers 49%) | 210.7 / 210.5 (over 49%) | 96–123 / 87–115 | 5% | BOS: Jayson Tatum (day-to-day); Derrick White (day-to-day); Mitchell Robinson (day-to-day) (-0.5)<br>GSW: Moses Moody (out); Jimmy Butler III (out); Kristaps Porzingis (out); Stephen Curry (out); Brandon Williams (out) (-3.5) | no edge | no edge | no edge |

## Monday, November 23

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Spread: model / line | Total: model / line | 80% range | Overtime | Missing (effect on margin) | Spread edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 7:00 PM | MEM @ CHA | MEM 111, CHA 107 | MEM 62% | MEM -165 / CHA +165 | MEM -4 | 218.8 | 97–125 / 93–122 | 5% | MEM: Cameron Boozer (day-to-day); Javon Small (day-to-day); Jerami Grant (day-to-day); Scotty Pippen Jr. (out) (+1.3)<br>CHA: Grayson Allen (day-to-day); Dennis Schroder (out); Grant Williams (day-to-day); Kon Knueppel (out) (-0.4) | no line yet | no line yet | no line yet |
| 7:00 PM | POR @ PHI | POR 115, PHI 116 | PHI 52% | POR +110 / PHI -110 | PHI -0.5 | 230.2 | 100–129 / 101–130 | 5% | POR: Ja Morant (out); Chris Youngblood (out) (+0.6)<br>PHI: Jaylen Brown (day-to-day); Dean Wade (day-to-day); Adem Bona (out) (+0.2) | no line yet | no line yet | no line yet |
| 7:30 PM | OKC @ IND | OKC 116, IND 115 | OKC 52% | OKC -110 / IND +110 | OKC -0.5 | 231.1 | 101–131 / 101–130 | 5% | OKC: Shai Gilgeous-Alexander (day-to-day); Chet Holmgren (out); Jalen Williams (out); Cason Wallace (out); Alex Caruso (out); Jaylin Williams (out) (-2.9)<br>IND: Pascal Siakam (day-to-day); Tyrese Haliburton (out); Johnny Furphy (out); Ben Sheppard (out); T.J. McConnell (out) (-0.5) | no line yet | no line yet | no line yet |
| 7:30 PM | MIL @ TOR | MIL 109, TOR 116 | TOR 70% | MIL +235 / TOR -235 | TOR -7.1 | 224.6 | 94–124 / 102–130 | 4% | TOR: RJ Barrett (out); Kawhi Leonard (out); Collin Murray-Boyles (day-to-day) (-2.4) | no line yet | no line yet | no line yet |
| 7:30 PM | BKN @ MIN | BKN 106, MIN 119 | MIN 84% | BKN +520 / MIN -520 | MIN -13.6 | 224.6 | 91–120 / 105–133 | 3% | BKN: Nolan Traore (day-to-day) (+0.3)<br>MIN: Anthony Edwards (out); Donte DiVincenzo (out); Jaylen Clark (out) (-0.6) | no line yet | no line yet | no line yet |
| 8:00 PM | CLE @ CHI | CLE 122, CHI 118 | CLE 62% | CLE -160 / CHI +160 | CLE -4.1 | 240.7 | 108–137 / 103–134 | 5% | CLE: Evan Mobley (out); Jaylon Tyson (out) (-0.1)<br>CHI: Norman Powell (out); Jalen Smith (day-to-day); Caleb Wilson (out); Nic Claxton (day-to-day); Patrick Williams (day-to-day) (+0.0) | no line yet | no line yet | no line yet |
| 8:00 PM | PHX @ NOP | PHX 119, NOP 114 | PHX 63% | PHX -170 / NOP +170 | PHX -4.7 | 233.5 | 104–134 / 100–129 | 5% | PHX: Mark Williams (out); Ryan Dunn (day-to-day) (+0.5)<br>NOP: Zion Williamson (day-to-day); Trey Murphy III (day-to-day); Dejounte Murray (out); Trendon Watford (out); Bennedict Mathurin (out); Bryce McGowens (out) (+0.0) | no line yet | no line yet | no line yet |
| 8:30 PM | LAC @ HOU | LAC 108, HOU 119 | HOU 79% | LAC +370 / HOU -370 | HOU -10.8 | 226.7 | 93–123 / 105–133 | 4% | LAC: Brandon Ingram (out); Jordan Miller (out); Bradley Beal (out) (+0.3)<br>HOU: Clint Capela (out) (-0.1) | no line yet | no line yet | no line yet |
| 10:00 PM | UTA @ LAL | UTA 109, LAL 119 | LAL 77% | UTA +325 / LAL -325 | LAL -9.9 | 228.1 | 95–124 / 105–133 | 4% | UTA: Lauri Markkanen (out); Jaren Jackson Jr. (out); Jusuf Nurkic (out) (-2.3)<br>LAL: Austin Reaves (out) (-1.3) | no line yet | no line yet | no line yet |
| 10:00 PM | SAS @ SAC | SAS 118, SAC 105 | SAS 83% | SAS -500 / SAC +500 | SAS -13.1 | 222.7 | 104–132 / 90–120 | 4% | SAS: Dylan Harper (out); Tobias Harris (out) (+0.4)<br>SAC: Maxime Raynaud (out) (+0.7) | no line yet | no line yet | no line yet |

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
| 1 | SAS | +7.7 | +7.7 | +2.8 | +4.8 | 99.9 | +0.4 | 1718 |
| 2 | BOS | +7.2 | +6.9 | +2.7 | +4.4 | 96.7 | -0.5 | 1639 |
| 3 | HOU | +5.9 | +5.8 | +3.8 | +2.1 | 98.4 | -0.1 | 1613 |
| 4 | DET | +5.4 | +5.3 | +2.5 | +2.9 | 97.6 | +0.0 | 1640 |
| 5 | MIN | +5.1 | +5.3 | +0.7 | +4.4 | 103.5 | -0.6 | 1612 |
| 6 | DEN | +4.5 | +4.5 | +4.2 | +0.3 | 100.2 | +0.2 | 1582 |
| 7 | NYK | +4.0 | +3.7 | +0.4 | +3.6 | 92.4 | -1.8 | 1694 |
| 8 | LAL | +3.6 | +3.7 | +3.3 | +0.4 | 101.7 | -1.3 | 1604 |
| 9 | OKC | +3.2 | +3.2 | -0.3 | +3.5 | 102.2 | -2.9 | 1641 |
| 10 | POR | +2.9 | +3.0 | +1.5 | +1.4 | 102.4 | +0.6 | 1576 |
| 11 | PHI | +1.9 | +1.9 | +1.7 | +0.2 | 100.7 | +0.2 | 1583 |
| 12 | PHX | +0.6 | +0.6 | +1.1 | -0.5 | 100.4 | +0.5 | 1534 |
| 13 | ORL | +0.5 | +0.5 | -1.1 | +1.6 | 99.1 | +1.7 | 1521 |
| 14 | CLE | +0.4 | +0.4 | +1.8 | -1.5 | 101.8 | -0.1 | 1570 |
| 15 | MIA | +0.3 | +0.3 | +1.9 | -1.6 | 105.2 | -0.8 | 1548 |
| 16 | TOR | +0.2 | +0.2 | +0.1 | +0.2 | 97.3 | -2.3 | 1500 |
| 17 | MEM | -0.7 | -0.8 | +1.3 | -2.1 | 100.3 | +1.3 | 1487 |
| 18 | GSW | -1.0 | -1.0 | -0.9 | -0.1 | 99.9 | -3.5 | 1468 |
| 19 | UTA | -1.2 | -1.2 | -2.0 | +0.8 | 100.4 | -2.3 | 1346 |
| 20 | IND | -1.4 | -1.5 | -0.3 | -1.1 | 104.0 | -0.6 | 1362 |
| 21 | DAL | -1.7 | -1.7 | -1.0 | -0.7 | 100.9 | +1.3 | 1456 |
| 22 | ATL | -2.1 | -2.2 | -2.0 | -0.1 | 106.6 | +1.0 | 1549 |
| 23 | LAC | -3.4 | -3.5 | -1.4 | -2.1 | 101.1 | +0.3 | 1433 |
| 24 | CHI | -4.0 | -4.3 | -2.3 | -1.6 | 107.4 | +0.0 | 1399 |
| 25 | CHA | -5.2 | -5.0 | -4.7 | -0.5 | 95.3 | -0.4 | 1460 |
| 26 | WAS | -5.3 | -5.3 | -2.6 | -2.6 | 100.3 | +0.3 | 1325 |
| 27 | NOP | -5.4 | -5.5 | -1.6 | -3.8 | 102.9 | +0.0 | 1359 |
| 28 | BKN | -6.9 | -6.9 | -2.5 | -4.3 | 100.9 | +0.3 | 1308 |
| 29 | SAC | -7.6 | -7.7 | -4.2 | -3.4 | 101.1 | +0.7 | 1315 |
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
| 24 | Damian Lillard | POR | +1.9 | +1.8 | +0.1 | 32 |
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
