"""chain.py's whole chains: one TF and one target gene per chain, ordered by the weakest link, with ties kept.

Graphs are built through the graph API on the development variant rs1427407 (chr2:60490908 T>G); TF, gene and trait
names and every observation are stipulated for the tests, not claims about that variant.
"""

import itertools
import json

from variant2mechanism.v9 import bundle, chain, commands, report
from variant2mechanism.v9.graph import ClaimGraph, EntityRef
from variant2mechanism.v9.schemas import ContextScope, RunResult

from .test_chain_view import INVESTIGATOR, TRAIT, binding_assay, eqtl, fragments, gwas
from .test_report_support import (
    HEPG2,
    VARIANT,
    claim,
    dev_case,
    gene,
    inventory_call,
    inventory_row,
    rich_graph,
    tf,
    tool_evidence,
    write_run,
)


def ranked(g: ClaimGraph) -> dict:
    return chain.chain_view(g)["ranked"]


def titles(g: ClaimGraph) -> list[tuple[int, str]]:
    return [(r["rank"], r["title"]) for r in ranked(g)["chains"]]


def gene_to_trait(g: ClaimGraph, symbol: str) -> str:
    """A gene to trait claim with an association linked (the class matrix holds it indirect for this relation)."""
    cid = claim(g, [gene(symbol)], "contributes_to_trait", [TRAIT], "decreases")
    eid = tool_evidence(g, "association", f"Burden test: {symbol} loss is associated with lower LDL cholesterol.",
                        about_genes=[symbol], about_traits=["LDL cholesterol"], direction="decreases")
    g.link(cid, eid, "supports", INVESTIGATOR, "the same gene and trait")
    return cid


def test_three_one_link_hypotheses_give_one_whole_chain():
    r = ranked(fragments())
    assert r["total"] == 1 and r["leaders"] == 1 and r["headline"] == "Leading chain: TFX → GENE1."
    row = r["chains"][0]
    assert (row["rank"], row["ties"], row["levels"]) == (1, 1, [3, 0, 2, 0, 2])
    assert [row["cells"][k]["kind"] for k in chain.LINK_KEYS] == ["assay", None, "association", None, "association"]
    assert row["weakest"] == ["activity", "mediation"]
    assert r["support"] == ("Measured: TF binding. Association only: target gene, variant to trait. "
                            "No claim: regulatory activity, gene to trait.")
    assert chain.weakest_text(row) == "regulatory activity (no claim); gene to trait (no claim)"


def test_genes_with_the_same_kind_of_evidence_tie_and_the_tie_is_said():
    g = fragments()
    eqtl(g, "GENE2")
    r = ranked(g)
    assert titles(g) == [(1, "TFX → GENE1"), (1, "TFX → GENE2")] and r["leaders"] == 2
    assert [row["ties"] for row in r["chains"]] == [2, 2] and r["differ"] == ["gene"]
    assert r["headline"] == "2 chains tie for first: TFX → GENE1 or GENE2. They differ only in the target gene."
    view = chain.chain_view(g)
    assert [row[0] for row in chain.ranked_rows(view, "G")] == ["1=", "1="]
    gene_step = next(s for s in chain.strip_rows(view, "G") if s["key"] == "gene")
    assert gene_step["names"] == "GENE1, GENE2 (tied)" and gene_step["evidence"] == "association, G ↑"


def test_a_gene_to_trait_claim_separates_two_genes_that_tie_on_the_gene_link():
    g = fragments()
    eqtl(g, "GENE2")
    onward = gene_to_trait(g, "GENE2")
    assert titles(g) == [(1, "TFX → GENE2"), (2, "TFX → GENE1")]
    first, second = ranked(g)["chains"]
    assert first["cells"]["mediation"]["claims"] == [onward] and first["cells"]["mediation"]["kind"] == "association"
    assert second["cells"]["mediation"]["kind"] is None                # the claim names GENE2, so GENE1 has none
    view = chain.chain_view(g)
    rows = chain.ranked_rows(view, "G")
    assert rows[0][4] == "GENE2 → LDL cholesterol: association, ↓" and rows[0][5] == "leads"
    assert rows[1][4] == "no claim" and rows[1][5] == "weaker on gene to trait"
    assert g.claims[onward].assessment == "unassessed"                  # the view assessed nothing


def test_chains_are_ordered_by_their_weakest_link_not_their_strongest():
    g = ClaimGraph(dev_case())
    inventory_call(g, [inventory_row(1, True, [{"tf": "TFP", "mapping": "own"}])])
    binding_assay(g, "TFX")                                              # an allele-resolved assay
    claim(g, [VARIANT], "alters_binding", [tf("TFP")], "increases")      # predicted only
    eqtl(g, "GENE1")                                                     # an association
    claim(g, [VARIANT], "associated_with_expression", [gene("GENE2")], "increases")     # claimed, nothing linked
    gwas(g)
    # TFP → GENE1 has no unsupported choice link; TFX → GENE2 has the stronger TF and an unsupported gene link
    assert titles(g) == [(1, "TFX → GENE1"), (2, "TFP → GENE1"), (3, "TFX → GENE2"), (4, "TFP → GENE2")]
    rows = chain.ranked_rows(chain.chain_view(g), "G")
    assert [row[5] for row in rows] == ["leads", "weaker on TF binding", "weaker on target gene",
                                        "weaker on TF binding, target gene"]
    assert rows[1][2] == "predicted by QBiC-SELEX, G ↑" and rows[2][3] == "no supporting evidence, G ↑"


def test_no_chain_ranks_above_one_at_least_as_strong_on_every_link():
    g = rich_graph()
    inventory_call(g, [inventory_row(7, True, [{"tf": "TFP", "mapping": "own"}])])
    binding_assay(g, "TFA")
    claim(g, [VARIANT], "alters_binding", [tf("TFP")], "increases")
    eqtl(g, "GENE3")
    gene_to_trait(g, "GENE3")
    claim(g, [VARIANT], "associated_with_expression", [gene("GENE4")], "increases")
    chains = ranked(g)["chains"]
    assert len(chains) >= 6
    for a, b in itertools.permutations(chains, 2):
        if all(x >= y for x, y in zip(a["levels"], b["levels"], strict=True)):
            assert a["rank"] <= b["rank"], (a["title"], b["title"])
            if a["levels"] != b["levels"]:
                assert a["rank"] < b["rank"], (a["title"], b["title"])
    assert [r["rank"] for r in chains] == sorted(r["rank"] for r in chains)
    assert all(r["ties"] == sum(1 for o in chains if o["rank"] == r["rank"]) for r in chains)


def test_a_gene_only_a_gene_to_trait_claim_names_gets_a_chain_with_an_empty_gene_link():
    g = fragments()
    gene_to_trait(g, "GENE9")
    assert titles(g) == [(1, "TFX → GENE1"), (1, "TFX → GENE9")]         # each has one empty link of the two
    loose = ranked(g)["chains"][1]
    assert loose["cells"]["gene"]["kind"] is None and loose["cells"]["gene"]["names"] == ["GENE9"]
    assert loose["cells"]["gene"]["claims"] == [] and loose["cells"]["mediation"]["kind"] == "association"
    assert "No claim: regulatory activity, target gene." in loose["support"]


def test_a_contradicted_candidate_enters_no_chain_and_is_listed():
    r = ranked(rich_graph())                       # GENE2's claim is contradicted in scope; the activity is contested
    assert [x for x in r["left_out"] if x["link"] == "gene"] == [{"link": "gene", "names": ["GENE2"]}]
    assert all("GENE2" not in row["title"] for row in r["chains"])
    assert {row["cells"]["activity"]["kind"] for row in r["chains"]} == {"contested"}
    assert all(row["cells"]["activity"]["level"] == 0 for row in r["chains"])


def test_a_link_whose_candidates_are_all_contradicted_is_not_called_unclaimed():
    g = ClaimGraph(dev_case())
    cid = claim(g, [VARIANT], "associated_with_expression", [gene("GENE1")], "increases")
    eid = tool_evidence(g, "association", "eQTL: G is associated with lower GENE1.", about_genes=["GENE1"],
                        allele="G", direction="decreases", about_variants=["rs1427407"])
    g.link(cid, eid, "contradicts", INVESTIGATOR, "the opposite direction")
    g.assess(cid, "contradicted_in_scope", "eQTL in the opposite direction", "critic", g.claims[cid].version)
    binding_assay(g, "TFX")
    row = ranked(g)["chains"][0]
    assert row["title"] == "TFX → no target gene named" and row["cells"]["gene"]["kind"] == "contradicted"
    assert "Every candidate contradicted in scope: target gene." in row["support"]


def test_the_size_of_z_never_orders_chains_and_a_claim_without_a_record_shows_nothing_in_place():
    """A hundredfold larger z changes nothing. A claim that a factor is expressed, with no record linked, is no record
    of presence, so the two chains tie."""
    g = ClaimGraph(dev_case())
    inventory_call(g, [inventory_row(1, True, [{"tf": "TFA", "mapping": "own"}], z=4.2),
                       inventory_row(2, True, [{"tf": "TFB", "mapping": "own"}], z=160.0)])
    claim(g, [VARIANT], "alters_binding", [tf("TFA")], "increases")
    claim(g, [VARIANT], "alters_binding", [tf("TFB")], "increases")
    claim(g, [tf("TFB")], "expressed_in", [EntityRef(kind="context", label="HepG2")])
    eqtl(g, "GENE1")
    r = ranked(g)
    assert titles(g) == [(1, "TFA → GENE1"), (1, "TFB → GENE1")]         # tied, and listed in id order
    assert r["headline"] == ("2 chains tie for first: TFA or TFB → GENE1. They differ only in the transcription "
                             "factor.")
    assert [c["in_place"] for c in r["chains"]] == [[], []]
    dumped = json.dumps(r)
    assert not any(word in dumped for word in ('"z"', "score", "probability", "confidence"))


def test_a_record_that_the_factor_is_in_place_breaks_a_tie_by_presence_never_by_size():
    """TFB has a ChIP-seq peak linked to a claim that it occupies the site: it leads the otherwise equal TFA, which
    stays in the list. One peak or fifty, a weak signal or a strong one: the cell only says "occupies"."""
    def graph(peaks: int) -> ClaimGraph:
        g = ClaimGraph(dev_case())
        inventory_call(g, [inventory_row(1, True, [{"tf": "TFA", "mapping": "own"}], z=160.0),
                           inventory_row(2, True, [{"tf": "TFB", "mapping": "own"}], z=4.2)])
        claim(g, [VARIANT], "alters_binding", [tf("TFA")], "increases")
        claim(g, [VARIANT], "alters_binding", [tf("TFB")], "increases")
        occupies = claim(g, [tf("TFB")], "occupies", [EntityRef(kind="element", label="enhancer",
                                                                 canonical_id="EH38E0000001")], context=HEPG2)
        for i in range(peaks):
            chip = tool_evidence(g, "occupancy", f"ChIP-seq {i}: a TFB peak covers the variant in HepG2.",
                                 about_tfs=["TFB"], about_elements=["EH38E0000001"], context=HEPG2,
                                 data={"signal": 10.0 * (i + 1)})
            g.link(occupies, chip, "supports", INVESTIGATOR, "peak at the variant")
        eqtl(g, "GENE1")
        return g

    one, many = ranked(graph(1)), ranked(graph(50))
    for r in (one, many):
        assert [(c["rank"], c["ties"], c["title"], c["in_place"]) for c in r["chains"]] == [
            (1, 1, "TFB → GENE1", ["occupies"]), (2, 1, "TFA → GENE1", [])]
        assert r["chains"][0]["strength"] == r["chains"][1]["strength"]       # the same kinds on every link
        assert r["headline"] == "Leading chain: TFB → GENE1." and r["total"] == 2
    assert chain.versus_text(one["chains"][1], one["chains"][0]) == (
        "the same kinds of evidence on every link; no record of a ChIP-seq peak over the variant")
    lead, second = (chain.cell_evidence(c["cells"]["binding"], "G") for c in one["chains"])
    assert lead == "predicted by QBiC-SELEX, G ↑; in place: a ChIP-seq peak over the variant"
    assert second == "predicted by QBiC-SELEX, G ↑" and chain.cell_presence(one["chains"][0]["cells"]["gene"]) == ""
    dumped = json.dumps({**one, "rule": ""})                     # the rule's own text names what is never read
    assert not any(word in dumped for word in ('"z"', "score", "probability", "confidence", "signal"))


def _cutoffs(monkeypatch, cutoffs: dict[str, float]) -> None:
    """Stand-in background cut-offs, so a test does not lean on the real table's numbers."""
    monkeypatch.setattr(chain, "in_top_share",
                        lambda group, z: None if group not in cutoffs or z is None else abs(z) >= cutoffs[group])


def _peak(g: ClaimGraph, symbol: str) -> None:
    occupies = claim(g, [tf(symbol)], "occupies", [EntityRef(kind="element", label="enhancer",
                                                              canonical_id="EH38E0000001")], context=HEPG2)
    chip = tool_evidence(g, "occupancy", f"ChIP-seq: a {symbol} peak covers the variant in HepG2.",
                         about_tfs=[symbol], about_elements=["EH38E0000001"], context=HEPG2)
    g.link(occupies, chip, "supports", INVESTIGATOR, "peak at the variant")


def test_a_strong_prediction_orders_tied_chains_and_needs_both_the_size_and_the_peak(monkeypatch):
    """Each group is read against its own cut-off: z 12 is large for TFA's group and z 30 is not for TFB's. A large
    prediction without a peak, and a peak without a large prediction, are not strong. Nothing is removed."""
    _cutoffs(monkeypatch, {"G001": 10.0, "G002": 40.0, "G003": 10.0, "G004": 10.0})
    g = ClaimGraph(dev_case())
    inventory_call(g, [inventory_row(1, True, [{"tf": "TFA", "mapping": "own"}], z=12.0),
                       inventory_row(2, True, [{"tf": "TFB", "mapping": "own"}], z=30.0),
                       inventory_row(3, True, [{"tf": "TFC", "mapping": "own"}], z=90.0),
                       inventory_row(4, True, [{"tf": "TFD", "mapping": "own"}], z=-12.0)])
    for symbol in ("TFA", "TFB", "TFC", "TFD"):
        claim(g, [VARIANT], "alters_binding", [tf(symbol)], "increases")
    for symbol in ("TFA", "TFB", "TFD"):                   # TFC: the largest z of all, and no peak
        _peak(g, symbol)
    eqtl(g, "GENE1")
    r = ranked(g)
    assert [(c["rank"], c["ties"], c["title"], c["strong"]) for c in r["chains"]] == [
        (1, 2, "TFA → GENE1", True), (1, 2, "TFD → GENE1", True),         # the sign of z is not read
        (3, 1, "TFB → GENE1", False), (4, 1, "TFC → GENE1", False)]
    assert len({tuple(c["strength"]) for c in r["chains"]}) == 1           # the same kinds on every link
    lead, second, last = (r["chains"][i] for i in (0, 2, 3))
    assert chain.cell_evidence(lead["cells"]["binding"], "G") == (
        "predicted by QBiC-SELEX, G ↑; strong prediction: the QBiC-SELEX change is in the top 10% for this TF group, "
        "with a ChIP-seq peak over the variant; in place: a ChIP-seq peak over the variant")
    assert chain.cell_strong(second["cells"]["binding"]) == "" == chain.cell_strong(lead["cells"]["gene"])
    assert chain.versus_text(second, lead) == chain.versus_text(last, lead) == (
        "the same kinds of evidence on every link; no strong prediction (a change in the top 10% for the TF group, "
        "with a ChIP-seq peak over the variant)")
    dumped = json.dumps({**chain.chain_view(g), "factors": None})
    assert '"z"' not in dumped                                             # a yes or a no: no z leaves the view


def test_a_strong_prediction_never_lifts_a_chain_above_a_stronger_link(monkeypatch):
    _cutoffs(monkeypatch, {"G001": 10.0})
    g = ClaimGraph(dev_case())
    inventory_call(g, [inventory_row(1, True, [{"tf": "TFA", "mapping": "own"}], z=80.0)])
    claim(g, [VARIANT], "alters_binding", [tf("TFA")], "increases")
    _peak(g, "TFA")
    binding_assay(g, "TFC")                                # measured, no model, never assayed by ChIP-seq
    assert [(c["rank"], c["title"].split(" → ")[0], c["strong"]) for c in ranked(g)["chains"]] == [
        (1, "TFC", False), (2, "TFA", True)]


def test_a_large_prediction_for_the_other_allele_or_from_an_unknown_group_is_not_strong(monkeypatch):
    _cutoffs(monkeypatch, {"G001": 10.0})
    g = ClaimGraph(dev_case())
    inventory_call(g, [inventory_row(1, True, [{"tf": "TFA", "mapping": "own"}], z=80.0),      # favours G
                       inventory_row(2, True, [{"tf": "TFB", "mapping": "own"}], z=80.0)])     # no cut-off on file
    cid = claim(g, [VARIANT], "alters_binding", [tf("TFA")], "decreases", HEPG2)               # measured: G binds less
    eid = tool_evidence(g, "binding_assay", "EMSA: TFA binds the G probe less.", about_tfs=["TFA"], allele="G",
                        direction="decreases", about_variants=["rs1427407"], context=HEPG2)
    g.link(cid, eid, "supports", INVESTIGATOR, "the G probe binds less")
    claim(g, [VARIANT], "alters_binding", [tf("TFB")], "increases")
    _peak(g, "TFA")
    _peak(g, "TFB")
    assert {c["title"].split(" → ")[0]: c["strong"] for c in ranked(g)["chains"]} == {"TFA": False, "TFB": False}


def test_a_group_is_read_by_its_strongest_model_whichever_allele_that_favours(monkeypatch):
    """A group whose models disagree has one item per allele. The background takes the group's largest |z|, so the
    group counts only when that item does not go against the claim."""
    _cutoffs(monkeypatch, {"G001": 10.0})
    agrees = {"group": "G001", "verdict": "agrees"}
    against = {"group": "G001", "verdict": "disagrees"}
    assert chain._large([agrees, against], [30.0, -12.0]) == ["G001"]
    assert chain._large([agrees, against], [12.0, -30.0]) == []            # 12 is past the cut-off, 30 decides
    assert chain._large([agrees], [9.9]) == [] and chain._large([agrees], [None]) == []
    assert chain._large([{"group": "G999", "verdict": "agrees"}], [500.0]) == []


def test_a_peak_from_a_different_context_is_no_record_of_presence():
    g = ClaimGraph(dev_case())
    inventory_call(g, [inventory_row(1, True, [{"tf": "TFA", "mapping": "own"}]),
                       inventory_row(2, True, [{"tf": "TFB", "mapping": "own"}])])
    claim(g, [VARIANT], "alters_binding", [tf("TFA")], "increases")
    claim(g, [VARIANT], "alters_binding", [tf("TFB")], "increases")
    occupies = claim(g, [tf("TFB")], "occupies", [EntityRef(kind="element", label="enhancer",
                                                             canonical_id="EH38E0000001")], context=HEPG2)
    chip = tool_evidence(g, "occupancy", "ChIP-seq: a TFB peak covers the variant in K562.", about_tfs=["TFB"],
                         about_elements=["EH38E0000001"], context=ContextScope(label="K562", source="evidence"))
    g.link(occupies, chip, "supports", INVESTIGATOR, "peak at the variant")        # stored as context only
    eqtl(g, "GENE1")
    assert titles(g) == [(1, "TFA → GENE1"), (1, "TFB → GENE1")]


def test_a_report_embeds_the_rows_it_lists_and_says_how_many_more_there_are():
    g = ClaimGraph(dev_case())
    inventory_call(g, [inventory_row(i, True, [{"tf": f"TF{i}", "mapping": "own"}]) for i in range(1, 13)])
    for i in range(1, 13):
        claim(g, [VARIANT], "alters_binding", [tf(f"TF{i}")], "increases")
    eqtl(g, "GENE1")
    view = chain.chain_view(g)
    cut = chain.for_report(view)
    assert len(view["ranked"]["chains"]) == 12 and len(cut["ranked"]["chains"]) == chain.RANKED_SHOWN
    assert cut["ranked"]["total"] == 12 and cut["ranked"]["leaders"] == 12
    assert chain.ranked_more(cut) == chain.ranked_more(view) == "4 more chains not shown, 4 of them tied at rank 1."
    assert chain.ranked_rows(cut) == chain.ranked_rows(view) and chain.strip_rows(cut) == chain.strip_rows(view)
    assert view["ranked"]["chains"][11]["rank"] == 1                # the whole view is unchanged


def test_a_significant_prediction_that_agrees_lifts_a_measured_link_and_silence_costs_nothing():
    g = ClaimGraph(dev_case())
    inventory_call(g, [inventory_row(1, True, [{"tf": "TFA", "mapping": "own"}], z=3.1),
                       inventory_row(2, False, [{"tf": "TFB", "mapping": "own"}])])
    for symbol in ("TFA", "TFB", "TFC"):                  # a passing model, models below the gate, no model
        binding_assay(g, symbol)
    view = chain.chain_view(g)
    chains = view["ranked"]["chains"]
    assert [(r["title"].split(" → ")[0], r["rank"], r["ties"]) for r in chains] == [
        ("TFA", 1, 1), ("TFB", 2, 2), ("TFC", 2, 2)]      # below the gate and no model tie: neither is penalised
    cells = [r["cells"]["binding"] for r in chains]
    assert [(c["kind"], c["level"], c["backed"], c["step"]) for c in cells] == [
        ("assay", 3, True, 3.5), ("assay", 3, False, 3), ("assay", 3, False, 3)]
    assert 3 < cells[0]["step"] < chain.LEVEL["edit"]     # above the same rung, below the next one
    assert [chain.cell_qbic(c) for c in cells] == [
        "QBiC-SELEX predicts more binding to G", "QBiC-SELEX: its models do not pass the gate",
        "QBiC-SELEX: no model for it"]
    rows = chain.ranked_rows(view, "G")
    assert rows[0][2].startswith("allele-resolved assay + QBiC-SELEX prediction, G ↑") and rows[0][5] == "leads"
    assert rows[1][5] == rows[2][5] == "weaker on TF binding (no QBiC-SELEX prediction in support)"
    assert view["ranked"]["headline"] == "Leading chain: TFA → no target gene named."
    bare = ClaimGraph(dev_case())                          # no inventory in the run: nothing is said about it
    binding_assay(bare, "TFA")
    cell = chain.chain_view(bare)["ranked"]["chains"][0]["cells"]["binding"]
    assert cell["qbic"] == [] and cell["backed"] is False


def test_the_size_of_z_does_not_change_how_much_a_prediction_lifts():
    def steps(z: float) -> list[float]:
        g = ClaimGraph(dev_case())
        inventory_call(g, [inventory_row(1, True, [{"tf": "TFA", "mapping": "own"}], z=z)])
        binding_assay(g, "TFA")
        return chain.chain_view(g)["ranked"]["chains"][0]["levels"]

    assert steps(3.1) == steps(160.0) == [3.5, 0, 0, 0, 0]


def test_a_prediction_for_the_other_allele_lifts_nothing_drops_nothing_and_is_flagged():
    g = ClaimGraph(dev_case())
    inventory_call(g, [inventory_row(1, True, [{"tf": "TFA", "mapping": "own"}])])       # the model favours G
    cid = claim(g, [VARIANT], "alters_binding", [tf("TFA")], "decreases", HEPG2)         # measured: G binds less
    eid = tool_evidence(g, "binding_assay", "EMSA: TFA binds the G probe less.", about_tfs=["TFA"], allele="G",
                        direction="decreases", about_variants=["rs1427407"], context=HEPG2)
    g.link(cid, eid, "supports", INVESTIGATOR, "the G probe binds less")
    binding_assay(g, "TFC")                                                              # no model at all
    view = chain.chain_view(g)
    assert [(r["rank"], r["ties"]) for r in view["ranked"]["chains"]] == [(1, 2), (1, 2)]
    opposed = next(r for r in view["ranked"]["chains"] if r["title"].startswith("TFA"))["cells"]["binding"]
    assert (opposed["kind"], opposed["backed"], opposed["step"]) == ("assay", False, 3)
    assert chain.cell_qbic(opposed) == "QBiC-SELEX predicts more binding to G, against the claim's direction"


def test_a_prediction_alone_gives_the_predicted_rung_and_no_extra_step():
    g = ClaimGraph(dev_case())
    inventory_call(g, [inventory_row(1, True, [{"tf": "TFA", "mapping": "own"}])])
    claim(g, [VARIANT], "alters_binding", [tf("TFA")], "increases")
    cell = chain.chain_view(g)["ranked"]["chains"][0]["cells"]["binding"]
    assert (cell["kind"], cell["backed"], cell["step"]) == ("prediction", False, 1)
    assert chain.cell_qbic(cell) == "" and chain.cell_evidence(cell, "G") == "predicted by QBiC-SELEX, G ↑"


def test_gate_passing_groups_no_claim_names_are_counted_and_get_no_chain():
    g = ClaimGraph(dev_case())
    inventory_call(g, [inventory_row(1, True, [{"tf": "TFA", "mapping": "own"}]),
                       inventory_row(2, True),                                           # passes, no claim
                       inventory_row(3, False),                                          # below the gate
                       inventory_row(4, True, [{"tf": "TFD", "mapping": "own"}])])       # passes, claim opposes it
    claim(g, [VARIANT], "alters_binding", [tf("TFA")], "increases")
    claim(g, [VARIANT], "alters_binding", [tf("TFD")], "decreases")
    eqtl(g, "GENE1")
    view = chain.chain_view(g)
    assert titles(g) == [(1, "TFA → GENE1"), (2, "TFD → GENE1")]         # nothing for G002: no claim names it
    assert view["ranked"]["unclaimed"] == {"count": 1, "passing": 3, "total": 4, "groups": ["G002"]}
    assert chain.unclaimed_text(view).startswith(
        "QBiC-SELEX also predicts a significant change for 1 TF group that no binding claim names (3 of 4 scored")
    bare = ClaimGraph(dev_case())
    binding_assay(bare, "TFA")
    assert chain.unclaimed_text(chain.chain_view(bare)) is None           # no inventory: nothing to count


def test_tied_factors_that_favour_different_alleles_are_each_given_their_own_direction():
    g = ClaimGraph(dev_case())
    binding_assay(g, "TFA")                                                      # G binds more
    cid = claim(g, [VARIANT], "alters_binding", [tf("TFB")], "decreases", HEPG2)
    eid = tool_evidence(g, "binding_assay", "EMSA: TFB binds the G probe less.", about_tfs=["TFB"], allele="G",
                        direction="decreases", about_variants=["rs1427407"], context=HEPG2)
    g.link(cid, eid, "supports", INVESTIGATOR, "the G probe binds less")
    view = chain.chain_view(g)
    assert view["ranked"]["leaders"] == 2
    step = chain.strip_rows(view, "G")[0]
    assert step["names"] == "TFA, TFB (tied)" and step["detail"][0] == "TFA G ↑; TFB G ↓"
    assert [row[2].split(" (")[0] for row in chain.ranked_rows(view, "G")] == [
        "allele-resolved assay, G ↑", "allele-resolved assay, G ↓"]


def test_a_run_with_no_claims_has_no_chain_and_the_view_changes_nothing():
    empty = ranked(ClaimGraph(dev_case()))
    assert empty["chains"] == [] and empty["headline"] is None and empty["total"] == 0
    g = rich_graph()
    before = g.to_json()
    first = chain.chain_view(g)["ranked"]
    assert g.to_json() == before and json.loads(json.dumps(first)) == first == chain.chain_view(g)["ranked"]


def test_both_reports_lead_with_the_ranked_chains(tmp_path):
    g = fragments()
    eqtl(g, "GENE2")
    g.set_result(RunResult(outcome="multiple_explanations", stop_reason="converged"), "code")
    loaded = bundle.load_bundle(write_run(g, tmp_path / "run"))
    html, md = report.render_html(loaded), report.render_markdown(loaded)
    for rendered in (html, md):
        assert "2 chains tie for first: TFX → GENE1 or GENE2. They differ only in the target gene." in rendered
        assert "Chains are ordered by their weakest link" in rendered
        assert "Multiple explanations" in rendered                     # the comparison's own outcome is still shown
    assert html.index('id="answer"') < html.index('id="summary"')
    assert md.index("## Answer: ranked mechanism chains") < md.index("## Outcome")
    assert '<a href="#answer">Answer</a>' in html and "| 1= | TFX → GENE1 |" in md
    bare = bundle.load_bundle(write_run(ClaimGraph(dev_case()), tmp_path / "bare"))
    for rendered in (report.render_html(bare), report.render_markdown(bare)):
        assert report.NO_CHAIN in rendered


def test_the_terminal_summary_names_the_answer(tmp_path):
    g = fragments()
    text = commands.summary(g, tmp_path, {"model_calls": 0})
    assert "  answer: Leading chain: TFX → GENE1." in text.splitlines()
    assert "answer:" not in commands.summary(ClaimGraph(dev_case()), tmp_path, {})


def test_names_in_the_answer_cannot_become_markup(tmp_path):
    g = ClaimGraph(dev_case())
    cid = claim(g, [VARIANT], "associated_with_expression", [gene("<b>GENE|1</b>")], "increases")
    eid = tool_evidence(g, "association", "eQTL: G is associated with higher expression.",
                        about_genes=["<b>GENE|1</b>"], allele="G", direction="increases",
                        about_variants=["rs1427407"])
    g.link(cid, eid, "supports", INVESTIGATOR, "same allele and direction")
    loaded = bundle.load_bundle(write_run(g, tmp_path / "run"))
    html, md = report.render_html(loaded), report.render_markdown(loaded)
    assert "<b>gene" not in html.lower() and "no TF named → &lt;B&gt;GENE|1&lt;/B&gt;" in html   # symbols are upper-cased
    assert "<b>gene" not in md.lower() and "no TF named → &lt;B&gt;GENE\\|1&lt;/B&gt;" in md


def test_a_small_named_group_is_called_by_its_members_and_a_large_one_keeps_its_name():
    import types

    from variant2mechanism.v9.schemas import Entity

    tfs = {f"N{i}": Entity(entity_id=f"N{i}", kind="tf", label=f"TF{i}") for i in range(1, 6)}
    graph = types.SimpleNamespace(entities=tfs)
    small = Entity(entity_id="N8", kind="tf_group", label="A FAMILY GROUP", canonical_id="G1",
                   participants=["N1", "N2", "N3"])
    large = small.model_copy(update={"participants": list(tfs)})
    assert chain._label(graph, small, short=True) == "TF1, TF2, TF3 (group G1)"
    assert chain._label(graph, large, short=True) == "A FAMILY GROUP group G1"
    assert chain._label(graph, small) == "A FAMILY GROUP group G1 (TF1, TF2, TF3)"
    assert chain._label(graph, large) == "A FAMILY GROUP group G1 (TF1, TF2, TF3 and 2 more)"


def test_the_strip_names_every_rival_and_counts_the_rest_of_a_shared_link():
    traits = ["a trait with a long name", "second trait", "third trait"]
    assert chain.strip_names({"link": "trait", "names": traits}) == "a trait with a long name and 2 more"
    assert chain.strip_names({"link": "trait", "names": traits[:1]}) == "a trait with a long name"
    assert chain.strip_names({"link": "gene", "names": ["A", "B", "C"]}) == "A, B, C (tied)"
    assert chain.strip_names({"link": "binding", "names": []}) == ""
