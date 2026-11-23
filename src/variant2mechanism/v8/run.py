"""One v8 run (design: agent-lab/v8-plan-draft.md).

Code gathers the evidence, infers the context when asked, and screens TF families; the generator writes one chain per
top family (one TF each, no probabilities, no null chain); the critic reviews the chains once; at most one round of
the critic's lookups follows, then one regrade; code assigns each link a tier from the data, eliminates on strong
contradictions only, ranks, and gives the verdict. `code_only` replaces both models with code (the baseline); arm
`single` is the memory test: the generator alone, with no tools and no evidence.
"""

import dataclasses
import hashlib
import json
import logging
import time
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass, field
from pathlib import Path

from ..agent.case import CaseSpec
from ..agent.ledger import Ledger, render_evidence
from ..agent.llm import LLMClient
from ..agent.schemas import Comparison
from ..agent.stages.critique import keep_checks, tool_list, validate_check
from ..agent.stages.gather import add_literature, disease_terms, note_retries, top_gene
from ..agent.stages.investigate import call_key, outcome, run_tool
from ..agent.stages.screen import RunStopped
from ..config import Config, load_config
from ..context.base import Case, ToolResult, call_tool
from ..context.ccre import ccre_lookup
from ..context.ensembl import nearest_genes, variant_annotation
from ..context.genetics import eqtl_lookup, finemap_lookup, gwas_lookup
from ..context.http import Http
from ..context.literature import mask_rsids
from ..context.occupancy import fetch as fetch_occupancy
from ..qbic.expression import ContextError, get_expression
from ..qbic.registry import get_registry
from ..qbic.screen import ScreenSettings, gate
from . import screendb
from .chipgrade import REMAP, fetch_chip
from .families import family_line, family_screen
from .intake import depmap_models, disease_line, here_names, infer_context, promoter_check
from .pubtator import chain_tags, pubtator_search
from .schemas import ChainsV8, ChainV8, CritiqueV8, LinkV8, SingleOut, check_chains, check_cited, check_critique
from .sitescore import site_score
from .tiers import NAMES, Facts, chain_tiers, code_eliminations, gene_tier, minimum, rank, verdict

log = logging.getLogger(__name__)
PROMPTS = Path(__file__).parent / "prompts"
ARMS = ("full", "no_qbic", "single")
# The memory test's prompts: "memory" invites the model's own knowledge; "rules" is the first version, under the v8
# generator's rules ("only the evidence you are given"), which measures willingness to answer rather than memory.
SINGLE_PROMPTS = {"memory": ("memory_system", "memory"), "rules": ("generator_system", "single")}
LINEAGE_TISSUE = {"bowel": "colon", "colorectal": "colon", "breast": "breast", "prostate": "prostate",
                  "liver": "liver", "nervous": "nerve", "brain": "brain", "cns": "brain", "lung": "lung",
                  "skin": "skin", "kidney": "kidney", "pancrea": "pancreas", "esophag": "esophagus",
                  "stomach": "stomach", "myeloid": "blood", "lymphoid": "blood", "bone": "bone"}


def prompt8(name: str) -> str:
    return (PROMPTS / f"{name}.txt").read_text().strip()


def chains_json(chains) -> str:
    return "[\n" + ",\n".join(c.model_dump_json() for c in chains) + "\n]"


@dataclass
class State8:
    spec: CaseSpec
    arm: str
    masked: bool
    run_dir: Path
    ledger: Ledger
    llm: object | None
    tool_case: Case
    qbic: object | None
    cfg: Config
    infer: bool = False
    drop: set = field(default_factory=set)
    before: str | None = None
    context: dict = field(default_factory=dict)
    facts: Facts | None = None
    screen: dict | None = None
    fam_ev: dict = field(default_factory=dict)
    papers: list = field(default_factory=list)
    chains: list = field(default_factory=list)
    grades0: list = field(default_factory=list)
    grades1: list = field(default_factory=list)
    problems: list = field(default_factory=list)
    critic_elims: list = field(default_factory=list)
    checks: list = field(default_factory=list)
    lookups: list = field(default_factory=list)
    next_experiment: str = ""
    tiers: dict = field(default_factory=dict)
    mins: dict = field(default_factory=dict)
    eliminated: dict = field(default_factory=dict)
    rejected_elims: list = field(default_factory=list)
    ranked: list = field(default_factory=list)
    verdict: dict | None = None
    flags: list = field(default_factory=list)
    gene_choice: dict = field(default_factory=dict)

    @property
    def config(self) -> str:                 # what the v7 investigate tools call the configuration
        return "full" if self.arm == "full" else "no_qbic"

    def mask(self, text: str) -> str:
        return mask_rsids(text) if self.masked else text

    def user_message(self, instruction: str, with_evidence: bool = True) -> list[dict]:
        first = self.spec.header(self.masked)
        self.evidence_sha256 = None
        if with_evidence:
            evidence = render_evidence(self.ledger.evidence(), self.mask)
            self.evidence_sha256 = hashlib.sha256(evidence.encode()).hexdigest()
            first += "\n\nEvidence (cite these IDs):\n\n" + evidence
        return [{"role": "user", "content": f"{first}\n\n{instruction}"}]

    def known_ids(self) -> set[str]:
        """Every evidence ID in the ledger, quotes included: what a model output may cite."""
        return {e.id for e in self.ledger.evidence()}

    def trace(self) -> dict:
        """For the trace line of a call made with the latest user_message: a hash of the evidence it showed."""
        return {"evidence_sha256": self.evidence_sha256}

    def flag(self, kind: str, detail: str) -> None:
        self.flags.append({"flag": kind, "detail": detail})
        self.ledger.log("flags", kind, detail)


# -- gather ---------------------------------------------------------------------------------------------------------


def drop_papers(papers: list[dict], drop: set[str]) -> list[dict]:
    """The ablation: papers that name a dropped TF are removed before anything sees them."""
    if not drop:
        return papers
    up = {d.upper() for d in drop}
    return [p for p in papers if not (up & set(p.get("genes", [])) or any(d in f"{p.get('title', '')} "
                                                                             f"{p.get('abstract', '')}".upper()
                                                                             for d in up))]


def search_literature(state: State8, query: str) -> ToolResult:
    n = int(state.cfg["v8"]["literature"]["max_papers"])
    res = call_tool(pubtator_search, state.tool_case, query, masked=state.masked, before=state.before, max_papers=n)
    if res.ok and isinstance(res.full, list) and state.drop:
        kept = drop_papers(res.full, state.drop)
        if len(kept) != len(res.full):
            res.full = kept
            res.summary = "\n".join([res.summary.splitlines()[0]] + [
                f"PMID {p['pmid']} ({p['year']}): {p['title']}" for p in kept])
    if res.ok and isinstance(res.full, list):
        state.papers += res.full
    return res


def literature_query(state: State8, gene: str | None) -> str:
    parts = [state.spec.rsid] if state.spec.rsid and not state.masked else []
    parts += [gene] if gene else []
    parts.append(disease_terms(state.spec.disease).replace('"', "").strip("()").split(" OR ")[0])
    return " ".join(parts)


def row(tool: str, args: dict, summary: str, full, source: str, kind: str, status: str = "found") -> ToolResult:
    return ToolResult(tool, args, summary, full, source, "", kind, ok=status != "failed", status=status)


def ccre_location(ccre: ToolResult) -> tuple[bool, dict | None]:
    """(located, the registry's cCRE at or nearest the variant). The registry is local, so it answers even when
    SCREEN's own API fails (ccre_lookup keeps it in `full`); only without it is the location unknown."""
    located = isinstance(ccre.full, dict) and "local" in ccre.full
    return located, ccre.full["local"] if located else None


def element_summary(element: dict, context: str | None) -> str:
    if element.get("status") == "failed":
        return "The cCRE lookup failed, so whether the variant lies in a cCRE is unknown: no evidence either way."
    if not element["in_ccre"]:
        return (f"The variant is not inside a cCRE (the nearest, {element.get('accession')}, is "
                f"{element.get('distance')} bp away), so SCREEN has no activity data for this base.")
    act = element.get("status")
    here = "; ".join(f"{n}: {c}" for n, c in element.get("here", [])[:6]) or "none of the 170 core biosamples"
    els = element.get("active_elsewhere", [])
    where = ", ".join(sorted({n for n, _ in els})[:8])
    return (f"The variant lies in cCRE {element['accession']} ({element.get('class')}). SCREEN core collection (170 "
            f"biosamples with DNase, H3K4me3, H3K27ac and CTCF): in biosamples matching the context ({context or 'none'})"
            f": {here} -> {act}. Enhancer- or promoter-like in {len(els)} of {element.get('n', 170)} core biosamples"
            + (f", including {where}" if where else "") + ".")


def links_summary(accession: str | None, links: dict, names: list[str], tissue: str | None) -> str:
    if not accession:
        return "No cCRE at the variant, so SCREEN has no cCRE-gene links for it."
    parts = []
    by_gene: dict[str, list] = {}
    for x in links.get("3d", []):
        by_gene.setdefault(x["gene"], []).append(x)
    rows = []
    for g, xs in sorted(by_gene.items(), key=lambda kv: -len(kv[1])):
        here = [x for x in xs if screendb.matches(x["biosample"], names, tissue)]
        methods = sorted({x["method"] for x in (here or xs)})
        rows.append(f"{g} ({len(xs)} links; " + (f"in the context: {', '.join(methods)}" if here else
                                                 f"other biosamples only: {', '.join(methods)}") + ")")
    parts.append("3D contacts (Intact Hi-C, RNAPII and CTCF ChIA-PET): " + ("; ".join(rows[:10]) or "none"))
    eq = [f"{x['gene']} in {x['tissue']} (variant {x['variant']}, slope {x['slope']:+.2f})" for x in links.get("eqtl", [])]
    parts.append("eQTLs linked to the element: " + ("; ".join(eq[:8]) or "none"))
    cr = [f"{x['gene']} in {x['biosample']} (effect {x['effect']:+.2f}, p {x['p']:.2g})" for x in links.get("crispr", [])]
    parts.append("CRISPR perturbations of the element: " + ("; ".join(cr[:6]) or "none"))
    return f"SCREEN cCRE-gene links for {accession}. " + ". ".join(parts) + "."


def tissue_key(context: str | None, tissue: str | None) -> str | None:
    if tissue:
        low = tissue.lower()
        return next((k for k in screendb.TISSUE_WORDS if k in low), None)
    if context and context.startswith("DepMap:"):
        models = depmap_models()
        body = context[len("DepMap:"):]
        if body.startswith("subtype="):
            sub = body[len("subtype="):].split(" (")[0]
            lin = models.loc[models.OncotreeSubtype == sub, "OncotreeLineage"].mode()
            lineage = str(lin.iloc[0]) if len(lin) else ""
        else:
            mid = body.split(" ")[0]
            lineage = str(models.at[mid, "OncotreeLineage"]) if mid in models.index else ""
        low = lineage.lower()
        return next((v for k, v in LINEAGE_TISSUE.items() if k in low), None)
    return None


def gather8(state: State8) -> None:
    case, spec, cfg = state.tool_case, state.spec, state.cfg
    germline = spec.origin != "somatic"
    with ThreadPoolExecutor(max_workers=6) as pool:
        futs = {"variant_annotation": pool.submit(call_tool, variant_annotation, case),
                "nearest_genes": pool.submit(call_tool, nearest_genes, case),
                "ccre_lookup": pool.submit(call_tool, ccre_lookup, case),
                "promoter": pool.submit(promoter_check, case)}
        va = futs["variant_annotation"].result()
        if germline and not case.rsid and va.ok:
            rs = [c["id"] for c in va.full[0].get("colocated_variants", []) if str(c.get("id", "")).startswith("rs")]
            case.rsid = rs[0] if rs else None
        if germline:
            futs["gwas_lookup"] = pool.submit(call_tool, gwas_lookup, case)
            futs["finemap_lookup"] = pool.submit(call_tool, finemap_lookup, case)
            futs["eqtl_lookup"] = pool.submit(call_tool, eqtl_lookup, case)
        results = {k: f.result() for k, f in futs.items()}
    promoter = results.pop("promoter")
    ccre = results["ccre_lookup"]
    located, local = ccre_location(ccre)
    accession = (local or {}).get("accession")
    in_ccre = bool(local) and local.get("distance") == 0
    sdata = screendb.lookup(accession, case.http, cfg) if in_ccre else {"classes": [], "links": {}}
    expression = get_expression()
    if state.infer:
        info = infer_context(spec.disease, spec.is_cancer, results.get("eqtl_lookup"),
                             sdata["classes"] if in_ccre else [], expression)
    else:
        info = {"context": spec.expression_context, "route": "given", "reason": "given with the case", "tried": []}
    context = info["context"]
    if context:
        try:
            expression.parse(context)
        except ContextError as e:
            state.flag("context_unusable", f"{context}: {e}")
            context = None
    names, tissue = here_names(context)
    state.context = {**info, "context": context, "names": names[:30], "tissue": tissue}
    case.expression_context = context
    state.spec = dataclasses.replace(spec, expression_context=(f"{context} (inferred by code: {info['reason']})"
                                                               if state.infer and context else context))
    occ, occ_err = fetch_occupancy(case, get_registry())
    if occ_err is not None:
        state.flag("tool_failed", f"ENCODE occupancy: {occ_err.summary[:160]}")
    chip = fetch_chip(case, occ, names, int(cfg["v8"]["chip"]["window_bp"]))
    if not chip.remap_ok:
        state.flag("tool_failed", "ReMap lookup failed: ChIP grades use ENCODE peaks only")
    activity = screendb.activity(sdata["classes"], names, tissue) if in_ccre else {
        "status": "no_ccre" if located else "failed", "here": [], "active_elsewhere": [], "n": 0}
    element = {**activity, "in_ccre": in_ccre, "accession": accession, "class": (local or {}).get("class"),
               "distance": (local or {}).get("distance")}
    dline = disease_line(spec.origin, spec.disease, results.get("gwas_lookup"), results.get("finemap_lookup"), va,
                         spec.variant.alt)
    gene = top_gene(results.get("finemap_lookup"), results["nearest_genes"])
    query = literature_query(state, gene)
    lit = search_literature(state, query)
    # the evidence, in a fixed order whatever finished first
    for name in ("variant_annotation", "nearest_genes", "ccre_lookup"):
        note_retries(state, results[name])
        state.ledger.add_evidence("gather", results[name])
    prom = promoter.get("promoter_of", [])
    near = promoter.get("nearest_tss")
    state.ledger.add_evidence("gather", row(
        "promoter_check", {"variant": spec.variant.key()},
        ("The variant is in the promoter (1 kb upstream to 500 bp downstream of a transcript start) of "
         + ", ".join(f"{p['gene']} ({p['biotype']}, {p['distance']:+d} bp)" for p in prom) if prom else
         "The variant is not within 1 kb upstream or 500 bp downstream of any transcript start")
        + (f". Nearest transcript start: {near['gene']} ({near['distance']:+d} bp)." if near else "."),
        promoter, "Ensembl REST (transcripts of every gene type)", "genomic",
        status="found" if promoter.get("ok") else "failed"))
    state.ledger.add_evidence("gather", row("element_activity", {"ccre": accession, "context": context},
                                            element_summary(element, context), element, screendb.SOURCE, "epigenomic",
                                            status="found" if in_ccre else "tested_negative" if located
                                            else "failed"))
    state.ledger.add_evidence("gather", row("gene_links", {"ccre": accession},
                                            links_summary(accession if in_ccre else None, sdata["links"], names,
                                                          tissue), sdata["links"], screendb.SOURCE, "regulatory",
                                            status="found" if in_ccre else "not_tested"))
    for name in ("gwas_lookup", "finemap_lookup", "eqtl_lookup"):
        if name in results:
            note_retries(state, results[name])
            state.ledger.add_evidence("gather", results[name])
    state.ledger.add_evidence("gather", row(
        "intake", {"variant": spec.variant.key()},
        f"Code's intake. Expression context: {context or 'none'} ({info['route']}: {info['reason']}). Association "
        f"with the disease: {dline['state'].replace('_', ' ')} ({dline['reason']}).", {"context": state.context,
                                                                                      "disease_line": dline},
        "v2m intake (code)", "genetic"))
    note_retries(state, lit)
    if state.llm is not None:
        add_literature(state, "gather", lit, query)
    else:
        state.ledger.add_evidence("gather", lit)
    fm = results.get("finemap_lookup")
    va_genes = sorted({c.get("gene_symbol") for c in (va.full[0].get("transcript_consequences") or [])
                       if c.get("gene_symbol")}) if va.ok and va.full else []
    state.facts = Facts(
        use_qbic=state.arm == "full", families=[], element=element, disease=dline, promoter=promoter,
        eqtl=list(results["eqtl_lookup"].full or []) if "eqtl_lookup" in results and results["eqtl_lookup"].ok else [],
        links=sdata["links"] if in_ccre else {}, l2g=(fm.full or {}).get("best_l2g", {}) if fm is not None and fm.ok
        and isinstance(fm.full, dict) else {},
        nearest=[g["gene"] for g in (results["nearest_genes"].full or [])] if results["nearest_genes"].ok else [],
        overlaps=va_genes, here_names=names, tissue=tissue, tissue_key=tissue_key(context, tissue))
    state.ledger.log("gather", "done", {"context": state.context, "query": state.mask(query)})
    state._chip = chip


# -- the family screen ------------------------------------------------------------------------------------------------


def screen8(state: State8) -> None:
    v, cfg = state.spec.variant, state.cfg
    reg, expression = get_registry(), get_expression()
    use_qbic = state.arm == "full"
    scores, z_thr, site = None, 0.0, None
    if use_qbic:
        scores, err = state.qbic._scores(v)
        if err:
            raise RunStopped(f"QBiC-SELEX scores unavailable: {err}")
        _, _, z_thr = gate(scores, len(state.qbic.cache.models), ScreenSettings(alpha=0.05))
        ref, alt = state.qbic.cache.sequences(v.key(), stats=True)
        site = lambda m: site_score(m, ref, alt)  # noqa: E731
    context = state.context.get("context")
    ctx = expression.parse(context) if context else None
    out = family_screen(reg.groups(), reg, scores, z_thr, expression, ctx, state._chip, site=site, use_qbic=use_qbic,
                        drop=state.drop, table_n=int(cfg["v8"]["family"]["table_n"]),
                        min_tpm=float(cfg["screen"]["min_tpm"]))
    state.screen = out
    state.facts.families = out["families"]
    c = out["counts"]
    state.facts.element["bound_here"] = c["with_chip_here"] > 0
    if context and context.startswith("DepMap:ACH") and state.context.get("names"):
        here_label = state.context["names"][0]
    elif state.context.get("tissue"):
        here_label = state.context["tissue"]
    else:
        here_label = "the matched biosamples" if state.context.get("names") else "the context (no matched biosample)"
    order = ("ChIP-seq grade of the best member in the matched biosamples, then anywhere, then the family's best |z|"
             if use_qbic else "ChIP-seq grade of the best member in the matched biosamples, then anywhere, then expression")
    head = (f"Family screen of {v.key()} (code). " + (
        f"QBiC-SELEX: families with a model past the Bonferroni gate (|z| > {out['z_thr']}): {c['families_passing']}. "
        if use_qbic else "Without QBiC-SELEX: families with a member bound at the variant by ChIP-seq. ")
        + f"Candidates (at least one member not known to be unexpressed): {c['candidates']}; with ChIP-seq in the "
        f"matched biosamples: {c['with_chip_here']} (summit within 50 bp: {c['with_summit_here']}); anywhere: "
        f"{c['with_chip_anywhere']}. Ordered by {order}; shown: {c['shown']}. ChIP grades: summit within 50 bp of the "
        f"variant; peak within 50 bp; none. Sources: QBiC-SELEX 1.0.0, {REMAP}, ENCODE TF ChIP-seq, DepMap and GTEx "
        "expression. Effect > 0: the alternate allele binds more. In vitro binding only.")
    state.ledger.add_evidence("screen", row("family_screen", {"variant": v.key()}, head,
                                            {"counts": c, "z_thr": out["z_thr"]}, "v2m family screen (code)",
                                            "computational", status="found" if out["families"] else "tested_negative"))
    for f in out["families"]:
        ev = state.ledger.add_evidence("screen", row("family_screen", {"variant": v.key(), "family": f["fid"]},
                                                     family_line(f, here_label, context or "none"), f,
                                                     "v2m family screen (code)", "computational"))
        state.fam_ev[f["fid"]] = ev.id


# -- chains ----------------------------------------------------------------------------------------------------------


def top_families(state: State8) -> list[dict]:
    return state.screen["families"][: int(state.cfg["v8"]["family"]["top_n"])]


def generate8(state: State8) -> None:
    top = top_families(state)
    fams = "\n".join(f"- {f['fid']} ({f['label'].split(',')[0]} family): code names {f['named']}"
                     + (f"; paralogs not ruled out: {', '.join(f['paralogs'])}" if f["paralogs"] else "") for f in top)
    res = state.llm.call("generator", "generate", prompt8("generator_system"),
                         state.user_message(prompt8("generate").format(families=fams)), output_model=ChainsV8,
                         trace=state.trace(),
                         check=lambda c: ChainsV8(chains=check_chains(c.chains, state.screen["families"], len(top),
                                                                      {f["fid"] for f in top}, state.known_ids())))
    state.chains = res.parsed.chains
    state.ledger.add_chains("generate", 0, state.chains)


def best_gene(facts: Facts) -> tuple[str | None, dict]:
    """The gene with the highest gene-link tier among every gene the evidence names (ties: L2G, then nearness)."""
    cands = [p["gene"] for p in facts.promoter.get("promoter_of", [])] + [x["geneSymbol"] for x in facts.eqtl]
    for kind in ("crispr", "3d", "eqtl"):
        cands += [x["gene"] for x in facts.links.get(kind, [])]
    cands += list(facts.l2g) + facts.nearest[:2] + facts.overlaps
    seen, scored = set(), []
    for i, g in enumerate(cands):
        if not g or g.upper() in seen or g.startswith("ENSG"):
            continue
        seen.add(g.upper())
        t, why = gene_tier(facts, g)
        scored.append((t, facts.l2g.get(g, 0.0), -i, g, why))
    if not scored:
        return None, {}
    t, l2g, _, g, why = max(scored)
    return g, {"gene": g, "tier": t, "reason": why, "candidates": len(scored)}


def code_chains(state: State8) -> None:
    """The baseline: for each top family, its named member and the gene with the best gene link, with no model."""
    gene, choice = best_gene(state.facts)
    state.gene_choice = choice
    ev = {e.tool: e.id for e in state.ledger.evidence() if e.parent is None}
    out = []
    for i, f in enumerate(top_families(state), 1):
        fe = state.fam_ev[f["fid"]]
        links = [LinkV8(step="binding", claim=f"{f['named']} binding changes at the variant", evidence_ids=[fe]),
                 LinkV8(step="element", claim="the variant lies in a regulatory element",
                        evidence_ids=[ev.get("element_activity", "")]),
                 LinkV8(step="gene", claim=f"the element regulates {gene}", evidence_ids=[ev.get("gene_links", "")]),
                 LinkV8(step="cell_type", claim=f"{f['named']} acts in the context", evidence_ids=[fe]),
                 LinkV8(step="phenotype", claim=f"{gene} affects the disease", evidence_ids=[ev.get("intake", "")])]
        out.append(ChainV8(id=f"H{i}", title=f"{f['named']} ({f['label'].split(',')[0]} family) via {gene}",
                           family_id=f["fid"], tf=f["named"], member_reason="",
                           allele_binding_more=f.get("binds_more") or "ref", element=state.facts.element.get(
                               "accession") or "none", target_gene=gene or "", cell_type=state.context.get(
                               "context") or "none", links=links, predictions=[], falsified_if=[]))
    state.chains = out
    state.ledger.add_chains("code", 0, out)


def critique8(state: State8) -> None:
    instruction = prompt8("critique").format(tool_list=tool_list(state), chains=chains_json(state.chains))
    res = state.llm.call("critic", "critique", prompt8("critic_system"), state.user_message(instruction),
                         output_model=CritiqueV8, trace=state.trace(),
                         check=lambda o: check_critique(o, state.chains, state.known_ids()))
    out = res.parsed
    state.grades0, state.problems, state.critic_elims = out.grades, out.problems, out.eliminations
    state.next_experiment = out.next_experiment
    state.checks = keep_checks(state, "critique", out.checks)
    state.ledger.add_grades("critique", 0, "critic", state.grades0)


def run_lookup(state: State8, name: str, args: dict) -> tuple[str, str]:
    if name == "literature_search":
        res = search_literature(state, args.get("query", ""))
        note_retries(state, res)
        ev, quotes = add_literature(state, "investigate", res, args.get("query", ""))
        text = f"{ev.id}: {ev.summary}" + "".join(f'\n{q.id} (PMID {q.pmid}): "{q.quote}"' for q in quotes)
        return state.mask(text), outcome(res)
    return run_tool(state, name, args)


def lookups8(state: State8) -> None:
    """One round: the critic's kept checks, at most `max_calls`, then one regrade if anything ran."""
    max_calls = int(state.cfg["v8"]["lookups"]["max_calls"])
    done, records = set(), []
    for c in state.checks[:max_calls]:
        ok, note = validate_check(state, c)
        rec = {"tool": c.tool, "args": None, "resolves": c.resolves, "why": c.why, "run": False, "status": note or "",
               "evidence_id": None, "new_information": False}
        if ok:
            args = {k: v for k, v in json.loads(c.args_json).items() if v is not None}
            key = call_key(c.tool, args)
            rec["args"] = args
            if key in done:
                rec["status"] = "repeat"
            else:
                done.add(key)
                text, got = run_lookup(state, c.tool, args)
                if text.startswith("Error"):
                    rec["status"] = text
                else:
                    rec |= {"run": True, "status": "run" if got == "new" else got,
                            "evidence_id": text.split(":", 1)[0], "new_information": got == "new"}
        records.append(rec)
    state.lookups = records
    state.ledger.log("lookups", "round 1", records)
    if any(r["run"] for r in records):
        regrade8(state, records)


def regrade8(state: State8, records: list[dict]) -> None:
    calls = "\n".join(f"{r['tool']}({json.dumps(r['args'])}) for {r['resolves']}: "
                      + (f"result {r['evidence_id']}" if r["run"] else f"not run ({r['status']})") for r in records)
    instruction = prompt8("regrade").format(calls=calls, chains=chains_json(state.chains))
    res = state.llm.call("critic", "regrade", prompt8("critic_system"), state.user_message(instruction),
                         output_model=CritiqueV8, trace=state.trace(),
                         check=lambda o: check_critique(o, state.chains, state.known_ids()))
    out = res.parsed
    state.grades1, state.problems, state.critic_elims = out.grades, out.problems, out.eliminations
    state.next_experiment = out.next_experiment.strip() or state.next_experiment
    state.ledger.add_grades("regrade", 1, "critic", state.grades1)


def refresh_facts(state: State8) -> None:
    """Lookups can add eQTL rows and gene-disease scores that the gene and disease tiers use."""
    for e in state.ledger.evidence():
        if e.stage != "investigate" or not e.ok or not e.full_path:
            continue
        try:
            full = json.loads((state.run_dir / e.full_path).read_text())
        except (OSError, ValueError):
            continue
        if e.tool == "eqtl_lookup" and isinstance(full, list):
            seen = {(x["geneSymbol"], x["tissueSiteDetailId"]) for x in state.facts.eqtl}
            state.facts.eqtl += [x for x in full if (x["geneSymbol"], x["tissueSiteDetailId"]) not in seen]
        if e.tool == "gene_disease" and isinstance(full, dict) and full.get("rows"):
            state.facts.gene_disease[e.args.get("gene", "")] = float(full["rows"][0]["score"])


# -- decide (code) ---------------------------------------------------------------------------------------------------


def relevant(ev, chain) -> bool:
    names = {chain.tf.upper(), (chain.target_gene or "").upper()} - {""}
    return any(str(v).upper() in names for v in (ev.args or {}).values())


def decide8(state: State8) -> None:
    facts, chains = state.facts, state.chains
    state.tiers = {c.id: chain_tiers(facts, c) for c in chains}
    state.mins = {c.id: minimum(facts, c, state.tiers[c.id]) for c in chains}
    elim = code_eliminations(chains, state.tiers)
    by_id = {c.id: c for c in chains}
    for e in state.critic_elims:
        c = by_id.get(e.hypothesis_id)
        evs = [state.ledger.get(i) for i in e.evidence_ids]
        neg = [ev.id for ev in evs if ev is not None and ev.status == "tested_negative" and c is not None
               and relevant(ev, c)]
        if c is not None and neg and c.id not in elim:
            elim[c.id] = f"critic, on tested-negative evidence {', '.join(neg)}: {e.reason}"
            continue
        why = ("names no chain of this run" if c is None else
               "already eliminated by code (the critic agrees)" if c.id in elim else
               "cites no tested-negative evidence about this chain's TF or gene")
        state.rejected_elims.append({"hypothesis_id": e.hypothesis_id, "reason": e.reason, "why_rejected": why})
    flag_failed_citations(state)
    state.eliminated = elim
    order = {f["fid"]: i for i, f in enumerate(state.screen["families"])}
    state.ranked = rank(chains, state.tiers, state.mins, elim, order)
    if state.llm is not None and len(state.ranked) >= 2 and tied(state, *state.ranked[:2]):
        tie_break(state)
    v = verdict(state.ranked, state.mins, facts, len(chains))
    if state.ranked:
        top = state.ranked[0]
        g = state.tiers[top.id]["gene"]
        v["gene"] = {"gene": top.target_gene, "tier": g["tier"], "name": g["name"], "reason": g["reason"],
                     "resolved": g["tier"] >= 2}
    else:
        v["gene"] = {"gene": None, "tier": None, "name": None, "reason": "no chain", "resolved": False}
    state.verdict = v


def flag_failed_citations(state: State8) -> None:
    """A chain may cite a row whose tool failed (it says nothing either way); flag each such citation."""
    failed = {e.id: e.tool for e in state.ledger.evidence() if not e.ok}
    for c in state.chains:
        for lk in c.links:
            for i in lk.evidence_ids:
                if i in failed:
                    state.flag("cites_failed_row", f"{c.id}.{lk.step} cites {i} ({failed[i]}), whose tool failed")


def tied(state: State8, a, b) -> bool:
    """Equal on the minimum and on every link tier: code cannot separate them."""
    ta = [state.tiers[a.id][s]["tier"] for s in ("binding", "cell_type", "element", "gene", "phenotype")]
    tb = [state.tiers[b.id][s]["tier"] for s in ("binding", "cell_type", "element", "gene", "phenotype")]
    return ta == tb and state.mins[a.id] == state.mins[b.id]


def tie_break(state: State8) -> None:
    """The critic compares the two tied chains in both orders; the order changes only if B wins both."""
    a, b = state.ranked[0], state.ranked[1]
    games = []
    for x, y in ((a, b), (b, a)):
        instruction = prompt8("compare").format(a=f"Chain A ({x.id}):\n{x.model_dump_json()}",
                                                b=f"Chain B ({y.id}):\n{y.model_dump_json()}")
        res = state.llm.call("critic", "compare", prompt8("critic_system"), state.user_message(instruction),
                             output_model=Comparison, trace=state.trace(),
                             check=lambda o: check_cited(o, state.known_ids()))
        games.append({"a": x.id, "b": y.id, **res.parsed.model_dump()})
    b_wins = games[0]["winner"] == "B" and games[1]["winner"] == "A"
    if b_wins:
        state.ranked[0], state.ranked[1] = b, a
    state.tie_break = {"pair": [a.id, b.id], "games": games, "swapped": b_wins}
    state.ledger.log("rank", "tie break", state.tie_break)


def literature_flags(state: State8) -> list[dict]:
    rsid = state.tool_case.rsid
    out = []
    for c in state.chains:
        fam = state.facts.family(c.family_id) or {}
        tfs = [c.tf] + list(fam.get("paralogs", []))
        for p in state.papers:
            t = chain_tags(p, rsid, tfs, [c.target_gene], state.spec.disease)
            if t["flags"]:
                out.append({"chain": c.id, **t})
    return out


# -- run -------------------------------------------------------------------------------------------------------------


def run_dir_for(cfg: Config, spec: CaseSpec, arm: str, seed: int, root: str | None = None) -> Path:
    from ..config import REPO
    return REPO / (root or cfg["v8"]["dev_dir"]) / arm / str(seed) / spec.case_id


def run_case8(spec: CaseSpec, arm: str = "full", masked: bool = True, seed: int = 0, cfg: Config | None = None,
              transport=None, http: Http | None = None, qbic=None, run_dir: Path | None = None, phase: str = "dev",
              infer: bool = False, code_only: bool = False, drop: set | None = None, before: str | None = None,
              fresh: bool = True, single_prompts: str = "memory") -> dict:
    from .report import build_report, write_report
    if arm not in ARMS:
        raise ValueError(f"arm must be one of {ARMS}")
    cfg = cfg or load_config()
    run_dir = Path(run_dir or run_dir_for(cfg, spec, arm, seed))
    if fresh and run_dir.exists():
        run_dir.rename(run_dir.with_name(f"{run_dir.name}.prev-{time.strftime('%Y%m%dT%H%M%S')}"))
    run_dir.mkdir(parents=True, exist_ok=True)
    t0 = time.time()
    t = cfg["tools"]
    http = http or Http(cfg.path("tools", "http_cache"), tries=int(t.get("http_tries", 6)))
    llm = None if code_only else LLMClient(cfg, transport=transport, phase=phase, trace_path=run_dir / "trace.jsonl",
                                           seed=seed)
    tool_case = Case(spec.variant, spec.disease, spec.origin, spec.rsid, spec.expression_context, http,
                     retry_rounds=int(t.get("tool_retry_rounds", 2)), retry_wait=float(t.get("tool_retry_wait", 60)))
    if arm == "full" and qbic is None:
        from ..qbic.tools import QbicTools
        qbic = QbicTools(cfg)
    state = State8(spec, arm, masked, run_dir, Ledger(run_dir), llm, tool_case, qbic if arm == "full" else None, cfg,
                   infer=infer, drop=set(drop or ()), before=before)
    state.code_only = code_only
    try:
        if arm == "single":
            system, task = SINGLE_PROMPTS[single_prompts]
            res = llm.call("generator", "single", prompt8(system),
                           state.user_message(prompt8(task), with_evidence=False), output_model=SingleOut,
                           trace=state.trace())
            state.single = res.parsed.chains[:5]
        else:
            gather8(state)
            screen8(state)
            if state.screen["families"]:
                if code_only:
                    code_chains(state)
                else:
                    generate8(state)
                    critique8(state)
                    lookups8(state)
                    refresh_facts(state)
            decide8(state)
        for e in state.ledger.evidence():
            if not e.ok:
                state.flag("tool_failed", f"{e.id} {e.tool}: {e.summary.splitlines()[0][:160]}")
        report = build_report(state, time.time() - t0)
        write_report(state, report)
        return report
    finally:
        state.ledger.close()


__all__ = ["run_case8", "State8", "NAMES"]
