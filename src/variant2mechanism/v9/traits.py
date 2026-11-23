"""Conservative trait identity, separate from broader retrieval queries.

Normalise orthography, never infer synonyms, measurement types or populations.
Ontology ids are provenance; a shared broad id cannot erase different source labels.
"""

import re
from collections.abc import Iterable

SPELLINGS = {
    "haemoglobin": "hemoglobin", "haematocrit": "hematocrit", "anaemia": "anemia",
    "foetal": "fetal", "leucocyte": "leukocyte", "leucocytes": "leukocytes",
    "leukaemia": "leukemia", "tumour": "tumor", "tumours": "tumors",
}
ONTOLOGY_ID = re.compile(r"(?:https?://[^\s]+[/#])?([a-z][a-z0-9]*)[:_](\d+)", re.I)


def ontology_id(value: str | None) -> str | None:
    hit = ONTOLOGY_ID.fullmatch((value or "").strip())
    return f"{hit[1].upper()}_{hit[2]}" if hit else None


def trait_key(value: str | None) -> str:
    if ident := ontology_id(value):
        return ident
    words = re.sub(r"[^0-9a-z]+", " ", (value or "").casefold()).split()
    return " ".join(SPELLINGS.get(w, w) for w in words)


def trait_identity(label: str, canonical_id: str | None, names: Iterable[str]) -> bool:
    """Require a source label match for named phenotypes; ids alone match only id-only entities.

    This intentionally refuses unverified semantic synonyms. Copy a source label instead.
    Multiple mapped ontology terms in one record are not assumed to be synonyms of one another.
    """
    keys = {trait_key(n) for n in names} - {""}
    if not keys:
        return False
    if label:
        # Source mappings are often incomplete or mix phenotype and population ids. A missing annotation is
        # not a contradiction of an identical full source label; ids still cannot rescue a different label.
        return trait_key(label) in keys
    ident = ontology_id(canonical_id)
    ids = {key for key in keys if ontology_id(key)}
    return bool(ident and ident in ids)


def trait_query_match(query: str, names: Iterable[str]) -> bool:
    """Whole-word retrieval filter, not permission to attach evidence to a claim."""
    key = trait_key(query)
    if not key:
        return False
    if ontology_id(query):
        return any(key == trait_key(n) for n in names)
    pattern = re.compile(rf"(?<![a-z0-9]){re.escape(key)}(?![a-z0-9])")
    return any(pattern.search(trait_key(n)) for n in names if n)
