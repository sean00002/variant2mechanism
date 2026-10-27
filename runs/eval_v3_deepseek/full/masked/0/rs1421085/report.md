# rs1421085 and Obesity (FTO)

Configuration `full`, masked mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.05 over 7 model calls; 289 s.

Variant `chr16:53767042:T>C` (germline); expression context: GTEx:Adipose - Subcutaneous (proxy for preadipocytes).

## QBiC-SELEX screen (occupancy first)

Occupied candidates: ATF3 (bound elsewhere, z 21.73); TEAD1 (bound elsewhere, z 21.23); JUN (bound elsewhere, z 17.91); FOXP1 (bound elsewhere, z -16.49); USF2 (bound elsewhere, z 9.15); MAX (bound elsewhere, z 9.06); GATAD2A (bound elsewhere, z 5.71); HMG20B (bound elsewhere, z 4.52); PHF21A (bound elsewhere, z -2.87, no clear allelic change); ZNF48 (bound elsewhere, z 2.69, no clear allelic change). Occupancy unknown: MEIS3 (z 54.71); PKNOX2 (z 54.71); TGIF1 (z 54.71); NR4A2 (z 32.74); NR4A3 (z 32.74). Diagnostic, not shown to the model: 425 of 997 models pass Bonferroni.

## Ranked chains

### 1. H5_NULL: Null: linked causal variant or no TF-mediated allelic effect at this base (p = 0.44)

Null chain: no TF-mediated effect of this variant.

Predictions: No allele-specific TF occupancy at this exact base in preadipocytes.; Any GWAS/eQTL effect is mediated by a linked variant in the same dELS or by another regulatory mechanism.; CRISPR editing of this single base does not change FTO enhancer activity.

Falsified if: A reproducible allele-specific TF occupancy at this exact base in subcutaneous preadipocytes is demonstrated.; CRISPR editing of this single base changes FTO enhancer activity or FTO expression in preadipocytes.; Conditioning on this SNP abolishes the FTO/obesity signal while a linked variant retains it.

### 2. H1_ATF3: ATF3 gains binding on the non-risk C allele at an FTO intronic dELS (p = 0.22)

TF ATF3 (QBiC-SELEX coverage own_model), alt allele binds more; element dELS EH38E3181208; gene FTO; cell type Adipose - Subcutaneous / preadipocytes.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | ATF3 binds the alt C allele more strongly than ref T: QBiC-SELEX with ATF3's own model gives z 21.73 and effect +1.403, with a strong site on both alleles (ref 98.9th, alt 99.7th percentile). ATF3 is expressed in adipose (57.63 TPM, rank 88/1631), but the only ENCODE ChIP peak over the variant is in HCT116, and no adipose ATF3 peak is reported; E04 also notes no ENCODE biosample matches the expression context, so adipose occupancy is not proven. I chose ATF3 because it has an own-model QBiC alt-gain, strong site, and reasonably high adipose expression among the bound-elsewhere TFs. | weak | [E20](#e20), [E09](#e09), [E35](#e35), [E04](#e04) |
| element | The variant lies in dELS EH38E3181208, an active enhancer-like cCRE with co-factor/Pol II binding in ENCODE, so an allele-specific ATF3 site could alter enhancer output; however, the cCRE activity data are maxima over biosamples and are not adipose-specific. | supported | [E03](#e03), [E04](#e04) |
| gene | The dELS is in the FTO intron, and FTO is the top Open Targets L2G gene (0.99) with a GTEx FTO eQTL in skeletal muscle (alt C NES +0.14); however, there is no significant adipose eQTL in GTEx v8, so FTO is the best-supported target but adipose target-gene direction is not established. IRX3 is not excluded as an alternative target. | weak | [E01](#e01), [E02](#e02), [E16](#e16), [E17](#e17), [E36](#e36) |
| cell_type | Subcutaneous adipose/preadipocytes are the disease-relevant expression context; ATF3 is expressed there and the element is active, but matched adipose ATF3 occupancy is absent/unknown. | weak | [E20](#e20), [E03](#e03), [E04](#e04), [E35](#e35) |
| phenotype | GWAS reports the T allele as the risk/effect allele for BMI and obesity. ATF3 binds C more than T, so risk T has weaker ATF3 binding; if ATF3 represses FTO at this element, risk T would derepress FTO, while if ATF3 activates FTO the direction would be opposite. The ATF3-to-FTO-to-obesity direction is therefore conditional, not demonstrated. | weak | [E15](#e15), [E16](#e16), [E18](#e18), [E20](#e20) |

Predictions: Allele-specific ATF3 CUT&RUN/ChIP in heterozygous preadipocytes will show stronger ATF3 occupancy on C than T at this base.; ATF3 knockdown/knockout will change FTO enhancer reporter activity or FTO expression in preadipocytes.; The risk T allele will have lower ATF3 occupancy; FTO expression direction will depend on whether ATF3 is repressive or activating at this element.

Falsified if: Allele-specific ATF3 CUT&RUN/ChIP in subcutaneous preadipocytes shows no C-over-T occupancy at this base.; ATF3 perturbation does not change FTO enhancer activity or FTO expression in preadipocytes.; A linked variant in the same dELS fully explains the adipose/GWAS signal and this base has no allelic effect.

### 3. H2_TEAD1: TEAD1 gains binding on the non-risk C allele at the FTO intronic dELS (p = 0.12)

TF TEAD1 (QBiC-SELEX coverage own_model), alt allele binds more; element dELS EH38E3181208; gene FTO; cell type Adipose - Subcutaneous / preadipocytes.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | TEAD1 binds the alt C allele more strongly than ref T: QBiC-SELEX with TEAD1's own model gives z 21.23 and effect +1.544, with a strong site on both alleles (98.8th percentile). TEAD1 is expressed in adipose (40.88 TPM, rank 148/1631), but the only ENCODE ChIP peak over the variant is in HepG2, not adipose; adipose occupancy is unproven. | weak | [E21](#e21), [E12](#e12), [E04](#e04) |
| element | The variant lies in dELS EH38E3181208, an active enhancer-like cCRE, so allele-specific TEAD1 binding could change enhancer activity; adipose-specific activity is not shown. | supported | [E03](#e03), [E04](#e04) |
| gene | The dELS is in the FTO intron and FTO is the top L2G gene (0.99), with a skeletal-muscle FTO eQTL (alt C NES +0.14); no significant adipose eQTL is reported, and IRX3 remains an unexcluded alternative target. | weak | [E01](#e01), [E02](#e02), [E16](#e16), [E17](#e17), [E36](#e36) |
| cell_type | Subcutaneous adipose/preadipocytes are the expression context; TEAD1 is expressed there, but matched adipose TEAD1 ChIP and adipose-specific enhancer activity are not demonstrated. | weak | [E21](#e21), [E03](#e03), [E04](#e04) |
| phenotype | Risk T binds TEAD1 less than C. If TEAD1 is activating at this element, risk T would lower TEAD1-dependent FTO enhancer output; whether lower FTO in preadipocytes promotes obesity is not established, so the phenotype direction remains conditional. | weak | [E15](#e15), [E16](#e16), [E18](#e18), [E21](#e21) |

Predictions: Allele-specific TEAD1 CUT&RUN/ChIP in preadipocytes will show stronger TEAD1 occupancy on C than T.; TEAD1 knockdown will reduce FTO enhancer reporter activity if TEAD1 is activating at this element.; Risk T will show lower TEAD1 occupancy and, if TEAD1 is activating, lower FTO expression.

Falsified if: Allele-specific TEAD1 CUT&RUN/ChIP in subcutaneous preadipocytes shows no C-over-T occupancy at this base.; TEAD1 perturbation does not change FTO enhancer activity or FTO expression in preadipocytes.; TEAD1 occupancy at this element is not detectable in adipose-lineage cells.

### 4. H3_JUN: JUN/AP-1 gains binding on the non-risk C allele at the FTO intronic dELS (p = 0.12)

TF JUN (QBiC-SELEX coverage own_model), alt allele binds more; element dELS EH38E3181208; gene FTO; cell type Adipose - Subcutaneous / preadipocytes.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | JUN binds the alt C allele more strongly than ref T: QBiC-SELEX with JUN's own model gives z 17.91 and effect +0.317; the better-allele site strength rises from 82.8th percentile on ref to 99.8th on alt. JUN is very highly expressed in adipose (442.88 TPM, rank 3/1631), but the only ENCODE ChIP peak over the variant is in HepG2, not adipose; AP-1 family redundancy further weakens the specific JUN claim. | weak | [E22](#e22), [E05](#e05), [E04](#e04) |
| element | The variant lies in dELS EH38E3181208 within an active enhancer-like cCRE, so allele-specific JUN/AP-1 occupancy could alter enhancer output; the evidence is not adipose-specific. | supported | [E03](#e03), [E04](#e04) |
| gene | The element is in the FTO intron; FTO has the strongest L2G support (0.99) and a skeletal-muscle eQTL (alt C NES +0.14), but no significant adipose eQTL is reported and IRX3 is not excluded. | weak | [E01](#e01), [E02](#e02), [E16](#e16), [E17](#e17), [E36](#e36) |
| cell_type | Subcutaneous adipose/preadipocytes are the disease-relevant context; JUN is highly expressed there, but matched adipose ChIP and adipose-specific enhancer activity are absent. | weak | [E22](#e22), [E03](#e03), [E04](#e04) |
| phenotype | Risk T has lower JUN binding than C. Because AP-1 can activate or repress, the direction of FTO change on risk T is not determined by the binding data; reduced AP-1 occupancy could shift FTO expression in preadipocytes, but the phenotype direction remains conditional. | weak | [E15](#e15), [E16](#e16), [E18](#e18), [E22](#e22) |

Predictions: Allele-specific JUN/AP-1 CUT&RUN/ChIP in preadipocytes will show stronger occupancy on C than T.; An FTO enhancer reporter will respond to JUN/AP-1 perturbation.; Risk T will have lower JUN occupancy, but the FTO expression direction may depend on AP-1 co-factors.

Falsified if: Allele-specific JUN/AP-1 CUT&RUN/ChIP in preadipocytes shows no C-over-T occupancy at this base.; JUN perturbation does not change FTO enhancer activity or FTO expression in preadipocytes.; The QBiC-SELEX JUN effect is not reproduced in an occupied chromatin context.

### 5. H4_FOXP1: FOXP1 binds the risk T allele more strongly at the FTO intronic dELS (p = 0.10)

TF FOXP1 (QBiC-SELEX coverage own_model), ref allele binds more; element dELS EH38E3181208; gene FTO; cell type Adipose - Subcutaneous / preadipocytes.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | FOXP1 binds the ref T allele more strongly than alt C: QBiC-SELEX with FOXP1's own model gives z -4.91 and effect -0.262, and the stronger CIS-BP-mapped FOXC2 model gives z -16.49 and effect -1.476 with a strong ref site (99.4th percentile) and weaker alt site (92.1st). FOXP1 is expressed at lower level in adipose (14.95 TPM, rank 419/1631), and the only ENCODE ChIP peak over the variant is in HepG2; the binding evidence is allelic but occupancy in adipose is unproven. | weak | [E37](#e37), [E23](#e23), [E04](#e04) |
| element | The variant lies in dELS EH38E3181208, an active enhancer-like cCRE, so an allele-specific FOXP1 site could alter enhancer activity; adipose-specific activity is not demonstrated. | supported | [E03](#e03), [E04](#e04) |
| gene | The dELS is in the FTO intron and FTO is the top L2G gene (0.99), with a skeletal-muscle FTO eQTL (alt C NES +0.14); no significant adipose eQTL is reported, and IRX3 remains an alternative target. | weak | [E01](#e01), [E02](#e02), [E16](#e16), [E17](#e17), [E36](#e36) |
| cell_type | Subcutaneous adipose/preadipocytes are the expression context; FOXP1 is expressed there at lower levels, but matched adipose ChIP and adipose-specific enhancer activity are missing. | weak | [E37](#e37), [E03](#e03), [E04](#e04) |
| phenotype | Risk T binds FOXP1 more strongly than C. If FOXP1 acts as a repressor at this element, risk T would repress FTO more and lower FTO expression; the FOXP1-repressive-to-obesity direction is not demonstrated, so the phenotype link is conditional. | weak | [E15](#e15), [E16](#e16), [E18](#e18), [E37](#e37) |

Predictions: Allele-specific FOXP1 CUT&RUN/ChIP in preadipocytes will show stronger FOXP1 occupancy on T than C.; FOXP1 knockdown will derepress the FTO enhancer if FOXP1 is repressive.; Risk T will show higher FOXP1 occupancy and, if FOXP1 is repressive, lower FTO expression.

Falsified if: Allele-specific FOXP1 CUT&RUN/ChIP in preadipocytes shows no ref-T preference.; FOXP1 perturbation does not change FTO enhancer activity or FTO expression in preadipocytes.; The ref-allele preference disappears with FOXP1's own model and is not reproduced with FOXP1 protein.

## Prediction matrix

| Test | Cost | Separates top two | H5_NULL | H1_ATF3 | H2_TEAD1 | H3_JUN | H4_FOXP1 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Allele-specific ATF3 CUT&RUN or ChIP in subcutaneous preadipocytes heterozygous at this SNP | medium | yes | No allele-specific ATF3 occupancy at this base. | Stronger ATF3 occupancy on C than T at this base in preadipocytes. | No ATF3 allelic difference; TEAD1 not directly tested. | No ATF3 allelic difference; JUN not directly tested. | No ATF3 allelic difference; FOXP1 not directly tested. |
| Larger subcutaneous-adipose eQTL/colocalization study for FTO and IRX3 at this variant | medium | yes | No adipose eQTL/colocalization at this base, or the signal is explained by a linked variant. | Adipose FTO eQTL/colocalization exists; if ATF3 is repressive, alt C should lower FTO. | Adipose FTO eQTL/colocalization exists; if TEAD1 is activating, alt C should raise FTO. | Adipose FTO eQTL may exist, but AP-1 direction is not fixed. | Adipose FTO eQTL/colocalization exists; if FOXP1 is repressive, alt C should raise FTO. |
| FOXP1 own-model EMSA or allele-specific FOXP1 ChIP for T versus C | low | no | No allele-specific FOXP1 binding at this base. | No FOXP1 ref-T preference; ATF3 remains candidate. | No FOXP1 ref-T preference; TEAD1 remains candidate. | No FOXP1 ref-T preference; JUN remains candidate. | FOXP1 binds T more strongly than C by own-model EMSA/allele-specific assay. |
| CRISPR single-base enhancer reporter in subcutaneous preadipocytes | high | yes | No single-base effect on enhancer activity. | Single-base C allele changes enhancer activity in an ATF3-dependent direction. | Single-base C allele increases TEAD1-dependent enhancer activity. | Single-base C allele changes AP-1-dependent enhancer activity. | Single-base T allele increases FOXP1-dependent repression, so C has higher activity if FOXP1 is repressive. |

## Next experiment

Allele-specific ATF3 CUT&RUN (or ChIP-seq) in subcutaneous preadipocytes from T/C heterozygotes, with input and ATF3 knockdown controls, to test whether ATF3 occupies this dELS and whether the C allele is preferentially bound; this directly separates H1_ATF3 from H5_NULL.

## Investigate calls

- chip_peaks({"tf": "ATF3", "biosample": "Adipose - Subcutaneous"})
- eqtl_lookup({"tissue": "Adipose - Subcutaneous"})
- qbic_tf_detail({"tf": "FOXP1"})

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

> No ENCODE ATF3 ChIP-seq peak contains chr16:53767042:T>C in biosamples matching 'Adipose - Subcutaneous'. Absence can also mean no ATF3 experiment in that biosample. In other biosamples, 1 ATF3 peaks do contain the variant: HCT116 (experiments ENCSR000BUG).

<a id="e36"></a>**E36** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr16_53767042_T_C_b38&datasetId=gtex_v8; retrieved 2026-10-25T17:30:38+00:00)

> 0 significant GTEx v8 single-tissue eQTLs for chr16_53767042_T_C_b38 in tissues matching 'Adipose - Subcutaneous'. NES is the effect of the alt allele (C) relative to ref (T).

<a id="e37"></a>**E37** qbic_tf_detail, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> {"tf":"FOXP1","symbol":"FOXP1","via":"hgnc_symbol","notes":[],"coverage":"own_model","variant":"chr16:53767042:T>C","gate_p":5.02e-05,"models":[{"model":"FOXP1_eDBD_TTATGA40NCAG_KT_yin2017_0_4_7mer","mapping":"own","group":"G069 Forkhead, 2 models","quality":0.81,"effect":-0.262,"z":-4.91,"p":9.3e-07,"rank_abs_z":"329/997","passed_gate":true,"site_strength":{"ref_percentile":97.7,"alt_percentile":93.2,"k":7}},{"model":"FOXC2_eDBD_TCAGAA40NAGG_KO_yin2017_0_4_7mer","mapping":"CIS-BP (FOXC2)","group":"G007 Forkhead, 10 models","quality":0.877,"effect":-1.476,"z":-16.49,"p":4.3e-61,"rank_abs_z":"48/997","passed_gate":true,"site_strength":{"ref_percentile":99.4,"alt_percentile":92.1,"k":7}},{"model":"FOXJ3_NA_TAAACA20NCAA_AF_jolma2013_0_3_7mer","mapping":"CIS-BP (FOXJ3)","group":"G183 Forkhead, 1 model","quality":0.654,"effect":-0.102,"z":-2.91,"p":0.0036,"rank_abs_z":"526/997","passed_gate":false,"site_strength":{"ref_percentile":99.0,"alt_percentile":92.3,"k":7}},{"model":"FOXP3_FL_TCCACA40NGCC_KAE_yin2017_0_3_7mer","mapping":"CIS-BP (FOXP3)","group":"G069 Forkhead, 2 models","quality":0.473,"effect":0.066,"z":1.2,"p":0.23,"rank_abs_z":"784/997","passed_gate":false,"site_strength":{"ref_percentile":99.6,"alt_percentile":98.6,"k":7}}]}
