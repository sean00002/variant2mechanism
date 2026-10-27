# rs4784227 and Breast cancer (16q12)

Configuration `full`, named mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.02 over 7 model calls; 165 s.

Variant `chr16:52565276:C>T` (germline); expression context: DepMap:ACH-000019 (MCF7).

## QBiC-SELEX screen

290 of 997 models pass the gate. Top groups: bZIP, 6 models (best MAFG, z 71.57); C2H2 ZF, 1 model (best ZNF134, z 37.4); Homeodomain, 81 models (best LHX8, z 28.05); Rel, 4 models (best NFATC4, z -23.46); Homeodomain; POU, 1 model (best POU2F1, z 22.8).

## Ranked chains

### 1. H2_GATA3_alt_gain: Alt T strengthens a GATA3-bound site in the TOX3 enhancer in MCF7 (p = 0.35)

TF GATA3 (stated coverage own_model; registry own_model), alt allele binds more; element distal enhancer-like cCRE EH38E3180851 / ENSR16_9QTBS; gene TOX3; cell type MCF7 / breast cancer.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The alt T allele binds GATA3 more strongly than the ref C allele in QBiC-SELEX: GATA3 has its own passing model in G010 with positive direction (GATA3 z 10.91; group effect +0.283, alt binds more). I chose GATA3 over other GATA-family members because it is by far the highest-expressed own-model member in the MCF7 expression context (346.04 TPM). E19 also shows that GATA3 ChIP-seq peaks contain this variant in MCF7, supporting occupancy, though not allele specificity. | weak | [E17](#e17), [E07](#e07), [E19](#e19) |
| element | rs4784227 lies in a distal enhancer-like cCRE, EH38E3180851, with DNase and H3K27ac signal, so it is plausible that an allele-specific GATA3 site change alters enhancer activity. | supported | [E01](#e01), [E03](#e03) |
| gene | TOX3 is the nearest protein-coding gene, 17.5 kb away, and is the best L2G gene for this variant. However, GTEx v8 shows no significant breast-mammary-tissue eQTL for this variant, so TOX3 as the direct breast target remains candidate-level rather than demonstrated. | weak | [E02](#e02), [E05](#e05), [E18](#e18) |
| cell_type | MCF7 is the provided expression context, GATA3 is extremely highly expressed there, and GATA3 ChIP-seq peaks in MCF7 contain this variant. This supports MCF7 as a relevant cell type, although allele-specific GATA3 occupancy has not been shown. | supported | [E07](#e07), [E17](#e17), [E19](#e19) |
| phenotype | The T allele is associated with increased breast cancer risk in GWAS and meta-analysis. The evidence does not support restricting this to ER-positive/luminal breast cancer, since ER-negative breast cancer also shows strong association. | supported | [E04](#e04), [E06b](#e06b) |

Predictions: Allele-specific GATA3 ChIP in MCF7 should show stronger GATA3 occupancy on the T allele than on the C allele.; Mutating the predicted GATA3 motif in an enhancer reporter should reduce the T-allele-specific enhancer effect.; If GATA3 activates TOX3, the T allele should increase TOX3 expression or enhancer activity in breast cells.

Falsified if: Existing or new MCF7 GATA3 ChIP-seq shows no allele-specific GATA3 binding at rs4784227.; GATA3 motif mutation does not affect allele-specific enhancer activity.; The T allele does not change TOX3 expression or enhancer activity in a GATA3-dependent way.

### 2. H1_MAFK_alt_gain: Alt T creates a stronger MAFK site in the TOX3 enhancer, but MCF7 MAFK occupancy is unproven (p = 0.29)

TF MAFK (stated coverage own_model; registry own_model), alt allele binds more; element distal enhancer-like cCRE EH38E3180851 / ENSR16_9QTBS; gene TOX3; cell type MCF7 / breast cancer.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The alt T allele binds MAFK more strongly than the ref C allele in QBiC-SELEX: MAFK has its own passing model in G012 with the positive direction of the group best model. I chose MAFK over MAFG/MAFB because MAFK is the highest-expressed own-model member in the MCF7 expression context (16.96 TPM), although MAFG has the stronger individual model. This is in vitro binding only. | weak | [E08](#e08), [E07](#e07) |
| element | rs4784227 lies in a distal enhancer-like cCRE, EH38E3180851, with DNase and H3K27ac signal, so an allele-specific MAFK binding change could alter enhancer activity. | supported | [E01](#e01), [E03](#e03) |
| gene | TOX3 is the nearest protein-coding gene and the best L2G gene. However, no significant GTEx breast-mammary-tissue eQTL for this variant is reported, so a direct MAFK-to-TOX3 regulatory link in breast tissue is not demonstrated. | weak | [E02](#e02), [E05](#e05), [E06a](#e06a), [E18](#e18) |
| cell_type | MAFK is expressed in the MCF7 expression context, but no ENCODE MAFK ChIP-seq peak contains this variant in MCF7; one MAFK peak contains it in HepG2. Thus MCF7 MAFK occupancy at this enhancer is plausible from expression but not supported by ChIP. | weak | [E07](#e07), [E08](#e08), [E20](#e20) |
| phenotype | The T allele is associated with increased breast cancer risk, with very strong GWAS support and meta-analysis ORs greater than 1 for T versus C. | supported | [E04](#e04), [E06b](#e06b) |

Predictions: Allele-specific MAFK ChIP in MCF7 should show stronger MAFK occupancy on the T allele than on the C allele.; Mutating the predicted MAFK motif in an enhancer reporter should reduce the T-allele-specific enhancer effect.; If MAFK activates TOX3, the T allele should increase TOX3 expression or enhancer activity in breast cells.

Falsified if: Allele-specific MAFK ChIP in MCF7 shows no T-allele preference or no MAFK binding at the locus.; MAFK motif mutation does not affect allele-specific enhancer activity.; The T allele does not change enhancer activity or TOX3 expression in a MAFK-dependent way.

### 3. H0_null_no_TF_effect: No TF-mediated effect of rs4784227 (p = 0.26)

Null chain: no TF-mediated effect of this variant.

Predictions: No reproducible allele-specific TF binding or enhancer-activity difference should be detected for rs4784227 itself in breast cells.; The 16q12 breast cancer signal may be explained by LD with another causal variant or by a TOX3-regulatory effect not mediated by this base.; TOX3 L2G evidence may reflect locus proximity rather than a direct rs4784227 TF mechanism.

Falsified if: A reproducible allele-specific TF binding change is demonstrated at rs4784227 in a relevant breast cell type.; Allele-specific enhancer reporter activity and TOX3 expression changes are shown for this exact base.; Editing rs4784227 alone changes TOX3 expression or a breast cancer phenotype.

### 4. H3_NFATC3_ref_loss: Alt T loses a repressive NFATC3 site in the TOX3 enhancer (p = 0.10)

TF NFATC3 (stated coverage own_model; registry own_model), ref allele binds more; element distal enhancer-like cCRE EH38E3180851 / ENSR16_9QTBS; gene TOX3; cell type MCF7 / breast cancer.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The ref C allele binds NFATC3 more strongly than the alt T allele in QBiC-SELEX: NFATC3 has an own passing model in G026 with negative direction, but its model barely passes the gate and the group best model is NFATC4. I chose NFATC3 because it is the highest-expressed own-model member in MCF7 (9.54 TPM). No allele-specific ChIP evidence is available. | weak | [E11](#e11), [E07](#e07) |
| element | The variant lies in an active distal enhancer-like cCRE, so loss of a repressive NFATC3 site could in principle change enhancer output. | supported | [E01](#e01), [E03](#e03) |
| gene | TOX3 is the nearest protein-coding gene and best L2G gene, but no significant breast GTEx eQTL is reported, so TOX3 as the target of an NFATC3-dependent effect is not demonstrated. | weak | [E02](#e02), [E05](#e05), [E18](#e18) |
| cell_type | NFATC3 is expressed in the provided MCF7 context, but there is no MCF7 ChIP evidence that NFATC3 binds this enhancer. | weak | [E07](#e07), [E11](#e11) |
| phenotype | The T allele is the breast cancer risk allele, but the mechanistic claim that loss of a repressive NFATC3 site increases TOX3 and thereby contributes to risk rests on an untested repression assumption. | weak | [E04](#e04), [E06b](#e06b) |

Predictions: Allele-specific NFATC3 ChIP should show stronger NFATC3 binding on the C allele and reduced binding on the T allele.; If NFATC3 represses TOX3, NFATC3 knockdown should increase TOX3 expression or enhancer activity.; Mutating the predicted NFATC3 motif should phenocopy the T allele in an enhancer reporter.

Falsified if: NFATC3 does not bind this locus allele-specifically in breast cells.; The T allele does not reduce NFATC3 occupancy.; NFATC3 knockdown does not change TOX3 expression or enhancer activity in the predicted direction.

## Prediction matrix

| Test | Cost | Separates top two | H2_GATA3_alt_gain | H1_MAFK_alt_gain | H0_null_no_TF_effect | H3_NFATC3_ref_loss |
| --- | --- | --- | --- | --- | --- | --- |
| Allele-specific reanalysis of existing MCF7 GATA3 ChIP-seq reads at rs4784227 (E19 ENCSR000BST/ENCSR000EWV/ENCSR423RTK), comparing C vs T read counts | low | yes | GATA3 ChIP reads show T-allele bias over C at rs4784227. | No GATA3 allelic bias at rs4784227. | No allele-specific GATA3 ChIP signal at rs4784227. | No GATA3 allelic bias at rs4784227. |
| Allele-specific MAFK ChIP-qPCR or SNP-ChIP in MCF7 at rs4784227, comparing C vs T alleles | medium | yes | No MAFK allelic bias at rs4784227. | MAFK ChIP shows T-allele bias over C at rs4784227. | No allele-specific MAFK ChIP signal at rs4784227. | No MAFK allelic bias at rs4784227. |
| Dual-luciferase enhancer reporter with ref vs alt allele in MCF7, plus separate GATA3-motif and MAFK-motif mutations | medium | yes | Alt allele increases activity; GATA3-motif mutation reduces the alt-specific effect; MAFK-motif mutation does not. | Alt allele increases activity; MAFK-motif mutation reduces the alt-specific effect; GATA3-motif mutation does not. | No reproducible allele-specific enhancer activity difference. | Alt allele may increase activity if NFATC3 represses; NFATC3-motif mutation or NFATC3 knockdown should affect the allelic difference. |
| Breast-tissue eQTL/colocalization for TOX3 with rs4784227 in a larger mammary-tissue dataset | high | no | If GATA3 activates TOX3, T allele associates with higher TOX3 expression in breast tissue. | If MAFK activates TOX3, T allele associates with higher TOX3 expression in breast tissue. | No rs4784227-TOX3 eQTL association in breast tissue. | If NFATC3 represses TOX3, T allele associates with higher TOX3 expression in breast tissue. |

## Next experiment

The cheapest experiment that separates the top two chains is allele-specific reanalysis of existing MCF7 GATA3 ChIP-seq reads at rs4784227 (E19 experiments), comparing C vs T read counts. H2_GATA3_alt_gain predicts T-allele-biased GATA3 occupancy; H1_MAFK_alt_gain predicts no GATA3 allelic bias.

## Investigate calls

- eqtl_lookup({"tissue": "Breast - Mammary Tissue"})
- chip_peaks({"tf": "GATA3", "biosample": "MCF7"})
- chip_peaks({"tf": "MAFK", "biosample": "MCF7"})

## Flags

- none

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

> The pooled ORs regarding the association between the rs4784227-CASC16 polymorphism and breast cancer risk were statistically significant [T vs C: OR = 1.244, 95% CI = 1.202-1.287; TT vs CT + CC: OR = 1.407, 95% CI = 1.296-1.528; CC vs CT + TT: OR = 0.777, 95% CI = 0.745-0.811; TT vs CC: OR = 1.544, 95% CI = 1.419-1.681; CT vs CC: OR = 1.244, 95% CI = 1.189-1.301].

<a id="e06c"></a>**E06c** literature_search, Europe PMC abstract, PMID 36042591 (https://europepmc.org/article/MED/36042591; retrieved 2026-10-25T17:26:28+00:00)

> Our pooled analysis showed a significant association between the rs4784227- (T) allele and breast cancer susceptibility in Asian and North American populations, and intervention with this mutation might be a new therapeutic strategy for breast cancer.

<a id="e07"></a>**E07** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> QBiC-SELEX screen of chr16:52565276:C>T: 997 models scored, 290 pass the gate (Bonferroni 0.05/997, p < 5.02e-05, |z| > 4.05), in 173 CIS-BP groups. Expression context: DepMap line ACH-000019. Groups shown: 10; dropped because no TF in the group reaches 1 TPM: 53 (Homeodomain, 1 model z -49.09, bZIP, 1 model z 44.2, Homeodomain; POU, 2 models z 23.66, Homeodomain; POU, 1 model z 22.86, Homeodomain; POU, 1 model z 19.26). Passing groups ranked below the ones shown: 110. In the group rows, 'own model' means the TF has its own QBiC-SELEX model and 'mapped' that it is covered only through CIS-BP-mapped models of related TFs. A TF not named in any group row may still have its own model, even one that passes the gate: look it up with qbic_tf_detail before stating its coverage or a QBiC-SELEX direction for it. predicted_effect > 0 means the alternate allele binds more strongly. In vitro binding only: expression and chromatin decide whether a change matters.

<a id="e08"></a>**E08** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G012 (bZIP, 6 models): best model MAFG_eDBD_TTGTTC40NAAG_KN_yin2017_0_3_7mer (own model of MAFG), z 71.57, effect 2.788 (alt binds more); 6 passing models (6 with the best model's sign). Passing members: MAFG z 71.57, NRL z 52.25, MAFK z 48.84, MAFB z 47.42, MAF z 41.62 (+1 more). TFs this group covers: MAFK (own model) 16.96 TPM, MAFG (own model) 8.48 TPM, MAFB (own model) 3.09 TPM, MAFA (own model) 1.07 TPM, NRL (own model) 0.98 TPM, MAF (own model) 0.23 TPM; best model's site strength: ref 97.6th, alt 100.0th percentile of its k-mer coefficients.

<a id="e09"></a>**E09** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G441 (C2H2 ZF, 1 model): best model ZNF134_FL_AC40NTGTTAC_AATA_jolma2025_0_3_7mer (own model of ZNF134), z 37.4, effect 2.724 (alt binds more); 1 passing models (1 with the best model's sign). Passing members: ZNF134 z 37.4. TFs this group covers: ZNF134 (own model) 4.56 TPM; best model's site strength: ref 99.2th, alt 100.0th percentile of its k-mer coefficients.

<a id="e10"></a>**E10** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G001 (Homeodomain, 81 models): best model LHX8_FL_TTGCGA40NGTA_KW_yin2017_0_4_7mer (own model of LHX8), z 28.05, effect 2.175 (alt binds more); 59 passing models (46 with the best model's sign); members disagree on direction. Passing members: LHX8 z 28.05, BARHL2 z -27.02, BARX1 z -23.33, HOXA2 z 20.4, HMX1 z -20.39 (+54 more). TFs this group covers: MSX2 (own model) 17.65 TPM, LMX1B (own model) 11.66 TPM, BARX2 (own model) 6.62 TPM, ZFHX3 (own model) 5.13 TPM, DLX3 (own model) 4.42 TPM, HOXB7 (own model) 4.39 TPM, LHX1 (own model) 4.3 TPM, PITX1 (own model) 4.1 TPM, HOXC9 (own model) 3.41 TPM, LBX2 (own model) 2.97 TPM (+103 more); best model's site strength: ref 94.6th, alt 99.3th percentile of its k-mer coefficients.

<a id="e11"></a>**E11** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G026 (Rel, 4 models): best model NFATC4_eDBD_TAGGTA40NGAT_KAN_yin2017_0_4_7mer (own model of NFATC4), z -23.46, effect -1.044 (alt binds less); 3 passing models (3 with the best model's sign). Passing members: NFATC4 z -23.46, NFATC2 z -9.14, NFATC3 z -4.28. TFs this group covers: NFATC3 (own model) 9.54 TPM, NFATC2 (own model) 2.41 TPM, NFATC1 (own model) 1.66 TPM, NFATC4 (own model) 0.86 TPM; best model's site strength: ref 98.0th, alt 70.9th percentile of its k-mer coefficients.

<a id="e12"></a>**E12** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G285 (Homeodomain; POU, 1 model): best model POU2F1_NA_TCTTTC20NGA_ESAC_yang2017_1_2_7mer (own model of POU2F1), z 22.8, effect 0.903 (alt binds more); 1 passing models (1 with the best model's sign). Passing members: POU2F1 z 22.8. TFs this group covers: POU2F1 (own model) 3.33 TPM; best model's site strength: ref 86.5th, alt 98.9th percentile of its k-mer coefficients.

<a id="e13"></a>**E13** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G217 (CENPB, 1 model): best model JRK_DBD_CA40NAGCGTA_YWCB_jolma2025_0_3_7mer (own model of JRK), z -21.69, effect -0.43 (alt binds less); 1 passing models (1 with the best model's sign). Passing members: JRK z -21.69. TFs this group covers: JRK (own model) 4.89 TPM; best model's site strength: ref 99.8th, alt 88.4th percentile of its k-mer coefficients.

<a id="e14"></a>**E14** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G006 (Homeodomain, 11 models): best model TPRX1_DBD_TG40NGACCTT_YWCB_jolma2025_0_2_7mer (own model of TPRX1), z -21.39, effect -0.283 (alt binds less); 6 passing models (5 with the best model's sign); members disagree on direction. Passing members: TPRX1 z -21.39, OTX1 z -16.59, OTX2 z -12.55, CRX z -5.7, DPRX z -4.88 (+1 more). TFs this group covers: PITX1 (own model) 4.1 TPM, GSC (own model) 2.38 TPM, OTX1 (own model) 1.25 TPM, PITX2 (own model) 1.02 TPM, DMBX1 (own model) 0.2 TPM, VSX1 (own model) 0.09 TPM, PITX3 (own model) 0.02 TPM, GSC2 (own model) 0.01 TPM, VAX1 (own model) 0.01 TPM, CRX (own model) 0.0 TPM (+4 more); best model's site strength: ref 100.0th, alt 99.7th percentile of its k-mer coefficients.

<a id="e15"></a>**E15** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G354 (bHLH, 1 model): best model TFAP4_NA_TCACGT20NGCA_ESAC_yang2017_0_3_7mer (own model of TFAP4), z 19.55, effect 1.433 (alt binds more); 1 passing models (1 with the best model's sign). Passing members: TFAP4 z 19.55. TFs this group covers: TFAP4 (own model) 6.85 TPM; best model's site strength: ref 83.4th, alt 100.0th percentile of its k-mer coefficients.

<a id="e16"></a>**E16** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G401 (C2H2 ZF, 1 model): best model ZBTB37_eDBD_TATGTC40NGGA_KR_yin2017_0_4_7mer (own model of ZBTB37), z -19.38, effect -3.006 (alt binds less); 1 passing models (1 with the best model's sign). Passing members: ZBTB37 z -19.38. TFs this group covers: ZBTB37 (own model) 2.15 TPM; best model's site strength: ref 99.7th, alt 97.1th percentile of its k-mer coefficients.

<a id="e17"></a>**E17** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G010 (GATA, 6 models): best model GATA2_eDBD_TATGCA40NGAG_KR_yin2017_1_3_7mer (own model of GATA2), z 18.65, effect 0.283 (alt binds more); 6 passing models (6 with the best model's sign). Passing members: GATA2 z 18.65, GATA6 z 14.98, GATA1 z 12.45, GATA3 z 10.91, GATA4 z 8.04 (+1 more). TFs this group covers: GATA3 (own model) 346.04 TPM, GATA2 (own model) 12.69 TPM, GATA6 (own model) 0.86 TPM, GATA4 (own model) 0.45 TPM, GATA1 (own model) 0.02 TPM, GATA5 (own model) 0.0 TPM; best model's site strength: ref 92.3th, alt 98.6th percentile of its k-mer coefficients.

<a id="e18"></a>**E18** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr16_52565276_C_T_b38&datasetId=gtex_v8; retrieved 2026-10-25T17:27:51+00:00)

> 0 significant GTEx v8 single-tissue eQTLs for chr16_52565276_C_T_b38 in tissues matching 'Breast - Mammary Tissue'. NES is the effect of the alt allele (T) relative to ref (C).

<a id="e19"></a>**E19** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-25T17:27:50+00:00)

> 5 ENCODE GATA3 ChIP-seq peaks contain chr16:52565276:C>T in biosamples matching 'MCF7': biosamples MCF-7; experiments ENCSR000BST, ENCSR000EWV, ENCSR423RTK. In other biosamples, 2 GATA3 peaks do contain the variant: A549, T47D (experiments ENCSR000BMX, ENCSR000BTI).

<a id="e20"></a>**E20** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-26T00:40:00+00:00)

> No ENCODE MAFK ChIP-seq peak contains chr16:52565276:C>T in biosamples matching 'MCF7'. Absence can also mean no MAFK experiment in that biosample. In other biosamples, 1 MAFK peaks do contain the variant: HepG2 (experiments ENCSR000EEB).
