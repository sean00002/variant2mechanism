# rs2168101 and Neuroblastoma (LMO1)

Configuration `full`, named mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.03 over 10 model calls; 149 s.

Variant `chr11:8233861:C>A` (germline); expression context: DepMap:ACH-000149 (SK-N-SH).

## QBiC-SELEX screen (occupancy first)

Occupied candidates: GATA2 (bound here, z -56.07); GATA3 (bound here, z -56.07); ZNF8 (bound here, z 16.02); FOXJ3 (bound here, z 14.24); MAX (bound here, z -4.96); TEAD4 (bound here, z -4.85); YY1 (bound here, z 3.73, no clear allelic change); BACH2 (bound here, z -2.45, no clear allelic change); GLIS3 (bound here, z 1.73, no clear allelic change); TSHZ2 (bound here, z -0.28, no clear allelic change). Occupancy unknown: CPEB1 (z 78.94); HOXC9 (z 40.23); HOXD9 (z 40.23); ZBTB18 (z -31.2); HOXC5 (z 29.07). Diagnostic, not shown to the model: 334 of 997 models pass Bonferroni.

## Ranked chains

### 1. GATA2_ref_enhancer_LMO1: GATA2 binds the risk ref C allele more strongly at a distal LMO1 enhancer, increasing LMO1 expression and neuroblastoma risk (p = 0.58)

TF GATA2 (QBiC-SELEX coverage own_model), ref allele binds more; element distal enhancer-like cCRE EH38E1518342; gene LMO1; cell type adrenergic neuroblastoma / SK-N-SH.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The ref C allele binds GATA2 more strongly than the alt A allele. The literature strand calls this G/T, so ref C corresponds to the risk G allele and alt A to the protective T allele. GATA2 is selected because it is highly expressed in SK-N-SH (rank 17), has a SK-N-SH ChIP-seq peak over the variant, and has its own QBiC-SELEX model with a strong ref-biased change (z -56.07, effect -0.816). ChIP supports occupancy in the region, not allele-specific occupancy. | missing | [E05](#e05), [E20](#e20), [E18f](#e18f) |
| element | The variant lies in an active distal enhancer-like cCRE (EH38E1518342) with DNase, H3K27ac, H3K4me3 and TF ChIP-seq occupancy, consistent with a regulatory element. | missing | [E03](#e03), [E04](#e04) |
| gene | LMO1 is the nearest plausible target gene, lies 34.9 kb away, and is the best L2G gene for this variant. The alt A allele is associated with lower LMO1 expression in GTEx skeletal muscle, but no adrenal-gland eQTL was reported, so this direction is tissue-limited. | missing | [E02](#e02), [E16](#e16), [E17](#e17), [E37](#e37) |
| cell_type | SK-N-SH neuroblastoma cells express high GATA2 and show GATA2 ChIP-seq occupancy over the variant. Literature links the rs2168101 GATA/TATA motif to adrenergic neuroblastoma state, with the risk GATA allele corresponding to ref C. | missing | [E05](#e05), [E18f](#e18f), [E18g](#e18g) |
| phenotype | If stronger GATA2 binding at the risk ref C allele raises LMO1 expression, this is predicted to promote the adrenergic neuroblastoma state and metastasis, while the protective alt A allele would lower LMO1. GATA2-specific causality is inferred from motif literature and is not directly proven. | missing | [E18b](#e18b), [E18f](#e18f), [E18g](#e18g), [E18h](#e18h) |

Predictions: Allele-specific GATA2 ChIP in a heterozygous neuroblastoma line shows higher GATA2 occupancy on ref C than alt A.; A C vs A enhancer reporter in SK-N-SH shows higher activity for ref C than alt A.; GATA2 knockdown or CRISPRi in SK-N-SH reduces LMO1 expression and enhancer activity.; The risk ref C allele is associated with higher LMO1 expression in an adrenal/neuroblastoma-relevant context.

Falsified if: Allele-specific reporter or ChIP assays show a reproducible C vs A difference at this base.; GATA2 perturbation changes LMO1 expression in SK-N-SH in the predicted direction.; Fine-mapping excludes linked causal variants and supports rs2168101 as the causal base.

### 2. null_no_tf_mediated_effect: Null: no TF-mediated allelic effect of rs2168101; association may reflect linkage or no causal base effect (p = 0.25)

Null chain: no TF-mediated effect of this variant.

Predictions: No allele-specific TF-mediated effect of rs2168101 on LMO1 enhancer activity.; Any association is due to a linked causal variant or a passenger event rather than this base.; The variant may lie in a regulatory element but is not the causal base.

Falsified if: Allele-specific reporter or ChIP assays show a reproducible C vs A difference at this base.; GATA2 perturbation changes LMO1 expression and neuroblastoma phenotypes in the predicted direction.; Fine-mapping excludes linked causal variants and supports rs2168101 itself as the causal base.

### 3. GATA3_ref_enhancer_LMO1: GATA3 may act through the same GATA motif, with ref C binding more strongly and increasing LMO1 (p = 0.12)

TF GATA3 (QBiC-SELEX coverage own_model), ref allele binds more; element distal enhancer-like cCRE EH38E1518342; gene LMO1; cell type neuroblastoma / SK-N-SH.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The ref C allele binds GATA3 more strongly than alt A. GATA3 is expressed and has SK-N-SH ChIP-seq occupancy over the variant. E35 shows GATA3 has its own QBiC-SELEX model with a ref-biased change (effect -4.206), though GATA2 has higher expression and overlapping motif specificity. | missing | [E06](#e06), [E35](#e35) |
| element | The variant is in an active distal enhancer-like cCRE with chromatin marks and TF occupancy. | missing | [E03](#e03), [E04](#e04) |
| gene | LMO1 is nearby and is the strongest L2G gene. GTEx skeletal muscle shows alt A associated with lower LMO1, but adrenal-gland eQTL data were negative, so the expression direction is not confirmed in the most relevant tissue. | missing | [E02](#e02), [E16](#e16), [E17](#e17), [E37](#e37) |
| cell_type | GATA3 is expressed in SK-N-SH and occupies the variant by ChIP-seq, supporting a possible role in this neuroblastoma cell context. | missing | [E06](#e06) |
| phenotype | If GATA3 is the relevant GATA factor, stronger ref C binding would increase LMO1 and promote neuroblastoma, while alt A would reduce LMO1 and risk. This remains conditional because the literature supports a general GATA-motif effect rather than GATA3 specifically. | missing | [E18f](#e18f), [E18g](#e18g) |

Predictions: Allele-specific GATA3 ChIP shows higher GATA3 occupancy on ref C than alt A.; GATA3 knockdown reduces LMO1 expression or reporter activity in SK-N-SH.; The C/A enhancer effect is partly GATA3-dependent and not solely GATA2-dependent.

Falsified if: GATA3 depletion does not affect LMO1 expression or enhancer activity in SK-N-SH.; Allele-specific assays show the differential GATA occupancy is accounted for by GATA2 rather than GATA3.; The GATA3 QBiC-SELEX signal is shown not to reflect GATA3 binding at this motif.

### 4. FOXJ3_alt_repressor_LMO1: FOXJ3 binds the alt A allele more strongly and may repress LMO1, reducing neuroblastoma risk (p = 0.05)

TF FOXJ3 (QBiC-SELEX coverage own_model), alt allele binds more; element distal enhancer-like cCRE EH38E1518342; gene LMO1; cell type neuroblastoma / SK-N-SH.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The alt A allele binds FOXJ3 more strongly than ref C. FOXJ3 is expressed and occupied at the variant in SK-N-SH, and QBiC-SELEX shows an alt-biased change, but the best model is a CIS-BP-mapped FOXG1 model, so the allele-specific binding evidence is weaker and not fully FOXJ3-specific. | missing | [E07](#e07), [E23](#e23) |
| element | The variant lies in a distal enhancer-like cCRE, so an allele-specific FOXJ3 site could modulate enhancer activity. | missing | [E03](#e03), [E04](#e04) |
| gene | The element is near LMO1, the best L2G gene, and alt A is associated with lower LMO1 expression in GTEx skeletal muscle; adrenal eQTL data are negative, so this is not confirmed in the most relevant tissue. | missing | [E02](#e02), [E16](#e16), [E17](#e17), [E37](#e37) |
| cell_type | FOXJ3 is expressed in SK-N-SH and has ChIP-seq occupancy over the variant. | missing | [E07](#e07) |
| phenotype | If FOXJ3 represses LMO1, stronger alt A binding would lower LMO1 and reduce neuroblastoma risk. There is no direct evidence that FOXJ3 represses LMO1, so this phenotype link is speculative. | missing | [E17](#e17), [E18g](#e18g) |

Predictions: Alt A increases FOXJ3 occupancy at the enhancer.; FOXJ3 depletion increases LMO1 expression in SK-N-SH if FOXJ3 is a repressor.; The alt A reporter effect is reversed by FOXJ3 knockdown if FOXJ3 mediates repression.

Falsified if: FOXJ3 depletion decreases rather than increases LMO1 expression.; Allele-specific FOXJ3 ChIP or reporter assays show no alt A effect.; FOXJ3 is not shown to repress LMO1 or enhancer activity in neuroblastoma cells.

## Prediction matrix

| Test | Cost | Separates top two | GATA2_ref_enhancer_LMO1 | null_no_tf_mediated_effect | GATA3_ref_enhancer_LMO1 | FOXJ3_alt_repressor_LMO1 |
| --- | --- | --- | --- | --- | --- | --- |
| Allele-specific enhancer reporter in SK-N-SH (C vs A) | medium | yes | Ref C reporter activity is higher than alt A in SK-N-SH. | No reproducible C vs A reporter difference. | Ref C reporter activity is higher than alt A in SK-N-SH. | Alt A may lower reporter activity if FOXJ3 represses, but the C/A difference could still exist. |
| Allele-specific GATA2 ChIP in a heterozygous SK-N-SH or reporter line | medium | yes | GATA2 occupancy is higher on ref C than alt A. | No reproducible allele-specific TF occupancy difference. | GATA3 occupancy may be higher on ref C; GATA2-specific signal may be weaker. | FOXJ3 occupancy is higher on alt A than ref C. |
| GATA2 CRISPRi/knockdown in SK-N-SH with LMO1 expression readout | medium | yes | GATA2 knockdown/CRISPRi reduces LMO1 expression. | No change in LMO1 expression. | Little or no LMO1 change, unless GATA3 compensates. | No change in LMO1 expression. |
| GATA3 CRISPRi/knockdown in SK-N-SH with LMO1 expression readout | medium | no | Little or no LMO1 change. | No change in LMO1 expression. | GATA3 knockdown reduces LMO1 expression. | No change in LMO1 expression. |
| Adrenal-gland eQTL lookup for rs2168101 and LMO1 | low | no | Alt A is associated with lower LMO1 in adrenal gland, supporting the gene-direction link but not GATA2 specificity. | No adrenal eQTL or a signal explained by linkage, not a base-specific TF effect. | Alt A is associated with lower LMO1 in adrenal gland, supporting the gene-direction link but not GATA3 specificity. | Alt A is associated with lower LMO1 in adrenal gland, supporting the gene-direction link but not FOXJ3 specificity. |

## Next experiment

Allele-specific enhancer reporter in SK-N-SH comparing ref C and alt A, with a GATA-motif-mutated control; if affordable, include allele-specific GATA2 ChIP in a heterozygous line to distinguish GATA2 from the null and from GATA3/FOXJ3.

## Investigate calls

- qbic_tf_detail({"tf": "GATA3"})
- literature_search({"query": "rs2168101 LMO1 GATA2 allele-specific enhancer reporter neuroblastoma"})
- eqtl_lookup({"tissue": "Adrenal Gland"})

## Flags

- quote_rejected: PMID 26560027: not an exact substring of the abstract

Citation support: 1.00 of links cite only evidence that passed every check.

## Evidence

<a id="e01"></a>**E01** variant_annotation, Ensembl VEP (GRCh38) (https://rest.ensembl.org/vep/human/region/11:8233861-8233861:1/A?content-type=application/json&Conservation=1; retrieved 2026-10-25T17:26:14+00:00)

> Variant chr11:8233861:C>A (GRCh38), allele string C/A
> Known IDs: rs2168101
> Most severe consequence: intron_variant
> Regulatory features: none
> GERP conservation score at the site: 6.43
> Transcript consequences: LMO1 (intron_variant); LMO1 (intron_variant, non_coding_transcript_variant)

<a id="e02"></a>**E02** nearest_genes, Ensembl overlap (protein_coding) (https://rest.ensembl.org/overlap/region/human/11:7233861-9233861?feature=gene;biotype=protein_coding;content-type=application/json; retrieved 2026-10-25T17:26:12+00:00)

> 25 protein-coding genes within 1000 kb of chr11:8233861:C>A, by distance to TSS:
> LMO1: 34.9 kb from TSS (in gene body, strand -1)
> RIC3: 64.8 kb from TSS (upstream, strand -1)
> TUB: 214.7 kb from TSS (downstream, strand +1)
> EIF3F: 263.6 kb from TSS (downstream, strand +1)
> NLRP10: 268.4 kb from TSS (upstream, strand -1)
> OR10A3: 292.2 kb from TSS (upstream, strand -1)
> OR10A6: 302.6 kb from TSS (upstream, strand -1)
> STK33: 360.4 kb from TSS (downstream, strand -1)
> OR5P3: 403.0 kb from TSS (upstream, strand -1)
> OR5P2: 436.9 kb from TSS (upstream, strand -1)

<a id="e03"></a>**E03** ccre_lookup, ENCODE v4 cCRE registry (ENCFF420VPZ) and SCREEN (https://screen-beta-api.wenglab.org/dataws/cre_table; retrieved 2026-10-25T17:25:50+00:00)

> The variant lies in cCRE EH38E1518342 (dELS: distal enhancer-like), chr11:8233740-8234086.
> SCREEN: 3 cCREs within 500 bp (max z-score across ENCODE biosamples):
> EH38E1518342 dELS (contains the variant): DNase z 4.5, H3K27ac z 4.0, H3K4me3 z 2.7, CTCF z 1.4; nearby genes LMO1, AC091013.1, RIC3
> EH38E1518343 dELS: DNase z 4.4, H3K27ac z 3.9, H3K4me3 z 2.9, CTCF z 1.6; nearby genes LMO1, AC091013.1, RIC3
> EH38E2943027 dELS: DNase z 2.8, H3K27ac z 4.0, H3K4me3 z 1.8, CTCF z 1.6; nearby genes LMO1, AC091013.1, RIC3
> Biosample-specific z-scores are not in this call; the values above are maxima over biosamples.

<a id="e04"></a>**E04** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> ENCODE TF ChIP-seq at chr11:8233861:C>A: 30 peaks contain the variant, from 22 factors in 6 biosamples. In the matching biosample SK-N-SH: 19 peaks from 15 factors. cCRE class at the variant: dELS. Bound factors outside the TF model collection (co-factors, Pol II, and TFs with no binding model; signs of an active element, not TF candidates): BNC2, EP300, MXI1, MYC, PRDM6, RCOR1, TOX2, TRIM28. Bound, expressed TFs with a binding model: 12; listed one per row: GATA2, GATA3, FOXJ3, TEAD4, MAX, YY1, GLIS3, BACH2, ZNF8, TSHZ2; also bound: NFIC, CEBPB. Bound but below 1 TPM: OSR2, SP7. Assayed with no peak here: 30 TFs in the matching biosample, 529 only elsewhere; never assayed: 536.

<a id="e05"></a>**E05** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> GATA2: bound here. 2 ENCODE ChIP-seq peak(s) contain the variant, in the matching biosample SK-N-SH; also in SH-SY5Y (e.g. ENCSR706VOO). 133.07 TPM in DepMap:ACH-000149 (SK-N-SH), rank 17 of 1626 TFs.

<a id="e06"></a>**E06** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> GATA3: bound here. 2 ENCODE ChIP-seq peak(s) contain the variant, in the matching biosample SK-N-SH; also in SH-SY5Y (e.g. ENCSR000BTH). 51.82 TPM in DepMap:ACH-000149 (SK-N-SH), rank 80 of 1626 TFs.

<a id="e07"></a>**E07** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> FOXJ3: bound here. 2 ENCODE ChIP-seq peak(s) contain the variant, in the matching biosample SK-N-SH (e.g. ENCSR667WDR). 26.62 TPM in DepMap:ACH-000149 (SK-N-SH), rank 196 of 1626 TFs.

<a id="e08"></a>**E08** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> TEAD4: bound here. 2 ENCODE ChIP-seq peak(s) contain the variant, in the matching biosample SK-N-SH (e.g. ENCSR000BUQ). 16.62 TPM in DepMap:ACH-000149 (SK-N-SH), rank 346 of 1626 TFs.

<a id="e09"></a>**E09** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> MAX: bound here. 1 ENCODE ChIP-seq peak(s) contain the variant, in the matching biosample SK-N-SH (e.g. ENCSR000BVD). 60.9 TPM in DepMap:ACH-000149 (SK-N-SH), rank 61 of 1626 TFs.

<a id="e10"></a>**E10** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> YY1: bound here. 1 ENCODE ChIP-seq peak(s) contain the variant, in the matching biosample SK-N-SH (e.g. ENCSR000BLZ). 43.79 TPM in DepMap:ACH-000149 (SK-N-SH), rank 102 of 1626 TFs.

<a id="e11"></a>**E11** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> GLIS3: bound here. 1 ENCODE ChIP-seq peak(s) contain the variant, in the matching biosample SK-N-SH (e.g. ENCSR507BWM). 7.84 TPM in DepMap:ACH-000149 (SK-N-SH), rank 629 of 1626 TFs.

<a id="e12"></a>**E12** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> BACH2: bound here. 1 ENCODE ChIP-seq peak(s) contain the variant, in the matching biosample SK-N-SH (e.g. ENCSR036THH). 3.54 TPM in DepMap:ACH-000149 (SK-N-SH), rank 907 of 1626 TFs.

<a id="e13"></a>**E13** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> ZNF8: bound here. 1 ENCODE ChIP-seq peak(s) contain the variant, in the matching biosample SK-N-SH (e.g. ENCSR325QLX). 2.18 TPM in DepMap:ACH-000149 (SK-N-SH), rank 1024 of 1626 TFs.

<a id="e14"></a>**E14** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> TSHZ2: bound here. 1 ENCODE ChIP-seq peak(s) contain the variant, in the matching biosample SK-N-SH (e.g. ENCSR282NLQ). 2.15 TPM in DepMap:ACH-000149 (SK-N-SH), rank 1028 of 1626 TFs.

<a id="e15"></a>**E15** gwas_lookup, GWAS Catalog REST v2 (https://www.ebi.ac.uk/gwas/rest/api/v2/associations?rs_id=rs2168101&size=100; retrieved 2026-10-25T17:26:22+00:00)

> 71 GWAS Catalog associations for rs2168101, strongest first:
> Glutamine levels: p 2.0e-208, effect allele A, risk-allele frequency NR, PMID 41044249
> Alanine levels: p 2.0e-151, effect allele A, risk-allele frequency NR, PMID 41044249
> Glycine levels: p 3.0e-43, effect allele A, risk-allele frequency NR, PMID 41044249
> Fasting blood glucose: p 2.0e-42, effect allele A, risk-allele frequency NR, PMID 40436827
> Tyrosine levels: p 2.0e-40, effect allele A, risk-allele frequency NR, PMID 41044249
> Height (maximum, inv-normal transformed): p 5.0e-37, effect allele C, risk-allele frequency 0.7115, PMID 39024449
> Glutamine levels (UKB data field 23461): p 4.0e-33, effect allele A, risk-allele frequency 0.308564, PMID 36764567
> height (mean, inv-normal transformed): p 9.0e-33, effect allele C, risk-allele frequency 0.7115, PMID 39024449
> Alanine levels (UKB data field 23460): p 7.0e-27, effect allele A, risk-allele frequency 0.308491, PMID 36764567
> height (minimum, inv-normal transformed): p 1.0e-24, effect allele C, risk-allele frequency 0.7115, PMID 39024449
> Albumin levels: p 2.0e-24, effect allele A, risk-allele frequency NR, PMID 40436827
> Histidine levels: p 5.0e-23, effect allele A, risk-allele frequency NR, PMID 41044249

<a id="e16"></a>**E16** finemap_lookup, Open Targets Platform (credible sets, L2G) (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-25T17:26:15+00:00)

> 158 credible sets contain 11_8233861_C_A: 157 GWAS, 1 molecular QTL.
> GWAS Height: PIP 1.00; L2G LMO1 0.70, RIC3 0.06
> GWAS Hemoglobin A1c levels: PIP 1.00; L2G LMO1 0.70, RIC3 0.06
> GWAS Tyrosine levels: PIP 1.00; L2G LMO1 0.70, RIC3 0.06
> GWAS Total concentration of branched-chain amino acids (leucine +: PIP 1.00; L2G LMO1 0.70, RIC3 0.06
> GWAS chloride  (minimum, inv-norm transformed): PIP 1.00; L2G LMO1 0.70, RIC3 0.06
> GWAS Diastolic blood pressure x short total sleep time interactio: PIP 1.00; L2G LMO1 0.70, RIC3 0.06
> pqtl for CFC1 (UKB_PPP_EUR_CFC1_P0CG37_OID21261_v1): PIP 1.00
> Best L2G gene scores across these sets: LMO1 0.92, RIC3 0.08

<a id="e17"></a>**E17** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr11_8233861_C_A_b38&datasetId=gtex_v8; retrieved 2026-10-26T00:40:54+00:00)

> 1 significant GTEx v8 single-tissue eQTLs for chr11_8233861_C_A_b38. NES is the effect of the alt allele (A) relative to ref (C).
> LMO1 in Muscle_Skeletal: NES -0.13, p 1.6e-09

<a id="e18"></a>**E18** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=rs2168101%20AND%20LMO1%20AND%20%22neuroblastoma%22&format=json&pageSize=8&resultType=core; retrieved 2026-10-25T17:26:22+00:00)

> Europe PMC: 51 hits for 'rs2168101 AND LMO1 AND "neuroblastoma"'; top 7 with PMIDs:
> PMID 41858882 (2026): LMO1 expression in neuroblastoma cells reprograms tumor-associated macrophages to promote metastasis.
> PMID 38937681 (2024): LMO family gene polymorphisms and Wilms tumor susceptibility in Chinese children: a five-center case-control study.
> PMID 40078563 (2025): Improving neuroblastoma risk prediction through a polygenic risk score derived from genome-wide association study-identified loci.
> PMID 37183825 (2023): Genetic predisposition to neuroblastoma results from a regulatory polymorphism that promotes the adrenergic cell state.
> PMID 40340897 (2025): Genetic variants of m&lt;sup&gt;1&lt;/sup&gt;A modification genes and the risk of neuroblastoma: novel insights from a Chinese case-control study.
> PMID 37183823 (2023): Back to the future: evolutionary biology reveals a key regulatory switch in neuroblastoma pathogenesis.
> PMID 37849756 (2023): Two bullets in the gun: combining immunotherapy with chemotherapy to defeat neuroblastoma by targeting adrenergic-mesenchymal plasticity.

<a id="e18a"></a>**E18a** literature_search, Europe PMC abstract, PMID 41858882 (https://europepmc.org/article/MED/41858882; retrieved 2026-10-25T17:26:22+00:00)

> To better understand this synergy, we performed single-cell RNA sequencing analysis on primary tumors from transgenic zebrafish overexpressing MYCN alone or with LMO1.

<a id="e18b"></a>**E18b** literature_search, Europe PMC abstract, PMID 41858882 (https://europepmc.org/article/MED/41858882; retrieved 2026-10-25T17:26:22+00:00)

> Our data suggest that LMO1 overexpression in MYCN-amplified NB cells increases the pro-metastatic properties of macrophages in the tumor-cell microenvironment, which is important for driving NB metastasis.

<a id="e18c"></a>**E18c** literature_search, Europe PMC abstract, PMID 38937681 (https://europepmc.org/article/MED/38937681; retrieved 2026-10-25T17:26:22+00:00)

> We found LMO1 rs2168101 G > T and rs11603024 C > T as well as LMO2 rs7933499 G > A were significantly associated with Wilms tumor risk.

<a id="e18d"></a>**E18d** literature_search, Europe PMC abstract, PMID 38937681 (https://europepmc.org/article/MED/38937681; retrieved 2026-10-25T17:26:22+00:00)

> Stratified analysis demonstrated a protective role of rs2168101 GT/TT genotypes against Wilms tumor in the subgroups of age ≤ 18 months, males and clinical stages I/II compared to the rs2168101 GG genotype.

<a id="e18e"></a>**E18e** literature_search, Europe PMC abstract, PMID 40078563 (https://europepmc.org/article/MED/40078563; retrieved 2026-10-25T17:26:22+00:00)

> Fourteen loci, including ten protective polymorphisms from CASC15, BARD1, LMO1, HSD17B12, and HACE1, and four risk variants from BARD1, RSRC1, CPZ and MMP20 were significantly associated with neuroblastoma risk.

<a id="e18f"></a>**E18f** literature_search, Europe PMC abstract, PMID 37183825 (https://europepmc.org/article/MED/37183825; retrieved 2026-10-25T17:26:22+00:00)

> Both LMO1 expression levels and the risk of developing neuroblastoma in children are associated with a single nucleotide polymorphism, G/T, that affects a GATA motif in the first intron of LMO1.

<a id="e18g"></a>**E18g** literature_search, Europe PMC abstract, PMID 37183825 (https://europepmc.org/article/MED/37183825; retrieved 2026-10-25T17:26:22+00:00)

> Here, we showed that WT zebrafish with the GATA genotype developed adrenergic neuroblastoma, while knock-in of the protective TATA allele at this locus reduced the penetrance of MYCN-driven tumors, which were restricted to the mesenchymal cell state.

<a id="e18h"></a>**E18h** literature_search, Europe PMC abstract, PMID 37183823 (https://europepmc.org/article/MED/37183823; retrieved 2026-10-25T17:26:22+00:00)

> They now demonstrate experimentally, using genome-edited zebrafish, that a polymorphism in the human rs2168101 locus of the LMO1 gene determines which CRC is active in a tumor.

<a id="e18i"></a>**E18i** literature_search, Europe PMC abstract, PMID 37183823 (https://europepmc.org/article/MED/37183823; retrieved 2026-10-25T17:26:22+00:00)

> The authors previously showed that overexpression of LIM-domain-only 1 (LMO1), a transcriptional coregulator, synergizes with MYCN to accelerate tumor formation and metastasis in an NBL-zebrafish model.

<a id="e19"></a>**E19** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> QBiC-SELEX screen of chr11:8233861:C>A, one line per TF, each with the TF's own or CIS-BP-mapped model of largest |z|. Candidates are TFs whose ENCODE ChIP-seq peaks contain the variant and that are expressed (DepMap line ACH-000149), bound here before bound elsewhere, then by |z|; then expressed TFs ENCODE never assayed whose best model passes the gate (occupancy unknown). Shown: 10 of 12 occupied, 5 of 115 with unknown occupancy. Left out: 30 TFs assayed in the matching biosample and 529 assayed only elsewhere, none with a peak here; 2 bound but below 1 TPM. The gate (|z| > 4.05, Bonferroni over 997 models) marks a change QBiC-SELEX detects; it says nothing about occupancy. Effect > 0 means the alternate allele binds more strongly. In vitro binding only.

<a id="e20"></a>**E20** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> GATA2 (GATA, 6 models; QBiC-SELEX coverage: own model): best model GATA2_eDBD_TATGCA40NGAG_KR_yin2017_1_3_7mer (its own model), z -56.07, effect -0.816: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 133.07 TPM, rank 17 of 1626 TFs in DepMap:ACH-000149 (SK-N-SH). Occupancy: bound here: ENCODE ChIP-seq peak over the variant in SK-N-SH, e.g. ENCSR706VOO. Best model's site strength: ref 100.0th, alt 77.3th percentile of its k-mer coefficients.

<a id="e21"></a>**E21** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> GATA3 (GATA, 6 models; QBiC-SELEX coverage: own model): best model GATA2_eDBD_TATGCA40NGAG_KR_yin2017_1_3_7mer (a CIS-BP-mapped model of GATA2), z -56.07, effect -0.816: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 51.82 TPM, rank 80 of 1626 TFs in DepMap:ACH-000149 (SK-N-SH). Occupancy: bound here: ENCODE ChIP-seq peak over the variant in SK-N-SH, e.g. ENCSR000BTH. Best model's site strength: ref 100.0th, alt 77.3th percentile of its k-mer coefficients.

<a id="e22"></a>**E22** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> ZNF8 (C2H2 ZF, 1 model; QBiC-SELEX coverage: own model): best model ZNF8_FL_TC40NACGGGA_AATA_jolma2025_0_2_7mer (its own model), z 16.02, effect 0.286: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 2.18 TPM, rank 1024 of 1626 TFs in DepMap:ACH-000149 (SK-N-SH). Occupancy: bound here: ENCODE ChIP-seq peak over the variant in SK-N-SH, e.g. ENCSR325QLX. Best model's site strength: ref 99.2th, alt 99.9th percentile of its k-mer coefficients.

<a id="e23"></a>**E23** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> FOXJ3 (Forkhead, 10 models; QBiC-SELEX coverage: own model): best model FOXG1_NA_TATCTG20NTCG_ESAF_yang2017_0_4_7mer (a CIS-BP-mapped model of FOXG1), z 14.24, effect 0.65: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 26.62 TPM, rank 196 of 1626 TFs in DepMap:ACH-000149 (SK-N-SH). Occupancy: bound here: ENCODE ChIP-seq peak over the variant in SK-N-SH, e.g. ENCSR667WDR. Best model's site strength: ref 54.8th, alt 99.0th percentile of its k-mer coefficients.

<a id="e24"></a>**E24** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> MAX (bHLH, 1 model; QBiC-SELEX coverage: own model): best model MAX_FL_TG40NGACCTT_YWN_jolma2025_0_3_7mer (its own model), z -4.96, effect -0.274: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 60.9 TPM, rank 61 of 1626 TFs in DepMap:ACH-000149 (SK-N-SH). Occupancy: bound here: ENCODE ChIP-seq peak over the variant in SK-N-SH, e.g. ENCSR000BVD. Best model's site strength: ref 47.4th, alt 46.1th percentile of its k-mer coefficients.

<a id="e25"></a>**E25** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> TEAD4 (TEA, 4 models; QBiC-SELEX coverage: own model): best model TEAD4_NA_TGATTT20NTTA_ESY_yang2017_0_4_7mer (its own model), z -4.85, effect -0.29: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 16.62 TPM, rank 346 of 1626 TFs in DepMap:ACH-000149 (SK-N-SH). Occupancy: bound here: ENCODE ChIP-seq peak over the variant in SK-N-SH, e.g. ENCSR000BUQ. Best model's site strength: ref 96.8th, alt 67.8th percentile of its k-mer coefficients.

<a id="e26"></a>**E26** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> YY1 (C2H2 ZF, 1 model; QBiC-SELEX coverage: own model): best model YY1_FL_GG40NGTGAGA_YWKA_jolma2025_0_3_7mer (its own model), z 3.73, effect 0.326: alt allele binds slightly more; occupied, no clear allelic change (|z| below the gate). 43.79 TPM, rank 102 of 1626 TFs in DepMap:ACH-000149 (SK-N-SH). Occupancy: bound here: ENCODE ChIP-seq peak over the variant in SK-N-SH, e.g. ENCSR000BLZ. Best model's site strength: ref 88.6th, alt 92.5th percentile of its k-mer coefficients.

<a id="e27"></a>**E27** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> BACH2 (bZIP, 1 model; QBiC-SELEX coverage: own model): best model BACH2_eDBD_TAGCAT40NAGG_KR_yin2017_0_3_7mer (its own model), z -2.45, effect -0.123: ref allele binds slightly more; occupied, no clear allelic change (|z| below the gate). 3.54 TPM, rank 907 of 1626 TFs in DepMap:ACH-000149 (SK-N-SH). Occupancy: bound here: ENCODE ChIP-seq peak over the variant in SK-N-SH, e.g. ENCSR036THH. Best model's site strength: ref 96.2th, alt 77.6th percentile of its k-mer coefficients.

<a id="e28"></a>**E28** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> GLIS3 (C2H2 ZF, 1 model; QBiC-SELEX coverage: own model): best model GLIS3_NA_TCGCAT20NGA_O_jolma2013_0_6_6mer (its own model), z 1.73, effect 0.715: alt allele binds slightly more; occupied, no clear allelic change (|z| below the gate). 7.84 TPM, rank 629 of 1626 TFs in DepMap:ACH-000149 (SK-N-SH). Occupancy: bound here: ENCODE ChIP-seq peak over the variant in SK-N-SH, e.g. ENCSR507BWM. Best model's site strength: ref 81.2th, alt 98.7th percentile of its k-mer coefficients.

<a id="e29"></a>**E29** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> TSHZ2 (C2H2 ZF, 1 model; QBiC-SELEX coverage: own model): best model TSHZ2_FL_AG40NGGAATC_YWL_jolma2025_0_4_7mer (its own model), z -0.28, effect -0.022: ref allele binds slightly more; occupied, no clear allelic change (|z| below the gate). 2.15 TPM, rank 1028 of 1626 TFs in DepMap:ACH-000149 (SK-N-SH). Occupancy: bound here: ENCODE ChIP-seq peak over the variant in SK-N-SH, e.g. ENCSR282NLQ. Best model's site strength: ref 86.8th, alt 79.7th percentile of its k-mer coefficients.

<a id="e30"></a>**E30** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> CPEB1 (Unknown, 1 model; QBiC-SELEX coverage: own model): best model CPEB1_NA_TAACCC20NCG_ESAC_yang2017_0_3_7mer (its own model), z 78.94, effect 3.719: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 4.79 TPM, rank 829 of 1626 TFs in DepMap:ACH-000149 (SK-N-SH). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 99.6th, alt 100.0th percentile of its k-mer coefficients.

<a id="e31"></a>**E31** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> HOXC9 (Homeodomain, 18 models; QBiC-SELEX coverage: own model): best model HOXC11_NA_TCACTA20NTCA_ESAC_yang2017_0_4_7mer (a CIS-BP-mapped model of HOXC11), z 40.23, effect 1.457: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 5.16 TPM, rank 797 of 1626 TFs in DepMap:ACH-000149 (SK-N-SH). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 92.0th, alt 99.7th percentile of its k-mer coefficients.

<a id="e32"></a>**E32** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> HOXD9 (Homeodomain, 18 models; QBiC-SELEX coverage: own model): best model HOXC11_NA_TCACTA20NTCA_ESAC_yang2017_0_4_7mer (a CIS-BP-mapped model of HOXC11), z 40.23, effect 1.457: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 7.58 TPM, rank 648 of 1626 TFs in DepMap:ACH-000149 (SK-N-SH). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 92.0th, alt 99.7th percentile of its k-mer coefficients.

<a id="e33"></a>**E33** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> ZBTB18 (C2H2 ZF, 1 model; QBiC-SELEX coverage: own model): best model ZBTB18_eDBD_TACTCC40NGTA_KR_yin2017_0_3_7mer (its own model), z -31.2, effect -2.791: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 17.06 TPM, rank 337 of 1626 TFs in DepMap:ACH-000149 (SK-N-SH). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 99.4th, alt 78.4th percentile of its k-mer coefficients.

<a id="e34"></a>**E34** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> HOXC5 (Homeodomain, 18 models; QBiC-SELEX coverage: mapped models only): best model HOXC9_FL_TATGTA40NTGT_KV_yin2017_1_2_7mer (a CIS-BP-mapped model of HOXC9), z 29.07, effect 0.472: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 3.65 TPM, rank 899 of 1626 TFs in DepMap:ACH-000149 (SK-N-SH). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 72.2th, alt 99.9th percentile of its k-mer coefficients.

<a id="e35"></a>**E35** qbic_tf_detail, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> {"tf":"GATA3","symbol":"GATA3","via":"hgnc_symbol","notes":[],"coverage":"own_model","variant":"chr11:8233861:C>A","gate_p":5.02e-05,"models":[{"model":"GATA3_NA_TGTCGT20NGA_ESAC_yang2017_0_4_7mer","mapping":"own","group":"G010 GATA, 6 models","quality":0.858,"effect":-4.206,"z":-54.11,"p":0.0,"rank_abs_z":"5/997","passed_gate":true,"site_strength":{"ref_percentile":99.9,"alt_percentile":97.4,"k":7}},{"model":"GATA1_eDBD_TTTAGA40NGGC_KN_yin2017_0_4_7mer","mapping":"CIS-BP (GATA1)","group":"G010 GATA, 6 models","quality":0.626,"effect":-5.572,"z":-49.7,"p":0.0,"rank_abs_z":"10/997","passed_gate":true,"site_strength":{"ref_percentile":99.3,"alt_percentile":78.7,"k":7}},{"model":"GATA2_eDBD_TATGCA40NGAG_KR_yin2017_1_3_7mer","mapping":"CIS-BP (GATA2)","group":"G010 GATA, 6 models","quality":0.874,"effect":-0.816,"z":-56.07,"p":0.0,"rank_abs_z":"4/997","passed_gate":true,"site_strength":{"ref_percentile":100.0,"alt_percentile":77.3,"k":7}},{"model":"GATA4_NA_TAAAAT20NAAA_Y_jolma2013_0_3_7mer","mapping":"CIS-BP (GATA4)","group":"G010 GATA, 6 models","quality":0.789,"effect":-3.553,"z":-38.66,"p":0.0,"rank_abs_z":"15/997","passed_gate":true,"site_strength":{"ref_percentile":99.9,"alt_percentile":98.5,"k":7}},{"model":"GATA5_NA_TAAATG20NTAA_ESY_yang2017_0_4_7mer","mapping":"CIS-BP (GATA5)","group":"G010 GATA, 6 models","quality":0.882,"effect":-3.915,"z":-52.75,"p":0.0,"rank_abs_z":"7/997","passed_gate":true,"site_strength":{"ref_percentile":99.5,"alt_percentile":99.5,"k":7}},{"model":"GATA6_eDBD_TCCATC40NTGA_KS_yin2017_0_3_7mer","mapping":"CIS-BP (GATA6)","group":"G010 GATA, 6 models","quality":0.937,"effect":-3.654,"z":-53.73,"p":0.0,"rank_abs_z":"6/997","passed_gate":true,"site_strength":{"ref_percentile":100.0,"alt_percentile":95.4,"k":7}}]}

<a id="e36"></a>**E36** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=rs2168101%20LMO1%20GATA2%20allele-specific%20enhancer%20reporter%20neuroblastoma&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T02:37:05+00:00)

> Europe PMC: 3 hits for 'rs2168101 LMO1 GATA2 allele-specific enhancer reporter neuroblastoma'; top 3 with PMIDs:
> PMID 38542080 (2024): Super-Enhancers and Their Parts: From Prediction Efforts to Pathognomonic Status.
> PMID 26560027 (2015): Genetic predisposition to neuroblastoma mediated by a LMO1 super-enhancer polymorphism.
> PMID 27807102 (2016): Emergence of the Noncoding Cancer Genome: A Target of Genetic and Epigenetic Alterations.

<a id="e37"></a>**E37** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr11_8233861_C_A_b38&datasetId=gtex_v8; retrieved 2026-10-26T00:40:54+00:00)

> 0 significant GTEx v8 single-tissue eQTLs for chr11_8233861_C_A_b38 in tissues matching 'Adrenal Gland'. NES is the effect of the alt allele (A) relative to ref (C).
