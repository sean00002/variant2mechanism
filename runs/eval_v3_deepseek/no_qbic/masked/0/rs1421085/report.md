# rs1421085 and Obesity (FTO)

Configuration `no_qbic`, masked mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.05 over 7 model calls; 306 s.

Variant `chr16:53767042:T>C` (germline); expression context: GTEx:Adipose - Subcutaneous (proxy for preadipocytes).

## Ranked chains

### 1. H0: Null: no TF-mediated allelic effect at this base; the obesity signal reflects a linked causal variant or passenger intronic variant (p = 0.42)

Null chain: no TF-mediated effect of this variant.

Predictions: No allele-specific TF binding at this base in adipose/pre-adipocytes.; The GWAS signal is explained by a linked causal variant elsewhere in the credible set or by a passenger variant in an active enhancer.; Reporter assays show no allelic enhancer activity difference for T versus C at this base.

Falsified if: Reproducible allele-specific TF occupancy or enhancer activity at this exact base in preadipocytes would argue against the null.; Fine-mapping and functional assays show that this variant, not a linked variant, drives the FTO/IRX3 regulatory change.

### 2. H1: JUN/AP-1 binds the ref T allele at the FTO intronic dELS and represses FTO, making T risk via lower FTO (p = 0.27)

TF JUN (QBiC-SELEX coverage own_model), ref allele binds more; element EH38E3181208 dELS in FTO intron 1; gene FTO; cell type Subcutaneous adipose / preadipocytes (GTEx adipose expression proxy).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | No QBiC-SELEX model is provided for JUN, and no subcutaneous-adipose JUN ChIP peak contains the variant (E20); the only JUN peak is in HepG2 (E05). JUN is highly expressed in GTEx subcutaneous adipose (E05), so I propose that the ref T allele binds JUN more strongly, but this direction is inferred and weak. | missing | [E04](#e04), [E05](#e05), [E20](#e20) |
| element | The variant lies in EH38E3181208, a distal enhancer-like cCRE, with nearby active-enhancer cofactor and Pol II marks, supporting a regulatory element rather than a passive intronic site. | supported | [E03](#e03), [E04](#e04) |
| gene | FTO is the top L2G gene for BMI/obesity credible sets (0.99). The skeletal-muscle FTO eQTL shows alt C increases FTO, i.e. T is associated with lower FTO, which is consistent with JUN repressing FTO. However, there is no significant subcutaneous-adipose eQTL for this variant (E19) and no JUN perturbation of FTO. | weak | [E02](#e02), [E16](#e16), [E17](#e17), [E18](#e18), [E19](#e19) |
| cell_type | The proposed cell type is subcutaneous adipose/pre-adipocyte, where JUN is highly expressed and the cCRE is active by ENCODE annotation; however, E20 shows no matching adipose JUN ChIP peak, so adipose occupancy at this base is unproven. | weak | [E03](#e03), [E05](#e05), [E20](#e20) |
| phenotype | GWAS strongly associates the T allele with higher BMI and obesity (e.g. BMI p 9.9e-324, effect allele T), so the phenotype link is T-risk allele to obesity. | supported | [E15](#e15) |

Predictions: Allele-specific JUN ChIP or reporter in subcutaneous preadipocytes should show ref T > alt C JUN binding at this base.; JUN knockdown should increase FTO expression if JUN represses this enhancer.; The T risk allele should associate with lower FTO expression in adipose tissue, consistent with the skeletal-muscle eQTL direction.

Falsified if: Allele-specific JUN ChIP or reporter in preadipocytes shows no ref-T-preferring JUN binding at this base.; JUN depletion does not change FTO expression in preadipocytes, or JUN activation raises rather than lowers FTO.; Adipose eQTL/colocalization shows the T allele raises FTO rather than lowering it.

### 3. H2: KLF6 binds the alt C allele at the FTO intronic dELS and activates FTO, making alt C protective (p = 0.23)

TF KLF6 (QBiC-SELEX coverage own_model), alt allele binds more; element EH38E3181208 dELS in FTO intron 1; gene FTO; cell type Subcutaneous adipose / preadipocytes (GTEx adipose expression proxy).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | No QBiC-SELEX model is provided for KLF6, and no subcutaneous-adipose KLF6 ChIP peak contains the variant (E21); the only KLF6 peak is in HepG2 (E06). KLF6 is highly expressed in GTEx subcutaneous adipose (E06), so I propose that the alt C allele binds KLF6 more strongly, but this direction is inferred and weak. | missing | [E04](#e04), [E06](#e06), [E21](#e21) |
| element | The variant lies in EH38E3181208, a distal enhancer-like cCRE, with nearby active-enhancer cofactor and Pol II marks, consistent with a KLF6-responsive enhancer element. | supported | [E03](#e03), [E04](#e04) |
| gene | FTO is the top L2G gene (0.99), and the skeletal-muscle FTO eQTL shows alt C increases FTO, consistent with alt C enhancing FTO through KLF6. However, E19 finds no significant subcutaneous-adipose eQTL and there is no KLF6 perturbation of FTO. | weak | [E02](#e02), [E16](#e16), [E17](#e17), [E18](#e18), [E19](#e19) |
| cell_type | The proposed cell type is subcutaneous adipose/pre-adipocyte, where KLF6 is highly expressed and the cCRE is active by ENCODE annotation; however, E21 shows no matching adipose KLF6 ChIP peak, so adipose occupancy at this base is unproven. | weak | [E03](#e03), [E06](#e06), [E21](#e21) |
| phenotype | GWAS assigns the T allele as the effect/risk allele for BMI and obesity, so this chain requires the alt C allele to be protective through higher KLF6-driven FTO expression. | supported | [E15](#e15) |

Predictions: Allele-specific KLF6 ChIP or reporter in subcutaneous preadipocytes should show alt C > ref T KLF6 binding at this base.; KLF6 knockdown should lower FTO expression if KLF6 activates this enhancer.; The alt C allele should associate with higher FTO expression in adipose tissue.

Falsified if: Allele-specific KLF6 ChIP or reporter in preadipocytes shows no alt-C-preferring KLF6 binding at this base.; KLF6 depletion does not lower FTO expression in preadipocytes.; Adipose eQTL/colocalization shows alt C lowers rather than raises FTO.

### 4. H3: ATF3 binds the ref T allele at the FTO intronic dELS and activates FTO, making T risk via higher FTO (p = 0.08)

TF ATF3 (QBiC-SELEX coverage own_model), ref allele binds more; element EH38E3181208 dELS in FTO intron 1; gene FTO; cell type Subcutaneous adipose / preadipocytes (GTEx adipose expression proxy).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | No QBiC-SELEX model is provided for ATF3, and no subcutaneous-adipose ATF3 ChIP peak contains the variant; the only ATF3 peak is in HCT116 (E09). ATF3 is expressed in GTEx subcutaneous adipose, so I weakly infer that the ref T allele binds ATF3 more strongly, but this is not measured. | missing | [E04](#e04), [E09](#e09) |
| element | The variant lies in EH38E3181208, a distal enhancer-like cCRE with active-enhancer marks, consistent with an ATF3-responsive regulatory element. | supported | [E03](#e03), [E04](#e04) |
| gene | FTO is the top L2G gene (0.99), but the skeletal-muscle FTO eQTL shows alt C increases FTO, which conflicts with H3's required direction that T activates FTO. E19 finds no significant subcutaneous-adipose eQTL to resolve the direction. | missing | [E16](#e16), [E17](#e17), [E19](#e19) |
| cell_type | The proposed cell type is subcutaneous adipose/pre-adipocyte, where ATF3 is expressed and the cCRE is active by ENCODE annotation; however, there is no matching adipose ATF3 ChIP peak. | weak | [E03](#e03), [E09](#e09) |
| phenotype | GWAS strongly associates the T allele with higher BMI and obesity, so this chain requires T to increase FTO activity if FTO activation is the risk direction. | supported | [E15](#e15) |

Predictions: Allele-specific ATF3 ChIP or reporter in subcutaneous preadipocytes should show ref T > alt C ATF3 binding.; ATF3 knockdown should lower FTO expression if ATF3 activates this enhancer.; Adipose eQTL should show the T risk allele associated with higher FTO, contrary to the skeletal-muscle alt-C-increasing FTO eQTL.

Falsified if: Allele-specific ATF3 ChIP or reporter in preadipocytes shows no ref-T-preferring ATF3 binding at this base.; ATF3 depletion does not change FTO expression in preadipocytes.; Adipose eQTL shows the T risk allele lowers rather than raises FTO, as the conflicting E17 direction already suggests.

## Prediction matrix

| Test | Cost | Separates top two | H0 | H1 | H2 | H3 |
| --- | --- | --- | --- | --- | --- | --- |
| Allele-specific JUN ChIP or reporter assay in subcutaneous preadipocytes | medium | yes | No allele-specific TF binding at this base. | Ref T > alt C JUN binding at this base. | No JUN allelic binding; KLF6 is the proposed allele-specific factor. | No JUN allelic binding; ATF3 remains the proposed factor. |
| Allele-specific KLF6 ChIP or reporter assay in subcutaneous preadipocytes | medium | yes | No allele-specific TF binding at this base. | No KLF6 allelic binding; JUN is the proposed allele-specific factor. | Alt C > ref T KLF6 binding at this base. | No KLF6 allelic binding; ATF3 remains the proposed factor. |
| siRNA knockdown of JUN and KLF6 in subcutaneous preadipocytes, followed by FTO qPCR | low | yes | No change in FTO after JUN or KLF6 knockdown. | JUN knockdown increases FTO; KLF6 knockdown has no effect. | KLF6 knockdown decreases FTO; JUN knockdown has no effect. | ATF3 knockdown, not JUN or KLF6 knockdown, would be expected to change FTO. |
| Adipose eQTL/colocalization for FTO and IRX3 at this variant | existing data | no | No adipose allelic effect on FTO or IRX3; current E19 is consistent but underpowered. | Adipose eQTL should show alt C higher FTO / T lower FTO; current data show no significant subcutaneous-adipose eQTL (E19), so this remains unresolved. | Adipose eQTL should show alt C higher FTO; current data show no significant subcutaneous-adipose eQTL (E19), so this remains unresolved. | Adipose eQTL should show T higher FTO, which conflicts with the skeletal-muscle alt-C-increasing FTO eQTL (E17). |

## Next experiment

Cheapest experiment separating H1 from H2: in subcutaneous preadipocytes, knock down JUN and KLF6 separately and measure FTO expression. H1 predicts JUN depletion increases FTO, whereas H2 predicts KLF6 depletion decreases FTO.

## Investigate calls

- eqtl_lookup({"tissue": "Adipose - Subcutaneous"})
- chip_peaks({"tf": "JUN", "biosample": "Subcutaneous adipose"})
- chip_peaks({"tf": "KLF6", "biosample": "Subcutaneous adipose"})

## Flags

- quote_rejected: PMID dsf: not an exact substring of the abstract

Citation support: 1.00 of links cite only evidence that passed every check.

## Evidence

<a id="e01"></a>**E01** variant_annotation, Ensembl VEP (GRCh38) (https://rest.ensembl.org/vep/human/region/16:53767042-53767042:1/C?content-type=application/json&Conservation=1; retrieved 2026-10-25T17:38:25+00:00)

> Variant chr16:53767042:T>C (GRCh38), allele string T/C
> Known IDs: rs1421085
> Most severe consequence: intron_variant
> Regulatory features: none
> GERP conservation score at the site: 2.55
> Transcript consequences: FTO (intron_variant, NMD_transcript_variant); FTO (intron_variant); FTO (intron_variant, non_coding_transcript_variant)

<a id="e02"></a>**E02** nearest_genes, Ensembl overlap (protein_coding) (https://rest.ensembl.org/overlap/region/human/16:52767042-54767042?feature=gene;biotype=protein_coding;content-type=application/json; retrieved 2026-10-25T17:38:17+00:00)

> 7 protein-coding genes within 1000 kb of chr16:53767042:T>C, by distance to TSS:
> RPGRIP1L: 63.1 kb from TSS (upstream, strand -1)
> FTO: 65.3 kb from TSS (in gene body, strand +1)
> AKTIP: 262.6 kb from TSS (upstream, strand -1)
> RBL2: 333.1 kb from TSS (downstream, strand +1)
> IRX3: 520.4 kb from TSS (downstream, strand -1)
> CHD9: 712.1 kb from TSS (downstream, strand +1)
> CHD9NB: 714.1 kb from TSS (upstream, strand -1)

<a id="e03"></a>**E03** ccre_lookup, ENCODE v4 cCRE registry (ENCFF420VPZ) and SCREEN (https://screen-beta-api.wenglab.org/dataws/cre_table; retrieved 2026-10-25T17:29:02+00:00)

> The variant lies in cCRE EH38E3181208 (dELS: distal enhancer-like), chr16:53766999-53767220.
> SCREEN: 1 cCREs within 500 bp (max z-score across ENCODE biosamples):
> EH38E3181207 dELS: DNase z 3.5, H3K27ac z 3.2, H3K4me3 z 1.5, CTCF z 1.5; nearby genes RPGRIP1L, FTO, AC007497.1
> Biosample-specific z-scores are not in this call; the values above are maxima over biosamples.

<a id="e04"></a>**E04** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> ENCODE TF ChIP-seq at chr16:53767042:T>C: 39 peaks contain the variant, from 37 factors in 4 biosamples. No ENCODE biosample matches the expression context, so no peak counts as bound here. cCRE class at the variant: dELS. Bound factors outside the TF model collection (co-factors, Pol II, and TFs with no binding model; signs of an active element, not TF candidates): ASH2L, DMAP1, EHMT2, EP300, HBP1, IKZF5, KAT2B, LCORL, MED1, POLR2AphosphoS5, RBFOX2, RNF219 (+6 more). Bound, expressed TFs with a binding model: 16; listed one per row: JUN, KLF6, USF2, HMG20B, ATF3, MAX, SP1, TEAD1, ZGPAT, GATAD2A; also bound: PHF21A, ZNF335, FOXP1, ZNF449, ZNF280D, ZNF48. Bound but below 1 TPM: HNF1A, MIXL1, ONECUT1. Assayed with no peak here: 0 TFs in the matching biosample, 554 only elsewhere; never assayed: 536.

<a id="e05"></a>**E05** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> JUN: bound elsewhere. 1 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: HepG2 (e.g. ENCSR747VUU). 442.88 TPM in GTEx:Adipose - Subcutaneous (proxy for preadipocytes), rank 3 of 1631 TFs.

<a id="e06"></a>**E06** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> KLF6: bound elsewhere. 1 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: HepG2 (e.g. ENCSR757EKM). 247.5 TPM in GTEx:Adipose - Subcutaneous (proxy for preadipocytes), rank 11 of 1631 TFs.

<a id="e07"></a>**E07** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> USF2: bound elsewhere. 1 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: HepG2 (e.g. ENCSR145QNL). 114.23 TPM in GTEx:Adipose - Subcutaneous (proxy for preadipocytes), rank 31 of 1631 TFs.

<a id="e08"></a>**E08** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> HMG20B: bound elsewhere. 1 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: HepG2 (e.g. ENCSR925QAW). 84.43 TPM in GTEx:Adipose - Subcutaneous (proxy for preadipocytes), rank 51 of 1631 TFs.

<a id="e09"></a>**E09** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> ATF3: bound elsewhere. 1 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: HCT116 (e.g. ENCSR000BUG). 57.63 TPM in GTEx:Adipose - Subcutaneous (proxy for preadipocytes), rank 88 of 1631 TFs.

<a id="e10"></a>**E10** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> MAX: bound elsewhere. 1 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: HepG2 (e.g. ENCSR168DYA). 41.99 TPM in GTEx:Adipose - Subcutaneous (proxy for preadipocytes), rank 141 of 1631 TFs.

<a id="e11"></a>**E11** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> SP1: bound elsewhere. 1 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: HCT116 (e.g. ENCSR000BSF). 41.01 TPM in GTEx:Adipose - Subcutaneous (proxy for preadipocytes), rank 145 of 1631 TFs.

<a id="e12"></a>**E12** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> TEAD1: bound elsewhere. 1 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: HepG2 (e.g. ENCSR497JLX). 40.88 TPM in GTEx:Adipose - Subcutaneous (proxy for preadipocytes), rank 148 of 1631 TFs.

<a id="e13"></a>**E13** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> ZGPAT: bound elsewhere. 1 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: HepG2 (e.g. ENCSR704IGU). 30.27 TPM in GTEx:Adipose - Subcutaneous (proxy for preadipocytes), rank 211 of 1631 TFs.

<a id="e14"></a>**E14** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> GATAD2A: bound elsewhere. 1 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: HepG2 (e.g. ENCSR925BFV). 25.37 TPM in GTEx:Adipose - Subcutaneous (proxy for preadipocytes), rank 260 of 1631 TFs.

<a id="e15"></a>**E15** gwas_lookup, GWAS Catalog REST v2 (https://www.ebi.ac.uk/gwas/rest/api/v2/associations?rs_id=rs1421085&size=100; retrieved 2026-10-25T17:29:17+00:00)

> 100 GWAS Catalog associations for rs1421085, strongest first:
> Body mass index (BMI, mean, inv-normal transformed): p 9.9e-324, effect allele T, risk-allele frequency 0.669, PMID 39024449
> Body mass index (BMI, maximum, inv-normal transformed): p 9.9e-324, effect allele T, risk-allele frequency 0.669, PMID 39024449
> What is your weight? (pounds, inv-normal transformed): p 9.9e-324, effect allele T, risk-allele frequency 0.5909, PMID 39024449
> Weight (mean, inv-normal transformed): p 2.0e-300, effect allele T, risk-allele frequency 0.669, PMID 39024449
> Obesity (PheCode 278.1): p 6.0e-291, effect allele T, risk-allele frequency 0.593, PMID 39024449
> Body mass index (BMI, minimum, inv-normal transformed): p 2.0e-277, effect allele T, risk-allele frequency 0.669, PMID 39024449
> Overweight, obesity and other hyperalimentation (PheCode 278): p 4.0e-246, effect allele T, risk-allele frequency 0.5927, PMID 39024449
> Body shape phenotype PC1: p 2.0e-241, effect allele T, risk-allele frequency 0.596423, PMID 38640244
> Type 2 diabetes (PheCode 250.2): p 4.0e-211, effect allele T, risk-allele frequency 0.5926, PMID 39024449
> Diabetes mellitus (PheCode 250): p 8.0e-207, effect allele T, risk-allele frequency 0.5926, PMID 39024449
> Hemoglobin A1c (HbA1c, maximum, inv-norm transformed): p 8.0e-195, effect allele T, risk-allele frequency 0.5901, PMID 39024449
> Hemoglobin A1c (HbA1c, mean, inv-norm transformed): p 1.0e-185, effect allele T, risk-allele frequency 0.5901, PMID 39024449

<a id="e16"></a>**E16** finemap_lookup, Open Targets Platform (credible sets, L2G) (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-25T17:29:10+00:00)

> 1701 credible sets contain 16_53767042_T_C: 200 GWAS, 0 molecular QTL.
> GWAS Body mass index (BMI, minimum, inv-normal transformed): PIP 0.85; L2G FTO 0.99, RPGRIP1L 0.20, CHD9 0.06
> GWAS Body mass index: PIP 0.80; L2G FTO 0.99, RPGRIP1L 0.25
> GWAS Impedance of leg left (UKB data field 23108): PIP 0.67; L2G FTO 0.99, RPGRIP1L 0.20
> GWAS Diabetes mellitus (PheCode 250): PIP 0.46; L2G FTO 0.99, RPGRIP1L 0.20, CHD9 0.06
> GWAS Impedance of leg left (UKB data field 23108): PIP 0.46; L2G FTO 0.99, RPGRIP1L 0.20
> GWAS Leg fat free mass left (UKB data field 23117): PIP 0.41; L2G FTO 0.99, RPGRIP1L 0.21, CHD9 0.07
> Best L2G gene scores across these sets: FTO 0.99, RPGRIP1L 0.36, CHD9 0.16

<a id="e17"></a>**E17** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr16_53767042_T_C_b38&datasetId=gtex_v8; retrieved 2026-10-25T17:30:38+00:00)

> 2 significant GTEx v8 single-tissue eQTLs for chr16_53767042_T_C_b38. NES is the effect of the alt allele (C) relative to ref (T).
> FTO in Muscle_Skeletal: NES +0.14, p 7.5e-08
> IRX3 in Pancreas: NES +0.37, p 8.3e-06

<a id="e18"></a>**E18** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=FTO%20AND%20%22obesity%22&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T20:20:08+00:00)

> Europe PMC: 11476 hits for 'FTO AND "obesity"'; top 7 with PMIDs:
> PMID 42861203 (2026): Circulating FTO Protein Levels and β-Cell Function in Individuals with Different Metabolic Profiles: A Cross- Sectional Study.
> PMID 42866557 (2026): FTO-Mediated m6A Demethylation in Insulin Resistance and Type 2 Diabetes: Tissue-Specific Mechanisms - a Narrative Review.
> PMID 42860309 (2026): Mogroside V Promotes Brown Adipose Thermogenesis via FTO-m&lt;sup&gt;6&lt;/sup&gt;A-LETMD1-UCP1 Pathway to Combat Obesity.
> PMID 42708306 (2026): Fat Mass and Obesity Associated (FTO) and Melanocortin 4 Receptor (MC4R) Gene Variants as Prognostic Markers of Obesity in Quetta City.
> PMID 42893248 (2026): Genetic and Body Composition Factors Associated with Metabolic-Associated Steatotic Liver Disease: A Cross-Sectional Analysis of a Health Screening Cohort.
> PMID 42790767 (2026): RNA m6A demethylase FTO in central nervous system disorders: Mechanisms and therapeutic implications.
> PMID 42747632 (2026): FTO-mediated GPX4 m6A modification in ferroptosis-induced DNA damage and inflammatory response during acute lung injury.

<a id="e19"></a>**E19** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr16_53767042_T_C_b38&datasetId=gtex_v8; retrieved 2026-10-25T17:30:38+00:00)

> 0 significant GTEx v8 single-tissue eQTLs for chr16_53767042_T_C_b38 in tissues matching 'Adipose - Subcutaneous'. NES is the effect of the alt allele (C) relative to ref (T).

<a id="e20"></a>**E20** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-26T02:29:32+00:00)

> No ENCODE JUN ChIP-seq peak contains chr16:53767042:T>C in biosamples matching 'Subcutaneous adipose'. Absence can also mean no JUN experiment in that biosample. In other biosamples, 1 JUN peaks do contain the variant: HepG2 (experiments ENCSR747VUU).

<a id="e21"></a>**E21** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-26T13:25:56+00:00)

> No ENCODE KLF6 ChIP-seq peak contains chr16:53767042:T>C in biosamples matching 'Subcutaneous adipose'. Absence can also mean no KLF6 experiment in that biosample. In other biosamples, 1 KLF6 peaks do contain the variant: HepG2 (experiments ENCSR757EKM).
