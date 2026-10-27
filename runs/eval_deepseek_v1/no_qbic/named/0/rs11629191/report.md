# rs11629191 and Breast cancer

Configuration `no_qbic`, named mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.01 over 7 model calls; 144 s.

Variant `chr14:55887040:C>T` (germline); expression context: DepMap:ACH-000019 (MCF7).

## Ranked chains

### 1. H0_no_TF_effect: No TF-mediated allelic effect (p = 0.90)

Null chain: no TF-mediated effect of this variant.

Predictions: No reproducible allele-specific TF binding at rs11629191 in MCF7 or breast-derived assays.; No allele-specific regulatory activity in reporter or MPRA assays.; Any disease association would be explained by a linked causal variant or by chance.

Falsified if: An allele-specific TF footprint, EMSA, or MPRA signal is reproducibly detected.; CRISPR editing of rs11629191 changes a nearby gene or a breast-cancer phenotype.

### 2. H2_FOXA1_ref_lncRNA: FOXA1 binds the ref allele at an unannotated element and affects ENSG00000259868 (p = 0.06)

TF FOXA1 (stated coverage not_checked; registry own_model), ref allele binds more; element unannotated intronic element; gene ENSG00000259868; cell type brain nucleus accumbens (eQTL), not MCF7.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | FOXA1 would need to bind the ref C allele more strongly; no positive motif, SELEX, MPRA, or reporter evidence is provided, and ENCODE FOXA1 ChIP-seq shows no FOXA1 peak containing the variant in MCF7 (E08). | missing | [E08](#e08) |
| element | This requires an unannotated intronic element, but E01 reports no regulatory features and E03 reports no cCRE overlap; absence of annotation is not positive evidence for a functional element. | missing | [E01](#e01), [E03](#e03) |
| gene | The only genetic signal is a weak credible-set molecular QTL for ENSG00000259868 with PIP 0.03 in brain nucleus accumbens (E05), and GTEx breast tissue shows no significant eQTL for this variant (E09). | weak | [E05](#e05), [E09](#e09) |
| cell_type | The eQTL is in brain nucleus accumbens, not MCF7 (E05), and FOXA1 ChIP-seq has no peak at the variant in MCF7 (E08), so breast-cell relevance is unproven. | weak | [E05](#e05), [E08](#e08) |
| phenotype | There is no GWAS association for rs11629191 (E04), so a breast-cancer effect through ENSG00000259868 is only speculative. | missing | [E04](#e04) |

Predictions: FOXA1 ChIP-seq or EMSA shows stronger binding to the ref C allele.; ENSG00000259868 expression is allele-dependent in the relevant cell type.; Editing the variant changes ENSG00000259868 expression.

Falsified if: FOXA1 binds equally to both alleles or not at all.; ENSG00000259868 is not expressed or not allele-dependent in the relevant cell type.; The element is not active in MCF7.

### 3. H1_ESR1_alt_PELI2: ESR1 binds the alt allele in a cryptic intronic enhancer and affects PELI2 (p = 0.04)

TF ESR1 (stated coverage not_checked; registry own_model), alt allele binds more; element cryptic intronic enhancer; gene PELI2; cell type MCF7 breast cancer.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | ESR1 would need to bind the alt T allele more strongly; no positive motif, SELEX, MPRA, or reporter evidence is provided, and ENCODE FOXA1/ESR1 ChIP-seq shows no ESR1 peak containing the variant in MCF7 (E07). | missing | [E07](#e07) |
| element | This requires a cryptic intronic enhancer, but E01 reports an intron_variant with no regulatory features and E03 reports no cCRE overlap, with the nearest dELS 1868 bp away; the evidence argues against an annotated element. | missing | [E01](#e01), [E03](#e03) |
| gene | PELI2 is the nearest protein-coding gene at 230.8 kb upstream, but the only credible-set molecular QTL is for ENSG00000259868, not PELI2 (E05), and GTEx breast tissue shows no significant eQTL for this variant (E09). | missing | [E02](#e02), [E05](#e05), [E09](#e09) |
| cell_type | MCF7 is the stated expression context, but no MCF7-specific regulatory or expression evidence supports this chain; ESR1 ChIP-seq has no peak at the variant in MCF7 (E07), and the only eQTL is in brain nucleus accumbens (E05). | missing | [E05](#e05), [E07](#e07) |
| phenotype | rs11629191 has no GWAS Catalog association (E04), and the PELI2 literature hits (E06) do not provide variant-specific or allele-specific breast-cancer evidence. | missing | [E04](#e04), [E06](#e06) |

Predictions: ESR1 ChIP-seq or EMSA shows stronger binding to the alt T allele.; PELI2 expression is allele-dependent in MCF7 or other estrogen-receptor-positive breast cells.; Editing the variant changes PELI2 expression or a breast-cancer phenotype.

Falsified if: ESR1 binds equally to both alleles or not at all.; No PELI2 expression change is seen with allele or editing.; The region is inactive in MCF7.

## Prediction matrix

| Test | Cost | Separates top two | H0_no_TF_effect | H2_FOXA1_ref_lncRNA | H1_ESR1_alt_PELI2 |
| --- | --- | --- | --- | --- | --- |
| Allele-specific FOXA1 EMSA with ref C vs alt T oligos | low | yes | Equal/no FOXA1 binding to both alleles; supports no TF-mediated allelic effect | FOXA1 binds ref C more than alt T; supports FOXA1-ref-allele chain | No FOXA1 allele-specific binding; does not test ESR1 |
| Allele-specific ESR1 EMSA or high-sensitivity ESR1 ChIP-qPCR at rs11629191 in MCF7 | low | no | No ESR1 allele-specific binding or peak | No ESR1 allele-specific binding or peak | ESR1 binds alt T more strongly or shows an allele-specific MCF7 peak |
| Allele-specific MPRA/reporter with ref C vs alt T in MCF7 or ER+ breast cells | medium | yes | No allelic difference in regulatory activity | Ref C shows higher activity if FOXA1 activates, or lower activity if FOXA1 represses | Alt T shows higher activity if ESR1 activates, or lower activity if ESR1 represses |
| Breast mammary eQTL lookup for rs11629191 with ENSG00000259868 and PELI2 | low | yes | No significant allele-specific eQTL | Allele-dependent ENSG00000259868 expression in breast tissue; current GTEx breast lookup is negative (E09) | Allele-dependent PELI2 expression in breast tissue |
| CRISPR edit rs11629191 in MCF7 or ER+ breast cells and measure PELI2/ENSG00000259868 | high | yes | No change in nearby gene expression or breast-cancer phenotype | ENSG00000259868 expression changes with allele | PELI2 expression or breast-cancer phenotype changes with allele |

## Next experiment

allele-specific FOXA1 EMSA

## Investigate calls

- chip_peaks({"tf": "ESR1", "biosample": "MCF7"})
- chip_peaks({"tf": "FOXA1", "biosample": "MCF7"})
- eqtl_lookup({"tissue": "Breast_Mammary_Tissue"})

## Flags

- literature_fallback: no hits for 'rs11629191 AND PELI2 AND "breast cancer"'; dropped the rsID

Citation support: 1.00 of links cite only evidence that passed every check.

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

<a id="e07"></a>**E07** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-26T00:36:39+00:00)

> No ENCODE ESR1 ChIP-seq peak contains chr14:55887040:C>T in biosamples matching 'MCF7'. Absence can also mean no ESR1 experiment in that biosample. 0 peaks lie within 100 bp without containing it.

<a id="e08"></a>**E08** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-26T00:28:52+00:00)

> No ENCODE FOXA1 ChIP-seq peak contains chr14:55887040:C>T in biosamples matching 'MCF7'. Absence can also mean no FOXA1 experiment in that biosample. 0 peaks lie within 100 bp without containing it.

<a id="e09"></a>**E09** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr14_55887040_C_T_b38&datasetId=gtex_v8; retrieved 2026-10-25T17:34:02+00:00)

> 0 significant GTEx v8 single-tissue eQTLs for chr14_55887040_C_T_b38 in tissues matching 'Breast_Mammary_Tissue'. NES is the effect of the alt allele (T) relative to ref (C).
