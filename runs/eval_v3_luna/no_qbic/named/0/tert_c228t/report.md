# TERT promoter C228T and Glioblastoma, melanoma, bladder

Configuration `no_qbic`, named mode, seed 0. Models: generator openai/gpt-6-luna, critic openai/gpt-6-luna, summariser openai/gpt-6-luna. Cost $0.01 over 8 model calls; 322 s.

Variant `chr5:1295113:G>A` (somatic); expression context: DepMap:subtype=Glioblastoma (median of 54 lines).

## Ranked chains

### 1. H1: No TF-mediated effect of this variant (p = 0.55)

Null chain: no TF-mediated effect of this variant.

Predictions: Changing this base alone will not reproducibly cause a TF-dependent change in TERT expression.; Any association with cancer will be due to other genetic or cellular factors, or to a mechanism not mediated by a TF binding change at this variant.

Falsified if: In an otherwise matched system, changing this base reproducibly alters TERT expression and that effect depends on a TF binding at the site.

### 2. H2: The mutant promoter recruits GABPA and increases TERT output (p = 0.40)

TF GABPA (QBiC-SELEX coverage own_model), alt allele binds more; element The variant overlaps a promoter-like cCRE; activity of this element in glioblastoma cells is not established by the biosample-maximal chromatin scores.; gene TERT; cell type Glioblastoma is a plausible context, but variant-overlapping GABPA occupancy there has not been demonstrated..

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | GABPA is the best-supported TF candidate because literature identifies GABPA as an activator of mutant TERT promoters, while ChIP peaks at this site are reported only in other biosamples; an alt-favored effect is consistent with the reported ETS-motif gain, but no GABPA QBiC-SELEX model or result is supplied here and the allelic binding direction is not directly measured for this variant. | weak | [E04](#e04), [E11](#e11), [E16](#e16), [E18a](#e18a), [E18d](#e18d) |
| element | The variant lies in a promoter-like cCRE with chromatin marks consistent with promoter activity, although the reported scores are maxima across biosamples. | supported | [E03](#e03) |
| gene | TERT is immediately adjacent to the variant and is listed near the variant-overlapping promoter-like cCRE, which supports proximity but does not establish functional regulation by this variant. | supported | [E01](#e01), [E02](#e02), [E03](#e03) |
| cell_type | Glioblastoma is a candidate context, but the evidence reports no variant-overlapping GABPA peak in a matching biosample and notes that no matching-biosample peak counts as bound. | weak | [E04](#e04), [E11](#e11), [E16](#e16) |
| phenotype | If mutant-promoter GABPA activity increases TERT output, it could contribute to telomerase-related cancer biology, but the supplied literature does not establish this full chain for this variant in the stated cells. | weak | [E15a](#e15a), [E15e](#e15e), [E15h](#e15h), [E18a](#e18a), [E18b](#e18b) |

Predictions: In an appropriate cellular context, the alt promoter will show greater GABPA-dependent activity than the ref promoter; the allelic binding difference itself remains to be measured.; Reducing GABPA will diminish or eliminate the alt-associated increase in TERT expression or promoter activity.

Falsified if: Matched assays show no alt-associated GABPA-dependent promoter or TERT-expression effect, or GABPA perturbation leaves the allelic effect unchanged.

### 3. H3: An alternative MAX-dependent promoter effect (p = 0.05)

TF MAX (QBiC-SELEX coverage own_model), alt allele binds more; element The variant overlaps a promoter-like cCRE; activity of this element in glioblastoma cells is not established by the biosample-maximal chromatin scores.; gene TERT; cell type Glioblastoma is a candidate context, but variant-overlapping MAX occupancy there has not been demonstrated..

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | MAX is expressed and has variant-overlapping ChIP peaks in other biosamples, but there is no matching-biosample occupancy or supplied MAX QBiC-SELEX result to support an alt-favored effect; that direction is a speculative alternative, not a measured result. | missing | [E04](#e04), [E05](#e05), [E17](#e17) |
| element | The variant lies in a promoter-like cCRE with chromatin marks consistent with promoter activity, although the reported scores are maxima across biosamples. | supported | [E03](#e03) |
| gene | TERT is immediately adjacent to the variant and is listed near the variant-overlapping promoter-like cCRE, which supports proximity but does not establish functional regulation by this variant. | supported | [E01](#e01), [E02](#e02), [E03](#e03) |
| cell_type | Glioblastoma is a candidate context, but the evidence reports no variant-overlapping MAX peak in a matching biosample. | weak | [E04](#e04), [E05](#e05), [E17](#e17) |
| phenotype | A MAX-dependent change in TERT promoter output could affect cancer-related telomerase biology, but the supplied evidence does not connect MAX binding at this variant to a disease phenotype. | weak | [E15a](#e15a), [E15e](#e15e), [E15h](#e15h) |

Predictions: If this alternative is correct, the alt promoter's effect on TERT will depend on MAX rather than GABPA.; MAX perturbation will remove the allelic promoter or expression difference, whereas GABPA perturbation will not.

Falsified if: MAX perturbation does not affect an alt-associated promoter or TERT-expression difference, or the effect instead depends on GABPA.

## Prediction matrix

| Test | Cost | Separates top two | H1 | H2 | H3 |
| --- | --- | --- | --- | --- | --- |
| Dual-luciferase comparison of ref and alt TERT promoter constructs in a glioblastoma cell line, with and without GABPA depletion | medium | yes | No reproducible alt-specific increase in promoter activity that depends on GABPA. | Alt promoter activity is higher, and the difference is reduced or lost after GABPA depletion. | Any alt-specific activity is not selectively lost after GABPA depletion; a MAX-dependent effect remains possible. |
| Allele-specific GABPA occupancy assay at the endogenous locus in a suitable heterozygous glioblastoma model | high | yes | No reproducible allele-specific GABPA occupancy. | Greater GABPA occupancy on the alt allele. | No required alt-favored GABPA occupancy; MAX is the proposed alternative. |
| Compare ref and alt TERT promoter activity with and without MAX perturbation | medium | no | No reproducible MAX-dependent allelic difference. | Any alt-associated effect is not specifically dependent on MAX. | The alt-associated promoter effect is reduced or lost after MAX perturbation. |

## Next experiment

Run the ref-versus-alt dual-luciferase promoter assay in a glioblastoma cell line with and without GABPA depletion. It is the cheapest proposed test that directly distinguishes the top two hypotheses, H1 and H2.

## Investigate calls

- chip_peaks({"tf": "GABPA", "biosample": "Glioblastoma"})
- chip_peaks({"tf": "MAX", "biosample": "Glioblastoma"})
- literature_search({"query": "TERT C228T GABPA MAX allele-specific binding reporter assay glioblastoma"})

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

<a id="e16"></a>**E16** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-25T11:58:44+00:00)

> No ENCODE GABPA ChIP-seq peak contains chr5:1295113:G>A in biosamples matching 'Glioblastoma'. Absence can also mean no GABPA experiment in that biosample. In other biosamples, 2 GABPA peaks do contain the variant: HepG2, SK-N-SH (experiments ENCSR000BJK, ENCSR000BTG).

<a id="e17"></a>**E17** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-26T13:20:00+00:00)

> No ENCODE MAX ChIP-seq peak contains chr5:1295113:G>A in biosamples matching 'Glioblastoma'. Absence can also mean no MAX experiment in that biosample. In other biosamples, 13 MAX peaks do contain the variant: A549, HCT116, HepG2, Ishikawa, K562, MCF-7, NB4, SK-N-SH (experiments ENCSR000BLP, ENCSR000BSH, ENCSR000BTJ, ENCSR000BTM, ENCSR000BTY, ENCSR000BUL).

<a id="e18"></a>**E18** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TERT%20C228T%20GABPA%20MAX%20allele-specific%20binding%20reporter%20assay%20glioblastoma&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T13:20:12+00:00)

> Europe PMC: 8 hits for 'TERT C228T GABPA MAX allele-specific binding reporter assay glioblastoma'; top 5 with PMIDs:
> PMID 31802036 (2020): GABPA is a master regulator of luminal identity and restrains aggressive diseases in bladder cancer.
> PMID 31285550 (2019): Mechanisms underlying the activation of TERT transcription and telomerase activity in human cancer: old actors and new players.
> PMID 33832990 (2021): Interpretation of allele-specific chromatin accessibility using cell state-aware deep learning.
> PMID 31903880 (2020): Telomere-related Markers for Cancer.
> PMID 27548225 (2016): Transcription Regulation of the Human Telomerase Reverse Transcriptase (hTERT) Gene.

<a id="e18a"></a>**E18a** literature_search, Europe PMC abstract, PMID 31802036 (https://europepmc.org/article/MED/31802036; retrieved 2026-10-26T13:20:12+00:00)

> TERT promoter mutations occur in the majority of glioblastoma, bladder cancer (BC), and other malignancies while the ETS family transcription factors GABPA and its partner GABPB1 activate the mutant TERT promoter and telomerase in these tumors.

<a id="e18b"></a>**E18b** literature_search, Europe PMC abstract, PMID 31802036 (https://europepmc.org/article/MED/31802036; retrieved 2026-10-26T13:20:12+00:00)

> GABPA depletion or the disruption of the GABPA/GABPB1 complex by knocking down GABPB1 was shown to inhibit telomerase, thereby eliminating the tumorigenic potential of glioblastoma cells.

<a id="e18c"></a>**E18c** literature_search, Europe PMC abstract, PMID 31285550 (https://europepmc.org/article/MED/31285550; retrieved 2026-10-26T13:20:12+00:00)

> In the last two decades since the TERT gene and promoter were cloned, the derepression of the TERT gene has been shown to be achieved typically at a transcriptional level through dysregulation of oncogenic factors or signaling, post-transcriptional/translational regulation and genomic amplification.

<a id="e18d"></a>**E18d** literature_search, Europe PMC abstract, PMID 33832990 (https://europepmc.org/article/MED/33832990; retrieved 2026-10-26T13:20:12+00:00)

> Finally, by augmenting the DeepMEL2 model with ChIP-seq data for GABPA, the TERT promoter mutation, as well as additional ETS motif gains, can be identified with high confidence.
