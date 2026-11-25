# NBA score predictions

Updated Wed Nov 25, 2026 05:39 PM ET. Refreshed automatically several times a day during the season, around the injury report's deadlines; each game's prediction is locked at tip-off and graded once the final score is in.

Each team's expected points are its expected possessions times its expected points per possession, from team efficiency ratings and the ratings of the players expected to play, blended with the betting line. Each game is then simulated 10,000 times, overtime included. The predicted score is the expected points rounded; the 80% range holds 80% of simulated outcomes for each team. Basketball is the most predictable major sport, but a team's score still varies by about ±14 points around the forecast, so read the win chance and the ranges too.

Missing players come from the injury report: out players are left out, and doubtful, questionable and probable ones count with the share of their minutes their chance of playing implies, and their minutes go mostly to the bench. The effect is how many points of margin the team gains or loses against its full-strength roster: negative when it is missing good players, positive when the minutes go to better ones. Predictions are rerun when the report changes, up to tip-off.

The fair moneyline is the American odds that match the win chance exactly, with no bookmaker margin: -150 means risk $150 to win $100, +150 means risk $100 to win $150.

The edge columns check every side of the spread, the moneyline and the total for expected value: the profit per $1 bet at the posted price, using the final prediction's chances (the model blended with the line, simulated against the posted lines, pushes returning the stake, and anchored to the market's own chances so only what the blend moves off the line counts). The model's own spread and total are shown alongside, but the blend keeps only the share of that disagreement the model has earned in past seasons, so edges are rare. A side is an edge when its EV is 3% or more; the best such side is shown with its price, its EV, its chance of winning the bet and its stake, a 25% share of the Kelly stake in units of 1% of the bankroll, with at most 3 units on one game. Where a spread or total price is not posted it is assumed to be -110 (marked \*); a moneyline is never assumed. Edges are logged with each prediction, locked at tip-off and graded below. Treat them as an experiment, not betting advice; see the backtest for how they have done on past seasons.

## Wednesday, November 25

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Spread: model / line | Total: model / line | 80% range | Overtime | Missing (effect on margin) | Spread edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 7:00 PM | CHI @ CHA | CHI 108, CHA 111 | CHA 60% | CHI +150 / CHA -150<br>posted CHI +151 / CHA -180 | CHA -3.2 / CHA -3.5 (fav covers 51%) | 218.7 / 218.5 (over 50%) | 94–122 / 97–125 | 5% | CHI: Norman Powell (out); Jalen Smith (out); Caleb Wilson (out) (-1.0)<br>CHA: Grayson Allen (out); Dennis Schroder (out); Kon Knueppel (out); Ryan Kalkbrenner (out) (-0.2) | no edge | no edge | no edge |
| 7:30 PM | CLE @ NYK | CLE 108, NYK 112 | NYK 62% | CLE +165 / NYK -165<br>posted CLE +151 / NYK -180 | NYK -4.1 / NYK -4.5 (fav covers 50%) | 219.6 / 219.5 (over 49%) | 93–122 / 98–126 | 5% | CLE: Evan Mobley (out) (-0.3)<br>NYK: OG Anunoby (out); Jalen Brunson (day-to-day); Josh Hart (day-to-day); Karl-Anthony Towns (day-to-day) (-2.7) | no edge | no edge | no edge |
| 7:30 PM | MIN @ OKC | MIN 110, OKC 112 | OKC 56% | MIN +130 / OKC -130<br>posted MIN +114 / OKC -135 | OKC -2.2 / OKC -2.5 (fav covers 50%) | 222.7 / 222.5 (over 50%) | 96–125 / 98–127 | 6% | MIN: Anthony Edwards (out); Donte DiVincenzo (out); Jaylen Clark (out) (-0.5)<br>OKC: Chet Holmgren (out); Jalen Williams (out); Aday Mara (out); Cason Wallace (out); Jaylin Williams (out) (+1.5) | no edge | no edge | no edge |
| 8:00 PM | LAC @ MEM | LAC 110, MEM 117 | MEM 70% | LAC +230 / MEM -230<br>posted LAC +220 / MEM -269 | MEM -7.3 / MEM -7.5 (fav covers 50%) | 227.3 / 227.5 (over 49%) | 96–125 / 103–132 | 4% | LAC: Jordan Miller (out); Bradley Beal (out) (+0.5)<br>MEM: Cameron Boozer (out); Jerami Grant (out); Scotty Pippen Jr. (out) (+2.3) | no edge | no edge | no edge |
| 8:00 PM | BKN @ MIL | BKN 117, MIL 118 | MIL 54% | BKN +120 / MIL -120<br>posted BKN -101 / MIL -117 | MIL -1.3 / MIL -1.5 (fav covers 52%) | 234.7 / 234.5 (over 49%) | 102–131 / 103–132 | 5% | BKN: Nolan Traore (out) (+0.8) | no edge | no edge | no edge |
| 8:30 PM | PHX @ HOU | PHX 107, HOU 116 | HOU 76% | PHX +315 / HOU -315<br>posted PHX +312 / HOU -395 | HOU -9.1 / HOU -9.5 (fav covers 49%) | 222.3 / 222.5 (over 48%) | 92–121 / 102–130 | 5% | PHX: Mark Williams (out) (+0.5) | no edge | no edge | no edge |
| 10:00 PM | SAC @ GSW | SAC 104, GSW 111 | GSW 71% | SAC +240 / GSW -240<br>posted SAC +257 / GSW -319 | GSW -7.1 / GSW -7.5 (fav covers 50%) | 214.5 / 214.5 (over 49%) | 89–118 / 97–125 | 5% | SAC: Maxime Raynaud (out); Zach LaVine (day-to-day) (+0.7)<br>GSW: Yaxel Lendeborg (day-to-day); Moses Moody (out); Jimmy Butler III (out); Kristaps Porzingis (out); Stephen Curry (out); Brandon Williams (out) (-2.6) | no edge | no edge | no edge |
| 10:00 PM | SAS @ POR | SAS 114, POR 111 | SAS 59% | SAS -145 / POR +145<br>posted SAS -162 / POR +136 | SAS -3 / SAS -3.5 (fav covers 50%) | 225.7 / 225.5 (over 49%) | 100–129 / 97–126 | 5% | SAS: Dylan Harper (out); Victor Wembanyama (day-to-day); Tobias Harris (out); De'Aaron Fox (day-to-day) (-1.3)<br>POR: Ja Morant (out); Chris Youngblood (out) (+0.8) | no edge | no edge | no edge |

## Friday, November 27

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Spread: model / line | Total: model / line | 80% range | Overtime | Missing (effect on margin) | Spread edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 7:00 PM | MIA @ NYK | MIA 110, NYK 112 | NYK 56% | MIA +125 / NYK -125 | NYK -2 | 222.7 | 96–125 / 98–127 | 5% | NYK: OG Anunoby (out); Jalen Brunson (day-to-day); Josh Hart (day-to-day); Karl-Anthony Towns (day-to-day) (-2.8) | no line yet | no line yet | no line yet |
| 7:30 PM | MIL @ DET | MIL 104, DET 119 | DET 86% | MIL +625 / DET -625 | DET -14.7 | 223.0 | 90–119 / 105–133 | 3% | DET: Cade Cunningham (day-to-day); Duncan Robinson (out); Jalen Duren (out) (-0.2) | no line yet | no line yet | no line yet |
| 7:30 PM | PHI @ IND | PHI 116, IND 117 | IND 51% | PHI +105 / IND -105 | IND -0.5 | 232.7 | 101–131 / 102–131 | 6% | PHI: Joel Embiid (out) (-2.0)<br>IND: Tyrese Haliburton (out); Aaron Nesmith (day-to-day); Ben Sheppard (out); T.J. McConnell (day-to-day) (-0.6) | no line yet | no line yet | no line yet |
| 7:30 PM | BKN @ TOR | BKN 109, TOR 115 | TOR 67% | BKN +205 / TOR -205 | TOR -5.9 | 223.4 | 94–123 / 100–129 | 5% | BKN: Nolan Traore (out) (+0.8)<br>TOR: RJ Barrett (out); Kawhi Leonard (out) (-2.5) | no line yet | no line yet | no line yet |
| 8:00 PM | ATL @ BOS | ATL 106, BOS 118 | BOS 79% | ATL +375 / BOS -375 | BOS -11.1 | 223.9 | 92–121 / 103–132 | 4% | ATL: CJ McCollum (out); Jock Landale (out) (+1.0)<br>BOS: Mitchell Robinson (out) (+0.4) | no line yet | no line yet | no line yet |
| 8:30 PM | MEM @ MIN | MEM 112, MIN 117 | MIN 63% | MEM +170 / MIN -170 | MIN -4.5 | 229.0 | 98–127 / 102–131 | 5% | MEM: Cameron Boozer (out); Jerami Grant (out); Scotty Pippen Jr. (out) (+2.4)<br>MIN: Anthony Edwards (out); Donte DiVincenzo (out); Jaylen Clark (out) (-0.5) | no line yet | no line yet | no line yet |
| 9:00 PM | DAL @ PHX | DAL 113, PHX 116 | PHX 59% | DAL +140 / PHX -140 | PHX -2.9 | 228.9 | 99–128 / 101–130 | 5% | DAL: Dereck Lively II (out); Sergio de Larrea (out) (+1.2)<br>PHX: Mark Williams (out) (+0.5) | no line yet | no line yet | no line yet |
| 9:30 PM | LAL @ SAS | LAL 110, SAS 116 | SAS 66% | LAL +190 / SAS -190 | SAS -5.4 | 226.0 | 96–125 / 101–130 | 5% | LAL: Austin Reaves (out) (-1.3)<br>SAS: Dylan Harper (out); Victor Wembanyama (day-to-day); Tobias Harris (out); De'Aaron Fox (day-to-day) (-1.3) | no line yet | no line yet | no line yet |
| 9:30 PM | DEN @ UTA | DEN 118, UTA 112 | DEN 68% | DEN -215 / UTA +215 | DEN -6.4 | 229.9 | 104–132 / 97–127 | 5% | UTA: Lauri Markkanen (out); Jaren Jackson Jr. (out); Jaxson Hayes (day-to-day); Jusuf Nurkic (out) (-2.5) | no line yet | no line yet | no line yet |
| 9:30 PM | NOP @ LAC | NOP 115, LAC 118 | LAC 61% | NOP +155 / LAC -155 | LAC -3.7 | 233.0 | 100–130 / 104–133 | 5% | NOP: Dejounte Murray (out); Trendon Watford (out); Bennedict Mathurin (out) (+0.8)<br>LAC: Jordan Miller (out); Bradley Beal (out) (+0.5) | no line yet | no line yet | no line yet |
| 9:30 PM | GSW @ POR | GSW 106, POR 115 | POR 75% | GSW +290 / POR -290 | POR -9 | 221.3 | 92–121 / 101–129 | 4% | GSW: Yaxel Lendeborg (day-to-day); Moses Moody (out); Jimmy Butler III (out); Kristaps Porzingis (out); Stephen Curry (out); Brandon Williams (out) (-2.6)<br>POR: Ja Morant (out); Chris Youngblood (out) (+0.7) | no line yet | no line yet | no line yet |

## How the 2026-27 predictions have done

| Predictor | Games | Margin MAE | Total MAE | Team-points MAE | Log loss | Brier | Winners | 80% range hit |
|---|---|---|---|---|---|---|---|---|
| Final prediction | 261 | 10.90 | 14.57 | 9.38 | 0.578 | 0.198 | 69.7% | 80.5% |
| Model only (before blending) | 261 | 11.10 | 14.51 | 9.44 | 0.591 | 0.203 | 69.3% | – |
| Elo | 261 | 11.48 | – | – | 0.617 | 0.215 | 64.4% | – |
| Final prediction, games with a line | 261 | 10.90 | 14.57 | 9.38 | 0.578 | 0.198 | 69.7% | 80.5% |
| Model only, games with a line | 261 | 11.10 | 14.51 | 9.44 | 0.591 | 0.203 | 69.3% | – |
| Betting line | 261 | 10.89 | 14.58 | 9.38 | 0.575 | 0.197 | 69.7% | – |

MAE is the average miss in points; team-points MAE is the average miss on each team's score. Log loss and Brier score the win chances (lower is better; a coin flip scores 0.693 and 0.250). The closing line misses margins by about 10 points and totals by about 14.

Overtime: predicted in 4.6% of games, happened in 5.4%.

### Betting edges

| Market | Edges | Record (W-L-P) | Staked | Units won | ROI | Expected ROI |
|---|---|---|---|---|---|---|
| Spread | 1 | 1-0-0 | 1.0 | +0.90 | +89.3% | +3.6% |
| Moneyline | 18 | 4-14-0 | 6.7 | -0.94 | -14.1% | +6.1% |
| Total | 0 | 0-0-0 | 0.0 | +0.00 | – | – |

Spread moved toward the model's first spread edge before tip-off: 5 of 6 games (83%).

Live predictions only, each edge at the stake and price logged with the last prediction before tip-off (edges logged before edges were priced from the final prediction are left out); a push returns the stake. Units are 1% of the bankroll; ROI is units won per unit staked, and expected ROI is what the edges' EVs promised. The line moving toward the model's edge before tip-off is the quickest sign that it knows something the market doesn't yet.

### Results, Tuesday, November 24

| Game | Predicted | Final | Win chance for winner | Spread: model / line | Inside 80% ranges |
|---|---|---|---|---|---|
| DET @ ORL | 108–105 | 104–86 | 57% | DET -2.4 / DET -2.5 | no |
| BOS @ WAS | 114–104 | 131–116 | 78% | BOS -10.2 / BOS -10.5 | no |
| DAL @ DEN | 113–121 | 120–101 | 27% | DEN -8.5 / DEN -8.5 | no |

## Power ratings

Points per 100 possessions better than an average team on a neutral floor, combining opponent-adjusted team efficiency (garbage time removed) with the ratings of the team's healthy roster, through the fitted points map. Net per game uses the team's pace. Injury effect now is what its current injury report does to its margin, in points.

| # | Team | Net per 100 | Net per game | Offense | Defense | Pace | Injury effect now | Elo |
|---|---|---|---|---|---|---|---|---|
| 1 | BOS | +7.6 | +7.3 | +2.7 | +4.8 | 96.8 | +0.4 | 1639 |
| 2 | SAS | +7.1 | +7.0 | +2.7 | +4.3 | 99.4 | -1.3 | 1721 |
| 3 | HOU | +6.3 | +6.2 | +4.0 | +2.3 | 98.1 | +0.0 | 1616 |
| 4 | DET | +5.6 | +5.4 | +2.2 | +3.5 | 96.8 | -0.2 | 1641 |
| 5 | MIN | +5.1 | +5.3 | +1.2 | +3.9 | 103.6 | -0.5 | 1615 |
| 6 | DEN | +3.9 | +4.0 | +4.3 | -0.4 | 100.7 | +0.0 | 1558 |
| 7 | LAL | +3.8 | +3.9 | +3.0 | +0.9 | 101.4 | -1.3 | 1607 |
| 8 | NYK | +3.7 | +3.5 | -0.3 | +3.9 | 94.0 | -2.6 | 1696 |
| 9 | POR | +3.3 | +3.4 | +1.8 | +1.5 | 102.0 | +0.8 | 1595 |
| 10 | OKC | +1.8 | +1.9 | -0.6 | +2.5 | 101.5 | +1.5 | 1617 |
| 11 | PHI | +1.6 | +1.6 | +1.6 | -0.1 | 100.4 | -2.0 | 1564 |
| 12 | MIA | +0.8 | +0.8 | +2.2 | -1.4 | 104.8 | +0.0 | 1559 |
| 13 | PHX | +0.7 | +0.7 | +0.8 | -0.1 | 100.8 | +0.5 | 1538 |
| 14 | CLE | +0.3 | +0.3 | +1.7 | -1.4 | 100.9 | -0.3 | 1552 |
| 15 | TOR | +0.3 | +0.3 | +0.1 | +0.2 | 97.4 | -2.5 | 1485 |
| 16 | MEM | -0.4 | -0.4 | +1.3 | -1.7 | 100.5 | +2.3 | 1496 |
| 17 | GSW | -0.4 | -0.4 | -1.0 | +0.6 | 98.3 | -2.6 | 1474 |
| 18 | ORL | -0.8 | -0.8 | -2.0 | +1.1 | 97.7 | +1.5 | 1485 |
| 19 | DAL | -0.9 | -0.9 | -0.9 | -0.1 | 101.5 | +1.2 | 1488 |
| 20 | IND | -1.4 | -1.4 | -0.2 | -1.2 | 104.9 | -0.6 | 1373 |
| 21 | UTA | -1.9 | -1.9 | -2.4 | +0.5 | 100.2 | -2.5 | 1339 |
| 22 | ATL | -2.0 | -2.1 | -2.2 | +0.2 | 106.2 | +1.0 | 1561 |
| 23 | LAC | -3.5 | -3.5 | -1.4 | -2.1 | 100.8 | +0.5 | 1430 |
| 24 | CHI | -3.8 | -4.1 | -1.7 | -2.1 | 106.4 | -1.0 | 1412 |
| 25 | WAS | -4.5 | -4.6 | -2.0 | -2.6 | 100.9 | +0.3 | 1345 |
| 26 | CHA | -5.1 | -4.9 | -4.6 | -0.6 | 95.6 | -0.2 | 1451 |
| 27 | NOP | -5.3 | -5.5 | -1.7 | -3.6 | 103.3 | +0.8 | 1355 |
| 28 | MIL | -7.1 | -7.3 | -2.5 | -4.5 | 103.2 | +0.0 | 1322 |
| 29 | BKN | -7.1 | -7.2 | -2.3 | -4.8 | 101.0 | +0.8 | 1304 |
| 30 | SAC | -7.5 | -7.6 | -3.9 | -3.6 | 100.5 | +0.7 | 1312 |

## Top players

Regularized adjusted plus-minus from every lineup this season and past ones: points per 100 possessions a player adds on offense and saves on defense, against an average player, shrunk toward last season's rating. Players expected to play 20 minutes or more.

| # | Player | Team | Net impact per 100 | Offense | Defense | Expected minutes |
|---|---|---|---|---|---|---|
| 1 | Victor Wembanyama | SAS | +8.5 | +2.5 | +6.0 | 32 |
| 2 | Shai Gilgeous-Alexander | OKC | +5.9 | +5.4 | +0.5 | 36 |
| 3 | Nikola Jokic | DEN | +5.1 | +4.7 | +0.4 | 37 |
| 4 | Kawhi Leonard | TOR | +4.6 | +3.6 | +1.0 | 30 |
| 5 | Giannis Antetokounmpo | MIA | +4.3 | +4.2 | +0.1 | 31 |
| 6 | Kyrie Irving | DAL | +4.3 | +3.9 | +0.4 | 32 |
| 7 | Luka Doncic | LAL | +3.7 | +4.8 | -1.1 | 36 |
| 8 | Joel Embiid | PHI | +2.9 | +1.9 | +1.0 | 33 |
| 9 | Derrick White | BOS | +2.8 | +0.5 | +2.3 | 31 |
| 10 | Neemias Queta | BOS | +2.7 | +0.8 | +1.9 | 27 |
| 11 | Dyson Daniels | ATL | +2.6 | +0.4 | +2.2 | 36 |
| 12 | Bam Adebayo | MIA | +2.2 | +1.7 | +0.5 | 32 |
| 13 | Jimmy Butler III | GSW | +2.2 | +2.1 | +0.1 | 27 |
| 14 | Ausar Thompson | DET | +2.2 | +0.2 | +2.0 | 33 |
| 15 | LaMelo Ball | MIN | +2.2 | +3.5 | -1.3 | 31 |
| 16 | Chet Holmgren | OKC | +2.1 | +0.0 | +2.1 | 30 |
| 17 | Marcus Smart | HOU | +2.1 | +0.5 | +1.6 | 22 |
| 18 | Herbert Jones | NOP | +2.1 | -1.1 | +3.2 | 25 |
| 19 | Fred VanVleet | HOU | +2.0 | +1.6 | +0.4 | 31 |
| 20 | Paul George | BOS | +2.0 | +0.9 | +1.1 | 32 |
| 21 | Ty Jerome | MEM | +2.0 | +2.7 | -0.6 | 29 |
| 22 | Pascal Siakam | IND | +2.0 | +1.4 | +0.6 | 33 |
| 23 | Javonte Green | DET | +2.0 | +0.0 | +1.9 | 24 |
| 24 | Franz Wagner | ORL | +1.9 | +1.1 | +0.8 | 36 |
| 25 | Jrue Holiday | POR | +1.9 | +1.1 | +0.7 | 29 |
| 26 | Paul Reed | DET | +1.8 | +0.5 | +1.3 | 24 |
| 27 | Damian Lillard | POR | +1.8 | +1.7 | +0.1 | 31 |
| 28 | Donovan Mitchell | CLE | +1.7 | +3.0 | -1.3 | 34 |
| 29 | De'Aaron Fox | SAS | +1.7 | +1.3 | +0.4 | 28 |
| 30 | Austin Reaves | LAL | +1.5 | +2.6 | -1.1 | 33 |

## Current model fit

- Fitted on 5543 games from 2022-23 to 2026-27.
- Home court: +2.0 points per 100 possessions for the home team over the visitor (about 2.0 points a game).
- Second night of a back-to-back: -0.8 points per 100 scored, +1.2 allowed.
- Weights: team efficiency ratings 0.14 (offense) and 0.15 (defense); player lineup ratings 0.77 and 0.76.
- Blend: 82% on the betting line for the margin and 100% for the total, wherever there is a line (fitted on past closing lines).
- Simulator: each team's points vary by 11.0 with correlation 0.23; 5.2% of recent games went to overtime.
