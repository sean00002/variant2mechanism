"""Which variant an extracted experiment is about (core C3-1) and what a perturbation can say about the variant's
alleles (core C3-2), checked against the paper: an rsID or position the extractor names is kept only where the paper
names it for that experiment, in the form the graph reads; an allele comparison must name the one variant whose alleles
it compared; an LD partner tested in the same paper never stands in for the case variant. Article text is invented
(fixtures/literature/oa_variants.xml names rs1427407, an LD partner rs90000017 and a near-miss id rs14274070; the
cases article oa_cases.xml names rs1427407 only)."""

import pytest

from variant2mechanism.v9 import literature as lit
from variant2mechanism.v9.context_match import scope_from_label
from variant2mechanism.v9.graph import ClaimDraft, ClaimGraph, EntityRef, GraphRefusal

from .test_literature_fakes import FakeHttp, case, cases, read, record, records, runner, search_response

CASE_SECTION = "The T allele probe bound GATA1 more strongly than the G allele probe in K562 nuclear extract."
PARTNER = "At rs90000017, the A allele probe bound GATA1 more strongly than the C allele probe in K562 nuclear extract."
SIDE_BY_SIDE = "the T allele probe bound TAL1 more strongly than the G allele probe"
NEAR_MISS = "its T and G probes showed no difference in GATA1 binding"
REPORTER = ("its T allele construct gave 2-fold higher luciferase activity than the G allele construct in K562 "
            "cells")
REVERSED = "The G allele probe bound GATA1 less strongly than the T allele probe"
KNOCKDOWN = "siRNA knockdown of GATA1 in K562 cells reduced BCL11A mRNA by half"
TT_DELETION = ("CRISPR/Cas9 deletion of the enhancer containing rs1427407 in HUDEP-2 cells (TT at rs1427407) reduced "
               "BCL11A mRNA by 60%.")
INTRO = ("Previous electrophoretic mobility shift assays in K562 nuclear extract showed that the T allele binds GATA1 "
         "more strongly than the G allele")


@pytest.fixture
def linked(tmp_path):
    """The article naming several variants (PMC9000008), read once: (graph, call, article)."""
    return cases(tmp_path / "linked", "PMC9000008")


@pytest.fixture
def single(tmp_path):
    """The cases article (PMC9000007), which names rs1427407 alone: (graph, call, article)."""
    return cases(tmp_path / "single")


def comparison(passage: str, location: str, variants: list[str], *, tf: str = "GATA1", allele: str = "T",
               direction: str = "increases", source: str = "PMID:90000008", **fields):
    """An EMSA comparing two alleles, naming `variants` (about_variants)."""
    return record(passage, source_id=source, intervention="EMSA with allele probes", endpoint=f"{tf} binding",
                  manipulated="allele", compared_allele=allele, direction=direction, about_tfs=[tf],
                  about_variants=variants, location=location, **fields)


def reporter(variants: list[str]):
    """The T and G luciferase constructs of PMC9000008 (sec1.3/p1), naming `variants`."""
    return record(REPORTER, source_id="PMID:90000008", intervention="luciferase reporter constructs",
                  endpoint="luciferase activity", manipulated="allele", compared_allele="T", direction="increases",
                  about_variants=variants, location="sec1.3/p1")


def case_claim(graph: ClaimGraph, relation: str = "alters_binding", obj: EntityRef | None = None) -> str:
    return graph.add_claim(ClaimDraft(subjects=[EntityRef(kind="variant", label="rs1427407")], relation=relation,
                                      objects=[obj or EntityRef(kind="tf", label="GATA1")], direction="increases",
                                      effect_allele="T", context=scope_from_label("K562")), "coordinator")


def extract(paper, rec):
    _, call, article = paper
    return lit.evidence_from_experiment(rec, call, article)


# --- kept where the paper names it, as the graph reads it ------------------------------------------------------------

def test_a_variant_named_where_the_passage_is_is_kept_and_reaches_the_graph(linked):
    graph, call, article = linked
    ev = lit.evidence_from_experiment(comparison(CASE_SECTION, "sec1.1/p1", ["rs1427407"]), call, article,
                                      resolver=graph.resolver)          # the call the engine makes
    assert ev.about_variants == ev.experiment.about_variants == ["rs1427407"]     # named by the section's heading
    eid = graph.add_evidence(ev, "literature_investigator")
    link = graph.link(case_claim(graph), eid, "supports", "literature_investigator", "the T probe binds GATA1 more")
    assert (link.strength, link.applicability) == ("direct", "exact")
    by_position = extract(linked, comparison(CASE_SECTION, "sec1.1/p1", ["chr2:60490908"]))
    assert by_position.about_variants == ["chr2:60490908 T>G"]     # the paper writes it beside rs1427407, with alleles
    assert graph.variant_mention(by_position.about_variants[0]) == "case"


def test_positions_are_kept_with_the_alleles_the_paper_writes(linked):
    """The section writes "chr2:60,490,908 (T/G)"; the methods write "rs1427407 (chr2:60,490,908 T>G)"."""
    for given in ("chr2:60490908", "2:60490908", "chr2:60,490,908", "CHR2:60490908 G/T"):
        ev = extract(linked, reporter([given]))
        assert ev.about_variants == (["chr2:60490908 G>T"] if "/" in given else ["chr2:60490908 T>G"])
    assert extract(linked, reporter(["rs1427407"])).about_variants == ["rs1427407"]
    kept = extract(linked, reporter(["rs1427407", "the SNP", "chr2_60490908_T_G_b38"]))
    assert kept.about_variants == ["rs1427407"]
    assert any("the SNP" in x and "chr2_60490908_T_G_b38" in x and "no rsID or chromosome position" in x
               for x in kept.limitations)                          # a GTEx-style id names nothing, as in the graph
    for wrong, why in (("chr2:60490908 T>C", "other alleles"), ("rs90000017", "other variants")):
        with pytest.raises(lit.ExtractionRefused, match=why):
            extract(linked, reporter([wrong]))


# --- an LD partner is never the case variant -------------------------------------------------------------------------

def test_an_ld_partner_tested_in_the_same_paper_is_never_filed_as_the_case_variant(linked):
    graph, call, article = linked
    with pytest.raises(lit.ExtractionRefused, match="passage names rs90000017") as refused:
        extract(linked, comparison(PARTNER, "sec1.2/p1", ["rs1427407"], allele="A"))
    assert "name the variant whose alleles were compared" in refused.value.reason
    partner = extract(linked, comparison(PARTNER, "sec1.2/p1", ["rs90000017", "rs1427407"], allele="A"))
    assert partner.about_variants == ["rs90000017"] and any("rs1427407" in x for x in partner.limitations)
    eid = graph.add_evidence(partner, "literature_investigator")
    with pytest.raises(GraphRefusal, match="not the case variant"):
        graph.link(case_claim(graph), eid, "supports", "literature_investigator", "an EMSA in the same paper")
    other = graph.add_claim(ClaimDraft(subjects=[EntityRef(kind="variant", label="rs90000017")],
                                       relation="alters_binding", objects=[EntityRef(kind="tf", label="GATA1")],
                                       direction="increases", effect_allele="A", context=scope_from_label("K562")),
                            "coordinator")
    assert graph.claim_frame(other) == "other"
    assert graph.link(other, eid, "supports", "literature_investigator", "the A probe binds more").strength == "direct"


def test_a_near_miss_id_never_names_the_variant(linked):
    """rs14274070 is not rs1427407: an id is read as a whole word."""
    with pytest.raises(lit.ExtractionRefused, match="names no variant the paper names"):
        extract(linked, comparison(NEAR_MISS, "sec1.2/p3", ["rs1427407"], direction="no_change", allele=""))
    null = extract(linked, comparison(NEAR_MISS, "sec1.2/p3", ["rs14274070"], direction="no_change", allele=""))
    assert (null.about_variants, null.result_kind) == (["rs14274070"], "null_in_assessed_scope")


# --- an allele comparison names its one variant ----------------------------------------------------------------------

def test_an_allele_comparison_must_name_a_variant_the_paper_names_for_it(linked, single):
    for variants in ([], ["the variant"], ["rs90000017"], ["rs999"]):
        with pytest.raises(lit.ExtractionRefused, match="compares alleles but names no variant"):
            extract(linked, comparison(CASE_SECTION, "sec1.1/p1", variants))
    with pytest.raises(lit.ExtractionRefused, match="not named where the passage is"):
        extract(linked, comparison(CASE_SECTION, "sec1.1/p1", ["rs90000017"]))
    with pytest.raises(lit.ExtractionRefused, match="article does not name"):
        extract(linked, comparison(CASE_SECTION, "sec1.1/p1", ["rs999"]))
    designed = record(CASE_SECTION, source_id="PMID:90000008", intervention="EMSA", endpoint="GATA1 binding",
                      compared_allele="T", direction="increases", about_tfs=["GATA1"], location="sec1.1/p1")
    with pytest.raises(lit.ExtractionRefused, match="compares alleles"):    # two alleles named and one compared
        extract(linked, designed)
    observed = extract(linked, designed.model_copy(update={"compared_allele": None}))
    assert (observed.allele, observed.about_variants) == (None, [])        # no allele kept: not an allele comparison
    retold = extract(single, comparison(INTRO, "sec1/p1", [], source="PMID:90000007"))
    assert retold.evidence_class == "review" and retold.about_variants == []   # context only: never refused for it


def test_one_allele_comparison_is_about_one_variant(linked):
    side = comparison(SIDE_BY_SIDE, "sec1.2/p2", ["rs1427407"], tf="TAL1")
    assert extract(linked, side).about_variants == ["rs1427407"]          # its paragraph names both variants
    with pytest.raises(lit.ExtractionRefused, match="one experiment per variant"):
        extract(linked, side.model_copy(update={"about_variants": ["rs1427407", "rs90000017"]}))
    both_forms = extract(linked, side.model_copy(update={"about_variants": ["rs1427407", "chr2:60490908"]}))
    assert both_forms.about_variants == ["rs1427407", "chr2:60490908 T>G"]   # one variant, as the paper writes it


# --- an article about one variant -------------------------------------------------------------------------------------

def test_a_passage_of_an_article_about_one_variant_need_not_name_it(single):
    graph, call, article = single
    for given, kept in ((["rs1427407"], ["rs1427407"]), (["chr2:60490908"], ["chr2:60490908 T>G"])):
        ev = extract(single, comparison(REVERSED, "sec2.2/p2", given, allele="G", direction="decreases",
                                        source="PMID:90000007"))
        assert ev.about_variants == kept                               # the article's one variant, written two ways
    with pytest.raises(lit.ExtractionRefused, match="article does not name"):
        extract(single, comparison(REVERSED, "sec2.2/p2", ["rs90000017"], source="PMID:90000007"))


def article_with(tmp_path, body: str) -> tuple[ClaimGraph, object, lit.Article]:
    """A one-off open-access article (PMC9000009) whose body is `body`, read once."""
    row = {**records()["PMC9000001"], "pmid": "90000009", "pmcid": "PMC9000009", "doi": None,
           "title": "An invented study of rs1427407"}
    xml = ('<article><front><article-meta><article-id pub-id-type="pmcid">PMC9000009</article-id>'
           '<article-id pub-id-type="pmid">90000009</article-id></article-meta></front>'
           f'<body><sec><title>Results</title>{body}</sec></body></article>')
    graph = ClaimGraph(case())
    http = FakeHttp({lit.metadata_url("PMC9000009", None): search_response([row]), lit.fulltext_url("PMC9000009"): xml})
    call = read(runner(http, tmp_path), graph, pmcid="PMC9000009")
    return graph, call, lit.load_article(tmp_path, call)


@pytest.mark.parametrize("written, kept", [
    ("<p>The variant lies at chr2:60,490,908 in the enhancer.</p>", []),         # another variant, for all we know
    ("<p>The variant rs1427407 (chr2:60,490,908 T&gt;G) lies in the enhancer.</p>", ["rs1427407"]),
    ("<p>The enhancer spans chr2:60,490,700-60,491,200; antibodies were used at 1:1000 and 1:200000.</p>",
     ["rs1427407"]),                                                              # a range and dilutions name none
    ("<p>We genotyped rs1427407 and rs90000017 (chr2:60,490,908; chr2:60,491,234).</p>", []),
])
def test_only_the_paper_writing_an_rsid_and_its_position_together_makes_them_one_variant(tmp_path, written, kept):
    paper = article_with(tmp_path / "run", f"{written}<p>{CASE_SECTION}</p>")
    rec = comparison(CASE_SECTION, "sec1/p2", ["rs1427407"], source="PMID:90000009")
    if kept:
        assert extract(paper, rec).about_variants == kept
    else:
        with pytest.raises(lit.ExtractionRefused, match="names no variant"):
            extract(paper, rec)


def test_a_listing_never_ties_one_variants_id_to_anothers_position(tmp_path):
    paper = article_with(tmp_path / "run", "<p>We genotyped rs1427407 and rs90000017 (chr2:60,490,908; "
                                           "chr2:60,491,234).</p><p>At chr2:60,490,908, the T allele probe bound "
                                           "GATA1 more strongly than the G allele probe.</p>")
    passage = "At chr2:60,490,908, the T allele probe bound GATA1 more strongly than the G allele probe."
    with pytest.raises(lit.ExtractionRefused, match="passage names chr2:60490908"):
        extract(paper, comparison(passage, "sec1/p2", ["rs90000017"], source="PMID:90000009"))
    assert extract(paper, comparison(passage, "sec1/p2", ["chr2:60490908"], source="PMID:90000009")).about_variants \
        == ["chr2:60490908"]


# --- what a perturbation can say about the alleles (core C3-2) ---------------------------------------------------------

def test_perturbations_say_what_they_cannot_show_about_the_alleles(single):
    graph, call, article = single
    knockdown = record(KNOCKDOWN, source_id="PMID:90000007", intervention="siRNA knockdown of GATA1",
                       endpoint="BCL11A mRNA", direction="decreases", about_tfs=["GATA1"], about_genes=["BCL11A"],
                       compared_allele="T", about_variants=["rs1427407"], manipulated="tf", location="sec2.1/p1")
    ev = lit.evidence_from_experiment(knockdown, call, article)
    assert ev.allele is None
    assert any("compared_allele 'T' is not kept: a TF perturbation does not test the variant's alleles" in x
               for x in ev.limitations)
    assert any("does not test what the variant's alleles do" in x and "context only" in x for x in ev.limitations)
    with pytest.raises(lit.ExtractionRefused, match="TF or gene perturbation, which does not test what the variant"):
        lit.evidence_from_experiment(knockdown.model_copy(update={"manipulated": "allele"}), call, article)
    eid = graph.add_evidence(ev, "literature_investigator")
    activity = case_claim(graph, "alters_regulatory_activity", EntityRef(kind="element", label="the enhancer"))
    with pytest.raises(GraphRefusal, match="does not test what the variant's alleles do"):   # the graph agrees
        graph.link(activity, eid, "supports", "literature_investigator", "the knockdown lowered BCL11A")
    deletion = lit.evidence_from_experiment(record(
        TT_DELETION, source_id="PMID:90000007", intervention="CRISPR/Cas9 deletion of the enhancer",
        endpoint="BCL11A mRNA", cell="HUDEP-2", genotype="TT", direction="decreases", about_genes=["BCL11A"],
        about_elements=["the enhancer containing rs1427407"], about_variants=["rs1427407"], manipulated="element",
        location="sec2.3/p2"), call, article)
    assert deletion.about_variants == ["rs1427407"]
    assert any("element perturbation" in x and "indirect at most" in x for x in deletion.limitations)
