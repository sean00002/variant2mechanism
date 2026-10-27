# rs73706717 and Colorectal cancer (8q24)

Configuration `full`, named mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.03 over 8 model calls; 151 s.

Variant `chr8:127401265:T>C` (germline); expression context: DepMap:ACH-000971 (HCT 116).

## QBiC-SELEX screen

307 of 997 models pass the gate. Top groups: C2H2 ZF, 1 model (best ZBTB22, z -33.75); E2F, 4 models (best E2F1, z 29.17); SMAD, 4 models (best NFIB, z 24.28); Homeodomain, 3 models (best HMBOX1, z -23.93); bHLH, 1 model (best MLX, z -23.15).

## Ranked chains

### 1. H4: No TF-mediated effect; linked or passenger variant, or no allelic effect (p = 0.47)

Null chain: no TF-mediated effect of this variant.

Predictions: No allele-specific TF occupancy at chr8:127401265 in HCT116.; No molecular QTL or allelic expression effect for POU5F1B or MYC in colon.; Any trait association reflects linkage or chance; E04 has no GWAS Catalog association and E05 credible sets are not colorectal cancer.

Falsified if: A direct allele-specific assay shows a reproducible TF occupancy difference at this site.; A colon molecular QTL or 3D-contact assay ties this variant to POU5F1B or MYC.; Fine-mapping identifies rs73706717 itself as causal rather than a linked variant.

### 2. H1: E2F4 binds the alt allele more strongly and, if repressive here, lowers POU5F1B (p = 0.30)

TF E2F4 (stated coverage own_model; registry own_model), alt allele binds more; element pELS; gene POU5F1B; cell type HCT116 colorectal carcinoma.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | QBiC-SELEX group G018 contains an own model for E2F4 that passes with the same sign as the best E2F1 model (E2F4 z 10.46; predicted_effect > 0), so the alt C allele is predicted to bind E2F4 more strongly. E2F4 is the highest-expressed covered E2F in the HCT116 DepMap context (134.92 TPM), which is why I select E2F4 within the shared E2F specificity rather than the best-model E2F1. | weak | [E09](#e09) |
| element | The variant lies in cCRE EH38E3858447, a proximal enhancer-like element with DNase and H3K27ac signal, and VEP annotates an ENSR8_CGMBX enhancer at this site. | supported | [E03](#e03), [E01](#e01) |
| gene | POU5F1B is the strongest L2G gene (0.83) in the credible sets containing this position and is among the cCRE-nearby genes; however those credible sets are for PSA and urinary incontinence, not colorectal cancer, and no colon transverse eQTL is reported, so the target-gene link is indirect. | weak | [E05](#e05), [E02](#e02), [E03](#e03), [E18](#e18) |
| cell_type | HCT116 is the DepMap expression context and expresses E2F4 at 134.92 TPM; the enhancer annotation is ENCODE biosample-maximum, not HCT116-specific, so activity in HCT116 is plausible but unproven. | weak | [E07](#e07), [E09](#e09), [E03](#e03) |
| phenotype | POU5F1B has literature support in colon cancer growth, invasion and angiogenesis, but CRISPR dependency in HCT116 and bowel lineage is minimal, and E2F4 repressor activity at this enhancer is not shown; the proposed direction is therefore conditional. | weak | [E06](#e06), [E20](#e20) |

Predictions: Recombinant E2F4-DP1 binds the alt oligo more strongly than ref.; Allele-specific E2F4 ChIP in HCT116 shows higher alt-allele occupancy.; If E2F4 represses this element, the alt allele lowers reporter activity and POU5F1B allelic expression.

Falsified if: Recombinant E2F4-DP1 binds ref equal to or more strongly than alt.; Allele-specific E2F4 ChIP in HCT116 shows no alt-allele occupancy preference.; The alt allele does not lower POU5F1B or reporter activity in an E2F4-dependent assay.

### 3. H2: E2F1 binds the alt allele more strongly and, if activating, raises POU5F1B (p = 0.15)

TF E2F1 (stated coverage own_model; registry own_model), alt allele binds more; element pELS; gene POU5F1B; cell type HCT116 colorectal carcinoma.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | QBiC-SELEX group G018's best model is E2F1's own model (z 29.17, effect 2.095), so the alt C allele is predicted to bind E2F1 more strongly. E2F1 is expressed in the HCT116 DepMap context at 21.43 TPM, lower than E2F4 but present. | weak | [E09](#e09) |
| element | The variant lies in cCRE EH38E3858447, a proximal enhancer-like element with DNase and H3K27ac signal, and VEP annotates an ENSR8_CGMBX enhancer at this site. | supported | [E03](#e03), [E01](#e01) |
| gene | POU5F1B is the strongest L2G gene (0.83) in the credible sets containing this position and is among the cCRE-nearby genes; however those credible sets are not colorectal cancer and no colon transverse eQTL is reported, so the target-gene link is indirect. | weak | [E05](#e05), [E02](#e02), [E03](#e03), [E18](#e18) |
| cell_type | HCT116 is the DepMap expression context and expresses E2F1 at 21.43 TPM; the enhancer annotation is ENCODE biosample-maximum, not HCT116-specific, so activity in HCT116 is plausible but unproven. | weak | [E07](#e07), [E09](#e09), [E03](#e03) |
| phenotype | POU5F1B has literature support in colon cancer growth, invasion and angiogenesis, but CRISPR dependency in HCT116 and bowel lineage is minimal, and E2F1 activator activity at this enhancer is not shown; the proposed direction is therefore conditional. | weak | [E06](#e06), [E20](#e20) |

Predictions: Recombinant E2F1 binds the alt oligo more strongly than ref.; Allele-specific E2F1 ChIP in HCT116 shows higher alt-allele occupancy.; If E2F1 activates this element, the alt allele increases reporter activity and POU5F1B allelic expression.

Falsified if: Recombinant E2F1 binds ref equal to or more strongly than alt.; Allele-specific E2F1 ChIP in HCT116 shows no alt-allele occupancy preference.; The alt allele does not increase reporter activity or POU5F1B expression in an E2F1-dependent assay.

### 4. H3: MLX binds the ref allele more strongly and, if activating, lowers POU5F1B on the alt allele (p = 0.08)

TF MLX (stated coverage own_model; registry own_model), ref allele binds more; element pELS; gene POU5F1B; cell type HCT116 colorectal carcinoma.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | QBiC-SELEX group G239 contains MLX's own model passing with z -23.15 and effect -0.809, so the ref T allele is predicted to bind MLX more strongly and the alt C allele less strongly. MLX is expressed in the HCT116 DepMap context at 74.84 TPM. | weak | [E12](#e12) |
| element | The variant lies in cCRE EH38E3858447, a proximal enhancer-like element with DNase and H3K27ac signal, and VEP annotates an ENSR8_CGMBX enhancer at this site. | supported | [E03](#e03), [E01](#e01) |
| gene | POU5F1B is the strongest L2G gene (0.83) in the credible sets containing this position and is among the cCRE-nearby genes listed in E03 (CCAT2, PCAT1, POU5F1B; MYC is only a distance-based gene in E02); however the credible sets are not colorectal cancer and no colon transverse eQTL is reported, so the target-gene link is indirect. | weak | [E05](#e05), [E02](#e02), [E03](#e03), [E18](#e18) |
| cell_type | HCT116 is the DepMap expression context and expresses MLX at 74.84 TPM; the enhancer annotation is ENCODE biosample-maximum, not HCT116-specific, so activity in HCT116 is plausible but unproven. | weak | [E07](#e07), [E12](#e12), [E03](#e03) |
| phenotype | POU5F1B has literature support in colon cancer growth, invasion and angiogenesis, but CRISPR dependency in HCT116 and bowel lineage is minimal, and MLX activator versus repressor activity at this element is not shown; the simplest chain assumes MLX supports the element, so reduced alt binding lowers POU5F1B. | weak | [E06](#e06), [E20](#e20) |

Predictions: Recombinant MLX binds the ref oligo more strongly than alt.; Allele-specific MLX ChIP shows higher ref-allele occupancy.; If MLX activates this element, the alt allele lowers reporter activity and POU5F1B allelic expression.

Falsified if: Recombinant MLX binds alt equal to or more strongly than ref.; Allele-specific MLX ChIP in colorectal cells shows no ref-allele occupancy preference.; The alt allele does not lower reporter activity or POU5F1B in an MLX-dependent assay.

## Prediction matrix

| Test | Cost | Separates top two | H4 | H1 | H2 | H3 |
| --- | --- | --- | --- | --- | --- | --- |
| Recombinant E2F4-DP1 EMSA or fluorescence polarization with ref versus alt oligos | low | yes | No allele-specific E2F4 binding difference. | Alt oligo binds recombinant E2F4-DP1 more strongly than ref. | No E2F4-specific prediction; if anything, the E2F1 model, not E2F4, is the primary alt-binding factor. | No E2F4 allele-specific binding difference; MLX, not E2F4, is the proposed allele-sensitive factor. |
| Allele-specific E2F4 ChIP-qPCR at chr8:127401265 in HCT116 | medium | yes | No reproducible allele-specific TF occupancy. | Alt allele shows higher E2F4 occupancy at the variant element. | No E2F4 allelic occupancy effect; E2F1 would be the relevant E2F. | No E2F4 allelic occupancy effect. |
| Ref versus alt pELS reporter assay in HCT116 with E2F4 knockdown | medium | yes | No allele-dependent reporter difference. | Alt reporter is lower if E2F4 represses; E2F4 knockdown increases activity and blunts the alt-lower effect. | Alt reporter is higher if E2F1 activates; E2F4 knockdown has little effect. | Alt reporter is lower if MLX activates; E2F4 knockdown has little effect. |
| Recombinant MLX EMSA or allele-specific MLX ChIP at the variant | low | no | No allele-specific MLX binding difference. | No MLX allele-specific binding difference. | No MLX allele-specific binding difference. | Ref binds MLX more strongly than alt. |
| Colon or HCT116 allelic expression assay for POU5F1B in heterozygous samples | medium | yes | No allelic expression effect on POU5F1B. | Alt allele associates with lower POU5F1B allelic expression. | Alt allele associates with higher POU5F1B allelic expression. | Alt allele associates with lower POU5F1B allelic expression if MLX activates the element. |

## Next experiment

Single cheapest experiment that separates the top two chains H4 and H1: recombinant E2F4-DP1 EMSA or fluorescence polarization with ref versus alt oligos. H1 predicts stronger alt binding; H4 predicts no allele-specific E2F4 binding. This is an in vitro binding test and would not by itself establish cellular occupancy or phenotype.

## Investigate calls

- eqtl_lookup({"tissue": "Colon - Transverse"})
- chip_peaks({"biosample": "HCT116", "tf": "E2F4"})
- gene_dependency({"gene": "POU5F1B"})

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

<a id="e04"></a>**E04** gwas_lookup, GWAS Catalog REST v2 (https://www.ebi.ac.uk/gwas/rest/api/v2/associations?rs_id=rs73706717&size=100; retrieved 2026-10-26T02:21:56+00:00)

> 0 GWAS Catalog associations for rs73706717, strongest first:

<a id="e05"></a>**E05** finemap_lookup, Open Targets Platform (credible sets, L2G) (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-26T02:21:56+00:00)

> 2 credible sets contain 8_127401265_T_C: 2 GWAS, 0 molecular QTL.
> GWAS prostate-specific antigen (PSA, maximum, inv-norm transforme: PIP 0.04; L2G POU5F1B 0.83
> GWAS Urinary incontinence (PheCode 599.4): PIP 0.04; L2G POU5F1B 0.78
> Best L2G gene scores across these sets: POU5F1B 0.83

<a id="e06"></a>**E06** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=POU5F1B%20AND%20%22colorectal%20cancer%22&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T02:21:59+00:00)

> Europe PMC: 150 hits for 'POU5F1B AND "colorectal cancer"'; top 8 with PMIDs:
> PMID 42465001 (2026): Circ_0075829 affects POU5F1B expression through sponging miR-576-3p to promote growth, invasion, and angiogenesis of colon cancer cells.
> PMID 41993623 (2026): Tailorable porous collagen hydrogels as a physiologically relevant platform for extrachromosomal DNA-associated colorectal cancer research.
> PMID 41796348 (2026): Harnessing the LncRNA CCAT2 role in gastric cancer: from molecular insights to clinical implications.
> PMID 41930642 (2026): Systematic Identification and Characterization of Causal Risk Genes Implicated in Colorectal Cancer by Integrating GWAS, eQTL, and mQTL Data.
> PMID 42686757 (2026): Phase separation of ecDNA condensates establishes in-trans contact domains that boost selective MYC regulatory interactions.
> PMID 40506516 (2025): Association between methylation quantitative trait loci and colorectal cancer risk, survival and cancer recurrence.
> PMID 41144378 (2025): Integrative GWAS and RNA-Seq analysis for target identification and virtual drug screening in colorectal cancer.
> PMID 41196428 (2025): Combined CHK1 and PD-L1 blockade as a novel therapeutic strategy against stemness and immunosuppression in ovarian cancer.

<a id="e07"></a>**E07** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> QBiC-SELEX screen of chr8:127401265:T>C: 997 models scored, 307 pass the gate (Bonferroni 0.05/997, p < 5.02e-05, |z| > 4.05), in 217 CIS-BP groups. Expression context: DepMap line ACH-000971. Groups shown: 10; dropped because no TF in the group reaches 1 TPM: 62 (C2H2 ZF, 1 model z 48.28, bHLH, 2 models z -21.14, bHLH, 1 model z -20.92, C2H2 ZF, 2 models z -15.35, bHLH, 1 model z -14.88). Passing groups ranked below the ones shown: 145. In the group rows, 'own model' means the TF has its own QBiC-SELEX model and 'mapped' that it is covered only through CIS-BP-mapped models of related TFs. A TF not named in any group row may still have its own model, even one that passes the gate: look it up with qbic_tf_detail before stating its coverage or a QBiC-SELEX direction for it. predicted_effect > 0 means the alternate allele binds more strongly. In vitro binding only: expression and chromatin decide whether a change matters.

<a id="e08"></a>**E08** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G395 (C2H2 ZF, 1 model): best model ZBTB22_eDBD_TGCCTC40NCAA_KP_yin2017_0_4_7mer (own model of ZBTB22), z -33.75, effect -1.962 (alt binds less); 1 passing models (1 with the best model's sign). Passing members: ZBTB22 z -33.75. TFs this group covers: ZBTB22 (own model) 3.74 TPM; best model's site strength: ref 99.8th, alt 92.4th percentile of its k-mer coefficients.

<a id="e09"></a>**E09** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G018 (E2F, 4 models): best model E2F1_NA_CAATT14N_ESU_yang2017_0_4_7mer (own model of E2F1), z 29.17, effect 2.095 (alt binds more); 3 passing models (3 with the best model's sign). Passing members: E2F1 z 29.17, E2F2 z 12.62, E2F4 z 10.46. TFs this group covers: E2F4 (own model) 134.92 TPM, E2F6 (mapped) 31.36 TPM, E2F3 (own model) 28.76 TPM, E2F1 (own model) 21.43 TPM, E2F5 (mapped) 13.57 TPM, E2F2 (own model) 12.62 TPM; best model's site strength: ref 89.4th, alt 99.9th percentile of its k-mer coefficients.

<a id="e10"></a>**E10** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G027 (SMAD, 4 models): best model NFIB_NA_TCATCA20NCG_ESAD_yang2017_0_3_7mer (own model of NFIB), z 24.28, effect 1.783 (alt binds more); 4 passing models (4 with the best model's sign). Passing members: NFIB z 24.28, NFIX z 23.96, NFIC z 23.35, NFIA z 11.49. TFs this group covers: NFIC (own model) 36.29 TPM, NFIX (own model) 13.23 TPM, NFIA (own model) 7.07 TPM, NFIB (own model) 2.12 TPM; best model's site strength: ref 96.3th, alt 99.5th percentile of its k-mer coefficients.

<a id="e11"></a>**E11** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G038 (Homeodomain, 3 models): best model HMBOX1_eDBD_TGGCTC40NCGC_KAN_yin2017_1_2_7mer (own model of HMBOX1), z -23.93, effect -0.32 (alt binds less); 1 passing models (1 with the best model's sign). Passing members: HMBOX1 z -23.93. TFs this group covers: HMBOX1 (own model) 8.15 TPM, HNF1B (own model) 2.08 TPM, HNF1A (own model) 0.02 TPM; best model's site strength: ref 100.0th, alt 67.8th percentile of its k-mer coefficients.

<a id="e12"></a>**E12** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G239 (bHLH, 1 model): best model MLX_eDBD_TAGGCT40NACC_KAN_yin2017_0_4_6mer (own model of MLX), z -23.15, effect -0.809 (alt binds less); 1 passing models (1 with the best model's sign). Passing members: MLX z -23.15. TFs this group covers: MLX (own model) 74.84 TPM; best model's site strength: ref 99.4th, alt 90.5th percentile of its k-mer coefficients.

<a id="e13"></a>**E13** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G051 (bHLH, 3 models): best model TCF12_eDBD_TTTGAG40NATT_KS_yin2017_0_3_7mer (own model of TCF12), z -22.53, effect -1.05 (alt binds less); 2 passing models (2 with the best model's sign). Passing members: TCF12 z -22.53, TCF3 z -6.22. TFs this group covers: TCF3 (own model) 111.29 TPM, TCF12 (own model) 40.64 TPM, TCF4 (own model) 0.23 TPM; best model's site strength: ref 99.6th, alt 99.5th percentile of its k-mer coefficients.

<a id="e14"></a>**E14** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G468 (C2H2 ZF, 1 model): best model ZNF263_eDBD_TTAGAT40NGTG_KS_yin2017_0_4_7mer (own model of ZNF263), z -20.79, effect -0.757 (alt binds less); 1 passing models (1 with the best model's sign). Passing members: ZNF263 z -20.79. TFs this group covers: ZNF263 (own model) 36.75 TPM; best model's site strength: ref 100.0th, alt 85.3th percentile of its k-mer coefficients.

<a id="e15"></a>**E15** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G250 (Myb/SANT, 1 model): best model MYPOP_FL_CC40NTGAGTA_YWO_jolma2025_0_2_7mer (own model of MYPOP), z 16.88, effect 0.569 (alt binds more); 1 passing models (1 with the best model's sign). Passing members: MYPOP z 16.88. TFs this group covers: MYPOP (own model) 5.37 TPM; best model's site strength: ref 84.9th, alt 98.8th percentile of its k-mer coefficients.

<a id="e16"></a>**E16** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G002 (Nuclear receptor, 29 models): best model NR1H3_DBD_TGAGCG40NTTG_KY_nitta2015_2_3_7mer (own model of NR1H3), z -15.02, effect -0.286 (alt binds less); 13 passing models (12 with the best model's sign); members disagree on direction. Passing members: NR1H3 z -15.02, NR2C1 z -13.82, RORB z -13.43, RORC z -7.66, NR2F6 z -7.56 (+8 more). TFs this group covers: NR2F2 (own model) 61.74 TPM, PPARG (own model) 47.9 TPM, ESRRA (own model) 38.54 TPM, NR1D2 (own model) 37.06 TPM, NR2F6 (own model) 37.02 TPM, RARG (own model) 31.32 TPM, NR2F1 (own model) 28.42 TPM, NR2C2 (own model) 22.6 TPM, NR1H2 (mapped) 20.86 TPM, PPARD (own model) 20.8 TPM (+28 more); best model's site strength: ref 95.9th, alt 60.2th percentile of its k-mer coefficients.

<a id="e17"></a>**E17** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G064 (CxxC, 2 models): best model CXXC4_FL_GG40NTAGTTT_YWKC_jolma2025_0_4_7mer (own model of CXXC4), z 14.12, effect 0.794 (alt binds more); 2 passing models (2 with the best model's sign). Passing members: CXXC4 z 14.12, TET3 z 7.27. TFs this group covers: CXXC5 (mapped) 25.91 TPM, TET3 (own model) 10.17 TPM, CXXC4 (own model) 0.23 TPM; best model's site strength: ref 87.7th, alt 96.6th percentile of its k-mer coefficients.

<a id="e18"></a>**E18** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr8_127401265_T_C_b38&datasetId=gtex_v8; retrieved 2026-10-26T02:23:32+00:00)

> 0 significant GTEx v8 single-tissue eQTLs for chr8_127401265_T_C_b38 in tissues matching 'Colon - Transverse'. NES is the effect of the alt allele (C) relative to ref (T).

<a id="e19"></a>**E19** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-26T02:26:46+00:00)

> No ENCODE E2F4 ChIP-seq peak contains chr8:127401265:T>C in biosamples matching 'HCT116'. Absence can also mean no E2F4 experiment in that biosample. 0 peaks lie within 100 bp without containing it.

<a id="e20"></a>**E20** gene_dependency, DepMap CRISPRGeneEffect (Biomni copy) and CRISPRInferredCommonEssentials (Public 26Q3) (local files; retrieved local)

> DepMap CRISPR gene effect for POU5F1B (0 = no effect, -1 = median common-essential; < -0.5 called dependent). HCT 116 (ACH-000971): -0.09. Bowel lineage, 31 lines: median -0.06, 0% dependent. All 351 lines: median -0.05, 3% dependent.
