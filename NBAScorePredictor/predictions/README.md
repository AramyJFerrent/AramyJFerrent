# NBA score predictions

Updated Thu Nov 26, 2026 05:30 PM ET. Refreshed automatically several times a day during the season, around the injury report's deadlines; each game's prediction is locked at tip-off and graded once the final score is in.

Each team's expected points are its expected possessions times its expected points per possession, from team efficiency ratings and the ratings of the players expected to play, blended with the betting line. Each game is then simulated 10,000 times, overtime included. The predicted score is the expected points rounded; the 80% range holds 80% of simulated outcomes for each team. Basketball is the most predictable major sport, but a team's score still varies by about ±14 points around the forecast, so read the win chance and the ranges too.

Missing players come from the injury report: out players are left out, and doubtful, questionable and probable ones count with the share of their minutes their chance of playing implies, and their minutes go mostly to the bench. The effect is how many points of margin the team gains or loses against its full-strength roster: negative when it is missing good players, positive when the minutes go to better ones. Predictions are rerun when the report changes, up to tip-off.

The fair moneyline is the American odds that match the win chance exactly, with no bookmaker margin: -150 means risk $150 to win $100, +150 means risk $100 to win $150.

The edge columns check every side of the spread, the moneyline and the total for expected value: the profit per $1 bet at the posted price, using the final prediction's chances (the model blended with the line, simulated against the posted lines, pushes returning the stake, and anchored to the market's own chances so only what the blend moves off the line counts). The model's own spread and total are shown alongside, but the blend keeps only the share of that disagreement the model has earned in past seasons, so edges are rare. A side is an edge when its EV is 3% or more; the best such side is shown with its price, its EV, its chance of winning the bet and its stake, a 25% share of the Kelly stake in units of 1% of the bankroll, with at most 3 units on one game. Where a spread or total price is not posted it is assumed to be -110 (marked \*); a moneyline is never assumed. Edges are logged with each prediction, locked at tip-off and graded below. Treat them as an experiment, not betting advice; see the backtest for how they have done on past seasons.

## Friday, November 27

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Spread: model / line | Total: model / line | 80% range | Overtime | Missing (effect on margin) | Spread edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 7:00 PM | MIA @ NYK | MIA 110, NYK 114 | NYK 61% | MIA +155 / NYK -155<br>posted MIA +142 / NYK -169 | NYK -3.8 / NYK -3.5 (fav covers 52%) | 223.7 / 223.5 (over 49%) | 96–124 / 100–128 | 5% | MIA: Giannis Antetokounmpo (day-to-day); Andrew Wiggins (day-to-day) (-0.5)<br>NYK: OG Anunoby (out); Andre Drummond (day-to-day) (-1.1) | no edge | no edge | no edge |
| 7:30 PM | MIL @ DET | MIL 105, DET 114 | DET 76% | MIL +320 / DET -320<br>posted MIL +320 / DET -407 | DET -9.3 / DET -8.5 (fav covers 52%) | 219.6 / 219.5 (over 49%) | 91–120 / 101–128 | 5% | DET: Cade Cunningham (out); Duncan Robinson (out); Jalen Duren (out) (-0.8) | no edge | no edge | no edge |
| 7:30 PM | PHI @ IND | PHI 117, IND 115 | PHI 54% | PHI -120 / IND +120<br>posted PHI -148 / IND +124 | PHI -1.5 / PHI -1.5 (fav covers 52%) | 232.5 / 232.5 (over 49%) | 103–131 / 101–130 | 5% | PHI: Joel Embiid (day-to-day); Jaylen Brown (out) (+0.0)<br>IND: Tyrese Haliburton (out); Aaron Nesmith (day-to-day); Ben Sheppard (out); T.J. McConnell (day-to-day) (-0.6) | no edge | no edge | no edge |
| 7:30 PM | BKN @ TOR | BKN 107, TOR 114 | TOR 70% | BKN +235 / TOR -235<br>posted BKN +268 / TOR -333 | TOR -7 / TOR -7.5 (fav covers 50%) | 220.5 / 220.5 (over 49%) | 93–121 / 99–128 | 4% | BKN: Nolan Traore (out); Moritz Wagner (out) (+0.9)<br>TOR: RJ Barrett (out); Kawhi Leonard (out); Alijah Martin (day-to-day) (-2.4) | no edge | no edge | no edge |
| 8:00 PM | ATL @ BOS | ATL 106, BOS 116 | BOS 77% | ATL +335 / BOS -335<br>posted ATL +322 / BOS -410 | BOS -9.7 / BOS -9.5 (fav covers 50%) | 222.2 / 222.5 (over 49%) | 92–121 / 102–130 | 4% | ATL: CJ McCollum (out); Jock Landale (out) (+1.0)<br>BOS: Mitchell Robinson (out) (+0.4) | no edge | no edge | no edge |
| 8:30 PM | MEM @ MIN | MEM 109, MIN 112 | MIN 61% | MEM +155 / MIN -155<br>posted MEM +124 / MIN -148 | MIN -3.7 / MIN -3.5 (fav covers 52%) | 220.7 / 220.5 (over 49%) | 94–123 / 98–126 | 6% | MEM: Cameron Boozer (out); Zach Edey (day-to-day); Jerami Grant (out); Scotty Pippen Jr. (out) (+2.2)<br>MIN: Anthony Edwards (out); LaMelo Ball (day-to-day); Donte DiVincenzo (out); Jaylen Clark (out) (-1.0) | no edge | no edge | no edge |
| 9:00 PM | DAL @ PHX | DAL 113, PHX 115 | PHX 55% | DAL +120 / PHX -120<br>posted DAL +120 / PHX -142 | PHX -1.6 / PHX -1.5 (fav covers 52%) | 227.8 / 227.5 (over 50%) | 99–128 / 100–129 | 6% | DAL: Dereck Lively II (out); Sergio de Larrea (out) (+1.2)<br>PHX: Mark Williams (out) (+0.5) | no edge | no edge | no edge |
| 9:30 PM | LAL @ SAS | LAL 110, SAS 116 | SAS 67% | LAL +200 / SAS -200<br>posted LAL +171 / SAS -205 | SAS -5.5 / SAS -5.5 (fav covers 52%) | 225.7 / 225.5 (over 49%) | 96–125 / 101–130 | 5% | LAL: Austin Reaves (out) (-1.3)<br>SAS: Dylan Harper (out); Tobias Harris (out); De'Aaron Fox (day-to-day) (+0.1) | no edge | no edge | no edge |
| 9:30 PM | DEN @ UTA | DEN 119, UTA 110 | DEN 74% | DEN -285 / UTA +285<br>posted DEN -416 / UTA +326 | DEN -8.8 / DEN -9.5 (fav covers 46%) | 229.2 / 229.5 (over 49%) | 105–133 / 95–125 | 4% | UTA: Lauri Markkanen (out); Jaren Jackson Jr. (out); Jaxson Hayes (day-to-day); Jusuf Nurkic (out) (-2.5) | no edge | no edge | no edge |
| 9:30 PM | NOP @ LAC | NOP 114, LAC 117 | LAC 59% | NOP +145 / LAC -145<br>posted NOP +136 / LAC -162 | LAC -3.3 / LAC -3.5 (fav covers 50%) | 231.5 / 231.5 (over 49%) | 99–129 / 103–132 | 5% | NOP: Dejounte Murray (out); Trendon Watford (out); Bennedict Mathurin (out) (+0.8)<br>LAC: Jordan Miller (out); Bradley Beal (out) (+0.4) | no edge | no edge | no edge |
| 9:30 PM | GSW @ POR | GSW 106, POR 114 | POR 74% | GSW +285 / POR -285<br>posted GSW +276 / POR -344 | POR -8.4 / POR -8.5 (fav covers 49%) | 220.5 / 220.5 (over 49%) | 92–121 / 100–128 | 4% | GSW: Moses Moody (out); Jimmy Butler III (out); Kristaps Porzingis (out); Stephen Curry (out) (-3.0)<br>POR: Ja Morant (out); Chris Youngblood (out) (+1.1) | no edge | no edge | no edge |

## Saturday, November 28

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Spread: model / line | Total: model / line | 80% range | Overtime | Missing (effect on margin) | Spread edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 5:00 PM | ORL @ WAS | ORL 112, WAS 110 | ORL 58% | ORL -140 / WAS +140 | ORL -2.8 | 221.8 | 98–127 / 95–124 | 6% | ORL: Paolo Banchero (out) (+1.5)<br>WAS: Jamir Watkins (out); Justin Champagnie (out); Tristan Vukcevic (out) (+0.3) | no line yet | no line yet | no line yet |
| 6:00 PM | BKN @ CHA | BKN 107, CHA 111 | CHA 63% | BKN +165 / CHA -165 | CHA -4.1 | 217.1 | 92–121 / 96–125 | 5% | BKN: Nolan Traore (out); Moritz Wagner (out) (+0.9)<br>CHA: Grayson Allen (out); Dennis Schroder (out); Kon Knueppel (out); Ryan Kalkbrenner (day-to-day) (-0.3) | no line yet | no line yet | no line yet |
| 8:00 PM | IND @ CHI | IND 117, CHI 120 | CHI 58% | IND +135 / CHI -135 | CHI -2.6 | 237.4 | 103–132 / 105–135 | 5% | IND: Tyrese Haliburton (out); Aaron Nesmith (day-to-day); Ben Sheppard (out); T.J. McConnell (day-to-day) (-0.6)<br>CHI: Norman Powell (out); Jalen Smith (day-to-day); Caleb Wilson (out) (+0.3) | no line yet | no line yet | no line yet |
| 8:00 PM | OKC @ MIL | OKC 121, MIL 110 | OKC 79% | OKC -385 / MIL +385 | OKC -11.2 | 230.8 | 107–135 / 95–125 | 4% | OKC: Chet Holmgren (out); Jalen Williams (out); Aday Mara (out); Cason Wallace (out); Jaylin Williams (out) (+1.8) | no line yet | no line yet | no line yet |
| 8:30 PM | PHI @ HOU | PHI 109, HOU 118 | HOU 74% | PHI +280 / HOU -280 | HOU -8.5 | 226.8 | 94–124 / 103–132 | 4% | PHI: Joel Embiid (day-to-day); Jaylen Brown (out) (+0.0) | no line yet | no line yet | no line yet |

## How the 2026-27 predictions have done

| Predictor | Games | Margin MAE | Total MAE | Team-points MAE | Log loss | Brier | Winners | 80% range hit |
|---|---|---|---|---|---|---|---|---|
| Final prediction | 270 | 10.81 | 14.50 | 9.32 | 0.579 | 0.198 | 69.3% | 80.7% |
| Model only (before blending) | 270 | 11.00 | 14.47 | 9.38 | 0.590 | 0.203 | 69.3% | – |
| Elo | 270 | 11.39 | – | – | 0.617 | 0.215 | 64.1% | – |
| Final prediction, games with a line | 270 | 10.81 | 14.50 | 9.32 | 0.579 | 0.198 | 69.3% | 80.7% |
| Model only, games with a line | 270 | 11.00 | 14.47 | 9.38 | 0.590 | 0.203 | 69.3% | – |
| Betting line | 270 | 10.80 | 14.51 | 9.32 | 0.576 | 0.197 | 69.3% | – |

MAE is the average miss in points; team-points MAE is the average miss on each team's score. Log loss and Brier score the win chances (lower is better; a coin flip scores 0.693 and 0.250). The closing line misses margins by about 10 points and totals by about 14.

Overtime: predicted in 4.7% of games, happened in 5.2%.

### Betting edges

| Market | Edges | Record (W-L-P) | Staked | Units won | ROI | Expected ROI |
|---|---|---|---|---|---|---|
| Spread | 1 | 1-0-0 | 1.0 | +0.90 | +89.3% | +3.6% |
| Moneyline | 18 | 4-14-0 | 6.7 | -0.94 | -14.1% | +6.1% |
| Total | 0 | 0-0-0 | 0.0 | +0.00 | – | – |

Spread moved toward the model's first spread edge before tip-off: 5 of 6 games (83%).

Live predictions only, each edge at the stake and price logged with the last prediction before tip-off (edges logged before edges were priced from the final prediction are left out); a push returns the stake. Units are 1% of the bankroll; ROI is units won per unit staked, and expected ROI is what the edges' EVs promised. The line moving toward the model's edge before tip-off is the quickest sign that it knows something the market doesn't yet.

### Results, Wednesday, November 25

| Game | Predicted | Final | Win chance for winner | Spread: model / line | Inside 80% ranges |
|---|---|---|---|---|---|
| MIA @ PHI | 118–120 | 104–111 | 55% | PHI -1.8 / PHI -1.5 | yes |
| CHI @ CHA | 108–111 | 107–105 | 40% | CHA -3.2 / CHA -3.5 | yes |
| CLE @ NYK | 108–112 | 102–121 | 62% | NYK -4.1 / NYK -4.5 | yes |
| MIN @ OKC | 110–112 | 113–106 | 44% | OKC -2.2 / OKC -2.5 | yes |
| LAC @ MEM | 110–117 | 97–115 | 70% | MEM -7.3 / MEM -7.5 | yes |
| BKN @ MIL | 117–118 | 104–97 | 46% | MIL -1.3 / MIL -1.5 | no |
| PHX @ HOU | 107–116 | 104–116 | 75% | HOU -9 / HOU -9.5 | yes |
| SAC @ GSW | 104–112 | 110–129 | 72% | GSW -7.9 / GSW -8.5 | no |
| SAS @ POR | 115–112 | 111–116 | 42% | SAS -2.7 / SAS -3.5 | yes |

## Power ratings

Points per 100 possessions better than an average team on a neutral floor, combining opponent-adjusted team efficiency (garbage time removed) with the ratings of the team's healthy roster, through the fitted points map. Net per game uses the team's pace. Injury effect now is what its current injury report does to its margin, in points.

| # | Team | Net per 100 | Net per game | Offense | Defense | Pace | Injury effect now | Elo |
|---|---|---|---|---|---|---|---|---|
| 1 | BOS | +7.5 | +7.2 | +2.7 | +4.8 | 96.9 | +0.4 | 1639 |
| 2 | SAS | +7.3 | +7.2 | +2.8 | +4.5 | 99.7 | +0.1 | 1712 |
| 3 | HOU | +6.7 | +6.6 | +4.3 | +2.4 | 98.1 | +0.0 | 1623 |
| 4 | DET | +5.5 | +5.4 | +2.1 | +3.4 | 96.9 | -0.8 | 1641 |
| 5 | MIN | +5.4 | +5.6 | +1.3 | +4.1 | 103.4 | -1.0 | 1626 |
| 6 | NYK | +4.4 | +4.1 | +0.1 | +4.3 | 94.2 | -1.0 | 1702 |
| 7 | DEN | +3.9 | +3.9 | +4.3 | -0.4 | 100.8 | +0.0 | 1558 |
| 8 | LAL | +3.7 | +3.7 | +2.9 | +0.8 | 101.4 | -1.3 | 1607 |
| 9 | POR | +3.5 | +3.6 | +1.9 | +1.6 | 102.4 | +1.1 | 1604 |
| 10 | OKC | +2.1 | +2.1 | -0.5 | +2.6 | 101.2 | +1.7 | 1606 |
| 11 | PHI | +2.0 | +2.0 | +1.8 | +0.2 | 99.6 | +0.0 | 1570 |
| 12 | MIA | +1.0 | +1.1 | +2.3 | -1.3 | 103.6 | -0.5 | 1553 |
| 13 | TOR | +0.2 | +0.2 | +0.1 | +0.2 | 97.5 | -2.4 | 1485 |
| 14 | GSW | +0.2 | +0.2 | -0.5 | +0.7 | 98.8 | -3.0 | 1479 |
| 15 | CLE | +0.0 | +0.0 | +1.6 | -1.5 | 101.4 | -0.4 | 1546 |
| 16 | PHX | +0.0 | +0.0 | +0.4 | -0.4 | 100.8 | +0.5 | 1532 |
| 17 | MEM | -0.4 | -0.4 | +1.0 | -1.4 | 100.0 | +2.2 | 1505 |
| 18 | ORL | -0.9 | -0.9 | -2.0 | +1.1 | 97.7 | +1.4 | 1485 |
| 19 | DAL | -1.0 | -1.1 | -0.9 | -0.1 | 101.4 | +1.2 | 1488 |
| 20 | IND | -1.4 | -1.5 | -0.2 | -1.2 | 104.9 | -0.6 | 1373 |
| 21 | UTA | -2.0 | -2.0 | -2.4 | +0.4 | 100.2 | -2.5 | 1339 |
| 22 | ATL | -2.1 | -2.2 | -2.2 | +0.1 | 106.4 | +1.0 | 1561 |
| 23 | CHI | -3.8 | -4.0 | -1.5 | -2.3 | 104.9 | +0.3 | 1419 |
| 24 | LAC | -4.3 | -4.3 | -2.0 | -2.3 | 100.3 | +0.4 | 1421 |
| 25 | WAS | -4.6 | -4.7 | -2.0 | -2.6 | 101.1 | +0.3 | 1345 |
| 26 | CHA | -5.4 | -5.1 | -4.4 | -0.9 | 94.1 | -0.3 | 1444 |
| 27 | NOP | -5.4 | -5.6 | -1.8 | -3.6 | 103.2 | +0.8 | 1355 |
| 28 | BKN | -6.8 | -6.8 | -2.4 | -4.4 | 100.6 | +0.9 | 1316 |
| 29 | MIL | -7.1 | -7.3 | -2.8 | -4.3 | 102.6 | +0.0 | 1311 |
| 30 | SAC | -8.0 | -8.1 | -3.9 | -4.2 | 100.9 | +0.6 | 1307 |

## Top players

Regularized adjusted plus-minus from every lineup this season and past ones: points per 100 possessions a player adds on offense and saves on defense, against an average player, shrunk toward last season's rating. Players expected to play 20 minutes or more.

| # | Player | Team | Net impact per 100 | Offense | Defense | Expected minutes |
|---|---|---|---|---|---|---|
| 1 | Victor Wembanyama | SAS | +8.5 | +2.6 | +5.9 | 33 |
| 2 | Shai Gilgeous-Alexander | OKC | +5.5 | +5.3 | +0.2 | 37 |
| 3 | Alex Caruso | OKC | +5.5 | +0.1 | +5.4 | 20 |
| 4 | Nikola Jokic | DEN | +5.1 | +4.7 | +0.4 | 37 |
| 5 | Kawhi Leonard | TOR | +4.6 | +3.6 | +1.0 | 30 |
| 6 | Giannis Antetokounmpo | MIA | +4.4 | +4.3 | +0.2 | 33 |
| 7 | Kyrie Irving | DAL | +4.3 | +3.9 | +0.4 | 32 |
| 8 | Luka Doncic | LAL | +3.7 | +4.7 | -1.1 | 36 |
| 9 | Joel Embiid | PHI | +2.9 | +1.9 | +1.0 | 33 |
| 10 | Derrick White | BOS | +2.8 | +0.6 | +2.3 | 31 |
| 11 | Neemias Queta | BOS | +2.7 | +0.8 | +1.9 | 27 |
| 12 | Dyson Daniels | ATL | +2.6 | +0.4 | +2.2 | 36 |
| 13 | Fred VanVleet | HOU | +2.4 | +1.8 | +0.6 | 32 |
| 14 | Ty Jerome | MEM | +2.3 | +2.7 | -0.4 | 28 |
| 15 | Jimmy Butler III | GSW | +2.2 | +2.1 | +0.1 | 27 |
| 16 | Ausar Thompson | DET | +2.2 | +0.2 | +2.0 | 33 |
| 17 | Jrue Holiday | POR | +2.2 | +1.2 | +0.9 | 30 |
| 18 | Chet Holmgren | OKC | +2.1 | +0.0 | +2.1 | 30 |
| 19 | LaMelo Ball | MIN | +2.1 | +3.5 | -1.5 | 30 |
| 20 | Herbert Jones | NOP | +2.1 | -1.1 | +3.1 | 25 |
| 21 | Bam Adebayo | MIA | +2.0 | +1.4 | +0.6 | 33 |
| 22 | Paul George | BOS | +2.0 | +0.9 | +1.1 | 32 |
| 23 | Pascal Siakam | IND | +2.0 | +1.4 | +0.6 | 33 |
| 24 | Javonte Green | DET | +2.0 | +0.1 | +1.9 | 24 |
| 25 | Marcus Smart | HOU | +2.0 | +0.4 | +1.6 | 20 |
| 26 | Franz Wagner | ORL | +1.9 | +1.1 | +0.8 | 36 |
| 27 | Karl-Anthony Towns | NYK | +1.9 | +2.0 | +0.0 | 33 |
| 28 | Damian Lillard | POR | +1.9 | +2.0 | -0.1 | 32 |
| 29 | Paul Reed | DET | +1.8 | +0.5 | +1.3 | 24 |
| 30 | De'Aaron Fox | SAS | +1.7 | +1.3 | +0.4 | 28 |

## Current model fit

- Fitted on 5552 games from 2022-23 to 2026-27.
- Home court: +2.0 points per 100 possessions for the home team over the visitor (about 2.0 points a game).
- Second night of a back-to-back: -0.8 points per 100 scored, +1.2 allowed.
- Weights: team efficiency ratings 0.14 (offense) and 0.15 (defense); player lineup ratings 0.77 and 0.76.
- Blend: 82% on the betting line for the margin and 100% for the total, wherever there is a line (fitted on past closing lines).
- Simulator: each team's points vary by 11.0 with correlation 0.23; 5.2% of recent games went to overtime.
