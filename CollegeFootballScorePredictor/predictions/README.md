# College football score predictions

Updated Sat Nov 14, 2026 05:45 PM ET. Refreshed automatically every day of the season and several times on Saturdays; each game's prediction is locked at kickoff and graded once the final score is in. Scores are the most likely real scoreline near the expected points; ranges cover 80% of simulated outcomes for each team. College scores scatter widely, so read the ranges, not just the headline score.

Expected points blend the model with the betting line using the weight that has predicted best in recent seasons (see Current model fit). The spread and total columns show the model's own numbers next to the line, so you can see where it disagrees. Games without a line yet use the model alone.

The fair moneyline is the American odds that match the win chance exactly, with no bookmaker margin: -200 means risk $200 to win $100, +200 means risk $100 to win $200. A sportsbook's price will be a little worse on both sides because of its cut, so a book only offers value on a team when its price beats the fair line.

The edge columns judge each bet by its expected value per $1 staked at the posted price, using the final prediction: the model blended with the line, run through the score simulator, pushes included, and anchored to the market's own chances so that only what the blend moves off the line counts. The model's own spread and total (shown alongside) sit several points from the line in most games, but the blend keeps only the share of that disagreement the model has earned in past seasons, so edges are rare. The side with the higher value is shown when it reaches 3% (+3 cents per $1), as the team or side, the price, the expected value, its chance of winning the bet and its stake, a 25% share of the Kelly stake in units of 1% of the bankroll with at most 3 units on one game; anything short is no edge. Where a book posts no price for a spread or total it is assumed to be -110 and marked -110*; moneylines are never assumed. In the walk-forward backtest against closing lines, edges returned spread -100.0% on 1 bets (posted prices, 2016–2019); spread -3.9% on 156 bets (assumed -110 prices, 2016–2025); moneyline +13.7% on 575 bets (posted prices, 2016–2025); total +2.6% on 367 bets (posted prices, 2016–2019); total -5.7% on 172 bets (assumed -110 prices, 2016–2025). None of these is clearly above zero, so treat these edges as an experiment, not a betting system. The live record is tracked below, graded at the price logged with the last prediction before kickoff.

## 2026 Week 11

| Kickoff (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected points | 80% range | Spread: model / line | Total: model / line | Spread edge | Moneyline edge | Total edge | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sat 11/14 6:00 PM | Oregon State @ Boise State | Oregon State 24, Boise State 41 | Boise State 85% | Oregon State +565 / Boise State -565 | 24.5 – 40.4 | 10–38 / 24–56 | Boise State -8.8 / Boise State -16.5 | 61.4 / 65.8 | no edge | no edge | no edge |  |
| Sat 11/14 6:00 PM | App State @ Marshall | App State 24, Marshall 27 | Marshall 53% | App State +110 / Marshall -110 | 26.5 – 27.9 | 13–41 / 14–42 | Marshall -3.0 / Marshall -1.2 | 55.1 / 54.2 | no edge | no edge | no edge |  |
| Sat 11/14 6:15 PM | Florida @ Kentucky | Florida 24, Kentucky 27 | Kentucky 58% | Florida +135 / Kentucky -135 | 24.9 – 27.6 | 13–38 / 14–42 | Florida -0.8 / Kentucky -3.0 | 51.3 / 52.8 | no edge | no edge | no edge |  |
| Sat 11/14 7:00 PM | Baylor @ BYU | Baylor 21, BYU 28 | BYU 71% | Baylor +250 / BYU -250 | 20.8 – 29.1 | 8–34 / 14–44 | BYU -5.9 / BYU -8.5 | 52.1 / 49.5 | no edge | no edge | no edge |  |
| Sat 11/14 7:00 PM | Louisville @ North Carolina | Louisville 31, North Carolina 28 | Louisville 61% | Louisville -155 / North Carolina +155 | 30.7 – 26.7 | 17–45 / 13–41 | Louisville -9.7 / Louisville -3.5 | 57.1 / 57.5 | no edge | no edge | no edge |  |
| Sat 11/14 7:00 PM | Minnesota @ Penn State | Minnesota 14, Penn State 28 | Penn State 81% | Minnesota +425 / Penn State -425 | 15.0 – 27.3 | 3–27 / 14–42 | Penn State -10.6 / Penn State -12.5 | 41.6 / 42.5 | no edge | no edge | no edge |  |
| Sat 11/14 7:00 PM | San José State @ Air Force | San José State 17, Air Force 31 | Air Force 83% | San José State +495 / Air Force -495 | 18.5 – 32.5 | 7–31 / 17–48 | Air Force -13.7 / Air Force -14.0 | 53.1 / 50.5 | no edge | no edge | no edge |  |
| Sat 11/14 7:00 PM | Troy @ South Alabama | Troy 24, South Alabama 27 | South Alabama 59% | Troy +145 / South Alabama -145 | 26.1 – 29.2 | 13–40 / 15–45 | South Alabama -3.8 / South Alabama -3.0 | 54.4 / 55.5 | no edge | no edge | no edge |  |
| Sat 11/14 7:15 PM | Florida Atlantic @ Tulsa | Florida Atlantic 31, Tulsa 38 | Tulsa 66% | Florida Atlantic +195 / Tulsa -195 | 32.7 – 39.2 | 17–48 / 24–55 | Tulsa -3.6 / Tulsa -6.8 | 66.1 / 73.2 | no edge | no edge | no edge |  |
| Sat 11/14 7:30 PM | Texas @ LSU | Texas 21, LSU 24 | LSU 62% | Texas +165 / LSU -165 | 21.3 – 25.9 | 10–35 / 13–41 | LSU -5.6 / LSU -4.5 | 46.0 / 47.5 | no edge | no edge | no edge |  |
| Sat 11/14 7:30 PM | Stanford @ Virginia Tech | Stanford 21, Virginia Tech 38 | Virginia Tech 88% | Stanford +720 / Virginia Tech -720 | 20.1 – 37.4 | 7–34 / 23–53 | Virginia Tech -15.2 / Virginia Tech -17.5 | 56.3 / 57.8 | no edge | no edge | no edge |  |
| Sat 11/14 7:30 PM | Purdue @ Iowa | Purdue 14, Iowa 31 | Iowa 90% | Purdue +905 / Iowa -905 | 14.7 – 33.2 | 3–27 / 17–48 | Iowa -17.5 / Iowa -18.5 | 48.6 / 47.8 | no edge | no edge | no edge |  |
| Sat 11/14 7:30 PM | UNLV @ New Mexico | UNLV 14, New Mexico 31 | New Mexico 88% | UNLV +725 / New Mexico -725 | 14.9 – 31.7 | 3–27 / 17–48 | New Mexico -9.0 / New Mexico -17.5 | 47.3 / 46.5 | no edge | UNLV (+541): EV +5.7%, 16%, stake 0.3u | no edge |  |
| Sat 11/14 7:45 PM | South Carolina @ Arkansas | South Carolina 31, Arkansas 24 | South Carolina 70% | South Carolina -230 / Arkansas +230 | 29.9 – 22.4 | 16–45 / 10–36 | South Carolina -10.2 / South Carolina -7.2 | 55.0 / 51.8 | no edge | no edge | no edge |  |
| Sat 11/14 9:00 PM | North Texas @ UTSA | North Texas 38, UTSA 35 | North Texas 55% | North Texas -125 / UTSA +125 | 38.3 – 36.2 | 23–53 / 21–51 | UTSA -0.4 / North Texas -2.2 | 69.1 / 75.8 | no edge | no edge | no edge |  |
| Sat 11/14 9:30 PM | Texas Tech @ Oklahoma State | Texas Tech 35, Oklahoma State 38 | Oklahoma State 58% | Texas Tech +140 / Oklahoma State -140 | 34.0 – 36.7 | 20–49 / 22–52 | Texas Tech -5.9 / Oklahoma State -3.5 | 57.2 / 73.8 | no edge | no edge | Under 73.75 (-110*): EV +8.7%, 57%, stake 2.4u | * price not posted; assumed -110 |
| Sat 11/14 9:30 PM | Utah State @ San Diego State | Utah State 24, San Diego State 21 | Utah State 58% | Utah State -135 / San Diego State +135 | 23.5 – 21.0 | 10–37 / 9–34 | San Diego State -1.9 / Utah State -3.0 | 47.8 / 43.8 | no edge | no edge | no edge |  |
| Sat 11/14 10:00 PM | Wyoming @ UTEP | Wyoming 24, UTEP 17 | Wyoming 71% | Wyoming -245 / UTEP +245 | 24.5 – 17.0 | 10–38 / 6–29 | Wyoming -13.9 / Wyoming -7.0 | 46.0 / 40.5 | no edge | no edge | no edge |  |
| Sat 11/14 10:30 PM | Utah @ Arizona | Utah 31, Arizona 28 | Utah 55% | Utah -125 / Arizona +125 | 28.7 – 26.9 | 14–44 / 13–41 | Utah -5.7 / Utah -1.5 | 55.9 / 55.5 | no edge | no edge | no edge |  |
| Sat 11/14 10:30 PM | Colorado State @ Washington State | Colorado State 28, Washington State 35 | Washington State 70% | Colorado State +235 / Washington State -235 | 27.7 – 36.0 | 14–42 / 21–52 | Washington State -5.3 / Washington State -8.5 | 59.0 / 64.8 | no edge | no edge | no edge |  |
| Sat 11/14 11:00 PM | North Dakota State @ Hawai'i | North Dakota State 24, Hawai'i 17 | North Dakota State 69% | North Dakota State -225 / Hawai'i +225 | 23.9 – 16.9 | 10–38 / 6–29 | North Dakota State -6.9 / North Dakota State -7.0 | 47.4 / 39.2 | no edge | no edge | Over 39.25 (-110*): EV +3.1%, 54%, stake 0.9u | * price not posted; assumed -110 |
| Sun 11/15 1:00 PM | Ole Miss @ Oklahoma | Ole Miss 24, Oklahoma 27 | Oklahoma 58% | Ole Miss +135 / Oklahoma -135 | 23.1 – 25.8 | 10–37 / 13–40 | Oklahoma -2.1 / Oklahoma -2.8 | 50.0 / 48.8 | no edge | no edge | no edge |  |

## 2026 Week 12

| Kickoff (ET) | Game | Predicted score | Win chance | Fair moneyline | Expected points | 80% range | Spread: model / line | Total: model / line | Spread edge | Moneyline edge | Total edge | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tue 11/17 6:00 PM | Eastern Michigan @ Western Michigan | Eastern Michigan 17, Western Michigan 34 | Western Michigan 89% | Eastern Michigan +800 / Western Michigan -800 | 17.0 – 34.5 | 6–29 / 20–49 | Western Michigan -17.5 / – | 51.5 / – | no line yet | no line yet (fair: Western Michigan -800) | no line yet |  |
| Tue 11/17 7:00 PM | Ball State @ Ohio | Ball State 17, Ohio 34 | Ohio 86% | Ball State +635 / Ohio -635 | 17.5 – 33.0 | 7–30 / 17–48 | Ohio -15.5 / – | 50.5 / – | no line yet | no line yet (fair: Ohio -635) | no line yet |  |
| Tue 11/17 7:00 PM | Miami (OH) @ Kent State | Miami (OH) 31, Kent State 17 | Miami (OH) 83% | Miami (OH) -495 / Kent State +495 | 30.4 – 16.4 | 16–45 / 6–28 | Miami (OH) -13.9 / – | 46.8 / – | no line yet | no line yet (fair: Miami (OH) -495) | no line yet |  |
| Wed 11/18 7:00 PM | Akron @ Massachusetts | Akron 17, Massachusetts 24 | Massachusetts 71% | Akron +250 / Massachusetts -250 | 19.4 – 27.7 | 7–32 / 14–42 | Massachusetts -8.3 / – | 47.1 / – | no line yet | no line yet (fair: Massachusetts -250) | no line yet |  |
| Wed 11/18 7:30 PM | Central Michigan @ Buffalo | Central Michigan 27, Buffalo 24 | Central Michigan 52% | Central Michigan -110 / Buffalo +110 | 25.4 – 24.5 | 13–39 / 10–38 | Central Michigan -0.9 / – | 49.9 / – | no line yet | no line yet (fair: Central Michigan -110) | no line yet |  |
| Thu 11/19 7:30 PM | Rice @ Temple | Rice 24, Temple 31 | Temple 65% | Rice +185 / Temple -185 | 23.9 – 29.9 | 10–38 / 16–45 | Temple -6.0 / – | 53.8 / – | no line yet | no line yet (fair: Temple -185) | no line yet |  |
| Fri 11/20 6:00 PM | Iowa State @ UCF | Iowa State 27, UCF 24 | Iowa State 58% | Iowa State -135 / UCF +135 | 27.6 – 25.0 | 14–42 / 12–38 | Iowa State -2.6 / – | 52.5 / – | no line yet | no line yet (fair: Iowa State -135) | no line yet |  |
| Fri 11/20 7:30 PM | Clemson @ Duke | Clemson 21, Duke 24 | Duke 66% | Clemson +200 / Duke -200 | 20.6 – 26.6 | 7–34 / 13–41 | Duke -6.1 / – | 47.2 / – | no line yet | no line yet (fair: Duke -200) | no line yet |  |
| Fri 11/20 7:30 PM | Bowling Green @ Toledo | Bowling Green 10, Toledo 31 | Toledo 93% | Bowling Green +1280 / Toledo -1280 | 12.2 – 32.3 | 3–24 / 17–48 | Toledo -20.0 / – | 44.5 / – | no line yet | no line yet (fair: Toledo -1280) | no line yet |  |
| Fri 11/20 8:00 PM | Oregon @ Michigan State | Oregon 31, Michigan State 14 | Oregon 90% | Oregon -865 / Michigan State +865 | 32.5 – 14.4 | 17–48 / 3–26 | Oregon -18.2 / – | 46.9 / – | no line yet | no line yet (fair: Oregon -865) | no line yet |  |
| Fri 11/20 8:00 PM | UTEP @ Air Force | UTEP 14, Air Force 38 | Air Force 95% | UTEP +2025 / Air Force -2025 | 13.8 – 37.4 | 3–24 / 22–54 | Air Force -23.6 / – | 51.3 / – | no line yet | no line yet (fair: Air Force -2025) | no line yet |  |
| Fri 11/20 9:00 PM | New Mexico @ Wyoming | New Mexico 24, Wyoming 17 | New Mexico 70% | New Mexico -235 / Wyoming +235 | 25.6 – 18.2 | 13–40 / 7–31 | New Mexico -7.4 / – | 43.9 / – | no line yet | no line yet (fair: New Mexico -235) | no line yet |  |
| Sat 11/21 TBA | Arizona @ Kansas State | Arizona 27, Kansas State 24 | Arizona 59% | Arizona -145 / Kansas State +145 | 28.9 – 25.8 | 14–44 / 13–41 | Arizona -3.1 / – | 54.8 / – | no line yet | no line yet (fair: Arizona -145) | no line yet |  |
| Sat 11/21 TBA | BYU @ Kansas | BYU 31, Kansas 24 | BYU 64% | BYU -175 / Kansas +175 | 29.1 – 23.9 | 14–44 / 10–38 | BYU -5.2 / – | 52.9 / – | no line yet | no line yet (fair: BYU -175) | no line yet |  |
| Sat 11/21 TBA | Houston @ West Virginia | Houston 34, West Virginia 31 | Houston 63% | Houston -170 / West Virginia +170 | 36.2 – 30.7 | 21–52 / 17–45 | Houston -5.5 / – | 66.9 / – | no line yet | no line yet (fair: Houston -170) | no line yet |  |
| Sat 11/21 TBA | Texas Tech @ Baylor | Texas Tech 27, Baylor 24 | Texas Tech 55% | Texas Tech -120 / Baylor +120 | 28.4 – 26.5 | 14–42 / 13–41 | Texas Tech -5.9 / Texas Tech -1.5 | 51.9 / 55.5 | no edge | no edge | no edge |  |
| Sat 11/21 TBA | Utah @ TCU | Utah 24, TCU 17 | Utah 66% | Utah -195 / TCU +195 | 25.7 – 19.7 | 13–40 / 7–33 | Utah -12.3 / Utah -5.5 | 49.4 / 44.5 | no edge | no edge | no edge |  |
| Sat 11/21 TBA | Virginia Tech @ Miami | Virginia Tech 20, Miami 41 | Miami 89% | Virginia Tech +825 / Miami -825 | 21.2 – 40.0 | 7–34 / 24–56 | Miami -21.8 / Miami -18.5 | 59.8 / 61.5 | no edge | no edge | no edge |  |
| Sat 11/21 TBA | Pittsburgh @ Louisville | Pittsburgh 17, Louisville 34 | Louisville 85% | Pittsburgh +580 / Louisville -580 | 18.5 – 34.1 | 7–31 / 20–49 | Louisville -15.6 / – | 52.6 / – | no line yet | no line yet (fair: Louisville -580) | no line yet |  |
| Sat 11/21 TBA | Wake Forest @ Georgia Tech | Wake Forest 38, Georgia Tech 17 | Wake Forest 95% | Wake Forest -1805 / Georgia Tech +1805 | 39.5 – 15.7 | 24–56 / 3–27 | Wake Forest -23.8 / – | 55.2 / – | no line yet | no line yet (fair: Wake Forest -1805) | no line yet |  |
| Sat 11/21 TBA | UCLA @ Michigan | UCLA 24, Michigan 17 | UCLA 65% | UCLA -185 / Michigan +185 | 23.5 – 18.1 | 10–37 / 7–31 | UCLA -4.1 / UCLA -5.5 | 41.7 / 41.5 | no edge | no edge | no edge |  |
| Sat 11/21 TBA | Ohio State @ Nebraska | Ohio State 24, Nebraska 21 | Ohio State 65% | Ohio State -180 / Nebraska +180 | 26.8 – 21.1 | 13–41 / 9–34 | Ohio State -7.4 / Ohio State -5.5 | 49.6 / 47.5 | no edge | no edge | no edge |  |
| Sat 11/21 TBA | Indiana @ Washington | Indiana 24, Washington 17 | Indiana 76% | Indiana -320 / Washington +320 | 27.1 – 17.0 | 13–41 / 6–29 | Indiana -10.1 / – | 44.1 / – | no line yet | no line yet (fair: Indiana -320) | no line yet |  |
| Sat 11/21 TBA | North Texas @ Tulane | North Texas 35, Tulane 28 | North Texas 70% | North Texas -235 / Tulane +235 | 35.5 – 27.2 | 20–51 / 13–42 | North Texas -8.3 / – | 62.7 / – | no line yet | no line yet (fair: North Texas -235) | no line yet |  |
| Sat 11/21 TBA | UTSA @ UAB | UTSA 31, UAB 24 | UTSA 72% | UTSA -255 / UAB +255 | 31.3 – 22.5 | 17–46 / 10–37 | UTSA -8.8 / – | 53.8 / – | no line yet | no line yet (fair: UTSA -255) | no line yet |  |
| Sat 11/21 12:00 PM | Vanderbilt @ Florida | Vanderbilt 24, Florida 31 | Florida 71% | Vanderbilt +250 / Florida -250 | 22.1 – 30.5 | 10–35 / 17–45 | Florida -8.4 / – | 52.6 / – | no line yet | no line yet (fair: Florida -250) | no line yet |  |
| Sat 11/21 12:00 PM | Wofford @ Ole Miss | Wofford 3, Ole Miss 58 | Ole Miss 100% | Wofford +9900 / Ole Miss -9900 | 3.0 – 57.6 | 0–7 / 44–73 | Ole Miss -54.6 / – | 60.6 / – | no line yet | no line yet (fair: Ole Miss -9900) | no line yet | FCS opponent |
| Sat 11/21 12:00 PM | Texas A&M @ Oklahoma | Texas A&M 24, Oklahoma 27 | Oklahoma 58% | Texas A&M +135 / Oklahoma -135 | 23.2 – 26.2 | 10–37 / 13–41 | Oklahoma -7.6 / Oklahoma -2.5 | 40.2 / 51.5 | no edge | no edge | Under 51.5 (-110*): EV +4.6%, 55%, stake 1.3u | * price not posted; assumed -110 |
| Sat 11/21 12:00 PM | Colorado @ Cincinnati | Colorado 28, Cincinnati 31 | Cincinnati 63% | Colorado +170 / Cincinnati -170 | 27.2 – 32.1 | 14–42 / 17–48 | Cincinnati -4.9 / – | 59.3 / – | no line yet | no line yet (fair: Cincinnati -170) | no line yet |  |
| Sat 11/21 12:00 PM | Syracuse @ Boston College | Syracuse 31, Boston College 24 | Syracuse 65% | Syracuse -185 / Boston College +185 | 29.0 – 22.7 | 14–44 / 10–37 | Syracuse -6.2 / – | 51.7 / – | no line yet | no line yet (fair: Syracuse -185) | no line yet |  |
| Sat 11/21 12:00 PM | Northwestern @ Minnesota | Northwestern 24, Minnesota 21 | Northwestern 60% | Northwestern -150 / Minnesota +150 | 25.1 – 21.2 | 12–38 / 9–34 | Northwestern -3.9 / – | 46.3 / – | no line yet | no line yet (fair: Northwestern -150) | no line yet |  |
| Sat 11/21 12:00 PM | Wisconsin @ Purdue | Wisconsin 24, Purdue 21 | Wisconsin 65% | Wisconsin -190 / Purdue +190 | 26.2 – 21.0 | 13–41 / 9–34 | Wisconsin -5.3 / – | 47.2 / – | no line yet | no line yet (fair: Wisconsin -190) | no line yet |  |
| Sat 11/21 12:00 PM | East Carolina @ Army | East Carolina 24, Army 27 | Army 55% | East Carolina +125 / Army -125 | 25.8 – 27.8 | 13–40 / 14–42 | Army -2.1 / – | 53.6 / – | no line yet | no line yet (fair: Army -125) | no line yet |  |
| Sat 11/21 12:00 PM | Memphis @ Navy | Memphis 31, Navy 28 | Memphis 54% | Memphis -115 / Navy +115 | 31.1 – 29.5 | 17–45 / 16–44 | Memphis -1.6 / – | 60.5 / – | no line yet | no line yet (fair: Memphis -115) | no line yet |  |
| Sat 11/21 12:30 PM | North Carolina @ Virginia | North Carolina 27, Virginia 24 | North Carolina 54% | North Carolina -120 / Virginia +120 | 26.3 – 24.8 | 13–41 / 10–38 | North Carolina -1.5 / – | 51.2 / – | no line yet | no line yet (fair: North Carolina -120) | no line yet |  |
| Sat 11/21 1:00 PM | Tennessee Tech @ Mississippi State | Tennessee Tech 10, Mississippi State 41 | Mississippi State 99% | Tennessee Tech +9900 / Mississippi State -9900 | 10.2 – 41.5 | 0–20 / 27–58 | Mississippi State -31.3 / – | 51.7 / – | no line yet | no line yet (fair: Mississippi State -9900) | no line yet | FCS opponent |
| Sat 11/21 1:00 PM | Western Kentucky @ Liberty | Western Kentucky 17, Liberty 34 | Liberty 87% | Western Kentucky +685 / Liberty -685 | 18.3 – 35.3 | 7–31 / 20–51 | Liberty -17.0 / – | 53.6 / – | no line yet | no line yet (fair: Liberty -685) | no line yet |  |
| Sat 11/21 2:00 PM | Chattanooga @ Alabama | Chattanooga 3, Alabama 55 | Alabama 100% | Chattanooga +9900 / Alabama -9900 | 3.0 – 55.6 | 0–7 / 41–72 | Alabama -52.6 / – | 58.6 / – | no line yet | no line yet (fair: Alabama -9900) | no line yet | FCS opponent |
| Sat 11/21 2:00 PM | Charlotte @ Tulsa | Charlotte 17, Tulsa 38 | Tulsa 94% | Charlotte +1550 / Tulsa -1550 | 15.8 – 38.5 | 5–28 / 23–55 | Tulsa -22.8 / – | 54.3 / – | no line yet | no line yet (fair: Tulsa -1550) | no line yet |  |
| Sat 11/21 2:00 PM | Missouri State @ Jacksonville State | Missouri State 24, Jacksonville State 34 | Jacksonville State 81% | Missouri State +420 / Jacksonville State -420 | 21.2 – 34.3 | 9–35 / 20–50 | Jacksonville State -13.1 / – | 55.4 / – | no line yet | no line yet (fair: Jacksonville State -420) | no line yet |  |
| Sat 11/21 2:00 PM | Middle Tennessee @ Sam Houston | Middle Tennessee 24, Sam Houston 21 | Middle Tennessee 52% | Middle Tennessee -110 / Sam Houston +110 | 22.8 – 22.0 | 10–37 / 10–35 | Middle Tennessee -0.8 / – | 44.8 / – | no line yet | no line yet (fair: Middle Tennessee -110) | no line yet |  |
| Sat 11/21 2:30 PM | Iowa @ Illinois | Iowa 24, Illinois 21 | Iowa 66% | Iowa -195 / Illinois +195 | 25.0 – 19.5 | 12–39 / 7–33 | Iowa -6.2 / Iowa -5.5 | 49.1 / 43.5 | no edge | no edge | no edge |  |
| Sat 11/21 2:30 PM | South Florida @ Florida Atlantic | South Florida 31, Florida Atlantic 34 | Florida Atlantic 57% | South Florida +130 / Florida Atlantic -130 | 30.5 – 33.1 | 17–45 / 18–49 | Florida Atlantic -2.5 / – | 63.6 / – | no line yet | no line yet (fair: Florida Atlantic -130) | no line yet |  |
| Sat 11/21 2:30 PM | UL Monroe @ App State | UL Monroe 21, App State 31 | App State 79% | UL Monroe +380 / App State -380 | 21.4 – 33.0 | 9–35 / 17–48 | App State -11.7 / – | 54.4 / – | no line yet | no line yet (fair: App State -380) | no line yet |  |
| Sat 11/21 3:00 PM | Coastal Carolina @ Louisiana | Coastal Carolina 24, Louisiana 27 | Louisiana 64% | Coastal Carolina +180 / Louisiana -180 | 22.7 – 28.4 | 10–37 / 14–43 | Louisiana -5.7 / – | 51.0 / – | no line yet | no line yet (fair: Louisiana -180) | no line yet |  |
| Sat 11/21 3:00 PM | Delaware @ New Mexico State | Delaware 31, New Mexico State 24 | Delaware 72% | Delaware -255 / New Mexico State +255 | 31.9 – 23.3 | 17–47 / 10–37 | Delaware -8.5 / – | 55.2 / – | no line yet | no line yet (fair: Delaware -255) | no line yet |  |
| Sat 11/21 3:00 PM | Florida International @ Kennesaw State | Florida International 21, Kennesaw State 24 | Kennesaw State 65% | Florida International +185 / Kennesaw State -185 | 21.1 – 26.5 | 9–34 / 13–41 | Kennesaw State -5.4 / – | 47.6 / – | no line yet | no line yet (fair: Kennesaw State -185) | no line yet |  |
| Sat 11/21 3:30 PM | Samford @ Auburn | Samford 3, Auburn 48 | Auburn 100% | Samford +9900 / Auburn -9900 | 3.0 – 47.4 | 0–7 / 33–63 | Auburn -44.3 / – | 50.4 / – | no line yet | no line yet (fair: Auburn -9900) | no line yet | FCS opponent |
| Sat 11/21 3:30 PM | LSU @ Tennessee | LSU 24, Tennessee 21 | LSU 54% | LSU -120 / Tennessee +120 | 25.1 – 23.5 | 13–38 / 10–38 | LSU -2.9 / LSU -1.5 | 49.2 / 48.5 | no edge | no edge | no edge |  |
| Sat 11/21 3:30 PM | Arkansas @ Texas | Arkansas 10, Texas 34 | Texas 96% | Arkansas +2265 / Texas -2265 | 12.0 – 34.5 | 3–22 / 20–49 | Texas -22.6 / – | 46.5 / – | no line yet | no line yet (fair: Texas -2265) | no line yet |  |
| Sat 11/21 3:30 PM | NC State @ Florida State | NC State 24, Florida State 31 | Florida State 69% | NC State +225 / Florida State -225 | 25.8 – 33.8 | 13–41 / 20–49 | Florida State -8.0 / – | 59.7 / – | no line yet | no line yet (fair: Florida State -225) | no line yet |  |
| Sat 11/21 3:30 PM | Rutgers @ Penn State | Rutgers 17, Penn State 38 | Penn State 92% | Rutgers +1150 / Penn State -1150 | 15.8 – 36.1 | 5–28 / 21–52 | Penn State -20.3 / – | 51.9 / – | no line yet | no line yet (fair: Penn State -1150) | no line yet |  |
| Sat 11/21 3:30 PM | Old Dominion @ UConn | Old Dominion 17, UConn 34 | UConn 89% | Old Dominion +790 / UConn -790 | 15.6 – 32.9 | 6–27 / 17–49 | UConn -17.3 / – | 48.5 / – | no line yet | no line yet (fair: UConn -790) | no line yet |  |
| Sat 11/21 4:00 PM | Northern Illinois @ North Dakota State | Northern Illinois 13, North Dakota State 34 | North Dakota State 93% | Northern Illinois +1435 / North Dakota State -1435 | 13.3 – 34.8 | 3–24 / 20–50 | North Dakota State -21.5 / – | 48.1 / – | no line yet | no line yet (fair: North Dakota State -1435) | no line yet |  |
| Sat 11/21 4:00 PM | Georgia Southern @ Troy | Georgia Southern 27, Troy 24 | Georgia Southern 61% | Georgia Southern -160 / Troy +160 | 27.0 – 22.8 | 14–41 / 10–36 | Georgia Southern -4.2 / – | 49.8 / – | no line yet | no line yet (fair: Georgia Southern -160) | no line yet |  |
| Sat 11/21 4:00 PM | Georgia State @ Marshall | Georgia State 28, Marshall 31 | Marshall 53% | Georgia State +115 / Marshall -115 | 28.1 – 29.7 | 14–42 / 16–44 | Marshall -1.5 / – | 57.8 / – | no line yet | no line yet (fair: Marshall -115) | no line yet |  |
| Sat 11/21 4:00 PM | South Alabama @ Southern Miss | South Alabama 34, Southern Miss 31 | South Alabama 56% | South Alabama -130 / Southern Miss +130 | 31.4 – 28.8 | 17–45 / 14–44 | South Alabama -2.6 / – | 60.2 / – | no line yet | no line yet (fair: South Alabama -130) | no line yet |  |
| Sat 11/21 6:00 PM | Washington State @ Texas State | Washington State 24, Texas State 34 | Texas State 78% | Washington State +345 / Texas State -345 | 23.7 – 35.2 | 10–37 / 21–50 | Texas State -11.6 / – | 58.9 / – | no line yet | no line yet (fair: Texas State -345) | no line yet |  |
| Sat 11/21 6:15 PM | Maryland @ USC | Maryland 21, USC 31 | USC 80% | Maryland +400 / USC -400 | 21.1 – 33.5 | 9–34 / 20–49 | USC -12.5 / – | 54.6 / – | no line yet | no line yet (fair: USC -400) | no line yet |  |
| Sat 11/21 7:00 PM | UNLV @ San José State | UNLV 31, San José State 24 | UNLV 68% | UNLV -215 / San José State +215 | 29.2 – 22.1 | 14–44 / 10–35 | UNLV -7.1 / – | 51.3 / – | no line yet | no line yet (fair: UNLV -215) | no line yet |  |
| Sat 11/21 7:00 PM | Arkansas State @ Louisiana Tech | Arkansas State 21, Louisiana Tech 31 | Louisiana Tech 77% | Arkansas State +335 / Louisiana Tech -335 | 19.9 – 30.6 | 7–33 / 17–45 | Louisiana Tech -10.8 / – | 50.5 / – | no line yet | no line yet (fair: Louisiana Tech -335) | no line yet |  |
| Sat 11/21 7:30 PM | Kentucky @ Missouri | Kentucky 20, Missouri 27 | Missouri 66% | Kentucky +200 / Missouri -200 | 21.6 – 27.8 | 10–35 / 14–42 | Missouri -8.8 / Missouri -6.0 | 49.1 / 49.5 | no edge | no edge | no edge |  |
| Sat 11/21 7:30 PM | Georgia @ South Carolina | Georgia 31, South Carolina 21 | Georgia 75% | Georgia -300 / South Carolina +300 | 30.7 – 20.6 | 16–45 / 7–34 | Georgia -11.2 / Georgia -10.0 | 50.1 / 51.5 | no edge | no edge | no edge |  |
| Sat 11/21 7:30 PM | SMU @ Notre Dame | SMU 21, Notre Dame 38 | Notre Dame 87% | SMU +650 / Notre Dame -650 | 20.1 – 36.6 | 7–34 / 21–52 | Notre Dame -17.2 / Notre Dame -16.5 | 52.9 / 57.5 | no edge | no edge | no edge |  |
| Sat 11/21 7:30 PM | Stanford @ California | Stanford 24, California 31 | California 61% | Stanford +160 / California -160 | 25.4 – 30.1 | 13–40 / 16–45 | California -4.6 / – | 55.5 / – | no line yet | no line yet (fair: California -160) | no line yet |  |
| Sat 11/21 7:30 PM | Colorado State @ Fresno State | Colorado State 24, Fresno State 34 | Fresno State 75% | Colorado State +300 / Fresno State -300 | 25.1 – 35.1 | 12–39 / 20–51 | Fresno State -10.0 / – | 60.2 / – | no line yet | no line yet (fair: Fresno State -300) | no line yet |  |
| Sat 11/21 9:30 PM | San Diego State @ Boise State | San Diego State 21, Boise State 38 | Boise State 87% | San Diego State +660 / Boise State -660 | 19.9 – 36.3 | 7–33 / 21–52 | Boise State -16.4 / – | 56.3 / – | no line yet | no line yet (fair: Boise State -660) | no line yet |  |
| Sat 11/21 10:15 PM | Oklahoma State @ Arizona State | Oklahoma State 31, Arizona State 28 | Oklahoma State 56% | Oklahoma State -130 / Arizona State +130 | 30.0 – 27.8 | 16–45 / 14–42 | Oklahoma State -2.2 / – | 57.8 / – | no line yet | no line yet (fair: Oklahoma State -130) | no line yet |  |
| Sat 11/21 10:30 PM | Utah State @ Oregon State | Utah State 24, Oregon State 31 | Oregon State 74% | Utah State +280 / Oregon State -280 | 21.8 – 31.2 | 10–35 / 17–46 | Oregon State -9.4 / – | 53.0 / – | no line yet | no line yet (fair: Oregon State -280) | no line yet |  |
| Sat 11/21 10:30 PM | Hawai'i @ Nevada | Hawai'i 24, Nevada 21 | Hawai'i 58% | Hawai'i -140 / Nevada +140 | 25.6 – 22.8 | 13–40 / 10–36 | Hawai'i -2.8 / – | 48.4 / – | no line yet | no line yet (fair: Hawai'i -140) | no line yet |  |

## How the 2026 predictions have done

| Predictor | Games | Margin MAE | Total MAE | Team-score MAE | Winners | Brier | 80% range hit |
|---|---|---|---|---|---|---|---|
| Final prediction | 705 | 11.81 | 12.30 | 8.52 | 78.7% | 0.147 | 81.4% |
| Model only (before blending) | 705 | 12.57 | 12.66 | 8.80 | 75.7% | – | – |
| Betting line when predicted | 703 | 11.80 | 12.26 | 8.51 | 78.8% | – | – |

MAE is mean absolute error in points (lower is better). Brier scores the win chances (lower is better, 0.25 is a coin flip). Even the closing betting line misses the final margin of an FBS game by about 12.5 points.

501 of these games were played before the predictor went live. They are backfilled walk-forward (each week predicted from earlier weeks only) but with closing lines, so they flatter the model slightly. Every game since is graded on the prediction logged before kickoff.

### Betting edges

| Market | Edges | Record (W-L-P) | Staked | Units won | ROI | Expected ROI |
|---|---|---|---|---|---|---|
| Spread | 0 | 0-0-0 | 0.0 | +0.00 | – | – |
| Moneyline | 9 | 1-8-0 | 2.9 | -0.88 | -30.7% | +4.6% |
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

## FBS power ratings

Points per game better than an average FBS team on a neutral field, from opponent-adjusted EPA (garbage time removed) with this season's games weighted against a preseason prior, plus the weight the margin model puts on Elo (a rating built from game results alone). Defense is positive when it holds opponents below average.

| # | Team | Conference | Net | Offense | Defense | Special teams | Results (Elo) | Elo rating |
|---|---|---|---|---|---|---|---|---|
| 1 | Georgia | SEC | +25.6 | +8.2 | +11.6 | +0.8 | +5.0 | 1931 |
| 2 | LSU | SEC | +23.7 | +9.6 | +11.8 | +0.0 | +2.3 | 1703 |
| 3 | Miami | ACC | +23.5 | +15.2 | +3.5 | +0.3 | +4.5 | 1881 |
| 4 | Ohio State | Big Ten | +23.2 | +10.0 | +9.3 | +0.2 | +3.7 | 1817 |
| 5 | Notre Dame | FBS Independents | +23.2 | +8.6 | +9.1 | +1.0 | +4.5 | 1888 |
| 6 | Alabama | SEC | +21.9 | +9.6 | +8.2 | +0.3 | +3.8 | 1825 |
| 7 | Indiana | Big Ten | +21.3 | +5.5 | +10.5 | +0.1 | +5.1 | 1939 |
| 8 | Wake Forest | ACC | +20.4 | +7.5 | +9.1 | +0.6 | +3.2 | 1776 |
| 9 | Utah | Big 12 | +20.4 | +10.1 | +6.2 | -0.1 | +4.2 | 1862 |
| 10 | Texas | SEC | +19.7 | +2.4 | +12.5 | +0.8 | +4.1 | 1848 |
| 11 | Oregon | Big Ten | +19.6 | +6.0 | +9.5 | +0.5 | +3.6 | 1806 |
| 12 | UCLA | Big Ten | +17.7 | +4.6 | +9.7 | +0.8 | +2.6 | 1729 |
| 13 | Texas Tech | Big 12 | +17.3 | +2.8 | +10.1 | +1.3 | +3.1 | 1767 |
| 14 | Tennessee | SEC | +17.3 | +4.3 | +8.7 | +1.2 | +3.0 | 1758 |
| 15 | Ole Miss | SEC | +16.5 | +9.3 | +3.4 | +0.7 | +3.1 | 1764 |
| 16 | Louisville | ACC | +16.5 | +9.9 | +4.0 | +0.2 | +2.3 | 1699 |
| 17 | Oklahoma | SEC | +16.4 | +1.0 | +12.9 | +0.6 | +1.8 | 1659 |
| 18 | Missouri | SEC | +14.3 | +4.2 | +7.7 | +0.4 | +2.0 | 1680 |
| 19 | Iowa | Big Ten | +14.3 | +1.4 | +8.6 | +1.0 | +3.3 | 1783 |
| 20 | USC | Big Ten | +13.7 | +10.4 | +0.3 | +0.3 | +2.7 | 1738 |
| 21 | Nebraska | Big Ten | +13.4 | +3.9 | +8.2 | +0.4 | +1.0 | 1589 |
| 22 | BYU | Big 12 | +13.2 | +5.2 | +4.5 | +0.7 | +2.8 | 1739 |
| 23 | Michigan | Big Ten | +12.4 | +2.2 | +9.3 | -0.3 | +1.1 | 1602 |
| 24 | South Carolina | SEC | +12.3 | +5.7 | +3.9 | +0.6 | +2.1 | 1683 |
| 25 | Arizona | Big 12 | +12.0 | +5.9 | +3.5 | +0.1 | +2.4 | 1713 |
| 26 | Penn State | Big Ten | +12.0 | +3.8 | +6.5 | +0.1 | +1.6 | 1640 |
| 27 | Auburn | SEC | +11.6 | +5.0 | +5.5 | +0.6 | +0.5 | 1550 |
| 28 | Texas A&M | SEC | +11.3 | +2.4 | +7.6 | +0.4 | +0.8 | 1579 |
| 29 | SMU | ACC | +10.7 | +6.7 | +2.3 | +0.2 | +1.5 | 1637 |
| 30 | Florida | SEC | +10.6 | +5.7 | +3.8 | +0.8 | +0.3 | 1534 |
| 31 | Oklahoma State | Big 12 | +9.9 | +9.1 | -0.2 | +0.5 | +0.6 | 1556 |
| 32 | Northwestern | Big Ten | +9.4 | +5.7 | +2.1 | +0.6 | +1.0 | 1591 |
| 33 | Baylor | Big 12 | +9.4 | +0.7 | +6.3 | +0.9 | +1.4 | 1628 |
| 34 | Houston | Big 12 | +9.3 | +8.9 | -1.2 | +0.3 | +1.4 | 1621 |
| 35 | Washington | Big Ten | +8.8 | +2.3 | +4.8 | +0.1 | +1.6 | 1642 |
| 36 | Duke | ACC | +8.6 | +4.4 | +1.2 | +0.8 | +2.3 | 1700 |
| 37 | Mississippi State | SEC | +8.3 | +4.4 | +4.1 | -0.1 | -0.2 | 1493 |
| 38 | Kentucky | SEC | +8.2 | +2.5 | +4.0 | +0.1 | +1.6 | 1642 |
| 39 | Iowa State | Big 12 | +7.6 | +4.6 | +1.2 | +1.0 | +0.9 | 1581 |
| 40 | Wisconsin | Big Ten | +7.0 | -1.8 | +7.2 | +0.8 | +0.8 | 1575 |
| 41 | Kansas | Big 12 | +6.6 | +5.0 | +2.8 | -0.2 | -1.0 | 1428 |
| 42 | Kansas State | Big 12 | +6.5 | +4.6 | +2.3 | +0.2 | -0.7 | 1454 |
| 43 | Boise State | Pac-12 | +6.4 | +6.2 | -2.1 | -0.3 | +2.6 | 1730 |
| 44 | Illinois | Big Ten | +6.4 | +6.1 | -1.3 | +0.4 | +1.3 | 1617 |
| 45 | Florida State | ACC | +6.4 | +6.4 | +0.2 | -0.6 | +0.4 | 1540 |
| 46 | Arizona State | Big 12 | +5.9 | +1.0 | +4.3 | -0.1 | +0.7 | 1565 |
| 47 | TCU | Big 12 | +5.5 | -2.0 | +6.5 | +0.1 | +0.9 | 1582 |
| 48 | Cincinnati | Big 12 | +5.2 | +9.0 | -4.0 | +0.3 | -0.0 | 1507 |
| 49 | Vanderbilt | SEC | +4.9 | +3.6 | +0.4 | +0.5 | +0.5 | 1547 |
| 50 | Clemson | ACC | +4.9 | -4.6 | +8.2 | +0.8 | +0.5 | 1547 |
| 51 | Virginia Tech | ACC | +4.3 | +4.0 | -0.2 | +0.1 | +0.4 | 1541 |
| 52 | North Carolina | ACC | +3.9 | +3.4 | -0.8 | +0.8 | +0.5 | 1554 |
| 53 | North Texas | American Athletic | +3.7 | +10.4 | -7.5 | -0.8 | +1.7 | 1651 |
| 54 | Colorado | Big 12 | +3.6 | +1.1 | +4.0 | -0.6 | -0.9 | 1432 |
| 55 | UCF | Big 12 | +3.5 | +1.5 | +2.3 | +0.2 | -0.5 | 1470 |
| 56 | Maryland | Big Ten | +3.4 | -0.1 | +4.2 | +0.5 | -1.2 | 1408 |
| 57 | Minnesota | Big Ten | +3.0 | -3.6 | +5.5 | +0.8 | +0.2 | 1529 |
| 58 | Pittsburgh | ACC | +2.9 | -2.8 | +5.0 | +0.5 | +0.2 | 1525 |
| 59 | Syracuse | ACC | +2.9 | +1.8 | +2.8 | -0.7 | -1.0 | 1424 |
| 60 | Memphis | American Athletic | +2.9 | +4.8 | -3.1 | -0.5 | +1.7 | 1652 |
| 61 | Texas State | Pac-12 | +1.6 | +6.1 | -4.5 | -1.1 | +1.1 | 1602 |
| 62 | Liberty | Conference USA | +1.5 | +1.8 | -1.4 | +0.4 | +0.7 | 1568 |
| 63 | West Virginia | Big 12 | +1.4 | +6.2 | -5.1 | +0.4 | -0.2 | 1495 |
| 64 | Virginia | ACC | +1.3 | -1.3 | +3.3 | -0.5 | -0.2 | 1494 |
| 65 | James Madison | Sun Belt | +1.0 | -0.8 | +0.2 | +0.2 | +1.4 | 1625 |
| 66 | Arkansas | SEC | +1.0 | +1.5 | +0.8 | -0.7 | -0.6 | 1455 |
| 67 | UTSA | American Athletic | +1.0 | +3.5 | -3.6 | -0.0 | +1.0 | 1596 |
| 68 | New Mexico | Mountain West | +0.5 | -3.7 | +2.9 | -0.2 | +1.5 | 1636 |
| 69 | NC State | ACC | +0.5 | +4.8 | -3.3 | -0.4 | -0.5 | 1467 |
| 70 | Toledo | Mid-American | +0.4 | -2.5 | +2.5 | -0.4 | +0.7 | 1567 |
| 71 | Tulsa | American Athletic | -0.2 | +0.5 | +0.4 | -0.6 | -0.5 | 1466 |
| 72 | Oregon State | Pac-12 | -0.3 | +3.3 | -2.6 | -0.0 | -1.0 | 1428 |
| 73 | Purdue | Big Ten | -0.6 | +3.2 | -3.0 | +0.7 | -1.5 | 1386 |
| 74 | UConn | FBS Independents | -0.7 | +2.9 | -3.8 | +0.1 | +0.0 | 1512 |
| 75 | Navy | American Athletic | -1.0 | +3.5 | -3.6 | -0.6 | -0.3 | 1484 |
| 76 | Michigan State | Big Ten | -1.1 | -3.1 | +2.0 | +0.6 | -0.6 | 1459 |
| 77 | North Dakota State | Mountain West | -1.3 | -4.8 | +3.5 | +1.1 | -1.1 | 1419 |
| 78 | South Florida | American Athletic | -2.5 | -1.5 | -1.4 | +0.2 | +0.3 | 1531 |
| 79 | Louisiana Tech | Sun Belt | -2.5 | -3.4 | +0.9 | -0.8 | +0.8 | 1575 |
| 80 | Florida Atlantic | American Athletic | -2.8 | +4.7 | -8.1 | +0.7 | -0.0 | 1506 |
| 81 | East Carolina | American Athletic | -3.0 | -5.4 | +2.8 | -0.5 | +0.1 | 1520 |
| 82 | Fresno State | Pac-12 | -3.7 | -2.8 | -0.8 | -0.3 | +0.3 | 1530 |
| 83 | Army | American Athletic | -3.7 | +4.3 | -8.2 | -0.1 | +0.2 | 1525 |
| 84 | Air Force | Mountain West | -4.2 | +2.2 | -6.3 | -0.2 | +0.1 | 1517 |
| 85 | Jacksonville State | Conference USA | -5.0 | -0.3 | -4.6 | -0.1 | -0.0 | 1505 |
| 86 | Georgia Tech | ACC | -5.0 | +0.4 | -4.6 | -0.2 | -0.6 | 1455 |
| 87 | Western Michigan | Mid-American | -5.3 | -3.5 | -3.3 | +0.6 | +0.8 | 1574 |
| 88 | Boston College | ACC | -5.9 | -3.5 | -0.9 | -0.6 | -0.9 | 1431 |
| 89 | California | ACC | -5.9 | -2.1 | -1.8 | -0.3 | -1.7 | 1369 |
| 90 | Georgia Southern | Sun Belt | -6.0 | -1.9 | -4.0 | -0.7 | +0.6 | 1556 |
| 91 | Utah State | Pac-12 | -6.2 | -6.9 | +2.4 | -1.1 | -0.6 | 1455 |
| 92 | UNLV | Mountain West | -6.5 | -2.9 | -3.7 | +0.2 | -0.1 | 1497 |
| 93 | Ohio | Mid-American | -6.5 | -4.0 | -2.8 | +0.1 | +0.2 | 1525 |
| 94 | Rutgers | Big Ten | -6.6 | +1.4 | -6.6 | +0.6 | -2.0 | 1342 |
| 95 | Miami (OH) | Mid-American | -6.9 | -4.9 | -2.6 | +0.9 | -0.3 | 1482 |
| 96 | Delaware | Conference USA | -7.2 | -0.3 | -5.5 | +0.1 | -1.4 | 1389 |
| 97 | Tulane | American Athletic | -8.0 | -4.8 | -2.8 | +0.2 | -0.7 | 1454 |
| 98 | San Diego State | Pac-12 | -8.1 | -4.6 | -2.5 | +0.2 | -1.2 | 1406 |
| 99 | Washington State | Pac-12 | -8.3 | -6.0 | -0.1 | -0.4 | -1.9 | 1349 |
| 100 | Louisiana | Sun Belt | -8.4 | -3.8 | -4.5 | -0.0 | -0.0 | 1505 |
| 101 | Stanford | ACC | -8.4 | -2.7 | -5.0 | -0.1 | -0.7 | 1448 |
| 102 | Georgia State | Sun Belt | -9.1 | -0.7 | -7.1 | -0.0 | -1.2 | 1407 |
| 103 | Wyoming | Mountain West | -9.2 | -5.5 | -3.0 | -0.2 | -0.6 | 1460 |
| 104 | Temple | American Athletic | -9.7 | +0.5 | -7.0 | -0.4 | -2.7 | 1279 |
| 105 | Marshall | Sun Belt | -9.8 | -5.1 | -4.0 | -0.1 | -0.6 | 1456 |
| 106 | App State | Sun Belt | -10.0 | -3.9 | -3.8 | -0.5 | -1.8 | 1361 |
| 107 | UAB | American Athletic | -10.0 | -7.2 | -1.6 | -0.2 | -1.1 | 1419 |
| 108 | Hawai'i | Mountain West | -10.5 | -3.8 | -6.1 | +1.0 | -1.6 | 1374 |
| 109 | Colorado State | Pac-12 | -11.4 | +4.7 | -13.2 | -0.2 | -2.8 | 1278 |
| 110 | Central Michigan | Mid-American | -11.5 | -6.2 | -4.4 | +0.0 | -0.9 | 1429 |
| 111 | Arkansas State | Sun Belt | -11.8 | -3.3 | -7.3 | +0.0 | -1.2 | 1408 |
| 112 | Troy | Sun Belt | -12.0 | -8.6 | -0.3 | -1.4 | -1.7 | 1366 |
| 113 | Kennesaw State | Conference USA | -12.1 | -6.2 | -3.7 | -0.5 | -1.7 | 1363 |
| 114 | South Alabama | Sun Belt | -12.1 | -0.1 | -10.8 | +0.3 | -1.4 | 1388 |
| 115 | Coastal Carolina | Sun Belt | -12.2 | -6.7 | -3.9 | +0.4 | -2.1 | 1334 |
| 116 | Old Dominion | Sun Belt | -12.5 | -13.6 | +4.0 | -1.7 | -1.2 | 1407 |
| 117 | Western Kentucky | Conference USA | -12.5 | -5.3 | -4.5 | -0.2 | -2.4 | 1306 |
| 118 | Rice | American Athletic | -12.9 | -3.6 | -5.3 | -0.8 | -3.2 | 1240 |
| 119 | Florida International | Conference USA | -14.2 | -10.4 | -0.6 | -1.5 | -1.7 | 1366 |
| 120 | Missouri State | Conference USA | -14.6 | -3.1 | -7.4 | -1.2 | -2.9 | 1268 |
| 121 | Nevada | Mountain West | -15.0 | -10.9 | -2.0 | +0.4 | -2.4 | 1309 |
| 122 | Buffalo | Mid-American | -15.1 | -10.9 | -4.3 | +0.3 | -0.2 | 1491 |
| 123 | Southern Miss | Sun Belt | -15.6 | -8.2 | -3.9 | -1.2 | -2.3 | 1318 |
| 124 | San José State | Mountain West | -15.8 | -10.1 | -3.5 | +0.0 | -2.3 | 1318 |
| 125 | New Mexico State | Conference USA | -16.2 | -7.6 | -3.7 | -1.9 | -3.0 | 1258 |
| 126 | Middle Tennessee | Conference USA | -17.1 | -5.9 | -8.7 | -0.0 | -2.5 | 1296 |
| 127 | Bowling Green | Mid-American | -17.8 | -11.3 | -4.0 | +0.1 | -2.6 | 1290 |
| 128 | Northern Illinois | Mountain West | -18.3 | -3.8 | -8.8 | -1.1 | -4.5 | 1130 |
| 129 | UL Monroe | Sun Belt | -18.4 | -6.0 | -7.0 | -1.5 | -3.9 | 1184 |
| 130 | Massachusetts | Mid-American | -18.4 | -10.4 | -4.4 | -0.2 | -3.4 | 1221 |
| 131 | Ball State | Mid-American | -19.0 | -7.0 | -7.9 | -0.6 | -3.5 | 1218 |
| 132 | Sam Houston | Conference USA | -19.0 | -12.5 | -0.8 | -1.3 | -4.4 | 1136 |
| 133 | Eastern Michigan | Mid-American | -19.2 | -7.9 | -8.0 | -0.6 | -2.6 | 1287 |
| 134 | Sacramento State | Mid-American | -20.3 | -11.5 | -4.5 | +0.2 | -4.5 | 1136 |
| 135 | Charlotte | American Athletic | -20.6 | -8.1 | -8.0 | -0.7 | -3.8 | 1190 |
| 136 | Kent State | Mid-American | -21.4 | -10.7 | -6.5 | -0.9 | -3.4 | 1221 |
| 137 | Akron | Mid-American | -23.9 | -10.4 | -9.0 | -0.6 | -3.9 | 1185 |
| 138 | UTEP | Mountain West | -24.4 | -11.6 | -6.8 | -1.2 | -4.8 | 1103 |

## Current model fit

- Fitted on 4322 games from seasons 2022–2026.
- Home field on top of the ratings: 3.3 points (1.8 in conference games).
- Extra FBS edge over FCS opponents beyond their ratings: 14.1 points.
- Elo weight: 0.19 points of margin per point of Elo spread.
- Weight on the betting line: 92% for the margin, 82% for the total.
