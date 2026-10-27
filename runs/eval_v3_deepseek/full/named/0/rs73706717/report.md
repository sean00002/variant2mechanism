# rs73706717 and Colorectal cancer (8q24)

Configuration `full`, named mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.06 over 8 model calls; 357 s.

Variant `chr8:127401265:T>C` (germline); expression context: DepMap:ACH-000971 (HCT 116).

## QBiC-SELEX screen (occupancy first)

Occupied candidates: TCF7L2 (bound here, z -8.8, weak site); SP1 (bound here, z -7.07, weak site); NFIC (bound elsewhere, z 24.28); NFIA (bound elsewhere, z 24.28); HNF1B (bound elsewhere, z -23.93); CTCF (bound elsewhere, z 8.21); CEBPB (bound elsewhere, z -6.94); TFAP4 (bound elsewhere, z 0.51, no clear allelic change); NR2F2 (bound elsewhere, z -15.02, weak site); NR2F6 (bound elsewhere, z -15.02, weak site). Occupancy unknown: ZBTB22 (z -33.75); NR1H3 (z -15.02); TET3 (z 14.12); NR1D2 (z -13.82); NR4A2 (z -13.82). Diagnostic, not shown to the model: 307 of 997 models pass Bonferroni.

## Ranked chains

### 1. H5: No TF-mediated effect of rs73706717 itself (p = 0.36)

Null chain: no TF-mediated effect of this variant.

Predictions: No allele-specific TF binding or enhancer activity at this exact base in HCT116.; Any disease association is due to a linked causal variant, a passenger event, or no allelic effect.; The many ChIP peaks at the element reflect the active 8q24 enhancer, but not necessarily this base; several QBiC-SELEX changes are weak or from TFs without demonstrated HCT116 occupancy.

Falsified if: Allele-specific TF ChIP or enhancer reporter assays show a reproducible effect of this exact base in HCT116.; Fine-mapping shows rs73706717 itself is the causal variant rather than a linked variant.

### 2. H1: TCF7L2 loss-of-binding at the 8q24 pELS (p = 0.26)

TF TCF7L2 (QBiC-SELEX coverage mapped), ref allele binds more; element EH38E3858447 pELS; gene POU5F1B; cell type HCT116.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | TCF7L2 is the stronger HCT116-occupied candidate at this base: ENCODE TCF7L2 ChIP-seq has peaks containing the variant in HCT116 (E05). The ref T allele is predicted to bind more than alt C, but this is low-confidence: TCF7L2 has no own QBiC-SELEX model, and E20 reports only a CIS-BP-mapped TCF7 model at weak k-mers, so the mapped model is not direct TCF7L2 allelic evidence. Occupancy supports TCF7L2 at the element, not allele-specific binding at the base. | weak | [E05](#e05), [E20](#e20) |
| element | The variant lies in cCRE EH38E3858447, a pELS, and TCF7L2 ChIP-seq contains the variant in HCT116. The cCRE activity z-scores are maxima over ENCODE biosamples, so HCT116-specific enhancer activity is only partly supported. | supported | [E03](#e03), [E04](#e04), [E05](#e05) |
| gene | POU5F1B is the closest protein-coding gene with local L2G support at 79.1 kb from its TSS, but the L2G credible sets are PSA and urinary incontinence, not colorectal cancer, and no colorectal eQTL is provided; MYC remains a farther long-range alternative. | weak | [E02](#e02), [E16](#e16), [E17](#e17) |
| cell_type | HCT116 is a colorectal cancer cell line that expresses TCF7L2 at 63.61 TPM and has TCF7L2 ChIP-seq occupancy over the variant. | supported | [E05](#e05), [E20](#e20) |
| phenotype | TCF7L2-dependent enhancer activity at 8q24 is a plausible colorectal cancer mechanism, but this exact variant has no GWAS Catalog association, no significant GTEx eQTL, and only general POU5F1B/colorectal cancer literature plus Open Targets gene-disease support. | weak | [E15](#e15), [E17](#e17), [E18](#e18), [E37](#e37) |

Predictions: Allele-specific TCF7L2 ChIP in HCT116 shows stronger T than C binding at rs73706717.; If TCF7L2 activates the element, a T-vs-C enhancer reporter gives higher activity on T.; TCF7L2 knockdown reduces the linked target gene if this chain is correct.

Falsified if: Allele-specific TCF7L2 ChIP in HCT116 shows no difference between T and C at rs73706717.; TCF7L2 knockdown does not change the proposed target gene expression.; An allele-specific enhancer reporter in HCT116 shows no T-vs-C difference.

### 3. H2: SP1 loss-of-binding at the 8q24 pELS (p = 0.18)

TF SP1 (QBiC-SELEX coverage own_model), ref allele binds more; element EH38E3858447 pELS; gene POU5F1B; cell type HCT116.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | SP1 is HCT116-occupied over the variant by ENCODE SP1 ChIP-seq (E06). The ref T allele is predicted to bind more than alt C from the QBiC-SELEX best model, but that model is a CIS-BP-mapped SP3 model at a weak site, so direct allele-specific SP1 binding at this base is not established. | weak | [E06](#e06), [E21](#e21) |
| element | The variant sits in the pELS EH38E3858447, and SP1 ChIP-seq contains the variant in HCT116; the cCRE activity z-scores are maxima over biosamples, so HCT116-specific enhancer activity is not fully proven by E03 alone. | supported | [E03](#e03), [E04](#e04), [E06](#e06) |
| gene | POU5F1B is the local L2G candidate at 79.1 kb, but the credible sets are not colorectal cancer and no colorectal eQTL supports this target; MYC is a farther long-range alternative. | weak | [E02](#e02), [E16](#e16), [E17](#e17) |
| cell_type | HCT116 expresses SP1 at 38.96 TPM and has SP1 ChIP-seq occupancy over the variant. | supported | [E06](#e06), [E21](#e21) |
| phenotype | SP1-dependent enhancer activity at 8q24 could affect colorectal biology through POU5F1B or MYC, but direct variant-specific colorectal cancer genetic evidence is absent. | weak | [E15](#e15), [E17](#e17), [E18](#e18), [E37](#e37) |

Predictions: Allele-specific SP1 ChIP in HCT116 shows stronger T than C binding at rs73706717.; If SP1 activates the element, a T-vs-C enhancer reporter gives higher activity on T.; SP1 knockdown reduces the linked target gene.

Falsified if: Allele-specific SP1 ChIP in HCT116 shows no difference between T and C.; SP1 is not occupied at this element in HCT116.; SP1 knockdown or inhibition does not alter the linked target gene.

### 4. H3: NFIC gain-of-binding at the 8q24 pELS (p = 0.13)

TF NFIC (QBiC-SELEX coverage own_model), alt allele binds more; element EH38E3858447 pELS; gene POU5F1B; cell type HCT116.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | NFIC-family QBiC-SELEX gives a strong alt-allele gain: z=24.28 and effect=1.783 for an NFIB-mapped model with a strong site, so alt C is predicted to bind NFIC more than ref T. However, HCT116 occupancy is not shown; ENCODE NFIC ChIP over the variant is only in HepG2. | weak | [E22](#e22), [E35](#e35) |
| element | The variant lies in pELS EH38E3858447, but NFIC-family ChIP over the variant is from another biosample and HCT116 occupancy at this base is not demonstrated. | weak | [E03](#e03), [E22](#e22), [E35](#e35) |
| gene | POU5F1B is the local L2G candidate at 79.1 kb, but the L2G credible sets are not colorectal cancer and no colorectal eQTL supports this target; MYC remains a long-range alternative. | weak | [E02](#e02), [E16](#e16), [E17](#e17) |
| cell_type | HCT116 expresses NFIC at 36.29 TPM, but HCT116 occupancy at this exact site is absent from the provided evidence. | weak | [E22](#e22), [E35](#e35) |
| phenotype | If NFIC binds more strongly on alt C and activates the element, this could increase POU5F1B or MYC expression in colorectal cells, but direct variant-specific colorectal cancer evidence is absent. | weak | [E15](#e15), [E17](#e17), [E18](#e18), [E37](#e37) |

Predictions: Alt C increases NFIC binding in an allele-specific assay.; NFIC ChIP-seq in HCT116 shows occupancy at this element if this chain is correct.; An enhancer reporter gives higher activity on C than T if NFIC activates the element.

Falsified if: NFIC ChIP in HCT116 does not occupy this element.; Alt C does not increase NFIC binding in an allele-specific assay.; NFIC knockdown does not change the linked target gene.

### 5. H4: CTCF gain-of-binding and 8q24 insulation (p = 0.07)

TF CTCF (QBiC-SELEX coverage own_model), alt allele binds more; element EH38E3858447 pELS; gene MYC; cell type HCT116.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | CTCF's own QBiC-SELEX model gives a strong alt-allele gain: z=8.21 and effect=0.902 at a strong site, so alt C is predicted to bind CTCF more than ref T. However, CTCF ChIP peaks over the variant are in other biosamples, not HCT116. | weak | [E25](#e25), [E36](#e36) |
| element | The variant lies in a pELS with CTCF signal in the cCRE call, but HCT116 CTCF occupancy over this base is absent and the cCRE signal is not HCT116-specific. | weak | [E03](#e03), [E25](#e25), [E36](#e36) |
| gene | A CTCF-dependent insulator change at this 8q24 element would most plausibly affect long-range MYC regulation; MYC is 334.2 kb upstream of the variant, but no contact assay or CTCF perturbation at this variant is provided. | weak | [E02](#e02), [E18](#e18) |
| cell_type | HCT116 expresses CTCF at 50.0 TPM, but the provided CTCF peaks over the variant are from other biosamples, not HCT116. | weak | [E25](#e25), [E36](#e36) |
| phenotype | Altered CTCF insulation at 8q24 could change MYC regulatory contacts in colorectal cancer, but this variant has no direct colorectal genetic, eQTL, or contact evidence in the provided data. | weak | [E15](#e15), [E17](#e17), [E18](#e18) |

Predictions: Alt C increases CTCF binding at this base if CTCF occupies the element in HCT116.; Allele-specific CTCF ChIP or Hi-C/contact assays detect a chromatin-contact change.; This chain predicts a MYC-centered effect rather than a direct POU5F1B promoter effect.

Falsified if: CTCF does not occupy this element in HCT116.; Alt C does not increase CTCF binding.; No chromatin-contact or MYC expression change is seen.

## Prediction matrix

| Test | Cost | Separates top two | H5 | H1 | H2 | H3 | H4 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Allele-specific TCF7L2 ChIP-qPCR in HCT116 at rs73706717 | low | yes | No reproducible allele-specific TCF7L2 binding at this base. | Stronger T than C TCF7L2 binding at rs73706717 in HCT116. | No allele-specific TCF7L2 binding; SP1, if anything, is the relevant factor. | No allele-specific TCF7L2 binding; NFIC is the proposed factor. | No allele-specific TCF7L2 binding; CTCF is the proposed factor. |
| Allele-specific SP1 ChIP-qPCR in HCT116 at rs73706717 | low | no | No reproducible allele-specific SP1 binding at this base. | No allele-specific SP1 binding; TCF7L2 is the proposed factor. | Stronger T than C SP1 binding at rs73706717 in HCT116. | No allele-specific SP1 binding; NFIC is the proposed factor. | No allele-specific SP1 binding; CTCF is the proposed factor. |
| NFIC ChIP-qPCR in HCT116 at the rs73706717 element | low | no | No NFIC occupancy or no allele-specific NFIC effect at this base. | No NFIC occupancy at this element in HCT116. | No NFIC occupancy at this element in HCT116. | NFIC occupies this element in HCT116, with stronger C than T binding if allele-specific. | No NFIC occupancy at this element in HCT116. |
| CTCF ChIP-qPCR in HCT116 at the rs73706717 element | low | no | No CTCF occupancy or no allele-specific CTCF effect at this base. | No CTCF occupancy at this element in HCT116. | No CTCF occupancy at this element in HCT116. | No CTCF occupancy at this element in HCT116. | CTCF occupies this element in HCT116, with stronger C than T binding if allele-specific. |
| Allele-specific enhancer reporter in HCT116 with rs73706717 T vs C | medium | yes | No reproducible allele-specific enhancer activity in HCT116. | T-vs-C reporter shows higher activity on T if TCF7L2 activates the element. | T-vs-C reporter shows higher activity on T if SP1 activates the element. | T-vs-C reporter shows higher activity on C if NFIC activates the element. | No enhancer activity change, or a C-dependent change if CTCF affects insulation. |
| TF knockdown plus target-gene expression in HCT116 | medium | no | No target-gene change attributable to this variant; effects may come from a linked variant. | TCF7L2 knockdown reduces POU5F1B or MYC expression. | SP1 knockdown, not TCF7L2 knockdown, reduces the linked target gene. | NFIC knockdown reduces the linked target gene. | CTCF perturbation changes chromatin contacts or MYC expression. |

## Next experiment

Allele-specific TCF7L2 ChIP-qPCR in HCT116 at rs73706717, with a heterozygous-sample input control; low cost and directly separates H1 (T>C TCF7L2 binding) from H5 (no allele-specific TCF7L2 effect). If TCF7L2 shows no allele-specific binding, H5 is favored and H1 is falsified; if T>C TCF7L2 binding is reproducible, H1 gains direct support.

## Investigate calls

- chip_peaks({"biosample": "HCT116", "tf": "NFIC"})
- chip_peaks({"biosample": "HCT116", "tf": "CTCF"})
- gene_disease({"gene": "POU5F1B"})

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

> QBiC-SELEX screen of chr8:127401265:T>C, one line per TF, each with the TF's own or CIS-BP-mapped model of largest |z|. Candidates are TFs whose ENCODE ChIP-seq peaks contain the variant and that are expressed (DepMap line ACH-000971), bound here before bound elsewhere, then a strong site before a weak one, then by |z|; then expressed TFs ENCODE never assayed whose best model passes the gate (occupancy unknown). Shown: 10 of 40 occupied (6 with a strong site), 5 of 103 with unknown occupancy. Left out: 11 TFs assayed in the matching biosample and 517 assayed only elsewhere, none with a peak here; 5 bound but below 1 TPM. The gate (|z| > 4.05, Bonferroni over 997 models) marks a change QBiC-SELEX detects; it says nothing about occupancy. Effect > 0 means the alternate allele binds more strongly. In vitro binding only. Site strength is the better allele's best k-mer over the variant, as a percentile of the best model's k-mers; a strong site reaches the 97.5th. At a weak site the ChIP peak more likely reflects another site in the element.

<a id="e20"></a>**E20** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> TCF7L2 (HMG/Sox, 3 models; QBiC-SELEX coverage: mapped models only): best model TCF7_eDBD_TCGGAC40NCCA_KS_yin2017_0_3_7mer (a CIS-BP-mapped model of TCF7), z -8.8, effect -0.429: ref allele binds more (|z| above the gate), but between weak k-mers. 63.61 TPM, rank 53 of 1626 TFs in DepMap:ACH-000971 (HCT 116). Occupancy: bound here: ENCODE ChIP-seq peak over the variant in HCT116, e.g. ENCSR000EUV. Best model's site strength: ref 90.0th, alt 87.2th percentile of its k-mer coefficients: a weak site (neither allele reaches the 97.5th), so the ChIP peak more likely reflects another site in the element.

<a id="e21"></a>**E21** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> SP1 (C2H2 ZF, 5 models; QBiC-SELEX coverage: own model): best model SP3_eDBD_TTCACC40NGCT_KR_yin2017_0_3_7mer (a CIS-BP-mapped model of SP3), z -7.07, effect -0.298: ref allele binds more (|z| above the gate), but between weak k-mers. 38.96 TPM, rank 118 of 1626 TFs in DepMap:ACH-000971 (HCT 116). Occupancy: bound here: ENCODE ChIP-seq peak over the variant in HCT116, e.g. ENCSR000BSF. Best model's site strength: ref 90.4th, alt 75.6th percentile of its k-mer coefficients: a weak site (neither allele reaches the 97.5th), so the ChIP peak more likely reflects another site in the element.

<a id="e22"></a>**E22** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> NFIC (SMAD, 4 models; QBiC-SELEX coverage: own model): best model NFIB_NA_TCATCA20NCG_ESAD_yang2017_0_3_7mer (a CIS-BP-mapped model of NFIB), z 24.28, effect 1.783: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 36.29 TPM, rank 137 of 1626 TFs in DepMap:ACH-000971 (HCT 116). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in HepG2, e.g. ENCSR000BQX. Best model's site strength: ref 96.3th, alt 99.5th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e23"></a>**E23** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> NFIA (SMAD, 4 models; QBiC-SELEX coverage: own model): best model NFIB_NA_TCATCA20NCG_ESAD_yang2017_0_3_7mer (a CIS-BP-mapped model of NFIB), z 24.28, effect 1.783: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 7.07 TPM, rank 616 of 1626 TFs in DepMap:ACH-000971 (HCT 116). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in HepG2, e.g. ENCSR226QQM. Best model's site strength: ref 96.3th, alt 99.5th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e24"></a>**E24** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> HNF1B (Homeodomain, 3 models; QBiC-SELEX coverage: own model): best model HMBOX1_eDBD_TGGCTC40NCGC_KAN_yin2017_1_2_7mer (a CIS-BP-mapped model of HMBOX1), z -23.93, effect -0.32: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 2.08 TPM, rank 929 of 1626 TFs in DepMap:ACH-000971 (HCT 116). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in HepG2, e.g. ENCSR127XTZ. Best model's site strength: ref 100.0th, alt 67.8th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e25"></a>**E25** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> CTCF (C2H2 ZF, 1 model; QBiC-SELEX coverage: own model): best model CTCF_FL_TG40NCTGTGG_YWL_jolma2025_0_3_7mer (its own model), z 8.21, effect 0.902: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 50.0 TPM, rank 78 of 1626 TFs in DepMap:ACH-000971 (HCT 116). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in A549, C4-2B, Panc1, RWPE2, adrenal gland (+14 more), e.g. ENCSR173IEA. Best model's site strength: ref 98.8th, alt 99.4th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e26"></a>**E26** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> CEBPB (bZIP, 3 models; QBiC-SELEX coverage: own model): best model CEBPB_eDBD_TATAAA40NACG_KAN_yin2017_0_4_7mer (its own model), z -6.94, effect -0.844: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 13.15 TPM, rank 408 of 1626 TFs in DepMap:ACH-000971 (HCT 116). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in HepG2, e.g. ENCSR000BQI. Best model's site strength: ref 98.2th, alt 73.1th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e27"></a>**E27** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> TFAP4 (bHLH, 1 model; QBiC-SELEX coverage: own model): best model TFAP4_NA_TCACGT20NGCA_ESAC_yang2017_0_3_7mer (its own model), z 0.51, effect 0.042: alt allele binds slightly more; occupied, no clear allelic change (|z| below the gate). 19.72 TPM, rank 283 of 1626 TFs in DepMap:ACH-000971 (HCT 116). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in HepG2, e.g. ENCSR587BVQ. Best model's site strength: ref 98.2th, alt 96.4th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e28"></a>**E28** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> NR2F2 (Nuclear receptor, 29 models; QBiC-SELEX coverage: own model): best model NR1H3_DBD_TGAGCG40NTTG_KY_nitta2015_2_3_7mer (a CIS-BP-mapped model of NR1H3), z -15.02, effect -0.286: ref allele binds more (|z| above the gate), but between weak k-mers. 61.74 TPM, rank 58 of 1626 TFs in DepMap:ACH-000971 (HCT 116). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in HepG2, e.g. ENCSR000BVM. Best model's site strength: ref 95.9th, alt 60.2th percentile of its k-mer coefficients: a weak site (neither allele reaches the 97.5th), so the ChIP peak more likely reflects another site in the element.

<a id="e29"></a>**E29** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> NR2F6 (Nuclear receptor, 29 models; QBiC-SELEX coverage: own model): best model NR1H3_DBD_TGAGCG40NTTG_KY_nitta2015_2_3_7mer (a CIS-BP-mapped model of NR1H3), z -15.02, effect -0.286: ref allele binds more (|z| above the gate), but between weak k-mers. 37.02 TPM, rank 133 of 1626 TFs in DepMap:ACH-000971 (HCT 116). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in HepG2, e.g. ENCSR798IJO. Best model's site strength: ref 95.9th, alt 60.2th percentile of its k-mer coefficients: a weak site (neither allele reaches the 97.5th), so the ChIP peak more likely reflects another site in the element.

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

<a id="e35"></a>**E35** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-26T13:23:02+00:00)

> No ENCODE NFIC ChIP-seq peak contains chr8:127401265:T>C in biosamples matching 'HCT116'. Absence can also mean no NFIC experiment in that biosample. In other biosamples, 1 NFIC peaks do contain the variant: HepG2 (experiments ENCSR000BQX).

<a id="e36"></a>**E36** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-26T13:23:02+00:00)

> No ENCODE CTCF ChIP-seq peak contains chr8:127401265:T>C in biosamples matching 'HCT116'. Absence can also mean no CTCF experiment in that biosample. In other biosamples, 34 CTCF peaks do contain the variant: A549, C4-2B, Panc1, RWPE2, adrenal gland, astrocyte, brain, breast epithelium, endothelial cell, epithelial cell of prostate, esophagus squamous epithelium, excitatory neuron, left lung, mesothelial cell of epicardium, middle frontal area 46, stomach, testis, thoracic aorta, tibial nerve (experiments ENCSR031PXV, ENCSR037GKL, ENCSR073BPG, ENCSR130TQM, ENCSR173IEA, ENCSR188XCX).

<a id="e37"></a>**E37** gene_disease, Open Targets Platform (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-26T02:23:32+00:00)

> Open Targets: POU5F1B and colorectal cancer (MONDO_0005575), overall score 0.54; by evidence type: genetic_association 0.87, literature 0.18, rna_expression 0.14
