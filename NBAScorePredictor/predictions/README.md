# NBA score predictions

Updated Sat Oct 24, 2026 09:11 PM ET. Refreshed automatically several times a day during the season, around the injury report's deadlines; each game's prediction is locked at tip-off and graded once the final score is in.

Each team's expected points are its expected possessions times its expected points per possession, from team efficiency ratings and the ratings of the players expected to play, blended with the betting line. Each game is then simulated 10,000 times, overtime included. The predicted score is the expected points rounded; the 80% range holds 80% of simulated outcomes for each team. Basketball is the most predictable major sport, but a team's score still varies by about ±14 points around the forecast, so read the win chance and the ranges too.

Missing players come from the injury report: out players are left out, and doubtful, questionable and probable ones count with the share of their minutes their chance of playing implies, and their minutes go mostly to the bench. The effect is how many points of margin the team gains or loses against its full-strength roster: negative when it is missing good players, positive when the minutes go to better ones. Predictions are rerun when the report changes, up to tip-off.

The fair moneyline is the American odds that match the win chance exactly, with no bookmaker margin: -150 means risk $150 to win $100, +150 means risk $100 to win $150.

The edge columns check every side of the spread, the moneyline and the total for expected value: the profit per $1 bet at the posted price, using the final prediction's chances (the model blended with the line, simulated against the posted lines, pushes returning the stake, and anchored to the market's own chances so only what the blend moves off the line counts). The model's own spread and total are shown alongside, but the blend keeps only the share of that disagreement the model has earned in past seasons, so edges are rare. A side is an edge when its EV is 3% or more; the best such side is shown with its price, its EV, its chance of winning the bet and its stake, a 25% share of the Kelly stake in units of 1% of the bankroll, with at most 3 units on one game. Where a spread or total price is not posted it is assumed to be -110 (marked \*); a moneyline is never assumed. Edges are logged with each prediction, locked at tip-off and graded below. Treat them as an experiment, not betting advice; see the backtest for how they have done on past seasons.

## Saturday, October 24

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Spread: model / line | Total: model / line | 80% range | Overtime | Missing (effect on margin) | Spread edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 10:00 PM | GSW @ PHX | GSW 106, PHX 115 | PHX 75% | GSW +305 / PHX -305<br>posted GSW +320 / PHX -410 | PHX -9.3 / PHX -9.5 (fav covers 49%) | 221.5 / 221.5 (over 50%) | 92–120 / 102–129 | 4% | GSW: Brandin Podziemski (out); Moses Moody (out); Draymond Green (out); Stephen Curry (out); Jimmy Butler III (out); Kristaps Porzingis (out); Al Horford (out) (-3.9)<br>PHX: Oso Ighodaro (out); Mark Williams (out) (+0.1) | no edge | no edge | no edge |

## Sunday, October 25

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Spread: model / line | Total: model / line | 80% range | Overtime | Missing (effect on margin) | Spread edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 5:00 PM | LAL @ UTA | LAL 117, UTA 112 | LAL 65% | LAL -185 / UTA +185 | LAL -5.1 | 229.5 | 103–132 / 98–127 | 5% | UTA: Trey Alexander (out); Jusuf Nurkic (out) (+0.1) | no line yet | no line yet | no line yet |
| 6:00 PM | IND @ BKN | IND 117, BKN 113 | IND 63% | IND -170 / BKN +170 | IND -4.4 | 230.0 | 103–132 / 98–127 | 5% | IND: Aaron Nesmith (day-to-day); Johnny Furphy (out); Ben Sheppard (out); T.J. McConnell (out) (+0.6) | no line yet | no line yet | no line yet |
| 7:00 PM | ORL @ NYK | ORL 107, NYK 112 | NYK 65% | ORL +180 / NYK -180 | NYK -5 | 218.3 | 92–121 / 97–126 | 5% | ORL: Paolo Banchero (out); Anthony Black (day-to-day) (+1.5)<br>NYK: Jose Alvarado (day-to-day) (-0.1) | no line yet | no line yet | no line yet |
| 7:00 PM | TOR @ MIN | TOR 114, MIN 115 | MIN 52% | TOR +105 / MIN -105 | MIN -0.7 | 228.5 | 99–129 / 100–129 | 6% | MIN: Donte DiVincenzo (out) (-0.2) | no line yet | no line yet | no line yet |
| 7:00 PM | LAC @ OKC | LAC 104, OKC 114 | OKC 75% | LAC +305 / OKC -305 | OKC -9.1 | 218.0 | 90–119 / 100–127 | 4% | LAC: Max Strus (out); Brandon Ingram (out); Jordan Miller (out); Bradley Beal (out); Yanic Konan Niederhauser (out) (+1.2) | no line yet | no line yet | no line yet |
| 7:30 PM | DET @ PHI | DET 115, PHI 114 | DET 53% | DET -110 / PHI +110 | DET -0.9 | 229.2 | 100–130 / 100–129 | 5% | DET: Ausar Thompson (day-to-day); Jalen Duren (out) (-0.8)<br>PHI: LeBron James (out); Dominick Barlow (out) (+0.1) | no line yet | no line yet | no line yet |
| 9:00 PM | MEM @ SAC | MEM 115, SAC 116 | SAC 51% | MEM +105 / SAC -105 | SAC -0.6 | 230.3 | 100–130 / 101–130 | 5% | MEM: Cedric Coward (day-to-day); Zach Edey (out) (-0.9)<br>SAC: Maxime Raynaud (out); Keegan Murray (day-to-day); Dylan Cardwell (out) (+0.9) | no line yet | no line yet | no line yet |

## How the 2026-27 predictions have done

| Predictor | Games | Margin MAE | Total MAE | Team-points MAE | Log loss | Brier | Winners | 80% range hit |
|---|---|---|---|---|---|---|---|---|
| Final prediction | 28 | 13.03 | 14.44 | 9.84 | 0.617 | 0.214 | 67.9% | 80.4% |
| Model only (before blending) | 28 | 14.32 | 14.01 | 10.39 | 0.677 | 0.242 | 60.7% | – |
| Elo | 28 | 14.06 | – | – | 0.703 | 0.254 | 50.0% | – |
| Final prediction, games with a line | 28 | 13.03 | 14.44 | 9.84 | 0.617 | 0.214 | 67.9% | 80.4% |
| Model only, games with a line | 28 | 14.32 | 14.01 | 10.39 | 0.677 | 0.242 | 60.7% | – |
| Betting line | 28 | 12.82 | 14.39 | 9.75 | 0.597 | 0.205 | 67.9% | – |

MAE is the average miss in points; team-points MAE is the average miss on each team's score. Log loss and Brier score the win chances (lower is better; a coin flip scores 0.693 and 0.250). The closing line misses margins by about 10 points and totals by about 14.

Overtime: predicted in 4.9% of games, happened in 0.0%.

### Betting edges

| Market | Edges | Record (W-L-P) | Staked | Units won | ROI | Expected ROI |
|---|---|---|---|---|---|---|
| Spread | 0 | 0-0-0 | 0.0 | +0.00 | – | – |
| Moneyline | 1 | 0-1-0 | 0.3 | -0.29 | -100.0% | +3.4% |
| Total | 0 | 0-0-0 | 0.0 | +0.00 | – | – |

Spread moved toward the model's first spread edge before tip-off: 4 of 5 games (80%).

Live predictions only, each edge at the stake and price logged with the last prediction before tip-off (edges logged before edges were priced from the final prediction are left out); a push returns the stake. Units are 1% of the bankroll; ROI is units won per unit staked, and expected ROI is what the edges' EVs promised. The line moving toward the model's edge before tip-off is the quickest sign that it knows something the market doesn't yet.

### Results, Friday, October 23

| Game | Predicted | Final | Win chance for winner | Spread: model / line | Inside 80% ranges |
|---|---|---|---|---|---|
| CHI @ MIL | 119–121 | 132–125 | 45% | MIL -1.9 / MIL -1.5 | yes |
| NYK @ BOS | 109–112 | 103–107 | 59% | BOS -3 / BOS -2.5 | yes |
| ATL @ CHA | 115–113 | 128–81 | 57% | ATL -2.2 / ATL -2.5 | no |
| DAL @ IND | 117–124 | 121–105 | 31% | IND -6.9 / IND -7.5 | no |
| MIN @ ORL | 116–118 | 115–93 | 45% | ORL -1.8 / ORL -1.5 | no |
| TOR @ WAS | 123–115 | 112–102 | 72% | TOR -8.3 / TOR -8.5 | yes |
| DET @ MIA | 118–117 | 128–111 | 53% | DET -1.3 / DET -1.5 | yes |
| HOU @ SAS | 110–115 | 114–110 | 38% | SAS -4.3 / SAS -4.5 | yes |
| NOP @ UTA | 118–120 | 119–120 | 56% | UTA -2.1 / UTA -1.5 | yes |
| MEM @ GSW | 116–121 | 111–108 | 37% | GSW -4.5 / GSW -4.5 | yes |
| LAC @ LAL | 109–117 | 117–125 | 72% | LAL -7.6 / LAL -8.5 | yes |
| POR @ SAC | 120–111 | 128–120 | 75% | POR -9.1 / POR -9.5 | yes |

## Power ratings

Points per 100 possessions better than an average team on a neutral floor, combining opponent-adjusted team efficiency (garbage time removed) with the ratings of the team's healthy roster, through the fitted points map. Net per game uses the team's pace. Injury effect now is what its current injury report does to its margin, in points.

| # | Team | Net per 100 | Net per game | Offense | Defense | Pace | Injury effect now | Elo |
|---|---|---|---|---|---|---|---|---|
| 1 | BOS | +6.5 | +6.4 | +3.7 | +2.8 | 97.9 | +1.2 | 1609 |
| 2 | SAS | +6.1 | +6.4 | +1.7 | +4.4 | 105.5 | +0.7 | 1677 |
| 3 | HOU | +5.7 | +5.7 | +3.3 | +2.4 | 100.8 | -3.2 | 1587 |
| 4 | OKC | +5.2 | +5.3 | +0.1 | +5.0 | 102.2 | +1.8 | 1708 |
| 5 | NYK | +5.0 | +5.1 | +1.9 | +3.2 | 100.3 | -0.1 | 1704 |
| 6 | DET | +4.0 | +4.2 | +2.0 | +2.1 | 103.8 | -0.8 | 1635 |
| 7 | POR | +3.3 | +3.4 | +2.2 | +1.1 | 103.2 | +0.6 | 1549 |
| 8 | TOR | +3.0 | +3.3 | +0.4 | +2.7 | 108.0 | +0.8 | 1560 |
| 9 | CLE | +3.0 | +3.2 | +2.0 | +0.9 | 105.9 | +0.0 | 1572 |
| 10 | MIN | +2.7 | +2.8 | +1.1 | +1.6 | 103.9 | -0.2 | 1599 |
| 11 | LAL | +2.4 | +2.5 | +2.0 | +0.5 | 103.5 | +1.1 | 1582 |
| 12 | PHI | +2.3 | +2.5 | -0.1 | +2.4 | 108.4 | +0.1 | 1557 |
| 13 | DEN | +2.1 | +2.1 | +2.9 | -0.8 | 99.9 | +2.0 | 1591 |
| 14 | ATL | +1.1 | +1.2 | +0.8 | +0.3 | 107.6 | +0.8 | 1589 |
| 15 | ORL | +0.4 | +0.4 | -1.7 | +2.0 | 105.0 | +1.6 | 1520 |
| 16 | PHX | -0.1 | -0.1 | +0.8 | -0.9 | 100.4 | +0.1 | 1505 |
| 17 | MIA | -0.5 | -0.5 | +0.5 | -1.0 | 106.7 | +0.0 | 1489 |
| 18 | GSW | -0.6 | -0.6 | -0.1 | -0.5 | 101.5 | -4.0 | 1435 |
| 19 | LAC | -1.4 | -1.4 | -0.3 | -1.0 | 102.9 | +1.3 | 1526 |
| 20 | DAL | -1.6 | -1.7 | -0.8 | -0.8 | 103.6 | -2.7 | 1406 |
| 21 | IND | -2.1 | -2.3 | +0.0 | -2.1 | 105.4 | +0.6 | 1370 |
| 22 | CHA | -3.0 | -3.1 | -3.0 | +0.0 | 102.3 | -1.0 | 1555 |
| 23 | MEM | -3.4 | -3.6 | -0.9 | -2.5 | 103.4 | -0.9 | 1358 |
| 24 | UTA | -3.8 | -4.0 | -2.2 | -1.6 | 105.1 | +0.1 | 1333 |
| 25 | MIL | -5.7 | -6.0 | -1.5 | -4.2 | 105.6 | +0.0 | 1364 |
| 26 | WAS | -5.8 | -6.2 | -2.7 | -3.0 | 106.5 | +0.8 | 1293 |
| 27 | NOP | -5.8 | -6.1 | -2.0 | -3.8 | 105.0 | +0.2 | 1416 |
| 28 | CHI | -6.0 | -6.6 | -3.4 | -2.6 | 110.9 | +0.8 | 1384 |
| 29 | BKN | -6.4 | -6.7 | -3.6 | -2.8 | 103.6 | +0.4 | 1317 |
| 30 | SAC | -6.5 | -6.8 | -2.9 | -3.6 | 104.7 | +0.9 | 1361 |

## Top players

Regularized adjusted plus-minus from every lineup this season and past ones: points per 100 possessions a player adds on offense and saves on defense, against an average player, shrunk toward last season's rating. Players expected to play 20 minutes or more.

| # | Player | Team | Net impact per 100 | Offense | Defense | Expected minutes |
|---|---|---|---|---|---|---|
| 1 | Shai Gilgeous-Alexander | OKC | +6.0 | +5.1 | +0.9 | 36 |
| 2 | Victor Wembanyama | SAS | +5.2 | +0.7 | +4.4 | 35 |
| 3 | Nikola Jokic | DEN | +5.2 | +5.4 | -0.2 | 38 |
| 4 | Kawhi Leonard | TOR | +4.4 | +3.7 | +0.8 | 30 |
| 5 | Giannis Antetokounmpo | MIA | +4.1 | +3.8 | +0.2 | 30 |
| 6 | Alex Caruso | OKC | +4.0 | -0.2 | +4.2 | 25 |
| 7 | Joel Embiid | PHI | +3.2 | +1.7 | +1.6 | 33 |
| 8 | Luka Doncic | LAL | +3.2 | +4.0 | -0.8 | 34 |
| 9 | Dyson Daniels | ATL | +2.7 | +1.4 | +1.3 | 26 |
| 10 | Kyrie Irving | DAL | +2.6 | +2.6 | +0.0 | 26 |
| 11 | Marcus Smart | HOU | +2.4 | +1.1 | +1.3 | 27 |
| 12 | Chet Holmgren | OKC | +2.4 | +0.4 | +2.0 | 29 |
| 13 | Jimmy Butler III | GSW | +2.2 | +2.1 | +0.1 | 27 |
| 14 | Ausar Thompson | DET | +2.2 | +0.2 | +2.1 | 26 |
| 15 | Lauri Markkanen | UTA | +2.2 | +1.7 | +0.5 | 32 |
| 16 | Franz Wagner | ORL | +2.1 | +0.8 | +1.3 | 30 |
| 17 | Fred VanVleet | HOU | +2.1 | +1.4 | +0.7 | 35 |
| 18 | Derrick White | BOS | +2.0 | +0.3 | +1.7 | 36 |
| 19 | Jarrett Allen | CLE | +1.9 | +1.3 | +0.7 | 29 |
| 20 | Rudy Gobert | MIN | +1.7 | -2.9 | +4.7 | 29 |
| 21 | Pascal Siakam | IND | +1.7 | +1.7 | +0.0 | 31 |
| 22 | Cade Cunningham | DET | +1.6 | +1.7 | -0.2 | 35 |
| 23 | Nickeil Alexander-Walker | ATL | +1.6 | +1.9 | -0.3 | 30 |
| 24 | LaMelo Ball | MIN | +1.4 | +3.8 | -2.4 | 28 |
| 25 | Jrue Holiday | POR | +1.3 | +0.3 | +1.0 | 30 |
| 26 | Donovan Mitchell | CLE | +1.3 | +1.8 | -0.6 | 36 |
| 27 | Bam Adebayo | MIA | +1.3 | +0.8 | +0.5 | 26 |
| 28 | OG Anunoby | NYK | +1.2 | -0.2 | +1.4 | 34 |
| 29 | Ty Jerome | MEM | +1.2 | +2.9 | -1.7 | 29 |
| 30 | Damian Lillard | POR | +1.2 | +1.9 | -0.7 | 27 |

## Current model fit

- Fitted on 5310 games from 2022-23 to 2026-27.
- Home court: +2.0 points per 100 possessions for the home team over the visitor (about 2.0 points a game).
- Second night of a back-to-back: -0.7 points per 100 scored, +1.2 allowed.
- Weights: team efficiency ratings 0.16 (offense) and 0.16 (defense); player lineup ratings 0.76 and 0.75.
- Blend: 82% on the betting line for the margin and 100% for the total, wherever there is a line (fitted on past closing lines).
- Simulator: each team's points vary by 10.9 with correlation 0.23; 5.1% of recent games went to overtime.
