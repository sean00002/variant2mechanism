"""The run's verdict (code): mechanism, no mechanism, or undetermined.

The chains are hypotheses about the variant, and the null among them means evidence against a TF mechanism. Missing
evidence is neither, so the verdict keeps the two apart, by a rule fixed in advance that adds no numbers of its own:

    mechanism       the top chain names a TF whose binding counts (verdict.binding: the critic graded the binding
                    link supported, QBiC-SELEX passes the gate in the claimed direction, or either), and no tested
                    fact counts against that TF
    no mechanism    the null leads, and every TF chain has at least one tested fact against its TF
    undetermined    anything else

Facts about a chain's TF come from code, with the tools its configuration has: QBiC-SELEX (full only: covered with no
model past the gate, or a change in the other direction, counts against), ENCODE occupancy (assayed in a matching
biosample with no peak over the variant counts against, unless ReMap has a peak there) and expression in the case's
context (below screen.min_tpm counts against). A `single` run gathers nothing, so it has no facts. An untested fact
counts neither way. The same function scores saved reports.
"""

from ...context.chip import same_biosample
from ..case import RunState
from .investigate import qbic_status
from .tournament import beats_null

FOR, AGAINST, UNKNOWN = "for", "against", "unknown"
FACTS = ("qbic", "occupancy", "expression")
BINDING_RULES = ("critic", "code", "either")
OCCUPANCY_WHY = {"bound_elsewhere": "bound only in other biosamples", "not_assayed": "never assayed by ENCODE",
                 "unbound_assayed_elsewhere": "assayed only in other biosamples"}


def qbic_fact(qbic, variant, symbol: str, allele: str | None) -> list[str]:
    """For if a model of the TF passes the gate in the claimed direction; against if the TF is covered and no model
    passes, or the best passing model points the other way; unknown otherwise."""
    if qbic is None:
        return [UNKNOWN, "no QBiC-SELEX in this configuration"]
    out = qbic.qbic_tf_detail(variant.chrom, variant.pos, variant.ref, variant.alt, symbol)
    status = qbic_status(out)
    if status in ("not_tested", "failed"):
        return [UNKNOWN, f"QBiC-SELEX: {out.get('coverage') or out.get('status') or out.get('error', 'unavailable')}"]
    if status == "tested_negative":
        return [AGAINST, "QBiC-SELEX: covered, but no model passes the gate"]
    best = max((m for m in out["models"] if m.get("passed_gate")), key=lambda m: abs(m["z"]))
    more = "alt" if best["effect"] > 0 else "ref"
    if allele and more != allele:
        return [AGAINST, f"QBiC-SELEX: {best['model']} passes the gate, but the {more} allele binds more"]
    return [FOR, f"QBiC-SELEX: {best['model']} passes the gate, the {more} allele binds more"]


def occupancy_fact(occupancy, symbol: str, remap=None) -> list[str]:
    """`remap(symbol)` returns ReMap peaks over the variant (dicts with a biosample), or None if it cannot."""
    if occupancy is None:
        return [UNKNOWN, "occupancy unavailable"]
    cls = occupancy.tf_class(symbol)
    if cls == "bound_here":
        return [FOR, "ENCODE ChIP-seq peak over the variant in a matching biosample"]
    if cls == "unbound_assayed_here":
        peaks = remap(symbol) if remap is not None else None
        if peaks and any(same_biosample(b, p["biosample"]) for b in occupancy.match.biosamples for p in peaks):
            return [FOR, "ReMap peak over the variant in a matching biosample (ENCODE's experiment has none)"]
        return [AGAINST, "ENCODE assayed it in a matching biosample: no peak over the variant"]
    return [UNKNOWN, OCCUPANCY_WHY.get(cls, cls)]


def expression_fact(expression, symbol: str, context: str | None, min_tpm: float) -> list[str]:
    if expression is None or not context or context.lower().startswith("none"):
        return [UNKNOWN, "no expression context"]
    try:
        tpm = expression.tf_expression([symbol], context)[symbol].get("tpm")
    except ValueError as err:                 # an expression context no table knows
        return [UNKNOWN, f"expression unavailable ({str(err)[:80]})"]
    if tpm is None:
        return [UNKNOWN, "no expression value"]
    return [AGAINST, f"{tpm} TPM, below {min_tpm:g}"] if tpm < min_tpm else [FOR, f"{tpm} TPM"]


def chain_facts(chains: list[dict], variant, context: str | None, reg, qbic=None, occupancy=None, expression=None,
                min_tpm: float = 1.0, remap=None) -> dict[str, dict]:
    """The facts about each TF chain's TF, by chain id."""
    out = {}
    for c in chains:
        if c["is_null"]:
            continue
        name = reg.resolve_tf(c["tf"]) if c.get("tf") else {"status": "none"}
        if name["status"] != "ok":
            out[c["id"]] = {"tf": c.get("tf"), "symbol": None,
                            **{k: [UNKNOWN, "TF name not resolved"] for k in FACTS}}
            continue
        sym = name["symbol"]
        out[c["id"]] = {"tf": c["tf"], "symbol": sym, "qbic": qbic_fact(qbic, variant, sym, c.get("allele")),
                        "occupancy": occupancy_fact(occupancy, sym, remap),
                        "expression": expression_fact(expression, sym, context, min_tpm)}
    return out


def decide(chains: list[dict], facts: dict[str, dict], pairwise_ok: bool | None = None,
           binding: str = "either") -> tuple[str, str]:
    """The verdict and its reason. `chains` are ranked, each with id, is_null, tf and links (step, final status);
    `pairwise_ok` is False when the top TF chain does not beat the null in both orders of the pairwise comparison;
    `binding` is one of BINDING_RULES."""
    against = {cid: [k for k in FACTS if f[k][0] == AGAINST] for cid, f in facts.items()}
    top = chains[0]
    if not top["is_null"]:
        graded = next((lk["status"] for lk in top["links"] if lk["step"] == "binding"), "missing")
        qbic_for = facts.get(top["id"], {}).get("qbic", [UNKNOWN])[0] == FOR
        counts = {"critic": graded == "supported", "code": qbic_for, "either": graded == "supported" or qbic_for}
        if not counts[binding]:
            return "undetermined", (f"the top chain's ({top['tf']}) binding link is {graded}"
                                    + ("" if binding == "critic" else " and QBiC-SELEX does not back it"))
        if against.get(top["id"]):
            why = "; ".join(facts[top["id"]][k][1] for k in against[top["id"]])
            return "undetermined", f"tested evidence counts against {top['tf']}: {why}"
        if pairwise_ok is False:
            return "undetermined", f"{top['tf']} does not beat the null in both orders of the pairwise comparison"
        return "mechanism", f"{top['tf']}: its binding counts, and nothing tested counts against it"
    untested = [c["tf"] for c in chains if not c["is_null"] and not against.get(c["id"])]
    if untested:
        return "undetermined", f"the null leads, but nothing tested counts against {', '.join(untested)}"
    return "no mechanism", "the null leads, and tested evidence counts against the TF of every other chain"


def verdict(state: RunState, ranked: list, statuses: dict, pairwise_ok: bool | None = None) -> dict:
    """The verdict of a run, from its ranked chains and the final link statuses of the citation check."""
    from ...context.chip import remap_peaks
    from ...qbic.expression import get_expression
    from ...qbic.registry import get_registry
    chains = [{"id": h.id, "is_null": h.is_null, "tf": h.tf, "allele": h.allele_binding_more,
               "links": [{"step": lk.step, "status": statuses.get((h.id, lk.step), "missing")} for lk in h.links]}
              for h in ranked]
    gathered = state.config != "single"                 # a single run has no tools, so code adds no facts
    facts = chain_facts(chains, state.spec.variant, state.spec.expression_context, get_registry(), state.qbic,
                        state.occupancy, get_expression() if gathered else None,
                        float(state.llm.cfg["screen"]["min_tpm"]), lambda s: remap_peaks(state.tool_case, s))
    if pairwise_ok is None and state.tournament and not ranked[0].is_null:
        null = next(h for h in ranked if h.is_null)
        pairwise_ok = beats_null(state.tournament, ranked[0].id, null.id)
    v, why = decide(chains, facts, pairwise_ok, (state.llm.cfg.get("verdict") or {}).get("binding", "either"))
    association = {e.tool: e.status for e in state.ledger.evidence() if e.tool in ("gwas_lookup", "finemap_lookup")}
    out = {"verdict": v, "reason": why, "pairwise_ok": pairwise_ok, "association": association, "facts": facts}
    state.ledger.log("verdict", v, out)
    return out
