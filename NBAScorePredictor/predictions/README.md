# NBA score predictions

Updated Thu Nov 05, 2026 03:46 PM ET. Refreshed automatically several times a day during the season, around the injury report's deadlines; each game's prediction is locked at tip-off and graded once the final score is in.

Each team's expected points are its expected possessions times its expected points per possession, from team efficiency ratings and the ratings of the players expected to play, blended with the betting line. Each game is then simulated 10,000 times, overtime included. The predicted score is the expected points rounded; the 80% range holds 80% of simulated outcomes for each team. Basketball is the most predictable major sport, but a team's score still varies by about ±14 points around the forecast, so read the win chance and the ranges too.

Missing players come from the injury report: out players are left out, and doubtful, questionable and probable ones count with the share of their minutes their chance of playing implies, and their minutes go mostly to the bench. The effect is how many points of margin the team gains or loses against its full-strength roster: negative when it is missing good players, positive when the minutes go to better ones. Predictions are rerun when the report changes, up to tip-off.

The fair moneyline is the American odds that match the win chance exactly, with no bookmaker margin: -150 means risk $150 to win $100, +150 means risk $100 to win $150.

The edge columns check every side of the spread, the moneyline and the total for expected value: the profit per $1 bet at the posted price, using the final prediction's chances (the model blended with the line, simulated against the posted lines, pushes returning the stake, and anchored to the market's own chances so only what the blend moves off the line counts). The model's own spread and total are shown alongside, but the blend keeps only the share of that disagreement the model has earned in past seasons, so edges are rare. A side is an edge when its EV is 3% or more; the best such side is shown with its price, its EV, its chance of winning the bet and its stake, a 25% share of the Kelly stake in units of 1% of the bankroll, with at most 3 units on one game. Where a spread or total price is not posted it is assumed to be -110 (marked \*); a moneyline is never assumed. Edges are logged with each prediction, locked at tip-off and graded below. Treat them as an experiment, not betting advice; see the backtest for how they have done on past seasons.

## Thursday, November 5

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Spread: model / line | Total: model / line | 80% range | Overtime | Missing (effect on margin) | Spread edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 9:00 PM | ORL @ PHX | ORL 111, PHX 112 | PHX 54% | ORL +115 / PHX -115<br>posted ORL -104 / PHX -114 | PHX -1.2 / PHX -1.5 (fav covers 51%) | 222.8 / 222.5 (over 50%) | 96–125 / 98–126 | 5% | ORL: Paolo Banchero (out); Jalen Suggs (out) (+0.4)<br>PHX: Mark Williams (out); Jordan Goodwin (out) (+0.2) | no edge | no edge | no edge |
| 10:00 PM | MIA @ GSW | MIA 113, GSW 119 | GSW 67% | MIA +200 / GSW -200<br>posted MIA +218 / GSW -265 | GSW -5.9 / GSW -6.5 (fav covers 49%) | 232.6 / 232.5 (over 49%) | 98–128 / 105–134 | 5% | GSW: Moses Moody (out); Jimmy Butler III (out); Kristaps Porzingis (out); Gui Santos (out) (-1.3) | no edge | no edge | no edge |

## Friday, November 6

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Spread: model / line | Total: model / line | 80% range | Overtime | Missing (effect on margin) | Spread edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 7:00 PM | WAS @ ATL | WAS 112, ATL 118 | ATL 68% | WAS +210 / ATL -210 | ATL -6 | 229.2 | 97–127 / 103–132 | 5% | WAS: Jamir Watkins (out); Justin Champagnie (out); Tristan Vukcevic (out) (+0.2)<br>ATL: Jalen Johnson (day-to-day) (+0.7) | no line yet | no line yet | no line yet |
| 7:00 PM | BOS @ CHA | BOS 109, CHA 100 | BOS 77% | BOS -340 / CHA +340 | BOS -9.5 | 209.2 | 96–123 / 86–114 | 4% | BOS: Jayson Tatum (day-to-day); Devin Carter (out); Payton Pritchard (day-to-day) (+0.9)<br>CHA: Kon Knueppel (day-to-day); Grant Williams (out) (-0.6) | no line yet | no line yet | no line yet |
| 7:30 PM | PHI @ CLE | PHI 115, CLE 114 | PHI 52% | PHI -110 / CLE +110 | PHI -0.7 | 228.1 | 100–129 / 99–128 | 5% | PHI: Adem Bona (day-to-day); Dominick Barlow (out) (+0.4)<br>CLE: Peyton Watson (day-to-day); Jarrett Allen (day-to-day); Jaylon Tyson (out); Tyrese Proctor (day-to-day) (+0.2) | no line yet | no line yet | no line yet |
| 8:00 PM | UTA @ DAL | UTA 109, DAL 116 | DAL 70% | UTA +230 / DAL -230 | DAL -6.8 | 224.8 | 94–124 / 102–130 | 5% | UTA: Jaren Jackson Jr. (out); Trey Alexander (out); Jusuf Nurkic (out) (-0.7)<br>DAL: Santi Aldama (out); Max Christie (day-to-day); Dereck Lively II (out); Sergio de Larrea (out) (+1.1) | no line yet | no line yet | no line yet |
| 8:00 PM | OKC @ MEM | OKC 115, MEM 113 | OKC 56% | OKC -125 / MEM +125 | OKC -1.9 | 227.4 | 100–129 / 98–127 | 5% | OKC: Chet Holmgren (out); Jalen Williams (out); Jaylin Williams (day-to-day); Cason Wallace (out) (-0.3)<br>MEM: Isaiah Stewart (day-to-day); Scotty Pippen Jr. (out) (+0.0) | no line yet | no line yet | no line yet |
| 8:00 PM | TOR @ MIL | TOR 119, MIL 115 | TOR 61% | TOR -160 / MIL +160 | TOR -3.9 | 234.4 | 104–134 / 100–130 | 6% | TOR: Kawhi Leonard (out) (-1.9)<br>MIL: Kam Jones (day-to-day) (+0.2) | no line yet | no line yet | no line yet |
| 8:00 PM | MIN @ NOP | MIN 117, NOP 112 | MIN 65% | MIN -185 / NOP +185 | MIN -5.2 | 229.6 | 103–132 / 98–127 | 5% | MIN: Anthony Edwards (out); Terrence Shannon Jr. (day-to-day); Donte DiVincenzo (out) (-0.5)<br>NOP: Trey Murphy III (day-to-day); Yves Missi (out) (+0.3) | no line yet | no line yet | no line yet |
| 10:00 PM | POR @ LAL | POR 114, LAL 117 | LAL 57% | POR +135 / LAL -135 | LAL -2.6 | 231.5 | 100–129 / 102–131 | 5% | POR: Ja Morant (out) (+0.0) | no line yet | no line yet | no line yet |
| 10:00 PM | SAS @ SAC | SAS 121, SAC 108 | SAS 83% | SAS -495 / SAC +495 | SAS -13 | 229.0 | 107–135 / 93–123 | 4% | SAS: Tobias Harris (out) (+0.7)<br>SAC: Maxime Raynaud (out); Keegan Murray (out) (+0.0) | no line yet | no line yet | no line yet |

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
| 1 | HOU | +6.9 | +6.8 | +3.7 | +3.2 | 99.0 | -0.5 | 1620 |
| 2 | DET | +6.4 | +6.5 | +2.2 | +4.2 | 101.2 | -0.1 | 1653 |
| 3 | SAS | +6.4 | +6.5 | +1.9 | +4.5 | 102.6 | +0.7 | 1695 |
| 4 | BOS | +5.9 | +5.7 | +3.1 | +2.8 | 96.4 | +0.9 | 1619 |
| 5 | MIN | +5.1 | +5.3 | +2.1 | +3.0 | 103.3 | -0.5 | 1615 |
| 6 | LAL | +4.3 | +4.3 | +3.9 | +0.3 | 102.0 | +0.4 | 1593 |
| 7 | POR | +4.0 | +4.0 | +2.7 | +1.3 | 101.4 | +0.0 | 1563 |
| 8 | NYK | +3.7 | +3.5 | +1.2 | +2.4 | 96.5 | -0.1 | 1690 |
| 9 | PHI | +3.6 | +3.6 | +0.4 | +3.1 | 101.4 | +0.4 | 1588 |
| 10 | OKC | +3.2 | +3.2 | -0.2 | +3.4 | 100.8 | -0.3 | 1672 |
| 11 | DEN | +2.0 | +2.0 | +3.5 | -1.4 | 97.5 | +1.3 | 1577 |
| 12 | GSW | +1.9 | +1.9 | +1.5 | +0.3 | 101.3 | -1.2 | 1505 |
| 13 | CLE | +1.2 | +1.2 | +2.0 | -0.9 | 103.0 | +0.2 | 1573 |
| 14 | MIA | +0.8 | +0.8 | +2.0 | -1.2 | 105.9 | +0.0 | 1497 |
| 15 | TOR | +0.7 | +0.7 | +0.3 | +0.4 | 105.6 | -2.0 | 1544 |
| 16 | MEM | -0.9 | -0.9 | +0.5 | -1.4 | 102.5 | +0.0 | 1412 |
| 17 | ORL | -1.0 | -1.0 | -2.1 | +1.1 | 99.4 | +0.4 | 1505 |
| 18 | DAL | -1.0 | -1.1 | -0.8 | -0.3 | 101.6 | +1.1 | 1431 |
| 19 | PHX | -1.2 | -1.2 | +1.1 | -2.3 | 101.9 | +0.2 | 1481 |
| 20 | ATL | -1.7 | -1.8 | -1.1 | -0.6 | 106.8 | +0.8 | 1546 |
| 21 | IND | -2.6 | -2.7 | -1.2 | -1.4 | 102.7 | -0.4 | 1362 |
| 22 | NOP | -2.6 | -2.8 | -1.2 | -1.5 | 105.7 | +0.3 | 1443 |
| 23 | LAC | -3.4 | -3.4 | -1.8 | -1.6 | 100.1 | +0.5 | 1476 |
| 24 | UTA | -4.0 | -4.1 | -3.6 | -0.4 | 102.6 | -0.7 | 1304 |
| 25 | CHA | -4.4 | -4.2 | -3.9 | -0.4 | 96.1 | -0.6 | 1488 |
| 26 | WAS | -4.9 | -4.9 | -3.0 | -1.8 | 100.2 | +0.2 | 1337 |
| 27 | BKN | -6.0 | -6.0 | -3.4 | -2.5 | 100.9 | +0.5 | 1319 |
| 28 | MIL | -7.1 | -7.4 | -2.8 | -4.3 | 104.1 | +0.2 | 1343 |
| 29 | SAC | -7.5 | -7.8 | -3.5 | -4.0 | 104.5 | +0.0 | 1344 |
| 30 | CHI | -7.6 | -8.5 | -3.8 | -3.8 | 112.1 | -0.5 | 1356 |

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
| 7 | Kyrie Irving | DAL | +3.6 | +3.4 | +0.2 | 33 |
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
