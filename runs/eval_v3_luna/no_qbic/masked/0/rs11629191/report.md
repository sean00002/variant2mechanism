# rs11629191 and Breast cancer

Configuration `no_qbic`, masked mode, seed 0. Models: generator openai/gpt-6-luna, critic openai/gpt-6-luna, summariser openai/gpt-6-luna. Cost $0.01 over 8 model calls; 132 s.

Variant `chr14:55887040:C>T` (germline); expression context: DepMap:ACH-000019 (MCF7).

## Ranked chains

### 1. H0: No TF-mediated effect at this variant (p = 0.96)

Null chain: no TF-mediated effect of this variant.

Predictions: The variant will not show a reproducible allele-specific TF-binding and regulatory effect in a relevant cell context; any disease relationship would be absent or due to another variant or process.

Falsified if: The variant shows reproducible allele-specific TF occupancy and a linked regulatory effect on a target gene in a relevant cell context.

### 2. H1: Speculative ESR1-to-PELI2 regulatory chain (p = 0.02)

TF ESR1 (QBiC-SELEX coverage own_model), alt allele binds more; element Unverified regulatory element at the variant; gene PELI2; cell type MCF7.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | This is an unsupported candidate model: it hypothesizes that ESR1 binds the alt T allele more strongly than ref C. No QBiC-SELEX result is supplied, and no ESR1 occupancy at the site is reported; the evidence does not support this direction or rank ESR1 above related TFs. | missing | [E04](#e04), [E09](#e09) |
| element | The model requires a regulatory element containing the variant, but none is demonstrated: no cCRE overlaps the site, and the nearest listed cCRE is 1868 bp away. | supported | [E03](#e03) |
| gene | PELI2 is only a candidate target based on distance; no evidence links this variant or an element at the site to PELI2. | supported | [E02](#e02), [E06](#e06), [E07](#e07) |
| cell_type | MCF7 is the stated expression context, but the supplied evidence does not establish ESR1 occupancy or activity at this site in MCF7. | supported | [E04](#e04), [E09](#e09) |
| phenotype | A PELI2-mediated breast-cancer effect is hypothetical; the variant has no reported GWAS Catalog association, and the supplied gene-level evidence does not establish a PELI2–breast cancer link. | supported | [E05](#e05), [E10](#e10) |

Predictions: If this model is correct, an allele-specific binding assay in MCF7 will show greater ESR1 binding to T than C; this distinguishes it from H2's proposed FOXA1/C-greater-than-T model.; If the variant affects PELI2 through this chain, perturbing ESR1 or the site will alter the allele-dependent regulatory effect; the direction of the resulting PELI2 change is not specified.

Falsified if: A suitably sensitive assay finds no ESR1 occupancy or no T-greater-than-C binding difference at the site.; ESR1 perturbation and variant editing do not affect the proposed allele-dependent regulatory effect or PELI2 expression in relevant cells.

### 3. H2: Speculative FOXA1-to-PELI2 regulatory chain (p = 0.02)

TF FOXA1 (QBiC-SELEX coverage own_model), ref allele binds more; element Unverified regulatory element at the variant; gene PELI2; cell type MCF7.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | This is an unsupported candidate model: it hypothesizes that FOXA1 binds the ref C allele more strongly than alt T. No QBiC-SELEX result is supplied, and no FOXA1 occupancy at the site is reported; the evidence does not support this direction or rank FOXA1 above related TFs. | missing | [E04](#e04) |
| element | The model requires a regulatory element containing the variant, but none is demonstrated: no cCRE overlaps the site, and the nearest listed cCRE is 1868 bp away. | supported | [E03](#e03) |
| gene | PELI2 is only a candidate target based on distance; no evidence links this variant or an element at the site to PELI2. | supported | [E02](#e02), [E06](#e06), [E07](#e07) |
| cell_type | MCF7 is the stated expression context, but the supplied evidence does not establish FOXA1 occupancy or activity at this site in MCF7. | supported | [E04](#e04) |
| phenotype | A PELI2-mediated breast-cancer effect is hypothetical; the variant has no reported GWAS Catalog association, and the supplied gene-level evidence does not establish a PELI2–breast cancer link. | supported | [E05](#e05), [E10](#e10) |

Predictions: If this model is correct, an allele-specific binding assay in MCF7 will show greater FOXA1 binding to C than T; this distinguishes it from H1's proposed ESR1/T-greater-than-C model.; If the variant affects PELI2 through this chain, perturbing FOXA1 or the site will alter the allele-dependent regulatory effect; the direction of the resulting PELI2 change is not specified.

Falsified if: A suitably sensitive assay finds no FOXA1 occupancy or no C-greater-than-T binding difference at the site.; FOXA1 perturbation and variant editing do not affect the proposed allele-dependent regulatory effect or PELI2 expression in relevant cells.

## Prediction matrix

| Test | Cost | Separates top two | H0 | H1 | H2 |
| --- | --- | --- | --- | --- | --- |
| Allele-specific ESR1 CUT&RUN in MCF7, with variant genotyping and sequencing across the site | medium | yes | No reproducible ESR1 occupancy with allele-specific imbalance at the variant. | ESR1 occupancy with greater signal from the T allele than the C allele. | No ESR1-specific T-greater-than-C occupancy; FOXA1 occupancy, if present, is not tested by this assay. |
| Allele-specific FOXA1 CUT&RUN in MCF7, with variant genotyping and sequencing across the site | medium | no | No reproducible FOXA1 occupancy with allele-specific imbalance at the variant. | No FOXA1-specific C-greater-than-T occupancy; ESR1 occupancy, if present, is not tested by this assay. | FOXA1 occupancy with greater signal from the C allele than the T allele. |
| Isogenic editing of C/T at the site in MCF7 followed by PELI2 expression measurement and ESR1 perturbation | high | yes | Editing does not reproducibly change PELI2 expression in an ESR1-dependent manner. | Editing changes PELI2 expression, and the effect depends on ESR1; the expression-change direction is not specified. | No ESR1-dependent PELI2 effect; a FOXA1-dependent effect would remain possible. |

## Next experiment

Run allele-specific ESR1 CUT&RUN in MCF7, first confirming the cell line's genotype at the site. It is the most direct, relatively low-burden test of the proposed H1 binding step against the null; a positive result would support ESR1 occupancy but would not by itself establish an allele-specific regulatory effect, the PELI2 target, or a breast-cancer link.

## Investigate calls

- chip_peaks({"tf": "ESR1", "biosample": "MCF-7"})
- gene_disease({"gene": "PELI2"})
- literature_search({"query": "PELI2 breast cancer regulatory variant"})

## Flags

- none

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

<a id="e04"></a>**E04** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> No ENCODE TF ChIP-seq peak contains chr14:55887040:C>T in any biosample. In the matching biosample MCF-7: 0 peaks from 0 factors. No cCRE contains the variant. Of the TFs with a binding model, 65 were assayed in the matching biosample and 508 only elsewhere, all without a peak here; 536 were never assayed.

<a id="e05"></a>**E05** gwas_lookup, GWAS Catalog REST v2 (https://www.ebi.ac.uk/gwas/rest/api/v2/associations?rs_id=rs11629191&size=100; retrieved 2026-10-25T17:32:50+00:00)

> 0 GWAS Catalog associations for rs11629191, strongest first:

<a id="e06"></a>**E06** finemap_lookup, Open Targets Platform (credible sets, L2G) (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-25T17:32:49+00:00)

> 1 credible sets contain 14_55887040_C_T: 0 GWAS, 1 molecular QTL.
> eqtl for ENSG00000259868 (gtex-v10_ge_brain_nucleus_accumbens_ensg0000025986): PIP 0.03

<a id="e07"></a>**E07** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr14_55887040_C_T_b38&datasetId=gtex_v8; retrieved 2026-10-25T17:34:02+00:00)

> 0 significant GTEx v8 single-tissue eQTLs for chr14_55887040_C_T_b38. NES is the effect of the alt allele (T) relative to ref (C).

<a id="e08"></a>**E08** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=PELI2%20AND%20%22breast%20cancer%22&format=json&pageSize=8&resultType=core; retrieved 2026-10-25T17:32:50+00:00)

> Europe PMC: 178 hits for 'PELI2 AND "breast cancer"'; top 7 with PMIDs:
> PMID 41023515 (2025): Pellino ubiquitin ligases: double-edged swords in hematologic malignancies-from oncogenic stabilizers to therapeutic vulnerabilities.
> PMID 41331176 (2025): Construction and validation of risk models of prognostic genes associated with parthanatos in papillary thyroid carcinoma based on bioinformatics.
> PMID 40362379 (2025): &lt;i&gt;O&lt;/i&gt;-Desmethyltramadol Enhanced Anti-Cancer Efficacy over Tramadol Through Non-μ-Opioid Receptor and Differential Cellular Contexts of Human Breast Cancer Cells.
> PMID 42757486 (2026): Pemetrexed increases BRCA1 protein stability and sensitizes TNBC cells to radiotherapy.
> PMID 42734444 (2027): Anesthesia inhalation agent sevoflurane induces perioperative cognitive impairment: Apelin/early growth response 1 axis induces ferritinophagy and exacerbates ferroptosis.
> PMID 41079921 (2025): PRMT1/PRMT5-Mediated Differential Arginine Methylation of CRIP1 Promotes the Recurrence of Small Cell Lung Cancer after Chemotherapy.
> PMID 42380137 (2026): HOXC9 accelerates esophageal squamous cell carcinoma progression via OTUD1-FABP5-mediated lipid metabolic reprogramming.

<a id="e08a"></a>**E08a** literature_search, Europe PMC abstract, PMID 41331176 (https://europepmc.org/article/MED/41331176; retrieved 2026-10-25T17:32:50+00:00)

> ResultsSeven prognostic genes (TSHZ3, SERGEF, AKAP12, SGPP2, ASGR1, AK1, PELI2) were identified.

<a id="e09"></a>**E09** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-26T00:36:39+00:00)

> No ENCODE ESR1 ChIP-seq peak contains chr14:55887040:C>T in biosamples matching 'MCF-7'. Absence can also mean no ESR1 experiment in that biosample. 0 peaks lie within 100 bp without containing it.

<a id="e10"></a>**E10** gene_disease, Open Targets Platform (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-25T17:34:03+00:00)

> Open Targets: PELI2 and breast cancer (MONDO_0007254), overall score 0.00; by evidence type: literature 0.01

<a id="e11"></a>**E11** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=PELI2%20breast%20cancer%20regulatory%20variant&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T20:24:13+00:00)

> Europe PMC: 33 hits for 'PELI2 breast cancer regulatory variant'; top 8 with PMIDs:
> PMID 41331176 (2025): Construction and validation of risk models of prognostic genes associated with parthanatos in papillary thyroid carcinoma based on bioinformatics.
> PMID 42060612 (2026): Unraveling the role of ChREBP in lung adenocarcinoma: Expression, regulatory networks, and potential functional impact.
> PMID 42272870 (2026): T-cell-targeted immunotherapy in neurofibromatosis type 2-related vestibular schwannoma: current evidence and future direction.
> PMID 41716334 (2026): Nanomedicine-based lactate metabolism and lactylation regulation for exploring new therapeutic strategies in cancer.
> PMID 38453895 (2024): Isoform alterations in the ubiquitination machinery impacting gastrointestinal malignancies.
> PMID 40830878 (2025): The components and regulation of the Hippo pathway and its relationships with the progression and treatment of Non-small cell lung cancer (NSCLC).
> PMID 41009541 (2025): Kinesin Spindle Protein (KIF11) in Mitosis and Cancer.
> PMID 41049757 (2025): &lt;i&gt;USP20&lt;/i&gt; as a super-enhancer-regulated gene drives T-ALL progression &lt;i&gt;via&lt;/i&gt; HIF1A deubiquitination.

<a id="e11a"></a>**E11a** literature_search, Europe PMC abstract, PMID 41331176 (https://europepmc.org/article/MED/41331176; retrieved 2026-10-26T20:24:13+00:00)

> Seven prognostic genes (TSHZ3, SERGEF, AKAP12, SGPP2, ASGR1, AK1, PELI2) were identified.
