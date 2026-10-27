# rs1421085 and Obesity (FTO)

Configuration `no_qbic`, masked mode, seed 0. Models: generator openai/gpt-6-luna, critic openai/gpt-6-luna, summariser openai/gpt-6-luna. Cost $0.02 over 8 model calls; 193 s.

Variant `chr16:53767042:T>C` (germline); expression context: GTEx:Adipose - Subcutaneous (proxy for preadipocytes).

## Ranked chains

### 1. H1: Null: no TF-mediated effect of this variant (p = 0.86)

Null chain: no TF-mediated effect of this variant.

Predictions: The T>C change has no TF-mediated effect; the association could reflect linkage or a mechanism not mediated by TF binding at this base.; Relevant-cell assays will not show a reproducible allele-dependent TF effect at this variant.

Falsified if: A reproducible allele-dependent TF effect at this base is demonstrated in a relevant cell type and linked to altered regulatory output.

### 2. H2: Candidate JUN-dependent regulation of FTO (p = 0.09)

TF JUN (QBiC-SELEX coverage own_model), alt allele binds more; element The variant overlaps a distal enhancer-like cCRE; whether it is active in the proposed cell type is unknown.; gene FTO; cell type Adipose-derived preadipocytes (proposed context).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | JUN is a testable candidate because it has a peak over the variant in HepG2 and is the most highly expressed of the listed peak-overlapping TFs in the adipose proxy; neither establishes occupancy in preadipocytes. No QBiC-SELEX result or allele-specific binding direction is provided. Alt C is a provisional hypothesis, not an evidence-supported direction. | weak | [E04](#e04), [E05](#e05), [E19](#e19) |
| element | The variant lies in a distal enhancer-like cCRE, but activity in preadipocytes and an allele-dependent effect are not established. | supported | [E03](#e03) |
| gene | FTO is the leading candidate target by credible-set L2G, but regulation of FTO by this cCRE is not demonstrated; the reported FTO eQTL is in skeletal muscle and no adipose-subcutaneous eQTL is reported. | weak | [E16](#e16), [E17](#e17), [E20](#e20) |
| cell_type | Adipose-derived preadipocytes are a proposed context based on the expression proxy, not a demonstrated site of JUN occupancy at this variant. | weak | [E04](#e04), [E05](#e05), [E19](#e19) |
| phenotype | The variant is strongly associated with obesity-related traits, but the association does not establish a JUN–cCRE–FTO mechanism or its regulatory direction. | supported | [E15](#e15), [E16](#e16) |

Predictions: In relevant preadipocytes, this provisional model predicts greater JUN binding to alt C than ref T and a JUN-dependent allele-specific regulatory effect; the direction of the downstream effect is unknown.; Unlike H4, this model predicts that disrupting JUN, rather than USF2, removes the allele-dependent effect.

Falsified if: JUN does not occupy the site in relevant cells, or a well-powered assay finds no JUN-dependent allele effect on regulatory output.

### 3. H4: Candidate USF2-dependent regulation of FTO (p = 0.05)

TF USF2 (QBiC-SELEX coverage own_model), alt allele binds more; element The variant overlaps a distal enhancer-like cCRE; whether it is active in the proposed cell type is unknown.; gene FTO; cell type Adipose-derived preadipocytes (proposed context).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | USF2 is an alternative testable candidate because a HepG2 peak overlaps the variant and USF2 is expressed in the adipose proxy; occupancy in preadipocytes is not shown. No QBiC-SELEX result or allele-specific binding direction is provided. Alt C is a provisional hypothesis, not an evidence-supported direction. | weak | [E04](#e04), [E07](#e07) |
| element | The variant lies in a distal enhancer-like cCRE, but activity in preadipocytes and an allele-dependent effect are not established. | supported | [E03](#e03) |
| gene | FTO is the leading candidate target by credible-set L2G, but regulation of FTO by this cCRE is not demonstrated; the reported FTO eQTL is in skeletal muscle and no adipose-subcutaneous eQTL is reported. | weak | [E16](#e16), [E17](#e17), [E20](#e20) |
| cell_type | Adipose-derived preadipocytes are a proposed context based on the expression proxy, not a demonstrated site of USF2 occupancy at this variant. | weak | [E04](#e04), [E07](#e07) |
| phenotype | The variant is strongly associated with obesity-related traits, but the association does not establish a USF2–cCRE–FTO mechanism or its regulatory direction. | supported | [E15](#e15), [E16](#e16) |

Predictions: In relevant preadipocytes, this provisional model predicts greater USF2 binding to alt C than ref T and a USF2-dependent allele-specific regulatory effect; the direction of the downstream effect is unknown.; Unlike H2, this model predicts that disrupting USF2, rather than JUN, removes the allele-dependent effect.

Falsified if: USF2 does not occupy the site in relevant cells, or a well-powered assay finds no USF2-dependent allele effect on regulatory output.

## Prediction matrix

| Test | Cost | Separates top two | H1 | H2 | H4 |
| --- | --- | --- | --- | --- | --- |
| Dual-allele enhancer reporter in adipose precursor cells, with control versus JUN or USF2 depletion; test for an allele-by-TF interaction. | low | yes | No reproducible allele-dependent reporter effect, or no effect specifically dependent on JUN or USF2. | An allele-dependent reporter effect that is reduced by JUN depletion; this model provisionally predicts greater binding for alt C, but the downstream direction is unknown. | An allele-dependent reporter effect that is reduced by USF2 depletion; this model provisionally predicts greater binding for alt C, but the downstream direction is unknown. |
| Check ENCODE or other available ChIP-seq data for a JUN peak in the closest available adipose-subcutaneous biosample. | existing data | no | No matching peak is compatible with the null; a peak alone would not establish an allelic effect. | A matching peak would support occupancy in that biosample, but would not establish allele-specific binding. | A JUN peak is not required by this USF2 model and would not establish USF2-mediated allelic regulation. |
| Look up variant-associated expression of FTO and other candidate genes in GTEx Adipose - Subcutaneous. | existing data | no | No adipose eQTL is compatible with the null; a detected eQTL alone would not prove TF mediation. | An FTO eQTL would be compatible with the proposed target, though not specific to JUN; absence would not by itself exclude a context-specific effect. | An FTO eQTL would be compatible with the proposed target, though not specific to USF2; absence would not by itself exclude a context-specific effect. |
| Check independent gene-disease evidence for RPGRIP1L and obesity. | existing data | no | Any RPGRIP1L-disease association would not establish a TF-mediated effect of this variant. | RPGRIP1L evidence would not test the proposed JUN–FTO chain. | RPGRIP1L evidence would not test the proposed USF2–FTO chain. |

## Next experiment

The cheapest direct discriminator for the top two hypotheses (H1 and H2) is a dual-allele enhancer reporter in an adipose precursor cell model with control versus JUN depletion. H2 predicts a JUN-dependent allelic difference; H1 predicts no reproducible JUN-dependent allelic difference. The result would test the proposed mechanism, not prove endogenous regulation at the native locus.

## Investigate calls

- chip_peaks({"tf": "JUN", "biosample": "Adipose - Subcutaneous"})
- eqtl_lookup({"tissue": "Adipose - Subcutaneous"})
- gene_disease({"gene": "RPGRIP1L"})

## Flags

- none

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

<a id="e18a"></a>**E18a** literature_search, Europe PMC abstract, PMID 42861203 (https://europepmc.org/article/MED/42861203; retrieved 2026-10-26T20:20:08+00:00)

> Fat mass and obesity-associated (FTO) protein, an m6A demethylase involved in metabolic regulation, has been linked to obesity.

<a id="e18b"></a>**E18b** literature_search, Europe PMC abstract, PMID 42866557 (https://europepmc.org/article/MED/42866557; retrieved 2026-10-26T20:20:08+00:00)

> This narrative review aims to clarify the tissue-specific effects of the fat mass and obesity-associated (FTO) gene, which encodes a demethylase enzyme, on lipid and glucose metabolism and appetite regulation.

<a id="e18c"></a>**E18c** literature_search, Europe PMC abstract, PMID 42860309 (https://europepmc.org/article/MED/42860309; retrieved 2026-10-26T20:20:08+00:00)

> Mogroside V (MV) is a triterpene glycoside extracted from Siraitia grosvenorii and has shown beneficial effects in models of obesity.

<a id="e18d"></a>**E18d** literature_search, Europe PMC abstract, PMID 42860309 (https://europepmc.org/article/MED/42860309; retrieved 2026-10-26T20:20:08+00:00)

> MV promoted brown adipocyte thermogenesis through the FTO-m6A-LETMD1-UCP1 axis, suggesting a potential therapeutic strategy for obesity.

<a id="e18e"></a>**E18e** literature_search, Europe PMC abstract, PMID 42708306 (https://europepmc.org/article/MED/42708306; retrieved 2026-10-26T20:20:08+00:00)

> Single nucleotide polymorphisms (SNPs) in the FTO (rs[masked]) and melanocortin-4-receptor (MC4R) (rs[masked]) genes have been strongly linked to an increased risk of obesity.

<a id="e18f"></a>**E18f** literature_search, Europe PMC abstract, PMID 42708306 (https://europepmc.org/article/MED/42708306; retrieved 2026-10-26T20:20:08+00:00)

> This study shows a clear correlation between the higher incidence of obesity in Quetta, Pakistan, and the FTO rs[masked] and MC4R rs[masked] polymorphisms.

<a id="e18g"></a>**E18g** literature_search, Europe PMC abstract, PMID 42893248 (https://europepmc.org/article/MED/42893248; retrieved 2026-10-26T20:20:08+00:00)

> Variants in the FTO (fat mass and obesity-associated) gene are well established as genetic determinants of adiposity and metabolic dysfunction.

<a id="e18h"></a>**E18h** literature_search, Europe PMC abstract, PMID 42893248 (https://europepmc.org/article/MED/42893248; retrieved 2026-10-26T20:20:08+00:00)

> The BRI is a strong predictor of MASLD, with FTO risk allele further amplifying susceptibility to MASLD.

<a id="e18i"></a>**E18i** literature_search, Europe PMC abstract, PMID 42790767 (https://europepmc.org/article/MED/42790767; retrieved 2026-10-26T20:20:08+00:00)

> The fat mass and obesity-associated protein (FTO) is an obesity-related protein that is widely expressed in different tissues throughout the human body, with relatively high expression levels observed in the brain.

<a id="e18j"></a>**E18j** literature_search, Europe PMC abstract, PMID 42790767 (https://europepmc.org/article/MED/42790767; retrieved 2026-10-26T20:20:08+00:00)

> Initial investigations into FTO mainly concentrated on its involvement in the development of obesity and diabetes.

<a id="e19"></a>**E19** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-26T02:29:32+00:00)

> No ENCODE JUN ChIP-seq peak contains chr16:53767042:T>C in biosamples matching 'Adipose - Subcutaneous'. Absence can also mean no JUN experiment in that biosample. In other biosamples, 1 JUN peaks do contain the variant: HepG2 (experiments ENCSR747VUU).

<a id="e20"></a>**E20** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr16_53767042_T_C_b38&datasetId=gtex_v8; retrieved 2026-10-25T17:30:38+00:00)

> 0 significant GTEx v8 single-tissue eQTLs for chr16_53767042_T_C_b38 in tissues matching 'Adipose - Subcutaneous'. NES is the effect of the alt allele (C) relative to ref (T).

<a id="e21"></a>**E21** gene_disease, Open Targets Platform (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-26T20:21:21+00:00)

> Open Targets: RPGRIP1L and obesity disorder (MONDO_0011122), overall score 0.15; by evidence type: genetic_association 0.24, literature 0.19
