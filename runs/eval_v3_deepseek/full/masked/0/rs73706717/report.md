# rs73706717 and Colorectal cancer (8q24)

Configuration `full`, masked mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.04 over 9 model calls; 214 s.

Variant `chr8:127401265:T>C` (germline); expression context: DepMap:ACH-000971 (HCT 116).

## QBiC-SELEX screen (occupancy first)

Occupied candidates: TCF7L2 (bound here, z -8.8, weak site); SP1 (bound here, z -7.07, weak site); NFIC (bound elsewhere, z 24.28); NFIA (bound elsewhere, z 24.28); HNF1B (bound elsewhere, z -23.93); CTCF (bound elsewhere, z 8.21); CEBPB (bound elsewhere, z -6.94); TFAP4 (bound elsewhere, z 0.51, no clear allelic change); NR2F2 (bound elsewhere, z -15.02, weak site); NR2F6 (bound elsewhere, z -15.02, weak site). Occupancy unknown: ZBTB22 (z -33.75); NR1H3 (z -15.02); TET3 (z 14.12); NR1D2 (z -13.82); NR4A2 (z -13.82). Diagnostic, not shown to the model: 307 of 997 models pass Bonferroni.

## Ranked chains

### 1. M4: Null: no TF-mediated effect of this variant (p = 0.47)

Null chain: no TF-mediated effect of this variant.

Predictions: No reproducible allele-specific TF occupancy at this base in HCT116 for any candidate TF.; No allele-specific enhancer activity or target-gene expression difference attributable to this variant.; Any disease association is due to a linked causal variant, chance, or a passenger event rather than a TF-mediated effect at chr8:127401265.

Falsified if: Reproducible allele-specific TF occupancy at this base is found in HCT116.; An allele-specific enhancer or target-gene expression difference is attributable to this variant.; The disease association is shown to be mediated by a TF binding this exact base.

### 2. M1: TCF7L2 occupies the ref allele at an 8q24 pELS and may regulate MYC, but allele specificity is unproven (p = 0.32)

TF TCF7L2 (QBiC-SELEX coverage mapped), ref allele binds more; element pELS EH38E3858447; gene MYC; cell type HCT116 colorectal cancer cell line.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | TCF7L2 is the best HCT116-occupied candidate TF at this base, with ENCODE ChIP-seq peaks over the variant in HCT116 and expression at 63.61 TPM. QBiC-SELEX gives ref T > alt C for its CIS-BP-mapped TCF7 model (z = -8.8, effect = -0.429), but the k-mer site is weak (ref 90.0th, alt 87.2th percentile), so the ChIP peak may reflect another site in the element and allele-specific binding at this base is not established. | weak | [E05](#e05), [E20](#e20), [E37](#e37) |
| element | The variant lies in pELS EH38E3858447, an active enhancer-like cCRE with DNase and H3K27ac signal. | supported | [E01](#e01), [E03](#e03) |
| gene | A candidate target is MYC, which is 334.2 kb upstream at 8q24 and has locus biology linked to colorectal cancer. This is proximity/biological inference only: the GTEx eQTL lookup is null and L2G instead favors POU5F1B, so the variant-to-MYC regulatory link is weak. | weak | [E02](#e02), [E16](#e16), [E17](#e17), [E18](#e18) |
| cell_type | HCT116 is a colorectal cancer cell line in which TCF7L2 is expressed and ENCODE ChIP-seq has a peak over this variant, making it the relevant expression context. | supported | [E05](#e05) |
| phenotype | A colorectal cancer connection is plausible through Wnt/TCF7L2-MYC biology, but direct variant-disease evidence is absent: there are no GWAS Catalog associations for this variant, no significant GTEx colon eQTL, and the provided L2G credible sets are not colorectal cancer. | weak | [E15](#e15), [E16](#e16), [E17](#e17), [E18](#e18) |

Predictions: Allele-specific TCF7L2 ChIP in HCT116 at this base should show higher ref T occupancy than alt C if M1 is correct.; An allele-specific enhancer reporter in HCT116 should show a TCF7L2-dependent decrease for alt C relative to ref T if TCF7L2 activates the element.; TCF7L2 knockdown or CRISPR disruption of the enhancer should reduce any allele-dependent MYC expression effect.

Falsified if: Allele-specific TCF7L2 ChIP in HCT116 does not show higher TCF7L2 occupancy on ref T than alt C at this base.; An allele-specific enhancer reporter in HCT116 does not show a TCF7L2-dependent difference between ref T and alt C.; TCF7L2 knockdown or enhancer disruption does not attenuate any allele-dependent enhancer or MYC expression effect.

### 3. M3: NFIC binds the alt allele strongly in vitro but lacks HCT116 occupancy evidence (p = 0.13)

TF NFIC (QBiC-SELEX coverage own_model), alt allele binds more; element pELS EH38E3858447; gene POU5F1B; cell type HCT116 colorectal cancer cell line.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | NFIC has a strong QBiC-SELEX alt C > ref T effect (z = 24.28, effect = +1.783; strong site, ref 96.3th and alt 99.5th percentile) and is expressed in HCT116 at 36.29 TPM. However, ENCODE ChIP-seq occupancy over this variant is reported only in HepG2, not HCT116, and NFIA shares the same mapped NFIB model and identical QBiC-SELEX statistics, so NFIC is chosen over NFIA mainly by expression and the relevant-cell occupancy evidence is missing. | weak | [E22](#e22), [E23](#e23), [E35](#e35) |
| element | The variant lies in pELS EH38E3858447, an active enhancer-like cCRE with DNase and H3K27ac signal. | supported | [E01](#e01), [E03](#e03) |
| gene | POU5F1B is the best L2G gene at this locus (score 0.83) and is 79.1 kb from the variant, but the credible sets are for PSA and urinary incontinence rather than colorectal cancer and direct NFIC regulation of POU5F1B is not shown. | weak | [E02](#e02), [E16](#e16) |
| cell_type | HCT116 expresses NFIC, but the provided ENCODE ChIP data do not show NFIC occupancy over this variant in HCT116; occupancy is only in HepG2. | supported | [E22](#e22), [E35](#e35) |
| phenotype | POU5F1B is linked to colorectal cancer in the provided literature and L2G data, but no evidence ties this specific NFIC-binding allele to colorectal cancer. | weak | [E16](#e16), [E18](#e18) |

Predictions: If NFIC acts here, alt C should increase NFIC occupancy in HCT116 at this base and, if NFIC is an activator, increase POU5F1B expression.; NFIC knockdown should reduce any alt-C-dependent enhancer or POU5F1B expression effect in HCT116.; The allele-dependent effect should be absent in cell types where NFIC does not occupy this element.

Falsified if: Alt C does not increase NFIC occupancy in HCT116 at this base.; NFIC knockdown does not reduce any alt-C-dependent enhancer or POU5F1B expression effect in HCT116.; The allele-dependent effect is present in cell types where NFIC does not occupy this element.

### 4. M2: SP1 occupies the ref allele at the pELS and may regulate CCAT2, but allele specificity and target regulation are unproven (p = 0.08)

TF SP1 (QBiC-SELEX coverage own_model), ref allele binds more; element pELS EH38E3858447; gene CCAT2; cell type HCT116 colorectal cancer cell line.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | SP1 is expressed in HCT116 and has ENCODE ChIP-seq peaks over the variant in HCT116. QBiC-SELEX gives ref T > alt C for its best CIS-BP-mapped SP3 model (z = -7.07, effect = -0.298), but the k-mer site is weak (ref 90.4th, alt 75.6th percentile), so occupancy could reflect another site in the element and allele-specific binding at this base is not established. | weak | [E06](#e06), [E21](#e21) |
| element | The variant lies in pELS EH38E3858447, an active enhancer-like cCRE with DNase and H3K27ac signal. | supported | [E01](#e01), [E03](#e03) |
| gene | A candidate target is CCAT2 because the variant lies in a CCAT2 non_coding_transcript_exon and the cCRE is annotated near CCAT2. There is no direct evidence that this variant regulates CCAT2 or that SP1 mediates such regulation. | weak | [E01](#e01), [E03](#e03) |
| cell_type | HCT116 is a colorectal cancer cell line in which SP1 is expressed and ENCODE ChIP-seq has a peak over this variant. | supported | [E06](#e06) |
| phenotype | The CCAT2 colorectal cancer connection is indirect in the provided data. There are no GWAS associations for this variant, no significant GTEx colon eQTL, and the cited literature discusses CCAT2 mainly in gastrointestinal cancer rather than this variant in colorectal cancer. | weak | [E15](#e15), [E16](#e16), [E17](#e17), [E18](#e18) |

Predictions: Allele-specific SP1 ChIP in HCT116 at this base should show higher ref T occupancy than alt C if M2 is correct.; An allele-specific enhancer reporter in HCT116 should show an SP1-dependent decrease for alt C relative to ref T if SP1 activates the element.; SP1 knockdown should reduce any allele-dependent CCAT2 expression effect.

Falsified if: Allele-specific SP1 ChIP in HCT116 does not show higher SP1 occupancy on ref T than alt C at this base.; An allele-specific enhancer reporter in HCT116 does not show an SP1-dependent difference between ref T and alt C.; SP1 knockdown or enhancer disruption does not attenuate any allele-dependent CCAT2 expression effect.

## Prediction matrix

| Test | Cost | Separates top two | M4 | M1 | M3 | M2 |
| --- | --- | --- | --- | --- | --- | --- |
| Allele-specific TCF7L2 ChIP-qPCR/ChIP-SNP at chr8:127401265 in HCT116 | medium | yes | No reproducible allele-specific TCF7L2 occupancy. | Ref T shows higher TCF7L2 occupancy than alt C at this base. | No allele-specific TCF7L2 occupancy effect. | No allele-specific TCF7L2 occupancy effect. |
| Allele-specific SP1 ChIP-qPCR/ChIP-SNP at chr8:127401265 in HCT116 | medium | no | No reproducible allele-specific SP1 occupancy. | No allele-specific SP1 occupancy effect. | No allele-specific SP1 occupancy effect. | Ref T shows higher SP1 occupancy than alt C at this base. |
| NFIC ChIP-seq occupancy in HCT116 | medium | no | NFIC occupancy may be present or absent, but it would not establish allele specificity. | No NFIC occupancy over this variant in HCT116 required. | NFIC ChIP-seq shows occupancy over the variant in HCT116. | No NFIC occupancy over this variant in HCT116 required. |
| Allele-specific enhancer reporter in HCT116 | medium | yes | No allele-specific enhancer activity difference. | Alt C reduces enhancer activity in an allele-specific reporter if TCF7L2 activates the element. | Alt C increases enhancer activity if NFIC activates the element; direction opposite if NFIC represses. | Alt C reduces enhancer activity in an allele-specific reporter if SP1 activates the element. |
| Candidate TF knockdown plus allele-specific enhancer/target expression readout | high | yes | No TF knockdown-dependent allele effect. | TCF7L2 knockdown or enhancer disruption reduces the allele-dependent effect. | NFIC knockdown reduces the alt-C-dependent effect. | SP1 knockdown reduces the allele-dependent effect. |

## Next experiment

Allele-specific TCF7L2 ChIP-qPCR/ChIP-SNP at chr8:127401265 in HCT116 is the cheapest single experiment that separates the top two chains, M1 and M4: M1 predicts ref T > alt C TCF7L2 occupancy, while M4 predicts no reproducible allele-specific TCF7L2 occupancy.

## Investigate calls

- chip_peaks({"biosample": "HCT116", "tf": "NFIC"})
- eqtl_lookup({"tissue": "Colon - Transverse"})
- qbic_tf_detail({"tf": "TCF7L2"})

## Flags

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

<a id="e36"></a>**E36** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr8_127401265_T_C_b38&datasetId=gtex_v8; retrieved 2026-10-26T02:23:32+00:00)

> 0 significant GTEx v8 single-tissue eQTLs for chr8_127401265_T_C_b38 in tissues matching 'Colon - Transverse'. NES is the effect of the alt allele (C) relative to ref (T).

<a id="e37"></a>**E37** qbic_tf_detail, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> {"tf":"TCF7L2","symbol":"TCF7L2","via":"hgnc_symbol","notes":[],"coverage":"mapped","variant":"chr8:127401265:T>C","gate_p":5.02e-05,"models":[{"model":"LEF1_FL_TAGTCG40NAGA_KZ_yin2017_0_3_7mer","mapping":"CIS-BP (LEF1)","group":"G041 HMG/Sox, 3 models","quality":0.63,"effect":-0.306,"z":-2.77,"p":0.0056,"rank_abs_z":"461/997","passed_gate":false,"site_strength":{"ref_percentile":81.3,"alt_percentile":95.3,"k":7}},{"model":"TCF7_eDBD_TCGGAC40NCCA_KS_yin2017_0_3_7mer","mapping":"CIS-BP (TCF7)","group":"G041 HMG/Sox, 3 models","quality":0.732,"effect":-0.429,"z":-8.8,"p":1.4e-18,"rank_abs_z":"66/997","passed_gate":true,"site_strength":{"ref_percentile":90.0,"alt_percentile":87.2,"k":7}},{"model":"TCF7L1_eDBD_TTGGCA40NTCG_KW_yin2017_0_3_7mer","mapping":"CIS-BP (TCF7L1)","group":"G041 HMG/Sox, 3 models","quality":0.602,"effect":-0.242,"z":-3.57,"p":0.00036,"rank_abs_z":"359/997","passed_gate":false,"site_strength":{"ref_percentile":84.6,"alt_percentile":58.3,"k":7}}]}
