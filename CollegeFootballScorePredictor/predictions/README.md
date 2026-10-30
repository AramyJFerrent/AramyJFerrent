# College football score predictions

Updated Thu Oct 29, 2026 09:56 PM ET. Refreshed automatically every day of the season and several times on Saturdays; each game's prediction is locked at kickoff and graded once the final score is in. Scores are the most likely real scoreline near the expected points; ranges cover 80% of simulated outcomes for each team. College scores scatter widely, so read the ranges, not just the headline score.

Expected points blend the model with the betting line using the weight that has predicted best in recent seasons (see Current model fit). The spread and total columns show the model's own numbers next to the line, so you can see where it disagrees. Games without a line yet use the model alone.

The fair moneyline is the American odds that match the win chance exactly, with no bookmaker margin: -200 means risk $200 to win $100, +200 means risk $100 to win $200. A sportsbook's price will be a little worse on both sides because of its cut, so a book only offers value on a team when its price beats the fair line.

The edge columns judge each bet by its expected value per $1 staked at the posted price, using the final prediction: the model blended with the line, run through the score simulator, pushes included, and anchored to the market's own chances so that only what the blend moves off the line counts. The model's own spread and total (shown alongside) sit several points from the line in most games, but the blend keeps only the share of that disagreement the model has earned in past seasons, so edges are rare. The side with the higher value is shown when it reaches 3% (+3 cents per $1), as the team or side, the price, the expected value, its chance of winning the bet and its stake, a 25% share of the Kelly stake in units of 1% of the bankroll with at most 3 units on one game; anything short is no edge. Where a book posts no price for a spread or total it is assumed to be -110 and marked -110*; moneylines are never assumed. In the walk-forward backtest against closing lines, edges returned spread -100.0% on 1 bets (posted prices, 2016–2019); spread -3.9% on 156 bets (assumed -110 prices, 2016–2025); moneyline +13.7% on 575 bets (posted prices, 2016–2025); total +2.6% on 367 bets (posted prices, 2016–2019); total -5.7% on 172 bets (assumed -110 prices, 2016–2025). None of these is clearly above zero, so treat these edges as an experiment, not a betting system. The live record is tracked below, graded at the price logged with the last prediction before kickoff.

## 2026 Week 9

| Kickoff (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected points | 80% range | Spread: model / line | Total: model / line | Spread edge | Moneyline edge | Total edge | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Fri 10/30 7:00 PM | Tulane @ Charlotte | Tulane 28, Charlotte 21 | Tulane 73% | Tulane -275 / Charlotte +275 | 28.2 – 19.2 | 14–42 / 7–31 | Tulane -14.4 / Tulane -8.5 | 47.9 / 47.2 | no edge | no edge | no edge |  |
| Fri 10/30 7:30 PM | Baylor @ UCF | Baylor 24, UCF 21 | Baylor 54% | Baylor -120 / UCF +120 | 25.0 – 23.7 | 13–38 / 10–37 | UCF -0.2 / Baylor -1.5 | 52.4 / 47.8 | no edge | no edge | no edge |  |
| Fri 10/30 10:30 PM | Kent State @ Sacramento State | Kent State 27, Sacramento State 20 | Kent State 68% | Kent State -215 / Sacramento State +215 | 26.8 – 20.0 | 13–41 / 7–33 | Sacramento State -0.5 / Kent State -7.5 | 48.4 / 46.5 | no edge | no edge | no edge |  |
| Sat 10/31 12:00 PM | Arizona @ Texas Tech | Arizona 24, Texas Tech 27 | Texas Tech 60% | Arizona +150 / Texas Tech -150 | 24.8 – 28.6 | 11–38 / 14–44 | Texas Tech -8.1 / Texas Tech -3.5 | 48.9 / 54.5 | no edge | no edge | no edge |  |
| Sat 10/31 12:00 PM | California @ NC State | California 24, NC State 31 | NC State 69% | California +220 / NC State -220 | 24.9 – 32.4 | 10–38 / 17–48 | NC State -10.8 / NC State -7.2 | 60.5 / 56.5 | no edge | no edge | no edge |  |
| Sat 10/31 12:00 PM | SMU @ Syracuse | SMU 34, Syracuse 24 | SMU 75% | SMU -300 / Syracuse +300 | 33.7 – 23.3 | 20–49 / 10–37 | SMU -9.1 / SMU -10.5 | 54.8 / 57.5 | no edge | no edge | no edge |  |
| Sat 10/31 12:00 PM | Boston College @ Duke | Boston College 21, Duke 28 | Duke 70% | Boston College +235 / Duke -235 | 20.7 – 28.2 | 7–34 / 14–42 | Duke -12.5 / Duke -7.0 | 50.4 / 48.5 | no edge | no edge | no edge |  |
| Sat 10/31 12:00 PM | Wisconsin @ Iowa | Wisconsin 17, Iowa 20 | Iowa 58% | Wisconsin +140 / Iowa -140 | 17.4 – 20.0 | 7–30 / 7–33 | Iowa -4.1 / Iowa -2.5 | 41.4 / 36.5 | no edge | no edge | no edge |  |
| Sat 10/31 12:00 PM | Illinois @ Maryland | Illinois 27, Maryland 24 | Illinois 56% | Illinois -125 / Maryland +125 | 28.3 – 26.0 | 14–43 / 13–41 | Maryland -0.4 / Illinois -2.5 | 54.4 / 54.2 | no edge | no edge | no edge |  |
| Sat 10/31 12:00 PM | Notre Dame vs Navy | Notre Dame 42, Navy 10 | Notre Dame 98% | Notre Dame -6200 / Navy +6200 | 42.9 – 12.7 | 28–59 / 3–24 | Notre Dame -27.9 / Notre Dame -30.5 | 50.9 / 56.8 | no edge | no edge | no edge | neutral site |
| Sat 10/31 12:00 PM | UAB @ South Florida | UAB 17, South Florida 24 | South Florida 72% | UAB +255 / South Florida -255 | 17.9 – 25.8 | 7–30 / 13–41 | South Florida -10.1 / South Florida -7.8 | 50.5 / 42.2 | no edge | no edge | no edge |  |
| Sat 10/31 12:00 PM | Bowling Green @ Western Michigan | Bowling Green 17, Western Michigan 31 | Western Michigan 83% | Bowling Green +505 / Western Michigan -505 | 15.4 – 29.1 | 6–27 / 14–44 | Western Michigan -15.5 / Western Michigan -13.5 | 44.5 / 44.5 | no edge | no edge | no edge |  |
| Sat 10/31 12:30 PM | Michigan @ Rutgers | Michigan 31, Rutgers 14 | Michigan 87% | Michigan -650 / Rutgers +650 | 31.0 – 15.3 | 17–45 / 3–27 | Michigan -15.2 / Michigan -15.8 | 49.8 / 45.5 | no edge | no edge | no edge |  |
| Sat 10/31 12:45 PM | Auburn @ Ole Miss | Auburn 24, Ole Miss 38 | Ole Miss 78% | Auburn +365 / Ole Miss -365 | 22.8 – 35.0 | 10–37 / 20–51 | Ole Miss -8.1 / Ole Miss -12.5 | 58.1 / 57.8 | no edge | no edge | no edge |  |
| Sat 10/31 1:00 PM | Marshall @ Old Dominion | Marshall 24, Old Dominion 21 | Marshall 59% | Marshall -145 / Old Dominion +145 | 24.2 – 21.0 | 10–38 / 8–34 | Marshall -5.8 / Marshall -3.0 | 47.1 / 44.8 | no edge | no edge | no edge |  |
| Sat 10/31 2:00 PM | Kansas State @ Colorado | Kansas State 24, Colorado 27 | Colorado 52% | Kansas State +110 / Colorado -110 | 23.5 – 24.3 | 10–37 / 10–38 | Kansas State -6.6 / Colorado -1.5 | 52.3 / 46.8 | no edge | no edge | no edge |  |
| Sat 10/31 2:00 PM | Coastal Carolina @ Georgia State | Coastal Carolina 24, Georgia State 31 | Georgia State 65% | Coastal Carolina +185 / Georgia State -185 | 25.2 – 30.6 | 13–39 / 17–45 | Georgia State -6.6 / Georgia State -5.2 | 56.8 / 55.8 | no edge | no edge | no edge |  |
| Sat 10/31 3:00 PM | UConn @ Air Force | UConn 24, Air Force 27 | Air Force 53% | UConn +110 / Air Force -110 | 26.0 – 27.2 | 13–40 / 14–42 | Air Force -1.4 / Air Force -1.2 | 59.0 / 51.8 | no edge | no edge | Over 51.75 (-110*): EV +3.3%, 54%, stake 0.9u | * price not posted; assumed -110 |
| Sat 10/31 3:00 PM | Temple @ East Carolina | Temple 24, East Carolina 27 | East Carolina 62% | Temple +160 / East Carolina -160 | 22.7 – 27.5 | 10–36 / 14–42 | East Carolina -8.4 / East Carolina -4.5 | 52.4 / 49.8 | no edge | no edge | no edge |  |
| Sat 10/31 3:00 PM | Louisiana Tech @ South Alabama | Louisiana Tech 31, South Alabama 28 | Louisiana Tech 64% | Louisiana Tech -180 / South Alabama +180 | 32.0 – 26.3 | 17–47 / 13–41 | Louisiana Tech -4.2 / Louisiana Tech -5.8 | 57.5 / 58.5 | no edge | no edge | no edge |  |
| Sat 10/31 3:15 PM | Stanford @ Louisville | Stanford 17, Louisville 41 | Louisville 94% | Stanford +1535 / Louisville -1535 | 18.4 – 41.3 | 7–31 / 27–56 | Louisville -26.9 / Louisville -22.5 | 56.2 / 60.5 | no edge | no edge | no edge |  |
| Sat 10/31 3:30 PM | Florida vs Georgia | Florida 20, Georgia 34 | Georgia 79% | Florida +380 / Georgia -380 | 21.9 – 33.9 | 10–35 / 20–49 | Georgia -9.1 / Georgia -12.2 | 53.2 / 56.5 | no edge | no edge | no edge | neutral site |
| Sat 10/31 3:30 PM | Arizona State @ BYU | Arizona State 17, BYU 34 | BYU 87% | Arizona State +695 / BYU -695 | 16.4 – 32.5 | 6–28 / 17–48 | BYU -12.1 / BYU -16.5 | 50.5 / 48.5 | no edge | no edge | no edge |  |
| Sat 10/31 3:30 PM | Kansas @ TCU | Kansas 21, TCU 24 | TCU 64% | Kansas +180 / TCU -180 | 20.6 – 25.9 | 7–34 / 13–40 | PK / TCU -5.8 | 49.8 / 45.8 | no edge | no edge | no edge |  |
| Sat 10/31 3:30 PM | Minnesota @ Indiana | Minnesota 10, Indiana 31 | Indiana 94% | Minnesota +1530 / Indiana -1530 | 10.1 – 30.6 | 0–20 / 16–45 | Indiana -20.7 / Indiana -20.5 | 38.8 / 41.2 | no edge | no edge | no edge |  |
| Sat 10/31 3:30 PM | Northwestern @ Oregon | Northwestern 21, Oregon 24 | Oregon 60% | Northwestern +150 / Oregon -150 | 22.2 – 25.9 | 10–35 / 13–40 | Oregon -6.1 / Oregon -3.5 | 50.5 / 47.5 | no edge | no edge | no edge |  |
| Sat 10/31 3:30 PM | Colorado State @ Utah State | Colorado State 27, Utah State 34 | Utah State 65% | Colorado State +190 / Utah State -190 | 27.9 – 34.1 | 14–42 / 20–49 | Utah State -3.0 / Utah State -6.5 | 57.1 / 63.2 | no edge | no edge | no edge |  |
| Sat 10/31 3:30 PM | UTEP @ North Dakota State | UTEP 10, North Dakota State 34 | North Dakota State 97% | UTEP +3555 / North Dakota State -3555 | 8.9 – 33.9 | 0–17 / 20–49 | North Dakota State -27.5 / North Dakota State -24.8 | 41.3 / 43.2 | no edge | no edge | no edge |  |
| Sat 10/31 3:30 PM | Florida International @ Liberty | Florida International 17, Liberty 31 | Liberty 84% | Florida International +525 / Liberty -525 | 15.7 – 29.8 | 6–27 / 16–45 | Liberty -15.2 / Liberty -14.0 | 46.6 / 45.2 | no edge | no edge | no edge |  |
| Sat 10/31 3:30 PM | Southern Miss @ UL Monroe | Southern Miss 27, UL Monroe 24 | Southern Miss 58% | Southern Miss -135 / UL Monroe +135 | 29.3 – 26.0 | 15–44 / 13–41 | Southern Miss -1.7 / Southern Miss -3.5 | 54.4 / 55.5 | no edge | no edge | no edge |  |
| Sat 10/31 3:45 PM | Utah @ Cincinnati | Utah 31, Cincinnati 24 | Utah 68% | Utah -210 / Cincinnati +210 | 32.1 – 25.1 | 17–48 / 13–39 | Utah -7.5 / Utah -7.0 | 60.3 / 56.5 | no edge | no edge | no edge |  |
| Sat 10/31 3:45 PM | Virginia @ Wake Forest | Virginia 17, Wake Forest 31 | Wake Forest 81% | Virginia +415 / Wake Forest -415 | 18.0 – 31.0 | 7–31 / 17–45 | Wake Forest -15.3 / Wake Forest -12.8 | 48.3 / 49.2 | no edge | no edge | no edge |  |
| Sat 10/31 4:00 PM | New Mexico @ San José State | New Mexico 31, San José State 14 | New Mexico 85% | New Mexico -585 / San José State +585 | 29.0 – 14.3 | 14–44 / 3–26 | New Mexico -13.7 / New Mexico -14.8 | 47.7 / 42.2 | no edge | no edge | no edge |  |
| Sat 10/31 4:15 PM | South Carolina @ Oklahoma | South Carolina 21, Oklahoma 24 | Oklahoma 61% | South Carolina +155 / Oklahoma -155 | 20.1 – 24.2 | 7–34 / 10–38 | Oklahoma -10.8 / Oklahoma -3.5 | 44.9 / 44.2 | no edge | no edge | no edge |  |
| Sat 10/31 4:15 PM | Purdue @ Penn State | Purdue 21, Penn State 31 | Penn State 75% | Purdue +305 / Penn State -305 | 21.7 – 32.1 | 9–35 / 17–48 | Penn State -12.1 / Penn State -10.2 | 50.7 / 54.5 | no edge | no edge | no edge |  |
| Sat 10/31 4:15 PM | Nevada @ UCLA | Nevada 10, UCLA 34 | UCLA 96% | Nevada +2370 / UCLA -2370 | 10.3 – 33.9 | 0–20 / 20–49 | UCLA -32.9 / UCLA -22.8 | 45.8 / 43.8 | no edge | no edge | no edge |  |
| Sat 10/31 6:30 PM | App State @ Georgia Southern | App State 24, Georgia Southern 31 | Georgia Southern 63% | App State +170 / Georgia Southern -170 | 25.8 – 30.7 | 13–40 / 17–45 | App State -0.9 / Georgia Southern -5.5 | 57.5 / 56.5 | no edge | no edge | no edge |  |
| Sat 10/31 7:00 PM | Oklahoma State @ Iowa State | Oklahoma State 31, Iowa State 24 | Oklahoma State 71% | Oklahoma State -245 / Iowa State +245 | 32.7 – 24.3 | 17–48 / 10–38 | Iowa State -2.8 / Oklahoma State -9.5 | 55.1 / 57.5 | no edge | Iowa State (+285): EV +3.0%, 27%, stake 0.3u | no edge |  |
| Sat 10/31 7:00 PM | Clemson @ Florida State | Clemson 24, Florida State 27 | Florida State 65% | Clemson +185 / Florida State -185 | 22.3 – 28.2 | 10–35 / 14–42 | Florida State -4.8 / Florida State -6.0 | 51.2 / 50.2 | no edge | no edge | no edge |  |
| Sat 10/31 7:00 PM | Washington State @ San Diego State | Washington State 21, San Diego State 24 | San Diego State 57% | Washington State +135 / San Diego State -135 | 22.8 – 25.3 | 10–36 / 13–39 | San Diego State -2.7 / San Diego State -2.5 | 47.5 / 48.2 | no edge | no edge | no edge |  |
| Sat 10/31 7:30 PM | Mississippi State @ Texas | Mississippi State 17, Texas 38 | Texas 91% | Mississippi State +1040 / Texas -1040 | 15.5 – 35.2 | 3–27 / 20–51 | Texas -11.4 / Texas -20.5 | 51.4 / 50.5 | no edge | Mississippi State (+824): EV +4.9%, 11%, stake 0.1u | no edge |  |
| Sat 10/31 7:30 PM | Georgia Tech @ Pittsburgh | Georgia Tech 24, Pittsburgh 31 | Pittsburgh 69% | Georgia Tech +225 / Pittsburgh -225 | 23.3 – 31.3 | 10–37 / 17–45 | Pittsburgh -10.2 / Pittsburgh -7.8 | 55.0 / 54.5 | no edge | no edge | no edge |  |
| Sat 10/31 7:30 PM | Miami @ North Carolina | Miami 34, North Carolina 17 | Miami 83% | Miami -495 / North Carolina +495 | 33.8 – 19.3 | 20–49 / 7–31 | Miami -20.2 / Miami -14.0 | 54.8 / 52.8 | no edge | no edge | no edge |  |
| Sat 10/31 7:30 PM | Ohio State @ USC | Ohio State 31, USC 24 | Ohio State 68% | Ohio State -210 / USC +210 | 29.7 – 22.7 | 16–44 / 10–37 | Ohio State -12.0 / Ohio State -6.5 | 55.9 / 51.5 | no edge | no edge | no edge |  |
| Sat 10/31 7:45 PM | Missouri @ Arkansas | Missouri 31, Arkansas 21 | Missouri 76% | Missouri -310 / Arkansas +310 | 29.4 – 19.2 | 15–44 / 7–31 | Missouri -12.5 / Missouri -10.0 | 49.3 / 48.5 | no edge | no edge | no edge |  |
| Sat 10/31 8:00 PM | Washington @ Nebraska | Washington 21, Nebraska 28 | Nebraska 69% | Washington +225 / Nebraska -225 | 21.3 – 28.7 | 9–35 / 14–43 | Nebraska -8.9 / Nebraska -7.2 | 48.9 / 50.2 | no edge | no edge | no edge |  |
| Sat 10/31 8:00 PM | Army @ Memphis | Army 24, Memphis 31 | Memphis 65% | Army +190 / Memphis -190 | 27.0 – 33.2 | 14–41 / 19–48 | Memphis -5.6 / Memphis -6.2 | 60.4 / 60.2 | no edge | no edge | no edge |  |
| Sat 10/31 10:00 PM | Texas State @ Boise State | Texas State 28, Boise State 38 | Boise State 76% | Texas State +310 / Boise State -310 | 26.4 – 37.3 | 13–41 / 23–52 | Boise State -12.4 / Boise State -10.8 | 63.7 / 63.8 | no edge | no edge | no edge |  |
| Sat 10/31 10:30 PM | Northern Illinois @ UNLV | Northern Illinois 17, UNLV 38 | UNLV 95% | Northern Illinois +1820 / UNLV -1820 | 15.2 – 38.9 | 3–27 / 24–55 | UNLV -17.4 / UNLV -24.2 | 53.6 / 54.2 | no edge | no edge | no edge |  |
| Sat 10/31 11:00 PM | Oregon State @ Fresno State | Oregon State 31, Fresno State 24 | Oregon State 65% | Oregon State -185 / Fresno State +185 | 31.9 – 26.1 | 17–47 / 13–41 | Oregon State -3.7 / Oregon State -6.0 | 56.2 / 58.5 | no edge | no edge | no edge |  |

## 2026 Week 10

| Kickoff (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected points | 80% range | Spread: model / line | Total: model / line | Spread edge | Moneyline edge | Total edge | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tue 11/03 7:00 PM | Ohio @ Akron | Ohio 34, Akron 17 | Ohio 90% | Ohio -925 / Akron +925 | 34.1 – 15.7 | 20–50 / 5–27 | Ohio -18.4 / – | 49.9 / – | no line yet | no line yet (fair: Ohio -925) | no line yet |  |
| Tue 11/03 7:00 PM | Buffalo @ Miami (OH) | Buffalo 17, Miami (OH) 31 | Miami (OH) 81% | Buffalo +415 / Miami (OH) -415 | 18.1 – 30.5 | 7–31 / 16–45 | Miami (OH) -12.4 / – | 48.6 / – | no line yet | no line yet (fair: Miami (OH) -415) | no line yet |  |
| Wed 11/04 TBA | Ball State @ Massachusetts | Ball State 24, Massachusetts 27 | Massachusetts 59% | Ball State +145 / Massachusetts -145 | 23.1 – 26.0 | 10–37 / 13–41 | Massachusetts -2.9 / – | 49.0 / – | no line yet | no line yet (fair: Massachusetts -145) | no line yet |  |
| Wed 11/04 TBA | Central Michigan vs Eastern Michigan | Central Michigan 27, Eastern Michigan 24 | Central Michigan 60% | Central Michigan -150 / Eastern Michigan +150 | 26.6 – 23.0 | 13–41 / 10–37 | Central Michigan -3.7 / – | 49.6 / – | no line yet | no line yet (fair: Central Michigan -150) | no line yet | neutral site |
| Wed 11/04 TBA | Toledo @ Sacramento State | Toledo 35, Sacramento State 14 | Toledo 90% | Toledo -935 / Sacramento State +935 | 35.4 – 16.2 | 20–51 / 6–28 | Toledo -19.2 / – | 51.6 / – | no line yet | no line yet (fair: Toledo -935) | no line yet |  |
| Thu 11/05 8:00 PM | UTSA @ Florida Atlantic | UTSA 34, Florida Atlantic 31 | UTSA 59% | UTSA -140 / Florida Atlantic +140 | 34.1 – 31.0 | 20–49 / 17–45 | UTSA -3.1 / – | 65.3 / – | no line yet | no line yet (fair: UTSA -140) | no line yet |  |
| Thu 11/05 8:00 PM | James Madison @ Southern Miss | James Madison 34, Southern Miss 17 | James Madison 87% | James Madison -680 / Southern Miss +680 | 36.0 – 18.9 | 21–52 / 7–31 | James Madison -17.2 / – | 54.9 / – | no line yet | no line yet (fair: James Madison -680) | no line yet |  |
| Fri 11/06 7:00 PM | Virginia Tech @ SMU | Virginia Tech 24, SMU 31 | SMU 69% | Virginia Tech +220 / SMU -220 | 24.6 – 32.3 | 10–38 / 17–47 | SMU -10.4 / SMU -7.5 | 54.4 / 57.5 | no edge | no edge | no edge |  |
| Fri 11/06 7:30 PM | South Florida @ East Carolina | South Florida 24, East Carolina 27 | East Carolina 51% | South Florida +105 / East Carolina -105 | 24.7 – 24.7 | 12–38 / 13–38 | PK / – | 49.4 / – | no line yet | no line yet (fair: East Carolina -105) | no line yet |  |
| Fri 11/06 8:00 PM | Nebraska @ Illinois | Nebraska 31, Illinois 24 | Nebraska 70% | Nebraska -235 / Illinois +235 | 31.2 – 23.1 | 17–45 / 10–37 | Nebraska -8.1 / – | 54.3 / – | no line yet | no line yet (fair: Nebraska -235) | no line yet |  |
| Fri 11/06 9:00 PM | New Mexico @ Nevada | New Mexico 24, Nevada 17 | New Mexico 75% | New Mexico -295 / Nevada +295 | 27.2 – 17.5 | 13–41 / 7–30 | New Mexico -9.7 / – | 44.7 / – | no line yet | no line yet (fair: New Mexico -295) | no line yet |  |
| Fri 11/06 10:15 PM | TCU @ Arizona | TCU 20, Arizona 27 | Arizona 75% | TCU +295 / Arizona -295 | 19.4 – 29.3 | 7–31 / 14–44 | Arizona -9.9 / – | 48.9 / – | no line yet | no line yet (fair: Arizona -295) | no line yet |  |
| Sat 11/07 TBA | Arkansas @ Auburn | Arkansas 20, Auburn 34 | Auburn 83% | Arkansas +505 / Auburn -505 | 18.9 – 33.8 | 7–31 / 20–49 | Auburn -14.8 / – | 52.7 / – | no line yet | no line yet (fair: Auburn -505) | no line yet |  |
| Sat 11/07 TBA | Oklahoma @ Florida | Oklahoma 21, Florida 24 | Florida 60% | Oklahoma +150 / Florida -150 | 22.3 – 25.9 | 10–35 / 13–40 | Oklahoma -0.6 / Florida -4.0 | 46.6 / 48.5 | no edge | no edge | no edge |  |
| Sat 11/07 TBA | Alabama @ LSU | Alabama 24, LSU 27 | LSU 63% | Alabama +170 / LSU -170 | 23.6 – 28.5 | 10–37 / 14–43 | LSU -9.2 / LSU -4.5 | 50.1 / 52.5 | no edge | no edge | no edge |  |
| Sat 11/07 TBA | Georgia @ Ole Miss | Georgia 31, Ole Miss 28 | Georgia 57% | Georgia -130 / Ole Miss +130 | 29.6 – 26.6 | 16–44 / 13–41 | Georgia -3.0 / Georgia -3.0 | 55.3 / 56.5 | no edge | no edge | no edge |  |
| Sat 11/07 TBA | Vanderbilt @ Mississippi State | Vanderbilt 24, Mississippi State 31 | Mississippi State 70% | Vanderbilt +230 / Mississippi State -230 | 24.4 – 32.5 | 10–38 / 17–48 | Mississippi State -8.1 / – | 57.0 / – | no line yet | no line yet (fair: Mississippi State -230) | no line yet |  |
| Sat 11/07 TBA | Texas @ Missouri | Texas 27, Missouri 24 | Texas 59% | Texas -140 / Missouri +140 | 25.9 – 22.6 | 13–41 / 10–36 | Texas -1.0 / Texas -3.5 | 44.6 / 49.5 | no edge | no edge | no edge |  |
| Sat 11/07 TBA | Texas A&M @ South Carolina | Texas A&M 24, South Carolina 27 | Texas A&M 50% | Texas A&M -100 / South Carolina +100 | 24.6 – 24.4 | 10–38 / 10–38 | Texas A&M -0.2 / – | 49.0 / – | no line yet | no line yet (fair: Texas A&M -100) | no line yet |  |
| Sat 11/07 TBA | Kentucky @ Tennessee | Kentucky 24, Tennessee 27 | Tennessee 65% | Kentucky +185 / Tennessee -185 | 22.2 – 27.9 | 10–35 / 14–42 | Tennessee -8.6 / Tennessee -5.5 | 48.3 / 50.5 | no edge | no edge | no edge |  |
| Sat 11/07 TBA | BYU @ Utah | BYU 24, Utah 27 | Utah 59% | BYU +140 / Utah -140 | 23.0 – 26.3 | 10–37 / 13–41 | Utah -6.1 / Utah -3.0 | 52.8 / 48.5 | no edge | no edge | no edge |  |
| Sat 11/07 TBA | UCF @ Kansas | UCF 24, Kansas 27 | Kansas 62% | UCF +165 / Kansas -165 | 24.3 – 28.9 | 10–38 / 14–44 | Kansas -4.6 / – | 53.2 / – | no line yet | no line yet (fair: Kansas -165) | no line yet |  |
| Sat 11/07 TBA | Cincinnati @ Houston | Cincinnati 31, Houston 34 | Houston 61% | Cincinnati +155 / Houston -155 | 28.9 – 33.3 | 14–44 / 20–48 | Houston -4.4 / – | 62.3 / – | no line yet | no line yet (fair: Houston -155) | no line yet |  |
| Sat 11/07 TBA | Colorado @ Arizona State | Colorado 24, Arizona State 27 | Arizona State 66% | Colorado +195 / Arizona State -195 | 22.0 – 28.3 | 9–35 / 14–42 | Arizona State -6.3 / – | 50.3 / – | no line yet | no line yet (fair: Arizona State -195) | no line yet |  |
| Sat 11/07 TBA | Iowa State @ Baylor | Iowa State 24, Baylor 27 | Baylor 58% | Iowa State +135 / Baylor -135 | 24.0 – 27.2 | 10–38 / 14–41 | Baylor -3.1 / – | 51.2 / – | no line yet | no line yet (fair: Baylor -135) | no line yet |  |
| Sat 11/07 TBA | Oklahoma State @ Kansas State | Oklahoma State 24, Kansas State 31 | Kansas State 65% | Oklahoma State +185 / Kansas State -185 | 26.2 – 32.3 | 13–41 / 17–48 | Kansas State -6.1 / – | 58.5 / – | no line yet | no line yet (fair: Kansas State -185) | no line yet |  |
| Sat 11/07 TBA | West Virginia @ Texas Tech | West Virginia 17, Texas Tech 38 | Texas Tech 92% | West Virginia +1155 / Texas Tech -1155 | 17.9 – 38.2 | 6–31 / 23–54 | Texas Tech -20.2 / – | 56.1 / – | no line yet | no line yet (fair: Texas Tech -1155) | no line yet |  |
| Sat 11/07 TBA | Clemson @ Syracuse | Clemson 24, Syracuse 27 | Syracuse 51% | Clemson +100 / Syracuse -100 | 23.8 – 24.0 | 10–38 / 10–38 | Syracuse -0.2 / – | 47.9 / – | no line yet | no line yet (fair: Syracuse -100) | no line yet |  |
| Sat 11/07 TBA | Duke @ NC State | Duke 31, NC State 28 | Duke 53% | Duke -115 / NC State +115 | 29.3 – 28.3 | 16–44 / 14–42 | Duke -1.0 / – | 58.2 / – | no line yet | no line yet (fair: Duke -115) | no line yet |  |
| Sat 11/07 TBA | Louisville @ Georgia Tech | Louisville 38, Georgia Tech 21 | Louisville 85% | Louisville -575 / Georgia Tech +575 | 37.4 – 20.9 | 23–52 / 8–35 | Louisville -16.5 / – | 58.3 / – | no line yet | no line yet (fair: Louisville -575) | no line yet |  |
| Sat 11/07 TBA | Florida State @ Boston College | Florida State 31, Boston College 24 | Florida State 69% | Florida State -220 / Boston College +220 | 31.3 – 23.4 | 17–45 / 10–37 | Florida State -7.9 / – | 54.6 / – | no line yet | no line yet (fair: Florida State -220) | no line yet |  |
| Sat 11/07 TBA | Merrimack @ Wake Forest | Merrimack 3, Wake Forest 59 | Wake Forest 100% | Merrimack +9900 / Wake Forest -9900 | 3.0 – 58.4 | 0–7 / 45–73 | Wake Forest -55.4 / – | 61.4 / – | no line yet | no line yet (fair: Wake Forest -9900) | no line yet | FCS opponent |
| Sat 11/07 TBA | Michigan State @ Michigan | Michigan State 10, Michigan 27 | Michigan 85% | Michigan State +590 / Michigan -590 | 12.7 – 27.3 | 3–24 / 14–42 | Michigan -20.5 / Michigan -14.0 | 42.0 / 39.5 | no edge | no edge | no edge |  |
| Sat 11/07 TBA | UCLA @ Minnesota | UCLA 24, Minnesota 17 | UCLA 68% | UCLA -215 / Minnesota +215 | 24.6 – 17.8 | 10–38 / 7–31 | UCLA -10.0 / UCLA -6.5 | 41.6 / 42.5 | no edge | no edge | no edge |  |
| Sat 11/07 TBA | Iowa @ Northwestern | Iowa 21, Northwestern 24 | Northwestern 57% | Iowa +135 / Northwestern -135 | 20.6 – 23.1 | 9–34 / 10–37 | Northwestern -3.3 / Northwestern -2.5 | 48.7 / 42.5 | no edge | no edge | Over 42.5 (-110*): EV +3.8%, 54%, stake 1.0u | * price not posted; assumed -110 |
| Sat 11/07 TBA | Oregon @ Ohio State | Oregon 17, Ohio State 31 | Ohio State 84% | Oregon +510 / Ohio State -510 | 16.0 – 30.0 | 6–28 / 16–45 | Ohio State -13.6 / Ohio State -14.0 | 48.2 / 45.5 | no edge | no edge | no edge |  |
| Sat 11/07 TBA | Maryland @ Purdue | Maryland 24, Purdue 27 | Purdue 56% | Maryland +125 / Purdue -125 | 25.4 – 27.6 | 13–39 / 14–42 | Purdue -2.2 / – | 53.0 / – | no line yet | no line yet (fair: Purdue -125) | no line yet |  |
| Sat 11/07 TBA | Penn State @ Washington | Penn State 24, Washington 21 | Penn State 51% | Penn State -105 / Washington +105 | 23.6 – 23.1 | 10–38 / 10–37 | Penn State -0.6 / – | 46.7 / – | no line yet | no line yet (fair: Penn State -105) | no line yet |  |
| Sat 11/07 TBA | Rutgers @ Wisconsin | Rutgers 17, Wisconsin 34 | Wisconsin 86% | Rutgers +595 / Wisconsin -595 | 17.2 – 33.0 | 6–30 / 17–48 | Wisconsin -15.8 / – | 50.1 / – | no line yet | no line yet (fair: Wisconsin -595) | no line yet |  |
| Sat 11/07 TBA | Charlotte @ UAB | Charlotte 17, UAB 31 | UAB 84% | Charlotte +530 / UAB -530 | 17.7 – 32.2 | 7–30 / 17–48 | UAB -14.5 / – | 49.9 / – | no line yet | no line yet (fair: UAB -530) | no line yet |  |
| Sat 11/07 TBA | Rice @ North Texas | Rice 21, North Texas 41 | North Texas 90% | Rice +865 / North Texas -865 | 21.5 – 40.8 | 9–35 / 26–56 | North Texas -19.3 / – | 62.2 / – | no line yet | no line yet (fair: North Texas -865) | no line yet |  |
| Sat 11/07 TBA | Tulsa @ Tulane | Tulsa 24, Tulane 27 | Tulane 55% | Tulsa +125 / Tulane -125 | 24.4 – 26.6 | 10–38 / 13–41 | Tulane -2.1 / – | 51.0 / – | no line yet | no line yet (fair: Tulane -125) | no line yet |  |
| Sat 11/07 TBA | Hawai'i @ UTEP | Hawai'i 27, UTEP 17 | Hawai'i 80% | Hawai'i -405 / UTEP +405 | 28.2 – 15.9 | 14–42 / 6–28 | Hawai'i -12.3 / – | 49.8 / – | no line yet | no line yet (fair: Hawai'i -405) | no line yet |  |
| Sat 11/07 TBA | Northern Illinois @ San José State | Northern Illinois 24, San José State 31 | San José State 65% | Northern Illinois +190 / San José State -190 | 23.5 – 29.6 | 10–38 / 16–44 | San José State -6.0 / – | 53.1 / – | no line yet | no line yet (fair: San José State -190) | no line yet |  |
| Sat 11/07 TBA | Georgia State @ App State | Georgia State 28, App State 31 | App State 60% | Georgia State +150 / App State -150 | 27.4 – 31.3 | 14–42 / 17–46 | App State -4.0 / – | 59.1 / – | no line yet | no line yet (fair: App State -150) | no line yet |  |
| Sat 11/07 TBA | Old Dominion @ Coastal Carolina | Old Dominion 21, Coastal Carolina 24 | Coastal Carolina 63% | Old Dominion +170 / Coastal Carolina -170 | 19.9 – 24.6 | 7–32 / 13–38 | Coastal Carolina -4.7 / – | 44.5 / – | no line yet | no line yet (fair: Coastal Carolina -170) | no line yet |  |
| Sat 11/07 TBA | Marshall @ Georgia Southern | Marshall 31, Georgia Southern 28 | Marshall 53% | Marshall -115 / Georgia Southern +115 | 29.6 – 28.3 | 15–44 / 14–42 | Marshall -1.4 / – | 57.9 / – | no line yet | no line yet (fair: Marshall -115) | no line yet |  |
| Sat 11/07 TBA | South Alabama @ Louisiana | South Alabama 28, Louisiana 31 | Louisiana 58% | South Alabama +140 / Louisiana -140 | 27.6 – 31.2 | 14–42 / 17–45 | Louisiana -3.6 / – | 58.8 / – | no line yet | no line yet (fair: Louisiana -140) | no line yet |  |
| Sat 11/07 TBA | Louisiana Tech @ Troy | Louisiana Tech 27, Troy 20 | Louisiana Tech 69% | Louisiana Tech -220 / Troy +220 | 27.5 – 20.3 | 14–42 / 7–34 | Louisiana Tech -7.2 / – | 47.9 / – | no line yet | no line yet (fair: Louisiana Tech -220) | no line yet |  |
| Sat 11/07 12:00 PM | North Carolina @ UConn | North Carolina 24, UConn 27 | North Carolina 50% | North Carolina -100 / UConn +100 | 27.2 – 27.0 | 14–42 / 13–42 | North Carolina -0.2 / – | 55.9 / – | no line yet | no line yet (fair: North Carolina -100) | no line yet |  |
| Sat 11/07 3:00 PM | UL Monroe @ Arkansas State | UL Monroe 21, Arkansas State 31 | Arkansas State 79% | UL Monroe +385 / Arkansas State -385 | 20.4 – 32.6 | 7–34 / 17–48 | Arkansas State -12.1 / – | 53.0 / – | no line yet | no line yet (fair: Arkansas State -385) | no line yet |  |
| Sat 11/07 3:00 PM | Delaware @ Kennesaw State | Delaware 31, Kennesaw State 24 | Delaware 63% | Delaware -170 / Kennesaw State +170 | 30.0 – 25.0 | 16–45 / 13–38 | Delaware -5.0 / – | 55.1 / – | no line yet | no line yet (fair: Delaware -170) | no line yet |  |
| Sat 11/07 3:30 PM | Temple @ Navy | Temple 24, Navy 31 | Navy 75% | Temple +295 / Navy -295 | 22.1 – 31.9 | 10–35 / 17–47 | Navy -9.8 / – | 56.0 / – | no line yet | no line yet (fair: Navy -295) | no line yet |  |
| Sat 11/07 3:30 PM | Western Kentucky @ Middle Tennessee | Western Kentucky 27, Middle Tennessee 24 | Western Kentucky 55% | Western Kentucky -125 / Middle Tennessee +125 | 26.1 – 24.1 | 13–40 / 10–38 | Western Kentucky -1.9 / – | 50.2 / – | no line yet | no line yet (fair: Western Kentucky -125) | no line yet |  |
| Sat 11/07 4:00 PM | Missouri State @ Florida International | Missouri State 24, Florida International 27 | Florida International 60% | Missouri State +150 / Florida International -150 | 23.8 – 28.0 | 10–38 / 14–42 | Florida International -4.2 / – | 51.8 / – | no line yet | no line yet (fair: Florida International -150) | no line yet |  |
| Sat 11/07 5:00 PM | Liberty @ New Mexico State | Liberty 27, New Mexico State 14 | Liberty 80% | Liberty -400 / New Mexico State +400 | 26.6 – 14.7 | 13–41 / 3–27 | Liberty -11.9 / – | 47.9 / – | no line yet | no line yet (fair: Liberty -400) | no line yet |  |
| Sat 11/07 6:00 PM | Boise State @ Colorado State | Boise State 41, Colorado State 24 | Boise State 83% | Boise State -500 / Colorado State +500 | 39.1 – 23.9 | 24–55 / 10–38 | Boise State -15.2 / – | 63.1 / – | no line yet | no line yet (fair: Boise State -500) | no line yet |  |
| Sat 11/07 7:00 PM | Sam Houston @ Jacksonville State | Sam Houston 17, Jacksonville State 31 | Jacksonville State 86% | Sam Houston +590 / Jacksonville State -590 | 15.7 – 31.1 | 6–28 / 17–45 | Jacksonville State -15.4 / – | 46.7 / – | no line yet | no line yet (fair: Jacksonville State -590) | no line yet |  |
| Sat 11/07 7:30 PM | Miami @ Notre Dame | Miami 24, Notre Dame 27 | Notre Dame 59% | Miami +145 / Notre Dame -145 | 25.6 – 29.2 | 13–40 / 14–44 | Notre Dame -4.9 / Notre Dame -3.5 | 51.9 / 55.5 | no edge | no edge | no edge |  |
| Sat 11/07 7:30 PM | Air Force @ Army | Air Force 24, Army 31 | Army 64% | Air Force +180 / Army -180 | 23.8 – 29.3 | 10–38 / 16–44 | Army -6.3 / Army -5.5 | 59.8 / 51.5 | no edge | no edge | Over 51.5 (-110*): EV +4.4%, 55%, stake 1.2u | * price not posted; assumed -110 |
| Sat 11/07 9:30 PM | Fresno State @ Utah State | Fresno State 27, Utah State 24 | Fresno State 61% | Fresno State -155 / Utah State +155 | 25.3 – 21.3 | 13–38 / 9–35 | Fresno State -4.0 / – | 46.6 / – | no line yet | no line yet (fair: Fresno State -155) | no line yet |  |
| Sat 11/07 10:30 PM | Texas State @ Oregon State | Texas State 27, Oregon State 34 | Oregon State 68% | Texas State +215 / Oregon State -215 | 28.2 – 36.2 | 14–43 / 21–52 | Oregon State -7.9 / – | 67.4 / – | no line yet | no line yet (fair: Oregon State -215) | no line yet |  |
| Sat 11/07 10:30 PM | Wyoming @ UNLV | Wyoming 20, UNLV 27 | UNLV 73% | Wyoming +275 / UNLV -275 | 20.1 – 29.0 | 7–34 / 14–44 | UNLV -9.0 / – | 49.1 / – | no line yet | no line yet (fair: UNLV -275) | no line yet |  |

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
