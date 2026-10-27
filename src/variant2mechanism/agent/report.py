"""report.json and report.md (spec 2, 8.8)."""

import json

from .case import RunState

STATUS_MARK = {"supported": "supported", "weak": "weak", "missing": "missing"}


def build_report(state: RunState, ranked: list, cit: dict, seconds: float) -> dict:
    statuses = cit["statuses"]
    chains = []
    for i, h in enumerate(ranked, 1):
        d = h.model_dump()
        d["rank"] = i
        d.update(cit["coverage"].get(h.id, {}))
        for link in d["links"]:
            link["status"] = statuses.get((h.id, link["step"]), "missing")
        chains.append(d)
    ev = state.ledger.evidence()
    return {
        "case_id": state.spec.case_id, "variant": state.spec.label, "variant_key": state.spec.variant.key(),
        "disease": state.spec.disease, "origin": state.spec.origin,
        "expression_context": state.spec.expression_context, "config": state.config,
        "mode": "masked" if state.masked else "named", "seed": state.llm.seed,
        "models": {k: state.llm.cfg["llm"][k] for k in ("generator", "critic", "summariser")},
        "cost_usd": round(state.llm.total_cost, 4), "seconds": round(seconds, 1), "model_calls": state.llm.calls,
        "screen": None if not state.screen else {
            "n_pass": state.screen["n_pass"],          # diagnostic only: never shown to the model (spec 3, 2.5)
            "counts": state.screen["counts"], "nothing_occupied": state.screen["nothing_occupied"],
            "occupied": [{**{k: r[k] for k in ("tf", "z", "occupancy", "passes_gate")},
                          "strong_site": r.get("strong_site")} for r in state.screen["occupied"]],
            "unknown": [{k: r[k] for k in ("tf", "z")} for r in state.screen["unknown"]]},
        "chains": chains,
        "chains_v0": [{"id": h.id, "tf": h.tf, "is_null": h.is_null, "probability": h.probability,
                       "allele_binding_more": h.allele_binding_more} for h in state.v0],
        "grades_v0": [g.model_dump() for g in state.grades0],
        "grades_final": [g.model_dump() for g in state.grades1],
        "checks": [c.model_dump() for c in state.checks0],
        "investigate_calls": state.investigate_calls,
        "rounds": state.rounds, "stop_reason": state.stop_reason,
        "matrix": [r.model_dump() for r in state.revised.matrix],
        "next_experiment": state.revised.next_experiment,
        "citation_support": cit["citation_support"],
        "flags": state.flags,
        "evidence": [{"id": e.id, "tool": e.tool, "source": e.source, "url": e.url, "retrieved_utc": e.retrieved_utc,
                      "kind": e.kind, "ok": e.ok, "summary": e.summary} for e in ev],
    }


def render_markdown(r: dict) -> str:
    out = [f"# {r['variant']} and {r['disease']}", "",
           f"Configuration `{r['config']}`, {r['mode']} mode, seed {r['seed']}. Models: generator "
           f"{r['models']['generator']}, critic {r['models']['critic']}, summariser {r['models']['summariser']}. "
           f"Cost ${r['cost_usd']:.2f} over {r['model_calls']} model calls; {r['seconds']:.0f} s.", "",
           f"Variant `{r['variant_key']}` ({r['origin']}); expression context: {r['expression_context'] or 'none'}.", ""]
    if r["screen"]:
        occ = "; ".join(f"{x['tf']} ({x['occupancy'].replace('_', ' ')}, z {x['z']}"
                        + ("" if x["passes_gate"] else ", no clear allelic change")
                        + (", weak site" if x.get("strong_site") is False else "") + ")"
                        for x in r["screen"]["occupied"])
        unk = "; ".join(f"{x['tf']} (z {x['z']})" for x in r["screen"]["unknown"])
        out += ["## QBiC-SELEX screen (occupancy first)", "",
                f"Occupied candidates: {occ or 'none'}. Occupancy unknown: {unk or 'none'}. Diagnostic, not shown to "
                f"the model: {r['screen']['n_pass']} of 997 models pass Bonferroni.", ""]
    out += ["## Ranked chains", ""]
    for c in r["chains"]:
        title = f"### {c['rank']}. {c['id']}: {c['title']} (p = {c['probability']:.2f})"
        out += [title, ""]
        if c["is_null"]:
            out += ["Null chain: no TF-mediated effect of this variant.", ""]
        else:
            out += [f"TF {c['tf']} (QBiC-SELEX coverage {c.get('coverage_status')}), "
                    f"{c['allele_binding_more']} allele binds more; element {c['element']}; gene {c['target_gene']}; "
                    f"cell type {c['cell_type']}.", "", "| Step | Claim | Status | Evidence |", "| --- | --- | --- | --- |"]
            for lk in c["links"]:
                ids = ", ".join(f"[{i}](#{i.lower()})" for i in lk["evidence_ids"]) or "none"
                claim = lk["claim"].replace("|", "/").replace("\n", " ")
                out.append(f"| {lk['step']} | {claim} | {lk['status']} | {ids} |")
            out.append("")
        if c["predictions"]:
            out += ["Predictions: " + "; ".join(c["predictions"]), ""]
        if c["falsified_if"]:
            out += ["Falsified if: " + "; ".join(c["falsified_if"]), ""]
    out += ["## Prediction matrix", ""]
    ids = [c["id"] for c in r["chains"]]
    out += ["| Test | Cost | Separates top two | " + " | ".join(ids) + " |",
            "| --- | --- | --- | " + " | ".join("---" for _ in ids) + " |"]
    for row in r["matrix"]:
        oc = {o["hypothesis_id"]: o["outcome"].replace("|", "/") for o in row["outcomes"]}
        out.append(f"| {row['test'].replace('|', '/')} | {row['cost']} | {'yes' if row['separates_top_two'] else 'no'} | "
                   + " | ".join(oc.get(i, "") for i in ids) + " |")
    out += ["", "## Next experiment", "", r["next_experiment"], ""]
    if r["rounds"]:
        out += render_rounds(r)
    out += ["## Flags", ""] + ([f"- {f['flag']}: {f['detail']}" for f in r["flags"]] or ["- none"]) + [""]
    if r["citation_support"] is not None:
        out += [f"Citation support: {r['citation_support']:.2f} of links cite only evidence that passed every check.", ""]
    out += ["## Evidence", ""]
    for e in r["evidence"]:
        status = "" if e["ok"] else " (failed)"
        out += [f'<a id="{e["id"].lower()}"></a>**{e["id"]}** {e["tool"]}{status}, {e["source"]} '
                f"({e['url']}; retrieved {e['retrieved_utc'] or 'local'})", "", "> " + e["summary"].replace("\n", "\n> "),
                ""]
    return "\n".join(out)


def render_rounds(r: dict) -> list[str]:
    """Each refinement round: the planned calls with their expected results, what ran, the results against the
    expectations, the chains after revision and the link grades that changed."""
    out = ["## Refinement rounds", "", f"Stopped: {r['stop_reason']}.", ""]
    later = [c for c in r["investigate_calls"] if c["round"] > len(r["rounds"])]
    for rd in r["rounds"] + ([{"round": later[0]["round"], "calls": later}] if later else []):
        out += [f"### Round {rd['round']}", ""]
        for c in rd["calls"]:
            args = json.dumps(c["args"]) if c["args"] is not None else "(invalid arguments)"
            done = (f"ran as [{c['evidence_id']}](#{c['evidence_id'].lower()})"
                    + ("" if c["status"] == "run" else f" ({c['status']})")) if c["run"] else f"not run: {c['status']}"
            out.append(f"- {c['tool']}({args}) for {c['resolves']}, {done}. Expected: {c['expected']}")
        if not rd["calls"]:
            out.append("- No calls planned.")
        if "chains" not in rd:                 # the stopping round: nothing new ran, so no revision
            out.append("")
            continue
        out += [""] + [f"- Result of {x['call']}: {x['observed']} (as expected: {x['as_expected']})"
                       for x in rd["check_results"]]
        top = "; ".join(f"{'null' if c['is_null'] else c['tf']} {c['probability']:.2f}"
                        for c in sorted(rd["chains"], key=lambda c: -c["probability"]))
        out += ["", f"Chains after revision: {top}. Link grades changed: {', '.join(rd['grades_changed']) or 'none'}.",
                ""]
    return out


def write_report(state: RunState, report: dict) -> None:
    (state.run_dir / "report.json").write_text(json.dumps(report, indent=1, default=str))
    (state.run_dir / "report.md").write_text(render_markdown(report))
