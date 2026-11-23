"""Link tiers, eliminations, ranking and the verdict (v8, code). The model's grades are shown, never used here.

Each link of a chain gets a tier from the data, by fixed rules: 3 direct, 2 supporting, 1 indirect, 0 untested,
-1 contradicted. Chains are ranked by whether they meet the minimum for a mechanism, then by dominance (at least as good
on every link and better on one), then by the binding link, the total and the screen's order. "No mechanism" comes
from these rules, never from a contest with a null chain.
"""

from dataclasses import dataclass, field

from .families import EXPRESSED, LOW, UNKNOWN
from .screendb import matches
from .sitescore import creates_site

NAMES = {3: "direct", 2: "supporting", 1: "indirect", 0: "untested", -1: "contradicted"}
STEPS = ("binding", "cell_type", "element", "gene", "phenotype")


@dataclass
class Facts:
    """What code knows about the run, gathered once."""
    use_qbic: bool
    families: list[dict]
    element: dict                       # screendb.activity(), plus "in_ccre", "accession", "class"
    disease: dict                       # intake.disease_line()
    promoter: dict                      # intake.promoter_check()
    eqtl: list[dict] = field(default_factory=list)          # GTEx rows for the variant (gather and lookups)
    links: dict = field(default_factory=dict)               # SCREEN cCRE-gene links of the element
    l2g: dict = field(default_factory=dict)                 # gene -> best L2G score
    nearest: list[str] = field(default_factory=list)        # nearest protein-coding genes
    overlaps: list[str] = field(default_factory=list)       # genes whose transcripts contain the variant
    gene_disease: dict = field(default_factory=dict)        # gene -> Open Targets overall score (from lookups)
    here_names: list[str] = field(default_factory=list)
    tissue: str | None = None                               # GTEx tissue of the context, for word matching
    tissue_key: str | None = None                           # e.g. "colon": matches eQTL tissues to the context

    def family(self, fid: str | None) -> dict | None:
        return next((f for f in self.families if f["fid"] == fid), None)


def member_of(fam: dict | None, tf: str) -> dict | None:
    return next((m for m in fam["members"] if m["tf"].upper() == (tf or "").upper()), None) if fam else None


def binding_tier(facts: Facts, fam: dict | None, m: dict | None, allele: str | None) -> tuple[int, str]:
    if fam is None or m is None:
        return 0, "the TF is not a member of a screened family"
    if facts.use_qbic:
        if allele != fam["binds_more"]:
            return -1, f"QBiC-SELEX says the {fam['binds_more']} allele binds more; the chain says {allele}"
        base = f"QBiC-SELEX: the {allele} allele binds more (z {fam['z']})"
        if m["grade_here"] == 1:
            return 3, f"{base}; {m['tf']} ChIP summit {m['summit_here']} bp from the variant in the context"
        if m["grade_here"] == 2 or m["grade_any"] == 1:
            return 2, f"{base}; {m['tf']} ChIP " + ("peak in the context" if m["grade_here"] == 2
                                                     else f"summit {m['summit_any']} bp away in another biosample")
        return 1, f"{base}; no {m['tf']} ChIP summit at the variant"
    if m["grade_here"] == 1:
        return 3, f"{m['tf']} ChIP summit {m['summit_here']} bp from the variant in the context"
    if m["grade_here"] == 2 or m["grade_any"] == 1:
        return 2, f"{m['tf']} ChIP peak in the context or a summit elsewhere"
    if m["grade_any"] == 2:
        return 1, f"{m['tf']} ChIP peak elsewhere"
    return 0, "no ChIP-seq for this TF at the variant"


def cell_tier(m: dict | None) -> tuple[int, str]:
    if m is None:
        return 0, "no expression data"
    tpm = f"{m['tpm']:.1f} TPM" if m["tpm"] is not None else "TPM unknown"
    if m["state"] == EXPRESSED and m["grade_here"] <= 2:
        return 3, f"expressed ({tpm}) and bound in the context"
    if m["state"] == EXPRESSED:
        return 2, f"expressed ({tpm})"
    if m["state"] == LOW:
        return 1, f"low in bulk tissue ({tpm}); a rare cell type can be diluted out"
    if m["state"] == UNKNOWN:
        return 0, "no expression context"
    return -1, f"not expressed ({tpm})"


def element_tier(facts: Facts, fam: dict | None) -> tuple[int, str]:
    """Activity of the element in the context. A ChIP-seq peak of any TF at the variant in the context shows the
    element is bound there, whatever SCREEN's DNase call (which can miss a site the cell line's allele lacks); with
    no SCREEN data for the context, activity elsewhere is only indirect, and its absence is no evidence."""
    e = facts.element
    creates = creates_site((fam or {}).get("site"), (fam or {}).get("binds_more"))
    bound = bool(e.get("bound_here"))
    if e.get("status") == "failed":           # a failed lookup is no evidence: never a contradiction
        return (1, "the cCRE lookup failed, but TFs are bound there by ChIP-seq in the context") if bound else \
               (0, "the cCRE lookup failed, so the element is untested")
    if not e.get("in_ccre"):
        if bound:
            return 1, "no cCRE at the variant, but TFs are bound there by ChIP-seq in the context"
        return (1, "no cCRE at the variant, but the variant creates the site") if creates else \
               (-1, "the variant is not in a cCRE and no TF is bound there in the context")
    status = e.get("status")
    here = ", ".join(sorted({n for n, _ in e.get("here", [])})[:4])
    if status == "active":
        return 3, f"active in {here}"
    if status == "open":
        return 2, f"open, without enhancer or promoter marks, in {here}"
    if bound:
        return 2, ("SCREEN calls it inactive in " + here + ", but ChIP-seq shows TFs bound there in the context"
                   if status == "inactive" else "no SCREEN data for the context, but ChIP-seq shows TFs bound there")
    if status == "inactive":
        return (1, f"inactive in {here}, but the variant creates the site") if creates else \
               (-1, f"inactive (Low-DNase) in {here}, and no TF bound there")
    if e.get("active_elsewhere"):
        return 1, f"no matched core biosample; active in {len(e['active_elsewhere'])} of {e.get('n', 170)} others"
    return 0, "no SCREEN data for the context, and no core biosample shows it active"


def eqtl_matched(tissue_id: str, facts: Facts) -> bool:
    return bool(facts.tissue_key) and facts.tissue_key in tissue_id.lower().replace("_", " ")


def gene_tier(facts: Facts, gene: str | None) -> tuple[int, str]:
    if not gene:
        return 0, "no target gene"
    g = gene.upper()
    if g in {p["gene"].upper() for p in facts.promoter.get("promoter_of", [])}:
        return 3, f"the variant is in the {gene} promoter"
    crispr = [x for x in facts.links.get("crispr", []) if x["gene"].upper() == g and x["p"] < 0.05]
    if crispr:
        return 3, f"CRISPR perturbation of the element changes {gene} ({crispr[0]['biosample']})"
    own = [x for x in facts.eqtl if x["geneSymbol"].upper() == g]
    if any(eqtl_matched(x["tissueSiteDetailId"], facts) for x in own):
        x = next(x for x in own if eqtl_matched(x["tissueSiteDetailId"], facts))
        return 3, f"eQTL for {gene} in {x['tissueSiteDetailId']} (NES {x['nes']:+.2f})"
    contact = [x for x in facts.links.get("3d", []) if x["gene"].upper() == g]
    near = [x for x in contact if matches(x["biosample"], facts.here_names, facts.tissue)]
    if near:
        return 2, f"3D contact with {gene} in {near[0]['biosample']} ({near[0]['method']})"
    if own:
        return 2, f"eQTL for {gene} in {own[0]['tissueSiteDetailId']} (another tissue)"
    if facts.l2g.get(gene, 0) >= 0.1:
        return 1, f"Open Targets L2G {facts.l2g[gene]:.2f}"
    if contact:
        return 1, f"3D contact with {gene} in other biosamples ({len(contact)} links)"
    if g in {x["gene"].upper() for x in facts.links.get("eqtl", [])}:
        return 1, f"SCREEN eQTL link between the element and {gene}"
    if g in {n.upper() for n in facts.nearest[:2]} or g in {o.upper() for o in facts.overlaps}:
        return 1, f"{gene} is the nearest gene or overlaps the variant"
    return 0, f"nothing links the element to {gene}"


def phenotype_tier(facts: Facts, gene: str | None) -> tuple[int, str]:
    d = facts.disease
    gd = max(facts.gene_disease.get(gene or "", 0.0), 0.0)
    gene_ev = (facts.l2g.get(gene or "", 0) >= 0.5) or gd >= 0.3
    why = d["reason"]
    if d["state"] == "supported":
        return (3, f"{why}; {gene} also has gene-level evidence") if gene_ev else (2, why)
    if d["state"] == "no_association":
        return -1, why
    return (1, f"{why}; {gene} has gene-level evidence") if gene_ev else (0, why)


def chain_tiers(facts: Facts, chain) -> dict[str, dict]:
    fam = facts.family(chain.family_id)
    m = member_of(fam, chain.tf)
    out = {}
    for step, (t, why) in zip(STEPS, (binding_tier(facts, fam, m, chain.allele_binding_more), cell_tier(m),
                                      element_tier(facts, fam), gene_tier(facts, chain.target_gene),
                                      phenotype_tier(facts, chain.target_gene)), strict=True):
        out[step] = {"tier": t, "name": NAMES[t], "reason": why}
    return out


def minimum(facts: Facts, chain, tiers: dict) -> dict:
    """The four checks a mechanism needs: pass, fail or unknown each."""
    fam = facts.family(chain.family_id)
    checks = {}
    b = tiers["binding"]["tier"]
    checks["binding change"] = "pass" if b >= (1 if facts.use_qbic else 2) else "fail"
    if fam is None:
        checks["ChIP-seq"] = "fail"
    else:                    # a family never assayed passes only where the element is open or bound in the context
        best = min(m["grade_any"] for m in fam["members"])
        checks["ChIP-seq"] = ("pass" if best <= 2 or (not fam["assayed"] and tiers["element"]["tier"] >= 2)
                              else "fail")
    c = tiers["cell_type"]["tier"]
    checks["expressed"] = "pass" if c >= 2 else ("unknown" if c == 0 else "fail")
    e = tiers["element"]["tier"]
    checks["element open"] = "pass" if e >= 1 else ("unknown" if e == 0 else "fail")
    return checks


def code_eliminations(chains, tiers: dict) -> dict[str, str]:
    """Strong contradictions only: the TF not expressed in a cell line, or an inactive element the variant does not
    create a site in."""
    out = {}
    for h in chains:
        t = tiers[h.id]
        if t["cell_type"]["tier"] == -1:
            out[h.id] = f"{h.tf} {t['cell_type']['reason']}"
        elif t["element"]["tier"] == -1:
            out[h.id] = f"element: {t['element']['reason']}"
    return out


def dominates(a: list[int], b: list[int]) -> bool:
    return all(x >= y for x, y in zip(a, b, strict=True)) and any(x > y for x, y in zip(a, b, strict=True))


def rank(chains, tiers: dict, mins: dict, eliminated: dict, order: dict) -> list:
    """Surviving chains: meets-the-minimum first, then dominance layer, binding tier, total, screen order."""
    alive = [h for h in chains if h.id not in eliminated]
    vec = {h.id: [tiers[h.id][s]["tier"] for s in STEPS] for h in alive}
    layer, left, n = {}, set(vec), 0
    while left:
        top = {i for i in left if not any(dominates(vec[j], vec[i]) for j in left if j != i)}
        for i in top:
            layer[i] = n
        left -= top
        n += 1
    meets = {h.id: all(v == "pass" for v in mins[h.id].values()) for h in alive}
    return sorted(alive, key=lambda h: (not meets[h.id], layer[h.id], -vec[h.id][0], -sum(vec[h.id]),
                                        order.get(h.family_id, 99)))


def verdict(ranked, mins: dict, facts: Facts, n_chains: int) -> dict:
    """Three lines (TF mechanism, target gene, disease link) and the overall verdict."""
    if not ranked:
        tf_line = {"verdict": "no mechanism", "reason": "every chain was eliminated" if n_chains
                   else "no candidate family"}
    else:
        top = ranked[0]
        m = mins[top.id]
        if all(v == "pass" for v in m.values()):
            tf_line = {"verdict": "mechanism", "reason": f"{top.tf} meets every check", "chain": top.id}
        elif any("unknown" in mins[h.id].values() and "fail" not in mins[h.id].values() for h in ranked):
            open_ = [k for k, v in m.items() if v != "pass"]
            tf_line = {"verdict": "undetermined", "reason": f"{top.tf}: not shown: {', '.join(open_)}", "chain": top.id}
        else:
            fails = [k for k, v in m.items() if v == "fail"]
            tf_line = {"verdict": "no mechanism", "chain": top.id,
                       "reason": f"no chain meets the minimum; the top chain ({top.tf}) fails: {', '.join(fails)}"}
    d = facts.disease
    if tf_line["verdict"] == "mechanism" and d["state"] == "no_association":
        overall = {"verdict": "no mechanism", "reason": "a molecular effect is possible, but the variant has no "
                                                        f"association with the disease ({d['reason']})"}
    else:
        overall = {"verdict": tf_line["verdict"], "reason": tf_line["reason"]}
    return {"tf": tf_line, "disease": {"state": d["state"], "reason": d["reason"]}, "overall": overall}
