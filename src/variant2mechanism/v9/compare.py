"""Comparison profiles, validation of the critic's comparisons, and the run outcome (SPEC 7, 13.9).

Why: the final judgement is the critic's, but code checks it and can only weaken it, so a persuasive comparison can
never turn thin evidence into an explanation, and missing data can never decide between hypotheses.
- `profile` lays a hypothesis's evidence out claim by claim (assessment, display status and basis, applicability,
  independent support, contradictions, critical gaps, proxy use, claims shared with or divergent from each rival),
  with no score: incomparable kinds of evidence are never added up.
- `validate` refuses a comparison whose ids are unknown, which compares a hypothesis with itself or with a superseded
  one, whose decisive claims belong to neither hypothesis, which prefers a hypothesis with a contradicted or contested
  required claim, or which prefers one without a decisive claim that only one of the two has (a shared claim cannot
  separate them).
- `decide` sets the RunResult and the leading/tied dispositions (role "code", the only role allowed to). A required
  claim is settled when it is supported in scope, live, and its premise and path in the hypothesis are intact. The
  checks only weaken, and code never names a leader the critic did not name:
  - leading_explanation: the critic's leader is active, has no contradicted or contested required claim, has a
    required claim supported beyond annotation, every required claim is settled, and an accepted comparison prefers it
    over every other viable active hypothesis (an untested rival is not beaten by default);
  - partial_mechanism: the same, except that only the molecular required claims must be settled: an unsettled bridge
    (BRIDGE_RELATIONS: from the molecular event to a target, process or trait) is what makes it partial;
  - multiple_explanations: the critic's tie among viable named hypotheses, at least one of which explains; a named
    hypothesis that is merely unresolved stays in the tie, and a lead that no accepted comparison separates from its
    viable rivals becomes a tie with them;
  - no_supported_explanation: every hypothesis rejected, or no viable hypothesis explains (molecular claims settled
    and support beyond annotation).
  When the critic's leader or tie fails these checks, the outcome is what the graph alone shows, naming nobody.
- Without a final comparison (a budget stop, a failed critic call, nothing active) the outcome comes from the graph
  alone and names no hypothesis, because leading and tied are set only by a comparison: partial_mechanism when the
  single viable hypothesis explains, multiple_explanations when several are viable and one explains,
  no_supported_explanation otherwise. A graph with no hypothesis at all, or a run stopped by an engine error or a
  replay miss, is input_or_capability_limitation: nothing scientific was assessed.
- A rejection rests on a contradicted required claim. When that contradiction is withdrawn (a misread passage
  relinked as context only, a re-assessment), the engine reinstates the hypothesis as deferred, once
  (graph.reinstate), and the result names it; a rejection that no longer stands but stays rejected (a second
  rejection, one code did not make) is disclosed instead, so neither passes as a refutation.
"""

from collections.abc import Sequence
from typing import Any

from .graph import ClaimGraph, GraphRefusal
from .roles import V9Final, sort_ids
from .schemas import NextExperiment, Outcome, PairComparison, RunResult, StopReason, WeakLink

# Links from the molecular event to a target gene, a process or a trait: while one of these is unsettled but the
# molecular links hold, a mechanism is partial. SPEC 7 names regulates, contributes_to_trait and affects_process; the
# association and locus-level links reach the same targets and traits, so a missing GWAS or eQTL record leaves a
# mechanism partial instead of unsupported.
BRIDGE_RELATIONS = frozenset({"regulates", "associated_with_expression", "affects_process", "associated_with_trait",
                              "causal_at_locus", "contributes_to_trait"})
LOCATION_RELATIONS = frozenset({"overlaps"})          # where a variant lies is not a mechanism
LIMITATION_STOPS = frozenset({"engine_error", "cache_miss"})   # the run could not assess (or reproduce) anything
# How much an outcome claims; code may keep or lower it, never raise it (tests hold decide() to this).
STRENGTH: dict[str, int] = {"leading_explanation": 3, "partial_mechanism": 2, "multiple_explanations": 2,
                            "no_supported_explanation": 1, "input_or_capability_limitation": 1}


# --- reading a hypothesis ------------------------------------------------------------------------------------------------

def settled(graph: ClaimGraph, claim_id: str, hid: str | None = None) -> bool:
    """Supported in scope, live and with no failed premise; within a hypothesis, also an intact path (a required claim
    that was superseded and never swapped for its replacement is not settled there)."""
    c = graph.claims[claim_id]
    if c.assessment != "supported_in_scope" or c.superseded_by is not None or c.dependency_flag != "none":
        return False
    return hid is None or graph.hypotheses[hid].path_status.get(claim_id, "intact") == "intact"


def beyond_annotation(graph: ClaimGraph, claim_id: str) -> bool:
    """Supported in scope by more than an annotation: an overlap claim, or support whose basis is annotation, places
    the variant but shows no mechanism."""
    c = graph.claims[claim_id]
    if c.assessment != "supported_in_scope" or c.superseded_by or c.relation in LOCATION_RELATIONS:
        return False
    return graph.display(claim_id).basis not in (None, "annotation")


def blocking(graph: ClaimGraph, hid: str) -> list[str]:
    """Required claims that stop a hypothesis from being preferred: contradicted or contested in scope."""
    return [c for c in graph.hypotheses[hid].required_claim_ids
            if graph.claims[c].assessment in ("contradicted_in_scope", "contested")]


def viable(graph: ClaimGraph, hid: str) -> bool:
    return graph.hypotheses[hid].disposition == "active" and not blocking(graph, hid)


def has_support(graph: ClaimGraph, hid: str) -> bool:
    return any(beyond_annotation(graph, c) for c in graph.hypotheses[hid].required_claim_ids)


def unsettled(graph: ClaimGraph, hid: str, *, bridges: bool) -> list[str]:
    """Required claims of a hypothesis that are not settled in it: all of them, or only the molecular ones."""
    return [c for c in graph.hypotheses[hid].required_claim_ids
            if not settled(graph, c, hid) and (bridges or graph.claims[c].relation not in BRIDGE_RELATIONS)]


def explains(graph: ClaimGraph, hid: str) -> bool:
    """At least a partial mechanism: viable, every molecular required claim settled, and a required claim supported
    beyond annotation."""
    return viable(graph, hid) and has_support(graph, hid) and not unsettled(graph, hid, bridges=False)


def complete(graph: ClaimGraph, hid: str) -> bool:
    """Explains, with every required claim settled (bridges included)."""
    return explains(graph, hid) and not unsettled(graph, hid, bridges=True)


def stale_rejections(graph: ClaimGraph) -> list[str]:
    """Rejected hypotheses none of whose required claims is contradicted in scope any more (the passage behind the
    contradiction was found misread, or the claim was re-assessed). The engine reinstates those it can
    (graph.reinstate: a code rejection, once); what this returns after that stays rejected and is disclosed."""
    return [hid for hid in sort_ids(graph.hypotheses) if graph.hypotheses[hid].disposition == "rejected"
            and not any(graph.claims[c].assessment == "contradicted_in_scope"
                        for c in graph.hypotheses[hid].required_claim_ids)]


def reinstated(graph: ClaimGraph) -> list[str]:
    """Hypotheses code reinstated (graph.reinstate): rejected for a contradicted required claim whose contradiction
    was later withdrawn, and returned to deferred once (their history holds a "reinstatement" entry), whatever their
    disposition now."""
    return [hid for hid in sort_ids(graph.hypotheses)
            if any(x.get("kind") == "reinstatement" for x in graph.hypotheses[hid].history)]


def _reinstatement_text(graph: ClaimGraph, hid: str) -> str:
    entry = next(x for x in reversed(graph.hypotheses[hid].history) if x.get("kind") == "reinstatement")
    claims = ", ".join(str(c) for c in entry.get("claims") or []) or "a required claim"
    return f"{hid} ({claims} no longer contradicted in scope; now {graph.hypotheses[hid].disposition})"


def weak_links(graph: ClaimGraph, hid: str) -> list[WeakLink]:
    """Every required claim of the hypothesis that is not settled in it, with why."""
    out = []
    h = graph.hypotheses[hid]
    for cid in h.required_claim_ids:
        c = graph.claims[cid]
        if c.superseded_by:
            why = f"superseded by {c.superseded_by}, which this hypothesis does not use"
        elif c.assessment != "supported_in_scope":
            d = graph.display(cid)
            basis = f"; support so far is {d.status} ({d.basis})" if d.basis else ""
            why = f"{c.relation} claim is {c.assessment}{basis}"
        elif c.dependency_flag != "none":
            why = f"supported, but a premise ({', '.join(c.dependencies)}) failed"
        elif h.path_status.get(cid, "intact") != "intact":
            why = f"supported, but its path in {hid} is {h.path_status[cid]}"
        else:
            continue
        out.append(WeakLink(hypothesis_id=hid, claim_id=cid, why=why))
    return out


def profile(graph: ClaimGraph, hid: str) -> dict[str, Any]:
    """The evidence profile of one hypothesis (JSON-native), for the critic's final packet and the report."""
    h = graph.hypotheses[hid]
    claims = []
    for cid in h.claim_ids:
        c = graph.claims[cid]
        d = graph.display(cid)
        usable = [x for x in c.evidence_links if x.stance in ("supports", "contradicts")]
        supports = [x for x in usable if x.stance == "supports"]
        groups = {graph.evidence[x.evidence_id].independence_group for x in supports
                  if x.applicability in ("exact", "proxy")}
        claims.append({
            "claim_id": cid, "required": cid in h.required_claim_ids, "relation": c.relation,
            "bridge": c.relation in BRIDGE_RELATIONS, "direction": c.direction, "effect_allele": c.effect_allele,
            "assessment": c.assessment, "settled": settled(graph, cid, hid), "display": d.status, "basis": d.basis,
            "dependency_flag": c.dependency_flag, "path_status": h.path_status.get(cid, "intact"),
            "superseded_by": c.superseded_by, "supports": [x.evidence_id for x in supports],
            "contradicts": [x.evidence_id for x in usable if x.stance == "contradicts"],
            "applicability": sorted({x.applicability for x in usable}),
            "independent_support": len(groups),
            "proxy": any(x.applicability == "proxy" for x in usable)})
    rivals = [o for o, x in graph.hypotheses.items() if o != hid and x.disposition in ("active", "leading", "tied")]
    return {
        "hypothesis_id": hid, "version": h.version, "disposition": h.disposition, "title": h.title,
        "mechanism_class": h.mechanism_class, "endpoint": h.endpoint, "claims": claims,
        "critical_gaps": [w.claim_id for w in weak_links(graph, hid)],
        "contradictions": [c["claim_id"] for c in claims if c["contradicts"]],
        "blocking": blocking(graph, hid), "supported_beyond_annotation": has_support(graph, hid),
        "molecular_claims_settled": not unsettled(graph, hid, bridges=False),
        "required_claims_settled": not unsettled(graph, hid, bridges=True),
        "proxy_use": any(c["proxy"] for c in claims),
        "shared": {o: sort_ids(set(h.claim_ids) & set(graph.hypotheses[o].claim_ids)) for o in sort_ids(rivals)},
        "divergent": {o: sort_ids(set(h.required_claim_ids) - set(graph.hypotheses[o].claim_ids))
                      for o in sort_ids(rivals)}}


# --- comparisons ---------------------------------------------------------------------------------------------------------

def validate(graph: ClaimGraph, final: V9Final) -> list[PairComparison]:
    """Each of the critic's comparisons, accepted or refused with the reason (not stored here)."""
    out = []
    for c in final.comparisons:
        problems = [f"unknown hypothesis {x}" for x in (c.a, c.b) if x not in graph.hypotheses]
        if c.a == c.b:
            problems.append("a hypothesis cannot be compared with itself")
        if not problems:
            ha, hb = graph.hypotheses[c.a], graph.hypotheses[c.b]
            problems += [f"{x.hypothesis_id} is superseded; compare its replacement" for x in (ha, hb)
                         if x.disposition == "superseded"]
            stray = [x for x in c.decisive_claim_ids if x not in set(ha.claim_ids) | set(hb.claim_ids)]
            if stray:
                problems.append(f"decisive claim(s) {', '.join(stray)} belong to neither {c.a} nor {c.b}")
            preferred = c.a if c.outcome == "A_preferred" else c.b if c.outcome == "B_preferred" else None
            if preferred and (bad := blocking(graph, preferred)):
                problems.append(f"{preferred} cannot be preferred: its required claim(s) {', '.join(bad)} are "
                                "contradicted or contested in scope")
            divergent = set(ha.claim_ids) ^ set(hb.claim_ids)
            if preferred and not divergent & set(c.decisive_claim_ids):
                problems.append(f"preferring {preferred} needs a decisive claim that only one of {c.a} and {c.b} "
                                "has: a shared claim cannot separate them")
        out.append(PairComparison(a=c.a, b=c.b, outcome=c.outcome, decisive_claim_ids=list(c.decisive_claim_ids),
                                  decisive_gaps=list(c.decisive_gaps), reason=c.reason, accepted=not problems,
                                  refusal_reason="; ".join(problems)))
    return out


def preferred(leader: str, rival: str, comparisons: Sequence[PairComparison]) -> bool:
    """Whether an accepted comparison prefers `leader` over `rival`."""
    return any(p.accepted and ((p.a, p.b, p.outcome) == (leader, rival, "A_preferred")
                               or (p.a, p.b, p.outcome) == (rival, leader, "B_preferred")) for p in comparisons)


def _record(graph: ClaimGraph, final: V9Final) -> list[PairComparison]:
    """Store every comparison the graph can hold (accepted or refused); log the ones it cannot (unknown ids)."""
    stored = []
    for p in validate(graph, final):
        try:
            stored.append(graph.comparisons[graph.add_comparison(p, "critic")])
        except GraphRefusal as r:
            graph.log("compare", "critic", f"comparison {p.a} vs {p.b} refused: {p.refusal_reason or r.reason}",
                      details={"accepted": False, "refusal_reason": p.refusal_reason or r.reason})
    return stored


# --- the outcome -----------------------------------------------------------------------------------------------------------

def _graph_outcome(graph: ClaimGraph, candidates: Sequence[str]) -> Outcome:
    """The outcome the graph alone supports, naming no hypothesis (only a comparison names one)."""
    if not graph.hypotheses:
        return "input_or_capability_limitation"
    if not any(explains(graph, h) for h in candidates):
        return "no_supported_explanation"
    return "partial_mechanism" if len(candidates) == 1 else "multiple_explanations"


def _lead_problem(graph: ClaimGraph, leader: str | None) -> str | None:
    """Why the critic's leader cannot lead (even partially), or None."""
    if leader is None:
        return "no leader was named"
    h = graph.hypotheses[leader]
    if h.disposition != "active":
        return f"{leader} is {h.disposition}"
    if bad := blocking(graph, leader):
        return f"{leader} has a contradicted or contested required claim ({', '.join(bad)})"
    if gaps := unsettled(graph, leader, bridges=False):
        return f"{leader}'s molecular required claim(s) {', '.join(gaps)} are not settled in scope"
    if not has_support(graph, leader):
        return f"{leader} has no required claim supported beyond annotation"
    return None


def _check(graph: ClaimGraph, final: V9Final, candidates: list[str],
           comparisons: Sequence[PairComparison]) -> tuple[Outcome, list[str], list[str]]:
    """The critic's proposed outcome after code's checks: (category, named hypotheses, reasons for each change)."""
    category = final.outcome.category
    named = [h for h in dict.fromkeys(final.outcome.leading_ids) if h in graph.hypotheses]
    if category in ("no_supported_explanation", "input_or_capability_limitation"):
        return category, [], []
    if not any(explains(graph, h) for h in candidates):
        viable_text = "; ".join(_state(graph, h) for h in candidates) or "none is active"
        return "no_supported_explanation", [], [
            "no viable hypothesis has its molecular claims settled and a required claim supported beyond annotation "
            f"(viable: {viable_text})"]
    if category in ("leading_explanation", "partial_mechanism"):
        leader = named[0] if named else None
        if problem := _lead_problem(graph, leader):
            return _graph_outcome(graph, candidates), [], [f"{problem}; code names no other hypothesis in its place"]
        unbeaten = [r for r in candidates if r != leader and not preferred(leader, r, comparisons)]
        if unbeaten:
            return "multiple_explanations", [leader, *unbeaten], [
                f"{leader} is not preferred over {', '.join(unbeaten)} by an accepted comparison"]
        if category == "leading_explanation" and (gaps := unsettled(graph, leader, bridges=True)):
            return "partial_mechanism", [leader], [f"required bridge claim(s) {', '.join(gaps)} of {leader} are not "
                                                   "settled in scope"]
        return category, [leader], []
    kept = [h for h in named if h in candidates]
    reasons = [f"{h} is not an active hypothesis free of contradicted or contested required claims"
               for h in named if h not in candidates]
    if len(kept) >= 2 and any(explains(graph, h) for h in kept):
        return category, kept, reasons
    return _graph_outcome(graph, candidates), [], reasons + [
        "a tie needs two viable named hypotheses, one of which explains; code names no hypothesis in its place"]


def _state(graph: ClaimGraph, hid: str) -> str:
    if complete(graph, hid):
        return f"{hid} (every required claim settled)"
    gaps = unsettled(graph, hid, bridges=True)
    if explains(graph, hid):
        return f"{hid} (molecular claims settled; open: {', '.join(gaps)})"
    return f"{hid} (open: {', '.join(gaps) or 'no required claim supported beyond annotation'})"


def _code_summary(graph: ClaimGraph, category: str, candidates: Sequence[str], lead: str) -> str:
    counts: dict[str, int] = {}
    for h in graph.hypotheses.values():
        counts[h.disposition] = counts.get(h.disposition, 0) + 1
    tally = ", ".join(f"{n} {d}" for d, n in sorted(counts.items())) or "no hypothesis"
    viable_text = "; ".join(_state(graph, h) for h in candidates) or "none"
    return (f"{lead}: {category}. No comparison names a hypothesis leading or tied. Viable active hypotheses: "
            f"{viable_text}. Hypotheses: {tally}.")


def decide(graph: ClaimGraph, final: V9Final | None, *, stop_reason: StopReason, budget_stop: bool,
           note: str = "") -> RunResult:
    """Validate and store the critic's comparisons, check its outcome (or decide from the graph alone when `final`
    is None), set leading/tied dispositions as code, and record the RunResult."""
    comparisons = _record(graph, final) if final is not None else []
    candidates = sort_ids(h for h in graph.hypotheses if viable(graph, h))
    proposed: Outcome | None = None
    reasons: list[str] = []
    named: list[str] = []
    if stop_reason in LIMITATION_STOPS:
        category: Outcome = "input_or_capability_limitation"
        summary = _code_summary(graph, category, candidates,
                                f"No scientific outcome ({note or stop_reason}); the run could not assess the case")
    elif final is None:
        category = _graph_outcome(graph, candidates)
        summary = _code_summary(graph, category, candidates,
                                f"Outcome from the graph alone ({note or 'no final comparison'})")
    else:
        proposed = final.outcome.category
        category, named, reasons = _check(graph, final, candidates, comparisons)
        summary = final.outcome.summary
        if category != proposed or reasons:
            change = f"{category} instead of {proposed}" if category != proposed else category
            summary = f"{summary} [Code check: {change}: {'; '.join(reasons)}]".strip()
    if named and category in ("leading_explanation", "partial_mechanism", "multiple_explanations"):
        disposition = "tied" if category == "multiple_explanations" else "leading"
        why = f"{category} (critic comparison checked by code)"
        for hid in named:
            try:
                graph.set_disposition(hid, disposition, why, "code")
            except GraphRefusal as r:
                graph.log("decide", "code", f"{hid} not set {disposition}: {r.reason}", target_ids=[hid])
    if back := reinstated(graph):           # after the dispositions above, so each is named as it ends
        summary += (" Reinstated by code as deferred, because the contradiction that rejected each was withdrawn (a "
                    "reinstatement is not support): " + "; ".join(_reinstatement_text(graph, h) for h in back) + ".")
    if stale := stale_rejections(graph):
        summary += (f" Rejection(s) that no longer stand: {', '.join(stale)} (no required claim is contradicted in "
                    "scope now; they stay rejected in the graph, so they were not compared).")
    weakest = [w for hid in (named or candidates) for w in weak_links(graph, hid)]
    if final is not None:
        have = {(w.hypothesis_id, w.claim_id) for w in weakest}
        weakest += [WeakLink(hypothesis_id=w.hypothesis_id, claim_id=w.claim_id, why=w.why)
                    for w in final.outcome.weakest_links
                    if (w.hypothesis_id, w.claim_id) not in have and w.hypothesis_id in graph.hypotheses
                    and w.claim_id in graph.hypotheses[w.hypothesis_id].claim_ids]
    experiments = [] if final is None else [
        NextExperiment(text=x.text, distinguishes=[h for h in x.distinguishes if h in graph.hypotheses],
                       claim_ids=[c for c in x.claim_ids if c in graph.claims])
        for x in final.outcome.next_experiments]
    open_questions = [f"{q}: {graph.questions[q].text}" for q in sort_ids(graph.questions)
                      if graph.questions[q].status in ("open", "deferred")]
    changed = proposed is not None and category != proposed
    result = RunResult(outcome=category, budget_stop=budget_stop, stop_reason=stop_reason, leading_ids=named,
                       summary=summary, weakest_links=weakest, next_experiments=experiments,
                       uninvestigated_questions=open_questions,
                       downgraded_from=proposed if changed else None,
                       downgrade_reason="; ".join(reasons) if changed else "")
    graph.set_result(result, "code")
    return result
