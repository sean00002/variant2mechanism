"""A bounded retry against the original source, with code-copied sentence spans."""

import json
import re


def spans(text):
    """Whole sentence windows, never arbitrary token ranges that could cut off a negation."""
    bounds = [0, *(m.end() for m in re.finditer(r"[.!?]\s+(?=[A-Z(])", text)), len(text)]
    items = []
    for start, end in zip(bounds, bounds[1:], strict=False):
        while start < end and text[start].isspace():
            start += 1
        while end > start and text[end - 1].isspace():
            end -= 1
        if 20 <= end - start <= 600:
            items.append({"selector": f"@span:{start}:{end}", "text": text[start:end]})
    return items


def materialise(record, article):
    """Selectors refer to one saved section. Free-form quotations still pass the existing verifier."""
    if not record.passage.startswith("@span:"):
        return record
    from .literature import ExtractionRefused
    section = next((s for s in article.sections if s.location == record.location), None)
    selected = next((s for s in spans(section.text) if s["selector"] == record.passage), None) if section else None
    if selected is None:
        raise ExtractionRefused("invalid source span: select one of the whole-sentence selectors at this location")
    return record.model_copy(update={"passage": selected["text"]})


def packet(graph, run_dir, events):
    from .literature import ExtractionRefused, find_read, load_article
    from .schemas import ExperimentRecord
    rows = []
    for event in events[:6]:
        record = ExperimentRecord.model_validate(event.details["experiment"])
        try:
            call = find_read(graph, record)
            article = load_article(run_dir, call)
            section = next(s for s in article.sections if s.location == record.location)
        except (ExtractionRefused, ValueError, StopIteration, OSError, AttributeError, TypeError):
            continue
        rows.append({"question_id": event.details["question_id"], "read_id": call.tool_call_id,
                     "failure": event.concise_reason, "failed_experiment": record.model_dump(mode="json"),
                     "source_location": section.location, "whole_sentence_choices": spans(section.text)[:16]})
    if not rows:
        return ""
    data = json.dumps(rows, ensure_ascii=False).replace("<", "\\u003c").replace(">", "\\u003e")
    return ("\nExtraction repair: one bounded attempt using the ORIGINAL sources below. Choose an exact source "
            "sentence by writing its @span:start:end selector in passage; code copies it verbatim. Recheck the "
            "assay, variant, direction and scope; a valid quote alone is not sufficient. Reuse accepted evidence "
            "and existing claims; do not duplicate them. Do not search or reread another paper to repair a quote. "
            "If unresolved, retain the observation in paper scope or state the processing gap.\n<data>" + data + "</data>")
