# UFC fight predictions

Updated Sun Nov 01, 2026 01:32 PM ET. Refreshed automatically every day and several times on fight week; each bout's prediction is locked when its part of the card starts and graded once the result is in.

Each bout gets one consistent breakdown: each fighter's chance to win, split into KO/TKO, submission and decision, and the chance it ends in each round. The win chance blends the model with the betting market (about 81% market, the weight that has predicted best on past fights) and corrects the market's habit of underrating heavy favorites. MMA is high-variance: even the most likely single result is usually well under 50%.

The fair odds are the American odds that match the win chance with no bookmaker margin: -200 means risk $200 to win $100, +200 means risk $100 to win $200. A sportsbook only offers value on a fighter when its price beats the fair line.

The three edge columns value every side of each market at its posted price: expected value (EV) is the average profit per $1 staked, from the final prediction: the win chance blended with the moneyline (which corrects the market's habit of underrating heavy favorites), and method and round chances anchored to their own props, moved only by what the blend changes. A side is an edge when its EV is at least 3%; each cell names the best side if one clears that bar, with its stake, a 25% share of the Kelly stake in units of 1% of the bankroll, at most 3 units on one bout; else "no edge". Moneylines and props are never priced near -110, so a missing price is never assumed: without one, the round-total cell shows the model's fair odds at the line closest to even and the method cell each fighter's fair KO/TKO, submission and decision odds. Over 1.5 rounds means the fight passes 2:30 of round 2 (a decision is always over); finishes are assumed spread evenly within a round.

See the backtest (backtest.md) for how these edges did against the dataset's closing prices, next to the model alone, which finds a 3% edge in most fights and lost money on them. Treat these columns as a live test, tracked below, not as betting advice.

## UFC Fight Night: Cortes Acosta vs. Walker

Saturday, November 07, 2026 · first bout locks Sat Nov 7, 5:00 PM ET

| Bout | Win chance | Fair odds | Market | Model alone | KO / Sub / Dec | Distance | Most likely result | Moneyline edge | Round total edge | Method edge |
|---|---|---|---|---|---|---|---|---|---|---|
| **Waldo Cortes Acosta** vs. **Johnny Walker**<br>HW, 5 rds | Acosta 66% – 34% Walker | -195 / +195 | Acosta 64% (-198 / +164) | Acosta 58% (-140) | Acosta 47% / 4% / 15%<br>Walker 21% / 2% / 10% | 25% | Acosta by KO/TKO (47%) | no edge | no edge | no prices yet; fair KO / Sub / Dec<br>Acosta +115 / +2445 / +560<br>Walker +365 / +4040 / +875 |
| **Tatiana Suarez** vs. **Virna Jandiroba**<br>W-SW, 3 rds | Suarez 66% – 34% Jandiroba | -195 / +195 | Suarez 62% (-185 / +154) | Suarez 65% (-185) | Suarez 4% / 16% / 46%<br>Jandiroba 2% / 8% / 24% | 71% | Suarez by decision (46%) | no edge | no edge | no prices yet; fair KO / Sub / Dec<br>Suarez +2715 / +525 / +115<br>Jandiroba +5280 / +1150 / +315 |
| **Davey Grant** vs. **Elijah Smith**<br>BW, 3 rds | Grant 26% – 74% Smith | +290 / -290 | Grant 34% (+185 / -225) | Grant 18% (+465) | Grant 7% / 2% / 17%<br>Smith 19% / 19% / 37% | 53% | Smith by decision (37%) | Smith (-225): EV +7.5%, 74%, stake 3.0u | no price yet; fair Over 2.5 -135, Under +135 | no prices yet; fair KO / Sub / Dec<br>Grant +1400 / +4595 / +495<br>Smith +420 / +435 / +175 |
| **Seokhyeon Ko** vs. **Wellington Turman**<br>WW, 3 rds | Ko 88% – 12% Turman | -715 / +715 | Ko 83% (-650 / +470) | Ko 79% (-375) | Ko 22% / 21% / 45%<br>Turman 3% / 2% / 7% | 52% | Ko by decision (45%) | no edge | no price yet; fair Over 2.5 -125, Under +125 | no prices yet; fair KO / Sub / Dec<br>Ko +345 / +385 / +125<br>Turman +3070 / +4560 / +1330 |
| **Billy Elekana** vs. **Lucas Fernando**<br>LHW, 3 rds | Elekana 29% – 71% Fernando | +250 / -250 | Elekana 31% (+210 / -258) | Elekana 42% (+135) | Elekana 11% / 7% / 10%<br>Fernando 46% / 7% / 19% | 28% | Fernando by KO/TKO (46%) | no edge | no edge | no prices yet; fair KO / Sub / Dec<br>Elekana +770 / +1240 / +920<br>Fernando +120 / +1370 / +440 |
| **Mantas Kondratavičius** vs. **Andre Petroski**<br>MW, 3 rds | Kondratavičius 76% – 24% Petroski | -320 / +320 | Kondratavičius 71% (-285 / +230) | Kondratavičius 73% (-265) | Kondratavičius 38% / 10% / 28%<br>Petroski 6% / 5% / 12% | 40% | Kondratavičius by KO/TKO (38%) | no edge | no edge | no prices yet; fair KO / Sub / Dec<br>Kondratavičius +160 / +925 / +255<br>Petroski +1475 / +1825 / +710 |
| **Gabriel Lorenço** vs. **Thomas Petersen**<br>HW, 3 rds, UFC debut: Lorenço | Lorenço 37% – 63% Petersen | +170 / -170 | Lorenço 40% (+142 / -170) | Lorenço 39% (+155) | Lorenço 19% / 6% / 12%<br>Petersen 27% / 9% / 27% | 39% | Petersen by decision (27%) | no edge | no price yet; fair Over 2.5 +130, Under -130 | no prices yet; fair KO / Sub / Dec<br>Lorenço +415 / +1670 / +755<br>Petersen +275 / +990 / +265 |
| **Karine Silva** vs. **Gabriella Fernandes**<br>W-FLW, 3 rds | Silva 65% – 35% Fernandes | -185 / +185 | Silva 60% (-166 / +140) | Silva 69% (-220) | Silva 9% / 19% / 37%<br>Fernandes 4% / 5% / 26% | 63% | Silva by decision (37%) | Silva (-166): EV +3.6%, 65%, stake 1.5u | no edge | no prices yet; fair KO / Sub / Dec<br>Silva +1065 / +420 / +170<br>Fernandes +2150 / +1920 / +285 |
| **Mitch Raposo** vs. **Marcos Degli**<br>FLW, 3 rds, UFC debut: Degli | Raposo 35% – 65% Degli | +180 / -180 | Raposo 34% (+180 / -218) | Raposo 58% (-140) | Raposo 7% / 6% / 22%<br>Degli 14% / 13% / 38% | 60% | Degli by decision (38%) | no edge | no price yet; fair Over 2.5 -175, Under +175 | no prices yet; fair KO / Sub / Dec<br>Raposo +1310 / +1485 / +355<br>Degli +635 / +665 / +165 |
| **Jose Delano** vs. **Murtazali Magomedov**<br>FW, 3 rds | Delano 47% – 53% Magomedov | +110 / -110 | Delano 48% (-102 / -118) | Delano 46% (+115) | Delano 15% / 3% / 29%<br>Magomedov 12% / 18% / 22% | 51% | Delano by decision (29%) | no edge | no price yet; fair Over 2.5 -125, Under +125 | no prices yet; fair KO / Sub / Dec<br>Delano +560 / +2850 / +245<br>Magomedov +730 / +445 / +350 |
| **Keiichiro Nakamura** vs. **Ollie Schmid**<br>FW, 3 rds | Nakamura 78% – 22% Schmid | -360 / +360 | Nakamura 76% (-375 / +295) | Nakamura 60% (-150) | Nakamura 44% / 8% / 27%<br>Schmid 7% / 3% / 12% | 39% | Nakamura by KO/TKO (44%) | no edge | no price yet; fair Over 2.5 +130, Under -130 | no prices yet; fair KO / Sub / Dec<br>Nakamura +130 / +1180 / +275<br>Schmid +1385 / +3305 / +720 |
| **Austin Bashi** vs. **Lucas Brennan**<br>FW, 3 rds | Bashi 66% – 34% Brennan | -195 / +195 | no line yet | Bashi 66% (-195) | Bashi 15% / 19% / 32%<br>Brennan 9% / 6% / 19% | 51% | Bashi by decision (32%) | no line yet | no price yet; fair Over 2.5 -120, Under +120 | no prices yet; fair KO / Sub / Dec<br>Bashi +555 / +435 / +215<br>Brennan +1000 / +1500 / +430 |
| **Priscila Cachoeira** vs. **Nina Milošević**<br>W-BW, 3 rds | Cachoeira 15% – 85% Milošević | +585 / -585 | Cachoeira 22% (+340 / -440) | Cachoeira 13% (+655) | Cachoeira 3% / 1% / 10%<br>Milošević 29% / 14% / 42% | 52% | Milošević by decision (42%) | Milošević (-440): EV +4.8%, 85%, stake 3.0u | no price yet; fair Over 2.5 -130, Under +130 | no prices yet; fair KO / Sub / Dec<br>Cachoeira +3540 / +6935 / +860<br>Milošević +240 / +605 / +140 |
| **Jonny Parsons** vs. **Jose Henrique**<br>WW, 3 rds, UFC debut: Henrique | Parsons 37% – 63% Henrique | +165 / -165 | Parsons 38% (+154 / -185) | Parsons 50% (-100) | Parsons 18% / 3% / 16%<br>Henrique 21% / 11% / 31% | 47% | Henrique by decision (31%) | no edge | no price yet; fair Over 2.5 -105, Under +105 | no prices yet; fair KO / Sub / Dec<br>Parsons +455 / +2855 / +525<br>Henrique +375 / +835 / +225 |

When it ends (either fighter):

| Bout | Round 1 | Round 2 | Round 3 | Round 4 | Round 5 | Decision |
|---|---|---|---|---|---|---|
| Acosta vs. Walker | 30% | 21% | 12% | 6% | 5% | 25% |
| Suarez vs. Jandiroba | 14% | 10% | 5% |  |  | 71% |
| Grant vs. Smith | 24% | 15% | 8% |  |  | 53% |
| Ko vs. Turman | 25% | 16% | 8% |  |  | 52% |
| Elekana vs. Fernando | 41% | 21% | 9% |  |  | 28% |
| Kondratavičius vs. Petroski | 32% | 19% | 9% |  |  | 40% |
| Lorenço vs. Petersen | 33% | 19% | 9% |  |  | 39% |
| Silva vs. Fernandes | 18% | 13% | 7% |  |  | 63% |
| Raposo vs. Degli | 20% | 13% | 7% |  |  | 60% |
| Delano vs. Magomedov | 25% | 16% | 8% |  |  | 51% |
| Nakamura vs. Schmid | 33% | 19% | 9% |  |  | 39% |
| Bashi vs. Brennan | 25% | 16% | 8% |  |  | 51% |
| Cachoeira vs. Milošević | 24% | 16% | 8% |  |  | 52% |
| Parsons vs. Henrique | 28% | 17% | 8% |  |  | 47% |

## UFC 334: Gane vs. Hokit

Saturday, November 14, 2026 · first bout locks Sat Nov 14, 5:00 PM ET

| Bout | Win chance | Fair odds | Market | Model alone | KO / Sub / Dec | Distance | Most likely result | Moneyline edge | Round total edge | Method edge |
|---|---|---|---|---|---|---|---|---|---|---|
| **Ciryl Gane** vs. **Josh Hokit**<br>HW, title, 5 rds | Gane 72% – 28% Hokit | -260 / +260 | Gane 70% (-265 / +215) | Gane 61% (-155) | Gane 49% / 5% / 18%<br>Hokit 21% / 1% / 6% | 24% | Gane by KO/TKO (49%) | no edge | no edge | no prices yet; fair KO / Sub / Dec<br>Gane +105 / +1755 / +455<br>Hokit +380 / +9900 / +1605 |
| **Kayla Harrison** vs. **Amanda Nunes**<br>W-BW, title, 5 rds | Harrison 67% – 33% Nunes | -200 / +200 | Harrison 63% (-192 / +160) | Harrison 65% (-190) | Harrison 8% / 23% / 36%<br>Nunes 6% / 5% / 22% | 57% | Harrison by decision (36%) | no edge | no edge | no prices yet; fair KO / Sub / Dec<br>Harrison +1135 / +330 / +180<br>Nunes +1500 / +1835 / +360 |
| **Caio Borralho** vs. **Yousri Belgaroui**<br>MW, 3 rds | Borralho 55% – 45% Belgaroui | -120 / +120 | Borralho 57% (-148 / +124) | Borralho 39% (+155) | Borralho 18% / 7% / 30%<br>Belgaroui 23% / 3% / 19% | 49% | Borralho by decision (30%) | no edge | no price yet; fair Over 2.5 -115, Under +115 | no prices yet; fair KO / Sub / Dec<br>Borralho +450 / +1405 / +230<br>Belgaroui +325 / +3660 / +425 |
| **Uroš Medić** vs. **Kevin Holland**<br>WW, 3 rds | Medić 58% – 42% Holland | -140 / +140 | Medić 59% (-162 / +136) | Medić 43% (+135) | Medić 38% / 2% / 18%<br>Holland 17% / 7% / 18% | 36% | Medić by KO/TKO (38%) | no edge | no price yet; fair Over 1.5 -120, Under +120 | no prices yet; fair KO / Sub / Dec<br>Medić +165 / +4550 / +455<br>Holland +485 / +1295 / +460 |
| **Bilal Hasan** vs. **Luis Gurule**<br>FLW, 3 rds | Hasan 91% – 9% Gurule | -1000 / +1000 | Hasan 87% (-950 / +625) | Hasan 82% (-445) | Hasan 35% / 17% / 40%<br>Gurule 2% / 1% / 6% | 45% | Hasan by decision (40%) | no edge | no price yet; fair Over 2.5 +100, Under -100 | no prices yet; fair KO / Sub / Dec<br>Hasan +190 / +505 / +155<br>Gurule +4325 / +7620 / +1700 |
| **Stephen Thompson** vs. **Charles Radtke**<br>WW, 3 rds | Thompson 35% – 65% Radtke | +185 / -185 | no line yet | Thompson 35% (+185) | Thompson 14% / 3% / 18%<br>Radtke 19% / 15% / 31% | 48% | Radtke by decision (31%) | no line yet | no price yet; fair Over 2.5 -110, Under +110 | no prices yet; fair KO / Sub / Dec<br>Thompson +615 / +2975 / +465<br>Radtke +425 / +545 / +225 |
| **Drew Dober** vs. **Chris Duncan**<br>LW, 3 rds | Dober 32% – 68% Duncan | +210 / -210 | no line yet | Dober 32% (+210) | Dober 15% / 4% / 13%<br>Duncan 21% / 17% / 30% | 43% | Duncan by decision (30%) | no line yet | no price yet; fair Over 2.5 +110, Under -110 | no prices yet; fair KO / Sub / Dec<br>Dober +585 / +2180 / +660<br>Duncan +375 / +495 / +235 |
| **Jim Miller** vs. **Terrance McKinney**<br>LW, 3 rds | Miller 22% – 78% McKinney | +360 / -360 | no line yet | Miller 22% (+360) | Miller 9% / 7% / 5%<br>McKinney 33% / 19% / 27% | 32% | McKinney by KO/TKO (33%) | no line yet | no price yet; fair Over 1.5 -110, Under +110 | no prices yet; fair KO / Sub / Dec<br>Miller +1020 / +1260 / +1750<br>McKinney +205 / +430 / +275 |
| **Donte Johnson** vs. **Cesar Almeida**<br>MW, 3 rds | Johnson 80% – 20% Almeida | -415 / +415 | no line yet | Johnson 80% (-415) | Johnson 34% / 17% / 30%<br>Almeida 7% / 3% / 10% | 40% | Johnson by KO/TKO (34%) | no line yet | no price yet; fair Over 2.5 +125, Under -125 | no prices yet; fair KO / Sub / Dec<br>Johnson +195 / +495 / +235<br>Almeida +1255 / +3895 / +940 |
| **Macy Chiasson** vs. **Bia Mesquita**<br>W-BW, 3 rds | Chiasson 31% – 69% Mesquita | +230 / -230 | no line yet | Chiasson 31% (+230) | Chiasson 4% / 5% / 22%<br>Mesquita 5% / 40% / 24% | 46% | Mesquita by submission (40%) | no line yet | no price yet; fair Over 2.5 -100, Under +100 | no prices yet; fair KO / Sub / Dec<br>Chiasson +2580 / +1870 / +360<br>Mesquita +1995 / +150 / +310 |
| **Adrian Yañez** vs. **Juan Diaz**<br>BW, 3 rds | Yañez 37% – 63% Diaz | +170 / -170 | no line yet | Yañez 37% (+170) | Yañez 14% / 3% / 20%<br>Diaz 11% / 22% / 30% | 50% | Diaz by decision (30%) | no line yet | no price yet; fair Over 2.5 -120, Under +120 | no prices yet; fair KO / Sub / Dec<br>Yañez +590 / +3605 / +410<br>Diaz +820 / +355 / +230 |
| **Nazim Sadykhov** vs. **Jefferson Nascimento**<br>LW, 3 rds | Sadykhov 49% – 51% Nascimento | +105 / -105 | no line yet | Sadykhov 49% (+105) | Sadykhov 23% / 8% / 18%<br>Nascimento 24% / 8% / 19% | 37% | Nascimento by KO/TKO (24%) | no line yet | no price yet; fair Over 1.5 -125, Under +125 | no prices yet; fair KO / Sub / Dec<br>Sadykhov +335 / +1110 / +465<br>Nascimento +315 / +1185 / +415 |
| **Jared Gordon** vs. **Melquizael Costa**<br>LW, 3 rds | Gordon 27% – 73% Costa | +265 / -265 | no line yet | Gordon 27% (+265) | Gordon 9% / 3% / 15%<br>Costa 27% / 18% / 28% | 42% | Costa by decision (28%) | no line yet | no price yet; fair Over 2.5 +115, Under -115 | no prices yet; fair KO / Sub / Dec<br>Gordon +955 / +3030 / +580<br>Costa +265 / +460 / +265 |
| **Evan Elder** vs. **Samuel Sanches**<br>LW, 3 rds, UFC debut: Sanches | Elder 54% – 46% Sanches | -115 / +115 | no line yet | Elder 54% (-115) | Elder 20% / 8% / 25%<br>Sanches 17% / 8% / 21% | 46% | Elder by decision (25%) | no line yet | no price yet; fair Over 2.5 -100, Under +100 | no prices yet; fair KO / Sub / Dec<br>Elder +395 / +1085 / +295<br>Sanches +495 / +1085 / +380 |

When it ends (either fighter):

| Bout | Round 1 | Round 2 | Round 3 | Round 4 | Round 5 | Decision |
|---|---|---|---|---|---|---|
| Gane vs. Hokit | 31% | 22% | 12% | 6% | 5% | 24% |
| Harrison vs. Nunes | 14% | 12% | 8% | 5% | 4% | 57% |
| Borralho vs. Belgaroui | 26% | 16% | 8% |  |  | 49% |
| Medić vs. Holland | 35% | 20% | 9% |  |  | 36% |
| Hasan vs. Gurule | 29% | 18% | 9% |  |  | 45% |
| Thompson vs. Radtke | 27% | 17% | 8% |  |  | 48% |
| Dober vs. Duncan | 30% | 18% | 9% |  |  | 43% |
| Miller vs. McKinney | 38% | 21% | 9% |  |  | 32% |
| Johnson vs. Almeida | 32% | 19% | 9% |  |  | 40% |
| Chiasson vs. Mesquita | 28% | 17% | 9% |  |  | 46% |
| Yañez vs. Diaz | 26% | 16% | 8% |  |  | 50% |
| Sadykhov vs. Nascimento | 34% | 20% | 9% |  |  | 37% |
| Gordon vs. Costa | 31% | 18% | 9% |  |  | 42% |
| Elder vs. Sanches | 28% | 17% | 9% |  |  | 46% |

## How the 2026 predictions have done

| Predictor | Fights | Log loss | Brier | Winners |
|---|---|---|---|---|
| Final prediction | 475 | 0.6189 | 0.215 | 64.2% |
| Model alone (before the market) | 475 | 0.6389 | 0.223 | 62.1% |
| Glicko-2 rating alone | 475 | 0.6821 | 0.244 | 57.5% |
| Final, on fights with a price | 140 | 0.5231 | 0.175 | 75.0% |
| Market price when predicted | 140 | 0.5340 | 0.177 | 75.7% |
| Coin flip | 475 | 0.6931 | 0.250 | – |

Log loss scores the win chances (lower is better; a coin flip scores 0.693, and the betting market about 0.61). Brier is the squared error of the win chance. Picking every betting favorite already gets about two thirds of winners right, so the win rate says little on its own.

- Winner and method (six outcomes): log loss 1.579 on 474 fights, against 1.792 for guessing uniformly. The single most likely result happened 34% of the time.
- Went the distance: predicted 49% on average, actual 42%.

449 of these fights happened before the predictor went live. They are backfilled walk-forward (each fight predicted from earlier fights only, with models fitted on earlier years) using the odds dataset's approximate closing prices, which run only through March 2026, so later backfilled fights use the model alone. Every fight since is graded on the prediction logged before it started.

### Edge record

Every edge logged with a live prediction (the last one before the fight), at the stake and price logged with it; edges logged before edges were priced from the final prediction are left out. Pushes return the stake (a no contest voids every bet; a draw refunds the moneyline). Units are 1% of the bankroll; ROI is units won per unit staked, and expected ROI is what the edges' EVs promised.

| Market | Edges | Record (W-L-P) | Staked | Units won | ROI | Expected ROI |
|---|---|---|---|---|---|---|
| Moneyline | 3 | 1-2-0 | 5.9 | -1.99 | -33.9% | +5.7% |
| Round total | 0 | 0-0-0 | 0.0 | +0.00 | – | – |
| Method of victory | 0 | 0-0-0 | 0.0 | +0.00 | – | – |

### Latest results: UFC Fight Night: Moicano vs. Nolan

| Bout | Predicted | Result | Chance given to the winner | Chance given to the exact result |
|---|---|---|---|---|
| Renato Moicano vs. Tom Nolan | Nolan 50% | Tom Nolan by KO/TKO, R3 | 50% | 21% |
| Randy Brown vs. Jacobe Smith | Smith 75% | Jacobe Smith by decision | 75% | 33% |
| Ode' Osbourne vs. Cody Durden | Durden 53% | Cody Durden by decision | 53% | 27% |
| Yana Santos vs. Luana Santos | Santos 80% | Luana Santos by decision | 80% | 52% |
| Jean-Paul Lebosnoyani vs. Farman Hasanov | Lebosnoyani 74% | Jean-Paul Lebosnoyani by KO/TKO, R3 | 74% | 18% |
| Francis Marshall vs. Dakota Hope | Marshall 68% | Dakota Hope by decision | 32% | 19% |
| Rodrigo Sezinando vs. Theodor Berggren | Sezinando 61% | Rodrigo Sezinando by KO/TKO, R2 | 61% | 33% |
| Julian Erosa vs. JeongYeong Lee | Lee 58% | Julian Erosa by KO/TKO, R1 | 42% | 13% |
| Zach Reese vs. Mickey Gall | Reese 82% | Zach Reese by decision | 82% | 26% |
| Nick Klein vs. Joe Kropschot | Kropschot 74% | Joe Kropschot by submission, R2 | 74% | 17% |
| Talita Alencar vs. Piera Rodriguez | Rodriguez 73% | Piera Rodriguez by decision | 73% | 62% |
| Lucia Szabová vs. Tainara Lisboa | Szabová 87% | Lucia Szabová by KO/TKO, R3 | 87% | 14% |

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
|  | 2 | Merab Dvalishvili | 2128 | 224 | 14-4 | 2026-10-24 |
|  | 3 | Song Yadong | 2064 | 225 | 13-4-1 | 2026-08-29 |
|  | 4 | Cory Sandhagen | 2059 | 231 | 11-6 | 2026-07-11 |
|  | 5 | Sean O'Malley | 2059 | 244 | 12-3 | 2026-06-14 |
| Featherweight | 1 | Alexander Volkanovski | 2214 | 225 | 16-3 | 2026-10-24 |
|  | 2 | Diego Lopes | 2145 | 267 | 7-3 | 2026-06-14 |
|  | 3 | Aljamain Sterling | 2097 | 229 | 18-5 | 2026-04-25 |
|  | 4 | Brian Ortega | 2062 | 272 | 8-5 | 2025-08-23 |
|  | 5 | Jean Silva | 2075 | 301 | 7-1 | 2026-09-12 |
| Lightweight | 1 | Ilia Topuria | 2274 | 296 | 9-1 | 2026-06-14 |
|  | 2 | Justin Gaethje | 2193 | 240 | 11-5 | 2026-06-14 |
|  | 3 | Charles Oliveira | 2146 | 212 | 25-11 | 2026-03-07 |
|  | 4 | Arman Tsarukyan | 2148 | 267 | 11-2 | 2026-09-19 |
|  | 5 | Dustin Poirier | 2096 | 230 | 22-9 | 2025-07-19 |
| Welterweight | 1 | Islam Makhachev | 2278 | 233 | 18-1 | 2026-08-15 |
|  | 2 | Shavkat Rakhmonov | 2401 | 407 | 7-0 | 2024-12-07 |
|  | 3 | Max Holloway | 2190 | 211 | 24-9 | 2026-07-11 |
|  | 4 | Carlos Prates | 2236 | 282 | 7-1 | 2026-05-02 |
|  | 5 | Michael Morales | 2245 | 323 | 7-0 | 2025-11-15 |
| Middleweight | 1 | Dricus Du Plessis | 2231 | 253 | 10-1 | 2026-07-18 |
|  | 2 | Khamzat Chimaev | 2255 | 278 | 9-1 | 2026-05-09 |
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
|  | 4 | Alexander Volkov | 2247 | 230 | 15-5 | 2026-10-24 |
|  | 5 | Alex Pereira | 2268 | 255 | 10-3 | 2026-06-14 |
| Women's Strawweight | 1 | Tatiana Suarez | 2011 | 315 | 9-1 | 2026-04-11 |
|  | 2 | Virna Jandiroba | 1841 | 252 | 9-4 | 2026-04-04 |
|  | 3 | Mackenzie Dern | 1797 | 230 | 12-5 | 2026-08-15 |
|  | 4 | Gillian Robertson | 1785 | 231 | 14-7 | 2026-08-15 |
|  | 5 | Jessica Andrade | 1753 | 221 | 17-13 | 2025-08-16 |
| Women's Flyweight | 1 | Valentina Shevchenko | 1998 | 255 | 15-3-1 | 2025-11-15 |
|  | 2 | Zhang Weili | 1981 | 258 | 10-3 | 2025-11-15 |
|  | 3 | Erin Blanchfield | 1984 | 285 | 8-2 | 2026-10-17 |
|  | 4 | Natalia Silva | 2007 | 311 | 9-0 | 2026-10-03 |
|  | 5 | Manon Fiorot | 1961 | 288 | 8-2 | 2026-09-12 |
| Women's Bantamweight | 1 | Kayla Harrison | 2075 | 468 | 3-0 | 2025-06-07 |
|  | 2 | Luana Santos | 1846 | 322 | 7-1 | 2026-10-31 |
|  | 3 | Ketlen Vieira | 1773 | 250 | 10-5 | 2026-05-16 |
|  | 4 | Julianna Pena | 1821 | 307 | 8-4 | 2025-06-07 |
|  | 5 | Norma Dumont | 1743 | 260 | 9-4 | 2026-09-26 |

## Current model fit

- Fitted on 5356 fights from 2016–2026.
- Market blend: 81% weight on the de-vigged price, total slope 1.28 (above 1 stretches favorites, correcting the favorite-longshot bias). Without a price: slope 1.02 on the model alone.
- Strongest win-model inputs (log-odds per standard deviation, A minus B): age -0.28, glicko_logit +0.21, strike_matchup +0.18, debut -0.12, age_decline -0.11, sapm -0.09.
