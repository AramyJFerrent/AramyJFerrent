# NBA score predictions

Updated Mon Nov 16, 2026 08:06 PM ET. Refreshed automatically several times a day during the season, around the injury report's deadlines; each game's prediction is locked at tip-off and graded once the final score is in.

Each team's expected points are its expected possessions times its expected points per possession, from team efficiency ratings and the ratings of the players expected to play, blended with the betting line. Each game is then simulated 10,000 times, overtime included. The predicted score is the expected points rounded; the 80% range holds 80% of simulated outcomes for each team. Basketball is the most predictable major sport, but a team's score still varies by about ±14 points around the forecast, so read the win chance and the ranges too.

Missing players come from the injury report: out players are left out, and doubtful, questionable and probable ones count with the share of their minutes their chance of playing implies, and their minutes go mostly to the bench. The effect is how many points of margin the team gains or loses against its full-strength roster: negative when it is missing good players, positive when the minutes go to better ones. Predictions are rerun when the report changes, up to tip-off.

The fair moneyline is the American odds that match the win chance exactly, with no bookmaker margin: -150 means risk $150 to win $100, +150 means risk $100 to win $150.

The edge columns check every side of the spread, the moneyline and the total for expected value: the profit per $1 bet at the posted price, using the final prediction's chances (the model blended with the line, simulated against the posted lines, pushes returning the stake, and anchored to the market's own chances so only what the blend moves off the line counts). The model's own spread and total are shown alongside, but the blend keeps only the share of that disagreement the model has earned in past seasons, so edges are rare. A side is an edge when its EV is 3% or more; the best such side is shown with its price, its EV, its chance of winning the bet and its stake, a 25% share of the Kelly stake in units of 1% of the bankroll, with at most 3 units on one game. Where a spread or total price is not posted it is assumed to be -110 (marked \*); a moneyline is never assumed. Edges are logged with each prediction, locked at tip-off and graded below. Treat them as an experiment, not betting advice; see the backtest for how they have done on past seasons.

## Monday, November 16

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Spread: model / line | Total: model / line | 80% range | Overtime | Missing (effect on margin) | Spread edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 9:00 PM | PHX @ DEN | PHX 110, DEN 119 | DEN 75% | PHX +310 / DEN -310<br>posted PHX +333 / DEN -426 | DEN -9.3 / DEN -9.5 (fav covers 49%) | 229.5 / 229.5 (over 49%) | 95–125 / 105–133 | 4% | PHX: Mark Williams (out); Ryan Dunn (day-to-day) (+0.3) | no edge | no edge | no edge |

## Tuesday, November 17

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Spread: model / line | Total: model / line | 80% range | Overtime | Missing (effect on margin) | Spread edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 7:30 PM | NYK @ TOR | NYK 110, TOR 107 | NYK 60% | NYK -150 / TOR +150<br>posted NYK -152 / TOR +128 | NYK -3.4 / NYK -3.5 (fav covers 51%) | 216.7 / 216.5 (over 49%) | 96–124 / 93–121 | 6% | TOR: Kawhi Leonard (out) (-1.8) | no edge | no edge | no edge |
| 8:00 PM | POR @ MIN | POR 114, MIN 116 | MIN 55% | POR +120 / MIN -120 | MIN -1.6 | 229.9 | 99–129 / 101–130 | 6% | POR: Ja Morant (out); Chris Youngblood (out) (+0.8)<br>MIN: Anthony Edwards (out); Donte DiVincenzo (out); Jaylen Clark (out) (-0.9) | no line yet | no line yet | no line yet |
| 8:00 PM | DET @ SAS | DET 107, SAS 114 | SAS 71% | DET +240 / SAS -240<br>posted DET +277 / SAS -345 | SAS -7.1 / SAS -7.5 (fav covers 49%) | 220.5 / 220.5 (over 49%) | 92–121 / 99–128 | 5% | DET: Duncan Robinson (out); Jalen Duren (out); Ronald Holland II (out) (+0.0)<br>SAS: Tobias Harris (out) (+0.8) | no edge | no edge | no edge |
| 10:30 PM | UTA @ LAC | UTA 109, LAC 115 | LAC 66% | UTA +195 / LAC -195<br>posted UTA +182 / LAC -219 | LAC -5.5 / LAC -5.5 (fav covers 51%) | 223.6 / 223.5 (over 49%) | 95–124 / 100–129 | 5% | UTA: Lauri Markkanen (out); Jaren Jackson Jr. (out); Jaxson Hayes (day-to-day); Jusuf Nurkic (out) (-2.8)<br>LAC: Brandon Ingram (out); Jordan Miller (out); Bradley Beal (out); Yanic Konan Niederhauser (out) (+0.7) | no edge | no edge | no edge |
| 11:00 PM | CHA @ LAL | CHA 103, LAL 115 | LAL 81% | CHA +430 / LAL -430<br>posted CHA +431 / LAL -578 | LAL -11.8 / LAL -11.5 (fav covers 49%) | 218.2 / 218.5 (over 49%) | 89–118 / 101–129 | 4% | CHA: Dennis Schroder (out); Kon Knueppel (out) (-0.4)<br>LAL: Austin Reaves (day-to-day) (-0.3) | no edge | no edge | no edge |

## How the 2026-27 predictions have done

| Predictor | Games | Margin MAE | Total MAE | Team-points MAE | Log loss | Brier | Winners | 80% range hit |
|---|---|---|---|---|---|---|---|---|
| Final prediction | 197 | 11.16 | 14.18 | 9.30 | 0.551 | 0.186 | 72.6% | 81.0% |
| Model only (before blending) | 197 | 11.42 | 13.94 | 9.32 | 0.569 | 0.193 | 71.6% | – |
| Elo | 197 | 11.79 | – | – | 0.589 | 0.203 | 66.5% | – |
| Final prediction, games with a line | 197 | 11.16 | 14.18 | 9.30 | 0.551 | 0.186 | 72.6% | 81.0% |
| Model only, games with a line | 197 | 11.42 | 13.94 | 9.32 | 0.569 | 0.193 | 71.6% | – |
| Betting line | 197 | 11.13 | 14.19 | 9.29 | 0.545 | 0.183 | 72.6% | – |

MAE is the average miss in points; team-points MAE is the average miss on each team's score. Log loss and Brier score the win chances (lower is better; a coin flip scores 0.693 and 0.250). The closing line misses margins by about 10 points and totals by about 14.

Overtime: predicted in 4.6% of games, happened in 5.6%.

### Betting edges

| Market | Edges | Record (W-L-P) | Staked | Units won | ROI | Expected ROI |
|---|---|---|---|---|---|---|
| Spread | 1 | 1-0-0 | 1.0 | +0.90 | +89.3% | +3.6% |
| Moneyline | 15 | 2-13-0 | 5.6 | -2.59 | -46.2% | +6.5% |
| Total | 0 | 0-0-0 | 0.0 | +0.00 | – | – |

Spread moved toward the model's first spread edge before tip-off: 5 of 6 games (83%).

Live predictions only, each edge at the stake and price logged with the last prediction before tip-off (edges logged before edges were priced from the final prediction are left out); a push returns the stake. Units are 1% of the bankroll; ROI is units won per unit staked, and expected ROI is what the edges' EVs promised. The line moving toward the model's edge before tip-off is the quickest sign that it knows something the market doesn't yet.

### Results, Sunday, November 15

| Game | Predicted | Final | Win chance for winner | Spread: model / line | Inside 80% ranges |
|---|---|---|---|---|---|
| IND @ PHI | 109–116 | 124–131 | 69% | PHI -6.6 / PHI -7.5 | no |
| LAL @ PHX | 115–112 | 131–123 | 59% | LAL -3 / LAL -3.5 | no |
| CHA @ LAC | 108–107 | 105–113 | 49% | CHA -0.4 / CHA -1.5 | yes |
| SAS @ UTA | 120–104 | 110–102 | 87% | SAS -15.1 / SAS -15.5 | yes |
| DAL @ BOS | 101–116 | 94–131 | 87% | BOS -14.9 / BOS -14.5 | no |
| NYK @ TOR | 111–107 | 112–108 (OT) | 63% | NYK -4.4 / NYK -4.5 | yes |
| HOU @ WAS | 116–108 | 147–119 | 73% | HOU -8.2 / HOU -8.5 | no |
| ATL @ MIL | 121–112 | 113–106 | 73% | ATL -8.2 / ATL -8.5 | yes |
| OKC @ SAC | 117–105 | 125–103 | 82% | OKC -11.7 / OKC -12.5 | yes |

## Power ratings

Points per 100 possessions better than an average team on a neutral floor, combining opponent-adjusted team efficiency (garbage time removed) with the ratings of the team's healthy roster, through the fitted points map. Net per game uses the team's pace. Injury effect now is what its current injury report does to its margin, in points.

| # | Team | Net per 100 | Net per game | Offense | Defense | Pace | Injury effect now | Elo |
|---|---|---|---|---|---|---|---|---|
| 1 | BOS | +8.2 | +7.8 | +4.2 | +4.0 | 94.9 | -0.9 | 1675 |
| 2 | SAS | +8.0 | +7.9 | +3.3 | +4.7 | 99.1 | +0.8 | 1734 |
| 3 | HOU | +6.9 | +6.8 | +3.8 | +3.1 | 98.2 | -1.7 | 1632 |
| 4 | LAL | +5.4 | +5.6 | +4.5 | +0.9 | 103.0 | -0.3 | 1631 |
| 5 | DET | +5.4 | +5.4 | +2.5 | +2.8 | 101.0 | +0.0 | 1626 |
| 6 | MIN | +4.9 | +5.0 | +1.7 | +3.2 | 103.5 | -0.9 | 1605 |
| 7 | DEN | +4.2 | +4.1 | +4.3 | -0.1 | 97.6 | +0.2 | 1585 |
| 8 | NYK | +4.1 | +3.9 | +0.9 | +3.2 | 94.6 | +0.0 | 1681 |
| 9 | POR | +3.6 | +3.7 | +2.8 | +0.9 | 101.7 | +0.8 | 1582 |
| 10 | OKC | +3.5 | +3.5 | -0.5 | +4.0 | 102.0 | -0.2 | 1652 |
| 11 | PHI | +2.1 | +2.2 | +0.6 | +1.5 | 101.2 | +0.2 | 1569 |
| 12 | GSW | +1.2 | +1.3 | +0.6 | +0.7 | 100.6 | -2.8 | 1526 |
| 13 | MIA | +0.4 | +0.4 | +1.5 | -1.1 | 104.5 | +0.6 | 1528 |
| 14 | TOR | +0.3 | +0.3 | -0.4 | +0.8 | 101.1 | -1.9 | 1508 |
| 15 | CLE | +0.2 | +0.2 | +1.8 | -1.6 | 100.4 | -0.9 | 1573 |
| 16 | PHX | -0.3 | -0.3 | +0.4 | -0.7 | 102.2 | +0.3 | 1499 |
| 17 | MEM | -1.0 | -1.1 | +0.8 | -1.8 | 102.4 | -1.4 | 1455 |
| 18 | IND | -1.1 | -1.1 | -0.1 | -0.9 | 103.4 | +0.2 | 1371 |
| 19 | ORL | -1.2 | -1.2 | -2.6 | +1.3 | 100.1 | +1.2 | 1506 |
| 20 | DAL | -2.2 | -2.2 | -1.0 | -1.1 | 102.3 | -0.2 | 1431 |
| 21 | ATL | -2.3 | -2.5 | -2.0 | -0.3 | 107.8 | +1.5 | 1530 |
| 22 | LAC | -3.0 | -3.0 | -1.3 | -1.7 | 101.0 | +0.7 | 1484 |
| 23 | UTA | -3.3 | -3.4 | -3.0 | -0.4 | 100.8 | -2.8 | 1282 |
| 24 | CHI | -4.4 | -4.8 | -2.2 | -2.3 | 108.1 | +1.5 | 1389 |
| 25 | CHA | -5.7 | -5.5 | -5.1 | -0.6 | 96.8 | -0.3 | 1469 |
| 26 | BKN | -5.7 | -5.8 | -2.9 | -2.8 | 100.8 | +0.0 | 1339 |
| 27 | NOP | -5.7 | -6.0 | -2.0 | -3.7 | 104.3 | -0.3 | 1343 |
| 28 | WAS | -6.0 | -6.1 | -2.9 | -3.2 | 100.7 | -0.1 | 1312 |
| 29 | MIL | -8.2 | -8.3 | -3.8 | -4.5 | 101.0 | +0.0 | 1315 |
| 30 | SAC | -8.3 | -8.5 | -4.1 | -4.2 | 102.4 | +0.4 | 1317 |

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
| 7 | Giannis Antetokounmpo | MIA | +3.9 | +3.8 | +0.1 | 32 |
| 8 | Kyrie Irving | DAL | +3.5 | +3.6 | -0.1 | 33 |
| 9 | Joel Embiid | PHI | +3.0 | +1.4 | +1.5 | 29 |
| 10 | Neemias Queta | BOS | +2.9 | +1.2 | +1.6 | 21 |
| 11 | Donovan Mitchell | CLE | +2.6 | +3.3 | -0.7 | 33 |
| 12 | Franz Wagner | ORL | +2.5 | +1.4 | +1.1 | 38 |
| 13 | Derrick White | BOS | +2.4 | +0.6 | +1.8 | 28 |
| 14 | LaMelo Ball | MIN | +2.4 | +4.1 | -1.7 | 29 |
| 15 | Fred VanVleet | HOU | +2.3 | +1.5 | +0.8 | 32 |
| 16 | Jimmy Butler III | GSW | +2.2 | +2.1 | +0.1 | 27 |
| 17 | Jarrett Allen | CLE | +2.2 | +2.0 | +0.2 | 27 |
| 18 | Chet Holmgren | OKC | +2.1 | +0.0 | +2.1 | 30 |
| 19 | Ausar Thompson | DET | +2.1 | +0.1 | +1.9 | 28 |
| 20 | Bam Adebayo | MIA | +2.0 | +1.8 | +0.3 | 36 |
| 21 | Dyson Daniels | ATL | +1.9 | +0.2 | +1.8 | 31 |
| 22 | Paul George | BOS | +1.9 | +0.9 | +1.0 | 28 |
| 23 | Ty Jerome | MEM | +1.8 | +2.8 | -1.0 | 30 |
| 24 | Day'Ron Sharpe | BKN | +1.8 | +0.7 | +1.0 | 24 |
| 25 | Jrue Holiday | POR | +1.8 | +0.8 | +0.9 | 27 |
| 26 | De'Aaron Fox | SAS | +1.8 | +1.7 | +0.1 | 24 |
| 27 | Pascal Siakam | IND | +1.7 | +1.5 | +0.2 | 33 |
| 28 | Paul Reed | DET | +1.7 | +0.4 | +1.3 | 27 |
| 29 | Rudy Gobert | MIN | +1.7 | -3.4 | +5.0 | 27 |
| 30 | Herbert Jones | NOP | +1.6 | -1.2 | +2.8 | 27 |

## Current model fit

- Fitted on 5479 games from 2022-23 to 2026-27.
- Home court: +2.0 points per 100 possessions for the home team over the visitor (about 2.0 points a game).
- Second night of a back-to-back: -0.7 points per 100 scored, +1.2 allowed.
- Weights: team efficiency ratings 0.15 (offense) and 0.15 (defense); player lineup ratings 0.77 and 0.76.
- Blend: 82% on the betting line for the margin and 100% for the total, wherever there is a line (fitted on past closing lines).
- Simulator: each team's points vary by 10.9 with correlation 0.23; 5.2% of recent games went to overtime.
