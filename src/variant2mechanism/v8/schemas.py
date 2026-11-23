"""Model output schemas for v8, and the code checks the schemas cannot express. No probabilities and no null chain:
code ranks the chains and decides the verdict."""

from typing import Literal

from pydantic import BaseModel

from ..agent.schemas import STEPS, Check, LinkGrade, SchemaCheckError, Step


class LinkV8(BaseModel):
    step: Step
    claim: str
    evidence_ids: list[str]


class ChainV8(BaseModel):
    id: str
    title: str
    family_id: str                      # F1, F2, ... from the family table
    tf: str
    member_reason: str                  # why a member other than the one code named; empty otherwise
    allele_binding_more: Literal["ref", "alt"]
    element: str
    target_gene: str
    cell_type: str
    links: list[LinkV8]
    predictions: list[str]
    falsified_if: list[str]


class ChainsV8(BaseModel):
    chains: list[ChainV8]


class Elimination(BaseModel):
    hypothesis_id: str
    evidence_ids: list[str]
    reason: str


class CritiqueV8(BaseModel):
    grades: list[LinkGrade]
    problems: list[str]
    eliminations: list[Elimination]
    checks: list[Check]
    next_experiment: str


class SingleChain(BaseModel):
    tf: str
    allele_binding_more: Literal["ref", "alt"]
    target_gene: str
    reason: str


class SingleOut(BaseModel):
    chains: list[SingleChain]


def unknown_ids(cited: list[str], known: set[str] | None) -> list[str]:
    """Cited evidence IDs that are not in the ledger (none when `known` is None: the check is off)."""
    return [] if known is None else sorted({i for i in cited if i not in known})


def cites(what: str, cited: list[str], known: set[str] | None) -> str | None:
    bad = unknown_ids(cited, known)
    return f"{what} cites {', '.join(bad[:6])}, which are not evidence IDs; cite only the IDs listed" if bad else None


def check_chains(chains: list[ChainV8], families: list[dict], want: int, requested: set[str] | None = None,
                 known: set[str] | None = None) -> list[ChainV8]:
    """One chain per family, `want` of them (or as many as there are families), each naming a member of its family,
    with the five links once each in order, citing only evidence IDs in `known` (the ledger's). A chain for a family
    outside `requested` (the families asked for) replaces one of them, and its member_reason, which says why, is kept
    even when it names that family's code member."""
    problems = []
    by_fid = {f["fid"]: f for f in families}
    need = min(want, len(families))
    if not need <= len(chains) <= max(need, 5):
        problems.append(f"give {need} chains (one per family asked for), not {len(chains)}")
    ids = [c.id for c in chains]
    if len(set(ids)) != len(ids):
        problems.append(f"chain ids must be unique; got {ids}")
    fids = [c.family_id for c in chains]
    if len(set(fids)) != len(fids):
        problems.append(f"one chain per family; got {fids}")
    tfs = [c.tf.strip().upper() for c in chains]
    if len(set(tfs)) != len(tfs):
        problems.append(f"each chain names a different TF; got {tfs}")
    for c in chains:
        gene = c.target_gene.strip()
        if not gene or " " in gene or len(gene) > 30:
            problems.append(f"{c.id}: target_gene must be one gene symbol; put the reasoning in the gene link's "
                            f"claim; got {gene[:60]!r}")
        f = by_fid.get(c.family_id)
        if f is None:
            problems.append(f"{c.id}: family_id must be one of {sorted(by_fid)}; got {c.family_id!r}")
            continue
        members = {m["tf"].upper() for m in f["members"]}
        if c.tf.strip().upper() not in members:
            problems.append(f"{c.id}: {c.tf!r} is not a member of {c.family_id}; members: {sorted(members)[:12]}")
        elif c.tf.strip().upper() != f["named"].upper() and not c.member_reason.strip():
            problems.append(f"{c.id}: code named {f['named']} for {c.family_id}; give member_reason for {c.tf}")
        steps = [lk.step for lk in c.links]
        if steps != STEPS:
            problems.append(f"{c.id}: links must be the five steps once each in order {STEPS}; got {steps}")
        bad = cites(c.id, [i for lk in c.links for i in lk.evidence_ids], known)
        if bad:
            problems.append(bad)
    if problems:
        raise SchemaCheckError("; ".join(problems))
    for c in chains:
        c.tf, c.target_gene = c.tf.strip().upper(), c.target_gene.strip()
        asked = requested is None or c.family_id in requested
        if asked and c.tf == by_fid[c.family_id]["named"].upper():
            c.member_reason = ""                 # no switch, so no reason to keep
    return chains


def check_grades(grades: list[LinkGrade], chains: list[ChainV8]) -> list[LinkGrade]:
    need = {(c.id, lk.step) for c in chains for lk in c.links}
    got = {(g.hypothesis_id, g.step) for g in grades}
    missing = need - got
    if missing:
        raise SchemaCheckError(f"grade every link; missing {sorted(missing)[:8]}")
    seen, out = set(), []
    for g in grades:
        k = (g.hypothesis_id, g.step)
        if k in need and k not in seen:
            seen.add(k)
            out.append(g)
    return out


def check_critique(out: CritiqueV8, chains: list[ChainV8], known: set[str] | None = None) -> CritiqueV8:
    """Every link graded once, and eliminations citing only evidence IDs in `known`."""
    grades = check_grades(out.grades, chains)
    bad = cites("an elimination", [i for e in out.eliminations for i in e.evidence_ids], known)
    if bad:
        raise SchemaCheckError(bad)
    return out.model_copy(update={"grades": grades})


def check_cited(out, known: set[str] | None):
    """A comparison (or any output with `evidence_ids`) citing only evidence IDs in `known`."""
    bad = cites("the comparison", out.evidence_ids, known)
    if bad:
        raise SchemaCheckError(bad)
    return out
