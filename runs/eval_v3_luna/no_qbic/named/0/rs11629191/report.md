# rs11629191 and Breast cancer

Configuration `no_qbic`, named mode, seed 0. Models: generator openai/gpt-6-luna, critic openai/gpt-6-luna, summariser openai/gpt-6-luna. Cost $0.01 over 7 model calls; 129 s.

Variant `chr14:55887040:C>T` (germline); expression context: DepMap:ACH-000019 (MCF7).

## Ranked chains

### 1. H0: No TF-mediated effect of rs11629191 (p = 0.99)

Null chain: no TF-mediated effect of this variant.

Predictions: C-to-T editing will not reproducibly change TF occupancy or regulatory output attributable to this base.; Any future association with breast cancer could reflect another variant or a mechanism other than TF binding at rs11629191.

Falsified if: Allele-specific experiments show a reproducible TF occupancy difference at this site and a linked regulatory effect that depends on the variant.

### 2. H1: Speculative ESR1-mediated effect on PELI2 (p = 0.00)

TF ESR1 (QBiC-SELEX coverage own_model), alt allele binds more; element Unannotated regulatory sequence at or near the variant (unverified); gene PELI2; cell type MCF7.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The testable hypothesis is that ESR1 binds T more strongly than C, but this direction is unsupported: no QBiC-SELEX result or variant-overlapping ChIP-seq peak is reported. ESR1 expression makes it a plausible candidate in MCF7, not evidence of occupancy at this base. | missing | [E04](#e04), [E10](#e10) |
| element | This chain requires an unannotated regulatory sequence because no cCRE overlaps the variant; the evidence does not establish that such an element functions here. | missing | [E03](#e03) |
| gene | PELI2 is only a candidate target because it is the nearest listed protein-coding gene; no supplied evidence links it to regulation by this variant. | weak | [E02](#e02) |
| cell_type | MCF7 is a proposed context because ESR1 is highly expressed there, but no TF peak over the variant was found in this biosample. | weak | [E04](#e04), [E10](#e10) |
| phenotype | The proposed downstream effect is increased breast-cancer risk if greater ESR1 binding increases PELI2 expression; neither this regulatory direction nor a link to risk is established by the supplied evidence. | missing | [E05](#e05), [E11](#e11) |

Predictions: Relative to H0, allele-specific ESR1 assays will show greater binding to T than C.; Under this chain's unverified activating-element assumption, T will increase PELI2 expression; disrupting ESR1 or editing T back to C will reduce that effect.

Falsified if: A sensitive allele-specific assay finds no greater ESR1 binding to T than C.; Variant editing or ESR1 perturbation does not produce the predicted linked change in PELI2 expression.

### 3. H2: Very weak alternative: FOXA1-mediated effect on PELI2 (p = 0.00)

TF FOXA1 (QBiC-SELEX coverage own_model), ref allele binds more; element Unannotated regulatory sequence at or near the variant (unverified); gene PELI2; cell type MCF7.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The testable hypothesis is that FOXA1 binds C more strongly than T, but the direction is unsupported: no QBiC-SELEX result or variant-overlapping ChIP-seq peak is reported, and the supplied evidence does not establish FOXA1 occupancy or expression in MCF7. | missing | [E04](#e04) |
| element | This chain requires an unannotated regulatory sequence because no cCRE overlaps the variant; the evidence does not establish that such an element functions here. | missing | [E03](#e03) |
| gene | PELI2 is only a candidate target based on proximity; no supplied evidence connects it to this variant. | weak | [E02](#e02) |
| cell_type | MCF7 is a proposed context, but the supplied evidence shows no TF peak over the variant there and gives no FOXA1 expression evidence for this line. | missing | [E04](#e04) |
| phenotype | The proposed downstream effect is reduced breast-cancer risk if greater FOXA1 binding represses PELI2; neither this regulatory direction nor a link to risk is established by the supplied evidence. | missing | [E05](#e05), [E11](#e11) |

Predictions: Relative to H0, allele-specific FOXA1 assays will show greater binding to C than T.; Under this chain's unverified repressive-element assumption, C will reduce PELI2 expression; disrupting FOXA1 or editing C to T will remove that effect.

Falsified if: A sensitive allele-specific assay finds no greater FOXA1 binding to C than T.; Variant editing or FOXA1 perturbation does not produce the predicted linked change in PELI2 expression.

## Prediction matrix

| Test | Cost | Separates top two | H0 | H1 | H2 |
| --- | --- | --- | --- | --- | --- |
| Allele-specific EMSA using C and T probes with MCF7 nuclear extract and an ESR1-specific supershift or depletion control. | low | yes | No reproducible ESR1-dependent binding difference between the C and T probes. | Greater ESR1-dependent binding to the T probe than the C probe. | No predicted ESR1-specific T-over-C difference; this chain instead predicts greater FOXA1 binding to C. |
| Isogenic C-to-T editing in MCF7 cells followed by ESR1 and FOXA1 occupancy assays and PELI2 expression measurement. | high | yes | No reproducible variant-dependent occupancy or PELI2 expression change. | T increases ESR1 occupancy and, under the proposed activating-element assumption, PELI2 expression. | C increases FOXA1 occupancy and, under the proposed repressive-element assumption, reduces PELI2 expression. |

## Next experiment

The cheapest test separating the top two hypotheses (H0 and H1) is the allele-specific ESR1 EMSA with an ESR1-specific supershift or depletion control. It directly tests H1's proposed T-over-C binding difference; a positive result would motivate, but would not by itself establish, the proposed element-to-PELI2-to-disease chain.

## Investigate calls

- literature_search({"query": "rs11629191"})
- tf_expression({"tf": "ESR1", "context": "DepMap:ACH-000019"})
- gene_disease({"gene": "PELI2"})

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

<a id="e09"></a>**E09** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=rs11629191&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T13:27:54+00:00)

> Europe PMC: 0 hits for 'rs11629191'; top 0 with PMIDs:

<a id="e10"></a>**E10** tf_expression, DepMap expression / GTEx v8 medians (local files; retrieved local)

> ESR1 in DepMap line ACH-000019: 48.18 TPM, rank 69 of 1626 TFs (1 = highest); this context is at the 99.5th percentile of ESR1 across all DepMap lines.

<a id="e11"></a>**E11** gene_disease, Open Targets Platform (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-25T17:34:03+00:00)

> Open Targets: PELI2 and breast cancer (MONDO_0007254), overall score 0.00; by evidence type: literature 0.01
