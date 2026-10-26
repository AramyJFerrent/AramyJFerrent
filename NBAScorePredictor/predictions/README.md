# NBA score predictions

Updated Sun Oct 25, 2026 09:10 PM ET. Refreshed automatically several times a day during the season, around the injury report's deadlines; each game's prediction is locked at tip-off and graded once the final score is in.

Each team's expected points are its expected possessions times its expected points per possession, from team efficiency ratings and the ratings of the players expected to play, blended with the betting line. Each game is then simulated 10,000 times, overtime included. The predicted score is the expected points rounded; the 80% range holds 80% of simulated outcomes for each team. Basketball is the most predictable major sport, but a team's score still varies by about ±14 points around the forecast, so read the win chance and the ranges too.

Missing players come from the injury report: out players are left out, and doubtful, questionable and probable ones count with the share of their minutes their chance of playing implies, and their minutes go mostly to the bench. The effect is how many points of margin the team gains or loses against its full-strength roster: negative when it is missing good players, positive when the minutes go to better ones. Predictions are rerun when the report changes, up to tip-off.

The fair moneyline is the American odds that match the win chance exactly, with no bookmaker margin: -150 means risk $150 to win $100, +150 means risk $100 to win $150.

The edge columns check every side of the spread, the moneyline and the total for expected value: the profit per $1 bet at the posted price, using the final prediction's chances (the model blended with the line, simulated against the posted lines, pushes returning the stake, and anchored to the market's own chances so only what the blend moves off the line counts). The model's own spread and total are shown alongside, but the blend keeps only the share of that disagreement the model has earned in past seasons, so edges are rare. A side is an edge when its EV is 3% or more; the best such side is shown with its price, its EV, its chance of winning the bet and its stake, a 25% share of the Kelly stake in units of 1% of the bankroll, with at most 3 units on one game. Where a spread or total price is not posted it is assumed to be -110 (marked \*); a moneyline is never assumed. Edges are logged with each prediction, locked at tip-off and graded below. Treat them as an experiment, not betting advice; see the backtest for how they have done on past seasons.

## Monday, October 26

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Spread: model / line | Total: model / line | 80% range | Overtime | Missing (effect on margin) | Spread edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 7:00 PM | WAS @ CHA | WAS 113, CHA 116 | CHA 58% | WAS +140 / CHA -140<br>posted WAS +120 / CHA -142 | CHA -2.8 / CHA -2.5 (fav covers 52%) | 228.6 / 228.5 (over 49%) | 98–128 / 101–130 | 5% | WAS: Jamir Watkins (out); Tristan Vukcevic (out) (+0.9)<br>CHA: Kon Knueppel (out); Coby White (out); Grant Williams (out) (-0.7) | no edge | no edge | no edge |
| 7:00 PM | MIN @ CLE | MIN 114, CLE 119 | CLE 63% | MIN +170 / CLE -170 | CLE -4.4 | 233.0 | 99–129 / 104–133 | 5% | MIN: Donte DiVincenzo (out) (-0.2) | no line yet | no line yet | no line yet |
| 7:30 PM | CHI @ BOS | CHI 110, BOS 124 | BOS 84% | CHI +540 / BOS -540<br>posted CHI +575 / BOS -850 | BOS -14 / BOS -13.5 (fav covers 50%) | 233.2 / 233.5 (over 48%) | 95–125 / 109–138 | 3% | CHI: Nic Claxton (out); Patrick Williams (day-to-day) (+0.3)<br>BOS: Devin Carter (out) (+1.2) | no edge | no edge | no edge |
| 7:30 PM | DAL @ MIA | DAL 114, MIA 121 | MIA 70% | DAL +230 / MIA -230<br>posted DAL +235 / MIA -290 | MIA -7.2 / MIA -7.5 (fav covers 49%) | 235.3 / 235.5 (over 49%) | 99–129 / 106–136 | 5% | DAL: Naji Marshall (out); Santi Aldama (out); Cooper Flagg (out); Dereck Lively II (out) (-1.0) | no edge | no edge | no edge |
| 8:00 PM | IND @ MIL | IND 120, MIL 119 | IND 51% | IND -105 / MIL +105 | IND -0.4 | 237.8 | 104–134 / 104–133 | 5% | IND: Ivica Zubac (day-to-day); Johnny Furphy (out); Ben Sheppard (out); T.J. McConnell (out) (+0.8) | no line yet | no line yet | no line yet |
| 8:00 PM | PHX @ OKC | PHX 107, OKC 114 | OKC 70% | PHX +240 / OKC -240 | OKC -7.1 | 221.0 | 93–121 / 100–128 | 4% | PHX: Oso Ighodaro (day-to-day); Mark Williams (out) (+0.3)<br>OKC: Cason Wallace (day-to-day); Jaylin Williams (out) (+2.1) | no line yet | no line yet | no line yet |
| 8:30 PM | ATL @ HOU | ATL 112, HOU 118 | HOU 66% | ATL +190 / HOU -190<br>posted ATL +180 / HOU -218 | HOU -5.4 / HOU -5.5 (fav covers 51%) | 229.6 / 229.5 (over 49%) | 98–127 / 103–132 | 5% | HOU: Marcus Smart (day-to-day); Steven Adams (out) (-0.7) | no edge | no edge | no edge |
| 9:00 PM | MEM @ UTA | MEM 114, UTA 117 | UTA 57% | MEM +130 / UTA -130 | UTA -2.5 | 231.1 | 100–129 / 102–131 | 5% | MEM: Zach Edey (out) (-0.7)<br>UTA: Trey Alexander (out); Jusuf Nurkic (out) (+0.1) | no line yet | no line yet | no line yet |
| 10:00 PM | GSW @ DEN | GSW 114, DEN 121 | DEN 71% | GSW +240 / DEN -240<br>posted GSW +235 / DEN -290 | DEN -7.5 / DEN -7.5 (fav covers 51%) | 235.4 / 235.5 (over 48%) | 99–129 / 107–136 | 4% | GSW: Moses Moody (out); Jimmy Butler III (out); Gui Santos (day-to-day); Kristaps Porzingis (out); Brandon Williams (day-to-day) (-1.7)<br>DEN: Spencer Jones (out); Cameron Johnson (day-to-day); Alpha Diallo (day-to-day) (+1.3) | no edge | no edge | no edge |

## Tuesday, October 27

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Spread: model / line | Total: model / line | 80% range | Overtime | Missing (effect on margin) | Spread edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 7:30 PM | BKN @ BOS | BKN 105, BOS 117 | BOS 82% | BKN +455 / BOS -455 | BOS -12.1 | 222.8 | 91–120 / 103–131 | 3% | BKN: Mikel Brown Jr. (out) (+1.2)<br>BOS: Devin Carter (out) (+1.2) | no line yet | no line yet | no line yet |
| 8:00 PM | DET @ NYK | DET 109, NYK 113 | NYK 63% | DET +170 / NYK -170 | NYK -4.4 | 221.8 | 94–123 / 99–127 | 6% | DET: Ausar Thompson (out); Jalen Duren (out); Isaiah Joe (day-to-day) (-1.9)<br>NYK: Jose Alvarado (out) (-0.2) | no line yet | no line yet | no line yet |
| 8:00 PM | SAC @ SAS | SAC 106, SAS 122 | SAS 89% | SAC +770 / SAS -770 | SAS -16.4 | 228.6 | 92–121 / 108–137 | 2% | SAC: Maxime Raynaud (out); Keegan Murray (out); Dylan Cardwell (out) (+0.4)<br>SAS: Tobias Harris (out) (+0.7) | no line yet | no line yet | no line yet |
| 11:00 PM | POR @ LAL | POR 113, LAL 115 | LAL 56% | POR +125 / LAL -125 | LAL -1.9 | 228.1 | 99–128 / 100–130 | 5% | POR: Branden Carlson (day-to-day) (+0.6) | no line yet | no line yet | no line yet |

## How the 2026-27 predictions have done

| Predictor | Games | Margin MAE | Total MAE | Team-points MAE | Log loss | Brier | Winners | 80% range hit |
|---|---|---|---|---|---|---|---|---|
| Final prediction | 36 | 11.15 | 14.24 | 9.29 | 0.576 | 0.197 | 69.4% | 79.2% |
| Model only (before blending) | 36 | 12.36 | 13.96 | 9.85 | 0.626 | 0.220 | 61.1% | – |
| Elo | 36 | 12.16 | – | – | 0.651 | 0.231 | 55.6% | – |
| Final prediction, games with a line | 36 | 11.15 | 14.24 | 9.29 | 0.576 | 0.197 | 69.4% | 79.2% |
| Model only, games with a line | 36 | 12.36 | 13.96 | 9.85 | 0.626 | 0.220 | 61.1% | – |
| Betting line | 36 | 10.94 | 14.19 | 9.21 | 0.557 | 0.188 | 69.4% | – |

MAE is the average miss in points; team-points MAE is the average miss on each team's score. Log loss and Brier score the win chances (lower is better; a coin flip scores 0.693 and 0.250). The closing line misses margins by about 10 points and totals by about 14.

Overtime: predicted in 4.8% of games, happened in 2.8%.

### Betting edges

| Market | Edges | Record (W-L-P) | Staked | Units won | ROI | Expected ROI |
|---|---|---|---|---|---|---|
| Spread | 0 | 0-0-0 | 0.0 | +0.00 | – | – |
| Moneyline | 2 | 0-2-0 | 0.7 | -0.68 | -100.0% | +6.7% |
| Total | 0 | 0-0-0 | 0.0 | +0.00 | – | – |

Spread moved toward the model's first spread edge before tip-off: 4 of 5 games (80%).

Live predictions only, each edge at the stake and price logged with the last prediction before tip-off (edges logged before edges were priced from the final prediction are left out); a push returns the stake. Units are 1% of the bankroll; ROI is units won per unit staked, and expected ROI is what the edges' EVs promised. The line moving toward the model's edge before tip-off is the quickest sign that it knows something the market doesn't yet.

### Results, Saturday, October 24

| Game | Predicted | Final | Win chance for winner | Spread: model / line | Inside 80% ranges |
|---|---|---|---|---|---|
| MIA @ CHA | 116–113 | 110–115 | 41% | MIA -3.1 / MIA -3.5 | yes |
| BKN @ CLE | 108–120 | 121–125 | 80% | CLE -11.5 / CLE -11.5 | yes |
| MIL @ PHI | 111–123 | 116–127 | 80% | PHI -11.6 / PHI -11.5 | yes |
| WAS @ CHI | 122–123 | 124–120 | 46% | CHI -1.5 / CHI -1.5 | yes |
| SAS @ DAL | 121–108 | 122–106 | 84% | SAS -13.5 / SAS -14.5 | yes |
| HOU @ ATL | 114–113 | 121–114 | 52% | HOU -0.9 / HOU -1.5 | yes |
| NOP @ DEN | 114–126 | 135–141 (OT) | 80% | DEN -11.7 / DEN -11.5 | no |
| GSW @ PHX | 106–115 | 122–131 | 75% | PHX -9.3 / PHX -9.5 | no |

## Power ratings

Points per 100 possessions better than an average team on a neutral floor, combining opponent-adjusted team efficiency (garbage time removed) with the ratings of the team's healthy roster, through the fitted points map. Net per game uses the team's pace. Injury effect now is what its current injury report does to its margin, in points.

| # | Team | Net per 100 | Net per game | Offense | Defense | Pace | Injury effect now | Elo |
|---|---|---|---|---|---|---|---|---|
| 1 | BOS | +6.4 | +6.3 | +3.6 | +2.9 | 98.1 | +1.2 | 1609 |
| 2 | SAS | +6.4 | +6.8 | +1.6 | +4.8 | 106.0 | +0.8 | 1682 |
| 3 | HOU | +6.0 | +6.0 | +3.5 | +2.5 | 100.4 | -0.7 | 1598 |
| 4 | OKC | +5.1 | +5.2 | +0.0 | +5.1 | 102.0 | +2.2 | 1708 |
| 5 | NYK | +4.9 | +4.9 | +1.7 | +3.2 | 100.4 | -0.2 | 1704 |
| 6 | DET | +3.9 | +4.1 | +1.8 | +2.1 | 104.1 | -2.0 | 1635 |
| 7 | POR | +3.2 | +3.3 | +2.0 | +1.1 | 103.1 | +0.6 | 1549 |
| 8 | TOR | +2.9 | +3.2 | +0.2 | +2.7 | 108.1 | -1.8 | 1560 |
| 9 | CLE | +2.7 | +2.9 | +1.9 | +0.8 | 107.7 | +0.0 | 1573 |
| 10 | MIN | +2.6 | +2.7 | +1.0 | +1.6 | 104.3 | -0.2 | 1599 |
| 11 | PHI | +2.5 | +2.7 | -0.1 | +2.6 | 108.7 | -2.7 | 1561 |
| 12 | LAL | +2.4 | +2.4 | +1.8 | +0.5 | 103.5 | +1.1 | 1582 |
| 13 | DEN | +1.7 | +1.7 | +2.9 | -1.2 | 101.2 | +1.3 | 1593 |
| 14 | ATL | +1.2 | +1.3 | +0.9 | +0.3 | 107.6 | +0.8 | 1578 |
| 15 | ORL | +0.3 | +0.3 | -1.8 | +2.1 | 105.1 | +1.7 | 1520 |
| 16 | MIA | -0.2 | -0.2 | +0.8 | -1.0 | 105.9 | +0.0 | 1485 |
| 17 | PHX | -0.2 | -0.2 | +1.2 | -1.3 | 101.4 | +0.3 | 1510 |
| 18 | GSW | -1.3 | -1.3 | -0.2 | -1.1 | 102.2 | -1.7 | 1429 |
| 19 | LAC | -1.5 | -1.5 | -0.5 | -1.0 | 103.1 | +1.3 | 1526 |
| 20 | IND | -2.3 | -2.4 | -0.1 | -2.1 | 105.2 | +0.8 | 1370 |
| 21 | CHA | -2.4 | -2.4 | -2.7 | +0.3 | 101.3 | -0.7 | 1559 |
| 22 | DAL | -2.9 | -3.0 | -1.6 | -1.2 | 104.2 | -1.0 | 1400 |
| 23 | MEM | -3.5 | -3.7 | -1.0 | -2.5 | 103.5 | -0.7 | 1358 |
| 24 | UTA | -3.8 | -4.0 | -2.3 | -1.5 | 105.1 | +0.1 | 1333 |
| 25 | NOP | -5.0 | -5.3 | -1.4 | -3.6 | 105.9 | +0.3 | 1414 |
| 26 | WAS | -5.4 | -5.7 | -2.5 | -2.8 | 106.5 | +1.0 | 1304 |
| 27 | BKN | -5.6 | -5.9 | -3.0 | -2.6 | 105.8 | +1.2 | 1315 |
| 28 | MIL | -5.7 | -6.0 | -1.4 | -4.2 | 106.5 | +0.0 | 1361 |
| 29 | CHI | -6.0 | -6.7 | -3.4 | -2.6 | 110.8 | +0.3 | 1374 |
| 30 | SAC | -6.6 | -6.9 | -3.0 | -3.6 | 104.8 | +0.4 | 1361 |

## Top players

Regularized adjusted plus-minus from every lineup this season and past ones: points per 100 possessions a player adds on offense and saves on defense, against an average player, shrunk toward last season's rating. Players expected to play 20 minutes or more.

| # | Player | Team | Net impact per 100 | Offense | Defense | Expected minutes |
|---|---|---|---|---|---|---|
| 1 | Shai Gilgeous-Alexander | OKC | +6.0 | +5.1 | +0.9 | 36 |
| 2 | Victor Wembanyama | SAS | +5.7 | +1.0 | +4.8 | 33 |
| 3 | Nikola Jokic | DEN | +5.1 | +5.5 | -0.4 | 40 |
| 4 | Kawhi Leonard | TOR | +4.4 | +3.6 | +0.8 | 30 |
| 5 | Alex Caruso | OKC | +4.0 | -0.2 | +4.2 | 25 |
| 6 | Giannis Antetokounmpo | MIA | +3.5 | +3.5 | +0.0 | 28 |
| 7 | Joel Embiid | PHI | +3.3 | +1.8 | +1.5 | 34 |
| 8 | Luka Doncic | LAL | +3.2 | +4.0 | -0.8 | 34 |
| 9 | Kyrie Irving | DAL | +2.6 | +2.6 | +0.0 | 26 |
| 10 | Dyson Daniels | ATL | +2.4 | +1.2 | +1.2 | 27 |
| 11 | Chet Holmgren | OKC | +2.4 | +0.4 | +2.0 | 29 |
| 12 | Jimmy Butler III | GSW | +2.2 | +2.1 | +0.1 | 27 |
| 13 | Ausar Thompson | DET | +2.2 | +0.1 | +2.1 | 26 |
| 14 | Lauri Markkanen | UTA | +2.2 | +1.7 | +0.5 | 32 |
| 15 | Franz Wagner | ORL | +2.1 | +0.8 | +1.3 | 30 |
| 16 | Fred VanVleet | HOU | +2.1 | +1.4 | +0.7 | 35 |
| 17 | Derrick White | BOS | +2.0 | +0.3 | +1.7 | 36 |
| 18 | Rudy Gobert | MIN | +1.7 | -3.0 | +4.7 | 29 |
| 19 | Jarrett Allen | CLE | +1.7 | +1.0 | +0.7 | 28 |
| 20 | Pascal Siakam | IND | +1.7 | +1.6 | +0.1 | 31 |
| 21 | Bam Adebayo | MIA | +1.6 | +1.0 | +0.6 | 31 |
| 22 | Kevin Durant | HOU | +1.6 | +3.1 | -1.5 | 37 |
| 23 | Cade Cunningham | DET | +1.6 | +1.7 | -0.1 | 35 |
| 24 | Nickeil Alexander-Walker | ATL | +1.5 | +1.7 | -0.2 | 31 |
| 25 | LaMelo Ball | MIN | +1.3 | +3.7 | -2.4 | 28 |
| 26 | Jrue Holiday | POR | +1.3 | +0.3 | +1.0 | 30 |
| 27 | OG Anunoby | NYK | +1.2 | -0.2 | +1.4 | 34 |
| 28 | Donovan Mitchell | CLE | +1.2 | +1.7 | -0.5 | 35 |
| 29 | Ty Jerome | MEM | +1.2 | +2.8 | -1.6 | 29 |
| 30 | Damian Lillard | POR | +1.2 | +1.9 | -0.7 | 27 |

## Current model fit

- Fitted on 5318 games from 2022-23 to 2026-27.
- Home court: +2.0 points per 100 possessions for the home team over the visitor (about 2.0 points a game).
- Second night of a back-to-back: -0.7 points per 100 scored, +1.2 allowed.
- Weights: team efficiency ratings 0.16 (offense) and 0.16 (defense); player lineup ratings 0.76 and 0.75.
- Blend: 82% on the betting line for the margin and 100% for the total, wherever there is a line (fitted on past closing lines).
- Simulator: each team's points vary by 10.9 with correlation 0.23; 5.1% of recent games went to overtime.
