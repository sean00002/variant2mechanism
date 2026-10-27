# rs2168101 and Neuroblastoma (LMO1)

Configuration `no_qbic`, masked mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.03 over 8 model calls; 239 s.

Variant `chr11:8233861:C>A` (germline); expression context: DepMap:ACH-000149 (SK-N-SH).

## Ranked chains

### 1. H4: No TF-mediated allelic effect at this exact base; signal reflects linked causal variant or locus context (p = 0.50)

Null chain: no TF-mediated effect of this variant.

Predictions: No reproducible allele-specific TF binding distinguishes ref C from alt A at this exact base.; The LMO1 association is driven by a linked causal variant or broader LMO1 locus context rather than this nucleotide.; The many ChIP peaks at the element reflect general active-element occupancy, not an allele-specific effect of C>A.

Falsified if: A robust allele-specific binding assay shows a clear ref/alt difference for a TF at this base.; CRISPR editing this exact nucleotide changes LMO1 enhancer activity or LMO1 expression in SK-N-SH.; Fine-mapping shows this base, rather than a linked variant, is causal.

### 2. H2: GATA3 binds the ref C allele at the LMO1 enhancer and sustains LMO1 expression (p = 0.40)

TF GATA3 (QBiC-SELEX coverage own_model), ref allele binds more; element EH38E1518342 dELS; gene LMO1; cell type SK-N-SH neuroblastoma.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | GATA3 is ChIP-bound at this element in SK-N-SH and expressed there (E06, E04). Locus literature shows that a protective low-LMO1 allele at the LMO1 super-enhancer ablates GATA3 binding (E19b), and the provided eQTL reports alt A with lower LMO1 (E17). I therefore infer that ref C preserves GATA3 binding more than alt A, but the published GATA3-ablating SNP is not this exact C>A and no QBiC-SELEX model or allele-specific assay for this base is given, so the direction is locus-level inference. | weak | [E04](#e04), [E06](#e06), [E17](#e17), [E19b](#e19b) |
| element | The variant sits in EH38E1518342, an active distal enhancer-like cCRE, and the locus is described as an LMO1 super-enhancer. | supported | [E03](#e03), [E04](#e04), [E19a](#e19a) |
| gene | LMO1 is the proximal gene and strongest L2G target. GTEx skeletal muscle shows alt A with lower LMO1 (NES -0.13), while Brain_Cortex has no significant eQTL in the provided data; this supports LMO1 as target but does not establish neuroblastoma-cell direction. | weak | [E02](#e02), [E16](#e16), [E17](#e17), [E20](#e20) |
| cell_type | GATA3 occupancy at this element is reported in the matched SK-N-SH neuroblastoma biosample. | supported | [E04](#e04), [E06](#e06) |
| phenotype | LMO1 is a neuroblastoma predisposition/oncogene candidate and LMO1-expressing neuroblastoma cells show pro-metastatic behavior. The provided GWAS credible sets are not neuroblastoma, so the exact-variant disease link remains indirect. | weak | [E18](#e18), [E18a](#e18a), [E21](#e21) |

Predictions: Allele-specific GATA3 ChIP, EMSA or MPRA in SK-N-SH shows ref C > alt A at the exact C>A base.; CRISPR editing C>A at the endogenous locus lowers LMO1 enhancer activity or LMO1 expression in SK-N-SH.; GATA3 knockdown reduces LMO1 expression/enhancer activity more than GATA2 knockdown.

Falsified if: Alt A binds GATA3 more strongly than ref C, or GATA3 binding is not allele-specific at this base.; GATA3 depletion does not reduce LMO1 expression or enhancer activity in SK-N-SH.; The C>A edit increases rather than decreases LMO1 expression in the neuroblastoma context.

### 3. H1: GATA2, rather than GATA3, binds the ref C allele and activates LMO1 (p = 0.10)

TF GATA2 (QBiC-SELEX coverage own_model), ref allele binds more; element EH38E1518342 dELS; gene LMO1; cell type SK-N-SH neuroblastoma.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | GATA2 is ChIP-bound at this element in SK-N-SH and is highly expressed there (E05, E04). GATA2 has no QBiC-SELEX model in the provided evidence, and there is no allele-specific GATA2 binding measurement. I infer that ref C binds GATA2 more strongly because the locus implicates a GATA motif, but this is a GATA-family inference, not direct GATA2 evidence. | weak | [E04](#e04), [E05](#e05) |
| element | The variant lies in EH38E1518342, a distal enhancer-like cCRE with DNase and H3K27ac signal, and multiple active-element factor ChIP peaks in SK-N-SH. | supported | [E03](#e03), [E04](#e04) |
| gene | The element is in the LMO1 gene body and LMO1 is the strongest L2G target. GTEx reports an LMO1 eQTL in skeletal muscle with alt A NES -0.13, but there is no Brain_Cortex eQTL in the provided data; the direction in neuroblastoma is not established. | weak | [E02](#e02), [E16](#e16), [E17](#e17), [E20](#e20) |
| cell_type | GATA2 occupancy at this element is reported in the matched SK-N-SH neuroblastoma biosample. | supported | [E04](#e04), [E05](#e05) |
| phenotype | LMO1 is a neuroblastoma-associated gene and LMO1-expressing neuroblastoma cells show pro-migratory/pro-invasive behavior. However, the exact variant lacks a provided neuroblastoma GWAS signal, so the phenotype link is indirect. | weak | [E18](#e18), [E18a](#e18a), [E21](#e21) |

Predictions: Allele-specific GATA2 ChIP or EMSA in SK-N-SH shows ref C > alt A at this base.; GATA2 knockdown reduces LMO1 enhancer activity or LMO1 expression in SK-N-SH, while GATA3 knockdown does not.; The alt A allele lowers LMO1 expression when GATA2 is present.

Falsified if: GATA2 binding is not allele-specific or alt A binds GATA2 more than ref C.; GATA2 depletion does not change LMO1 expression or enhancer activity in SK-N-SH.; GATA3, not GATA2, accounts for the allele-specific GATA-factor binding at this base.

## Prediction matrix

| Test | Cost | Separates top two | H4 | H2 | H1 |
| --- | --- | --- | --- | --- | --- |
| Re-analyze existing ENCODE GATA3 ChIP-seq raw reads from SK-N-SH for allele-specific read counts at chr11:8233861 C>A | existing data | yes | No reproducible allelic skew for GATA3. | Ref C shows more GATA3 ChIP reads than alt A at the exact base. | No GATA3 allelic skew; a GATA2 skew would be more consistent with H1. |
| Allele-specific GATA2 ChIP or EMSA at chr11:8233861 C>A in SK-N-SH | low | no | No allele-specific GATA2 binding. | No required GATA2 allelic skew; GATA3 is the predicted allele-specific factor. | Ref C binds GATA2 more than alt A. |
| GATA3 EMSA, allele-specific reporter, or MPRA with ref C versus alt A in a neuroblastoma context | low | yes | Equal GATA3 binding/activity for ref C and alt A. | Ref C shows stronger GATA3 binding and/or higher enhancer activity than alt A. | No GATA3 allele-specific effect; GATA2 may show ref>C. |
| CRISPR edit C>A at the endogenous locus and measure LMO1 enhancer activity/expression in SK-N-SH | medium | yes | No change in LMO1 enhancer activity/expression. | Alt A lowers LMO1 enhancer activity/expression. | Alt A lowers LMO1 if GATA2 is the activating factor. |
| GATA3 versus GATA2 knockdown/CRISPRi in SK-N-SH, measuring LMO1 expression | medium | yes | Neither GATA3 nor GATA2 loss changes LMO1. | GATA3 loss reduces LMO1; GATA2 loss has little effect. | GATA2 loss reduces LMO1; GATA3 loss has little effect. |

## Next experiment

Re-analyze existing ENCODE GATA3 ChIP-seq raw reads from SK-N-SH (E06) for allele-specific read counts at chr11:8233861 C>A. This is the cheapest test that directly separates H2 (ref C binds GATA3 more) from H4 (no allele-specific effect at this base).

## Investigate calls

- literature_search({"query": "LMO1 neuroblastoma enhancer GATA2 GATA3 allele-specific binding rs110419"})
- eqtl_lookup({"tissue": "Brain_Cortex"})
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

<a id="e19"></a>**E19** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=LMO1%20neuroblastoma%20enhancer%20GATA2%20GATA3%20allele-specific%20binding%20rs110419&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T20:21:33+00:00)

> Europe PMC: 1 hits for 'LMO1 neuroblastoma enhancer GATA2 GATA3 allele-specific binding rs[masked]'; top 1 with PMIDs:
> PMID 26560027 (2015): Genetic predisposition to neuroblastoma mediated by a LMO1 super-enhancer polymorphism.

<a id="e19a"></a>**E19a** literature_search, Europe PMC abstract, PMID 26560027 (https://europepmc.org/article/MED/26560027; retrieved 2026-10-26T20:21:33+00:00)

> We show that SNP rs[masked] G>T is the most highly associated variant (combined P = 7.47 × 10(-29), odds ratio 0.65, 95% confidence interval 0.60-0.70), and resides in a super-enhancer defined by extensive acetylation of histone H3 lysine 27 within the first intron of LMO1.

<a id="e19b"></a>**E19b** literature_search, Europe PMC abstract, PMID 26560027 (https://europepmc.org/article/MED/26560027; retrieved 2026-10-26T20:21:33+00:00)

> We show that the newly evolved protective TATA allele is associated with decreased total LMO1 expression (P = 0.028) in neuroblastoma primary tumours, and ablates GATA3 binding (P < 0.0001).

<a id="e20"></a>**E20** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr11_8233861_C_A_b38&datasetId=gtex_v8; retrieved 2026-10-26T00:40:54+00:00)

> 0 significant GTEx v8 single-tissue eQTLs for chr11_8233861_C_A_b38 in tissues matching 'Brain_Cortex'. NES is the effect of the alt allele (A) relative to ref (C).

<a id="e21"></a>**E21** gene_disease, Open Targets Platform (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-26T02:28:30+00:00)

> Open Targets: LMO1 and neuroblastoma (MONDO_0005072), overall score 0.48; by evidence type: literature 0.91, genetic_association 0.74
