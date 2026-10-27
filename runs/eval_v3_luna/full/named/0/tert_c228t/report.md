# TERT promoter C228T and Glioblastoma, melanoma, bladder

Configuration `full`, named mode, seed 0. Models: generator openai/gpt-6-luna, critic openai/gpt-6-luna, summariser openai/gpt-6-luna. Cost $0.01 over 7 model calls; 126 s.

Variant `chr5:1295113:G>A` (somatic); expression context: DepMap:subtype=Glioblastoma (median of 54 lines).

## QBiC-SELEX screen (occupancy first)

Occupied candidates: GABPA (bound elsewhere, z 166.19); ZIC2 (bound elsewhere, z -20.85); CTCF (bound elsewhere, z -14.7); ZBTB7A (bound elsewhere, z -14.11); NR2C1 (bound elsewhere, z -10.53); E2F4 (bound elsewhere, z 5.78); E2F6 (bound elsewhere, z 5.78); E2F5 (bound elsewhere, z 5.78); EGR1 (bound elsewhere, z -3.42, no clear allelic change); JUN (bound elsewhere, z 3.26, no clear allelic change). Occupancy unknown: ETV2 (z 166.19); ETV3 (z 166.19); FLI1 (z 166.19); TFAP2A (z -36.84); TFAP2C (z -36.84). Diagnostic, not shown to the model: 310 of 997 models pass Bonferroni.

## Ranked chains

### 1. H0: Null: no TF-mediated effect of this variant (p = 0.60)

Null chain: no TF-mediated effect of this variant.

Predictions: There will be no reproducible allele-specific TF occupancy that causes a TF-dependent change in TERT expression in relevant tumor cells.; Any disease association may reflect another cause, a non-TF mechanism, or no causal effect of this variant.

Falsified if: Isogenic allele editing demonstrates a reproducible TF-dependent change in occupancy and TERT expression in relevant tumor cells.

### 2. H1: Possible alt-allele gain of ETS-family binding, with GABPA as a candidate (p = 0.22)

TF GABPA (QBiC-SELEX coverage own_model), alt allele binds more; element TERT promoter-like cCRE EH38E3622530; gene TERT; cell type Glioblastoma cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The QBiC-SELEX result predicts greater alt-allele binding, but its best model is ETV5-mapped and gives the same result for several ETS factors; it does not identify GABPA specifically. GABPA is a candidate because it has variant-overlapping peaks in other biosamples and is expressed in the stated context, but occupancy in glioblastoma is not established. | weak | [E11](#e11), [E17](#e17), [E27](#e27), [E28](#e28), [E29](#e29), [E32](#e32) |
| element | The variant lies in a promoter-like cCRE with chromatin activity indicated by maxima across ENCODE biosamples, not specifically in glioblastoma cells. | supported | [E03](#e03) |
| gene | The promoter location makes altered TERT regulation plausible, but the supplied evidence does not show that GABPA or ETS binding at this variant changes TERT expression. | weak | [E01](#e01), [E02](#e02), [E03](#e03), [E34](#e34) |
| cell_type | This is proposed for glioblastoma cells; GABPA is expressed in the stated context, but no matching-context occupancy is shown, and the U-87 MG query found no peak while noting that an experiment may be absent. | weak | [E04](#e04), [E11](#e11), [E17](#e17), [E32](#e32) |
| phenotype | A TERT regulatory effect could be relevant to TERT-promoter-associated melanoma and IDH-wildtype glioblastoma, but the supplied evidence does not establish this mechanism or its contribution to bladder cancer. | weak | [E15a](#e15a), [E15e](#e15e), [E15h](#e15h) |

Predictions: In relevant tumor cells, the alt allele should show greater occupancy by GABPA or another ETS factor at this site.; A TERT expression difference caused by editing the allele should be reduced by perturbing the ETS factor that actually occupies the site.

Falsified if: Relevant tumor cells show no allele-dependent ETS occupancy at this site.; Isogenic allele editing produces no reproducible ETS-dependent change in TERT expression.

### 3. H2: Possible ref-allele gain of CTCF binding at the TERT promoter (p = 0.10)

TF CTCF (QBiC-SELEX coverage own_model), ref allele binds more; element TERT promoter-like cCRE EH38E3622530; gene TERT; cell type Glioblastoma cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | CTCF's own QBiC-SELEX model predicts stronger binding to the ref allele; a variant-overlapping CTCF peak is reported in another biosample, not in glioblastoma cells. | weak | [E13](#e13), [E19](#e19) |
| element | The variant lies in a promoter-like cCRE, but the reported chromatin maxima do not establish activity in glioblastoma cells. | supported | [E03](#e03) |
| gene | The promoter location makes a TERT effect plausible, but no supplied evidence connects CTCF binding at this site to TERT expression or determines the direction of any effect. | weak | [E01](#e01), [E02](#e02), [E03](#e03), [E34](#e34) |
| cell_type | CTCF is expressed in the stated context, but the reported occupancy is from another biosample and does not demonstrate binding in glioblastoma cells. | weak | [E04](#e04), [E13](#e13), [E19](#e19) |
| phenotype | A TERT regulatory effect could be relevant to TERT-promoter-associated melanoma and IDH-wildtype glioblastoma, but this CTCF mechanism is not demonstrated and the supplied literature does not establish relevance to bladder cancer. | weak | [E15a](#e15a), [E15e](#e15e), [E15h](#e15h) |

Predictions: If CTCF occupies this site in relevant tumor cells, occupancy should be greater on the ref allele.; Any allele-dependent TERT regulatory effect attributed to this chain should be reduced by disrupting CTCF.

Falsified if: CTCF does not occupy the site in relevant tumor cells.; The ref allele does not show greater CTCF occupancy, or CTCF perturbation leaves the allele-dependent TERT effect unchanged.

### 4. H3: Possible alt-allele gain of E2F-family binding, with E2F4 as a candidate (p = 0.08)

TF E2F4 (QBiC-SELEX coverage own_model), alt allele binds more; element TERT promoter-like cCRE EH38E3622530; gene TERT; cell type Glioblastoma cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The QBiC-SELEX result predicts greater alt-allele binding using an E2F1-mapped model, which does not identify E2F4 specifically. E2F4 has variant-overlapping peaks in other biosamples, but no occupancy is established in glioblastoma; the U-87 MG query found no peak and notes that an experiment may be absent. | weak | [E09](#e09), [E22](#e22), [E33](#e33) |
| element | The variant lies in a promoter-like cCRE, but the biosample-maximum chromatin scores do not establish activity in glioblastoma cells. | supported | [E03](#e03) |
| gene | The promoter location makes altered E2F-family regulation of TERT plausible, but the supplied evidence does not show that E2F4 or another E2F factor changes TERT expression through this variant. | weak | [E01](#e01), [E02](#e02), [E03](#e03), [E34](#e34) |
| cell_type | E2F4 is expressed in the stated context, but the available occupancy evidence is from other biosamples and does not establish binding in glioblastoma cells. | weak | [E04](#e04), [E09](#e09), [E22](#e22), [E33](#e33) |
| phenotype | A TERT regulatory effect could be relevant to TERT-promoter-associated melanoma and IDH-wildtype glioblastoma, but this E2F mechanism is not demonstrated and the supplied literature does not establish relevance to bladder cancer. | weak | [E15a](#e15a), [E15e](#e15e), [E15h](#e15h) |

Predictions: If this chain operates, E2F4 or another E2F factor should occupy the site in relevant tumor cells, with greater occupancy on the alt allele.; Perturbing the E2F factor that occupies the site should reduce any allele-dependent TERT expression effect.

Falsified if: No E2F-family factor occupies the site in relevant tumor cells.; The alt allele does not increase E2F occupancy, or E2F perturbation leaves the allele-dependent TERT effect unchanged.

## Prediction matrix

| Test | Cost | Separates top two | H0 | H1 | H2 | H3 |
| --- | --- | --- | --- | --- | --- | --- |
| In a glioblastoma model, edit the promoter allele and measure TERT RNA with and without GABPA depletion. | medium | yes | No reproducible TF-dependent allele effect on TERT RNA. | Editing changes TERT RNA, and the allele-dependent change is reduced by GABPA depletion. | No GABPA-dependent allele effect; a CTCF-mediated effect remains possible. | No GABPA-dependent allele effect; an E2F-mediated effect remains possible. |
| Measure allele-specific CTCF occupancy at the endogenous site in informative glioblastoma cells. | medium | no | No reproducible allele-specific CTCF occupancy. | No specific ref-greater-than-alt CTCF occupancy is predicted by this chain. | CTCF occupies the site more strongly on the ref allele. | No specific ref-greater-than-alt CTCF occupancy is predicted by this chain. |
| Measure allele-specific E2F4 occupancy at the endogenous site in glioblastoma cells. | medium | no | No reproducible allele-specific E2F4 occupancy. | No specific E2F4 alt-allele occupancy is predicted by this chain. | No specific E2F4 alt-allele occupancy is predicted by this chain. | E2F4 occupancy is greater on the alt allele if E2F4 is the factor acting at the site. |

## Next experiment

The top two hypotheses are H1 and H0. The cheapest informative test is a dual-allele TERT-promoter reporter assay in a glioblastoma cell model, measuring reporter output with and without GABPA depletion. H1 predicts an allele-dependent output difference reduced by GABPA depletion; H0 predicts no reproducible GABPA-dependent allele effect. This is a screening test and would not replace validation at the endogenous locus.

## Investigate calls

- chip_peaks({"tf": "GABPA", "biosample": "U-87 MG"})
- chip_peaks({"tf": "E2F4", "biosample": "U-87 MG"})
- literature_search({"query": "TERT promoter C228T GABPA CTCF E2F4 reporter assay TERT expression glioblastoma"})

## Flags

- none

Citation support: 1.00 of links cite only evidence that passed every check.

## Evidence

<a id="e01"></a>**E01** variant_annotation, Ensembl VEP (GRCh38) (https://rest.ensembl.org/vep/human/region/5:1295113-1295113:1/A?content-type=application/json&Conservation=1; retrieved 2026-10-25T11:57:36+00:00)

> Variant chr5:1295113:G>A (GRCh38), allele string G/A
> Known IDs: rs1242535815
> Most severe consequence: upstream_gene_variant
> Regulatory features: ENSR5_832QG promoter
> GERP conservation score at the site: -7.45
> Transcript consequences: TERT (upstream_gene_variant)

<a id="e02"></a>**E02** nearest_genes, Ensembl overlap (protein_coding) (https://rest.ensembl.org/overlap/region/human/5:295113-2295113?feature=gene;biotype=protein_coding;content-type=application/json; retrieved 2026-10-25T11:57:33+00:00)

> 23 protein-coding genes within 1000 kb of chr5:1295113:G>A, by distance to TSS:
> TERT: 0.0 kb from TSS (upstream, strand -1)
> CLPTM1L: 50.0 kb from TSS (downstream, strand -1)
> SLC6A18: 69.7 kb from TSS (downstream, strand +1)
> SLC6A19: 93.5 kb from TSS (downstream, strand +1)
> SLC12A7: 138.9 kb from TSS (upstream, strand -1)
> SLC6A3: 150.4 kb from TSS (downstream, strand -1)
> LPCAT1: 229.2 kb from TSS (downstream, strand -1)
> NKD2: 287.1 kb from TSS (downstream, strand +1)
> TRIP13: 402.3 kb from TSS (downstream, strand +1)
> BRD9: 402.3 kb from TSS (upstream, strand -1)

<a id="e03"></a>**E03** ccre_lookup, ENCODE v4 cCRE registry (ENCFF420VPZ) and SCREEN (https://screen-beta-api.wenglab.org/dataws/cre_table; retrieved 2026-10-25T11:57:31+00:00)

> The variant lies in cCRE EH38E3622530 (PLS: promoter-like), chr5:1294945-1295294.
> SCREEN: 3 cCREs within 500 bp (max z-score across ENCODE biosamples):
> EH38E3622530 PLS (contains the variant): DNase z 4.8, H3K27ac z 4.2, H3K4me3 z 4.5, CTCF z 2.0; nearby genes TERT, MIR4457, CLPTM1L
> EH38E3622531 pELS: DNase z 3.9, H3K27ac z 4.3, H3K4me3 z 4.4, CTCF z 2.8; nearby genes TERT, MIR4457, CLPTM1L
> EH38E3622529 pELS: DNase z 3.7, H3K27ac z 4.1, H3K4me3 z 4.6, CTCF z 2.0; nearby genes TERT, MIR4457, CLPTM1L
> Biosample-specific z-scores are not in this call; the values above are maxima over biosamples.

<a id="e04"></a>**E04** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> ENCODE TF ChIP-seq at chr5:1295113:G>A: 121 peaks contain the variant, from 54 factors in 21 biosamples. No ENCODE biosample matches the expression context, so no peak counts as bound here. cCRE class at the variant: PLS. Bound factors outside the TF model collection (co-factors, Pol II, and TFs with no binding model; signs of an active element, not TF candidates): ARID4A, BCL3, DMAP1, EZH2, EZH2phosphoT487, GABPB1, HDAC1, HDAC2, HDAC6, HNRNPK, IKZF1, KDM4A (+21 more). Bound, expressed TFs with a binding model: 20; listed one per row: MAX, JUN, EGR1, BHLHE40, E2F4, E2F6, GABPA, ZNF687, CTCF, NR2C1; also bound: ZNF143, SP2, TGIF2, MNT, ZBTB7A, E2F5, ZBTB26, KLF12, ZNF48, ZIC2. Bound but below 1 TPM: ZFHX2. Assayed with no peak here: 0 TFs in the matching biosample, 552 only elsewhere; never assayed: 536.

<a id="e05"></a>**E05** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> MAX: bound elsewhere. 13 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: A549, HCT116, HepG2, Ishikawa, K562, MCF-7 (+2 more) (e.g. ENCSR000BLP). 58.6 TPM in DepMap:subtype=Glioblastoma (median of 54 lines), rank 48 of 1626 TFs.

<a id="e06"></a>**E06** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> JUN: bound elsewhere. 11 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: A549 (e.g. ENCSR022WVP). 91.65 TPM in DepMap:subtype=Glioblastoma (median of 54 lines), rank 16 of 1626 TFs.

<a id="e07"></a>**E07** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> EGR1: bound elsewhere. 3 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: HepG2, Ishikawa, K562 (e.g. ENCSR000BNE). 28.32 TPM in DepMap:subtype=Glioblastoma (median of 54 lines), rank 151 of 1626 TFs.

<a id="e08"></a>**E08** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> BHLHE40: bound elsewhere. 2 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: GM12878 (e.g. ENCSR000DZJ). 68.33 TPM in DepMap:subtype=Glioblastoma (median of 54 lines), rank 33 of 1626 TFs.

<a id="e09"></a>**E09** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> E2F4: bound elsewhere. 2 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: GM12878, HepG2 (e.g. ENCSR000DYY). 58.31 TPM in DepMap:subtype=Glioblastoma (median of 54 lines), rank 49 of 1626 TFs.

<a id="e10"></a>**E10** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> E2F6: bound elsewhere. 2 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: A549, K562 (e.g. ENCSR000BLI). 17.63 TPM in DepMap:subtype=Glioblastoma (median of 54 lines), rank 267 of 1626 TFs.

<a id="e11"></a>**E11** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> GABPA: bound elsewhere. 2 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: HepG2, SK-N-SH (e.g. ENCSR000BJK). 15.52 TPM in DepMap:subtype=Glioblastoma (median of 54 lines), rank 303 of 1626 TFs.

<a id="e12"></a>**E12** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> ZNF687: bound elsewhere. 2 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: HepG2 (e.g. ENCSR647PSR). 10.74 TPM in DepMap:subtype=Glioblastoma (median of 54 lines), rank 436 of 1626 TFs.

<a id="e13"></a>**E13** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> CTCF: bound elsewhere. 1 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: DOHH2 (e.g. ENCSR084RDK). 26.45 TPM in DepMap:subtype=Glioblastoma (median of 54 lines), rank 163 of 1626 TFs.

<a id="e14"></a>**E14** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> NR2C1: bound elsewhere. 1 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: GM12878 (e.g. ENCSR784VIQ). 18.52 TPM in DepMap:subtype=Glioblastoma (median of 54 lines), rank 251 of 1626 TFs.

<a id="e15"></a>**E15** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TERT%20AND%20%28%22glioblastoma%22%20OR%20%22melanoma%22%20OR%20%22bladder%22%29&format=json&pageSize=8&resultType=core; retrieved 2026-10-25T11:57:36+00:00)

> Europe PMC: 23888 hits for 'TERT AND ("glioblastoma" OR "melanoma" OR "bladder")'; top 7 with PMIDs:
> PMID 41744838 (2026): Telomerase Activity in Melanoma: Impact on Cancer Cell Proliferation Kinetics, Tumor Progression, and Clinical Therapeutic Strategies-A Scoping Review.
> PMID 42577103 (2026): Familial melanoma: genetic, clinical, and dermoscopic insights and follow-up.
> PMID 42722679 (2026): Developing neoantigen cancer vaccines: where are we now?
> PMID 42741698 (2026): Melanoma of unknown primary with solitary lesions to the prostate and lung uncovered after simple prostatectomy.
> PMID 42804732 (2026): SNP rs2853669 potentially elevates the risk of glioblastoma development and leads to worse prognosis when in cis with mutant TERT promoter in a Japanese cohort.
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

> BackgroundMutations in the telomerase reverse transcriptase (TERT) promoter region (TPM), particularly C228T and C250T, are common in IDH-wildtype glioblastoma (GBM).

<a id="e15f"></a>**E15f** literature_search, Europe PMC abstract, PMID 42804732 (https://europepmc.org/article/MED/42804732; retrieved 2026-10-25T11:57:36+00:00)

> ConclusionThe rs2853669 C allele may increase GBM susceptibility and, when in cis with TPM, is associated with reduced TERT expression and poorer prognosis, underscoring its biological and clinical significance in TPM-mutant GBM.

<a id="e15g"></a>**E15g** literature_search, Europe PMC abstract, PMID 42807929 (https://europepmc.org/article/MED/42807929; retrieved 2026-10-25T11:57:36+00:00)

> Additionally, loss of either USP10 or FOXM1 suppresses the expression of the downstream target Telomerase reverse transcriptase (TERT), triggering cellular senescence.

<a id="e15h"></a>**E15h** literature_search, Europe PMC abstract, PMID 42859331 (https://europepmc.org/article/MED/42859331; retrieved 2026-10-25T11:57:36+00:00)

> TERT promoter (TERTp) mutations are among the most frequent molecular alterations in isocitrate dehydrogenase (IDH) wild-type glioblastoma (GBM), yet the molecular profiles and prognostic implications associated with TERTp status remain incompletely characterized.

<a id="e15i"></a>**E15i** literature_search, Europe PMC abstract, PMID 42859331 (https://europepmc.org/article/MED/42859331; retrieved 2026-10-25T11:57:36+00:00)

> The prognostic relevance of CDKN2A deletion may vary according to TERTp status, particularly for OS.

<a id="e16"></a>**E16** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> QBiC-SELEX screen of chr5:1295113:G>A, one line per TF, each with the TF's own or CIS-BP-mapped model of largest |z|. Candidates are TFs whose ENCODE ChIP-seq peaks contain the variant and that are expressed (DepMap subtype median Glioblastoma), bound here before bound elsewhere, then a strong site before a weak one, then by |z|; then expressed TFs ENCODE never assayed whose best model passes the gate (occupancy unknown). Shown: 10 of 20 occupied (15 with a strong site), 5 of 111 with unknown occupancy. Left out: 0 TFs assayed in the matching biosample and 552 assayed only elsewhere, none with a peak here; 1 bound but below 1 TPM. The gate (|z| > 4.05, Bonferroni over 997 models) marks a change QBiC-SELEX detects; it says nothing about occupancy. Effect > 0 means the alternate allele binds more strongly. In vitro binding only. Site strength is the better allele's best k-mer over the variant, as a percentile of the best model's k-mers; a strong site reaches the 97.5th. At a weak site the ChIP peak more likely reflects another site in the element.

<a id="e17"></a>**E17** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> GABPA (Ets, 18 models; QBiC-SELEX coverage: own model): best model ETV5_NA_TGCACT20NGA_ESAF_yang2017_1_3_6mer (a CIS-BP-mapped model of ETV5), z 166.19, effect 2.121: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 15.52 TPM, rank 303 of 1626 TFs in DepMap:subtype=Glioblastoma (median of 54 lines). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in HepG2, SK-N-SH, e.g. ENCSR000BJK. Best model's site strength: ref 97.1th, alt 99.3th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e18"></a>**E18** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> ZIC2 (C2H2 ZF, 4 models; QBiC-SELEX coverage: mapped models only): best model ZIC4_eDBD_TGCGTA40NTCA_KT_yin2017_1_3_7mer (a CIS-BP-mapped model of ZIC4), z -20.85, effect -0.916: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 3.7 TPM, rank 852 of 1626 TFs in DepMap:subtype=Glioblastoma (median of 54 lines). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in HEK293, e.g. ENCSR728MWW. Best model's site strength: ref 99.8th, alt 97.4th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e19"></a>**E19** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> CTCF (C2H2 ZF, 1 model; QBiC-SELEX coverage: own model): best model CTCF_FL_TG40NCTGTGG_YWL_jolma2025_0_3_7mer (its own model), z -14.7, effect -1.719: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 26.45 TPM, rank 163 of 1626 TFs in DepMap:subtype=Glioblastoma (median of 54 lines). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in DOHH2, e.g. ENCSR084RDK. Best model's site strength: ref 99.8th, alt 97.0th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e20"></a>**E20** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> ZBTB7A (C2H2 ZF, 1 model; QBiC-SELEX coverage: own model): best model ZBTB7A_eDBD_TTTGCT40NCGT_KR_yin2017_0_4_7mer (its own model), z -14.11, effect -0.826: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 8.49 TPM, rank 531 of 1626 TFs in DepMap:subtype=Glioblastoma (median of 54 lines). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in K562, e.g. ENCSR000BME. Best model's site strength: ref 99.9th, alt 99.9th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e21"></a>**E21** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> NR2C1 (Nuclear receptor, 29 models; QBiC-SELEX coverage: own model): best model FXR_NA_Lib1_NA_bhimsaria2023_0(3)_3_7mer (a CIS-BP-mapped model of NR1H4), z -10.53, effect -0.434: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 18.52 TPM, rank 251 of 1626 TFs in DepMap:subtype=Glioblastoma (median of 54 lines). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in GM12878, e.g. ENCSR784VIQ. Best model's site strength: ref 97.7th, alt 97.9th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e22"></a>**E22** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> E2F4 (E2F, 4 models; QBiC-SELEX coverage: own model): best model E2F1_NA_CAATT14N_ESU_yang2017_0_4_7mer (a CIS-BP-mapped model of E2F1), z 5.78, effect 0.464: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 58.31 TPM, rank 49 of 1626 TFs in DepMap:subtype=Glioblastoma (median of 54 lines). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in GM12878, HepG2, e.g. ENCSR000DYY. Best model's site strength: ref 98.9th, alt 99.5th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e23"></a>**E23** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> E2F6 (E2F, 4 models; QBiC-SELEX coverage: mapped models only): best model E2F1_NA_CAATT14N_ESU_yang2017_0_4_7mer (a CIS-BP-mapped model of E2F1), z 5.78, effect 0.464: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 17.63 TPM, rank 267 of 1626 TFs in DepMap:subtype=Glioblastoma (median of 54 lines). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in A549, K562, e.g. ENCSR000BLI. Best model's site strength: ref 98.9th, alt 99.5th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e24"></a>**E24** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> E2F5 (E2F, 4 models; QBiC-SELEX coverage: mapped models only): best model E2F1_NA_CAATT14N_ESU_yang2017_0_4_7mer (a CIS-BP-mapped model of E2F1), z 5.78, effect 0.464: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 6.91 TPM, rank 605 of 1626 TFs in DepMap:subtype=Glioblastoma (median of 54 lines). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in HepG2, e.g. ENCSR486JYI. Best model's site strength: ref 98.9th, alt 99.5th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e25"></a>**E25** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> EGR1 (C2H2 ZF, 4 models; QBiC-SELEX coverage: own model): best model EGR4_NA_TGCGCC20NCGC_Y_jolma2013_1_4_7mer (a CIS-BP-mapped model of EGR4), z -3.42, effect -0.541: ref allele binds slightly more; occupied, no clear allelic change (|z| below the gate). 28.32 TPM, rank 151 of 1626 TFs in DepMap:subtype=Glioblastoma (median of 54 lines). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in HepG2, Ishikawa, K562, e.g. ENCSR000BNE. Best model's site strength: ref 99.5th, alt 99.6th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e26"></a>**E26** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> JUN (bZIP, 3 models; QBiC-SELEX coverage: own model): best model JUND_eDBD_TCTCTA40NCAC_KS_yin2017_0_4_7mer (a CIS-BP-mapped model of JUND), z 3.26, effect 0.185: alt allele binds slightly more; occupied, no clear allelic change (|z| below the gate). 91.65 TPM, rank 16 of 1626 TFs in DepMap:subtype=Glioblastoma (median of 54 lines). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in A549, e.g. ENCSR022WVP. Best model's site strength: ref 98.5th, alt 94.9th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e27"></a>**E27** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> ETV2 (Ets, 18 models; QBiC-SELEX coverage: own model): best model ETV5_NA_TGCACT20NGA_ESAF_yang2017_1_3_6mer (a CIS-BP-mapped model of ETV5), z 166.19, effect 2.121: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 1.4 TPM, rank 1063 of 1626 TFs in DepMap:subtype=Glioblastoma (median of 54 lines). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 97.1th, alt 99.3th percentile of its k-mer coefficients.

<a id="e28"></a>**E28** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> ETV3 (Ets, 18 models; QBiC-SELEX coverage: own model): best model ETV5_NA_TGCACT20NGA_ESAF_yang2017_1_3_6mer (a CIS-BP-mapped model of ETV5), z 166.19, effect 2.121: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 8.69 TPM, rank 521 of 1626 TFs in DepMap:subtype=Glioblastoma (median of 54 lines). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 97.1th, alt 99.3th percentile of its k-mer coefficients.

<a id="e29"></a>**E29** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> FLI1 (Ets, 18 models; QBiC-SELEX coverage: own model): best model ETV5_NA_TGCACT20NGA_ESAF_yang2017_1_3_6mer (a CIS-BP-mapped model of ETV5), z 166.19, effect 2.121: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 4.71 TPM, rank 767 of 1626 TFs in DepMap:subtype=Glioblastoma (median of 54 lines). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 97.1th, alt 99.3th percentile of its k-mer coefficients.

<a id="e30"></a>**E30** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> TFAP2A (AP-2, 4 models; QBiC-SELEX coverage: own model): best model TFAP2E_FL_TCAAAC40NAAC_KW_yin2017_1_3_7mer (a CIS-BP-mapped model of TFAP2E), z -36.84, effect -1.289: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 9.65 TPM, rank 479 of 1626 TFs in DepMap:subtype=Glioblastoma (median of 54 lines). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 99.5th, alt 96.5th percentile of its k-mer coefficients.

<a id="e31"></a>**E31** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> TFAP2C (AP-2, 4 models; QBiC-SELEX coverage: own model): best model TFAP2E_FL_TCAAAC40NAAC_KW_yin2017_1_3_7mer (a CIS-BP-mapped model of TFAP2E), z -36.84, effect -1.289: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 6.49 TPM, rank 631 of 1626 TFs in DepMap:subtype=Glioblastoma (median of 54 lines). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 99.5th, alt 96.5th percentile of its k-mer coefficients.

<a id="e32"></a>**E32** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-25T11:58:44+00:00)

> No ENCODE GABPA ChIP-seq peak contains chr5:1295113:G>A in biosamples matching 'U-87 MG'. Absence can also mean no GABPA experiment in that biosample. In other biosamples, 2 GABPA peaks do contain the variant: HepG2, SK-N-SH (experiments ENCSR000BJK, ENCSR000BTG).

<a id="e33"></a>**E33** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-26T13:31:14+00:00)

> No ENCODE E2F4 ChIP-seq peak contains chr5:1295113:G>A in biosamples matching 'U-87 MG'. Absence can also mean no E2F4 experiment in that biosample. In other biosamples, 2 E2F4 peaks do contain the variant: GM12878, HepG2 (experiments ENCSR000DYY, ENCSR924LSO).

<a id="e34"></a>**E34** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TERT%20promoter%20C228T%20GABPA%20CTCF%20E2F4%20reporter%20assay%20TERT%20expression%20glioblastoma&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T13:31:14+00:00)

> Europe PMC: 0 hits for 'TERT promoter C228T GABPA CTCF E2F4 reporter assay TERT expression glioblastoma'; top 0 with PMIDs:
