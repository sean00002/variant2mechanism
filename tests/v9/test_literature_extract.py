"""Passage verification and extraction: an experiment becomes Evidence only from a verified passage (whole words, no
governing negation, typography folded but never a number) of the article a successful read returned; what it is
about (TFs, genes, elements, traits, the compared allele) only as the paper names it; its direction only as the
passage states it, in the frame claims use; retellings stay context; data flags only from what the paper states; and
the item enters a real ClaimGraph through add_evidence with retrieval_ref = the read."""

import pytest

from variant2mechanism.v9 import literature as lit
from variant2mechanism.v9.context_match import scope_from_label
from variant2mechanism.v9.graph import ClaimDraft, ClaimGraph, EntityRef, GraphRefusal, HypothesisDraft, SymbolResolver
from variant2mechanism.v9.schemas import evidence_strength

from .test_literature_fakes import FakeHttp, case, cases, read, record, routes, runner, search

# oa_fulltext.xml (PMC9000001)
EMSA = ("Electrophoretic mobility shift assays with K562 nuclear extract showed that the T allele probe bound GATA1 "
        "more strongly than the G allele probe")
REPORTER = ("luciferase constructs carrying the T allele gave 2.4-fold higher activity than constructs carrying the G "
            "allele (n = 6; P = 0.003)")
DELETION = "CRISPR/Cas9 deletion of the 300-bp enhancer region in HUDEP-2 cells reduced BCL11A mRNA by 60%"
BASE_EDIT = "Base editing that converted the T allele to G in HUDEP-2 cells lowered BCL11A expression by 35%"
CHIP = ("Allele-specific ChIP-qPCR in heterozygous K562 cells recovered more GATA1-bound fragments from the T allele "
        "than from the G allele")
# oa_cases.xml (PMC9000007): one case per paragraph
INTRO = ("Previous electrophoretic mobility shift assays in K562 nuclear extract showed that the T allele binds GATA1 "
         "more strongly than the G allele")
KNOCKDOWN = "siRNA knockdown of GATA1 in K562 cells reduced BCL11A mRNA by half"
NEGATED = "Overexpression of GATA1 did not increase BCL11A mRNA in K562 cells."
TF_NULL = "siRNA knockdown of GATA1 did not change SORT1 mRNA in HepG2 cells."
IN_VIVO_WORDS = "siRNA knockdown of GATA1 in K562 cells lowered in vivo GATA1 occupancy at the enhancer"
MIXED = "TAL1 binding was similar for both probes, whereas GATA-1 binding was threefold higher for the T allele probe."
REVERSED = "The G allele probe bound GATA1 less strongly than the T allele probe"
POWER = "Affinity for GATA1 differed by 10\u00b3-fold between the T and G probes"
RETOLD = "As previously reported, the T allele probe bound GATA1 more strongly than the G allele probe in K562 extract."
INDELS = "Cas9 genome editing that introduced small indels at the SNP in HUDEP-2 cells (TT at rs1427407) lowered BCL11A"
TT_DELETION = ("CRISPR/Cas9 deletion of the enhancer containing rs1427407 in HUDEP-2 cells (TT at rs1427407) reduced "
               "BCL11A mRNA by 60%.")
BARE_LETTERS = "A 300-bp deletion of the enhancer in primary T cells lowered IL2 mRNA."
MICE = "Mice lacking the enhancer had 40% lower plasma LDL cholesterol than wild-type littermates."
DISCUSSION = "Our EMSA results show that the T allele probe bound GATA1 more strongly than the G allele probe"
PLAIN_CHIP = "ChIP-qPCR showed GATA1 occupancy at the enhancer in K562 cells."
RAISED = "Overexpression of GATA1 raised BCL11A mRNA twofold in K562 cells."
TARGETED = "Targeting the enhancer with Cas9 lowered BCL11A mRNA in HUDEP-2 cells."


@pytest.fixture
def setup(tmp_path):
    """A graph, a runner writing raw/ under tmp_path, a successful read of the open-access article and its text."""
    graph = ClaimGraph(case())
    run_dir = tmp_path / "run"
    run = runner(FakeHttp(routes()), run_dir)
    call = read(run, graph, pmcid="PMC9000001", focus=["gata1"])
    return graph, run, call, lit.load_article(run_dir, call), run_dir


@pytest.fixture
def paper(tmp_path):
    """The extraction-cases article (oa_cases.xml), read once: (graph, call, article)."""
    return cases(tmp_path / "cases")


def emsa(**fields):
    """The EMSA of PMC9000001 (sec1.1/p1): an allele comparison that names the variant whose alleles it compared (the
    article names that one variant, in its abstract)."""
    return record(EMSA, **{"intervention": "EMSA with T and G allele probes", "endpoint": "GATA1 binding",
                           "compared_allele": "T", "manipulated": "allele", "direction": "increases",
                           "about_tfs": ["GATA1"], "about_variants": ["rs1427407"], "location": "sec1.1/p1", **fields})


def on_cases(passage: str, **fields):
    """A record citing the extraction-cases article."""
    return record(passage, source_id="PMID:90000007", **fields)


def probe(passage: str, location: str, **fields):
    """An EMSA record from the cases article's probe comparisons, naming its one variant."""
    return on_cases(passage, **{"intervention": "EMSA with T and G allele probes", "endpoint": "GATA1 binding",
                                "manipulated": "allele", "location": location, "about_variants": ["rs1427407"],
                                **fields})


def variant_claim(graph: ClaimGraph, relation: str, obj: EntityRef, direction: str, allele: str, cell: str) -> str:
    return graph.add_claim(ClaimDraft(subjects=[EntityRef(kind="variant", label="chr2:60490908")], relation=relation,
                                      objects=[obj], direction=direction, effect_allele=allele,
                                      context=scope_from_label(cell)), "coordinator")


def binding_claim(graph: ClaimGraph, tf: str = "GATA1") -> str:
    return variant_claim(graph, "alters_binding", EntityRef(kind="tf", label=tf), "increases", "T", "K562")


# --- verification -----------------------------------------------------------------------------------------------------

def test_passages_are_found_through_typographic_differences(setup):
    article = setup[3]
    assert lit.verify_passage(article, REPORTER) == "sec1.2/p1"                    # non-breaking hyphen and spaces
    assert lit.verify_passage(article, 'explain the "higher" enhancer activity - a hypothesis') == "sec2/p1"
    assert lit.verify_passage(article, "a fictional example with a soft hyphen") == "body/p1"   # ligature, soft hyphen
    assert lit.verify_passage(article, f"\u201c{EMSA}\u201d") == "sec1.1/p1"     # wrapping quotation marks
    assert lit.verify_passage(article, "the T allele probe   bound\nGATA1 more strongly") == "sec1.1/p1"
    assert lit.verify_passage(article, "with K562 nuclear extract") == "sec1.1/p1"
    assert lit.verify_passage(article, "with K562 nuclear extract", prefer="fig1") == "fig1"


def test_a_misquoted_or_unbounded_passage_is_not_verified(setup):
    article = setup[3]
    assert lit.verify_passage(article, EMSA.replace("T allele probe bound", "G allele probe bound")) is None
    assert lit.verify_passage(article, "the T allele probe bound GATA1 ... than the G allele probe") is None
    assert lit.verify_passage(article, "the t allele probe bound gata1 more strongly") is None   # case is kept
    assert lit.verify_passage(article, "GATA1") is None                                         # too short to mean much
    assert lit.verify_passage(article, EMSA + " " + "and more " * 70) is None                   # over 600 characters


def test_a_fragment_must_be_whole_words_and_keep_the_negation_that_governs_it(paper):
    article = paper[2]
    assert lit.verify_passage(article, "increase BCL11A mRNA in K562 cells") is None     # "did not" comes before it
    assert lit.verify_passage(article, "change SORT1 mRNA in HepG2 cells") is None       # "did not change"
    assert lit.verify_passage(article, NEGATED) == "sec2.1/p2"
    assert lit.verify_passage(article, "verexpression of GATA1 did not") is None         # starts mid-word
    assert lit.verify_passage(article, "Overexpression of GATA1 did no") is None         # ends mid-word


def test_a_quote_that_changes_a_number_is_not_verified_and_the_source_span_is_stored(paper):
    _, call, article = paper
    assert lit.verify_passage(article, POWER) == "sec2.2/p3"
    assert lit.verify_passage(article, POWER.replace("10\u00b3", "103")) is None        # a superscript is not a digit
    assert lit.verify_passage(article, "between the T and G probes (P = 3 \u00d7 10-8)") is None
    assert lit.verify_passage(article, "with a 10^3-fold difference in affinity") == "sec2.2/p2"   # JATS <sup>
    assert lit.verify_passage(article, "with a 103-fold difference in affinity") is None
    quoted = 'between the T and G probes (P = 3 \u00d7 10\u207b\u2078), as "expected" from the motif'
    ev = lit.evidence_from_experiment(on_cases(quoted, intervention="EMSA", endpoint="GATA1 affinity",
                                               about_tfs=["GATA1"], location="sec2.2/p3"), call, article)
    assert ev.experiment.passage == quoted.replace('"expected"', "\u201cexpected\u201d")   # the source's own text
    assert ev.experiment.passage in article.section("sec2.2/p3").text


# --- extraction refusals -------------------------------------------------------------------------------------------

def test_extraction_refuses_a_misquoted_passage(setup):
    _, _, call, article, _ = setup
    assert lit.evidence_from_experiment(emsa(), call, article).experiment.location == "sec1.1/p1"
    misquoted = emsa().model_copy(update={"passage": EMSA.replace("more strongly", "less strongly")})
    with pytest.raises(lit.ExtractionRefused, match="not in PMC9000001"):
        lit.evidence_from_experiment(misquoted, call, article)


def test_a_record_citing_another_article_is_refused(setup):
    _, _, call, article, _ = setup
    for cited in ({"source_id": "PMID:90000002"}, {"pmcid": "PMC9000002"}, {"doi": "10.5555/v2m.test.2"},
                  {"source_id": "not an identifier"}):
        with pytest.raises(lit.ExtractionRefused):
            lit.evidence_from_experiment(emsa().model_copy(update=cited), call, article)
    for same in ("PMCID:PMC9000001", "doi:10.5555/V2M.TEST.1", "https://doi.org/10.5555/v2m.test.1", "90000001"):
        ev = lit.evidence_from_experiment(emsa(source_id=same), call, article)
        assert ev.experiment.source_id == "PMID:90000001"                  # every id of the one article is kept


def test_only_a_successful_read_of_that_article_grounds_an_experiment(setup):
    graph, run, call, article, run_dir = setup
    searched = search(run, graph, "GATA1")                                 # nothing saved for it: a cache miss
    with pytest.raises(lit.ExtractionRefused, match="not a successful literature read"):
        lit.evidence_from_experiment(emsa(), searched, article)
    missed = read(run, graph, pmcid="PMC9000777")
    with pytest.raises(lit.ExtractionRefused, match="not a successful literature read"):
        lit.evidence_from_experiment(emsa(), missed, article)
    other = read(run, graph, pmcid="PMC9000002")
    with pytest.raises(lit.ExtractionRefused, match="is not the one"):
        lit.evidence_from_experiment(emsa(), other, article)


@pytest.mark.parametrize("intervention, reason", [
    ("eQTL mapping in whole blood", "names no assay"),
    ("EMSA and luciferase reporter assays", "several assays"),
])
def test_an_intervention_must_name_one_mapped_assay(setup, intervention, reason):
    _, _, call, article, _ = setup
    with pytest.raises(lit.ExtractionRefused, match=reason):
        lit.evidence_from_experiment(emsa().model_copy(update={"intervention": intervention}), call, article)


@pytest.mark.parametrize("intervention, cls", [
    ("electrophoretic mobility shift assay", "binding_assay"), ("supershift EMSA", "binding_assay"),
    ("biotinylated DNA pull-down", "binding_assay"), ("dual luciferase reporter", "reporter_assay"),
    ("MPRA", "reporter_assay"), ("luciferase reporter with a deleted motif", "reporter_assay"),
    ("ChIP-seq", "occupancy"), ("CUT&RUN", "occupancy"), ("CRISPRi", "perturbation"),
    ("siRNA knockdown then luciferase readout", "perturbation"), ("overexpression of GATA1", "perturbation"),
    ("deletion of the enhancer in mice", "perturbation"), ("microchip array", None),
])
def test_assay_class_comes_from_the_intervention(intervention, cls):
    assert lit.assay_class(intervention)[0] == cls


# --- what an extracted experiment becomes --------------------------------------------------------------------------

def test_one_paper_gives_several_evidence_items(setup):
    _, _, call, article, _ = setup
    items = {
        "emsa": emsa(),
        "reporter": record(REPORTER, intervention="luciferase reporter constructs carrying the T allele",
                           comparator="G allele construct", endpoint="luciferase activity", compared_allele="T",
                           manipulated="allele", direction="increases", about_variants=["rs1427407"],
                           location="sec1.2/p1"),
        "deletion": record(DELETION, intervention="CRISPR/Cas9 deletion of the 300-bp enhancer region",
                           endpoint="BCL11A mRNA", cell="HUDEP-2", direction="decreases", about_genes=["BCL11A"],
                           about_elements=["the 300-bp enhancer region"], manipulated="element",
                           location="sec1.3/p1"),
        "base_edit": record(BASE_EDIT, intervention="base editing converting the T allele to G",
                            endpoint="BCL11A expression", cell="HUDEP-2", compared_allele="G", manipulated="allele",
                            direction="decreases", about_genes=["BCL11A"], about_variants=["RS1427407"],
                            location="sec1.3/p2"),
        "chip": record(CHIP, intervention="allele-specific ChIP-qPCR for GATA1", endpoint="GATA1 occupancy",
                       compared_allele="T", direction="increases", about_tfs=["GATA1"],
                       about_variants=["rs1427407"], location="sec1.4/p1"),
    }
    ev = {k: lit.evidence_from_experiment(r, call, article) for k, r in items.items()}
    assert {k: e.evidence_class for k, e in ev.items()} == {
        "emsa": "binding_assay", "reporter": "reporter_assay", "deletion": "perturbation",
        "base_edit": "perturbation", "chip": "occupancy"}
    groups = {k: e.independence_group for k, e in ev.items()}
    assert len({groups[k] for k in ("emsa", "reporter", "deletion", "chip")}) == 4
    assert groups["deletion"] == groups["base_edit"]    # one paper, system and endpoint: not independent replications
    assert all(g.startswith("PMID:90000001#") for g in groups.values())
    for e in ev.values():
        assert e.source_ids == ["PMID:90000001", "PMCID:PMC9000001", "DOI:10.5555/v2m.test.1"]
        assert (e.retrieval_ref, e.origin, e.access, e.evidence_id) == (call.tool_call_id, "literature",
                                                                        "full_text", "")
        assert e.raw_artifact_ref == f"{call.raw_result_path}#{e.experiment.location}"
    assert ev["chip"].data == {"allele_specific": True}
    assert ev["base_edit"].data == {"allele_targeted": True}
    assert ev["reporter"].data == {"allele_targeted": True}       # constructs that differ at the compared allele
    assert ev["deletion"].data == {} and ev["emsa"].data == {}    # a region deletion is never an allele edit
    assert {k: e.allele for k, e in ev.items()} == {"emsa": "T", "reporter": "T", "deletion": None, "base_edit": "G",
                                                    "chip": "T"}
    assert {k: e.about_variants for k, e in ev.items()} == {   # as the graph reads them, on the record too (C3-1)
        "emsa": ["rs1427407"], "reporter": ["rs1427407"], "deletion": [], "base_edit": ["rs1427407"],
        "chip": ["rs1427407"]}
    assert all(e.experiment.about_variants == e.about_variants for e in ev.values())
    assert (ev["emsa"].direction, ev["emsa"].about_tfs) == ("increases", ["GATA1"])
    assert ev["deletion"].about_elements == ["the 300-bp enhancer region"]
    assert ev["emsa"].context.biosample == "K562" and ev["deletion"].context.biosample == "HUDEP-2"


def test_directions_are_read_in_the_frame_claims_use(setup, paper):
    """The record states the change the passage reports; the evidence states the effect of what was changed."""
    _, _, call, article, _ = setup
    deletion = lit.evidence_from_experiment(record(
        DELETION, intervention="CRISPR/Cas9 deletion of the 300-bp enhancer region", endpoint="BCL11A mRNA",
        cell="HUDEP-2", direction="decreases", about_genes=["BCL11A"], about_elements=["the 300-bp enhancer region"],
        manipulated="element", location="sec1.3/p1"), call, article)
    assert (deletion.experiment.direction, deletion.direction) == ("decreases", "increases")   # the region raises it
    assert any("removed or blocked" in x for x in deletion.limitations)
    graph, cases_call, cases_article = paper
    knockdown = lit.evidence_from_experiment(on_cases(
        KNOCKDOWN, intervention="siRNA knockdown of GATA1", endpoint="BCL11A mRNA", direction="decreases",
        about_tfs=["GATA1"], about_genes=["BCL11A"], manipulated="tf", location="sec2.1/p1"), cases_call, cases_article)
    assert knockdown.direction == "increases"                      # GATA1 raises BCL11A: its knockdown lowered it
    eid = graph.add_evidence(knockdown, "literature_investigator")
    activates = graph.add_claim(ClaimDraft(subjects=[EntityRef(kind="tf", label="GATA1")], relation="regulates",
                                           objects=[EntityRef(kind="gene", label="BCL11A")], direction="increases",
                                           context=scope_from_label("K562")), "coordinator")
    link = graph.link(activates, eid, "supports", "literature_investigator", "GATA1 knockdown lowered BCL11A")
    assert (link.stance, link.strength, link.applicability) == ("supports", "direct", "exact")
    raised = lit.evidence_from_experiment(on_cases(
        RAISED, intervention="overexpression of GATA1", endpoint="BCL11A mRNA", direction="increases",
        about_tfs=["GATA1"], about_genes=["BCL11A"], manipulated="tf", location="sec2.1/p5"), cases_call, cases_article)
    assert raised.direction == "increases"                         # a gain of GATA1 shows its effect as seen
    targeted = on_cases(TARGETED, intervention="Cas9 targeting of the enhancer", endpoint="BCL11A mRNA",
                        cell="HUDEP-2", direction="decreases", about_genes=["BCL11A"], manipulated="element",
                        location="sec2.3/p5")
    for intervention in ("Cas9 targeting of the enhancer", "dCas9-KRAB repression and dCas9-VP64 activation"):
        unplaced = lit.evidence_from_experiment(targeted.model_copy(update={"intervention": intervention}),
                                                cases_call, cases_article)
        assert unplaced.direction == "unspecified" and any("removed or added" in x for x in unplaced.limitations)


def test_flags_are_set_only_when_the_paper_states_them(setup, paper):
    _, _, call, article, _ = setup
    base = {"endpoint": "BCL11A mRNA", "cell": "HUDEP-2", "direction": "decreases", "manipulated": "element",
            "location": "sec1.3/p1"}
    for plain in ("CRISPR/Cas9 deletion of the enhancer region", "CRISPR/Cas9 deletion of the enhancer region in vivo"):
        assert lit.evidence_from_experiment(record(DELETION, intervention=plain, **base), call, article).data == {}
    said_by_the_paper = record(CHIP, intervention="ChIP-qPCR for GATA1", endpoint="GATA1 occupancy",
                               about_tfs=["GATA1"], location="sec1.4/p1")
    assert lit.evidence_from_experiment(said_by_the_paper, call, article).data == {"allele_specific": True}
    _, cases_call, cases_article = paper
    claimed_only = on_cases(PLAIN_CHIP, intervention="allele-specific ChIP-qPCR for GATA1", endpoint="GATA1 occupancy",
                            about_tfs=["GATA1"], location="sec2.4/p1")
    assert lit.evidence_from_experiment(claimed_only, cases_call, cases_article).data == {}   # the paper says no such
    in_cells = lit.evidence_from_experiment(on_cases(
        IN_VIVO_WORDS, intervention="siRNA knockdown of GATA1", endpoint="in vivo GATA1 occupancy (ChIP)",
        direction="decreases", about_tfs=["GATA1"], manipulated="tf", location="sec2.1/p4"), cases_call, cases_article)
    assert in_cells.data == {} and evidence_strength("contributes_to_trait", in_cells) == "indirect"   # a cell line
    mice = lit.evidence_from_experiment(on_cases(
        MICE, intervention="deletion of the enhancer in mice", endpoint="plasma LDL cholesterol", organism="mouse",
        cell="liver", direction="decreases", about_elements=["the enhancer"], about_traits=["LDL cholesterol"],
        manipulated="element", location="sec2.3/p4"), cases_call, cases_article)
    assert mice.data == {"in_vivo": True} and evidence_strength("contributes_to_trait", mice) == "direct"
    assert (mice.about_traits, mice.direction) == (["LDL cholesterol"], "increases")   # the enhancer raises LDL
    indels = lit.evidence_from_experiment(on_cases(
        INDELS, intervention="Cas9 genome editing introducing small indels at the SNP", endpoint="BCL11A mRNA",
        cell="HUDEP-2", compared_allele="T", manipulated="allele", direction="decreases", about_genes=["BCL11A"],
        about_variants=["rs1427407"], location="sec2.3/p1"), cases_call, cases_article)
    assert indels.data == {} and evidence_strength("causal_at_locus", indels) == "indirect"   # disruption, not an edit


def test_direction_and_allele_are_kept_only_when_the_passage_states_them(setup):
    _, _, call, article, _ = setup
    passage = "K562 and HUDEP-2 cells were cultured under standard erythroid conditions"
    ev = lit.evidence_from_experiment(record(passage, intervention="luciferase reporter", endpoint="activity",
                                             compared_allele="C", manipulated="allele", direction="increases",
                                             about_variants=["rs1427407"], location="sec3/p1"), call, article)
    assert (ev.direction, ev.allele) == ("unspecified", None)
    assert any("direction" in x for x in ev.limitations) and any("compared_allele" in x for x in ev.limitations)
    assert lit.evidence_from_experiment(emsa(), call, article).direction == "increases"


def test_a_reported_absence_of_effect_is_a_measured_null(setup):
    graph, _, call, article, _ = setup
    passage = "the T and G probes showed no difference in TAL1 binding in the same extracts"
    ev = lit.evidence_from_experiment(record(passage, intervention="EMSA", endpoint="TAL1 binding",
                                             direction="no_change", about_tfs=["TAL1"], location="sec1.1/p2"),
                                      call, article)
    assert (ev.result_kind, ev.assessed_relation, ev.direction) == ("null_in_assessed_scope", "alters_binding",
                                                                    "no_change")
    assert graph.add_evidence(ev, "literature_investigator").startswith("E")     # the graph takes it as a null
    with pytest.raises(lit.ExtractionRefused, match="absence of effect"):
        lit.evidence_from_experiment(emsa().model_copy(update={"direction": "no_change"}), call, article)


def test_a_hypothesis_stays_context(setup):
    _, _, call, article, _ = setup
    ev = lit.evidence_from_experiment(record("We propose that GATA1 recruitment to the T allele could explain",
                                             intervention="EMSA", endpoint="GATA1 binding", about_tfs=["GATA1"],
                                             authors_hypothesis_vs_result="hypothesis", location="sec2/p1"),
                                      call, article)
    assert evidence_strength("alters_binding", ev) == "context"
    assert any("hypothesis" in x for x in ev.limitations)


def test_a_review_is_context_only(tmp_path):
    graph = ClaimGraph(case())
    run = runner(FakeHttp(routes()), tmp_path / "run")
    call = read(run, graph, pmcid="PMC9000004")
    article = lit.load_article(tmp_path / "run", call)
    retold = record("Earlier gel shift experiments reported that the T allele binds GATA1 more strongly than the G "
                    "allele", intervention="gel shift", endpoint="GATA1 binding", source_id="PMID:90000004",
                    compared_allele="T", manipulated="allele", direction="increases", about_tfs=["GATA1"])
    ev = lit.evidence_from_experiment(retold, call, article)
    assert ev.evidence_class == "review" and ev.data == {}
    assert evidence_strength("alters_binding", ev) == "context"
    eid = graph.add_evidence(ev, "literature_investigator")
    claim = binding_claim(graph)
    with pytest.raises(GraphRefusal):
        graph.link(claim, eid, "supports", "literature_investigator", "the review says so")
    assert graph.link(claim, eid, "context_only", "literature_investigator", "background").stance == "context_only"


# --- what an experiment is about (review finding 1) ----------------------------------------------------------------

def test_a_factor_the_section_does_not_name_never_stands_in_for_another(setup):
    graph, _, call, article, _ = setup
    with pytest.raises(lit.ExtractionRefused, match="factor it measured"):
        lit.evidence_from_experiment(emsa().model_copy(update={"about_tfs": ["TAL1"]}), call, article)
    both = lit.evidence_from_experiment(emsa().model_copy(update={"about_tfs": ["GATA1", "TAL1"]}), call, article)
    assert both.about_tfs == ["GATA1"] and any("TAL1" in x and "not named" in x for x in both.limitations)
    eid = graph.add_evidence(both, "literature_investigator")
    with pytest.raises(GraphRefusal, match="not TAL1"):                     # the GATA1 assay never supports TAL1
        graph.link(binding_claim(graph, "TAL1"), eid, "supports", "literature_investigator", "EMSA")
    assert graph.link(binding_claim(graph), eid, "supports", "literature_investigator", "EMSA").strength == "direct"


def test_the_papers_spelling_and_hgnc_previous_symbols_name_the_same_factor(setup, paper):
    _, _, call, article, _ = setup
    resolver = SymbolResolver({"GATA1": ("GATA1", "HGNC:4170"), "GF1": ("GATA1", "HGNC:4170")})
    with pytest.raises(lit.ExtractionRefused, match="factor it measured"):    # GF1 is not written in the section
        lit.evidence_from_experiment(emsa().model_copy(update={"about_tfs": ["GF1"]}), call, article)
    previous = lit.evidence_from_experiment(emsa().model_copy(update={"about_tfs": ["GF1"]}), call, article,
                                            resolver=resolver)
    assert previous.about_tfs == ["GF1"]                                   # the graph's resolver makes it GATA1
    _, cases_call, cases_article = paper
    mixed = probe(MIXED, "sec2.2/p1", compared_allele="T", direction="increases")
    for given, kept in ((["GATA1"], ["GATA1"]), (["GATA-1"], ["GATA-1"])):    # the paper writes GATA-1
        ev = lit.evidence_from_experiment(mixed.model_copy(update={"about_tfs": given}), cases_call, cases_article)
        assert ev.about_tfs == kept
    spelled = lit.evidence_from_experiment(mixed.model_copy(update={"about_tfs": ["GATA-1"]}), cases_call,
                                           cases_article, resolver=resolver)
    assert spelled.about_tfs == ["GATA1"]                                  # stored as the approved symbol


def test_a_tf_manipulation_never_tests_what_an_element_does(paper):
    graph, call, article = paper
    knockdown = on_cases(KNOCKDOWN, intervention="siRNA knockdown of GATA1", endpoint="BCL11A mRNA",
                         direction="decreases", about_tfs=["GATA1"], about_genes=["BCL11A"],
                         about_elements=["the enhancer"], manipulated="tf", location="sec2.1/p1")
    ev = lit.evidence_from_experiment(knockdown, call, article)
    assert ev.about_elements == [] and any("does not test what an element does" in x for x in ev.limitations)
    with pytest.raises(lit.ExtractionRefused, match="knockdown, overexpression or inhibitor"):
        lit.evidence_from_experiment(knockdown.model_copy(update={"manipulated": "element"}), call, article)
    with pytest.raises(lit.ExtractionRefused, match="TF manipulation is about that TF"):
        lit.evidence_from_experiment(knockdown.model_copy(update={"about_tfs": ["TAL1"]}), call, article)
    null = lit.evidence_from_experiment(on_cases(
        TF_NULL, intervention="siRNA knockdown of GATA1", endpoint="SORT1 mRNA", cell="HepG2", direction="no_change",
        about_tfs=["GATA1"], about_genes=["SORT1"], manipulated="tf", location="sec2.1/p3"), call, article)
    assert (null.result_kind, null.assessed_relation, null.about_elements) == ("null_in_assessed_scope", "regulates",
                                                                               [])
    eid = graph.add_evidence(null, "literature_investigator")
    regulates = graph.add_claim(ClaimDraft(subjects=[EntityRef(kind="element", label="the enhancer")],
                                           relation="regulates", objects=[EntityRef(kind="gene", label="SORT1")],
                                           direction="increases", context=scope_from_label("HepG2")), "coordinator")
    hid = graph.add_hypothesis(HypothesisDraft(title="E drives SORT1", required_claim_ids=[regulates],
                                               mechanism_class="regulatory", reason_for_inclusion="test"),
                               "coordinator")
    with pytest.raises(GraphRefusal, match="names that element"):
        graph.link(regulates, eid, "contradicts", "literature_investigator", "the knockdown left SORT1 unchanged")
    assert graph.hypotheses[hid].disposition == "active"                  # no false rejection


def test_an_element_is_kept_only_as_the_paper_names_it(paper):
    _, call, article = paper
    deletion = on_cases(TT_DELETION, intervention="CRISPR/Cas9 deletion of the enhancer", endpoint="BCL11A mRNA",
                        cell="HUDEP-2", genotype="TT", direction="decreases", about_genes=["BCL11A"],
                        about_elements=["the enhancer containing rs1427407", "the enhancer containing rs999",
                                        "EH38E0000042"], manipulated="element", location="sec2.3/p2")
    ev = lit.evidence_from_experiment(deletion, call, article)
    assert ev.about_elements == ["the enhancer containing rs1427407"]
    assert any("rs999" in x and "EH38E0000042" in x for x in ev.limitations)
    observed = lit.evidence_from_experiment(deletion.model_copy(update={"manipulated": "none"}), call, article)
    assert observed.about_elements == [] and any("does not say what" in x for x in observed.limitations)


# --- the allele a direction refers to (review finding 2) -----------------------------------------------------------

def test_a_genotype_is_never_the_allele_a_direction_refers_to(paper):
    graph, call, article = paper
    deletion = on_cases(TT_DELETION, intervention="CRISPR/Cas9 deletion of the enhancer", endpoint="BCL11A mRNA",
                        cell="HUDEP-2", genotype="TT", direction="decreases", about_genes=["BCL11A"],
                        about_elements=["the enhancer containing rs1427407"], manipulated="element",
                        location="sec2.3/p2")
    ev = lit.evidence_from_experiment(deletion, call, article)
    assert (ev.allele, ev.context.genotype) == (None, "TT")
    for value, why in (("TT", "not one allele"), ("T/G", "not one allele"), ("homozygous T", "not one allele"),
                       ("T", "an element perturbation does not compare the variant's alleles")):
        given = lit.evidence_from_experiment(deletion.model_copy(update={"compared_allele": value}), call, article)
        assert given.allele is None and any(why in x for x in given.limitations)
    eid = graph.add_evidence(ev, "literature_investigator")
    activity = variant_claim(graph, "alters_regulatory_activity",
                             EntityRef(kind="element", label="the enhancer containing rs1427407"), "decreases", "G",
                             "HUDEP-2")
    hid = graph.add_hypothesis(HypothesisDraft(title="G lowers the enhancer", required_claim_ids=[activity],
                                               mechanism_class="regulatory", reason_for_inclusion="test"),
                               "coordinator")
    with pytest.raises(GraphRefusal, match="cannot be placed"):           # a region deletion says nothing of G or T
        graph.link(activity, eid, "contradicts", "literature_investigator", "deletion in TT cells")
    assert graph.hypotheses[hid].disposition == "active"


def test_a_bare_letter_is_not_an_allele(paper):
    _, call, article = paper
    for letter in ("A", "T"):                       # "A 300-bp deletion ...", "... primary T cells ..."
        ev = lit.evidence_from_experiment(on_cases(
            BARE_LETTERS, intervention="deletion of the enhancer", endpoint="IL2 mRNA", cell="primary T cell",
            compared_allele=letter, manipulated="allele", direction="decreases", about_genes=["IL2"],
            about_variants=["rs1427407"], location="sec2.3/p3"), call, article)
        assert ev.allele is None and any("not named as an allele" in x for x in ev.limitations)


# --- the direction the passage states (review finding 3) -----------------------------------------------------------

def test_a_direction_opposite_to_the_passage_is_refused(setup):
    _, _, call, article, _ = setup
    with pytest.raises(lit.ExtractionRefused, match="opposite direction"):
        lit.evidence_from_experiment(record(DELETION, intervention="CRISPR/Cas9 deletion of the 300-bp enhancer "
                                            "region", endpoint="BCL11A mRNA", cell="HUDEP-2", direction="increases",
                                            about_genes=["BCL11A"], manipulated="element", location="sec1.3/p1"),
                                     call, article)


def test_the_reference_side_of_a_comparison_is_read_as_such(paper):
    _, call, article = paper
    for allele, direction in (("T", "increases"), ("G", "decreases")):
        ev = lit.evidence_from_experiment(probe(REVERSED, "sec2.2/p2", about_tfs=["GATA1"], compared_allele=allele,
                                                direction=direction), call, article)
        assert (ev.allele, ev.direction) == (allele, direction)
    for allele, direction in (("T", "decreases"), ("G", "increases")):
        with pytest.raises(lit.ExtractionRefused, match="opposite direction"):
            lit.evidence_from_experiment(probe(REVERSED, "sec2.2/p2", about_tfs=["GATA1"], compared_allele=allele,
                                               direction=direction), call, article)


def test_each_factor_is_held_to_what_the_passage_says_about_it(paper):
    graph, call, article = paper
    with pytest.raises(lit.ExtractionRefused, match="states an effect"):  # GATA-1 was threefold higher
        lit.evidence_from_experiment(probe(MIXED, "sec2.2/p1", about_tfs=["GATA1"], direction="no_change"), call,
                                     article)
    tal1 = lit.evidence_from_experiment(probe(MIXED, "sec2.2/p1", about_tfs=["TAL1"], direction="no_change"), call,
                                        article)
    assert (tal1.result_kind, tal1.assessed_relation) == ("null_in_assessed_scope", "alters_binding")
    with pytest.raises(lit.ExtractionRefused, match="states no change"):
        lit.evidence_from_experiment(probe(MIXED, "sec2.2/p1", about_tfs=["TAL1"], compared_allele="T",
                                           direction="increases"), call, article)
    gata1 = lit.evidence_from_experiment(probe(MIXED, "sec2.2/p1", about_tfs=["GATA1"], compared_allele="T",
                                               direction="increases"), call, article)
    assert (gata1.allele, gata1.direction, gata1.result_kind) == ("T", "increases", "effect")
    negated = on_cases(NEGATED, intervention="overexpression of GATA1", endpoint="BCL11A mRNA", about_tfs=["GATA1"],
                       about_genes=["BCL11A"], manipulated="tf", location="sec2.1/p2")
    with pytest.raises(lit.ExtractionRefused, match="states no change"):
        lit.evidence_from_experiment(negated.model_copy(update={"direction": "increases"}), call, article)
    null = lit.evidence_from_experiment(negated.model_copy(update={"direction": "no_change"}), call, article)
    assert (null.result_kind, null.assessed_relation) == ("null_in_assessed_scope", "regulates")
    with pytest.raises(GraphRefusal, match="measured null"):              # a null is never support for an effect
        claim = graph.add_claim(ClaimDraft(subjects=[EntityRef(kind="tf", label="GATA1")], relation="regulates",
                                           objects=[EntityRef(kind="gene", label="BCL11A")], direction="increases",
                                           context=scope_from_label("K562")), "coordinator")
        graph.link(claim, graph.add_evidence(null, "literature_investigator"), "supports", "literature_investigator",
                   "overexpression")


# --- retellings (review finding 4) --------------------------------------------------------------------------------

def test_a_retelling_is_context_never_a_second_observation(setup, tmp_path):
    graph, _, call, article, _ = setup
    original = graph.add_evidence(lit.evidence_from_experiment(emsa(), call, article), "literature_investigator")
    run_dir = tmp_path / "cases"
    cases_call = read(runner(FakeHttp(routes()), run_dir), graph, pmcid="PMC9000007")
    cases_article = lit.load_article(run_dir, cases_call)
    retellings = {location: lit.evidence_from_experiment(probe(passage, location, about_tfs=["GATA1"],
                                                               compared_allele="T", direction="increases"),
                                                         cases_call, cases_article)
                  for passage, location in ((INTRO, "sec1/p1"), (DISCUSSION, "sec3/p1"), (RETOLD, "sec2.2/p4"))}
    for ev in retellings.values():
        assert ev.evidence_class == "review" and ev.data == {} and any("retelling" in x for x in ev.limitations)
        assert evidence_strength("alters_binding", ev) == "context"
    claim = binding_claim(graph)
    assert graph.link(claim, original, "supports", "literature_investigator", "EMSA").strength == "direct"
    retold = graph.add_evidence(retellings["sec1/p1"], "literature_investigator")
    with pytest.raises(GraphRefusal):                  # the introduction's retelling is not a second support
        graph.link(claim, retold, "supports", "literature_investigator", "the introduction says so")


# --- load_article, find_read and the claim graph -------------------------------------------------------------------

def test_load_article_returns_the_saved_text_and_refuses_otherwise(setup):
    graph, run, call, article, run_dir = setup
    assert (article.key, article.access, article.route) == ("PMC9000001", "full_text", "europepmc_fulltext")
    missed = read(run, graph, pmcid="PMC9000777")
    with pytest.raises(lit.ExtractionRefused, match="not a successful literature read"):
        lit.load_article(run_dir, missed)
    raw = run_dir / call.raw_result_path
    raw.write_text(raw.read_text().replace("more strongly", "less strongly"))
    with pytest.raises(lit.ExtractionRefused, match="changed since"):
        lit.load_article(run_dir, call)
    raw.unlink()
    with pytest.raises(lit.ExtractionRefused, match="missing"):
        lit.load_article(run_dir, call)


def test_find_read_finds_the_article_by_any_of_its_ids(tmp_path):
    graph = ClaimGraph(case())
    run = runner(FakeHttp(routes()), tmp_path / "run")
    by_pmid = read(run, graph, pmid="90000001")
    assert by_pmid.read_article == "PMC9000001"
    for cited in ("PMCID:PMC9000001", "doi:10.5555/v2m.test.1", "PMID:90000001"):
        assert lit.find_read(graph, emsa(source_id=cited)).tool_call_id == by_pmid.tool_call_id
    with pytest.raises(lit.ExtractionRefused, match="no literature read"):
        lit.find_read(graph, emsa(source_id="PMID:90000002"))


def test_an_extracted_experiment_enters_the_claim_graph(setup):
    graph, _, call, article, _ = setup
    ev = lit.evidence_from_experiment(emsa(), call, article)
    eid = graph.add_evidence(ev, "literature_investigator")
    stored = graph.evidence[eid]
    assert stored.retrieval_ref == call.tool_call_id and stored.experiment.location == "sec1.1/p1"
    assert stored.about_variants == stored.experiment.about_variants == ["rs1427407"]
    assert graph.events[-1].action == "add_evidence"
    cited_by_pmcid = lit.evidence_from_experiment(emsa(source_id="PMCID:PMC9000001"), call, article)
    assert graph.add_evidence(cited_by_pmcid, "literature_investigator") == eid     # one article, one experiment
    claim = binding_claim(graph)
    link = graph.link(claim, eid, "supports", "literature_investigator", "EMSA: the T probe binds GATA1 more")
    assert (link.applicability, link.strength) == ("exact", "direct")
    graph.assess(claim, "supported_in_scope", "a direct allele comparison in K562 extract", "critic",
                 graph.claims[claim].version)
    assert graph.claims[claim].assessment == "supported_in_scope"


def test_extraction_bounds_the_extractors_own_text(setup):
    _, _, call, article, _ = setup
    pasted = " ".join(s.text for s in article.sections)                  # stands in for pasted article paragraphs
    ev = lit.evidence_from_experiment(emsa().model_copy(update={
        "result": pasted, "comparator": pasted, "scope_supports": pasted * 3, "scope_does_not_test": pasted * 2,
        "about_traits": [pasted]}), call, article)
    x = ev.experiment
    assert len(ev.observed_result) <= lit.RESULT_LIMIT and x.result == ev.observed_result
    assert all(len(v) <= lit.FIELD_LIMIT for v in (x.comparator, x.scope_supports, x.scope_does_not_test,
                                                    *ev.limitations))
    assert ev.about_traits == [] and len(x.passage) <= lit.PASSAGE_MAX
