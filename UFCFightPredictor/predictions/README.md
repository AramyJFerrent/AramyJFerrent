# UFC fight predictions

Updated Mon Oct 19, 2026 05:10 AM ET. Refreshed automatically every day and several times on fight week; each bout's prediction is locked when its part of the card starts and graded once the result is in.

Each bout gets one consistent breakdown: each fighter's chance to win, split into KO/TKO, submission and decision, and the chance it ends in each round. The win chance blends the model with the betting market (about 81% market, the weight that has predicted best on past fights) and corrects the market's habit of underrating heavy favorites. MMA is high-variance: even the most likely single result is usually well under 50%.

The fair odds are the American odds that match the win chance with no bookmaker margin: -200 means risk $200 to win $100, +200 means risk $100 to win $200. A sportsbook only offers value on a fighter when its price beats the fair line.

Value vs. price flags a fighter whose price implies a chance at least 2 points below the final win chance, bookmaker margin included. In the walk-forward backtest these bets made money, mostly by backing favorites the market underrates (see backtest.md), but on approximate closing prices; treat it as an experiment, tracked live below.

## UFC 333: Volkanovski vs. Evloev

Saturday, October 24, 2026 · first bout locks Sat Oct 24, 10:00 AM ET

| Bout | Win chance | Fair odds | Market | Model alone | KO / Sub / Dec | Distance | Most likely result | Value vs. price |
|---|---|---|---|---|---|---|---|---|
| **Alexander Volkanovski** vs. **Movsar Evloev**<br>FW, title, 5 rds | Volkanovski 49% – 51% Evloev | +105 / -105 | Volkanovski 50% (-110 / -110) | Volkanovski 44% | Volkanovski 16% / 5% / 28%<br>Evloev 13% / 6% / 33% | 60% | Evloev by decision (33%) | none |
| **Petr Yan** vs. **Merab Dvalishvili**<br>BW, title, 5 rds | Yan 60% – 40% Dvalishvili | -150 / +150 | Yan 59% (-162 / +136) | Yan 51% | Yan 16% / 5% / 38%<br>Dvalishvili 6% / 6% / 29% | 67% | Yan by decision (38%) | none |
| **Lone'er Kavanagh** vs. **Ramazan Temirov**<br>FLW, 3 rds | Kavanagh 49% – 51% Temirov | +105 / -105 | Kavanagh 50% (-112 / -108) | Kavanagh 43% | Kavanagh 10% / 6% / 32%<br>Temirov 24% / 4% / 22% | 55% | Kavanagh by decision (32%) | none |
| **Alexander Volkov** vs. **Rizvan Kuniev**<br>HW, 3 rds | Volkov 51% – 49% Kuniev | -100 / +100 | Volkov 52% (-118 / -102) | Volkov 45% | Volkov 22% / 3% / 25%<br>Kuniev 24% / 3% / 22% | 47% | Volkov by decision (25%) | none |
| **Aaron Pico** vs. **Losene Keita**<br>FW, 3 rds | Pico 48% – 52% Keita | +110 / -110 | Pico 51% (-115 / -105) | Pico 37% | Pico 10% / 5% / 33%<br>Keita 26% / 4% / 22% | 55% | Pico by decision (33%) | none |
| **Azamat Murzakanov** vs. **Dominick Reyes**<br>LHW, 3 rds | Murzakanov 64% – 36% Reyes | -175 / +175 | Murzakanov 65% (-205 / +180) | Murzakanov 40% | Murzakanov 42% / 5% / 16%<br>Reyes 22% / 2% / 12% | 28% | Murzakanov by KO/TKO (42%) | none |
| **Nikita Krylov** vs. **Abdul-Rakhman Yakhyaev**<br>LHW, 3 rds | Krylov 19% – 81% Yakhyaev | +435 / -435 | Krylov 22% (+340 / -440) | Krylov 35% | Krylov 8% / 3% / 8%<br>Yakhyaev 46% / 25% / 10% | 18% | Yakhyaev by KO/TKO (46%) | none |
| **Abus Magomedov** vs. **Cam Rowston**<br>MW, 3 rds | Magomedov 48% – 52% Rowston | +105 / -105 | Magomedov 53% (-122 / +102) | Magomedov 32% | Magomedov 13% / 12% / 23%<br>Rowston 23% / 6% / 23% | 46% | Magomedov by decision (23%) | Rowston +102 (2 pts) |
| **Grant Dawson** vs. **Nurullo Aliev**<br>LW, 3 rds | Dawson 51% – 49% Aliev | -105 / +105 | Dawson 52% (-120 / +100) | Dawson 44% | Dawson 9% / 17% / 25%<br>Aliev 11% / 8% / 31% | 56% | Aliev by decision (31%) | none |
| **Colby Thicknesse** vs. **Asaf Chopurov**<br>BW, 3 rds, UFC debut: Chopurov | Thicknesse 63% – 37% Chopurov | -170 / +170 | no line yet | Thicknesse 63% | Thicknesse 17% / 15% / 31%<br>Chopurov 9% / 6% / 22% | 54% | Thicknesse by decision (31%) | – |
| **Abubakar Vagaev** vs. **Jacob Malkoun**<br>MW, 3 rds | Vagaev 38% – 62% Malkoun | +165 / -165 | no line yet | Vagaev 38% | Vagaev 9% / 6% / 23%<br>Malkoun 18% / 11% / 32% | 55% | Malkoun by decision (32%) | – |

When it ends (either fighter):

| Bout | Round 1 | Round 2 | Round 3 | Round 4 | Round 5 | Decision |
|---|---|---|---|---|---|---|
| Volkanovski vs. Evloev | 13% | 11% | 8% | 4% | 4% | 60% |
| Yan vs. Dvalishvili | 10% | 9% | 7% | 4% | 3% | 67% |
| Kavanagh vs. Temirov | 23% | 15% | 8% |  |  | 55% |
| Volkov vs. Kuniev | 28% | 17% | 8% |  |  | 47% |
| Pico vs. Keita | 22% | 15% | 8% |  |  | 55% |
| Murzakanov vs. Reyes | 41% | 21% | 9% |  |  | 28% |
| Krylov vs. Yakhyaev | 51% | 23% | 9% |  |  | 18% |
| Magomedov vs. Rowston | 28% | 17% | 9% |  |  | 46% |
| Dawson vs. Aliev | 22% | 14% | 7% |  |  | 56% |
| Thicknesse vs. Chopurov | 23% | 15% | 8% |  |  | 54% |
| Vagaev vs. Malkoun | 22% | 15% | 8% |  |  | 55% |

## UFC Fight Night: Moicano vs. Nolan

Saturday, October 31, 2026 · first bout locks Sat Oct 31, 5:00 PM ET

| Bout | Win chance | Fair odds | Market | Model alone | KO / Sub / Dec | Distance | Most likely result | Value vs. price |
|---|---|---|---|---|---|---|---|---|
| **Renato Moicano** vs. **Tom Nolan**<br>LW, 5 rds | Moicano 40% – 60% Nolan | +150 / -150 | no line yet | Moicano 40% | Moicano 16% / 10% / 14%<br>Nolan 25% / 15% / 20% | 35% | Nolan by KO/TKO (25%) | – |
| **Randy Brown** vs. **Carlos Leal**<br>WW, 3 rds | Brown 51% – 49% Leal | -100 / +100 | no line yet | Brown 51% | Brown 22% / 5% / 24%<br>Leal 21% / 3% / 25% | 49% | Leal by decision (25%) | – |
| **Yana Santos** vs. **Luana Santos**<br>W-BW, 3 rds | Santos 20% – 80% Santos | +410 / -410 | no line yet | Santos 20% | Santos 2% / 1% / 16%<br>Santos 9% / 19% / 52% | 68% | Santos by decision (52%) | – |
| **Jean-Paul Lebosnoyani** vs. **Farman Hasanov**<br>WW, 3 rds | Lebosnoyani 62% – 38% Hasanov | -165 / +165 | no line yet | Lebosnoyani 62% | Lebosnoyani 15% / 13% / 34%<br>Hasanov 5% / 7% / 26% | 60% | Lebosnoyani by decision (34%) | – |
| **Francis Marshall** vs. **Gaston Bolaños**<br>FW, 3 rds | Marshall 71% – 29% Bolaños | -240 / +240 | no line yet | Marshall 71% | Marshall 19% / 17% / 34%<br>Bolaños 7% / 2% / 21% | 55% | Marshall by decision (34%) | – |
| **Azamat Bekoev** vs. **Andre Petroski**<br>MW, 3 rds | Bekoev 41% – 59% Petroski | +145 / -145 | no line yet | Bekoev 41% | Bekoev 20% / 5% / 16%<br>Petroski 19% / 20% / 20% | 36% | Petroski by decision (20%) | – |
| **Rodrigo Sezinando** vs. **Theodor Berggren**<br>WW, 3 rds | Sezinando 41% – 59% Berggren | +145 / -145 | no line yet | Sezinando 41% | Sezinando 22% / 6% / 13%<br>Berggren 30% / 8% / 21% | 34% | Berggren by KO/TKO (30%) | – |
| **Julian Erosa** vs. **JeongYeong Lee**<br>FW, 3 rds | Erosa 49% – 51% Lee | +105 / -105 | no line yet | Erosa 49% | Erosa 16% / 7% / 26%<br>Lee 21% / 5% / 25% | 51% | Erosa by decision (26%) | – |
| **Nick Klein** vs. **Joe Kropschot**<br>MW, 3 rds, UFC debut: Kropschot | Klein 46% – 54% Kropschot | +115 / -115 | no line yet | Klein 46% | Klein 13% / 15% / 18%<br>Kropschot 26% / 12% / 16% | 33% | Kropschot by KO/TKO (26%) | – |
| **Talita Alencar** vs. **Piera Rodriguez**<br>W-SW, 3 rds | Alencar 42% – 58% Rodriguez | +135 / -135 | no line yet | Alencar 42% | Alencar 3% / 7% / 32%<br>Rodriguez 5% / 4% / 49% | 81% | Rodriguez by decision (49%) | – |
| **Lucia Szabová** vs. **Tainara Lisboa**<br>W-FLW, 3 rds, UFC debut: Szabová | Szabová 67% – 33% Lisboa | -205 / +205 | no line yet | Szabová 67% | Szabová 11% / 18% / 38%<br>Lisboa 4% / 7% / 23% | 60% | Szabová by decision (38%) | – |

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
- Value-vs-price sides: 10-4, -0.3 units at one unit a bet.

449 of these fights happened before the predictor went live. They are backfilled walk-forward (each fight predicted from earlier fights only, with models fitted on earlier years) using the odds dataset's approximate closing prices, which run only through March 2026, so later backfilled fights use the model alone. Every fight since is graded on the prediction logged before it started.

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
|  | 3 | Brandon Moreno | 1895 | 236 | 12-7-2 | 2026-09-12 |
|  | 4 | Alexandre Pantoja | 1894 | 237 | 14-5 | 2026-09-19 |
|  | 5 | Tatsuro Taira | 1963 | 317 | 8-2 | 2026-05-09 |
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
|  | 3 | Max Holloway | 2190 | 210 | 24-9 | 2026-07-11 |
|  | 4 | Carlos Prates | 2236 | 282 | 7-1 | 2026-05-02 |
|  | 5 | Michael Morales | 2245 | 322 | 7-0 | 2025-11-15 |
| Middleweight | 1 | Dricus Du Plessis | 2231 | 253 | 10-1 | 2026-07-18 |
|  | 2 | Khamzat Chimaev | 2255 | 277 | 9-1 | 2026-05-09 |
|  | 3 | Kamaru Usman | 2181 | 239 | 16-4 | 2026-07-18 |
|  | 4 | Nassourdine Imavov | 2173 | 276 | 9-2 | 2025-09-06 |
|  | 5 | Brendan Allen | 2123 | 228 | 16-4 | 2026-10-10 |
| Light Heavyweight | 1 | Magomed Ankalaev | 2188 | 241 | 13-2-1 | 2026-07-25 |
|  | 2 | Robert Whittaker | 2156 | 230 | 18-7 | 2026-07-11 |
|  | 3 | Carlos Ulberg | 2126 | 272 | 10-1 | 2026-04-11 |
|  | 4 | Jiri Prochazka | 2174 | 329 | 6-3 | 2026-04-11 |
|  | 5 | Paulo Costa | 2107 | 267 | 8-4 | 2026-04-11 |
| Heavyweight | 1 | Jon Jones | 2438 | 281 | 22-1 | 2024-11-16 |
|  | 2 | Ciryl Gane | 2336 | 272 | 11-2 | 2026-06-14 |
|  | 3 | Stipe Miocic | 2319 | 277 | 14-5 | 2024-11-16 |
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
