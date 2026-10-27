# rs642961 and Cleft lip (IRF6)

Configuration `no_qbic`, named mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.02 over 9 model calls; 114 s.

Variant `chr1:209815925:A>G` (germline); expression context: none.

## Ranked chains

### 1. H01: Null Hypothesis: rs642961 is a linked/passenger variant not mediating a TF-dependent regulatory effect. (p = 0.40)

Null chain: no TF-mediated effect of this variant.

Predictions: The rs642961 variant does not alter the binding of any known transcription factor at the ENSR1_B3JM9C enhancer.

Falsified if: A specific TF binding event is identified at the enhancer linked to the rs642961 locus.

### 2. H02: Enhancer regulatory mechanism acting on IRF6 development via ETS1. (p = 0.35)

TF ETS1 (stated coverage not_in_coverage; registry own_model), ref allele binds more; element ENSR1_B3JM9C enhancer; gene IRF6; cell type Developmental/Craniofacial.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The reference allele (A) favors binding of ETS1 to the ENSR1_B3JM9C enhancer. | missing | none |
| element | The variant rs642961 resides within the ENSR1_B3JM9C enhancer. | supported | [E01](#e01), [E03](#e03) |
| gene | The ENSR1_B3JM9C enhancer regulates IRF6 expression. | weak | [E02](#e02), [E05](#e05), [E06](#e06) |
| cell_type | The functional consequence occurs in developmental/craniofacial cells, consistent with IRF6 function in cleft lip. | missing | [E03](#e03), [E06](#e06) |
| phenotype | The risk allele (A) increases expression of IRF6, leading to the orofacial cleft phenotype. | weak | [E04](#e04), [E09b](#e09b) |

Predictions: The reference allele (A) increases binding of ETS1, leading to enhanced IRF6 expression, which is critical for proper craniofacial development.; The risk allele (A) maintains or increases binding, leading to the orofacial cleft phenotype.

Falsified if: Binding of ETS1 is unaffected by the A>G change, or IRF6 expression levels are not significantly altered/increased by the A allele.

### 3. H03: Enhancer regulatory mechanism acting on UTP25 via PAX3. (p = 0.20)

TF PAX3 (stated coverage not_checked; registry own_model), ref allele binds more; element ENSR1_B3JM9C enhancer; gene UTP25; cell type Developmental/Craniofacial.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The reference allele (A) favors binding of PAX3 to the enhancer element. | missing | none |
| element | The variant rs642961 resides within the ENSR1_B3JM9C enhancer. | supported | [E01](#e01), [E03](#e03) |
| gene | The ENSR1_B3JM9C enhancer regulates UTP25 expression. | weak | [E02](#e02), [E05](#e05) |
| cell_type | The functional consequence occurs in developmental/craniofacial cells. | missing | [E03](#e03), [E06](#e06) |
| phenotype | Altered UTP25 expression due to the A allele contributes to the risk of orofacial cleft. | weak | [E04](#e04), [E05](#e05) |

Predictions: The risk allele (A) alters PAX3 binding, leading to dysregulated UTP25 expression, which contributes to orofacial cleft risk.

Falsified if: UTP25 expression levels are not significantly altered between ref and alt alleles, or PAX3 binding is unaffected.

### 4. H04: Linkage Disequilibrium/Indirect Effect via a novel factor. (p = 0.05)

TF Unknown_Transcription_Factor (stated coverage not_checked; registry unknown_name), ref allele binds more; element ENSR1_B3JM9C enhancer; gene None; cell type None.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The reference allele (A) increases binding affinity for a specific factor at the enhancer region. | missing | [E01](#e01), [E03](#e03) |
| element | The variant rs642961 resides within the ENSR1_B3JM9C enhancer. | supported | [E01](#e01), [E03](#e03) |
| gene | The ENSR1_B3JM9C enhancer modulates expression of a key developmental gene linked to pleiotropic traits. | missing | [E04](#e04) |
| cell_type | The effect manifests in cells related to the pleiotropy observed in related traits (developmental/vascular). | missing | [E04](#e04) |
| phenotype | The functional impact associated with the reference allele contributes to the risk of orofacial cleft. | weak | [E04](#e04) |

Predictions: Mutating rs642961 to the G allele should diminish the risk associated with the binding event at this enhancer.

Falsified if: The functional impact persists even when the binding event is genetically decoupled from the rs642961 locus.

## Prediction matrix

| Test | Cost | Separates top two | H01 | H02 | H03 | H04 |
| --- | --- | --- | --- | --- | --- | --- |
| chip_peaks({"tf":"ETS1"}) | medium | yes |  | Test confirms ETS1 occupies the enhancer |  |  |
| chip_peaks({"tf":"PAX3"}) | low | yes |  |  | Test confirms PAX3 occupies the enhancer |  |
| literature_search({"query":"rs642961 IRF6 allele-specific reporter MPRA"}) | high | no |  | Test identifies allele-specific functional regulation of IRF6 |  |  |

## Next experiment

chip_peaks({"tf":"PAX3"})

## Investigate calls

- chip_peaks({"biosample": null, "tf": "TRIB1"})
- chip_peaks({"biosample": null, "tf": "PAX3"})
- literature_search({"query": "rs642961 UTP25 IRF6 enhancer regulation functional variant"})

## Flags

- coverage_misstated: H02: stated not_in_coverage, registry says own_model for ETS1

Citation support: 0.87 of links cite only evidence that passed every check.

## Evidence

<a id="e01"></a>**E01** variant_annotation, Ensembl VEP (GRCh38) (https://rest.ensembl.org/vep/human/region/1:209815925-209815925:1/G?content-type=application/json&Conservation=1; retrieved 2026-10-25T17:29:41+00:00)

> Variant chr1:209815925:A>G (GRCh38), allele string A/G
> Known IDs: rs642961
> Most severe consequence: regulatory_region_variant
> Regulatory features: ENSR1_B3JM9C enhancer
> GERP conservation score at the site: 0.516
> Transcript consequences: none (intergenic)

<a id="e02"></a>**E02** nearest_genes, Ensembl overlap (protein_coding) (https://rest.ensembl.org/overlap/region/human/1:208815925-210815925?feature=gene;biotype=protein_coding;content-type=application/json; retrieved 2026-10-25T17:29:25+00:00)

> 13 protein-coding genes within 1000 kb of chr1:209815925:A>G, by distance to TSS:
> IRF6: 9.7 kb from TSS (upstream, strand -1)
> ENSG00000289700: 9.7 kb from TSS (upstream, strand -1)
> UTP25: 12.0 kb from TSS (upstream, strand +1)
> C1orf74: 31.3 kb from TSS (upstream, strand -1)
> TRAF3IP3: 60.4 kb from TSS (downstream, strand +1)
> SYT14: 85.0 kb from TSS (upstream, strand +1)
> HSD11B1: 129.8 kb from TSS (downstream, strand +1)
> G0S2: 140.5 kb from TSS (downstream, strand +1)
> LAMB3: 162.8 kb from TSS (upstream, strand -1)
> CAMK1G: 232.2 kb from TSS (downstream, strand +1)

<a id="e03"></a>**E03** ccre_lookup, ENCODE v4 cCRE registry (ENCFF420VPZ) and SCREEN (https://screen-beta-api.wenglab.org/dataws/cre_table; retrieved 2026-10-25T17:29:16+00:00)

> The variant lies in cCRE EH38E2863563 (dELS: distal enhancer-like), chr1:209815915-209816264.
> SCREEN: 2 cCREs within 500 bp (max z-score across ENCODE biosamples):
> EH38E2863563 dELS (contains the variant): DNase z 5.3, H3K27ac z 5.0, H3K4me3 z 2.4, CTCF z 1.5; nearby genes IRF6, UTP25, C1orf74
> EH38E2863562 dELS: DNase z 3.2, H3K27ac z 4.9, H3K4me3 z 1.9, CTCF z 1.5; nearby genes IRF6, UTP25, C1orf74
> Biosample-specific z-scores are not in this call; the values above are maxima over biosamples.

<a id="e04"></a>**E04** gwas_lookup, GWAS Catalog REST v2 (https://www.ebi.ac.uk/gwas/rest/api/v2/associations?rs_id=rs642961&size=100; retrieved 2026-10-25T17:29:42+00:00)

> 8 GWAS Catalog associations for rs642961, strongest first:
> Systolic blood pressure: p 6.0e-12, effect allele G, risk-allele frequency NR, PMID 38689001
> Hypertension: p 2.0e-08, effect allele A, risk-allele frequency 0.1951, PMID 33230300
> Pulse pressure: p 1.0e-07, effect allele G, risk-allele frequency NR, PMID 38689001
> Diastolic blood pressure: p 3.0e-07, effect allele G, risk-allele frequency NR, PMID 38689001
> Orofacial clefts: p 2.0e-06, effect allele A, risk-allele frequency NR, PMID 19270707

<a id="e05"></a>**E05** finemap_lookup, Open Targets Platform (credible sets, L2G) (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-25T17:29:41+00:00)

> 18 credible sets contain 1_209815925_A_G: 14 GWAS, 4 molecular QTL.
> GWAS Systolic blood pressure: PIP 0.10; L2G TRAF3IP3 0.11, IRF6 0.11, UTP25 0.10
> GWAS Systolic blood pressure: PIP 0.09; L2G IRF6 0.67, UTP25 0.14, TRAF3IP3 0.08
> GWAS Systolic blood pressure, combined automated + manual reading: PIP 0.05; L2G IRF6 0.13, UTP25 0.10, C1orf74 0.10
> GWAS Orofacial clefts: PIP 0.05; L2G IRF6 0.16, TRAF3IP3 0.12, C1orf74 0.10
> GWAS Systolic blood pressure: PIP 0.05; L2G IRF6 0.13, C1orf74 0.09, UTP25 0.08
> GWAS Systolic blood pressure (MTAG): PIP 0.05; L2G IRF6 0.17, C1orf74 0.09, UTP25 0.08
> eqtl for TRAF3IP3 (blueprint_tx_monocyte_enst00000460314): PIP 0.04
> eqtl for TRAF3IP3 (twinsuk_tx_blood_enst00000367023): PIP 0.02
> eqtl for TRAF3IP3 (twinsuk_exon_blood_ensg00000009790_15_1_209782056_): PIP 0.02
> eqtl for TRAF3IP3 (schmiedel_2018_exon_treg_naive_ensg00000009790_15_): PIP 0.02
> Best L2G gene scores across these sets: UTP25 0.75, IRF6 0.67, TRAF3IP3 0.53, C1orf74 0.10

<a id="e06"></a>**E06** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=rs642961%20AND%20UTP25%20AND%20%22cleft%20lip%22&format=json&pageSize=8&resultType=core; retrieved 2026-10-25T17:29:43+00:00)

> Europe PMC: 2 hits for 'rs642961 AND UTP25 AND "cleft lip"'; top 2 with PMIDs:
> PMID 40670354 (2025): Identification of functional non-coding variants associated with orofacial cleft.
> PMID 37161310 (2023): A Variant in the <i>IRF6</i> Promoter Associated with the Risk for Orofacial Clefting.

<a id="e07"></a>**E07** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-26T01:39:36+00:00)

> No ENCODE TRIB1 ChIP-seq peak contains chr1:209815925:A>G. Absence can also mean no TRIB1 experiment in that biosample. 0 peaks lie within 100 bp without containing it.

<a id="e08"></a>**E08** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-26T01:39:36+00:00)

> No ENCODE PAX3 ChIP-seq peak contains chr1:209815925:A>G. Absence can also mean no PAX3 experiment in that biosample. 0 peaks lie within 100 bp without containing it.

<a id="e09"></a>**E09** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=rs642961%20UTP25%20IRF6%20enhancer%20regulation%20functional%20variant&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T01:39:36+00:00)

> Europe PMC: 2 hits for 'rs642961 UTP25 IRF6 enhancer regulation functional variant'; top 2 with PMIDs:
> PMID 40670354 (2025): Identification of functional non-coding variants associated with orofacial cleft.
> PMID 37161310 (2023): A Variant in the <i>IRF6</i> Promoter Associated with the Risk for Orofacial Clefting.

<a id="e09a"></a>**E09a** literature_search, Europe PMC abstract, PMID 40670354 (https://europepmc.org/article/MED/40670354; retrieved 2026-10-26T01:39:36+00:00)

> For two SNPs near IRF6 and one near FOXE1, we engineer the genome of induced pluripotent stem cells, differentiate the cells into embryonic oral epithelium, and discover allele-specific effects on the levels of effector gene expression, and, in two cases, the binding affinity of transcription factors FOXE1 or ETS2.

<a id="e09b"></a>**E09b** literature_search, Europe PMC abstract, PMID 40670354 (https://europepmc.org/article/MED/40670354; retrieved 2026-10-26T01:39:36+00:00)

> Conditional analyses of GWAS data suggest the two functional SNPs near IRF6 account for the majority of risk for CL/P at this locus.

<a id="e09c"></a>**E09c** literature_search, Europe PMC abstract, PMID 37161310 (https://europepmc.org/article/MED/37161310; retrieved 2026-10-26T01:39:36+00:00)

> This study revealed that the SNP rs12403599, within the IRF6 promoter, is associated with all phenotypes of NSCL/P, especially nonsyndromic cleft lip (NSCLO) and a subphenotype of it, microform cleft lip (MCL).

<a id="e09d"></a>**E09d** literature_search, Europe PMC abstract, PMID 37161310 (https://europepmc.org/article/MED/37161310; retrieved 2026-10-26T01:39:36+00:00)

> To test if rs12403599 is functional, we carried out reporter assays in a fetal oral epithelium cells (GMSM-K).
