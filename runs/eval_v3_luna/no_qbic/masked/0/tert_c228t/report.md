# TERT promoter C228T and Glioblastoma, melanoma, bladder

Configuration `no_qbic`, masked mode, seed 0. Models: generator openai/gpt-6-luna, critic openai/gpt-6-luna, summariser openai/gpt-6-luna. Cost $0.01 over 7 model calls; 145 s.

Variant `chr5:1295113:G>A` (somatic); expression context: DepMap:subtype=Glioblastoma (median of 54 lines).

## Ranked chains

### 1. H1: No TF-mediated effect at this variant (p = 0.92)

Null chain: no TF-mediated effect of this variant.

Predictions: In relevant glioblastoma cells, the variant will not produce a reproducible allele-specific binding effect for the candidate TFs or a TF-dependent change in TERT expression; any disease association could reflect linkage or another process.

Falsified if: An allele-specific assay shows a reproducible binding difference at this base and a corresponding TF-dependent change in TERT expression.

### 2. H2: Speculative MAX-mediated effect at the TERT promoter (p = 0.05)

TF MAX (QBiC-SELEX coverage own_model), alt allele binds more; element Promoter-like cCRE EH38E3622530; gene TERT; cell type Glioblastoma cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The testable prediction is that MAX binds alt A more strongly than ref G, but the supplied evidence gives no allele-specific binding direction or QBiC-SELEX result; MAX is a candidate because it is expressed and has more site-overlapping peaks in other biosamples than the other named candidates, not because its occupancy in glioblastoma is established. | missing | [E04](#e04), [E05](#e05) |
| element | The variant lies in a promoter-like cCRE with active chromatin marks reported across ENCODE biosamples, although activity in glioblastoma is not established. | supported | [E03](#e03) |
| gene | The variant is annotated upstream of TERT and at its transcription start site, but this positional evidence does not demonstrate that the cCRE regulates TERT. | supported | [E01](#e01), [E02](#e02) |
| cell_type | Glioblastoma is the supplied expression context, but no matching-biosample MAX occupancy evidence is reported. | supported | [E04](#e04), [E05](#e05), [E16](#e16) |
| phenotype | A TERT regulatory effect could be relevant to glioblastoma, where TERT promoter mutations are common, but these sources do not establish a MAX-mediated effect of this variant or a disease effect in this case. | weak | [E15e](#e15e), [E15h](#e15h) |

Predictions: Compared with ref G, alt A will show greater MAX binding in a relevant assay; if this chain is correct, perturbing MAX will alter the allele-dependent effect on TERT expression, though the direction of the expression change is not established.

Falsified if: A sufficiently sensitive allele-specific assay finds no greater MAX binding to alt A.; MAX perturbation does not alter any allele-dependent effect on TERT expression in relevant cells.

### 3. H3: Speculative JUN-mediated effect at the TERT promoter (p = 0.03)

TF JUN (QBiC-SELEX coverage own_model), ref allele binds more; element Promoter-like cCRE EH38E3622530; gene TERT; cell type Glioblastoma cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The testable prediction is that JUN binds ref G more strongly than alt A, but the supplied evidence gives no allele-specific binding direction or QBiC-SELEX result; JUN is expressed and has site-overlapping peaks only in other biosamples, so its occupancy in glioblastoma is unconfirmed. | missing | [E04](#e04), [E06](#e06), [E17](#e17) |
| element | The variant lies in a promoter-like cCRE with active chromatin marks reported across ENCODE biosamples, although activity in glioblastoma is not established. | supported | [E03](#e03) |
| gene | The variant is annotated upstream of TERT and at its transcription start site, but this positional evidence does not demonstrate that the cCRE regulates TERT. | supported | [E01](#e01), [E02](#e02) |
| cell_type | Glioblastoma is the supplied expression context, but no matching-biosample JUN occupancy evidence is reported. | supported | [E04](#e04), [E06](#e06), [E17](#e17) |
| phenotype | A TERT regulatory effect could be relevant to glioblastoma, where TERT promoter mutations are common, but these sources do not establish a JUN-mediated effect of this variant or a disease effect in this case. | weak | [E15e](#e15e), [E15h](#e15h) |

Predictions: Compared with ref G, alt A will show reduced JUN binding; if this chain is correct, perturbing JUN will alter the allele-dependent effect on TERT expression, though the direction of the expression change is not established.

Falsified if: A sufficiently sensitive allele-specific assay finds no greater JUN binding to ref G.; JUN perturbation does not alter any allele-dependent effect on TERT expression in relevant cells.

## Prediction matrix

| Test | Cost | Separates top two | H1 | H2 | H3 |
| --- | --- | --- | --- | --- | --- |
| Compare ref G and alt A probes in an electrophoretic mobility-shift assay using glioblastoma nuclear extract, with MAX- and JUN-specific supershift or depletion controls. | low | yes | No reproducible allele-specific MAX- or JUN-containing complex. | A MAX-containing complex binds the alt A probe more strongly than the ref G probe. | A JUN-containing complex binds the ref G probe more strongly than the alt A probe. |
| In a glioblastoma model, compare allele-specific MAX and JUN occupancy and TERT expression after editing the variant; perturb the candidate TF to test whether any expression effect depends on it. | high | yes | No reproducible allele-specific occupancy or TF-dependent TERT-expression effect. | Greater MAX occupancy on alt A and an allele-dependent TERT-expression effect that changes with MAX perturbation; the expression direction is not specified. | Greater JUN occupancy on ref G and an allele-dependent TERT-expression effect that changes with JUN perturbation; the expression direction is not specified. |

## Next experiment

Run the low-cost allele-specific EMSA with glioblastoma nuclear extract and MAX/JUN supershift or depletion controls. It directly tests the predicted MAX binding difference separating the two highest-probability chains, while also checking the JUN alternative; a positive binding result would still need follow-up to establish an effect on TERT expression.

## Investigate calls

- chip_peaks({"tf": "MAX", "biosample": "Glioblastoma"})
- chip_peaks({"tf": "JUN", "biosample": "Glioblastoma"})
- chip_peaks({"tf": "EGR1", "biosample": "Glioblastoma"})

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

<a id="e16"></a>**E16** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-26T13:20:00+00:00)

> No ENCODE MAX ChIP-seq peak contains chr5:1295113:G>A in biosamples matching 'Glioblastoma'. Absence can also mean no MAX experiment in that biosample. In other biosamples, 13 MAX peaks do contain the variant: A549, HCT116, HepG2, Ishikawa, K562, MCF-7, NB4, SK-N-SH (experiments ENCSR000BLP, ENCSR000BSH, ENCSR000BTJ, ENCSR000BTM, ENCSR000BTY, ENCSR000BUL).

<a id="e17"></a>**E17** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-26T20:17:58+00:00)

> No ENCODE JUN ChIP-seq peak contains chr5:1295113:G>A in biosamples matching 'Glioblastoma'. Absence can also mean no JUN experiment in that biosample. In other biosamples, 11 JUN peaks do contain the variant: A549 (experiments ENCSR022WVP, ENCSR110UPH, ENCSR192PBJ, ENCSR604CKQ, ENCSR628MQN, ENCSR708DGM).

<a id="e18"></a>**E18** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-26T20:17:58+00:00)

> No ENCODE EGR1 ChIP-seq peak contains chr5:1295113:G>A in biosamples matching 'Glioblastoma'. Absence can also mean no EGR1 experiment in that biosample. In other biosamples, 3 EGR1 peaks do contain the variant: HepG2, Ishikawa, K562 (experiments ENCSR000BNE, ENCSR000BSQ, ENCSR026GSW).
