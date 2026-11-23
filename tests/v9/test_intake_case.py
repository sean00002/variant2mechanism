"""Intake (SPEC 6 step 1, 13.2, 13.12): variant forms, chromosome ends, rsID resolution offline, the reference check,
notes that do not depend on cache state, origin, disease and context normalisation, and opaque request ids.

The biological variant here is the development case rs1427407 (chr2:60490908 T>G), cached in qbic.sqlite and not in
the gold set; Ensembl records and sequences are stipulated for the test.
"""

import copy
import hashlib
import json
import re

import pysam
import pytest

from variant2mechanism.config import Config
from variant2mechanism.context.http import Http, HttpResult, cache_key
from variant2mechanism.v9.intake import (
    PROVENANCE_KEYS,
    IntakeError,
    Request,
    build_case,
    check_reference,
    parse_coordinates,
)

DEV = "chr2:60490908:T>G"
VARIATION = "https://rest.ensembl.org/variation/human/rs1427407?content-type=application/json"
SEQUENCE = "https://rest.ensembl.org/sequence/region/human/2:60490908..60490908:1?content-type=text/plain"
WHEN = "2026-11-08T00:00:00+00:00"


def mapping(chrom="2", start=60490908, alleles="T/G", strand=1, assembly="GRCh38") -> dict:
    return {"assembly_name": assembly, "seq_region_name": chrom, "start": start, "end": start, "strand": strand,
            "allele_string": alleles, "location": f"{chrom}:{start}-{start}"}


def record(*mappings, name="rs1427407") -> dict:
    return {"name": name, "var_class": "SNP", "mappings": list(mappings) or [mapping()]}


class FakeHttp:
    """An Http-like client answering from a dict; offline means it never pretends to have reached the network."""

    def __init__(self, responses: dict, offline: bool):
        self.responses, self.offline, self.urls = responses, offline, []

    def get(self, url: str, **kw) -> HttpResult:
        self.urls.append(url)
        if url in self.responses:
            return HttpResult(True, 200, self.responses[url], url, WHEN, cached=self.offline)
        error = f"offline and not cached: GET {url}" if self.offline else "HTTP 503: unavailable"
        return HttpResult(False, None, None, url, WHEN, error=error)


def saved_http(tmp_path, data: dict) -> Http:
    """The real HTTP client, offline, with one saved Ensembl response in its cache folder."""
    folder = tmp_path / "http"
    folder.mkdir(exist_ok=True)
    (folder / f"{cache_key('GET', VARIATION)}.json").write_text(json.dumps(
        {"method": "GET", "url": VARIATION, "body": None, "status": 200, "retrieved_utc": WHEN, "data": data}))
    return Http(folder, offline=True)


def config_with(cfg: Config, *, db=None, genome=None) -> Config:
    """The isolated configuration with the QBiC cache and the local genome pointed elsewhere (or nowhere)."""
    data = copy.deepcopy(dict(cfg))
    data["cache"] = {**data["cache"], "db": str(db)}
    data["local"] = {**data["local"], "genome": str(genome)}
    return Config(data)


def case(text: str, cfg: Config, http=None, mode="cache_only", **kw):
    return build_case(Request(variant=text, **kw), config=cfg, http=http, mode=mode)


# --- variant forms and ids --------------------------------------------------------------------------------------------

def test_every_coordinate_form_gives_the_same_variant_and_opaque_id(v9_cfg):
    forms = [DEV, "2:60490908 T>G", "chr2-60490908-T-G", "GRCh38:2:60490908:T:G", "CHR2:60490908:t>g"]
    cases = [case(f, v9_cfg) for f in forms]
    assert {c.variant.key for c in cases} == {"GRCh38:2:60490908:T:G"}
    assert len({c.case_id for c in cases}) == 1
    assert re.fullmatch(r"REQ-[0-9a-f]{12}", cases[0].case_id)
    assert [c.variant.input_text for c in cases] == forms
    assert all(c.variant.variant_type == "SNV" and c.variant.rsid is None for c in cases)


def test_the_id_follows_the_normalised_request_not_its_wording(v9_cfg):
    base = case(DEV, v9_cfg, disease=["Anaemia", "Thalassaemia"]).case_id
    assert case(DEV, v9_cfg, disease=["thalassaemia (beta)", "ANAEMIA"]).case_id == base
    assert case(DEV, v9_cfg, disease=["Anaemia"]).case_id != base
    assert case(DEV, v9_cfg, origin="germline", disease=["Anaemia", "Thalassaemia"]).case_id != base
    assert case(DEV, v9_cfg, request_id="dev-run.1").case_id == "dev-run.1"
    for bad, why in [("../escape", "letters, digits"), ("SYN-1", "synthetic fixtures"), ("a b", "letters, digits")]:
        with pytest.raises(IntakeError, match=why):
            case(DEV, v9_cfg, request_id=bad)


@pytest.mark.parametrize("text, why", [
    ("chr2:60490908:T>G,C", "several alternate alleles"),
    ("chrUn:5:A>G", "primary chromosome"),
    ("hg19 chr2:60718043:T>G", "only GRCh38"),
    ("chr2:60490908:T>T", "the same"),
    ("chr2:60490908:T>N", "A, C, G or T"),
    ("chr2:0:T>G", "1-based"),
    ("near the BCL11A enhancer", "could not read"),
    ("", "no variant given"),
])
def test_unreadable_variants_are_refused_with_a_message(v9_cfg, text, why):
    with pytest.raises(IntakeError, match=why):
        case(text, v9_cfg)


def test_indels_and_multibase_changes_are_typed_not_refused():
    assert parse_coordinates("chr2:60490908:TA>T").variant_type == "indel"
    assert parse_coordinates("chr2:60490908:TA>GC").variant_type == "other"


@pytest.mark.parametrize("text", ["chr21:46709984:C>T", "chr21:46709983:CA>C", "chrM:16570:A>G", "chrY:57227416:A>G",
                                  "1:300000000 A>G"])
def test_positions_past_a_chromosome_end_are_refused(v9_cfg, text):
    """Refused offline at parse, before any lookup could report the position as merely unchecked."""
    with pytest.raises(IntakeError, match="past the end of chromosome"):
        case(text, v9_cfg)


def test_the_last_base_of_a_chromosome_is_accepted():
    assert parse_coordinates("chr21:46709983:C>T").pos == 46709983
    assert parse_coordinates("chrMT:16569:A>G").chrom == "MT"


def test_an_online_client_is_refused_outside_live_mode(v9_cfg):
    with pytest.raises(ValueError, match="offline HTTP client"):
        case(DEV, v9_cfg, http=FakeHttp({}, offline=False), mode="cache_only")


# --- the reference check ----------------------------------------------------------------------------------------------

def test_the_reference_is_verified_from_the_cached_21mer_read_only(v9_cfg, tmp_path):
    db = v9_cfg.path("cache", "db")
    only_21mer = config_with(v9_cfg, db=db, genome=tmp_path / "absent.fa")
    before = hashlib.sha256(db.read_bytes()).hexdigest(), db.stat().st_mtime_ns
    verified = case(DEV, only_21mer)
    assert verified.variant.reference_check == "verified"
    assert verified.input_provenance["reference_check"] == "verified: GRCh38 has T at 2:60490908"
    swapped = case("chr2:60490908:G>T", only_21mer)         # the base at index 10 is T whatever the cached row's alleles
    assert swapped.variant.reference_check == "mismatch"
    assert "GRCh38 has T" in swapped.input_provenance["reference_check"]
    minus = case("chr2:60490908:A>C", only_21mer)           # A is T's complement: written on the minus strand
    assert minus.variant.reference_check == "mismatch"
    assert "minus-strand" in minus.input_provenance["reference_check"]
    assert "chr2:60490908:T>G" in minus.input_provenance["reference_check"]
    assert (hashlib.sha256(db.read_bytes()).hexdigest(), db.stat().st_mtime_ns) == before
    assert not db.with_name(db.name + "-journal").exists()


def test_without_a_21mer_the_local_genome_is_read_and_never_indexed(v9_cfg, tmp_path):
    fasta = tmp_path / "mini.fa"
    fasta.write_text(">chr21\n" + "ACGT" * 25 + "\n")            # position 50 is C
    plain = config_with(v9_cfg, db=tmp_path / "absent.sqlite", genome=fasta)
    assert case("chr21:50:C>T", plain).variant.reference_check == "unavailable"
    assert not (tmp_path / "mini.fa.fai").exists()                # no index is built beside a genome
    pysam.faidx(str(fasta))
    assert case("chr21:50:C>T", plain).variant.reference_check == "verified"
    assert case("chr21:50:C>T", plain).input_provenance["reference_check"] == "verified: GRCh38 has C at 21:50"
    assert case("chr21:50:A>T", plain).variant.reference_check == "mismatch"
    minus = case("chr21:50:G>T", plain)
    assert minus.variant.reference_check == "mismatch" and "minus-strand" in minus.input_provenance["reference_check"]
    assert case("chr21:50:CG>C", plain).variant.reference_check == "verified"     # an indel compares its whole ref
    assert case("chr21:50:CA>C", plain).variant.reference_check == "mismatch"


def test_ensembl_checks_the_reference_live_or_from_a_saved_response(v9_cfg, tmp_path):
    nothing_local = config_with(v9_cfg, db=tmp_path / "absent.sqlite", genome=tmp_path / "absent.fa")
    live = FakeHttp({SEQUENCE: "T"}, offline=False)
    checked = case(DEV, nothing_local, http=live, mode="live")
    assert checked.variant.reference_check == "verified" and live.urls == [SEQUENCE]
    saved = FakeHttp({SEQUENCE: "T"}, offline=True)
    assert case(DEV, nothing_local, http=saved).variant.reference_check == "verified"
    empty = FakeHttp({}, offline=True)
    unavailable = case(DEV, nothing_local, http=empty)
    assert unavailable.variant.reference_check == "unavailable"
    assert unavailable.input_provenance["reference_check"].startswith("unavailable")
    assert case(DEV, nothing_local).variant.reference_check == "unavailable"
    variant = parse_coordinates(DEV)
    assert check_reference(variant, config=nothing_local, http=FakeHttp({SEQUENCE: "C"}, offline=True))[0] == "mismatch"


# --- rsIDs ------------------------------------------------------------------------------------------------------------

def test_an_rsid_resolves_offline_from_a_saved_response_only(v9_cfg, tmp_path):
    http = saved_http(tmp_path, record(mapping(), mapping(chrom="CHR_HSCHR2_1_CTG7", start=1)))
    resolved = case("rs1427407", v9_cfg, http=http)
    assert resolved.variant.key == "GRCh38:2:60490908:T:G" and resolved.variant.rsid == "rs1427407"
    assert resolved.variant.input_text == "rs1427407"
    assert resolved.input_provenance["variant"] == "rsID rs1427407 resolved through Ensembl GRCh38"
    assert resolved.variant.reference_check == "verified"
    assert resolved.case_id == case(DEV, v9_cfg).case_id          # the same request, whatever form named the variant
    with pytest.raises(IntakeError, match="not in the HTTP cache"):
        case("rs1427408", v9_cfg, http=http)
    with pytest.raises(IntakeError, match="no HTTP client"):
        case("rs1427407", v9_cfg)


def test_a_multiallelic_rsid_needs_its_alternate_allele(v9_cfg, tmp_path):
    http = saved_http(tmp_path, record(mapping(alleles="T/A/G")))
    with pytest.raises(IntakeError, match=r"multiallelic.*A, G.*rs1427407:A"):
        case("rs1427407", v9_cfg, http=http)
    assert case("rs1427407:G", v9_cfg, http=http).variant.key == "GRCh38:2:60490908:T:G"
    assert case("rs1427407 T>A", v9_cfg, http=http).variant.alt == "A"
    with pytest.raises(IntakeError, match="not an alternate allele"):
        case("rs1427407:C", v9_cfg, http=http)
    with pytest.raises(IntakeError, match="reference allele of rs1427407 is T"):
        case("rs1427407 G>A", v9_cfg, http=http)


@pytest.mark.parametrize("data, why", [
    (record(mapping(), mapping(start=60490999)), "maps to 2 GRCh38 places"),
    (record(mapping(start=242193530)), "past the end of chromosome 2"),
    (record(mapping(strand=-1)), "minus strand"),
    (record(mapping(alleles="-/T")), "insertion or deletion"),
    (record(mapping(assembly="GRCh37")), "no GRCh38 mapping"),
])
def test_ambiguous_rsid_records_are_refused(v9_cfg, tmp_path, data, why):
    with pytest.raises(IntakeError, match=why):
        case("rs1427407", v9_cfg, http=saved_http(tmp_path, data))


# --- origin, disease and context --------------------------------------------------------------------------------------

def test_origin_is_kept_as_supplied_never_inferred(v9_cfg, tmp_path):
    # Even a record listing a somatic (COSMIC) synonym does not make the origin somatic: intake keeps what was given.
    http = saved_http(tmp_path, {**record(), "synonyms": ["COSV12345678"], "evidence": ["Cited"]})
    unknown = case("rs1427407", v9_cfg, http=http)
    assert unknown.origin == "unknown"
    assert "never inferred" in unknown.input_provenance["origin"]
    supplied = case(DEV, v9_cfg, origin="somatic")
    assert supplied.origin == "somatic" and supplied.input_provenance["origin"] == "supplied"


def test_bracketed_text_and_context_notes_are_removed(v9_cfg):
    c = case(DEV, v9_cfg, disease=["Obesity (FTO)", "none", " obesity ", "Anaemia [beta-globin locus"],
             context=["GTEx:Adipose - Subcutaneous (proxy for preadipocytes)", "DepMap:ACH-000739 (HepG2)", "none"])
    assert c.supplied_disease == ["Obesity", "Anaemia"]
    assert [s.label for s in c.supplied_context] == ["GTEx:Adipose - Subcutaneous", "DepMap:ACH-000739"]
    assert all(s.source == "supplied" for s in c.supplied_context)
    assert c.supplied_context[1].biosample == "HepG2" and c.supplied_context[1].biosample_kind == "cell_line"
    text = c.model_dump_json()
    assert "FTO" not in text and "proxy for" not in text and "beta-globin" not in text
    assert c.input_provenance["disease"] == "supplied" and c.input_provenance["context"] == "supplied"
    bare = case(DEV, v9_cfg)
    assert bare.input_provenance["disease"] == "not supplied" and bare.input_provenance["context"] == "not supplied"


def test_a_caller_cannot_overwrite_what_intake_checked(v9_cfg):
    c = case(DEV, v9_cfg, provenance={"reference_check": "verified by hand", "request": "command line"})
    assert c.input_provenance["request"] == "command line"
    assert c.input_provenance["reference_check"] == "verified: GRCh38 has T at 2:60490908"
    assert set(c.input_provenance) == PROVENANCE_KEYS | {"request"}
    assert set(case(DEV, v9_cfg).input_provenance) == PROVENANCE_KEYS      # a request without notes adds none


def test_the_case_does_not_depend_on_cache_state(v9_cfg, tmp_path):
    """A replay rebuilds the case from the saved request, and its notes reach every packet: whether Ensembl answered
    live or from a saved response, and which source checked the reference (a 21-mer may be precomputed after the live
    run), must not change it."""
    nothing_local = config_with(v9_cfg, db=tmp_path / "absent.sqlite", genome=tmp_path / "absent.fa")
    only_21mer = config_with(v9_cfg, db=v9_cfg.path("cache", "db"), genome=tmp_path / "absent.fa")
    by_21mer = case(DEV, only_21mer)
    by_live_ensembl = case(DEV, nothing_local, http=FakeHttp({SEQUENCE: "T"}, offline=False), mode="live")
    by_saved_ensembl = case(DEV, nothing_local, http=FakeHttp({SEQUENCE: "T"}, offline=True))
    assert by_21mer == by_live_ensembl == by_saved_ensembl
    live = case("rs1427407", only_21mer, http=FakeHttp({VARIATION: record()}, offline=False), mode="live")
    saved = case("rs1427407", only_21mer, http=saved_http(tmp_path, record()))
    assert live == saved and live.variant.rsid == "rs1427407"
