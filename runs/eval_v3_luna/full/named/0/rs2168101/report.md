# rs2168101 and Neuroblastoma (LMO1)

Configuration `full`, named mode, seed 0. Models: generator openai/gpt-6-luna, critic openai/gpt-6-luna, summariser openai/gpt-6-luna. Cost $0.01 over 8 model calls; 133 s.

Variant `chr11:8233861:C>A` (germline); expression context: DepMap:ACH-000149 (SK-N-SH).

## QBiC-SELEX screen (occupancy first)

Occupied candidates: GATA2 (bound here, z -56.07); GATA3 (bound here, z -56.07); ZNF8 (bound here, z 16.02); FOXJ3 (bound here, z 14.24); GLIS3 (bound here, z 1.73, no clear allelic change); MAX (bound here, z -4.96, weak site); TEAD4 (bound here, z -4.85, weak site); YY1 (bound here, z 3.73, no clear allelic change, weak site); BACH2 (bound here, z -2.45, no clear allelic change, weak site); TSHZ2 (bound here, z -0.28, no clear allelic change, weak site). Occupancy unknown: CPEB1 (z 78.94); HOXC9 (z 40.23); HOXD9 (z 40.23); ZBTB18 (z -31.2); HOXC5 (z 29.07). Diagnostic, not shown to the model: 334 of 997 models pass Bonferroni.

## Ranked chains

### 1. H1: GATA2 binding at the ref allele contributes to LMO1 regulation (p = 0.50)

TF GATA2 (QBiC-SELEX coverage own_model), ref allele binds more; element The variant lies in a candidate distal enhancer-like element.; gene LMO1; cell type SK-N-SH neuroblastoma cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | GATA2 is the leading candidate: it is strongly expressed and ChIP-bound over the variant in SK-N-SH, and its own QBiC-SELEX model predicts stronger binding to ref C than alt A. GATA3 is also occupied and has a significant ref-favoring result in its own model, but is less expressed; binding evidence alone does not establish which factor mediates the regulatory effect. | supported | [E04](#e04), [E05](#e05), [E06](#e06), [E20](#e20), [E35](#e35) |
| element | The variant is inside cCRE EH38E1518342, annotated as distal enhancer-like; the reported chromatin scores are maxima across biosamples, not evidence of enhancer activity in SK-N-SH. | supported | [E03](#e03) |
| gene | LMO1 is the favored target, based on the intronic location, gene-link scores favoring LMO1 over RIC3, and literature connecting the intronic GATA motif to LMO1 expression; regulation of LMO1 by this particular cCRE is not established. | supported | [E01](#e01), [E02](#e02), [E16](#e16), [E18d](#e18d), [E36a](#e36a) |
| cell_type | GATA2 occupancy and high expression are documented in SK-N-SH, while the locus has been implicated in the adrenergic neuroblastoma cell state; the full proposed mechanism has not been demonstrated in that state. | supported | [E05](#e05), [E18d](#e18d), [E18e](#e18e), [E36a](#e36a), [E36b](#e36b) |
| phenotype | This model predicts that stronger GATA2 binding on ref C supports LMO1 regulation associated with neuroblastoma susceptibility, with alt A corresponding to the protective allele direction reported for the complementary T allele; GATA2-specific mediation and the binding-to-expression direction remain unproven. | weak | [E18d](#e18d), [E18e](#e18e), [E36a](#e36a), [E36b](#e36b), [E37](#e37) |

Predictions: GATA2-specific depletion should reduce the variant-dependent LMO1 regulatory output more than GATA3-specific depletion does.; In a relevant neuroblastoma context, ref C should show stronger GATA2 binding than alt A, and precise C-to-A editing should alter LMO1 regulation in the predicted direction.

Falsified if: GATA2-specific depletion leaves the allele-dependent LMO1 output unchanged while GATA3-specific depletion removes it.; Precise editing and allele-aware assays show no reproducible GATA2-dependent difference in occupancy or LMO1 regulation.

### 2. H2: GATA3 binding at the ref allele contributes to LMO1 regulation (p = 0.28)

TF GATA3 (QBiC-SELEX coverage own_model), ref allele binds more; element The variant lies in a candidate distal enhancer-like element.; gene LMO1; cell type SK-N-SH neuroblastoma cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | GATA3 is an occupied, expressed candidate in SK-N-SH, and its own QBiC-SELEX model predicts stronger binding to ref C than alt A; a separate GATA2-mapped model gives the same direction. GATA2 remains a competing candidate because it is more highly expressed and also has strong own-model evidence. | supported | [E04](#e04), [E06](#e06), [E21](#e21), [E35](#e35) |
| element | The variant is inside cCRE EH38E1518342, annotated as distal enhancer-like; the reported chromatin scores are maxima across biosamples, not evidence of enhancer activity in SK-N-SH. | supported | [E03](#e03) |
| gene | LMO1 is the favored target, based on the intronic location, gene-link scores favoring LMO1 over RIC3, and literature connecting the intronic GATA motif to LMO1 expression; regulation of LMO1 by this particular cCRE is not established. | supported | [E01](#e01), [E02](#e02), [E16](#e16), [E18d](#e18d), [E36a](#e36a) |
| cell_type | GATA3 occupancy and expression are documented in SK-N-SH, and the locus has been implicated in the adrenergic neuroblastoma cell state; GATA3-specific action in that state has not been demonstrated. | supported | [E06](#e06), [E18d](#e18d), [E18e](#e18e), [E36a](#e36a), [E36b](#e36b) |
| phenotype | This model predicts that stronger GATA3 binding on ref C contributes to LMO1 regulation associated with neuroblastoma susceptibility, with alt A corresponding to the protective allele direction reported for the complementary T allele; GATA3-specific mediation and the binding-to-expression direction remain unproven. | weak | [E18d](#e18d), [E18e](#e18e), [E36a](#e36a), [E36b](#e36b), [E37](#e37) |

Predictions: GATA3-specific depletion should reduce the variant-dependent LMO1 regulatory output more than GATA2-specific depletion does.; Allele-aware assays should show stronger GATA3 binding on ref C than alt A, and precise C-to-A editing should alter LMO1 regulation in the predicted direction.

Falsified if: GATA3-specific depletion leaves the allele-dependent LMO1 output unchanged while GATA2-specific depletion removes it.; Precise editing and allele-aware assays show no reproducible GATA3-dependent difference in occupancy or LMO1 regulation.

### 3. H3: No TF-mediated effect of rs2168101 (p = 0.22)

Null chain: no TF-mediated effect of this variant.

Predictions: The variant may be a marker of another causal change, or the predicted in-vitro binding differences may not cause a regulatory effect in cells.; Precise editing of rs2168101 alone should not reproducibly change LMO1 regulation or a neuroblastoma-relevant phenotype.

Falsified if: Precise editing of rs2168101 reproducibly changes TF-dependent LMO1 regulation and a neuroblastoma-relevant phenotype in an allele-dependent manner.

## Prediction matrix

| Test | Cost | Separates top two | H1 | H2 | H3 |
| --- | --- | --- | --- | --- | --- |
| Parallel GATA2-specific and GATA3-specific depletion in SK-N-SH, measuring allele-dependent LMO1 RNA or enhancer output | medium | yes | GATA2 depletion preferentially removes the allele-dependent LMO1 output; GATA3 depletion has a smaller effect. | GATA3 depletion preferentially removes the allele-dependent LMO1 output; GATA2 depletion has a smaller effect. | Neither depletion reproducibly removes a variant-dependent LMO1 output. |
| Allele-aware GATA2 and GATA3 occupancy assay at rs2168101 in heterozygous neuroblastoma cells | medium | yes | Ref C is preferentially occupied by GATA2; this would support, but not prove, GATA2 mediation. | Ref C is preferentially occupied by GATA3; this would support, but not prove, GATA3 mediation. | No reproducible allele-specific occupancy is detected for either factor. |
| Precise C-to-A editing followed by measurement of LMO1 expression and neuroblastoma-relevant cell-state output | high | yes | Editing changes LMO1 output in the predicted direction, with the change dependent on GATA2. | Editing changes LMO1 output in the predicted direction, with the change dependent on GATA3. | Editing alone produces no reproducible change in LMO1 output or relevant cell-state output. |

## Next experiment

The cheapest direct discriminator is a parallel, factor-specific GATA2 versus GATA3 depletion experiment in SK-N-SH, measuring allele-dependent LMO1 RNA or enhancer output. A preferential loss after GATA2 depletion favors H1; after GATA3 depletion favors H2. Include non-targeting controls and verify depletion of each factor.

## Investigate calls

- qbic_tf_detail({"tf": "GATA3"})
- literature_search({"query": "rs2168101 neuroblastoma GATA allele-specific LMO1 expression binding"})
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

> Our data suggest that LMO1 overexpression in MYCN-amplified NB cells increases the pro-metastatic properties of macrophages in the tumor-cell microenvironment, which is important for driving NB metastasis.

<a id="e18b"></a>**E18b** literature_search, Europe PMC abstract, PMID 38937681 (https://europepmc.org/article/MED/38937681; retrieved 2026-10-25T17:26:22+00:00)

> We found LMO1 rs2168101 G > T and rs11603024 C > T as well as LMO2 rs7933499 G > A were significantly associated with Wilms tumor risk.

<a id="e18c"></a>**E18c** literature_search, Europe PMC abstract, PMID 40078563 (https://europepmc.org/article/MED/40078563; retrieved 2026-10-25T17:26:22+00:00)

> Fourteen loci, including ten protective polymorphisms from CASC15, BARD1, LMO1, HSD17B12, and HACE1, and four risk variants from BARD1, RSRC1, CPZ and MMP20 were significantly associated with neuroblastoma risk.

<a id="e18d"></a>**E18d** literature_search, Europe PMC abstract, PMID 37183825 (https://europepmc.org/article/MED/37183825; retrieved 2026-10-25T17:26:22+00:00)

> Both LMO1 expression levels and the risk of developing neuroblastoma in children are associated with a single nucleotide polymorphism, G/T, that affects a GATA motif in the first intron of LMO1.

<a id="e18e"></a>**E18e** literature_search, Europe PMC abstract, PMID 37183825 (https://europepmc.org/article/MED/37183825; retrieved 2026-10-25T17:26:22+00:00)

> Here, we showed that WT zebrafish with the GATA genotype developed adrenergic neuroblastoma, while knock-in of the protective TATA allele at this locus reduced the penetrance of MYCN-driven tumors, which were restricted to the mesenchymal cell state.

<a id="e18f"></a>**E18f** literature_search, Europe PMC abstract, PMID 37183823 (https://europepmc.org/article/MED/37183823; retrieved 2026-10-25T17:26:22+00:00)

> They now demonstrate experimentally, using genome-edited zebrafish, that a polymorphism in the human rs2168101 locus of the LMO1 gene determines which CRC is active in a tumor.

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

<a id="e36"></a>**E36** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=rs2168101%20neuroblastoma%20GATA%20allele-specific%20LMO1%20expression%20binding&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T13:33:35+00:00)

> Europe PMC: 18 hits for 'rs2168101 neuroblastoma GATA allele-specific LMO1 expression binding'; top 8 with PMIDs:
> PMID 37183825 (2023): Genetic predisposition to neuroblastoma results from a regulatory polymorphism that promotes the adrenergic cell state.
> PMID 37183823 (2023): Back to the future: evolutionary biology reveals a key regulatory switch in neuroblastoma pathogenesis.
> PMID 37849756 (2023): Two bullets in the gun: combining immunotherapy with chemotherapy to defeat neuroblastoma by targeting adrenergic-mesenchymal plasticity.
> PMID 38653778 (2024): Lineage specific transcription factor waves reprogram neuroblastoma from self-renewal to differentiation.
> PMID 38902506 (2024): Hidden secrets of the cancer genome: unlocking the impact of non-coding mutations in gene regulatory elements.
> PMID 38587919 (2024): Super-enhancers: drivers of cells' identities and cells' debacles.
> PMID 33870932 (2021): LIM domain only 1: an oncogenic transcription cofactor contributing to the tumorigenesis of multiple cancer types.
> PMID 38542080 (2024): Super-Enhancers and Their Parts: From Prediction Efforts to Pathognomonic Status.

<a id="e36a"></a>**E36a** literature_search, Europe PMC abstract, PMID 37183825 (https://europepmc.org/article/MED/37183825; retrieved 2026-10-26T13:33:35+00:00)

> Both LMO1 expression levels and the risk of developing neuroblastoma in children are associated with a single nucleotide polymorphism, G/T, that affects a GATA motif in the first intron of LMO1.

<a id="e36b"></a>**E36b** literature_search, Europe PMC abstract, PMID 37183825 (https://europepmc.org/article/MED/37183825; retrieved 2026-10-26T13:33:35+00:00)

> Thus, conversion of the regulatory GATA to a TATA allele in the first intron of LMO1 reduced the neuroblastoma-initiation rate by preventing formation of the adrenergic cell state.

<a id="e36c"></a>**E36c** literature_search, Europe PMC abstract, PMID 37183823 (https://europepmc.org/article/MED/37183823; retrieved 2026-10-26T13:33:35+00:00)

> They now demonstrate experimentally, using genome-edited zebrafish, that a polymorphism in the human rs2168101 locus of the LMO1 gene determines which CRC is active in a tumor.

<a id="e37"></a>**E37** gene_disease, Open Targets Platform (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-26T02:28:30+00:00)

> Open Targets: LMO1 and neuroblastoma (MONDO_0005072), overall score 0.48; by evidence type: literature 0.91, genetic_association 0.74
