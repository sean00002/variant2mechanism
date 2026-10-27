# rs12740374 and LDL cholesterol, myocardial infarction (1p13)

Configuration `no_qbic`, named mode, seed 0. Models: generator claude-opus-5, critic claude-sonnet-5-5, summariser claude-haiku-5-5. Cost $0.59 over 8 model calls; 179 s.

Variant `chr1:109274968:G>T` (germline); expression context: DepMap:ACH-000625 (Hep 3B2.1-7).

## Ranked chains

### 1. H1: Alt T creates a C/EBP site bound by CEBPA in the liver enhancer, raising SORT1 and lowering LDL (p = 0.47)

TF CEBPA (stated coverage not_checked; registry own_model), alt allele binds more; element ENCODE cCRE EH38E1374646 (dELS, chr1:109274794-109275142), overlapping the CELSR2 3'UTR / ENSR1_CDSQQ enhancer; gene SORT1; cell type hepatocyte (Hep 3B2.1-7, DepMap ACH-000625).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The alt T allele is proposed to create a C/EBP-family recognition sequence bound more strongly than ref G. No QBiC-SELEX row, motif scan or liver ChIP peak was returned for this site, so this link remains unsupported by the evidence in hand: E09 explicitly finds no CEBPB peak at the variant in HepG2 (though absence may reflect a missing experiment), while CEBPB peaks in A549, HeLa-S3, IMR-90 and MCF-7 show only that the sequence is C/EBP-accessible in some cells. Within the C/EBP specificity group I name CEBPA rather than CEBPB because the liver effect is hepatocyte-restricted (E08) and CEBPA is the C/EBP member associated with the hepatocyte programme; this choice rests on background knowledge, not on cited expression or ChIP data. CEBPA coverage was never looked up, hence not_checked. | missing | [E09](#e09) |
| element | The variant lies inside a distal enhancer-like cCRE (EH38E1374646) with high DNase/H3K27ac z-scores; these are maxima across biosamples, so activity in liver or Hep3B is not shown by this evidence. | weak | [E01](#e01), [E03](#e03) |
| gene | In liver the alt T allele is associated with higher SORT1 expression (NES +1.27, p 3.1e-54), the largest liver eQTL effect of the variant, and SORT1 is the top L2G gene (0.99) for the lipid GWAS; the eQTL is association, not a demonstrated enhancer-promoter link. | weak | [E08](#e08), [E05](#e05) |
| cell_type | The effect is seen in liver tissue eQTLs and the expression context is a hepatoma line; literature attributes liver-specific modulation of SORT1 to this variant. | supported | [E08](#e08), [E07a](#e07a) |
| phenotype | The minor (T) allele sequence enhances SORT1 expression in hepatocytes, and G is the risk allele for high cholesterol/LDL in GWAS, consistent with higher hepatic SORT1 lowering LDL-C and MI risk; the SORT1-to-LDL direction itself is taken from literature statements, not measured here. | weak | [E07b](#e07b), [E07c](#e07c), [E04](#e04) |

Predictions: CEBPA ChIP-seq in HepG2/primary hepatocytes shows a peak at chr1:109274968 with allele-specific reads favouring T; CEBPA knockdown in Hep3B abolishes the allelic difference in SORT1 expression while CEBPB knockdown does not; Reporter/MPRA: T allele drives higher activity in hepatocyte lines but not in non-hepatic lines; QBiC-SELEX lookup of CEBPA returns an own model with a positive alt-preferring score at this site

Falsified if: No C/EBP occupancy or allele preference at this position in hepatocytes; CEBPA depletion leaves the allelic SORT1 effect intact; Single-base editing of G>T does not change SORT1 expression in hepatocytes

### 2. H5: Null: no TF-mediated effect of this base; signal carried by a linked variant (p = 0.18)

Null chain: no TF-mediated effect of this variant.

Predictions: Isogenic single-base editing of chr1:109274968 changes neither enhancer activity nor SORT1/CELSR2/PSRC1 expression; Denser fine-mapping shifts the causal credible set to a neighbouring variant in EH38E2829474/EH38E2829475; No allele-specific TF footprint at this position in liver DNase/ATAC footprint data; Liver eQTL signal is explained by an LD proxy (e.g. rs646776) when conditioned on

Falsified if: Single-base editing reproduces the SORT1 expression difference; A TF shows reproducible allele-specific binding at this exact position; MPRA shows allelic activity for this base in hepatocytes

### 3. H2: Same created C/EBP site, but CEBPB is the operative family member (p = 0.17)

TF CEBPB (stated coverage not_checked; registry own_model), alt allele binds more; element cCRE EH38E1374646 (dELS) in the CELSR2 3'UTR region; gene SORT1; cell type hepatocyte (Hep 3B2.1-7).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The alt T allele is proposed to create a C/EBP-class motif occupied by CEBPB. The only direct data are Factorbook peaks: CEBPB peaks containing the variant exist in A549, HeLa-S3, IMR-90 and MCF-7, showing the sequence can be CEBPB-bound, but no CEBPB peak was found in HepG2 (possibly because no such experiment exists in that biosample). CEBPB is chosen over CEBPA only because it is the one C/EBP member with observed occupancy at this exact position; coverage not looked up. | weak | [E09](#e09) |
| element | The variant lies in the same enhancer-like cCRE with strong (cross-biosample maximum) DNase and H3K27ac signal. | weak | [E03](#e03) |
| gene | Liver eQTL links the alt allele to higher SORT1 (NES +1.27), the top L2G gene at the locus. | weak | [E08](#e08), [E05](#e05) |
| cell_type | Liver/hepatocyte context from the liver eQTL and the hepatoma expression context; CEBPB abundance in Hep3B was not measured. | weak | [E08](#e08), [E07a](#e07a) |
| phenotype | Higher hepatic SORT1 from the T allele lowers LDL-C, with G the GWAS risk allele for high cholesterol. | weak | [E07b](#e07b), [E04](#e04) |

Predictions: CEBPB ChIP in hepatocytes (once performed) shows an allele-specific peak while CEBPA ChIP does not; Allelic enhancer activity is sensitive to CEBPB but not CEBPA knockdown; Inflammatory stimulation that induces CEBPB amplifies the allelic difference; CEBPB expression in Hep3B exceeds CEBPA

Falsified if: CEBPB is not bound at this element in hepatocytes even when assayed; CEBPB knockdown does not change allelic SORT1 expression; CEBPA ChIP shows the allele-specific peak instead

### 4. H3: Created C/EBP site acts on the proximal genes CELSR2/PSRC1 rather than SORT1 (p = 0.12)

TF CEBPA (stated coverage not_checked; registry own_model), alt allele binds more; element cCRE EH38E1374646, within the CELSR2 3'UTR and 9.1 kb from the PSRC1 TSS; gene CELSR2; cell type hepatocyte (Hep 3B2.1-7).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | Same proposed C/EBP site created by the alt T allele, with CEBPA named as the liver-associated family member; no motif or liver ChIP evidence supports this, and the only C/EBP occupancy data are non-hepatic CEBPB peaks. | missing | [E09](#e09) |
| element | The variant is a CELSR2 3'UTR variant, sits 9.1 kb from the PSRC1 TSS, and SCREEN lists CELSR2, PSRC1 and MYBPHL as the nearby genes of this cCRE. | weak | [E01](#e01), [E02](#e02), [E03](#e03) |
| gene | The alt allele also raises PSRC1 (NES +1.24) and CELSR2 (NES +1.04) in liver, with CELSR2 L2G 0.98 and PSRC1 0.66, so the proximal genes are co-regulated and could be the effectors rather than SORT1. | weak | [E08](#e08), [E05](#e05) |
| cell_type | The co-regulation is observed in liver tissue; other QTLs for these genes are in muscle, pancreas and esophagus, so hepatocyte specificity is only partly shown. | weak | [E08](#e08), [E05](#e05) |
| phenotype | Altered CELSR2/PSRC1 levels would change hepatic lipoprotein handling and LDL-C, with G the GWAS risk allele; no cited evidence shows a CELSR2 or PSRC1 effect on lipids. | missing | [E04](#e04) |

Predictions: Knockdown of CELSR2 or PSRC1, but not SORT1, reproduces the apoB/LDL phenotype in hepatocytes; Allele-specific 3C/HiC contacts from the element go to CELSR2/PSRC1 promoters rather than the SORT1 promoter; Editing the base changes CELSR2 or PSRC1 with only secondary change in SORT1

Falsified if: SORT1 knockdown alone reproduces the lipid phenotype and CELSR2/PSRC1 knockdown does not; Enhancer deletion changes SORT1 without changing CELSR2/PSRC1

### 5. H4: Ref G is bound by a liver nuclear receptor (HNF4A) whose loss on T de-represses the element (p = 0.06)

TF HNF4A (stated coverage not_checked; registry own_model), ref allele binds more; element cCRE EH38E1374646 (dELS); gene SORT1; cell type hepatocyte (Hep 3B2.1-7).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | Alternative reading: the ref G allele supports stronger binding of a liver nuclear receptor such as HNF4A acting as a repressor at this element. No motif, SELEX, ChIP or expression evidence for HNF4A at this site was returned; the only occupancy data concern CEBPB in non-liver cells. Coverage not looked up. | missing | [E09](#e09) |
| element | The variant lies in an enhancer-like cCRE (max-over-biosample marks). | weak | [E03](#e03) |
| gene | Liver eQTL shows the alt allele raises SORT1, which is equally compatible with loss of a repressor on T. | weak | [E08](#e08) |
| cell_type | Liver, where the eQTL effect is observed. | weak | [E08](#e08) |
| phenotype | De-repression on T raises SORT1 and lowers LDL-C and MI risk; direction identical to H1/H2, so phenotype cannot discriminate. | weak | [E04](#e04), [E07b](#e07b) |

Predictions: Footprint/ChIP shows stronger HNF4A or nuclear-receptor occupancy on the G allele; HNF4A knockdown raises SORT1 specifically from the G-allele haplotype; No C/EBP occupancy detected at either allele in hepatocytes

Falsified if: A C/EBP factor, not a nuclear receptor, shows allele-specific binding; HNF4A is not bound at this element in liver ChIP data; HNF4A depletion does not alter allelic SORT1 expression

## Prediction matrix

| Test | Cost | Separates top two | H1 | H5 | H2 | H3 | H4 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Factorbook/ENCODE lookup of CEBPA ChIP-seq peaks at chr1:109274968 in HepG2 or liver (existing data) | existing data | yes | CEBPA peak present at the site in hepatic cells | No peak, or a peak with no allelic imbalance | No CEBPA peak; CEBPB peaks only (as in non-liver cells) | CEBPA peak present (same binding claim as H1) | No C/EBP peak at either allele |
| QBiC-SELEX detail lookup for CEBPA, CEBPB and HNF4A at this site (coverage plus predicted allelic effect) | existing data | yes | CEBPA model (own or mapped) predicts stronger binding to T | No TF model shows a meaningful allelic difference | CEBPB model predicts stronger binding to T; CEBPA weaker or not covered | Same C/EBP alt-preferring prediction as H1 | HNF4A model predicts stronger binding to G |
| RNA-seq/DepMap expression of CEBPA, CEBPB, HNF4A in Hep 3B2.1-7 (ACH-000625) | existing data | yes | CEBPA expressed at levels comparable to or above CEBPB | Uninformative; no prediction | CEBPB clearly dominant over CEBPA | CEBPA expressed (same as H1) | HNF4A highly expressed |
| siRNA knockdown of CEBPA vs CEBPB in Hep3B, measure SORT1 and allele-specific enhancer reporter activity | medium | yes | CEBPA knockdown reduces T-allele reporter activity and SORT1 | No allelic reporter difference to modulate | CEBPB knockdown, not CEBPA, reduces T-allele activity | CEBPA knockdown lowers CELSR2/PSRC1 more than SORT1 | Neither C/EBP knockdown matters; HNF4A knockdown raises SORT1 |
| CRISPR single-base edit G>T in a hepatocyte line, then RNA-seq of SORT1, CELSR2, PSRC1 | high | no | SORT1 up (largest effect), matching liver eQTL NES +1.27 | No expression change at any of the three genes | SORT1 up (same as H1) | CELSR2/PSRC1 up with little or no SORT1 change | SORT1 up (de-repression; same direction) |
| Allele-specific ATAC/DNase footprint QTL analysis at this position in heterozygous human livers | existing data | no | Footprint with C/EBP-shaped protection stronger on T | No allele-specific footprint at this base | Same C/EBP footprint stronger on T | Same footprint; gene assignment unchanged | Footprint stronger on G |

## Next experiment

Query existing ENCODE/Factorbook ChIP-seq for CEBPA (and re-query CEBPB) peaks overlapping chr1:109274968 in HepG2 and liver, together with a QBiC-SELEX detail lookup for CEBPA and CEBPB at this site and their expression in Hep 3B2.1-7. All are existing-data lookups and they directly separate H1 (CEBPA) from H2 (CEBPB) while also testing whether any C/EBP binding occurs at all.

## Investigate calls

- literature_search({"query": "rs12740374 C/EBP binding site SORT1 minor allele"})
- eqtl_lookup({"tissue": "Liver"})
- chip_peaks({"tf": "CEBPB", "biosample": "HepG2"})

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

<a id="e07"></a>**E07** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=rs12740374%20C/EBP%20binding%20site%20SORT1%20minor%20allele&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T00:18:20+00:00)

> Europe PMC: 37 hits for 'rs12740374 C/EBP binding site SORT1 minor allele'; top 8 with PMIDs:
> PMID 41380003 (2025): Computationally efficient whole-genome quantile regression at biobank scale.
> PMID 40250421 (2025): Characterization of non-coding variants associated with transcription-factor binding through ATAC-seq-defined footprint QTLs in liver.
> PMID 41991941 (2026): Genetic and molecular factors underlying human longevity and epigenetic aging.
> PMID 41650936 (2026): Expanded chromatin accessibility mapping explains genetic variation associated with complex traits in liver.
> PMID 37582372 (2023): Prioritization of therapeutic targets for dyslipidemia using integrative multi-omics and multi-trait analysis.
> PMID 35724703 (2022): Sorting through the extensive and confusing roles of sortilin in metabolic disease.
> PMID 34784266 (2022): Emerging roles of sortilin in affecting the metabolism of glucose and lipid profiles.
> PMID 29097363 (2018): Interrogation of the Atherosclerosis-Associated <i>SORT1</i> (Sortilin 1) Locus With Primary Human Hepatocytes, Induced Pluripotent Stem Cell-Hepatocytes, and Locus-Humanized Mice.

<a id="e07a"></a>**E07a** literature_search, Europe PMC abstract, PMID 29097363 (https://europepmc.org/article/MED/29097363; retrieved 2026-10-26T00:18:20+00:00)

> The noncoding single-nucleotide polymorphism rs12740374 has been hypothesized to be the causal variant responsible for liver-specific modulation of SORT1(sortilin 1) expression (ie, expression quantitative trait locus) and, by extension, the association of the SORT1 locus on human chromosome 1p13 with low-density lipoprotein cholesterol levels and coronary heart disease.

<a id="e07b"></a>**E07b** literature_search, Europe PMC abstract, PMID 29097363 (https://europepmc.org/article/MED/29097363; retrieved 2026-10-26T00:18:20+00:00)

> The rs12740374 minor allele sequence enhances SORT1 expression in hepatocytes.

<a id="e07c"></a>**E07c** literature_search, Europe PMC abstract, PMID 35724703 (https://europepmc.org/article/MED/35724703; retrieved 2026-10-26T00:18:20+00:00)

> The 1p13.3 locus containing SORT1, the gene encoding sortilin, carries the strongest association with LDL-C of all loci in human genome-wide association studies.

<a id="e08"></a>**E08** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr1_109274968_G_T_b38&datasetId=gtex_v8; retrieved 2026-10-25T17:30:36+00:00)

> 5 significant GTEx v8 single-tissue eQTLs for chr1_109274968_G_T_b38 in tissues matching 'Liver'. NES is the effect of the alt allele (T) relative to ref (G).
> SORT1 in Liver: NES +1.27, p 3.1e-54
> PSRC1 in Liver: NES +1.24, p 1.1e-37
> CELSR2 in Liver: NES +1.04, p 9.4e-34
> ATXN7L2 in Liver: NES +0.40, p 5.9e-07
> SYPL2 in Liver: NES +0.50, p 1.2e-06

<a id="e09"></a>**E09** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-25T22:29:03+00:00)

> No ENCODE CEBPB ChIP-seq peak contains chr1:109274968:G>T in biosamples matching 'HepG2'. Absence can also mean no CEBPB experiment in that biosample. In other biosamples, 4 CEBPB peaks do contain the variant: A549, HeLa-S3, IMR-90, MCF-7 (experiments ENCSR000BSR, ENCSR000EDA, ENCSR000EFM, ENCSR752AQK).
