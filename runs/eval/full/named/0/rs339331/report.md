# rs339331 and Prostate cancer (6q22)

Configuration `full`, named mode, seed 0. Models: generator claude-opus-5, critic claude-sonnet-5-5, summariser claude-haiku-5-5. Cost $0.66 over 7 model calls; 175 s.

Variant `chr6:116888889:T>C` (germline); expression context: DepMap:ACH-000977 (LNCaP clone FGC).

## QBiC-SELEX screen

487 of 997 models pass the gate. Top groups: Homeodomain, 4 models (best HOXB13, z -103.49); Homeodomain, 18 models (best HOXC10, z -84.28); IRF, 2 models (best IRF6, z 56.39); C2H2 ZF, 1 model (best PRDM4, z 47.33); IRF, 1 model (best IRF3, z 44.89).

## Ranked chains

### 1. H1: Ref T preserves a HOXB13 site in the 6q22 enhancer, raising RFX6 expression in prostate cells (p = 0.34)

TF HOXB13 (stated coverage own_model; registry own_model), ref allele binds more; element cCRE EH38E2496909 (distal enhancer-like, chr6:116888741-116889057); gene RFX6; cell type Prostate luminal/adenocarcinoma epithelium (LNCaP, ACH-000977).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | QBiC-SELEX gives HOXB13 its own model with the largest effect in the screen (z -103.49, effect -4.771; ref 99.9th vs alt 97.2th percentile k-mer strength), so ref T is predicted to bind more. Within Homeodomain group G024 (HOXA13/C13/D13 share the specificity) HOXB13 is chosen because it is by far the most expressed member in LNCaP (182.31 vs 4.13, 0.01, 0.01 TPM) and is the prostate master TF reported in a complex at this enhancer. This is an in vitro prediction only: no allele-specific HOXB13 assay is shown, and Factorbook finds no HOXB13 peak containing the variant in LNCaP-matching biosamples (absence may reflect no experiment). | weak | [E07](#e07), [E08](#e08), [E06d](#e06d), [E19](#e19) |
| element | The variant lies in a distal enhancer-like cCRE with DNase/H3K27ac signal (z-scores are maxima over biosamples, not LNCaP-specific), described in the literature as the rs339331/6q22 prostate risk enhancer carrying a HOXB13-containing complex. | supported | [E03](#e03), [E06d](#e06d) |
| gene | The enhancer is assigned to RFX6: the variant is intronic to RFX6, RFX6 has the nearest TSS, L2G scores RFX6 highest (0.87, though 0.27-0.87 across sets), and GATA2/SMAD4/HOXB13 at this enhancer are reported to increase RFX6 expression. No GTEx prostate eQTL is significant for this variant, so the steady-state effect in normal prostate is small or absent. | weak | [E01](#e01), [E02](#e02), [E05](#e05), [E06d](#e06d), [E20](#e20) |
| cell_type | HOXB13 is highly expressed in LNCaP (182.31 TPM) and the enhancer is described as an AR/HOXB13-associated site in prostate tumors; LNCaP-specific chromatin tracks are not shown here. | weak | [E08](#e08), [E06c](#e06c), [E06d](#e06d) |
| phenotype | The locus is a genome-wide significant prostate cancer risk locus (p 5e-20) and RFX6 dysregulation is reported to affect tumour proliferation, migration and prognosis; the allele-to-RFX6-to-phenotype step is not directly demonstrated in the cited quotes. | weak | [E04](#e04), [E06a](#e06a), [E06b](#e06b) |

Predictions: HOXB13 ChIP-seq in heterozygous LNCaP/prostate tumours shows allele-imbalanced occupancy favouring T; CRISPRi or deletion of EH38E2496909 lowers RFX6 but not GPRC6A in LNCaP; HOXB13 knockdown reduces RFX6 and abolishes the allelic reporter difference, while enzalutamide does not; EMSA: T-allele oligo gives stronger HOXB13 binding

Falsified if: Targeted HOXB13 ChIP in LNCaP shows no occupancy or no allelic imbalance at chr6:116888889; Enhancer deletion leaves RFX6 unchanged; Allelic reporter difference persists after HOXB13 depletion

### 2. H5: Null: no TF-binding-mediated effect of rs339331 itself (p = 0.30)

Null chain: no TF-mediated effect of this variant.

Predictions: Fine-mapping PIP for rs339331 stays modest (max 0.23) and a linked variant in the same LD block carries the functional allelic effect; No significant prostate eQTL for RFX6 at this variant, consistent with E20; Reporter and CRISPR base-editing of rs339331 alone produce no RFX6 change; No allelic imbalance in ChIP or ATAC at this position in heterozygous prostate samples

Falsified if: Base editing T>C at this exact position changes RFX6 expression or enhancer activity; Reproducible allele-specific TF occupancy is observed at chr6:116888889

### 3. H2: Ref T strengthens a reprogrammed androgen receptor binding site, increasing AR-driven RFX6 output (p = 0.24)

TF AR (stated coverage own_model; registry own_model), ref allele binds more; element cCRE EH38E2496909 / reprogrammed AR binding site at rs339331; gene RFX6; cell type AR-positive prostate adenocarcinoma cells (LNCaP).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | Published functional work reports rs339331 lies in a reprogrammed AR binding site with the T risk allele enhancing AR chromatin occupancy. QBiC-SELEX lookup shows AR has its own model, but it does not pass the gate at this site (z 0.94, p 0.35) and its small effect is positive (alt slightly favoured); only the CIS-BP-mapped NR3C2 model passes (effect +0.811, alt binds more). So in vitro motif data do not support, and mildly oppose, a T-favoured direct AR contact: the reported T-allele AR gain is more likely indirect, via a cooperating pioneer factor (e.g. HOXB13/GATA2) rather than direct AR half-site change. | weak | [E06c](#e06c), [E18](#e18) |
| element | The same distal enhancer-like cCRE harbours the reported AR site and carries active enhancer marks. | supported | [E03](#e03), [E06c](#e06c) |
| gene | Enhancer activity at this site is reported to drive RFX6 (shown for the GATA2/SMAD4/HOXB13 complex, not for AR directly); RFX6 is also the host gene and top L2G gene. | weak | [E01](#e01), [E05](#e05), [E06d](#e06d) |
| cell_type | AR reprogramming to this site is reported in prostate tumours; LNCaP is AR-positive but is not named in the quoted evidence and AR occupancy there is untested. | weak | [E06c](#e06c) |
| phenotype | The inherited allele is reported to confer prostate cancer progression and drug resistance via RFX6/HOXA10-orchestrated TGFbeta signalling, at a locus associated with prostate cancer at p 5e-20. | weak | [E06b](#e06b), [E04](#e04) |

Predictions: AR ChIP-seq in LNCaP shows androgen-dependent occupancy with allelic imbalance favouring T; Enzalutamide or AR knockdown abolishes the allelic difference in RFX6 expression / reporter activity; Effect is absent in AR-negative prostate or non-prostate lines; Direct AR motif-disrupting EMSA shows little allelic difference with purified AR DBD (indirect, cofactor-dependent occupancy)

Falsified if: AR ChIP shows no occupancy at chr6:116888889 in LNCaP or prostate tumours; RFX6 allelic expression difference is androgen-independent; AR depletion leaves enhancer reporter allelic difference intact

### 4. H3: Ref T preserves a posterior-HOX (HOXA10/HOXC6-type) site; alt C weakens it, altering RFX6 output (p = 0.07)

TF HOXA10 (stated coverage own_model; registry own_model), ref allele binds more; element cCRE EH38E2496909; gene RFX6; cell type LNCaP prostate adenocarcinoma.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | Homeodomain group G004 (18 concordant passing models, best HOXC10 z -84.28, effect -4.457; ref 100th vs alt 89.4th percentile) predicts the alt C allele binds this posterior-HOX specificity less. This is a group-level specificity, not one TF: I name HOXA10 because it has its own model and is expressed in LNCaP (4.23 TPM) and is the RFX6 partner named downstream in the literature, but HOXC6 (18.43 TPM, mapped), MNX1 (8.35) and HOXC12 (6.33) are better-expressed alternatives that the motif cannot distinguish. No allele-specific occupancy data exist for any of them. | weak | [E07](#e07), [E09](#e09) |
| element | The affected k-mer lies inside the active distal enhancer-like cCRE containing the variant; no direct evidence places a posterior-HOX site there. | weak | [E03](#e03) |
| gene | The enhancer is assigned to RFX6 by host-gene status, proximity and L2G, with no HOXA10-specific link to RFX6 from this element. | weak | [E01](#e01), [E02](#e02), [E05](#e05) |
| cell_type | Posterior HOX factors are expressed in LNCaP (HOXC6 18.43, MNX1 8.35, HOXA10 4.23 TPM), but expression does not demonstrate occupancy. | weak | [E09](#e09) |
| phenotype | The locus associates with prostate cancer (p 5e-20) and an RFX6/HOXA10 TGFbeta axis is reported downstream; no quote links posterior-HOX binding at this allele to phenotype. | weak | [E04](#e04), [E06b](#e06b) |

Predictions: HOXA10 (or HOXC6) ChIP shows occupancy with T-favoured imbalance at the enhancer, independent of HOXB13; Allelic enhancer activity persists after HOXB13 depletion but is lost after posterior-HOX knockdown

Falsified if: No posterior-HOX factor occupies the enhancer in prostate cells; Knockdown of HOXA10/HOXC6 leaves RFX6 and enhancer activity unchanged

### 5. H4: Alt C creates an IRF-family (IRF3/IRF6) binding site that alters enhancer activity (p = 0.05)

TF IRF3 (stated coverage own_model; registry own_model), alt allele binds more; element cCRE EH38E2496909; gene RFX6; cell type LNCaP prostate adenocarcinoma.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | Several IRF models score positively at this site (IRF3 own model, z 44.89, effect 2.092, ref 80.5th to alt 100th percentile; IRF6 own model z 56.39). IRF3 is chosen because it is the most expressed IRF in LNCaP (54.41 TPM) and has its own model; IRF6 (38.37 TPM) cannot be excluded from motif data alone. The predicted direction (alt binds more) is opposite to the published T-risk-allele AR/HOXB13 mechanism. | weak | [E07](#e07), [E12](#e12), [E10](#e10) |
| element | A gained IRF site would fall in the active distal enhancer-like cCRE containing the variant; no IRF footprint is documented there. | weak | [E03](#e03) |
| gene | Changed enhancer activity would act on RFX6, the host and top L2G gene; no IRF-RFX6 link is shown, and no prostate eQTL is detected. | weak | [E01](#e01), [E05](#e05), [E20](#e20) |
| cell_type | IRF3 is abundantly expressed in LNCaP (54.41 TPM), consistent with but not demonstrating occupancy. | weak | [E12](#e12) |
| phenotype | C is the GWAS risk allele for prostate cancer (p 5e-20) and RFX6 dysregulation is linked to tumour behaviour generally. | weak | [E04](#e04), [E06a](#e06a) |

Predictions: IRF3 (or IRF6) ChIP-seq shows C-allele-specific occupancy at this site; Interferon stimulation amplifies the allelic difference in enhancer reporter activity; Allelic effect survives HOXB13 and AR depletion

Falsified if: No IRF3/IRF6 occupancy detected at the enhancer in prostate cells; Allelic reporter difference unchanged by IRF3 depletion or IFN stimulation

## Prediction matrix

| Test | Cost | Separates top two | H1 | H5 | H2 | H3 | H4 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Targeted HOXB13 ChIP (or re-analysis of LNCaP/prostate tumour HOXB13 ChIP-seq) for allelic imbalance at chr6:116888889 in heterozygotes | low | yes | Peak present with imbalance favouring T | No peak or no allelic imbalance | Peak may be present (co-binding complex) but AR is the allele-sensitive factor; imbalance weaker or AR-dependent | Little or no HOXB13 imbalance; posterior-HOX factor responsible | No HOXB13 imbalance; if anything C-favoured IRF occupancy |
| AR ChIP-seq in androgen-stimulated LNCaP, allelic imbalance at the variant | low | yes | AR peak possible but imbalance secondary to HOXB13; persists after AR-independent manipulation | No allelic imbalance | Androgen-dependent AR peak with T-favoured imbalance | No requirement for AR occupancy | No AR imbalance |
| Allelic luciferase reporter of the 316 bp cCRE in LNCaP with HOXB13 vs AR knockdown | medium | yes | T > C activity; difference lost on HOXB13 knockdown, retained on AR knockdown | No allelic difference | T > C activity; difference lost on AR knockdown/enzalutamide | T > C activity retained after both knockdowns | C > T activity, IFN-responsive |
| Prostate eQTL / allele-specific RFX6 expression lookup (GTEx v8 already run) | existing data | no | No normal-tissue eQTL expected; effect tumour/context-specific (consistent with E20) | No eQTL, as observed | No normal-tissue eQTL; androgen/tumour-context dependent | Possible weak eQTL; none observed | Possible eQTL with opposite direction; none observed |
| Base editing of T>C at chr6:116888889 in heterozygous LNCaP, measure RFX6 | high | yes | RFX6 falls with C allele; HOXB13 occupancy falls | No change in RFX6 or chromatin | RFX6 falls with C allele; AR occupancy falls, androgen-dependent | RFX6 falls, HOXB13/AR occupancy unchanged | RFX6 changes with gained IRF occupancy at C |
| IRF3/IRF6 ChIP or IFN-stimulated reporter at the enhancer | medium | no | No IRF occupancy | No IRF occupancy or allelic effect | No IRF occupancy | No IRF occupancy | C-allele IRF occupancy, IFN-amplified |

## Next experiment

Re-analyse existing LNCaP/prostate-tumour HOXB13 and AR ChIP-seq in rs339331 heterozygotes for allele-specific reads at chr6:116888889 (with androgen-stimulated and vehicle AR data): a T-favoured HOXB13 imbalance that is androgen-independent supports H1, while a T-favoured, androgen-dependent AR imbalance without HOXB13 imbalance supports H2; no imbalance for either supports the null.

## Investigate calls

- qbic_tf_detail({"tf": "AR"})
- chip_peaks({"tf": "HOXB13", "biosample": "LNCaP"})
- eqtl_lookup({"tissue": "Prostate"})

## Flags

- none

Citation support: 1.00 of links cite only evidence that passed every check.

## Evidence

<a id="e01"></a>**E01** variant_annotation, Ensembl VEP (GRCh38) (https://rest.ensembl.org/vep/human/region/6:116888889-116888889:1/C?content-type=application/json&Conservation=1; retrieved 2026-10-25T17:26:00+00:00)

> Variant chr6:116888889:T>C (GRCh38), allele string T/C
> Known IDs: rs339331
> Most severe consequence: intron_variant
> Regulatory features: none
> GERP conservation score at the site: 1.28
> Transcript consequences: RFX6 (intron_variant); RFX6 (intron_variant, non_coding_transcript_variant)

<a id="e02"></a>**E02** nearest_genes, Ensembl overlap (protein_coding) (https://rest.ensembl.org/overlap/region/human/6:115888889-117888889?feature=gene;biotype=protein_coding;content-type=application/json; retrieved 2026-10-25T17:26:06+00:00)

> 24 protein-coding genes within 1000 kb of chr6:116888889:T>C, by distance to TSS:
> RFX6: 11.7 kb from TSS (in gene body, strand +1)
> GPRC6A: 59.8 kb from TSS (upstream, strand -1)
> FAM162B: 123.1 kb from TSS (upstream, strand -1)
> KPNA5: 207.7 kb from TSS (downstream, strand +1)
> ZUP1: 220.1 kb from TSS (upstream, strand -1)
> RSPH4A: 272.4 kb from TSS (downstream, strand +1)
> RWDD1: 317.5 kb from TSS (downstream, strand +1)
> TRAPPC3L: 343.2 kb from TSS (upstream, strand -1)
> CALHM4: 359.9 kb from TSS (downstream, strand +1)
> VGLL2: 376.7 kb from TSS (upstream, strand +1)

<a id="e03"></a>**E03** ccre_lookup, ENCODE v4 cCRE registry (ENCFF420VPZ) and SCREEN (https://screen-beta-api.wenglab.org/dataws/cre_table; retrieved 2026-10-25T17:25:50+00:00)

> The variant lies in cCRE EH38E2496909 (dELS: distal enhancer-like), chr6:116888741-116889057.
> SCREEN: 1 cCREs within 500 bp (max z-score across ENCODE biosamples):
> EH38E2496909 dELS (contains the variant): DNase z 2.2, H3K27ac z 1.7, H3K4me3 z 1.4, CTCF z 1.5; nearby genes RFX6, GPRC6A, FAM162B
> Biosample-specific z-scores are not in this call; the values above are maxima over biosamples.

<a id="e04"></a>**E04** gwas_lookup, GWAS Catalog REST v2 (https://www.ebi.ac.uk/gwas/rest/api/v2/associations?rs_id=rs339331&size=100; retrieved 2026-10-25T17:26:01+00:00)

> 13 GWAS Catalog associations for rs339331, strongest first:
> Prostate cancer: p 5.0e-20, effect allele C, risk-allele frequency 0.367114986, PMID 32514122
> Phospholipids in small HDL: p 2.0e-13, effect allele C, risk-allele frequency NR, PMID 41044249
> Total lipids in small HDL: p 2.0e-13, effect allele C, risk-allele frequency NR, PMID 41044249
> Concentration of small HDL particles: p 5.0e-12, effect allele C, risk-allele frequency NR, PMID 41044249
> Cholesterol in Small HDL: p 1.0e-11, effect allele C, risk-allele frequency NR, PMID 41044249
> Prostate-specific antigen levels: p 4.0e-09, effect allele T, risk-allele frequency NR, PMID 39930085

<a id="e05"></a>**E05** finemap_lookup, Open Targets Platform (credible sets, L2G) (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-25T17:26:00+00:00)

> 95 credible sets contain 6_116888889_T_C: 94 GWAS, 1 molecular QTL.
> GWAS Cancer of prostate (PheCode 185): PIP 0.23; L2G RFX6 0.87, GPRC6A 0.05
> GWAS Prostate cancer: PIP 0.07; L2G RFX6 0.42, GPRC6A 0.12
> GWAS Prostate cancer: PIP 0.07; L2G RFX6 0.75, GPRC6A 0.06
> GWAS Prostate cancer: PIP 0.06; L2G RFX6 0.27, GPRC6A 0.16
> GWAS Prostate cancer: PIP 0.06; L2G RFX6 0.61
> GWAS Cancer of prostate (PheCode 185): PIP 0.06; L2G RFX6 0.75
> pqtl for SCG2 (UKB_PPP_EUR_SCG2_P13521_OID21400_v1): PIP 0.01
> Best L2G gene scores across these sets: RFX6 0.87, NUS1 0.55, GPRC6A 0.38, ROS1 0.11

<a id="e06"></a>**E06** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=rs339331%20AND%20RFX6%20AND%20%22prostate%20cancer%22&format=json&pageSize=8&resultType=core; retrieved 2026-10-25T17:26:07+00:00)

> Europe PMC: 67 hits for 'rs339331 AND RFX6 AND "prostate cancer"'; top 7 with PMIDs:
> PMID 41422049 (2025): Multifaceted functions of transcription regulatory factor X6 (RFX6): from pancreatic development to cancer progression.
> PMID 38932472 (2024): An Inherited Allele Confers Prostate Cancer Progression and Drug Resistance via RFX6/HOXA10-Orchestrated TGFβ Signaling.
> PMID 40181298 (2025): Genetic associations of prostate cancer in China: a systematic review.
> PMID 37550764 (2023): GATA2 co-opts TGFβ1/SMAD4 oncogenic signaling and inherited variants at 6q22 to modulate prostate cancer progression.
> PMID 41374944 (2025): The Clinical Relevance of Tumor Biomarkers in Prostate Cancer-A Review.
> PMID 38052806 (2023): Prostate cancer genetic risk and associated aggressive disease in men of African ancestry.
> PMID 41432001 (2026): Insights into human history and complex traits from the genomes of African populations.

<a id="e06a"></a>**E06a** literature_search, Europe PMC abstract, PMID 41422049 (https://europepmc.org/article/MED/41422049; retrieved 2026-10-25T17:26:07+00:00)

> Dysregulated expression or mutations of the RFX6 gene in prostate cancer, hepatocellular carcinoma, gastric cancer, melanoma, and other tumors have garnered significant interest, with studies showing that such alterations affect tumor cell proliferation, migration, and invasion, and are correlated with an unfavorable clinical prognosis in patients carrying RFX6 mutations.

<a id="e06b"></a>**E06b** literature_search, Europe PMC abstract, PMID 38932472 (https://europepmc.org/article/MED/38932472; retrieved 2026-10-25T17:26:07+00:00)

> Here the FinnGen cohort phenome-wide analysis, along with multiple genome-wide association studies, has consistently identified the rs339331-RFX6/6q22 locus associated with prostate cancer (PCa) risk across diverse populations.

<a id="e06c"></a>**E06c** literature_search, Europe PMC abstract, PMID 38932472 (https://europepmc.org/article/MED/38932472; retrieved 2026-10-25T17:26:07+00:00)

> It is uncovered that rs339331 resides in a reprogrammed androgen receptor (AR) binding site in PCa tumors, with the T risk allele enhancing AR chromatin occupancy.

<a id="e06d"></a>**E06d** literature_search, Europe PMC abstract, PMID 37550764 (https://europepmc.org/article/MED/37550764; retrieved 2026-10-25T17:26:07+00:00)

> Strinkingly, GATA2 and SMAD4 globally mediated inherited PCa risk and formed a transcriptional complex with HOXB13 at the PCa risk-associated rs339331/6q22 enhancer, leading to increased expression of the PCa susceptibility gene RFX6.

<a id="e06e"></a>**E06e** literature_search, Europe PMC abstract, PMID 38052806 (https://europepmc.org/article/MED/38052806; retrieved 2026-10-25T17:26:07+00:00)

> Notable genes of interest include HCP5, RFX6 and H3C1 for risk, and MKI67 and KLF5 for aggressive disease.

<a id="e07"></a>**E07** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> QBiC-SELEX screen of chr6:116888889:T>C: 997 models scored, 487 pass the gate (Bonferroni 0.05/997, p < 5.02e-05, |z| > 4.05), in 361 CIS-BP groups. Expression context: DepMap line ACH-000977. Groups shown: 10; dropped because no TF in the group reaches 1 TPM: 91 (Homeodomain, 3 models z -77.59, IRF, 2 models z 70.98, Unknown, 1 model z -31.89, bHLH, 1 model z 17.52, Unknown, 1 model z 17.51). Passing groups ranked below the ones shown: 260. In the group rows, 'own model' means the TF has its own QBiC-SELEX model and 'mapped' that it is covered only through CIS-BP-mapped models of related TFs. A TF not named in any group row may still have its own model, even one that passes the gate: look it up with qbic_tf_detail before stating its coverage or a QBiC-SELEX direction for it. predicted_effect > 0 means the alternate allele binds more strongly. In vitro binding only: expression and chromatin decide whether a change matters.

<a id="e08"></a>**E08** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G024 (Homeodomain, 4 models): best model HOXB13_NA_TGCCTG20NGA_ESY_yang2017_0_3_7mer (own model of HOXB13), z -103.49, effect -4.771 (alt binds less); 4 passing models (4 with the best model's sign). Passing members: HOXB13 z -103.49, HOXA13 z -74.87, HOXD13 z -69.26, HOXC13 z -64.27. TFs this group covers: HOXB13 (own model) 182.31 TPM, HOXC13 (own model) 4.13 TPM, HOXA13 (own model) 0.01 TPM, HOXD13 (own model) 0.01 TPM; best model's site strength: ref 99.9th, alt 97.2th percentile of its k-mer coefficients.

<a id="e09"></a>**E09** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G004 (Homeodomain, 18 models): best model HOXC10_FL_TTGGCC40NTCG_KX_yin2017_0_3_7mer (own model of HOXC10), z -84.28, effect -4.457 (alt binds less); 18 passing models (18 with the best model's sign). Passing members: HOXC10 z -84.28, HOXD10 z -80.29, HOXC12 z -75.59, HOXC9 z -71.63, HOXD11 z -68.62 (+13 more). TFs this group covers: HOXC6 (mapped) 18.43 TPM, MNX1 (own model) 8.35 TPM, HOXC12 (own model) 6.33 TPM, HOXC4 (own model) 5.27 TPM, HOXA10 (own model) 4.23 TPM, HOXA6 (own model) 2.75 TPM, HOXA5 (own model) 1.94 TPM, HOXC10 (own model) 1.89 TPM, HOXC9 (own model) 1.78 TPM, HOXB9 (own model) 1.77 TPM (+24 more); best model's site strength: ref 100.0th, alt 89.4th percentile of its k-mer coefficients.

<a id="e10"></a>**E10** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G080 (IRF, 2 models): best model IRF6_eDBD_TCTAGT40NAAC_KS_yin2017_0_4_7mer (own model of IRF6), z 56.39, effect 2.918 (alt binds more); 2 passing models (2 with the best model's sign). Passing members: IRF6 z 56.39, IRF5 z 16.69. TFs this group covers: IRF6 (own model) 38.37 TPM, IRF5 (own model) 5.53 TPM; best model's site strength: ref 73.0th, alt 98.5th percentile of its k-mer coefficients.

<a id="e11"></a>**E11** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G302 (C2H2 ZF, 1 model): best model PRDM4_eDBD_TAAATC40NGTT_KT_yin2017_0_4_7mer (own model of PRDM4), z 47.33, effect 3.137 (alt binds more); 1 passing models (1 with the best model's sign). Passing members: PRDM4 z 47.33. TFs this group covers: PRDM4 (own model) 10.83 TPM; best model's site strength: ref 99.3th, alt 100.0th percentile of its k-mer coefficients.

<a id="e12"></a>**E12** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G213 (IRF, 1 model): best model IRF3_eDBD_TGAGAA40NGCG_KS_yin2017_0_4_7mer (own model of IRF3), z 44.89, effect 2.092 (alt binds more); 1 passing models (1 with the best model's sign). Passing members: IRF3 z 44.89. TFs this group covers: IRF3 (own model) 54.41 TPM; best model's site strength: ref 80.5th, alt 100.0th percentile of its k-mer coefficients.

<a id="e13"></a>**E13** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G228 (bHLH, 1 model): best model MAX_FL_TG40NGACCTT_YWN_jolma2025_0_3_7mer (own model of MAX), z 28.99, effect 1.595 (alt binds more); 1 passing models (1 with the best model's sign). Passing members: MAX z 28.99. TFs this group covers: MAX (own model) 61.61 TPM; best model's site strength: ref 63.6th, alt 96.8th percentile of its k-mer coefficients.

<a id="e14"></a>**E14** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G212 (IRF, 1 model): best model IRF2_FL_TTCATT40NTAT_KX_yin2017_0_3_7mer (own model of IRF2), z 25.39, effect 2.187 (alt binds more); 1 passing models (1 with the best model's sign). Passing members: IRF2 z 25.39. TFs this group covers: IRF2 (own model) 8.32 TPM, IRF1 (mapped) 5.75 TPM; best model's site strength: ref 89.1th, alt 99.1th percentile of its k-mer coefficients.

<a id="e15"></a>**E15** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G460 (C2H2 ZF, 1 model): best model ZNF230_FL_TG40NGACCTT_YWDA_jolma2025_0_3_7mer (own model of ZNF230), z -23.63, effect -0.439 (alt binds less); 1 passing models (1 with the best model's sign). Passing members: ZNF230 z -23.63. TFs this group covers: ZNF230 (own model) 1.65 TPM; best model's site strength: ref 98.9th, alt 93.9th percentile of its k-mer coefficients.

<a id="e16"></a>**E16** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G367 (Unknown, 1 model): best model THYN1_FL_TG40NCTGTGG_YWFA_jolma2025_0_4_7mer (own model of THYN1), z 22.24, effect 0.173 (alt binds more); 1 passing models (1 with the best model's sign). Passing members: THYN1 z 22.24. TFs this group covers: THYN1 (own model) 37.42 TPM; best model's site strength: ref 36.3th, alt 74.1th percentile of its k-mer coefficients.

<a id="e17"></a>**E17** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G467 (C2H2 ZF, 1 model): best model ZNF260_FL_AT40NCCTTGG_AATA_jolma2025_0_3_7mer (own model of ZNF260), z -20.85, effect -0.516 (alt binds less); 1 passing models (1 with the best model's sign). Passing members: ZNF260 z -20.85. TFs this group covers: ZNF260 (own model) 13.26 TPM; best model's site strength: ref 99.5th, alt 92.9th percentile of its k-mer coefficients.

<a id="e18"></a>**E18** qbic_tf_detail, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> {"tf":"AR","symbol":"AR","via":"hgnc_symbol","notes":[],"coverage":"own_model","variant":"chr6:116888889:T>C","gate_p":5.02e-05,"models":[{"model":"AR_NA_TGCTCG20NGA_AF_jolma2013_1_3_7mer","mapping":"own","group":"G016 Nuclear receptor, 4 models","quality":0.601,"effect":0.035,"z":0.94,"p":0.35,"rank_abs_z":"866/997","passed_gate":false,"site_strength":{"ref_percentile":70.4,"alt_percentile":83.3,"k":7}},{"model":"GR_NA_Lib1_NA_bhimsaria2023_0(2)_2_7mer","mapping":"CIS-BP (NR3C1)","group":"G016 Nuclear receptor, 4 models","quality":0.913,"effect":0.083,"z":1.44,"p":0.15,"rank_abs_z":"799/997","passed_gate":false,"site_strength":{"ref_percentile":65.9,"alt_percentile":74.5,"k":7}},{"model":"NR3C2_eDBD_TGCTGG40NGCC_KT_yin2017_0_4_7mer","mapping":"CIS-BP (NR3C2)","group":"G016 Nuclear receptor, 4 models","quality":0.751,"effect":0.811,"z":9.5,"p":2e-21,"rank_abs_z":"135/997","passed_gate":true,"site_strength":{"ref_percentile":64.7,"alt_percentile":83.6,"k":7}},{"model":"PGR_NA_Lib1_NA_bhimsaria2023_0(3)_3_7mer","mapping":"CIS-BP (PGR)","group":"G016 Nuclear receptor, 4 models","quality":0.544,"effect":0.108,"z":2.46,"p":0.014,"rank_abs_z":"660/997","passed_gate":false,"site_strength":{"ref_percentile":65.1,"alt_percentile":80.1,"k":7}}]}

<a id="e19"></a>**E19** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-25T17:27:22+00:00)

> No ENCODE HOXB13 ChIP-seq peak contains chr6:116888889:T>C in biosamples matching 'LNCaP'. Absence can also mean no HOXB13 experiment in that biosample. 0 peaks lie within 100 bp without containing it.

<a id="e20"></a>**E20** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr6_116888889_T_C_b38&datasetId=gtex_v8; retrieved 2026-10-25T17:27:22+00:00)

> 0 significant GTEx v8 single-tissue eQTLs for chr6_116888889_T_C_b38 in tissues matching 'Prostate'. NES is the effect of the alt allele (C) relative to ref (T).
