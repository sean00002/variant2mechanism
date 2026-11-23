"""The fill: the chain table filled by code from databases and model predictions, and, with a reader, from articles.

Why: a language model is worth its cost only where it does something code cannot. Before any model is asked, code
alone can state every claim its own sources can speak to and attach every record they return. What comes out is the
floor a model-driven run has to beat, the "code only" arm of every comparison, and the table a reader and a
proposer later add to. It is also what an unstudied variant gets when no article exists.

What code does, in order (run):

1. Lookups, as role code. After the evidence bundle (commands.collect_evidence: the variant's annotation, its cCRE,
   the QBiC-SELEX inventory, its eQTLs, its GWAS associations, the ChIP-seq survey), code asks what the candidates
   need: every credible set holding the variant; the ChIP-seq peaks of each TF that the survey lists and a
   gate-passing QBiC-SELEX group covers; those TFs' expression, when the request names a context; and, for each
   candidate gene, Open Targets' own evidence linking it to the variant's traits (fill_tools.py).

2. Claims. Code states a claim when a record on file can count for it, and never otherwise, so the candidates are
   the data's and not a list code made up:
       TF binding, alleles differ      one claim per model-sharing group with a gate-passing QBiC-SELEX prediction
       TF binding, in place            a TF of such a group occupies the variant's site; it is expressed in the context
       regulatory activity, in place   the variant lies in the element a registry places it in
       target gene, alleles differ     one claim per gene with an eQTL of this variant, or a colocalising
                                       expression or splicing QTL (a protein QTL is often a trans effect)
       target gene, in place           the variant's element regulates a gene it was perturbed against
       trait, alleles differ           one claim per trait term with an association or a credible set of this variant
       trait, in place                 a candidate gene bears on such a trait
   The one database source that compares the two alleles' regulatory activity is ADASTRA's allele-specific reads of
   a protein that does not bind DNA itself (proteins.py): where a variant has such a record, code states the claim
   for the variant's site. A claim that the alleles differ states no direction. The records say which allele (a
   prediction for T, an eQTL slope), and a measurement in the other direction is then still a record that they
   differ, never a contradiction of something a prediction alone asserted.

3. Links, through the graph's own gates (identity, variant, direction, context), each with a rationale written by
   code. A record the graph refuses is logged with the graph's reason, so the table lists it as set aside. Every
   record that names what a claim names is therefore counted, listed beside it or set aside: nothing is left
   unjudged.

4. Presence, never size. ChIP-seq counts as support that a TF is in place when a peak contains the variant; the
   signal is not read. Expression counts when the level reaches EXPRESSED_TPM, the usual convention for a detected
   transcript; a lower level is linked as context only, with the level in its rationale, and is evidence of nothing.
   Neither is required: a TF with no peak and no level keeps its claim and its place among equals, and only loses a
   tie to one whose presence is on record (chain.py). Without a context in the request, expression is not looked
   up: where the TF would act is unknown, so a level says nothing.

5. Assessment by the graph's gate: a claim is supported in scope when a record of a class that can establish it is
   linked in scope and none goes against it. Code proposes nothing the gate would refuse.

6. The result. A chain is an answer even when a link is predicted only: the summary says which links are measured,
   associated, predicted or empty. A leading chain with a link that holds no record is reported as a partial
   mechanism, which is every chain code fills alone, since no source of its own fills regulatory activity; with a
   record on every link it is a leading explanation, or several when chains tie. With no chain at all the run
   reports that nothing was found.

7. Articles, when the run has a reader (reader.py). The reader finds the articles that name the variant and has a
   model read each once; what comes back is a set of experiments, each with the passage it was read from. Code,
   not the model, decides what each one bears on, by what it manipulated and what it read out (read_targets):
       alleles compared in a binding assay, or allele-specific ChIP reads   the alleles differ in binding the TF
       ChIP at the variant's site                                           the TF occupies the site
       alleles compared in a reporter, or an edit read out as activity      the alleles differ in regulatory activity
       an allele edit read out as a gene's RNA                              the alleles differ in the gene's RNA
       the two alleles' transcripts in heterozygous cells                   the same claim, as an association
       the element perturbed, a gene's RNA read out                         the element regulates the gene
       an allele edit read out as a trait                                   the alleles differ in the trait
       the gene perturbed, a trait read out                                 the gene bears on the trait
   An experiment is not a database row: the graph may refuse it for the claim it would need (a TF knockdown offered
   as a test of an element, an assay of a neighbouring variant). A claim stated for a refused record would stand in
   the answer with nothing behind it, so a claim and its link are made in one step that is undone when the graph
   refuses the link, and the refusal is logged for the slot. A measured null counts against a claim only in the
   claim's exact scope (the graph's rule); elsewhere it is linked beside the claim, and no claim is stated for a
   null alone. Every experiment on file therefore has a judgement: counted, beside, or set aside with a reason.

8. A second reading, when the run has a critic (critic.py). Before any experiment is linked, code works out which
   experiments stand alone: the only one counted for, or the only one counted against, some claim. Taking such a
   record out changes a cell; taking out one of several changes none, so only those are read. A second model, from
   another provider than the reader's, is shown each with its quotation in its paragraph and the claims code
   counts it for, and says of each whether the text shows it. Code acts on the answer: a claim the critic answers
   "not shown" does not get the record, which is set aside with the critic's reason, and a claim that would have
   been stated for that record alone is not stated; where the critic names further sentences of the paragraph as
   the ones that state the result, code copies them and the table quotes them with the record. Every other
   answer, and no answer at all, leaves the record where the steps above put it. The critic cannot add a record,
   a claim or a link.

9. A tie, when the run has a judge (judge.py). After the assessments the order of chains is final. When several
   chains share the first rank, code lists what they differ in (a TF, a target gene) and, for each such candidate,
   the experiments read from articles that name it and that no cell counts for it: a TF removed and the allele
   difference read out, the element deleted and a gene's protein read out. A second model reads them and answers
   for each candidate whether an experiment ties it to the variant's site; with two or more candidates it is asked
   twice, in opposite orders, and only an answer both readings give is kept. The answers are written under the
   tie. No cell, no rank and no count of tied chains changes.

The request's disease, when given, limits the trait claims to the terms that name it; its context scopes the claims
whose records depend on a cell or tissue (occupancy, expression, eQTLs, perturbations).
"""

from collections.abc import Iterable, Mapping
from dataclasses import dataclass
from typing import Any

from . import critic as K
from . import judge as J
from . import literature as L
from . import table as T
from .bundle import inventory_items, inventory_table
from .chain import LINK_KEYS, chain_view
from .context_match import is_unscoped, link_applicability, normalise_scope
from .graph import ClaimDraft, ClaimGraph, EntityRef, GraphRefusal
from .proteins import COFACTOR_FLAG, NOT_TF_NAMES
from .schemas import CONTEXT_FREE_CLASSES, ContextScope, Evidence, Role, RunResult, ToolCall, ToolRequest
from .tools import ToolRunner
from .traits import ontology_id, trait_query_match

# 4: allele-specific ChIP of a protein that does not bind DNA itself bears on the site's activity, not on a TF's
# binding (3: ties are ordered by a strong QBiC-SELEX prediction; 2: ADASTRA is asked)
FILL_FORMAT = 4
DRIVER = "code_only_fill"          # no model call at all
READER_DRIVER = "fill_with_reader"  # the same fill, with articles read by a model (reader.py)
DRIVERS = (DRIVER, READER_DRIVER)
ROLE: Role = "code"
EXPRESSED_TPM = 1.0                # the usual convention for a detected transcript; a presence call, never a ranking
NAMED = 8                          # TF symbols spelt out in one rationale
SUPPORTED = "a record of a class that can establish it is linked in scope, and none goes against it"
ASSESSED = {"supported_in_scope": SUPPORTED,
            "contradicted_in_scope": "a measured null of a class that can test it is linked in its exact scope, and "
                                     "no record of such a class supports it",
            "contested": "records of a class that can test it are linked on both sides"}
PURPOSE = {
    "credible_sets_all": "every credible set holding the variant, for the trait and gene claims",
    "tf_occupancy_set": "ChIP-seq peaks of the candidate TFs: is each one bound at the variant's site",
    "tf_expression_set": "expression of the candidate TFs in the request's context",
    "gene_disease": "does this candidate gene bear on a trait the variant is associated with",
    "adastra_asb": "allele-specific ChIP-seq reads called at the variant, for any protein assayed",
}
MECHANISM = {"alters_binding": "tf_binding", "occupies": "tf_binding", "expressed_in": "tf_binding",
             "overlaps": "regulatory", "regulates": "regulatory", "associated_with_expression": "regulatory",
             "alters_regulatory_activity": "regulatory", "alters_rna": "regulatory",
             "associated_with_trait": "association_only", "contributes_to_trait": "other"}
ASSAY_WORDS = {"binding_assay": "a binding assay", "occupancy": "ChIP", "reporter_assay": "a reporter assay",
               "perturbation": "a perturbation", "association": "allele-specific expression"}
MANIPULATED_WORDS = {"allele": "an allele comparison or edit", "element": "a perturbation of the element",
                     "tf": "a TF perturbation", "gene": "a gene perturbation", "none": "an observation"}
ASSESSMENTS = ("supported_in_scope", "contradicted_in_scope", "contested")   # tried in this order; the gate decides
Target = tuple[tuple, ClaimDraft, str, str]            # (key, the claim, the stance code links with, the rationale)


@dataclass(frozen=True)
class Term:
    """A trait as a record names it: the label of the term its source mapped it to, with that term's ontology id, or
    the source's own label when it mapped none."""
    label: str
    ident: str | None = None


def _unique(values: Iterable[Any]) -> list[Any]:
    return list(dict.fromkeys(v for v in values if v))


def _named(values: list[str]) -> str:
    return ", ".join(values[:NAMED]) + (f" and {len(values) - NAMED} more" if len(values) > NAMED else "")


def variant_name(graph: ClaimGraph) -> str:
    """How code names the case variant in a sentence: its rsID (supplied, else the first one recorded as its own),
    else its position and alleles."""
    v = graph.case.variant
    return v.rsid or next(iter(graph.variant_aliases), None) or f"chr{v.chrom}:{v.pos} {v.ref}>{v.alt}"


def scopes(graph: ClaimGraph) -> list[ContextScope | None]:
    """The contexts a context-dependent claim is stated in: each context the request supplies, or one unscoped
    claim when it supplies none."""
    found = [normalise_scope(s, variant=graph.case.variant) for s in graph.case.supplied_context]
    return [s for s in found if s is not None and not is_unscoped(s)] or [None]


def candidate_groups(graph: ClaimGraph) -> dict[str, dict[str, Any]]:
    """The model-sharing groups with a gate-passing QBiC-SELEX prediction, by group id in the inventory's own neutral
    order: the group's DBD label, its members as the inventory lists them, its Evidence items and the TFs those items
    are about (the TFs the gate-passing models map to)."""
    items = inventory_items(graph)
    out: dict[str, dict[str, Any]] = {}
    for row in inventory_table(graph):
        gid = str(row.get("group_id"))
        if gid not in items:
            continue
        members = [str(m.get("tf")) for m in row.get("members") or [] if isinstance(m, dict) and m.get("tf")]
        tfs = _unique(tf for eid in items[gid] for tf in graph.evidence[eid].about_tfs)
        out[gid] = {"dbd": str(row.get("dbd") or ""), "members": members or tfs, "items": items[gid], "tfs": tfs}
    return out


class Fill:
    """One fill of one graph (see the module docstring). `runner` runs the lookups; without one (a test, or a graph
    that already holds them) only the claims, links, assessments and result are made. `reader` (reader.Reader, or
    anything with its run(graph)) reads the articles; without one no article is read and no model is called.
    `critic` (critic.Critic) reads the experiments that stand alone behind a cell against the claims code counts
    them for; without one every experiment is linked as code judges it."""

    def __init__(self, graph: ClaimGraph, runner: ToolRunner | None = None, reader: Any = None, critic: Any = None,
                 judge: Any = None):
        self.graph, self.runner, self.reader, self.critic, self.judge = graph, runner, reader, critic, judge
        self.reading: dict[str, Any] | None = None
        self.critique: dict[str, Any] | None = None
        self.judgement: dict[str, Any] | None = None       # the judge's reading of a tie; None without a tie
        self.groups = candidate_groups(graph)
        self.scopes = scopes(graph)
        self.claims: dict[tuple, str] = {}
        self.by_slot: dict[str, list[str]] = {key: [] for key in T.SLOT_KEYS}
        self.links = self.beside = self.refused = 0
        self._observed: dict[str, dict[str, dict[str, Any]]] = {}
        self._by_member: dict[str, list[str]] | None = None

    # --- lookups -------------------------------------------------------------------------------------------------------

    def _ask(self, tool: str, **params: Any) -> ToolCall | None:
        if self.runner is None or tool not in {s.name for s in self.runner.specs("computational")}:
            return None
        return self.runner.run(ToolRequest(tool=tool, params=params, purpose=PURPOSE[tool]), self.graph.case,
                               self.graph, ROLE)

    def survey_tfs(self) -> set[str]:
        """The TFs the ChIP-seq survey lists with a peak containing the variant (upper case)."""
        return {str(o["tf"]).upper() for t in self.graph.tool_calls.values()
                if t.tool_name == "chip_occupancy" and t.execution_status == "success"
                and not t.query_parameters.get("tf")
                for o in t.observations if o.get("record") == "factor" and o.get("tf")}

    def lookups(self) -> list[ToolCall]:
        graph = self.graph
        tfs = sorted({tf for g in self.groups.values() for tf in g["tfs"]})
        calls = [self._ask("credible_sets_all"), self._ask("adastra_asb")]
        bound = sorted(set(tfs) & self.survey_tfs())
        if bound:
            calls.append(self._ask("tf_occupancy_set", tfs=bound))
        if tfs and self.scopes != [None]:
            calls.append(self._ask("tf_expression_set", tfs=tfs))
        ids = sorted({term.ident for ev in graph.evidence.values()
                      if ev.origin == "tool" and self._bears(ev, "trait.allele")
                      for term in self.terms(ev) if term.ident})
        genes = sorted({gene for ev in graph.evidence.values() if ev.origin == "tool"
                        for slot in ("gene.allele", "gene.premise", "trait.premise") if self._bears(ev, slot)
                        for gene in ev.about_genes})
        if ids:
            calls += [self._ask("gene_disease", gene=gene, traits=ids) for gene in genes]
        calls = [c for c in calls if c is not None]
        if calls:
            graph.log("collect_facts", ROLE, "lookups for the chain table: " + "; ".join(
                f"{c.tool_call_id} {c.tool_name}: {c.execution_status}/{c.retrieval_status}" for c in calls),
                target_ids=[c.tool_call_id for c in calls if c.tool_call_id],
                evidence_ids=[e for c in calls for e in c.evidence_ids],
                details={"candidate_tfs": len(tfs), "tfs_with_a_peak": len(bound), "genes": genes,
                         "trait_terms": len(ids)})
        return calls

    # --- what a record is about ----------------------------------------------------------------------------------------

    def _tool(self, ev: Evidence) -> str | None:
        call = self.graph.tool_calls.get(ev.retrieval_ref or "")
        return call.tool_name if call is not None else None

    def _bears(self, ev: Evidence, slot: str) -> bool:
        """Whether the map lists this record for one of the slot's cells, the class matrix lets it count, and, for a
        claim that the alleles differ, it names this variant."""
        s = T.SLOTS[slot]
        return (T.listed(slot, T.lane_of(ev), self._tool(ev), ev) and T.can_count(s, ev)
                and (s.part != "allele" or T.names_case(self.graph, ev)))

    def _observation(self, ev: Evidence, record: str, key: str, value: Any) -> dict[str, Any]:
        """The observation of the record's own tool call that describes it (its accession, its study locus)."""
        ref = ev.retrieval_ref or ""
        if ref not in self._observed:
            call = self.graph.tool_calls.get(ref)
            self._observed[ref] = {}
            for o in call.observations if call else []:
                for field in ("accession", "study_locus_id", "study_id"):
                    if o.get(field):
                        self._observed[ref].setdefault(f"{o.get('record')}:{field}:{o[field]}", o)
        return self._observed[ref].get(f"{record}:{key}:{value}", {})

    def terms(self, ev: Evidence) -> list[Term]:
        """The trait terms a record is about: the ontology terms its source mapped the trait to, each with the
        source's label for it; where it mapped none, the source's own trait label. With a disease in the request,
        only the terms that name it."""
        tool, found = self._tool(ev), []
        if tool == "gwas_associations":
            row = self._observation(ev, "association", "accession", ev.data.get("accession"))
            found = [Term(str(x["label"]), str(x["id"])) for x in row.get("efo") or [] if x.get("label") and x.get("id")]
            found = found or [Term(str(t)) for t in (row.get("reported_traits") or [])[:1]]
        elif tool in ("credible_sets_all", "credible_sets_l2g"):
            row = (self._observation(ev, "set", "study_locus_id", ev.data.get("study_locus_id"))
                   or self._observation(ev, "set", "study_id", ev.data.get("study_id")))
            found = [Term(str(d["name"]), str(d["id"])) for d in row.get("diseases") or []
                     if d.get("name") and d.get("id")]
            found = found or ([Term(str(row["trait"]))] if row.get("trait") else [])
        elif tool == "gene_disease":
            found = [Term(str(ev.data.get("disease") or ""), str(ev.data.get("disease_id") or "") or None)]
        if not found:                              # any other source: the first label it names that is not an id
            found = [Term(x) for x in ev.about_traits if not ontology_id(x)][:1]
        wanted = self.graph.case.supplied_disease
        return [t for t in _unique(found) if t.label and (
            not wanted or any(trait_query_match(d, [t.label, t.ident or ""]) for d in wanted))]

    # --- claims --------------------------------------------------------------------------------------------------------

    def _variant(self) -> EntityRef:
        return EntityRef(kind="variant", entity_id=self.graph.variant_entity())

    def _claim(self, slot: str, key: tuple, draft: ClaimDraft) -> str:
        """The claim for this key, stated once (role code)."""
        full = (slot, *key)
        if full not in self.claims:
            draft = draft.model_copy(update={"mechanism_class": MECHANISM[draft.relation]})
            self.claims[full] = self.graph.add_claim(draft, ROLE, draft.assertion_text)
            self.by_slot[slot].append(self.claims[full])
        return self.claims[full]

    def _in(self, scope: ContextScope | None) -> str:
        return f" in {scope.label or scope.biosample or scope.tissue}" if scope is not None else ""

    def _scoped(self, ev: Evidence) -> list[ContextScope | None]:
        """The scopes whose claim a context-dependent record is linked to: those it matches (exact or proxy), else
        the first, where the graph stores it as context only."""
        if self.scopes == [None]:
            return [None]
        free = ev.evidence_class in CONTEXT_FREE_CLASSES and ev.result_kind == "effect"
        fits = [s for s in self.scopes if link_applicability(s, ev.context, context_free=free) in ("exact", "proxy")]
        return fits or self.scopes[:1]

    def _group(self, gid: str) -> EntityRef:
        group = self.groups[gid]
        registered = self.graph.groups is not None and self.graph.groups.members(gid) is not None
        # named by its id alone, so the chain view always spells out its first members
        return EntityRef(kind="tf_group", label=gid, canonical_id=gid,
                         members=[] if registered else list(group["members"]))

    def _members(self, gid: str) -> list[str]:
        """A candidate group's member TFs as the graph's group entity has them: the registry's, else the inventory's."""
        registered = self.graph.groups.members(gid) if self.graph.groups is not None else None
        return list(registered) if registered is not None else list(self.groups[gid]["members"])

    def _groups_of(self) -> dict[str, list[str]]:
        """TF symbol (upper case) -> the candidate groups it is a member of."""
        if self._by_member is None:
            self._by_member = {}
            for gid in self.groups:
                for tf in self._members(gid):
                    self._by_member.setdefault(tf.upper(), []).append(gid)
        return self._by_member

    def _covered(self) -> set[str]:
        """The TFs a binding claim covers: the members and model TFs of every candidate group (upper case)."""
        return {tf.upper() for g in self.groups.values() for tf in [*g["members"], *g["tfs"]]}

    def targets(self, slot: str, ev: Evidence) -> list[tuple[tuple, ClaimDraft, str, str]]:
        """The claims a record bears on in one slot: (key, the claim, the stance code links it with, the rationale).
        Empty when the record names nothing a claim of that slot is about."""
        graph, v, name = self.graph, self._variant(), variant_name(self.graph)
        out: list[tuple[tuple, ClaimDraft, str, str]] = []

        def add(key: tuple, relation: str, subjects: list[EntityRef], objects: list[EntityRef], text: str,
                rationale: str, scope: ContextScope | None = None, stance: str = "supports") -> None:
            out.append((key, ClaimDraft(subjects=subjects, relation=relation, objects=objects, context=scope,
                                        assertion_text=text), stance, rationale))

        if slot == "activity.allele" and self._tool(ev) == "adastra_asb":
            # allele-specific ChIP-seq reads of a protein that does not bind DNA itself (the source map sends only
            # those here): the state of the site differs between the alleles, and the claim names the site, no TF
            site = self._site(ev)
            who = _named(list(ev.about_tfs))
            add((site.label,), "alters_regulatory_activity", [v], [site],
                f"The two alleles of {name} differ in the regulatory activity of {site.label}.",
                f"ADASTRA: ChIP-seq reads of {who}, which does not bind DNA itself, favour "
                + (f"the {ev.allele} allele" if ev.allele else "one allele in some experiments and the other in "
                                                                "others")
                + " over the variant: the site's state differs between the alleles")
        elif slot == "binding.allele" and self._tool(ev) == "adastra_asb":
            # allele-specific ChIP-seq reads are about the TF that was pulled down, whether or not it is a candidate
            # of QBiC-SELEX: the claim names that TF, as a claim stated for an article's allele-specific ChIP does
            for tf in ev.about_tfs:
                add((tf,), "alters_binding", [v], [EntityRef(kind="tf", label=tf)],
                    f"The two alleles of {name} differ in binding {tf}.",
                    f"ADASTRA: ChIP-seq reads of {tf} over the variant favour "
                    + (f"the {ev.allele} allele" if ev.allele else "one allele in some experiments and the other "
                                                                    "in others"))
        elif slot == "binding.allele":
            # a prediction bears on its own group's claim, and on the claim of any other candidate group that has
            # one of the TFs it is about as a member (a model can map to TFs of two groups)
            own = str(ev.data.get("group_id"))
            about = {tf.upper() for tf in ev.about_tfs}
            for gid in _unique([own, *(g for tf in sorted(about) for g in self._groups_of().get(tf, []))]):
                if gid not in self.groups:
                    continue
                shared = [tf for tf in self._members(gid) if tf.upper() in about]
                add((gid,), "alters_binding", [v], [self._group(gid)],
                    f"The two alleles of {name} differ in binding {self.groups[gid]['dbd'] or 'TF'} group {gid} "
                    f"({_named(self.groups[gid]['tfs'])}).",
                    f"QBiC-SELEX: the gate-passing models of {_named(list(ev.about_tfs))} predict more binding to "
                    f"the {ev.allele} allele" if gid == own else
                    f"QBiC-SELEX: gate-passing models of group {own}, which also cover {_named(shared)} of this "
                    f"group, predict more binding to the {ev.allele} allele")
        elif slot == "binding.premise":
            covered = self._covered()
            for tf in ev.about_tfs:
                if tf.upper() not in covered:
                    continue
                factor = EntityRef(kind="tf", label=tf)
                if ev.evidence_class == "occupancy":
                    for scope in self._scoped(ev):
                        add((tf, "occupies", self._in(scope)), "occupies", [factor], [v],
                            f"{tf} occupies the site of {name}{self._in(scope)}.",
                            f"a ChIP-seq peak of {tf} contains the variant", scope)
                    continue
                tpm = ev.data.get("tpm", ev.data.get("median_tpm"))
                if tpm is None or ev.context is None:
                    continue
                expressed = float(tpm) >= EXPRESSED_TPM
                rationale = (f"{tf} at {float(tpm):g} TPM, at or above the {EXPRESSED_TPM:g} TPM convention for a "
                             "detected transcript" if expressed else
                             f"{tf} at {float(tpm):g} TPM, below the {EXPRESSED_TPM:g} TPM convention for a detected "
                             "transcript: not counted as expressed, and no evidence against it")
                for scope in self._scoped(ev) if self.scopes != [None] else [ev.context]:
                    label = scope.label or scope.biosample or scope.tissue or "the context"
                    add((tf, "expressed_in", label), "expressed_in", [factor],
                        [EntityRef(kind="context", label=label)], f"{tf} is expressed in {label}.", rationale, scope,
                        "supports" if expressed else "context_only")
        elif slot == "activity.premise":
            placed = {x.casefold() for x in graph.variant_elements}
            for element in ev.about_elements:
                if not (T.names_case(graph, ev) or element.casefold() in placed):
                    continue
                add((element,), "overlaps", [v], [EntityRef(kind="element", label=element, canonical_id=element)],
                    f"{name} lies in the regulatory element {element}.",
                    "a registry places the variant in this element" if T.names_case(graph, ev) else
                    "the element's class in a biosample of the request's context")
        elif slot == "gene.allele":
            for gene in ev.about_genes:
                for scope in self._scoped(ev):
                    add((gene, self._in(scope)), "associated_with_expression", [v],
                        [EntityRef(kind="gene", label=gene)],
                        f"The two alleles of {name} differ in the RNA of {gene}{self._in(scope)}.",
                        f"an eQTL of this variant for {gene}" if ev.evidence_class == "association" else
                        f"a trait signal holding this variant colocalises with a QTL of {gene}", scope)
        elif slot == "gene.premise":
            placed = {x.casefold() for x in graph.variant_elements}
            for element in ev.about_elements:
                if element.casefold() not in placed:
                    continue
                for gene in ev.about_genes:
                    for scope in self._scoped(ev):
                        add((element, gene, self._in(scope)), "regulates",
                            [EntityRef(kind="element", label=element, canonical_id=element)],
                            [EntityRef(kind="gene", label=gene)],
                            f"The element {element}, which holds {name}, regulates {gene}{self._in(scope)}.",
                            f"a perturbation of {element} changed {gene}", scope)
        elif slot == "trait.allele":
            for term in self.terms(ev):
                add((term,), "associated_with_trait", [v],
                    [EntityRef(kind="phenotype", label=term.label, canonical_id=term.ident)],
                    f"The two alleles of {name} differ in {term.label}.",
                    f"an association of this variant with {term.label}" if ev.evidence_class == "association" else
                    f"a credible set for {term.label} holds this variant" if ev.evidence_class == "statistical_inference"
                    else f"a clinical assertion about this variant and {term.label}")
        elif slot == "trait.premise" and ev.evidence_class != "dependency_screen":
            for gene in ev.about_genes:
                for term in self.terms(ev):
                    what = (f"Open Targets: {ev.data.get('datasource')} links {gene} to {term.label}"
                            if self._tool(ev) == "gene_disease" else
                            f"the locus-to-gene model scores {gene} for the {term.label} signal"
                            if ev.evidence_class == "precomputed_prediction" else
                            f"the {term.label} signal colocalises with a QTL of {gene}")
                    add((gene, term), "contributes_to_trait", [EntityRef(kind="gene", label=gene)],
                        [EntityRef(kind="phenotype", label=term.label, canonical_id=term.ident)],
                        f"{gene} bears on {term.label}.", what)
        return out

    # --- experiments read from articles ----------------------------------------------------------------------------------

    def _at_site(self, ev: Evidence) -> bool:
        """Whether an experiment is about this variant's site: it names the variant, or an element recorded as
        holding it. Without that, ChIP "at the enhancer" or a deletion of "the region" could be about any site."""
        placed = {x.casefold() for x in self.graph.variant_elements}
        return T.names_case(self.graph, ev) or any(
            x.casefold() in placed or self.graph.variant_mention(x) == "case" for x in ev.about_elements)

    def _site(self, ev: Evidence) -> EntityRef:
        """The element a claim about the site's activity names for this experiment: the element a registry places
        the variant in, unless the article names the region in its own terms (a "2.1-kb fragment"), which is then
        kept as the article names it, since code cannot tell that the two are one region."""
        placed = list(self.graph.variant_elements)
        known = {x.casefold() for x in placed}
        own = [x for x in ev.about_elements
               if x.casefold() not in known and self.graph.variant_mention(x) != "case"]
        if own:
            return EntityRef(kind="element", label=own[0])
        if placed:
            return EntityRef(kind="element", label=placed[0], canonical_id=placed[0])
        # No registry places the variant in an element: the claim then names the region as the article does when the
        # article names it by this variant ("the 88-bp region flanking rs9349379"), so the record that states it is
        # a record about it. A label of code's own would be an element no record names.
        named = [x for x in ev.about_elements if self.graph.variant_mention(x) == "case"]
        if named:
            return EntityRef(kind="element", label=named[0])
        return EntityRef(kind="element", label=f"the site of {variant_name(self.graph)}")

    def read_targets(self, slot: str, ev: Evidence) -> tuple[list[Target], str]:
        """The claims an experiment read from an article bears on in one slot, and, when it bears on none, why (the
        table lists it as set aside with that reason). What decides is what the experiment manipulated and what it
        read out, never what a model proposed: see the module docstring, step 7."""
        v, name = self._variant(), variant_name(self.graph)
        x = ev.experiment
        cls, readout = ev.evidence_class, L._endpoint_category(x.endpoint)
        null = ev.result_kind == "null_in_assessed_scope"
        stance = "contradicts" if null else "supports"
        where = f"{ev.source_ids[0]} {x.location}" if ev.source_ids else x.location
        how, did = ASSAY_WORDS.get(cls, cls), MANIPULATED_WORDS[x.manipulated]
        # The graph's own test (ClaimGraph._strength): an experiment compares the alleles when it changed or compared
        # them, or its verified passage names the allele its result is for. A ChIP peak or a reporter of the region
        # compares none. An edit the record calls an exchange of alleles is taken as one unless the article states
        # the opposite: a description or a quotation that speaks of a cut, an indel, a deletion or a disruption is a
        # perturbation of the site, whatever the record calls it (the reader is told to file a cut as a change to the
        # element; this catches the ones it does not). The engine's allele_targeted flag, set when the article states
        # a conversion, overrides the wording.
        converted = ev.data.get("allele_targeted") is True
        site_edit = (cls == "perturbation" and x.manipulated == "allele" and not converted
                     and bool(L._DISRUPTION.search(L._fold(x.intervention, x.passage))))
        # What only the reader could see (reader.reader_flags): a comparison of haplotypes that differ at several
        # variants does not isolate this one, so only allele-specific expression, which is filed as an association,
        # may count for a claim about its alleles; and a result the article itself calls not significant, a trend or
        # inconsistent is neither an effect nor a measured null, so it counts for nothing.
        if ev.data.get("unclear_result") is True:
            return [], ("the article calls this difference not significant, a trend or inconsistent: neither an "
                        "effect nor a measured null")
        if slot.endswith(".allele") and ev.data.get("haplotype_comparison") is True and cls != "association":
            return [], ("it compares haplotypes that differ at more variants than this one, so it does not isolate "
                        "this variant's alleles")
        compares = (x.manipulated == "allele" or bool(ev.allele)) and not site_edit
        not_swapped = ("an edit at the variant that its description or quotation gives as a cut, an indel or a "
                       "deletion: it perturbs the site and exchanges no allele, so it is counted under what the "
                       "element does")
        # An article's name for a TF or gene that today names one gene and once named another (TCF4 was the symbol
        # of TCF7L2): code cannot tell which gene the article means, so the record states nothing about either.
        named = ev.about_tfs if slot.startswith("binding.") else ev.about_genes if slot != "activity.allele" else []
        former = self.graph.resolver.formerly if self.graph.resolver is not None else (lambda _name: ())
        unclear = [f"{n} (today's {n}, and formerly the symbol of {' and '.join(former(n))})"
                   for n in named if former(n)]
        if unclear:
            return [], (f"the article's name {'; '.join(unclear)} can mean either gene, and code cannot tell which "
                        "the article means")
        out: list[Target] = []

        def add(key: tuple, relation: str, subjects: list[EntityRef], objects: list[EntityRef], text: str,
                saw: str, scope: ContextScope | None = None) -> None:
            if null and ev.assessed_relation != relation:
                return                                     # a null for another relation says nothing about this one
            rationale = f"{how} {'saw no ' + saw.removeprefix('a ') if null else 'shows ' + saw} ({where})"
            out.append((key, ClaimDraft(subjects=subjects, relation=relation, objects=objects, context=scope,
                                        assertion_text=text), stance, rationale))

        if slot == "binding.allele":
            if not ev.about_tfs:
                return [], "it names no TF"
            if not compares:
                return [], (f"{how} that compares no alleles: it shows the TF at the site, which is counted under "
                            "the TF being in place")
            # ChIP of a protein that does not bind DNA itself (proteins.py) says nothing about a TF's binding
            other = set(ev.data.get(NOT_TF_NAMES) or []) if cls == "occupancy" else set()
            if other and not set(ev.about_tfs) - other:
                return [], (f"ChIP of {_named(sorted(other))}, which does not bind DNA by sequence: a difference "
                            "between the alleles in it is counted under the site's regulatory activity")
            for tf in [tf for tf in ev.about_tfs if tf not in other]:
                add((tf,), "alters_binding", [v], [EntityRef(kind="tf", label=tf)],
                    f"The two alleles of {name} differ in binding {tf}.",
                    f"a difference between the alleles in binding {tf}")
        elif slot == "binding.premise":
            if not ev.about_tfs:
                return [], "it names no TF"
            if not self._at_site(ev):
                return [], "it names neither this variant nor an element recorded as holding it"
            for tf in ev.about_tfs:
                for scope in self._scoped(ev):
                    add((tf, "occupies", self._in(scope)), "occupies", [EntityRef(kind="tf", label=tf)], [v],
                        f"{tf} occupies the site of {name}{self._in(scope)}.", f"{tf} at the variant's site", scope)
        elif slot == "activity.allele":
            if cls == "perturbation" and readout not in ("reporter", "chromatin"):
                return [], f"its readout ({readout}) is not the site's regulatory activity"
            if site_edit:
                return [], not_swapped
            if not compares:
                return [], (f"{how} that compares no alleles ({did}): it shows the site is active, not that the "
                            "alleles differ")
            if cls == "occupancy" and ev.data.get(COFACTOR_FLAG) is not True:
                return [], "ChIP of a TF: a difference between the alleles in it is counted under TF binding"
            site = self._site(ev)
            # ChIP counts here only as allele-specific reads of a protein that is not a TF (the class matrix)
            saw = (f"a difference between the alleles in the occupancy of {_named(list(ev.about_tfs))}, which does "
                   "not bind DNA by sequence, so the site's state differs" if cls == "occupancy" else
                   "a difference between the alleles in regulatory activity")
            add((site.label,), "alters_regulatory_activity", [v], [site],
                f"The two alleles of {name} differ in the regulatory activity of {site.label}.", saw)
        elif slot == "gene.allele" and cls == "association":
            # Allele-specific expression: the transcripts of the two alleles in the same cells. It compares the two
            # haplotypes, not this variant alone, so it joins the claim an eQTL of the variant states.
            if not compares:
                return [], "allele-specific expression that does not say which of this variant's alleles it compared"
            if not ev.about_genes:
                return [], "it names no gene"
            for gene in ev.about_genes:
                for scope in self._scoped(ev):
                    add((gene, self._in(scope)), "associated_with_expression", [v],
                        [EntityRef(kind="gene", label=gene)],
                        f"The two alleles of {name} differ in the RNA of {gene}{self._in(scope)}.",
                        f"a difference between the alleles in {gene} RNA", scope)
        elif slot == "gene.allele":
            if cls != "perturbation":
                return [], "a reporter measures the site's activity: it is counted under regulatory activity"
            if x.manipulated != "allele":
                return [], f"{did}, not a comparison of the alleles"
            if site_edit:
                return [], not_swapped
            if readout != "expression" or not ev.about_genes:
                return [], f"its readout ({readout}) is not a named gene's RNA"
            for gene in ev.about_genes:
                for scope in self._scoped(ev):
                    add((gene, "rna", self._in(scope)), "alters_rna", [v], [EntityRef(kind="gene", label=gene)],
                        f"Changing the allele of {name} changes the RNA of {gene}{self._in(scope)}.",
                        f"a change in {gene} RNA when the allele is changed", scope)
        elif slot == "gene.premise":
            if x.manipulated != "element" and not site_edit:
                return [], f"{did}, not a test of what the element does"
            if readout != "expression" or not ev.about_genes:
                return [], f"its readout ({readout}) is not a named gene's RNA"
            if not self._at_site(ev):
                return [], "it names neither this variant nor an element recorded as holding it"
            site = self._site(ev)
            for gene in ev.about_genes:
                for scope in self._scoped(ev):
                    add((site.label, gene, self._in(scope)), "regulates", [site],
                        [EntityRef(kind="gene", label=gene)],
                        f"The element {site.label}, which holds {name}, regulates {gene}{self._in(scope)}.",
                        f"a change in {gene} RNA when the element is perturbed", scope)
        elif slot == "trait.allele":
            if x.manipulated != "allele" or readout != "phenotype" or not ev.about_traits:
                return [], f"{did} read out as {readout}, not an allele edit read out as a named trait"
            if site_edit:
                return [], not_swapped
            for trait in ev.about_traits:
                add(("read", trait), "contributes_to_trait", [v], [EntityRef(kind="phenotype", label=trait)],
                    f"Changing the allele of {name} changes {trait}.", f"a change in {trait} when the allele is changed")
        elif slot == "trait.premise":
            if x.manipulated != "gene" or readout != "phenotype" or not (ev.about_genes and ev.about_traits):
                return [], f"{did} read out as {readout}, not a gene perturbed and a named trait read out"
            for gene in ev.about_genes:
                for trait in ev.about_traits:
                    add((gene, "read", trait), "contributes_to_trait", [EntityRef(kind="gene", label=gene)],
                        [EntityRef(kind="phenotype", label=trait)], f"{gene} bears on {trait}.",
                        f"a change in {trait} when {gene} is perturbed")
        if not out:
            return [], (f"a measured null for {ev.assessed_relation}, which is not what this claim states" if null
                        else "it names nothing a claim of this kind is about")
        return out, ""

    def _aside(self, slot: str, ev: Evidence, claim_id: str | None, why: str, stance: str = "supports",
               **details: Any) -> None:
        """Log that code judged a record for a slot and did not count it, so the table lists it as set aside."""
        self.refused += 1
        self.graph.log("refuse_update", ROLE, f"{ev.evidence_id} not counted for {claim_id or T.SLOTS[slot].text}: "
                                              f"{why}",
                       target_ids=[t for t in (claim_id, ev.evidence_id) if t], evidence_ids=[ev.evidence_id],
                       details={"kind": "attach_evidence", "slot": slot, "stance": stance,
                                "stated": claim_id is not None, **details})

    def _link_read(self, slot: str, target: Target, ev: Evidence) -> str | None:
        """State one claim for an experiment (unless code already states it) and link the experiment, as one step:
        when the graph refuses the link, the claim is not stated either. A null the graph will not count against an
        existing claim (it is outside the claim's exact scope) is linked beside it; no claim is stated for a null.
        Returns the claim the experiment now counts for or against, or None when it counts for none."""
        graph = self.graph
        key, draft, stance, rationale = target
        full = (slot, *key)
        known = self.claims.get(full)
        if known is None and stance == "contradicts":
            self._aside(slot, ev, None, "a measured null, and no record on file states the claim it would count "
                                        "against", stance)
            return None
        cid = known
        try:
            with graph.batch():
                if cid is None:
                    cid = graph.add_claim(draft.model_copy(update={"mechanism_class": MECHANISM[draft.relation]}),
                                          ROLE, draft.assertion_text)
                link = graph.link(cid, ev.evidence_id, stance, ROLE, rationale)
        except GraphRefusal as r:
            if known is not None and stance == "contradicts":
                try:
                    graph.link(known, ev.evidence_id, "context_only", ROLE,
                               f"{rationale}; not counted against the claim: {r.reason}")
                    self.beside += 1
                    return None
                except GraphRefusal:
                    pass
            self._aside(slot, ev, known, r.reason, stance)
            return None
        if known is None:
            self.claims[full] = cid
            self.by_slot[slot].append(cid)
        counted = link.stance in ("supports", "contradicts")
        self.links += counted
        self.beside += not counted
        return cid if counted else None

    def attach_read(self) -> None:
        """Judge every experiment read from an article for every slot it could count in: link it to the claims it
        bears on (read_targets), or log why it bears on none. Results that found an effect come first and measured
        nulls after them, so whether a null finds a claim to stand beside never depends on the order the articles
        were read in. With a critic, the experiments that stand alone behind a cell are read a second time before
        anything is linked (_second_readings), and each is then linked as the answer allows."""
        read = [e for e in self.graph.evidence.values() if e.origin == "literature" and e.experiment is not None]
        plan = [(ev, [(slot, *self.read_targets(slot, ev)) for slot in T.SLOT_KEYS if self._bears(ev, slot)])
                for ev in sorted(read, key=lambda e: e.result_kind == "null_in_assessed_scope")]
        readings = self._second_readings(plan)
        for ev, judged in plan:
            checks = readings.get(ev.evidence_id)
            for slot, targets, why in judged:
                if not targets:
                    self._aside(slot, ev, None, why)
                for target in targets:
                    check = (checks or {}).get((slot, target[0]))
                    if check is not None and check.verdict == "not_shown":
                        self._aside(slot, ev, self.claims.get((slot, *target[0])), K.refusal(check), target[2],
                                    critic=self._verdict(check))
                        continue
                    cid = self._link_read(slot, target, ev)
                    if cid is not None and checks is not None:
                        self._note_reading(cid, ev, slot, check)
        if self.critic is not None:
            sides = K.counted_by_side(K.linked_items(self.graph))
            self.critic.alone_not_sent = len(K.alone(sides, readings))

    def _counted_alone(self, plan: list[tuple[Evidence, list[tuple]]]) -> dict[tuple, list[str]]:
        """What code alone would count: every planned experiment is linked as it would be without a critic, the
        experiments counted under each claim and stance are noted, and all of it is undone. The graph's gates decide
        what counts, so this asks them and leaves no trace: neither a claim, a link nor a logged refusal remains."""
        kept = (dict(self.claims), {slot: list(ids) for slot, ids in self.by_slot.items()},
                self.links, self.beside, self.refused)
        counted: dict[tuple, list[str]] = {}

        class Undo(Exception):
            pass

        try:
            with self.graph.batch():
                for ev, judged in plan:
                    for slot, targets, _ in judged:
                        for target in targets:
                            if self._link_read(slot, target, ev) is not None:
                                counted.setdefault((slot, target[0], target[2]), []).append(ev.evidence_id)
                raise Undo
        except Undo:
            pass
        self.claims, self.by_slot, self.links, self.beside, self.refused = kept
        return counted

    def _second_readings(self, plan: list[tuple[Evidence, list[tuple]]]) -> dict[str, dict[tuple, Any]]:
        """The critic's answers, by experiment and then by slot and claim key (module docstring, step 8). Only an
        experiment that stands alone is sent: the only one counted for, or the only one counted against, some claim.
        An answer that takes a record out of a claim can leave another record alone there, so the question is asked
        again until no record that stands alone is unread. An experiment sent is asked about every claim code counts
        it for; one not sent is linked as code judges it. Empty without a critic; an experiment the critic gave no
        reply for has an empty entry."""
        if self.critic is None:
            return {}
        counted = self._counted_alone(plan)
        targets = {ev.evidence_id: (ev, [(slot, t) for slot, found, _ in judged for t in found
                                         if ev.evidence_id in counted.get((slot, t[0], t[2]), ())])
                   for ev, judged in plan}
        readings: dict[str, dict[tuple, Any]] = {}
        while True:
            left = K.alone(counted, readings)
            if not left:
                break
            for eid in left:
                ev, asked = targets[eid]
                checks = self.critic.review(self.graph, ev, [K.Asked(draft.assertion_text, stance, rationale)
                                                             for _, (_, draft, stance, rationale) in asked])
                readings[eid] = {(slot, t[0]): check for (slot, t), check in zip(asked, checks, strict=True)
                                 if check is not None}
                for (slot, t), check in zip(asked, checks, strict=True):
                    if check is not None and check.verdict == "not_shown":
                        counted[(slot, t[0], t[2])].remove(eid)
        for eid, (ev, asked) in targets.items():
            if asked and eid not in readings:
                self.critic.skip(ev, len(asked))
        return readings

    @staticmethod
    def _verdict(check: Any) -> dict[str, Any]:
        found: dict[str, Any] = {"verdict": check.verdict, "fault": check.fault,
                                 "reason": " ".join(check.reason.split())[:K.REASON_LIMIT]}
        if getattr(check, "passage", ""):
            # the critic pointed to sentences outside the quotation, and code copied them (critic.pointed)
            found.update(passage=check.passage, sentences=list(check.sentences))
        return found

    def _note_reading(self, cid: str, ev: Evidence, slot: str, check: Any) -> None:
        """Log what the critic said of a record that is counted for a claim, so the table can say it beside the
        record: that it agrees, that it found the result in further sentences (which the table then quotes), that
        it could not tell, or that it gave no answer."""
        found = self._verdict(check) if check is not None else {"verdict": "not_reviewed", "fault": "none",
                                                                "reason": "the critic gave no answer for it"}
        self.graph.log("audit", K.CRITIC if check is not None else ROLE,
                       f"{ev.evidence_id} counted for {cid}; the critic: {found['verdict']}"
                       + (", with the result in further sentences of the paragraph" if found.get("passage") else "")
                       + (f" ({found['reason']})" if found["reason"] and check is not None else ""),
                       target_ids=[cid, ev.evidence_id], evidence_ids=[ev.evidence_id],
                       details={"critic": {**found, "slot": slot}})

    # --- links, assessments, the result ----------------------------------------------------------------------------------

    def attach(self) -> None:
        """State every claim a record on file can count for and link the record, in evidence order. A link the graph
        refuses is logged with the graph's reason (the table then lists the record as set aside)."""
        graph = self.graph
        for ev in [e for e in graph.evidence.values() if e.origin == "tool"]:
            for slot in T.SLOT_KEYS:
                if not self._bears(ev, slot):
                    continue
                for key, draft, stance, rationale in self.targets(slot, ev):
                    cid = self._claim(slot, key, draft)
                    try:
                        link = graph.link(cid, ev.evidence_id, stance, ROLE, rationale)
                    except GraphRefusal as r:
                        self.refused += 1
                        graph.log("refuse_update", ROLE, f"{ev.evidence_id} not linked to {cid}: {r.reason}",
                                  target_ids=[cid, ev.evidence_id], evidence_ids=[ev.evidence_id],
                                  details={"kind": "attach_evidence", "slot": slot, "stance": stance})
                        continue
                    counted = link.stance == "supports"
                    self.links += counted
                    self.beside += not counted

    def assess(self) -> None:
        """Assess each claim code stated, where the graph's gate allows it: supported in scope, else contradicted
        in scope (a measured null in the claim's exact scope and nothing for it), else contested (both). The others
        stay as they are (an association in an unstated context, a prediction: linked, never settled)."""
        graph = self.graph
        for cid in [c for ids in self.by_slot.values() for c in ids]:
            claim = graph.claims[cid]
            if claim.assessment != "unassessed":
                continue
            for assessment in ASSESSMENTS:
                try:
                    graph.assess(cid, assessment, ASSESSED[assessment], ROLE, claim.version)
                    break
                except GraphRefusal:
                    continue

    def decide(self) -> dict[str, Any]:
        """The run's result, from the chain view of what was filled. A chain with a predicted link is an answer:
        the summary says what kind of evidence each link holds."""
        ranked = chain_view(self.graph)["ranked"]
        leaders = ranked["leaders"]
        if not ranked["chains"]:
            outcome, text = "no_supported_explanation", ("No record on file can count for a claim of the chain: no "
                                                          "QBiC-SELEX group passes the gate and no database names a "
                                                          "gene or a trait for this variant.")
        else:
            # the leaders hold the same kinds of evidence, so a link is empty in all of them or in none
            cells = ranked["chains"][0]["cells"]
            empty = [key for key in LINK_KEYS if cells[key]["kind"] in (None, "none", "contested", "contradicted")]
            outcome = ("partial_mechanism" if empty else
                       "leading_explanation" if leaders == 1 else "multiple_explanations")
            text = " ".join(x for x in (ranked["headline"], ranked["support"]) if x)
        reading = self.reading
        if reading is None:
            how = "Filled by code alone from databases and model predictions: no article was read."
        elif not reading["found"]:
            how = ("Filled by code from databases and model predictions. " + (
                "A search found no article that names the variant, so none was read."
                if T._searched(reading) else
                "The search for articles that name the variant did not complete, so none was read."))
        else:
            how = (f"Filled by code from databases and model predictions, and from {reading['read']} of "
                   f"{reading['found']} article(s) found that name the variant, each read once by a model: "
                   f"{reading['accepted']} experiment(s) were filed as records.")
            if reading["stopped"]:
                how += f" Reading stopped early ({reading['stopped']}), so the literature column is incomplete."
        critique = self.critique
        if critique is not None and critique["records"] and not critique["asked"]:
            how += (f" The second reading had nothing to read: none of the {critique['records']} experiment(s) "
                    "code counts is the only record behind a cell.")
        elif critique is not None and critique["records"]:
            how += (f" A second model, from another provider, read {critique['reviewed']} of the "
                    f"{critique['asked']} experiment(s) that are the only record behind a cell (code counts "
                    f"{critique['records']} in all) against the claims they count for: of {critique['claims']} "
                    f"claim(s) checked it found {critique['not_shown']} not shown by the text, and those were not "
                    "counted.")
            if critique["stopped"]:
                how += f" The second reading stopped early ({critique['stopped']}), so the rest were not reviewed."
        if self.judgement is not None:
            how += " " + J.sentence(self.judgement)
        stop = ((reading or {}).get("stopped") or (critique or {}).get("stopped")
                or (self.judgement or {}).get("stopped") or "converged")
        self.graph.set_result(RunResult(outcome=outcome, stop_reason=stop, summary=f"{text} {how}"), ROLE)
        return {"chains": ranked["total"], "leaders": leaders}

    def run(self) -> dict[str, Any]:
        """Lookups, claims and links; then, with a reader, the articles and what their experiments bear on; then
        assessments and the result. Returns the fill's counts (also the manifest's)."""
        calls = self.lookups()
        self.groups, self._by_member = candidate_groups(self.graph), None
        with self.graph.batch():
            self.attach()
        if self.reader is not None:
            self.reading = self.reader.run(self.graph)
            self.attach_read()                             # outside a batch: each claim and link is its own step
            if self.critic is not None:
                self.critique = self.critic.summary()
                c = self.critique
                self.graph.log("audit", K.CRITIC,
                               f"the critic: {c['reviewed']} of {c['records']} experiment(s) read; of {c['claims']} "
                               f"claim(s) checked, {c['shown']} shown, {c['not_shown']} not shown, "
                               f"{c['cannot_tell']} could not be told",
                               details={"critic_summary": {k: v for k, v in c.items()
                                                           if k not in ("rows", "model_calls", "cost_usd")}})
        with self.graph.batch():
            self.assess()
        if self.judge is not None:
            self.judgement = self.judge.run(self.graph)    # after the assessments: the order of chains is final
        decided = self.decide()
        return {"driver": READER_DRIVER if self.reader is not None else DRIVER, "format": FILL_FORMAT,
                "expressed_tpm": EXPRESSED_TPM, "lookups": [c.tool_call_id for c in calls],
                "claims": {slot: len(ids) for slot, ids in self.by_slot.items()},
                "records_counted": self.links, "records_beside": self.beside, "records_set_aside": self.refused,
                **decided, **({"reading": self.reading} if self.reading is not None else {}),
                **({"critique": self.critique} if self.critique is not None else {}),
                **({"judgement": self.judgement} if self.judgement is not None else {})}


def run(graph: ClaimGraph, runner: ToolRunner | None = None, reader: Any = None,
        critic: Any = None, judge: Any = None) -> dict[str, Any]:
    """Fill the chain table of a graph that holds the evidence bundle (see the module docstring)."""
    return Fill(graph, runner, reader, critic, judge).run()


def manifest_parts(counts: Mapping[str, Any], reader: Mapping[str, Any] | None = None,
                   tool_limits: Mapping[str, Any] | None = None,
                   critic: Mapping[str, Any] | None = None,
                   judge: Mapping[str, Any] | None = None) -> dict[str, Any]:
    """What a fill run's manifest records as its engine: the driver and its settings. A fill by code alone names no
    prompt and no model; with a reader, `reader` holds its settings (reader.manifest_parts), with a critic `critic`
    holds the critic's (critic.manifest_parts), with a judge `judge` holds the judge's (judge.manifest_parts), and
    the run replays only if every reply it got is one the response cache can give back."""
    reading = counts.get("reading") or {}
    critique = counts.get("critique") or {}
    judgement = counts.get("judgement") or {}
    kept = {k: v for k, v in counts.items()
            if k not in ("driver", "format", "expressed_tpm", "reading", "critique", "judgement")}
    if reading:                                            # the counts; the per-article rows are in metrics.json
        kept["reading"] = {k: v for k, v in reading.items() if k not in ("articles", "cost_usd")}
    if critique:                                           # the counts; the per-record rows are in metrics.json
        kept["critique"] = {k: v for k, v in critique.items() if k not in ("rows", "cost_usd")}
    if judgement:                                          # the counts; the per-candidate rows are in metrics.json
        kept["judgement"] = {k: v for k, v in judgement.items() if k not in ("rows", "cost_usd")}
    parts: dict[str, Any] = {"driver": counts.get("driver", DRIVER), "fill_format": FILL_FORMAT,
                             "expressed_tpm": EXPRESSED_TPM,
                             "stop_reason": (reading.get("stopped") or critique.get("stopped")
                                             or judgement.get("stopped") or "converged"),
                             "replayable": True, "counts": kept}
    why: list[str] = []
    for name, settings in (("reader", reader), ("critic", critic), ("judge", judge)):
        if settings is not None:
            why += [f"{u['role']} {u['stage']}: {u['why']}" for u in settings.get("not_replayable") or []]
            parts[name] = {k: v for k, v in settings.items() if k != "not_replayable"}
    if reader is not None or critic is not None or judge is not None:
        parts["replayable"] = not why
        if why:
            parts["not_replayable"] = why
    if tool_limits is not None:
        parts["tool_limits"] = dict(tool_limits)
    return parts
