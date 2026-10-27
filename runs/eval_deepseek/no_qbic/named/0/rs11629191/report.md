# rs11629191 and Breast cancer

Configuration `no_qbic`, named mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.02 over 9 model calls; 230 s.

Variant `chr14:55887040:C>T` (germline); expression context: DepMap:ACH-000019 (MCF7).

## Ranked chains

### 1. null: Null hypothesis: no TF-mediated effect of rs11629191; any association is linkage, passenger, or noise (p = 0.80)

Null chain: no TF-mediated effect of this variant.

Predictions: No allele-specific TF binding at this position; No breast-tissue eQTL or regulatory effect for this variant; No FOXA1 or ESR1 occupancy in MCF7 at this position

Falsified if: A reproducible allele-specific TF binding and regulatory effect is demonstrated; The variant changes expression of a nearby gene in breast cancer cells; The variant is shown to be the causal variant in a breast cancer GWAS or functional assay

### 2. chain_1: FOXA1 binds the reference C allele more strongly at a cryptic distal element and alters PELI2 expression in MCF7 breast cancer cells (p = 0.13)

TF FOXA1 (stated coverage not_checked; registry own_model), ref allele binds more; element cryptic distal element; gene PELI2; cell type MCF7 breast cancer cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | Hypothesis: FOXA1 binds the reference C allele preferentially and the T allele weakens binding; no direct allele-specific binding evidence exists. | missing | none |
| element | No annotated cCRE overlaps the variant, so this chain requires a cryptic distal regulatory element. | weak | [E03](#e03) |
| gene | PELI2 is the nearest listed protein-coding gene at 230.8 kb upstream and encodes a Pellino E3 ubiquitin ligase; direct element-to-PELI2 targeting is unproven. | weak | [E02](#e02), [E06a](#e06a) |
| cell_type | The hypothesized effect would occur in MCF7 breast cancer cells; no direct evidence shows FOXA1/PELI2 mediation for this variant in MCF7. | missing | none |
| phenotype | PELI2 has cancer-relevant literature, but no specific breast-cancer phenotype for PELI2 at this variant is established. | weak | [E06](#e06) |

Predictions: Targeted FOXA1 ChIP-qPCR shows enrichment in MCF7; Allele-specific FOXA1 binding is stronger for C than T; PELI2 expression is altered in breast cancer cells

Falsified if: Targeted FOXA1 ChIP-qPCR shows no enrichment in MCF7; Allele-specific assays show no FOXA1 binding difference between C and T; PELI2 expression is unchanged by the variant or FOXA1 perturbation

### 3. chain_2: ESR1 binds the alt T allele more strongly at a cryptic estrogen-responsive element and alters ENSG00000259868 expression (p = 0.07)

TF ESR1 (stated coverage not_checked; registry own_model), alt allele binds more; element cryptic estrogen-responsive distal element; gene ENSG00000259868; cell type MCF7 breast cancer cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | Hypothesis: ESR1 binds the alt T allele preferentially and the C allele has weaker binding; no direct allele-specific binding evidence exists. | missing | none |
| element | No annotated cCRE overlaps the variant, so this chain requires a cryptic estrogen-responsive distal element. | weak | [E03](#e03) |
| gene | A weak molecular-QTL credible set links the variant to ENSG00000259868 with PIP 0.03 in GTEx brain nucleus accumbens; this does not establish breast-tissue regulation. | weak | [E05](#e05) |
| cell_type | The hypothesized ESR1 effect would occur in MCF7 breast cancer cells; no direct cell-type evidence supports it. | missing | none |
| phenotype | Altered ENSG00000259868 expression would affect breast cancer risk or progression; no evidence supports this. | missing | none |

Predictions: Targeted ESR1 ChIP-qPCR shows enrichment in MCF7; Allele-specific ESR1 binding is stronger for T than C; ENSG00000259868 expression is associated with rs11629191 in breast tissue

Falsified if: Targeted ESR1 ChIP-qPCR shows no enrichment in MCF7; Allele-specific assays show no ESR1 binding difference between C and T; No breast-tissue eQTL for ENSG00000259868 is replicated

## Prediction matrix

| Test | Cost | Separates top two | null | chain_1 | chain_2 |
| --- | --- | --- | --- | --- | --- |
| Targeted FOXA1 ChIP-qPCR in MCF7 at rs11629191 | low | yes | No FOXA1 enrichment | FOXA1 enrichment over negative control | No ESR1-dependent prediction; no FOXA1 prediction |
| Targeted ESR1 ChIP-qPCR in MCF7 at rs11629191 | low | no | No enrichment | No enrichment | ESR1 enrichment over negative control |
| Allele-specific FOXA1 binding assay (EMSA/SELEX with C vs T probes) | low | yes | No allele-specific FOXA1 binding | Stronger FOXA1 binding to C than T | No allele-specific FOXA1 binding |
| Breast tissue eQTL lookup for PELI2 and ENSG00000259868 | low | yes | Neither eQTL signal | PELI2 eQTL signal associated with rs11629191 | ENSG00000259868 eQTL signal associated with rs11629191 |

## Next experiment

cheapest

## Investigate calls

- chip_peaks({"tf": "FOXA1", "biosample": "MCF7"})
- chip_peaks({"tf": "ESR1", "biosample": "MCF7"})
- eqtl_lookup({"tissue": "Breast - Mammary Tissue"})

## Flags

- literature_fallback: no hits for 'rs11629191 AND PELI2 AND "breast cancer"'; dropped the rsID

Citation support: 0.50 of links cite only evidence that passed every check.

## Evidence

<a id="e01"></a>**E01** variant_annotation, Ensembl VEP (GRCh38) (https://rest.ensembl.org/vep/human/region/14:55887040-55887040:1/T?content-type=application/json&Conservation=1; retrieved 2026-10-25T17:32:49+00:00)

> Variant chr14:55887040:C>T (GRCh38), allele string C/T
> Known IDs: rs11629191
> Most severe consequence: intron_variant
> Regulatory features: none
> GERP conservation score at the site: -3.12
> Transcript consequences: none (intergenic)

<a id="e02"></a>**E02** nearest_genes, Ensembl overlap (protein_coding) (https://rest.ensembl.org/overlap/region/human/14:54887040-56887040?feature=gene;biotype=protein_coding;content-type=application/json; retrieved 2026-10-25T17:32:40+00:00)

> 14 protein-coding genes within 1000 kb of chr14:55887040:C>T, by distance to TSS:
> PELI2: 230.8 kb from TSS (upstream, strand +1)
> KTN1: 328.0 kb from TSS (downstream, strand +1)
> TBPL2: 430.3 kb from TSS (upstream, strand -1)
> ATG14: 475.2 kb from TSS (upstream, strand -1)
> TMEM260: 601.3 kb from TSS (upstream, strand +1)
> CHMP4BP1: 615.7 kb from TSS (downstream, strand +1)
> FBXO34: 615.7 kb from TSS (downstream, strand +1)
> DLGAP5: 695.4 kb from TSS (upstream, strand -1)
> LGALS3: 765.7 kb from TSS (downstream, strand +1)
> MAPK1IP1L: 835.4 kb from TSS (downstream, strand +1)

<a id="e03"></a>**E03** ccre_lookup, ENCODE v4 cCRE registry (ENCFF420VPZ) and SCREEN (https://screen-beta-api.wenglab.org/dataws/cre_table; retrieved 2026-10-25T17:32:13+00:00)

> No cCRE overlaps the variant; nearest is EH38E1716463 (dELS) 1868 bp away.
> SCREEN: 0 cCREs within 500 bp (max z-score across ENCODE biosamples):
> Biosample-specific z-scores are not in this call; the values above are maxima over biosamples.

<a id="e04"></a>**E04** gwas_lookup, GWAS Catalog REST v2 (https://www.ebi.ac.uk/gwas/rest/api/v2/associations?rs_id=rs11629191&size=100; retrieved 2026-10-25T17:32:50+00:00)

> 0 GWAS Catalog associations for rs11629191, strongest first:

<a id="e05"></a>**E05** finemap_lookup, Open Targets Platform (credible sets, L2G) (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-25T17:32:49+00:00)

> 1 credible sets contain 14_55887040_C_T: 0 GWAS, 1 molecular QTL.
> eqtl for ENSG00000259868 (gtex-v10_ge_brain_nucleus_accumbens_ensg0000025986): PIP 0.03

<a id="e06"></a>**E06** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=PELI2%20AND%20%22breast%20cancer%22&format=json&pageSize=8&resultType=core; retrieved 2026-10-25T17:32:50+00:00)

> Europe PMC: 178 hits for 'PELI2 AND "breast cancer"'; top 7 with PMIDs:
> PMID 41023515 (2025): Pellino ubiquitin ligases: double-edged swords in hematologic malignancies-from oncogenic stabilizers to therapeutic vulnerabilities.
> PMID 41331176 (2025): Construction and validation of risk models of prognostic genes associated with parthanatos in papillary thyroid carcinoma based on bioinformatics.
> PMID 40362379 (2025): &lt;i&gt;O&lt;/i&gt;-Desmethyltramadol Enhanced Anti-Cancer Efficacy over Tramadol Through Non-μ-Opioid Receptor and Differential Cellular Contexts of Human Breast Cancer Cells.
> PMID 42757486 (2026): Pemetrexed increases BRCA1 protein stability and sensitizes TNBC cells to radiotherapy.
> PMID 42734444 (2027): Anesthesia inhalation agent sevoflurane induces perioperative cognitive impairment: Apelin/early growth response 1 axis induces ferritinophagy and exacerbates ferroptosis.
> PMID 41079921 (2025): PRMT1/PRMT5-Mediated Differential Arginine Methylation of CRIP1 Promotes the Recurrence of Small Cell Lung Cancer after Chemotherapy.
> PMID 42380137 (2026): HOXC9 accelerates esophageal squamous cell carcinoma progression via OTUD1-FABP5-mediated lipid metabolic reprogramming.

<a id="e06a"></a>**E06a** literature_search, Europe PMC abstract, PMID 41023515 (https://europepmc.org/article/MED/41023515; retrieved 2026-10-25T17:32:50+00:00)

> The Pellino protein family is an evolutionarily conserved group of E3 ubiquitin ligases comprising Pellino1, Pellino2, and Pellino3.

<a id="e06b"></a>**E06b** literature_search, Europe PMC abstract, PMID 41331176 (https://europepmc.org/article/MED/41331176; retrieved 2026-10-25T17:32:50+00:00)

> Seven prognostic genes (TSHZ3, SERGEF, AKAP12, SGPP2, ASGR1, AK1, PELI2) were identified.

<a id="e06c"></a>**E06c** literature_search, Europe PMC abstract, PMID 40362379 (https://europepmc.org/article/MED/40362379; retrieved 2026-10-25T17:32:50+00:00)

> Hence, we sought to examine whether the cytotoxic effect of O-desmethyltramadol was better than tramadol on breast cancer cells.

<a id="e06d"></a>**E06d** literature_search, Europe PMC abstract, PMID 42757486 (https://europepmc.org/article/MED/42757486; retrieved 2026-10-25T17:32:50+00:00)

> Although pathogenic BRCA1 mutations are relatively uncommon, decreased BRCA1 protein expression, which is typically driven by accelerated proteasomal degradation, is implicated in aggressive breast cancer (BC), particularly triple‑negative (TN)BC.

<a id="e07"></a>**E07** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-26T00:28:52+00:00)

> No ENCODE FOXA1 ChIP-seq peak contains chr14:55887040:C>T in biosamples matching 'MCF7'. Absence can also mean no FOXA1 experiment in that biosample. 0 peaks lie within 100 bp without containing it.

<a id="e08"></a>**E08** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-26T00:36:39+00:00)

> No ENCODE ESR1 ChIP-seq peak contains chr14:55887040:C>T in biosamples matching 'MCF7'. Absence can also mean no ESR1 experiment in that biosample. 0 peaks lie within 100 bp without containing it.

<a id="e09"></a>**E09** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr14_55887040_C_T_b38&datasetId=gtex_v8; retrieved 2026-10-25T17:34:02+00:00)

> 0 significant GTEx v8 single-tissue eQTLs for chr14_55887040_C_T_b38 in tissues matching 'Breast - Mammary Tissue'. NES is the effect of the alt allele (T) relative to ref (C).
