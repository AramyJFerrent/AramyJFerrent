# UFC fight predictions

Updated Sat Nov 14, 2026 01:51 PM ET. Refreshed automatically every day and several times on fight week; each bout's prediction is locked when its part of the card starts and graded once the result is in.

Each bout gets one consistent breakdown: each fighter's chance to win, split into KO/TKO, submission and decision, and the chance it ends in each round. The win chance blends the model with the betting market (about 81% market, the weight that has predicted best on past fights) and corrects the market's habit of underrating heavy favorites. MMA is high-variance: even the most likely single result is usually well under 50%.

The fair odds are the American odds that match the win chance with no bookmaker margin: -200 means risk $200 to win $100, +200 means risk $100 to win $200. A sportsbook only offers value on a fighter when its price beats the fair line.

The three edge columns value every side of each market at its posted price: expected value (EV) is the average profit per $1 staked, from the final prediction: the win chance blended with the moneyline (which corrects the market's habit of underrating heavy favorites), and method and round chances anchored to their own props, moved only by what the blend changes. A side is an edge when its EV is at least 3%; each cell names the best side if one clears that bar, with its stake, a 25% share of the Kelly stake in units of 1% of the bankroll, at most 3 units on one bout; else "no edge". Moneylines and props are never priced near -110, so a missing price is never assumed: without one, the round-total cell shows the model's fair odds at the line closest to even and the method cell each fighter's fair KO/TKO, submission and decision odds. Over 1.5 rounds means the fight passes 2:30 of round 2 (a decision is always over); finishes are assumed spread evenly within a round.

See the backtest (backtest.md) for how these edges did against the dataset's closing prices, next to the model alone, which finds a 3% edge in most fights and lost money on them. Treat these columns as a live test, tracked below, not as betting advice.

## UFC 334: Gane vs. Hokit

Saturday, November 14, 2026 · first bout locks Sat Nov 14, 5:00 PM ET

| Bout | Win chance | Fair odds | Market | Model alone | KO / Sub / Dec | Distance | Most likely result | Moneyline edge | Round total edge | Method edge |
|---|---|---|---|---|---|---|---|---|---|---|
| **Ciryl Gane** vs. **Josh Hokit**<br>HW, title, 5 rds | Gane 70% – 30% Hokit | -230 / +230 | Gane 67% (-230 / +190) | Gane 61% (-160) | Gane 47% / 5% / 17%<br>Hokit 23% / 1% / 6% | 24% | Gane by KO/TKO (47%) | no edge | no edge | no prices yet; fair KO / Sub / Dec<br>Gane +110 / +1845 / +475<br>Hokit +335 / +9900 / +1470 |
| **Kayla Harrison** vs. **Amanda Nunes**<br>W-BW, title, 5 rds | Harrison 64% – 36% Nunes | -175 / +175 | Harrison 60% (-166 / +140) | Harrison 65% (-190) | Harrison 8% / 22% / 34%<br>Nunes 7% / 6% / 23% | 57% | Harrison by decision (34%) | no edge | no edge | no prices yet; fair KO / Sub / Dec<br>Harrison +1170 / +355 / +195<br>Nunes +1340 / +1660 / +325 |
| **Caio Borralho** vs. **Yousri Belgaroui**<br>MW, 3 rds | Borralho 57% – 43% Belgaroui | -130 / +130 | Borralho 59% (-155 / +136) | Borralho 39% (+155) | Borralho 19% / 7% / 31%<br>Belgaroui 23% / 3% / 18% | 49% | Borralho by decision (31%) | no edge | no edge | no prices yet; fair KO / Sub / Dec<br>Borralho +435 / +1355 / +225<br>Belgaroui +345 / +3845 / +445 |
| **Uroš Medić** vs. **Kevin Holland**<br>WW, 3 rds | Medić 57% – 43% Holland | -130 / +130 | Medić 58% (-155 / +130) | Medić 43% (+135) | Medić 37% / 2% / 18%<br>Holland 18% / 7% / 18% | 36% | Medić by KO/TKO (37%) | no edge | no edge | no prices yet; fair KO / Sub / Dec<br>Medić +170 / +4720 / +465<br>Holland +470 / +1255 / +445 |
| **Bilal Hasan** vs. **Luis Gurule**<br>FLW, 3 rds | Hasan 91% – 9% Gurule | -1040 / +1040 | Hasan 87% (-1000 / +650) | Hasan 82% (-445) | Hasan 35% / 17% / 40%<br>Gurule 2% / 1% / 5% | 45% | Hasan by decision (40%) | no edge | no edge | no prices yet; fair KO / Sub / Dec<br>Hasan +185 / +505 / +150<br>Gurule +4500 / +7985 / +1760 |
| **Stephen Thompson** vs. **Charles Radtke**<br>WW, 3 rds | Thompson 51% – 49% Radtke | -105 / +105 | Thompson 55% (-135 / +114) | Thompson 35% (+190) | Thompson 21% / 5% / 26%<br>Radtke 14% / 11% / 23% | 49% | Thompson by decision (26%) | Radtke (+114): EV +3.8%, 49%, stake 0.8u | no edge | no prices yet; fair KO / Sub / Dec<br>Thompson +385 / +1865 / +290<br>Radtke +600 / +810 / +330 |
| **Drew Dober** vs. **Chris Duncan**<br>LW, 3 rds | Dober 33% – 67% Duncan | +200 / -200 | Dober 38% (+154 / -185) | Dober 32% (+210) | Dober 15% / 5% / 14%<br>Duncan 21% / 16% / 30% | 43% | Duncan by decision (30%) | no edge | no edge | no prices yet; fair KO / Sub / Dec<br>Dober +560 / +2105 / +635<br>Duncan +385 / +510 / +240 |
| **Jim Miller** vs. **Terrance McKinney**<br>LW, 3 rds | Miller 27% – 73% McKinney | +270 / -270 | Miller 34% (+180 / -218) | Miller 21% (+365) | Miller 11% / 9% / 7%<br>McKinney 30% / 17% / 25% | 32% | McKinney by KO/TKO (30%) | McKinney (-218): EV +6.2%, 73%, stake 3.0u | no edge | no prices yet; fair KO / Sub / Dec<br>Miller +795 / +970 / +1400<br>McKinney +230 / +475 / +295 |
| **Donte Johnson** vs. **Cesar Almeida**<br>CW, 3 rds | Johnson 72% – 28% Almeida | -260 / +260 | Johnson 64% (-205 / +170) | Johnson 81% (-415) | Johnson 24% / 17% / 31%<br>Almeida 8% / 4% / 15% | 46% | Johnson by decision (31%) | Johnson (-205): EV +7.5%, 72%, stake 3.0u | no edge | no prices yet; fair KO / Sub / Dec<br>Johnson +315 / +480 / +225<br>Almeida +1105 / +2230 / +560 |
| **Jared Gordon** vs. **Melquizael Costa**<br>LW, 3 rds | Gordon 19% – 81% Costa | +415 / -415 | Gordon 24% (+300 / -380) | Gordon 27% (+265) | Gordon 7% / 2% / 11%<br>Costa 30% / 20% / 30% | 41% | Costa by KO/TKO (30%) | no edge | no edge | no prices yet; fair KO / Sub / Dec<br>Gordon +1395 / +4470 / +850<br>Costa +230 / +390 / +230 |
| **Macy Chiasson** vs. **Bia Mesquita**<br>W-BW, 3 rds | Chiasson 26% – 74% Mesquita | +280 / -280 | Chiasson 31% (+210 / -258) | Chiasson 30% (+230) | Chiasson 3% / 4% / 19%<br>Mesquita 5% / 43% / 25% | 44% | Mesquita by submission (43%) | no edge | no edge | no prices yet; fair KO / Sub / Dec<br>Chiasson +2970 / +2220 / +430<br>Mesquita +1855 / +130 / +290 |
| **Alatengheili** vs. **Juan Diaz**<br>BW, 3 rds | Alatengheili 16% – 84% Diaz | +510 / -510 | Alatengheili 21% (+360 / -470) | Alatengheili 26% (+285) | Alatengheili 3% / 2% / 11%<br>Diaz 12% / 29% / 43% | 54% | Diaz by decision (43%) | no edge | no edge | no prices yet; fair KO / Sub / Dec<br>Alatengheili +2990 / +5540 / +775<br>Diaz +755 / +240 / +135 |
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
| Johnson vs. Almeida | 28% | 17% | 9% |  |  | 46% |
| Gordon vs. Costa | 32% | 19% | 9% |  |  | 41% |
| Chiasson vs. Mesquita | 29% | 18% | 9% |  |  | 44% |
| Alatengheili vs. Diaz | 23% | 15% | 8% |  |  | 54% |
| Elder vs. Sanches | 28% | 17% | 9% |  |  | 46% |

## UFC Fight Night: Procházka vs. Stirling

Saturday, November 21, 2026 · first bout locks Sat Nov 21, 10:00 AM ET

| Bout | Win chance | Fair odds | Market | Model alone | KO / Sub / Dec | Distance | Most likely result | Moneyline edge | Round total edge | Method edge |
|---|---|---|---|---|---|---|---|---|---|---|
| **Jiří Procházka** vs. **Navajo Stirling**<br>LHW, 5 rds | Procházka 38% – 62% Stirling | +165 / -165 | Procházka 43% (+124 / -148) | Procházka 32% (+215) | Procházka 26% / 3% / 10%<br>Stirling 46% / 4% / 12% | 22% | Stirling by KO/TKO (46%) | Stirling (-148): EV +3.8%, 62%, stake 1.4u | no price yet; fair Over 1.5 -130, Under +130 | no prices yet; fair KO / Sub / Dec<br>Procházka +290 / +3500 / +940<br>Stirling +115 / +2450 / +740 |
| **Aljamain Sterling** vs. **Kevin Vallejos**<br>FW, 3 rds | Sterling 43% – 57% Vallejos | +130 / -130 | Sterling 45% (+114 / -135) | Sterling 43% (+130) | Sterling 7% / 5% / 32%<br>Vallejos 25% / 3% / 29% | 61% | Sterling by decision (32%) | no edge | no price yet; fair Over 2.5 -180, Under +180 | no prices yet; fair KO / Sub / Dec<br>Sterling +1380 / +2055 / +215<br>Vallejos +305 / +3150 / +240 |
| **Dan Hooker** vs. **Brian Ortega**<br>LW, 3 rds | Hooker 59% – 41% Ortega | -140 / +140 | Hooker 59% (-162 / +136) | Hooker 46% (+115) | Hooker 25% / 9% / 25%<br>Ortega 16% / 10% / 15% | 40% | Hooker by decision (25%) | no edge | no price yet; fair Over 2.5 +125, Under -125 | no prices yet; fair KO / Sub / Dec<br>Hooker +300 / +1060 / +295<br>Ortega +545 / +855 / +555 |
| **Kyoji Horiguchi** vs. **Asu Almabayev**<br>FLW, 3 rds | Horiguchi 63% – 37% Almabayev | -170 / +170 | Horiguchi 64% (-205 / +170) | Horiguchi 43% (+135) | Horiguchi 13% / 12% / 38%<br>Almabayev 5% / 14% / 18% | 56% | Horiguchi by decision (38%) | no edge | no price yet; fair Over 2.5 -150, Under +150 | no prices yet; fair KO / Sub / Dec<br>Horiguchi +685 / +720 / +160<br>Almabayev +2065 / +595 / +465 |
| **Jared Cannonier** vs. **Ikram Aliskerov**<br>MW, 3 rds | Cannonier 19% – 81% Aliskerov | +415 / -415 | Cannonier 26% (+275 / -345) | Cannonier 21% (+375) | Cannonier 8% / 2% / 10%<br>Aliskerov 33% / 9% / 39% | 48% | Aliskerov by decision (39%) | Aliskerov (-345): EV +3.9%, 81%, stake 3.0u | no price yet; fair Over 2.5 -110, Under +110 | no prices yet; fair KO / Sub / Dec<br>Cannonier +1140 / +5400 / +945<br>Aliskerov +205 / +1045 / +160 |
| **Aleksandre Topuria** vs. **Santiago Luna**<br>BW, 3 rds | Topuria 39% – 61% Luna | +155 / -155 | no line yet | Topuria 39% (+155) | Topuria 8% / 7% / 25%<br>Luna 16% / 8% / 37% | 61% | Luna by decision (37%) | no line yet | no price yet; fair Over 2.5 -185, Under +185 | no prices yet; fair KO / Sub / Dec<br>Topuria +1130 / +1415 / +305<br>Luna +530 / +1120 / +175 |
| **Shamil Gaziev** vs. **Tallison Teixeira**<br>HW, 3 rds | Gaziev 62% – 38% Teixeira | -165 / +165 | Gaziev 66% (-225 / +185) | Gaziev 29% (+240) | Gaziev 41% / 5% / 16%<br>Teixeira 23% / 3% / 12% | 27% | Gaziev by KO/TKO (41%) | Teixeira (+185): EV +8.3%, 38%, stake 1.1u | no price yet; fair Over 1.5 +110, Under -110 | no prices yet; fair KO / Sub / Dec<br>Gaziev +145 / +1775 / +540<br>Teixeira +330 / +3040 / +760 |
| **Amir Albazi** vs. **Alessandro Costa**<br>FLW, 3 rds | Albazi 44% – 56% Costa | +125 / -125 | Albazi 45% (+114 / -135) | Albazi 48% (+105) | Albazi 10% / 8% / 26%<br>Costa 16% / 13% / 27% | 52% | Costa by decision (27%) | no edge | no price yet; fair Over 2.5 -130, Under +130 | no prices yet; fair KO / Sub / Dec<br>Albazi +865 / +1085 / +290<br>Costa +520 / +685 / +275 |
| **Jake Matthews** vs. **Tahir Abdullayev**<br>WW, 3 rds | Matthews 62% – 38% Abdullayev | -165 / +165 | Matthews 60% (-170 / +142) | Matthews 56% (-130) | Matthews 19% / 11% / 33%<br>Abdullayev 11% / 7% / 20% | 53% | Matthews by decision (33%) | no edge | no price yet; fair Over 2.5 -130, Under +130 | no prices yet; fair KO / Sub / Dec<br>Matthews +430 / +845 / +205<br>Abdullayev +810 / +1370 / +400 |
| **Nikolas Motta** vs. **Dom Mar Fan**<br>LW, 3 rds | Motta 28% – 72% Fan | +265 / -265 | no line yet | Motta 28% (+265) | Motta 13% / 4% / 11%<br>Fan 31% / 9% / 32% | 43% | Fan by decision (32%) | no line yet | no price yet; fair Over 2.5 +110, Under -110 | no prices yet; fair KO / Sub / Dec<br>Motta +695 / +2610 / +785<br>Fan +225 / +960 / +210 |
| **Diyar Nurgozhay** vs. **Alik Lorenz**<br>LHW, 3 rds, UFC debut: Lorenz | Nurgozhay 64% – 36% Lorenz | -180 / +180 | no line yet | Nurgozhay 64% (-180) | Nurgozhay 39% / 6% / 20%<br>Lorenz 17% / 8% / 10% | 30% | Nurgozhay by KO/TKO (39%) | no line yet | no price yet; fair Over 1.5 +100, Under -100 | no prices yet; fair KO / Sub / Dec<br>Nurgozhay +155 / +1650 / +415<br>Lorenz +485 / +1095 / +900 |

When it ends (either fighter):

| Bout | Round 1 | Round 2 | Round 3 | Round 4 | Round 5 | Decision |
|---|---|---|---|---|---|---|
| Procházka vs. Stirling | 33% | 22% | 13% | 6% | 5% | 22% |
| Sterling vs. Vallejos | 19% | 13% | 7% |  |  | 61% |
| Hooker vs. Ortega | 32% | 19% | 9% |  |  | 40% |
| Horiguchi vs. Almabayev | 22% | 15% | 8% |  |  | 56% |
| Cannonier vs. Aliskerov | 27% | 17% | 8% |  |  | 48% |
| Topuria vs. Luna | 19% | 13% | 7% |  |  | 61% |
| Gaziev vs. Teixeira | 42% | 22% | 9% |  |  | 27% |
| Albazi vs. Costa | 24% | 16% | 8% |  |  | 52% |
| Matthews vs. Abdullayev | 24% | 16% | 8% |  |  | 53% |
| Motta vs. Fan | 30% | 18% | 9% |  |  | 43% |
| Nurgozhay vs. Lorenz | 40% | 21% | 9% |  |  | 30% |

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
|  | 4 | Alexandre Pantoja | 1894 | 238 | 14-5 | 2026-09-19 |
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
|  | 5 | Jean Silva | 2075 | 302 | 7-1 | 2026-09-12 |
| Lightweight | 1 | Ilia Topuria | 2274 | 297 | 9-1 | 2026-06-14 |
|  | 2 | Justin Gaethje | 2193 | 240 | 11-5 | 2026-06-14 |
|  | 3 | Charles Oliveira | 2146 | 212 | 25-11 | 2026-03-07 |
|  | 4 | Arman Tsarukyan | 2148 | 268 | 11-2 | 2026-09-19 |
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
