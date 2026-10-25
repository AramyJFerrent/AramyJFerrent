# College football score predictions

Updated Sun Oct 25, 2026 02:53 AM ET. Refreshed automatically every day of the season and several times on Saturdays; each game's prediction is locked at kickoff and graded once the final score is in. Scores are the most likely real scoreline near the expected points; ranges cover 80% of simulated outcomes for each team. College scores scatter widely, so read the ranges, not just the headline score.

Expected points blend the model with the betting line using the weight that has predicted best in recent seasons (see Current model fit). The spread and total columns show the model's own numbers next to the line, so you can see where it disagrees. Games without a line yet use the model alone.

The fair moneyline is the American odds that match the win chance exactly, with no bookmaker margin: -200 means risk $200 to win $100, +200 means risk $100 to win $200. A sportsbook's price will be a little worse on both sides because of its cut, so a book only offers value on a team when its price beats the fair line.

The edge columns judge each bet by its expected value per $1 staked at the posted price, using the final prediction: the model blended with the line, run through the score simulator, pushes included, and anchored to the market's own chances so that only what the blend moves off the line counts. The model's own spread and total (shown alongside) sit several points from the line in most games, but the blend keeps only the share of that disagreement the model has earned in past seasons, so edges are rare. The side with the higher value is shown when it reaches 3% (+3 cents per $1), as the team or side, the price, the expected value, its chance of winning the bet and its stake, a 25% share of the Kelly stake in units of 1% of the bankroll with at most 3 units on one game; anything short is no edge. Where a book posts no price for a spread or total it is assumed to be -110 and marked -110*; moneylines are never assumed. In the walk-forward backtest against closing lines, edges returned spread -100.0% on 1 bets (posted prices, 2016–2019); spread -3.9% on 156 bets (assumed -110 prices, 2016–2025); moneyline +13.7% on 575 bets (posted prices, 2016–2025); total +2.6% on 367 bets (posted prices, 2016–2019); total -5.7% on 172 bets (assumed -110 prices, 2016–2025). None of these is clearly above zero, so treat these edges as an experiment, not a betting system. The live record is tracked below, graded at the price logged with the last prediction before kickoff.

## 2026 Week 9

| Kickoff (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected points | 80% range | Spread: model / line | Total: model / line | Spread edge | Moneyline edge | Total edge | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tue 10/27 7:00 PM | Delaware @ Western Kentucky | Delaware 31, Western Kentucky 28 | Delaware 56% | Delaware -130 / Western Kentucky +130 | 30.0 – 27.7 | 16–45 / 14–42 | Western Kentucky -0.3 / Delaware -2.5 | 54.6 / 58.5 | no edge | no edge | no edge |  |
| Tue 10/27 8:00 PM | Sam Houston @ Missouri State | Sam Houston 24, Missouri State 31 | Missouri State 67% | Sam Houston +200 / Missouri State -200 | 22.3 – 28.8 | 10–36 / 14–44 | Missouri State -6.3 / Missouri State -6.5 | 49.2 / 51.5 | no edge | no edge | no edge |  |
| Wed 10/28 7:00 PM | Kennesaw State @ Middle Tennessee | Kennesaw State 24, Middle Tennessee 27 | Middle Tennessee 57% | Kennesaw State +130 / Middle Tennessee -130 | 23.2 – 25.7 | 10–37 / 13–41 | Middle Tennessee -3.2 / Middle Tennessee -2.5 | 50.5 / 48.5 | no edge | no edge | no edge |  |
| Wed 10/28 8:00 PM | Jacksonville State @ New Mexico State | Jacksonville State 27, New Mexico State 24 | Jacksonville State 59% | Jacksonville State -145 / New Mexico State +145 | 27.0 – 23.6 | 13–41 / 10–38 | Jacksonville State -6.7 / Jacksonville State -3.0 | 50.9 / 50.5 | no edge | no edge | no edge |  |
| Thu 10/29 7:30 PM | Florida Atlantic @ North Texas | Florida Atlantic 28, North Texas 41 | North Texas 78% | Florida Atlantic +365 / North Texas -365 | 28.8 – 41.0 | 14–44 / 26–57 | North Texas -9.8 / North Texas -12.5 | 71.2 / 69.5 | no edge | no edge | no edge |  |
| Thu 10/29 7:30 PM | Troy @ James Madison | Troy 17, James Madison 34 | James Madison 88% | Troy +765 / James Madison -765 | 17.4 – 34.9 | 6–30 / 20–51 | James Madison -18.2 / James Madison -17.5 | 51.6 / 52.5 | no edge | no edge | no edge |  |
| Fri 10/30 7:00 PM | Tulane @ Charlotte | Tulane 31, Charlotte 17 | Tulane 83% | Tulane -480 / Charlotte +480 | 29.8 – 16.1 | 16–45 / 6–28 | Tulane -15.5 / Tulane -13.5 | 47.8 / 45.5 | no edge | no edge | no edge |  |
| Fri 10/30 7:30 PM | Baylor @ UCF | Baylor 21, UCF 24 | UCF 56% | Baylor +130 / UCF -130 | 23.4 – 25.6 | 10–37 / 13–41 | Baylor -0.7 / UCF -2.5 | 51.2 / 48.5 | no edge | no edge | no edge |  |
| Fri 10/30 10:30 PM | Kent State @ Sacramento State | Kent State 27, Sacramento State 20 | Kent State 74% | Kent State -285 / Sacramento State +285 | 27.9 – 18.9 | 14–42 / 7–31 | Sacramento State -0.5 / Kent State -10.0 | 48.0 / 46.5 | no edge | Sacramento State (+300): EV +3.5%, 26%, stake 0.3u | no edge |  |
| Sat 10/31 TBA | Northwestern @ Oregon | Northwestern 24, Oregon 27 | Oregon 62% | Northwestern +165 / Oregon -165 | 23.3 – 27.9 | 10–37 / 14–42 | Oregon -5.6 / Oregon -4.5 | 50.5 / 51.5 | no edge | no edge | no edge |  |
| Sat 10/31 TBA | Purdue @ Penn State | Purdue 17, Penn State 31 | Penn State 80% | Purdue +410 / Penn State -410 | 19.2 – 31.3 | 7–31 / 17–46 | Penn State -12.1 / – | 50.6 / – | no line yet | no line yet (fair: Penn State -410) | no line yet |  |
| Sat 10/31 12:00 PM | Arizona @ Texas Tech | Arizona 24, Texas Tech 27 | Texas Tech 63% | Arizona +170 / Texas Tech -170 | 24.6 – 29.5 | 10–38 / 15–44 | Texas Tech -9.5 / Texas Tech -4.5 | 48.9 / 55.5 | no edge | no edge | no edge |  |
| Sat 10/31 12:00 PM | California @ NC State | California 24, NC State 34 | NC State 75% | California +305 / NC State -305 | 24.7 – 35.6 | 12–38 / 20–51 | NC State -10.9 / – | 60.3 / – | no line yet | no line yet (fair: NC State -305) | no line yet |  |
| Sat 10/31 12:00 PM | SMU @ Syracuse | SMU 31, Syracuse 24 | SMU 74% | SMU -280 / Syracuse +280 | 32.8 – 23.3 | 17–48 / 10–37 | SMU -9.8 / SMU -9.5 | 54.6 / 56.5 | no edge | no edge | no edge |  |
| Sat 10/31 12:00 PM | Boston College @ Duke | Boston College 17, Duke 31 | Duke 80% | Boston College +400 / Duke -400 | 18.9 – 31.4 | 7–31 / 17–46 | Duke -12.5 / – | 50.3 / – | no line yet | no line yet (fair: Duke -400) | no line yet |  |
| Sat 10/31 12:00 PM | Wisconsin @ Iowa | Wisconsin 17, Iowa 20 | Iowa 61% | Wisconsin +155 / Iowa -155 | 18.2 – 22.0 | 7–31 / 10–35 | Iowa -6.8 / Iowa -3.5 | 43.4 / 39.5 | no edge | no edge | no edge |  |
| Sat 10/31 12:00 PM | Illinois @ Maryland | Illinois 24, Maryland 27 | Maryland 51% | Illinois +105 / Maryland -105 | 27.0 – 27.3 | 14–41 / 14–42 | Maryland -0.3 / – | 54.3 / – | no line yet | no line yet (fair: Maryland -105) | no line yet |  |
| Sat 10/31 12:00 PM | Notre Dame vs Navy | Notre Dame 41, Navy 10 | Notre Dame 99% | Notre Dame -7440 / Navy +7440 | 41.2 – 10.9 | 27–58 / 0–21 | Notre Dame -28.5 / Notre Dame -30.5 | 50.8 / 52.5 | no edge | no edge | no edge | neutral site |
| Sat 10/31 12:00 PM | UAB @ South Florida | UAB 17, South Florida 27 | South Florida 76% | UAB +310 / South Florida -310 | 19.0 – 29.1 | 7–31 / 14–44 | South Florida -10.1 / – | 50.4 / – | no line yet | no line yet (fair: South Florida -310) | no line yet |  |
| Sat 10/31 12:00 PM | Bowling Green @ Western Michigan | Bowling Green 14, Western Michigan 28 | Western Michigan 86% | Bowling Green +590 / Western Michigan -590 | 14.7 – 29.7 | 3–27 / 15–45 | Western Michigan -15.0 / – | 44.4 / – | no line yet | no line yet (fair: Western Michigan -590) | no line yet |  |
| Sat 10/31 12:30 PM | Michigan @ Rutgers | Michigan 31, Rutgers 17 | Michigan 83% | Michigan -500 / Rutgers +500 | 31.0 – 16.9 | 17–46 / 6–30 | Michigan -15.5 / Michigan -14.0 | 49.6 / 47.5 | no edge | no edge | no edge |  |
| Sat 10/31 12:45 PM | Auburn @ Ole Miss | Auburn 24, Ole Miss 34 | Ole Miss 78% | Auburn +350 / Ole Miss -350 | 22.4 – 33.7 | 10–36 / 20–49 | Ole Miss -9.4 / Ole Miss -11.5 | 58.6 / 55.5 | no edge | no edge | no edge |  |
| Sat 10/31 1:00 PM | Marshall @ Old Dominion | Marshall 24, Old Dominion 21 | Marshall 61% | Marshall -160 / Old Dominion +160 | 25.6 – 21.4 | 13–40 / 9–35 | Marshall -4.2 / – | 47.0 / – | no line yet | no line yet (fair: Marshall -160) | no line yet |  |
| Sat 10/31 2:00 PM | Kansas State @ Colorado | Kansas State 28, Colorado 21 | Kansas State 69% | Kansas State -230 / Colorado +230 | 28.6 – 20.7 | 14–43 / 9–34 | Kansas State -7.8 / – | 52.2 / – | no line yet | no line yet (fair: Kansas State -230) | no line yet |  |
| Sat 10/31 2:00 PM | Coastal Carolina @ Georgia State | Coastal Carolina 24, Georgia State 31 | Georgia State 69% | Coastal Carolina +220 / Georgia State -220 | 24.6 – 32.1 | 10–38 / 17–48 | Georgia State -7.6 / – | 56.7 / – | no line yet | no line yet (fair: Georgia State -220) | no line yet |  |
| Sat 10/31 3:00 PM | UConn @ Air Force | UConn 28, Air Force 31 | Air Force 53% | UConn +115 / Air Force -115 | 28.8 – 30.1 | 14–44 / 16–45 | Air Force -1.4 / – | 58.9 / – | no line yet | no line yet (fair: Air Force -115) | no line yet |  |
| Sat 10/31 3:00 PM | Temple @ East Carolina | Temple 24, East Carolina 31 | East Carolina 72% | Temple +255 / East Carolina -255 | 22.0 – 30.4 | 10–35 / 17–45 | East Carolina -8.4 / – | 52.3 / – | no line yet | no line yet (fair: East Carolina -255) | no line yet |  |
| Sat 10/31 3:00 PM | Louisiana Tech @ South Alabama | Louisiana Tech 31, South Alabama 28 | Louisiana Tech 56% | Louisiana Tech -130 / South Alabama +130 | 29.8 – 27.2 | 16–45 / 14–42 | Louisiana Tech -2.6 / – | 57.1 / – | no line yet | no line yet (fair: Louisiana Tech -130) | no line yet |  |
| Sat 10/31 3:15 PM | Stanford @ Louisville | Stanford 14, Louisville 42 | Louisville 97% | Stanford +3050 / Louisville -3050 | 14.7 – 41.5 | 3–27 / 27–58 | Louisville -26.8 / – | 56.2 / – | no line yet | no line yet (fair: Louisville -3050) | no line yet |  |
| Sat 10/31 3:30 PM | Florida vs Georgia | Florida 24, Georgia 31 | Georgia 75% | Florida +295 / Georgia -295 | 22.7 – 33.1 | 10–37 / 17–48 | Georgia -9.3 / Georgia -10.5 | 53.2 / 56.5 | no edge | no edge | no edge | neutral site |
| Sat 10/31 3:30 PM | Arizona State @ BYU | Arizona State 17, BYU 31 | BYU 84% | Arizona State +545 / BYU -545 | 18.4 – 32.9 | 7–31 / 19–48 | BYU -14.6 / BYU -14.5 | 50.6 / 51.5 | no edge | no edge | no edge |  |
| Sat 10/31 3:30 PM | Kansas @ TCU | Kansas 24, TCU 21 | Kansas 51% | Kansas -105 / TCU +105 | 24.5 – 23.9 | 10–38 / 10–38 | Kansas -0.6 / – | 49.4 / – | no line yet | no line yet (fair: Kansas -105) | no line yet |  |
| Sat 10/31 3:30 PM | Minnesota @ Indiana | Minnesota 10, Indiana 31 | Indiana 94% | Minnesota +1475 / Indiana -1475 | 11.1 – 31.7 | 2–21 / 17–48 | Indiana -21.0 / Indiana -20.5 | 40.2 / 43.5 | no edge | no edge | no edge |  |
| Sat 10/31 3:30 PM | Colorado State @ Utah State | Colorado State 24, Utah State 27 | Utah State 59% | Colorado State +140 / Utah State -140 | 26.1 – 29.4 | 13–41 / 14–45 | Utah State -3.3 / – | 55.5 / – | no line yet | no line yet (fair: Utah State -140) | no line yet |  |
| Sat 10/31 3:30 PM | UTEP @ North Dakota State | UTEP 6, North Dakota State 34 | North Dakota State 99% | UTEP +7055 / North Dakota State -7055 | 7.1 – 34.8 | 0–15 / 20–51 | North Dakota State -27.7 / – | 41.9 / – | no line yet | no line yet (fair: North Dakota State -7055) | no line yet |  |
| Sat 10/31 3:30 PM | Florida International @ Liberty | Florida International 14, Liberty 31 | Liberty 85% | Florida International +590 / Liberty -590 | 15.8 – 30.9 | 6–28 / 16–45 | Liberty -15.1 / – | 46.6 / – | no line yet | no line yet (fair: Liberty -590) | no line yet |  |
| Sat 10/31 3:30 PM | Southern Miss @ UL Monroe | Southern Miss 27, UL Monroe 24 | Southern Miss 57% | Southern Miss -135 / UL Monroe +135 | 29.1 – 26.2 | 14–44 / 13–41 | Southern Miss -2.8 / – | 55.3 / – | no line yet | no line yet (fair: Southern Miss -135) | no line yet |  |
| Sat 10/31 3:45 PM | Utah @ Cincinnati | Utah 31, Cincinnati 24 | Utah 66% | Utah -195 / Cincinnati +195 | 31.5 – 25.0 | 17–47 / 11–38 | Utah -7.0 / Utah -6.5 | 60.8 / 55.5 | no edge | no edge | no edge |  |
| Sat 10/31 3:45 PM | Virginia @ Wake Forest | Virginia 17, Wake Forest 31 | Wake Forest 83% | Virginia +480 / Wake Forest -480 | 17.8 – 31.5 | 7–31 / 17–48 | Wake Forest -15.3 / Wake Forest -13.5 | 48.4 / 49.5 | no edge | no edge | no edge |  |
| Sat 10/31 4:00 PM | New Mexico @ San José State | New Mexico 31, San José State 17 | New Mexico 79% | New Mexico -380 / San José State +380 | 30.8 – 18.7 | 17–45 / 7–31 | New Mexico -12.0 / – | 49.5 / – | no line yet | no line yet (fair: New Mexico -380) | no line yet |  |
| Sat 10/31 4:15 PM | South Carolina @ Oklahoma | South Carolina 17, Oklahoma 24 | Oklahoma 67% | South Carolina +200 / Oklahoma -200 | 18.7 – 24.7 | 7–31 / 10–38 | Oklahoma -11.7 / Oklahoma -5.5 | 44.6 / 43.5 | no edge | no edge | no edge |  |
| Sat 10/31 4:15 PM | Nevada @ UCLA | Nevada 10, UCLA 34 | UCLA 96% | Nevada +2490 / UCLA -2490 | 12.0 – 36.4 | 3–23 / 21–52 | UCLA -33.6 / UCLA -23.5 | 48.0 / 48.5 | no edge | no edge | no edge |  |
| Sat 10/31 6:30 PM | App State @ Georgia Southern | App State 31, Georgia Southern 28 | App State 51% | App State -105 / Georgia Southern +105 | 29.1 – 28.2 | 14–44 / 14–42 | App State -0.9 / – | 57.3 / – | no line yet | no line yet (fair: App State -105) | no line yet |  |
| Sat 10/31 7:00 PM | Oklahoma State @ Iowa State | Oklahoma State 24, Iowa State 31 | Iowa State 65% | Oklahoma State +185 / Iowa State -185 | 23.9 – 29.8 | 10–38 / 16–45 | Iowa State -6.0 / – | 54.1 / – | no line yet | no line yet (fair: Iowa State -185) | no line yet |  |
| Sat 10/31 7:00 PM | Clemson @ Florida State | Clemson 24, Florida State 27 | Florida State 63% | Clemson +170 / Florida State -170 | 22.7 – 28.1 | 10–37 / 14–42 | Florida State -3.9 / Florida State -5.5 | 52.0 / 50.5 | no edge | no edge | no edge |  |
| Sat 10/31 7:00 PM | Washington State @ San Diego State | Washington State 21, San Diego State 24 | San Diego State 57% | Washington State +130 / San Diego State -130 | 21.2 – 23.5 | 9–34 / 10–37 | San Diego State -2.4 / – | 44.7 / – | no line yet | no line yet (fair: San Diego State -130) | no line yet |  |
| Sat 10/31 7:30 PM | Mississippi State @ Texas | Mississippi State 13, Texas 34 | Texas 92% | Mississippi State +1150 / Texas -1150 | 15.5 – 35.2 | 3–27 / 20–51 | Texas -10.9 / Texas -20.5 | 51.8 / 50.5 | no edge | no edge | no edge |  |
| Sat 10/31 7:30 PM | Georgia Tech @ Pittsburgh | Georgia Tech 24, Pittsburgh 31 | Pittsburgh 74% | Georgia Tech +290 / Pittsburgh -290 | 22.4 – 32.3 | 10–36 / 17–48 | Pittsburgh -9.9 / – | 54.7 / – | no line yet | no line yet (fair: Pittsburgh -290) | no line yet |  |
| Sat 10/31 7:30 PM | Miami @ North Carolina | Miami 34, North Carolina 17 | Miami 88% | Miami -720 / North Carolina +720 | 34.0 – 17.2 | 20–50 / 6–30 | Miami -20.1 / Miami -16.5 | 54.1 / 50.5 | no edge | no edge | no edge |  |
| Sat 10/31 7:30 PM | Ohio State @ USC | Ohio State 31, USC 24 | Ohio State 69% | Ohio State -220 / USC +220 | 30.3 – 23.0 | 16–45 / 10–37 | Ohio State -10.1 / Ohio State -7.0 | 56.8 / 52.5 | no edge | no edge | no edge |  |
| Sat 10/31 7:45 PM | Missouri @ Arkansas | Missouri 27, Arkansas 17 | Missouri 77% | Missouri -330 / Arkansas +330 | 29.2 – 18.5 | 15–44 / 7–31 | Missouri -12.8 / Missouri -10.5 | 49.2 / 47.5 | no edge | no edge | no edge |  |
| Sat 10/31 8:00 PM | Washington @ Nebraska | Washington 21, Nebraska 31 | Nebraska 73% | Washington +275 / Nebraska -275 | 19.9 – 29.4 | 7–34 / 14–44 | Nebraska -8.8 / Nebraska -9.5 | 48.7 / 49.5 | no edge | no edge | no edge |  |
| Sat 10/31 8:00 PM | Army @ Memphis | Army 28, Memphis 31 | Memphis 64% | Army +180 / Memphis -180 | 27.4 – 33.1 | 14–42 / 20–49 | Memphis -5.7 / – | 60.5 / – | no line yet | no line yet (fair: Memphis -180) | no line yet |  |
| Sat 10/31 10:00 PM | Texas State @ Boise State | Texas State 31, Boise State 38 | Boise State 71% | Texas State +250 / Boise State -250 | 28.1 – 36.8 | 14–42 / 21–52 | Boise State -8.7 / – | 65.0 / – | no line yet | no line yet (fair: Boise State -250) | no line yet |  |
| Sat 10/31 10:30 PM | Northern Illinois @ UNLV | Northern Illinois 17, UNLV 34 | UNLV 88% | Northern Illinois +765 / UNLV -765 | 18.2 – 35.6 | 7–31 / 21–52 | UNLV -17.4 / – | 53.7 / – | no line yet | no line yet (fair: UNLV -765) | no line yet |  |
| Sat 10/31 11:00 PM | Oregon State @ Fresno State | Oregon State 31, Fresno State 24 | Oregon State 67% | Oregon State -205 / Fresno State +205 | 31.6 – 24.9 | 17–47 / 10–38 | Oregon State -3.8 / Oregon State -7.0 | 56.5 / 56.5 | no edge | no edge | no edge |  |

## 2026 Week 10

| Kickoff (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected points | 80% range | Spread: model / line | Total: model / line | Spread edge | Moneyline edge | Total edge | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tue 11/03 7:00 PM | Ohio @ Akron | Ohio 34, Akron 17 | Ohio 91% | Ohio -980 / Akron +980 | 35.0 – 16.0 | 20–51 / 6–28 | Ohio -19.0 / – | 51.2 / – | no line yet | no line yet (fair: Ohio -980) | no line yet |  |
| Tue 11/03 7:00 PM | Buffalo @ Miami (OH) | Buffalo 17, Miami (OH) 31 | Miami (OH) 81% | Buffalo +420 / Miami (OH) -420 | 17.9 – 30.1 | 7–31 / 16–45 | Miami (OH) -12.2 / – | 48.4 / – | no line yet | no line yet (fair: Miami (OH) -420) | no line yet |  |
| Wed 11/04 TBA | Ball State @ Massachusetts | Ball State 24, Massachusetts 27 | Massachusetts 57% | Ball State +130 / Massachusetts -130 | 23.1 – 25.8 | 10–37 / 13–40 | Massachusetts -2.7 / – | 48.9 / – | no line yet | no line yet (fair: Massachusetts -130) | no line yet |  |
| Wed 11/04 TBA | Central Michigan vs Eastern Michigan | Central Michigan 27, Eastern Michigan 24 | Central Michigan 60% | Central Michigan -150 / Eastern Michigan +150 | 27.1 – 23.4 | 14–42 / 10–37 | Central Michigan -3.7 / – | 50.4 / – | no line yet | no line yet (fair: Central Michigan -150) | no line yet | neutral site |
| Wed 11/04 TBA | Toledo @ Sacramento State | Toledo 38, Sacramento State 17 | Toledo 92% | Toledo -1110 / Sacramento State +1110 | 35.7 – 15.6 | 21–52 / 3–28 | Toledo -20.0 / – | 51.3 / – | no line yet | no line yet (fair: Toledo -1110) | no line yet |  |
| Thu 11/05 8:00 PM | UTSA @ Florida Atlantic | UTSA 34, Florida Atlantic 31 | UTSA 56% | UTSA -130 / Florida Atlantic +130 | 33.7 – 31.4 | 20–49 / 17–46 | UTSA -2.3 / – | 65.2 / – | no line yet | no line yet (fair: UTSA -130) | no line yet |  |
| Thu 11/05 8:00 PM | James Madison @ Southern Miss | James Madison 38, Southern Miss 17 | James Madison 90% | James Madison -870 / Southern Miss +870 | 36.7 – 18.0 | 21–52 / 7–31 | James Madison -18.7 / – | 54.7 / – | no line yet | no line yet (fair: James Madison -870) | no line yet |  |
| Fri 11/06 7:00 PM | Virginia Tech @ SMU | Virginia Tech 21, SMU 31 | SMU 77% | Virginia Tech +330 / SMU -330 | 22.2 – 33.0 | 10–35 / 17–48 | SMU -10.9 / – | 55.2 / – | no line yet | no line yet (fair: SMU -330) | no line yet |  |
| Fri 11/06 7:30 PM | South Florida @ East Carolina | South Florida 24, East Carolina 27 | East Carolina 50% | South Florida +100 / East Carolina -100 | 24.7 – 24.7 | 10–38 / 10–38 | PK / – | 49.4 / – | no line yet | no line yet (fair: East Carolina -100) | no line yet |  |
| Fri 11/06 8:00 PM | Nebraska @ Illinois | Nebraska 31, Illinois 24 | Nebraska 71% | Nebraska -245 / Illinois +245 | 31.2 – 23.0 | 17–45 / 10–37 | Nebraska -8.2 / – | 54.2 / – | no line yet | no line yet (fair: Nebraska -245) | no line yet |  |
| Fri 11/06 9:00 PM | New Mexico @ Nevada | New Mexico 27, Nevada 17 | New Mexico 78% | New Mexico -345 / Nevada +345 | 28.7 – 17.8 | 14–43 / 7–31 | New Mexico -10.9 / – | 46.6 / – | no line yet | no line yet (fair: New Mexico -345) | no line yet |  |
| Fri 11/06 10:15 PM | TCU @ Arizona | TCU 21, Arizona 28 | Arizona 72% | TCU +255 / Arizona -255 | 20.2 – 28.8 | 7–34 / 14–43 | Arizona -8.6 / – | 49.0 / – | no line yet | no line yet (fair: Arizona -255) | no line yet |  |
| Sat 11/07 TBA | Arkansas @ Auburn | Arkansas 17, Auburn 34 | Auburn 84% | Arkansas +530 / Auburn -530 | 19.0 – 33.7 | 7–32 / 20–49 | Auburn -14.7 / – | 52.7 / – | no line yet | no line yet (fair: Auburn -530) | no line yet |  |
| Sat 11/07 TBA | Oklahoma @ Florida | Oklahoma 24, Florida 21 | Oklahoma 52% | Oklahoma -105 / Florida +105 | 23.6 – 22.9 | 10–38 / 10–37 | Oklahoma -0.7 / – | 46.5 / – | no line yet | no line yet (fair: Oklahoma -105) | no line yet |  |
| Sat 11/07 TBA | Alabama @ LSU | Alabama 21, LSU 31 | LSU 74% | Alabama +285 / LSU -285 | 20.2 – 29.9 | 7–34 / 16–45 | LSU -9.7 / – | 50.0 / – | no line yet | no line yet (fair: LSU -285) | no line yet |  |
| Sat 11/07 TBA | Georgia @ Ole Miss | Georgia 27, Ole Miss 24 | Georgia 55% | Georgia -120 / Ole Miss +120 | 28.8 – 26.9 | 14–44 / 14–41 | Georgia -1.8 / – | 55.7 / – | no line yet | no line yet (fair: Georgia -120) | no line yet |  |
| Sat 11/07 TBA | Vanderbilt @ Mississippi State | Vanderbilt 24, Mississippi State 31 | Mississippi State 66% | Vanderbilt +195 / Mississippi State -195 | 25.0 – 31.7 | 12–38 / 17–48 | Mississippi State -6.7 / – | 56.7 / – | no line yet | no line yet (fair: Mississippi State -195) | no line yet |  |
| Sat 11/07 TBA | Texas @ Missouri | Texas 24, Missouri 21 | Texas 51% | Texas -105 / Missouri +105 | 22.7 – 22.4 | 10–36 / 10–35 | Texas -0.3 / – | 45.0 / – | no line yet | no line yet (fair: Texas -105) | no line yet |  |
| Sat 11/07 TBA | Texas A&M @ South Carolina | Texas A&M 24, South Carolina 21 | Texas A&M 54% | Texas A&M -120 / South Carolina +120 | 25.2 – 23.5 | 13–39 / 10–37 | Texas A&M -1.7 / – | 48.7 / – | no line yet | no line yet (fair: Texas A&M -120) | no line yet |  |
| Sat 11/07 TBA | Kentucky @ Tennessee | Kentucky 17, Tennessee 31 | Tennessee 77% | Kentucky +340 / Tennessee -340 | 18.6 – 29.3 | 7–31 / 14–45 | Tennessee -10.7 / – | 47.8 / – | no line yet | no line yet (fair: Tennessee -340) | no line yet |  |
| Sat 11/07 TBA | BYU @ Utah | BYU 24, Utah 27 | Utah 58% | BYU +135 / Utah -135 | 24.7 – 27.9 | 10–38 / 14–42 | Utah -4.5 / Utah -3.0 | 52.6 / – | no edge | no line yet (fair: Utah -135) | no line yet |  |
| Sat 11/07 TBA | UCF @ Kansas | UCF 24, Kansas 31 | Kansas 67% | UCF +205 / Kansas -205 | 22.6 – 29.2 | 10–36 / 14–44 | Kansas -6.6 / – | 51.7 / – | no line yet | no line yet (fair: Kansas -205) | no line yet |  |
| Sat 11/07 TBA | Cincinnati @ Houston | Cincinnati 31, Houston 34 | Houston 63% | Cincinnati +170 / Houston -170 | 28.9 – 33.8 | 14–44 / 20–49 | Houston -4.9 / – | 62.8 / – | no line yet | no line yet (fair: Houston -170) | no line yet |  |
| Sat 11/07 TBA | Colorado @ Arizona State | Colorado 24, Arizona State 27 | Arizona State 60% | Colorado +150 / Arizona State -150 | 23.2 – 27.0 | 10–37 / 14–41 | Arizona State -3.7 / – | 50.2 / – | no line yet | no line yet (fair: Arizona State -150) | no line yet |  |
| Sat 11/07 TBA | Iowa State @ Baylor | Iowa State 24, Baylor 27 | Baylor 53% | Iowa State +110 / Baylor -110 | 25.1 – 25.9 | 13–39 / 13–41 | Baylor -0.8 / – | 51.0 / – | no line yet | no line yet (fair: Baylor -110) | no line yet |  |
| Sat 11/07 TBA | Oklahoma State @ Kansas State | Oklahoma State 24, Kansas State 34 | Kansas State 75% | Oklahoma State +295 / Kansas State -295 | 24.2 – 34.1 | 10–38 / 20–49 | Kansas State -9.8 / – | 58.3 / – | no line yet | no line yet (fair: Kansas State -295) | no line yet |  |
| Sat 11/07 TBA | West Virginia @ Texas Tech | West Virginia 17, Texas Tech 38 | Texas Tech 91% | West Virginia +1070 / Texas Tech -1070 | 17.9 – 38.2 | 7–31 / 23–54 | Texas Tech -20.3 / – | 56.0 / – | no line yet | no line yet (fair: Texas Tech -1070) | no line yet |  |
| Sat 11/07 TBA | Clemson @ Syracuse | Clemson 27, Syracuse 24 | Clemson 53% | Clemson -110 / Syracuse +110 | 24.9 – 23.6 | 12–38 / 10–38 | Clemson -1.3 / – | 48.5 / – | no line yet | no line yet (fair: Clemson -110) | no line yet |  |
| Sat 11/07 TBA | Duke @ NC State | Duke 31, NC State 28 | Duke 53% | Duke -110 / NC State +110 | 29.6 – 28.6 | 16–45 / 14–43 | Duke -1.0 / – | 58.2 / – | no line yet | no line yet (fair: Duke -110) | no line yet |  |
| Sat 11/07 TBA | Louisville @ Georgia Tech | Louisville 38, Georgia Tech 21 | Louisville 87% | Louisville -650 / Georgia Tech +650 | 37.4 – 20.7 | 22–52 / 7–34 | Louisville -16.7 / – | 58.1 / – | no line yet | no line yet (fair: Louisville -650) | no line yet |  |
| Sat 11/07 TBA | Florida State @ Boston College | Florida State 31, Boston College 24 | Florida State 70% | Florida State -235 / Boston College +235 | 31.2 – 23.3 | 17–46 / 10–37 | Florida State -7.9 / – | 54.5 / – | no line yet | no line yet (fair: Florida State -235) | no line yet |  |
| Sat 11/07 TBA | Merrimack @ Wake Forest | Merrimack 3, Wake Forest 59 | Wake Forest 100% | Merrimack +9900 / Wake Forest -9900 | 3.0 – 58.5 | 0–7 / 44–73 | Wake Forest -55.5 / – | 61.5 / – | no line yet | no line yet (fair: Wake Forest -9900) | no line yet | FCS opponent |
| Sat 11/07 TBA | Michigan State @ Michigan | Michigan State 10, Michigan 31 | Michigan 93% | Michigan State +1300 / Michigan -1300 | 11.7 – 31.3 | 3–22 / 17–46 | Michigan -19.6 / – | 43.0 / – | no line yet | no line yet (fair: Michigan -1300) | no line yet |  |
| Sat 11/07 TBA | UCLA @ Minnesota | UCLA 24, Minnesota 17 | UCLA 76% | UCLA -310 / Minnesota +310 | 27.0 – 17.1 | 13–42 / 6–30 | UCLA -9.9 / – | 44.1 / – | no line yet | no line yet (fair: UCLA -310) | no line yet |  |
| Sat 11/07 TBA | Iowa @ Northwestern | Iowa 24, Northwestern 27 | Northwestern 56% | Iowa +125 / Northwestern -125 | 23.8 – 26.2 | 10–38 / 13–41 | Northwestern -2.4 / – | 49.9 / – | no line yet | no line yet (fair: Northwestern -125) | no line yet |  |
| Sat 11/07 TBA | Oregon @ Ohio State | Oregon 21, Ohio State 28 | Ohio State 68% | Oregon +210 / Ohio State -210 | 20.7 – 27.4 | 7–34 / 14–42 | Ohio State -13.7 / Ohio State -6.0 | 48.2 / – | no edge | no line yet (fair: Ohio State -210) | no line yet |  |
| Sat 11/07 TBA | Maryland @ Purdue | Maryland 24, Purdue 27 | Purdue 56% | Maryland +125 / Purdue -125 | 25.3 – 27.5 | 13–39 / 14–42 | Purdue -2.2 / – | 52.9 / – | no line yet | no line yet (fair: Purdue -125) | no line yet |  |
| Sat 11/07 TBA | Penn State @ Washington | Penn State 24, Washington 21 | Penn State 52% | Penn State -105 / Washington +105 | 23.6 – 23.0 | 10–37 / 10–37 | Penn State -0.6 / – | 46.5 / – | no line yet | no line yet (fair: Penn State -105) | no line yet |  |
| Sat 11/07 TBA | Rutgers @ Wisconsin | Rutgers 17, Wisconsin 31 | Wisconsin 84% | Rutgers +520 / Wisconsin -520 | 18.2 – 32.6 | 7–31 / 17–48 | Wisconsin -14.3 / – | 50.8 / – | no line yet | no line yet (fair: Wisconsin -520) | no line yet |  |
| Sat 11/07 TBA | Charlotte @ UAB | Charlotte 17, UAB 31 | UAB 84% | Charlotte +525 / UAB -525 | 17.8 – 32.1 | 7–31 / 17–48 | UAB -14.3 / – | 49.9 / – | no line yet | no line yet (fair: UAB -525) | no line yet |  |
| Sat 11/07 TBA | Rice @ North Texas | Rice 20, North Texas 41 | North Texas 91% | Rice +1010 / North Texas -1010 | 21.0 – 40.8 | 7–34 / 26–57 | North Texas -19.8 / – | 61.8 / – | no line yet | no line yet (fair: North Texas -1010) | no line yet |  |
| Sat 11/07 TBA | Tulsa @ Tulane | Tulsa 24, Tulane 27 | Tulane 58% | Tulsa +140 / Tulane -140 | 23.9 – 27.1 | 10–38 / 13–41 | Tulane -3.2 / – | 51.0 / – | no line yet | no line yet (fair: Tulane -140) | no line yet |  |
| Sat 11/07 TBA | Hawai'i @ UTEP | Hawai'i 31, UTEP 17 | Hawai'i 80% | Hawai'i -400 / UTEP +400 | 30.9 – 18.6 | 17–45 / 7–31 | Hawai'i -12.4 / – | 49.5 / – | no line yet | no line yet (fair: Hawai'i -400) | no line yet |  |
| Sat 11/07 TBA | Northern Illinois @ San José State | Northern Illinois 24, San José State 31 | San José State 70% | Northern Illinois +230 / San José State -230 | 23.2 – 30.9 | 10–37 / 17–45 | San José State -7.7 / – | 54.1 / – | no line yet | no line yet (fair: San José State -230) | no line yet |  |
| Sat 11/07 TBA | Georgia State @ App State | Georgia State 28, App State 31 | App State 57% | Georgia State +130 / App State -130 | 28.0 – 30.9 | 14–42 / 17–45 | App State -3.0 / – | 58.9 / – | no line yet | no line yet (fair: App State -130) | no line yet |  |
| Sat 11/07 TBA | Old Dominion @ Coastal Carolina | Old Dominion 21, Coastal Carolina 24 | Coastal Carolina 58% | Old Dominion +140 / Coastal Carolina -140 | 20.7 – 23.7 | 8–34 / 10–38 | Coastal Carolina -3.0 / – | 44.4 / – | no line yet | no line yet (fair: Coastal Carolina -140) | no line yet |  |
| Sat 11/07 TBA | Marshall @ Georgia Southern | Marshall 31, Georgia Southern 28 | Marshall 55% | Marshall -120 / Georgia Southern +120 | 29.6 – 28.2 | 16–44 / 14–42 | Marshall -1.4 / – | 57.7 / – | no line yet | no line yet (fair: Marshall -120) | no line yet |  |
| Sat 11/07 TBA | South Alabama @ Louisiana | South Alabama 28, Louisiana 31 | Louisiana 64% | South Alabama +175 / Louisiana -175 | 26.6 – 31.8 | 13–41 / 17–47 | Louisiana -5.2 / – | 58.3 / – | no line yet | no line yet (fair: Louisiana -175) | no line yet |  |
| Sat 11/07 TBA | Louisiana Tech @ Troy | Louisiana Tech 24, Troy 21 | Louisiana Tech 58% | Louisiana Tech -135 / Troy +135 | 25.9 – 23.0 | 13–40 / 10–37 | Louisiana Tech -3.0 / – | 48.9 / – | no line yet | no line yet (fair: Louisiana Tech -135) | no line yet |  |
| Sat 11/07 12:00 PM | North Carolina @ UConn | North Carolina 30, UConn 27 | North Carolina 52% | North Carolina -110 / UConn +110 | 28.2 – 27.4 | 14–42 / 14–42 | North Carolina -0.8 / – | 55.7 / – | no line yet | no line yet (fair: North Carolina -110) | no line yet |  |
| Sat 11/07 3:00 PM | UL Monroe @ Arkansas State | UL Monroe 21, Arkansas State 31 | Arkansas State 82% | UL Monroe +450 / Arkansas State -450 | 20.4 – 33.7 | 7–34 / 20–49 | Arkansas State -13.3 / – | 54.1 / – | no line yet | no line yet (fair: Arkansas State -450) | no line yet |  |
| Sat 11/07 3:00 PM | Delaware @ Kennesaw State | Delaware 27, Kennesaw State 24 | Delaware 63% | Delaware -165 / Kennesaw State +165 | 29.9 – 25.1 | 16–45 / 13–38 | Delaware -4.8 / – | 55.0 / – | no line yet | no line yet (fair: Delaware -165) | no line yet |  |
| Sat 11/07 3:30 PM | Temple @ Navy | Temple 24, Navy 31 | Navy 73% | Temple +265 / Navy -265 | 23.3 – 32.6 | 10–37 / 17–48 | Navy -9.3 / – | 55.8 / – | no line yet | no line yet (fair: Navy -265) | no line yet |  |
| Sat 11/07 3:30 PM | Western Kentucky @ Middle Tennessee | Western Kentucky 27, Middle Tennessee 24 | Western Kentucky 56% | Western Kentucky -125 / Middle Tennessee +125 | 26.0 – 24.0 | 13–41 / 10–38 | Western Kentucky -2.0 / – | 50.1 / – | no line yet | no line yet (fair: Western Kentucky -125) | no line yet |  |
| Sat 11/07 4:00 PM | Missouri State @ Florida International | Missouri State 24, Florida International 27 | Florida International 60% | Missouri State +150 / Florida International -150 | 23.8 – 27.8 | 10–38 / 14–42 | Florida International -4.0 / – | 51.7 / – | no line yet | no line yet (fair: Florida International -150) | no line yet |  |
| Sat 11/07 5:00 PM | Liberty @ New Mexico State | Liberty 31, New Mexico State 17 | Liberty 81% | Liberty -415 / New Mexico State +415 | 30.1 – 18.1 | 16–45 / 7–31 | Liberty -12.1 / – | 48.2 / – | no line yet | no line yet (fair: Liberty -415) | no line yet |  |
| Sat 11/07 6:00 PM | Boise State @ Colorado State | Boise State 38, Colorado State 21 | Boise State 84% | Boise State -530 / Colorado State +530 | 38.0 – 22.5 | 23–54 / 10–36 | Boise State -15.5 / – | 60.5 / – | no line yet | no line yet (fair: Boise State -530) | no line yet |  |
| Sat 11/07 7:00 PM | Sam Houston @ Jacksonville State | Sam Houston 14, Jacksonville State 31 | Jacksonville State 86% | Sam Houston +590 / Jacksonville State -590 | 15.9 – 31.0 | 6–28 / 17–46 | Jacksonville State -15.1 / – | 46.9 / – | no line yet | no line yet (fair: Jacksonville State -590) | no line yet |  |
| Sat 11/07 7:30 PM | Miami @ Notre Dame | Miami 24, Notre Dame 27 | Notre Dame 62% | Miami +165 / Notre Dame -165 | 23.5 – 28.1 | 10–38 / 14–42 | Notre Dame -4.5 / – | 51.6 / – | no line yet | no line yet (fair: Notre Dame -165) | no line yet |  |
| Sat 11/07 7:30 PM | Air Force @ Army | Air Force 24, Army 31 | Army 67% | Air Force +200 / Army -200 | 26.7 – 33.0 | 13–41 / 17–48 | Army -6.3 / – | 59.7 / – | no line yet | no line yet (fair: Army -200) | no line yet |  |
| Sat 11/07 9:30 PM | Fresno State @ Utah State | Fresno State 27, Utah State 20 | Fresno State 66% | Fresno State -200 / Utah State +200 | 26.7 – 20.9 | 13–41 / 9–34 | Fresno State -5.8 / – | 47.6 / – | no line yet | no line yet (fair: Fresno State -200) | no line yet |  |
| Sat 11/07 10:30 PM | Texas State @ Oregon State | Texas State 31, Oregon State 38 | Oregon State 65% | Texas State +190 / Oregon State -190 | 31.5 – 37.5 | 17–45 / 23–52 | Oregon State -6.0 / – | 69.0 / – | no line yet | no line yet (fair: Oregon State -190) | no line yet |  |
| Sat 11/07 10:30 PM | Wyoming @ UNLV | Wyoming 21, UNLV 28 | UNLV 72% | Wyoming +255 / UNLV -255 | 20.2 – 29.0 | 7–34 / 14–44 | UNLV -8.8 / – | 49.2 / – | no line yet | no line yet (fair: UNLV -255) | no line yet |  |

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
