# rs11629191 and Breast cancer

Configuration `no_qbic`, masked mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.02 over 7 model calls; 97 s.

Variant `chr14:55887040:C>T` (germline); expression context: DepMap:ACH-000019 (MCF7).

## Ranked chains

### 1. H1: No TF-mediated allelic effect at chr14:55887040:C>T (p = 0.93)

Null chain: no TF-mediated effect of this variant.

Predictions: No allele-specific TF binding at chr14:55887040 in MCF7 or other breast cells.; The variant remains outside annotated cCREs and has no ENCODE ChIP-seq peak containing it.; The weak molecular-QTL signal (PIP 0.03 for ENSG00000259868 in brain) does not replicate as a breast-cancer eQTL and is not explained by this base.; Any disease association would be due to a linked causal variant or passenger event, not direct TF binding at chr14:55887040.

Falsified if: A strong allele-specific ChIP-seq or QBiC-SELEX effect is shown for an expressed TF in MCF7 at this exact position.; The variant is placed in a validated MCF7 cCRE/enhancer that physically contacts a breast-cancer target gene.; A replicated breast-cancer eQTL or GWAS signal maps to this variant rather than a linked variant.

### 2. H2: ESR1 binds the alt allele in a latent MCF7 regulatory element upstream of PELI2 (p = 0.03)

TF ESR1 (QBiC-SELEX coverage own_model), alt allele binds more; element latent intronic/intergenic element at chr14:55887040; gene PELI2; cell type MCF7 breast cancer cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | ESR1 is a lineage-plausible MCF7 breast-cancer TF, but E09 reports no ESR1 ChIP-seq peak containing the variant in MCF7, E03 reports no cCRE overlap, and no QBiC-SELEX model for ESR1 is provided. If ESR1 bound here, the alt T allele is proposed to bind more strongly, but this is speculative and not supported by occupancy or SELEX. | missing | [E03](#e03), [E04](#e04), [E09](#e09) |
| element | The variant is intronic/intergenic with no overlapping cCRE; the nearest dELS is 1868 bp away, so this would have to be a cryptic or poorly annotated element rather than a demonstrated regulatory element. | missing | [E01](#e01), [E03](#e03) |
| gene | PELI2 is the nearest protein-coding gene at 230.8 kb, but there is no significant GTEx v8 single-tissue eQTL for this variant and the only credible-set signal is a very weak brain molecular QTL for ENSG00000259868 (PIP 0.03), not PELI2. | missing | [E02](#e02), [E06](#e06), [E07](#e07) |
| cell_type | MCF7 is the provided breast-cancer expression context, but E09 reports no ESR1 ChIP-seq peak at this site in MCF7, so MCF7-specific ESR1 occupancy is not shown. | missing | [E09](#e09) |
| phenotype | PELI2 has generic cancer literature and is included in a prognostic gene set, but there is no variant-specific evidence connecting this site to breast-cancer risk or progression. | missing | [E05](#e05), [E08](#e08), [E08a](#e08a), [E08b](#e08b) |

Predictions: ESR1 ChIP-qPCR in MCF7 should show occupancy at this position, with stronger binding to the alt T allele than the ref C allele.; The alt T allele should increase ESR1-dependent reporter activity in MCF7 if the element is active.; The element should contact PELI2 in MCF7 chromatin-contact assays.

Falsified if: No ESR1 occupancy is detected at the variant in MCF7.; Allele-specific assays show no ESR1 difference or show ref-binding more than alt.; The element does not contact or regulate PELI2 in MCF7.

### 3. H3: FOXA1 binds the ref allele at a cryptic element and represses PELI2 (p = 0.03)

TF FOXA1 (QBiC-SELEX coverage own_model), ref allele binds more; element cryptic intronic/intergenic element at chr14:55887040; gene PELI2; cell type MCF7 breast cancer cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | FOXA1 is a major MCF7/breast-cancer TF, but E10 reports no FOXA1 ChIP-seq peak containing the variant in MCF7, E03 reports no cCRE overlap, and no QBiC-SELEX model for FOXA1 is provided. If FOXA1 bound here, the ref C allele is proposed to bind more strongly, but this is speculative and not supported. | missing | [E03](#e03), [E04](#e04), [E10](#e10) |
| element | The variant has no annotated regulatory feature and is 1868 bp from the nearest dELS, so it would need to create or mark a cryptic element rather than lie in a known cCRE. | missing | [E01](#e01), [E03](#e03) |
| gene | PELI2 is the closest protein-coding gene but is 230.8 kb away; there is no significant GTEx v8 eQTL for this variant and no strong credible-set link to PELI2. | missing | [E02](#e02), [E06](#e06), [E07](#e07) |
| cell_type | MCF7 is a breast-cancer context in which FOXA1 is relevant, but E10 reports no FOXA1 ChIP-seq peak at this site in MCF7, so occupancy is not demonstrated. | missing | [E10](#e10) |
| phenotype | PELI2 cancer literature is not variant-specific, and there is no allele-specific breast-cancer phenotype evidence for this site. | missing | [E05](#e05), [E08](#e08), [E08a](#e08a), [E08b](#e08b) |

Predictions: FOXA1 ChIP-qPCR in MCF7 should show stronger binding to the ref C allele than the alt T allele at this position.; The element should have repressive regulatory activity in MCF7 that is FOXA1-sensitive.; PELI2 expression should change inversely with FOXA1 occupancy if FOXA1 represses.

Falsified if: FOXA1 does not occupy the variant in MCF7.; Allele-specific assays show alt binding more than ref, opposite to this chain.; No regulatory contact between this element and PELI2 is found in MCF7.

### 4. H4: CTCF binds the ref allele and alters insulation near a weak noncoding RNA signal (p = 0.01)

TF CTCF (QBiC-SELEX coverage own_model), ref allele binds more; element cryptic insulator element at chr14:55887040; gene ENSG00000259868; cell type MCF7 breast cancer cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | CTCF can bind intergenic sequence, but E11 reports no CTCF ChIP-seq peak containing the variant in MCF7, E03 reports no cCRE overlap, and no QBiC-SELEX model for CTCF is provided. If CTCF bound here, the ref C allele is proposed to bind more strongly, but this is speculative and not supported. | missing | [E03](#e03), [E04](#e04), [E11](#e11) |
| element | No annotated cCRE or insulator element overlaps the variant; the nearest dELS is far away, so a cryptic insulator is hypothetical rather than demonstrated. | missing | [E01](#e01), [E03](#e03) |
| gene | The only credible-set signal is a weak brain eQTL for ENSG00000259868 (PIP 0.03), with no significant GTEx v8 single-tissue eQTL and no breast-context link. | weak | [E06](#e06), [E07](#e07) |
| cell_type | MCF7 is the breast-cancer context, but E11 reports no CTCF ChIP-seq peak at this site in MCF7, so MCF7 CTCF occupancy is not shown. | missing | [E11](#e11) |
| phenotype | There are zero GWAS Catalog associations for this variant and no variant-specific breast-cancer evidence linking ENSG00000259868 or CTCF binding at this site to disease. | missing | [E05](#e05), [E06](#e06) |

Predictions: CTCF ChIP-qPCR in MCF7 should show occupancy at this position, with stronger binding to the ref C allele than the alt T allele.; The variant should alter local chromatin insulation or contact in MCF7.; The effect should track with ENSG00000259868 or another nearby gene in breast cells, not only brain.

Falsified if: No CTCF occupancy is detected at the variant in MCF7.; CTCF binding is not allele-specific or favors alt.; Chromatin contact/insulation assays show no change near this site.

## Prediction matrix

| Test | Cost | Separates top two | H1 | H2 | H3 | H4 |
| --- | --- | --- | --- | --- | --- | --- |
| Allele-specific ESR1 ChIP-qPCR in MCF7 at chr14:55887040 | low | yes | No ESR1 occupancy and no allelic imbalance. | ESR1 occupancy with stronger binding to the alt T allele. | No ESR1 occupancy; this chain makes no ESR1-binding prediction. | No ESR1 occupancy; this chain makes no ESR1-binding prediction. |
| Allele-specific FOXA1 ChIP-qPCR in MCF7 at chr14:55887040 | low | no | No FOXA1 occupancy and no allelic imbalance. | No FOXA1 occupancy; this chain makes no FOXA1-binding prediction. | FOXA1 occupancy with stronger binding to the ref C allele. | No FOXA1 occupancy; this chain makes no FOXA1-binding prediction. |
| Allele-specific CTCF ChIP-qPCR in MCF7 at chr14:55887040 | low | no | No CTCF occupancy and no allelic imbalance. | No CTCF occupancy; this chain makes no CTCF-binding prediction. | No CTCF occupancy; this chain makes no CTCF-binding prediction. | CTCF occupancy with stronger binding to the ref C allele. |
| MCF7 reporter assay with ref vs alt sequence at chr14:55887040, with and without ESR1 knockdown | medium | yes | No allele-specific reporter activity and no ESR1-dependent effect. | Alt T increases reporter activity in an ESR1-dependent manner. | Ref C changes reporter activity in a FOXA1-sensitive direction if the cryptic element is active. | No allele-specific reporter activity; any effect would be insulation/contact rather than enhancer activity. |

## Next experiment

Cheapest separating test: allele-specific ESR1 ChIP-qPCR in MCF7 at chr14:55887040. Existing E09 reports no ESR1 ChIP-seq peak in MCF7, but absence can mean no experiment; a targeted ChIP-qPCR with allele-specific primers directly tests H2 against H1.

## Investigate calls

- chip_peaks({"tf": "ESR1", "biosample": "MCF-7"})
- chip_peaks({"tf": "FOXA1", "biosample": "MCF-7"})
- chip_peaks({"tf": "CTCF", "biosample": "MCF-7"})

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

<a id="e08a"></a>**E08a** literature_search, Europe PMC abstract, PMID 41023515 (https://europepmc.org/article/MED/41023515; retrieved 2026-10-25T17:32:50+00:00)

> The Pellino protein family is an evolutionarily conserved group of E3 ubiquitin ligases comprising Pellino1, Pellino2, and Pellino3.

<a id="e08b"></a>**E08b** literature_search, Europe PMC abstract, PMID 41331176 (https://europepmc.org/article/MED/41331176; retrieved 2026-10-25T17:32:50+00:00)

> Seven prognostic genes (TSHZ3, SERGEF, AKAP12, SGPP2, ASGR1, AK1, PELI2) were identified.

<a id="e08c"></a>**E08c** literature_search, Europe PMC abstract, PMID 40362379 (https://europepmc.org/article/MED/40362379; retrieved 2026-10-25T17:32:50+00:00)

> Hence, we sought to examine whether the cytotoxic effect of O-desmethyltramadol was better than tramadol on breast cancer cells.

<a id="e08d"></a>**E08d** literature_search, Europe PMC abstract, PMID 42757486 (https://europepmc.org/article/MED/42757486; retrieved 2026-10-25T17:32:50+00:00)

> Although pathogenic BRCA1 mutations are relatively uncommon, decreased BRCA1 protein expression, which is typically driven by accelerated proteasomal degradation, is implicated in aggressive breast cancer (BC), particularly triple‑negative (TN)BC.

<a id="e09"></a>**E09** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-26T00:36:39+00:00)

> No ENCODE ESR1 ChIP-seq peak contains chr14:55887040:C>T in biosamples matching 'MCF-7'. Absence can also mean no ESR1 experiment in that biosample. 0 peaks lie within 100 bp without containing it.

<a id="e10"></a>**E10** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-26T00:28:52+00:00)

> No ENCODE FOXA1 ChIP-seq peak contains chr14:55887040:C>T in biosamples matching 'MCF-7'. Absence can also mean no FOXA1 experiment in that biosample. 0 peaks lie within 100 bp without containing it.

<a id="e11"></a>**E11** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-26T00:28:52+00:00)

> No ENCODE CTCF ChIP-seq peak contains chr14:55887040:C>T in biosamples matching 'MCF-7'. Absence can also mean no CTCF experiment in that biosample. 0 peaks lie within 100 bp without containing it.
