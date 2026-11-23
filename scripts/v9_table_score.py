"""Score the chain tables of a saved fill suite against the gold specification.

    python scripts/v9_table_score.py --runs runs/<suite> --out runs/score_<name> --freeze eval/fill_freeze_<date>.json

The rule was fixed on 23 November 2026, before any table of the fill was scored, and it is all here.

What is scored. A case's answer is the set of chains that share the first rank of its table. Chains are scored by
what they name, with the gold specification's own rules for a name (eval/v9_gold_spec.json, "rules", written before
the fill existed):

    TF, as the member    a first-ranked chain names the gold TF itself; naming its model-sharing group is not this
    TF, as its group     a first-ranked chain names a QBiC-SELEX group that holds the gold TF, or a TF of such a group
    TF, as its family    a first-ranked chain names a TF of the gold TF's DNA-binding-domain family
    target gene          a first-ranked chain names one of the gold genes
    both in one chain    one first-ranked chain names the gold TF (as its group where the gold TF has one, else as
                         the member) and a gold gene
    trait                the first-ranked chains name a trait that contains every word of a gold trait

A component counts only where the specification says it applies. Direction is not scored: the fill's claims state
no direction, by its own rule. Context is not scored: the cases are run from the variant alone.

Ties. Two numbers are given for every component, because "named among 316 tied chains" says little:

    named     1 when a first-ranked candidate matches, else 0
    share     the matching candidates over all the candidates the first-ranked chains name for that component: the
              chance that one candidate drawn from the tie is right. A chain that names no TF, or no gene, is a
              candidate that matches nothing. For "both in one chain" the share is over the first-ranked chains.

Summed over cases, "named" is the generous count and "share" the strict one; with one leading chain they are equal.

The judge. Where the judge read a tie, both numbers are given a second time with its answers applied, so that what
it adds or costs is one subtraction. Applied means: the candidates it points to replace the tie's candidates of
that kind when it points to any; otherwise the candidates it points away from are left out when others remain.
Nothing else of the judge is used, and a tie it did not read, could not decide or disagreed on is left as it was.

Controls. No component applies (the specification calls them evidence-sparse comparisons, not established nulls).
For every case, gold or control, the script also counts what needs no label: how many of the first chain's eight
claims have support, and how many of its four "the alleles differ" claims rest on a measurement (an assay or an
edit) and not only on an association or a prediction. A control whose first chain has a measured allele claim is
named.

The 15 cases are not a blind test of the people who built this: their gold answers were known while the pipeline
was designed, and two of them (rs12740374 and the TERT C228T case) were used to build the earlier engine. The
numbers are given for all nine gold cases and for the seven others. Every score is provisional while the
specification's status is "unreviewed".

Nothing is written into an existing --out folder. With --freeze, the script first checks that nothing the freeze
pins has changed (scripts/v9_freeze.py) and refuses to score when something has.
"""

import argparse
import json
import sys
from collections.abc import Mapping, Sequence
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "scripts"))

from v9_demo_export import saved_graph  # noqa: E402

from variant2mechanism.v9 import evaluation as E  # noqa: E402
from variant2mechanism.v9 import table as T  # noqa: E402

TF_LEVELS = (("tf_member", "TF, as the member"), ("tf_group", "TF, as its group"), ("tf_family", "TF, as its family"))
COMPONENTS = (*TF_LEVELS, ("target_gene", "Target gene"), ("both", "Both in one chain"), ("phenotype", "Trait"))
ENGINE_DEVELOPMENT = ("rs12740374", "tert_c228t")          # used while the earlier engine was built
ALLELE_SLOTS = tuple(key for key in T.SLOT_KEYS if key.endswith(".allele"))
MEASURED = ("edit", "assay")


def tf_names(claim: T.TableClaim, ref: E.Reference) -> E._Names:
    """What a chain's TF claim names, as the evaluator reads names: a group gives group credit only."""
    names = E._Names()
    tfs = {ref.symbol(t) for t in claim.names.get("tfs") or []}
    groups = {g.upper() for g in claim.names.get("groups") or [] if g}
    if groups:
        names.group_ids, names.group_members = groups, tfs
    else:
        names.tfs = tfs
    return names


def candidates(table: T.Table, leaders: Sequence[T.TableChain], slot: str) -> dict[str, T.TableClaim]:
    """The distinct claims the first-ranked chains hold in a slot, by label (chains that name nothing there hold
    one candidate between them, which matches nothing)."""
    found: dict[str, T.TableClaim] = {}
    for chain in leaders:
        if chain.claims.get(slot):
            claim = table.claims[str(chain.claims[slot])]
            found.setdefault(claim.label, claim)
    return found


def judged(rows: Sequence[Mapping[str, Any]], kind: str, labels: Sequence[str]) -> list[str]:
    """The candidates of a kind that stand once the judge's answers are applied (see the module docstring)."""
    said = {r["label"]: r["answer"] for r in rows if r["kind"] == kind}
    to = [x for x in labels if said.get(x) == "shown"]
    if to:
        return to
    left = [x for x in labels if said.get(x) != "against"]
    return left or list(labels)


def _pair(matching: int, total: int) -> dict[str, Any]:
    return {"named": int(matching > 0), "matching": matching, "candidates": total,
            "share": round(matching / total, 4) if total else 0.0}


def score_case(entry: Mapping[str, Any], table: T.Table, rows: Sequence[Mapping[str, Any]], ref: E.Reference,
               ) -> dict[str, Any]:
    """One case: for every component that applies, named and share over the first-ranked chains, without and with
    the judge's answers (`rows`: its per-candidate rows, empty when it read nothing); and the label-free counts."""
    components = entry["components"]
    leaders = [c for c in table.chains if c.rank == 1]
    tfs, genes = candidates(table, leaders, "binding.allele"), candidates(table, leaders, "gene.allele")
    level_for_both = "tf_group" if components["tf_group"]["applicable"] else "tf_member"
    gold_genes = set(components["target_gene"]["genes"]) if components["target_gene"]["applicable"] else set()

    def tf_hit(label: str, level: str) -> bool:
        return bool(E._tf_matches(tf_names(tfs[label], ref), components, ref)[level])

    def gene_hit(label: str) -> bool:
        return bool({ref.symbol(g) for g in genes[label].names.get("genes") or []} & gold_genes)

    def scored(tf_labels: Sequence[str], gene_labels: Sequence[str]) -> dict[str, Any]:
        out: dict[str, Any] = {}
        for level, _ in TF_LEVELS:
            if components[level]["applicable"]:
                out[level] = _pair(sum(tf_hit(x, level) for x in tf_labels), len(tf_labels))
        if components["target_gene"]["applicable"]:
            out["target_gene"] = _pair(sum(gene_hit(x) for x in gene_labels), len(gene_labels))
        if components[level_for_both]["applicable"] and components["target_gene"]["applicable"]:
            kept = [c for c in leaders
                    if table.claims[str(c.claims["binding.allele"])].label in tf_labels
                    and table.claims[str(c.claims["gene.allele"])].label in gene_labels]
            both = sum(tf_hit(table.claims[str(c.claims["binding.allele"])].label, level_for_both)
                       and gene_hit(table.claims[str(c.claims["gene.allele"])].label) for c in kept)
            out["both"] = _pair(both, len(kept))
        return out

    first = table.chains[0] if table.chains else None
    claims = [table.claims[str(first.claims[key])] for key in T.SLOT_KEYS] if first is not None else []
    out: dict[str, Any] = {
        "case_id": entry["case_id"], "control": bool(entry["control"]), "label_class": entry["label_class"],
        "chains": len(table.chains), "first_ranked": len(leaders),
        "tf_candidates": list(tfs), "gene_candidates": list(genes),
        "claims_supported": sum(any(cell.state in ("supports", "both") for cell in c.cells.values()) for c in claims),
        "allele_claims_measured": sum(c.strongest in MEASURED for c in claims if f"{c.step}.{c.part}" in ALLELE_SLOTS),
        "judge": {"read": bool(rows), "points_to": [f"{r['kind']} {r['label']}" for r in rows if r["answer"] == "shown"],
                  "points_away": [f"{r['kind']} {r['label']}" for r in rows if r["answer"] == "against"]},
    }
    if entry["control"] or not leaders:
        return out
    out["scores"] = scored(list(tfs), list(genes))
    out["with_judge"] = scored(judged(rows, "tf", list(tfs)), judged(rows, "gene", list(genes)))
    if components["phenotype"]["applicable"]:
        traits = E._Names()
        for chain in leaders:
            for key in ("trait.allele", "trait.premise"):
                if chain.claims.get(key):
                    traits.phenotypes |= set(table.claims[str(chain.claims[key])].names.get("traits") or [])
        hit, _ = E._phenotype_recovery(traits, components["phenotype"])
        out["scores"]["phenotype"] = out["with_judge"]["phenotype"] = _pair(int(hit), 1)
    return out


def totals(cases: Sequence[Mapping[str, Any]], which: str) -> dict[str, dict[str, Any]]:
    """Over the gold cases given: for each component, how many it applies to, the sum of named and of share."""
    out = {}
    for key, _ in COMPONENTS:
        have = [c[which][key] for c in cases if key in c.get(which, {})]
        out[key] = {"cases": len(have), "named": sum(x["named"] for x in have),
                    "share": round(sum(x["share"] for x in have), 2)}
    return out


def summary(result: Mapping[str, Any]) -> str:
    cases = result["cases"]
    gold = [c for c in cases if not c["control"]]
    controls = [c for c in cases if c["control"]]
    lines = [f"# Scores of {result['runs']} against the gold specification", "",
             f"Specification status: {result['spec_status']}; every number is provisional until it is reviewed. The "
             "rule is in scripts/v9_table_score.py and was fixed before any table of the fill was scored.", "",
             "\"Named\" counts a case when a first-ranked chain names the gold answer. \"Share\" is the matching "
             "candidates over the candidates the first-ranked chains name, summed over cases: what picking one "
             "candidate from each tie at random would get.", ""]
    for title, key in (("All gold cases", "all"), ("Without the two cases the earlier engine was built on", "clean")):
        lines += [f"## {title} ({result['totals'][key]['n']})", "",
                  "| Component | Cases it applies to | Named | Share | Named, with the judge | Share, with the judge |",
                  "|---|---|---|---|---|---|"]
        plain, with_judge = result["totals"][key]["scores"], result["totals"][key]["with_judge"]
        lines += [f"| {label} | {plain[k]['cases']} | {plain[k]['named']} | {plain[k]['share']:.2f} | "
                  f"{with_judge[k]['named']} | {with_judge[k]['share']:.2f} |" for k, label in COMPONENTS]
        lines.append("")
    lines += ["## Gold cases, one by one", "",
              "| Case | Chains tied for first | TF candidates | Gene candidates | TF as member | TF as group | "
              "Target gene | Both in one chain | Trait | The judge points to | Claims with support (of 8) | "
              "Allele claims measured (of 4) |", "|---|---|---|---|---|---|---|---|---|---|---|---|"]

    def cell(case: Mapping[str, Any], key: str) -> str:
        if key not in case.get("scores", {}):
            return "does not apply"
        a, b = case["scores"][key], case["with_judge"][key]
        text = f"{a['matching']} of {a['candidates']}"
        return text if (a["matching"], a["candidates"]) == (b["matching"], b["candidates"]) else (
            f"{text}; with the judge {b['matching']} of {b['candidates']}")
    for c in gold:
        lines.append(f"| {c['case_id']} | {c['first_ranked']} | {len(c['tf_candidates'])} | {len(c['gene_candidates'])} | "
                     + " | ".join(cell(c, k) for k in ("tf_member", "tf_group", "target_gene", "both", "phenotype"))
                     + f" | {', '.join(c['judge']['points_to']) or '-'} | {c['claims_supported']} | "
                     f"{c['allele_claims_measured']} |")
    lines += ["", "## Controls and gold cases, without labels", "",
              "| Set | Cases | First chain: claims with support, mean of 8 | Cases whose first chain has a measured "
              "allele claim |", "|---|---|---|---|"]
    for name, group in (("Gold", gold), ("Controls", controls)):
        mean = sum(c["claims_supported"] for c in group) / len(group) if group else 0.0
        measured = [c["case_id"] for c in group if c["allele_claims_measured"]]
        lines.append(f"| {name} | {len(group)} | {mean:.1f} | {len(measured)}"
                     + (f" ({', '.join(measured)})" if measured and name == "Controls" else "") + " |")
    lines += ["", "| Control | Class | Chains tied for first | Claims with support (of 8) | Allele claims measured "
                  "(of 4) |", "|---|---|---|---|---|"]
    lines += [f"| {c['case_id']} | {c['label_class']} | {c['first_ranked']} | {c['claims_supported']} | "
              f"{c['allele_claims_measured']} |" for c in controls]
    return "\n".join(lines) + "\n"


def score(runs: Path, spec: Mapping[str, Any], ref: E.Reference) -> dict[str, Any]:
    cases = []
    for entry in spec["cases"]:
        graph = saved_graph(runs / entry["case_id"])     # a run folder, or its public copy (demo/tables)
        if graph is None:
            cases.append({"case_id": entry["case_id"], "control": bool(entry["control"]), "missing": True})
            continue
        cases.append(score_case(entry, T.from_graph(graph), list(T._Index(graph).judged), ref))
    gold = [c for c in cases if not c["control"] and "scores" in c]
    clean = [c for c in gold if c["case_id"] not in ENGINE_DEVELOPMENT]
    return {"runs": str(runs.relative_to(ROOT)) if runs.is_relative_to(ROOT) else str(runs),
            "spec_status": spec.get("status"), "spec_version": spec.get("spec_version"), "cases": cases,
            "totals": {name: {"n": len(group), "scores": totals(group, "scores"),
                              "with_judge": totals(group, "with_judge")}
                       for name, group in (("all", gold), ("clean", clean))}}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--runs", required=True, help="a folder of saved fills, one folder per case")
    parser.add_argument("--out", required=True, help="a new folder for score.json and summary.md")
    parser.add_argument("--freeze", default=None, help="a freeze file: refuse to score when something it pins changed")
    args = parser.parse_args()
    runs, out = (ROOT / args.runs).resolve(), (ROOT / args.out).resolve()
    if out.exists():
        print(f"refused: {out} already exists; choose a new folder", file=sys.stderr)
        return 2
    freeze = None
    if args.freeze:
        import v9_freeze
        record = json.loads((ROOT / args.freeze).read_text())
        changed = v9_freeze.differences(record)
        if changed:
            print(f"refused: {len(changed)} thing(s) differ from {args.freeze}: " + "; ".join(changed[:5]),
                  file=sys.stderr)
            return 2
        if record.get("runs") != str(runs.relative_to(ROOT)):
            print(f"refused: {args.freeze} pins {record.get('runs')}, not {args.runs}", file=sys.stderr)
            return 2
        freeze = {"file": args.freeze, "frozen": record["frozen"], "files": len(record["files"])}
    try:
        reference = E.load_reference()
    except OSError as e:
        print(f"refused: a reference table is missing ({e.filename}). Scoring reads two public tables that the "
              "repository does not hold: data/reference/hgnc/hgnc_complete_set.txt (HGNC) and "
              "data/reference/tf_families/DatabaseExtract_v_1.01.csv (the human TF catalogue). The README says "
              "where each comes from.", file=sys.stderr)
        return 2
    result = {**score(runs, E.load_gold_spec(), reference), "freeze": freeze}
    out.mkdir(parents=True)
    (out / "score.json").write_text(json.dumps(result, indent=1) + "\n")
    (out / "summary.md").write_text(summary(result))
    print(f"scored {len(result['cases'])} case(s); see {out / 'summary.md'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
