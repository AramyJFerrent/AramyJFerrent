# NBA score predictions

Updated Sat Oct 31, 2026 10:14 PM ET. Refreshed automatically several times a day during the season, around the injury report's deadlines; each game's prediction is locked at tip-off and graded once the final score is in.

Each team's expected points are its expected possessions times its expected points per possession, from team efficiency ratings and the ratings of the players expected to play, blended with the betting line. Each game is then simulated 10,000 times, overtime included. The predicted score is the expected points rounded; the 80% range holds 80% of simulated outcomes for each team. Basketball is the most predictable major sport, but a team's score still varies by about ±14 points around the forecast, so read the win chance and the ranges too.

Missing players come from the injury report: out players are left out, and doubtful, questionable and probable ones count with the share of their minutes their chance of playing implies, and their minutes go mostly to the bench. The effect is how many points of margin the team gains or loses against its full-strength roster: negative when it is missing good players, positive when the minutes go to better ones. Predictions are rerun when the report changes, up to tip-off.

The fair moneyline is the American odds that match the win chance exactly, with no bookmaker margin: -150 means risk $150 to win $100, +150 means risk $100 to win $150.

The edge columns check every side of the spread, the moneyline and the total for expected value: the profit per $1 bet at the posted price, using the final prediction's chances (the model blended with the line, simulated against the posted lines, pushes returning the stake, and anchored to the market's own chances so only what the blend moves off the line counts). The model's own spread and total are shown alongside, but the blend keeps only the share of that disagreement the model has earned in past seasons, so edges are rare. A side is an edge when its EV is 3% or more; the best such side is shown with its price, its EV, its chance of winning the bet and its stake, a 25% share of the Kelly stake in units of 1% of the bankroll, with at most 3 units on one game. Where a spread or total price is not posted it is assumed to be -110 (marked \*); a moneyline is never assumed. Edges are logged with each prediction, locked at tip-off and graded below. Treat them as an experiment, not betting advice; see the backtest for how they have done on past seasons.

## Sunday, November 1

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Spread: model / line | Total: model / line | 80% range | Overtime | Missing (effect on margin) | Spread edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 3:30 PM | BOS @ ORL | BOS 114, ORL 108 | BOS 67% | BOS -205 / ORL +205<br>posted BOS -258 / ORL +210 | BOS -5.8 / BOS -6.5 (fav covers 49%) | 222.8 / 222.5 (over 50%) | 100–128 / 94–123 | 5% | BOS: Devin Carter (out); Mitchell Robinson (day-to-day) (+1.2)<br>ORL: Paolo Banchero (out); Jalen Suggs (out) (+0.7) | no edge | no edge | no edge |
| 5:00 PM | BKN @ IND | BKN 114, IND 118 | IND 62% | BKN +165 / IND -165<br>posted BKN +145 / IND -175 | IND -4.3 / IND -4.5 (fav covers 51%) | 231.5 / 231.5 (over 49%) | 99–128 / 104–132 | 5% | BKN: Mikel Brown Jr. (out); Egor Demin (out) (+1.7)<br>IND: Tyrese Haliburton (out); Aaron Nesmith (day-to-day); Obi Toppin (day-to-day); Johnny Furphy (out); Ben Sheppard (out); T.J. McConnell (out); Ivica Zubac (out) (-1.0) | no edge | no edge | no edge |
| 8:30 PM | LAC @ GSW | LAC 111, GSW 113 | GSW 58% | LAC +135 / GSW -135 | GSW -2.7 | 224.0 | 96–125 / 99–127 | 5% | LAC: Max Strus (out); Brandon Ingram (out); Jordan Miller (out); Bradley Beal (out); Yanic Konan Niederhauser (out) (+0.7)<br>GSW: Draymond Green (out); Moses Moody (out); Stephen Curry (out); Jimmy Butler III (out); Kristaps Porzingis (out); Gui Santos (day-to-day) (-3.5) | no line yet | no line yet | no line yet |
| 9:00 PM | TOR @ LAL | TOR 112, LAL 116 | LAL 62% | TOR +165 / LAL -165<br>posted TOR +150 / LAL -180 | LAL -4.3 / LAL -4.5 (fav covers 50%) | 227.6 / 227.5 (over 49%) | 97–126 / 101–131 | 5% | TOR: Kawhi Leonard (out) (-1.8)<br>LAL: Ziaire Williams (day-to-day) (+0.4) | no edge | no edge | no edge |

## Monday, November 2

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Spread: model / line | Total: model / line | 80% range | Overtime | Missing (effect on margin) | Spread edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 7:00 PM | OKC @ CLE | OKC 112, CLE 114 | CLE 59% | OKC +140 / CLE -140 | CLE -2.9 | 226.0 | 97–126 / 100–129 | 5% | OKC: Chet Holmgren (out); Jalen Williams (out); Alex Caruso (out); Cason Wallace (out) (-2.4)<br>CLE: Jaylon Tyson (out) (+0.2) | no line yet | no line yet | no line yet |
| 7:30 PM | DET @ CHA | DET 107, CHA 100 | DET 72% | DET -255 / CHA +255 | DET -7.3 | 206.3 | 93–120 / 86–114 | 5% | DET: Jalen Duren (out) (-0.2)<br>CHA: Kon Knueppel (out); Coby White (out); Grant Williams (out) (-0.9) | no line yet | no line yet | no line yet |
| 7:30 PM | ATL @ IND | ATL 120, IND 116 | ATL 64% | ATL -175 / IND +175 | ATL -4.9 | 235.9 | 106–135 / 101–130 | 5% | ATL: Jalen Johnson (day-to-day); Jock Landale (out) (+1.0)<br>IND: Tyrese Haliburton (out); Aaron Nesmith (day-to-day); Obi Toppin (day-to-day); Johnny Furphy (out); Ben Sheppard (out); T.J. McConnell (out); Ivica Zubac (out) (-1.0) | no line yet | no line yet | no line yet |
| 7:30 PM | BKN @ NYK | BKN 106, NYK 119 | NYK 84% | BKN +515 / NYK -515 | NYK -13.4 | 225.5 | 92–121 / 105–134 | 4% | BKN: Mikel Brown Jr. (out); Egor Demin (out) (+1.7)<br>NYK: Jose Alvarado (out) (-0.3) | no line yet | no line yet | no line yet |
| 7:30 PM | WAS @ ORL | WAS 110, ORL 116 | ORL 67% | WAS +200 / ORL -200 | ORL -5.9 | 226.2 | 96–125 / 102–130 | 5% | WAS: Jamir Watkins (out); Justin Champagnie (out); Tristan Vukcevic (out) (+0.0)<br>ORL: Paolo Banchero (out); Jalen Suggs (out) (+0.7) | no line yet | no line yet | no line yet |
| 7:30 PM | CHI @ PHI | CHI 115, PHI 123 | PHI 71% | CHI +245 / PHI -245 | PHI -7.8 | 238.4 | 100–131 / 108–138 | 5% | CHI: Nic Claxton (out) (+0.2)<br>PHI: Joel Embiid (out); LeBron James (out); Dominick Barlow (out) (-3.0) | no line yet | no line yet | no line yet |
| 8:00 PM | SAC @ DAL | SAC 111, DAL 122 | DAL 78% | SAC +350 / DAL -350 | DAL -10.5 | 232.7 | 96–126 / 107–136 | 4% | SAC: Maxime Raynaud (out); Keegan Murray (out); Dylan Cardwell (out) (+0.2)<br>DAL: Santi Aldama (out); Dereck Lively II (out); Sergio de Larrea (out) (+1.1) | no line yet | no line yet | no line yet |
| 8:00 PM | NOP @ MEM | NOP 115, MEM 119 | MEM 59% | NOP +145 / MEM -145 | MEM -3.3 | 234.1 | 100–130 / 104–133 | 5% | NOP: Dejounte Murray (out); Yves Missi (out); Jordan Poole (out) (+0.5)<br>MEM: Ty Jerome (out); Scotty Pippen Jr. (out); Quinten Post (out) (-1.8) | no line yet | no line yet | no line yet |
| 8:00 PM | MIL @ MIN | MIL 113, MIN 123 | MIN 75% | MIL +300 / MIN -300 | MIN -9.7 | 235.8 | 98–128 / 108–137 | 4% | MIN: Anthony Edwards (out); Rudy Gobert (out); Donte DiVincenzo (out) (-3.0) | no line yet | no line yet | no line yet |
| 8:30 PM | BOS @ HOU | BOS 110, HOU 113 | HOU 60% | BOS +150 / HOU -150 | HOU -3.2 | 223.0 | 96–124 / 99–127 | 5% | BOS: Devin Carter (out); Mitchell Robinson (day-to-day) (+1.2)<br>HOU: Fred VanVleet (out); Reed Sheppard (out); Steven Adams (out) (-0.3) | no line yet | no line yet | no line yet |
| 8:30 PM | UTA @ SAS | UTA 105, SAS 119 | SAS 85% | UTA +560 / SAS -560 | SAS -14.2 | 224.5 | 91–120 / 105–133 | 3% | UTA: Jaren Jackson Jr. (out); Trey Alexander (out); Jusuf Nurkic (out) (-0.7)<br>SAS: Tobias Harris (out) (+0.7) | no line yet | no line yet | no line yet |
| 9:00 PM | POR @ DEN | POR 113, DEN 117 | DEN 61% | POR +160 / DEN -160 | DEN -3.9 | 229.8 | 99–127 / 102–132 | 5% | POR: Ja Morant (out) (-0.6)<br>DEN: Spencer Jones (out); Alpha Diallo (out) (+2.2) | no line yet | no line yet | no line yet |
| 10:00 PM | PHX @ GSW | PHX 116, GSW 115 | PHX 54% | PHX -115 / GSW +115 | PHX -1.5 | 231.0 | 102–131 / 100–130 | 6% | PHX: Mark Williams (out) (+0.4)<br>GSW: Draymond Green (out); Moses Moody (out); Stephen Curry (out); Jimmy Butler III (out); Kristaps Porzingis (out); Gui Santos (day-to-day) (-3.5) | no line yet | no line yet | no line yet |
| 10:00 PM | TOR @ LAC | TOR 112, LAC 111 | TOR 52% | TOR -110 / LAC +110 | TOR -0.6 | 222.9 | 97–126 / 97–125 | 5% | TOR: Kawhi Leonard (out) (-1.8)<br>LAC: Max Strus (out); Brandon Ingram (out); Jordan Miller (out); Bradley Beal (out); Yanic Konan Niederhauser (out) (+0.7) | no line yet | no line yet | no line yet |
| 10:00 PM | MIA @ LAL | MIA 117, LAL 119 | LAL 54% | MIA +120 / LAL -120 | LAL -1.5 | 236.1 | 102–133 / 104–134 | 5% | LAL: Ziaire Williams (day-to-day) (+0.4) | no line yet | no line yet | no line yet |

## How the 2026-27 predictions have done

| Predictor | Games | Margin MAE | Total MAE | Team-points MAE | Log loss | Brier | Winners | 80% range hit |
|---|---|---|---|---|---|---|---|---|
| Final prediction | 81 | 11.24 | 15.26 | 9.80 | 0.588 | 0.203 | 66.7% | 80.2% |
| Model only (before blending) | 81 | 11.87 | 14.87 | 9.97 | 0.620 | 0.218 | 63.0% | – |
| Elo | 81 | 12.13 | – | – | 0.655 | 0.233 | 58.0% | – |
| Final prediction, games with a line | 81 | 11.24 | 15.26 | 9.80 | 0.588 | 0.203 | 66.7% | 80.2% |
| Model only, games with a line | 81 | 11.87 | 14.87 | 9.97 | 0.620 | 0.218 | 63.0% | – |
| Betting line | 81 | 11.14 | 15.23 | 9.76 | 0.573 | 0.197 | 66.7% | – |

MAE is the average miss in points; team-points MAE is the average miss on each team's score. Log loss and Brier score the win chances (lower is better; a coin flip scores 0.693 and 0.250). The closing line misses margins by about 10 points and totals by about 14.

Overtime: predicted in 4.8% of games, happened in 4.9%.

### Betting edges

| Market | Edges | Record (W-L-P) | Staked | Units won | ROI | Expected ROI |
|---|---|---|---|---|---|---|
| Spread | 1 | 1-0-0 | 1.0 | +0.90 | +89.3% | +3.6% |
| Moneyline | 5 | 0-5-0 | 1.9 | -1.88 | -100.0% | +8.8% |
| Total | 0 | 0-0-0 | 0.0 | +0.00 | – | – |

Spread moved toward the model's first spread edge before tip-off: 4 of 5 games (80%).

Live predictions only, each edge at the stake and price logged with the last prediction before tip-off (edges logged before edges were priced from the final prediction are left out); a push returns the stake. Units are 1% of the bankroll; ROI is units won per unit staked, and expected ROI is what the edges' EVs promised. The line moving toward the model's edge before tip-off is the quickest sign that it knows something the market doesn't yet.

### Results, Friday, October 30

| Game | Predicted | Final | Win chance for winner | Spread: model / line | Inside 80% ranges |
|---|---|---|---|---|---|
| CHA @ WAS | 110–109 | 79–95 | 46% | CHA -1.3 / CHA -1.5 | no |
| CHI @ BOS | 110–125 | 111–125 | 86% | BOS -15 / BOS -14.5 | yes |
| DET @ BKN | 115–108 | 110–94 | 72% | DET -7.5 / DET -7.5 | yes |
| NYK @ PHI | 114–112 | 93–98 | 42% | NYK -2.7 / NYK -3.5 | no |
| ORL @ TOR | 111–116 | 121–114 | 36% | TOR -4.8 / TOR -5.5 | yes |
| IND @ MIA | 114–122 | 125–145 | 72% | MIA -7.8 / MIA -8.5 | no |
| HOU @ DAL | 115–109 | 111–116 | 31% | HOU -6.5 / HOU -6.5 | yes |
| LAC @ MIN | 108–114 | 101–127 | 68% | MIN -6.3 / MIN -6.5 | yes |
| LAL @ GSW | 119–116 | 95–112 | 41% | LAL -3 / LAL -3.5 | no |
| DEN @ PHX | 118–114 | 127–120 | 61% | DEN -3.7 / DEN -4.5 | yes |

## Power ratings

Points per 100 possessions better than an average team on a neutral floor, combining opponent-adjusted team efficiency (garbage time removed) with the ratings of the team's healthy roster, through the fitted points map. Net per game uses the team's pace. Injury effect now is what its current injury report does to its margin, in points.

| # | Team | Net per 100 | Net per game | Offense | Defense | Pace | Injury effect now | Elo |
|---|---|---|---|---|---|---|---|---|
| 1 | HOU | +6.6 | +6.7 | +3.3 | +3.3 | 101.4 | -0.3 | 1606 |
| 2 | SAS | +6.5 | +6.6 | +1.9 | +4.6 | 102.2 | +0.7 | 1687 |
| 3 | DET | +5.8 | +5.7 | +1.5 | +4.3 | 99.5 | -0.2 | 1647 |
| 4 | BOS | +5.6 | +5.6 | +3.1 | +2.5 | 99.7 | +1.2 | 1618 |
| 5 | NYK | +4.5 | +4.4 | +1.5 | +3.0 | 98.3 | -0.3 | 1686 |
| 6 | MIN | +3.7 | +3.9 | +1.6 | +2.2 | 104.4 | -3.0 | 1603 |
| 7 | OKC | +3.2 | +3.3 | -0.7 | +3.9 | 102.0 | -2.4 | 1677 |
| 8 | POR | +2.6 | +2.7 | +2.4 | +0.2 | 102.3 | -0.6 | 1527 |
| 9 | PHI | +2.1 | +2.2 | -0.8 | +2.9 | 104.0 | -2.9 | 1562 |
| 10 | TOR | +2.1 | +2.1 | +0.4 | +1.6 | 102.8 | -1.8 | 1552 |
| 11 | LAL | +1.8 | +1.9 | +2.1 | -0.2 | 100.7 | +0.4 | 1573 |
| 12 | CLE | +1.7 | +1.7 | +2.0 | -0.3 | 101.6 | +0.2 | 1574 |
| 13 | GSW | +1.7 | +1.7 | +1.1 | +0.5 | 102.6 | -3.6 | 1492 |
| 14 | DEN | +1.5 | +1.4 | +2.8 | -1.4 | 98.5 | +2.2 | 1579 |
| 15 | MIA | +0.9 | +0.9 | +1.9 | -1.0 | 106.8 | +0.0 | 1501 |
| 16 | ORL | +0.6 | +0.7 | -1.0 | +1.7 | 102.8 | +0.7 | 1536 |
| 17 | ATL | +0.4 | +0.5 | +0.4 | +0.0 | 107.2 | +1.1 | 1556 |
| 18 | DAL | -0.4 | -0.4 | -0.3 | -0.1 | 102.5 | +1.1 | 1456 |
| 19 | PHX | -0.7 | -0.8 | +1.4 | -2.2 | 101.4 | +0.4 | 1498 |
| 20 | MEM | -1.3 | -1.3 | +0.3 | -1.5 | 102.5 | -1.7 | 1414 |
| 21 | IND | -2.5 | -2.5 | +0.1 | -2.5 | 103.1 | -1.0 | 1371 |
| 22 | CHA | -3.2 | -3.1 | -3.9 | +0.7 | 96.7 | -0.9 | 1531 |
| 23 | LAC | -3.2 | -3.3 | -1.9 | -1.4 | 101.0 | +0.7 | 1498 |
| 24 | UTA | -3.9 | -4.0 | -2.3 | -1.6 | 102.3 | -0.7 | 1319 |
| 25 | WAS | -4.5 | -4.6 | -2.5 | -2.0 | 102.5 | +0.0 | 1325 |
| 26 | NOP | -4.6 | -5.0 | -2.3 | -2.3 | 108.3 | +0.5 | 1412 |
| 27 | CHI | -6.1 | -6.9 | -3.1 | -3.0 | 113.7 | +0.2 | 1363 |
| 28 | MIL | -6.4 | -6.8 | -2.4 | -4.0 | 105.8 | +0.0 | 1357 |
| 29 | BKN | -6.9 | -7.3 | -3.6 | -3.2 | 106.3 | +1.8 | 1290 |
| 30 | SAC | -7.6 | -8.0 | -3.2 | -4.4 | 105.8 | +0.2 | 1337 |

## Top players

Regularized adjusted plus-minus from every lineup this season and past ones: points per 100 possessions a player adds on offense and saves on defense, against an average player, shrunk toward last season's rating. Players expected to play 20 minutes or more.

| # | Player | Team | Net impact per 100 | Offense | Defense | Expected minutes |
|---|---|---|---|---|---|---|
| 1 | Victor Wembanyama | SAS | +6.2 | +1.5 | +4.7 | 34 |
| 2 | Shai Gilgeous-Alexander | OKC | +5.8 | +5.0 | +0.8 | 32 |
| 3 | Nikola Jokic | DEN | +5.1 | +5.4 | -0.3 | 37 |
| 4 | Kawhi Leonard | TOR | +4.5 | +3.6 | +0.9 | 30 |
| 5 | Giannis Antetokounmpo | MIA | +3.8 | +3.9 | -0.1 | 31 |
| 6 | Luka Doncic | LAL | +3.7 | +4.9 | -1.2 | 36 |
| 7 | Kyrie Irving | DAL | +3.5 | +3.4 | +0.1 | 31 |
| 8 | Joel Embiid | PHI | +3.2 | +1.6 | +1.5 | 35 |
| 9 | Fred VanVleet | HOU | +2.6 | +1.8 | +0.8 | 32 |
| 10 | Franz Wagner | ORL | +2.6 | +1.2 | +1.3 | 35 |
| 11 | Herbert Jones | NOP | +2.3 | +0.0 | +2.4 | 22 |
| 12 | Lauri Markkanen | UTA | +2.3 | +2.1 | +0.2 | 24 |
| 13 | Jimmy Butler III | GSW | +2.2 | +2.1 | +0.1 | 27 |
| 14 | Chet Holmgren | OKC | +2.1 | +0.0 | +2.0 | 30 |
| 15 | Ausar Thompson | DET | +1.9 | -0.3 | +2.2 | 27 |
| 16 | Dyson Daniels | ATL | +1.9 | +0.9 | +1.0 | 29 |
| 17 | Ty Jerome | MEM | +1.9 | +3.3 | -1.4 | 28 |
| 18 | LaMelo Ball | MIN | +1.9 | +4.1 | -2.2 | 28 |
| 19 | Bam Adebayo | MIA | +1.8 | +1.4 | +0.4 | 32 |
| 20 | Rudy Gobert | MIN | +1.8 | -3.3 | +5.0 | 28 |
| 21 | Cade Cunningham | DET | +1.7 | +1.7 | +0.1 | 33 |
| 22 | Jarrett Allen | CLE | +1.6 | +1.2 | +0.4 | 29 |
| 23 | Kevin Durant | HOU | +1.6 | +3.2 | -1.6 | 35 |
| 24 | Stephen Curry | GSW | +1.4 | +4.2 | -2.7 | 30 |
| 25 | Derrick White | BOS | +1.4 | -0.1 | +1.6 | 29 |
| 26 | Pascal Siakam | IND | +1.4 | +1.8 | -0.4 | 31 |
| 27 | Nickeil Alexander-Walker | ATL | +1.4 | +1.6 | -0.2 | 31 |
| 28 | Dean Wade | PHI | +1.3 | -0.3 | +1.6 | 24 |
| 29 | Jrue Holiday | POR | +1.2 | +0.2 | +1.0 | 28 |
| 30 | Sam Hauser | BOS | +1.0 | +1.7 | -0.7 | 21 |

## Current model fit

- Fitted on 5363 games from 2022-23 to 2026-27.
- Home court: +2.0 points per 100 possessions for the home team over the visitor (about 2.0 points a game).
- Second night of a back-to-back: -0.7 points per 100 scored, +1.2 allowed.
- Weights: team efficiency ratings 0.15 (offense) and 0.15 (defense); player lineup ratings 0.76 and 0.76.
- Blend: 82% on the betting line for the margin and 100% for the total, wherever there is a line (fitted on past closing lines).
- Simulator: each team's points vary by 10.9 with correlation 0.23; 5.2% of recent games went to overtime.
