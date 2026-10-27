# rs642961 and Cleft lip (IRF6)

Configuration `no_qbic`, named mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.02 over 9 model calls; 99 s.

Variant `chr1:209815925:A>G` (germline); expression context: none.

## Ranked chains

### 1. H2: rs642961 alters TF binding to promote detrimental IRF6 expression, increasing cleft lip risk (A=Risk). (p = 0.31)

TF Tbx24 (stated coverage not_checked; registry unknown_name), ref allele binds more; element ENSR1_B3JM9C enhancer; gene IRF6; cell type Neural crest cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The reference allele (A) binds TF Tbx24 more strongly than the alternative allele (G), leading to altered TF occupancy and expression regulation. | missing | [E01](#e01) |
| element | The variant rs642961 is located within the enhancer region ENSR1_B3JM9C, which is marked as an active distal enhancer-like element. | supported | [E03](#e03) |
| gene | The element ENSR1_B3JM9C regulates IRF6 expression, which is indirectly supported by L2G scoring. | weak | [E02](#e02), [E05](#e05) |
| cell_type | IRF6 plays a known role in craniofacial development, linking this regulation to relevant cell types. | missing | [E06](#e06) |
| phenotype | The risk allele (A) alters IRF6 expression in a manner consistent with the observed association between rs642961 and orofacial cleft risk. | weak | [E04](#e04) |

Predictions: The risk allele (A) influences IRF6 expression leading to increased orofacial cleft risk.

Falsified if: No detectable binding of Tbx24 to the variant location.; The functional relationship is indirect or does not lead to altered IRF6 expression.

### 2. H1: Null hypothesis: rs642961 is a passenger mutation or linked causal variant with no TF-mediated regulatory effect. (p = 0.25)

Null chain: no TF-mediated effect of this variant.

Predictions: The regulatory effect of rs642961 on disease risk is independent of transcription factor binding and subsequent changes in gene expression.

Falsified if: A TF is found to bind rs642961 and modulate the expression of IRF6, UTP25, C1orf74, or TRAF3IP3, correlating with the disease risk.

### 3. H3: rs642961 alters TF binding to promote detrimental UTP25 expression, increasing cleft lip risk (A=Risk). (p = 0.25)

TF Egr2 (stated coverage not_checked; registry own_model), ref allele binds more; element ENSR1_B3JM9C enhancer; gene UTP25; cell type Dental/Oral epithelial progenitors.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The reference allele (A) of rs642961 binds TF Egr2 more strongly than the alternative allele (G). | missing | [E01](#e01) |
| element | The variant lies within the accessible enhancer ENSR1_B3JM9C, facilitating interaction with Egr2. | weak | [E03](#e03) |
| gene | The element ENSR1_B3JM9C regulates UTP25 expression, evidenced by high L2G scores. | weak | [E05](#e05) |
| cell_type | UTP25 is expressed in craniofacial and dental tissues, making this cell type relevant for the phenotype. | missing | [E03](#e03) |
| phenotype | Altered UTP25 expression linked to rs642961 contributes to orofacial cleft risk, consistent with the risk allele A. | weak | [E04](#e04) |

Predictions: The risk allele (A) influences UTP25 expression leading to increased orofacial cleft risk.

Falsified if: No detectable binding of Egr2 to the variant location.; The risk is not mediated by changes in UTP25 expression.

### 4. H4: rs642961 alters TF binding to promote detrimental TRAF3IP3 expression, increasing cleft lip risk (A=Risk). (p = 0.19)

TF STAT3 (stated coverage not_checked; registry not_in_coverage), ref allele binds more; element ENSR1_B3JM9C enhancer; gene TRAF3IP3; cell type Immune cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The reference allele (A) of rs642961 binds TF STAT3 more strongly than the alternative allele (G). | missing | [E01](#e01) |
| element | The enhancer ENSR1_B3JM9C mediates the regulatory influence of the rs642961 variant on TRAF3IP3. | weak | [E03](#e03) |
| gene | The element ENSR1_B3JM9C regulates TRAF3IP3 expression, supported by low-confidence eQTL data. | weak | [E05](#e05) |
| cell_type | STAT3 and TRAF3IP3 function are implicated in inflammatory processes relevant to congenital defects. | missing | [E05](#e05) |
| phenotype | Altered TRAF3IP3 levels due to the risk allele A contribute to orofacial cleft risk. | weak | [E04](#e04) |

Predictions: The risk allele (A) influences TRAF3IP3 expression leading to increased orofacial cleft risk.

Falsified if: No detectable binding of STAT3 to the variant location.; The risk is not mediated by changes in TRAF3IP3 expression.

## Prediction matrix

| Test | Cost | Separates top two | H2 | H1 | H3 | H4 |
| --- | --- | --- | --- | --- | --- | --- |
| chip_peaks({"tf":"Tbx24"}) | medium | yes | Positive | Negative | Negative | Negative |
| chip_peaks({"tf":"Egr2"}) | medium | yes | Negative | Negative | Positive | Negative |
| chip_peaks({"tf":"STAT3"}) | medium | yes | Negative | Negative | Negative | Positive |

## Next experiment

chip_peaks({"tf":"Tbx24"})

## Investigate calls

- chip_peaks({"tf": "Tbx24"})
- chip_peaks({"tf": "Egr2"})
- chip_peaks({"tf": "STAT3"})

## Flags

- none

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

<a id="e07"></a>**E07** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-26T00:34:21+00:00)

> No ENCODE Tbx24 ChIP-seq peak contains chr1:209815925:A>G. Absence can also mean no Tbx24 experiment in that biosample. 0 peaks lie within 100 bp without containing it.

<a id="e08"></a>**E08** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-26T00:34:23+00:00)

> No ENCODE Egr2 ChIP-seq peak contains chr1:209815925:A>G. Absence can also mean no Egr2 experiment in that biosample. 0 peaks lie within 100 bp without containing it.

<a id="e09"></a>**E09** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-26T00:34:24+00:00)

> 1 ENCODE STAT3 ChIP-seq peaks contain chr1:209815925:A>G: biosamples MCF 10A; experiments ENCSR000DOQ.
