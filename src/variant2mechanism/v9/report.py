"""Render a v9 run folder as report.html (standalone, interactive) and report.md (compact text) (SPEC 9).

Why only the bundle: a saved run must be inspectable on any machine, offline, without keys, caches or adapters, and the
report must show what the graph records, nothing recomputed from elsewhere. Rendering reads the run folder through
bundle.load_bundle and calls no tool, model or network.

How the report stays faithful to the graph:
- one view model (report_data) feeds the HTML, its no-script tables and the Markdown, so all three name the same claim
  and evidence ids and the same statuses; current claim statuses are graph.display's;
- the version stepper shows past states rebuilt from the append-only record: claim history (assessments), the
  attach_evidence events (links, including ones a later link replaced), propagate events (dependency flags) and
  supersessions; a past status is graph.display_of applied to the claim as it stood then, so the stepper and the graph
  share one rule, and the last state of every claim equals graph.display;
- the mechanism graph is laid out by code in columns by entity kind (variant, TF or group, element, gene, process,
  phenotype, context), rows in entity-id order, so the layout is deterministic and the same at every version;
- statuses are shown by line style and a text badge as well as colour; a broken premise is a separate badge, never
  "contradicted", and a claim whose premise failed is never listed as retained; missing retrievals are listed as
  missing data, never as evidence;
- the case shows what was supplied apart from what the run found: inferred diseases and contexts are labelled
  inferred with their basis, and the rsID and elements code recorded for the variant are labelled as found by code;
- a bundle is called an evidence bundle only when no engine ran (no engine parts, no result, no model call); a run that
  stopped before proposing says so, with its stop reason and model-call count; the stop reason is shown with what the
  stop event says (an engine error names unusable model output or the internal failure);
- whether a run can be re-executed is the engine's own record (manifest engine.replayable, with its reasons when
  not), never a claim the report makes; a folder written by a replay names the run it re-executed and the outcome;
- a rejection whose contradiction was later withdrawn is shown as such: reinstated by code (ClaimGraph.reinstate, a
  "reinstatement" in the hypothesis's history, which the version stepper follows), or, when it still stands as a
  rejection, as one that no longer stands, with the engine's note; a question code closed as refused (a repeat of one
  already answered) is listed with its reason;
- evidence shows the variants it is about (about_variants), each read by the graph's own variant rule as the case
  variant or another one, since evidence about one variant never bears on a claim about another;
- the QBiC-SELEX inventory is one compact table in the adapter's neutral order (DBD label, then group id), never
  re-ordered by z, expression or ChIP; a CIS-BP-mapped model is labelled as provenance, never penalised; a group
  whose gate-passing models disagree about the allele shows both of its items, each with its allele;
- the mechanism chain (chain.chain_view) places every live claim about the case variant on the link it speaks to and
  names the strongest kind of evidence linked to it: a derived reading of the graph, shown beside the claims' own
  statuses, that changes no assessment, disposition or outcome and gives no score;
- the answer section shows the whole chains code assembles from those claims, in rank order (chain.py: ordered by
  their weakest link, on the kind of evidence only): the leading chain link by link, then every chain; a predicted
  link is labelled as predicted and ties are shown as ties, never broken by z, ChIP signal or expression;
- suggested experiments are marked suggested, never performed;
- under the chain table, the numbers each source returned for the leading chain's claims are copied by code from
  the saved records, never typed by a model, and are shown, never ranked on; and each claim of that chain that no
  measurement supports is given the kind of record that would fill it, written by code from the table's own rule
  for which record counts for which claim (suggested, not performed);
- a value a label table does not know (a stop reason, outcome or relation added to the schemas later) is shown as its
  words, so no saved run is ever unreadable.

Safety: retrieved and model-written text is data, never markup. The data are embedded as JSON in a
<script type="application/json"> block with <, > and & escaped as \\u003c, \\u003e and \\u0026; the template's script
builds every element with createElement and textContent and links only https URLs built here from source ids; the
no-script tables and the Markdown escape every string.
"""

import html
import json
import os
import re
from collections import Counter
from collections.abc import Callable, Iterable, Mapping
from pathlib import Path
from typing import Any
from urllib.parse import quote

from ..qbic.background import in_top_share
from . import adoption, chain
from . import table as chain_table
from .bundle import Bundle, inventory_call, inventory_items, inventory_table, load_bundle, safe_raw_path, write_new
from .graph import ClaimGraph, display_of
from .resolution import support_summary
from .schemas import (
    CLASS_ORDER,
    Claim,
    ContextScope,
    DecisionEvent,
    Evidence,
    EvidenceLink,
    Hypothesis,
    ToolCall,
    Variant,
)

REPORT_FORMAT = 1
TEMPLATE = Path(__file__).with_name("report_template.html")
PLACEHOLDER = re.compile(r"@@V2M_([A-Z]+)@@")
COLUMNS: tuple[tuple[str, tuple[str, ...]], ...] = (
    ("Variant", ("variant",)), ("TF or TF group", ("tf", "tf_group", "complex", "binding_event")),
    ("Element", ("element",)), ("Gene", ("gene", "transcript")), ("Process", ("process",)),
    ("Phenotype", ("phenotype",)), ("Context", ("context",)))
NODE_W, NODE_H, COL_GAP, ROW_GAP, PAD, HEAD, CHIP_H, PARALLEL, LANE = 196, 58, 200, 40, 24, 34, 36, 52, 7
STATUS_LABELS = {"supported": "Supported in scope", "predicted": "Predicted", "associated": "Associated",
                 "contested": "Contested", "contradicted": "Contradicted in scope", "unresolved": "Unresolved"}
OUTCOME_LABELS = {"leading_explanation": "Leading explanation", "partial_mechanism": "Partial mechanism",
                  "multiple_explanations": "Multiple explanations",
                  "no_supported_explanation": "No supported explanation",
                  "input_or_capability_limitation": "Input or capability limitation"}
STOP_LABELS = {"converged": "converged", "no_affordable_discriminating_action": "no affordable discriminating action",
               "coordinator_stop": "the coordinator stopped", "budget_model_calls": "model-call budget reached",
               "budget_tool_calls": "tool-call budget reached", "budget_currency": "currency budget reached",
               "wall_time": "wall-time limit reached", "regeneration_limit": "regeneration limit reached",
               "input_invalid": "the input was invalid", "unsupported_variant": "unsupported variant",
               "cache_miss": "a cache miss (a new call or a precompute would be needed)",
               "engine_error": "an engine error: unusable model output or an internal failure"}
MODE_LABELS = {"live": "Live run", "cache_only": "Cache-only run", "fixture": "Synthetic fixture run"}
DISPOSITION_LABELS = {"active": "Active", "deferred": "Deferred", "leading": "Leading", "tied": "Tied",
                      "rejected": "Rejected", "superseded": "Superseded"}
COMPARISON_LABELS = {"tied": "tied", "complementary": "complementary",
                     "insufficient_evidence": "insufficient evidence to choose"}
RELATION_LABELS = {"overlaps": "overlaps", "expressed_in": "is expressed in", "occupies": "occupies",
                   "alters_binding": "alters binding of", "alters_regulatory_activity": "alters regulatory activity of",
                   "regulates": "regulates", "associated_with_expression": "is associated with expression of",
                   "affects_process": "affects", "associated_with_trait": "is associated with",
                   "causal_at_locus": "is causal at the locus for", "contributes_to_trait": "contributes to",
                   "alters_rna": "alters RNA of", "other": "relates to"}
RELATION_SHORT = {"overlaps": "overlaps", "expressed_in": "expressed", "occupies": "occupies",
                  "alters_binding": "binding", "alters_regulatory_activity": "activity", "regulates": "regulates",
                  "associated_with_expression": "expression assoc.", "affects_process": "process",
                  "associated_with_trait": "trait assoc.", "causal_at_locus": "causal", "contributes_to_trait": "trait",
                  "alters_rna": "RNA", "other": "other"}
DIRECTION_MARKS = {"increases": " ↑", "decreases": " ↓", "creates": " creates", "abolishes": " abolishes",
                   "no_change": " no change", "unspecified": ""}
EVENT_GROUPS = {"tool_call": "tools", "attach_evidence": "evidence", "add_evidence": "evidence",
                "refuse_update": "refusals", "normalize": "log", "collect_facts": "log", "audit": "log",
                "stop": "log", "add_variant_alias": "log", "add_variant_element": "log", "reinstate": "decisions"}
VARIANT_FRAMES = {"case": "the case variant", "other": "another variant"}
REPLAY_STATUS = {"identical": "identical to the saved run", "different": "different from the saved run",
                 "miss": "incomplete: the saved run lacks a model reply or tool result the replay needed"}
RETRIEVAL_GAPS = {"no_records_found": "found no records", "error": "failed", "unavailable": "were unavailable",
                  "cache_miss": "were not in the cache", "not_applicable": "did not apply"}
OPEN_DISPOSITIONS = ("active", "leading", "tied")
SEVERITY = {"contradicted": 0, "contested": 2, "unresolved": 3, "predicted": 4, "associated": 4, "supported": 9}
RUNG_CLASSES = {"edit": "s-supported", "assay": "s-supported", "association": "s-associated",
                "prediction": "s-predicted", "none": "s-unresolved", "contradicted": "s-contradicted",
                "contested": "s-contested"}
NO_CHAIN = "No claim of this run is a link of the chain, so there is no chain to rank."
CHAIN_HEADERS = ["Link", "Strongest kind of evidence", "Leading candidates", "Other candidates"]
CHIP_W = 188
# (pattern over the whole source id, URL template, how the captured id is written in the URL)
SOURCE_PATTERNS: tuple[tuple[re.Pattern[str], str, Any], ...] = (
    (re.compile(r"(?i)pmid[:\s]\s*(\d{1,9})"), "https://pubmed.ncbi.nlm.nih.gov/{}/", str),
    (re.compile(r"(?i)(?:pmcid[:\s]\s*)?(pmc\d{1,9})"), "https://pmc.ncbi.nlm.nih.gov/articles/{}/", str.upper),
    (re.compile(r"(?i)(?:doi:\s*|https?://(?:dx\.)?doi\.org/)?(10\.\d{4,9}/\S+)"), "https://doi.org/{}", str),
    (re.compile(r"(?i)(?:encode:\s*)?(enc[a-z]{2}\d{3}[a-z]{3})"), "https://www.encodeproject.org/{}/", str.upper),
    (re.compile(r"(?i)(?:gwas(?: catalog)?:\s*)?(gcst\d{6,9})"), "https://www.ebi.ac.uk/gwas/studies/{}", str.upper),
    (re.compile(r"(?i)gtex[:\s]\s*(rs\d{1,12})"), "https://gtexportal.org/home/snp/{}", str.lower),
    (re.compile(r"(?i)gtex[:\s]\s*(ensg\d{11}(?:\.\d+)?)"), "https://gtexportal.org/home/gene/{}", str.upper),
)


# --- text helpers ----------------------------------------------------------------------------------------------------

def _text(value: Any) -> str:
    """One line of text; None is empty, but 0 and False are shown."""
    return "" if value is None else " ".join(str(value).split())


def _label(table: Mapping[str, str], value: str) -> str:
    """The display label of a schema value. A value the table does not know (one added to the schemas after this
    table) is shown as its words: a saved run must always render, whatever version of the schemas wrote it."""
    return table.get(value) or _text(value).replace("_", " ")


def _cut(text: str, n: int) -> str:
    return text if len(text) <= n else text[:n - 1].rstrip() + "…"


def _num(entity_id: str) -> int:
    return int(entity_id[1:]) if entity_id[1:].isdigit() else 0


def source_link(source_id: str) -> dict[str, str | None]:
    """A source id as {"text", "url"}. PubMed, PMC, DOI, ENCODE, GWAS Catalog and GTEx (rsID or Ensembl gene) ids get
    an https link built here from the id, never a URL taken from the data; anything else is text only."""
    text = _text(source_id)
    for pattern, url, case in SOURCE_PATTERNS:
        if m := pattern.fullmatch(text):
            return {"text": text, "url": url.format(quote(case(m.group(1)), safe="/:;()._-"))}
    return {"text": text, "url": None}


def _position(v: Variant) -> str:
    """chr2:60490908 T>G (a "chr" prefix only for human chromosome names; SYN:1 A>G stays as it is)."""
    chrom = f"chr{v.chrom}" if re.fullmatch(r"\d{1,2}|X|Y|MT?", v.chrom) else v.chrom
    return f"{chrom}:{v.pos} {v.ref}>{v.alt}"


def variant_label(v: Variant) -> str:
    label = f"{v.assembly} {_position(v)}"
    return f"{label} ({v.rsid})" if v.rsid else label


def _scope(scope: ContextScope | None) -> dict[str, Any] | None:
    """A context as stored plus one readable line: name (kind; tissue; species; condition; genotype)."""
    if scope is None:
        return None
    name = scope.biosample or (f"{scope.tissue} tissue" if scope.tissue else "") or scope.label or "unscoped"
    notes = [scope.biosample_kind.replace("_", " ") if scope.biosample_kind != "unknown" else "",
             scope.tissue if scope.biosample and scope.tissue else "",
             scope.species if scope.species != "human" else "", scope.condition or "",
             f"genotype {scope.genotype}" if scope.genotype else ""]
    notes = [n for n in notes if n]
    shown = f"{name} ({'; '.join(notes)})" if notes else name
    if scope.label and _text(scope.label).casefold() != name.casefold():
        shown += f", given as “{_text(scope.label)}”"
    return {**scope.model_dump(mode="json"), "text": shown}


# --- past states (version stepper) -----------------------------------------------------------------------------------

def _past_link(e: DecisionEvent, current: EvidenceLink | None) -> EvidenceLink:
    """The link an attach_evidence event made, as the claim held it then: the claim's own link object while it is
    current, else rebuilt from the event (graph.link records every field of the link in its event's details)."""
    if current is not None:
        return current
    d = e.details
    stance = d.get("stance", "context_only")
    return EvidenceLink(claim_id=e.target_ids[0], evidence_id=e.evidence_ids[0], stance=stance,
                        applicability=d.get("applicability", "unknown"), rationale=e.concise_reason,
                        proposed_by=e.role, event_id=e.event_id,
                        code_applicability=d.get("code_applicability") or d.get("applicability", "unknown"),
                        corrected=bool(d.get("corrected")), strength=d.get("strength", "context"),
                        downgraded_from=d.get("downgraded_from"), revises=d.get("revises"))


class _Record:
    """Indexes over the append-only events that past states are rebuilt from."""

    def __init__(self, graph: ClaimGraph):
        self.version = {e.event_id: e.graph_version_after for e in graph.events}
        self.links: dict[str, list[tuple[int, EvidenceLink]]] = {}
        self.flags: dict[str, list[tuple[int, str]]] = {}
        self.superseded: dict[str, tuple[int, str]] = {}
        # every rejection of a hypothesis, in order (a reinstated hypothesis can be rejected again, finally), and the
        # engine's notes that a rejection no longer stood (audit events with details.stale_rejection)
        self.rejections: dict[str, list[dict[str, Any]]] = {}
        self.stale_notes: dict[str, list[tuple[str, str]]] = {}     # hid -> [(audit event id, why it stays rejected)]
        current = {x.event_id: x for c in graph.claims.values() for x in c.evidence_links}
        for e in graph.events:
            v, d = e.graph_version_after, e.details
            if e.action == "attach_evidence" and e.target_ids and e.evidence_ids:
                self.links.setdefault(e.target_ids[0], []).append((v, _past_link(e, current.get(e.event_id))))
            elif e.action == "propagate":
                for cid in d.get("flagged") or {}:
                    self.flags.setdefault(cid, []).append((v, "unsupported_due_to_dependency"))
                for cid in d.get("cleared") or []:
                    self.flags.setdefault(cid, []).append((v, "none"))
            elif e.action == "supersede_claim" and len(e.target_ids) >= 2:
                self.superseded.setdefault(e.target_ids[0], (v, e.target_ids[1]))
            elif e.action == "reject" and e.target_ids:
                claims = d.get("claims") if isinstance(d.get("claims"), list) else []
                self.rejections.setdefault(e.target_ids[0], []).append(
                    {"event": e.event_id, "v": v, "role": e.role, "evidence": list(e.evidence_ids),
                     "claims": [str(c) for c in claims], "reason": e.concise_reason})
            elif e.action == "audit" and isinstance(d.get("stale_rejection"), str):
                self.stale_notes.setdefault(d["stale_rejection"], []).append((e.event_id, _text(d.get("why"))))

    def link_history(self, claim_id: str) -> list[dict[str, Any]]:
        """Every link the claim has had, in order, with the graph version it was made at (the page shows the links
        current at a version: the last per evidence item)."""
        return [{"v": v, "event": x.event_id, "evidence": x.evidence_id, "role": x.proposed_by, "stance": x.stance,
                 "applicability": x.applicability, "code_applicability": x.code_applicability,
                 "corrected": x.corrected, "strength": x.strength, "downgraded_from": x.downgraded_from,
                 "revises": x.revises, "rationale": x.rationale, "limitations": list(x.limitations)}
                for v, x in self.links.get(claim_id, [])]

    def claim_states(self, graph: ClaimGraph, claim: Claim) -> list[dict[str, Any]]:
        """The claim's state at each graph version where it changed: status, basis, assessment, dependency flag and
        supersession. The first entry is its creation. The status is graph.display_of on the claim as it stood then
        (its assessment and the links current at that version), the rule the graph itself displays with."""
        assessments = [(self.version.get(h.event_id, 0), h.assessment) for h in claim.history]
        created = assessments[0][0] if assessments else 0
        links = self.links.get(claim.claim_id, [])
        flags = self.flags.get(claim.claim_id, [])
        superseded = self.superseded.get(claim.claim_id)
        points = sorted({created, *(v for v, _ in assessments), *(v for v, _ in links), *(v for v, _ in flags),
                         *([superseded[0]] if superseded else [])})
        states: list[dict[str, Any]] = []
        for v in (p for p in points if p >= created):
            active = {x.evidence_id: x for lv, x in links if lv <= v}
            flag = ([f for fv, f in flags if fv <= v] or ["none"])[-1]
            then = claim.model_copy(update={"assessment": [a for av, a in assessments if av <= v][-1],
                                            "evidence_links": list(active.values()), "dependency_flag": flag})
            shown = display_of(then, graph.evidence)
            state = {"status": shown.status, "basis": shown.basis, "assessment": then.assessment, "flag": flag,
                     "superseded_by": superseded[1] if superseded and superseded[0] <= v else None}
            if not states or any(states[-1][k] != state[k] for k in state):
                states.append({"v": v, **state})
        return states


# --- the view model --------------------------------------------------------------------------------------------------

def _variant_names(graph: ClaimGraph, names: list[str]) -> list[dict[str, str | None]]:
    """The variants an item names (Evidence.about_variants), each with what the graph's own variant rule
    (ClaimGraph.variant_mention) reads it as: the case variant, another variant, or None (no rsID or position)."""
    return [{"text": name, "frame": graph.variant_mention(name)} for name in names]


def _evidence_view(graph: ClaimGraph, ev: Evidence, linked: Mapping[str, list[str]], group_sizes: Counter,
                   inventory_ids: set[str]) -> dict[str, Any]:
    call = graph.tool_calls.get(ev.retrieval_ref) if ev.retrieval_ref else None
    return {"id": ev.evidence_id, "class": ev.evidence_class, "observed": ev.observed_result,
            "sources": [source_link(s) for s in ev.source_ids],
            "raw": safe_raw_path(ev.raw_artifact_ref) or (safe_raw_path(call.raw_result_path) if call else None),
            "tool_call": ev.retrieval_ref, "tool": call.tool_name if call else None, "data": ev.data,
            "allele": ev.allele, "direction": ev.direction, "context": _scope(ev.context),
            "about": {"variants": ev.about_variants, "tfs": ev.about_tfs, "genes": ev.about_genes,
                      "elements": ev.about_elements, "traits": ev.about_traits},
            "variants": _variant_names(graph, ev.about_variants),
            "group": ev.independence_group, "group_size": group_sizes[ev.independence_group], "origin": ev.origin,
            "access": ev.access, "result_kind": ev.result_kind, "assessed_relation": ev.assessed_relation,
            "experiment": ev.experiment.model_dump(mode="json") if ev.experiment else None,
            "limitations": ev.limitations, "claims": linked.get(ev.evidence_id, []),
            "inventory": ev.evidence_id in inventory_ids}


def _claim_view(graph: ClaimGraph, claim: Claim, record: _Record) -> dict[str, Any]:
    shown = graph.display(claim.claim_id)
    mark = DIRECTION_MARKS.get(claim.direction, f" {_label({}, claim.direction)}")
    return {"id": claim.claim_id, "version": claim.version, "relation": claim.relation,
            "relation_label": _label(RELATION_LABELS, claim.relation), "direction": claim.direction,
            "effect_allele": claim.effect_allele, "allele_scope": claim.allele_scope,
            "context": _scope(claim.context_scope), "mechanism_class": claim.mechanism_class,
            "assertion": claim.assertion_text, "assessment": claim.assessment,
            "rationale": claim.assessment_rationale, "status": shown.status,
            "status_label": _label(STATUS_LABELS, shown.status),
            "basis": shown.basis, "basis_classes": list(shown.basis_classes), "flag": claim.dependency_flag,
            "dependencies": claim.dependencies, "supersedes": claim.supersedes, "superseded_by": claim.superseded_by,
            "limitations": claim.limitations, "proposed_by": claim.proposed_by, "subjects": claim.subject_ids,
            "objects": claim.object_ids,
            "chip": f"{claim.claim_id} · {_label(RELATION_SHORT, claim.relation)}{mark}",
            "hypotheses": [{"id": h.hypothesis_id, "required": claim.claim_id in h.required_claim_ids,
                            "disposition": h.disposition} for h in graph.hypotheses.values()
                           if claim.claim_id in h.claim_ids],
            "states": record.claim_states(graph, claim), "links": record.link_history(claim.claim_id)}


def _weakest(h: Hypothesis, claims: Mapping[str, dict[str, Any]], result_links: list[dict[str, str]]
             ) -> dict[str, str] | None:
    """The run result's weakest link for this hypothesis, else its least-supported required claim (a broken premise
    counts as the weakest after a contradiction). None when every required claim is supported."""
    if named := next((w for w in result_links if w["hypothesis_id"] == h.hypothesis_id), None):
        return {"claim": named["claim_id"], "why": named["why"]}

    def rank(cid: str) -> tuple[int, int]:
        c = claims[cid]
        return (1 if c["flag"] != "none" and c["status"] != "contradicted" else SEVERITY[c["status"]], _num(cid))

    worst = min(h.required_claim_ids, key=rank, default=None)
    if worst is None or (claims[worst]["status"] == "supported" and claims[worst]["flag"] == "none"):
        return None
    c = claims[worst]
    why = c["status_label"].lower() + (f" ({c['basis']} only)" if c["status"] in ("predicted", "associated") else "")
    if c["flag"] != "none":
        why += "; a premise it depends on failed"
    return {"claim": worst, "why": why}


def _best(h: Hypothesis, claims: Mapping[str, dict[str, Any]]) -> dict[str, str] | None:
    """The hypothesis's best-supported live claim: a supported one, most experimental basis first (CLASS_ORDER), then
    a predicted or associated one. A display aid naming a claim, not a score."""
    def rank(cid: str) -> tuple[int, int, int, int]:
        c = claims[cid]
        basis = CLASS_ORDER.index(c["basis"]) if c["basis"] in CLASS_ORDER else len(CLASS_ORDER)
        return (0 if c["status"] == "supported" else 1, basis, 0 if cid in h.required_claim_ids else 1, _num(cid))

    live = [cid for cid in h.claim_ids if claims[cid]["status"] in ("supported", "predicted", "associated")
            and not claims[cid]["superseded_by"]]
    if not live:
        return None
    best = min(live, key=rank)
    c = claims[best]
    return {"claim": best, "why": c["status_label"].lower() + (f" ({c['basis']})" if c["basis"] else "")}


def _stale_rejection(graph: ClaimGraph, h: Hypothesis, record: _Record,
                     reinstated: list[dict[str, Any]]) -> dict[str, Any] | None:
    """For a hypothesis that is still rejected although none of its required claims is contradicted in scope now (a
    reassessment or a replaced link withdrew the contradiction; the rule of compare.stale_rejections): the claims, the
    engine's notes (audit events with details.stale_rejection), and why it stays rejected: the engine's recorded
    reason (details.why) when a note gives one, else what the graph shows (a reinstatement already made, so this
    later rejection is final; an open hypothesis with the same structure). None otherwise."""
    if h.disposition != "rejected" or any(graph.claims[c].assessment == "contradicted_in_scope"
                                          for c in h.required_claim_ids):
        return None
    rejections = record.rejections.get(h.hypothesis_id, [])
    notes = record.stale_notes.get(h.hypothesis_id, [])
    why = [w for _, w in notes if w][-1:]
    if not why and reinstated:
        why.append(f"it was reinstated once already ({reinstated[-1]['event']}), so this later rejection is final")
    twins = [o.hypothesis_id for o in graph.hypotheses.values() if o.hypothesis_id != h.hypothesis_id
             and graph.hypothesis_signature(o) == graph.hypothesis_signature(h)
             and o.disposition not in ("rejected", "superseded")]
    if not why and twins:
        why.append(f"{', '.join(twins)} is open with the same structure")
    return {"claims": list(h.required_claim_ids), "rested_on": rejections[-1]["claims"] if rejections else [],
            "rejected_by": rejections[-1]["event"] if rejections else None,
            "noted_by": [event for event, _ in notes], "why_still_rejected": why}


def _reinstated_text(h: Hypothesis, x: Mapping[str, Any]) -> str:
    """One reinstatement as a sentence: which rejection it undid and on which claims (its recorded reason is the
    hypothesis's disposition reason, shown with the disposition, and the reinstate event's text in the timeline)."""
    claims = ", ".join(x["claims"]) or "its required claims"
    return (f"{h.hypothesis_id} was reinstated as deferred by {x['event']}: the contradiction of {claims} that "
            f"rejected it ({x['rejected_by'] or 'rejection not recorded'}) was withdrawn.")


def _stale_text(hid: str, stale: Mapping[str, Any]) -> str:
    """A rejection that no longer stands, as a sentence: the claims no longer contradicted, the rejection, the
    engine's note, and why it stays rejected when the record says."""
    parts = [f"The rejection of {hid} no longer stands: none of its required claims ({', '.join(stale['claims'])}) "
             "is contradicted in scope now"]
    if stale["rejected_by"]:
        rested = f" on {', '.join(stale['rested_on'])}" if stale["rested_on"] else ""
        parts.append(f"it was rejected by {stale['rejected_by']}{rested}")
    if stale["noted_by"]:
        parts.append(f"the engine noted this in {', '.join(stale['noted_by'])}")
    return "; ".join([*parts, *stale["why_still_rejected"]]) + "."


def _hypothesis_view(graph: ClaimGraph, h: Hypothesis, claims: Mapping[str, dict[str, Any]], record: _Record,
                     result_links: list[dict[str, str]]) -> dict[str, Any]:
    decisive = sorted({cid for p in graph.comparisons.values() if p.accepted and h.hypothesis_id in (p.a, p.b)
                       for cid in p.decisive_claim_ids}, key=_num)
    # The disposition at each version: its creation, every change, and a reinstatement (code moving a rejection whose
    # contradiction was withdrawn back to deferred: ClaimGraph.reinstate, the one way out of "rejected").
    states = [{"v": record.version.get(x.get("event_id", ""), 0), "disposition": x.get("to") or x.get("disposition")}
              for x in h.history if x.get("kind") in ("created", "disposition", "reinstatement")]
    reinstated = [{"event": x.get("event_id"), "v": record.version.get(x.get("event_id", ""), 0),
                   "rejected_by": x.get("rejected_by"), "claims": [str(c) for c in x.get("claims") or []],
                   "reason": _text(x.get("reason"))} for x in h.history if x.get("kind") == "reinstatement"]
    rejections = record.rejections.get(h.hypothesis_id, [])
    stale = _stale_rejection(graph, h, record, reinstated)
    # The archive's retained subclaims are the claims that still stand on their own: not contradicted, not superseded
    # and resting on no failed premise. A claim whose premise failed is listed apart, never as retained (SPEC 13.8).
    standing = [cid for cid in h.claim_ids if claims[cid]["status"] != "contradicted" and not claims[cid]["superseded_by"]]
    return {"id": h.hypothesis_id, "version": h.version, "title": h.title, "summary": h.summary,
            "disposition": h.disposition, "disposition_label": _label(DISPOSITION_LABELS, h.disposition),
            "reason": h.disposition_reason, "revisit_trigger": h.revisit_trigger, "origin": h.origin,
            "replaces": h.replaces,
            "replaced_by": [o.hypothesis_id for o in graph.hypotheses.values() if o.replaces == h.hypothesis_id],
            "endpoint": h.endpoint, "mechanism_class": h.mechanism_class, "context": _scope(h.context),
            "claims": h.claim_ids, "required": h.required_claim_ids, "path_status": h.path_status,
            "assumptions": h.assumptions, "member_alternatives": h.member_alternatives,
            "missing_links": h.missing_links, "reason_for_inclusion": h.reason_for_inclusion,
            "best": _best(h, claims), "weakest": _weakest(h, claims, result_links), "decisive": decisive,
            "states": states, "reject_evidence": rejections[-1]["evidence"] if rejections else [],
            "rejections": rejections, "reinstated": reinstated, "stale_rejection": stale,
            "reinstated_notes": [_reinstated_text(h, x) for x in reinstated],
            "stale_note": _stale_text(h.hypothesis_id, stale) if stale else None,
            "retained": [cid for cid in standing if claims[cid]["flag"] == "none"],
            "premise_failed": [cid for cid in standing if claims[cid]["flag"] != "none"],
            "shared": {cid: [o.hypothesis_id for o in graph.hypotheses.values()
                             if o.hypothesis_id != h.hypothesis_id and cid in o.claim_ids
                             and o.disposition not in ("rejected", "superseded")] for cid in h.claim_ids}}


def _inventory_view(graph: ClaimGraph, linked: Mapping[str, list[str]]) -> dict[str, Any]:
    """The inventory rows as recorded (neutral order kept), with the allele each group's best model favours, every
    Evidence item of the group (one, or one per allele when its gate-passing models disagree: each with its allele and
    the TFs its models map to) and the claims that link any of them (a row counts as linked when either item is)."""
    v = graph.case.variant
    items = inventory_items(graph)
    rows = []
    for r in inventory_table(graph):
        more = r.get("binds_more")
        group = items.get(str(r.get("group_id"))) or []
        rows.append({"group": r.get("group_id"), "label": r.get("group_label"), "dbd": r.get("dbd"),
                     "members": [{"tf": m.get("tf"), "mapping": m.get("mapping")} for m in r.get("members") or []
                                 if isinstance(m, dict)],
                     "stem": r.get("paralog_stem"), "best_model": r.get("best_model"), "binds_more": more,
                     "allele": v.alt if more == "alt" else v.ref if more == "ref" else None,
                     "z": r.get("z"), "effect": r.get("effect"), "p": r.get("p"), "n_pass": r.get("n_pass"),
                     "n_models": r.get("n_models"), "passes": r.get("passes_gate") is True,
                     "evidence": r.get("evidence_id"), "discordant": len(group) > 1,
                     "items": [{"id": e, "allele": graph.evidence[e].allele, "tfs": graph.evidence[e].about_tfs}
                               for e in group],
                     "claims": list(dict.fromkeys(c for e in group for c in linked.get(e, [])))})
    call = inventory_call(graph)
    return {"call": call.tool_call_id if call else None, "rows": rows, "groups": len(rows),
            "gate_passing": sum(r["passes"] for r in rows),
            "linked": sum(bool(r["claims"]) for r in rows)}


def _gaps(graph: ClaimGraph, claims: Mapping[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """What the run leaves open: the result's weakest links (else the unsupported required claims of open
    hypotheses), uninvestigated questions and lookups that returned nothing (missing data, not evidence)."""
    gaps: list[dict[str, Any]] = []
    result = graph.result
    if result and result.weakest_links:
        gaps += [{"kind": "weakest_link", "text": f"{w.hypothesis_id} · {w.claim_id}: {w.why}",
                  "ids": [w.hypothesis_id, w.claim_id]} for w in result.weakest_links]
    else:
        for h in graph.hypotheses.values():
            if h.disposition in OPEN_DISPOSITIONS:
                gaps += [{"kind": "unresolved_required", "ids": [h.hypothesis_id, cid],
                          "text": f"{h.hypothesis_id} needs {cid} ({claims[cid]['status_label'].lower()})"}
                         for cid in h.required_claim_ids if claims[cid]["status"] != "supported"]
    if result:
        gaps += [{"kind": "question", "text": q, "ids": []} for q in result.uninvestigated_questions]
    missing = Counter(t.retrieval_status if t.execution_status == "success" else t.execution_status
                      for t in graph.tool_calls.values() if t.charged_to != "none"
                      and (t.execution_status != "success" or t.retrieval_status == "no_records_found"))
    if missing:
        what = "; ".join(f"{n} {_label(RETRIEVAL_GAPS, k)}" for k, n in sorted(missing.items()))
        gaps.append({"kind": "retrieval", "ids": [],
                     "text": f"Lookups without an answer: {what}. Missing data, not evidence either way."})
    gaps += [{"kind": "unadopted_observation", "ids": ids,
              "text": f"{', '.join(ids)}: accepted observation not represented by a non-context claim link in "
                      "a hypothesis and not explicitly deferred or set aside."} for ids in adoption.pending(graph)]
    return gaps


def _tool_call_view(t: ToolCall) -> dict[str, Any]:
    return {"id": t.tool_call_id, "tool": t.tool_name, "requested_by": t.requested_by, "question": t.question_id,
            "purpose": t.purpose, "status": t.execution_status, "retrieval": t.retrieval_status,
            "charged_to": t.charged_to, "cached": t.cached, "provider": t.provider, "release": t.dataset_release,
            "message": t.message, "raw": safe_raw_path(t.raw_result_path), "evidence": len(t.evidence_ids),
            "time": t.retrieval_time, "params": t.query_parameters}


def _count(n: int, noun: str) -> str:
    return f"{n} {noun}" + ("" if n == 1 else "s")


def _model_calls(bundle: Bundle) -> int:
    """The model calls the run made: metrics.json's count (normalised by bundle.write_bundle), else the graph's own
    record, which the engine keeps current."""
    calls = (bundle.metrics.get("model") or {}).get("calls")
    return calls if isinstance(calls, int) and not isinstance(calls, bool) else bundle.graph.model_usage.calls


def _no_hypotheses(g: ClaimGraph, evidence_only: bool, model_calls: int, tool_calls: int) -> str | None:
    """Why the run holds no hypothesis, in one sentence; None when it holds some. An evidence bundle never ran the
    engine; any other run stopped before proposing, and its stop reason and model calls say how far it got."""
    if g.hypotheses:
        return None
    if evidence_only:
        return (f"Facts collected by code ({_count(tool_calls, 'tool call')}); no model was called and no hypotheses "
                "or claims were proposed.")
    calls = _count(model_calls, "model call") if model_calls else "no model call"
    if g.claims and all(c.proposed_by == "code" for c in g.claims.values()):
        how = ("no model was called" if not model_calls else
               f"a model was called only to read articles ({_count(model_calls, 'model call')})")
        return (f"Code stated every claim a record on file can count for and linked the records "
                f"({_count(tool_calls, 'tool call')}); {how}, so no hypothesis was proposed.")
    if g.result is not None:
        return (f"The run stopped before any hypothesis was proposed ({_label(STOP_LABELS, g.result.stop_reason)}; "
                f"{calls}).")
    return f"No hypothesis was proposed and the run recorded no outcome ({calls})."


def _replay_view(manifest: Mapping[str, Any]) -> dict[str, Any]:
    """Whether the run can be re-executed, as the engine recorded it in the manifest (engine.replayable, with the
    reasons when it cannot: a retried, refused or failed model call, a wall-time or currency stop), and, for a folder
    `v2m v9 replay` wrote, the run it re-executed and how that came out. None where nothing was recorded (an evidence
    bundle or an older run)."""
    engine = manifest.get("engine") if isinstance(manifest.get("engine"), Mapping) else {}
    recorded, reasons = engine.get("replayable"), engine.get("not_replayable")
    of = manifest.get("replay_of") if isinstance(manifest.get("replay_of"), Mapping) else None
    status = _text(of.get("status")) if of else ""
    return {"replayable": recorded if isinstance(recorded, bool) else None,
            "reasons": [_text(r) for r in reasons] if isinstance(reasons, list) else [],
            "of": None if of is None else {"run": Path(_text(of.get("run_folder"))).name or None, "status": status,
                                           "status_label": _label(REPLAY_STATUS, status),
                                           "differences": of.get("differences")}}


def _meta(bundle: Bundle, render_only: bool) -> dict[str, Any]:
    g, m = bundle.graph, bundle.manifest
    mode = m.get("mode")
    synthetic = g.case.synthetic or mode == "fixture" or any(
        e.origin == "fixture" or e.evidence_class == "synthetic" for e in g.evidence.values())
    label = variant_label(g.case.variant)
    model_calls = _model_calls(bundle)
    tool_calls = sum(t.charged_to != "none" for t in g.tool_calls.values())
    # What `v2m v9 evidence` writes: code's fact collection alone. No engine ran (no engine parts in the manifest, no
    # result) and no model was called; a run that stopped before proposing is never called an evidence bundle.
    evidence_only = not (m.get("engine") or g.result or g.claims or g.hypotheses or model_calls)
    return {"title": f"{label} · v2m run report", "case_id": g.case.case_id, "variant": label, "mode": mode,
            "mode_label": MODE_LABELS.get(mode or "", "Mode not recorded"), "render_only": render_only,
            "synthetic": synthetic, "evidence_only": evidence_only, "model_calls": model_calls,
            "tool_calls": tool_calls, "hypotheses_note": _no_hypotheses(g, evidence_only, model_calls, tool_calls),
            "public_export": m.get("public_export"), "engine_version": g.engine_version, "created": m.get("created"),
            "profile": m.get("profile"), "manifest_missing": not m, "evaluation_present": bundle.evaluation is not None,
            "code_only": isinstance(m.get("engine"), Mapping) and m["engine"].get("driver") == "code_only_fill",
            "with_reader": isinstance(m.get("engine"), Mapping) and m["engine"].get("driver") == "fill_with_reader",
            "integrity": list(bundle.integrity), "replay": _replay_view(m)}


def _stop_event(g: ClaimGraph) -> tuple[str | None, str]:
    """The stop event that recorded the run's stop reason (the last one) and what it says beyond the reason itself
    ("no usable proposal from the coordinator in 2 attempts", "internal error (KeyError)..."), or (None, "")."""
    reason = g.result.stop_reason if g.result else None
    event = next((e for e in reversed(g.events) if e.action == "stop" and reason
                  and e.details.get("stop_reason") == reason), None)
    if event is None:
        return None, ""
    text = event.concise_reason
    return event.event_id, _text(text[len(reason) + 2:] if text.startswith(f"{reason}: ") else
                                 "" if text == reason else text)


def report_data(bundle: Bundle, *, render_only: bool = False, raw_base: str = "") -> dict[str, Any]:
    """The view model both formats render: JSON-native and deterministic for a given bundle. `render_only` marks a
    report rendered later from a saved run; `raw_base` is the path from the report's folder to the run folder, for
    links to raw results."""
    g = bundle.graph
    record = _Record(g)
    linked: dict[str, list[str]] = {}
    for c in g.claims.values():
        for x in c.evidence_links:
            linked.setdefault(x.evidence_id, []).append(c.claim_id)
    inventory = _inventory_view(g, linked)
    inventory_ids = {x["id"] for r in inventory["rows"] for x in r["items"]}     # both items of a discordant group
    group_sizes = Counter(e.independence_group for e in g.evidence.values())
    claims = {cid: _claim_view(g, c, record) for cid, c in g.claims.items()}
    result = g.result
    result_links = [w.model_dump(mode="json") for w in result.weakest_links] if result else []
    v = g.case.variant
    stop_event, stop_detail = _stop_event(g)

    def found_by(tool_call_id: str) -> str | None:
        call = g.tool_calls.get(tool_call_id)
        return call.tool_name if call else None

    return {
        "format": REPORT_FORMAT,
        "scope_graph": g.scope_views(),
        "meta": _meta(bundle, render_only),
        "case": {"case_id": g.case.case_id, "variant": {**v.model_dump(mode="json"), "label": variant_label(v)},
                 "origin": g.case.origin, "supplied_disease": g.case.supplied_disease,
                 "supplied_context": [_scope(s) for s in g.case.supplied_context],
                 "inferred": [c.model_dump(mode="json") for c in g.case.inferred_candidates],
                 "aliases": [{"rsid": rsid, "tool_call": tid, "tool": found_by(tid)}
                             for rsid, tid in g.variant_aliases.items()],
                 "elements": [{"element": element, "tool_call": tid, "tool": found_by(tid)}
                              for element, tid in g.variant_elements.items()],
                 "provenance": g.case.input_provenance},
        "result": None if result is None else {
            "resolution": support_summary(g),
            **result.model_dump(mode="json"), "outcome_label": _label(OUTCOME_LABELS, result.outcome),
            "stop_label": _label(STOP_LABELS, result.stop_reason), "stop_event": stop_event,
            "stop_detail": stop_detail,
            "downgraded_label": _label(OUTCOME_LABELS, result.downgraded_from) if result.downgraded_from else None},
        "gaps": _gaps(g, claims),
        "chain": chain.for_report(chain.chain_view(g)),
        "table": {**chain_table.report_view(g), **table_extras(g)},
        "entities": {eid: {"id": eid, "kind": e.kind, "label": e.label, "canonical_id": e.canonical_id,
                           "members": [g.entities[p].label for p in e.participants]} for eid, e in g.entities.items()},
        "claims": claims,
        "evidence": {eid: _evidence_view(g, e, linked, group_sizes, inventory_ids) for eid, e in g.evidence.items()},
        "hypotheses": [_hypothesis_view(g, h, claims, record, result_links) for h in g.hypotheses.values()],
        "comparisons": [{"id": p.comparison_id, "a": p.a, "b": p.b, "outcome": p.outcome,
                         "outcome_label": (f"{p.a} preferred" if p.outcome == "A_preferred" else f"{p.b} preferred"
                                           if p.outcome == "B_preferred" else _label(COMPARISON_LABELS, p.outcome)),
                         "decisive": p.decisive_claim_ids, "gaps": p.decisive_gaps, "reason": p.reason,
                         "accepted": p.accepted, "refusal_reason": p.refusal_reason}
                        for p in g.comparisons.values()],
        "questions": [{"id": q.question_id, "text": q.text, "route": q.route, "status": q.status, "round": q.round,
                       "targets": q.target_claim_ids, "hypotheses": q.hypothesis_ids,
                       "rubric": q.rubric.model_dump(mode="json"), "outcomes": q.possible_outcomes,
                       "actions": [a.model_dump(mode="json") for a in q.actions], "answer": q.answer_summary,
                       "gap": q.remaining_gap} for q in g.questions.values()],
        "events": [{"id": e.event_id, "v": e.graph_version_after, "before": e.graph_version_before, "role": e.role,
                    "action": e.action, "group": EVENT_GROUPS.get(e.action, "decisions"), "targets": e.target_ids,
                    "evidence": e.evidence_ids, "reason": e.concise_reason, "supersedes": e.supersedes}
                   for e in g.events],
        "final_version": g.version,
        "layout": layout(g),
        "inventory": inventory,
        "tool_calls": [_tool_call_view(t) for t in g.tool_calls.values()],
        "provenance": {"manifest": {k: bundle.manifest[k] for k in ("format", "engine_version", "created", "mode",
                                                                    "profile", "code", "config", "engine",
                                                                    "dataset_releases", "cache_policy", "files",
                                                                    "public_export", "replay_of")
                                    if k in bundle.manifest},
                       "metrics": bundle.metrics},
        "raw_base": raw_base,
    }


# --- layout ----------------------------------------------------------------------------------------------------------

def _point(p: list[tuple[float, float]], t: float) -> tuple[float, float]:
    """A point of the cubic Bézier curve with control points p at parameter t."""
    a, b, c, d = (1 - t) ** 3, 3 * (1 - t) ** 2 * t, 3 * (1 - t) * t ** 2, t ** 3
    return (a * p[0][0] + b * p[1][0] + c * p[2][0] + d * p[3][0],
            a * p[0][1] + b * p[1][1] + c * p[2][1] + d * p[3][1])


def _curve(p: list[tuple[float, float]], move: bool = True) -> str:
    """SVG path data for one cubic curve (with its starting move, or continuing a path)."""
    start = f"M{p[0][0]:.1f} {p[0][1]:.1f} " if move else ""
    return start + "C" + ", ".join(f"{x:.1f} {y:.1f}" for x, y in p[1:])


def _route(s: dict[str, Any], o: dict[str, Any], index: int,
           lane: float) -> tuple[str, list[tuple[float, float]], tuple[float, float]]:
    """One edge from node s to node o: SVG path data, the points that bound it, and where the claim's chip sits.
    No edge passes behind a node, so a line can only be read as ending where it ends:
    - to the next column (either way): one curve across the gap between them, fanned out when several claims join
      the same two nodes;
    - two or more columns away: down into the channel below the lower of the two rows (no node lies there, since all
      columns share one row grid), along it, and into the object's facing side; `lane` separates edges sharing it;
    - within one column: a loop into the empty gap on its right; to itself: a loop above the box.
    The chip sits in a gap beside the object, where no node is."""
    sy, oy = s["y"] + NODE_H / 2, o["y"] + NODE_H / 2
    if s["id"] == o["id"]:
        lift = 52 + 14 * index
        p = [(s["x"] + NODE_W * .3, s["y"]), (s["x"] + NODE_W * .1, s["y"] - lift),
             (s["x"] + NODE_W * .9, s["y"] - lift), (s["x"] + NODE_W * .7, s["y"])]
        return _curve(p), p, _point(p, .5)
    if o["col"] == s["col"]:
        bulge = 70 + 18 * index
        x = s["x"] + NODE_W
        p = [(x, sy), (x + bulge, sy), (x + bulge, oy), (x, oy)]
        return _curve(p), p, _point(p, .5)
    off = ((index + 1) // 2) * PARALLEL * (1 if index % 2 else -1)
    if o["col"] == s["col"] + 1:
        x0, x3 = s["x"] + NODE_W, o["x"]
        dx = (x3 - x0) * .45
        p = [(x0, sy), (x0 + dx, sy + off), (x3 - dx, oy + off), (x3, oy)]
        return _curve(p), p, _point(p, .5)
    channel = max(s["y"], o["y"]) + NODE_H + ROW_GAP / 2 + lane
    if o["col"] == s["col"] - 1:
        x0, x3 = s["x"], o["x"] + NODE_W
        dx = (x0 - x3) * .4
        p = [(x0, sy), (x0 - dx, channel), (x3 + dx, channel), (x3, oy)]
        return _curve(p), p, _point(p, .5)
    half, way = COL_GAP / 2, 1 if o["col"] > s["col"] else -1
    a = (s["x"] + NODE_W if way > 0 else s["x"], sy)
    d = (o["x"] if way > 0 else o["x"] + NODE_W, oy)
    b, c = (a[0] + way * COL_GAP, channel), (d[0] - way * COL_GAP, channel)
    first = [a, (a[0] + way * half, sy), (a[0] + way * half, channel), b]
    last = [c, (d[0] - way * half, channel), (d[0] - way * half, oy), d]
    return f"{_curve(first)} L{c[0]:.1f} {c[1]:.1f} {_curve(last, move=False)}", first + last, _point(last, .5)


def _free_row(cx: float, cy: float, placed: list[tuple[float, float]]) -> float:
    """The chip centre's y, moved down past every chip already placed that it would overlap, so that chips of
    parallel edges, or of edges meeting the same column, never cover each other (placement follows claim order)."""
    step = CHIP_H + 6
    while any(abs(cx - px) < CHIP_W + 4 and abs(cy - py) < step for px, py in placed):
        cy += step
    return cy


def _node_text(graph: ClaimGraph, eid: str) -> tuple[str, str, str]:
    """(label, sub-line, full description) for a node."""
    e = graph.entities[eid]
    members = [graph.entities[p].label for p in e.participants]
    v = graph.case.variant
    if e.kind == "variant":
        sub = _position(v) if e.canonical_id == v.key else (e.canonical_id or "variant")
    elif e.kind in ("tf_group", "complex", "binding_event"):
        sub = f"{e.kind.replace('_', ' ')}: {', '.join(members)}" if members else e.kind.replace("_", " ")
    else:
        sub = " · ".join(x for x in (e.kind.replace("_", " "), e.canonical_id) if x)
    full = " · ".join(x for x in (e.label, e.kind.replace("_", " "), e.canonical_id, ", ".join(members)) if x)
    return _cut(e.label, 21), _cut(sub, 30), full


def layout(graph: ClaimGraph) -> dict[str, Any]:
    """Node boxes and claim edges for the mechanism graph: one column per entity kind (empty columns dropped), rows in
    entity-id order, every claim drawn (superseded ones too, so the layout is the same at every version). Edges are
    routed around nodes (_route) and chips never overlap (_free_row)."""
    used = sorted({e for c in graph.claims.values() for e in c.subject_ids + c.object_ids}, key=_num)
    columns = [(title, [e for e in used if graph.entities[e].kind in kinds]) for title, kinds in COLUMNS]
    columns = [(title, ids) for title, ids in columns if ids]
    if not columns:
        return {"view_box": [0, 0, 0, 0], "heads": [], "nodes": [], "edges": []}
    nodes: dict[str, dict[str, Any]] = {}
    heads = []
    for ci, (title, ids) in enumerate(columns):
        x = PAD + ci * (NODE_W + COL_GAP)
        heads.append({"x": x + NODE_W / 2, "y": PAD + 12, "text": title})
        for ri, eid in enumerate(ids):
            label, sub, full = _node_text(graph, eid)
            nodes[eid] = {"id": eid, "kind": graph.entities[eid].kind, "col": ci, "x": x,
                          "y": PAD + HEAD + ri * (NODE_H + ROW_GAP), "w": NODE_W, "h": NODE_H, "label": label,
                          "sub": sub, "title": full}
    pairs: Counter = Counter()
    channels: Counter = Counter()
    edges = []
    placed: list[tuple[float, float]] = []
    xs = [float(PAD)] + [n["x"] + NODE_W for n in nodes.values()]
    ys = [float(PAD)] + [n["y"] + NODE_H for n in nodes.values()]
    for cid, claim in graph.claims.items():
        paths, chip = [], None
        for s, o in ((s, o) for s in claim.subject_ids for o in claim.object_ids):
            key = tuple(sorted((s, o)))
            lane = 0.0
            if nodes[o]["col"] - nodes[s]["col"] not in (0, 1):     # through a channel: take its next lane
                row = max(nodes[s]["y"], nodes[o]["y"])
                k = channels[row] % 5
                lane = ((k + 1) // 2) * LANE * (1 if k % 2 else -1)
                channels[row] += 1
            path, points, (cx, cy) = _route(nodes[s], nodes[o], pairs[key], lane)
            pairs[key] += 1
            paths.append(path)
            xs += [pt[0] for pt in points]
            ys += [pt[1] for pt in points]
            if chip is None:
                cy = _free_row(cx, cy, placed)
                placed.append((cx, cy))
                chip = {"x": round(cx - CHIP_W / 2, 1), "y": round(cy - CHIP_H / 2, 1), "w": CHIP_W, "h": CHIP_H,
                        "cx": round(cx, 1), "cy": round(cy, 1)}
                xs += [chip["x"], chip["x"] + CHIP_W]
                ys += [chip["y"], chip["y"] + CHIP_H]
        edges.append({"claim": cid, "paths": paths, "chip": chip})
    left, top = min(xs) - PAD, min(ys) - PAD
    return {"view_box": [round(left, 1), round(top, 1), round(max(xs) + PAD - left, 1), round(max(ys) + PAD - top, 1)],
            "heads": heads, "nodes": list(nodes.values()), "edges": edges}


# --- HTML ------------------------------------------------------------------------------------------------------------

def _embed(data: Any) -> str:
    """The JSON for <script type="application/json">: <, > and & as \\u escapes, so no text can close the element or
    open markup; U+2028/2029 escaped too."""
    text = json.dumps(data, ensure_ascii=False, separators=(",", ":"))
    for char, escape in (("&", "\\u0026"), ("<", "\\u003c"), (">", "\\u003e"), ("\u2028", "\\u2028"),
                         ("\u2029", "\\u2029")):
        text = text.replace(char, escape)
    return text


def _h(value: Any) -> str:
    return html.escape(_text(value), quote=True)


def _link_html(link: Mapping[str, Any]) -> str:
    if link.get("url"):
        return f'<a href="{_h(link["url"])}" rel="noopener noreferrer">{_h(link["text"])}</a>'
    return _h(link["text"])


def _table_html(caption: str, headers: list[str], rows: list[list[str]], cls: str = "") -> str:
    """A static table; every cell is already escaped HTML."""
    head = "".join(f"<th scope=\"col\">{_h(h)}</th>" for h in headers)
    body = "".join("<tr>" + "".join(f"<td>{cell}</td>" for cell in row) + "</tr>" for row in rows)
    return (f'<div class="table-wrap"><table class="{_h(cls)}"><caption>{_h(caption)}</caption><thead><tr>{head}'
            f"</tr></thead><tbody>{body}</tbody></table></div>")


def _status_html(c: Mapping[str, Any]) -> str:
    badge = f'<span class="tag s-{_h(c["status"])}">{_h(c["status_label"])}</span>'
    if c["basis"]:
        badge += f' <span class="small">basis: {_h(c["basis"])}</span>'
    if c["flag"] != "none":
        badge += ' <span class="tag premise">premise failed</span>'
    if c["superseded_by"]:
        badge += f' <span class="tag">superseded by {_h(c["superseded_by"])}</span>'
    return badge


def _list_html(values: list[str], empty: str, sep: str = ", ") -> str:
    return sep.join(_h(v) for v in values) if values else f'<span class="muted">{_h(empty)}</span>'


def _linked(c: Mapping[str, Any], stance: str) -> list[str]:
    """The evidence ids a claim's current links hold with this stance (the last link per evidence item)."""
    current = {x["evidence"]: x for x in c["links"]}
    return [eid for eid, x in current.items() if x["stance"] == stance]


INVENTORY_HEADERS = ["Group", "DBD", "Members", "Paralog stem", "Best model", "Binds more", "z", "Models past gate",
                     "Evidence"]


def _inventory_evidence(r: Mapping[str, Any]) -> str:
    """A row's Evidence as plain text: its item, or, for a group whose gate-passing models disagree about the allele,
    each item with its allele and the TFs its models map to; then the claims that link any of them."""
    if r["discordant"]:
        text = "; ".join(f"{x['id']}: {x['allele'] or '?'} binds more (models of {', '.join(x['tfs']) or 'no TF'})"
                         for x in r["items"]) + "; the group's gate-passing models disagree"
    else:
        text = r["evidence"] or "–"
    return text + (f" (linked: {', '.join(r['claims'])})" if r["claims"] else "")


def _inventory_cells(r: Mapping[str, Any]) -> list[str]:
    """One inventory row as plain text cells (each format escapes them its own way)."""
    members = ", ".join(f"{m['tf']}" + (" (CIS-BP-mapped)" if m["mapping"] == "cisbp" else "") for m in r["members"])
    allele = f"{r['allele']} ({r['binds_more']})" if r["allele"] else (r["binds_more"] or "–")
    return [f"{r['group']} {r['label'] or ''}".strip(), r["dbd"] or "–", members or "–", r["stem"] or "–",
            r["best_model"] or "–", allele, str(r["z"]) if r["z"] is not None else "–",
            f"{r['n_pass']} / {r['n_models']}", _inventory_evidence(r)]


def _refused_questions(d: Mapping[str, Any]) -> list[str]:
    """Questions code closed as refused without asking a model (a repeat of one already answered, with nothing
    changed since), each with the reason recorded, as plain text."""
    def sentence(value: Any) -> str:
        text = _text(value)
        text = text[:1].upper() + text[1:]
        return text if not text or text.endswith((".", "?", "!")) else text + "."

    return [f"{q['id']} ({q['route']}): {sentence(q['text'])} {sentence(q['answer']) or 'Closed as refused.'}"
            for q in d["questions"] if q["status"] == "refused"]


def _inferred_text(c: Mapping[str, Any]) -> str:
    """An inferred candidate as plain text: its label, the evidence it rests on and the note, marked inferred."""
    basis = f"; from {', '.join(c['basis_evidence_ids'])}" if c["basis_evidence_ids"] else ""
    note = f": {_text(c['note'])}" if _text(c["note"]) else ""
    return f"{_text(c['label'])} (inferred{basis}){note}"


def _found_text(item: Mapping[str, Any], key: str) -> str:
    """An rsID or element code recorded for the case variant, with the tool call that reported it."""
    return f"{item[key]} ({item['tool_call']}" + (f", {item['tool']}" if item["tool"] else "") + ")"


def _case_rows(case: Mapping[str, Any]) -> list[tuple[str, list[str], str]]:
    """The case facts both formats list: (heading, plain-text values, text when there are none). What the request
    supplied is kept apart from what the run inferred and from what code found about the variant."""
    inferred = {k: [_inferred_text(c) for c in case["inferred"] if c["kind"] == k] for k in ("disease", "context")}
    return [("Disease, supplied", case["supplied_disease"], "none supplied"),
            ("Disease, inferred", inferred["disease"], "none inferred"),
            ("Context, supplied", [s["text"] for s in case["supplied_context"]], "none supplied"),
            ("Context, inferred", inferred["context"], "none inferred"),
            ("rsID, found by code", [_found_text(a, "rsid") for a in case["aliases"]], "none recorded"),
            ("Elements containing it, found by code", [_found_text(e, "element") for e in case["elements"]],
             "none recorded")]


def _stop_text(result: Mapping[str, Any]) -> str:
    """Why the run stopped: the stop reason's label, a budget stop said as such, and what the stop event adds."""
    detail = f" ({result['stop_event']}: {result['stop_detail']})" if result["stop_detail"] else ""
    return result["stop_label"] + (" (a budget stop)" if result["budget_stop"] else "") + detail


def _record_rows(d: Mapping[str, Any]) -> list[tuple[str, str]]:
    """Run-summary lines both formats show after the outcome, as plain text: whether the run can be re-executed (the
    engine's record, with its reasons when not), what a replay folder re-executed, hypotheses that code reinstated
    after the contradiction that rejected them was withdrawn, and rejections that no longer stand."""
    rows: list[tuple[str, str]] = []
    replay = d["meta"]["replay"]
    if replay["replayable"] is True:
        rows.append(("Replay", "replayable: no model reply was retried, refused or lost, so v2m v9 replay can "
                               "re-execute the run from this folder's tool results and the saved model replies"))
    elif replay["replayable"] is False:
        rows.append(("Replay", "not replayable: " + ("; ".join(replay["reasons"]) or "no reason was recorded")))
    if of := replay["of"]:
        n = of["differences"]
        rows.append(("Replay of", f"{of['run'] or 'a saved run'}: {of['status_label'] or 'status not recorded'}"
                     + (f" ({_count(n, 'difference')})" if isinstance(n, int) and not isinstance(n, bool) else "")))
    reinstated = [note for h in d["hypotheses"] for note in h["reinstated_notes"]]
    stale = [h["stale_note"] for h in d["hypotheses"] if h["stale_note"]]
    if reinstated:
        rows.append(("Reinstated", " ".join(reinstated)))
    if stale:
        rows.append(("Rejections that no longer stand", " ".join(stale)))
    return rows


def _chain_ladder(view: Mapping[str, Any]) -> str:
    """The ladder in one sentence, strongest first (the last rung, nothing linked, needs no gloss)."""
    return "Kinds of evidence, strongest first: " + "; ".join(
        f"{r['label'].lower()}: {r['meaning']}" for r in view["rungs"][:-1]) + "."


def _chain_unplaced(view: Mapping[str, Any]) -> str:
    return "Claims not placed on the chain: " + "; ".join(f"{u['id']} ({u['why']})" for u in view["unplaced"]) + "."


def _chain_html(d: Mapping[str, Any]) -> str:
    """The mechanism chain as a static block: the link table, the open hypotheses link by link with their order,
    and what is missing. Empty when no claim is a link of the chain."""
    view = d["chain"]
    if not view["placed"]:
        return ""
    rows = []
    for r in chain.chain_rows(view, d["case"]["variant"]["alt"]):
        badge = f'<span class="tag {RUNG_CLASSES.get(r["rung"], "s-unresolved")}">{_h(r["rung_label"])}</span>'
        if r["tied"]:
            badge += ' <span class="small">tied</span>'
        leading = "<br>".join(_h(text) for text in r["leading"])
        if r["leading_more"]:
            leading += f'<br><span class="small">and {r["leading_more"]} more</span>'
        rows.append([f'<strong>{_h(r["label"])}</strong><br><span class="small">{_h(r["question"])}</span>', badge,
                     leading or '<span class="muted">–</span>', _h(r["others"]) or '<span class="muted">–</span>'])
    parts = ["<h3>Mechanism chain</h3>", f'<p class="small">{_h(view["note"])} {_h(_chain_ladder(view))}</p>',
             _table_html("The variant's route to a trait, link by link", CHAIN_HEADERS, rows, "chain")]
    if view["missing"]:
        parts.append('<ul class="gaps">' + "".join(f"<li>{_h(m['text'])}</li>" for m in view["missing"]) + "</ul>")
    if view["hypotheses"]:
        parts.append(_table_html("Open hypotheses, link by link (their own claims only)",
                                 ["Hypothesis", "Disposition", *chain.LINK_LABEL.values()],
                                 [[_h(cell) for cell in row] for row in chain.hypothesis_rows(view)],
                                 "chain-hypotheses"))
        parts += [f"<p>{_h(text)}</p>" for text in view["order"]["text"]]
    if view["unplaced"]:
        parts.append(f'<p class="small">{_h(_chain_unplaced(view))}</p>')
    return "".join(parts)


def _left_out(ranked: Mapping[str, Any]) -> str:
    """Candidates that enter no chain because they are contradicted in scope, as one sentence; "" when none."""
    if not ranked["left_out"]:
        return ""
    return "In no chain, because contradicted in scope: " + "; ".join(
        f"{chain.LINK_LOWER[x['link']]}: {', '.join(x['names'])}" for x in ranked["left_out"]) + "."


def _tie_line(d: Mapping[str, Any]) -> str:
    """The judge's reading of a tie for first in one line, shown under the answer's headline; empty for a run with
    no judge or no tie (the table section gives the candidates and their quotations)."""
    found = (d.get("table") or {}).get("judgement")
    return f"Reading the tie. {found['text']}" if found else ""


def _ranked_html(d: Mapping[str, Any]) -> str:
    """The run's answer as a static section: the leading chain (or the chains tied for first) link by link, then
    every chain in rank order with the rule that orders them."""
    view = d["chain"]
    ranked = view["ranked"]
    head = ('<section id="answer" aria-labelledby="answer-h"><span class="section-no">ANSWER</span>'
            '<h2 id="answer-h">Ranked mechanism chains</h2>')
    if not ranked["chains"]:
        return head + f'<p class="muted">{_h(NO_CHAIN)}</p></section>'
    alt = d["case"]["variant"]["alt"]
    steps = []
    for step in chain.strip_rows(view, alt):
        detail = "".join(f'<span class="small">{_h(part)}</span>' for part in step["detail"])
        steps.append(f'<li class="route-step{" aside" if step["key"] == "trait" else ""}">'
                     f'<span class="route-label">{_h(step["label"])}</span>'
                     f'<span class="route-name">{_h(step["names"]) or "–"}</span>'
                     f'<span class="tag {RUNG_CLASSES.get(step["kind"] or "none", "s-unresolved")}">'
                     f'{_h(step["kind_text"])}</span>{detail}</li>')
    rows = [[f'<span class="num">{_h(row[0])}</span>', f"<strong>{_h(row[1])}</strong>", *(_h(c) for c in row[2:])]
            for row in chain.ranked_rows(view, alt)]
    notes = " ".join(_h(text) for text in (chain.ranked_more(view), _left_out(ranked), chain.SHARED_NOTE,
                                           chain.unclaimed_text(view)) if text)
    variant = d["case"]["variant"]
    factors = chain.factor_rows(view, variant["ref"], alt)
    more = view["factors"]["not_listed"]
    factor_block = "" if not factors else (
        _table_html("The transcription factors in these chains: what the lookups returned (shown, never ranked)",
                    chain.FACTOR_HEADERS, [[f"<strong>{_h(row[0])}</strong>", *(_h(c) for c in row[1:])]
                                           for row in factors], "factors")
        + f'<p class="small">{_h(chain.FACTOR_NOTE)}'
        + (f" {more} more named factor{'s' if more != 1 else ''} not listed." if more else "") + "</p>")
    tie = _tie_line(d)
    return (head + f'<p class="lead">{_h(ranked["headline"])}</p>' + (f"<p>{_h(tie)}</p>" if tie else "")
            + '<ol class="route" aria-label="The leading chain, link by link">' + "".join(steps) + "</ol>"
            + (f'<p>{_h(ranked["support"])}</p>' if ranked["support"] else "")
            + (f'<p><strong>Joined.</strong> {_h(ranked["join"])}</p>' if ranked.get("join") else "")
            + _table_html(f"All {ranked['total']} chains in rank order (= marks a tie)" if ranked["total"] > 1
                          else "The only chain the claims give", chain.RANKED_HEADERS, rows, "ranked")
            + f'<p class="small">{notes}</p>' + factor_block
            + f'<p class="small">{_h(ranked["rule"])}</p></section>')


TABLE_TITLE = "Chain table"
TABLE_LEAD = ("Every chain is eight small claims: at each of four steps, that the two alleles differ and that the parts "
              "are in place. Each claim has one cell per kind of record. \"Nothing found\" means a source was asked; "
              "\"not checked\" means nobody looked, or records on file were never judged; \"no source\" means the "
              "workflow has none of that kind for the claim.")


def _table_caption(t: Mapping[str, Any]) -> str:
    tied = f", one of {t['tied']} tied for first" if t["tied"] > 1 else ""
    return f"The leading chain{tied}: {t['title']}. The run stated {t['stated']} of its 8 claims."


def _table_notes(t: Mapping[str, Any]) -> list[str]:
    """The lines under the table: where the literature column comes from (a run with the reader), what the second
    reading found (a run with the critic), then the rules."""
    return [x for x in (t.get("reading"), t.get("critique"), t["rules"]) if x]


# --- under the table: the numbers each source returned, and what would fill the gaps ---------------------------------

NUMBERS_TITLE = "The numbers behind the cells"
NUMBERS_LEAD = ("What each source returned for the claims of the leading chain. Code copied every number from the saved "
                "record, and no model typed one. The numbers are shown and never ranked on: a chain's place rests on "
                "the kind of evidence under each claim, not on its size.")
NUMBERS_HEADERS = ["Claim", "Kind of record", "Source", "Records", "What it returned"]
FILLS_TITLE = "What would fill the gaps"
FILLS_LEAD = ("Suggested, not performed. For each claim of the leading chain that no measurement supports, the kind of "
              "record that would. Code wrote these from the table's rule for which record counts for which claim, with "
              "the names on file. No model wrote them.")
FILLS_NONE = "Every claim of this chain rests on a measurement, or on the kind of record it can have."
FILLS_POINTER = f'See "{FILLS_TITLE}" under the chain table.'
SOURCE_LABELS: dict[tuple[str, str], str] = {
    ("qbic_inventory", "prediction"): "QBiC-SELEX",
    ("adastra_asb", "occupancy"): "ADASTRA, ChIP-seq reads counted by allele",
    ("tf_occupancy_set", "occupancy"): "ReMap ChIP-seq peaks",
    ("gtex_eqtl", "association"): "GTEx eQTL",
    ("ccre_overlap", "association"): "SCREEN eQTL links",
    ("ccre_overlap", "annotation"): "ENCODE registry of regulatory elements",
    ("credible_sets_all", "statistical_inference"): "Open Targets credible sets",
    ("credible_sets_l2g", "statistical_inference"): "Open Targets credible sets",
    ("credible_sets_all", "precomputed_prediction"): "Open Targets locus-to-gene score",
    ("credible_sets_l2g", "precomputed_prediction"): "Open Targets locus-to-gene score",
    ("gwas_associations", "association"): "GWAS Catalog",
    ("udacha_asa", "occupancy"): "UDACHA, open-chromatin reads counted by allele",
    ("mavedb_reporter", "reporter_assay"): "MaveDB, saturation-mutagenesis reporter assays",
    ("protein_qtl_sets", "statistical_inference"): "Open Targets protein QTL credible sets",
    ("tumour_recurrence", "association"): "cBioPortal, tumours of the MSK-IMPACT 2017 cohort",
}
TOOL_LABELS: dict[str, str] = {
    "gene_disease": "Open Targets gene and disease records", "literature_read": "Articles read by the model",
    "variant_annotation": "Ensembl annotation", "chip_occupancy": "ChIP-seq peaks"}
ELEMENT_CLASSES: dict[str, str] = {"PLS": "promoter-like", "pELS": "proximal enhancer-like",
                                   "dELS": "distal enhancer-like", "CA-CTCF": "accessible, with CTCF",
                                   "CA-H3K4me3": "accessible, with H3K4me3", "CA-TF": "accessible, with a TF",
                                   "CA": "accessible", "TF": "bound by a TF"}
NAMES_SHOWN = 4                                           # names a line lists before it counts the rest
NEEDS: dict[str, str] = {"none": "nothing supports it", "prediction": "predicted only",
                         "association": "associated only"}   # in this order: the weakest claim first


def _floats(evs: Iterable[Evidence], key: str) -> list[float]:
    """The values of one field over a group of records, for those that hold a number there."""
    out = []
    for e in evs:
        try:
            out.append(float((e.data or {}).get(key)))
        except (TypeError, ValueError):
            continue
    return out


def _span(values: list[float], fmt: Callable[[float], str]) -> str:
    """One value in words, or the lowest and the highest of several."""
    if not values:
        return ""
    low, high = fmt(min(values)), fmt(max(values))
    return low if low == high else f"{low} to {high}"


def _p_text(p: float) -> str:
    return "below 1e-300" if p <= 0 else f"{p:.1e}"


def _some(values: Iterable[Any], limit: int = NAMES_SHOWN) -> str:
    """The first few distinct names, then how many more."""
    names = list(dict.fromkeys(str(v) for v in values if v))
    return ", ".join(names[:limit]) + (f" and {len(names) - limit} more" if len(names) > limit else "")


def _joined(*parts: str) -> str:
    return "; ".join(x for x in parts if x)


def _source(tool: str, ev: Evidence) -> str:
    """The name a record's source goes by in the numbers table. A colocalisation and a credible set come from one
    tool and say different things, so they are two sources."""
    if tool.startswith("credible_sets") and "h4" in (ev.data or {}):
        return "Open Targets colocalisations"
    return (SOURCE_LABELS.get((tool, ev.evidence_class)) or TOOL_LABELS.get(tool) or tool.replace("_", " ")
            or "a record")


def _returned(tool: str, cls: str, evs: list[Evidence]) -> str:
    """What the records of one source returned for a claim, in the numbers the source gave. Several records give the
    lowest and the highest value: a range says what is on file without picking a best one."""
    n, data = len(evs), [e.data or {} for e in evs]
    alleles = {e.allele for e in evs if e.allele}
    allele = next(iter(alleles)) if len(alleles) == 1 else None
    if tool == "qbic_inventory":
        lines = []
        for e, d in zip(evs, data, strict=True):
            z = _floats([e], "z")
            top = in_top_share(d.get("group_id"), z[0]) if z else None
            lines.append(_joined(
                f"group {d.get('group_id')}" + (f" ({d['dbd']})" if d.get("dbd") else ""),
                f"more binding to {e.allele}" if e.allele else "",
                f"|z| {abs(z[0]):.1f}" if z else "", _span(_floats([e], "p"), lambda x: f"p {_p_text(x)}"),
                f"{d['n_pass']} of {d['n_models']} models past the gate" if d.get("n_models") else "",
                "" if top is None else f"{'in' if top else 'not in'} the top 10% for this group"))
        return " / ".join(lines[:2]) + (f" / and {_count(n - 2, 'more record')}" if n > 2 else "")
    if tool == "adastra_asb":
        lines = []
        for e, d in zip(evs, data, strict=True):
            fdr = _floats([e], "fdr_ref") + _floats([e], "fdr_alt")
            size = _floats([e], "effect_size_ref") + _floats([e], "effect_size_alt")
            lines.append(_joined(
                (_some(e.about_tfs) or "the protein") + (f": reads favour {e.allele}" if e.allele else ""),
                f"FDR {min(fdr):.2g}" if fdr else "", f"effect size {max(size):.2f}" if size else "",
                f"{d['tf_experiments']} experiments" if d.get("tf_experiments") else ""))
        return " / ".join(lines)
    if tool == "udacha_asa":
        favoured = Counter(e.allele for e in evs if e.allele)
        sides = " and ".join(f"{base} in {_count(k, 'cell type')}" for base, k in favoured.most_common())
        fdr = [min(x) for e in evs if (x := _floats([e], "fdr_ref") + _floats([e], "fdr_alt"))]
        assays = _some(dict.fromkeys(str(d.get("assay") or "") for d in data))
        return _joined(f"{assays} reads favour {sides}" if sides else f"{assays} reads favour each allele somewhere",
                       _span(fdr, lambda x: f"FDR {x:.2g}").replace(" to FDR ", " to "),
                       "cell types: " + _some(str(d.get("cell_type") or "") for d in data))
    if tool == "mavedb_reporter":
        effect = _span(_floats(evs, "score"), lambda x: f"{x:+.2f}")
        tags = _span(_floats(evs, "unique_tags"), lambda x: f"{x:.0f}")
        cells = _some(dict.fromkeys(str(d.get("cells") or "") for d in data))
        named = "cells: " if all(d.get("cells") for d in data) else "cells, where a set names them: "
        return _joined(f"log2 effect on reporter activity {effect}, as each set records it" if effect else "",
                       _span(_floats(evs, "p_value"), lambda x: f"p {_p_text(x)}").replace(" to p ", " to "),
                       f"{tags} barcodes" if tags else "", named + cells if cells else "",
                       f"{_count(n, 'score set')}: " + _some(str(d.get("score_set") or "").rsplit(":", 1)[-1]
                                                              for d in data))
    if tool == "protein_qtl_sets":
        inside = sum(1 for d in data if d.get("in_95_set"))
        chance = _span(_floats(evs, "pip"), lambda x: f"{x:.2g}")
        where = _some(dict.fromkeys(str(d.get("biosample") or "") for d in data))
        return _joined(f"fine-mapping probability {chance}" if chance else "",
                       f"in the 95% credible set in {inside} of {n}", f"protein measured in {where}" if where else "",
                       _some(dict.fromkeys(str(d.get("project") or "") for d in data), 3))
    if tool == "tumour_recurrence":
        rows = sorted(data, key=lambda d: -int(d.get("patients_with_mutation") or 0))
        return "called in the tumours of " + _some(
            f"{d.get('patients_with_mutation')} of {d.get('patients_sequenced')} patients with {d.get('cancer_type')}"
            for d in rows)
    if tool == "literature_read":
        articles = list(dict.fromkeys(x for e in evs for x in e.source_ids if x.startswith("PMID:")))
        return (f"{_count(n, 'experiment')} in {_count(len(articles), 'article')}"
                + (f" ({_some(articles, 3)})" if articles else "") + "; the report quotes the sentences")
    if cls == "occupancy":
        distance = _span(_floats(evs, "summit_distance"), lambda x: f"{x:.0f}")
        cells = _some(d.get("biosample_label") or (e.context.label if e.context else "")
                      for e, d in zip(evs, data, strict=True))
        tfs = _some(x for e in evs for x in e.about_tfs)
        return _joined(f"a peak over the variant in {_count(n, 'experiment')}", f"TFs: {tfs}" if tfs else "",
                       f"cell types: {cells}" if cells else "",
                       f"summits {distance} bp from the variant" if distance else "")
    if tool == "gtex_eqtl" or (tool == "ccre_overlap" and cls == "association"):
        size = _span(_floats(evs, "nes") + _floats(evs, "slope"), lambda x: f"{x:+.2f}")
        tissues = _some(str(d.get("tissue") or "").replace("_", " ") for d in data)
        return _joined(f"effect size {size}" + (f" for {allele}" if allele else "") if size else "",
                       _span(_floats(evs, "p"), lambda x: f"p {_p_text(x)}").replace(" to p ", " to "),
                       f"tissues: {tissues}" if tissues else "")
    if tool.startswith("credible_sets") and all("h4" in d for d in data):
        shared = _span(_floats(evs, "h4"), lambda x: f"{x:.2f}")
        return _joined(f"probability of one shared causal variant (H4) {shared}" if shared else "",
                       _some((d.get("method") for d in data), 3))
    if cls == "statistical_inference" and tool.startswith("credible_sets"):
        inside = sum(1 for d in data if d.get("in_95_set"))
        chance = _span(_floats(evs, "pip"), lambda x: f"{x:.2g}")
        return _joined(f"fine-mapping probability {chance}" if chance else "",
                       f"in the 95% credible set in {inside} of {n}",
                       _some((d.get("finemapping_method") for d in data), 3))
    if cls == "precomputed_prediction":
        score = _span(_floats(evs, "score"), lambda x: f"{x:.2f}")
        return f"score {score}" if score else ""
    if tool == "gwas_associations":
        effect = str(data[0].get("effect_text") or "") if n == 1 else ""
        return _joined(_span(_floats(evs, "p"), lambda x: f"p {_p_text(x)}").replace(" to p ", " to "),
                       effect + (f" for {allele}" if effect and allele else ""))
    if tool == "gene_disease":
        score = _span(_floats(evs, "score"), lambda x: f"{x:.2f}")
        return _joined(f"source score {score}" if score else "",
                       "sources: " + _some(str(d.get("datasource") or "").replace("_", " ") for d in data))
    if tool == "ccre_overlap":
        return _joined(_some(x for e in evs for x in e.about_elements),
                       _some(f"{ELEMENT_CLASSES.get(str(d.get('class')), 'class')} ({d.get('class')})"
                             for d in data if d.get("class")))
    if tool == "variant_annotation":
        return _some(str(c).replace("_", " ") for d in data for c in d.get("consequences") or [])
    return ""


def _claim_title(claim: Any) -> str:
    return f"{dict(chain_table.STEPS)[claim.step]}: {dict(chain_table.PARTS)[claim.part].lower()}"


def _number_rows(g: ClaimGraph, table: Any) -> list[list[str]]:
    """One row per source behind each cell of the first chain (NUMBERS_HEADERS): the records counted for the claim,
    or against it, and what they returned. A record listed beside a claim counts for nothing and is not shown."""
    first, rows = table.chains[0], []
    for key in chain_table.SLOT_KEYS:
        claim = table.claims[str(first.claims[key])]
        for lane, lane_label in chain_table.LANES:
            groups: dict[tuple[str, str, str], list[Evidence]] = {}
            for r in claim.cells[lane].records:
                if r.stance != "beside" and r.id in g.evidence:
                    ev = g.evidence[r.id]
                    groups.setdefault((_source(r.tool or "", ev), r.tool or "", r.stance), []).append(ev)
            for (source, tool, stance), evs in groups.items():
                rows.append([_claim_title(claim), lane_label,
                             source + (" (counted against)" if stance == "disagrees" else ""), str(len(evs)),
                             _returned(tool, evs[0].evidence_class, evs) or "no number in the record"])
    return rows


def _fill_rows(g: ClaimGraph, table: Any) -> list[dict[str, str]]:
    """What would fill each claim of the first chain that no measurement supports, weakest claim first: the kind of
    record the table counts for that claim (docs/chain-table.md), with the names the run has on file. A tie for
    first comes before them, with what would separate it."""
    first = table.chains[0]
    claims = {key: table.claims[str(first.claims[key])] for key in chain_table.SLOT_KEYS}

    def counted(key: str, lane: str) -> list[Evidence]:
        return [g.evidence[r.id] for r in claims[key].cells[lane].records
                if r.stance == "supports" and r.id in g.evidence]

    def tied(key: str) -> list[Any]:
        """The distinct claims the chains tied for first hold in a slot, by what they name."""
        return list({c.label: c for c in (table.claims[str(x.claims[key])] for x in leaders)}.values())

    v = g.case.variant
    somatic = g.case.origin == "somatic"
    leaders = [c for c in table.chains if c.rank == 1]
    factors, targets = tied("binding.allele"), tied("gene.allele")
    tf = _some(claims["binding.allele"].names.get("tfs") or []) or "the transcription factor"
    gene = _some((x for c in targets for x in c.names.get("genes") or []), NAMES_SHOWN)
    element = _some(claims["activity.premise"].names.get("elements") or [], 2) or "the variant's site"
    cells = _some(((e.data or {}).get("biosample_label") for e in counted("binding.premise", "database")
                   if e.context is not None and e.context.biosample_kind == "cell_line"), 3)
    favoured = {e.allele for e in counted("binding.allele", "model") if e.allele}
    if len(factors) > 1:                          # the first chain's TF is one of several: name none of them here
        tf, cells, favoured = "each of the tied transcription factors", "", set()
    order = list(NEEDS)
    found: list[tuple[tuple[int, int], dict[str, str]]] = []

    def add(key: str, kind: str, text: str) -> None:
        claim = claims[key]
        found.append(((order.index(claim.strongest), chain_table.SLOT_KEYS.index(key)),
                      {"claim": _claim_title(claim), "state": NEEDS[claim.strongest], "kind": kind, "text": text}))

    def needs(key: str, *kinds: str) -> bool:
        return claims[key].strongest in (kinds or tuple(NEEDS))

    if needs("binding.allele"):
        add("binding.allele", "Experiment",
            f"Compare the binding of {tf} to the {v.ref} and {v.alt} alleles directly: a binding assay with both "
            "alleles, or ChIP reads counted by allele in cells that carry both."
            + (f" ReMap has a peak over the variant in {cells}." if cells else "")
            + (f" QBiC-SELEX predicts more binding to {next(iter(favoured))}, which is the result to expect."
               if len(favoured) == 1 and claims["binding.allele"].strongest == "prediction" else ""))
    if needs("binding.premise", "none"):
        subject = tf if len(factors) > 1 else f"the transcription factor ({tf})"
        add("binding.premise", "Experiment", f"Show {subject} at the site: ChIP in a cell type where the element is "
            "active.")
        if not g.case.supplied_context:
            add("binding.premise", "Lookup", "Give the run a cell context, and the expression of the transcription "
                "factor there is looked up.")
    if needs("activity.allele"):
        add("activity.allele", "Experiment",
            "Compare the regulatory activity of the two alleles: a reporter assay with both, or the allele edited in "
            "the genome with accessibility or enhancer marks read out" + (f", for example in {cells}" if cells else "")
            + ".")
        add("activity.allele", "Model run", "No model in this version predicts the alleles' regulatory activity. A "
            "sequence-to-activity model would give this cell a prediction.")
    if needs("activity.premise", "none"):
        add("activity.premise", "Experiment", "The variant lies in no registered regulatory element. An accessibility "
            "or histone-mark assay at the site, in a cell type that matters for the trait, would show whether it is "
            "one.")
    if needs("gene.allele", "none") and not gene:
        add("gene.allele", "Experiment",
            "No source names a gene whose RNA differs between the alleles. "
            + ("An eQTL cannot exist for a somatic mutation. The allele edited in the genome, or tumours with and "
               "without the mutation compared, with the RNA of nearby genes read out, would name one." if somatic else
               "An eQTL of this variant, or the allele edited in the genome with the RNA of nearby genes read out, "
               "would name one."))
    elif needs("gene.allele"):
        add("gene.allele", "Experiment", f"Edit the allele in the genome and read out the RNA of {gene}. An "
            "association cannot separate this variant from the variants inherited with it.")
    if gene and needs("gene.premise", "none"):
        add("gene.premise", "Experiment", f"Silence or delete the element ({element}) and read out the RNA of {gene}.")
    if needs("trait.allele", "none"):
        add("trait.allele", "Source",
            "The sources this run reads hold inherited variants, not somatic mutations. How often the mutation recurs "
            "in tumours, by cancer type, would be the matching record, and no such source is connected yet."
            if somatic else "No association of this variant with a trait is on file in the sources this run reads.")
    if gene and needs("trait.premise", "none", "prediction"):
        add("trait.premise", "Experiment", f"Perturb {gene} and read out the trait, or the cell behaviour behind it. "
            "Genetic evidence that ties the gene itself to the trait would be an association for the same claim.")
    fills = [row for _, row in sorted(found, key=lambda x: x[0])]
    for group, word, how in ((targets, "target gene", "the allele edited in the genome, with the RNA of each gene "
                              "read out"),
                             (factors, "transcription factor", "a measurement of the alleles' binding where there "
                              "is only a prediction")):
        if len(group) > 1:
            fills.insert(0, {"claim": "The tie for first", "state": f"{len(leaders)} chains", "kind": "Experiment",
                             "text": f"The tied chains differ in the {word}: {_some((c.label for c in group), 3)}. "
                                     "They hold the same kinds of evidence, so a stronger kind of record for one of "
                                     f"them would separate them: {how}."})
    return fills


def table_extras(g: ClaimGraph) -> dict[str, Any]:
    """What the table section shows beyond table.report_view: the numbers behind the first chain's cells and what
    would fill its gaps. Empty for a run with no chain."""
    from . import loop
    again = loop.report_view(g)                  # only a run with the loop has the key: other reports are unchanged
    table = chain_table.from_graph(g)
    if not table.chains:
        return {"numbers": [], "fills": [], **({"loop": again} if again else {})}
    return {"numbers": _number_rows(g, table), "fills": _fill_rows(g, table), **({"loop": again} if again else {})}


def _numbers_html(t: Mapping[str, Any]) -> str:
    if not t.get("numbers"):
        return ""
    return (f'<h3 id="numbers-h">{_h(NUMBERS_TITLE)}</h3><p class="small">{_h(NUMBERS_LEAD)}</p>'
            + _table_html(NUMBERS_TITLE, NUMBERS_HEADERS, [[_h(cell) for cell in row] for row in t["numbers"]],
                          "numbers"))


def _fills_html(t: Mapping[str, Any]) -> str:
    if "fills" not in t or not t.get("rows"):
        return ""
    items = "".join(f'<li><strong>{_h(f["claim"])}</strong> ({_h(f["state"])}). {_h(f["kind"])}: {_h(f["text"])}</li>'
                    for f in t["fills"]) or f"<li>{_h(FILLS_NONE)}</li>"
    return (f'<h3 id="fills-h">{_h(FILLS_TITLE)}</h3><p class="small">{_h(FILLS_LEAD)}</p>'
            f'<ul class="gaps">{items}</ul>')


LOOP_TITLE = "Going back for evidence"


def _loop_html(t: Mapping[str, Any]) -> str:
    """What the loop did after the first reading: its rounds, and for each search what it found and what came of
    it. The effort is shown so that a chain which leads because more was searched for it can be seen."""
    again = t.get("loop")
    if not again:
        return ""
    rounds = "".join(f"<li>{_h(x)}</li>" for x in again["rounds"])
    table = (_table_html(LOOP_TITLE, again["headers"], [[_h(c) for c in row] for row in again["effort"]], "numbers")
             if again["effort"] else "")
    notes = "".join(f'<p class="small">{_h(x)}</p>' for x in (again["memory"], again["not_built"]) if x)
    return (f'<h3 id="loop-h">{_h(LOOP_TITLE)}</h3><p>{_h(again["lead"])} {_h(again["moved"])}</p>'
            f'<ul class="gaps">{rounds}</ul>{table}{notes}')


def _loop_markdown(t: Mapping[str, Any]) -> list[str]:
    again = t.get("loop")
    if not again:
        return []
    return [f"### {LOOP_TITLE}", "", _md(f"{again['lead']} {again['moved']}"), "",
            *[f"- {_md(x)}" for x in again["rounds"]], "",
            *(_md_table(again["headers"], [[_md(c) for c in row] for row in again["effort"]])
              if again["effort"] else []),
            *(line for x in (again["memory"], again["not_built"]) if x for line in (_md(x), ""))]


def _numbers_markdown(t: Mapping[str, Any]) -> list[str]:
    if not t.get("numbers"):
        return []
    return [f"### {NUMBERS_TITLE}", "", _md(NUMBERS_LEAD), "",
            *_md_table(NUMBERS_HEADERS, [[_md(cell) for cell in row] for row in t["numbers"]])]


def _fills_markdown(t: Mapping[str, Any]) -> list[str]:
    if "fills" not in t or not t.get("rows"):
        return []
    return [f"### {FILLS_TITLE}", "", _md(FILLS_LEAD), "",
            *([f"- **{_md(f['claim'])}** ({_md(f['state'])}). {_md(f['kind'])}: {_md(f['text'])}" for f in t["fills"]]
              or [f"- {_md(FILLS_NONE)}"]), ""]


def _no_next(d: Mapping[str, Any]) -> str:
    """What the suggestions section says when the run's result names no next experiment."""
    return FILLS_POINTER if (d.get("table") or {}).get("fills") else "None suggested."


QUOTES_TITLE = "What the articles say"
QUOTES_LEAD = ("The sentences the literature cells of this chain were read from. Code copied each one from the "
               "article, so it is the article's own text; a quotation counts for a claim only where the table says so.")


def _quote_head(q: Mapping[str, Any]) -> str:
    """Step and claim of one group of quotations, with what the claim names."""
    return f"{q['step']}: {q['claim'][0].lower()}{q['claim'][1:]} ({q['names']})"


def _quote_tail(x: Mapping[str, Any]) -> str:
    """How a quotation counts: its kind of evidence, for or beside the claim, and how many records quote it."""
    return (f"{x['kind']}, {x['counts']}"
            + (f"; {x['records']} records quote this sentence" if x["records"] > 1 else "")
            + (f"; {x['second']}" if x.get("second") else ""))


TIE_TITLE = "Reading the tie"
TIE_LEAD = ("The chains tied for first hold the same kinds of evidence behind every claim. Articles also report "
            "experiments that test no single claim, so no cell counts them: a TF removed and the difference between "
            "the alleles read out, the element deleted and a gene's protein read out. A second model read those for "
            "each tied TF and gene. Its answers are below with the sentences they rest on, copied from the "
            "articles by code. They change no cell and no rank.")


def _tie_answer(row: Mapping[str, Any]) -> str:
    """One candidate's answer in words, with whether both readings gave it and how many experiments were read."""
    twice = " (both readings)" if row.get("agreed") else ""
    more = row["on_file"] - row["sent"]
    read = (f"{row['sent']} experiment{'s' if row['sent'] != 1 else ''} "
            f"{'sent' if row['answer'] == 'no_answer' else 'read'}"
            + (f", {more} more on file beyond the cap" if more > 0 else ""))
    return f"{row['words']}{twice}; {read}"


def _tie_quote_tail(x: Mapping[str, Any]) -> str:
    return "the judge named these sentences; code copied them" if x["pointed"] else "the record's own quotation"


def _tie_html(t: Mapping[str, Any]) -> str:
    j = t.get("judgement")
    if not j:
        return ""
    items = []
    for row in j["rows"]:
        quotes = "".join(f'<li>{_link_html(source_link(x["source"]))}: <q>{_h(x["passage"])}</q> '
                         f'<span class="small">({_h(_tie_quote_tail(x))})</span></li>' for x in row["quotes"])
        reason = f' <span class="small">{_h(row["reason"])}</span>' if row["reason"] else ""
        items.append(f'<li><strong>{_h(row["candidate"])}</strong>: {_h(_tie_answer(row))}.{reason}'
                     + (f"<ul>{quotes}</ul>" if quotes else "") + "</li>")
    return (f'<h3 id="tie-h">{_h(TIE_TITLE)}</h3><p class="small">{_h(TIE_LEAD)}</p><p>{_h(j["text"])}</p>'
            + (f'<ul class="gaps quotes">{"".join(items)}</ul>' if items else ""))


def _tie_markdown(t: Mapping[str, Any]) -> list[str]:
    j = t.get("judgement")
    if not j:
        return []
    lines = [f"### {TIE_TITLE}", "", _md(TIE_LEAD), "", _md(j["text"]), ""]
    for row in j["rows"]:
        lines.append(f"- **{_md(row['candidate'])}**: {_md(_tie_answer(row))}."
                     + (f" {_md(row['reason'])}" if row["reason"] else ""))
        lines += [f"  - {_md(x['source'])}: \"{_md(x['passage'])}\" ({_md(_tie_quote_tail(x))})"
                  for x in row["quotes"]]
    return [*lines, ""] if j["rows"] else lines


def _quotes_html(t: Mapping[str, Any]) -> str:
    groups = t.get("quotes") or []
    if not groups:
        return ""
    items = []
    for q in groups:
        lines = "".join(
            f'<li>{_link_html(source_link(x["source"]))}: <q>{_h(x["passage"])}</q> '
            f'<span class="small">({_h(_quote_tail(x))})</span></li>' for x in q["quotes"])
        more = (f'<li class="small">{q["more"]} more quotation{"s" if q["more"] != 1 else ""} in table.json</li>'
                if q["more"] else "")
        items.append(f"<li><strong>{_h(_quote_head(q))}</strong><ul>{lines}{more}</ul></li>")
    return (f'<h3 id="quotes-h">{_h(QUOTES_TITLE)}</h3><p class="small">{_h(QUOTES_LEAD)}</p>'
            f'<ul class="gaps quotes">{"".join(items)}</ul>')


def _table_section_html(d: Mapping[str, Any]) -> str:
    """The first chain as its eight claims with three cells each, after the answer, then the sentences its
    literature cells quote."""
    t = d["table"]
    rows = [[_h(row[0]), _h(row[1]), f"<strong>{_h(row[2])}</strong>", *(_h(cell) for cell in row[3:])]
            for row in t["rows"]]
    return ('<section id="table" aria-labelledby="table-h"><span class="section-no">TABLE</span>'
            f'<h2 id="table-h">{_h(TABLE_TITLE)}</h2><p>{_h(TABLE_LEAD)}</p>'
            + _table_html(_table_caption(t), t["headers"], rows, "cells")
            + "".join(f'<p class="small">{_h(x)}</p>' for x in _table_notes(t)) + _numbers_html(t)
            + _fills_html(t) + _loop_html(t) + _tie_html(t) + _quotes_html(t)
            + "</section>")


def _quotes_markdown(t: Mapping[str, Any]) -> list[str]:
    groups = t.get("quotes") or []
    if not groups:
        return []
    lines = [f"### {QUOTES_TITLE}", "", _md(QUOTES_LEAD), ""]
    for q in groups:
        lines.append(f"- **{_md(_quote_head(q))}**")
        lines += [f"  - {_md(x['source'])}: \"{_md(x['passage'])}\" ({_md(_quote_tail(x))})" for x in q["quotes"]]
        if q["more"]:
            lines.append(f"  - {q['more']} more quotation{'s' if q['more'] != 1 else ''} in table.json")
    return [*lines, ""]


def _table_markdown(d: Mapping[str, Any]) -> list[str]:
    t = d["table"]
    return [f"## {TABLE_TITLE}", "", _md(TABLE_LEAD), "", _md(_table_caption(t)), "",
            *_md_table(t["headers"], [[_md(cell) for cell in row] for row in t["rows"]]),
            *(line for x in _table_notes(t) for line in (_md(x), "")), *_numbers_markdown(t),
            *_fills_markdown(t), *_loop_markdown(t), *_tie_markdown(t), *_quotes_markdown(t)]


def _banner(cls: str, title: str, text: str) -> str:
    return f'<div class="banner {cls}" role="note"><strong>{_h(title)}</strong> {_h(text)}</div>'


def _header_html(d: Mapping[str, Any]) -> str:
    """Banners, the title block and the run summary: rendered here so they read the same with or without script."""
    meta, case, result = d["meta"], d["case"], d["result"]
    banners = []
    if meta["synthetic"]:
        banners.append('<div class="banner synthetic" role="note"><strong>Synthetic fixture, not biological '
                       "evidence.</strong> Every entity and observation in this run is stipulated to test the "
                       "software. It says nothing about any real variant, gene or trait and never enters biological "
                       "results.</div>")
    if meta["integrity"]:
        banners.append(_banner("warn", "Changed after the run.", "; ".join(meta["integrity"]) + ". This report shows "
                               "the folder as it is now, not necessarily as the run wrote it."))
    if meta["public_export"]:
        banners.append('<div class="banner info" role="note"><strong>Public export.</strong> Verified passages and '
                       "every other long text (observations, rationales, answers, summaries) are cut to "
                       f"{_h(meta['public_export'].get('passage_limit'))} characters, and article text is removed; "
                       "evaluator files are left out.</div>")
    if meta["render_only"]:
        banners.append('<div class="banner info" role="note"><strong>Render-only.</strong> This report was rendered '
                       "later from the saved run folder; nothing was re-run.</div>")
    if meta["hypotheses_note"]:
        banners.append(_banner("info", "Evidence bundle." if meta["evidence_only"] else "No hypotheses.",
                               meta["hypotheses_note"]))
    if meta["manifest_missing"]:
        banners.append('<div class="banner warn" role="note"><strong>No manifest.</strong> The run folder has no '
                       "manifest.json, so its mode, code and settings are not recorded.</div>")
    tags = [f'<span class="tag mode">{_h(meta["mode_label"])}</span>']
    if meta["replay"]["of"]:
        tags.append('<span class="tag mode">Replay</span>')
    if meta["render_only"]:
        tags.append('<span class="tag mode">Render-only</span>')
    if meta["synthetic"]:
        tags.append('<span class="tag s-contradicted">Synthetic fixture</span>')
    compared = bool(d["hypotheses"])                      # a run with hypotheses compared them; code alone has none
    if meta["code_only"]:
        tags.append('<span class="tag mode">Filled by code alone</span>')
    if meta["with_reader"]:
        tags.append('<span class="tag mode">Filled by code; articles read by a model</span>')
    if result and compared:
        tags.append(f'<span class="tag outcome">{_h(result["resolution"]["molecular_label"])}</span>')
        tags.append(f'<span class="tag">Comparison: {_h(result["outcome_label"])}</span>')
    elif result:
        tags.append(f'<span class="tag outcome">{_h(result["outcome_label"])}</span>')
    tags.append(f'<span class="tag">Origin: {_h(case["origin"])}</span>')
    lead = _h(result["summary"]) if result and result["summary"] else (
        "No outcome was recorded." if not result and not meta["evidence_only"] else "")
    rows = [("Variant", _h(case["variant"]["label"]) + f' <span class="small">reference check: '
             f'{_h(case["variant"]["reference_check"])}; {_h(case["variant"]["variant_type"])}</span>'),
            ("Case", _h(case["case_id"])), ("Origin", _h(case["origin"])),
            *((title, _list_html(values, empty, "; ")) for title, values, empty in _case_rows(case)),
            ("Mode", _h(meta["mode_label"]) + (" · render-only" if meta["render_only"] else ""))]
    if result:
        outcome = _h(result["outcome_label"])
        if result["downgraded_label"]:
            outcome += (f' <span class="small">(downgraded from {_h(result["downgraded_label"])}: '
                        f'{_h(result["downgrade_reason"])})</span>')
        resolution = result["resolution"]
        if compared:
            rows += [("Molecular evidence", _h(resolution["molecular_label"]) + ": " +
                      _h(", ".join(resolution["supported_molecular_claim_ids"]) or "none")),
                     ("Chain completeness", _h(resolution["required_link_label"])),
                     ("Whole-hypothesis comparison", outcome), ("Stopped because", _h(_stop_text(result))),
                     ("Leading", _list_html(result["leading_ids"], "none"))]
        else:
            rows += [("Outcome", outcome), ("Stopped because", _h(_stop_text(result)))]
    if d["chain"]["placed"]:
        rows.append(("Mechanism chain", _h(d["chain"]["summary"])))
    rows += [(title, _h(text)) for title, text in _record_rows(d)]
    grid = "".join(f"<dt>{_h(k)}</dt><dd>{v}</dd>" for k, v in rows)
    gaps = "".join(f"<li>{_h(gap['text'])}</li>" for gap in d["gaps"]) or "<li>None recorded.</li>"
    answered = bool(d["chain"]["ranked"]["chains"])       # the ranked chains lead; the run's own summary follows
    return ("".join(banners)
            + f'<header class="hero"><div class="eyebrow">v2m · run report · engine {_h(meta["engine_version"])}</div>'
            f'<h1>{_h(meta["variant"])}</h1><div class="tags">{"".join(tags)}</div>'
            + (f'<p class="lead">{lead}</p>' if lead and not answered else "") + "</header>"
            + _ranked_html(d) + _table_section_html(d)
            + '<section id="summary" aria-labelledby="summary-h"><span class="section-no">01 / RUN SUMMARY</span>'
            '<h2 id="summary-h">Run summary</h2>' + (f"<p>{lead}</p>" if lead and answered else "")
            + f'<dl class="facts">{grid}</dl>{_chain_html(d)}<h3>Major gaps</h3>'
            f'<ul class="gaps">{gaps}</ul></section>')


def _static_html(d: Mapping[str, Any]) -> str:
    """The no-script equivalent: hypotheses, claims, evidence, next steps and the inventory as static tables."""
    claims, evidence = d["claims"], d["evidence"]
    parts = ['<section class="static"><h2>Report tables</h2><p class="muted">Interactive views need script; these '
             "tables hold the same claims, evidence and statuses.</p>"]
    parts.append(_table_html("Hypotheses", ["Hypothesis", "Disposition", "Required claims", "Reason"], [
        [f"{_h(h['id'])} · {_h(h['title'])}", _h(h["disposition_label"]),
         "<br>".join(f"{_h(cid)}: {_h(claims[cid]['status_label'])}" for cid in h["required"]),
         "<br>".join(_h(text) for text in (h["reason"] or h["reason_for_inclusion"], *h["reinstated_notes"],
                                            h["stale_note"]) if text)] for h in d["hypotheses"]]))
    parts.append(_table_html("Claims", ["Claim", "Assertion", "Status", "Supports", "Contradicts", "Context only",
                                        "Hypotheses"], [
        [_h(c["id"]), _h(c["assertion"]), _status_html(c)]
        + [_h(", ".join(_linked(c, stance)) or "–") for stance in ("supports", "contradicts", "context_only")]
        + [_h(", ".join(h["id"] + (" (required)" if h["required"] else "") for h in c["hypotheses"]))]
        for c in claims.values()]))
    shown = [e for e in evidence.values() if e["claims"] or not e["inventory"]]
    parts.append(_table_html("Evidence (the inventory's unlinked groups are in the inventory table)",
                             ["Evidence", "Class", "Observation", "Sources", "Context"], [
        [_h(e["id"]), _h(e["class"] + (" (measured null)" if e["result_kind"] != "effect" else "")),
         _h(e["observed"]), ", ".join(_link_html(s) for s in e["sources"]) or "–",
         _h(e["context"]["text"]) if e["context"] else "–"] for e in shown]))
    nexts = (d["result"] or {}).get("next_experiments") or []
    parts.append("<h3>Next discriminating evidence (suggested, not performed)</h3><ul>"
                 + ("".join(f"<li>{_h(n['text'])}</li>" for n in nexts) or f"<li>{_h(_no_next(d))}</li>")
                 + "</ul>")
    if refused := _refused_questions(d):
        parts.append("<h3>Questions closed without being asked (refused)</h3><ul>"
                     + "".join(f"<li>{_h(text)}</li>" for text in refused) + "</ul>")
    inv = d["inventory"]
    if inv["rows"]:
        rows = [r for r in inv["rows"] if r["passes"]]
        parts.append(f"<details><summary>QBiC-SELEX inventory: {inv['gate_passing']} groups pass the gate "
                     f"(of {inv['groups']})</summary>" + _table_html(
                         "Gate-passing model-sharing groups, in DBD then group order", INVENTORY_HEADERS,
                         [[_h(cell) for cell in _inventory_cells(r)] for r in rows], "inventory") + "</details>")
    return "".join(parts) + "</section>"


def scope_html(graph: ClaimGraph) -> str:
    """Always-visible, script-free scope graph; each arrow is labelled, never mistaken for an evidence edge."""
    views = graph.scope_views()
    groups = "".join(f"<li><b>{_h(f['family_id'])}</b>: {_h(', '.join(f['hypothesis_ids']))}</li>"
                     for f in views["hypothesis_families"])
    edges = "".join(f"<tr><td>{_h(e['child_claim_id'])} → {_h(e['parent_claim_id'])}</td>"
                    f"<td>{_h(e['relation'])}</td><td>{_h(e['basis'])}</td></tr>"
                    for e in views["claim_refinements"])
    return ("<section id='scope-families'><h2>Scope families and claim refinement</h2>"
            "<p>Related hypotheses stay separate. These organisational links transfer no evidence, assessment, "
            "rejection or statistical weight. Unspecified context is not universal context; shared ontology "
            "annotations alone do not prove a population subset.</p><ul>" + groups + "</ul>"
            "<table><thead><tr><th>Claim link</th><th>Relationship</th><th>Basis</th></tr></thead><tbody>"
            + edges + "</tbody></table></section>")


def render_html(bundle: Bundle, *, render_only: bool = False, raw_base: str = "") -> str:
    """report.html: the template with the run's data embedded as escaped JSON, the header and summary, and the
    no-script tables. Placeholders are filled in one pass, so no inserted text is ever read as a placeholder."""
    data = report_data(bundle, render_only=render_only, raw_base=raw_base)
    meta = data["meta"]
    side = f"{meta['case_id']} · {meta['mode_label']}" + (" · SYNTHETIC" if meta["synthetic"] else "")
    parts = {"TITLE": _h(meta["title"]), "SIDEMETA": _h(side), "HEADER": _header_html(data),
             "STATIC": _static_html(data), "DATA": _embed(data), "SCOPES": scope_html(bundle.graph)}
    return PLACEHOLDER.sub(lambda m: parts[m.group(1)], TEMPLATE.read_text(encoding="utf-8"))


# --- Markdown --------------------------------------------------------------------------------------------------------

_MD_SPECIAL = re.compile(r"([\\`*_\[\]|<>])")


def _md(value: Any) -> str:
    """Text for Markdown: one line, markup characters escaped (and <, > as entities), so no retrieved or
    model-written text can become a link, an HTML tag or a table cell break."""
    text = _text(value).replace("&", "&amp;")
    return _MD_SPECIAL.sub(lambda m: {"<": "&lt;", ">": "&gt;"}.get(m.group(1), "\\" + m.group(1)), text)


def _md_link(link: Mapping[str, Any]) -> str:
    return f"[{_md(link['text'])}]({link['url']})" if link.get("url") else _md(link["text"])


def _md_table(headers: list[str], rows: list[list[str]]) -> list[str]:
    return ["| " + " | ".join(headers) + " |", "|" + "---|" * len(headers),
            *("| " + " | ".join(cell or "–" for cell in row) + " |" for row in rows), ""]


def _chain_markdown(d: Mapping[str, Any]) -> list[str]:
    """The mechanism chain as Markdown lines: the same rows, order and gaps as the HTML block."""
    view = d["chain"]
    if not view["placed"]:
        return []
    out = ["## Mechanism chain", "", _md(view["summary"]), "", _md(view["note"]), _md(_chain_ladder(view)), ""]
    out += _md_table(CHAIN_HEADERS, [
        [_md(r["label"]), _md(r["rung_label"] + ("; tied" if r["tied"] else "")),
         "<br>".join(_md(text) for text in r["leading"])
         + (f"<br>and {r['leading_more']} more" if r["leading_more"] else ""), _md(r["others"])]
        for r in chain.chain_rows(view, d["case"]["variant"]["alt"])])
    out += [f"- {_md(m['text'])}" for m in view["missing"]] + ([""] if view["missing"] else [])
    if view["hypotheses"]:
        out += ["Open hypotheses, link by link (their own claims only):", ""]
        out += _md_table(["Hypothesis", "Disposition", *chain.LINK_LABEL.values()],
                         [[_md(cell) for cell in row] for row in chain.hypothesis_rows(view)])
        out += [_md(text) for text in view["order"]["text"]] + [""]
    if view["unplaced"]:
        out += [_md(_chain_unplaced(view)), ""]
    return out


def _ranked_markdown(d: Mapping[str, Any]) -> list[str]:
    """The run's answer as Markdown lines: the same headline, link-by-link table, ranked table and rule as the HTML."""
    view = d["chain"]
    ranked = view["ranked"]
    out = ["## Answer: ranked mechanism chains", ""]
    if not ranked["chains"]:
        return [*out, _md(NO_CHAIN), ""]
    alt = d["case"]["variant"]["alt"]
    out += [f"**{_md(ranked['headline'])}**", ""]
    if tie := _tie_line(d):
        out += [_md(tie), ""]
    if ranked["support"]:
        out += [_md(ranked["support"]), ""]
    if ranked.get("join"):                       # only a run whose first chain a record joins has the line
        out += [f"**Joined.** {_md(ranked['join'])}", ""]
    out += _md_table(chain.STRIP_HEADERS, [[_md(step["label"]), _md(step["names"]), _md(step["evidence"])]
                                           for step in chain.strip_rows(view, alt)])
    out += _md_table(chain.RANKED_HEADERS, [[_md(cell) for cell in row] for row in chain.ranked_rows(view, alt)])
    notes = [text for text in (chain.ranked_more(view), _left_out(ranked), chain.SHARED_NOTE,
                               chain.unclaimed_text(view)) if text]
    out += [_md(" ".join(notes)), ""]
    variant = d["case"]["variant"]
    if factors := chain.factor_rows(view, variant["ref"], alt):
        more = view["factors"]["not_listed"]
        out += ["The transcription factors in these chains: what the lookups returned (shown, never ranked).", ""]
        out += _md_table(chain.FACTOR_HEADERS, [[_md(cell) for cell in row] for row in factors])
        out += [_md(chain.FACTOR_NOTE) + (f" {more} more named factor{'s' if more != 1 else ''} not listed."
                                          if more else ""), ""]
    return [*out, _md(ranked["rule"]), ""]


def render_markdown(bundle: Bundle, *, render_only: bool = False) -> str:
    """report.md: the compact text equivalent (outcome, hypotheses, claims with status and evidence ids, gaps, next
    experiments, evidence, inventory and provenance), from the same view model as the HTML."""
    d = report_data(bundle, render_only=render_only)
    meta, case, result, claims = d["meta"], d["case"], d["result"], d["claims"]
    out = [f"# v2m run report: {_md(meta['variant'])}", ""]
    if meta["synthetic"]:
        out += ["> **Synthetic fixture, not biological evidence.** Every entity and observation here is stipulated to "
                "test the software.", ""]
    if meta["integrity"]:
        out += [f"> **Changed after the run.** {_md('; '.join(meta['integrity']))}.", ""]
    if meta["public_export"]:
        out += [f"> **Public export.** Verified passages and every other long text are cut to "
                f"{_md(meta['public_export'].get('passage_limit'))} characters, and article text is removed.", ""]
    if meta["hypotheses_note"]:
        out += [f"> **{'Evidence bundle.' if meta['evidence_only'] else 'No hypotheses.'}** "
                f"{_md(meta['hypotheses_note'])}", ""]
    out += [f"Case {_md(case['case_id'])} · {_md(meta['mode_label'])}" + (" · render-only" if render_only else "")
            + f" · origin {_md(case['origin'])} · engine {_md(meta['engine_version'])}", ""]
    out += [f"- {title}: {_md('; '.join(values) or empty)}" for title, values, empty in _case_rows(case)] + [""]
    out += _ranked_markdown(d)
    out += _table_markdown(d)
    out += ["## Outcome", ""]
    if result:
        out += [f"**{_md(result['outcome_label'])}**; stopped because {_md(_stop_text(result))}.", ""]
        resolution = result["resolution"]
        if d["hypotheses"]:                    # hypotheses were compared; a fill by code alone has none
            out += [f"**Molecular evidence:** {_md(resolution['molecular_label'])} "
                    f"({_md(', '.join(resolution['supported_molecular_claim_ids']) or 'none')}).",
                    f"**Chain completeness:** {_md(resolution['required_link_label'])}.",
                    _md(resolution["note"]), ""]
        if result["summary"]:
            out += [_md(result["summary"]), ""]
    else:
        out += ["No outcome recorded.", ""]
    if records := _record_rows(d):
        out += [f"- {title}: {_md(text)}" for title, text in records] + [""]
    out += _chain_markdown(d)
    if d["hypotheses"]:
        out += ["## Hypotheses", ""] + _md_table(["Hypothesis", "Disposition", "Required claims", "Weakest link",
                                                   "Reason"], [
            [f"{_md(h['id'])} {_md(h['title'])}", _md(h["disposition_label"]),
             ", ".join(f"{_md(c)} ({_md(claims[c]['status'])})" for c in h["required"]),
             f"{_md(h['weakest']['claim'])}: {_md(h['weakest']['why'])}" if h["weakest"] else "",
             " · ".join(_md(text) for text in (h["reason"] or h["reason_for_inclusion"], *h["reinstated_notes"],
                                               h["stale_note"]) if text)] for h in d["hypotheses"]])
    if claims:
        out += ["## Claims", ""] + _md_table(["Claim", "Assertion", "Status", "Supports", "Contradicts",
                                              "Context only"], [
            [_md(c["id"]), _md(c["assertion"]),
             _md(c["status"] + (f" ({c['basis']})" if c["basis"] else "")
                 + ("; premise failed" if c["flag"] != "none" else "")
                 + (f"; superseded by {c['superseded_by']}" if c["superseded_by"] else ""))]
            + [_md(", ".join(_linked(c, stance))) for stance in ("supports", "contradicts", "context_only")]
            for c in claims.values()])
    out += ["## Gaps", ""] + [f"- {_md(g['text'])}" for g in d["gaps"]] + (["- None recorded."] if not d["gaps"]
                                                                              else []) + [""]
    nexts = (result or {}).get("next_experiments") or []
    out += ["## Next discriminating evidence (suggested, not performed)", ""]
    out += [f"- {_md(n['text'])}" + (f" (distinguishes {_md(', '.join(n['distinguishes']))})"
                                      if n["distinguishes"] else "") for n in nexts] or [f"- {_md(_no_next(d))}"]
    out.append("")
    if refused := _refused_questions(d):
        out += ["## Questions closed without being asked (refused)", ""] + [f"- {_md(t)}" for t in refused] + [""]
    shown = [e for e in d["evidence"].values() if e["claims"] or not e["inventory"]]
    if shown:
        out += ["## Evidence", ""] + _md_table(["Evidence", "Class", "Observation", "Sources"], [
            [_md(e["id"]), _md(e["class"]), _md(e["observed"]), ", ".join(_md_link(s) for s in e["sources"])]
            for e in shown])
    inv = d["inventory"]
    if inv["rows"]:
        out += ["## QBiC-SELEX inventory", "",
                f"{inv['gate_passing']} model-sharing groups pass the gate, of {inv['groups']} with cached scores "
                "(DBD then group order; not ordered by z, expression or ChIP; CIS-BP-mapped models count as the TF's "
                "own).", ""]
        out += _md_table(INVENTORY_HEADERS, [[_md(cell) for cell in _inventory_cells(r)]
                                             for r in inv["rows"] if r["passes"]])
    manifest = d["provenance"]["manifest"]
    git = (manifest.get("code") or {}).get("git") or {}
    model = (d["provenance"]["metrics"].get("model") or {})
    tools = Counter(t["status"] for t in d["tool_calls"])
    out += ["## Provenance", "",
            f"- Engine {_md(meta['engine_version'])}; git {_md(git.get('head') or 'unknown')}"
            + (" (uncommitted changes)" if git.get("dirty") else ""),
            f"- Model calls: {_md(model.get('calls', 'not recorded'))}; cost USD: {_md(model.get('cost_usd', 'n/a'))}",
            "- Tool calls: " + (_md(", ".join(f"{n} {k}" for k, n in sorted(tools.items()))) or "none"),
            f"- Created: {_md(meta['created'] or 'not recorded')}", ""]
    return "\n".join(out)


# --- writing ---------------------------------------------------------------------------------------------------------

def write_reports(run_dir: str | Path, out_dir: str | Path | None = None) -> list[Path]:
    """Write report.html and report.md. By default into the run folder, refused when either exists (never
    overwritten); with out_dir, into that new folder (refused when it exists) as a render-only report whose raw-result
    links point back to the run folder."""
    bundle = load_bundle(run_dir)
    if out_dir is None:
        target, render_only, raw_base = bundle.path, False, ""
        existing = [n for n in ("report.html", "report.md") if (target / n).exists()]
        if existing:
            raise FileExistsError(f"{target} already holds {', '.join(existing)}: reports are never overwritten; "
                                  "render into a new folder instead")
    else:
        target, render_only = Path(out_dir), True
        try:
            target.mkdir(parents=True, exist_ok=False)
        except FileExistsError:
            raise FileExistsError(f"{target} already exists: reports are rendered into a new folder") from None
        raw_base = Path(os.path.relpath(bundle.path.resolve(), target.resolve())).as_posix() + "/"
    paths = [target / "report.html", target / "report.md"]
    write_new(paths[0], render_html(bundle, render_only=render_only, raw_base=raw_base))
    write_new(paths[1], render_markdown(bundle, render_only=render_only))
    return paths
