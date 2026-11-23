"""A fake model transport (OpenAI chat-completions replies): answers by output schema, and scripts the plan and the
chain probabilities of each refinement round."""

import json
import re

STEPS = ["binding", "element", "gene", "cell_type", "phenotype"]


def chain(hid, tf, allele, prob, ev="E01"):
    return {"id": hid, "title": f"{tf} chain", "is_null": False, "tf": tf,
            "allele_binding_more": allele, "element": "enhancer", "target_gene": "MYC", "cell_type": "colon",
            "links": [{"step": s, "claim": f"{tf} {s}", "evidence_ids": [ev] if s != "phenotype" else []}
                      for s in STEPS],
            "predictions": [f"{tf} ChIP at the SNP"], "falsified_if": ["no allelic imbalance"], "probability": prob}


NULL = {"id": "H3", "title": "No TF effect", "is_null": True, "tf": None,
        "allele_binding_more": None, "element": None, "target_gene": None, "cell_type": None, "links": [],
        "predictions": ["no allelic expression"], "falsified_if": ["allelic ChIP imbalance"], "probability": 0.2}


def default_chains():
    return [chain("H1", "TCF7L2", "ref", 0.5),
            chain("H2", "LEF1", "ref", 0.3), NULL]


def message(content, finish="stop", usage=None, tool_calls=None, reasoning="sig-fake"):
    msg = {"role": "assistant", "content": content, "reasoning_details": [{"type": "reasoning.text", "id": reasoning}]}
    if tool_calls:
        msg["tool_calls"] = tool_calls
    return {"id": "gen-fake", "model": "fake", "provider": "Fake", "choices": [{"finish_reason": finish,
                                                                               "message": msg}],
            "usage": usage or {"prompt_tokens": 1000, "completion_tokens": 500}}


def text(obj):
    return json.dumps(obj)


PLANS = [
    [("chip_peaks", {"tf": "TCF7L2", "biosample": "HCT116"}, "H1.binding", "a TCF7L2 peak in HCT116 supports H1"),
     ("eqtl_lookup", {"tissue": "Colon"}, "H1.gene", "a colon eQTL for MYC supports H1.gene")],
    [("gene_disease", {"gene": "MYC"}, "H1.phenotype", "MYC linked to colorectal cancer supports H1"),
     ("chip_peaks", {"tf": "TCF7L2", "biosample": "HCT116"}, "H1.binding", "the same call again"),
     ("nope", {}, "H2.gene", "an unknown tool")],
    [],
]


class FakeTransport:
    """Round k plans `plans[k]` (each call: tool, arguments, the link it resolves, the expected result) and revises to
    `revise_probs[k]`; by default round 2 repeats a round-1 call and names an unknown tool, and round 3 plans nothing."""

    def __init__(self, chains=None, plans=None, revise_probs=None, quote_from_abstract=True, compare=None):
        self.calls: list[dict] = []
        self.compare = compare          # (id shown as A, id shown as B) -> "A", "B" or "neither"; default: earlier wins
        self.chains = chains or default_chains()
        self.plans = PLANS if plans is None else plans
        self.revise_probs = revise_probs
        self.quote_from_abstract = quote_from_abstract

    def seen(self, title):
        return sum(1 for c in self.calls if (c.get("response_format") or {}).get("json_schema", {}).get(
            "schema", {}).get("title") == title) - 1

    def __call__(self, params):
        self.calls.append(json.loads(json.dumps(params, default=str)))
        fmt = params.get("response_format")
        title = fmt["json_schema"]["schema"].get("title") if fmt else None
        if title == "Plan":
            k = self.seen("Plan")
            calls = self.plans[k] if k < len(self.plans) else []
            return message(text({"calls": [{"tool": t, "args_json": json.dumps(a), "resolves": r, "expected": e}
                                           for t, a, r, e in calls],
                                 "stop_reason": "" if calls else "Nothing left could change a grade."}))
        if title == "Quotes":
            prompt = next(m["content"] for m in params["messages"] if m["role"] == "user")
            m = re.search(r"PMID (\d+)\nTitle: .*?\nAbstract: (.+?)(?:\n\nPMID|\Z)", prompt, re.S)
            if not m:
                return message(text({"quotes": []}))
            sentence = m.group(2).split(". ")[0] + "." if self.quote_from_abstract else "An invented sentence."
            return message(text({"quotes": [{"pmid": m.group(1), "sentence": sentence}]}))
        if title == "Chains":
            return message(text({"hypotheses": self.chains}))
        if title == "CritiqueOut":                         # the critique and each round's regrade
            grades = [{"hypothesis_id": c["id"], "step": s, "status": "supported" if s == "binding" else "weak",
                       "reason": "fake"} for c in self.chains if not c["is_null"] for s in STEPS]
            return message(text({"grades": grades, "problems": ["direction unclear"],
                                 "checks": [{"tool": "chip_peaks", "args_json": '{"tf": "TCF7L2"}',
                                             "resolves": "H1.binding", "why": "ChIP"},
                                            {"tool": "nope", "args_json": "{}", "resolves": "H2.gene",
                                             "why": "bad tool"}]}))
        if title in ("Revised", "RevisedRound"):
            chains = self.chains
            k = self.seen("RevisedRound")
            if title == "RevisedRound" and self.revise_probs is not None:
                probs = self.revise_probs[min(k, len(self.revise_probs) - 1)]
                chains = [{**c, "probability": p} for c, p in zip(self.chains, probs, strict=True)]
            extra = {"check_results": [{"call": "chip_peaks", "observed": "a peak", "as_expected": "yes"}]} \
                if title == "RevisedRound" else {}
            return message(text(extra | {"hypotheses": chains,
                                 "matrix": [{"test": "allele-specific ChIP", "cost": "low",
                                             "outcomes": [{"hypothesis_id": c["id"], "outcome": "x"}
                                                          for c in self.chains], "separates_top_two": True}],
                                 "next_experiment": "Allele-specific TCF7L2 ChIP-qPCR in HCT116."}))
        if title == "Comparison":
            prompt = next(m["content"] for m in params["messages"] if m["role"] == "user")
            a, b = (re.search(rf"Chain {x} \((\w+)\)", prompt).group(1) for x in "AB")
            order = [c["id"] for c in self.chains]
            winner = self.compare(a, b) if self.compare else ("A" if order.index(a) < order.index(b) else "B")
            return message(text({"winner": winner, "reason": "fake", "evidence_ids": ["E01"]}))
        raise AssertionError(f"unexpected call: {title}")
