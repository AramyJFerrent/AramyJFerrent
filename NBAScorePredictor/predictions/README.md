# NBA score predictions

Updated Tue Oct 27, 2026 05:29 PM ET. Refreshed automatically several times a day during the season, around the injury report's deadlines; each game's prediction is locked at tip-off and graded once the final score is in.

Each team's expected points are its expected possessions times its expected points per possession, from team efficiency ratings and the ratings of the players expected to play, blended with the betting line. Each game is then simulated 10,000 times, overtime included. The predicted score is the expected points rounded; the 80% range holds 80% of simulated outcomes for each team. Basketball is the most predictable major sport, but a team's score still varies by about ±14 points around the forecast, so read the win chance and the ranges too.

Missing players come from the injury report: out players are left out, and doubtful, questionable and probable ones count with the share of their minutes their chance of playing implies, and their minutes go mostly to the bench. The effect is how many points of margin the team gains or loses against its full-strength roster: negative when it is missing good players, positive when the minutes go to better ones. Predictions are rerun when the report changes, up to tip-off.

The fair moneyline is the American odds that match the win chance exactly, with no bookmaker margin: -150 means risk $150 to win $100, +150 means risk $100 to win $150.

The edge columns check every side of the spread, the moneyline and the total for expected value: the profit per $1 bet at the posted price, using the final prediction's chances (the model blended with the line, simulated against the posted lines, pushes returning the stake, and anchored to the market's own chances so only what the blend moves off the line counts). The model's own spread and total are shown alongside, but the blend keeps only the share of that disagreement the model has earned in past seasons, so edges are rare. A side is an edge when its EV is 3% or more; the best such side is shown with its price, its EV, its chance of winning the bet and its stake, a 25% share of the Kelly stake in units of 1% of the bankroll, with at most 3 units on one game. Where a spread or total price is not posted it is assumed to be -110 (marked \*); a moneyline is never assumed. Edges are logged with each prediction, locked at tip-off and graded below. Treat them as an experiment, not betting advice; see the backtest for how they have done on past seasons.

## Tuesday, October 27

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Spread: model / line | Total: model / line | 80% range | Overtime | Missing (effect on margin) | Spread edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 7:30 PM | BKN @ BOS | BKN 105, BOS 118 | BOS 83% | BKN +500 / BOS -500<br>posted BKN +455 / BOS -625 | BOS -12.9 / BOS -12.5 (fav covers 49%) | 222.3 / 222.5 (over 49%) | 90–119 / 104–131 | 4% | BOS: Devin Carter (out); Derrick White (day-to-day) (+1.0) | no edge | no edge | no edge |
| 8:00 PM | DET @ NYK | DET 108, NYK 112 | NYK 61% | DET +160 / NYK -160<br>posted DET +142 / NYK -170 | NYK -3.7 / NYK -4.5 (fav covers 49%) | 219.7 / 219.5 (over 49%) | 94–122 / 98–126 | 5% | DET: Ausar Thompson (day-to-day); Jalen Duren (out) (-0.6)<br>NYK: Jose Alvarado (out) (-0.3) | no edge | no edge | no edge |
| 8:00 PM | SAC @ SAS | SAC 107, SAS 125 | SAS 91% | SAC +995 / SAS -995<br>posted SAC +1000 / SAS -1800 | SAS -18.5 / SAS -18.5 (fav covers 49%) | 231.9 / 232.5 (over 48%) | 92–121 / 111–139 | 2% | SAC: Maxime Raynaud (out); Keegan Murray (out); Dylan Cardwell (out) (+0.3)<br>SAS: Tobias Harris (out) (+0.7) | no edge | no edge | no edge |
| 11:00 PM | POR @ LAL | POR 116, LAL 118 | LAL 55% | POR +120 / LAL -120<br>posted POR +105 / LAL -125 | LAL -1.6 / LAL -1.5 (fav covers 52%) | 233.5 / 233.5 (over 49%) | 102–131 / 103–132 | 5% | POR: Scoot Henderson (day-to-day) (+0.5) | no edge | no edge | no edge |

## Wednesday, October 28

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Spread: model / line | Total: model / line | 80% range | Overtime | Missing (effect on margin) | Spread edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 7:00 PM | MIA @ ATL | MIA 117, ATL 121 | ATL 61% | MIA +160 / ATL -160 | ATL -4 | 238.4 | 102–132 / 107–136 | 5% | MIA: Pelle Larsson (day-to-day) (+0.1)<br>ATL: Aaron Wiggins (day-to-day) (+0.7) | no line yet | no line yet | no line yet |
| 7:00 PM | WAS @ CLE | WAS 112, CLE 122 | CLE 77% | WAS +335 / CLE -335 | CLE -10 | 233.5 | 97–127 / 107–136 | 4% | WAS: Jamir Watkins (out); Justin Champagnie (out); Tristan Vukcevic (out) (+0.3) | no line yet | no line yet | no line yet |
| 7:00 PM | CHA @ DET | CHA 103, DET 110 | DET 71% | CHA +240 / DET -240 | DET -7.2 | 213.8 | 89–118 / 97–124 | 5% | CHA: Kon Knueppel (out); Coby White (out); Grant Williams (out) (-0.7)<br>DET: Ausar Thompson (day-to-day); Jalen Duren (out) (-0.6) | no line yet | no line yet | no line yet |
| 7:00 PM | PHI @ IND | PHI 121, IND 117 | PHI 62% | PHI -160 / IND +160<br>posted PHI -162 / IND +136 | PHI -4 / PHI -4.5 (fav covers 50%) | 237.6 / 237.5 (over 49%) | 106–136 / 102–132 | 5% | PHI: Dominick Barlow (out) (+0.3)<br>IND: Andrew Nembhard (day-to-day); Tyrese Haliburton (day-to-day); Aaron Nesmith (day-to-day); Obi Toppin (day-to-day); Johnny Furphy (out); Ivica Zubac (out); Ben Sheppard (out); T.J. McConnell (out) (+0.2) | no edge | no edge | no edge |
| 7:30 PM | ORL @ TOR | ORL 113, TOR 114 | TOR 51% | ORL +105 / TOR -105 | pick'em | 226.6 | 99–128 / 99–128 | 6% | ORL: Paolo Banchero (out); Jalen Suggs (out) (+0.2)<br>TOR: Kawhi Leonard (out) (-1.9) | no line yet | no line yet | no line yet |
| 8:00 PM | NYK @ CHI | NYK 120, CHI 113 | NYK 69% | NYK -220 / CHI +220 | NYK -6.5 | 233.2 | 105–134 / 99–128 | 5% | NYK: Jose Alvarado (out) (-0.3)<br>CHI: Nic Claxton (out); Patrick Williams (day-to-day) (+0.2) | no line yet | no line yet | no line yet |
| 8:00 PM | HOU @ MIL | HOU 120, MIL 110 | HOU 76% | HOU -320 / MIL +320 | HOU -9.6 | 229.7 | 105–134 / 95–125 | 5% | HOU: Alperen Sengun (out); Marcus Smart (day-to-day); Steven Adams (out) (-0.7) | no line yet | no line yet | no line yet |
| 8:00 PM | GSW @ MIN | GSW 108, MIN 115 | MIN 69% | GSW +225 / MIN -225 | MIN -6.6 | 223.5 | 94–123 / 101–129 | 4% | GSW: Yaxel Lendeborg (day-to-day); Moses Moody (out); Jimmy Butler III (out); Kristaps Porzingis (out) (-0.9)<br>MIN: Donte DiVincenzo (out) (-0.1) | no line yet | no line yet | no line yet |
| 8:00 PM | DEN @ NOP | DEN 119, NOP 115 | DEN 61% | DEN -155 / NOP +155 | DEN -3.9 | 234.4 | 104–134 / 100–130 | 5% | DEN: Spencer Jones (out); Cameron Johnson (day-to-day); Alpha Diallo (day-to-day) (+1.1)<br>NOP: Yves Missi (out); Jordan Poole (day-to-day) (+0.3) | no line yet | no line yet | no line yet |
| 9:00 PM | SAS @ UTA | SAS 119, UTA 110 | SAS 75% | SAS -295 / UTA +295 | SAS -8.9 | 229.3 | 105–133 / 96–125 | 4% | SAS: Tobias Harris (out) (+0.7)<br>UTA: Lauri Markkanen (day-to-day); Jaren Jackson Jr. (out); Jaxson Hayes (day-to-day); Trey Alexander (out); Jusuf Nurkic (out) (-1.3) | no line yet | no line yet | no line yet |
| 9:30 PM | OKC @ DAL | OKC 114, DAL 109 | OKC 65% | OKC -190 / DAL +190 | OKC -5.2 | 223.6 | 100–129 / 95–124 | 4% | OKC: Chet Holmgren (day-to-day); Jalen Williams (out); Alex Caruso (day-to-day); Cason Wallace (out) (+0.8)<br>DAL: Naji Marshall (day-to-day); Santi Aldama (out); Dereck Lively II (out); Sergio de Larrea (day-to-day) (+0.2) | no line yet | no line yet | no line yet |
| 10:30 PM | LAL @ LAC | LAL 116, LAC 115 | LAC 50% | LAL +100 / LAC -100 | pick'em | 229.7 | 100–130 / 100–130 | 5% | LAC: Rui Hachimura (out); Max Strus (out); Brandon Ingram (out); Jordan Miller (out); Bradley Beal (out); Yanic Konan Niederhauser (out) (+0.8) | no line yet | no line yet | no line yet |

## How the 2026-27 predictions have done

| Predictor | Games | Margin MAE | Total MAE | Team-points MAE | Log loss | Brier | Winners | 80% range hit |
|---|---|---|---|---|---|---|---|---|
| Final prediction | 52 | 11.20 | 14.38 | 9.33 | 0.593 | 0.205 | 69.2% | 80.8% |
| Model only (before blending) | 52 | 11.96 | 14.12 | 9.67 | 0.631 | 0.222 | 61.5% | – |
| Elo | 52 | 11.96 | – | – | 0.656 | 0.233 | 57.7% | – |
| Final prediction, games with a line | 52 | 11.20 | 14.38 | 9.33 | 0.593 | 0.205 | 69.2% | 80.8% |
| Model only, games with a line | 52 | 11.96 | 14.12 | 9.67 | 0.631 | 0.222 | 61.5% | – |
| Betting line | 52 | 11.08 | 14.37 | 9.27 | 0.579 | 0.199 | 69.2% | – |

MAE is the average miss in points; team-points MAE is the average miss on each team's score. Log loss and Brier score the win chances (lower is better; a coin flip scores 0.693 and 0.250). The closing line misses margins by about 10 points and totals by about 14.

Overtime: predicted in 4.8% of games, happened in 3.8%.

### Betting edges

| Market | Edges | Record (W-L-P) | Staked | Units won | ROI | Expected ROI |
|---|---|---|---|---|---|---|
| Spread | 1 | 1-0-0 | 1.0 | +0.90 | +89.3% | +3.6% |
| Moneyline | 3 | 0-3-0 | 1.2 | -1.19 | -100.0% | +11.2% |
| Total | 0 | 0-0-0 | 0.0 | +0.00 | – | – |

Spread moved toward the model's first spread edge before tip-off: 4 of 5 games (80%).

Live predictions only, each edge at the stake and price logged with the last prediction before tip-off (edges logged before edges were priced from the final prediction are left out); a push returns the stake. Units are 1% of the bankroll; ROI is units won per unit staked, and expected ROI is what the edges' EVs promised. The line moving toward the model's edge before tip-off is the quickest sign that it knows something the market doesn't yet.

### Results, Monday, October 26

| Game | Predicted | Final | Win chance for winner | Spread: model / line | Inside 80% ranges |
|---|---|---|---|---|---|
| WAS @ CHA | 112–115 | 103–110 | 58% | CHA -2.7 / CHA -2.5 | yes |
| MIN @ CLE | 116–119 | 125–127 (OT) | 57% | CLE -2.5 / CLE -2.5 | yes |
| CHI @ BOS | 110–124 | 99–134 | 84% | BOS -13.9 / BOS -13.5 | yes |
| DAL @ MIA | 117–124 | 113–109 | 31% | MIA -7.2 / MIA -7.5 | yes |
| IND @ MIL | 121–117 | 102–110 | 38% | IND -4 / IND -4.5 | no |
| PHX @ OKC | 107–115 | 114–125 | 72% | OKC -7.8 / OKC -8.5 | yes |
| ATL @ HOU | 113–117 | 110–120 | 64% | HOU -4.5 / HOU -4.5 | yes |
| MEM @ UTA | 118–120 | 110–105 | 45% | UTA -1.4 / UTA -1.5 | yes |
| GSW @ DEN | 114–122 | 134–114 | 29% | DEN -7.8 / DEN -7.5 | no |

## Power ratings

Points per 100 possessions better than an average team on a neutral floor, combining opponent-adjusted team efficiency (garbage time removed) with the ratings of the team's healthy roster, through the fitted points map. Net per game uses the team's pace. Injury effect now is what its current injury report does to its margin, in points.

| # | Team | Net per 100 | Net per game | Offense | Defense | Pace | Injury effect now | Elo |
|---|---|---|---|---|---|---|---|---|
| 1 | HOU | +6.6 | +6.6 | +3.6 | +3.0 | 101.1 | -0.7 | 1605 |
| 2 | SAS | +6.5 | +6.9 | +1.7 | +4.8 | 105.6 | +0.8 | 1682 |
| 3 | BOS | +6.3 | +6.3 | +3.4 | +2.9 | 100.5 | +1.0 | 1615 |
| 4 | DET | +4.9 | +5.0 | +1.9 | +3.1 | 101.5 | -0.6 | 1647 |
| 5 | OKC | +4.7 | +4.8 | +0.1 | +4.6 | 102.9 | +0.8 | 1713 |
| 6 | MIN | +4.3 | +4.4 | +1.7 | +2.6 | 101.6 | -0.1 | 1606 |
| 7 | NYK | +3.6 | +3.7 | +0.7 | +3.0 | 101.1 | -0.3 | 1684 |
| 8 | LAL | +3.3 | +3.4 | +3.0 | +0.3 | 103.5 | +0.3 | 1587 |
| 9 | POR | +3.1 | +3.2 | +2.0 | +1.1 | 103.1 | +0.5 | 1549 |
| 10 | CLE | +2.7 | +2.8 | +2.0 | +0.6 | 106.3 | +0.0 | 1577 |
| 11 | PHI | +1.6 | +1.7 | -0.8 | +2.4 | 107.2 | +0.3 | 1549 |
| 12 | TOR | +1.4 | +1.5 | -0.6 | +2.0 | 106.9 | -2.0 | 1549 |
| 13 | ORL | +1.3 | +1.4 | -1.4 | +2.7 | 106.3 | +0.2 | 1540 |
| 14 | ATL | +0.8 | +0.9 | +0.7 | +0.2 | 108.2 | +0.7 | 1571 |
| 15 | GSW | +0.4 | +0.4 | +1.0 | -0.6 | 101.3 | -1.0 | 1461 |
| 16 | DEN | +0.2 | +0.2 | +2.4 | -2.2 | 99.8 | +1.0 | 1561 |
| 17 | MIA | -0.4 | -0.5 | +0.4 | -0.8 | 106.8 | +0.1 | 1474 |
| 18 | PHX | -0.7 | -0.8 | +1.1 | -1.9 | 101.7 | +0.3 | 1507 |
| 19 | LAC | -1.3 | -1.4 | -0.6 | -0.7 | 103.4 | +0.8 | 1524 |
| 20 | IND | -1.8 | -1.9 | -0.1 | -1.7 | 104.2 | +0.2 | 1383 |
| 21 | DAL | -1.9 | -2.0 | -1.2 | -0.7 | 104.1 | +0.3 | 1410 |
| 22 | MEM | -2.3 | -2.4 | -0.2 | -2.2 | 102.4 | +0.0 | 1380 |
| 23 | CHA | -2.4 | -2.4 | -2.5 | +0.1 | 98.8 | -0.7 | 1561 |
| 24 | UTA | -4.2 | -4.4 | -2.2 | -2.0 | 104.3 | -1.3 | 1321 |
| 25 | NOP | -5.0 | -5.4 | -1.4 | -3.6 | 106.2 | +0.3 | 1414 |
| 26 | WAS | -5.3 | -5.6 | -2.3 | -3.0 | 104.2 | +0.3 | 1302 |
| 27 | MIL | -5.4 | -5.7 | -1.6 | -3.8 | 105.7 | +0.0 | 1368 |
| 28 | BKN | -6.9 | -7.3 | -3.5 | -3.3 | 106.4 | +0.4 | 1294 |
| 29 | SAC | -6.9 | -7.2 | -3.0 | -4.0 | 104.1 | +0.3 | 1347 |
| 30 | CHI | -7.1 | -8.0 | -4.2 | -2.9 | 112.9 | +0.2 | 1368 |

## Top players

Regularized adjusted plus-minus from every lineup this season and past ones: points per 100 possessions a player adds on offense and saves on defense, against an average player, shrunk toward last season's rating. Players expected to play 20 minutes or more.

| # | Player | Team | Net impact per 100 | Offense | Defense | Expected minutes |
|---|---|---|---|---|---|---|
| 1 | Shai Gilgeous-Alexander | OKC | +6.3 | +5.3 | +1.0 | 34 |
| 2 | Victor Wembanyama | SAS | +5.7 | +1.0 | +4.8 | 33 |
| 3 | Nikola Jokic | DEN | +4.8 | +5.4 | -0.6 | 38 |
| 4 | Kawhi Leonard | TOR | +4.5 | +3.7 | +0.8 | 30 |
| 5 | Giannis Antetokounmpo | MIA | +3.5 | +3.6 | +0.0 | 32 |
| 6 | Joel Embiid | PHI | +3.3 | +1.8 | +1.5 | 34 |
| 7 | Luka Doncic | LAL | +3.2 | +4.3 | -1.1 | 35 |
| 8 | Kyrie Irving | DAL | +2.7 | +2.8 | -0.1 | 28 |
| 9 | Dyson Daniels | ATL | +2.5 | +1.3 | +1.2 | 27 |
| 10 | Franz Wagner | ORL | +2.5 | +0.9 | +1.6 | 33 |
| 11 | Fred VanVleet | HOU | +2.4 | +1.6 | +0.9 | 33 |
| 12 | Lauri Markkanen | UTA | +2.3 | +2.2 | +0.2 | 24 |
| 13 | Jimmy Butler III | GSW | +2.2 | +2.1 | +0.1 | 27 |
| 14 | Ausar Thompson | DET | +2.2 | +0.1 | +2.0 | 26 |
| 15 | Chet Holmgren | OKC | +2.0 | +0.1 | +2.0 | 30 |
| 16 | Cade Cunningham | DET | +2.0 | +1.9 | +0.2 | 34 |
| 17 | Rudy Gobert | MIN | +1.9 | -3.1 | +5.0 | 32 |
| 18 | Ty Jerome | MEM | +1.8 | +3.4 | -1.6 | 30 |
| 19 | Pascal Siakam | IND | +1.8 | +1.7 | +0.0 | 32 |
| 20 | Kevin Durant | HOU | +1.7 | +3.1 | -1.4 | 35 |
| 21 | LaMelo Ball | MIN | +1.7 | +4.0 | -2.3 | 26 |
| 22 | Neemias Queta | BOS | +1.7 | +0.8 | +0.8 | 22 |
| 23 | Derrick White | BOS | +1.6 | -0.1 | +1.7 | 29 |
| 24 | Jarrett Allen | CLE | +1.5 | +0.9 | +0.6 | 28 |
| 25 | Dean Wade | PHI | +1.4 | -0.1 | +1.5 | 25 |
| 26 | Jrue Holiday | POR | +1.3 | +0.2 | +1.0 | 30 |
| 27 | Bam Adebayo | MIA | +1.2 | +0.7 | +0.6 | 30 |
| 28 | Nickeil Alexander-Walker | ATL | +1.2 | +1.5 | -0.2 | 30 |
| 29 | Paul George | BOS | +1.2 | +0.1 | +1.1 | 30 |
| 30 | Jayson Tatum | BOS | +1.2 | +1.1 | +0.1 | 33 |

## Current model fit

- Fitted on 5334 games from 2022-23 to 2026-27.
- Home court: +2.0 points per 100 possessions for the home team over the visitor (about 2.0 points a game).
- Second night of a back-to-back: -0.7 points per 100 scored, +1.2 allowed.
- Weights: team efficiency ratings 0.16 (offense) and 0.16 (defense); player lineup ratings 0.76 and 0.76.
- Blend: 82% on the betting line for the margin and 100% for the total, wherever there is a line (fitted on past closing lines).
- Simulator: each team's points vary by 10.9 with correlation 0.23; 5.1% of recent games went to overtime.
