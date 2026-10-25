# College football score predictions

Updated Sat Oct 24, 2026 08:19 PM ET. Refreshed automatically every day of the season and several times on Saturdays; each game's prediction is locked at kickoff and graded once the final score is in. Scores are the most likely real scoreline near the expected points; ranges cover 80% of simulated outcomes for each team. College scores scatter widely, so read the ranges, not just the headline score.

Expected points blend the model with the betting line using the weight that has predicted best in recent seasons (see Current model fit). The spread and total columns show the model's own numbers next to the line, so you can see where it disagrees. Games without a line yet use the model alone.

The fair moneyline is the American odds that match the win chance exactly, with no bookmaker margin: -200 means risk $200 to win $100, +200 means risk $100 to win $200. A sportsbook's price will be a little worse on both sides because of its cut, so a book only offers value on a team when its price beats the fair line.

The edge columns judge each bet by its expected value per $1 staked at the posted price, using the final prediction: the model blended with the line, run through the score simulator, pushes included, and anchored to the market's own chances so that only what the blend moves off the line counts. The model's own spread and total (shown alongside) sit several points from the line in most games, but the blend keeps only the share of that disagreement the model has earned in past seasons, so edges are rare. The side with the higher value is shown when it reaches 3% (+3 cents per $1), as the team or side, the price, the expected value, its chance of winning the bet and its stake, a 25% share of the Kelly stake in units of 1% of the bankroll with at most 3 units on one game; anything short is no edge. Where a book posts no price for a spread or total it is assumed to be -110 and marked -110*; moneylines are never assumed. In the walk-forward backtest against closing lines, edges returned spread -100.0% on 1 bets (posted prices, 2016–2019); spread -3.9% on 156 bets (assumed -110 prices, 2016–2025); moneyline +13.7% on 575 bets (posted prices, 2016–2025); total +2.6% on 367 bets (posted prices, 2016–2019); total -5.7% on 172 bets (assumed -110 prices, 2016–2025). None of these is clearly above zero, so treat these edges as an experiment, not a betting system. The live record is tracked below, graded at the price logged with the last prediction before kickoff.

## 2026 Week 8

| Kickoff (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected points | 80% range | Spread: model / line | Total: model / line | Spread edge | Moneyline edge | Total edge | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sat 10/24 10:00 PM | North Dakota State @ New Mexico | North Dakota State 17, New Mexico 20 | New Mexico 62% | North Dakota State +165 / New Mexico -165 | 17.7 – 22.3 | 7–30 / 10–36 | New Mexico -2.6 / New Mexico -4.8 | 43.0 / 39.5 | no edge | no edge | no edge |  |
| Sat 10/24 10:15 PM | Houston @ Utah | Houston 24, Utah 31 | Utah 67% | Houston +210 / Utah -210 | 25.4 – 32.1 | 13–39 / 17–48 | Utah -9.4 / Utah -6.5 | 58.4 / 57.2 | no edge | no edge | no edge |  |

## 2026 Week 9

| Kickoff (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected points | 80% range | Spread: model / line | Total: model / line | Spread edge | Moneyline edge | Total edge | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tue 10/27 7:00 PM | Delaware @ Western Kentucky | Delaware 24, Western Kentucky 27 | Western Kentucky 51% | Delaware +105 / Western Kentucky -105 | 27.1 – 27.4 | 14–41 / 14–42 | Western Kentucky -0.3 / – | 54.6 / – | no line yet | no line yet (fair: Western Kentucky -105) | no line yet |  |
| Tue 10/27 8:00 PM | Sam Houston @ Missouri State | Sam Houston 21, Missouri State 28 | Missouri State 66% | Sam Houston +195 / Missouri State -195 | 21.5 – 27.7 | 10–35 / 14–42 | Missouri State -6.3 / – | 49.2 / – | no line yet | no line yet (fair: Missouri State -195) | no line yet |  |
| Wed 10/28 7:00 PM | Kennesaw State @ Middle Tennessee | Kennesaw State 24, Middle Tennessee 27 | Middle Tennessee 58% | Kennesaw State +140 / Middle Tennessee -140 | 23.7 – 26.8 | 10–37 / 14–41 | Middle Tennessee -3.2 / – | 50.5 / – | no line yet | no line yet (fair: Middle Tennessee -140) | no line yet |  |
| Wed 10/28 8:00 PM | Jacksonville State @ New Mexico State | Jacksonville State 31, New Mexico State 24 | Jacksonville State 68% | Jacksonville State -210 / New Mexico State +210 | 28.8 – 22.1 | 14–44 / 10–35 | Jacksonville State -6.7 / – | 50.9 / – | no line yet | no line yet (fair: Jacksonville State -210) | no line yet |  |
| Thu 10/29 7:30 PM | Florida Atlantic @ North Texas | Florida Atlantic 31, North Texas 41 | North Texas 74% | Florida Atlantic +280 / North Texas -280 | 30.7 – 40.5 | 17–45 / 26–56 | North Texas -9.8 / – | 71.2 / – | no line yet | no line yet (fair: North Texas -280) | no line yet |  |
| Thu 10/29 7:30 PM | Troy @ James Madison | Troy 17, James Madison 34 | James Madison 89% | Troy +840 / James Madison -840 | 16.7 – 34.9 | 6–29 / 20–51 | James Madison -18.2 / – | 51.6 / – | no line yet | no line yet (fair: James Madison -840) | no line yet |  |
| Fri 10/30 7:00 PM | Tulane @ Charlotte | Tulane 31, Charlotte 17 | Tulane 86% | Tulane -600 / Charlotte +600 | 31.7 – 16.2 | 17–48 / 6–28 | Tulane -15.5 / – | 47.8 / – | no line yet | no line yet (fair: Tulane -600) | no line yet |  |
| Fri 10/30 7:30 PM | Baylor @ UCF | Baylor 27, UCF 24 | Baylor 51% | Baylor -105 / UCF +105 | 25.6 – 24.9 | 13–39 / 13–38 | Baylor -0.7 / – | 51.2 / – | no line yet | no line yet (fair: Baylor -105) | no line yet |  |
| Fri 10/30 10:30 PM | Kent State @ Sacramento State | Kent State 21, Sacramento State 24 | Sacramento State 52% | Kent State +105 / Sacramento State -105 | 23.8 – 24.2 | 10–38 / 10–38 | Sacramento State -0.5 / – | 48.0 / – | no line yet | no line yet (fair: Sacramento State -105) | no line yet |  |
| Sat 10/31 TBA | Northwestern @ Oregon | Northwestern 24, Oregon 31 | Oregon 68% | Northwestern +215 / Oregon -215 | 22.4 – 29.7 | 10–36 / 16–44 | Oregon -5.6 / Oregon -7.5 | 50.5 / 52.5 | no edge | no edge | no edge |  |
| Sat 10/31 TBA | Purdue @ Penn State | Purdue 17, Penn State 31 | Penn State 80% | Purdue +400 / Penn State -400 | 19.2 – 31.3 | 7–32 / 17–47 | Penn State -12.1 / – | 50.6 / – | no line yet | no line yet (fair: Penn State -400) | no line yet |  |
| Sat 10/31 12:00 PM | Arizona @ Texas Tech | Arizona 24, Texas Tech 31 | Texas Tech 70% | Arizona +240 / Texas Tech -240 | 22.6 – 30.3 | 10–36 / 17–45 | Texas Tech -9.5 / Texas Tech -7.5 | 48.9 / 54.5 | no edge | no edge | no edge |  |
| Sat 10/31 12:00 PM | California @ NC State | California 24, NC State 34 | NC State 77% | California +330 / NC State -330 | 24.7 – 35.6 | 10–38 / 20–52 | NC State -10.9 / – | 60.3 / – | no line yet | no line yet (fair: NC State -330) | no line yet |  |
| Sat 10/31 12:00 PM | SMU @ Syracuse | SMU 31, Syracuse 24 | SMU 74% | SMU -290 / Syracuse +290 | 32.2 – 22.4 | 17–48 / 10–35 | SMU -9.8 / – | 54.6 / – | no line yet | no line yet (fair: SMU -290) | no line yet |  |
| Sat 10/31 12:00 PM | Boston College @ Duke | Boston College 17, Duke 31 | Duke 80% | Boston College +390 / Duke -390 | 18.9 – 31.4 | 7–31 / 17–46 | Duke -12.5 / – | 50.3 / – | no line yet | no line yet (fair: Duke -390) | no line yet |  |
| Sat 10/31 12:00 PM | Wisconsin @ Iowa | Wisconsin 17, Iowa 20 | Iowa 64% | Wisconsin +180 / Iowa -180 | 17.8 – 22.5 | 7–30 / 10–35 | Iowa -6.8 / Iowa -4.5 | 43.4 / 39.5 | no edge | no edge | no edge |  |
| Sat 10/31 12:00 PM | Illinois @ Maryland | Illinois 24, Maryland 27 | Maryland 51% | Illinois +105 / Maryland -105 | 27.0 – 27.3 | 13–41 / 14–41 | Maryland -0.3 / – | 54.3 / – | no line yet | no line yet (fair: Maryland -105) | no line yet |  |
| Sat 10/31 12:00 PM | Notre Dame vs Navy | Notre Dame 42, Navy 14 | Notre Dame 98% | Notre Dame -4540 / Navy +4540 | 40.7 – 12.2 | 26–57 / 3–23 | Notre Dame -28.5 / Notre Dame -28.5 | 50.8 / 53.5 | no edge | no edge | no edge | neutral site |
| Sat 10/31 12:00 PM | UAB @ South Florida | UAB 17, South Florida 27 | South Florida 75% | UAB +305 / South Florida -305 | 18.9 – 29.0 | 7–31 / 14–44 | South Florida -10.1 / – | 50.4 / – | no line yet | no line yet (fair: South Florida -305) | no line yet |  |
| Sat 10/31 12:00 PM | Bowling Green @ Western Michigan | Bowling Green 14, Western Michigan 31 | Western Michigan 86% | Bowling Green +610 / Western Michigan -610 | 14.7 – 29.7 | 3–27 / 16–45 | Western Michigan -15.0 / – | 44.4 / – | no line yet | no line yet (fair: Western Michigan -610) | no line yet |  |
| Sat 10/31 12:30 PM | Michigan @ Rutgers | Michigan 31, Rutgers 17 | Michigan 86% | Michigan -610 / Rutgers +610 | 32.6 – 17.1 | 17–48 / 6–30 | Michigan -15.5 / – | 49.6 / – | no line yet | no line yet (fair: Michigan -610) | no line yet |  |
| Sat 10/31 12:45 PM | Auburn @ Ole Miss | Auburn 21, Ole Miss 31 | Ole Miss 76% | Auburn +315 / Ole Miss -315 | 22.1 – 32.5 | 10–35 / 17–48 | Ole Miss -9.4 / Ole Miss -10.5 | 58.6 / 53.5 | no edge | no edge | no edge |  |
| Sat 10/31 1:00 PM | Marshall @ Old Dominion | Marshall 24, Old Dominion 21 | Marshall 62% | Marshall -160 / Old Dominion +160 | 25.6 – 21.4 | 13–39 / 9–35 | Marshall -4.2 / – | 47.0 / – | no line yet | no line yet (fair: Marshall -160) | no line yet |  |
| Sat 10/31 2:00 PM | Kansas State @ Colorado | Kansas State 31, Colorado 24 | Kansas State 70% | Kansas State -230 / Colorado +230 | 30.0 – 22.2 | 16–45 / 10–36 | Kansas State -7.8 / – | 52.2 / – | no line yet | no line yet (fair: Kansas State -230) | no line yet |  |
| Sat 10/31 2:00 PM | Coastal Carolina @ Georgia State | Coastal Carolina 24, Georgia State 31 | Georgia State 69% | Coastal Carolina +230 / Georgia State -230 | 24.6 – 32.1 | 12–38 / 17–48 | Georgia State -7.6 / – | 56.7 / – | no line yet | no line yet (fair: Georgia State -230) | no line yet |  |
| Sat 10/31 3:00 PM | UConn @ Air Force | UConn 28, Air Force 31 | Air Force 54% | UConn +120 / Air Force -120 | 28.8 – 30.1 | 14–44 / 16–45 | Air Force -1.4 / – | 58.9 / – | no line yet | no line yet (fair: Air Force -120) | no line yet |  |
| Sat 10/31 3:00 PM | Temple @ East Carolina | Temple 24, East Carolina 31 | East Carolina 71% | Temple +245 / East Carolina -245 | 22.0 – 30.4 | 10–35 / 16–45 | East Carolina -8.4 / – | 52.3 / – | no line yet | no line yet (fair: East Carolina -245) | no line yet |  |
| Sat 10/31 3:00 PM | Louisiana Tech @ South Alabama | Louisiana Tech 31, South Alabama 28 | Louisiana Tech 57% | Louisiana Tech -135 / South Alabama +135 | 29.8 – 27.2 | 16–44 / 13–41 | Louisiana Tech -2.6 / – | 57.1 / – | no line yet | no line yet (fair: Louisiana Tech -135) | no line yet |  |
| Sat 10/31 3:15 PM | Stanford @ Louisville | Stanford 14, Louisville 42 | Louisville 97% | Stanford +3060 / Louisville -3060 | 14.7 – 41.5 | 3–27 / 27–58 | Louisville -26.8 / – | 56.2 / – | no line yet | no line yet (fair: Louisville -3060) | no line yet |  |
| Sat 10/31 3:30 PM | Florida vs Georgia | Florida 24, Georgia 34 | Georgia 75% | Florida +305 / Georgia -305 | 22.7 – 33.1 | 10–37 / 19–49 | Georgia -9.3 / Georgia -10.5 | 53.2 / 56.5 | no edge | no edge | no edge | neutral site |
| Sat 10/31 3:30 PM | Arizona State @ BYU | Arizona State 17, BYU 34 | BYU 87% | Arizona State +655 / BYU -655 | 17.5 – 33.8 | 6–30 / 20–49 | BYU -14.6 / BYU -16.5 | 50.6 / 51.5 | no edge | no edge | no edge |  |
| Sat 10/31 3:30 PM | Kansas @ TCU | Kansas 27, TCU 24 | Kansas 52% | Kansas -110 / TCU +110 | 24.2 – 23.5 | 10–38 / 10–38 | Kansas -0.6 / – | 49.4 / – | no line yet | no line yet (fair: Kansas -110) | no line yet |  |
| Sat 10/31 3:30 PM | Minnesota @ Indiana | Minnesota 10, Indiana 31 | Indiana 95% | Minnesota +1975 / Indiana -1975 | 11.0 – 33.4 | 2–21 / 19–49 | Indiana -21.0 / Indiana -22.5 | 40.2 / 45.5 | no edge | no edge | no edge |  |
| Sat 10/31 3:30 PM | Colorado State @ Utah State | Colorado State 24, Utah State 27 | Utah State 58% | Colorado State +140 / Utah State -140 | 26.1 – 29.4 | 13–41 / 15–44 | Utah State -3.3 / – | 55.5 / – | no line yet | no line yet (fair: Utah State -140) | no line yet |  |
| Sat 10/31 3:30 PM | UTEP @ North Dakota State | UTEP 7, North Dakota State 35 | North Dakota State 99% | UTEP +7165 / North Dakota State -7165 | 7.1 – 34.8 | 0–15 / 20–51 | North Dakota State -27.7 / – | 41.9 / – | no line yet | no line yet (fair: North Dakota State -7165) | no line yet |  |
| Sat 10/31 3:30 PM | Florida International @ Liberty | Florida International 14, Liberty 31 | Liberty 86% | Florida International +605 / Liberty -605 | 15.8 – 30.9 | 6–28 / 17–46 | Liberty -15.1 / – | 46.6 / – | no line yet | no line yet (fair: Liberty -605) | no line yet |  |
| Sat 10/31 3:30 PM | Southern Miss @ UL Monroe | Southern Miss 27, UL Monroe 24 | Southern Miss 58% | Southern Miss -140 / UL Monroe +140 | 28.9 – 26.0 | 14–44 / 13–41 | Southern Miss -2.8 / – | 55.3 / – | no line yet | no line yet (fair: Southern Miss -140) | no line yet |  |
| Sat 10/31 3:45 PM | Utah @ Cincinnati | Utah 31, Cincinnati 24 | Utah 74% | Utah -280 / Cincinnati +280 | 33.3 – 24.0 | 19–48 / 10–38 | Utah -7.0 / Utah -9.5 | 60.8 / 56.5 | no edge | no edge | no edge |  |
| Sat 10/31 3:45 PM | Virginia @ Wake Forest | Virginia 14, Wake Forest 31 | Wake Forest 85% | Virginia +580 / Wake Forest -580 | 16.5 – 31.8 | 6–28 / 17–48 | Wake Forest -15.3 / – | 48.4 / – | no line yet | no line yet (fair: Wake Forest -580) | no line yet |  |
| Sat 10/31 4:00 PM | New Mexico @ San José State | New Mexico 31, San José State 17 | New Mexico 79% | New Mexico -375 / San José State +375 | 30.8 – 18.7 | 16–45 / 7–31 | New Mexico -12.0 / – | 49.5 / – | no line yet | no line yet (fair: New Mexico -375) | no line yet |  |
| Sat 10/31 4:15 PM | South Carolina @ Oklahoma | South Carolina 17, Oklahoma 24 | Oklahoma 67% | South Carolina +205 / Oklahoma -205 | 18.5 – 24.6 | 7–31 / 10–38 | Oklahoma -11.7 / Oklahoma -5.5 | 44.6 / 43.5 | no edge | no edge | no edge |  |
| Sat 10/31 4:15 PM | Nevada @ UCLA | Nevada 7, UCLA 41 | UCLA 99% | Nevada +9900 / UCLA -9900 | 7.2 – 40.8 | 0–15 / 27–58 | UCLA -33.6 / – | 48.0 / – | no line yet | no line yet (fair: UCLA -9900) | no line yet |  |
| Sat 10/31 6:30 PM | App State @ Georgia Southern | App State 31, Georgia Southern 28 | App State 51% | App State -105 / Georgia Southern +105 | 29.1 – 28.2 | 14–44 / 14–42 | App State -0.9 / – | 57.3 / – | no line yet | no line yet (fair: App State -105) | no line yet |  |
| Sat 10/31 7:00 PM | Oklahoma State @ Iowa State | Oklahoma State 24, Iowa State 31 | Iowa State 66% | Oklahoma State +190 / Iowa State -190 | 24.1 – 30.0 | 10–38 / 16–45 | Iowa State -6.0 / – | 54.1 / – | no line yet | no line yet (fair: Iowa State -190) | no line yet |  |
| Sat 10/31 7:00 PM | Clemson @ Florida State | Clemson 27, Florida State 24 | Clemson 53% | Clemson -115 / Florida State +115 | 26.3 – 25.3 | 13–41 / 13–38 | Florida State -3.9 / Clemson -1.5 | 52.0 / 51.5 | no edge | no edge | no edge |  |
| Sat 10/31 7:00 PM | Washington State @ San Diego State | Washington State 21, San Diego State 24 | San Diego State 58% | Washington State +135 / San Diego State -135 | 21.2 – 23.5 | 8–34 / 10–38 | San Diego State -2.4 / – | 44.7 / – | no line yet | no line yet (fair: San Diego State -135) | no line yet |  |
| Sat 10/31 7:30 PM | Mississippi State @ Texas | Mississippi State 21, Texas 31 | Texas 77% | Mississippi State +340 / Texas -340 | 20.4 – 31.3 | 7–34 / 17–46 | Texas -10.9 / – | 51.8 / – | no line yet | no line yet (fair: Texas -340) | no line yet |  |
| Sat 10/31 7:30 PM | Georgia Tech @ Pittsburgh | Georgia Tech 24, Pittsburgh 31 | Pittsburgh 75% | Georgia Tech +295 / Pittsburgh -295 | 22.4 – 32.3 | 10–35 / 17–48 | Pittsburgh -9.9 / – | 54.7 / – | no line yet | no line yet (fair: Pittsburgh -295) | no line yet |  |
| Sat 10/31 7:30 PM | Miami @ North Carolina | Miami 34, North Carolina 17 | Miami 85% | Miami -560 / North Carolina +560 | 33.1 – 18.1 | 17–48 / 7–31 | Miami -20.1 / Miami -14.5 | 54.1 / 50.5 | no edge | no edge | no edge |  |
| Sat 10/31 7:30 PM | Ohio State @ USC | Ohio State 31, USC 24 | Ohio State 67% | Ohio State -205 / USC +205 | 30.5 – 23.7 | 16–45 / 10–37 | Ohio State -10.1 / Ohio State -6.5 | 56.8 / 53.5 | no edge | no edge | no edge |  |
| Sat 10/31 7:45 PM | Missouri @ Arkansas | Missouri 31, Arkansas 17 | Missouri 81% | Missouri -425 / Arkansas +425 | 29.8 – 17.0 | 15–45 / 6–29 | Missouri -12.8 / – | 49.2 / – | no line yet | no line yet (fair: Missouri -425) | no line yet |  |
| Sat 10/31 8:00 PM | Washington @ Nebraska | Washington 20, Nebraska 27 | Nebraska 73% | Washington +270 / Nebraska -270 | 19.4 – 28.3 | 7–32 / 14–43 | Nebraska -8.8 / – | 48.7 / – | no line yet | no line yet (fair: Nebraska -270) | no line yet |  |
| Sat 10/31 8:00 PM | Army @ Memphis | Army 24, Memphis 31 | Memphis 65% | Army +185 / Memphis -185 | 27.4 – 33.1 | 14–42 / 18–48 | Memphis -5.7 / – | 60.5 / – | no line yet | no line yet (fair: Memphis -185) | no line yet |  |
| Sat 10/31 10:00 PM | Texas State @ Boise State | Texas State 31, Boise State 38 | Boise State 72% | Texas State +250 / Boise State -250 | 28.1 – 36.8 | 14–42 / 21–52 | Boise State -8.7 / – | 65.0 / – | no line yet | no line yet (fair: Boise State -250) | no line yet |  |
| Sat 10/31 10:30 PM | Northern Illinois @ UNLV | Northern Illinois 17, UNLV 35 | UNLV 88% | Northern Illinois +730 / UNLV -730 | 18.2 – 35.6 | 7–31 / 20–51 | UNLV -17.4 / – | 53.7 / – | no line yet | no line yet (fair: UNLV -730) | no line yet |  |
| Sat 10/31 11:00 PM | Oregon State @ Fresno State | Oregon State 31, Fresno State 28 | Oregon State 60% | Oregon State -155 / Fresno State +155 | 30.2 – 26.4 | 16–45 / 13–41 | Oregon State -3.8 / – | 56.5 / – | no line yet | no line yet (fair: Oregon State -155) | no line yet |  |

## How the 2026 predictions have done

| Predictor | Games | Margin MAE | Total MAE | Team-score MAE | Winners | Brier | 80% range hit |
|---|---|---|---|---|---|---|---|
| Final prediction | 542 | 11.61 | 12.21 | 8.42 | 81.0% | 0.133 | 82.5% |
| Model only (before blending) | 542 | 12.36 | 12.51 | 8.69 | 78.8% | – | – |
| Betting line when predicted | 540 | 11.60 | 12.17 | 8.41 | 80.9% | – | – |

MAE is mean absolute error in points (lower is better). Brier scores the win chances (lower is better, 0.25 is a coin flip). Even the closing betting line misses the final margin of an FBS game by about 12.5 points.

501 of these games were played before the predictor went live. They are backfilled walk-forward (each week predicted from earlier weeks only) but with closing lines, so they flatter the model slightly. Every game since is graded on the prediction logged before kickoff.

### Betting edges

| Market | Edges | Record (W-L-P) | Staked | Units won | ROI | Expected ROI |
|---|---|---|---|---|---|---|
| Spread | 0 | 0-0-0 | 0.0 | +0.00 | – | – |
| Moneyline | 1 | 0-1-0 | 0.4 | -0.45 | -100.0% | +6.9% |
| Total | 0 | 0-0-0 | 0.0 | +0.00 | – | – |

Every edge logged before kickoff at the stake and price logged with it (backfilled games, and edges logged before edges were priced from the final prediction, are not included). Units are 1% of the bankroll; ROI is units won per unit staked, pushes returning the stake, and expected ROI is what the edges' EVs promised.

### Week 8 results

| Game | Predicted | Final | Win chance for winner | Inside 80% ranges |
|---|---|---|---|---|
| Middle Tennessee @ Florida International | 17–24 | 26–23 | 25% | yes |
| Missouri State @ Delaware | 24–27 | 38–61 | 58% | no |
| South Alabama @ Marshall | 34–31 | 13–20 | 45% | no |
| New Mexico State @ Sam Houston | 24–21 | 30–24 | 58% | yes |
| James Madison @ App State | 34–24 | 31–34 | 21% | yes |
| Liberty @ Kennesaw State | 31–24 | 34–6 | 73% | no |
| East Carolina @ Memphis | 24–31 | 34–41 | 75% | yes |
| Duke @ Virginia | 21–24 | 19–16 | 45% | yes |
| Massachusetts @ UConn | 17–34 | 16–35 | 82% | yes |
| Army @ Tulsa | 24–27 | 38–35 | 45% | yes |
| Air Force @ Wyoming | 27–20 | 14–28 | 33% | yes |
| NC State @ Stanford | 31–24 | 28–31 | 30% | yes |
| LSU @ Auburn | 31–24 | 38–17 | 69% | yes |
| Texas Tech @ Cincinnati | 34–24 | 24–37 | 22% | no |
| West Virginia @ TCU | 24–34 | 24–20 | 25% | yes |
| California @ SMU | 17–38 | 20–59 | 90% | no |
| Pittsburgh @ Miami | 14–35 | 23–52 | 92% | no |
| Indiana @ Michigan | 24–17 | 13–6 | 70% | no |
| Rutgers @ Northwestern | 21–38 | 14–42 | 85% | yes |
| Rice @ Florida Atlantic | 24–31 | 49–51 | 73% | no |
| Western Michigan @ Toledo | 24–27 | 38–45 | 59% | no |
| Baylor @ Kansas | 24–27 | 24–25 | 54% | yes |
| Akron @ Kent State | 21–24 | 20–35 | 58% | yes |
| Miami (OH) @ Central Michigan | 20–17 | 28–27 | 60% | yes |
| Oregon @ Illinois | 31–21 | 10–21 | 24% | no |
| Oklahoma @ Mississippi State | 24–21 | 23–15 | 55% | yes |
| Boston College @ Georgia Tech | 24–31 | 49–27 | 32% | no |
| Iowa @ Minnesota | 24–17 | 10–13 | 29% | yes |
| North Texas @ Navy | 31–28 | 49–39 | 58% | no |
| Hawai'i @ Northern Illinois | 27–24 | 56–21 | 58% | no |
| Sacramento State @ Ball State | 17–31 | 17–34 | 82% | yes |
| Bowling Green @ Buffalo | 21–24 | 24–31 | 59% | yes |

## FBS power ratings

Points per game better than an average FBS team on a neutral field, from opponent-adjusted EPA (garbage time removed) with this season's games weighted against a preseason prior, plus the weight the margin model puts on Elo (a rating built from game results alone). Defense is positive when it holds opponents below average.

| # | Team | Conference | Net | Offense | Defense | Special teams | Results (Elo) | Elo rating |
|---|---|---|---|---|---|---|---|---|
| 1 | Ohio State | Big Ten | +26.9 | +10.8 | +10.5 | +0.4 | +5.2 | 1934 |
| 2 | LSU | SEC | +26.3 | +10.4 | +12.8 | +0.2 | +3.0 | 1751 |
| 3 | Miami | ACC | +24.4 | +12.9 | +6.6 | +0.2 | +4.6 | 1890 |
| 4 | Notre Dame | FBS Independents | +24.1 | +8.5 | +10.2 | +1.2 | +4.2 | 1849 |
| 5 | Georgia | SEC | +23.3 | +9.4 | +8.6 | +0.9 | +4.4 | 1866 |
| 6 | Indiana | Big Ten | +22.2 | +6.1 | +10.5 | +0.5 | +5.2 | 1935 |
| 7 | Ole Miss | SEC | +19.2 | +11.0 | +3.5 | +0.7 | +4.0 | 1834 |
| 8 | Alabama | SEC | +18.9 | +8.2 | +7.3 | +0.3 | +3.1 | 1760 |
| 9 | Texas | SEC | +18.0 | +3.5 | +10.9 | +0.5 | +3.2 | 1770 |
| 10 | Utah | Big 12 | +17.8 | +8.6 | +5.4 | +0.2 | +3.6 | 1801 |
| 11 | Texas Tech | Big 12 | +17.5 | +1.2 | +12.5 | +1.0 | +2.7 | 1733 |
| 12 | Oklahoma | SEC | +17.3 | +1.1 | +13.6 | +0.6 | +2.1 | 1677 |
| 13 | Tennessee | SEC | +16.0 | +3.2 | +9.1 | +0.7 | +3.0 | 1753 |
| 14 | UCLA | Big Ten | +15.9 | +6.3 | +7.2 | +0.6 | +1.8 | 1657 |
| 15 | Oregon | Big Ten | +15.7 | +2.9 | +9.9 | +0.4 | +2.6 | 1722 |
| 16 | BYU | Big 12 | +15.5 | +6.0 | +5.4 | +0.4 | +3.7 | 1814 |
| 17 | Missouri | SEC | +15.3 | +3.9 | +8.8 | +0.5 | +2.2 | 1686 |
| 18 | Louisville | ACC | +15.0 | +8.6 | +4.2 | +0.3 | +1.9 | 1663 |
| 19 | Wake Forest | ACC | +14.9 | +5.5 | +7.0 | +0.1 | +2.2 | 1688 |
| 20 | USC | Big Ten | +14.6 | +12.1 | -0.6 | +0.3 | +2.7 | 1734 |
| 21 | Michigan | Big Ten | +14.4 | +2.4 | +9.9 | +0.2 | +1.9 | 1661 |
| 22 | Nebraska | Big Ten | +14.0 | +4.7 | +7.4 | +0.6 | +1.4 | 1622 |
| 23 | Florida | SEC | +13.8 | +8.7 | +3.2 | +1.0 | +1.0 | 1592 |
| 24 | SMU | ACC | +13.1 | +6.7 | +3.9 | -0.0 | +2.5 | 1716 |
| 25 | Kansas State | Big 12 | +12.4 | +7.9 | +3.2 | +0.3 | +1.1 | 1599 |
| 26 | Texas A&M | SEC | +12.3 | +2.2 | +8.2 | +0.5 | +1.3 | 1618 |
| 27 | Auburn | SEC | +12.2 | +4.7 | +6.3 | +0.7 | +0.5 | 1550 |
| 28 | Iowa | Big Ten | +12.0 | +2.2 | +6.2 | +1.0 | +2.6 | 1723 |
| 29 | Northwestern | Big Ten | +11.9 | +6.1 | +3.0 | +1.0 | +1.8 | 1655 |
| 30 | Arizona | Big 12 | +11.5 | +5.4 | +3.7 | -0.0 | +2.5 | 1710 |
| 31 | Houston | Big 12 | +11.0 | +8.6 | +0.2 | +0.0 | +2.2 | 1690 |
| 32 | Penn State | Big Ten | +10.8 | +2.6 | +6.7 | +0.4 | +1.0 | 1593 |
| 33 | Mississippi State | SEC | +9.6 | +6.6 | +2.5 | +0.4 | +0.2 | 1523 |
| 34 | Wisconsin | Big Ten | +8.4 | +0.8 | +6.8 | +0.2 | +0.6 | 1559 |
| 35 | Kansas | Big 12 | +8.3 | +5.4 | +3.5 | +0.0 | -0.7 | 1454 |
| 36 | Kentucky | SEC | +8.3 | +1.8 | +4.6 | +0.2 | +1.8 | 1653 |
| 37 | Washington | Big Ten | +8.2 | +2.3 | +4.4 | -0.0 | +1.5 | 1635 |
| 38 | Cincinnati | Big 12 | +8.1 | +8.8 | -2.1 | +0.5 | +1.0 | 1592 |
| 39 | Iowa State | Big 12 | +7.9 | +2.9 | +3.2 | +0.9 | +0.8 | 1578 |
| 40 | South Carolina | SEC | +7.9 | +3.7 | +2.6 | +0.8 | +0.7 | 1569 |
| 41 | Florida State | ACC | +6.2 | +7.9 | -1.4 | -0.1 | -0.1 | 1497 |
| 42 | Baylor | Big 12 | +6.1 | -1.6 | +6.0 | +1.2 | +0.5 | 1546 |
| 43 | Boise State | Pac-12 | +5.4 | +4.0 | -1.1 | +0.2 | +2.4 | 1702 |
| 44 | Vanderbilt | SEC | +5.3 | +4.0 | +0.4 | +0.4 | +0.5 | 1553 |
| 45 | Duke | ACC | +5.1 | +2.0 | +0.6 | +0.7 | +1.8 | 1653 |
| 46 | Oklahoma State | Big 12 | +4.9 | +5.1 | -0.2 | +0.4 | -0.5 | 1464 |
| 47 | TCU | Big 12 | +4.9 | -1.7 | +5.4 | +0.4 | +0.8 | 1572 |
| 48 | Virginia Tech | ACC | +4.4 | +3.4 | +0.4 | +0.3 | +0.3 | 1531 |
| 49 | Clemson | ACC | +4.2 | -4.2 | +6.7 | +0.4 | +1.3 | 1613 |
| 50 | North Texas | American Athletic | +4.2 | +9.9 | -6.6 | -0.7 | +1.5 | 1634 |
| 51 | UCF | Big 12 | +4.1 | +0.8 | +4.1 | +0.0 | -0.7 | 1448 |
| 52 | James Madison | Sun Belt | +3.8 | -0.2 | +0.7 | +0.4 | +2.9 | 1747 |
| 53 | Minnesota | Big Ten | +3.6 | -2.4 | +4.9 | +0.5 | +0.7 | 1565 |
| 54 | Illinois | Big Ten | +3.6 | +5.4 | -3.2 | +0.3 | +1.1 | 1601 |
| 55 | Arizona State | Big 12 | +3.5 | +1.1 | +1.9 | +0.3 | +0.2 | 1521 |
| 56 | Colorado | Big 12 | +3.2 | -0.4 | +5.9 | -0.7 | -1.6 | 1377 |
| 57 | Pittsburgh | ACC | +3.1 | -0.5 | +2.6 | +0.6 | +0.4 | 1542 |
| 58 | NC State | ACC | +3.0 | +7.2 | -3.7 | -0.6 | +0.1 | 1515 |
| 59 | Oregon State | Pac-12 | +2.9 | +5.3 | -2.3 | +0.0 | -0.1 | 1498 |
| 60 | Virginia | ACC | +2.3 | -1.2 | +3.5 | -0.2 | +0.1 | 1517 |
| 61 | North Carolina | ACC | +1.5 | +0.8 | -0.3 | +0.6 | +0.3 | 1532 |
| 62 | Maryland | Big Ten | +1.2 | -0.7 | +3.4 | +0.6 | -2.0 | 1343 |
| 63 | Syracuse | ACC | +1.2 | +0.9 | +2.6 | -0.3 | -2.0 | 1347 |
| 64 | Memphis | American Athletic | +1.2 | +3.0 | -2.0 | -0.5 | +0.7 | 1566 |
| 65 | Purdue | Big Ten | +1.1 | +3.1 | -1.8 | +0.5 | -0.8 | 1444 |
| 66 | UTSA | American Athletic | +1.1 | +2.6 | -3.0 | -0.2 | +1.6 | 1636 |
| 67 | Arkansas | SEC | +0.9 | +1.0 | +0.4 | -0.4 | -0.2 | 1496 |
| 68 | Texas State | Pac-12 | +0.8 | +7.3 | -5.6 | -1.5 | +0.6 | 1559 |
| 69 | Toledo | Mid-American | +0.3 | -1.3 | +0.8 | +0.3 | +0.6 | 1555 |
| 70 | West Virginia | Big 12 | +0.0 | +4.0 | -4.6 | +0.6 | -0.1 | 1502 |
| 71 | New Mexico | Mountain West | -0.2 | -2.1 | +0.7 | +0.1 | +1.1 | 1598 |
| 72 | Liberty | Conference USA | -1.0 | -0.5 | -0.7 | -0.1 | +0.2 | 1527 |
| 73 | North Dakota State | Mountain West | -1.3 | -4.8 | +3.4 | +1.1 | -1.1 | 1419 |
| 74 | South Florida | American Athletic | -1.6 | -1.4 | -0.9 | -0.1 | +0.8 | 1572 |
| 75 | UConn | FBS Independents | -2.3 | +1.3 | -3.3 | -0.3 | -0.0 | 1507 |
| 76 | Army | American Athletic | -2.4 | +4.7 | -8.0 | -0.2 | +1.1 | 1602 |
| 77 | Navy | American Athletic | -2.5 | +2.1 | -3.5 | -0.7 | -0.3 | 1481 |
| 78 | Michigan State | Big Ten | -2.8 | -2.2 | +0.5 | +0.2 | -1.3 | 1399 |
| 79 | Ohio | Mid-American | -3.1 | -0.7 | -3.7 | +0.6 | +0.8 | 1571 |
| 80 | Fresno State | Pac-12 | -3.2 | -2.5 | -1.1 | -0.0 | +0.4 | 1544 |
| 81 | Tulane | American Athletic | -3.4 | -4.6 | -0.0 | +0.0 | +1.2 | 1604 |
| 82 | Boston College | ACC | -3.4 | -3.0 | +0.5 | -0.8 | -0.2 | 1493 |
| 83 | East Carolina | American Athletic | -3.5 | -5.1 | +2.5 | -0.6 | -0.3 | 1484 |
| 84 | Tulsa | American Athletic | -3.7 | -1.0 | -0.4 | -0.4 | -1.8 | 1358 |
| 85 | Georgia Tech | ACC | -3.8 | +2.5 | -5.2 | -0.0 | -1.1 | 1416 |
| 86 | Rutgers | Big Ten | -4.0 | +2.2 | -5.5 | +0.7 | -1.3 | 1402 |
| 87 | Florida Atlantic | American Athletic | -4.4 | +3.3 | -7.2 | +0.5 | -1.0 | 1426 |
| 88 | Air Force | Mountain West | -4.8 | +2.4 | -6.2 | -0.3 | -0.7 | 1453 |
| 89 | UNLV | Mountain West | -4.8 | -3.1 | -2.0 | +0.0 | +0.4 | 1540 |
| 90 | Louisiana Tech | Sun Belt | -5.3 | -3.7 | -0.3 | -0.8 | -0.5 | 1464 |
| 91 | California | ACC | -5.6 | -0.7 | -3.0 | -0.5 | -1.4 | 1392 |
| 92 | Jacksonville State | Conference USA | -6.1 | -0.7 | -4.6 | -0.4 | -0.5 | 1465 |
| 93 | Marshall | Sun Belt | -6.6 | -2.3 | -3.6 | -0.2 | -0.6 | 1462 |
| 94 | Washington State | Pac-12 | -6.8 | -6.3 | +1.4 | -0.4 | -1.5 | 1388 |
| 95 | Western Michigan | Mid-American | -7.1 | -4.2 | -3.9 | +0.5 | +0.5 | 1552 |
| 96 | App State | Sun Belt | -7.1 | -3.0 | -3.3 | -0.2 | -0.7 | 1454 |
| 97 | San Diego State | Pac-12 | -7.7 | -7.5 | +0.2 | +0.5 | -1.0 | 1425 |
| 98 | Georgia State | Sun Belt | -7.7 | +0.2 | -6.8 | -0.1 | -1.0 | 1424 |
| 99 | Miami (OH) | Mid-American | -8.1 | -4.6 | -3.3 | +0.5 | -0.8 | 1446 |
| 100 | Louisiana | Sun Belt | -8.4 | -4.5 | -4.1 | +0.0 | +0.1 | 1520 |
| 101 | Delaware | Conference USA | -8.6 | -1.7 | -5.2 | +0.2 | -1.9 | 1352 |
| 102 | Stanford | ACC | -8.9 | -3.6 | -4.6 | -0.2 | -0.5 | 1465 |
| 103 | UAB | American Athletic | -9.4 | -5.0 | -3.3 | -0.0 | -1.0 | 1427 |
| 104 | Temple | American Athletic | -9.5 | +1.0 | -7.5 | -0.5 | -2.5 | 1303 |
| 105 | Georgia Southern | Sun Belt | -9.6 | -2.3 | -6.0 | -1.0 | -0.3 | 1481 |
| 106 | Utah State | Pac-12 | -10.2 | -8.2 | +0.7 | -1.3 | -1.4 | 1393 |
| 107 | Western Kentucky | Conference USA | -10.4 | -7.0 | -1.8 | -0.2 | -1.3 | 1399 |
| 108 | Troy | Sun Belt | -10.4 | -5.9 | -2.2 | -1.2 | -1.1 | 1416 |
| 109 | Wyoming | Mountain West | -11.0 | -6.4 | -3.2 | -0.2 | -1.2 | 1413 |
| 110 | Arkansas State | Sun Belt | -11.2 | -3.6 | -6.5 | -0.0 | -1.1 | 1416 |
| 111 | South Alabama | Sun Belt | -11.3 | +0.1 | -10.8 | +0.1 | -0.9 | 1438 |
| 112 | Hawai'i | Mountain West | -11.4 | -4.4 | -5.9 | +0.7 | -1.7 | 1365 |
| 113 | Colorado State | Pac-12 | -11.7 | +1.1 | -9.4 | -0.6 | -2.9 | 1271 |
| 114 | Old Dominion | Sun Belt | -12.3 | -12.8 | +2.7 | -1.2 | -0.9 | 1431 |
| 115 | Rice | American Athletic | -13.0 | -3.8 | -5.0 | -0.9 | -3.2 | 1246 |
| 116 | Florida International | Conference USA | -13.0 | -9.7 | -1.0 | -0.7 | -1.6 | 1377 |
| 117 | Coastal Carolina | Sun Belt | -13.4 | -5.9 | -5.8 | +0.4 | -2.2 | 1332 |
| 118 | Nevada | Mountain West | -13.7 | -8.4 | -3.1 | +0.4 | -2.6 | 1292 |
| 119 | Missouri State | Conference USA | -14.0 | -1.6 | -7.8 | -1.4 | -3.1 | 1253 |
| 120 | Central Michigan | Mid-American | -14.0 | -7.6 | -4.6 | -0.2 | -1.6 | 1375 |
| 121 | New Mexico State | Conference USA | -14.2 | -7.8 | -2.5 | -1.4 | -2.5 | 1307 |
| 122 | San José State | Mountain West | -14.2 | -7.8 | -4.3 | -0.3 | -1.9 | 1356 |
| 123 | Kennesaw State | Conference USA | -14.9 | -6.8 | -4.7 | -0.8 | -2.6 | 1295 |
| 124 | Middle Tennessee | Conference USA | -15.1 | -5.7 | -7.0 | +0.1 | -2.4 | 1309 |
| 125 | Southern Miss | Sun Belt | -15.4 | -6.6 | -4.1 | -1.5 | -3.1 | 1254 |
| 126 | Ball State | Mid-American | -16.8 | -5.8 | -7.0 | -1.0 | -3.1 | 1251 |
| 127 | Eastern Michigan | Mid-American | -17.1 | -6.8 | -7.5 | -0.8 | -2.1 | 1337 |
| 128 | Massachusetts | Mid-American | -17.4 | -9.5 | -4.2 | -0.2 | -3.5 | 1219 |
| 129 | Sam Houston | Conference USA | -17.9 | -11.6 | -0.9 | -1.3 | -4.1 | 1173 |
| 130 | Buffalo | Mid-American | -18.0 | -12.7 | -5.1 | +0.6 | -0.8 | 1444 |
| 131 | Northern Illinois | Mountain West | -18.8 | -4.6 | -8.9 | -0.9 | -4.4 | 1149 |
| 132 | Kent State | Mid-American | -19.0 | -9.2 | -6.5 | -1.0 | -2.3 | 1318 |
| 133 | Bowling Green | Mid-American | -19.0 | -11.6 | -4.5 | -0.1 | -2.8 | 1279 |
| 134 | UL Monroe | Sun Belt | -20.6 | -6.5 | -8.1 | -1.5 | -4.5 | 1139 |
| 135 | Charlotte | American Athletic | -20.9 | -8.7 | -8.2 | -0.4 | -3.6 | 1211 |
| 136 | Sacramento State | Mid-American | -22.2 | -10.3 | -6.8 | +0.2 | -5.3 | 1074 |
| 137 | Akron | Mid-American | -22.8 | -10.1 | -7.8 | -1.2 | -3.7 | 1205 |
| 138 | UTEP | Mountain West | -24.1 | -11.9 | -6.1 | -1.4 | -4.7 | 1123 |

## Current model fit

- Fitted on 4159 games from seasons 2022–2026.
- Home field on top of the ratings: 3.2 points (1.8 in conference games).
- Extra FBS edge over FCS opponents beyond their ratings: 14.0 points.
- Elo weight: 0.20 points of margin per point of Elo spread.
- Weight on the betting line: 91% for the margin, 80% for the total.
