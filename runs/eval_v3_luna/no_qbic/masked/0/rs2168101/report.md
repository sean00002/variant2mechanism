# rs2168101 and Neuroblastoma (LMO1)

Configuration `no_qbic`, masked mode, seed 0. Models: generator openai/gpt-6-luna, critic openai/gpt-6-luna, summariser openai/gpt-6-luna. Cost $0.01 over 8 model calls; 184 s.

Variant `chr11:8233861:C>A` (germline); expression context: DepMap:ACH-000149 (SK-N-SH).

## Ranked chains

### 1. H1: No TF-mediated effect of this variant (p = 0.86)

Null chain: no TF-mediated effect of this variant.

Predictions: The C>A substitution does not cause a material TF-mediated change in enhancer activity or LMO1 expression. Any disease association could reflect another cause or a non-causal association at this locus.

Falsified if: Isogenic allele editing reproducibly changes TF occupancy at this site and changes enhancer activity or LMO1 expression in a TF-dependent manner.

### 2. H2: Possible GATA2-mediated regulation of LMO1 (p = 0.06)

TF GATA2 (QBiC-SELEX coverage own_model), alt allele binds more; element The variant-containing distal enhancer-like cCRE EH38E1518342; gene LMO1; cell type SK-N-SH neuroblastoma cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | GATA2 occupies the variant site and is highly expressed in SK-N-SH, making it a candidate TF. The proposed direction is stronger binding to A, but this is an unsubstantiated hypothesis: no allele-specific QBiC-SELEX result or other evidence establishes whether C or A binds more strongly. GATA2 is weakly prioritized over the alternatives by its expression and occupancy, not by demonstrated allele-specific binding. | weak | [E04](#e04), [E05](#e05) |
| element | The variant lies in a distal enhancer-like cCRE. Its reported activity scores are maxima across biosamples, not SK-N-SH-specific evidence of enhancer activity. | supported | [E03](#e03) |
| gene | LMO1 is a plausible target because it is nearby and is the strongest Open Targets gene nomination at this variant, but direct regulation of LMO1 by this cCRE is not established. The A-associated decrease in LMO1 expression reported in skeletal muscle does not determine the effect in SK-N-SH. | weak | [E02](#e02), [E03](#e03), [E16](#e16), [E17](#e17) |
| cell_type | GATA2 occupancy at the site is reported in SK-N-SH, the expression-context cell line, although this does not show an allele-dependent effect. | supported | [E04](#e04), [E05](#e05) |
| phenotype | LMO1 has independent neuroblastoma disease and literature support, including reports connecting its overexpression to pro-metastatic properties. These data do not connect this variant or GATA2 to those effects; LMO1 is not a CRISPR dependency in SK-N-SH. | supported | [E18a](#e18a), [E18b](#e18b), [E18c](#e18c), [E20](#e20), [E21](#e21) |

Predictions: The working, unverified direction is greater GATA2 binding to A than C. The supplied evidence does not establish this direction.; If the variant acts through this chain, editing the allele will alter LMO1 expression in SK-N-SH, and that effect will depend on GATA2.

Falsified if: Sensitive allele-specific assays find no GATA2 binding difference at the site or find stronger binding to C.; Allele editing does not change LMO1 expression, or any expression effect persists unchanged when GATA2 is perturbed.

### 3. H3: Possible GATA3-mediated regulation of LMO1 (p = 0.05)

TF GATA3 (QBiC-SELEX coverage own_model), alt allele binds more; element The variant-containing distal enhancer-like cCRE EH38E1518342; gene LMO1; cell type SK-N-SH neuroblastoma cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | GATA3 occupies the variant site and is expressed in SK-N-SH. The proposed direction is stronger binding to A, but this is an unsubstantiated hypothesis: no allele-specific QBiC-SELEX result or other evidence establishes whether C or A binds more strongly. The evidence does not resolve GATA3 from the related candidate GATA2 as the relevant factor. | weak | [E04](#e04), [E06](#e06) |
| element | The variant lies in a distal enhancer-like cCRE, but the reported activity scores are maxima across biosamples rather than SK-N-SH-specific measurements. | supported | [E03](#e03) |
| gene | LMO1 is a plausible target based on proximity and its strong variant-level gene nomination, but direct regulation by this cCRE is not demonstrated. The skeletal-muscle eQTL does not establish the direction in SK-N-SH. | weak | [E02](#e02), [E03](#e03), [E16](#e16), [E17](#e17) |
| cell_type | GATA3 occupancy at the site is reported in SK-N-SH, but occupancy does not establish an allele-dependent effect. | supported | [E04](#e04), [E06](#e06) |
| phenotype | LMO1 is linked to neuroblastoma by disease-association and literature evidence, including reports about overexpression and pro-metastatic properties. No supplied evidence connects this variant or GATA3 to those effects; LMO1 is not a CRISPR dependency in SK-N-SH. | supported | [E18a](#e18a), [E18b](#e18b), [E18c](#e18c), [E20](#e20), [E21](#e21) |

Predictions: The working, unverified direction is greater GATA3 binding to A than C. The supplied evidence does not establish this direction.; If this chain is correct, allele editing will alter LMO1 expression in SK-N-SH, and that effect will depend on GATA3 rather than GATA2 or TEAD4.

Falsified if: Sensitive allele-specific assays find no GATA3 binding difference at the site or find stronger binding to C.; Allele editing does not change LMO1 expression, or any expression effect persists unchanged when GATA3 is perturbed.

### 4. H4: Possible TEAD4-mediated regulation of LMO1 (p = 0.03)

TF TEAD4 (QBiC-SELEX coverage own_model), alt allele binds more; element The variant-containing distal enhancer-like cCRE EH38E1518342; gene LMO1; cell type SK-N-SH neuroblastoma cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | TEAD4 occupies the variant site and is expressed in SK-N-SH. The proposed direction is stronger binding to A, but this is an unsubstantiated hypothesis: no allele-specific QBiC-SELEX result or other evidence establishes whether C or A binds more strongly. | weak | [E04](#e04), [E08](#e08) |
| element | The variant lies in a distal enhancer-like cCRE, but its reported activity scores are maxima across biosamples rather than measurements specific to SK-N-SH. | supported | [E03](#e03) |
| gene | LMO1 is a plausible target based on proximity and the variant-level gene nomination, but the supplied evidence does not establish that this cCRE regulates LMO1. The skeletal-muscle eQTL does not determine the effect in SK-N-SH. | weak | [E02](#e02), [E03](#e03), [E16](#e16), [E17](#e17) |
| cell_type | TEAD4 occupancy at the site is reported in SK-N-SH, but this does not establish allele-specific binding or activity. | supported | [E04](#e04), [E08](#e08) |
| phenotype | LMO1 has independent neuroblastoma disease and literature support, but the evidence does not connect this variant or TEAD4 to LMO1 expression or disease effects. LMO1 is not a CRISPR dependency in SK-N-SH. | supported | [E18a](#e18a), [E18b](#e18b), [E18c](#e18c), [E20](#e20), [E21](#e21) |

Predictions: The working, unverified direction is greater TEAD4 binding to A than C. The supplied evidence does not establish this direction.; If this chain is correct, allele editing will alter LMO1 expression in SK-N-SH, and that effect will depend on TEAD4 rather than GATA2 or GATA3.

Falsified if: Sensitive allele-specific assays find no TEAD4 binding difference at the site or find stronger binding to C.; Allele editing does not change LMO1 expression, or any expression effect persists unchanged when TEAD4 is perturbed.

## Prediction matrix

| Test | Cost | Separates top two | H1 | H2 | H3 | H4 |
| --- | --- | --- | --- | --- | --- | --- |
| Compare C- and A-containing site oligonucleotides in SK-N-SH nuclear extract by EMSA, with TF-specific supershift or antibody disruption for GATA2, GATA3, and TEAD4. | low | yes | No reproducible allele-dependent shift attributable to one of the proposed TFs. | A reproducible C/A binding difference attributable to GATA2; the chain's working direction predicts stronger binding to A. | A reproducible C/A binding difference attributable to GATA3; the chain's working direction predicts stronger binding to A. | A reproducible C/A binding difference attributable to TEAD4; the chain's working direction predicts stronger binding to A. |
| Use isogenic SK-N-SH cells edited C-to-A and A-to-C; measure allele-dependent TF occupancy at the site and LMO1 expression, with separate perturbation of GATA2, GATA3, and TEAD4. | high | no | No reproducible allele-dependent occupancy and LMO1 expression effect attributable to these TFs. | An allele-dependent GATA2 occupancy difference accompanies an LMO1 expression change that is reduced by GATA2 perturbation. | An allele-dependent GATA3 occupancy difference accompanies an LMO1 expression change that is reduced by GATA3 perturbation. | An allele-dependent TEAD4 occupancy difference accompanies an LMO1 expression change that is reduced by TEAD4 perturbation. |
| Test whether the variant-containing cCRE regulates LMO1 using targeted CRISPRi of the cCRE and measure LMO1 expression in SK-N-SH. | medium | no | No reproducible effect of cCRE perturbation on LMO1 expression. | The cCRE perturbation changes LMO1 expression; this test alone does not establish GATA2 mediation or an allele effect. | The cCRE perturbation changes LMO1 expression; this test alone does not establish GATA3 mediation or an allele effect. | The cCRE perturbation changes LMO1 expression; this test alone does not establish TEAD4 mediation or an allele effect. |

## Next experiment

Start with the low-cost EMSA using C- and A-containing oligonucleotides and SK-N-SH nuclear extract, with TF-specific supershift or antibody disruption. A reproducible GATA2-attributable allelic difference would support H2 over the top-ranked null; the working prediction is stronger binding to A, but the supplied evidence does not establish that direction. No difference would weaken H2, though a negative in-vitro result would not rule out a chromatin-dependent effect.

## Investigate calls

- literature_search({"query": "chr11:8233861 LMO1 neuroblastoma variant enhancer allele-specific expression"})
- gene_disease({"gene": "LMO1"})
- gene_dependency({"gene": "LMO1"})

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

> To better understand this synergy, we performed single-cell RNA sequencing analysis on primary tumors from transgenic zebrafish overexpressing MYCN alone or with LMO1.

<a id="e18b"></a>**E18b** literature_search, Europe PMC abstract, PMID 41858882 (https://europepmc.org/article/MED/41858882; retrieved 2026-10-26T20:19:16+00:00)

> Our data suggest that LMO1 overexpression in MYCN-amplified NB cells increases the pro-metastatic properties of macrophages in the tumor-cell microenvironment, which is important for driving NB metastasis.

<a id="e18c"></a>**E18c** literature_search, Europe PMC abstract, PMID 40078563 (https://europepmc.org/article/MED/40078563; retrieved 2026-10-26T20:19:16+00:00)

> Fourteen loci, including ten protective polymorphisms from CASC15, BARD1, LMO1, HSD17B12, and HACE1, and four risk variants from BARD1, RSRC1, CPZ and MMP20 were significantly associated with neuroblastoma risk.

<a id="e19"></a>**E19** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=chr11%3A8233861%20LMO1%20neuroblastoma%20variant%20enhancer%20allele-specific%20expression&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T20:20:23+00:00)

> Europe PMC: 0 hits for 'chr11:8233861 LMO1 neuroblastoma variant enhancer allele-specific expression'; top 0 with PMIDs:

<a id="e20"></a>**E20** gene_disease, Open Targets Platform (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-26T02:28:30+00:00)

> Open Targets: LMO1 and neuroblastoma (MONDO_0005072), overall score 0.48; by evidence type: literature 0.91, genetic_association 0.74

<a id="e21"></a>**E21** gene_dependency, DepMap CRISPRGeneEffect (Biomni copy) and CRISPRInferredCommonEssentials (Public 26Q3) (local files; retrieved local)

> DepMap CRISPR gene effect for LMO1 (0 = no effect, -1 = median common-essential; < -0.5 called dependent). SK-N-SH (ACH-000149): -0.04. Peripheral Nervous System lineage, 45 lines: median 0.01, 0% dependent. All 1183 lines: median 0.04, 0% dependent.
