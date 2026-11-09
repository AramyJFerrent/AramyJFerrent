# UFC fight predictions

Updated Mon Nov 09, 2026 06:08 PM ET. Refreshed automatically every day and several times on fight week; each bout's prediction is locked when its part of the card starts and graded once the result is in.

Each bout gets one consistent breakdown: each fighter's chance to win, split into KO/TKO, submission and decision, and the chance it ends in each round. The win chance blends the model with the betting market (about 81% market, the weight that has predicted best on past fights) and corrects the market's habit of underrating heavy favorites. MMA is high-variance: even the most likely single result is usually well under 50%.

The fair odds are the American odds that match the win chance with no bookmaker margin: -200 means risk $200 to win $100, +200 means risk $100 to win $200. A sportsbook only offers value on a fighter when its price beats the fair line.

The three edge columns value every side of each market at its posted price: expected value (EV) is the average profit per $1 staked, from the final prediction: the win chance blended with the moneyline (which corrects the market's habit of underrating heavy favorites), and method and round chances anchored to their own props, moved only by what the blend changes. A side is an edge when its EV is at least 3%; each cell names the best side if one clears that bar, with its stake, a 25% share of the Kelly stake in units of 1% of the bankroll, at most 3 units on one bout; else "no edge". Moneylines and props are never priced near -110, so a missing price is never assumed: without one, the round-total cell shows the model's fair odds at the line closest to even and the method cell each fighter's fair KO/TKO, submission and decision odds. Over 1.5 rounds means the fight passes 2:30 of round 2 (a decision is always over); finishes are assumed spread evenly within a round.

See the backtest (backtest.md) for how these edges did against the dataset's closing prices, next to the model alone, which finds a 3% edge in most fights and lost money on them. Treat these columns as a live test, tracked below, not as betting advice.

## UFC 334: Gane vs. Hokit

Saturday, November 14, 2026 · first bout locks Sat Nov 14, 5:00 PM ET

| Bout | Win chance | Fair odds | Market | Model alone | KO / Sub / Dec | Distance | Most likely result | Moneyline edge | Round total edge | Method edge |
|---|---|---|---|---|---|---|---|---|---|---|
| **Ciryl Gane** vs. **Josh Hokit**<br>HW, title, 5 rds | Gane 69% – 31% Hokit | -225 / +225 | Gane 66% (-225 / +185) | Gane 61% (-160) | Gane 47% / 5% / 17%<br>Hokit 23% / 1% / 6% | 24% | Gane by KO/TKO (47%) | no edge | no edge | no prices yet; fair KO / Sub / Dec<br>Gane +115 / +1865 / +480<br>Hokit +330 / +9785 / +1445 |
| **Kayla Harrison** vs. **Amanda Nunes**<br>W-BW, title, 5 rds | Harrison 67% – 33% Nunes | -205 / +205 | Harrison 63% (-192 / +160) | Harrison 65% (-190) | Harrison 8% / 23% / 35%<br>Nunes 6% / 5% / 22% | 57% | Harrison by decision (35%) | no edge | no edge | no prices yet; fair KO / Sub / Dec<br>Harrison +1115 / +330 / +180<br>Nunes +1475 / +1845 / +365 |
| **Caio Borralho** vs. **Yousri Belgaroui**<br>MW, 3 rds | Borralho 58% – 42% Belgaroui | -135 / +135 | Borralho 60% (-166 / +140) | Borralho 39% (+155) | Borralho 19% / 7% / 32%<br>Belgaroui 22% / 2% / 18% | 49% | Borralho by decision (32%) | no edge | no edge | no prices yet; fair KO / Sub / Dec<br>Borralho +425 / +1320 / +215<br>Belgaroui +355 / +3960 / +460 |
| **Uroš Medić** vs. **Kevin Holland**<br>WW, 3 rds | Medić 56% – 44% Holland | -125 / +125 | Medić 57% (-148 / +124) | Medić 43% (+135) | Medić 36% / 2% / 17%<br>Holland 18% / 8% / 19% | 36% | Medić by KO/TKO (36%) | no edge | no edge | no prices yet; fair KO / Sub / Dec<br>Medić +175 / +4835 / +475<br>Holland +455 / +1215 / +435 |
| **Bilal Hasan** vs. **Luis Gurule**<br>FLW, 3 rds | Hasan 92% – 8% Gurule | -1120 / +1120 | Hasan 88% (-1100 / +700) | Hasan 82% (-445) | Hasan 35% / 17% / 40%<br>Gurule 2% / 1% / 5% | 45% | Hasan by decision (40%) | no edge | no edge | no prices yet; fair KO / Sub / Dec<br>Hasan +185 / +500 / +150<br>Gurule +4830 / +8615 / +1890 |
| **Stephen Thompson** vs. **Charles Radtke**<br>WW, 3 rds | Thompson 55% – 45% Radtke | -120 / +120 | Thompson 58% (-155 / +130) | Thompson 35% (+190) | Thompson 22% / 5% / 27%<br>Radtke 13% / 10% / 22% | 49% | Thompson by decision (27%) | Radtke (+130): EV +4.0%, 45%, stake 0.8u | no edge | no prices yet; fair KO / Sub / Dec<br>Thompson +355 / +1730 / +265<br>Radtke +650 / +885 / +360 |
| **Drew Dober** vs. **Chris Duncan**<br>LW, 3 rds | Dober 37% – 63% Duncan | +170 / -170 | Dober 42% (+130 / -155) | Dober 32% (+210) | Dober 17% / 5% / 15%<br>Duncan 20% / 15% / 28% | 43% | Duncan by decision (28%) | Duncan (-155): EV +3.4%, 63%, stake 1.3u | no edge | no prices yet; fair KO / Sub / Dec<br>Dober +490 / +1850 / +560<br>Duncan +410 / +555 / +255 |
| **Jim Miller** vs. **Terrance McKinney**<br>LW, 3 rds | Miller 28% – 72% McKinney | +255 / -255 | Miller 36% (+170 / -205) | Miller 21% (+365) | Miller 12% / 10% / 7%<br>McKinney 30% / 17% / 25% | 32% | McKinney by KO/TKO (30%) | McKinney (-205): EV +6.6%, 72%, stake 3.0u | no edge | no prices yet; fair KO / Sub / Dec<br>Miller +760 / +925 / +1340<br>McKinney +235 / +490 / +300 |
| **Donte Johnson** vs. **Cesar Almeida**<br>MW, 3 rds | Johnson 69% – 31% Almeida | -225 / +225 | Johnson 61% (-175 / +145) | Johnson 81% (-415) | Johnson 29% / 14% / 26%<br>Almeida 12% / 4% / 15% | 41% | Johnson by KO/TKO (29%) | Johnson (-175): EV +8.4%, 69%, stake 3.0u | no edge | no prices yet; fair KO / Sub / Dec<br>Johnson +245 / +625 / +280<br>Almeida +750 / +2305 / +565 |
| **Jared Gordon** vs. **Melquizael Costa**<br>LW, 3 rds | Gordon 20% – 80% Costa | +410 / -410 | Gordon 24% (+295 / -375) | Gordon 27% (+265) | Gordon 7% / 2% / 11%<br>Costa 30% / 20% / 30% | 41% | Costa by KO/TKO (30%) | no edge | no edge | no prices yet; fair KO / Sub / Dec<br>Gordon +1380 / +4405 / +840<br>Costa +230 / +395 / +235 |
| **Macy Chiasson** vs. **Bia Mesquita**<br>W-BW, 3 rds | Chiasson 27% – 73% Mesquita | +270 / -270 | Chiasson 31% (+205 / -250) | Chiasson 30% (+230) | Chiasson 3% / 4% / 19%<br>Mesquita 5% / 43% / 25% | 44% | Mesquita by submission (43%) | no edge | no edge | no prices yet; fair KO / Sub / Dec<br>Chiasson +2910 / +2170 / +425<br>Mesquita +1870 / +135 / +295 |
| **Adrian Yañez** vs. **Juan Diaz**<br>BW, 3 rds | Yañez 37% – 63% Diaz | +170 / -170 | no line yet | Yañez 37% (+170) | Yañez 14% / 3% / 20%<br>Diaz 11% / 22% / 30% | 50% | Diaz by decision (30%) | no line yet | no price yet; fair Over 2.5 -120, Under +120 | no prices yet; fair KO / Sub / Dec<br>Yañez +590 / +3620 / +410<br>Diaz +815 / +355 / +230 |
| **Evan Elder** vs. **Samuel Sanches**<br>LW, 3 rds, UFC debut: Sanches | Elder 49% – 51% Sanches | +105 / -105 | Elder 48% (+100 / -120) | Elder 54% (-115) | Elder 18% / 7% / 23%<br>Sanches 19% / 10% / 23% | 46% | Sanches by decision (23%) | no edge | no edge | no prices yet; fair KO / Sub / Dec<br>Elder +445 / +1235 / +340<br>Sanches +435 / +950 / +335 |

When it ends (either fighter):

| Bout | Round 1 | Round 2 | Round 3 | Round 4 | Round 5 | Decision |
|---|---|---|---|---|---|---|
| Gane vs. Hokit | 31% | 22% | 13% | 6% | 5% | 24% |
| Harrison vs. Nunes | 14% | 12% | 8% | 5% | 4% | 57% |
| Borralho vs. Belgaroui | 26% | 16% | 8% |  |  | 49% |
| Medić vs. Holland | 35% | 20% | 9% |  |  | 36% |
| Hasan vs. Gurule | 29% | 18% | 9% |  |  | 45% |
| Thompson vs. Radtke | 26% | 17% | 8% |  |  | 49% |
| Dober vs. Duncan | 30% | 18% | 9% |  |  | 43% |
| Miller vs. McKinney | 38% | 21% | 9% |  |  | 32% |
| Johnson vs. Almeida | 31% | 19% | 9% |  |  | 41% |
| Gordon vs. Costa | 32% | 19% | 9% |  |  | 41% |
| Chiasson vs. Mesquita | 29% | 18% | 9% |  |  | 44% |
| Yañez vs. Diaz | 26% | 16% | 8% |  |  | 50% |
| Elder vs. Sanches | 28% | 17% | 9% |  |  | 46% |

## UFC Fight Night: Procházka vs. Stirling

Saturday, November 21, 2026 · first bout locks Sat Nov 21, 10:00 AM ET

| Bout | Win chance | Fair odds | Market | Model alone | KO / Sub / Dec | Distance | Most likely result | Moneyline edge | Round total edge | Method edge |
|---|---|---|---|---|---|---|---|---|---|---|
| **Jiří Procházka** vs. **Navajo Stirling**<br>LHW, 5 rds | Procházka 32% – 68% Stirling | +215 / -215 | no line yet | Procházka 32% (+215) | Procházka 21% / 2% / 8%<br>Stirling 51% / 4% / 13% | 21% | Stirling by KO/TKO (51%) | no line yet | no price yet; fair Over 1.5 -125, Under +125 | no prices yet; fair KO / Sub / Dec<br>Procházka +370 / +4340 / +1150<br>Stirling -105 / +2155 / +665 |
| **Aljamain Sterling** vs. **Kevin Vallejos**<br>FW, 3 rds | Sterling 43% – 57% Vallejos | +130 / -130 | no line yet | Sterling 43% (+130) | Sterling 7% / 5% / 32%<br>Vallejos 25% / 3% / 29% | 61% | Sterling by decision (32%) | no line yet | no price yet; fair Over 2.5 -180, Under +180 | no prices yet; fair KO / Sub / Dec<br>Sterling +1380 / +2050 / +215<br>Vallejos +305 / +3155 / +245 |
| **Dan Hooker** vs. **Brian Ortega**<br>LW, 3 rds | Hooker 46% – 54% Ortega | +115 / -115 | no line yet | Hooker 46% (+115) | Hooker 20% / 7% / 20%<br>Ortega 20% / 14% / 20% | 40% | Ortega by KO/TKO (20%) | no line yet | no price yet; fair Over 2.5 +125, Under -125 | no prices yet; fair KO / Sub / Dec<br>Hooker +410 / +1430 / +400<br>Ortega +395 / +610 / +415 |
| **Kyoji Horiguchi** vs. **Asu Almabayev**<br>FLW, 3 rds | Horiguchi 43% – 57% Almabayev | +135 / -135 | no line yet | Horiguchi 43% (+135) | Horiguchi 9% / 8% / 26%<br>Almabayev 7% / 24% / 27% | 53% | Almabayev by decision (27%) | no line yet | no price yet; fair Over 2.5 -130, Under +130 | no prices yet; fair KO / Sub / Dec<br>Horiguchi +1065 / +1200 / +280<br>Almabayev +1305 / +325 / +275 |
| **Jared Cannonier** vs. **Ikram Aliskerov**<br>MW, 3 rds | Cannonier 21% – 79% Aliskerov | +375 / -375 | no line yet | Cannonier 21% (+375) | Cannonier 9% / 2% / 10%<br>Aliskerov 32% / 9% / 38% | 48% | Aliskerov by decision (38%) | no line yet | no price yet; fair Over 2.5 -110, Under +110 | no prices yet; fair KO / Sub / Dec<br>Cannonier +1050 / +4960 / +870<br>Aliskerov +210 / +1075 / +160 |
| **Aleksandre Topuria** vs. **Santiago Luna**<br>BW, 3 rds | Topuria 39% – 61% Luna | +155 / -155 | no line yet | Topuria 39% (+155) | Topuria 8% / 7% / 25%<br>Luna 16% / 8% / 37% | 61% | Luna by decision (37%) | no line yet | no price yet; fair Over 2.5 -185, Under +185 | no prices yet; fair KO / Sub / Dec<br>Topuria +1130 / +1415 / +305<br>Luna +530 / +1120 / +175 |
| **Shamil Gaziev** vs. **Tallison Teixeira**<br>HW, 3 rds | Gaziev 29% – 71% Teixeira | +240 / -240 | no line yet | Gaziev 29% (+240) | Gaziev 19% / 2% / 8%<br>Teixeira 43% / 7% / 21% | 29% | Teixeira by KO/TKO (43%) | no line yet | no price yet; fair Over 1.5 +105, Under -105 | no prices yet; fair KO / Sub / Dec<br>Gaziev +415 / +4270 / +1210<br>Teixeira +130 / +1425 / +380 |
| **Amir Albazi** vs. **Alessandro Costa**<br>FLW, 3 rds | Albazi 48% – 52% Costa | +105 / -105 | no line yet | Albazi 48% (+105) | Albazi 11% / 9% / 28%<br>Costa 15% / 12% / 25% | 53% | Albazi by decision (28%) | no line yet | no price yet; fair Over 2.5 -130, Under +130 | no prices yet; fair KO / Sub / Dec<br>Albazi +780 / +970 / +260<br>Costa +570 / +755 / +300 |
| **Jake Matthews** vs. **Tahir Abdullayev**<br>WW, 3 rds | Matthews 56% – 44% Abdullayev | -130 / +130 | no line yet | Matthews 56% (-130) | Matthews 17% / 9% / 30%<br>Abdullayev 13% / 8% / 23% | 53% | Matthews by decision (30%) | no line yet | no price yet; fair Over 2.5 -130, Under +130 | no prices yet; fair KO / Sub / Dec<br>Matthews +485 / +965 / +235<br>Abdullayev +685 / +1145 / +335 |

When it ends (either fighter):

| Bout | Round 1 | Round 2 | Round 3 | Round 4 | Round 5 | Decision |
|---|---|---|---|---|---|---|
| Procházka vs. Stirling | 33% | 22% | 13% | 6% | 5% | 21% |
| Sterling vs. Vallejos | 19% | 13% | 7% |  |  | 61% |
| Hooker vs. Ortega | 32% | 19% | 9% |  |  | 40% |
| Horiguchi vs. Almabayev | 24% | 15% | 8% |  |  | 53% |
| Cannonier vs. Aliskerov | 27% | 17% | 8% |  |  | 48% |
| Topuria vs. Luna | 19% | 13% | 7% |  |  | 61% |
| Gaziev vs. Teixeira | 41% | 21% | 9% |  |  | 29% |
| Albazi vs. Costa | 24% | 15% | 8% |  |  | 53% |
| Matthews vs. Abdullayev | 24% | 15% | 8% |  |  | 53% |

## How the 2026 predictions have done

| Predictor | Fights | Log loss | Brier | Winners |
|---|---|---|---|---|
| Final prediction | 489 | 0.6185 | 0.215 | 64.2% |
| Model alone (before the market) | 489 | 0.6362 | 0.222 | 62.6% |
| Glicko-2 rating alone | 489 | 0.6814 | 0.244 | 57.9% |
| Final, on fights with a price | 154 | 0.5306 | 0.178 | 74.0% |
| Market price when predicted | 154 | 0.5415 | 0.181 | 74.7% |
| Coin flip | 489 | 0.6931 | 0.250 | – |

Log loss scores the win chances (lower is better; a coin flip scores 0.693, and the betting market about 0.61). Brier is the squared error of the win chance. Picking every betting favorite already gets about two thirds of winners right, so the win rate says little on its own.

- Winner and method (six outcomes): log loss 1.576 on 488 fights, against 1.792 for guessing uniformly. The single most likely result happened 34% of the time.
- Went the distance: predicted 48% on average, actual 42%.

449 of these fights happened before the predictor went live. They are backfilled walk-forward (each fight predicted from earlier fights only, with models fitted on earlier years) using the odds dataset's approximate closing prices, which run only through March 2026, so later backfilled fights use the model alone. Every fight since is graded on the prediction logged before it started.

### Edge record

Every edge logged with a live prediction (the last one before the fight), at the stake and price logged with it; edges logged before edges were priced from the final prediction are left out. Pushes return the stake (a no contest voids every bet; a draw refunds the moneyline). Units are 1% of the bankroll; ROI is units won per unit staked, and expected ROI is what the edges' EVs promised.

| Market | Edges | Record (W-L-P) | Staked | Units won | ROI | Expected ROI |
|---|---|---|---|---|---|---|
| Moneyline | 5 | 3-2-0 | 11.9 | -0.54 | -4.6% | +5.0% |
| Round total | 0 | 0-0-0 | 0.0 | +0.00 | – | – |
| Method of victory | 0 | 0-0-0 | 0.0 | +0.00 | – | – |

### Latest results: UFC Fight Night: Cortes Acosta vs. Walker

| Bout | Predicted | Result | Chance given to the winner | Chance given to the exact result |
|---|---|---|---|---|
| Waldo Cortes Acosta vs. Johnny Walker | Acosta 69% | Johnny Walker by KO/TKO, R3 | 31% | 20% |
| Tatiana Suarez vs. Virna Jandiroba | Suarez 67% | Tatiana Suarez by decision | 67% | 47% |
| Davey Grant vs. Elijah Smith | Smith 81% | Elijah Smith by KO/TKO, R1 | 81% | 21% |
| Billy Elekana vs. Lucas Fernando | Fernando 76% | Lucas Fernando by decision | 76% | 20% |
| Priscila Cachoeira vs. Nina Milošević | Milošević 87% | Nina Milošević by KO/TKO, R2 | 87% | 30% |
| Mitch Raposo vs. Marcos Degli | Degli 67% | Mitch Raposo by decision | 33% | 20% |
| Keiichiro Nakamura vs. Ollie Schmid | Nakamura 78% | Ollie Schmid by decision | 22% | 12% |
| Gabriel Lorenço vs. Thomas Petersen | Petersen 63% | Thomas Petersen by KO/TKO, R3 | 63% | 27% |
| Karine Silva vs. Gabriella Fernandes | Silva 71% | Karine Silva by decision | 71% | 40% |
| Jose Delano vs. Murtazali Magomedov | Delano 52% | Murtazali Magomedov by decision | 48% | 21% |
| Austin Bashi vs. Carlos Calderon | Bashi 86% | Austin Bashi by submission, R1 | 86% | 26% |
| Mantas Kondratavičius vs. Andre Petroski | Kondratavičius 78% | Andre Petroski by KO/TKO, R2 | 22% | 6% |
| Seokhyeon Ko vs. Wellington Turman | Ko 88% | Seokhyeon Ko by decision | 88% | 45% |
| Jonny Parsons vs. José Souza | Souza 68% | José Souza by KO/TKO, R1 | 68% | 23% |

## Top fighters by division

Glicko-2 rating from UFC results, with finishes counting as clearer wins than decisions. ± is two rating deviations (fighters with few or old fights are less certain), and the ranking uses the rating minus that margin so an unproven fighter does not top a division on one big win. Active fighters only (a fight in the last two years).

| Division | # | Fighter | Rating | ± | UFC record | Last fight |
|---|---|---|---|---|---|---|
| Flyweight | 1 | Manel Kape | 1978 | 284 | 8-3 | 2026-06-20 |
|  | 2 | Joshua Van | 1942 | 261 | 11-1 | 2026-09-19 |
|  | 3 | Brandon Moreno | 1895 | 237 | 12-7-2 | 2026-09-12 |
|  | 4 | Alexandre Pantoja | 1894 | 237 | 14-5 | 2026-09-19 |
|  | 5 | Tatsuro Taira | 1963 | 318 | 8-2 | 2026-05-09 |
| Bantamweight | 1 | Petr Yan | 2147 | 228 | 13-4 | 2026-10-24 |
|  | 2 | Merab Dvalishvili | 2128 | 225 | 14-4 | 2026-10-24 |
|  | 3 | Song Yadong | 2064 | 225 | 13-4-1 | 2026-08-29 |
|  | 4 | Cory Sandhagen | 2059 | 232 | 11-6 | 2026-07-11 |
|  | 5 | Sean O'Malley | 2059 | 244 | 12-3 | 2026-06-14 |
| Featherweight | 1 | Alexander Volkanovski | 2214 | 226 | 16-3 | 2026-10-24 |
|  | 2 | Diego Lopes | 2145 | 267 | 7-3 | 2026-06-14 |
|  | 3 | Aljamain Sterling | 2097 | 229 | 18-5 | 2026-04-25 |
|  | 4 | Brian Ortega | 2062 | 272 | 8-5 | 2025-08-23 |
|  | 5 | Jean Silva | 2075 | 301 | 7-1 | 2026-09-12 |
| Lightweight | 1 | Ilia Topuria | 2274 | 297 | 9-1 | 2026-06-14 |
|  | 2 | Justin Gaethje | 2193 | 240 | 11-5 | 2026-06-14 |
|  | 3 | Charles Oliveira | 2146 | 212 | 25-11 | 2026-03-07 |
|  | 4 | Arman Tsarukyan | 2148 | 267 | 11-2 | 2026-09-19 |
|  | 5 | Dustin Poirier | 2096 | 230 | 22-9 | 2025-07-19 |
| Welterweight | 1 | Islam Makhachev | 2278 | 233 | 18-1 | 2026-08-15 |
|  | 2 | Shavkat Rakhmonov | 2401 | 408 | 7-0 | 2024-12-07 |
|  | 3 | Max Holloway | 2190 | 211 | 24-9 | 2026-07-11 |
|  | 4 | Carlos Prates | 2236 | 282 | 7-1 | 2026-05-02 |
|  | 5 | Michael Morales | 2245 | 323 | 7-0 | 2025-11-15 |
| Middleweight | 1 | Dricus Du Plessis | 2231 | 253 | 10-1 | 2026-07-18 |
|  | 2 | Khamzat Chimaev | 2255 | 278 | 9-1 | 2026-05-09 |
|  | 3 | Kamaru Usman | 2181 | 240 | 16-4 | 2026-07-18 |
|  | 4 | Nassourdine Imavov | 2173 | 277 | 9-2 | 2025-09-06 |
|  | 5 | Brendan Allen | 2123 | 229 | 16-4 | 2026-10-10 |
| Light Heavyweight | 1 | Magomed Ankalaev | 2188 | 242 | 13-2-1 | 2026-07-25 |
|  | 2 | Robert Whittaker | 2156 | 230 | 18-7 | 2026-07-11 |
|  | 3 | Carlos Ulberg | 2126 | 273 | 10-1 | 2026-04-11 |
|  | 4 | Jiri Prochazka | 2174 | 329 | 6-3 | 2026-04-11 |
|  | 5 | Paulo Costa | 2107 | 268 | 8-4 | 2026-04-11 |
| Heavyweight | 1 | Jon Jones | 2438 | 281 | 22-1 | 2024-11-16 |
|  | 2 | Ciryl Gane | 2336 | 272 | 11-2 | 2026-06-14 |
|  | 3 | Stipe Miocic | 2319 | 278 | 14-5 | 2024-11-16 |
|  | 4 | Alexander Volkov | 2247 | 231 | 15-5 | 2026-10-24 |
|  | 5 | Alex Pereira | 2268 | 255 | 10-3 | 2026-06-14 |
| Women's Strawweight | 1 | Tatiana Suarez | 2021 | 295 | 10-1 | 2026-11-07 |
|  | 2 | Virna Jandiroba | 1834 | 242 | 9-5 | 2026-11-07 |
|  | 3 | Mackenzie Dern | 1797 | 230 | 12-5 | 2026-08-15 |
|  | 4 | Gillian Robertson | 1785 | 232 | 14-7 | 2026-08-15 |
|  | 5 | Jessica Andrade | 1753 | 221 | 17-13 | 2025-08-16 |
| Women's Flyweight | 1 | Valentina Shevchenko | 1998 | 255 | 15-3-1 | 2025-11-15 |
|  | 2 | Zhang Weili | 1981 | 258 | 10-3 | 2025-11-15 |
|  | 3 | Erin Blanchfield | 1984 | 285 | 8-2 | 2026-10-17 |
|  | 4 | Natalia Silva | 2007 | 311 | 9-0 | 2026-10-03 |
|  | 5 | Manon Fiorot | 1961 | 288 | 8-2 | 2026-09-12 |
| Women's Bantamweight | 1 | Kayla Harrison | 2075 | 468 | 3-0 | 2025-06-07 |
|  | 2 | Luana Santos | 1846 | 323 | 7-1 | 2026-10-31 |
|  | 3 | Ketlen Vieira | 1773 | 250 | 10-5 | 2026-05-16 |
|  | 4 | Julianna Pena | 1821 | 307 | 8-4 | 2025-06-07 |
|  | 5 | Norma Dumont | 1743 | 260 | 9-4 | 2026-09-26 |

## Current model fit

- Fitted on 5370 fights from 2016–2026.
- Market blend: 81% weight on the de-vigged price, total slope 1.28 (above 1 stretches favorites, correcting the favorite-longshot bias). Without a price: slope 1.02 on the model alone.
- Strongest win-model inputs (log-odds per standard deviation, A minus B): age -0.28, glicko_logit +0.21, strike_matchup +0.18, debut -0.13, age_decline -0.11, sapm -0.09.
