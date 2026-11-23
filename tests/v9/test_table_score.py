"""scripts/v9_table_score.py and scripts/v9_freeze.py: scoring first-ranked chains, and pinning what is frozen.

Every table here is made up: a few chains with invented TF groups and genes, and a gold entry written for them.
No saved run and no gold label of the evaluated cases is read.
"""

import importlib.util
import sys
from pathlib import Path

from variant2mechanism.v9 import evaluation as E
from variant2mechanism.v9 import table as T

REPO = Path(__file__).resolve().parents[2]


def load(name: str):
    spec = importlib.util.spec_from_file_location(name, REPO / "scripts" / f"{name}.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


S = load("v9_table_score")
REF = E.Reference(groups=(), resolver=None, lambert={"TFA1": "bZIP", "TFA2": "bZIP", "TFB1": "bZIP", "TFC1": "C2H2 ZF",
                                                     "TFD1": "Homeodomain"})
ENTRY = {"case_id": "made_up", "control": False, "label_class": "tf_mechanism_other", "components": {
    "tf_member": {"applicable": True, "tfs": ["TFA1"]},
    "tf_group": {"applicable": True, "groups": [{"id": "G900", "tfs": ["TFA1", "TFA2"]}]},
    "tf_family": {"applicable": True, "dbd": ["bZIP"]},
    "direction": {"applicable": True}, "context": {"applicable": True},
    "target_gene": {"applicable": True, "genes": ["GENEA"]},
    "phenotype": {"applicable": True, "labels": ["LDL cholesterol"]}}}
GROUP_A = ("G900 (TFA1, TFA2)", ["TFA1", "TFA2"], ["G900", "G900 (TFA1, TFA2)"])       # holds the gold TF
GROUP_B = ("G901 (TFB1)", ["TFB1"], ["G901", "G901 (TFB1)"])                           # its family, another group
GROUP_C = ("G902 (TFC1)", ["TFC1"], ["G902", "G902 (TFC1)"])
GROUP_D = ("G903 (TFD1)", ["TFD1"], ["G903", "G903 (TFD1)"])


def claim(slot: str, label: str, *, tfs=(), groups=(), genes=(), traits=(), strongest="none",
          state="nothing_found") -> T.TableClaim:
    step, part = slot.split(".")
    names = {"tfs": list(tfs), "groups": list(groups), "elements": [], "genes": list(genes), "traits": list(traits),
             "trait_ids": []}
    cells = {lane: T.Cell(state=state if lane == "database" else "nothing_found") for lane in T.LANE_KEYS}
    return T.TableClaim(id=f"{slot}:{label}", step=step, part=part, text="", label=label, names=names,
                        graph_claims=[], cells=cells, strongest=strongest)


def table(pairs: list[tuple[tuple, str]], *, behind: list[tuple[tuple, str]] = (), trait: str = "LDL cholesterol measurement",
          measured: tuple[str, ...] = ()) -> T.Table:
    """A table whose first-ranked chains are `pairs` of a TF group and a gene, with `behind` ranked after them."""
    claims: dict[str, T.TableClaim] = {}
    chains = []

    def add(c: T.TableClaim) -> str:
        claims.setdefault(c.id, c)
        return c.id
    shared = {key: add(claim(key, "shared", traits=[trait] if key.startswith("trait") else (),
                             strongest="assay" if key in measured else "association", state="supports"))
              for key in T.SLOT_KEYS if key.split(".")[0] in ("activity", "trait")}
    for rank, group in ((1, pairs), (len(pairs) + 1, behind)):
        for (label, tfs, groups), gene in group:
            tf = (add(claim("binding.allele", label, tfs=tfs, groups=groups, strongest="prediction", state="supports"))
                  if label else add(claim("binding.allele", "no TF named")))
            chains.append(T.TableChain(rank=rank, ties=len(group), title=f"{label} → {gene}", claims={
                **shared, "binding.allele": tf, "binding.premise": add(claim("binding.premise", label or "no TF named")),
                "gene.allele": add(claim("gene.allele", gene, genes=[gene], strongest="association", state="supports")),
                "gene.premise": add(claim("gene.premise", gene, genes=[gene]))}))
    return T.Table(case_id="made_up", variant="chr1:1:A>T", chains=chains, claims=claims)


def row(kind: str, label: str, answer: str) -> dict:
    return {"kind": kind, "label": label, "answer": answer}


def test_one_leading_chain_is_scored_by_what_it_names():
    found = S.score_case(ENTRY, table([(GROUP_A, "GENEA")], behind=[(GROUP_C, "GENEB")]), [], REF)
    scores = found["scores"]
    assert (found["first_ranked"], found["chains"]) == (1, 2)
    assert scores["tf_member"] == {"named": 0, "matching": 0, "candidates": 1, "share": 0.0}   # a group is not the member
    assert scores["tf_group"]["named"] == 1 and scores["tf_group"]["share"] == 1.0
    assert scores["tf_family"]["share"] == 1.0 and scores["target_gene"]["share"] == 1.0
    assert scores["both"] == {"named": 1, "matching": 1, "candidates": 1, "share": 1.0}
    assert scores["phenotype"]["named"] == 1                             # every word of "LDL cholesterol" is in the trait
    assert found["with_judge"] == scores and found["judge"]["read"] is False
    # a single TF the chain names is the member, and counts for its group and family too
    single = S.score_case(ENTRY, table([(("TFA1", ["TFA1"], []), "GENEA")]), [], REF)["scores"]
    assert single["tf_member"]["share"] == single["tf_group"]["share"] == single["tf_family"]["share"] == 1.0


def test_a_tie_gets_the_share_of_its_candidates_that_match():
    tied = table([(GROUP_A, "GENEA"), (GROUP_B, "GENEA"), (GROUP_C, "GENEA"), (GROUP_D, "GENEA")])
    scores = S.score_case(ENTRY, tied, [], REF)["scores"]
    assert scores["tf_group"] == {"named": 1, "matching": 1, "candidates": 4, "share": 0.25}
    assert scores["tf_family"]["matching"] == 2 and scores["tf_family"]["share"] == 0.5      # TFB1 is a bZIP too
    assert scores["target_gene"] == {"named": 1, "matching": 1, "candidates": 1, "share": 1.0}
    assert scores["both"] == {"named": 1, "matching": 1, "candidates": 4, "share": 0.25}
    # two TFs and two genes: four chains, one of which names both
    cross = table([(GROUP_A, "GENEA"), (GROUP_A, "GENEB"), (GROUP_C, "GENEA"), (GROUP_C, "GENEB")])
    scores = S.score_case(ENTRY, cross, [], REF)["scores"]
    assert (scores["tf_group"]["share"], scores["target_gene"]["share"], scores["both"]["share"]) == (0.5, 0.5, 0.25)
    # a chain that names no TF is a candidate that matches nothing
    partly = S.score_case(ENTRY, table([(GROUP_A, "GENEA"), (("", [], []), "GENEA")]), [], REF)["scores"]
    assert partly["tf_group"] == {"named": 1, "matching": 1, "candidates": 2, "share": 0.5}
    # nothing right among the tied chains
    wrong = S.score_case(ENTRY, table([(GROUP_C, "GENEB"), (GROUP_D, "GENEB")]), [], REF)["scores"]
    assert wrong["tf_group"]["named"] == wrong["target_gene"]["named"] == wrong["both"]["named"] == 0
    assert wrong["phenotype"]["named"] == 1


def test_the_judges_answers_are_applied_and_shown_beside_the_plain_scores():
    tied = table([(GROUP_A, "GENEA"), (GROUP_B, "GENEA"), (GROUP_C, "GENEA"), (GROUP_D, "GENEA")])
    right = S.score_case(ENTRY, tied, [row("tf", GROUP_A[0], "shown")], REF)
    assert right["scores"]["tf_group"]["share"] == 0.25                  # the plain score does not move
    assert right["with_judge"]["tf_group"] == {"named": 1, "matching": 1, "candidates": 1, "share": 1.0}
    assert right["with_judge"]["both"]["share"] == 1.0 and right["judge"]["points_to"] == [f"tf {GROUP_A[0]}"]
    wrong = S.score_case(ENTRY, tied, [row("tf", GROUP_C[0], "shown")], REF)["with_judge"]
    assert wrong["tf_group"] == {"named": 0, "matching": 0, "candidates": 1, "share": 0.0}   # a wrong pointer costs
    away = S.score_case(ENTRY, tied, [row("tf", GROUP_C[0], "against")], REF)["with_judge"]
    assert away["tf_group"] == {"named": 1, "matching": 1, "candidates": 3, "share": 0.3333}
    lost = S.score_case(ENTRY, tied, [row("tf", GROUP_A[0], "against")], REF)["with_judge"]
    assert lost["tf_group"]["named"] == 0 and lost["tf_group"]["candidates"] == 3
    # an answer that is no pointer changes nothing; nor does one about another kind
    for answer in ("not_shown", "cannot_tell", "disagreed", "check_failed", "no_answer"):
        same = S.score_case(ENTRY, tied, [row("tf", GROUP_A[0], answer)], REF)
        assert same["with_judge"] == same["scores"]
    assert S.judged([row("gene", "GENEA", "against")], "gene", ["GENEA"]) == ["GENEA"]       # the only one stays


def test_a_component_counts_only_where_the_specification_says_it_applies():
    entry = {**ENTRY, "components": {**ENTRY["components"],
                                     "tf_group": {"applicable": False}, "tf_family": {"applicable": False}}}
    found = S.score_case(entry, table([(("TFA1", ["TFA1"], []), "GENEA")]), [], REF)["scores"]
    assert "tf_group" not in found and "tf_family" not in found
    assert found["tf_member"]["share"] == 1.0 and found["both"]["share"] == 1.0   # "both" falls back to the member


def test_a_control_gets_no_score_and_every_case_its_label_free_counts():
    entry = {**ENTRY, "control": True, "label_class": "control_random"}
    found = S.score_case(entry, table([(GROUP_A, "GENEA")], measured=("activity.allele",)), [], REF)
    assert "scores" not in found and "with_judge" not in found
    # activity (both claims), the trait step (both), the TF's allele claim and the gene's: six of eight with support
    assert found["claims_supported"] == 6 and found["allele_claims_measured"] == 1
    assert S.score_case(entry, table([(GROUP_A, "GENEA")]), [], REF)["allele_claims_measured"] == 0


def test_totals_and_the_summary_table():
    tied = table([(GROUP_A, "GENEA"), (GROUP_B, "GENEA"), (GROUP_C, "GENEA"), (GROUP_D, "GENEA")])
    cases = [S.score_case(ENTRY, table([(GROUP_A, "GENEA")]), [], REF),
             S.score_case({**ENTRY, "case_id": "tied"}, tied, [row("tf", GROUP_A[0], "shown")], REF),
             S.score_case({**ENTRY, "case_id": "ctrl", "control": True}, table([(GROUP_C, "GENEB")]), [], REF)]
    gold = [c for c in cases if not c["control"]]
    plain, judged = S.totals(gold, "scores"), S.totals(gold, "with_judge")
    assert plain["tf_group"] == {"cases": 2, "named": 2, "share": 1.25}
    assert judged["tf_group"] == {"cases": 2, "named": 2, "share": 2.0}
    assert plain["tf_member"] == {"cases": 2, "named": 0, "share": 0.0}
    result = {"runs": "runs/made_up", "spec_status": "unreviewed", "cases": cases,
              "totals": {name: {"n": 2, "scores": plain, "with_judge": judged} for name in ("all", "clean")}}
    text = S.summary(result)
    assert "| TF, as its group | 2 | 2 | 1.25 | 2 | 2.00 |" in text
    assert "| tied | 4 | 4 | 1 | 0 of 4; with the judge 0 of 1 | 1 of 4; with the judge 1 of 1 |" in text
    assert "| made_up | 1 | 1 | 1 | 0 of 1 | 1 of 1 | 1 of 1 | 1 of 1 | 1 of 1 | - | 6 | 0 |" in text
    assert "provisional" in text and "| Controls | 1 |" in text


def test_a_freeze_lists_what_changed_and_nothing_when_nothing_did():
    freeze = load("v9_freeze")
    files = freeze.pipeline_files()
    assert "src/variant2mechanism/v9/judge.py" in files and "config.yaml" in files
    assert "src/variant2mechanism/v9/prompts/judge_system.txt" in files
    assert not any(name.endswith(("v9/report.py", "v9/evaluation.py")) for name in files)     # display and scoring
    assert not any(name.startswith(("scripts/", "tests/", "docs/")) for name in files)
    record = {"files": files, "formats": freeze.formats()}
    assert freeze.differences(record) == []
    changed = {"files": {**files, "config.yaml": "0" * 64, "src/variant2mechanism/gone.py": "1" * 64},
               "formats": {**freeze.formats(), "judge_format": 0}}
    del changed["files"]["src/variant2mechanism/v9/judge.py"]
    found = freeze.differences(changed)
    assert "changed: config.yaml" in found and "gone: src/variant2mechanism/gone.py" in found
    assert "new: src/variant2mechanism/v9/judge.py" in found
    assert any(line.startswith("format judge_format: was 0") for line in found)
