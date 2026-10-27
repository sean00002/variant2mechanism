# rs2168101 and Neuroblastoma (LMO1)

Configuration `full`, masked mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.03 over 7 model calls; 196 s.

Variant `chr11:8233861:C>A` (germline); expression context: DepMap:ACH-000149 (SK-N-SH).

## QBiC-SELEX screen (occupancy first)

Occupied candidates: GATA2 (bound here, z -56.07); GATA3 (bound here, z -56.07); ZNF8 (bound here, z 16.02); FOXJ3 (bound here, z 14.24); GLIS3 (bound here, z 1.73, no clear allelic change); MAX (bound here, z -4.96, weak site); TEAD4 (bound here, z -4.85, weak site); YY1 (bound here, z 3.73, no clear allelic change, weak site); BACH2 (bound here, z -2.45, no clear allelic change, weak site); TSHZ2 (bound here, z -0.28, no clear allelic change, weak site). Occupancy unknown: CPEB1 (z 78.94); HOXC9 (z 40.23); HOXD9 (z 40.23); ZBTB18 (z -31.2); HOXC5 (z 29.07). Diagnostic, not shown to the model: 334 of 997 models pass Bonferroni.

## Ranked chains

### 1. H1: GATA2 binds the reference allele more strongly at the LMO1 enhancer and activates LMO1 (p = 0.52)

TF GATA2 (QBiC-SELEX coverage own_model), ref allele binds more; element EH38E1518342 dELS (chr11:8233740-8234086); gene LMO1; cell type SK-N-SH neuroblastoma cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | GATA2 binds the reference C allele more strongly than the alt A allele. GATA2 has its own QBiC-SELEX model and is strongly expressed in SK-N-SH (133.07 TPM, rank 17/1626); ENCODE ChIP-seq shows GATA2 occupancy over the variant in SK-N-SH. Its own model gives effect -0.816 (z -56.07), with ref at the 100th and alt at the 77.3rd percentile, so the ref allele is the stronger GATA2 site. GATA3 shares the motif but is lower-expressed and has a weaker allele-specific drop at this base, so GATA2 is the better-supported GATA factor. | supported | [E20](#e20), [E05](#e05), [E04](#e04) |
| element | The variant lies in the active distal enhancer-like cCRE EH38E1518342, and GATA2 ChIP-seq occupies this element over the variant in SK-N-SH. | supported | [E03](#e03), [E05](#e05), [E20](#e20) |
| gene | The element is in the LMO1 gene body 34.9 kb from the LMO1 TSS; fine-mapping/L2G links this credible set to LMO1, and the alt A allele is associated with lower LMO1 expression in GTEx skeletal muscle (NES -0.13), consistent with weakening a ref-preferring activator. Caveat: the eQTL tissue is skeletal muscle and the L2G sets are not neuroblastoma. | supported | [E02](#e02), [E16](#e16), [E17](#e17) |
| cell_type | SK-N-SH is a neuroblastoma line in which this element is active, GATA2 is highly expressed, and GATA2 is bound over the variant, making the mechanism plausible in the relevant tumor-cell context. | supported | [E04](#e04), [E05](#e05), [E20](#e20) |
| phenotype | LMO1 is implicated in neuroblastoma biology and can promote aggressive/migratory phenotypes. If GATA2 activates LMO1 through this enhancer, the alt A allele would lower LMO1 and reduce LMO1-driven phenotypes. This direction is inferred, not directly shown: no supplied evidence ties this allele to neuroblastoma risk. | weak | [E18](#e18), [E18a](#e18a), [E36](#e36), [E17](#e17) |

Predictions: Allele-specific GATA2 ChIP or reporter assays show ref C > alt A at this base.; The alt A allele reduces enhancer activity and LMO1 expression in SK-N-SH or other neuroblastoma cells.; GATA2 depletion reduces LMO1 expression in SK-N-SH.

Falsified if: GATA2 occupancy over this base is not allele-specific.; The alt A allele does not reduce LMO1 enhancer activity or LMO1 expression in neuroblastoma cells.; The LMO1 effect is independent of GATA2, for example GATA2 depletion does not change LMO1.

### 2. H4: No TF-mediated allelic effect at this base; signal reflects a linked causal variant or non-TF mechanism (p = 0.30)

Null chain: no TF-mediated effect of this variant.

Predictions: No allele-specific transcription-factor binding at chr11:8233861 itself after controlling for linked variants.; The LMO1 eQTL/GWAS signal is driven by another variant in linkage disequilibrium, not by this base.; Enhancer activity and LMO1 expression are not allele-specific in neuroblastoma cells at this position.

Falsified if: Allele-specific GATA2 or another TF occupancy is demonstrated at this exact base.; Allele-specific enhancer activity and LMO1 expression are shown in SK-N-SH or other neuroblastoma cells.; A linked-variant explanation is excluded and this base directly changes TF binding.

### 3. H3: FOXJ3, via a paralog-mapped forkhead motif, binds the alt allele more strongly and may repress LMO1 (p = 0.10)

TF FOXJ3 (QBiC-SELEX coverage own_model), alt allele binds more; element EH38E1518342 dELS (chr11:8233740-8234086); gene LMO1; cell type SK-N-SH neuroblastoma cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | FOXJ3 is occupied over the variant in SK-N-SH and expressed there (26.62 TPM, rank 196/1626). The reported best QBiC-SELEX model is a CIS-BP-mapped FOXG1 model, not FOXJ3's own model, and it gives effect 0.65 (z 14.24), with alt at the 99.0th percentile: this supports alt-stronger binding only at paralog level. The allelic direction for FOXJ3 itself is therefore weaker than for GATA2. | weak | [E23](#e23), [E07](#e07), [E04](#e04) |
| element | The variant lies in the active dELS EH38E1518342, and FOXJ3 ChIP-seq occupies this element over the variant in SK-N-SH. | supported | [E03](#e03), [E07](#e07), [E23](#e23) |
| gene | The element is in the LMO1 gene body near LMO1; L2G/fine-mapping links the credible set to LMO1, and the alt allele is associated with lower LMO1 expression in GTEx skeletal muscle. This direction fits only if FOXJ3 represses LMO1, which is not established. | weak | [E02](#e02), [E16](#e16), [E17](#e17) |
| cell_type | FOXJ3 is expressed and bound at this active enhancer in SK-N-SH neuroblastoma cells. | supported | [E04](#e04), [E07](#e07), [E23](#e23) |
| phenotype | If FOXJ3 represses LMO1, the alt A allele's stronger FOXJ3 site would lower LMO1 and reduce LMO1-driven neuroblastoma phenotypes. The sign of FOXJ3 action and any allele-to-neuroblastoma link are missing from the supplied evidence, so this is an unproven inference. | weak | [E18](#e18), [E18a](#e18a), [E36](#e36) |

Predictions: Alt A increases FOXJ3 occupancy at this base in allele-specific ChIP or reporter assays.; FOXJ3 depletion reverses the alt-lower-LMO1 effect if FOXJ3 is the relevant repressor.; The alt allele changes LMO1 enhancer activity in a FOXJ3-site-dependent manner.

Falsified if: FOXJ3 binding is not allele-specific at this base.; The alt A allele does not increase FOXJ3 occupancy.; FOXJ3 depletion has no effect on LMO1 expression or on the allelic enhancer effect.

### 4. H2: GATA3, via its own GATA model, binds the reference allele more strongly and regulates LMO1 (p = 0.08)

TF GATA3 (QBiC-SELEX coverage own_model), ref allele binds more; element EH38E1518342 dELS (chr11:8233740-8234086); gene LMO1; cell type SK-N-SH neuroblastoma cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | GATA3 is occupied over the variant in SK-N-SH and expressed there (51.82 TPM, rank 80/1626). The GATA3 detail row provides its own GATA3 model in addition to the mapped GATA2 model: the own model gives effect -4.206 (z -54.11), with ref at the 99.9th and alt at the 97.4th percentile, so ref binds more strongly. The E21 'best model' line is a CIS-BP-mapped GATA2 model and is not independent GATA3 evidence; the own-model row is what supports this chain, but GATA2 remains better supported overall because of higher expression and the larger alt-site loss. | supported | [E35](#e35), [E06](#e06), [E04](#e04) |
| element | The variant lies in the active dELS EH38E1518342, and GATA3 ChIP-seq occupies this element over the variant in SK-N-SH. | supported | [E03](#e03), [E06](#e06) |
| gene | The element is in the LMO1 gene body near the LMO1 TSS; L2G/fine-mapping links the credible set to LMO1, and the alt A allele is associated with lower LMO1 expression in GTEx skeletal muscle, consistent with weakening a ref-preferring GATA activator. Caveat: the eQTL tissue is not neuroblastoma. | supported | [E02](#e02), [E16](#e16), [E17](#e17) |
| cell_type | GATA3 is expressed and bound at this active enhancer in SK-N-SH neuroblastoma cells. | supported | [E04](#e04), [E06](#e06), [E35](#e35) |
| phenotype | If GATA3 rather than GATA2 activates LMO1 at this element, the alt A allele would lower LMO1 and reduce LMO1-driven neuroblastoma phenotypes. The neuroblastoma-risk direction is not established by the supplied evidence. | weak | [E18](#e18), [E18a](#e18a), [E36](#e36), [E17](#e17) |

Predictions: GATA3-specific ChIP or reporter assays show ref C > alt A at this base.; GATA3 depletion reduces LMO1 expression in SK-N-SH, ideally more than GATA2 depletion.; The alt A allele lowers LMO1 enhancer activity in a GATA-motif-dependent manner.

Falsified if: GATA3 binding is not allele-specific at this base.; GATA2 depletion accounts for the LMO1 effect and GATA3 depletion does not.; The alt A allele does not alter LMO1 expression in neuroblastoma cells.

## Prediction matrix

| Test | Cost | Separates top two | H1 | H4 | H3 | H2 |
| --- | --- | --- | --- | --- | --- | --- |
| Allele-specific GATA2 ChIP-qPCR in SK-N-SH cells heterozygous at chr11:8233861 | medium | yes | Ref C shows stronger GATA2 occupancy than alt A at this base. | No allele-specific TF occupancy at this base. | No GATA2 allele effect; FOXJ3 may show alt > ref occupancy. | No GATA2 allele-specific occupancy; GATA3 may show the allele effect instead. |
| Enhancer MPRA or reporter assay with ref vs alt sequence in SK-N-SH | medium | yes | Ref C has higher enhancer activity; alt A lowers LMO1 reporter output. | No allelic difference in enhancer activity. | Alt A changes enhancer activity in a FOXJ3-site-dependent direction, lower if FOXJ3 represses. | Ref C has higher GATA-dependent enhancer activity, but the responsible factor is GATA3. |
| GATA2 knockdown in SK-N-SH followed by LMO1 qPCR | low | yes | LMO1 expression decreases. | No change in LMO1 expression. | No change in LMO1 expression. | Little or no LMO1 decrease; GATA3 depletion is more relevant. |
| FOXJ3 knockdown or overexpression in SK-N-SH with LMO1 expression and allelic reporter readout | medium | no | No FOXJ3-dependent change in LMO1 or the allelic enhancer effect. | No FOXJ3-dependent allelic effect at this base. | FOXJ3 loss changes LMO1 expression and/or reverses the alt-dependent enhancer effect. | No FOXJ3-dependent change in LMO1 or the allelic enhancer effect. |

## Next experiment

Allele-specific GATA2 ChIP-qPCR in SK-N-SH cells heterozygous at chr11:8233861, comparing ref C versus alt A occupancy; this is the cheapest direct test that separates H1 from the null H4.

## Investigate calls

- qbic_tf_detail({"tf": "GATA3"})
- gene_disease({"gene": "LMO1"})
- eqtl_lookup({"tissue": null})

## Flags

- none

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

<a id="e18"></a>**E18** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=LMO1%20AND%20%22neuroblastoma%22&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T20:19:16+00:00)

> Europe PMC: 396 hits for 'LMO1 AND "neuroblastoma"'; top 8 with PMIDs:
> PMID 41858882 (2026): LMO1 expression in neuroblastoma cells reprograms tumor-associated macrophages to promote metastasis.
> PMID 41630162 (2026): ARX mutation-associated interneuron defects provide insights into mechanisms underlying developmental epilepsies.
> PMID 42909156 (2026): The role of personalised medicine in treating high-risk neuroblastoma in paediatric patients.
> PMID 41960368 (2026): Cellular Functional Analyses of &lt;i&gt;ARX&lt;/i&gt; Variants Reveal New Insights Into Genotype-Phenotype Correlations in Neurodevelopmental Disorders Among Male and Female Patients.
> PMID 41202161 (2026): Defining the Functional Role and Potential as an Immunotherapeutic Target of ALCAM in Neuroblastoma.
> PMID 40078563 (2025): Improving neuroblastoma risk prediction through a polygenic risk score derived from genome-wide association study-identified loci.
> PMID 40076569 (2025): Prognostic Biomarkers in Breast Cancer via Multi-Omics Clustering Analysis.
> PMID 41982370 (2026): miRNA-Processing Gene Variants and Neuroblastoma Susceptibility: A Pilot Case-Control Study.

<a id="e18a"></a>**E18a** literature_search, Europe PMC abstract, PMID 41858882 (https://europepmc.org/article/MED/41858882; retrieved 2026-10-26T20:19:16+00:00)

> Conditioned media from LMO1-expressing NB cells activated PI3K-Akt signaling and MMP expression in human macrophages, enhancing matrix degradation and promoting NB cell migration in vivo.

<a id="e19"></a>**E19** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> QBiC-SELEX screen of chr11:8233861:C>A, one line per TF, each with the TF's own or CIS-BP-mapped model of largest |z|. Candidates are TFs whose ENCODE ChIP-seq peaks contain the variant and that are expressed (DepMap line ACH-000149), bound here before bound elsewhere, then a strong site before a weak one, then by |z|; then expressed TFs ENCODE never assayed whose best model passes the gate (occupancy unknown). Shown: 10 of 12 occupied (5 with a strong site), 5 of 115 with unknown occupancy. Left out: 30 TFs assayed in the matching biosample and 529 assayed only elsewhere, none with a peak here; 2 bound but below 1 TPM. The gate (|z| > 4.05, Bonferroni over 997 models) marks a change QBiC-SELEX detects; it says nothing about occupancy. Effect > 0 means the alternate allele binds more strongly. In vitro binding only. Site strength is the better allele's best k-mer over the variant, as a percentile of the best model's k-mers; a strong site reaches the 97.5th. At a weak site the ChIP peak more likely reflects another site in the element.

<a id="e20"></a>**E20** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> GATA2 (GATA, 6 models; QBiC-SELEX coverage: own model): best model GATA2_eDBD_TATGCA40NGAG_KR_yin2017_1_3_7mer (its own model), z -56.07, effect -0.816: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 133.07 TPM, rank 17 of 1626 TFs in DepMap:ACH-000149 (SK-N-SH). Occupancy: bound here: ENCODE ChIP-seq peak over the variant in SK-N-SH, e.g. ENCSR706VOO. Best model's site strength: ref 100.0th, alt 77.3th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e21"></a>**E21** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> GATA3 (GATA, 6 models; QBiC-SELEX coverage: own model): best model GATA2_eDBD_TATGCA40NGAG_KR_yin2017_1_3_7mer (a CIS-BP-mapped model of GATA2), z -56.07, effect -0.816: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 51.82 TPM, rank 80 of 1626 TFs in DepMap:ACH-000149 (SK-N-SH). Occupancy: bound here: ENCODE ChIP-seq peak over the variant in SK-N-SH, e.g. ENCSR000BTH. Best model's site strength: ref 100.0th, alt 77.3th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e22"></a>**E22** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> ZNF8 (C2H2 ZF, 1 model; QBiC-SELEX coverage: own model): best model ZNF8_FL_TC40NACGGGA_AATA_jolma2025_0_2_7mer (its own model), z 16.02, effect 0.286: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 2.18 TPM, rank 1024 of 1626 TFs in DepMap:ACH-000149 (SK-N-SH). Occupancy: bound here: ENCODE ChIP-seq peak over the variant in SK-N-SH, e.g. ENCSR325QLX. Best model's site strength: ref 99.2th, alt 99.9th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e23"></a>**E23** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> FOXJ3 (Forkhead, 10 models; QBiC-SELEX coverage: own model): best model FOXG1_NA_TATCTG20NTCG_ESAF_yang2017_0_4_7mer (a CIS-BP-mapped model of FOXG1), z 14.24, effect 0.65: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 26.62 TPM, rank 196 of 1626 TFs in DepMap:ACH-000149 (SK-N-SH). Occupancy: bound here: ENCODE ChIP-seq peak over the variant in SK-N-SH, e.g. ENCSR667WDR. Best model's site strength: ref 54.8th, alt 99.0th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e24"></a>**E24** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> GLIS3 (C2H2 ZF, 1 model; QBiC-SELEX coverage: own model): best model GLIS3_NA_TCGCAT20NGA_O_jolma2013_0_6_6mer (its own model), z 1.73, effect 0.715: alt allele binds slightly more; occupied, no clear allelic change (|z| below the gate). 7.84 TPM, rank 629 of 1626 TFs in DepMap:ACH-000149 (SK-N-SH). Occupancy: bound here: ENCODE ChIP-seq peak over the variant in SK-N-SH, e.g. ENCSR507BWM. Best model's site strength: ref 81.2th, alt 98.7th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e25"></a>**E25** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> MAX (bHLH, 1 model; QBiC-SELEX coverage: own model): best model MAX_FL_TG40NGACCTT_YWN_jolma2025_0_3_7mer (its own model), z -4.96, effect -0.274: ref allele binds more (|z| above the gate), but between weak k-mers. 60.9 TPM, rank 61 of 1626 TFs in DepMap:ACH-000149 (SK-N-SH). Occupancy: bound here: ENCODE ChIP-seq peak over the variant in SK-N-SH, e.g. ENCSR000BVD. Best model's site strength: ref 47.4th, alt 46.1th percentile of its k-mer coefficients: a weak site (neither allele reaches the 97.5th), so the ChIP peak more likely reflects another site in the element.

<a id="e26"></a>**E26** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> TEAD4 (TEA, 4 models; QBiC-SELEX coverage: own model): best model TEAD4_NA_TGATTT20NTTA_ESY_yang2017_0_4_7mer (its own model), z -4.85, effect -0.29: ref allele binds more (|z| above the gate), but between weak k-mers. 16.62 TPM, rank 346 of 1626 TFs in DepMap:ACH-000149 (SK-N-SH). Occupancy: bound here: ENCODE ChIP-seq peak over the variant in SK-N-SH, e.g. ENCSR000BUQ. Best model's site strength: ref 96.8th, alt 67.8th percentile of its k-mer coefficients: a weak site (neither allele reaches the 97.5th), so the ChIP peak more likely reflects another site in the element.

<a id="e27"></a>**E27** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> YY1 (C2H2 ZF, 1 model; QBiC-SELEX coverage: own model): best model YY1_FL_GG40NGTGAGA_YWKA_jolma2025_0_3_7mer (its own model), z 3.73, effect 0.326: alt allele binds slightly more; occupied, no clear allelic change (|z| below the gate). 43.79 TPM, rank 102 of 1626 TFs in DepMap:ACH-000149 (SK-N-SH). Occupancy: bound here: ENCODE ChIP-seq peak over the variant in SK-N-SH, e.g. ENCSR000BLZ. Best model's site strength: ref 88.6th, alt 92.5th percentile of its k-mer coefficients: a weak site (neither allele reaches the 97.5th), so the ChIP peak more likely reflects another site in the element.

<a id="e28"></a>**E28** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> BACH2 (bZIP, 1 model; QBiC-SELEX coverage: own model): best model BACH2_eDBD_TAGCAT40NAGG_KR_yin2017_0_3_7mer (its own model), z -2.45, effect -0.123: ref allele binds slightly more; occupied, no clear allelic change (|z| below the gate). 3.54 TPM, rank 907 of 1626 TFs in DepMap:ACH-000149 (SK-N-SH). Occupancy: bound here: ENCODE ChIP-seq peak over the variant in SK-N-SH, e.g. ENCSR036THH. Best model's site strength: ref 96.2th, alt 77.6th percentile of its k-mer coefficients: a weak site (neither allele reaches the 97.5th), so the ChIP peak more likely reflects another site in the element.

<a id="e29"></a>**E29** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> TSHZ2 (C2H2 ZF, 1 model; QBiC-SELEX coverage: own model): best model TSHZ2_FL_AG40NGGAATC_YWL_jolma2025_0_4_7mer (its own model), z -0.28, effect -0.022: ref allele binds slightly more; occupied, no clear allelic change (|z| below the gate). 2.15 TPM, rank 1028 of 1626 TFs in DepMap:ACH-000149 (SK-N-SH). Occupancy: bound here: ENCODE ChIP-seq peak over the variant in SK-N-SH, e.g. ENCSR282NLQ. Best model's site strength: ref 86.8th, alt 79.7th percentile of its k-mer coefficients: a weak site (neither allele reaches the 97.5th), so the ChIP peak more likely reflects another site in the element.

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

<a id="e36"></a>**E36** gene_disease, Open Targets Platform (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-26T02:28:30+00:00)

> Open Targets: LMO1 and neuroblastoma (MONDO_0005072), overall score 0.48; by evidence type: literature 0.91, genetic_association 0.74

<a id="e37"></a>**E37** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr11_8233861_C_A_b38&datasetId=gtex_v8; retrieved 2026-10-26T00:40:54+00:00)

> 1 significant GTEx v8 single-tissue eQTLs for chr11_8233861_C_A_b38. NES is the effect of the alt allele (A) relative to ref (C).
> LMO1 in Muscle_Skeletal: NES -0.13, p 1.6e-09
