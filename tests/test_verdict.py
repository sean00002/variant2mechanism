"""The run's verdict: mechanism, no mechanism or undetermined, from the ranked chains and tested facts."""

from variant2mechanism.agent.stages.verdict import (
    AGAINST,
    FOR,
    UNKNOWN,
    chain_facts,
    decide,
    expression_fact,
    occupancy_fact,
    qbic_fact,
)
from variant2mechanism.evaluation.metrics import verdict_scores
from variant2mechanism.qbic.variants import Variant

V = Variant.make("chr8", 127401060, "G", "T")


def chain(cid, tf=None, binding="supported", null=False):
    return {"id": cid, "is_null": null, "tf": tf, "allele": None if null else "ref",
            "links": [] if null else [{"step": "binding", "status": binding}, {"step": "element", "status": "weak"}]}


def facts(**per_chain):
    """Chain id -> {fact name: for, against or unknown}; facts not given are unknown."""
    return {cid: {"tf": cid, "symbol": cid, **{k: [f.get(k, UNKNOWN), f"{k} reason"]
                                               for k in ("qbic", "occupancy", "expression")}}
            for cid, f in per_chain.items()}


def test_mechanism_needs_binding_that_counts_and_nothing_against():
    chains = [chain("H1", "TCF7L2"), chain("H0", null=True)]
    assert decide(chains, facts(H1={"qbic": FOR})) == ("mechanism", "TCF7L2: its binding counts, and nothing tested "
                                                                     "counts against it")
    weak = [chain("H1", "TCF7L2", binding="weak"), chain("H0", null=True)]
    assert decide(weak, facts(H1={}))[0] == "undetermined"
    assert decide(weak, facts(H1={"qbic": FOR}), binding="either")[0] == "mechanism"     # QBiC-SELEX backs it
    assert decide(weak, facts(H1={"qbic": FOR}), binding="critic")[0] == "undetermined"
    assert decide(chains, facts(H1={}), binding="code")[0] == "undetermined"               # graded, but no QBiC
    v, why = decide(chains, facts(H1={"occupancy": AGAINST}))
    assert v == "undetermined" and why == "tested evidence counts against TCF7L2: occupancy reason"
    assert decide(chains, facts(H1={"qbic": FOR}), pairwise_ok=False)[0] == "undetermined"


def test_no_mechanism_needs_a_tested_fact_against_every_tf_chain():
    chains = [chain("H0", null=True), chain("H1", "TCF7L2"), chain("H2", "NFIC")]
    assert decide(chains, facts(H1={"qbic": AGAINST}, H2={"occupancy": AGAINST}))[0] == "no mechanism"
    v, why = decide(chains, facts(H1={"qbic": AGAINST}, H2={}))
    assert v == "undetermined" and why == "the null leads, but nothing tested counts against NFIC"


class FakeQbic:
    def __init__(self, out):
        self.out = out

    def qbic_tf_detail(self, chrom, pos, ref, alt, tf):
        return self.out


def test_qbic_fact_reads_the_gate_and_the_direction():
    passing = {"coverage": "own_model", "models": [{"model": "M1", "z": -6.0, "effect": -0.8, "passed_gate": True}]}
    assert qbic_fact(FakeQbic(passing), V, "TCF7L2", "ref")[0] == FOR          # effect below 0: ref binds more
    assert qbic_fact(FakeQbic(passing), V, "TCF7L2", "alt")[0] == AGAINST
    below = {"coverage": "own_model", "models": [{"model": "M1", "z": 0.4, "effect": 0.1, "passed_gate": False}]}
    assert qbic_fact(FakeQbic(below), V, "TCF7L2", "ref")[0] == AGAINST
    assert qbic_fact(FakeQbic({"coverage": "not_in_coverage"}), V, "ARID5B", "ref")[0] == UNKNOWN
    assert qbic_fact(None, V, "TCF7L2", "ref")[0] == UNKNOWN                    # no_qbic: QBiC-SELEX never decides


class FakeOccupancy:
    def __init__(self, cls):
        self.cls = cls

    def tf_class(self, symbol):
        return self.cls


class FakeExpression:
    def __init__(self, tpm):
        self.tpm = tpm

    def tf_expression(self, symbols, context):
        return {symbols[0]: {"tpm": self.tpm}}


def test_occupancy_and_expression_facts():
    assert occupancy_fact(FakeOccupancy("bound_here"), "X")[0] == FOR
    assert occupancy_fact(FakeOccupancy("unbound_assayed_here"), "X")[0] == AGAINST
    assert occupancy_fact(FakeOccupancy("not_assayed"), "X")[0] == UNKNOWN       # never assayed: no evidence
    assert occupancy_fact(None, "X")[0] == UNKNOWN
    no_peak = FakeOccupancy("unbound_assayed_here")
    no_peak.match = type("Match", (), {"biosamples": ["LNCaP clone FGC"]})()
    assert occupancy_fact(no_peak, "X", lambda s: [{"biosample": "LNCaP"}])[0] == FOR     # ReMap has a peak there
    assert occupancy_fact(no_peak, "X", lambda s: [{"biosample": "K562"}])[0] == AGAINST
    assert occupancy_fact(no_peak, "X", lambda s: None)[0] == AGAINST
    assert expression_fact(FakeExpression(0.2), "X", "DepMap:ACH-1", 1.0)[0] == AGAINST
    assert expression_fact(FakeExpression(5.0), "X", "DepMap:ACH-1", 1.0)[0] == FOR
    assert expression_fact(FakeExpression(None), "X", "DepMap:ACH-1", 1.0)[0] == UNKNOWN
    assert expression_fact(FakeExpression(0.2), "X", None, 1.0)[0] == UNKNOWN


class Registry:
    def resolve_tf(self, name):
        return {"status": "ok", "symbol": name.upper()} if name != "??" else {"status": "unknown"}


def test_chain_facts_skip_the_null_and_unresolved_names():
    chains = [chain("H0", null=True), chain("H1", "tcf7l2"), chain("H2", "??")]
    f = chain_facts(chains, V, "DepMap:ACH-1", Registry(), occupancy=FakeOccupancy("bound_here"))
    assert set(f) == {"H1", "H2"} and f["H1"]["symbol"] == "TCF7L2" and f["H1"]["occupancy"][0] == FOR
    assert all(f["H2"][k][0] == UNKNOWN for k in ("qbic", "occupancy", "expression"))


def test_verdict_scores_abstention_apart_from_error():
    tf_case = {"causal_tf": "TCF7L2", "label_class": "tf_mechanism_cancer", "score_level": "mapped"}
    control = {"causal_tf": "none", "label_class": "control_random", "score_level": "control"}
    top = {"is_null": False, "tf": "TCF7L2"}
    assert verdict_scores({"verdict": {"verdict": "mechanism"}}, tf_case, top, Registry())["verdict_correct"]
    held = verdict_scores({"verdict": {"verdict": "undetermined"}}, tf_case, top, Registry())
    assert held["abstained"] and not held["verdict_correct"] and held["verdict_overclaim"] is None
    over = verdict_scores({"verdict": {"verdict": "mechanism"}}, control, top, Registry())
    assert over["verdict_overclaim"] and not over["verdict_correct"]
    assert verdict_scores({"verdict": {"verdict": "no mechanism"}}, control, None, Registry())["verdict_correct"]
    assert verdict_scores({}, tf_case, top, Registry()) == {}                   # reports from before the verdict
