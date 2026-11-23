"""Biosample and context normalisation, and the exact / proxy / different / unknown comparison (SPEC 3.4, 13.13).

Why this exists: evidence is only as good as the context it was measured in. v8 resolved a Hep3B request to HepG2
(context/biosample_match.yaml) and then treated HepG2 peaks as "bound here". v9 keeps every biosample's real identity
(v9/biosamples.yaml) and says how far an observation transfers:

    exact      the same normalised biosample, or the same tissue when neither side names a biosample
    proxy      a shared organ-level tissue (primary hepatocytes vs liver), a declared proxy (Hep3B vs HepG2), or the
               same biosample in another species, or under another (or an unstated) condition than the claim's
    different  both sides are recognised and unrelated
    unknown    either side has no context, or a side names something the table does not recognise

Two distinct cell lines are proxies only when a table declares it: an organ-level tissue says little about how alike
two transformed lines are (K562 and GM12878 are both "blood"). A tissue, a primary cell or a cell type shares its
tissue with the lines derived from it.

A scope that names only a species or a condition is still a scope (mouse, ER stress): only a scope with no biosample,
no tissue, no condition and the default species asserts no context. Graph code calls `link_applicability`, which adds
one rule to `compare_context`: an unscoped claim and an unscoped observation agree exactly when the observation's
class does not depend on a context (a coordinate overlap, a sequence-level prediction, a population association). A
cell-based observation that lost its context, or a measured null without a stated scope, stays unknown.

Names are matched the v8 way (context.occupancy.norm: spaces, hyphens and underscores removed, case ignored, a trailing
"(...)" note dropped) and v8's declared proxies are read from context/biosample_match.yaml, which v9 never edits.
"""

import re
from dataclasses import dataclass, field
from functools import lru_cache
from pathlib import Path

import yaml

from ..context.occupancy import MATCH_FILE as V8_MATCH_FILE
from ..context.occupancy import context_key, norm
from .schemas import Applicability, ContextScope, ContextSource, Variant

BIOSAMPLES_FILE = Path(__file__).with_name("biosamples.yaml")
UNSPECIFIED = {"", "none", "na", "n/a", "unknown", "unspecified", "not supplied", "none supplied"}
SPECIES = {"human": ("human", "humans", "homo sapiens"), "mouse": ("mouse", "mice", "murine", "mus musculus"),
           "rat": ("rat", "rats", "rattus norvegicus")}
QUALIFIER_WORDS = ("adult", "fetal", "foetal", "normal")
CELL_SUFFIXES = ("cell line", "cells", "cell")


@dataclass(frozen=True)
class Genotype:
    variant: str                 # an rsID
    key: str                     # GRCh38:chrom:pos:ref:alt
    genotype: str
    source: str


@dataclass(frozen=True)
class Biosample:
    name: str
    kind: str
    tissue: str | None
    organ: bool = False          # the name is a whole organ: its scope carries the tissue only
    aliases: tuple[str, ...] = ()
    depmap: str | None = None
    rrid: str | None = None
    ontology: str | None = None
    in_screen_core: bool = False
    proxies: tuple[str, ...] = ()
    genotypes: tuple[Genotype, ...] = ()
    note: str = ""

    def genotype_at(self, variant: Variant) -> Genotype | None:
        """The genotype a source states for this biosample at the variant, matched by rsID or GRCh38 key."""
        for g in self.genotypes:
            if (variant.rsid and g.variant.lower() == variant.rsid.lower()) or g.key == variant.key:
                return g
        return None


@dataclass
class BiosampleTable:
    records: dict[str, Biosample]
    tissues: dict[str, tuple[str, ...]]
    by_alias: dict[str, str] = field(default_factory=dict)       # norm(name or alias) -> record name
    by_depmap: dict[str, str] = field(default_factory=dict)      # ACH id -> record name
    proxy_pairs: set[frozenset[str]] = field(default_factory=set)

    def __post_init__(self):
        for rec in self.records.values():
            for alias in (rec.name, *rec.aliases):
                self.by_alias.setdefault(norm(alias), rec.name)
            if rec.depmap:
                self.by_depmap[rec.depmap] = rec.name
            for other in rec.proxies:
                self.proxy_pairs.add(frozenset({rec.name, other}))

    def record(self, name: str | None) -> Biosample | None:
        """The record for a biosample name, alias or DepMap ID (any of the forms v8 used), or None."""
        if not name:
            return None
        text = context_key(name)
        m = re.match(r"(?:DepMap:)?(ACH-\d+)$", text)
        if m:
            found = self.by_depmap.get(m.group(1))
            return self.records[found] if found else None
        found = self.by_alias.get(norm(text))
        return self.records[found] if found else None

    def tissue_named(self, text: str) -> str | None:
        """The tissue when the text is just an organ-level tissue name ("liver", "liver tissue")."""
        key = norm(re.sub(r"\s+tissue$", "", text.strip().lower()))
        return next((t for t in self.tissues if norm(t) == key), None)

    def tissue_for(self, text: str) -> str | None:
        """The one tissue whose keywords appear in free text; None when none or several match."""
        low = f" {text.lower()} "
        hits = {t for t, words in self.tissues.items()
                if any(re.search(rf"(?<![a-z]){re.escape(w)}", low) for w in words)}
        return hits.pop() if len(hits) == 1 else None

    def tissue_of(self, text: str) -> str:
        """A tissue field normalised: a tissue name, else the one keyword match, else the text in lower case."""
        return self.tissue_named(text) or self.tissue_for(text) or " ".join(text.lower().split())

    def declared_proxy(self, a: str, b: str) -> bool:
        return frozenset({a, b}) in self.proxy_pairs


def _records(raw: list[dict]) -> dict[str, Biosample]:
    out: dict[str, Biosample] = {}
    for r in raw:
        genotypes = tuple(Genotype(g["variant"], g["key"], g["genotype"], g["source"])
                          for g in r.get("genotypes") or [])
        rec = Biosample(name=r["name"], kind=r["kind"], tissue=r.get("tissue"), organ=bool(r.get("organ")),
                        aliases=tuple(r.get("aliases") or ()), depmap=r.get("depmap"), rrid=r.get("rrid"),
                        ontology=r.get("ontology"), in_screen_core=bool(r.get("in_screen_core")),
                        proxies=tuple(r.get("proxies") or ()), genotypes=genotypes, note=r.get("note") or "")
        if rec.name in out:
            raise ValueError(f"biosamples.yaml: {rec.name} is listed twice")
        out[rec.name] = rec
    return out


def _v8_proxies(path: Path, table: BiosampleTable) -> None:
    """Add the proxies v8's yaml declares (an entry with a `proxy:` note maps its line to a stand-in biosample)."""
    entries = yaml.safe_load(Path(path).read_text()) or {}
    for key, entry in entries.items():
        if not entry or not entry.get("proxy"):
            continue
        line = table.record(key) or table.record(entry.get("line"))
        for stand_in in entry.get("biosamples") or []:
            other = table.record(stand_in)
            if line and other and line.name != other.name:
                table.proxy_pairs.add(frozenset({line.name, other.name}))


@lru_cache(maxsize=4)
def load_table(path: str | Path = BIOSAMPLES_FILE, v8_path: str | Path = V8_MATCH_FILE) -> BiosampleTable:
    """The v9 biosample table plus v8's declared proxies; both files are read, never written."""
    data = yaml.safe_load(Path(path).read_text())
    tissues = {t: tuple(w.lower() for w in words) for t, words in (data.get("tissues") or {}).items()}
    table = BiosampleTable(records=_records(data.get("biosamples") or []), tissues=tissues)
    for rec in table.records.values():
        if rec.tissue and rec.tissue not in tissues:
            raise ValueError(f"biosamples.yaml: {rec.name} names tissue {rec.tissue!r}, which has no keywords")
        for other in rec.proxies:
            if other not in table.records:
                raise ValueError(f"biosamples.yaml: {rec.name} declares an unknown proxy {other!r}")
    if Path(v8_path).exists():
        _v8_proxies(Path(v8_path), table)
    return table


def species_of(text: str) -> str:
    """'Homo sapiens', 'humans' -> 'human'; 'mice', 'murine' -> 'mouse'; anything else in lower case."""
    low = " ".join(text.lower().split())
    return next((name for name, words in SPECIES.items() if low in words), low)


def _strip_words(text: str) -> tuple[str, str | None]:
    """The label without species and qualifier words, and the species it named (if any)."""
    low, named = text.lower(), None
    for name, words in SPECIES.items():
        for word in words:
            if re.search(rf"\b{word}\b", low):
                named = named or name
                low = re.sub(rf"\b{word}\b", " ", low)
    for word in QUALIFIER_WORDS:
        low = re.sub(rf"\b{word}\b", " ", low)
    return " ".join(low.split()), named


def _from_record(rec: Biosample, scope: ContextScope, variant: Variant | None) -> ContextScope:
    """A scope filled from its table record. The record's kind wins over a proposer's (HepG2 is a cell line whatever
    a label says); a proposer's kind is kept only where the record does not know it."""
    genotype = scope.genotype
    if genotype is None and variant is not None and (g := rec.genotype_at(variant)):
        genotype = g.genotype
    kind = rec.kind if rec.kind != "unknown" else scope.biosample_kind
    return scope.model_copy(update={"biosample": None if rec.organ else rec.name, "tissue": rec.tissue,
                                    "biosample_kind": kind, "genotype": genotype})


def _normalise(scope: ContextScope, variant: Variant | None, table: BiosampleTable) -> ContextScope:
    scope = scope.model_copy(update={"species": species_of(scope.species or "human")})
    if scope.tissue:
        scope = scope.model_copy(update={"tissue": table.tissue_of(scope.tissue)})
    if scope.biosample:
        rec = table.record(scope.biosample)
        if rec:
            return _from_record(rec, scope, variant)
        name = " ".join(scope.biosample.split())
        return scope.model_copy(update={"biosample": name, "tissue": scope.tissue or table.tissue_for(name)})
    if scope.tissue:
        return scope
    text = " ".join(context_key(scope.label).split())
    for prefix in ("GTEx:", "DepMap:subtype=", "ENCODE:"):
        if text.startswith(prefix):
            text = text[len(prefix):].strip()
    if text.lower() in UNSPECIFIED:
        return scope
    bare, named = _strip_words(text)
    if named and scope.species == "human":
        scope = scope.model_copy(update={"species": named})
    rec = table.record(text) or table.record(bare)
    for suffix in CELL_SUFFIXES:
        if rec is None and bare.endswith(" " + suffix):
            rec = table.record(bare[: -len(suffix)].strip())
    if rec is not None:
        return _from_record(rec, scope, variant)
    if tissue := table.tissue_named(bare):
        return scope.model_copy(update={"tissue": tissue, "biosample_kind": "tissue"})
    return scope.model_copy(update={"biosample": text, "tissue": table.tissue_for(text)})


def normalise_scope(scope: ContextScope | None, variant: Variant | None = None,
                    table: BiosampleTable | None = None) -> ContextScope | None:
    """Fill a ContextScope's biosample, kind, tissue, species and genotype from the table. A known biosample becomes
    its record's name (an organ becomes a tissue-only scope); an unknown explicit biosample is kept as given; with
    neither biosample nor tissue, the label is resolved (record, organ-level tissue, keyword tissue, or the label
    itself as an unrecognised biosample)."""
    return None if scope is None else _normalise(scope, variant, table or load_table())


def scope_from_label(label: str, source: ContextSource = "supplied", species: str = "human",
                     condition: str | None = None, variant: Variant | None = None,
                     table: BiosampleTable | None = None) -> ContextScope:
    """A normalised ContextScope from a free label, such as a supplied context or an assay's biosample name."""
    scope = ContextScope(label=label, species=species, condition=condition, source=source)
    return _normalise(scope, variant, table or load_table())


def _condition(scope: ContextScope) -> str:
    return " ".join((scope.condition or "").lower().split())


def is_unscoped(scope: ContextScope | None) -> bool:
    """The scope asserts no context: no biosample, no tissue, no condition and the default species. A scope naming
    only a species (mouse) or only a condition (ER stress) is a scope."""
    return scope is None or (not scope.biosample and not scope.tissue and not _condition(scope) and not scope.genotype
                             and species_of(scope.species or "human") == "human")


def scope_key(scope: ContextScope | None) -> str | None:
    """The context part of a claim's dedup key: normalised biosample, else tissue, else "any"; species and condition
    are added when set, so mouse liver, or a claim scoped only to a stressed condition, is a different claim from the
    unscoped or basal human one. None for an unscoped scope."""
    scope = normalise_scope(scope)
    if scope is None or is_unscoped(scope):
        return None
    key = norm(scope.biosample) if scope.biosample else f"tissue:{scope.tissue}" if scope.tissue else "any"
    if scope.species != "human":
        key = f"{scope.species}:{key}"
    if scope.condition:
        key = f"{key}|{_condition(scope)}"
    if scope.genotype:
        key = f"{key}|genotype:{norm(scope.genotype)}"
    return key


def compare_context(claim_ctx: ContextScope | None, ev_ctx: ContextScope | None,
                    table: BiosampleTable | None = None) -> Applicability:
    """How an observation's context transfers to a claim's context (see the module docstring)."""
    table = table or load_table()
    a, b = normalise_scope(claim_ctx, table=table), normalise_scope(ev_ctx, table=table)
    if a is None or b is None or is_unscoped(a) or is_unscoped(b):
        return "unknown"
    ba = norm(a.biosample) if a.biosample else None
    bb = norm(b.biosample) if b.biosample else None
    same_species = a.species == b.species
    # A claim scoped to a condition transfers exactly only from evidence stating the same condition; a claim with no
    # condition is the general case, which evidence under any condition instantiates.
    same_condition = not a.condition or _condition(a) == _condition(b)
    if (ba and bb and ba == bb) or (not ba and not bb and a.tissue == b.tissue):
        return "exact" if same_species and same_condition else "proxy"
    if a.biosample and b.biosample and table.declared_proxy(a.biosample, b.biosample):
        return "proxy"
    two_lines = a.biosample_kind == b.biosample_kind == "cell_line"
    if a.tissue and b.tissue and a.tissue == b.tissue and not two_lines:
        return "proxy"
    known_a = bool(a.tissue) or table.record(a.biosample) is not None
    known_b = bool(b.tissue) or table.record(b.biosample) is not None
    return "different" if known_a and known_b else "unknown"


def link_applicability(claim_ctx: ContextScope | None, ev_ctx: ContextScope | None, *, context_free: bool,
                       table: BiosampleTable | None = None) -> Applicability:
    """What graph code stores on an evidence link. When neither side is scoped, exact only for an observation whose
    class does not depend on a context (`context_free`: schemas.CONTEXT_FREE_CLASSES, never a measured null), else
    unknown; otherwise compare_context."""
    table = table or load_table()
    if is_unscoped(normalise_scope(claim_ctx, table=table)) and is_unscoped(normalise_scope(ev_ctx, table=table)):
        return "exact" if context_free else "unknown"
    return compare_context(claim_ctx, ev_ctx, table=table)
