# TERT promoter C250T and Glioblastoma, melanoma, bladder

Configuration `full`, masked mode, seed 0. Models: generator openai/gpt-6-luna, critic openai/gpt-6-luna, summariser openai/gpt-6-luna. Cost $0.01 over 7 model calls; 131 s.

Variant `chr5:1295135:G>A` (somatic); expression context: DepMap:subtype=Glioblastoma (median of 54 lines).

## QBiC-SELEX screen (occupancy first)

Occupied candidates: GABPA (bound elsewhere, z 167.5); KLF12 (bound elsewhere, z -15.38); NR2C1 (bound elsewhere, z 15.31); TGIF2 (bound elsewhere, z -12.19); ZNF143 (bound elsewhere, z -11.71); ZBTB7A (bound elsewhere, z -10.91); SP2 (bound elsewhere, z -9.83); EGR1 (bound elsewhere, z -8.0); BHLHE40 (bound elsewhere, z -7.34); E2F4 (bound elsewhere, z -5.4). Occupancy unknown: ETV2 (z 167.5); ETV3 (z 167.5); FLI1 (z 167.5); ZNF92 (z -33.21); EBF4 (z -24.35). Diagnostic, not shown to the model: 477 of 997 models pass Bonferroni.

## Ranked chains

### 1. H0: No TF-mediated effect of this variant (p = 0.46)

Null chain: no TF-mediated effect of this variant.

Predictions: The variant produces no reproducible TF-mediated regulatory effect in relevant cells; any disease association is absent, indirect, or due to another alteration.

Falsified if: Changing this single base reproducibly changes binding of an occupying TF and alters a relevant target gene's expression in an appropriate cellular context.

### 2. H1: GABPA-mediated increase in TERT promoter activity (p = 0.34)

TF GABPA (QBiC-SELEX coverage own_model), alt allele binds more; element The variant lies in a promoter-like cCRE with active-chromatin marks in some ENCODE biosamples; activity in glioblastoma is not established.; gene TERT is immediately adjacent to the variant and is a plausible target, but regulation of TERT by this element is not demonstrated.; cell type GABPA is expressed in the glioblastoma DepMap context, but its site-overlapping peaks are from other biosamples; glioblastoma occupancy is unestablished..

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | GABPA is a plausible ETS-family candidate: its own QBiC-SELEX model predicts stronger alt binding, as do several related ETS-family models. GABPA is expressed and has peaks over the site in other biosamples, but those peaks do not establish occupancy in glioblastoma; the shared ETS predictions also do not uniquely identify GABPA. | weak | [E04](#e04), [E11](#e11), [E17](#e17), [E34](#e34) |
| element | The variant falls within a promoter-like cCRE with active-chromatin marks in some ENCODE biosamples, without glioblastoma-specific confirmation. | supported | [E03](#e03) |
| gene | TERT is adjacent to the variant at its TSS and is a plausible target, but no supplied evidence directly links this element to TERT expression; no significant brain-cortex eQTL was reported. | weak | [E01](#e01), [E02](#e02), [E33](#e33) |
| cell_type | GABPA is expressed in the glioblastoma DepMap context, but the reported overlapping peaks are from other biosamples and do not establish occupancy in glioblastoma. | weak | [E04](#e04), [E11](#e11), [E17](#e17) |
| phenotype | TERT promoter alterations are relevant to cancer, but the evidence does not establish that this variant changes TERT activity or contributes to the listed diseases. | weak | [E15a](#e15a), [E15e](#e15e), [E15h](#e15h), [E32a](#e32a) |

Predictions: If GABPA occupies this site in glioblastoma, alt should show greater GABPA binding than ref.; If the extra GABPA binding activates this promoter, an alt construct or alt-edited allele should increase TERT transcription; this activity direction remains unproven.

Falsified if: A suitable glioblastoma assay finds no GABPA occupancy or no alt-over-ref binding difference at the site.; With GABPA occupancy and the predicted binding difference confirmed, changing ref to alt does not increase TERT expression or promoter activity.

### 3. H2: TGIF2-mediated regulation of the TERT promoter (p = 0.10)

TF TGIF2 (QBiC-SELEX coverage own_model), ref allele binds more; element The variant lies in a promoter-like cCRE with active-chromatin marks in some ENCODE biosamples; activity in glioblastoma is not established.; gene TERT is adjacent to the variant and is a plausible target, but regulation by this element is not demonstrated.; cell type TGIF2 is expressed in the glioblastoma DepMap context, but its site-overlapping peak is from HepG2; occupancy in glioblastoma is unestablished..

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | QBiC-SELEX predicts stronger ref binding for TGIF2 using a CIS-BP-mapped PKNOX2 model. A TGIF2 peak over the site was observed in another biosample, but neither result establishes TGIF2 occupancy in glioblastoma. | weak | [E04](#e04), [E20](#e20) |
| element | The variant falls within a promoter-like cCRE with active-chromatin marks in some ENCODE biosamples, without glioblastoma-specific confirmation. | supported | [E03](#e03) |
| gene | TERT is adjacent to the variant and is a plausible target, but no supplied evidence directly links this element to TERT expression; no significant brain-cortex eQTL was reported. | weak | [E01](#e01), [E02](#e02), [E33](#e33) |
| cell_type | TGIF2 is expressed in the glioblastoma DepMap context, but the reported overlapping peak is from HepG2 and does not establish occupancy in glioblastoma. | weak | [E04](#e04), [E20](#e20) |
| phenotype | TERT promoter alterations are relevant to cancer, but the evidence does not establish TGIF2 activity at this site or a disease effect of this variant. | weak | [E15a](#e15a), [E15e](#e15e), [E15h](#e15h), [E32a](#e32a) |

Predictions: If TGIF2 occupies this site in glioblastoma, ref should show greater TGIF2 binding than alt.; If ref-bound TGIF2 represses the promoter, alt should increase TERT transcription; if TGIF2 activates it, the expression direction would be reversed.

Falsified if: A suitable glioblastoma assay finds no TGIF2 occupancy or no ref-over-alt binding difference at the site.; With TGIF2 occupancy and the predicted binding difference confirmed, changing ref to alt produces no TERT regulatory effect.

### 4. H3: ZNF143-mediated regulation of the TERT promoter (p = 0.10)

TF ZNF143 (QBiC-SELEX coverage own_model), ref allele binds more; element The variant lies in a promoter-like cCRE with active-chromatin marks in some ENCODE biosamples; activity in glioblastoma is not established.; gene TERT is adjacent to the variant and is a plausible target, but regulation by this element is not demonstrated.; cell type ZNF143 is expressed in the glioblastoma DepMap context, but its site-overlapping peak is from GM12878; occupancy in glioblastoma is unestablished..

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | ZNF143's own QBiC-SELEX model predicts stronger ref binding. Its site-overlapping peak is from GM12878, not glioblastoma, so occupancy in the disease context is unestablished. | weak | [E04](#e04), [E14](#e14), [E21](#e21) |
| element | The variant falls within a promoter-like cCRE with active-chromatin marks in some ENCODE biosamples, without glioblastoma-specific confirmation. | supported | [E03](#e03) |
| gene | TERT is adjacent to the variant and is a plausible target, but no supplied evidence directly links this element to TERT expression; no significant brain-cortex eQTL was reported. | weak | [E01](#e01), [E02](#e02), [E33](#e33) |
| cell_type | ZNF143 is expressed in the glioblastoma DepMap context, but the reported overlapping peak is from GM12878 and does not establish occupancy in glioblastoma. | weak | [E04](#e04), [E14](#e14), [E21](#e21) |
| phenotype | TERT promoter alterations are relevant to cancer, but the evidence does not establish ZNF143 activity at this site or a disease effect of this variant. | weak | [E15a](#e15a), [E15e](#e15e), [E15h](#e15h), [E32a](#e32a) |

Predictions: If ZNF143 occupies this site in glioblastoma, ref should show greater ZNF143 binding than alt.; The TERT expression direction is not determined by the binding prediction: it depends on whether ZNF143 activates or represses this promoter.

Falsified if: A suitable glioblastoma assay finds no ZNF143 occupancy or no ref-over-alt binding difference at the site.; With ZNF143 occupancy and the predicted binding difference confirmed, changing ref to alt produces no TERT regulatory effect.

## Prediction matrix

| Test | Cost | Separates top two | H0 | H1 | H2 | H3 |
| --- | --- | --- | --- | --- | --- | --- |
| Paired ref/alt TERT-promoter reporter assay in a glioblastoma line, with and without GABPA depletion | medium | yes | No reproducible ref/alt reporter difference attributable to GABPA. | Alt reporter activity exceeds ref; the difference is reduced by GABPA depletion. | No GABPA-dependent difference is predicted; a result would require follow-up for TGIF2. | No GABPA-dependent difference is predicted; a result would require follow-up for ZNF143. |
| Allele-specific GABPA occupancy assay at the endogenous site in glioblastoma cells | medium | yes | No reproducible allele-specific GABPA occupancy difference. | GABPA occupancy is detected and is higher on alt than ref. | No specific GABPA occupancy difference is predicted. | No specific GABPA occupancy difference is predicted. |
| Allele-specific TGIF2 and ZNF143 occupancy assays at the endogenous site in glioblastoma cells | medium | no | No reproducible allele-specific occupancy pattern for either TF. | Neither TF-specific ref-higher occupancy pattern is predicted. | TGIF2 occupancy is detected and is higher on ref than alt. | ZNF143 occupancy is detected and is higher on ref than alt. |
| Isogenic ref-to-alt editing followed by TERT RNA and telomerase activity measurements in glioblastoma cells | high | yes | No reproducible TERT RNA or telomerase activity change. | Alt editing increases TERT RNA or telomerase activity if GABPA binding activates the promoter. | Alt editing changes TERT regulation; an increase is predicted only if ref-bound TGIF2 represses the promoter. | Alt editing may change TERT regulation, but the direction depends on ZNF143's unestablished activity here. |

## Next experiment

Run the paired ref/alt TERT-promoter reporter assay in a glioblastoma line with and without GABPA depletion. It is the lowest-cost proposed test of the leading GABPA chain against the null; a positive result would still need endogenous-locus validation.

## Refinement rounds

Stopped: round 1 left the top chain and the grades of its links unchanged.

### Round 1

- literature_search({"query": "chr5:1295135 G>A TERT promoter glioblastoma variant"}) for H1.phenotype, ran as [E32](#e32). Expected: If the search finds variant-specific functional or disease evidence, H1.phenotype gains support and H1 may rise; if it finds only general TERT-promoter literature, the grade remains weak.
- eqtl_lookup({"tissue": "Brain - Cortex"}) for H1.gene, ran as [E33](#e33). Expected: If this variant is associated with TERT expression in brain cortex, H1.gene gains support; if no association is reported, the proposed TERT link remains plausible but unproven.
- qbic_tf_detail({"tf": "GABPA"}) for H1.binding, ran as [E34](#e34). Expected: If the detail confirms a GABPA-specific model or additional GABPA coverage supporting the alt-higher prediction, H1.binding gains support; if it confirms only the mapped ETV5 model, attribution to GABPA remains weak.

- Result of literature_search for chr5:1295135 G>A TERT promoter glioblastoma variant (E32): The returned literature includes general evidence about TERT promoter mutations in bladder cancer, but no variant-specific functional or disease evidence for this site. (as expected: yes)
- Result of eQTL lookup in Brain - Cortex (E33): No significant GTEx v8 single-tissue eQTL was reported for this variant in brain cortex. (as expected: yes)
- Result of QBiC-SELEX detail for GABPA (E34): GABPA's own model predicts stronger alt binding, alongside alt-higher predictions from CIS-BP-mapped ETS models. This adds GABPA-specific in-vitro support, but does not establish GABPA occupancy in glioblastoma. (as expected: yes)

Chains after revision: null 0.46; GABPA 0.34; TGIF2 0.10; ZNF143 0.10. Link grades changed: H1.cell_type: supported → weak, H2.cell_type: supported → weak, H3.cell_type: supported → weak.

## Flags

- none

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

<a id="e32"></a>**E32** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=chr5%3A1295135%20G%3EA%20TERT%20promoter%20glioblastoma%20variant&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T23:19:47+00:00)

> Europe PMC: 4 hits for 'chr5:1295135 G>A TERT promoter glioblastoma variant'; top 4 with PMIDs:
> PMID 41062697 (2025): Sex and smoking bias in the selection of somatic mutations in human bladder.
> PMID 40097403 (2025): Multi-omic analysis of SDHB-deficient pheochromocytomas and paragangliomas identifies metastasis and treatment-related molecular profiles.
> PMID 38981438 (2024): Multi-scale signaling and tumor evolution in high-grade gliomas.
> PMID 33577785 (2021): Proteogenomic and metabolomic characterization of human glioblastoma.

<a id="e32a"></a>**E32a** literature_search, Europe PMC abstract, PMID 41062697 (https://europepmc.org/article/MED/41062697; retrieved 2026-10-26T23:19:47+00:00)

> We also found activating TERT promoter mutations driving clonal expansions in the normal bladder that were associated strongly with age and smoking.

<a id="e32b"></a>**E32b** literature_search, Europe PMC abstract, PMID 40097403 (https://europepmc.org/article/MED/40097403; retrieved 2026-10-26T23:19:47+00:00)

> TERT and ATRX-alterations are associated with metastatic PCPG and these tumours have an increased mutation load, and distinct transcriptional and telomeric features.

<a id="e33"></a>**E33** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr5_1295135_G_A_b38&datasetId=gtex_v8; retrieved 2026-10-26T20:17:52+00:00)

> 0 significant GTEx v8 single-tissue eQTLs for chr5_1295135_G_A_b38 in tissues matching 'Brain - Cortex'. NES is the effect of the alt allele (A) relative to ref (G).

<a id="e34"></a>**E34** qbic_tf_detail, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> {"tf":"GABPA","symbol":"GABPA","via":"hgnc_symbol","notes":[],"coverage":"own_model","variant":"chr5:1295135:G>A","gate_p":5.02e-05,"models":[{"model":"GABPA_FL_TC40NGCGATT_YWL_jolma2025_0_2_7mer","mapping":"own","group":"G003 Ets, 18 models","quality":0.658,"effect":4.05,"z":71.32,"p":0.0,"rank_abs_z":"7/997","passed_gate":true,"site_strength":{"ref_percentile":96.3,"alt_percentile":99.8,"k":7}},{"model":"ELF1_FL_TATGAC40NTCA_KW_yin2017_0_2_7mer","mapping":"CIS-BP (ELF1)","group":"G003 Ets, 18 models","quality":0.615,"effect":3.222,"z":164.23,"p":0.0,"rank_abs_z":"2/997","passed_gate":true,"site_strength":{"ref_percentile":96.6,"alt_percentile":100.0,"k":7}},{"model":"ELF2_eDBD_TGAAAT40NCAA_KR_yin2017_0_4_7mer","mapping":"CIS-BP (ELF2)","group":"G003 Ets, 18 models","quality":0.896,"effect":6.017,"z":54.18,"p":0.0,"rank_abs_z":"9/997","passed_gate":true,"site_strength":{"ref_percentile":98.8,"alt_percentile":100.0,"k":7}},{"model":"ELF4_eDBD_TGCGGT40NTCA_KAN_yin2017_0_4_7mer","mapping":"CIS-BP (ELF4)","group":"G003 Ets, 18 models","quality":0.732,"effect":4.814,"z":110.16,"p":0.0,"rank_abs_z":"4/997","passed_gate":true,"site_strength":{"ref_percentile":98.0,"alt_percentile":100.0,"k":7}},{"model":"ELK1_NA_TCGGAA20NAGT_ESAG_yang2017_1_3_7mer","mapping":"CIS-BP (ELK1)","group":"G003 Ets, 18 models","quality":0.779,"effect":2.107,"z":20.4,"p":1.6e-92,"rank_abs_z":"34/997","passed_gate":true,"site_strength":{"ref_percentile":92.4,"alt_percentile":99.9,"k":7}},{"model":"ELK3_FL_TTCGAA40NGAC_KX_yin2017_0_4_7mer","mapping":"CIS-BP (ELK3)","group":"G003 Ets, 18 models","quality":0.841,"effect":2.718,"z":34.59,"p":3.1e-262,"rank_abs_z":"16/997","passed_gate":true,"site_strength":{"ref_percentile":94.0,"alt_percentile":100.0,"k":7}},{"model":"ELK4_FL_TCCGCC40NTCA_KAE_yin2017_0_3_7mer","mapping":"CIS-BP (ELK4)","group":"G003 Ets, 18 models","quality":0.921,"effect":3.594,"z":62.15,"p":0.0,"rank_abs_z":"8/997","passed_gate":true,"site_strength":{"ref_percentile":70.7,"alt_percentile":99.6,"k":7}},{"model":"ERF_NA_TCAGAG20NCG_ESW_yang2017_1_4_7mer","mapping":"CIS-BP (ERF)","group":"G003 Ets, 18 models","quality":0.729,"effect":0.529,"z":19.81,"p":2.3e-87,"rank_abs_z":"36/997","passed_gate":true,"site_strength":{"ref_percentile":99.5,"alt_percentile":99.7,"k":7}},{"model":"ERG_NA_TCTACA20NCAG_ESAG_yang2017_1_4_7mer","mapping":"CIS-BP (ERG)","group":"G003 Ets, 18 models","quality":0.881,"effect":2.441,"z":24.39,"p":2e-131,"rank_abs_z":"22/997","passed_gate":true,"site_strength":{"ref_percentile":98.7,"alt_percentile":99.8,"k":7}},{"model":"ETS1_NA_TGTAAA20NGA_ESAF_yang2017_0_4_7mer","mapping":"CIS-BP (ETS1)","group":"G003 Ets, 18 models","quality":0.873,"effect":1.226,"z":25.6,"p":1.5e-144,"rank_abs_z":"20/997","passed_gate":true,"site_strength":{"ref_percentile":99.6,"alt_percentile":100.0,"k":7}}],"n_models_trimmed":8}
