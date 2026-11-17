# NBA score predictions

Updated Tue Nov 17, 2026 06:58 PM ET. Refreshed automatically several times a day during the season, around the injury report's deadlines; each game's prediction is locked at tip-off and graded once the final score is in.

Each team's expected points are its expected possessions times its expected points per possession, from team efficiency ratings and the ratings of the players expected to play, blended with the betting line. Each game is then simulated 10,000 times, overtime included. The predicted score is the expected points rounded; the 80% range holds 80% of simulated outcomes for each team. Basketball is the most predictable major sport, but a team's score still varies by about ±14 points around the forecast, so read the win chance and the ranges too.

Missing players come from the injury report: out players are left out, and doubtful, questionable and probable ones count with the share of their minutes their chance of playing implies, and their minutes go mostly to the bench. The effect is how many points of margin the team gains or loses against its full-strength roster: negative when it is missing good players, positive when the minutes go to better ones. Predictions are rerun when the report changes, up to tip-off.

The fair moneyline is the American odds that match the win chance exactly, with no bookmaker margin: -150 means risk $150 to win $100, +150 means risk $100 to win $150.

The edge columns check every side of the spread, the moneyline and the total for expected value: the profit per $1 bet at the posted price, using the final prediction's chances (the model blended with the line, simulated against the posted lines, pushes returning the stake, and anchored to the market's own chances so only what the blend moves off the line counts). The model's own spread and total are shown alongside, but the blend keeps only the share of that disagreement the model has earned in past seasons, so edges are rare. A side is an edge when its EV is 3% or more; the best such side is shown with its price, its EV, its chance of winning the bet and its stake, a 25% share of the Kelly stake in units of 1% of the bankroll, with at most 3 units on one game. Where a spread or total price is not posted it is assumed to be -110 (marked \*); a moneyline is never assumed. Edges are logged with each prediction, locked at tip-off and graded below. Treat them as an experiment, not betting advice; see the backtest for how they have done on past seasons.

## Tuesday, November 17

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Spread: model / line | Total: model / line | 80% range | Overtime | Missing (effect on margin) | Spread edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 7:30 PM | NYK @ TOR | NYK 109, TOR 107 | NYK 58% | NYK -140 / TOR +140<br>posted NYK -142 / TOR +120 | NYK -2.7 / NYK -2.5 (fav covers 53%) | 215.9 / 215.5 (over 50%) | 95–123 / 93–121 | 6% | TOR: Kawhi Leonard (out) (-1.8) | no edge | no edge | no edge |
| 8:00 PM | POR @ MIN | POR 113, MIN 115 | MIN 58% | POR +135 / MIN -135<br>posted POR +114 / MIN -135 | MIN -2.5 / MIN -2.5 (fav covers 51%) | 227.8 / 227.5 (over 50%) | 98–127 / 101–129 | 6% | POR: Deni Avdija (day-to-day); Ja Morant (out); Chris Youngblood (out) (+0.1)<br>MIN: Anthony Edwards (out); Jonathan Kuminga (out); Donte DiVincenzo (out); Jaylen Clark (out) (-1.7) | no edge | no edge | no edge |
| 8:00 PM | DET @ SAS | DET 106, SAS 115 | SAS 75% | DET +295 / SAS -295<br>posted DET +340 / SAS -437 | SAS -8.7 / SAS -9.5 (fav covers 47%) | 221.5 / 221.5 (over 49%) | 92–121 / 101–129 | 4% | DET: Duncan Robinson (out); Jalen Duren (out); Ronald Holland II (out) (+0.0)<br>SAS: Tobias Harris (out) (+0.8) | no edge | no edge | no edge |
| 10:30 PM | UTA @ LAC | UTA 110, LAC 116 | LAC 68% | UTA +210 / LAC -210<br>posted UTA +190 / LAC -229 | LAC -6.2 / LAC -6.5 (fav covers 50%) | 226.5 / 226.5 (over 49%) | 95–125 / 102–131 | 5% | UTA: Lauri Markkanen (out); Jaren Jackson Jr. (out); Jaxson Hayes (out); Jusuf Nurkic (out) (-2.8)<br>LAC: Brandon Ingram (out); Jordan Miller (out); Bradley Beal (out); Yanic Konan Niederhauser (out) (+0.7) | no edge | no edge | no edge |
| 11:00 PM | CHA @ LAL | CHA 108, LAL 116 | LAL 73% | CHA +265 / LAL -265<br>posted CHA +243 / LAL -299 | LAL -8.1 / LAL -7.5 (fav covers 53%) | 223.4 / 223.5 (over 49%) | 93–122 / 102–130 | 4% | CHA: Dennis Schroder (out); Kon Knueppel (out) (-0.4)<br>LAL: Austin Reaves (out); Walker Kessler (out) (-2.5) | no edge | no edge | no edge |

## Wednesday, November 18

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Spread: model / line | Total: model / line | 80% range | Overtime | Missing (effect on margin) | Spread edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 7:00 PM | MEM @ CLE | MEM 117, CLE 121 | CLE 60% | MEM +150 / CLE -150 | CLE -3.4 | 238.1 | 103–132 / 106–135 | 6% | MEM: Ty Jerome (out); Isaiah Stewart (out); Scotty Pippen Jr. (out) (-1.2)<br>CLE: Evan Mobley (out); Jaylon Tyson (day-to-day); Peyton Watson (day-to-day); Sam Merrill (out) (-0.9) | no line yet | no line yet | no line yet |
| 7:00 PM | HOU @ IND | HOU 116, IND 111 | HOU 63% | HOU -170 / IND +170 | HOU -4.3 | 226.9 | 101–130 / 97–126 | 5% | HOU: Amen Thompson (day-to-day); Clint Capela (out) (-0.3)<br>IND: Andrew Nembhard (day-to-day); Tyrese Haliburton (out); Johnny Furphy (out); Ben Sheppard (out); T.J. McConnell (day-to-day) (+0.2) | no line yet | no line yet | no line yet |
| 7:00 PM | MIL @ MIA | MIL 112, MIA 122 | MIA 77% | MIL +340 / MIA -340 | MIA -10.5 | 233.6 | 97–126 / 108–136 | 4% | MIA: Bam Adebayo (day-to-day); Myron Gardner (day-to-day) (-0.4) | no line yet | no line yet | no line yet |
| 7:00 PM | PHI @ ORL | PHI 111, ORL 112 | ORL 51% | PHI +105 / ORL -105 | pick'em | 222.8 | 97–126 / 97–126 | 5% | PHI: Jaylen Brown (out); Adem Bona (out); Dominick Barlow (out) (+1.1)<br>ORL: Paolo Banchero (out) (+1.5) | no line yet | no line yet | no line yet |
| 7:30 PM | CHI @ BKN | CHI 118, BKN 120 | BKN 55% | CHI +120 / BKN -120<br>posted CHI +128 / BKN -152 | BKN -1.7 / BKN -2.5 (fav covers 49%) | 237.9 / 237.5 (over 50%) | 103–133 / 105–134 | 6% | CHI: Caleb Wilson (out); Patrick Williams (day-to-day) (+1.7) | no edge | no edge | no edge |
| 7:30 PM | WAS @ TOR | WAS 111, TOR 115 | TOR 63% | WAS +175 / TOR -175 | TOR -4.4 | 226.4 | 96–126 / 101–130 | 5% | WAS: Jamir Watkins (out); Justin Champagnie (out); Tristan Vukcevic (out) (+0.0)<br>TOR: Kawhi Leonard (out) (-1.9) | no line yet | no line yet | no line yet |
| 8:00 PM | DET @ NOP | DET 118, NOP 112 | DET 68% | DET -215 / NOP +215 | DET -6.5 | 229.6 | 104–133 / 97–127 | 5% | DET: Duncan Robinson (out); Jalen Duren (out); Ronald Holland II (out) (+0.0)<br>NOP: Trey Murphy III (out); Dejounte Murray (out); Trendon Watford (out); Bennedict Mathurin (out); Bryce McGowens (out) (+0.0) | no line yet | no line yet | no line yet |
| 8:00 PM | ATL @ OKC | ATL 112, OKC 118 | OKC 67% | ATL +205 / OKC -205 | OKC -6 | 230.8 | 98–127 / 104–133 | 5% | ATL: CJ McCollum (out); Kingston Flemings (out); Jock Landale (out) (+2.0)<br>OKC: Chet Holmgren (out); Jalen Williams (out); Jaylin Williams (out); Cason Wallace (out) (-0.3) | no line yet | no line yet | no line yet |
| 8:00 PM | GSW @ DAL | GSW 111, DAL 114 | DAL 60% | GSW +150 / DAL -150 | DAL -3.4 | 225.5 | 97–126 / 100–129 | 5% | GSW: Moses Moody (out); Jimmy Butler III (out); Kristaps Porzingis (out); Stephen Curry (out); Al Horford (day-to-day); Brandon Williams (out) (-3.3)<br>DAL: Walter Clayton Jr. (day-to-day); Dereck Lively II (out); Santi Aldama (day-to-day); Sergio de Larrea (out) (+0.9) | no line yet | no line yet | no line yet |
| 9:30 PM | BOS @ DEN | BOS 111, DEN 109 | BOS 56% | BOS -130 / DEN +130 | BOS -2 | 220.2 | 97–126 / 95–124 | 5% | – | no line yet | no line yet | no line yet |
| 10:00 PM | UTA @ LAL | UTA 111, LAL 122 | LAL 78% | UTA +360 / LAL -360 | LAL -10.7 | 232.6 | 96–126 / 107–136 | 4% | UTA: Lauri Markkanen (out); Jaren Jackson Jr. (out); Jaxson Hayes (out); Jusuf Nurkic (out) (-2.9)<br>LAL: Austin Reaves (out); Walker Kessler (out) (-2.6) | no line yet | no line yet | no line yet |
| 10:00 PM | PHX @ SAC | PHX 119, SAC 112 | PHX 69% | PHX -220 / SAC +220 | PHX -6.7 | 230.7 | 104–133 / 97–127 | 4% | PHX: Mark Williams (out) (+0.5)<br>SAC: De'Andre Hunter (day-to-day); Maxime Raynaud (out); Zach LaVine (day-to-day); Precious Achiuwa (day-to-day) (+0.4) | no line yet | no line yet | no line yet |

## How the 2026-27 predictions have done

| Predictor | Games | Margin MAE | Total MAE | Team-points MAE | Log loss | Brier | Winners | 80% range hit |
|---|---|---|---|---|---|---|---|---|
| Final prediction | 205 | 11.27 | 14.18 | 9.34 | 0.561 | 0.190 | 71.7% | 81.0% |
| Model only (before blending) | 205 | 11.53 | 13.98 | 9.36 | 0.577 | 0.197 | 70.7% | – |
| Elo | 205 | 11.85 | – | – | 0.596 | 0.206 | 65.9% | – |
| Final prediction, games with a line | 205 | 11.27 | 14.18 | 9.34 | 0.561 | 0.190 | 71.7% | 81.0% |
| Model only, games with a line | 205 | 11.53 | 13.98 | 9.36 | 0.577 | 0.197 | 70.7% | – |
| Betting line | 205 | 11.25 | 14.19 | 9.34 | 0.555 | 0.188 | 71.7% | – |

MAE is the average miss in points; team-points MAE is the average miss on each team's score. Log loss and Brier score the win chances (lower is better; a coin flip scores 0.693 and 0.250). The closing line misses margins by about 10 points and totals by about 14.

Overtime: predicted in 4.6% of games, happened in 5.4%.

### Betting edges

| Market | Edges | Record (W-L-P) | Staked | Units won | ROI | Expected ROI |
|---|---|---|---|---|---|---|
| Spread | 1 | 1-0-0 | 1.0 | +0.90 | +89.3% | +3.6% |
| Moneyline | 15 | 2-13-0 | 5.6 | -2.59 | -46.2% | +6.5% |
| Total | 0 | 0-0-0 | 0.0 | +0.00 | – | – |

Spread moved toward the model's first spread edge before tip-off: 5 of 6 games (83%).

Live predictions only, each edge at the stake and price logged with the last prediction before tip-off (edges logged before edges were priced from the final prediction are left out); a push returns the stake. Units are 1% of the bankroll; ROI is units won per unit staked, and expected ROI is what the edges' EVs promised. The line moving toward the model's edge before tip-off is the quickest sign that it knows something the market doesn't yet.

### Results, Monday, November 16

| Game | Predicted | Final | Win chance for winner | Spread: model / line | Inside 80% ranges |
|---|---|---|---|---|---|
| ORL @ BOS | 102–111 | 115–105 | 26% | BOS -8.4 / BOS -8.5 | yes |
| CHI @ CLE | 117–125 | 115–126 | 71% | CLE -7.8 / CLE -8.5 | yes |
| MEM @ WAS | 118–115 | 136–120 | 60% | MEM -3.6 / MEM -3.5 | no |
| PHI @ BKN | 115–111 | 135–123 | 62% | PHI -4.3 / PHI -4.5 | no |
| HOU @ MIA | 117–115 | 110–128 | 43% | HOU -2.2 / HOU -2.5 | yes |
| POR @ MIN | 113–115 | 98–106 | 56% | MIN -2.3 / MIN -2.5 | yes |
| GSW @ NOP | 113–110 | 94–115 | 41% | GSW -3.3 / GSW -3.5 | no |
| PHX @ DEN | 110–119 | 117–105 | 24% | DEN -9.3 / DEN -9.5 | yes |

## Power ratings

Points per 100 possessions better than an average team on a neutral floor, combining opponent-adjusted team efficiency (garbage time removed) with the ratings of the team's healthy roster, through the fitted points map. Net per game uses the team's pace. Injury effect now is what its current injury report does to its margin, in points.

| # | Team | Net per 100 | Net per game | Offense | Defense | Pace | Injury effect now | Elo |
|---|---|---|---|---|---|---|---|---|
| 1 | SAS | +8.0 | +7.9 | +3.3 | +4.7 | 99.0 | +0.8 | 1734 |
| 2 | BOS | +7.8 | +7.4 | +4.1 | +3.7 | 95.1 | +0.0 | 1654 |
| 3 | HOU | +5.6 | +5.5 | +3.2 | +2.4 | 97.9 | -0.2 | 1615 |
| 4 | LAL | +5.4 | +5.5 | +4.5 | +0.8 | 103.0 | -2.6 | 1631 |
| 5 | DET | +5.4 | +5.4 | +2.4 | +2.9 | 101.0 | +0.0 | 1626 |
| 6 | MIN | +4.7 | +4.9 | +1.2 | +3.5 | 103.7 | -1.7 | 1611 |
| 7 | NYK | +4.1 | +3.9 | +0.9 | +3.2 | 94.4 | +0.0 | 1681 |
| 8 | DEN | +3.4 | +3.4 | +3.7 | -0.3 | 97.7 | +0.2 | 1566 |
| 9 | OKC | +3.4 | +3.5 | -0.5 | +3.9 | 101.9 | -0.3 | 1652 |
| 10 | POR | +2.8 | +2.9 | +1.9 | +0.9 | 102.1 | +0.1 | 1576 |
| 11 | PHI | +2.4 | +2.4 | +1.1 | +1.3 | 101.3 | +1.1 | 1575 |
| 12 | CLE | +0.5 | +0.5 | +1.7 | -1.3 | 101.5 | -0.9 | 1577 |
| 13 | GSW | +0.4 | +0.4 | +0.0 | +0.5 | 100.2 | -3.3 | 1502 |
| 14 | MIA | +0.4 | +0.4 | +1.7 | -1.3 | 104.0 | -0.4 | 1546 |
| 15 | TOR | +0.4 | +0.4 | -0.4 | +0.8 | 101.1 | -1.9 | 1508 |
| 16 | PHX | +0.4 | +0.4 | +0.7 | -0.4 | 102.1 | +0.5 | 1517 |
| 17 | ORL | +0.1 | +0.1 | -1.8 | +1.9 | 100.4 | +1.5 | 1526 |
| 18 | MEM | -0.7 | -0.7 | +1.4 | -2.0 | 102.6 | -1.2 | 1465 |
| 19 | IND | -1.0 | -1.0 | -0.2 | -0.8 | 103.4 | +0.2 | 1371 |
| 20 | DAL | -2.2 | -2.2 | -1.1 | -1.1 | 102.2 | +1.0 | 1431 |
| 21 | ATL | -2.3 | -2.5 | -2.1 | -0.3 | 107.6 | +2.1 | 1530 |
| 22 | UTA | -2.8 | -2.8 | -2.8 | -0.1 | 100.9 | -2.8 | 1282 |
| 23 | LAC | -2.9 | -2.9 | -1.2 | -1.7 | 101.1 | +0.7 | 1484 |
| 24 | CHI | -4.6 | -5.0 | -2.3 | -2.3 | 109.3 | +1.8 | 1386 |
| 25 | NOP | -5.2 | -5.4 | -1.9 | -3.3 | 103.8 | +0.0 | 1368 |
| 26 | CHA | -5.6 | -5.5 | -5.1 | -0.5 | 96.7 | -0.3 | 1469 |
| 27 | BKN | -5.6 | -5.7 | -2.3 | -3.4 | 101.2 | +0.0 | 1334 |
| 28 | WAS | -5.9 | -5.9 | -2.5 | -3.4 | 100.9 | +0.0 | 1302 |
| 29 | SAC | -8.2 | -8.4 | -4.1 | -4.1 | 102.4 | +0.4 | 1317 |
| 30 | MIL | -8.2 | -8.3 | -3.8 | -4.4 | 100.9 | +0.2 | 1315 |

## Top players

Regularized adjusted plus-minus from every lineup this season and past ones: points per 100 possessions a player adds on offense and saves on defense, against an average player, shrunk toward last season's rating. Players expected to play 20 minutes or more.

| # | Player | Team | Net impact per 100 | Offense | Defense | Expected minutes |
|---|---|---|---|---|---|---|
| 1 | Victor Wembanyama | SAS | +8.3 | +2.7 | +5.6 | 29 |
| 2 | Shai Gilgeous-Alexander | OKC | +5.8 | +5.2 | +0.6 | 33 |
| 3 | Alex Caruso | OKC | +5.4 | +0.4 | +5.1 | 22 |
| 4 | Nikola Jokic | DEN | +4.9 | +4.7 | +0.2 | 37 |
| 5 | Luka Doncic | LAL | +4.7 | +5.3 | -0.6 | 36 |
| 6 | Kawhi Leonard | TOR | +4.6 | +3.6 | +0.9 | 30 |
| 7 | Giannis Antetokounmpo | MIA | +4.4 | +4.2 | +0.2 | 31 |
| 8 | Kyrie Irving | DAL | +3.5 | +3.6 | -0.1 | 33 |
| 9 | Neemias Queta | BOS | +2.9 | +1.3 | +1.7 | 21 |
| 10 | Joel Embiid | PHI | +2.9 | +1.5 | +1.3 | 30 |
| 11 | Franz Wagner | ORL | +2.8 | +1.6 | +1.2 | 38 |
| 12 | Donovan Mitchell | CLE | +2.5 | +3.4 | -0.9 | 34 |
| 13 | LaMelo Ball | MIN | +2.3 | +3.8 | -1.5 | 27 |
| 14 | Derrick White | BOS | +2.3 | +0.6 | +1.7 | 29 |
| 15 | Jimmy Butler III | GSW | +2.2 | +2.1 | +0.1 | 27 |
| 16 | Jarrett Allen | CLE | +2.2 | +1.8 | +0.4 | 28 |
| 17 | Chet Holmgren | OKC | +2.1 | +0.0 | +2.1 | 30 |
| 18 | Fred VanVleet | HOU | +2.1 | +1.4 | +0.7 | 30 |
| 19 | Ausar Thompson | DET | +2.0 | +0.1 | +1.9 | 28 |
| 20 | Bam Adebayo | MIA | +2.0 | +1.6 | +0.4 | 29 |
| 21 | Herbert Jones | NOP | +1.9 | -1.1 | +3.0 | 26 |
| 22 | Dyson Daniels | ATL | +1.9 | +0.1 | +1.8 | 31 |
| 23 | De'Aaron Fox | SAS | +1.8 | +1.7 | +0.1 | 24 |
| 24 | Dean Wade | PHI | +1.7 | +1.1 | +0.7 | 30 |
| 25 | Pascal Siakam | IND | +1.7 | +1.5 | +0.2 | 33 |
| 26 | Ty Jerome | MEM | +1.7 | +2.7 | -1.0 | 30 |
| 27 | Day'Ron Sharpe | BKN | +1.7 | +0.8 | +0.9 | 25 |
| 28 | Paul Reed | DET | +1.7 | +0.4 | +1.3 | 27 |
| 29 | Rudy Gobert | MIN | +1.7 | -3.6 | +5.2 | 29 |
| 30 | Paul George | BOS | +1.6 | +0.8 | +0.8 | 31 |

## Current model fit

- Fitted on 5487 games from 2022-23 to 2026-27.
- Home court: +2.0 points per 100 possessions for the home team over the visitor (about 2.0 points a game).
- Second night of a back-to-back: -0.7 points per 100 scored, +1.2 allowed.
- Weights: team efficiency ratings 0.15 (offense) and 0.15 (defense); player lineup ratings 0.77 and 0.76.
- Blend: 82% on the betting line for the margin and 100% for the total, wherever there is a line (fitted on past closing lines).
- Simulator: each team's points vary by 11.0 with correlation 0.23; 5.2% of recent games went to overtime.
