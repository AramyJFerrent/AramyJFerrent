# NBA score predictions

Updated Sat Oct 24, 2026 01:21 AM ET. Refreshed automatically several times a day during the season, around the injury report's deadlines; each game's prediction is locked at tip-off and graded once the final score is in.

Each team's expected points are its expected possessions times its expected points per possession, from team efficiency ratings and the ratings of the players expected to play, blended with the betting line. Each game is then simulated 10,000 times, overtime included. The predicted score is the expected points rounded; the 80% range holds 80% of simulated outcomes for each team. Basketball is the most predictable major sport, but a team's score still varies by about ±14 points around the forecast, so read the win chance and the ranges too.

Missing players come from the injury report: out players are left out, and doubtful, questionable and probable ones count with the share of their minutes their chance of playing implies, and their minutes go mostly to the bench. The effect is how many points of margin the team gains or loses against its full-strength roster: negative when it is missing good players, positive when the minutes go to better ones. Predictions are rerun when the report changes, up to tip-off.

The fair moneyline is the American odds that match the win chance exactly, with no bookmaker margin: -150 means risk $150 to win $100, +150 means risk $100 to win $150.

The edge columns check every side of the spread, the moneyline and the total for expected value: the profit per $1 bet at the posted price, using the final prediction's chances (the model blended with the line, simulated against the posted lines, pushes returning the stake, and anchored to the market's own chances so only what the blend moves off the line counts). The model's own spread and total are shown alongside, but the blend keeps only the share of that disagreement the model has earned in past seasons, so edges are rare. A side is an edge when its EV is 3% or more; the best such side is shown with its price, its EV, its chance of winning the bet and its stake, a 25% share of the Kelly stake in units of 1% of the bankroll, with at most 3 units on one game. Where a spread or total price is not posted it is assumed to be -110 (marked \*); a moneyline is never assumed. Edges are logged with each prediction, locked at tip-off and graded below. Treat them as an experiment, not betting advice; see the backtest for how they have done on past seasons.

## Saturday, October 24

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Spread: model / line | Total: model / line | 80% range | Overtime | Missing (effect on margin) | Spread edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 6:00 PM | MIA @ CHA | MIA 117, CHA 115 | MIA 57% | MIA -135 / CHA +135<br>posted MIA -155 / CHA +130 | MIA -2.7 / MIA -3.5 (fav covers 48%) | 231.8 / 231.5 (over 50%) | 103–132 / 100–129 | 5% | CHA: Kon Knueppel (day-to-day); Coby White (day-to-day); Grant Williams (day-to-day) (+0.3) | no edge | no edge | no edge |
| 7:30 PM | BKN @ CLE | BKN 110, CLE 121 | CLE 80% | BKN +390 / CLE -390<br>posted BKN +390 / CLE -520 | CLE -11.5 / CLE -11.5 (fav covers 49%) | 231.3 / 231.5 (over 48%) | 95–125 / 107–136 | 4% | – | no edge | no edge | no edge |
| 7:30 PM | MIL @ PHI | MIL 110, PHI 123 | PHI 82% | MIL +450 / PHI -450<br>posted MIL +455 / PHI -625 | PHI -12.5 / PHI -12.5 (fav covers 48%) | 233.3 / 233.5 (over 50%) | 96–125 / 109–137 | 3% | PHI: LeBron James (day-to-day); Dominick Barlow (out) (+0.0) | no edge | no edge | no edge |
| 8:00 PM | WAS @ CHI | WAS 122, CHI 121 | WAS 54% | WAS -115 / CHI +115<br>posted WAS -110 / CHI -110 | WAS -1.1 / WAS -1.5 (fav covers 51%) | 243.7 / 243.5 (over 50%) | 107–137 / 106–137 | 5% | WAS: Jamir Watkins (out); Tristan Vukcevic (out) (+0.4)<br>CHI: Nic Claxton (out) (+0.0) | no edge | no edge | no edge |
| 8:00 PM | SAS @ DAL | SAS 121, DAL 110 | SAS 80% | SAS -395 / DAL +395<br>posted SAS -470 / DAL +360 | SAS -11.1 / SAS -11.5 (fav covers 47%) | 230.3 / 230.5 (over 48%) | 107–135 / 95–124 | 4% | SAS: Tobias Harris (out) (+0.8)<br>DAL: Cooper Flagg (out); Santi Aldama (day-to-day); Dereck Lively II (out) (-0.3) | no edge | no edge | no edge |
| 8:30 PM | HOU @ ATL | HOU 115, ATL 116 | ATL 51% | HOU +105 / ATL -105<br>posted HOU +100 / ATL -120 | ATL -0.6 / ATL -1.5 (fav covers 49%) | 230.7 / 230.5 (over 50%) | 100–130 / 101–130 | 5% | HOU: Reed Sheppard (out) (+1.5) | no edge | no edge | no edge |
| 9:00 PM | NOP @ DEN | NOP 113, DEN 125 | DEN 80% | NOP +410 / DEN -410<br>posted NOP +370 / DEN -485 | DEN -12 / DEN -11.5 (fav covers 50%) | 237.3 / 237.5 (over 49%) | 98–128 / 110–139 | 4% | NOP: Yves Missi (day-to-day) (+0.1)<br>DEN: Spencer Jones (out); Cameron Johnson (out); Alpha Diallo (day-to-day) (+1.4) | no edge | no edge | no edge |
| 10:00 PM | GSW @ PHX | GSW 108, PHX 115 | PHX 70% | GSW +235 / PHX -235<br>posted GSW +200 / PHX -245 | PHX -7.1 / PHX -7.5 (fav covers 49%) | 223.5 / 223.5 (over 49%) | 94–123 / 101–129 | 5% | GSW: Moses Moody (out); Jimmy Butler III (out); Kristaps Porzingis (out) (-1.4)<br>PHX: Luke Kennard (day-to-day); Oso Ighodaro (day-to-day); Mark Williams (out) (+0.2) | no edge | no edge | no edge |

## Sunday, October 25

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Spread: model / line | Total: model / line | 80% range | Overtime | Missing (effect on margin) | Spread edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 5:00 PM | LAL @ UTA | LAL 115, UTA 111 | LAL 59% | LAL -145 / UTA +145 | LAL -3.3 | 226.3 | 101–129 / 97–126 | 5% | UTA: Trey Alexander (out); Jusuf Nurkic (out) (+0.1) | no line yet | no line yet | no line yet |
| 6:00 PM | IND @ BKN | IND 117, BKN 112 | IND 66% | IND -195 / BKN +195 | IND -5.5 | 229.2 | 103–132 / 97–126 | 5% | IND: Johnny Furphy (out); Ben Sheppard (out); T.J. McConnell (day-to-day) (+0.9) | no line yet | no line yet | no line yet |
| 7:00 PM | ORL @ NYK | ORL 110, NYK 114 | NYK 61% | ORL +160 / NYK -160 | NYK -3.7 | 223.5 | 96–124 / 99–128 | 5% | ORL: Paolo Banchero (day-to-day); Anthony Black (day-to-day) (+1.3) | no line yet | no line yet | no line yet |
| 7:00 PM | TOR @ MIN | TOR 116, MIN 117 | MIN 51% | TOR +105 / MIN -105 | pick'em | 232.2 | 101–131 / 101–131 | 5% | MIN: Donte DiVincenzo (out) (-0.3) | no line yet | no line yet | no line yet |
| 7:00 PM | LAC @ OKC | LAC 104, OKC 113 | OKC 75% | LAC +300 / OKC -300 | OKC -8.8 | 216.2 | 90–118 / 98–126 | 4% | LAC: Max Strus (out); Brandon Ingram (out); Jordan Miller (out); Bradley Beal (out); Yanic Konan Niederhauser (out) (+1.1) | no line yet | no line yet | no line yet |
| 7:30 PM | DET @ PHI | DET 113, PHI 114 | PHI 50% | DET +100 / PHI -100 | pick'em | 226.5 | 99–128 / 99–128 | 6% | DET: Ausar Thompson (day-to-day); Jalen Duren (day-to-day) (-0.5)<br>PHI: LeBron James (day-to-day); Dominick Barlow (out) (+0.0) | no line yet | no line yet | no line yet |
| 9:00 PM | MEM @ SAC | MEM 113, SAC 114 | SAC 51% | MEM +105 / SAC -105 | SAC -0.5 | 227.5 | 99–128 / 99–129 | 5% | MEM: Cedric Coward (out) (-0.4)<br>SAC: Maxime Raynaud (out); Dylan Cardwell (out) (+0.9) | no line yet | no line yet | no line yet |

## How the 2026-27 predictions have done

| Predictor | Games | Margin MAE | Total MAE | Team-points MAE | Log loss | Brier | Winners | 80% range hit |
|---|---|---|---|---|---|---|---|---|
| Final prediction | 16 | 14.21 | 14.86 | 10.29 | 0.581 | 0.197 | 75.0% | 75.0% |
| Model only (before blending) | 16 | 15.78 | 13.52 | 10.82 | 0.674 | 0.240 | 62.5% | – |
| Elo | 16 | 14.87 | – | – | 0.628 | 0.218 | 62.5% | – |
| Final prediction, games with a line | 16 | 14.21 | 14.86 | 10.29 | 0.581 | 0.197 | 75.0% | 75.0% |
| Model only, games with a line | 16 | 15.78 | 13.52 | 10.82 | 0.674 | 0.240 | 62.5% | – |
| Betting line | 16 | 13.88 | 14.81 | 10.16 | 0.560 | 0.188 | 75.0% | – |

MAE is the average miss in points; team-points MAE is the average miss on each team's score. Log loss and Brier score the win chances (lower is better; a coin flip scores 0.693 and 0.250). The closing line misses margins by about 10 points and totals by about 14.

Overtime: predicted in 4.9% of games, happened in 0.0%.

### Betting edges

| Market | Edges | Record (W-L-P) | Staked | Units won | ROI | Expected ROI |
|---|---|---|---|---|---|---|
| Spread | 0 | 0-0-0 | 0.0 | +0.00 | – | – |
| Moneyline | 0 | 0-0-0 | 0.0 | +0.00 | – | – |
| Total | 0 | 0-0-0 | 0.0 | +0.00 | – | – |

Spread moved toward the model's first spread edge before tip-off: 4 of 5 games (80%).

Live predictions only, each edge at the stake and price logged with the last prediction before tip-off (edges logged before edges were priced from the final prediction are left out); a push returns the stake. Units are 1% of the bankroll; ROI is units won per unit staked, and expected ROI is what the edges' EVs promised. The line moving toward the model's edge before tip-off is the quickest sign that it knows something the market doesn't yet.

### Results, Thursday, October 22

| Game | Predicted | Final | Win chance for winner | Spread: model / line | Inside 80% ranges |
|---|---|---|---|---|---|
| CLE @ PHI | 118–120 | 106–114 | 58% | PHI -2.4 / PHI -2.5 | yes |
| DEN @ OKC | 115–122 | 84–96 | 71% | OKC -7.4 / OKC -7.5 | no |

## Power ratings

Points per 100 possessions better than an average team on a neutral floor, combining opponent-adjusted team efficiency (garbage time removed) with the ratings of the team's healthy roster, through the fitted points map. Net per game uses the team's pace. Injury effect now is what its current injury report does to its margin, in points.

| # | Team | Net per 100 | Net per game | Offense | Defense | Pace | Injury effect now | Elo |
|---|---|---|---|---|---|---|---|---|
| 1 | SAS | +6.9 | +7.4 | +2.0 | +4.9 | 106.8 | +0.8 | 1687 |
| 2 | BOS | +6.4 | +6.4 | +3.5 | +2.9 | 101.0 | +1.1 | 1602 |
| 3 | HOU | +5.1 | +5.2 | +2.8 | +2.4 | 102.0 | +1.5 | 1576 |
| 4 | OKC | +4.9 | +5.0 | +0.2 | +4.8 | 102.0 | +1.7 | 1708 |
| 5 | NYK | +4.6 | +4.8 | +1.4 | +3.2 | 103.2 | +0.0 | 1711 |
| 6 | POR | +3.3 | +3.3 | +1.6 | +1.7 | 101.6 | +1.5 | 1543 |
| 7 | CLE | +3.2 | +3.5 | +2.2 | +1.0 | 106.3 | +0.0 | 1572 |
| 8 | DET | +2.9 | +3.0 | +1.5 | +1.4 | 102.2 | -0.5 | 1623 |
| 9 | PHI | +2.5 | +2.7 | +0.1 | +2.4 | 107.9 | +0.0 | 1557 |
| 10 | TOR | +2.5 | +2.6 | +0.7 | +1.8 | 107.5 | +0.7 | 1556 |
| 11 | DEN | +2.4 | +2.4 | +3.1 | -0.7 | 100.2 | +1.4 | 1591 |
| 12 | ORL | +1.7 | +1.8 | -0.5 | +2.2 | 107.2 | +1.4 | 1540 |
| 13 | MIN | +1.7 | +1.8 | +1.0 | +0.7 | 106.6 | -0.3 | 1580 |
| 14 | ATL | +0.9 | +0.9 | +1.0 | -0.1 | 108.1 | +0.8 | 1543 |
| 15 | LAL | +0.8 | +0.9 | +0.9 | -0.1 | 102.5 | +1.0 | 1577 |
| 16 | MIA | +0.5 | +0.6 | +0.8 | -0.2 | 105.2 | +0.0 | 1501 |
| 17 | PHX | +0.1 | +0.1 | +1.0 | -0.8 | 101.0 | +0.2 | 1505 |
| 18 | GSW | -0.5 | -0.5 | +0.0 | -0.5 | 103.6 | -1.5 | 1444 |
| 19 | CHA | -0.7 | -0.8 | -1.5 | +0.7 | 103.3 | +0.4 | 1601 |
| 20 | IND | -1.0 | -1.1 | +0.6 | -1.6 | 105.6 | +1.0 | 1388 |
| 21 | LAC | -1.4 | -1.5 | -0.7 | -0.8 | 102.7 | +1.1 | 1532 |
| 22 | DAL | -2.8 | -2.9 | -1.3 | -1.5 | 103.7 | -0.3 | 1388 |
| 23 | UTA | -3.5 | -3.7 | -2.2 | -1.3 | 105.4 | +0.1 | 1329 |
| 24 | MEM | -3.8 | -4.0 | -1.0 | -2.8 | 105.1 | -0.4 | 1349 |
| 25 | MIL | -5.3 | -5.5 | -1.5 | -3.8 | 104.0 | +0.0 | 1374 |
| 26 | WAS | -5.9 | -6.2 | -2.2 | -3.6 | 106.0 | +0.4 | 1298 |
| 27 | NOP | -6.0 | -6.3 | -2.3 | -3.7 | 105.6 | +0.1 | 1421 |
| 28 | BKN | -6.2 | -6.4 | -3.5 | -2.7 | 103.5 | +0.4 | 1317 |
| 29 | SAC | -6.7 | -7.0 | -3.4 | -3.3 | 103.3 | +0.9 | 1367 |
| 30 | CHI | -6.8 | -7.4 | -4.3 | -2.5 | 109.3 | +0.0 | 1374 |

## Top players

Regularized adjusted plus-minus from every lineup this season and past ones: points per 100 possessions a player adds on offense and saves on defense, against an average player, shrunk toward last season's rating. Players expected to play 20 minutes or more.

| # | Player | Team | Net impact per 100 | Offense | Defense | Expected minutes |
|---|---|---|---|---|---|---|
| 1 | Shai Gilgeous-Alexander | OKC | +6.0 | +5.1 | +0.9 | 36 |
| 2 | Victor Wembanyama | SAS | +5.4 | +0.9 | +4.5 | 38 |
| 3 | Nikola Jokic | DEN | +5.2 | +5.4 | -0.2 | 38 |
| 4 | Kawhi Leonard | TOR | +4.9 | +4.2 | +0.7 | 31 |
| 5 | Giannis Antetokounmpo | MIA | +4.7 | +4.1 | +0.6 | 28 |
| 6 | Alex Caruso | OKC | +4.0 | -0.2 | +4.2 | 25 |
| 7 | Joel Embiid | PHI | +3.2 | +1.7 | +1.5 | 33 |
| 8 | Luka Doncic | LAL | +3.0 | +3.9 | -0.9 | 32 |
| 9 | Franz Wagner | ORL | +2.6 | +1.2 | +1.4 | 29 |
| 10 | Kyrie Irving | DAL | +2.4 | +2.6 | -0.1 | 26 |
| 11 | Chet Holmgren | OKC | +2.4 | +0.4 | +2.0 | 29 |
| 12 | Dyson Daniels | ATL | +2.4 | +1.5 | +0.9 | 28 |
| 13 | Jimmy Butler III | GSW | +2.2 | +2.1 | +0.1 | 27 |
| 14 | Lauri Markkanen | UTA | +2.2 | +1.5 | +0.7 | 31 |
| 15 | Marcus Smart | HOU | +2.1 | +0.8 | +1.4 | 31 |
| 16 | Derrick White | BOS | +2.1 | +0.3 | +1.8 | 37 |
| 17 | Pascal Siakam | IND | +2.0 | +1.8 | +0.2 | 32 |
| 18 | Jarrett Allen | CLE | +1.9 | +1.3 | +0.7 | 29 |
| 19 | Fred VanVleet | HOU | +1.8 | +1.2 | +0.6 | 36 |
| 20 | Ausar Thompson | DET | +1.8 | -0.2 | +1.9 | 30 |
| 21 | Bam Adebayo | MIA | +1.7 | +0.8 | +0.9 | 27 |
| 22 | Rudy Gobert | MIN | +1.6 | -2.8 | +4.4 | 28 |
| 23 | Jrue Holiday | POR | +1.5 | +0.1 | +1.4 | 32 |
| 24 | OG Anunoby | NYK | +1.5 | -0.2 | +1.7 | 34 |
| 25 | Cade Cunningham | DET | +1.3 | +1.4 | -0.1 | 38 |
| 26 | Donovan Mitchell | CLE | +1.3 | +1.8 | -0.6 | 36 |
| 27 | Jayson Tatum | BOS | +1.2 | +1.3 | -0.1 | 36 |
| 28 | Damian Lillard | POR | +1.1 | +1.9 | -0.8 | 24 |
| 29 | Devin Vassell | SAS | +1.1 | +0.6 | +0.5 | 36 |
| 30 | Ty Jerome | MEM | +1.1 | +2.8 | -1.7 | 27 |

## Current model fit

- Fitted on 5298 games from 2022-23 to 2026-27.
- Home court: +2.1 points per 100 possessions for the home team over the visitor (about 2.1 points a game).
- Second night of a back-to-back: -0.7 points per 100 scored, +1.2 allowed.
- Weights: team efficiency ratings 0.17 (offense) and 0.16 (defense); player lineup ratings 0.76 and 0.75.
- Blend: 82% on the betting line for the margin and 100% for the total, wherever there is a line (fitted on past closing lines).
- Simulator: each team's points vary by 10.9 with correlation 0.23; 5.1% of recent games went to overtime.
