# College football score predictions

Updated Wed Oct 28, 2026 03:02 PM ET. Refreshed automatically every day of the season and several times on Saturdays; each game's prediction is locked at kickoff and graded once the final score is in. Scores are the most likely real scoreline near the expected points; ranges cover 80% of simulated outcomes for each team. College scores scatter widely, so read the ranges, not just the headline score.

Expected points blend the model with the betting line using the weight that has predicted best in recent seasons (see Current model fit). The spread and total columns show the model's own numbers next to the line, so you can see where it disagrees. Games without a line yet use the model alone.

The fair moneyline is the American odds that match the win chance exactly, with no bookmaker margin: -200 means risk $200 to win $100, +200 means risk $100 to win $200. A sportsbook's price will be a little worse on both sides because of its cut, so a book only offers value on a team when its price beats the fair line.

The edge columns judge each bet by its expected value per $1 staked at the posted price, using the final prediction: the model blended with the line, run through the score simulator, pushes included, and anchored to the market's own chances so that only what the blend moves off the line counts. The model's own spread and total (shown alongside) sit several points from the line in most games, but the blend keeps only the share of that disagreement the model has earned in past seasons, so edges are rare. The side with the higher value is shown when it reaches 3% (+3 cents per $1), as the team or side, the price, the expected value, its chance of winning the bet and its stake, a 25% share of the Kelly stake in units of 1% of the bankroll with at most 3 units on one game; anything short is no edge. Where a book posts no price for a spread or total it is assumed to be -110 and marked -110*; moneylines are never assumed. In the walk-forward backtest against closing lines, edges returned spread -100.0% on 1 bets (posted prices, 2016–2019); spread -3.9% on 156 bets (assumed -110 prices, 2016–2025); moneyline +13.7% on 575 bets (posted prices, 2016–2025); total +2.6% on 367 bets (posted prices, 2016–2019); total -5.7% on 172 bets (assumed -110 prices, 2016–2025). None of these is clearly above zero, so treat these edges as an experiment, not a betting system. The live record is tracked below, graded at the price logged with the last prediction before kickoff.

## 2026 Week 9

| Kickoff (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected points | 80% range | Spread: model / line | Total: model / line | Spread edge | Moneyline edge | Total edge | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Wed 10/28 7:00 PM | Kennesaw State @ Middle Tennessee | Kennesaw State 27, Middle Tennessee 24 | Kennesaw State 53% | Kennesaw State -115 / Middle Tennessee +115 | 25.3 – 24.4 | 13–38 / 10–38 | Middle Tennessee -3.3 / Kennesaw State -1.2 | 50.5 / 49.5 | no edge | no edge | no edge |  |
| Wed 10/28 8:00 PM | Jacksonville State @ New Mexico State | Jacksonville State 27, New Mexico State 24 | Jacksonville State 59% | Jacksonville State -145 / New Mexico State +145 | 26.5 – 23.2 | 13–41 / 10–37 | Jacksonville State -6.5 / Jacksonville State -3.0 | 50.8 / 49.5 | no edge | no edge | no edge |  |
| Thu 10/29 7:30 PM | Florida Atlantic @ North Texas | Florida Atlantic 31, North Texas 45 | North Texas 79% | Florida Atlantic +380 / North Texas -380 | 31.1 – 44.5 | 17–46 / 30–59 | North Texas -9.2 / North Texas -13.8 | 71.7 / 76.5 | no edge | no edge | no edge |  |
| Thu 10/29 7:30 PM | Troy @ James Madison | Troy 14, James Madison 35 | James Madison 92% | Troy +1195 / James Madison -1195 | 14.6 – 35.1 | 3–27 / 20–51 | James Madison -20.5 / James Madison -20.5 | 50.1 / 49.5 | no edge | no edge | no edge |  |
| Fri 10/30 7:00 PM | Tulane @ Charlotte | Tulane 27, Charlotte 17 | Tulane 76% | Tulane -315 / Charlotte +315 | 28.9 – 18.5 | 14–43 / 7–31 | Tulane -14.4 / Tulane -10.0 | 47.9 / 47.2 | no edge | no edge | no edge |  |
| Fri 10/30 7:30 PM | Baylor @ UCF | Baylor 24, UCF 27 | UCF 54% | Baylor +120 / UCF -120 | 23.5 – 24.9 | 10–38 / 13–38 | UCF -0.2 / UCF -1.5 | 52.4 / 47.5 | no edge | no edge | no edge |  |
| Fri 10/30 10:30 PM | Kent State @ Sacramento State | Kent State 27, Sacramento State 17 | Kent State 73% | Kent State -270 / Sacramento State +270 | 27.9 – 19.0 | 14–42 / 7–31 | Sacramento State -0.5 / Kent State -9.8 | 48.4 / 46.5 | no edge | Sacramento State (+310): EV +4.6%, 26%, stake 0.4u | no edge |  |
| Sat 10/31 12:00 PM | Arizona @ Texas Tech | Arizona 24, Texas Tech 27 | Texas Tech 59% | Arizona +145 / Texas Tech -145 | 24.8 – 28.6 | 11–38 / 14–43 | Texas Tech -8.1 / Texas Tech -3.5 | 48.9 / 54.5 | no edge | no edge | no edge |  |
| Sat 10/31 12:00 PM | California @ NC State | California 24, NC State 31 | NC State 69% | California +220 / NC State -220 | 25.1 – 32.4 | 13–38 / 17–48 | NC State -10.8 / NC State -7.0 | 60.5 / 56.8 | no edge | no edge | no edge |  |
| Sat 10/31 12:00 PM | SMU @ Syracuse | SMU 31, Syracuse 24 | SMU 74% | SMU -280 / Syracuse +280 | 33.8 – 23.9 | 20–49 / 10–38 | SMU -9.1 / SMU -10.0 | 54.8 / 58.5 | no edge | no edge | no edge |  |
| Sat 10/31 12:00 PM | Boston College @ Duke | Boston College 20, Duke 27 | Duke 69% | Boston College +225 / Duke -225 | 20.4 – 27.9 | 7–34 / 14–42 | Duke -12.5 / Duke -7.0 | 50.4 / 47.8 | no edge | no edge | no edge |  |
| Sat 10/31 12:00 PM | Wisconsin @ Iowa | Wisconsin 17, Iowa 20 | Iowa 60% | Wisconsin +155 / Iowa -155 | 17.0 – 20.5 | 6–28 / 7–34 | Iowa -4.1 / Iowa -3.5 | 41.4 / 36.5 | no edge | no edge | no edge |  |
| Sat 10/31 12:00 PM | Illinois @ Maryland | Illinois 27, Maryland 24 | Illinois 56% | Illinois -125 / Maryland +125 | 28.4 – 26.1 | 14–42 / 13–40 | Maryland -0.4 / Illinois -2.5 | 54.4 / 54.5 | no edge | no edge | no edge |  |
| Sat 10/31 12:00 PM | Notre Dame vs Navy | Notre Dame 45, Navy 13 | Notre Dame 98% | Notre Dame -5925 / Navy +5925 | 42.9 – 12.7 | 28–59 / 3–23 | Notre Dame -27.9 / Notre Dame -30.5 | 50.9 / 56.8 | no edge | no edge | no edge | neutral site |
| Sat 10/31 12:00 PM | UAB @ South Florida | UAB 17, South Florida 24 | South Florida 71% | UAB +245 / South Florida -245 | 17.9 – 25.8 | 7–30 / 13–40 | South Florida -10.1 / South Florida -7.8 | 50.5 / 42.5 | no edge | no edge | no edge |  |
| Sat 10/31 12:00 PM | Bowling Green @ Western Michigan | Bowling Green 17, Western Michigan 31 | Western Michigan 82% | Bowling Green +450 / Western Michigan -450 | 15.6 – 28.5 | 3–27 / 14–43 | Western Michigan -15.5 / Western Michigan -12.8 | 44.5 / 44.0 | no edge | no edge | no edge |  |
| Sat 10/31 12:30 PM | Michigan @ Rutgers | Michigan 31, Rutgers 17 | Michigan 84% | Michigan -525 / Rutgers +525 | 30.6 – 16.5 | 17–45 / 6–28 | Michigan -15.2 / Michigan -14.0 | 49.8 / 46.5 | no edge | no edge | no edge |  |
| Sat 10/31 12:45 PM | Auburn @ Ole Miss | Auburn 24, Ole Miss 38 | Ole Miss 80% | Auburn +410 / Ole Miss -410 | 22.4 – 35.2 | 10–36 / 21–51 | Ole Miss -8.1 / Ole Miss -13.2 | 58.1 / 57.5 | no edge | no edge | no edge |  |
| Sat 10/31 1:00 PM | Marshall @ Old Dominion | Marshall 24, Old Dominion 21 | Marshall 57% | Marshall -135 / Old Dominion +135 | 23.6 – 20.8 | 10–37 / 9–34 | Marshall -5.8 / Marshall -2.5 | 47.1 / 43.8 | no edge | no edge | no edge |  |
| Sat 10/31 2:00 PM | Kansas State @ Colorado | Kansas State 24, Colorado 21 | Kansas State 54% | Kansas State -120 / Colorado +120 | 25.1 – 23.4 | 13–38 / 10–37 | Kansas State -6.6 / Kansas State -1.2 | 52.3 / 47.5 | no edge | no edge | no edge |  |
| Sat 10/31 2:00 PM | Coastal Carolina @ Georgia State | Coastal Carolina 24, Georgia State 31 | Georgia State 67% | Coastal Carolina +200 / Georgia State -200 | 25.5 – 32.0 | 13–39 / 17–48 | Georgia State -6.6 / Georgia State -6.5 | 56.8 / 57.8 | no edge | no edge | no edge |  |
| Sat 10/31 3:00 PM | UConn @ Air Force | UConn 24, Air Force 27 | Air Force 53% | UConn +110 / Air Force -110 | 26.0 – 27.2 | 13–40 / 14–41 | Air Force -1.4 / Air Force -1.2 | 59.0 / 51.8 | no edge | no edge | no edge |  |
| Sat 10/31 3:00 PM | Temple @ East Carolina | Temple 24, East Carolina 27 | East Carolina 66% | Temple +195 / East Carolina -195 | 22.0 – 28.2 | 10–35 / 14–42 | East Carolina -8.4 / East Carolina -6.0 | 52.4 / 49.8 | no edge | no edge | no edge |  |
| Sat 10/31 3:00 PM | Louisiana Tech @ South Alabama | Louisiana Tech 31, South Alabama 24 | Louisiana Tech 64% | Louisiana Tech -175 / South Alabama +175 | 31.8 – 26.5 | 17–46 / 13–41 | Louisiana Tech -4.2 / Louisiana Tech -5.5 | 57.5 / 58.5 | no edge | no edge | no edge |  |
| Sat 10/31 3:15 PM | Stanford @ Louisville | Stanford 17, Louisville 41 | Louisville 93% | Stanford +1440 / Louisville -1440 | 18.3 – 41.2 | 7–31 / 27–57 | Louisville -26.9 / Louisville -22.5 | 56.2 / 60.2 | no edge | no edge | no edge |  |
| Sat 10/31 3:30 PM | Florida vs Georgia | Florida 21, Georgia 31 | Georgia 78% | Florida +355 / Georgia -355 | 21.9 – 33.4 | 9–35 / 20–49 | Georgia -9.1 / Georgia -11.8 | 53.2 / 55.8 | no edge | no edge | no edge | neutral site |
| Sat 10/31 3:30 PM | Arizona State @ BYU | Arizona State 17, BYU 34 | BYU 86% | Arizona State +635 / BYU -635 | 16.5 – 32.4 | 6–28 / 17–48 | BYU -12.1 / BYU -16.2 | 50.5 / 48.5 | no edge | no edge | no edge |  |
| Sat 10/31 3:30 PM | Kansas @ TCU | Kansas 21, TCU 24 | TCU 64% | Kansas +180 / TCU -180 | 20.9 – 26.4 | 9–34 / 13–40 | PK / TCU -6.0 | 49.8 / 46.8 | no edge | no edge | no edge |  |
| Sat 10/31 3:30 PM | Minnesota @ Indiana | Minnesota 10, Indiana 31 | Indiana 94% | Minnesota +1680 / Indiana -1680 | 10.1 – 30.9 | 0–20 / 17–45 | Indiana -20.7 / Indiana -20.8 | 38.8 / 41.5 | no edge | no edge | no edge |  |
| Sat 10/31 3:30 PM | Northwestern @ Oregon | Northwestern 21, Oregon 24 | Oregon 59% | Northwestern +145 / Oregon -145 | 22.2 – 25.9 | 10–35 / 13–40 | Oregon -6.1 / Oregon -3.5 | 50.5 / 47.5 | no edge | no edge | no edge |  |
| Sat 10/31 3:30 PM | Colorado State @ Utah State | Colorado State 28, Utah State 35 | Utah State 65% | Colorado State +185 / Utah State -185 | 27.9 – 34.1 | 14–42 / 20–49 | Utah State -3.0 / Utah State -6.5 | 57.1 / 63.2 | no edge | no edge | no edge |  |
| Sat 10/31 3:30 PM | UTEP @ North Dakota State | UTEP 10, North Dakota State 34 | North Dakota State 97% | UTEP +3235 / North Dakota State -3235 | 9.0 – 33.5 | 0–18 / 20–49 | North Dakota State -27.5 / North Dakota State -24.2 | 41.3 / 42.8 | no edge | no edge | no edge |  |
| Sat 10/31 3:30 PM | Florida International @ Liberty | Florida International 17, Liberty 31 | Liberty 83% | Florida International +500 / Liberty -500 | 15.5 – 29.6 | 3–28 / 16–45 | Liberty -15.2 / Liberty -14.0 | 46.6 / 44.8 | no edge | no edge | no edge |  |
| Sat 10/31 3:30 PM | Southern Miss @ UL Monroe | Southern Miss 27, UL Monroe 24 | Southern Miss 58% | Southern Miss -140 / UL Monroe +140 | 29.4 – 26.1 | 16–44 / 13–41 | Southern Miss -1.7 / Southern Miss -3.5 | 54.4 / 55.8 | no edge | no edge | no edge |  |
| Sat 10/31 3:45 PM | Utah @ Cincinnati | Utah 31, Cincinnati 24 | Utah 66% | Utah -195 / Cincinnati +195 | 32.0 – 25.4 | 17–47 / 13–40 | Utah -7.5 / Utah -6.5 | 60.3 / 56.8 | no edge | no edge | no edge |  |
| Sat 10/31 3:45 PM | Virginia @ Wake Forest | Virginia 17, Wake Forest 31 | Wake Forest 81% | Virginia +435 / Wake Forest -435 | 18.3 – 31.0 | 7–31 / 17–46 | Wake Forest -15.3 / Wake Forest -12.5 | 48.3 / 49.5 | no edge | no edge | no edge |  |
| Sat 10/31 4:00 PM | New Mexico @ San José State | New Mexico 31, San José State 14 | New Mexico 85% | New Mexico -585 / San José State +585 | 29.0 – 14.3 | 14–44 / 3–26 | New Mexico -13.7 / New Mexico -14.8 | 47.7 / 42.2 | no edge | no edge | no edge |  |
| Sat 10/31 4:15 PM | South Carolina @ Oklahoma | South Carolina 17, Oklahoma 24 | Oklahoma 64% | South Carolina +180 / Oklahoma -180 | 19.6 – 24.8 | 7–32 / 11–38 | Oklahoma -10.8 / Oklahoma -4.8 | 44.9 / 44.2 | no edge | no edge | no edge |  |
| Sat 10/31 4:15 PM | Purdue @ Penn State | Purdue 24, Penn State 31 | Penn State 71% | Purdue +245 / Penn State -245 | 22.8 – 30.9 | 10–36 / 17–45 | Penn State -12.1 / Penn State -7.8 | 50.7 / 54.5 | no edge | no edge | no edge |  |
| Sat 10/31 4:15 PM | Nevada @ UCLA | Nevada 10, UCLA 34 | UCLA 96% | Nevada +2410 / UCLA -2410 | 10.6 – 34.2 | 0–20 / 20–50 | UCLA -32.9 / UCLA -22.8 | 45.8 / 44.5 | no edge | no edge | no edge |  |
| Sat 10/31 6:30 PM | App State @ Georgia Southern | App State 24, Georgia Southern 31 | Georgia Southern 63% | App State +170 / Georgia Southern -170 | 25.4 – 30.4 | 13–40 / 17–45 | App State -0.9 / Georgia Southern -5.5 | 57.5 / 55.8 | no edge | no edge | no edge |  |
| Sat 10/31 7:00 PM | Oklahoma State @ Iowa State | Oklahoma State 31, Iowa State 24 | Oklahoma State 70% | Oklahoma State -240 / Iowa State +240 | 32.6 – 24.4 | 17–48 / 10–38 | Iowa State -2.8 / Oklahoma State -9.2 | 55.1 / 57.5 | no edge | Iowa State (+285): EV +3.9%, 27%, stake 0.3u | no edge |  |
| Sat 10/31 7:00 PM | Clemson @ Florida State | Clemson 24, Florida State 27 | Florida State 65% | Clemson +185 / Florida State -185 | 22.1 – 27.8 | 10–35 / 14–42 | Florida State -4.8 / Florida State -5.8 | 51.2 / 49.5 | no edge | no edge | no edge |  |
| Sat 10/31 7:00 PM | Washington State @ San Diego State | Washington State 21, San Diego State 24 | San Diego State 57% | Washington State +130 / San Diego State -130 | 22.8 – 25.3 | 10–36 / 13–39 | San Diego State -2.7 / San Diego State -2.5 | 47.5 / 48.2 | no edge | no edge | no edge |  |
| Sat 10/31 7:30 PM | Mississippi State @ Texas | Mississippi State 17, Texas 38 | Texas 91% | Mississippi State +1030 / Texas -1030 | 15.5 – 35.2 | 3–27 / 20–51 | Texas -11.4 / Texas -20.5 | 51.4 / 50.5 | no edge | Mississippi State (+824): EV +10.2%, 12%, stake 0.3u | no edge |  |
| Sat 10/31 7:30 PM | Georgia Tech @ Pittsburgh | Georgia Tech 24, Pittsburgh 31 | Pittsburgh 69% | Georgia Tech +225 / Pittsburgh -225 | 23.3 – 31.1 | 10–37 / 17–45 | Pittsburgh -10.2 / Pittsburgh -7.5 | 55.0 / 54.2 | no edge | no edge | no edge |  |
| Sat 10/31 7:30 PM | Miami @ North Carolina | Miami 34, North Carolina 17 | Miami 84% | Miami -520 / North Carolina +520 | 33.8 – 19.3 | 20–49 / 7–31 | Miami -20.2 / Miami -14.0 | 54.8 / 52.8 | no edge | no edge | no edge |  |
| Sat 10/31 7:30 PM | Ohio State @ USC | Ohio State 31, USC 24 | Ohio State 69% | Ohio State -220 / USC +220 | 29.7 – 22.7 | 16–45 / 10–35 | Ohio State -12.0 / Ohio State -6.5 | 55.9 / 51.5 | no edge | no edge | no edge |  |
| Sat 10/31 7:45 PM | Missouri @ Arkansas | Missouri 27, Arkansas 17 | Missouri 75% | Missouri -310 / Arkansas +310 | 29.8 – 19.6 | 16–45 / 7–32 | Missouri -12.5 / Missouri -10.0 | 49.3 / 49.5 | no edge | no edge | no edge |  |
| Sat 10/31 8:00 PM | Washington @ Nebraska | Washington 21, Nebraska 28 | Nebraska 70% | Washington +230 / Nebraska -230 | 21.0 – 28.6 | 7–34 / 14–43 | Nebraska -8.9 / Nebraska -7.5 | 48.9 / 49.8 | no edge | no edge | no edge |  |
| Sat 10/31 8:00 PM | Army @ Memphis | Army 24, Memphis 31 | Memphis 65% | Army +185 / Memphis -185 | 27.2 – 33.1 | 13–42 / 19–48 | Memphis -5.6 / Memphis -6.0 | 60.4 / 60.2 | no edge | no edge | no edge |  |
| Sat 10/31 10:00 PM | Texas State @ Boise State | Texas State 28, Boise State 38 | Boise State 76% | Texas State +320 / Boise State -320 | 26.2 – 37.5 | 13–41 / 23–52 | Boise State -12.4 / Boise State -11.2 | 63.7 / 63.8 | no edge | no edge | no edge |  |
| Sat 10/31 10:30 PM | Northern Illinois @ UNLV | Northern Illinois 14, UNLV 38 | UNLV 95% | Northern Illinois +1900 / UNLV -1900 | 15.2 – 38.9 | 3–27 / 24–55 | UNLV -17.4 / UNLV -24.2 | 53.6 / 54.2 | no edge | no edge | no edge |  |
| Sat 10/31 11:00 PM | Oregon State @ Fresno State | Oregon State 31, Fresno State 24 | Oregon State 64% | Oregon State -180 / Fresno State +180 | 31.5 – 25.9 | 17–46 / 13–40 | Oregon State -3.7 / Oregon State -5.8 | 56.2 / 57.8 | no edge | no edge | no edge |  |

## 2026 Week 10

| Kickoff (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected points | 80% range | Spread: model / line | Total: model / line | Spread edge | Moneyline edge | Total edge | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tue 11/03 7:00 PM | Ohio @ Akron | Ohio 34, Akron 17 | Ohio 89% | Ohio -825 / Akron +825 | 34.1 – 15.7 | 20–49 / 6–28 | Ohio -18.4 / – | 49.9 / – | no line yet | no line yet (fair: Ohio -825) | no line yet |  |
| Tue 11/03 7:00 PM | Buffalo @ Miami (OH) | Buffalo 17, Miami (OH) 31 | Miami (OH) 80% | Buffalo +410 / Miami (OH) -410 | 18.1 – 30.5 | 7–31 / 17–45 | Miami (OH) -12.4 / – | 48.6 / – | no line yet | no line yet (fair: Miami (OH) -410) | no line yet |  |
| Wed 11/04 TBA | Ball State @ Massachusetts | Ball State 24, Massachusetts 27 | Massachusetts 58% | Ball State +135 / Massachusetts -135 | 23.1 – 26.0 | 10–37 / 13–41 | Massachusetts -2.9 / – | 49.0 / – | no line yet | no line yet (fair: Massachusetts -135) | no line yet |  |
| Wed 11/04 TBA | Central Michigan vs Eastern Michigan | Central Michigan 27, Eastern Michigan 24 | Central Michigan 60% | Central Michigan -155 / Eastern Michigan +155 | 26.6 – 23.0 | 13–41 / 10–37 | Central Michigan -3.7 / – | 49.6 / – | no line yet | no line yet (fair: Central Michigan -155) | no line yet | neutral site |
| Wed 11/04 TBA | Toledo @ Sacramento State | Toledo 34, Sacramento State 17 | Toledo 90% | Toledo -935 / Sacramento State +935 | 35.4 – 16.2 | 20–51 / 6–28 | Toledo -19.2 / – | 51.6 / – | no line yet | no line yet (fair: Toledo -935) | no line yet |  |
| Thu 11/05 8:00 PM | UTSA @ Florida Atlantic | UTSA 34, Florida Atlantic 31 | UTSA 58% | UTSA -140 / Florida Atlantic +140 | 34.0 – 30.8 | 20–49 / 17–45 | UTSA -3.1 / – | 65.3 / – | no line yet | no line yet (fair: UTSA -140) | no line yet |  |
| Thu 11/05 8:00 PM | James Madison @ Southern Miss | James Madison 34, Southern Miss 17 | James Madison 87% | James Madison -695 / Southern Miss +695 | 36.0 – 18.9 | 21–52 / 7–31 | James Madison -17.2 / – | 54.9 / – | no line yet | no line yet (fair: James Madison -695) | no line yet |  |
| Fri 11/06 7:00 PM | Virginia Tech @ SMU | Virginia Tech 21, SMU 31 | SMU 76% | Virginia Tech +310 / SMU -310 | 22.0 – 32.4 | 10–35 / 17–48 | SMU -10.4 / – | 54.4 / – | no line yet | no line yet (fair: SMU -310) | no line yet |  |
| Fri 11/06 7:30 PM | South Florida @ East Carolina | South Florida 24, East Carolina 27 | East Carolina 51% | South Florida +100 / East Carolina -100 | 24.7 – 24.7 | 12–38 / 12–38 | PK / – | 49.4 / – | no line yet | no line yet (fair: East Carolina -100) | no line yet |  |
| Fri 11/06 8:00 PM | Nebraska @ Illinois | Nebraska 31, Illinois 24 | Nebraska 71% | Nebraska -240 / Illinois +240 | 31.2 – 23.1 | 17–45 / 10–37 | Nebraska -8.1 / – | 54.3 / – | no line yet | no line yet (fair: Nebraska -240) | no line yet |  |
| Fri 11/06 9:00 PM | New Mexico @ Nevada | New Mexico 27, Nevada 17 | New Mexico 75% | New Mexico -305 / Nevada +305 | 27.2 – 17.5 | 14–42 / 7–30 | New Mexico -9.7 / – | 44.7 / – | no line yet | no line yet (fair: New Mexico -305) | no line yet |  |
| Fri 11/06 10:15 PM | TCU @ Arizona | TCU 21, Arizona 31 | Arizona 74% | TCU +285 / Arizona -285 | 19.5 – 29.4 | 7–32 / 14–44 | Arizona -9.9 / – | 48.9 / – | no line yet | no line yet (fair: Arizona -285) | no line yet |  |
| Sat 11/07 TBA | Arkansas @ Auburn | Arkansas 17, Auburn 34 | Auburn 83% | Arkansas +505 / Auburn -505 | 18.9 – 33.8 | 7–31 / 19–49 | Auburn -14.8 / – | 52.7 / – | no line yet | no line yet (fair: Auburn -505) | no line yet |  |
| Sat 11/07 TBA | Oklahoma @ Florida | Oklahoma 27, Florida 24 | Oklahoma 52% | Oklahoma -105 / Florida +105 | 23.6 – 23.0 | 10–37 / 10–37 | Oklahoma -0.6 / – | 46.6 / – | no line yet | no line yet (fair: Oklahoma -105) | no line yet |  |
| Sat 11/07 TBA | Alabama @ LSU | Alabama 24, LSU 27 | LSU 60% | Alabama +150 / LSU -150 | 24.8 – 28.8 | 10–38 / 14–43 | LSU -9.2 / LSU -3.5 | 50.1 / 54.5 | no edge | no edge | no edge |  |
| Sat 11/07 TBA | Georgia @ Ole Miss | Georgia 27, Ole Miss 24 | Georgia 62% | Georgia -160 / Ole Miss +160 | 29.9 – 25.5 | 16–45 / 13–39 | Georgia -3.0 / Georgia -4.5 | 55.3 / 55.5 | no edge | no edge | no edge |  |
| Sat 11/07 TBA | Vanderbilt @ Mississippi State | Vanderbilt 24, Mississippi State 31 | Mississippi State 70% | Vanderbilt +230 / Mississippi State -230 | 24.4 – 32.5 | 10–38 / 17–48 | Mississippi State -8.1 / – | 57.0 / – | no line yet | no line yet (fair: Mississippi State -230) | no line yet |  |
| Sat 11/07 TBA | Texas @ Missouri | Texas 24, Missouri 21 | Texas 52% | Texas -110 / Missouri +110 | 22.8 – 21.8 | 10–36 / 10–35 | Texas -1.0 / – | 44.6 / – | no line yet | no line yet (fair: Texas -110) | no line yet |  |
| Sat 11/07 TBA | Texas A&M @ South Carolina | Texas A&M 27, South Carolina 24 | Texas A&M 52% | Texas A&M -105 / South Carolina +105 | 24.6 – 24.4 | 13–38 / 10–38 | Texas A&M -0.2 / – | 49.0 / – | no line yet | no line yet (fair: Texas A&M -105) | no line yet |  |
| Sat 11/07 TBA | Kentucky @ Tennessee | Kentucky 21, Tennessee 31 | Tennessee 72% | Kentucky +260 / Tennessee -260 | 19.8 – 28.5 | 7–33 / 14–43 | Tennessee -8.6 / – | 48.3 / – | no line yet | no line yet (fair: Tennessee -260) | no line yet |  |
| Sat 11/07 TBA | BYU @ Utah | BYU 24, Utah 27 | Utah 59% | BYU +145 / Utah -145 | 24.2 – 27.5 | 10–38 / 14–42 | Utah -6.1 / Utah -3.0 | 52.8 / 51.5 | no edge | no edge | no edge |  |
| Sat 11/07 TBA | UCF @ Kansas | UCF 24, Kansas 27 | Kansas 62% | UCF +165 / Kansas -165 | 24.3 – 28.9 | 10–38 / 14–44 | Kansas -4.6 / – | 53.2 / – | no line yet | no line yet (fair: Kansas -165) | no line yet |  |
| Sat 11/07 TBA | Cincinnati @ Houston | Cincinnati 31, Houston 34 | Houston 61% | Cincinnati +160 / Houston -160 | 28.9 – 33.3 | 14–44 / 19–48 | Houston -4.4 / – | 62.3 / – | no line yet | no line yet (fair: Houston -160) | no line yet |  |
| Sat 11/07 TBA | Colorado @ Arizona State | Colorado 24, Arizona State 27 | Arizona State 68% | Colorado +210 / Arizona State -210 | 22.0 – 28.3 | 10–35 / 14–42 | Arizona State -6.3 / – | 50.3 / – | no line yet | no line yet (fair: Arizona State -210) | no line yet |  |
| Sat 11/07 TBA | Iowa State @ Baylor | Iowa State 24, Baylor 27 | Baylor 59% | Iowa State +145 / Baylor -145 | 24.0 – 27.2 | 10–38 / 14–41 | Baylor -3.1 / – | 51.2 / – | no line yet | no line yet (fair: Baylor -145) | no line yet |  |
| Sat 11/07 TBA | Oklahoma State @ Kansas State | Oklahoma State 24, Kansas State 31 | Kansas State 66% | Oklahoma State +190 / Kansas State -190 | 26.2 – 32.3 | 13–41 / 17–48 | Kansas State -6.1 / – | 58.5 / – | no line yet | no line yet (fair: Kansas State -190) | no line yet |  |
| Sat 11/07 TBA | West Virginia @ Texas Tech | West Virginia 17, Texas Tech 38 | Texas Tech 91% | West Virginia +1055 / Texas Tech -1055 | 17.5 – 37.7 | 6–30 / 23–54 | Texas Tech -20.2 / – | 56.1 / – | no line yet | no line yet (fair: Texas Tech -1055) | no line yet |  |
| Sat 11/07 TBA | Clemson @ Syracuse | Clemson 21, Syracuse 24 | Syracuse 50% | Clemson +100 / Syracuse -100 | 23.8 – 24.0 | 10–38 / 10–38 | Syracuse -0.2 / – | 47.9 / – | no line yet | no line yet (fair: Syracuse -100) | no line yet |  |
| Sat 11/07 TBA | Duke @ NC State | Duke 31, NC State 28 | Duke 52% | Duke -110 / NC State +110 | 29.6 – 28.6 | 16–44 / 14–43 | Duke -1.0 / – | 58.2 / – | no line yet | no line yet (fair: Duke -110) | no line yet |  |
| Sat 11/07 TBA | Louisville @ Georgia Tech | Louisville 38, Georgia Tech 20 | Louisville 86% | Louisville -610 / Georgia Tech +610 | 37.4 – 20.9 | 22–53 / 7–34 | Louisville -16.5 / – | 58.3 / – | no line yet | no line yet (fair: Louisville -610) | no line yet |  |
| Sat 11/07 TBA | Florida State @ Boston College | Florida State 31, Boston College 24 | Florida State 70% | Florida State -230 / Boston College +230 | 31.3 – 23.4 | 17–46 / 10–37 | Florida State -7.9 / – | 54.6 / – | no line yet | no line yet (fair: Florida State -230) | no line yet |  |
| Sat 11/07 TBA | Merrimack @ Wake Forest | Merrimack 3, Wake Forest 59 | Wake Forest 100% | Merrimack +9900 / Wake Forest -9900 | 3.0 – 58.4 | 0–7 / 44–73 | Wake Forest -55.4 / – | 61.4 / – | no line yet | no line yet (fair: Wake Forest -9900) | no line yet | FCS opponent |
| Sat 11/07 TBA | Michigan State @ Michigan | Michigan State 17, Michigan 34 | Michigan 87% | Michigan State +680 / Michigan -680 | 15.9 – 32.7 | 6–28 / 17–48 | Michigan -20.5 / Michigan -16.5 | 42.0 / 50.5 | no edge | no edge | Under 50.5 (-110*): EV +6.1%, 56%, stake 1.7u | * price not posted; assumed -110 |
| Sat 11/07 TBA | UCLA @ Minnesota | UCLA 24, Minnesota 17 | UCLA 77% | UCLA -335 / Minnesota +335 | 25.8 – 15.8 | 13–41 / 6–28 | UCLA -10.0 / – | 41.6 / – | no line yet | no line yet (fair: UCLA -335) | no line yet |  |
| Sat 11/07 TBA | Iowa @ Northwestern | Iowa 21, Northwestern 24 | Northwestern 59% | Iowa +145 / Northwestern -145 | 22.7 – 26.0 | 10–36 / 13–41 | Northwestern -3.3 / – | 48.7 / – | no line yet | no line yet (fair: Northwestern -145) | no line yet |  |
| Sat 11/07 TBA | Oregon @ Ohio State | Oregon 24, Ohio State 31 | Ohio State 67% | Oregon +205 / Ohio State -205 | 22.5 – 29.1 | 10–36 / 15–44 | Ohio State -13.6 / Ohio State -6.0 | 48.2 / 52.5 | no edge | no edge | no edge |  |
| Sat 11/07 TBA | Maryland @ Purdue | Maryland 24, Purdue 27 | Purdue 55% | Maryland +125 / Purdue -125 | 25.4 – 27.6 | 13–39 / 14–42 | Purdue -2.2 / – | 53.0 / – | no line yet | no line yet (fair: Purdue -125) | no line yet |  |
| Sat 11/07 TBA | Penn State @ Washington | Penn State 24, Washington 21 | Penn State 51% | Penn State -105 / Washington +105 | 23.6 – 23.1 | 10–37 / 10–37 | Penn State -0.6 / – | 46.7 / – | no line yet | no line yet (fair: Penn State -105) | no line yet |  |
| Sat 11/07 TBA | Rutgers @ Wisconsin | Rutgers 17, Wisconsin 34 | Wisconsin 86% | Rutgers +620 / Wisconsin -620 | 16.9 – 32.6 | 6–28 / 17–48 | Wisconsin -15.8 / – | 50.1 / – | no line yet | no line yet (fair: Wisconsin -620) | no line yet |  |
| Sat 11/07 TBA | Charlotte @ UAB | Charlotte 17, UAB 31 | UAB 84% | Charlotte +510 / UAB -510 | 17.7 – 32.2 | 7–30 / 17–48 | UAB -14.5 / – | 49.9 / – | no line yet | no line yet (fair: UAB -510) | no line yet |  |
| Sat 11/07 TBA | Rice @ North Texas | Rice 24, North Texas 41 | North Texas 89% | Rice +820 / North Texas -820 | 21.5 – 40.8 | 9–35 / 26–56 | North Texas -19.3 / – | 62.2 / – | no line yet | no line yet (fair: North Texas -820) | no line yet |  |
| Sat 11/07 TBA | Tulsa @ Tulane | Tulsa 24, Tulane 27 | Tulane 56% | Tulsa +125 / Tulane -125 | 24.4 – 26.6 | 10–38 / 13–41 | Tulane -2.1 / – | 51.0 / – | no line yet | no line yet (fair: Tulane -125) | no line yet |  |
| Sat 11/07 TBA | Hawai'i @ UTEP | Hawai'i 31, UTEP 17 | Hawai'i 80% | Hawai'i -405 / UTEP +405 | 31.1 – 18.8 | 17–46 / 7–31 | Hawai'i -12.3 / – | 49.8 / – | no line yet | no line yet (fair: Hawai'i -405) | no line yet |  |
| Sat 11/07 TBA | Northern Illinois @ San José State | Northern Illinois 24, San José State 31 | San José State 65% | Northern Illinois +190 / San José State -190 | 23.5 – 29.6 | 10–38 / 16–44 | San José State -6.0 / – | 53.1 / – | no line yet | no line yet (fair: San José State -190) | no line yet |  |
| Sat 11/07 TBA | Georgia State @ App State | Georgia State 28, App State 31 | App State 60% | Georgia State +150 / App State -150 | 27.6 – 31.5 | 14–42 / 17–46 | App State -4.0 / – | 59.1 / – | no line yet | no line yet (fair: App State -150) | no line yet |  |
| Sat 11/07 TBA | Old Dominion @ Coastal Carolina | Old Dominion 21, Coastal Carolina 24 | Coastal Carolina 62% | Old Dominion +165 / Coastal Carolina -165 | 19.9 – 24.6 | 7–33 / 10–38 | Coastal Carolina -4.7 / – | 44.5 / – | no line yet | no line yet (fair: Coastal Carolina -165) | no line yet |  |
| Sat 11/07 TBA | Marshall @ Georgia Southern | Marshall 31, Georgia Southern 28 | Marshall 54% | Marshall -120 / Georgia Southern +120 | 29.6 – 28.3 | 16–44 / 14–42 | Marshall -1.4 / – | 57.9 / – | no line yet | no line yet (fair: Marshall -120) | no line yet |  |
| Sat 11/07 TBA | South Alabama @ Louisiana | South Alabama 28, Louisiana 31 | Louisiana 60% | South Alabama +145 / Louisiana -145 | 27.6 – 31.2 | 14–42 / 17–46 | Louisiana -3.6 / – | 58.8 / – | no line yet | no line yet (fair: Louisiana -145) | no line yet |  |
| Sat 11/07 TBA | Louisiana Tech @ Troy | Louisiana Tech 28, Troy 21 | Louisiana Tech 68% | Louisiana Tech -215 / Troy +215 | 27.5 – 20.3 | 14–42 / 7–34 | Louisiana Tech -7.2 / – | 47.9 / – | no line yet | no line yet (fair: Louisiana Tech -215) | no line yet |  |
| Sat 11/07 12:00 PM | North Carolina @ UConn | North Carolina 31, UConn 28 | North Carolina 51% | North Carolina -100 / UConn +100 | 28.1 – 27.9 | 14–42 / 14–42 | North Carolina -0.2 / – | 55.9 / – | no line yet | no line yet (fair: North Carolina -100) | no line yet |  |
| Sat 11/07 3:00 PM | UL Monroe @ Arkansas State | UL Monroe 21, Arkansas State 31 | Arkansas State 79% | UL Monroe +370 / Arkansas State -370 | 20.4 – 32.6 | 7–34 / 17–48 | Arkansas State -12.1 / – | 53.0 / – | no line yet | no line yet (fair: Arkansas State -370) | no line yet |  |
| Sat 11/07 3:00 PM | Delaware @ Kennesaw State | Delaware 31, Kennesaw State 24 | Delaware 63% | Delaware -170 / Kennesaw State +170 | 30.0 – 25.0 | 16–44 / 13–39 | Delaware -5.0 / – | 55.1 / – | no line yet | no line yet (fair: Delaware -170) | no line yet |  |
| Sat 11/07 3:30 PM | Temple @ Navy | Temple 24, Navy 31 | Navy 74% | Temple +280 / Navy -280 | 23.1 – 32.9 | 10–37 / 19–48 | Navy -9.8 / – | 56.0 / – | no line yet | no line yet (fair: Navy -280) | no line yet |  |
| Sat 11/07 3:30 PM | Western Kentucky @ Middle Tennessee | Western Kentucky 27, Middle Tennessee 24 | Western Kentucky 55% | Western Kentucky -125 / Middle Tennessee +125 | 26.1 – 24.1 | 13–41 / 10–38 | Western Kentucky -1.9 / – | 50.2 / – | no line yet | no line yet (fair: Western Kentucky -125) | no line yet |  |
| Sat 11/07 4:00 PM | Missouri State @ Florida International | Missouri State 24, Florida International 27 | Florida International 61% | Missouri State +155 / Florida International -155 | 23.8 – 28.0 | 10–37 / 14–42 | Florida International -4.2 / – | 51.8 / – | no line yet | no line yet (fair: Florida International -155) | no line yet |  |
| Sat 11/07 5:00 PM | Liberty @ New Mexico State | Liberty 31, New Mexico State 17 | Liberty 79% | Liberty -380 / New Mexico State +380 | 29.9 – 18.0 | 16–45 / 7–31 | Liberty -11.9 / – | 47.9 / – | no line yet | no line yet (fair: Liberty -380) | no line yet |  |
| Sat 11/07 6:00 PM | Boise State @ Colorado State | Boise State 41, Colorado State 24 | Boise State 84% | Boise State -530 / Colorado State +530 | 39.1 – 23.9 | 24–55 / 10–38 | Boise State -15.2 / – | 63.1 / – | no line yet | no line yet (fair: Boise State -530) | no line yet |  |
| Sat 11/07 7:00 PM | Sam Houston @ Jacksonville State | Sam Houston 14, Jacksonville State 31 | Jacksonville State 86% | Sam Houston +615 / Jacksonville State -615 | 15.7 – 31.1 | 3–28 / 17–46 | Jacksonville State -15.4 / – | 46.7 / – | no line yet | no line yet (fair: Jacksonville State -615) | no line yet |  |
| Sat 11/07 7:30 PM | Miami @ Notre Dame | Miami 24, Notre Dame 31 | Notre Dame 67% | Miami +200 / Notre Dame -200 | 23.8 – 30.2 | 10–38 / 16–45 | Notre Dame -4.9 / Notre Dame -6.5 | 51.9 / 54.5 | no edge | no edge | no edge |  |
| Sat 11/07 7:30 PM | Air Force @ Army | Air Force 24, Army 31 | Army 65% | Air Force +190 / Army -190 | 26.8 – 33.0 | 14–41 / 18–48 | Army -6.3 / – | 59.8 / – | no line yet | no line yet (fair: Army -190) | no line yet |  |
| Sat 11/07 9:30 PM | Fresno State @ Utah State | Fresno State 24, Utah State 21 | Fresno State 61% | Fresno State -155 / Utah State +155 | 25.3 – 21.3 | 13–38 / 9–34 | Fresno State -4.0 / – | 46.6 / – | no line yet | no line yet (fair: Fresno State -155) | no line yet |  |
| Sat 11/07 10:30 PM | Texas State @ Oregon State | Texas State 31, Oregon State 38 | Oregon State 69% | Texas State +225 / Oregon State -225 | 29.7 – 37.6 | 16–44 / 23–53 | Oregon State -7.9 / – | 67.4 / – | no line yet | no line yet (fair: Oregon State -225) | no line yet |  |
| Sat 11/07 10:30 PM | Wyoming @ UNLV | Wyoming 21, UNLV 28 | UNLV 74% | Wyoming +285 / UNLV -285 | 20.1 – 29.0 | 7–33 / 14–44 | UNLV -9.0 / – | 49.1 / – | no line yet | no line yet (fair: UNLV -285) | no line yet |  |

## How the 2026 predictions have done

| Predictor | Games | Margin MAE | Total MAE | Team-score MAE | Winners | Brier | 80% range hit |
|---|---|---|---|---|---|---|---|
| Final prediction | 566 | 11.55 | 12.25 | 8.38 | 80.2% | 0.137 | 82.4% |
| Model only (before blending) | 566 | 12.35 | 12.56 | 8.68 | 77.9% | – | – |
| Betting line when predicted | 564 | 11.54 | 12.20 | 8.37 | 80.1% | – | – |

MAE is mean absolute error in points (lower is better). Brier scores the win chances (lower is better, 0.25 is a coin flip). Even the closing betting line misses the final margin of an FBS game by about 12.5 points.

501 of these games were played before the predictor went live. They are backfilled walk-forward (each week predicted from earlier weeks only) but with closing lines, so they flatter the model slightly. Every game since is graded on the prediction logged before kickoff.

### Betting edges

| Market | Edges | Record (W-L-P) | Staked | Units won | ROI | Expected ROI |
|---|---|---|---|---|---|---|
| Spread | 0 | 0-0-0 | 0.0 | +0.00 | – | – |
| Moneyline | 2 | 0-2-0 | 0.7 | -0.68 | -100.0% | +5.8% |
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
| Texas A&M @ Alabama | 17–31 | 20–31 | 82% | yes |
| Oklahoma @ Mississippi State | 24–21 | 23–15 | 55% | yes |
| Tennessee @ South Carolina | 24–27 | 24–27 | 56% | yes |
| BYU @ UCF | 24–17 | 31–39 | 29% | no |
| Boston College @ Georgia Tech | 24–31 | 49–27 | 32% | no |
| Iowa @ Minnesota | 24–17 | 10–13 | 29% | yes |
| Michigan State @ UCLA | 14–31 | 10–28 | 89% | yes |
| North Texas @ Navy | 31–28 | 49–39 | 58% | no |
| Hawai'i @ Northern Illinois | 27–24 | 56–21 | 58% | no |
| Sacramento State @ Ball State | 17–31 | 17–34 | 82% | yes |
| Bowling Green @ Buffalo | 21–24 | 24–31 | 59% | yes |
| Kansas State @ Arizona State | 27–24 | 17–28 | 45% | yes |
| Eastern Michigan @ Ohio | 21–31 | 20–24 | 78% | yes |
| UL Monroe @ Troy | 17–31 | 21–14 | 18% | no |
| San José State @ Nevada | 21–24 | 13–28 | 64% | yes |
| Louisiana @ Southern Miss | 31–24 | 31–35 | 26% | yes |
| Old Dominion @ Louisiana Tech | 13–27 | 0–26 | 83% | no |
| Boise State @ Washington State | 31–17 | 31–10 | 83% | yes |
| San Diego State @ Colorado State | 31–28 | 49–56 | 48% | no |
| Colorado @ Oklahoma State | 20–34 | 24–57 | 80% | no |
| Virginia Tech @ Clemson | 24–27 | 20–16 | 42% | yes |
| Georgia State @ Arkansas State | 31–28 | 32–38 | 43% | yes |
| Vanderbilt @ Kentucky | 21–31 | 17–34 | 75% | yes |
| Ole Miss @ Texas | 24–27 | 27–34 | 57% | yes |
| Iowa State @ Arizona | 21–31 | 3–39 | 79% | no |
| Syracuse @ North Carolina | 21–28 | 31–30 | 27% | yes |
| USC @ Wisconsin | 27–24 | 7–24 | 44% | no |
| Utah State @ Texas State | 24–38 | 17–20 | 81% | no |
| UTSA @ Tulane | 27–24 | 42–19 | 58% | yes |
| North Dakota State @ New Mexico | 17–20 | 16–21 | 62% | yes |
| Houston @ Utah | 24–31 | 13–21 | 67% | yes |

## FBS power ratings

Points per game better than an average FBS team on a neutral field, from opponent-adjusted EPA (garbage time removed) with this season's games weighted against a preseason prior, plus the weight the margin model puts on Elo (a rating built from game results alone). Defense is positive when it holds opponents below average.

| # | Team | Conference | Net | Offense | Defense | Special teams | Results (Elo) | Elo rating |
|---|---|---|---|---|---|---|---|---|
| 1 | Ohio State | Big Ten | +27.0 | +11.0 | +10.4 | +0.4 | +5.1 | 1934 |
| 2 | LSU | SEC | +26.3 | +10.6 | +12.7 | +0.2 | +2.9 | 1751 |
| 3 | Miami | ACC | +24.0 | +13.2 | +6.1 | +0.2 | +4.6 | 1890 |
| 4 | Notre Dame | FBS Independents | +24.0 | +8.6 | +10.0 | +1.3 | +4.1 | 1849 |
| 5 | Georgia | SEC | +23.2 | +9.5 | +8.6 | +0.8 | +4.3 | 1866 |
| 6 | Indiana | Big Ten | +22.2 | +6.1 | +10.5 | +0.5 | +5.1 | 1935 |
| 7 | Alabama | SEC | +19.5 | +8.7 | +7.3 | +0.3 | +3.2 | 1777 |
| 8 | Texas | SEC | +18.6 | +2.8 | +11.9 | +0.5 | +3.5 | 1803 |
| 9 | Utah | Big 12 | +18.4 | +8.8 | +5.9 | +0.0 | +3.7 | 1819 |
| 10 | Ole Miss | SEC | +17.9 | +9.6 | +4.1 | +0.7 | +3.5 | 1802 |
| 11 | Oklahoma | SEC | +17.4 | +1.3 | +13.5 | +0.6 | +2.0 | 1677 |
| 12 | Texas Tech | Big 12 | +17.4 | +1.3 | +12.4 | +1.0 | +2.7 | 1733 |
| 13 | UCLA | Big Ten | +16.4 | +5.2 | +8.7 | +0.6 | +1.9 | 1668 |
| 14 | Oregon | Big Ten | +15.9 | +3.1 | +9.9 | +0.4 | +2.6 | 1722 |
| 15 | Tennessee | SEC | +15.2 | +3.3 | +8.7 | +0.7 | +2.6 | 1723 |
| 16 | Missouri | SEC | +15.1 | +3.9 | +8.6 | +0.5 | +2.1 | 1686 |
| 17 | Louisville | ACC | +15.0 | +8.8 | +4.1 | +0.3 | +1.9 | 1663 |
| 18 | Wake Forest | ACC | +14.9 | +5.6 | +7.0 | +0.1 | +2.2 | 1688 |
| 19 | Michigan | Big Ten | +14.4 | +2.6 | +9.8 | +0.2 | +1.8 | 1661 |
| 20 | BYU | Big 12 | +14.3 | +6.4 | +4.5 | +0.5 | +2.9 | 1748 |
| 21 | Nebraska | Big Ten | +14.0 | +4.9 | +7.3 | +0.5 | +1.4 | 1622 |
| 22 | Florida | SEC | +13.9 | +8.9 | +3.0 | +1.0 | +1.0 | 1592 |
| 23 | SMU | ACC | +13.1 | +6.7 | +3.9 | -0.0 | +2.5 | 1716 |
| 24 | Arizona | Big 12 | +12.8 | +5.8 | +4.2 | +0.0 | +2.7 | 1736 |
| 25 | USC | Big Ten | +12.8 | +10.6 | +0.0 | +0.2 | +2.0 | 1672 |
| 26 | Auburn | SEC | +12.3 | +4.8 | +6.3 | +0.6 | +0.5 | 1550 |
| 27 | Texas A&M | SEC | +11.9 | +2.4 | +7.8 | +0.6 | +1.1 | 1601 |
| 28 | Northwestern | Big Ten | +11.7 | +6.2 | +2.8 | +1.0 | +1.8 | 1655 |
| 29 | Iowa | Big Ten | +11.1 | +0.5 | +7.3 | +0.7 | +2.6 | 1723 |
| 30 | Penn State | Big Ten | +10.8 | +2.7 | +6.6 | +0.4 | +1.0 | 1593 |
| 31 | Houston | Big 12 | +10.2 | +8.0 | +0.1 | +0.2 | +2.0 | 1673 |
| 32 | Kansas State | Big 12 | +10.1 | +5.8 | +3.3 | +0.4 | +0.6 | 1558 |
| 33 | Wisconsin | Big Ten | +9.9 | +0.2 | +8.0 | +0.3 | +1.4 | 1621 |
| 34 | Mississippi State | SEC | +9.8 | +6.8 | +2.4 | +0.4 | +0.2 | 1523 |
| 35 | Kentucky | SEC | +9.5 | +2.7 | +4.5 | +0.3 | +2.0 | 1677 |
| 36 | South Carolina | SEC | +8.9 | +4.3 | +2.8 | +0.8 | +1.1 | 1599 |
| 37 | Washington | Big Ten | +8.2 | +2.6 | +4.1 | -0.1 | +1.5 | 1635 |
| 38 | Cincinnati | Big 12 | +8.0 | +8.9 | -2.4 | +0.5 | +1.0 | 1592 |
| 39 | Kansas | Big 12 | +7.8 | +5.7 | +2.8 | +0.0 | -0.7 | 1454 |
| 40 | Boise State | Pac-12 | +7.1 | +5.0 | -0.4 | +0.0 | +2.5 | 1717 |
| 41 | Baylor | Big 12 | +6.8 | -0.8 | +6.0 | +1.2 | +0.4 | 1546 |
| 42 | Oklahoma State | Big 12 | +6.5 | +6.7 | -0.6 | +0.5 | -0.2 | 1495 |
| 43 | Iowa State | Big 12 | +6.4 | +2.3 | +2.7 | +0.9 | +0.5 | 1552 |
| 44 | Florida State | ACC | +6.2 | +7.9 | -1.4 | -0.1 | -0.1 | 1497 |
| 45 | UCF | Big 12 | +5.8 | +2.0 | +3.8 | -0.1 | +0.1 | 1514 |
| 46 | Arizona State | Big 12 | +5.1 | +0.7 | +3.6 | +0.2 | +0.6 | 1562 |
| 47 | Duke | ACC | +5.1 | +2.0 | +0.6 | +0.7 | +1.7 | 1653 |
| 48 | Virginia Tech | ACC | +4.9 | +3.0 | +1.0 | +0.3 | +0.7 | 1566 |
| 49 | TCU | Big 12 | +4.9 | -1.8 | +5.4 | +0.5 | +0.8 | 1572 |
| 50 | Vanderbilt | SEC | +4.3 | +4.3 | -0.5 | +0.3 | +0.2 | 1529 |
| 51 | Minnesota | Big Ten | +3.8 | -3.9 | +6.2 | +0.7 | +0.7 | 1565 |
| 52 | North Texas | American Athletic | +3.7 | +10.1 | -7.2 | -0.7 | +1.5 | 1634 |
| 53 | James Madison | Sun Belt | +3.7 | -0.3 | +0.8 | +0.4 | +2.9 | 1747 |
| 54 | Illinois | Big Ten | +3.7 | +5.5 | -3.3 | +0.3 | +1.1 | 1601 |
| 55 | Pittsburgh | ACC | +3.5 | -0.0 | +2.6 | +0.5 | +0.4 | 1542 |
| 56 | Clemson | ACC | +3.4 | -5.0 | +7.1 | +0.4 | +0.8 | 1578 |
| 57 | NC State | ACC | +3.0 | +7.3 | -3.8 | -0.6 | +0.1 | 1515 |
| 58 | Oregon State | Pac-12 | +2.7 | +5.1 | -2.3 | +0.0 | -0.1 | 1498 |
| 59 | Virginia | ACC | +2.3 | -1.1 | +3.5 | -0.2 | +0.1 | 1517 |
| 60 | Colorado | Big 12 | +2.2 | +0.2 | +4.7 | -0.7 | -2.0 | 1346 |
| 61 | Syracuse | ACC | +2.2 | +1.6 | +2.9 | -0.6 | -1.7 | 1366 |
| 62 | UTSA | American Athletic | +2.1 | +3.0 | -2.8 | -0.2 | +2.1 | 1686 |
| 63 | Maryland | Big Ten | +1.4 | -0.6 | +3.4 | +0.5 | -2.0 | 1343 |
| 64 | Memphis | American Athletic | +1.2 | +3.0 | -2.0 | -0.5 | +0.7 | 1566 |
| 65 | Purdue | Big Ten | +1.2 | +3.3 | -1.9 | +0.5 | -0.8 | 1444 |
| 66 | Arkansas | SEC | +0.9 | +1.0 | +0.4 | -0.4 | -0.2 | 1496 |
| 67 | North Carolina | ACC | +0.6 | +0.5 | -0.9 | +0.9 | +0.1 | 1514 |
| 68 | West Virginia | Big 12 | +0.0 | +4.1 | -4.6 | +0.6 | -0.1 | 1502 |
| 69 | New Mexico | Mountain West | -0.0 | -2.6 | +1.3 | +0.0 | +1.2 | 1608 |
| 70 | Toledo | Mid-American | -0.1 | -1.3 | +0.7 | -0.0 | +0.6 | 1555 |
| 71 | Liberty | Conference USA | -1.0 | -0.4 | -0.8 | -0.1 | +0.2 | 1527 |
| 72 | Texas State | Pac-12 | -1.3 | +5.1 | -5.6 | -1.5 | +0.7 | 1567 |
| 73 | South Florida | American Athletic | -1.6 | -1.3 | -0.9 | -0.1 | +0.8 | 1572 |
| 74 | North Dakota State | Mountain West | -1.6 | -5.4 | +3.8 | +1.2 | -1.2 | 1408 |
| 75 | Navy | American Athletic | -2.0 | +2.6 | -3.5 | -0.7 | -0.3 | 1481 |
| 76 | UConn | FBS Independents | -2.1 | +1.6 | -3.4 | -0.3 | -0.0 | 1507 |
| 77 | Army | American Athletic | -2.3 | +4.9 | -8.1 | -0.2 | +1.1 | 1602 |
| 78 | Fresno State | Pac-12 | -3.4 | -2.6 | -1.2 | -0.1 | +0.4 | 1544 |
| 79 | Ohio | Mid-American | -3.4 | -2.0 | -2.7 | +0.4 | +0.8 | 1578 |
| 80 | East Carolina | American Athletic | -3.5 | -5.0 | +2.4 | -0.6 | -0.3 | 1484 |
| 81 | Boston College | ACC | -3.5 | -2.9 | +0.3 | -0.7 | -0.2 | 1493 |
| 82 | Michigan State | Big Ten | -3.6 | -3.6 | +1.3 | +0.2 | -1.4 | 1388 |
| 83 | Tulsa | American Athletic | -3.6 | -1.0 | -0.3 | -0.5 | -1.8 | 1358 |
| 84 | Georgia Tech | ACC | -3.7 | +2.7 | -5.3 | -0.0 | -1.1 | 1416 |
| 85 | Louisiana Tech | Sun Belt | -3.7 | -3.0 | -0.0 | -0.6 | -0.1 | 1500 |
| 86 | Rutgers | Big Ten | -3.7 | +2.5 | -5.6 | +0.6 | -1.3 | 1402 |
| 87 | Florida Atlantic | American Athletic | -4.2 | +3.5 | -7.3 | +0.5 | -1.0 | 1426 |
| 88 | Tulane | American Athletic | -4.6 | -4.7 | -0.5 | +0.1 | +0.5 | 1554 |
| 89 | Air Force | Mountain West | -4.6 | +2.6 | -6.3 | -0.3 | -0.7 | 1453 |
| 90 | UNLV | Mountain West | -4.8 | -3.1 | -2.1 | +0.0 | +0.4 | 1540 |
| 91 | California | ACC | -5.4 | -0.4 | -3.2 | -0.5 | -1.4 | 1392 |
| 92 | Jacksonville State | Conference USA | -6.1 | -0.5 | -4.7 | -0.4 | -0.5 | 1465 |
| 93 | Marshall | Sun Belt | -6.6 | -2.2 | -3.6 | -0.2 | -0.6 | 1462 |
| 94 | Western Michigan | Mid-American | -6.7 | -4.2 | -3.9 | +0.8 | +0.5 | 1552 |
| 95 | App State | Sun Belt | -7.2 | -3.0 | -3.4 | -0.2 | -0.7 | 1454 |
| 96 | Miami (OH) | Mid-American | -8.1 | -4.6 | -3.3 | +0.5 | -0.8 | 1446 |
| 97 | Washington State | Pac-12 | -8.2 | -6.9 | +0.6 | -0.2 | -1.6 | 1373 |
| 98 | San Diego State | Pac-12 | -8.4 | -5.3 | -1.8 | +0.2 | -1.5 | 1382 |
| 99 | Delaware | Conference USA | -8.4 | -1.5 | -5.3 | +0.2 | -1.9 | 1352 |
| 100 | Georgia State | Sun Belt | -8.4 | +0.5 | -7.3 | -0.4 | -1.3 | 1399 |
| 101 | Utah State | Pac-12 | -8.7 | -7.9 | +2.0 | -1.3 | -1.5 | 1384 |
| 102 | Stanford | ACC | -8.9 | -3.5 | -4.7 | -0.2 | -0.5 | 1465 |
| 103 | UAB | American Athletic | -9.2 | -4.8 | -3.5 | -0.0 | -1.0 | 1427 |
| 104 | Temple | American Athletic | -9.5 | +1.1 | -7.6 | -0.6 | -2.5 | 1303 |
| 105 | Georgia Southern | Sun Belt | -9.7 | -2.2 | -6.1 | -1.0 | -0.3 | 1481 |
| 106 | Louisiana | Sun Belt | -9.7 | -5.3 | -4.0 | -0.1 | -0.4 | 1478 |
| 107 | Colorado State | Pac-12 | -10.2 | +3.6 | -11.2 | -0.3 | -2.3 | 1313 |
| 108 | Western Kentucky | Conference USA | -10.3 | -6.8 | -2.0 | -0.2 | -1.3 | 1399 |
| 109 | Arkansas State | Sun Belt | -10.3 | -2.9 | -6.8 | +0.2 | -0.8 | 1441 |
| 110 | Wyoming | Mountain West | -11.1 | -6.5 | -3.3 | -0.2 | -1.1 | 1413 |
| 111 | South Alabama | Sun Belt | -11.1 | +0.4 | -10.8 | +0.2 | -0.8 | 1438 |
| 112 | Hawai'i | Mountain West | -11.3 | -4.1 | -6.1 | +0.7 | -1.7 | 1365 |
| 113 | Nevada | Mountain West | -12.5 | -8.7 | -2.1 | +0.4 | -2.1 | 1336 |
| 114 | Troy | Sun Belt | -12.8 | -7.6 | -2.0 | -1.2 | -1.9 | 1352 |
| 115 | Rice | American Athletic | -12.9 | -3.7 | -5.1 | -0.9 | -3.2 | 1246 |
| 116 | Florida International | Conference USA | -13.0 | -9.7 | -1.0 | -0.7 | -1.6 | 1377 |
| 117 | Coastal Carolina | Sun Belt | -13.3 | -5.8 | -5.8 | +0.4 | -2.1 | 1332 |
| 118 | Old Dominion | Sun Belt | -13.7 | -13.2 | +2.3 | -1.4 | -1.4 | 1394 |
| 119 | Central Michigan | Mid-American | -14.0 | -7.4 | -4.8 | -0.2 | -1.6 | 1375 |
| 120 | Missouri State | Conference USA | -14.1 | -1.5 | -8.1 | -1.4 | -3.1 | 1253 |
| 121 | New Mexico State | Conference USA | -14.1 | -8.0 | -2.2 | -1.4 | -2.4 | 1307 |
| 122 | Southern Miss | Sun Belt | -14.3 | -6.9 | -3.5 | -1.4 | -2.6 | 1296 |
| 123 | Kennesaw State | Conference USA | -14.9 | -6.8 | -4.7 | -0.8 | -2.6 | 1295 |
| 124 | Middle Tennessee | Conference USA | -15.0 | -5.6 | -7.1 | +0.1 | -2.4 | 1309 |
| 125 | San José State | Mountain West | -15.8 | -8.9 | -4.2 | -0.3 | -2.4 | 1312 |
| 126 | Ball State | Mid-American | -16.8 | -5.7 | -7.1 | -1.0 | -3.1 | 1251 |
| 127 | Eastern Michigan | Mid-American | -17.2 | -7.7 | -6.7 | -0.6 | -2.1 | 1330 |
| 128 | Massachusetts | Mid-American | -17.3 | -9.4 | -4.3 | -0.1 | -3.5 | 1219 |
| 129 | Sam Houston | Conference USA | -18.1 | -12.0 | -0.8 | -1.3 | -4.0 | 1173 |
| 130 | Buffalo | Mid-American | -18.1 | -12.6 | -5.4 | +0.6 | -0.8 | 1444 |
| 131 | UL Monroe | Sun Belt | -18.4 | -6.8 | -6.5 | -1.4 | -3.7 | 1203 |
| 132 | Northern Illinois | Mountain West | -18.8 | -4.6 | -9.0 | -0.9 | -4.3 | 1149 |
| 133 | Bowling Green | Mid-American | -18.8 | -11.3 | -4.6 | -0.1 | -2.8 | 1279 |
| 134 | Kent State | Mid-American | -18.9 | -9.0 | -6.6 | -1.0 | -2.3 | 1318 |
| 135 | Charlotte | American Athletic | -20.9 | -8.6 | -8.4 | -0.4 | -3.6 | 1211 |
| 136 | Sacramento State | Mid-American | -22.0 | -10.1 | -7.0 | +0.2 | -5.2 | 1074 |
| 137 | Akron | Mid-American | -22.7 | -9.9 | -7.9 | -1.2 | -3.6 | 1205 |
| 138 | UTEP | Mountain West | -24.0 | -11.7 | -6.3 | -1.4 | -4.6 | 1123 |

## Current model fit

- Fitted on 4183 games from seasons 2022–2026.
- Home field on top of the ratings: 3.2 points (1.9 in conference games).
- Extra FBS edge over FCS opponents beyond their ratings: 14.1 points.
- Elo weight: 0.19 points of margin per point of Elo spread.
- Weight on the betting line: 92% for the margin, 80% for the total.
