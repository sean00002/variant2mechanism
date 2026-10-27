# rs1421085 and Obesity (FTO)

Configuration `no_qbic`, named mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.04 over 7 model calls; 271 s.

Variant `chr16:53767042:T>C` (germline); expression context: GTEx:Adipose - Subcutaneous (proxy for preadipocytes).

## Ranked chains

### 1. null: No TF-mediated effect at this base (p = 0.55)

Null chain: no TF-mediated effect of this variant.

Predictions: No allele-specific TF binding at this exact base; No reproducible adipose allele-specific effect on FTO or IRX3; The strong obesity association is due to a linked causal variant or is not TF-mediated at this base

Falsified if: Allele-specific TF binding at this exact base is demonstrated in preadipocytes; A linked causal variant is excluded and this base is shown to alter FTO or IRX3 in adipose

### 2. ARID5B_ref: ARID5B binding on ref T activates IRX3 and increases obesity risk (p = 0.25)

TF ARID5B (QBiC-SELEX coverage not_in_coverage), ref allele binds more; element dELS enhancer EH38E3181208; gene IRX3; cell type preadipocyte/adipose.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | Hypothesis: ref T binds ARID5B more strongly than alt C. ARID5B is the literature-nominated TF for this locus, but the supplied evidence has no ARID5B QBiC-SELEX model and no adipose/pre-adipocyte ARID5B ChIP peak at the variant (E19), so this allele-specific direction is not demonstrated. | missing | [E19](#e19) |
| element | The variant lies in EH38E3181208, a distal enhancer-like cCRE, consistent with a regulatory element. | supported | [E03](#e03), [E04](#e04) |
| gene | If ARID5B positively regulates IRX3 in preadipocytes, ref T would raise IRX3; E17 reports only a pancreas IRX3 eQTL where alt C raises IRX3, E21 finds no subcutaneous adipose eQTL, and E02 gives only distance, so the adipose IRX3 link is unsupported and the required activator direction is not established. | missing | [E02](#e02), [E17](#e17), [E21](#e21) |
| cell_type | The disease-relevant context is adipose/pre-adipocyte, but E04 has no ENCODE biosample matching that context and E19 finds no adipose ARID5B ChIP peak; absence is not definitive because the assay may be missing. | missing | [E04](#e04), [E19](#e19) |
| phenotype | E15 reports T as the obesity/BMI effect allele, so this chain predicts T increases risk if ARID5B activation raises an obesogenic IRX3 signal; this matches the reported T effect direction but depends on the unsupported activator assumption. | weak | [E15](#e15), [E16](#e16) |

Predictions: ARID5B binding is stronger on ref T than alt C in preadipocytes; Ref T increases IRX3 in preadipocytes if ARID5B activates IRX3; T is the obesity-increasing allele

Falsified if: Allele-specific ARID5B binding is not stronger on ref T than alt C in preadipocytes; ARID5B perturbation does not alter IRX3 in preadipocytes; Adipose eQTL/reporter shows no ref-T-dependent IRX3 effect

### 3. JUN_alt: JUN repression on alt C lowers FTO and shifts risk toward ref T (p = 0.20)

TF JUN (QBiC-SELEX coverage own_model), alt allele binds more; element dELS enhancer EH38E3181208; gene FTO; cell type preadipocyte/adipose.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | Hypothesis: alt C binds JUN more strongly than ref T. JUN is highly expressed in adipose and has a ChIP peak containing this variant only in HepG2, not adipose/pre-adipocytes (E05, E20), and no JUN QBiC-SELEX model is supplied, so allele-specific binding is unproven. | weak | [E05](#e05), [E20](#e20) |
| element | The variant lies in EH38E3181208, a distal enhancer-like cCRE, consistent with a regulatory element. | supported | [E03](#e03), [E04](#e04) |
| gene | If JUN represses FTO in preadipocytes, alt C would lower FTO and ref T would leave FTO higher; E17 reports alt C raises FTO only in skeletal muscle, E21 finds no subcutaneous adipose eQTL, and E16 is L2G/fine-mapping evidence, so the adipose repression link is unsupported. | missing | [E16](#e16), [E17](#e17), [E21](#e21) |
| cell_type | JUN is expressed in adipose (E05), but E04 and E20 show no matching adipose ENCODE ChIP peak at the variant, so occupancy in the proposed cell type is not established. | weak | [E04](#e04), [E05](#e05), [E20](#e20) |
| phenotype | E15 reports T as the obesity/BMI effect allele; this chain predicts T risk if higher FTO is obesogenic and alt C lowers FTO through JUN repression, but the adipose FTO repression direction is not supported by the supplied data. | weak | [E15](#e15), [E16](#e16) |

Predictions: JUN binding is stronger on alt C than ref T in preadipocytes; Alt C lowers FTO in preadipocytes if JUN represses FTO; T is the obesity-increasing allele because ref T has less JUN-mediated FTO repression

Falsified if: JUN binding is not stronger on alt C than ref T in preadipocytes; JUN perturbation does not alter FTO in preadipocytes; Adipose eQTL/reporter does not show alt-C-dependent FTO repression

## Prediction matrix

| Test | Cost | Separates top two | null | ARID5B_ref | JUN_alt |
| --- | --- | --- | --- | --- | --- |
| Allele-specific ARID5B binding assay in preadipocytes (EMSA, mini-reporter, or ChIP-qPCR) comparing ref T and alt C | low | yes | No allele-specific ARID5B binding at this base | Ref T binds ARID5B more strongly than alt C | No allele-specific ARID5B binding at this base |
| Allele-specific JUN binding assay in preadipocytes comparing ref T and alt C | low | no | No allele-specific JUN binding at this base | No allele-specific JUN binding at this base | Alt C binds JUN more strongly than ref T |
| Adipose/pre-adipocyte allele-specific IRX3 reporter or eQTL assay for rs1421085 ref T vs alt C | medium | yes | No reproducible adipose allele-specific IRX3 effect | Ref T increases IRX3 in preadipocytes | No reproducible adipose allele-specific IRX3 effect |
| ARID5B knockdown/knockout in preadipocytes followed by IRX3 expression | medium | yes | ARID5B perturbation does not change IRX3 | ARID5B perturbation changes IRX3 in preadipocytes | ARID5B perturbation does not change IRX3 |

## Next experiment

Cheapest separating test for the top two chains (null vs ARID5B_ref): an allele-specific ARID5B binding assay in preadipocytes comparing ref T and alt C, preferably a small reporter or EMSA with preadipocyte ChIP-qPCR confirmation. The null predicts no allele-specific ARID5B binding; ARID5B_ref predicts ref T > alt C ARID5B binding.

## Investigate calls

- chip_peaks({"biosample": "adipose", "tf": "ARID5B"})
- chip_peaks({"biosample": "adipose", "tf": "JUN"})
- eqtl_lookup({"tissue": "Adipose - Subcutaneous"})

## Flags

- quote_rejected: PMID 42440472: not an exact substring of the abstract

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

<a id="e18"></a>**E18** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=rs1421085%20AND%20FTO%20AND%20%22obesity%22&format=json&pageSize=8&resultType=core; retrieved 2026-10-25T17:29:18+00:00)

> Europe PMC: 653 hits for 'rs1421085 AND FTO AND "obesity"'; top 8 with PMIDs:
> PMID 42440472 (2026): A Rapid Genotyping Assay for &lt;i&gt;FTO&lt;/i&gt; and &lt;i&gt;PPAR-γ&lt;/i&gt; Nutrigenetic Variants in Thai Adults with Overweight/Obesity.
> PMID 41862896 (2026): Impact of fat mass and obesity-associated (FTO) gene variants on adult obesity and overweight: a comprehensive meta-analysis.
> PMID 41591493 (2026): Obesity-related RNA m&lt;sup&gt;6&lt;/sup&gt;A demethylase gene FTO rs1421085 is associated with neuroticism in a longitudinal birth cohort study.
> PMID 42197023 (2026): Associations Between FTO rs9939609 Genotype, Physical Activity, and Dietary Behaviors in Young Adults.
> PMID 42757464 (2026): Demethylase FTO attenuates atherosclerotic plaque via upregulating ABCA1 and ABCG1 expression by targeting ATG5.
> PMID 42299366 (2026): Hepatogenomics of MAFLD in Asian Population: Genetic Polymorphisms and Pathway-Based Insights.
> PMID 42534632 (2025): Genetic Polymorphisms Associated with Obesity in Southeast Asian Populations: A Systematic Review without Meta-Analysis.
> PMID 42245481 (2026): FTO in cardiovascular diseases: mechanisms, context dependence, and translational opportunities.

<a id="e19"></a>**E19** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-25T17:30:39+00:00)

> No ENCODE ARID5B ChIP-seq peak contains chr16:53767042:T>C in biosamples matching 'adipose'. Absence can also mean no ARID5B experiment in that biosample. 0 peaks lie within 100 bp without containing it.

<a id="e20"></a>**E20** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-26T02:29:32+00:00)

> No ENCODE JUN ChIP-seq peak contains chr16:53767042:T>C in biosamples matching 'adipose'. Absence can also mean no JUN experiment in that biosample. In other biosamples, 1 JUN peaks do contain the variant: HepG2 (experiments ENCSR747VUU).

<a id="e21"></a>**E21** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr16_53767042_T_C_b38&datasetId=gtex_v8; retrieved 2026-10-25T17:30:38+00:00)

> 0 significant GTEx v8 single-tissue eQTLs for chr16_53767042_T_C_b38 in tissues matching 'Adipose - Subcutaneous'. NES is the effect of the alt allele (C) relative to ref (T).
