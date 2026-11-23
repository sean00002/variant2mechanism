"""variant_identity._other_strand: an allele a paper names on the other strand, placed on the case variant's strand.

A synthetic variant (chr7:2345678 G>A, rs99123456) and stipulated passages: nothing here is a claim about a real
variant. The case's alleles are G and A, so the other strand's names for them are C and T.
"""

import pytest

from variant2mechanism.v9.graph import ClaimDraft, ClaimGraph, EntityRef, GraphRefusal
from variant2mechanism.v9.schemas import Case, Evidence, ExperimentRecord, ToolCall, Variant
from variant2mechanism.v9.variant_identity import named_alleles, normalise_evidence

RSID = "rs99123456"
PASSAGE = "Constructs containing the C-allele gave 30-fold higher luminescence than the T-allele (P = 0.002)."


def graph(ref: str = "G", alt: str = "A") -> ClaimGraph:
    return ClaimGraph(Case(case_id="synthetic", variant=Variant(chrom="7", pos=2345678, ref=ref, alt=alt, rsid=RSID)))


def read(g: ClaimGraph) -> str:
    call = g.record_tool_call(ToolCall(tool_call_id=g.reserve_tool_call_id(), tool_name="literature_read",
                                       execution_status="success", retrieval_status="records_found",
                                       requested_by="literature_investigator", charged_to="agent",
                                       read_article="PMID:90000001", article_ids=["90000001"]))
    return call.tool_call_id


def reporter(passage: str = PASSAGE, allele: str | None = "T", variants=(RSID,), retrieval_ref: str | None = None,
             **fields) -> Evidence:
    record = ExperimentRecord(source_id="PMID:90000001", access="full_text", location="results/p3", passage=passage,
                              manipulated="allele", compared_allele=allele, direction="decreases")
    return Evidence(evidence_class="reporter_assay", observed_result="The T-allele construct had lower luminescence.",
                    independence_group="PMID:90000001#reporter", origin="literature", source_ids=["PMID:90000001"],
                    experiment=record, allele=allele, direction="decreases", about_variants=list(variants),
                    access="full_text", retrieval_ref=retrieval_ref, **fields)


@pytest.mark.parametrize("text, named", [
    ("the risk G-allele compared to the T-allele", {"G", "T"}),
    ("allele C bound more strongly than allele T", {"C", "T"}),
    ("the G>T substitution", {"G", "T"}), ("rs1 (G/T)", {"G", "T"}), ("a C to T change", {"C", "T"}),
    ("the G and T alleles", {"G", "T"}),
    ("a GATA motif in the sequence ACGTTGCA", set()), ("Table 2, panel C, at 37 C", set()), ("", set()),
])
def test_a_passage_names_an_allele_only_as_an_allele(text, named):
    assert named_alleles(text) == named


def test_an_allele_named_on_the_other_strand_is_placed_and_the_paper_s_notation_is_kept():
    g = graph()
    ev = reporter()
    placed = normalise_evidence(ev, g)
    assert (ev.allele, placed.allele, placed.direction) == ("T", "A", "decreases")
    assert placed.experiment.compared_allele == "T" and placed.experiment.passage == PASSAGE
    proof = placed.data["variant_identity"]
    assert proof["basis"] == "other_strand_allele_pair" and proof["paper_to_case_strand_flip"] is True
    assert (proof["paper_allele"], proof["case_allele"], proof["paper_alleles"]) == ("T", "A", ["C", "T"])
    assert "the other strand's names of G and A: T is read as A" in placed.limitations[-1]
    assert normalise_evidence(placed, g) is placed                               # mapped once


def test_the_graph_refuses_the_record_as_the_paper_wrote_it_and_takes_it_once_placed():
    g = graph()
    cid = g.add_claim(ClaimDraft(subjects=[EntityRef(kind="variant", label=RSID)],
                                 relation="alters_regulatory_activity",
                                 objects=[EntityRef(kind="element", label="reporter construct")],
                                 direction="decreases", effect_allele="A"), "coordinator")
    call = read(g)
    raw = g.add_evidence(reporter(retrieval_ref=call), "literature_investigator")
    with pytest.raises(GraphRefusal, match="neither ref G nor alt A"):
        g.link(cid, raw, "supports", "coordinator", "the alleles were compared")
    placed = normalise_evidence(reporter(retrieval_ref=call, about_elements=["reporter construct"]), g)
    eid = g.add_evidence(placed, "literature_investigator")
    link = g.link(cid, eid, "supports", "coordinator", "the alleles were compared")
    assert (link.stance, link.strength) == ("supports", "direct")
    other = g.add_claim(ClaimDraft(subjects=[EntityRef(kind="variant", label=RSID)],
                                   relation="alters_regulatory_activity",
                                   objects=[EntityRef(kind="element", label="reporter construct")],
                                   direction="increases", effect_allele="A"), "coordinator")
    with pytest.raises(GraphRefusal, match="opposite to the claim"):             # placed, it can still disagree
        g.link(other, eid, "supports", "coordinator", "the alleles were compared")


@pytest.mark.parametrize("why, g, ev", [
    ("an A/T variant reads the same on both strands", graph("A", "T"),
     reporter("The A-allele gave higher luminescence than the T-allele.", allele="C")),
    ("a C/G variant reads the same on both strands", graph("C", "G"),
     reporter("The C-allele gave higher luminescence than the G-allele.", allele="T")),
    ("the passage names one allele only: its partner could be a third allele", graph(),
     reporter("The T-allele construct had lower luminescence than the reference construct.")),
    ("the passage also names one of the case's own alleles", graph(),
     reporter("The G-allele gave higher luminescence than the T-allele; the C allele was not tested.")),
    ("the allele is already one of the case's", graph(), reporter(allele="A")),
    ("the record names another variant", graph(), reporter(variants=["rs1"])),
    ("the record names the case and another variant", graph(), reporter(variants=[RSID, "rs1"])),
    ("the record names no variant", graph(), reporter(variants=[])),
    ("no allele is named", graph(), reporter(allele=None)),
])
def test_nothing_is_placed_unless_nothing_else_can_be_meant(why, g, ev):
    assert normalise_evidence(ev, g) is ev, why


def test_a_database_row_is_never_placed_by_this_rule():
    g = graph()
    row = Evidence(evidence_class="association", observed_result="GWAS: the T allele lowers the trait.",
                   independence_group="GWAS:1", origin="tool", allele="T", direction="decreases",
                   about_variants=[RSID])
    assert normalise_evidence(row, g) is row            # an adapter places its own alleles (or leaves them out)
