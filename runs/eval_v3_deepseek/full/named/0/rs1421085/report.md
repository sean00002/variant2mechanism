# rs1421085 and Obesity (FTO)

Configuration `full`, named mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.03 over 8 model calls; 172 s.

Variant `chr16:53767042:T>C` (germline); expression context: GTEx:Adipose - Subcutaneous (proxy for preadipocytes).

## QBiC-SELEX screen (occupancy first)

Occupied candidates: ATF3 (bound elsewhere, z 21.73); TEAD1 (bound elsewhere, z 21.23); JUN (bound elsewhere, z 17.91); FOXP1 (bound elsewhere, z -16.49); USF2 (bound elsewhere, z 9.15); MAX (bound elsewhere, z 9.06); GATAD2A (bound elsewhere, z 5.71); HMG20B (bound elsewhere, z 4.52); PHF21A (bound elsewhere, z -2.87, no clear allelic change); ZNF48 (bound elsewhere, z 2.69, no clear allelic change). Occupancy unknown: MEIS3 (z 54.71); PKNOX2 (z 54.71); TGIF1 (z 54.71); NR4A2 (z 32.74); NR4A3 (z 32.74). Diagnostic, not shown to the model: 425 of 997 models pass Bonferroni.

## Ranked chains

### 1. H5: ARID5B binds the ref T allele; alt C disrupts a repressor motif in the dELS (p = 0.40)

TF ARID5B (QBiC-SELEX coverage not_in_coverage), ref allele binds more; element EH38E3181208 dELS; gene FTO; cell type subcutaneous adipose/pre-adipocytes.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | ARID5B binds the ref T allele more strongly: the literature states that rs1421085 T-to-C interrupts a conserved ARID5B repressor motif, so the C allele loses ARID5B binding. ARID5B has no QBiC-SELEX model in the supplied rows, so I do not use another TF's SELEX change as its evidence; selection is by the quoted motif-disruption literature, with conservation at the site consistent with a functional motif. | weak | [E37a](#e37a), [E37b](#e37b), [E01](#e01) |
| element | The motif lies in dELS EH38E3181208, a distal enhancer-like element with active chromatin and cofactor occupancy over the variant, consistent with a regulatory element whose output could be altered by loss of ARID5B repression. | supported | [E03](#e03), [E04](#e04), [E37a](#e37a) |
| gene | FTO is the strongest locus-assigned gene (L2G 0.99) and contains the variant, but no adipose eQTL establishes FTO as the directly regulated gene; IRX3 is a plausible distal target but has only a pancreas eQTL in the supplied data. The target-gene direction in adipose remains unresolved. | weak | [E02](#e02), [E16](#e16), [E17](#e17), [E36](#e36) |
| cell_type | The quoted literature ties the allele effect to activated adipocytes and thermogenic/beige-to-white adipocyte state, making subcutaneous adipose/pre-adipocytes the relevant context, although direct pre-adipocyte ARID5B occupancy at this base is not supplied. | supported | [E37b](#e37b), [E03](#e03) |
| phenotype | Allele-specific loss of ARID5B repression on C can shift adipocyte thermogenesis and thereby influence obesity. The core claim is motif loss on C; however the GWAS evidence in E15 codes T as the effect/risk allele, while the quoted literature implies C disrupts ARID5B repression and may be the functional risk allele, so the disease-risk direction is not settled by the supplied evidence. | weak | [E15](#e15), [E37a](#e37a), [E37b](#e37b) |

Predictions: Allele-specific ARID5B binding or reporter assays in pre-adipocytes show stronger ref T binding and C-allele loss of repression.; ARID5B perturbation in pre-adipocytes changes thermogenic/beige-adipocyte programs and, if FTO/IRX3 is the relevant target, changes their expression.; The C allele alters enhancer activity in an ARID5B-motif-dependent manner.

Falsified if: ARID5B does not bind the ref T motif or shows no allele-specific binding in adipose/pre-adipocyte assays.; Disrupting the ARID5B motif has no effect on enhancer activity or adipocyte thermogenic programs.; The phenotype is fully explained by a linked variant rather than by ARID5B binding at this base.

### 2. H0: No TF-mediated allelic effect; linked or unproven causal variant (p = 0.35)

Null chain: no TF-mediated effect of this variant.

Predictions: No reproducible allele-specific TF occupancy or enhancer activity from this base in subcutaneous adipose/pre-adipocytes.; Any obesity association is attributable to a linked causal variant or to non-allelic regulatory effects at the FTO/IRX3 locus rather than to rs1421085 itself.; Allele-specific assays at this base show no difference after controlling for linked variants.

Falsified if: Adipose or pre-adipocyte assays show rs1421085 allele-specific TF binding and enhancer activity that tracks with the GWAS effect.; A molecular QTL in adipose maps the causal variant to this base and is disrupted by the allele.

### 3. H1: ATF3 binds the alt C allele more and represses FTO (p = 0.15)

TF ATF3 (QBiC-SELEX coverage own_model), alt allele binds more; element EH38E3181208 dELS; gene FTO; cell type subcutaneous adipose/pre-adipocytes.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | ATF3 has its own QBiC-SELEX model and the alt C allele binds more strongly (z 21.73, effect +1.403, strong site), and ATF3 is highly expressed in adipose. However, the only ENCODE ATF3 peak over the variant is in HCT116, not adipose; E35 explicitly reports no matching subcutaneous-adipose ATF3 ChIP peak, so adipose occupancy is unproven. | weak | [E20](#e20), [E09](#e09), [E35](#e35), [E19](#e19) |
| element | The variant lies in dELS EH38E3181208 with active-enhancer cofactor occupancy, so an allele-specific TF change could in principle alter enhancer output. | supported | [E03](#e03), [E04](#e04) |
| gene | FTO is the top locus-assigned gene (L2G 0.99), but the only FTO eQTL is in skeletal muscle (alt C NES +0.14), and there is no significant subcutaneous adipose eQTL for this variant; adipose target-gene direction is not established. | weak | [E16](#e16), [E17](#e17), [E36](#e36), [E02](#e02) |
| cell_type | Subcutaneous adipose/pre-adipocytes are the expression context and ATF3 is highly expressed there, but no adipose/pre-adipocyte ChIP-seq or functional assay over this variant is available. | weak | [E19](#e19), [E20](#e20), [E35](#e35) |
| phenotype | This chain requires ATF3 to repress FTO so that protective C binding more lowers FTO and reduces obesity. No supplied evidence shows ATF3 represses FTO, and the muscle FTO eQTL has alt C increasing FTO, creating a direction conflict. | missing | [E15](#e15), [E17](#e17), [E20](#e20) |

Predictions: Adipose/pre-adipocyte ChIP or reporter assays show C-allele-specific ATF3 occupancy at this element.; ATF3 knockdown or overexpression changes FTO expression in the repression direction.; The C allele lowers FTO in adipose if this chain is correct.

Falsified if: Adipose assays show no ATF3 binding or no allelic difference at rs1421085.; ATF3 activation increases FTO or IRX3 rather than repressing it.; Adipose eQTL or reporter data show the C allele increases FTO/IRX3 in a way incompatible with the GWAS risk direction.

### 4. H4: FOXP1 binds the ref T allele more and activates FTO (p = 0.10)

TF FOXP1 (QBiC-SELEX coverage own_model), ref allele binds more; element EH38E3181208 dELS; gene FTO; cell type subcutaneous adipose/pre-adipocytes.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | FOXP1 shows ref T binding more in QBiC-SELEX (z -16.49, effect -1.476, strong ref site), but the best model is a CIS-BP-mapped FOXC2 model rather than an own FOXP1 model, and the only cited occupancy is in HepG2, not adipose. The binding evidence is therefore indirect and not in the relevant cell type. | weak | [E23](#e23), [E19](#e19) |
| element | The variant lies in dELS EH38E3181208 with active-enhancer marks, supporting element context only. | supported | [E03](#e03), [E04](#e04) |
| gene | FTO is strongly locus-assigned (L2G 0.99), but the only FTO eQTL is skeletal muscle with alt C NES +0.14, and no adipose eQTL establishes FTO direction. | weak | [E16](#e16), [E17](#e17), [E36](#e36), [E02](#e02) |
| cell_type | FOXP1 is expressed in GTEx subcutaneous adipose, but no adipose/pre-adipocyte ChIP-seq or functional assay over the variant is supplied. | weak | [E19](#e19), [E23](#e23) |
| phenotype | This chain requires FOXP1 to activate FTO so that risk T with more FOXP1 raises FTO and obesity. No supplied evidence supports FOXP1 activation of FTO, and FOXP1 is often a repressor; the direction is conditional and atypical. | missing | [E15](#e15), [E23](#e23) |

Predictions: Adipose/pre-adipocyte assays show T-allele-specific FOXP1 occupancy at this element.; FOXP1 perturbation increases FTO expression if FOXP1 acts as an activator here.; The T allele is associated with higher FTO in adipose if this chain is correct.

Falsified if: FOXP1 does not occupy this element in adipose/pre-adipocytes.; FOXP1 represses FTO or IRX3 in this context, making the direction incompatible with T as the risk allele.; Functional assays show no T-allele-specific FOXP1 effect.

## Prediction matrix

| Test | Cost | Separates top two | H5 | H0 | H1 | H4 |
| --- | --- | --- | --- | --- | --- | --- |
| Allele-specific ARID5B binding assay (EMSA or ChIP) in subcutaneous pre-adipocytes comparing ref T and alt C oligonucleotides | low | yes | ARID5B binds the ref T oligonucleotide more strongly; alt C reduces ARID5B binding. | No reproducible allele-specific ARID5B binding at this base. | No allele-specific ARID5B binding; if any, ATF3 shows the alt C-specific effect instead. | No allele-specific ARID5B binding; if any, FOXP1 shows the ref T-specific effect instead. |
| Allele-specific enhancer reporter (MPRA) in pre-adipocytes, with wild-type versus ARID5B-motif-mutant constructs | medium | yes | C-allele reporter activity changes in an ARID5B-motif-dependent manner. | No allele-specific reporter activity from this base. | C-allele reporter activity changes and is ATF3-dependent rather than ARID5B-dependent. | T-allele reporter activity changes and is FOXP1-dependent. |
| ATF3 ChIP-seq or ATF3 knockdown in subcutaneous pre-adipocytes at rs1421085 | medium | no | No ATF3 allele-specific occupancy; ARID5B motif remains the primary explanation. | No allele-specific ATF3 occupancy. | C-allele-specific ATF3 occupancy and ATF3-dependent enhancer/FTO effect. | No ATF3 allele-specific effect; FOXP1 remains the alternative. |
| Adipose/pre-adipocyte eQTL or CRISPR perturbation of FTO and IRX3 at this enhancer | high | yes | ARID5B-motif-dependent change in thermogenic genes and/or FTO/IRX3 expression. | No allele-specific effect on FTO or IRX3 after controlling for linked variants. | ATF3-dependent repression of FTO in adipose. | FOXP1-dependent activation of FTO in adipose. |

## Next experiment

Cheapest discriminating test: allele-specific ARID5B EMSA/ChIP in subcutaneous pre-adipocytes using ref T versus alt C oligonucleotides or nuclear extract; if ARID5B reagents are unavailable, use a minimal ARID5B-motif-mutant reporter to test whether the C allele loses ARID5B-dependent repression.

## Investigate calls

- chip_peaks({"tf": "ATF3", "biosample": "subcutaneous adipose"})
- eqtl_lookup({"tissue": "Adipose - Subcutaneous"})
- literature_search({"query": "rs1421085 FTO adipose enhancer ARID5B allele-specific"})

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

> QBiC-SELEX screen of chr16:53767042:T>C, one line per TF, each with the TF's own or CIS-BP-mapped model of largest |z|. Candidates are TFs whose ENCODE ChIP-seq peaks contain the variant and that are expressed (GTEx tissue median Adipose - Subcutaneous), bound here before bound elsewhere, then a strong site before a weak one, then by |z|; then expressed TFs ENCODE never assayed whose best model passes the gate (occupancy unknown). Shown: 10 of 16 occupied (10 with a strong site), 5 of 157 with unknown occupancy. Left out: 0 TFs assayed in the matching biosample and 554 assayed only elsewhere, none with a peak here; 3 bound but below 1 TPM. The gate (|z| > 4.05, Bonferroni over 997 models) marks a change QBiC-SELEX detects; it says nothing about occupancy. Effect > 0 means the alternate allele binds more strongly. In vitro binding only. Site strength is the better allele's best k-mer over the variant, as a percentile of the best model's k-mers; a strong site reaches the 97.5th. At a weak site the ChIP peak more likely reflects another site in the element.

<a id="e20"></a>**E20** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> ATF3 (bZIP, 2 models; QBiC-SELEX coverage: own model): best model ATF3_eDBD_TTGGAC40NGTG_KS_yin2017_0_3_7mer (its own model), z 21.73, effect 1.403: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 57.63 TPM, rank 88 of 1631 TFs in GTEx:Adipose - Subcutaneous (proxy for preadipocytes). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in HCT116, e.g. ENCSR000BUG. Best model's site strength: ref 98.9th, alt 99.7th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e21"></a>**E21** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> TEAD1 (TEA, 4 models; QBiC-SELEX coverage: own model): best model TEAD1_FL_TCACGC40NACT_KW_yin2017_0_4_7mer (its own model), z 21.23, effect 1.544: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 40.88 TPM, rank 148 of 1631 TFs in GTEx:Adipose - Subcutaneous (proxy for preadipocytes). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in HepG2, e.g. ENCSR497JLX. Best model's site strength: ref 98.8th, alt 98.8th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e22"></a>**E22** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> JUN (bZIP, 3 models; QBiC-SELEX coverage: own model): best model JUN_FL_TCAGTG40NGAT_KAE_yin2017_0_3_7mer (its own model), z 17.91, effect 0.317: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 442.88 TPM, rank 3 of 1631 TFs in GTEx:Adipose - Subcutaneous (proxy for preadipocytes). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in HepG2, e.g. ENCSR747VUU. Best model's site strength: ref 82.8th, alt 99.8th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e23"></a>**E23** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> FOXP1 (Forkhead, 10 models; QBiC-SELEX coverage: own model): best model FOXC2_eDBD_TCAGAA40NAGG_KO_yin2017_0_4_7mer (a CIS-BP-mapped model of FOXC2), z -16.49, effect -1.476: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 14.95 TPM, rank 419 of 1631 TFs in GTEx:Adipose - Subcutaneous (proxy for preadipocytes). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in HepG2, e.g. ENCSR369YUK. Best model's site strength: ref 99.4th, alt 92.1th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e24"></a>**E24** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> USF2 (bHLH, 2 models; QBiC-SELEX coverage: own model): best model USF2_eDBD_TTGAAG40NCTC_KS_yin2017_1_2_7mer (its own model), z 9.15, effect 0.124: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 114.23 TPM, rank 31 of 1631 TFs in GTEx:Adipose - Subcutaneous (proxy for preadipocytes). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in HepG2, e.g. ENCSR145QNL. Best model's site strength: ref 99.7th, alt 99.8th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e25"></a>**E25** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> MAX (bHLH, 1 model; QBiC-SELEX coverage: own model): best model MAX_FL_TG40NGACCTT_YWN_jolma2025_0_3_7mer (its own model), z 9.06, effect 0.497: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 41.99 TPM, rank 141 of 1631 TFs in GTEx:Adipose - Subcutaneous (proxy for preadipocytes). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in HepG2, e.g. ENCSR168DYA. Best model's site strength: ref 97.5th, alt 97.8th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e26"></a>**E26** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> GATAD2A (GATA, 1 model; QBiC-SELEX coverage: own model): best model GATAD2A_FL_AA40NGTGGTG_YWN_jolma2025_0_4_7mer (its own model), z 5.71, effect 0.358: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 25.37 TPM, rank 260 of 1631 TFs in GTEx:Adipose - Subcutaneous (proxy for preadipocytes). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in HepG2, e.g. ENCSR925BFV. Best model's site strength: ref 95.4th, alt 99.2th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e27"></a>**E27** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> HMG20B (HMG/Sox, 1 model; QBiC-SELEX coverage: mapped models only): best model HMG20A_FL_TG40NTGATCT_YWL_jolma2025_0_4_7mer (a CIS-BP-mapped model of HMG20A), z 4.52, effect 0.125: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 84.43 TPM, rank 51 of 1631 TFs in GTEx:Adipose - Subcutaneous (proxy for preadipocytes). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in HepG2, e.g. ENCSR925QAW. Best model's site strength: ref 98.6th, alt 98.5th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e28"></a>**E28** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> PHF21A (AT hook, 1 model; QBiC-SELEX coverage: own model): best model PHF21A_DBD_TC40NGGCTGT_YWQA_jolma2025_0_3_7mer (its own model), z -2.87, effect -0.079: ref allele binds slightly more; occupied, no clear allelic change (|z| below the gate). 20.58 TPM, rank 319 of 1631 TFs in GTEx:Adipose - Subcutaneous (proxy for preadipocytes). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in HepG2, e.g. ENCSR315VYZ. Best model's site strength: ref 98.4th, alt 84.6th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e29"></a>**E29** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> ZNF48 (C2H2 ZF, 1 model; QBiC-SELEX coverage: own model): best model ZNF48_FL_TC40NTGCATA_YWKA_jolma2025_0_3_7mer (its own model), z 2.69, effect 0.153: alt allele binds slightly more; occupied, no clear allelic change (|z| below the gate). 4.75 TPM, rank 822 of 1631 TFs in GTEx:Adipose - Subcutaneous (proxy for preadipocytes). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in HepG2, e.g. ENCSR415AEB. Best model's site strength: ref 88.8th, alt 98.1th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

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

<a id="e35"></a>**E35** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-26T13:17:12+00:00)

> No ENCODE ATF3 ChIP-seq peak contains chr16:53767042:T>C in biosamples matching 'subcutaneous adipose'. Absence can also mean no ATF3 experiment in that biosample. In other biosamples, 1 ATF3 peaks do contain the variant: HCT116 (experiments ENCSR000BUG).

<a id="e36"></a>**E36** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr16_53767042_T_C_b38&datasetId=gtex_v8; retrieved 2026-10-25T17:30:38+00:00)

> 0 significant GTEx v8 single-tissue eQTLs for chr16_53767042_T_C_b38 in tissues matching 'Adipose - Subcutaneous'. NES is the effect of the alt allele (C) relative to ref (T).

<a id="e37"></a>**E37** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=rs1421085%20FTO%20adipose%20enhancer%20ARID5B%20allele-specific&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T13:17:13+00:00)

> Europe PMC: 36 hits for 'rs1421085 FTO adipose enhancer ARID5B allele-specific'; top 7 with PMIDs:
> PMID 42877975 (2026): Human Genetics of Adipose Dysfunction: Genomic Mechanisms and Therapeutic Opportunities in Cardiometabolic Disease.
> PMID 42299366 (2026): Hepatogenomics of MAFLD in Asian Population: Genetic Polymorphisms and Pathway-Based Insights.
> PMID 42589667 (2026): Functional Annotation of GWAS Loci Using Public Transcriptome and Epigenome Datasets Reveals Non-Coding Genes and Regulatory Elements Which May Contribute to BMI.
> PMID 41273414 (2026): Bridging the variant-to-function gap in type 2 diabetes: advances and challenges.
> PMID 37200795 (2023): <i>FTO</i> Gene Polymorphisms at the Crossroads of Metabolic Pathways of Obesity and Epigenetic Influences.
> PMID 37416800 (2023): Human abdominal subcutaneous-derived active beige adipocytes carrying <i>FTO</i> rs1421085 obesity-risk alleles exert lower thermogenic capacity.
> PMID 36882962 (2023): Technologies, strategies, and cautions when deconvoluting genome-wide association signals: FTO in focus.

<a id="e37a"></a>**E37a** literature_search, Europe PMC abstract, PMID 37416800 (https://europepmc.org/article/MED/37416800; retrieved 2026-10-26T13:17:13+00:00)

> The rs1421085 T-to-C single-nucleotide polymorphism (SNP) of the human FTO gene interrupts a conserved motif for ARID5B repressor, resulting in adipocyte type shift from beige to white.

<a id="e37b"></a>**E37b** literature_search, Europe PMC abstract, PMID 37416800 (https://europepmc.org/article/MED/37416800; retrieved 2026-10-26T13:17:13+00:00)

> We did not observe any influence of the FTO rs1421085 SNP on white and inactive beige adipocytes highlighting its exclusive and critical effect when adipocytes were activated for thermogenesis.
