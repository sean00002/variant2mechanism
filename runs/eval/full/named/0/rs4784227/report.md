# rs4784227 and Breast cancer (16q12)

Configuration `full`, named mode, seed 0. Models: generator claude-opus-5, critic claude-sonnet-5-5, summariser claude-haiku-5-5. Cost $0.63 over 7 model calls; 165 s.

Variant `chr16:52565276:C>T` (germline); expression context: DepMap:ACH-000019 (MCF7).

## QBiC-SELEX screen

290 of 997 models pass the gate. Top groups: bZIP, 6 models (best MAFG, z 71.57); C2H2 ZF, 1 model (best ZNF134, z 37.4); Homeodomain, 81 models (best LHX8, z 28.05); Rel, 4 models (best NFATC4, z -23.46); Homeodomain; POU, 1 model (best POU2F1, z 22.8).

## Ranked chains

### 1. H1: T allele strengthens a GATA site in the TOX3 enhancer; GATA3, which occupies this element in MCF7, mediates the effect (p = 0.38)

TF GATA3 (stated coverage own_model; registry own_model), alt allele binds more; element EH38E3180851 (dELS enhancer, also ENSR16_9QTBS), chr16:52565011-52565360; gene TOX3; cell type Luminal (ER-positive) mammary epithelial cells / MCF7.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The GATA specificity group passes the screen with all 6 models agreeing the alt (T) allele binds more (best model GATA2 z 18.65, effect +0.283; site strength 92.3th to 98.6th percentile). Within the group I pick GATA3 because it is by far the most expressed member in MCF7 (346 TPM vs GATA2 12.7, rest <1), has its own QBiC-SELEX model, and is the only group member with direct ChIP-seq occupancy at this variant: 5 ENCODE GATA3 peaks in MCF-7 and further peaks in T47D and A549 contain chr16:52565276. The direction (alt stronger) is a group-level in vitro prediction, not measured allele-specific binding. | weak | [E17](#e17), [E18](#e18), [E07](#e07) |
| element | The variant lies in dELS cCRE EH38E3180851 (DNase z 4.2, H3K27ac z 6.1; maxima across biosamples) and in Ensembl enhancer ENSR16_9QTBS; GATA3 ChIP peaks in MCF-7 show the element is bound in the relevant cell line. | supported | [E01](#e01), [E03](#e03), [E18](#e18) |
| gene | The cCRE is assigned to CASC16/TOX3; TOX3 is 17.5 kb away and the top L2G gene (0.92-0.96) in breast cancer credible sets where the variant has PIP 1.00. No breast eQTL supports this link (0 significant GTEx breast eQTLs), so the gene assignment rests on proximity and L2G only, and CASC16 is not excluded. | weak | [E02](#e02), [E03](#e03), [E05](#e05), [E20](#e20) |
| cell_type | The element is occupied by GATA3 in MCF-7 and T47D (both luminal breast lines), matching the MCF7 expression context; associations are reported for both ER+ and ER- breast cancer, so I do not claim subtype specificity. | weak | [E18](#e18), [E17](#e17), [E04](#e04), [E05](#e05) |
| phenotype | If allelic GATA3 binding changes enhancer output onto TOX3, this would alter breast cancer risk in T-allele carriers; the T allele is the risk allele in the largest studies, but the direction of the TOX3 expression change is not established by any cited evidence. | weak | [E04](#e04), [E06a](#e06a), [E06b](#e06b) |

Predictions: Allele-specific read counting in existing heterozygous MCF-7/T47D GATA3 ChIP-seq shows excess T-allele reads; GATA3 knockdown in MCF7 removes the allelic difference in an enhancer reporter; CRISPR deletion of EH38E3180851 lowers TOX3 in MCF7 with GATA3 dependence

Falsified if: Allele-specific analysis of existing GATA3 ChIP-seq shows equal or C-biased binding; Enhancer reporter allelic difference persists after GATA3 depletion; Isogenic C>T swap in MCF7 does not change TOX3/CASC16

### 2. H5: Null: no TF-binding-mediated effect of rs4784227 itself (p = 0.24)

Null chain: no TF-mediated effect of this variant.

Predictions: Isogenic CRISPR allele swap of rs4784227 in MCF7 leaves TOX3/CASC16 expression unchanged; Allelic enhancer reporter activity is equal for C and T; Existing MCF-7 ChIP-seq shows no allele-specific read imbalance for any factor at this site; A tightly linked variant in the same credible set carries the allelic effect

Falsified if: Isogenic allele swap changes TOX3 expression or enhancer activity; Reproducible allele-specific TF occupancy at the variant in breast cells

### 3. H2: T allele strengthens a FOXA1 (forkhead) site in the TOX3 enhancer (p = 0.19)

TF FOXA1 (stated coverage own_model; registry own_model), alt allele binds more; element EH38E3180851 (dELS enhancer) at chr16:52565276; gene TOX3; cell type ER-positive luminal breast epithelium / MCF7.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The FOXA1 lookup shows its own QBiC-SELEX model passes the gate with the alt allele binding more (effect +0.314, z 9.34, rank 82/997; site strength 99.0th to 99.8th percentile), and the CIS-BP FOXA2 model agrees (effect +0.296, z 15.4). Direction is alt-stronger, but the effect size is small relative to the Maf and GATA groups, and no FOXA1 ChIP evidence at this element is in the evidence set. | weak | [E19](#e19) |
| element | The variant lies in an active distal enhancer-like cCRE / Ensembl enhancer, the class of element FOXA1 pioneers in breast cells; no FOXA1 occupancy at this cCRE is shown in the cited data. | weak | [E01](#e01), [E03](#e03) |
| gene | The enhancer is assigned to CASC16/TOX3 and TOX3 is the top L2G gene; no contact or eQTL evidence links the element to TOX3 in breast. | weak | [E02](#e02), [E03](#e03), [E05](#e05), [E20](#e20) |
| cell_type | The QBiC lookup was run in the MCF7 expression context, which the screen uses for a 1 TPM expression filter, and FOXA1 was returned as a scored, gated model; direct FOXA1 TPM in MCF7 is not quoted here. | missing | [E19](#e19), [E07](#e07) |
| phenotype | Greater pioneer-factor binding on the T allele could open the enhancer further and alter TOX3 levels, matching the T-allele risk association; no cited evidence connects FOXA1 to TOX3 levels at this variant. | missing | [E04](#e04), [E06b](#e06b) |

Predictions: FOXA1 ChIP-seq in MCF-7/T47D shows a peak overlapping chr16:52565011-52565360 with T-allele bias; FOXA1 depletion, but not GATA3 depletion, abolishes the allelic reporter difference; FOXA1 motif disruption by targeted edit removes the allelic effect

Falsified if: No FOXA1 peak overlaps the cCRE in breast cell ChIP-seq; Allele-specific FOXA1 ChIP shows no bias; Allelic reporter difference is unaffected by FOXA1 knockdown

### 4. H3: T allele creates a strong small-Maf (MAFK/MAFG) site that rewires the enhancer (p = 0.12)

TF MAFK (stated coverage own_model; registry own_model), alt allele binds more; element EH38E3180851 distal enhancer; gene TOX3; cell type MCF7 luminal breast cancer cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The small-Maf group gives the largest effect in the screen (best model MAFG z 71.57, effect +2.788; alt site strength 100th vs ref 97.6th percentile), with all 6 models alt-stronger. I pick MAFK because it is the most expressed small Maf in MCF7 (16.96 TPM vs MAFG 8.48) and has its own model and a passing z of 48.84; the choice rests on expression alone, with no ChIP support. | weak | [E08](#e08), [E07](#e07) |
| element | The predicted gained site falls inside an active distal enhancer-like cCRE with high H3K27ac (maxima across biosamples). | weak | [E03](#e03), [E01](#e01) |
| gene | The cCRE is assigned to CASC16/TOX3 and TOX3 is the top L2G gene; no eQTL in breast supports a TOX3 link. | weak | [E03](#e03), [E05](#e05), [E02](#e02), [E20](#e20) |
| cell_type | MAFK and MAFG are expressed above 1 TPM in MCF7, so a created MARE could in principle be bound there; occupancy is unverified. | weak | [E08](#e08) |
| phenotype | If bound, small Mafs could repress (as homodimers) or activate (with CNC partners), changing TOX3 output; no cited evidence ties Maf factors to this locus or to risk, so this step is unsupported. | missing | none |

Predictions: MAFK or MAFG ChIP-seq shows a T-allele-specific peak at chr16:52565276; Reporter activity responds to MAFK/NFE2L2 overexpression in an allele-dependent way; GATA3 and FOXA1 depletion leave the allelic difference intact

Falsified if: No small-Maf occupancy at the locus despite the very large in vitro prediction; Allelic enhancer activity unchanged by MAFK/MAFG/NFE2L2 perturbation

### 5. H4: C (ref) allele preferentially binds NFAT; loss of NFATC3 binding on the T allele changes enhancer output (p = 0.07)

TF NFATC3 (stated coverage own_model; registry own_model), ref allele binds more; element EH38E3180851 distal enhancer; gene TOX3; cell type MCF7 / breast epithelium.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The Rel/NFAT group passes with all three models ref-stronger (best model NFATC4 z -23.46, effect -1.044; site strength 98.0th to 70.9th percentile). I pick NFATC3 as the most expressed member in MCF7 (9.54 TPM) and a passing own-model member, though its own z (-4.28) is barely above the gate and the best model belongs to a low-expressed paralogue. | weak | [E11](#e11), [E07](#e07) |
| element | The predicted lost site lies within the dELS cCRE containing the variant. | weak | [E03](#e03), [E01](#e01) |
| gene | TOX3 is the nearest protein-coding gene and the top L2G target; no breast eQTL supports the link. | weak | [E02](#e02), [E05](#e05), [E20](#e20) |
| cell_type | NFATC3 is expressed in MCF7, so a ref-specific site could be occupied in luminal breast cells; occupancy is not shown. | weak | [E11](#e11) |
| phenotype | A change in NFAT occupancy between alleles could alter enhancer output and TOX3 levels; the direction of that change and its link to risk are not supported by cited evidence. | missing | [E04](#e04) |

Predictions: ChIP shows C-allele-biased NFATC3 binding at the variant; Calcineurin/NFAT inhibition changes enhancer reporter activity only for the C allele; GATA3 ChIP allelic bias is absent

Falsified if: No NFAT peak at the enhancer in breast cells; Allelic reporter difference persists under NFAT inhibition

## Prediction matrix

| Test | Cost | Separates top two | H1 | H5 | H2 | H3 | H4 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Allele-specific read imbalance at chr16:52565276 in existing heterozygous MCF-7/T47D GATA3 ChIP-seq (ENCSR000BST, ENCSR000EWV, ENCSR423RTK, ENCSR000BTI) | existing data | yes | T-allele excess reads | Balanced reads | No or weak GATA3 bias (FOXA1-driven co-occupancy possible but not allele-biased for GATA3) | No GATA3 allelic bias | No GATA3 bias; if any, C-biased |
| Factorbook/ENCODE query for FOXA1 ChIP-seq peaks overlapping chr16:52565011-52565360 in MCF-7, then allele-specific read counts | existing data | yes | FOXA1 peak may exist but without T-allele read bias | No peak or balanced reads | FOXA1 peak present with T-allele excess reads | No FOXA1 allelic bias | No FOXA1 allelic bias |
| Luciferase reporter of the 350 bp cCRE with C vs T in MCF7, combined with siRNA against GATA3, FOXA1, MAFK, NFATC3 | medium | yes | Allelic difference lost on GATA3 knockdown only | No allelic difference in any condition | Allelic difference lost on FOXA1 knockdown only | Allelic difference lost on MAFK/MAFG knockdown | Allelic difference lost on NFATC3 knockdown or calcineurin inhibition |
| Isogenic CRISPR C>T knock-in in MCF7, then RNA-seq for TOX3 and CASC16 | high | no | TOX3 changes | No change in TOX3 or CASC16 | TOX3 changes | TOX3 changes (direction unspecified) | TOX3 changes |
| EMSA with MCF7 nuclear extract and C/T probes, supershift with GATA3 and FOXA1 antibodies | low | yes | T probe forms a stronger GATA3-supershifted complex | Equal complexes on both probes | T probe forms a stronger FOXA1-supershifted complex | T-specific complex not supershifted by either antibody | C probe forms the stronger complex |
| Breast-tissue eQTL/chromatin-contact lookup linking the cCRE to TOX3 (already partly done: 0 significant GTEx breast eQTLs, E20) | existing data | no | Gene link remains proximity/L2G-based; weak | Consistent with no cis effect in bulk breast tissue | Same, weak | Same, weak | Same, weak |

## Next experiment

Re-analyse the existing ENCODE MCF-7 and T47D ChIP-seq data at chr16:52565276 for allele-specific read counts in heterozygous samples, comparing GATA3 (peaks already documented, E18) with FOXA1 in the same cells. This uses existing data, costs nothing to generate, and directly separates H1 (T-biased GATA3 reads) from H2 (T-biased FOXA1 reads) while also testing the null (balanced reads).

## Investigate calls

- chip_peaks({"tf": "GATA3", "biosample": "MCF-7"})
- qbic_tf_detail({"tf": "FOXA1"})
- eqtl_lookup({"tissue": "Breast - Mammary Tissue"})

## Flags

- none

Citation support: 0.95 of links cite only evidence that passed every check.

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

<a id="e18"></a>**E18** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-25T17:27:50+00:00)

> 5 ENCODE GATA3 ChIP-seq peaks contain chr16:52565276:C>T in biosamples matching 'MCF-7': biosamples MCF-7; experiments ENCSR000BST, ENCSR000EWV, ENCSR423RTK. In other biosamples, 2 GATA3 peaks do contain the variant: A549, T47D (experiments ENCSR000BMX, ENCSR000BTI).

<a id="e19"></a>**E19** qbic_tf_detail, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> {"tf":"FOXA1","symbol":"FOXA1","via":"hgnc_symbol","notes":[],"coverage":"own_model","variant":"chr16:52565276:C>T","gate_p":5.02e-05,"models":[{"model":"FOXA1_FL_TCCCAT40NTGT_KX_yin2017_0_4_7mer","mapping":"own","group":"G022 Forkhead, 4 models","quality":0.775,"effect":0.314,"z":9.34,"p":9.6e-21,"rank_abs_z":"82/997","passed_gate":true,"site_strength":{"ref_percentile":99.0,"alt_percentile":99.8,"k":7}},{"model":"FOXA2_eDBD_TTGCGA40NGTA_KT_yin2017_1_2_7mer","mapping":"CIS-BP (FOXA2)","group":"G022 Forkhead, 4 models","quality":0.83,"effect":0.296,"z":15.4,"p":1.6e-53,"rank_abs_z":"37/997","passed_gate":true,"site_strength":{"ref_percentile":91.3,"alt_percentile":98.8,"k":7}},{"model":"FOXA3_FL_TGTGGT40NGGC_KX_yin2017_0_3_7mer","mapping":"CIS-BP (FOXA3)","group":"G022 Forkhead, 4 models","quality":0.928,"effect":0.144,"z":1.85,"p":0.065,"rank_abs_z":"569/997","passed_gate":false,"site_strength":{"ref_percentile":79.5,"alt_percentile":98.7,"k":7}},{"model":"FOXB1_NA_TGAGCA30NCGA_ESAI_yang2017_0_4_7mer","mapping":"CIS-BP (FOXB1)","group":"G022 Forkhead, 4 models","quality":0.674,"effect":0.045,"z":0.7,"p":0.49,"rank_abs_z":"814/997","passed_gate":false,"site_strength":{"ref_percentile":72.5,"alt_percentile":94.6,"k":7}}]}

<a id="e20"></a>**E20** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr16_52565276_C_T_b38&datasetId=gtex_v8; retrieved 2026-10-25T17:27:51+00:00)

> 0 significant GTEx v8 single-tissue eQTLs for chr16_52565276_C_T_b38 in tissues matching 'Breast - Mammary Tissue'. NES is the effect of the alt allele (T) relative to ref (C).
