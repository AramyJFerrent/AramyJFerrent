# College football score predictions

Updated Sun Nov 01, 2026 01:30 PM ET. Refreshed automatically every day of the season and several times on Saturdays; each game's prediction is locked at kickoff and graded once the final score is in. Scores are the most likely real scoreline near the expected points; ranges cover 80% of simulated outcomes for each team. College scores scatter widely, so read the ranges, not just the headline score.

Expected points blend the model with the betting line using the weight that has predicted best in recent seasons (see Current model fit). The spread and total columns show the model's own numbers next to the line, so you can see where it disagrees. Games without a line yet use the model alone.

The fair moneyline is the American odds that match the win chance exactly, with no bookmaker margin: -200 means risk $200 to win $100, +200 means risk $100 to win $200. A sportsbook's price will be a little worse on both sides because of its cut, so a book only offers value on a team when its price beats the fair line.

The edge columns judge each bet by its expected value per $1 staked at the posted price, using the final prediction: the model blended with the line, run through the score simulator, pushes included, and anchored to the market's own chances so that only what the blend moves off the line counts. The model's own spread and total (shown alongside) sit several points from the line in most games, but the blend keeps only the share of that disagreement the model has earned in past seasons, so edges are rare. The side with the higher value is shown when it reaches 3% (+3 cents per $1), as the team or side, the price, the expected value, its chance of winning the bet and its stake, a 25% share of the Kelly stake in units of 1% of the bankroll with at most 3 units on one game; anything short is no edge. Where a book posts no price for a spread or total it is assumed to be -110 and marked -110*; moneylines are never assumed. In the walk-forward backtest against closing lines, edges returned spread -100.0% on 1 bets (posted prices, 2016–2019); spread -3.9% on 156 bets (assumed -110 prices, 2016–2025); moneyline +13.7% on 575 bets (posted prices, 2016–2025); total +2.6% on 367 bets (posted prices, 2016–2019); total -5.7% on 172 bets (assumed -110 prices, 2016–2025). None of these is clearly above zero, so treat these edges as an experiment, not a betting system. The live record is tracked below, graded at the price logged with the last prediction before kickoff.

## 2026 Week 10

| Kickoff (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected points | 80% range | Spread: model / line | Total: model / line | Spread edge | Moneyline edge | Total edge | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tue 11/03 7:00 PM | Ohio @ Akron | Ohio 31, Akron 17 | Ohio 82% | Ohio -445 / Akron +445 | 30.9 – 17.9 | 17–45 / 7–31 | Ohio -18.3 / Ohio -12.5 | 50.0 / 48.5 | no edge | no edge | no edge |  |
| Tue 11/03 8:00 PM | Buffalo @ Miami (OH) | Buffalo 17, Miami (OH) 24 | Miami (OH) 69% | Buffalo +220 / Miami (OH) -220 | 19.0 – 26.0 | 7–31 / 13–40 | Miami (OH) -12.7 / Miami (OH) -6.5 | 48.5 / 44.5 | no edge | no edge | no edge |  |
| Wed 11/04 7:00 PM | Ball State @ Massachusetts | Ball State 24, Massachusetts 27 | Massachusetts 61% | Ball State +160 / Massachusetts -160 | 22.4 – 26.3 | 10–35 / 13–41 | Massachusetts -3.0 / Massachusetts -4.0 | 49.1 / 48.5 | no edge | no edge | no edge |  |
| Wed 11/04 7:00 PM | Toledo @ Sacramento State | Toledo 38, Sacramento State 10 | Toledo 97% | Toledo -3460 / Sacramento State +3460 | 38.9 – 12.3 | 24–55 / 3–23 | Toledo -17.7 / Toledo -27.5 | 50.1 / 51.5 | no edge | Sacramento State (+1700): EV +4.5%, 6%, stake 0.1u | no edge |  |
| Wed 11/04 7:30 PM | Central Michigan vs Eastern Michigan | Central Michigan 21, Eastern Michigan 24 | Eastern Michigan 52% | Central Michigan +110 / Eastern Michigan -110 | 22.2 – 23.3 | 10–35 / 10–37 | Central Michigan -3.6 / Eastern Michigan -1.5 | 49.9 / 44.5 | no edge | no edge | no edge | neutral site |
| Thu 11/05 7:30 PM | UTSA @ Florida Atlantic | UTSA 38, Florida Atlantic 31 | UTSA 66% | UTSA -195 / Florida Atlantic +195 | 39.0 – 32.4 | 24–55 / 17–48 | UTSA -2.5 / UTSA -7.0 | 66.6 / 72.5 | no edge | no edge | no edge |  |
| Thu 11/05 8:00 PM | James Madison @ Southern Miss | James Madison 34, Southern Miss 17 | James Madison 84% | James Madison -525 / Southern Miss +525 | 34.9 – 20.3 | 20–51 / 7–34 | James Madison -14.9 / James Madison -14.5 | 53.9 / 55.5 | no edge | no edge | no edge |  |
| Fri 11/06 7:00 PM | Virginia Tech @ SMU | Virginia Tech 24, SMU 31 | SMU 67% | Virginia Tech +205 / SMU -205 | 24.7 – 31.6 | 12–38 / 17–47 | SMU -10.8 / SMU -6.5 | 55.2 / 56.5 | no edge | no edge | no edge |  |
| Fri 11/06 7:30 PM | South Florida @ East Carolina | South Florida 24, East Carolina 21 | South Florida 54% | South Florida -120 / East Carolina +120 | 22.5 – 21.0 | 10–36 / 9–34 | South Florida -0.8 / South Florida -1.5 | 47.6 / 42.5 | no edge | no edge | no edge |  |
| Fri 11/06 8:00 PM | Nebraska @ Illinois | Nebraska 28, Illinois 21 | Nebraska 65% | Nebraska -185 / Illinois +185 | 27.6 – 21.9 | 14–42 / 10–35 | Nebraska -7.1 / Nebraska -5.5 | 53.9 / 48.5 | no edge | no edge | no edge |  |
| Fri 11/06 9:00 PM | New Mexico @ Nevada | New Mexico 28, Nevada 14 | New Mexico 82% | New Mexico -455 / Nevada +455 | 27.3 – 15.1 | 14–42 / 3–27 | New Mexico -9.9 / New Mexico -12.5 | 42.1 / 42.5 | no edge | no edge | no edge |  |
| Fri 11/06 10:15 PM | TCU @ Arizona | TCU 20, Arizona 27 | Arizona 73% | TCU +270 / Arizona -270 | 18.4 – 26.9 | 7–31 / 14–41 | Arizona -8.4 / Arizona -8.5 | 49.0 / 44.5 | no edge | no edge | no edge |  |
| Sat 11/07 TBA | Cincinnati @ Houston | Cincinnati 28, Houston 38 | Houston 76% | Cincinnati +310 / Houston -310 | 26.2 – 36.4 | 13–41 / 21–52 | Houston -6.3 / Houston -10.5 | 63.1 / 62.5 | no edge | no edge | no edge |  |
| Sat 11/07 TBA | Iowa State @ Baylor | Iowa State 21, Baylor 31 | Baylor 73% | Iowa State +270 / Baylor -270 | 21.3 – 30.5 | 9–34 / 17–45 | Baylor -5.3 / Baylor -9.5 | 53.0 / 51.5 | no edge | no edge | no edge |  |
| Sat 11/07 TBA | Michigan State @ Michigan | Michigan State 14, Michigan 28 | Michigan 84% | Michigan State +530 / Michigan -530 | 13.4 – 26.6 | 3–24 / 13–41 | Michigan -20.8 / Michigan -12.5 | 42.3 / 39.5 | no edge | no edge | no edge |  |
| Sat 11/07 TBA | UCLA @ Minnesota | UCLA 24, Minnesota 17 | UCLA 69% | UCLA -220 / Minnesota +220 | 22.8 – 16.0 | 10–36 / 6–28 | UCLA -9.7 / UCLA -6.5 | 40.4 / 38.5 | no edge | no edge | no edge |  |
| Sat 11/07 TBA | Iowa @ Northwestern | Iowa 21, Northwestern 24 | Northwestern 54% | Iowa +120 / Northwestern -120 | 21.2 – 22.6 | 9–34 / 10–36 | Northwestern -0.6 / Northwestern -1.5 | 49.4 / 42.5 | no edge | no edge | no edge |  |
| Sat 11/07 TBA | Penn State @ Washington | Penn State 21, Washington 24 | Washington 55% | Penn State +125 / Washington -125 | 20.9 – 23.2 | 9–34 / 10–37 | Penn State -0.1 / Washington -2.5 | 46.6 / 43.5 | no edge | no edge | no edge |  |
| Sat 11/07 12:00 PM | Texas @ Missouri | Texas 24, Missouri 21 | Texas 58% | Texas -140 / Missouri +140 | 24.5 – 21.4 | 10–38 / 10–34 | Missouri -0.9 / Texas -3.5 | 43.3 / 46.5 | no edge | no edge | no edge |  |
| Sat 11/07 12:00 PM | BYU @ Utah | BYU 21, Utah 28 | Utah 66% | BYU +190 / Utah -190 | 20.6 – 26.4 | 9–34 / 13–41 | Utah -9.0 / Utah -5.5 | 53.6 / 45.5 | no edge | no edge | Over 45.5 (-110*): EV +4.2%, 55%, stake 1.2u | * price not posted; assumed -110 |
| Sat 11/07 12:00 PM | Oklahoma State @ Kansas State | Oklahoma State 31, Kansas State 28 | Oklahoma State 63% | Oklahoma State -175 / Kansas State +175 | 32.5 – 27.5 | 17–48 / 14–42 | Kansas State -5.4 / Oklahoma State -6.0 | 60.5 / 60.5 | no edge | no edge | no edge |  |
| Sat 11/07 12:00 PM | Clemson @ Syracuse | Clemson 27, Syracuse 24 | Clemson 54% | Clemson -120 / Syracuse +120 | 25.4 – 23.8 | 13–38 / 10–38 | Clemson -2.2 / Clemson -1.5 | 47.9 / 49.5 | no edge | no edge | no edge |  |
| Sat 11/07 12:00 PM | Florida State @ Boston College | Florida State 31, Boston College 24 | Florida State 68% | Florida State -210 / Boston College +210 | 29.3 – 22.7 | 15–44 / 10–37 | Florida State -7.8 / Florida State -6.5 | 53.9 / 51.5 | no edge | no edge | no edge |  |
| Sat 11/07 12:00 PM | North Carolina @ UConn | North Carolina 31, UConn 24 | North Carolina 70% | North Carolina -235 / UConn +235 | 30.7 – 22.9 | 17–45 / 10–36 | North Carolina -1.4 / North Carolina -8.5 | 58.2 / 52.5 | no edge | no edge | no edge |  |
| Sat 11/07 12:00 PM | Tulsa @ Tulane | Tulsa 24, Tulane 21 | Tulsa 57% | Tulsa -130 / Tulane +130 | 25.9 – 23.4 | 13–40 / 10–37 | Tulane -2.4 / Tulsa -3.0 | 52.4 / 48.5 | no edge | no edge | no edge |  |
| Sat 11/07 12:30 PM | Duke @ NC State | Duke 27, NC State 24 | Duke 66% | Duke -190 / NC State +190 | 28.6 – 22.9 | 14–42 / 10–37 | Duke -2.4 / Duke -6.0 | 56.1 / 50.5 | no edge | no edge | no edge |  |
| Sat 11/07 12:30 PM | Maryland @ Purdue | Maryland 24, Purdue 31 | Purdue 66% | Maryland +190 / Purdue -190 | 25.1 – 31.3 | 13–38 / 17–46 | Purdue -2.4 / Purdue -6.5 | 51.9 / 57.5 | no edge | no edge | no edge |  |
| Sat 11/07 12:30 PM | Rutgers @ Wisconsin | Rutgers 14, Wisconsin 31 | Wisconsin 87% | Rutgers +700 / Wisconsin -700 | 15.5 – 31.8 | 6–27 / 17–47 | Wisconsin -14.2 / Wisconsin -16.5 | 50.2 / 46.5 | no edge | no edge | no edge |  |
| Sat 11/07 12:45 PM | Arkansas @ Auburn | Arkansas 21, Auburn 31 | Auburn 78% | Arkansas +355 / Auburn -355 | 20.1 – 31.1 | 7–34 / 17–46 | Auburn -15.7 / Auburn -10.5 | 54.0 / 50.5 | no edge | no edge | no edge |  |
| Sat 11/07 1:00 PM | Old Dominion @ Coastal Carolina | Old Dominion 17, Coastal Carolina 24 | Coastal Carolina 68% | Old Dominion +215 / Coastal Carolina -215 | 19.1 – 26.1 | 7–31 / 13–41 | Coastal Carolina -6.1 / Coastal Carolina -7.0 | 44.0 / 45.5 | no edge | no edge | no edge |  |
| Sat 11/07 2:30 PM | Georgia State @ App State | Georgia State 28, App State 31 | App State 60% | Georgia State +150 / App State -150 | 26.9 – 30.5 | 14–41 / 17–45 | App State -4.6 / App State -3.5 | 57.4 / 57.5 | no edge | no edge | no edge |  |
| Sat 11/07 3:00 PM | Texas A&M @ South Carolina | Texas A&M 24, South Carolina 27 | South Carolina 68% | Texas A&M +210 / South Carolina -210 | 22.2 – 28.9 | 10–35 / 14–44 | South Carolina -2.7 / South Carolina -7.0 | 49.5 / 51.5 | no edge | no edge | no edge |  |
| Sat 11/07 3:00 PM | UL Monroe @ Arkansas State | UL Monroe 17, Arkansas State 31 | Arkansas State 84% | UL Monroe +520 / Arkansas State -520 | 18.8 – 33.1 | 7–31 / 18–48 | Arkansas State -12.5 / Arkansas State -14.5 | 53.4 / 51.5 | no edge | no edge | no edge |  |
| Sat 11/07 3:00 PM | Delaware @ Kennesaw State | Delaware 27, Kennesaw State 24 | Delaware 58% | Delaware -140 / Kennesaw State +140 | 27.5 – 24.8 | 14–42 / 10–38 | Delaware -5.0 / Delaware -2.5 | 55.4 / 51.5 | no edge | no edge | no edge |  |
| Sat 11/07 3:30 PM | Alabama @ LSU | Alabama 24, LSU 27 | LSU 64% | Alabama +180 / LSU -180 | 23.6 – 28.5 | 10–37 / 14–42 | LSU -9.3 / LSU -4.5 | 50.6 / 52.5 | no edge | no edge | no edge |  |
| Sat 11/07 3:30 PM | Merrimack @ Wake Forest | Merrimack 3, Wake Forest 62 | Wake Forest 100% | Merrimack +9900 / Wake Forest -9900 | 3.0 – 61.0 | 0–7 / 48–75 | Wake Forest -58.0 / – | 64.0 / – | no line yet | no line yet (fair: Wake Forest -9900) | no line yet | FCS opponent |
| Sat 11/07 3:30 PM | Oregon @ Ohio State | Oregon 17, Ohio State 27 | Ohio State 75% | Oregon +305 / Ohio State -305 | 19.1 – 28.7 | 7–31 / 14–44 | Ohio State -11.3 / Ohio State -9.5 | 49.2 / 47.5 | no edge | no edge | no edge |  |
| Sat 11/07 3:30 PM | Charlotte @ UAB | Charlotte 21, UAB 31 | UAB 78% | Charlotte +355 / UAB -355 | 20.3 – 31.0 | 7–34 / 17–45 | UAB -12.9 / UAB -10.5 | 50.1 / 51.5 | no edge | no edge | no edge |  |
| Sat 11/07 3:30 PM | Temple @ Navy | Temple 24, Navy 31 | Navy 69% | Temple +230 / Navy -230 | 22.6 – 30.4 | 10–36 / 16–45 | Navy -10.7 / Navy -7.5 | 55.5 / 52.5 | no edge | no edge | no edge |  |
| Sat 11/07 3:30 PM | Marshall @ Georgia Southern | Marshall 24, Georgia Southern 31 | Georgia Southern 70% | Marshall +230 / Georgia Southern -230 | 23.1 – 31.0 | 10–37 / 17–45 | Georgia Southern -1.0 / Georgia Southern -8.5 | 56.7 / 53.5 | no edge | Marshall (+250): EV +3.9%, 30%, stake 0.4u | no edge |  |
| Sat 11/07 3:30 PM | Western Kentucky @ Middle Tennessee | Western Kentucky 24, Middle Tennessee 27 | Middle Tennessee 53% | Western Kentucky +110 / Middle Tennessee -110 | 25.5 – 26.7 | 13–39 / 13–41 | Western Kentucky -2.2 / Middle Tennessee -1.5 | 50.8 / 52.5 | no edge | no edge | no edge |  |
| Sat 11/07 3:45 PM | UCF @ Kansas | UCF 21, Kansas 24 | Kansas 59% | UCF +140 / Kansas -140 | 22.8 – 26.1 | 10–37 / 13–41 | Kansas -6.9 / Kansas -3.0 | 52.0 / 48.5 | no edge | no edge | no edge |  |
| Sat 11/07 4:00 PM | Rice @ North Texas | Rice 24, North Texas 41 | North Texas 86% | Rice +635 / North Texas -635 | 23.8 – 40.5 | 10–38 / 25–56 | North Texas -19.0 / North Texas -16.5 | 63.3 / 64.5 | no edge | no edge | no edge |  |
| Sat 11/07 4:00 PM | Northern Illinois @ San José State | Northern Illinois 24, San José State 31 | San José State 64% | Northern Illinois +175 / San José State -175 | 23.6 – 29.1 | 10–38 / 15–43 | San José State -5.5 / – | 52.6 / – | no line yet | no line yet (fair: San José State -175) | no line yet |  |
| Sat 11/07 4:00 PM | Missouri State @ Florida International | Missouri State 24, Florida International 27 | Florida International 64% | Missouri State +175 / Florida International -175 | 22.3 – 27.4 | 10–35 / 14–42 | Florida International -1.0 / Florida International -5.5 | 50.5 / 49.5 | no edge | no edge | no edge |  |
| Sat 11/07 4:00 PM | Louisiana Tech @ Troy | Louisiana Tech 24, Troy 17 | Louisiana Tech 67% | Louisiana Tech -205 / Troy +205 | 26.0 – 19.6 | 13–40 / 7–32 | Louisiana Tech -6.2 / Louisiana Tech -6.5 | 46.1 / 45.5 | no edge | no edge | no edge |  |
| Sat 11/07 4:15 PM | Vanderbilt @ Mississippi State | Vanderbilt 24, Mississippi State 27 | Mississippi State 61% | Vanderbilt +155 / Mississippi State -155 | 22.9 – 26.8 | 10–36 / 14–41 | Mississippi State -7.8 / Mississippi State -3.5 | 55.1 / 48.5 | no edge | no edge | no edge |  |
| Sat 11/07 5:00 PM | South Alabama @ Louisiana | South Alabama 24, Louisiana 31 | Louisiana 64% | South Alabama +175 / Louisiana -175 | 26.1 – 31.5 | 13–41 / 17–46 | Louisiana -4.6 / Louisiana -5.5 | 58.3 / 57.5 | no edge | no edge | no edge |  |
| Sat 11/07 6:00 PM | Boise State @ Colorado State | Boise State 41, Colorado State 24 | Boise State 89% | Boise State -785 / Colorado State +785 | 42.9 – 24.6 | 28–59 / 10–38 | Boise State -15.7 / Boise State -18.5 | 63.2 / 68.5 | no edge | no edge | no edge |  |
| Sat 11/07 6:15 PM | Kentucky @ Tennessee | Kentucky 24, Tennessee 27 | Tennessee 67% | Kentucky +205 / Tennessee -205 | 21.9 – 28.2 | 10–35 / 14–43 | Tennessee -8.8 / Tennessee -6.0 | 48.3 / 50.5 | no edge | no edge | no edge |  |
| Sat 11/07 7:00 PM | Sam Houston @ Jacksonville State | Sam Houston 17, Jacksonville State 31 | Jacksonville State 85% | Sam Houston +580 / Jacksonville State -580 | 16.2 – 31.0 | 6–28 / 17–45 | Jacksonville State -17.7 / Jacksonville State -14.5 | 45.6 / 47.5 | no edge | no edge | no edge |  |
| Sat 11/07 7:30 PM | Georgia @ Ole Miss | Georgia 31, Ole Miss 28 | Georgia 58% | Georgia -135 / Ole Miss +135 | 29.5 – 26.5 | 16–44 / 13–41 | Georgia -2.8 / Georgia -3.0 | 54.1 / 56.5 | no edge | no edge | no edge |  |
| Sat 11/07 7:30 PM | Colorado @ Arizona State | Colorado 24, Arizona State 27 | Arizona State 60% | Colorado +150 / Arizona State -150 | 22.9 – 26.6 | 10–36 / 13–41 | Arizona State -5.8 / Arizona State -3.5 | 49.9 / 49.5 | no edge | no edge | no edge |  |
| Sat 11/07 7:30 PM | Louisville @ Georgia Tech | Louisville 38, Georgia Tech 24 | Louisville 83% | Louisville -490 / Georgia Tech +490 | 36.6 – 22.7 | 21–52 / 10–37 | Louisville -18.1 / Louisville -13.5 | 58.6 / 59.5 | no edge | no edge | no edge |  |
| Sat 11/07 7:30 PM | Miami @ Notre Dame | Miami 28, Notre Dame 31 | Notre Dame 61% | Miami +155 / Notre Dame -155 | 26.2 – 30.7 | 13–41 / 17–45 | Notre Dame -4.6 / Notre Dame -4.5 | 54.0 / 57.5 | no edge | no edge | no edge |  |
| Sat 11/07 7:30 PM | Air Force @ Army | Air Force 24, Army 31 | Army 65% | Air Force +185 / Army -185 | 23.9 – 29.4 | 10–38 / 15–44 | Army -6.5 / Army -5.5 | 60.8 / 51.5 | no edge | no edge | Over 51.5 (-110*): EV +4.4%, 55%, stake 1.2u | * price not posted; assumed -110 |
| Sat 11/07 7:45 PM | Oklahoma @ Florida | Oklahoma 21, Florida 24 | Florida 66% | Oklahoma +190 / Florida -190 | 20.7 – 26.3 | 7–34 / 13–41 | Florida -1.1 / Florida -6.0 | 45.2 / 47.5 | no edge | no edge | no edge |  |
| Sat 11/07 8:00 PM | Liberty @ New Mexico State | Liberty 31, New Mexico State 17 | Liberty 84% | Liberty -525 / New Mexico State +525 | 30.6 – 16.9 | 17–45 / 6–28 | Liberty -16.4 / Liberty -13.5 | 47.3 / 47.5 | no edge | no edge | no edge |  |
| Sat 11/07 9:30 PM | West Virginia @ Texas Tech | West Virginia 24, Texas Tech 41 | Texas Tech 87% | West Virginia +680 / Texas Tech -680 | 22.6 – 39.6 | 10–36 / 24–55 | Texas Tech -21.5 / Texas Tech -16.5 | 56.7 / 63.5 | no edge | no edge | no edge |  |
| Sat 11/07 9:30 PM | Fresno State @ Utah State | Fresno State 20, Utah State 17 | Fresno State 57% | Fresno State -130 / Utah State +130 | 22.5 – 20.0 | 10–36 / 7–33 | Fresno State -2.9 / Fresno State -2.5 | 46.5 / 41.5 | no edge | no edge | no edge |  |
| Sat 11/07 9:30 PM | Hawai'i @ UTEP | Hawai'i 31, UTEP 21 | Hawai'i 77% | Hawai'i -340 / UTEP +340 | 30.1 – 19.4 | 16–45 / 7–32 | Hawai'i -12.7 / Hawai'i -10.5 | 49.7 / 49.5 | no edge | no edge | no edge |  |
| Sat 11/07 10:30 PM | Texas State @ Oregon State | Texas State 31, Oregon State 38 | Oregon State 71% | Texas State +240 / Oregon State -240 | 29.3 – 37.5 | 14–44 / 23–52 | Oregon State -5.8 / Oregon State -8.5 | 68.0 / 66.5 | no edge | no edge | no edge |  |
| Sat 11/07 10:30 PM | Wyoming @ UNLV | Wyoming 20, UNLV 27 | UNLV 73% | Wyoming +265 / UNLV -265 | 18.9 – 27.4 | 7–31 / 14–42 | UNLV -8.7 / UNLV -8.5 | 49.7 / 45.5 | no edge | no edge | no edge |  |

## 2026 Week 11

| Kickoff (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected points | 80% range | Spread: model / line | Total: model / line | Spread edge | Moneyline edge | Total edge | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tue 11/10 7:00 PM | Western Michigan @ Akron | Western Michigan 31, Akron 17 | Western Michigan 86% | Western Michigan -590 / Akron +590 | 32.5 – 17.4 | 17–48 / 6–30 | Western Michigan -15.1 / – | 49.8 / – | no line yet | no line yet (fair: Western Michigan -590) | no line yet |  |
| Tue 11/10 7:00 PM | Kent State @ Bowling Green | Kent State 17, Bowling Green 24 | Bowling Green 65% | Kent State +185 / Bowling Green -185 | 18.0 – 23.3 | 7–31 / 10–37 | Bowling Green -5.3 / – | 41.4 / – | no line yet | no line yet (fair: Bowling Green -185) | no line yet |  |
| Tue 11/10 8:00 PM | Ohio @ Miami (OH) | Ohio 27, Miami (OH) 24 | Ohio 54% | Ohio -120 / Miami (OH) +120 | 24.9 – 22.9 | 11–38 / 10–37 | Ohio -2.0 / – | 47.8 / – | no line yet | no line yet (fair: Ohio -120) | no line yet |  |
| Wed 11/11 TBA | Buffalo @ Ball State | Buffalo 24, Ball State 27 | Ball State 57% | Buffalo +135 / Ball State -135 | 24.7 – 27.2 | 13–38 / 14–42 | Ball State -2.5 / – | 52.0 / – | no line yet | no line yet (fair: Ball State -135) | no line yet |  |
| Wed 11/11 TBA | Massachusetts @ Toledo | Massachusetts 17, Toledo 34 | Toledo 92% | Massachusetts +1170 / Toledo -1170 | 15.0 – 34.7 | 3–27 / 20–51 | Toledo -19.7 / – | 49.8 / – | no line yet | no line yet (fair: Toledo -1170) | no line yet |  |
| Wed 11/11 7:30 PM | Sacramento State @ Central Michigan | Sacramento State 20, Central Michigan 27 | Central Michigan 73% | Sacramento State +275 / Central Michigan -275 | 18.9 – 27.7 | 7–31 / 14–42 | Central Michigan -8.7 / – | 46.6 / – | no line yet | no line yet (fair: Central Michigan -275) | no line yet |  |
| Thu 11/12 8:00 PM | Memphis @ South Florida | Memphis 24, South Florida 27 | South Florida 51% | Memphis +105 / South Florida -105 | 27.1 – 27.7 | 14–42 / 14–42 | South Florida -0.6 / – | 54.7 / – | no line yet | no line yet (fair: South Florida -105) | no line yet |  |
| Thu 11/12 9:00 PM | Louisiana @ UL Monroe | Louisiana 31, UL Monroe 24 | Louisiana 71% | Louisiana -250 / UL Monroe +250 | 30.2 – 22.3 | 17–45 / 10–35 | Louisiana -7.9 / – | 52.6 / – | no line yet | no line yet (fair: Louisiana -250) | no line yet |  |
| Fri 11/13 7:00 PM | Florida State @ Pittsburgh | Florida State 28, Pittsburgh 31 | Pittsburgh 59% | Florida State +140 / Pittsburgh -140 | 26.1 – 29.2 | 13–41 / 14–44 | Pittsburgh -3.1 / – | 55.2 / – | no line yet | no line yet (fair: Pittsburgh -140) | no line yet |  |
| Fri 11/13 9:00 PM | Illinois @ UCLA | Illinois 17, UCLA 34 | UCLA 87% | Illinois +645 / UCLA -645 | 18.0 – 33.4 | 7–30 / 20–49 | UCLA -15.4 / – | 51.5 / – | no line yet | no line yet (fair: UCLA -645) | no line yet |  |
| Fri 11/13 10:15 PM | Houston @ Colorado | Houston 31, Colorado 24 | Houston 64% | Houston -180 / Colorado +180 | 29.8 – 24.2 | 16–45 / 10–38 | Houston -5.6 / – | 54.0 / – | no line yet | no line yet (fair: Houston -180) | no line yet |  |
| Sat 11/14 TBA | Arizona State @ UCF | Arizona State 24, UCF 27 | Arizona State 51% | Arizona State -105 / UCF +105 | 25.1 – 24.9 | 13–39 / 13–38 | Arizona State -0.2 / – | 50.0 / – | no line yet | no line yet (fair: Arizona State -105) | no line yet |  |
| Sat 11/14 TBA | Baylor @ BYU | Baylor 24, BYU 27 | BYU 67% | Baylor +200 / BYU -200 | 22.8 – 29.0 | 10–36 / 14–43 | BYU -6.2 / – | 51.8 / – | no line yet | no line yet (fair: BYU -200) | no line yet |  |
| Sat 11/14 TBA | Cincinnati @ Iowa State | Cincinnati 28, Iowa State 31 | Iowa State 59% | Cincinnati +145 / Iowa State -145 | 28.2 – 31.6 | 14–42 / 17–46 | Iowa State -3.4 / – | 59.7 / – | no line yet | no line yet (fair: Iowa State -145) | no line yet |  |
| Sat 11/14 TBA | Kansas @ West Virginia | Kansas 34, West Virginia 31 | Kansas 60% | Kansas -155 / West Virginia +155 | 32.8 – 28.5 | 17–48 / 14–43 | Kansas -4.2 / – | 61.3 / – | no line yet | no line yet (fair: Kansas -155) | no line yet |  |
| Sat 11/14 TBA | Kansas State @ TCU | Kansas State 27, TCU 24 | Kansas State 54% | Kansas State -115 / TCU +115 | 25.0 – 23.4 | 13–38 / 10–37 | Kansas State -1.6 / – | 48.4 / – | no line yet | no line yet (fair: Kansas State -115) | no line yet |  |
| Sat 11/14 TBA | Texas Tech @ Oklahoma State | Texas Tech 38, Oklahoma State 24 | Texas Tech 83% | Texas Tech -500 / Oklahoma State +500 | 37.7 – 22.7 | 22–52 / 10–36 | Texas Tech -9.7 / Texas Tech -15.5 | 56.0 / 61.5 | no edge | Oklahoma State (+500): EV +3.5%, 17%, stake 0.2u | no edge |  |
| Sat 11/14 TBA | Utah @ Arizona | Utah 31, Arizona 24 | Utah 67% | Utah -205 / Arizona +205 | 31.3 – 25.1 | 17–45 / 12–38 | Utah -6.2 / – | 56.4 / – | no line yet | no line yet (fair: Utah -205) | no line yet |  |
| Sat 11/14 TBA | South Carolina @ Arkansas | South Carolina 31, Arkansas 21 | South Carolina 76% | South Carolina -320 / Arkansas +320 | 32.4 – 21.6 | 17–48 / 9–35 | South Carolina -10.8 / – | 54.1 / – | no line yet | no line yet (fair: South Carolina -320) | no line yet |  |
| Sat 11/14 TBA | Missouri @ Georgia | Missouri 17, Georgia 27 | Georgia 76% | Missouri +320 / Georgia -320 | 17.9 – 28.0 | 7–31 / 14–43 | Georgia -10.1 / – | 45.9 / – | no line yet | no line yet (fair: Georgia -320) | no line yet |  |
| Sat 11/14 TBA | Florida @ Kentucky | Florida 27, Kentucky 24 | Florida 53% | Florida -115 / Kentucky +115 | 26.5 – 25.3 | 13–41 / 13–39 | Florida -1.2 / – | 51.8 / – | no line yet | no line yet (fair: Florida -115) | no line yet |  |
| Sat 11/14 TBA | Texas @ LSU | Texas 27, LSU 24 | Texas 53% | Texas -115 / LSU +115 | 27.0 – 25.7 | 14–42 / 13–40 | LSU -10.4 / Texas -2.5 | 45.4 / 54.5 | no edge | no edge | Under 54.5 (-110*): EV +4.5%, 55%, stake 1.2u | * price not posted; assumed -110 |
| Sat 11/14 TBA | Auburn @ Mississippi State | Auburn 31, Mississippi State 28 | Auburn 51% | Auburn -105 / Mississippi State +105 | 28.2 – 28.0 | 14–42 / 14–42 | Auburn -0.1 / – | 56.2 / – | no line yet | no line yet (fair: Auburn -105) | no line yet |  |
| Sat 11/14 TBA | Ole Miss @ Oklahoma | Ole Miss 24, Oklahoma 27 | Oklahoma 59% | Ole Miss +145 / Oklahoma -145 | 24.7 – 28.2 | 11–38 / 14–42 | Ole Miss -1.8 / Oklahoma -4.0 | 50.3 / 53.5 | no edge | no edge | no edge |  |
| Sat 11/14 TBA | Tennessee @ Texas A&M | Tennessee 24, Texas A&M 31 | Texas A&M 70% | Tennessee +230 / Texas A&M -230 | 22.9 – 30.6 | 10–37 / 17–45 | Tennessee -1.1 / Texas A&M -8.5 | 45.1 / 55.5 | no edge | no edge | no edge |  |
| Sat 11/14 TBA | Alabama @ Vanderbilt | Alabama 31, Vanderbilt 17 | Alabama 81% | Alabama -415 / Vanderbilt +415 | 32.0 – 19.4 | 17–48 / 7–32 | Alabama -12.7 / – | 51.4 / – | no line yet | no line yet (fair: Alabama -415) | no line yet |  |
| Sat 11/14 TBA | California @ Virginia | California 21, Virginia 31 | Virginia 75% | California +295 / Virginia -295 | 20.6 – 30.2 | 7–34 / 16–45 | Virginia -9.6 / – | 50.8 / – | no line yet | no line yet (fair: Virginia -295) | no line yet |  |
| Sat 11/14 TBA | Duke @ Miami | Duke 17, Miami 38 | Miami 92% | Duke +1170 / Miami -1170 | 17.4 – 38.2 | 6–30 / 23–54 | Miami -18.3 / Miami -21.0 | 56.2 / 55.5 | no edge | no edge | no edge |  |
| Sat 11/14 TBA | Georgia Tech @ Clemson | Georgia Tech 17, Clemson 31 | Clemson 82% | Georgia Tech +455 / Clemson -455 | 18.3 – 31.4 | 7–31 / 17–46 | Clemson -13.1 / – | 49.7 / – | no line yet | no line yet (fair: Clemson -455) | no line yet |  |
| Sat 11/14 TBA | Louisville @ North Carolina | Louisville 31, North Carolina 24 | Louisville 75% | Louisville -305 / North Carolina +305 | 33.6 – 23.5 | 20–49 / 10–37 | Louisville -10.1 / – | 57.1 / – | no line yet | no line yet (fair: Louisville -305) | no line yet |  |
| Sat 11/14 TBA | Stanford @ Virginia Tech | Stanford 17, Virginia Tech 34 | Virginia Tech 88% | Stanford +760 / Virginia Tech -760 | 19.3 – 36.2 | 7–31 / 21–52 | Virginia Tech -17.0 / – | 55.5 / – | no line yet | no line yet (fair: Virginia Tech -760) | no line yet |  |
| Sat 11/14 TBA | Syracuse @ NC State | Syracuse 28, NC State 31 | NC State 61% | Syracuse +155 / NC State -155 | 26.7 – 31.0 | 14–41 / 17–45 | NC State -4.3 / – | 57.7 / – | no line yet | no line yet (fair: NC State -155) | no line yet |  |
| Sat 11/14 TBA | Wake Forest @ SMU | Wake Forest 27, SMU 24 | Wake Forest 52% | Wake Forest -110 / SMU +110 | 27.1 – 26.3 | 14–42 / 13–41 | Wake Forest -0.7 / – | 53.4 / – | no line yet | no line yet (fair: Wake Forest -110) | no line yet |  |
| Sat 11/14 TBA | USC @ Indiana | USC 24, Indiana 34 | Indiana 75% | USC +300 / Indiana -300 | 23.5 – 33.5 | 10–37 / 20–49 | Indiana -10.3 / Indiana -10.0 | 50.6 / 58.5 | no edge | no edge | no edge |  |
| Sat 11/14 TBA | Purdue @ Iowa | Purdue 17, Iowa 31 | Iowa 85% | Purdue +585 / Iowa -585 | 16.8 – 31.8 | 6–28 / 17–46 | Iowa -15.0 / – | 48.6 / – | no line yet | no line yet (fair: Iowa -585) | no line yet |  |
| Sat 11/14 TBA | Wisconsin @ Maryland | Wisconsin 24, Maryland 21 | Wisconsin 62% | Wisconsin -165 / Maryland +165 | 24.4 – 20.0 | 10–38 / 7–33 | Wisconsin -4.4 / – | 44.4 / – | no line yet | no line yet (fair: Wisconsin -165) | no line yet |  |
| Sat 11/14 TBA | Washington @ Michigan State | Washington 27, Michigan State 17 | Washington 74% | Washington -290 / Michigan State +290 | 28.1 – 18.3 | 14–42 / 7–31 | Washington -9.8 / – | 46.4 / – | no line yet | no line yet (fair: Washington -290) | no line yet |  |
| Sat 11/14 TBA | Northwestern @ Ohio State | Northwestern 17, Ohio State 34 | Ohio State 87% | Northwestern +680 / Ohio State -680 | 18.7 – 35.2 | 7–31 / 20–51 | Ohio State -16.6 / – | 53.9 / – | no line yet | no line yet (fair: Ohio State -680) | no line yet |  |
| Sat 11/14 TBA | Michigan @ Oregon | Michigan 17, Oregon 31 | Oregon 80% | Michigan +405 / Oregon -405 | 19.5 – 32.2 | 7–33 / 17–48 | Oregon -5.0 / Oregon -13.5 | 43.9 / 53.5 | no edge | Michigan (+440): EV +5.3%, 20%, stake 0.3u | Under 53.5 (-110*): EV +3.7%, 54%, stake 1.0u | * price not posted; assumed -110 |
| Sat 11/14 TBA | Minnesota @ Penn State | Minnesota 17, Penn State 24 | Penn State 74% | Minnesota +290 / Penn State -290 | 15.7 – 24.7 | 6–27 / 10–38 | Penn State -8.9 / – | 40.4 / – | no line yet | no line yet (fair: Penn State -290) | no line yet |  |
| Sat 11/14 TBA | Nebraska @ Rutgers | Nebraska 34, Rutgers 17 | Nebraska 85% | Nebraska -550 / Rutgers +550 | 34.8 – 19.9 | 20–50 / 7–33 | Nebraska -14.9 / – | 54.8 / – | no line yet | no line yet (fair: Nebraska -550) | no line yet |  |
| Sat 11/14 TBA | East Carolina @ Charlotte | East Carolina 31, Charlotte 17 | East Carolina 84% | East Carolina -510 / Charlotte +510 | 31.9 – 18.0 | 17–48 / 7–31 | East Carolina -13.9 / – | 49.9 / – | no line yet | no line yet (fair: East Carolina -510) | no line yet |  |
| Sat 11/14 TBA | Florida Atlantic @ Tulsa | Florida Atlantic 31, Tulsa 34 | Tulsa 54% | Florida Atlantic +120 / Tulsa -120 | 31.3 – 32.9 | 17–45 / 19–48 | Tulsa -1.6 / – | 64.2 / – | no line yet | no line yet (fair: Tulsa -120) | no line yet |  |
| Sat 11/14 TBA | North Texas @ UTSA | North Texas 31, UTSA 34 | UTSA 54% | North Texas +120 / UTSA -120 | 33.1 – 34.8 | 19–48 / 20–50 | UTSA -1.7 / – | 68.0 / – | no line yet | no line yet (fair: UTSA -120) | no line yet |  |
| Sat 11/14 TBA | Tulane @ Rice | Tulane 31, Rice 24 | Tulane 69% | Tulane -220 / Rice +220 | 28.6 – 21.5 | 14–43 / 10–35 | Tulane -7.1 / – | 50.1 / – | no line yet | no line yet (fair: Tulane -220) | no line yet |  |
| Sat 11/14 TBA | UAB @ Temple | UAB 24, Temple 27 | Temple 57% | UAB +130 / Temple -130 | 24.1 – 27.0 | 10–38 / 13–41 | Temple -2.9 / – | 51.1 / – | no line yet | no line yet (fair: Temple -130) | no line yet |  |
| Sat 11/14 TBA | Nevada @ Northern Illinois | Nevada 27, Northern Illinois 24 | Nevada 60% | Nevada -150 / Northern Illinois +150 | 26.7 – 23.0 | 13–41 / 10–37 | Nevada -3.7 / – | 49.7 / – | no line yet | no line yet (fair: Nevada -150) | no line yet |  |
| Sat 11/14 TBA | Wyoming @ UTEP | Wyoming 31, UTEP 17 | Wyoming 82% | Wyoming -440 / UTEP +440 | 28.6 – 16.5 | 14–43 / 6–28 | Wyoming -12.1 / – | 45.1 / – | no line yet | no line yet (fair: Wyoming -440) | no line yet |  |
| Sat 11/14 TBA | App State @ Marshall | App State 28, Marshall 31 | Marshall 59% | App State +145 / Marshall -145 | 26.0 – 29.8 | 13–41 / 16–45 | Marshall -3.7 / – | 55.8 / – | no line yet | no line yet (fair: Marshall -145) | no line yet |  |
| Sat 11/14 TBA | Arkansas State @ Coastal Carolina | Arkansas State 24, Coastal Carolina 27 | Coastal Carolina 54% | Arkansas State +115 / Coastal Carolina -115 | 25.6 – 27.1 | 13–40 / 14–41 | Coastal Carolina -1.5 / – | 52.7 / – | no line yet | no line yet (fair: Coastal Carolina -115) | no line yet |  |
| Sat 11/14 TBA | Georgia Southern @ Georgia State | Georgia Southern 28, Georgia State 31 | Georgia State 51% | Georgia Southern +105 / Georgia State -105 | 28.8 – 29.5 | 14–44 / 16–44 | Georgia State -0.7 / – | 58.3 / – | no line yet | no line yet (fair: Georgia State -105) | no line yet |  |
| Sat 11/14 TBA | Southern Miss @ Louisiana Tech | Southern Miss 17, Louisiana Tech 31 | Louisiana Tech 85% | Southern Miss +555 / Louisiana Tech -555 | 18.7 – 32.8 | 7–31 / 19–48 | Louisiana Tech -14.1 / – | 51.5 / – | no line yet | no line yet (fair: Louisiana Tech -555) | no line yet |  |
| Sat 11/14 TBA | Troy @ South Alabama | Troy 24, South Alabama 27 | South Alabama 59% | Troy +140 / South Alabama -140 | 25.9 – 28.8 | 13–39 / 14–43 | South Alabama -3.0 / – | 54.7 / – | no line yet | no line yet (fair: South Alabama -140) | no line yet |  |
| Sat 11/14 12:00 PM | James Madison @ UConn | James Madison 27, UConn 24 | James Madison 52% | James Madison -110 / UConn +110 | 28.5 – 27.8 | 14–43 / 14–42 | James Madison -0.8 / – | 56.3 / – | no line yet | no line yet (fair: James Madison -110) | no line yet |  |
| Sat 11/14 2:00 PM | Kennesaw State @ Sam Houston | Kennesaw State 24, Sam Houston 21 | Kennesaw State 62% | Kennesaw State -165 / Sam Houston +165 | 24.0 – 19.9 | 10–38 / 7–33 | Kennesaw State -4.1 / – | 43.8 / – | no line yet | no line yet (fair: Kennesaw State -165) | no line yet |  |
| Sat 11/14 3:00 PM | New Mexico State @ Missouri State | New Mexico State 24, Missouri State 27 | Missouri State 64% | New Mexico State +180 / Missouri State -180 | 23.3 – 28.4 | 10–37 / 14–42 | Missouri State -5.2 / – | 51.7 / – | no line yet | no line yet (fair: Missouri State -180) | no line yet |  |
| Sat 11/14 3:00 PM | Florida International @ Delaware | Florida International 17, Delaware 31 | Delaware 80% | Florida International +410 / Delaware -410 | 19.6 – 32.2 | 7–31 / 17–48 | Delaware -12.6 / – | 51.8 / – | no line yet | no line yet (fair: Delaware -410) | no line yet |  |
| Sat 11/14 3:30 PM | Boston College @ Notre Dame | Boston College 6, Notre Dame 41 | Notre Dame 100% | Boston College +9900 / Notre Dame -9900 | 6.5 – 40.9 | 0–14 / 27–58 | Notre Dame -34.4 / – | 47.4 / – | no line yet | no line yet (fair: Notre Dame -9900) | no line yet |  |
| Sat 11/14 3:30 PM | Jacksonville State @ Western Kentucky | Jacksonville State 31, Western Kentucky 24 | Jacksonville State 62% | Jacksonville State -165 / Western Kentucky +165 | 29.2 – 24.2 | 14–43 / 10–38 | Jacksonville State -5.0 / – | 53.4 / – | no line yet | no line yet (fair: Jacksonville State -165) | no line yet |  |
| Sat 11/14 3:30 PM | Middle Tennessee @ Liberty | Middle Tennessee 13, Liberty 34 | Liberty 94% | Middle Tennessee +1540 / Liberty -1540 | 13.8 – 35.1 | 3–24 / 20–51 | Liberty -21.3 / – | 48.9 / – | no line yet | no line yet (fair: Liberty -1540) | no line yet |  |
| Sat 11/14 4:00 PM | Fresno State @ Texas State | Fresno State 28, Texas State 31 | Texas State 60% | Fresno State +150 / Texas State -150 | 28.5 – 32.3 | 14–42 / 17–48 | Texas State -3.8 / – | 60.7 / – | no line yet | no line yet (fair: Texas State -150) | no line yet |  |
| Sat 11/14 6:00 PM | Oregon State @ Boise State | Oregon State 27, Boise State 34 | Boise State 67% | Oregon State +200 / Boise State -200 | 26.9 – 33.6 | 14–41 / 20–49 | Boise State -6.7 / – | 60.5 / – | no line yet | no line yet (fair: Boise State -200) | no line yet |  |
| Sat 11/14 7:00 PM | San José State @ Air Force | San José State 20, Air Force 34 | Air Force 82% | San José State +455 / Air Force -455 | 20.1 – 33.7 | 7–33 / 20–49 | Air Force -13.6 / – | 53.9 / – | no line yet | no line yet (fair: Air Force -455) | no line yet |  |
| Sat 11/14 7:30 PM | UNLV @ New Mexico | UNLV 21, New Mexico 28 | New Mexico 69% | UNLV +220 / New Mexico -220 | 20.2 – 27.2 | 7–33 / 14–41 | New Mexico -7.0 / – | 47.3 / – | no line yet | no line yet (fair: New Mexico -220) | no line yet |  |
| Sat 11/14 9:30 PM | Utah State @ San Diego State | Utah State 21, San Diego State 24 | San Diego State 58% | Utah State +140 / San Diego State -140 | 22.5 – 25.4 | 10–36 / 13–39 | San Diego State -2.9 / – | 48.0 / – | no line yet | no line yet (fair: San Diego State -140) | no line yet |  |
| Sat 11/14 10:30 PM | Colorado State @ Washington State | Colorado State 24, Washington State 31 | Washington State 65% | Colorado State +190 / Washington State -190 | 25.4 – 31.5 | 13–39 / 17–45 | Washington State -6.1 / – | 57.0 / – | no line yet | no line yet (fair: Washington State -190) | no line yet |  |
| Sat 11/14 11:00 PM | North Dakota State @ Hawai'i | North Dakota State 27, Hawai'i 20 | North Dakota State 72% | North Dakota State -260 / Hawai'i +260 | 27.5 – 19.4 | 14–42 / 7–31 | North Dakota State -8.1 / – | 46.9 / – | no line yet | no line yet (fair: North Dakota State -260) | no line yet |  |

## How the 2026 predictions have done

| Predictor | Games | Margin MAE | Total MAE | Team-score MAE | Winners | Brier | 80% range hit |
|---|---|---|---|---|---|---|---|
| Final prediction | 622 | 11.65 | 12.16 | 8.42 | 80.2% | 0.139 | 82.1% |
| Model only (before blending) | 622 | 12.39 | 12.48 | 8.69 | 77.5% | – | – |
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
| 2 | Ohio State | Big Ten | +25.7 | +10.9 | +10.2 | +0.3 | +4.3 | 1868 |
| 3 | Georgia | SEC | +23.9 | +7.9 | +10.6 | +0.9 | +4.5 | 1880 |
| 4 | Notre Dame | FBS Independents | +23.1 | +8.8 | +9.1 | +1.1 | +4.2 | 1858 |
| 5 | Miami | ACC | +23.1 | +14.3 | +3.7 | +0.4 | +4.7 | 1894 |
| 6 | Indiana | Big Ten | +21.7 | +5.7 | +10.7 | +0.1 | +5.2 | 1939 |
| 7 | Utah | Big 12 | +20.5 | +10.6 | +5.8 | +0.0 | +4.0 | 1842 |
| 8 | Alabama | SEC | +19.6 | +9.0 | +7.1 | +0.2 | +3.2 | 1777 |
| 9 | Ole Miss | SEC | +18.6 | +10.4 | +3.8 | +0.7 | +3.7 | 1815 |
| 10 | Texas Tech | Big 12 | +18.2 | +2.1 | +11.9 | +1.2 | +3.0 | 1761 |
| 11 | Texas | SEC | +18.1 | +1.3 | +12.4 | +0.6 | +3.7 | 1814 |
| 12 | Oregon | Big Ten | +16.8 | +4.4 | +9.0 | +0.5 | +2.8 | 1743 |
| 13 | UCLA | Big Ten | +16.6 | +4.6 | +9.3 | +0.7 | +2.0 | 1676 |
| 14 | Missouri | SEC | +16.3 | +4.5 | +8.4 | +0.9 | +2.5 | 1714 |
| 15 | Wake Forest | ACC | +16.3 | +6.0 | +7.3 | +0.5 | +2.4 | 1710 |
| 16 | Louisville | ACC | +15.6 | +9.8 | +3.7 | +0.0 | +2.1 | 1681 |
| 17 | Tennessee | SEC | +15.4 | +3.7 | +8.5 | +0.7 | +2.6 | 1723 |
| 18 | Michigan | Big Ten | +14.7 | +3.5 | +9.3 | +0.0 | +2.0 | 1674 |
| 19 | Oklahoma | SEC | +14.4 | +0.2 | +12.4 | +0.6 | +1.3 | 1615 |
| 20 | USC | Big Ten | +13.8 | +10.5 | +0.3 | +0.3 | +2.8 | 1738 |
| 21 | Nebraska | Big Ten | +13.5 | +4.9 | +7.1 | +0.5 | +0.9 | 1587 |
| 22 | BYU | Big 12 | +13.4 | +5.5 | +4.2 | +0.6 | +3.0 | 1759 |
| 23 | SMU | ACC | +13.3 | +7.5 | +3.7 | +0.2 | +2.0 | 1675 |
| 24 | Iowa | Big Ten | +13.1 | +1.6 | +7.8 | +0.8 | +2.9 | 1751 |
| 25 | Florida | SEC | +12.6 | +6.6 | +4.2 | +1.0 | +0.8 | 1579 |
| 26 | Texas A&M | SEC | +12.0 | +2.5 | +7.8 | +0.5 | +1.1 | 1601 |
| 27 | Auburn | SEC | +12.0 | +5.4 | +5.6 | +0.6 | +0.3 | 1536 |
| 28 | Arizona | Big 12 | +12.0 | +6.2 | +3.5 | -0.2 | +2.4 | 1708 |
| 29 | South Carolina | SEC | +11.9 | +5.4 | +3.8 | +0.8 | +1.8 | 1662 |
| 30 | Penn State | Big Ten | +11.4 | +3.0 | +7.0 | +0.1 | +1.2 | 1611 |
| 31 | Northwestern | Big Ten | +11.2 | +7.1 | +1.8 | +0.8 | +1.5 | 1634 |
| 32 | Houston | Big 12 | +10.2 | +7.9 | +0.1 | +0.2 | +2.0 | 1673 |
| 33 | Mississippi State | SEC | +9.7 | +5.8 | +3.6 | +0.2 | +0.0 | 1512 |
| 34 | Kansas State | Big 12 | +9.7 | +6.2 | +3.0 | +0.3 | +0.2 | 1526 |
| 35 | Kentucky | SEC | +9.6 | +2.8 | +4.5 | +0.3 | +2.0 | 1677 |
| 36 | Baylor | Big 12 | +9.3 | +0.3 | +6.8 | +1.0 | +1.1 | 1601 |
| 37 | Washington | Big Ten | +8.8 | +2.8 | +4.1 | -0.0 | +2.0 | 1670 |
| 38 | Wisconsin | Big Ten | +8.1 | -0.1 | +7.0 | +0.2 | +1.0 | 1593 |
| 39 | Kansas | Big 12 | +7.2 | +4.6 | +3.4 | -0.0 | -0.8 | 1439 |
| 40 | Duke | ACC | +6.8 | +2.6 | +1.3 | +0.8 | +2.0 | 1677 |
| 41 | Oklahoma State | Big 12 | +6.8 | +8.5 | -1.9 | +0.4 | -0.3 | 1484 |
| 42 | Iowa State | Big 12 | +6.6 | +3.9 | +1.1 | +0.9 | +0.7 | 1563 |
| 43 | Cincinnati | Big 12 | +6.3 | +8.9 | -3.8 | +0.4 | +0.7 | 1568 |
| 44 | Boise State | Pac-12 | +6.2 | +4.8 | -1.0 | -0.2 | +2.6 | 1721 |
| 45 | Arizona State | Big 12 | +5.6 | +1.0 | +4.0 | +0.0 | +0.5 | 1550 |
| 46 | TCU | Big 12 | +5.4 | -2.3 | +6.4 | +0.5 | +0.9 | 1587 |
| 47 | Clemson | ACC | +4.9 | -4.9 | +7.8 | +0.7 | +1.3 | 1613 |
| 48 | Virginia Tech | ACC | +4.9 | +3.3 | +0.5 | +0.3 | +0.7 | 1566 |
| 49 | Illinois | Big Ten | +4.5 | +5.9 | -2.5 | -0.1 | +1.2 | 1610 |
| 50 | Florida State | ACC | +4.5 | +6.9 | -1.4 | -0.5 | -0.6 | 1462 |
| 51 | Vanderbilt | SEC | +4.4 | +4.5 | -0.6 | +0.3 | +0.2 | 1529 |
| 52 | Minnesota | Big Ten | +4.0 | -4.1 | +6.4 | +1.0 | +0.6 | 1561 |
| 53 | Pittsburgh | ACC | +4.0 | -1.2 | +3.9 | +0.6 | +0.7 | 1566 |
| 54 | North Texas | American Athletic | +3.5 | +10.2 | -7.4 | -0.8 | +1.6 | 1645 |
| 55 | NC State | ACC | +3.3 | +5.7 | -2.1 | -0.6 | +0.4 | 1538 |
| 56 | Colorado | Big 12 | +3.0 | +0.5 | +4.7 | -0.7 | -1.6 | 1378 |
| 57 | UCF | Big 12 | +2.8 | +0.7 | +2.7 | +0.0 | -0.6 | 1459 |
| 58 | North Carolina | ACC | +2.3 | +3.3 | -1.8 | +0.8 | +0.0 | 1509 |
| 59 | James Madison | Sun Belt | +2.0 | -1.7 | +1.0 | +0.4 | +2.3 | 1698 |
| 60 | UTSA | American Athletic | +2.0 | +2.9 | -3.0 | -0.1 | +2.1 | 1686 |
| 61 | Syracuse | ACC | +1.9 | +1.7 | +2.4 | -0.9 | -1.2 | 1407 |
| 62 | Oregon State | Pac-12 | +1.7 | +4.6 | -2.5 | +0.1 | -0.5 | 1468 |
| 63 | Memphis | American Athletic | +1.3 | +3.0 | -2.5 | -0.4 | +1.3 | 1614 |
| 64 | Liberty | Conference USA | +1.1 | +0.7 | -0.5 | +0.4 | +0.5 | 1551 |
| 65 | Virginia | ACC | +1.0 | -1.3 | +3.0 | -0.6 | -0.2 | 1494 |
| 66 | Purdue | Big Ten | +0.6 | +2.9 | -2.1 | +0.8 | -1.0 | 1426 |
| 67 | Maryland | Big Ten | +0.5 | -1.6 | +3.1 | +1.0 | -2.1 | 1334 |
| 68 | Arkansas | SEC | +0.2 | +1.2 | +0.3 | -0.8 | -0.5 | 1468 |
| 69 | Toledo | Mid-American | -0.0 | -1.2 | +0.6 | -0.0 | +0.6 | 1555 |
| 70 | West Virginia | Big 12 | -0.1 | +3.9 | -4.5 | +0.6 | -0.1 | 1502 |
| 71 | Texas State | Pac-12 | -0.2 | +5.8 | -5.4 | -1.2 | +0.7 | 1563 |
| 72 | New Mexico | Mountain West | -0.4 | -3.4 | +2.0 | -0.3 | +1.3 | 1618 |
| 73 | North Dakota State | Mountain West | -1.2 | -5.1 | +3.9 | +1.1 | -1.1 | 1419 |
| 74 | Navy | American Athletic | -1.3 | +3.6 | -3.9 | -0.6 | -0.4 | 1473 |
| 75 | South Florida | American Athletic | -1.3 | -2.3 | -0.2 | +0.2 | +1.0 | 1593 |
| 76 | UConn | FBS Independents | -2.0 | +2.2 | -3.5 | -0.3 | -0.4 | 1472 |
| 77 | Army | American Athletic | -2.4 | +5.6 | -8.3 | -0.2 | +0.6 | 1554 |
| 78 | Fresno State | Pac-12 | -2.6 | -2.2 | -1.0 | -0.1 | +0.8 | 1574 |
| 79 | Louisiana Tech | Sun Belt | -2.7 | -3.2 | +0.8 | -0.7 | +0.4 | 1540 |
| 80 | Ohio | Mid-American | -3.4 | -1.8 | -2.9 | +0.5 | +0.8 | 1578 |
| 81 | Tulsa | American Athletic | -3.6 | -1.0 | -0.3 | -0.5 | -1.8 | 1358 |
| 82 | Michigan State | Big Ten | -3.6 | -3.5 | +1.2 | +0.1 | -1.5 | 1388 |
| 83 | East Carolina | American Athletic | -3.7 | -5.4 | +2.6 | -0.7 | -0.1 | 1496 |
| 84 | Florida Atlantic | American Athletic | -3.9 | +3.9 | -7.4 | +0.7 | -1.1 | 1416 |
| 85 | Rutgers | Big Ten | -4.2 | +2.8 | -6.3 | +0.8 | -1.4 | 1388 |
| 86 | Tulane | American Athletic | -4.4 | -3.7 | -1.7 | +0.2 | +0.6 | 1562 |
| 87 | Georgia Tech | ACC | -4.8 | +1.1 | -4.4 | -0.1 | -1.4 | 1393 |
| 88 | Jacksonville State | Conference USA | -4.9 | -0.1 | -4.4 | -0.2 | -0.1 | 1497 |
| 89 | Air Force | Mountain West | -4.9 | +2.4 | -6.8 | -0.3 | -0.2 | 1488 |
| 90 | UNLV | Mountain West | -5.3 | -2.8 | -3.0 | +0.1 | +0.4 | 1543 |
| 91 | Boston College | ACC | -5.4 | -3.6 | -0.4 | -0.9 | -0.5 | 1469 |
| 92 | California | ACC | -6.2 | -2.1 | -2.0 | -0.4 | -1.7 | 1369 |
| 93 | Delaware | Conference USA | -6.3 | -0.2 | -5.2 | +0.3 | -1.2 | 1406 |
| 94 | Utah State | Pac-12 | -6.9 | -6.7 | +2.2 | -1.2 | -1.2 | 1412 |
| 95 | Western Michigan | Mid-American | -7.0 | -4.8 | -3.6 | +0.8 | +0.6 | 1561 |
| 96 | Marshall | Sun Belt | -7.3 | -3.2 | -3.7 | -0.3 | -0.1 | 1500 |
| 97 | San Diego State | Pac-12 | -8.0 | -4.6 | -2.4 | +0.3 | -1.2 | 1406 |
| 98 | Miami (OH) | Mid-American | -8.1 | -4.5 | -3.3 | +0.5 | -0.8 | 1446 |
| 99 | Georgia Southern | Sun Belt | -8.2 | -2.2 | -5.2 | -0.9 | +0.1 | 1513 |
| 100 | Washington State | Pac-12 | -8.3 | -6.3 | +0.2 | -0.3 | -1.9 | 1349 |
| 101 | App State | Sun Belt | -8.5 | -3.9 | -3.3 | -0.3 | -1.0 | 1422 |
| 102 | Stanford | ACC | -9.3 | -3.0 | -5.6 | +0.0 | -0.7 | 1448 |
| 103 | Louisiana | Sun Belt | -9.4 | -4.9 | -4.0 | -0.1 | -0.4 | 1478 |
| 104 | Temple | American Athletic | -9.5 | +0.6 | -6.9 | -0.5 | -2.6 | 1291 |
| 105 | UAB | American Athletic | -9.9 | -5.8 | -2.5 | -0.4 | -1.2 | 1407 |
| 106 | Arkansas State | Sun Belt | -10.2 | -2.7 | -6.9 | +0.2 | -0.8 | 1441 |
| 107 | Georgia State | Sun Belt | -10.4 | -0.9 | -7.2 | -0.4 | -2.0 | 1347 |
| 108 | Troy | Sun Belt | -10.9 | -7.9 | -0.5 | -1.2 | -1.3 | 1401 |
| 109 | Wyoming | Mountain West | -11.2 | -6.5 | -3.4 | -0.2 | -1.1 | 1413 |
| 110 | Hawai'i | Mountain West | -11.4 | -4.0 | -6.2 | +0.6 | -1.7 | 1365 |
| 111 | Coastal Carolina | Sun Belt | -11.4 | -5.7 | -4.7 | +0.5 | -1.5 | 1384 |
| 112 | Colorado State | Pac-12 | -11.9 | +3.2 | -12.1 | -0.3 | -2.7 | 1286 |
| 113 | South Alabama | Sun Belt | -11.9 | -0.4 | -10.5 | +0.3 | -1.3 | 1398 |
| 114 | Western Kentucky | Conference USA | -12.2 | -6.7 | -3.2 | -0.3 | -2.0 | 1345 |
| 115 | Kennesaw State | Conference USA | -12.8 | -6.5 | -3.5 | -0.8 | -2.0 | 1346 |
| 116 | Rice | American Athletic | -12.9 | -3.6 | -5.2 | -0.9 | -3.2 | 1246 |
| 117 | Old Dominion | Sun Belt | -13.2 | -13.0 | +3.1 | -1.4 | -1.8 | 1357 |
| 118 | Missouri State | Conference USA | -13.3 | -1.7 | -7.4 | -1.4 | -2.7 | 1281 |
| 119 | Nevada | Mountain West | -13.4 | -9.7 | -1.8 | +0.3 | -2.2 | 1327 |
| 120 | Central Michigan | Mid-American | -13.9 | -7.2 | -4.8 | -0.2 | -1.6 | 1375 |
| 121 | Southern Miss | Sun Belt | -14.0 | -7.5 | -3.3 | -1.0 | -2.1 | 1331 |
| 122 | Florida International | Conference USA | -15.0 | -10.0 | -1.9 | -1.2 | -1.9 | 1353 |
| 123 | New Mexico State | Conference USA | -15.6 | -8.4 | -2.6 | -1.7 | -2.8 | 1275 |
| 124 | San José State | Mountain West | -16.3 | -9.8 | -3.9 | -0.1 | -2.5 | 1303 |
| 125 | Ball State | Mid-American | -16.7 | -5.5 | -7.2 | -1.0 | -3.1 | 1251 |
| 126 | Eastern Michigan | Mid-American | -17.1 | -7.5 | -6.9 | -0.6 | -2.2 | 1330 |
| 127 | Massachusetts | Mid-American | -17.2 | -9.4 | -4.4 | -0.0 | -3.5 | 1219 |
| 128 | Middle Tennessee | Conference USA | -17.3 | -7.1 | -7.3 | +0.1 | -3.0 | 1257 |
| 129 | Northern Illinois | Mountain West | -18.2 | -3.6 | -9.1 | -1.1 | -4.4 | 1145 |
| 130 | UL Monroe | Sun Belt | -18.2 | -6.3 | -6.1 | -1.7 | -4.1 | 1168 |
| 131 | Buffalo | Mid-American | -18.2 | -12.6 | -5.4 | +0.5 | -0.8 | 1444 |
| 132 | Bowling Green | Mid-American | -18.7 | -11.7 | -4.0 | -0.1 | -2.9 | 1270 |
| 133 | Sam Houston | Conference USA | -18.9 | -12.5 | -0.7 | -1.3 | -4.4 | 1145 |
| 134 | Charlotte | American Athletic | -20.2 | -6.9 | -9.2 | -0.5 | -3.7 | 1203 |
| 135 | Sacramento State | Mid-American | -20.4 | -11.0 | -5.3 | +0.1 | -4.3 | 1151 |
| 136 | Kent State | Mid-American | -20.7 | -10.8 | -5.9 | -0.8 | -3.2 | 1241 |
| 137 | Akron | Mid-American | -22.7 | -9.9 | -8.0 | -1.1 | -3.7 | 1205 |
| 138 | UTEP | Mountain West | -24.7 | -12.2 | -6.4 | -1.3 | -4.8 | 1112 |

## Current model fit

- Fitted on 4239 games from seasons 2022–2026.
- Home field on top of the ratings: 3.3 points (1.9 in conference games).
- Extra FBS edge over FCS opponents beyond their ratings: 14.1 points.
- Elo weight: 0.19 points of margin per point of Elo spread.
- Weight on the betting line: 91% for the margin, 81% for the total.
