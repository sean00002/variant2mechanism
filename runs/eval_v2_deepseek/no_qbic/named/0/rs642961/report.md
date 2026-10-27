# rs642961 and Cleft lip (IRF6)

Configuration `no_qbic`, named mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.03 over 9 model calls; 222 s.

Variant `chr1:209815925:A>G` (germline); expression context: none.

## Ranked chains

### 1. H_Null: No TF-mediated effect at this regulatory element. (p = 0.44)

Null chain: no TF-mediated effect of this variant.

Predictions: The variant rs642961 does not functionally alter TF binding or transcriptional activity of linked genes.

Falsified if: Any change in TF binding occupancy or gene expression correlates with the A/G genotype.

### 2. H_IRF6_ZNF687: The variant alters ZNF687 binding affinity at the IRF6 enhancer, influencing orofacial cleft risk. (p = 0.38)

TF ZNF687 (QBiC-SELEX coverage own_model), ref allele binds more; element EH38E2863563 dELS; gene IRF6; cell type Cerebellum.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The reference allele (A) increases ZNF687 binding affinity at the variant site, despite lack of allele-specific ChIP data. | weak | [E04](#e04), [E05](#e05) |
| element | The variant rs642961 is located within the distal enhancer-like element EH38E2863563. | supported | [E01](#e01), [E03](#e03) |
| gene | ZNF687 binding modulates IRF6 expression in the cerebellum, showing a change associated with the risk allele (A). | weak | [E08](#e08) |
| cell_type | The regulatory effect occurs in bulk cerebellar tissue. | supported | [E08](#e08) |
| phenotype | Alterations in IRF6 expression driven by the A allele contributes to the risk of Orofacial Cleft. | weak | [E06](#e06) |

Predictions: The A allele increases ZNF687 binding compared to the G allele.; The IRF6 eQTL in Brain_Cerebellum shows that the G allele leads to significantly lower expression compared to the A allele (consistent with NES -0.62).

Falsified if: The fold change in ZNF687 occupancy at the rs642961 locus is not reproducible across different assays.; The expression change in IRF6 in the cerebellum is not significant, or the direction of change does not align with the risk allele (A).

### 3. H_TRAF3IP3_MYC: The variant affects MYC binding at the TRAF3IP3 enhancer, linking the locus to systemic cardiovascular risk. (p = 0.19)

TF MYC (QBiC-SELEX coverage not_in_coverage), ref allele binds more; element EH38E2863563 dELS; gene TRAF3IP3; cell type Whole Blood.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The reference allele (A) increases MYC binding at the variant site, inferred from non-specific peak association. | missing | [E04](#e04) |
| element | The variant rs642961 is located within the distal enhancer-like element EH38E2863563. | supported | [E01](#e01), [E03](#e03) |
| gene | The variant modulates TRAF3IP3 expression, showing an increase associated with the risk allele (A). | missing | [E08](#e08) |
| cell_type | The regulatory effect occurs in Whole Blood. | supported | [E08](#e08) |
| phenotype | The alteration in TRAF3IP3 expression driven by the A allele is associated with systemic Hypertension. | weak | [E06](#e06) |

Predictions: The A allele increases MYC binding at the variant locus in blood cells.; Increased TRAF3IP3 expression in Whole Blood is linked to elevated blood pressure.

Falsified if: MYC binding at the rs642961 locus is not allele-specific or significantly altered.; The correlation between rs642961 and TRAF3IP3 expression is entirely mediated through linkage.

## Prediction matrix

| Test | Cost | Separates top two | H_Null | H_IRF6_ZNF687 | H_TRAF3IP3_MYC |
| --- | --- | --- | --- | --- | --- |
| Allele-Specific ChIP-seq for ZNF687 at chr1:209815925 | medium | yes | No difference in binding | A allele binds more strongly | No difference in binding |
| Allele-Specific ChIP-seq for MYC at chr1:209815925 | medium | yes | No difference in binding | No difference in binding | A allele binds more strongly |
| Allele-Specific GTEx Expression comparison (A vs G) for IRF6 in Brain_Cerebellum | low | yes | No significant difference in expression | G expression is significantly lower than A expression | No significant difference in expression (IRF6 not measured) |
| Allele-Specific GTEx Expression comparison (A vs G) for TRAF3IP3 in Whole_Blood | low | yes | No significant difference in expression | No significant difference in expression (TRAF3IP3 not measured) | G expression is significantly higher than A expression |

## Next experiment

Allele-Specific ChIP-seq for ZNF687 at chr1:209815925

## Investigate calls

- literature_search({"query": "rs642961 IRF6 enhancer transcription factor allele-specific binding cleft lip"})
- tf_expression({"tf": "ZNF687", "context": "GTEx:Brain - Cerebellum"})
- chip_peaks({"tf": "MYC", "biosample": "Whole Blood"})

## Flags

- quote_rejected: PMID 42799765: not an exact substring of the abstract

Citation support: 1.00 of links cite only evidence that passed every check.

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

<a id="e04"></a>**E04** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> ENCODE TF ChIP-seq at chr1:209815925:A>G: 15 peaks contain the variant, from 6 factors in 6 biosamples. No ENCODE biosample matches the expression context, so no peak counts as bound here. cCRE class at the variant: dELS. Bound factors outside the TF model collection (co-factors, Pol II, and TFs with no binding model; signs of an active element, not TF candidates): DPF2, MYC, POLR2A, POLR2AphosphoS5, STAT3. Bound, expressed TFs with a binding model: 1; listed one per row: ZNF687. Assayed with no peak here: 0 TFs in the matching biosample, 572 only elsewhere; never assayed: 536.

<a id="e05"></a>**E05** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> ZNF687: bound elsewhere. 1 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: GM12878 (e.g. ENCSR859FDL). expression not filtered (no expression data for this context).

<a id="e06"></a>**E06** gwas_lookup, GWAS Catalog REST v2 (https://www.ebi.ac.uk/gwas/rest/api/v2/associations?rs_id=rs642961&size=100; retrieved 2026-10-25T17:29:42+00:00)

> 8 GWAS Catalog associations for rs642961, strongest first:
> Systolic blood pressure: p 6.0e-12, effect allele G, risk-allele frequency NR, PMID 38689001
> Hypertension: p 2.0e-08, effect allele A, risk-allele frequency 0.1951, PMID 33230300
> Pulse pressure: p 1.0e-07, effect allele G, risk-allele frequency NR, PMID 38689001
> Diastolic blood pressure: p 3.0e-07, effect allele G, risk-allele frequency NR, PMID 38689001
> Orofacial clefts: p 2.0e-06, effect allele A, risk-allele frequency NR, PMID 19270707

<a id="e07"></a>**E07** finemap_lookup, Open Targets Platform (credible sets, L2G) (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-25T17:29:41+00:00)

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

<a id="e08"></a>**E08** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr1_209815925_A_G_b38&datasetId=gtex_v8; retrieved 2026-10-25T22:31:38+00:00)

> 15 significant GTEx v8 single-tissue eQTLs for chr1_209815925_A_G_b38. NES is the effect of the alt allele (G) relative to ref (A).
> SYT14 in Nerve_Tibial: NES -0.50, p 6.7e-20
> DIEXF in Cells_Cultured_fibroblasts: NES -0.23, p 1.9e-14
> DIEXF in Artery_Tibial: NES -0.23, p 1.2e-10
> TRAF3IP3 in Whole_Blood: NES +0.24, p 5.9e-10
> IRF6 in Brain_Cerebellum: NES -0.62, p 2.2e-07
> DIEXF in Whole_Blood: NES -0.15, p 2.9e-07
> SYT14 in Brain_Hippocampus: NES +0.53, p 3.3e-07
> DIEXF in Adipose_Subcutaneous: NES -0.20, p 7.5e-07
> SYT14 in Brain_Spinal_cord_cervical_c-1: NES +0.72, p 2.7e-06
> DIEXF in Lung: NES -0.11, p 3.2e-06
> IRF6 in Brain_Cerebellar_Hemisphere: NES -0.61, p 3.3e-06
> DIEXF in Brain_Frontal_Cortex_BA9: NES +0.35, p 4.6e-06
> DIEXF in Brain_Cortex: NES +0.33, p 7.0e-06
> DIEXF in Adipose_Visceral_Omentum: NES -0.16, p 2.5e-05
> C1orf74 in Whole_Blood: NES +0.15, p 8.6e-05

<a id="e09"></a>**E09** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=rs642961%20AND%20UTP25%20AND%20%22cleft%20lip%22&format=json&pageSize=8&resultType=core; retrieved 2026-10-25T17:29:43+00:00)

> Europe PMC: 2 hits for 'rs642961 AND UTP25 AND "cleft lip"'; top 2 with PMIDs:
> PMID 40670354 (2025): Identification of functional non-coding variants associated with orofacial cleft.
> PMID 37161310 (2023): A Variant in the <i>IRF6</i> Promoter Associated with the Risk for Orofacial Clefting.

<a id="e10"></a>**E10** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=rs642961%20IRF6%20enhancer%20transcription%20factor%20allele-specific%20binding%20cleft%20lip&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T02:30:53+00:00)

> Europe PMC: 30 hits for 'rs642961 IRF6 enhancer transcription factor allele-specific binding cleft lip'; top 8 with PMIDs:
> PMID 42799765 (2026): The orofacial cleft risk gene IRF6 is a target gene of SOX9 in cranial neural crest cells.
> PMID 40670354 (2025): Identification of functional non-coding variants associated with orofacial cleft.
> PMID 40918684 (2025): Functional Validation of Noncoding Variants Associated With Nonsyndromic Orofacial Cleft.
> PMID 39500877 (2024): High incidence and geographic distribution of cleft palate in Finland are associated with the IRF6 gene.
> PMID 37762190 (2023): Genetic Factors of Teeth Impaction: Polymorphic and Haplotype Variants of &lt;i&gt;PAX9&lt;/i&gt;, &lt;i&gt;MSX1&lt;/i&gt;, &lt;i&gt;AXIN2&lt;/i&gt;, and &lt;i&gt;IRF6&lt;/i&gt; Genes.
> PMID 37161310 (2023): A Variant in the <i>IRF6</i> Promoter Associated with the Risk for Orofacial Clefting.
> PMID 36008388 (2022): Chromatin conformation of human oral epithelium can identify orofacial cleft missing functional variants.
> PMID 35110662 (2022): Allele-specific transcription factor binding in a cellular model of orofacial clefting.

<a id="e11"></a>**E11** tf_expression, DepMap expression / GTEx v8 medians (local files; retrieved local)

> ZNF687 in GTEx tissue median Brain - Cerebellum: 22.25 TPM, rank 327 of 1631 TFs (1 = highest); this context is at the 92.6th percentile of ZNF687 across all GTEx tissues.

<a id="e12"></a>**E12** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-26T02:31:02+00:00)

> No ENCODE MYC ChIP-seq peak contains chr1:209815925:A>G in biosamples matching 'Whole Blood'. Absence can also mean no MYC experiment in that biosample. In other biosamples, 2 MYC peaks do contain the variant: MCF 10A (experiments ENCSR000DOM, ENCSR000DOS).
