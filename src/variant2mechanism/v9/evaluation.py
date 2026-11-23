"""Evaluation (SPEC 10, 13.12): gold isolation, the gold claim specification and the audit of one run. Evaluator-only.

Nothing in the engine imports this module, and nothing it writes (eval/v9_gold_spec.json, a run's evaluation.json) is
read by the engine or shown to an agent. It works in three steps.

Gold isolation. `clean_request(row, arm)` is the only route from a gold row to a run: GRCh38 coordinates and the
origin from the row's explicit `origin` column (never from the label class, the disease, the variant's name or the
notes, so a cancer hotspot is not made somatic by its fame), plus, in the supplied-disease arm, the disease with its
bracketed text removed (the brackets name loci and genes: "(1p13)", "(FTO)"). Context is withheld in every arm (the
gold `expression_context` is derived from the labels); no TF, gene, PMID, note or literature cut-off is passed; the
request id is opaque (REQ- plus a hash of what the request holds). `label_strings(row)` lists every label-derived
string, so tests can show none reaches a request (and the engine's tests that none reaches a packet).

The gold specification. `build_gold_spec(csv)` turns each row mechanically into evaluator components: the TF member
(scored strictly), its QBiC-SELEX model-sharing group(s) from cache/groups.json and its Lambert 2018 DBD family (both
scored leniently, never collapsed with the member; no family credit when the gold TF is not in QBiC-SELEX coverage,
because such a case tests that the run says so instead of naming a relative), the binding direction of the alt
allele read from the direction text, the target gene(s), the context and the phenotype. Each entry keeps its CSV row,
so the audit derives the label strings from the same cells as the isolation tests. Alternatives stay empty because
the CSV states none; wherever reading the CSV needs a judgement (a family label that is not the Lambert DBD, a
direction that names no allele, several genes, a context the biosample table does not know, symbols the notes name),
the component is flagged `needs_review` with the reason. The spec records the sha256 of the CSV and of each reference
file it read, and is refused once any of them changes; the CSV is never edited. The spec is built "unreviewed": every
score against it is provisional until the user reviews it and sets its status to "reviewed".

The audit. `audit(run_dir, spec_entry)` reads a run folder (graph.json, plus metrics.json and manifest.json when
present) and reports: how the run ended (an explanation, an abstention, which is no_supported_explanation, or a
limitation; a run stopped by engine_error or cache_miss, whatever outcome it recorded, and a request refused as input
assessed nothing, so it is a case-level failure, scored as neither a miss nor an abstention nor a control's null);
component recovery by the run's answer (the leading or tied hypotheses its result names, none when it was decided
without a final comparison, counting only claims that stand: none the run contradicted in scope or superseded, and
none about another variant by the graph's claim_frame), each component with its own denominator (a control, a
capability gap, a run that assessed nothing, an input the run was given or a gold value that names nothing assessable
leaves the denominator); whether the run's input was the clean request (the case as supplied, never what the run
inferred or a tool found: recorded rsID aliases and the variants evidence names are the run's own work); candidate
retention (is an acceptable member, group, family or gene still available after the inventory, the proposal, the
activation and at the end: leading, active, deferred, eliminated (rejected, or dropped by a revision or
supersession), or listed by the QBiC-SELEX inventory but never sketched, "inventory_only"; a hypothesis code
reinstated after the contradiction behind its rejection was withdrawn is deferred, not eliminated); possible improper
eliminations (deferrals, rejections, revisions and supersessions whose reasons cite coverage data or a z, TPM or peak
ranking, since missing data and more-is-better readings must never decide; rejections resting only on proxy-context
contradictions, or on a contradiction that no longer stands; a rejection a reinstatement withdrew, and the deferral
that restored it, are not eliminations), with every reinstatement listed for a person to check; unsupported causal
claims of the answer; an evidence-fidelity sheet of the decisive links, with the variants each item names, for manual
review (never scored by code); and efficiency from the run's metrics and graph. Every flag is mechanical and left for
a person to judge. The graph's own rules are used, never copied: claim_frame, hypothesis_versions, sketched_groups
and variant_mention.
"""

import csv
import hashlib
import json
import math
import re
from collections import Counter
from collections.abc import Callable, Iterable, Mapping
from dataclasses import dataclass, field
from functools import lru_cache
from pathlib import Path
from typing import Any, Literal, NoReturn, get_args

from ..config import REPO, Config, ConfigError, load_config
from ..evaluation.gold import NEVER_IN_PROMPT, NONE_VALUES, is_control
from .context_match import BIOSAMPLES_FILE, BiosampleTable, compare_context, load_table, scope_from_label
from .graph import ClaimGraph, SymbolResolver, hypothesis_versions, sketched_groups
from .intake import (
    PROVENANCE_KEYS,
    Request,
    bracketed_parts,
    normalise_disease,
    parse_coordinates,
    request_id,
    strip_bracketed,
)
from .schemas import SPECIFIC_DIRECTIONS, Case, ContextScope, Evidence, Hypothesis, Relation, Variant

Arm = Literal["main", "supplied_disease"]
ARMS: tuple[Arm, ...] = get_args(Arm)
GOLD_SPEC_FILE = REPO / "eval" / "v9_gold_spec.json"
EVALUATION_FILE = "evaluation.json"
SPEC_VERSION = "v9-gold-spec/2"
UNREVIEWED, REVIEWED = "unreviewed", "reviewed"     # a spec's status: built mechanically / settled by the user
NOT_IN_COVERAGE = "not_in_coverage"                 # the CSV's score_level for a gold TF QBiC-SELEX cannot assess
ORIGIN_COLUMN = "origin"
COMPONENTS = ("tf_member", "tf_group", "tf_family", "direction", "target_gene", "context", "phenotype")
TF_COMPONENTS = ("tf_member", "tf_group", "tf_family")
CAUSAL_RELATIONS = frozenset({"alters_binding", "alters_regulatory_activity", "regulates", "affects_process",
                              "causal_at_locus", "contributes_to_trait", "alters_rna"})
RELATION_ORDER = {r: i for i, r in enumerate(get_args(Relation))}
ABSTENTION = "no_supported_explanation"         # the run assessed the case and found no supported explanation
LIMITATION = "input_or_capability_limitation"
# Stop reasons after which a run assessed nothing (compare.LIMITATION_STOPS): an internal failure or unusable model
# output (engine_error), or a reply or tool result missing from a cache-only run or a replay (cache_miss).
RUN_FAILURES = frozenset({"engine_error", "cache_miss"})
INPUT_STOPS = frozenset({"input_invalid", "unsupported_variant"})   # the request could not be assessed as given
RETAINED = ("leading", "active", "deferred")
STAGES = ("inventory", "proposal", "activation", "final")
LABEL_KINDS = ("identity", "tf", "group", "gene", "context", "disease", "bracketed", "source", "notes",
               "notes_tokens", "other")
NOT_LABELS = frozenset(NONE_VALUES) | {"not applicable", "control"}
STOPWORDS = frozenset({"and", "the", "for", "with", "from", "into", "via", "per", "its", "not", "of", "in", "on"})
APPLICABILITY_RANK = {"exact": 3, "proxy": 2, "unknown": 1, "different": 0}
POSITIVE = re.compile(r"\b(?:gains?|gained|creates?|created|binds more|more strongly|stronger|strengthens|"
                      r"increases?|higher)\b", re.I)
NEGATIVE = re.compile(r"\b(?:lose|loses|loss|lost|disrupts?|disrupted|abolish(?:es)?|ablates?|weakens?|weaker|"
                      r"reduces?|decreases?|lower|less)\b", re.I)
ALLELE_LETTER = re.compile(r"(?<![A-Za-z0-9])([ACGT])(?![A-Za-z0-9])")
ALLELE_WORD = re.compile(r"\b(alt|alternate|alternative|ref|reference)\b", re.I)
# Elimination reasons worth a person's look. Deliberately broad: a flag is never a verdict, and a missed phrasing
# hides exactly the elimination these checks exist for. Any mention of a coverage-type source (ChIP, peaks,
# occupancy, expression, TPM, annotation, cCREs, eQTLs, GTEx, ENCODE), or an absence of records, data, literature or
# GWAS hits, is flagged as possible missing-coverage reasoning; any z, rank, or comparative or superlative of an
# effect, score, binding or signal as possible more-is-better reasoning.
MISSING_COVERAGE = re.compile(
    r"\b(?:chip(?:-?(?:seq|exo))?|peaks?|occupan(?:cy|cies)|occupied|expression|expressed|tpm|fpkm|rpkm|"
    r"rna-?seq|annotations?|annotated|ccres?|eqtls?|gtex|encode)\b"
    r"|\b(?:no|zero|absent|absence|missing|lacks?|lacking|without|unavailable|insufficient|not (?:available|found|"
    r"assayed|tested|covered|reported))\b[^.;]{0,60}?\b(?:records?|data|literature|gwas|coverage)\b", re.I)
MORE_IS_BETTER = re.compile(
    r"(?<![\w|-])\|?z\|?(?:[- ]?scores?)?(?![\w|-])|\b(?:out)?rank(?:s|ed|ings?)?\b"
    r"|\b(?:lower|lowest|smaller|smallest|weaker|weakest|low|weak|modest|small|least|largest|highest|strongest|"
    r"greatest|most|top|higher|larger|stronger|bigger|biggest)\b[^.;]{0,30}?\b(?:z|scores?|effects?|predictions?|"
    r"predicted|binding|changes?|tpm|expression|peaks?|signals?|enrichment)\b", re.I)
RULES = {
    "tf_member": "strict: the answer names the gold TF itself (HGNC symbol), as a TF or as a participant of a complex "
                 "or binding event; naming its model-sharing group is not member credit",
    "tf_group": "lenient: the answer names a QBiC-SELEX model-sharing group holding the gold TF (cache/groups.json), "
                "or any TF of such a group",
    "tf_family": "lenient: the answer names any TF of the gold TF's Lambert 2018 DBD family; not applicable when the "
                 "gold TF is not in QBiC-SELEX coverage (score_level not_in_coverage), because the right answer there "
                 "is that it cannot be assessed, not a modelled relative",
    "direction": "the binding change of the alt allele relative to ref, read from the direction text; compared with "
                 "the answer's alters_binding claims about a TF matching at member, group or family level (member "
                 "level only when the gold TF is not in QBiC-SELEX coverage)",
    "target_gene": "the answer names one of the genes (HGNC symbols)",
    "context": "an answer context matches a gold scope exactly or as a proxy (v9 context_match)",
    "phenotype": "the answer's endpoint or a phenotype it names contains every word of a gold trait; not scored when "
                 "the run was given the disease",
    "answer": "the claims that stand of the leading or tied hypotheses the run's result names (a result decided "
              "without a final comparison names none, and the audit names none in its place): a claim the run "
              "assessed contradicted_in_scope, a superseded claim and a claim about another variant (by the graph's "
              "claim_frame, under which an rsID code recorded for the case variant, or its chrom:pos, names the case) "
              "earn nothing",
    "outcome": "an explanation (leading_explanation, partial_mechanism, multiple_explanations), an abstention "
               "(no_supported_explanation) or a limitation (input_or_capability_limitation). A run stopped by "
               "engine_error or cache_miss, whatever outcome it recorded, or refused as input (input_invalid, "
               "unsupported_variant), assessed nothing: a case-level failure to report and rerun, scored as neither a "
               "miss nor an abstention nor a control's null. A limitation the run concluded itself is its answer",
    "controls": "no component applies: the audit records the outcome and any supported causal claim of the answer "
                "(controls are evidence-sparse comparisons, not established biological nulls); a run that assessed "
                "nothing is not a null",
    "denominators": "a component counts only where it applies, the run assessed the case (see outcome), the run was "
                    "not given it as input and its gold value is defined",
    "review": "every score is provisional until the spec's status is 'reviewed'; after that, a component still marked "
              "needs_review stays provisional",
    "row": "each case keeps its CSV row as read: the isolation check derives the gold label strings from it, so it "
           "is never edited in the review (the CSV is the source)",
}
REVIEW_TEMPLATE = {"source": None, "intervention": None, "endpoint": None, "scope": None, "verdict": None, "note": ""}
REVIEW_HELP = ("Fill source, intervention, endpoint and scope with true or false after reading the source; verdict is "
               "one of faithful, misread, not_in_source, scope_exceeded. Code never fills these.")


class SuiteRefusal(ValueError):
    """An evaluation suite request refused before anything runs."""


# --- rows and reference data -----------------------------------------------------------------------------------------

def _cell(row: Mapping[str, Any], key: str) -> str:
    value = row.get(key)
    return "" if value is None else " ".join(str(value).split())


def _is_label(text: str) -> bool:
    return len(text) >= 3 and text.casefold() not in NOT_LABELS


def _split(text: str, separators: str = r"[,;/+]") -> list[str]:
    return [p.strip() for p in re.split(separators, text) if p.strip()]


def _identifiers(text: str) -> list[str]:
    """Identifier-like tokens: gene symbols, rsIDs, cytobands, hotspot names (TERT, rs6983267, 1p13, C228T)."""
    tokens = re.findall(r"[A-Za-z0-9][A-Za-z0-9/._-]*[A-Za-z0-9]", text)
    return [t for t in tokens if any(c.isalpha() for c in t)
            and (sum(c.isupper() for c in t) >= 2 or (any(c.isdigit() for c in t) and len(t) >= 3))]


def _row_variant(row: Mapping[str, Any]) -> Variant:
    return parse_coordinates(f"{_cell(row, 'chrom')}:{_cell(row, 'pos_grch38')}:{_cell(row, 'ref')}>"
                             f"{_cell(row, 'alt')}")


def _sha256(path: Path) -> str:
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def _display(path: Path) -> str:
    path = Path(path).resolve()
    return str(path.relative_to(REPO)) if path.is_relative_to(REPO) else str(path)


@lru_cache(maxsize=4)
def _groups_file(path: str) -> tuple[dict, ...]:
    return tuple(json.loads(Path(path).read_text()).get("groups") or ())


@lru_cache(maxsize=2)
def _resolver_file(path: str) -> SymbolResolver:
    return SymbolResolver.from_hgnc(path)


@lru_cache(maxsize=2)
def _lambert_file(path: str) -> dict[str, str]:
    with open(path, newline="") as f:
        return {row["HGNC symbol"].strip().upper(): row["DBD"].strip() for row in csv.DictReader(f)
                if row.get("Is TF?") == "Yes" and row.get("HGNC symbol") and row.get("DBD")}


@dataclass(frozen=True)
class Reference:
    """The read-only reference data the evaluator uses: QBiC-SELEX model-sharing groups (cache/groups.json, read with
    json, never through the registry, which can rewrite it), HGNC symbols and the Lambert 2018 DBD of each TF."""
    groups: tuple[dict, ...] = ()
    resolver: SymbolResolver | None = None
    lambert: dict[str, str] = field(default_factory=dict)
    files: dict[str, str] = field(default_factory=dict)     # "<name>_sha256" -> sha256 of each file read

    def symbol(self, text: str) -> str:
        """An HGNC-normalised symbol (approved, or an unambiguous previous symbol), else the text in upper case."""
        label = " ".join(str(text).split()).upper()
        hit = self.resolver(label) if self.resolver and label else None
        return hit[0].upper() if hit else label

    def approved(self, token: str) -> bool:
        hit = self.resolver(token) if self.resolver else None
        return bool(hit) and hit[0].upper() == token.upper()

    def dbd(self, tf: str) -> str | None:
        return self.lambert.get(tf.upper())

    def groups_of(self, tfs: Iterable[str]) -> list[dict]:
        wanted = set(tfs)
        return [g for g in self.groups if wanted & set(g.get("tfs") or ())]


def load_reference(config: Config | None = None, *, required: bool = True) -> Reference:
    """The reference data at the configured paths (cache.groups, data.hgnc, data.lambert). With required=False a
    missing file is skipped and the checks that need it are reported as not assessable."""
    cfg = config or load_config()
    readers: dict[str, tuple[tuple[str, str], Callable[[str], Any]]] = {
        "groups": (("cache", "groups"), _groups_file), "hgnc": (("data", "hgnc"), _resolver_file),
        "lambert": (("data", "lambert"), _lambert_file)}
    loaded: dict[str, Any] = {}
    files: dict[str, str] = {}
    for name, ((section, key), reader) in readers.items():
        try:
            path = cfg.path(section, key)
            loaded[name] = reader(str(path))
            files[f"{name}_sha256"] = _sha256(path)
        except (KeyError, ConfigError, OSError):
            if required:
                raise
    return Reference(groups=loaded.get("groups", ()), resolver=loaded.get("hgnc"),
                     lambert=loaded.get("lambert", {}), files=files)


# --- gold isolation --------------------------------------------------------------------------------------------------

def clean_request(row: Mapping[str, Any], arm: Arm) -> Request:
    """The request a run of this gold row may see (see the module docstring). Raises IntakeError for coordinates
    that cannot be read and ValueError for an unknown arm."""
    if arm not in ARMS:
        raise ValueError(f"unknown arm {arm!r} (use {', '.join(ARMS)})")
    variant = _row_variant(row)
    origin = _cell(row, ORIGIN_COLUMN).lower()
    origin = origin if origin in ("somatic", "germline") else "unknown"
    disease = normalise_disease([_cell(row, "disease_or_trait")]) if arm == "supplied_disease" else []
    return Request(variant=f"chr{variant.chrom}:{variant.pos}:{variant.ref}>{variant.alt}", origin=origin,
                   disease=disease, request_id=request_id(variant, origin, disease, []))


def label_strings_by_kind(row: Mapping[str, Any], *, config: Config | None = None) -> dict[str, set[str]]:
    """Every label-derived string of a gold row, by kind (LABEL_KINDS). A clean request must contain none of them.
    Tools legitimately return TF, gene, trait, cytoband and rsID strings, so a test on agent packets should check
    only the kinds no tool produces (source, notes, other, and the case id and variant name under identity). Match
    with find_label_strings (whole tokens, case ignored)."""
    cell = {key: _cell(row, key) for key in (*NEVER_IN_PROMPT, "case_id", "variant", "disease_or_trait",
                                             "expression_context")}
    tfs = _split(cell["causal_tf"])
    groups = _groups_file(str((config or load_config()).path("cache", "groups")))
    disease = cell["disease_or_trait"]
    stripped = strip_bracketed(disease)
    source = cell["source_pmid_or_ref"]
    kinds: dict[str, set[str]] = {
        "identity": {cell["case_id"], cell["variant"], *_identifiers(cell["variant"]),
                     *re.findall(r"rs\d+", " ".join(cell[k] for k in NEVER_IN_PROMPT), re.I)},
        "tf": {cell["causal_tf"], *tfs, cell["tf_family"], *_split(cell["tf_family"], r"/"), cell["qbic_model"],
               *_identifiers(cell["qbic_model"])},
        "group": {s for g in groups if set(tfs) & set(g.get("tfs") or ())
                  for s in (g["id"], g.get("label", ""), g.get("dbd", ""), *g.get("tfs", ()))},
        "gene": {cell["target_gene"], *_split(cell["target_gene"])},
        "context": {s for key in ("tissue_or_cell_type", "expression_context") for s in (
            cell[key], strip_bracketed(cell[key]), *_split(strip_bracketed(cell[key]), r"[;=]"),
            *(p for part in bracketed_parts(cell[key]) for p in (part, *_split(part))),
            *re.findall(r"ACH-\d+", cell[key]))},
        "disease": {disease, stripped, *_split(stripped, r"[,;]"),
                    *(w for w in re.findall(r"[A-Za-z][A-Za-z0-9-]+", stripped) if w.lower() not in STOPWORDS)},
        "bracketed": {p for part in bracketed_parts(disease) for p in (part, f"({part})")},
        "source": {source, f"PMID:{source}"} if source.isdigit() else {source},
        "notes": {cell["notes"]},
        "notes_tokens": set(_identifiers(cell["notes"])),
        "other": {cell["direction"], cell["label_class"], cell["score_level"]},
    }
    return {k: {s for s in v if _is_label(s)} for k, v in kinds.items()}


def label_strings(row: Mapping[str, Any], *, arm: Arm = "main", config: Config | None = None) -> set[str]:
    """Every label-derived string that must not appear in this arm's clean request: all of them, except, in the
    supplied-disease arm, those the bracket-free disease itself contains."""
    strings = set().union(*label_strings_by_kind(row, config=config).values())
    if arm == "supplied_disease":
        supplied = " | ".join(clean_request(row, arm).disease)
        strings = {s for s in strings if not find_label_strings(supplied, [s])}
    return strings


def find_label_strings(text: str, strings: Iterable[str]) -> list[str]:
    """The strings that occur in the text as whole tokens, ignoring case ("REST" is not found in "request")."""
    low = text.casefold()
    return sorted(s for s in set(strings)
                  if re.search(rf"(?<![0-9a-z]){re.escape(s.casefold())}(?![0-9a-z])", low))


# --- the gold specification ------------------------------------------------------------------------------------------

def _not_applicable(reason: str) -> dict[str, Any]:
    return {"applicable": False, "reason": reason, "needs_review": False, "review_reasons": []}


def _component(values: dict[str, Any], reasons: list[str]) -> dict[str, Any]:
    return {"applicable": True, **values, "needs_review": bool(reasons), "review_reasons": reasons}


def _symbols(text: str, ref: Reference) -> tuple[list[str], list[str]]:
    """The HGNC-normalised symbols a cell lists, and those HGNC does not know."""
    parts = [p for p in _split(text) if p.casefold() not in NOT_LABELS]
    return list(dict.fromkeys(ref.symbol(p) for p in parts)), [p for p in parts if not ref.approved(ref.symbol(p))]


def _symbol_spec(key: str, symbols: list[str], unknown: list[str], what: str) -> dict[str, Any]:
    reasons = ([f"not an HGNC symbol: {', '.join(unknown)}"] if unknown else []) + (
        [f"several {what} listed; recovery counts any of them"] if len(symbols) > 1 else [])
    return _component({key: symbols}, reasons)


def _group_spec(tfs: list[str], ref: Reference, uncovered: bool) -> dict[str, Any]:
    groups = ref.groups_of(tfs)
    if not groups:
        return _not_applicable(f"no QBiC-SELEX model or CIS-BP mapping covers {', '.join(tfs)} (cache/groups.json): "
                               "a capability case")
    reasons = (["the TF sits in several model-sharing groups; recovery counts any of them"] if len(groups) > 1
               else []) + ([f"the CSV says not in coverage, but cache/groups.json lists {', '.join(tfs)} in "
                            f"{', '.join(g['id'] for g in groups)}"] if uncovered else [])
    return _component({"groups": [{"id": g["id"], "label": g.get("label", ""), "dbd": g.get("dbd", ""),
                                   "tfs": sorted(g.get("tfs") or ())} for g in groups]}, reasons)


def _alnum(text: str) -> str:
    return re.sub(r"[^0-9a-z]", "", text.casefold())


def _family_spec(tfs: list[str], csv_family: str, ref: Reference, uncovered: bool) -> dict[str, Any]:
    if uncovered:
        return _not_applicable(f"{', '.join(tfs)} is not in QBiC-SELEX coverage: the case tests that the run says so "
                               "rather than naming another TF of its family, so family credit does not apply")
    dbds = sorted({d for t in tfs if (d := ref.dbd(t))})
    if not dbds:
        return _not_applicable(f"{', '.join(tfs)} is not in the Lambert 2018 TF list")
    reasons = ([f"the CSV family {csv_family!r} is not the Lambert DBD {' / '.join(dbds)!r}; family credit uses "
                "the Lambert DBD"] if _alnum(csv_family) not in {_alnum(d) for d in dbds} else []) + (
        ["the TFs fall in several Lambert families"] if len(dbds) > 1 else [])
    return _component({"dbd": dbds, "csv_family": csv_family}, reasons)


def _clause(text: str, ref_allele: str, alt_allele: str) -> dict[str, Any] | None:
    """One clause of a direction text read as an allele and a binding change, or None when it does not name both
    (or names them ambiguously)."""
    up, down = bool(POSITIVE.search(text)), bool(NEGATIVE.search(text))
    sides = {"ref" if b == ref_allele else "alt" if b == alt_allele else "other" for b in ALLELE_LETTER.findall(text)}
    sides |= {"alt" if w.lower().startswith("alt") else "ref" for w in ALLELE_WORD.findall(text)}
    if up == down or len(sides) != 1 or sides == {"other"}:
        return None
    side = sides.pop()
    alt_up = up if side == "alt" else down
    return {"text": text, "allele": alt_allele if side == "alt" else ref_allele, "side": side,
            "alt_direction": "increases" if alt_up else "decreases"}


def _direction_spec(text: str, variant: Variant) -> dict[str, Any]:
    clauses = _split(text, r"[;,]")
    read = [c for c in (_clause(t, variant.ref, variant.alt) for t in clauses) if c]
    unread = [t for t in clauses if not _clause(t, variant.ref, variant.alt)]
    directions = {c["alt_direction"] for c in read}
    reasons = []
    if not read:
        reasons.append(f"{text!r} names no allele with a binding change: state which allele binds more")
    elif unread:
        reasons.append(f"not read as a binding change: {'; '.join(unread)}")
    if len(directions) > 1:
        reasons.append("its clauses disagree on the alt allele's binding")
    direction = directions.pop() if len(directions) == 1 else None
    binds_more = None if direction is None else "alt" if direction == "increases" else "ref"
    return _component({"text": text, "alt_direction": direction, "binds_more": binds_more, "clauses": read}, reasons)


def _context_spec(text: str, variant: Variant, table: BiosampleTable) -> dict[str, Any]:
    heads = _split(strip_bracketed(text), r";")
    names = [n for part in bracketed_parts(text) for n in _split(part)]
    scopes, unknown = [], []
    for label in heads + names:
        known = table.record(label) is not None or table.tissue_named(label) is not None
        scope = scope_from_label(label, source="unspecified", variant=variant, table=table)
        scopes.append({"label": label, "recognised": known, "scope": scope.model_dump(mode="json")})
        if not known:
            unknown.append(label)
    reasons = ([f"not in the biosample table: {', '.join(unknown)}"] if unknown else []) + (
        ["several contexts listed; recovery counts any of them"] if len(heads) > 1 else [])
    return _component({"text": text, "scopes": scopes}, reasons)


def _phenotype_spec(text: str) -> dict[str, Any]:
    labels = _split(strip_bracketed(text), r"[,;]")
    reasons = ["several traits listed; recovery counts any of them"] if len(labels) > 1 else []
    return _component({"text": strip_bracketed(text), "labels": labels, "bracketed": bracketed_parts(text)},
                      reasons)


def _components(row: Mapping[str, Any], variant: Variant, ref: Reference,
                table: BiosampleTable) -> dict[str, dict[str, Any]]:
    cell = {key: _cell(row, key) for key in ("causal_tf", "tf_family", "direction", "target_gene",
                                             "tissue_or_cell_type", "disease_or_trait", "score_level")}
    tfs, unknown_tfs = _symbols(cell["causal_tf"], ref)
    genes, unknown_genes = _symbols(cell["target_gene"], ref)
    uncovered = cell["score_level"].lower() == NOT_IN_COVERAGE
    no_tf = _not_applicable("the CSV names no TF")
    return {
        "tf_member": _symbol_spec("tfs", tfs, unknown_tfs, "TFs") if tfs else no_tf,
        "tf_group": _group_spec(tfs, ref, uncovered) if tfs else no_tf,
        "tf_family": _family_spec(tfs, cell["tf_family"], ref, uncovered) if tfs else no_tf,
        "direction": _direction_spec(cell["direction"], variant) if _is_label(cell["direction"])
        else _not_applicable("the CSV gives no direction"),
        "target_gene": _symbol_spec("genes", genes, unknown_genes, "genes") if genes
        else _not_applicable("the CSV names no target gene"),
        "context": _context_spec(cell["tissue_or_cell_type"], variant, table)
        if _is_label(cell["tissue_or_cell_type"]) else _not_applicable("the CSV gives no context"),
        "phenotype": _phenotype_spec(cell["disease_or_trait"]) if _is_label(cell["disease_or_trait"])
        else _not_applicable("the CSV gives no disease or trait"),
    }


def _other_symbols(row: Mapping[str, Any], components: dict[str, dict[str, Any]], ref: Reference) -> list[str]:
    """Approved HGNC symbols the notes or the coverage text name besides the gold TFs, genes and group members."""
    known = {*components["tf_member"].get("tfs", ()), *components["target_gene"].get("genes", ()),
             *(t for g in components["tf_group"].get("groups", ()) for t in g["tfs"])}
    text = f"{_cell(row, 'notes')} {_cell(row, 'qbic_model')}"
    tokens = re.findall(r"[A-Za-z0-9]+(?:/[A-Za-z0-9]+)*", text)       # C/EBP stays whole; MYC-expression splits
    return sorted({t.upper() for t in tokens
                   if len(t) >= 3 and sum(c.isupper() for c in t) >= 2 and ref.approved(t)} - known)


def _flag(component: dict[str, Any], reason: str) -> bool:
    """Add a review reason to an applicable component; False when the component does not apply."""
    if not component["applicable"]:
        return False
    component["review_reasons"].append(reason)
    component["needs_review"] = True
    return True


def _flag_named(components: dict[str, dict[str, Any]], named: list[str], ref: Reference) -> list[str]:
    """Attach the symbols the notes name to the components they could be alternatives for, so the components a
    reviewer must settle are provisional, not just the entry: a TF (Lambert list) may be an alternative causal TF,
    and any symbol an alternative target gene. Returns the entry-level reasons left for symbols no applicable
    component can take."""
    def reason(symbols: list[str], one: str, many: str) -> str:
        alternative = f"a possible alternative {one}" if len(symbols) == 1 else f"possible alternative {many}"
        return (f"the notes name {', '.join(symbols)}: {alternative} the CSV does not state as accepted; "
                "alternatives stay empty until reviewed")

    unplaced = list(named)
    if (tfs := [s for s in named if ref.dbd(s)]) and _flag(components["tf_member"], reason(tfs, "TF", "TFs")):
        unplaced = [s for s in unplaced if s not in tfs]
    if _flag(components["target_gene"], reason(named, "target gene", "target genes")):
        unplaced = []
    return [reason(unplaced, "TF or target gene", "TFs or target genes")] if unplaced else []


def _spec_case(row: Mapping[str, Any], ref: Reference, table: BiosampleTable) -> dict[str, Any]:
    variant = _row_variant(row)
    control = is_control(row)
    requests = {arm: clean_request(row, arm).model_dump(mode="json") for arm in ARMS}
    components = ({name: _not_applicable("control: no TF mechanism is expected") for name in COMPONENTS} if control
                  else _components(row, variant, ref, table))
    named = [] if control else _other_symbols(row, components, ref)
    entry_reasons = _flag_named(components, named, ref) if named else []
    reasons = [f"{name}: {r}" for name, c in components.items() for r in c["review_reasons"]] + entry_reasons
    return {"case_id": _cell(row, "case_id"), "label_class": _cell(row, "label_class"), "control": control,
            "variant": {"key": variant.key, "chrom": variant.chrom, "pos": variant.pos, "ref": variant.ref,
                        "alt": variant.alt},
            "origin": requests["main"]["origin"], "qbic_coverage": _cell(row, "score_level") or None,
            "expected": ("null: no TF mechanism expected (an evidence-sparse comparison, not an established biological "
                         "null)") if control else "the published TF mechanism, by component",
            "requests": requests, "components": components, "alternatives": [],
            "source": _cell(row, "source_pmid_or_ref"), "notes": _cell(row, "notes"),
            "needs_review": bool(reasons), "review_reasons": reasons,
            "row": {str(k): "" if v is None else str(v) for k, v in row.items() if k is not None}}


def build_gold_spec(csv_path: str | Path, *, config: Config | None = None) -> dict[str, Any]:
    """The evaluator-only gold claim specification, built mechanically from the CSV (never edited). The same CSV and
    reference files always give the same spec: nothing in it depends on time or order of reading."""
    cfg = config or load_config()
    path = Path(csv_path)
    with open(path, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    ids = [_cell(r, "case_id") for r in rows]
    if duplicated := sorted({i for i in ids if ids.count(i) > 1}):
        raise ValueError(f"{path} lists case ids more than once: {', '.join(duplicated)}")
    ref = load_reference(cfg)
    table = load_table()
    return {"spec_version": SPEC_VERSION, "status": UNREVIEWED,
            "about": ("Evaluator-only gold claim specification, built mechanically from the gold CSV by "
                      "variant2mechanism.v9.evaluation.build_gold_spec. Review every needs_review item, then set "
                      f"status to {REVIEWED!r}; until then every score against this spec is provisional. The CSV is "
                      "never edited; the engine never reads this file."),
            "source": _source_hashes(path, ref),
            "rules": RULES, "cases": [_spec_case(r, ref, table) for r in rows]}


def _source_hashes(csv_path: Path, ref: Reference) -> dict[str, str]:
    """The CSV's path and the sha256 of every file a spec is built from: change any of them and the spec is stale."""
    return {"csv": _display(csv_path), "csv_sha256": _sha256(csv_path), **ref.files,
            "biosamples_sha256": _sha256(BIOSAMPLES_FILE)}


def render_gold_spec(spec: dict[str, Any]) -> str:
    return json.dumps(spec, indent=1, ensure_ascii=False) + "\n"


def write_gold_spec(out_path: str | Path, *, csv_path: str | Path | None = None, config: Config | None = None,
                    overwrite: bool = False) -> Path:
    """Build the spec from the configured gold CSV (eval.gold_set) or csv_path and write it. An existing file may
    hold the user's review, so it is replaced only with overwrite=True."""
    cfg = config or load_config()
    text = render_gold_spec(build_gold_spec(Path(csv_path) if csv_path else cfg.path("eval", "gold_set"), config=cfg))
    out = Path(out_path)
    out.parent.mkdir(parents=True, exist_ok=True)
    try:
        with open(out, "w" if overwrite else "x", encoding="utf-8") as f:
            f.write(text)
    except FileExistsError:
        raise FileExistsError(f"{out} exists and may hold the user's review; rebuild it only on purpose "
                              "(overwrite=True)") from None
    return out


def load_gold_spec(path: str | Path | None = None, *, config: Config | None = None) -> dict[str, Any]:
    """A gold spec, refused when any file it was built from has changed since: the CSV, or a reference file (the
    model-sharing groups, HGNC, the Lambert table, the biosample table) whose change could alter its components."""
    spec = json.loads(Path(path or GOLD_SPEC_FILE).read_text())
    recorded = spec["source"]
    csv_path = Path(recorded["csv"])
    csv_path = csv_path if csv_path.is_absolute() else REPO / csv_path
    current = _source_hashes(csv_path, load_reference(config))
    changed = [name.removesuffix("_sha256") for name, digest in recorded.items()
               if name.endswith("_sha256") and current.get(name) != digest]
    if changed:
        raise ValueError(f"{', '.join(changed)} changed after the gold spec was built ({csv_path}): rebuild the spec "
                         "and review it again")
    return spec


def spec_entry(spec: dict[str, Any], case_id: str) -> dict[str, Any]:
    """One case of a gold spec, carrying the spec's review status (`spec_status`) so that its audit knows whether
    the scores are final. An entry without it is audited as unreviewed."""
    for entry in spec["cases"]:
        if entry["case_id"] == case_id:
            return {**entry, "spec_status": spec.get("status", UNREVIEWED)}
    raise KeyError(f"{case_id} is not in the gold spec (cases: {', '.join(e['case_id'] for e in spec['cases'])})")


# --- reading a run ---------------------------------------------------------------------------------------------------

def _num(identifier: str) -> int:
    return int(identifier[1:]) if identifier[1:].isdigit() else 0


def _at(data: Any, *keys: str) -> Any:
    """data[k1][k2]..., or None where a level is missing or not a mapping."""
    for key in keys:
        data = data.get(key) if isinstance(data, Mapping) else None
    return data


@dataclass
class _Names:
    """What a set of claims (and a hypothesis's own fields) names, normalised."""
    tfs: set[str] = field(default_factory=set)            # TF entities, and members of complexes and binding events
    group_members: set[str] = field(default_factory=set)  # members of tf_groups: group level, not member identity
    group_ids: set[str] = field(default_factory=set)      # canonical ids of tf_groups (registry ids such as G035)
    alternatives: set[str] = field(default_factory=set)   # a hypothesis's member alternatives (retention only)
    genes: set[str] = field(default_factory=set)
    phenotypes: set[str] = field(default_factory=set)
    contexts: list[ContextScope] = field(default_factory=list)

    def merge(self, other: "_Names") -> None:
        for name in ("tfs", "group_members", "group_ids", "alternatives", "genes", "phenotypes"):
            getattr(self, name).update(getattr(other, name))
        self.contexts += other.contexts

    def all_tfs(self) -> set[str]:
        return self.tfs | self.group_members

    def candidates(self) -> set[str]:
        """Every TF, group and gene named: what an elimination can set aside."""
        return self.all_tfs() | self.alternatives | self.group_ids | self.genes


class _Run:
    """A run's graph as the audit reads it: what each claim and hypothesis names, normalised once."""

    def __init__(self, graph: ClaimGraph, ref: Reference):
        self.graph, self.ref = graph, ref
        self._claims: dict[str, _Names] = {}

    def claim_names(self, claim_id: str) -> _Names:
        if claim_id not in self._claims:
            names, claim = _Names(), self.graph.claims[claim_id]
            if claim.context_scope is not None:
                names.contexts.append(claim.context_scope)
            for eid in claim.subject_ids + claim.object_ids:
                entity = self.graph.entities[eid]
                members = {self.ref.symbol(self.graph.entities[p].label) for p in entity.participants}
                if entity.kind == "tf":
                    names.tfs.add(self.ref.symbol(entity.label))
                elif entity.kind == "tf_group":
                    names.group_members |= members
                    names.group_ids |= {entity.canonical_id.upper()} if entity.canonical_id else set()
                elif entity.kind in ("complex", "binding_event"):
                    names.tfs |= members
                elif entity.kind in ("gene", "transcript"):
                    names.genes.add(self.ref.symbol(entity.label))
                elif entity.kind == "phenotype":
                    names.phenotypes.add(entity.label)
            self._claims[claim_id] = names
        return self._claims[claim_id]

    def names(self, claim_ids: Iterable[str], hypothesis: Hypothesis | None = None,
              alternatives: Iterable[str] = ()) -> _Names:
        names = _Names()
        for cid in claim_ids:
            if cid in self.graph.claims:
                names.merge(self.claim_names(cid))
        if hypothesis is not None:
            endpoint = hypothesis.endpoint.strip()
            names.contexts += [hypothesis.context] if hypothesis.context is not None else []
            names.phenotypes |= {endpoint} if endpoint and endpoint.lower() != "molecular" else set()
        names.alternatives |= {self.ref.symbol(a) for a in alternatives if a.strip()}
        return names

    def claims_with(self, claim_ids: Iterable[str], matches: Callable[[_Names], bool]) -> list[dict[str, str]]:
        return [{"claim_id": cid, "relation": self.graph.claims[cid].relation,
                 "display": self.graph.display_status(cid)} for cid in claim_ids if matches(self.claim_names(cid))]

    def excluded(self, claim_id: str) -> str | None:
        """Why a claim of the answer earns no credit, or None when it stands: the run's own verdict against it, its
        retirement by a replacement, or a variant that is not this case's (an LD partner or a famous neighbour), by
        the graph's own claim_frame (a reference naming the case by an rsID code recorded as its alias, or by its
        chrom:pos, resolves to the case variant's entity, so such a claim is about the case)."""
        claim = self.graph.claims[claim_id]
        if claim.assessment == "contradicted_in_scope":
            return "contradicted in scope"
        if claim.superseded_by:
            return f"superseded by {claim.superseded_by}"
        if self.graph.claim_frame(claim_id) == "other":
            return "about another variant"
        return None

    def evidence_variant(self, ev: Evidence) -> Literal["case", "other"] | None:
        """Which variant an evidence item names in about_variants, by the graph's variant_mention rule: "case" when
        an entry names the case variant (one of its rsIDs, recorded aliases included, or its chrom:pos), "other" when
        the entries name only other variants, None when they name none (an element-, gene- or line-level item)."""
        named = {self.graph.variant_mention(x) for x in ev.about_variants} - {None}
        return "case" if "case" in named else "other" if named else None


def _leaders(graph: ClaimGraph) -> list[str]:
    """The run's answer: the hypotheses its result names (leading_ids). A result decided without a final comparison,
    or whose critic's choice failed code's checks, names none, and the audit names none in its place (code never
    names a leader the critic did not); a graph with no result has no answer."""
    return list(graph.result.leading_ids) if graph.result is not None else []


def _outcome(graph: ClaimGraph) -> dict[str, Any]:
    """How the run ended, read for scoring (RULES["outcome"]): its kind (explanation, abstention or limitation),
    which limitation, whether the run assessed the case (only then are components scored and is a control's empty
    answer a null), whether its result names a hypothesis, and a note saying why when that matters. A run stopped by
    engine_error or cache_miss is a limitation whatever outcome it recorded (an engine before the review fix recorded
    a crash as no_supported_explanation): it assessed nothing. So did a request refused as input. A limitation the
    run concluded itself (the critic's judgement that the case cannot be assessed, or no hypothesis at all) is its
    answer and is scored."""
    result = graph.result
    if result is None:
        return {"kind": None, "limitation": "no_result", "assessed": False, "names_answer": False,
                "note": "no result recorded (an evidence bundle, or a run that did not finish): nothing to score"}
    stop, category, names = result.stop_reason, result.outcome, bool(result.leading_ids)
    limitation, note = None, ""
    if stop in RUN_FAILURES:
        kind, limitation = "limitation", "run_failure"
        recorded = "" if category == LIMITATION else f"; it recorded {category}"
        note = (f"the run stopped with {stop} and assessed nothing{recorded}: a case-level failure to report and "
                "rerun, scored as neither a miss nor an abstention nor a control's null")
    elif category == LIMITATION:
        kind, limitation = "limitation", "input" if stop in INPUT_STOPS else "capability"
        note = (f"the request could not be assessed as given ({stop}): check the request; scored as neither a miss "
                "nor an abstention nor a control's null" if limitation == "input" else
                f"the run ended as a capability limitation ({stop}): the case could not be assessed with the models and "
                "data it had; that is its answer, and it is scored")
    elif category == ABSTENTION:
        kind = "abstention"
    else:
        kind = "explanation"
        if not names:
            note = (f"the result ({category}) names no hypothesis: decided without a final comparison, or the "
                    "critic's choice failed code's checks; nothing in the answer earns credit (candidate retention "
                    "shows what stayed available)")
    return {"kind": kind, "limitation": limitation, "assessed": limitation not in ("run_failure", "input"),
            "names_answer": names, "note": note}


def _answer_claims(run: _Run, leaders: list[str]) -> tuple[list[str], list[dict[str, str]]]:
    """The answer's claims that stand, in order, and the others with the reason each earns nothing."""
    claim_ids = list(dict.fromkeys(c for hid in leaders for c in run.graph.hypotheses[hid].claim_ids))
    excluded = [{"claim_id": c, "reason": why} for c in claim_ids if (why := run.excluded(c))]
    out = {x["claim_id"] for x in excluded}
    return [c for c in claim_ids if c not in out], excluded


Version = tuple[list[str], list[str]]           # a hypothesis version's claim ids and member alternatives


def _revision_entries(h: Hypothesis) -> list[dict[str, Any]]:
    """The revision entries of a hypothesis's history that keep the version they replaced: the entries
    graph.hypothesis_versions reads, one per version before the current one."""
    return [e for e in h.history if e.get("kind") == "revision" and isinstance(e.get("previous"), Mapping)]


def _created(h: Hypothesis) -> tuple[list[str], list[str], str]:
    """A hypothesis as proposed: its claim ids, member alternatives (graph.hypothesis_versions' first version) and
    its disposition at creation."""
    claim_ids, alternatives = hypothesis_versions(h)[0]
    disposition = next((e.get("disposition") for e in h.history if e.get("kind") == "created"), h.disposition)
    return claim_ids, alternatives, str(disposition)


def _step(graph: ClaimGraph, before: list[str], after: list[str]) -> str:
    """"supersession" when a claim the revision removed was superseded by one it added, else "revision"."""
    kept = set(after)
    removed = [c for c in before if c not in kept and c in graph.claims]
    return "supersession" if any(graph.claims[c].superseded_by in kept for c in removed) else "revision"


@dataclass
class _Revision:
    """One revision of a hypothesis: the versions before and after, and what each named."""
    hypothesis: Hypothesis
    version: int                # the hypothesis version the revision made
    reason: str
    step: str                   # "revision", or "supersession" when it swapped in a claim's replacement
    before: Version
    after: Version
    named_before: _Names
    named_after: _Names

    def record(self) -> dict[str, Any]:
        return {"hypothesis_id": self.hypothesis.hypothesis_id, "version": self.version, "step": self.step,
                "reason": self.reason}


def _revisions(run: _Run) -> list[_Revision]:
    """Every revision of every hypothesis, oldest first within each. A supersession that named a hypothesis is one
    of them: the graph swaps the claim through a revision that carries the supersession's reason."""
    out = []
    for h in run.graph.hypotheses.values():
        versions = hypothesis_versions(h)
        for before, after, entry in zip(versions[:-1], versions[1:], _revision_entries(h), strict=True):
            out.append(_Revision(h, int(entry.get("version") or 0), str(entry.get("reason", "")),
                                 _step(run.graph, before[0], after[0]), before, after,
                                 run.names(before[0], None, before[1]), run.names(after[0], None, after[1])))
    return out


def _inventory_rows(graph: ClaimGraph) -> list[dict[str, Any]]:
    """The observations of the latest successful qbic_inventory call (one row per model-sharing group, C2)."""
    calls = [t for t in graph.tool_calls.values()
             if t.tool_name == "qbic_inventory" and t.execution_status == "success"]
    return list(max(calls, key=lambda t: _num(t.tool_call_id)).observations) if calls else []


def _row_tfs(rows: Iterable[dict[str, Any]], ref: Reference) -> set[str]:
    return {ref.symbol(m["tf"]) for r in rows for m in r.get("members") or [] if isinstance(m, dict) and m.get("tf")}


def _json_file(path: Path) -> dict[str, Any] | None:
    return json.loads(path.read_text()) if path.is_file() else None


# --- the audit -------------------------------------------------------------------------------------------------------

def _tf_matches(names: _Names, components: dict[str, Any], ref: Reference) -> dict[str, list[str]]:
    """Which named TFs or groups match the gold TF: as the member (strict), its group or its family (lenient)."""
    member, group, family = (components[k] for k in TF_COMPONENTS)
    out: dict[str, list[str]] = {k: [] for k in TF_COMPONENTS}
    if member["applicable"]:
        out["tf_member"] = sorted(names.tfs & set(member["tfs"]))
    if group["applicable"]:
        ids = {g["id"].upper() for g in group["groups"]}
        members = {t for g in group["groups"] for t in g["tfs"]}
        out["tf_group"] = sorted((names.group_ids & ids) | (names.all_tfs() & members))
    if family["applicable"]:
        out["tf_family"] = sorted(t for t in names.all_tfs() if ref.dbd(t) in set(family["dbd"]))
    return out


def _words(text: str) -> set[str]:
    return {w for w in re.findall(r"[0-9a-z]+", text.casefold()) if w not in STOPWORDS}


def _direction_recovery(run: _Run, claim_ids: list[str], components: dict[str, Any], variant: Variant,
                        uncovered: bool) -> tuple[bool, dict[str, Any]]:
    """The answer's alters_binding claims about a matching TF, each read as the alt allele's binding change. When
    the gold TF is not in coverage only the member itself matches: a relative's predicted binding change is the
    substitution that case tests for."""
    gold = components["direction"]["alt_direction"]
    levels = ("tf_member",) if uncovered else TF_COMPONENTS
    rows = []
    for cid in claim_ids:
        claim = run.graph.claims[cid]
        matches = _tf_matches(run.claim_names(cid), components, run.ref)
        if claim.relation != "alters_binding" or not any(matches[k] for k in levels):
            continue
        sign = SPECIFIC_DIRECTIONS.get(claim.direction)
        side = {variant.alt: 1, variant.ref: -1}.get(claim.effect_allele or "")
        alt = None if sign is None or side is None else "increases" if sign * side > 0 else "decreases"
        rows.append({"claim_id": cid, "direction": claim.direction, "effect_allele": claim.effect_allele,
                     "alt_direction": alt})
    stated = {r["alt_direction"] for r in rows if r["alt_direction"]}
    note = "" if rows else "the answer states no binding change for a TF matching the gold TF"
    return stated == {gold}, {"gold": gold, "claims": rows, "note": note}


def _context_recovery(answer: _Names, spec: dict[str, Any]) -> tuple[bool, dict[str, Any]]:
    gold = [ContextScope.model_validate(s["scope"]) for s in spec["scopes"]]
    pairs = [(compare_context(g, a), g.label, a.label) for g in gold for a in answer.contexts]
    best = max(pairs, key=lambda p: APPLICABILITY_RANK[p[0]]) if pairs else None
    level = best[0] if best else None
    return level in ("exact", "proxy"), {"level": level, "gold_label": best[1] if best else None,
                                         "answer_label": best[2] if best else None,
                                         "answer_contexts": sorted({a.label for a in answer.contexts})}


def _phenotype_recovery(answer: _Names, spec: dict[str, Any]) -> tuple[bool, dict[str, Any]]:
    matched = sorted(g for g in spec["labels"] if any(_words(g) and _words(g) <= _words(p) for p in answer.phenotypes))
    return bool(matched), {"matched": matched, "answer_traits": sorted(answer.phenotypes)}


def _component_recovery(run: _Run, entry: dict[str, Any], leaders: list[str], claim_ids: list[str],
                        outcome: dict[str, Any]) -> dict[str, dict[str, Any]]:
    """Each component scored on the answer's standing claims (claim_ids) and its hypotheses' own context and
    endpoint. A run that assessed nothing (outcome: a run failure, an input limitation, no result) leaves every
    denominator: it is a case-level failure, not a miss."""
    graph, ref, components = run.graph, run.ref, entry["components"]
    standing = set(claim_ids)
    answer = _Names()
    for hid in leaders:
        h = graph.hypotheses[hid]
        answer.merge(run.names([c for c in h.claim_ids if c in standing], h))
    supplied = {"phenotype": bool(graph.case.supplied_disease), "context": bool(graph.case.supplied_context)}
    uncovered = str(entry.get("qbic_coverage") or "").lower() == NOT_IN_COVERAGE
    out: dict[str, dict[str, Any]] = {}
    for name in COMPONENTS:
        spec = components[name]
        base = {"applicable": spec["applicable"], "needs_review": bool(spec.get("needs_review"))}
        unassessable = (spec.get("reason", "not applicable") if not spec["applicable"]
                        else f"not scored: {outcome['note']}" if not outcome["assessed"]
                        else "given to the run as input: not scored" if supplied.get(name)
                        else "the Lambert table is not available" if name == "tf_family" and not ref.lambert
                        else "the gold direction names no allele: review it" if name == "direction"
                        and spec.get("alt_direction") is None else None)
        if unassessable:
            out[name] = {**base, "assessable": False, "recovered": None, "numerator": 0, "denominator": 0,
                         "note": unassessable}
            continue
        if name in TF_COMPONENTS:
            matched = _tf_matches(answer, components, ref)[name]
            recovered, detail = bool(matched), {
                "matched": matched,
                "claims": run.claims_with(claim_ids, lambda n, k=name: bool(_tf_matches(n, components, ref)[k]))}
        elif name == "target_gene":
            genes = set(spec["genes"])
            matched = sorted(answer.genes & genes)
            recovered, detail = bool(matched), {
                "matched": matched, "claims": run.claims_with(claim_ids, lambda n, g=genes: bool(n.genes & g))}
        elif name == "direction":
            recovered, detail = _direction_recovery(run, claim_ids, components, graph.case.variant, uncovered)
        elif name == "context":
            recovered, detail = _context_recovery(answer, spec)
        else:
            recovered, detail = _phenotype_recovery(answer, spec)
        out[name] = {**base, "assessable": True, "recovered": recovered, "numerator": int(recovered),
                     "denominator": 1, **detail}
    return out


def _status(dispositions: set[str]) -> str | None:
    if dispositions & {"leading", "tied"}:
        return "leading"
    for disposition in ("active", "deferred"):
        if disposition in dispositions:
            return disposition
    return "eliminated" if dispositions else None


@dataclass
class _Candidate:
    kind: str
    name: str
    names_it: Callable[[_Names], bool]
    listed: bool              # in the facts code collected (the inventory, or tool evidence for a gene)
    shown: bool               # among what the proposal packet lists (gate-passing inventory groups; gene facts)


def _candidates(run: _Run, components: dict[str, Any]) -> list[_Candidate]:
    graph, ref = run.graph, run.ref
    rows = _inventory_rows(graph)
    shown_rows = [r for r in rows if r.get("passes_gate") is True]
    row_ids, shown_ids = ({str(r.get("group_id", "")).upper() for r in rs} for rs in (rows, shown_rows))
    fact_tfs = {ref.symbol(t) for e in graph.evidence.values() if e.origin == "tool" for t in e.about_tfs}
    fact_genes = {ref.symbol(g) for e in graph.evidence.values() if e.origin == "tool" for g in e.about_genes}
    listed_tfs, shown_tfs = _row_tfs(rows, ref) | fact_tfs, _row_tfs(shown_rows, ref)
    out: list[_Candidate] = []
    member, group, family, gene = (components[k] for k in ("tf_member", "tf_group", "tf_family", "target_gene"))
    for tf in member.get("tfs", []) if member["applicable"] else []:
        out.append(_Candidate("member", tf, lambda n, tf=tf: tf in n.all_tfs() | n.alternatives, tf in listed_tfs,
                              tf in shown_tfs))
    for g in group.get("groups", []) if group["applicable"] else []:
        gid, members = g["id"].upper(), set(g["tfs"])
        out.append(_Candidate("group", g["id"], lambda n, gid=gid, members=members: gid in n.group_ids
                              or bool((n.all_tfs() | n.alternatives) & members), gid in row_ids, gid in shown_ids))
    if family["applicable"] and ref.lambert:
        for dbd in family["dbd"]:
            def in_family(tfs: Iterable[str], dbd: str = dbd) -> bool:
                return any(ref.dbd(t) == dbd for t in tfs)
            out.append(_Candidate("family", dbd, lambda n, f=in_family: f(n.all_tfs() | n.alternatives),
                                  in_family(listed_tfs), in_family(shown_tfs)))
    for symbol in gene.get("genes", []) if gene["applicable"] else []:
        out.append(_Candidate("gene", symbol, lambda n, s=symbol: s in n.genes, symbol in fact_genes,
                              symbol in fact_genes))
    return out


def _reinstatements(h: Hypothesis) -> list[dict[str, Any]]:
    """The hypothesis's reinstatements (graph.reinstate), oldest first: code rejections withdrawn because the
    contradiction they rested on no longer stood (each names the rejecting event, rejected_by, and its claims)."""
    return [e for e in h.history if e.get("kind") == "reinstatement"]


def _restored(h: Hypothesis) -> bool:
    """Whether the hypothesis stands where a reinstatement put it (deferred, awaiting new evidence on the claims whose
    contradiction was withdrawn): restored, not set aside. A later disposition (an activation, a new deferral, a
    second rejection, which is final) ends that."""
    steps = [e for e in h.history if e.get("kind") in ("disposition", "reinstatement")]
    return h.disposition == "deferred" and bool(steps) and steps[-1].get("kind") == "reinstatement"


def _set_aside_reasons(h: Hypothesis) -> list[str]:
    """The reasons that deferred or rejected the hypothesis (its current one and every earlier one), without the
    rejections a reinstatement withdrew: their contradiction no longer stood, so they eliminated nothing."""
    withdrawn = {e.get("rejected_by") for e in _reinstatements(h)}
    past = [str(e.get("reason", "")) for e in h.history if e.get("kind") == "disposition"
            and e.get("to") in ("deferred", "rejected") and e.get("event_id") not in withdrawn]
    return list(dict.fromkeys(r for r in [h.disposition_reason, *past] if r))


def _acceptable(candidates: list[_Candidate], names: _Names) -> list[str]:
    return sorted(f"{c.kind}:{c.name}" for c in candidates if c.names_it(names))


def _candidate_retention(run: _Run, candidates: list[_Candidate], metrics: dict[str, Any] | None,
                         revisions: list[_Revision]) -> dict[str, Any]:
    """Each acceptable candidate's status and the stages it survived. A candidate no current hypothesis names but an
    earlier version did was eliminated by a revision or supersession (dropped_by, with the reason); only one that no
    version ever named is inventory_only (when the inventory showed it), not_shown, facts_only or absent. A hypothesis
    code reinstated (its rejection's contradiction was withdrawn) is deferred, so its candidates are retained, not
    eliminated; `reinstated` names the naming hypotheses that were."""
    hypotheses = list(run.graph.hypotheses.values())
    final = {h.hypothesis_id: run.names(h.claim_ids, h, h.member_alternatives) for h in hypotheses}
    created = {h.hypothesis_id: (run.names(claims, h, alternatives), disposition)
               for h in hypotheses if h.origin == "initial"
               for claims, alternatives, disposition in [_created(h)]}
    kinds: dict[str, dict[str, Any]] = {k: {"applicable": False, "candidates": [],
                                            "available_after": dict.fromkeys(STAGES, False)}
                                        for k in ("member", "group", "family", "gene")}
    for c in candidates:
        naming = {h.hypothesis_id: h.disposition for h in hypotheses if c.names_it(final[h.hypothesis_id])}
        dropped = [r.record() for r in revisions if c.names_it(r.named_before) and not c.names_it(r.named_after)]
        status = _status(set(naming.values())) or ("eliminated" if dropped else (
            ("facts_only" if c.listed else "absent") if c.kind == "gene"
            else "inventory_only" if c.shown else "not_shown" if c.listed else "absent"))
        stages = {"inventory": c.listed,
                  "proposal": any(c.names_it(n) for n, _ in created.values()),
                  "activation": any(c.names_it(n) and d == "active" for n, d in created.values()),
                  "final": status in RETAINED}
        kind = kinds[c.kind]
        kind["applicable"] = True
        kind["candidates"].append({"name": c.name, "listed": c.listed, "shown": c.shown, "status": status,
                                   "hypotheses": naming, "dropped_by": dropped, "stages": stages,
                                   "reinstated": [hid for hid in naming
                                                  if _reinstatements(run.graph.hypotheses[hid])]})
        kind["available_after"] = {s: kind["available_after"][s] or stages[s] for s in STAGES}
    return {"kinds": kinds, "inventory": _inventory_summary(run, metrics)}


def _inventory_summary(run: _Run, metrics: dict[str, Any] | None) -> dict[str, Any]:
    """The gate-passing inventory groups that no version of any hypothesis sketched, by graph.sketched_groups (the
    one rule the engine's metrics and metrics.json use; bundle re-exports it), checked against each list of them the
    run's metrics recorded: the bundle's ("inventory", computed from graph.json when the bundle was written) and the
    engine's own ("engine.inventory", counted during the run). agrees_with_metrics is empty when the metrics recorded
    neither."""
    rows = _inventory_rows(run.graph)
    passing = [str(r.get("group_id")) for r in rows if r.get("passes_gate") is True]
    sketched = sketched_groups(run.graph, rows)
    inventory_only = [g for g in passing if g not in sketched]
    recorded = {"inventory": _at(metrics, "inventory", "inventory_only"),
                "engine.inventory": _at(metrics, "engine", "inventory", "inventory_only")}
    agrees = {source: sorted(map(str, ids)) == sorted(inventory_only) for source, ids in recorded.items()
              if isinstance(ids, list)}
    return {"groups": len(rows), "gate_passing": len(passing), "sketched": len(passing) - len(inventory_only),
            "inventory_only": len(inventory_only), "inventory_only_groups": inventory_only,
            "agrees_with_metrics": agrees}


def _flags(text: str) -> dict[str, list[str]]:
    found = {"missing_coverage": [m.group(0) for m in MISSING_COVERAGE.finditer(text)],
             "more_is_better": [m.group(0) for m in MORE_IS_BETTER.finditer(text)]}
    return {k: v for k, v in found.items() if v}


def _improper_eliminations(run: _Run, candidates: list[_Candidate],
                           revisions: list[_Revision]) -> list[dict[str, Any]]:
    """Deferrals, rejections, revisions and supersessions whose reasons cite coverage data or a z, TPM or peak
    ranking; rejections resting only on proxy-context contradictions; and rejections resting on a contradiction that
    no longer stands (no required claim is contradicted in scope now: a stale rejection the graph could not reinstate,
    such as a second one). A rejection resting on a matched contradiction, and a revision that removed only claims the
    run contradicted in scope, are proper and not listed; a revision that set nothing aside (no TF, group or gene
    dropped) eliminated nothing. The audit reads reinstatements: a rejection a reinstatement withdrew eliminated
    nothing, and a hypothesis standing where its reinstatement put it was restored, not set aside (`reinstatements`
    lists them for a person to check). Mechanical flags for review, never verdicts."""
    graph = run.graph
    out = []
    for h in graph.hypotheses.values():
        if h.disposition not in ("deferred", "rejected") or _restored(h):
            continue
        reasons = _set_aside_reasons(h)
        flags = _flags(" | ".join(reasons))
        contradicted = [c for c in h.required_claim_ids if graph.claims[c].assessment == "contradicted_in_scope"]
        if h.disposition == "rejected" and not contradicted:
            flags["withdrawn_contradiction"] = [f"{c}: {graph.claims[c].assessment}" for c in h.required_claim_ids]
        elif h.disposition == "rejected":
            links = [x for c in contradicted for x in graph.claims[c].evidence_links
                     if x.stance == "contradicts" and x.strength == "direct"]
            if links and all(x.applicability == "proxy" for x in links):
                flags["proxy_context_rejection"] = [f"{x.claim_id}: {x.evidence_id} (proxy)" for x in links]
        if not flags or (contradicted and "proxy_context_rejection" not in flags):
            continue
        names = run.names(h.claim_ids, h, h.member_alternatives)
        out.append({"hypothesis_id": h.hypothesis_id, "step": h.disposition, "version": h.version,
                    "disposition": h.disposition, "reasons": reasons, "flags": flags, "contradicted": contradicted,
                    "dropped": sorted(names.candidates()), "names_acceptable": _acceptable(candidates, names),
                    "reinstated": [str(e.get("event_id")) for e in _reinstatements(h)], "verdict": None})
    for r in revisions:
        dropped = sorted(r.named_before.candidates() - r.named_after.candidates())
        flags = _flags(r.reason)
        removed = [c for c in r.before[0] if c not in r.after[0] and c in graph.claims]
        contradicted = [c for c in removed if graph.claims[c].assessment == "contradicted_in_scope"]
        if not dropped or not flags or (removed and contradicted == removed):
            continue
        out.append({"hypothesis_id": r.hypothesis.hypothesis_id, "step": r.step, "version": r.version,
                    "disposition": r.hypothesis.disposition, "reasons": [r.reason],
                    "flags": flags, "contradicted": contradicted, "dropped": dropped,
                    "names_acceptable": sorted(f"{c.kind}:{c.name}" for c in candidates
                                               if c.names_it(r.named_before) and not c.names_it(r.named_after)),
                    "reinstated": [str(e.get("event_id")) for e in _reinstatements(r.hypothesis)], "verdict": None})
    return out


def _reinstatement_records(run: _Run, candidates: list[_Candidate]) -> list[dict[str, Any]]:
    """Every reinstatement of the run (graph.reinstate): a code rejection withdrawn because the contradiction it
    rested on no longer stood, so the hypothesis came back as deferred. Not an elimination; listed so a person can
    check that the contradiction was rightly withdrawn (a misread passage, a re-assessment), never judged by code."""
    out = []
    for h in run.graph.hypotheses.values():
        names = run.names(h.claim_ids, h, h.member_alternatives)
        for e in _reinstatements(h):
            out.append({"hypothesis_id": h.hypothesis_id, "version": e.get("version"), "event_id": e.get("event_id"),
                        "rejected_by": e.get("rejected_by"), "claims": list(e.get("claims") or []),
                        "reason": str(e.get("reason", "")), "disposition": h.disposition,
                        "names_acceptable": _acceptable(candidates, names), "verdict": None})
    return out


def _unsupported_causal_claims(run: _Run, leaders: list[str]) -> dict[str, Any]:
    graph = run.graph
    rows = [{"hypothesis_id": hid, "claim_id": cid, "relation": c.relation, "required": cid in h.required_claim_ids,
             "assessment": c.assessment, "display": graph.display_status(cid), "dependency_flag": c.dependency_flag,
             "variant": graph.claim_frame(cid), "assertion": c.assertion_text}
            for hid in leaders for h in [graph.hypotheses[hid]] for cid in h.claim_ids
            for c in [graph.claims[cid]] if c.relation in CAUSAL_RELATIONS and c.assessment != "supported_in_scope"]
    return {"claims": rows, "count": len(rows), "required": sum(r["required"] for r in rows),
            "by_relation": dict(sorted(Counter(r["relation"] for r in rows).items()))}


def _fidelity_sheet(run: _Run, leaders: list[str]) -> dict[str, Any]:
    """The links an outcome rests on (the answer's required claims, decisive claims of accepted comparisons, the
    contradictions behind rejections), one row each for a person to check against the source. Each row says which
    variant the claim is about (claim_frame) and which the evidence names (its about_variants, read by
    variant_mention): the graph now refuses a link from evidence about another variant, but a graph written before it
    did may hold one, and a person checks the variant as part of the source."""
    graph = run.graph
    why: dict[tuple[str, str], list[str]] = {}

    def add(claim_id: str, stances: tuple[str, ...], reason: str, direct_only: bool = False) -> None:
        for x in graph.claims[claim_id].evidence_links:
            if x.stance in stances and (not direct_only or x.strength == "direct"):
                why.setdefault((claim_id, x.evidence_id), []).append(reason)

    for hid in leaders:
        for cid in graph.hypotheses[hid].required_claim_ids:
            add(cid, ("supports", "contradicts"), f"required claim of the answer {hid}")
    for p in graph.comparisons.values():
        for cid in (p.decisive_claim_ids if p.accepted else []):
            if cid in graph.claims:
                add(cid, ("supports", "contradicts"), f"decisive in comparison {p.comparison_id}")
    for h in graph.hypotheses.values():
        if h.disposition == "rejected":
            for cid in h.required_claim_ids:
                if graph.claims[cid].assessment == "contradicted_in_scope":
                    add(cid, ("contradicts",), f"behind the rejection of {h.hypothesis_id}", direct_only=True)
    rows = []
    for (cid, eid), reasons in sorted(why.items(), key=lambda kv: (
            RELATION_ORDER[graph.claims[kv[0][0]].relation], _num(kv[0][0]), _num(kv[0][1]))):
        claim, ev = graph.claims[cid], graph.evidence[eid]
        link = next(x for x in claim.evidence_links if x.evidence_id == eid)
        exp = ev.experiment
        rows.append({
            "claim_id": cid, "relation": claim.relation, "assertion": claim.assertion_text,
            "claim_assessment": claim.assessment, "why_decisive": reasons, "stance": link.stance,
            "strength": link.strength, "applicability": link.applicability,
            "code_applicability": link.code_applicability, "corrected": link.corrected, "rationale": link.rationale,
            "evidence_id": eid, "evidence_class": ev.evidence_class, "origin": ev.origin, "access": ev.access,
            "source_ids": ev.source_ids, "observed_result": ev.observed_result,
            "context": ev.context.label if ev.context else None, "allele": ev.allele, "direction": ev.direction,
            "claim_variant": graph.claim_frame(cid), "about_variants": list(ev.about_variants),
            "evidence_variant": run.evidence_variant(ev),
            "passage": exp.passage if exp else None, "location": exp.location if exp else None,
            "intervention": exp.intervention if exp else None, "endpoint": exp.endpoint if exp else None,
            "review": dict(REVIEW_TEMPLATE)})
    return {"instructions": REVIEW_HELP, "auto_scored": False, "rows": rows,
            "by_relation": dict(sorted(Counter(r["relation"] for r in rows).items()))}


def _efficiency(graph: ClaimGraph, metrics: dict[str, Any] | None) -> dict[str, Any]:
    calls = list(graph.tool_calls.values())
    executed = [t for t in calls if t.charged_to != "none"]
    budget = graph.budget_snapshot()
    return {"metrics": metrics or {},
            "graph": {"model_calls": graph.model_usage.calls, "cost_usd": graph.model_usage.cost_usd,
                      "tool_calls_agent": budget.tool_calls, "tool_calls_code": budget.code_tool_calls,
                      "tool_requests_refused": len(calls) - len(executed),
                      "tool_calls_by_status": dict(sorted(Counter(t.execution_status for t in executed).items())),
                      "tool_calls_cached": sum(t.cached for t in executed), "fulltext_reads": budget.fulltext_reads,
                      "evidence_items": len(graph.evidence),
                      "unique_sources": len({s for e in graph.evidence.values() for s in e.source_ids}),
                      "qbic_precompute_required": sum(t.execution_status == "cache_miss" and
                                                      t.tool_name.startswith("qbic") for t in calls)}}


def _supplied_text(case: Case) -> str:
    """The case as the caller supplied it, one value per line: everything of the request that a packet can show. Left
    out: what the run added (inferred candidates) and intake's own notes, which say how intake read the request's
    variant text (checked separately) and what it found, never what the caller wrote."""
    v = case.variant
    values = [case.case_id, v.input_text, v.rsid or "", case.origin, *case.supplied_disease,
              *(s.label for s in case.supplied_context),
              *(x for key, value in case.input_provenance.items() if key not in PROVENANCE_KEYS for x in (key, value))]
    return "\n".join(x for x in values if x)


def _isolation(graph: ClaimGraph, entry: dict[str, Any], config: Config | None) -> tuple[Arm, list[str]]:
    """Which clean request the run was made from, and anything in the case as supplied that a clean request would
    not hold: another id, a context, another origin or disease, a bracket, an rsID or other variant text, caller
    provenance, or any label-derived string of the gold row. Only the request is checked: an rsID a tool found for
    the coordinates (a recorded alias) or a candidate the run inferred is the run's own work, not a leak."""
    if not isinstance(row := entry.get("row"), Mapping):
        raise ValueError(f"the spec entry {entry.get('case_id')} has no CSV row (an older spec): rebuild the spec")
    case, requests = graph.case, entry.get("requests") or {}
    arm = next((a for a in ARMS if (requests.get(a) or {}).get("request_id") == case.case_id), None)
    problems = [] if arm else [f"case id {case.case_id} is not the opaque id of a clean request for this case"]
    arm = arm or ("supplied_disease" if case.supplied_disease else "main")
    expected = requests.get(arm) or {}
    if case.supplied_context:
        problems.append("the run was given a context; gold context is withheld in every arm")
    if any(bracketed_parts(d) for d in case.supplied_disease):
        problems.append("the supplied disease carries bracketed text")
    if expected and case.origin != expected.get("origin"):
        problems.append(f"origin {case.origin} differs from the clean request's {expected.get('origin')}")
    supplied = [d.casefold() for d in case.supplied_disease]
    if expected and supplied != [d.casefold() for d in expected.get("disease") or []]:
        problems.append("the supplied disease differs from the clean request's")
    variant = case.variant
    if variant.rsid:
        problems.append(f"the run was given rsID {variant.rsid}; a clean request names the variant by coordinates "
                        "only")
    if expected and variant.input_text != expected.get("variant"):
        problems.append(f"the variant was given as {variant.input_text!r}, not as the clean request's "
                        f"{expected.get('variant')!r}")
    if extra := sorted(set(case.input_provenance) - PROVENANCE_KEYS):
        problems.append(f"the request carried provenance notes ({', '.join(extra)}); a clean request carries none")
    if found := find_label_strings(_supplied_text(case), label_strings(row, arm=arm, config=config)):
        problems.append(f"label-derived strings in the case as supplied: {', '.join(found)}")
    return arm, problems


def audit(run_dir: str | Path, spec_entry: dict[str, Any], *, config: Config | None = None) -> dict[str, Any]:
    """The content of evaluation.json for one run folder and one gold spec entry (see the module docstring).
    Deterministic: the same folder and entry always give the same result. Raises ValueError when the run is for
    another variant than the entry. Every score is provisional unless the entry comes from a reviewed spec
    (spec_entry carries the spec's status). A run that assessed nothing (outcome.assessed False: stopped by
    engine_error or cache_miss, refused as input, or no result) is reported, not scored."""
    run_dir = Path(run_dir)
    if not (run_dir / "graph.json").is_file():
        raise FileNotFoundError(f"{run_dir} has no graph.json: not a v9 run folder")
    graph = ClaimGraph.from_json((run_dir / "graph.json").read_text())
    if graph.case.variant.key != spec_entry["variant"]["key"]:
        raise ValueError(f"the run is for {graph.case.variant.key}, the spec entry {spec_entry['case_id']} for "
                         f"{spec_entry['variant']['key']}")
    manifest, metrics = _json_file(run_dir / "manifest.json"), _json_file(run_dir / "metrics.json")
    run = _Run(graph, load_reference(config, required=False))
    arm, problems = _isolation(graph, spec_entry, config)
    leaders = _leaders(graph)
    result = graph.result
    outcome = _outcome(graph)
    standing, excluded = _answer_claims(run, leaders)
    components = _component_recovery(run, spec_entry, leaders, standing, outcome)
    revisions = _revisions(run)
    candidates = _candidates(run, spec_entry["components"])
    status = str(spec_entry.get("spec_status") or UNREVIEWED)
    final = status == REVIEWED
    control = None
    if spec_entry.get("control"):
        control = {"expected": spec_entry.get("expected"), "outcome": result.outcome if result else None,
                   "kind": outcome["kind"], "assessed": outcome["assessed"],
                   "note": "" if outcome["assessed"] else f"not a null: {outcome['note']}",
                   "supported_causal_claims": [
                       {"hypothesis_id": hid, "claim_id": cid, "relation": graph.claims[cid].relation,
                        "variant": graph.claim_frame(cid)}
                       for hid in leaders for cid in graph.hypotheses[hid].claim_ids
                       if graph.claims[cid].relation in CAUSAL_RELATIONS
                       and graph.claims[cid].assessment == "supported_in_scope"]}
    entry_hash = hashlib.sha256(json.dumps(spec_entry, sort_keys=True, ensure_ascii=False).encode()).hexdigest()
    return {
        "evaluator_only": "never read by the engine or shown to an agent",
        "spec": {"case_id": spec_entry["case_id"], "label_class": spec_entry.get("label_class"),
                 "control": bool(spec_entry.get("control")), "entry_sha256": entry_hash, "status": status,
                 "provisional": not final, "needs_review": bool(spec_entry.get("needs_review"))},
        "run": {"request_id": graph.case.case_id, "variant": graph.case.variant.key, "arm": arm,
                "mode": (manifest or {}).get("mode"), "engine_version": graph.engine_version,
                "outcome": result.outcome if result else None, "stop_reason": result.stop_reason if result else None,
                "budget_stop": result.budget_stop if result else None, "answer": leaders,
                "variant_aliases": sorted(graph.variant_aliases)},
        "outcome": outcome,
        "isolation": {"clean": not problems, "problems": problems},
        "answer_claims": {"standing": standing, "excluded": excluded},
        "components": components,
        "component_recovery": {name: {"numerator": c["numerator"], "denominator": c["denominator"],
                                      "provisional": c["denominator"] > 0 and (c["needs_review"] or not final)}
                               for name, c in components.items()},
        "candidate_retention": _candidate_retention(run, candidates, metrics, revisions),
        "improper_elimination": _improper_eliminations(run, candidates, revisions),
        "reinstatements": _reinstatement_records(run, candidates),
        "unsupported_causal_claims": _unsupported_causal_claims(run, leaders),
        "evidence_fidelity": _fidelity_sheet(run, leaders),
        "efficiency": _efficiency(graph, metrics),
        "control": control,
        "reference_files": {name: name in run.ref.files for name in ("groups_sha256", "hgnc_sha256",
                                                                     "lambert_sha256")},
    }


def write_evaluation(run_dir: str | Path, spec_entry: dict[str, Any], *, config: Config | None = None) -> Path:
    """Write audit(...) to the run folder's evaluation.json, which is never overwritten."""
    path = Path(run_dir) / EVALUATION_FILE
    if path.exists():
        raise FileExistsError(f"{path} exists: an evaluation is never overwritten; move it aside to audit again")
    content = audit(run_dir, spec_entry, config=config)
    with open(path, "x", encoding="utf-8") as f:
        f.write(json.dumps(content, indent=1, ensure_ascii=False) + "\n")
    return path


def run_suite(manifest: str | Path, budget_usd: float | None) -> NoReturn:
    """Run a frozen evaluation suite (the manifest of clean requests) under an explicit currency cap. Refused without
    a positive cap before anything is read or run; not implemented in this build, because a gold run needs the
    user's approved cap and profile."""
    if isinstance(budget_usd, bool) or not isinstance(budget_usd, int | float) or not math.isfinite(budget_usd) \
            or budget_usd <= 0:
        raise SuiteRefusal(f"an evaluation suite needs an explicit positive currency cap (--budget-usd); nothing "
                           f"was run for {manifest}")
    raise NotImplementedError("needs the user's approved cap and profile")
