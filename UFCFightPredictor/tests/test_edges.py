import numpy as np
import pandas as pd
import pytest

from ufcpredictor import pipeline
from ufcpredictor.backtest import edge_bets, edge_summary
from ufcpredictor.cards import attach_core_odds, parse_core_props, parse_espn, parse_props, round_total
from ufcpredictor.edges import (EDGE_COLUMNS, EDGE_MIN_EV, attach_edges, best_side, decimal_odds, edge_cell,
                                expected_value, fair_american, fair_round_line, implied_prob, outcome, over_prob,
                                record, settle)
from ufcpredictor.model import MODEL_ONLY, FightModel
from ufcpredictor.pipeline import LOG_COLUMNS, prediction_rows
from ufcpredictor.report import edge_records, upcoming_tables

from test_cards import espn_payload
from test_model import synthetic

NOW = pd.Timestamp("2026-10-22 12:00", tz="UTC")


# ---- price math ---------------------------------------------------------------

def test_decimal_implied_and_fair_odds():
    assert decimal_odds(150) == 2.5 and decimal_odds(-200) == 1.5 and decimal_odds(100) == 2.0
    assert np.allclose(decimal_odds([150, -200]), [2.5, 1.5])
    assert abs(implied_prob(-200) - 2 / 3) < 1e-12 and implied_prob(300) == 0.25
    assert fair_american(0.75) == -300 and fair_american(0.25) == 300 and fair_american(0.5) == 100
    assert fair_american(0.6) == -150 and fair_american(0.4) == 150


def test_expected_value_with_and_without_pushes():
    assert abs(expected_value(0.5, 0.0, 100)) < 1e-12                     # fair coin at even money
    assert abs(expected_value(0.55, 0.0, -110) - (0.55 * 100 / 110 - 0.45)) < 1e-12
    # A push returns the stake: only the losing share costs.
    assert abs(expected_value(0.5, 0.1, 100) - (0.5 - 0.4)) < 1e-12
    assert settle("win", 150) == 1.5 and settle("win", -200) == 0.5
    assert settle("loss", 150) == -1.0 and settle("push", 150) == 0.0


def test_best_side_needs_three_percent():
    opts = [{"label": "Lee", "side": "a", "prob": 0.42, "price": 150},          # EV +5%
            {"label": "Cruz", "side": "b", "prob": 0.58, "price": -180}]        # EV -9.8%
    pick = best_side(opts)
    assert pick.side == "a" and abs(pick.ev - 0.05) < 1e-12 and not pick.assumed
    assert pick.cell() == "Lee (+150): EV +5.0%, model 42%"
    opts[0]["prob"] = 0.41                                                      # EV +2.5%: below the bar
    assert best_side(opts) is None
    assert best_side(opts, min_ev=0.02).side == "a"
    assert EDGE_MIN_EV == 0.03
    # A side without a price is skipped, not assumed.
    assert best_side([{"label": "Lee", "side": "a", "prob": 0.9, "price": np.nan}]) is None


# ---- round totals ---------------------------------------------------------------

def test_round_over_probability():
    by_round = [0.2, 0.15, 0.1, 0.0, 0.0]
    dist = 0.55
    # Over 1.5: survives round 1, and round 2 past 2:30 (half its finishes), or later.
    assert abs(over_prob(by_round, dist, 3, 1.5) - (0.55 + 0.1 + 0.075)) < 1e-12
    assert abs(over_prob(by_round, dist, 3, 0.5) - (1 - 0.1)) < 1e-12
    assert abs(over_prob(by_round, dist, 3, 2.5) - (0.55 + 0.05)) < 1e-12      # a decision is always over
    assert np.isnan(over_prob(by_round, dist, 3, 3.5))                           # beyond three rounds
    assert np.isnan(over_prob(by_round, dist, 3, 2.0))                           # not an x.5 line
    five = [0.15, 0.12, 0.1, 0.08, 0.05]
    assert abs(over_prob(five, 0.5, 5, 4.5) - (0.5 + 0.025)) < 1e-12
    line, p = fair_round_line(by_round, dist, 3)
    assert line == 2.5 and abs(p - 0.6) < 1e-12


# ---- model-only probabilities -----------------------------------------------------

def test_model_only_outcomes_rerun_the_method_and_round_models():
    f = synthetic()
    model = FightModel.fit(f, ridge=10.0)
    head = f.head(200).reset_index(drop=True)
    out = model.predict(head)
    six = out[[c for c in MODEL_ONLY if c[6:7] in "ab" and c.count("_") == 2]]
    assert six.shape[1] == 6 and np.allclose(six.sum(axis=1), 1.0)
    assert np.allclose(out[["model_a_ko", "model_a_sub", "model_a_dec"]].sum(axis=1), out["p_model"])
    assert np.allclose(out["model_distance"], out["model_a_dec"] + out["model_b_dec"])
    rounds = out[[f"model_r{r}" for r in range(1, 6)]].sum(axis=1)
    assert np.allclose(rounds, 1 - out["model_distance"], atol=1e-3)
    # The split is the method model rerun on the model's own log-odds, not the blended split rescaled.
    z_own = model.calibration.model_slope * model.win.logit(head)
    split = model.method.split(head, "a", z_own)
    assert np.allclose(out["model_a_ko"], out["p_model"] * split[:, 0])
    # The blended outputs are unchanged.
    assert np.allclose(out[["a_ko", "a_sub", "a_dec"]].sum(axis=1), out["p_a"])


# ---- ESPN prices ------------------------------------------------------------------

def test_round_total_from_scoreboard_formats():
    assert round_total({"overUnder": 1.5, "overOdds": -150, "underOdds": 125}) == (1.5, -150.0, 125.0)
    nested = {"total": {"over": {"close": {"line": "o2.5", "odds": "-110"}},
                        "under": {"close": {"line": "u2.5", "odds": "-120"}}}}
    assert round_total(nested) == (2.5, -110.0, -120.0)
    line, over, under = round_total({"overUnder": 225.5})               # not a round line
    assert np.isnan(line) and np.isnan(over)
    row = parse_espn(espn_payload({"homeAthleteOdds": {"moneyLine": 200}, "awayAthleteOdds": {"moneyLine": -250},
                                   "overUnder": 3.5, "overOdds": 105, "underOdds": -135})).set_index("espn_id")
    assert (row.loc["401", "rounds_line"], row.loc["401", "over_price"], row.loc["401", "under_price"]) == \
        (3.5, 105.0, -135.0)


ATH = "http://sports.core.api.espn.com/v2/sports/mma/athletes/{}?lang=en"
PROP_BETS = [
    {"type": {"name": "Fight Result - Method of Victory"}, "name": "Smith by KO/TKO",
     "athlete": {"$ref": ATH.format(11)}, "odds": {"american": {"value": "+250"}}},
    {"type": {"name": "Method of Victory"}, "name": "Smith by Submission",
     "athlete": {"$ref": ATH.format(11)}, "odds": {"american": {"value": "+900"}}},
    {"type": {"name": "Method of Victory"}, "name": "Smith by Decision", "athlete": {"$ref": ATH.format(11)},
     "odds": {"american": {"value": "+200"}}},
    {"type": {"name": "Method of Victory"}, "name": "Jones by KO/TKO", "athlete": {"$ref": ATH.format(22)},
     "odds": {"american": {"value": "+150"}}},
    {"type": {"name": "Method of Victory"}, "name": "Jones by Decision", "athlete": {"$ref": ATH.format(22)},
     "odds": {"american": {"value": "+175"}}},
    # Not plain method markets: round-specific, or by unanimous decision.
    {"type": {"name": "Round Betting"}, "name": "Jones by KO in Round 1", "athlete": {"$ref": ATH.format(22)},
     "odds": {"american": {"value": "+600"}}},
    {"type": {"name": "Decision Type"}, "name": "Jones by Unanimous Decision",
     "athlete": {"$ref": ATH.format(22)}, "odds": {"american": {"value": "+250"}}},
    # Round totals: an alternate line and the main one, one item per side.
    {"type": {"name": "Total Rounds"}, "name": "Over 1.5", "current": {"target": {"value": 1.5}},
     "odds": {"american": {"value": "-250"}}},
    {"type": {"name": "Total Rounds"}, "name": "Under 1.5", "current": {"target": {"value": 1.5}},
     "odds": {"american": {"value": "+190"}}},
    {"type": {"name": "Total Rounds"}, "name": "Over 2.5", "current": {"target": {"value": 2.5}},
     "odds": {"american": {"value": "-115"}}},
    {"type": {"name": "Total Rounds"}, "name": "Under 2.5", "current": {"target": {"value": 2.5}},
     "odds": {"american": {"value": "-105"}}},
]


def test_prop_bets_parse_by_athlete_and_line():
    out = parse_props(PROP_BETS, ("11", "22"), ("John Smith", "Jon Jones"))
    assert (out["odds_a_ko"], out["odds_a_sub"], out["odds_a_dec"]) == (250.0, 900.0, 200.0)
    assert (out["odds_b_ko"], out["odds_b_dec"]) == (150.0, 175.0) and np.isnan(out["odds_b_sub"])
    assert (out["rounds_line"], out["over_price"], out["under_price"]) == (2.5, -115.0, -105.0)   # main line
    flipped = parse_props(PROP_BETS, ("22", "11"))
    assert flipped["odds_a_ko"] == 150.0 and flipped["odds_b_sub"] == 900.0
    # One item carrying both sides of the total.
    both = parse_props([{"name": "Total Rounds", "line": 1.5, "over": {"american": "-140"},
                         "under": {"american": "+110"}}], ("11", "22"))
    assert (both["rounds_line"], both["over_price"], both["under_price"]) == (1.5, -140.0, 110.0)
    assert np.isnan(parse_props([], ("11", "22"))["odds_a_ko"])


def test_core_odds_props_and_bounded_requests():
    link = "http://sports.core.api.espn.com/v2/sports/mma/leagues/ufc/events/9/competitions/401/odds/100/propBets"
    core = {"items": [
        {"provider": {"name": "DraftKings", "priority": 1}, "overUnder": 2.5, "overOdds": -120, "underOdds": 100,
         "propBets": {"$ref": link},
         "homeAthleteOdds": {"moneyLine": -180, "athlete": {"$ref": ATH.format(11)}},
         "awayAthleteOdds": {"moneyLine": 150, "athlete": {"$ref": ATH.format(22)}}}]}
    props, found = parse_core_props(core, ("11", "22"))
    assert found == link and (props["rounds_line"], props["over_price"]) == (2.5, -120.0)

    class Resp:
        def __init__(self, body):
            self.body = body

        def raise_for_status(self):
            pass

        def json(self):
            return self.body

    calls = []

    class Session:
        def get(self, url, **kw):
            calls.append(url)
            if url.endswith("/propBets"):
                return Resp({"count": len(PROP_BETS), "items": PROP_BETS})
            return Resp(core if "/competitions/401/odds" in url else {"items": []})

    espn = parse_espn(espn_payload({"homeAthleteOdds": {"moneyLine": 200}, "awayAthleteOdds": {"moneyLine": -250}}))
    espn.loc[espn["espn_id"] == "401", ["espn_a", "espn_b"]] = ["11", "22"]
    out = attach_core_odds(espn, Session()).set_index("espn_id")
    assert out.loc["401", "odds_a"] == 200.0                     # the scoreboard's moneyline stands
    assert out.loc["401", "odds_a_ko"] == 250.0 and out.loc["401", "odds_b_dec"] == 175.0
    assert (out.loc["401", "rounds_line"], out.loc["401", "under_price"]) == (2.5, 100.0)   # from the odds item
    assert sum(c.endswith("/propBets") for c in calls) == 1 and len(calls) == 2


# ---- log, edges and rendering --------------------------------------------------------

def log_row(**kw):
    row = {c: np.nan for c in LOG_COLUMNS}
    row.update(bout_key="k1", event="UFC Fight Night", order=0, date=pd.Timestamp("2026-10-24"),
               start=pd.Timestamp("2026-10-24 23:00", tz="UTC"), division="Lightweight", rounds=3, title=False,
               fighter_a="Ann Lee", fighter_b="Bea Cruz", a_id="a", b_id="b", p_a=0.5, p_model=0.45,
               p_market=0.55, a_ko=0.2, a_sub=0.05, a_dec=0.25, b_ko=0.15, b_sub=0.05, b_dec=0.3, p_distance=0.55,
               r1=0.2, r2=0.15, r3=0.1, r4=0.0, r5=0.0, best_side="b", best_method="dec", best_prob=0.3,
               model_a_ko=0.18, model_a_sub=0.05, model_a_dec=0.22, model_b_ko=0.17, model_b_sub=0.06,
               model_b_dec=0.32, model_distance=0.54, model_r1=0.2, model_r2=0.16, model_r3=0.1, model_r4=0.0,
               model_r5=0.0, odds_a=150.0, odds_b=-180.0, source="live", status="upcoming",
               predicted_at=NOW)
    row.update(kw)
    return row


def test_edges_are_attached_to_rows_and_rendered():
    rows = attach_edges(pd.DataFrame([log_row(odds_a_ko=500.0, odds_b_ko=400.0, rounds_line=1.5,
                                              over_price=-300.0, under_price=230.0)]))
    r = rows.iloc[0]
    assert r.moneyline_edge_side == "a" and abs(r.moneyline_edge_ev - (0.45 * 1.5 - 0.55)) < 1e-12
    assert r.moneyline_edge_pick == "Lee"
    assert r.method_edge_side == "a_ko" and r.method_edge_pick == "Lee by KO/TKO"     # 18% at +500: EV +8%
    # Over 1.5 = 0.54 + 0.1 + 0.08 = 72% at -300 (75%): no edge; under 28% at +230: EV -7.6%.
    assert abs(r.model_over_prob - 0.72) < 1e-12 and pd.isna(r.rounds_edge_pick)
    tup = next(rows.itertuples(index=False))
    assert edge_cell(tup, "moneyline") == "Lee (+150): EV +12.5%, model 45%"
    assert edge_cell(tup, "rounds") == "no edge"
    assert edge_cell(tup, "method").startswith("Lee by KO/TKO (+500): EV +8.0%")

    # No prices at all: no line for the moneyline, the model's fair odds for the props, never -110.
    bare = next(attach_edges(pd.DataFrame([log_row(odds_a=np.nan, odds_b=np.nan)])).itertuples(index=False))
    assert edge_cell(bare, "moneyline") == "no line yet"
    assert edge_cell(bare, "rounds") == "no price yet; fair Over 2.5 -145, Under +145"
    assert edge_cell(bare, "method").startswith("no prices yet; fair KO / Sub / Dec<br>Lee +455 / +1900 / +355")
    page = upcoming_tables(attach_edges(pd.DataFrame([log_row(a_fights=3, b_fights=4)])))
    assert "| Moneyline edge | Round total edge | Method edge |" in page and "-110" not in page
    assert "Lee 45% (+120)" in page                                         # model alone with its fair odds


def test_log_round_trip_and_old_logs(tmp_path, monkeypatch):
    monkeypatch.setattr(pipeline, "LOG_PATH", tmp_path / "log.csv")
    feats = pd.DataFrame([log_row(odds_a_ko=500.0)])
    preds = feats[pipeline.PRED_COLUMNS]
    rows = prediction_rows(feats, preds, NOW, "live")
    assert list(rows.columns) == LOG_COLUMNS and set(EDGE_COLUMNS) <= set(rows.columns)
    saved = rows.copy()
    for col in pipeline.TIME_COLUMNS:
        saved[col] = saved[col].map(lambda t: t.isoformat() if not pd.isna(t) else "")
    saved.to_csv(pipeline.LOG_PATH, index=False)
    back = pipeline.load_log().iloc[0]
    assert back.moneyline_edge_pick == "Lee" and back.method_edge_side == "a_ko"
    assert back.odds_a_ko == 500.0 and pd.isna(back.rounds_edge_pick)
    # A log written before these columns existed still loads, with NaN for them.
    old_cols = LOG_COLUMNS[:LOG_COLUMNS.index("end_round") + 1]
    saved[old_cols].to_csv(pipeline.LOG_PATH, index=False)
    old = pipeline.load_log()
    assert list(old.columns) == LOG_COLUMNS and old["method_edge_pick"].isna().all()
    assert old["model_over_prob"].isna().all()


# ---- grading ------------------------------------------------------------------------

def test_outcomes_for_each_market():
    assert outcome("moneyline", "a", np.nan, "final", "a", "KO", 1, 30) == "win"
    assert outcome("moneyline", "b", np.nan, "final", "a", "KO", 1, 30) == "loss"
    assert outcome("moneyline", "a", np.nan, "draw", "draw", "DEC", 3, 300) == "push"
    assert outcome("method", "a_ko", np.nan, "final", "a", "KO", 1, 30) == "win"
    assert outcome("method", "a_dec", np.nan, "final", "a", "KO", 1, 30) == "loss"
    assert outcome("method", "a_dec", np.nan, "draw", "draw", "DEC", 3, 300) == "loss"
    assert outcome("method", "a_ko", np.nan, "upcoming", np.nan, np.nan, np.nan, np.nan) is None
    # Round totals: over 1.5 needs 2:30 of round 2.
    assert outcome("rounds", "over", 1.5, "final", "a", "KO", 2, 151) == "win"
    assert outcome("rounds", "over", 1.5, "final", "a", "KO", 2, 150) == "win"          # exactly 2:30 counts
    assert outcome("rounds", "over", 1.5, "final", "a", "SUB", 2, 149) == "loss"
    assert outcome("rounds", "under", 1.5, "final", "a", "KO", 1, 299) == "win"
    assert outcome("rounds", "over", 2.5, "final", "b", "DEC", 3, 300) == "win"          # the distance is over
    assert outcome("rounds", "over", 1.5, "final", "a", "KO", 2, np.nan) is None         # no time: ungraded
    for market, side in (("moneyline", "a"), ("method", "a_ko"), ("rounds", "over")):
        assert outcome(market, side, 1.5, "no contest", "nc", "Other", 1, 60) == "push"


def test_edge_record_counts_settled_picks():
    rows = attach_edges(pd.DataFrame([
        log_row(bout_key="k1", status="final", winner="a", method="KO", end_round=1, end_seconds=40.0),
        log_row(bout_key="k2", status="final", winner="b", method="DEC", end_round=3, end_seconds=300.0),
        log_row(bout_key="k3", status="no contest", winner="nc", method="Other", end_round=1, end_seconds=20.0),
        log_row(bout_key="k4"),                                                 # not fought yet
    ]))
    r = record(rows, "moneyline")
    assert (r["edges"], r["wins"], r["losses"], r["pushes"]) == (3, 1, 1, 1)
    assert abs(r["units"] - 0.5) < 1e-12 and abs(r["roi"] - 0.5 / 3) < 1e-12
    table = edge_records(rows)
    assert "| Moneyline | 3 | 1-1-1 | +0.50 | +16.7% |" in table
    assert "| Round total | 0 | 0-0-0 | +0.00 | – |" in table


def test_backtest_edges_use_model_alone_and_dataset_prices():
    book = dict(odds_a_ko=500.0, odds_a_sub=1200.0, odds_a_dec=250.0, odds_b_ko=450.0, odds_b_sub=1000.0,
                odds_b_dec=200.0)                                            # 113.5% implied: a real book
    bt = pd.DataFrame([log_row(winner="a", method="KO", end_round=1, **book),
                       log_row(winner="b", method="DEC", end_round=3, odds_a_ko=500.0),   # 17% implied: dropped
                       log_row(winner="a", method="DEC", end_round=3, odds_a=np.nan, odds_b=np.nan)])
    bets = edge_bets(bt)
    ml = bets[bets["market"] == "moneyline"]
    assert len(ml) == 2 and list(ml["result"]) == ["win", "loss"]
    method = bets[bets["market"] == "method"]
    assert list(method["side"]) == ["a_ko"] and list(method["result"]) == ["win"]
    summary = edge_summary(bt, bets, n=200).set_index("market")
    assert summary.loc["moneyline", "fights"] == 2 and summary.loc["moneyline", "edges"] == 2
    assert summary.loc["moneyline", "units"] == pytest.approx(0.5)
    assert summary.loc["method", "fights"] == 1
    assert summary.loc["rounds", "fights"] == 0                              # no historical round prices
