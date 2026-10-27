# TERT promoter C250T and Glioblastoma, melanoma, bladder

Configuration `full`, masked mode, seed 0. Models: generator openai/gpt-6-luna, critic openai/gpt-6-luna, summariser openai/gpt-6-luna. Cost $0.02 over 12 model calls; 256 s.

Variant `chr5:1295135:G>A` (somatic); expression context: DepMap:subtype=Glioblastoma (median of 54 lines).

## QBiC-SELEX screen (occupancy first)

Occupied candidates: GABPA (bound elsewhere, z 167.5); KLF12 (bound elsewhere, z -15.38); NR2C1 (bound elsewhere, z 15.31); TGIF2 (bound elsewhere, z -12.19); ZNF143 (bound elsewhere, z -11.71); ZBTB7A (bound elsewhere, z -10.91); SP2 (bound elsewhere, z -9.83); EGR1 (bound elsewhere, z -8.0); BHLHE40 (bound elsewhere, z -7.34); E2F4 (bound elsewhere, z -5.4). Occupancy unknown: ETV2 (z 167.5); ETV3 (z 167.5); FLI1 (z 167.5); ZNF92 (z -33.21); EBF4 (z -24.35). Diagnostic, not shown to the model: 477 of 997 models pass Bonferroni.

## Ranked chains

### 1. H0: No TF-mediated effect of this variant (p = 0.84)

Null chain: no TF-mediated effect of this variant.

Predictions: A controlled comparison of the G and A alleles will show no reproducible TF-dependent regulatory effect in an appropriate glioblastoma context.; Any disease association, if present, may reflect another variant or process rather than this base.

Falsified if: A controlled edit of this base reproducibly changes TF-dependent regulation of a relevant gene in an appropriate cellular context.

### 2. H3: Possible ZNF143-associated effect at the TERT promoter (p = 0.08)

TF ZNF143 (QBiC-SELEX coverage own_model), ref allele binds more; element The variant lies in a promoter-like cCRE with active-chromatin marks reported among ENCODE biosample maxima; activity in glioblastoma is not established.; gene TERT is immediately adjacent and a plausible target, but regulation of TERT by this element is unproven.; cell type ZNF143 is expressed in the glioblastoma DepMap context, but its reported overlapping peak is from GM12878 and glioblastoma occupancy is not shown..

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | ZNF143's own QBiC-SELEX model predicts stronger ref binding, making this a more TF-specific in-vitro prediction than the mapped models for GABPA and TGIF2; the reported ZNF143 peak is from GM12878, so occupancy in glioblastoma remains unestablished. | weak | [E04](#e04), [E14](#e14), [E21](#e21), [E34](#e34) |
| element | The variant is within a promoter-like cCRE with active-chromatin marks among ENCODE biosample maxima, but glioblastoma-specific activity is not established. | supported | [E03](#e03) |
| gene | TERT is the nearest gene and the variant is annotated upstream of it, but this does not establish that the cCRE regulates TERT; TERT is not broadly essential in the reported CNS/Brain lines. | weak | [E01](#e01), [E02](#e02), [E39](#e39) |
| cell_type | ZNF143 is expressed in the glioblastoma DepMap context, but its reported overlapping peak is from GM12878, not a matching glioblastoma biosample. | supported | [E14](#e14), [E21](#e21), [E34](#e34) |
| phenotype | TERT promoter alterations are relevant to melanoma and glioblastoma, but the supplied evidence does not connect this variant to TERT regulation or any listed disease, and the exact-variant literature search returned no hits. | weak | [E15a](#e15a), [E15e](#e15e), [E15h](#e15h), [E38](#e38) |

Predictions: If ZNF143 occupies this site in glioblastoma cells, allele-specific binding should favor G over A; the in-vitro result does not establish occupancy or downstream activity.; A regulatory effect attributed to ZNF143 should depend on both the allele and ZNF143; the direction of any TERT expression change is unknown.; A reproducible effect dependent on GABPA or TGIF2 rather than ZNF143 would favor H1 or H2.

Falsified if: With ZNF143 occupancy confirmed in an appropriate glioblastoma context, sensitive allele-specific assays show no G-over-A binding difference.; A controlled endogenous edit shows no ZNF143-dependent regulatory effect despite confirmed occupancy and an adequately sensitive assay.

### 3. H1: Possible GABPA-associated effect at the TERT promoter (p = 0.04)

TF GABPA (QBiC-SELEX coverage own_model), alt allele binds more; element The variant lies in a promoter-like cCRE with active-chromatin marks reported among ENCODE biosample maxima; activity in glioblastoma is not established.; gene TERT is immediately adjacent and a plausible target, but regulation of TERT by this element is unproven.; cell type GABPA is expressed in the glioblastoma DepMap context, but its reported overlapping peaks are from other biosamples and glioblastoma occupancy is not shown..

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The QBiC-SELEX result predicts stronger alt binding from a model mapped to ETV5, not a GABPA-specific model; GABPA has overlapping peaks only in other biosamples, so GABPA occupancy and an allelic effect in glioblastoma remain uncertain. | weak | [E04](#e04), [E11](#e11), [E17](#e17), [E32](#e32) |
| element | The variant is within a promoter-like cCRE with active-chromatin marks among ENCODE biosample maxima, but glioblastoma-specific activity is not established. | supported | [E03](#e03) |
| gene | TERT is the nearest gene and the variant is annotated upstream of it, but this does not establish that the cCRE regulates TERT; no significant brain-cortex eQTL was reported, and TERT is not broadly essential in the reported CNS/Brain lines. | weak | [E01](#e01), [E02](#e02), [E35](#e35), [E39](#e39) |
| cell_type | GABPA is expressed in the glioblastoma DepMap context, but the reported overlapping peaks are from HepG2 and SK-N-SH, not a matching glioblastoma biosample. | supported | [E11](#e11), [E17](#e17), [E32](#e32) |
| phenotype | TERT promoter alterations are relevant to melanoma and glioblastoma, but the supplied evidence does not connect this variant to TERT regulation or any listed disease, and the exact-variant literature search returned no hits. | weak | [E15a](#e15a), [E15e](#e15e), [E15h](#e15h), [E38](#e38) |

Predictions: If GABPA occupies this site in glioblastoma cells, allele-specific binding should favor A over G; the available in-vitro result does not establish such occupancy or a GABPA-specific effect.; A regulatory effect attributed to GABPA should depend on both the allele and GABPA; the direction of any TERT expression change is unknown.; A reproducible effect dependent on ZNF143 or TGIF2 rather than GABPA would favor H3 or H2.

Falsified if: With GABPA occupancy confirmed in an appropriate glioblastoma context, sensitive allele-specific assays show no A-over-G binding difference.; A controlled endogenous edit shows no GABPA-dependent regulatory effect despite confirmed occupancy and an adequately sensitive assay.

### 4. H2: Possible TGIF2-associated effect at the TERT promoter (p = 0.04)

TF TGIF2 (QBiC-SELEX coverage own_model), ref allele binds more; element The variant lies in a promoter-like cCRE with active-chromatin marks reported among ENCODE biosample maxima; activity in glioblastoma is not established.; gene TERT is immediately adjacent and a plausible target, but regulation of TERT by this element is unproven.; cell type TGIF2 is expressed in the glioblastoma DepMap context, but its reported overlapping peak is from HepG2 and glioblastoma occupancy is not shown..

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The QBiC-SELEX result predicts stronger ref binding from a model mapped to PKNOX2, not a TGIF2-specific model; the reported TGIF2 peak is from HepG2, so occupancy and an allelic effect in glioblastoma remain uncertain. | weak | [E04](#e04), [E20](#e20), [E33](#e33) |
| element | The variant is within a promoter-like cCRE with active-chromatin marks among ENCODE biosample maxima, but glioblastoma-specific activity is not established. | supported | [E03](#e03) |
| gene | TERT is the nearest gene and the variant is annotated upstream of it, but this does not establish that the cCRE regulates TERT; no significant sun-exposed-skin eQTL was reported, and TERT is not broadly essential in the reported CNS/Brain lines. | weak | [E01](#e01), [E02](#e02), [E36](#e36), [E39](#e39) |
| cell_type | TGIF2 is expressed in the glioblastoma DepMap context, but its reported overlapping peak is from HepG2, not a matching glioblastoma biosample. | supported | [E20](#e20), [E33](#e33) |
| phenotype | TERT promoter alterations are relevant to melanoma and glioblastoma, but the supplied evidence does not connect this variant to TERT regulation or any listed disease, and the exact-variant literature search returned no hits. | weak | [E15a](#e15a), [E15e](#e15e), [E15h](#e15h), [E38](#e38) |

Predictions: If TGIF2 occupies this site in glioblastoma cells, allele-specific binding should favor G over A; the available in-vitro result does not establish such occupancy or a TGIF2-specific effect.; A regulatory effect attributed to TGIF2 should depend on both the allele and TGIF2; the direction of any TERT expression change is unknown.; A reproducible effect dependent on GABPA or ZNF143 rather than TGIF2 would favor H1 or H3.

Falsified if: With TGIF2 occupancy confirmed in an appropriate glioblastoma context, sensitive allele-specific assays show no G-over-A binding difference.; A controlled endogenous edit shows no TGIF2-dependent regulatory effect despite confirmed occupancy and an adequately sensitive assay.

## Prediction matrix

| Test | Cost | Separates top two | H0 | H3 | H1 | H2 |
| --- | --- | --- | --- | --- | --- | --- |
| Paired G- and A-allele reporter assay in a glioblastoma line, with and without ZNF143 depletion; include GABPA and TGIF2 depletion arms if feasible. | low | yes | No reproducible allele-dependent, TF-dependent reporter difference. | A reporter difference between alleles that is reduced by ZNF143 depletion; activity direction is not specified. | A reporter difference between alleles that is reduced by GABPA depletion; activity direction is not specified. | A reporter difference between alleles that is reduced by TGIF2 depletion; activity direction is not specified. |
| ZNF143 CUT&RUN or ChIP in glioblastoma cells followed by allele-specific occupancy measurement in heterozygous cells. | medium | yes | No reproducible occupancy over the site or no allele-specific occupancy. | ZNF143 occupancy with greater binding to G than A is predicted if the factor occupies the site. | ZNF143 occupancy is not specifically predicted; a GABPA-focused occupancy test would be more relevant. | ZNF143 occupancy is not specifically predicted; a TGIF2-focused occupancy test would be more relevant. |
| Endogenous G-to-A base editing in glioblastoma cells, with and without ZNF143 depletion, followed by TERT expression and local regulatory readouts. | high | yes | No reproducible allele-dependent, ZNF143-dependent change in TERT or local regulatory readouts. | An allele-dependent regulatory change should be reduced by ZNF143 depletion; TERT expression direction is unknown. | Any effect should depend on GABPA rather than specifically on ZNF143; TERT expression direction is unknown. | Any effect should depend on TGIF2 rather than specifically on ZNF143; TERT expression direction is unknown. |

## Next experiment

Run a paired G/A-allele reporter assay in a glioblastoma line with and without ZNF143 depletion. It is the cheapest proposed test that distinguishes the leading null hypothesis from H3; a positive result would need endogenous validation.

## Refinement rounds

Stopped: round limit (3).

### Round 1

- chip_peaks({"tf": "GABPA", "biosample": "glioblastoma"}) for H1.binding, ran as [E32](#e32). Expected: If ENCODE reports a GABPA peak overlapping the variant in a glioblastoma biosample, H1.binding gains relevant-context occupancy support and H1 rises; if none is found, the binding claim remains weak and H1 falls.
- chip_peaks({"tf": "TGIF2", "biosample": "glioblastoma"}) for H2.binding, ran as [E33](#e33). Expected: If a glioblastoma peak overlaps the variant, H2.binding gains relevant-context occupancy support and H2 rises; if none is found, its HepG2-only occupancy and mapped-model prediction remain weak support, lowering H2.
- chip_peaks({"tf": "ZNF143", "biosample": "glioblastoma"}) for H3.binding, ran as [E34](#e34). Expected: If a glioblastoma peak overlaps the variant, H3.binding gains relevant-context occupancy support and H3 rises; if none is found, the GM12878-only occupancy remains weak support, lowering H3.

- Result of chip_peaks GABPA in glioblastoma (E32): No overlapping GABPA peak is reported in a matching glioblastoma biosample; the result notes that this may reflect lack of a GABPA experiment in that context. (as expected: yes)
- Result of chip_peaks TGIF2 in glioblastoma (E33): No overlapping TGIF2 peak is reported in a matching glioblastoma biosample; the reported peak is from HepG2, and absence may reflect lack of a matching experiment. (as expected: yes)
- Result of chip_peaks ZNF143 in glioblastoma (E34): No overlapping ZNF143 peak is reported in a matching glioblastoma biosample; the reported peak is from GM12878, and absence may reflect lack of a matching experiment. (as expected: yes)

Chains after revision: null 0.56; GABPA 0.19; ZNF143 0.14; TGIF2 0.11. Link grades changed: H1.cell_type: weak → supported, H1.phenotype: weak → missing, H2.cell_type: weak → supported, H2.phenotype: weak → missing, H3.cell_type: weak → supported, H3.phenotype: weak → missing.

### Round 2

- eqtl_lookup({"tissue": "Brain - Cortex"}) for H1.gene, ran as [E35](#e35). Expected: If the variant is associated with TERT expression in brain cortex, the variant-to-gene link gains evidence beyond proximity and H1 rises modestly; no association leaves that link weak.
- eqtl_lookup({"tissue": "Skin - Sun Exposed"}) for H2.gene, ran as [E36](#e36). Expected: A variant-associated TERT eQTL in sun-exposed skin would add evidence for a variant-to-gene link relevant to melanoma, without proving a tumor-specific effect; no association leaves the link weak.
- gene_disease({"gene": "TERT"}) for H1.phenotype, ran as [E37](#e37). Expected: If Open Targets reports disease-specific evidence linking TERT to glioblastoma, melanoma, or bladder cancer, the gene-level phenotype plausibility increases; it would not establish that this variant affects TERT or disease risk.

- Result of eqtl_lookup({"tissue": "Brain - Cortex"}) for H1.gene: E35 reports 0 significant GTEx v8 single-tissue eQTLs for this variant in Brain - Cortex. (as expected: yes)
- Result of eqtl_lookup({"tissue": "Skin - Sun Exposed"}) for H2.gene: E36 reports 0 significant GTEx v8 single-tissue eQTLs for this variant in Skin - Sun Exposed. (as expected: yes)
- Result of gene_disease({"gene": "TERT"}) for H1.phenotype: E37 reports that the Open Targets lookup failed and returned no disease match; this is not evidence that TERT lacks disease relevance. (as expected: unclear)

Chains after revision: null 0.75; ZNF143 0.11; GABPA 0.08; TGIF2 0.06. Link grades changed: none.

### Round 3

- literature_search({"query": "chr5:1295135 G>A TERT glioblastoma melanoma bladder"}) for H1.phenotype, ran as [E38](#e38). Expected: If the search finds a report linking this exact variant to altered TERT regulation or one of the listed diseases, H1.phenotype gains variant-specific support and H1 may rise relative to H2, H3, and H0; if it returns only general TERT-promoter literature, the phenotype link remains unsupported.
- gene_dependency({"gene": "TERT"}) for H1.phenotype, ran as [E39](#e39). Expected: If TERT shows a relevant glioblastoma-lineage dependency, this would support the biological relevance of TERT in that context, but would not establish that this variant regulates TERT or causes disease; little or no dependency would weaken the general target-gene rationale.

- Result of literature_search({"query":"chr5:1295135 G>A TERT glioblastoma melanoma bladder"}) for H1.phenotype: E38 reports zero hits for the exact-variant search; this supplies no variant-specific literature support. (as expected: yes)
- Result of gene_dependency({"gene":"TERT"}) for H1.phenotype: E39 reports a CNS/Brain-line median TERT CRISPR gene effect of -0.00, with 2% dependent, and 1% dependent across all lines; this weakens a broad dependency rationale but does not test whether the variant regulates TERT. (as expected: yes)

Chains after revision: null 0.84; ZNF143 0.08; GABPA 0.04; TGIF2 0.04. Link grades changed: H1.phenotype: missing → weak, H2.phenotype: missing → weak, H3.phenotype: missing → weak.

## Flags

- tool_failed: E37 gene_disease: Open Targets lookup failed: no disease matches 'Glioblastoma, melanoma, bladder'

Citation support: 1.00 of links cite only evidence that passed every check.

## Evidence

<a id="e01"></a>**E01** variant_annotation, Ensembl VEP (GRCh38) (https://rest.ensembl.org/vep/human/region/5:1295135-1295135:1/A?content-type=application/json&Conservation=1; retrieved 2026-10-25T17:26:00+00:00)

> Variant chr5:1295135:G>A (GRCh38), allele string G/A
> Known IDs: rs1561215364
> Most severe consequence: upstream_gene_variant
> Regulatory features: ENSR5_832QG promoter
> GERP conservation score at the site: -4.69
> Transcript consequences: TERT (upstream_gene_variant)

<a id="e02"></a>**E02** nearest_genes, Ensembl overlap (protein_coding) (https://rest.ensembl.org/overlap/region/human/5:295135-2295135?feature=gene;biotype=protein_coding;content-type=application/json; retrieved 2026-10-25T17:25:54+00:00)

> 23 protein-coding genes within 1000 kb of chr5:1295135:G>A, by distance to TSS:
> TERT: 0.0 kb from TSS (upstream, strand -1)
> CLPTM1L: 50.0 kb from TSS (downstream, strand -1)
> SLC6A18: 69.8 kb from TSS (downstream, strand +1)
> SLC6A19: 93.5 kb from TSS (downstream, strand +1)
> SLC12A7: 138.9 kb from TSS (upstream, strand -1)
> SLC6A3: 150.4 kb from TSS (downstream, strand -1)
> LPCAT1: 229.1 kb from TSS (downstream, strand -1)
> NKD2: 287.1 kb from TSS (downstream, strand +1)
> TRIP13: 402.3 kb from TSS (downstream, strand +1)
> BRD9: 402.3 kb from TSS (upstream, strand -1)

<a id="e03"></a>**E03** ccre_lookup, ENCODE v4 cCRE registry (ENCFF420VPZ) and SCREEN (https://screen-beta-api.wenglab.org/dataws/cre_table; retrieved 2026-10-25T17:25:50+00:00)

> The variant lies in cCRE EH38E3622530 (PLS: promoter-like), chr5:1294945-1295294.
> SCREEN: 3 cCREs within 500 bp (max z-score across ENCODE biosamples):
> EH38E3622530 PLS (contains the variant): DNase z 4.8, H3K27ac z 4.2, H3K4me3 z 4.5, CTCF z 2.0; nearby genes TERT, MIR4457, CLPTM1L
> EH38E3622531 pELS: DNase z 3.9, H3K27ac z 4.3, H3K4me3 z 4.4, CTCF z 2.8; nearby genes TERT, MIR4457, CLPTM1L
> EH38E3622529 pELS: DNase z 3.7, H3K27ac z 4.1, H3K4me3 z 4.6, CTCF z 2.0; nearby genes TERT, MIR4457, CLPTM1L
> Biosample-specific z-scores are not in this call; the values above are maxima over biosamples.

<a id="e04"></a>**E04** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> ENCODE TF ChIP-seq at chr5:1295135:G>A: 113 peaks contain the variant, from 47 factors in 22 biosamples. No ENCODE biosample matches the expression context, so no peak counts as bound here. cCRE class at the variant: PLS. Bound factors outside the TF model collection (co-factors, Pol II, and TFs with no binding model; signs of an active element, not TF candidates): ARID4A, BCL3, DMAP1, EZH2, EZH2phosphoT487, GABPB1, HDAC1, HNRNPK, IKZF1, KDM4A, LIN54, MAZ (+16 more). Bound, expressed TFs with a binding model: 18; listed one per row: MAX, JUN, BHLHE40, E2F4, EGR1, CTCF, GABPA, ZNF687, NR2C1, ZNF143; also bound: SP2, TGIF2, MNT, ZBTB7A, E2F5, ZBTB26, KLF12, ZNF48. Bound but below 1 TPM: ZFHX2. Assayed with no peak here: 0 TFs in the matching biosample, 554 only elsewhere; never assayed: 536.

<a id="e05"></a>**E05** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> MAX: bound elsewhere. 12 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: A549, HCT116, HepG2, Ishikawa, K562, NB4 (+1 more) (e.g. ENCSR000BLP). 58.6 TPM in DepMap:subtype=Glioblastoma (median of 54 lines), rank 48 of 1626 TFs.

<a id="e06"></a>**E06** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> JUN: bound elsewhere. 11 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: A549 (e.g. ENCSR022WVP). 91.65 TPM in DepMap:subtype=Glioblastoma (median of 54 lines), rank 16 of 1626 TFs.

<a id="e07"></a>**E07** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> BHLHE40: bound elsewhere. 2 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: GM12878 (e.g. ENCSR000DZJ). 68.33 TPM in DepMap:subtype=Glioblastoma (median of 54 lines), rank 33 of 1626 TFs.

<a id="e08"></a>**E08** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> E2F4: bound elsewhere. 2 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: GM12878, HepG2 (e.g. ENCSR000DYY). 58.31 TPM in DepMap:subtype=Glioblastoma (median of 54 lines), rank 49 of 1626 TFs.

<a id="e09"></a>**E09** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> EGR1: bound elsewhere. 2 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: HepG2, Ishikawa (e.g. ENCSR000BSQ). 28.32 TPM in DepMap:subtype=Glioblastoma (median of 54 lines), rank 151 of 1626 TFs.

<a id="e10"></a>**E10** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> CTCF: bound elsewhere. 2 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: DOHH2, endodermal cell (e.g. ENCSR084RDK). 26.45 TPM in DepMap:subtype=Glioblastoma (median of 54 lines), rank 163 of 1626 TFs.

<a id="e11"></a>**E11** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> GABPA: bound elsewhere. 2 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: HepG2, SK-N-SH (e.g. ENCSR000BJK). 15.52 TPM in DepMap:subtype=Glioblastoma (median of 54 lines), rank 303 of 1626 TFs.

<a id="e12"></a>**E12** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> ZNF687: bound elsewhere. 2 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: HepG2 (e.g. ENCSR647PSR). 10.74 TPM in DepMap:subtype=Glioblastoma (median of 54 lines), rank 436 of 1626 TFs.

<a id="e13"></a>**E13** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> NR2C1: bound elsewhere. 1 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: GM12878 (e.g. ENCSR784VIQ). 18.52 TPM in DepMap:subtype=Glioblastoma (median of 54 lines), rank 251 of 1626 TFs.

<a id="e14"></a>**E14** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> ZNF143: bound elsewhere. 1 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: GM12878 (e.g. ENCSR936XTK). 15.92 TPM in DepMap:subtype=Glioblastoma (median of 54 lines), rank 297 of 1626 TFs.

<a id="e15"></a>**E15** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TERT%20AND%20%28%22glioblastoma%22%20OR%20%22melanoma%22%20OR%20%22bladder%22%29&format=json&pageSize=8&resultType=core; retrieved 2026-10-25T11:57:36+00:00)

> Europe PMC: 23888 hits for 'TERT AND ("glioblastoma" OR "melanoma" OR "bladder")'; top 7 with PMIDs:
> PMID 41744838 (2026): Telomerase Activity in Melanoma: Impact on Cancer Cell Proliferation Kinetics, Tumor Progression, and Clinical Therapeutic Strategies-A Scoping Review.
> PMID 42577103 (2026): Familial melanoma: genetic, clinical, and dermoscopic insights and follow-up.
> PMID 42722679 (2026): Developing neoantigen cancer vaccines: where are we now?
> PMID 42741698 (2026): Melanoma of unknown primary with solitary lesions to the prostate and lung uncovered after simple prostatectomy.
> PMID 42804732 (2026): SNP rs[masked] potentially elevates the risk of glioblastoma development and leads to worse prognosis when in cis with mutant TERT promoter in a Japanese cohort.
> PMID 42807929 (2026): USP10 stabilizes FOXM1 through KAT5-mediated acetylation to suppress cell senescence and promote melanoma malignant progression.
> PMID 42859331 (2026): CDKN2A deletion associated with poor prognosis in patients with TERT promoter wild-type, IDH wild-type glioblastoma.

<a id="e15a"></a>**E15a** literature_search, Europe PMC abstract, PMID 41744838 (https://europepmc.org/article/MED/41744838; retrieved 2026-10-25T11:57:36+00:00)

> A major molecular feature of melanoma is abnormal telomerase activation; this is most often caused by telomerase reverse transcriptase (TERT) promoter mutations, which occur in 50-82% of cases and are the most common noncoding alteration in this cancer.

<a id="e15b"></a>**E15b** literature_search, Europe PMC abstract, PMID 41744838 (https://europepmc.org/article/MED/41744838; retrieved 2026-10-25T11:57:36+00:00)

> Conclusions: Understanding both telomere-dependent and -independent TERT functions is essential for developing effective biomarkers and therapies that overcome resistance and slow melanoma progression.

<a id="e15c"></a>**E15c** literature_search, Europe PMC abstract, PMID 42577103 (https://europepmc.org/article/MED/42577103; retrieved 2026-10-25T11:57:36+00:00)

> The genetic landscape of familial melanoma is heterogeneous.

<a id="e15d"></a>**E15d** literature_search, Europe PMC abstract, PMID 42577103 (https://europepmc.org/article/MED/42577103; retrieved 2026-10-25T11:57:36+00:00)

> CDKN2A and CDK4 mutations act through UV-dependent and cell cycle disruption pathways, while BAP1, POT1, and TERT mutations are considered UV-independent.

<a id="e15e"></a>**E15e** literature_search, Europe PMC abstract, PMID 42804732 (https://europepmc.org/article/MED/42804732; retrieved 2026-10-25T11:57:36+00:00)

> Mutations in the telomerase reverse transcriptase (TERT) promoter region (TPM), particularly C228T and C250T, are common in IDH-wildtype glioblastoma (GBM).

<a id="e15f"></a>**E15f** literature_search, Europe PMC abstract, PMID 42804732 (https://europepmc.org/article/MED/42804732; retrieved 2026-10-25T11:57:36+00:00)

> The rs[masked] C allele may increase GBM susceptibility and, when in cis with TPM, is associated with reduced TERT expression and poorer prognosis, underscoring its biological and clinical significance in TPM-mutant GBM.

<a id="e15g"></a>**E15g** literature_search, Europe PMC abstract, PMID 42807929 (https://europepmc.org/article/MED/42807929; retrieved 2026-10-25T11:57:36+00:00)

> Additionally, loss of either USP10 or FOXM1 suppresses the expression of the downstream target Telomerase reverse transcriptase (TERT), triggering cellular senescence.

<a id="e15h"></a>**E15h** literature_search, Europe PMC abstract, PMID 42859331 (https://europepmc.org/article/MED/42859331; retrieved 2026-10-25T11:57:36+00:00)

> TERT promoter (TERTp) mutations are among the most frequent molecular alterations in isocitrate dehydrogenase (IDH) wild-type glioblastoma (GBM), yet the molecular profiles and prognostic implications associated with TERTp status remain incompletely characterized.

<a id="e15i"></a>**E15i** literature_search, Europe PMC abstract, PMID 42859331 (https://europepmc.org/article/MED/42859331; retrieved 2026-10-25T11:57:36+00:00)

> The prognostic relevance of CDKN2A deletion may vary according to TERTp status, particularly for OS.

<a id="e16"></a>**E16** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> QBiC-SELEX screen of chr5:1295135:G>A, one line per TF, each with the TF's own or CIS-BP-mapped model of largest |z|. Candidates are TFs whose ENCODE ChIP-seq peaks contain the variant and that are expressed (DepMap subtype median Glioblastoma), bound here before bound elsewhere, then a strong site before a weak one, then by |z|; then expressed TFs ENCODE never assayed whose best model passes the gate (occupancy unknown). Shown: 10 of 18 occupied (14 with a strong site), 5 of 145 with unknown occupancy. Left out: 0 TFs assayed in the matching biosample and 554 assayed only elsewhere, none with a peak here; 1 bound but below 1 TPM. The gate (|z| > 4.05, Bonferroni over 997 models) marks a change QBiC-SELEX detects; it says nothing about occupancy. Effect > 0 means the alternate allele binds more strongly. In vitro binding only. Site strength is the better allele's best k-mer over the variant, as a percentile of the best model's k-mers; a strong site reaches the 97.5th. At a weak site the ChIP peak more likely reflects another site in the element.

<a id="e17"></a>**E17** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> GABPA (Ets, 18 models; QBiC-SELEX coverage: own model): best model ETV5_NA_TGCACT20NGA_ESAF_yang2017_1_3_6mer (a CIS-BP-mapped model of ETV5), z 167.5, effect 2.421: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 15.52 TPM, rank 303 of 1626 TFs in DepMap:subtype=Glioblastoma (median of 54 lines). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in HepG2, SK-N-SH, e.g. ENCSR000BJK. Best model's site strength: ref 94.8th, alt 99.9th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e18"></a>**E18** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> KLF12 (C2H2 ZF, 6 models; QBiC-SELEX coverage: own model): best model KLF5_eDBD_TAACGC40NGTG_KS_yin2017_0_4_7mer (a CIS-BP-mapped model of KLF5), z -15.38, effect -0.439: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 4.47 TPM, rank 787 of 1626 TFs in DepMap:subtype=Glioblastoma (median of 54 lines). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in HepG2, e.g. ENCSR552YWL. Best model's site strength: ref 99.9th, alt 98.9th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e19"></a>**E19** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> NR2C1 (Nuclear receptor, 29 models; QBiC-SELEX coverage: own model): best model RORC_NA_Lib1_NA_bhimsaria2023_0(3)_3_7mer (a CIS-BP-mapped model of RORC), z 15.31, effect 1.182: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 18.52 TPM, rank 251 of 1626 TFs in DepMap:subtype=Glioblastoma (median of 54 lines). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in GM12878, e.g. ENCSR784VIQ. Best model's site strength: ref 98.3th, alt 99.2th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e20"></a>**E20** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> TGIF2 (Homeodomain, 9 models; QBiC-SELEX coverage: own model): best model PKNOX2_eDBD_TAACGT40NGAT_KAN_yin2017_0_4_7mer (a CIS-BP-mapped model of PKNOX2), z -12.19, effect -1.113: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 10.31 TPM, rank 452 of 1626 TFs in DepMap:subtype=Glioblastoma (median of 54 lines). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in HepG2, e.g. ENCSR993LMB. Best model's site strength: ref 98.3th, alt 71.5th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e21"></a>**E21** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> ZNF143 (C2H2 ZF, 2 models; QBiC-SELEX coverage: own model): best model ZNF143_NA_TGCAAG20NCG_V_jolma2013_0_3_7mer (its own model), z -11.71, effect -0.649: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 15.92 TPM, rank 297 of 1626 TFs in DepMap:subtype=Glioblastoma (median of 54 lines). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in GM12878, e.g. ENCSR936XTK. Best model's site strength: ref 100.0th, alt 98.4th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e22"></a>**E22** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> ZBTB7A (C2H2 ZF, 1 model; QBiC-SELEX coverage: own model): best model ZBTB7A_eDBD_TTTGCT40NCGT_KR_yin2017_0_4_7mer (its own model), z -10.91, effect -0.707: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 8.49 TPM, rank 531 of 1626 TFs in DepMap:subtype=Glioblastoma (median of 54 lines). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in K562, e.g. ENCSR000BME. Best model's site strength: ref 99.9th, alt 99.9th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e23"></a>**E23** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> SP2 (C2H2 ZF, 1 model; QBiC-SELEX coverage: own model): best model SP2_eDBD_TCATGT40NCTG_KV_yin2017_0_4_7mer (its own model), z -9.83, effect -0.269: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 15.49 TPM, rank 305 of 1626 TFs in DepMap:subtype=Glioblastoma (median of 54 lines). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in HepG2, e.g. ENCSR946RZN. Best model's site strength: ref 100.0th, alt 99.7th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e24"></a>**E24** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> EGR1 (C2H2 ZF, 4 models; QBiC-SELEX coverage: own model): best model EGR3_NA_TCATGC20NGTA_ESZ_yang2017_0_4_7mer (a CIS-BP-mapped model of EGR3), z -8.0, effect -0.422: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 28.32 TPM, rank 151 of 1626 TFs in DepMap:subtype=Glioblastoma (median of 54 lines). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in HepG2, Ishikawa, e.g. ENCSR000BSQ. Best model's site strength: ref 99.8th, alt 99.7th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e25"></a>**E25** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> BHLHE40 (bHLH, 2 models; QBiC-SELEX coverage: own model): best model BHLHE40_eDBD_TTAGTG40NACC_KR_yin2017_0_3_7mer (its own model), z -7.34, effect -0.318: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 68.33 TPM, rank 33 of 1626 TFs in DepMap:subtype=Glioblastoma (median of 54 lines). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in GM12878, e.g. ENCSR000DZJ. Best model's site strength: ref 99.6th, alt 93.6th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e26"></a>**E26** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> E2F4 (E2F, 4 models; QBiC-SELEX coverage: own model): best model E2F3_NA_TTACAT20NACA_ESAF_yang2017_0_4_7mer (a CIS-BP-mapped model of E2F3), z -5.4, effect -0.455: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 58.31 TPM, rank 49 of 1626 TFs in DepMap:subtype=Glioblastoma (median of 54 lines). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in GM12878, HepG2, e.g. ENCSR000DYY. Best model's site strength: ref 99.5th, alt 99.4th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e27"></a>**E27** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> ETV2 (Ets, 18 models; QBiC-SELEX coverage: own model): best model ETV5_NA_TGCACT20NGA_ESAF_yang2017_1_3_6mer (a CIS-BP-mapped model of ETV5), z 167.5, effect 2.421: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 1.4 TPM, rank 1063 of 1626 TFs in DepMap:subtype=Glioblastoma (median of 54 lines). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 94.8th, alt 99.9th percentile of its k-mer coefficients.

<a id="e28"></a>**E28** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> ETV3 (Ets, 18 models; QBiC-SELEX coverage: own model): best model ETV5_NA_TGCACT20NGA_ESAF_yang2017_1_3_6mer (a CIS-BP-mapped model of ETV5), z 167.5, effect 2.421: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 8.69 TPM, rank 521 of 1626 TFs in DepMap:subtype=Glioblastoma (median of 54 lines). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 94.8th, alt 99.9th percentile of its k-mer coefficients.

<a id="e29"></a>**E29** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> FLI1 (Ets, 18 models; QBiC-SELEX coverage: own model): best model ETV5_NA_TGCACT20NGA_ESAF_yang2017_1_3_6mer (a CIS-BP-mapped model of ETV5), z 167.5, effect 2.421: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 4.71 TPM, rank 767 of 1626 TFs in DepMap:subtype=Glioblastoma (median of 54 lines). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 94.8th, alt 99.9th percentile of its k-mer coefficients.

<a id="e30"></a>**E30** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> ZNF92 (C2H2 ZF, 1 model; QBiC-SELEX coverage: own model): best model ZNF92_FL_TC40NAATCTC_YWIA_jolma2025_0_3_7mer (its own model), z -33.21, effect -0.623: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 9.63 TPM, rank 481 of 1626 TFs in DepMap:subtype=Glioblastoma (median of 54 lines). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 100.0th, alt 99.7th percentile of its k-mer coefficients.

<a id="e31"></a>**E31** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> EBF4 (EBF1, 2 models; QBiC-SELEX coverage: own model): best model EBF1_NA_TATAAG20NCG_AC_jolma2013_1_3_7mer (a CIS-BP-mapped model of EBF1), z -24.35, effect -0.646: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 2.58 TPM, rank 952 of 1626 TFs in DepMap:subtype=Glioblastoma (median of 54 lines). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 99.9th, alt 99.7th percentile of its k-mer coefficients.

<a id="e32"></a>**E32** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-25T17:27:26+00:00)

> No ENCODE GABPA ChIP-seq peak contains chr5:1295135:G>A in biosamples matching 'glioblastoma'. Absence can also mean no GABPA experiment in that biosample. In other biosamples, 2 GABPA peaks do contain the variant: HepG2, SK-N-SH (experiments ENCSR000BJK, ENCSR000BTG).

<a id="e33"></a>**E33** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-26T13:33:05+00:00)

> No ENCODE TGIF2 ChIP-seq peak contains chr5:1295135:G>A in biosamples matching 'glioblastoma'. Absence can also mean no TGIF2 experiment in that biosample. In other biosamples, 1 TGIF2 peaks do contain the variant: HepG2 (experiments ENCSR993LMB).

<a id="e34"></a>**E34** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-26T20:27:28+00:00)

> No ENCODE ZNF143 ChIP-seq peak contains chr5:1295135:G>A in biosamples matching 'glioblastoma'. Absence can also mean no ZNF143 experiment in that biosample. In other biosamples, 1 ZNF143 peaks do contain the variant: GM12878 (experiments ENCSR936XTK).

<a id="e35"></a>**E35** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr5_1295135_G_A_b38&datasetId=gtex_v8; retrieved 2026-10-26T20:17:52+00:00)

> 0 significant GTEx v8 single-tissue eQTLs for chr5_1295135_G_A_b38 in tissues matching 'Brain - Cortex'. NES is the effect of the alt allele (A) relative to ref (G).

<a id="e36"></a>**E36** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr5_1295135_G_A_b38&datasetId=gtex_v8; retrieved 2026-10-26T20:17:52+00:00)

> 0 significant GTEx v8 single-tissue eQTLs for chr5_1295135_G_A_b38 in tissues matching 'Skin - Sun Exposed'. NES is the effect of the alt allele (A) relative to ref (G).

<a id="e37"></a>**E37** gene_disease (failed), Open Targets (; retrieved local)

> Open Targets lookup failed: no disease matches 'Glioblastoma, melanoma, bladder'

<a id="e38"></a>**E38** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=chr5%3A1295135%20G%3EA%20TERT%20glioblastoma%20melanoma%20bladder&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T22:06:52+00:00)

> Europe PMC: 0 hits for 'chr5:1295135 G>A TERT glioblastoma melanoma bladder'; top 0 with PMIDs:

<a id="e39"></a>**E39** gene_dependency, DepMap CRISPRGeneEffect (Biomni copy) and CRISPRInferredCommonEssentials (Public 26Q3) (local files; retrieved local)

> DepMap CRISPR gene effect for TERT (0 = no effect, -1 = median common-essential; < -0.5 called dependent). CNS/Brain lineage, 50 lines: median -0.00, 2% dependent. All 1183 lines: median -0.02, 1% dependent.
