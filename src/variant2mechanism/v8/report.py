"""v8 reports: report.json (everything), report.md (a summary) and report.html (the mechanism map, self-contained)."""

import json
from pathlib import Path

TEMPLATE = Path(__file__).with_name("report_template.html")


def _members(f: dict, n: int = 8) -> dict:
    keep = ("tf", "tpm", "state", "grade_here", "grade_any", "summit_here", "summit_any", "cells_any", "assayed_here")
    return {**{k: v for k, v in f.items() if k != "members"},
            "members": [{k: m.get(k) for k in keep} for m in f["members"][:n]], "n_members": len(f["members"])}


def build_report(state, seconds: float) -> dict:
    llm = state.llm
    base = {"version": "v8", "case_id": state.spec.case_id, "variant": state.spec.label,
            "variant_key": state.spec.variant.key(), "disease": state.spec.disease, "origin": state.spec.origin,
            "arm": state.arm, "mode": "masked" if state.masked else "named", "seed": llm.seed if llm else None,
            "repeat": llm.seed if llm else None,     # what "seed" always was: a repeat that only changes the cache key
            "code_only": getattr(state, "code_only", False), "infer_context": state.infer,
            "literature_before": state.before, "dropped_tfs": sorted(state.drop),
            "models": {k: llm.cfg["llm"][k] for k in ("generator", "critic", "summariser")} if llm else None,
            "cost_usd": round(llm.total_cost, 4) if llm else 0.0, "model_calls": llm.calls if llm else 0,
            "seconds": round(seconds, 1), "flags": state.flags}
    if state.arm == "single":
        return base | {"single": [c.model_dump() for c in getattr(state, "single", [])], "verdict": None}
    rank_of = {c.id: i for i, c in enumerate(state.ranked, 1)}
    g0 = {(g.hypothesis_id, g.step): g.model_dump() for g in state.grades0}
    g1 = {(g.hypothesis_id, g.step): g.model_dump() for g in state.grades1}
    chains = []
    for c in state.chains:
        d = c.model_dump()
        d |= {"rank": rank_of.get(c.id), "eliminated": state.eliminated.get(c.id), "tiers": state.tiers.get(c.id),
              "minimum": state.mins.get(c.id), "evidence_family": state.fam_ev.get(c.family_id)}
        for lk in d["links"]:
            lk["critique"] = g0.get((c.id, lk["step"]))
            lk["regrade"] = g1.get((c.id, lk["step"]))
        chains.append(d)
    chains.sort(key=lambda d: (d["rank"] is None, d["rank"] or 0))
    e = state.facts.element
    element = {k: e.get(k) for k in ("status", "in_ccre", "accession", "class", "distance", "n")}
    element |= {"here": e.get("here", []), "active_elsewhere": [n for n, _ in e.get("active_elsewhere", [])]}
    papers = [{k: p.get(k) for k in ("pmid", "title", "year", "journal", "genes", "variants", "diseases")}
              for p in state.papers]
    ev = state.ledger.evidence()
    return base | {
        "context": state.context, "intake": {"disease_line": state.facts.disease, "promoter": state.facts.promoter},
        "element": element, "gene_links": state.facts.links, "eqtl": state.facts.eqtl, "l2g": state.facts.l2g,
        "screen": {"counts": state.screen["counts"], "z_thr": state.screen["z_thr"],
                   "use_qbic": state.screen["use_qbic"], "families": [_members(f) for f in state.screen["families"]],
                   "evidence_ids": state.fam_ev},
        "chains": chains, "ranking": [c.id for c in state.ranked], "eliminated": state.eliminated,
        "rejected_eliminations": state.rejected_elims, "verdict": state.verdict,
        "critique": {"problems": state.problems, "checks": [c.model_dump() for c in state.checks],
                     "next_experiment": state.next_experiment},
        "lookups": state.lookups, "gene_choice": state.gene_choice, "papers": papers,
        "tie_break": getattr(state, "tie_break", None),
        "literature_flags": literature_flags_safe(state),
        "evidence": [{"id": x.id, "tool": x.tool, "source": x.source, "url": x.url, "kind": x.kind, "ok": x.ok,
                      "status": x.status, "stage": x.stage, "summary": x.summary} for x in ev]}


def literature_flags_safe(state) -> list[dict]:
    from .run import literature_flags
    try:
        return literature_flags(state)
    except Exception as e:             # a tagging error must not lose the run
        return [{"error": str(e)[:200]}]


def render_markdown(r: dict) -> str:
    out = [f"# {r['variant']} and {r['disease']} (v8, {r['arm']}, {r['mode']}, repeat {r.get('repeat', r['seed'])})",
           ""]
    if r["arm"] == "single":
        out += ["Memory test: no tools, no evidence.", ""] + [
            f"{i}. {c['tf']} ({c['allele_binding_more']} binds more) -> {c['target_gene']}: {c['reason']}"
            for i, c in enumerate(r["single"], 1)]
        return "\n".join(out) + "\n"
    v = r["verdict"]
    ctx = r["context"]
    out += [f"Context: {ctx.get('context') or 'none'} ({ctx.get('route')}: {ctx.get('reason')}).", "",
            f"**Verdict: {v['overall']['verdict']}.** {v['overall']['reason']}.", "",
            f"- TF mechanism: {v['tf']['verdict']} ({v['tf']['reason']})",
            f"- Target gene: {v['gene']['gene']} ({v['gene']['name']}: {v['gene']['reason']})",
            f"- Disease link: {v['disease']['state'].replace('_', ' ')} ({v['disease']['reason']})", "",
            f"Cost ${r['cost_usd']:.3f} over {r['model_calls']} model calls; {r['seconds']:.0f} s.", "",
            "## Chains", "", "| Rank | Chain | TF | Gene | Binding | Cell type | Element | Gene link | Disease | Status |",
            "|---|---|---|---|---|---|---|---|---|---|"]
    for c in r["chains"]:
        t = c["tiers"] or {}
        cells = [t.get(s, {}).get("name", "") for s in ("binding", "cell_type", "element", "gene", "phenotype")]
        status = f"eliminated: {c['eliminated']}" if c["eliminated"] else "kept"
        out.append(f"| {c['rank'] or '-'} | {c['id']} ({c['family_id']}) | {c['tf']} | {c['target_gene']} | "
                   + " | ".join(cells) + f" | {status} |")
    out += ["", "## Family screen", ""]
    for f in r["screen"]["families"]:
        out.append(f"- {f['fid']} {f['label']}: named {f['named']}" + (f" (z {f['z']})" if "z" in f else "")
                   + f"; ChIP tier here {f['tier_here']}, anywhere {f['tier_any']}")
    out += ["", "## Next experiment", "", r["critique"]["next_experiment"] or "none", ""]
    if r["literature_flags"]:
        out += ["## Literature flags", ""] + [f"- {x.get('chain')}: PMID {x.get('pmid')} ({', '.join(x.get('flags', []))})"
                                               for x in r["literature_flags"]] + [""]
    out += ["## Flags", ""] + ([f"- {f['flag']}: {f['detail']}" for f in r["flags"]] or ["- none"])
    return "\n".join(out) + "\n"


def render_html(r: dict) -> str:
    data = json.dumps(r, default=str).replace("</", "<\\/")
    return TEMPLATE.read_text().replace("/*DATA*/", data)


def write_report(state, report: dict) -> None:
    (state.run_dir / "report.json").write_text(json.dumps(report, indent=1, default=str))
    (state.run_dir / "report.md").write_text(render_markdown(report))
    if report["arm"] != "single" and TEMPLATE.exists():
        (state.run_dir / "report.html").write_text(render_html(report))
