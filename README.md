# Sports Predictors

Self-updating models that predict the outcome of every game in six sports: the NFL, college football (FBS), the NBA, MLB, the NHL and the UFC. Each one rates teams or fighters from detailed historical data, blends its own view with the betting market, and simulates every game or bout thousands of times to produce a full forecast, not just a pick. Scheduled GitHub Actions keep the data, the models and the predictions current through each season, and every predictor grades its own finished games and is scored by a walk-forward backtest against the betting market or a strong baseline such as Elo.

| Predictor | Predicts | Betting edges | Latest predictions | Backtest |
| --- | --- | --- | --- | --- |
| [NFL](NFLScorePredictor) | Final score, win probability, 80% points range | Spread, moneyline, total | [Predictions](NFLScorePredictor/predictions/README.md) | 2015–2025 |
| [College football](CollegeFootballScorePredictor) | Final score, win probability, 80% points range | Spread, moneyline, total | [Predictions](CollegeFootballScorePredictor/predictions/README.md) | 2016–2025 |
| [NBA](NBAScorePredictor) | Final score, win probability, overtime, spread and total, missing players, 80% points range | Spread, moneyline, total | [Predictions](NBAScorePredictor/predictions/README.md) | 2015-16 – 2025-26 |
| [MLB](MLBScorePredictor) | Final score, win probability, extra innings, run line, 80% runs range | Run line, moneyline, total | [Predictions](MLBScorePredictor/predictions/README.md) | 2016–2025 |
| [NHL](NHLScorePredictor) | Final score, win probability, overtime, 80% goals range | Puck line, moneyline, total | [Predictions](NHLScorePredictor/predictions/README.md) | 2016-17 – 2025-26 |
| [UFC](UFCFightPredictor) | Win probability by KO/TKO, submission and decision, and by round | Moneyline, round total, method of victory | [Predictions](UFCFightPredictor/predictions/README.md) | 2015–2026 |

## Betting edges

Every predictions page also says, for each game or bout, whether there is an edge in each market in the table above, and how much to stake on it. All six predictors price edges the same way, through the shared [BettingCore](BettingCore) package:

- **The forecast on the page prices the bet.** Each side's chance comes from the final prediction: the model blended with the betting line by the weight that predicted best on earlier seasons (fitted out of sample, so a model that has not beaten the market gets little say), not from the model alone.
- **Anchored to the market.** That chance is the market's own de-vigged chance plus how far the blend moves it, measured by simulating the game twice with the same random draws, once at the blend and once at the line. So the simulator's shape cannot pose as an edge, only real disagreement with the market can.
- **Edge and stake.** A side is an edge when its expected return at the posted price is at least 3% of the stake. It is staked at a quarter of the Kelly stake, in units of 1% of the bankroll, with at most 3 units on one game across its markets, since they tend to win or lose together.
- Posted prices are used wherever the source gives them; a spread or total without one is assumed to be -110 (and marked), and any other market without a price shows fair odds instead. NHL edges wait for both starting goalies to be confirmed, and college football has none in bowl games outside the playoff (opt-outs).
- Each edge is frozen at the last price before the game, graded afterward and tallied by market: units staked and won, ROI, and expected ROI (what the edges' EVs promised). Each backtest scores the same rule wherever historical prices exist, including the free sportsbookreview archive of 2011-2021 lines for MLB, the NHL and NFL openers, next to the old rule (the model alone, before the blend) for comparison.

What the backtests found at the closing line, the price the pages bet:

| Predictor | Edges per season | Final-prediction edges | Old rule (model alone) |
| --- | --- | --- | --- |
| NFL | about 70 | Totals +7.9%, spreads and moneylines negative; no range clear of zero | Spreads about break-even, moneylines and totals −2% to −4% |
| College football | about 90 | Spreads −8%, totals +2%, moneylines +12% on long underdogs; no range clear of zero | Spreads −4.4% (clearly negative) |
| NBA | about 300 | Moneylines +11.5% (+3.4% to +19.2%), almost all underdogs; spreads and totals slightly negative | Spreads and totals −4% (clearly negative) |
| MLB | almost none | 16 edges in six seasons: the blend is 9% model | Run lines −2.9%, moneylines and totals about break-even |
| NHL | about 1,000 | Every market slightly ahead (+0.7% to +2.4%); no range clear of zero | Puck lines −2.7%, totals +2.5% |
| UFC | about 80 bouts | Moneylines +5.1% (−1.3% to +11.4%) | Moneylines −6.0% (clearly negative) |

The old rule lost in almost every sport, because the model alone disagrees with the market on most games and most of that disagreement is noise; the new rule bets far less often. Its results are mostly within noise of break-even, with the NBA's underdog moneylines the one market whose range clears zero, so treat the edges as an experiment, not betting advice. Several backtests also bet into the opening line, where the model alone did better (NHL and NBA moneylines, MLB and college football totals), but the pages bet the last price before the game, not the opener.

## Running a predictor

Each predictor is a Python 3.12 package in its own folder; its requirements also install the shared [BettingCore](BettingCore) package from this repository:

```bash
cd NFLScorePredictor            # or any other predictor folder
pip install -r requirements.txt
python -m nflpredictor update   # cfbpredictor, nbapredictor, mlbpredictor, nhlpredictor, ufcpredictor
```

See each predictor's README for its data sources, model details, backtest results and other commands. The workflows in [`.github/workflows`](.github/workflows) run the same `update` command on a schedule and commit the refreshed predictions.

## NFL

This Python project predicts the final score of every NFL game during the season, along with each team's win probability and an 80% range for its points. It rates every offense, defense and special-teams unit from opponent-adjusted play-by-play efficiency (EPA) using ridge regression toward a preseason prior, adjusts for the projected starting quarterback, home field, rest and forecast wind, blends the result with the betting line, and simulates each game 10,000 times drive by drive to get realistic scores. A scheduled GitHub Action refreshes the data, refits the model, re-predicts upcoming games and grades finished ones every day, so it keeps itself current through the season. A walk-forward backtest over 2015 to 2025 scores it against the closing betting line. See [NFLScorePredictor](NFLScorePredictor) and the [latest predictions](NFLScorePredictor/predictions/README.md).

## College football

This Python project predicts the final score of every FBS college football game during the season, along with each team's win probability and an 80% range for its points. It starts each team from a preseason prior fitted on past seasons (last year's rating, program history and returning production that counts transfer-portal arrivals), rates every offense, defense and special-teams unit from opponent-adjusted play-by-play efficiency (EPA) with garbage time removed, gives FCS opponents ratings of their own, blends the result with the betting line, and simulates each game 10,000 times drive by drive, overtime included, to get realistic scores. A scheduled GitHub Action refreshes the data, refits the model, re-predicts upcoming games and grades finished ones every day and several times on Saturdays, so it keeps itself current through the season. A walk-forward backtest over 2016 to 2025 scores it against the closing betting line, overall and by kind of game. See [CollegeFootballScorePredictor](CollegeFootballScorePredictor) and the [latest predictions](CollegeFootballScorePredictor/predictions/README.md).

## NBA

This Python project predicts the final score of every NBA game during the season, along with each team's win probability, the chance of overtime, the spread and total, the players each team will be missing and an 80% range for its points. It rates every player by regularized adjusted plus-minus on every lineup stint rebuilt from play-by-play, with garbage time removed and priors carried from season to season, projects tonight's minutes from each player's recent games and the injury report (weighing a questionable player by his chance of playing), turns that lineup into each team's expected possessions and points per possession alongside opponent-adjusted team efficiency, home court and back-to-backs, blends the margin and total with the betting line, and simulates each game 10,000 times from correlated scores weighted to real late-game margins, with overtime. A scheduled GitHub Action pulls new box scores and play-by-play, ESPN's injury report, rosters and lines several times a day around the injury report's deadlines, refits the model, re-predicts the next two days of games and grades finished ones, so it keeps itself current through the season. A walk-forward backtest over 2015-16 to 2025-26 scores it against the closing betting line, team ratings alone and Elo. See [NBAScorePredictor](NBAScorePredictor) and the [latest predictions](NBAScorePredictor/predictions/README.md).

## MLB

This Python project predicts the final score of every MLB game during the season, postseason included, along with each team's win probability, the chance of extra innings, the run line and an 80% range for its runs. It rates every batter and pitcher on each plate-appearance outcome (strikeouts, walks, singles through home runs) from park-adjusted, recency-weighted results shrunk toward the league by how fast each outcome stabilizes, matches tonight's lineup against the probable starter (with platoon splits) and against a bullpen weighted by recent use and rest, hands the game from starter to bullpen at the inning he is likely to leave, adds park, weather, home field and team ratings in a run model fitted inning by inning, blends with runs backed out of the betting line, and simulates each game 10,000 times through a base-out Markov chain built from Retrosheet play-by-play, with the skipped bottom of the ninth, walk-offs, closers and the extra-inning runner on second. A scheduled GitHub Action pulls new box scores, probable pitchers, posted lineups, weather and lines from the MLB Stats API, ESPN and Open-Meteo several times a day, refits the model, re-predicts the next two days of games and grades finished ones, so it keeps itself current through the season. A walk-forward backtest over 2016 to 2025 scores it against pitcher-adjusted Elo, Pinnacle's 2016 betting lines and sportsbookreview's archived 2016-2021 lines. See [MLBScorePredictor](MLBScorePredictor) and the [latest predictions](MLBScorePredictor/predictions/README.md).

## NHL

This Python project predicts the final score of every NHL game during the season, along with each team's win probability, the chance of overtime and an 80% range for its goals. It rates every team from score-and-venue-adjusted expected goals (from its own frozen shot model) and actual goals using ridge regression toward a preseason prior, values each starting goalie by goals saved above expected (projecting the starter from recent usage and back-to-backs when he is not yet named), adds home ice, rest and an Elo edge in a Poisson goal-rate model, blends the result with goal rates backed out of the betting line, and simulates each game 10,000 times minute by minute, with pulled goalies, empty-net goals, three-on-three overtime and shootouts. A scheduled GitHub Action refreshes the data, refits the model, re-predicts the next few days of games and grades finished ones several times a day, so it keeps itself current through the season. A walk-forward backtest over 2016-17 to 2025-26 scores it against Elo, a goals-only Poisson model and sportsbookreview's archived 2016-17 to 2021-22 lines. See [NHLScorePredictor](NHLScorePredictor) and the [latest predictions](NHLScorePredictor/predictions/README.md).

## UFC

This Python project predicts every bout on the upcoming UFC cards: each fighter's chance to win, split into KO/TKO, submission and decision, and the chance the fight ends in each round, all adding up to one consistent breakdown. It rates every fighter with Glicko-2 (whose uncertainty grows with layoffs), builds opponent-adjusted striking, grappling and durability profiles shrunk toward division averages, and feeds the differences between the two fighters (with age, reach, experience and matchup terms) into a calibrated, corner-symmetric logistic model. It blends that with the de-vigged moneyline on the log-odds scale, correcting the market's habit of underrating heavy favorites, then splits the win chance by method with division base rates and by round with a finish hazard. A scheduled GitHub Action refreshes UFCStats results, reads the next cards and prices, refits the model, re-predicts bouts that have not started (dropping ones that fall off a card) and grades finished ones every day and several times on fight week, so it keeps itself current year-round. A walk-forward backtest over 2015 to 2026 scores it against the betting market. See [UFCFightPredictor](UFCFightPredictor) and the [latest predictions](UFCFightPredictor/predictions/README.md).
