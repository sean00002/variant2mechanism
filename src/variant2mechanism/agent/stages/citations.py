"""Citation check and rank (code; spec 2, 8.7 and 8.8)."""

import json

from ..case import RunState
from .gather import norm

QBIC_TOOLS = {"qbic_screen", "qbic_tf_detail"}
REGISTRY_TO_COVERAGE = {"tf": "own_model", "mapped": "mapped", "not_in_coverage": "not_in_coverage"}


def evidence_checks(state: RunState) -> dict[str, tuple[bool, str]]:
    """For every evidence row: does it pass (exists, tool succeeded, quote is an exact substring of its abstract)?"""
    out = {}
    for e in state.ledger.evidence():
        if e.quote is not None:
            try:
                papers = json.loads((state.run_dir / e.full_path).read_text())
                abstract = next((p["abstract"] for p in papers if p["pmid"] == e.pmid), "")
            except (OSError, ValueError):
                abstract = ""
            ok = norm(e.quote) in norm(abstract)
            out[e.id] = (ok, "" if ok else "quote is not an exact substring of its saved abstract")
        else:
            out[e.id] = (e.ok, "" if e.ok else "the tool call failed")
    return out


def borrows_binding(ev, symbol: str | None) -> bool:
    """Evidence that is another TF's binding change: any screen row, or a qbic_tf_detail lookup of a different TF.
    A lookup of the chain's own TF (which reports it is not in coverage) is honest, not borrowed."""
    if ev is None or ev.tool not in QBIC_TOOLS:
        return False
    if ev.tool == "qbic_tf_detail":
        name = (ev.args or {}).get("tf")
        looked_up = resolve_coverage(name)[1] if name else None
        return looked_up != symbol
    return True


def resolve_coverage(tf: str | None):
    from ...qbic.registry import get_registry
    if not tf:
        return None, None
    r = get_registry().resolve_tf(tf)
    if r["status"] != "ok":
        return r["status"], None
    return REGISTRY_TO_COVERAGE[get_registry().coverage(r["symbol"])["status"]], r["symbol"]


def citation_check(state: RunState) -> dict:
    """Final link statuses, coverage status per chain, flags, and citation_support."""
    hyps = state.revised.hypotheses
    grades = {(g.hypothesis_id, g.step): g for g in state.grades1}
    checks = evidence_checks(state)
    statuses, n_links, n_good = {}, 0, 0
    evidence = {e.id: e for e in state.ledger.evidence()}
    coverage = {}
    for h in hyps:
        cov, symbol = resolve_coverage(h.tf) if not h.is_null else (None, None)
        coverage[h.id] = {"coverage_status": cov, "resolved_symbol": symbol}
        if not h.is_null and cov is not None:
            if cov == "not_in_coverage":
                binding = next((lk for lk in h.links if lk.step == "binding"), None)
                borrowed = [i for i in (binding.evidence_ids if binding else []) if borrows_binding(evidence.get(i), symbol)]
                if borrowed:
                    state.flag("coverage_violation", f"{h.id}: {h.tf} is not in QBiC-SELEX coverage but its binding "
                                                     f"link cites another TF's QBiC-SELEX binding change ({borrowed})")
        for link in h.links:
            n_links += 1
            g = grades.get((h.id, link.step))
            status = g.status if g else "missing"
            unknown = [i for i in link.evidence_ids if i not in checks]
            failed = [i for i in link.evidence_ids if i in checks and not checks[i][0]]
            if unknown:
                state.flag("unknown_evidence_id", f"{h.id}.{link.step} cites {unknown}, not in this run's ledger")
            if not link.evidence_ids:
                if status != "missing":
                    state.flag("no_citation", f"{h.id}.{link.step}: cites nothing; {status} -> missing")
                status = "missing"
            elif (unknown or failed) and status == "supported":
                state.flag("failed_citation", f"{h.id}.{link.step}: cited {unknown + failed} failed a check; "
                                              "supported -> weak")
                status = "weak"
            if link.evidence_ids and not unknown and not failed:
                n_good += 1
            statuses[(h.id, link.step)] = status
    support = (n_good / n_links) if (n_links and state.config != "single") else None
    return {"statuses": statuses, "coverage": coverage, "citation_support": support}


def rank(state: RunState, statuses: dict) -> list:
    hyps = state.revised.hypotheses
    total = sum(h.probability for h in hyps) or 1.0
    for h in hyps:
        h.probability = h.probability / total

    def supported(h):
        return sum(statuses.get((h.id, lk.step)) == "supported" for lk in h.links)

    return sorted(hyps, key=lambda h: (-round(h.probability, 9), -supported(h)))
