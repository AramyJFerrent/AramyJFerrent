# College football score predictions

Updated Thu Nov 05, 2026 09:23 PM ET. Refreshed automatically every day of the season and several times on Saturdays; each game's prediction is locked at kickoff and graded once the final score is in. Scores are the most likely real scoreline near the expected points; ranges cover 80% of simulated outcomes for each team. College scores scatter widely, so read the ranges, not just the headline score.

Expected points blend the model with the betting line using the weight that has predicted best in recent seasons (see Current model fit). The spread and total columns show the model's own numbers next to the line, so you can see where it disagrees. Games without a line yet use the model alone.

The fair moneyline is the American odds that match the win chance exactly, with no bookmaker margin: -200 means risk $200 to win $100, +200 means risk $100 to win $200. A sportsbook's price will be a little worse on both sides because of its cut, so a book only offers value on a team when its price beats the fair line.

The edge columns judge each bet by its expected value per $1 staked at the posted price, using the final prediction: the model blended with the line, run through the score simulator, pushes included, and anchored to the market's own chances so that only what the blend moves off the line counts. The model's own spread and total (shown alongside) sit several points from the line in most games, but the blend keeps only the share of that disagreement the model has earned in past seasons, so edges are rare. The side with the higher value is shown when it reaches 3% (+3 cents per $1), as the team or side, the price, the expected value, its chance of winning the bet and its stake, a 25% share of the Kelly stake in units of 1% of the bankroll with at most 3 units on one game; anything short is no edge. Where a book posts no price for a spread or total it is assumed to be -110 and marked -110*; moneylines are never assumed. In the walk-forward backtest against closing lines, edges returned spread -100.0% on 1 bets (posted prices, 2016–2019); spread -3.9% on 156 bets (assumed -110 prices, 2016–2025); moneyline +13.7% on 575 bets (posted prices, 2016–2025); total +2.6% on 367 bets (posted prices, 2016–2019); total -5.7% on 172 bets (assumed -110 prices, 2016–2025). None of these is clearly above zero, so treat these edges as an experiment, not a betting system. The live record is tracked below, graded at the price logged with the last prediction before kickoff.

## 2026 Week 10

| Kickoff (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected points | 80% range | Spread: model / line | Total: model / line | Spread edge | Moneyline edge | Total edge | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Fri 11/06 7:00 PM | Virginia Tech @ SMU | Virginia Tech 24, SMU 31 | SMU 68% | Virginia Tech +210 / SMU -210 | 24.8 – 31.4 | 10–38 / 17–46 | SMU -10.4 / SMU -6.2 | 55.2 / 56.5 | no edge | no edge | no edge |  |
| Fri 11/06 7:30 PM | South Florida @ East Carolina | South Florida 21, East Carolina 24 | East Carolina 56% | South Florida +130 / East Carolina -130 | 19.4 – 21.7 | 7–31 / 10–35 | South Florida -0.5 / East Carolina -2.5 | 47.7 / 39.5 | no edge | no edge | no edge |  |
| Fri 11/06 8:00 PM | Nebraska @ Illinois | Nebraska 27, Illinois 24 | Nebraska 62% | Nebraska -165 / Illinois +165 | 27.8 – 23.2 | 14–42 / 10–37 | Nebraska -6.0 / Nebraska -4.5 | 52.9 / 50.5 | no edge | no edge | no edge |  |
| Fri 11/06 9:00 PM | New Mexico @ Nevada | New Mexico 24, Nevada 14 | New Mexico 76% | New Mexico -320 / Nevada +320 | 24.5 – 14.6 | 10–38 / 3–27 | New Mexico -9.3 / New Mexico -10.0 | 41.7 / 38.5 | no edge | no edge | no edge |  |
| Fri 11/06 10:15 PM | TCU @ Arizona | TCU 20, Arizona 27 | Arizona 69% | TCU +225 / Arizona -225 | 19.6 – 27.2 | 7–32 / 14–41 | Arizona -8.4 / Arizona -7.5 | 49.0 / 46.2 | no edge | no edge | no edge |  |
| Sat 11/07 12:00 PM | Texas @ Missouri | Texas 24, Missouri 21 | Texas 57% | Texas -130 / Missouri +130 | 22.5 – 20.2 | 10–35 / 7–34 | Missouri -0.5 / Texas -2.5 | 43.5 / 42.5 | no edge | no edge | no edge |  |
| Sat 11/07 12:00 PM | BYU @ Utah | BYU 24, Utah 27 | Utah 64% | BYU +175 / Utah -175 | 22.3 – 27.2 | 10–35 / 14–41 | Utah -8.8 / Utah -4.5 | 53.6 / 48.5 | no edge | no edge | no edge |  |
| Sat 11/07 12:00 PM | Iowa State @ Baylor | Iowa State 24, Baylor 31 | Baylor 75% | Iowa State +295 / Baylor -295 | 21.0 – 30.6 | 7–34 / 17–45 | Baylor -5.3 / Baylor -10.0 | 53.1 / 51.2 | no edge | no edge | no edge |  |
| Sat 11/07 12:00 PM | Clemson @ Syracuse | Clemson 27, Syracuse 24 | Clemson 58% | Clemson -135 / Syracuse +135 | 25.8 – 23.4 | 13–40 / 10–37 | Clemson -1.5 / Clemson -2.5 | 48.0 / 49.5 | no edge | no edge | no edge |  |
| Sat 11/07 12:00 PM | Florida State @ Boston College | Florida State 31, Boston College 24 | Florida State 68% | Florida State -210 / Boston College +210 | 29.7 – 23.1 | 16–45 / 10–37 | Florida State -7.9 / Florida State -6.5 | 54.1 / 52.5 | no edge | no edge | no edge |  |
| Sat 11/07 12:00 PM | North Carolina @ UConn | North Carolina 31, UConn 24 | North Carolina 67% | North Carolina -200 / UConn +200 | 30.9 – 24.3 | 17–45 / 10–38 | North Carolina -1.4 / North Carolina -7.0 | 58.1 / 54.5 | no edge | no edge | no edge |  |
| Sat 11/07 12:00 PM | UCLA @ Minnesota | UCLA 24, Minnesota 17 | UCLA 67% | UCLA -205 / Minnesota +205 | 22.5 – 16.6 | 10–35 / 6–28 | UCLA -9.6 / UCLA -5.5 | 40.4 / 38.8 | no edge | no edge | no edge |  |
| Sat 11/07 12:00 PM | Tulsa @ Tulane | Tulsa 27, Tulane 24 | Tulsa 55% | Tulsa -120 / Tulane +120 | 26.0 – 24.2 | 13–40 / 10–38 | Tulane -2.8 / Tulsa -2.2 | 52.4 / 49.8 | no edge | no edge | no edge |  |
| Sat 11/07 12:30 PM | Duke @ NC State | Duke 27, NC State 24 | Duke 60% | Duke -150 / NC State +150 | 28.1 – 24.2 | 14–42 / 10–38 | Duke -2.7 / Duke -4.0 | 56.1 / 51.5 | no edge | no edge | no edge |  |
| Sat 11/07 12:30 PM | Maryland @ Purdue | Maryland 24, Purdue 31 | Purdue 64% | Maryland +180 / Purdue -180 | 25.2 – 30.5 | 12–39 / 17–45 | Purdue -3.0 / Purdue -5.5 | 52.0 / 56.5 | no edge | no edge | no edge |  |
| Sat 11/07 12:45 PM | Arkansas @ Auburn | Arkansas 21, Auburn 31 | Auburn 76% | Arkansas +315 / Auburn -315 | 21.8 – 32.5 | 10–35 / 17–48 | Auburn -15.5 / Auburn -10.2 | 54.1 / 54.2 | no edge | no edge | no edge |  |
| Sat 11/07 1:00 PM | Oklahoma State @ Kansas State | Oklahoma State 31, Kansas State 28 | Oklahoma State 62% | Oklahoma State -165 / Kansas State +165 | 33.7 – 28.5 | 20–49 / 14–43 | Kansas State -5.5 / Oklahoma State -6.2 | 60.5 / 62.5 | no edge | Kansas State (+166): EV +4.1%, 39%, stake 0.6u | no edge |  |
| Sat 11/07 1:00 PM | Old Dominion @ Coastal Carolina | Old Dominion 17, Coastal Carolina 24 | Coastal Carolina 67% | Old Dominion +205 / Coastal Carolina -205 | 18.9 – 25.3 | 7–31 / 13–38 | Coastal Carolina -6.2 / Coastal Carolina -6.5 | 43.9 / 44.2 | no edge | no edge | no edge |  |
| Sat 11/07 2:30 PM | Georgia State @ App State | Georgia State 24, App State 31 | App State 66% | Georgia State +190 / App State -190 | 24.4 – 30.5 | 10–38 / 17–45 | App State -4.3 / App State -6.2 | 57.4 / 54.2 | no edge | no edge | no edge |  |
| Sat 11/07 3:00 PM | Texas A&M @ South Carolina | Texas A&M 24, South Carolina 31 | South Carolina 68% | Texas A&M +210 / South Carolina -210 | 22.0 – 28.5 | 10–35 / 14–43 | South Carolina -2.0 / South Carolina -7.0 | 49.6 / 50.8 | no edge | no edge | no edge |  |
| Sat 11/07 3:00 PM | UL Monroe @ Arkansas State | UL Monroe 17, Arkansas State 34 | Arkansas State 83% | UL Monroe +505 / Arkansas State -505 | 19.5 – 33.8 | 7–31 / 20–49 | Arkansas State -11.7 / Arkansas State -14.5 | 53.5 / 53.2 | no edge | no edge | no edge |  |
| Sat 11/07 3:00 PM | Delaware @ Kennesaw State | Delaware 31, Kennesaw State 28 | Delaware 56% | Delaware -125 / Kennesaw State +125 | 29.2 – 27.4 | 15–44 / 14–41 | Delaware -5.0 / Delaware -1.5 | 55.4 / 57.0 | no edge | no edge | no edge |  |
| Sat 11/07 3:30 PM | Alabama @ LSU | Alabama 24, LSU 31 | LSU 67% | Alabama +205 / LSU -205 | 22.9 – 29.2 | 10–37 / 16–44 | LSU -9.2 / LSU -6.0 | 50.6 / 52.5 | no edge | no edge | no edge |  |
| Sat 11/07 3:30 PM | Cincinnati @ Houston | Cincinnati 28, Houston 38 | Houston 75% | Cincinnati +295 / Houston -295 | 26.1 – 36.5 | 13–41 / 21–52 | Houston -6.3 / Houston -10.8 | 63.1 / 62.5 | no edge | no edge | no edge |  |
| Sat 11/07 3:30 PM | Merrimack @ Wake Forest | Merrimack 3, Wake Forest 52 | Wake Forest 100% | Merrimack +9900 / Wake Forest -9900 | 5.5 – 53.9 | 0–13 / 40–69 | Wake Forest -57.4 / Wake Forest -47.5 | 63.4 / 58.5 | no edge | no line yet (fair: Wake Forest -9900) | no edge | FCS opponent |
| Sat 11/07 3:30 PM | Oregon @ Ohio State | Oregon 20, Ohio State 27 | Ohio State 71% | Oregon +240 / Ohio State -240 | 19.5 – 27.5 | 7–32 / 14–42 | Ohio State -11.4 / Ohio State -7.8 | 49.2 / 46.5 | no edge | no edge | no edge |  |
| Sat 11/07 3:30 PM | Penn State @ Washington | Penn State 21, Washington 24 | Washington 57% | Penn State +130 / Washington -130 | 21.1 – 23.4 | 9–34 / 10–37 | Washington -0.3 / Washington -2.5 | 45.6 / 44.2 | no edge | no edge | no edge |  |
| Sat 11/07 3:30 PM | Charlotte @ UAB | Charlotte 21, UAB 28 | UAB 73% | Charlotte +275 / UAB -275 | 19.6 – 28.4 | 7–32 / 14–42 | UAB -12.8 / UAB -8.5 | 50.1 / 47.5 | no edge | no edge | no edge |  |
| Sat 11/07 3:30 PM | Temple @ Navy | Temple 24, Navy 31 | Navy 70% | Temple +230 / Navy -230 | 23.5 – 31.0 | 10–37 / 17–45 | Navy -10.9 / Navy -7.2 | 55.6 / 54.5 | no edge | no edge | no edge |  |
| Sat 11/07 3:30 PM | Marshall @ Georgia Southern | Marshall 24, Georgia Southern 31 | Georgia Southern 74% | Marshall +285 / Georgia Southern -285 | 22.7 – 32.4 | 10–36 / 17–48 | Georgia Southern -0.6 / Georgia Southern -10.5 | 56.5 / 54.8 | no edge | Marshall (+310): EV +3.7%, 25%, stake 0.3u | no edge |  |
| Sat 11/07 3:30 PM | Western Kentucky @ Middle Tennessee | Western Kentucky 27, Middle Tennessee 24 | Western Kentucky 54% | Western Kentucky -120 / Middle Tennessee +120 | 27.3 – 25.7 | 14–42 / 13–40 | Western Kentucky -2.2 / Western Kentucky -1.5 | 50.8 / 53.5 | no edge | no edge | no edge |  |
| Sat 11/07 3:45 PM | UCF @ Kansas | UCF 21, Kansas 24 | Kansas 59% | UCF +145 / Kansas -145 | 22.5 – 25.9 | 10–36 / 13–40 | Kansas -6.8 / Kansas -3.0 | 52.0 / 47.5 | no edge | no edge | no edge |  |
| Sat 11/07 4:00 PM | Rice @ North Texas | Rice 24, North Texas 41 | North Texas 87% | Rice +690 / North Texas -690 | 23.4 – 40.8 | 10–37 / 26–56 | North Texas -18.8 / North Texas -17.2 | 63.3 / 64.5 | no edge | no edge | no edge |  |
| Sat 11/07 4:00 PM | Northern Illinois @ San José State | Northern Illinois 24, San José State 31 | San José State 74% | Northern Illinois +290 / San José State -290 | 21.1 – 30.8 | 7–34 / 17–45 | San José State -6.0 / San José State -10.0 | 52.5 / 51.8 | no edge | no edge | no edge |  |
| Sat 11/07 4:00 PM | Missouri State @ Florida International | Missouri State 24, Florida International 27 | Florida International 61% | Missouri State +160 / Florida International -160 | 22.8 – 27.2 | 10–36 / 14–41 | Florida International -0.7 / Florida International -4.8 | 50.6 / 49.8 | no edge | no edge | no edge |  |
| Sat 11/07 4:00 PM | Louisiana Tech @ Troy | Louisiana Tech 24, Troy 21 | Louisiana Tech 65% | Louisiana Tech -185 / Troy +185 | 26.4 – 21.1 | 13–41 / 9–34 | Louisiana Tech -6.2 / Louisiana Tech -5.2 | 46.2 / 47.8 | no edge | no edge | no edge |  |
| Sat 11/07 4:15 PM | Vanderbilt @ Mississippi State | Vanderbilt 24, Mississippi State 27 | Mississippi State 59% | Vanderbilt +145 / Mississippi State -145 | 23.2 – 26.6 | 10–37 / 13–41 | Mississippi State -7.4 / Mississippi State -3.0 | 55.3 / 48.5 | no edge | no edge | no edge |  |
| Sat 11/07 4:15 PM | Rutgers @ Wisconsin | Rutgers 14, Wisconsin 31 | Wisconsin 90% | Rutgers +895 / Wisconsin -895 | 14.6 – 32.5 | 3–27 / 17–48 | Wisconsin -14.2 / Wisconsin -18.2 | 50.2 / 46.2 | no edge | no edge | no edge |  |
| Sat 11/07 5:00 PM | South Alabama @ Louisiana | South Alabama 24, Louisiana 31 | Louisiana 69% | South Alabama +220 / Louisiana -220 | 25.2 – 32.5 | 13–39 / 17–48 | Louisiana -4.6 / Louisiana -7.5 | 58.4 / 57.5 | no edge | no edge | no edge |  |
| Sat 11/07 6:00 PM | Boise State @ Colorado State | Boise State 41, Colorado State 24 | Boise State 88% | Boise State -715 / Colorado State +715 | 42.5 – 25.2 | 27–58 / 12–38 | Boise State -15.9 / Boise State -17.5 | 63.2 / 68.8 | no edge | no edge | no edge |  |
| Sat 11/07 6:15 PM | Kentucky @ Tennessee | Kentucky 21, Tennessee 28 | Tennessee 68% | Kentucky +210 / Tennessee -210 | 21.3 – 28.0 | 9–34 / 14–42 | Tennessee -9.4 / Tennessee -6.5 | 48.3 / 49.5 | no edge | no edge | no edge |  |
| Sat 11/07 7:00 PM | Sam Houston @ Jacksonville State | Sam Houston 14, Jacksonville State 31 | Jacksonville State 90% | Sam Houston +910 / Jacksonville State -910 | 14.9 – 32.4 | 3–27 / 17–48 | Jacksonville State -18.0 / Jacksonville State -17.5 | 45.7 / 47.8 | no edge | no edge | no edge |  |
| Sat 11/07 7:30 PM | Georgia @ Ole Miss | Georgia 30, Ole Miss 27 | Georgia 59% | Georgia -145 / Ole Miss +145 | 29.8 – 26.3 | 16–44 / 13–41 | Georgia -3.0 / Georgia -3.5 | 54.2 / 56.5 | no edge | no edge | no edge |  |
| Sat 11/07 7:30 PM | Colorado @ Arizona State | Colorado 21, Arizona State 24 | Arizona State 60% | Colorado +150 / Arizona State -150 | 22.5 – 26.2 | 10–36 / 13–41 | Arizona State -5.9 / Arizona State -3.5 | 49.9 / 48.5 | no edge | no edge | no edge |  |
| Sat 11/07 7:30 PM | Louisville @ Georgia Tech | Louisville 41, Georgia Tech 24 | Louisville 83% | Louisville -500 / Georgia Tech +500 | 38.1 – 23.4 | 24–54 / 10–37 | Louisville -17.4 / Louisville -14.5 | 58.5 / 62.2 | no edge | no edge | no edge |  |
| Sat 11/07 7:30 PM | Miami @ Notre Dame | Miami 24, Notre Dame 31 | Notre Dame 68% | Miami +210 / Notre Dame -210 | 23.7 – 30.7 | 10–38 / 17–45 | Notre Dame -4.6 / Notre Dame -7.2 | 53.9 / 54.5 | no edge | no edge | no edge |  |
| Sat 11/07 7:30 PM | Michigan State @ Michigan | Michigan State 13, Michigan 27 | Michigan 86% | Michigan State +610 / Michigan -610 | 13.1 – 27.2 | 3–24 / 14–42 | Michigan -20.6 / Michigan -13.5 | 42.3 / 39.8 | no edge | no edge | no edge |  |
| Sat 11/07 7:30 PM | Iowa @ Northwestern | Iowa 21, Northwestern 24 | Northwestern 56% | Iowa +130 / Northwestern -130 | 21.9 – 24.2 | 10–35 / 10–38 | Northwestern -0.6 / Northwestern -2.5 | 49.5 / 45.2 | no edge | no edge | no edge |  |
| Sat 11/07 7:30 PM | Air Force @ Army | Air Force 24, Army 27 | Army 59% | Air Force +145 / Army -145 | 22.2 – 25.5 | 10–35 / 13–40 | Army -5.9 / Army -3.0 | 60.9 / 44.5 | no edge | no edge | Over 44.5 (-110*): EV +11.0%, 58%, stake 3.0u | * price not posted; assumed -110 |
| Sat 11/07 7:45 PM | Oklahoma @ Florida | Oklahoma 17, Florida 24 | Florida 66% | Oklahoma +190 / Florida -190 | 19.6 – 25.6 | 7–33 / 13–39 | Florida -1.1 / Florida -6.5 | 45.2 / 45.2 | no edge | no edge | no edge |  |
| Sat 11/07 8:00 PM | Liberty @ New Mexico State | Liberty 31, New Mexico State 14 | Liberty 88% | Liberty -750 / New Mexico State +750 | 31.5 – 15.0 | 17–47 / 3–27 | Liberty -16.5 / Liberty -16.5 | 47.3 / 46.2 | no edge | no edge | no edge |  |
| Sat 11/07 9:30 PM | West Virginia @ Texas Tech | West Virginia 24, Texas Tech 41 | Texas Tech 87% | West Virginia +675 / Texas Tech -675 | 23.1 – 40.7 | 10–37 / 26–56 | Texas Tech -21.4 / Texas Tech -17.2 | 56.7 / 65.5 | no edge | no edge | no edge |  |
| Sat 11/07 9:30 PM | Fresno State @ Utah State | Fresno State 24, Utah State 21 | Fresno State 57% | Fresno State -135 / Utah State +135 | 22.9 – 20.4 | 10–36 / 7–34 | Fresno State -2.6 / Fresno State -2.5 | 46.6 / 42.5 | no edge | no edge | no edge |  |
| Sat 11/07 9:30 PM | Hawai'i @ UTEP | Hawai'i 28, UTEP 21 | Hawai'i 73% | Hawai'i -275 / UTEP +275 | 29.1 – 20.3 | 15–44 / 7–34 | Hawai'i -12.9 / Hawai'i -8.5 | 50.0 / 49.2 | no edge | no edge | no edge |  |
| Sat 11/07 10:30 PM | Texas State @ Oregon State | Texas State 31, Oregon State 38 | Oregon State 65% | Texas State +190 / Oregon State -190 | 32.1 – 38.3 | 17–48 / 24–54 | Oregon State -5.9 / Oregon State -6.2 | 68.0 / 71.2 | no edge | no edge | no edge |  |
| Sat 11/07 10:30 PM | Wyoming @ UNLV | Wyoming 24, UNLV 27 | UNLV 66% | Wyoming +195 / UNLV -195 | 21.5 – 27.3 | 9–35 / 14–41 | UNLV -9.0 / UNLV -5.5 | 49.8 / 48.5 | no edge | no edge | no edge |  |

## 2026 Week 11

| Kickoff (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected points | 80% range | Spread: model / line | Total: model / line | Spread edge | Moneyline edge | Total edge | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tue 11/10 7:00 PM | Western Michigan @ Akron | Western Michigan 31, Akron 17 | Western Michigan 86% | Western Michigan -605 / Akron +605 | 32.5 – 17.4 | 19–48 / 6–30 | Western Michigan -15.1 / – | 49.8 / – | no line yet | no line yet (fair: Western Michigan -605) | no line yet |  |
| Tue 11/10 7:00 PM | Kent State @ Bowling Green | Kent State 17, Bowling Green 24 | Bowling Green 65% | Kent State +185 / Bowling Green -185 | 18.0 – 23.4 | 7–31 / 10–37 | Bowling Green -5.4 / – | 41.4 / – | no line yet | no line yet (fair: Bowling Green -185) | no line yet |  |
| Tue 11/10 8:00 PM | Ohio @ Miami (OH) | Ohio 24, Miami (OH) 21 | Ohio 56% | Ohio -125 / Miami (OH) +125 | 25.0 – 22.9 | 12–38 / 10–36 | Ohio -2.1 / – | 47.8 / – | no line yet | no line yet (fair: Ohio -125) | no line yet |  |
| Wed 11/11 TBA | Buffalo @ Ball State | Buffalo 24, Ball State 27 | Ball State 56% | Buffalo +125 / Ball State -125 | 24.7 – 27.3 | 13–38 / 14–42 | Ball State -2.7 / – | 52.0 / – | no line yet | no line yet (fair: Ball State -125) | no line yet |  |
| Wed 11/11 TBA | Massachusetts @ Toledo | Massachusetts 14, Toledo 35 | Toledo 91% | Massachusetts +1050 / Toledo -1050 | 15.2 – 34.6 | 3–27 / 20–50 | Toledo -19.4 / – | 49.8 / – | no line yet | no line yet (fair: Toledo -1050) | no line yet |  |
| Wed 11/11 7:30 PM | Sacramento State @ Central Michigan | Sacramento State 17, Central Michigan 24 | Central Michigan 72% | Sacramento State +260 / Central Michigan -260 | 18.9 – 27.7 | 7–31 / 14–42 | Central Michigan -8.9 / – | 46.6 / – | no line yet | no line yet (fair: Central Michigan -260) | no line yet |  |
| Thu 11/12 8:00 PM | Memphis @ South Florida | Memphis 27, South Florida 24 | Memphis 51% | Memphis -105 / South Florida +105 | 27.5 – 27.3 | 14–42 / 14–42 | Memphis -0.2 / – | 54.8 / – | no line yet | no line yet (fair: Memphis -105) | no line yet |  |
| Thu 11/12 9:00 PM | Louisiana @ UL Monroe | Louisiana 31, UL Monroe 24 | Louisiana 70% | Louisiana -230 / UL Monroe +230 | 30.0 – 22.6 | 17–45 / 10–36 | Louisiana -7.4 / – | 52.6 / – | no line yet | no line yet (fair: Louisiana -230) | no line yet |  |
| Fri 11/13 7:00 PM | Florida State @ Pittsburgh | Florida State 28, Pittsburgh 31 | Pittsburgh 58% | Florida State +135 / Pittsburgh -135 | 26.3 – 29.1 | 13–41 / 14–44 | Pittsburgh -2.8 / – | 55.4 / – | no line yet | no line yet (fair: Pittsburgh -135) | no line yet |  |
| Fri 11/13 9:00 PM | Illinois @ UCLA | Illinois 17, UCLA 31 | UCLA 82% | Illinois +440 / UCLA -440 | 17.8 – 30.5 | 7–31 / 17–45 | UCLA -15.0 / UCLA -12.5 | 51.4 / 47.5 | no edge | no edge | no edge |  |
| Fri 11/13 10:15 PM | Houston @ Colorado | Houston 31, Colorado 24 | Houston 65% | Houston -185 / Colorado +185 | 29.9 – 24.2 | 16–45 / 10–38 | Houston -5.7 / – | 54.0 / – | no line yet | no line yet (fair: Houston -185) | no line yet |  |
| Sat 11/14 TBA | Arizona State @ UCF | Arizona State 27, UCF 24 | UCF 50% | Arizona State +100 / UCF -100 | 25.1 – 24.9 | 13–38 / 13–38 | Arizona State -0.2 / – | 50.0 / – | no line yet | no line yet (fair: UCF -100) | no line yet |  |
| Sat 11/14 TBA | Baylor @ BYU | Baylor 20, BYU 27 | BYU 69% | Baylor +220 / BYU -220 | 20.7 – 27.6 | 7–34 / 14–42 | BYU -6.3 / BYU -7.0 | 51.9 / 47.5 | no edge | no edge | no edge |  |
| Sat 11/14 TBA | Cincinnati @ Iowa State | Cincinnati 28, Iowa State 31 | Iowa State 59% | Cincinnati +140 / Iowa State -140 | 28.2 – 31.6 | 14–42 / 17–47 | Iowa State -3.4 / – | 59.7 / – | no line yet | no line yet (fair: Iowa State -140) | no line yet |  |
| Sat 11/14 TBA | Kansas @ West Virginia | Kansas 31, West Virginia 28 | Kansas 59% | Kansas -145 / West Virginia +145 | 32.8 – 28.6 | 17–48 / 14–43 | Kansas -4.2 / – | 61.3 / – | no line yet | no line yet (fair: Kansas -145) | no line yet |  |
| Sat 11/14 TBA | Kansas State @ TCU | Kansas State 24, TCU 21 | Kansas State 54% | Kansas State -120 / TCU +120 | 25.0 – 23.4 | 13–38 / 10–37 | Kansas State -1.7 / – | 48.4 / – | no line yet | no line yet (fair: Kansas State -120) | no line yet |  |
| Sat 11/14 TBA | Texas Tech @ Oklahoma State | Texas Tech 31, Oklahoma State 28 | Texas Tech 55% | Texas Tech -125 / Oklahoma State +125 | 32.1 – 29.9 | 17–47 / 17–45 | Texas Tech -9.7 / Texas Tech -1.5 | 56.0 / 63.5 | no edge | no edge | no edge |  |
| Sat 11/14 TBA | Utah @ Arizona | Utah 27, Arizona 24 | Utah 54% | Utah -120 / Arizona +120 | 27.2 – 25.3 | 14–41 / 13–39 | Utah -6.0 / Utah -1.5 | 56.4 / 51.5 | no edge | no edge | no edge |  |
| Sat 11/14 TBA | South Carolina @ Arkansas | South Carolina 31, Arkansas 24 | South Carolina 76% | South Carolina -315 / Arkansas +315 | 32.0 – 22.1 | 17–47 / 10–35 | South Carolina -9.9 / – | 54.2 / – | no line yet | no line yet (fair: South Carolina -315) | no line yet |  |
| Sat 11/14 TBA | Missouri @ Georgia | Missouri 17, Georgia 31 | Georgia 81% | Missouri +440 / Georgia -440 | 17.0 – 29.4 | 6–30 / 15–44 | Georgia -10.4 / Georgia -12.5 | 45.9 / 46.5 | no edge | no edge | no edge |  |
| Sat 11/14 TBA | Florida @ Kentucky | Florida 24, Kentucky 27 | Kentucky 53% | Florida +115 / Kentucky -115 | 26.8 – 28.0 | 13–41 / 14–42 | Florida -1.1 / Kentucky -1.5 | 51.8 / 55.5 | no edge | no edge | no edge |  |
| Sat 11/14 TBA | Texas @ LSU | Texas 17, LSU 24 | LSU 67% | Texas +200 / LSU -200 | 20.2 – 26.1 | 7–34 / 13–41 | LSU -10.2 / LSU -5.5 | 45.5 / 46.5 | no edge | no edge | no edge |  |
| Sat 11/14 TBA | Auburn @ Mississippi State | Auburn 31, Mississippi State 28 | Auburn 51% | Auburn -105 / Mississippi State +105 | 28.5 – 27.9 | 14–42 / 14–42 | Auburn -0.6 / – | 56.5 / – | no line yet | no line yet (fair: Auburn -105) | no line yet |  |
| Sat 11/14 TBA | Ole Miss @ Oklahoma | Ole Miss 24, Oklahoma 27 | Oklahoma 61% | Ole Miss +155 / Oklahoma -155 | 24.7 – 28.2 | 12–38 / 14–43 | Ole Miss -1.7 / Oklahoma -4.0 | 50.4 / 53.5 | no edge | no edge | no edge |  |
| Sat 11/14 TBA | Tennessee @ Texas A&M | Tennessee 24, Texas A&M 31 | Texas A&M 69% | Tennessee +225 / Texas A&M -225 | 22.9 – 30.5 | 10–37 / 17–45 | Tennessee -1.7 / Texas A&M -8.5 | 45.1 / 55.5 | no edge | Tennessee (+285): EV +4.0%, 27%, stake 0.3u | Under 55.5 (-110*): EV +6.2%, 56%, stake 1.7u | * price not posted; assumed -110 |
| Sat 11/14 TBA | Alabama @ Vanderbilt | Alabama 31, Vanderbilt 17 | Alabama 81% | Alabama -430 / Vanderbilt +430 | 32.1 – 19.3 | 17–48 / 7–31 | Alabama -12.8 / – | 51.4 / – | no line yet | no line yet (fair: Alabama -430) | no line yet |  |
| Sat 11/14 TBA | California @ Virginia | California 21, Virginia 31 | Virginia 74% | California +290 / Virginia -290 | 20.6 – 30.1 | 7–34 / 16–45 | Virginia -9.5 / – | 50.7 / – | no line yet | no line yet (fair: Virginia -290) | no line yet |  |
| Sat 11/14 TBA | Duke @ Miami | Duke 17, Miami 38 | Miami 92% | Duke +1160 / Miami -1160 | 17.4 – 38.2 | 6–30 / 23–54 | Miami -18.0 / Miami -21.0 | 56.2 / 55.5 | no edge | no edge | no edge |  |
| Sat 11/14 TBA | Georgia Tech @ Clemson | Georgia Tech 17, Clemson 31 | Clemson 82% | Georgia Tech +450 / Clemson -450 | 18.6 – 31.3 | 7–31 / 17–46 | Clemson -12.8 / – | 49.9 / – | no line yet | no line yet (fair: Clemson -450) | no line yet |  |
| Sat 11/14 TBA | Louisville @ North Carolina | Louisville 31, North Carolina 28 | Louisville 60% | Louisville -150 / North Carolina +150 | 31.0 – 27.9 | 17–45 / 14–42 | Louisville -9.3 / Louisville -2.5 | 56.9 / 59.5 | no edge | no edge | no edge |  |
| Sat 11/14 TBA | Stanford @ Virginia Tech | Stanford 17, Virginia Tech 34 | Virginia Tech 87% | Stanford +640 / Virginia Tech -640 | 19.5 – 36.0 | 7–32 / 21–52 | Virginia Tech -16.5 / – | 55.4 / – | no line yet | no line yet (fair: Virginia Tech -640) | no line yet |  |
| Sat 11/14 TBA | Syracuse @ NC State | Syracuse 28, NC State 31 | NC State 60% | Syracuse +150 / NC State -150 | 27.0 – 30.7 | 13–41 / 17–45 | NC State -3.7 / – | 57.7 / – | no line yet | no line yet (fair: NC State -150) | no line yet |  |
| Sat 11/14 TBA | Wake Forest @ SMU | Wake Forest 31, SMU 28 | Wake Forest 57% | Wake Forest -135 / SMU +135 | 29.4 – 26.5 | 15–44 / 13–41 | Wake Forest -0.9 / Wake Forest -3.0 | 53.4 / 56.5 | no edge | no edge | no edge |  |
| Sat 11/14 TBA | USC @ Indiana | USC 20, Indiana 27 | Indiana 69% | USC +225 / Indiana -225 | 21.6 – 28.9 | 9–35 / 14–44 | Indiana -10.2 / Indiana -7.0 | 50.7 / 50.5 | no edge | no edge | no edge |  |
| Sat 11/14 TBA | Purdue @ Iowa | Purdue 17, Iowa 31 | Iowa 86% | Purdue +595 / Iowa -595 | 16.8 – 31.9 | 6–28 / 17–47 | Iowa -15.0 / – | 48.7 / – | no line yet | no line yet (fair: Iowa -595) | no line yet |  |
| Sat 11/14 TBA | Wisconsin @ Maryland | Wisconsin 24, Maryland 21 | Wisconsin 63% | Wisconsin -170 / Maryland +170 | 24.7 – 19.8 | 13–38 / 7–32 | Wisconsin -4.9 / – | 44.5 / – | no line yet | no line yet (fair: Wisconsin -170) | no line yet |  |
| Sat 11/14 TBA | Washington @ Michigan State | Washington 27, Michigan State 17 | Washington 76% | Washington -315 / Michigan State +315 | 27.8 – 17.7 | 14–42 / 7–31 | Washington -10.0 / – | 45.5 / – | no line yet | no line yet (fair: Washington -315) | no line yet |  |
| Sat 11/14 TBA | Northwestern @ Ohio State | Northwestern 17, Ohio State 27 | Ohio State 76% | Northwestern +315 / Ohio State -315 | 19.7 – 29.8 | 7–33 / 16–45 | Ohio State -16.5 / Ohio State -9.5 | 53.9 / 48.5 | no edge | no edge | no edge |  |
| Sat 11/14 TBA | Michigan @ Oregon | Michigan 21, Oregon 24 | Oregon 65% | Michigan +185 / Oregon -185 | 19.5 – 24.9 | 7–31 / 12–38 | Oregon -4.8 / Oregon -5.5 | 43.9 / 44.5 | no edge | no edge | no edge |  |
| Sat 11/14 TBA | Minnesota @ Penn State | Minnesota 17, Penn State 24 | Penn State 74% | Minnesota +285 / Penn State -285 | 15.7 – 24.6 | 6–28 / 10–38 | Penn State -8.9 / – | 40.4 / – | no line yet | no line yet (fair: Penn State -285) | no line yet |  |
| Sat 11/14 TBA | Nebraska @ Rutgers | Nebraska 31, Rutgers 17 | Nebraska 83% | Nebraska -495 / Rutgers +495 | 33.9 – 19.8 | 20–49 / 7–34 | Nebraska -14.1 / – | 53.8 / – | no line yet | no line yet (fair: Nebraska -495) | no line yet |  |
| Sat 11/14 TBA | East Carolina @ Charlotte | East Carolina 31, Charlotte 17 | East Carolina 84% | East Carolina -525 / Charlotte +525 | 32.0 – 18.0 | 17–48 / 7–31 | East Carolina -14.0 / – | 50.0 / – | no line yet | no line yet (fair: East Carolina -525) | no line yet |  |
| Sat 11/14 TBA | Florida Atlantic @ Tulsa | Florida Atlantic 31, Tulsa 34 | Tulsa 53% | Florida Atlantic +115 / Tulsa -115 | 31.5 – 32.7 | 17–45 / 17–48 | Tulsa -1.2 / – | 64.2 / – | no line yet | no line yet (fair: Tulsa -115) | no line yet |  |
| Sat 11/14 TBA | North Texas @ UTSA | North Texas 31, UTSA 34 | UTSA 56% | North Texas +125 / UTSA -125 | 33.1 – 34.9 | 18–48 / 20–50 | UTSA -1.8 / – | 68.0 / – | no line yet | no line yet (fair: UTSA -125) | no line yet |  |
| Sat 11/14 TBA | Tulane @ Rice | Tulane 28, Rice 21 | Tulane 69% | Tulane -220 / Rice +220 | 28.5 – 21.6 | 14–42 / 10–35 | Tulane -7.0 / – | 50.1 / – | no line yet | no line yet (fair: Tulane -220) | no line yet |  |
| Sat 11/14 TBA | UAB @ Temple | UAB 24, Temple 27 | Temple 57% | UAB +135 / Temple -135 | 24.2 – 27.0 | 10–38 / 13–41 | Temple -2.8 / – | 51.2 / – | no line yet | no line yet (fair: Temple -135) | no line yet |  |
| Sat 11/14 TBA | Nevada @ Northern Illinois | Nevada 27, Northern Illinois 24 | Nevada 61% | Nevada -155 / Northern Illinois +155 | 26.9 – 23.0 | 13–41 / 10–36 | Nevada -3.9 / – | 49.8 / – | no line yet | no line yet (fair: Nevada -155) | no line yet |  |
| Sat 11/14 TBA | Wyoming @ UTEP | Wyoming 27, UTEP 17 | Wyoming 79% | Wyoming -380 / UTEP +380 | 28.4 – 16.9 | 14–42 / 6–29 | Wyoming -11.5 / – | 45.3 / – | no line yet | no line yet (fair: Wyoming -380) | no line yet |  |
| Sat 11/14 TBA | App State @ Marshall | App State 24, Marshall 31 | Marshall 61% | App State +155 / Marshall -155 | 25.7 – 29.9 | 13–40 / 16–45 | Marshall -4.2 / – | 55.6 / – | no line yet | no line yet (fair: Marshall -155) | no line yet |  |
| Sat 11/14 TBA | Arkansas State @ Coastal Carolina | Arkansas State 24, Coastal Carolina 27 | Coastal Carolina 55% | Arkansas State +120 / Coastal Carolina -120 | 25.4 – 27.2 | 13–40 / 14–41 | Coastal Carolina -1.8 / – | 52.6 / – | no line yet | no line yet (fair: Coastal Carolina -120) | no line yet |  |
| Sat 11/14 TBA | Georgia Southern @ Georgia State | Georgia Southern 28, Georgia State 31 | Georgia State 53% | Georgia Southern +115 / Georgia State -115 | 28.7 – 29.6 | 14–43 / 16–44 | Georgia State -1.0 / – | 58.3 / – | no line yet | no line yet (fair: Georgia State -115) | no line yet |  |
| Sat 11/14 TBA | Southern Miss @ Louisiana Tech | Southern Miss 17, Louisiana Tech 31 | Louisiana Tech 83% | Southern Miss +500 / Louisiana Tech -500 | 18.9 – 32.8 | 7–31 / 17–48 | Louisiana Tech -13.9 / – | 51.8 / – | no line yet | no line yet (fair: Louisiana Tech -500) | no line yet |  |
| Sat 11/14 TBA | Troy @ South Alabama | Troy 24, South Alabama 27 | South Alabama 58% | Troy +140 / South Alabama -140 | 25.8 – 29.0 | 13–40 / 14–44 | South Alabama -3.3 / – | 54.8 / – | no line yet | no line yet (fair: South Alabama -140) | no line yet |  |
| Sat 11/14 12:00 PM | James Madison @ UConn | James Madison 31, UConn 28 | James Madison 51% | James Madison -105 / UConn +105 | 28.4 – 27.9 | 14–42 / 14–42 | James Madison -0.5 / – | 56.3 / – | no line yet | no line yet (fair: James Madison -105) | no line yet |  |
| Sat 11/14 2:00 PM | Kennesaw State @ Sam Houston | Kennesaw State 24, Sam Houston 21 | Kennesaw State 62% | Kennesaw State -165 / Sam Houston +165 | 24.1 – 19.8 | 10–38 / 7–32 | Kennesaw State -4.3 / – | 43.9 / – | no line yet | no line yet (fair: Kennesaw State -165) | no line yet |  |
| Sat 11/14 3:00 PM | New Mexico State @ Missouri State | New Mexico State 24, Missouri State 27 | Missouri State 64% | New Mexico State +175 / Missouri State -175 | 23.1 – 28.7 | 10–37 / 14–43 | Missouri State -5.5 / – | 51.8 / – | no line yet | no line yet (fair: Missouri State -175) | no line yet |  |
| Sat 11/14 3:00 PM | Florida International @ Delaware | Florida International 17, Delaware 31 | Delaware 82% | Florida International +445 / Delaware -445 | 19.3 – 32.2 | 7–31 / 17–48 | Delaware -12.9 / – | 51.8 / – | no line yet | no line yet (fair: Delaware -445) | no line yet |  |
| Sat 11/14 3:30 PM | Boston College @ Notre Dame | Boston College 6, Notre Dame 41 | Notre Dame 100% | Boston College +9900 / Notre Dame -9900 | 6.7 – 40.7 | 0–14 / 27–57 | Notre Dame -34.0 / – | 47.4 / – | no line yet | no line yet (fair: Notre Dame -9900) | no line yet |  |
| Sat 11/14 3:30 PM | Jacksonville State @ Western Kentucky | Jacksonville State 27, Western Kentucky 24 | Jacksonville State 63% | Jacksonville State -170 / Western Kentucky +170 | 29.2 – 24.1 | 15–44 / 10–38 | Jacksonville State -5.1 / – | 53.4 / – | no line yet | no line yet (fair: Jacksonville State -170) | no line yet |  |
| Sat 11/14 3:30 PM | Middle Tennessee @ Liberty | Middle Tennessee 14, Liberty 35 | Liberty 94% | Middle Tennessee +1505 / Liberty -1505 | 13.5 – 34.6 | 3–24 / 20–50 | Liberty -21.1 / – | 48.9 / – | no line yet | no line yet (fair: Liberty -1505) | no line yet |  |
| Sat 11/14 4:00 PM | Fresno State @ Texas State | Fresno State 28, Texas State 31 | Texas State 61% | Fresno State +155 / Texas State -155 | 28.3 – 32.4 | 14–42 / 17–48 | Texas State -4.0 / – | 60.7 / – | no line yet | no line yet (fair: Texas State -155) | no line yet |  |
| Sat 11/14 6:00 PM | Oregon State @ Boise State | Oregon State 31, Boise State 34 | Boise State 62% | Oregon State +160 / Boise State -160 | 28.7 – 33.4 | 14–43 / 20–48 | Boise State -6.8 / Boise State -4.5 | 60.4 / 62.5 | no edge | no edge | no edge |  |
| Sat 11/14 7:00 PM | San José State @ Air Force | San José State 20, Air Force 34 | Air Force 82% | San José State +440 / Air Force -440 | 20.1 – 33.5 | 7–34 / 20–49 | Air Force -13.4 / – | 53.6 / – | no line yet | no line yet (fair: Air Force -440) | no line yet |  |
| Sat 11/14 7:30 PM | UNLV @ New Mexico | UNLV 21, New Mexico 24 | New Mexico 67% | UNLV +200 / New Mexico -200 | 20.4 – 26.7 | 7–34 / 13–41 | New Mexico -6.3 / – | 47.1 / – | no line yet | no line yet (fair: New Mexico -200) | no line yet |  |
| Sat 11/14 9:30 PM | Utah State @ San Diego State | Utah State 21, San Diego State 24 | San Diego State 57% | Utah State +135 / San Diego State -135 | 22.7 – 25.4 | 10–36 / 13–39 | San Diego State -2.7 / – | 48.2 / – | no line yet | no line yet (fair: San Diego State -135) | no line yet |  |
| Sat 11/14 10:30 PM | Colorado State @ Washington State | Colorado State 24, Washington State 31 | Washington State 67% | Colorado State +200 / Washington State -200 | 25.0 – 31.3 | 10–38 / 17–45 | Washington State -6.3 / – | 57.2 / – | no line yet | no line yet (fair: Washington State -200) | no line yet |  |
| Sat 11/14 11:00 PM | North Dakota State @ Hawai'i | North Dakota State 28, Hawai'i 21 | North Dakota State 68% | North Dakota State -215 / Hawai'i +215 | 27.1 – 20.1 | 14–41 / 7–34 | North Dakota State -7.0 / – | 47.2 / – | no line yet | no line yet (fair: North Dakota State -215) | no line yet |  |

## How the 2026 predictions have done

| Predictor | Games | Margin MAE | Total MAE | Team-score MAE | Winners | Brier | 80% range hit |
|---|---|---|---|---|---|---|---|
| Final prediction | 622 | 11.65 | 12.16 | 8.42 | 80.2% | 0.139 | 82.2% |
| Model only (before blending) | 622 | 12.38 | 12.48 | 8.69 | 77.8% | – | – |
| Betting line when predicted | 620 | 11.64 | 12.12 | 8.41 | 80.2% | – | – |

MAE is mean absolute error in points (lower is better). Brier scores the win chances (lower is better, 0.25 is a coin flip). Even the closing betting line misses the final margin of an FBS game by about 12.5 points.

501 of these games were played before the predictor went live. They are backfilled walk-forward (each week predicted from earlier weeks only) but with closing lines, so they flatter the model slightly. Every game since is graded on the prediction logged before kickoff.

### Betting edges

| Market | Edges | Record (W-L-P) | Staked | Units won | ROI | Expected ROI |
|---|---|---|---|---|---|---|
| Spread | 0 | 0-0-0 | 0.0 | +0.00 | – | – |
| Moneyline | 5 | 1-4-0 | 1.7 | +0.25 | +14.1% | +5.1% |
| Total | 2 | 1-1-0 | 2.4 | -0.63 | -26.6% | +4.5% |

2 of these edges were priced at an assumed -110 (price not posted).

Every edge logged before kickoff at the stake and price logged with it (backfilled games, and edges logged before edges were priced from the final prediction, are not included). Units are 1% of the bankroll; ROI is units won per unit staked, pushes returning the stake, and expected ROI is what the edges' EVs promised.

### Week 9 results

| Game | Predicted | Final | Win chance for winner | Inside 80% ranges |
|---|---|---|---|---|
| Delaware @ Western Kentucky | 28–31 | 35–21 | 46% | yes |
| Sam Houston @ Missouri State | 24–27 | 3–24 | 64% | no |
| Kennesaw State @ Middle Tennessee | 27–24 | 44–28 | 53% | no |
| Jacksonville State @ New Mexico State | 27–24 | 24–0 | 59% | no |
| Florida Atlantic @ North Texas | 31–45 | 41–48 | 80% | yes |
| Troy @ James Madison | 17–38 | 24–21 | 9% | yes |
| Tulane @ Charlotte | 28–21 | 38–31 | 73% | yes |
| Baylor @ UCF | 27–24 | 41–9 | 55% | no |
| Kent State @ Sacramento State | 28–21 | 10–31 | 33% | no |
| Arizona @ Texas Tech | 24–27 | 26–34 | 60% | yes |
| California @ NC State | 24–31 | 10–31 | 71% | yes |
| SMU @ Syracuse | 31–24 | 27–30 | 25% | yes |
| Boston College @ Duke | 21–28 | 2–47 | 70% | no |
| Wisconsin @ Iowa | 17–20 | 0–30 | 57% | no |
| Illinois @ Maryland | 27–24 | 20–17 | 56% | yes |
| Notre Dame vs Navy | 42–10 | 35–13 | 98% | yes |
| UAB @ South Florida | 17–24 | 10–30 | 71% | yes |
| Bowling Green @ Western Michigan | 17–31 | 10–23 | 83% | yes |
| Michigan @ Rutgers | 31–14 | 28–21 | 87% | yes |
| Auburn @ Ole Miss | 24–34 | 15–45 | 77% | yes |
| Marshall @ Old Dominion | 24–21 | 36–23 | 58% | yes |
| Kansas State @ Colorado | 21–24 | 24–27 | 56% | yes |
| Coastal Carolina @ Georgia State | 28–31 | 31–20 | 39% | yes |
| UConn @ Air Force | 27–24 | 26–35 | 51% | yes |
| Temple @ East Carolina | 24–27 | 9–17 | 63% | no |
| Louisiana Tech @ South Alabama | 31–24 | 35–20 | 65% | yes |
| Stanford @ Louisville | 17–41 | 24–52 | 94% | yes |
| Florida vs Georgia | 24–34 | 8–27 | 79% | no |
| Arizona State @ BYU | 17–31 | 20–27 | 87% | yes |
| Kansas @ TCU | 21–28 | 16–22 | 64% | yes |
| Minnesota @ Indiana | 10–31 | 16–23 | 94% | yes |
| Northwestern @ Oregon | 24–27 | 26–34 | 60% | yes |
| Colorado State @ Utah State | 27–34 | 14–31 | 69% | yes |
| UTEP @ North Dakota State | 10–34 | 7–31 | 97% | yes |
| Florida International @ Liberty | 17–31 | 10–49 | 84% | no |
| Southern Miss @ UL Monroe | 27–24 | 35–21 | 59% | yes |
| Utah @ Cincinnati | 31–24 | 49–25 | 69% | no |
| Virginia @ Wake Forest | 17–31 | 7–51 | 83% | no |
| New Mexico @ San José State | 31–14 | 21–16 | 86% | yes |
| South Carolina @ Oklahoma | 21–24 | 42–25 | 40% | no |
| Purdue @ Penn State | 21–31 | 17–31 | 75% | yes |
| Nevada @ UCLA | 10–34 | 0–27 | 96% | yes |
| App State @ Georgia Southern | 24–31 | 3–19 | 63% | no |
| Oklahoma State @ Iowa State | 31–24 | 49–51 | 30% | no |
| Clemson @ Florida State | 24–27 | 36–24 | 35% | no |
| Washington State @ San Diego State | 21–24 | 20–26 | 56% | yes |
| Mississippi State @ Texas | 14–35 | 3–31 | 91% | no |
| Georgia Tech @ Pittsburgh | 24–31 | 11–34 | 69% | yes |
| Miami @ North Carolina | 34–17 | 38–35 | 84% | no |
| Ohio State @ USC | 31–24 | 18–30 | 33% | yes |
| Missouri @ Arkansas | 27–20 | 34–10 | 76% | yes |
| Washington @ Nebraska | 21–28 | 17–10 | 29% | no |
| Army @ Memphis | 24–31 | 22–49 | 65% | no |
| Texas State @ Boise State | 28–38 | 45–46 | 76% | no |
| Northern Illinois @ UNLV | 17–38 | 24–31 | 93% | yes |
| Oregon State @ Fresno State | 31–24 | 22–38 | 35% | yes |

## FBS power ratings

Points per game better than an average FBS team on a neutral field, from opponent-adjusted EPA (garbage time removed) with this season's games weighted against a preseason prior, plus the weight the margin model puts on Elo (a rating built from game results alone). Defense is positive when it holds opponents below average.

| # | Team | Conference | Net | Offense | Defense | Special teams | Results (Elo) | Elo rating |
|---|---|---|---|---|---|---|---|---|
| 1 | LSU | SEC | +26.4 | +10.8 | +12.5 | +0.2 | +2.9 | 1751 |
| 2 | Ohio State | Big Ten | +25.7 | +10.8 | +10.3 | +0.3 | +4.3 | 1868 |
| 3 | Georgia | SEC | +23.9 | +7.9 | +10.6 | +0.8 | +4.5 | 1880 |
| 4 | Notre Dame | FBS Independents | +23.1 | +8.8 | +9.1 | +1.0 | +4.2 | 1858 |
| 5 | Miami | ACC | +23.0 | +14.2 | +3.8 | +0.4 | +4.7 | 1894 |
| 6 | Indiana | Big Ten | +21.7 | +5.7 | +10.6 | +0.2 | +5.2 | 1939 |
| 7 | Utah | Big 12 | +20.3 | +10.6 | +5.7 | -0.0 | +4.0 | 1842 |
| 8 | Alabama | SEC | +19.7 | +9.0 | +7.1 | +0.3 | +3.2 | 1777 |
| 9 | Ole Miss | SEC | +18.5 | +10.4 | +3.7 | +0.7 | +3.7 | 1815 |
| 10 | Texas | SEC | +18.3 | +1.7 | +12.4 | +0.5 | +3.7 | 1814 |
| 11 | Texas Tech | Big 12 | +18.2 | +2.1 | +11.9 | +1.2 | +3.0 | 1761 |
| 12 | Oregon | Big Ten | +16.7 | +4.5 | +9.0 | +0.4 | +2.8 | 1743 |
| 13 | UCLA | Big Ten | +16.6 | +4.6 | +9.3 | +0.7 | +2.0 | 1676 |
| 14 | Wake Forest | ACC | +16.1 | +6.0 | +7.2 | +0.4 | +2.4 | 1710 |
| 15 | Missouri | SEC | +16.1 | +4.5 | +8.4 | +0.7 | +2.5 | 1714 |
| 16 | Tennessee | SEC | +15.8 | +3.7 | +8.5 | +1.0 | +2.6 | 1723 |
| 17 | Louisville | ACC | +15.0 | +9.4 | +3.5 | +0.1 | +2.1 | 1681 |
| 18 | Michigan | Big Ten | +14.8 | +3.4 | +9.3 | +0.1 | +2.0 | 1674 |
| 19 | Oklahoma | SEC | +14.4 | +0.2 | +12.3 | +0.6 | +1.3 | 1615 |
| 20 | USC | Big Ten | +13.9 | +10.6 | +0.3 | +0.3 | +2.8 | 1738 |
| 21 | BYU | Big 12 | +13.4 | +5.6 | +4.2 | +0.6 | +3.0 | 1759 |
| 22 | Iowa | Big Ten | +13.1 | +1.6 | +7.8 | +0.8 | +2.9 | 1751 |
| 23 | SMU | ACC | +13.0 | +7.3 | +3.6 | +0.1 | +2.0 | 1675 |
| 24 | Nebraska | Big Ten | +12.8 | +3.5 | +7.9 | +0.5 | +0.9 | 1587 |
| 25 | Florida | SEC | +12.6 | +6.6 | +4.2 | +0.9 | +0.8 | 1579 |
| 26 | Auburn | SEC | +12.1 | +5.5 | +5.6 | +0.6 | +0.3 | 1536 |
| 27 | Texas A&M | SEC | +12.0 | +2.6 | +7.8 | +0.5 | +1.1 | 1601 |
| 28 | Arizona | Big 12 | +12.0 | +6.2 | +3.6 | -0.2 | +2.4 | 1708 |
| 29 | South Carolina | SEC | +11.6 | +5.5 | +3.8 | +0.5 | +1.8 | 1662 |
| 30 | Penn State | Big Ten | +11.4 | +3.0 | +7.0 | +0.1 | +1.2 | 1611 |
| 31 | Northwestern | Big Ten | +11.2 | +7.1 | +1.9 | +0.8 | +1.5 | 1634 |
| 32 | Houston | Big 12 | +10.2 | +7.9 | +0.1 | +0.2 | +2.0 | 1673 |
| 33 | Kansas State | Big 12 | +9.8 | +6.2 | +3.0 | +0.3 | +0.2 | 1526 |
| 34 | Kentucky | SEC | +9.6 | +2.8 | +4.5 | +0.3 | +2.0 | 1677 |
| 35 | Mississippi State | SEC | +9.4 | +5.8 | +3.3 | +0.2 | +0.0 | 1512 |
| 36 | Baylor | Big 12 | +9.3 | +0.3 | +6.8 | +1.0 | +1.1 | 1601 |
| 37 | Washington | Big Ten | +9.2 | +1.9 | +5.3 | +0.1 | +2.0 | 1670 |
| 38 | Wisconsin | Big Ten | +8.1 | -0.2 | +7.0 | +0.3 | +1.0 | 1593 |
| 39 | Kansas | Big 12 | +7.2 | +4.6 | +3.4 | -0.0 | -0.8 | 1439 |
| 40 | Duke | ACC | +6.9 | +2.7 | +1.4 | +0.9 | +2.0 | 1677 |
| 41 | Oklahoma State | Big 12 | +6.7 | +8.5 | -1.9 | +0.4 | -0.3 | 1484 |
| 42 | Iowa State | Big 12 | +6.6 | +3.9 | +1.1 | +1.0 | +0.7 | 1563 |
| 43 | Boise State | Pac-12 | +6.3 | +4.8 | -1.0 | -0.1 | +2.6 | 1721 |
| 44 | Cincinnati | Big 12 | +6.3 | +9.0 | -3.8 | +0.3 | +0.7 | 1568 |
| 45 | Arizona State | Big 12 | +5.5 | +1.0 | +4.0 | +0.0 | +0.5 | 1550 |
| 46 | TCU | Big 12 | +5.4 | -2.3 | +6.4 | +0.5 | +0.9 | 1587 |
| 47 | Virginia Tech | ACC | +4.9 | +3.4 | +0.5 | +0.3 | +0.7 | 1566 |
| 48 | Florida State | ACC | +4.8 | +7.2 | -1.4 | -0.5 | -0.6 | 1462 |
| 49 | Illinois | Big Ten | +4.8 | +6.0 | -2.5 | +0.1 | +1.2 | 1610 |
| 50 | Clemson | ACC | +4.7 | -4.9 | +7.6 | +0.8 | +1.3 | 1613 |
| 51 | Vanderbilt | SEC | +4.4 | +4.5 | -0.6 | +0.2 | +0.2 | 1529 |
| 52 | Minnesota | Big Ten | +4.1 | -4.0 | +6.4 | +1.1 | +0.6 | 1561 |
| 53 | Pittsburgh | ACC | +4.0 | -1.2 | +3.9 | +0.6 | +0.7 | 1566 |
| 54 | North Texas | American Athletic | +3.5 | +10.2 | -7.5 | -0.9 | +1.6 | 1645 |
| 55 | NC State | ACC | +3.2 | +5.5 | -2.1 | -0.6 | +0.4 | 1538 |
| 56 | Colorado | Big 12 | +2.9 | +0.5 | +4.7 | -0.7 | -1.6 | 1378 |
| 57 | UCF | Big 12 | +2.8 | +0.7 | +2.7 | +0.0 | -0.6 | 1459 |
| 58 | North Carolina | ACC | +2.4 | +3.3 | -1.7 | +0.8 | +0.0 | 1509 |
| 59 | Syracuse | ACC | +2.2 | +1.7 | +2.5 | -0.8 | -1.2 | 1407 |
| 60 | UTSA | American Athletic | +2.0 | +2.9 | -3.0 | -0.1 | +2.1 | 1686 |
| 61 | Memphis | American Athletic | +2.0 | +3.5 | -2.3 | -0.4 | +1.3 | 1614 |
| 62 | James Madison | Sun Belt | +2.0 | -1.7 | +1.0 | +0.4 | +2.3 | 1698 |
| 63 | Oregon State | Pac-12 | +1.8 | +4.6 | -2.4 | +0.1 | -0.5 | 1468 |
| 64 | Virginia | ACC | +1.0 | -1.3 | +3.0 | -0.5 | -0.2 | 1494 |
| 65 | Liberty | Conference USA | +1.0 | +0.7 | -0.5 | +0.3 | +0.5 | 1551 |
| 66 | Purdue | Big Ten | +0.7 | +3.0 | -2.1 | +0.8 | -1.0 | 1426 |
| 67 | Arkansas | SEC | +0.4 | +1.2 | +0.3 | -0.7 | -0.5 | 1468 |
| 68 | Maryland | Big Ten | +0.2 | -1.5 | +3.0 | +0.8 | -2.1 | 1334 |
| 69 | West Virginia | Big 12 | -0.1 | +3.9 | -4.5 | +0.6 | -0.1 | 1502 |
| 70 | Toledo | Mid-American | -0.2 | -1.2 | +0.6 | -0.2 | +0.6 | 1555 |
| 71 | Texas State | Pac-12 | -0.2 | +5.8 | -5.4 | -1.2 | +0.7 | 1563 |
| 72 | New Mexico | Mountain West | -1.0 | -4.1 | +2.0 | -0.2 | +1.3 | 1618 |
| 73 | Navy | American Athletic | -1.2 | +3.6 | -3.9 | -0.5 | -0.4 | 1473 |
| 74 | South Florida | American Athletic | -1.3 | -2.3 | -0.2 | +0.2 | +1.0 | 1593 |
| 75 | North Dakota State | Mountain West | -1.6 | -5.1 | +3.5 | +1.1 | -1.1 | 1419 |
| 76 | UConn | FBS Independents | -1.8 | +2.3 | -3.5 | -0.2 | -0.4 | 1472 |
| 77 | Fresno State | Pac-12 | -2.8 | -2.3 | -1.0 | -0.2 | +0.8 | 1574 |
| 78 | Louisiana Tech | Sun Belt | -2.9 | -3.1 | +0.6 | -0.8 | +0.4 | 1540 |
| 79 | Army | American Athletic | -2.9 | +5.3 | -8.7 | -0.1 | +0.6 | 1554 |
| 80 | Ohio | Mid-American | -3.4 | -1.8 | -3.0 | +0.5 | +0.8 | 1578 |
| 81 | East Carolina | American Athletic | -3.5 | -5.3 | +2.6 | -0.7 | -0.1 | 1496 |
| 82 | Michigan State | Big Ten | -3.5 | -3.5 | +1.1 | +0.3 | -1.5 | 1388 |
| 83 | Tulsa | American Athletic | -3.8 | -1.0 | -0.3 | -0.7 | -1.8 | 1358 |
| 84 | Florida Atlantic | American Athletic | -3.9 | +3.9 | -7.4 | +0.7 | -1.1 | 1416 |
| 85 | Rutgers | Big Ten | -4.2 | +2.8 | -6.3 | +0.8 | -1.4 | 1388 |
| 86 | Tulane | American Athletic | -4.4 | -3.7 | -1.6 | +0.2 | +0.6 | 1562 |
| 87 | Georgia Tech | ACC | -4.8 | +1.1 | -4.4 | -0.1 | -1.4 | 1393 |
| 88 | Jacksonville State | Conference USA | -4.8 | -0.1 | -4.5 | -0.1 | -0.1 | 1497 |
| 89 | Air Force | Mountain West | -4.8 | +2.4 | -6.8 | -0.2 | -0.2 | 1488 |
| 90 | UNLV | Mountain West | -5.1 | -2.6 | -3.0 | +0.1 | +0.4 | 1543 |
| 91 | Boston College | ACC | -5.3 | -3.6 | -0.4 | -0.8 | -0.5 | 1469 |
| 92 | California | ACC | -6.1 | -2.1 | -1.9 | -0.4 | -1.7 | 1369 |
| 93 | Delaware | Conference USA | -6.4 | -0.2 | -5.2 | +0.3 | -1.2 | 1406 |
| 94 | Utah State | Pac-12 | -6.9 | -6.6 | +2.1 | -1.2 | -1.2 | 1412 |
| 95 | Western Michigan | Mid-American | -7.0 | -4.8 | -3.6 | +0.8 | +0.6 | 1561 |
| 96 | Marshall | Sun Belt | -7.3 | -3.6 | -3.7 | +0.2 | -0.1 | 1500 |
| 97 | Miami (OH) | Mid-American | -8.0 | -4.5 | -3.3 | +0.6 | -0.8 | 1446 |
| 98 | Washington State | Pac-12 | -8.1 | -6.0 | +0.1 | -0.4 | -1.9 | 1349 |
| 99 | Georgia Southern | Sun Belt | -8.1 | -2.1 | -5.2 | -0.9 | +0.1 | 1513 |
| 100 | San Diego State | Pac-12 | -8.2 | -4.6 | -2.6 | +0.3 | -1.2 | 1406 |
| 101 | App State | Sun Belt | -8.5 | -3.9 | -3.3 | -0.3 | -1.0 | 1422 |
| 102 | Stanford | ACC | -8.7 | -2.7 | -5.3 | -0.1 | -0.7 | 1448 |
| 103 | Louisiana | Sun Belt | -9.4 | -4.9 | -4.0 | -0.1 | -0.4 | 1478 |
| 104 | Temple | American Athletic | -9.6 | +0.6 | -7.1 | -0.5 | -2.6 | 1291 |
| 105 | UAB | American Athletic | -9.9 | -5.8 | -2.5 | -0.4 | -1.2 | 1407 |
| 106 | Georgia State | Sun Belt | -10.3 | -0.9 | -7.2 | -0.3 | -2.0 | 1347 |
| 107 | Arkansas State | Sun Belt | -10.4 | -2.7 | -6.9 | +0.1 | -0.8 | 1441 |
| 108 | Hawai'i | Mountain West | -11.0 | -4.0 | -6.3 | +1.0 | -1.7 | 1365 |
| 109 | Troy | Sun Belt | -11.1 | -7.9 | -0.5 | -1.3 | -1.3 | 1401 |
| 110 | Wyoming | Mountain West | -11.2 | -6.4 | -3.4 | -0.2 | -1.1 | 1413 |
| 111 | Coastal Carolina | Sun Belt | -11.5 | -5.8 | -4.7 | +0.5 | -1.5 | 1384 |
| 112 | South Alabama | Sun Belt | -11.9 | -0.2 | -10.6 | +0.3 | -1.3 | 1398 |
| 113 | Colorado State | Pac-12 | -11.9 | +3.2 | -12.1 | -0.3 | -2.7 | 1286 |
| 114 | Western Kentucky | Conference USA | -12.2 | -6.7 | -3.2 | -0.4 | -2.0 | 1345 |
| 115 | Rice | American Athletic | -12.8 | -3.6 | -5.2 | -0.8 | -3.2 | 1246 |
| 116 | Kennesaw State | Conference USA | -12.8 | -6.5 | -3.5 | -0.8 | -2.0 | 1346 |
| 117 | Old Dominion | Sun Belt | -13.1 | -13.0 | +3.4 | -1.6 | -1.8 | 1357 |
| 118 | Missouri State | Conference USA | -13.2 | -1.6 | -7.5 | -1.5 | -2.7 | 1281 |
| 119 | Nevada | Mountain West | -13.3 | -9.6 | -1.8 | +0.3 | -2.2 | 1327 |
| 120 | Central Michigan | Mid-American | -13.8 | -7.2 | -4.8 | -0.1 | -1.6 | 1375 |
| 121 | Southern Miss | Sun Belt | -13.9 | -7.3 | -3.3 | -1.1 | -2.1 | 1331 |
| 122 | Florida International | Conference USA | -15.1 | -10.0 | -1.9 | -1.4 | -1.9 | 1353 |
| 123 | New Mexico State | Conference USA | -15.8 | -8.4 | -2.6 | -1.9 | -2.8 | 1275 |
| 124 | San José State | Mountain West | -15.8 | -9.8 | -3.4 | -0.1 | -2.5 | 1303 |
| 125 | Ball State | Mid-American | -16.7 | -5.5 | -7.2 | -0.9 | -3.1 | 1251 |
| 126 | Eastern Michigan | Mid-American | -17.1 | -7.4 | -6.9 | -0.6 | -2.2 | 1330 |
| 127 | Massachusetts | Mid-American | -17.2 | -9.3 | -4.4 | -0.0 | -3.5 | 1219 |
| 128 | Middle Tennessee | Conference USA | -17.3 | -7.1 | -7.3 | +0.1 | -3.0 | 1257 |
| 129 | UL Monroe | Sun Belt | -18.1 | -6.3 | -6.2 | -1.4 | -4.1 | 1168 |
| 130 | Buffalo | Mid-American | -18.2 | -12.6 | -5.4 | +0.6 | -0.8 | 1444 |
| 131 | Northern Illinois | Mountain West | -18.3 | -3.6 | -9.3 | -1.1 | -4.4 | 1145 |
| 132 | Bowling Green | Mid-American | -18.6 | -11.7 | -4.1 | -0.0 | -2.9 | 1270 |
| 133 | Sam Houston | Conference USA | -19.1 | -12.5 | -0.9 | -1.3 | -4.4 | 1145 |
| 134 | Charlotte | American Athletic | -20.2 | -6.9 | -9.2 | -0.5 | -3.7 | 1203 |
| 135 | Sacramento State | Mid-American | -20.4 | -11.0 | -5.3 | +0.2 | -4.3 | 1151 |
| 136 | Kent State | Mid-American | -20.7 | -10.8 | -5.9 | -0.8 | -3.2 | 1241 |
| 137 | Akron | Mid-American | -22.6 | -9.9 | -8.0 | -1.1 | -3.7 | 1205 |
| 138 | UTEP | Mountain West | -24.1 | -11.6 | -6.5 | -1.3 | -4.8 | 1112 |

## Current model fit

- Fitted on 4239 games from seasons 2022–2026.
- Home field on top of the ratings: 3.3 points (1.9 in conference games).
- Extra FBS edge over FCS opponents beyond their ratings: 14.1 points.
- Elo weight: 0.19 points of margin per point of Elo spread.
- Weight on the betting line: 91% for the margin, 81% for the total.
