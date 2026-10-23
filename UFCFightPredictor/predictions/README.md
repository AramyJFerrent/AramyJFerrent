# UFC fight predictions

Updated Fri Oct 23, 2026 03:02 PM ET. Refreshed automatically every day and several times on fight week; each bout's prediction is locked when its part of the card starts and graded once the result is in.

Each bout gets one consistent breakdown: each fighter's chance to win, split into KO/TKO, submission and decision, and the chance it ends in each round. The win chance blends the model with the betting market (about 81% market, the weight that has predicted best on past fights) and corrects the market's habit of underrating heavy favorites. MMA is high-variance: even the most likely single result is usually well under 50%.

The fair odds are the American odds that match the win chance with no bookmaker margin: -200 means risk $200 to win $100, +200 means risk $100 to win $200. A sportsbook only offers value on a fighter when its price beats the fair line.

The three edge columns value every side of each market at its posted price: expected value (EV) is the average profit per $1 staked, from the final prediction: the win chance blended with the moneyline (which corrects the market's habit of underrating heavy favorites), and method and round chances anchored to their own props, moved only by what the blend changes. A side is an edge when its EV is at least 3%; each cell names the best side if one clears that bar, with its stake, a 25% share of the Kelly stake in units of 1% of the bankroll, at most 3 units on one bout; else "no edge". Moneylines and props are never priced near -110, so a missing price is never assumed: without one, the round-total cell shows the model's fair odds at the line closest to even and the method cell each fighter's fair KO/TKO, submission and decision odds. Over 1.5 rounds means the fight passes 2:30 of round 2 (a decision is always over); finishes are assumed spread evenly within a round.

See the backtest (backtest.md) for how these edges did against the dataset's closing prices, next to the model alone, which finds a 3% edge in most fights and lost money on them. Treat these columns as a live test, tracked below, not as betting advice.

## UFC 333: Volkanovski vs. Evloev

Saturday, October 24, 2026 · first bout locks Sat Oct 24, 10:00 AM ET

| Bout | Win chance | Fair odds | Market | Model alone | KO / Sub / Dec | Distance | Most likely result | Moneyline edge | Round total edge | Method edge |
|---|---|---|---|---|---|---|---|---|---|---|
| **Alexander Volkanovski** vs. **Movsar Evloev**<br>FW, title, 5 rds | Volkanovski 49% – 51% Evloev | +105 / -105 | Volkanovski 50% (-110 / -110) | Volkanovski 44% (+130) | Volkanovski 16% / 5% / 28%<br>Evloev 13% / 6% / 33% | 60% | Evloev by decision (33%) | no edge | no edge | no prices yet; fair KO / Sub / Dec<br>Volkanovski +515 / +2055 / +265<br>Evloev +645 / +1715 / +205 |
| **Petr Yan** vs. **Merab Dvalishvili**<br>BW, title, 5 rds | Yan 56% – 44% Dvalishvili | -125 / +125 | Yan 55% (-135 / +114) | Yan 51% (-105) | Yan 15% / 5% / 36%<br>Dvalishvili 6% / 7% / 32% | 67% | Yan by decision (36%) | no edge | no edge | no prices yet; fair KO / Sub / Dec<br>Yan +575 / +1890 / +180<br>Dvalishvili +1520 / +1430 / +215 |
| **Lone'er Kavanagh** vs. **Ramazan Temirov**<br>FLW, 3 rds | Kavanagh 50% – 50% Temirov | -100 / +100 | Kavanagh 52% (-118 / -102) | Kavanagh 43% (+130) | Kavanagh 11% / 6% / 33%<br>Temirov 24% / 4% / 22% | 55% | Kavanagh by decision (33%) | no edge | no edge | no prices yet; fair KO / Sub / Dec<br>Kavanagh +845 / +1475 / +200<br>Temirov +320 / +2290 / +355 |
| **Alexander Volkov** vs. **Rizvan Kuniev**<br>HW, 3 rds | Volkov 52% – 48% Kuniev | -110 / +110 | Volkov 53% (-125 / +105) | Volkov 45% (+125) | Volkov 23% / 3% / 26%<br>Kuniev 24% / 3% / 21% | 47% | Volkov by decision (26%) | no edge | no edge | no prices yet; fair KO / Sub / Dec<br>Volkov +335 / +3010 / +290<br>Kuniev +320 / +3045 / +375 |
| **Aaron Pico** vs. **Losene Keita**<br>FW, 3 rds | Pico 55% – 45% Keita | -125 / +125 | Pico 58% (-155 / +130) | Pico 37% (+170) | Pico 11% / 6% / 38%<br>Keita 22% / 4% / 19% | 57% | Pico by decision (38%) | no edge | no edge | no prices yet; fair KO / Sub / Dec<br>Pico +805 / +1555 / +160<br>Keita +350 / +2725 / +430 |
| **Azamat Murzakanov** vs. **Dominick Reyes**<br>LHW, 3 rds | Murzakanov 63% – 37% Reyes | -170 / +170 | Murzakanov 64% (-205 / +170) | Murzakanov 40% (+150) | Murzakanov 42% / 5% / 16%<br>Reyes 22% / 3% / 12% | 28% | Murzakanov by KO/TKO (42%) | no edge | no edge | no prices yet; fair KO / Sub / Dec<br>Murzakanov +140 / +1965 / +515<br>Reyes +345 / +3850 / +715 |
| **Nikita Krylov** vs. **Abdul-Rakhman Yakhyaev**<br>LHW, 3 rds | Krylov 16% – 84% Yakhyaev | +525 / -525 | Krylov 19% (+410 / -550) | Krylov 35% (+185) | Krylov 7% / 3% / 7%<br>Yakhyaev 47% / 26% / 10% | 17% | Yakhyaev by KO/TKO (47%) | no edge | no edge | no prices yet; fair KO / Sub / Dec<br>Krylov +1395 / +3560 / +1415<br>Yakhyaev +110 / +285 / +855 |
| **Abus Magomedov** vs. **Cam Rowston**<br>MW, 3 rds | Magomedov 49% – 51% Rowston | +105 / -105 | Magomedov 53% (-125 / +105) | Magomedov 32% (+210) | Magomedov 13% / 12% / 24%<br>Rowston 23% / 6% / 22% | 46% | Magomedov by decision (24%) | Rowston (+105): EV +4.8%, 51%, stake 1.1u | no edge | no prices yet; fair KO / Sub / Dec<br>Magomedov +680 / +715 / +320<br>Rowston +335 / +1620 / +345 |
| **Grant Dawson** vs. **Nurullo Aliev**<br>LW, 3 rds | Dawson 50% – 50% Aliev | -100 / +100 | Dawson 52% (-118 / -102) | Dawson 44% (+130) | Dawson 8% / 17% / 25%<br>Aliev 11% / 8% / 31% | 56% | Aliev by decision (31%) | no edge | no edge | no prices yet; fair KO / Sub / Dec<br>Dawson +1085 / +505 / +295<br>Aliev +840 / +1160 / +220 |
| **Colby Thicknesse** vs. **Asaf Chopurov**<br>BW, 3 rds, UFC debut: Chopurov | Thicknesse 19% – 81% Chopurov | +425 / -425 | Thicknesse 18% (+440 / -575) | Thicknesse 63% (-170) | Thicknesse 5% / 4% / 10%<br>Chopurov 19% / 15% / 47% | 57% | Chopurov by decision (47%) | no edge | no edge | no prices yet; fair KO / Sub / Dec<br>Thicknesse +1850 / +2465 / +900<br>Chopurov +415 / +580 / +115 |
| **Abubakar Vagaev** vs. **Jacob Malkoun**<br>MW, 3 rds | Vagaev 57% – 43% Malkoun | -130 / +130 | Vagaev 59% (-162 / +136) | Vagaev 38% (+165) | Vagaev 14% / 9% / 34%<br>Malkoun 13% / 8% / 23% | 57% | Vagaev by decision (34%) | no edge | no edge | no prices yet; fair KO / Sub / Dec<br>Vagaev +625 / +980 / +195<br>Malkoun +685 / +1215 / +335 |
| **Bolaji Oki** vs. **Daniel Santos**<br>FW, 3 rds | Oki 45% – 55% Santos | +120 / -120 | Oki 48% (+100 / -120) | Oki 40% (+150) | Oki 17% / 3% / 25%<br>Santos 25% / 6% / 24% | 49% | Santos by KO/TKO (25%) | no edge | no edge | no prices yet; fair KO / Sub / Dec<br>Oki +480 / +3130 / +300<br>Santos +300 / +1700 / +320 |
| **Kody Steele** vs. **Noah Gugnon**<br>LW, 3 rds | Steele 53% – 47% Gugnon | -110 / +110 | Steele 58% (-155 / +130) | Steele 27% (+275) | Steele 12% / 18% / 22%<br>Gugnon 14% / 18% / 15% | 37% | Steele by decision (22%) | Gugnon (+130): EV +9.1%, 47%, stake 1.7u | no edge | no prices yet; fair KO / Sub / Dec<br>Steele +745 / +445 / +350<br>Gugnon +610 / +445 / +570 |
| **Iasmin Lucindo** vs. **Nicolle Caliari**<br>W-SW, 3 rds | Lucindo 82% – 18% Caliari | -470 / +470 | Lucindo 78% (-425 / +330) | Lucindo 75% (-300) | Lucindo 10% / 12% / 61%<br>Caliari 1% / 3% / 13% | 74% | Lucindo by decision (61%) | no edge | no edge | no prices yet; fair KO / Sub / Dec<br>Lucindo +945 / +755 / -160<br>Caliari +6905 / +2995 / +680 |

When it ends (either fighter):

| Bout | Round 1 | Round 2 | Round 3 | Round 4 | Round 5 | Decision |
|---|---|---|---|---|---|---|
| Volkanovski vs. Evloev | 13% | 11% | 8% | 4% | 4% | 60% |
| Yan vs. Dvalishvili | 10% | 9% | 6% | 4% | 3% | 67% |
| Kavanagh vs. Temirov | 22% | 15% | 8% |  |  | 55% |
| Volkov vs. Kuniev | 28% | 17% | 8% |  |  | 47% |
| Pico vs. Keita | 21% | 14% | 7% |  |  | 57% |
| Murzakanov vs. Reyes | 41% | 21% | 9% |  |  | 28% |
| Krylov vs. Yakhyaev | 52% | 23% | 9% |  |  | 17% |
| Magomedov vs. Rowston | 28% | 17% | 9% |  |  | 46% |
| Dawson vs. Aliev | 22% | 14% | 7% |  |  | 56% |
| Thicknesse vs. Chopurov | 21% | 14% | 7% |  |  | 57% |
| Vagaev vs. Malkoun | 22% | 14% | 7% |  |  | 57% |
| Oki vs. Santos | 26% | 17% | 8% |  |  | 49% |
| Steele vs. Gugnon | 34% | 20% | 9% |  |  | 37% |
| Lucindo vs. Caliari | 12% | 9% | 5% |  |  | 74% |

## UFC Fight Night: Moicano vs. Nolan

Saturday, October 31, 2026 · first bout locks Sat Oct 31, 5:00 PM ET

| Bout | Win chance | Fair odds | Market | Model alone | KO / Sub / Dec | Distance | Most likely result | Moneyline edge | Round total edge | Method edge |
|---|---|---|---|---|---|---|---|---|---|---|
| **Renato Moicano** vs. **Tom Nolan**<br>LW, 5 rds | Moicano 40% – 60% Nolan | +150 / -150 | no line yet | Moicano 40% (+150) | Moicano 16% / 10% / 14%<br>Nolan 25% / 15% / 20% | 35% | Nolan by KO/TKO (25%) | no line yet | no price yet; fair Over 2.5 -105, Under +105 | no prices yet; fair KO / Sub / Dec<br>Moicano +540 / +895 / +605<br>Nolan +305 / +555 / +390 |
| **Randy Brown** vs. **Carlos Leal**<br>WW, 3 rds | Brown 51% – 49% Leal | -100 / +100 | no line yet | Brown 51% (-100) | Brown 22% / 5% / 24%<br>Leal 21% / 3% / 25% | 49% | Leal by decision (25%) | no line yet | no price yet; fair Over 2.5 -115, Under +115 | no prices yet; fair KO / Sub / Dec<br>Brown +355 / +2030 / +320<br>Leal +375 / +3130 / +295 |
| **Yana Santos** vs. **Luana Santos**<br>W-BW, 3 rds | Santos 20% – 80% Santos | +410 / -410 | no line yet | Santos 20% (+410) | Santos 2% / 1% / 16%<br>Santos 9% / 19% / 52% | 68% | Santos by decision (52%) | no line yet | no price yet; fair Over 2.5 -245, Under +245 | no prices yet; fair KO / Sub / Dec<br>Santos +4190 / +9065 / +515<br>Santos +955 / +425 / -105 |
| **Jean-Paul Lebosnoyani** vs. **Farman Hasanov**<br>WW, 3 rds | Lebosnoyani 62% – 38% Hasanov | -165 / +165 | no line yet | Lebosnoyani 62% (-165) | Lebosnoyani 15% / 13% / 34%<br>Hasanov 5% / 7% / 26% | 60% | Lebosnoyani by decision (34%) | no line yet | no price yet; fair Over 2.5 -170, Under +170 | no prices yet; fair KO / Sub / Dec<br>Lebosnoyani +565 / +645 / +195<br>Hasanov +1770 / +1430 / +290 |
| **Francis Marshall** vs. **Gaston Bolaños**<br>FW, 3 rds | Marshall 71% – 29% Bolaños | -240 / +240 | no line yet | Marshall 71% (-240) | Marshall 19% / 17% / 34%<br>Bolaños 7% / 2% / 21% | 55% | Marshall by decision (34%) | no line yet | no price yet; fair Over 2.5 -145, Under +145 | no prices yet; fair KO / Sub / Dec<br>Marshall +430 / +480 / +190<br>Bolaños +1400 / +4245 / +390 |
| **Azamat Bekoev** vs. **Andre Petroski**<br>MW, 3 rds | Bekoev 41% – 59% Petroski | +145 / -145 | no line yet | Bekoev 41% (+145) | Bekoev 20% / 5% / 16%<br>Petroski 19% / 20% / 20% | 36% | Petroski by decision (20%) | no line yet | no price yet; fair Over 1.5 -125, Under +125 | no prices yet; fair KO / Sub / Dec<br>Bekoev +405 / +1865 / +530<br>Petroski +415 / +405 / +395 |
| **Rodrigo Sezinando** vs. **Theodor Berggren**<br>WW, 3 rds | Sezinando 41% – 59% Berggren | +145 / -145 | no line yet | Sezinando 41% (+145) | Sezinando 22% / 6% / 13%<br>Berggren 30% / 8% / 21% | 34% | Berggren by KO/TKO (30%) | no line yet | no price yet; fair Over 1.5 -115, Under +115 | no prices yet; fair KO / Sub / Dec<br>Sezinando +355 / +1555 / +660<br>Berggren +240 / +1080 / +380 |
| **Julian Erosa** vs. **JeongYeong Lee**<br>FW, 3 rds | Erosa 49% – 51% Lee | +105 / -105 | no line yet | Erosa 49% (+105) | Erosa 16% / 7% / 26%<br>Lee 21% / 5% / 25% | 51% | Erosa by decision (26%) | no line yet | no price yet; fair Over 2.5 -125, Under +125 | no prices yet; fair KO / Sub / Dec<br>Erosa +540 / +1265 / +285<br>Lee +385 / +1795 / +300 |
| **Nick Klein** vs. **Joe Kropschot**<br>MW, 3 rds, UFC debut: Kropschot | Klein 46% – 54% Kropschot | +115 / -115 | no line yet | Klein 46% (+115) | Klein 13% / 15% / 18%<br>Kropschot 26% / 12% / 16% | 33% | Kropschot by KO/TKO (26%) | no line yet | no price yet; fair Over 1.5 -110, Under +110 | no prices yet; fair KO / Sub / Dec<br>Klein +650 / +555 / +460<br>Kropschot +280 / +755 / +545 |
| **Talita Alencar** vs. **Piera Rodriguez**<br>W-SW, 3 rds | Alencar 42% – 58% Rodriguez | +135 / -135 | no line yet | Alencar 42% (+135) | Alencar 3% / 7% / 32%<br>Rodriguez 5% / 4% / 49% | 81% | Rodriguez by decision (49%) | no line yet | no price yet; fair Over 2.5 -490, Under +490 | no prices yet; fair KO / Sub / Dec<br>Alencar +3155 / +1360 / +210<br>Rodriguez +2090 / +2235 / +105 |
| **Lucia Szabová** vs. **Tainara Lisboa**<br>W-FLW, 3 rds, UFC debut: Szabová | Szabová 67% – 33% Lisboa | -205 / +205 | no line yet | Szabová 67% (-205) | Szabová 11% / 18% / 38%<br>Lisboa 4% / 7% / 23% | 60% | Szabová by decision (38%) | no line yet | no price yet; fair Over 2.5 -175, Under +175 | no prices yet; fair KO / Sub / Dec<br>Szabová +810 / +450 / +165<br>Lisboa +2540 / +1405 / +345 |

When it ends (either fighter):

| Bout | Round 1 | Round 2 | Round 3 | Round 4 | Round 5 | Decision |
|---|---|---|---|---|---|---|
| Moicano vs. Nolan | 24% | 19% | 11% | 6% | 5% | 35% |
| Brown vs. Leal | 26% | 17% | 8% |  |  | 49% |
| Santos vs. Santos | 15% | 11% | 6% |  |  | 68% |
| Lebosnoyani vs. Hasanov | 20% | 13% | 7% |  |  | 60% |
| Marshall vs. Bolaños | 23% | 15% | 8% |  |  | 55% |
| Bekoev vs. Petroski | 35% | 20% | 9% |  |  | 36% |
| Sezinando vs. Berggren | 36% | 20% | 9% |  |  | 34% |
| Erosa vs. Lee | 25% | 16% | 8% |  |  | 51% |
| Klein vs. Kropschot | 37% | 20% | 9% |  |  | 33% |
| Alencar vs. Rodriguez | 9% | 7% | 4% |  |  | 81% |
| Szabová vs. Lisboa | 19% | 13% | 7% |  |  | 60% |

## How the 2026 predictions have done

| Predictor | Fights | Log loss | Brier | Winners |
|---|---|---|---|---|
| Final prediction | 449 | 0.6208 | 0.216 | 63.9% |
| Model alone (before the market) | 449 | 0.6372 | 0.223 | 62.4% |
| Glicko-2 rating alone | 449 | 0.6818 | 0.244 | 57.5% |
| Final, on fights with a price | 114 | 0.5091 | 0.169 | 76.3% |
| Market price when predicted | 114 | 0.5216 | 0.172 | 75.4% |
| Coin flip | 449 | 0.6931 | 0.250 | – |

Log loss scores the win chances (lower is better; a coin flip scores 0.693, and the betting market about 0.61). Brier is the squared error of the win chance. Picking every betting favorite already gets about two thirds of winners right, so the win rate says little on its own.

- Winner and method (six outcomes): log loss 1.585 on 448 fights, against 1.792 for guessing uniformly. The single most likely result happened 33% of the time.
- Went the distance: predicted 48% on average, actual 41%.

449 of these fights happened before the predictor went live. They are backfilled walk-forward (each fight predicted from earlier fights only, with models fitted on earlier years) using the odds dataset's approximate closing prices, which run only through March 2026, so later backfilled fights use the model alone. Every fight since is graded on the prediction logged before it started.

### Edge record

Every edge logged with a live prediction (the last one before the fight), at the stake and price logged with it; edges logged before edges were priced from the final prediction are left out. Pushes return the stake (a no contest voids every bet; a draw refunds the moneyline). Units are 1% of the bankroll; ROI is units won per unit staked, and expected ROI is what the edges' EVs promised.

| Market | Edges | Record (W-L-P) | Staked | Units won | ROI | Expected ROI |
|---|---|---|---|---|---|---|
| Moneyline | 0 | 0-0-0 | 0.0 | +0.00 | – | – |
| Round total | 0 | 0-0-0 | 0.0 | +0.00 | – | – |
| Method of victory | 0 | 0-0-0 | 0.0 | +0.00 | – | – |

### Latest results: UFC Fight Night: Buckley vs. Malott

| Bout | Predicted | Result | Chance given to the winner | Chance given to the exact result |
|---|---|---|---|---|
| Joaquin Buckley vs. Mike Malott | Buckley 50% | Mike Malott by KO/TKO, R2 | 50% | 24% |
| Erin Blanchfield vs. Jasmine Jasudavicius | Blanchfield 77% | Jasmine Jasudavicius by decision | 23% | 18% |
| Kyle Nelson vs. Cristian Perez | Perez 53% | Cristian Perez by KO/TKO, R1 | 53% | 19% |
| Marc-Andre Barriault vs. Kyle Daukaus | Daukaus 64% | Marc-Andre Barriault by KO/TKO, R1 | 36% | 20% |
| Louis Jourdain vs. Timmy Cuamba | Cuamba 59% | Timmy Cuamba by submission, R2 | 59% | 9% |
| Mandel Nallo vs. Nate Landwehr | Landwehr 60% | Mandel Nallo by KO/TKO, R2 | 40% | 25% |
| Tanner Boser vs. Jhonata Diniz | Boser 54% | Tanner Boser by KO/TKO, R3 | 54% | 30% |
| Julien Leblanc vs. Nick Galanti | Galanti 65% | Nick Galanti by submission, R1 | 65% | 23% |
| Javad Mahjoub vs. Joel Faglier | Faglier 63% | Joel Faglier by KO/TKO, R2 | 63% | 32% |
| Katlyn Cerminara vs. Mackenzie Stiller | Stiller 57% | Katlyn Cerminara by KO/TKO, R1 | 43% | 6% |
| Chad Anheliger vs. Steven Koslow | Koslow 68% | Steven Koslow by submission, R3 | 68% | 22% |
| Melissa Croden vs. Chelsea Chandler | Croden 73% | Chelsea Chandler by submission, R1 | 27% | 3% |
| Cody Chovancek vs. SuYoung You | You 64% | SuYoung You by submission, R3 | 64% | 10% |

## Top fighters by division

Glicko-2 rating from UFC results, with finishes counting as clearer wins than decisions. ± is two rating deviations (fighters with few or old fights are less certain), and the ranking uses the rating minus that margin so an unproven fighter does not top a division on one big win. Active fighters only (a fight in the last two years).

| Division | # | Fighter | Rating | ± | UFC record | Last fight |
|---|---|---|---|---|---|---|
| Flyweight | 1 | Manel Kape | 1978 | 283 | 8-3 | 2026-06-20 |
|  | 2 | Joshua Van | 1942 | 260 | 11-1 | 2026-09-19 |
|  | 3 | Brandon Moreno | 1895 | 237 | 12-7-2 | 2026-09-12 |
|  | 4 | Alexandre Pantoja | 1894 | 237 | 14-5 | 2026-09-19 |
|  | 5 | Tatsuro Taira | 1963 | 318 | 8-2 | 2026-05-09 |
| Bantamweight | 1 | Merab Dvalishvili | 2150 | 235 | 14-3 | 2025-12-06 |
|  | 2 | Petr Yan | 2123 | 239 | 12-4 | 2025-12-06 |
|  | 3 | Song Yadong | 2064 | 224 | 13-4-1 | 2026-08-29 |
|  | 4 | Cory Sandhagen | 2059 | 231 | 11-6 | 2026-07-11 |
|  | 5 | Sean O'Malley | 2059 | 243 | 12-3 | 2026-06-14 |
| Featherweight | 1 | Alexander Volkanovski | 2192 | 234 | 15-3 | 2026-01-31 |
|  | 2 | Diego Lopes | 2145 | 267 | 7-3 | 2026-06-14 |
|  | 3 | Aljamain Sterling | 2097 | 228 | 18-5 | 2026-04-25 |
|  | 4 | Brian Ortega | 2062 | 272 | 8-5 | 2025-08-23 |
|  | 5 | Jean Silva | 2075 | 301 | 7-1 | 2026-09-12 |
| Lightweight | 1 | Ilia Topuria | 2274 | 296 | 9-1 | 2026-06-14 |
|  | 2 | Justin Gaethje | 2193 | 239 | 11-5 | 2026-06-14 |
|  | 3 | Charles Oliveira | 2146 | 211 | 25-11 | 2026-03-07 |
|  | 4 | Arman Tsarukyan | 2148 | 267 | 11-2 | 2026-09-19 |
|  | 5 | Dustin Poirier | 2096 | 229 | 22-9 | 2025-07-19 |
| Welterweight | 1 | Islam Makhachev | 2278 | 233 | 18-1 | 2026-08-15 |
|  | 2 | Shavkat Rakhmonov | 2401 | 407 | 7-0 | 2024-12-07 |
|  | 3 | Max Holloway | 2190 | 211 | 24-9 | 2026-07-11 |
|  | 4 | Carlos Prates | 2236 | 282 | 7-1 | 2026-05-02 |
|  | 5 | Michael Morales | 2245 | 322 | 7-0 | 2025-11-15 |
| Middleweight | 1 | Dricus Du Plessis | 2231 | 253 | 10-1 | 2026-07-18 |
|  | 2 | Khamzat Chimaev | 2255 | 277 | 9-1 | 2026-05-09 |
|  | 3 | Kamaru Usman | 2181 | 240 | 16-4 | 2026-07-18 |
|  | 4 | Nassourdine Imavov | 2173 | 277 | 9-2 | 2025-09-06 |
|  | 5 | Brendan Allen | 2123 | 228 | 16-4 | 2026-10-10 |
| Light Heavyweight | 1 | Magomed Ankalaev | 2188 | 241 | 13-2-1 | 2026-07-25 |
|  | 2 | Robert Whittaker | 2156 | 230 | 18-7 | 2026-07-11 |
|  | 3 | Carlos Ulberg | 2126 | 273 | 10-1 | 2026-04-11 |
|  | 4 | Jiri Prochazka | 2174 | 329 | 6-3 | 2026-04-11 |
|  | 5 | Paulo Costa | 2107 | 268 | 8-4 | 2026-04-11 |
| Heavyweight | 1 | Jon Jones | 2438 | 281 | 22-1 | 2024-11-16 |
|  | 2 | Ciryl Gane | 2336 | 272 | 11-2 | 2026-06-14 |
|  | 3 | Stipe Miocic | 2319 | 278 | 14-5 | 2024-11-16 |
|  | 4 | Alex Pereira | 2268 | 254 | 10-3 | 2026-06-14 |
|  | 5 | Alexander Volkov | 2221 | 237 | 14-5 | 2026-05-09 |
| Women's Strawweight | 1 | Tatiana Suarez | 2011 | 315 | 9-1 | 2026-04-11 |
|  | 2 | Virna Jandiroba | 1841 | 252 | 9-4 | 2026-04-04 |
|  | 3 | Mackenzie Dern | 1797 | 230 | 12-5 | 2026-08-15 |
|  | 4 | Gillian Robertson | 1785 | 231 | 14-7 | 2026-08-15 |
|  | 5 | Jessica Andrade | 1753 | 220 | 17-13 | 2025-08-16 |
| Women's Flyweight | 1 | Valentina Shevchenko | 1998 | 255 | 15-3-1 | 2025-11-15 |
|  | 2 | Zhang Weili | 1981 | 257 | 10-3 | 2025-11-15 |
|  | 3 | Erin Blanchfield | 1984 | 285 | 8-2 | 2026-10-17 |
|  | 4 | Natalia Silva | 2007 | 311 | 9-0 | 2026-10-03 |
|  | 5 | Manon Fiorot | 1961 | 288 | 8-2 | 2026-09-12 |
| Women's Bantamweight | 1 | Kayla Harrison | 2075 | 468 | 3-0 | 2025-06-07 |
|  | 2 | Ketlen Vieira | 1773 | 250 | 10-5 | 2026-05-16 |
|  | 3 | Julianna Pena | 1821 | 306 | 8-4 | 2025-06-07 |
|  | 4 | Norma Dumont | 1743 | 259 | 9-4 | 2026-09-26 |
|  | 5 | Luana Santos | 1827 | 352 | 6-1 | 2026-06-20 |

## Current model fit

- Fitted on 5330 fights from 2016–2026.
- Market blend: 81% weight on the de-vigged price, total slope 1.28 (above 1 stretches favorites, correcting the favorite-longshot bias). Without a price: slope 1.02 on the model alone.
- Strongest win-model inputs (log-odds per standard deviation, A minus B): age -0.28, glicko_logit +0.21, strike_matchup +0.18, debut -0.12, age_decline -0.11, sapm -0.09.
