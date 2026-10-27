# rs2168101 and Neuroblastoma (LMO1)

Configuration `no_qbic`, named mode, seed 0. Models: generator openai/gpt-6-luna, critic openai/gpt-6-luna, summariser openai/gpt-6-luna. Cost $0.01 over 7 model calls; 152 s.

Variant `chr11:8233861:C>A` (germline); expression context: DepMap:ACH-000149 (SK-N-SH).

## Ranked chains

### 1. H1: GATA2 mediates the allele-sensitive LMO1 regulatory effect (p = 0.38)

TF GATA2 (QBiC-SELEX coverage own_model), ref allele binds more; element Enhancer-like cCRE EH38E1518342; gene LMO1; cell type Adrenergic neuroblastoma cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | GATA2 is a leading candidate because it occupies the variant in SK-N-SH and is highly expressed there. The literature describes an allele-sensitive GATA motif: ref C corresponds to G on the complementary strand and alt A to T, changing GATA to TATA. Thus stronger ref binding is plausible, but not directly measured for GATA2; no allele-specific QBiC-SELEX result is provided, and the literature does not distinguish GATA2 from GATA3. | weak | [E04](#e04), [E05](#e05), [E18d](#e18d), [E18e](#e18e), [E19](#e19) |
| element | The variant lies in enhancer-like cCRE EH38E1518342, which has enhancer-associated chromatin marks; the reported maxima are not specific to SK-N-SH. | supported | [E03](#e03) |
| gene | LMO1 is the leading candidate target because the variant is intronic to it and LMO1 has the strongest reported gene-link scores, but direct regulation of LMO1 by this cCRE is not shown. The skeletal-muscle eQTL is not neuroblastoma evidence, and no Brain-Cortex eQTL was reported. | weak | [E01](#e01), [E02](#e02), [E16](#e16), [E17](#e17), [E21](#e21) |
| cell_type | The proposed context is adrenergic neuroblastoma: GATA2 occupancy is observed in SK-N-SH, while the literature connects the locus genotype with adrenergic versus mesenchymal tumor states; GATA2-specific mediation in that state is not established. | weak | [E04](#e04), [E05](#e05), [E18d](#e18d), [E18e](#e18e) |
| phenotype | The ref-associated GATA motif is consistent with greater neuroblastoma susceptibility than alt: the cited zebrafish result reports reduced tumor penetrance for the protective TATA allele, which corresponds to alt A. This supports an allele-to-phenotype connection but does not establish GATA2 mediation. | supported | [E18d](#e18d), [E18e](#e18e), [E20](#e20) |

Predictions: In relevant cells, GATA2 occupancy should be greater on ref C than alt A.; Selective GATA2 depletion should reduce the allele-dependent LMO1 regulatory difference more than selective GATA3 depletion.

Falsified if: A suitable allele-specific assay shows no greater GATA2 binding on ref, or shows greater binding on alt.; GATA2 depletion leaves the allele-dependent LMO1 response unchanged while GATA3 depletion removes it.

### 2. H2: GATA3 rather than GATA2 mediates the allele-sensitive LMO1 regulatory effect (p = 0.33)

TF GATA3 (QBiC-SELEX coverage own_model), ref allele binds more; element Enhancer-like cCRE EH38E1518342; gene LMO1; cell type Adrenergic neuroblastoma cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | GATA3 occupies the variant in SK-N-SH, making it a plausible mediator of the reported GATA-motif change. Ref C corresponds to G on the complementary strand and alt A to T, changing GATA to TATA; stronger ref binding is plausible but not directly measured for GATA3. No allele-specific QBiC-SELEX result is provided, and the literature does not distinguish GATA3 from GATA2. | weak | [E04](#e04), [E06](#e06), [E18d](#e18d), [E18e](#e18e), [E19](#e19) |
| element | The variant lies in enhancer-like cCRE EH38E1518342, which has enhancer-associated chromatin marks; the reported maxima are not specific to SK-N-SH. | supported | [E03](#e03) |
| gene | LMO1 is the leading candidate target because the variant is intronic to it and LMO1 has the strongest reported gene-link scores, but direct regulation of LMO1 by this cCRE is not shown. The skeletal-muscle eQTL is not neuroblastoma evidence, and no Brain-Cortex eQTL was reported. | weak | [E01](#e01), [E02](#e02), [E16](#e16), [E17](#e17), [E21](#e21) |
| cell_type | The proposed context is adrenergic neuroblastoma: GATA3 occupancy is observed in SK-N-SH, and the literature connects the locus genotype with tumor cell state, but GATA3-specific mediation in adrenergic cells is not established. | weak | [E04](#e04), [E06](#e06), [E18d](#e18d), [E18e](#e18e) |
| phenotype | A GATA3-mediated effect would be consistent with the reported lower tumor penetrance of the protective TATA allele corresponding to alt A, but the phenotype evidence does not attribute that effect specifically to GATA3. | weak | [E18d](#e18d), [E18e](#e18e), [E20](#e20) |

Predictions: In relevant cells, GATA3 occupancy should be greater on ref C than alt A.; Selective GATA3 depletion should reduce the allele-dependent LMO1 regulatory difference more than selective GATA2 depletion.

Falsified if: A suitable allele-specific assay shows no greater GATA3 binding on ref, or shows greater binding on alt.; GATA3 depletion leaves the allele-dependent LMO1 response unchanged while GATA2 depletion removes it.

### 3. H3: No TF-mediated effect of this variant (p = 0.29)

Null chain: no TF-mediated effect of this variant.

Predictions: The observed occupancy and motif annotation may not produce a variant-dependent TF effect; the association may instead reflect a linked causal change or another mechanism.; Factor-specific depletion should not reveal a reproducible allele-dependent LMO1 response attributable to GATA2 or GATA3.

Falsified if: A reproducible allele-dependent GATA2- or GATA3-mediated change in LMO1 regulation is demonstrated in relevant neuroblastoma cells.

## Prediction matrix

| Test | Cost | Separates top two | H1 | H2 | H3 |
| --- | --- | --- | --- | --- | --- |
| In SK-N-SH cells, compare allele-paired enhancer reporter activity after selective GATA2 or GATA3 depletion. | medium | yes | The ref-versus-alt reporter difference is reduced more by GATA2 depletion than by GATA3 depletion. | The ref-versus-alt reporter difference is reduced more by GATA3 depletion than by GATA2 depletion. | No reproducible allele-dependent reporter difference, or no selective effect of either depletion on such a difference. |
| Measure allele-specific GATA2 and GATA3 occupancy at the endogenous site in heterozygous SK-N-SH cells. | medium | no | GATA2 occupancy favors ref C; this assay alone need not show that GATA2 is the functional mediator. | GATA3 occupancy favors ref C; this assay alone need not show that GATA3 is the functional mediator. | No reproducible allele-specific occupancy difference for the proposed mediator. |
| Perturb cCRE EH38E1518342 and measure endogenous LMO1 expression in an appropriate neuroblastoma model. | high | no | Perturbing the element changes LMO1 expression; this alone does not identify GATA2 as the mediator. | Perturbing the element changes LMO1 expression; this alone does not identify GATA3 as the mediator. | No reproducible LMO1 response attributable to this element and variant. |

## Next experiment

Run the allele-paired enhancer reporter in SK-N-SH cells with selective GATA2 versus GATA3 depletion, measuring the ref-versus-alt activity difference. This is the cheapest proposed test that distinguishes the two leading TF-specific chains.

## Investigate calls

- literature_search({"query": "PMID 37183825 rs2168101 GATA2 GATA3 allele-specific binding reporter assay"})
- gene_disease({"gene": "LMO1"})
- eqtl_lookup({"tissue": "Brain - Cortex"})

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

<a id="e19"></a>**E19** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=PMID%2037183825%20rs2168101%20GATA2%20GATA3%20allele-specific%20binding%20reporter%20assay&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T13:25:18+00:00)

> Europe PMC: 0 hits for 'PMID 37183825 rs2168101 GATA2 GATA3 allele-specific binding reporter assay'; top 0 with PMIDs:

<a id="e20"></a>**E20** gene_disease, Open Targets Platform (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-26T02:28:30+00:00)

> Open Targets: LMO1 and neuroblastoma (MONDO_0005072), overall score 0.48; by evidence type: literature 0.91, genetic_association 0.74

<a id="e21"></a>**E21** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr11_8233861_C_A_b38&datasetId=gtex_v8; retrieved 2026-10-26T00:40:54+00:00)

> 0 significant GTEx v8 single-tissue eQTLs for chr11_8233861_C_A_b38 in tissues matching 'Brain - Cortex'. NES is the effect of the alt allele (A) relative to ref (C).
