# NBA score predictions

Updated Wed Nov 18, 2026 03:11 AM ET. Refreshed automatically several times a day during the season, around the injury report's deadlines; each game's prediction is locked at tip-off and graded once the final score is in.

Each team's expected points are its expected possessions times its expected points per possession, from team efficiency ratings and the ratings of the players expected to play, blended with the betting line. Each game is then simulated 10,000 times, overtime included. The predicted score is the expected points rounded; the 80% range holds 80% of simulated outcomes for each team. Basketball is the most predictable major sport, but a team's score still varies by about ±14 points around the forecast, so read the win chance and the ranges too.

Missing players come from the injury report: out players are left out, and doubtful, questionable and probable ones count with the share of their minutes their chance of playing implies, and their minutes go mostly to the bench. The effect is how many points of margin the team gains or loses against its full-strength roster: negative when it is missing good players, positive when the minutes go to better ones. Predictions are rerun when the report changes, up to tip-off.

The fair moneyline is the American odds that match the win chance exactly, with no bookmaker margin: -150 means risk $150 to win $100, +150 means risk $100 to win $150.

The edge columns check every side of the spread, the moneyline and the total for expected value: the profit per $1 bet at the posted price, using the final prediction's chances (the model blended with the line, simulated against the posted lines, pushes returning the stake, and anchored to the market's own chances so only what the blend moves off the line counts). The model's own spread and total are shown alongside, but the blend keeps only the share of that disagreement the model has earned in past seasons, so edges are rare. A side is an edge when its EV is 3% or more; the best such side is shown with its price, its EV, its chance of winning the bet and its stake, a 25% share of the Kelly stake in units of 1% of the bankroll, with at most 3 units on one game. Where a spread or total price is not posted it is assumed to be -110 (marked \*); a moneyline is never assumed. Edges are logged with each prediction, locked at tip-off and graded below. Treat them as an experiment, not betting advice; see the backtest for how they have done on past seasons.

## Wednesday, November 18

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Spread: model / line | Total: model / line | 80% range | Overtime | Missing (effect on margin) | Spread edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 7:00 PM | MEM @ CLE | MEM 116, CLE 120 | CLE 62% | MEM +165 / CLE -165<br>posted MEM +171 / CLE -205 | CLE -4.4 / CLE -4.5 (fav covers 51%) | 235.7 / 235.5 (over 49%) | 101–131 / 106–135 | 5% | MEM: Ty Jerome (out); Isaiah Stewart (out); Scotty Pippen Jr. (out) (-1.2)<br>CLE: Evan Mobley (out); Jaylon Tyson (day-to-day); Peyton Watson (day-to-day); Sam Merrill (out) (-0.9) | no edge | no edge | no edge |
| 7:00 PM | HOU @ IND | HOU 116, IND 109 | HOU 70% | HOU -230 / IND +230<br>posted HOU -279 / IND +228 | HOU -6.9 / HOU -7.5 (fav covers 49%) | 225.7 / 225.5 (over 49%) | 102–131 / 95–124 | 5% | HOU: Amen Thompson (day-to-day); Clint Capela (out) (-0.3)<br>IND: Andrew Nembhard (day-to-day); Tyrese Haliburton (out); Johnny Furphy (out); Ben Sheppard (out); T.J. McConnell (day-to-day) (+0.2) | no edge | no edge | no edge |
| 7:00 PM | MIL @ MIA | MIL 112, MIA 124 | MIA 81% | MIL +435 / MIA -435<br>posted MIL +558 / MIA -800 | MIA -12.2 / MIA -12.5 (fav covers 47%) | 236.1 / 236.5 (over 48%) | 97–127 / 110–139 | 3% | MIA: Bam Adebayo (day-to-day); Myron Gardner (day-to-day) (-0.4) | no edge | no edge | no edge |
| 7:00 PM | PHI @ ORL | PHI 111, ORL 110 | PHI 53% | PHI -115 / ORL +115<br>posted PHI -135 / ORL +114 | PHI -1.2 / PHI -1.5 (fav covers 51%) | 221.7 / 221.5 (over 50%) | 97–126 / 96–125 | 6% | PHI: Jaylen Brown (out); Adem Bona (out); Dominick Barlow (out) (+1.1)<br>ORL: Paolo Banchero (out) (+1.5) | no edge | no edge | no edge |
| 7:30 PM | CHI @ BKN | CHI 119, BKN 121 | BKN 55% | CHI +120 / BKN -120<br>posted CHI +128 / BKN -152 | BKN -1.8 / BKN -2.5 (fav covers 49%) | 239.6 / 239.5 (over 49%) | 104–134 / 106–135 | 5% | CHI: Caleb Wilson (out); Patrick Williams (day-to-day) (+1.7) | no edge | no edge | no edge |
| 7:30 PM | WAS @ TOR | WAS 111, TOR 117 | TOR 67% | WAS +205 / TOR -205<br>posted WAS +205 / TOR -249 | TOR -6.1 / TOR -6.5 (fav covers 50%) | 227.5 / 227.5 (over 49%) | 96–126 / 103–131 | 5% | WAS: Jamir Watkins (out); Justin Champagnie (out); Tristan Vukcevic (out) (+0.0)<br>TOR: Kawhi Leonard (out) (-1.9) | no edge | no edge | no edge |
| 8:00 PM | DET @ NOP | DET 118, NOP 111 | DET 70% | DET -240 / NOP +240<br>posted DET -277 / NOP +227 | DET -7.3 / DET -7.5 (fav covers 50%) | 228.7 / 228.5 (over 50%) | 104–132 / 96–126 | 5% | DET: Duncan Robinson (out); Jalen Duren (out); Ronald Holland II (out) (-0.1)<br>NOP: Trey Murphy III (out); Dejounte Murray (out); Trendon Watford (out); Bennedict Mathurin (out); Bryce McGowens (out) (+0.0) | no edge | no edge | no edge |
| 8:00 PM | ATL @ OKC | ATL 111, OKC 117 | OKC 68% | ATL +215 / OKC -215<br>posted ATL +218 / OKC -265 | OKC -6.2 / OKC -6.5 (fav covers 50%) | 228.7 / 228.5 (over 49%) | 97–126 / 103–132 | 5% | ATL: CJ McCollum (out); Kingston Flemings (out); Jock Landale (out) (+2.0)<br>OKC: Chet Holmgren (out); Jalen Williams (out); Jaylin Williams (out); Cason Wallace (out) (-0.3) | no edge | no edge | no edge |
| 8:00 PM | GSW @ DAL | GSW 109, DAL 114 | DAL 66% | GSW +190 / DAL -190<br>posted GSW +184 / DAL -222 | DAL -5.2 / DAL -5.5 (fav covers 51%) | 222.5 / 222.5 (over 49%) | 94–123 / 100–128 | 5% | GSW: Moses Moody (out); Jimmy Butler III (out); Draymond Green (day-to-day); Kristaps Porzingis (out); Stephen Curry (out); Al Horford (day-to-day); Brandon Williams (out) (-3.4)<br>DAL: Walter Clayton Jr. (day-to-day); Dereck Lively II (out); Santi Aldama (day-to-day); Sergio de Larrea (out) (+0.9) | no edge | no edge | no edge |
| 9:30 PM | BOS @ DEN | BOS 113, DEN 110 | BOS 58% | BOS -135 / DEN +135<br>posted BOS -135 / DEN +114 | BOS -2.4 / BOS -2.5 (fav covers 52%) | 222.7 / 222.5 (over 49%) | 98–127 / 96–124 | 5% | – | no edge | no edge | no edge |
| 10:00 PM | UTA @ LAL | UTA 110, LAL 120 | LAL 78% | UTA +355 / LAL -355<br>posted UTA +371 / LAL -484 | LAL -10.4 / LAL -10.5 (fav covers 49%) | 230.5 / 230.5 (over 49%) | 95–125 / 106–135 | 4% | UTA: Lauri Markkanen (out); Jaren Jackson Jr. (out); Jaxson Hayes (out); Jusuf Nurkic (out) (-3.1)<br>LAL: Austin Reaves (out); Walker Kessler (out) (-2.6) | no edge | no edge | no edge |
| 10:00 PM | PHX @ SAC | PHX 118, SAC 111 | PHX 68% | PHX -215 / SAC +215<br>posted PHX -269 / SAC +220 | PHX -6.5 / PHX -6.5 (fav covers 50%) | 228.5 / 228.5 (over 49%) | 103–132 / 96–126 | 5% | PHX: Mark Williams (out) (+0.5)<br>SAC: De'Andre Hunter (day-to-day); Maxime Raynaud (out); Precious Achiuwa (day-to-day) (+0.5) | no edge | no edge | no edge |

## Thursday, November 19

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Spread: model / line | Total: model / line | 80% range | Overtime | Missing (effect on margin) | Spread edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 8:00 PM | GSW @ MEM | GSW 114, MEM 117 | MEM 60% | GSW +150 / MEM -150 | MEM -3.2 | 231.4 | 99–129 / 102–132 | 6% | GSW: Moses Moody (out); Jimmy Butler III (out); Draymond Green (day-to-day); Kristaps Porzingis (out); Stephen Curry (out); Al Horford (day-to-day); Brandon Williams (out) (-3.4)<br>MEM: Ty Jerome (out); Isaiah Stewart (out); Scotty Pippen Jr. (out) (-1.1) | no line yet | no line yet | no line yet |
| 8:00 PM | POR @ MIL | POR 118, MIL 109 | POR 76% | POR -325 / MIL +325 | POR -9.7 | 227.2 | 104–133 / 94–124 | 4% | POR: Deni Avdija (out); Ja Morant (out); Chris Youngblood (out) (-1.1) | no line yet | no line yet | no line yet |
| 8:00 PM | NYK @ MIN | NYK 108, MIN 109 | MIN 53% | NYK +110 / MIN -110 | MIN -0.9 | 217.5 | 94–122 / 95–123 | 6% | MIN: Anthony Edwards (out); Jonathan Kuminga (out); Donte DiVincenzo (out); Jaylen Clark (out) (-1.6) | no line yet | no line yet | no line yet |
| 8:00 PM | LAC @ SAS | LAC 105, SAS 118 | SAS 83% | LAC +500 / SAS -500 | SAS -13.1 | 223.4 | 91–120 / 104–133 | 3% | LAC: Brandon Ingram (out); Jordan Miller (out); Bradley Beal (out); Yanic Konan Niederhauser (out) (+0.7)<br>SAS: Dylan Harper (day-to-day); Tobias Harris (out) (+0.8) | no line yet | no line yet | no line yet |

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
| 1 | SAS | +8.0 | +7.9 | +3.3 | +4.7 | 99.1 | +0.8 | 1734 |
| 2 | BOS | +7.8 | +7.4 | +4.1 | +3.7 | 95.1 | +0.0 | 1654 |
| 3 | HOU | +5.6 | +5.5 | +3.2 | +2.4 | 98.0 | -0.2 | 1615 |
| 4 | LAL | +5.4 | +5.6 | +4.5 | +0.8 | 103.0 | -2.6 | 1631 |
| 5 | DET | +5.3 | +5.3 | +2.4 | +2.9 | 101.0 | -0.1 | 1626 |
| 6 | MIN | +4.7 | +4.9 | +1.2 | +3.5 | 103.7 | -1.7 | 1611 |
| 7 | NYK | +4.1 | +3.9 | +0.9 | +3.3 | 94.5 | +0.0 | 1681 |
| 8 | DEN | +3.5 | +3.4 | +3.7 | -0.2 | 97.7 | +0.2 | 1566 |
| 9 | OKC | +3.5 | +3.5 | -0.5 | +4.0 | 101.8 | -0.3 | 1652 |
| 10 | POR | +2.8 | +2.9 | +1.9 | +0.9 | 102.1 | -1.1 | 1576 |
| 11 | PHI | +2.4 | +2.5 | +1.2 | +1.3 | 101.3 | +1.1 | 1575 |
| 12 | CLE | +0.5 | +0.5 | +1.7 | -1.2 | 101.5 | -0.9 | 1577 |
| 13 | GSW | +0.5 | +0.5 | +0.0 | +0.5 | 100.2 | -3.4 | 1502 |
| 14 | MIA | +0.4 | +0.5 | +1.7 | -1.3 | 104.0 | -0.4 | 1546 |
| 15 | TOR | +0.4 | +0.4 | -0.4 | +0.8 | 101.1 | -1.9 | 1508 |
| 16 | PHX | +0.4 | +0.4 | +0.7 | -0.4 | 102.0 | +0.5 | 1517 |
| 17 | ORL | +0.1 | +0.1 | -1.8 | +1.9 | 100.4 | +1.5 | 1526 |
| 18 | MEM | -0.7 | -0.7 | +1.4 | -2.0 | 102.6 | -1.2 | 1465 |
| 19 | IND | -1.0 | -1.0 | -0.2 | -0.8 | 103.4 | +0.2 | 1371 |
| 20 | DAL | -2.2 | -2.2 | -1.1 | -1.1 | 102.2 | +1.0 | 1431 |
| 21 | ATL | -2.3 | -2.5 | -2.0 | -0.3 | 107.6 | +2.1 | 1530 |
| 22 | LAC | -2.9 | -2.9 | -1.2 | -1.6 | 101.1 | +0.7 | 1484 |
| 23 | UTA | -3.3 | -3.3 | -3.0 | -0.3 | 100.9 | -3.1 | 1282 |
| 24 | CHI | -4.5 | -5.0 | -2.3 | -2.3 | 109.2 | +1.8 | 1386 |
| 25 | NOP | -5.2 | -5.4 | -1.9 | -3.3 | 103.8 | +0.0 | 1368 |
| 26 | CHA | -5.6 | -5.4 | -5.1 | -0.5 | 96.7 | -0.5 | 1469 |
| 27 | BKN | -5.6 | -5.7 | -2.3 | -3.4 | 101.2 | +0.0 | 1334 |
| 28 | WAS | -5.8 | -5.9 | -2.5 | -3.4 | 100.9 | +0.0 | 1302 |
| 29 | SAC | -8.2 | -8.4 | -4.0 | -4.1 | 102.4 | +0.5 | 1317 |
| 30 | MIL | -8.2 | -8.2 | -3.7 | -4.4 | 100.9 | +0.2 | 1315 |

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
