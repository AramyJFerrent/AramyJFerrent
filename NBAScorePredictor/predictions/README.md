# NBA score predictions

Updated Thu Nov 12, 2026 05:52 PM ET. Refreshed automatically several times a day during the season, around the injury report's deadlines; each game's prediction is locked at tip-off and graded once the final score is in.

Each team's expected points are its expected possessions times its expected points per possession, from team efficiency ratings and the ratings of the players expected to play, blended with the betting line. Each game is then simulated 10,000 times, overtime included. The predicted score is the expected points rounded; the 80% range holds 80% of simulated outcomes for each team. Basketball is the most predictable major sport, but a team's score still varies by about ±14 points around the forecast, so read the win chance and the ranges too.

Missing players come from the injury report: out players are left out, and doubtful, questionable and probable ones count with the share of their minutes their chance of playing implies, and their minutes go mostly to the bench. The effect is how many points of margin the team gains or loses against its full-strength roster: negative when it is missing good players, positive when the minutes go to better ones. Predictions are rerun when the report changes, up to tip-off.

The fair moneyline is the American odds that match the win chance exactly, with no bookmaker margin: -150 means risk $150 to win $100, +150 means risk $100 to win $150.

The edge columns check every side of the spread, the moneyline and the total for expected value: the profit per $1 bet at the posted price, using the final prediction's chances (the model blended with the line, simulated against the posted lines, pushes returning the stake, and anchored to the market's own chances so only what the blend moves off the line counts). The model's own spread and total are shown alongside, but the blend keeps only the share of that disagreement the model has earned in past seasons, so edges are rare. A side is an edge when its EV is 3% or more; the best such side is shown with its price, its EV, its chance of winning the bet and its stake, a 25% share of the Kelly stake in units of 1% of the bankroll, with at most 3 units on one game. Where a spread or total price is not posted it is assumed to be -110 (marked \*); a moneyline is never assumed. Edges are logged with each prediction, locked at tip-off and graded below. Treat them as an experiment, not betting advice; see the backtest for how they have done on past seasons.

## Thursday, November 12

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Spread: model / line | Total: model / line | 80% range | Overtime | Missing (effect on margin) | Spread edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 7:00 PM | TOR @ PHI | TOR 108, PHI 116 | PHI 72% | TOR +255 / PHI -255<br>posted TOR +221 / PHI -270 | PHI -7.5 / PHI -7.5 (fav covers 50%) | 223.5 / 223.5 (over 49%) | 94–123 / 102–130 | 5% | TOR: Scottie Barnes (out); Kawhi Leonard (out) (-2.7)<br>PHI: LeBron James (out); Joel Embiid (day-to-day); Adem Bona (out); Dominick Barlow (out) (-1.1) | no edge | no edge | no edge |
| 7:00 PM | DET @ WAS | DET 117, WAS 106 | DET 79% | DET -370 / WAS +370<br>posted DET -438 / WAS +341 | DET -10.7 / DET -10.5 (fav covers 50%) | 222.5 / 222.5 (over 49%) | 102–131 / 92–121 | 4% | DET: Jalen Duren (out) (+0.1)<br>WAS: Jamir Watkins (out); Justin Champagnie (out); Tristan Vukcevic (out) (+0.0) | no edge | no edge | no edge |
| 8:00 PM | DAL @ MIN | DAL 110, MIN 115 | MIN 66% | DAL +190 / MIN -190<br>posted DAL +185 / MIN -223 | MIN -5.3 / MIN -5.5 (fav covers 51%) | 225.6 / 225.5 (over 49%) | 95–125 / 101–130 | 4% | DAL: Morez Johnson Jr. (day-to-day); Dereck Lively II (out); Sergio de Larrea (out) (+1.3)<br>MIN: Anthony Edwards (out); Donte DiVincenzo (out) (-0.8) | no edge | no edge | no edge |
| 9:00 PM | CHA @ PHX | CHA 104, PHX 111 | PHX 69% | CHA +225 / PHX -225<br>posted CHA +190 / PHX -229 | PHX -6.7 / PHX -6.5 (fav covers 51%) | 214.5 / 214.5 (over 50%) | 90–118 / 96–125 | 5% | CHA: Dennis Schroder (out); Brandon Miller (out); Kon Knueppel (out) (-0.4)<br>PHX: Mark Williams (out) (+0.4) | no edge | no edge | no edge |

## Friday, November 13

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Spread: model / line | Total: model / line | 80% range | Overtime | Missing (effect on margin) | Spread edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 7:00 PM | NYK @ IND | NYK 114, IND 108 | NYK 67% | NYK -205 / IND +205<br>posted NYK -241 / IND +199 | NYK -6 / NYK -6.5 (fav covers 50%) | 221.5 / 221.5 (over 49%) | 100–128 / 94–122 | 5% | IND: Tyrese Haliburton (out); Aaron Nesmith (day-to-day); Johnny Furphy (out); Ben Sheppard (out) (-0.1) | no edge | no edge | no edge |
| 7:00 PM | MIL @ ORL | MIL 107, ORL 117 | ORL 75% | MIL +305 / ORL -305 | ORL -9.3 | 224.2 | 93–122 / 103–131 | 4% | ORL: Paolo Banchero (out); Jalen Suggs (out); Tristan da Silva (day-to-day); Jamal Cain (day-to-day) (+0.8) | no line yet | no line yet | no line yet |
| 8:00 PM | CLE @ MIA | CLE 118, MIA 119 | MIA 55% | CLE +120 / MIA -120<br>posted CLE +105 / MIA -125 | MIA -1.3 / MIA -1.5 (fav covers 52%) | 237.6 / 237.5 (over 49%) | 104–133 / 105–134 | 5% | CLE: Evan Mobley (out); Sam Merrill (out) (-1.3)<br>MIA: Giannis Antetokounmpo (day-to-day); Klay Thompson (day-to-day); Pelle Larsson (day-to-day) (-0.6) | no edge | no edge | no edge |
| 8:00 PM | ATL @ CHI | ATL 124, CHI 121 | ATL 59% | ATL -145 / CHI +145 | ATL -3.2 | 245.7 | 110–139 / 106–136 | 5% | ATL: Keshon Gilbert (out) (+2.0)<br>CHI: Norman Powell (day-to-day); Caleb Wilson (out) (+1.3) | no line yet | no line yet | no line yet |
| 8:00 PM | MEM @ NOP | MEM 119, NOP 116 | MEM 57% | MEM -130 / NOP +130 | MEM -2.3 | 234.8 | 104–133 / 101–131 | 5% | MEM: Scotty Pippen Jr. (out) (+0.8)<br>NOP: Trey Murphy III (day-to-day); Yves Missi (out); Trendon Watford (out); Bennedict Mathurin (day-to-day); Bryce McGowens (day-to-day) (+0.3) | no line yet | no line yet | no line yet |
| 8:30 PM | UTA @ HOU | UTA 103, HOU 118 | HOU 87% | UTA +700 / HOU -700 | HOU -15.4 | 220.6 | 88–117 / 104–132 | 3% | UTA: Lauri Markkanen (out); Jaren Jackson Jr. (out); Trey Alexander (out); Jusuf Nurkic (out) (-2.7)<br>HOU: Steven Adams (out); Clint Capela (out) (-0.6) | no line yet | no line yet | no line yet |
| 9:30 PM | GSW @ SAS | GSW 107, SAS 116 | SAS 75% | GSW +310 / SAS -310 | SAS -9 | 222.6 | 92–122 / 102–130 | 5% | GSW: Moses Moody (out); Jimmy Butler III (out); Kristaps Porzingis (out); Stephen Curry (out); Charles Bassey (day-to-day); Brandon Williams (out) (-2.0)<br>SAS: Tobias Harris (out); Devin Vassell (day-to-day) (+0.6) | no line yet | no line yet | no line yet |
| 10:00 PM | POR @ SAC | POR 119, SAC 110 | POR 75% | POR -295 / SAC +295 | POR -9 | 230.0 | 105–134 / 96–126 | 4% | POR: Ja Morant (out); Chris Youngblood (day-to-day) (+0.2)<br>SAC: Maxime Raynaud (out); Precious Achiuwa (day-to-day) (+0.6) | no line yet | no line yet | no line yet |
| 10:30 PM | OKC @ LAC | OKC 115, LAC 110 | OKC 64% | OKC -180 / LAC +180 | OKC -4.7 | 225.0 | 101–129 / 95–125 | 5% | OKC: Chet Holmgren (out); Jalen Williams (out); Ajay Mitchell (day-to-day); Jaylin Williams (out); Cason Wallace (out) (-0.2)<br>LAC: Brandon Ingram (out); Jordan Miller (out); Bradley Beal (out); Yanic Konan Niederhauser (out) (+0.4) | no line yet | no line yet | no line yet |

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
| 2 | SAS | +7.4 | +7.4 | +3.4 | +4.0 | 99.6 | +0.6 | 1724 |
| 3 | HOU | +7.3 | +7.1 | +3.2 | +4.1 | 98.1 | -0.6 | 1624 |
| 4 | DET | +5.9 | +6.0 | +2.2 | +3.8 | 101.6 | +0.1 | 1645 |
| 5 | MIN | +5.4 | +5.6 | +2.3 | +3.2 | 102.9 | -0.8 | 1622 |
| 6 | LAL | +4.9 | +5.0 | +4.3 | +0.6 | 102.0 | -0.8 | 1624 |
| 7 | DEN | +4.0 | +3.9 | +4.4 | -0.5 | 97.5 | +0.2 | 1580 |
| 8 | NYK | +3.8 | +3.6 | +1.4 | +2.4 | 93.4 | +0.0 | 1686 |
| 9 | OKC | +3.7 | +3.8 | -0.4 | +4.1 | 101.6 | -0.2 | 1652 |
| 10 | POR | +3.5 | +3.6 | +2.8 | +0.7 | 102.1 | +0.2 | 1577 |
| 11 | GSW | +2.8 | +2.8 | +1.5 | +1.3 | 100.6 | -2.0 | 1534 |
| 12 | PHI | +1.5 | +1.5 | -0.3 | +1.8 | 101.4 | -1.1 | 1559 |
| 13 | CLE | +1.2 | +1.2 | +2.0 | -0.8 | 101.0 | -1.2 | 1581 |
| 14 | DAL | +0.5 | +0.5 | +0.3 | +0.2 | 101.9 | +1.3 | 1450 |
| 15 | TOR | +0.0 | +0.0 | -0.6 | +0.6 | 102.1 | -2.7 | 1520 |
| 16 | PHX | -0.2 | -0.2 | +0.6 | -0.8 | 101.5 | +0.4 | 1501 |
| 17 | MIA | -0.7 | -0.7 | +0.4 | -1.0 | 104.9 | -0.6 | 1495 |
| 18 | IND | -1.5 | -1.5 | -0.3 | -1.2 | 102.2 | -0.1 | 1364 |
| 19 | MEM | -1.6 | -1.6 | +0.3 | -1.9 | 101.8 | +0.8 | 1423 |
| 20 | ORL | -1.6 | -1.7 | -2.6 | +0.9 | 100.4 | +0.8 | 1503 |
| 21 | ATL | -2.3 | -2.5 | -1.1 | -1.2 | 108.3 | +2.0 | 1539 |
| 22 | LAC | -3.7 | -3.8 | -1.6 | -2.1 | 101.4 | +0.4 | 1471 |
| 23 | UTA | -3.9 | -4.0 | -3.6 | -0.3 | 102.1 | -2.8 | 1285 |
| 24 | BKN | -5.3 | -5.4 | -2.9 | -2.4 | 101.9 | +0.5 | 1347 |
| 25 | NOP | -5.5 | -5.6 | -1.7 | -3.7 | 102.8 | +0.3 | 1372 |
| 26 | WAS | -5.5 | -5.6 | -3.4 | -2.1 | 101.0 | +0.0 | 1321 |
| 27 | CHA | -5.6 | -5.4 | -4.5 | -1.1 | 96.6 | -0.4 | 1481 |
| 28 | CHI | -6.5 | -7.0 | -2.6 | -3.9 | 109.3 | +1.3 | 1350 |
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
