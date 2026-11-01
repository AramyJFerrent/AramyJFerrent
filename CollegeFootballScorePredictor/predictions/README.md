# College football score predictions

Updated Sat Oct 31, 2026 09:06 PM ET. Refreshed automatically every day of the season and several times on Saturdays; each game's prediction is locked at kickoff and graded once the final score is in. Scores are the most likely real scoreline near the expected points; ranges cover 80% of simulated outcomes for each team. College scores scatter widely, so read the ranges, not just the headline score.

Expected points blend the model with the betting line using the weight that has predicted best in recent seasons (see Current model fit). The spread and total columns show the model's own numbers next to the line, so you can see where it disagrees. Games without a line yet use the model alone.

The fair moneyline is the American odds that match the win chance exactly, with no bookmaker margin: -200 means risk $200 to win $100, +200 means risk $100 to win $200. A sportsbook's price will be a little worse on both sides because of its cut, so a book only offers value on a team when its price beats the fair line.

The edge columns judge each bet by its expected value per $1 staked at the posted price, using the final prediction: the model blended with the line, run through the score simulator, pushes included, and anchored to the market's own chances so that only what the blend moves off the line counts. The model's own spread and total (shown alongside) sit several points from the line in most games, but the blend keeps only the share of that disagreement the model has earned in past seasons, so edges are rare. The side with the higher value is shown when it reaches 3% (+3 cents per $1), as the team or side, the price, the expected value, its chance of winning the bet and its stake, a 25% share of the Kelly stake in units of 1% of the bankroll with at most 3 units on one game; anything short is no edge. Where a book posts no price for a spread or total it is assumed to be -110 and marked -110*; moneylines are never assumed. In the walk-forward backtest against closing lines, edges returned spread -100.0% on 1 bets (posted prices, 2016–2019); spread -3.9% on 156 bets (assumed -110 prices, 2016–2025); moneyline +13.7% on 575 bets (posted prices, 2016–2025); total +2.6% on 367 bets (posted prices, 2016–2019); total -5.7% on 172 bets (assumed -110 prices, 2016–2025). None of these is clearly above zero, so treat these edges as an experiment, not a betting system. The live record is tracked below, graded at the price logged with the last prediction before kickoff.

## 2026 Week 9

| Kickoff (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected points | 80% range | Spread: model / line | Total: model / line | Spread edge | Moneyline edge | Total edge | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sat 10/31 10:00 PM | Texas State @ Boise State | Texas State 28, Boise State 38 | Boise State 76% | Texas State +320 / Boise State -320 | 26.2 – 36.9 | 13–41 / 21–52 | Boise State -12.5 / Boise State -10.5 | 63.6 / 63.0 | no edge | no edge | no edge |  |
| Sat 10/31 10:30 PM | Northern Illinois @ UNLV | Northern Illinois 17, UNLV 38 | UNLV 93% | Northern Illinois +1420 / UNLV -1420 | 16.5 – 37.8 | 6–28 / 23–54 | UNLV -17.4 / UNLV -21.8 | 53.5 / 54.5 | no edge | no edge | no edge |  |
| Sat 10/31 11:00 PM | Oregon State @ Fresno State | Oregon State 31, Fresno State 24 | Oregon State 65% | Oregon State -185 / Fresno State +185 | 31.7 – 25.9 | 17–47 / 13–41 | Oregon State -3.6 / Oregon State -6.0 | 56.3 / 58.0 | no edge | no edge | no edge |  |

## 2026 Week 10

| Kickoff (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected points | 80% range | Spread: model / line | Total: model / line | Spread edge | Moneyline edge | Total edge | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tue 11/03 7:00 PM | Ohio @ Akron | Ohio 31, Akron 17 | Ohio 81% | Ohio -440 / Akron +440 | 31.3 – 18.3 | 17–45 / 7–31 | Ohio -18.3 / Ohio -12.5 | 50.0 / 49.5 | no edge | no edge | no edge |  |
| Tue 11/03 8:00 PM | Buffalo @ Miami (OH) | Buffalo 17, Miami (OH) 24 | Miami (OH) 69% | Buffalo +225 / Miami (OH) -225 | 19.4 – 26.5 | 7–31 / 13–41 | Miami (OH) -12.7 / Miami (OH) -6.5 | 48.5 / 45.5 | no edge | no edge | no edge |  |
| Wed 11/04 7:00 PM | Ball State @ Massachusetts | Ball State 24, Massachusetts 27 | Massachusetts 62% | Ball State +165 / Massachusetts -165 | 22.1 – 26.5 | 10–35 / 13–41 | Massachusetts -2.9 / Massachusetts -4.5 | 49.0 / 48.5 | no edge | no edge | no edge |  |
| Wed 11/04 7:00 PM | Toledo @ Sacramento State | Toledo 38, Sacramento State 10 | Toledo 97% | Toledo -3090 / Sacramento State +3090 | 38.5 – 12.8 | 24–54 / 3–24 | Toledo -17.8 / Toledo -26.5 | 50.2 / 51.5 | no edge | no edge | no edge |  |
| Wed 11/04 7:30 PM | Central Michigan vs Eastern Michigan | Central Michigan 21, Eastern Michigan 24 | Eastern Michigan 52% | Central Michigan +110 / Eastern Michigan -110 | 23.1 – 24.1 | 10–37 / 10–38 | Central Michigan -3.6 / Eastern Michigan -1.5 | 49.9 / 46.5 | no edge | no edge | no edge | neutral site |
| Thu 11/05 7:30 PM | UTSA @ Florida Atlantic | UTSA 38, Florida Atlantic 31 | UTSA 65% | UTSA -185 / Florida Atlantic +185 | 37.9 – 31.8 | 23–52 / 17–46 | UTSA -2.6 / UTSA -6.5 | 66.4 / 70.5 | no edge | no edge | no edge |  |
| Thu 11/05 8:00 PM | James Madison @ Southern Miss | James Madison 38, Southern Miss 21 | James Madison 85% | James Madison -580 / Southern Miss +580 | 35.7 – 20.3 | 21–51 / 7–34 | James Madison -14.9 / James Madison -15.5 | 53.9 / 56.5 | no edge | no edge | no edge |  |
| Fri 11/06 7:00 PM | Virginia Tech @ SMU | Virginia Tech 24, SMU 31 | SMU 68% | Virginia Tech +210 / SMU -210 | 24.6 – 31.6 | 13–38 / 17–47 | SMU -11.0 / SMU -6.5 | 55.0 / 56.5 | no edge | no edge | no edge |  |
| Fri 11/06 7:30 PM | South Florida @ East Carolina | South Florida 24, East Carolina 21 | South Florida 53% | South Florida -110 / East Carolina +110 | 24.1 – 23.4 | 10–38 / 10–37 | South Florida -0.7 / – | 47.6 / – | no line yet | no line yet (fair: South Florida -110) | no line yet |  |
| Fri 11/06 8:00 PM | Nebraska @ Illinois | Nebraska 31, Illinois 24 | Nebraska 69% | Nebraska -220 / Illinois +220 | 30.2 – 22.7 | 16–45 / 10–36 | Nebraska -7.5 / – | 53.8 / – | no line yet | no line yet (fair: Nebraska -220) | no line yet |  |
| Fri 11/06 9:00 PM | New Mexico @ Nevada | New Mexico 24, Nevada 17 | New Mexico 77% | New Mexico -340 / Nevada +340 | 26.1 – 16.0 | 13–41 / 6–28 | New Mexico -10.1 / – | 42.1 / – | no line yet | no line yet (fair: New Mexico -340) | no line yet |  |
| Fri 11/06 10:15 PM | TCU @ Arizona | TCU 21, Arizona 28 | Arizona 72% | TCU +260 / Arizona -260 | 20.3 – 28.8 | 7–34 / 14–43 | Arizona -8.5 / – | 49.1 / – | no line yet | no line yet (fair: Arizona -260) | no line yet |  |
| Sat 11/07 TBA | UCF @ Kansas | UCF 24, Kansas 31 | Kansas 68% | UCF +215 / Kansas -215 | 22.6 – 29.4 | 10–35 / 15–44 | Kansas -6.8 / – | 52.0 / – | no line yet | no line yet (fair: Kansas -215) | no line yet |  |
| Sat 11/07 TBA | Cincinnati @ Houston | Cincinnati 28, Houston 35 | Houston 65% | Cincinnati +190 / Houston -190 | 28.3 – 34.6 | 14–43 / 20–49 | Houston -6.2 / – | 62.9 / – | no line yet | no line yet (fair: Houston -190) | no line yet |  |
| Sat 11/07 TBA | Iowa State @ Baylor | Iowa State 24, Baylor 27 | Baylor 65% | Iowa State +185 / Baylor -185 | 22.7 – 28.1 | 10–36 / 14–42 | Baylor -5.4 / – | 50.8 / – | no line yet | no line yet (fair: Baylor -185) | no line yet |  |
| Sat 11/07 TBA | Oklahoma State @ Kansas State | Oklahoma State 24, Kansas State 31 | Kansas State 65% | Oklahoma State +185 / Kansas State -185 | 26.2 – 32.1 | 13–41 / 17–47 | Kansas State -5.8 / – | 58.3 / – | no line yet | no line yet (fair: Kansas State -185) | no line yet |  |
| Sat 11/07 TBA | West Virginia @ Texas Tech | West Virginia 17, Texas Tech 38 | Texas Tech 93% | West Virginia +1410 / Texas Tech -1410 | 17.7 – 39.2 | 6–31 / 24–55 | Texas Tech -21.5 / – | 56.8 / – | no line yet | no line yet (fair: Texas Tech -1410) | no line yet |  |
| Sat 11/07 TBA | Michigan State @ Michigan | Michigan State 10, Michigan 27 | Michigan 86% | Michigan State +595 / Michigan -595 | 12.7 – 27.3 | 3–24 / 14–42 | Michigan -21.0 / Michigan -14.0 | 42.3 / 39.5 | no edge | no edge | no edge |  |
| Sat 11/07 TBA | UCLA @ Minnesota | UCLA 24, Minnesota 17 | UCLA 68% | UCLA -215 / Minnesota +215 | 24.4 – 17.6 | 10–38 / 7–30 | UCLA -9.8 / UCLA -6.5 | 40.2 / 42.5 | no edge | no edge | no edge |  |
| Sat 11/07 TBA | Iowa @ Northwestern | Iowa 21, Northwestern 24 | Northwestern 57% | Iowa +130 / Northwestern -130 | 20.8 – 23.1 | 7–34 / 10–37 | Northwestern -0.6 / Northwestern -2.5 | 49.5 / 42.5 | no edge | no edge | no edge |  |
| Sat 11/07 TBA | Penn State @ Washington | Penn State 24, Washington 21 | Penn State 52% | Penn State -105 / Washington +105 | 23.6 – 23.0 | 10–37 / 10–37 | Penn State -0.6 / – | 46.6 / – | no line yet | no line yet (fair: Penn State -105) | no line yet |  |
| Sat 11/07 12:00 PM | Texas @ Missouri | Texas 24, Missouri 21 | Texas 59% | Texas -145 / Missouri +145 | 25.9 – 22.6 | 13–41 / 10–36 | Texas -0.8 / Texas -3.5 | 45.0 / 49.5 | no edge | no edge | no edge |  |
| Sat 11/07 12:00 PM | BYU @ Utah | BYU 24, Utah 27 | Utah 63% | BYU +170 / Utah -170 | 22.3 – 27.2 | 10–35 / 14–41 | Utah -9.0 / Utah -4.5 | 53.7 / 48.5 | no edge | no edge | no edge |  |
| Sat 11/07 12:00 PM | Clemson @ Syracuse | Clemson 27, Syracuse 24 | Clemson 52% | Clemson -105 / Syracuse +105 | 24.4 – 24.0 | 10–38 / 10–38 | Clemson -0.4 / – | 48.4 / – | no line yet | no line yet (fair: Clemson -105) | no line yet |  |
| Sat 11/07 12:00 PM | Florida State @ Boston College | Florida State 31, Boston College 24 | Florida State 74% | Florida State -290 / Boston College +290 | 32.0 – 22.1 | 17–47 / 10–35 | Florida State -9.9 / – | 54.2 / – | no line yet | no line yet (fair: Florida State -290) | no line yet |  |
| Sat 11/07 12:00 PM | North Carolina @ UConn | North Carolina 31, UConn 28 | UConn 51% | North Carolina +105 / UConn -105 | 28.1 – 28.3 | 14–43 / 14–42 | UConn -0.1 / – | 56.4 / – | no line yet | no line yet (fair: UConn -105) | no line yet |  |
| Sat 11/07 12:00 PM | Tulsa @ Tulane | Tulsa 24, Tulane 27 | Tulane 57% | Tulsa +135 / Tulane -135 | 24.8 – 27.2 | 11–38 / 14–41 | Tulane -2.4 / – | 52.6 / – | no line yet | no line yet (fair: Tulane -135) | no line yet |  |
| Sat 11/07 12:30 PM | Duke @ NC State | Duke 27, NC State 24 | Duke 56% | Duke -130 / NC State +130 | 29.2 – 26.8 | 16–44 / 14–41 | Duke -2.3 / – | 56.0 / – | no line yet | no line yet (fair: Duke -130) | no line yet |  |
| Sat 11/07 12:30 PM | Maryland @ Purdue | Maryland 24, Purdue 27 | Purdue 56% | Maryland +130 / Purdue -130 | 23.9 – 26.3 | 10–38 / 13–41 | Purdue -2.4 / – | 51.9 / – | no line yet | no line yet (fair: Purdue -130) | no line yet |  |
| Sat 11/07 12:30 PM | Rutgers @ Wisconsin | Rutgers 17, Wisconsin 31 | Wisconsin 84% | Rutgers +525 / Wisconsin -525 | 17.6 – 31.8 | 7–30 / 17–47 | Wisconsin -14.2 / – | 50.1 / – | no line yet | no line yet (fair: Wisconsin -525) | no line yet |  |
| Sat 11/07 12:45 PM | Arkansas @ Auburn | Arkansas 20, Auburn 34 | Auburn 83% | Arkansas +505 / Auburn -505 | 19.4 – 33.7 | 7–32 / 20–49 | Auburn -14.3 / – | 53.8 / – | no line yet | no line yet (fair: Auburn -505) | no line yet |  |
| Sat 11/07 1:00 PM | Old Dominion @ Coastal Carolina | Old Dominion 17, Coastal Carolina 24 | Coastal Carolina 68% | Old Dominion +210 / Coastal Carolina -210 | 18.3 – 24.5 | 7–31 / 10–38 | Coastal Carolina -6.2 / – | 43.8 / – | no line yet | no line yet (fair: Coastal Carolina -210) | no line yet |  |
| Sat 11/07 2:30 PM | Georgia State @ App State | Georgia State 24, App State 31 | App State 67% | Georgia State +200 / App State -200 | 26.2 – 32.5 | 13–41 / 17–48 | App State -6.2 / – | 58.8 / – | no line yet | no line yet (fair: App State -200) | no line yet |  |
| Sat 11/07 3:00 PM | Texas A&M @ South Carolina | Texas A&M 27, South Carolina 24 | Texas A&M 50% | Texas A&M -100 / South Carolina +100 | 24.3 – 24.0 | 10–38 / 10–38 | Texas A&M -0.3 / – | 49.2 / – | no line yet | no line yet (fair: Texas A&M -100) | no line yet |  |
| Sat 11/07 3:00 PM | UL Monroe @ Arkansas State | UL Monroe 17, Arkansas State 31 | Arkansas State 81% | UL Monroe +415 / Arkansas State -415 | 20.0 – 32.5 | 7–34 / 17–48 | Arkansas State -12.5 / – | 53.4 / – | no line yet | no line yet (fair: Arkansas State -415) | no line yet |  |
| Sat 11/07 3:00 PM | Delaware @ Kennesaw State | Delaware 31, Kennesaw State 24 | Delaware 64% | Delaware -180 / Kennesaw State +180 | 29.8 – 24.7 | 16–45 / 12–38 | Delaware -5.1 / – | 55.3 / – | no line yet | no line yet (fair: Delaware -180) | no line yet |  |
| Sat 11/07 3:30 PM | Alabama @ LSU | Alabama 24, LSU 27 | LSU 64% | Alabama +175 / LSU -175 | 23.6 – 28.5 | 10–37 / 14–43 | LSU -9.2 / LSU -4.5 | 50.3 / 52.5 | no edge | no edge | no edge |  |
| Sat 11/07 3:30 PM | Merrimack @ Wake Forest | Merrimack 0, Wake Forest 59 | Wake Forest 100% | Merrimack +9900 / Wake Forest -9900 | 3.0 – 61.2 | 0–7 / 48–75 | Wake Forest -58.2 / – | 64.2 / – | no line yet | no line yet (fair: Wake Forest -9900) | no line yet | FCS opponent |
| Sat 11/07 3:30 PM | Oregon @ Ohio State | Oregon 17, Ohio State 31 | Ohio State 84% | Oregon +520 / Ohio State -520 | 16.2 – 30.1 | 6–28 / 16–45 | Ohio State -12.7 / Ohio State -14.0 | 49.3 / 45.5 | no edge | no edge | no edge |  |
| Sat 11/07 3:30 PM | Charlotte @ UAB | Charlotte 17, UAB 31 | UAB 82% | Charlotte +440 / UAB -440 | 18.5 – 31.4 | 7–31 / 17–46 | UAB -12.9 / – | 50.0 / – | no line yet | no line yet (fair: UAB -440) | no line yet |  |
| Sat 11/07 3:30 PM | Temple @ Navy | Temple 21, Navy 31 | Navy 76% | Temple +310 / Navy -310 | 22.3 – 33.0 | 10–35 / 19–48 | Navy -10.7 / – | 55.4 / – | no line yet | no line yet (fair: Navy -310) | no line yet |  |
| Sat 11/07 3:30 PM | Marshall @ Georgia Southern | Marshall 27, Georgia Southern 24 | Marshall 50% | Marshall -100 / Georgia Southern +100 | 28.2 – 27.7 | 14–42 / 14–42 | Marshall -0.5 / – | 57.9 / – | no line yet | no line yet (fair: Marshall -100) | no line yet |  |
| Sat 11/07 3:30 PM | Western Kentucky @ Middle Tennessee | Western Kentucky 27, Middle Tennessee 24 | Western Kentucky 56% | Western Kentucky -125 / Middle Tennessee +125 | 26.3 – 24.0 | 13–41 / 10–38 | Western Kentucky -2.2 / – | 50.8 / – | no line yet | no line yet (fair: Western Kentucky -125) | no line yet |  |
| Sat 11/07 4:00 PM | Rice @ North Texas | Rice 24, North Texas 41 | North Texas 90% | Rice +875 / North Texas -875 | 22.2 – 41.1 | 10–35 / 27–56 | North Texas -18.9 / – | 63.2 / – | no line yet | no line yet (fair: North Texas -875) | no line yet |  |
| Sat 11/07 4:00 PM | Northern Illinois @ San José State | Northern Illinois 24, San José State 31 | San José State 65% | Northern Illinois +190 / San José State -190 | 22.9 – 28.8 | 10–37 / 14–43 | San José State -5.9 / – | 51.8 / – | no line yet | no line yet (fair: San José State -190) | no line yet |  |
| Sat 11/07 4:00 PM | Missouri State @ Florida International | Missouri State 24, Florida International 27 | Florida International 53% | Missouri State +110 / Florida International -110 | 24.2 – 25.2 | 10–38 / 13–38 | Florida International -1.0 / – | 50.4 / – | no line yet | no line yet (fair: Florida International -110) | no line yet |  |
| Sat 11/07 4:00 PM | Louisiana Tech @ Troy | Louisiana Tech 24, Troy 21 | Louisiana Tech 68% | Louisiana Tech -210 / Troy +210 | 26.3 – 20.0 | 13–41 / 7–33 | Louisiana Tech -6.3 / – | 46.3 / – | no line yet | no line yet (fair: Louisiana Tech -210) | no line yet |  |
| Sat 11/07 4:15 PM | Vanderbilt @ Mississippi State | Vanderbilt 24, Mississippi State 31 | Mississippi State 70% | Vanderbilt +235 / Mississippi State -235 | 24.5 – 32.4 | 10–38 / 17–48 | Mississippi State -7.9 / – | 57.0 / – | no line yet | no line yet (fair: Mississippi State -235) | no line yet |  |
| Sat 11/07 5:00 PM | South Alabama @ Louisiana | South Alabama 28, Louisiana 31 | Louisiana 62% | South Alabama +165 / Louisiana -165 | 26.8 – 31.3 | 13–41 / 17–46 | Louisiana -4.5 / – | 58.2 / – | no line yet | no line yet (fair: Louisiana -165) | no line yet |  |
| Sat 11/07 6:00 PM | Boise State @ Colorado State | Boise State 41, Colorado State 24 | Boise State 87% | Boise State -690 / Colorado State +690 | 39.8 – 22.8 | 24–56 / 10–37 | Boise State -17.0 / – | 62.6 / – | no line yet | no line yet (fair: Boise State -690) | no line yet |  |
| Sat 11/07 6:15 PM | Kentucky @ Tennessee | Kentucky 24, Tennessee 27 | Tennessee 66% | Kentucky +195 / Tennessee -195 | 22.1 – 27.9 | 10–35 / 14–42 | Tennessee -8.8 / Tennessee -5.5 | 48.3 / 50.5 | no edge | no edge | no edge |  |
| Sat 11/07 7:00 PM | Sam Houston @ Jacksonville State | Sam Houston 14, Jacksonville State 31 | Jacksonville State 90% | Sam Houston +855 / Jacksonville State -855 | 14.0 – 31.6 | 3–26 / 17–47 | Jacksonville State -17.6 / – | 45.5 / – | no line yet | no line yet (fair: Jacksonville State -855) | no line yet |  |
| Sat 11/07 7:30 PM | Georgia @ Ole Miss | Georgia 27, Ole Miss 24 | Georgia 58% | Georgia -140 / Ole Miss +140 | 29.5 – 26.5 | 14–44 / 13–41 | Georgia -3.1 / Georgia -3.0 | 54.0 / 56.5 | no edge | no edge | no edge |  |
| Sat 11/07 7:30 PM | Colorado @ Arizona State | Colorado 24, Arizona State 27 | Arizona State 66% | Colorado +195 / Arizona State -195 | 22.1 – 27.8 | 10–35 / 14–42 | Arizona State -5.8 / – | 49.9 / – | no line yet | no line yet (fair: Arizona State -195) | no line yet |  |
| Sat 11/07 7:30 PM | Louisville @ Georgia Tech | Louisville 38, Georgia Tech 21 | Louisville 87% | Louisville -680 / Georgia Tech +680 | 37.5 – 20.6 | 23–52 / 7–34 | Louisville -16.9 / – | 58.7 / – | no line yet | no line yet (fair: Louisville -680) | no line yet |  |
| Sat 11/07 7:30 PM | Miami @ Notre Dame | Miami 24, Notre Dame 27 | Notre Dame 59% | Miami +145 / Notre Dame -145 | 25.7 – 29.2 | 13–40 / 16–44 | Notre Dame -3.8 / Notre Dame -3.5 | 52.3 / 55.5 | no edge | no edge | no edge |  |
| Sat 11/07 7:30 PM | Air Force @ Army | Air Force 24, Army 27 | Army 65% | Air Force +185 / Army -185 | 23.4 – 29.0 | 10–37 / 15–43 | Army -6.8 / Army -5.5 | 60.1 / 50.5 | no edge | no edge | Over 50.5 (-110*): EV +5.6%, 55%, stake 1.5u | * price not posted; assumed -110 |
| Sat 11/07 7:45 PM | Oklahoma @ Florida | Oklahoma 24, Florida 27 | Florida 59% | Oklahoma +145 / Florida -145 | 22.2 – 25.6 | 10–35 / 13–40 | Oklahoma -2.2 / Florida -4.0 | 44.6 / 48.5 | no edge | no edge | no edge |  |
| Sat 11/07 8:00 PM | Liberty @ New Mexico State | Liberty 31, New Mexico State 14 | Liberty 87% | Liberty -695 / New Mexico State +695 | 31.8 – 15.4 | 17–48 / 3–27 | Liberty -16.3 / – | 47.2 / – | no line yet | no line yet (fair: Liberty -695) | no line yet |  |
| Sat 11/07 9:30 PM | Fresno State @ Utah State | Fresno State 24, Utah State 21 | Fresno State 57% | Fresno State -130 / Utah State +130 | 24.4 – 22.2 | 10–38 / 10–35 | Fresno State -2.2 / – | 46.6 / – | no line yet | no line yet (fair: Fresno State -130) | no line yet |  |
| Sat 11/07 9:30 PM | Hawai'i @ UTEP | Hawai'i 31, UTEP 17 | Hawai'i 81% | Hawai'i -435 / UTEP +435 | 31.2 – 18.5 | 17–46 / 7–31 | Hawai'i -12.7 / – | 49.7 / – | no line yet | no line yet (fair: Hawai'i -435) | no line yet |  |
| Sat 11/07 10:30 PM | Texas State @ Oregon State | Texas State 31, Oregon State 38 | Oregon State 70% | Texas State +230 / Oregon State -230 | 29.7 – 37.5 | 16–45 / 23–52 | Oregon State -7.8 / – | 67.2 / – | no line yet | no line yet (fair: Oregon State -230) | no line yet |  |
| Sat 11/07 10:30 PM | Wyoming @ UNLV | Wyoming 21, UNLV 28 | UNLV 73% | Wyoming +270 / UNLV -270 | 20.1 – 29.1 | 7–34 / 14–44 | UNLV -9.0 / – | 49.1 / – | no line yet | no line yet (fair: UNLV -270) | no line yet |  |

## How the 2026 predictions have done

| Predictor | Games | Margin MAE | Total MAE | Team-score MAE | Winners | Brier | 80% range hit |
|---|---|---|---|---|---|---|---|
| Final prediction | 607 | 11.59 | 12.09 | 8.37 | 80.7% | 0.137 | 82.5% |
| Model only (before blending) | 607 | 12.32 | 12.39 | 8.64 | 77.9% | – | – |
| Betting line when predicted | 605 | 11.58 | 12.05 | 8.36 | 80.7% | – | – |

MAE is mean absolute error in points (lower is better). Brier scores the win chances (lower is better, 0.25 is a coin flip). Even the closing betting line misses the final margin of an FBS game by about 12.5 points.

501 of these games were played before the predictor went live. They are backfilled walk-forward (each week predicted from earlier weeks only) but with closing lines, so they flatter the model slightly. Every game since is graded on the prediction logged before kickoff.

### Betting edges

| Market | Edges | Record (W-L-P) | Staked | Units won | ROI | Expected ROI |
|---|---|---|---|---|---|---|
| Spread | 0 | 0-0-0 | 0.0 | +0.00 | – | – |
| Moneyline | 3 | 0-3-0 | 1.1 | -1.10 | -100.0% | +4.8% |
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
| Purdue @ Penn State | 21–31 | 17–31 | 75% | yes |
| Nevada @ UCLA | 10–34 | 0–27 | 96% | yes |

## FBS power ratings

Points per game better than an average FBS team on a neutral field, from opponent-adjusted EPA (garbage time removed) with this season's games weighted against a preseason prior, plus the weight the margin model puts on Elo (a rating built from game results alone). Defense is positive when it holds opponents below average.

| # | Team | Conference | Net | Offense | Defense | Special teams | Results (Elo) | Elo rating |
|---|---|---|---|---|---|---|---|---|
| 1 | Ohio State | Big Ten | +27.0 | +11.3 | +10.2 | +0.4 | +5.1 | 1934 |
| 2 | LSU | SEC | +26.4 | +10.7 | +12.5 | +0.2 | +2.9 | 1751 |
| 3 | Miami | ACC | +24.0 | +13.1 | +6.1 | +0.2 | +4.6 | 1890 |
| 4 | Georgia | SEC | +24.0 | +8.0 | +10.7 | +0.9 | +4.4 | 1880 |
| 5 | Notre Dame | FBS Independents | +23.1 | +8.9 | +9.0 | +1.1 | +4.2 | 1858 |
| 6 | Indiana | Big Ten | +21.7 | +5.7 | +10.7 | +0.1 | +5.2 | 1939 |
| 7 | Utah | Big 12 | +20.5 | +10.7 | +5.8 | +0.0 | +4.0 | 1842 |
| 8 | Alabama | SEC | +19.6 | +9.0 | +7.1 | +0.2 | +3.2 | 1777 |
| 9 | Ole Miss | SEC | +18.6 | +10.4 | +3.9 | +0.7 | +3.7 | 1815 |
| 10 | Texas | SEC | +18.6 | +3.0 | +11.7 | +0.4 | +3.5 | 1803 |
| 11 | Texas Tech | Big 12 | +18.3 | +2.1 | +11.9 | +1.2 | +3.0 | 1761 |
| 12 | Oklahoma | SEC | +17.5 | +1.6 | +13.3 | +0.6 | +2.0 | 1677 |
| 13 | Oregon | Big Ten | +16.8 | +4.5 | +8.9 | +0.5 | +2.8 | 1743 |
| 14 | UCLA | Big Ten | +16.6 | +4.6 | +9.3 | +0.7 | +2.0 | 1676 |
| 15 | Wake Forest | ACC | +16.4 | +6.2 | +7.2 | +0.5 | +2.4 | 1710 |
| 16 | Louisville | ACC | +15.8 | +9.9 | +3.8 | +0.0 | +2.1 | 1681 |
| 17 | Tennessee | SEC | +15.4 | +3.5 | +8.6 | +0.7 | +2.6 | 1723 |
| 18 | Missouri | SEC | +15.3 | +4.4 | +8.3 | +0.5 | +2.1 | 1686 |
| 19 | Michigan | Big Ten | +14.9 | +3.5 | +9.3 | +0.0 | +2.0 | 1674 |
| 20 | Nebraska | Big Ten | +13.9 | +4.9 | +7.1 | +0.6 | +1.4 | 1622 |
| 21 | SMU | ACC | +13.4 | +7.5 | +3.7 | +0.2 | +2.0 | 1675 |
| 22 | BYU | Big 12 | +13.4 | +5.6 | +4.2 | +0.6 | +3.0 | 1759 |
| 23 | Iowa | Big Ten | +13.1 | +1.7 | +7.7 | +0.8 | +2.9 | 1751 |
| 24 | USC | Big Ten | +12.7 | +10.6 | -0.0 | +0.2 | +2.0 | 1672 |
| 25 | Florida | SEC | +12.4 | +6.5 | +4.2 | +0.9 | +0.8 | 1579 |
| 26 | Arizona | Big 12 | +12.0 | +6.4 | +3.5 | -0.2 | +2.4 | 1708 |
| 27 | Texas A&M | SEC | +12.0 | +2.6 | +7.8 | +0.5 | +1.1 | 1601 |
| 28 | Auburn | SEC | +12.0 | +5.5 | +5.5 | +0.6 | +0.3 | 1536 |
| 29 | Penn State | Big Ten | +11.4 | +3.0 | +7.0 | +0.1 | +1.2 | 1611 |
| 30 | Northwestern | Big Ten | +11.2 | +7.1 | +1.8 | +0.8 | +1.5 | 1634 |
| 31 | Houston | Big 12 | +10.2 | +7.9 | +0.1 | +0.2 | +2.0 | 1673 |
| 32 | Mississippi State | SEC | +9.8 | +6.9 | +2.3 | +0.4 | +0.2 | 1523 |
| 33 | Kansas State | Big 12 | +9.8 | +6.2 | +3.0 | +0.4 | +0.2 | 1526 |
| 34 | Kentucky | SEC | +9.5 | +2.8 | +4.4 | +0.3 | +2.0 | 1677 |
| 35 | Baylor | Big 12 | +9.3 | +0.3 | +6.9 | +1.0 | +1.1 | 1601 |
| 36 | South Carolina | SEC | +8.9 | +4.5 | +2.6 | +0.8 | +1.1 | 1599 |
| 37 | Washington | Big Ten | +8.4 | +2.8 | +4.1 | -0.0 | +1.5 | 1635 |
| 38 | Wisconsin | Big Ten | +8.1 | -0.2 | +7.0 | +0.2 | +1.0 | 1593 |
| 39 | Kansas | Big 12 | +7.2 | +4.6 | +3.5 | -0.0 | -0.8 | 1439 |
| 40 | Boise State | Pac-12 | +7.2 | +5.1 | -0.4 | +0.1 | +2.5 | 1717 |
| 41 | Duke | ACC | +6.8 | +2.7 | +1.3 | +0.8 | +2.0 | 1677 |
| 42 | Iowa State | Big 12 | +6.5 | +2.4 | +2.7 | +0.9 | +0.5 | 1552 |
| 43 | Oklahoma State | Big 12 | +6.3 | +6.7 | -0.7 | +0.5 | -0.2 | 1495 |
| 44 | Cincinnati | Big 12 | +6.3 | +8.9 | -3.8 | +0.4 | +0.7 | 1568 |
| 45 | Florida State | ACC | +6.3 | +8.0 | -1.4 | -0.2 | -0.1 | 1497 |
| 46 | Arizona State | Big 12 | +5.6 | +1.0 | +4.1 | +0.0 | +0.5 | 1550 |
| 47 | TCU | Big 12 | +5.4 | -2.3 | +6.3 | +0.5 | +0.9 | 1587 |
| 48 | Virginia Tech | ACC | +4.8 | +3.2 | +0.7 | +0.3 | +0.7 | 1566 |
| 49 | Illinois | Big Ten | +4.6 | +6.0 | -2.5 | -0.1 | +1.2 | 1610 |
| 50 | Vanderbilt | SEC | +4.5 | +4.6 | -0.6 | +0.3 | +0.2 | 1529 |
| 51 | Minnesota | Big Ten | +4.0 | -4.1 | +6.5 | +1.0 | +0.6 | 1561 |
| 52 | North Texas | American Athletic | +3.5 | +10.2 | -7.5 | -0.9 | +1.6 | 1645 |
| 53 | NC State | ACC | +3.4 | +5.7 | -2.0 | -0.6 | +0.4 | 1538 |
| 54 | Clemson | ACC | +3.4 | -4.8 | +6.9 | +0.4 | +0.8 | 1578 |
| 55 | Pittsburgh | ACC | +3.2 | -0.1 | +2.4 | +0.5 | +0.4 | 1542 |
| 56 | Colorado | Big 12 | +3.0 | +0.5 | +4.7 | -0.7 | -1.6 | 1378 |
| 57 | UCF | Big 12 | +2.8 | +0.7 | +2.7 | +0.0 | -0.6 | 1459 |
| 58 | Oregon State | Pac-12 | +2.6 | +5.0 | -2.4 | +0.1 | -0.1 | 1498 |
| 59 | UTSA | American Athletic | +2.1 | +3.0 | -2.9 | -0.1 | +2.1 | 1686 |
| 60 | James Madison | Sun Belt | +1.9 | -1.8 | +1.1 | +0.4 | +2.3 | 1698 |
| 61 | Syracuse | ACC | +1.8 | +1.7 | +2.3 | -0.9 | -1.2 | 1407 |
| 62 | Arkansas | SEC | +1.2 | +1.3 | +0.4 | -0.4 | -0.1 | 1496 |
| 63 | Liberty | Conference USA | +1.1 | +0.7 | -0.5 | +0.4 | +0.5 | 1551 |
| 64 | Memphis | American Athletic | +1.0 | +2.9 | -2.0 | -0.5 | +0.7 | 1566 |
| 65 | Virginia | ACC | +1.0 | -1.3 | +3.0 | -0.5 | -0.2 | 1494 |
| 66 | North Carolina | ACC | +0.6 | +0.6 | -1.0 | +0.9 | +0.1 | 1514 |
| 67 | Purdue | Big Ten | +0.6 | +2.9 | -2.1 | +0.8 | -1.0 | 1426 |
| 68 | Maryland | Big Ten | +0.5 | -1.5 | +3.1 | +1.0 | -2.1 | 1334 |
| 69 | Toledo | Mid-American | -0.0 | -1.2 | +0.6 | -0.0 | +0.6 | 1555 |
| 70 | West Virginia | Big 12 | -0.1 | +4.1 | -4.7 | +0.6 | -0.1 | 1502 |
| 71 | New Mexico | Mountain West | -0.2 | -3.3 | +2.1 | -0.3 | +1.3 | 1618 |
| 72 | North Dakota State | Mountain West | -1.1 | -5.1 | +4.0 | +1.0 | -1.1 | 1419 |
| 73 | Texas State | Pac-12 | -1.2 | +5.1 | -5.6 | -1.5 | +0.7 | 1567 |
| 74 | Navy | American Athletic | -1.2 | +3.6 | -3.9 | -0.6 | -0.4 | 1473 |
| 75 | South Florida | American Athletic | -1.3 | -2.3 | -0.2 | +0.2 | +1.0 | 1593 |
| 76 | UConn | FBS Independents | -2.0 | +2.2 | -3.5 | -0.3 | -0.4 | 1472 |
| 77 | Army | American Athletic | -2.1 | +5.0 | -8.1 | -0.1 | +1.1 | 1602 |
| 78 | Louisiana Tech | Sun Belt | -2.8 | -3.1 | +0.7 | -0.7 | +0.4 | 1540 |
| 79 | Fresno State | Pac-12 | -3.4 | -2.4 | -1.4 | -0.0 | +0.4 | 1544 |
| 80 | Ohio | Mid-American | -3.4 | -1.8 | -2.9 | +0.5 | +0.8 | 1578 |
| 81 | Georgia Tech | ACC | -3.6 | +2.8 | -5.2 | +0.0 | -1.1 | 1416 |
| 82 | East Carolina | American Athletic | -3.6 | -5.4 | +2.7 | -0.7 | -0.1 | 1496 |
| 83 | Tulsa | American Athletic | -3.6 | -0.9 | -0.5 | -0.5 | -1.8 | 1358 |
| 84 | Michigan State | Big Ten | -3.7 | -3.5 | +1.2 | +0.1 | -1.4 | 1388 |
| 85 | Florida Atlantic | American Athletic | -3.9 | +4.0 | -7.5 | +0.7 | -1.1 | 1416 |
| 86 | Rutgers | Big Ten | -4.2 | +2.8 | -6.4 | +0.8 | -1.4 | 1388 |
| 87 | Tulane | American Athletic | -4.4 | -3.6 | -1.7 | +0.2 | +0.6 | 1562 |
| 88 | Air Force | Mountain West | -4.9 | +2.5 | -6.8 | -0.3 | -0.2 | 1488 |
| 89 | UNLV | Mountain West | -4.9 | -3.0 | -2.3 | -0.0 | +0.4 | 1540 |
| 90 | Jacksonville State | Conference USA | -4.9 | -0.2 | -4.4 | -0.2 | -0.1 | 1497 |
| 91 | Boston College | ACC | -5.4 | -3.8 | -0.3 | -0.9 | -0.5 | 1469 |
| 92 | California | ACC | -6.2 | -2.1 | -2.0 | -0.4 | -1.7 | 1369 |
| 93 | Delaware | Conference USA | -6.3 | -0.2 | -5.2 | +0.3 | -1.2 | 1406 |
| 94 | Western Michigan | Mid-American | -6.9 | -4.8 | -3.6 | +0.8 | +0.6 | 1561 |
| 95 | Utah State | Pac-12 | -6.9 | -6.7 | +2.1 | -1.2 | -1.2 | 1412 |
| 96 | App State | Sun Belt | -7.0 | -2.6 | -3.6 | -0.2 | -0.7 | 1454 |
| 97 | Marshall | Sun Belt | -7.3 | -3.2 | -3.8 | -0.3 | -0.1 | 1500 |
| 98 | Washington State | Pac-12 | -8.0 | -6.8 | +0.6 | -0.2 | -1.6 | 1373 |
| 99 | Miami (OH) | Mid-American | -8.1 | -4.6 | -3.3 | +0.5 | -0.8 | 1446 |
| 100 | San Diego State | Pac-12 | -8.5 | -5.1 | -2.1 | +0.2 | -1.5 | 1382 |
| 101 | Stanford | ACC | -9.2 | -3.0 | -5.5 | +0.0 | -0.7 | 1448 |
| 102 | Temple | American Athletic | -9.5 | +0.6 | -7.0 | -0.5 | -2.6 | 1291 |
| 103 | Georgia Southern | Sun Belt | -9.5 | -1.9 | -6.3 | -1.0 | -0.3 | 1481 |
| 104 | Louisiana | Sun Belt | -9.6 | -5.0 | -4.1 | -0.1 | -0.4 | 1478 |
| 105 | UAB | American Athletic | -9.9 | -5.8 | -2.5 | -0.4 | -1.2 | 1407 |
| 106 | Arkansas State | Sun Belt | -10.3 | -2.7 | -7.0 | +0.2 | -0.8 | 1441 |
| 107 | Georgia State | Sun Belt | -10.5 | -0.9 | -7.3 | -0.4 | -1.9 | 1347 |
| 108 | Troy | Sun Belt | -11.0 | -7.9 | -0.6 | -1.2 | -1.3 | 1401 |
| 109 | Wyoming | Mountain West | -11.2 | -6.5 | -3.4 | -0.2 | -1.1 | 1413 |
| 110 | Hawai'i | Mountain West | -11.3 | -4.0 | -6.3 | +0.6 | -1.7 | 1365 |
| 111 | Coastal Carolina | Sun Belt | -11.5 | -5.8 | -4.6 | +0.5 | -1.5 | 1384 |
| 112 | Colorado State | Pac-12 | -11.9 | +3.2 | -12.1 | -0.3 | -2.7 | 1286 |
| 113 | South Alabama | Sun Belt | -12.0 | -0.3 | -10.6 | +0.3 | -1.3 | 1398 |
| 114 | Western Kentucky | Conference USA | -12.2 | -6.7 | -3.2 | -0.3 | -2.0 | 1345 |
| 115 | Kennesaw State | Conference USA | -12.8 | -6.6 | -3.6 | -0.8 | -1.9 | 1346 |
| 116 | Rice | American Athletic | -12.9 | -3.6 | -5.2 | -0.9 | -3.1 | 1246 |
| 117 | Old Dominion | Sun Belt | -13.3 | -13.1 | +3.1 | -1.4 | -1.8 | 1357 |
| 118 | Missouri State | Conference USA | -13.3 | -1.7 | -7.4 | -1.4 | -2.7 | 1281 |
| 119 | Nevada | Mountain West | -13.4 | -9.7 | -1.8 | +0.3 | -2.2 | 1327 |
| 120 | Central Michigan | Mid-American | -13.9 | -7.2 | -4.9 | -0.2 | -1.6 | 1375 |
| 121 | Southern Miss | Sun Belt | -14.0 | -7.5 | -3.4 | -1.0 | -2.1 | 1331 |
| 122 | Florida International | Conference USA | -15.0 | -10.0 | -1.9 | -1.2 | -1.9 | 1353 |
| 123 | New Mexico State | Conference USA | -15.5 | -8.5 | -2.6 | -1.7 | -2.8 | 1275 |
| 124 | San José State | Mountain West | -16.3 | -9.9 | -3.9 | -0.1 | -2.5 | 1303 |
| 125 | Ball State | Mid-American | -16.7 | -5.5 | -7.2 | -1.0 | -3.1 | 1251 |
| 126 | Eastern Michigan | Mid-American | -17.1 | -7.5 | -6.9 | -0.6 | -2.1 | 1330 |
| 127 | Massachusetts | Mid-American | -17.2 | -9.4 | -4.4 | -0.0 | -3.5 | 1219 |
| 128 | Middle Tennessee | Conference USA | -17.3 | -7.1 | -7.3 | +0.1 | -3.0 | 1257 |
| 129 | UL Monroe | Sun Belt | -18.3 | -6.4 | -6.1 | -1.7 | -4.1 | 1168 |
| 130 | Buffalo | Mid-American | -18.3 | -12.6 | -5.5 | +0.6 | -0.8 | 1444 |
| 131 | Bowling Green | Mid-American | -18.7 | -11.6 | -4.1 | -0.1 | -2.9 | 1270 |
| 132 | Northern Illinois | Mountain West | -18.8 | -4.6 | -9.0 | -0.9 | -4.3 | 1149 |
| 133 | Sam Houston | Conference USA | -18.9 | -12.6 | -0.7 | -1.3 | -4.4 | 1145 |
| 134 | Charlotte | American Athletic | -20.2 | -6.9 | -9.1 | -0.5 | -3.7 | 1203 |
| 135 | Sacramento State | Mid-American | -20.5 | -11.0 | -5.3 | +0.1 | -4.3 | 1151 |
| 136 | Kent State | Mid-American | -20.8 | -10.9 | -5.9 | -0.8 | -3.2 | 1241 |
| 137 | Akron | Mid-American | -22.6 | -9.9 | -8.0 | -1.1 | -3.6 | 1205 |
| 138 | UTEP | Mountain West | -24.6 | -12.2 | -6.4 | -1.3 | -4.7 | 1112 |

## Current model fit

- Fitted on 4224 games from seasons 2022–2026.
- Home field on top of the ratings: 3.2 points (1.9 in conference games).
- Extra FBS edge over FCS opponents beyond their ratings: 14.1 points.
- Elo weight: 0.19 points of margin per point of Elo spread.
- Weight on the betting line: 91% for the margin, 80% for the total.
