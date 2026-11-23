"""Bounded, persistent unread-paper leads derived from tool outputs; never scientific evidence."""

import json

from .graph import ClaimGraph


def _keys(record: dict) -> set[str]:
    keys = {f"{k}:{str(record[k]).casefold()}" for k in ("pmid", "pmcid", "doi") if record.get(k)}
    if record.get("title"):
        keys.add("title:" + " ".join(record["title"].casefold().rstrip(".").split()))
    return keys


def unread_leads(graph: ClaimGraph, limit: int = 12) -> list[dict]:
    """Most recent discovery calls first; non-review candidates before reviews within each call.

    Reading a full-text article retires the lead, not the scientific question. An abstract-only read does not
    retire its full-text lead. A read with failed extraction is handled by the existing processing-gap mechanism.
    """
    read = set()
    for call in graph.tool_calls.values():
        if call.tool_name == "literature_read" and call.execution_status == "success":
            for obs in call.observations:
                if obs.get("kind") == "article" and obs.get("access") == "full_text":
                    read |= _keys(obs)
    seen = set(read)
    leads = []
    for tid, call in reversed(list(graph.tool_calls.items())):
        if call.execution_status != "success" or call.tool_name not in ("literature_search", "literature_read"):
            continue
        candidates = [o for o in call.observations if (call.tool_name == "literature_search" or
                                                      o.get("kind") == "reference")]
        candidates.sort(key=lambda o: "review" in str(o.get("publication_type", "")).casefold())
        for obs in candidates:
            keys = _keys(obs)
            if not keys or keys & seen:
                continue
            seen |= keys
            leads.append({"from_call": tid, "kind": "citation" if obs.get("kind") == "reference" else "search",
                          **{k: obs.get(k) for k in ("pmid", "pmcid", "doi", "title", "publication_type")},
                          "reference_id": obs.get("reference_id"),
                          "discovery_query": call.query_parameters.get("query")})
    return leads[:limit]


def context_lines(graph: ClaimGraph) -> list[str]:
    leads = unread_leads(graph)
    if not leads:
        return []
    return ["Unread full-text leads (bounded to 12, not a completeness claim). These are pointers, NOT evidence. "
            "Choose a lead that could resolve an important mechanistic gap before repeating a search or reading "
            "another association summary. Do not call a non-review paper experimental until inspecting it.",
            *(json.dumps(x, ensure_ascii=False) for x in leads)]
