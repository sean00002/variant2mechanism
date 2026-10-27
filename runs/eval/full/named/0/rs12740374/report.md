# rs12740374 and LDL cholesterol, myocardial infarction (1p13)

Configuration `full`, named mode, seed 0. Models: generator claude-opus-5, critic claude-sonnet-5-5, summariser claude-haiku-5-5. Cost $0.62 over 7 model calls; 154 s.

Variant `chr1:109274968:G>T` (germline); expression context: DepMap:ACH-000625 (Hep 3B2.1-7).

## QBiC-SELEX screen

239 of 997 models pass the gate. Top groups: C2H2 ZF, 1 model (best ZNF43, z 35.83); bZIP, 1 model (best CEBPG, z 26.76); C2H2 ZF, 1 model (best ZNF696, z -24.85); RFX, 4 models (best RFX4, z 23.16); bZIP, 3 models (best CEBPB, z 22.81).

## Ranked chains

### 1. H1: Alt T allele creates a C/EBP site bound by CEBPA, raising hepatic SORT1 (and PSRC1/CELSR2) and lowering LDL/MI risk (p = 0.62)

TF CEBPA (stated coverage own_model; registry own_model), alt allele binds more; element EH38E1374646 (dELS enhancer, chr1:109274794-109275142; Ensembl regulatory ENSR1_CDSQQ); gene SORT1; cell type Hepatocyte (HepG2 ChIP evidence; Hep 3B2.1-7 expression context, DepMap ACH-000625).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The alt T allele creates a strong bZIP C/EBP-type site in vitro: QBiC-SELEX group G035 (CEBPB/CEBPA/CEBPE own models) gives z 22.81, effect +2.331, site moving from the 87.0th to the 99.8th percentile of k-mer coefficients. Within this specificity group CEBPA is chosen because (i) ENCODE ChIP-seq shows a CEBPA peak containing the variant in HepG2 (ENCSR142IGM) while no CEBPB peak is found in HepG2, and (ii) CEBPA is by far the most expressed group member in the hepatic context (141.33 TPM vs CEBPB 4.05, CEBPE 0.0). ChIP shows occupancy, not yet allele-specificity. | weak | [E12](#e12), [E19](#e19), [E18](#e18), [E07](#e07) |
| element | The variant lies in a distal enhancer-like cCRE (EH38E1374646, DNase z 4.9, H3K27ac z 4.8, maxima across biosamples) also annotated as an enhancer regulatory feature by VEP; CEBPA occupancy in HepG2 shows the element is accessible and TF-bound in a liver line. | weak | [E01](#e01), [E03](#e03), [E19](#e19) |
| gene | In liver, the alt T allele raises SORT1 expression (GTEx NES +1.27, p 3.1e-54), with concordant increases of PSRC1 (+1.24) and CELSR2 (+1.04); Open Targets gives SORT1 the top L2G score (0.99) across lipid credible sets with PIP 1.00, so SORT1 is the leading target although the eQTL does not by itself separate the three co-regulated genes. | supported | [E20](#e20), [E05](#e05) |
| cell_type | The hepatocyte is the relevant cell type: CEBPA binds the element in HepG2, is highly expressed in the hepatic line, and the eQTL signal is from liver tissue. | weak | [E19](#e19), [E12](#e12), [E20](#e20) |
| phenotype | Higher hepatic SORT1 on the T allele alters VLDL/LDL handling and lowers LDL and total cholesterol; the common G allele is the high-cholesterol/risk allele in GWAS (p ~1e-323) and the locus colocalizes with myocardial infarction. | weak | [E04](#e04), [E20](#e20), [E06b](#e06b) |

Predictions: Allele-specific CEBPA ChIP (or ChIP in heterozygous hepatocytes) shows preferential occupancy of the T allele at chr1:109274968; CEBPA knockdown in T-allele hepatocytes lowers SORT1 and flattens the allelic reporter difference, more than CEBPB knockdown; MPRA/luciferase: T > G activity in hepatic cells, lost when the C/EBP core is mutated; Base editing G>T in a G/G hepatocyte line raises SORT1 (and PSRC1/CELSR2) transcripts

Falsified if: No allele-specific CEBPA binding by EMSA/allelic ChIP at this base; CEBPA depletion leaves the allelic enhancer difference intact while another factor's depletion removes it; Isolated G>T editing does not change SORT1 or enhancer activity

### 2. H5: Null: no TF-binding-mediated effect of this variant itself (linked causal variant in the 1p13 LD block) (p = 0.21)

Null chain: no TF-mediated effect of this variant.

Predictions: Editing only chr1:109274968 G>T in hepatocytes leaves SORT1, PSRC1 and CELSR2 expression unchanged; The liver eQTL signal (E20) is driven by a tightly linked variant such as rs646776/rs12740347 (E06a); Reporter assays show no allelic difference despite the strong in vitro binding predictions and the CEBPA peak at the element

Falsified if: Isolated editing of this base changes SORT1/PSRC1/CELSR2 expression or enhancer activity; Allele-specific TF binding or allele-specific H3K27ac is demonstrated at this exact position

### 3. H2: CEBPB, not CEBPA, is the bZIP factor gained at the alt allele driving SORT1 (p = 0.08)

TF CEBPB (stated coverage own_model; registry own_model), alt allele binds more; element EH38E1374646 (dELS enhancer); gene SORT1; cell type Hepatocyte (Hep 3B2.1-7).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The best model of group G035 is CEBPB's own model (z 22.81, effect +2.331, alt binds more), and CEBPB ChIP peaks contain the variant in four non-hepatic biosamples (A549, HeLa-S3, IMR-90, MCF-7), showing the created site is a usable C/EBP site; however no CEBPB peak is found in HepG2 and CEBPB is only 4.05 TPM in the hepatic line, which weakens this chain. | weak | [E12](#e12), [E18](#e18) |
| element | The created site lies in the active distal enhancer-like cCRE EH38E1374646, occupied by C/EBP-family factors in several cell types. | weak | [E03](#e03), [E18](#e18), [E01](#e01) |
| gene | The element's output is SORT1 (best L2G 0.99), though CELSR2 (0.98) and PSRC1 (0.66) are co-scored and all three are up on the alt allele in liver. | weak | [E05](#e05), [E20](#e20) |
| cell_type | Hepatocytes under CEBPB-inducing conditions (acute-phase/inflammatory), where CEBPB protein can rise above its low basal transcript level. | missing | [E12](#e12), [E20](#e20) |
| phenotype | Changed SORT1 dose shifts LDL cholesterol and myocardial infarction risk at 1p13. | weak | [E04](#e04), [E06b](#e06b) |

Predictions: CEBPB knockdown, but not CEBPA knockdown, reduces the allelic enhancer difference in hepatic cells; CEBPB ChIP in HepG2 (once performed) gives an allele-biased peak at the variant; IL-6/acute-phase stimulation amplifies the T-allele effect on SORT1

Falsified if: CEBPA depletion alone abolishes the allelic effect; CEBPB ChIP in hepatic cells shows no peak at the element even after induction

### 4. H3: CEBPG is the gained bZIP factor at the alt allele (p = 0.06)

TF CEBPG (stated coverage own_model; registry own_model), alt allele binds more; element EH38E1374646 (dELS enhancer); gene SORT1; cell type Hepatocyte (Hep 3B2.1-7).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | CEBPG's own model gives the largest bZIP z in the screen (G143: z 26.76, effect +2.321, site 64.5th -> 99.4th percentile) and CEBPG is well expressed (46.37 TPM); z is a significance, not a strength, ranking, and no ChIP evidence for CEBPG at this site is available (the only hepatic C/EBP peak shown is CEBPA). | weak | [E09](#e09), [E19](#e19) |
| element | The created site is in the active distal enhancer-like cCRE EH38E1374646. | weak | [E03](#e03) |
| gene | SORT1 is the leading target of this element (L2G 0.99) and its liver expression rises with the alt allele (NES +1.27). | weak | [E05](#e05), [E20](#e20) |
| cell_type | Hepatocyte context, where CEBPG is abundantly expressed (46.37 TPM) and the liver eQTL is observed. | weak | [E09](#e09), [E20](#e20) |
| phenotype | Higher SORT1 lowers LDL cholesterol and MI risk at this locus. | weak | [E04](#e04), [E06b](#e06b) |

Predictions: CEBPG ChIP shows allele-specific binding at the variant while CEBPA ChIP signal is not allele-biased; CEBPG knockdown lowers SORT1 specifically in T-allele cells; CEBPG-ATF4 heterodimer motif mutations abolish the allelic difference

Falsified if: CEBPG is not bound at this element in liver chromatin; Only CEBPA depletion changes allelic activity

### 5. H4: An RFX-family factor (RFX5) gains binding at the alt allele and drives the element (p = 0.03)

TF RFX5 (stated coverage own_model; registry own_model), alt allele binds more; element EH38E1374646 (dELS enhancer); gene SORT1; cell type Hepatocyte (Hep 3B2.1-7).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | RFX-specificity models gain binding at the alt allele (G094: RFX7 z 18.73, RFX5 z 11.53, effect +0.788; G028 RFX4/RFX1 concordant). RFX5 is chosen on expression alone (41.14 TPM), the predicted effect is smaller than for the C/EBP groups, and there is no ChIP evidence for RFX at this site. | weak | [E15](#e15), [E11](#e11) |
| element | The site is in the active distal enhancer-like cCRE EH38E1374646. | weak | [E03](#e03) |
| gene | SORT1 is the leading candidate target, up on the alt allele in liver. | weak | [E05](#e05), [E20](#e20) |
| cell_type | Hepatocytes, where RFX5 is well expressed (41.14 TPM) and the eQTL is observed. | weak | [E15](#e15), [E20](#e20) |
| phenotype | SORT1 dosage change moves LDL cholesterol and MI risk. | weak | [E04](#e04) |

Predictions: RFX5 ChIP shows allele-specific occupancy at the variant; RFX5 knockdown, not C/EBP knockdown, flattens the allelic reporter difference; Mutating the X-box half-site, not the C/EBP core, removes the allelic effect

Falsified if: No RFX occupancy at this element in liver data; C/EBP core mutation abolishes the allelic difference while X-box mutation does not

## Prediction matrix

| Test | Cost | Separates top two | H1 | H5 | H2 | H3 | H4 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Allele-specific CEBPA ChIP-seq/ChIP-qPCR at chr1:109274968 in heterozygous hepatocytes (HepG2 peak already exists, E19) | low | yes | Strong T-allele bias in CEBPA reads | No allelic bias for any factor | CEBPA peak present but little or no allelic bias; bias appears for CEBPB after induction | CEBPA peak present but no allelic bias; CEBPG ChIP biased | No CEBPA allelic bias; RFX5 ChIP biased |
| CEBPB ChIP-seq in HepG2 (currently absent, E18) plus CEBPB knockdown reporter assay | medium | yes | Weak/no CEBPB peak; knockdown does not flatten allelic difference | No allelic difference to flatten | CEBPB peak with T-allele bias; knockdown flattens difference | No CEBPB dependence | No CEBPB dependence |
| Luciferase/MPRA of the 300-bp element, G vs T, in hepatic cells, with C/EBP-core and X-box point mutants | low | no | T > G; loss on C/EBP-core mutation | No allelic difference | T > G; loss on C/EBP-core mutation (same as H1) | T > G; loss on C/EBP-core mutation (same as H1) | T > G; loss on X-box mutation, retained with C/EBP-core mutation |
| CRISPR base edit G>T in a G/G hepatocyte line and measure SORT1/PSRC1/CELSR2 | high | no | SORT1 (and PSRC1/CELSR2) rise, matching GTEx NES signs | No change | Same rise | Same rise | Same rise |
| siRNA knockdown panel (CEBPA, CEBPB, CEBPG, RFX5) with SORT1 qPCR in heterozygous hepatic cells | medium | yes | CEBPA knockdown lowers SORT1 and allelic imbalance | No knockdown changes allelic imbalance | CEBPB knockdown does | CEBPG knockdown does | RFX5 knockdown does |

## Next experiment

Allele-specific CEBPA ChIP (ChIP-qPCR with allele-discriminating readout, or reanalysis of ENCSR142IGM reads if HepG2 is heterozygous) at chr1:109274968: cheapest test that distinguishes H1 (T-allele-biased CEBPA occupancy) from H2 (CEBPA bound without allelic bias, CEBPB-dependent) and from the null (no bias).

## Investigate calls

- chip_peaks({"tf": "CEBPB", "biosample": "HepG2"})
- chip_peaks({"tf": "CEBPA", "biosample": "HepG2"})
- eqtl_lookup({"tissue": "Liver"})

## Flags

- none

Citation support: 1.00 of links cite only evidence that passed every check.

## Evidence

<a id="e01"></a>**E01** variant_annotation, Ensembl VEP (GRCh38) (https://rest.ensembl.org/vep/human/region/1:109274968-109274968:1/T?content-type=application/json&Conservation=1; retrieved 2026-10-25T18:05:00+00:00)

> Variant chr1:109274968:G>T (GRCh38), allele string G/T
> Known IDs: rs12740374
> Most severe consequence: 3_prime_UTR_variant
> Regulatory features: ENSR1_CDSQQ enhancer
> GERP conservation score at the site: -0.782
> Transcript consequences: CELSR2 (3_prime_UTR_variant); PSRC1 (downstream_gene_variant); CELSR2 (downstream_gene_variant); CELSR2 (non_coding_transcript_exon_variant)

<a id="e02"></a>**E02** nearest_genes, Ensembl overlap (protein_coding) (https://rest.ensembl.org/overlap/region/human/1:108274968-110274968?feature=gene;biotype=protein_coding;content-type=application/json; retrieved 2026-10-25T18:05:25+00:00)

> 41 protein-coding genes within 1000 kb of chr1:109274968:G>T, by distance to TSS:
> PSRC1: 9.1 kb from TSS (downstream, strand -1)
> CELSR2: 25.4 kb from TSS (in gene body, strand +1)
> MYBPHL: 32.2 kb from TSS (downstream, strand -1)
> SARS1: 61.1 kb from TSS (downstream, strand +1)
> SORT1: 123.0 kb from TSS (downstream, strand -1)
> PSMA5: 151.5 kb from TSS (downstream, strand -1)
> CFAP276: 161.1 kb from TSS (upstream, strand -1)
> ELAPOR1: 161.8 kb from TSS (downstream, strand +1)
> TMEM167B: 184.6 kb from TSS (downstream, strand +1)
> SYPL2: 191.6 kb from TSS (upstream, strand +1)

<a id="e03"></a>**E03** ccre_lookup, ENCODE v4 cCRE registry (ENCFF420VPZ) and SCREEN (https://screen-beta-api.wenglab.org/dataws/cre_table; retrieved 2026-10-25T17:28:56+00:00)

> The variant lies in cCRE EH38E1374646 (dELS: distal enhancer-like), chr1:109274794-109275142.
> SCREEN: 3 cCREs within 500 bp (max z-score across ENCODE biosamples):
> EH38E1374646 dELS (contains the variant): DNase z 4.9, H3K27ac z 4.8, H3K4me3 z 4.2, CTCF z 1.9; nearby genes CELSR2, PSRC1, MYBPHL
> EH38E2829474 dELS: DNase z 3.2, H3K27ac z 4.8, H3K4me3 z 4.4, CTCF z 1.9; nearby genes CELSR2, PSRC1, MYBPHL
> EH38E2829475 dELS: DNase z 4.6, H3K27ac z 4.5, H3K4me3 z 3.7, CTCF z 1.6; nearby genes CELSR2, PSRC1, MYBPHL
> Biosample-specific z-scores are not in this call; the values above are maxima over biosamples.

<a id="e04"></a>**E04** gwas_lookup, GWAS Catalog REST v2 (https://www.ebi.ac.uk/gwas/rest/api/v2/associations?rs_id=rs12740374&size=100; retrieved 2026-10-25T17:29:12+00:00)

> 100 GWAS Catalog associations for rs12740374, strongest first:
> High cholesterol: p 9.9e-324, effect allele G, risk-allele frequency 0.7788, PMID 39024449
> Takes medication for high cholesterol?: p 6.0e-297, effect allele G, risk-allele frequency 0.7815, PMID 39024449
> Disorders of lipid metabolism (PheCode 272): p 7.0e-262, effect allele G, risk-allele frequency 0.778, PMID 39024449
> Circulating TNFSF13 levels: p 4.0e-260, effect allele ?, risk-allele frequency NR, PMID 42097137
> Hyperlipidemia (PheCode 272.1): p 6.0e-259, effect allele G, risk-allele frequency 0.778, PMID 39024449
> total cholesterol (minimum, inv-norm transformed): p 1.0e-208, effect allele G, risk-allele frequency 0.7774, PMID 39024449
> low density lipoprotein cholesterol (LDLC, maximum, inv-norm transformed): p 4.0e-164, effect allele G, risk-allele frequency 0.7453, PMID 39024449
> low density lipoprotein cholesterol (LDLC, mean, inv-norm transformed): p 4.0e-154, effect allele G, risk-allele frequency 0.7454, PMID 39024449
> Circulating LAG3 levels (id: OID05553_OID21315): p 1.0e-153, effect allele ?, risk-allele frequency NR, PMID 42097137
> Circulating LAG3 levels (id: OID01023_OID21315): p 1.0e-152, effect allele ?, risk-allele frequency NR, PMID 42097137
> LDL cholesterol levels: p 2.0e-137, effect allele T, risk-allele frequency NR, PMID 39414775
> total cholesterol (maximum, inv-norm transformed): p 2.0e-123, effect allele G, risk-allele frequency 0.7453, PMID 39024449

<a id="e05"></a>**E05** finemap_lookup, Open Targets Platform (credible sets, L2G) (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-25T17:29:04+00:00)

> 2316 credible sets contain 1_109274968_G_T: 189 GWAS, 11 molecular QTL.
> GWAS Total cholines levels (UKB data field 23436): PIP 1.00; L2G SORT1 0.99, CELSR2 0.96, PSRC1 0.20
> GWAS Apolipoprotein B levels (UKB data field 23439): PIP 1.00; L2G SORT1 0.99, CELSR2 0.96, PSRC1 0.20
> GWAS Total cholesterol levels: PIP 1.00; L2G SORT1 0.99, CELSR2 0.96, PSRC1 0.20
> GWAS Cholesterol to total lipids in large HDL percentage (UKB dat: PIP 1.00; L2G SORT1 0.99, CELSR2 0.96, PSRC1 0.20
> GWAS Total lipids in small VLDL (UKB data field 23510): PIP 1.00; L2G SORT1 0.99, CELSR2 0.96, PSRC1 0.20
> GWAS Triglycerides in medium VLDL (UKB data field 23508): PIP 1.00; L2G SORT1 0.99, CELSR2 0.96, PSRC1 0.20
> sqtl for SORT1 (gtex-v10_majiq_liver_ensg00000134243_s_109314672-1): PIP 0.72
> sqtl for CELSR2 (gtex-v10_majiq_muscle_ensg00000143126_s_109273436-): PIP 0.49
> eqtl for PSRC1 (gtex-v10_ge_pancreas_ensg00000134222): PIP 0.41
> eqtl for CELSR2 (gtex-v10_exon_esophagus_mucosa_ensg00000143126_8_1): PIP 0.37
> tuqtl for CELSR2 (gtex-v10_txrev_liver_ensg00000143126_grp_2_contain): PIP 0.32
> eqtl for PSRC1 (fairfax_2014_microarray_monocyte_naive_ilmn_231596): PIP 0.25
> Best L2G gene scores across these sets: SORT1 0.99, CELSR2 0.98, PSRC1 0.66

<a id="e06"></a>**E06** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=rs12740374%20AND%20SORT1%20AND%20%28%22ldl%20cholesterol%22%20OR%20%22myocardial%20infarction%22%29&format=json&pageSize=8&resultType=core; retrieved 2026-10-25T17:29:12+00:00)

> Europe PMC: 127 hits for 'rs12740374 AND SORT1 AND ("ldl cholesterol" OR "myocardial infarction")'; top 8 with PMIDs:
> PMID 42019808 (2026): Causal statistical association between remnant cholesterol and coronary heart disease: genetic insights into the PSRC1-CELSR2-SORT1 gene cluster.
> PMID 42820291 (2026): Clinical trials in a dish: cardiometabolic drug development with biological and digital twins.
> PMID 40922271 (2025): Effect of dietary habits on multiple cardiovascular diseases: A comprehensive Mendelian randomization study.
> PMID 41380003 (2025): Computationally efficient whole-genome quantile regression at biobank scale.
> PMID 39858645 (2025): Research Progress and Clinical Translation Potential of Coronary Atherosclerosis Diagnostic Markers from a Genomic Perspective.
> PMID 42211154 (2026): Treatment Target Discovery From Vasculo-Protective Phenotypes.
> PMID 41991941 (2026): Genetic and molecular factors underlying human longevity and epigenetic aging.
> PMID 38266112 (2024): Genome-Wide Genetic Associations Prioritize Evaluation of Causal Mechanisms of Atherosclerotic Disease Risk.

<a id="e06a"></a>**E06a** literature_search, Europe PMC abstract, PMID 42019808 (https://europepmc.org/article/MED/42019808; retrieved 2026-10-25T17:29:12+00:00)

> Colocalization identified shared signals at the PSRC1-CELSR2-SORT1 locus, with lead variants rs12740347 and rs646776.

<a id="e06b"></a>**E06b** literature_search, Europe PMC abstract, PMID 40922271 (https://europepmc.org/article/MED/40922271; retrieved 2026-10-25T17:29:12+00:00)

> The co-localization analysis, based on two-sample Mendelian randomization results, revealed that single nucleotide polymorphism (SNP) rs12740374 (PH4 = 0.855) was causally associated with MI and a balanced diet(I eat all of the above), while SNP rs7528419 (PH4 = 0.716) was causally associated with CHD and a balanced diet.

<a id="e06c"></a>**E06c** literature_search, Europe PMC abstract, PMID 39858645 (https://europepmc.org/article/MED/39858645; retrieved 2026-10-25T17:29:12+00:00)

> GWASs and sequencing studies have identified key genetic variations associated with CAD, including JCAD/KIAA1462, GUCY1A3, PCSK9, and SORT1, which regulate inflammation, lipid metabolism, and vascular function.

<a id="e07"></a>**E07** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> QBiC-SELEX screen of chr1:109274968:G>T: 997 models scored, 239 pass the gate (Bonferroni 0.05/997, p < 5.02e-05, |z| > 4.05), in 182 CIS-BP groups. Expression context: DepMap line ACH-000625. Groups shown: 10; dropped because no TF in the group reaches 1 TPM: 44 (GCM, 2 models z -44.12, Homeodomain, 3 models z -27.46, C2H2 ZF, 1 model z 21.63, Homeodomain, 2 models z -17.61, bHLH, 1 model z -14.43). Passing groups ranked below the ones shown: 128. In the group rows, 'own model' means the TF has its own QBiC-SELEX model and 'mapped' that it is covered only through CIS-BP-mapped models of related TFs. A TF not named in any group row may still have its own model, even one that passes the gate: look it up with qbic_tf_detail before stating its coverage or a QBiC-SELEX direction for it. predicted_effect > 0 means the alternate allele binds more strongly. In vitro binding only: expression and chromatin decide whether a change matters.

<a id="e08"></a>**E08** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G510 (C2H2 ZF, 1 model): best model ZNF43_FL_GC40NTATAGG_YWRA_jolma2025_0_3_7mer (own model of ZNF43), z 35.83, effect 3.431 (alt binds more); 1 passing models (1 with the best model's sign). Passing members: ZNF43 z 35.83. TFs this group covers: ZNF43 (own model) 8.74 TPM; best model's site strength: ref 93.6th, alt 99.9th percentile of its k-mer coefficients.

<a id="e09"></a>**E09** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G143 (bZIP, 1 model): best model CEBPG_eDBD_TACTTT40NTCT_KN_yin2017_0_4_7mer (own model of CEBPG), z 26.76, effect 2.321 (alt binds more); 1 passing models (1 with the best model's sign). Passing members: CEBPG z 26.76. TFs this group covers: CEBPG (own model) 46.37 TPM; best model's site strength: ref 64.5th, alt 99.4th percentile of its k-mer coefficients.

<a id="e10"></a>**E10** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G570 (C2H2 ZF, 1 model): best model ZNF696_FL_AG40NTGGCTA_YWSA_jolma2025_0_2_7mer (own model of ZNF696), z -24.85, effect -0.713 (alt binds less); 1 passing models (1 with the best model's sign). Passing members: ZNF696 z -24.85. TFs this group covers: ZNF696 (own model) 5.1 TPM; best model's site strength: ref 99.8th, alt 88.3th percentile of its k-mer coefficients.

<a id="e11"></a>**E11** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G028 (RFX, 4 models): best model RFX4_eDBD_TACTCG40NCAA_KAN_yin2017_0_3_7mer (own model of RFX4), z 23.16, effect 1.235 (alt binds more); 3 passing models (3 with the best model's sign). Passing members: RFX4 z 23.16, RFX1 z 16.27, RFX2 z 4.8. TFs this group covers: RFX2 (own model) 4.97 TPM, RFX1 (own model) 4.13 TPM, RFX3 (own model) 2.13 TPM, RFX6 (mapped) 0.35 TPM, RFX4 (own model) 0.0 TPM; best model's site strength: ref 95.8th, alt 99.0th percentile of its k-mer coefficients.

<a id="e12"></a>**E12** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G035 (bZIP, 3 models): best model CEBPB_eDBD_TATAAA40NACG_KAN_yin2017_0_4_7mer (own model of CEBPB), z 22.81, effect 2.331 (alt binds more); 3 passing models (3 with the best model's sign). Passing members: CEBPB z 22.81, CEBPA z 22.63, CEBPE z 11.28. TFs this group covers: CEBPA (own model) 141.33 TPM, CEBPB (own model) 4.05 TPM, CEBPE (own model) 0.0 TPM; best model's site strength: ref 87.0th, alt 99.8th percentile of its k-mer coefficients.

<a id="e13"></a>**E13** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G030 (AP-2, 4 models): best model TFAP2E_FL_TCAAAC40NAAC_KW_yin2017_1_3_7mer (own model of TFAP2E), z -21.21, effect -0.98 (alt binds less); 4 passing models (4 with the best model's sign). Passing members: TFAP2E z -21.21, TFAP2B z -18.18, TFAP2A z -13.22, TFAP2C z -12.55. TFs this group covers: TFAP2A (own model) 7.65 TPM, TFAP2E (own model) 2.06 TPM, TFAP2B (own model) 0.04 TPM, TFAP2C (own model) 0.01 TPM, TFAP2D (mapped) 0.0 TPM; best model's site strength: ref 99.8th, alt 98.8th percentile of its k-mer coefficients.

<a id="e14"></a>**E14** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G491 (C2H2 ZF, 1 model): best model ZNF345_eDBD_TGTAAG40NACT_KT_yin2017_0_3_7mer (own model of ZNF345), z 20.62, effect 0.964 (alt binds more); 1 passing models (1 with the best model's sign). Passing members: ZNF345 z 20.62. TFs this group covers: ZNF345 (own model) 1.64 TPM; best model's site strength: ref 97.7th, alt 99.9th percentile of its k-mer coefficients.

<a id="e15"></a>**E15** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G094 (RFX, 2 models): best model RFX7_eDBD_TCGTCC40NGCC_KT_yin2017_0_4_7mer (own model of RFX7), z 18.73, effect 0.788 (alt binds more); 2 passing models (2 with the best model's sign). Passing members: RFX7 z 18.73, RFX5 z 11.53. TFs this group covers: RFX5 (own model) 41.14 TPM, RFX7 (own model) 9.96 TPM; best model's site strength: ref 84.8th, alt 99.0th percentile of its k-mer coefficients.

<a id="e16"></a>**E16** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G142 (bZIP, 1 model): best model CEBPD_NA_TAATGA20NCG_ESY_yang2017_0_2_7mer (own model of CEBPD), z 18.08, effect 1.253 (alt binds more); 1 passing models (1 with the best model's sign). Passing members: CEBPD z 18.08. TFs this group covers: CEBPD (own model) 5.4 TPM; best model's site strength: ref 88.1th, alt 99.1th percentile of its k-mer coefficients.

<a id="e17"></a>**E17** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G012 (bZIP, 6 models): best model MAFG_eDBD_TTGTTC40NAAG_KN_yin2017_0_3_7mer (own model of MAFG), z 16.34, effect 0.625 (alt binds more); 5 passing models (5 with the best model's sign). Passing members: MAFG z 16.34, MAF z 11.17, MAFK z 10.91, NRL z 10.31, MAFA z 9.36. TFs this group covers: MAFK (own model) 39.41 TPM, MAFG (own model) 19.11 TPM, NRL (own model) 0.83 TPM, MAF (own model) 0.52 TPM, MAFB (own model) 0.47 TPM, MAFA (own model) 0.04 TPM; best model's site strength: ref 94.7th, alt 97.4th percentile of its k-mer coefficients.

<a id="e18"></a>**E18** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-25T22:29:03+00:00)

> No ENCODE CEBPB ChIP-seq peak contains chr1:109274968:G>T in biosamples matching 'HepG2'. Absence can also mean no CEBPB experiment in that biosample. In other biosamples, 4 CEBPB peaks do contain the variant: A549, HeLa-S3, IMR-90, MCF-7 (experiments ENCSR000BSR, ENCSR000EDA, ENCSR000EFM, ENCSR752AQK).

<a id="e19"></a>**E19** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-25T17:30:36+00:00)

> 1 ENCODE CEBPA ChIP-seq peaks contain chr1:109274968:G>T in biosamples matching 'HepG2': biosamples HepG2; experiments ENCSR142IGM.

<a id="e20"></a>**E20** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr1_109274968_G_T_b38&datasetId=gtex_v8; retrieved 2026-10-25T17:30:36+00:00)

> 5 significant GTEx v8 single-tissue eQTLs for chr1_109274968_G_T_b38 in tissues matching 'Liver'. NES is the effect of the alt allele (T) relative to ref (G).
> SORT1 in Liver: NES +1.27, p 3.1e-54
> PSRC1 in Liver: NES +1.24, p 1.1e-37
> CELSR2 in Liver: NES +1.04, p 9.4e-34
> ATXN7L2 in Liver: NES +0.40, p 5.9e-07
> SYPL2 in Liver: NES +0.50, p 1.2e-06
