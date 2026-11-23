"""Fine-map one GWAS window and colocalise it with every gene of one eQTL dataset. No language model is called.

    python scripts/statgen_locus.py --gwas GCST90239658 --eqtl QTS000015/QTD000266 --chrom 1 --pos 109274968 \\
        --window 100000 --genes SORT1 PSRC1 CELSR2 --focus-name rs12740374 \\
        --gwas-label "LDL cholesterol GWAS (GCST90239658)" --eqtl-label "liver (GTEx)" \\
        --out runs/statgen_sort1_<date>

What it does (src/variant2mechanism/statgen): reads the window of the GWAS Catalog's harmonised file and of the
eQTL Catalogue dataset by tabix over HTTPS, matches the alleles, fine-maps the GWAS under one causal variant, and
runs coloc for each gene the eQTL dataset tests in the window. It writes result.json (every number and setting),
summary.md (the table a person reads) and figure.png (the GWAS and the genes named with --genes, stacked).

The first run fetches each file's index (about 2 MB) and the two windows, pausing between requests as EBI asks;
everything fetched is kept in cache/statgen, so a second run makes no request. --offline reads the cache only.
Nothing is written into an existing --out folder.
"""

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from variant2mechanism.statgen import locus, plot, sumstats  # noqa: E402

HGNC = ROOT / "data" / "reference" / "hgnc" / "hgnc_complete_set.txt"


def markdown(result: dict, args: argparse.Namespace, requests: list[str]) -> str:
    g, s = result["gwas"], result["settings"]
    start, end = args.pos - args.window, args.pos + args.window
    lines = [f"# {args.gwas} against {args.eqtl}, chr{args.chrom}:{start:,}-{end:,}", "",
             f"GWAS: {args.gwas_label}. eQTL: {args.eqtl_label}. Variant of interest: "
             f"{args.focus_name or args.pos} (chr{args.chrom}:{args.pos:,}).", "",
             f"Settings: priors p1 {s['p1']:g}, p2 {s['p2']:g}, p12 {s['p12']:g}; both traits quantitative; "
             f"credible sets at {s['coverage']:.0%}; a gene needs {s['min_variants']} shared variants.", "",
             "## The GWAS alone, if the window holds one causal variant", "",
             f"{g['variants']:,} variants. The {s['coverage']:.0%} credible set has {len(g['credible_set'])} "
             "variant(s):", "", "| Variant | Position | z | Posterior probability |", "|---|---|---|---|"]
    lines += [f"| {v['rsid'] or '-'} | {v['pos']:,} | {v['z']:.1f} | {v['pp']:.3f} |" for v in g["credible_set"][:15]]
    if g["focus"]:
        f = g["focus"]
        lines += ["", f"The variant of interest: effect {f['beta']:+.4f} (z {f['z']:.1f}) for allele "
                      f"{f['effect_allele']}, posterior probability {f['pp']:.3f}; "
                      f"{'in' if f['in_credible_set'] else 'not in'} the credible set."]
    lines += ["", "## Each gene's expression against the GWAS signal", "",
              "PP.H3: both traits have a causal variant here, and they differ. PP.H4: they share one.", "",
              "| Gene | Shared variants | PP.H3 | PP.H4 | Variant with most of H4 | Its share | "
              "At the variant of interest: GWAS z, expression z (same allele) |", "|---|---|---|---|---|---|---|"]
    for gene in result["genes"]:
        top, f = gene["shared_variant"], gene["focus"]
        both = f"{f['z_gwas']:+.1f}, {f['z_eqtl']:+.1f} ({f['alt']})" if f else "not tested for this gene"
        # which variant is shared is only a question when the traits probably share one
        which = (f"{top['rsid'] or top['pos']} | {top['share_of_h4']:.2f}" if gene["PP.H4"] >= 0.5 else "- | -")
        lines.append(f"| {gene['symbol']} | {gene['variants']:,} | {gene['PP.H3']:.3f} | {gene['PP.H4']:.3f} | "
                     f"{which} | {both} |")
    if result["skipped"]:
        lines += ["", f"{len(result['skipped'])} gene(s) were not compared (too few shared variants): "
                      + ", ".join(x["symbol"] for x in result["skipped"]) + "."]
    lines += ["", "## How far the answer rests on the prior", "",
              "PP.H4 as the prior probability that a variant is causal for both traits (p12) is changed:", "",
              "| Gene | " + " | ".join(f"p12 {row['p12']:g}" for row in result["genes"][0]["sensitivity"]) + " |"
              if result["genes"] else "", "|---|" + "---|" * 5 if result["genes"] else ""]
    for name in args.genes:
        gene = next((x for x in result["genes"] if name in (x["symbol"], x["gene"])), None)
        if gene:
            lines.append(f"| {gene['symbol']} | " + " | ".join(f"{row['PP.H4']:.3f}" for row in gene["sensitivity"])
                         + " |")
    lines += ["", "## What was asked of the server", "",
              *([f"- {r}" for r in requests] or ["Nothing: every table came from the cache."]), ""]
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--gwas", required=True, help="a GWAS Catalog study accession with harmonised statistics")
    parser.add_argument("--eqtl", required=True, help="an eQTL Catalogue dataset as STUDY/DATASET (QTS.../QTD...)")
    parser.add_argument("--chrom", required=True)
    parser.add_argument("--pos", type=int, required=True, help="the variant of interest (GRCh38): the window's centre")
    parser.add_argument("--window", type=int, default=100_000, help="bases on each side (default 100,000)")
    parser.add_argument("--genes", nargs="*", default=[], help="genes to draw, by symbol or Ensembl id")
    parser.add_argument("--focus-name", default=None)
    parser.add_argument("--gwas-label", default=None)
    parser.add_argument("--eqtl-label", default=None)
    parser.add_argument("--p12", type=float, default=locus.DEFAULTS.p12)
    parser.add_argument("--out", required=True, help="a new folder for result.json, summary.md and figure.png")
    parser.add_argument("--cache", default="cache/statgen")
    parser.add_argument("--offline", action="store_true", help="read the cache only")
    args = parser.parse_args()
    out = (ROOT / args.out).resolve()
    if out.exists():
        print(f"refused: {out} already exists; choose a new folder", file=sys.stderr)
        return 2
    args.gwas_label = args.gwas_label or f"GWAS {args.gwas}"
    args.eqtl_label = args.eqtl_label or args.eqtl
    study, _, dataset = args.eqtl.partition("/")
    reader = sumstats.WindowReader((ROOT / args.cache).resolve(), offline=args.offline)
    start, end = max(1, args.pos - args.window), args.pos + args.window
    try:
        gwas = sumstats.gwas_frame(reader.window(sumstats.gwas_catalog_url(args.gwas), args.chrom, start, end))
        eqtl = sumstats.eqtl_frame(reader.window(sumstats.eqtl_catalogue_url(study, dataset), args.chrom, start, end))
    except sumstats.CacheMiss as miss:
        print(f"refused: {miss}", file=sys.stderr)
        return 2
    symbols = locus.symbols_from_hgnc(str(HGNC))
    result = locus.analyse(gwas, eqtl, locus.Settings(p12=args.p12), focus=args.pos, symbols=symbols)
    out.mkdir(parents=True)
    record = {"gwas": args.gwas, "eqtl": args.eqtl, "chrom": args.chrom, "start": start, "end": end,
              "requests": reader.requests, **locus.summary(result)}
    (out / "result.json").write_text(json.dumps(record, indent=1))
    (out / "summary.md").write_text(markdown(result, args, reader.requests))
    drawn = [g["gene"] for name in args.genes for g in result["genes"] if name in (g["symbol"], g["gene"])]
    plot.regional(result, drawn, out / "figure.png", chrom=args.chrom, gwas_label=args.gwas_label,
                  eqtl_label=args.eqtl_label, focus_label=args.focus_name)
    best = result["genes"][:5]
    print(f"{len(gwas):,} GWAS variants, {eqtl['gene'].nunique()} genes; {len(reader.requests)} request(s). "
          + "; ".join(f"{g['symbol']} PP.H4 {g['PP.H4']:.3f}" for g in best))
    print(f"see {out / 'summary.md'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
