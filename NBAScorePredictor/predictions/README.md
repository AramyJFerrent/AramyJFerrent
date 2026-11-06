# NBA score predictions

Updated Fri Nov 06, 2026 02:38 AM ET. Refreshed automatically several times a day during the season, around the injury report's deadlines; each game's prediction is locked at tip-off and graded once the final score is in.

Each team's expected points are its expected possessions times its expected points per possession, from team efficiency ratings and the ratings of the players expected to play, blended with the betting line. Each game is then simulated 10,000 times, overtime included. The predicted score is the expected points rounded; the 80% range holds 80% of simulated outcomes for each team. Basketball is the most predictable major sport, but a team's score still varies by about ±14 points around the forecast, so read the win chance and the ranges too.

Missing players come from the injury report: out players are left out, and doubtful, questionable and probable ones count with the share of their minutes their chance of playing implies, and their minutes go mostly to the bench. The effect is how many points of margin the team gains or loses against its full-strength roster: negative when it is missing good players, positive when the minutes go to better ones. Predictions are rerun when the report changes, up to tip-off.

The fair moneyline is the American odds that match the win chance exactly, with no bookmaker margin: -150 means risk $150 to win $100, +150 means risk $100 to win $150.

The edge columns check every side of the spread, the moneyline and the total for expected value: the profit per $1 bet at the posted price, using the final prediction's chances (the model blended with the line, simulated against the posted lines, pushes returning the stake, and anchored to the market's own chances so only what the blend moves off the line counts). The model's own spread and total are shown alongside, but the blend keeps only the share of that disagreement the model has earned in past seasons, so edges are rare. A side is an edge when its EV is 3% or more; the best such side is shown with its price, its EV, its chance of winning the bet and its stake, a 25% share of the Kelly stake in units of 1% of the bankroll, with at most 3 units on one game. Where a spread or total price is not posted it is assumed to be -110 (marked \*); a moneyline is never assumed. Edges are logged with each prediction, locked at tip-off and graded below. Treat them as an experiment, not betting advice; see the backtest for how they have done on past seasons.

## Friday, November 6

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Spread: model / line | Total: model / line | 80% range | Overtime | Missing (effect on margin) | Spread edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 7:00 PM | WAS @ ATL | WAS 112, ATL 119 | ATL 69% | WAS +225 / ATL -225<br>posted WAS +199 / ATL -241 | ATL -6.8 / ATL -6.5 (fav covers 52%) | 230.5 / 230.5 (over 49%) | 97–127 / 104–133 | 5% | WAS: Anthony Davis (day-to-day); Jamir Watkins (out); Justin Champagnie (out); Tristan Vukcevic (out) (-0.5)<br>ATL: Jalen Johnson (day-to-day); Keshon Gilbert (out) (+2.0) | no edge | no edge | no edge |
| 7:00 PM | BOS @ CHA | BOS 110, CHA 101 | BOS 75% | BOS -310 / CHA +310<br>posted BOS -344 / CHA +276 | BOS -8.8 / BOS -8.5 (fav covers 51%) | 210.6 / 210.5 (over 49%) | 96–123 / 87–115 | 5% | BOS: Devin Carter (out); Payton Pritchard (day-to-day) (+1.1)<br>CHA: Moussa Diabate (day-to-day); Dennis Schroder (day-to-day); Kon Knueppel (out); Grant Williams (out) (-0.8) | no edge | no edge | no edge |
| 7:30 PM | PHI @ CLE | PHI 115, CLE 113 | PHI 56% | PHI -130 / CLE +130<br>posted PHI -142 / CLE +120 | PHI -2.1 / PHI -2.5 (fav covers 50%) | 228.6 / 228.5 (over 49%) | 101–130 / 99–128 | 5% | PHI: Adem Bona (day-to-day); Dominick Barlow (out) (+0.4)<br>CLE: Peyton Watson (day-to-day); Jarrett Allen (day-to-day); Jaylon Tyson (out); Tyrese Proctor (day-to-day) (+0.2) | no edge | no edge | no edge |
| 8:00 PM | UTA @ DAL | UTA 110, DAL 117 | DAL 71% | UTA +240 / DAL -240<br>posted UTA +208 / DAL -253 | DAL -7.3 / DAL -7.5 (fav covers 50%) | 226.5 / 226.5 (over 49%) | 95–124 / 102–131 | 4% | UTA: Jaren Jackson Jr. (out); Trey Alexander (out); Jusuf Nurkic (out) (-0.7)<br>DAL: Santi Aldama (out); Max Christie (day-to-day); Dereck Lively II (out); Sergio de Larrea (out) (+1.1) | no edge | no edge | no edge |
| 8:00 PM | OKC @ MEM | OKC 114, MEM 111 | OKC 60% | OKC -150 / MEM +150<br>posted OKC -152 / MEM +128 | OKC -3.3 / OKC -3.5 (fav covers 51%) | 225.6 / 225.5 (over 49%) | 100–129 / 97–126 | 5% | OKC: Chet Holmgren (out); Jalen Williams (out); Jaylin Williams (out); Cason Wallace (out) (-0.1)<br>MEM: Isaiah Stewart (out); Scotty Pippen Jr. (out) (-0.1) | no edge | no edge | no edge |
| 8:00 PM | TOR @ MIL | TOR 118, MIL 112 | TOR 67% | TOR -200 / MIL +200<br>posted TOR -249 / MIL +206 | TOR -5.8 / TOR -6.5 (fav covers 49%) | 230.6 / 230.5 (over 49%) | 104–133 / 98–127 | 5% | TOR: Scottie Barnes (day-to-day); Kawhi Leonard (out) (-2.2)<br>MIL: Kam Jones (out) (+0.6) | no edge | no edge | no edge |
| 8:00 PM | MIN @ NOP | MIN 118, NOP 113 | MIN 63% | MIN -170 / NOP +170<br>posted MIN -184 / NOP +154 | MIN -4.6 / MIN -4.5 (fav covers 52%) | 230.6 / 230.5 (over 50%) | 103–132 / 98–128 | 5% | MIN: Anthony Edwards (out); Terrence Shannon Jr. (day-to-day); Donte DiVincenzo (out) (-0.5)<br>NOP: Trey Murphy III (day-to-day); Yves Missi (out) (+0.3) | no edge | no edge | no edge |
| 10:00 PM | POR @ LAL | POR 115, LAL 117 | LAL 57% | POR +130 / LAL -130<br>posted POR +124 / LAL -148 | LAL -2.3 / LAL -2.5 (fav covers 51%) | 231.8 / 231.5 (over 49%) | 100–130 / 102–132 | 6% | POR: Ja Morant (out) (+0.0)<br>LAL: Sandro Mamukelashvili (day-to-day) (+0.0) | no edge | no edge | no edge |
| 10:00 PM | SAS @ SAC | SAS 122, SAC 107 | SAS 86% | SAS -635 / SAC +635<br>posted SAS -990 / SAC +650 | SAS -15.1 / SAS -15.5 (fav covers 46%) | 228.8 / 229.5 (over 48%) | 108–136 / 92–122 | 3% | SAS: Tobias Harris (out) (+0.7)<br>SAC: Maxime Raynaud (out); Keegan Murray (out) (+0.0) | no edge | no edge | no edge |

## Saturday, November 7

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Spread: model / line | Total: model / line | 80% range | Overtime | Missing (effect on margin) | Spread edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 5:00 PM | DEN @ IND | DEN 117, IND 110 | DEN 68% | DEN -215 / IND +215 | DEN -6.2 | 227.0 | 102–131 / 96–125 | 5% | DEN: Spencer Jones (out); DeMar DeRozan (day-to-day) (+1.3)<br>IND: Tyrese Haliburton (out); Johnny Furphy (out); Ben Sheppard (out); T.J. McConnell (out); Kelly Oubre Jr. (day-to-day) (-0.4) | no line yet | no line yet | no line yet |
| 7:30 PM | BKN @ ATL | BKN 113, ATL 118 | ATL 66% | BKN +195 / ATL -195 | ATL -5.7 | 231.3 | 98–128 / 104–133 | 5% | BKN: Day'Ron Sharpe (day-to-day); Noah Clowney (day-to-day); Egor Demin (out) (+0.5)<br>ATL: Jalen Johnson (day-to-day); Keshon Gilbert (out) (+2.0) | no line yet | no line yet | no line yet |
| 8:00 PM | NYK @ CLE | NYK 114, CLE 111 | NYK 56% | NYK -125 / CLE +125 | NYK -2.1 | 224.9 | 99–128 / 97–126 | 5% | NYK: Josh Hart (day-to-day) (-0.1)<br>CLE: Peyton Watson (day-to-day); Jarrett Allen (day-to-day); Jaylon Tyson (out); Tyrese Proctor (day-to-day) (+0.2) | no line yet | no line yet | no line yet |
| 8:00 PM | WAS @ OKC | WAS 106, OKC 116 | OKC 78% | WAS +355 / OKC -355 | OKC -10.6 | 222.3 | 92–120 / 102–130 | 4% | WAS: Anthony Davis (day-to-day); Jamir Watkins (out); Justin Champagnie (out); Tristan Vukcevic (out) (-0.5)<br>OKC: Chet Holmgren (out); Jalen Williams (out); Jaylin Williams (out); Cason Wallace (out) (-0.1) | no line yet | no line yet | no line yet |
| 8:30 PM | ORL @ GSW | ORL 110, GSW 113 | GSW 60% | ORL +150 / GSW -150 | GSW -3.4 | 223.3 | 96–124 / 99–128 | 5% | ORL: Paolo Banchero (out); Jalen Suggs (out) (+0.4)<br>GSW: Moses Moody (out); Jimmy Butler III (out); Kristaps Porzingis (out); Gui Santos (day-to-day) (-1.1) | no line yet | no line yet | no line yet |
| 9:00 PM | HOU @ PHX | HOU 117, PHX 112 | HOU 66% | HOU -190 / PHX +190 | HOU -5.5 | 228.6 | 103–131 / 97–126 | 4% | HOU: Steven Adams (out); Clint Capela (day-to-day) (-0.5)<br>PHX: Mark Williams (out); Jordan Goodwin (day-to-day) (+0.3) | no line yet | no line yet | no line yet |
| 10:00 PM | SAS @ POR | SAS 114, POR 113 | SAS 53% | SAS -115 / POR +115 | SAS -1.1 | 227.0 | 99–129 / 98–128 | 5% | SAS: Tobias Harris (out) (+0.7)<br>POR: Ja Morant (out) (+0.0) | no line yet | no line yet | no line yet |

## How the 2026-27 predictions have done

| Predictor | Games | Margin MAE | Total MAE | Team-points MAE | Log loss | Brier | Winners | 80% range hit |
|---|---|---|---|---|---|---|---|---|
| Final prediction | 121 | 10.91 | 14.59 | 9.37 | 0.578 | 0.198 | 68.6% | 81.4% |
| Model only (before blending) | 121 | 11.35 | 14.30 | 9.49 | 0.605 | 0.211 | 66.9% | – |
| Elo | 121 | 11.74 | – | – | 0.641 | 0.227 | 59.5% | – |
| Final prediction, games with a line | 121 | 10.91 | 14.59 | 9.37 | 0.578 | 0.198 | 68.6% | 81.4% |
| Model only, games with a line | 121 | 11.35 | 14.30 | 9.49 | 0.605 | 0.211 | 66.9% | – |
| Betting line | 121 | 10.83 | 14.58 | 9.36 | 0.566 | 0.194 | 68.6% | – |

MAE is the average miss in points; team-points MAE is the average miss on each team's score. Log loss and Brier score the win chances (lower is better; a coin flip scores 0.693 and 0.250). The closing line misses margins by about 10 points and totals by about 14.

Overtime: predicted in 4.7% of games, happened in 5.8%.

### Betting edges

| Market | Edges | Record (W-L-P) | Staked | Units won | ROI | Expected ROI |
|---|---|---|---|---|---|---|
| Spread | 1 | 1-0-0 | 1.0 | +0.90 | +89.3% | +3.6% |
| Moneyline | 6 | 0-6-0 | 2.1 | -2.06 | -100.0% | +8.3% |
| Total | 0 | 0-0-0 | 0.0 | +0.00 | – | – |

Spread moved toward the model's first spread edge before tip-off: 4 of 5 games (80%).

Live predictions only, each edge at the stake and price logged with the last prediction before tip-off (edges logged before edges were priced from the final prediction are left out); a push returns the stake. Units are 1% of the bankroll; ROI is units won per unit staked, and expected ROI is what the edges' EVs promised. The line moving toward the model's edge before tip-off is the quickest sign that it knows something the market doesn't yet.

### Results, Wednesday, November 4

| Game | Predicted | Final | Win chance for winner | Spread: model / line | Inside 80% ranges |
|---|---|---|---|---|---|
| PHI @ DET | 108–111 | 112–106 | 41% | DET -3.1 / DET -2.5 | yes |
| ATL @ WAS | 117–114 | 120–105 | 59% | ATL -3 / ATL -3.5 | yes |
| MIL @ BOS | 104–117 | 102–109 | 82% | BOS -12.2 / BOS -11.5 | yes |
| CHA @ BKN | 108–105 | 104–114 | 42% | CHA -2.6 / CHA -3.5 | yes |
| CHI @ NYK | 111–122 | 105–135 | 80% | NYK -11.5 / NYK -11.5 | yes |
| IND @ MEM | 111–117 | 107–103 | 32% | MEM -6.4 / MEM -6.5 | yes |
| UTA @ NOP | 114–118 | 113–120 (OT) | 63% | NOP -4.4 / NOP -4.5 | yes |
| CLE @ OKC | 112–115 | 116–124 | 60% | OKC -3.2 / OKC -3.5 | yes |
| MIN @ HOU | 106–113 | 117–107 | 29% | HOU -7.1 / HOU -7.5 | yes |
| TOR @ DEN | 113–119 | 109–128 | 66% | DEN -5.5 / DEN -5.5 | yes |
| POR @ PHX | 115–112 | 132–119 | 59% | POR -3.1 / POR -3.5 | no |
| DAL @ SAS | 107–119 | 111–112 | 81% | SAS -11.9 / SAS -12.5 | yes |
| LAL @ SAC | 122–111 | 116–103 | 81% | LAL -11.9 / LAL -12.5 | yes |
| MIA @ LAC | 119–114 | 117–116 (OT) | 64% | MIA -4.7 / MIA -5.5 | yes |

## Power ratings

Points per 100 possessions better than an average team on a neutral floor, combining opponent-adjusted team efficiency (garbage time removed) with the ratings of the team's healthy roster, through the fitted points map. Net per game uses the team's pace. Injury effect now is what its current injury report does to its margin, in points.

| # | Team | Net per 100 | Net per game | Offense | Defense | Pace | Injury effect now | Elo |
|---|---|---|---|---|---|---|---|---|
| 1 | HOU | +7.0 | +7.0 | +3.8 | +3.2 | 99.1 | -0.5 | 1620 |
| 2 | DET | +6.4 | +6.5 | +2.2 | +4.2 | 101.2 | -0.1 | 1653 |
| 3 | SAS | +6.4 | +6.5 | +1.9 | +4.5 | 102.6 | +0.7 | 1695 |
| 4 | BOS | +6.0 | +5.8 | +3.2 | +2.8 | 96.4 | +1.1 | 1619 |
| 5 | MIN | +5.1 | +5.3 | +2.1 | +3.0 | 103.3 | -0.5 | 1615 |
| 6 | LAL | +4.2 | +4.3 | +3.9 | +0.3 | 102.0 | +0.0 | 1593 |
| 7 | POR | +4.0 | +4.0 | +2.7 | +1.3 | 101.4 | +0.0 | 1563 |
| 8 | NYK | +3.7 | +3.5 | +1.2 | +2.4 | 96.6 | -0.1 | 1690 |
| 9 | PHI | +3.6 | +3.6 | +0.4 | +3.1 | 101.4 | +0.4 | 1588 |
| 10 | OKC | +3.2 | +3.2 | -0.2 | +3.4 | 100.8 | -0.1 | 1672 |
| 11 | DEN | +2.0 | +2.0 | +3.5 | -1.4 | 97.5 | +1.3 | 1577 |
| 12 | GSW | +1.9 | +1.9 | +1.5 | +0.3 | 101.3 | -1.1 | 1505 |
| 13 | CLE | +1.2 | +1.2 | +2.0 | -0.9 | 103.0 | +0.2 | 1573 |
| 14 | MIA | +0.8 | +0.8 | +2.0 | -1.2 | 105.8 | +0.0 | 1497 |
| 15 | TOR | +0.7 | +0.7 | +0.3 | +0.4 | 105.5 | -2.2 | 1544 |
| 16 | MEM | -0.9 | -0.9 | +0.5 | -1.4 | 102.5 | -0.1 | 1412 |
| 17 | ORL | -1.0 | -1.0 | -2.1 | +1.1 | 99.4 | +0.4 | 1505 |
| 18 | DAL | -1.1 | -1.1 | -0.8 | -0.3 | 101.7 | +1.1 | 1431 |
| 19 | PHX | -1.2 | -1.2 | +1.1 | -2.3 | 101.9 | +0.3 | 1481 |
| 20 | ATL | -1.7 | -1.8 | -1.1 | -0.6 | 106.7 | +2.1 | 1546 |
| 21 | IND | -2.6 | -2.7 | -1.2 | -1.4 | 102.7 | -0.4 | 1362 |
| 22 | NOP | -2.6 | -2.8 | -1.2 | -1.5 | 105.7 | +0.3 | 1443 |
| 23 | LAC | -3.4 | -3.4 | -1.8 | -1.6 | 100.1 | +0.5 | 1476 |
| 24 | UTA | -4.0 | -4.1 | -3.6 | -0.5 | 102.7 | -0.7 | 1304 |
| 25 | CHA | -4.5 | -4.4 | -4.0 | -0.5 | 96.1 | -0.9 | 1488 |
| 26 | WAS | -4.9 | -4.9 | -3.0 | -1.8 | 100.2 | -0.5 | 1337 |
| 27 | BKN | -6.0 | -6.0 | -3.4 | -2.5 | 100.9 | +0.5 | 1319 |
| 28 | MIL | -7.1 | -7.4 | -2.8 | -4.3 | 104.0 | +0.6 | 1343 |
| 29 | SAC | -7.5 | -7.8 | -3.5 | -4.0 | 104.5 | +0.0 | 1344 |
| 30 | CHI | -7.6 | -8.5 | -3.8 | -3.7 | 112.0 | -0.5 | 1356 |

## Top players

Regularized adjusted plus-minus from every lineup this season and past ones: points per 100 possessions a player adds on offense and saves on defense, against an average player, shrunk toward last season's rating. Players expected to play 20 minutes or more.

| # | Player | Team | Net impact per 100 | Offense | Defense | Expected minutes |
|---|---|---|---|---|---|---|
| 1 | Victor Wembanyama | SAS | +6.7 | +1.8 | +4.9 | 32 |
| 2 | Shai Gilgeous-Alexander | OKC | +5.7 | +5.1 | +0.6 | 35 |
| 3 | Nikola Jokic | DEN | +5.4 | +5.5 | -0.1 | 34 |
| 4 | Kawhi Leonard | TOR | +4.5 | +3.6 | +0.9 | 30 |
| 5 | Luka Doncic | LAL | +4.4 | +5.4 | -1.0 | 36 |
| 6 | Giannis Antetokounmpo | MIA | +4.0 | +3.9 | +0.2 | 36 |
| 7 | Kyrie Irving | DAL | +3.6 | +3.4 | +0.1 | 33 |
| 8 | Joel Embiid | PHI | +3.4 | +1.6 | +1.8 | 32 |
| 9 | Herbert Jones | NOP | +3.3 | +0.0 | +3.3 | 29 |
| 10 | Marcus Smart | HOU | +2.3 | +1.2 | +1.1 | 21 |
| 11 | Fred VanVleet | HOU | +2.3 | +1.8 | +0.5 | 30 |
| 12 | Jimmy Butler III | GSW | +2.2 | +2.1 | +0.1 | 27 |
| 13 | LaMelo Ball | MIN | +2.2 | +4.0 | -1.8 | 29 |
| 14 | Chet Holmgren | OKC | +2.1 | +0.0 | +2.1 | 30 |
| 15 | Ausar Thompson | DET | +2.1 | +0.0 | +2.1 | 29 |
| 16 | Dean Wade | PHI | +2.0 | +0.5 | +1.6 | 24 |
| 17 | Franz Wagner | ORL | +2.0 | +0.8 | +1.2 | 37 |
| 18 | Stephen Curry | GSW | +2.0 | +4.4 | -2.4 | 31 |
| 19 | Donovan Mitchell | CLE | +1.9 | +2.7 | -0.8 | 33 |
| 20 | Bam Adebayo | MIA | +1.9 | +1.6 | +0.3 | 35 |
| 21 | Rudy Gobert | MIN | +1.9 | -3.2 | +5.1 | 31 |
| 22 | Cade Cunningham | DET | +1.8 | +1.6 | +0.2 | 34 |
| 23 | Ty Jerome | MEM | +1.8 | +3.1 | -1.3 | 30 |
| 24 | Dyson Daniels | ATL | +1.7 | +0.5 | +1.2 | 31 |
| 25 | Lauri Markkanen | UTA | +1.7 | +1.5 | +0.2 | 32 |
| 26 | Neemias Queta | BOS | +1.7 | +0.7 | +1.0 | 26 |
| 27 | Derrick White | BOS | +1.6 | +0.2 | +1.4 | 33 |
| 28 | Paul Reed | DET | +1.6 | +0.2 | +1.4 | 29 |
| 29 | Jrue Holiday | POR | +1.6 | +0.6 | +1.0 | 28 |
| 30 | Pascal Siakam | IND | +1.6 | +1.4 | +0.2 | 32 |

## Current model fit

- Fitted on 5403 games from 2022-23 to 2026-27.
- Home court: +2.0 points per 100 possessions for the home team over the visitor (about 2.0 points a game).
- Second night of a back-to-back: -0.7 points per 100 scored, +1.2 allowed.
- Weights: team efficiency ratings 0.16 (offense) and 0.15 (defense); player lineup ratings 0.76 and 0.76.
- Blend: 82% on the betting line for the margin and 100% for the total, wherever there is a line (fitted on past closing lines).
- Simulator: each team's points vary by 10.9 with correlation 0.23; 5.2% of recent games went to overtime.
