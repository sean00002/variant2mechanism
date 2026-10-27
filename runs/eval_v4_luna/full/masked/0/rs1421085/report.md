# rs1421085 and Obesity (FTO)

Configuration `full`, masked mode, seed 0. Models: generator openai/gpt-6-luna, critic openai/gpt-6-luna, summariser openai/gpt-6-luna. Cost $0.03 over 14 model calls; 247 s.

Variant `chr16:53767042:T>C` (germline); expression context: GTEx:Adipose - Subcutaneous (proxy for preadipocytes).

## QBiC-SELEX screen (occupancy first)

Occupied candidates: ATF3 (bound elsewhere, z 21.73); TEAD1 (bound elsewhere, z 21.23); JUN (bound elsewhere, z 17.91); FOXP1 (bound elsewhere, z -16.49); USF2 (bound elsewhere, z 9.15); MAX (bound elsewhere, z 9.06); GATAD2A (bound elsewhere, z 5.71); HMG20B (bound elsewhere, z 4.52); PHF21A (bound elsewhere, z -2.87, no clear allelic change); ZNF48 (bound elsewhere, z 2.69, no clear allelic change). Occupancy unknown: MEIS3 (z 54.71); PKNOX2 (z 54.71); TGIF1 (z 54.71); NR4A2 (z 32.74); NR4A3 (z 32.74). Diagnostic, not shown to the model: 425 of 997 models pass Bonferroni.

## Ranked chains

### 1. H4: Null: no TF-mediated effect of this variant (p = 0.72)

Null chain: no TF-mediated effect of this variant.

Predictions: The obesity association may reflect linkage or another mechanism rather than an allele-specific TF effect at this base.; In relevant cells, there will be no reproducible TF-dependent regulatory effect attributable to this variant; an in-vitro binding difference may not occur in cells or affect a target gene.

Falsified if: A relevant-cell experiment shows a reproducible allele-specific TF effect at this site that changes a linked target gene and depends on that TF.

### 2. H2: ATF3-mediated effect at a candidate regulatory element (p = 0.14)

TF ATF3 (QBiC-SELEX coverage own_model), alt allele binds more; element The variant overlaps distal enhancer-like cCRE EH38E3181208, but activity of this cCRE in adipose cells is not established; reported SCREEN maxima are for a nearby cCRE.; gene FTO is a strong locus-to-gene candidate, but regulation of FTO by this cCRE is not demonstrated.; cell type Adipose and adipocyte-differentiation evidence makes this a plausible context to test, but ATF3 occupancy at the variant there is not established..

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | ATF3 is expressed in the adipose proxy tissue, and its own QBiC-SELEX model predicts stronger in-vitro binding to C than T. Its variant-overlapping ChIP peak is from HCT116, not a matching context, so relevant-cell occupancy remains unproven. | weak | [E04](#e04), [E09](#e09), [E20](#e20), [E36](#e36) |
| element | The variant lies in distal enhancer-like cCRE EH38E3181208, but the reported SCREEN activity maxima are for nearby cCRE EH38E3181207 and do not establish activity of the overlapping cCRE in adipose cells. | supported | [E03](#e03) |
| gene | FTO is a candidate target based on proximity and strong locus-to-gene scores, but direct regulation by this cCRE is unproven and no significant adipose-subcutaneous eQTL is reported. | supported | [E02](#e02), [E16](#e16), [E17](#e17), [E37](#e37) |
| cell_type | ATF3 has reported adipose and adipocyte-differentiation relevance, but no ATF3 peak is reported in matching preadipocytes; the absence may reflect lack of a suitable experiment. | supported | [E04](#e04), [E36](#e36), [E39a](#e39a), [E39b](#e39b) |
| phenotype | The locus is associated with obesity-related traits and T is reported as the risk allele; literature supports ATF3 relevance to adipose biology but does not show that this variant acts through ATF3 or resolve how greater C binding relates to the trait. | supported | [E15](#e15), [E16](#e16), [E39a](#e39a), [E39b](#e39b), [E39c](#e39c), [E39d](#e39d) |

Predictions: If this chain is correct, relevant-cell assays should detect ATF3 at the variant and a reproducible C-over-T occupancy difference.; A variant-dependent regulatory effect should depend on ATF3 rather than JUN or TEAD1; an effect on FTO is a candidate, not an established outcome.

Falsified if: A sufficiently powered relevant-cell assay finds no ATF3 occupancy or no reproducible C-over-T occupancy difference.; A variant-dependent regulatory effect is absent after ATF3 perturbation, while another TF is shown to mediate the effect.

### 3. H1: JUN-mediated effect at a candidate regulatory element (p = 0.09)

TF JUN (QBiC-SELEX coverage own_model), alt allele binds more; element The variant overlaps distal enhancer-like cCRE EH38E3181208, but activity of this cCRE in adipose cells is not established; reported SCREEN maxima are for a nearby cCRE.; gene FTO is a strong locus-to-gene candidate, but regulation of FTO by this cCRE is not demonstrated.; cell type Adipose-subcutaneous is a proxy for preadipocytes; JUN occupancy at the variant in this context is not established..

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | JUN is highly expressed in the adipose proxy tissue, and its own QBiC-SELEX model predicts stronger in-vitro binding to C than T. The variant-overlapping JUN peak is from HepG2, not a matching context; this does not establish JUN occupancy in preadipocytes or distinguish JUN decisively from other candidates. | weak | [E04](#e04), [E05](#e05), [E22](#e22), [E35](#e35) |
| element | The variant lies in distal enhancer-like cCRE EH38E3181208, but the reported SCREEN activity maxima are for nearby cCRE EH38E3181207 and do not establish activity of the overlapping cCRE in adipose cells. | supported | [E03](#e03) |
| gene | FTO is a candidate target based on proximity and strong locus-to-gene scores, but direct regulation by this cCRE is unproven and no significant adipose-subcutaneous eQTL is reported. | supported | [E02](#e02), [E16](#e16), [E17](#e17), [E37](#e37) |
| cell_type | Adipose-subcutaneous is a proxy for preadipocytes; no JUN peak is reported in a matching context, although this may reflect lack of a suitable experiment. | supported | [E04](#e04), [E05](#e05), [E35](#e35) |
| phenotype | The locus is associated with obesity-related traits and T is reported as the risk allele, but the evidence does not connect JUN binding at this site to obesity or establish the downstream direction. | supported | [E15](#e15), [E16](#e16) |

Predictions: If this chain is correct, relevant-cell assays should detect JUN at the variant and a reproducible C-over-T occupancy difference.; A regulatory effect attributable to the variant should depend on JUN; the affected gene and direction of expression change are not established.

Falsified if: A sufficiently powered relevant-cell assay finds no JUN occupancy or no reproducible C-over-T occupancy difference.; A variant-dependent regulatory effect is absent after JUN perturbation, while another TF is shown to mediate the effect.

### 4. H3: TEAD1-mediated effect at a candidate regulatory element (p = 0.05)

TF TEAD1 (QBiC-SELEX coverage own_model), alt allele binds more; element The variant overlaps distal enhancer-like cCRE EH38E3181208, but activity of this cCRE in adipose cells is not established; reported SCREEN maxima are for a nearby cCRE.; gene FTO is a strong locus-to-gene candidate, but regulation of FTO by this cCRE is not demonstrated.; cell type Adipose-subcutaneous is a proxy for preadipocytes; TEAD1 occupancy at the variant in this context is not established..

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | TEAD1 is expressed in the adipose proxy tissue, and its own QBiC-SELEX model predicts stronger in-vitro binding to C than T. Its variant-overlapping ChIP peak is from HepG2; the additional search reports no matching-context peak, which does not rule out occupancy if no suitable experiment was available. | weak | [E04](#e04), [E12](#e12), [E21](#e21), [E40](#e40) |
| element | The variant lies in distal enhancer-like cCRE EH38E3181208, but the reported SCREEN activity maxima are for nearby cCRE EH38E3181207 and do not establish activity of the overlapping cCRE in adipose cells. | supported | [E03](#e03) |
| gene | FTO is a candidate target based on proximity and strong locus-to-gene scores, but direct regulation by this cCRE is unproven and no significant adipose-subcutaneous eQTL is reported. | supported | [E02](#e02), [E16](#e16), [E17](#e17), [E37](#e37) |
| cell_type | Adipose-subcutaneous is a proxy for preadipocytes; the reported TEAD1 peak is from HepG2 and no matching-context peak is reported, though a suitable experiment may be absent. | supported | [E04](#e04), [E12](#e12), [E40](#e40) |
| phenotype | The locus is associated with obesity-related traits and T is reported as the risk allele, but no supplied evidence connects TEAD1 binding at this site to obesity or establishes the downstream direction. | supported | [E15](#e15), [E16](#e16) |

Predictions: If this chain is correct, relevant-cell assays should detect TEAD1 at the variant and a reproducible C-over-T occupancy difference.; A variant-dependent regulatory effect should depend on TEAD1 rather than JUN or ATF3.

Falsified if: A sufficiently powered relevant-cell assay finds no TEAD1 occupancy or no reproducible C-over-T occupancy difference.; A variant-dependent regulatory effect is absent after TEAD1 perturbation, while another TF is shown to mediate the effect.

## Prediction matrix

| Test | Cost | Separates top two | H4 | H2 | H1 | H3 |
| --- | --- | --- | --- | --- | --- | --- |
| ATF3 CUT&RUN or ChIP in preadipocytes with allele-specific occupancy measurement at the variant | low | yes | No reproducible variant-centered, allele-specific ATF3 occupancy attributable to a causal TF-mediated effect. | ATF3 occupies the variant, with greater occupancy on C than T. | No specific prediction of ATF3 occupancy; this chain instead predicts JUN occupancy with greater occupancy on C. | No specific prediction of ATF3 occupancy; this chain instead predicts TEAD1 occupancy with greater occupancy on C. |
| Relevant-cell perturbation of each candidate TF followed by allele-aware measurement of candidate target-gene expression | medium | yes | No reproducible variant-dependent regulatory effect attributable to perturbing these TFs. | A variant-dependent regulatory effect is reduced by ATF3 perturbation. | A variant-dependent regulatory effect is reduced by JUN perturbation. | A variant-dependent regulatory effect is reduced by TEAD1 perturbation. |

## Next experiment

Perform ATF3 CUT&RUN or ChIP in preadipocytes, measuring occupancy across the variant and allele-specific enrichment. This is a low-cost first test of the leading non-null chain against the null; a positive result should be followed by a TF-perturbation assay to test regulatory consequence.

## Refinement rounds

Stopped: round limit (3).

### Round 1

- chip_peaks({"tf": "JUN", "biosample": "preadipocytes"}) for H1.binding, ran as [E35](#e35). Expected: If a JUN peak overlaps the variant in preadipocytes, H1 gains relevant-context occupancy support; if no peak is found, H1.binding remains weak and H1 falls relative to the alternatives.
- chip_peaks({"tf": "ATF3", "biosample": "preadipocytes"}) for H2.binding, ran as [E36](#e36). Expected: If an ATF3 peak overlaps the variant in preadipocytes, H2 gains relevant-context occupancy support and can be compared directly with H1; if no peak is found, H2.binding remains weak.
- eqtl_lookup({"tissue": "Adipose_Subcutaneous"}) for H1.gene, ran as [E37](#e37). Expected: If this variant has an adipose-subcutaneous eQTL for FTO, H1.gene gains relevant-tissue expression support, though this would not prove that the cCRE mediates the effect; an eQTL for another gene would shift target-gene consideration, and no eQTL would leave FTO as a candidate supported mainly by L2G and proximity.

- Result of chip_peaks({"tf":"JUN","biosample":"preadipocytes"}): E35 reports no JUN peak overlapping the variant in matching preadipocytes; a peak is reported in HepG2. The absence may reflect no matching-biosample experiment. (as expected: yes)
- Result of chip_peaks({"tf":"ATF3","biosample":"preadipocytes"}): E36 reports no ATF3 peak overlapping the variant in matching preadipocytes; a peak is reported in HCT116. The absence may reflect no matching-biosample experiment. (as expected: yes)
- Result of eqtl_lookup({"tissue":"Adipose_Subcutaneous"}): E37 reports no significant GTEx v8 eQTL for this variant in Adipose_Subcutaneous. (as expected: yes)

Chains after revision: null 0.71; JUN 0.12; ATF3 0.09; TEAD1 0.08. Link grades changed: H1.cell_type: weak → supported, H2.cell_type: weak → supported, H3.cell_type: weak → supported.

### Round 2

- literature_search({"query": "JUN adipocyte differentiation obesity adipose"}) for H1.phenotype, ran as [E38](#e38). Expected: If the search finds evidence specifically linking JUN activity to adipocyte or obesity-relevant regulation, H1 becomes more biologically plausible relative to H2 and H3; generic JUN or obesity references would not establish this variant’s mechanism and would leave the link unchanged.
- literature_search({"query": "ATF3 adipocyte differentiation obesity adipose"}) for H2.phenotype, ran as [E39](#e39). Expected: If the search finds evidence specifically linking ATF3 activity to adipocyte or obesity-relevant regulation, H2 may rise relative to H1 and H3; generic evidence would not establish a variant-specific mechanism and would leave the link unchanged.

- Result of literature_search({"query": "JUN adipocyte differentiation obesity adipose"}): E38 returned related literature search results, but no supplied result specifically links JUN activity to adipocyte or obesity-relevant regulation. The JUN link is unchanged. (as expected: yes)
- Result of literature_search({"query": "ATF3 adipocyte differentiation obesity adipose"}): E39a-b report elevated ATF3 in adipose tissue and that ATF3 knockdown can promote adipocyte differentiation and lipid accumulation; E39c-d describe an ATF3-associated pathway in a resveratrol obesity study. This raises ATF3's biological plausibility, but does not establish this variant's mechanism. (as expected: yes)

Chains after revision: null 0.68; ATF3 0.19; JUN 0.08; TEAD1 0.05. Link grades changed: H1.phenotype: supported → missing, H2.phenotype: supported → weak, H3.phenotype: supported → missing.

### Round 3

- chip_peaks({"tf": "TEAD1", "biosample": "preadipocytes"}) for H3.binding, ran as [E40](#e40). Expected: If a variant-overlapping TEAD1 peak is found in preadipocytes, H3.binding gains relevant-context occupancy support and H3 becomes more competitive with H1 and H2. If no peak is found, H3.binding remains weak; that result would not by itself exclude occupancy if no suitable experiment was available.

- Result of chip_peaks({"tf":"TEAD1","biosample":"preadipocytes"}): E40 reports no TEAD1 ChIP-seq peak containing the variant in matching preadipocytes; the reported variant-overlapping peak is in HepG2. The absence may also reflect no suitable preadipocyte experiment. (as expected: yes)

Chains after revision: null 0.72; ATF3 0.14; JUN 0.09; TEAD1 0.05. Link grades changed: H1.phenotype: missing → supported, H2.phenotype: weak → supported, H3.phenotype: missing → supported.

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

<a id="e35"></a>**E35** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-26T02:29:32+00:00)

> No ENCODE JUN ChIP-seq peak contains chr16:53767042:T>C in biosamples matching 'preadipocytes'. Absence can also mean no JUN experiment in that biosample. In other biosamples, 1 JUN peaks do contain the variant: HepG2 (experiments ENCSR747VUU).

<a id="e36"></a>**E36** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-26T13:17:12+00:00)

> No ENCODE ATF3 ChIP-seq peak contains chr16:53767042:T>C in biosamples matching 'preadipocytes'. Absence can also mean no ATF3 experiment in that biosample. In other biosamples, 1 ATF3 peaks do contain the variant: HCT116 (experiments ENCSR000BUG).

<a id="e37"></a>**E37** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr16_53767042_T_C_b38&datasetId=gtex_v8; retrieved 2026-10-25T17:30:38+00:00)

> 0 significant GTEx v8 single-tissue eQTLs for chr16_53767042_T_C_b38 in tissues matching 'Adipose_Subcutaneous'. NES is the effect of the alt allele (C) relative to ref (T).

<a id="e38"></a>**E38** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=JUN%20adipocyte%20differentiation%20obesity%20adipose&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T22:10:34+00:00)

> Europe PMC: 6040 hits for 'JUN adipocyte differentiation obesity adipose'; top 7 with PMIDs:
> PMID 42893979 (2026): Transient activation of ciliary CCR2 signaling promotes the initiation of adipogenesis.
> PMID 42278307 (2026): Adipogenesis Under Leptin Control: Mechanisms and Model-Specific Effects.
> PMID 42340603 (2026): Adipose Tissue Plasticity and Adipogenesis: From Cellular Mechanisms to Therapeutic Targets in Obesity.
> PMID 42584735 (2026): Peroxisome proliferator-activated receptor gamma (PPARγ) as a mechano-metabolic transducer: coordinating lipid homeostasis through mechanical cues.
> PMID 42653741 (2026): Sulforaphane and Broccoli-Derived Preparations in Obesity and Obesity-Related Metabolic Dysfunction: Mechanistic Insights, Preclinical Evidence, and Clinical Perspectives.
> PMID 42310100 (2026): Adipocyte-specific ablation of Gadd45b exacerbates obesity-associated cellular senescence and metabolic disorders via Fgf1b promoter hypermethylation.
> PMID 42751295 (2026): Lipid-Associated Macrophages in Obesity: Immunometabolic Programs and Emerging Therapeutic Implications-A Narrative Review.

<a id="e39"></a>**E39** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=ATF3%20adipocyte%20differentiation%20obesity%20adipose&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T22:10:35+00:00)

> Europe PMC: 464 hits for 'ATF3 adipocyte differentiation obesity adipose'; top 8 with PMIDs:
> PMID 41059793 (2025): Eugenol inhibits preadipocyte differentiation and lipid accumulation via upregulating ATF3.
> PMID 42245131 (2026): C/EBPα plays a critical role in adipocyte differentiation and obesity.
> PMID 42375567 (2026): Resveratrol Attenuates Obesity by Inducing GDF15 Expression via the p38-ATF3 Signaling Pathway.
> PMID 41973649 (2026): The role and mechanism of UPRmt in adipocytes.
> PMID 41817010 (2026): Adhesion-Related Macrophages Regulate Metabolic Homeostasis Through CAV-1 Dependency.
> PMID 42500673 (2026): Targeting macrophage metabolism: mechanisms, cellular crosstalk and implications in obesity-associated metabolic diseases.
> PMID 42819803 (2026): GDF15 as a sentinel of metabolic integrity: a narrative review of stress signaling, multisystem pathophysiology, and therapeutic potential.
> PMID 41750407 (2026): Modulation and Reprogramming of Adipose Tissue Macrophages in Obesity.

<a id="e39a"></a>**E39a** literature_search, Europe PMC abstract, PMID 41059793 (https://europepmc.org/article/MED/41059793; retrieved 2026-10-26T22:10:35+00:00)

> ATF3 expression was increased in the adipose tissues of HFD mice and in clinically obese patients.

<a id="e39b"></a>**E39b** literature_search, Europe PMC abstract, PMID 41059793 (https://europepmc.org/article/MED/41059793; retrieved 2026-10-26T22:10:35+00:00)

> ATF3 expression was found to be elevated within the adipose tissues of overweight patients, whereas ATF3 knockdown promoted adipocyte differentiation and lipid accumulation by activating the PI3K/AKT signaling pathway.

<a id="e39c"></a>**E39c** literature_search, Europe PMC abstract, PMID 42375567 (https://europepmc.org/article/MED/42375567; retrieved 2026-10-26T22:10:35+00:00)

> Transcriptome analysis and subsequent validation experiments revealed that Activating Transcription Factor 3 (ATF3) mediates the effect of resveratrol on GDF15 expression.

<a id="e39d"></a>**E39d** literature_search, Europe PMC abstract, PMID 42375567 (https://europepmc.org/article/MED/42375567; retrieved 2026-10-26T22:10:35+00:00)

> Additionally, resveratrol-treated mice exhibited resistance to high-fat diet-induced obesity and increased plasma GDF15 levels.

<a id="e40"></a>**E40** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-26T13:36:17+00:00)

> No ENCODE TEAD1 ChIP-seq peak contains chr16:53767042:T>C in biosamples matching 'preadipocytes'. Absence can also mean no TEAD1 experiment in that biosample. In other biosamples, 1 TEAD1 peaks do contain the variant: HepG2 (experiments ENCSR497JLX).
