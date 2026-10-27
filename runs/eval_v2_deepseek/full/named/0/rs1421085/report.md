# rs1421085 and Obesity (FTO)

Configuration `full`, named mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.05 over 8 model calls; 414 s.

Variant `chr16:53767042:T>C` (germline); expression context: GTEx:Adipose - Subcutaneous (proxy for preadipocytes).

## QBiC-SELEX screen (occupancy first)

Occupied candidates: ATF3 (bound elsewhere, z 21.73); TEAD1 (bound elsewhere, z 21.23); JUN (bound elsewhere, z 17.91); FOXP1 (bound elsewhere, z -16.49); USF2 (bound elsewhere, z 9.15); MAX (bound elsewhere, z 9.06); KLF6 (bound elsewhere, z 8.69); ZNF449 (bound elsewhere, z 6.4); SP1 (bound elsewhere, z -5.84); GATAD2A (bound elsewhere, z 5.71). Occupancy unknown: MEIS3 (z 54.71); PKNOX2 (z 54.71); TGIF1 (z 54.71); NR4A2 (z 32.74); NR4A3 (z 32.74). Diagnostic, not shown to the model: 425 of 997 models pass Bonferroni.

## Ranked chains

### 1. C5_ARID5B: ARID5B: ref T preserves a repressor site; alt C loses ARID5B and de-represses IRX3/IRX5 (p = 0.42)

TF ARID5B (QBiC-SELEX coverage not_in_coverage), ref allele binds more; element dELS active distal enhancer-like cCRE EH38E3181208; gene IRX3; cell type Adipose - Subcutaneous / preadipocyte proxy.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | ARID5B binds the ref T allele more strongly than the alt C allele. ARID5B is not in QBiC-SELEX coverage (E37), so no QBiC-SELEX allelic effect is available for ARID5B; the literature search E35 specifically points to ARID5B/IRX3 enhancer allele-specific reporter work, but the supplied excerpts do not give the reporter result. The direction is therefore literature/motif-motivated, not proven by an assay in this evidence set. | missing | [E35](#e35), [E37](#e37) |
| element | The variant lies in an active distal enhancer-like cCRE (dELS), with DNase and H3K27ac signal consistent with a regulatory element. | supported | [E03](#e03), [E04](#e04) |
| gene | IRX3 is a distal candidate target about 520 kb away; E17 reports alt C increasing IRX3 in pancreas (NES +0.37), and E35 points to an IRX3 enhancer model. This gene link is not adipose-specific and L2G favors FTO (E16), so it is indirect. | weak | [E02](#e02), [E16](#e16), [E17](#e17), [E35](#e35) |
| cell_type | The disease-relevant context is subcutaneous adipose/preadipocytes; the element is active in the adipose context (E03) and the literature model is in preadipocytes (E35), but this evidence set does not provide ARID5B expression or ChIP occupancy in preadipocytes. | weak | [E03](#e03), [E35](#e35) |
| phenotype | Loss of ARID5B binding on alt C is proposed to de-repress IRX3/IRX5, reduce thermogenic browning, and increase obesity risk. This predicts alt C as the risk allele; however, E15 labels T as the effect/risk allele, so the direction is discordant with the supplied GWAS label and must be resolved. | missing | [E15](#e15), [E17](#e17), [E35](#e35) |

Predictions: ARID5B ChIP-qPCR in preadipocytes will show higher ARID5B occupancy on ref T than alt C.; ARID5B knockdown in preadipocytes will increase IRX3/IRX5 expression.; An allele-specific reporter will show higher IRX3/IRX5 enhancer activity for alt C, abolished by ARID5B knockdown.

Falsified if: Allele-specific ARID5B ChIP in preadipocytes shows no ref-T preference at this base.; ARID5B knockdown or loss does not change IRX3/IRX5 in preadipocytes.; An allele-specific reporter in preadipocytes shows no C-allele effect on IRX3/IRX5 enhancer activity.

### 2. null: Null: no TF-mediated effect of rs1421085 at this base (p = 0.30)

Null chain: no TF-mediated effect of this variant.

Predictions: No allele-specific TF occupancy at this base in preadipocytes/subcutaneous adipose.; The obesity association is driven by a linked variant or a non-TF mechanism at this base.; ARID5B ChIP-qPCR in preadipocytes will not show a reproducible T-versus-C difference.

Falsified if: Allele-specific ARID5B ChIP in preadipocytes shows reproducible ref-T over alt-C occupancy at chr16:53767042.; An allele-specific reporter or CRISPR allele swap in preadipocytes shows the C allele changes IRX3/IRX5 enhancer activity in an ARID5B-dependent manner.; Adipose/preadipocyte molecular QTL or ASE data map to this exact base and track with obesity.

### 3. C1_ATF3: ATF3: alt C increases binding at the FTO enhancer (p = 0.16)

TF ATF3 (QBiC-SELEX coverage own_model), alt allele binds more; element dELS active distal enhancer-like cCRE EH38E3181208; gene FTO; cell type Adipose - Subcutaneous / preadipocyte proxy.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | ATF3 binds the alt C allele more strongly than ref T: QBiC-SELEX ATF3 own model gives z 21.73 and effect 1.403 (alt > ref). ATF3 is expressed in subcutaneous adipose (57.63 TPM, rank 88/1631), but its only ENCODE peak over this variant is in HCT116, not adipose, so adipose occupancy is not demonstrated. | weak | [E09](#e09), [E20](#e20) |
| element | The variant lies in an active distal enhancer-like cCRE (dELS) with DNase and H3K27ac signal, consistent with a regulatory element. | supported | [E03](#e03), [E04](#e04) |
| gene | FTO is the best L2G gene at this locus (E16), but E36 reports no significant adipose eQTL for this variant, and the only FTO eQTL is in skeletal muscle with alt C giving NES +0.14 (E17). The gene link in the disease context is therefore weak. | weak | [E02](#e02), [E16](#e16), [E17](#e17), [E36](#e36) |
| cell_type | ATF3 is expressed in subcutaneous adipose and the element is active there, but no adipose ATF3 ChIP is available; expression plus an active element does not demonstrate occupancy. | weak | [E03](#e03), [E20](#e20) |
| phenotype | The locus is strongly associated with obesity/BMI (E15/E16). If ATF3 represses FTO in preadipocytes, stronger alt-C ATF3 binding would lower FTO and be protective relative to T; this is compatible with T being the E15 effect allele but is a specific prediction, not established by the data. | weak | [E15](#e15), [E16](#e16) |

Predictions: ATF3 ChIP-qPCR in preadipocytes will show higher occupancy on alt C than ref T.; ATF3 knockdown will change FTO expression in preadipocytes.; If ATF3 represses FTO, the alt C allele will lower FTO in adipose/preadipocytes.

Falsified if: Allele-specific ATF3 ChIP in preadipocytes shows no alt-C preference.; ATF3 perturbation does not change FTO in preadipocytes.; The alt-C allele does not alter FTO in adipose when ATF3 is manipulated.

### 4. C3_JUN: JUN: alt C increases AP-1 factor binding at the FTO enhancer (p = 0.12)

TF JUN (QBiC-SELEX coverage own_model), alt allele binds more; element dELS active distal enhancer-like cCRE EH38E3181208; gene FTO; cell type Adipose - Subcutaneous / preadipocyte proxy.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | JUN binds the alt C allele more strongly than ref T: QBiC-SELEX JUN own model gives z 17.91 and effect 0.317 (alt > ref), with alt at the 99.8th percentile versus 82.8th for ref. JUN is very highly expressed in subcutaneous adipose (442.88 TPM, rank 3/1631), but its only ENCODE peak over this variant is in HepG2, not adipose. | weak | [E05](#e05), [E22](#e22) |
| element | The variant lies in an active distal enhancer-like cCRE (dELS); ENCODE ChIP-seq in other biosamples includes active-element factors such as EP300 and Pol II, consistent with an enhancer. | supported | [E03](#e03), [E04](#e04) |
| gene | FTO is the best L2G gene at this locus, but E36 reports no significant adipose eQTL for this variant and the FTO eQTL is only in skeletal muscle (alt C NES +0.14, E17). The FTO gene link is plausible but not proven in adipose. | weak | [E02](#e02), [E16](#e16), [E17](#e17), [E36](#e36) |
| cell_type | JUN is abundantly expressed in subcutaneous adipose and the element is active there, but no adipose JUN ChIP is available; expression does not demonstrate occupancy. | weak | [E03](#e03), [E05](#e05) |
| phenotype | The locus is associated with obesity/BMI. JUN can activate or repress depending on context: if JUN activates FTO, alt C would increase FTO and make C risk, conflicting with E15's T effect allele; if JUN represses FTO, alt C would lower FTO and be protective, consistent with T as effect allele. The direction is unresolved. | weak | [E15](#e15), [E16](#e16) |

Predictions: JUN ChIP-qPCR in preadipocytes will show higher occupancy on alt C than ref T.; JUN perturbation will change FTO expression in preadipocytes.; The FTO direction will depend on whether JUN activates or represses FTO in adipocytes.

Falsified if: Allele-specific JUN ChIP in preadipocytes shows no alt-C preference.; JUN perturbation does not change FTO in preadipocytes.; The alt-C allele does not alter FTO in adipose when JUN is manipulated.

## Prediction matrix

| Test | Cost | Separates top two | C5_ARID5B | null | C1_ATF3 | C3_JUN |
| --- | --- | --- | --- | --- | --- | --- |
| Allele-specific ARID5B ChIP-qPCR at rs1421085 in subcutaneous preadipocytes | medium | yes | ARID5B ChIP-qPCR shows higher occupancy on ref T than alt C. | No reproducible allele-specific ARID5B occupancy at rs1421085 (T approximately C). | No ARID5B allelic difference; this assay does not test ATF3 binding. | No ARID5B allelic difference; this assay does not test JUN binding. |
| Allele-specific ATF3 ChIP-qPCR at rs1421085 in preadipocytes | medium | no | No ATF3 allelic difference. | No reproducible allele-specific ATF3 occupancy. | Higher ATF3 occupancy on alt C than ref T. | No ATF3 allelic difference. |
| Allele-specific JUN ChIP-qPCR at rs1421085 in preadipocytes | medium | no | No JUN allelic difference. | No reproducible allele-specific JUN occupancy. | No JUN allelic difference. | Higher JUN occupancy on alt C than ref T. |
| Allele-specific IRX3/IRX5 enhancer reporter in preadipocytes with and without ARID5B knockdown | high | yes | Alt C increases IRX3/IRX5 reporter activity, and ARID5B knockdown abolishes the T-versus-C difference. | No allele-specific enhancer activity for T versus C. | No IRX3/IRX5 allele effect; an FTO reporter may change if ATF3 regulates FTO. | No IRX3/IRX5 allele effect; an FTO reporter may change if JUN regulates FTO. |
| Preadipocyte allele-specific expression of FTO and IRX3/IRX5 | medium | yes | IRX3/IRX5 allele-specific expression with alt C higher; FTO not necessarily affected. | No allele-specific expression of FTO or IRX3/IRX5. | FTO allele-specific expression, with alt C lower if ATF3 represses FTO. | FTO allele-specific expression, direction depending on JUN activation versus repression. |

## Next experiment

Allele-specific ARID5B ChIP-qPCR at rs1421085 in subcutaneous preadipocytes is the cheapest experiment that separates the top two chains: C5_ARID5B predicts ref T > alt C ARID5B occupancy, whereas the null predicts no reproducible allele-specific occupancy.

## Investigate calls

- literature_search({"query": "rs1421085 allele-specific reporter adipocyte ARID5B IRX3 enhancer"})
- eqtl_lookup({"tissue": "Adipose - Subcutaneous"})
- qbic_tf_detail({"tf": "ARID5B"})

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

<a id="e19"></a>**E19** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> QBiC-SELEX screen of chr16:53767042:T>C, one line per TF, each with the TF's own or CIS-BP-mapped model of largest |z|. Candidates are TFs whose ENCODE ChIP-seq peaks contain the variant and that are expressed (GTEx tissue median Adipose - Subcutaneous), bound here before bound elsewhere, then by |z|; then expressed TFs ENCODE never assayed whose best model passes the gate (occupancy unknown). Shown: 10 of 16 occupied, 5 of 157 with unknown occupancy. Left out: 0 TFs assayed in the matching biosample and 554 assayed only elsewhere, none with a peak here; 3 bound but below 1 TPM. The gate (|z| > 4.05, Bonferroni over 997 models) marks a change QBiC-SELEX detects; it says nothing about occupancy. Effect > 0 means the alternate allele binds more strongly. In vitro binding only.

<a id="e20"></a>**E20** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> ATF3 (bZIP, 2 models; QBiC-SELEX coverage: own model): best model ATF3_eDBD_TTGGAC40NGTG_KS_yin2017_0_3_7mer (its own model), z 21.73, effect 1.403: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 57.63 TPM, rank 88 of 1631 TFs in GTEx:Adipose - Subcutaneous (proxy for preadipocytes). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in HCT116, e.g. ENCSR000BUG. Best model's site strength: ref 98.9th, alt 99.7th percentile of its k-mer coefficients.

<a id="e21"></a>**E21** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> TEAD1 (TEA, 4 models; QBiC-SELEX coverage: own model): best model TEAD1_FL_TCACGC40NACT_KW_yin2017_0_4_7mer (its own model), z 21.23, effect 1.544: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 40.88 TPM, rank 148 of 1631 TFs in GTEx:Adipose - Subcutaneous (proxy for preadipocytes). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in HepG2, e.g. ENCSR497JLX. Best model's site strength: ref 98.8th, alt 98.8th percentile of its k-mer coefficients.

<a id="e22"></a>**E22** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> JUN (bZIP, 3 models; QBiC-SELEX coverage: own model): best model JUN_FL_TCAGTG40NGAT_KAE_yin2017_0_3_7mer (its own model), z 17.91, effect 0.317: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 442.88 TPM, rank 3 of 1631 TFs in GTEx:Adipose - Subcutaneous (proxy for preadipocytes). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in HepG2, e.g. ENCSR747VUU. Best model's site strength: ref 82.8th, alt 99.8th percentile of its k-mer coefficients.

<a id="e23"></a>**E23** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> FOXP1 (Forkhead, 10 models; QBiC-SELEX coverage: own model): best model FOXC2_eDBD_TCAGAA40NAGG_KO_yin2017_0_4_7mer (a CIS-BP-mapped model of FOXC2), z -16.49, effect -1.476: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 14.95 TPM, rank 419 of 1631 TFs in GTEx:Adipose - Subcutaneous (proxy for preadipocytes). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in HepG2, e.g. ENCSR369YUK. Best model's site strength: ref 99.4th, alt 92.1th percentile of its k-mer coefficients.

<a id="e24"></a>**E24** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> USF2 (bHLH, 2 models; QBiC-SELEX coverage: own model): best model USF2_eDBD_TTGAAG40NCTC_KS_yin2017_1_2_7mer (its own model), z 9.15, effect 0.124: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 114.23 TPM, rank 31 of 1631 TFs in GTEx:Adipose - Subcutaneous (proxy for preadipocytes). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in HepG2, e.g. ENCSR145QNL. Best model's site strength: ref 99.7th, alt 99.8th percentile of its k-mer coefficients.

<a id="e25"></a>**E25** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> MAX (bHLH, 1 model; QBiC-SELEX coverage: own model): best model MAX_FL_TG40NGACCTT_YWN_jolma2025_0_3_7mer (its own model), z 9.06, effect 0.497: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 41.99 TPM, rank 141 of 1631 TFs in GTEx:Adipose - Subcutaneous (proxy for preadipocytes). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in HepG2, e.g. ENCSR168DYA. Best model's site strength: ref 97.5th, alt 97.8th percentile of its k-mer coefficients.

<a id="e26"></a>**E26** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> KLF6 (C2H2 ZF, 6 models; QBiC-SELEX coverage: own model): best model KLF4_eDBD_TAGAGA40NCGC_KT_yin2017_0_4_7mer (a CIS-BP-mapped model of KLF4), z 8.69, effect 0.507: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 247.5 TPM, rank 11 of 1631 TFs in GTEx:Adipose - Subcutaneous (proxy for preadipocytes). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in HepG2, e.g. ENCSR757EKM. Best model's site strength: ref 92.9th, alt 95.6th percentile of its k-mer coefficients.

<a id="e27"></a>**E27** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> ZNF449 (C2H2 ZF, 1 model; QBiC-SELEX coverage: own model): best model ZNF449_eDBD_TGCGAG40NTTC_KT_yin2017_0_3_7mer (its own model), z 6.4, effect 0.296: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 9.4 TPM, rank 577 of 1631 TFs in GTEx:Adipose - Subcutaneous (proxy for preadipocytes). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in HEK293, e.g. ENCSR738SLS. Best model's site strength: ref 84.0th, alt 95.4th percentile of its k-mer coefficients.

<a id="e28"></a>**E28** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> SP1 (C2H2 ZF, 5 models; QBiC-SELEX coverage: own model): best model SP8_NA_TGCTCG20NCTC_ESY_yang2017_0_4_7mer (a CIS-BP-mapped model of SP8), z -5.84, effect -0.335: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 41.01 TPM, rank 145 of 1631 TFs in GTEx:Adipose - Subcutaneous (proxy for preadipocytes). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in HCT116, e.g. ENCSR000BSF. Best model's site strength: ref 82.4th, alt 70.6th percentile of its k-mer coefficients.

<a id="e29"></a>**E29** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> GATAD2A (GATA, 1 model; QBiC-SELEX coverage: own model): best model GATAD2A_FL_AA40NGTGGTG_YWN_jolma2025_0_4_7mer (its own model), z 5.71, effect 0.358: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 25.37 TPM, rank 260 of 1631 TFs in GTEx:Adipose - Subcutaneous (proxy for preadipocytes). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in HepG2, e.g. ENCSR925BFV. Best model's site strength: ref 95.4th, alt 99.2th percentile of its k-mer coefficients.

<a id="e30"></a>**E30** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> MEIS3 (Homeodomain, 9 models; QBiC-SELEX coverage: own model): best model PKNOX2_eDBD_TAACGT40NGAT_KAN_yin2017_0_4_7mer (a CIS-BP-mapped model of PKNOX2), z 54.71, effect 3.047: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 9.23 TPM, rank 583 of 1631 TFs in GTEx:Adipose - Subcutaneous (proxy for preadipocytes). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 95.5th, alt 99.7th percentile of its k-mer coefficients.

<a id="e31"></a>**E31** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> PKNOX2 (Homeodomain, 9 models; QBiC-SELEX coverage: own model): best model PKNOX2_eDBD_TAACGT40NGAT_KAN_yin2017_0_4_7mer (its own model), z 54.71, effect 3.047: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 2.8 TPM, rank 994 of 1631 TFs in GTEx:Adipose - Subcutaneous (proxy for preadipocytes). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 95.5th, alt 99.7th percentile of its k-mer coefficients.

<a id="e32"></a>**E32** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> TGIF1 (Homeodomain, 9 models; QBiC-SELEX coverage: own model): best model PKNOX2_eDBD_TAACGT40NGAT_KAN_yin2017_0_4_7mer (a CIS-BP-mapped model of PKNOX2), z 54.71, effect 3.047: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 13.07 TPM, rank 461 of 1631 TFs in GTEx:Adipose - Subcutaneous (proxy for preadipocytes). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 95.5th, alt 99.7th percentile of its k-mer coefficients.

<a id="e33"></a>**E33** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> NR4A2 (Nuclear receptor, 29 models; QBiC-SELEX coverage: own model): best model NR4A3_DBD_TTCGTA20NTA_KH_nitta2015_1_3_7mer (a CIS-BP-mapped model of NR4A3), z 32.74, effect 2.426: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 17.54 TPM, rank 373 of 1631 TFs in GTEx:Adipose - Subcutaneous (proxy for preadipocytes). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 99.6th, alt 100.0th percentile of its k-mer coefficients.

<a id="e34"></a>**E34** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> NR4A3 (Nuclear receptor, 29 models; QBiC-SELEX coverage: own model): best model NR4A3_DBD_TTCGTA20NTA_KH_nitta2015_1_3_7mer (its own model), z 32.74, effect 2.426: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 6.38 TPM, rank 708 of 1631 TFs in GTEx:Adipose - Subcutaneous (proxy for preadipocytes). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 99.6th, alt 100.0th percentile of its k-mer coefficients.

<a id="e35"></a>**E35** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=rs1421085%20allele-specific%20reporter%20adipocyte%20ARID5B%20IRX3%20enhancer&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T02:42:20+00:00)

> Europe PMC: 12 hits for 'rs1421085 allele-specific reporter adipocyte ARID5B IRX3 enhancer'; top 8 with PMIDs:
> PMID 42589667 (2026): Functional Annotation of GWAS Loci Using Public Transcriptome and Epigenome Datasets Reveals Non-Coding Genes and Regulatory Elements Which May Contribute to BMI.
> PMID 41273414 (2026): Bridging the variant-to-function gap in type 2 diabetes: advances and challenges.
> PMID 39965570 (2025): An evolving understanding of multiple causal variants underlying genetic association signals.
> PMID 36882962 (2023): Technologies, strategies, and cautions when deconvoluting genome-wide association signals: FTO in focus.
> PMID 37034418 (2022): Systematic assays and resources for the functional annotation of non-coding variants.
> PMID 37554175 (2023): Studies on the fat mass and obesity-associated (FTO) gene and its impact on obesity-associated diseases.
> PMID 27436305 (2016): Noncoding Genome-Wide Association Studies Variant for Obesity: Inroads Into Mechanism: An Overview From the AHA's Council on Functional Genomics and Translational Biology. [no abstract]
> PMID 31317254 (2020): Identifying causal variants and genes using functional genomics in specialized cell types and contexts.

<a id="e35a"></a>**E35a** literature_search, Europe PMC abstract, PMID 36882962 (https://europepmc.org/article/MED/36882962; retrieved 2026-10-26T02:42:20+00:00)

> By reviewing studies of the FTO locus in the genetic etiology of obesity, we wish to highlight advances in the field fueled by the evolution of technical and analytic strategies in assessing the molecular bases for genetic associations.

<a id="e35b"></a>**E35b** literature_search, Europe PMC abstract, PMID 36882962 (https://europepmc.org/article/MED/36882962; retrieved 2026-10-26T02:42:20+00:00)

> A unifying model is proposed by which independent obesogenic pathways regulated by multiple FTO variants and genes are integrated at the primary cilium, a cellular antenna where signaling molecules that control energy balance convene.

<a id="e35c"></a>**E35c** literature_search, Europe PMC abstract, PMID 37554175 (https://europepmc.org/article/MED/37554175; retrieved 2026-10-26T02:42:20+00:00)

> The fat mass and obesity-associated (FTO) gene, identified by genome-wide association studies (GWAS), was first reported to be positively associated with obesity in humans.

<a id="e35d"></a>**E35d** literature_search, Europe PMC abstract, PMID 37554175 (https://europepmc.org/article/MED/37554175; retrieved 2026-10-26T02:42:20+00:00)

> Second, we discuss the ongoing debates concerning the association between FTO polymorphisms and obesity.

<a id="e36"></a>**E36** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr16_53767042_T_C_b38&datasetId=gtex_v8; retrieved 2026-10-25T17:30:38+00:00)

> 0 significant GTEx v8 single-tissue eQTLs for chr16_53767042_T_C_b38 in tissues matching 'Adipose - Subcutaneous'. NES is the effect of the alt allele (C) relative to ref (T).

<a id="e37"></a>**E37** qbic_tf_detail, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> {"tf":"ARID5B","symbol":"ARID5B","via":"hgnc_symbol","notes":[],"coverage":"not_in_coverage"}
