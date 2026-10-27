# rs4784227 and Breast cancer (16q12)

Configuration `full`, named mode, seed 0. Models: generator claude-opus-5, critic claude-sonnet-5-5, summariser claude-haiku-5-5. Cost $0.63 over 7 model calls; 210 s.

Variant `chr16:52565276:C>T` (germline); expression context: DepMap:ACH-000019 (MCF7).

## QBiC-SELEX screen

290 of 997 models pass the gate. Top groups: bZIP, 6 models (best MAFG, z 71.57); C2H2 ZF, 1 model (best ZNF134, z 37.4); Homeodomain, 81 models (best LHX8, z 28.05); Rel, 4 models (best NFATC4, z -23.46); Homeodomain; POU, 1 model (best POU2F1, z 22.8).

## Ranked chains

### 1. H1: T (risk) allele increases GATA3 binding at the TOX3 distal enhancer in luminal breast cells (p = 0.37)

TF GATA3 (stated coverage own_model; registry own_model), alt allele binds more; element EH38E3180851 (dELS, chr16:52565011-52565360; Ensembl regulatory feature ENSR16_9QTBS); gene TOX3; cell type Luminal (ER-positive) breast epithelial cells, modelled by MCF7 (ACH-000019).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | QBiC GATA group G010 passes with all 6 models predicting stronger alt (T) binding (best model GATA2 z 18.65, effect +0.283; GATA3 own model z 10.91; site strength ref 92.3th to alt 98.6th percentile). Within the group GATA3 is chosen because it is by far the most expressed member in MCF7 (346 TPM vs GATA2 12.7 TPM, all others <1 TPM) and because ENCODE GATA3 ChIP-seq in MCF-7 places 5 peaks over this exact position in 3 independent experiments, so GATA3 is the group member demonstrably occupying the site. The allelic direction remains a prediction: no allele-specific ChIP is cited. | weak | [E17](#e17), [E07](#e07), [E18](#e18) |
| element | The variant is inside an ENCODE distal enhancer-like cCRE (DNase z 4.2, H3K27ac z 6.1; maxima across biosamples, not MCF7-specific) and an Ensembl enhancer feature; GATA3 occupancy in MCF-7 indicates the element is accessible in this cell line. | weak | [E03](#e03), [E01](#e01), [E18](#e18) |
| gene | Open Targets credible sets containing the variant at PIP 1.00 give TOX3 the top L2G score (0.92-0.96), and TOX3 is the nearest protein-coding TSS (17.5 kb). No contact, CRISPR or breast eQTL evidence links the element to TOX3; GTEx finds no significant breast eQTL, so the assignment rests on statistical gene prioritisation and proximity only. | weak | [E05](#e05), [E02](#e02), [E20](#e20) |
| cell_type | MCF7 expresses GATA3 at 346 TPM and ENCODE GATA3 ChIP peaks at this site come from MCF-7 biosamples, so the predicted occupancy change is realisable in this context. | weak | [E17](#e17), [E18](#e18) |
| phenotype | T is the effect allele for breast cancer at p 2e-240 and for ER-negative and ER-positive subtypes; the chain assumes but does not show that a GATA3-dependent change in TOX3 mediates this association. | weak | [E04](#e04), [E06b](#e06b), [E06a](#e06a) |

Predictions: Allele-specific GATA3 ChIP in heterozygous breast cells shows T-biased reads at chr16:52565276; GATA3 knockdown in MCF7 changes TOX3 expression and removes the allelic reporter difference; CRISPRi of EH38E3180851 lowers TOX3 without affecting CHD9 or RBL2

Falsified if: No allelic imbalance in GATA3 ChIP or EMSA at this position; GATA3 depletion leaves TOX3 and reporter allelic difference unchanged; Enhancer silencing does not alter TOX3

### 2. H5: Null: no TF-mediated effect of this variant itself (p = 0.28)

Null chain: no TF-mediated effect of this variant.

Predictions: Single-base editing or reporter assays show no allelic difference at chr16:52565276 in breast cells; Allele-specific ChIP for GATA3 and FOXA1 shows balanced reads despite peaks overlapping the site; Causal signal maps to another variant on the 16q12 haplotype; consistent with no significant breast eQTL (E20), poor conservation (GERP -2), and 290/997 QBiC models passing, which indicates a promiscuous k-mer change rather than a specific motif

Falsified if: An isolated C>T edit changes TOX3/CASC16 expression or enhancer activity; Reproducible allele-specific occupancy of any expressed TF at this position

### 3. H2: T allele acts through the FOXA1 pioneer site that overlaps the variant in MCF-7 (p = 0.17)

TF FOXA1 (stated coverage not_in_coverage; registry own_model), alt allele binds more; element EH38E3180851 distal enhancer at chr16:52565276; gene TOX3; cell type ER-positive luminal breast epithelial cells (MCF7).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | One ENCODE FOXA1 ChIP-seq peak in MCF-7 contains the variant, so FOXA1 occupies this element. FOXA1 has no QBiC-SELEX model among the 997 scored, so no allelic direction can be assigned from binding models; the alt-preferring direction is assumed from the risk-allele framing and is not evidenced. | weak | [E19](#e19), [E07](#e07) |
| element | The variant sits in an active distal enhancer-like cCRE, the chromatin class where pioneer FOXA1 opens chromatin; occupancy in MCF-7 is shown by ChIP. | weak | [E03](#e03), [E19](#e19) |
| gene | TOX3 is the top L2G gene (0.92-0.96) for the breast-cancer credible sets containing the variant and the nearest TSS; no looping or perturbation data connect this FOXA1-bound element to TOX3, and no breast eQTL exists. | weak | [E05](#e05), [E02](#e02), [E20](#e20) |
| cell_type | The only cited FOXA1 occupancy is in MCF-7, a luminal line, so any effect would be restricted to FOXA1-positive luminal cells; no FOXA1 expression value is cited. | weak | [E19](#e19) |
| phenotype | T is the breast-cancer risk allele (p 2e-240), with signal in both ER-negative (p 2e-26) and ER-positive (p 1e-13) analyses; the direction of any TOX3 change is not established. | weak | [E04](#e04), [E06b](#e06b) |

Predictions: FOXA1 ChIP in heterozygous cells shows allelic imbalance at chr16:52565276; FOXA1 knockdown, but not GATA3 knockdown, collapses the allelic reporter difference and reduces chromatin accessibility at the element; Accessibility (ATAC) at the element depends on FOXA1

Falsified if: FOXA1 ChIP shows balanced allelic reads; FOXA1 depletion leaves accessibility and TOX3 unchanged while GATA3 depletion does not

### 4. H3: T allele creates a strong small-MAF (MAFG/MAFK) site that alters output of the TOX3 enhancer (p = 0.13)

TF MAFG (stated coverage own_model; registry own_model), alt allele binds more; element EH38E3180851 distal enhancer at chr16:52565276; gene TOX3; cell type MCF7 luminal breast cancer cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The strongest QBiC signal at this site is bZIP group G012: best model is an own model of MAFG (z 71.57, effect +2.788; site strength ref 97.6th to alt 100th percentile) and all 6 passing models agree on alt-gain. I now name MAFG rather than MAFK because MAFG holds the best own model and is expressed in MCF7 (8.48 TPM); MAFK (16.96 TPM) is the more expressed close paralogue and the two are interchangeable at MARE half-sites, so this is a group-level specificity, not a single-TF call. | weak | [E08](#e08), [E07](#e07) |
| element | The site is an active distal enhancer-like cCRE, so a gained MARE-like site could recruit small MAFs; no small-MAF ChIP evidence at this element is cited and the repressive-versus-activating role is unresolved. | weak | [E03](#e03) |
| gene | TOX3 is the prioritised target by L2G (0.96) and proximity; no data connect a MAF site to TOX3, and no breast eQTL is seen. | weak | [E05](#e05), [E02](#e02), [E20](#e20) |
| cell_type | MAFK (16.96 TPM), MAFG (8.48 TPM) and MAFB (3.09 TPM) are expressed in MCF7, so the predicted gain of binding is realisable there. | weak | [E08](#e08) |
| phenotype | The T allele carries the 16q12 breast-cancer association; a MAF-mediated change in TOX3 is a hypothesis, not shown by any cited data. | weak | [E04](#e04) |

Predictions: MAFG/MAFK ChIP or EMSA supershift shows T-allele-specific binding absent on C; Small-MAF knockdown changes reporter activity only for the T allele; Reporter direction may be repressive (small-MAF homodimers), opposite to H1/H2

Falsified if: No small-MAF occupancy at the element in MCF7; MAFG/MAFK depletion has no effect on allelic reporter activity or TOX3

### 5. H4: T allele disrupts an NFAT site, lowering enhancer activity at TOX3 (p = 0.05)

TF NFATC3 (stated coverage mapped; registry own_model), ref allele binds more; element EH38E3180851 distal enhancer at chr16:52565276; gene TOX3; cell type MCF7 luminal breast cancer cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | QBiC Rel group G026 predicts loss of binding on the alt allele (best model NFATC4 own model z -23.46, effect -1.044; ref 98.0th to alt 70.9th percentile). NFATC3 is named because it is the most expressed member in MCF7 (9.54 TPM vs NFATC4 0.86 TPM), but its own passing z is only -4.28, the weakest in the group, so the TF assignment within the group is poorly supported. | weak | [E11](#e11), [E07](#e07) |
| element | The variant is in an active distal enhancer; loss of an NFAT site could lower or raise activity, since NFAT family members both activate and repress. | weak | [E03](#e03) |
| gene | TOX3 is the prioritised gene by L2G and proximity; no evidence ties an NFAT site to TOX3 regulation. | weak | [E05](#e05), [E02](#e02) |
| cell_type | NFATC3 is expressed in MCF7 (9.54 TPM); no NFAT occupancy at this element is shown, and GATA3 and FOXA1 are the only TFs with cited ChIP peaks here. | weak | [E11](#e11), [E18](#e18), [E19](#e19) |
| phenotype | T is the risk allele; no cited evidence sets the sign of the TOX3 change required by this chain, so the direction is an untested assumption. | missing | [E04](#e04) |

Predictions: Allele-specific binding favours C; the T-allele reporter shows reduced activity relative to C; TOX3 or CASC16 transcript levels are lower on T-allele chromosomes in allele-specific expression assays

Falsified if: T-allele reporter activity is equal to or higher than C; No NFAT occupancy at the enhancer in breast cells

## Prediction matrix

| Test | Cost | Separates top two | H1 | H5 | H2 | H3 | H4 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Allele-specific GATA3 ChIP-seq (or ChIP-qPCR/EMSA) in heterozygous MCF7-like breast cells at chr16:52565276 | medium | yes | T-allele-biased GATA3 reads | Balanced reads | Balanced GATA3 reads, or bias secondary to FOXA1-dependent accessibility | No GATA3 allelic bias | No GATA3 bias; if any, C-biased |
| Allele-specific FOXA1 ChIP at the same position (existing MCF-7 FOXA1 experiment ENCSR126YEB reads, if heterozygous) | existing data | yes | Balanced or weakly biased FOXA1 reads | Balanced | T-allele-biased FOXA1 reads | Balanced | Balanced or C-biased |
| Luciferase reporter of the 350 bp cCRE with C versus T in MCF7 | low | no | T higher than C | No allelic difference | T higher than C (FOXA1-dependent) | Allelic difference present, plausibly T lower (repressive MARE) | T lower than C |
| siRNA knockdown of GATA3 versus FOXA1 in MCF7, measuring TOX3/CASC16 and allelic reporter difference | medium | yes | GATA3 knockdown changes TOX3 and abolishes allelic difference; FOXA1 knockdown has lesser effect | No allelic difference to abolish in any arm | FOXA1 knockdown abolishes the allelic difference and accessibility; GATA3 knockdown does not | Neither changes the allelic difference; MAFG/MAFK knockdown does | Neither; NFAT inhibition does |
| CRISPR base-edit C>T on an isogenic background plus CRISPRi of EH38E3180851, reading TOX3, CASC16, CHD9 | high | no | Edit raises TOX3; CRISPRi lowers TOX3 | Edit changes nothing, even if CRISPRi lowers TOX3 | Edit raises TOX3; CRISPRi lowers TOX3 | Edit changes TOX3, possibly downward | Edit lowers TOX3 |
| Breast-tissue eQTL for TOX3 at this variant (GTEx v8) | existing data | no | No significant breast eQTL observed (E20); consistent only if the effect is cell-type restricted | Absence of eQTL is the expected result | Same as H1 | Same | Same |

## Next experiment

Re-analyse the existing ENCODE MCF-7 ChIP-seq reads at chr16:52565276 for allelic imbalance in GATA3 (ENCSR000BST, ENCSR000EWV, ENCSR423RTK) and FOXA1 (ENCSR126YEB), after confirming MCF7 is heterozygous at the site. This costs nothing beyond re-analysis and directly separates H1 (T-biased GATA3 reads) from H2 (T-biased FOXA1 reads) and from the null (balanced reads despite peaks).

## Investigate calls

- chip_peaks({"tf": "GATA3", "biosample": "MCF-7"})
- chip_peaks({"tf": "FOXA1", "biosample": "MCF-7"})
- eqtl_lookup({"tissue": "Breast_Mammary_Tissue"})

## Flags

- coverage_misstated: H2: stated not_in_coverage, registry says own_model for FOXA1
- coverage_misstated: H4: stated mapped, registry says own_model for NFATC3

Citation support: 1.00 of links cite only evidence that passed every check.

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

<a id="e07"></a>**E07** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> QBiC-SELEX screen of chr16:52565276:C>T: 997 models scored, 290 pass the gate (Bonferroni 0.05/997, p < 5.02e-05, |z| > 4.05), in 173 CIS-BP groups. Expression context: DepMap line ACH-000019. Groups shown: 10; dropped because no TF in the group reaches 1 TPM: 53 (Homeodomain, 1 model z -49.09, bZIP, 1 model z 44.2, Homeodomain; POU, 2 models z 23.66, Homeodomain; POU, 1 model z 22.86, Homeodomain; POU, 1 model z 19.26). predicted_effect > 0 means the alternate allele binds more strongly. In vitro binding only: expression and chromatin decide whether a change matters.

<a id="e08"></a>**E08** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G012 (bZIP, 6 models): best model MAFG_eDBD_TTGTTC40NAAG_KN_yin2017_0_3_7mer (own model of MAFG), z 71.57, effect 2.788 (alt binds more); 6 passing models (6 with the best model's sign). Passing members: MAFG z 71.57, NRL z 52.25, MAFK z 48.84, MAFB z 47.42, MAF z 41.62 (+1 more). TFs this group covers (own and CIS-BP-mapped models): MAFK 16.96 TPM, MAFG 8.48 TPM, MAFB 3.09 TPM, MAFA 1.07 TPM, NRL 0.98 TPM, MAF 0.23 TPM; best model's site strength: ref 97.6th, alt 100.0th percentile of its k-mer coefficients.

<a id="e09"></a>**E09** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G441 (C2H2 ZF, 1 model): best model ZNF134_FL_AC40NTGTTAC_AATA_jolma2025_0_3_7mer (own model of ZNF134), z 37.4, effect 2.724 (alt binds more); 1 passing models (1 with the best model's sign). Passing members: ZNF134 z 37.4. TFs this group covers (own and CIS-BP-mapped models): ZNF134 4.56 TPM; best model's site strength: ref 99.2th, alt 100.0th percentile of its k-mer coefficients.

<a id="e10"></a>**E10** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G001 (Homeodomain, 81 models): best model LHX8_FL_TTGCGA40NGTA_KW_yin2017_0_4_7mer (own model of LHX8), z 28.05, effect 2.175 (alt binds more); 59 passing models (46 with the best model's sign); members disagree on direction. Passing members: LHX8 z 28.05, BARHL2 z -27.02, BARX1 z -23.33, HOXA2 z 20.4, HMX1 z -20.39 (+54 more). TFs this group covers (own and CIS-BP-mapped models): MSX2 17.65 TPM, LMX1B 11.66 TPM, BARX2 6.62 TPM, ZFHX3 5.13 TPM, DLX3 4.42 TPM, HOXB7 4.39 TPM, LHX1 4.3 TPM, PITX1 4.1 TPM, HOXC9 3.41 TPM, LBX2 2.97 TPM (+103 more); best model's site strength: ref 94.6th, alt 99.3th percentile of its k-mer coefficients.

<a id="e11"></a>**E11** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G026 (Rel, 4 models): best model NFATC4_eDBD_TAGGTA40NGAT_KAN_yin2017_0_4_7mer (own model of NFATC4), z -23.46, effect -1.044 (alt binds less); 3 passing models (3 with the best model's sign). Passing members: NFATC4 z -23.46, NFATC2 z -9.14, NFATC3 z -4.28. TFs this group covers (own and CIS-BP-mapped models): NFATC3 9.54 TPM, NFATC2 2.41 TPM, NFATC1 1.66 TPM, NFATC4 0.86 TPM; best model's site strength: ref 98.0th, alt 70.9th percentile of its k-mer coefficients.

<a id="e12"></a>**E12** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G285 (Homeodomain; POU, 1 model): best model POU2F1_NA_TCTTTC20NGA_ESAC_yang2017_1_2_7mer (own model of POU2F1), z 22.8, effect 0.903 (alt binds more); 1 passing models (1 with the best model's sign). Passing members: POU2F1 z 22.8. TFs this group covers (own and CIS-BP-mapped models): POU2F1 3.33 TPM; best model's site strength: ref 86.5th, alt 98.9th percentile of its k-mer coefficients.

<a id="e13"></a>**E13** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G217 (CENPB, 1 model): best model JRK_DBD_CA40NAGCGTA_YWCB_jolma2025_0_3_7mer (own model of JRK), z -21.69, effect -0.43 (alt binds less); 1 passing models (1 with the best model's sign). Passing members: JRK z -21.69. TFs this group covers (own and CIS-BP-mapped models): JRK 4.89 TPM; best model's site strength: ref 99.8th, alt 88.4th percentile of its k-mer coefficients.

<a id="e14"></a>**E14** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G006 (Homeodomain, 11 models): best model TPRX1_DBD_TG40NGACCTT_YWCB_jolma2025_0_2_7mer (own model of TPRX1), z -21.39, effect -0.283 (alt binds less); 6 passing models (5 with the best model's sign); members disagree on direction. Passing members: TPRX1 z -21.39, OTX1 z -16.59, OTX2 z -12.55, CRX z -5.7, DPRX z -4.88 (+1 more). TFs this group covers (own and CIS-BP-mapped models): PITX1 4.1 TPM, GSC 2.38 TPM, OTX1 1.25 TPM, PITX2 1.02 TPM, DMBX1 0.2 TPM, VSX1 0.09 TPM, PITX3 0.02 TPM, GSC2 0.01 TPM, VAX1 0.01 TPM, CRX 0.0 TPM (+4 more); best model's site strength: ref 100.0th, alt 99.7th percentile of its k-mer coefficients.

<a id="e15"></a>**E15** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G354 (bHLH, 1 model): best model TFAP4_NA_TCACGT20NGCA_ESAC_yang2017_0_3_7mer (own model of TFAP4), z 19.55, effect 1.433 (alt binds more); 1 passing models (1 with the best model's sign). Passing members: TFAP4 z 19.55. TFs this group covers (own and CIS-BP-mapped models): TFAP4 6.85 TPM; best model's site strength: ref 83.4th, alt 100.0th percentile of its k-mer coefficients.

<a id="e16"></a>**E16** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G401 (C2H2 ZF, 1 model): best model ZBTB37_eDBD_TATGTC40NGGA_KR_yin2017_0_4_7mer (own model of ZBTB37), z -19.38, effect -3.006 (alt binds less); 1 passing models (1 with the best model's sign). Passing members: ZBTB37 z -19.38. TFs this group covers (own and CIS-BP-mapped models): ZBTB37 2.15 TPM; best model's site strength: ref 99.7th, alt 97.1th percentile of its k-mer coefficients.

<a id="e17"></a>**E17** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G010 (GATA, 6 models): best model GATA2_eDBD_TATGCA40NGAG_KR_yin2017_1_3_7mer (own model of GATA2), z 18.65, effect 0.283 (alt binds more); 6 passing models (6 with the best model's sign). Passing members: GATA2 z 18.65, GATA6 z 14.98, GATA1 z 12.45, GATA3 z 10.91, GATA4 z 8.04 (+1 more). TFs this group covers (own and CIS-BP-mapped models): GATA3 346.04 TPM, GATA2 12.69 TPM, GATA6 0.86 TPM, GATA4 0.45 TPM, GATA1 0.02 TPM, GATA5 0.0 TPM; best model's site strength: ref 92.3th, alt 98.6th percentile of its k-mer coefficients.

<a id="e18"></a>**E18** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-25T17:27:50+00:00)

> 5 ENCODE GATA3 ChIP-seq peaks contain chr16:52565276:C>T in biosamples matching 'MCF-7': biosamples MCF-7; experiments ENCSR000BST, ENCSR000EWV, ENCSR423RTK.

<a id="e19"></a>**E19** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-25T17:27:50+00:00)

> 1 ENCODE FOXA1 ChIP-seq peaks contain chr16:52565276:C>T in biosamples matching 'MCF-7': biosamples MCF-7; experiments ENCSR126YEB.

<a id="e20"></a>**E20** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr16_52565276_C_T_b38&datasetId=gtex_v8; retrieved 2026-10-25T17:27:51+00:00)

> 0 significant GTEx v8 single-tissue eQTLs for chr16_52565276_C_T_b38 in tissues matching 'Breast_Mammary_Tissue'. NES is the effect of the alt allele (T) relative to ref (C).
