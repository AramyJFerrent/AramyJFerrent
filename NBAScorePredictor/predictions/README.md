# NBA score predictions

Updated Wed Oct 28, 2026 10:27 PM ET. Refreshed automatically several times a day during the season, around the injury report's deadlines; each game's prediction is locked at tip-off and graded once the final score is in.

Each team's expected points are its expected possessions times its expected points per possession, from team efficiency ratings and the ratings of the players expected to play, blended with the betting line. Each game is then simulated 10,000 times, overtime included. The predicted score is the expected points rounded; the 80% range holds 80% of simulated outcomes for each team. Basketball is the most predictable major sport, but a team's score still varies by about ±14 points around the forecast, so read the win chance and the ranges too.

Missing players come from the injury report: out players are left out, and doubtful, questionable and probable ones count with the share of their minutes their chance of playing implies, and their minutes go mostly to the bench. The effect is how many points of margin the team gains or loses against its full-strength roster: negative when it is missing good players, positive when the minutes go to better ones. Predictions are rerun when the report changes, up to tip-off.

The fair moneyline is the American odds that match the win chance exactly, with no bookmaker margin: -150 means risk $150 to win $100, +150 means risk $100 to win $150.

The edge columns check every side of the spread, the moneyline and the total for expected value: the profit per $1 bet at the posted price, using the final prediction's chances (the model blended with the line, simulated against the posted lines, pushes returning the stake, and anchored to the market's own chances so only what the blend moves off the line counts). The model's own spread and total are shown alongside, but the blend keeps only the share of that disagreement the model has earned in past seasons, so edges are rare. A side is an edge when its EV is 3% or more; the best such side is shown with its price, its EV, its chance of winning the bet and its stake, a 25% share of the Kelly stake in units of 1% of the bankroll, with at most 3 units on one game. Where a spread or total price is not posted it is assumed to be -110 (marked \*); a moneyline is never assumed. Edges are logged with each prediction, locked at tip-off and graded below. Treat them as an experiment, not betting advice; see the backtest for how they have done on past seasons.

## Wednesday, October 28

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Spread: model / line | Total: model / line | 80% range | Overtime | Missing (effect on margin) | Spread edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 10:30 PM | LAL @ LAC | LAL 111, LAC 113 | LAC 55% | LAL +125 / LAC -125<br>posted LAL -108 / LAC -112 | LAC -1.8 / LAC -1.5 (fav covers 53%) | 224.8 / 224.5 (over 50%) | 97–126 / 99–128 | 6% | LAL: Luka Doncic (out); Ziaire Williams (out) (-1.8)<br>LAC: Rui Hachimura (out); Max Strus (out); Brandon Ingram (out); Jordan Miller (out); Bradley Beal (out); Yanic Konan Niederhauser (out) (+0.8) | no edge | no edge | no edge |

## Thursday, October 29

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Spread: model / line | Total: model / line | 80% range | Overtime | Missing (effect on margin) | Spread edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 8:00 PM | CLE @ ATL | CLE 119, ATL 121 | ATL 54% | CLE +120 / ATL -120<br>posted CLE -110 / ATL -110 | ATL -1.4 / ATL -1.5 (fav covers 52%) | 239.6 / 239.5 (over 50%) | 104–134 / 106–135 | 5% | – | no edge | no edge | no edge |
| 8:00 PM | SAC @ NOP | SAC 117, NOP 122 | NOP 64% | SAC +180 / NOP -180<br>posted SAC +170 / NOP -205 | NOP -4.9 / NOP -5.5 (fav covers 50%) | 238.8 / 238.5 (over 50%) | 102–132 / 107–137 | 6% | SAC: Maxime Raynaud (out); Keegan Murray (out); Dylan Cardwell (out) (+0.2)<br>NOP: Yves Missi (out); Jordan Poole (day-to-day) (+0.3) | no edge | no edge | no edge |
| 10:00 PM | MEM @ POR | MEM 113, POR 121 | POR 72% | MEM +260 / POR -260<br>posted MEM +215 / POR -265 | POR -7.8 / POR -7.5 (fav covers 52%) | 233.4 / 233.5 (over 48%) | 98–128 / 106–135 | 5% | – | no edge | no edge | no edge |

## How the 2026-27 predictions have done

| Predictor | Games | Margin MAE | Total MAE | Team-points MAE | Log loss | Brier | Winners | 80% range hit |
|---|---|---|---|---|---|---|---|---|
| Final prediction | 56 | 11.11 | 14.62 | 9.36 | 0.579 | 0.199 | 69.6% | 80.4% |
| Model only (before blending) | 56 | 11.94 | 14.35 | 9.69 | 0.618 | 0.217 | 62.5% | – |
| Elo | 56 | 11.93 | – | – | 0.639 | 0.227 | 58.9% | – |
| Final prediction, games with a line | 56 | 11.11 | 14.62 | 9.36 | 0.579 | 0.199 | 69.6% | 80.4% |
| Model only, games with a line | 56 | 11.94 | 14.35 | 9.69 | 0.618 | 0.217 | 62.5% | – |
| Betting line | 56 | 10.96 | 14.59 | 9.30 | 0.566 | 0.193 | 69.6% | – |

MAE is the average miss in points; team-points MAE is the average miss on each team's score. Log loss and Brier score the win chances (lower is better; a coin flip scores 0.693 and 0.250). The closing line misses margins by about 10 points and totals by about 14.

Overtime: predicted in 4.8% of games, happened in 5.4%.

### Betting edges

| Market | Edges | Record (W-L-P) | Staked | Units won | ROI | Expected ROI |
|---|---|---|---|---|---|---|
| Spread | 1 | 1-0-0 | 1.0 | +0.90 | +89.3% | +3.6% |
| Moneyline | 3 | 0-3-0 | 1.2 | -1.19 | -100.0% | +11.2% |
| Total | 0 | 0-0-0 | 0.0 | +0.00 | – | – |

Spread moved toward the model's first spread edge before tip-off: 4 of 5 games (80%).

Live predictions only, each edge at the stake and price logged with the last prediction before tip-off (edges logged before edges were priced from the final prediction are left out); a push returns the stake. Units are 1% of the bankroll; ROI is units won per unit staked, and expected ROI is what the edges' EVs promised. The line moving toward the model's edge before tip-off is the quickest sign that it knows something the market doesn't yet.

### Results, Tuesday, October 27

| Game | Predicted | Final | Win chance for winner | Spread: model / line | Inside 80% ranges |
|---|---|---|---|---|---|
| BKN @ BOS | 105–118 | 124–125 (OT) | 83% | BOS -12.9 / BOS -12.5 | no |
| DET @ NYK | 108–112 | 97–111 | 61% | NYK -3.7 / NYK -4.5 | yes |
| SAC @ SAS | 107–125 | 103–130 | 91% | SAS -18.5 / SAS -18.5 | yes |
| POR @ LAL | 116–118 | 136–129 | 45% | LAL -1.9 / LAL -1.5 | no |

## Power ratings

Points per 100 possessions better than an average team on a neutral floor, combining opponent-adjusted team efficiency (garbage time removed) with the ratings of the team's healthy roster, through the fitted points map. Net per game uses the team's pace. Injury effect now is what its current injury report does to its margin, in points.

| # | Team | Net per 100 | Net per game | Offense | Defense | Pace | Injury effect now | Elo |
|---|---|---|---|---|---|---|---|---|
| 1 | HOU | +6.6 | +6.6 | +3.5 | +3.0 | 101.3 | -1.3 | 1605 |
| 2 | SAS | +6.3 | +6.6 | +1.9 | +4.4 | 104.5 | +0.7 | 1685 |
| 3 | BOS | +5.6 | +5.6 | +3.1 | +2.6 | 100.0 | +1.1 | 1615 |
| 4 | DET | +4.7 | +4.7 | +1.6 | +3.1 | 100.5 | -0.3 | 1639 |
| 5 | OKC | +4.7 | +4.8 | +0.0 | +4.7 | 102.9 | -2.2 | 1713 |
| 6 | POR | +4.4 | +4.5 | +3.5 | +0.9 | 102.5 | +0.4 | 1561 |
| 7 | NYK | +4.2 | +4.2 | +0.9 | +3.4 | 100.1 | -0.3 | 1692 |
| 8 | MIN | +3.9 | +4.0 | +1.4 | +2.5 | 101.6 | -1.2 | 1606 |
| 9 | CLE | +2.7 | +2.9 | +2.0 | +0.7 | 106.3 | +0.0 | 1577 |
| 10 | LAL | +2.4 | +2.4 | +3.2 | -0.9 | 102.8 | -1.9 | 1575 |
| 11 | PHI | +1.6 | +1.7 | -0.9 | +2.5 | 107.3 | +0.3 | 1549 |
| 12 | TOR | +1.4 | +1.5 | -0.7 | +2.1 | 106.7 | -2.0 | 1549 |
| 13 | ORL | +1.3 | +1.4 | -1.5 | +2.8 | 106.3 | +0.2 | 1540 |
| 14 | ATL | +0.8 | +0.9 | +0.6 | +0.3 | 108.0 | +0.8 | 1571 |
| 15 | GSW | +0.4 | +0.4 | +0.9 | -0.5 | 101.3 | -1.8 | 1461 |
| 16 | DEN | +0.2 | +0.2 | +2.4 | -2.2 | 99.8 | +1.7 | 1561 |
| 17 | MIA | -0.4 | -0.5 | +0.3 | -0.8 | 106.8 | +0.0 | 1474 |
| 18 | PHX | -0.7 | -0.7 | +1.0 | -1.8 | 101.7 | +0.3 | 1507 |
| 19 | LAC | -1.4 | -1.4 | -0.8 | -0.6 | 103.6 | +0.8 | 1524 |
| 20 | IND | -1.8 | -1.8 | -0.2 | -1.6 | 104.3 | -0.4 | 1383 |
| 21 | DAL | -1.9 | -2.0 | -1.3 | -0.6 | 104.1 | +0.4 | 1410 |
| 22 | CHA | -2.3 | -2.3 | -2.5 | +0.2 | 99.0 | -0.7 | 1561 |
| 23 | MEM | -2.3 | -2.4 | -0.3 | -2.1 | 102.5 | +0.0 | 1380 |
| 24 | UTA | -4.3 | -4.4 | -2.4 | -1.9 | 104.4 | -2.6 | 1321 |
| 25 | NOP | -5.0 | -5.4 | -1.5 | -3.5 | 106.1 | +0.3 | 1414 |
| 26 | WAS | -5.3 | -5.6 | -2.4 | -2.9 | 104.1 | +0.0 | 1302 |
| 27 | MIL | -5.4 | -5.7 | -1.7 | -3.7 | 105.6 | +0.0 | 1368 |
| 28 | BKN | -5.9 | -6.2 | -2.8 | -3.1 | 105.4 | +0.6 | 1293 |
| 29 | CHI | -7.1 | -8.0 | -4.3 | -2.9 | 112.8 | +0.8 | 1368 |
| 30 | SAC | -7.3 | -7.6 | -3.1 | -4.2 | 103.1 | +0.2 | 1344 |

## Top players

Regularized adjusted plus-minus from every lineup this season and past ones: points per 100 possessions a player adds on offense and saves on defense, against an average player, shrunk toward last season's rating. Players expected to play 20 minutes or more.

| # | Player | Team | Net impact per 100 | Offense | Defense | Expected minutes |
|---|---|---|---|---|---|---|
| 1 | Shai Gilgeous-Alexander | OKC | +6.3 | +5.3 | +1.0 | 34 |
| 2 | Victor Wembanyama | SAS | +6.1 | +1.3 | +4.8 | 31 |
| 3 | Nikola Jokic | DEN | +4.7 | +5.4 | -0.6 | 38 |
| 4 | Kawhi Leonard | TOR | +4.5 | +3.7 | +0.8 | 30 |
| 5 | Giannis Antetokounmpo | MIA | +3.5 | +3.5 | +0.0 | 32 |
| 6 | Luka Doncic | LAL | +3.5 | +4.9 | -1.4 | 36 |
| 7 | Joel Embiid | PHI | +3.3 | +1.8 | +1.5 | 34 |
| 8 | Kyrie Irving | DAL | +2.7 | +2.7 | -0.1 | 28 |
| 9 | Dyson Daniels | ATL | +2.5 | +1.2 | +1.3 | 27 |
| 10 | Franz Wagner | ORL | +2.5 | +0.8 | +1.6 | 33 |
| 11 | Fred VanVleet | HOU | +2.4 | +1.5 | +0.9 | 33 |
| 12 | Lauri Markkanen | UTA | +2.3 | +2.1 | +0.2 | 24 |
| 13 | Jimmy Butler III | GSW | +2.2 | +2.1 | +0.1 | 27 |
| 14 | Chet Holmgren | OKC | +2.0 | +0.0 | +2.0 | 30 |
| 15 | Ausar Thompson | DET | +2.0 | +0.0 | +2.1 | 26 |
| 16 | Rudy Gobert | MIN | +1.9 | -3.1 | +5.0 | 32 |
| 17 | Ty Jerome | MEM | +1.8 | +3.3 | -1.5 | 30 |
| 18 | Pascal Siakam | IND | +1.8 | +1.7 | +0.1 | 32 |
| 19 | Cade Cunningham | DET | +1.8 | +1.6 | +0.1 | 35 |
| 20 | Kevin Durant | HOU | +1.7 | +3.1 | -1.4 | 35 |
| 21 | Jrue Holiday | POR | +1.7 | +0.6 | +1.1 | 30 |
| 22 | LaMelo Ball | MIN | +1.7 | +4.0 | -2.3 | 26 |
| 23 | Jarrett Allen | CLE | +1.5 | +0.9 | +0.6 | 28 |
| 24 | Dean Wade | PHI | +1.4 | -0.1 | +1.5 | 25 |
| 25 | Paul Reed | DET | +1.4 | +0.1 | +1.3 | 22 |
| 26 | Bam Adebayo | MIA | +1.2 | +0.7 | +0.6 | 30 |
| 27 | Derrick White | BOS | +1.2 | -0.2 | +1.4 | 31 |
| 28 | Nickeil Alexander-Walker | ATL | +1.2 | +1.4 | -0.2 | 30 |
| 29 | Donovan Mitchell | CLE | +1.2 | +1.8 | -0.7 | 36 |
| 30 | Devin Vassell | SAS | +1.1 | +0.7 | +0.5 | 31 |

## Current model fit

- Fitted on 5338 games from 2022-23 to 2026-27.
- Home court: +2.0 points per 100 possessions for the home team over the visitor (about 2.0 points a game).
- Second night of a back-to-back: -0.7 points per 100 scored, +1.2 allowed.
- Weights: team efficiency ratings 0.16 (offense) and 0.16 (defense); player lineup ratings 0.76 and 0.75.
- Blend: 82% on the betting line for the margin and 100% for the total, wherever there is a line (fitted on past closing lines).
- Simulator: each team's points vary by 10.9 with correlation 0.23; 5.2% of recent games went to overtime.
