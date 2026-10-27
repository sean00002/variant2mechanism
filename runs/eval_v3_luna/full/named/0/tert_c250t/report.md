# TERT promoter C250T and Glioblastoma, melanoma, bladder

Configuration `full`, named mode, seed 0. Models: generator openai/gpt-6-luna, critic openai/gpt-6-luna, summariser openai/gpt-6-luna. Cost $0.02 over 8 model calls; 200 s.

Variant `chr5:1295135:G>A` (somatic); expression context: DepMap:subtype=Glioblastoma (median of 54 lines).

## QBiC-SELEX screen (occupancy first)

Occupied candidates: GABPA (bound elsewhere, z 167.5); KLF12 (bound elsewhere, z -15.38); NR2C1 (bound elsewhere, z 15.31); TGIF2 (bound elsewhere, z -12.19); ZNF143 (bound elsewhere, z -11.71); ZBTB7A (bound elsewhere, z -10.91); SP2 (bound elsewhere, z -9.83); EGR1 (bound elsewhere, z -8.0); BHLHE40 (bound elsewhere, z -7.34); E2F4 (bound elsewhere, z -5.4). Occupancy unknown: ETV2 (z 167.5); ETV3 (z 167.5); FLI1 (z 167.5); ZNF92 (z -33.21); EBF4 (z -24.35). Diagnostic, not shown to the model: 477 of 997 models pass Bonferroni.

## Ranked chains

### 1. H0: No TF-mediated effect of this variant (p = 0.58)

Null chain: no TF-mediated effect of this variant.

Predictions: Editing this base alone will not produce a reproducible TF-dependent change in TERT output in relevant cells.; The variant may be a passenger, may act through a mechanism not mediated by allele-specific TF binding, or may have no measurable effect.

Falsified if: Isogenic editing produces a reproducible allele-dependent TERT effect that is accompanied by differential occupancy of a specific TF and is reduced by perturbing that TF.

### 2. H1: Alt-allele gain of GABPA binding alters TERT promoter output (p = 0.20)

TF GABPA (QBiC-SELEX coverage own_model), alt allele binds more; element TERT promoter-like cCRE EH38E3622530; gene TERT; cell type Glioblastoma.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | QBiC-SELEX predicts stronger binding to the alt allele using an ETV5-mapped ETS model, not a GABPA-specific model. GABPA has variant-overlapping ChIP peaks only in other biosamples; the shared ETS prediction also applies to ETV2, ETV3, and FLI1, so the evidence does not identify GABPA as the changing factor. | weak | [E04](#e04), [E11](#e11), [E17](#e17), [E27](#e27), [E28](#e28), [E29](#e29), [E32](#e32) |
| element | The variant lies in a promoter-like cCRE with activity-associated signals in ENCODE biosamples, but the reported maxima do not establish activity in glioblastoma cells. | supported | [E03](#e03) |
| gene | The variant is in the TERT promoter region at the TERT transcription start site. | supported | [E01](#e01), [E02](#e02) |
| cell_type | GABPA is expressed in the glioblastoma DepMap context, but occupancy at this site in that context has not been demonstrated. | supported | [E04](#e04), [E11](#e11), [E17](#e17), [E32](#e32) |
| phenotype | This model proposes that the alt-allele binding gain changes TERT promoter output; increased TERT transcription could contribute to tumor-associated telomerase activity. General literature supports increased transcription from TERT promoter mutations, but does not establish this variant's effect, its TF mechanism, or a disease effect, particularly in bladder cancer. | weak | [E15a](#e15a), [E15e](#e15e), [E15h](#e15h), [E34g](#e34g), [E34h](#e34h) |

Predictions: In relevant glioblastoma cells, the alt allele should show greater GABPA occupancy than the ref allele.; If GABPA is the causal factor and acts to increase promoter output here, editing to the alt allele should increase TERT transcription, and GABPA perturbation should diminish that allele-dependent effect.

Falsified if: A relevant-cell assay finds no alt-biased GABPA occupancy, while detecting the candidate factor's occupancy adequately.; Isogenic editing shows no reproducible TERT output difference, or any difference is unaffected by GABPA perturbation.

### 3. H3: Loss of ref-favored TGIF2 binding changes TERT promoter output (p = 0.12)

TF TGIF2 (QBiC-SELEX coverage own_model), ref allele binds more; element TERT promoter-like cCRE EH38E3622530; gene TERT; cell type Glioblastoma.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | QBiC-SELEX predicts stronger binding to the ref allele using a PKNOX2-mapped homeodomain model, not a TGIF2-specific model. TGIF2 has a variant-overlapping ChIP peak only in another biosample, so occupancy and the predicted allele effect are unconfirmed in glioblastoma. | weak | [E04](#e04), [E20](#e20), [E33](#e33) |
| element | The variant lies in a promoter-like cCRE with activity-associated signals in ENCODE biosamples, but glioblastoma-specific activity is not established. | supported | [E03](#e03) |
| gene | The variant is in the TERT promoter region at the TERT transcription start site. | supported | [E01](#e01), [E02](#e02) |
| cell_type | TGIF2 is expressed in the glioblastoma DepMap context, but the available variant-overlapping ChIP evidence is from HepG2, not glioblastoma. | supported | [E04](#e04), [E20](#e20), [E33](#e33) |
| phenotype | This model proposes that reduced TGIF2 binding on the alt allele changes TERT promoter output. A repressive role for TGIF2 at this site is an untested assumption; general TERT promoter literature does not establish a TGIF2-mediated or disease effect for this variant. | weak | [E15a](#e15a), [E15e](#e15e), [E15h](#e15h), [E34g](#e34g), [E34h](#e34h) |

Predictions: If TGIF2 occupies this site in relevant glioblastoma cells, occupancy should be greater on the ref allele.; If TGIF2 represses TERT here, the alt allele should increase TERT output and TGIF2 perturbation should reduce the allele-dependent difference.

Falsified if: A relevant-cell assay finds no ref-biased TGIF2 occupancy, while detecting TGIF2 occupancy adequately.; TGIF2 perturbation does not affect an allele-dependent TERT output difference, or the direction of the output change contradicts the proposed repressive model.

### 4. H4: Loss of ref-favored ZNF143 binding changes TERT promoter output (p = 0.10)

TF ZNF143 (QBiC-SELEX coverage own_model), ref allele binds more; element TERT promoter-like cCRE EH38E3622530; gene TERT; cell type Glioblastoma.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | QBiC-SELEX, using a ZNF143-specific model, predicts stronger binding to the ref allele. ZNF143 has a variant-overlapping ChIP peak in GM12878, but occupancy in glioblastoma is not shown. | weak | [E04](#e04), [E14](#e14), [E21](#e21) |
| element | The variant lies in a promoter-like cCRE with activity-associated signals in ENCODE biosamples, but glioblastoma-specific activity is not established. | supported | [E03](#e03) |
| gene | The variant is in the TERT promoter region at the TERT transcription start site. | supported | [E01](#e01), [E02](#e02) |
| cell_type | ZNF143 is expressed in the glioblastoma DepMap context, but the variant-overlapping ChIP evidence is from GM12878 rather than glioblastoma. | supported | [E04](#e04), [E14](#e14), [E21](#e21) |
| phenotype | This model proposes that reduced ZNF143 binding on the alt allele changes TERT promoter output. Whether ZNF143 activates or represses TERT at this site is not established, and the general TERT promoter literature does not demonstrate a ZNF143-mediated or disease effect for this variant. | weak | [E15a](#e15a), [E15e](#e15e), [E15h](#e15h), [E34g](#e34g), [E34h](#e34h) |

Predictions: In relevant glioblastoma cells, ZNF143 occupancy should be greater on the ref allele.; The allele-dependent TERT output change should depend on ZNF143; its direction cannot be predicted from the supplied evidence because ZNF143's regulatory role at this site is unknown.

Falsified if: A relevant-cell assay finds no ref-biased ZNF143 occupancy, while detecting ZNF143 occupancy adequately.; ZNF143 perturbation leaves any allele-dependent TERT output effect unchanged.

## Prediction matrix

| Test | Cost | Separates top two | H0 | H1 | H3 | H4 |
| --- | --- | --- | --- | --- | --- | --- |
| Allele-resolved CUT&RUN or CUT&Tag for GABPA, TGIF2, and ZNF143 in a relevant glioblastoma model. | medium | yes | No reproducible candidate-specific allele-biased occupancy consistent with a TF-mediated effect. | Greater GABPA occupancy on the alt allele. | Greater TGIF2 occupancy on the ref allele. | Greater ZNF143 occupancy on the ref allele. |
| Isogenic editing of the promoter allele in glioblastoma cells, followed by TERT nascent-RNA measurement with acute perturbation of the candidate TFs. | high | yes | No reproducible allele-dependent TERT change that depends on one of the candidate TFs. | An allele-dependent TERT change that is diminished by GABPA perturbation; an increase is predicted only if GABPA is activating here. | An allele-dependent TERT change that is diminished by TGIF2 perturbation; increased output requires the proposed, unproven repressive role. | An allele-dependent TERT change that is diminished by ZNF143 perturbation; the direction is not specified by the current evidence. |
| Allele-specific TERT promoter reporter assay in glioblastoma cells, with candidate-TF perturbation. | medium | yes | No reproducible allele-dependent reporter effect that depends on a candidate TF. | An alt-versus-ref reporter difference that is reduced by GABPA perturbation. | An alt-versus-ref reporter difference that is reduced by TGIF2 perturbation. | An alt-versus-ref reporter difference that is reduced by ZNF143 perturbation. |

## Next experiment

The cheapest direct discriminator for the top two hypotheses (H0 and H1) is allele-resolved GABPA CUT&RUN or CUT&Tag in a relevant glioblastoma model. H1 predicts greater GABPA occupancy on the alt allele; H0 predicts no reproducible TF-mediated allelic occupancy effect. A positive occupancy result would still need functional follow-up to establish an effect on TERT output.

## Investigate calls

- chip_peaks({"tf": "GABPA", "biosample": "Glioblastoma"})
- chip_peaks({"tf": "TGIF2", "biosample": "Glioblastoma"})
- literature_search({"query": "TERT promoter C250T glioblastoma reporter assay allele-specific expression TERT"})

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

> No ENCODE GABPA ChIP-seq peak contains chr5:1295135:G>A in biosamples matching 'Glioblastoma'. Absence can also mean no GABPA experiment in that biosample. In other biosamples, 2 GABPA peaks do contain the variant: HepG2, SK-N-SH (experiments ENCSR000BJK, ENCSR000BTG).

<a id="e33"></a>**E33** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-26T13:33:05+00:00)

> No ENCODE TGIF2 ChIP-seq peak contains chr5:1295135:G>A in biosamples matching 'Glioblastoma'. Absence can also mean no TGIF2 experiment in that biosample. In other biosamples, 1 TGIF2 peaks do contain the variant: HepG2 (experiments ENCSR993LMB).

<a id="e34"></a>**E34** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TERT%20promoter%20C250T%20glioblastoma%20reporter%20assay%20allele-specific%20expression%20TERT&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T13:33:05+00:00)

> Europe PMC: 44 hits for 'TERT promoter C250T glioblastoma reporter assay allele-specific expression TERT'; top 8 with PMIDs:
> PMID 42088607 (2026): Sensitive detection of somatic mutations in GC-rich cancer gene promoters.
> PMID 40822359 (2025): AURKB and PI3K/AKT/mTOR pathways converge to regulate &lt;i&gt;TERT&lt;/i&gt; expression.
> PMID 40594127 (2025): Comparison of genetic mutations in bladder cancers that arose following radiotherapy for prostate cancer with those in primary bladder cancers.
> PMID 40075591 (2025): Clinical Impact of a Next-Generation Sequencing Approach for Glioblastoma Patients.
> PMID 38398126 (2024): The C250T Mutation of <i>TERTp</i> Might Grant a Better Prognosis to Glioblastoma by Exerting Less Biological Effect on Telomeres and Chromosomes Than the C228T Mutation.
> PMID 37920169 (2023): Successes and challenges in modeling heterogeneous BRAF<sup>V600E</sup> mutated central nervous system neoplasms.
> PMID 34944589 (2021): <i>TERT</i> Promoter Mutations Increase Sense and Antisense Transcription from the <i>TERT</i> Promoter.
> PMID 35372034 (2022): A Custom DNA-Based NGS Panel for the Molecular Characterization of Patients With Diffuse Gliomas: Diagnostic and Therapeutic Applications.

<a id="e34a"></a>**E34a** literature_search, Europe PMC abstract, PMID 42088607 (https://europepmc.org/article/MED/42088607; retrieved 2026-10-26T13:33:05+00:00)

> Only a relatively small number of somatic noncoding mutations that are likely drivers have been described to date, including those in the promoters of the TERT, FOXA1, and TP53 genes.

<a id="e34b"></a>**E34b** literature_search, Europe PMC abstract, PMID 42088607 (https://europepmc.org/article/MED/42088607; retrieved 2026-10-26T13:33:05+00:00)

> The impact of these alterations can be profound by initiating, increasing, or abolishing gene expression.

<a id="e34c"></a>**E34c** literature_search, Europe PMC abstract, PMID 40822359 (https://europepmc.org/article/MED/40822359; retrieved 2026-10-26T13:33:05+00:00)

> Here, we identified previously uncharacterized pathways regulating TERTp MUT activity by inserting a luciferase reporter downstream of TERTp MUT in SW1736 anaplastic thyroid cancer cells via CRISPR-Cas9, generating SW1736TERT/LUC, and screening a 218-kinase inhibitor library.

<a id="e34d"></a>**E34d** literature_search, Europe PMC abstract, PMID 40822359 (https://europepmc.org/article/MED/40822359; retrieved 2026-10-26T13:33:05+00:00)

> Specifically, AURKB, via REST, is recruited to TERTp MUT by TRIM28.

<a id="e34e"></a>**E34e** literature_search, Europe PMC abstract, PMID 38398126 (https://europepmc.org/article/MED/38398126; retrieved 2026-10-26T13:33:05+00:00)

> Progression-free survival (mPFS) was 9.1 months for those with the C250T mutation and 7 months for those with either the C228T mutation or TERTp-wt (p = 0.016).

<a id="e34f"></a>**E34f** literature_search, Europe PMC abstract, PMID 38398126 (https://europepmc.org/article/MED/38398126; retrieved 2026-10-26T13:33:05+00:00)

> In our series, patients exhibiting the C250T mutation had a more favorable prognosis compared to those with either TERPp-wt or TERTp C228T mutations.

<a id="e34g"></a>**E34g** literature_search, Europe PMC abstract, PMID 34944589 (https://europepmc.org/article/MED/34944589; retrieved 2026-10-26T13:33:05+00:00)

> The two main TERT promoter mutations are C>T transitions located -146C>T and -124C>T upstream from the translational start site.

<a id="e34h"></a>**E34h** literature_search, Europe PMC abstract, PMID 34944589 (https://europepmc.org/article/MED/34944589; retrieved 2026-10-26T13:33:05+00:00)

> Both mutations generally increased TERT transcription by 2-4-fold regardless of upstream and downstream regulatory elements.

<a id="e34i"></a>**E34i** literature_search, Europe PMC abstract, PMID 35372034 (https://europepmc.org/article/MED/35372034; retrieved 2026-10-26T13:33:05+00:00)

> Specifically, the Glio-DNA panel targets specific genetic and chromosomal alterations involving ATRX chromatin remodeler (ATRX), cyclin dependent kinase inhibitor 2A (CDKN2A), isocitrate dehydrogenase (NADP+) 1 (IDH1) and the telomerase reverse transcriptase (TERT) promoter while also recognizing the co-deletion of 1p/19q, loss of chromosome 10 and gain of chromosome 7.

<a id="e34j"></a>**E34j** literature_search, Europe PMC abstract, PMID 35372034 (https://europepmc.org/article/MED/35372034; retrieved 2026-10-26T13:33:05+00:00)

> In conclusion, our analysis demonstrates NGS efficacy in simultaneously detecting different genetic alterations useful for the diagnosis, prognosis and treatment of adult patients with diffuse glioma.
