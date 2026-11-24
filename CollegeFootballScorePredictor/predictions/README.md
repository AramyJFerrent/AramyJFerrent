# College football score predictions

Updated Tue Nov 24, 2026 06:14 PM ET. Refreshed automatically every day of the season and several times on Saturdays; each game's prediction is locked at kickoff and graded once the final score is in. Scores are the most likely real scoreline near the expected points; ranges cover 80% of simulated outcomes for each team. College scores scatter widely, so read the ranges, not just the headline score.

Expected points blend the model with the betting line using the weight that has predicted best in recent seasons (see Current model fit). The spread and total columns show the model's own numbers next to the line, so you can see where it disagrees. Games without a line yet use the model alone.

The fair moneyline is the American odds that match the win chance exactly, with no bookmaker margin: -200 means risk $200 to win $100, +200 means risk $100 to win $200. A sportsbook's price will be a little worse on both sides because of its cut, so a book only offers value on a team when its price beats the fair line.

The edge columns judge each bet by its expected value per $1 staked at the posted price, using the final prediction: the model blended with the line, run through the score simulator, pushes included, and anchored to the market's own chances so that only what the blend moves off the line counts. The model's own spread and total (shown alongside) sit several points from the line in most games, but the blend keeps only the share of that disagreement the model has earned in past seasons, so edges are rare. The side with the higher value is shown when it reaches 3% (+3 cents per $1), as the team or side, the price, the expected value, its chance of winning the bet and its stake, a 25% share of the Kelly stake in units of 1% of the bankroll with at most 3 units on one game; anything short is no edge. Where a book posts no price for a spread or total it is assumed to be -110 and marked -110*; moneylines are never assumed. In the walk-forward backtest against closing lines, edges returned spread -100.0% on 1 bets (posted prices, 2016–2019); spread -3.9% on 156 bets (assumed -110 prices, 2016–2025); moneyline +13.7% on 575 bets (posted prices, 2016–2025); total +2.6% on 367 bets (posted prices, 2016–2019); total -5.7% on 172 bets (assumed -110 prices, 2016–2025). None of these is clearly above zero, so treat these edges as an experiment, not a betting system. The live record is tracked below, graded at the price logged with the last prediction before kickoff.

## 2026 Week 13

| Kickoff (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected points | 80% range | Spread: model / line | Total: model / line | Spread edge | Moneyline edge | Total edge | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tue 11/24 7:00 PM | Kent State @ Eastern Michigan | Kent State 21, Eastern Michigan 28 | Eastern Michigan 68% | Kent State +210 / Eastern Michigan -210 | 20.1 – 26.8 | 7–34 / 13–41 | Eastern Michigan -6.6 / Eastern Michigan -6.8 | 49.6 / 46.2 | no edge | no edge | no edge |  |
| Tue 11/24 7:00 PM | Miami (OH) @ Western Michigan | Miami (OH) 21, Western Michigan 24 | Western Michigan 61% | Miami (OH) +160 / Western Michigan -160 | 20.6 – 25.1 | 7–34 / 12–39 | Western Michigan -1.9 / Western Michigan -4.8 | 48.0 / 45.2 | no edge | no edge | no edge |  |
| Thu 11/26 8:00 PM | TCU @ Texas Tech | TCU 17, Texas Tech 31 | Texas Tech 85% | TCU +575 / Texas Tech -575 | 16.0 – 30.6 | 6–28 / 17–45 | Texas Tech -18.8 / Texas Tech -14.2 | 43.6 / 47.2 | no edge | no edge | no edge |  |
| Fri 11/27 12:00 PM | Mississippi State @ Ole Miss | Mississippi State 20, Ole Miss 38 | Ole Miss 89% | Mississippi State +815 / Ole Miss -815 | 19.4 – 37.5 | 7–32 / 23–53 | Ole Miss -14.9 / Ole Miss -18.5 | 58.9 / 56.5 | no edge | no edge | no edge |  |
| Fri 11/27 12:00 PM | Nebraska @ Iowa | Nebraska 17, Iowa 24 | Iowa 63% | Nebraska +170 / Iowa -170 | 18.3 – 22.9 | 7–31 / 10–37 | Iowa -5.6 / Iowa -4.5 | 44.7 / 40.5 | no edge | no edge | no edge |  |
| Fri 11/27 12:00 PM | Tulsa @ UTSA | Tulsa 28, UTSA 31 | UTSA 54% | Tulsa +120 / UTSA -120 | 28.0 – 29.4 | 14–42 / 15–44 | UTSA -3.6 / UTSA -1.2 | 55.9 / 57.8 | no edge | no edge | no edge |  |
| Fri 11/27 12:00 PM | Buffalo @ Akron | Buffalo 28, Akron 21 | Buffalo 69% | Buffalo -225 / Akron +225 | 28.2 – 20.9 | 14–42 / 8–34 | Buffalo -8.1 / Buffalo -7.2 | 52.0 / 48.8 | no edge | no edge | no edge |  |
| Fri 11/27 12:00 PM | Toledo @ Ohio | Toledo 24, Ohio 21 | Toledo 58% | Toledo -140 / Ohio +140 | 24.5 – 21.4 | 11–38 / 9–35 | Toledo -4.0 / Toledo -3.0 | 48.3 / 45.5 | no edge | no edge | no edge |  |
| Fri 11/27 3:00 PM | App State @ South Alabama | App State 28, South Alabama 31 | South Alabama 59% | App State +145 / South Alabama -145 | 26.9 – 30.1 | 13–41 / 16–45 | South Alabama -2.9 / South Alabama -3.2 | 59.2 / 56.5 | no edge | no edge | no edge |  |
| Fri 11/27 3:30 PM | Florida @ Florida State | Florida 31, Florida State 24 | Florida 67% | Florida -200 / Florida State +200 | 30.0 – 23.8 | 16–45 / 10–38 | Florida -5.8 / Florida -6.2 | 55.6 / 53.5 | no edge | no edge | no edge |  |
| Fri 11/27 3:30 PM | Temple @ Memphis | Temple 24, Memphis 41 | Memphis 87% | Temple +690 / Memphis -690 | 23.9 – 41.4 | 10–38 / 27–58 | Memphis -17.6 / Memphis -17.5 | 61.0 / 66.2 | no edge | no edge | no edge |  |
| Fri 11/27 3:30 PM | North Dakota State @ San José State | North Dakota State 24, San José State 17 | North Dakota State 74% | North Dakota State -290 / San José State +290 | 24.7 – 16.0 | 10–38 / 6–28 | North Dakota State -11.5 / North Dakota State -8.5 | 42.7 / 40.2 | no edge | no edge | no edge |  |
| Fri 11/27 4:30 PM | Air Force @ New Mexico | Air Force 17, New Mexico 24 | New Mexico 66% | Air Force +200 / New Mexico -200 | 18.4 – 24.7 | 7–31 / 12–38 | New Mexico -4.6 / New Mexico -6.5 | 48.6 / 42.0 | no edge | no edge | no edge |  |
| Fri 11/27 7:30 PM | Texas @ Texas A&M | Texas 24, Texas A&M 14 | Texas 80% | Texas -400 / Texas A&M +400 | 26.0 – 14.6 | 13–41 / 3–27 | Texas -12.5 / Texas -11.2 | 40.7 / 40.5 | no edge | no edge | no edge |  |
| Fri 11/27 7:30 PM | Minnesota @ Wisconsin | Minnesota 17, Wisconsin 24 | Wisconsin 71% | Minnesota +245 / Wisconsin -245 | 15.1 – 22.7 | 3–27 / 10–36 | Wisconsin -8.4 / Wisconsin -7.5 | 38.8 / 37.5 | no edge | no edge | no edge |  |
| Fri 11/27 9:00 PM | West Virginia @ Utah | West Virginia 21, Utah 48 | Utah 95% | West Virginia +1975 / Utah -1975 | 21.1 – 46.4 | 7–34 / 31–63 | Utah -25.8 / Utah -25.2 | 63.8 / 68.2 | no edge | no edge | no edge |  |
| Sat 11/28 12:00 PM | Louisville @ Kentucky | Louisville 27, Kentucky 24 | Louisville 58% | Louisville -140 / Kentucky +140 | 28.5 – 25.3 | 14–43 / 13–40 | Louisville -6.6 / Louisville -2.8 | 51.9 / 54.5 | no edge | no edge | no edge |  |
| Sat 11/28 12:00 PM | Boston College @ Miami | Boston College 14, Miami 38 | Miami 96% | Boston College +2680 / Miami -2680 | 14.0 – 39.9 | 3–24 / 24–56 | Miami -32.4 / Miami -25.2 | 54.8 / 53.8 | no edge | no edge | no edge |  |
| Sat 11/28 12:00 PM | NC State @ North Carolina | NC State 24, North Carolina 27 | North Carolina 63% | NC State +170 / North Carolina -170 | 25.0 – 30.2 | 12–39 / 16–45 | North Carolina -1.6 / North Carolina -5.5 | 58.4 / 54.5 | no edge | no edge | no edge |  |
| Sat 11/28 12:00 PM | Notre Dame @ Syracuse | Notre Dame 38, Syracuse 14 | Notre Dame 95% | Notre Dame -2020 / Syracuse +2020 | 38.2 – 14.0 | 23–55 / 3–24 | Notre Dame -21.5 / Notre Dame -24.5 | 51.3 / 52.5 | no edge | no edge | no edge |  |
| Sat 11/28 12:00 PM | Michigan @ Ohio State | Michigan 14, Ohio State 24 | Ohio State 78% | Michigan +355 / Ohio State -355 | 14.4 – 25.1 | 3–26 / 13–38 | Ohio State -14.4 / Ohio State -10.2 | 45.6 / 38.2 | no edge | no edge | no edge |  |
| Sat 11/28 12:00 PM | UConn @ Wyoming | UConn 24, Wyoming 21 | UConn 59% | UConn -145 / Wyoming +145 | 24.9 – 21.7 | 12–38 / 10–35 | UConn -4.6 / UConn -3.0 | 55.4 / 45.5 | no edge | no edge | no edge |  |
| Sat 11/28 12:00 PM | Navy @ Charlotte | Navy 34, Charlotte 17 | Navy 87% | Navy -690 / Charlotte +690 | 35.5 – 18.8 | 21–51 / 7–31 | Navy -18.3 / Navy -16.5 | 52.2 / 54.8 | no edge | no edge | no edge |  |
| Sat 11/28 12:00 PM | Central Michigan @ Ball State | Central Michigan 27, Ball State 24 | Central Michigan 60% | Central Michigan -150 / Ball State +150 | 26.7 – 22.9 | 13–41 / 10–36 | Central Michigan -4.2 / Central Michigan -3.8 | 51.1 / 49.5 | no edge | no edge | no edge |  |
| Sat 11/28 12:00 PM | Louisiana Tech @ Georgia Southern | Louisiana Tech 24, Georgia Southern 27 | Georgia Southern 56% | Louisiana Tech +130 / Georgia Southern -130 | 25.7 – 27.8 | 13–39 / 14–42 | Louisiana Tech -2.1 / Georgia Southern -2.5 | 50.0 / 54.2 | no edge | no edge | no edge |  |
| Sat 11/28 12:30 PM | Illinois @ Northwestern | Illinois 24, Northwestern 27 | Northwestern 58% | Illinois +135 / Northwestern -135 | 24.0 – 27.4 | 10–38 / 14–42 | Northwestern -7.0 / Northwestern -3.0 | 56.4 / 50.2 | no edge | no edge | no edge |  |
| Sat 11/28 12:45 PM | LSU @ Arkansas | LSU 31, Arkansas 17 | LSU 85% | LSU -550 / Arkansas +550 | 32.2 – 17.3 | 17–48 / 6–30 | LSU -18.5 / LSU -14.5 | 50.4 / 49.5 | no edge | no edge | no edge |  |
| Sat 11/28 1:00 PM | Florida Atlantic @ East Carolina | Florida Atlantic 28, East Carolina 31 | East Carolina 53% | Florida Atlantic +115 / East Carolina -115 | 28.1 – 29.7 | 14–42 / 16–45 | East Carolina -2.2 / East Carolina -1.5 | 58.1 / 57.8 | no edge | no edge | no edge |  |
| Sat 11/28 1:00 PM | Kennesaw State @ Western Kentucky | Kennesaw State 27, Western Kentucky 24 | Kennesaw State 57% | Kennesaw State -130 / Western Kentucky +130 | 28.2 – 25.3 | 14–43 / 13–39 | Western Kentucky -0.8 / Kennesaw State -3.2 | 54.2 / 53.5 | no edge | no edge | no edge |  |
| Sat 11/28 1:00 PM | Marshall @ UL Monroe | Marshall 31, UL Monroe 24 | Marshall 63% | Marshall -175 / UL Monroe +175 | 28.6 – 23.0 | 14–43 / 10–37 | Marshall -5.9 / Marshall -5.5 | 53.9 / 51.2 | no edge | no edge | no edge |  |
| Sat 11/28 1:00 PM | Southern Miss @ Old Dominion | Southern Miss 24, Old Dominion 27 | Old Dominion 65% | Southern Miss +190 / Old Dominion -190 | 22.0 – 28.1 | 10–35 / 14–42 | Old Dominion -8.9 / Old Dominion -5.8 | 46.8 / 50.8 | no edge | no edge | no edge |  |
| Sat 11/28 2:00 PM | UCF @ Colorado | UCF 24, Colorado 27 | Colorado 56% | UCF +130 / Colorado -130 | 24.0 – 26.2 | 10–38 / 13–41 | Colorado -1.8 / Colorado -2.2 | 51.6 / 50.0 | no edge | no edge | no edge |  |
| Sat 11/28 2:00 PM | Kansas State @ Iowa State | Kansas State 24, Iowa State 27 | Iowa State 59% | Kansas State +140 / Iowa State -140 | 24.8 – 28.3 | 12–39 / 14–42 | Iowa State -2.9 / Iowa State -3.5 | 53.3 / 53.2 | no edge | no edge | no edge |  |
| Sat 11/28 2:00 PM | Army @ Rice | Army 28, Rice 21 | Army 66% | Army -195 / Rice +195 | 27.9 – 22.1 | 14–42 / 10–35 | Army -6.1 / Army -5.8 | 56.8 / 48.5 | no edge | no edge | no edge |  |
| Sat 11/28 2:00 PM | Coastal Carolina @ James Madison | Coastal Carolina 17, James Madison 34 | James Madison 88% | Coastal Carolina +715 / James Madison -715 | 18.4 – 35.6 | 7–31 / 20–51 | James Madison -16.2 / James Madison -17.2 | 51.5 / 54.5 | no edge | no edge | no edge |  |
| Sat 11/28 2:00 PM | Louisiana @ Georgia State | Louisiana 31, Georgia State 24 | Louisiana 62% | Louisiana -165 / Georgia State +165 | 30.3 – 25.4 | 17–45 / 13–39 | Louisiana -1.4 / Louisiana -5.2 | 55.7 / 55.8 | no edge | no edge | no edge |  |
| Sat 11/28 2:00 PM | Liberty @ Missouri State | Liberty 34, Missouri State 17 | Liberty 87% | Liberty -690 / Missouri State +690 | 35.0 – 18.2 | 20–51 / 7–31 | Liberty -17.2 / Liberty -16.8 | 52.8 / 53.2 | no edge | no edge | no edge |  |
| Sat 11/28 2:00 PM | Sam Houston @ Florida International | Sam Houston 17, Florida International 24 | Florida International 78% | Sam Houston +365 / Florida International -365 | 15.2 – 26.2 | 3–27 / 13–41 | Florida International -8.5 / Florida International -11.2 | 40.6 / 41.5 | no edge | no edge | no edge |  |
| Sat 11/28 2:00 PM | New Mexico State @ Middle Tennessee | New Mexico State 24, Middle Tennessee 27 | Middle Tennessee 59% | New Mexico State +145 / Middle Tennessee -145 | 24.1 – 27.3 | 10–38 / 14–42 | Middle Tennessee -5.6 / Middle Tennessee -3.0 | 51.2 / 51.5 | no edge | no edge | no edge |  |
| Sat 11/28 3:00 PM | South Carolina @ Clemson | South Carolina 24, Clemson 17 | South Carolina 65% | South Carolina -190 / Clemson +190 | 24.1 – 18.5 | 10–38 / 7–31 | PK / South Carolina -6.2 | 46.6 / 41.8 | no edge | Clemson (+180): EV +3.1%, 37%, stake 0.4u | no edge |  |
| Sat 11/28 3:00 PM | Virginia @ Virginia Tech | Virginia 24, Virginia Tech 27 | Virginia Tech 58% | Virginia +135 / Virginia Tech -135 | 24.3 – 27.0 | 10–38 / 13–41 | Virginia -0.3 / Virginia Tech -3.0 | 50.8 / 51.5 | no edge | no edge | no edge |  |
| Sat 11/28 3:00 PM | Troy @ Arkansas State | Troy 21, Arkansas State 24 | Arkansas State 60% | Troy +150 / Arkansas State -150 | 21.4 – 25.1 | 9–35 / 12–38 | Arkansas State -3.1 / Arkansas State -3.8 | 47.2 / 46.5 | no edge | no edge | no edge |  |
| Sat 11/28 3:30 PM | Georgia Tech @ Georgia | Georgia Tech 10, Georgia 45 | Georgia 100% | Georgia Tech +9900 / Georgia -9900 | 9.3 – 45.0 | 0–18 / 30–61 | Georgia -38.2 / Georgia -35.5 | 50.1 / 55.2 | no edge | no edge | no edge |  |
| Sat 11/28 3:30 PM | Cincinnati @ BYU | Cincinnati 21, BYU 35 | BYU 84% | Cincinnati +510 / BYU -510 | 20.7 – 35.8 | 7–35 / 21–51 | BYU -11.1 / BYU -15.5 | 57.7 / 56.2 | no edge | Cincinnati (+500): EV +3.2%, 17%, stake 0.2u | no edge |  |
| Sat 11/28 3:30 PM | Duke @ Wake Forest | Duke 20, Wake Forest 34 | Wake Forest 84% | Duke +540 / Wake Forest -540 | 20.1 – 34.9 | 7–34 / 20–50 | Wake Forest -17.4 / Wake Forest -14.5 | 52.5 / 55.5 | no edge | no edge | no edge |  |
| Sat 11/28 3:30 PM | SMU @ Stanford | SMU 31, Stanford 24 | SMU 70% | SMU -230 / Stanford +230 | 34.0 – 26.1 | 20–49 / 13–41 | SMU -12.2 / SMU -7.5 | 57.1 / 60.8 | no edge | no edge | no edge |  |
| Sat 11/28 3:30 PM | Penn State @ Maryland | Penn State 28, Maryland 21 | Penn State 68% | Penn State -210 / Maryland +210 | 28.0 – 21.2 | 14–42 / 9–34 | Penn State -5.5 / Penn State -7.0 | 46.6 / 49.8 | no edge | no edge | no edge |  |
| Sat 11/28 3:30 PM | USC @ UCLA | USC 24, UCLA 21 | USC 65% | USC -185 / UCLA +185 | 26.3 – 20.7 | 13–41 / 9–34 | UCLA -7.3 / USC -7.0 | 52.4 / 45.8 | no edge | UCLA (+220): EV +4.4%, 33%, stake 0.5u | no edge |  |
| Sat 11/28 3:30 PM | Tulane @ South Florida | Tulane 17, South Florida 24 | South Florida 67% | Tulane +205 / South Florida -205 | 19.3 – 25.6 | 7–31 / 13–40 | South Florida -4.8 / South Florida -6.5 | 51.4 / 43.5 | no edge | no edge | no edge |  |
| Sat 11/28 3:30 PM | UTEP @ Northern Illinois | UTEP 24, Northern Illinois 27 | Northern Illinois 63% | UTEP +170 / Northern Illinois -170 | 22.8 – 27.5 | 10–36 / 14–42 | Northern Illinois -9.3 / Northern Illinois -4.2 | 50.9 / 50.2 | no edge | no edge | no edge |  |
| Sat 11/28 3:30 PM | Massachusetts @ Bowling Green | Massachusetts 21, Bowling Green 24 | Bowling Green 59% | Massachusetts +140 / Bowling Green -140 | 19.8 – 22.9 | 7–33 / 10–37 | Bowling Green -3.8 / Bowling Green -3.0 | 39.8 / 43.5 | no edge | no edge | no edge |  |
| Sat 11/28 3:30 PM | Jacksonville State @ Delaware | Jacksonville State 28, Delaware 31 | Delaware 57% | Jacksonville State +130 / Delaware -130 | 27.9 – 30.3 | 14–42 / 16–45 | Delaware -1.5 / Delaware -2.5 | 58.0 / 58.2 | no edge | no edge | no edge |  |
| Sat 11/28 4:00 PM | UAB @ North Texas | UAB 21, North Texas 24 | North Texas 61% | UAB +160 / North Texas -160 | 21.7 – 25.8 | 10–35 / 13–41 | North Texas -10.0 / North Texas -3.5 | 57.3 / 45.8 | no edge | no edge | Over 45.75 (-110*): EV +4.2%, 55%, stake 1.2u | * price not posted; assumed -110 |
| Sat 11/28 4:15 PM | Oklahoma @ Missouri | Oklahoma 17, Missouri 20 | Missouri 55% | Oklahoma +125 / Missouri -125 | 19.8 – 21.8 | 7–33 / 10–35 | Oklahoma -2.8 / Missouri -2.5 | 42.3 / 41.5 | no edge | no edge | no edge |  |
| Sat 11/28 4:15 PM | Michigan State @ Rutgers | Michigan State 24, Rutgers 21 | Michigan State 58% | Michigan State -140 / Rutgers +140 | 25.6 – 22.5 | 13–40 / 10–35 | Rutgers -0.6 / Michigan State -3.5 | 51.0 / 47.5 | no edge | no edge | no edge |  |
| Sat 11/28 6:00 PM | Boise State @ Colorado State | Boise State 48, Colorado State 27 | Boise State 90% | Boise State -870 / Colorado State +870 | 47.7 – 27.4 | 31–63 / 13–42 | Boise State -13.3 / Boise State -21.0 | 68.6 / 76.5 | no edge | Colorado State (+948): EV +6.8%, 10%, stake 0.2u | no edge |  |
| Sat 11/28 6:15 PM | Kansas @ Oklahoma State | Kansas 27, Oklahoma State 34 | Oklahoma State 66% | Kansas +195 / Oklahoma State -195 | 29.0 – 35.2 | 14–44 / 20–50 | Oklahoma State -3.1 / Oklahoma State -6.5 | 59.4 / 65.2 | no edge | no edge | no edge |  |
| Sat 11/28 6:30 PM | San Diego State @ Washington State | San Diego State 21, Washington State 24 | Washington State 57% | San Diego State +135 / Washington State -135 | 22.2 – 24.6 | 10–35 / 10–38 | San Diego State -0.9 / Washington State -2.8 | 48.3 / 46.5 | no edge | no edge | no edge |  |
| Sat 11/28 7:00 PM | Tennessee @ Vanderbilt | Tennessee 31, Vanderbilt 17 | Tennessee 84% | Tennessee -525 / Vanderbilt +525 | 28.7 – 15.2 | 14–44 / 3–27 | Tennessee -13.8 / Tennessee -13.5 | 45.6 / 43.5 | no edge | no edge | no edge |  |
| Sat 11/28 7:00 PM | Purdue @ Indiana | Purdue 17, Indiana 38 | Indiana 95% | Purdue +1765 / Indiana -1765 | 14.7 – 37.2 | 3–27 / 22–53 | Indiana -25.2 / Indiana -22.2 | 49.8 / 52.5 | no edge | no edge | no edge |  |
| Sat 11/28 7:30 PM | Auburn @ Alabama | Auburn 17, Alabama 31 | Alabama 83% | Auburn +490 / Alabama -490 | 17.8 – 31.9 | 7–30 / 17–47 | Alabama -9.9 / Alabama -14.5 | 51.5 / 49.2 | no edge | Auburn (+535): EV +4.7%, 16%, stake 0.2u | no edge |  |
| Sat 11/28 7:30 PM | Pittsburgh @ California | Pittsburgh 28, California 21 | Pittsburgh 74% | Pittsburgh -290 / California +290 | 28.6 – 19.2 | 14–43 / 7–31 | Pittsburgh -8.7 / Pittsburgh -9.5 | 49.4 / 47.5 | no edge | no edge | no edge |  |
| Sat 11/28 7:30 PM | Washington @ Oregon | Washington 17, Oregon 31 | Oregon 83% | Washington +505 / Oregon -505 | 18.1 – 32.1 | 7–31 / 17–47 | Oregon -13.8 / Oregon -14.0 | 48.9 / 50.5 | no edge | no edge | no edge |  |
| Sat 11/28 9:00 PM | Arizona State @ Arizona | Arizona State 24, Arizona 31 | Arizona 72% | Arizona State +255 / Arizona -255 | 22.7 – 31.0 | 10–36 / 17–46 | Arizona -7.1 / Arizona -8.5 | 53.4 / 53.8 | no edge | no edge | no edge |  |
| Sat 11/28 9:00 PM | Nevada @ UNLV | Nevada 17, UNLV 24 | UNLV 66% | Nevada +200 / UNLV -200 | 19.4 – 25.3 | 7–32 / 13–40 | UNLV -9.6 / UNLV -5.5 | 45.5 / 44.5 | no edge | no edge | no edge |  |
| Sat 11/28 9:30 PM | Baylor @ Houston | Baylor 28, Houston 31 | Houston 62% | Baylor +165 / Houston -165 | 25.7 – 30.2 | 13–40 / 16–45 | Houston -1.9 / Houston -4.8 | 57.3 / 55.5 | no edge | no edge | no edge |  |
| Sat 11/28 9:30 PM | Texas State @ Utah State | Texas State 31, Utah State 24 | Texas State 68% | Texas State -215 / Utah State +215 | 30.2 – 23.0 | 16–45 / 10–37 | Texas State -8.8 / Texas State -7.0 | 57.2 / 52.2 | no edge | no edge | no edge |  |
| Sat 11/28 10:00 PM | Oregon State @ Fresno State | Oregon State 28, Fresno State 31 | Fresno State 56% | Oregon State +130 / Fresno State -130 | 27.6 – 30.2 | 14–42 / 16–45 | Oregon State -0.8 / Fresno State -3.0 | 58.3 / 57.8 | no edge | no edge | no edge |  |
| Sat 11/28 11:00 PM | Sacramento State @ Hawai'i | Sacramento State 14, Hawai'i 28 | Hawai'i 84% | Sacramento State +535 / Hawai'i -535 | 13.7 – 27.2 | 3–24 / 13–42 | Hawai'i -12.7 / Hawai'i -13.5 | 47.4 / 39.5 | no edge | no edge | no edge |  |

## 2026 Week 14

| Kickoff (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected points | 80% range | Spread: model / line | Total: model / line | Spread edge | Moneyline edge | Total edge | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Fri 12/04 7:00 PM | Jacksonville State @ Liberty | Jacksonville State 21, Liberty 31 | Liberty 76% | Jacksonville State +320 / Liberty -320 | 20.4 – 30.9 | 7–34 / 17–45 | Liberty -10.5 / – | 51.2 / – | no line yet | no line yet (fair: Liberty -320) | no line yet |  |
| Fri 12/04 8:00 PM | San Diego State @ Boise State | San Diego State 21, Boise State 38 | Boise State 85% | San Diego State +550 / Boise State -550 | 21.1 – 36.2 | 7–35 / 21–52 | Boise State -12.0 / Boise State -15.5 | 56.4 / 57.5 | no edge | no edge | no edge |  |
| Sat 12/05 12:00 PM | Wake Forest vs Miami | Wake Forest 28, Miami 31 | Miami 57% | Wake Forest +135 / Miami -135 | 27.5 – 29.8 | 14–42 / 16–45 | Miami -0.8 / Miami -2.5 | 56.4 / 57.5 | no edge | no edge | no edge | neutral site |

## How the 2026 predictions have done

| Predictor | Games | Margin MAE | Total MAE | Team-score MAE | Winners | Brier | 80% range hit |
|---|---|---|---|---|---|---|---|
| Final prediction | 822 | 11.80 | 12.17 | 8.48 | 78.0% | 0.150 | 81.7% |
| Model only (before blending) | 822 | 12.43 | 12.52 | 8.73 | 75.8% | – | – |
| Betting line when predicted | 820 | 11.79 | 12.13 | 8.48 | 78.0% | – | – |

MAE is mean absolute error in points (lower is better). Brier scores the win chances (lower is better, 0.25 is a coin flip). Even the closing betting line misses the final margin of an FBS game by about 12.5 points.

501 of these games were played before the predictor went live. They are backfilled walk-forward (each week predicted from earlier weeks only) but with closing lines, so they flatter the model slightly. Every game since is graded on the prediction logged before kickoff.

### Betting edges

| Market | Edges | Record (W-L-P) | Staked | Units won | ROI | Expected ROI |
|---|---|---|---|---|---|---|
| Spread | 0 | 0-0-0 | 0.0 | +0.00 | – | – |
| Moneyline | 12 | 2-10-0 | 3.7 | -0.01 | -0.2% | +4.8% |
| Total | 10 | 5-5-0 | 13.6 | -1.01 | -7.4% | +6.9% |

10 of these edges were priced at an assumed -110 (price not posted).

Every edge logged before kickoff at the stake and price logged with it (backfilled games, and edges logged before edges were priced from the final prediction, are not included). Units are 1% of the bankroll; ROI is units won per unit staked, pushes returning the stake, and expected ROI is what the edges' EVs promised.

### Week 12 results

| Game | Predicted | Final | Win chance for winner | Inside 80% ranges |
|---|---|---|---|---|
| Eastern Michigan @ Western Michigan | 14–31 | 27–34 | 87% | yes |
| Ball State @ Ohio | 21–31 | 28–35 | 76% | yes |
| Miami (OH) @ Kent State | 24–17 | 20–3 | 75% | no |
| Akron @ Massachusetts | 21–24 | 34–33 | 40% | yes |
| Central Michigan @ Buffalo | 21–24 | 21–40 | 56% | no |
| Rice @ Temple | 24–27 | 31–27 | 43% | yes |
| Iowa State @ UCF | 27–24 | 17–48 | 46% | no |
| Clemson @ Duke | 17–24 | 20–10 | 21% | no |
| Bowling Green @ Toledo | 14–31 | 0–19 | 88% | no |
| Oregon @ Michigan State | 31–14 | 45–7 | 90% | yes |
| UTEP @ Air Force | 13–34 | 3–52 | 95% | yes |
| New Mexico @ Wyoming | 24–17 | 24–17 | 75% | yes |
| Vanderbilt @ Florida | 17–31 | 27–34 | 82% | yes |
| Wofford @ Ole Miss | 3–55 | 17–59 | 100% | no |
| BYU @ Kansas | 24–21 | 31–29 | 62% | yes |
| Colorado @ Cincinnati | 28–31 | 28–35 | 58% | yes |
| Syracuse @ Boston College | 27–24 | 15–27 | 41% | yes |
| Wake Forest @ Georgia Tech | 38–17 | 50–29 | 92% | yes |
| Northwestern @ Minnesota | 24–21 | 17–20 | 43% | yes |
| Ohio State @ Nebraska | 24–21 | 28–31 | 39% | yes |
| Wisconsin @ Purdue | 24–21 | 42–10 | 66% | no |
| East Carolina @ Army | 21–24 | 10–6 | 35% | no |
| Memphis @ Navy | 34–31 | 34–38 | 43% | yes |
| North Texas @ Tulane | 31–24 | 24–28 | 34% | yes |
| North Carolina @ Virginia | 21–24 | 24–41 | 55% | no |
| Tennessee Tech @ Mississippi State | 10–45 | 16–34 | 99% | yes |
| Houston @ West Virginia | 38–31 | 34–31 | 68% | yes |
| Western Kentucky @ Liberty | 17–34 | 14–45 | 88% | yes |
| Chattanooga @ Alabama | 3–52 | 0–47 | 100% | yes |
| Charlotte @ Tulsa | 14–38 | 14–42 | 95% | yes |
| Missouri State @ Jacksonville State | 21–31 | 20–25 | 77% | yes |
| Middle Tennessee @ Sam Houston | 27–24 | 31–28 | 66% | yes |
| Iowa @ Illinois | 24–17 | 34–17 | 74% | yes |
| South Florida @ Florida Atlantic | 34–31 | 14–35 | 48% | no |
| UL Monroe @ App State | 17–31 | 16–17 | 82% | yes |
| Coastal Carolina @ Louisiana | 21–31 | 24–38 | 75% | yes |
| Delaware @ New Mexico State | 27–24 | 42–30 | 59% | yes |
| Florida International @ Kennesaw State | 21–24 | 24–35 | 58% | yes |
| Samford @ Auburn | 3–52 | 17–59 | 100% | no |
| LSU @ Tennessee | 24–21 | 13–27 | 47% | yes |
| Arkansas @ Texas | 14–31 | 3–45 | 91% | yes |
| Texas Tech @ Baylor | 31–24 | 20–10 | 64% | no |
| NC State @ Florida State | 24–34 | 28–10 | 26% | no |
| UCLA @ Michigan | 20–17 | 16–18 | 40% | yes |
| Rutgers @ Penn State | 10–38 | 25–24 | 4% | no |
| Indiana @ Washington | 24–17 | 24–27 | 26% | yes |
| Old Dominion @ UConn | 17–31 | 21–29 | 84% | yes |
| Texas A&M @ Oklahoma | 17–24 | 7–28 | 70% | yes |
| Northern Illinois @ North Dakota State | 10–38 | 25–31 | 97% | no |
| Georgia Southern @ Troy | 28–21 | 45–7 | 73% | no |
| Georgia State @ Marshall | 28–31 | 27–28 | 58% | yes |
| South Alabama @ Southern Miss | 34–31 | 40–35 | 62% | yes |
| Washington State @ Texas State | 24–38 | 14–42 | 80% | yes |
| Maryland @ USC | 21–38 | 21–35 | 87% | yes |
| Arizona @ Kansas State | 31–24 | 35–28 | 74% | yes |
| Virginia Tech @ Miami | 17–38 | 20–28 | 92% | yes |
| UNLV @ San José State | 28–21 | 24–22 | 68% | yes |
| Arkansas State @ Louisiana Tech | 20–34 | 3–48 | 84% | no |
| Kentucky @ Missouri | 24–27 | 14–28 | 63% | yes |
| Georgia @ South Carolina | 31–17 | 34–6 | 84% | no |
| Pittsburgh @ Louisville | 21–31 | 10–42 | 79% | yes |
| SMU @ Notre Dame | 17–38 | 3–24 | 92% | no |
| Stanford @ California | 27–24 | 44–28 | 56% | no |
| Colorado State @ Fresno State | 24–45 | 42–49 | 89% | no |
| UTSA @ UAB | 27–24 | 19–17 | 61% | yes |
| Utah @ TCU | 24–17 | 38–17 | 73% | yes |
| San Diego State @ Boise State | 20–41 | 22–20 | 9% | no |
| Oklahoma State @ Arizona State | 31–28 | 30–27 | 55% | yes |
| Utah State @ Oregon State | 24–31 | 24–31 | 69% | yes |
| Hawai'i @ Nevada | 17–24 | 8–16 | 67% | yes |

## FBS power ratings

Points per game better than an average FBS team on a neutral field, from opponent-adjusted EPA (garbage time removed) with this season's games weighted against a preseason prior, plus the weight the margin model puts on Elo (a rating built from game results alone). Defense is positive when it holds opponents below average.

| # | Team | Conference | Net | Offense | Defense | Special teams | Results (Elo) | Elo rating |
|---|---|---|---|---|---|---|---|---|
| 1 | Georgia | SEC | +28.6 | +9.5 | +12.5 | +1.0 | +5.6 | 1958 |
| 2 | Notre Dame | FBS Independents | +24.8 | +8.7 | +10.1 | +1.1 | +4.9 | 1904 |
| 3 | Ohio State | Big Ten | +23.0 | +11.1 | +8.1 | +0.4 | +3.4 | 1784 |
| 4 | LSU | SEC | +22.9 | +7.7 | +13.4 | -0.3 | +2.0 | 1672 |
| 5 | Miami | ACC | +22.8 | +13.9 | +3.9 | +0.4 | +4.7 | 1885 |
| 6 | Utah | Big 12 | +22.5 | +11.4 | +6.3 | +0.1 | +4.7 | 1888 |
| 7 | Alabama | SEC | +22.0 | +8.3 | +9.0 | +0.6 | +4.1 | 1842 |
| 8 | Texas | SEC | +21.9 | +3.5 | +12.8 | +1.1 | +4.4 | 1866 |
| 9 | Wake Forest | ACC | +21.9 | +8.8 | +9.0 | +0.5 | +3.5 | 1790 |
| 10 | Oregon | Big Ten | +21.3 | +6.6 | +9.9 | +0.8 | +4.1 | 1835 |
| 11 | Indiana | Big Ten | +20.8 | +5.3 | +9.9 | +0.4 | +5.1 | 1916 |
| 12 | Tennessee | SEC | +19.6 | +2.5 | +11.8 | +1.5 | +3.7 | 1807 |
| 13 | Texas Tech | Big 12 | +19.6 | +2.4 | +11.7 | +1.6 | +3.8 | 1814 |
| 14 | Oklahoma | SEC | +18.6 | +1.9 | +13.4 | +0.7 | +2.6 | 1718 |
| 15 | UCLA | Big Ten | +17.9 | +4.4 | +10.3 | +0.7 | +2.5 | 1708 |
| 16 | Ole Miss | SEC | +17.7 | +11.1 | +3.3 | +0.6 | +2.7 | 1729 |
| 17 | Louisville | ACC | +17.1 | +8.2 | +5.6 | +0.6 | +2.8 | 1730 |
| 18 | Iowa | Big Ten | +16.4 | +2.0 | +9.7 | +0.9 | +3.8 | 1816 |
| 19 | Auburn | SEC | +14.6 | +6.5 | +6.4 | +0.5 | +1.2 | 1605 |
| 20 | Missouri | SEC | +13.8 | +4.3 | +7.0 | +0.2 | +2.3 | 1692 |
| 21 | Nebraska | Big Ten | +13.8 | +5.1 | +6.9 | +0.3 | +1.4 | 1622 |
| 22 | USC | Big Ten | +13.4 | +10.4 | +0.1 | +0.2 | +2.8 | 1731 |
| 23 | BYU | Big 12 | +12.8 | +4.1 | +4.6 | +0.8 | +3.3 | 1771 |
| 24 | Florida | SEC | +12.2 | +6.3 | +4.3 | +0.4 | +1.2 | 1603 |
| 25 | Penn State | Big Ten | +11.6 | +3.3 | +6.5 | +0.1 | +1.7 | 1644 |
| 26 | Michigan | Big Ten | +11.4 | +1.1 | +9.0 | -0.0 | +1.2 | 1608 |
| 27 | Arizona | Big 12 | +11.1 | +5.6 | +2.8 | +0.0 | +2.6 | 1718 |
| 28 | Washington | Big Ten | +10.7 | +3.4 | +4.9 | +0.1 | +2.4 | 1698 |
| 29 | SMU | ACC | +10.0 | +6.2 | +2.2 | +0.2 | +1.4 | 1625 |
| 30 | Houston | Big 12 | +9.7 | +8.8 | -1.0 | +0.2 | +1.6 | 1633 |
| 31 | Baylor | Big 12 | +9.6 | +0.5 | +7.3 | +0.8 | +0.9 | 1583 |
| 32 | South Carolina | SEC | +9.4 | +4.4 | +3.7 | +0.3 | +1.0 | 1588 |
| 33 | Oklahoma State | Big 12 | +9.1 | +8.5 | -0.1 | +0.1 | +0.6 | 1560 |
| 34 | Northwestern | Big Ten | +9.0 | +6.0 | +1.7 | +0.6 | +0.7 | 1567 |
| 35 | Wisconsin | Big Ten | +8.8 | -0.1 | +7.1 | +0.6 | +1.2 | 1605 |
| 36 | Kansas | Big 12 | +8.5 | +4.8 | +4.0 | -0.0 | -0.3 | 1488 |
| 37 | Texas A&M | SEC | +7.8 | -0.1 | +7.3 | +0.3 | +0.3 | 1533 |
| 38 | Kentucky | SEC | +6.8 | +2.6 | +3.1 | +0.4 | +0.7 | 1568 |
| 39 | Duke | ACC | +6.7 | +3.4 | +1.1 | +0.6 | +1.6 | 1639 |
| 40 | Arizona State | Big 12 | +6.2 | +1.7 | +3.7 | +0.2 | +0.8 | 1569 |
| 41 | Kansas State | Big 12 | +6.1 | +4.1 | +2.9 | +0.1 | -1.1 | 1424 |
| 42 | Mississippi State | SEC | +5.7 | +2.7 | +3.6 | +0.1 | -0.7 | 1449 |
| 43 | Iowa State | Big 12 | +5.6 | +4.5 | +0.1 | +1.0 | +0.0 | 1512 |
| 44 | Boise State | Pac-12 | +4.9 | +6.4 | -3.8 | -0.1 | +2.4 | 1701 |
| 45 | Clemson | ACC | +4.8 | -6.2 | +8.6 | +1.1 | +1.2 | 1608 |
| 46 | Cincinnati | Big 12 | +4.7 | +9.1 | -4.7 | +0.1 | +0.2 | 1526 |
| 47 | Illinois | Big Ten | +4.7 | +5.1 | -1.7 | +0.3 | +1.0 | 1590 |
| 48 | TCU | Big 12 | +4.6 | -2.4 | +6.1 | +0.0 | +0.9 | 1581 |
| 49 | UCF | Big 12 | +4.6 | +2.9 | +2.0 | -0.2 | -0.0 | 1505 |
| 50 | Colorado | Big 12 | +4.3 | +2.0 | +3.9 | -0.4 | -1.2 | 1413 |
| 51 | Vanderbilt | SEC | +4.1 | +2.2 | +1.2 | +0.8 | +0.0 | 1510 |
| 52 | Virginia | ACC | +3.9 | -0.3 | +3.5 | +0.1 | +0.6 | 1559 |
| 53 | NC State | ACC | +3.9 | +5.9 | -1.6 | -0.7 | +0.3 | 1529 |
| 54 | Maryland | Big Ten | +3.5 | +0.5 | +4.0 | +0.4 | -1.3 | 1400 |
| 55 | Florida State | ACC | +3.2 | +4.8 | -0.9 | -0.3 | -0.4 | 1477 |
| 56 | Texas State | Pac-12 | +2.9 | +7.6 | -5.3 | -0.8 | +1.5 | 1628 |
| 57 | Minnesota | Big Ten | +2.6 | -3.0 | +4.6 | +0.8 | +0.2 | 1526 |
| 58 | North Carolina | ACC | +2.4 | +3.7 | -1.3 | +0.1 | -0.1 | 1503 |
| 59 | Memphis | American Athletic | +2.3 | +4.7 | -3.0 | -0.7 | +1.4 | 1618 |
| 60 | Arkansas | SEC | +2.1 | +1.3 | +1.0 | -0.4 | +0.2 | 1525 |
| 61 | UTSA | American Athletic | +2.0 | +1.6 | -1.3 | -0.1 | +1.8 | 1651 |
| 62 | Pittsburgh | ACC | +1.8 | -4.1 | +5.4 | +0.5 | -0.0 | 1506 |
| 63 | Virginia Tech | ACC | +1.5 | +2.0 | +0.2 | -0.2 | -0.5 | 1471 |
| 64 | Tulsa | American Athletic | +1.4 | -0.1 | +2.2 | -0.7 | +0.1 | 1517 |
| 65 | Syracuse | ACC | +1.4 | +1.3 | +2.3 | -0.8 | -1.4 | 1392 |
| 66 | Liberty | Conference USA | +1.3 | +1.3 | -1.2 | +0.2 | +1.0 | 1591 |
| 67 | James Madison | Sun Belt | +1.1 | -0.6 | +0.1 | +0.2 | +1.4 | 1625 |
| 68 | Louisiana Tech | Sun Belt | +1.0 | -1.6 | +2.0 | -0.7 | +1.2 | 1607 |
| 69 | Oregon State | Pac-12 | +0.4 | +4.8 | -3.5 | -0.1 | -0.8 | 1448 |
| 70 | North Texas | American Athletic | +0.4 | +7.4 | -7.0 | -0.8 | +0.8 | 1573 |
| 71 | Toledo | Mid-American | +0.1 | -3.6 | +3.2 | -0.3 | +0.9 | 1577 |
| 72 | Navy | American Athletic | -0.5 | +3.6 | -3.8 | -0.4 | +0.1 | 1518 |
| 73 | New Mexico | Mountain West | -0.7 | -4.0 | +2.2 | -0.2 | +1.4 | 1620 |
| 74 | West Virginia | Big 12 | -1.1 | +4.9 | -5.2 | +0.3 | -1.1 | 1417 |
| 75 | UConn | FBS Independents | -1.5 | +3.0 | -4.7 | -0.1 | +0.3 | 1530 |
| 76 | North Dakota State | Mountain West | -2.0 | -5.4 | +3.1 | +1.0 | -0.6 | 1457 |
| 77 | East Carolina | American Athletic | -2.1 | -6.6 | +4.6 | -0.8 | +0.5 | 1552 |
| 78 | Purdue | Big Ten | -2.5 | +2.8 | -4.3 | +0.9 | -2.0 | 1351 |
| 79 | Michigan State | Big Ten | -3.1 | -3.2 | +1.1 | -0.1 | -1.0 | 1428 |
| 80 | Air Force | Mountain West | -3.2 | +2.3 | -6.0 | +0.0 | +0.4 | 1538 |
| 81 | Florida Atlantic | American Athletic | -3.5 | +3.2 | -7.5 | +0.8 | +0.1 | 1513 |
| 82 | South Florida | American Athletic | -3.6 | -1.2 | -2.1 | +0.0 | -0.3 | 1482 |
| 83 | Georgia Southern | Sun Belt | -3.6 | -1.3 | -3.1 | -0.5 | +1.3 | 1610 |
| 84 | San Diego State | Pac-12 | -3.7 | -3.6 | -0.1 | +0.3 | -0.3 | 1483 |
| 85 | Fresno State | Pac-12 | -4.3 | -1.2 | -3.2 | -0.1 | +0.2 | 1527 |
| 86 | Georgia Tech | ACC | -4.5 | +0.9 | -4.3 | -0.3 | -0.8 | 1440 |
| 87 | Stanford | ACC | -4.6 | -1.0 | -4.3 | +0.3 | +0.4 | 1540 |
| 88 | UNLV | Mountain West | -5.0 | -2.5 | -3.3 | +0.3 | +0.4 | 1544 |
| 89 | Jacksonville State | Conference USA | -5.1 | -0.8 | -3.8 | +0.0 | -0.6 | 1462 |
| 90 | Army | American Athletic | -5.1 | +3.4 | -8.4 | -0.0 | -0.1 | 1497 |
| 91 | Rutgers | Big Ten | -5.6 | +1.6 | -6.0 | +0.6 | -1.8 | 1364 |
| 92 | Miami (OH) | Mid-American | -5.8 | -4.1 | -2.3 | +0.7 | -0.1 | 1500 |
| 93 | Delaware | Conference USA | -6.0 | +1.7 | -6.8 | +0.0 | -0.9 | 1438 |
| 94 | Western Michigan | Mid-American | -6.2 | -3.7 | -3.8 | +0.5 | +0.9 | 1580 |
| 95 | Tulane | American Athletic | -6.2 | -4.1 | -2.2 | +0.2 | -0.2 | 1496 |
| 96 | Boston College | ACC | -6.3 | -3.8 | -1.3 | -0.6 | -0.6 | 1459 |
| 97 | Ohio | Mid-American | -6.5 | -3.5 | -3.2 | -0.1 | +0.3 | 1532 |
| 98 | Washington State | Pac-12 | -7.4 | -4.6 | -0.3 | -0.8 | -1.7 | 1374 |
| 99 | UAB | American Athletic | -8.0 | -7.1 | +0.0 | -0.1 | -0.8 | 1445 |
| 100 | California | ACC | -8.0 | -2.1 | -2.7 | -0.8 | -2.4 | 1317 |
| 101 | Louisiana | Sun Belt | -8.0 | -3.2 | -5.0 | +0.0 | +0.2 | 1524 |
| 102 | Utah State | Pac-12 | -9.4 | -8.7 | +2.1 | -1.2 | -1.5 | 1386 |
| 103 | App State | Sun Belt | -9.7 | -4.4 | -2.9 | -1.0 | -1.3 | 1400 |
| 104 | Wyoming | Mountain West | -9.8 | -5.2 | -3.6 | -0.2 | -0.8 | 1447 |
| 105 | Kennesaw State | Conference USA | -10.4 | -4.5 | -3.9 | -0.8 | -1.2 | 1412 |
| 106 | Marshall | Sun Belt | -10.5 | -5.2 | -4.3 | +0.0 | -1.0 | 1428 |
| 107 | South Alabama | Sun Belt | -10.7 | +1.1 | -11.2 | +0.3 | -0.9 | 1440 |
| 108 | Old Dominion | Sun Belt | -11.4 | -11.8 | +3.6 | -1.7 | -1.5 | 1389 |
| 109 | Georgia State | Sun Belt | -11.5 | -1.3 | -8.1 | -0.3 | -1.7 | 1370 |
| 110 | Western Kentucky | Conference USA | -12.2 | -5.8 | -3.8 | -0.5 | -2.1 | 1343 |
| 111 | Colorado State | Pac-12 | -12.2 | +6.5 | -15.0 | -0.2 | -3.5 | 1231 |
| 112 | Hawai'i | Mountain West | -12.4 | -6.0 | -4.9 | +1.0 | -2.4 | 1313 |
| 113 | Nevada | Mountain West | -12.6 | -11.1 | -0.4 | +0.7 | -1.8 | 1365 |
| 114 | Coastal Carolina | Sun Belt | -12.7 | -7.0 | -4.0 | +0.2 | -2.0 | 1349 |
| 115 | Rice | American Athletic | -12.7 | -2.4 | -6.3 | -0.9 | -3.1 | 1258 |
| 116 | Troy | Sun Belt | -12.9 | -8.9 | -0.2 | -1.3 | -2.5 | 1311 |
| 117 | Temple | American Athletic | -13.1 | -0.4 | -8.5 | -0.5 | -3.7 | 1214 |
| 118 | Central Michigan | Mid-American | -13.2 | -5.9 | -6.1 | +0.1 | -1.4 | 1400 |
| 119 | Buffalo | Mid-American | -13.3 | -9.2 | -4.5 | +0.3 | +0.2 | 1521 |
| 120 | Arkansas State | Sun Belt | -13.5 | -4.2 | -7.4 | +0.0 | -1.9 | 1356 |
| 121 | Florida International | Conference USA | -14.6 | -8.3 | -2.7 | -1.2 | -2.4 | 1315 |
| 122 | Middle Tennessee | Conference USA | -15.4 | -4.7 | -8.3 | +0.2 | -2.6 | 1303 |
| 123 | San José State | Mountain West | -15.8 | -9.7 | -3.0 | -0.4 | -2.7 | 1295 |
| 124 | New Mexico State | Conference USA | -16.7 | -7.3 | -4.0 | -1.7 | -3.7 | 1211 |
| 125 | Missouri State | Conference USA | -17.0 | -5.3 | -7.8 | -1.0 | -2.8 | 1280 |
| 126 | UL Monroe | Sun Belt | -17.5 | -5.8 | -6.4 | -1.2 | -4.1 | 1181 |
| 127 | Bowling Green | Mid-American | -18.0 | -12.1 | -2.9 | -0.1 | -2.8 | 1280 |
| 128 | Southern Miss | Sun Belt | -18.2 | -8.6 | -5.5 | -1.3 | -2.8 | 1283 |
| 129 | Northern Illinois | Mountain West | -18.4 | -2.9 | -9.0 | -1.4 | -5.1 | 1097 |
| 130 | Eastern Michigan | Mid-American | -18.6 | -7.2 | -8.0 | -0.6 | -2.8 | 1280 |
| 131 | Massachusetts | Mid-American | -19.1 | -9.8 | -5.1 | -0.4 | -3.7 | 1207 |
| 132 | Ball State | Mid-American | -19.2 | -6.3 | -8.6 | -0.6 | -3.7 | 1212 |
| 133 | Sacramento State | Mid-American | -20.4 | -11.2 | -4.7 | +0.2 | -4.6 | 1136 |
| 134 | Sam Houston | Conference USA | -20.8 | -13.1 | -1.5 | -1.2 | -5.1 | 1102 |
| 135 | Charlotte | American Athletic | -21.2 | -9.6 | -7.0 | -0.5 | -4.1 | 1178 |
| 136 | Kent State | Mid-American | -22.7 | -10.8 | -7.4 | -0.7 | -3.8 | 1203 |
| 137 | Akron | Mid-American | -23.1 | -9.6 | -9.2 | -0.4 | -3.9 | 1199 |
| 138 | UTEP | Mountain West | -25.7 | -11.6 | -7.7 | -1.1 | -5.2 | 1088 |

## Current model fit

- Fitted on 4439 games from seasons 2022–2026.
- Home field on top of the ratings: 3.2 points (1.8 in conference games).
- Extra FBS edge over FCS opponents beyond their ratings: 14.0 points.
- Elo weight: 0.20 points of margin per point of Elo spread.
- Weight on the betting line: 90% for the margin, 82% for the total.
