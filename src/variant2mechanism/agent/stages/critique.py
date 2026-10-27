"""Critique (critic): grade every link, list problems, suggest up to 3 checks (spec 2, 8.3); and the regrade after
each refinement round (8.6), which does the same for the revised chains, so its checks can steer the next round."""

import json

from ...context.catalog import tool_specs
from ..case import RunState, prompt
from ..schemas import CritiqueOut, check_grades
from .generate import chains_json

MAX_CHECKS = 3


def tool_list(state: RunState) -> str:
    lines = []
    for name, t in tool_specs(state.config, state.spec.is_cancer).items():
        args = ", ".join(t["input_schema"]["properties"])
        lines.append(f"- {name}({args}): {t['description']}")
    return "\n".join(lines)


def validate_check(state: RunState, c) -> tuple[bool, str | None]:
    """A suggested check or a planned call: a known tool, arguments as a JSON object, only arguments it takes."""
    tools = tool_specs(state.config, state.spec.is_cancer)
    if c.tool not in tools:
        return False, f"unknown tool {c.tool}"
    try:
        args = json.loads(c.args_json)
    except json.JSONDecodeError:
        return False, "args_json is not JSON"
    if not isinstance(args, dict):
        return False, "args_json is not an object"
    allowed = set(tools[c.tool]["input_schema"]["properties"])
    if set(args) - allowed:
        return False, f"arguments {sorted(set(args) - allowed)} are not taken by {c.tool}"
    return True, None


def keep_checks(state: RunState, stage: str, checks: list) -> list:
    """The first 3 valid checks; every suggestion goes to the ledger with the reason it was dropped."""
    rows, kept = [], []
    for i, c in enumerate(checks):
        ok, note = validate_check(state, c) if i < MAX_CHECKS else (False, "beyond the first 3")
        rows.append({**c.model_dump(), "kept": ok, "note": note})
        if ok:
            kept.append(c)
    state.ledger.add_checks(stage, rows)
    return kept


def critique(state: RunState) -> None:
    instruction = prompt("critique").format(tool_list=tool_list(state), chains=chains_json(state.v0))
    res = state.llm.call("critic", "critique", prompt("critic_system"), state.user_message(instruction),
                         output_model=CritiqueOut,
                         check=lambda o: CritiqueOut(grades=check_grades(o.grades, state.v0), problems=o.problems,
                                                     checks=o.checks))
    out = res.parsed
    state.grades0, state.problems = out.grades, out.problems
    state.checks = state.checks0 = keep_checks(state, "critique", out.checks)
    state.ledger.add_grades("critique", 0, "critic", state.grades0)


def regrade(state: RunState, rnd: int) -> None:
    hyps = state.revised.hypotheses
    instruction = prompt("regrade").format(tool_list=tool_list(state), round=rnd, chains=chains_json(hyps))
    res = state.llm.call("critic", "regrade", prompt("critic_system"), state.user_message(instruction),
                         output_model=CritiqueOut,
                         check=lambda o: CritiqueOut(grades=check_grades(o.grades, hyps), problems=o.problems,
                                                     checks=o.checks))
    out = res.parsed
    state.grades1, state.problems = out.grades, out.problems
    state.checks = keep_checks(state, "regrade", out.checks)
    state.ledger.add_grades("regrade", rnd, "critic", state.grades1)
