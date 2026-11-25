"""The mechanism chain: every live claim about the case variant placed on the link it speaks to, with the strongest
kind of evidence linked to it.

Why: a hypothesis is a set of claims, so a run that finds an allelic binding assay, a reporter effect and an eQTL can
hold them in three hypotheses and report three tied explanations, although they are three links of one route from the
variant to a trait. This view reads the graph link by link instead:

    variant -> TF binding -> regulatory activity -> target gene -> gene to trait, and the variant's own trait link

It is derived from the graph and never stored. It changes no assessment, disposition, comparison or outcome, transfers
no evidence between claims and gives no score.

Links. A claim is placed by its relation: alters_binding on "TF binding"; alters_regulatory_activity on "regulatory
activity"; alters_rna, associated_with_expression and regulates (from the variant or an element) on "target gene";
contributes_to_trait and affects_process on "gene to trait"; associated_with_trait and causal_at_locus on "variant
to trait". overlaps claims give the location; occupies and expressed_in claims are listed as context of the factor
they name. They give no rung and are never a requirement: expression and ChIP coverage are neither weights nor
conditions, and a factor with neither keeps its place among its equals (see "In place" below). A claim about another
variant, a factor-to-gene claim and a claim with relation "other" are listed as not placed, never dropped silently.

Candidates. Within a link, claims are grouped by what they name: the TF or TF group, the element or gene whose
activity was measured, the target gene, the gene and trait, the trait. A member TF's binding claim joins its
model-sharing group's candidate when exactly one group with a binding claim lists it, so a group-level prediction and a
member-level assay read as one candidate; the member each claim names is kept.

Rungs. Each candidate carries the strongest kind of evidence linked to its claims as supports (accepted by the
graph's own identity, variant, direction and context gates; a link in a different context is context only there):

    edit         a direct link from a perturbation: the allele edited in the genome, or the element or gene perturbed
    assay        a direct link from an assay that compares the alleles (EMSA, reporter, MPRA, allele-specific reads)
    association  an association or statistical inference (eQTL, GWAS, fine-mapping), direct or indirect
    prediction   a model's output (QBiC-SELEX, L2G), which the class matrix always holds indirect
    none         nothing linked in support

The rung names a kind of evidence, never its size: z, effect size, read counts and the number of records do not enter
it. Experimental evidence that the class matrix holds indirect for a relation (a region deletion for a claim that the
alleles differ, ordinary ChIP for an allelic binding change) is listed beside the candidate and gives no rung. A claim
contested by direct evidence on both sides counts as none; a claim contradicted in scope ranks below none. The
claim's own assessment is shown beside the rung and is not changed by it: "association, not assessed" means an
association is linked and no role has assessed the claim. A link whose context match is not exact is labelled; when
the stored match is "unknown" only because its proposer declared it so although code computed a match, the label
says that, since such a claim cannot be assessed as supported. Only runs saved before graph.link stopped letting a
proposed "unknown" weaken a supporting link hold such links.

QBiC-SELEX. A binding candidate also shows the inventory's prediction for the same group (or for the group whose
models cover the TF), whether or not a role linked it. When no prediction is linked and the prediction does not
oppose the claim's direction, it gives the candidate the prediction rung, marked as read from the inventory: the
record is in the graph, and a refused or forgotten link would otherwise show a predicted claim as unsupported.

Order. Candidates of a link are ordered by rung, then by whether the claim is supported in scope, then by id.
Hypotheses are compared link by link on their own claims: one ranks above another only if it is at least as strong on
every link and stronger on one. Ties and unordered pairs are reported as such. Adjacent links are separate claims:
nothing here shows that one link causes the next.

Whole chains. The link table names the strongest candidate of each link; the run's answer is whole chains, each a
route through all five links, ranked. Code assembles them, because a role's hypothesis often holds a single link:
each chain takes one TF binding candidate and one target gene candidate (every pair the claims name), the strongest
candidates of the regulatory activity and variant to trait links (the same in every chain: they describe the site
and the trait, not a rival mechanism) and the gene to trait claims that name its gene. A gene that only a gene to
trait claim names still gets a chain, with its target gene link empty.

Chains are ordered by their weakest link: the five links' rungs are compared lowest first, then the next lowest, and
so on (leximin). This never places a chain above one that is at least as strong on every link, needs no weights, and
uses the kind of evidence only, so the size of z, effect size, ChIP signal, expression level and the number of
records cannot enter it. A link with no claim counts as no supporting evidence; a predicted link stays in the chain,
labelled as predicted; chains with the same rungs tie and are reported as tied. A candidate contradicted in scope
enters no chain and is listed. The rule was fixed from this argument, not chosen by how it scores any labelled case.

In place. Chains that tie on every link are then ordered by whether a record shows their transcription factor in
place: a claim that it occupies the variant's site with a ChIP-seq peak linked in support, and a claim that it is
expressed in the stated context with an expression record linked in support. Each is a yes or a no; a chain with
both stands above a chain with one, and one above none. This is presence only: the peak's signal, the summit's
distance and the expression level are not read, and nothing is ever removed, since a factor that was never assayed
is not a factor that is absent. It breaks ties and nothing else: no number of such records lifts a chain above
one with a stronger link.

Strong prediction. Before the in-place count, chains that tie on every link are ordered by one yes or no about the
binding link: its QBiC-SELEX prediction is large for that TF group and a ChIP-seq peak lies over the variant. "Large"
is read against the group's own background (qbic/background.py): |z| of the group's strongest model at this variant
is at or above the 90th percentile of the same value over 21.8 million unlabelled variants. The gate alone cannot
say this, since it passes a third of all variants for the median model and nearly all for a large group. The
prediction must not go against the allele the link's leading claims state. This is the one place the size of z is
read, as a yes or no fixed before any labelled case was looked at, and it only breaks ties: a TF with no model, a
prediction below its group's cut-off, or a TF never assayed by ChIP-seq stays in the list and loses no rung.

QBiC-SELEX as support. A significant prediction is supporting evidence and never evidence against. Alone it gives a
binding link the prediction rung. Beside an association or a measurement it lifts the link half a step, above an
equal link without it and below the next rung, when a gate-passing model favours the allele the link's leading claims
state (or those claims state no allele: the prediction then says the alleles differ, which is what they claim).
"Significant" is the inventory's gate, a yes or no; the size of z gives no rung. A TF with no model, or with
models that do not pass the gate, loses nothing and is labelled as such. A prediction for the other allele, or models that
disagree with each other, lift nothing and are flagged beside the link.

Factor lookups. After a run's decision, code looks up every TF a binding claim names (investigate.Engine): the
QBiC-SELEX models of the TF or group, the ChIP-seq survey at the variant and the TF's expression in the contexts the
case and its claims name. `factors` lists what those calls returned, one row per TF, beside the answer. A row by
itself orders nothing (only a claim with a record linked to it can break a tie, as above), and a missing peak or a
low level removes nothing.

Unclaimed factors. A group whose prediction passes the gate and that no binding claim covers gets no chain: the
Bonferroni gate passes a third to a half of all groups at a variant (182 to 322 of 631 in the development runs),
so chains for all of them would be hundreds of ties. They are counted beside the answer (`unclaimed`) and listed in
the inventory table.
"""

from collections.abc import Iterable, Mapping
from typing import Any

from ..qbic.background import in_top_share
from .bundle import inventory_call, inventory_items, inventory_table
from .graph import ClaimGraph
from .schemas import SPECIFIC_DIRECTIONS, Claim, Entity

CHAIN_FORMAT = 1
RUNGS: tuple[tuple[str, str, str], ...] = (
    ("edit", "Edit or perturbation",
     "the allele was edited in the genome, or the element or gene perturbed, and the effect measured"),
    ("assay", "Allele-resolved assay",
     "the alleles were compared in an assay such as an EMSA, a reporter or an MPRA, or by allele-specific reads"),
    ("association", "Association",
     "a population or statistical association such as an eQTL, a GWAS hit, fine-mapping or colocalisation"),
    ("prediction", "Prediction", "a model's output, such as QBiC-SELEX or L2G"),
    ("none", "No supporting evidence", "nothing is linked in support"),
)
LEVEL: dict[str, int] = {key: len(RUNGS) - 1 - i for i, (key, _, _) in enumerate(RUNGS)}   # edit 4 ... none 0
RUNG_LABEL: dict[str, str] = {key: label for key, label, _ in RUNGS}
CONTRADICTED_LEVEL = -1
PREDICTS = frozenset({"agrees", "models_disagree", "direction_unstated"})   # inventory states that give the rung
LINKS: tuple[tuple[str, str, str], ...] = (
    ("binding", "TF binding", "Do the alleles differ in binding a transcription factor?"),
    ("activity", "Regulatory activity", "Do the alleles differ in regulatory activity?"),
    ("gene", "Target gene", "Does the variant, or the element it lies in, change a gene's RNA?"),
    ("mediation", "Gene to trait", "Does that gene or process bear on a trait?"),
    ("trait", "Variant to trait", "Is the variant associated with a trait?"),
)
LINK_KEYS: tuple[str, ...] = tuple(key for key, _, _ in LINKS)
LINK_LABEL: dict[str, str] = {key: label for key, label, _ in LINKS}
LINK_LOWER: dict[str, str] = {key: label if label.startswith("TF") else label[0].lower() + label[1:]
                              for key, label, _ in LINKS}
RELATION_LINK: dict[str, str] = {
    "alters_binding": "binding", "alters_regulatory_activity": "activity", "alters_rna": "gene",
    "associated_with_expression": "gene", "regulates": "gene", "contributes_to_trait": "mediation",
    "affects_process": "mediation", "associated_with_trait": "trait", "causal_at_locus": "trait"}
EDIT_CLASSES = frozenset({"perturbation", "dependency_screen"})
ASSAY_CLASSES = frozenset({"reporter_assay", "binding_assay", "occupancy", "synthetic"})
ASSOCIATION_CLASSES = frozenset({"association", "statistical_inference", "clinical_assertion"})
PREDICTION_CLASSES = frozenset({"prediction", "precomputed_prediction"})
FACTOR_KINDS = frozenset({"tf", "tf_group", "complex", "binding_event"})
GENE_KINDS = frozenset({"gene", "transcript"})
CONTEXT_RELATIONS = frozenset({"occupies", "expressed_in"})
OPEN = ("active", "leading", "tied", "deferred")          # hypotheses the view compares (never a rejected one)
APPLICABILITY_ORDER = ("exact", "proxy", "unknown")
MISSING: dict[str, str] = {
    "prediction": "predicted only: no measurement is linked",
    "association": "associated only: no experiment is linked",
    "none": "proposed, with no supporting evidence linked",
}
EXPECTED: frozenset[tuple[str, str]] = frozenset({("trait", "association")})   # the evidence that link can have
NOTE = ("Each link is a separate claim about this variant, read from every hypothesis. A rung names the strongest "
        "kind of evidence linked in support, never its size, and is not a score. Adjacent links are not shown to "
        "cause one another.")
CHOICE_LINKS = ("binding", "gene")                        # the links whose candidates are rival answers
SHARED_LINKS = ("activity", "trait")                      # read once and the same in every chain
CELL_WORDS: dict[str | None, str] = {
    "edit": "edit or perturbation", "assay": "allele-resolved assay", "association": "association",
    "prediction": "predicted", "none": "no supporting evidence", "contested": "contested", None: "no claim"}
CELL_WORDS["contradicted"] = "every candidate is contradicted in scope"
SUPPORT_GROUPS: tuple[tuple[str, tuple[str | None, ...]], ...] = (
    ("Measured", ("edit", "assay")), ("Association only", ("association",)), ("Predicted only", ("prediction",)),
    ("Contested", ("contested",)), ("Claimed without supporting evidence", ("none",)), ("No claim", (None,)),
    ("Every candidate contradicted in scope", ("contradicted",)))
DIFFER_WORDS = {"binding": "transcription factor", "gene": "target gene", "mediation": "gene to trait link"}
EMPTY_NAME = {"binding": "no TF named", "gene": "no target gene named"}
RANKED_SHOWN = 8                                          # chains listed in a report's table before "and n more"
RANK_RULE = ("Code assembles each chain: one transcription factor and one target gene (every pair), the strongest "
             "claims on the regulatory activity and variant to trait links, and the gene to trait claims that name "
             "its gene. Chains are ordered by their weakest link, then their next weakest, "
             "and so on. In that comparison only the kind of evidence counts: the size of z, effect size, ChIP "
             "signal, expression level and the number of records do not enter it. A significant QBiC-SELEX prediction is support: "
             "alone it makes a binding link predicted, and beside a measurement or an association that agrees with "
             "it, it lifts that link above an equal one without it. A factor with no model, or none past the gate, "
             "loses nothing. Chains with the same kinds of evidence are then ordered by two things that only break "
             "ties. First, a strong prediction: the QBiC-SELEX change is in the top 10% of what that TF group "
             "predicts across 21.8 million background variants, and a ChIP-seq peak lies over the variant. Second, "
             "whether a record shows the factor in place: a ChIP-seq peak over the variant, and expression in the "
             "stated context. Each is a yes or a no, never the size of the signal or the level, and a factor "
             "without it stays in the list. Chains still equal tie. Each link is a separate claim: nothing here "
             "shows that one link causes the next.")
PRESENCE: tuple[tuple[str, str], ...] = (("occupies", "a ChIP-seq peak over the variant"),
                                         ("expressed_in", "expression in the stated context"))
BACKS = frozenset({"agrees", "direction_unstated"})        # inventory states that back a measured or associated link
BACKED_STEP = 0.5                                         # above the same rung without it, below the next rung
STRONG_WORDS = ("strong prediction: the QBiC-SELEX change is in the top 10% for this TF group, with a ChIP-seq peak "
                "over the variant")
STRONG_LACKING = "no strong prediction (a change in the top 10% for the TF group, with a ChIP-seq peak over the variant)"


def _num(identifier: str) -> int:
    digits = "".join(ch for ch in identifier if ch.isdigit())
    return int(digits) if digits else 0


def _sign(direction: str) -> int | None:
    """+1 / -1 for a specific direction, 0 for no_change, None for unspecified."""
    return SPECIFIC_DIRECTIONS.get(direction, 0 if direction == "no_change" else None)


def link_rung(strength: str, evidence_class: str) -> str | None:
    """The rung one supports link gives, from the strength the graph computed for it and its evidence class; None
    when it gives none (context, annotation, expression, or an experiment the class matrix holds indirect)."""
    if strength == "direct":
        if evidence_class in EDIT_CLASSES:
            return "edit"
        if evidence_class in ASSAY_CLASSES:
            return "assay"
    if strength in ("direct", "indirect"):
        if evidence_class in ASSOCIATION_CLASSES:
            return "association"
        if strength == "indirect" and evidence_class in PREDICTION_CLASSES:
            return "prediction"
    return None


def _settled(graph: ClaimGraph, claim: Claim) -> bool:
    """Supported in scope, live and with no failed premise (compare.settled without a hypothesis path)."""
    return (claim.assessment == "supported_in_scope" and claim.superseded_by is None
            and claim.dependency_flag == "none")


def _label(graph: ClaimGraph, entity: Entity, short: bool = False) -> str:
    """An entity's name. A TF group is named with its id and its first members. The short form of a named group
    whose members all fit (three at most) leads with them, since they are what a reader recognises: "CEBPA, CEBPB,
    CEBPE (group G035)". A larger group keeps the name a role gave it ("ETS group G003"), which says more than
    its first three members; the long form always has both."""
    if entity.kind != "tf_group":
        return entity.label
    bare = not entity.canonical_id or entity.canonical_id == entity.label
    name = entity.label if bare else f"{entity.label} group {entity.canonical_id}"
    members = [graph.entities[p].label for p in entity.participants]
    if not members:
        return name
    listed = ", ".join(members[:3]) + (f" and {len(members) - 3} more" if len(members) > 3 else "")
    if short and not bare:
        return f"{listed} (group {entity.canonical_id})" if len(members) <= 3 else name
    return f"{name} ({listed})"


class _Inventory:
    """The QBiC-SELEX inventory's Evidence, by group id and by the TFs its models cover."""

    def __init__(self, graph: ClaimGraph):
        self.graph = graph
        self.present = inventory_call(graph) is not None
        self.rows = inventory_table(graph)
        self.by_group = inventory_items(graph)
        self.by_tf: dict[str, list[str]] = {}
        for ids in self.by_group.values():
            for eid in ids:
                for tf in graph.evidence[eid].about_tfs:
                    self.by_tf.setdefault(tf, []).append(eid)

    def items(self, factors: Iterable[Entity]) -> list[str]:
        """The inventory items for these factors: a group's own items, and for a TF the items whose models cover it
        (a CIS-BP-mapped model counts as the TF's own)."""
        found: list[str] = []
        for e in factors:
            if e.kind == "tf_group":
                found += self.by_group.get(str(e.canonical_id), []) or self.by_group.get(e.label, [])
            elif e.kind == "tf":
                found += self.by_tf.get(e.label, [])
        return sorted(dict.fromkeys(found), key=_num)

    def scored(self, factors: Iterable[Entity]) -> list[str]:
        """The ids of the inventory's groups that cover these factors, whether or not they pass the gate."""
        factors = list(factors)
        groups = {str(e.canonical_id) for e in factors if e.kind == "tf_group"} | {
            e.label for e in factors if e.kind == "tf_group"}
        tfs = {e.label for e in factors if e.kind == "tf"}
        found = []
        for row in self.rows:
            members = {m.get("tf") for m in row.get("members") or [] if isinstance(m, dict)}
            if str(row.get("group_id")) in groups or members & tfs:
                found.append(str(row.get("group_id")))
        return found

    def alt_sign(self, evidence_id: str) -> int | None:
        """+1 when the item predicts more binding to the alt allele, -1 to the ref allele, None when unreadable."""
        ev = self.graph.evidence[evidence_id]
        side, sign = self.graph._allele_side(ev.allele), _sign(ev.direction)
        if side is None or not sign:
            return None
        return sign if side == "alt" else -sign


def _alt_direction(graph: ClaimGraph, claim: Claim) -> str:
    """The claim's direction read for the alt allele of the case variant (as stated for a claim that names none)."""
    frame = graph.claim_frame(claim.claim_id)
    return graph._key_direction(claim.direction, claim.effect_allele, frame) if frame == "case" else claim.direction


def _prediction(graph: ClaimGraph, inventory: _Inventory, claim: Claim, factors: list[Entity]) -> dict[str, Any] | None:
    """What the inventory predicts for a binding claim's factors, and how it sits with the claim's direction:
    "agrees", "disagrees" (every item favours the other allele, or the claim says no change), "models_disagree" (the
    group's gate-passing models favour different alleles and one agrees) or "direction_unstated". Without a
    gate-passing item: "below_gate" (models covering the factor were scored and none passes) or "not_covered" (the
    inventory holds no model for it). None when the run has no inventory."""
    if not inventory.present:
        return None
    ids = inventory.items(factors)
    if not ids:
        groups = inventory.scored(factors)
        return {"state": "below_gate" if groups else "not_covered", "items": [], "linked": False, "groups": groups,
                "large": []}
    claimed = _sign(_alt_direction(graph, claim))
    linked = {x.evidence_id for x in claim.evidence_links if x.stance == "supports"}
    items, verdicts, sizes = [], [], []
    for eid in ids:
        ev = graph.evidence[eid]
        predicted = inventory.alt_sign(eid)
        if claimed is None or predicted is None:
            verdict = "unstated"
        elif claimed == 0 or claimed != predicted:
            verdict = "disagrees"
        else:
            verdict = "agrees"
        verdicts.append(verdict)
        items.append({"evidence": eid, "group": ev.data.get("group_id"), "allele": ev.allele,
                      "discordant": ev.data.get("discordant") is True, "tfs": list(ev.about_tfs),
                      "verdict": verdict, "linked": eid in linked})
        sizes.append(ev.data.get("z"))
    if "agrees" in verdicts:
        state = "models_disagree" if "disagrees" in verdicts else "agrees"
    elif "unstated" in verdicts:
        state = "direction_unstated"
    else:
        state = "disagrees"
    return {"state": state, "items": items, "linked": any(i["linked"] for i in items),
            "groups": list(dict.fromkeys(str(i["group"]) for i in items)), "large": _large(items, sizes)}


def _large(items: list[dict[str, Any]], sizes: list[Any]) -> list[str]:
    """The groups whose prediction is large for the group and does not go against the claim. `sizes` holds each
    item's z. A group's value is that of its item with the largest |z| (the background takes a group's value the same
    way), so a group whose strongest model favours the other allele is not counted on the strength of a weaker one.
    Only the group ids leave here: the view never carries a z."""
    top: dict[str, tuple[float, dict[str, Any]]] = {}
    for item, z in zip(items, sizes, strict=True):
        if isinstance(z, (int, float)) and not isinstance(z, bool):
            held = top.get(str(item["group"]))
            if held is None or abs(z) > abs(held[0]):
                top[str(item["group"])] = (float(z), item)
    return [group for group, (z, item) in top.items()
            if item["verdict"] != "disagrees" and in_top_share(group, z) is True]


def _read(graph: ClaimGraph, claim: Claim, inventory: _Inventory, factors: list[Entity]) -> dict[str, Any]:
    """One claim as the chain shows it: its rung from its supports links, the graph's own status beside it, and for a
    binding claim the inventory's prediction."""
    by_rung: dict[str, list[dict[str, Any]]] = {}
    indirect, contradicting = [], []
    for x in claim.evidence_links:
        ev = graph.evidence[x.evidence_id]
        entry = {"id": x.evidence_id, "class": ev.evidence_class, "strength": x.strength,
                 "applicability": x.applicability, "code_applicability": x.code_applicability,
                 "group": ev.independence_group}
        if x.stance == "contradicts" and x.strength == "direct" and x.applicability in ("exact", "proxy"):
            contradicting.append(x.evidence_id)
        if x.stance != "supports" or x.applicability == "different":
            continue
        rung = link_rung(x.strength, ev.evidence_class)
        if rung is None:
            indirect.append({"id": x.evidence_id, "class": ev.evidence_class})
        else:
            by_rung.setdefault(rung, []).append(entry)
    rung = max(by_rung, key=LEVEL.__getitem__, default="none")
    source = "links" if rung != "none" else None
    prediction = _prediction(graph, inventory, claim, factors) if factors else None
    if rung == "none" and prediction and prediction["state"] in PREDICTS:
        rung, source = "prediction", "inventory"
    display = graph.display(claim.claim_id)
    flags = []
    state = "open"
    if claim.assessment == "contradicted_in_scope":
        state = "contradicted"
    elif claim.assessment == "contested" or (contradicting and rung != "none"):
        state = "contested"
        flags.append("direct evidence on both sides" if claim.assessment == "contested" else
                     f"contradicting evidence is linked ({', '.join(contradicting)}) and not assessed")
    elif contradicting:
        flags.append(f"contradicting evidence is linked ({', '.join(contradicting)}) and not assessed")
    if claim.dependency_flag != "none":
        flags.append("a premise it depends on failed")
    frame = graph.claim_frame(claim.claim_id)
    if claim.relation == "regulates" and frame is None:    # element to gene: is it the variant's element?
        recorded = {x.casefold() for x in graph.variant_elements}
        elements = [graph.entities[e] for e in claim.subject_ids if graph.entities[e].kind == "element"]
        if not any({e.label.casefold(), (e.canonical_id or "").casefold()} & recorded for e in elements):
            flags.append("names no variant, and its element is not recorded as containing the variant")
    level = CONTRADICTED_LEVEL if state == "contradicted" else 0 if state == "contested" else LEVEL[rung]
    evidence = by_rung.get(rung, [])
    if source == "inventory":
        evidence = [{"id": i["evidence"], "class": "prediction", "strength": "indirect", "applicability": "exact",
                     "code_applicability": "exact", "group": graph.evidence[i["evidence"]].independence_group}
                    for i in prediction["items"] if i["verdict"] != "disagrees"]
    return {
        "id": claim.claim_id, "relation": claim.relation, "assertion": claim.assertion_text,
        "assessment": claim.assessment, "status": display.status, "basis": display.basis,
        "settled": _settled(graph, claim), "rung": rung, "level": level, "state": state, "source": source,
        "evidence": evidence, "sources": len({e["group"] for e in evidence}),
        "applicability": next((a for a in APPLICABILITY_ORDER if any(e["applicability"] == a for e in evidence)), None),
        # links stored as "unknown" because their proposer said so, although code computed a match: such a claim
        # cannot be assessed as supported, whatever the evidence (graph.link stores code's match now, so only runs
        # saved before that hold them)
        "weakened": [e["id"] for e in evidence if e["applicability"] == "unknown"
                     and e["code_applicability"] in ("exact", "proxy")],
        "indirect": indirect, "contradicting": contradicting, "flags": flags, "prediction": prediction,
        "direction": claim.direction, "effect_allele": claim.effect_allele, "frame": frame,
        "alt_direction": _alt_direction(graph, claim) if frame == "case" else None,
        "context": claim.context_scope.label if claim.context_scope else None,
        "names": [_label(graph, e) for e in factors],
        "hypotheses": [{"id": h.hypothesis_id, "required": claim.claim_id in h.required_claim_ids,
                        "disposition": h.disposition} for h in graph.hypotheses.values()
                       if claim.claim_id in h.claim_ids],
    }


def _context_read(graph: ClaimGraph, claim: Claim) -> dict[str, Any]:
    """One occupies or expressed_in claim as a candidate lists it. `in_place`: a record of a class that can establish
    it (ChIP-seq occupancy, an expression level a role or code judged as expressed) is linked in support, in a
    context that is not a different one. Whether, never how much."""
    display = graph.display(claim.claim_id)
    in_place = any(x.stance == "supports" and x.strength == "direct" and x.applicability != "different"
                   for x in claim.evidence_links)
    return {"id": claim.claim_id, "relation": claim.relation, "status": display.status, "basis": display.basis,
            "assertion": claim.assertion_text, "in_place": in_place}


def _place(graph: ClaimGraph, claim: Claim) -> tuple[str | None, list[str], str]:
    """(link key, candidate entity ids, why not) for a live claim: the link it speaks to and what it names there, or
    (None, [], reason) when it is not a link of the case variant's chain."""
    frame = graph.claim_frame(claim.claim_id)
    link = RELATION_LINK.get(claim.relation)
    if frame == "other":
        return None, [], "about another variant"
    if link is None:
        return None, [], f"relation {claim.relation} is not a link of the chain"
    entities = [(eid, graph.entities[eid]) for eid in claim.subject_ids + claim.object_ids]
    subjects = [graph.entities[eid] for eid in claim.subject_ids]
    others = [eid for eid, e in entities if e.kind != "variant"]
    if link in ("binding", "activity", "trait") and frame != "case":
        return None, [], "names no variant, so it does not say what the alleles do"
    if link == "binding":
        return link, [eid for eid, e in entities if e.kind in FACTOR_KINDS], ""
    if link == "gene":
        if claim.relation != "regulates" and frame != "case":
            return None, [], "names no variant, so it does not say what the alleles do"
        if claim.relation == "regulates" and any(e.kind in FACTOR_KINDS for e in subjects):
            return None, [], "a factor-to-gene link, not a link from the variant or its element"
        genes = [eid for eid, e in entities if e.kind in GENE_KINDS]
        return (link, genes, "") if genes else (None, [], "names no gene")
    if link == "mediation" and frame == "case":           # the variant itself said to bear on a trait or process
        link = "trait"
    if link == "trait":
        traits = [eid for eid, e in entities if e.kind in ("phenotype", "process")]
        return link, traits or others, ""
    return link, others, ""                                # activity, mediation


def _homes(graph: ClaimGraph, placed: Mapping[str, tuple[str, list[str]]]) -> dict[str, str]:
    """For the binding link: each member TF's group, when exactly one group with a binding claim lists it."""
    factors = {eid for link, ids in placed.values() if link == "binding" for eid in ids}
    groups = [eid for eid in factors if graph.entities[eid].kind == "tf_group"]
    home = {}
    for eid in factors:
        if graph.entities[eid].kind == "tf":
            owners = [g for g in groups if eid in graph.entities[g].participants]
            if len(owners) == 1:
                home[eid] = owners[0]
    return home


def _candidate(graph: ClaimGraph, link: str, key: tuple[str, ...], reads: list[dict[str, Any]],
               context: list[dict[str, Any]]) -> dict[str, Any]:
    entities = [graph.entities[eid] for eid in key]
    reads = sorted(reads, key=lambda r: (-r["level"], not r["settled"], _num(r["id"])))
    best = reads[0]
    separator = " → " if link == "mediation" else " + "
    members = [graph.entities[p].label for e in entities if e.kind == "tf_group" for p in e.participants]
    flags = list(dict.fromkeys(f for r in reads if r["level"] == best["level"] for f in r["flags"]))
    # backed: the leading claims are measured or associated, and a gate-passing QBiC-SELEX model favours their allele
    states = {r["prediction"]["state"] for r in reads if r["level"] == best["level"] and r.get("prediction")}
    backed = (link == "binding" and best["level"] > LEVEL["prediction"] and bool(states & BACKS)
              and not states & {"disagrees", "models_disagree"})
    in_place = [relation for relation, _ in PRESENCE if any(c["relation"] == relation and c["in_place"]
                                                            for c in context)]
    # strong: the leading claims' prediction is large for its TF group, and a ChIP-seq peak lies over the variant
    large = (link == "binding" and best["level"] > 0 and
             any(r["prediction"]["large"] for r in reads if r["level"] == best["level"] and r.get("prediction")))
    return {
        "key": "+".join(key), "label": separator.join(_label(graph, e) for e in entities) or "the variant's site",
        "short": separator.join(_label(graph, e, short=True) for e in entities) or "the variant's site",
        "kinds": [e.kind for e in entities], "members": members,
        "rung": best["rung"], "level": best["level"], "state": best["state"], "settled": best["settled"],
        "status": best["status"], "assessment": best["assessment"], "source": best["source"], "backed": backed,
        "claims": reads, "context": context, "in_place": in_place, "flags": flags,
        "large": large, "strong": large and "occupies" in in_place,
        "hypotheses": list(dict.fromkeys(h["id"] for r in reads for h in r["hypotheses"])),
    }


def _hypotheses(graph: ClaimGraph, reads: Mapping[str, dict[str, Any]], link_of: Mapping[str, str],
                label_of: Mapping[str, str]) -> list[dict[str, Any]]:
    rows = []
    for h in graph.hypotheses.values():
        if h.disposition not in OPEN:
            continue
        levels, rungs, claims, names = {}, {}, {}, {}
        for key in LINK_KEYS:
            own = sorted((reads[c] for c in h.claim_ids if link_of.get(c) == key),
                         key=lambda r: (-r["level"], _num(r["id"])))
            claims[key] = [r["id"] for r in own]
            names[key] = list(dict.fromkeys(label_of[r["id"]] for r in own))
            best = own[0]["level"] if own else None
            levels[key] = max(best or 0, 0)                # a contradicted or contested claim counts as none here
            rungs[key] = (None if best is None else "contradicted" if best < 0 else
                          "none" if best == 0 else own[0]["rung"])
        rows.append({"id": h.hypothesis_id, "title": h.title, "disposition": h.disposition, "endpoint": h.endpoint,
                     "levels": levels, "rungs": rungs, "claims": claims, "candidates": names,
                     "covers": [k for k in LINK_KEYS if claims[k]],
                     "strongest": [k for k in LINK_KEYS if levels[k] and levels[k] == max(levels.values())]})
    return rows


def _order(rows: list[dict[str, Any]]) -> dict[str, Any]:
    """Hypotheses compared link by link: `above` lists every pair where one is at least as strong on every link and
    stronger on one; `tiers` peels off the hypotheses nothing ranks above, then the next, and so on; `ties` groups
    identical profiles. No tier is a score: two hypotheses in one tier are tied or not ordered."""
    vectors = {r["id"]: tuple(r["levels"][k] for k in LINK_KEYS) for r in rows}
    ids = list(vectors)

    def above(a: str, b: str) -> bool:
        return vectors[a] != vectors[b] and all(x >= y for x, y in zip(vectors[a], vectors[b], strict=True))

    pairs = [{"upper": a, "lower": b,
              "stronger_at": [k for k, x, y in zip(LINK_KEYS, vectors[a], vectors[b], strict=True) if x > y]}
             for a in ids for b in ids if a != b and above(a, b)]
    tiers, left = [], list(ids)
    while left:
        front = [a for a in left if not any(above(b, a) for b in left)]
        tiers.append(front)
        left = [a for a in left if a not in front]
    groups: dict[tuple[int, ...], list[str]] = {}
    for a in ids:
        groups.setdefault(vectors[a], []).append(a)
    ties = [g for g in groups.values() if len(g) > 1]
    parts: dict[tuple[str, ...], list[str]] = {}            # hypotheses by the links their own claims cover
    for r in rows:
        parts.setdefault(tuple(r["covers"]), []).append(r["id"])
    covers = [set(k) for k in parts]
    disjoint = (len(parts) > 1 and all(covers) and
                all(not a & b for i, a in enumerate(covers) for b in covers[i + 1:]))
    text: list[str] = []
    empty = not any(any(v) for v in vectors.values())
    if len(ids) == 1:
        text.append(f"{ids[0]} is the only open hypothesis, so there is nothing to order.")
    elif len(ids) > 1 and empty:
        text.append("No open hypothesis has supporting evidence on any link, so there is nothing to order.")
    elif len(ids) > 1 and len(tiers) == 1 and len(groups) == 1:
        text.append(f"{', '.join(ids)} tie: the same kind of evidence on every link.")
    elif len(ids) > 1 and len(tiers) == 1:
        strongest = "; ".join(f"{r['id']}: {', '.join(LINK_LOWER[k] for k in r['strongest']) or 'no link'}"
                              for r in rows)
        text.append("No hypothesis is at least as strong as another on every link. Strongest link of each: "
                    f"{strongest}.")
        if disjoint:
            groups_text = "; ".join(f"{', '.join(members)}: {', '.join(LINK_LOWER[k] for k in cover)}"
                                    for cover, members in parts.items())
            text.append(f"They cover different links ({groups_text}), so they read as parts of one route, not as "
                        "rivals; hypotheses that cover the same link compete for it.")
    elif len(ids) > 1:
        text.append(f"Nothing ranks above {', '.join(tiers[0])}. " + " ".join(
            f"Ranked below at least one of {'them' if i == 1 else 'those'}: {', '.join(t)}."
            for i, t in enumerate(tiers[1:], 1)) + " Hypotheses named together are tied or not ordered.")
    if ties and not empty and not (len(tiers) == 1 and len(groups) == 1):
        text.append("Tied (the same kind of evidence on every link): " + "; ".join(" = ".join(g) for g in ties) + ".")
    return {"above": pairs, "tiers": tiers, "ties": ties, "text": text,
            "parts": [{"links": list(cover), "hypotheses": members} for cover, members in parts.items()],
            "parts_of_one_route": disjoint}


def _either(names: list[str], limit: int = 4) -> str:
    """Alternatives as "A", "A or B", "A, B or C"; past the limit, "A, B, C or 5 more"."""
    if len(names) > limit:
        names = [*names[:limit - 1], f"{len(names) - limit + 1} more"]
    return names[0] if len(names) == 1 else f"{', '.join(names[:-1])} or {names[-1]}"


QBIC_STATES = ("agrees", "models_disagree", "direction_unstated", "disagrees", "below_gate", "not_covered")


def _qbic_note(candidate: Mapping[str, Any]) -> str | None:
    """What the QBiC-SELEX inventory says about a binding candidate, as a phrase that follows "QBiC-SELEX",
    whatever evidence ranks the candidate: the allele its gate-passing models favour, or that its models do not
    pass the gate, or that it has none. Read from the candidate's claim that sits best with the inventory. None
    when the run has no inventory. It is shown beside the candidate and never orders a chain."""
    found = [r["prediction"] for r in candidate["claims"] if r.get("prediction")]
    if not found:
        return None
    p = min(found, key=lambda x: QBIC_STATES.index(x["state"]))
    if p["state"] == "below_gate":
        return "its models do not pass the gate"
    if p["state"] == "not_covered":
        return "no model for it"
    shown = [i for i in p["items"] if i["verdict"] != "disagrees"] or p["items"]
    alleles = list(dict.fromkeys(i["allele"] for i in shown if i["allele"]))
    how = {"models_disagree": "; its models disagree about the allele",
           "disagrees": ", against the claim's direction"}.get(p["state"], "")
    return f"predicts more binding to {' or '.join(alleles) or 'an allele'}{how}"


def _cell(key: str, filled: list[dict[str, Any]], claimed: bool, names: list[str] | None = None) -> dict[str, Any]:
    """One link of a whole chain, from the candidates that fill it (all at one level). `kind` is the rung, or
    "contested", or for an empty link None (no claim) or "contradicted" (`claimed`: it has candidates and every one
    is contradicted in scope). `names` names a gene that no target gene claim names."""
    reads = [r for c in filled for r in c["claims"] if r["level"] == c["level"]]
    if not filled:
        kind = "contradicted" if claimed else None
    elif filled[0]["level"] > 0:
        kind = filled[0]["rung"]
    else:
        kind = "contested" if all(c["state"] == "contested" for c in filled) else "none"
    stated = [(r["alt_direction"] if r["frame"] == "case" else r["direction"], r["frame"] == "case") for r in reads]

    def own(candidate: Mapping[str, Any]) -> list[str]:
        """The directions for the alt allele that this candidate's leading claims state."""
        return list(dict.fromkeys(
            r["alt_direction"] for r in candidate["claims"]
            if r["level"] == candidate["level"] and r["frame"] == "case" and r["alt_direction"] in DIRECTION_WORDS))

    backed = bool(filled) and all(c.get("backed") for c in filled)
    level = filled[0]["level"] if filled else 0
    in_place = [relation for relation, _ in PRESENCE if filled and all(relation in c.get("in_place", ())
                                                                       for c in filled)]
    return {
        "link": key, "kind": kind, "level": level, "backed": backed, "step": level + BACKED_STEP * backed,
        "in_place": in_place, "strong": bool(filled) and all(c.get("strong") for c in filled),
        "candidates": [c["key"] for c in filled],
        "names": list(names) if names is not None else [c["short"] for c in filled],
        "settled": any(c["settled"] for c in filled), "claims": [r["id"] for r in reads],
        "alt_directions": list(dict.fromkeys(d for d, case in stated if case and d in DIRECTION_WORDS)),
        "directions": list(dict.fromkeys(d for d, case in stated if not case and d in DIRECTION_WORDS)),
        "contexts": list(dict.fromkeys(r["context"] for r in reads if r["context"])),
        "by_name": [{"name": c["short"], "alt_directions": own(c)} for c in filled],
        "qbic": [{"name": c["short"], "text": note} for c in filled if (note := _qbic_note(c))]
        if key == "binding" else [],
    }


def _merged(cells: list[dict[str, Any]]) -> dict[str, Any]:
    """The same link of several tied chains as one cell: every candidate that fills it in one of them."""
    cells = list({id(c): c for c in cells}.values())      # tied chains share most cells: read each once
    first = cells[0]

    def union(field: str) -> list[Any]:
        return list(dict.fromkeys(x for c in cells for x in c[field]))

    def by_name(field: str) -> list[dict[str, Any]]:
        found: dict[str, dict[str, Any]] = {}
        for c in cells:
            for item in c[field]:
                found.setdefault(item["name"], item)
        return list(found.values())

    return {**first, **{f: union(f) for f in ("candidates", "names", "claims", "alt_directions", "directions",
                                              "contexts")},
            "in_place": [r for r, _ in PRESENCE if all(r in c.get("in_place", ()) for c in cells)],
            "strong": all(c.get("strong") for c in cells),
            "settled": any(c["settled"] for c in cells), "by_name": by_name("by_name"), "qbic": by_name("qbic")}


def support_text(cells: Mapping[str, Mapping[str, Any]]) -> str:
    """A chain's links grouped by the kind of evidence they hold, weakest group last."""
    parts = []
    for title, kinds in SUPPORT_GROUPS:
        keys = [k for k in LINK_KEYS if cells[k]["kind"] in kinds]
        if keys:
            parts.append(f"{title}: {', '.join(LINK_LOWER[k] for k in keys)}.")
    return " ".join(parts)


def _unclaimed(inventory: _Inventory, candidates: list[dict[str, Any]]) -> dict[str, Any]:
    """The gate-passing inventory groups that no binding claim covers, counted: they enter no chain (see the module
    docstring). A group a claim covers is not counted, whatever became of the claim."""
    covered = {str(group) for c in candidates for r in c["claims"] if r.get("prediction")
               for group in r["prediction"]["groups"]}
    groups = [group for group in inventory.by_group if group not in covered]
    return {"count": len(groups), "passing": len(inventory.by_group), "total": len(inventory.rows), "groups": groups}


JOIN_FLAG = "tf_gene_join"         # data flag of an experiment that changed a TF and read out another gene's RNA
JOIN_RULE = (" Last, a chain pairs a TF with a gene, and nothing above says the two belong together. Where an "
             "experiment read from an article changed the chain's TF and saw its gene's RNA or protein change, the "
             "chain comes before an otherwise equal one with no such record. That record shows the TF acting on "
             "the gene, not that it does so through this variant, so it only ever breaks a tie.")


def _symbol(graph: ClaimGraph, name: Any) -> str:
    """A TF or gene name in one form for comparing. Names are resolved to approved symbols when a record is filed
    and when a claim is stated, never here: a saved graph is read without the symbol table, and it must give the
    order the run gave."""
    return str(name).upper()


def tf_gene_joins(graph: ClaimGraph) -> list[tuple[frozenset[str], frozenset[str], str]]:
    """The experiments on file that show a TF acting on a gene, as (TFs, genes, record): the records the fill's
    reader flagged when it filed them (reader.reader_flags). A run of the engine, and a fill read before the flag
    existed, has none, and its chains are ordered exactly as before."""
    out = []
    for ev in graph.evidence.values():
        flag = ev.data.get(JOIN_FLAG)
        if ev.origin == "literature" and isinstance(flag, Mapping) and ev.data.get("unclear_result") is not True:
            out.append((frozenset(_symbol(graph, t) for t in flag.get("tfs") or ()),
                        frozenset(_symbol(graph, g) for g in flag.get("genes") or ()), ev.evidence_id))
    return out


def _whole_chains(graph: ClaimGraph, links: list[dict[str, Any]], inventory: _Inventory) -> dict[str, Any]:
    """Whole chains, ranked (see the module docstring): every pair of a binding candidate and a target gene, with
    the shared links and the gene to trait claims that name the gene, ordered by their weakest link (leximin over
    the five links' steps: the rung, half a step higher for a binding link QBiC-SELEX backs), then by a strong
    prediction on the binding link, then by the records of the factor in place. Competition ranks: chains equal on
    all three share a rank and are counted as tied."""
    by_link = {item["key"]: item for item in links}
    standing = {k: [c for c in by_link[k]["candidates"] if c["level"] >= 0] for k in LINK_KEYS}
    unclaimed = _unclaimed(inventory, by_link["binding"]["candidates"])
    claimed = {k: bool(by_link[k]["candidates"]) for k in LINK_KEYS}
    left_out = [{"link": k, "names": [c["short"] for c in by_link[k]["candidates"] if c["level"] < 0]}
                for k in LINK_KEYS if any(c["level"] < 0 for c in by_link[k]["candidates"])]
    if not any(standing.values()):
        return {"rule": RANK_RULE, "chains": [], "total": 0, "leaders": 0, "headline": None, "differ": [],
                "strip": [], "support": None, "left_out": left_out, "unclaimed": unclaimed}

    def top(candidates: list[dict[str, Any]]) -> list[dict[str, Any]]:
        level = max((c["level"] for c in candidates), default=0)
        return [c for c in candidates if c["level"] == level]

    shared = {k: _cell(k, top(standing[k]), claimed[k]) for k in SHARED_LINKS}
    # a gene whose only variant-to-gene candidates are contradicted in scope gets no chain: that link is broken
    named = {eid for c in by_link["gene"]["candidates"] for eid in c["key"].split("+")}
    loose: dict[str, str] = {}                              # genes that only a gene to trait claim names
    for c in standing["mediation"]:
        for eid, kind in zip(c["key"].split("+"), c["kinds"], strict=True):
            if kind in GENE_KINDS and eid not in named:
                loose.setdefault(eid, graph.entities[eid].label)
    factors: list[dict[str, Any] | None] = list(standing["binding"]) or [None]
    genes: list[tuple[list[str], dict[str, Any] | None, list[str] | None]] = (
        [(c["key"].split("+"), c, None) for c in standing["gene"]]
        + [([eid], None, [label]) for eid, label in sorted(loose.items(), key=lambda kv: _num(kv[0]))]) or [
            ([], None, None)]
    def names_gene(candidate: Mapping[str, Any], gene_ids: list[str]) -> bool:
        return not gene_ids or bool(set(gene_ids) & set(candidate["key"].split("+")))

    # a cell is made once per factor and once per gene, and shared by every chain that holds it
    factor_cells = [_cell("binding", [factor] if factor else [], claimed["binding"]) for factor in factors]
    gene_cells = []
    for gene_ids, gene, loose_name in genes:
        # an empty link is "contradicted" only when claims for it exist and none stands; a gene that only a
        # gene to trait claim names has no target gene claim at all
        onward_claimed = any(names_gene(c, gene_ids) for c in by_link["mediation"]["candidates"])
        gene_cells.append((gene_ids,
                           _cell("gene", [gene] if gene else [], claimed["gene"] and not loose_name, loose_name),
                           _cell("mediation", top([c for c in standing["mediation"] if names_gene(c, gene_ids)]),
                                 onward_claimed)))
    joins = tf_gene_joins(graph)
    chains = []
    for factor, binding in zip(factors, factor_cells, strict=True):
        named_tfs = ({_symbol(graph, m) for m in (factor.get("members") or [factor["label"]])}
                     if factor and joins else set())
        for gene_ids, target, onward in gene_cells:
            cells = {"binding": binding, "activity": shared["activity"], "gene": target, "mediation": onward,
                     "trait": shared["trait"]}
            levels = [cells[k]["step"] for k in LINK_KEYS]
            named_genes = ({_symbol(graph, graph.entities[e].label) for e in gene_ids if e in graph.entities}
                           if joins else set())
            chains.append({
                **({"joined": sorted((eid for tfs, genes, eid in joins if tfs & named_tfs and genes & named_genes),
                                     key=_num)} if joins else {}),
                "title": " → ".join((cells[k]["names"] or [EMPTY_NAME[k]])[0] for k in CHOICE_LINKS),
                "cells": cells, "levels": levels, "strength": sorted(levels), "in_place": binding["in_place"],
                "strong": binding["strong"],
                "weakest": [k for k in LINK_KEYS if cells[k]["step"] == min(levels)],
                "support": support_text(cells),
                "order": ([_num(x) for x in binding["candidates"]], [_num(x) for x in gene_ids])})

    def standing_of(row: Mapping[str, Any]) -> tuple:
        """What ranks a chain: its links weakest first, then a strong prediction on its binding link, then how
        many kinds of record show its factor in place."""
        return ([-x for x in row["strength"]], not row["strong"], -len(row["in_place"]))

    chains.sort(key=lambda r: (*standing_of(r), not r.get("joined"),
                               -sum(c["settled"] for c in r["cells"].values()), r["order"]))
    same: dict[tuple, list[int]] = {}
    for i, row in enumerate(chains):
        same.setdefault((tuple(row["strength"]), row["strong"], len(row["in_place"]), bool(row.get("joined"))),
                        []).append(i)
    for tied in same.values():
        for i in tied:
            chains[i]["rank"], chains[i]["ties"] = tied[0] + 1, len(tied)
            del chains[i]["order"]
    leaders = [r for r in chains if r["rank"] == 1]
    differ = [k for k in LINK_KEYS if len({tuple(r["cells"][k]["names"]) for r in leaders}) > 1]
    if len(leaders) == 1:
        headline = f"Leading chain: {leaders[0]['title']}."
    else:
        ends = [list(dict.fromkeys((r["cells"][k]["names"] or [EMPTY_NAME[k]])[0] for r in leaders))
                for k in CHOICE_LINKS]
        if len(ends[0]) * len(ends[1]) == len(leaders):     # every pair of these TFs and genes: say it once
            titles = f"{_either(ends[0])} → {_either(ends[1])}"
        else:
            titles = _more([r["title"] for r in leaders], 4, "; ")
        headline = f"{len(leaders)} chains tie for first: {titles}."
        if differ:
            where = " and the ".join(DIFFER_WORDS.get(k, LINK_LOWER[k]) for k in differ)
            headline += f" They differ {'only ' if len(differ) == 1 else ''}in the {where}."
    same_kinds = len({tuple(r["cells"][k]["kind"] for k in LINK_KEYS) for r in leaders}) == 1
    out = {
        "rule": RANK_RULE + (JOIN_RULE if joins else ""), "chains": chains, "total": len(chains),
        "leaders": len(leaders), "headline": headline,
        "differ": differ, "strip": [_merged([r["cells"][k] for r in leaders]) for k in LINK_KEYS],
        "support": leaders[0]["support"] if same_kinds else None, "left_out": left_out, "unclaimed": unclaimed,
    }
    joined = leaders[0].get("joined") or []
    if joined:
        # whether the record decided the first place: are there chains equal to it in everything else?
        first = leaders[0]
        beat = sum(1 for r in chains if not r.get("joined") and standing_of(r) == standing_of(first))
        sources = sorted({s for e in joined for s in graph.evidence[e].source_ids[:1]})
        out["join"] = (f"{len(joined)} experiment(s) read from articles changed this chain's TF and saw its gene "
                       f"change ({', '.join(sources)})"
                       + (f", which puts it before {beat} chain(s) that are otherwise its equal." if beat else "."))
    return out


FACTOR_CAP = 12                                           # TFs looked up and listed per run
CONTEXT_CAP = 4                                           # contexts a TF's expression is looked up in


def named_factors(graph: ClaimGraph) -> dict[str, list[Any]]:
    """What the live binding claims about the case variant name, in claim order: `tfs` (symbols named singly),
    `groups` (id and members of each model-sharing group named) and `listed`, the TFs to look up and list: those
    named singly, then group members, up to FACTOR_CAP (a group can have a hundred members)."""
    tfs: list[str] = []
    groups: dict[str, list[str]] = {}
    for c in graph.claims.values():
        if c.superseded_by or c.relation != "alters_binding" or graph.claim_frame(c.claim_id) != "case":
            continue
        for eid in c.subject_ids + c.object_ids:
            e = graph.entities[eid]
            if e.kind == "tf":
                tfs.append(e.label)
            elif e.kind == "tf_group":
                groups.setdefault(str(e.canonical_id or e.label), [graph.entities[m].label for m in e.participants])
    tfs = list(dict.fromkeys(tfs))
    members = [m for ms in groups.values() for m in ms]
    return {"tfs": tfs, "groups": [{"id": gid, "members": ms} for gid, ms in groups.items()],
            "listed": list(dict.fromkeys(tfs + members))[:FACTOR_CAP],
            "not_listed": max(len(set(tfs + members)) - FACTOR_CAP, 0)}


def lookup_contexts(graph: ClaimGraph) -> list[str]:
    """The contexts a TF's expression is looked up in: the supplied ones, the inferred ones, then those the claims
    are stated in when the graph recognised a human biosample or tissue in them (free text such as "in vitro assay"
    has no expression data to look up); up to CONTEXT_CAP, in that order."""
    case = graph.case
    labels = [s.label for s in case.supplied_context] + [c.label for c in case.inferred_candidates
                                                         if c.kind == "context"]
    for c in graph.claims.values():
        scope = c.context_scope
        known = scope is not None and (scope.biosample_kind != "unknown" or bool(scope.tissue))
        if not c.superseded_by and known and scope.species == "human" and scope.label:
            labels.append(scope.label)
    seen: dict[str, str] = {}
    for label in labels:
        if label and label.strip():
            seen.setdefault(label.strip().casefold(), label.strip())
    return list(seen.values())[:CONTEXT_CAP]


def _factor_rows(graph: ClaimGraph) -> dict[str, Any]:
    """One row per listed TF from the tool calls in the graph, whoever asked for them: its QBiC-SELEX models (the
    one with the largest |z| stands for it, as in the inventory), the ChIP-seq survey's record for it, and its
    expression levels. `looked_up` says which of the three kinds of call the graph holds at all."""
    named = named_factors(graph)
    calls = [t for t in graph.tool_calls.values() if t.execution_status == "success"]
    models: dict[str, dict[str, dict[str, Any]]] = {}
    peaks: dict[str, dict[str, Any]] = {}
    levels: dict[str, dict[str, dict[str, Any]]] = {}
    surveyed = detailed = expressed = False
    for t in calls:
        params = t.query_parameters
        if t.tool_name == "qbic_tf_detail":
            detailed = True
            for o in t.observations:
                if o.get("record") == "model":
                    for tf in o.get("maps_to") or []:
                        models.setdefault(str(tf), {})[str(o.get("model"))] = o
        elif t.tool_name == "chip_occupancy" and not params.get("tf") and not params.get("biosample"):
            surveyed = True
            for o in t.observations:
                if o.get("record") == "factor" and o.get("tf"):
                    peaks[str(o["tf"]).upper()] = o
        elif t.tool_name == "tf_expression":
            expressed = True
            for o in t.observations:
                if o.get("record") == "expression" and o.get("tf") and o.get("tpm") is not None:
                    levels.setdefault(str(o["tf"]).upper(), {})[str(o.get("source_context") or o.get("context"))] = o
    rows = []
    for tf in named["listed"]:
        own = [m for m in models.get(tf, {}).values() if m.get("status") == "ok" and m.get("z") is not None]
        best = min(own, key=lambda m: (-abs(m["z"]), str(m.get("model"))), default=None)
        peak = peaks.get(tf.upper())
        rows.append({
            "tf": tf,
            "qbic": None if not detailed else {
                "models": len(models.get(tf, {})), "passing": sum(1 for m in own if m.get("passes_gate")),
                "best": None if best is None else {
                    "model": best.get("model"), "binds_more": best.get("binds_more"), "z": best.get("z"),
                    "effect": best.get("effect"), "passes_gate": bool(best.get("passes_gate")),
                    "site_strength": best.get("site_strength")}},
            "chip": None if not surveyed else {
                "experiments": int(peak.get("experiments") or 0) if peak else 0,
                "biosamples": list(peak.get("biosamples") or []) if peak else []},
            "expression": None if not expressed else [
                {"context": str(o.get("source") or o.get("source_context") or o.get("context")), "tpm": o.get("tpm")}
                for o in levels.get(tf.upper(), {}).values()],
        })
    # the survey alone is no lookup of these factors: a run that only surveyed (the code-only fill, which states
    # what the survey shows as claims) has no rows to list here
    return {"rows": rows if (detailed or expressed) else [], "not_listed": named["not_listed"],
            "looked_up": {"qbic": detailed, "chip": surveyed, "expression": expressed}}


def chain_view(graph: ClaimGraph) -> dict[str, Any]:
    """The chain as JSON-native data, deterministic for a graph: the ladder, the links with their ranked candidates,
    the whole chains in rank order, the location, the open hypotheses link by link with their order, what is missing
    and the claims not placed."""
    inventory = _Inventory(graph)
    live = [c for c in graph.claims.values() if not c.superseded_by]
    placed: dict[str, tuple[str, list[str]]] = {}
    unplaced, location, context_claims = [], [], []
    for c in live:
        if c.relation == "overlaps":
            location.append(c)
        elif c.relation in CONTEXT_RELATIONS:
            context_claims.append(c)
        else:
            link, ids, why = _place(graph, c)
            if link is None:
                unplaced.append({"id": c.claim_id, "relation": c.relation, "why": why})
            else:
                placed[c.claim_id] = (link, ids)
    home = _homes(graph, placed)
    reads: dict[str, dict[str, Any]] = {}
    grouped: dict[str, dict[tuple[str, ...], list[str]]] = {key: {} for key in LINK_KEYS}
    for cid, (link, ids) in placed.items():
        claim = graph.claims[cid]
        factors = [graph.entities[e] for e in ids] if link == "binding" else []
        reads[cid] = _read(graph, claim, inventory, factors)
        merged = [home.get(e, e) for e in ids] if link == "binding" else ids
        key = tuple(merged) if link == "mediation" else tuple(sorted(dict.fromkeys(merged), key=_num))
        grouped[link].setdefault(key, []).append(cid)

    context_reads = {c.claim_id: _context_read(graph, c) for c in context_claims}

    def factor_context(key: tuple[str, ...]) -> list[dict[str, Any]]:
        """occupies and expressed_in claims naming this candidate's factor or one of its members: they give no rung,
        and one with a record linked in support shows the factor in place."""
        names = set(key) | {p for e in key for p in graph.entities[e].participants}
        return [context_reads[c.claim_id] for c in context_claims if names & set(c.subject_ids + c.object_ids)]

    links, label_of = [], {}
    for key, label, question in LINKS:
        candidates = [_candidate(graph, key, k, [reads[c] for c in cids], factor_context(k) if key == "binding" else [])
                      for k, cids in grouped[key].items()]
        candidates.sort(key=lambda c: (-c["level"], not c["settled"], [_num(x) for x in c["key"].split("+")]))
        for cand in candidates:
            for r in cand["claims"]:
                label_of[r["id"]] = cand["short"]
        level = max((c["level"] for c in candidates), default=None)
        top = [c for c in candidates if c["level"] == level and level > 0] if level is not None else []
        rung = (None if level is None else "contradicted" if level < 0 else
                top[0]["rung"] if top else "none")
        links.append({"key": key, "label": label, "question": question, "rung": rung,
                      "rung_label": "No claim" if rung is None else "Contradicted in scope" if rung == "contradicted"
                      else RUNG_LABEL[rung],
                      "measured": rung in ("edit", "assay"), "top": [c["key"] for c in top],
                      "tied": len(top) > 1, "candidates": candidates})
    link_of = {cid: link for cid, (link, _) in placed.items()}
    hypotheses = _hypotheses(graph, reads, link_of, label_of)
    missing = []
    for item in links:
        if item["rung"] is None:
            missing.append({"link": item["key"], "text": f"{item['label']}: no claim proposes this link."})
        elif item["rung"] == "contradicted":
            missing.append({"link": item["key"], "text": f"{item['label']}: every candidate is contradicted in scope."})
        elif item["rung"] in MISSING and (item["key"], item["rung"]) not in EXPECTED:
            missing.append({"link": item["key"], "text": f"{item['label']}: {MISSING[item['rung']]}."})
    held = [item for item in links if item["rung"] not in (None, "none", "contradicted")]
    return {
        "format": CHAIN_FORMAT,
        "rungs": [{"key": key, "label": label, "meaning": meaning} for key, label, meaning in RUNGS],
        "location": {"found_by_code": list(graph.variant_elements),
                     "claims": [{"id": c.claim_id, "status": graph.display(c.claim_id).status,
                                 "elements": [_label(graph, graph.entities[e]) for e in c.subject_ids + c.object_ids
                                              if graph.entities[e].kind == "element"]} for c in location]},
        "links": links,
        "placed": len(placed),
        "links_with_evidence": [item["key"] for item in held],
        "links_measured": [item["key"] for item in links if item["measured"]],
        "summary": " · ".join(summary_part(item) for item in links),
        "ranked": _whole_chains(graph, links, inventory),
        "factors": _factor_rows(graph),
        "missing": missing,
        "hypotheses": hypotheses,
        "order": _order(hypotheses),
        "unplaced": unplaced,
        "note": NOTE,
    }


# --- plain text, for the report's two formats (each escapes it its own way) ----------------------------------------------

DIRECTION_WORDS = {"increases": "↑", "decreases": "↓", "creates": "creates", "abolishes": "abolishes",
                   "no_change": "no change"}
STATUS_WORDS = {"supported": "supported in scope", "predicted": "predicted", "associated": "associated",
                "contested": "contested", "contradicted": "contradicted in scope", "unresolved": "not settled"}
MAX_SHOWN = 6


def _more(values: list[str], limit: int = MAX_SHOWN, sep: str = ", ") -> str:
    return sep.join(values[:limit]) + (f"{sep}and {len(values) - limit} more" if len(values) > limit else "")


def summary_part(link: Mapping[str, Any]) -> str:
    """One link in the one-line summary: its strongest kind of evidence and the candidates that hold it."""
    by_key = {c["key"]: c for c in link["candidates"]}
    names = [by_key[k]["short"] for k in link["top"]]
    if link["rung"] is None:
        return f"{link['label']}: no claim"
    if not names:
        return f"{link['label']}: {link['rung_label'].lower()}"
    return f"{link['label']}: {link['rung_label'].lower()} ({_more(names, 4)}{'; tied' if link['tied'] else ''})"


def claim_text(read: Mapping[str, Any], alt: str | None = None, candidate: str | None = None) -> str:
    """One claim of a candidate: its id (with the factor it names, when that is a member of the candidate's group),
    the graph's status, its direction for the alt allele, and the evidence that gives its rung."""
    status = STATUS_WORDS.get(read["status"], read["status"])
    if read["status"] == "unresolved" and read["assessment"] == "unassessed":
        status = "not assessed"
    named = f" ({', '.join(read['names'])})" if read["names"] and read["names"] != [candidate] else ""
    parts = [f"{read['id']}{named} {status}"]
    direction = read["alt_direction"] if read["frame"] == "case" else read["direction"]
    word = DIRECTION_WORDS.get(direction or "")
    if word:
        parts.append(f"{alt} {word}" if read["frame"] == "case" and alt else word)
    elif read["frame"] == "case":
        parts.append("direction not stated")
    if read["source"] == "links" and read["evidence"]:
        classes = sorted({e["class"] for e in read["evidence"]})
        if read["applicability"] in ("exact", None):
            note = ""
        elif read["applicability"] == "unknown" and read["weakened"]:
            note = "; its proposer declared the context match unknown, though code computed a match"
        else:
            note = f"; applicability {read['applicability']}"
        parts.append(f"{', '.join(classes)}: {_more([e['id'] for e in read['evidence']], 3)}{note}")
    if read["context"]:
        parts.append(f"context: {read['context']}")
    return ", ".join(parts) + (f" [{'; '.join(read['flags'])}]" if read["flags"] else "")


def prediction_text(read: Mapping[str, Any]) -> str | None:
    """What the QBiC-SELEX inventory predicts for a binding claim's factors, as one phrase; None without one."""
    p = read.get("prediction")
    if not p:
        return None
    if p["state"] == "below_gate":
        return f"QBiC-SELEX scored models covering it ({_more(p['groups'], 3)}); none passes the gate"
    if p["state"] == "not_covered":
        return "the QBiC-SELEX inventory holds no model covering it"
    shown = [i for i in p["items"] if i["verdict"] != "disagrees"] or p["items"]
    alleles = list(dict.fromkeys(i["allele"] for i in shown if i["allele"]))
    ids = _more([i["evidence"] for i in shown], 3)
    how = {"agrees": "", "models_disagree": "; the group's models disagree about the allele",
           "direction_unstated": "", "disagrees": "; this opposes the claim's direction"}[p["state"]]
    linked = "" if p["linked"] else ", read from the inventory, not linked by a role"
    return f"QBiC-SELEX predicts more binding to {' or '.join(alleles) or 'an allele'} ({ids}{linked}){how}"


def candidate_text(candidate: Mapping[str, Any], alt: str | None = None) -> str:
    """A candidate as one line: its name, its claims and, for a factor, the inventory's prediction and its context."""
    parts = [claim_text(r, alt, candidate["label"]) for r in candidate["claims"][:3]]
    if len(candidate["claims"]) > 3:
        parts.append(f"and {len(candidate['claims']) - 3} more claims")
    predictions = list(dict.fromkeys(t for r in candidate["claims"] if (t := prediction_text(r))))
    parts += predictions[:1]
    indirect = sorted({f"{e['id']} {e['class']}" for r in candidate["claims"] for e in r["indirect"]}, key=_num)
    if indirect:
        parts.append(f"indirect, no rung: {_more(indirect, 3)}")
    if candidate["context"]:
        parts.append("context, never ranked: " + _more(
            [f"{c['id']} {c['relation'].replace('_', ' ')} ({STATUS_WORDS.get(c['status'], c['status'])})"
             for c in candidate["context"]], 3))
    extra = [f for f in candidate["flags"] if not any(f in p for p in parts)]
    return f"{candidate['label']}: " + "; ".join(parts) + (f" [{'; '.join(extra)}]" if extra else "")


def _standing(candidate: Mapping[str, Any]) -> str:
    """Where a candidate that does not lead its link stands, in a few words."""
    if candidate["level"] < 0:
        return "contradicted in scope"
    if candidate["state"] == "contested":
        return "contested"
    return RUNG_LABEL[candidate["rung"]].lower()


def chain_rows(view: Mapping[str, Any], alt: str | None = None) -> list[dict[str, Any]]:
    """The chain table, one row per link: its label, rung key and label, the leading candidates and the others (each
    as plain text)."""
    rows = []
    for link in view["links"]:
        top = set(link["top"])
        leading = [candidate_text(c, alt) for c in link["candidates"] if c["key"] in top]
        others = [f"{c['label']} ({_standing(c)})" for c in link["candidates"] if c["key"] not in top]
        rows.append({"key": link["key"], "label": link["label"], "question": link["question"],
                     "rung": link["rung"], "rung_label": link["rung_label"], "tied": link["tied"],
                     "leading": leading[:MAX_SHOWN], "leading_more": max(len(leading) - MAX_SHOWN, 0),
                     "others": _more(others, 8, "; ")})
    return rows


def _short(text: str, limit: int = 48) -> str:
    return text if len(text) <= limit else text[:limit - 1].rstrip() + "…"


def cell_names(cell: Mapping[str, Any], limit: int = 3) -> str:
    """Who fills a link of a whole chain: its candidates, marked as tied when there are several; empty for none."""
    return _more(list(cell["names"]), limit) + (" (tied)" if len(cell["names"]) > 1 else "")


def cell_kind(cell: Mapping[str, Any]) -> str:
    """The kind of evidence that holds a link of a whole chain, in words; a predicted binding link names its model."""
    text = CELL_WORDS[cell["kind"]]
    if cell["kind"] == "prediction" and cell["link"] == "binding":
        return text + " by QBiC-SELEX"
    return text + " + QBiC-SELEX prediction" if cell["backed"] else text


def cell_detail(cell: Mapping[str, Any], alt: str | None = None, names: int = 4) -> tuple[str, str]:
    """What a link's claims add to the kind of evidence, as (direction, context): the direction for the alt allele
    (a gene to trait claim's direction is the gene's, so it names no allele) and the context the claims are stated
    in. Either is "" when not stated; an empty link has neither."""
    if cell["kind"] in (None, "contradicted"):
        return "", ""
    def mark(direction: str) -> str:
        return f"{alt} {DIRECTION_WORDS[direction]}" if alt else DIRECTION_WORDS[direction]

    marks = [mark(d) for d in cell["alt_directions"]]
    if len({tuple(x["alt_directions"]) for x in cell["by_name"]}) > 1:      # tied candidates that differ: say whose
        marks = [_more([f"{_short(x['name'])} {' / '.join(mark(d) for d in x['alt_directions'])}"
                        for x in cell["by_name"] if x["alt_directions"]], names, "; ")]
    if cell["link"] == "mediation":
        marks += [DIRECTION_WORDS[d] for d in cell["directions"]]
    context = ""
    if cell["contexts"]:
        more = f" and {len(cell['contexts']) - 1} more" if len(cell["contexts"]) > 1 else ""
        context = _short(cell["contexts"][0]) + more
    return " / ".join(marks[:2]), context


def cell_qbic(cell: Mapping[str, Any]) -> str:
    """What QBiC-SELEX says about a binding link's candidates, beside whatever evidence holds the link: "" for
    another link, for a run without an inventory, and for a link the prediction itself holds (its kind says so)."""
    if cell["kind"] == "prediction":
        return ""
    notes = cell["qbic"]
    if not notes:
        return ""
    if len(notes) == 1:
        text = notes[0]["text"]
        return f"QBiC-SELEX {text}" if text.startswith("predicts") else f"QBiC-SELEX: {text}"
    return "QBiC-SELEX: " + "; ".join(f"{n['name']}, {n['text']}" for n in notes)


def cell_presence(cell: Mapping[str, Any]) -> str:
    """What is on record that a binding link's factor is in place, as a phrase; "" when nothing is, and for any
    other link. It names the kind of record, never its size."""
    found = [text for relation, text in PRESENCE if relation in cell.get("in_place", ())]
    return "in place: " + " and ".join(found) if found and cell["link"] == "binding" else ""


def cell_strong(cell: Mapping[str, Any]) -> str:
    """That a binding link holds a strong prediction, as a phrase; "" otherwise. A yes or a no: no z is shown."""
    return STRONG_WORDS if cell.get("strong") and cell["link"] == "binding" else ""


def cell_evidence(cell: Mapping[str, Any], alt: str | None = None) -> str:
    """What holds a link of a whole chain, as one phrase: "association, T ↑ (Liver)"; a binding link adds what
    QBiC-SELEX says about its candidates and what shows them in place."""
    direction, context = cell_detail(cell, alt)
    text = cell_kind(cell) + (f", {direction}" if direction else "") + (f" ({context})" if context else "")
    return text + "".join(f"; {note}" for note in (cell_qbic(cell), cell_strong(cell), cell_presence(cell)) if note)


def cell_text(cell: Mapping[str, Any], alt: str | None = None) -> str:
    """A link of a whole chain as one phrase: who fills it, then what holds it."""
    names = cell_names(cell)
    return f"{names}: {cell_evidence(cell, alt)}" if names else cell_evidence(cell, alt)


def weakest_text(row: Mapping[str, Any]) -> str:
    """A chain's weakest links, each with what it holds."""
    return "; ".join(f"{LINK_LOWER[k]} ({CELL_WORDS[row['cells'][k]['kind']]})" for k in row["weakest"])


RANKED_HEADERS = ["Rank", "Chain", "TF binding", "Target gene", "Gene to trait", "Against the leading chain"]
STRIP_HEADERS = ["Link", "Filled by", "Kind of evidence"]
SHARED_NOTE = ("Regulatory activity and variant to trait are the same in every chain, so they are given once, in the "
               "link-by-link view of the leading chain.")


def versus_text(row: Mapping[str, Any], leader: Mapping[str, Any]) -> str:
    """Where a chain stands against the leading one: the links it is weaker on, and any it is stronger on."""
    if row["rank"] == 1:
        return "tied for first" if row["ties"] > 1 else "leads"
    pairs = list(zip(LINK_KEYS, row["levels"], leader["levels"], strict=True))
    weaker = [LINK_LOWER[k] + (" (no QBiC-SELEX prediction in support)" if int(mine) == int(lead) else "")
              for k, mine, lead in pairs if mine < lead]
    stronger = [LINK_LOWER[k] for k, mine, lead in pairs if mine > lead]
    if not weaker and not stronger:            # equal on every link: only the two tie-breakers differ
        same = "the same kinds of evidence on every link"
        if leader["cells"]["binding"].get("strong") and not row["cells"]["binding"].get("strong"):
            return f"{same}; {STRONG_LACKING}"
        lacking = [text for relation, text in PRESENCE
                   if relation in leader.get("in_place", ()) and relation not in row.get("in_place", ())]
        return f"{same}; no record of " + " or of ".join(lacking) if lacking else same
    return "; ".join(part for part in (f"weaker on {', '.join(weaker)}" if weaker else "",
                                       f"stronger on {', '.join(stronger)}" if stronger else "") if part)


def ranked_rows(view: Mapping[str, Any], alt: str | None = None, limit: int = RANKED_SHOWN) -> list[list[str]]:
    """The ranked chains as plain text cells (RANKED_HEADERS): rank ("=" marks a tie), the chain's TF and gene, what
    holds the three links that can differ between chains, and where it stands against the first chain. The two
    shared links are not repeated in every row (strip_rows gives them once)."""
    chains = view["ranked"]["chains"]
    rows = []
    for r in chains[:limit]:
        cells = r["cells"]
        onward = cell_text(cells["mediation"], alt) if cells["mediation"]["names"] else cell_evidence(cells["mediation"])
        rows.append([f"{r['rank']}{'=' if r['ties'] > 1 else ''}", r["title"], cell_evidence(cells["binding"], alt),
                     cell_evidence(cells["gene"], alt), onward, versus_text(r, chains[0])])
    return rows


def ranked_more(view: Mapping[str, Any], limit: int = RANKED_SHOWN) -> str | None:
    """What the table leaves out: how many chains, and how many of them tie with the last one shown."""
    ranked = view["ranked"]
    if "more" in ranked:                       # a view cut for a report (for_report) says it once, before the cut
        return ranked["more"]
    chains = ranked["chains"]
    if len(chains) <= limit:
        return None
    tied = sum(1 for r in chains[limit:] if r["rank"] == chains[limit - 1]["rank"])
    rest = len(chains) - limit
    return (f"{rest} more chain{'s' if rest != 1 else ''} not shown"
            + (f", {tied} of them tied at rank {chains[limit - 1]['rank']}" if tied else "") + ".")


def for_report(view: Mapping[str, Any], limit: int = RANKED_SHOWN) -> dict[str, Any]:
    """The view as a report embeds it: the ranked chains cut to the rows a report lists (their number and the ties
    stay in `total`, `leaders` and `more`). Code alone can state a chain for every pair of several hundred TF groups
    and a few dozen genes, and each row repeats the cells it shares with the others, so the whole list would be
    hundreds of megabytes of the same text."""
    ranked = view["ranked"]
    return {**view, "ranked": {**ranked, "chains": ranked["chains"][:limit], "more": ranked_more(view, limit)}}


def strip_names(cell: Mapping[str, Any]) -> str:
    """Who fills a link, for the one-screen strip. The rival answers (TF, target gene) are all named, up to four.
    A link that is the same in every chain names its first candidate and counts the rest: the table of links below
    lists them."""
    if cell["link"] in CHOICE_LINKS or len(cell["names"]) < 2:
        return cell_names(cell, 4)
    return f"{_short(cell['names'][0], 64)} and {len(cell['names']) - 1} more"


def strip_rows(view: Mapping[str, Any], alt: str | None = None) -> list[dict[str, Any]]:
    """The leading chain, or the chains tied for first, link by link: the link's label, who fills it, the kind of
    evidence as text, and the kind's key (for a badge). Kept short enough to read on one screen."""
    return [{"key": cell["link"], "label": LINK_LABEL[cell["link"]], "names": strip_names(cell),
             "kind": cell["kind"], "kind_text": cell_kind(cell),
             "detail": [part for part in (*cell_detail(cell, alt, 4 if cell["link"] in CHOICE_LINKS else 2),
                                          cell_qbic(cell), cell_presence(cell)) if part],
             "evidence": cell_evidence(cell, alt)} for cell in view["ranked"]["strip"]]


FACTOR_HEADERS = ["Transcription factor", "QBiC-SELEX", "ChIP-seq over the variant", "Expression"]
FACTOR_NOTE = ("Looked up by code for every transcription factor a binding claim names, after the run's decision. "
               "A row here orders nothing by itself, and a missing peak or a low level removes nothing: only a "
               "claim that the factor is in place, with a record linked to it, can break a tie between chains that "
               "are otherwise equal. A ChIP-seq peak is occupancy of the element, not an allele-specific readout, "
               "and no peak here is not evidence of absence. Site strength is the percentile of each allele's "
               "summed score among random 21-mers.")


def factor_rows(view: Mapping[str, Any], ref: str | None = None, alt: str | None = None) -> list[list[str]]:
    """The factor lookups as plain text cells (FACTOR_HEADERS), one row per TF."""
    rows = []
    for r in view["factors"]["rows"]:
        q, c, x = r["qbic"], r["chip"], r["expression"]
        if q is None:
            qbic = "not looked up"
        elif not q["models"]:
            qbic = "no model"
        elif q["best"] is None:
            qbic = f"{q['models']} model{'s' if q['models'] != 1 else ''}, none scored"
        else:
            b = q["best"]
            allele = {"alt": alt, "ref": ref}.get(b["binds_more"]) or b["binds_more"] or "neither"
            site = b.get("site_strength") or {}
            qbic = (f"{q['passing']} of {q['models']} model{'s' if q['models'] != 1 else ''} past the gate; largest "
                    f"|z|: more binding to {allele} (z {b['z']:+.1f}, effect {b['effect']:+.2f})")
            if site.get("ref") is not None and site.get("alt") is not None:
                qbic += f"; site strength {ref or 'ref'} {site['ref']:g} → {alt or 'alt'} {site['alt']:g}"
        if c is None:
            chip = "not looked up"
        elif not c["experiments"]:
            chip = "no peak in ENCODE or ReMap"
        else:
            chip = (f"peak in {c['experiments']} experiment{'s' if c['experiments'] != 1 else ''}: "
                    f"{_more(c['biosamples'], 4)}")
        if x is None:
            expression = "not looked up"
        elif not x:
            expression = "no level for the contexts looked up"
        else:
            expression = "; ".join(f"{e['tpm']:g} TPM, {e['context']}" for e in x[:CONTEXT_CAP])
        rows.append([r["tf"], qbic, chip, expression])
    return rows


def unclaimed_text(view: Mapping[str, Any]) -> str | None:
    """The gate-passing groups that are in no chain, as one sentence; None when there are none."""
    u = view["ranked"]["unclaimed"]
    if not u["count"]:
        return None
    return (f"QBiC-SELEX also predicts a significant change for {u['count']} TF group{'s' if u['count'] != 1 else ''} "
            f"that no binding claim names ({u['passing']} of {u['total']} scored groups pass its gate). They are in "
            "no chain and are listed in the QBiC-SELEX inventory.")


def hypothesis_rows(view: Mapping[str, Any]) -> list[list[str]]:
    """The open hypotheses link by link, as plain text cells: id and title, disposition, then one cell per link."""
    rows = []
    for h in view["hypotheses"]:
        cells = [f"{h['id']} {h['title']}", h["disposition"]]
        for key in LINK_KEYS:
            rung = h["rungs"][key]
            if rung is None:
                cells.append("–")
            else:
                label = "contradicted" if rung == "contradicted" else RUNG_LABEL[rung].lower()
                cells.append(f"{label}: {_more(h['candidates'][key], 3)} ({', '.join(h['claims'][key][:4])})")
        rows.append(cells)
    return rows
