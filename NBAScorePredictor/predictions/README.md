# NBA score predictions

Updated Thu Nov 12, 2026 10:26 PM ET. Refreshed automatically several times a day during the season, around the injury report's deadlines; each game's prediction is locked at tip-off and graded once the final score is in.

Each team's expected points are its expected possessions times its expected points per possession, from team efficiency ratings and the ratings of the players expected to play, blended with the betting line. Each game is then simulated 10,000 times, overtime included. The predicted score is the expected points rounded; the 80% range holds 80% of simulated outcomes for each team. Basketball is the most predictable major sport, but a team's score still varies by about ±14 points around the forecast, so read the win chance and the ranges too.

Missing players come from the injury report: out players are left out, and doubtful, questionable and probable ones count with the share of their minutes their chance of playing implies, and their minutes go mostly to the bench. The effect is how many points of margin the team gains or loses against its full-strength roster: negative when it is missing good players, positive when the minutes go to better ones. Predictions are rerun when the report changes, up to tip-off.

The fair moneyline is the American odds that match the win chance exactly, with no bookmaker margin: -150 means risk $150 to win $100, +150 means risk $100 to win $150.

The edge columns check every side of the spread, the moneyline and the total for expected value: the profit per $1 bet at the posted price, using the final prediction's chances (the model blended with the line, simulated against the posted lines, pushes returning the stake, and anchored to the market's own chances so only what the blend moves off the line counts). The model's own spread and total are shown alongside, but the blend keeps only the share of that disagreement the model has earned in past seasons, so edges are rare. A side is an edge when its EV is 3% or more; the best such side is shown with its price, its EV, its chance of winning the bet and its stake, a 25% share of the Kelly stake in units of 1% of the bankroll, with at most 3 units on one game. Where a spread or total price is not posted it is assumed to be -110 (marked \*); a moneyline is never assumed. Edges are logged with each prediction, locked at tip-off and graded below. Treat them as an experiment, not betting advice; see the backtest for how they have done on past seasons.

## Friday, November 13

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Spread: model / line | Total: model / line | 80% range | Overtime | Missing (effect on margin) | Spread edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 7:00 PM | NYK @ IND | NYK 113, IND 108 | NYK 67% | NYK -205 / IND +205<br>posted NYK -241 / IND +199 | NYK -5.8 / NYK -6.5 (fav covers 49%) | 220.8 / 220.5 (over 50%) | 99–127 / 93–122 | 5% | IND: Tyrese Haliburton (out); Aaron Nesmith (day-to-day); Johnny Furphy (out); Ben Sheppard (out); T.J. McConnell (day-to-day) (-0.1) | no edge | no edge | no edge |
| 7:00 PM | MIL @ ORL | MIL 107, ORL 116 | ORL 76% | MIL +310 / ORL -310<br>posted MIL +293 / ORL -368 | ORL -9.3 / ORL -9.5 (fav covers 48%) | 222.5 / 222.5 (over 50%) | 92–121 / 102–130 | 4% | ORL: Paolo Banchero (out); Jalen Suggs (out); Tristan da Silva (day-to-day); Jamal Cain (day-to-day) (+0.8) | no edge | no edge | no edge |
| 8:00 PM | CLE @ MIA | CLE 117, MIA 119 | MIA 57% | CLE +130 / MIA -130<br>posted CLE +105 / MIA -124 | MIA -2.2 / MIA -2.5 (fav covers 51%) | 236.8 / 236.5 (over 49%) | 102–132 / 105–134 | 6% | CLE: Evan Mobley (out); Sam Merrill (out) (-1.3)<br>MIA: Giannis Antetokounmpo (day-to-day); Klay Thompson (day-to-day); Pelle Larsson (day-to-day) (-0.6) | no edge | no edge | no edge |
| 8:00 PM | ATL @ CHI | ATL 126, CHI 120 | ATL 67% | ATL -205 / CHI +205<br>posted ATL -263 / CHI +216 | ATL -6.1 / ATL -6.5 (fav covers 50%) | 246.7 / 246.5 (over 50%) | 111–141 / 105–136 | 5% | ATL: Kingston Flemings (day-to-day); Keshon Gilbert (out) (+2.5)<br>CHI: Norman Powell (day-to-day); Caleb Wilson (out) (+1.3) | no edge | no edge | no edge |
| 8:00 PM | MEM @ NOP | MEM 119, NOP 116 | MEM 59% | MEM -145 / NOP +145<br>posted MEM -158 / NOP +133 | MEM -3.2 / MEM -3.5 (fav covers 51%) | 234.6 / 234.5 (over 49%) | 104–134 / 101–130 | 5% | MEM: Zach Edey (out); Scotty Pippen Jr. (out) (+0.1)<br>NOP: Trey Murphy III (day-to-day); Yves Missi (out); Trendon Watford (out); Bennedict Mathurin (day-to-day); Bryce McGowens (day-to-day) (+0.3) | no edge | no edge | no edge |
| 8:30 PM | UTA @ HOU | UTA 100, HOU 117 | HOU 90% | UTA +910 / HOU -910<br>posted UTA +900 / HOU -1580 | HOU -17.2 / HOU -17.5 (fav covers 47%) | 216.9 / 217.5 (over 48%) | 86–114 / 103–131 | 2% | UTA: Lauri Markkanen (out); Jaren Jackson Jr. (out); Trey Alexander (out); Jusuf Nurkic (out) (-2.7)<br>HOU: Marcus Smart (suspension); Steven Adams (out); Clint Capela (out) (-1.3) | no edge | UTA ML (+900): EV +4.0%, 10%, stake 0.1u | no edge |
| 9:30 PM | GSW @ SAS | GSW 103, SAS 115 | SAS 83% | GSW +495 / SAS -495<br>posted GSW +528 / SAS -750 | SAS -12.6 / SAS -13.5 (fav covers 46%) | 218.2 / 218.5 (over 49%) | 88–117 / 102–129 | 3% | GSW: Moses Moody (out); Jimmy Butler III (out); Kristaps Porzingis (out); Stephen Curry (out); Charles Bassey (day-to-day); Brandon Williams (out) (-2.0)<br>SAS: Tobias Harris (out); De'Aaron Fox (day-to-day); Devin Vassell (day-to-day) (+0.4) | no edge | GSW ML (+528): EV +3.5%, 16%, stake 0.2u | no edge |
| 10:00 PM | POR @ SAC | POR 120, SAC 109 | POR 78% | POR -350 / SAC +350<br>posted POR -569 / SAC +426 | POR -10.4 / POR -10.5 (fav covers 49%) | 229.1 / 229.5 (over 49%) | 105–134 / 95–124 | 4% | POR: Ja Morant (out); Chris Youngblood (out) (+0.7)<br>SAC: Maxime Raynaud (out); Precious Achiuwa (day-to-day) (+0.6) | no edge | no edge | no edge |
| 10:30 PM | OKC @ LAC | OKC 114, LAC 107 | OKC 71% | OKC -240 / LAC +240<br>posted OKC -276 / LAC +226 | OKC -7 / OKC -7.5 (fav covers 49%) | 221.5 / 221.5 (over 50%) | 100–128 / 93–122 | 5% | OKC: Chet Holmgren (out); Jalen Williams (out); Ajay Mitchell (day-to-day); Jaylin Williams (out); Cason Wallace (out) (-0.2)<br>LAC: Brandon Ingram (out); Jordan Miller (out); Bradley Beal (out); Yanic Konan Niederhauser (out) (+0.4) | no edge | no edge | no edge |

## Saturday, November 14

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Spread: model / line | Total: model / line | 80% range | Overtime | Missing (effect on margin) | Spread edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 7:00 PM | DEN @ NOP | DEN 121, NOP 111 | DEN 75% | DEN -300 / NOP +300 | DEN -9.4 | 231.8 | 107–135 / 96–126 | 4% | NOP: Trey Murphy III (day-to-day); Yves Missi (out); Trendon Watford (out); Bennedict Mathurin (day-to-day); Bryce McGowens (day-to-day) (+0.3) | no line yet | no line yet | no line yet |
| 7:30 PM | DAL @ CLE | DAL 117, CLE 115 | DAL 54% | DAL -120 / CLE +120 | DAL -1.4 | 231.9 | 102–131 / 101–130 | 5% | DAL: Dereck Lively II (out); Sergio de Larrea (out) (+1.0)<br>CLE: Evan Mobley (out); Sam Merrill (out) (-1.2) | no line yet | no line yet | no line yet |
| 8:00 PM | DET @ MIA | DET 119, MIA 111 | DET 71% | DET -245 / MIA +245 | DET -7.4 | 229.9 | 104–133 / 96–126 | 4% | DET: Jalen Duren (out) (+0.1)<br>MIA: Giannis Antetokounmpo (day-to-day); Klay Thompson (day-to-day); Pelle Larsson (day-to-day) (-0.6) | no line yet | no line yet | no line yet |
| 8:00 PM | BKN @ MEM | BKN 115, MEM 118 | MEM 60% | BKN +145 / MEM -145 | MEM -3.3 | 232.4 | 100–129 / 103–132 | 5% | BKN: Mikel Brown Jr. (day-to-day); Nolan Traore (day-to-day) (+0.5)<br>MEM: Zach Edey (out); Scotty Pippen Jr. (out) (+0.1) | no line yet | no line yet | no line yet |
| 8:00 PM | CHI @ MIN | CHI 110, MIN 125 | MIN 86% | CHI +630 / MIN -630 | MIN -14.9 | 235.7 | 96–125 / 111–140 | 3% | CHI: Norman Powell (day-to-day); Caleb Wilson (out) (+1.2)<br>MIN: Anthony Edwards (out); Donte DiVincenzo (out) (-0.8) | no line yet | no line yet | no line yet |

## How the 2026-27 predictions have done

| Predictor | Games | Margin MAE | Total MAE | Team-points MAE | Log loss | Brier | Winners | 80% range hit |
|---|---|---|---|---|---|---|---|---|
| Final prediction | 170 | 11.08 | 13.99 | 9.20 | 0.551 | 0.186 | 72.4% | 82.1% |
| Model only (before blending) | 170 | 11.43 | 13.81 | 9.26 | 0.574 | 0.196 | 70.6% | – |
| Elo | 170 | 11.86 | – | – | 0.599 | 0.208 | 65.3% | – |
| Final prediction, games with a line | 170 | 11.08 | 13.99 | 9.20 | 0.551 | 0.186 | 72.4% | 82.1% |
| Model only, games with a line | 170 | 11.43 | 13.81 | 9.26 | 0.574 | 0.196 | 70.6% | – |
| Betting line | 170 | 11.04 | 13.98 | 9.18 | 0.543 | 0.183 | 72.4% | – |

MAE is the average miss in points; team-points MAE is the average miss on each team's score. Log loss and Brier score the win chances (lower is better; a coin flip scores 0.693 and 0.250). The closing line misses margins by about 10 points and totals by about 14.

Overtime: predicted in 4.7% of games, happened in 4.7%.

### Betting edges

| Market | Edges | Record (W-L-P) | Staked | Units won | ROI | Expected ROI |
|---|---|---|---|---|---|---|
| Spread | 1 | 1-0-0 | 1.0 | +0.90 | +89.3% | +3.6% |
| Moneyline | 9 | 0-9-0 | 3.5 | -3.47 | -100.0% | +8.3% |
| Total | 0 | 0-0-0 | 0.0 | +0.00 | – | – |

Spread moved toward the model's first spread edge before tip-off: 5 of 6 games (83%).

Live predictions only, each edge at the stake and price logged with the last prediction before tip-off (edges logged before edges were priced from the final prediction are left out); a push returns the stake. Units are 1% of the bankroll; ROI is units won per unit staked, and expected ROI is what the edges' EVs promised. The line moving toward the model's edge before tip-off is the quickest sign that it knows something the market doesn't yet.

### Results, Wednesday, November 11

| Game | Predicted | Final | Win chance for winner | Spread: model / line | Inside 80% ranges |
|---|---|---|---|---|---|
| WAS @ IND | 112–116 | 101–114 | 62% | IND -3.8 / IND -3.5 | yes |
| CLE @ NYK | 109–113 | 115–107 | 38% | NYK -4.3 / NYK -4.5 | yes |
| BOS @ TOR | 110–106 | 98–93 | 64% | BOS -4.5 / BOS -4.5 | yes |
| SAS @ CHI | 126–110 | 124–119 | 86% | SAS -15.5 / SAS -15.5 | yes |
| DEN @ MEM | 117–114 | 123–118 | 60% | DEN -3.3 / DEN -3.5 | yes |
| LAL @ MIL | 122–107 | 123–112 | 86% | LAL -14.8 / LAL -14.5 | yes |
| BKN @ NOP | 113–116 | 145–111 | 43% | NOP -2.5 / NOP -2.5 | no |
| ORL @ UTA | 109–105 | 123–108 | 63% | ORL -4.3 / ORL -4.5 | yes |
| GSW @ HOU | 107–113 | 108–115 | 69% | HOU -6.4 / HOU -6.5 | yes |
| OKC @ POR | 111–114 | 108–118 | 58% | POR -2.7 / POR -2.5 | yes |

## Power ratings

Points per 100 possessions better than an average team on a neutral floor, combining opponent-adjusted team efficiency (garbage time removed) with the ratings of the team's healthy roster, through the fitted points map. Net per game uses the team's pace. Injury effect now is what its current injury report does to its margin, in points.

| # | Team | Net per 100 | Net per game | Offense | Defense | Pace | Injury effect now | Elo |
|---|---|---|---|---|---|---|---|---|
| 1 | BOS | +7.9 | +7.5 | +4.0 | +3.9 | 94.8 | -0.2 | 1669 |
| 2 | SAS | +7.4 | +7.4 | +3.4 | +4.0 | 99.6 | +0.4 | 1724 |
| 3 | HOU | +7.3 | +7.1 | +3.2 | +4.1 | 98.1 | -1.3 | 1624 |
| 4 | DET | +5.9 | +6.0 | +2.2 | +3.8 | 101.6 | +0.1 | 1645 |
| 5 | MIN | +5.4 | +5.5 | +2.2 | +3.1 | 102.9 | -0.8 | 1622 |
| 6 | LAL | +4.9 | +5.0 | +4.3 | +0.6 | 102.0 | -0.8 | 1624 |
| 7 | DEN | +4.0 | +3.9 | +4.4 | -0.5 | 97.5 | +0.2 | 1580 |
| 8 | NYK | +3.8 | +3.6 | +1.4 | +2.4 | 93.4 | +0.0 | 1686 |
| 9 | OKC | +3.7 | +3.8 | -0.4 | +4.1 | 101.6 | -0.2 | 1652 |
| 10 | POR | +3.5 | +3.6 | +2.8 | +0.7 | 102.1 | +0.7 | 1577 |
| 11 | GSW | +2.8 | +2.9 | +1.5 | +1.3 | 100.6 | -2.0 | 1534 |
| 12 | PHI | +1.5 | +1.5 | -0.3 | +1.8 | 101.4 | -0.3 | 1559 |
| 13 | CLE | +1.2 | +1.2 | +2.0 | -0.8 | 101.0 | -1.2 | 1581 |
| 14 | DAL | +0.5 | +0.5 | +0.3 | +0.2 | 101.9 | +1.1 | 1450 |
| 15 | TOR | +0.0 | +0.0 | -0.6 | +0.6 | 102.1 | -2.7 | 1520 |
| 16 | PHX | -0.2 | -0.2 | +0.6 | -0.8 | 101.5 | +0.4 | 1501 |
| 17 | MIA | -0.7 | -0.7 | +0.4 | -1.0 | 104.9 | -0.6 | 1495 |
| 18 | IND | -1.5 | -1.5 | -0.3 | -1.2 | 102.2 | -0.2 | 1364 |
| 19 | MEM | -1.6 | -1.6 | +0.3 | -1.9 | 101.8 | +0.1 | 1423 |
| 20 | ORL | -1.6 | -1.7 | -2.6 | +0.9 | 100.4 | +0.8 | 1503 |
| 21 | ATL | -2.3 | -2.5 | -1.1 | -1.2 | 108.3 | +2.5 | 1539 |
| 22 | LAC | -3.7 | -3.8 | -1.6 | -2.1 | 101.4 | +0.4 | 1471 |
| 23 | UTA | -3.9 | -4.0 | -3.6 | -0.3 | 102.1 | -2.8 | 1285 |
| 24 | BKN | -5.3 | -5.4 | -2.9 | -2.4 | 101.9 | +0.5 | 1347 |
| 25 | NOP | -5.5 | -5.6 | -1.7 | -3.7 | 102.8 | +0.3 | 1372 |
| 26 | WAS | -5.5 | -5.6 | -3.4 | -2.1 | 101.0 | +0.9 | 1321 |
| 27 | CHA | -5.5 | -5.4 | -4.5 | -1.1 | 96.6 | -0.4 | 1481 |
| 28 | CHI | -6.4 | -7.0 | -2.6 | -3.9 | 109.3 | +1.3 | 1350 |
| 29 | SAC | -7.9 | -8.1 | -4.0 | -3.9 | 102.3 | +0.6 | 1328 |
| 30 | MIL | -8.1 | -8.2 | -3.3 | -4.8 | 101.2 | +0.0 | 1323 |

## Top players

Regularized adjusted plus-minus from every lineup this season and past ones: points per 100 possessions a player adds on offense and saves on defense, against an average player, shrunk toward last season's rating. Players expected to play 20 minutes or more.

| # | Player | Team | Net impact per 100 | Offense | Defense | Expected minutes |
|---|---|---|---|---|---|---|
| 1 | Victor Wembanyama | SAS | +8.2 | +2.6 | +5.5 | 29 |
| 2 | Shai Gilgeous-Alexander | OKC | +5.7 | +5.0 | +0.7 | 33 |
| 3 | Alex Caruso | OKC | +5.2 | +0.4 | +4.8 | 22 |
| 4 | Nikola Jokic | DEN | +5.1 | +4.9 | +0.2 | 37 |
| 5 | Luka Doncic | LAL | +4.6 | +5.3 | -0.7 | 35 |
| 6 | Kawhi Leonard | TOR | +4.6 | +3.7 | +0.9 | 30 |
| 7 | Kyrie Irving | DAL | +4.1 | +3.9 | +0.2 | 33 |
| 8 | Giannis Antetokounmpo | MIA | +3.9 | +3.7 | +0.2 | 33 |
| 9 | Donovan Mitchell | CLE | +3.1 | +3.3 | -0.3 | 32 |
| 10 | Joel Embiid | PHI | +2.9 | +1.4 | +1.4 | 30 |
| 11 | Fred VanVleet | HOU | +2.6 | +1.5 | +1.1 | 30 |
| 12 | Neemias Queta | BOS | +2.4 | +1.0 | +1.4 | 25 |
| 13 | Jarrett Allen | CLE | +2.2 | +2.0 | +0.2 | 24 |
| 14 | Jimmy Butler III | GSW | +2.2 | +2.1 | +0.1 | 27 |
| 15 | LaMelo Ball | MIN | +2.2 | +4.1 | -1.9 | 31 |
| 16 | Ty Jerome | MEM | +2.1 | +3.2 | -1.1 | 31 |
| 17 | Chet Holmgren | OKC | +2.1 | +0.0 | +2.1 | 30 |
| 18 | Dyson Daniels | ATL | +2.0 | +0.5 | +1.5 | 32 |
| 19 | Franz Wagner | ORL | +2.0 | +1.0 | +1.0 | 39 |
| 20 | Derrick White | BOS | +2.0 | +0.3 | +1.7 | 31 |
| 21 | Pascal Siakam | IND | +1.9 | +1.7 | +0.3 | 33 |
| 22 | Herbert Jones | NOP | +1.8 | -1.0 | +2.8 | 24 |
| 23 | Ausar Thompson | DET | +1.8 | -0.4 | +2.2 | 28 |
| 24 | Jrue Holiday | POR | +1.8 | +1.1 | +0.7 | 27 |
| 25 | Rudy Gobert | MIN | +1.8 | -3.2 | +5.0 | 29 |
| 26 | Damian Lillard | POR | +1.7 | +2.3 | -0.6 | 29 |
| 27 | De'Aaron Fox | SAS | +1.7 | +1.7 | -0.1 | 29 |
| 28 | Day'Ron Sharpe | BKN | +1.6 | +0.5 | +1.1 | 22 |
| 29 | Dean Wade | PHI | +1.5 | +0.3 | +1.2 | 22 |
| 30 | Austin Reaves | LAL | +1.4 | +2.6 | -1.2 | 33 |

## Current model fit

- Fitted on 5452 games from 2022-23 to 2026-27.
- Home court: +2.0 points per 100 possessions for the home team over the visitor (about 2.0 points a game).
- Second night of a back-to-back: -0.8 points per 100 scored, +1.2 allowed.
- Weights: team efficiency ratings 0.15 (offense) and 0.15 (defense); player lineup ratings 0.76 and 0.76.
- Blend: 82% on the betting line for the margin and 100% for the total, wherever there is a line (fitted on past closing lines).
- Simulator: each team's points vary by 10.9 with correlation 0.23; 5.1% of recent games went to overtime.
