"""Record the context-tool fixtures: run each tool once live into tests/fixtures/http (spec 2, section 11).

Run: uv run python scripts/record_fixtures.py [--refresh]   (records what is missing; --refresh re-records all)
"""

import sys
from pathlib import Path

from variant2mechanism.context.base import Case
from variant2mechanism.context.catalog import LOCAL_TOOLS
from variant2mechanism.context.http import Http
from variant2mechanism.context.occupancy import fetch
from variant2mechanism.qbic.variants import Variant

FIXTURES = Path(__file__).resolve().parents[1] / "tests" / "fixtures" / "http"

CALLS = [
    ("rs6983267", Case(Variant.make("chr8", 127401060, "G", "T"), "Colorectal cancer", rsid="rs6983267"), [
        ("variant_annotation", {}), ("nearest_genes", {}), ("ccre_lookup", {}), ("gwas_lookup", {}),
        ("finemap_lookup", {}), ("literature_search", {"query": 'rs6983267 AND POU5F1B AND "colorectal cancer"'}),
        ("chip_peaks", {"tf": "TCF7L2", "biosample": "HCT116"}), ("eqtl_lookup", {"tissue": "Colon"}),
        ("gene_disease", {"gene": "MYC"}),
        # negative answers: tested in a tissue with no eQTL, a gene with no association, a search with no hits
        ("eqtl_lookup", {"tissue": "Liver"}), ("gene_disease", {"gene": "OR4F5", "ensembl_id": "ENSG00000186092"}),
        ("literature_search", {"query": 'rs6983267 AND "qzxv no such term"'}),
    ]),
    ("tert_c228t", Case(Variant.make("chr5", 1295113, "G", "A"), "Glioblastoma", origin="somatic"), [
        ("variant_annotation", {}), ("nearest_genes", {}), ("ccre_lookup", {}),
        ("literature_search", {"query": 'TERT AND promoter AND C228T AND GABPA'}),
        ("chip_peaks", {"tf": "GABPA"}), ("eqtl_lookup", {}),          # a somatic hotspot GTEx never genotyped
    ]),
    # controls: no GWAS association, no credible set, a variant outside any cCRE, a variant Open Targets lacks
    ("rs13078086", Case(Variant.make("chr3", 191441666, "T", "G"), "Colorectal cancer", rsid="rs13078086"), [
        ("gwas_lookup", {}), ("finemap_lookup", {}), ("ccre_lookup", {}),
    ]),
    ("rs7001688", Case(Variant.make("chr8", 57573391, "G", "T"), "LDL cholesterol", rsid="rs7001688"), [
        ("finemap_lookup", {}),
    ]),
]


# Occupancy (spec 3): ChIP peaks over these gold-set variants, and the ENCODE experiment list (recorded once).
OCCUPANCY = ["tert_c228t", "tert_c250t", "rs6983267", "rs4784227", "rs339331", "rs2168101", "rs12740374", "rs1421085",
             "rs642961", "rs13078086", "rs11629191", "rs7001688"]


def record_occupancy(http):
    from variant2mechanism.evaluation.gold import load_gold
    from variant2mechanism.qbic.registry import get_registry
    gold = {r["case_id"]: r for r in load_gold().to_dict("records")}
    reg = get_registry()
    for cid in OCCUPANCY:
        r = gold[cid]
        case = Case(Variant.make(r["chrom"], int(r["pos_grch38"]), r["ref"], r["alt"]), r["disease_or_trait"],
                    expression_context=r["expression_context"], http=http)
        occ, err = fetch(case, reg)
        print(f"{cid:11} occupancy {'error ' + err.summary[:80] if err else f'{len(occ.peaks)} peaks'}")


def main():
    http = Http(FIXTURES, refresh="--refresh" in sys.argv)
    record_occupancy(http)
    for case_id, case, calls in CALLS:
        case.http = http
        for name, args in calls:
            r = LOCAL_TOOLS[name](case, **args)
            print(f"{case_id:11} {name:18} {r.status:15} {r.summary.splitlines()[0][:100]}")


if __name__ == "__main__":
    main()
