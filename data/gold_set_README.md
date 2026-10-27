# Gold set

Nine TF-mechanism cases, three random controls and three near-miss controls for scoring the variant-to-mechanism agent. Positions are
GRCh38 / hg38, one-based, plus strand. Every `ref` was checked against the
GRCh38 RefSeq chromosome (NCBI efetch) on 24 October 2026 and matches.

## Columns

- `pos_grch38`, `ref`, `alt` — plus-strand, one-based. Feed these straight to
  `qbic-selex predict -v <csv>` (its input columns are `chrom,pos,ref,alt`).
- `origin` — `somatic` or `germline`. Somatic cases skip the GWAS and
  fine-mapping tools; germline cases skip tumour recurrence.
- `causal_tf` / `tf_family` — the published answer. Scoring is per TF;
  `tf_family` is kept for the group-level diagnostic.
- `direction` — which allele gains or loses binding, in words, because the
  risk allele is not always the alt allele (see below).
- `expression_context`: the dataset and sample used for TF expression, as
  `DepMap:<ModelID> (<name>)`, `DepMap:subtype=<Oncotree subtype> (median ...)`,
  `GTEx:<tissue>`, or `none`, in which case the expression filter is skipped.
  Proxies are marked as such.
- `qbic_model` — model coverage in QBiC-SELEX 1.0.0 (Zenodo 23482275:
  997 primary + 243 secondary models), resolved by HGNC symbol through Tables
  S1, S5 and S6.
- `score_level` — `tf` where the causal TF has its own primary model, `mapped`
  where it is covered only through CIS-BP-mapped models of other TFs (Table S6),
  `not_in_coverage` where it has neither.

## Two traps worth knowing before writing the scorer

**Risk allele is not always the alt allele.** For rs339331, rs642961 and
rs6983267 the published risk allele is the GRCh38 reference. The scorer must
compare the predicted effect against `direction`, not assume
"alt = risk = gain".

**Published strand is not always the plus strand.** TERT C228T/C250T are
named on the minus strand (TERT's own orientation) and are G>A on the plus
strand. rs2168101 is published as G>T and is C>A on the plus strand. QBiC-SELEX
is sensitive to ref/alt orientation, so use the CSV values, not the names in
the papers.

## Model coverage (checked 25 October 2026)

TFs are resolved by HGNC symbol through Tables S1, S5 and S6, because 222
experiment labels differ from the HGNC symbol. TFAP2A, for example, has its own
model under the old label Tcfap2a, and CEBPA has its own model too.

- TCF7L2 has no model of its own but is covered through CIS-BP-mapped LEF1,
  TCF7 and TCF7L1 models (`mapped`).
- TAL1 and ARID5B have neither, so they are `not_in_coverage`. rs1421085 is the deliberate not-in-coverage case.
  rs1427407 (GATA1/TAL1, BCL11A) was removed on 25 Oct 2026: QBiC-SELEX's
  21-bp window ends one base before its GATA site and TAL1 is not in coverage.

Expression filtering works on CIS-BP groups: a group survives if any TF mapped
to it is expressed in the case's tissue or cell line, including a TF with no
model of its own (TCF7L2 itself).

## Still to add

- 2 binding-only controls: large predicted binding change, no allelic activity
  in the MPRA / SNP-SELEX benchmarks. Label is null.
- More random controls if wanted. Three are in the file (added 25 October
  2026, `label_class` `control_random`, `score_level` `control`): common SNVs
  (gnomAD v4 AF 0.17 to 0.46) from random genomic windows, with no GWAS Catalog
  association, no significant GTEx v8 eQTL and no Open Targets credible set
  with PIP above 0.1. Each borrows the disease and expression context of a real
  case (colorectal cancer, breast cancer, LDL cholesterol), so over-claiming is
  measured under the same question. Distance to TSS is only loosely matched
  (19.5 to 421 kb).
- Optional, 2 to 3 mutational-process cases: PLEKHS1 promoter hotspot (APOBEC
  passenger), DPH3 / SDHD promoter mutations (UV hotspots at ETS sites). Label
  is null or contested.

## Near-miss controls (added 26 October 2026)

`label_class` `control_near_miss`, `score_level` `control`, correct answer the null.
Each is a SNV inside the element of a famous case (the same ENCODE ChIP peaks
contain it), with no GWAS Catalog association, no significant GTEx v8 eQTL and
no Open Targets credible set with PIP above 0.1. Each takes its parent case's
disease and expression context, so a model working from memory is drawn to the
famous mechanism, while QBiC-SELEX can say whether this base changes the bound
TF's site.

| Variant | Parent | Distance | gnomAD v4 AF |
| --- | --- | --- | --- |
| rs73706717 (chr8:127401265 T>C) | rs6983267 | 205 bp | 0.024 |
| rs34768248 (chr5:1295601 G>A) | TERT C228T | 488 bp | 0.027 |
| rs56007086 (chr16:52565398 G>A) | rs4784227 | 122 bp | 0.049 |

All three are low-frequency: the common SNPs near these loci all carry
association or eQTL signals. At 1p13 (rs12740374) no SNP within 1.5 kb passed,
so 16q12 replaces it.
