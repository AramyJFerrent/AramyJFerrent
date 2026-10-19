# UFC fight predictions

Updated Mon Oct 19, 2026 04:47 AM ET. Refreshed automatically every day and several times on fight week; each bout's prediction is locked when its part of the card starts and graded once the result is in.

Each bout gets one consistent breakdown: each fighter's chance to win, split into KO/TKO, submission and decision, and the chance it ends in each round. The win chance blends the model with the betting market (about 81% market, the weight that has predicted best on past fights) and corrects the market's habit of underrating heavy favorites. MMA is high-variance: even the most likely single result is usually well under 50%.

The fair odds are the American odds that match the win chance with no bookmaker margin: -200 means risk $200 to win $100, +200 means risk $100 to win $200. A sportsbook only offers value on a fighter when its price beats the fair line.

Value vs. price flags a fighter whose price implies a chance at least 2 points below the final win chance, bookmaker margin included. In the walk-forward backtest these bets made money, mostly by backing favorites the market underrates (see backtest.md), but on approximate closing prices; treat it as an experiment, tracked live below.

No upcoming bouts found on the next cards yet.

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
|  | 4 | Carlos Prates | 2236 | 281 | 7-1 | 2026-05-02 |
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
