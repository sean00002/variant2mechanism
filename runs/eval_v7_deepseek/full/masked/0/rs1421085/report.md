# rs1421085 and Obesity (FTO)

Configuration `full`, masked mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.05 over 22 model calls; 444 s.

Variant `chr16:53767042:T>C` (germline); expression context: GTEx:Adipose - Subcutaneous (proxy for preadipocytes).

**Verdict: undetermined.** The null leads, but nothing tested counts against ATF3, JUN, FOXP1.

Association with the disease (not part of the verdict): GWAS Catalog found; Open Targets fine-mapping found.

Pairwise ranking (Bradley-Terry strengths): H3_ATF3 0.33, H2_JUN 0.28, H4_FOXP1 0.28, H5_null 0.11. 2 of 6 pairs came out differently in the two orders.

## QBiC-SELEX screen (occupancy first)

Occupied candidates: ATF3 (bound elsewhere, z 21.73); TEAD1 (bound elsewhere, z 21.23); JUN (bound elsewhere, z 17.91); FOXP1 (bound elsewhere, z -16.49); USF2 (bound elsewhere, z 9.15); MAX (bound elsewhere, z 9.06); GATAD2A (bound elsewhere, z 5.71); HMG20B (bound elsewhere, z 4.52); PHF21A (bound elsewhere, z -2.87, no clear allelic change); ZNF48 (bound elsewhere, z 2.69, no clear allelic change). Occupancy unknown: MEIS3 (z 54.71); PKNOX2 (z 54.71); TGIF1 (z 54.71); NR4A2 (z 32.74); NR4A3 (z 32.74). Diagnostic, not shown to the model: 425 of 997 models pass Bonferroni.

## Ranked chains

### 1. H5_null: No TF-mediated allelic effect at this base; the association reflects a linked causal variant or no functional base change (p = 0.55)

Null chain: no TF-mediated effect of this variant.

Predictions: No reproducible allele-specific TF occupancy or enhancer activity at chr16:53767042 in preadipocytes.; The obesity association is driven by another variant in LD or by a bystander variant rather than this base.; QBiC-SELEX binding changes are not occupied or functional in the relevant adipose cell type.

Falsified if: A reproducible allele-specific TF occupancy or enhancer assay in preadipocytes shows a functional effect at this base.; A direct adipose eQTL or allelic reporter shows this base changes FTO/IRX3 in the obesity-relevant direction.

### 2. H3_ATF3: ATF3 binds the alt C allele more and may repress FTO, leaving the risk T allele less repressed (p = 0.21)

TF ATF3 (QBiC-SELEX coverage own_model), alt allele binds more; element EH38E3181208 dELS in FTO intron; gene FTO; cell type Adipose - Subcutaneous (preadipocyte proxy).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | ATF3's own QBiC-SELEX model gives a strong alt-C-binding-more effect (z 21.73, effect 1.403) at a strong site; however, ATF3 ChIP-seq peaks over the variant are reported only in HCT116 and K562, and ENCODE has no adipose ATF3 assay, so adipose occupancy is unproven. | weak | [E20](#e20), [E09](#e09), [E38](#e38) |
| element | The variant lies in a distal enhancer-like cCRE, a plausible ATF3-responsive regulatory element. | supported | [E03](#e03) |
| gene | FTO is the top L2G gene and has an alt-C-positive eQTL in skeletal muscle, but this variant has no significant subcutaneous adipose eQTL; an ATF3-repressor-to-FTO mechanism in adipose is inferential. | weak | [E16](#e16), [E17](#e17), [E36](#e36) |
| cell_type | ATF3 is expressed in subcutaneous adipose and a K562 ReMap peak overlaps the variant, but no adipose ENCODE ChIP-seq biosample is available, so preadipocyte occupancy is not directly demonstrated. | supported | [E20](#e20), [E04](#e04), [E38](#e38) |
| phenotype | The GWAS risk allele is T; if ATF3 represses FTO, less ATF3 binding on risk T could derepress FTO and contribute to obesity, but this direction is not directly tested by the provided adipose data. | weak | [E15](#e15), [E16](#e16) |

Predictions: Allele-specific ATF3 occupancy in preadipocytes, with alt C > ref T.; ATF3 loss increases FTO expression or enhancer activity if ATF3 is repressive.; ATF3 perturbation modifies the allelic enhancer effect.

Falsified if: ATF3 does not occupy this element in adipose-lineage cells.; ATF3 binding is not allele-specific in preadipocytes.; ATF3 perturbation does not affect FTO expression or allelic enhancer activity.

### 3. H2_JUN: JUN binds the alt C allele more and alters FTO expression in adipose (p = 0.14)

TF JUN (QBiC-SELEX coverage own_model), alt allele binds more; element EH38E3181208 dELS in FTO intron; gene FTO; cell type Adipose - Subcutaneous (preadipocyte proxy).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | JUN's own QBiC-SELEX model predicts that alt C binds more strongly (z 17.91, effect 0.317); however, the only cited JUN ChIP-seq peak over the variant is in HepG2, and ENCODE/ReMap provide no adipose JUN occupancy, so adipose occupancy is unproven. | weak | [E22](#e22), [E05](#e05), [E37](#e37) |
| element | The variant lies in a distal enhancer-like cCRE, compatible with JUN acting at a regulatory element. | supported | [E03](#e03) |
| gene | FTO is the top L2G gene and has an alt-C-positive eQTL in skeletal muscle, but this variant has no significant subcutaneous adipose eQTL, so the JUN-to-FTO link in the relevant tissue is indirect. | weak | [E16](#e16), [E17](#e17), [E36](#e36) |
| cell_type | JUN is highly expressed in subcutaneous adipose, but no matching adipose ChIP-seq biosample is available, so occupancy in preadipocytes is not shown. | supported | [E05](#e05), [E04](#e04), [E37](#e37) |
| phenotype | The locus is strongly associated with obesity/BMI and the reported risk allele is T, whereas JUN binding and the cited FTO skeletal-muscle eQTL are alt-C-positive; whether JUN activation or repression reconciles this direction is untested. | weak | [E15](#e15), [E16](#e16) |

Predictions: Allele-specific JUN occupancy in preadipocytes, with alt C > ref T.; JUN perturbation changes FTO expression or allelic enhancer activity.; The alt C allele increases JUN-dependent reporter activity.

Falsified if: JUN does not occupy this element in adipose-lineage cells.; JUN binding is not allele-specific in preadipocytes.; JUN perturbation does not affect FTO expression or enhancer activity.

### 4. H4_FOXP1: FOXP1 binds the ref T allele more and modulates FTO through this enhancer (p = 0.10)

TF FOXP1 (QBiC-SELEX coverage own_model), ref allele binds more; element EH38E3181208 dELS in FTO intron; gene FTO; cell type Adipose - Subcutaneous (preadipocyte proxy).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | FOXP1's own QBiC-SELEX model supports ref T binding more strongly (z -4.91, effect -0.262), and a FOXC2-mapped model gives a larger ref-T effect (z -16.49); however, occupancy over the variant is only reported in HepG2 and no adipose FOXP1 ChIP-seq exists, so allele-specific adipose binding remains weak. | weak | [E23](#e23), [E40](#e40), [E04](#e04), [E39](#e39) |
| element | The variant lies in a distal enhancer-like cCRE, compatible with allele-specific FOXP1 regulation. | supported | [E03](#e03) |
| gene | FTO is the top L2G gene and has an alt-C-positive eQTL in skeletal muscle, but there is no significant adipose eQTL and no FOXP1 perturbation data, so the FOXP1-to-FTO link is indirect. | weak | [E16](#e16), [E17](#e17), [E36](#e36) |
| cell_type | FOXP1 is expressed at modest levels in subcutaneous adipose, but no matching adipose ChIP-seq is provided, so occupancy in preadipocytes is inferred rather than shown. | supported | [E23](#e23), [E04](#e04), [E39](#e39) |
| phenotype | The GWAS risk allele is T, which is also the FOXP1-ref-binding allele, but whether higher FOXP1 binding at risk T increases or decreases FTO in adipose is not established. | weak | [E15](#e15), [E16](#e16) |

Predictions: Allele-specific FOXP1 occupancy in preadipocytes, with ref T > alt C.; FOXP1 perturbation changes FTO expression or allelic enhancer activity.; The ref T allele increases FOXP1-dependent reporter activity.

Falsified if: FOXP1 does not occupy this element in adipose-lineage cells.; FOXP1 binding is not allele-specific in preadipocytes.; FOXP1 perturbation does not affect FTO expression or enhancer activity.

## Prediction matrix

| Test | Cost | Separates top two | H5_null | H3_ATF3 | H2_JUN | H4_FOXP1 |
| --- | --- | --- | --- | --- | --- | --- |
| Allele-specific ATF3 ChIP-qPCR at chr16:53767042 in subcutaneous preadipocytes | medium | yes | No reproducible ATF3 occupancy or no allelic difference at this base. | ATF3 enrichment with alt C > ref T at this base. | No ATF3 enrichment or no allelic difference at this base. | No ATF3 enrichment or no allelic difference at this base. |
| Allele-specific JUN ChIP-qPCR at chr16:53767042 in subcutaneous preadipocytes | medium | no | No reproducible JUN occupancy or no allelic difference at this base. | No JUN enrichment or no allelic difference at this base. | JUN enrichment with alt C > ref T at this base. | No JUN enrichment or no allelic difference at this base. |
| Allele-specific FOXP1 ChIP-qPCR at chr16:53767042 in subcutaneous preadipocytes | medium | no | No reproducible FOXP1 occupancy or no allelic difference at this base. | No FOXP1 enrichment or no allelic difference at this base. | No FOXP1 enrichment or no allelic difference at this base. | FOXP1 enrichment with ref T > alt C at this base. |
| Allelic enhancer reporter/MPRA in preadipocytes with an ATF3-site mutation at the variant | medium | yes | No reproducible allelic activity difference. | Allelic activity changes in an ATF3-site-dependent manner. | Allelic activity remains JUN-dependent, not ATF3-dependent. | Allelic activity remains FOXP1-dependent, not ATF3-dependent. |
| CRISPRi or knockout of ATF3 in preadipocytes followed by FTO expression measurement | high | yes | FTO expression is unchanged by ATF3 perturbation. | FTO expression changes after ATF3 perturbation. | FTO expression is unchanged by ATF3 perturbation. | FTO expression is unchanged by ATF3 perturbation. |

## Next experiment

Allele-specific ATF3 ChIP-qPCR at chr16:53767042 in subcutaneous preadipocytes is the cheapest test that directly separates H3_ATF3 from H5_null.

## Refinement rounds

Stopped: round 2 left the top chain and the grades of its links unchanged.

### Round 1

- qbic_tf_detail({"tf": "ARID5B"}) for H1_ARID5B.binding, ran as [E35](#e35) (not tested). Expected: If ARID5B has an own or mapped QBiC-SELEX model at this variant, its allele effect would directly support or refute the claimed ref>T binding and could raise or lower H1. If ARID5B is absent from QBiC-SELEX coverage, H1.binding remains unsupported/missing, weakening H1 relative to chains with direct binding predictions.
- eqtl_lookup({"tissue": "Adipose - Subcutaneous"}) for H2_JUN.gene (also informs H1/H3/H4 gene links), ran as [E36](#e36). Expected: If this variant is an adipose eQTL for FTO or IRX3, its allele direction will test whether the alt-C-binding chains can be reconciled with the T risk allele and whether FTO/IRX3 mediation is plausible in the relevant tissue. If no adipose eQTL exists, the gene links remain tissue-mismatched and weak, and the null gains relative weight.
- chip_peaks({"tf": "JUN", "biosample": "Adipose - Subcutaneous"}) for H2_JUN.binding, ran as [E37](#e37) (not tested). Expected: If JUN has a ChIP-seq peak over this base in subcutaneous adipose, H2.binding gains the missing adipose occupancy arm and H2 rises. If no adipose JUN peak is found, JUN binding remains supported only by a HepG2 peak plus QBiC-SELEX, so H2.binding stays weak and H2 falls relative to H1 or the null.

- Result of ARID5B QBiC-SELEX model or allele-specific binding evidence: E35: ARID5B is not in QBiC-SELEX coverage (coverage not_in_coverage); no ARID5B allele effect is available. (as expected: yes)
- Result of Subcutaneous adipose eQTL for this variant: E36: no significant single-tissue eQTL in Adipose_Subcutaneous for chr16_53767042_T_C. (as expected: yes)
- Result of JUN ChIP-seq occupancy over the variant in subcutaneous adipose: E37: ENCODE has no JUN ChIP-seq experiment in adipose; ReMap has no JUN peak over the variant, which is no evidence against binding. (as expected: unclear)

Chains after revision: null 0.44; ATF3 0.24; JUN 0.14; FOXP1 0.10; ARID5B 0.08. Link grades changed: H1_ARID5B.cell_type: weak → missing.

### Round 2

- chip_peaks({"tf": "ATF3", "biosample": "Adipose - Subcutaneous"}) for H3_ATF3.cell_type, ran as [E38](#e38) (not tested). Expected: If an ENCODE adipose ATF3 peak contains the variant, H3 cell_type and binding strengthen and H3 rises; if ENCODE assayed ATF3 in adipose but has no peak here, H3 falls; if ATF3 was never assayed there, the result is not tested and H3 is unchanged.
- chip_peaks({"tf": "FOXP1", "biosample": "Adipose - Subcutaneous"}) for H4_FOXP1.cell_type, ran as [E39](#e39) (not tested). Expected: If an adipose FOXP1 peak contains the variant, H4 occupancy is supported and H4 rises; if assayed with no peak, H4 falls; if not assayed, no information and H4 is unchanged.
- qbic_tf_detail({"tf": "FOXP1"}) for H4_FOXP1.binding, ran as [E40](#e40). Expected: If FOXP1 has an own-model QBiC-SELEX prediction with a clear ref>alt effect, H4 binding becomes less model-ambiguous and H4 rises; if only CIS-BP-mapped FOXC2-family models support ref>alt, H4 remains weak and falls relative to better-supported chains.

- Result of chip_peaks({"tf": "ATF3", "biosample": "Adipose - Subcutaneous"}): E38 reports that ENCODE has no ATF3 ChIP-seq experiment in adipose/subcutaneous biosamples; ReMap has an ATF3 peak over the variant only in K562. This is not tested for adipose occupancy, so H3 is unchanged. (as expected: yes)
- Result of chip_peaks({"tf": "FOXP1", "biosample": "Adipose - Subcutaneous"}): E39 reports that ENCODE has no FOXP1 ChIP-seq experiment in adipose/subcutaneous biosamples and ReMap has no FOXP1 peak over the variant. This is not tested for adipose occupancy, so H4 is unchanged. (as expected: yes)
- Result of qbic_tf_detail({"tf": "FOXP1"}): E40 shows an FOXP1 own-model QBiC-SELEX prediction with ref T > alt C (z -4.91, effect -0.262) and a stronger FOXC2-mapped forkhead model (z -16.49); the own-model effect supports the direction but is small, and adipose occupancy is still absent. H4 remains weak rather than clearly strengthened. (as expected: unclear)

Chains after revision: null 0.55; ATF3 0.21; JUN 0.14; FOXP1 0.10. Link grades changed: H1_ARID5B.binding: missing → absent, H1_ARID5B.cell_type: missing → absent, H1_ARID5B.element: supported → absent, H1_ARID5B.gene: weak → absent, H1_ARID5B.phenotype: weak → absent, H2_JUN.cell_type: weak → supported, H3_ATF3.cell_type: weak → supported, H4_FOXP1.cell_type: weak → supported.

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

<a id="e28"></a>**E28** qbic_screen (tested, negative), QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> PHF21A (AT hook, 1 model; QBiC-SELEX coverage: own model): best model PHF21A_DBD_TC40NGGCTGT_YWQA_jolma2025_0_3_7mer (its own model), z -2.87, effect -0.079: ref allele binds slightly more; occupied, no clear allelic change (|z| below the gate). 20.58 TPM, rank 319 of 1631 TFs in GTEx:Adipose - Subcutaneous (proxy for preadipocytes). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in HepG2, e.g. ENCSR315VYZ. Best model's site strength: ref 98.4th, alt 84.6th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e29"></a>**E29** qbic_screen (tested, negative), QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

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

<a id="e35"></a>**E35** qbic_tf_detail (not tested), QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> {"tf":"ARID5B","symbol":"ARID5B","via":"hgnc_symbol","notes":[],"coverage":"not_in_coverage"}

<a id="e36"></a>**E36** eqtl_lookup (tested, negative), GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr16_53767042_T_C_b38&datasetId=gtex_v8; retrieved 2026-10-25T17:30:38+00:00)

> GTEx v8 tested chr16_53767042_T_C_b38: no significant single-tissue eQTL in Adipose_Subcutaneous.

<a id="e37"></a>**E37** chip_peaks (not tested), ENCODE experiment search; ReMap 2022 (UCSC track ReMapTFs) (https://www.encodeproject.org/search/?type=Experiment&assay_title=TF+ChIP-seq&status=released&assembly=GRCh38&format=json&limit=all&field=target.label&field=biosample_ontology.term_name&field=accession; retrieved local)

> ENCODE has no JUN ChIP-seq experiment in biosamples matching 'Adipose - Subcutaneous', so ENCODE says nothing about it there, for or against. ENCODE assayed JUN in: A549, H1, HeLa-S3, HepG2, K562, MCF-7, WTC11, endothelial cell of umbilical vein. ReMap 2022 has no JUN peak over the variant (ReMap lists peaks only, so this is no evidence against binding).

<a id="e38"></a>**E38** chip_peaks (not tested), ENCODE experiment search; ReMap 2022 (UCSC track ReMapTFs) (https://www.encodeproject.org/search/?type=Experiment&assay_title=TF+ChIP-seq&status=released&assembly=GRCh38&format=json&limit=all&field=target.label&field=biosample_ontology.term_name&field=accession; retrieved local)

> ENCODE has no ATF3 ChIP-seq experiment in biosamples matching 'Adipose - Subcutaneous', so ENCODE says nothing about it there, for or against. ENCODE assayed ATF3 in: A549, GM12878, H1, HCT116, HepG2, K562, WTC11, liver. ReMap 2022 (published ChIP-seq, reprocessed): 1 ATF3 peaks contain the variant, in 1 biosamples: K-562 (ENCSR028UIU). 0 of them in biosamples matching 'Adipose - Subcutaneous'.

<a id="e39"></a>**E39** chip_peaks (not tested), ENCODE experiment search; ReMap 2022 (UCSC track ReMapTFs) (https://www.encodeproject.org/search/?type=Experiment&assay_title=TF+ChIP-seq&status=released&assembly=GRCh38&format=json&limit=all&field=target.label&field=biosample_ontology.term_name&field=accession; retrieved local)

> ENCODE has no FOXP1 ChIP-seq experiment in biosamples matching 'Adipose - Subcutaneous', so ENCODE says nothing about it there, for or against. ENCODE assayed FOXP1 in: HepG2, K562, WTC11. ReMap 2022 has no FOXP1 peak over the variant (ReMap lists peaks only, so this is no evidence against binding).

<a id="e40"></a>**E40** qbic_tf_detail, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> {"tf":"FOXP1","symbol":"FOXP1","via":"hgnc_symbol","notes":[],"coverage":"own_model","variant":"chr16:53767042:T>C","gate_p":5.02e-05,"models":[{"model":"FOXP1_eDBD_TTATGA40NCAG_KT_yin2017_0_4_7mer","mapping":"own","group":"G069 Forkhead, 2 models","quality":0.81,"effect":-0.262,"z":-4.91,"p":9.3e-07,"rank_abs_z":"329/997","passed_gate":true,"site_strength":{"ref_percentile":97.7,"alt_percentile":93.2,"k":7}},{"model":"FOXC2_eDBD_TCAGAA40NAGG_KO_yin2017_0_4_7mer","mapping":"CIS-BP (FOXC2)","group":"G007 Forkhead, 10 models","quality":0.877,"effect":-1.476,"z":-16.49,"p":4.3e-61,"rank_abs_z":"48/997","passed_gate":true,"site_strength":{"ref_percentile":99.4,"alt_percentile":92.1,"k":7}},{"model":"FOXJ3_NA_TAAACA20NCAA_AF_jolma2013_0_3_7mer","mapping":"CIS-BP (FOXJ3)","group":"G183 Forkhead, 1 model","quality":0.654,"effect":-0.102,"z":-2.91,"p":0.0036,"rank_abs_z":"526/997","passed_gate":false,"site_strength":{"ref_percentile":99.0,"alt_percentile":92.3,"k":7}},{"model":"FOXP3_FL_TCCACA40NGCC_KAE_yin2017_0_3_7mer","mapping":"CIS-BP (FOXP3)","group":"G069 Forkhead, 2 models","quality":0.473,"effect":0.066,"z":1.2,"p":0.23,"rank_abs_z":"784/997","passed_gate":false,"site_strength":{"ref_percentile":99.6,"alt_percentile":98.6,"k":7}}]}
