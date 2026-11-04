# NBA score predictions

Updated Wed Nov 04, 2026 02:13 AM ET. Refreshed automatically several times a day during the season, around the injury report's deadlines; each game's prediction is locked at tip-off and graded once the final score is in.

Each team's expected points are its expected possessions times its expected points per possession, from team efficiency ratings and the ratings of the players expected to play, blended with the betting line. Each game is then simulated 10,000 times, overtime included. The predicted score is the expected points rounded; the 80% range holds 80% of simulated outcomes for each team. Basketball is the most predictable major sport, but a team's score still varies by about ±14 points around the forecast, so read the win chance and the ranges too.

Missing players come from the injury report: out players are left out, and doubtful, questionable and probable ones count with the share of their minutes their chance of playing implies, and their minutes go mostly to the bench. The effect is how many points of margin the team gains or loses against its full-strength roster: negative when it is missing good players, positive when the minutes go to better ones. Predictions are rerun when the report changes, up to tip-off.

The fair moneyline is the American odds that match the win chance exactly, with no bookmaker margin: -150 means risk $150 to win $100, +150 means risk $100 to win $150.

The edge columns check every side of the spread, the moneyline and the total for expected value: the profit per $1 bet at the posted price, using the final prediction's chances (the model blended with the line, simulated against the posted lines, pushes returning the stake, and anchored to the market's own chances so only what the blend moves off the line counts). The model's own spread and total are shown alongside, but the blend keeps only the share of that disagreement the model has earned in past seasons, so edges are rare. A side is an edge when its EV is 3% or more; the best such side is shown with its price, its EV, its chance of winning the bet and its stake, a 25% share of the Kelly stake in units of 1% of the bankroll, with at most 3 units on one game. Where a spread or total price is not posted it is assumed to be -110 (marked \*); a moneyline is never assumed. Edges are logged with each prediction, locked at tip-off and graded below. Treat them as an experiment, not betting advice; see the backtest for how they have done on past seasons.

## Wednesday, November 4

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Spread: model / line | Total: model / line | 80% range | Overtime | Missing (effect on margin) | Spread edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 7:00 PM | PHI @ DET | PHI 107, DET 110 | DET 59% | PHI +145 / DET -145<br>posted PHI +110 / DET -130 | DET -3 / DET -2.5 (fav covers 53%) | 217.7 / 217.5 (over 49%) | 93–122 / 96–124 | 5% | PHI: Dominick Barlow (out) (+0.2)<br>DET: Jalen Duren (out) (-0.1) | no edge | no edge | no edge |
| 7:00 PM | ATL @ WAS | ATL 117, WAS 115 | ATL 57% | ATL -130 / WAS +130<br>posted ATL -142 / WAS +120 | ATL -2.3 / ATL -2.5 (fav covers 51%) | 232.6 / 232.5 (over 49%) | 103–132 / 101–130 | 5% | ATL: Jalen Johnson (day-to-day) (+0.6)<br>WAS: Jamir Watkins (out); Alex Sarr (day-to-day); Justin Champagnie (out); Tristan Vukcevic (out) (+0.3) | no edge | no edge | no edge |
| 7:30 PM | MIL @ BOS | MIL 105, BOS 118 | BOS 82% | MIL +470 / BOS -470<br>posted MIL +424 / BOS -567 | BOS -12.4 / BOS -11.5 (fav covers 51%) | 223.2 / 223.5 (over 48%) | 91–120 / 104–132 | 3% | BOS: Jayson Tatum (day-to-day); Devin Carter (out); Payton Pritchard (day-to-day) (+1.0) | no edge | no edge | no edge |
| 7:30 PM | CHA @ BKN | CHA 108, BKN 106 | CHA 58% | CHA -135 / BKN +135<br>posted CHA -162 / BKN +136 | CHA -2.6 / CHA -3.5 (fav covers 49%) | 213.7 / 213.5 (over 50%) | 94–122 / 91–120 | 5% | CHA: Kon Knueppel (out); Grant Williams (out); Coby White (day-to-day) (-1.0)<br>BKN: Egor Demin (out) (+0.8) | no edge | no edge | no edge |
| 7:30 PM | CHI @ NYK | CHI 111, NYK 122 | NYK 81% | CHI +420 / NYK -420<br>posted CHI +443 / NYK -597 | NYK -11.7 / NYK -11.5 (fav covers 49%) | 233.2 / 233.5 (over 49%) | 96–126 / 108–137 | 3% | CHI: Jalen Smith (day-to-day); Nic Claxton (out) (-0.4)<br>NYK: Josh Hart (day-to-day) (-0.1) | no edge | no edge | no edge |
| 8:00 PM | IND @ MEM | IND 112, MEM 118 | MEM 68% | IND +215 / MEM -215<br>posted IND +205 / MEM -249 | MEM -6.4 / MEM -6.5 (fav covers 51%) | 229.4 / 229.5 (over 49%) | 97–126 / 104–132 | 4% | IND: Tyrese Haliburton (out); Johnny Furphy (out); Ben Sheppard (out); T.J. McConnell (out); Kelly Oubre Jr. (day-to-day); Obi Toppin (out); Ivica Zubac (out) (-0.9)<br>MEM: Scotty Pippen Jr. (out); Quinten Post (day-to-day) (+0.2) | no edge | no edge | no edge |
| 8:00 PM | UTA @ NOP | UTA 115, NOP 120 | NOP 65% | UTA +185 / NOP -185<br>posted UTA +180 / NOP -217 | NOP -5.3 / NOP -5.5 (fav covers 50%) | 234.6 / 234.5 (over 49%) | 100–130 / 105–134 | 5% | UTA: Jaren Jackson Jr. (out); Trey Alexander (out); Mo Bamba (day-to-day); Jusuf Nurkic (out) (-0.9)<br>NOP: Trey Murphy III (day-to-day); Yves Missi (out); Jordan Poole (out) (+0.3) | no edge | no edge | no edge |
| 8:00 PM | CLE @ OKC | CLE 113, OKC 116 | OKC 57% | CLE +135 / OKC -135<br>posted CLE +114 / OKC -135 | OKC -2.5 / OKC -2.5 (fav covers 52%) | 228.8 / 228.5 (over 50%) | 99–128 / 101–130 | 6% | CLE: Peyton Watson (out); Jaylon Tyson (out) (+0.2)<br>OKC: Chet Holmgren (out); Jalen Williams (out); Jaylin Williams (day-to-day); Cason Wallace (out) (-0.2) | no edge | no edge | no edge |
| 8:30 PM | MIN @ HOU | MIN 106, HOU 114 | HOU 73% | MIN +275 / HOU -275<br>posted MIN +251 / HOU -310 | HOU -8.1 / HOU -8.5 (fav covers 49%) | 220.3 / 220.5 (over 49%) | 92–120 / 100–128 | 5% | MIN: Anthony Edwards (out); Terrence Shannon Jr. (day-to-day); Donte DiVincenzo (out) (-0.8)<br>HOU: Steven Adams (out); Clint Capela (day-to-day) (-0.5) | no edge | no edge | no edge |
| 9:00 PM | TOR @ DEN | TOR 113, DEN 118 | DEN 63% | TOR +170 / DEN -170<br>posted TOR +160 / DEN -192 | DEN -4.6 / DEN -4.5 (fav covers 51%) | 230.7 / 230.5 (over 49%) | 98–128 / 103–132 | 5% | TOR: Kawhi Leonard (out); Jakob Poeltl (day-to-day) (-1.9)<br>DEN: Cameron Johnson (day-to-day); Spencer Jones (out); Alpha Diallo (day-to-day) (+1.4) | no edge | no edge | no edge |
| 9:00 PM | POR @ PHX | POR 116, PHX 112 | POR 61% | POR -155 / PHX +155<br>posted POR -155 / PHX +130 | POR -3.4 / POR -3.5 (fav covers 52%) | 227.7 / 227.5 (over 49%) | 101–130 / 98–127 | 5% | POR: Ja Morant (out) (-0.4)<br>PHX: Mark Williams (out); Jordan Goodwin (day-to-day) (+0.3) | no edge | no edge | no edge |
| 9:30 PM | DAL @ SAS | DAL 108, SAS 119 | SAS 79% | DAL +375 / SAS -375<br>posted DAL +411 / SAS -545 | SAS -11.1 / SAS -11.5 (fav covers 48%) | 227.3 / 227.5 (over 49%) | 94–123 / 105–134 | 4% | DAL: Santi Aldama (out); Max Christie (out); Dereck Lively II (out); Sergio de Larrea (out) (+1.3)<br>SAS: Tobias Harris (out) (+0.7) | no edge | no edge | no edge |
| 10:00 PM | LAL @ SAC | LAL 123, SAC 112 | LAL 78% | LAL -360 / SAC +360<br>posted LAL -574 / SAC +429 | LAL -11.1 / LAL -11.5 (fav covers 48%) | 234.3 / 234.5 (over 49%) | 108–137 / 97–127 | 4% | SAC: Maxime Raynaud (out); Precious Achiuwa (day-to-day); Keegan Murray (out) (-0.1) | no edge | no edge | no edge |
| 10:30 PM | MIA @ LAC | MIA 119, LAC 114 | MIA 63% | MIA -170 / LAC +170<br>posted MIA -205 / LAC +171 | MIA -4.5 / MIA -5.5 (fav covers 49%) | 233.4 / 233.5 (over 49%) | 104–134 / 100–129 | 5% | MIA: Giannis Antetokounmpo (day-to-day) (-0.8)<br>LAC: Brandon Ingram (out); Jordan Miller (out); Bradley Beal (out); Yanic Konan Niederhauser (out) (+0.4) | no edge | no edge | no edge |

## Thursday, November 5

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Spread: model / line | Total: model / line | 80% range | Overtime | Missing (effect on margin) | Spread edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 9:00 PM | ORL @ PHX | ORL 114, PHX 113 | ORL 51% | ORL -100 / PHX +100 | pick'em | 226.2 | 99–128 / 98–128 | 5% | ORL: Paolo Banchero (out); Jalen Suggs (out); Anthony Black (day-to-day) (+0.5)<br>PHX: Mark Williams (out); Jordan Goodwin (day-to-day) (+0.3) | no line yet | no line yet | no line yet |
| 10:00 PM | MIA @ GSW | MIA 116, GSW 121 | GSW 66% | MIA +195 / GSW -195 | GSW -5.4 | 237.3 | 101–131 / 107–136 | 5% | MIA: Giannis Antetokounmpo (day-to-day) (-0.8)<br>GSW: Moses Moody (out); Jimmy Butler III (out); Kristaps Porzingis (out); Brandon Williams (day-to-day); Al Horford (day-to-day); Gui Santos (day-to-day) (-1.2) | no line yet | no line yet | no line yet |

## How the 2026-27 predictions have done

| Predictor | Games | Margin MAE | Total MAE | Team-points MAE | Log loss | Brier | Winners | 80% range hit |
|---|---|---|---|---|---|---|---|---|
| Final prediction | 107 | 11.11 | 15.43 | 9.76 | 0.579 | 0.199 | 68.2% | 79.4% |
| Model only (before blending) | 107 | 11.62 | 15.11 | 9.89 | 0.608 | 0.212 | 65.4% | – |
| Elo | 107 | 12.02 | – | – | 0.646 | 0.229 | 59.8% | – |
| Final prediction, games with a line | 107 | 11.11 | 15.43 | 9.76 | 0.579 | 0.199 | 68.2% | 79.4% |
| Model only, games with a line | 107 | 11.62 | 15.11 | 9.89 | 0.608 | 0.212 | 65.4% | – |
| Betting line | 107 | 11.02 | 15.42 | 9.73 | 0.567 | 0.194 | 68.2% | – |

MAE is the average miss in points; team-points MAE is the average miss on each team's score. Log loss and Brier score the win chances (lower is better; a coin flip scores 0.693 and 0.250). The closing line misses margins by about 10 points and totals by about 14.

Overtime: predicted in 4.7% of games, happened in 4.7%.

### Betting edges

| Market | Edges | Record (W-L-P) | Staked | Units won | ROI | Expected ROI |
|---|---|---|---|---|---|---|
| Spread | 1 | 1-0-0 | 1.0 | +0.90 | +89.3% | +3.6% |
| Moneyline | 5 | 0-5-0 | 1.9 | -1.88 | -100.0% | +8.8% |
| Total | 0 | 0-0-0 | 0.0 | +0.00 | – | – |

Spread moved toward the model's first spread edge before tip-off: 4 of 5 games (80%).

Live predictions only, each edge at the stake and price logged with the last prediction before tip-off (edges logged before edges were priced from the final prediction are left out); a push returns the stake. Units are 1% of the bankroll; ROI is units won per unit staked, and expected ROI is what the edges' EVs promised. The line moving toward the model's edge before tip-off is the quickest sign that it knows something the market doesn't yet.

### Results, Monday, November 2

| Game | Predicted | Final | Win chance for winner | Spread: model / line | Inside 80% ranges |
|---|---|---|---|---|---|
| OKC @ CLE | 112–117 | 117–112 | 36% | CLE -4.6 / CLE -4.5 | yes |
| DET @ CHA | 108–102 | 124–91 | 67% | DET -5.6 / DET -5.5 | no |
| ATL @ IND | 118–109 | 108–104 | 74% | ATL -8.9 / ATL -9.5 | yes |
| BKN @ NYK | 102–116 | 90–103 | 86% | NYK -14.4 / NYK -14.5 | yes |
| WAS @ ORL | 111–114 | 103–94 | 41% | ORL -3 / ORL -2.5 | no |
| CHI @ PHI | 114–125 | 107–126 | 78% | PHI -10.4 / PHI -10.5 | yes |
| SAC @ DAL | 112–120 | 115–100 | 29% | DAL -7.5 / DAL -7.5 | no |
| NOP @ MEM | 113–118 | 135–134 (OT) | 34% | MEM -5.4 / MEM -5.5 | no |
| MIL @ MIN | 110–121 | 100–112 | 79% | MIN -10.9 / MIN -10.5 | yes |
| BOS @ HOU | 106–110 | 93–109 | 64% | HOU -4.4 / HOU -4.5 | yes |
| UTA @ SAS | 106–122 | 97–119 | 89% | SAS -16.6 / SAS -16.5 | yes |
| POR @ DEN | 114–118 | 118–110 | 38% | DEN -4.2 / DEN -4.5 | yes |
| PHX @ GSW | 113–115 | 113–116 | 57% | GSW -2.3 / GSW -2.5 | yes |
| TOR @ LAC | 112–108 | 125–118 | 62% | TOR -3.9 / TOR -4.5 | yes |
| MIA @ LAL | 117–119 | 117–138 | 57% | LAL -2.2 / LAL -2.5 | no |

## Power ratings

Points per 100 possessions better than an average team on a neutral floor, combining opponent-adjusted team efficiency (garbage time removed) with the ratings of the team's healthy roster, through the fitted points map. Net per game uses the team's pace. Injury effect now is what its current injury report does to its margin, in points.

| # | Team | Net per 100 | Net per game | Offense | Defense | Pace | Injury effect now | Elo |
|---|---|---|---|---|---|---|---|---|
| 1 | HOU | +7.6 | +7.5 | +4.0 | +3.6 | 98.9 | -0.5 | 1634 |
| 2 | DET | +6.3 | +6.3 | +2.0 | +4.3 | 101.0 | -0.1 | 1666 |
| 3 | SAS | +6.2 | +6.3 | +1.8 | +4.4 | 102.5 | +0.7 | 1694 |
| 4 | BOS | +5.9 | +5.7 | +3.2 | +2.7 | 97.5 | +0.9 | 1618 |
| 5 | MIN | +4.1 | +4.2 | +1.5 | +2.6 | 103.3 | -0.8 | 1600 |
| 6 | NYK | +4.0 | +3.9 | +1.1 | +2.9 | 97.1 | -0.1 | 1687 |
| 7 | LAL | +3.6 | +3.7 | +3.7 | -0.1 | 102.3 | +0.3 | 1587 |
| 8 | POR | +3.5 | +3.6 | +2.2 | +1.3 | 101.1 | -0.4 | 1550 |
| 9 | OKC | +3.4 | +3.4 | -0.3 | +3.7 | 100.1 | -0.2 | 1667 |
| 10 | PHI | +2.7 | +2.7 | +0.0 | +2.7 | 101.2 | +0.2 | 1575 |
| 11 | DEN | +1.9 | +1.9 | +3.3 | -1.3 | 98.2 | +1.3 | 1566 |
| 12 | GSW | +1.9 | +1.9 | +1.5 | +0.4 | 101.3 | -1.1 | 1505 |
| 13 | TOR | +1.9 | +2.0 | +0.5 | +1.4 | 106.2 | -2.0 | 1556 |
| 14 | CLE | +1.9 | +1.9 | +2.3 | -0.5 | 102.1 | +0.3 | 1578 |
| 15 | MIA | +0.3 | +0.3 | +1.9 | -1.6 | 106.5 | -0.8 | 1492 |
| 16 | MEM | -0.5 | -0.5 | +1.1 | -1.6 | 101.8 | +0.2 | 1421 |
| 17 | PHX | -0.9 | -0.9 | +1.2 | -2.1 | 101.7 | +0.3 | 1494 |
| 18 | ORL | -0.9 | -0.9 | -2.0 | +1.1 | 99.0 | +0.5 | 1505 |
| 19 | DAL | -1.3 | -1.3 | -1.0 | -0.4 | 101.7 | +1.2 | 1432 |
| 20 | ATL | -1.7 | -1.9 | -1.2 | -0.6 | 107.5 | +0.6 | 1538 |
| 21 | NOP | -3.1 | -3.2 | -1.1 | -2.0 | 105.8 | +0.3 | 1439 |
| 22 | IND | -3.2 | -3.3 | -1.3 | -1.9 | 102.0 | -0.9 | 1353 |
| 23 | LAC | -3.6 | -3.6 | -1.6 | -2.0 | 100.5 | +0.4 | 1480 |
| 24 | CHA | -4.2 | -4.0 | -3.8 | -0.4 | 96.0 | -1.0 | 1504 |
| 25 | WAS | -4.2 | -4.2 | -2.8 | -1.4 | 100.6 | +0.3 | 1345 |
| 26 | UTA | -4.5 | -4.7 | -3.6 | -0.9 | 102.9 | -0.9 | 1308 |
| 27 | CHI | -5.9 | -6.7 | -2.9 | -3.0 | 112.5 | -0.4 | 1359 |
| 28 | BKN | -6.3 | -6.4 | -3.7 | -2.6 | 101.1 | +0.8 | 1303 |
| 29 | SAC | -7.1 | -7.5 | -3.3 | -3.9 | 105.2 | -0.1 | 1350 |
| 30 | MIL | -7.4 | -7.8 | -2.9 | -4.5 | 105.6 | +0.0 | 1344 |

## Top players

Regularized adjusted plus-minus from every lineup this season and past ones: points per 100 possessions a player adds on offense and saves on defense, against an average player, shrunk toward last season's rating. Players expected to play 20 minutes or more.

| # | Player | Team | Net impact per 100 | Offense | Defense | Expected minutes |
|---|---|---|---|---|---|---|
| 1 | Victor Wembanyama | SAS | +6.2 | +1.6 | +4.6 | 30 |
| 2 | Shai Gilgeous-Alexander | OKC | +5.8 | +5.0 | +0.7 | 34 |
| 3 | Nikola Jokic | DEN | +4.9 | +5.2 | -0.3 | 37 |
| 4 | Kawhi Leonard | TOR | +4.5 | +3.6 | +0.9 | 30 |
| 5 | Luka Doncic | LAL | +4.4 | +5.5 | -1.1 | 36 |
| 6 | Giannis Antetokounmpo | MIA | +3.8 | +4.0 | -0.2 | 32 |
| 7 | Kyrie Irving | DAL | +3.6 | +3.4 | +0.2 | 31 |
| 8 | Joel Embiid | PHI | +3.4 | +1.7 | +1.7 | 31 |
| 9 | Herbert Jones | NOP | +3.0 | +0.0 | +3.0 | 25 |
| 10 | Fred VanVleet | HOU | +2.6 | +1.9 | +0.7 | 30 |
| 11 | Marcus Smart | HOU | +2.6 | +1.2 | +1.3 | 23 |
| 12 | Jarrett Allen | CLE | +2.3 | +1.8 | +0.6 | 28 |
| 13 | Jimmy Butler III | GSW | +2.2 | +2.1 | +0.1 | 27 |
| 14 | Ausar Thompson | DET | +2.1 | +0.0 | +2.1 | 26 |
| 15 | Chet Holmgren | OKC | +2.1 | +0.0 | +2.0 | 30 |
| 16 | Franz Wagner | ORL | +2.0 | +0.8 | +1.2 | 37 |
| 17 | Cade Cunningham | DET | +2.0 | +1.8 | +0.2 | 31 |
| 18 | Stephen Curry | GSW | +1.9 | +4.4 | -2.4 | 31 |
| 19 | Neemias Queta | BOS | +1.9 | +0.9 | +1.0 | 24 |
| 20 | Lauri Markkanen | UTA | +1.8 | +1.7 | +0.1 | 28 |
| 21 | Ty Jerome | MEM | +1.8 | +3.3 | -1.5 | 31 |
| 22 | Dean Wade | PHI | +1.8 | +0.4 | +1.4 | 25 |
| 23 | LaMelo Ball | MIN | +1.8 | +3.8 | -2.0 | 28 |
| 24 | Donovan Mitchell | CLE | +1.7 | +2.3 | -0.6 | 32 |
| 25 | Derrick White | BOS | +1.7 | +0.1 | +1.6 | 30 |
| 26 | Bam Adebayo | MIA | +1.6 | +1.4 | +0.2 | 32 |
| 27 | Jrue Holiday | POR | +1.6 | +0.7 | +0.9 | 28 |
| 28 | Rudy Gobert | MIN | +1.5 | -3.5 | +5.0 | 29 |
| 29 | Kevin Durant | HOU | +1.5 | +3.2 | -1.7 | 32 |
| 30 | Paul Reed | DET | +1.4 | +0.1 | +1.3 | 29 |

## Current model fit

- Fitted on 5389 games from 2022-23 to 2026-27.
- Home court: +2.0 points per 100 possessions for the home team over the visitor (about 2.0 points a game).
- Second night of a back-to-back: -0.7 points per 100 scored, +1.2 allowed.
- Weights: team efficiency ratings 0.16 (offense) and 0.15 (defense); player lineup ratings 0.76 and 0.76.
- Blend: 82% on the betting line for the margin and 100% for the total, wherever there is a line (fitted on past closing lines).
- Simulator: each team's points vary by 10.9 with correlation 0.23; 5.1% of recent games went to overtime.
