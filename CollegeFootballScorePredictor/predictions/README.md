# College football score predictions

Updated Sat Nov 14, 2026 08:51 PM ET. Refreshed automatically every day of the season and several times on Saturdays; each game's prediction is locked at kickoff and graded once the final score is in. Scores are the most likely real scoreline near the expected points; ranges cover 80% of simulated outcomes for each team. College scores scatter widely, so read the ranges, not just the headline score.

Expected points blend the model with the betting line using the weight that has predicted best in recent seasons (see Current model fit). The spread and total columns show the model's own numbers next to the line, so you can see where it disagrees. Games without a line yet use the model alone.

The fair moneyline is the American odds that match the win chance exactly, with no bookmaker margin: -200 means risk $200 to win $100, +200 means risk $100 to win $200. A sportsbook's price will be a little worse on both sides because of its cut, so a book only offers value on a team when its price beats the fair line.

The edge columns judge each bet by its expected value per $1 staked at the posted price, using the final prediction: the model blended with the line, run through the score simulator, pushes included, and anchored to the market's own chances so that only what the blend moves off the line counts. The model's own spread and total (shown alongside) sit several points from the line in most games, but the blend keeps only the share of that disagreement the model has earned in past seasons, so edges are rare. The side with the higher value is shown when it reaches 3% (+3 cents per $1), as the team or side, the price, the expected value, its chance of winning the bet and its stake, a 25% share of the Kelly stake in units of 1% of the bankroll with at most 3 units on one game; anything short is no edge. Where a book posts no price for a spread or total it is assumed to be -110 and marked -110*; moneylines are never assumed. In the walk-forward backtest against closing lines, edges returned spread -100.0% on 1 bets (posted prices, 2016–2019); spread -3.9% on 156 bets (assumed -110 prices, 2016–2025); moneyline +13.7% on 575 bets (posted prices, 2016–2025); total +2.6% on 367 bets (posted prices, 2016–2019); total -5.7% on 172 bets (assumed -110 prices, 2016–2025). None of these is clearly above zero, so treat these edges as an experiment, not a betting system. The live record is tracked below, graded at the price logged with the last prediction before kickoff.

## 2026 Week 11

| Kickoff (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected points | 80% range | Spread: model / line | Total: model / line | Spread edge | Moneyline edge | Total edge | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sat 11/14 9:00 PM | North Texas @ UTSA | North Texas 38, UTSA 35 | North Texas 56% | North Texas -130 / UTSA +130 | 38.5 – 36.0 | 24–54 / 21–52 | UTSA -0.4 / North Texas -2.8 | 69.0 / 75.8 | no edge | no edge | no edge |  |
| Sat 11/14 9:30 PM | Texas Tech @ Oklahoma State | Texas Tech 34, Oklahoma State 37 | Oklahoma State 58% | Texas Tech +140 / Oklahoma State -140 | 34.0 – 37.2 | 20–49 / 21–52 | Texas Tech -5.9 / Oklahoma State -4.0 | 57.3 / 74.2 | no edge | no edge | Under 74.25 (-110*): EV +9.7%, 57%, stake 2.7u | * price not posted; assumed -110 |
| Sat 11/14 9:30 PM | Utah State @ San Diego State | Utah State 24, San Diego State 21 | Utah State 58% | Utah State -135 / San Diego State +135 | 23.4 – 20.8 | 10–37 / 7–34 | San Diego State -1.8 / Utah State -3.0 | 47.7 / 43.5 | no edge | no edge | no edge |  |
| Sat 11/14 10:00 PM | Wyoming @ UTEP | Wyoming 24, UTEP 17 | Wyoming 72% | Wyoming -255 / UTEP +255 | 24.6 – 17.1 | 10–38 / 6–29 | Wyoming -13.9 / Wyoming -7.0 | 45.9 / 40.8 | no edge | no edge | no edge |  |
| Sat 11/14 10:30 PM | Utah @ Arizona | Utah 31, Arizona 28 | Utah 56% | Utah -125 / Arizona +125 | 28.9 – 26.8 | 14–44 / 13–41 | Utah -6.1 / Utah -1.8 | 55.9 / 55.8 | no edge | no edge | no edge |  |
| Sat 11/14 10:30 PM | Colorado State @ Washington State | Colorado State 27, Washington State 34 | Washington State 70% | Colorado State +230 / Washington State -230 | 27.7 – 36.0 | 14–42 / 21–52 | Washington State -5.3 / Washington State -8.5 | 58.9 / 64.8 | no edge | no edge | no edge |  |
| Sat 11/14 11:00 PM | North Dakota State @ Hawai'i | North Dakota State 24, Hawai'i 17 | North Dakota State 70% | North Dakota State -230 / Hawai'i +230 | 23.9 – 16.9 | 10–38 / 6–28 | North Dakota State -7.0 / North Dakota State -7.0 | 47.4 / 39.5 | no edge | no edge | no edge |  |
| Sun 11/15 1:00 PM | Ole Miss @ Oklahoma | Ole Miss 24, Oklahoma 27 | Oklahoma 57% | Ole Miss +135 / Oklahoma -135 | 23.1 – 25.8 | 10–37 / 13–40 | Oklahoma -2.1 / Oklahoma -2.8 | 49.9 / 48.8 | no edge | no edge | no edge |  |

## 2026 Week 12

| Kickoff (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected points | 80% range | Spread: model / line | Total: model / line | Spread edge | Moneyline edge | Total edge | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tue 11/17 6:00 PM | Eastern Michigan @ Western Michigan | Eastern Michigan 17, Western Michigan 34 | Western Michigan 89% | Eastern Michigan +805 / Western Michigan -805 | 16.9 – 34.4 | 6–29 / 20–50 | Western Michigan -17.5 / – | 51.3 / – | no line yet | no line yet (fair: Western Michigan -805) | no line yet |  |
| Tue 11/17 7:00 PM | Ball State @ Ohio | Ball State 17, Ohio 34 | Ohio 86% | Ball State +605 / Ohio -605 | 17.4 – 33.0 | 6–30 / 17–49 | Ohio -15.6 / – | 50.5 / – | no line yet | no line yet (fair: Ohio -605) | no line yet |  |
| Tue 11/17 7:00 PM | Miami (OH) @ Kent State | Miami (OH) 31, Kent State 17 | Miami (OH) 83% | Miami (OH) -500 / Kent State +500 | 30.3 – 16.3 | 16–45 / 6–28 | Miami (OH) -14.0 / – | 46.7 / – | no line yet | no line yet (fair: Miami (OH) -500) | no line yet |  |
| Wed 11/18 7:00 PM | Akron @ Massachusetts | Akron 21, Massachusetts 28 | Massachusetts 71% | Akron +250 / Massachusetts -250 | 19.3 – 27.6 | 7–31 / 14–42 | Massachusetts -8.3 / – | 47.0 / – | no line yet | no line yet (fair: Massachusetts -250) | no line yet |  |
| Wed 11/18 7:30 PM | Central Michigan @ Buffalo | Central Michigan 27, Buffalo 24 | Central Michigan 53% | Central Michigan -110 / Buffalo +110 | 25.4 – 24.5 | 13–40 / 10–38 | Central Michigan -0.9 / – | 49.9 / – | no line yet | no line yet (fair: Central Michigan -110) | no line yet |  |
| Thu 11/19 7:30 PM | Rice @ Temple | Rice 24, Temple 27 | Temple 59% | Rice +145 / Temple -145 | 25.1 – 28.5 | 13–38 / 14–42 | Temple -3.4 / – | 53.5 / – | no line yet | no line yet (fair: Temple -145) | no line yet |  |
| Fri 11/20 6:00 PM | Iowa State @ UCF | Iowa State 27, UCF 24 | Iowa State 57% | Iowa State -130 / UCF +130 | 27.5 – 25.0 | 14–41 / 13–38 | Iowa State -2.5 / – | 52.6 / – | no line yet | no line yet (fair: Iowa State -130) | no line yet |  |
| Fri 11/20 7:30 PM | Clemson @ Duke | Clemson 17, Duke 24 | Duke 70% | Clemson +240 / Duke -240 | 19.2 – 26.9 | 7–31 / 13–41 | Duke -7.7 / – | 46.1 / – | no line yet | no line yet (fair: Duke -240) | no line yet |  |
| Fri 11/20 7:30 PM | Bowling Green @ Toledo | Bowling Green 10, Toledo 31 | Toledo 93% | Bowling Green +1265 / Toledo -1265 | 12.3 – 32.2 | 3–23 / 17–48 | Toledo -19.9 / – | 44.5 / – | no line yet | no line yet (fair: Toledo -1265) | no line yet |  |
| Fri 11/20 8:00 PM | Oregon @ Michigan State | Oregon 31, Michigan State 14 | Oregon 91% | Oregon -1060 / Michigan State +1060 | 32.9 – 14.0 | 17–48 / 3–24 | Oregon -18.9 / – | 46.8 / – | no line yet | no line yet (fair: Oregon -1060) | no line yet |  |
| Fri 11/20 8:00 PM | UTEP @ Air Force | UTEP 14, Air Force 38 | Air Force 95% | UTEP +2025 / Air Force -2025 | 13.6 – 37.2 | 3–24 / 21–52 | Air Force -23.6 / – | 51.2 / – | no line yet | no line yet (fair: Air Force -2025) | no line yet |  |
| Fri 11/20 9:00 PM | New Mexico @ Wyoming | New Mexico 24, Wyoming 17 | New Mexico 71% | New Mexico -240 / Wyoming +240 | 25.7 – 18.1 | 13–41 / 7–31 | New Mexico -7.6 / – | 43.8 / – | no line yet | no line yet (fair: New Mexico -240) | no line yet |  |
| Sat 11/21 TBA | Arizona @ Kansas State | Arizona 27, Kansas State 24 | Arizona 58% | Arizona -135 / Kansas State +135 | 26.6 – 23.6 | 13–41 / 10–38 | Arizona -3.0 / – | 54.5 / – | no line yet | no line yet (fair: Arizona -135) | no line yet |  |
| Sat 11/21 TBA | BYU @ Kansas | BYU 24, Kansas 21 | BYU 58% | BYU -140 / Kansas +140 | 26.3 – 23.2 | 13–41 / 10–37 | BYU -3.1 / – | 52.2 / – | no line yet | no line yet (fair: BYU -140) | no line yet |  |
| Sat 11/21 TBA | Houston @ West Virginia | Houston 38, West Virginia 31 | Houston 69% | Houston -225 / West Virginia +225 | 37.1 – 29.2 | 21–52 / 14–44 | Houston -7.9 / – | 66.2 / – | no line yet | no line yet (fair: Houston -225) | no line yet |  |
| Sat 11/21 TBA | Texas Tech @ Baylor | Texas Tech 27, Baylor 24 | Texas Tech 55% | Texas Tech -125 / Baylor +125 | 28.3 – 26.4 | 14–42 / 13–41 | Texas Tech -5.7 / Texas Tech -1.5 | 51.9 / 55.5 | no edge | no edge | no edge |  |
| Sat 11/21 TBA | Utah @ TCU | Utah 24, TCU 17 | Utah 66% | Utah -190 / TCU +190 | 25.6 – 19.6 | 13–39 / 7–33 | Utah -12.3 / Utah -5.5 | 49.2 / 44.5 | no edge | no edge | no edge |  |
| Sat 11/21 TBA | Virginia Tech @ Miami | Virginia Tech 21, Miami 38 | Miami 89% | Virginia Tech +845 / Miami -845 | 21.1 – 39.9 | 9–34 / 24–56 | Miami -22.0 / Miami -18.5 | 59.9 / 61.5 | no edge | no edge | no edge |  |
| Sat 11/21 TBA | Pittsburgh @ Louisville | Pittsburgh 17, Louisville 34 | Louisville 86% | Pittsburgh +620 / Louisville -620 | 18.5 – 34.1 | 7–31 / 20–49 | Louisville -15.6 / – | 52.5 / – | no line yet | no line yet (fair: Louisville -620) | no line yet |  |
| Sat 11/21 TBA | Wake Forest @ Georgia Tech | Wake Forest 38, Georgia Tech 17 | Wake Forest 94% | Wake Forest -1500 / Georgia Tech +1500 | 38.4 – 15.7 | 24–55 / 6–28 | Wake Forest -22.6 / – | 54.1 / – | no line yet | no line yet (fair: Wake Forest -1500) | no line yet |  |
| Sat 11/21 TBA | UCLA @ Michigan | UCLA 24, Michigan 17 | UCLA 65% | UCLA -185 / Michigan +185 | 23.5 – 18.0 | 10–37 / 7–31 | UCLA -4.8 / UCLA -5.5 | 41.6 / 41.5 | no edge | no edge | no edge |  |
| Sat 11/21 TBA | Ohio State @ Nebraska | Ohio State 24, Nebraska 21 | Ohio State 65% | Ohio State -180 / Nebraska +180 | 26.6 – 20.9 | 13–41 / 7–34 | Ohio State -7.4 / Ohio State -5.5 | 49.5 / 47.5 | no edge | no edge | no edge |  |
| Sat 11/21 TBA | Indiana @ Washington | Indiana 27, Washington 17 | Indiana 77% | Indiana -335 / Washington +335 | 27.2 – 16.9 | 14–41 / 6–29 | Indiana -10.3 / – | 44.2 / – | no line yet | no line yet (fair: Indiana -335) | no line yet |  |
| Sat 11/21 TBA | North Texas @ Tulane | North Texas 35, Tulane 28 | North Texas 71% | North Texas -240 / Tulane +240 | 35.5 – 27.2 | 20–51 / 13–41 | North Texas -8.2 / – | 62.7 / – | no line yet | no line yet (fair: North Texas -240) | no line yet |  |
| Sat 11/21 TBA | UTSA @ UAB | UTSA 31, UAB 24 | UTSA 66% | UTSA -195 / UAB +195 | 30.1 – 23.6 | 16–45 / 10–38 | UTSA -6.5 / – | 53.7 / – | no line yet | no line yet (fair: UTSA -195) | no line yet |  |
| Sat 11/21 12:00 PM | Vanderbilt @ Florida | Vanderbilt 21, Florida 31 | Florida 73% | Vanderbilt +265 / Florida -265 | 21.1 – 30.0 | 9–35 / 16–45 | Florida -8.9 / – | 51.0 / – | no line yet | no line yet (fair: Florida -265) | no line yet |  |
| Sat 11/21 12:00 PM | Wofford @ Ole Miss | Wofford 3, Ole Miss 59 | Ole Miss 100% | Wofford +9900 / Ole Miss -9900 | 3.0 – 58.3 | 0–7 / 44–73 | Ole Miss -55.3 / – | 61.3 / – | no line yet | no line yet (fair: Ole Miss -9900) | no line yet | FCS opponent |
| Sat 11/21 12:00 PM | Texas A&M @ Oklahoma | Texas A&M 21, Oklahoma 24 | Oklahoma 59% | Texas A&M +140 / Oklahoma -140 | 22.8 – 25.9 | 10–36 / 13–40 | Oklahoma -9.5 / Oklahoma -2.5 | 38.5 / 51.5 | no edge | no edge | Under 51.5 (-110*): EV +9.0%, 57%, stake 2.5u | * price not posted; assumed -110 |
| Sat 11/21 12:00 PM | Colorado @ Cincinnati | Colorado 28, Cincinnati 31 | Cincinnati 62% | Colorado +165 / Cincinnati -165 | 27.4 – 32.0 | 14–41 / 17–47 | Cincinnati -4.6 / – | 59.3 / – | no line yet | no line yet (fair: Cincinnati -165) | no line yet |  |
| Sat 11/21 12:00 PM | Syracuse @ Boston College | Syracuse 31, Boston College 24 | Syracuse 69% | Syracuse -225 / Boston College +225 | 29.5 – 22.2 | 15–45 / 10–35 | Syracuse -7.4 / – | 51.7 / – | no line yet | no line yet (fair: Syracuse -225) | no line yet |  |
| Sat 11/21 12:00 PM | Northwestern @ Minnesota | Northwestern 24, Minnesota 21 | Northwestern 60% | Northwestern -155 / Minnesota +155 | 25.1 – 21.2 | 13–38 / 9–35 | Northwestern -3.9 / – | 46.2 / – | no line yet | no line yet (fair: Northwestern -155) | no line yet |  |
| Sat 11/21 12:00 PM | Wisconsin @ Purdue | Wisconsin 24, Purdue 21 | Wisconsin 64% | Wisconsin -180 / Purdue +180 | 25.4 – 19.9 | 13–40 / 7–33 | Wisconsin -5.5 / – | 47.1 / – | no line yet | no line yet (fair: Wisconsin -180) | no line yet |  |
| Sat 11/21 12:00 PM | East Carolina @ Army | East Carolina 24, Army 27 | Army 57% | East Carolina +135 / Army -135 | 24.8 – 27.4 | 12–38 / 14–42 | Army -2.6 / – | 52.3 / – | no line yet | no line yet (fair: Army -135) | no line yet |  |
| Sat 11/21 12:00 PM | Memphis @ Navy | Memphis 31, Navy 28 | Memphis 55% | Memphis -125 / Navy +125 | 31.1 – 29.4 | 17–45 / 16–44 | Memphis -1.7 / – | 60.5 / – | no line yet | no line yet (fair: Memphis -125) | no line yet |  |
| Sat 11/21 12:30 PM | North Carolina @ Virginia | North Carolina 24, Virginia 27 | Virginia 51% | North Carolina +105 / Virginia -105 | 25.2 – 25.4 | 13–39 / 13–39 | Virginia -0.2 / – | 50.6 / – | no line yet | no line yet (fair: Virginia -105) | no line yet |  |
| Sat 11/21 1:00 PM | Tennessee Tech @ Mississippi State | Tennessee Tech 10, Mississippi State 41 | Mississippi State 99% | Tennessee Tech +8795 / Mississippi State -8795 | 10.6 – 42.2 | 0–20 / 27–59 | Mississippi State -31.7 / – | 52.8 / – | no line yet | no line yet (fair: Mississippi State -8795) | no line yet | FCS opponent |
| Sat 11/21 1:00 PM | Western Kentucky @ Liberty | Western Kentucky 17, Liberty 31 | Liberty 84% | Western Kentucky +525 / Liberty -525 | 19.1 – 33.6 | 7–31 / 20–49 | Liberty -14.5 / – | 52.8 / – | no line yet | no line yet (fair: Liberty -525) | no line yet |  |
| Sat 11/21 2:00 PM | Chattanooga @ Alabama | Chattanooga 0, Alabama 55 | Alabama 100% | Chattanooga +9900 / Alabama -9900 | 3.0 – 56.8 | 0–7 / 42–72 | Alabama -53.8 / – | 59.8 / – | no line yet | no line yet (fair: Alabama -9900) | no line yet | FCS opponent |
| Sat 11/21 2:00 PM | Charlotte @ Tulsa | Charlotte 14, Tulsa 38 | Tulsa 95% | Charlotte +1785 / Tulsa -1785 | 14.3 – 36.8 | 3–26 / 22–52 | Tulsa -22.6 / – | 52.9 / – | no line yet | no line yet (fair: Tulsa -1785) | no line yet |  |
| Sat 11/21 2:00 PM | Missouri State @ Jacksonville State | Missouri State 17, Jacksonville State 31 | Jacksonville State 82% | Missouri State +450 / Jacksonville State -450 | 20.1 – 33.4 | 7–34 / 20–49 | Jacksonville State -13.3 / – | 53.6 / – | no line yet | no line yet (fair: Jacksonville State -450) | no line yet |  |
| Sat 11/21 2:00 PM | Middle Tennessee @ Sam Houston | Middle Tennessee 24, Sam Houston 21 | Middle Tennessee 60% | Middle Tennessee -150 / Sam Houston +150 | 24.0 – 20.1 | 10–38 / 7–34 | Middle Tennessee -3.9 / – | 44.2 / – | no line yet | no line yet (fair: Middle Tennessee -150) | no line yet |  |
| Sat 11/21 2:30 PM | Iowa @ Illinois | Iowa 24, Illinois 17 | Iowa 66% | Iowa -190 / Illinois +190 | 24.9 – 19.3 | 13–38 / 7–32 | Iowa -6.1 / Iowa -5.5 | 49.0 / 43.5 | no edge | no edge | no edge |  |
| Sat 11/21 2:30 PM | South Florida @ Florida Atlantic | South Florida 31, Florida Atlantic 34 | Florida Atlantic 56% | South Florida +130 / Florida Atlantic -130 | 30.0 – 32.6 | 16–45 / 17–48 | Florida Atlantic -2.5 / – | 63.6 / – | no line yet | no line yet (fair: Florida Atlantic -130) | no line yet |  |
| Sat 11/21 2:30 PM | UL Monroe @ App State | UL Monroe 21, App State 31 | App State 78% | UL Monroe +350 / App State -350 | 21.5 – 33.0 | 9–35 / 17–48 | App State -11.5 / – | 54.6 / – | no line yet | no line yet (fair: App State -350) | no line yet |  |
| Sat 11/21 3:00 PM | Coastal Carolina @ Louisiana | Coastal Carolina 24, Louisiana 27 | Louisiana 66% | Coastal Carolina +200 / Louisiana -200 | 22.2 – 28.4 | 10–35 / 14–43 | Louisiana -6.2 / – | 50.5 / – | no line yet | no line yet (fair: Louisiana -200) | no line yet |  |
| Sat 11/21 3:00 PM | Delaware @ New Mexico State | Delaware 31, New Mexico State 24 | Delaware 72% | Delaware -250 / New Mexico State +250 | 31.5 – 23.1 | 17–46 / 10–37 | Delaware -8.4 / – | 54.6 / – | no line yet | no line yet (fair: Delaware -250) | no line yet |  |
| Sat 11/21 3:00 PM | Florida International @ Kennesaw State | Florida International 21, Kennesaw State 28 | Kennesaw State 67% | Florida International +200 / Kennesaw State -200 | 20.4 – 26.8 | 7–34 / 13–41 | Kennesaw State -6.5 / – | 47.2 / – | no line yet | no line yet (fair: Kennesaw State -200) | no line yet |  |
| Sat 11/21 3:30 PM | Samford @ Auburn | Samford 3, Auburn 48 | Auburn 100% | Samford +9900 / Auburn -9900 | 3.0 – 48.6 | 0–7 / 34–65 | Auburn -45.6 / – | 51.6 / – | no line yet | no line yet (fair: Auburn -9900) | no line yet | FCS opponent |
| Sat 11/21 3:30 PM | LSU @ Tennessee | LSU 27, Tennessee 24 | LSU 54% | LSU -120 / Tennessee +120 | 24.9 – 23.5 | 13–38 / 10–37 | LSU -1.2 / LSU -1.5 | 48.0 / 48.5 | no edge | no edge | no edge |  |
| Sat 11/21 3:30 PM | Arkansas @ Texas | Arkansas 10, Texas 34 | Texas 95% | Arkansas +1975 / Texas -1975 | 12.1 – 34.6 | 3–23 / 20–51 | Texas -22.5 / – | 46.7 / – | no line yet | no line yet (fair: Texas -1975) | no line yet |  |
| Sat 11/21 3:30 PM | NC State @ Florida State | NC State 24, Florida State 31 | Florida State 70% | NC State +235 / Florida State -235 | 25.9 – 33.9 | 13–41 / 20–49 | Florida State -8.0 / – | 59.8 / – | no line yet | no line yet (fair: Florida State -235) | no line yet |  |
| Sat 11/21 3:30 PM | Rutgers @ Penn State | Rutgers 17, Penn State 38 | Penn State 92% | Rutgers +1180 / Penn State -1180 | 15.7 – 36.0 | 6–28 / 21–52 | Penn State -20.3 / – | 51.8 / – | no line yet | no line yet (fair: Penn State -1180) | no line yet |  |
| Sat 11/21 3:30 PM | Old Dominion @ UConn | Old Dominion 14, UConn 31 | UConn 89% | Old Dominion +790 / UConn -790 | 15.7 – 32.9 | 5–28 / 17–49 | UConn -17.2 / – | 48.6 / – | no line yet | no line yet (fair: UConn -790) | no line yet |  |
| Sat 11/21 4:00 PM | Northern Illinois @ North Dakota State | Northern Illinois 10, North Dakota State 34 | North Dakota State 95% | Northern Illinois +2030 / North Dakota State -2030 | 12.2 – 35.3 | 3–23 / 20–51 | North Dakota State -23.1 / – | 47.6 / – | no line yet | no line yet (fair: North Dakota State -2030) | no line yet |  |
| Sat 11/21 4:00 PM | Georgia Southern @ Troy | Georgia Southern 28, Troy 21 | Georgia Southern 67% | Georgia Southern -200 / Troy +200 | 27.8 – 21.4 | 14–42 / 9–35 | Georgia Southern -6.5 / – | 49.2 / – | no line yet | no line yet (fair: Georgia Southern -200) | no line yet |  |
| Sat 11/21 4:00 PM | Georgia State @ Marshall | Georgia State 28, Marshall 31 | Marshall 60% | Georgia State +150 / Marshall -150 | 26.6 – 30.6 | 13–41 / 17–45 | Marshall -3.9 / – | 57.2 / – | no line yet | no line yet (fair: Marshall -150) | no line yet |  |
| Sat 11/21 4:00 PM | South Alabama @ Southern Miss | South Alabama 31, Southern Miss 28 | South Alabama 55% | South Alabama -125 / Southern Miss +125 | 31.3 – 28.7 | 17–45 / 14–44 | South Alabama -2.6 / – | 60.0 / – | no line yet | no line yet (fair: South Alabama -125) | no line yet |  |
| Sat 11/21 6:00 PM | Washington State @ Texas State | Washington State 24, Texas State 34 | Texas State 78% | Washington State +360 / Texas State -360 | 23.7 – 35.2 | 10–38 / 20–51 | Texas State -11.5 / – | 58.9 / – | no line yet | no line yet (fair: Texas State -360) | no line yet |  |
| Sat 11/21 6:15 PM | Maryland @ USC | Maryland 21, USC 35 | USC 79% | Maryland +385 / USC -385 | 21.2 – 33.5 | 8–35 / 19–49 | USC -12.4 / – | 54.7 / – | no line yet | no line yet (fair: USC -385) | no line yet |  |
| Sat 11/21 7:00 PM | UNLV @ San José State | UNLV 31, San José State 24 | UNLV 68% | UNLV -215 / San José State +215 | 29.1 – 22.1 | 14–44 / 10–35 | UNLV -7.0 / – | 51.3 / – | no line yet | no line yet (fair: UNLV -215) | no line yet |  |
| Sat 11/21 7:00 PM | Arkansas State @ Louisiana Tech | Arkansas State 21, Louisiana Tech 31 | Louisiana Tech 77% | Arkansas State +335 / Louisiana Tech -335 | 19.5 – 30.5 | 7–33 / 17–45 | Louisiana Tech -11.0 / – | 49.9 / – | no line yet | no line yet (fair: Louisiana Tech -335) | no line yet |  |
| Sat 11/21 7:30 PM | Kentucky @ Missouri | Kentucky 24, Missouri 27 | Missouri 65% | Kentucky +190 / Missouri -190 | 21.5 – 27.6 | 10–35 / 14–42 | Missouri -7.1 / Missouri -6.0 | 49.1 / 49.5 | no edge | no edge | no edge |  |
| Sat 11/21 7:30 PM | Georgia @ South Carolina | Georgia 31, South Carolina 21 | Georgia 76% | Georgia -320 / South Carolina +320 | 30.8 – 20.5 | 17–45 / 7–34 | Georgia -13.1 / Georgia -10.0 | 50.1 / 51.5 | no edge | no edge | no edge |  |
| Sat 11/21 7:30 PM | SMU @ Notre Dame | SMU 20, Notre Dame 37 | Notre Dame 87% | SMU +645 / Notre Dame -645 | 19.9 – 36.6 | 7–34 / 21–52 | Notre Dame -18.7 / Notre Dame -16.5 | 52.9 / 57.5 | no edge | no edge | no edge |  |
| Sat 11/21 7:30 PM | Stanford @ California | Stanford 24, California 27 | California 56% | Stanford +130 / California -130 | 26.2 – 28.7 | 13–41 / 14–43 | California -2.4 / – | 54.9 / – | no line yet | no line yet (fair: California -130) | no line yet |  |
| Sat 11/21 7:30 PM | Colorado State @ Fresno State | Colorado State 27, Fresno State 34 | Fresno State 74% | Colorado State +290 / Fresno State -290 | 25.0 – 35.1 | 12–38 / 20–51 | Fresno State -10.0 / – | 60.1 / – | no line yet | no line yet (fair: Fresno State -290) | no line yet |  |
| Sat 11/21 9:30 PM | San Diego State @ Boise State | San Diego State 17, Boise State 34 | Boise State 86% | San Diego State +630 / Boise State -630 | 19.9 – 36.3 | 7–33 / 21–52 | Boise State -16.4 / – | 56.1 / – | no line yet | no line yet (fair: Boise State -630) | no line yet |  |
| Sat 11/21 10:15 PM | Oklahoma State @ Arizona State | Oklahoma State 31, Arizona State 28 | Oklahoma State 55% | Oklahoma State -125 / Arizona State +125 | 30.0 – 27.9 | 16–45 / 14–42 | Oklahoma State -2.1 / – | 57.9 / – | no line yet | no line yet (fair: Oklahoma State -125) | no line yet |  |
| Sat 11/21 10:30 PM | Utah State @ Oregon State | Utah State 24, Oregon State 31 | Oregon State 73% | Utah State +270 / Oregon State -270 | 21.8 – 31.1 | 10–35 / 17–46 | Oregon State -9.3 / – | 52.9 / – | no line yet | no line yet (fair: Oregon State -270) | no line yet |  |
| Sat 11/21 10:30 PM | Hawai'i @ Nevada | Hawai'i 24, Nevada 21 | Hawai'i 55% | Hawai'i -120 / Nevada +120 | 24.8 – 23.2 | 12–38 / 10–37 | Hawai'i -1.5 / – | 48.0 / – | no line yet | no line yet (fair: Hawai'i -120) | no line yet |  |

## How the 2026 predictions have done

| Predictor | Games | Margin MAE | Total MAE | Team-score MAE | Winners | Brier | 80% range hit |
|---|---|---|---|---|---|---|---|
| Final prediction | 724 | 11.81 | 12.23 | 8.49 | 78.9% | 0.146 | 81.6% |
| Model only (before blending) | 724 | 12.55 | 12.60 | 8.77 | 76.1% | – | – |
| Betting line when predicted | 722 | 11.79 | 12.19 | 8.48 | 78.9% | – | – |

MAE is mean absolute error in points (lower is better). Brier scores the win chances (lower is better, 0.25 is a coin flip). Even the closing betting line misses the final margin of an FBS game by about 12.5 points.

501 of these games were played before the predictor went live. They are backfilled walk-forward (each week predicted from earlier weeks only) but with closing lines, so they flatter the model slightly. Every game since is graded on the prediction logged before kickoff.

### Betting edges

| Market | Edges | Record (W-L-P) | Staked | Units won | ROI | Expected ROI |
|---|---|---|---|---|---|---|
| Spread | 0 | 0-0-0 | 0.0 | +0.00 | – | – |
| Moneyline | 10 | 1-9-0 | 3.2 | -1.24 | -38.3% | +4.6% |
| Total | 7 | 3-4-0 | 9.2 | +0.05 | +0.5% | +6.8% |

7 of these edges were priced at an assumed -110 (price not posted).

Every edge logged before kickoff at the stake and price logged with it (backfilled games, and edges logged before edges were priced from the final prediction, are not included). Units are 1% of the bankroll; ROI is units won per unit staked, pushes returning the stake, and expected ROI is what the edges' EVs promised.

### Week 11 results

| Game | Predicted | Final | Win chance for winner | Inside 80% ranges |
|---|---|---|---|---|
| Western Michigan @ Akron | 34–17 | 42–14 | 85% | yes |
| Kent State @ Bowling Green | 17–24 | 28–33 | 63% | yes |
| Ohio @ Miami (OH) | 24–21 | 17–34 | 47% | yes |
| Buffalo @ Ball State | 27–24 | 28–7 | 56% | no |
| Sacramento State @ Central Michigan | 14–31 | 7–28 | 90% | yes |
| Massachusetts @ Toledo | 17–31 | 0–24 | 85% | no |
| Memphis @ South Florida | 27–24 | 52–41 | 61% | no |
| Louisiana @ UL Monroe | 31–21 | 42–21 | 75% | yes |
| Florida State @ Pittsburgh | 24–27 | 16–10 | 40% | no |
| Illinois @ UCLA | 17–27 | 14–22 | 77% | yes |
| Houston @ Colorado | 31–24 | 32–42 | 30% | no |
| Cincinnati @ Iowa State | 28–31 | 13–41 | 57% | no |
| Duke @ Miami | 20–34 | 25–36 | 82% | yes |
| Syracuse @ NC State | 31–28 | 34–31 | 57% | yes |
| Wake Forest @ SMU | 28–31 | 49–7 | 48% | no |
| Wisconsin @ Maryland | 24–17 | 21–24 | 28% | yes |
| Northwestern @ Ohio State | 17–31 | 19–28 | 84% | yes |
| James Madison @ UConn | 31–24 | 22–46 | 39% | no |
| Georgia Tech @ Clemson | 17–31 | 20–6 | 14% | no |
| Nebraska @ Rutgers | 34–17 | 31–0 | 85% | no |
| Alabama @ Vanderbilt | 31–17 | 21–6 | 84% | yes |
| East Carolina @ Charlotte | 27–17 | 17–16 | 79% | yes |
| UAB @ Temple | 21–24 | 36–10 | 44% | no |
| Arkansas State @ Coastal Carolina | 24–27 | 21–28 | 55% | yes |
| Kansas State @ TCU | 17–31 | 10–20 | 81% | yes |
| Kennesaw State @ Sam Houston | 24–17 | 26–7 | 73% | yes |
| Tennessee @ Texas A&M | 24–21 | 22–7 | 56% | no |
| New Mexico State @ Missouri State | 24–27 | 21–27 | 55% | yes |
| Florida International @ Delaware | 24–27 | 16–24 | 62% | yes |
| Missouri @ Georgia | 14–31 | 21–48 | 87% | yes |
| Boston College @ Notre Dame | 10–38 | 7–41 | 98% | yes |
| California @ Virginia | 17–31 | 7–36 | 78% | yes |
| USC @ Indiana | 21–31 | 13–27 | 74% | yes |
| Michigan @ Oregon | 17–24 | 7–31 | 77% | yes |
| Nevada @ Northern Illinois | 28–21 | 28–7 | 68% | no |
| Georgia Southern @ Georgia State | 31–24 | 34–17 | 62% | yes |
| Jacksonville State @ Western Kentucky | 31–24 | 24–34 | 31% | yes |
| Middle Tennessee @ Liberty | 17–38 | 23–28 | 93% | yes |
| Kansas @ West Virginia | 31–34 | 37–14 | 46% | no |

## FBS power ratings

Points per game better than an average FBS team on a neutral field, from opponent-adjusted EPA (garbage time removed) with this season's games weighted against a preseason prior, plus the weight the margin model puts on Elo (a rating built from game results alone). Defense is positive when it holds opponents below average.

| # | Team | Conference | Net | Offense | Defense | Special teams | Results (Elo) | Elo rating |
|---|---|---|---|---|---|---|---|---|
| 1 | Georgia | SEC | +27.5 | +9.3 | +12.1 | +0.9 | +5.3 | 1944 |
| 2 | Notre Dame | FBS Independents | +24.6 | +9.2 | +9.7 | +1.1 | +4.7 | 1892 |
| 3 | LSU | SEC | +23.8 | +9.7 | +11.6 | +0.0 | +2.4 | 1703 |
| 4 | Miami | ACC | +23.4 | +15.2 | +3.3 | +0.3 | +4.5 | 1881 |
| 5 | Ohio State | Big Ten | +23.3 | +10.1 | +9.3 | +0.2 | +3.7 | 1817 |
| 6 | Alabama | SEC | +22.1 | +8.4 | +9.4 | +0.3 | +4.0 | 1841 |
| 7 | Indiana | Big Ten | +21.5 | +5.6 | +10.4 | +0.1 | +5.4 | 1953 |
| 8 | Oregon | Big Ten | +20.6 | +6.7 | +9.8 | +0.2 | +3.8 | 1823 |
| 9 | Utah | Big 12 | +20.5 | +10.3 | +6.1 | -0.1 | +4.3 | 1862 |
| 10 | Wake Forest | ACC | +20.4 | +7.6 | +9.0 | +0.6 | +3.2 | 1776 |
| 11 | Texas | SEC | +19.8 | +2.5 | +12.4 | +0.8 | +4.1 | 1848 |
| 12 | Tennessee | SEC | +18.9 | +4.1 | +10.1 | +1.4 | +3.3 | 1784 |
| 13 | UCLA | Big Ten | +17.8 | +4.8 | +9.6 | +0.7 | +2.7 | 1729 |
| 14 | Texas Tech | Big 12 | +17.2 | +2.9 | +9.9 | +1.3 | +3.1 | 1767 |
| 15 | Ole Miss | SEC | +16.6 | +9.5 | +3.3 | +0.7 | +3.1 | 1764 |
| 16 | Louisville | ACC | +16.6 | +10.0 | +4.0 | +0.2 | +2.3 | 1699 |
| 17 | Oklahoma | SEC | +16.5 | +1.1 | +12.9 | +0.6 | +1.8 | 1659 |
| 18 | Iowa | Big Ten | +14.3 | +1.5 | +8.5 | +1.0 | +3.3 | 1783 |
| 19 | USC | Big Ten | +13.7 | +10.5 | +0.3 | +0.2 | +2.6 | 1724 |
| 20 | Nebraska | Big Ten | +13.4 | +4.0 | +8.1 | +0.4 | +1.0 | 1589 |
| 21 | BYU | Big 12 | +13.3 | +5.3 | +4.5 | +0.7 | +2.8 | 1739 |
| 22 | Missouri | SEC | +12.8 | +3.7 | +7.0 | +0.3 | +1.9 | 1667 |
| 23 | South Carolina | SEC | +12.4 | +6.0 | +3.7 | +0.6 | +2.1 | 1683 |
| 24 | Arizona | Big 12 | +11.9 | +6.0 | +3.3 | +0.1 | +2.5 | 1713 |
| 25 | Penn State | Big Ten | +11.9 | +3.8 | +6.4 | +0.1 | +1.6 | 1640 |
| 26 | Auburn | SEC | +11.8 | +5.3 | +5.4 | +0.6 | +0.5 | 1550 |
| 27 | Michigan | Big Ten | +11.5 | +1.9 | +8.7 | -0.0 | +0.9 | 1586 |
| 28 | Florida | SEC | +10.7 | +5.7 | +3.8 | +0.8 | +0.3 | 1534 |
| 29 | SMU | ACC | +10.6 | +6.7 | +2.1 | +0.2 | +1.6 | 1637 |
| 30 | Oklahoma State | Big 12 | +9.9 | +9.2 | -0.3 | +0.5 | +0.6 | 1556 |
| 31 | Texas A&M | SEC | +9.7 | +0.8 | +8.0 | +0.2 | +0.6 | 1554 |
| 32 | Baylor | Big 12 | +9.6 | +0.9 | +6.3 | +1.0 | +1.5 | 1628 |
| 33 | Northwestern | Big Ten | +9.5 | +5.8 | +2.1 | +0.6 | +1.0 | 1591 |
| 34 | Houston | Big 12 | +9.4 | +9.0 | -1.2 | +0.3 | +1.4 | 1621 |
| 35 | Washington | Big Ten | +8.9 | +2.4 | +4.7 | +0.1 | +1.6 | 1642 |
| 36 | Duke | ACC | +8.7 | +4.6 | +1.1 | +0.8 | +2.3 | 1700 |
| 37 | Kansas | Big 12 | +8.7 | +5.2 | +3.8 | -0.1 | -0.2 | 1495 |
| 38 | Kentucky | SEC | +8.3 | +2.8 | +3.8 | +0.1 | +1.6 | 1642 |
| 39 | Mississippi State | SEC | +8.2 | +4.6 | +3.9 | -0.1 | -0.2 | 1493 |
| 40 | Iowa State | Big 12 | +7.6 | +4.7 | +1.1 | +1.0 | +0.9 | 1581 |
| 41 | Wisconsin | Big Ten | +7.1 | -1.6 | +7.1 | +0.8 | +0.8 | 1575 |
| 42 | Illinois | Big Ten | +6.5 | +6.2 | -1.4 | +0.4 | +1.3 | 1617 |
| 43 | Boise State | Pac-12 | +6.5 | +6.3 | -2.2 | -0.3 | +2.7 | 1730 |
| 44 | Kansas State | Big 12 | +6.4 | +4.7 | +2.4 | +0.3 | -0.9 | 1436 |
| 45 | Florida State | ACC | +6.3 | +6.6 | -0.1 | -0.6 | +0.4 | 1540 |
| 46 | Arizona State | Big 12 | +6.0 | +1.2 | +4.2 | -0.1 | +0.7 | 1565 |
| 47 | TCU | Big 12 | +5.7 | -1.9 | +6.4 | +0.1 | +1.1 | 1599 |
| 48 | Cincinnati | Big 12 | +5.1 | +9.0 | -4.2 | +0.3 | -0.0 | 1507 |
| 49 | Vanderbilt | SEC | +4.4 | +2.0 | +1.6 | +0.5 | +0.3 | 1531 |
| 50 | Virginia Tech | ACC | +4.1 | +4.1 | -0.5 | +0.1 | +0.4 | 1541 |
| 51 | North Carolina | ACC | +3.9 | +3.5 | -0.9 | +0.8 | +0.6 | 1554 |
| 52 | Colorado | Big 12 | +3.7 | +1.3 | +4.0 | -0.6 | -0.9 | 1432 |
| 53 | North Texas | American Athletic | +3.7 | +10.5 | -7.6 | -0.9 | +1.7 | 1651 |
| 54 | UCF | Big 12 | +3.6 | +1.6 | +2.2 | +0.2 | -0.5 | 1470 |
| 55 | Maryland | Big Ten | +3.4 | +0.0 | +4.1 | +0.5 | -1.2 | 1408 |
| 56 | Clemson | ACC | +3.1 | -6.5 | +8.2 | +1.0 | +0.5 | 1547 |
| 57 | Pittsburgh | ACC | +3.0 | -2.6 | +4.9 | +0.5 | +0.2 | 1525 |
| 58 | Memphis | American Athletic | +3.0 | +5.0 | -3.3 | -0.5 | +1.7 | 1652 |
| 59 | Minnesota | Big Ten | +3.0 | -3.5 | +5.4 | +0.9 | +0.2 | 1529 |
| 60 | Syracuse | ACC | +2.8 | +2.0 | +2.6 | -0.7 | -1.0 | 1424 |
| 61 | Virginia | ACC | +2.6 | -1.3 | +3.9 | -0.1 | +0.1 | 1519 |
| 62 | Texas State | Pac-12 | +1.6 | +6.2 | -4.5 | -1.1 | +1.1 | 1602 |
| 63 | Arkansas | SEC | +1.1 | +1.8 | +0.6 | -0.7 | -0.7 | 1455 |
| 64 | James Madison | Sun Belt | +1.0 | -0.7 | +0.1 | +0.2 | +1.4 | 1625 |
| 65 | UTSA | American Athletic | +1.0 | +3.6 | -3.6 | -0.0 | +1.1 | 1596 |
| 66 | New Mexico | Mountain West | +0.7 | -3.5 | +2.8 | -0.2 | +1.5 | 1636 |
| 67 | NC State | ACC | +0.5 | +4.9 | -3.5 | -0.4 | -0.5 | 1467 |
| 68 | Liberty | Conference USA | +0.4 | +1.3 | -1.8 | +0.1 | +0.8 | 1574 |
| 69 | Toledo | Mid-American | +0.3 | -2.4 | +2.4 | -0.4 | +0.7 | 1567 |
| 70 | Tulsa | American Athletic | -0.3 | +0.5 | +0.3 | -0.6 | -0.5 | 1466 |
| 71 | Oregon State | Pac-12 | -0.3 | +3.4 | -2.7 | -0.0 | -1.0 | 1428 |
| 72 | Purdue | Big Ten | -0.6 | +3.2 | -3.1 | +0.7 | -1.5 | 1386 |
| 73 | West Virginia | Big 12 | -0.8 | +5.1 | -5.2 | +0.3 | -1.0 | 1429 |
| 74 | UConn | FBS Independents | -0.8 | +3.0 | -3.9 | +0.1 | +0.0 | 1512 |
| 75 | Navy | American Athletic | -1.0 | +3.7 | -3.7 | -0.6 | -0.3 | 1484 |
| 76 | Michigan State | Big Ten | -1.0 | -2.9 | +1.9 | +0.6 | -0.6 | 1459 |
| 77 | North Dakota State | Mountain West | -1.3 | -4.6 | +3.4 | +1.1 | -1.1 | 1419 |
| 78 | South Florida | American Athletic | -2.5 | -1.3 | -1.6 | +0.1 | +0.3 | 1531 |
| 79 | Louisiana Tech | Sun Belt | -2.5 | -3.3 | +0.8 | -0.7 | +0.8 | 1575 |
| 80 | Florida Atlantic | American Athletic | -2.8 | +4.7 | -8.1 | +0.7 | -0.0 | 1506 |
| 81 | East Carolina | American Athletic | -3.5 | -6.8 | +3.8 | -0.7 | +0.2 | 1524 |
| 82 | Georgia Tech | ACC | -3.5 | +0.6 | -3.0 | -0.4 | -0.6 | 1455 |
| 83 | Fresno State | Pac-12 | -3.6 | -2.7 | -0.9 | -0.3 | +0.3 | 1530 |
| 84 | Army | American Athletic | -3.8 | +4.4 | -8.3 | -0.1 | +0.2 | 1525 |
| 85 | Georgia Southern | Sun Belt | -4.1 | -1.2 | -3.4 | -0.5 | +0.9 | 1586 |
| 86 | Air Force | Mountain West | -4.2 | +2.3 | -6.5 | -0.2 | +0.1 | 1517 |
| 87 | Western Michigan | Mid-American | -5.4 | -3.4 | -3.4 | +0.6 | +0.8 | 1574 |
| 88 | Utah State | Pac-12 | -6.2 | -6.7 | +2.3 | -1.1 | -0.7 | 1455 |
| 89 | Jacksonville State | Conference USA | -6.2 | -1.5 | -4.3 | +0.2 | -0.7 | 1451 |
| 90 | Ohio | Mid-American | -6.5 | -3.8 | -3.0 | +0.1 | +0.2 | 1525 |
| 91 | UNLV | Mountain West | -6.6 | -2.7 | -3.9 | +0.2 | -0.1 | 1497 |
| 92 | Rutgers | Big Ten | -6.7 | +1.5 | -6.7 | +0.6 | -2.0 | 1342 |
| 93 | Delaware | Conference USA | -6.8 | +0.7 | -6.4 | +0.1 | -1.1 | 1414 |
| 94 | Miami (OH) | Mid-American | -6.9 | -4.7 | -2.7 | +0.9 | -0.3 | 1482 |
| 95 | Boston College | ACC | -7.0 | -4.0 | -1.4 | -0.6 | -1.0 | 1427 |
| 96 | California | ACC | -7.5 | -2.9 | -1.9 | -0.7 | -2.0 | 1344 |
| 97 | UAB | American Athletic | -7.8 | -6.5 | -0.6 | -0.1 | -0.7 | 1455 |
| 98 | Tulane | American Athletic | -7.9 | -4.5 | -2.9 | +0.2 | -0.7 | 1454 |
| 99 | San Diego State | Pac-12 | -8.1 | -4.4 | -2.6 | +0.2 | -1.2 | 1406 |
| 100 | Stanford | ACC | -8.2 | -2.5 | -4.9 | -0.1 | -0.7 | 1448 |
| 101 | Louisiana | Sun Belt | -8.2 | -3.5 | -4.7 | +0.0 | -0.0 | 1505 |
| 102 | Washington State | Pac-12 | -8.3 | -5.8 | -0.2 | -0.4 | -1.9 | 1349 |
| 103 | Wyoming | Mountain West | -9.2 | -5.3 | -3.1 | -0.2 | -0.6 | 1460 |
| 104 | Marshall | Sun Belt | -9.8 | -4.9 | -4.2 | -0.1 | -0.6 | 1456 |
| 105 | App State | Sun Belt | -10.0 | -3.6 | -4.1 | -0.5 | -1.8 | 1361 |
| 106 | Hawai'i | Mountain West | -10.4 | -3.6 | -6.2 | +1.0 | -1.6 | 1374 |
| 107 | Kennesaw State | Conference USA | -11.1 | -6.2 | -2.9 | -0.5 | -1.5 | 1386 |
| 108 | Western Kentucky | Conference USA | -11.2 | -5.4 | -3.5 | -0.5 | -1.8 | 1360 |
| 109 | Georgia State | Sun Belt | -11.2 | -1.6 | -7.8 | -0.3 | -1.6 | 1377 |
| 110 | Central Michigan | Mid-American | -11.5 | -5.9 | -4.6 | +0.0 | -1.0 | 1429 |
| 111 | Colorado State | Pac-12 | -11.5 | +4.8 | -13.3 | -0.2 | -2.8 | 1278 |
| 112 | Arkansas State | Sun Belt | -12.0 | -3.7 | -6.9 | +0.1 | -1.6 | 1374 |
| 113 | Troy | Sun Belt | -12.1 | -8.5 | -0.5 | -1.4 | -1.7 | 1366 |
| 114 | South Alabama | Sun Belt | -12.1 | -0.0 | -10.9 | +0.3 | -1.5 | 1388 |
| 115 | Temple | American Athletic | -12.3 | -0.9 | -7.7 | -0.5 | -3.2 | 1244 |
| 116 | Coastal Carolina | Sun Belt | -12.4 | -7.3 | -3.7 | +0.3 | -1.7 | 1368 |
| 117 | Old Dominion | Sun Belt | -12.5 | -13.4 | +3.8 | -1.7 | -1.2 | 1407 |
| 118 | Rice | American Athletic | -13.0 | -3.3 | -5.5 | -0.9 | -3.3 | 1240 |
| 119 | Nevada | Mountain West | -13.8 | -10.9 | -1.4 | +0.5 | -2.1 | 1337 |
| 120 | Florida International | Conference USA | -14.3 | -9.4 | -1.3 | -1.5 | -2.0 | 1341 |
| 121 | Buffalo | Mid-American | -15.0 | -10.8 | -4.4 | +0.3 | -0.2 | 1491 |
| 122 | Southern Miss | Sun Belt | -15.6 | -8.1 | -4.0 | -1.2 | -2.3 | 1318 |
| 123 | New Mexico State | Conference USA | -15.6 | -7.7 | -2.7 | -1.9 | -3.3 | 1235 |
| 124 | Missouri State | Conference USA | -15.7 | -4.5 | -7.3 | -1.3 | -2.6 | 1292 |
| 125 | San José State | Mountain West | -15.8 | -9.9 | -3.6 | +0.0 | -2.3 | 1318 |
| 126 | Middle Tennessee | Conference USA | -15.9 | -5.3 | -8.2 | +0.3 | -2.7 | 1290 |
| 127 | Bowling Green | Mid-American | -17.8 | -11.1 | -4.1 | +0.1 | -2.7 | 1290 |
| 128 | UL Monroe | Sun Belt | -18.3 | -5.7 | -7.1 | -1.5 | -3.9 | 1184 |
| 129 | Massachusetts | Mid-American | -18.4 | -10.2 | -4.5 | -0.2 | -3.5 | 1221 |
| 130 | Ball State | Mid-American | -19.1 | -6.9 | -8.1 | -0.6 | -3.5 | 1218 |
| 131 | Eastern Michigan | Mid-American | -19.3 | -7.8 | -8.1 | -0.6 | -2.7 | 1287 |
| 132 | Northern Illinois | Mountain West | -19.7 | -4.6 | -8.8 | -1.3 | -4.9 | 1101 |
| 133 | Sacramento State | Mid-American | -20.3 | -11.3 | -4.6 | +0.2 | -4.5 | 1136 |
| 134 | Sam Houston | Conference USA | -20.5 | -13.5 | -0.9 | -1.3 | -4.8 | 1114 |
| 135 | Charlotte | American Athletic | -20.6 | -9.4 | -6.7 | -0.5 | -3.9 | 1187 |
| 136 | Kent State | Mid-American | -21.5 | -10.5 | -6.6 | -0.9 | -3.5 | 1221 |
| 137 | Akron | Mid-American | -23.9 | -10.3 | -9.1 | -0.6 | -3.9 | 1185 |
| 138 | UTEP | Mountain West | -24.5 | -11.4 | -6.9 | -1.2 | -4.9 | 1103 |

## Current model fit

- Fitted on 4341 games from seasons 2022–2026.
- Home field on top of the ratings: 3.3 points (1.7 in conference games).
- Extra FBS edge over FCS opponents beyond their ratings: 14.1 points.
- Elo weight: 0.19 points of margin per point of Elo spread.
- Weight on the betting line: 92% for the margin, 82% for the total.
