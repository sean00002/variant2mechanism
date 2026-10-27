# TERT promoter C250T and Glioblastoma, melanoma, bladder

Configuration `no_qbic`, masked mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.02 over 8 model calls; 101 s.

Variant `chr5:1295135:G>A` (somatic); expression context: DepMap:subtype=Glioblastoma (median of 54 lines).

## Ranked chains

### 1. GABPA_alt_gain: Alt allele strengthens a GABPA site at the TERT promoter (p = 0.58)

TF GABPA (QBiC-SELEX coverage own_model), alt allele binds more; element The variant lies in the promoter-like cCRE EH38E3622530 with H3K27ac and H3K4me3 across ENCODE biosamples, consistent with an active TERT promoter element; glioblastoma-specific activity is not directly proven.; gene TERT; cell type Glioblastoma is the expression context; TERT promoter mutations are reported in CNS tumors including glioblastoma, but direct GABPA occupancy in glioblastoma is not shown by ENCODE here..

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | GABPA is the best-supported TF: TERT promoter mutations create a de novo ETS motif, and the GABP tetramer is reported to activate mutant TERT promoters. GABPB1, a GABP co-factor, is ChIP-bound at this element, and GABPA is expressed in glioblastoma and has ENCODE peaks containing the variant in other biosamples. No QBiC-SELEX model or allele-effect data are provided for GABPA in this case. Hypothesis: the alt A allele creates/strengthens a GABPA site and binds GABPA more strongly than ref G. | weak | [E04](#e04), [E11](#e11), [E18a](#e18a), [E18b](#e18b), [E18d](#e18d), [E18f](#e18f) |
| element | The variant sits in a promoter-like cCRE at the TERT upstream promoter, so an allele-specific GABPA change could alter promoter activity. | supported | [E01](#e01), [E03](#e03) |
| gene | The variant is 0 kb from the TERT TSS, making TERT the most direct target gene. | supported | [E02](#e02) |
| cell_type | Glioblastoma is the stated expression context and TERT promoter mutations are found in CNS tumors including glioblastoma; however, glioblastoma-specific GABPA occupancy is not established by the ENCODE data here. | weak | [E15](#e15), [E18g](#e18g) |
| phenotype | If alt A increases GABPA binding and GABP activates the mutant TERT promoter, this would raise TERT transcription/telomerase and contribute to tumor biology. | weak | [E18b](#e18b), [E18c](#e18c), [E18f](#e18f) |

Predictions: Allele-specific GABPA EMSA/ChIP or reporter assays will show higher GABPA occupancy/activity for alt A than ref G.; GABPA or GABPB1 knockdown should reduce TERT expression preferentially when the alt allele is present.; The alt allele should create or strengthen an ETS/GABPA motif at this position.

Falsified if: Allele-specific GABPA binding assays in glioblastoma cells show no alt/ref difference or show the opposite direction.; Glioblastoma ChIP shows no GABPA occupancy at this element.; GABPA knockdown or mutation does not change TERT expression in the relevant context.; Allele-specific reporter assays show no alt/ref difference or show the opposite direction.

### 2. null_no_tf_mediated_effect: No TF-mediated effect of this variant (p = 0.34)

Null chain: no TF-mediated effect of this variant.

Predictions: No TF-mediated allelic effect at chr5:1295135:G>A; disease association is explained by a linked causal variant, a passenger mutation, or no allelic effect.; TF ChIP peaks containing the variant in other biosamples do not demonstrate occupancy or allele-specific function in the glioblastoma expression context.; Reporter assays would not show an allele-specific effect attributable to this single base.

Falsified if: Allele-specific TF ChIP, EMSA, or reporter assays in glioblastoma cells show reproducible differential binding/activity for this exact base.; A valid QBiC-SELEX or equivalent assay shows a clear allele effect for a TF that is occupied at this element in the relevant cell type.

### 3. MAX_alt_gain: Alt allele strengthens a MAX site at the TERT promoter (p = 0.05)

TF MAX (QBiC-SELEX coverage own_model), alt allele binds more; element The variant is in the active TERT promoter PLS EH38E3622530 across ENCODE biosamples, where a MAX site could affect promoter output; glioblastoma-specific activity is not directly proven.; gene TERT; cell type Glioblastoma is the expression context, but no glioblastoma-specific MAX occupancy at this element is shown..

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | MAX is a weaker candidate: it is expressed in glioblastoma and has ENCODE ChIP peaks containing this variant in other biosamples, but no matching glioblastoma occupancy is shown and no QBiC-SELEX model or allele-effect data are provided for MAX in this case. Hypothesis: alt A creates/strengthens an E-box-like MAX site and binds MAX more strongly than ref G. | weak | [E04](#e04), [E05](#e05) |
| element | The variant lies in a promoter-like cCRE at the TERT promoter, so allele-specific MAX binding could change promoter activity. | supported | [E01](#e01), [E03](#e03) |
| gene | TERT is the nearest gene, with its TSS 0 kb away. | supported | [E02](#e02) |
| cell_type | Glioblastoma is the expression context, and TERT is implicated in glioblastoma and melanoma; direct MAX regulation of TERT here is not established. | weak | [E15](#e15) |
| phenotype | If alt A increases MAX binding and MAX acts as an activator in this context, TERT promoter output would increase. | missing | [E15](#e15) |

Predictions: Allele-specific MAX EMSA/ChIP or reporter assays will show higher MAX occupancy/activity for alt A than ref G.; The alt allele should create or strengthen a MAX-compatible motif.; MAX perturbation should alter TERT expression in an allele-dependent manner.

Falsified if: No allele-specific MAX occupancy at the variant in glioblastoma cells.; Reporter assays show no alt/ref difference or the opposite direction.; MAX knockdown does not affect TERT in the relevant context.; QBiC-SELEX or equivalent shows no MAX allele effect.

### 4. JUN_alt_gain: Alt allele strengthens a JUN site at the TERT promoter (p = 0.03)

TF JUN (QBiC-SELEX coverage own_model), alt allele binds more; element The variant is within the TERT promoter PLS EH38E3622530 across ENCODE biosamples, where AP-1 occupancy could affect TERT transcription; glioblastoma-specific activity is not directly proven.; gene TERT; cell type Glioblastoma is the expression context, but no glioblastoma-specific JUN occupancy at this element is shown..

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | JUN is a weaker candidate: it is expressed in glioblastoma and has ENCODE ChIP peaks containing this variant in other biosamples, but no matching glioblastoma occupancy is shown and no QBiC-SELEX model or allele-effect data are provided for JUN in this case. Hypothesis: alt A creates/strengthens an AP-1-like JUN site and binds JUN more strongly than ref G. | weak | [E04](#e04), [E06](#e06) |
| element | The variant lies in the active TERT promoter cCRE EH38E3622530 across ENCODE biosamples, so an allele-specific AP-1/JUN site could alter promoter activity. | supported | [E01](#e01), [E03](#e03) |
| gene | TERT is the nearest gene and is 0 kb from the variant. | supported | [E02](#e02) |
| cell_type | Glioblastoma is the expression context, and TERT is implicated in glioblastoma and melanoma; direct JUN regulation of TERT here is not established. | weak | [E15](#e15) |
| phenotype | If alt A increases JUN binding and JUN activates TERT, this would raise TERT promoter output/telomerase. | missing | [E15](#e15) |

Predictions: Allele-specific JUN EMSA/ChIP or reporter assays will show higher JUN occupancy/activity for alt A than ref G.; The alt allele should create or strengthen an AP-1/JUN-compatible motif.; JUN perturbation should alter TERT expression in an allele-dependent manner.

Falsified if: No allele-specific JUN occupancy at the variant in glioblastoma cells.; Reporter assays show no alt/ref difference or the opposite direction.; JUN knockdown does not affect TERT in the relevant context.; QBiC-SELEX or equivalent shows no JUN allele effect.

## Prediction matrix

| Test | Cost | Separates top two | GABPA_alt_gain | null_no_tf_mediated_effect | MAX_alt_gain | JUN_alt_gain |
| --- | --- | --- | --- | --- | --- | --- |
| Allele-specific EMSA with GABPA/GABPB1 complex on ref vs alt oligos | low | yes | Alt A binds GABPA more strongly than ref G. | No difference between ref G and alt A. | No GABPA allele-specific difference expected; MAX effect would require a separate assay. | No GABPA allele-specific difference expected; JUN effect would require a separate assay. |
| Allele-specific TERT promoter reporter assay in glioblastoma cells with GABPA/GABPB1 knockdown | medium | yes | Alt A increases TERT reporter activity; GABPA/GABPB1 knockdown reduces the alt-specific increase. | No allele-specific TERT reporter activity. | Alt A may increase reporter activity, but MAX knockdown, not GABPA knockdown, would reduce it. | Alt A may increase reporter activity, but JUN knockdown, not GABPA knockdown, would reduce it. |
| Allele-specific MAX ChIP or EMSA at the variant | medium | no | No MAX allele-specific effect required. | No allele-specific MAX occupancy. | Alt A shows higher MAX occupancy. | No MAX allele-specific effect required. |
| Allele-specific JUN ChIP or EMSA at the variant | medium | no | No JUN allele-specific effect required. | No allele-specific JUN occupancy. | No JUN allele-specific effect required. | Alt A shows higher JUN occupancy. |

## Next experiment

Allele-specific EMSA with GABPA/GABPB1 complex on ref vs alt oligos; it is the cheapest direct test of the top GABPA chain versus the null because it distinguishes alt-specific GABPA binding from no allelic effect without requiring glioblastoma ChIP.

## Investigate calls

- chip_peaks({"tf": "GABPA", "biosample": null})
- eqtl_lookup({"tissue": null})
- literature_search({"query": "TERT promoter mutation creates ETS GABPA binding site gain of function glioblastoma"})

## Flags

- quote_rejected: PMID 41744838: not an exact substring of the abstract

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

<a id="e16"></a>**E16** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-25T17:27:26+00:00)

> 2 ENCODE GABPA ChIP-seq peaks contain chr5:1295135:G>A: biosamples HepG2, SK-N-SH; experiments ENCSR000BJK, ENCSR000BTG.

<a id="e17"></a>**E17** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr5_1295135_G_A_b38&datasetId=gtex_v8; retrieved 2026-10-26T20:17:52+00:00)

> 0 significant GTEx v8 single-tissue eQTLs for chr5_1295135_G_A_b38. NES is the effect of the alt allele (A) relative to ref (G).

<a id="e18"></a>**E18** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TERT%20promoter%20mutation%20creates%20ETS%20GABPA%20binding%20site%20gain%20of%20function%20glioblastoma&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T20:17:53+00:00)

> Europe PMC: 15 hits for 'TERT promoter mutation creates ETS GABPA binding site gain of function glioblastoma'; top 8 with PMIDs:
> PMID 40513567 (2025): The immortality mechanism of TERT promoter mutant cancers is self-reinforcing and reversible.
> PMID 41155227 (2025): From Transcription Factors Dysregulation to Malignancy: In Silico Reconstruction of Cancer's Foundational Drivers-The Eternity Triangle.
> PMID 41776093 (2026): Unrevealing the dual role of paired box and sex determining region Y related high mobility group box in glioblastoma.
> PMID 35568649 (2022): Emerging mechanisms of telomerase reactivation in cancer.
> PMID 33178776 (2020): Telomerase reverse transcriptase promoter mutations in thyroid carcinomas: implications in precision oncology-a narrative review.
> PMID 32981294 (2020): Mechanisms of TERT Reactivation and Its Interaction with BRAFV600E.
> PMID 32226942 (2020): &lt;i&gt;TERT&lt;/i&gt;, a promoter of CNS malignancies.
> PMID 33599797 (2021): Non-canonical roles of canonical telomere binding proteins in cancers.

<a id="e18a"></a>**E18a** literature_search, Europe PMC abstract, PMID 40513567 (https://europepmc.org/article/MED/40513567; retrieved 2026-10-26T20:17:53+00:00)

> TERT promoter (TERTp) mutations create a de novo E26 transformation-specific (ETS) transcription factor binding motif.

<a id="e18b"></a>**E18b** literature_search, Europe PMC abstract, PMID 40513567 (https://europepmc.org/article/MED/40513567; retrieved 2026-10-26T20:17:53+00:00)

> Here, we analyzed 53 cell lines representing 16 cancer types and 6 recurrent TERTp mutations and found that the GA-binding protein (GABP) tetramer is responsible for promoter activation in all cases.

<a id="e18c"></a>**E18c** literature_search, Europe PMC abstract, PMID 35568649 (https://europepmc.org/article/MED/35568649; retrieved 2026-10-26T20:17:53+00:00)

> Mutations in the promoter of human telomerase reverse transcriptase (hTERT) result in hyperactivation of hTERT.

<a id="e18d"></a>**E18d** literature_search, Europe PMC abstract, PMID 35568649 (https://europepmc.org/article/MED/35568649; retrieved 2026-10-26T20:17:53+00:00)

> Initially, the mutations were understood to reactivate hTERT by generating novel E26 transformation-specific (ETS) binding sites.

<a id="e18e"></a>**E18e** literature_search, Europe PMC abstract, PMID 33178776 (https://europepmc.org/article/MED/33178776; retrieved 2026-10-26T20:17:53+00:00)

> The TERT promoter's gain-of-function mutation has recently been identified in TCs and many other malignancies.

<a id="e18f"></a>**E18f** literature_search, Europe PMC abstract, PMID 33178776 (https://europepmc.org/article/MED/33178776; retrieved 2026-10-26T20:17:53+00:00)

> The mutation creates a de novo ETS-binding motif through which TERT transcription is de-repressed and telomerase is activated; through this, the mutant TERT promoter promotes the development of TC, contributes to disease aggressiveness and treatment resistance, and thereby leads to poor patient outcomes.

<a id="e18g"></a>**E18g** literature_search, Europe PMC abstract, PMID 32226942 (https://europepmc.org/article/MED/32226942; retrieved 2026-10-26T20:17:53+00:00)

> TERT promoter mutations, which result in the upregulation of TERT transcription, have been identified in several central nervous system (CNS) tumors, including meningiomas, medulloblastomas, and primary glial neoplasms.
