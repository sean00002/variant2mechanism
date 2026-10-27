# rs339331 and Prostate cancer (6q22)

Configuration `no_qbic`, named mode, seed 0. Models: generator claude-opus-5, critic claude-sonnet-5-5, summariser claude-haiku-5-5. Cost $0.58 over 7 model calls; 176 s.

Variant `chr6:116888889:T>C` (germline); expression context: DepMap:ACH-000977 (LNCaP clone FGC).

## Ranked chains

### 1. H2: Ref T allele strengthens a tumour-reprogrammed androgen receptor binding site in the 6q22 enhancer, raising RFX6 (p = 0.27)

TF AR (stated coverage not_checked; registry own_model), ref allele binds more; element EH38E2496909 (dELS, chr6:116888741-116889057), within RFX6 intron; gene RFX6; cell type AR-positive prostate cancer cells (LNCaP clone FGC, ACH-000977).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The only allele-specific binding statement in the evidence is for AR: rs339331 lies in an AR binding site reprogrammed in PCa tumours, with the T allele enhancing AR chromatin occupancy. No QBiC-SELEX row or detail lookup for AR was provided, so coverage is not_checked; ENCODE LNCaP AR ChIP shows no peak containing the site, which may reflect absence of a matching experiment or tumour-specific (not cell-line) reprogramming. | supported | [E06c](#e06c), [E08](#e08) |
| element | The variant sits in a distal enhancer-like cCRE with DNase/H3K27ac/CTCF signal; the z-scores are maxima across biosamples, so prostate-specific activity is not demonstrated here. | weak | [E03](#e03), [E01](#e01) |
| gene | RFX6 is the most likely target: the variant is intronic to RFX6, 11.7 kb from its TSS, and RFX6 is the top L2G gene (0.87) in prostate cancer credible sets. No eQTL or contact data in the evidence connect the element to RFX6, and GTEx prostate shows no significant eQTL. | weak | [E01](#e01), [E02](#e02), [E05](#e05), [E09](#e09) |
| cell_type | An AR-dependent effect is restricted to AR-positive prostate luminal/tumour cells, the context described for the reprogrammed AR site and matching the LNCaP expression context; AR expression in ACH-000977 was not supplied. | weak | [E06c](#e06c) |
| phenotype | Altered RFX6 levels are linked to prostate tumour proliferation, invasion and prognosis, and rs339331 is a genome-wide significant prostate cancer locus; note the direction conflict (GWAS effect allele C in E04 versus T risk allele in E06c) is unresolved by the evidence. | weak | [E04](#e04), [E06a](#e06a), [E06b](#e06b) |

Predictions: Allele-specific AR ChIP (or ChIP-qPCR) in androgen-stimulated prostate tumour material shows higher signal on T; signal is androgen-dependent.; Enzalutamide or AR knockdown abolishes the allelic reporter difference, while HOXB13 or GATA2 depletion does not.; Luciferase reporter with T versus C differs only in AR-positive, androgen-treated cells.

Falsified if: Allele-specific reporter or ChIP difference persists after AR depletion/androgen deprivation.; No AR occupancy at the site in any prostate AR ChIP-seq, including tumour tissue.; C allele shows stronger AR occupancy or no allelic difference.

### 2. H0: Null: no TF-mediated effect of rs339331 itself; a linked variant in the credible set carries the function (p = 0.27)

Null chain: no TF-mediated effect of this variant.

Predictions: Allele-specific reporter and base-edited isogenic lines show no difference in enhancer activity or RFX6 expression.; No allelic imbalance in ChIP-seq/ATAC-seq at chr6:116888889 in heterozygous prostate samples.; Fine-mapping PIP stays low (0.06-0.23) and another credible-set SNP carries the functional signal.

Falsified if: Base editing T>C at the endogenous locus changes RFX6 expression or enhancer activity.; Reproducible allele-specific TF occupancy is shown at chr6:116888889.; Fine-mapping resolves the credible set to this SNP.

### 3. H1: Ref T allele creates a stronger HOXB13 site in the 6q22 enhancer, raising RFX6 in prostate tumour cells (p = 0.20)

TF HOXB13 (stated coverage not_checked; registry own_model), ref allele binds more; element EH38E2496909 (dELS, chr6:116888741-116889057); gene RFX6; cell type Prostate luminal/AR-positive tumour cells (LNCaP, ACH-000977).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | HOXB13 is reported to sit in a GATA2/SMAD4/HOXB13 complex at the rs339331 enhancer, but no allele-specific HOXB13 data are in the evidence (E06c's allelic statement concerns AR, not HOXB13), and ENCODE shows no HOXB13 peak containing the variant in LNCaP (which may mean no matching experiment). Coverage not checked by QBiC-SELEX. Allele assignment to T is therefore an inference, not an observation. | weak | [E06d](#e06d), [E07](#e07) |
| element | The variant lies in a distal enhancer-like cCRE, and the literature independently calls this position the '6q22 enhancer' bound by the complex. | supported | [E03](#e03), [E06d](#e06d) |
| gene | The complex at this enhancer is reported to increase RFX6, the nearest gene and top L2G gene (0.87) in prostate cancer credible sets. | weak | [E02](#e02), [E05](#e05), [E06d](#e06d) |
| cell_type | Prostate tumour cells are the stated context for this complex; HOXB13 expression in ACH-000977 was not supplied. | weak | [E06d](#e06d) |
| phenotype | Higher RFX6 is associated with proliferation, invasion and poor prognosis and with prostate cancer risk at this locus. | weak | [E04](#e04), [E06a](#e06a), [E06b](#e06b), [E06e](#e06e) |

Predictions: HOXB13 ChIP in prostate cells shows a peak at chr6:116888889 with allelic imbalance toward T.; HOXB13 knockdown reduces RFX6 and abolishes the allelic reporter difference, while AR blockade does not.; T>C base editing lowers RFX6 without changing GPRC6A.

Falsified if: No HOXB13 occupancy at the site in any prostate HOXB13 ChIP-seq.; C allele binds HOXB13 more, or no allelic difference in HOXB13 binding.; RFX6 is unchanged by HOXB13 depletion in prostate cells.

### 4. H3: GATA2 is the allele-sensitive factor at the 6q22 enhancer, driving RFX6 through the GATA2/SMAD4/HOXB13 complex (p = 0.16)

TF GATA2 (stated coverage not_checked; registry own_model), ref allele binds more; element EH38E2496909 (dELS, chr6:116888741-116889057); gene RFX6; cell type Prostate cancer cells with TGFbeta1/SMAD4 signalling (LNCaP).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | GATA2 is named as part of the complex at the rs339331 enhancer; the evidence gives no GATA2 allele-specific binding data and does not identify GATA2 as the pioneer factor, so T-allele preference is assumed, not shown. No QBiC-SELEX lookup for GATA2 was available (not_checked). | weak | [E06d](#e06d) |
| element | The complex is placed at the rs339331/6q22 enhancer, which coincides with the dELS cCRE containing the variant. | supported | [E03](#e03), [E06d](#e06d) |
| gene | The complex is reported to increase expression of the susceptibility gene RFX6, which also has the highest L2G score. | weak | [E06d](#e06d), [E05](#e05) |
| cell_type | Prostate tumour cells with GATA2/SMAD4 activity are the described context; co-expression in LNCaP was not shown in the evidence. | weak | [E06d](#e06d) |
| phenotype | Increased RFX6 modulates prostate cancer progression, consistent with the strong GWAS association at rs339331. | weak | [E04](#e04), [E06a](#e06a), [E06b](#e06b) |

Predictions: GATA2 knockdown collapses enhancer activity and RFX6 more than HOXB13 or AR depletion.; TGFbeta1 stimulation amplifies the allelic difference via SMAD4 recruitment.; GATA2 ChIP shows allelic imbalance toward T in heterozygotes.

Falsified if: No GATA2 occupancy or motif at the variant.; GATA2 depletion leaves RFX6 and enhancer activity intact.; SMAD4/TGFbeta perturbation does not modulate the allelic effect.

### 5. H4: Same enhancer, different target: allele-dependent binding alters GPRC6A rather than RFX6 (p = 0.10)

TF AR (stated coverage not_checked; registry own_model), ref allele binds more; element EH38E2496909 dELS, SCREEN-linked to RFX6, GPRC6A and FAM162B; gene GPRC6A; cell type Prostate epithelial/tumour cells (LNCaP).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | Binding follows the only allele-specific statement available (AR, stronger on T); coverage not checked, and no LNCaP AR peak contains the site. | weak | [E06c](#e06c), [E08](#e08) |
| element | The cCRE's SCREEN gene assignment is proximity-based and lists GPRC6A and FAM162B alongside RFX6, so the target is not fixed by this evidence. | weak | [E03](#e03) |
| gene | GPRC6A is 59.8 kb away and receives modest L2G support (0.05-0.16 in the sets shown, best 0.38), far below RFX6 (0.87); no contact or eQTL evidence supports it, and prostate eQTL analysis is null for both genes. | missing | [E02](#e02), [E05](#e05), [E09](#e09) |
| cell_type | Prostate epithelial cells are the assumed context; no evidence of GPRC6A expression in prostate or LNCaP was provided. | missing | none |
| phenotype | The locus also associates with small-HDL lipid traits, which is at least compatible with a non-RFX6 effector, though no evidence ties these traits to GPRC6A. | missing | [E04](#e04) |

Predictions: CRISPRi of the enhancer in LNCaP changes GPRC6A more than RFX6.; Chromatin-contact data place the element at the GPRC6A promoter.; Any eQTL that emerges in larger prostate datasets is for GPRC6A, not RFX6.

Falsified if: Enhancer perturbation changes RFX6 only.; No physical contact between the element and the GPRC6A promoter.; GPRC6A is not expressed in prostate epithelium or LNCaP.

## Prediction matrix

| Test | Cost | Separates top two | H2 | H0 | H1 | H3 | H4 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| QBiC-SELEX detail lookup for AR, HOXB13 and GATA2 (coverage and predicted allelic effect at chr6:116888889) | existing data | yes | AR has a model (or mapped) and predicts stronger T-allele binding | No covered TF shows a meaningful predicted allelic change | HOXB13 model predicts stronger T-allele binding | GATA2 model predicts stronger T-allele binding | AR (or another covered TF) predicts a T-allele gain, target gene unresolved |
| Allele-specific luciferase reporter of the 316 bp cCRE (T vs C) in LNCaP, +/- DHT and +/- enzalutamide | low | yes | T > C activity, difference androgen-dependent and lost with enzalutamide | No allelic difference in activity | T > C activity, retained under enzalutamide | T > C activity, retained under enzalutamide, enhanced by TGFbeta1 | T > C activity (reporter cannot distinguish target gene) |
| Allelic-imbalance analysis of AR, HOXB13 and GATA2 ChIP-seq in heterozygous prostate tumours | medium | yes | AR reads skewed to T; HOXB13/GATA2 not skewed or secondary | No allelic imbalance at the site | HOXB13 reads skewed to T | GATA2 reads skewed to T | Some TF skewed to T, same as H2 at the binding step |
| Base editing T>C at the endogenous site in a heterozygous/ref prostate line, RNA-seq readout | high | yes | RFX6 falls, effect abolished by AR inhibition | No expression change at any neighbouring gene | RFX6 falls, AR-independent | RFX6 falls, TGFbeta/SMAD4-dependent | GPRC6A changes more than RFX6 |
| Enhancer CRISPRi in LNCaP with RFX6 and GPRC6A qPCR | medium | no | RFX6 down | Element may still regulate RFX6, so this test does not address the variant's allelic effect | RFX6 down | RFX6 down | GPRC6A down more than RFX6 |
| GTEx prostate eQTL lookup for rs339331 (already performed) | existing data | no | Null result is tolerated (tumour-reprogrammed AR site, not normal tissue) | Consistent: no eQTL in prostate | Null result tolerated (tumour-specific complex) | Null result tolerated | Predicted a GPRC6A eQTL; none seen, so weakened |

## Next experiment

Allele-specific luciferase reporter of the 316 bp EH38E2496909 element (T vs C) in LNCaP with and without DHT/enzalutamide: cheap, and it directly separates H2 (androgen-dependent T>C difference) from H0 (no allelic difference), while also flagging AR-independence that would favour H1/H3. If a QBiC-SELEX detail lookup for AR/HOXB13/GATA2 is available first, run it, since it is free and sets coverage.

## Investigate calls

- chip_peaks({"tf": "HOXB13", "biosample": "LNCaP"})
- chip_peaks({"tf": "AR", "biosample": "LNCaP"})
- eqtl_lookup({"tissue": "Prostate"})

## Flags

- none

Citation support: 0.95 of links cite only evidence that passed every check.

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

<a id="e07"></a>**E07** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-25T17:27:22+00:00)

> No ENCODE HOXB13 ChIP-seq peak contains chr6:116888889:T>C in biosamples matching 'LNCaP'. Absence can also mean no HOXB13 experiment in that biosample. 0 peaks lie within 100 bp without containing it.

<a id="e08"></a>**E08** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-25T17:27:23+00:00)

> No ENCODE AR ChIP-seq peak contains chr6:116888889:T>C in biosamples matching 'LNCaP'. Absence can also mean no AR experiment in that biosample. 0 peaks lie within 100 bp without containing it.

<a id="e09"></a>**E09** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr6_116888889_T_C_b38&datasetId=gtex_v8; retrieved 2026-10-25T17:27:22+00:00)

> 0 significant GTEx v8 single-tissue eQTLs for chr6_116888889_T_C_b38 in tissues matching 'Prostate'. NES is the effect of the alt allele (C) relative to ref (T).
