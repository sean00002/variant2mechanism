import pytest

from variant2mechanism.qbic.variants import Variant, VariantError, parse, strand_precheck


@pytest.mark.parametrize("text", ["chr5:1295113:G>A", "chr5-1295113-G-A", "5:1295113 G>A", "5:1295113:g>a"])
def test_parse_forms(text):
    assert parse(text).key() == "chr5:1295113:G>A"


def test_normalisation():
    v = Variant.make("5", "1295113", "g", "a")
    assert (v.chrom, v.pos, v.ref, v.alt) == ("chr5", 1295113, "G", "A")
    assert Variant.make("chrX", 10, "A", "C").chrom_bare == "X"


@pytest.mark.parametrize("args", [("5", 10, "AT", "A"), ("5", 10, "A", "AT"), ("5", 10, "A", "A"),
                                  ("5", 0, "A", "C"), ("5", 10, "N", "C"), ("5", "x", "A", "C")])
def test_rejects_non_snvs(args):
    with pytest.raises(VariantError):
        Variant.make(*args)


def test_rejects_unparseable():
    with pytest.raises(VariantError, match="GRCh38"):
        parse("rs6983267")


def test_strand_hint():
    v = parse("chr5:1295113:C>T")
    msg = strand_precheck(v, fetch=lambda _: "G")
    assert msg == ("Alleles look like minus-strand notation. QBiC-SELEX needs plus-strand alleles: "
                   "use chr5:1295113 G>A.")
    assert strand_precheck(parse("chr5:1295113:G>A"), fetch=lambda _: "G") is None


def test_strand_check_unreachable_submits_anyway():
    def down(_):
        raise ConnectionError("no network")
    assert strand_precheck(parse("chr5:1295113:C>T"), fetch=down) is None
