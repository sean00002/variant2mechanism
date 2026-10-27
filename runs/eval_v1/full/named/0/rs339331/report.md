# rs339331 and Prostate cancer (6q22)

Configuration `full`, named mode, seed 0. Models: generator claude-opus-5, critic claude-sonnet-5-5, summariser claude-haiku-5-5. Cost $0.61 over 7 model calls; 191 s.

Variant `chr6:116888889:T>C` (germline); expression context: DepMap:ACH-000977 (LNCaP clone FGC).

## QBiC-SELEX screen

487 of 997 models pass the gate. Top groups: Homeodomain, 4 models (best HOXB13, z -103.49); Homeodomain, 18 models (best HOXC10, z -84.28); IRF, 2 models (best IRF6, z 56.39); C2H2 ZF, 1 model (best PRDM4, z 47.33); IRF, 1 model (best IRF3, z 44.89).

## Ranked chains

### 1. H1: Ref T preserves a HOXB13 site in the 6q22 enhancer, supporting the GATA2/SMAD4/HOXB13 complex and RFX6 expression (p = 0.32)

TF HOXB13 (stated coverage own_model; registry own_model), ref allele binds more; element cCRE EH38E2496909 (distal enhancer-like, chr6:116888741-116889057); gene RFX6; cell type AR-positive prostate luminal/tumor epithelium (LNCaP, ACH-000977).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | QBiC own model of HOXB13 predicts a large loss of binding with alt C (z -103.5, effect -4.77; ref 99.9th vs alt 97.2nd percentile of k-mer coefficients), so ref T binds more; within group G024 HOXB13 is chosen because it is by far the most expressed member in LNCaP (182 TPM vs HOXC13 4.1, HOXA13/HOXD13 ~0). This is in vitro prediction only: ENCODE shows no HOXB13 peak at the site in LNCaP, though that may reflect no matching experiment. | weak | [E08](#e08), [E07](#e07), [E18](#e18) |
| element | The variant lies in a distal enhancer-like cCRE, described in the literature as the rs339331/6q22 prostate risk enhancer at which GATA2, SMAD4 and HOXB13 form a complex; cCRE z-scores are maxima across biosamples, not LNCaP-specific. | supported | [E03](#e03), [E06d](#e06d) |
| gene | The enhancer acts on RFX6: the variant is intronic to RFX6, RFX6 is the top L2G gene (0.87), and the HOXB13-containing complex at this enhancer is reported to increase RFX6 expression; no prostate eQTL is detected in GTEx v8, so the effect, if real, is below GTEx power or context-specific. | supported | [E01](#e01), [E02](#e02), [E05](#e05), [E06d](#e06d), [E19](#e19) |
| cell_type | HOXB13 is abundantly expressed in LNCaP (182 TPM) and the enhancer was characterized in prostate tumors and prostate lines; no LNCaP-specific allele-resolved chromatin data was retrieved. | weak | [E08](#e08), [E06d](#e06d), [E18](#e18) |
| phenotype | Altered RFX6 dosage from this enhancer affects proliferation, migration and TGFbeta-driven progression and the locus is genome-wide significant for prostate cancer; note the direction tension: E04 lists C as the prostate cancer effect allele while E06c calls T the risk/AR-enhancing allele and the PSA effect allele is T, so the risk direction is not settled. | weak | [E04](#e04), [E06a](#e06a), [E06b](#e06b), [E06c](#e06c) |

Predictions: Allele-specific HOXB13 ChIP (or ChIP in heterozygous tumors) shows stronger occupancy on the T allele at chr6:116888889.; HOXB13 knockdown in LNCaP reduces RFX6 mRNA and reduces enhancer reporter activity in a T-allele-dependent manner.; Base editing T>C at this single base lowers RFX6 in AR-positive prostate lines.

Falsified if: HOXB13 ChIP in prostate chromatin with an actual HOXB13 experiment shows no occupancy at EH38E2496909 or no allelic imbalance.; HOXB13 knockdown leaves the enhancer activity and RFX6 unchanged.

### 2. H5: Null: rs339331 is a tag for another causal variant on the 6q22 haplotype, with no TF-mediated effect of its own (p = 0.29)

Null chain: no TF-mediated effect of this variant.

Predictions: Fine-mapping PIP for rs339331 stays modest (0.06-0.23) and a linked variant in the credible set carries the signal.; Base editing only this base leaves RFX6 expression and enhancer reporter activity unchanged in prostate cells.; No allele-specific TF occupancy at this exact base in heterozygous prostate chromatin; GTEx prostate shows no eQTL (already observed).

Falsified if: A single-base allele swap or MPRA reproducibly changes RFX6 expression or enhancer activity.; Allele-specific AR or HOXB13 ChIP imbalance is demonstrated at this base.

### 3. H6: Ref T strengthens a reprogrammed AR binding site at the 6q22 enhancer, increasing RFX6 (p = 0.26)

TF AR (stated coverage not_checked; registry own_model), ref allele binds more; element cCRE EH38E2496909; gene RFX6; cell type AR-positive prostate tumor epithelium.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | Published functional work states rs339331 resides in a reprogrammed AR binding site in prostate tumors, with the T risk allele enhancing AR chromatin occupancy; this is direct allele-specific occupancy evidence rather than an in vitro model. AR was not assessed by QBiC here, and ENCODE shows no AR peak at the site in LNCaP biosamples (which may reflect the absence of a matching AR experiment or a tumor-specific reprogrammed site). | supported | [E06c](#e06c), [E20](#e20) |
| element | The site is an annotated distal enhancer-like cCRE and is the enhancer described at 6q22 in the AR/GATA2/HOXB13 literature. | supported | [E03](#e03), [E06c](#e06c), [E06d](#e06d) |
| gene | The enhancer's target is RFX6 (L2G 0.87, intronic to RFX6, literature states the complex increases RFX6 expression); GTEx prostate shows no significant eQTL, consistent with a tumor- or androgen-context-dependent effect. | supported | [E05](#e05), [E01](#e01), [E06d](#e06d), [E19](#e19) |
| cell_type | The reprogrammed AR site was mapped in prostate cancer tumors, i.e. AR-positive malignant epithelium rather than normal prostate. | supported | [E06c](#e06c) |
| phenotype | Allele-dependent AR occupancy drives RFX6/HOXA10-orchestrated TGFbeta signaling linked to progression and drug resistance, in a locus genome-wide significant for prostate cancer and PSA levels (T is the PSA effect allele). | weak | [E06b](#e06b), [E06c](#e06c), [E04](#e04), [E06a](#e06a) |

Predictions: AR ChIP-seq in androgen-stimulated prostate tumor cells heterozygous at rs339331 shows T-allele-biased reads; HOXB13 ChIP shows little or no allelic bias.; Enhancer reporter activity is androgen-dependent and higher with the T allele; enzalutamide abolishes the allelic difference.; AR knockdown, more than HOXB13 knockdown, collapses the allelic difference in RFX6 expression.

Falsified if: AR ChIP in heterozygous tumor material shows no peak or no allelic imbalance at this base.; Enhancer activity is androgen-independent and unaffected by AR depletion.

### 4. H2: Ref T preserves a broader posterior-HOX specificity site (HOXC6) acting on RFX6 (p = 0.08)

TF HOXC6 (stated coverage mapped; registry mapped), ref allele binds more; element cCRE EH38E2496909; gene RFX6; cell type Prostate tumor epithelium (LNCaP).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | QBiC group G004 (18 concordant homeodomain models, best HOXC10 z -84.3, effect -4.46; ref 100th vs alt 89.4th percentile) indicates alt C weakens an AT-rich posterior-HOX site. This group is a shared specificity, not one TF; among the covered members HOXC6 is the most expressed in LNCaP (18.4 TPM vs HOXA10 4.2, HOXC10 1.9), so HOXC6 is the best candidate on expression grounds. HOXC6 is covered only via CIS-BP-mapped models. | weak | [E09](#e09), [E07](#e07) |
| element | The same dELS cCRE contains the predicted homeodomain site; literature places a homeodomain-containing complex at this enhancer, though it names HOXB13 rather than HOXC6. | weak | [E03](#e03), [E06d](#e06d) |
| gene | RFX6 is the credible-set target (L2G 0.87) and the variant is in its intron. | supported | [E05](#e05), [E01](#e01) |
| cell_type | Several posterior HOX factors are expressed in LNCaP, so loss of this site is realizable in prostate cells; no occupancy data for HOXC6 at this element was retrieved. | weak | [E09](#e09) |
| phenotype | Reduced RFX6 enhancer drive in prostate epithelium would alter RFX6-dependent TGFbeta signaling at a locus genome-wide significant for prostate cancer. | weak | [E04](#e04), [E06a](#e06a), [E06b](#e06b) |

Predictions: HOXC6 (or another non-HOXB13 posterior HOX) ChIP shows occupancy and allelic bias at the element; HOXB13 knockdown alone does not abolish the allelic difference.; Mutating the AT-rich posterior-HOX core, leaving the HOXB13-preferred core intact, still reduces reporter activity.

Falsified if: HOXC6 depletion does not change RFX6 or enhancer activity.; All homeodomain occupancy at the element is attributable to HOXB13.

### 5. H3: Alt C creates an IRF6 site that alters enhancer output (p = 0.05)

TF IRF6 (stated coverage own_model; registry own_model), alt allele binds more; element cCRE EH38E2496909; gene RFX6; cell type Prostate tumor epithelium (LNCaP).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | QBiC own model of IRF6 gives the strongest IRF gain with alt C (z 56.4, effect 2.92; ref 73rd vs alt 98.5th percentile), with concordant gains for IRF3 (z 44.9) and IRF2 (z 25.4); IRF6 is chosen as the single TF because it has the top z in the IRF groups and is well expressed in LNCaP (38.4 TPM). | weak | [E10](#e10), [E12](#e12), [E14](#e14) |
| element | The gained site falls inside the same distal enhancer-like cCRE; whether an added IRF site raises or lowers output is unknown. | weak | [E03](#e03) |
| gene | Any change in this enhancer's output would act on RFX6, the mapped target gene; there is no evidence for an IRF-dependent effect on RFX6, and no prostate eQTL is seen. | missing | [E05](#e05), [E19](#e19) |
| cell_type | IRF6 and IRF3 are expressed in LNCaP, so an alt-specific IRF site could be occupied in prostate cells; no occupancy data were retrieved. | weak | [E10](#e10), [E12](#e12) |
| phenotype | If the C allele (the GWAS prostate cancer effect allele) gains IRF6 binding and raises enhancer output, higher RFX6 would promote proliferation and progression; this specific direction is untested. | missing | [E04](#e04), [E06a](#e06a) |

Predictions: IRF6 ChIP or CUT&RUN shows C-allele-specific occupancy at chr6:116888889.; IRF6 knockdown removes the allelic difference in reporter activity; interferon stimulation modulates the allelic difference.; Allelic effect is retained in AR-negative or androgen-deprived cells.

Falsified if: No IRF6 occupancy at this element in prostate chromatin.; Allelic reporter difference persists unchanged after IRF6 depletion.

## Prediction matrix

| Test | Cost | Separates top two | H1 | H5 | H6 | H2 | H3 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Reanalyze existing public AR and HOXB13 ChIP-seq from prostate tumors/lines heterozygous at rs339331 for allelic read imbalance | existing data | yes | HOXB13 reads biased to T (AR bias secondary or absent) | No allelic imbalance for either factor | AR reads biased to T; HOXB13 bias minimal | No HOXB13 imbalance; any homeodomain signal from other HOX factors | No AR or HOXB13 imbalance |
| Androgen-dependent allelic luciferase/MPRA of the 316 bp cCRE (T vs C) in LNCaP, +/- DHT and +/- enzalutamide | low | yes | T > C activity, largely androgen-independent | No allelic difference | T > C only with DHT; difference lost with enzalutamide | T > C activity, androgen-independent | C > T activity, modulated by interferon |
| siRNA/degron knockdown of HOXB13 vs AR in LNCaP, measure RFX6 mRNA and allelic enhancer activity | medium | yes | HOXB13 loss reduces RFX6 and abolishes allelic difference | RFX6 may change but no allele-specific component | AR loss reduces RFX6 and abolishes allelic difference | Neither fully abolishes it; HOXC6 depletion does | Neither changes the allelic difference |
| Base editing T>C at chr6:116888889 in an AR-positive prostate line, RNA-seq for RFX6 and GPRC6A | high | no | RFX6 decreases | No change in any nearby gene | RFX6 decreases, androgen-dependent | RFX6 decreases | RFX6 increases |
| IRF6 CUT&RUN in LNCaP at the element, allele-resolved | medium | no | No IRF6 signal | No IRF6 signal | No IRF6 signal | No IRF6 signal | C-allele-biased IRF6 signal |

## Next experiment

Reanalyze already-public AR and HOXB13 ChIP-seq datasets from prostate tumors and LNCaP-derived models that are heterozygous at rs339331, counting allele-resolved reads at chr6:116888889. This costs nothing new and directly separates H1 (T-biased HOXB13 occupancy) from H6 (T-biased AR occupancy), while a complete absence of imbalance in either factor supports the null H5.

## Investigate calls

- chip_peaks({"tf": "HOXB13", "biosample": "LNCaP"})
- eqtl_lookup({"tissue": "Prostate"})
- chip_peaks({"tf": "AR", "biosample": "LNCaP"})

## Flags

- coverage_misstated: H6: stated not_checked, registry says own_model for AR

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

> QBiC-SELEX screen of chr6:116888889:T>C: 997 models scored, 487 pass the gate (Bonferroni 0.05/997, p < 5.02e-05, |z| > 4.05), in 361 CIS-BP groups. Expression context: DepMap line ACH-000977. Groups shown: 10; dropped because no TF in the group reaches 1 TPM: 91 (Homeodomain, 3 models z -77.59, IRF, 2 models z 70.98, Unknown, 1 model z -31.89, bHLH, 1 model z 17.52, Unknown, 1 model z 17.51). predicted_effect > 0 means the alternate allele binds more strongly. In vitro binding only: expression and chromatin decide whether a change matters.

<a id="e08"></a>**E08** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G024 (Homeodomain, 4 models): best model HOXB13_NA_TGCCTG20NGA_ESY_yang2017_0_3_7mer (own model of HOXB13), z -103.49, effect -4.771 (alt binds less); 4 passing models (4 with the best model's sign). Passing members: HOXB13 z -103.49, HOXA13 z -74.87, HOXD13 z -69.26, HOXC13 z -64.27. TFs this group covers (own and CIS-BP-mapped models): HOXB13 182.31 TPM, HOXC13 4.13 TPM, HOXA13 0.01 TPM, HOXD13 0.01 TPM; best model's site strength: ref 99.9th, alt 97.2th percentile of its k-mer coefficients.

<a id="e09"></a>**E09** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G004 (Homeodomain, 18 models): best model HOXC10_FL_TTGGCC40NTCG_KX_yin2017_0_3_7mer (own model of HOXC10), z -84.28, effect -4.457 (alt binds less); 18 passing models (18 with the best model's sign). Passing members: HOXC10 z -84.28, HOXD10 z -80.29, HOXC12 z -75.59, HOXC9 z -71.63, HOXD11 z -68.62 (+13 more). TFs this group covers (own and CIS-BP-mapped models): HOXC6 18.43 TPM, MNX1 8.35 TPM, HOXC12 6.33 TPM, HOXC4 5.27 TPM, HOXA10 4.23 TPM, HOXA6 2.75 TPM, HOXA5 1.94 TPM, HOXC10 1.89 TPM, HOXC9 1.78 TPM, HOXB9 1.77 TPM (+24 more); best model's site strength: ref 100.0th, alt 89.4th percentile of its k-mer coefficients.

<a id="e10"></a>**E10** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G080 (IRF, 2 models): best model IRF6_eDBD_TCTAGT40NAAC_KS_yin2017_0_4_7mer (own model of IRF6), z 56.39, effect 2.918 (alt binds more); 2 passing models (2 with the best model's sign). Passing members: IRF6 z 56.39, IRF5 z 16.69. TFs this group covers (own and CIS-BP-mapped models): IRF6 38.37 TPM, IRF5 5.53 TPM; best model's site strength: ref 73.0th, alt 98.5th percentile of its k-mer coefficients.

<a id="e11"></a>**E11** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G302 (C2H2 ZF, 1 model): best model PRDM4_eDBD_TAAATC40NGTT_KT_yin2017_0_4_7mer (own model of PRDM4), z 47.33, effect 3.137 (alt binds more); 1 passing models (1 with the best model's sign). Passing members: PRDM4 z 47.33. TFs this group covers (own and CIS-BP-mapped models): PRDM4 10.83 TPM; best model's site strength: ref 99.3th, alt 100.0th percentile of its k-mer coefficients.

<a id="e12"></a>**E12** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G213 (IRF, 1 model): best model IRF3_eDBD_TGAGAA40NGCG_KS_yin2017_0_4_7mer (own model of IRF3), z 44.89, effect 2.092 (alt binds more); 1 passing models (1 with the best model's sign). Passing members: IRF3 z 44.89. TFs this group covers (own and CIS-BP-mapped models): IRF3 54.41 TPM; best model's site strength: ref 80.5th, alt 100.0th percentile of its k-mer coefficients.

<a id="e13"></a>**E13** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G228 (bHLH, 1 model): best model MAX_FL_TG40NGACCTT_YWN_jolma2025_0_3_7mer (own model of MAX), z 28.99, effect 1.595 (alt binds more); 1 passing models (1 with the best model's sign). Passing members: MAX z 28.99. TFs this group covers (own and CIS-BP-mapped models): MAX 61.61 TPM; best model's site strength: ref 63.6th, alt 96.8th percentile of its k-mer coefficients.

<a id="e14"></a>**E14** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G212 (IRF, 1 model): best model IRF2_FL_TTCATT40NTAT_KX_yin2017_0_3_7mer (own model of IRF2), z 25.39, effect 2.187 (alt binds more); 1 passing models (1 with the best model's sign). Passing members: IRF2 z 25.39. TFs this group covers (own and CIS-BP-mapped models): IRF2 8.32 TPM, IRF1 5.75 TPM; best model's site strength: ref 89.1th, alt 99.1th percentile of its k-mer coefficients.

<a id="e15"></a>**E15** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G460 (C2H2 ZF, 1 model): best model ZNF230_FL_TG40NGACCTT_YWDA_jolma2025_0_3_7mer (own model of ZNF230), z -23.63, effect -0.439 (alt binds less); 1 passing models (1 with the best model's sign). Passing members: ZNF230 z -23.63. TFs this group covers (own and CIS-BP-mapped models): ZNF230 1.65 TPM; best model's site strength: ref 98.9th, alt 93.9th percentile of its k-mer coefficients.

<a id="e16"></a>**E16** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G367 (Unknown, 1 model): best model THYN1_FL_TG40NCTGTGG_YWFA_jolma2025_0_4_7mer (own model of THYN1), z 22.24, effect 0.173 (alt binds more); 1 passing models (1 with the best model's sign). Passing members: THYN1 z 22.24. TFs this group covers (own and CIS-BP-mapped models): THYN1 37.42 TPM; best model's site strength: ref 36.3th, alt 74.1th percentile of its k-mer coefficients.

<a id="e17"></a>**E17** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G467 (C2H2 ZF, 1 model): best model ZNF260_FL_AT40NCCTTGG_AATA_jolma2025_0_3_7mer (own model of ZNF260), z -20.85, effect -0.516 (alt binds less); 1 passing models (1 with the best model's sign). Passing members: ZNF260 z -20.85. TFs this group covers (own and CIS-BP-mapped models): ZNF260 13.26 TPM; best model's site strength: ref 99.5th, alt 92.9th percentile of its k-mer coefficients.

<a id="e18"></a>**E18** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-25T17:27:22+00:00)

> No ENCODE HOXB13 ChIP-seq peak contains chr6:116888889:T>C in biosamples matching 'LNCaP' (0 peaks within 100 bp). Absence can also mean no HOXB13 experiment in that biosample.

<a id="e19"></a>**E19** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr6_116888889_T_C_b38&datasetId=gtex_v8; retrieved 2026-10-25T17:27:22+00:00)

> 0 significant GTEx v8 single-tissue eQTLs for chr6_116888889_T_C_b38 in tissues matching 'Prostate'. NES is the effect of the alt allele (C) relative to ref (T).

<a id="e20"></a>**E20** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-25T17:27:23+00:00)

> No ENCODE AR ChIP-seq peak contains chr6:116888889:T>C in biosamples matching 'LNCaP' (0 peaks within 100 bp). Absence can also mean no AR experiment in that biosample.
