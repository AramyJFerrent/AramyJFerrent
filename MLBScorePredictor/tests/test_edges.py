import numpy as np
import pandas as pd
import pytest

from bettingcore import EDGE_MIN_EV, best_side, expected_value

from mlbpredictor.edges import EDGE_COLUMNS, add_edges, edge_record, grade_pick, market_options


def game(**kw):
    """A game with the given model-only chances; the final rule's (``edge_*``) match them unless set."""
    row = {"game_id": "g", "home_team": "NYY", "away_team": "BOS", "model_home_prob": 0.6, "home_moneyline": np.nan,
           "away_moneyline": np.nan, "home_run_line": np.nan, "home_run_line_price": np.nan,
           "away_run_line_price": np.nan, "model_home_cover_prob": np.nan, "model_away_cover_prob": np.nan,
           "total_line": np.nan, "over_price": np.nan, "under_price": np.nan, "model_over_prob": np.nan,
           "model_under_prob": np.nan, "model_total_push_prob": np.nan, "home_score": np.nan, "away_score": np.nan}
    row.update(kw)
    for edge, model in (("edge_home_ml_prob", "model_home_prob"), ("edge_home_cover_prob", "model_home_cover_prob"),
                        ("edge_away_cover_prob", "model_away_cover_prob"), ("edge_over_prob", "model_over_prob"),
                        ("edge_under_prob", "model_under_prob"), ("edge_total_push_prob", "model_total_push_prob")):
        row.setdefault(edge, row[model])
    return row


def test_three_percent_bar():
    opts = [{"label": "NYY", "side": "home", "price": -120, "prob": 0.56},
            {"label": "BOS", "side": "away", "price": 110, "prob": 0.44}]
    assert best_side(opts) is None                                      # EV +2.7% and -7.6%
    assert expected_value(0.5, 0, 106) == pytest.approx(EDGE_MIN_EV)
    assert best_side([{"label": "BOS", "side": "away", "price": 106, "prob": 0.5}]) is not None   # at the bar
    # The final rule and the model-only rule read different chances.
    r = game(home_moneyline=110, away_moneyline=-130, model_home_prob=0.55, edge_home_ml_prob=0.45)
    assert add_edges(pd.DataFrame([r])).loc[0, "moneyline_edge_pick"] == ""
    assert add_edges(pd.DataFrame([r]), chances="model").loc[0, "moneyline_edge_pick"] == "NYY"


def test_run_line_uses_posted_side_and_never_assumes_a_price():
    # Away team favored: home +1.5 at -170, away -1.5 at +150.
    r = game(home_run_line=1.5, home_run_line_price=-170, away_run_line_price=150, model_home_cover_prob=0.55,
             model_away_cover_prob=0.45)
    opts = market_options(r)["spread"]
    assert [o["label"] for o in opts] == ["NYY +1.5", "BOS -1.5"] and opts[1]["line"] == -1.5
    pick = best_side(opts)
    assert pick["pick"] == "BOS -1.5" and np.isclose(pick["ev"], 0.45 * 1.5 - 0.55)
    # Without a price there is nothing to bet: no option, so no edge.
    assert market_options(game(home_run_line=-1.5, model_home_cover_prob=0.5, model_away_cover_prob=0.5))[
        "spread"] == []
    assert market_options(game(model_home_prob=0.7))["moneyline"] == []


def test_total_price_assumed_only_when_missing():
    r = game(total_line=8.0, model_over_prob=0.50, model_under_prob=0.42, model_total_push_prob=0.08)
    opts = market_options(r)["total"]
    assert all(o["assumed"] and o["price"] == -110 for o in opts) and opts[0]["push"] == 0.08
    pick = best_side(opts)
    assert pick["pick"] == "Over 8" and np.isclose(pick["ev"], 0.5 * 100 / 110 - 0.42)
    posted = market_options(game(total_line=8.5, over_price=-105, under_price=-115, model_over_prob=0.5,
                                 model_under_prob=0.5))["total"]
    assert [o["price"] for o in posted] == [-105, -115] and not any(o["assumed"] for o in posted)


def test_add_edges_grading_and_record():
    rows = pd.DataFrame([
        game(home_moneyline=110, away_moneyline=-130, model_home_prob=0.55, home_score=5, away_score=3),
        game(home_moneyline=-150, away_moneyline=130, model_home_prob=0.6, home_score=2, away_score=3),
        game(total_line=8.0, over_price=-110, under_price=-110, model_over_prob=0.56, model_under_prob=0.37,
             model_total_push_prob=0.07, home_score=5, away_score=3),
        game(home_run_line=-1.5, home_run_line_price=140, away_run_line_price=-160, model_home_cover_prob=0.45,
             model_away_cover_prob=0.55, home_score=4, away_score=3),
    ])
    out = add_edges(rows)
    assert set(EDGE_COLUMNS) <= set(out.columns)
    assert out.loc[0, "moneyline_edge_pick"] == "NYY" and out.loc[0, "moneyline_edge_price"] == 110
    assert out.loc[1, "moneyline_edge_pick"] == ""                       # -150 on a 60% team is break-even
    assert out.loc[2, "total_edge_pick"] == "Over 8" and out.loc[2, "total_edge_side"] == "over"
    assert out.loc[3, "spread_edge_pick"] == "NYY -1.5" and np.isclose(out.loc[3, "spread_edge_ev"], 0.08)
    ml, tot, rl = (edge_record(out, m) for m in ("moneyline", "total", "spread"))
    assert (ml["bets"], ml["wins"], ml["roi"]) == (1, 1, pytest.approx(1.1))
    assert np.isclose(ml["units"], 1.1 * out.loc[0, "moneyline_edge_stake"])
    assert (tot["wins"], tot["losses"], tot["pushes"], tot["units"]) == (0, 0, 1, 0.0)
    assert (rl["wins"], rl["losses"], rl["roi"]) == (0, 1, -1.0)                 # won by one: no cover


def test_grade_pick():
    assert grade_pick("spread", "away", 1.5, -180, 4, 3) == ("W", pytest.approx(100 / 180))
    assert grade_pick("spread", "home", -1.5, 130, 4, 3) == ("L", -1.0)
    assert grade_pick("total", "under", 9.0, -110, 5, 4) == ("P", 0.0)
    assert grade_pick("total", "under", 9.5, 105, 5, 4) == ("W", pytest.approx(1.05))
    assert grade_pick("moneyline", "away", np.nan, 120, 2, 6) == ("W", pytest.approx(1.2))


def test_archive_lines_map_teams_and_keep_priced_run_lines(monkeypatch):
    from bettingcore import sbr

    from mlbpredictor import backtest

    rows = [{"date": 20160405, "season": 2016, "home_team": "Yankees", "away_team": "Red Sox", "home_final": 5,
             "away_final": 3, "home_open_ml": -140, "away_open_ml": 120, "home_close_ml": -150, "away_close_ml": 130,
             "home_close_spread": -1.5, "home_close_spread_odds": 135, "away_close_spread_odds": -155,
             "open_over_under": 8.5, "close_over_under": 8.0},
            # Odds-less run line (stored as zeros) and an unknown team: no run line; the second never matches.
            {"date": 20160406, "season": 2016, "home_team": "SFO", "away_team": "LOS", "home_final": 2,
             "away_final": 1, "home_open_ml": 105, "away_open_ml": -125, "home_close_ml": 110, "away_close_ml": -130,
             "home_close_spread": 1.5, "home_close_spread_odds": 0, "away_close_spread_odds": 0,
             "open_over_under": 7.0, "close_over_under": 7.5},
            {"date": 20160406, "season": 2016, "home_team": "Expos", "away_team": "Mets", "home_final": 1,
             "away_final": 0, "home_close_ml": 100, "away_close_ml": -120}]
    monkeypatch.setattr(sbr, "load_archive", lambda sport, cache_dir, max_age_hours: sbr.parse(rows))
    games = pd.DataFrame({"game_id": ["a", "b", "c"], "date": ["2016-04-05", "2016-04-07", "2016-04-06"],
                          "home_team": ["NYY", "SF", "WSH"], "away_team": ["BOS", "LAD", "NYM"],
                          "home_score": [5, 2, 1], "away_score": [3, 1, 0]})
    out = backtest.archive_lines(games)
    assert sorted(out.index) == ["a", "b"]
    a, b = out.loc["a"], out.loc["b"]
    assert (a["home_moneyline"], a["open_away_moneyline"], a["total_line"], a["open_total_line"]) == (-150, 120, 8.0, 8.5)
    assert (a["home_run_line"], a["home_run_line_price"], a["away_run_line_price"]) == (-1.5, 135, -155)
    assert np.isnan(b["home_run_line"]) and np.isnan(b["home_run_line_price"]) and b["away_moneyline"] == -130


def test_archive_section_lists_each_rule_and_line():
    from mlbpredictor.report import archive_section, backtest_edge_table

    rec = {"bets": 2, "wins": 1, "losses": 1, "pushes": 0, "staked": 3.0, "units": 0.4, "roi": 0.4 / 3,
           "roi_low": -0.5, "roi_high": 0.7, "expected_roi": 0.05}
    none = {"bets": 0, "wins": 0, "losses": 0, "pushes": 0, "staked": 0.0, "units": 0.0, "roi": np.nan,
            "roi_low": np.nan, "roi_high": np.nan, "expected_roi": np.nan}
    loss = np.array([0.68, 0.66])
    archive = {"games": 2, "seasons": (2016, 2021), "rate_seasons": (2015, 2021), "all_weight": 0.21,
               "all_games": 14000, "weights": {2016: 0.1, 2017: 0.25},
               "losses": {"model": loss, "open": loss, "close": loss, "blend": loss},
               "bootstrap": {"Model vs closing line": (0.001, -0.002, 0.004)},
               "edges": {("closing", "final", "moneyline"): rec, ("opening", "model", "total"): none}}
    text = "\n".join(archive_section(archive))
    assert "## Against the betting market, 2016 to 2021" in text
    assert "(2016 10%, 2017 25%)" in text and "it is 21%: the live predictor's starting weight" in text
    assert "| Moneyline, closing line, final prediction | 2 | 1-1-0 | 3.0 | +0.40 | +13.3% | +5.0% | -50.0% to +70.0% |" in text
    assert "| Total (-110 assumed), opening line, model only | 0 | 0-0-0 | 0.0 | +0.00 | – | – | – |" in text
    assert archive_section({"all_weight": 0.2}) == []
    assert "| Run line | no historical prices |" in backtest_edge_table({"Run line": None})
