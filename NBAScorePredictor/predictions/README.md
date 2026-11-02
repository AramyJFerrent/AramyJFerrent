# NBA score predictions

Updated Mon Nov 02, 2026 05:24 PM ET. Refreshed automatically several times a day during the season, around the injury report's deadlines; each game's prediction is locked at tip-off and graded once the final score is in.

Each team's expected points are its expected possessions times its expected points per possession, from team efficiency ratings and the ratings of the players expected to play, blended with the betting line. Each game is then simulated 10,000 times, overtime included. The predicted score is the expected points rounded; the 80% range holds 80% of simulated outcomes for each team. Basketball is the most predictable major sport, but a team's score still varies by about ±14 points around the forecast, so read the win chance and the ranges too.

Missing players come from the injury report: out players are left out, and doubtful, questionable and probable ones count with the share of their minutes their chance of playing implies, and their minutes go mostly to the bench. The effect is how many points of margin the team gains or loses against its full-strength roster: negative when it is missing good players, positive when the minutes go to better ones. Predictions are rerun when the report changes, up to tip-off.

The fair moneyline is the American odds that match the win chance exactly, with no bookmaker margin: -150 means risk $150 to win $100, +150 means risk $100 to win $150.

The edge columns check every side of the spread, the moneyline and the total for expected value: the profit per $1 bet at the posted price, using the final prediction's chances (the model blended with the line, simulated against the posted lines, pushes returning the stake, and anchored to the market's own chances so only what the blend moves off the line counts). The model's own spread and total are shown alongside, but the blend keeps only the share of that disagreement the model has earned in past seasons, so edges are rare. A side is an edge when its EV is 3% or more; the best such side is shown with its price, its EV, its chance of winning the bet and its stake, a 25% share of the Kelly stake in units of 1% of the bankroll, with at most 3 units on one game. Where a spread or total price is not posted it is assumed to be -110 (marked \*); a moneyline is never assumed. Edges are logged with each prediction, locked at tip-off and graded below. Treat them as an experiment, not betting advice; see the backtest for how they have done on past seasons.

## Monday, November 2

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Spread: model / line | Total: model / line | 80% range | Overtime | Missing (effect on margin) | Spread edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 7:00 PM | OKC @ CLE | OKC 112, CLE 117 | CLE 64% | OKC +175 / CLE -175<br>posted OKC +142 / CLE -170 | CLE -4.6 / CLE -4.5 (fav covers 52%) | 229.3 / 229.5 (over 49%) | 98–127 / 103–131 | 4% | OKC: Chet Holmgren (out); Jalen Williams (out); Alex Caruso (out); Cason Wallace (out) (-2.5)<br>CLE: Peyton Watson (day-to-day); Jaylon Tyson (out) (+0.2) | no edge | no edge | no edge |
| 7:30 PM | DET @ CHA | DET 108, CHA 102 | DET 68% | DET -210 / CHA +210<br>posted DET -229 / CHA +189 | DET -5.7 / DET -5.5 (fav covers 53%) | 209.8 / 209.5 (over 49%) | 94–122 / 88–116 | 5% | DET: Jalen Duren (out) (-0.2)<br>CHA: Kon Knueppel (out); Grant Williams (out) (-0.6) | no edge | no edge | no edge |
| 7:30 PM | ATL @ IND | ATL 120, IND 110 | ATL 76% | ATL -325 / IND +325<br>posted ATL -423 / IND +331 | ATL -9.8 / ATL -10.5 (fav covers 48%) | 229.4 / 229.5 (over 49%) | 105–134 / 95–124 | 4% | ATL: Jalen Johnson (day-to-day); Kingston Flemings (suspension) (+2.3)<br>IND: Pascal Siakam (out); Andrew Nembhard (out); Tyrese Haliburton (out); Aaron Nesmith (out); Obi Toppin (day-to-day); Johnny Furphy (out); Larry Nance Jr. (day-to-day); Ben Sheppard (out); T.J. McConnell (out); Ivica Zubac (out) (-3.4) | no edge | IND ML (+331): EV +3.9%, 24%, stake 0.3u | no edge |
| 7:30 PM | BKN @ NYK | BKN 102, NYK 116 | NYK 86% | BKN +610 / NYK -610<br>posted BKN +670 / NYK -1040 | NYK -14.2 / NYK -14.5 (fav covers 47%) | 218.2 / 218.5 (over 49%) | 88–116 / 102–130 | 3% | BKN: Egor Demin (out) (+0.8)<br>NYK: Jose Alvarado (out) (-0.3) | no edge | no edge | no edge |
| 7:30 PM | WAS @ ORL | WAS 111, ORL 114 | ORL 59% | WAS +145 / ORL -145<br>posted WAS +131 / ORL -155 | ORL -3 / ORL -2.5 (fav covers 53%) | 225.5 / 225.5 (over 50%) | 97–126 / 100–128 | 5% | WAS: Jamir Watkins (out); Alex Sarr (out); Justin Champagnie (out); Tristan Vukcevic (out) (-0.2)<br>ORL: Paolo Banchero (out); Jalen Suggs (out); Anthony Black (out) (+0.5) | no edge | no edge | no edge |
| 7:30 PM | CHI @ PHI | CHI 114, PHI 124 | PHI 77% | CHI +330 / PHI -330<br>posted CHI +396 / PHI -522 | PHI -9.9 / PHI -9.5 (fav covers 51%) | 238.1 / 238.5 (over 48%) | 99–129 / 110–138 | 4% | CHI: Jalen Smith (day-to-day); Nic Claxton (out) (-0.3)<br>PHI: Joel Embiid (day-to-day); Dominick Barlow (out) (-0.5) | no edge | no edge | no edge |
| 8:00 PM | SAC @ DAL | SAC 111, DAL 120 | DAL 74% | SAC +290 / DAL -290<br>posted SAC +276 / DAL -344 | DAL -8.8 / DAL -8.5 (fav covers 51%) | 231.3 / 231.5 (over 48%) | 97–126 / 106–134 | 4% | SAC: Maxime Raynaud (out); Zach LaVine (day-to-day); Keegan Murray (out); Dylan Cardwell (out) (+0.0)<br>DAL: Kyrie Irving (day-to-day); Santi Aldama (out); Dereck Lively II (out); Sergio de Larrea (out) (+0.3) | no edge | no edge | no edge |
| 8:00 PM | NOP @ MEM | NOP 114, MEM 119 | MEM 65% | NOP +190 / MEM -190<br>posted NOP +169 / MEM -203 | MEM -5.3 / MEM -5.5 (fav covers 51%) | 232.4 / 232.5 (over 49%) | 99–129 / 104–133 | 5% | NOP: Dejounte Murray (day-to-day); Yves Missi (out); Jordan Poole (out) (+0.5)<br>MEM: Scotty Pippen Jr. (day-to-day); Quinten Post (day-to-day) (+0.1) | no edge | no edge | no edge |
| 8:00 PM | MIL @ MIN | MIL 110, MIN 121 | MIN 79% | MIL +375 / MIN -375<br>posted MIL +331 / MIN -423 | MIN -10.8 / MIN -10.5 (fav covers 50%) | 230.2 / 230.5 (over 49%) | 95–125 / 106–135 | 4% | MIN: Anthony Edwards (out); LaMelo Ball (day-to-day); Terrence Shannon Jr. (day-to-day); Donte DiVincenzo (out) (-1.3) | no edge | no edge | no edge |
| 8:30 PM | BOS @ HOU | BOS 106, HOU 110 | HOU 63% | BOS +170 / HOU -170<br>posted BOS +160 / HOU -191 | HOU -4.3 / HOU -4.5 (fav covers 51%) | 215.6 / 215.5 (over 49%) | 91–120 / 96–124 | 5% | BOS: Devin Carter (out); Paul George (out) (+0.3)<br>HOU: Reed Sheppard (day-to-day); Steven Adams (out); Clint Capela (out) (-0.1) | no edge | no edge | no edge |
| 8:30 PM | UTA @ SAS | UTA 106, SAS 122 | SAS 89% | UTA +790 / SAS -790<br>posted UTA +740 / SAS -1180 | SAS -16.7 / SAS -16.5 (fav covers 48%) | 227.7 / 228.5 (over 47%) | 91–120 / 108–136 | 3% | UTA: Jaren Jackson Jr. (out); Trey Alexander (out); Jusuf Nurkic (out) (-0.9)<br>SAS: Tobias Harris (out) (+0.8) | no edge | no edge | no edge |
| 9:00 PM | POR @ DEN | POR 114, DEN 118 | DEN 62% | POR +165 / DEN -165<br>posted POR +146 / DEN -174 | DEN -4.3 / DEN -4.5 (fav covers 51%) | 231.7 / 231.5 (over 50%) | 99–129 / 103–133 | 5% | POR: Ja Morant (out) (-0.5)<br>DEN: Spencer Jones (out); Alpha Diallo (out) (+2.2) | no edge | no edge | no edge |
| 10:00 PM | PHX @ GSW | PHX 113, GSW 115 | GSW 57% | PHX +130 / GSW -130<br>posted PHX +120 / GSW -142 | GSW -2.1 / GSW -2.5 (fav covers 51%) | 227.9 / 227.5 (over 50%) | 98–127 / 100–130 | 6% | PHX: Mark Williams (out) (+0.4)<br>GSW: Moses Moody (out); Jimmy Butler III (out); Kristaps Porzingis (out); Brandon Williams (day-to-day); Al Horford (out); Gui Santos (out) (-1.7) | no edge | no edge | no edge |
| 10:00 PM | TOR @ LAC | TOR 112, LAC 108 | TOR 62% | TOR -165 / LAC +165<br>posted TOR -180 / LAC +151 | TOR -4.1 / TOR -4.5 (fav covers 50%) | 219.6 / 219.5 (over 49%) | 98–126 / 93–123 | 6% | TOR: Scottie Barnes (day-to-day); Kawhi Leonard (out); Jakob Poeltl (day-to-day) (-2.3)<br>LAC: Rui Hachimura (out); Derrick Jones Jr. (out); Brandon Ingram (out); Jordan Miller (out); Bradley Beal (out); Yanic Konan Niederhauser (out) (-1.0) | no edge | no edge | no edge |
| 10:00 PM | MIA @ LAL | MIA 117, LAL 119 | LAL 57% | MIA +135 / LAL -135<br>posted MIA +114 / LAL -135 | LAL -2.3 / LAL -2.5 (fav covers 51%) | 236.6 / 236.5 (over 49%) | 102–132 / 105–134 | 4% | – | no edge | no edge | no edge |

## Wednesday, November 4

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Spread: model / line | Total: model / line | 80% range | Overtime | Missing (effect on margin) | Spread edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 7:00 PM | PHI @ DET | PHI 106, DET 111 | DET 67% | PHI +200 / DET -200 | DET -5.7 | 217.2 | 92–120 / 97–126 | 5% | PHI: Joel Embiid (day-to-day); Dominick Barlow (out) (-0.5)<br>DET: Jalen Duren (out) (-0.2) | no line yet | no line yet | no line yet |
| 7:00 PM | ATL @ WAS | ATL 119, WAS 115 | ATL 62% | ATL -160 / WAS +160 | ATL -3.9 | 233.8 | 104–133 / 100–130 | 5% | ATL: Jalen Johnson (day-to-day); Kingston Flemings (suspension) (+2.3)<br>WAS: Jamir Watkins (out); Alex Sarr (out); Justin Champagnie (out); Tristan Vukcevic (out) (-0.2) | no line yet | no line yet | no line yet |
| 7:30 PM | MIL @ BOS | MIL 106, BOS 123 | BOS 89% | MIL +780 / BOS -780 | BOS -16.4 | 229.2 | 92–121 / 108–137 | 3% | BOS: Devin Carter (out); Paul George (out) (+0.4) | no line yet | no line yet | no line yet |
| 7:30 PM | CHA @ BKN | CHA 107, BKN 108 | BKN 50% | CHA +100 / BKN -100 | pick'em | 215.0 | 94–121 / 93–122 | 5% | CHA: Kon Knueppel (out); Grant Williams (out) (-0.6)<br>BKN: Egor Demin (out) (+0.7) | no line yet | no line yet | no line yet |
| 7:30 PM | CHI @ NYK | CHI 111, NYK 124 | NYK 82% | CHI +450 / NYK -450 | NYK -12.7 | 234.8 | 96–126 / 110–138 | 4% | CHI: Jalen Smith (day-to-day); Nic Claxton (out) (-0.3)<br>NYK: Jose Alvarado (out) (-0.3) | no line yet | no line yet | no line yet |
| 8:00 PM | IND @ MEM | IND 111, MEM 117 | MEM 69% | IND +220 / MEM -220 | MEM -6.7 | 228.1 | 96–125 / 103–132 | 4% | IND: Pascal Siakam (out); Andrew Nembhard (out); Tyrese Haliburton (out); Aaron Nesmith (out); Obi Toppin (day-to-day); Johnny Furphy (out); Larry Nance Jr. (day-to-day); Ben Sheppard (out); T.J. McConnell (out); Ivica Zubac (out) (-3.3)<br>MEM: Scotty Pippen Jr. (day-to-day); Quinten Post (day-to-day) (+0.1) | no line yet | no line yet | no line yet |
| 8:00 PM | UTA @ NOP | UTA 114, NOP 119 | NOP 65% | UTA +185 / NOP -185 | NOP -5 | 232.3 | 99–128 / 104–133 | 5% | UTA: Jaren Jackson Jr. (out); Trey Alexander (out); Jusuf Nurkic (out) (-1.0)<br>NOP: Dejounte Murray (day-to-day); Yves Missi (out); Jordan Poole (out) (+0.5) | no line yet | no line yet | no line yet |
| 8:00 PM | CLE @ OKC | CLE 113, OKC 114 | OKC 51% | CLE +100 / OKC -100 | pick'em | 226.1 | 98–128 / 99–128 | 6% | CLE: Peyton Watson (day-to-day); Jaylon Tyson (out) (+0.2)<br>OKC: Chet Holmgren (out); Jalen Williams (out); Alex Caruso (out); Cason Wallace (out) (-2.5) | no line yet | no line yet | no line yet |
| 8:30 PM | MIN @ HOU | MIN 109, HOU 115 | HOU 69% | MIN +225 / HOU -225 | HOU -6.6 | 223.9 | 94–123 / 101–130 | 4% | MIN: Anthony Edwards (out); LaMelo Ball (day-to-day); Terrence Shannon Jr. (day-to-day); Donte DiVincenzo (out) (-1.3)<br>HOU: Reed Sheppard (day-to-day); Steven Adams (out); Clint Capela (out) (-0.1) | no line yet | no line yet | no line yet |
| 9:00 PM | TOR @ DEN | TOR 112, DEN 118 | DEN 68% | TOR +215 / DEN -215 | DEN -6.3 | 230.1 | 97–127 / 104–133 | 5% | TOR: Scottie Barnes (day-to-day); Kawhi Leonard (out); Jakob Poeltl (day-to-day) (-2.3)<br>DEN: Spencer Jones (out); Alpha Diallo (out) (+2.3) | no line yet | no line yet | no line yet |
| 9:00 PM | POR @ PHX | POR 116, PHX 115 | POR 52% | POR -110 / PHX +110 | POR -0.7 | 230.5 | 101–130 / 100–130 | 5% | POR: Ja Morant (out) (-0.5)<br>PHX: Mark Williams (out) (+0.4) | no line yet | no line yet | no line yet |
| 9:30 PM | DAL @ SAS | DAL 107, SAS 117 | SAS 78% | DAL +350 / SAS -350 | SAS -10 | 224.1 | 93–122 / 103–131 | 4% | DAL: Kyrie Irving (day-to-day); Santi Aldama (out); Dereck Lively II (out); Sergio de Larrea (out) (+0.3)<br>SAS: Tobias Harris (out) (+0.8) | no line yet | no line yet | no line yet |
| 10:00 PM | LAL @ SAC | LAL 123, SAC 114 | LAL 74% | LAL -285 / SAC +285 | LAL -9.1 | 237.1 | 109–138 / 99–129 | 4% | SAC: Maxime Raynaud (out); Zach LaVine (day-to-day); Keegan Murray (out); Dylan Cardwell (out) (+0.0) | no line yet | no line yet | no line yet |
| 10:30 PM | MIA @ LAC | MIA 118, LAC 114 | MIA 60% | MIA -150 / LAC +150 | MIA -3.7 | 232.1 | 103–132 / 100–129 | 5% | LAC: Rui Hachimura (out); Derrick Jones Jr. (out); Brandon Ingram (out); Jordan Miller (out); Bradley Beal (out); Yanic Konan Niederhauser (out) (-1.0) | no line yet | no line yet | no line yet |

## How the 2026-27 predictions have done

| Predictor | Games | Margin MAE | Total MAE | Team-points MAE | Log loss | Brier | Winners | 80% range hit |
|---|---|---|---|---|---|---|---|---|
| Final prediction | 92 | 11.33 | 15.48 | 9.86 | 0.579 | 0.199 | 68.5% | 79.3% |
| Model only (before blending) | 92 | 11.90 | 15.11 | 10.01 | 0.609 | 0.212 | 65.2% | – |
| Elo | 92 | 12.37 | – | – | 0.650 | 0.230 | 58.7% | – |
| Final prediction, games with a line | 92 | 11.33 | 15.48 | 9.86 | 0.579 | 0.199 | 68.5% | 79.3% |
| Model only, games with a line | 92 | 11.90 | 15.11 | 10.01 | 0.609 | 0.212 | 65.2% | – |
| Betting line | 92 | 11.24 | 15.45 | 9.82 | 0.567 | 0.194 | 68.5% | – |

MAE is the average miss in points; team-points MAE is the average miss on each team's score. Log loss and Brier score the win chances (lower is better; a coin flip scores 0.693 and 0.250). The closing line misses margins by about 10 points and totals by about 14.

Overtime: predicted in 4.8% of games, happened in 4.3%.

### Betting edges

| Market | Edges | Record (W-L-P) | Staked | Units won | ROI | Expected ROI |
|---|---|---|---|---|---|---|
| Spread | 1 | 1-0-0 | 1.0 | +0.90 | +89.3% | +3.6% |
| Moneyline | 5 | 0-5-0 | 1.9 | -1.88 | -100.0% | +8.8% |
| Total | 0 | 0-0-0 | 0.0 | +0.00 | – | – |

Spread moved toward the model's first spread edge before tip-off: 4 of 5 games (80%).

Live predictions only, each edge at the stake and price logged with the last prediction before tip-off (edges logged before edges were priced from the final prediction are left out); a push returns the stake. Units are 1% of the bankroll; ROI is units won per unit staked, and expected ROI is what the edges' EVs promised. The line moving toward the model's edge before tip-off is the quickest sign that it knows something the market doesn't yet.

### Results, Sunday, November 1

| Game | Predicted | Final | Win chance for winner | Spread: model / line | Inside 80% ranges |
|---|---|---|---|---|---|
| BOS @ ORL | 114–107 | 108–97 | 70% | BOS -6.7 / BOS -7.5 | yes |
| BKN @ IND | 114–117 | 98–90 | 40% | IND -3.5 / IND -3.5 | no |
| LAC @ GSW | 110–111 | 112–124 | 55% | GSW -1.6 / GSW -1.5 | yes |
| TOR @ LAL | 110–114 | 125–131 | 61% | LAL -3.6 / LAL -3.5 | no |

## Power ratings

Points per 100 possessions better than an average team on a neutral floor, combining opponent-adjusted team efficiency (garbage time removed) with the ratings of the team's healthy roster, through the fitted points map. Net per game uses the team's pace. Injury effect now is what its current injury report does to its margin, in points.

| # | Team | Net per 100 | Net per game | Offense | Defense | Pace | Injury effect now | Elo |
|---|---|---|---|---|---|---|---|---|
| 1 | HOU | +7.0 | +7.0 | +3.6 | +3.4 | 100.1 | -0.1 | 1623 |
| 2 | SAS | +6.8 | +7.0 | +2.2 | +4.6 | 102.1 | +0.8 | 1692 |
| 3 | BOS | +6.1 | +6.0 | +3.3 | +2.8 | 98.5 | +0.3 | 1629 |
| 4 | DET | +5.8 | +5.9 | +1.5 | +4.4 | 100.2 | -0.2 | 1647 |
| 5 | NYK | +4.0 | +4.0 | +1.2 | +2.8 | 99.0 | -0.3 | 1686 |
| 6 | MIN | +3.6 | +3.8 | +1.5 | +2.1 | 104.5 | -1.3 | 1598 |
| 7 | POR | +2.9 | +2.9 | +1.8 | +1.1 | 102.2 | -0.6 | 1537 |
| 8 | OKC | +2.6 | +2.7 | -0.8 | +3.4 | 100.6 | -2.5 | 1660 |
| 9 | LAL | +2.5 | +2.5 | +2.7 | -0.2 | 102.8 | +0.3 | 1578 |
| 10 | PHI | +2.3 | +2.4 | -0.2 | +2.5 | 102.0 | -0.5 | 1570 |
| 11 | CLE | +2.0 | +2.0 | +2.3 | -0.3 | 102.3 | +0.2 | 1585 |
| 12 | GSW | +2.0 | +2.0 | +1.6 | +0.4 | 101.1 | -1.7 | 1501 |
| 13 | TOR | +1.8 | +1.9 | +0.5 | +1.4 | 105.1 | -2.4 | 1547 |
| 14 | DEN | +1.6 | +1.6 | +2.9 | -1.3 | 99.0 | +2.2 | 1579 |
| 15 | MIA | +0.9 | +0.9 | +1.9 | -1.1 | 106.9 | +0.0 | 1501 |
| 16 | ORL | +0.4 | +0.4 | -1.3 | +1.6 | 100.5 | +0.5 | 1526 |
| 17 | DAL | -0.3 | -0.3 | -0.2 | -0.1 | 103.1 | +0.3 | 1456 |
| 18 | PHX | -0.6 | -0.6 | +1.5 | -2.1 | 101.6 | +0.4 | 1498 |
| 19 | MEM | -0.8 | -0.8 | +0.5 | -1.2 | 103.2 | +0.1 | 1426 |
| 20 | ATL | -1.0 | -1.0 | -0.5 | -0.5 | 107.1 | +2.3 | 1533 |
| 21 | IND | -2.2 | -2.2 | -0.1 | -2.1 | 101.0 | -3.3 | 1357 |
| 22 | CHA | -3.1 | -3.0 | -3.4 | +0.3 | 95.1 | -0.6 | 1523 |
| 23 | NOP | -3.6 | -3.8 | -1.8 | -1.8 | 107.5 | +0.5 | 1434 |
| 24 | LAC | -3.7 | -3.7 | -1.7 | -1.9 | 99.7 | -1.0 | 1489 |
| 25 | WAS | -4.5 | -4.6 | -2.5 | -2.0 | 102.5 | -0.2 | 1325 |
| 26 | UTA | -4.9 | -5.0 | -3.4 | -1.5 | 102.4 | -0.9 | 1309 |
| 27 | CHI | -6.0 | -6.8 | -3.1 | -3.0 | 113.2 | -0.3 | 1363 |
| 28 | BKN | -6.2 | -6.5 | -3.5 | -2.7 | 103.6 | +0.8 | 1304 |
| 29 | MIL | -7.5 | -8.0 | -2.8 | -4.7 | 106.6 | +0.0 | 1347 |
| 30 | SAC | -8.0 | -8.5 | -3.6 | -4.4 | 106.5 | +0.0 | 1325 |

## Top players

Regularized adjusted plus-minus from every lineup this season and past ones: points per 100 possessions a player adds on offense and saves on defense, against an average player, shrunk toward last season's rating. Players expected to play 20 minutes or more.

| # | Player | Team | Net impact per 100 | Offense | Defense | Expected minutes |
|---|---|---|---|---|---|---|
| 1 | Victor Wembanyama | SAS | +6.4 | +1.7 | +4.7 | 34 |
| 2 | Shai Gilgeous-Alexander | OKC | +5.8 | +5.0 | +0.8 | 31 |
| 3 | Nikola Jokic | DEN | +5.1 | +5.4 | -0.3 | 37 |
| 4 | Kawhi Leonard | TOR | +4.5 | +3.6 | +0.9 | 30 |
| 5 | Luka Doncic | LAL | +4.1 | +5.2 | -1.1 | 36 |
| 6 | Giannis Antetokounmpo | MIA | +3.8 | +3.9 | -0.1 | 31 |
| 7 | Kyrie Irving | DAL | +3.5 | +3.3 | +0.1 | 31 |
| 8 | Joel Embiid | PHI | +3.1 | +1.5 | +1.6 | 35 |
| 9 | Herbert Jones | NOP | +2.6 | -0.3 | +2.9 | 23 |
| 10 | Fred VanVleet | HOU | +2.5 | +1.8 | +0.7 | 32 |
| 11 | Marcus Smart | HOU | +2.5 | +1.3 | +1.2 | 24 |
| 12 | Franz Wagner | ORL | +2.4 | +1.1 | +1.3 | 37 |
| 13 | Jimmy Butler III | GSW | +2.2 | +2.1 | +0.1 | 27 |
| 14 | Chet Holmgren | OKC | +2.1 | +0.0 | +2.0 | 30 |
| 15 | Lauri Markkanen | UTA | +2.0 | +1.7 | +0.2 | 26 |
| 16 | Jarrett Allen | CLE | +2.0 | +1.2 | +0.7 | 27 |
| 17 | Ausar Thompson | DET | +2.0 | -0.3 | +2.2 | 27 |
| 18 | Ty Jerome | MEM | +1.9 | +3.3 | -1.4 | 28 |
| 19 | Derrick White | BOS | +1.8 | +0.2 | +1.6 | 31 |
| 20 | Bam Adebayo | MIA | +1.8 | +1.4 | +0.4 | 32 |
| 21 | Rudy Gobert | MIN | +1.8 | -3.3 | +5.1 | 28 |
| 22 | Cade Cunningham | DET | +1.8 | +1.6 | +0.1 | 33 |
| 23 | Neemias Queta | BOS | +1.7 | +0.8 | +0.9 | 22 |
| 24 | Dyson Daniels | ATL | +1.7 | +0.7 | +1.0 | 28 |
| 25 | LaMelo Ball | MIN | +1.6 | +3.8 | -2.1 | 25 |
| 26 | Kevin Durant | HOU | +1.5 | +3.2 | -1.7 | 32 |
| 27 | Donovan Mitchell | CLE | +1.5 | +2.3 | -0.8 | 30 |
| 28 | Pascal Siakam | IND | +1.5 | +1.6 | -0.2 | 33 |
| 29 | Stephen Curry | GSW | +1.4 | +4.1 | -2.7 | 30 |
| 30 | Dean Wade | PHI | +1.3 | -0.2 | +1.5 | 26 |

## Current model fit

- Fitted on 5374 games from 2022-23 to 2026-27.
- Home court: +2.0 points per 100 possessions for the home team over the visitor (about 2.0 points a game).
- Second night of a back-to-back: -0.7 points per 100 scored, +1.2 allowed.
- Weights: team efficiency ratings 0.16 (offense) and 0.15 (defense); player lineup ratings 0.76 and 0.76.
- Blend: 82% on the betting line for the margin and 100% for the total, wherever there is a line (fitted on past closing lines).
- Simulator: each team's points vary by 11.0 with correlation 0.23; 5.1% of recent games went to overtime.
