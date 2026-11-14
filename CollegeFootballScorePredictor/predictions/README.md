# College football score predictions

Updated Sat Nov 14, 2026 01:49 PM ET. Refreshed automatically every day of the season and several times on Saturdays; each game's prediction is locked at kickoff and graded once the final score is in. Scores are the most likely real scoreline near the expected points; ranges cover 80% of simulated outcomes for each team. College scores scatter widely, so read the ranges, not just the headline score.

Expected points blend the model with the betting line using the weight that has predicted best in recent seasons (see Current model fit). The spread and total columns show the model's own numbers next to the line, so you can see where it disagrees. Games without a line yet use the model alone.

The fair moneyline is the American odds that match the win chance exactly, with no bookmaker margin: -200 means risk $200 to win $100, +200 means risk $100 to win $200. A sportsbook's price will be a little worse on both sides because of its cut, so a book only offers value on a team when its price beats the fair line.

The edge columns judge each bet by its expected value per $1 staked at the posted price, using the final prediction: the model blended with the line, run through the score simulator, pushes included, and anchored to the market's own chances so that only what the blend moves off the line counts. The model's own spread and total (shown alongside) sit several points from the line in most games, but the blend keeps only the share of that disagreement the model has earned in past seasons, so edges are rare. The side with the higher value is shown when it reaches 3% (+3 cents per $1), as the team or side, the price, the expected value, its chance of winning the bet and its stake, a 25% share of the Kelly stake in units of 1% of the bankroll with at most 3 units on one game; anything short is no edge. Where a book posts no price for a spread or total it is assumed to be -110 and marked -110*; moneylines are never assumed. In the walk-forward backtest against closing lines, edges returned spread -100.0% on 1 bets (posted prices, 2016–2019); spread -3.9% on 156 bets (assumed -110 prices, 2016–2025); moneyline +13.7% on 575 bets (posted prices, 2016–2025); total +2.6% on 367 bets (posted prices, 2016–2019); total -5.7% on 172 bets (assumed -110 prices, 2016–2025). None of these is clearly above zero, so treat these edges as an experiment, not a betting system. The live record is tracked below, graded at the price logged with the last prediction before kickoff.

## 2026 Week 11

| Kickoff (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected points | 80% range | Spread: model / line | Total: model / line | Spread edge | Moneyline edge | Total edge | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sat 11/14 2:00 PM | Kansas State @ TCU | Kansas State 17, TCU 31 | TCU 81% | Kansas State +435 / TCU -435 | 16.1 – 29.0 | 6–28 / 14–44 | TCU -1.4 / TCU -14.0 | 48.2 / 44.5 | no edge | Kansas State (+332): EV +4.7%, 24%, stake 0.4u | no edge |  |
| Sat 11/14 2:00 PM | Tulane @ Rice | Tulane 21, Rice 24 | Rice 57% | Tulane +130 / Rice -130 | 23.1 – 25.8 | 10–37 / 13–40 | Tulane -3.6 / Rice -3.2 | 50.7 / 48.5 | no edge | no edge | no edge |  |
| Sat 11/14 2:00 PM | Kennesaw State @ Sam Houston | Kennesaw State 24, Sam Houston 17 | Kennesaw State 73% | Kennesaw State -265 / Sam Houston +265 | 26.4 – 18.1 | 13–41 / 7–31 | Kennesaw State -5.4 / Kennesaw State -8.5 | 44.8 / 44.5 | no edge | no edge | no edge |  |
| Sat 11/14 3:00 PM | Tennessee @ Texas A&M | Tennessee 24, Texas A&M 21 | Tennessee 56% | Tennessee -125 / Texas A&M +125 | 23.1 – 21.3 | 10–37 / 9–35 | Tennessee -4.5 / Tennessee -1.5 | 45.3 / 44.2 | no edge | no edge | no edge |  |
| Sat 11/14 3:00 PM | New Mexico State @ Missouri State | New Mexico State 24, Missouri State 27 | Missouri State 55% | New Mexico State +125 / Missouri State -125 | 24.0 – 25.8 | 10–38 / 13–41 | Missouri State -4.8 / Missouri State -1.5 | 52.3 / 49.2 | no edge | no edge | no edge |  |
| Sat 11/14 3:00 PM | Florida International @ Delaware | Florida International 24, Delaware 27 | Delaware 62% | Florida International +160 / Delaware -160 | 24.9 – 29.2 | 11–38 / 14–44 | Delaware -11.0 / Delaware -3.8 | 52.3 / 54.5 | no edge | no edge | no edge |  |
| Sat 11/14 3:30 PM | Arizona State @ UCF | Arizona State 21, UCF 24 | UCF 60% | Arizona State +150 / UCF -150 | 22.1 – 25.3 | 10–35 / 13–39 | UCF -0.4 / UCF -3.5 | 50.5 / 46.8 | no edge | no edge | no edge |  |
| Sat 11/14 3:30 PM | Baylor @ BYU | Baylor 24, BYU 31 | BYU 71% | Baylor +250 / BYU -250 | 21.0 – 29.6 | 9–34 / 15–44 | BYU -6.0 / BYU -8.8 | 52.1 / 50.2 | no edge | no edge | no edge |  |
| Sat 11/14 3:30 PM | Missouri @ Georgia | Missouri 14, Georgia 31 | Georgia 87% | Missouri +700 / Georgia -700 | 15.8 – 32.2 | 5–28 / 17–48 | Georgia -14.2 / Georgia -16.5 | 45.8 / 48.5 | no edge | no edge | no edge |  |
| Sat 11/14 3:30 PM | Boston College @ Notre Dame | Boston College 10, Notre Dame 38 | Notre Dame 99% | Boston College +6750 / Notre Dame -6750 | 10.6 – 40.3 | 0–20 / 25–57 | Notre Dame -34.3 / Notre Dame -29.2 | 48.1 / 51.5 | no edge | no edge | no edge |  |
| Sat 11/14 3:30 PM | California @ Virginia | California 17, Virginia 27 | Virginia 78% | California +355 / Virginia -355 | 18.2 – 29.3 | 7–31 / 14–44 | Virginia -9.5 / Virginia -11.2 | 50.6 / 46.8 | no edge | no edge | no edge |  |
| Sat 11/14 3:30 PM | USC @ Indiana | USC 24, Indiana 31 | Indiana 74% | USC +275 / Indiana -275 | 21.1 – 30.4 | 9–34 / 17–45 | Indiana -9.7 / Indiana -9.2 | 50.8 / 51.8 | no edge | no edge | no edge |  |
| Sat 11/14 3:30 PM | Michigan @ Oregon | Michigan 17, Oregon 24 | Oregon 77% | Michigan +340 / Oregon -340 | 15.3 – 25.3 | 3–27 / 13–39 | Oregon -10.3 / Oregon -10.0 | 44.2 / 39.8 | no edge | no edge | no edge |  |
| Sat 11/14 3:30 PM | Florida Atlantic @ Tulsa | Florida Atlantic 31, Tulsa 38 | Tulsa 65% | Florida Atlantic +185 / Tulsa -185 | 32.8 – 39.1 | 18–48 / 24–55 | Tulsa -3.7 / Tulsa -6.5 | 66.0 / 73.2 | no edge | no edge | no edge |  |
| Sat 11/14 3:30 PM | Nevada @ Northern Illinois | Nevada 24, Northern Illinois 21 | Nevada 65% | Nevada -190 / Northern Illinois +190 | 26.9 – 20.9 | 13–41 / 7–34 | Nevada -2.4 / Nevada -6.2 | 49.0 / 47.5 | no edge | no edge | no edge |  |
| Sat 11/14 3:30 PM | Georgia Southern @ Georgia State | Georgia Southern 31, Georgia State 24 | Georgia Southern 64% | Georgia Southern -180 / Georgia State +180 | 30.7 – 25.2 | 17–45 / 13–39 | PK / Georgia Southern -6.0 | 57.7 / 55.5 | no edge | no edge | no edge |  |
| Sat 11/14 3:30 PM | Jacksonville State @ Western Kentucky | Jacksonville State 31, Western Kentucky 24 | Jacksonville State 68% | Jacksonville State -215 / Western Kentucky +215 | 31.0 – 23.6 | 17–45 / 10–38 | Jacksonville State -5.5 / Jacksonville State -7.5 | 55.1 / 54.5 | no edge | no edge | no edge |  |
| Sat 11/14 3:30 PM | Middle Tennessee @ Liberty | Middle Tennessee 17, Liberty 38 | Liberty 93% | Middle Tennessee +1290 / Liberty -1290 | 16.0 – 37.1 | 6–28 / 23–53 | Liberty -21.7 / Liberty -21.0 | 51.7 / 53.5 | no edge | no edge | no edge |  |
| Sat 11/14 4:00 PM | Fresno State @ Texas State | Fresno State 27, Texas State 34 | Texas State 74% | Fresno State +285 / Texas State -285 | 25.2 – 35.0 | 12–39 / 20–50 | Texas State -6.9 / Texas State -10.0 | 60.1 / 60.2 | no edge | no edge | no edge |  |
| Sat 11/14 4:15 PM | Ole Miss @ Oklahoma | Ole Miss 24, Oklahoma 27 | Oklahoma 56% | Ole Miss +130 / Oklahoma -130 | 23.1 – 25.8 | 10–37 / 13–40 | Oklahoma -2.1 / Oklahoma -2.8 | 50.0 / 48.8 | no edge | no edge | no edge |  |
| Sat 11/14 4:15 PM | Washington @ Michigan State | Washington 24, Michigan State 21 | Washington 59% | Washington -140 / Michigan State +140 | 23.7 – 20.8 | 10–38 / 7–34 | Washington -7.0 / Washington -2.5 | 45.6 / 44.2 | no edge | no edge | no edge |  |
| Sat 11/14 5:00 PM | Southern Miss @ Louisiana Tech | Southern Miss 21, Louisiana Tech 38 | Louisiana Tech 88% | Southern Miss +760 / Louisiana Tech -760 | 19.1 – 36.3 | 7–31 / 21–52 | Louisiana Tech -16.0 / Louisiana Tech -17.2 | 51.7 / 56.2 | no edge | no edge | no edge |  |
| Sat 11/14 5:30 PM | Kansas @ West Virginia | Kansas 31, West Virginia 34 | West Virginia 53% | Kansas +115 / West Virginia -115 | 33.2 – 34.4 | 19–48 / 20–50 | Kansas -2.2 / West Virginia -1.5 | 64.1 / 68.5 | no edge | no edge | no edge |  |
| Sat 11/14 6:00 PM | Oregon State @ Boise State | Oregon State 24, Boise State 41 | Boise State 85% | Oregon State +565 / Boise State -565 | 24.0 – 39.8 | 10–38 / 24–56 | Boise State -8.8 / Boise State -16.5 | 61.7 / 64.2 | no edge | no edge | no edge |  |
| Sat 11/14 6:00 PM | App State @ Marshall | App State 27, Marshall 24 | App State 53% | App State -115 / Marshall +115 | 27.8 – 26.9 | 14–42 / 14–41 | Marshall -2.9 / App State -1.2 | 55.1 / 54.5 | no edge | no edge | no edge |  |
| Sat 11/14 6:15 PM | Florida @ Kentucky | Florida 24, Kentucky 27 | Kentucky 57% | Florida +135 / Kentucky -135 | 24.9 – 27.6 | 12–38 / 14–42 | Florida -0.7 / Kentucky -3.0 | 51.3 / 52.8 | no edge | no edge | no edge |  |
| Sat 11/14 7:00 PM | Louisville @ North Carolina | Louisville 31, North Carolina 28 | Louisville 60% | Louisville -150 / North Carolina +150 | 30.7 – 26.7 | 17–45 / 13–41 | Louisville -9.7 / Louisville -3.5 | 57.1 / 57.5 | no edge | no edge | no edge |  |
| Sat 11/14 7:00 PM | Minnesota @ Penn State | Minnesota 14, Penn State 28 | Penn State 81% | Minnesota +420 / Penn State -420 | 15.0 – 27.3 | 3–27 / 13–42 | Penn State -10.5 / Penn State -12.5 | 41.5 / 42.5 | no edge | no edge | no edge |  |
| Sat 11/14 7:00 PM | San José State @ Air Force | San José State 17, Air Force 31 | Air Force 84% | San José State +510 / Air Force -510 | 17.7 – 31.7 | 7–31 / 17–47 | Air Force -13.7 / Air Force -14.0 | 53.0 / 48.5 | no edge | no edge | no edge |  |
| Sat 11/14 7:00 PM | Troy @ South Alabama | Troy 24, South Alabama 27 | South Alabama 58% | Troy +135 / South Alabama -135 | 26.1 – 29.2 | 13–40 / 14–44 | South Alabama -3.9 / South Alabama -3.0 | 54.4 / 55.5 | no edge | no edge | no edge |  |
| Sat 11/14 7:30 PM | Utah @ Arizona | Utah 27, Arizona 24 | Utah 54% | Utah -120 / Arizona +120 | 28.6 – 27.0 | 14–43 / 14–42 | Utah -5.7 / Utah -1.2 | 56.0 / 55.5 | no edge | no edge | no edge |  |
| Sat 11/14 7:30 PM | Texas @ LSU | Texas 21, LSU 24 | LSU 62% | Texas +165 / LSU -165 | 20.9 – 25.5 | 8–34 / 13–40 | LSU -5.7 / LSU -4.5 | 45.9 / 46.5 | no edge | no edge | no edge |  |
| Sat 11/14 7:30 PM | Stanford @ Virginia Tech | Stanford 21, Virginia Tech 38 | Virginia Tech 88% | Stanford +700 / Virginia Tech -700 | 20.1 – 37.4 | 7–34 / 21–52 | Virginia Tech -15.4 / Virginia Tech -17.5 | 56.3 / 57.8 | no edge | no edge | no edge |  |
| Sat 11/14 7:30 PM | Purdue @ Iowa | Purdue 14, Iowa 31 | Iowa 89% | Purdue +835 / Iowa -835 | 15.2 – 32.7 | 3–27 / 17–48 | Iowa -17.9 / Iowa -17.5 | 48.4 / 47.8 | no edge | no edge | no edge |  |
| Sat 11/14 7:30 PM | UNLV @ New Mexico | UNLV 14, New Mexico 31 | New Mexico 88% | UNLV +765 / New Mexico -765 | 14.9 – 31.7 | 3–27 / 17–47 | New Mexico -9.1 / New Mexico -17.5 | 47.2 / 46.5 | no edge | no edge | no edge |  |
| Sat 11/14 7:45 PM | South Carolina @ Arkansas | South Carolina 31, Arkansas 24 | South Carolina 70% | South Carolina -230 / Arkansas +230 | 30.0 – 22.3 | 16–45 / 10–35 | South Carolina -10.3 / South Carolina -7.5 | 54.9 / 51.8 | no edge | no edge | no edge |  |
| Sat 11/14 9:00 PM | North Texas @ UTSA | North Texas 41, UTSA 38 | North Texas 56% | North Texas -125 / UTSA +125 | 38.6 – 36.3 | 24–55 / 21–52 | UTSA -0.4 / North Texas -2.5 | 69.2 / 76.2 | no edge | no edge | no edge |  |
| Sat 11/14 9:30 PM | Texas Tech @ Oklahoma State | Texas Tech 35, Oklahoma State 38 | Oklahoma State 57% | Texas Tech +130 / Oklahoma State -130 | 34.0 – 36.8 | 20–49 / 21–52 | Texas Tech -5.7 / Oklahoma State -3.5 | 57.5 / 73.8 | no edge | no edge | Under 73.75 (-110*): EV +7.8%, 56%, stake 2.2u | * price not posted; assumed -110 |
| Sat 11/14 9:30 PM | Utah State @ San Diego State | Utah State 24, San Diego State 21 | Utah State 56% | Utah State -130 / San Diego State +130 | 23.5 – 20.9 | 10–37 / 9–34 | San Diego State -1.9 / Utah State -3.0 | 47.6 / 43.8 | no edge | no edge | no edge |  |
| Sat 11/14 10:00 PM | Wyoming @ UTEP | Wyoming 24, UTEP 17 | Wyoming 71% | Wyoming -240 / UTEP +240 | 24.5 – 17.0 | 10–38 / 6–29 | Wyoming -14.0 / Wyoming -7.0 | 45.9 / 40.5 | no edge | no edge | no edge |  |
| Sat 11/14 10:30 PM | Colorado State @ Washington State | Colorado State 28, Washington State 35 | Washington State 70% | Colorado State +235 / Washington State -235 | 27.7 – 36.0 | 14–42 / 21–52 | Washington State -5.2 / Washington State -8.5 | 58.9 / 64.8 | no edge | no edge | no edge |  |
| Sat 11/14 11:00 PM | North Dakota State @ Hawai'i | North Dakota State 24, Hawai'i 17 | North Dakota State 70% | North Dakota State -230 / Hawai'i +230 | 23.8 – 16.8 | 10–38 / 6–28 | North Dakota State -6.7 / North Dakota State -7.0 | 47.3 / 39.2 | no edge | no edge | no edge |  |

## 2026 Week 12

| Kickoff (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected points | 80% range | Spread: model / line | Total: model / line | Spread edge | Moneyline edge | Total edge | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tue 11/17 7:00 PM | Ball State @ Ohio | Ball State 17, Ohio 34 | Ohio 88% | Ball State +700 / Ohio -700 | 17.2 – 34.0 | 6–30 / 20–49 | Ohio -16.7 / – | 51.2 / – | no line yet | no line yet (fair: Ohio -700) | no line yet |  |
| Tue 11/17 7:00 PM | Eastern Michigan @ Western Michigan | Eastern Michigan 17, Western Michigan 34 | Western Michigan 86% | Eastern Michigan +610 / Western Michigan -610 | 17.5 – 33.4 | 7–30 / 17–49 | Western Michigan -15.8 / – | 50.9 / – | no line yet | no line yet (fair: Western Michigan -610) | no line yet |  |
| Tue 11/17 7:00 PM | Miami (OH) @ Kent State | Miami (OH) 27, Kent State 17 | Miami (OH) 77% | Miami (OH) -340 / Kent State +340 | 28.7 – 17.9 | 14–43 / 7–31 | Miami (OH) -10.8 / – | 46.6 / – | no line yet | no line yet (fair: Miami (OH) -340) | no line yet |  |
| Wed 11/18 TBA | Akron @ Massachusetts | Akron 20, Massachusetts 27 | Massachusetts 72% | Akron +255 / Massachusetts -255 | 19.7 – 28.1 | 7–33 / 14–42 | Massachusetts -8.4 / – | 47.8 / – | no line yet | no line yet (fair: Massachusetts -255) | no line yet |  |
| Wed 11/18 7:30 PM | Central Michigan @ Buffalo | Central Michigan 27, Buffalo 24 | Central Michigan 58% | Central Michigan -140 / Buffalo +140 | 26.4 – 23.7 | 13–41 / 10–38 | Central Michigan -2.7 / – | 50.1 / – | no line yet | no line yet (fair: Central Michigan -140) | no line yet |  |
| Thu 11/19 7:30 PM | Rice @ Temple | Rice 24, Temple 31 | Temple 65% | Rice +185 / Temple -185 | 23.9 – 29.8 | 10–38 / 16–44 | Temple -5.9 / – | 53.7 / – | no line yet | no line yet (fair: Temple -185) | no line yet |  |
| Fri 11/20 6:00 PM | Iowa State @ UCF | Iowa State 27, UCF 24 | Iowa State 54% | Iowa State -120 / UCF +120 | 26.9 – 25.1 | 13–41 / 13–38 | Iowa State -1.8 / – | 52.4 / – | no line yet | no line yet (fair: Iowa State -120) | no line yet |  |
| Fri 11/20 7:30 PM | Clemson @ Duke | Clemson 21, Duke 24 | Duke 65% | Clemson +185 / Duke -185 | 20.4 – 25.8 | 7–34 / 13–40 | Duke -5.4 / – | 46.2 / – | no line yet | no line yet (fair: Duke -185) | no line yet |  |
| Fri 11/20 7:30 PM | Bowling Green @ Toledo | Bowling Green 10, Toledo 31 | Toledo 93% | Bowling Green +1360 / Toledo -1360 | 12.4 – 32.4 | 3–23 / 17–48 | Toledo -20.0 / – | 44.8 / – | no line yet | no line yet (fair: Toledo -1360) | no line yet |  |
| Fri 11/20 8:00 PM | Oregon @ Michigan State | Oregon 31, Michigan State 14 | Oregon 90% | Oregon -945 / Michigan State +945 | 32.3 – 14.2 | 17–48 / 3–24 | Oregon -18.1 / – | 46.4 / – | no line yet | no line yet (fair: Oregon -945) | no line yet |  |
| Fri 11/20 8:00 PM | UTEP @ Air Force | UTEP 10, Air Force 38 | Air Force 95% | UTEP +2005 / Air Force -2005 | 13.1 – 36.7 | 3–24 / 21–52 | Air Force -23.6 / – | 51.2 / – | no line yet | no line yet (fair: Air Force -2005) | no line yet |  |
| Fri 11/20 9:00 PM | New Mexico @ Wyoming | New Mexico 24, Wyoming 17 | New Mexico 71% | New Mexico -240 / Wyoming +240 | 22.9 – 15.4 | 10–36 / 6–27 | New Mexico -7.5 / – | 43.7 / – | no line yet | no line yet (fair: New Mexico -240) | no line yet |  |
| Sat 11/21 TBA | Vanderbilt @ Florida | Vanderbilt 24, Florida 31 | Florida 71% | Vanderbilt +250 / Florida -250 | 22.1 – 30.5 | 10–35 / 16–45 | Florida -8.4 / – | 52.6 / – | no line yet | no line yet (fair: Florida -250) | no line yet |  |
| Sat 11/21 TBA | Kentucky @ Missouri | Kentucky 21, Missouri 28 | Missouri 66% | Kentucky +195 / Missouri -195 | 21.5 – 27.7 | 9–35 / 14–42 | Missouri -8.8 / Missouri -6.0 | 49.1 / 49.5 | no edge | no edge | no edge |  |
| Sat 11/21 TBA | Texas A&M @ Oklahoma | Texas A&M 24, Oklahoma 27 | Oklahoma 58% | Texas A&M +140 / Oklahoma -140 | 23.1 – 26.0 | 10–37 / 13–41 | Oklahoma -7.7 / Oklahoma -2.5 | 40.1 / 51.5 | no edge | no edge | Under 51.5 (-110*): EV +8.6%, 57%, stake 2.4u | * price not posted; assumed -110 |
| Sat 11/21 TBA | Georgia @ South Carolina | Georgia 31, South Carolina 21 | Georgia 75% | Georgia -305 / South Carolina +305 | 30.7 – 20.6 | 17–45 / 7–34 | Georgia -11.1 / Georgia -10.0 | 50.0 / 51.5 | no edge | no edge | no edge |  |
| Sat 11/21 TBA | LSU @ Tennessee | LSU 24, Tennessee 21 | LSU 55% | LSU -120 / Tennessee +120 | 25.1 – 23.5 | 13–38 / 10–37 | LSU -2.9 / LSU -1.5 | 49.2 / 48.5 | no edge | no edge | no edge |  |
| Sat 11/21 TBA | Arkansas @ Texas | Arkansas 13, Texas 34 | Texas 95% | Arkansas +1890 / Texas -1890 | 11.8 – 34.5 | 3–23 / 20–51 | Texas -22.7 / – | 46.4 / – | no line yet | no line yet (fair: Texas -1890) | no line yet |  |
| Sat 11/21 TBA | Arizona @ Kansas State | Arizona 27, Kansas State 24 | Arizona 58% | Arizona -140 / Kansas State +140 | 25.5 – 22.3 | 13–40 / 10–35 | Arizona -3.2 / – | 54.8 / – | no line yet | no line yet (fair: Arizona -140) | no line yet |  |
| Sat 11/21 TBA | BYU @ Kansas | BYU 24, Kansas 21 | BYU 64% | BYU -180 / Kansas +180 | 26.0 – 20.8 | 13–41 / 8–34 | BYU -5.2 / – | 52.8 / – | no line yet | no line yet (fair: BYU -180) | no line yet |  |
| Sat 11/21 TBA | Colorado @ Cincinnati | Colorado 24, Cincinnati 31 | Cincinnati 68% | Colorado +210 / Cincinnati -210 | 25.5 – 32.6 | 13–40 / 17–48 | Cincinnati -7.1 / – | 58.1 / – | no line yet | no line yet (fair: Cincinnati -210) | no line yet |  |
| Sat 11/21 TBA | Houston @ West Virginia | Houston 38, West Virginia 31 | Houston 67% | Houston -200 / West Virginia +200 | 36.3 – 29.5 | 21–52 / 16–44 | Houston -6.7 / – | 65.8 / – | no line yet | no line yet (fair: Houston -200) | no line yet |  |
| Sat 11/21 TBA | Oklahoma State @ Arizona State | Oklahoma State 31, Arizona State 28 | Oklahoma State 56% | Oklahoma State -125 / Arizona State +125 | 30.1 – 27.8 | 16–45 / 14–42 | Oklahoma State -2.3 / – | 57.9 / – | no line yet | no line yet (fair: Oklahoma State -125) | no line yet |  |
| Sat 11/21 TBA | Texas Tech @ Baylor | Texas Tech 31, Baylor 28 | Texas Tech 55% | Texas Tech -120 / Baylor +120 | 28.3 – 26.4 | 14–42 / 13–41 | Texas Tech -5.8 / Texas Tech -1.5 | 52.1 / 55.5 | no edge | no edge | no edge |  |
| Sat 11/21 TBA | Utah @ TCU | Utah 24, TCU 17 | Utah 66% | Utah -195 / TCU +195 | 25.7 – 19.6 | 13–40 / 7–33 | Utah -12.4 / Utah -5.5 | 49.4 / 44.5 | no edge | no edge | no edge |  |
| Sat 11/21 TBA | Virginia Tech @ Miami | Virginia Tech 21, Miami 38 | Miami 90% | Virginia Tech +865 / Miami -865 | 21.1 – 39.9 | 9–34 / 24–56 | Miami -21.3 / Miami -18.5 | 58.7 / 61.5 | no edge | no edge | no edge |  |
| Sat 11/21 TBA | NC State @ Florida State | NC State 28, Florida State 31 | Florida State 65% | NC State +185 / Florida State -185 | 27.5 – 33.5 | 14–42 / 19–48 | Florida State -6.0 / – | 61.0 / – | no line yet | no line yet (fair: Florida State -185) | no line yet |  |
| Sat 11/21 TBA | North Carolina @ Virginia | North Carolina 27, Virginia 24 | North Carolina 53% | North Carolina -115 / Virginia +115 | 26.3 – 24.9 | 13–41 / 11–38 | North Carolina -1.4 / – | 51.2 / – | no line yet | no line yet (fair: North Carolina -115) | no line yet |  |
| Sat 11/21 TBA | Pittsburgh @ Louisville | Pittsburgh 17, Louisville 34 | Louisville 83% | Pittsburgh +490 / Louisville -490 | 19.8 – 34.3 | 7–34 / 20–49 | Louisville -14.5 / – | 54.1 / – | no line yet | no line yet (fair: Louisville -490) | no line yet |  |
| Sat 11/21 TBA | Stanford @ California | Stanford 24, California 31 | California 61% | Stanford +160 / California -160 | 25.5 – 30.1 | 13–40 / 16–45 | California -4.6 / – | 55.6 / – | no line yet | no line yet (fair: California -160) | no line yet |  |
| Sat 11/21 TBA | Syracuse @ Boston College | Syracuse 27, Boston College 24 | Syracuse 62% | Syracuse -165 / Boston College +165 | 27.8 – 23.3 | 14–42 / 10–37 | Syracuse -4.5 / – | 51.1 / – | no line yet | no line yet (fair: Syracuse -165) | no line yet |  |
| Sat 11/21 TBA | Wake Forest @ Georgia Tech | Wake Forest 38, Georgia Tech 17 | Wake Forest 93% | Wake Forest -1290 / Georgia Tech +1290 | 38.5 – 17.0 | 23–55 / 6–29 | Wake Forest -21.5 / – | 55.4 / – | no line yet | no line yet (fair: Wake Forest -1290) | no line yet |  |
| Sat 11/21 TBA | Iowa @ Illinois | Iowa 24, Illinois 21 | Iowa 66% | Iowa -190 / Illinois +190 | 25.1 – 19.5 | 12–38 / 7–32 | Iowa -6.3 / Iowa -5.5 | 49.9 / 43.5 | no edge | no edge | no edge |  |
| Sat 11/21 TBA | UCLA @ Michigan | UCLA 24, Michigan 17 | UCLA 65% | UCLA -190 / Michigan +190 | 23.5 – 18.1 | 10–37 / 7–31 | UCLA -4.3 / UCLA -5.5 | 42.5 / 41.5 | no edge | no edge | no edge |  |
| Sat 11/21 TBA | Northwestern @ Minnesota | Northwestern 24, Minnesota 21 | Northwestern 61% | Northwestern -155 / Minnesota +155 | 24.7 – 20.7 | 10–38 / 7–34 | Northwestern -4.0 / – | 46.7 / – | no line yet | no line yet (fair: Northwestern -155) | no line yet |  |
| Sat 11/21 TBA | Ohio State @ Nebraska | Ohio State 27, Nebraska 20 | Ohio State 65% | Ohio State -185 / Nebraska +185 | 26.7 – 20.9 | 13–41 / 9–34 | Ohio State -9.1 / Ohio State -5.5 | 50.5 / 47.5 | no edge | no edge | no edge |  |
| Sat 11/21 TBA | Rutgers @ Penn State | Rutgers 17, Penn State 34 | Penn State 90% | Rutgers +865 / Penn State -865 | 17.0 – 35.4 | 6–30 / 20–51 | Penn State -18.4 / – | 52.4 / – | no line yet | no line yet (fair: Penn State -865) | no line yet |  |
| Sat 11/21 TBA | Wisconsin @ Purdue | Wisconsin 28, Purdue 21 | Wisconsin 69% | Wisconsin -220 / Purdue +220 | 27.5 – 20.6 | 14–42 / 7–34 | Wisconsin -6.9 / – | 48.1 / – | no line yet | no line yet (fair: Wisconsin -220) | no line yet |  |
| Sat 11/21 TBA | Maryland @ USC | Maryland 20, USC 34 | USC 82% | Maryland +465 / USC -465 | 20.8 – 34.5 | 7–34 / 20–50 | USC -13.7 / – | 55.3 / – | no line yet | no line yet (fair: USC -465) | no line yet |  |
| Sat 11/21 TBA | Indiana @ Washington | Indiana 27, Washington 17 | Indiana 77% | Indiana -325 / Washington +325 | 27.1 – 16.8 | 13–42 / 6–29 | Indiana -10.2 / – | 43.9 / – | no line yet | no line yet (fair: Indiana -325) | no line yet |  |
| Sat 11/21 TBA | Charlotte @ Tulsa | Charlotte 14, Tulsa 38 | Tulsa 95% | Charlotte +1760 / Tulsa -1760 | 14.7 – 37.8 | 3–27 / 23–54 | Tulsa -23.1 / – | 54.2 / – | no line yet | no line yet (fair: Tulsa -1760) | no line yet |  |
| Sat 11/21 TBA | South Florida @ Florida Atlantic | South Florida 31, Florida Atlantic 34 | Florida Atlantic 55% | South Florida +125 / Florida Atlantic -125 | 29.8 – 31.9 | 16–45 / 17–47 | Florida Atlantic -2.1 / – | 61.7 / – | no line yet | no line yet (fair: Florida Atlantic -125) | no line yet |  |
| Sat 11/21 TBA | North Texas @ Tulane | North Texas 34, Tulane 27 | North Texas 70% | North Texas -230 / Tulane +230 | 35.6 – 27.1 | 20–51 / 13–42 | North Texas -8.5 / – | 62.7 / – | no line yet | no line yet (fair: North Texas -230) | no line yet |  |
| Sat 11/21 TBA | UTSA @ UAB | UTSA 31, UAB 24 | UTSA 73% | UTSA -265 / UAB +265 | 31.4 – 22.6 | 17–46 / 10–36 | UTSA -8.8 / – | 53.9 / – | no line yet | no line yet (fair: UTSA -265) | no line yet |  |
| Sat 11/21 TBA | Hawai'i @ Nevada | Hawai'i 27, Nevada 24 | Hawai'i 58% | Hawai'i -135 / Nevada +135 | 25.5 – 22.8 | 13–40 / 10–37 | Hawai'i -2.7 / – | 48.3 / – | no line yet | no line yet (fair: Hawai'i -135) | no line yet |  |
| Sat 11/21 TBA | UL Monroe @ App State | UL Monroe 21, App State 31 | App State 76% | UL Monroe +315 / App State -315 | 21.8 – 32.3 | 9–35 / 17–48 | App State -10.5 / – | 54.2 / – | no line yet | no line yet (fair: App State -315) | no line yet |  |
| Sat 11/21 TBA | Arkansas State @ Louisiana Tech | Arkansas State 21, Louisiana Tech 31 | Louisiana Tech 77% | Arkansas State +340 / Louisiana Tech -340 | 19.8 – 30.7 | 7–33 / 17–45 | Louisiana Tech -10.9 / – | 50.5 / – | no line yet | no line yet (fair: Louisiana Tech -340) | no line yet |  |
| Sat 11/21 TBA | Coastal Carolina @ Louisiana | Coastal Carolina 24, Louisiana 27 | Louisiana 61% | Coastal Carolina +155 / Louisiana -155 | 23.3 – 27.6 | 10–37 / 14–42 | Louisiana -4.3 / – | 50.8 / – | no line yet | no line yet (fair: Louisiana -155) | no line yet |  |
| Sat 11/21 TBA | Georgia Southern @ Troy | Georgia Southern 27, Troy 24 | Georgia Southern 61% | Georgia Southern -160 / Troy +160 | 27.1 – 22.8 | 13–42 / 10–37 | Georgia Southern -4.4 / – | 49.9 / – | no line yet | no line yet (fair: Georgia Southern -160) | no line yet |  |
| Sat 11/21 TBA | Georgia State @ Marshall | Georgia State 28, Marshall 31 | Marshall 55% | Georgia State +120 / Marshall -120 | 28.1 – 29.7 | 14–42 / 16–45 | Marshall -1.5 / – | 57.8 / – | no line yet | no line yet (fair: Marshall -120) | no line yet |  |
| Sat 11/21 TBA | South Alabama @ Southern Miss | South Alabama 31, Southern Miss 28 | South Alabama 57% | South Alabama -130 / Southern Miss +130 | 31.4 – 28.8 | 17–46 / 14–44 | South Alabama -2.6 / – | 60.2 / – | no line yet | no line yet (fair: South Alabama -130) | no line yet |  |
| Sat 11/21 12:00 PM | Wofford @ Ole Miss | Wofford 3, Ole Miss 59 | Ole Miss 100% | Wofford +9900 / Ole Miss -9900 | 3.0 – 57.7 | 0–7 / 44–73 | Ole Miss -54.7 / – | 60.7 / – | no line yet | no line yet (fair: Ole Miss -9900) | no line yet | FCS opponent |
| Sat 11/21 12:00 PM | East Carolina @ Army | East Carolina 24, Army 27 | Army 56% | East Carolina +125 / Army -125 | 25.9 – 28.0 | 13–41 / 14–42 | Army -2.1 / – | 54.0 / – | no line yet | no line yet (fair: Army -125) | no line yet |  |
| Sat 11/21 12:00 PM | Memphis @ Navy | Memphis 28, Navy 31 | Memphis 51% | Memphis -105 / Navy +105 | 29.6 – 29.0 | 16–44 / 14–44 | Memphis -0.6 / – | 58.7 / – | no line yet | no line yet (fair: Memphis -105) | no line yet |  |
| Sat 11/21 1:00 PM | Tennessee Tech @ Mississippi State | Tennessee Tech 10, Mississippi State 41 | Mississippi State 99% | Tennessee Tech +9185 / Mississippi State -9185 | 10.2 – 41.5 | 0–20 / 27–58 | Mississippi State -31.3 / – | 51.7 / – | no line yet | no line yet (fair: Mississippi State -9185) | no line yet | FCS opponent |
| Sat 11/21 1:00 PM | Western Kentucky @ Liberty | Western Kentucky 17, Liberty 34 | Liberty 88% | Western Kentucky +760 / Liberty -760 | 18.1 – 35.4 | 7–31 / 20–51 | Liberty -17.3 / – | 53.6 / – | no line yet | no line yet (fair: Liberty -760) | no line yet |  |
| Sat 11/21 2:00 PM | Chattanooga @ Alabama | Chattanooga 3, Alabama 55 | Alabama 100% | Chattanooga +9900 / Alabama -9900 | 3.0 – 55.6 | 0–7 / 41–72 | Alabama -52.6 / – | 58.6 / – | no line yet | no line yet (fair: Alabama -9900) | no line yet | FCS opponent |
| Sat 11/21 2:00 PM | Missouri State @ Jacksonville State | Missouri State 21, Jacksonville State 35 | Jacksonville State 82% | Missouri State +450 / Jacksonville State -450 | 21.1 – 34.3 | 7–34 / 20–50 | Jacksonville State -13.2 / – | 55.4 / – | no line yet | no line yet (fair: Jacksonville State -450) | no line yet |  |
| Sat 11/21 2:00 PM | Middle Tennessee @ Sam Houston | Middle Tennessee 24, Sam Houston 21 | Middle Tennessee 52% | Middle Tennessee -105 / Sam Houston +105 | 22.7 – 21.9 | 10–36 / 10–35 | Middle Tennessee -0.8 / – | 44.6 / – | no line yet | no line yet (fair: Middle Tennessee -105) | no line yet |  |
| Sat 11/21 3:00 PM | Delaware @ New Mexico State | Delaware 31, New Mexico State 24 | Delaware 71% | Delaware -250 / New Mexico State +250 | 31.8 – 23.2 | 17–47 / 10–37 | Delaware -8.6 / – | 55.0 / – | no line yet | no line yet (fair: Delaware -250) | no line yet |  |
| Sat 11/21 3:00 PM | Florida International @ Kennesaw State | Florida International 21, Kennesaw State 24 | Kennesaw State 64% | Florida International +180 / Kennesaw State -180 | 21.0 – 26.6 | 9–34 / 13–41 | Kennesaw State -5.6 / – | 47.6 / – | no line yet | no line yet (fair: Kennesaw State -180) | no line yet |  |
| Sat 11/21 3:30 PM | Samford @ Auburn | Samford 3, Auburn 48 | Auburn 100% | Samford +9900 / Auburn -9900 | 3.0 – 47.3 | 0–7 / 32–63 | Auburn -44.3 / – | 50.3 / – | no line yet | no line yet (fair: Auburn -9900) | no line yet | FCS opponent |
| Sat 11/21 3:30 PM | Old Dominion @ UConn | Old Dominion 17, UConn 31 | UConn 84% | Old Dominion +535 / UConn -535 | 16.7 – 30.9 | 6–28 / 17–46 | UConn -14.2 / – | 47.6 / – | no line yet | no line yet (fair: UConn -535) | no line yet |  |
| Sat 11/21 4:00 PM | Northern Illinois @ North Dakota State | Northern Illinois 13, North Dakota State 34 | North Dakota State 94% | Northern Illinois +1520 / North Dakota State -1520 | 13.3 – 34.7 | 3–24 / 20–50 | North Dakota State -21.4 / – | 48.0 / – | no line yet | no line yet (fair: North Dakota State -1520) | no line yet |  |
| Sat 11/21 6:00 PM | Washington State @ Texas State | Washington State 24, Texas State 34 | Texas State 77% | Washington State +345 / Texas State -345 | 23.5 – 35.3 | 10–38 / 20–51 | Texas State -11.7 / – | 58.8 / – | no line yet | no line yet (fair: Texas State -345) | no line yet |  |
| Sat 11/21 7:00 PM | UNLV @ San José State | UNLV 31, San José State 24 | UNLV 68% | UNLV -210 / San José State +210 | 29.2 – 22.1 | 14–44 / 10–35 | UNLV -7.1 / – | 51.3 / – | no line yet | no line yet (fair: UNLV -210) | no line yet |  |
| Sat 11/21 7:30 PM | SMU @ Notre Dame | SMU 17, Notre Dame 34 | Notre Dame 86% | SMU +625 / Notre Dame -625 | 20.0 – 36.3 | 7–33 / 21–52 | Notre Dame -13.9 / Notre Dame -16.5 | 53.1 / 57.5 | no edge | no edge | no edge |  |
| Sat 11/21 7:30 PM | Colorado State @ Fresno State | Colorado State 24, Fresno State 34 | Fresno State 74% | Colorado State +290 / Fresno State -290 | 25.1 – 35.1 | 12–39 / 20–51 | Fresno State -10.0 / – | 60.2 / – | no line yet | no line yet (fair: Fresno State -290) | no line yet |  |
| Sat 11/21 9:30 PM | San Diego State @ Boise State | San Diego State 21, Boise State 38 | Boise State 86% | San Diego State +630 / Boise State -630 | 20.0 – 36.3 | 7–34 / 21–52 | Boise State -16.4 / – | 56.3 / – | no line yet | no line yet (fair: Boise State -630) | no line yet |  |
| Sat 11/21 10:30 PM | Utah State @ Oregon State | Utah State 24, Oregon State 31 | Oregon State 74% | Utah State +280 / Oregon State -280 | 21.7 – 31.2 | 10–35 / 17–46 | Oregon State -9.5 / – | 53.0 / – | no line yet | no line yet (fair: Oregon State -280) | no line yet |  |

## How the 2026 predictions have done

| Predictor | Games | Margin MAE | Total MAE | Team-score MAE | Winners | Brier | 80% range hit |
|---|---|---|---|---|---|---|---|
| Final prediction | 685 | 11.76 | 12.26 | 8.47 | 79.1% | 0.145 | 81.8% |
| Model only (before blending) | 685 | 12.51 | 12.62 | 8.76 | 76.2% | – | – |
| Betting line when predicted | 683 | 11.75 | 12.21 | 8.46 | 79.2% | – | – |

MAE is mean absolute error in points (lower is better). Brier scores the win chances (lower is better, 0.25 is a coin flip). Even the closing betting line misses the final margin of an FBS game by about 12.5 points.

501 of these games were played before the predictor went live. They are backfilled walk-forward (each week predicted from earlier weeks only) but with closing lines, so they flatter the model slightly. Every game since is graded on the prediction logged before kickoff.

### Betting edges

| Market | Edges | Record (W-L-P) | Staked | Units won | ROI | Expected ROI |
|---|---|---|---|---|---|---|
| Spread | 0 | 0-0-0 | 0.0 | +0.00 | – | – |
| Moneyline | 8 | 1-7-0 | 2.7 | -0.68 | -25.4% | +4.6% |
| Total | 6 | 2-4-0 | 8.3 | -0.81 | -9.8% | +7.2% |

6 of these edges were priced at an assumed -110 (price not posted).

Every edge logged before kickoff at the stake and price logged with it (backfilled games, and edges logged before edges were priced from the final prediction, are not included). Units are 1% of the bankroll; ROI is units won per unit staked, pushes returning the stake, and expected ROI is what the edges' EVs promised.

### Week 10 results

| Game | Predicted | Final | Win chance for winner | Inside 80% ranges |
|---|---|---|---|---|
| Ohio @ Akron | 31–17 | 28–20 | 84% | yes |
| Buffalo @ Miami (OH) | 17–24 | 34–31 | 32% | no |
| Ball State @ Massachusetts | 24–27 | 30–31 | 57% | yes |
| Toledo @ Sacramento State | 38–14 | 20–17 | 96% | no |
| Central Michigan vs Eastern Michigan | 21–24 | 35–7 | 47% | no |
| UTSA @ Florida Atlantic | 38–31 | 29–60 | 35% | no |
| James Madison @ Southern Miss | 34–21 | 54–23 | 82% | no |
| Virginia Tech @ SMU | 24–31 | 28–51 | 67% | no |
| South Florida @ East Carolina | 17–20 | 17–20 | 55% | yes |
| Nebraska @ Illinois | 27–24 | 13–24 | 39% | no |
| New Mexico @ Nevada | 24–17 | 31–3 | 78% | yes |
| TCU @ Arizona | 21–28 | 28–29 | 70% | yes |
| Texas @ Missouri | 20–17 | 34–20 | 56% | yes |
| BYU @ Utah | 24–27 | 20–28 | 63% | yes |
| Iowa State @ Baylor | 21–28 | 31–42 | 75% | yes |
| Clemson @ Syracuse | 27–24 | 18–13 | 56% | yes |
| Florida State @ Boston College | 31–24 | 31–24 | 67% | yes |
| North Carolina @ UConn | 31–24 | 38–21 | 67% | yes |
| UCLA @ Minnesota | 24–17 | 34–20 | 64% | yes |
| Tulsa @ Tulane | 27–24 | 60–10 | 55% | no |
| Duke @ NC State | 27–24 | 41–3 | 61% | no |
| Maryland @ Purdue | 24–31 | 34–29 | 37% | yes |
| Arkansas @ Auburn | 21–31 | 23–26 | 77% | yes |
| Oklahoma State @ Kansas State | 34–31 | 66–28 | 64% | no |
| Old Dominion @ Coastal Carolina | 17–24 | 21–8 | 33% | no |
| Georgia State @ App State | 24–31 | 39–23 | 34% | no |
| Texas A&M @ South Carolina | 24–31 | 9–17 | 67% | no |
| UL Monroe @ Arkansas State | 20–34 | 19–17 | 17% | no |
| Delaware @ Kennesaw State | 27–24 | 40–42 | 49% | yes |
| Alabama @ LSU | 24–31 | 31–13 | 33% | no |
| Cincinnati @ Houston | 24–34 | 24–31 | 75% | yes |
| Merrimack @ Wake Forest | 3–52 | 0–77 | 100% | no |
| Oregon @ Ohio State | 17–24 | 41–28 | 29% | no |
| Penn State @ Washington | 21–24 | 28–25 | 44% | yes |
| Charlotte @ UAB | 20–27 | 12–23 | 74% | yes |
| Temple @ Navy | 24–31 | 35–42 | 69% | yes |
| Marshall @ Georgia Southern | 24–31 | 13–49 | 68% | no |
| Western Kentucky @ Middle Tennessee | 27–24 | 42–51 | 44% | no |
| UCF @ Kansas | 21–24 | 33–32 | 37% | yes |
| Rice @ North Texas | 24–41 | 23–52 | 84% | yes |
| Northern Illinois @ San José State | 21–31 | 19–30 | 79% | yes |
| Missouri State @ Florida International | 24–27 | 20–23 | 62% | yes |
| Louisiana Tech @ Troy | 28–21 | 41–17 | 68% | yes |
| Vanderbilt @ Mississippi State | 24–27 | 25–23 | 42% | yes |
| Rutgers @ Wisconsin | 14–31 | 10–31 | 92% | yes |
| South Alabama @ Louisiana | 24–31 | 26–28 | 67% | yes |
| Boise State @ Colorado State | 41–24 | 64–38 | 85% | no |
| Kentucky @ Tennessee | 21–28 | 6–34 | 66% | no |
| Sam Houston @ Jacksonville State | 14–31 | 14–47 | 88% | no |
| Georgia @ Ole Miss | 27–24 | 42–7 | 58% | no |
| Colorado @ Arizona State | 24–27 | 10–20 | 60% | yes |
| Louisville @ Georgia Tech | 38–24 | 44–17 | 84% | yes |
| Miami @ Notre Dame | 24–31 | 24–31 | 68% | yes |
| Michigan State @ Michigan | 14–28 | 15–6 | 14% | no |
| Iowa @ Northwestern | 24–21 | 24–10 | 56% | yes |
| Air Force @ Army | 21–24 | 24–21 | 40% | yes |
| Oklahoma @ Florida | 21–24 | 23–7 | 37% | no |
| Liberty @ New Mexico State | 31–14 | 30–14 | 85% | yes |
| West Virginia @ Texas Tech | 24–41 | 48–53 | 86% | no |
| Fresno State @ Utah State | 24–21 | 10–17 | 51% | yes |
| Hawai'i @ UTEP | 28–21 | 17–14 | 71% | yes |
| Texas State @ Oregon State | 31–38 | 42–21 | 36% | no |
| Wyoming @ UNLV | 24–27 | 41–35 | 39% | no |

## FBS power ratings

Points per game better than an average FBS team on a neutral field, from opponent-adjusted EPA (garbage time removed) with this season's games weighted against a preseason prior, plus the weight the margin model puts on Elo (a rating built from game results alone). Defense is positive when it holds opponents below average.

| # | Team | Conference | Net | Offense | Defense | Special teams | Results (Elo) | Elo rating |
|---|---|---|---|---|---|---|---|---|
| 1 | Georgia | SEC | +25.7 | +8.2 | +11.6 | +0.8 | +5.1 | 1931 |
| 2 | LSU | SEC | +23.8 | +9.6 | +11.9 | +0.0 | +2.4 | 1703 |
| 3 | Notre Dame | FBS Independents | +23.3 | +8.6 | +9.1 | +1.0 | +4.6 | 1888 |
| 4 | Ohio State | Big Ten | +23.2 | +10.2 | +9.2 | +0.3 | +3.6 | 1805 |
| 5 | Miami | ACC | +23.0 | +14.2 | +4.1 | +0.4 | +4.3 | 1865 |
| 6 | Alabama | SEC | +22.0 | +9.5 | +8.3 | +0.3 | +3.8 | 1825 |
| 7 | Indiana | Big Ten | +21.3 | +5.4 | +10.5 | +0.1 | +5.2 | 1939 |
| 8 | Utah | Big 12 | +20.4 | +10.2 | +6.1 | -0.1 | +4.3 | 1862 |
| 9 | Texas | SEC | +19.8 | +2.3 | +12.6 | +0.8 | +4.1 | 1848 |
| 10 | Oregon | Big Ten | +19.5 | +5.8 | +9.6 | +0.5 | +3.6 | 1806 |
| 11 | UCLA | Big Ten | +17.9 | +5.5 | +9.1 | +0.9 | +2.4 | 1709 |
| 12 | Tennessee | SEC | +17.3 | +4.3 | +8.8 | +1.2 | +3.0 | 1758 |
| 13 | Texas Tech | Big 12 | +17.2 | +2.9 | +10.0 | +1.3 | +3.1 | 1767 |
| 14 | Wake Forest | ACC | +17.2 | +6.6 | +7.7 | +0.5 | +2.5 | 1712 |
| 15 | Ole Miss | SEC | +16.6 | +9.4 | +3.4 | +0.7 | +3.1 | 1764 |
| 16 | Louisville | ACC | +16.5 | +9.8 | +4.1 | +0.2 | +2.3 | 1699 |
| 17 | Oklahoma | SEC | +16.4 | +1.0 | +12.9 | +0.6 | +1.8 | 1659 |
| 18 | Iowa | Big Ten | +14.4 | +1.5 | +8.6 | +1.0 | +3.3 | 1783 |
| 19 | Missouri | SEC | +14.4 | +4.2 | +7.7 | +0.4 | +2.1 | 1680 |
| 20 | SMU | ACC | +13.9 | +8.1 | +3.2 | +0.3 | +2.3 | 1700 |
| 21 | USC | Big Ten | +13.9 | +10.5 | +0.4 | +0.3 | +2.8 | 1738 |
| 22 | BYU | Big 12 | +13.2 | +5.2 | +4.5 | +0.7 | +2.8 | 1739 |
| 23 | South Carolina | SEC | +12.4 | +5.8 | +4.0 | +0.6 | +2.1 | 1683 |
| 24 | Michigan | Big Ten | +12.3 | +2.2 | +9.3 | -0.3 | +1.1 | 1602 |
| 25 | Arizona | Big 12 | +12.0 | +5.9 | +3.6 | +0.1 | +2.5 | 1713 |
| 26 | Penn State | Big Ten | +11.9 | +3.7 | +6.6 | +0.0 | +1.6 | 1640 |
| 27 | Nebraska | Big Ten | +11.7 | +3.4 | +7.4 | +0.3 | +0.6 | 1558 |
| 28 | Auburn | SEC | +11.6 | +5.0 | +5.5 | +0.6 | +0.5 | 1550 |
| 29 | Texas A&M | SEC | +11.3 | +2.4 | +7.6 | +0.4 | +0.9 | 1579 |
| 30 | Houston | Big 12 | +10.6 | +8.3 | -0.2 | +0.3 | +2.2 | 1690 |
| 31 | Florida | SEC | +10.6 | +5.7 | +3.8 | +0.8 | +0.3 | 1534 |
| 32 | Oklahoma State | Big 12 | +10.0 | +9.2 | -0.3 | +0.5 | +0.6 | 1556 |
| 33 | Northwestern | Big Ten | +9.6 | +6.0 | +1.9 | +0.6 | +1.1 | 1602 |
| 34 | Baylor | Big 12 | +9.4 | +0.7 | +6.3 | +0.9 | +1.4 | 1628 |
| 35 | Duke | ACC | +8.8 | +3.6 | +1.9 | +0.7 | +2.5 | 1716 |
| 36 | Wisconsin | Big Ten | +8.7 | -0.2 | +7.3 | +0.4 | +1.2 | 1608 |
| 37 | Washington | Big Ten | +8.7 | +2.2 | +4.7 | +0.1 | +1.6 | 1642 |
| 38 | Mississippi State | SEC | +8.4 | +4.5 | +4.1 | -0.1 | -0.2 | 1493 |
| 39 | Kentucky | SEC | +8.3 | +2.6 | +4.1 | +0.1 | +1.6 | 1642 |
| 40 | Iowa State | Big 12 | +6.9 | +4.7 | +0.9 | +1.0 | +0.3 | 1536 |
| 41 | Kansas | Big 12 | +6.6 | +5.0 | +2.8 | -0.2 | -1.0 | 1428 |
| 42 | Boise State | Pac-12 | +6.4 | +6.3 | -2.3 | -0.2 | +2.7 | 1730 |
| 43 | Illinois | Big Ten | +6.4 | +6.8 | -2.2 | +0.3 | +1.6 | 1638 |
| 44 | Kansas State | Big 12 | +6.4 | +4.6 | +2.2 | +0.2 | -0.7 | 1454 |
| 45 | Cincinnati | Big 12 | +5.9 | +9.2 | -4.1 | +0.3 | +0.5 | 1551 |
| 46 | Arizona State | Big 12 | +5.8 | +0.9 | +4.3 | -0.1 | +0.7 | 1565 |
| 47 | Clemson | ACC | +5.7 | -4.7 | +8.2 | +0.8 | +1.4 | 1627 |
| 48 | Florida State | ACC | +5.6 | +7.6 | -1.2 | -0.7 | -0.1 | 1499 |
| 49 | TCU | Big 12 | +5.4 | -2.1 | +6.6 | +0.1 | +0.9 | 1582 |
| 50 | Vanderbilt | SEC | +4.9 | +3.6 | +0.4 | +0.5 | +0.5 | 1547 |
| 51 | Virginia Tech | ACC | +4.3 | +3.9 | -0.1 | +0.1 | +0.4 | 1541 |
| 52 | Pittsburgh | ACC | +4.0 | -1.2 | +4.0 | +0.6 | +0.7 | 1566 |
| 53 | North Carolina | ACC | +3.8 | +3.4 | -0.9 | +0.8 | +0.6 | 1554 |
| 54 | North Texas | American Athletic | +3.8 | +10.4 | -7.5 | -0.8 | +1.7 | 1651 |
| 55 | UCF | Big 12 | +3.5 | +1.4 | +2.4 | +0.2 | -0.5 | 1470 |
| 56 | James Madison | Sun Belt | +3.4 | -1.0 | +1.5 | +0.4 | +2.4 | 1711 |
| 57 | Minnesota | Big Ten | +3.0 | -3.6 | +5.5 | +0.8 | +0.2 | 1529 |
| 58 | Colorado | Big 12 | +2.0 | -0.1 | +4.5 | -0.6 | -1.7 | 1364 |
| 59 | Maryland | Big Ten | +2.0 | -0.2 | +3.0 | +0.8 | -1.6 | 1374 |
| 60 | Memphis | American Athletic | +1.8 | +3.4 | -2.4 | -0.4 | +1.3 | 1614 |
| 61 | Liberty | Conference USA | +1.8 | +1.9 | -1.3 | +0.4 | +0.7 | 1568 |
| 62 | NC State | ACC | +1.7 | +5.0 | -2.8 | -0.4 | -0.1 | 1498 |
| 63 | Texas State | Pac-12 | +1.7 | +6.1 | -4.4 | -1.1 | +1.1 | 1602 |
| 64 | Syracuse | ACC | +1.6 | +1.1 | +2.6 | -0.8 | -1.4 | 1392 |
| 65 | West Virginia | Big 12 | +1.4 | +6.2 | -5.1 | +0.4 | -0.2 | 1495 |
| 66 | Virginia | ACC | +1.3 | -1.3 | +3.3 | -0.5 | -0.2 | 1494 |
| 67 | UTSA | American Athletic | +1.0 | +3.6 | -3.6 | -0.0 | +1.1 | 1596 |
| 68 | Arkansas | SEC | +0.9 | +1.4 | +0.8 | -0.7 | -0.6 | 1455 |
| 69 | New Mexico | Mountain West | +0.6 | -3.7 | +3.0 | -0.2 | +1.5 | 1636 |
| 70 | Tulsa | American Athletic | -0.2 | +0.5 | +0.5 | -0.6 | -0.5 | 1466 |
| 71 | Oregon State | Pac-12 | -0.2 | +3.4 | -2.7 | +0.0 | -1.0 | 1428 |
| 72 | Toledo | Mid-American | -0.8 | -2.5 | +1.4 | -0.3 | +0.6 | 1559 |
| 73 | Purdue | Big Ten | -0.8 | +2.9 | -3.0 | +0.7 | -1.5 | 1386 |
| 74 | Navy | American Athletic | -1.0 | +3.5 | -3.6 | -0.6 | -0.3 | 1484 |
| 75 | Michigan State | Big Ten | -1.1 | -3.3 | +2.1 | +0.6 | -0.6 | 1459 |
| 76 | North Dakota State | Mountain West | -1.5 | -5.0 | +3.5 | +1.1 | -1.1 | 1419 |
| 77 | South Florida | American Athletic | -1.8 | -2.3 | -0.3 | +0.1 | +0.7 | 1569 |
| 78 | Louisiana Tech | Sun Belt | -2.4 | -3.4 | +0.9 | -0.8 | +0.8 | 1575 |
| 79 | Florida Atlantic | American Athletic | -2.7 | +4.8 | -8.1 | +0.7 | -0.0 | 1506 |
| 80 | East Carolina | American Athletic | -3.0 | -5.3 | +2.7 | -0.5 | +0.1 | 1520 |
| 81 | UConn | FBS Independents | -3.5 | +1.2 | -3.6 | -0.1 | -1.0 | 1427 |
| 82 | Fresno State | Pac-12 | -3.6 | -2.8 | -0.8 | -0.3 | +0.3 | 1530 |
| 83 | Ohio | Mid-American | -3.7 | -1.9 | -2.9 | +0.2 | +0.9 | 1586 |
| 84 | Army | American Athletic | -3.8 | +4.5 | -8.4 | -0.1 | +0.2 | 1525 |
| 85 | Air Force | Mountain West | -4.3 | +2.1 | -6.4 | -0.2 | +0.1 | 1517 |
| 86 | Rutgers | Big Ten | -4.8 | +2.4 | -6.2 | +0.7 | -1.6 | 1373 |
| 87 | Jacksonville State | Conference USA | -4.8 | -0.2 | -4.5 | -0.1 | -0.0 | 1505 |
| 88 | Boston College | ACC | -5.6 | -3.6 | -0.5 | -0.6 | -0.9 | 1431 |
| 89 | Georgia Southern | Sun Belt | -5.8 | -1.7 | -4.0 | -0.7 | +0.6 | 1556 |
| 90 | Georgia Tech | ACC | -6.0 | +0.5 | -4.6 | -0.2 | -1.6 | 1375 |
| 91 | California | ACC | -6.0 | -2.2 | -1.7 | -0.4 | -1.7 | 1369 |
| 92 | Utah State | Pac-12 | -6.2 | -6.9 | +2.5 | -1.1 | -0.6 | 1455 |
| 93 | UNLV | Mountain West | -6.5 | -2.8 | -3.7 | +0.2 | -0.1 | 1497 |
| 94 | Western Michigan | Mid-American | -7.0 | -4.9 | -3.6 | +0.8 | +0.6 | 1561 |
| 95 | Delaware | Conference USA | -7.2 | -0.3 | -5.6 | +0.1 | -1.4 | 1389 |
| 96 | San Diego State | Pac-12 | -8.1 | -4.6 | -2.5 | +0.3 | -1.2 | 1406 |
| 97 | Tulane | American Athletic | -8.1 | -4.8 | -2.9 | +0.2 | -0.7 | 1454 |
| 98 | Washington State | Pac-12 | -8.4 | -6.1 | -0.0 | -0.3 | -1.9 | 1349 |
| 99 | Stanford | ACC | -8.5 | -2.6 | -5.1 | -0.1 | -0.7 | 1448 |
| 100 | Georgia State | Sun Belt | -8.9 | -0.6 | -7.1 | -0.0 | -1.2 | 1407 |
| 101 | Wyoming | Mountain West | -9.2 | -5.4 | -3.0 | -0.2 | -0.6 | 1460 |
| 102 | Miami (OH) | Mid-American | -9.2 | -4.9 | -4.1 | +0.8 | -1.1 | 1421 |
| 103 | Marshall | Sun Belt | -9.7 | -5.0 | -4.0 | -0.0 | -0.6 | 1456 |
| 104 | App State | Sun Belt | -9.8 | -3.8 | -3.7 | -0.5 | -1.8 | 1361 |
| 105 | Louisiana | Sun Belt | -9.8 | -4.8 | -4.6 | -0.2 | -0.2 | 1488 |
| 106 | Temple | American Athletic | -9.9 | +0.4 | -7.1 | -0.4 | -2.8 | 1279 |
| 107 | UAB | American Athletic | -10.1 | -7.1 | -1.7 | -0.2 | -1.1 | 1419 |
| 108 | Hawai'i | Mountain West | -10.5 | -3.8 | -6.1 | +1.0 | -1.6 | 1374 |
| 109 | Colorado State | Pac-12 | -11.4 | +4.7 | -13.2 | -0.2 | -2.8 | 1278 |
| 110 | Central Michigan | Mid-American | -11.5 | -6.1 | -4.2 | -0.1 | -1.1 | 1418 |
| 111 | Arkansas State | Sun Belt | -11.7 | -3.2 | -7.3 | +0.0 | -1.2 | 1408 |
| 112 | Troy | Sun Belt | -11.9 | -8.5 | -0.3 | -1.3 | -1.7 | 1366 |
| 113 | South Alabama | Sun Belt | -12.0 | -0.1 | -10.8 | +0.3 | -1.5 | 1388 |
| 114 | Kennesaw State | Conference USA | -12.1 | -6.2 | -3.6 | -0.5 | -1.8 | 1363 |
| 115 | Coastal Carolina | Sun Belt | -12.3 | -6.8 | -3.9 | +0.5 | -2.1 | 1334 |
| 116 | Old Dominion | Sun Belt | -12.4 | -13.7 | +4.2 | -1.6 | -1.2 | 1407 |
| 117 | Western Kentucky | Conference USA | -12.5 | -5.3 | -4.5 | -0.2 | -2.4 | 1306 |
| 118 | Rice | American Athletic | -13.0 | -3.6 | -5.3 | -0.8 | -3.2 | 1240 |
| 119 | Florida International | Conference USA | -14.2 | -10.4 | -0.6 | -1.5 | -1.7 | 1366 |
| 120 | Missouri State | Conference USA | -14.5 | -3.1 | -7.3 | -1.2 | -2.9 | 1268 |
| 121 | Nevada | Mountain West | -15.0 | -11.0 | -2.0 | +0.4 | -2.4 | 1309 |
| 122 | Southern Miss | Sun Belt | -15.6 | -8.1 | -4.0 | -1.2 | -2.3 | 1318 |
| 123 | San José State | Mountain West | -15.8 | -10.1 | -3.4 | +0.0 | -2.3 | 1318 |
| 124 | New Mexico State | Conference USA | -16.2 | -7.7 | -3.6 | -1.9 | -3.0 | 1258 |
| 125 | Buffalo | Mid-American | -16.9 | -11.4 | -5.3 | +0.3 | -0.5 | 1469 |
| 126 | UL Monroe | Sun Belt | -17.0 | -5.8 | -6.2 | -1.3 | -3.7 | 1201 |
| 127 | Middle Tennessee | Conference USA | -17.1 | -5.8 | -8.7 | -0.0 | -2.6 | 1296 |
| 128 | Massachusetts | Mid-American | -17.2 | -9.1 | -4.4 | -0.3 | -3.4 | 1229 |
| 129 | Ball State | Mid-American | -17.3 | -5.8 | -7.7 | -0.6 | -3.2 | 1241 |
| 130 | Northern Illinois | Mountain West | -18.3 | -3.8 | -8.9 | -1.1 | -4.6 | 1130 |
| 131 | Bowling Green | Mid-American | -18.6 | -11.8 | -4.0 | -0.0 | -2.9 | 1270 |
| 132 | Sam Houston | Conference USA | -19.0 | -12.5 | -0.7 | -1.3 | -4.5 | 1136 |
| 133 | Eastern Michigan | Mid-American | -19.1 | -7.9 | -7.8 | -0.6 | -2.7 | 1287 |
| 134 | Sacramento State | Mid-American | -20.4 | -11.9 | -4.4 | +0.3 | -4.4 | 1147 |
| 135 | Charlotte | American Athletic | -20.8 | -8.2 | -8.1 | -0.7 | -3.8 | 1190 |
| 136 | Kent State | Mid-American | -20.9 | -10.8 | -6.1 | -0.8 | -3.2 | 1241 |
| 137 | Akron | Mid-American | -22.7 | -10.3 | -7.9 | -0.8 | -3.8 | 1198 |
| 138 | UTEP | Mountain West | -24.5 | -11.6 | -6.8 | -1.2 | -4.9 | 1103 |

## Current model fit

- Fitted on 4302 games from seasons 2022–2026.
- Home field on top of the ratings: 3.2 points (1.8 in conference games).
- Extra FBS edge over FCS opponents beyond their ratings: 14.1 points.
- Elo weight: 0.19 points of margin per point of Elo spread.
- Weight on the betting line: 92% for the margin, 82% for the total.
