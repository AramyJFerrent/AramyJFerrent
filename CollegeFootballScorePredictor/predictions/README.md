# College football score predictions

Updated Sat Oct 31, 2026 05:51 PM ET. Refreshed automatically every day of the season and several times on Saturdays; each game's prediction is locked at kickoff and graded once the final score is in. Scores are the most likely real scoreline near the expected points; ranges cover 80% of simulated outcomes for each team. College scores scatter widely, so read the ranges, not just the headline score.

Expected points blend the model with the betting line using the weight that has predicted best in recent seasons (see Current model fit). The spread and total columns show the model's own numbers next to the line, so you can see where it disagrees. Games without a line yet use the model alone.

The fair moneyline is the American odds that match the win chance exactly, with no bookmaker margin: -200 means risk $200 to win $100, +200 means risk $100 to win $200. A sportsbook's price will be a little worse on both sides because of its cut, so a book only offers value on a team when its price beats the fair line.

The edge columns judge each bet by its expected value per $1 staked at the posted price, using the final prediction: the model blended with the line, run through the score simulator, pushes included, and anchored to the market's own chances so that only what the blend moves off the line counts. The model's own spread and total (shown alongside) sit several points from the line in most games, but the blend keeps only the share of that disagreement the model has earned in past seasons, so edges are rare. The side with the higher value is shown when it reaches 3% (+3 cents per $1), as the team or side, the price, the expected value, its chance of winning the bet and its stake, a 25% share of the Kelly stake in units of 1% of the bankroll with at most 3 units on one game; anything short is no edge. Where a book posts no price for a spread or total it is assumed to be -110 and marked -110*; moneylines are never assumed. In the walk-forward backtest against closing lines, edges returned spread -100.0% on 1 bets (posted prices, 2016–2019); spread -3.9% on 156 bets (assumed -110 prices, 2016–2025); moneyline +13.7% on 575 bets (posted prices, 2016–2025); total +2.6% on 367 bets (posted prices, 2016–2019); total -5.7% on 172 bets (assumed -110 prices, 2016–2025). None of these is clearly above zero, so treat these edges as an experiment, not a betting system. The live record is tracked below, graded at the price logged with the last prediction before kickoff.

## 2026 Week 9

| Kickoff (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected points | 80% range | Spread: model / line | Total: model / line | Spread edge | Moneyline edge | Total edge | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sat 10/31 6:30 PM | App State @ Georgia Southern | App State 24, Georgia Southern 31 | Georgia Southern 63% | App State +170 / Georgia Southern -170 | 25.4 – 30.7 | 13–39 / 17–45 | App State -0.9 / Georgia Southern -6.0 | 57.6 / 55.8 | no edge | no edge | no edge |  |
| Sat 10/31 7:00 PM | Oklahoma State @ Iowa State | Oklahoma State 31, Iowa State 24 | Oklahoma State 70% | Oklahoma State -235 / Iowa State +235 | 33.0 – 24.6 | 17–48 / 11–38 | Iowa State -3.1 / Oklahoma State -9.5 | 55.0 / 58.2 | no edge | Iowa State (+292): EV +5.9%, 27%, stake 0.5u | no edge |  |
| Sat 10/31 7:00 PM | Clemson @ Florida State | Clemson 24, Florida State 27 | Florida State 65% | Clemson +185 / Florida State -185 | 22.1 – 28.0 | 10–35 / 14–42 | Florida State -4.9 / Florida State -6.0 | 51.2 / 50.0 | no edge | no edge | no edge |  |
| Sat 10/31 7:00 PM | Washington State @ San Diego State | Washington State 21, San Diego State 24 | San Diego State 56% | Washington State +130 / San Diego State -130 | 22.6 – 25.1 | 10–35 / 12–38 | San Diego State -2.7 / San Diego State -2.5 | 47.4 / 47.8 | no edge | no edge | no edge |  |
| Sat 10/31 7:30 PM | Mississippi State @ Texas | Mississippi State 14, Texas 35 | Texas 91% | Mississippi State +1005 / Texas -1005 | 15.5 – 35.2 | 5–27 / 20–51 | Texas -11.5 / Texas -20.5 | 51.3 / 50.5 | no edge | Mississippi State (+824): EV +4.5%, 11%, stake 0.1u | no edge |  |
| Sat 10/31 7:30 PM | Georgia Tech @ Pittsburgh | Georgia Tech 24, Pittsburgh 31 | Pittsburgh 69% | Georgia Tech +225 / Pittsburgh -225 | 23.4 – 31.1 | 10–38 / 17–46 | Pittsburgh -9.8 / Pittsburgh -7.5 | 54.8 / 54.5 | no edge | no edge | no edge |  |
| Sat 10/31 7:30 PM | Miami @ North Carolina | Miami 34, North Carolina 17 | Miami 84% | Miami -515 / North Carolina +515 | 34.1 – 19.6 | 20–49 / 7–33 | Miami -20.2 / Miami -14.0 | 54.6 / 53.5 | no edge | no edge | no edge |  |
| Sat 10/31 7:30 PM | Ohio State @ USC | Ohio State 31, USC 24 | Ohio State 67% | Ohio State -205 / USC +205 | 29.3 – 22.5 | 14–44 / 10–36 | Ohio State -12.1 / Ohio State -6.2 | 55.9 / 50.8 | no edge | no edge | no edge |  |
| Sat 10/31 7:45 PM | Missouri @ Arkansas | Missouri 27, Arkansas 20 | Missouri 76% | Missouri -325 / Arkansas +325 | 29.4 – 19.2 | 16–44 / 7–31 | Missouri -12.4 / Missouri -10.0 | 49.3 / 48.5 | no edge | no edge | no edge |  |
| Sat 10/31 8:00 PM | Washington @ Nebraska | Washington 21, Nebraska 28 | Nebraska 71% | Washington +240 / Nebraska -240 | 20.9 – 28.7 | 9–34 / 14–42 | Nebraska -8.6 / Nebraska -7.8 | 48.9 / 49.8 | no edge | no edge | no edge |  |
| Sat 10/31 8:00 PM | Army @ Memphis | Army 24, Memphis 31 | Memphis 65% | Army +185 / Memphis -185 | 26.7 – 32.7 | 13–41 / 17–48 | Memphis -5.4 / Memphis -6.0 | 60.2 / 59.2 | no edge | no edge | no edge |  |
| Sat 10/31 10:00 PM | Texas State @ Boise State | Texas State 28, Boise State 38 | Boise State 76% | Texas State +310 / Boise State -310 | 26.3 – 37.2 | 13–41 / 22–52 | Boise State -12.3 / Boise State -10.8 | 63.5 / 63.5 | no edge | no edge | no edge |  |
| Sat 10/31 10:30 PM | Northern Illinois @ UNLV | Northern Illinois 17, UNLV 38 | UNLV 93% | Northern Illinois +1360 / UNLV -1360 | 16.5 – 38.3 | 6–28 / 23–55 | UNLV -17.3 / UNLV -22.2 | 53.5 / 55.0 | no edge | no edge | no edge |  |
| Sat 10/31 11:00 PM | Oregon State @ Fresno State | Oregon State 31, Fresno State 28 | Oregon State 66% | Oregon State -190 / Fresno State +190 | 31.7 – 25.9 | 17–47 / 13–41 | Oregon State -3.7 / Oregon State -6.0 | 56.1 / 58.0 | no edge | no edge | no edge |  |

## 2026 Week 10

| Kickoff (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected points | 80% range | Spread: model / line | Total: model / line | Spread edge | Moneyline edge | Total edge | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tue 11/03 7:00 PM | Ohio @ Akron | Ohio 34, Akron 17 | Ohio 90% | Ohio -900 / Akron +900 | 34.2 – 15.7 | 20–49 / 6–28 | Ohio -18.5 / – | 49.8 / – | no line yet | no line yet (fair: Ohio -900) | no line yet |  |
| Tue 11/03 8:00 PM | Buffalo @ Miami (OH) | Buffalo 17, Miami (OH) 31 | Miami (OH) 80% | Buffalo +400 / Miami (OH) -400 | 17.6 – 30.2 | 7–30 / 16–45 | Miami (OH) -12.5 / – | 48.4 / – | no line yet | no line yet (fair: Miami (OH) -400) | no line yet |  |
| Wed 11/04 7:00 PM | Ball State @ Massachusetts | Ball State 24, Massachusetts 27 | Massachusetts 57% | Ball State +135 / Massachusetts -135 | 23.0 – 26.0 | 10–37 / 13–41 | Massachusetts -3.0 / – | 49.0 / – | no line yet | no line yet (fair: Massachusetts -135) | no line yet |  |
| Wed 11/04 7:00 PM | Toledo @ Sacramento State | Toledo 34, Sacramento State 17 | Toledo 89% | Toledo -810 / Sacramento State +810 | 33.9 – 16.1 | 19–49 / 6–28 | Toledo -17.7 / – | 50.0 / – | no line yet | no line yet (fair: Toledo -810) | no line yet |  |
| Wed 11/04 7:30 PM | Central Michigan vs Eastern Michigan | Central Michigan 27, Eastern Michigan 24 | Central Michigan 60% | Central Michigan -145 / Eastern Michigan +145 | 26.6 – 23.0 | 13–41 / 10–36 | Central Michigan -3.7 / – | 49.6 / – | no line yet | no line yet (fair: Central Michigan -145) | no line yet | neutral site |
| Thu 11/05 7:30 PM | UTSA @ Florida Atlantic | UTSA 34, Florida Atlantic 31 | UTSA 57% | UTSA -130 / Florida Atlantic +130 | 34.4 – 31.8 | 20–49 / 17–46 | UTSA -2.6 / – | 66.2 / – | no line yet | no line yet (fair: UTSA -130) | no line yet |  |
| Thu 11/05 8:00 PM | James Madison @ Southern Miss | James Madison 34, Southern Miss 17 | James Madison 84% | James Madison -525 / Southern Miss +525 | 34.6 – 19.3 | 20–49 / 7–32 | James Madison -15.3 / – | 53.9 / – | no line yet | no line yet (fair: James Madison -525) | no line yet |  |
| Fri 11/06 7:00 PM | Virginia Tech @ SMU | Virginia Tech 24, SMU 31 | SMU 69% | Virginia Tech +220 / SMU -220 | 24.6 – 32.4 | 12–38 / 17–48 | SMU -11.3 / SMU -7.5 | 54.9 / 57.5 | no edge | no edge | no edge |  |
| Fri 11/06 7:30 PM | South Florida @ East Carolina | South Florida 27, East Carolina 24 | South Florida 51% | South Florida -105 / East Carolina +105 | 24.4 – 23.7 | 10–38 / 10–38 | South Florida -0.7 / – | 48.1 / – | no line yet | no line yet (fair: South Florida -105) | no line yet |  |
| Fri 11/06 8:00 PM | Nebraska @ Illinois | Nebraska 31, Illinois 24 | Nebraska 69% | Nebraska -225 / Illinois +225 | 30.6 – 23.1 | 17–45 / 10–37 | Nebraska -7.5 / – | 53.8 / – | no line yet | no line yet (fair: Nebraska -225) | no line yet |  |
| Fri 11/06 9:00 PM | New Mexico @ Nevada | New Mexico 27, Nevada 17 | New Mexico 74% | New Mexico -280 / Nevada +280 | 27.1 – 17.5 | 13–41 / 7–30 | New Mexico -9.6 / – | 44.6 / – | no line yet | no line yet (fair: New Mexico -280) | no line yet |  |
| Fri 11/06 10:15 PM | TCU @ Arizona | TCU 20, Arizona 27 | Arizona 73% | TCU +270 / Arizona -270 | 20.4 – 29.4 | 7–34 / 14–44 | Arizona -9.0 / – | 49.8 / – | no line yet | no line yet (fair: Arizona -270) | no line yet |  |
| Sat 11/07 TBA | UCF @ Kansas | UCF 24, Kansas 31 | Kansas 69% | UCF +220 / Kansas -220 | 22.6 – 30.0 | 10–36 / 16–45 | Kansas -7.4 / – | 52.5 / – | no line yet | no line yet (fair: Kansas -220) | no line yet |  |
| Sat 11/07 TBA | Cincinnati @ Houston | Cincinnati 28, Houston 31 | Houston 60% | Cincinnati +150 / Houston -150 | 28.9 – 33.2 | 14–43 / 19–48 | Houston -4.3 / – | 62.1 / – | no line yet | no line yet (fair: Houston -150) | no line yet |  |
| Sat 11/07 TBA | Iowa State @ Baylor | Iowa State 24, Baylor 27 | Baylor 64% | Iowa State +180 / Baylor -180 | 22.6 – 28.0 | 10–36 / 14–42 | Baylor -5.4 / – | 50.5 / – | no line yet | no line yet (fair: Baylor -180) | no line yet |  |
| Sat 11/07 TBA | Oklahoma State @ Kansas State | Oklahoma State 24, Kansas State 31 | Kansas State 66% | Oklahoma State +195 / Kansas State -195 | 26.0 – 32.4 | 13–40 / 17–48 | Kansas State -6.3 / – | 58.4 / – | no line yet | no line yet (fair: Kansas State -195) | no line yet |  |
| Sat 11/07 TBA | West Virginia @ Texas Tech | West Virginia 17, Texas Tech 38 | Texas Tech 93% | West Virginia +1255 / Texas Tech -1255 | 17.7 – 39.0 | 7–31 / 24–55 | Texas Tech -21.3 / – | 56.7 / – | no line yet | no line yet (fair: Texas Tech -1255) | no line yet |  |
| Sat 11/07 TBA | Michigan State @ Michigan | Michigan State 10, Michigan 24 | Michigan 86% | Michigan State +620 / Michigan -620 | 12.7 – 27.3 | 3–24 / 14–42 | Michigan -21.0 / Michigan -14.0 | 42.2 / 39.5 | no edge | no edge | no edge |  |
| Sat 11/07 TBA | UCLA @ Minnesota | UCLA 24, Minnesota 17 | UCLA 69% | UCLA -225 / Minnesota +225 | 24.6 – 17.8 | 12–38 / 7–30 | UCLA -9.6 / UCLA -6.5 | 41.7 / 42.5 | no edge | no edge | no edge |  |
| Sat 11/07 TBA | Iowa @ Northwestern | Iowa 21, Northwestern 24 | Northwestern 57% | Iowa +135 / Northwestern -135 | 20.6 – 23.0 | 9–34 / 10–37 | Northwestern -1.2 / Northwestern -2.5 | 48.5 / 42.5 | no edge | no edge | no edge |  |
| Sat 11/07 TBA | Penn State @ Washington | Penn State 24, Washington 21 | Washington 50% | Penn State +100 / Washington -100 | 23.5 – 23.2 | 10–37 / 10–37 | Penn State -0.3 / – | 46.7 / – | no line yet | no line yet (fair: Washington -100) | no line yet |  |
| Sat 11/07 12:00 PM | Texas @ Missouri | Texas 27, Missouri 24 | Texas 58% | Texas -140 / Missouri +140 | 25.9 – 22.6 | 13–40 / 10–37 | Texas -1.0 / Texas -3.5 | 44.7 / 49.5 | no edge | no edge | no edge |  |
| Sat 11/07 12:00 PM | BYU @ Utah | BYU 24, Utah 27 | Utah 59% | BYU +145 / Utah -145 | 23.0 – 26.3 | 10–37 / 13–41 | Utah -6.4 / Utah -3.0 | 52.7 / 48.5 | no edge | no edge | no edge |  |
| Sat 11/07 12:00 PM | Clemson @ Syracuse | Clemson 27, Syracuse 24 | Clemson 51% | Clemson -105 / Syracuse +105 | 24.3 – 23.9 | 10–38 / 10–38 | Clemson -0.4 / – | 48.3 / – | no line yet | no line yet (fair: Clemson -105) | no line yet |  |
| Sat 11/07 12:00 PM | Florida State @ Boston College | Florida State 31, Boston College 21 | Florida State 75% | Florida State -300 / Boston College +300 | 30.9 – 21.0 | 17–45 / 7–34 | Florida State -9.9 / – | 54.1 / – | no line yet | no line yet (fair: Florida State -300) | no line yet |  |
| Sat 11/07 12:00 PM | North Carolina @ UConn | North Carolina 27, UConn 24 | North Carolina 51% | North Carolina -105 / UConn +105 | 27.3 – 27.0 | 14–42 / 14–42 | North Carolina -0.3 / – | 55.8 / – | no line yet | no line yet (fair: North Carolina -105) | no line yet |  |
| Sat 11/07 12:00 PM | Tulsa @ Tulane | Tulsa 24, Tulane 27 | Tulane 56% | Tulsa +125 / Tulane -125 | 25.0 – 27.4 | 13–38 / 14–42 | Tulane -2.4 / – | 52.4 / – | no line yet | no line yet (fair: Tulane -125) | no line yet |  |
| Sat 11/07 12:30 PM | Duke @ NC State | Duke 27, NC State 24 | Duke 57% | Duke -130 / NC State +130 | 29.2 – 26.7 | 16–44 / 13–41 | Duke -2.4 / – | 55.9 / – | no line yet | no line yet (fair: Duke -130) | no line yet |  |
| Sat 11/07 12:30 PM | Maryland @ Purdue | Maryland 24, Purdue 27 | Purdue 58% | Maryland +135 / Purdue -135 | 24.7 – 27.4 | 10–38 / 14–42 | Purdue -2.7 / – | 52.2 / – | no line yet | no line yet (fair: Purdue -135) | no line yet |  |
| Sat 11/07 12:30 PM | Rutgers @ Wisconsin | Rutgers 17, Wisconsin 31 | Wisconsin 83% | Rutgers +490 / Wisconsin -490 | 17.9 – 31.9 | 7–31 / 17–47 | Wisconsin -13.9 / – | 49.8 / – | no line yet | no line yet (fair: Wisconsin -490) | no line yet |  |
| Sat 11/07 12:45 PM | Arkansas @ Auburn | Arkansas 17, Auburn 34 | Auburn 84% | Arkansas +525 / Auburn -525 | 18.9 – 33.7 | 7–31 / 19–49 | Auburn -14.8 / – | 52.7 / – | no line yet | no line yet (fair: Auburn -525) | no line yet |  |
| Sat 11/07 1:00 PM | Old Dominion @ Coastal Carolina | Old Dominion 17, Coastal Carolina 24 | Coastal Carolina 63% | Old Dominion +175 / Coastal Carolina -175 | 19.6 – 24.5 | 7–32 / 10–38 | Coastal Carolina -4.9 / – | 44.4 / – | no line yet | no line yet (fair: Coastal Carolina -175) | no line yet |  |
| Sat 11/07 2:30 PM | Georgia State @ App State | Georgia State 28, App State 31 | App State 61% | Georgia State +155 / App State -155 | 27.5 – 31.6 | 14–42 / 17–46 | App State -4.1 / – | 59.2 / – | no line yet | no line yet (fair: App State -155) | no line yet |  |
| Sat 11/07 3:00 PM | Texas A&M @ South Carolina | Texas A&M 27, South Carolina 24 | Texas A&M 50% | Texas A&M -100 / South Carolina +100 | 24.6 – 24.4 | 12–38 / 10–38 | Texas A&M -0.2 / – | 49.0 / – | no line yet | no line yet (fair: Texas A&M -100) | no line yet |  |
| Sat 11/07 3:00 PM | UL Monroe @ Arkansas State | UL Monroe 21, Arkansas State 31 | Arkansas State 79% | UL Monroe +380 / Arkansas State -380 | 20.4 – 32.6 | 7–34 / 17–48 | Arkansas State -12.2 / – | 53.0 / – | no line yet | no line yet (fair: Arkansas State -380) | no line yet |  |
| Sat 11/07 3:00 PM | Delaware @ Kennesaw State | Delaware 31, Kennesaw State 24 | Delaware 62% | Delaware -165 / Kennesaw State +165 | 30.1 – 25.1 | 16–45 / 12–39 | Delaware -5.0 / – | 55.1 / – | no line yet | no line yet (fair: Delaware -165) | no line yet |  |
| Sat 11/07 3:30 PM | Alabama @ LSU | Alabama 24, LSU 27 | LSU 63% | Alabama +170 / LSU -170 | 23.6 – 28.5 | 10–37 / 14–43 | LSU -9.2 / LSU -4.5 | 50.1 / 52.5 | no edge | no edge | no edge |  |
| Sat 11/07 3:30 PM | Merrimack @ Wake Forest | Merrimack 3, Wake Forest 59 | Wake Forest 100% | Merrimack +9900 / Wake Forest -9900 | 3.0 – 59.2 | 0–7 / 45–73 | Wake Forest -56.2 / – | 62.2 / – | no line yet | no line yet (fair: Wake Forest -9900) | no line yet | FCS opponent |
| Sat 11/07 3:30 PM | Oregon @ Ohio State | Oregon 17, Ohio State 31 | Ohio State 84% | Oregon +510 / Ohio State -510 | 16.0 – 30.0 | 6–28 / 16–45 | Ohio State -13.7 / Ohio State -14.0 | 48.3 / 45.5 | no edge | no edge | no edge |  |
| Sat 11/07 3:30 PM | Charlotte @ UAB | Charlotte 17, UAB 31 | UAB 81% | Charlotte +430 / UAB -430 | 18.5 – 31.3 | 7–31 / 17–46 | UAB -12.8 / – | 49.8 / – | no line yet | no line yet (fair: UAB -430) | no line yet |  |
| Sat 11/07 3:30 PM | Temple @ Navy | Temple 24, Navy 34 | Navy 76% | Temple +315 / Navy -315 | 22.8 – 33.5 | 10–37 / 20–49 | Navy -10.7 / – | 56.3 / – | no line yet | no line yet (fair: Navy -315) | no line yet |  |
| Sat 11/07 3:30 PM | Marshall @ Georgia Southern | Marshall 31, Georgia Southern 28 | Marshall 53% | Marshall -115 / Georgia Southern +115 | 29.7 – 28.3 | 16–44 / 14–42 | Marshall -1.4 / – | 58.1 / – | no line yet | no line yet (fair: Marshall -115) | no line yet |  |
| Sat 11/07 3:30 PM | Western Kentucky @ Middle Tennessee | Western Kentucky 27, Middle Tennessee 24 | Western Kentucky 55% | Western Kentucky -125 / Middle Tennessee +125 | 26.2 – 24.2 | 13–41 / 10–38 | Western Kentucky -2.0 / – | 50.4 / – | no line yet | no line yet (fair: Western Kentucky -125) | no line yet |  |
| Sat 11/07 4:00 PM | Rice @ North Texas | Rice 21, North Texas 38 | North Texas 89% | Rice +775 / North Texas -775 | 21.3 – 40.3 | 9–35 / 24–56 | North Texas -19.0 / – | 63.1 / – | no line yet | no line yet (fair: North Texas -775) | no line yet |  |
| Sat 11/07 4:00 PM | Northern Illinois @ San José State | Northern Illinois 24, San José State 31 | San José State 66% | Northern Illinois +190 / San José State -190 | 23.5 – 29.5 | 10–37 / 16–44 | San José State -6.0 / – | 52.9 / – | no line yet | no line yet (fair: San José State -190) | no line yet |  |
| Sat 11/07 4:00 PM | Missouri State @ Florida International | Missouri State 24, Florida International 27 | Florida International 60% | Missouri State +150 / Florida International -150 | 23.4 – 26.7 | 10–37 / 14–41 | Florida International -3.3 / – | 50.8 / – | no line yet | no line yet (fair: Florida International -150) | no line yet |  |
| Sat 11/07 4:00 PM | Louisiana Tech @ Troy | Louisiana Tech 24, Troy 21 | Louisiana Tech 65% | Louisiana Tech -185 / Troy +185 | 26.3 – 20.7 | 13–41 / 7–34 | Louisiana Tech -5.7 / – | 47.0 / – | no line yet | no line yet (fair: Louisiana Tech -185) | no line yet |  |
| Sat 11/07 4:15 PM | Vanderbilt @ Mississippi State | Vanderbilt 24, Mississippi State 31 | Mississippi State 70% | Vanderbilt +240 / Mississippi State -240 | 24.5 – 32.4 | 10–38 / 17–48 | Mississippi State -7.9 / – | 56.9 / – | no line yet | no line yet (fair: Mississippi State -240) | no line yet |  |
| Sat 11/07 5:00 PM | South Alabama @ Louisiana | South Alabama 28, Louisiana 31 | Louisiana 59% | South Alabama +145 / Louisiana -145 | 27.5 – 31.1 | 14–42 / 17–45 | Louisiana -3.6 / – | 58.6 / – | no line yet | no line yet (fair: Louisiana -145) | no line yet |  |
| Sat 11/07 6:00 PM | Boise State @ Colorado State | Boise State 38, Colorado State 24 | Boise State 84% | Boise State -510 / Colorado State +510 | 39.0 – 23.9 | 24–55 / 10–38 | Boise State -15.1 / – | 62.9 / – | no line yet | no line yet (fair: Boise State -510) | no line yet |  |
| Sat 11/07 6:15 PM | Kentucky @ Tennessee | Kentucky 24, Tennessee 27 | Tennessee 65% | Kentucky +180 / Tennessee -180 | 22.1 – 27.9 | 10–35 / 14–42 | Tennessee -8.7 / Tennessee -5.5 | 48.3 / 50.5 | no edge | no edge | no edge |  |
| Sat 11/07 7:00 PM | Sam Houston @ Jacksonville State | Sam Houston 14, Jacksonville State 31 | Jacksonville State 90% | Sam Houston +920 / Jacksonville State -920 | 13.7 – 31.6 | 3–24 / 17–48 | Jacksonville State -17.9 / – | 45.3 / – | no line yet | no line yet (fair: Jacksonville State -920) | no line yet |  |
| Sat 11/07 7:30 PM | Georgia @ Ole Miss | Georgia 31, Ole Miss 28 | Georgia 56% | Georgia -125 / Ole Miss +125 | 29.6 – 26.6 | 15–45 / 14–41 | Georgia -2.7 / Georgia -3.0 | 55.0 / 56.5 | no edge | no edge | no edge |  |
| Sat 11/07 7:30 PM | Colorado @ Arizona State | Colorado 24, Arizona State 31 | Arizona State 65% | Colorado +190 / Arizona State -190 | 22.0 – 28.3 | 10–35 / 14–42 | Arizona State -6.3 / – | 50.2 / – | no line yet | no line yet (fair: Arizona State -190) | no line yet |  |
| Sat 11/07 7:30 PM | Louisville @ Georgia Tech | Louisville 38, Georgia Tech 21 | Louisville 86% | Louisville -630 / Georgia Tech +630 | 37.2 – 20.9 | 22–52 / 7–34 | Louisville -16.3 / – | 58.1 / – | no line yet | no line yet (fair: Louisville -630) | no line yet |  |
| Sat 11/07 7:30 PM | Miami @ Notre Dame | Miami 24, Notre Dame 27 | Notre Dame 61% | Miami +155 / Notre Dame -155 | 25.7 – 29.2 | 13–40 / 15–44 | Notre Dame -3.9 / Notre Dame -3.5 | 52.2 / 55.5 | no edge | no edge | no edge |  |
| Sat 11/07 7:30 PM | Air Force @ Army | Air Force 24, Army 27 | Army 64% | Air Force +180 / Army -180 | 23.3 – 28.9 | 10–37 / 14–44 | Army -6.4 / Army -5.5 | 59.5 / 50.5 | no edge | no edge | Over 50.5 (-110*): EV +4.8%, 55%, stake 1.3u | * price not posted; assumed -110 |
| Sat 11/07 7:45 PM | Oklahoma @ Florida | Oklahoma 24, Florida 27 | Florida 60% | Oklahoma +155 / Florida -155 | 22.2 – 25.8 | 10–35 / 13–40 | Oklahoma -0.5 / Florida -4.0 | 46.4 / 48.5 | no edge | no edge | no edge |  |
| Sat 11/07 8:00 PM | Liberty @ New Mexico State | Liberty 31, New Mexico State 17 | Liberty 83% | Liberty -490 / New Mexico State +490 | 30.5 – 16.9 | 16–45 / 6–30 | Liberty -13.6 / – | 47.4 / – | no line yet | no line yet (fair: Liberty -490) | no line yet |  |
| Sat 11/07 9:30 PM | Fresno State @ Utah State | Fresno State 24, Utah State 21 | Fresno State 61% | Fresno State -155 / Utah State +155 | 25.3 – 21.4 | 13–38 / 10–35 | Fresno State -4.0 / – | 46.7 / – | no line yet | no line yet (fair: Fresno State -155) | no line yet |  |
| Sat 11/07 9:30 PM | Hawai'i @ UTEP | Hawai'i 31, UTEP 17 | Hawai'i 80% | Hawai'i -405 / UTEP +405 | 31.0 – 18.8 | 17–46 / 7–31 | Hawai'i -12.2 / – | 49.8 / – | no line yet | no line yet (fair: Hawai'i -405) | no line yet |  |
| Sat 11/07 10:30 PM | Texas State @ Oregon State | Texas State 31, Oregon State 38 | Oregon State 69% | Texas State +225 / Oregon State -225 | 29.6 – 37.5 | 15–44 / 22–52 | Oregon State -8.0 / – | 67.1 / – | no line yet | no line yet (fair: Oregon State -225) | no line yet |  |
| Sat 11/07 10:30 PM | Wyoming @ UNLV | Wyoming 20, UNLV 28 | UNLV 72% | Wyoming +260 / UNLV -260 | 20.1 – 29.0 | 7–34 / 14–44 | UNLV -8.9 / – | 49.1 / – | no line yet | no line yet (fair: UNLV -260) | no line yet |  |

## How the 2026 predictions have done

| Predictor | Games | Margin MAE | Total MAE | Team-score MAE | Winners | Brier | 80% range hit |
|---|---|---|---|---|---|---|---|
| Final prediction | 586 | 11.67 | 12.16 | 8.42 | 80.2% | 0.139 | 82.3% |
| Model only (before blending) | 586 | 12.41 | 12.50 | 8.70 | 77.6% | – | – |
| Betting line when predicted | 584 | 11.66 | 12.12 | 8.41 | 80.1% | – | – |

MAE is mean absolute error in points (lower is better). Brier scores the win chances (lower is better, 0.25 is a coin flip). Even the closing betting line misses the final margin of an FBS game by about 12.5 points.

501 of these games were played before the predictor went live. They are backfilled walk-forward (each week predicted from earlier weeks only) but with closing lines, so they flatter the model slightly. Every game since is graded on the prediction logged before kickoff.

### Betting edges

| Market | Edges | Record (W-L-P) | Staked | Units won | ROI | Expected ROI |
|---|---|---|---|---|---|---|
| Spread | 0 | 0-0-0 | 0.0 | +0.00 | – | – |
| Moneyline | 2 | 0-2-0 | 0.7 | -0.68 | -100.0% | +5.8% |
| Total | 1 | 0-1-0 | 1.4 | -1.45 | -100.0% | +5.3% |

1 of these edges were priced at an assumed -110 (price not posted).

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

## FBS power ratings

Points per game better than an average FBS team on a neutral field, from opponent-adjusted EPA (garbage time removed) with this season's games weighted against a preseason prior, plus the weight the margin model puts on Elo (a rating built from game results alone). Defense is positive when it holds opponents below average.

| # | Team | Conference | Net | Offense | Defense | Special teams | Results (Elo) | Elo rating |
|---|---|---|---|---|---|---|---|---|
| 1 | Ohio State | Big Ten | +27.0 | +11.2 | +10.3 | +0.4 | +5.1 | 1934 |
| 2 | LSU | SEC | +26.3 | +10.7 | +12.5 | +0.2 | +2.9 | 1751 |
| 3 | Miami | ACC | +24.0 | +13.2 | +6.1 | +0.2 | +4.6 | 1890 |
| 4 | Georgia | SEC | +23.2 | +9.5 | +8.5 | +0.8 | +4.3 | 1866 |
| 5 | Notre Dame | FBS Independents | +23.1 | +8.9 | +9.0 | +1.1 | +4.2 | 1858 |
| 6 | Indiana | Big Ten | +22.0 | +6.0 | +10.4 | +0.4 | +5.1 | 1935 |
| 7 | Alabama | SEC | +19.5 | +8.8 | +7.2 | +0.3 | +3.2 | 1777 |
| 8 | Texas | SEC | +18.7 | +2.9 | +11.8 | +0.5 | +3.5 | 1803 |
| 9 | Utah | Big 12 | +18.4 | +8.9 | +5.8 | +0.0 | +3.7 | 1819 |
| 10 | Texas Tech | Big 12 | +18.3 | +2.1 | +11.9 | +1.2 | +3.0 | 1761 |
| 11 | Ole Miss | SEC | +18.1 | +9.6 | +4.1 | +0.7 | +3.7 | 1815 |
| 12 | Oklahoma | SEC | +17.4 | +1.4 | +13.4 | +0.6 | +2.0 | 1677 |
| 13 | UCLA | Big Ten | +16.1 | +5.3 | +8.3 | +0.6 | +1.9 | 1668 |
| 14 | Oregon | Big Ten | +15.9 | +3.3 | +9.7 | +0.3 | +2.6 | 1722 |
| 15 | Tennessee | SEC | +15.3 | +3.5 | +8.5 | +0.7 | +2.6 | 1723 |
| 16 | Missouri | SEC | +15.1 | +4.1 | +8.4 | +0.5 | +2.1 | 1686 |
| 17 | Louisville | ACC | +15.0 | +8.9 | +4.0 | +0.3 | +1.9 | 1663 |
| 18 | Michigan | Big Ten | +14.9 | +3.4 | +9.4 | +0.0 | +2.0 | 1674 |
| 19 | Wake Forest | ACC | +14.7 | +5.7 | +6.8 | +0.1 | +2.1 | 1688 |
| 20 | Florida | SEC | +14.0 | +9.0 | +3.0 | +1.0 | +1.0 | 1592 |
| 21 | BYU | Big 12 | +14.0 | +6.3 | +4.3 | +0.5 | +2.9 | 1748 |
| 22 | Nebraska | Big Ten | +13.9 | +4.9 | +7.1 | +0.5 | +1.4 | 1622 |
| 23 | SMU | ACC | +13.6 | +7.5 | +3.8 | +0.2 | +2.0 | 1675 |
| 24 | Iowa | Big Ten | +13.1 | +1.7 | +7.7 | +0.8 | +2.9 | 1751 |
| 25 | USC | Big Ten | +12.7 | +10.6 | -0.0 | +0.1 | +2.0 | 1672 |
| 26 | Auburn | SEC | +12.3 | +5.0 | +6.4 | +0.6 | +0.3 | 1536 |
| 27 | Arizona | Big 12 | +12.0 | +6.3 | +3.5 | -0.2 | +2.4 | 1708 |
| 28 | Texas A&M | SEC | +12.0 | +2.6 | +7.7 | +0.6 | +1.1 | 1601 |
| 29 | Northwestern | Big Ten | +11.6 | +6.1 | +2.7 | +1.0 | +1.8 | 1655 |
| 30 | Penn State | Big Ten | +10.7 | +2.7 | +6.5 | +0.4 | +1.0 | 1593 |
| 31 | Kansas State | Big 12 | +10.2 | +5.8 | +3.3 | +0.4 | +0.6 | 1558 |
| 32 | Houston | Big 12 | +10.1 | +7.9 | -0.0 | +0.2 | +2.0 | 1673 |
| 33 | Mississippi State | SEC | +9.8 | +6.8 | +2.3 | +0.4 | +0.2 | 1523 |
| 34 | Kentucky | SEC | +9.5 | +2.8 | +4.5 | +0.3 | +2.0 | 1677 |
| 35 | Baylor | Big 12 | +9.3 | +0.1 | +7.0 | +1.1 | +1.1 | 1601 |
| 36 | South Carolina | SEC | +9.0 | +4.3 | +2.7 | +0.8 | +1.1 | 1599 |
| 37 | Washington | Big Ten | +8.3 | +2.8 | +4.1 | -0.1 | +1.5 | 1635 |
| 38 | Cincinnati | Big 12 | +8.0 | +8.9 | -2.3 | +0.5 | +1.0 | 1592 |
| 39 | Kansas | Big 12 | +8.0 | +5.9 | +2.7 | +0.0 | -0.6 | 1454 |
| 40 | Wisconsin | Big Ten | +7.9 | -0.4 | +7.0 | +0.2 | +1.0 | 1593 |
| 41 | Boise State | Pac-12 | +7.1 | +5.0 | -0.5 | +0.0 | +2.5 | 1717 |
| 42 | Duke | ACC | +7.0 | +2.7 | +1.4 | +0.8 | +2.0 | 1677 |
| 43 | Iowa State | Big 12 | +6.5 | +2.4 | +2.7 | +0.9 | +0.5 | 1552 |
| 44 | Florida State | ACC | +6.3 | +8.0 | -1.4 | -0.1 | -0.1 | 1497 |
| 45 | Oklahoma State | Big 12 | +6.3 | +6.7 | -0.7 | +0.5 | -0.2 | 1495 |
| 46 | Arizona State | Big 12 | +5.2 | +0.9 | +3.6 | +0.2 | +0.6 | 1562 |
| 47 | TCU | Big 12 | +4.9 | -1.6 | +5.3 | +0.5 | +0.8 | 1572 |
| 48 | Virginia Tech | ACC | +4.7 | +3.0 | +0.7 | +0.3 | +0.7 | 1566 |
| 49 | Illinois | Big Ten | +4.6 | +6.0 | -2.5 | -0.1 | +1.2 | 1610 |
| 50 | Vanderbilt | SEC | +4.5 | +4.5 | -0.6 | +0.3 | +0.2 | 1529 |
| 51 | Minnesota | Big Ten | +3.9 | -3.7 | +6.2 | +0.7 | +0.7 | 1565 |
| 52 | North Texas | American Athletic | +3.5 | +10.2 | -7.4 | -0.8 | +1.6 | 1645 |
| 53 | NC State | ACC | +3.5 | +5.8 | -2.0 | -0.6 | +0.4 | 1538 |
| 54 | Clemson | ACC | +3.4 | -4.8 | +7.0 | +0.4 | +0.8 | 1578 |
| 55 | Pittsburgh | ACC | +3.3 | -0.2 | +2.5 | +0.5 | +0.4 | 1542 |
| 56 | UCF | Big 12 | +3.0 | +0.6 | +3.0 | +0.0 | -0.6 | 1459 |
| 57 | Oregon State | Pac-12 | +2.7 | +5.0 | -2.3 | +0.1 | -0.1 | 1498 |
| 58 | Virginia | ACC | +2.6 | -0.9 | +3.6 | -0.2 | +0.1 | 1517 |
| 59 | Colorado | Big 12 | +2.4 | +0.3 | +4.7 | -0.8 | -1.9 | 1346 |
| 60 | UTSA | American Athletic | +2.2 | +3.0 | -2.8 | -0.1 | +2.1 | 1686 |
| 61 | James Madison | Sun Belt | +1.8 | -2.0 | +1.1 | +0.4 | +2.3 | 1698 |
| 62 | Syracuse | ACC | +1.8 | +1.6 | +2.2 | -0.9 | -1.2 | 1407 |
| 63 | Purdue | Big Ten | +1.2 | +3.4 | -1.8 | +0.4 | -0.8 | 1444 |
| 64 | Memphis | American Athletic | +1.2 | +2.9 | -2.0 | -0.5 | +0.7 | 1566 |
| 65 | Arkansas | SEC | +1.0 | +1.2 | +0.4 | -0.4 | -0.1 | 1496 |
| 66 | North Carolina | ACC | +0.6 | +0.5 | -0.8 | +0.9 | +0.1 | 1514 |
| 67 | Maryland | Big Ten | +0.4 | -1.6 | +3.1 | +1.0 | -2.1 | 1334 |
| 68 | West Virginia | Big 12 | +0.1 | +4.1 | -4.6 | +0.6 | -0.1 | 1502 |
| 69 | Toledo | Mid-American | -0.1 | -1.3 | +0.7 | -0.0 | +0.6 | 1555 |
| 70 | New Mexico | Mountain West | -0.1 | -2.5 | +1.2 | +0.0 | +1.2 | 1608 |
| 71 | Liberty | Conference USA | -1.0 | -0.3 | -0.9 | -0.1 | +0.2 | 1527 |
| 72 | Navy | American Athletic | -1.2 | +3.6 | -3.8 | -0.5 | -0.4 | 1473 |
| 73 | Texas State | Pac-12 | -1.2 | +5.1 | -5.6 | -1.5 | +0.7 | 1567 |
| 74 | South Florida | American Athletic | -1.3 | -2.4 | -0.1 | +0.3 | +1.0 | 1593 |
| 75 | North Dakota State | Mountain West | -1.5 | -5.2 | +3.6 | +1.2 | -1.2 | 1408 |
| 76 | Army | American Athletic | -2.1 | +4.8 | -8.0 | -0.1 | +1.1 | 1602 |
| 77 | UConn | FBS Independents | -2.3 | +1.5 | -3.5 | -0.3 | -0.0 | 1507 |
| 78 | Fresno State | Pac-12 | -3.4 | -2.5 | -1.2 | -0.1 | +0.4 | 1544 |
| 79 | Ohio | Mid-American | -3.4 | -1.9 | -2.8 | +0.5 | +0.8 | 1578 |
| 80 | Georgia Tech | ACC | -3.5 | +2.8 | -5.2 | -0.0 | -1.1 | 1416 |
| 81 | East Carolina | American Athletic | -3.5 | -4.8 | +2.2 | -0.6 | -0.3 | 1484 |
| 82 | Tulsa | American Athletic | -3.7 | -1.0 | -0.4 | -0.4 | -1.8 | 1358 |
| 83 | Louisiana Tech | Sun Belt | -3.7 | -3.0 | -0.0 | -0.6 | -0.1 | 1500 |
| 84 | Michigan State | Big Ten | -3.7 | -3.6 | +1.2 | +0.1 | -1.4 | 1388 |
| 85 | Florida Atlantic | American Athletic | -3.8 | +3.8 | -7.3 | +0.8 | -1.1 | 1416 |
| 86 | Rutgers | Big Ten | -4.1 | +2.8 | -6.2 | +0.8 | -1.4 | 1388 |
| 87 | Tulane | American Athletic | -4.4 | -3.7 | -1.6 | +0.2 | +0.6 | 1562 |
| 88 | Air Force | Mountain West | -4.6 | +2.6 | -6.2 | -0.3 | -0.7 | 1453 |
| 89 | Jacksonville State | Conference USA | -4.8 | -0.2 | -4.4 | -0.1 | -0.1 | 1497 |
| 90 | UNLV | Mountain West | -4.8 | -3.0 | -2.3 | +0.0 | +0.4 | 1540 |
| 91 | Boston College | ACC | -5.3 | -3.7 | -0.2 | -0.9 | -0.5 | 1469 |
| 92 | California | ACC | -6.4 | -2.3 | -1.9 | -0.5 | -1.7 | 1369 |
| 93 | Delaware | Conference USA | -6.4 | -0.3 | -5.2 | +0.3 | -1.2 | 1406 |
| 94 | Marshall | Sun Belt | -6.7 | -2.1 | -3.8 | -0.2 | -0.6 | 1462 |
| 95 | Western Michigan | Mid-American | -7.0 | -4.9 | -3.5 | +0.8 | +0.6 | 1561 |
| 96 | App State | Sun Belt | -7.2 | -2.8 | -3.5 | -0.2 | -0.7 | 1454 |
| 97 | Miami (OH) | Mid-American | -8.1 | -4.6 | -3.3 | +0.5 | -0.8 | 1446 |
| 98 | Washington State | Pac-12 | -8.2 | -6.9 | +0.6 | -0.2 | -1.6 | 1373 |
| 99 | San Diego State | Pac-12 | -8.4 | -5.2 | -1.9 | +0.2 | -1.5 | 1382 |
| 100 | Georgia State | Sun Belt | -8.5 | +0.5 | -7.4 | -0.4 | -1.3 | 1399 |
| 101 | Utah State | Pac-12 | -8.7 | -7.8 | +1.9 | -1.3 | -1.5 | 1384 |
| 102 | Stanford | ACC | -8.8 | -3.3 | -4.7 | -0.2 | -0.5 | 1465 |
| 103 | Temple | American Athletic | -9.4 | +1.2 | -7.6 | -0.5 | -2.5 | 1303 |
| 104 | Louisiana | Sun Belt | -9.6 | -5.1 | -4.1 | -0.1 | -0.4 | 1478 |
| 105 | Georgia Southern | Sun Belt | -9.7 | -2.1 | -6.2 | -1.0 | -0.3 | 1481 |
| 106 | UAB | American Athletic | -10.0 | -5.9 | -2.4 | -0.4 | -1.2 | 1407 |
| 107 | Arkansas State | Sun Belt | -10.1 | -2.8 | -6.7 | +0.2 | -0.8 | 1441 |
| 108 | Colorado State | Pac-12 | -10.2 | +3.5 | -11.1 | -0.3 | -2.3 | 1313 |
| 109 | South Alabama | Sun Belt | -11.0 | +0.3 | -10.6 | +0.2 | -0.8 | 1438 |
| 110 | Wyoming | Mountain West | -11.1 | -6.5 | -3.3 | -0.2 | -1.1 | 1413 |
| 111 | Troy | Sun Belt | -11.2 | -8.0 | -0.6 | -1.3 | -1.3 | 1401 |
| 112 | Hawai'i | Mountain West | -11.3 | -4.1 | -6.1 | +0.7 | -1.7 | 1365 |
| 113 | Western Kentucky | Conference USA | -12.2 | -6.9 | -3.0 | -0.3 | -2.0 | 1345 |
| 114 | Nevada | Mountain West | -12.6 | -8.7 | -2.2 | +0.4 | -2.1 | 1336 |
| 115 | Kennesaw State | Conference USA | -12.8 | -6.6 | -3.4 | -0.8 | -1.9 | 1346 |
| 116 | Rice | American Athletic | -12.9 | -3.7 | -5.1 | -0.9 | -3.1 | 1246 |
| 117 | Florida International | Conference USA | -13.1 | -9.6 | -1.2 | -0.7 | -1.6 | 1377 |
| 118 | Coastal Carolina | Sun Belt | -13.2 | -5.8 | -5.7 | +0.4 | -2.1 | 1332 |
| 119 | Missouri State | Conference USA | -13.2 | -1.8 | -7.3 | -1.4 | -2.7 | 1281 |
| 120 | Old Dominion | Sun Belt | -13.8 | -13.1 | +2.2 | -1.4 | -1.4 | 1394 |
| 121 | Central Michigan | Mid-American | -13.9 | -7.3 | -4.8 | -0.2 | -1.6 | 1375 |
| 122 | Southern Miss | Sun Belt | -14.2 | -6.8 | -3.4 | -1.4 | -2.5 | 1296 |
| 123 | New Mexico State | Conference USA | -15.5 | -8.6 | -2.4 | -1.7 | -2.8 | 1275 |
| 124 | San José State | Mountain West | -15.8 | -8.9 | -4.3 | -0.3 | -2.4 | 1312 |
| 125 | Ball State | Mid-American | -16.8 | -5.5 | -7.2 | -1.0 | -3.1 | 1251 |
| 126 | Middle Tennessee | Conference USA | -17.1 | -7.2 | -7.0 | +0.1 | -3.0 | 1257 |
| 127 | Eastern Michigan | Mid-American | -17.2 | -7.6 | -6.8 | -0.6 | -2.1 | 1330 |
| 128 | Massachusetts | Mid-American | -17.3 | -9.5 | -4.4 | -0.0 | -3.5 | 1219 |
| 129 | UL Monroe | Sun Belt | -18.2 | -6.6 | -6.5 | -1.4 | -3.7 | 1203 |
| 130 | Buffalo | Mid-American | -18.2 | -12.7 | -5.4 | +0.6 | -0.8 | 1444 |
| 131 | Northern Illinois | Mountain West | -18.7 | -4.6 | -8.8 | -0.9 | -4.3 | 1149 |
| 132 | Bowling Green | Mid-American | -18.7 | -11.7 | -4.1 | -0.1 | -2.9 | 1270 |
| 133 | Sam Houston | Conference USA | -19.1 | -12.8 | -0.7 | -1.3 | -4.4 | 1145 |
| 134 | Charlotte | American Athletic | -20.2 | -7.0 | -9.1 | -0.5 | -3.7 | 1203 |
| 135 | Sacramento State | Mid-American | -20.5 | -11.1 | -5.2 | +0.1 | -4.3 | 1151 |
| 136 | Kent State | Mid-American | -20.8 | -11.0 | -5.9 | -0.8 | -3.2 | 1241 |
| 137 | Akron | Mid-American | -22.8 | -10.0 | -8.0 | -1.2 | -3.6 | 1205 |
| 138 | UTEP | Mountain West | -23.9 | -11.7 | -6.2 | -1.4 | -4.6 | 1123 |

## Current model fit

- Fitted on 4203 games from seasons 2022–2026.
- Home field on top of the ratings: 3.2 points (1.9 in conference games).
- Extra FBS edge over FCS opponents beyond their ratings: 14.1 points.
- Elo weight: 0.19 points of margin per point of Elo spread.
- Weight on the betting line: 91% for the margin, 81% for the total.
