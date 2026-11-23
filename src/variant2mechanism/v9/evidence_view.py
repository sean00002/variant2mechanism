"""Bounded model views of an unchanged evidence store; omission is never a scientific rejection."""

import json
from collections import defaultdict


def ordered(ids):
    return sorted(set(ids), key=lambda x: int(x[1:]))


def index_lines(graph, ids, max_chars=18000):
    groups = defaultdict(list)
    for eid in ordered(ids):
        e = graph.evidence[eid]
        key = (e.evidence_class, tuple(e.about_genes), tuple(e.about_traits),
               e.context.label if e.context else "unspecified", e.allele, e.direction)
        groups[key].append(eid)
    lines, used, omitted = [], 0, 0
    for key, members in groups.items():
        cls, genes, traits, context, allele, direction = key
        sources = {s for eid in members for s in graph.evidence[eid].source_ids}
        line = json.dumps(dict(ids=members, evidence_class=cls, genes=genes, traits=traits, context=context,
                               allele=allele, direction=direction, source_count=len(sources)), ensure_ascii=False)
        line = line.replace("<", "\\u003c").replace(">", "\\u003e")
        if used + len(line) <= max_chars:
            lines.append(line)
            used += len(line)
        else:
            omitted += len(members)
    return [f"Compact index: {len(set(ids))} records in {len(groups)} scope groups; {omitted} records outside the "
            "display bound. All records remain in the graph. Use evidence_inspect with evidence_ids, or query and "
            "offset, for full records. Grouping does not merge studies, confer support or reject candidates.", *lines]


def packet_lines(graph, ids, render, claim_ids=()):
    ids = ordered(ids)
    linked = {x.evidence_id for c in graph.claims.values() for x in c.evidence_links}
    priority = sorted(ids, key=lambda eid: (graph.evidence[eid].origin != "literature", eid not in linked,
                                          int(eid[1:])))
    # A small packet stays verbatim; in a large one retain measured literature and claim-linked detail first.
    detailed, size = [], 0
    for eid in priority:
        lines = render(graph, eid, claim_ids)
        length = sum(map(len, lines))
        if len(detailed) < 20 and size + length <= 24000:
            detailed.append(eid)
            size += length
    rest = set(ids) - set(detailed)
    return ([line for eid in detailed for line in render(graph, eid, claim_ids)] +
            (index_lines(graph, rest) if rest else []))
