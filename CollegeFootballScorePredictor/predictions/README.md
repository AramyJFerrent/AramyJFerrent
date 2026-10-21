# College football score predictions

Updated Wed Oct 21, 2026 02:13 PM ET. Refreshed automatically every day of the season and several times on Saturdays; each game's prediction is locked at kickoff and graded once the final score is in. Scores are the most likely real scoreline near the expected points; ranges cover 80% of simulated outcomes for each team. College scores scatter widely, so read the ranges, not just the headline score.

Expected points blend the model with the betting line using the weight that has predicted best in recent seasons (see Current model fit). The spread and total columns show the model's own numbers next to the line, so you can see where it disagrees. Games without a line yet use the model alone.

The fair moneyline is the American odds that match the win chance exactly, with no bookmaker margin: -200 means risk $200 to win $100, +200 means risk $100 to win $200. A sportsbook's price will be a little worse on both sides because of its cut, so a book only offers value on a team when its price beats the fair line.

The edge columns judge each bet by its expected value per $1 staked at the posted price, using the model's own numbers before any blending with the line (its spread, total and win chance run through the same score simulator, pushes included). The side with the higher value is shown when it reaches 3% (+3 cents per $1), as the team or side, the price, the expected value and the model's chance of winning the bet; anything short is no edge. Where a book posts no price for a spread or total it is assumed to be -110 and marked -110*; moneylines are never assumed. In the walk-forward backtest against closing lines, model-only edges returned spread -5.6% on 2089 bets (posted prices, 2016–2019); spread -4.2% on 4069 bets (assumed -110 prices, 2016–2025); moneyline +7.5% on 4463 bets (posted prices, 2016–2025); total -1.7% on 2367 bets (posted prices, 2016–2019); total +0.8% on 3693 bets (assumed -110 prices, 2016–2025). None of these is clearly above zero, so treat these edges as an experiment, not a betting system. The live record is tracked below, graded at the price logged with the last prediction before kickoff.

## 2026 Week 8

| Kickoff (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected points | 80% range | Spread: model / line | Total: model / line | Spread edge | Moneyline edge | Total edge | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Wed 10/21 8:00 PM | New Mexico State @ Sam Houston | New Mexico State 24, Sam Houston 21 | New Mexico State 58% | New Mexico State -135 / Sam Houston +135 | 24.4 – 21.7 | 10–38 / 10–35 | New Mexico State -1.0 / New Mexico State -3.0 | 43.9 / 46.8 | Sam Houston +3.0 (-110*): EV +7.9%, model 53% | Sam Houston (+125): EV +8.6%, model 48% | Under 46.75 (-110*): EV +12.5%, model 59% | * price not posted; assumed -110 |
| Thu 10/22 7:00 PM | James Madison @ App State | James Madison 34, App State 24 | James Madison 76% | James Madison -315 / App State +315 | 33.5 – 22.8 | 20–49 / 10–37 | James Madison -11.9 / James Madison -10.5 | 55.4 / 56.5 | no edge | no edge | no edge |  |
| Thu 10/22 7:00 PM | Liberty @ Kennesaw State | Liberty 31, Kennesaw State 21 | Liberty 74% | Liberty -280 / Kennesaw State +280 | 30.2 – 20.5 | 16–45 / 7–34 | Liberty -7.9 / Liberty -10.0 | 51.4 / 50.5 | Kennesaw State +10.0 (-110*): EV +14.0%, model 58% | Kennesaw State (+320): EV +27.0%, model 30% | no edge | * price not posted; assumed -110 |
| Thu 10/22 7:30 PM | East Carolina @ Memphis | East Carolina 24, Memphis 31 | Memphis 74% | East Carolina +285 / Memphis -285 | 22.1 – 31.6 | 10–35 / 17–46 | Memphis -6.1 / Memphis -10.0 | 51.8 / 54.2 | East Carolina +10.0 (-110*): EV +20.9%, model 61% | East Carolina (+307): EV +41.5%, model 35% | Under 54.25 (-110*): EV +11.7%, model 59% | * price not posted; assumed -110 |
| Fri 10/23 7:00 PM | Duke @ Virginia | Duke 21, Virginia 24 | Virginia 54% | Duke +115 / Virginia -115 | 23.5 – 24.8 | 10–38 / 13–38 | PK / Virginia -1.5 | 51.3 / 47.5 | no edge | no edge | Over 47.5 (-110*): EV +12.7%, model 59% | * price not posted; assumed -110 |
| Fri 10/23 7:00 PM | Massachusetts @ UConn | Massachusetts 17, UConn 34 | UConn 85% | Massachusetts +570 / UConn -570 | 17.7 – 32.6 | 6–31 / 17–48 | UConn -17.9 / UConn -14.5 | 53.1 / 49.5 | UConn -14.5 (-110*): EV +9.9%, model 58% | no edge | Over 49.5 (-110*): EV +11.5%, model 58% | * price not posted; assumed -110 |
| Fri 10/23 8:30 PM | Army @ Tulsa | Army 28, Tulsa 31 | Tulsa 53% | Army +115 / Tulsa -115 | 26.8 – 28.4 | 14–41 / 14–42 | Tulsa -0.1 / Tulsa -1.8 | 57.9 / 54.5 | no edge | no edge | Over 54.5 (-110*): EV +12.2%, model 59% | * price not posted; assumed -110 |
| Fri 10/23 9:00 PM | Air Force @ Wyoming | Air Force 24, Wyoming 21 | Air Force 65% | Air Force -185 / Wyoming +185 | 26.0 – 20.7 | 13–41 / 7–34 | Air Force -5.8 / Air Force -5.2 | 50.9 / 45.5 | no edge | no edge | Over 45.5 (-110*): EV +17.8%, model 62% | * price not posted; assumed -110 |
| Fri 10/23 10:30 PM | NC State @ Stanford | NC State 31, Stanford 24 | NC State 68% | NC State -210 / Stanford +210 | 31.4 – 24.6 | 17–47 / 10–38 | NC State -9.7 / NC State -6.5 | 57.8 / 55.5 | NC State -6.5 (-110*): EV +8.8%, model 57% | no edge | Over 55.5 (-110*): EV +3.3%, model 54% | * price not posted; assumed -110 |
| Sat 10/24 12:00 PM | LSU @ Auburn | LSU 28, Auburn 21 | LSU 69% | LSU -220 / Auburn +220 | 29.3 – 21.8 | 14–44 / 10–35 | LSU -7.3 / LSU -7.5 | 50.9 / 51.2 | Auburn +7.5 (-110*): EV +7.1%, model 56% | Auburn (+237): EV +7.3%, model 32% | no edge | * price not posted; assumed -110 |
| Sat 10/24 12:00 PM | Texas Tech @ Cincinnati | Texas Tech 34, Cincinnati 24 | Texas Tech 75% | Texas Tech -305 / Cincinnati +305 | 33.3 – 22.7 | 19–48 / 10–37 | Texas Tech -11.0 / Texas Tech -10.5 | 54.2 / 56.5 | no edge | no edge | Under 56.5 (-110*): EV +8.4%, model 57% | * price not posted; assumed -110 |
| Sat 10/24 12:00 PM | West Virginia @ TCU | West Virginia 24, TCU 31 | TCU 73% | West Virginia +270 / TCU -270 | 23.5 – 33.0 | 10–37 / 17–48 | TCU -9.1 / TCU -9.5 | 56.4 / 56.5 | West Virginia +9.5 (-110*): EV +3.5%, model 54% | West Virginia (+264): EV +3.3%, model 28% | no edge | * price not posted; assumed -110 |
| Sat 10/24 12:00 PM | California @ SMU | California 17, SMU 38 | SMU 91% | California +970 / SMU -970 | 17.5 – 37.1 | 6–30 / 22–52 | SMU -20.3 / SMU -19.5 | 54.8 / 54.5 | SMU -19.5 (-110*): EV +4.1%, model 55% | no edge | no edge | * price not posted; assumed -110 |
| Sat 10/24 12:00 PM | Pittsburgh @ Miami | Pittsburgh 17, Miami 34 | Miami 91% | Pittsburgh +1045 / Miami -1045 | 15.1 – 34.7 | 3–27 / 20–50 | Miami -20.1 / Miami -19.5 | 51.7 / 49.2 | no edge | no edge | Over 49.25 (-110*): EV +4.3%, model 55% | * price not posted; assumed -110 |
| Sat 10/24 12:00 PM | Indiana @ Michigan | Indiana 24, Michigan 17 | Indiana 68% | Indiana -215 / Michigan +215 | 24.4 – 17.6 | 10–38 / 7–30 | Indiana -4.8 / Indiana -7.0 | 44.0 / 41.5 | Michigan +7.0 (-110*): EV +14.2%, model 56% | Michigan (+225): EV +20.5%, model 37% | Over 41.5 (-110*): EV +3.3%, model 54% | * price not posted; assumed -110 |
| Sat 10/24 12:00 PM | Rutgers @ Northwestern | Rutgers 21, Northwestern 38 | Northwestern 86% | Rutgers +595 / Northwestern -595 | 20.9 – 37.2 | 7–34 / 23–52 | Northwestern -17.0 / Northwestern -16.2 | 57.4 / 58.2 | no edge | no edge | no edge |  |
| Sat 10/24 12:00 PM | Rice @ Florida Atlantic | Rice 24, Florida Atlantic 31 | Florida Atlantic 71% | Rice +245 / Florida Atlantic -245 | 22.3 – 30.5 | 10–35 / 16–45 | Florida Atlantic -15.8 / Florida Atlantic -7.2 | 57.0 / 51.5 | Florida Atlantic -7.2 (-110*): EV +27.2%, model 67% | Florida Atlantic (-359): EV +8.3%, model 85% | Over 51.5 (-110*): EV +19.6%, model 63% | * price not posted; assumed -110 |
| Sat 10/24 12:00 PM | Western Michigan @ Toledo | Western Michigan 21, Toledo 24 | Toledo 60% | Western Michigan +150 / Toledo -150 | 21.4 – 25.2 | 10–35 / 11–39 | Toledo -9.5 / Toledo -3.0 | 49.6 / 45.8 | Toledo -3.0 (-110*): EV +27.0%, model 63% | Toledo (-168): EV +17.6%, model 74% | Over 45.75 (-110*): EV +12.8%, model 59% | * price not posted; assumed -110 |
| Sat 10/24 1:00 PM | Baylor @ Kansas | Baylor 27, Kansas 24 | Baylor 56% | Baylor -125 / Kansas +125 | 27.9 – 25.5 | 14–42 / 13–39 | Kansas -2.6 / Baylor -3.0 | 55.6 / 52.8 | Kansas +3.0 (-110*): EV +23.4%, model 61% | Kansas (+110): EV +18.8%, model 57% | Over 52.75 (-110*): EV +7.4%, model 56% | * price not posted; assumed -110 |
| Sat 10/24 1:00 PM | Akron @ Kent State | Akron 21, Kent State 24 | Kent State 58% | Akron +140 / Kent State -140 | 21.6 – 24.8 | 10–35 / 12–38 | Kent State -4.4 / Kent State -3.0 | 46.9 / 46.2 | no edge | no edge | no edge |  |
| Sat 10/24 1:00 PM | Miami (OH) @ Central Michigan | Miami (OH) 24, Central Michigan 21 | Miami (OH) 58% | Miami (OH) -135 / Central Michigan +135 | 22.2 – 19.4 | 10–35 / 7–31 | Miami (OH) -5.3 / Miami (OH) -2.5 | 46.9 / 40.0 | Miami (OH) -2.5 (-110*): EV +13.9%, model 60% | Miami (OH) (-127): EV +14.6%, model 64% | Over 40 (-110*): EV +30.3%, model 67% | * price not posted; assumed -110 |
| Sat 10/24 3:00 PM | Oregon @ Illinois | Oregon 31, Illinois 21 | Oregon 75% | Oregon -300 / Illinois +300 | 30.6 – 20.7 | 17–45 / 7–34 | Oregon -13.7 / Oregon -9.5 | 53.2 / 50.8 | Oregon -9.5 (-110*): EV +11.5%, model 58% | Oregon (-396): EV +3.2%, model 82% | Over 50.75 (-110*): EV +7.9%, model 57% | * price not posted; assumed -110 |
| Sat 10/24 3:30 PM | Texas A&M @ Alabama | Texas A&M 17, Alabama 31 | Alabama 81% | Texas A&M +430 / Alabama -430 | 18.1 – 31.3 | 7–31 / 17–46 | Alabama -8.8 / Alabama -13.8 | 45.8 / 50.5 | Texas A&M +13.8 (-110*): EV +22.8%, model 64% | Texas A&M (+457): EV +52.2%, model 27% | Under 50.5 (-110*): EV +21.0%, model 63% | * price not posted; assumed -110 |
| Sat 10/24 3:30 PM | Oklahoma @ Mississippi State | Oklahoma 24, Mississippi State 21 | Oklahoma 63% | Oklahoma -170 / Mississippi State +170 | 24.8 – 20.5 | 13–38 / 7–34 | Oklahoma -3.4 / Oklahoma -4.5 | 47.3 / 44.8 | Mississippi State +4.5 (-110*): EV +5.5%, model 55% | no edge | Over 44.75 (-110*): EV +7.1%, model 56% | * price not posted; assumed -110 |
| Sat 10/24 3:30 PM | Tennessee @ South Carolina | Tennessee 24, South Carolina 27 | South Carolina 54% | Tennessee +120 / South Carolina -120 | 24.5 – 26.1 | 10–38 / 13–40 | Tennessee -6.0 / South Carolina -2.5 | 50.2 / 50.8 | Tennessee +2.5 (-110*): EV +33.2%, model 70% | Tennessee (-100): EV +31.5%, model 66% | no edge | * price not posted; assumed -110 |
| Sat 10/24 3:30 PM | BYU @ UCF | BYU 24, UCF 17 | BYU 68% | BYU -215 / UCF +215 | 25.7 – 18.9 | 13–39 / 7–31 | BYU -9.3 / BYU -6.5 | 48.4 / 43.5 | BYU -6.5 (-110*): EV +8.0%, model 57% | BYU (-251): EV +3.4%, model 74% | Over 43.5 (-110*): EV +18.3%, model 62% | * price not posted; assumed -110 |
| Sat 10/24 3:30 PM | Boston College @ Georgia Tech | Boston College 21, Georgia Tech 24 | Georgia Tech 63% | Boston College +170 / Georgia Tech -170 | 22.7 – 27.4 | 10–37 / 14–42 | Georgia Tech -8.8 / Georgia Tech -4.2 | 52.4 / 49.5 | Georgia Tech -4.2 (-110*): EV +10.8%, model 58% | Georgia Tech (-201): EV +8.7%, model 73% | Over 49.5 (-110*): EV +8.9%, model 57% | * price not posted; assumed -110 |
| Sat 10/24 3:30 PM | Iowa @ Minnesota | Iowa 24, Minnesota 17 | Iowa 68% | Iowa -210 / Minnesota +210 | 23.7 – 17.1 | 10–38 / 6–30 | Iowa -7.4 / Iowa -6.5 | 41.6 / 40.5 | no edge | no edge | no edge |  |
| Sat 10/24 3:30 PM | Michigan State @ UCLA | Michigan State 14, UCLA 31 | UCLA 85% | Michigan State +560 / UCLA -560 | 15.3 – 30.1 | 3–27 / 16–45 | UCLA -21.8 / UCLA -14.0 | 47.8 / 44.8 | UCLA -14.0 (-110*): EV +34.8%, model 69% | UCLA (-637): EV +8.2%, model 94% | Over 44.75 (-110*): EV +10.0%, model 58% | * price not posted; assumed -110 |
| Sat 10/24 3:30 PM | North Texas @ Navy | North Texas 31, Navy 28 | North Texas 56% | North Texas -125 / Navy +125 | 32.4 – 30.0 | 17–48 / 16–45 | North Texas -1.7 / North Texas -2.5 | 62.5 / 62.5 | no edge | no edge | no edge |  |
| Sat 10/24 3:30 PM | Hawai'i @ Northern Illinois | Hawai'i 27, Northern Illinois 24 | Hawai'i 61% | Hawai'i -155 / Northern Illinois +155 | 26.5 – 22.5 | 13–41 / 10–35 | Hawai'i -2.2 / Hawai'i -4.2 | 53.1 / 47.8 | Northern Illinois +4.2 (-110*): EV +10.9%, model 58% | Northern Illinois (+169): EV +18.4%, model 44% | Over 47.75 (-110*): EV +19.6%, model 63% | * price not posted; assumed -110 |
| Sat 10/24 3:30 PM | Sacramento State @ Ball State | Sacramento State 17, Ball State 31 | Ball State 82% | Sacramento State +450 / Ball State -450 | 19.0 – 32.0 | 7–31 / 17–48 | Ball State -3.1 / Ball State -14.2 | 50.0 / 51.2 | Sacramento State +14.2 (-110*): EV +50.3%, model 79% | Sacramento State (+385): EV +101.6%, model 42% | Under 51.25 (-110*): EV +6.3%, model 56% | * price not posted; assumed -110 |
| Sat 10/24 3:30 PM | Bowling Green @ Buffalo | Bowling Green 21, Buffalo 24 | Buffalo 58% | Bowling Green +140 / Buffalo -140 | 20.7 – 23.7 | 7–34 / 10–38 | Buffalo -2.8 / Buffalo -3.0 | 42.8 / 44.8 | no edge | Bowling Green (+152): EV +5.6%, model 42% | Under 44.75 (-110*): EV +7.1%, model 56% | * price not posted; assumed -110 |
| Sat 10/24 3:45 PM | Kansas State @ Arizona State | Kansas State 27, Arizona State 24 | Kansas State 60% | Kansas State -150 / Arizona State +150 | 30.0 – 26.2 | 16–45 / 13–41 | Kansas State -6.5 / Kansas State -3.5 | 54.2 / 56.8 | Kansas State -3.5 (-110*): EV +4.3%, model 55% | Kansas State (-168): EV +5.3%, model 66% | Under 56.75 (-110*): EV +6.6%, model 56% | * price not posted; assumed -110 |
| Sat 10/24 4:00 PM | Eastern Michigan @ Ohio | Eastern Michigan 17, Ohio 31 | Ohio 81% | Eastern Michigan +425 / Ohio -425 | 18.3 – 31.2 | 7–31 / 17–46 | Ohio -17.9 / Ohio -12.2 | 52.7 / 48.5 | Ohio -12.2 (-110*): EV +21.6%, model 64% | Ohio (-460): EV +8.6%, model 89% | Over 48.5 (-110*): EV +13.9%, model 60% | * price not posted; assumed -110 |
| Sat 10/24 4:00 PM | UL Monroe @ Troy | UL Monroe 20, Troy 34 | Troy 82% | UL Monroe +445 / Troy -445 | 18.8 – 32.6 | 7–31 / 17–48 | Troy -12.8 / Troy -14.0 | 52.0 / 51.2 | UL Monroe +14.0 (-110*): EV +5.2%, model 53% | UL Monroe (+546): EV +27.2%, model 20% | no edge | * price not posted; assumed -110 |
| Sat 10/24 5:00 PM | San José State @ Nevada | San José State 21, Nevada 24 | Nevada 64% | San José State +175 / Nevada -175 | 21.0 – 26.1 | 9–34 / 13–41 | Nevada -3.8 / Nevada -5.2 | 49.7 / 46.2 | San José State +5.2 (-110*): EV +6.1%, model 56% | San José State (+177): EV +8.3%, model 39% | Over 46.25 (-110*): EV +10.2%, model 58% | * price not posted; assumed -110 |
| Sat 10/24 5:00 PM | Louisiana @ Southern Miss | Louisiana 31, Southern Miss 24 | Louisiana 74% | Louisiana -280 / Southern Miss +280 | 31.1 – 21.5 | 17–45 / 9–35 | Louisiana -6.0 / Louisiana -10.0 | 53.1 / 52.5 | Southern Miss +10.0 (-110*): EV +20.6%, model 61% | Southern Miss (+310): EV +38.7%, model 34% | no edge | * price not posted; assumed -110 |
| Sat 10/24 5:00 PM | Old Dominion @ Louisiana Tech | Old Dominion 17, Louisiana Tech 27 | Louisiana Tech 80% | Old Dominion +405 / Louisiana Tech -405 | 16.4 – 28.6 | 6–28 / 14–43 | Louisiana Tech -9.8 / Louisiana Tech -12.5 | 42.3 / 45.8 | Old Dominion +12.5 (-110*): EV +13.4%, model 59% | Old Dominion (+339): EV +9.1%, model 25% | Under 45.75 (-110*): EV +17.5%, model 62% | * price not posted; assumed -110 |
| Sat 10/24 6:00 PM | Boise State @ Washington State | Boise State 31, Washington State 17 | Boise State 81% | Boise State -415 / Washington State +415 | 32.0 – 19.1 | 17–48 / 7–31 | Boise State -10.4 / Boise State -13.2 | 49.6 / 51.5 | Washington State +13.2 (-110*): EV +11.9%, model 59% | Washington State (+389): EV +15.1%, model 24% | Under 51.5 (-110*): EV +8.3%, model 57% | * price not posted; assumed -110 |
| Sat 10/24 6:30 PM | San Diego State @ Colorado State | San Diego State 34, Colorado State 31 | San Diego State 54% | San Diego State -115 / Colorado State +115 | 31.6 – 30.2 | 17–47 / 17–45 | San Diego State -2.8 / San Diego State -1.2 | 55.5 / 63.5 | no edge | no edge | Under 63.5 (-110*): EV +33.0%, model 70% | * price not posted; assumed -110 |
| Sat 10/24 7:00 PM | Colorado @ Oklahoma State | Colorado 20, Oklahoma State 34 | Oklahoma State 79% | Colorado +385 / Oklahoma State -385 | 21.4 – 34.0 | 9–35 / 20–49 | Oklahoma State -5.2 / Oklahoma State -13.5 | 53.9 / 55.8 | Colorado +13.5 (-110*): EV +36.7%, model 72% | Colorado (+405): EV +82.0%, model 36% | Under 55.75 (-110*): EV +6.9%, model 56% | * price not posted; assumed -110 |
| Sat 10/24 7:00 PM | Virginia Tech @ Clemson | Virginia Tech 24, Clemson 27 | Clemson 57% | Virginia Tech +135 / Clemson -135 | 23.4 – 26.0 | 10–37 / 13–40 | Clemson -2.1 / Clemson -2.8 | 49.1 / 49.5 | no edge | no edge | no edge |  |
| Sat 10/24 7:00 PM | Georgia State @ Arkansas State | Georgia State 31, Arkansas State 28 | Georgia State 56% | Georgia State -125 / Arkansas State +125 | 30.1 – 28.0 | 17–45 / 14–42 | Georgia State -1.1 / Georgia State -2.2 | 56.8 / 58.5 | no edge | no edge | Under 58.5 (-110*): EV +6.1%, model 56% | * price not posted; assumed -110 |
| Sat 10/24 7:30 PM | Vanderbilt @ Kentucky | Vanderbilt 21, Kentucky 31 | Kentucky 75% | Vanderbilt +295 / Kentucky -295 | 20.8 – 30.7 | 9–34 / 17–45 | Kentucky -5.3 / Kentucky -10.5 | 51.3 / 51.5 | Vanderbilt +10.5 (-110*): EV +28.5%, model 67% | Vanderbilt (+337): EV +56.7%, model 36% | no edge | * price not posted; assumed -110 |
| Sat 10/24 7:30 PM | Ole Miss @ Texas | Ole Miss 24, Texas 27 | Texas 59% | Ole Miss +140 / Texas -140 | 25.3 – 28.5 | 13–38 / 14–42 | Texas -1.1 / Texas -3.5 | 53.2 / 54.0 | Ole Miss +3.5 (-110*): EV +11.7%, model 59% | Ole Miss (+135): EV +11.3%, model 47% | no edge | * price not posted; assumed -110 |
| Sat 10/24 7:30 PM | Iowa State @ Arizona | Iowa State 21, Arizona 31 | Arizona 74% | Iowa State +290 / Arizona -290 | 20.4 – 30.3 | 7–34 / 16–45 | Arizona -5.1 / Arizona -10.5 | 51.0 / 50.5 | Iowa State +10.5 (-110*): EV +28.5%, model 67% | Iowa State (+239): EV +21.8%, model 36% | no edge | * price not posted; assumed -110 |
| Sat 10/24 7:30 PM | Syracuse @ North Carolina | Syracuse 21, North Carolina 28 | North Carolina 68% | Syracuse +215 / North Carolina -215 | 20.5 – 27.6 | 7–34 / 14–42 | North Carolina -3.5 / North Carolina -7.5 | 52.8 / 46.8 | Syracuse +7.5 (-110*): EV +23.2%, model 65% | Syracuse (+270): EV +52.0%, model 41% | Over 46.75 (-110*): EV +23.0%, model 64% | * price not posted; assumed -110 |
| Sat 10/24 7:30 PM | USC @ Wisconsin | USC 27, Wisconsin 24 | USC 58% | USC -140 / Wisconsin +140 | 26.7 – 23.6 | 13–41 / 10–38 | USC -3.8 / USC -3.0 | 52.4 / 49.8 | no edge | no edge | Over 49.75 (-110*): EV +7.0%, model 56% | * price not posted; assumed -110 |
| Sat 10/24 7:30 PM | Utah State @ Texas State | Utah State 24, Texas State 38 | Texas State 81% | Utah State +420 / Texas State -420 | 23.4 – 36.9 | 10–37 / 21–52 | Texas State -13.2 / Texas State -13.5 | 59.8 / 60.5 | no edge | no edge | no edge |  |
| Sat 10/24 8:00 PM | UTSA @ Tulane | UTSA 27, Tulane 24 | UTSA 56% | UTSA -125 / Tulane +125 | 27.1 – 24.7 | 14–41 / 11–38 | UTSA -1.8 / UTSA -2.5 | 52.7 / 51.5 | no edge | no edge | no edge |  |
| Sat 10/24 10:00 PM | North Dakota State @ New Mexico | North Dakota State 17, New Mexico 24 | New Mexico 62% | North Dakota State +165 / New Mexico -165 | 18.7 – 22.9 | 7–31 / 10–37 | New Mexico -2.3 / New Mexico -4.5 | 42.7 / 41.2 | North Dakota State +4.5 (-110*): EV +12.0%, model 59% | North Dakota State (+157): EV +11.3%, model 43% | no edge | * price not posted; assumed -110 |
| Sat 10/24 10:15 PM | Houston @ Utah | Houston 24, Utah 31 | Utah 68% | Houston +210 / Utah -210 | 25.0 – 31.8 | 13–38 / 17–46 | Utah -9.2 / Utah -6.5 | 58.2 / 56.5 | Utah -6.5 (-110*): EV +6.8%, model 56% | no edge | no edge | * price not posted; assumed -110 |

## 2026 Week 9

| Kickoff (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected points | 80% range | Spread: model / line | Total: model / line | Spread edge | Moneyline edge | Total edge | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tue 10/27 7:00 PM | Delaware @ Western Kentucky | Delaware 24, Western Kentucky 27 | Western Kentucky 60% | Delaware +155 / Western Kentucky -155 | 24.5 – 28.3 | 11–38 / 14–42 | Western Kentucky -3.8 / – | 52.8 / – | no line yet | no line yet (model fair: Western Kentucky -150) | no line yet |  |
| Tue 10/27 8:00 PM | Sam Houston @ Missouri State | Sam Houston 21, Missouri State 28 | Missouri State 72% | Sam Houston +260 / Missouri State -260 | 19.9 – 28.3 | 7–33 / 14–42 | Missouri State -8.4 / – | 48.2 / – | no line yet | no line yet (model fair: Missouri State -250) | no line yet |  |
| Wed 10/28 7:00 PM | Kennesaw State @ Middle Tennessee | Kennesaw State 27, Middle Tennessee 24 | Kennesaw State 55% | Kennesaw State -120 / Middle Tennessee +120 | 26.1 – 24.5 | 13–41 / 10–38 | Kennesaw State -1.7 / – | 50.6 / – | no line yet | no line yet (model fair: Kennesaw State -120) | no line yet |  |
| Wed 10/28 8:00 PM | Jacksonville State @ New Mexico State | Jacksonville State 31, New Mexico State 24 | Jacksonville State 67% | Jacksonville State -205 / New Mexico State +205 | 29.0 – 22.1 | 14–44 / 10–35 | Jacksonville State -6.9 / – | 51.0 / – | no line yet | no line yet (model fair: Jacksonville State -205) | no line yet |  |
| Thu 10/29 7:30 PM | Florida Atlantic @ North Texas | Florida Atlantic 31, North Texas 38 | North Texas 66% | Florida Atlantic +195 / North Texas -195 | 30.9 – 37.7 | 17–45 / 23–52 | North Texas -6.8 / – | 68.6 / – | no line yet | no line yet (model fair: North Texas -200) | no line yet |  |
| Thu 10/29 7:30 PM | Troy @ James Madison | Troy 17, James Madison 38 | James Madison 91% | Troy +1040 / James Madison -1040 | 15.9 – 35.6 | 6–28 / 21–51 | James Madison -19.7 / – | 51.5 / – | no line yet | no line yet (model fair: James Madison -960) | no line yet |  |
| Fri 10/30 7:00 PM | Tulane @ Charlotte | Tulane 31, Charlotte 17 | Tulane 86% | Tulane -635 / Charlotte +635 | 31.5 – 15.8 | 17–46 / 6–28 | Tulane -15.6 / – | 47.3 / – | no line yet | no line yet (model fair: Tulane -635) | no line yet |  |
| Fri 10/30 7:30 PM | Baylor @ UCF | Baylor 27, UCF 24 | Baylor 53% | Baylor -115 / UCF +115 | 26.5 – 25.3 | 13–41 / 13–38 | Baylor -1.2 / – | 51.8 / – | no line yet | no line yet (model fair: Baylor -110) | no line yet |  |
| Fri 10/30 10:30 PM | Kent State @ Sacramento State | Kent State 21, Sacramento State 24 | Sacramento State 58% | Kent State +140 / Sacramento State -140 | 21.7 – 25.1 | 10–35 / 13–38 | Sacramento State -3.4 / – | 46.7 / – | no line yet | no line yet (model fair: Sacramento State -145) | no line yet |  |
| Sat 10/31 TBA | Missouri @ Arkansas | Missouri 31, Arkansas 17 | Missouri 82% | Missouri -445 / Arkansas +445 | 31.0 – 17.9 | 17–46 / 7–31 | Missouri -13.0 / – | 48.9 / – | no line yet | no line yet (model fair: Missouri -450) | no line yet |  |
| Sat 10/31 TBA | Auburn @ Ole Miss | Auburn 24, Ole Miss 31 | Ole Miss 69% | Auburn +220 / Ole Miss -220 | 25.2 – 32.6 | 13–38 / 17–48 | Ole Miss -7.4 / – | 57.7 / – | no line yet | no line yet (model fair: Ole Miss -220) | no line yet |  |
| Sat 10/31 TBA | South Carolina @ Oklahoma | South Carolina 17, Oklahoma 27 | Oklahoma 77% | South Carolina +330 / Oklahoma -330 | 16.9 – 27.4 | 6–29 / 14–42 | Oklahoma -10.5 / – | 44.3 / – | no line yet | no line yet (model fair: Oklahoma -340) | no line yet |  |
| Sat 10/31 TBA | Mississippi State @ Texas | Mississippi State 21, Texas 31 | Texas 74% | Mississippi State +290 / Texas -290 | 21.0 – 30.7 | 7–34 / 17–45 | Texas -9.8 / – | 51.7 / – | no line yet | no line yet (model fair: Texas -275) | no line yet |  |
| Sat 10/31 TBA | Arizona @ Texas Tech | Arizona 17, Texas Tech 27 | Texas Tech 77% | Arizona +335 / Texas Tech -335 | 18.8 – 30.0 | 7–31 / 16–45 | Texas Tech -11.2 / – | 48.8 / – | no line yet | no line yet (model fair: Texas Tech -350) | no line yet |  |
| Sat 10/31 TBA | Arizona State @ BYU | Arizona State 17, BYU 34 | BYU 85% | Arizona State +550 / BYU -550 | 17.8 – 32.5 | 7–30 / 17–48 | BYU -14.7 / – | 50.4 / – | no line yet | no line yet (model fair: BYU -540) | no line yet |  |
| Sat 10/31 TBA | Kansas @ TCU | Kansas 24, TCU 27 | TCU 51% | Kansas +105 / TCU -105 | 24.6 – 25.3 | 10–38 / 13–39 | TCU -0.6 / – | 49.9 / – | no line yet | no line yet (model fair: TCU -110) | no line yet |  |
| Sat 10/31 TBA | Kansas State @ Colorado | Kansas State 31, Colorado 24 | Kansas State 69% | Kansas State -225 / Colorado +225 | 29.9 – 22.3 | 16–45 / 10–35 | Kansas State -7.6 / – | 52.1 / – | no line yet | no line yet (model fair: Kansas State -230) | no line yet |  |
| Sat 10/31 TBA | Oklahoma State @ Iowa State | Oklahoma State 24, Iowa State 31 | Iowa State 65% | Oklahoma State +190 / Iowa State -190 | 24.0 – 29.9 | 10–38 / 16–45 | Iowa State -5.9 / – | 53.9 / – | no line yet | no line yet (model fair: Iowa State -190) | no line yet |  |
| Sat 10/31 TBA | Utah @ Cincinnati | Utah 34, Cincinnati 27 | Utah 72% | Utah -250 / Cincinnati +250 | 34.7 – 26.0 | 20–49 / 13–41 | Utah -8.7 / – | 60.7 / – | no line yet | no line yet (model fair: Utah -255) | no line yet |  |
| Sat 10/31 TBA | California @ NC State | California 24, NC State 34 | NC State 75% | California +305 / NC State -305 | 24.2 – 34.6 | 10–38 / 20–49 | NC State -10.4 / – | 58.9 / – | no line yet | no line yet (model fair: NC State -300) | no line yet |  |
| Sat 10/31 TBA | SMU @ Syracuse | SMU 31, Syracuse 24 | SMU 72% | SMU -255 / Syracuse +255 | 31.3 – 22.5 | 17–46 / 10–36 | SMU -8.8 / – | 53.9 / – | no line yet | no line yet (model fair: SMU -260) | no line yet |  |
| Sat 10/31 TBA | Boston College @ Duke | Boston College 17, Duke 31 | Duke 83% | Boston College +505 / Duke -505 | 17.8 – 32.8 | 7–31 / 17–48 | Duke -15.0 / – | 50.6 / – | no line yet | no line yet (model fair: Duke -535) | no line yet |  |
| Sat 10/31 TBA | Clemson @ Florida State | Clemson 27, Florida State 24 | Clemson 53% | Clemson -110 / Florida State +110 | 26.3 – 25.3 | 13–41 / 13–40 | Florida State -3.9 / Clemson -1.5 | 52.0 / 51.5 | Florida State +1.5 (-110*): EV +18.2%, model 62% | Florida State (-108): EV +15.3%, model 60% | no edge | * price not posted; assumed -110 |
| Sat 10/31 TBA | Georgia Tech @ Pittsburgh | Georgia Tech 24, Pittsburgh 31 | Pittsburgh 71% | Georgia Tech +240 / Pittsburgh -240 | 22.6 – 31.0 | 10–36 / 17–46 | Pittsburgh -8.4 / – | 53.5 / – | no line yet | no line yet (model fair: Pittsburgh -250) | no line yet |  |
| Sat 10/31 TBA | Miami @ North Carolina | Miami 34, North Carolina 17 | Miami 89% | Miami -845 / North Carolina +845 | 35.6 – 17.4 | 21–51 / 6–30 | Miami -18.2 / – | 53.0 / – | no line yet | no line yet (model fair: Miami -825) | no line yet |  |
| Sat 10/31 TBA | Stanford @ Louisville | Stanford 14, Louisville 42 | Louisville 97% | Stanford +3435 / Louisville -3435 | 14.1 – 41.5 | 3–25 / 27–57 | Louisville -27.3 / – | 55.6 / – | no line yet | no line yet (model fair: Louisville -3325) | no line yet |  |
| Sat 10/31 TBA | Virginia @ Wake Forest | Virginia 17, Wake Forest 31 | Wake Forest 84% | Virginia +530 / Wake Forest -530 | 17.3 – 31.9 | 6–30 / 17–47 | Wake Forest -14.7 / – | 49.2 / – | no line yet | no line yet (model fair: Wake Forest -515) | no line yet |  |
| Sat 10/31 TBA | Minnesota @ Indiana | Minnesota 10, Indiana 31 | Indiana 94% | Minnesota +1575 / Indiana -1575 | 10.2 – 31.5 | 0–20 / 17–47 | Indiana -21.3 / – | 41.7 / – | no line yet | no line yet (model fair: Indiana -1685) | no line yet |  |
| Sat 10/31 TBA | Wisconsin @ Iowa | Wisconsin 17, Iowa 24 | Iowa 70% | Wisconsin +230 / Iowa -230 | 18.0 – 25.2 | 7–31 / 12–38 | Iowa -7.2 / – | 43.3 / – | no line yet | no line yet (model fair: Iowa -235) | no line yet |  |
| Sat 10/31 TBA | Illinois @ Maryland | Illinois 24, Maryland 27 | Maryland 55% | Illinois +125 / Maryland -125 | 26.2 – 28.4 | 13–41 / 14–43 | Maryland -2.2 / – | 54.6 / – | no line yet | no line yet (model fair: Maryland -130) | no line yet |  |
| Sat 10/31 TBA | Washington @ Nebraska | Washington 21, Nebraska 28 | Nebraska 74% | Washington +280 / Nebraska -280 | 19.8 – 28.7 | 7–33 / 14–44 | Nebraska -9.0 / – | 48.5 / – | no line yet | no line yet (model fair: Nebraska -280) | no line yet |  |
| Sat 10/31 TBA | Northwestern @ Oregon | Northwestern 21, Oregon 28 | Oregon 72% | Northwestern +250 / Oregon -250 | 21.2 – 29.6 | 9–35 / 15–44 | Oregon -8.4 / – | 50.9 / – | no line yet | no line yet (model fair: Oregon -250) | no line yet |  |
| Sat 10/31 TBA | Purdue @ Penn State | Purdue 17, Penn State 31 | Penn State 79% | Purdue +380 / Penn State -380 | 19.1 – 31.2 | 7–31 / 17–47 | Penn State -12.1 / – | 50.3 / – | no line yet | no line yet (model fair: Penn State -395) | no line yet |  |
| Sat 10/31 TBA | Michigan @ Rutgers | Michigan 31, Rutgers 17 | Michigan 85% | Michigan -570 / Rutgers +570 | 33.5 – 18.0 | 19–49 / 7–31 | Michigan -15.4 / – | 51.5 / – | no line yet | no line yet (model fair: Michigan -580) | no line yet |  |
| Sat 10/31 TBA | Nevada @ UCLA | Nevada 6, UCLA 41 | UCLA 100% | Nevada +9900 / UCLA -9900 | 7.2 – 40.8 | 0–14 / 27–58 | UCLA -33.6 / – | 48.0 / – | no line yet | no line yet (model fair: UCLA -9900) | no line yet |  |
| Sat 10/31 TBA | Ohio State @ USC | Ohio State 31, USC 24 | Ohio State 70% | Ohio State -230 / USC +230 | 31.4 – 23.6 | 17–46 / 10–38 | Ohio State -9.9 / Ohio State -7.5 | 56.6 / 54.5 | no edge | no edge | Over 54.5 (-110*): EV +4.6%, model 55% | * price not posted; assumed -110 |
| Sat 10/31 TBA | Oregon State @ Fresno State | Oregon State 31, Fresno State 28 | Oregon State 60% | Oregon State -155 / Fresno State +155 | 30.2 – 26.3 | 16–45 / 13–41 | Oregon State -3.9 / – | 56.5 / – | no line yet | no line yet (model fair: Oregon State -150) | no line yet |  |
| Sat 10/31 TBA | Army @ Memphis | Army 28, Memphis 31 | Memphis 62% | Army +160 / Memphis -160 | 27.3 – 31.8 | 14–42 / 17–47 | Memphis -4.6 / – | 59.1 / – | no line yet | no line yet (model fair: Memphis -160) | no line yet |  |
| Sat 10/31 TBA | Temple @ East Carolina | Temple 21, East Carolina 28 | East Carolina 72% | Temple +255 / East Carolina -255 | 21.3 – 30.0 | 9–35 / 16–45 | East Carolina -8.7 / – | 51.2 / – | no line yet | no line yet (model fair: East Carolina -255) | no line yet |  |
| Sat 10/31 TBA | UAB @ South Florida | UAB 21, South Florida 31 | South Florida 76% | UAB +320 / South Florida -320 | 19.9 – 30.2 | 7–33 / 16–45 | South Florida -10.3 / – | 50.1 / – | no line yet | no line yet (model fair: South Florida -315) | no line yet |  |
| Sat 10/31 TBA | New Mexico @ San José State | New Mexico 31, San José State 17 | New Mexico 80% | New Mexico -390 / San José State +390 | 30.7 – 18.6 | 17–45 / 7–31 | New Mexico -12.1 / – | 49.3 / – | no line yet | no line yet (model fair: New Mexico -390) | no line yet |  |
| Sat 10/31 TBA | App State @ Georgia Southern | App State 28, Georgia Southern 31 | Georgia Southern 51% | App State +105 / Georgia Southern -105 | 28.4 – 28.9 | 14–42 / 14–44 | Georgia Southern -0.5 / – | 57.3 / – | no line yet | no line yet (model fair: Georgia Southern -105) | no line yet |  |
| Sat 10/31 TBA | Coastal Carolina @ Georgia State | Coastal Carolina 24, Georgia State 31 | Georgia State 71% | Coastal Carolina +240 / Georgia State -240 | 24.1 – 32.4 | 10–38 / 17–48 | Georgia State -8.3 / – | 56.5 / – | no line yet | no line yet (model fair: Georgia State -235) | no line yet |  |
| Sat 10/31 TBA | Southern Miss @ UL Monroe | Southern Miss 27, UL Monroe 24 | Southern Miss 57% | Southern Miss -135 / UL Monroe +135 | 29.0 – 26.2 | 14–44 / 13–41 | Southern Miss -2.8 / – | 55.2 / – | no line yet | no line yet (model fair: Southern Miss -135) | no line yet |  |
| Sat 10/31 TBA | Marshall @ Old Dominion | Marshall 24, Old Dominion 21 | Marshall 59% | Marshall -140 / Old Dominion +140 | 25.3 – 22.2 | 13–39 / 10–35 | Marshall -3.1 / – | 47.5 / – | no line yet | no line yet (model fair: Marshall -140) | no line yet |  |
| Sat 10/31 TBA | Louisiana Tech @ South Alabama | Louisiana Tech 31, South Alabama 28 | Louisiana Tech 53% | Louisiana Tech -115 / South Alabama +115 | 29.5 – 28.1 | 16–44 / 14–42 | Louisiana Tech -1.4 / – | 57.6 / – | no line yet | no line yet (model fair: Louisiana Tech -110) | no line yet |  |
| Sat 10/31 12:00 PM | Notre Dame vs Navy | Notre Dame 38, Navy 10 | Notre Dame 98% | Notre Dame -4050 / Navy +4050 | 38.8 – 11.5 | 24–55 / 3–21 | Notre Dame -27.3 / – | 50.3 / – | no line yet | no line yet (model fair: Notre Dame -3520) | no line yet | neutral site |
| Sat 10/31 12:00 PM | Bowling Green @ Western Michigan | Bowling Green 13, Western Michigan 27 | Western Michigan 86% | Bowling Green +590 / Western Michigan -590 | 13.9 – 28.1 | 3–24 / 14–42 | Western Michigan -14.2 / – | 42.0 / – | no line yet | no line yet (model fair: Western Michigan -555) | no line yet |  |
| Sat 10/31 3:00 PM | UConn @ Air Force | UConn 28, Air Force 31 | Air Force 56% | UConn +125 / Air Force -125 | 28.0 – 30.6 | 14–42 / 17–45 | Air Force -2.5 / – | 58.6 / – | no line yet | no line yet (model fair: Air Force -130) | no line yet |  |
| Sat 10/31 3:30 PM | Florida vs Georgia | Florida 21, Georgia 31 | Georgia 79% | Florida +380 / Georgia -380 | 20.7 – 32.8 | 7–34 / 17–48 | Georgia -9.2 / Georgia -12.5 | 53.3 / 53.5 | Florida +12.5 (-110*): EV +13.5%, model 59% | Florida (+410): EV +35.4%, model 27% | no edge | neutral site, * price not posted; assumed -110 |
| Sat 10/31 3:30 PM | Colorado State @ Utah State | Colorado State 24, Utah State 27 | Utah State 59% | Colorado State +145 / Utah State -145 | 26.0 – 29.3 | 13–40 / 15–45 | Utah State -3.3 / – | 55.3 / – | no line yet | no line yet (model fair: Utah State -140) | no line yet |  |
| Sat 10/31 3:30 PM | UTEP @ North Dakota State | UTEP 6, North Dakota State 34 | North Dakota State 99% | UTEP +8875 / North Dakota State -8875 | 6.7 – 34.7 | 0–14 / 20–51 | North Dakota State -28.0 / – | 41.4 / – | no line yet | no line yet (model fair: North Dakota State -8750) | no line yet |  |
| Sat 10/31 3:30 PM | Florida International @ Liberty | Florida International 17, Liberty 27 | Liberty 77% | Florida International +345 / Liberty -345 | 17.9 – 29.0 | 7–31 / 14–44 | Liberty -11.1 / – | 46.9 / – | no line yet | no line yet (model fair: Liberty -340) | no line yet |  |
| Sat 10/31 7:00 PM | Washington State @ San Diego State | Washington State 21, San Diego State 24 | San Diego State 56% | Washington State +130 / San Diego State -130 | 21.1 – 23.5 | 9–34 / 10–37 | San Diego State -2.3 / – | 44.6 / – | no line yet | no line yet (model fair: San Diego State -135) | no line yet |  |
| Sat 10/31 10:00 PM | Texas State @ Boise State | Texas State 31, Boise State 38 | Boise State 72% | Texas State +250 / Boise State -250 | 28.0 – 37.0 | 14–42 / 21–52 | Boise State -8.9 / – | 65.0 / – | no line yet | no line yet (model fair: Boise State -245) | no line yet |  |
| Sat 10/31 10:30 PM | Northern Illinois @ UNLV | Northern Illinois 17, UNLV 34 | UNLV 84% | Northern Illinois +535 / UNLV -535 | 18.8 – 34.0 | 7–31 / 20–49 | UNLV -15.2 / – | 52.8 / – | no line yet | no line yet (model fair: UNLV -545) | no line yet |  |

## How the 2026 predictions have done

| Predictor | Games | Margin MAE | Total MAE | Team-score MAE | Winners | Brier | 80% range hit |
|---|---|---|---|---|---|---|---|
| Final prediction | 510 | 11.64 | 11.97 | 8.34 | 82.2% | 0.126 | 82.7% |
| Model only (before blending) | 510 | 12.42 | 12.30 | 8.63 | 79.6% | – | – |
| Betting line when predicted | 508 | 11.62 | 11.92 | 8.33 | 82.1% | – | – |

MAE is mean absolute error in points (lower is better). Brier scores the win chances (lower is better, 0.25 is a coin flip). Even the closing betting line misses the final margin of an FBS game by about 12.5 points.

501 of these games were played before the predictor went live. They are backfilled walk-forward (each week predicted from earlier weeks only) but with closing lines, so they flatter the model slightly. Every game since is graded on the prediction logged before kickoff.

### Betting edges

| Market | Edges | Record (W-L-P) | Units | ROI |
|---|---|---|---|---|
| Spread | 0 | 0-0-0 | +0.00 | – |
| Moneyline | 0 | 0-0-0 | +0.00 | – |
| Total | 0 | 0-0-0 | +0.00 | – |

One unit staked on every edge logged before kickoff (backfilled games are not included). Units are profit at the logged price; ROI is units per unit staked, pushes returning the stake.

### Week 7 results

| Game | Predicted | Final | Win chance for winner | Inside 80% ranges |
|---|---|---|---|---|
| Delaware @ Middle Tennessee | 27–24 | 30–33 | 45% | yes |
| Florida International @ Jacksonville State | 21–24 | 24–27 | 61% | yes |
| Kennesaw State @ Missouri State | 27–24 | 21–24 | 44% | yes |
| Western Kentucky @ Sam Houston | 27–24 | 16–3 | 55% | no |
| East Carolina @ UAB | 28–21 | 17–30 | 35% | yes |
| Georgia Southern @ Old Dominion | 24–21 | 23–15 | 56% | yes |
| Colorado State @ Texas State | 24–41 | 27–66 | 84% | no |
| Memphis @ Tulane | 31–24 | 17–31 | 33% | yes |
| Washington @ Purdue | 24–27 | 38–26 | 44% | yes |
| App State @ Coastal Carolina | 27–24 | 35–32 | 53% | yes |
| Mississippi State @ LSU | 21–38 | 0–31 | 87% | no |
| Florida @ Texas | 17–31 | 27–24 | 19% | yes |
| Cincinnati @ West Virginia | 31–34 | 42–45 | 52% | yes |
| Kansas @ Kansas State | 24–27 | 24–35 | 58% | yes |
| Charleston Southern @ Clemson | 3–48 | 0–37 | 100% | yes |
| Pittsburgh @ Boston College | 24–17 | 21–27 | 31% | yes |
| Virginia @ SMU | 21–31 | 13–23 | 75% | yes |
| Ohio State @ Indiana | 27–24 | 19–15 | 57% | yes |
| Northwestern @ Michigan State | 31–24 | 24–21 | 71% | yes |
| Florida Atlantic @ Army | 28–31 | 24–56 | 56% | no |
| Ball State @ Bowling Green | 17–24 | 32–31 | 33% | yes |
| Georgia State @ James Madison | 24–31 | 22–49 | 70% | no |
| Rutgers @ Maryland | 24–31 | 37–30 | 34% | yes |
| The Citadel @ Texas A&M | 3–52 | 0–41 | 100% | yes |
| Charlotte @ Temple | 17–34 | 38–31 | 11% | no |
| Massachusetts @ Buffalo | 17–24 | 18–25 | 67% | yes |
| Western Michigan @ Central Michigan | 24–17 | 21–14 | 69% | yes |
| Auburn @ Georgia | 14–35 | 27–24 | 9% | yes |
| Missouri @ Ole Miss | 28–31 | 3–31 | 60% | no |
| Alabama @ Tennessee | 28–21 | 10–26 | 31% | no |
| Arizona State @ Texas Tech | 17–34 | 25–53 | 87% | no |
| Georgia Tech @ Virginia Tech | 24–31 | 24–34 | 71% | yes |
| North Carolina @ Duke | 24–27 | 24–20 | 40% | yes |
| Penn State @ Michigan | 17–24 | 18–21 | 67% | yes |
| Northern Illinois @ Wyoming | 17–24 | 23–41 | 69% | no |
| UNLV @ Air Force | 24–27 | 31–41 | 54% | yes |
| Toledo @ Eastern Michigan | 31–24 | 34–14 | 71% | yes |
| Akron @ Miami (OH) | 17–27 | 14–34 | 77% | yes |
| Tulsa @ Rice | 24–21 | 38–17 | 60% | yes |
| Troy @ Louisiana | 24–27 | 6–33 | 58% | no |
| Washington State @ Oregon State | 17–34 | 30–48 | 89% | yes |
| Arkansas @ Vanderbilt | 21–28 | 31–21 | 34% | yes |
| TCU @ Baylor | 24–27 | 17–6 | 39% | no |
| Florida State @ Miami | 17–38 | 35–43 | 91% | no |
| Kent State @ South Florida | 13–34 | 2–29 | 93% | no |
| Nevada @ North Dakota State | 14–28 | 17–31 | 86% | yes |
| Arkansas State @ Southern Miss | 31–28 | 23–13 | 62% | no |
| Kentucky @ Oklahoma | 17–24 | 21–13 | 29% | yes |
| Notre Dame @ BYU | 27–17 | 24–28 | 25% | yes |
| Oklahoma State @ Houston | 28–31 | 32–35 | 62% | yes |
| Elon @ Stanford | 10–42 | 7–34 | 99% | yes |
| Louisville @ Syracuse | 34–20 | 34–26 | 83% | yes |
| Wisconsin @ UCLA | 21–24 | 7–17 | 57% | yes |
| Navy @ UTSA | 24–31 | 34–38 | 67% | yes |
| Louisiana Tech @ UL Monroe | 34–24 | 24–0 | 76% | no |
| San José State @ UTEP | 27–20 | 24–11 | 67% | yes |
| Ohio @ Sacramento State | 31–14 | 48–7 | 87% | yes |
| Utah @ Colorado | 34–17 | 27–24 | 85% | yes |
| Wake Forest @ California | 31–24 | 41–7 | 74% | no |
| Fresno State @ San Diego State | 27–20 | 23–26 | 33% | yes |
| New Mexico @ Hawai'i | 31–17 | 21–10 | 82% | yes |
| Nebraska @ Oregon | 21–28 | 14–17 | 66% | yes |

## FBS power ratings

Points per game better than an average FBS team on a neutral field, from opponent-adjusted EPA (garbage time removed) with this season's games weighted against a preseason prior, plus the weight the margin model puts on Elo (a rating built from game results alone). Defense is positive when it holds opponents below average.

| # | Team | Conference | Net | Offense | Defense | Special teams | Results (Elo) | Elo rating |
|---|---|---|---|---|---|---|---|---|
| 1 | Ohio State | Big Ten | +26.8 | +10.7 | +10.5 | +0.4 | +5.1 | 1934 |
| 2 | LSU | SEC | +24.4 | +9.0 | +12.7 | +0.2 | +2.5 | 1717 |
| 3 | Notre Dame | FBS Independents | +24.1 | +8.7 | +10.1 | +1.3 | +4.1 | 1849 |
| 4 | Georgia | SEC | +23.4 | +9.6 | +8.6 | +0.9 | +4.3 | 1866 |
| 5 | Miami | ACC | +22.7 | +11.6 | +6.5 | +0.1 | +4.5 | 1881 |
| 6 | Indiana | Big Ten | +22.2 | +7.9 | +9.1 | +0.3 | +5.0 | 1921 |
| 7 | Texas Tech | Big 12 | +19.1 | +1.8 | +12.6 | +1.2 | +3.6 | 1803 |
| 8 | Alabama | SEC | +19.1 | +8.4 | +7.4 | +0.3 | +3.0 | 1760 |
| 9 | Ole Miss | SEC | +19.1 | +11.1 | +3.4 | +0.7 | +3.9 | 1834 |
| 10 | Texas | SEC | +18.0 | +3.4 | +10.9 | +0.5 | +3.2 | 1770 |
| 11 | Utah | Big 12 | +17.7 | +8.6 | +5.3 | +0.3 | +3.5 | 1801 |
| 12 | Oregon | Big Ten | +17.7 | +4.0 | +10.0 | +0.4 | +3.3 | 1784 |
| 13 | Tennessee | SEC | +16.4 | +3.4 | +9.3 | +0.7 | +3.0 | 1753 |
| 14 | Oklahoma | SEC | +16.1 | +0.4 | +13.3 | +0.8 | +1.7 | 1649 |
| 15 | UCLA | Big Ten | +16.0 | +6.4 | +7.3 | +0.6 | +1.8 | 1657 |
| 16 | BYU | Big 12 | +15.6 | +6.1 | +5.4 | +0.4 | +3.7 | 1814 |
| 17 | Missouri | SEC | +15.5 | +3.9 | +8.9 | +0.5 | +2.1 | 1686 |
| 18 | Wake Forest | ACC | +15.0 | +5.8 | +6.9 | +0.1 | +2.2 | 1688 |
| 19 | Louisville | ACC | +14.9 | +8.7 | +4.0 | +0.3 | +1.9 | 1663 |
| 20 | Michigan | Big Ten | +14.9 | +4.2 | +8.4 | +0.4 | +2.0 | 1674 |
| 21 | USC | Big Ten | +14.6 | +12.3 | -0.7 | +0.3 | +2.7 | 1734 |
| 22 | Auburn | SEC | +14.1 | +4.9 | +7.6 | +0.7 | +0.9 | 1584 |
| 23 | Nebraska | Big Ten | +14.1 | +4.7 | +7.5 | +0.5 | +1.4 | 1622 |
| 24 | Florida | SEC | +14.0 | +9.0 | +3.1 | +1.0 | +1.0 | 1592 |
| 25 | Iowa | Big Ten | +12.5 | +2.3 | +6.2 | +1.0 | +3.0 | 1756 |
| 26 | Texas A&M | SEC | +12.4 | +2.3 | +8.2 | +0.6 | +1.3 | 1618 |
| 27 | Kansas State | Big 12 | +12.3 | +7.9 | +3.1 | +0.3 | +1.1 | 1599 |
| 28 | SMU | ACC | +12.2 | +5.8 | +4.0 | +0.1 | +2.4 | 1705 |
| 29 | Arizona | Big 12 | +11.6 | +5.5 | +3.6 | -0.0 | +2.4 | 1710 |
| 30 | Houston | Big 12 | +11.1 | +8.7 | +0.2 | +0.0 | +2.2 | 1690 |
| 31 | Mississippi State | SEC | +10.8 | +7.2 | +2.8 | +0.3 | +0.5 | 1551 |
| 32 | Northwestern | Big Ten | +10.8 | +5.6 | +2.3 | +1.3 | +1.6 | 1640 |
| 33 | Penn State | Big Ten | +10.6 | +2.4 | +6.7 | +0.5 | +1.0 | 1593 |
| 34 | Wisconsin | Big Ten | +8.5 | +0.9 | +6.8 | +0.2 | +0.6 | 1559 |
| 35 | Kentucky | SEC | +8.3 | +1.8 | +4.5 | +0.2 | +1.7 | 1653 |
| 36 | Washington | Big Ten | +8.1 | +2.3 | +4.3 | -0.1 | +1.5 | 1635 |
| 37 | South Carolina | SEC | +8.0 | +3.8 | +2.6 | +0.8 | +0.7 | 1569 |
| 38 | Kansas | Big 12 | +7.9 | +6.0 | +2.6 | +0.2 | -0.8 | 1441 |
| 39 | Iowa State | Big 12 | +7.9 | +3.0 | +3.2 | +0.9 | +0.8 | 1578 |
| 40 | Baylor | Big 12 | +6.8 | -0.4 | +5.5 | +1.1 | +0.6 | 1559 |
| 41 | Cincinnati | Big 12 | +6.5 | +8.8 | -2.8 | +0.3 | +0.2 | 1522 |
| 42 | Florida State | ACC | +6.1 | +7.9 | -1.6 | -0.1 | -0.1 | 1497 |
| 43 | TCU | Big 12 | +5.8 | -1.3 | +5.4 | +0.5 | +1.3 | 1613 |
| 44 | Boise State | Pac-12 | +5.5 | +4.2 | -1.2 | +0.2 | +2.3 | 1702 |
| 45 | Vanderbilt | SEC | +5.2 | +4.2 | +0.1 | +0.4 | +0.5 | 1553 |
| 46 | James Madison | Sun Belt | +5.0 | +0.4 | +0.6 | +0.6 | +3.4 | 1789 |
| 47 | Oklahoma State | Big 12 | +4.9 | +5.2 | -0.2 | +0.5 | -0.5 | 1464 |
| 48 | Duke | ACC | +4.6 | +2.6 | -0.3 | +0.7 | +1.5 | 1635 |
| 49 | Virginia Tech | ACC | +4.5 | +3.7 | +0.2 | +0.3 | +0.3 | 1531 |
| 50 | Pittsburgh | ACC | +4.4 | -0.4 | +3.6 | +0.7 | +0.5 | 1551 |
| 51 | UCF | Big 12 | +4.2 | +0.9 | +4.1 | +0.0 | -0.7 | 1448 |
| 52 | Clemson | ACC | +4.1 | -4.2 | +6.6 | +0.4 | +1.3 | 1613 |
| 53 | Arizona State | Big 12 | +3.4 | +1.0 | +1.9 | +0.3 | +0.2 | 1521 |
| 54 | Colorado | Big 12 | +3.3 | -0.3 | +6.0 | -0.7 | -1.6 | 1377 |
| 55 | Minnesota | Big Ten | +3.2 | -2.5 | +4.9 | +0.5 | +0.3 | 1532 |
| 56 | Virginia | ACC | +3.1 | -0.0 | +3.0 | -0.2 | +0.3 | 1534 |
| 57 | North Texas | American Athletic | +3.0 | +9.1 | -6.3 | -0.9 | +1.1 | 1603 |
| 58 | Oregon State | Pac-12 | +3.0 | +5.4 | -2.3 | +0.1 | -0.1 | 1498 |
| 59 | NC State | ACC | +2.9 | +6.3 | -3.3 | -0.5 | +0.4 | 1539 |
| 60 | Illinois | Big Ten | +1.6 | +5.3 | -4.4 | +0.3 | +0.4 | 1539 |
| 61 | North Carolina | ACC | +1.6 | +0.9 | -0.2 | +0.6 | +0.3 | 1532 |
| 62 | Syracuse | ACC | +1.4 | +1.0 | +2.7 | -0.3 | -1.9 | 1347 |
| 63 | Maryland | Big Ten | +1.3 | -0.7 | +3.4 | +0.5 | -2.0 | 1343 |
| 64 | UTSA | American Athletic | +1.0 | +2.7 | -3.1 | -0.1 | +1.5 | 1636 |
| 65 | Purdue | Big Ten | +0.9 | +3.1 | -1.9 | +0.5 | -0.8 | 1444 |
| 66 | Arkansas | SEC | +0.9 | +1.0 | +0.4 | -0.4 | -0.2 | 1496 |
| 67 | Texas State | Pac-12 | +0.7 | +7.4 | -5.8 | -1.5 | +0.6 | 1559 |
| 68 | Memphis | American Athletic | +0.4 | +2.2 | -1.8 | -0.4 | +0.4 | 1544 |
| 69 | Toledo | Mid-American | -0.1 | -2.0 | +1.3 | +0.4 | +0.2 | 1522 |
| 70 | New Mexico | Mountain West | -0.2 | -2.1 | +0.6 | +0.2 | +1.1 | 1598 |
| 71 | Georgia Tech | ACC | -0.9 | +3.3 | -3.9 | -0.0 | -0.3 | 1480 |
| 72 | West Virginia | Big 12 | -0.9 | +4.1 | -5.1 | +0.6 | -0.6 | 1462 |
| 73 | North Dakota State | Mountain West | -1.2 | -4.7 | +3.4 | +1.2 | -1.1 | 1419 |
| 74 | Navy | American Athletic | -1.4 | +2.1 | -3.0 | -0.5 | +0.0 | 1512 |
| 75 | South Florida | American Athletic | -1.4 | -1.1 | -0.9 | -0.1 | +0.8 | 1572 |
| 76 | Army | American Athletic | -1.8 | +4.8 | -7.2 | -0.4 | +1.0 | 1591 |
| 77 | UConn | FBS Independents | -2.4 | +2.1 | -4.0 | -0.3 | -0.2 | 1496 |
| 78 | Florida Atlantic | American Athletic | -2.6 | +2.8 | -4.8 | +0.4 | -1.1 | 1419 |
| 79 | Rutgers | Big Ten | -2.8 | +3.2 | -5.2 | +0.3 | -1.1 | 1417 |
| 80 | Liberty | Conference USA | -2.8 | -0.4 | -2.1 | -0.2 | -0.2 | 1495 |
| 81 | Michigan State | Big Ten | -3.0 | -2.2 | +0.3 | +0.2 | -1.3 | 1399 |
| 82 | East Carolina | American Athletic | -3.0 | -5.3 | +3.1 | -0.8 | -0.0 | 1507 |
| 83 | Ohio | Mid-American | -3.0 | -0.7 | -3.7 | +0.6 | +0.8 | 1571 |
| 84 | Fresno State | Pac-12 | -3.3 | -2.3 | -1.3 | -0.0 | +0.4 | 1544 |
| 85 | Tulane | American Athletic | -3.4 | -4.6 | +0.1 | +0.0 | +1.2 | 1604 |
| 86 | Air Force | Mountain West | -3.8 | +1.9 | -5.4 | -0.3 | -0.0 | 1507 |
| 87 | Tulsa | American Athletic | -4.2 | -1.8 | -0.4 | -0.3 | -1.7 | 1369 |
| 88 | UNLV | Mountain West | -4.8 | -2.9 | -2.3 | +0.0 | +0.4 | 1540 |
| 89 | California | ACC | -5.0 | -0.8 | -2.4 | -0.5 | -1.3 | 1403 |
| 90 | Louisiana Tech | Sun Belt | -5.3 | -3.5 | -0.4 | -0.8 | -0.5 | 1464 |
| 91 | Jacksonville State | Conference USA | -6.0 | -0.6 | -4.5 | -0.4 | -0.5 | 1465 |
| 92 | Boston College | ACC | -6.5 | -4.8 | +0.0 | -0.8 | -1.0 | 1430 |
| 93 | Washington State | Pac-12 | -6.8 | -6.2 | +1.3 | -0.4 | -1.5 | 1388 |
| 94 | Western Michigan | Mid-American | -7.3 | -5.1 | -3.5 | +0.4 | +0.9 | 1584 |
| 95 | Georgia State | Sun Belt | -7.4 | +0.5 | -6.9 | -0.1 | -1.0 | 1424 |
| 96 | Marshall | Sun Belt | -7.6 | -1.5 | -4.8 | -0.4 | -0.9 | 1433 |
| 97 | Miami (OH) | Mid-American | -7.6 | -3.9 | -3.5 | +0.6 | -0.9 | 1435 |
| 98 | San Diego State | Pac-12 | -7.8 | -7.5 | +0.2 | +0.6 | -1.0 | 1425 |
| 99 | App State | Sun Belt | -8.3 | -2.8 | -3.9 | -0.4 | -1.2 | 1411 |
| 100 | Louisiana | Sun Belt | -8.4 | -4.4 | -4.2 | -0.0 | +0.1 | 1520 |
| 101 | Stanford | ACC | -9.3 | -4.0 | -4.2 | -0.4 | -0.8 | 1441 |
| 102 | Temple | American Athletic | -9.4 | +1.2 | -7.6 | -0.6 | -2.5 | 1303 |
| 103 | UAB | American Athletic | -9.4 | -5.0 | -3.4 | -0.0 | -1.0 | 1427 |
| 104 | Georgia Southern | Sun Belt | -9.5 | -2.1 | -6.0 | -1.0 | -0.3 | 1481 |
| 105 | Western Kentucky | Conference USA | -10.2 | -6.9 | -1.8 | -0.2 | -1.3 | 1399 |
| 106 | South Alabama | Sun Belt | -10.2 | +1.4 | -11.5 | +0.4 | -0.5 | 1468 |
| 107 | Utah State | Pac-12 | -10.3 | -8.3 | +0.7 | -1.3 | -1.4 | 1393 |
| 108 | Troy | Sun Belt | -10.4 | -5.8 | -2.3 | -1.2 | -1.1 | 1416 |
| 109 | Arkansas State | Sun Belt | -11.0 | -3.5 | -6.4 | -0.0 | -1.1 | 1416 |
| 110 | Florida International | Conference USA | -11.2 | -9.4 | -0.2 | -0.5 | -1.2 | 1411 |
| 111 | Delaware | Conference USA | -11.3 | -4.0 | -4.6 | -0.4 | -2.3 | 1316 |
| 112 | Colorado State | Pac-12 | -11.8 | +1.3 | -9.6 | -0.6 | -2.9 | 1271 |
| 113 | Wyoming | Mountain West | -12.1 | -7.3 | -2.8 | -0.2 | -1.8 | 1359 |
| 114 | Old Dominion | Sun Belt | -12.2 | -12.8 | +2.8 | -1.3 | -0.9 | 1431 |
| 115 | Missouri State | Conference USA | -12.3 | -2.6 | -6.2 | -0.8 | -2.7 | 1289 |
| 116 | Kennesaw State | Conference USA | -12.6 | -5.0 | -4.7 | -0.7 | -2.2 | 1327 |
| 117 | Hawai'i | Mountain West | -13.6 | -6.2 | -5.8 | +0.6 | -2.2 | 1326 |
| 118 | Nevada | Mountain West | -13.6 | -8.2 | -3.2 | +0.4 | -2.6 | 1292 |
| 119 | Coastal Carolina | Sun Belt | -13.7 | -5.9 | -6.0 | +0.4 | -2.1 | 1332 |
| 120 | Central Michigan | Mid-American | -14.3 | -7.2 | -5.3 | -0.4 | -1.5 | 1386 |
| 121 | San José State | Mountain West | -14.3 | -7.8 | -4.4 | -0.3 | -1.8 | 1356 |
| 122 | New Mexico State | Conference USA | -14.5 | -7.6 | -2.8 | -1.2 | -2.8 | 1281 |
| 123 | Rice | American Athletic | -14.9 | -6.3 | -4.7 | -0.8 | -3.1 | 1252 |
| 124 | Southern Miss | Sun Belt | -15.3 | -6.5 | -4.2 | -1.5 | -3.1 | 1254 |
| 125 | Massachusetts | Mid-American | -16.7 | -8.7 | -4.5 | -0.1 | -3.4 | 1230 |
| 126 | Northern Illinois | Mountain West | -16.8 | -5.0 | -7.2 | -0.8 | -3.9 | 1188 |
| 127 | Eastern Michigan | Mid-American | -17.1 | -6.7 | -7.6 | -0.8 | -2.1 | 1337 |
| 128 | Middle Tennessee | Conference USA | -17.2 | -6.8 | -7.4 | -0.2 | -2.8 | 1275 |
| 129 | Sam Houston | Conference USA | -17.6 | -11.3 | -1.0 | -1.5 | -3.7 | 1199 |
| 130 | Ball State | Mid-American | -18.4 | -6.4 | -7.5 | -1.1 | -3.4 | 1230 |
| 131 | Bowling Green | Mid-American | -18.5 | -12.2 | -3.5 | -0.2 | -2.6 | 1294 |
| 132 | Buffalo | Mid-American | -18.9 | -13.7 | -4.9 | +0.6 | -1.0 | 1429 |
| 133 | Kent State | Mid-American | -20.2 | -10.4 | -6.1 | -1.0 | -2.6 | 1290 |
| 134 | UL Monroe | Sun Belt | -20.5 | -6.3 | -8.2 | -1.5 | -4.5 | 1139 |
| 135 | Sacramento State | Mid-American | -20.7 | -9.9 | -6.2 | +0.4 | -5.0 | 1095 |
| 136 | Charlotte | American Athletic | -20.9 | -8.6 | -8.3 | -0.4 | -3.6 | 1211 |
| 137 | Akron | Mid-American | -22.0 | -10.8 | -6.8 | -1.2 | -3.3 | 1233 |
| 138 | UTEP | Mountain West | -24.1 | -12.0 | -6.1 | -1.4 | -4.7 | 1123 |

## Current model fit

- Fitted on 4127 games from seasons 2022–2026.
- Home field on top of the ratings: 3.2 points (1.8 in conference games).
- Extra FBS edge over FCS opponents beyond their ratings: 14.0 points.
- Elo weight: 0.19 points of margin per point of Elo spread.
- Weight on the betting line: 89% for the margin, 78% for the total.
