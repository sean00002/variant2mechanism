"""Gold isolation (SPEC 10, 13.12): clean requests carry no label-derived string, for every gold row and both arms.

These tests read data/gold_set.csv (never edited) only to prove that nothing label-derived reaches a request or the
case intake builds from it; no gold row is run, scored or used to choose anything.
"""

import ast
import csv
import re

import pytest

from variant2mechanism.config import REPO
from variant2mechanism.evaluation.gold import NEVER_IN_PROMPT
from variant2mechanism.v9.evaluation import (
    ARMS,
    LABEL_KINDS,
    clean_request,
    find_label_strings,
    label_strings,
    label_strings_by_kind,
)
from variant2mechanism.v9.graph import ClaimGraph
from variant2mechanism.v9.intake import bracketed_parts, build_case, strip_bracketed
from variant2mechanism.v9.roles import render_case

GOLD = REPO / "data" / "gold_set.csv"
with open(GOLD, newline="") as _f:
    ROWS = list(csv.DictReader(_f))
BY_ID = {r["case_id"]: r for r in ROWS}
V9 = REPO / "src" / "variant2mechanism" / "v9"


@pytest.mark.parametrize("arm", ARMS)
@pytest.mark.parametrize("row", ROWS, ids=[r["case_id"] for r in ROWS])
def test_a_clean_request_carries_no_label_string(row, arm):
    request = clean_request(row, arm)
    assert find_label_strings(request.model_dump_json(), label_strings(row, arm=arm)) == []


@pytest.mark.parametrize("row", ROWS, ids=[r["case_id"] for r in ROWS])
def test_the_main_arm_holds_coordinates_and_origin_only(row):
    request = clean_request(row, "main")
    chrom = row["chrom"].removeprefix("chr")
    assert request.variant == f"chr{chrom}:{row['pos_grch38']}:{row['ref']}>{row['alt']}"
    assert (request.disease, request.context, request.provenance) == ([], [], {})
    assert re.fullmatch(r"REQ-[0-9a-f]{12}", request.request_id)
    assert request.origin == row["origin"]


@pytest.mark.parametrize("row", ROWS, ids=[r["case_id"] for r in ROWS])
def test_the_supplied_disease_arm_strips_bracketed_text(row):
    request = clean_request(row, "supplied_disease")
    assert request.disease == [strip_bracketed(row["disease_or_trait"])]
    assert request.context == []
    for part in bracketed_parts(row["disease_or_trait"]):
        assert not find_label_strings(" ".join(request.disease), [part])
    assert not re.search(r"[()\[\]{}]", " ".join(request.disease))
    assert request.request_id != clean_request(row, "main").request_id


def test_origin_comes_only_from_the_explicit_origin_column():
    tert = BY_ID["tert_c228t"]
    assert clean_request(tert, "main").origin == "somatic"
    # Without the column, nothing else may make it somatic: not the label class, the cancer disease, the hotspot's
    # name or the notes.
    unlabelled = {k: v for k, v in tert.items() if k != "origin"}
    assert "cancer" in unlabelled["label_class"] and "TERT" in unlabelled["variant"]
    assert clean_request(unlabelled, "main").origin == "unknown"
    assert clean_request(unlabelled, "supplied_disease").origin == "unknown"
    assert clean_request({**tert, "origin": " Somatic "}, "main").origin == "somatic"
    assert clean_request({**tert, "origin": "cancer"}, "main").origin == "unknown"
    assert clean_request({**tert, "origin": ""}, "main").origin == "unknown"


@pytest.mark.parametrize("row", ROWS, ids=[r["case_id"] for r in ROWS])
def test_intake_turns_a_clean_request_into_a_case_without_labels(row, v9_cfg):
    for arm in ARMS:
        request = clean_request(row, arm)
        case = build_case(request, config=v9_cfg, http=None, mode="cache_only")
        assert case.case_id == request.request_id
        unnamed = build_case(request.model_copy(update={"request_id": None}), config=v9_cfg, http=None,
                             mode="cache_only")
        assert unnamed.case_id == request.request_id          # the id is the hash of the clean request itself
        assert case.variant.reference_check == "verified"     # every gold variant has a cached 21-mer
        assert case.supplied_context == []
        assert find_label_strings(case.model_dump_json(), label_strings(row, arm=arm)) == []


@pytest.mark.parametrize("row", ROWS, ids=[r["case_id"] for r in ROWS])
def test_the_case_packet_of_a_clean_request_carries_no_label_string(row, v9_cfg):
    """What every agent packet shows of the case (roles.render_case), for the case intake builds from each arm's clean
    request: the engine-side half of the isolation the audit checks on the request."""
    for arm in ARMS:
        case = build_case(clean_request(row, arm), config=v9_cfg, http=None, mode="cache_only")
        assert find_label_strings(render_case(ClaimGraph(case)), label_strings(row, arm=arm)) == [], arm


def test_label_strings_cover_every_label_column():
    for row in ROWS:
        strings = label_strings(row)
        for column in (*NEVER_IN_PROMPT, "case_id", "variant", "disease_or_trait", "expression_context"):
            value = " ".join(row[column].split())
            if len(value) >= 3 and value.lower() not in ("none", "not applicable", "control"):
                assert value in strings, (row["case_id"], column)
    kinds = label_strings_by_kind(BY_ID["rs12740374"])
    assert set(kinds) == set(LABEL_KINDS)
    assert {"CEBPA", "CEBPB", "CEBPE", "G035"} <= kinds["group"]          # TF members and the registry group
    assert {"1p13", "(1p13)"} <= kinds["bracketed"]
    assert {"20686566", "PMID:20686566"} <= kinds["source"]
    assert "SORT1" in kinds["gene"] and "Hep3B" in kinds["context"] and "rs12740374" in kinds["identity"]
    assert "rs6983267" in label_strings_by_kind(BY_ID["rs73706717"])["identity"]   # the parent the notes name


def test_the_supplied_arm_exempts_only_the_supplied_disease():
    row = BY_ID["rs12740374"]
    main, supplied = label_strings(row), label_strings(row, arm="supplied_disease")
    assert {"LDL cholesterol", "myocardial infarction", "1p13", "CEBPA"} <= main
    assert "LDL cholesterol" not in supplied and "myocardial infarction" not in supplied
    assert {"1p13", "(1p13)", "CEBPA", "SORT1", "Liver"} <= supplied


def test_label_strings_match_whole_tokens_ignoring_case():
    assert find_label_strings('{"request_id": "REQ-1"}', ["REST", "req"]) == ["req"]
    assert find_label_strings("binding of cebpa here", ["CEBPA", "CEBP"]) == ["CEBPA"]
    assert find_label_strings("locus (1p13) here", ["(1p13)", "1p13", "1p1"]) == ["(1p13)", "1p13"]


# The evaluator must stay out of every engine path. Engine modules (all but the evaluator, and the modules that only
# read a finished run folder) may not import it, nor the shared gold package, nor name the gold files or a run's
# evaluation.json in code. bundle.py and report.py read a finished run (they note whether an evaluation.json exists
# and leave it out of public exports); replay.py holds the v8 replay, which reads v8's gold cases. Even they may not
# import the v9 evaluator.
EVALUATOR = ("variant2mechanism.v9.evaluation",)
GOLD_IMPORTS = (*EVALUATOR, "variant2mechanism.evaluation", "variant2mechanism.v8.evaluation")
GOLD_STRINGS = ("v9_gold_spec", "gold_set", "evaluation.json", "v9.evaluation")
RUN_FOLDER_READERS = {"bundle.py", "report.py", "replay.py"}


def _imported(tree: ast.AST, package: str = "variant2mechanism.v9") -> set[str]:
    """Every module an import statement in a v9 module can bind, relative imports resolved against the package:
    `from . import evaluation`, `from ..v9 import evaluation` and `from variant2mechanism.v9 import evaluation` all
    give variant2mechanism.v9.evaluation."""
    parts, names = package.split("."), set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            names |= {a.name for a in node.names}
        elif isinstance(node, ast.ImportFrom):
            base = parts[:len(parts) - node.level + 1] if node.level else []
            module = ".".join([*base, *(node.module.split(".") if node.module else [])])
            names |= {module, *(f"{module}.{a.name}" for a in node.names)}
    return names


def _forbidden(names: set[str], prefixes: tuple[str, ...]) -> list[str]:
    return sorted(n for n in names if any(n == p or n.startswith(f"{p}.") for p in prefixes))


def _code_strings(tree: ast.AST) -> list[str]:
    """String constants in code (f-string parts included), docstrings left out: a docstring may say what a module
    never reads; code that reads a file has to name it."""
    docstrings = {id(node.body[0].value) for node in ast.walk(tree)
                  if isinstance(node, ast.Module | ast.ClassDef | ast.FunctionDef | ast.AsyncFunctionDef)
                  and node.body and isinstance(node.body[0], ast.Expr)
                  and isinstance(node.body[0].value, ast.Constant) and isinstance(node.body[0].value.value, str)}
    return [n.value for n in ast.walk(tree)
            if isinstance(n, ast.Constant) and isinstance(n.value, str) and id(n) not in docstrings]


@pytest.mark.parametrize("source, evaluator, gold", [
    ("from variant2mechanism.v9 import evaluation", True, True),
    ("from ..v9 import evaluation", True, True),
    ("from . import evaluation, graph", True, True),
    ("from .evaluation import audit", True, True),
    ("import variant2mechanism.v9.evaluation as ev", True, True),
    ("from .. import evaluation", False, True),                 # the shared gold package
    ("from ..evaluation.gold import NEVER_IN_PROMPT", False, True),
    ("from ..v8.evaluation import ARMS", False, True),
    ("from .graph import ClaimGraph\nimport json", False, False),
])
def test_the_import_guard_reads_every_import_form(source, evaluator, gold):
    names = _imported(ast.parse(source))
    assert bool(_forbidden(names, EVALUATOR)) is evaluator
    assert bool(_forbidden(names, GOLD_IMPORTS)) is gold


def test_the_string_guard_skips_docstrings_and_reads_code():
    tree = ast.parse('"""Never reads data/gold_set.csv."""\n'
                     'def f(cfg):\n    """Nor evaluation.json."""\n    return cfg.path("eval", "gold_set")\n'
                     'g = importlib.import_module(f"{PKG}.v9.evaluation")\n')
    assert sorted(s for s in _code_strings(tree) if any(g in s for g in GOLD_STRINGS)) == [".v9.evaluation",
                                                                                          "gold_set"]


def test_no_engine_module_imports_the_evaluator_or_names_gold_files():
    """evaluation.py is evaluator-only: no other v9 module may import it, and no engine module may import the gold
    package or name the gold files or evaluation.json (a module another task is still writing is skipped while it
    does not parse)."""
    for path in sorted(V9.glob("*.py")):
        if path.name == "evaluation.py":
            continue
        try:
            tree = ast.parse(path.read_text())
        except SyntaxError:
            continue
        engine = path.name not in RUN_FOLDER_READERS
        imports = _forbidden(_imported(tree), GOLD_IMPORTS if engine else EVALUATOR)
        named = GOLD_STRINGS if engine else ("v9.evaluation",)      # importlib can load the evaluator by name
        strings = sorted({s for s in _code_strings(tree) if any(g in s for g in named)})
        assert not imports and not strings, (path.name, imports, strings)
