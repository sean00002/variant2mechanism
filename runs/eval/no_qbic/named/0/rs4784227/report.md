# rs4784227 and Breast cancer (16q12)

Configuration `no_qbic`, named mode, seed 0. Models: generator claude-opus-5, critic claude-sonnet-5-5, summariser claude-haiku-5-5. Cost $0.56 over 8 model calls; 169 s.

Variant `chr16:52565276:C>T` (germline); expression context: DepMap:ACH-000019 (MCF7).

## Ranked chains

### 1. H1: Risk allele T strengthens FOXA1 binding at the TOX3 distal enhancer, altering TOX3 expression in breast epithelium (p = 0.42)

TF FOXA1 (stated coverage not_checked; registry own_model), alt allele binds more; element EH38E3180851 (dELS distal enhancer, chr16:52565011-52565360; Ensembl regulatory feature ENSR16_9QTBS); gene TOX3; cell type Breast epithelium, modelled by MCF7 (DepMap ACH-000019).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | A FOXA1 ChIP-seq peak in MCF-7 contains the variant (ENCSR126YEB), and the published hypothesis for this locus is that the SNP changes the FOXA1 recognition sequence and increases FOXA1 binding affinity; the forkhead family member is named FOXA1 because it is the forkhead factor whose ChIP peak actually overlaps the site in MCF-7 and in liver/A549/HepG2. No QBiC-SELEX row or lookup for FOXA1 was available, so coverage is not_checked; the allele direction (T binds more) comes only from the literature assertion in E07b, not from any allele-resolved assay here. | weak | [E08](#e08), [E07a](#e07a), [E07b](#e07b) |
| element | The variant lies inside a distal enhancer-like cCRE (EH38E3180851) with high H3K27ac (z 6.1) and DNase (z 4.2) and low H3K4me3, i.e. enhancer not promoter; z-scores are maxima across biosamples, so MCF7-specific activity is not demonstrated, though the FOXA1 peak in MCF-7 indicates the region is accessible there. | supported | [E01](#e01), [E03](#e03), [E08](#e08) |
| gene | TOX3 is the prioritised target: top L2G gene (0.92-0.96) in multiple breast-cancer credible sets and nearest protein-coding TSS (17.5 kb); this is genetic prioritisation plus a review assertion, not contact or perturbation data, and the host lncRNA CASC16 is not excluded. | weak | [E02](#e02), [E05](#e05), [E06a](#e06a) |
| cell_type | The relevant cells are breast epithelium generally rather than strictly luminal: the association is seen for ER-positive/luminal A and also ER-negative disease; MCF7 is used because the only matching FOXA1 peak evidence is in MCF-7. | weak | [E04](#e04), [E05](#e05), [E08](#e08) |
| phenotype | The T allele is the risk allele at a genome-wide significant breast-cancer locus (p 2e-240; meta-analysis supports T-allele risk); mediation through TOX3 dosage and its direction are not demonstrated, and there is no significant breast eQTL for this variant. | weak | [E04](#e04), [E06b](#e06b), [E09](#e09) |

Predictions: Reanalysis of ENCODE MCF-7 FOXA1 ChIP-seq reads at chr16:52565276 shows T-allele-biased reads if MCF-7 is heterozygous; allele-specific FOXA1 ChIP in heterozygous primary/organoid cells shows excess T reads; FOXA1 knockdown removes the allelic enhancer difference and lowers TOX3 expression; Isogenic C>T editing in MCF7 raises FOXA1 occupancy at the element and changes TOX3, not CASC16-only, expression; QBiC-SELEX forkhead models predict increased affinity for the T allele

Falsified if: Allele-specific FOXA1 ChIP shows equal or C-biased occupancy; CRISPR C>T editing leaves FOXA1 occupancy and TOX3 expression unchanged; Mutating the forkhead core in the element does not abolish the allelic reporter difference

### 2. H5: Null: no TF-mediated effect of rs4784227 itself (p = 0.30)

Null chain: no TF-mediated effect of this variant.

Predictions: Editing only rs4784227 in an isogenic background changes neither enhancer activity nor TOX3/CASC16 expression; No allele-specific read imbalance in MCF-7 FOXA1 ChIP-seq at the position; A different variant in the same strong-LD block carries the causal allelic activity; Consistent with no significant breast-mammary eQTL for this variant (E09)

Falsified if: Isogenic C>T editing reproducibly alters TOX3/CASC16 expression or enhancer activity; Reproducible allele-specific TF ChIP signal at the site

### 3. H6: Same FOXA1 allelic binding event, but the regulated product is the CASC16 lncRNA rather than TOX3 protein-coding output (p = 0.13)

TF FOXA1 (stated coverage not_checked; registry own_model), alt allele binds more; element EH38E3180851 dELS; intronic to CASC16 (ENSR16_9QTBS); gene CASC16; cell type Breast epithelium (MCF7).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | Identical binding step to H1: a FOXA1 peak in MCF-7 overlaps the variant and the literature proposes an altered FOXA1 recognition sequence with higher affinity for the variant allele; FOXA1 chosen because it is the only forkhead factor with peak evidence at the site. Coverage not_checked. | weak | [E08](#e08), [E07b](#e07b) |
| element | The variant is an intronic position of the CASC16 non-coding transcript that also falls in a distal enhancer-like cCRE, so the element can act internally to the lncRNA unit. | supported | [E01](#e01), [E03](#e03) |
| gene | CASC16 hosts the variant and is the gene named in the association literature for this SNP; no breast eQTL distinguishes CASC16 from TOX3, and L2G prioritises TOX3 only from genetic mapping. | weak | [E01](#e01), [E06b](#e06b), [E05](#e05), [E09](#e09) |
| cell_type | Breast epithelium across ER subtypes, consistent with the association being present in both ER-positive and ER-negative disease. | weak | [E04](#e04) |
| phenotype | Altered CASC16 transcription on the T allele modifies breast cancer risk; direction and mediation are not shown by any cited data. | weak | [E04](#e04), [E06b](#e06b) |

Predictions: Isogenic editing changes CASC16 transcript level or isoform usage with little or no change in TOX3 mRNA; CASC16 knockdown, not TOX3 knockdown, reproduces the allele-associated transcriptional phenotype; Capture-C/HiC shows no enhancer-TOX3 promoter contact gain on the T allele

Falsified if: Editing changes TOX3 mRNA without changing CASC16; CASC16 depletion has no effect while TOX3 depletion does

### 4. H4: The ref C allele preserves a TFAP2C site that the T allele weakens, lowering enhancer output (p = 0.08)

TF TFAP2C (stated coverage not_checked; registry own_model), ref allele binds more; element EH38E3180851 distal enhancer-like cCRE; gene TOX3; cell type Breast epithelium, ER-positive and ER-negative.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | No evidence cited shows an AP-2 motif or TFAP2C occupancy here; the paralogue choice and the C-preferring direction are prior assumptions, retained to represent the opposite-direction possibility (the risk allele reducing binding). Coverage not_checked. | missing | none |
| element | The variant lies in an active distal enhancer-like cCRE. | weak | [E03](#e03) |
| gene | The element is assigned to TOX3 by L2G and proximity, with CASC16 overlapping it. | weak | [E01](#e01), [E02](#e02), [E05](#e05) |
| cell_type | A broad breast-epithelial factor fits the association being present in both ER-positive and ER-negative disease. | weak | [E04](#e04) |
| phenotype | Lower enhancer output on the T risk allele would reduce TOX3 and raise risk; direction is unsupported by any cited measurement, including the absent breast eQTL. | weak | [E04](#e04), [E09](#e09) |

Predictions: T allele reduces reporter activity relative to C; AP-2 occupancy at the element is C-biased; Allelic effect present in ER-negative lines

Falsified if: T allele increases enhancer activity or FOXA1 binding; No AP-2 occupancy at the element

### 5. H2: Allele-specific GATA3 binding at the same enhancer drives TOX3 regulation (p = 0.07)

TF GATA3 (stated coverage not_checked; registry own_model), alt allele binds more; element EH38E3180851 distal enhancer-like cCRE; gene TOX3; cell type ER-positive luminal breast epithelium (MCF7).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | No cited evidence shows a GATA motif or GATA3 occupancy at this position; GATA3 is named within the GATA family only as the luminal-breast paralogue, which is prior knowledge outside the evidence. Coverage not_checked. This chain is kept only as the main alternative luminal TF to the FOXA1 explanation. | missing | none |
| element | The variant sits in an active distal enhancer-like cCRE (H3K27ac z 6.1, DNase z 4.2), a plausible site for lineage TF binding. | weak | [E03](#e03) |
| gene | TOX3 is the top L2G gene at the locus and the nearest protein-coding TSS; enhancer-gene linkage is not directly shown. | weak | [E05](#e05), [E02](#e02) |
| cell_type | Luminal credible sets (luminal A, ER-positive) are present, but ER-negative association of similar strength argues against a strictly luminal mechanism. | weak | [E04](#e04), [E05](#e05) |
| phenotype | If GATA3 occupancy changed, altered TOX3 output could shift risk; no direction is demonstrated. | weak | [E04](#e04) |

Predictions: GATA3 ChIP shows T-allele bias while the overlapping FOXA1 peak is allele-neutral; GATA3 depletion, not FOXA1 depletion, removes the allelic reporter difference

Falsified if: No GATA3 peak overlaps the cCRE in MCF7; GATA3 knockdown leaves allelic enhancer activity intact

## Prediction matrix

| Test | Cost | Separates top two | H1 | H5 | H6 | H4 | H2 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Allelic-imbalance reanalysis of existing ENCODE MCF-7 FOXA1 ChIP-seq reads (ENCSR126YEB) at chr16:52565276 | existing data | yes | T-allele-biased reads (if heterozygous) | No imbalance beyond noise | T-allele-biased reads (same binding step) | C-allele-biased or no FOXA1 imbalance | No FOXA1 imbalance |
| QBiC-SELEX detail lookup for FOXA1 and forkhead group; allele-specific affinity prediction for C>T | existing data | yes | Forkhead model predicts higher affinity for T | No significant predicted affinity change | Same prediction as H1 | AP-2 model flagged with C preference | GATA model, not forkhead, flagged |
| Isogenic CRISPR C>T edit in MCF7 followed by RT-qPCR of TOX3 and CASC16 | high | yes | TOX3 changes | No change in either | CASC16 changes, TOX3 largely unchanged | TOX3 decreases | TOX3 changes (GATA3-dependent) |
| FOXA1 siRNA knockdown in MCF7 with allelic luciferase reporter for the 350 bp element | medium | no | Allelic difference lost, TOX3 falls | No allelic difference to begin with | Allelic difference lost, CASC16 falls | Allelic difference persists (AP-2 dependent) | Allelic difference persists |
| GATA3 and TFAP2C ChIP-seq peak overlap at EH38E3180851 in MCF7 | existing data | no | Irrelevant or co-binding without allelic effect | Peaks may exist but no allelic effect | Irrelevant | TFAP2C peak present | GATA3 peak present |
| Capture-C / promoter-capture HiC in MCF7 for contacts of the element with TOX3 vs CASC16 promoters | high | no | Contact with TOX3 promoter | Contacts unrelated to allele | Contact confined to CASC16 unit | Contact with TOX3 promoter | Contact with TOX3 promoter |
| TOX3 gene dependency in breast cancer lines (DepMap, ACH-000019) | existing data | no | Some TOX3 dependence expected but not required | Uninformative | TOX3 dependence not required | Same as H1 | Same as H1 |

## Next experiment

Reanalyse the existing ENCODE MCF-7 FOXA1 ChIP-seq data (ENCSR126YEB) for allele-specific reads at chr16:52565276 after genotyping MCF7 at the site: a reproducible T-allele read bias supports H1 (and H6) over the null, while balanced reads in a heterozygous line argues for H5. This costs nothing beyond analysis and directly tests the binding step that all current chains lack.

## Investigate calls

- literature_search({"query": "rs4784227 allele-specific transcription factor binding TOX3 enhancer FOXA1"})
- chip_peaks({"tf": "FOXA1", "biosample": "MCF-7"})
- eqtl_lookup({"tissue": "Breast - Mammary Tissue"})

## Flags

- none

Citation support: 0.90 of links cite only evidence that passed every check.

## Evidence

<a id="e01"></a>**E01** variant_annotation, Ensembl VEP (GRCh38) (https://rest.ensembl.org/vep/human/region/16:52565276-52565276:1/T?content-type=application/json&Conservation=1; retrieved 2026-10-25T17:26:24+00:00)

> Variant chr16:52565276:C>T (GRCh38), allele string C/T
> Known IDs: rs4784227
> Most severe consequence: intron_variant
> Regulatory features: ENSR16_9QTBS enhancer
> GERP conservation score at the site: -2
> Transcript consequences: CASC16 (intron_variant, non_coding_transcript_variant)

<a id="e02"></a>**E02** nearest_genes, Ensembl overlap (protein_coding) (https://rest.ensembl.org/overlap/region/human/16:51565276-53565276?feature=gene;biotype=protein_coding;content-type=application/json; retrieved 2026-10-25T17:25:47+00:00)

> 6 protein-coding genes within 1000 kb of chr16:52565276:C>T, by distance to TSS:
> TOX3: 17.5 kb from TSS (upstream, strand -1)
> CHD9NB: 487.6 kb from TSS (downstream, strand -1)
> CHD9: 489.7 kb from TSS (upstream, strand +1)
> RBL2: 868.7 kb from TSS (upstream, strand +1)
> AKTIP: 939.1 kb from TSS (downstream, strand -1)
> HNRNPA1L3: 1011.8 kb from TSS (downstream, strand +1)

<a id="e03"></a>**E03** ccre_lookup, ENCODE v4 cCRE registry (ENCFF420VPZ) and SCREEN (https://screen-beta-api.wenglab.org/dataws/cre_table; retrieved 2026-10-25T17:25:50+00:00)

> The variant lies in cCRE EH38E3180851 (dELS: distal enhancer-like), chr16:52565011-52565360.
> SCREEN: 1 cCREs within 500 bp (max z-score across ENCODE biosamples):
> EH38E3180851 dELS (contains the variant): DNase z 4.2, H3K27ac z 6.1, H3K4me3 z 1.8, CTCF z 1.9; nearby genes CASC16, TOX3, AC026462.5
> Biosample-specific z-scores are not in this call; the values above are maxima over biosamples.

<a id="e04"></a>**E04** gwas_lookup, GWAS Catalog REST v2 (https://www.ebi.ac.uk/gwas/rest/api/v2/associations?rs_id=rs4784227&size=100; retrieved 2026-10-25T17:26:28+00:00)

> 34 GWAS Catalog associations for rs4784227, strongest first:
> Breast cancer: p 2.0e-240, effect allele T, risk-allele frequency NR, PMID 32139696
> Postmenopausal breast cancer: p 5.0e-50, effect allele T, risk-allele frequency NR, PMID 38538606
> Breast cancer (estrogen-receptor negative): p 2.0e-26, effect allele T, risk-allele frequency 0.24, PMID 29058716
> Biological Mother:  Cancer, Breast: p 2.0e-25, effect allele C, risk-allele frequency 0.7783, PMID 39024449
> Breast cancer (estrogen-receptor positive): p 1.0e-13, effect allele T, risk-allele frequency 0.06, PMID 38741014
> Parkinson's disease: p 1.0e-10, effect allele T, risk-allele frequency 0.265, PMID 28892059
> Systolic blood pressure: p 1.0e-09, effect allele T, risk-allele frequency 0.2398, PMID 33230300
> BRCA1/2-negative high-risk breast cancer: p 2.0e-09, effect allele T, risk-allele frequency 0.26, PMID 30323354
> Pulse pressure: p 2.0e-08, effect allele T, risk-allele frequency 0.2354, PMID 33230300
> Cancer: p 3.0e-08, effect allele ?, risk-allele frequency NR, PMID 34290314

<a id="e05"></a>**E05** finemap_lookup, Open Targets Platform (credible sets, L2G) (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-25T17:26:25+00:00)

> 83 credible sets contain 16_52565276_C_T: 74 GWAS, 9 molecular QTL.
> GWAS Breast cancer: PIP 1.00; L2G TOX3 0.92
> GWAS Malignant neoplasm of breast, excluding all cancers (control: PIP 1.00; L2G TOX3 0.92
> GWAS Breast cancer: PIP 1.00; L2G TOX3 0.93
> GWAS Breast cancer (luminal A): PIP 1.00; L2G TOX3 0.92
> GWAS Malignant neoplasm of breast, ER-positive, excluding all can: PIP 1.00; L2G TOX3 0.92
> GWAS Breast cancer [female] (PheCode 174.1): PIP 1.00; L2G TOX3 0.92
> eqtl for ENSG00000285800 (gtex-v10_exon_brain_spinal_cord_ensg00000285800_1_): PIP 0.07
> eqtl for ENSG00000285800 (gtex-v10_ge_brain_hippocampus_ensg00000285800): PIP 0.06
> tuqtl for TOX3 (gtex-v10_txrev_brain_hippocampus_ensg00000103460_g): PIP 0.05
> eqtl for ENSG00000285800 (gtex-v10_ge_brain_spinal_cord_ensg00000285800): PIP 0.04
> tuqtl for TOX3 (gtex-v10_txrev_brain_substantia_nigra_ensg00000103): PIP 0.04
> eqtl for ENSG00000285800 (gtex-v10_exon_brain_hippocampus_ensg00000285800_1_): PIP 0.03
> Best L2G gene scores across these sets: TOX3 0.96

<a id="e06"></a>**E06** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=rs4784227%20AND%20TOX3%20AND%20%22breast%20cancer%22&format=json&pageSize=8&resultType=core; retrieved 2026-10-25T17:26:28+00:00)

> Europe PMC: 77 hits for 'rs4784227 AND TOX3 AND "breast cancer"'; top 8 with PMIDs:
> PMID 41230718 (2026): Cis-regulatory and long noncoding RNA alterations in breast cancer - current insights, biomarker utility, and the critical need for functional validation.
> PMID 40932605 (2025): Molecular signatures of breast cancer in the Iranian population: a review of cell growth and cell cycle regulators.
> PMID 42001218 (2026): Prioritizing context-specific genetic risk mechanisms in 11 solid cancers.
> PMID 36042591 (2022): Association between the rs4784227-CASC16 polymorphism and the risk of breast cancer: A meta-analysis.
> PMID 39777116 (2025): Identification of significant single-nucleotide polymorphisms associated with breast cancer recurrence and metastasis using GWAS.
> PMID 38741014 (2024): Genome-wide association analyses of breast cancer in women of African ancestry identify new susceptibility loci and improve risk prediction.
> PMID 39587695 (2024): The shared genetic landscape of polycystic ovary syndrome and breast cancer: convergence on ER + breast cancer but not ER- breast cancer.
> PMID 38902506 (2024): Hidden secrets of the cancer genome: unlocking the impact of non-coding mutations in gene regulatory elements.

<a id="e06a"></a>**E06a** literature_search, Europe PMC abstract, PMID 41230718 (https://europepmc.org/article/MED/41230718; retrieved 2026-10-25T17:26:28+00:00)

> Key examples include promoter mutations [e.g., rs2279744 (Mouse double minute 2 homolog gene; MDM2)], enhancer mutations [e.g., rs4784227 (thymocyte selection-associated high mobility group box family member 3 gene; TOX3)], and lncRNAs [e.g., HOX transcript antisense intergenic RNA (HOTAIR)] linked to progression, metastasis, and poor survival.

<a id="e06b"></a>**E06b** literature_search, Europe PMC abstract, PMID 36042591 (https://europepmc.org/article/MED/36042591; retrieved 2026-10-25T17:26:28+00:00)

> Our pooled analysis showed a significant association between the rs4784227- (T) allele and breast cancer susceptibility in Asian and North American populations, and intervention with this mutation might be a new therapeutic strategy for breast cancer.

<a id="e07"></a>**E07** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=rs4784227%20allele-specific%20transcription%20factor%20binding%20TOX3%20enhancer%20FOXA1&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T00:09:57+00:00)

> Europe PMC: 19 hits for 'rs4784227 allele-specific transcription factor binding TOX3 enhancer FOXA1'; top 8 with PMIDs:
> PMID 38902506 (2024): Hidden secrets of the cancer genome: unlocking the impact of non-coding mutations in gene regulatory elements.
> PMID 39777116 (2025): Identification of significant single-nucleotide polymorphisms associated with breast cancer recurrence and metastasis using GWAS.
> PMID 36042591 (2022): Association between the rs4784227-CASC16 polymorphism and the risk of breast cancer: A meta-analysis.
> PMID 31338012 (2019): Association of <i>rs4784227-CASC16 (LOC643714 locus)</i> and <i>rs4782447-ACSF3</i> polymorphisms and their association with breast cancer risk among Iranian population.
> PMID 35011637 (2021): Three-Dimensional Genome Organization in Breast and Gynecological Cancers: How Chromatin Folding Influences Tumorigenic Transcriptional Programs.
> PMID 32765587 (2020): ABC-GWAS: Functional Annotation of Estrogen Receptor-Positive Breast Cancer Genetic Variants.
> PMID 33919522 (2021): Genetic Variants in Transcription Factor Binding Sites in Humans: Triggered by Natural Selection and Triggers of Diseases.
> PMID 38314912 (2024): ChIP-GPT: a managed large language model for robust data extraction from biomedical database records.

<a id="e07a"></a>**E07a** literature_search, Europe PMC abstract, PMID 31338012 (https://europepmc.org/article/MED/31338012; retrieved 2026-10-26T00:09:57+00:00)

> TOX3 and FOXA1 proteins are believed to be involved in the susceptibility of breast cancer.

<a id="e07b"></a>**E07b** literature_search, Europe PMC abstract, PMID 31338012 (https://europepmc.org/article/MED/31338012; retrieved 2026-10-26T00:09:57+00:00)

> rs4784227-CASC16 and rs4782447-ACSF3, as single nucleotide polymorphisms (SNPs), located at the 16q may affect the FOXA1 DNA binding sequence change and therefore may enhance the FOXA1-binding affinity to the promoter of TOX3 gene.

<a id="e08"></a>**E08** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-25T17:27:50+00:00)

> 1 ENCODE FOXA1 ChIP-seq peaks contain chr16:52565276:C>T in biosamples matching 'MCF-7': biosamples MCF-7; experiments ENCSR126YEB. In other biosamples, 7 FOXA1 peaks do contain the variant: A549, HepG2, liver (experiments ENCSR000BLE, ENCSR000BMO, ENCSR000BRD, ENCSR324RCI, ENCSR735KEY, ENCSR865RXA).

<a id="e09"></a>**E09** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr16_52565276_C_T_b38&datasetId=gtex_v8; retrieved 2026-10-25T17:27:51+00:00)

> 0 significant GTEx v8 single-tissue eQTLs for chr16_52565276_C_T_b38 in tissues matching 'Breast - Mammary Tissue'. NES is the effect of the alt allele (T) relative to ref (C).
