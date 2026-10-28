"""Pairwise comparison of the chains (after the last round; `tournament.enabled`).

The critic compares every pair of chains, each pair twice with the order swapped, and says which of the two the
evidence supports better: A, B or neither. Models judge "which of these two" more reliably than they state absolute
probabilities, and asking both orders cancels a preference for the first or second position: a pair that changes
winner with the order counts as a tie. Code turns the games into a ranking with a Bradley-Terry fit.
"""

import json
from itertools import combinations

import numpy as np

from ..case import RunState, prompt
from ..schemas import Comparison

SCORE = {"A": 1.0, "B": 0.0, "neither": 0.5}       # the score of the chain shown as A


def bradley_terry(ids: list[str], games: list[tuple[str, str, float]], iters: int = 500) -> dict[str, float]:
    """Strengths that sum to 1, from games (i, j, score of i: 1 a win, 0.5 a tie, 0 a loss). Each pair also gets one
    virtual tie, so a chain that never wins keeps a small strength and the fit always exists."""
    at = {k: n for n, k in enumerate(ids)}
    n = len(ids)
    wins, count = np.zeros(n), np.zeros((n, n))
    for i, j, s in games:
        wins[at[i]] += s
        wins[at[j]] += 1 - s
        count[at[i], at[j]] += 1
        count[at[j], at[i]] += 1
    for a, b in combinations(range(n), 2):
        wins[a] += 0.5
        wins[b] += 0.5
        count[a, b] += 1
        count[b, a] += 1
    p = np.full(n, 1 / n)
    for _ in range(iters):
        denom = np.array([sum(count[a, b] / (p[a] + p[b]) for b in range(n) if b != a) for a in range(n)])
        p = wins / denom
        p /= p.sum()
    return {k: round(float(p[at[k]]), 4) for k in ids}


def _grades(state: RunState, ids: set[str]) -> str:
    return "\n".join(f"{g.hypothesis_id}.{g.step}: {g.status} ({g.reason})"
                     for g in state.current_grades() if g.hypothesis_id in ids) or "none"


def compare(state: RunState, a, b) -> Comparison:
    hide = {"probability"}                    # judged on the evidence, not on the probabilities the model gave
    instruction = prompt("compare").format(a=f"Chain A ({a.id}):\n{json.dumps(a.model_dump(exclude=hide))}",
                                           b=f"Chain B ({b.id}):\n{json.dumps(b.model_dump(exclude=hide))}",
                                           grades=_grades(state, {a.id, b.id}))
    res = state.llm.call("critic", "compare", prompt("critic_system"), state.user_message(instruction),
                         output_model=Comparison)
    return res.parsed


def tournament(state: RunState) -> dict:
    """Every pair in both orders; the games, the Bradley-Terry strengths and the ranking they give."""
    chains = state.current_chains()
    matches, games = [], []
    for a, b in combinations(chains, 2):
        first, second = compare(state, a, b), compare(state, b, a)
        s1, s2 = SCORE[first.winner], 1 - SCORE[second.winner]          # both as the score of a
        games += [(a.id, b.id, s1), (a.id, b.id, s2)]
        matches.append({"pair": [a.id, b.id], "scores": [s1, s2], "first": first.model_dump(),
                        "second": second.model_dump()})
    strengths = bradley_terry([h.id for h in chains], games)
    out = {"matches": matches, "strengths": strengths,
           "ranking": sorted(strengths, key=lambda k: -strengths[k])}
    state.tournament = out
    state.ledger.log("tournament", "done", {"strengths": strengths, "ranking": out["ranking"]})
    return out


def beats_null(result: dict | None, chain_id: str, null_id: str) -> bool | None:
    """Did the chain beat the null in both orders? None when there was no tournament or no such match."""
    if not result:
        return None
    for m in result["matches"]:
        if set(m["pair"]) == {chain_id, null_id}:
            mine = m["scores"] if m["pair"][0] == chain_id else [1 - s for s in m["scores"]]
            return all(s == 1.0 for s in mine)
    return None
