# rs11629191 and Breast cancer

Configuration `no_qbic`, named mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.02 over 8 model calls; 159 s.

Variant `chr14:55887040:C>T` (germline); expression context: DepMap:ACH-000019 (MCF7).

## Ranked chains

### 1. null_no_tf_effect: Null hypothesis: no TF-mediated effect of rs11629191 (p = 0.95)

Null chain: no TF-mediated effect of this variant.

Predictions: No allele-specific transcription-factor ChIP-seq signal at chr14:55887040 in MCF-7 or other ENCODE biosamples.; No reproducible C-versus-T difference in chromatin accessibility, reporter activity, or nearby gene expression.; Any breast-cancer association at this locus would be attributable to a linked causal variant rather than to this base.

Falsified if: Allele-specific ChIP-seq or reporter assays show a reproducible TF-dependent effect of C versus T at this exact base.; A matched breast-cancer eQTL or chromatin assay shows an allele effect that is abolished when the site is mutated.

### 2. foxa1_cryptic_enhancer_peli2: FOXA1 binds the alt T allele more strongly at a cryptic intronic enhancer and distally up-regulates PELI2 (p = 0.03)

TF FOXA1 (QBiC-SELEX coverage own_model), alt allele binds more; element cryptic intronic enhancer; gene PELI2; cell type MCF-7 breast-cancer cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The hypothesis posits that FOXA1 binds the alt T allele more strongly, but no QBiC-SELEX model or allele-specific binding data are supplied for FOXA1 in this case; E04 reports no ENCODE ChIP-seq peak over this base in any biosample, including MCF-7, and E09 specifically reports no FOXA1 ChIP-seq peak in MCF-7. The binding claim is therefore speculative and unsupported. | missing | [E04](#e04), [E09](#e09) |
| element | The variant would have to create or alter a cryptic FOXA1-responsive enhancer; E01 shows an intronic variant with GERP -3.12, not evidence of conservation, and E03 shows no overlapping cCRE, with the nearest dELS 1868 bp away. No cryptic enhancer activity or allele-dependent regulatory effect is demonstrated. | missing | [E01](#e01), [E03](#e03) |
| gene | The cryptic enhancer would distally up-regulate PELI2, the nearest protein-coding gene at 230.8 kb; this long-range linkage is unproven. E02 gives linear distance only, E07 reports no significant GTEx v8 eQTL for this variant, and E06 is a weak brain molecular QTL for a different non-coding gene ENSG00000259868 (PIP 0.03), not PELI2 in MCF-7. | missing | [E02](#e02), [E06](#e06), [E07](#e07) |
| cell_type | The proposed effect occurs in MCF-7 breast-cancer cells, but E04 reports no ENCODE TF ChIP-seq peak over this base in MCF-7 and E09 reports no FOXA1 ChIP-seq peak in MCF-7; FOXA1 occupancy and allele-specific activity in this cell type are not demonstrated. | missing | [E04](#e04), [E09](#e09) |
| phenotype | PELI2 dysregulation is proposed to contribute to breast cancer. E08a supports Pellino-family E3 ubiquitin-ligase identity, E08b lists PELI2 among prognostic genes in papillary thyroid carcinoma, E08c concerns tramadol in breast cancer cells without PELI2, and E08d concerns BRCA1. None establishes PELI2 dysregulation as contributing to breast cancer at this locus. | missing | [E08a](#e08a), [E08b](#e08b), [E08c](#e08c), [E08d](#e08d) |

Predictions: Allele-specific FOXA1 ChIP-qPCR in MCF-7 shows higher FOXA1 occupancy on the T allele.; A reporter carrying T has higher activity than C in MCF-7 cells if the element is an enhancer.; PELI2 expression is higher with the T allele if the element is an enhancer.

Falsified if: No allele-specific FOXA1 occupancy is detected at this base.; Reporter assays show no C-versus-T difference.; PELI2 expression does not differ by allele in MCF-7 cells.

### 3. esr1_cryptic_silencer_peli2: ESR1 binds the ref C allele more strongly at a cryptic intronic silencer and represses PELI2 (p = 0.02)

TF ESR1 (QBiC-SELEX coverage own_model), ref allele binds more; element cryptic intronic silencer; gene PELI2; cell type MCF-7 breast-cancer cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The hypothesis posits that ESR1 binds the ref C allele more strongly, but no QBiC-SELEX model or allele-specific binding data are supplied for ESR1 in this case; E04 reports no ENCODE ChIP-seq peak over this base in any biosample, including MCF-7, and E10 specifically reports no ESR1 ChIP-seq peak in MCF-7. The binding claim is therefore speculative and unsupported. | missing | [E04](#e04), [E10](#e10) |
| element | The variant would have to create or alter a cryptic ESR1-responsive silencer; E01 shows an intronic variant with GERP -3.12, not evidence of conservation, and E03 shows no overlapping cCRE, with the nearest dELS 1868 bp away. No cryptic silencer activity or allele-dependent regulatory effect is demonstrated. | missing | [E01](#e01), [E03](#e03) |
| gene | The cryptic silencer would distally repress PELI2, the nearest protein-coding gene at 230.8 kb; this long-range linkage is unproven. E02 gives linear distance only, E07 reports no significant GTEx v8 eQTL for this variant, and E06 is a weak brain molecular QTL for a different non-coding gene ENSG00000259868 (PIP 0.03), not PELI2 in MCF-7. | missing | [E02](#e02), [E06](#e06), [E07](#e07) |
| cell_type | The proposed effect occurs in MCF-7 breast-cancer cells, but E04 reports no ENCODE TF ChIP-seq peak over this base in MCF-7 and E10 reports no ESR1 ChIP-seq peak in MCF-7; ESR1 occupancy and allele-specific activity in this cell type are not demonstrated. | missing | [E04](#e04), [E10](#e10) |
| phenotype | PELI2 dysregulation is proposed to contribute to breast cancer. E08a supports Pellino-family E3 ubiquitin-ligase identity, E08b lists PELI2 among prognostic genes in papillary thyroid carcinoma, E08c concerns tramadol in breast cancer cells without PELI2, and E08d concerns BRCA1. None establishes PELI2 dysregulation as contributing to breast cancer at this locus. | missing | [E08a](#e08a), [E08b](#e08b), [E08c](#e08c), [E08d](#e08d) |

Predictions: Allele-specific ESR1 ChIP-qPCR in MCF-7 shows higher ESR1 occupancy on the C allele.; A reporter carrying C has lower activity than T in MCF-7 cells if the element is a silencer.; PELI2 expression is lower with the C allele if ESR1 represses through this element.

Falsified if: No allele-specific ESR1 occupancy is detected at this base.; Reporter assays show no C-versus-T difference.; PELI2 expression does not differ by allele in MCF-7 cells.

## Prediction matrix

| Test | Cost | Separates top two | null_no_tf_effect | foxa1_cryptic_enhancer_peli2 | esr1_cryptic_silencer_peli2 |
| --- | --- | --- | --- | --- | --- |
| Allele-specific FOXA1 ChIP-qPCR in MCF-7 at rs11629191 | low | yes | No FOXA1 occupancy over the base, or no C-versus-T difference | FOXA1 occupancy is higher on the T allele | No FOXA1 occupancy over the base, or no C-versus-T difference |
| Allele-specific ESR1 ChIP-qPCR in MCF-7 at rs11629191 | low | no | No ESR1 occupancy over the base, or no C-versus-T difference | No ESR1 occupancy over the base, or no C-versus-T difference | ESR1 occupancy is higher on the C allele |
| Allele-specific reporter assay for C versus T in MCF-7 | medium | yes | No reproducible C-versus-T difference in reporter activity | The T allele gives higher reporter activity if the element is an enhancer | The C allele gives lower reporter activity if the element is a silencer |
| PELI2 expression by genotype in MCF-7 or breast eQTL data | high | yes | No reproducible allele-dependent PELI2 expression difference | PELI2 expression is higher with the T allele if the element is an enhancer | PELI2 expression is lower with the C allele if ESR1 represses through this element |

## Next experiment

Allele-specific FOXA1 ChIP-qPCR in MCF-7 at rs11629191

## Investigate calls

- chip_peaks({"tf": "FOXA1", "biosample": "MCF-7"})
- chip_peaks({"tf": "ESR1", "biosample": "MCF-7"})
- chip_peaks({"tf": "CTCF", "biosample": "MCF-7"})

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

<a id="e08a"></a>**E08a** literature_search, Europe PMC abstract, PMID 41023515 (https://europepmc.org/article/MED/41023515; retrieved 2026-10-25T17:32:50+00:00)

> The Pellino protein family is an evolutionarily conserved group of E3 ubiquitin ligases comprising Pellino1, Pellino2, and Pellino3.

<a id="e08b"></a>**E08b** literature_search, Europe PMC abstract, PMID 41331176 (https://europepmc.org/article/MED/41331176; retrieved 2026-10-25T17:32:50+00:00)

> Seven prognostic genes (TSHZ3, SERGEF, AKAP12, SGPP2, ASGR1, AK1, PELI2) were identified.

<a id="e08c"></a>**E08c** literature_search, Europe PMC abstract, PMID 40362379 (https://europepmc.org/article/MED/40362379; retrieved 2026-10-25T17:32:50+00:00)

> Hence, we sought to examine whether the cytotoxic effect of O-desmethyltramadol was better than tramadol on breast cancer cells.

<a id="e08d"></a>**E08d** literature_search, Europe PMC abstract, PMID 42757486 (https://europepmc.org/article/MED/42757486; retrieved 2026-10-25T17:32:50+00:00)

> Although pathogenic BRCA1 mutations are relatively uncommon, decreased BRCA1 protein expression, which is typically driven by accelerated proteasomal degradation, is implicated in aggressive breast cancer (BC), particularly triple‑negative (TN)BC.

<a id="e09"></a>**E09** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-26T00:28:52+00:00)

> No ENCODE FOXA1 ChIP-seq peak contains chr14:55887040:C>T in biosamples matching 'MCF-7'. Absence can also mean no FOXA1 experiment in that biosample. 0 peaks lie within 100 bp without containing it.

<a id="e10"></a>**E10** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-26T00:36:39+00:00)

> No ENCODE ESR1 ChIP-seq peak contains chr14:55887040:C>T in biosamples matching 'MCF-7'. Absence can also mean no ESR1 experiment in that biosample. 0 peaks lie within 100 bp without containing it.

<a id="e11"></a>**E11** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-26T00:28:52+00:00)

> No ENCODE CTCF ChIP-seq peak contains chr14:55887040:C>T in biosamples matching 'MCF-7'. Absence can also mean no CTCF experiment in that biosample. 0 peaks lie within 100 bp without containing it.
