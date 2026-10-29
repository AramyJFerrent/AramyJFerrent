# NBA score predictions

Updated Thu Oct 29, 2026 06:01 PM ET. Refreshed automatically several times a day during the season, around the injury report's deadlines; each game's prediction is locked at tip-off and graded once the final score is in.

Each team's expected points are its expected possessions times its expected points per possession, from team efficiency ratings and the ratings of the players expected to play, blended with the betting line. Each game is then simulated 10,000 times, overtime included. The predicted score is the expected points rounded; the 80% range holds 80% of simulated outcomes for each team. Basketball is the most predictable major sport, but a team's score still varies by about ±14 points around the forecast, so read the win chance and the ranges too.

Missing players come from the injury report: out players are left out, and doubtful, questionable and probable ones count with the share of their minutes their chance of playing implies, and their minutes go mostly to the bench. The effect is how many points of margin the team gains or loses against its full-strength roster: negative when it is missing good players, positive when the minutes go to better ones. Predictions are rerun when the report changes, up to tip-off.

The fair moneyline is the American odds that match the win chance exactly, with no bookmaker margin: -150 means risk $150 to win $100, +150 means risk $100 to win $150.

The edge columns check every side of the spread, the moneyline and the total for expected value: the profit per $1 bet at the posted price, using the final prediction's chances (the model blended with the line, simulated against the posted lines, pushes returning the stake, and anchored to the market's own chances so only what the blend moves off the line counts). The model's own spread and total are shown alongside, but the blend keeps only the share of that disagreement the model has earned in past seasons, so edges are rare. A side is an edge when its EV is 3% or more; the best such side is shown with its price, its EV, its chance of winning the bet and its stake, a 25% share of the Kelly stake in units of 1% of the bankroll, with at most 3 units on one game. Where a spread or total price is not posted it is assumed to be -110 (marked \*); a moneyline is never assumed. Edges are logged with each prediction, locked at tip-off and graded below. Treat them as an experiment, not betting advice; see the backtest for how they have done on past seasons.

## Thursday, October 29

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Spread: model / line | Total: model / line | 80% range | Overtime | Missing (effect on margin) | Spread edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 8:00 PM | CLE @ ATL | CLE 118, ATL 120 | ATL 54% | CLE +115 / ATL -115<br>posted CLE -102 / ATL -118 | ATL -1.4 / ATL -1.5 (fav covers 51%) | 237.7 / 237.5 (over 49%) | 103–133 / 105–134 | 5% | CLE: Jaylon Tyson (day-to-day); Meleek Thomas (day-to-day) (+0.3) | no edge | no edge | no edge |
| 8:00 PM | SAC @ NOP | SAC 115, NOP 121 | NOP 66% | SAC +195 / NOP -195<br>posted SAC +195 / NOP -238 | NOP -5.7 / NOP -6.5 (fav covers 48%) | 235.6 / 235.5 (over 50%) | 100–130 / 106–135 | 5% | SAC: Maxime Raynaud (out); Keegan Murray (out); Dylan Cardwell (out) (+0.2)<br>NOP: Yves Missi (out); Jordan Poole (day-to-day) (+0.3) | no edge | no edge | no edge |
| 10:00 PM | MEM @ POR | MEM 113, POR 120 | POR 71% | MEM +250 / POR -250<br>posted MEM +235 / POR -290 | POR -7.6 / POR -7.5 (fav covers 51%) | 232.7 / 232.5 (over 49%) | 97–128 / 106–135 | 5% | POR: Robert Williams III (day-to-day) (+0.2) | no edge | no edge | no edge |

## Friday, October 30

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Spread: model / line | Total: model / line | 80% range | Overtime | Missing (effect on margin) | Spread edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 7:00 PM | CHA @ WAS | CHA 112, WAS 111 | CHA 54% | CHA -115 / WAS +115<br>posted CHA -110 / WAS -110 | CHA -1.2 / CHA -1.5 (fav covers 51%) | 222.5 / 222.5 (over 50%) | 98–126 / 96–125 | 5% | CHA: Dennis Schroder (day-to-day); Kon Knueppel (out); Coby White (out); Grant Williams (out) (-0.8)<br>WAS: Jamir Watkins (out); Justin Champagnie (out); Tre Johnson (day-to-day); Tristan Vukcevic (out) (-0.1) | no edge | no edge | no edge |
| 7:30 PM | CHI @ BOS | CHI 109, BOS 124 | BOS 87% | CHI +670 / BOS -670<br>posted CHI +575 / BOS -850 | BOS -15.5 / BOS -15.5 (fav covers 48%) | 233.1 / 233.5 (over 49%) | 94–124 / 110–139 | 3% | CHI: Jalen Smith (day-to-day); Nic Claxton (out); Patrick Williams (out) (+0.2)<br>BOS: Devin Carter (out) (+1.2) | no edge | no edge | no edge |
| 7:30 PM | DET @ BKN | DET 114, BKN 107 | DET 72% | DET -250 / BKN +250<br>posted DET -258 / BKN +210 | DET -7.6 / DET -7.5 (fav covers 51%) | 221.4 / 221.5 (over 49%) | 100–128 / 93–121 | 4% | DET: Jalen Duren (out) (-0.2)<br>BKN: Egor Demin (out) (+0.8) | no edge | no edge | no edge |
| 7:30 PM | NYK @ PHI | NYK 115, PHI 114 | NYK 52% | NYK -110 / PHI +110<br>posted NYK -120 / PHI +100 | NYK -1.1 / NYK -1.5 (fav covers 50%) | 228.6 / 228.5 (over 49%) | 101–129 / 99–128 | 5% | NYK: Jose Alvarado (out) (-0.3)<br>PHI: Jaylen Brown (day-to-day); Dominick Barlow (out) (+0.5) | no edge | no edge | no edge |
| 7:30 PM | ORL @ TOR | ORL 110, TOR 115 | TOR 63% | ORL +175 / TOR -175<br>posted ORL +160 / TOR -192 | TOR -4.7 / TOR -5.5 (fav covers 48%) | 224.7 / 224.5 (over 49%) | 96–124 / 100–129 | 5% | ORL: Paolo Banchero (out); Jalen Suggs (out) (+0.2)<br>TOR: Kawhi Leonard (out) (-1.9) | no edge | no edge | no edge |
| 8:00 PM | IND @ MIA | IND 116, MIA 123 | MIA 69% | IND +220 / MIA -220<br>posted IND +205 / MIA -250 | MIA -6.9 / MIA -7.5 (fav covers 49%) | 239.5 / 239.5 (over 49%) | 101–131 / 108–138 | 5% | IND: Andrew Nembhard (day-to-day); Tyrese Haliburton (out); Aaron Nesmith (day-to-day); Johnny Furphy (out); Ivica Zubac (out); Ben Sheppard (out); T.J. McConnell (out) (-0.7) | no edge | no edge | no edge |
| 8:00 PM | HOU @ DAL | HOU 117, DAL 111 | HOU 67% | HOU -205 / DAL +205<br>posted HOU -192 / DAL +160 | HOU -5.7 / HOU -5.5 (fav covers 52%) | 227.7 / 227.5 (over 50%) | 102–131 / 96–125 | 5% | HOU: Alperen Sengun (day-to-day); Reed Sheppard (out); Marcus Smart (out); Steven Adams (out) (+0.6)<br>DAL: Naji Marshall (day-to-day); Santi Aldama (out); Dereck Lively II (out); Sergio de Larrea (day-to-day) (+0.2) | no edge | no edge | no edge |
| 8:00 PM | LAC @ MIN | LAC 107, MIN 114 | MIN 70% | LAC +235 / MIN -235<br>posted LAC +200 / MIN -245 | MIN -6.8 / MIN -7.5 (fav covers 49%) | 221.5 / 221.5 (over 49%) | 93–122 / 100–128 | 5% | LAC: Rui Hachimura (day-to-day); Max Strus (out); Brandon Ingram (out); Jordan Miller (out); Bradley Beal (out); Yanic Konan Niederhauser (out) (+1.0)<br>MIN: Anthony Edwards (out); Donte DiVincenzo (out) (-1.4) | no edge | no edge | no edge |
| 10:00 PM | LAL @ GSW | LAL 118, GSW 117 | LAL 54% | LAL -115 / GSW +115<br>posted LAL -125 / GSW +105 | LAL -1.3 / LAL -1.5 (fav covers 51%) | 234.4 / 234.5 (over 49%) | 103–132 / 102–131 | 5% | LAL: Luka Doncic (day-to-day); Ziaire Williams (day-to-day) (+0.5)<br>GSW: Moses Moody (out); Jimmy Butler III (out); Gui Santos (day-to-day); Kristaps Porzingis (out) (-1.4) | no edge | no edge | no edge |
| 10:00 PM | DEN @ PHX | DEN 117, PHX 114 | DEN 61% | DEN -155 / PHX +155<br>posted DEN -170 / PHX +142 | DEN -3.7 / DEN -4.5 (fav covers 49%) | 230.9 / 230.5 (over 49%) | 103–132 / 99–129 | 5% | DEN: Spencer Jones (out); Cameron Johnson (out); Alpha Diallo (out) (+1.8)<br>PHX: Oso Ighodaro (day-to-day); Mark Williams (out) (+0.3) | no edge | no edge | no edge |

## How the 2026-27 predictions have done

| Predictor | Games | Margin MAE | Total MAE | Team-points MAE | Log loss | Brier | Winners | 80% range hit |
|---|---|---|---|---|---|---|---|---|
| Final prediction | 68 | 11.19 | 14.83 | 9.64 | 0.572 | 0.196 | 69.1% | 80.1% |
| Model only (before blending) | 68 | 11.90 | 14.37 | 9.82 | 0.611 | 0.213 | 63.2% | – |
| Elo | 68 | 12.14 | – | – | 0.640 | 0.226 | 60.3% | – |
| Final prediction, games with a line | 68 | 11.19 | 14.83 | 9.64 | 0.572 | 0.196 | 69.1% | 80.1% |
| Model only, games with a line | 68 | 11.90 | 14.37 | 9.82 | 0.611 | 0.213 | 63.2% | – |
| Betting line | 68 | 11.09 | 14.82 | 9.60 | 0.556 | 0.189 | 69.1% | – |

MAE is the average miss in points; team-points MAE is the average miss on each team's score. Log loss and Brier score the win chances (lower is better; a coin flip scores 0.693 and 0.250). The closing line misses margins by about 10 points and totals by about 14.

Overtime: predicted in 4.8% of games, happened in 5.9%.

### Betting edges

| Market | Edges | Record (W-L-P) | Staked | Units won | ROI | Expected ROI |
|---|---|---|---|---|---|---|
| Spread | 1 | 1-0-0 | 1.0 | +0.90 | +89.3% | +3.6% |
| Moneyline | 5 | 0-5-0 | 1.9 | -1.88 | -100.0% | +8.8% |
| Total | 0 | 0-0-0 | 0.0 | +0.00 | – | – |

Spread moved toward the model's first spread edge before tip-off: 4 of 5 games (80%).

Live predictions only, each edge at the stake and price logged with the last prediction before tip-off (edges logged before edges were priced from the final prediction are left out); a push returns the stake. Units are 1% of the bankroll; ROI is units won per unit staked, and expected ROI is what the edges' EVs promised. The line moving toward the model's edge before tip-off is the quickest sign that it knows something the market doesn't yet.

### Results, Wednesday, October 28

| Game | Predicted | Final | Win chance for winner | Spread: model / line | Inside 80% ranges |
|---|---|---|---|---|---|
| MIA @ ATL | 120–123 | 129–117 | 41% | ATL -2.8 / ATL -2.5 | yes |
| WAS @ CLE | 115–125 | 111–121 | 75% | CLE -9.7 / CLE -9.5 | yes |
| CHA @ DET | 103–110 | 89–97 | 72% | DET -7.3 / DET -7.5 | yes |
| PHI @ IND | 120–114 | 114–109 | 69% | PHI -6.6 / PHI -7.5 | yes |
| ORL @ TOR | 110–114 | 99–129 | 61% | TOR -3.6 / TOR -4.5 | no |
| NYK @ CHI | 120–113 | 133–127 | 71% | NYK -7.4 / NYK -7.5 | yes |
| HOU @ MIL | 117–109 | 132–100 | 74% | HOU -8.5 / HOU -8.5 | yes |
| GSW @ MIN | 112–116 | 119–114 | 39% | MIN -3.7 / MIN -3.5 | yes |
| DEN @ NOP | 123–118 | 104–91 | 63% | DEN -4.6 / DEN -4.5 | no |
| SAS @ UTA | 123–110 | 117–111 (OT) | 82% | SAS -12.5 / SAS -13.5 | yes |
| OKC @ DAL | 117–112 | 96–120 | 35% | OKC -4.8 / OKC -5.5 | no |
| LAL @ LAC | 111–113 | 103–87 | 45% | LAC -1.8 / LAC -1.5 | no |

## Power ratings

Points per 100 possessions better than an average team on a neutral floor, combining opponent-adjusted team efficiency (garbage time removed) with the ratings of the team's healthy roster, through the fitted points map. Net per game uses the team's pace. Injury effect now is what its current injury report does to its margin, in points.

| # | Team | Net per 100 | Net per game | Offense | Defense | Pace | Injury effect now | Elo |
|---|---|---|---|---|---|---|---|---|
| 1 | HOU | +7.1 | +7.2 | +3.5 | +3.5 | 101.4 | +0.6 | 1616 |
| 2 | SAS | +6.7 | +6.8 | +2.0 | +4.6 | 102.6 | +0.7 | 1687 |
| 3 | BOS | +5.6 | +5.6 | +3.1 | +2.6 | 99.7 | +1.1 | 1615 |
| 4 | DET | +5.4 | +5.3 | +1.7 | +3.7 | 98.4 | -0.2 | 1643 |
| 5 | POR | +4.4 | +4.5 | +3.5 | +0.9 | 102.6 | +0.2 | 1561 |
| 6 | NYK | +4.0 | +4.0 | +1.4 | +2.6 | 101.1 | -0.3 | 1695 |
| 7 | OKC | +3.4 | +3.4 | -0.5 | +3.9 | 101.9 | -1.0 | 1677 |
| 8 | MIN | +3.0 | +3.1 | +1.0 | +2.0 | 104.0 | -1.4 | 1593 |
| 9 | LAL | +2.6 | +2.6 | +2.9 | -0.3 | 101.3 | +0.5 | 1590 |
| 10 | CLE | +2.3 | +2.3 | +2.2 | +0.1 | 103.4 | +0.3 | 1579 |
| 11 | PHI | +2.1 | +2.2 | -0.6 | +2.7 | 107.1 | +0.5 | 1553 |
| 12 | TOR | +1.9 | +2.0 | -0.3 | +2.2 | 106.3 | -1.9 | 1565 |
| 13 | GSW | +1.1 | +1.1 | +1.2 | -0.1 | 103.5 | -1.4 | 1474 |
| 14 | DEN | +0.5 | +0.5 | +1.8 | -1.3 | 99.1 | +1.8 | 1570 |
| 15 | MIA | +0.4 | +0.4 | +0.9 | -0.5 | 107.7 | +0.0 | 1494 |
| 16 | ATL | +0.2 | +0.2 | +0.3 | -0.1 | 108.7 | +0.8 | 1551 |
| 17 | ORL | +0.0 | +0.0 | -2.0 | +2.1 | 105.5 | +0.2 | 1524 |
| 18 | PHX | -0.7 | -0.7 | +1.0 | -1.8 | 101.4 | +0.3 | 1507 |
| 19 | DAL | -1.3 | -1.3 | -0.7 | -0.5 | 102.6 | +0.2 | 1447 |
| 20 | IND | -1.5 | -1.6 | -0.1 | -1.5 | 103.8 | -0.7 | 1379 |
| 21 | CHA | -2.3 | -2.2 | -2.6 | +0.3 | 97.1 | -0.8 | 1556 |
| 22 | MEM | -2.3 | -2.4 | -0.2 | -2.1 | 102.6 | +0.0 | 1380 |
| 23 | LAC | -2.5 | -2.5 | -1.7 | -0.7 | 101.9 | +1.0 | 1509 |
| 24 | UTA | -3.8 | -3.9 | -2.2 | -1.6 | 102.5 | -1.3 | 1319 |
| 25 | WAS | -5.1 | -5.2 | -1.9 | -3.1 | 102.4 | -0.1 | 1300 |
| 26 | NOP | -5.2 | -5.5 | -2.2 | -2.9 | 105.9 | +0.3 | 1405 |
| 27 | BKN | -5.9 | -6.3 | -2.8 | -3.1 | 105.9 | +0.9 | 1293 |
| 28 | CHI | -6.3 | -7.1 | -3.3 | -3.0 | 113.4 | +0.2 | 1366 |
| 29 | MIL | -6.3 | -6.7 | -2.3 | -4.0 | 105.7 | +0.0 | 1357 |
| 30 | SAC | -7.4 | -7.6 | -3.1 | -4.3 | 103.4 | +0.2 | 1344 |

## Top players

Regularized adjusted plus-minus from every lineup this season and past ones: points per 100 possessions a player adds on offense and saves on defense, against an average player, shrunk toward last season's rating. Players expected to play 20 minutes or more.

| # | Player | Team | Net impact per 100 | Offense | Defense | Expected minutes |
|---|---|---|---|---|---|---|
| 1 | Victor Wembanyama | SAS | +6.3 | +1.6 | +4.7 | 34 |
| 2 | Shai Gilgeous-Alexander | OKC | +5.8 | +5.1 | +0.8 | 32 |
| 3 | Nikola Jokic | DEN | +5.0 | +5.3 | -0.3 | 37 |
| 4 | Kawhi Leonard | TOR | +4.5 | +3.6 | +0.8 | 30 |
| 5 | Luka Doncic | LAL | +3.5 | +4.9 | -1.4 | 36 |
| 6 | Giannis Antetokounmpo | MIA | +3.3 | +3.5 | -0.1 | 32 |
| 7 | Joel Embiid | PHI | +3.2 | +1.7 | +1.5 | 36 |
| 8 | Kyrie Irving | DAL | +3.1 | +3.1 | +0.1 | 28 |
| 9 | Fred VanVleet | HOU | +2.8 | +1.9 | +0.9 | 31 |
| 10 | Lauri Markkanen | UTA | +2.3 | +2.1 | +0.2 | 24 |
| 11 | Jimmy Butler III | GSW | +2.2 | +2.1 | +0.1 | 27 |
| 12 | Franz Wagner | ORL | +2.1 | +0.6 | +1.5 | 33 |
| 13 | Chet Holmgren | OKC | +2.1 | +0.1 | +2.0 | 30 |
| 14 | Ausar Thompson | DET | +2.0 | -0.2 | +2.2 | 27 |
| 15 | Dyson Daniels | ATL | +2.0 | +0.9 | +1.1 | 28 |
| 16 | Bam Adebayo | MIA | +1.9 | +1.0 | +0.9 | 31 |
| 17 | Ty Jerome | MEM | +1.8 | +3.4 | -1.5 | 30 |
| 18 | Pascal Siakam | IND | +1.8 | +1.7 | +0.1 | 33 |
| 19 | Jrue Holiday | POR | +1.7 | +0.6 | +1.1 | 30 |
| 20 | Kevin Durant | HOU | +1.6 | +3.1 | -1.5 | 33 |
| 21 | Cade Cunningham | DET | +1.6 | +1.6 | +0.0 | 37 |
| 22 | LaMelo Ball | MIN | +1.6 | +3.9 | -2.3 | 27 |
| 23 | Rudy Gobert | MIN | +1.5 | -3.4 | +4.9 | 28 |
| 24 | Nickeil Alexander-Walker | ATL | +1.4 | +1.6 | -0.2 | 31 |
| 25 | Jarrett Allen | CLE | +1.4 | +1.0 | +0.4 | 29 |
| 26 | Dean Wade | PHI | +1.3 | -0.1 | +1.4 | 22 |
| 27 | Paul Reed | DET | +1.2 | +0.0 | +1.3 | 28 |
| 28 | Derrick White | BOS | +1.2 | -0.2 | +1.4 | 31 |
| 29 | Damian Lillard | POR | +1.1 | +2.1 | -1.0 | 29 |
| 30 | Devin Vassell | SAS | +1.0 | +0.8 | +0.3 | 33 |

## Current model fit

- Fitted on 5350 games from 2022-23 to 2026-27.
- Home court: +2.0 points per 100 possessions for the home team over the visitor (about 2.0 points a game).
- Second night of a back-to-back: -0.7 points per 100 scored, +1.2 allowed.
- Weights: team efficiency ratings 0.16 (offense) and 0.15 (defense); player lineup ratings 0.76 and 0.76.
- Blend: 82% on the betting line for the margin and 100% for the total, wherever there is a line (fitted on past closing lines).
- Simulator: each team's points vary by 10.9 with correlation 0.23; 5.2% of recent games went to overtime.
