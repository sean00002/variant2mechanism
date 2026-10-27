"""Occupancy (spec 3, section 1) and screen v2 (section 2), on recorded fixtures and on stand-ins."""

import re
from pathlib import Path

import pandas as pd
import pytest

from variant2mechanism.context.base import Case
from variant2mechanism.context.http import Http
from variant2mechanism.context.occupancy import (
    NOT_SEQUENCE_SPECIFIC,
    Match,
    Occupancy,
    biosample_match,
    candidates,
    context_key,
    fetch,
    occupancy_results,
)
from variant2mechanism.qbic.screen import NO_PEAK, screen_v2
from variant2mechanism.qbic.variants import Variant

FIXTURES = Path(__file__).parent / "fixtures" / "http"
N = 997


def test_context_key_and_biosample_match():
    assert context_key("DepMap:ACH-000971 (HCT 116)") == "DepMap:ACH-000971"
    assert context_key("DepMap:subtype=Glioblastoma (median of 54 lines)") == "DepMap:subtype=Glioblastoma"
    assert context_key("none (embryonic craniofacial tissue; no matching dataset)") == "none"
    assert biosample_match("DepMap:ACH-000971 (HCT 116)").biosamples == ["HCT116"]
    hep = biosample_match("DepMap:ACH-000625 (Hep 3B2.1-7)")
    assert hep.biosamples == ["HepG2"] and "proxy" not in (hep.proxy or "proxy") and hep.proxy
    assert biosample_match("GTEx:Adipose - Subcutaneous (proxy for preadipocytes)").biosamples == []
    assert biosample_match("DepMap:ACH-999999 (new line)").key is None          # not listed: add it to biosample_match.yaml first
    assert Match("x", ["LNCaP clone FGC", "LNCaP"]).matches("LNCAP")


# -- stand-ins --------------------------------------------------------------------------------------------------


class Reg:
    """TFs A (own model a), B (own model b), C (mapped to a), EP300 (a mapped model, which must not matter)."""
    own_model = {"A": "a", "B": "b"}
    mapped_models = {"C": ["a"], "EP300": ["b"]}
    cognate_tf = {"a": "A", "b": "B"}

    def group_of_model(self, m):
        return {"id": f"G{m}", "label": f"Fam {m}"}

    def resolve_tf(self, label):
        return {"status": "ok", "symbol": label}


def peak(target, biosample, acc="ENCSR1"):
    return {"target": target, "biosample": biosample, "experiment_accession": acc, "chrom_start": 0, "chrom_end": 10}


def occ(peaks, assayed=None, biosamples=("HCT116",)):
    labels = {p["target"] for p in peaks} | set(assayed or {})
    return Occupancy("chr1:5:A>C", Match("k", list(biosamples)), peaks, assayed or {}, {x: x for x in labels})


def test_classes_and_non_sequence_specific_factors():
    o = occ([peak("A", "HCT116"), peak("C", "HepG2"), peak("EP300", "HCT116"), peak("POLR2A", "HCT116")],
            assayed={"A": {"HCT116"}, "C": {"HepG2"}, "B": {"HCT116"}})
    assert [o.tf_class(t) for t in ("A", "C", "B", "Z")] == ["bound_here", "bound_elsewhere", "unbound_assayed_here",
                                                             "not_assayed"]
    rows = candidates(o, Reg())["rows"]
    assert [r["tf"] for r in rows] == ["A", "C"]                      # EP300 and POLR2A never become candidates
    assert o.detail("A")["experiment"] == "ENCSR1" and o.detail("C")["biosamples_elsewhere"] == ["HepG2"]


def scores(z):
    return pd.DataFrame([{"model": m, "effect": 0.1 * v, "z": v, "p": 1e-30 if abs(v) > 4.05 else 0.5, "status": "ok"}
                         for m, v in z.items()])


def test_occupied_tf_without_a_clear_change_stays_listed():
    from variant2mechanism.agent.stages.screen import summary_line, tf_line
    o = occ([peak("A", "HCT116"), peak("C", "HepG2")], assayed={"A": {"HCT116"}, "C": {"HepG2"}})
    out = screen_v2(scores({"a": 2.0, "b": 30.0}), Reg(), N, occupancy=o, exclude=NOT_SEQUENCE_SPECIFIC)
    assert [r["tf"] for r in out["occupied"]] == ["A", "C"] and out["occupied"][0]["passes_gate"] is False
    assert [r["tf"] for r in out["unknown"]] == ["B"]                 # not assayed, passes the gate
    assert "occupied, no clear allelic change" in tf_line(out["occupied"][0], "HCT116")
    assert out["occupied"][1]["best_model_kind"] == "mapped" and "mapped model of A" in tf_line(out["occupied"][1], "x")
    text = summary_line("chr1:5:A>C", out)
    assert out["n_pass"] == 1 and not re.search(r"\b1 (of 997 )?models? pass", text) and "Bonferroni over 997" in text


def test_nothing_occupied_line():
    from variant2mechanism.agent.stages.screen import summary_line
    out = screen_v2(scores({"a": 9.0, "b": 30.0}), Reg(), N, occupancy=occ([], assayed={"A": {"HCT116"}}),
                    exclude=NOT_SEQUENCE_SPECIFIC)
    assert out["occupied"] == [] and out["nothing_occupied"] and NO_PEAK in summary_line("v", out)


def site_of(pct):
    return lambda m: {"ref_percentile": pct[m][0], "alt_percentile": pct[m][1], "k": 7}


def test_site_rule_puts_strong_sites_first():
    from variant2mechanism.agent.stages.screen import summary_line, tf_line
    o = occ([peak("A", "HCT116"), peak("B", "HCT116")], assayed={"A": {"HCT116"}, "B": {"HCT116"}})
    site = site_of({"a": (90.0, 80.0), "b": (99.0, 50.0)})            # weak for A, strong for B (the better allele)
    out = screen_v2(scores({"a": 30.0, "b": 6.0}), Reg(), N, occupancy=o, site=site, exclude=NOT_SEQUENCE_SPECIFIC)
    b, a = out["occupied"]
    assert (b["tf"], a["tf"]) == ("B", "A") and (b["strong_site"], a["strong_site"]) == (True, False)
    assert out["counts"]["occupied_strong_site"] == 1 and not out["no_strong_site"]
    weak, strong = tf_line(a, "x", out["strong_site_pct"]), tf_line(b, "x", out["strong_site_pct"])
    assert "between weak k-mers" in weak and "detects a change" not in weak
    assert "a weak site (neither allele reaches the 97.5th)" in weak
    assert "detects a change" in strong and "a strong site (the better allele reaches the 97.5th)" in strong
    text = summary_line("v", out)
    assert "a strong site before a weak one" in text and "(1 with a strong site)" in text
    assert "No occupied TF has a strong site" not in text


def test_no_strong_site_line_and_no_demotion_without_weights():
    from variant2mechanism.agent.stages.screen import summary_line
    o = occ([peak("A", "HCT116"), peak("B", "HCT116")], assayed={"A": {"HCT116"}, "B": {"HCT116"}})
    out = screen_v2(scores({"a": 30.0, "b": 6.0}), Reg(), N, occupancy=o, site=site_of({"a": (60, 70), "b": (90, 97)}),
                    exclude=NOT_SEQUENCE_SPECIFIC)
    assert out["no_strong_site"] and "No occupied TF has a strong site at the variant." in summary_line("v", out)

    def no_weights(m):
        raise KeyError(f"no weights for {m}")
    out = screen_v2(scores({"a": 30.0, "b": 6.0}), Reg(), N, occupancy=o, site=no_weights,
                    exclude=NOT_SEQUENCE_SPECIFIC)
    assert [r["tf"] for r in out["occupied"]] == ["A", "B"] and "strong_site" not in out["occupied"][0]
    assert "error" in out["occupied"][0]["site_strength"] and not out["no_strong_site"]


# -- recorded fixtures ------------------------------------------------------------------------------------------


def gold_case(case_id):
    from variant2mechanism.evaluation.gold import load_gold
    r = next(x for x in load_gold().to_dict("records") if x["case_id"] == case_id)
    return Case(Variant.make(r["chrom"], int(r["pos_grch38"]), r["ref"], r["alt"]), r["disease_or_trait"],
                expression_context=r["expression_context"], http=Http(FIXTURES, offline=True)), r


@pytest.fixture(scope="module")
def reg():
    from variant2mechanism.qbic.registry import get_registry
    return get_registry()


@pytest.mark.data
@pytest.mark.parametrize("case_id, tf, cls", [("rs6983267", "TCF7L2", "bound_here"),
                                              ("rs642961", "TFAP2A", "not_assayed"),
                                              ("rs339331", "HOXB13", "unbound_assayed_elsewhere")])
def test_occupancy_classes_on_fixtures(reg, case_id, tf, cls):
    case, _ = gold_case(case_id)
    o, err = fetch(case, reg)
    assert err is None and o.tf_class(tf) == cls


@pytest.mark.data
def test_random_control_has_no_occupied_candidates(reg):
    from variant2mechanism.qbic.expression import get_expression
    case, _ = gold_case("rs13078086")
    o, rows = occupancy_results(case, reg, get_expression())
    assert o.peaks == [] and len(rows) == 1 and rows[0].summary.startswith("No ENCODE TF ChIP-seq peak contains")


@pytest.mark.data
def test_screen_v2_reproduces_the_preview(reg):
    """Spec 3, section 0: the gold TF's rank among occupied TFs by |z| (ties share a rank)."""
    from variant2mechanism.evaluation.gold import scoring_tf
    from variant2mechanism.qbic.tools import QbicTools
    tools = QbicTools()
    ranks = {}
    for case_id in ("tert_c228t", "tert_c250t", "rs2168101", "rs12740374", "rs4784227", "rs6983267"):
        case, r = gold_case(case_id)
        o, _ = fetch(case, reg)
        out = tools.qbic_screen_v2(r["chrom"], int(r["pos_grch38"]), r["ref"], r["alt"], r["expression_context"], o)
        rows, gold = out["occupied"], scoring_tf(r)
        g = next(x for x in rows if x["tf"] == gold)
        order = ("bound_here", "bound_elsewhere")
        ranks[case_id] = 1 + sum(1 for x in rows if order.index(x["occupancy"]) < order.index(g["occupancy"])
                                 or (x["occupancy"] == g["occupancy"] and abs(x["z"]) > abs(g["z"])))
    assert list(ranks.values()) == [1, 1, 1, 2, 2, 3]


@pytest.mark.data
def test_site_rule_on_rs6983267(reg):
    """Of the TFs bound in HCT116, only TCF7L2 has a strong site (98.8th), so it leads; by |z| it was third."""
    from variant2mechanism.qbic.tools import QbicTools
    case, r = gold_case("rs6983267")
    o, _ = fetch(case, reg)
    out = QbicTools().qbic_screen_v2(r["chrom"], int(r["pos_grch38"]), r["ref"], r["alt"], r["expression_context"], o)
    strong = {x["tf"]: x.get("strong_site") for x in out["occupied"]}
    assert out["occupied"][0]["tf"] == "TCF7L2" and strong["TCF7L2"] is True
    assert strong["SRF"] is False and strong["SP1"] is False
