# NBA score predictions

Updated Wed Nov 18, 2026 09:44 PM ET. Refreshed automatically several times a day during the season, around the injury report's deadlines; each game's prediction is locked at tip-off and graded once the final score is in.

Each team's expected points are its expected possessions times its expected points per possession, from team efficiency ratings and the ratings of the players expected to play, blended with the betting line. Each game is then simulated 10,000 times, overtime included. The predicted score is the expected points rounded; the 80% range holds 80% of simulated outcomes for each team. Basketball is the most predictable major sport, but a team's score still varies by about ±14 points around the forecast, so read the win chance and the ranges too.

Missing players come from the injury report: out players are left out, and doubtful, questionable and probable ones count with the share of their minutes their chance of playing implies, and their minutes go mostly to the bench. The effect is how many points of margin the team gains or loses against its full-strength roster: negative when it is missing good players, positive when the minutes go to better ones. Predictions are rerun when the report changes, up to tip-off.

The fair moneyline is the American odds that match the win chance exactly, with no bookmaker margin: -150 means risk $150 to win $100, +150 means risk $100 to win $150.

The edge columns check every side of the spread, the moneyline and the total for expected value: the profit per $1 bet at the posted price, using the final prediction's chances (the model blended with the line, simulated against the posted lines, pushes returning the stake, and anchored to the market's own chances so only what the blend moves off the line counts). The model's own spread and total are shown alongside, but the blend keeps only the share of that disagreement the model has earned in past seasons, so edges are rare. A side is an edge when its EV is 3% or more; the best such side is shown with its price, its EV, its chance of winning the bet and its stake, a 25% share of the Kelly stake in units of 1% of the bankroll, with at most 3 units on one game. Where a spread or total price is not posted it is assumed to be -110 (marked \*); a moneyline is never assumed. Edges are logged with each prediction, locked at tip-off and graded below. Treat them as an experiment, not betting advice; see the backtest for how they have done on past seasons.

## Wednesday, November 18

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Spread: model / line | Total: model / line | 80% range | Overtime | Missing (effect on margin) | Spread edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 10:00 PM | UTA @ LAL | UTA 109, LAL 120 | LAL 80% | UTA +400 / LAL -400<br>posted UTA +411 / LAL -545 | LAL -11.4 / LAL -11.5 (fav covers 49%) | 229.3 / 229.5 (over 49%) | 94–124 / 106–134 | 4% | UTA: Lauri Markkanen (out); Jaren Jackson Jr. (out); Jusuf Nurkic (out) (-2.5)<br>LAL: Austin Reaves (out) (-1.0) | no edge | no edge | no edge |
| 10:00 PM | PHX @ SAC | PHX 117, SAC 110 | PHX 71% | PHX -240 / SAC +240<br>posted PHX -269 / SAC +221 | PHX -7.2 / PHX -7.5 (fav covers 50%) | 226.5 / 226.5 (over 49%) | 103–131 / 95–124 | 5% | PHX: Mark Williams (out) (+0.5)<br>SAC: Maxime Raynaud (out) (+0.6) | no edge | no edge | no edge |

## Thursday, November 19

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Spread: model / line | Total: model / line | 80% range | Overtime | Missing (effect on margin) | Spread edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 8:00 PM | GSW @ MEM | GSW 114, MEM 117 | MEM 60% | GSW +150 / MEM -150 | MEM -3.4 | 231.3 | 99–129 / 103–132 | 5% | GSW: Moses Moody (out); Jimmy Butler III (out); Kristaps Porzingis (out); Stephen Curry (out); Al Horford (out); Brandon Williams (out) (-3.6)<br>MEM: Ty Jerome (out); Isaiah Stewart (out); Scotty Pippen Jr. (out) (-1.2) | no line yet | no line yet | no line yet |
| 8:00 PM | POR @ MIL | POR 120, MIL 109 | POR 78% | POR -360 / MIL +360 | POR -10.6 | 229.5 | 106–134 / 95–125 | 4% | POR: Deni Avdija (day-to-day); Toumani Camara (day-to-day); Ja Morant (out); Robert Williams III (out); Chris Youngblood (out) (-0.8)<br>MIL: Ryan Rollins (out) (-0.5) | no line yet | no line yet | no line yet |
| 8:00 PM | NYK @ MIN | NYK 107, MIN 108 | MIN 53% | NYK +115 / MIN -115 | MIN -1.2 | 215.0 | 93–121 / 94–122 | 5% | MIN: Anthony Edwards (out); Jonathan Kuminga (day-to-day); Donte DiVincenzo (out); Jaylen Clark (out) (-0.8) | no line yet | no line yet | no line yet |
| 8:00 PM | LAC @ SAS | LAC 104, SAS 121 | SAS 88% | LAC +740 / SAS -740<br>posted LAC +720 / SAS -1140 | SAS -16.1 / SAS -16.5 (fav covers 47%) | 225.0 / 225.5 (over 48%) | 90–119 / 107–135 | 3% | LAC: Brandon Ingram (out); Jordan Miller (out); Bradley Beal (out) (+0.2)<br>SAS: Dylan Harper (out); Tobias Harris (out) (+0.1) | no edge | no edge | no edge |

## How the 2026-27 predictions have done

| Predictor | Games | Margin MAE | Total MAE | Team-points MAE | Log loss | Brier | Winners | 80% range hit |
|---|---|---|---|---|---|---|---|---|
| Final prediction | 210 | 11.31 | 14.15 | 9.33 | 0.566 | 0.192 | 71.4% | 81.0% |
| Model only (before blending) | 210 | 11.56 | 13.97 | 9.36 | 0.580 | 0.198 | 70.5% | – |
| Elo | 210 | 11.88 | – | – | 0.602 | 0.208 | 65.7% | – |
| Final prediction, games with a line | 210 | 11.31 | 14.15 | 9.33 | 0.566 | 0.192 | 71.4% | 81.0% |
| Model only, games with a line | 210 | 11.56 | 13.97 | 9.36 | 0.580 | 0.198 | 70.5% | – |
| Betting line | 210 | 11.28 | 14.16 | 9.32 | 0.562 | 0.191 | 71.4% | – |

MAE is the average miss in points; team-points MAE is the average miss on each team's score. Log loss and Brier score the win chances (lower is better; a coin flip scores 0.693 and 0.250). The closing line misses margins by about 10 points and totals by about 14.

Overtime: predicted in 4.7% of games, happened in 5.7%.

### Betting edges

| Market | Edges | Record (W-L-P) | Staked | Units won | ROI | Expected ROI |
|---|---|---|---|---|---|---|
| Spread | 1 | 1-0-0 | 1.0 | +0.90 | +89.3% | +3.6% |
| Moneyline | 15 | 2-13-0 | 5.6 | -2.59 | -46.2% | +6.5% |
| Total | 0 | 0-0-0 | 0.0 | +0.00 | – | – |

Spread moved toward the model's first spread edge before tip-off: 5 of 6 games (83%).

Live predictions only, each edge at the stake and price logged with the last prediction before tip-off (edges logged before edges were priced from the final prediction are left out); a push returns the stake. Units are 1% of the bankroll; ROI is units won per unit staked, and expected ROI is what the edges' EVs promised. The line moving toward the model's edge before tip-off is the quickest sign that it knows something the market doesn't yet.

### Results, Tuesday, November 17

| Game | Predicted | Final | Win chance for winner | Spread: model / line | Inside 80% ranges |
|---|---|---|---|---|---|
| NYK @ TOR | 109–107 | 111–102 | 58% | NYK -2.7 / NYK -2.5 | yes |
| POR @ MIN | 113–115 | 105–106 | 58% | MIN -2.5 / MIN -2.5 | yes |
| DET @ SAS | 106–115 | 105–93 | 25% | SAS -8.7 / SAS -9.5 | no |
| UTA @ LAC | 111–117 | 132–107 | 34% | LAC -5.6 / LAC -5.5 | no |
| CHA @ LAL | 106–114 | 114–118 (OT) | 72% | LAL -8 / LAL -7.5 | yes |

## Power ratings

Points per 100 possessions better than an average team on a neutral floor, combining opponent-adjusted team efficiency (garbage time removed) with the ratings of the team's healthy roster, through the fitted points map. Net per game uses the team's pace. Injury effect now is what its current injury report does to its margin, in points.

| # | Team | Net per 100 | Net per game | Offense | Defense | Pace | Injury effect now | Elo |
|---|---|---|---|---|---|---|---|---|
| 1 | SAS | +8.3 | +8.1 | +3.1 | +5.1 | 98.2 | +0.1 | 1714 |
| 2 | BOS | +7.8 | +7.4 | +4.0 | +3.8 | 95.3 | +0.0 | 1654 |
| 3 | DET | +5.7 | +5.7 | +2.3 | +3.3 | 100.2 | -1.6 | 1646 |
| 4 | HOU | +5.6 | +5.4 | +3.2 | +2.4 | 97.9 | -0.1 | 1615 |
| 5 | LAL | +4.9 | +5.0 | +4.3 | +0.6 | 102.0 | -1.0 | 1633 |
| 6 | NYK | +4.4 | +4.1 | +1.3 | +3.1 | 92.8 | +0.0 | 1687 |
| 7 | MIN | +4.4 | +4.6 | +1.0 | +3.4 | 104.3 | -0.8 | 1613 |
| 8 | DEN | +3.4 | +3.3 | +3.7 | -0.3 | 97.7 | +0.2 | 1566 |
| 9 | OKC | +3.3 | +3.4 | -0.6 | +3.9 | 101.7 | -0.5 | 1652 |
| 10 | POR | +2.6 | +2.7 | +1.5 | +1.2 | 102.7 | -0.8 | 1573 |
| 11 | PHI | +2.4 | +2.5 | +1.1 | +1.3 | 101.5 | -2.4 | 1575 |
| 12 | TOR | +0.5 | +0.5 | +0.0 | +0.5 | 99.4 | -4.0 | 1502 |
| 13 | MIA | +0.4 | +0.4 | +1.7 | -1.2 | 104.1 | +0.5 | 1546 |
| 14 | GSW | +0.4 | +0.4 | -0.1 | +0.4 | 100.3 | -3.6 | 1502 |
| 15 | PHX | +0.3 | +0.3 | +0.7 | -0.4 | 102.2 | +0.5 | 1517 |
| 16 | ORL | +0.1 | +0.1 | -1.8 | +1.9 | 100.5 | +1.5 | 1526 |
| 17 | CLE | -0.1 | -0.1 | +1.4 | -1.4 | 101.7 | -0.3 | 1577 |
| 18 | MEM | -0.7 | -0.7 | +1.3 | -2.0 | 102.7 | -1.2 | 1465 |
| 19 | IND | -1.0 | -1.1 | -0.2 | -0.8 | 103.5 | +0.3 | 1371 |
| 20 | UTA | -2.1 | -2.1 | -2.0 | -0.1 | 100.6 | -2.5 | 1323 |
| 21 | DAL | -2.2 | -2.3 | -1.1 | -1.1 | 102.2 | +1.0 | 1431 |
| 22 | ATL | -2.3 | -2.5 | -2.1 | -0.3 | 107.6 | +2.1 | 1530 |
| 23 | LAC | -3.4 | -3.5 | -1.4 | -2.1 | 100.9 | +0.3 | 1443 |
| 24 | CHI | -4.6 | -5.0 | -2.3 | -2.3 | 109.3 | +1.6 | 1386 |
| 25 | CHA | -5.0 | -4.7 | -4.5 | -0.4 | 95.7 | -0.2 | 1467 |
| 26 | NOP | -5.2 | -5.4 | -1.9 | -3.3 | 103.8 | +0.1 | 1368 |
| 27 | BKN | -5.6 | -5.7 | -2.3 | -3.3 | 101.4 | +0.0 | 1334 |
| 28 | WAS | -5.8 | -5.9 | -2.4 | -3.4 | 101.1 | +0.0 | 1302 |
| 29 | MIL | -8.2 | -8.3 | -3.8 | -4.4 | 101.0 | -0.5 | 1315 |
| 30 | SAC | -8.2 | -8.4 | -4.1 | -4.2 | 102.4 | +0.6 | 1317 |

## Top players

Regularized adjusted plus-minus from every lineup this season and past ones: points per 100 possessions a player adds on offense and saves on defense, against an average player, shrunk toward last season's rating. Players expected to play 20 minutes or more.

| # | Player | Team | Net impact per 100 | Offense | Defense | Expected minutes |
|---|---|---|---|---|---|---|
| 1 | Victor Wembanyama | SAS | +8.4 | +2.7 | +5.7 | 31 |
| 2 | Shai Gilgeous-Alexander | OKC | +5.7 | +5.2 | +0.6 | 33 |
| 3 | Alex Caruso | OKC | +5.4 | +0.3 | +5.1 | 22 |
| 4 | Nikola Jokic | DEN | +4.9 | +4.6 | +0.2 | 37 |
| 5 | Kawhi Leonard | TOR | +4.6 | +3.6 | +0.9 | 30 |
| 6 | Luka Doncic | LAL | +4.4 | +5.3 | -0.9 | 38 |
| 7 | Giannis Antetokounmpo | MIA | +4.4 | +4.1 | +0.2 | 31 |
| 8 | Kyrie Irving | DAL | +3.5 | +3.6 | -0.1 | 33 |
| 9 | Neemias Queta | BOS | +3.0 | +1.3 | +1.7 | 21 |
| 10 | Joel Embiid | PHI | +2.9 | +1.5 | +1.4 | 30 |
| 11 | Franz Wagner | ORL | +2.8 | +1.5 | +1.2 | 38 |
| 12 | Donovan Mitchell | CLE | +2.5 | +3.4 | -0.9 | 34 |
| 13 | Derrick White | BOS | +2.3 | +0.6 | +1.7 | 29 |
| 14 | Ausar Thompson | DET | +2.2 | +0.0 | +2.2 | 28 |
| 15 | Jimmy Butler III | GSW | +2.2 | +2.1 | +0.1 | 27 |
| 16 | Jarrett Allen | CLE | +2.2 | +1.8 | +0.4 | 28 |
| 17 | Paul Reed | DET | +2.1 | +0.6 | +1.5 | 26 |
| 18 | Chet Holmgren | OKC | +2.1 | +0.0 | +2.1 | 30 |
| 19 | Fred VanVleet | HOU | +2.1 | +1.4 | +0.7 | 30 |
| 20 | Bam Adebayo | MIA | +2.0 | +1.6 | +0.5 | 29 |
| 21 | LaMelo Ball | MIN | +2.0 | +3.5 | -1.5 | 29 |
| 22 | Herbert Jones | NOP | +1.9 | -1.1 | +3.0 | 26 |
| 23 | Dyson Daniels | ATL | +1.9 | +0.1 | +1.8 | 31 |
| 24 | Dean Wade | PHI | +1.8 | +1.1 | +0.7 | 30 |
| 25 | Pascal Siakam | IND | +1.7 | +1.5 | +0.2 | 33 |
| 26 | Day'Ron Sharpe | BKN | +1.7 | +0.8 | +0.9 | 25 |
| 27 | Ty Jerome | MEM | +1.7 | +2.7 | -1.0 | 30 |
| 28 | Cade Cunningham | DET | +1.7 | +1.9 | -0.2 | 38 |
| 29 | Paul George | BOS | +1.6 | +0.8 | +0.8 | 31 |
| 30 | Damian Lillard | POR | +1.5 | +1.7 | -0.2 | 29 |

## Current model fit

- Fitted on 5492 games from 2022-23 to 2026-27.
- Home court: +2.0 points per 100 possessions for the home team over the visitor (about 2.0 points a game).
- Second night of a back-to-back: -0.7 points per 100 scored, +1.2 allowed.
- Weights: team efficiency ratings 0.14 (offense) and 0.15 (defense); player lineup ratings 0.77 and 0.76.
- Blend: 82% on the betting line for the margin and 100% for the total, wherever there is a line (fitted on past closing lines).
- Simulator: each team's points vary by 11.0 with correlation 0.23; 5.2% of recent games went to overtime.
