# rs73706717 and Colorectal cancer (8q24)

Configuration `full`, named mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.04 over 8 model calls; 137 s.

Variant `chr8:127401265:T>C` (germline); expression context: DepMap:ACH-000971 (HCT 116).

## QBiC-SELEX screen (occupancy first)

Occupied candidates: TCF7L2 (bound here, z -8.8); SP1 (bound here, z -7.07); NFIC (bound elsewhere, z 24.28); NFIA (bound elsewhere, z 24.28); HNF1B (bound elsewhere, z -23.93); NR2F2 (bound elsewhere, z -15.02); NR2F6 (bound elsewhere, z -15.02); NR2C2 (bound elsewhere, z -15.02); RXRB (bound elsewhere, z -13.82); NR3C1 (bound elsewhere, z -12.32). Occupancy unknown: ZBTB22 (z -33.75); NR1H3 (z -15.02); TET3 (z 14.12); NR1D2 (z -13.82); NR4A2 (z -13.82). Diagnostic, not shown to the model: 307 of 997 models pass Bonferroni.

## Ranked chains

### 1. null: No TF-mediated effect of this variant (p = 0.45)

Null chain: no TF-mediated effect of this variant.

Predictions: No TF-mediated allele-specific effect at rs73706717 after controlling for linked variants.; Any disease signal at 8q24 is driven by another variant or haplotype, not this base.; POU5F1B or MYC expression is not reproducibly affected by the T>C change in HCT116.

Falsified if: Allele-specific TF ChIP or reporter assays show a reproducible difference between T and C at rs73706717 in HCT116.; A linked variant is excluded and rs73706717 itself changes target-gene expression or enhancer activity.

### 2. TCF7L2_ref: TCF7L2 ref-preferred binding at an 8q24 enhancer (p = 0.30)

TF TCF7L2 (QBiC-SELEX coverage mapped), ref allele binds more; element pELS enhancer EH38E3858447; gene POU5F1B; cell type HCT116 colorectal carcinoma.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | TCF7L2 is the strongest TF candidate: it occupies the variant in HCT116 ChIP-seq and is highly expressed, and QBiC-SELEX reports ref-preferred binding (effect -0.429, z -8.8); however the QBiC model is CIS-BP-mapped TCF7, not a TCF7L2 own model, and bulk ChIP does not prove allele-specific occupancy. | weak | [E05](#e05), [E20](#e20) |
| element | rs73706717 lies in the active proximal enhancer-like cCRE EH38E3858447 marked by DNase, H3K27ac, and TF occupancy, although the cCRE z-scores are maxima across ENCODE biosamples rather than HCT116-specific. | supported | [E01](#e01), [E03](#e03), [E04](#e04) |
| gene | POU5F1B is the nearest protein-coding gene and the best L2G gene in the supplied credible sets, but those sets are for non-CRC traits with low PIP, no GTEx eQTL links this base to POU5F1B, and MYC is a farther but known 8q24 CRC oncogene, so target assignment is uncertain. | weak | [E02](#e02), [E16](#e16), [E17](#e17), [E18](#e18) |
| cell_type | HCT116 is the matching colorectal carcinoma biosample; TCF7L2 is expressed at 63.61 TPM and HCT116 ChIP-seq peaks contain the variant. | supported | [E04](#e04), [E05](#e05) |
| phenotype | A TCF7L2-dependent enhancer change could alter 8q24 target expression in colorectal cells, but rs73706717 has no GWAS Catalog association and no colorectal-cancer genetic link is supplied, so the phenotype step is speculative. | missing | [E15](#e15), [E16](#e16), [E18](#e18) |

Predictions: The alt C allele reduces TCF7L2 binding at rs73706717.; If TCF7L2 activates this enhancer, alt C reduces target-gene expression in HCT116.; TCF7L2 knockdown should reduce enhancer activity if this element is TCF7L2-dependent.

Falsified if: Allele-specific TCF7L2 ChIP does not show ref>T occupancy at rs73706717 in HCT116.; Reporter assays show no differential enhancer activity between T and C alleles.; TCF7L2 knockdown or CRISPRi does not affect the relevant 8q24 target gene in HCT116.

### 3. SP1_ref: SP1 ref-preferred binding at the same enhancer (p = 0.17)

TF SP1 (QBiC-SELEX coverage own_model), ref allele binds more; element pELS enhancer EH38E3858447; gene POU5F1B; cell type HCT116 colorectal carcinoma.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | SP1 occupies the variant in HCT116 and is expressed, and QBiC-SELEX reports ref-preferred binding (effect -0.298, z -7.07); however the best QBiC model is CIS-BP-mapped SP3, not an SP1 own model, and ChIP does not prove allele-specific occupancy. | weak | [E06](#e06), [E21](#e21) |
| element | The variant is in the active pELS EH38E3858447, consistent with an SP1-bound regulatory element, though the cCRE annotation is not HCT116-specific. | supported | [E03](#e03), [E04](#e04) |
| gene | POU5F1B is nearest and top L2G in the supplied non-CRC credible sets, but there is no GTEx eQTL and no direct SP1-to-POU5F1B enhancer evidence, so the target-gene link is weak. | weak | [E02](#e02), [E16](#e16), [E17](#e17) |
| cell_type | HCT116 expresses SP1 at 38.96 TPM and has SP1 ChIP-seq peaks containing the variant. | supported | [E04](#e04), [E06](#e06) |
| phenotype | A change in SP1 occupancy at this 8q24 enhancer could alter colorectal-cell gene regulation, but no supplied evidence links rs73706717 or SP1 at this element to colorectal cancer. | missing | [E15](#e15), [E16](#e16), [E18](#e18) |

Predictions: The alt C allele reduces SP1 binding at rs73706717.; If SP1 activates this enhancer, alt C lowers target-gene expression in HCT116.; SP1 knockdown should reduce enhancer activity if SP1 is the functional factor.

Falsified if: Allele-specific SP1 ChIP does not show ref>T occupancy at rs73706717 in HCT116.; SP1 knockdown or CRISPRi does not affect enhancer activity or the relevant 8q24 target gene in HCT116.; The SP1 QBiC-SELEX effect is not replicated by direct binding assays for this site.

### 4. NFIC_alt: NFIC alt-preferred binding, occupancy not shown in colorectal cells (p = 0.08)

TF NFIC (QBiC-SELEX coverage own_model), alt allele binds more; element pELS enhancer EH38E3858447; gene POU5F1B; cell type HCT116 colorectal carcinoma, but occupancy evidence is from HepG2.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | NFIC is a QBiC-gated alt-preferred candidate (effect 1.783, z 24.28) and is expressed in HCT116, but the best model is CIS-BP-mapped NFIB and ENCODE ChIP-seq occupancy over the variant is only in HepG2, not HCT116; allele-specific occupancy is untested. | weak | [E22](#e22) |
| element | The variant lies in the active pELS EH38E3858447, so it could be an NFIC-responsive element, although the cCRE annotation is not HCT116-specific. | supported | [E03](#e03), [E04](#e04) |
| gene | POU5F1B is the nearest protein-coding gene and top L2G in non-CRC credible sets, but no eQTL or perturbation data link this base to POU5F1B. | weak | [E02](#e02), [E16](#e16), [E17](#e17) |
| cell_type | HCT116 expresses NFIC at 36.29 TPM but has no reported HCT116 ChIP peak at this variant; the observed occupancy is in HepG2, so the colorectal cell-type link is weak. | weak | [E04](#e04), [E22](#e22) |
| phenotype | An alt-preferred NFIC site could change 8q24 enhancer output, but there is no colorectal-cancer association for rs73706717 and no NFIC-specific CRC evidence in the supplied data. | missing | [E15](#e15), [E16](#e16), [E18](#e18) |

Predictions: The alt C allele increases NFIC binding at rs73706717.; If NFIC activates this enhancer, alt C raises target-gene expression in a permissive cell type.; NFIC knockdown should reduce enhancer activity only where NFIC occupies the element.

Falsified if: Allele-specific NFIC ChIP in a relevant cell type does not show alt>C occupancy at rs73706717.; NFIC has no occupancy at this element in colorectal cells.; Reporter assays show no NFIC-dependent allelic effect.

## Prediction matrix

| Test | Cost | Separates top two | null | TCF7L2_ref | SP1_ref | NFIC_alt |
| --- | --- | --- | --- | --- | --- | --- |
| Allele-specific TCF7L2 ChIP-qPCR (or ChIP with allele-specific primer extension) at rs73706717 in HCT116, comparing T and C alleles. | low | yes | No allele-specific TCF7L2 enrichment. | Ref T allele shows greater TCF7L2 ChIP enrichment than alt C. | No allele-specific TCF7L2 enrichment. | No allele-specific TCF7L2 enrichment. |
| Allele-specific SP1 ChIP-qPCR at rs73706717 in HCT116. | low | no | No allele-specific SP1 enrichment. | No allele-specific SP1 enrichment (TCF7L2 chain does not predict SP1 binding change). | Ref T allele shows greater SP1 ChIP enrichment than alt C. | No allele-specific SP1 enrichment. |
| Luciferase reporter carrying ~300 bp around rs73706717 with T vs C allele in HCT116. | medium | yes | No reproducible difference between T and C alleles. | Alt C allele lowers enhancer activity (assuming TCF7L2 is an activator). | Alt C allele lowers enhancer activity (assuming SP1 is an activator). | Alt C allele raises enhancer activity (assuming NFIC is an activator). |
| siRNA or dCas9-KRAB knockdown of TCF7L2 in HCT116, measuring POU5F1B/MYC expression and, if feasible, the enhancer activity reporter. | medium | yes | TCF7L2 knockdown has no effect attributable to this element or allele. | TCF7L2 knockdown/CRISPRi reduces enhancer activity and/or target-gene expression. | TCF7L2 knockdown has no effect on this element or target gene. | TCF7L2 knockdown has no effect on this element or target gene. |

## Next experiment

Allele-specific TCF7L2 ChIP-qPCR (or ChIP with allele-specific primer extension) at rs73706717 in HCT116, comparing T and C alleles; this directly tests the ref-preferred TCF7L2 binding claim and separates the null from the TCF7L2 chain more cheaply than a reporter or 3C assay. A qbic_tf_detail lookup would clarify whether TCF7L2 has an own model, but it cannot separate an allele-specific mechanism from the null because it does not measure occupancy at the T versus C allele in cells.

## Investigate calls

- qbic_tf_detail({"tf": "TCF7L2"})
- qbic_tf_detail({"tf": "SP1"})
- eqtl_lookup({"tissue": "Colon - Transverse"})

## Flags

- literature_fallback: no hits for 'rs73706717 AND POU5F1B AND "colorectal cancer"'; dropped the rsID
- quote_rejected: PMID 42465001: not an exact substring of the abstract

Citation support: 1.00 of links cite only evidence that passed every check.

## Evidence

<a id="e01"></a>**E01** variant_annotation, Ensembl VEP (GRCh38) (https://rest.ensembl.org/vep/human/region/8:127401265-127401265:1/C?content-type=application/json&Conservation=1; retrieved 2026-10-26T02:21:56+00:00)

> Variant chr8:127401265:T>C (GRCh38), allele string T/C
> Known IDs: rs73706717
> Most severe consequence: non_coding_transcript_exon_variant
> Regulatory features: ENSR8_CGMBX enhancer
> GERP conservation score at the site: -2.8
> Transcript consequences: CASC8 (intron_variant, non_coding_transcript_variant); CCAT2 (non_coding_transcript_exon_variant); PCAT1 (intron_variant, non_coding_transcript_variant); POU5F1B (intron_variant); PCAT1 (downstream_gene_variant)

<a id="e02"></a>**E02** nearest_genes, Ensembl overlap (protein_coding) (https://rest.ensembl.org/overlap/region/human/8:126401265-128401265?feature=gene;biotype=protein_coding;content-type=application/json; retrieved 2026-10-26T02:21:59+00:00)

> 3 protein-coding genes within 1000 kb of chr8:127401265:T>C, by distance to TSS:
> POU5F1B: 79.1 kb from TSS (in gene body, strand +1)
> MYC: 334.2 kb from TSS (upstream, strand +1)
> LRATD2: 842.8 kb from TSS (upstream, strand -1)

<a id="e03"></a>**E03** ccre_lookup, ENCODE v4 cCRE registry (ENCFF420VPZ) and SCREEN (https://screen-beta-api.wenglab.org/dataws/cre_table; retrieved 2026-10-26T02:21:42+00:00)

> The variant lies in cCRE EH38E3858447 (pELS: proximal enhancer-like), chr8:127401053-127401303.
> SCREEN: 3 cCREs within 500 bp (max z-score across ENCODE biosamples):
> EH38E3858447 pELS (contains the variant): DNase z 5.2, H3K27ac z 4.8, H3K4me3 z 1.5, CTCF z 4.1; nearby genes CCAT2, PCAT1, POU5F1B
> EH38E3858448 pELS: DNase z 5.2, H3K27ac z 4.8, H3K4me3 z 1.5, CTCF z 2.2; nearby genes CCAT2, PCAT1, POU5F1B
> EH38E3858446 pELS: DNase z 4.9, H3K27ac z 4.8, H3K4me3 z 1.5, CTCF z 5.5; nearby genes CCAT2, PCAT1, POU5F1B
> Biosample-specific z-scores are not in this call; the values above are maxima over biosamples.

<a id="e04"></a>**E04** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> ENCODE TF ChIP-seq at chr8:127401265:T>C: 149 peaks contain the variant, from 83 factors in 25 biosamples. In the matching biosample HCT116: 3 peaks from 3 factors. cCRE class at the variant: pELS. Bound factors outside the TF model collection (co-factors, Pol II, and TFs with no binding model; signs of an active element, not TF candidates): ASH2L, CHD4, EP300, HDAC1, HDAC2, HMGXB4, KDM1A, KDM6A, LCORL, LIN54, MED1, MED13 (+26 more). Bound, expressed TFs with a binding model: 40; listed one per row: TCF7L2, SP1, CTCF, CEBPB, MYBL2, NR2C2, TFAP4, ISL2, NR2F2, ERF; also bound: NR2F6, NFIC, ELF1, ZNF317, NFIL3, ZBTB7B, KLF16, PITX1, JUNB, SKI, CREM, RXRB, ATF2, ZNF609, ZNF280D, ZNF12, AHDC1, ZNF652, PHF21A, ETS1, NFIA, NR3C1, BCL6, PRDM10, HOXA3, HNF4A, MNX1, HNF1B, ZNF362, FOXA1. Bound but below 1 TPM: FOXA2, HNF1A, ONECUT1, SOX6, TBX2. Assayed with no peak here: 11 TFs in the matching biosample, 517 only elsewhere; never assayed: 536.

<a id="e05"></a>**E05** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> TCF7L2: bound here. 4 ENCODE ChIP-seq peak(s) contain the variant, in the matching biosample HCT116; also in HepG2 (e.g. ENCSR000EUV). 63.61 TPM in DepMap:ACH-000971 (HCT 116), rank 53 of 1626 TFs.

<a id="e06"></a>**E06** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> SP1: bound here. 2 ENCODE ChIP-seq peak(s) contain the variant, in the matching biosample HCT116; also in HepG2 (e.g. ENCSR000BSF). 38.96 TPM in DepMap:ACH-000971 (HCT 116), rank 118 of 1626 TFs.

<a id="e07"></a>**E07** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> CTCF: bound elsewhere. 34 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: A549, C4-2B, Panc1, RWPE2, adrenal gland, astrocyte (+13 more) (e.g. ENCSR173IEA). 50.0 TPM in DepMap:ACH-000971 (HCT 116), rank 78 of 1626 TFs.

<a id="e08"></a>**E08** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> CEBPB: bound elsewhere. 3 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: HepG2 (e.g. ENCSR000BQI). 13.15 TPM in DepMap:ACH-000971 (HCT 116), rank 408 of 1626 TFs.

<a id="e09"></a>**E09** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> MYBL2: bound elsewhere. 2 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: HepG2 (e.g. ENCSR581KCO). 67.51 TPM in DepMap:ACH-000971 (HCT 116), rank 46 of 1626 TFs.

<a id="e10"></a>**E10** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> NR2C2: bound elsewhere. 2 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: HepG2 (e.g. ENCSR559ZKI). 22.6 TPM in DepMap:ACH-000971 (HCT 116), rank 244 of 1626 TFs.

<a id="e11"></a>**E11** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> TFAP4: bound elsewhere. 2 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: HepG2 (e.g. ENCSR587BVQ). 19.72 TPM in DepMap:ACH-000971 (HCT 116), rank 283 of 1626 TFs.

<a id="e12"></a>**E12** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> ISL2: bound elsewhere. 2 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: HepG2 (e.g. ENCSR492IHH). 2.77 TPM in DepMap:ACH-000971 (HCT 116), rank 862 of 1626 TFs.

<a id="e13"></a>**E13** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> NR2F2: bound elsewhere. 1 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: HepG2 (e.g. ENCSR000BVM). 61.74 TPM in DepMap:ACH-000971 (HCT 116), rank 58 of 1626 TFs.

<a id="e14"></a>**E14** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> ERF: bound elsewhere. 1 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: HepG2 (e.g. ENCSR159DQO). 46.58 TPM in DepMap:ACH-000971 (HCT 116), rank 90 of 1626 TFs.

<a id="e15"></a>**E15** gwas_lookup, GWAS Catalog REST v2 (https://www.ebi.ac.uk/gwas/rest/api/v2/associations?rs_id=rs73706717&size=100; retrieved 2026-10-26T02:21:56+00:00)

> 0 GWAS Catalog associations for rs73706717, strongest first:

<a id="e16"></a>**E16** finemap_lookup, Open Targets Platform (credible sets, L2G) (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-26T02:21:56+00:00)

> 2 credible sets contain 8_127401265_T_C: 2 GWAS, 0 molecular QTL.
> GWAS prostate-specific antigen (PSA, maximum, inv-norm transforme: PIP 0.04; L2G POU5F1B 0.83
> GWAS Urinary incontinence (PheCode 599.4): PIP 0.04; L2G POU5F1B 0.78
> Best L2G gene scores across these sets: POU5F1B 0.83

<a id="e17"></a>**E17** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr8_127401265_T_C_b38&datasetId=gtex_v8; retrieved 2026-10-26T02:23:32+00:00)

> 0 significant GTEx v8 single-tissue eQTLs for chr8_127401265_T_C_b38. NES is the effect of the alt allele (C) relative to ref (T).

<a id="e18"></a>**E18** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=POU5F1B%20AND%20%22colorectal%20cancer%22&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T02:21:59+00:00)

> Europe PMC: 150 hits for 'POU5F1B AND "colorectal cancer"'; top 8 with PMIDs:
> PMID 42465001 (2026): Circ_0075829 affects POU5F1B expression through sponging miR-576-3p to promote growth, invasion, and angiogenesis of colon cancer cells.
> PMID 41993623 (2026): Tailorable porous collagen hydrogels as a physiologically relevant platform for extrachromosomal DNA-associated colorectal cancer research.
> PMID 41796348 (2026): Harnessing the LncRNA CCAT2 role in gastric cancer: from molecular insights to clinical implications.
> PMID 41930642 (2026): Systematic Identification and Characterization of Causal Risk Genes Implicated in Colorectal Cancer by Integrating GWAS, eQTL, and mQTL Data.
> PMID 42686757 (2026): Phase separation of ecDNA condensates establishes in-trans contact domains that boost selective MYC regulatory interactions.
> PMID 40506516 (2025): Association between methylation quantitative trait loci and colorectal cancer risk, survival and cancer recurrence.
> PMID 41144378 (2025): Integrative GWAS and RNA-Seq analysis for target identification and virtual drug screening in colorectal cancer.
> PMID 41196428 (2025): Combined CHK1 and PD-L1 blockade as a novel therapeutic strategy against stemness and immunosuppression in ovarian cancer.

<a id="e19"></a>**E19** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> QBiC-SELEX screen of chr8:127401265:T>C, one line per TF, each with the TF's own or CIS-BP-mapped model of largest |z|. Candidates are TFs whose ENCODE ChIP-seq peaks contain the variant and that are expressed (DepMap line ACH-000971), bound here before bound elsewhere, then by |z|; then expressed TFs ENCODE never assayed whose best model passes the gate (occupancy unknown). Shown: 10 of 40 occupied, 5 of 103 with unknown occupancy. Left out: 11 TFs assayed in the matching biosample and 517 assayed only elsewhere, none with a peak here; 5 bound but below 1 TPM. The gate (|z| > 4.05, Bonferroni over 997 models) marks a change QBiC-SELEX detects; it says nothing about occupancy. Effect > 0 means the alternate allele binds more strongly. In vitro binding only.

<a id="e20"></a>**E20** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> TCF7L2 (HMG/Sox, 3 models; QBiC-SELEX coverage: mapped models only): best model TCF7_eDBD_TCGGAC40NCCA_KS_yin2017_0_3_7mer (a CIS-BP-mapped model of TCF7), z -8.8, effect -0.429: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 63.61 TPM, rank 53 of 1626 TFs in DepMap:ACH-000971 (HCT 116). Occupancy: bound here: ENCODE ChIP-seq peak over the variant in HCT116, e.g. ENCSR000EUV. Best model's site strength: ref 90.0th, alt 87.2th percentile of its k-mer coefficients.

<a id="e21"></a>**E21** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> SP1 (C2H2 ZF, 5 models; QBiC-SELEX coverage: own model): best model SP3_eDBD_TTCACC40NGCT_KR_yin2017_0_3_7mer (a CIS-BP-mapped model of SP3), z -7.07, effect -0.298: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 38.96 TPM, rank 118 of 1626 TFs in DepMap:ACH-000971 (HCT 116). Occupancy: bound here: ENCODE ChIP-seq peak over the variant in HCT116, e.g. ENCSR000BSF. Best model's site strength: ref 90.4th, alt 75.6th percentile of its k-mer coefficients.

<a id="e22"></a>**E22** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> NFIC (SMAD, 4 models; QBiC-SELEX coverage: own model): best model NFIB_NA_TCATCA20NCG_ESAD_yang2017_0_3_7mer (a CIS-BP-mapped model of NFIB), z 24.28, effect 1.783: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 36.29 TPM, rank 137 of 1626 TFs in DepMap:ACH-000971 (HCT 116). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in HepG2, e.g. ENCSR000BQX. Best model's site strength: ref 96.3th, alt 99.5th percentile of its k-mer coefficients.

<a id="e23"></a>**E23** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> NFIA (SMAD, 4 models; QBiC-SELEX coverage: own model): best model NFIB_NA_TCATCA20NCG_ESAD_yang2017_0_3_7mer (a CIS-BP-mapped model of NFIB), z 24.28, effect 1.783: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 7.07 TPM, rank 616 of 1626 TFs in DepMap:ACH-000971 (HCT 116). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in HepG2, e.g. ENCSR226QQM. Best model's site strength: ref 96.3th, alt 99.5th percentile of its k-mer coefficients.

<a id="e24"></a>**E24** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> HNF1B (Homeodomain, 3 models; QBiC-SELEX coverage: own model): best model HMBOX1_eDBD_TGGCTC40NCGC_KAN_yin2017_1_2_7mer (a CIS-BP-mapped model of HMBOX1), z -23.93, effect -0.32: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 2.08 TPM, rank 929 of 1626 TFs in DepMap:ACH-000971 (HCT 116). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in HepG2, e.g. ENCSR127XTZ. Best model's site strength: ref 100.0th, alt 67.8th percentile of its k-mer coefficients.

<a id="e25"></a>**E25** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> NR2F2 (Nuclear receptor, 29 models; QBiC-SELEX coverage: own model): best model NR1H3_DBD_TGAGCG40NTTG_KY_nitta2015_2_3_7mer (a CIS-BP-mapped model of NR1H3), z -15.02, effect -0.286: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 61.74 TPM, rank 58 of 1626 TFs in DepMap:ACH-000971 (HCT 116). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in HepG2, e.g. ENCSR000BVM. Best model's site strength: ref 95.9th, alt 60.2th percentile of its k-mer coefficients.

<a id="e26"></a>**E26** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> NR2F6 (Nuclear receptor, 29 models; QBiC-SELEX coverage: own model): best model NR1H3_DBD_TGAGCG40NTTG_KY_nitta2015_2_3_7mer (a CIS-BP-mapped model of NR1H3), z -15.02, effect -0.286: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 37.02 TPM, rank 133 of 1626 TFs in DepMap:ACH-000971 (HCT 116). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in HepG2, e.g. ENCSR798IJO. Best model's site strength: ref 95.9th, alt 60.2th percentile of its k-mer coefficients.

<a id="e27"></a>**E27** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> NR2C2 (Nuclear receptor, 29 models; QBiC-SELEX coverage: own model): best model NR1H3_DBD_TGAGCG40NTTG_KY_nitta2015_2_3_7mer (a CIS-BP-mapped model of NR1H3), z -15.02, effect -0.286: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 22.6 TPM, rank 244 of 1626 TFs in DepMap:ACH-000971 (HCT 116). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in HepG2, e.g. ENCSR559ZKI. Best model's site strength: ref 95.9th, alt 60.2th percentile of its k-mer coefficients.

<a id="e28"></a>**E28** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> RXRB (Nuclear receptor, 29 models; QBiC-SELEX coverage: own model): best model NR2C1_eDBD_TATTCA40NAGT_KT_yin2017_0_3_7mer (a CIS-BP-mapped model of NR2C1), z -13.82, effect -0.705: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 18.71 TPM, rank 299 of 1626 TFs in DepMap:ACH-000971 (HCT 116). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in HepG2, e.g. ENCSR560SEP. Best model's site strength: ref 97.3th, alt 92.0th percentile of its k-mer coefficients.

<a id="e29"></a>**E29** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> NR3C1 (Nuclear receptor, 4 models; QBiC-SELEX coverage: own model): best model NR3C2_eDBD_TGCTGG40NGCC_KT_yin2017_0_4_7mer (a CIS-BP-mapped model of NR3C2), z -12.32, effect -0.868: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 6.51 TPM, rank 637 of 1626 TFs in DepMap:ACH-000971 (HCT 116). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in A549, e.g. ENCSR070VXO. Best model's site strength: ref 83.8th, alt 60.7th percentile of its k-mer coefficients.

<a id="e30"></a>**E30** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> ZBTB22 (C2H2 ZF, 1 model; QBiC-SELEX coverage: own model): best model ZBTB22_eDBD_TGCCTC40NCAA_KP_yin2017_0_4_7mer (its own model), z -33.75, effect -1.962: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 3.74 TPM, rank 794 of 1626 TFs in DepMap:ACH-000971 (HCT 116). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 99.8th, alt 92.4th percentile of its k-mer coefficients.

<a id="e31"></a>**E31** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> NR1H3 (Nuclear receptor, 29 models; QBiC-SELEX coverage: own model): best model NR1H3_DBD_TGAGCG40NTTG_KY_nitta2015_2_3_7mer (its own model), z -15.02, effect -0.286: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 11.39 TPM, rank 459 of 1626 TFs in DepMap:ACH-000971 (HCT 116). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 95.9th, alt 60.2th percentile of its k-mer coefficients.

<a id="e32"></a>**E32** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> TET3 (CxxC, 2 models; QBiC-SELEX coverage: own model): best model CXXC4_FL_GG40NTAGTTT_YWKC_jolma2025_0_4_7mer (a CIS-BP-mapped model of CXXC4), z 14.12, effect 0.794: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 10.17 TPM, rank 497 of 1626 TFs in DepMap:ACH-000971 (HCT 116). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 87.7th, alt 96.6th percentile of its k-mer coefficients.

<a id="e33"></a>**E33** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> NR1D2 (Nuclear receptor, 29 models; QBiC-SELEX coverage: own model): best model NR2C1_eDBD_TATTCA40NAGT_KT_yin2017_0_3_7mer (a CIS-BP-mapped model of NR2C1), z -13.82, effect -0.705: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 37.06 TPM, rank 132 of 1626 TFs in DepMap:ACH-000971 (HCT 116). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 97.3th, alt 92.0th percentile of its k-mer coefficients.

<a id="e34"></a>**E34** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> NR4A2 (Nuclear receptor, 29 models; QBiC-SELEX coverage: own model): best model NR2C1_eDBD_TATTCA40NAGT_KT_yin2017_0_3_7mer (a CIS-BP-mapped model of NR2C1), z -13.82, effect -0.705: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 7.19 TPM, rank 611 of 1626 TFs in DepMap:ACH-000971 (HCT 116). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 97.3th, alt 92.0th percentile of its k-mer coefficients.

<a id="e35"></a>**E35** qbic_tf_detail, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> {"tf":"TCF7L2","symbol":"TCF7L2","via":"hgnc_symbol","notes":[],"coverage":"mapped","variant":"chr8:127401265:T>C","gate_p":5.02e-05,"models":[{"model":"LEF1_FL_TAGTCG40NAGA_KZ_yin2017_0_3_7mer","mapping":"CIS-BP (LEF1)","group":"G041 HMG/Sox, 3 models","quality":0.63,"effect":-0.306,"z":-2.77,"p":0.0056,"rank_abs_z":"461/997","passed_gate":false,"site_strength":{"ref_percentile":81.3,"alt_percentile":95.3,"k":7}},{"model":"TCF7_eDBD_TCGGAC40NCCA_KS_yin2017_0_3_7mer","mapping":"CIS-BP (TCF7)","group":"G041 HMG/Sox, 3 models","quality":0.732,"effect":-0.429,"z":-8.8,"p":1.4e-18,"rank_abs_z":"66/997","passed_gate":true,"site_strength":{"ref_percentile":90.0,"alt_percentile":87.2,"k":7}},{"model":"TCF7L1_eDBD_TTGGCA40NTCG_KW_yin2017_0_3_7mer","mapping":"CIS-BP (TCF7L1)","group":"G041 HMG/Sox, 3 models","quality":0.602,"effect":-0.242,"z":-3.57,"p":0.00036,"rank_abs_z":"359/997","passed_gate":false,"site_strength":{"ref_percentile":84.6,"alt_percentile":58.3,"k":7}}]}

<a id="e36"></a>**E36** qbic_tf_detail, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> {"tf":"SP1","symbol":"SP1","via":"hgnc_symbol","notes":[],"coverage":"own_model","variant":"chr8:127401265:T>C","gate_p":5.02e-05,"models":[{"model":"SP1_eDBD_TCTCTA40NCAC_KV_yin2017_0_3_7mer","mapping":"own","group":"G015 C2H2 ZF, 5 models","quality":0.891,"effect":-0.007,"z":-0.11,"p":0.91,"rank_abs_z":"975/997","passed_gate":false,"site_strength":{"ref_percentile":97.2,"alt_percentile":97.4,"k":7}},{"model":"SP3_eDBD_TTCACC40NGCT_KR_yin2017_0_3_7mer","mapping":"CIS-BP (SP3)","group":"G015 C2H2 ZF, 5 models","quality":0.813,"effect":-0.298,"z":-7.07,"p":1.5e-12,"rank_abs_z":"117/997","passed_gate":true,"site_strength":{"ref_percentile":90.4,"alt_percentile":75.6,"k":7}},{"model":"SP4_NA_TTATGT20NGTA_ESAE_yang2017_0_3_7mer","mapping":"CIS-BP (SP4)","group":"G015 C2H2 ZF, 5 models","quality":0.825,"effect":-0.111,"z":-2.06,"p":0.04,"rank_abs_z":"566/997","passed_gate":false,"site_strength":{"ref_percentile":65.1,"alt_percentile":79.1,"k":7}},{"model":"SP8_NA_TGCTCG20NCTC_ESY_yang2017_0_4_7mer","mapping":"CIS-BP (SP8)","group":"G015 C2H2 ZF, 5 models","quality":0.672,"effect":-0.048,"z":-0.66,"p":0.51,"rank_abs_z":"848/997","passed_gate":false,"site_strength":{"ref_percentile":88.7,"alt_percentile":84.7,"k":7}},{"model":"SP9_eDBD_TACCGA40NATA_KP_yin2017_0_4_7mer","mapping":"CIS-BP (SP9)","group":"G015 C2H2 ZF, 5 models","quality":0.936,"effect":-0.485,"z":-6.42,"p":1.3e-10,"rank_abs_z":"143/997","passed_gate":true,"site_strength":{"ref_percentile":70.8,"alt_percentile":67.5,"k":7}}]}

<a id="e37"></a>**E37** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr8_127401265_T_C_b38&datasetId=gtex_v8; retrieved 2026-10-26T02:23:32+00:00)

> 0 significant GTEx v8 single-tissue eQTLs for chr8_127401265_T_C_b38 in tissues matching 'Colon - Transverse'. NES is the effect of the alt allele (C) relative to ref (T).
