# NBA score predictions

Updated Tue Nov 24, 2026 12:27 AM ET. Refreshed automatically several times a day during the season, around the injury report's deadlines; each game's prediction is locked at tip-off and graded once the final score is in.

Each team's expected points are its expected possessions times its expected points per possession, from team efficiency ratings and the ratings of the players expected to play, blended with the betting line. Each game is then simulated 10,000 times, overtime included. The predicted score is the expected points rounded; the 80% range holds 80% of simulated outcomes for each team. Basketball is the most predictable major sport, but a team's score still varies by about ±14 points around the forecast, so read the win chance and the ranges too.

Missing players come from the injury report: out players are left out, and doubtful, questionable and probable ones count with the share of their minutes their chance of playing implies, and their minutes go mostly to the bench. The effect is how many points of margin the team gains or loses against its full-strength roster: negative when it is missing good players, positive when the minutes go to better ones. Predictions are rerun when the report changes, up to tip-off.

The fair moneyline is the American odds that match the win chance exactly, with no bookmaker margin: -150 means risk $150 to win $100, +150 means risk $100 to win $150.

The edge columns check every side of the spread, the moneyline and the total for expected value: the profit per $1 bet at the posted price, using the final prediction's chances (the model blended with the line, simulated against the posted lines, pushes returning the stake, and anchored to the market's own chances so only what the blend moves off the line counts). The model's own spread and total are shown alongside, but the blend keeps only the share of that disagreement the model has earned in past seasons, so edges are rare. A side is an edge when its EV is 3% or more; the best such side is shown with its price, its EV, its chance of winning the bet and its stake, a 25% share of the Kelly stake in units of 1% of the bankroll, with at most 3 units on one game. Where a spread or total price is not posted it is assumed to be -110 (marked \*); a moneyline is never assumed. Edges are logged with each prediction, locked at tip-off and graded below. Treat them as an experiment, not betting advice; see the backtest for how they have done on past seasons.

## Tuesday, November 24

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Spread: model / line | Total: model / line | 80% range | Overtime | Missing (effect on margin) | Spread edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 7:00 PM | DET @ ORL | DET 108, ORL 106 | DET 55% | DET -120 / ORL +120<br>posted DET -130 / ORL +110 | DET -1.6 / DET -1.5 (fav covers 52%) | 213.9 / 213.5 (over 50%) | 94–122 / 92–120 | 6% | DET: Cade Cunningham (day-to-day); Duncan Robinson (out); Jalen Duren (out) (-0.3)<br>ORL: Paolo Banchero (out) (+1.5) | no edge | no edge | no edge |
| 8:00 PM | BOS @ WAS | BOS 114, WAS 104 | BOS 78% | BOS -350 / WAS +350<br>posted BOS -453 / WAS +351 | BOS -10.2 / BOS -10.5 (fav covers 48%) | 217.2 / 217.5 (over 49%) | 100–128 / 90–118 | 4% | BOS: Mitchell Robinson (out) (+0.4)<br>WAS: Jamir Watkins (out); Justin Champagnie (out); Tristan Vukcevic (out) (+0.3) | no edge | no edge | no edge |
| 10:00 PM | DAL @ DEN | DAL 112, DEN 120 | DEN 72% | DAL +265 / DEN -265<br>posted DAL +260 / DEN -322 | DEN -8.4 / DEN -8.5 (fav covers 50%) | 231.6 / 231.5 (over 49%) | 97–127 / 106–134 | 4% | DAL: P.J. Washington (day-to-day); Dereck Lively II (out); Sergio de Larrea (out) (+1.0) | no edge | no edge | no edge |

## Wednesday, November 25

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Spread: model / line | Total: model / line | 80% range | Overtime | Missing (effect on margin) | Spread edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 5:00 PM | MIA @ PHI | MIA 116, PHI 120 | PHI 60% | MIA +150 / PHI -150 | PHI -3.4 | 235.8 | 101–131 / 105–134 | 5% | MIA: Giannis Antetokounmpo (day-to-day) (-0.9)<br>PHI: Joel Embiid (day-to-day) (-0.5) | no line yet | no line yet | no line yet |
| 7:00 PM | CHI @ CHA | CHI 112, CHA 111 | CHI 52% | CHI -105 / CHA +105 | CHI -0.6 | 223.5 | 98–126 / 97–126 | 5% | CHI: Norman Powell (out); Caleb Wilson (out) (+0.7)<br>CHA: Grayson Allen (out); Dennis Schroder (out); Grant Williams (day-to-day); Kon Knueppel (out); Ryan Kalkbrenner (day-to-day) (-0.5) | no line yet | no line yet | no line yet |
| 7:30 PM | CLE @ NYK | CLE 108, NYK 113 | NYK 64% | CLE +180 / NYK -180 | NYK -4.9 | 220.4 | 94–122 / 99–127 | 5% | CLE: Evan Mobley (out) (-0.3)<br>NYK: OG Anunoby (day-to-day) (-0.4) | no line yet | no line yet | no line yet |
| 7:30 PM | MIN @ OKC | MIN 113, OKC 111 | MIN 57% | MIN -130 / OKC +130 | MIN -2.3 | 223.8 | 99–127 / 96–125 | 5% | MIN: Anthony Edwards (out); Donte DiVincenzo (out); Jaylen Clark (out) (-0.6)<br>OKC: Chet Holmgren (out); Jalen Williams (out); Aday Mara (day-to-day); Cason Wallace (out); Alex Caruso (out); Jaylin Williams (day-to-day) (-1.6) | no line yet | no line yet | no line yet |
| 8:00 PM | LAC @ MEM | LAC 113, MEM 119 | MEM 69% | LAC +220 / MEM -220 | MEM -6.4 | 231.8 | 98–128 / 105–134 | 5% | LAC: Jordan Miller (out); Bradley Beal (out) (+0.5)<br>MEM: Cameron Boozer (out); Jerami Grant (out); Scotty Pippen Jr. (out) (+2.2) | no line yet | no line yet | no line yet |
| 8:00 PM | BKN @ MIL | BKN 116, MIL 117 | MIL 51% | BKN +105 / MIL -105 | MIL -0.5 | 233.2 | 102–131 / 102–132 | 6% | BKN: Nolan Traore (out) (+0.8) | no line yet | no line yet | no line yet |
| 8:30 PM | PHX @ HOU | PHX 110, HOU 117 | HOU 69% | PHX +220 / HOU -220 | HOU -6.7 | 227.5 | 96–125 / 103–131 | 5% | PHX: Mark Williams (out) (+0.5) | no line yet | no line yet | no line yet |
| 10:00 PM | SAC @ GSW | SAC 108, GSW 112 | GSW 64% | SAC +175 / GSW -175 | GSW -4.7 | 219.7 | 93–122 / 98–126 | 5% | SAC: Maxime Raynaud (out) (+0.7)<br>GSW: Moses Moody (out); Jimmy Butler III (out); Kristaps Porzingis (out); Stephen Curry (out); Brandon Williams (out) (-3.3) | no line yet | no line yet | no line yet |
| 10:00 PM | SAS @ POR | SAS 111, POR 115 | POR 63% | SAS +170 / POR -170 | POR -4.3 | 226.6 | 97–126 / 101–130 | 5% | SAS: Dylan Harper (out); Victor Wembanyama (out); Tobias Harris (out); De'Aaron Fox (out) (-6.6)<br>POR: Ja Morant (out); Chris Youngblood (out) (+0.6) | no line yet | no line yet | no line yet |

## How the 2026-27 predictions have done

| Predictor | Games | Margin MAE | Total MAE | Team-points MAE | Log loss | Brier | Winners | 80% range hit |
|---|---|---|---|---|---|---|---|---|
| Final prediction | 248 | 10.91 | 14.55 | 9.38 | 0.574 | 0.196 | 70.2% | 80.6% |
| Model only (before blending) | 248 | 11.18 | 14.48 | 9.46 | 0.592 | 0.204 | 69.4% | – |
| Elo | 248 | 11.51 | – | – | 0.612 | 0.212 | 64.9% | – |
| Final prediction, games with a line | 248 | 10.91 | 14.55 | 9.38 | 0.574 | 0.196 | 70.2% | 80.6% |
| Model only, games with a line | 248 | 11.18 | 14.48 | 9.46 | 0.592 | 0.204 | 69.4% | – |
| Betting line | 248 | 10.89 | 14.56 | 9.38 | 0.570 | 0.194 | 70.2% | – |

MAE is the average miss in points; team-points MAE is the average miss on each team's score. Log loss and Brier score the win chances (lower is better; a coin flip scores 0.693 and 0.250). The closing line misses margins by about 10 points and totals by about 14.

Overtime: predicted in 4.7% of games, happened in 5.2%.

### Betting edges

| Market | Edges | Record (W-L-P) | Staked | Units won | ROI | Expected ROI |
|---|---|---|---|---|---|---|
| Spread | 1 | 1-0-0 | 1.0 | +0.90 | +89.3% | +3.6% |
| Moneyline | 15 | 2-13-0 | 5.6 | -2.59 | -46.2% | +6.5% |
| Total | 0 | 0-0-0 | 0.0 | +0.00 | – | – |

Spread moved toward the model's first spread edge before tip-off: 5 of 6 games (83%).

Live predictions only, each edge at the stake and price logged with the last prediction before tip-off (edges logged before edges were priced from the final prediction are left out); a push returns the stake. Units are 1% of the bankroll; ROI is units won per unit staked, and expected ROI is what the edges' EVs promised. The line moving toward the model's edge before tip-off is the quickest sign that it knows something the market doesn't yet.

### Results, Sunday, November 22

| Game | Predicted | Final | Win chance for winner | Spread: model / line | Inside 80% ranges |
|---|---|---|---|---|---|
| DET @ ATL | 114–111 | 97–107 | 41% | DET -2.9 / DET -2.5 | no |
| OKC @ MIA | 111–115 | 113–123 | 61% | MIA -3.8 / MIA -4.5 | yes |
| ORL @ WAS | 112–108 | 96–116 | 36% | ORL -4.6 / ORL -4.5 | no |
| DEN @ CHI | 123–113 | 151–145 (OT) | 76% | DEN -9.7 / DEN -10.5 | no |
| DAL @ UTA | 114–112 | 116–114 | 55% | DAL -1.8 / DAL -2.5 | yes |
| IND @ NYK | 103–110 | 106–113 | 70% | NYK -6.7 / NYK -7.5 | yes |
| BOS @ GSW | 109–102 | 87–88 | 28% | BOS -7.4 / BOS -7.5 | no |

## Power ratings

Points per 100 possessions better than an average team on a neutral floor, combining opponent-adjusted team efficiency (garbage time removed) with the ratings of the team's healthy roster, through the fitted points map. Net per game uses the team's pace. Injury effect now is what its current injury report does to its margin, in points.

| # | Team | Net per 100 | Net per game | Offense | Defense | Pace | Injury effect now | Elo |
|---|---|---|---|---|---|---|---|---|
| 1 | SAS | +7.6 | +7.6 | +2.8 | +4.8 | 100.0 | -6.5 | 1718 |
| 2 | BOS | +7.3 | +7.0 | +2.4 | +4.9 | 95.4 | +0.4 | 1634 |
| 3 | HOU | +5.9 | +5.8 | +3.7 | +2.2 | 98.6 | +0.0 | 1613 |
| 4 | DET | +5.3 | +5.2 | +2.2 | +3.1 | 97.4 | -0.3 | 1629 |
| 5 | DEN | +5.0 | +5.0 | +5.1 | -0.1 | 100.2 | +0.0 | 1586 |
| 6 | MIN | +5.0 | +5.2 | +0.6 | +4.4 | 103.4 | -0.6 | 1612 |
| 7 | NYK | +3.8 | +3.5 | -0.1 | +3.9 | 93.8 | -0.4 | 1696 |
| 8 | LAL | +3.6 | +3.7 | +3.2 | +0.4 | 101.7 | -1.3 | 1604 |
| 9 | POR | +2.9 | +3.0 | +1.5 | +1.4 | 102.3 | +0.6 | 1576 |
| 10 | PHI | +1.8 | +1.9 | +1.6 | +0.2 | 100.7 | -0.4 | 1583 |
| 11 | OKC | +1.8 | +1.8 | -0.9 | +2.6 | 101.7 | -1.6 | 1630 |
| 12 | MIA | +0.8 | +0.8 | +2.2 | -1.4 | 104.6 | -0.9 | 1559 |
| 13 | PHX | +0.6 | +0.6 | +1.0 | -0.4 | 100.5 | +0.5 | 1534 |
| 14 | CLE | +0.4 | +0.4 | +1.8 | -1.4 | 101.5 | -0.3 | 1570 |
| 15 | TOR | +0.2 | +0.2 | +0.0 | +0.2 | 97.4 | -2.4 | 1500 |
| 16 | GSW | -0.4 | -0.4 | -1.0 | +0.6 | 98.4 | -3.3 | 1474 |
| 17 | ORL | -0.6 | -0.6 | -1.5 | +0.9 | 98.4 | +1.5 | 1497 |
| 18 | MEM | -0.7 | -0.7 | +1.3 | -2.0 | 100.5 | +2.2 | 1487 |
| 19 | IND | -1.3 | -1.3 | -0.4 | -0.9 | 105.3 | +0.0 | 1361 |
| 20 | UTA | -1.3 | -1.3 | -2.0 | +0.7 | 100.4 | -2.3 | 1342 |
| 21 | DAL | -1.8 | -1.8 | -1.1 | -0.7 | 100.9 | +1.0 | 1460 |
| 22 | ATL | -2.0 | -2.1 | -2.1 | +0.2 | 106.2 | +1.0 | 1561 |
| 23 | LAC | -3.4 | -3.5 | -1.4 | -2.1 | 101.1 | +0.5 | 1433 |
| 24 | CHI | -3.7 | -3.9 | -1.5 | -2.2 | 107.4 | +0.7 | 1394 |
| 25 | WAS | -4.6 | -4.6 | -2.2 | -2.4 | 99.4 | +0.3 | 1350 |
| 26 | CHA | -5.1 | -4.9 | -4.7 | -0.5 | 95.7 | -0.5 | 1460 |
| 27 | NOP | -5.4 | -5.5 | -1.6 | -3.8 | 103.0 | +0.7 | 1359 |
| 28 | BKN | -6.9 | -6.9 | -2.5 | -4.3 | 100.8 | +0.8 | 1308 |
| 29 | SAC | -7.3 | -7.4 | -4.0 | -3.3 | 101.3 | +0.7 | 1315 |
| 30 | MIL | -7.6 | -7.8 | -2.8 | -4.7 | 103.1 | +0.0 | 1308 |

## Top players

Regularized adjusted plus-minus from every lineup this season and past ones: points per 100 possessions a player adds on offense and saves on defense, against an average player, shrunk toward last season's rating. Players expected to play 20 minutes or more.

| # | Player | Team | Net impact per 100 | Offense | Defense | Expected minutes |
|---|---|---|---|---|---|---|
| 1 | Victor Wembanyama | SAS | +8.5 | +2.6 | +5.9 | 32 |
| 2 | Shai Gilgeous-Alexander | OKC | +5.8 | +5.2 | +0.6 | 35 |
| 3 | Nikola Jokic | DEN | +5.2 | +4.9 | +0.3 | 39 |
| 4 | Kawhi Leonard | TOR | +4.6 | +3.6 | +0.9 | 30 |
| 5 | Giannis Antetokounmpo | MIA | +4.3 | +4.2 | +0.1 | 31 |
| 6 | Kyrie Irving | DAL | +3.9 | +3.6 | +0.2 | 31 |
| 7 | Luka Doncic | LAL | +3.7 | +4.8 | -1.1 | 37 |
| 8 | Joel Embiid | PHI | +2.8 | +1.9 | +1.0 | 33 |
| 9 | Dyson Daniels | ATL | +2.6 | +0.4 | +2.2 | 36 |
| 10 | Neemias Queta | BOS | +2.6 | +0.7 | +1.9 | 27 |
| 11 | Derrick White | BOS | +2.4 | +0.3 | +2.2 | 32 |
| 12 | Herbert Jones | NOP | +2.4 | -0.7 | +3.1 | 28 |
| 13 | Franz Wagner | ORL | +2.2 | +1.4 | +0.9 | 35 |
| 14 | Jimmy Butler III | GSW | +2.2 | +2.1 | +0.1 | 27 |
| 15 | Bam Adebayo | MIA | +2.2 | +1.7 | +0.5 | 32 |
| 16 | Chet Holmgren | OKC | +2.1 | +0.0 | +2.1 | 30 |
| 17 | LaMelo Ball | MIN | +2.1 | +3.4 | -1.4 | 31 |
| 18 | Paul Reed | DET | +2.0 | +0.7 | +1.4 | 26 |
| 19 | Marcus Smart | HOU | +2.0 | +0.5 | +1.4 | 20 |
| 20 | Ausar Thompson | DET | +2.0 | +0.1 | +1.9 | 34 |
| 21 | Pascal Siakam | IND | +1.9 | +1.3 | +0.6 | 32 |
| 22 | Fred VanVleet | HOU | +1.9 | +1.6 | +0.3 | 30 |
| 23 | Javonte Green | DET | +1.9 | +0.1 | +1.8 | 21 |
| 24 | Donovan Mitchell | CLE | +1.9 | +3.0 | -1.1 | 32 |
| 25 | Damian Lillard | POR | +1.8 | +1.8 | +0.1 | 32 |
| 26 | Jrue Holiday | POR | +1.8 | +1.0 | +0.7 | 30 |
| 27 | De'Aaron Fox | SAS | +1.7 | +1.4 | +0.3 | 28 |
| 28 | Ty Jerome | MEM | +1.7 | +2.6 | -0.9 | 29 |
| 29 | Dean Wade | PHI | +1.7 | +0.9 | +0.8 | 30 |
| 30 | Paul George | BOS | +1.6 | +0.4 | +1.1 | 31 |

## Current model fit

- Fitted on 5530 games from 2022-23 to 2026-27.
- Home court: +2.0 points per 100 possessions for the home team over the visitor (about 2.0 points a game).
- Second night of a back-to-back: -0.8 points per 100 scored, +1.2 allowed.
- Weights: team efficiency ratings 0.14 (offense) and 0.15 (defense); player lineup ratings 0.77 and 0.76.
- Blend: 82% on the betting line for the margin and 100% for the total, wherever there is a line (fitted on past closing lines).
- Simulator: each team's points vary by 11.0 with correlation 0.23; 5.2% of recent games went to overtime.
