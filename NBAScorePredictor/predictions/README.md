# NBA score predictions

Updated Fri Nov 20, 2026 06:22 PM ET. Refreshed automatically several times a day during the season, around the injury report's deadlines; each game's prediction is locked at tip-off and graded once the final score is in.

Each team's expected points are its expected possessions times its expected points per possession, from team efficiency ratings and the ratings of the players expected to play, blended with the betting line. Each game is then simulated 10,000 times, overtime included. The predicted score is the expected points rounded; the 80% range holds 80% of simulated outcomes for each team. Basketball is the most predictable major sport, but a team's score still varies by about ±14 points around the forecast, so read the win chance and the ranges too.

Missing players come from the injury report: out players are left out, and doubtful, questionable and probable ones count with the share of their minutes their chance of playing implies, and their minutes go mostly to the bench. The effect is how many points of margin the team gains or loses against its full-strength roster: negative when it is missing good players, positive when the minutes go to better ones. Predictions are rerun when the report changes, up to tip-off.

The fair moneyline is the American odds that match the win chance exactly, with no bookmaker margin: -150 means risk $150 to win $100, +150 means risk $100 to win $150.

The edge columns check every side of the spread, the moneyline and the total for expected value: the profit per $1 bet at the posted price, using the final prediction's chances (the model blended with the line, simulated against the posted lines, pushes returning the stake, and anchored to the market's own chances so only what the blend moves off the line counts). The model's own spread and total are shown alongside, but the blend keeps only the share of that disagreement the model has earned in past seasons, so edges are rare. A side is an edge when its EV is 3% or more; the best such side is shown with its price, its EV, its chance of winning the bet and its stake, a 25% share of the Kelly stake in units of 1% of the bankroll, with at most 3 units on one game. Where a spread or total price is not posted it is assumed to be -110 (marked \*); a moneyline is never assumed. Edges are logged with each prediction, locked at tip-off and graded below. Treat them as an experiment, not betting advice; see the backtest for how they have done on past seasons.

## Friday, November 20

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Spread: model / line | Total: model / line | 80% range | Overtime | Missing (effect on margin) | Spread edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 7:00 PM | CHA @ ATL | CHA 106, ATL 113 | ATL 71% | CHA +250 / ATL -250<br>posted CHA +227 / ATL -277 | ATL -7.6 / ATL -7.5 (fav covers 51%) | 218.6 / 218.5 (over 50%) | 91–120 / 99–127 | 4% | CHA: Grayson Allen (out); Dennis Schroder (out); Grant Williams (out); Kon Knueppel (out) (-1.1)<br>ATL: CJ McCollum (out); Kingston Flemings (out); Jock Landale (out) (+2.3) | no edge | no edge | no edge |
| 7:30 PM | ORL @ BKN | ORL 115, BKN 109 | ORL 68% | ORL -215 / BKN +215<br>posted ORL -264 / BKN +217 | ORL -6.4 / ORL -6.5 (fav covers 51%) | 224.4 / 224.5 (over 49%) | 101–130 / 95–123 | 5% | ORL: Paolo Banchero (out) (+1.6) | no edge | no edge | no edge |
| 7:30 PM | IND @ CLE | IND 115, CLE 120 | CLE 65% | IND +180 / CLE -180<br>posted IND +180 / CLE -217 | CLE -5 / CLE -5.5 (fav covers 49%) | 234.8 / 234.5 (over 50%) | 100–130 / 105–134 | 5% | IND: Tyrese Haliburton (out); Johnny Furphy (out); Ben Sheppard (out); T.J. McConnell (day-to-day) (+0.2)<br>CLE: Evan Mobley (out); Jaylon Tyson (out); Peyton Watson (day-to-day) (-0.1) | no edge | no edge | no edge |
| 7:30 PM | TOR @ DET | TOR 105, DET 112 | DET 71% | TOR +240 / DET -240<br>posted TOR +217 / DET -264 | DET -7.1 / DET -6.5 (fav covers 53%) | 216.4 / 216.5 (over 49%) | 90–119 / 98–126 | 5% | TOR: RJ Barrett (out); Kawhi Leonard (out); Collin Murray-Boyles (out) (-2.5)<br>DET: Cade Cunningham (day-to-day); Duncan Robinson (out); Jalen Duren (out); Ronald Holland II (day-to-day) (+0.2) | no edge | no edge | no edge |
| 8:00 PM | WAS @ CHI | WAS 118, CHI 121 | CHI 58% | WAS +140 / CHI -140<br>posted WAS +114 / CHI -135 | CHI -2.7 / CHI -2.5 (fav covers 53%) | 238.6 / 238.5 (over 49%) | 103–133 / 106–135 | 6% | WAS: Jamir Watkins (out); Justin Champagnie (out); Tristan Vukcevic (out) (+0.1)<br>CHI: Jalen Smith (out); Caleb Wilson (out); Noa Essengue (day-to-day) (+0.4) | no edge | no edge | no edge |
| 8:00 PM | NOP @ OKC | NOP 108, OKC 119 | OKC 79% | NOP +385 / OKC -385<br>posted NOP +429 / OKC -574 | OKC -11 / OKC -11.5 (fav covers 47%) | 227.3 / 227.5 (over 49%) | 93–123 / 105–133 | 4% | NOP: Trey Murphy III (out); Dejounte Murray (out); Trendon Watford (out); Bennedict Mathurin (out); Bryce McGowens (out) (+0.1)<br>OKC: Chet Holmgren (out); Jalen Williams (out); Cason Wallace (out); Alex Caruso (day-to-day) (-0.5) | no edge | no edge | no edge |
| 9:30 PM | PHX @ UTA | PHX 115, UTA 111 | PHX 62% | PHX -160 / UTA +160<br>posted PHX -184 / UTA +154 | PHX -4.1 / PHX -4.5 (fav covers 50%) | 225.7 / 225.5 (over 49%) | 101–129 / 96–125 | 6% | PHX: Mark Williams (out) (+0.5)<br>UTA: Lauri Markkanen (out); Jaren Jackson Jr. (out); Jusuf Nurkic (out) (-2.3) | no edge | no edge | no edge |
| 10:00 PM | HOU @ DEN | HOU 113, DEN 114 | DEN 53% | HOU +115 / DEN -115<br>posted HOU +105 / DEN -125 | DEN -1.2 / DEN -1.5 (fav covers 51%) | 227.7 / 227.5 (over 49%) | 99–128 / 100–129 | 5% | HOU: Alperen Sengun (day-to-day); Clint Capela (out); Steven Adams (day-to-day) (-0.3) | no edge | no edge | no edge |
| 10:00 PM | SAC @ LAL | SAC 107, LAL 122 | LAL 85% | SAC +580 / LAL -580<br>posted SAC +600 / LAL -890 | LAL -14.3 / LAL -14.5 (fav covers 48%) | 229.2 / 229.5 (over 48%) | 93–122 / 107–136 | 3% | SAC: De'Andre Hunter (day-to-day); Maxime Raynaud (out); Precious Achiuwa (out) (+0.2)<br>LAL: Austin Reaves (out) (-1.2) | no edge | no edge | no edge |

## Saturday, November 21

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Spread: model / line | Total: model / line | 80% range | Overtime | Missing (effect on margin) | Spread edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1:00 PM | MIL @ PHI | MIL 110, PHI 121 | PHI 80% | MIL +405 / PHI -405 | PHI -11.4 | 231.1 | 95–125 / 107–135 | 4% | PHI: Tyrese Maxey (day-to-day); Jaylen Brown (out); Dean Wade (out); Adem Bona (out); Dominick Barlow (out) (-0.9) | no line yet | no line yet | no line yet |
| 7:30 PM | POR @ NYK | POR 107, NYK 110 | NYK 61% | POR +160 / NYK -160 | NYK -3.6 | 216.9 | 93–121 / 96–124 | 5% | POR: Deni Avdija (day-to-day); Ja Morant (out); Chris Youngblood (out) (+0.2)<br>NYK: OG Anunoby (day-to-day) (-0.3) | no line yet | no line yet | no line yet |
| 8:00 PM | LAC @ DAL | LAC 113, DAL 117 | DAL 62% | LAC +160 / DAL -160 | DAL -4 | 230.7 | 99–128 / 103–132 | 5% | LAC: Brandon Ingram (out); Jordan Miller (out); Bradley Beal (out) (+0.4)<br>DAL: P.J. Washington (day-to-day); Walter Clayton Jr. (day-to-day); Dereck Lively II (out); Sergio de Larrea (out) (+1.0) | no line yet | no line yet | no line yet |
| 8:00 PM | MEM @ MIN | MEM 111, MIN 118 | MIN 72% | MEM +260 / MIN -260 | MIN -7.8 | 229.1 | 96–125 / 104–133 | 4% | MEM: Ty Jerome (out); Zach Edey (day-to-day); Jerami Grant (day-to-day); Scotty Pippen Jr. (out) (-1.0)<br>MIN: Anthony Edwards (out); Donte DiVincenzo (out); Jaylen Clark (out) (-0.7) | no line yet | no line yet | no line yet |
| 8:00 PM | NOP @ SAS | NOP 105, SAS 123 | SAS 90% | NOP +900 / SAS -900 | SAS -17.6 | 227.5 | 90–120 / 108–137 | 2% | NOP: Trey Murphy III (out); Dejounte Murray (out); Trendon Watford (out); Bennedict Mathurin (out); Bryce McGowens (out) (+0.1)<br>SAS: Dylan Harper (out); Tobias Harris (out) (+0.3) | no line yet | no line yet | no line yet |
| 10:00 PM | BOS @ SAC | BOS 119, SAC 103 | BOS 88% | BOS -760 / SAC +760 | BOS -15.9 | 221.5 | 105–133 / 88–117 | 3% | SAC: De'Andre Hunter (day-to-day); Maxime Raynaud (out); Precious Achiuwa (out) (+0.2) | no line yet | no line yet | no line yet |

## How the 2026-27 predictions have done

| Predictor | Games | Margin MAE | Total MAE | Team-points MAE | Log loss | Brier | Winners | 80% range hit |
|---|---|---|---|---|---|---|---|---|
| Final prediction | 226 | 11.28 | 13.97 | 9.24 | 0.572 | 0.195 | 70.4% | 81.4% |
| Model only (before blending) | 226 | 11.51 | 13.83 | 9.28 | 0.585 | 0.201 | 69.5% | – |
| Elo | 226 | 11.88 | – | – | 0.615 | 0.213 | 64.6% | – |
| Final prediction, games with a line | 226 | 11.28 | 13.97 | 9.24 | 0.572 | 0.195 | 70.4% | 81.4% |
| Model only, games with a line | 226 | 11.51 | 13.83 | 9.28 | 0.585 | 0.201 | 69.5% | – |
| Betting line | 226 | 11.26 | 13.97 | 9.24 | 0.568 | 0.193 | 70.4% | – |

MAE is the average miss in points; team-points MAE is the average miss on each team's score. Log loss and Brier score the win chances (lower is better; a coin flip scores 0.693 and 0.250). The closing line misses margins by about 10 points and totals by about 14.

Overtime: predicted in 4.7% of games, happened in 5.3%.

### Betting edges

| Market | Edges | Record (W-L-P) | Staked | Units won | ROI | Expected ROI |
|---|---|---|---|---|---|---|
| Spread | 1 | 1-0-0 | 1.0 | +0.90 | +89.3% | +3.6% |
| Moneyline | 15 | 2-13-0 | 5.6 | -2.59 | -46.2% | +6.5% |
| Total | 0 | 0-0-0 | 0.0 | +0.00 | – | – |

Spread moved toward the model's first spread edge before tip-off: 5 of 6 games (83%).

Live predictions only, each edge at the stake and price logged with the last prediction before tip-off (edges logged before edges were priced from the final prediction are left out); a push returns the stake. Units are 1% of the bankroll; ROI is units won per unit staked, and expected ROI is what the edges' EVs promised. The line moving toward the model's edge before tip-off is the quickest sign that it knows something the market doesn't yet.

### Results, Thursday, November 19

| Game | Predicted | Final | Win chance for winner | Spread: model / line | Inside 80% ranges |
|---|---|---|---|---|---|
| GSW @ MEM | 110–115 | 98–126 | 65% | MEM -5.2 / MEM -5.5 | yes |
| POR @ MIL | 121–110 | 124–114 | 79% | POR -11.3 / POR -11.5 | yes |
| NYK @ MIN | 109–108 | 102–99 | 53% | NYK -1 / NYK -1.5 | yes |
| LAC @ SAS | 104–120 | 112–124 | 87% | SAS -15.3 / SAS -15.5 | yes |

## Power ratings

Points per 100 possessions better than an average team on a neutral floor, combining opponent-adjusted team efficiency (garbage time removed) with the ratings of the team's healthy roster, through the fitted points map. Net per game uses the team's pace. Injury effect now is what its current injury report does to its margin, in points.

| # | Team | Net per 100 | Net per game | Offense | Defense | Pace | Injury effect now | Elo |
|---|---|---|---|---|---|---|---|---|
| 1 | SAS | +8.0 | +8.0 | +3.0 | +5.0 | 99.6 | +0.3 | 1716 |
| 2 | BOS | +7.5 | +7.3 | +3.4 | +4.2 | 96.3 | +0.0 | 1648 |
| 3 | HOU | +5.9 | +5.7 | +3.4 | +2.4 | 97.4 | -0.3 | 1622 |
| 4 | DET | +5.7 | +5.6 | +2.4 | +3.2 | 99.1 | +0.3 | 1651 |
| 5 | MIN | +4.8 | +5.0 | +0.8 | +4.0 | 104.0 | -0.7 | 1608 |
| 6 | NYK | +4.7 | +4.3 | +1.0 | +3.7 | 93.2 | -0.3 | 1693 |
| 7 | LAL | +4.1 | +4.2 | +3.5 | +0.5 | 102.3 | -1.2 | 1603 |
| 8 | DEN | +4.1 | +4.0 | +3.5 | +0.5 | 99.1 | +0.2 | 1573 |
| 9 | OKC | +2.9 | +3.0 | -0.7 | +3.6 | 101.8 | -0.5 | 1640 |
| 10 | POR | +2.4 | +2.5 | +1.2 | +1.2 | 103.4 | +0.2 | 1578 |
| 11 | PHI | +2.1 | +2.1 | +1.3 | +0.7 | 100.6 | -0.9 | 1582 |
| 12 | PHX | +0.5 | +0.5 | +1.0 | -0.5 | 101.2 | +0.5 | 1527 |
| 13 | MIA | +0.4 | +0.5 | +1.9 | -1.5 | 105.2 | +0.1 | 1548 |
| 14 | CLE | +0.4 | +0.4 | +1.8 | -1.4 | 100.8 | -0.1 | 1567 |
| 15 | ORL | +0.4 | +0.4 | -1.2 | +1.6 | 99.2 | +1.6 | 1519 |
| 16 | TOR | -0.1 | -0.1 | -0.3 | +0.3 | 98.5 | -2.5 | 1489 |
| 17 | MEM | -0.4 | -0.4 | +1.8 | -2.2 | 101.1 | -1.0 | 1491 |
| 18 | GSW | -0.9 | -0.9 | -0.9 | +0.0 | 99.7 | -3.7 | 1468 |
| 19 | UTA | -1.1 | -1.1 | -1.9 | +0.8 | 100.9 | -2.3 | 1353 |
| 20 | IND | -1.4 | -1.4 | -0.4 | -1.0 | 103.2 | +0.2 | 1364 |
| 21 | DAL | -1.7 | -1.7 | -1.0 | -0.6 | 102.3 | +1.0 | 1448 |
| 22 | ATL | -2.1 | -2.2 | -2.0 | +0.0 | 107.6 | +2.4 | 1542 |
| 23 | LAC | -3.1 | -3.2 | -1.1 | -2.0 | 102.2 | +0.4 | 1441 |
| 24 | CHI | -3.7 | -4.0 | -1.6 | -2.1 | 108.3 | +0.5 | 1409 |
| 25 | NOP | -5.0 | -5.1 | -1.5 | -3.4 | 103.0 | +0.1 | 1363 |
| 26 | CHA | -5.0 | -4.8 | -4.6 | -0.4 | 95.9 | -1.1 | 1467 |
| 27 | WAS | -5.5 | -5.5 | -2.4 | -3.1 | 100.7 | +0.1 | 1315 |
| 28 | BKN | -7.2 | -7.2 | -2.9 | -4.3 | 100.8 | +0.1 | 1310 |
| 29 | MIL | -8.1 | -8.4 | -3.5 | -4.6 | 102.8 | +0.2 | 1309 |
| 30 | SAC | -8.7 | -8.9 | -4.1 | -4.6 | 101.7 | +0.2 | 1307 |

## Top players

Regularized adjusted plus-minus from every lineup this season and past ones: points per 100 possessions a player adds on offense and saves on defense, against an average player, shrunk toward last season's rating. Players expected to play 20 minutes or more.

| # | Player | Team | Net impact per 100 | Offense | Defense | Expected minutes |
|---|---|---|---|---|---|---|
| 1 | Victor Wembanyama | SAS | +8.1 | +2.4 | +5.7 | 32 |
| 2 | Shai Gilgeous-Alexander | OKC | +5.9 | +5.1 | +0.7 | 34 |
| 3 | Nikola Jokic | DEN | +5.1 | +4.5 | +0.5 | 38 |
| 4 | Kawhi Leonard | TOR | +4.6 | +3.6 | +0.9 | 30 |
| 5 | Giannis Antetokounmpo | MIA | +4.4 | +4.3 | +0.1 | 31 |
| 6 | Luka Doncic | LAL | +4.0 | +5.0 | -1.0 | 38 |
| 7 | Kyrie Irving | DAL | +3.7 | +3.6 | +0.1 | 32 |
| 8 | Joel Embiid | PHI | +2.9 | +1.7 | +1.2 | 32 |
| 9 | Neemias Queta | BOS | +2.8 | +1.1 | +1.8 | 24 |
| 10 | Franz Wagner | ORL | +2.5 | +1.5 | +1.0 | 37 |
| 11 | Derrick White | BOS | +2.5 | +0.5 | +2.0 | 31 |
| 12 | Donovan Mitchell | CLE | +2.4 | +3.3 | -0.9 | 34 |
| 13 | Javonte Green | DET | +2.3 | +0.2 | +2.1 | 24 |
| 14 | Jimmy Butler III | GSW | +2.2 | +2.1 | +0.1 | 27 |
| 15 | Ausar Thompson | DET | +2.2 | +0.1 | +2.1 | 30 |
| 16 | Paul Reed | DET | +2.1 | +0.7 | +1.4 | 24 |
| 17 | Chet Holmgren | OKC | +2.1 | +0.0 | +2.1 | 30 |
| 18 | Bam Adebayo | MIA | +2.1 | +1.4 | +0.6 | 29 |
| 19 | Dyson Daniels | ATL | +2.0 | +0.2 | +1.9 | 33 |
| 20 | Jarrett Allen | CLE | +2.0 | +1.9 | +0.1 | 29 |
| 21 | Herbert Jones | NOP | +2.0 | -1.0 | +3.0 | 28 |
| 22 | Fred VanVleet | HOU | +2.0 | +1.4 | +0.5 | 29 |
| 23 | Jrue Holiday | POR | +1.9 | +1.2 | +0.8 | 29 |
| 24 | Pascal Siakam | IND | +1.9 | +1.5 | +0.4 | 33 |
| 25 | LaMelo Ball | MIN | +1.8 | +3.3 | -1.5 | 31 |
| 26 | Damian Lillard | POR | +1.7 | +1.7 | +0.0 | 31 |
| 27 | Dean Wade | PHI | +1.7 | +0.9 | +0.7 | 30 |
| 28 | Karl-Anthony Towns | NYK | +1.6 | +1.6 | +0.0 | 35 |
| 29 | Cade Cunningham | DET | +1.6 | +1.8 | -0.2 | 38 |
| 30 | Ty Jerome | MEM | +1.6 | +2.6 | -1.0 | 30 |

## Current model fit

- Fitted on 5508 games from 2022-23 to 2026-27.
- Home court: +2.0 points per 100 possessions for the home team over the visitor (about 2.0 points a game).
- Second night of a back-to-back: -0.7 points per 100 scored, +1.2 allowed.
- Weights: team efficiency ratings 0.14 (offense) and 0.15 (defense); player lineup ratings 0.77 and 0.76.
- Blend: 82% on the betting line for the margin and 100% for the total, wherever there is a line (fitted on past closing lines).
- Simulator: each team's points vary by 10.9 with correlation 0.23; 5.2% of recent games went to overtime.
