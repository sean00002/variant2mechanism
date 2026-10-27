"""Gather (code): the fixed tool calls with default arguments, then literature quotes from the summariser."""

import json
import re
from concurrent.futures import ThreadPoolExecutor

from ...context.base import ToolResult, call_tool
from ...context.ccre import ccre_lookup
from ...context.ensembl import nearest_genes, variant_annotation
from ...context.genetics import eqtl_lookup, finemap_lookup, gwas_lookup
from ...context.literature import literature_search
from ..case import BRACKETS, RunState, prompt
from ..ledger import Evidence
from ..schemas import Quotes

WS = re.compile(r"\s+")


def norm(text: str) -> str:
    return WS.sub(" ", text or "").strip()


def disease_terms(disease: str) -> str:
    terms = [t.strip() for t in re.split(r"[,;]", BRACKETS.sub("", disease)) if t.strip()]
    quoted = [f'"{t.lower()}"' for t in terms]
    return quoted[0] if len(quoted) == 1 else "(" + " OR ".join(quoted) + ")"


def top_gene(finemap: ToolResult | None, genes: ToolResult) -> str | None:
    if finemap is not None and finemap.ok and finemap.full.get("best_l2g"):
        return max(finemap.full["best_l2g"].items(), key=lambda kv: kv[1])[0]
    if genes.ok and genes.full:
        return genes.full[0]["gene"]
    return None


def literature_query(state: RunState, gene: str | None) -> str:
    parts = []
    if state.spec.rsid and not state.masked:
        parts.append(state.spec.rsid)
    if gene:
        parts.append(gene)
    parts.append(disease_terms(state.spec.disease))
    return " AND ".join(parts)


def quotes_for(state: RunState, stage: str, search: Evidence, papers: list[dict], query: str) -> list[Evidence]:
    """Summariser picks at most 2 verbatim sentences per abstract; code keeps exact substrings only."""
    with_abs = [p for p in papers if p.get("abstract")]
    if not with_abs:
        return []
    block = "\n\n".join(f"PMID {p['pmid']}\nTitle: {p['title']}\nAbstract: {p['abstract']}" for p in with_abs)
    res = state.llm.call("summariser", f"{stage}.quotes", prompt("summariser_system"),
                         [{"role": "user", "content": prompt("summarise").format(query=state.mask(query),
                                                                                  abstracts=block)}],
                         output_model=Quotes)
    by_pmid = {p["pmid"]: norm(p["abstract"]) for p in with_abs}
    kept, per = [], {}
    for q in res.parsed.quotes:
        sentence = norm(q.sentence)
        if q.pmid not in by_pmid or not sentence or sentence not in by_pmid[q.pmid]:
            state.flag("quote_rejected", f"PMID {q.pmid}: not an exact substring of the abstract")
            continue
        if per.get(q.pmid, 0) >= 2:
            continue
        per[q.pmid] = per.get(q.pmid, 0) + 1
        url = f"https://europepmc.org/article/MED/{q.pmid}"
        kept.append(state.ledger.add_quote(stage, search, q.pmid, sentence, url))
    return kept


def add_literature(state: RunState, stage: str, result: ToolResult, query: str) -> tuple[Evidence, list[Evidence]]:
    ev = state.ledger.add_evidence(stage, result)
    quotes = quotes_for(state, stage, ev, result.full, query) if result.ok else []
    return ev, quotes


def gather(state: RunState) -> None:
    case = state.tool_case
    germline = state.spec.origin != "somatic"
    with ThreadPoolExecutor(max_workers=5) as pool:
        futs = {"variant_annotation": pool.submit(call_tool, variant_annotation, case),
                "nearest_genes": pool.submit(call_tool, nearest_genes, case),
                "ccre_lookup": pool.submit(call_tool, ccre_lookup, case)}
        va = futs["variant_annotation"].result()
        if germline and not case.rsid and va.ok:          # coordinates given: take the rsID from VEP
            rs = [c["id"] for c in va.full[0].get("colocated_variants", []) if str(c.get("id", "")).startswith("rs")]
            case.rsid = rs[0] if rs else None
        if germline:
            futs["gwas_lookup"] = pool.submit(call_tool, gwas_lookup, case)
            futs["finemap_lookup"] = pool.submit(call_tool, finemap_lookup, case)
            futs["eqtl_lookup"] = pool.submit(call_tool, eqtl_lookup, case)      # GTEx, all tissues (spec 3, 3.4)
        results = {k: f.result() for k, f in futs.items()}
    occupancy_rows = add_occupancy(state, results["ccre_lookup"])
    gene = top_gene(results.get("finemap_lookup"), results["nearest_genes"])
    query = literature_query(state, gene)
    lit = call_tool(literature_search, case, query, masked=state.masked)
    if lit.ok and not lit.full and state.spec.rsid and not state.masked:
        state.flag("literature_fallback", f"no hits for '{query}'; dropped the rsID")
        query = " AND ".join(x for x in [gene, disease_terms(state.spec.disease)] if x)
        lit = call_tool(literature_search, case, query, masked=state.masked)
    order = ["variant_annotation", "nearest_genes", "ccre_lookup", "occupancy", "gwas_lookup", "finemap_lookup",
             "eqtl_lookup"]
    for name in order:                                        # fixed order, whatever finished first
        if name == "occupancy":
            for res in occupancy_rows:
                state.ledger.add_evidence("gather", res)
        elif name in results:
            note_retries(state, results[name])
            state.ledger.add_evidence("gather", results[name])
    note_retries(state, lit)
    add_literature(state, "gather", lit, query)
    state.ledger.log("gather", "done", {"top_gene": gene, "literature_query": state.mask(query),
                                        "tools": order + ["literature_search"]})


def add_occupancy(state: RunState, ccre: ToolResult) -> list[ToolResult]:
    """Occupancy in code (spec 3, section 1), for no_qbic and full: the element line and one row per bound TF."""
    from ...context.occupancy import occupancy_results
    from ...qbic.expression import get_expression
    from ...qbic.registry import get_registry
    local = (ccre.full or {}).get("local") if isinstance(ccre.full, dict) else None
    ccre_class = local["class"] if local and local.get("distance") == 0 else None
    occ, rows = occupancy_results(state.tool_case, get_registry(), get_expression(), ccre_class,
                                  float(state.llm.cfg["screen"]["min_tpm"]))
    state.occupancy = occ
    return rows


def note_retries(state: RunState, res: ToolResult) -> None:
    if res.attempts > 1:
        state.flag("tool_retried", f"{res.tool}: {'succeeded' if res.ok else 'still failing'} on attempt {res.attempts}")


def tool_result_text(ev: Evidence, quotes: list[Evidence], mask) -> str:
    text = f"{ev.id}: {ev.summary}"
    for q in quotes:
        text += f'\n{q.id} (PMID {q.pmid}): "{q.quote}"'
    return mask(text)


def dumps(obj) -> str:
    return json.dumps(obj, separators=(",", ":"), default=str)
