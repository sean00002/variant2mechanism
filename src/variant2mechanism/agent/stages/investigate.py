"""Refinement rounds (spec 2, 8.4 to 8.6; iterative since 26 Oct 2026): plan, act, revise, regrade, up to
`max_rounds` times.

Each round the generator plans up to `max_calls` tool calls as data: the tool, its arguments, the link each would
resolve and the result it expects. Code drops invalid calls and repeats (the same tool with the same arguments in any
round), runs the rest with the ledger first, and the generator revises, saying call by call whether the result matched
the expectation. The critic then regrades and suggests checks for the next round. The loop stops when the planner has
no new call to run, or after `max_rounds`. Round 1 always revises and regrades, so every run has a revision.

An empty search is not news: a ChIP-seq call for a TF in a biosample ENCODE never assayed it in is answered "no
experiment" and does not count against the round's calls, and a round whose calls bring no new information ends the
loop. So does a round that leaves the top chain and the grades of its links as they were.
"""

import json

from ...context.base import ToolResult, call_tool
from ...context.catalog import run_context_tool, tool_specs
from ...context.literature import literature_search
from ..case import RunState, prompt
from ..schemas import Plan, RevisedRound, check_revised
from .citations import REGISTRY_TO_COVERAGE
from .critique import regrade, tool_list, validate_check
from .gather import add_literature, note_retries, tool_result_text
from .generate import chains_json


def _grades_text(grades) -> str:
    return "\n".join(f"{g.hypothesis_id}.{g.step}: {g.status} ({g.reason})" for g in grades) or "none"


def _checks_text(checks) -> str:
    return "\n".join(f"{c.tool}({c.args_json}) resolves {c.resolves}: {c.why}" for c in checks) or "none"


def outcome(res: ToolResult) -> str:
    """What a call brought: "new" information, "no experiment" (ENCODE never ran it), or "failed"."""
    if not res.ok:
        return "failed"
    if res.tool == "chip_peaks" and isinstance(res.full, dict) and res.full.get("status") == "not_assayed":
        return "no experiment"
    return "new"


def run_tool(state: RunState, name: str, args: dict) -> tuple[str, str]:
    """Run one investigate tool bound to this case, ledger first. Returns the tool result text, which starts with the
    new evidence ID, and its outcome."""
    spec = tool_specs(state.config, state.spec.is_cancer).get(name)
    if spec is None:
        return f"Error: {name} is not available in this configuration.", "failed"
    extra = set(args) - set(spec["input_schema"]["properties"])
    if extra:
        return f"Error: {name} does not take {sorted(extra)}.", "failed"
    if name == "qbic_tf_detail":
        v = state.spec.variant
        out = state.qbic.qbic_tf_detail(v.chrom, v.pos, v.ref, v.alt, args.get("tf", ""))
        if out.get("coverage") in REGISTRY_TO_COVERAGE:        # the chains' words: "tf" is own_model
            out = {**out, "coverage": REGISTRY_TO_COVERAGE[out["coverage"]]}
        res = ToolResult("qbic_tf_detail", args, json.dumps(out, separators=(",", ":")), out,
                         "QBiC-SELEX 1.0.0 primary collection (997 models)", "cache/qbic.sqlite", "computational",
                         ok="error" not in out, limit=3000)
        ev = state.ledger.add_evidence("investigate", res)
        return tool_result_text(ev, [], state.mask), outcome(res)
    clean = {k: v for k, v in args.items() if v is not None}
    if name == "literature_search":
        query = clean.get("query", "")
        res = call_tool(literature_search, state.tool_case, query, masked=state.masked)
        note_retries(state, res)
        ev, quotes = add_literature(state, "investigate", res, query)
        return tool_result_text(ev, quotes, state.mask), outcome(res)
    res = run_context_tool(name, state.tool_case, clean)
    note_retries(state, res)
    ev = state.ledger.add_evidence("investigate", res)
    return tool_result_text(ev, [], state.mask), outcome(res)


def call_key(tool: str, args: dict) -> str:
    return f"{tool}({json.dumps(args, sort_keys=True, separators=(',', ':'))})"


def memory_text(state: RunState) -> str:
    """What the planner carries between rounds: every call already run, with the evidence it produced."""
    return "\n".join(f"round {c['round']}: {c['key']} -> {c['evidence_id']}"
                     + ("" if c["status"] == "run" else f" ({c['status']})")
                     for c in state.investigate_calls if c["run"]) or "none"


def plan(state: RunState, rnd: int, max_rounds: int, max_calls: int) -> Plan:
    instruction = prompt("plan").format(round=rnd, max_rounds=max_rounds, max_calls=max_calls,
                                        tool_list=tool_list(state), version=rnd - 1,
                                        chains=chains_json(state.current_chains()),
                                        grades=_grades_text(state.current_grades()),
                                        problems="\n".join(state.problems) or "none",
                                        checks=_checks_text(state.checks), memory=memory_text(state))
    res = state.llm.call("generator", "plan", prompt("generator_system"), state.user_message(instruction),
                         output_model=Plan)
    state.ledger.log("plan", f"round {rnd}", res.parsed.model_dump())
    return res.parsed


def act(state: RunState, rnd: int, calls: list, max_calls: int) -> list[dict]:
    """Run the planned calls in order; invalid calls, repeats and calls beyond `max_calls` are recorded, not run. A
    "no experiment" answer does not count against `max_calls`."""
    done = {c["key"] for c in state.investigate_calls if c["run"]}
    records, used = [], 0
    for p in calls:
        rec = {"round": rnd, "tool": p.tool, "args": None, "key": None, "resolves": p.resolves,
               "expected": p.expected, "run": False, "status": "", "evidence_id": None, "new_information": False}
        ok, note = validate_check(state, p)
        if not ok:
            rec["status"] = f"invalid: {note}"
        else:
            args = {k: v for k, v in json.loads(p.args_json).items() if v is not None}
            rec |= {"args": args, "key": call_key(p.tool, args)}
            if rec["key"] in done:
                rec["status"] = "repeat"
            elif used >= max_calls:
                rec["status"] = "over the limit"
            else:
                done.add(rec["key"])
                text, got = run_tool(state, p.tool, args)
                used += got != "no experiment"
                if text.startswith("Error"):
                    rec["status"] = text
                else:
                    rec |= {"run": True, "status": "run" if got == "new" else got,
                            "evidence_id": text.split(":", 1)[0], "new_information": got == "new"}
        records.append(rec)
    state.investigate_calls += records
    state.ledger.log("act", f"round {rnd}", records)
    return records


def _calls_text(records: list[dict]) -> str:
    lines = []
    for r in records:
        args = json.dumps(r["args"]) if r["args"] is not None else "(invalid arguments)"
        done = f"result {r['evidence_id']}" if r["run"] else f"not run ({r['status']})"
        lines.append(f"{r['tool']}({args}) for {r['resolves']}; expected: {r['expected']}; {done}")
    return "\n".join(lines) or "none"


def revise(state: RunState, rnd: int, records: list[dict]) -> None:
    instruction = prompt("revise").format(version=rnd - 1, chains=chains_json(state.current_chains()),
                                          grades=_grades_text(state.current_grades()),
                                          problems="\n".join(state.problems) or "none", calls=_calls_text(records))
    res = state.llm.call("generator", "revise", prompt("generator_system"), state.user_message(instruction),
                         output_model=RevisedRound, check=check_revised)
    state.revised = res.parsed
    state.ledger.add_chains("revise", rnd, state.revised.hypotheses)


def snapshot(state: RunState) -> tuple[dict, dict]:
    return ({h.id: h.probability for h in state.current_chains()},
            {(g.hypothesis_id, g.step): g.status for g in state.current_grades()})


def answer(state: RunState) -> tuple[str, dict]:
    """The top chain (its TF, or "null") and the grades of its links."""
    top = max(state.current_chains(), key=lambda h: h.probability)
    return ("null" if top.is_null else (top.tf or "").upper(),
            {g.step: g.status for g in state.current_grades() if g.hypothesis_id == top.id})


def moved(before: tuple[dict, dict], after: tuple[dict, dict]) -> tuple[list[str], float]:
    """The link grades that changed, and the largest change in a chain's probability (a chain added or dropped counts
    with its whole probability)."""
    (p0, g0), (p1, g1) = before, after
    changed = [f"{h}.{s}: {g0.get((h, s), 'absent')} → {g1.get((h, s), 'absent')}"
               for h, s in sorted(set(g0) | set(g1)) if g0.get((h, s)) != g1.get((h, s))]
    dp = max((abs(p1.get(k, 0.0) - p0.get(k, 0.0)) for k in set(p0) | set(p1)), default=0.0)
    return changed, dp


def refine(state: RunState, max_rounds: int = 3, max_calls: int = 3) -> None:
    for rnd in range(1, max_rounds + 1):
        before, top_before = snapshot(state), answer(state)
        p = plan(state, rnd, max_rounds, max_calls)
        records = act(state, rnd, p.calls, max_calls)
        ran = any(r["run"] for r in records)
        new = any(r["new_information"] for r in records)
        note = f" ({p.stop_reason.strip()})" if p.stop_reason.strip() else ""
        if rnd > 1 and not ran:
            state.stop_reason = f"round {rnd}: no new call to run{note}"
            break
        if rnd > 1 and not new:
            state.stop_reason = f"round {rnd}: its calls brought no new information"
            break
        revise(state, rnd, records)
        regrade(state, rnd)
        changed, dp = moved(before, snapshot(state))
        state.rounds.append({
            "round": rnd, "calls": records, "planner_note": p.stop_reason,
            "check_results": [c.model_dump() for c in state.revised.check_results],
            "chains": [{"id": h.id, "tf": h.tf, "is_null": h.is_null, "probability": round(h.probability, 4)}
                       for h in state.revised.hypotheses],
            "grades": [g.model_dump() for g in state.grades1], "grades_changed": changed,
            "max_probability_change": round(dp, 4), "problems": list(state.problems),
            "critic_checks": [c.model_dump() for c in state.checks]})
        if not ran:
            state.stop_reason = f"round 1: no call to run{note}"
            break
        if not new:
            state.stop_reason = "round 1: its calls brought no new information"
            break
        if answer(state) == top_before:
            state.stop_reason = f"round {rnd} left the top chain and the grades of its links unchanged"
            break
    else:
        state.stop_reason = f"round limit ({max_rounds})"
    state.ledger.log("refine", "stop", state.stop_reason)
