"""Generate (generator): 3 to 5 chains, exactly one null (spec 2, 8.2). Also the one-call `single` configuration."""

from ..case import RunState, prompt
from ..schemas import Chains, Revised, check_chains, check_revised


def chains_json(hyps) -> str:
    return "[\n" + ",\n".join(h.model_dump_json() for h in hyps) + "\n]"


def generate(state: RunState) -> None:
    res = state.llm.call("generator", "generate", prompt("generator_system"), state.user_message(prompt("generate")),
                         output_model=Chains, check=lambda c: Chains(hypotheses=check_chains(c.hypotheses)))
    state.v0 = res.parsed.hypotheses
    state.ledger.add_chains("generate", 0, state.v0)


def single(state: RunState) -> None:
    res = state.llm.call("generator", "single", prompt("generator_system"),
                         state.user_message(prompt("single"), with_evidence=False), output_model=Revised,
                         check=check_revised)
    state.revised = res.parsed
    state.v0 = res.parsed.hypotheses
    state.ledger.add_chains("single", 1, state.revised.hypotheses)
