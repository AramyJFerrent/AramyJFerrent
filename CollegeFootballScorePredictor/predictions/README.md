# College football score predictions

Updated Sat Nov 21, 2026 06:35 PM ET. Refreshed automatically every day of the season and several times on Saturdays; each game's prediction is locked at kickoff and graded once the final score is in. Scores are the most likely real scoreline near the expected points; ranges cover 80% of simulated outcomes for each team. College scores scatter widely, so read the ranges, not just the headline score.

Expected points blend the model with the betting line using the weight that has predicted best in recent seasons (see Current model fit). The spread and total columns show the model's own numbers next to the line, so you can see where it disagrees. Games without a line yet use the model alone.

The fair moneyline is the American odds that match the win chance exactly, with no bookmaker margin: -200 means risk $200 to win $100, +200 means risk $100 to win $200. A sportsbook's price will be a little worse on both sides because of its cut, so a book only offers value on a team when its price beats the fair line.

The edge columns judge each bet by its expected value per $1 staked at the posted price, using the final prediction: the model blended with the line, run through the score simulator, pushes included, and anchored to the market's own chances so that only what the blend moves off the line counts. The model's own spread and total (shown alongside) sit several points from the line in most games, but the blend keeps only the share of that disagreement the model has earned in past seasons, so edges are rare. The side with the higher value is shown when it reaches 3% (+3 cents per $1), as the team or side, the price, the expected value, its chance of winning the bet and its stake, a 25% share of the Kelly stake in units of 1% of the bankroll with at most 3 units on one game; anything short is no edge. Where a book posts no price for a spread or total it is assumed to be -110 and marked -110*; moneylines are never assumed. In the walk-forward backtest against closing lines, edges returned spread -100.0% on 1 bets (posted prices, 2016–2019); spread -3.9% on 156 bets (assumed -110 prices, 2016–2025); moneyline +13.7% on 575 bets (posted prices, 2016–2025); total +2.6% on 367 bets (posted prices, 2016–2019); total -5.7% on 172 bets (assumed -110 prices, 2016–2025). None of these is clearly above zero, so treat these edges as an experiment, not a betting system. The live record is tracked below, graded at the price logged with the last prediction before kickoff.

## 2026 Week 12

| Kickoff (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected points | 80% range | Spread: model / line | Total: model / line | Spread edge | Moneyline edge | Total edge | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sat 11/21 7:00 PM | Arizona @ Kansas State | Arizona 31, Kansas State 24 | Arizona 74% | Arizona -280 / Kansas State +280 | 31.6 – 22.4 | 17–46 / 10–35 | Arizona -1.7 / Arizona -10.0 | 55.2 / 53.8 | no edge | no edge | no edge |  |
| Sat 11/21 7:00 PM | Virginia Tech @ Miami | Virginia Tech 17, Miami 38 | Miami 92% | Virginia Tech +1115 / Miami -1115 | 19.9 – 41.4 | 7–34 / 27–58 | Miami -24.5 / Miami -21.2 | 59.4 / 61.8 | no edge | no edge | no edge |  |
| Sat 11/21 7:00 PM | UNLV @ San José State | UNLV 28, San José State 21 | UNLV 68% | UNLV -210 / San José State +210 | 27.6 – 21.1 | 14–42 / 8–34 | UNLV -9.5 / UNLV -6.2 | 50.4 / 48.2 | no edge | no edge | no edge |  |
| Sat 11/21 7:00 PM | Arkansas State @ Louisiana Tech | Arkansas State 20, Louisiana Tech 34 | Louisiana Tech 84% | Arkansas State +510 / Louisiana Tech -510 | 19.5 – 34.1 | 7–32 / 20–49 | Louisiana Tech -13.2 / Louisiana Tech -14.8 | 49.8 / 54.5 | no edge | no edge | no edge |  |
| Sat 11/21 7:30 PM | Kentucky @ Missouri | Kentucky 24, Missouri 27 | Missouri 63% | Kentucky +170 / Missouri -170 | 22.3 – 27.1 | 10–35 / 13–41 | Missouri -7.9 / Missouri -4.5 | 48.6 / 49.5 | no edge | no edge | no edge |  |
| Sat 11/21 7:30 PM | Georgia @ South Carolina | Georgia 31, South Carolina 17 | Georgia 84% | Georgia -540 / South Carolina +540 | 32.8 – 18.0 | 17–48 / 7–31 | Georgia -15.7 / Georgia -14.8 | 49.3 / 51.2 | no edge | no edge | no edge |  |
| Sat 11/21 7:30 PM | Pittsburgh @ Louisville | Pittsburgh 21, Louisville 31 | Louisville 79% | Pittsburgh +375 / Louisville -375 | 19.5 – 31.0 | 7–31 / 17–46 | Louisville -16.2 / Louisville -11.0 | 51.4 / 50.2 | no edge | no edge | no edge |  |
| Sat 11/21 7:30 PM | SMU @ Notre Dame | SMU 17, Notre Dame 38 | Notre Dame 92% | SMU +1090 / Notre Dame -1090 | 17.3 – 37.7 | 7–30 / 23–54 | Notre Dame -18.7 / Notre Dame -20.5 | 52.6 / 55.5 | no edge | no edge | no edge |  |
| Sat 11/21 7:30 PM | Stanford @ California | Stanford 27, California 24 | Stanford 56% | Stanford -125 / California +125 | 28.8 – 26.5 | 14–42 / 13–41 | California -0.1 / Stanford -2.5 | 54.7 / 55.5 | no edge | no edge | no edge |  |
| Sat 11/21 7:30 PM | Colorado State @ Fresno State | Colorado State 24, Fresno State 45 | Fresno State 89% | Colorado State +800 / Fresno State -800 | 23.3 – 42.8 | 10–37 / 27–59 | Fresno State -12.3 / Fresno State -20.2 | 60.9 / 67.2 | no edge | Colorado State (+874): EV +6.6%, 11%, stake 0.2u | no edge |  |
| Sat 11/21 8:00 PM | UTSA @ UAB | UTSA 27, UAB 24 | UTSA 61% | UTSA -160 / UAB +160 | 27.1 – 22.8 | 14–41 / 10–36 | UTSA -7.3 / UTSA -4.0 | 51.7 / 49.5 | no edge | no edge | no edge |  |
| Sat 11/21 9:00 PM | Utah @ TCU | Utah 24, TCU 17 | Utah 73% | Utah -275 / TCU +275 | 27.9 – 19.0 | 14–42 / 7–31 | Utah -13.3 / Utah -8.5 | 49.9 / 46.2 | no edge | no edge | no edge |  |
| Sat 11/21 9:30 PM | San Diego State @ Boise State | San Diego State 20, Boise State 41 | Boise State 91% | San Diego State +965 / Boise State -965 | 20.1 – 40.0 | 7–33 / 24–56 | Boise State -13.8 / Boise State -20.5 | 56.7 / 60.8 | no edge | no edge | no edge |  |
| Sat 11/21 10:15 PM | Oklahoma State @ Arizona State | Oklahoma State 31, Arizona State 28 | Oklahoma State 55% | Oklahoma State -120 / Arizona State +120 | 30.7 – 28.5 | 17–45 / 14–44 | Arizona State -1.3 / Oklahoma State -2.5 | 57.7 / 59.5 | no edge | no edge | no edge |  |
| Sat 11/21 10:30 PM | Utah State @ Oregon State | Utah State 24, Oregon State 31 | Oregon State 69% | Utah State +225 / Oregon State -225 | 22.1 – 29.5 | 10–35 / 16–44 | Oregon State -12.1 / Oregon State -7.0 | 53.3 / 51.2 | no edge | no edge | no edge |  |
| Sat 11/21 10:30 PM | Hawai'i @ Nevada | Hawai'i 17, Nevada 24 | Nevada 67% | Hawai'i +200 / Nevada -200 | 17.7 – 24.0 | 7–31 / 10–38 | Hawai'i -1.2 / Nevada -7.0 | 46.9 / 40.5 | no edge | no edge | Over 40.5 (-110*): EV +3.3%, 54%, stake 0.9u | * price not posted; assumed -110 |

## 2026 Week 13

| Kickoff (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected points | 80% range | Spread: model / line | Total: model / line | Spread edge | Moneyline edge | Total edge | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tue 11/24 7:00 PM | Kent State @ Eastern Michigan | Kent State 20, Eastern Michigan 27 | Eastern Michigan 67% | Kent State +205 / Eastern Michigan -205 | 20.3 – 26.8 | 7–34 / 13–41 | Eastern Michigan -6.6 / Eastern Michigan -6.5 | 49.5 / 46.5 | no edge | no edge | no edge |  |
| Tue 11/24 7:00 PM | Miami (OH) @ Western Michigan | Miami (OH) 20, Western Michigan 27 | Western Michigan 69% | Miami (OH) +220 / Western Michigan -220 | 19.9 – 26.9 | 7–33 / 13–41 | Western Michigan -1.9 / Western Michigan -7.5 | 48.0 / 46.5 | no edge | no edge | no edge |  |
| Thu 11/26 8:00 PM | TCU @ Texas Tech | TCU 17, Texas Tech 27 | Texas Tech 79% | TCU +365 / Texas Tech -365 | 18.0 – 29.0 | 7–31 / 14–44 | Texas Tech -16.8 / Texas Tech -10.5 | 44.9 / 47.5 | no edge | no edge | no edge |  |
| Fri 11/27 12:00 PM | Mississippi State @ Ole Miss | Mississippi State 17, Ole Miss 38 | Ole Miss 90% | Mississippi State +895 / Ole Miss -895 | 19.3 – 38.4 | 7–31 / 24–54 | Ole Miss -14.9 / Ole Miss -19.5 | 59.0 / 57.5 | no edge | no edge | no edge |  |
| Fri 11/27 12:00 PM | Nebraska @ Iowa | Nebraska 17, Iowa 24 | Iowa 68% | Nebraska +210 / Iowa -210 | 16.7 – 23.0 | 6–28 / 10–37 | Iowa -3.9 / Iowa -6.5 | 44.9 / 38.5 | no edge | no edge | no edge |  |
| Fri 11/27 12:00 PM | Tulsa @ UTSA | Tulsa 28, UTSA 31 | UTSA 61% | Tulsa +155 / UTSA -155 | 26.5 – 30.6 | 13–41 / 17–45 | UTSA -4.1 / – | 57.0 / – | no line yet | no line yet (fair: UTSA -155) | no line yet |  |
| Fri 11/27 12:00 PM | Buffalo @ Akron | Buffalo 31, Akron 21 | Buffalo 75% | Buffalo -300 / Akron +300 | 29.8 – 20.0 | 16–45 / 7–33 | Buffalo -8.1 / Buffalo -10.0 | 52.0 / 49.5 | no edge | no edge | no edge |  |
| Fri 11/27 12:00 PM | Toledo @ Ohio | Toledo 24, Ohio 21 | Toledo 61% | Toledo -155 / Ohio +155 | 25.9 – 21.9 | 13–40 / 10–35 | Toledo -4.0 / – | 48.3 / – | no line yet | no line yet (fair: Toledo -155) | no line yet |  |
| Fri 11/27 3:00 PM | App State @ South Alabama | App State 28, South Alabama 31 | South Alabama 52% | App State +105 / South Alabama -105 | 29.3 – 29.9 | 15–44 / 16–45 | South Alabama -0.6 / – | 59.2 / – | no line yet | no line yet (fair: South Alabama -105) | no line yet |  |
| Fri 11/27 3:30 PM | Florida @ Florida State | Florida 27, Florida State 24 | Florida 61% | Florida -155 / Florida State +155 | 28.7 – 24.4 | 14–43 / 10–38 | Florida -2.7 / Florida -4.5 | 56.0 / 52.5 | no edge | no edge | no edge |  |
| Fri 11/27 3:30 PM | Temple @ Memphis | Temple 24, Memphis 41 | Memphis 88% | Temple +745 / Memphis -745 | 21.7 – 39.5 | 9–35 / 24–55 | Memphis -17.7 / – | 61.2 / – | no line yet | no line yet (fair: Memphis -745) | no line yet |  |
| Fri 11/27 3:30 PM | North Dakota State @ San José State | North Dakota State 27, San José State 14 | North Dakota State 84% | North Dakota State -535 / San José State +535 | 28.0 – 14.1 | 14–42 / 3–26 | North Dakota State -14.0 / – | 42.1 / – | no line yet | no line yet (fair: North Dakota State -535) | no line yet |  |
| Fri 11/27 4:30 PM | Air Force @ New Mexico | Air Force 24, New Mexico 27 | New Mexico 62% | Air Force +165 / New Mexico -165 | 21.9 – 26.7 | 10–35 / 13–41 | New Mexico -4.7 / – | 48.6 / – | no line yet | no line yet (fair: New Mexico -165) | no line yet |  |
| Fri 11/27 7:30 PM | Texas @ Texas A&M | Texas 24, Texas A&M 17 | Texas 70% | Texas -240 / Texas A&M +240 | 24.5 – 16.9 | 10–38 / 6–29 | Texas -8.9 / Texas -7.5 | 40.5 / 41.5 | no edge | no edge | no edge |  |
| Fri 11/27 7:30 PM | Minnesota @ Wisconsin | Minnesota 17, Wisconsin 24 | Wisconsin 73% | Minnesota +275 / Wisconsin -275 | 15.2 – 23.7 | 6–27 / 10–38 | Wisconsin -8.5 / – | 38.9 / – | no line yet | no line yet (fair: Wisconsin -275) | no line yet |  |
| Fri 11/27 9:00 PM | West Virginia @ Utah | West Virginia 17, Utah 45 | Utah 95% | West Virginia +1765 / Utah -1765 | 19.7 – 44.4 | 7–32 / 30–61 | Utah -24.7 / – | 64.2 / – | no line yet | no line yet (fair: Utah -1765) | no line yet |  |
| Sat 11/28 TBA | Auburn @ Alabama | Auburn 17, Alabama 31 | Alabama 85% | Auburn +550 / Alabama -550 | 17.8 – 32.8 | 7–31 / 17–48 | Alabama -10.6 / Alabama -15.5 | 50.9 / 50.5 | no edge | no edge | no edge |  |
| Sat 11/28 TBA | LSU @ Arkansas | LSU 34, Arkansas 17 | LSU 90% | LSU -910 / Arkansas +910 | 35.0 – 16.8 | 20–51 / 6–28 | LSU -18.2 / – | 51.8 / – | no line yet | no line yet (fair: LSU -910) | no line yet |  |
| Sat 11/28 TBA | Georgia Tech @ Georgia | Georgia Tech 6, Georgia 45 | Georgia 100% | Georgia Tech +9900 / Georgia -9900 | 6.4 – 43.6 | 0–13 / 29–59 | Georgia -37.2 / – | 50.4 / – | no line yet | no line yet (fair: Georgia -9900) | no line yet |  |
| Sat 11/28 TBA | Louisville @ Kentucky | Louisville 24, Kentucky 27 | Kentucky 52% | Louisville +110 / Kentucky -110 | 26.6 – 27.5 | 14–41 / 14–42 | Louisville -5.6 / Kentucky -1.5 | 52.6 / 54.5 | no edge | no edge | no edge |  |
| Sat 11/28 TBA | South Carolina @ Clemson | South Carolina 24, Clemson 27 | Clemson 57% | South Carolina +130 / Clemson -130 | 24.8 – 27.5 | 12–38 / 14–42 | South Carolina -0.4 / Clemson -3.0 | 46.9 / 53.5 | no edge | no edge | no edge |  |
| Sat 11/28 TBA | Tennessee @ Vanderbilt | Tennessee 31, Vanderbilt 28 | Tennessee 60% | Tennessee -150 / Vanderbilt +150 | 29.8 – 25.9 | 16–45 / 13–40 | Tennessee -13.2 / Tennessee -3.0 | 47.4 / 57.5 | no edge | no edge | Under 57.5 (-110*): EV +3.1%, 54%, stake 0.9u | * price not posted; assumed -110 |
| Sat 11/28 TBA | Duke @ Wake Forest | Duke 21, Wake Forest 31 | Wake Forest 77% | Duke +335 / Wake Forest -335 | 20.7 – 31.8 | 7–34 / 17–47 | Wake Forest -17.3 / Wake Forest -10.5 | 52.6 / 52.5 | no edge | no edge | no edge |  |
| Sat 11/28 TBA | SMU @ Stanford | SMU 35, Stanford 21 | SMU 81% | SMU -430 / Stanford +430 | 35.3 – 21.3 | 20–51 / 9–35 | SMU -13.9 / – | 56.6 / – | no line yet | no line yet (fair: SMU -430) | no line yet |  |
| Sat 11/28 TBA | Purdue @ Indiana | Purdue 10, Indiana 38 | Indiana 97% | Purdue +3025 / Indiana -3025 | 11.8 – 37.7 | 3–22 / 23–54 | Indiana -25.9 / – | 49.4 / – | no line yet | no line yet (fair: Indiana -3025) | no line yet |  |
| Sat 11/28 TBA | Washington @ Oregon | Washington 17, Oregon 31 | Oregon 82% | Washington +445 / Oregon -445 | 17.9 – 30.6 | 7–31 / 17–45 | Oregon -14.4 / Oregon -12.5 | 48.5 / 48.5 | no edge | no edge | no edge |  |
| Sat 11/28 12:00 PM | Boston College @ Miami | Boston College 10, Miami 45 | Miami 99% | Boston College +9900 / Miami -9900 | 11.5 – 44.2 | 3–21 / 30–61 | Miami -32.7 / – | 55.7 / – | no line yet | no line yet (fair: Miami -9900) | no line yet |  |
| Sat 11/28 12:00 PM | NC State @ North Carolina | NC State 31, North Carolina 28 | NC State 52% | NC State -110 / North Carolina +110 | 28.5 – 27.5 | 14–43 / 14–42 | North Carolina -4.5 / NC State -1.5 | 58.5 / 55.5 | no edge | no edge | no edge |  |
| Sat 11/28 12:00 PM | Notre Dame @ Syracuse | Notre Dame 38, Syracuse 17 | Notre Dame 92% | Notre Dame -1175 / Syracuse +1175 | 37.3 – 16.7 | 22–52 / 6–28 | Notre Dame -20.9 / Notre Dame -20.5 | 51.7 / 54.5 | no edge | no edge | no edge |  |
| Sat 11/28 12:00 PM | Michigan @ Ohio State | Michigan 17, Ohio State 27 | Ohio State 81% | Michigan +440 / Ohio State -440 | 14.9 – 27.5 | 3–27 / 14–42 | Ohio State -14.2 / Ohio State -12.5 | 46.3 / 41.5 | no edge | no edge | no edge |  |
| Sat 11/28 12:00 PM | UConn @ Wyoming | UConn 27, Wyoming 24 | UConn 62% | UConn -165 / Wyoming +165 | 30.0 – 25.0 | 16–44 / 12–39 | UConn -5.1 / – | 55.0 / – | no line yet | no line yet (fair: UConn -165) | no line yet |  |
| Sat 11/28 12:00 PM | Navy @ Charlotte | Navy 34, Charlotte 17 | Navy 88% | Navy -740 / Charlotte +740 | 34.9 – 17.4 | 20–51 / 6–30 | Navy -17.5 / – | 52.3 / – | no line yet | no line yet (fair: Navy -740) | no line yet |  |
| Sat 11/28 12:00 PM | Central Michigan @ Ball State | Central Michigan 27, Ball State 24 | Central Michigan 61% | Central Michigan -160 / Ball State +160 | 27.2 – 23.1 | 14–41 / 10–37 | Central Michigan -4.1 / – | 51.0 / – | no line yet | no line yet (fair: Central Michigan -160) | no line yet |  |
| Sat 11/28 12:00 PM | Louisiana Tech @ Georgia Southern | Louisiana Tech 27, Georgia Southern 24 | Louisiana Tech 53% | Louisiana Tech -110 / Georgia Southern +110 | 25.0 – 23.9 | 13–39 / 10–38 | Louisiana Tech -1.0 / – | 50.8 / – | no line yet | no line yet (fair: Louisiana Tech -110) | no line yet |  |
| Sat 11/28 12:30 PM | Illinois @ Northwestern | Illinois 27, Northwestern 24 | Illinois 57% | Illinois -135 / Northwestern +135 | 28.0 – 25.3 | 14–42 / 13–38 | Northwestern -5.6 / Illinois -3.5 | 56.7 / 52.5 | no edge | no edge | no edge |  |
| Sat 11/28 1:00 PM | Florida Atlantic @ East Carolina | Florida Atlantic 28, East Carolina 31 | East Carolina 59% | Florida Atlantic +145 / East Carolina -145 | 26.6 – 30.3 | 13–41 / 16–45 | East Carolina -3.7 / – | 57.9 / – | no line yet | no line yet (fair: East Carolina -145) | no line yet |  |
| Sat 11/28 1:00 PM | Kennesaw State @ Western Kentucky | Kennesaw State 24, Western Kentucky 27 | Western Kentucky 53% | Kennesaw State +115 / Western Kentucky -115 | 25.5 – 26.8 | 13–40 / 14–41 | Western Kentucky -1.3 / – | 53.2 / – | no line yet | no line yet (fair: Western Kentucky -115) | no line yet |  |
| Sat 11/28 1:00 PM | Marshall @ UL Monroe | Marshall 31, UL Monroe 24 | Marshall 66% | Marshall -195 / UL Monroe +195 | 30.3 – 23.7 | 16–45 / 10–38 | Marshall -6.6 / – | 54.6 / – | no line yet | no line yet (fair: Marshall -195) | no line yet |  |
| Sat 11/28 1:00 PM | Southern Miss @ Old Dominion | Southern Miss 17, Old Dominion 24 | Old Dominion 70% | Southern Miss +230 / Old Dominion -230 | 19.0 – 26.4 | 7–31 / 13–41 | Old Dominion -7.4 / – | 45.4 / – | no line yet | no line yet (fair: Old Dominion -230) | no line yet |  |
| Sat 11/28 2:00 PM | UCF @ Colorado | UCF 24, Colorado 27 | Colorado 55% | UCF +120 / Colorado -120 | 25.0 – 26.6 | 12–38 / 13–41 | Colorado -1.7 / – | 51.6 / – | no line yet | no line yet (fair: Colorado -120) | no line yet |  |
| Sat 11/28 2:00 PM | Kansas State @ Iowa State | Kansas State 24, Iowa State 27 | Iowa State 55% | Kansas State +125 / Iowa State -125 | 25.6 – 27.6 | 13–39 / 14–42 | Iowa State -2.1 / – | 54.0 / – | no line yet | no line yet (fair: Iowa State -125) | no line yet |  |
| Sat 11/28 2:00 PM | Army @ Rice | Army 31, Rice 24 | Army 65% | Army -180 / Rice +180 | 31.4 – 25.6 | 17–47 / 13–41 | Army -5.8 / – | 56.9 / – | no line yet | no line yet (fair: Army -180) | no line yet |  |
| Sat 11/28 2:00 PM | Coastal Carolina @ James Madison | Coastal Carolina 17, James Madison 34 | James Madison 86% | Coastal Carolina +590 / James Madison -590 | 17.9 – 33.6 | 7–31 / 19–49 | James Madison -15.7 / – | 51.5 / – | no line yet | no line yet (fair: James Madison -590) | no line yet |  |
| Sat 11/28 2:00 PM | Louisiana @ Georgia State | Louisiana 27, Georgia State 24 | Louisiana 51% | Louisiana -105 / Georgia State +105 | 27.8 – 27.2 | 14–42 / 14–42 | Louisiana -0.6 / – | 55.5 / – | no line yet | no line yet (fair: Louisiana -105) | no line yet |  |
| Sat 11/28 2:00 PM | Liberty @ Missouri State | Liberty 34, Missouri State 17 | Liberty 86% | Liberty -610 / Missouri State +610 | 33.6 – 17.6 | 19–49 / 7–30 | Liberty -16.0 / – | 53.0 / – | no line yet | no line yet (fair: Liberty -610) | no line yet |  |
| Sat 11/28 2:00 PM | Sam Houston @ Florida International | Sam Houston 17, Florida International 24 | Florida International 74% | Sam Houston +280 / Florida International -280 | 15.3 – 23.7 | 6–27 / 10–38 | Florida International -8.4 / – | 39.0 / – | no line yet | no line yet (fair: Florida International -280) | no line yet |  |
| Sat 11/28 2:00 PM | New Mexico State @ Middle Tennessee | New Mexico State 24, Middle Tennessee 27 | Middle Tennessee 62% | New Mexico State +165 / Middle Tennessee -165 | 22.6 – 26.8 | 10–35 / 14–41 | Middle Tennessee -4.2 / – | 49.7 / – | no line yet | no line yet (fair: Middle Tennessee -165) | no line yet |  |
| Sat 11/28 3:00 PM | Virginia @ Virginia Tech | Virginia 24, Virginia Tech 27 | Virginia Tech 52% | Virginia +110 / Virginia Tech -110 | 25.9 – 27.3 | 13–40 / 14–42 | Virginia -0.4 / Virginia Tech -1.5 | 51.8 / 53.5 | no edge | no edge | no edge |  |
| Sat 11/28 3:00 PM | Troy @ Arkansas State | Troy 24, Arkansas State 27 | Arkansas State 60% | Troy +150 / Arkansas State -150 | 22.0 – 26.0 | 10–35 / 13–40 | Arkansas State -4.0 / – | 48.3 / – | no line yet | no line yet (fair: Arkansas State -150) | no line yet |  |
| Sat 11/28 3:30 PM | Cincinnati @ BYU | Cincinnati 24, BYU 34 | BYU 77% | Cincinnati +335 / BYU -335 | 23.2 – 34.5 | 10–37 / 20–49 | BYU -11.3 / – | 57.7 / – | no line yet | no line yet (fair: BYU -335) | no line yet |  |
| Sat 11/28 3:30 PM | Penn State @ Maryland | Penn State 24, Maryland 17 | Penn State 68% | Penn State -210 / Maryland +210 | 26.6 – 19.8 | 13–41 / 7–33 | Penn State -6.8 / – | 46.4 / – | no line yet | no line yet (fair: Penn State -210) | no line yet |  |
| Sat 11/28 3:30 PM | USC @ UCLA | USC 24, UCLA 27 | UCLA 58% | USC +140 / UCLA -140 | 24.8 – 27.7 | 10–38 / 14–42 | UCLA -7.3 / UCLA -2.5 | 52.7 / 52.5 | no edge | no edge | no edge |  |
| Sat 11/28 3:30 PM | Tulane @ South Florida | Tulane 24, South Florida 27 | South Florida 67% | Tulane +200 / South Florida -200 | 22.4 – 28.6 | 10–35 / 14–43 | South Florida -6.2 / – | 51.3 / – | no line yet | no line yet (fair: South Florida -200) | no line yet |  |
| Sat 11/28 3:30 PM | UTEP @ Northern Illinois | UTEP 21, Northern Illinois 28 | Northern Illinois 71% | UTEP +245 / Northern Illinois -245 | 20.8 – 29.0 | 7–34 / 14–44 | Northern Illinois -8.2 / – | 49.7 / – | no line yet | no line yet (fair: Northern Illinois -245) | no line yet |  |
| Sat 11/28 3:30 PM | Massachusetts @ Bowling Green | Massachusetts 17, Bowling Green 20 | Bowling Green 61% | Massachusetts +160 / Bowling Green -160 | 17.9 – 21.8 | 7–31 / 10–35 | Bowling Green -3.9 / – | 39.8 / – | no line yet | no line yet (fair: Bowling Green -160) | no line yet |  |
| Sat 11/28 3:30 PM | Jacksonville State @ Delaware | Jacksonville State 28, Delaware 31 | Delaware 54% | Jacksonville State +120 / Delaware -120 | 27.4 – 29.2 | 14–41 / 14–44 | Delaware -1.8 / – | 57.0 / – | no line yet | no line yet (fair: Delaware -120) | no line yet |  |
| Sat 11/28 4:00 PM | UAB @ North Texas | UAB 24, North Texas 34 | North Texas 74% | UAB +285 / North Texas -285 | 24.1 – 34.1 | 10–38 / 20–49 | North Texas -10.0 / – | 58.2 / – | no line yet | no line yet (fair: North Texas -285) | no line yet |  |
| Sat 11/28 4:15 PM | Oklahoma @ Missouri | Oklahoma 21, Missouri 24 | Missouri 54% | Oklahoma +115 / Missouri -115 | 20.6 – 21.8 | 7–34 / 10–35 | Oklahoma -1.8 / Missouri -1.5 | 42.4 / 42.5 | no edge | no edge | no edge |  |
| Sat 11/28 4:15 PM | Michigan State @ Rutgers | Michigan State 27, Rutgers 24 | Michigan State 52% | Michigan State -110 / Rutgers +110 | 26.0 – 25.2 | 13–40 / 13–38 | Michigan State -0.8 / – | 51.1 / – | no line yet | no line yet (fair: Michigan State -110) | no line yet |  |
| Sat 11/28 6:15 PM | Kansas @ Oklahoma State | Kansas 28, Oklahoma State 31 | Oklahoma State 56% | Kansas +130 / Oklahoma State -130 | 28.6 – 30.8 | 14–43 / 17–45 | Oklahoma State -2.1 / – | 59.4 / – | no line yet | no line yet (fair: Oklahoma State -130) | no line yet |  |
| Sat 11/28 7:30 PM | Pittsburgh @ California | Pittsburgh 28, California 21 | Pittsburgh 72% | Pittsburgh -260 / California +260 | 29.5 – 20.6 | 14–44 / 7–34 | Pittsburgh -8.9 / – | 50.0 / – | no line yet | no line yet (fair: Pittsburgh -260) | no line yet |  |
| Sat 11/28 9:00 PM | Arizona State @ Arizona | Arizona State 24, Arizona 27 | Arizona 62% | Arizona State +160 / Arizona -160 | 24.1 – 28.7 | 10–38 / 14–43 | Arizona -5.9 / Arizona -4.5 | 53.9 / 52.5 | no edge | no edge | no edge |  |
| Sat 11/28 9:00 PM | Nevada @ UNLV | Nevada 17, UNLV 31 | UNLV 78% | Nevada +350 / UNLV -350 | 17.9 – 29.2 | 7–31 / 14–44 | UNLV -11.3 / – | 47.0 / – | no line yet | no line yet (fair: UNLV -350) | no line yet |  |
| Sat 11/28 9:30 PM | Baylor @ Houston | Baylor 28, Houston 31 | Houston 52% | Baylor +110 / Houston -110 | 28.7 – 29.4 | 14–43 / 15–44 | Houston -0.7 / – | 58.1 / – | no line yet | no line yet (fair: Houston -110) | no line yet |  |
| Sat 11/28 11:00 PM | Sacramento State @ Hawai'i | Sacramento State 17, Hawai'i 31 | Hawai'i 83% | Sacramento State +500 / Hawai'i -500 | 17.3 – 31.5 | 6–30 / 17–47 | Hawai'i -14.2 / – | 48.7 / – | no line yet | no line yet (fair: Hawai'i -500) | no line yet |  |

## How the 2026 predictions have done

| Predictor | Games | Margin MAE | Total MAE | Team-score MAE | Winners | Brier | 80% range hit |
|---|---|---|---|---|---|---|---|
| Final prediction | 781 | 11.85 | 12.29 | 8.53 | 77.7% | 0.150 | 81.6% |
| Model only (before blending) | 781 | 12.52 | 12.65 | 8.79 | 75.7% | – | – |
| Betting line when predicted | 779 | 11.84 | 12.24 | 8.53 | 77.8% | – | – |

MAE is mean absolute error in points (lower is better). Brier scores the win chances (lower is better, 0.25 is a coin flip). Even the closing betting line misses the final margin of an FBS game by about 12.5 points.

501 of these games were played before the predictor went live. They are backfilled walk-forward (each week predicted from earlier weeks only) but with closing lines, so they flatter the model slightly. Every game since is graded on the prediction logged before kickoff.

### Betting edges

| Market | Edges | Record (W-L-P) | Staked | Units won | ROI | Expected ROI |
|---|---|---|---|---|---|---|
| Spread | 0 | 0-0-0 | 0.0 | +0.00 | – | – |
| Moneyline | 11 | 2-9-0 | 3.5 | +0.18 | +5.2% | +4.7% |
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

## FBS power ratings

Points per game better than an average FBS team on a neutral field, from opponent-adjusted EPA (garbage time removed) with this season's games weighted against a preseason prior, plus the weight the margin model puts on Elo (a rating built from game results alone). Defense is positive when it holds opponents below average.

| # | Team | Conference | Net | Offense | Defense | Special teams | Results (Elo) | Elo rating |
|---|---|---|---|---|---|---|---|---|
| 1 | Georgia | SEC | +27.7 | +9.2 | +12.3 | +0.9 | +5.3 | 1944 |
| 2 | Notre Dame | FBS Independents | +24.6 | +8.9 | +9.9 | +1.0 | +4.7 | 1892 |
| 3 | LSU | SEC | +23.6 | +9.6 | +11.9 | -0.2 | +2.3 | 1696 |
| 4 | Miami | ACC | +23.2 | +14.8 | +3.5 | +0.3 | +4.6 | 1881 |
| 5 | Ohio State | Big Ten | +22.9 | +11.2 | +8.1 | +0.3 | +3.4 | 1784 |
| 6 | Alabama | SEC | +21.9 | +8.2 | +9.4 | +0.3 | +4.1 | 1842 |
| 7 | Wake Forest | ACC | +21.8 | +8.8 | +9.0 | +0.6 | +3.4 | 1790 |
| 8 | Indiana | Big Ten | +21.5 | +5.3 | +10.4 | +0.3 | +5.4 | 1953 |
| 9 | Utah | Big 12 | +21.5 | +11.2 | +5.7 | +0.1 | +4.4 | 1869 |
| 10 | Oregon | Big Ten | +21.3 | +6.6 | +9.9 | +0.8 | +4.0 | 1835 |
| 11 | Texas | SEC | +20.3 | +2.3 | +12.8 | +1.0 | +4.3 | 1856 |
| 12 | Tennessee | SEC | +18.9 | +4.1 | +10.1 | +1.3 | +3.4 | 1784 |
| 13 | Texas Tech | Big 12 | +18.7 | +2.6 | +11.1 | +1.6 | +3.5 | 1793 |
| 14 | UCLA | Big Ten | +17.8 | +4.7 | +9.6 | +0.7 | +2.7 | 1729 |
| 15 | Ole Miss | SEC | +17.4 | +10.9 | +3.3 | +0.6 | +2.7 | 1729 |
| 16 | Oklahoma | SEC | +16.7 | +1.3 | +12.5 | +0.6 | +2.3 | 1696 |
| 17 | Louisville | ACC | +16.6 | +9.0 | +4.5 | +0.6 | +2.5 | 1711 |
| 18 | Iowa | Big Ten | +14.9 | +1.5 | +9.0 | +0.9 | +3.4 | 1789 |
| 19 | Nebraska | Big Ten | +13.9 | +5.2 | +6.9 | +0.4 | +1.4 | 1622 |
| 20 | Auburn | SEC | +13.6 | +5.1 | +6.8 | +0.5 | +1.1 | 1601 |
| 21 | USC | Big Ten | +13.5 | +10.4 | +0.4 | +0.1 | +2.6 | 1724 |
| 22 | Penn State | Big Ten | +12.9 | +4.0 | +6.8 | +0.2 | +1.9 | 1666 |
| 23 | Missouri | SEC | +12.9 | +3.7 | +7.0 | +0.3 | +1.9 | 1667 |
| 24 | BYU | Big 12 | +12.8 | +4.1 | +4.7 | +0.8 | +3.2 | 1771 |
| 25 | Florida | SEC | +12.0 | +6.4 | +4.1 | +0.4 | +1.2 | 1603 |
| 26 | Michigan | Big Ten | +11.5 | +1.8 | +8.7 | -0.0 | +1.0 | 1586 |
| 27 | Arizona | Big 12 | +10.9 | +6.2 | +2.4 | -0.1 | +2.4 | 1706 |
| 28 | Baylor | Big 12 | +10.6 | +1.4 | +7.2 | +0.8 | +1.2 | 1604 |
| 29 | SMU | ACC | +10.5 | +6.6 | +2.1 | +0.2 | +1.6 | 1637 |
| 30 | South Carolina | SEC | +10.1 | +4.4 | +4.1 | +0.3 | +1.1 | 1602 |
| 31 | Washington | Big Ten | +9.9 | +3.0 | +4.9 | +0.2 | +1.9 | 1660 |
| 32 | Texas A&M | SEC | +9.8 | +0.9 | +8.1 | +0.3 | +0.6 | 1554 |
| 33 | Houston | Big 12 | +9.4 | +8.6 | -1.0 | +0.3 | +1.5 | 1633 |
| 34 | Northwestern | Big Ten | +9.2 | +6.2 | +1.7 | +0.6 | +0.7 | 1567 |
| 35 | Wisconsin | Big Ten | +8.7 | -0.1 | +7.1 | +0.6 | +1.2 | 1605 |
| 36 | Kansas | Big 12 | +8.6 | +4.8 | +4.1 | +0.0 | -0.3 | 1488 |
| 37 | Oklahoma State | Big 12 | +8.3 | +8.0 | -0.2 | +0.2 | +0.3 | 1530 |
| 38 | Kentucky | SEC | +7.5 | +2.4 | +3.8 | +0.2 | +1.0 | 1594 |
| 39 | Arizona State | Big 12 | +7.2 | +1.7 | +4.2 | +0.1 | +1.1 | 1599 |
| 40 | Duke | ACC | +6.8 | +3.4 | +1.1 | +0.7 | +1.6 | 1639 |
| 41 | Kansas State | Big 12 | +6.5 | +4.6 | +2.4 | +0.3 | -0.9 | 1436 |
| 42 | Boise State | Pac-12 | +6.4 | +7.3 | -3.5 | -0.1 | +2.8 | 1735 |
| 43 | Florida State | ACC | +6.3 | +6.5 | -0.1 | -0.5 | +0.4 | 1540 |
| 44 | Illinois | Big Ten | +6.3 | +5.9 | -1.4 | +0.4 | +1.3 | 1617 |
| 45 | TCU | Big 12 | +5.8 | -1.8 | +6.4 | +0.1 | +1.1 | 1599 |
| 46 | Iowa State | Big 12 | +5.5 | +4.4 | +0.1 | +0.9 | +0.0 | 1512 |
| 47 | Mississippi State | SEC | +5.4 | +2.6 | +3.5 | +0.0 | -0.7 | 1449 |
| 48 | Clemson | ACC | +5.0 | -6.2 | +8.9 | +1.1 | +1.2 | 1608 |
| 49 | UCF | Big 12 | +4.9 | +2.9 | +2.1 | -0.1 | -0.0 | 1505 |
| 50 | Colorado | Big 12 | +4.6 | +2.2 | +4.0 | -0.5 | -1.2 | 1413 |
| 51 | Cincinnati | Big 12 | +4.4 | +8.9 | -4.9 | +0.2 | +0.2 | 1526 |
| 52 | Virginia | ACC | +4.0 | -0.2 | +3.5 | +0.1 | +0.6 | 1559 |
| 53 | Vanderbilt | SEC | +4.0 | +2.3 | +1.0 | +0.7 | +0.0 | 1510 |
| 54 | Maryland | Big Ten | +3.4 | -0.0 | +4.2 | +0.5 | -1.2 | 1408 |
| 55 | Arkansas | SEC | +3.3 | +1.5 | +1.9 | -0.4 | +0.3 | 1536 |
| 56 | Pittsburgh | ACC | +3.0 | -2.6 | +4.9 | +0.5 | +0.2 | 1525 |
| 57 | North Carolina | ACC | +2.6 | +3.7 | -1.1 | +0.1 | -0.1 | 1503 |
| 58 | Memphis | American Athletic | +2.5 | +4.8 | -3.0 | -0.6 | +1.3 | 1618 |
| 59 | Minnesota | Big Ten | +2.4 | -3.0 | +4.4 | +0.8 | +0.2 | 1526 |
| 60 | UTSA | American Athletic | +1.9 | +2.3 | -2.0 | -0.1 | +1.6 | 1642 |
| 61 | Texas State | Pac-12 | +1.8 | +7.2 | -5.5 | -1.2 | +1.3 | 1613 |
| 62 | Syracuse | ACC | +1.7 | +1.5 | +2.3 | -0.8 | -1.4 | 1392 |
| 63 | Virginia Tech | ACC | +1.5 | +2.7 | -0.6 | -0.2 | -0.4 | 1475 |
| 64 | Liberty | Conference USA | +1.5 | +1.5 | -1.3 | +0.2 | +1.0 | 1591 |
| 65 | James Madison | Sun Belt | +1.1 | -0.6 | +0.1 | +0.2 | +1.4 | 1625 |
| 66 | NC State | ACC | +0.9 | +5.0 | -3.2 | -0.4 | -0.5 | 1467 |
| 67 | Tulsa | American Athletic | +0.8 | -0.4 | +1.8 | -0.6 | -0.0 | 1508 |
| 68 | North Texas | American Athletic | +0.6 | +7.6 | -7.0 | -0.8 | +0.8 | 1573 |
| 69 | Toledo | Mid-American | +0.1 | -3.7 | +3.2 | -0.3 | +0.8 | 1577 |
| 70 | Oregon State | Pac-12 | -0.2 | +4.8 | -3.8 | -0.1 | -1.0 | 1423 |
| 71 | Louisiana Tech | Sun Belt | -0.5 | -2.5 | +1.8 | -0.8 | +1.0 | 1588 |
| 72 | Navy | American Athletic | -0.6 | +3.5 | -3.8 | -0.4 | +0.1 | 1518 |
| 73 | New Mexico | Mountain West | -0.6 | -4.0 | +2.2 | -0.3 | +1.4 | 1620 |
| 74 | North Dakota State | Mountain West | -0.8 | -5.6 | +4.6 | +0.9 | -0.7 | 1453 |
| 75 | West Virginia | Big 12 | -1.0 | +4.9 | -5.1 | +0.3 | -1.1 | 1417 |
| 76 | UConn | FBS Independents | -1.1 | +2.8 | -3.9 | +0.0 | +0.0 | 1512 |
| 77 | East Carolina | American Athletic | -2.0 | -6.5 | +4.7 | -0.8 | +0.5 | 1552 |
| 78 | South Florida | American Athletic | -2.4 | -1.2 | -1.7 | +0.1 | +0.3 | 1531 |
| 79 | Purdue | Big Ten | -2.6 | +2.8 | -4.4 | +0.9 | -1.9 | 1351 |
| 80 | Michigan State | Big Ten | -2.8 | -3.0 | +1.2 | -0.0 | -1.0 | 1428 |
| 81 | Air Force | Mountain West | -3.2 | +2.4 | -6.0 | +0.0 | +0.4 | 1538 |
| 82 | Fresno State | Pac-12 | -3.6 | -1.9 | -1.7 | -0.2 | +0.1 | 1520 |
| 83 | Georgia Southern | Sun Belt | -4.1 | -1.1 | -3.5 | -0.5 | +1.0 | 1586 |
| 84 | Georgia Tech | ACC | -4.5 | +0.8 | -4.1 | -0.3 | -0.8 | 1440 |
| 85 | UNLV | Mountain West | -4.7 | -2.1 | -3.1 | +0.2 | +0.3 | 1536 |
| 86 | Florida Atlantic | American Athletic | -4.7 | +2.7 | -7.5 | +0.7 | -0.5 | 1464 |
| 87 | Army | American Athletic | -5.3 | +3.4 | -8.5 | -0.0 | -0.1 | 1497 |
| 88 | San Diego State | Pac-12 | -5.3 | -3.9 | -0.9 | +0.3 | -0.7 | 1449 |
| 89 | Miami (OH) | Mid-American | -5.7 | -4.1 | -2.3 | +0.7 | -0.1 | 1500 |
| 90 | Stanford | ACC | -5.8 | -2.2 | -3.9 | +0.2 | +0.1 | 1513 |
| 91 | Western Michigan | Mid-American | -6.1 | -3.7 | -3.8 | +0.5 | +0.9 | 1580 |
| 92 | Washington State | Pac-12 | -6.3 | -4.5 | +0.1 | -0.3 | -1.5 | 1389 |
| 93 | Boston College | ACC | -6.3 | -3.8 | -1.4 | -0.6 | -0.6 | 1459 |
| 94 | Tulane | American Athletic | -6.3 | -4.0 | -2.4 | +0.2 | -0.1 | 1496 |
| 95 | Jacksonville State | Conference USA | -6.5 | -1.5 | -4.5 | +0.2 | -0.7 | 1451 |
| 96 | Ohio | Mid-American | -6.5 | -3.5 | -3.2 | -0.1 | +0.3 | 1532 |
| 97 | Rutgers | Big Ten | -6.7 | +1.4 | -6.6 | +0.6 | -2.0 | 1342 |
| 98 | Delaware | Conference USA | -6.9 | +0.6 | -6.4 | +0.1 | -1.2 | 1414 |
| 99 | California | ACC | -7.2 | -2.7 | -1.9 | -0.7 | -2.0 | 1344 |
| 100 | UAB | American Athletic | -7.7 | -6.4 | -0.5 | -0.1 | -0.7 | 1455 |
| 101 | Louisiana | Sun Belt | -8.5 | -3.5 | -5.0 | -0.0 | -0.0 | 1505 |
| 102 | Utah State | Pac-12 | -8.8 | -8.7 | +2.2 | -1.1 | -1.2 | 1412 |
| 103 | App State | Sun Belt | -9.0 | -3.5 | -3.5 | -0.7 | -1.4 | 1397 |
| 104 | Wyoming | Mountain West | -9.8 | -5.1 | -3.7 | -0.2 | -0.8 | 1447 |
| 105 | Marshall | Sun Belt | -10.7 | -5.6 | -4.2 | +0.1 | -1.1 | 1420 |
| 106 | Hawai'i | Mountain West | -11.0 | -4.8 | -5.3 | +1.2 | -2.1 | 1341 |
| 107 | Kennesaw State | Conference USA | -11.1 | -6.1 | -3.0 | -0.5 | -1.5 | 1386 |
| 108 | Georgia State | Sun Belt | -11.2 | -1.5 | -7.8 | -0.3 | -1.6 | 1377 |
| 109 | South Alabama | Sun Belt | -11.7 | +0.0 | -10.8 | +0.2 | -1.1 | 1419 |
| 110 | Old Dominion | Sun Belt | -12.0 | -12.9 | +3.9 | -1.7 | -1.2 | 1407 |
| 111 | Western Kentucky | Conference USA | -12.1 | -5.8 | -3.8 | -0.5 | -2.0 | 1343 |
| 112 | Arkansas State | Sun Belt | -12.2 | -3.7 | -6.9 | +0.1 | -1.6 | 1374 |
| 113 | Coastal Carolina | Sun Belt | -12.3 | -7.1 | -3.7 | +0.3 | -1.7 | 1368 |
| 114 | Troy | Sun Belt | -12.4 | -8.5 | -0.5 | -1.3 | -2.1 | 1336 |
| 115 | Rice | American Athletic | -12.6 | -2.3 | -6.4 | -0.9 | -3.1 | 1258 |
| 116 | Temple | American Athletic | -13.1 | -0.4 | -8.7 | -0.5 | -3.6 | 1214 |
| 117 | Central Michigan | Mid-American | -13.2 | -5.9 | -6.0 | +0.1 | -1.3 | 1400 |
| 118 | Buffalo | Mid-American | -13.2 | -9.1 | -4.5 | +0.3 | +0.1 | 1521 |
| 119 | Colorado State | Pac-12 | -13.5 | +4.5 | -14.5 | -0.2 | -3.3 | 1238 |
| 120 | Nevada | Mountain West | -13.9 | -10.8 | -1.5 | +0.5 | -2.1 | 1337 |
| 121 | Florida International | Conference USA | -14.1 | -9.2 | -1.3 | -1.5 | -2.1 | 1341 |
| 122 | Missouri State | Conference USA | -15.6 | -4.5 | -7.2 | -1.2 | -2.7 | 1292 |
| 123 | New Mexico State | Conference USA | -15.7 | -7.8 | -2.8 | -1.8 | -3.4 | 1235 |
| 124 | Middle Tennessee | Conference USA | -16.0 | -5.2 | -8.4 | +0.3 | -2.7 | 1290 |
| 125 | San José State | Mountain West | -16.1 | -9.9 | -3.3 | -0.3 | -2.5 | 1302 |
| 126 | Southern Miss | Sun Belt | -17.5 | -9.2 | -4.7 | -1.2 | -2.5 | 1305 |
| 127 | Bowling Green | Mid-American | -17.9 | -12.1 | -2.9 | -0.1 | -2.8 | 1280 |
| 128 | UL Monroe | Sun Belt | -18.1 | -5.3 | -7.4 | -1.5 | -4.0 | 1184 |
| 129 | Eastern Michigan | Mid-American | -18.6 | -7.2 | -8.0 | -0.6 | -2.8 | 1280 |
| 130 | Massachusetts | Mid-American | -19.0 | -9.8 | -5.1 | -0.4 | -3.7 | 1207 |
| 131 | Ball State | Mid-American | -19.1 | -6.3 | -8.6 | -0.6 | -3.6 | 1212 |
| 132 | Northern Illinois | Mountain West | -19.6 | -4.5 | -8.9 | -1.2 | -5.0 | 1101 |
| 133 | Sacramento State | Mid-American | -20.2 | -11.1 | -4.7 | +0.1 | -4.6 | 1136 |
| 134 | Sam Houston | Conference USA | -20.3 | -13.2 | -1.1 | -1.3 | -4.8 | 1114 |
| 135 | Charlotte | American Athletic | -20.4 | -9.2 | -6.7 | -0.5 | -3.9 | 1187 |
| 136 | Kent State | Mid-American | -22.6 | -10.8 | -7.4 | -0.7 | -3.7 | 1203 |
| 137 | Akron | Mid-American | -23.0 | -9.5 | -9.2 | -0.4 | -3.8 | 1199 |
| 138 | UTEP | Mountain West | -25.6 | -11.7 | -7.7 | -1.1 | -5.2 | 1088 |

## Current model fit

- Fitted on 4398 games from seasons 2022–2026.
- Home field on top of the ratings: 3.3 points (1.8 in conference games).
- Extra FBS edge over FCS opponents beyond their ratings: 14.0 points.
- Elo weight: 0.20 points of margin per point of Elo spread.
- Weight on the betting line: 91% for the margin, 82% for the total.
