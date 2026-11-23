"""Intake: the normalise step (SPEC 6 step 1, 13.2, 13.12). A request becomes the Case a run works on.

Why this is code and not an agent step: a wrong allele, a minus-strand or swapped notation, or an ambiguous rsID must
never reach a prediction, and nothing an agent reads may say more than the user supplied. So intake

- reads the variant in the forms `qbic.variants.parse` accepts (chr2:60490908:T>G, chr2-60490908-T-G,
  2:60490908 T>G), the Variant.key form (GRCh38:2:60490908:T:G) and rsIDs (rs1427407, or rs1427407:G to name the
  alternate allele of a multiallelic record). GRCh38, 1-based, plus strand; a position past the end of its GRCh38
  chromosome is refused before any lookup. SNVs are the scoring target; indels and multi-base changes are accepted
  with variant_type "indel" or "other", so routes other than QBiC-SELEX still apply;
- resolves an rsID through Ensembl with the run's HTTP client (an Http9 or anything with `.get` and `.offline`).
  Outside live mode the client is offline, so only a cached response counts; a record with several alternate alleles
  is refused unless the request names one, and so is one that maps to several places or to the minus strand;
- checks the reference allele, cheapest and most local first: the cached QBiC-SELEX 21-mer (cache/qbic.sqlite, read
  only; the base at index 10 is the GRCh38 base, whatever alleles the cached row was for), the local GRCh38 FASTA
  through pysam (only when its .fai index exists: building one would write beside the genome), then Ensembl through
  the HTTP client (in cache_only mode a saved response only), else "unavailable". A mismatch is recorded, not
  raised: the engine stops on it with input_or_capability_limitation and the case's input_provenance says why (with
  a minus-strand hint when the complement matches). Every note intake writes depends only on the request and the
  GRCh38 bases, never on which source answered or whether a response came from the cache: the notes reach every
  agent packet, so a replay must see the same text as the live run (and a precomputed 21-mer must not change it);
- keeps the origin exactly as supplied ("unknown" when absent). It is never inferred from a database: a locus that
  appears in a cancer catalogue says nothing about how this sample's allele arose;
- removes bracketed text from each supplied disease (in the gold set brackets name loci and genes: "(1p13)",
  "(FTO)") and notes from each supplied context, which context_match then normalises;
- names the case with the request's id, else REQ- plus the first 12 hex digits of the sha256 of the normalised request
  (variant key, origin, disease, context), so the id is opaque and the same request always gets the same id.
"""

import hashlib
import json
import re
import sqlite3
from collections.abc import Iterable, Sequence
from pathlib import Path
from typing import Any, Literal

from pydantic import Field

from ..config import Config, ConfigError
from ..qbic.cache import settings_hash
from .context_match import UNSPECIFIED, scope_from_label
from .schemas import Case, Origin, RunMode, V9Model, Variant, variant_type_of

ENSEMBL = "https://rest.ensembl.org"
# GRCh38 primary-assembly chromosome lengths (GCA_000001405.15; the lengths in hg38.fa.fai). Fixed for the assembly,
# so a position past a chromosome's end is refused offline, before any lookup could mistake it for a gap in coverage.
GRCH38_LENGTHS = {"1": 248956422, "2": 242193529, "3": 198295559, "4": 190214555, "5": 181538259, "6": 170805979,
                  "7": 159345973, "8": 145138636, "9": 138394717, "10": 133797422, "11": 135086622, "12": 133275309,
                  "13": 114364328, "14": 107043718, "15": 101991189, "16": 90338345, "17": 83257441, "18": 80373285,
                  "19": 58617616, "20": 64444167, "21": 46709983, "22": 50818468, "X": 156040895, "Y": 57227415,
                  "MT": 16569}
CHROMOSOMES = frozenset(GRCH38_LENGTHS)
COMPLEMENT = str.maketrans("ACGT", "TGCA")
CONTEXT_LENGTH = 10                     # QBiC-SELEX 21-mers: 10 bp each side, the variant base at index 10
BASES = re.compile(r"^[ACGT]+$")
REQUEST_ID = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]{0,63}$")
OTHER_ASSEMBLY = re.compile(r"grch37|hg19|\bb37\b", re.I)
FORMS = (
    re.compile(r"^(?:chr)?(\w+):(\d+):([A-Za-z]+)>([A-Za-z]+)$", re.I),          # chr2:60490908:T>G
    re.compile(r"^(?:chr)?(\w+)-(\d+)-([A-Za-z]+)-([A-Za-z]+)$", re.I),          # chr2-60490908-T-G
    re.compile(r"^(?:chr)?(\w+):(\d+)\s+([A-Za-z]+)>([A-Za-z]+)$", re.I),        # 2:60490908 T>G
    re.compile(r"^GRCh38:(?:chr)?(\w+):(\d+):([A-Za-z]+):([A-Za-z]+)$", re.I),   # GRCh38:2:60490908:T:G
)
RSID = re.compile(r"^(rs\d+)(?:[:\s]+(?:([A-Za-z]+)>)?([A-Za-z]+))?$", re.I)     # rs1, rs1:T, rs1 G>T
FORMS_HELP = ("use chr2:60490908:T>G, chr2-60490908-T-G, 2:60490908 T>G, GRCh38:2:60490908:T:G or an rsID such as "
              "rs1427407 (rs1427407:G names the alternate allele); GRCh38, 1-based, plus strand")
BRACKETED = re.compile(r"[(\[{][^()\[\]{}]*[)\]}]")
ReferenceCheck = Literal["verified", "mismatch", "unavailable"]
UNAVAILABLE = ("unavailable: no GRCh38 reference source answered (a cached QBiC-SELEX 21-mer, an indexed local FASTA, "
               "or Ensembl in a live run or from its saved response)")
# The input_provenance keys build_case writes itself; they win over the caller's. A clean evaluation request adds
# no other key, which the evaluator checks.
PROVENANCE_KEYS = frozenset({"variant", "reference_check", "origin", "disease", "context"})


class IntakeError(ValueError):
    """A request intake cannot turn into a case; `message` says what to change."""

    def __init__(self, message: str):
        super().__init__(message)
        self.message = message


class Request(V9Model):
    """What a user (or the evaluation harness) asks about. Only `variant` is required: origin, disease and context
    are optional inputs, recorded as supplied and never inferred. `provenance` holds the caller's notes on where an
    input came from; what intake itself checks (the variant, the reference, which inputs were supplied) wins."""
    variant: str
    origin: Origin = "unknown"
    disease: list[str] = Field(default_factory=list)
    context: list[str] = Field(default_factory=list)
    request_id: str | None = None
    provenance: dict[str, str] = Field(default_factory=dict)


# --- text helpers (shared with evaluation.py) -------------------------------------------------------------------------

def bracketed_parts(text: str) -> list[str]:
    """The texts inside brackets, innermost first ("LDL (1p13)" -> ["1p13"]); an unclosed bracket runs to the end."""
    parts, current = [], str(text)
    while found := BRACKETED.findall(current):
        parts += [inner for p in found if (inner := " ".join(p[1:-1].split()))]
        current = BRACKETED.sub(" ", current)
    if (tail := re.search(r"[(\[{](.*)$", current)) and (inner := " ".join(tail.group(1).split())):
        parts.append(inner)
    return parts


def strip_bracketed(text: str) -> str:
    """The text without any bracketed part (nested, unclosed or stray brackets included), whitespace collapsed."""
    current = str(text)
    while (stripped := BRACKETED.sub(" ", current)) != current:
        current = stripped
    current = re.sub(r"[)\]}]", " ", re.sub(r"[(\[{].*$", " ", current))
    return " ".join(current.split()).strip(" ,;:")


def _cleaned(values: Iterable[str]) -> list[str]:
    """Bracket-free, whitespace-collapsed, non-placeholder values, first spelling kept, case-insensitively unique."""
    out: dict[str, str] = {}
    for value in values:
        text = strip_bracketed(value)
        if text and text.lower() not in UNSPECIFIED:
            out.setdefault(text.casefold(), text)
    return list(out.values())


def normalise_disease(values: Iterable[str]) -> list[str]:
    """Supplied diseases without bracketed text: a bracket can carry a locus or gene hint that was never supplied
    as a disease ("Obesity (FTO)" -> "Obesity")."""
    return _cleaned(values)


def normalise_context_labels(values: Iterable[str]) -> list[str]:
    """Supplied context labels without notes ("GTEx:Adipose - Subcutaneous (proxy for preadipocytes)" -> the GTEx
    name): a note says why someone chose a context, which is not part of the context itself."""
    return _cleaned(values)


# --- the variant -------------------------------------------------------------------------------------------------------

def _chromosome(text: str) -> str:
    chrom = re.sub(r"^chr", "", text.strip(), flags=re.I).upper()
    chrom = {"M": "MT"}.get(chrom, chrom.lstrip("0") if chrom.isdigit() else chrom)
    if chrom not in CHROMOSOMES:
        raise IntakeError(f"{text} is not a GRCh38 primary chromosome (use 1-22, X, Y or MT)")
    return chrom


def _variant(chrom: str, pos: int, ref: str, alt: str, text: str, rsid: str | None = None) -> Variant:
    ref, alt = ref.upper(), alt.upper()
    if not (BASES.match(ref) and BASES.match(alt)):
        raise IntakeError(f"alleles must be A, C, G or T (got {ref}>{alt}); write an indel VCF-style with its anchor "
                          "base, e.g. chr1:100:AT>A")
    if ref == alt:
        raise IntakeError(f"ref and alt are the same ({ref})")
    if pos < 1:
        raise IntakeError(f"positions are 1-based (got {pos})")
    chrom = _chromosome(chrom)
    if (end := pos + len(ref) - 1) > (length := GRCH38_LENGTHS[chrom]):
        raise IntakeError(f"{chrom}:{pos if end == pos else f'{pos}-{end}'} is past the end of chromosome {chrom} "
                          f"({length} bp in GRCh38): check the position and the assembly")
    return Variant(chrom=chrom, pos=pos, ref=ref, alt=alt, rsid=rsid, input_text=text,
                   variant_type=variant_type_of(ref, alt))


def parse_coordinates(text: str) -> Variant:
    """A GRCh38 variant from coordinate text (no network, no reference check); raises IntakeError."""
    text = " ".join(str(text).split())
    if OTHER_ASSEMBLY.search(text):
        raise IntakeError("only GRCh38 coordinates are accepted; lift the variant over to GRCh38 first")
    match = next((m for form in FORMS if (m := form.match(text))), None)
    if match is None:
        if re.search(r">[A-Za-z]+,", text):
            raise IntakeError(f"{text} lists several alternate alleles; a request names one")
        raise IntakeError(f"could not read {text!r} as a variant: {FORMS_HELP}")
    chrom, pos, ref, alt = match.groups()
    return _variant(chrom, int(pos), ref, alt, text)


def _resolve_rsid(text: str, match: re.Match, http: Any, mode: RunMode) -> tuple[Variant, str]:
    """An rsID through Ensembl's variation endpoint (the same URL v8 used, so saved responses are shared)."""
    rsid, given_ref, given_alt = match.group(1).lower(), match.group(2), match.group(3)
    given_ref, given_alt = (given_ref or "").upper() or None, (given_alt or "").upper() or None
    if http is None:
        raise IntakeError(f"{rsid} needs Ensembl to resolve and this run has no HTTP client; give GRCh38 coordinates "
                          "such as chr2:60490908:T>G")
    result = http.get(f"{ENSEMBL}/variation/human/{rsid}?content-type=application/json")
    if not result.ok:
        if getattr(http, "offline", False):
            raise IntakeError(f"{rsid} is not in the HTTP cache and this {mode} run may not use the network; give "
                              "GRCh38 coordinates (chrom:pos:ref>alt) or resolve it in a live run first")
        raise IntakeError(f"Ensembl could not resolve {rsid}: {result.error}")
    data = result.data if isinstance(result.data, dict) else {}
    maps = [m for m in data.get("mappings") or [] if m.get("assembly_name") == "GRCh38"
            and str(m.get("seq_region_name")) in CHROMOSOMES and isinstance(m.get("start"), int)]
    places = sorted({f"{m['seq_region_name']}:{m['start']}" for m in maps})
    if not maps:
        raise IntakeError(f"{rsid} has no GRCh38 mapping on a primary chromosome in Ensembl")
    if len(places) > 1:
        raise IntakeError(f"{rsid} maps to {len(places)} GRCh38 places ({', '.join(places)}); give coordinates")
    m = maps[0]
    if m.get("strand", 1) != 1:
        raise IntakeError(f"{rsid} maps to the minus strand in Ensembl; give plus-strand GRCh38 coordinates")
    alleles = [a.upper() for a in str(m.get("allele_string", "")).split("/")]
    ref, alts = alleles[0], alleles[1:]
    if not all(BASES.match(a) for a in alleles):
        raise IntakeError(f"{rsid} is an insertion or deletion in Ensembl's notation ({m.get('allele_string')}); give "
                          "VCF-style coordinates with the anchor base, e.g. chr1:100:AT>A")
    if not alts:
        raise IntakeError(f"{rsid} has no alternate allele in Ensembl")
    if given_ref and given_ref != ref:
        raise IntakeError(f"the reference allele of {rsid} is {ref} in Ensembl GRCh38, not {given_ref}")
    if given_alt is None:
        if len(alts) != 1:
            raise IntakeError(f"{rsid} is multiallelic in Ensembl (alternate alleles {', '.join(alts)}): name the one "
                              f"you mean, e.g. {rsid}:{alts[0]}")
        given_alt = alts[0]
    elif given_alt not in alts:
        raise IntakeError(f"{given_alt} is not an alternate allele of {rsid} in Ensembl ({', '.join(alts)})")
    name = str(data.get("name") or rsid).lower()
    current = name if re.fullmatch(r"rs\d+", name) else rsid
    variant = _variant(str(m["seq_region_name"]), m["start"], ref, given_alt, text, rsid=current)
    # Whether the record came live or from the HTTP cache is left out: a replay resolves it from the saved response
    # and must write the same note as the live run did.
    how = f"rsID {rsid} resolved through Ensembl GRCh38" + (f"; Ensembl names it {current}" if current != rsid else "")
    return variant, how


# --- the reference check -----------------------------------------------------------------------------------------------

def _cached_21mer_base(variant: Variant, config: Config) -> str | None:
    """The GRCh38 base at the variant from a cached QBiC-SELEX 21-mer at the same position under this configuration's
    settings (whose hash covers the genome index), or None. QBiC-SELEX stores a 21-mer only after its own check that
    the genome base equals the row's ref, so the stored base is the genome's whatever alleles the row was for."""
    if variant.variant_type != "SNV":
        return None
    try:
        path = config.path("cache", "db")
        hashes = (settings_hash(config, True), settings_hash(config, False))
    except (KeyError, ConfigError, OSError):
        return None
    if not path.is_file():
        return None
    prefix = f"chr{variant.chrom}:{variant.pos}:"
    try:
        con = sqlite3.connect(f"{path.resolve().as_uri()}?mode=ro", uri=True)
        try:
            rows = con.execute("SELECT ref_sequence FROM sequences WHERE settings_hash IN (?, ?) "
                               "AND substr(variant_key, 1, ?) = ?", (*hashes, len(prefix), prefix)).fetchall()
        finally:
            con.close()
    except sqlite3.Error:
        return None
    bases = {seq[CONTEXT_LENGTH].upper() for (seq,) in rows
             if isinstance(seq, str) and len(seq) == 2 * CONTEXT_LENGTH + 1}
    return bases.pop() if len(bases) == 1 else None


def _contigs(chrom: str) -> tuple[str, ...]:
    return ("chrM", "MT", "chrMT", "M") if chrom == "MT" else (f"chr{chrom}", chrom)


def _genome_bases(variant: Variant, config: Config) -> str | None:
    """The reference bases from the local GRCh38 FASTA (config local.genome), only when its .fai index exists. The
    position is already within its GRCh38 chromosome (checked at parse), so a contig too short to hold it means the
    file is not the full assembly, and it is passed over as a source rather than blamed on the request."""
    try:
        path = config.path("local", "genome")
    except (KeyError, ConfigError):
        return None
    if not path.is_file() or not Path(f"{path}.fai").is_file():
        return None
    try:
        import pysam
    except ImportError:
        return None
    start = variant.pos - 1
    try:
        with pysam.FastaFile(str(path)) as fasta:
            contig = next((c for c in _contigs(variant.chrom) if c in fasta.references), None)
            if contig is None or start + len(variant.ref) > fasta.get_reference_length(contig):
                return None
            return fasta.fetch(contig, start, start + len(variant.ref)).upper()
    except (OSError, ValueError, KeyError):
        return None


def _ensembl_bases(variant: Variant, http: Any) -> str | None:
    """The reference bases from Ensembl's GRCh38 sequence endpoint (the URL qbic.variants uses for an SNV)."""
    if http is None:
        return None
    end = variant.pos + len(variant.ref) - 1
    result = http.get(f"{ENSEMBL}/sequence/region/human/{variant.chrom}:{variant.pos}..{end}:1"
                      "?content-type=text/plain")
    if not result.ok:
        return None
    data = result.data.get("seq") if isinstance(result.data, dict) else result.data
    seq = str(data or "").strip().upper()
    return seq if BASES.match(seq) and len(seq) == len(variant.ref) else None


def _mismatch(variant: Variant, genome: str) -> str:
    note = f"mismatch: GRCh38 has {genome} at {variant.chrom}:{variant.pos}, the request gives ref {variant.ref}"
    if variant.variant_type == "SNV" and genome == variant.ref.translate(COMPLEMENT):
        plus = f"chr{variant.chrom}:{variant.pos}:{genome}>{variant.alt.translate(COMPLEMENT)}"
        note += f"; the alleles look like minus-strand notation (plus strand: {plus})"
    return note


def check_reference(variant: Variant, *, config: Config, http: Any) -> tuple[ReferenceCheck, str]:
    """The reference check and its note. Sources are tried in the module docstring's order and the first that answers
    decides; all of them read GRCh38, so the note states the bases, not the source, and is the same whichever answered
    (a replay may find a 21-mer that the live run had to fetch from Ensembl)."""
    for fetch in (lambda: _cached_21mer_base(variant, config), lambda: _genome_bases(variant, config),
                  lambda: _ensembl_bases(variant, http)):
        genome = fetch()
        if genome is None:
            continue
        if genome == variant.ref:
            return "verified", f"verified: GRCh38 has {genome} at {variant.chrom}:{variant.pos}"
        return "mismatch", _mismatch(variant, genome)
    return "unavailable", UNAVAILABLE


# --- the case ----------------------------------------------------------------------------------------------------------

def request_id(variant: Variant, origin: str, disease: Sequence[str], context: Sequence[str]) -> str:
    """REQ- plus the first 12 hex digits of the sha256 of the normalised request. The variant enters as its key, so
    every way of writing it gives the same id; disease and context labels enter sorted and case-folded."""
    body = {"variant": variant.key, "origin": origin, "disease": sorted(d.casefold() for d in disease),
            "context": sorted(c.casefold() for c in context)}
    blob = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return "REQ-" + hashlib.sha256(blob.encode()).hexdigest()[:12]


def _given_id(value: str) -> str:
    if not REQUEST_ID.match(value):
        raise IntakeError("a request id may use letters, digits, '.', '_' and '-' (at most 64 characters), so it can "
                          "name a run folder")
    if value.upper().startswith("SYN-"):
        raise IntakeError("request ids starting SYN- are reserved for synthetic fixtures")
    return value


def build_case(request: Request, *, config: Config, http: Any, mode: RunMode) -> Case:
    """The normalised Case for a request; raises IntakeError when the variant cannot be read or resolved. Outside
    live mode `http` (when given) must be offline, so intake can never reach the network there."""
    if mode != "live" and http is not None and getattr(http, "offline", False) is not True:
        raise ValueError(f"{mode} mode needs an offline HTTP client: intake must never reach the network")
    text = " ".join(request.variant.split())
    if not text:
        raise IntakeError(f"no variant given: {FORMS_HELP}")
    if rs := RSID.match(text):
        variant, how = _resolve_rsid(text, rs, http, mode)
    else:
        variant, how = parse_coordinates(text), "GRCh38 coordinates as supplied"
    check, note = check_reference(variant, config=config, http=http)
    variant = variant.model_copy(update={"reference_check": check})
    disease = normalise_disease(request.disease)
    contexts = normalise_context_labels(request.context)
    scopes = [scope_from_label(label, source="supplied", variant=variant) for label in contexts]
    case_id = (_given_id(request.request_id) if request.request_id
               else request_id(variant, request.origin, disease, contexts))
    checked = {"variant": how, "reference_check": note,
               "origin": "supplied" if request.origin != "unknown" else
               "not supplied: unknown (never inferred from database membership)",
               "disease": "supplied" if disease else "not supplied",
               "context": "supplied" if scopes else "not supplied"}           # PROVENANCE_KEYS, exactly
    return Case(case_id=case_id, variant=variant, origin=request.origin, supplied_disease=disease,
                supplied_context=scopes, input_provenance={**request.provenance, **checked})
