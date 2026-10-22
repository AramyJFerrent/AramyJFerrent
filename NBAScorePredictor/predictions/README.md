# NBA score predictions

Updated Wed Oct 21, 2026 08:08 PM ET. Refreshed automatically several times a day during the season, around the injury report's deadlines; each game's prediction is locked at tip-off and graded once the final score is in.

Each team's expected points are its expected possessions times its expected points per possession, from team efficiency ratings and the ratings of the players expected to play, blended with the betting line. Each game is then simulated 10,000 times, overtime included. The predicted score is the expected points rounded; the 80% range holds 80% of simulated outcomes for each team. Basketball is the most predictable major sport, but a team's score still varies by about ±14 points around the forecast, so read the win chance and the ranges too.

Missing players come from the injury report: out players are left out, and doubtful, questionable and probable ones count with the share of their minutes their chance of playing implies, and their minutes go mostly to the bench. The effect is how many points of margin the team gains or loses against its full-strength roster: negative when it is missing good players, positive when the minutes go to better ones. Predictions are rerun when the report changes, up to tip-off.

The fair moneyline is the American odds that match the win chance exactly, with no bookmaker margin: -150 means risk $150 to win $100, +150 means risk $100 to win $150.

The edge columns check every side of the spread, the moneyline and the total for expected value: the profit per $1 bet at the posted price, using the model's own chances before any blending with the line (its own simulated scores, pushes returning the stake). A side is an edge when its EV is 3% or more; the best such side is shown with its price, its EV and the model's chance of winning the bet. Where a spread or total price is not posted it is assumed to be -110 (marked \*); a moneyline is never assumed. Edges are logged with each prediction, locked at tip-off and graded below. Treat them as an experiment: the model alone is less accurate than the closing line, and its backtest found no edge against closing lines.

## Wednesday, October 21

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Spread: model / line | Total: model / line | 80% range | Overtime | Missing (effect on margin) | Spread edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 8:30 PM | DAL @ HOU | DAL 111, HOU 120 | HOU 76% | DAL +310 / HOU -310<br>posted DAL +330 / HOU -425 | HOU -9.3 / HOU -9.5 (fav covers 49%) | 230.5 / 230.5 (over 49%) | 96–125 / 106–134 | 4% | DAL: Santi Aldama (out); Dereck Lively II (out) (-0.3)<br>HOU: Steven Adams (out) (-0.6) | DAL +9.5 (-102): EV +5.6%, model 53% | DAL ML (+330): EV +9.9%, model 26% | Under 230.5 (-118): EV +17.1%, model 63% |
| 10:00 PM | GSW @ LAL | GSW 114, LAL 120 | LAL 67% | GSW +200 / LAL -200<br>posted GSW +190 / LAL -230 | LAL -5.8 / LAL -6.5 (fav covers 49%) | 234.4 / 234.5 (over 48%) | 100–129 / 106–135 | 5% | GSW: Brandin Podziemski (out); Stephen Curry (day-to-day); Moses Moody (out); Jimmy Butler III (out); Kristaps Porzingis (out) (-1.3)<br>LAL: Collin Sexton (out) (+1.4) | GSW +6.5 (-108): EV +14.9%, model 60% | GSW ML (+190): EV +21.1%, model 42% | Under 234.5 (-108): EV +32.9%, model 69% |
| 10:00 PM | PHX @ POR | PHX 115, POR 117 | POR 58% | PHX +135 / POR -135<br>posted PHX +120 / POR -142 | POR -2.6 / POR -2.5 (fav covers 52%) | 231.7 / 231.5 (over 49%) | 100–130 / 103–132 | 5% | PHX: Luke Kennard (day-to-day); Mark Williams (out) (+0.4)<br>POR: Deni Avdija (day-to-day); Micah Potter (day-to-day); Branden Carlson (out) (+1.3) | no edge | no edge | Under 231.5 (-108): EV +24.0%, model 64% |
| 10:30 PM | SAC @ LAC | SAC 111, LAC 116 | LAC 66% | SAC +195 / LAC -195<br>posted SAC +154 / LAC -185 | LAC -5.4 / LAC -5.5 (fav covers 50%) | 226.5 / 226.5 (over 49%) | 96–125 / 102–131 | 5% | SAC: Maxime Raynaud (out); Dylan Cardwell (out); Malik Monk (day-to-day) (+1.0)<br>LAC: Max Strus (out); Brandon Ingram (out); Jordan Miller (out); Bradley Beal (out); Yanic Konan Niederhauser (out) (+0.7) | no edge | no edge | Under 226.5 (-108): EV +6.4%, model 55% |

## Thursday, October 22

| Time (ET) | Game | Predicted score | Win chance | Fair moneyline | Spread: model / line | Total: model / line | 80% range | Overtime | Missing (effect on margin) | Spread edge | Moneyline edge | Total edge |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 7:00 PM | CLE @ PHI | CLE 116, PHI 119 | PHI 59% | CLE +145 / PHI -145<br>posted CLE +130 / PHI -155 | PHI -3.2 / PHI -3.5 (fav covers 51%) | 235.4 / 235.5 (over 49%) | 101–131 / 105–134 | 5% | CLE: Jarrett Allen (day-to-day) (+0.3)<br>PHI: Dean Wade (day-to-day); Dominick Barlow (out) (-0.1) | no edge | no edge | Under 235.5 (-108): EV +30.3%, model 68% |
| 9:30 PM | DEN @ OKC | DEN 114, OKC 121 | OKC 70% | DEN +235 / OKC -235<br>posted DEN +250 / OKC -298 | OKC -7.2 / OKC -7.5 (fav covers 49%) | 235.5 / 235.5 (over 49%) | 99–129 / 107–136 | 5% | DEN: Spencer Jones (day-to-day) (+0.4) | no edge | DEN ML (+250): EV +12.6%, model 32% | Under 235.5 (-110): EV +22.8%, model 64% |

## How the 2026-27 predictions have done

| Predictor | Games | Margin MAE | Total MAE | Team-points MAE | Log loss | Brier | Winners | 80% range hit |
|---|---|---|---|---|---|---|---|---|
| Final prediction | 3 | 10.68 | 16.25 | 8.37 | 0.829 | 0.316 | 33.3% | 83.3% |
| Model only (before blending) | 3 | 12.89 | 10.82 | 7.75 | 0.993 | 0.392 | 0.0% | – |
| Elo | 3 | 11.91 | – | – | 1.061 | 0.404 | 33.3% | – |
| Final prediction, games with a line | 3 | 10.68 | 16.25 | 8.37 | 0.829 | 0.316 | 33.3% | 83.3% |
| Model only, games with a line | 3 | 12.89 | 10.82 | 7.75 | 0.993 | 0.392 | 0.0% | – |
| Betting line | 3 | 10.17 | 16.17 | 8.25 | 0.785 | 0.295 | 33.3% | – |

MAE is the average miss in points; team-points MAE is the average miss on each team's score. Log loss and Brier score the win chances (lower is better; a coin flip scores 0.693 and 0.250). The closing line misses margins by about 10 points and totals by about 14.

Overtime: predicted in 5.2% of games, happened in 0.0%.

### Betting edges

| Market | Edges | Record (W-L-P) | Units | ROI |
|---|---|---|---|---|
| Spread | 2 | 0-2-0 | -2.00 | -100.0% |
| Moneyline | 3 | 0-3-0 | -3.00 | -100.0% |
| Total | 2 | 2-0-0 | +1.88 | +93.9% |

Spread moved toward the model's first spread edge before tip-off: 1 of 2 games (50%).

Live predictions only, 1 unit on each edge at the price logged with the last prediction before tip-off; a push returns the stake. ROI is units won per unit bet. The line moving toward the model's edge before tip-off is the quickest sign that it knows something the market doesn't yet.

### Results, Tuesday, October 20

| Game | Predicted | Final | Win chance for winner | Spread: model / line | Inside 80% ranges |
|---|---|---|---|---|---|
| BOS @ DET | 111–110 | 113–121 | 46% | BOS -1.6 / BOS -1.5 | yes |
| PHI @ NYK | 113–118 | 106–100 | 35% | NYK -5.2 / NYK -4.5 | no |
| OKC @ SAS | 116–115 | 116–104 | 52% | OKC -0.8 / OKC -1.5 | yes |

## Power ratings

Points per 100 possessions better than an average team on a neutral floor, combining opponent-adjusted team efficiency (garbage time removed) with the ratings of the team's healthy roster, through the fitted points map. Net per game uses the team's pace. Injury effect now is what its current injury report does to its margin, in points.

| # | Team | Net per 100 | Net per game | Offense | Defense | Pace | Injury effect now | Elo |
|---|---|---|---|---|---|---|---|---|
| 1 | SAS | +7.2 | +7.6 | +2.2 | +5.0 | 106.0 | +0.9 | 1687 |
| 2 | BOS | +6.6 | +6.6 | +3.7 | +2.9 | 100.9 | +1.1 | 1602 |
| 3 | OKC | +6.3 | +6.6 | +1.4 | +4.8 | 105.0 | +2.0 | 1702 |
| 4 | NYK | +4.6 | +4.8 | +1.4 | +3.2 | 103.9 | +0.0 | 1711 |
| 5 | HOU | +4.3 | +4.4 | +1.9 | +2.4 | 102.9 | -0.6 | 1571 |
| 6 | DEN | +3.3 | +3.5 | +4.5 | -1.1 | 103.8 | +0.4 | 1596 |
| 7 | DET | +3.2 | +3.3 | +1.7 | +1.5 | 102.0 | +0.2 | 1623 |
| 8 | ORL | +2.9 | +3.0 | -0.5 | +3.5 | 104.3 | +1.8 | 1551 |
| 9 | POR | +2.3 | +2.4 | +0.8 | +1.5 | 104.1 | +1.4 | 1522 |
| 10 | PHX | +2.3 | +2.4 | +2.0 | +0.3 | 103.5 | +0.4 | 1526 |
| 11 | PHI | +1.9 | +2.0 | +0.4 | +1.5 | 105.5 | -0.1 | 1550 |
| 12 | TOR | +1.6 | +1.7 | +0.6 | +1.0 | 104.5 | +0.6 | 1546 |
| 13 | MIA | +1.5 | +1.6 | +1.2 | +0.3 | 103.8 | +0.0 | 1522 |
| 14 | CLE | +1.5 | +1.6 | +1.7 | -0.2 | 103.0 | +0.3 | 1579 |
| 15 | GSW | +1.5 | +1.5 | +1.1 | +0.4 | 103.5 | -1.3 | 1452 |
| 16 | ATL | -0.3 | -0.3 | -0.1 | -0.1 | 105.2 | +0.6 | 1531 |
| 17 | LAL | -0.5 | -0.5 | +0.2 | -0.7 | 102.4 | +1.4 | 1569 |
| 18 | MIN | -0.5 | -0.5 | -0.1 | -0.4 | 105.2 | -0.4 | 1558 |
| 19 | CHA | -1.4 | -1.5 | -1.6 | +0.2 | 103.6 | -0.8 | 1597 |
| 20 | LAC | -1.8 | -1.8 | -0.8 | -1.0 | 103.3 | +0.8 | 1525 |
| 21 | IND | -1.9 | -2.0 | -0.3 | -1.7 | 105.1 | -0.8 | 1379 |
| 22 | UTA | -2.6 | -2.7 | -1.6 | -1.0 | 106.1 | +0.0 | 1342 |
| 23 | DAL | -2.6 | -2.7 | -1.5 | -1.1 | 104.6 | -0.3 | 1393 |
| 24 | CHI | -4.6 | -4.9 | -3.1 | -1.5 | 106.2 | +1.5 | 1384 |
| 25 | MEM | -4.6 | -4.9 | -1.7 | -2.9 | 105.8 | -0.1 | 1336 |
| 26 | MIL | -5.2 | -5.4 | -1.7 | -3.5 | 103.7 | +0.0 | 1388 |
| 27 | SAC | -5.5 | -5.7 | -2.5 | -3.0 | 103.9 | +1.0 | 1374 |
| 28 | NOP | -6.1 | -6.4 | -2.6 | -3.5 | 105.1 | +0.0 | 1429 |
| 29 | WAS | -6.7 | -7.1 | -3.0 | -3.7 | 105.7 | +0.4 | 1285 |
| 30 | BKN | -6.8 | -7.1 | -3.8 | -3.0 | 103.8 | +0.3 | 1320 |

## Top players

Regularized adjusted plus-minus from every lineup this season and past ones: points per 100 possessions a player adds on offense and saves on defense, against an average player, shrunk toward last season's rating. Players expected to play 20 minutes or more.

| # | Player | Team | Net impact per 100 | Offense | Defense | Expected minutes |
|---|---|---|---|---|---|---|
| 1 | Shai Gilgeous-Alexander | OKC | +5.7 | +5.2 | +0.6 | 37 |
| 2 | Nikola Jokic | DEN | +5.5 | +5.8 | -0.3 | 40 |
| 3 | Victor Wembanyama | SAS | +5.4 | +0.9 | +4.5 | 38 |
| 4 | Giannis Antetokounmpo | MIA | +4.9 | +4.4 | +0.6 | 27 |
| 5 | Kawhi Leonard | TOR | +4.9 | +4.3 | +0.6 | 35 |
| 6 | Alex Caruso | OKC | +3.9 | +0.0 | +3.8 | 27 |
| 7 | Joel Embiid | PHI | +3.0 | +1.8 | +1.2 | 32 |
| 8 | Franz Wagner | ORL | +2.7 | +1.1 | +1.6 | 28 |
| 9 | Kyrie Irving | DAL | +2.7 | +2.7 | +0.0 | 27 |
| 10 | Bam Adebayo | MIA | +2.5 | +0.9 | +1.5 | 25 |
| 11 | Chet Holmgren | OKC | +2.3 | +0.4 | +1.9 | 30 |
| 12 | Jimmy Butler III | GSW | +2.2 | +2.1 | +0.1 | 27 |
| 13 | Derrick White | BOS | +2.1 | +0.3 | +1.8 | 37 |
| 14 | Luka Doncic | LAL | +2.1 | +3.3 | -1.2 | 33 |
| 15 | Lauri Markkanen | UTA | +2.1 | +1.4 | +0.7 | 27 |
| 16 | Jarrett Allen | CLE | +2.0 | +1.6 | +0.4 | 30 |
| 17 | Dyson Daniels | ATL | +2.0 | +1.0 | +1.0 | 24 |
| 18 | Marcus Smart | HOU | +1.9 | +0.4 | +1.5 | 34 |
| 19 | Pascal Siakam | IND | +1.8 | +1.4 | +0.4 | 30 |
| 20 | Ausar Thompson | DET | +1.8 | -0.2 | +1.9 | 30 |
| 21 | Fred VanVleet | HOU | +1.5 | +0.9 | +0.6 | 40 |
| 22 | OG Anunoby | NYK | +1.5 | -0.3 | +1.7 | 34 |
| 23 | Donovan Mitchell | CLE | +1.4 | +2.0 | -0.6 | 36 |
| 24 | Cade Cunningham | DET | +1.3 | +1.4 | -0.1 | 38 |
| 25 | Devin Booker | PHX | +1.2 | +2.4 | -1.1 | 39 |
| 26 | Jayson Tatum | BOS | +1.2 | +1.3 | -0.1 | 36 |
| 27 | Devin Vassell | SAS | +1.1 | +0.6 | +0.5 | 36 |
| 28 | Paul George | BOS | +1.0 | -0.1 | +1.1 | 33 |
| 29 | Amen Thompson | HOU | +1.0 | +0.3 | +0.6 | 44 |
| 30 | Neemias Queta | BOS | +1.0 | +0.1 | +0.8 | 24 |

## Current model fit

- Fitted on 5285 games from 2022-23 to 2026-27.
- Home court: +2.0 points per 100 possessions for the home team over the visitor (about 2.0 points a game).
- Second night of a back-to-back: -0.7 points per 100 scored, +1.2 allowed.
- Weights: team efficiency ratings 0.16 (offense) and 0.17 (defense); player lineup ratings 0.76 and 0.74.
- Blend: 81% on the betting line for the margin and 100% for the total, wherever there is a line (fitted on past closing lines).
- Simulator: each team's points vary by 10.9 with correlation 0.23; 5.2% of recent games went to overtime.
