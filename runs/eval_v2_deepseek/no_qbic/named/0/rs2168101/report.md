# rs2168101 and Neuroblastoma (LMO1)

Configuration `no_qbic`, named mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.02 over 8 model calls; 136 s.

Variant `chr11:8233861:C>A` (germline); expression context: DepMap:ACH-000149 (SK-N-SH).

## Ranked chains

### 1. H2_GATA3: GATA3 binds the ref GATA motif and activates LMO1 (p = 0.58)

TF GATA3 (QBiC-SELEX coverage own_model), ref allele binds more; element active distal enhancer-like cCRE EH38E1518342; gene LMO1; cell type SK-N-SH neuroblastoma / adrenergic-lineage cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | GATA3 binds the ref C allele more strongly than alt A. On the LMO1 minus strand, ref C corresponds to G and alt A to T; the ref allele preserves a GATA motif, while the protective alt allele creates a TATA-like sequence. GATA3 is chosen because it is occupied at the variant in SK-N-SH and the literature directly reports that the protective TATA allele ablates GATA3 binding. No QBiC-SELEX model/data for GATA3 is supplied in this evidence set. | weak | [E06](#e06), [E18f](#e18f), [E19b](#e19b) |
| element | rs2168101 lies in EH38E1518342, a distal enhancer-like cCRE with DNase and H3K27ac signal, consistent with an active regulatory element. | supported | [E03](#e03), [E04](#e04) |
| gene | The variant is in the LMO1 gene body 34.9 kb from the TSS; credible-set L2G maps the association best to LMO1, the GTEx eQTL reports lower LMO1 expression for alt A relative to ref C, and the protective TATA allele is associated with decreased total LMO1 expression in neuroblastoma primary tumours. | supported | [E02](#e02), [E16](#e16), [E17](#e17), [E19b](#e19b) |
| cell_type | GATA3 is occupied at this element in SK-N-SH neuroblastoma cells and is expressed there; GATA3 is also linked to neuroblastoma super-enhancer and adrenergic-lineage biology, supporting a cell-type-compatible route. | supported | [E06](#e06), [E19c](#e19c), [E18f](#e18f), [E18g](#e18g) |
| phenotype | The ref GATA allele is associated with higher LMO1 and increased adrenergic neuroblastoma risk, whereas the protective alt TATA allele ablates GATA3 binding, lowers LMO1 expression, and reduces MYCN-driven tumor penetrance in the zebrafish knock-in model. | supported | [E17](#e17), [E19a](#e19a), [E19b](#e19b), [E18g](#e18g), [E21](#e21) |

Predictions: Allele-specific GATA3 ChIP-qPCR shows preferential GATA3 occupancy on ref C over alt A in SK-N-SH.; GATA3 knockdown or CRISPRi reduces ref-allele enhancer activity and LMO1 expression more than alt-allele activity.; The protective alt A allele lowers LMO1 and enhancer activity in a GATA3-dependent manner.

Falsified if: Allele-specific GATA3 occupancy at rs2168101 is absent or opposite in SK-N-SH cells.; Editing ref C to alt A does not reduce enhancer activity or LMO1 expression in neuroblastoma cells.; Conditioning on nearby variants abolishes the LMO1/neuroblastoma signal at rs2168101.

### 2. H3_null: No TF-mediated allelic effect; linked causal variant or passenger (p = 0.28)

Null chain: no TF-mediated effect of this variant.

Predictions: No allele-specific TF binding at the rs2168101 base after controlling for linked variants.; No allele-specific enhancer activity attributable to rs2168101 itself.; The disease association is explained by a nearby causal variant or by a passenger change in an active element.

Falsified if: Allele-specific GATA3 occupancy and enhancer activity are demonstrated for rs2168101 itself.; Fine-mapping and conditioning show that rs2168101, not a linked variant, drives the LMO1 signal.

### 3. H1_GATA2: GATA2 binds the ref GATA motif as an alternative related factor and activates LMO1 (p = 0.14)

TF GATA2 (QBiC-SELEX coverage own_model), ref allele binds more; element active distal enhancer-like cCRE EH38E1518342; gene LMO1; cell type SK-N-SH neuroblastoma / adrenergic-lineage cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | GATA2 is an alternative GATA-family factor at this motif: it is occupied at the variant in SK-N-SH and the ref C allele preserves the GATA motif, so GATA2 is predicted to bind ref C more strongly than alt A. However, there is no QBiC-SELEX model/data for GATA2 in this evidence set, and no allele-specific GATA2 binding is shown; direct literature instead reports GATA3 binding ablation for the protective allele, making GATA2 the weaker competing factor. | weak | [E05](#e05), [E18f](#e18f), [E19b](#e19b) |
| element | rs2168101 lies in EH38E1518342, a distal enhancer-like cCRE with DNase and H3K27ac signal, consistent with an active regulatory element. | supported | [E03](#e03), [E04](#e04) |
| gene | The variant is in the LMO1 gene body 34.9 kb from the TSS; credible-set L2G maps the association best to LMO1, and the GTEx eQTL reports lower LMO1 expression for alt A relative to ref C, supporting allele-dependent LMO1 regulation. | supported | [E02](#e02), [E16](#e16), [E17](#e17) |
| cell_type | GATA2 is occupied at this element in SK-N-SH neuroblastoma cells and is highly expressed there; GATA2 is also reported in neuroblastoma differentiation TF waves, making this cell type plausible for a GATA2-mediated effect. | supported | [E05](#e05), [E19d](#e19d), [E18f](#e18f) |
| phenotype | If GATA2 were the functional factor, the ref GATA allele would be associated with higher LMO1 and increased adrenergic neuroblastoma risk, while the alt TATA allele would lower LMO1 and be protective. The GATA-family and locus-level literature supports this direction, but the evidence is not GATA2-specific. | weak | [E17](#e17), [E18f](#e18f), [E18g](#e18g), [E19a](#e19a) |

Predictions: Allele-specific GATA2 ChIP-qPCR shows preferential GATA2 occupancy on ref C over alt A in SK-N-SH.; GATA2 knockdown or CRISPRi reduces ref-allele enhancer activity and LMO1 expression more than alt-allele activity.; GATA2 occupancy at this element is stronger in adrenergic neuroblastoma cells than in non-neural cells.

Falsified if: Allele-specific GATA2 occupancy at rs2168101 is absent or opposite in SK-N-SH cells.; GATA2 knockdown does not affect ref-vs-alt enhancer activity or LMO1 expression.; GATA3, not GATA2, accounts for all allele-specific GATA-family occupancy and activity at this site.

## Prediction matrix

| Test | Cost | Separates top two | H2_GATA3 | H3_null | H1_GATA2 |
| --- | --- | --- | --- | --- | --- |
| Allele-specific GATA3 ChIP-qPCR in SK-N-SH | low | yes | Allele-specific GATA3 ChIP-qPCR in SK-N-SH shows stronger GATA3 occupancy on ref C than alt A. | No allele-specific TF binding at the rs2168101 base. | No or weak allele-specific GATA3 occupancy; if any GATA-family allelic binding is seen, GATA2 is the better candidate. |
| Allele-specific GATA2 ChIP-qPCR in SK-N-SH | low | no | No or weak allele-specific GATA2 occupancy; GATA3 is the main GATA-family factor. | No allele-specific TF binding at the rs2168101 base. | Allele-specific GATA2 ChIP-qPCR shows stronger GATA2 occupancy on ref C than alt A. |
| Allele-specific luciferase reporter comparing ref C and alt A enhancer sequences in SK-N-SH | low | yes | Alt A reduces enhancer activity in an allele-specific reporter in SK-N-SH. | No allele-specific enhancer activity difference between ref C and alt A. | Alt A reduces enhancer activity in an allele-specific reporter in SK-N-SH, but the effect should be GATA2-dependent. |
| Adrenal-gland / neuroblastoma LMO1 eQTL lookup | low | yes | Adrenal-gland or neuroblastoma-relevant eQTL shows alt A associated with lower LMO1. | No LMO1 eQTL in adrenal gland/neuroblastoma, or the signal is explained by a linked variant. | Adrenal-gland or neuroblastoma-relevant eQTL shows alt A associated with lower LMO1, but the effect is not GATA2-specific. |
| CRISPR/Cas9 edit ref C to alt A at the endogenous LMO1 locus in SK-N-SH, measure LMO1 expression and H3K27ac | high | yes | CRISPR editing ref C to alt A at the endogenous locus reduces LMO1 expression and enhancer activity in SK-N-SH. | No effect of the rs2168101 edit on LMO1 expression or enhancer activity after controlling for linked variants. | CRISPR editing ref C to alt A reduces LMO1 expression and enhancer activity, but the effect is rescued by GATA2, not GATA3. |
| GATA3 knockdown/CRISPRi in SK-N-SH with ref allele, measure LMO1 expression and enhancer activity | medium | yes | GATA3 knockdown/CRISPRi reduces ref-allele enhancer activity and LMO1 expression. | No allele-specific effect of GATA3 perturbation on enhancer activity or LMO1 expression. | GATA3 knockdown has little or no effect; GATA2 knockdown reduces ref-allele activity. |
| Fine-mapping and conditioning on linked variants at the LMO1 locus | medium | yes | rs2168101 remains the best causal candidate after conditioning on nearby variants. | The LMO1/neuroblastoma signal is explained by a linked variant, not rs2168101. | rs2168101 remains the best causal candidate after conditioning on nearby variants. |

## Next experiment

Allele-specific luciferase reporter in SK-N-SH comparing the ref C and alt A enhancer sequences is the single cheapest experiment that separates the top two chains H2_GATA3 and H3_null. H2_GATA3 predicts alt A reduces enhancer activity; H3_null predicts no allele-specific difference. If SK-N-SH cells are heterozygous at rs2168101, allele-specific GATA3 ChIP-qPCR would be an equally cheap direct binding test, but heterozygosity is not given in the evidence.

## Investigate calls

- literature_search({"query": "rs2168101 allele-specific GATA2 GATA3 binding LMO1 neuroblastoma"})
- eqtl_lookup({"tissue": "Adrenal Gland"})
- gene_disease({"gene": "LMO1"})

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

<a id="e19"></a>**E19** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=rs2168101%20allele-specific%20GATA2%20GATA3%20binding%20LMO1%20neuroblastoma&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T02:28:20+00:00)

> Europe PMC: 4 hits for 'rs2168101 allele-specific GATA2 GATA3 binding LMO1 neuroblastoma'; top 4 with PMIDs:
> PMID 38653778 (2024): Lineage specific transcription factor waves reprogram neuroblastoma from self-renewal to differentiation.
> PMID 38542080 (2024): Super-Enhancers and Their Parts: From Prediction Efforts to Pathognomonic Status.
> PMID 26560027 (2015): Genetic predisposition to neuroblastoma mediated by a LMO1 super-enhancer polymorphism.
> PMID 27807102 (2016): Emergence of the Noncoding Cancer Genome: A Target of Genetic and Epigenetic Alterations.

<a id="e19a"></a>**E19a** literature_search, Europe PMC abstract, PMID 26560027 (https://europepmc.org/article/MED/26560027; retrieved 2026-10-26T02:28:20+00:00)

> We show that SNP rs2168101 G>T is the most highly associated variant (combined P = 7.47 × 10(-29), odds ratio 0.65, 95% confidence interval 0.60-0.70), and resides in a super-enhancer defined by extensive acetylation of histone H3 lysine 27 within the first intron of LMO1.

<a id="e19b"></a>**E19b** literature_search, Europe PMC abstract, PMID 26560027 (https://europepmc.org/article/MED/26560027; retrieved 2026-10-26T02:28:20+00:00)

> We show that the newly evolved protective TATA allele is associated with decreased total LMO1 expression (P = 0.028) in neuroblastoma primary tumours, and ablates GATA3 binding (P < 0.0001).

<a id="e19c"></a>**E19c** literature_search, Europe PMC abstract, PMID 38653778 (https://europepmc.org/article/MED/38653778; retrieved 2026-10-26T02:28:20+00:00)

> SEs that decrease with ATRA link to stem cell development (MYCN, GATA3, SOX11).

<a id="e19d"></a>**E19d** literature_search, Europe PMC abstract, PMID 38653778 (https://europepmc.org/article/MED/38653778; retrieved 2026-10-26T02:28:20+00:00)

> Other TFs activate in sequential waves at 2, 4 and 8 days of ATRA treatment that regulate neural development (GATA2 and SOX4).

<a id="e20"></a>**E20** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr11_8233861_C_A_b38&datasetId=gtex_v8; retrieved 2026-10-26T00:40:54+00:00)

> 0 significant GTEx v8 single-tissue eQTLs for chr11_8233861_C_A_b38 in tissues matching 'Adrenal Gland'. NES is the effect of the alt allele (A) relative to ref (C).

<a id="e21"></a>**E21** gene_disease, Open Targets Platform (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-26T02:28:30+00:00)

> Open Targets: LMO1 and neuroblastoma (MONDO_0005072), overall score 0.48; by evidence type: literature 0.91, genetic_association 0.74
