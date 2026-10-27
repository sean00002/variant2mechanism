# rs6983267 and Colorectal cancer (8q24)

Configuration `full`, named mode, seed 0. Models: generator claude-opus-5, critic claude-sonnet-5-5, summariser claude-haiku-5-5. Cost $0.71 over 7 model calls; 270 s.

Variant `chr8:127401060:G>T` (germline); expression context: DepMap:ACH-000971 (HCT 116).

## QBiC-SELEX screen

421 of 997 models pass the gate. Top groups: Nuclear receptor, 1 model (best NR2E1, z 53.69); C2H2 ZF, 1 model (best ZNF493, z -34.16); C2H2 ZF, 2 models (best GFI1B, z -31.27); T-box, 2 models (best TBX19, z 26.18); C2H2 ZF, 1 model (best ZBTB43, z -23.26).

## Ranked chains

### 1. H1: Ref G allele preserves a TCF/LEF site bound by TCF7L2 in the 8q24 enhancer, supporting long-range Wnt-driven MYC activation (p = 0.35)

TF TCF7L2 (stated coverage mapped; registry mapped), ref allele binds more; element ENCODE cCRE EH38E3858447 (pELS) / Ensembl enhancer ENSR8_CGMBX, chr8:127401053-127401303; gene MYC; cell type Colorectal adenocarcinoma cells (HCT 116, ACH-000971).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | TCF7L2 is covered only through CIS-BP-mapped models of related HMG/Sox family members (LEF1, TCF7, TCF7L1, group G041). Two of these pass the gate with negative effects (LEF1 z -4.66, effect -0.47; TCF7 z -4.59, effect -0.229), i.e. the alt T allele binds less and the ref G allele binds more. I chose TCF7L2 within this shared TCF/LEF specificity because it is the family member with a ChIP-seq peak covering this exact position in HCT116 (ENCSR000EUV). Caveat: the effect sizes are small, the models rank only ~350/997 by /z/, and the per-model site-strength percentiles are not internally consistent (TCF7 model ref 96.9th vs alt 99.2th). | weak | [E18](#e18), [E19](#e19) |
| element | The variant lies in an accessible, H3K27ac-marked proximal enhancer-like cCRE (DNase z 5.2, H3K27ac z 4.8, maxima across biosamples, not HCT116-specific) that is also annotated as an Ensembl enhancer. | weak | [E03](#e03), [E01](#e01) |
| gene | MYC is the nearest cancer-relevant protein-coding gene (334 kb upstream of the element). Cited evidence for this specific link is weak: Open Targets gives MYC only L2G 0.05 against POU5F1B 0.89, and no eQTL, Hi-C or CRISPR evidence for an element-MYC connection is in the record; a PVT1 single-cell eQTL in colon goblet cells (PIP 0.95) is the only MYC-region molecular QTL cited. | missing | [E02](#e02), [E05](#e05) |
| cell_type | TCF7L2 occupies this position in HCT116, a colorectal line, by ENCODE ChIP-seq, so the relevant TF is present and bound in colorectal cells. | weak | [E19](#e19) |
| phenotype | rs6983267 is among the strongest CRC signals (p 2e-122; several entries list G as the effect allele for colorectal cancer/advanced adenoma, colon polyps and benign colon neoplasm, while the top 2022 entry lists T). If G is the risk allele, more TCF7L2 binding on G raising MYC output fits; the inconsistent effect-allele reporting in the catalog is unresolved and weakens this link. | weak | [E04](#e04), [E06a](#e06a) |

Predictions: Allele-specific read counts in the existing HCT116 TCF7L2 ChIP (ENCSR000EUV) show excess G-allele reads at chr8:127401060.; 4C/Capture-C from this element contacts the MYC promoter, and prime-edited G>T clones lower MYC mRNA without changing POU5F1B.; Wnt stimulation amplifies the G>T reporter difference.

Falsified if: Allele-specific TCF7L2 ChIP or EMSA shows no G preference or a T preference.; Single-base allele swap changes POU5F1B/CCAT2 but leaves MYC unchanged.

### 2. H0: Null: no TF-binding-mediated effect of this base itself (linked causal variant in the adjacent cCREs, or no allelic effect) (p = 0.30)

Null chain: no TF-mediated effect of this variant.

Predictions: Prime-edited single-base G>T clones change neither MYC, POU5F1B, CCAT2 nor proliferation.; Allele-specific read counts in existing HCT116 ChIP data show balanced alleles at chr8:127401060.; Fine-mapping in further ancestries moves the signal to EH38E3858446/EH38E3858448; the GTEx POU5F1B signal is driven by a linked variant.

Falsified if: A single-base allelic replacement reproducibly changes enhancer activity or target-gene expression.; Any TF shows reproducible allele-specific occupancy at this position in colonic cells.

### 3. H5: Same TCF7L2 site, but the gene it controls is POU5F1B/CCAT2, not MYC: loss of TCF7L2 binding on the T allele raises POU5F1B in colon (p = 0.22)

TF TCF7L2 (stated coverage mapped; registry mapped), ref allele binds more; element cCRE EH38E3858447 (pELS), overlapping the CCAT2 exon / CASC8 intron; gene POU5F1B (and overlapping CCAT2); cell type Colon / colorectal adenocarcinoma cells (Colon_Transverse tissue; HCT 116).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | Identical binding evidence to H1: CIS-BP-mapped TCF/LEF models give a ref-preferring change (LEF1 effect -0.47, z -4.66; TCF7 effect -0.229, z -4.59), and TCF7L2 itself is chosen within this specificity group because an ENCODE TCF7L2 ChIP peak in HCT116 contains the variant. | weak | [E18](#e18), [E19](#e19) |
| element | The variant is an exonic base of CCAT2 inside an active proximal enhancer-like cCRE whose SCREEN-linked genes are CCAT2, PCAT1 and POU5F1B. | weak | [E01](#e01), [E03](#e03) |
| gene | The alt T allele is associated with higher POU5F1B expression in Colon_Transverse (GTEx NES +0.20, p 8.2e-06) and with lower CASC8 in whole blood (NES -0.32); Open Targets L2G favours POU5F1B (0.89), and TWAS implicates POU5F1B at this locus. Direction is consistent with ref-G TCF7L2 binding acting repressively or with TCF7L2 loss permitting local transcription, but the repressive role itself is not demonstrated by any cited experiment. | weak | [E20](#e20), [E05](#e05), [E06b](#e06b) |
| cell_type | The eQTL is measured in transverse colon, and TCF7L2 is bound at this position in the colorectal line HCT116, so TF and target respond in the same tissue. | weak | [E20](#e20), [E19](#e19) |
| phenotype | POU5F1B promotes colorectal cancer cell proliferation and metastasis, so a T-allele increase in POU5F1B fits the top CRC association entry, in which T is the effect allele (p 2e-122); entries listing G as effect allele for related colon traits are not reconciled. | weak | [E06c](#e06c), [E04](#e04) |

Predictions: Prime-edited G>T clones in a colorectal line raise POU5F1B/CCAT2 with little or no change in MYC.; TCF7L2 knockdown raises POU5F1B in G/G but not T/T backgrounds.; Genotype-stratified colon RNA shows POU5F1B, not MYC, tracking the variant.

Falsified if: Allele swap changes MYC but not POU5F1B/CCAT2.; TCF7L2 depletion lowers rather than raises POU5F1B, i.e. the site acts as an activator of POU5F1B.

### 4. H4: Ref G allele supports ZBTB43 binding; loss on the T allele de-represses the local CCAT2/POU5F1B unit (p = 0.07)

TF ZBTB43 (stated coverage own_model; registry own_model), ref allele binds more; element cCRE EH38E3858447, overlapping the CCAT2 exon / CASC8 intron; gene POU5F1B (and overlapping CCAT2); cell type Colorectal adenocarcinoma cells (HCT 116, ACH-000971).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | QBiC has an own model for ZBTB43 (group G404, single member) with a ref-preferring effect (z -23.26, effect -1.724; ref 99.8th to alt 87.9th percentile), and ZBTB43 is expressed at 8.32 TPM in HCT 116. This is an in vitro prediction only; other expressed ref-preferring hits exist (e.g. MBNL2 at 26.09 TPM, an RNA-binding CCCH protein), so ZBTB43 is not uniquely indicated. | weak | [E12](#e12), [E13](#e13), [E07](#e07) |
| element | The variant is an exonic base of CCAT2 inside an active proximal enhancer-like cCRE; no cited evidence shows ZBTB43 occupancy or a repressive role there. | weak | [E01](#e01), [E03](#e03) |
| gene | POU5F1B carries the highest L2G score at this locus (0.89), has TWAS support, and shows a colon eQTL in which the T allele raises expression (NES +0.20), the direction expected if a ref-bound repressor is lost. | weak | [E05](#e05), [E06b](#e06b), [E20](#e20) |
| cell_type | ZBTB43 is expressed in HCT 116 (8.32 TPM) and POU5F1B is functional in colorectal cancer cells; no ChIP evidence places ZBTB43 at this element. | weak | [E12](#e12), [E06c](#e06c) |
| phenotype | Higher POU5F1B promotes colorectal proliferation and metastasis, consistent with the T-allele CRC association in the top catalog entry; other entries list G as effect allele and are not reconciled. | weak | [E06c](#e06c), [E04](#e04) |

Predictions: ZBTB43 ChIP or EMSA shows G-preferential occupancy at chr8:127401060.; ZBTB43 depletion raises POU5F1B/CCAT2 only in G-allele-containing cells.; TCF7L2 depletion leaves the allelic effect intact.

Falsified if: ZBTB43 shows no binding at this sequence in cells.; Allelic effect persists after ZBTB43 knockout.

### 5. H3: Alt T allele strengthens a COUP-TF/ESRR-type nuclear-receptor site (group G002) read by an abundant family member such as NR2F2 (p = 0.06)

TF NR2F2 (stated coverage mapped; registry own_model), alt allele binds more; element cCRE EH38E3858447 (pELS); gene POU5F1B; cell type Colorectal adenocarcinoma cells (HCT 116, ACH-000971).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | QBiC group G002 (nuclear receptor, 29 models) has an alt-preferring best model (NR2F6, own model, z 20.82, effect 1.92; ref 98.6th to alt 100.0th percentile), but passing members disagree in direction (NR2C2 z -6.01). NR2F2 is only a CIS-BP-mapped member of this shared specificity and is not itself a named passing member; it is chosen only because it is the most abundant covered member in HCT 116 (61.74 TPM), which is a weak basis. NR2F6 (37.02 TPM) is an equally plausible reader. | weak | [E14](#e14), [E07](#e07) |
| element | The site is in an accessible, H3K27ac-marked proximal enhancer-like cCRE (values are maxima over biosamples, not HCT116-specific). | weak | [E03](#e03) |
| gene | The element's linked genes are CCAT2/PCAT1/POU5F1B, and the only colon eQTL for this variant is POU5F1B (alt T raises it), so POU5F1B is the target if the alt-preferring nuclear-receptor site acts as an activator. | weak | [E03](#e03), [E05](#e05), [E20](#e20) |
| cell_type | NR2F2 and related receptors are highly expressed in this colorectal line, making occupancy possible; occupancy itself is not shown. | weak | [E14](#e14) |
| phenotype | Higher POU5F1B promotes CRC cell growth and metastasis, matching a T-risk-allele reading of the association. | weak | [E06c](#e06c), [E04](#e04) |

Predictions: NR2F2 (or NR2F6) ChIP shows T-biased occupancy at the variant; knockdown reduces POU5F1B in T-allele cells.; Mutating the nuclear-receptor half-site, but not the TCF/LEF core, abolishes the allelic reporter difference.

Falsified if: No NR2F2/NR2F6 signal at this cCRE in colorectal cells.; Allelic reporter difference persists after disrupting the predicted NR half-site.

## Prediction matrix

| Test | Cost | Separates top two | H1 | H0 | H5 | H4 | H3 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Allele-specific read counts at chr8:127401060 in existing ENCODE HCT116 TCF7L2 ChIP-seq (ENCSR000EUV), given HCT116 heterozygosity | existing data | yes | Excess G-allele reads (ref-biased occupancy) | Balanced allelic reads | Excess G-allele reads (same binding claim) | No TCF7L2 allelic bias required; bias, if any, incidental | No TCF7L2 allelic bias; if anything T-biased NR occupancy |
| Prime-edit G>T (and T>G) single-base clones in a colorectal line; RT-qPCR of MYC, POU5F1B, CCAT2, PVT1 | high | yes | MYC falls with T; POU5F1B largely unchanged | No gene changes | POU5F1B/CCAT2 rise with T; MYC little changed | POU5F1B/CCAT2 rise with T | POU5F1B rises with T |
| Genotype-stratified eQTL re-analysis in colon (GTEx v8 and larger colon cohorts) for MYC vs POU5F1B vs CCAT2 | existing data | yes | Expect MYC signal; currently absent, which counts against H1 | Signal attributable to a linked variant; conditional analysis removes it | POU5F1B positive NES for T, as observed (E20) | POU5F1B positive NES for T | POU5F1B positive NES for T |
| TCF7L2 siRNA knockdown in HCT116 followed by MYC/POU5F1B/CCAT2 measurement and reporter assay with both alleles | medium | yes | MYC drops; G-allele reporter loses its advantage | No allelic difference to begin with | POU5F1B/CCAT2 rise; allelic reporter difference collapses | No change in allelic difference | No change in allelic difference |
| ZBTB43 and NR2F2/NR2F6 ChIP-seq (or CUT&RUN) in HCT116 at this cCRE | medium | no | No requirement for either peak | No allele-biased occupancy for any factor | No requirement for either peak | ZBTB43 peak with G bias | NR2F2/NR2F6 peak with T bias |
| Capture-C/4C from EH38E3858447 in colorectal cells to define the contacted promoter | medium | no | Strong contact with MYC promoter | Contacts present but allele-independent | Contacts remain local (POU5F1B/CCAT2) | Local contacts | Local contacts |

## Next experiment

Re-analyse the existing ENCODE HCT116 TCF7L2 ChIP-seq (ENCSR000EUV) for allele-specific reads at chr8:127401060 after confirming HCT116 heterozygosity: this is zero new bench cost and directly tests H1's binding claim against the null H0 (balanced reads would push weight to H0; a clear G bias would confirm allele-specific TCF7L2 occupancy).

## Investigate calls

- qbic_tf_detail({"tf": "TCF7L2"})
- chip_peaks({"tf": "TCF7L2", "biosample": "HCT116"})
- eqtl_lookup({"tissue": null})

## Flags

- coverage_misstated: H3: stated mapped, registry says own_model for NR2F2

Citation support: 1.00 of links cite only evidence that passed every check.

## Evidence

<a id="e01"></a>**E01** variant_annotation, Ensembl VEP (GRCh38) (https://rest.ensembl.org/vep/human/region/8:127401060-127401060:1/T?content-type=application/json&Conservation=1; retrieved 2026-10-25T16:33:46+00:00)

> Variant chr8:127401060:G>T (GRCh38), allele string G/T
> Known IDs: rs6983267
> Most severe consequence: non_coding_transcript_exon_variant
> Regulatory features: ENSR8_CGMBX enhancer
> GERP conservation score at the site: 1.54
> Transcript consequences: CASC8 (intron_variant, non_coding_transcript_variant); CCAT2 (non_coding_transcript_exon_variant); PCAT1 (intron_variant, non_coding_transcript_variant); POU5F1B (intron_variant); PCAT1 (downstream_gene_variant)

<a id="e02"></a>**E02** nearest_genes, Ensembl overlap (protein_coding) (https://rest.ensembl.org/overlap/region/human/8:126401060-128401060?feature=gene;biotype=protein_coding;content-type=application/json; retrieved 2026-10-25T16:33:42+00:00)

> 3 protein-coding genes within 1000 kb of chr8:127401060:G>T, by distance to TSS:
> POU5F1B: 78.9 kb from TSS (in gene body, strand +1)
> MYC: 334.4 kb from TSS (upstream, strand +1)
> LRATD2: 842.6 kb from TSS (upstream, strand -1)

<a id="e03"></a>**E03** ccre_lookup, ENCODE v4 cCRE registry (ENCFF420VPZ) and SCREEN (https://screen-beta-api.wenglab.org/dataws/cre_table; retrieved 2026-10-25T16:32:58+00:00)

> The variant lies in cCRE EH38E3858447 (pELS: proximal enhancer-like), chr8:127401053-127401303.
> SCREEN: 3 cCREs within 500 bp (max z-score across ENCODE biosamples):
> EH38E3858447 pELS (contains the variant): DNase z 5.2, H3K27ac z 4.8, H3K4me3 z 1.5, CTCF z 4.1; nearby genes CCAT2, PCAT1, POU5F1B
> EH38E3858446 pELS: DNase z 4.9, H3K27ac z 4.8, H3K4me3 z 1.5, CTCF z 5.5; nearby genes CCAT2, PCAT1, POU5F1B
> EH38E3858448 pELS: DNase z 5.2, H3K27ac z 4.8, H3K4me3 z 1.5, CTCF z 2.2; nearby genes CCAT2, PCAT1, POU5F1B
> Biosample-specific z-scores are not in this call; the values above are maxima over biosamples.

<a id="e04"></a>**E04** gwas_lookup, GWAS Catalog REST v2 (https://www.ebi.ac.uk/gwas/rest/api/v2/associations?rs_id=rs6983267&size=100; retrieved 2026-10-25T16:33:55+00:00)

> 69 GWAS Catalog associations for rs6983267, strongest first:
> Colorectal cancer: p 2.0e-122, effect allele T, risk-allele frequency NR, PMID 36539618
> Prostate-specific antigen levels: p 9.0e-121, effect allele T, risk-allele frequency NR, PMID 39930085
> Prostate cancer: p 1.0e-113, effect allele G, risk-allele frequency NR, PMID 33398198
> Elevated prostate specific antigen [PSA] (PheCode 796): p 2.0e-96, effect allele G, risk-allele frequency 0.5087, PMID 39024449
> prostate-specific antigen (PSA, maximum, inv-norm transformed): p 7.0e-74, effect allele G, risk-allele frequency 0.5102, PMID 39024449
> Cancer (pleiotropy): p 8.0e-74, effect allele G, risk-allele frequency NR, PMID 32887889
> prostate-specific antigen (PSA, mean, inv-norm transformed): p 1.0e-72, effect allele G, risk-allele frequency 0.5102, PMID 39024449
> Colorectal cancer or advanced adenoma: p 3.0e-64, effect allele G, risk-allele frequency 0.5228, PMID 30510241
> prostate-specific antigen (PSA, minimum, inv-norm transformed): p 6.0e-52, effect allele G, risk-allele frequency 0.5102, PMID 39024449
> Benign neoplasm of colon (PheCode 208): p 2.0e-48, effect allele G, risk-allele frequency 0.5088, PMID 39024449
> Colon polyps: p 6.0e-30, effect allele G, risk-allele frequency 0.566, PMID 39024449
> Colon cancer (PheCode 153.2): p 8.0e-26, effect allele G, risk-allele frequency 0.5899, PMID 39024449

<a id="e05"></a>**E05** finemap_lookup, Open Targets Platform (credible sets, L2G) (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-25T16:33:46+00:00)

> 92 credible sets contain 8_127401060_G_T: 91 GWAS, 1 molecular QTL.
> GWAS Prostate cancer: PIP 1.00; L2G POU5F1B 0.82
> GWAS Prostate cancer: PIP 1.00; L2G POU5F1B 0.82
> GWAS Cancer of prostate (PheCode 185): PIP 1.00; L2G POU5F1B 0.82
> GWAS Elevated prostate specific antigen [PSA] (PheCode 796): PIP 1.00; L2G POU5F1B 0.82
> GWAS Prostate cancer: PIP 1.00; L2G POU5F1B 0.82
> GWAS Prostate cancer: PIP 1.00; L2G POU5F1B 0.82
> sceqtl for PVT1 (OTAR2057_IBDverse_ge_Colon_Goblet_MUC2+_SPDEF+_ENS): PIP 0.95
> Best L2G gene scores across these sets: POU5F1B 0.89, MYC 0.05

<a id="e06"></a>**E06** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=rs6983267%20AND%20POU5F1B%20AND%20%22colorectal%20cancer%22&format=json&pageSize=8&resultType=core; retrieved 2026-10-25T16:33:56+00:00)

> Europe PMC: 52 hits for 'rs6983267 AND POU5F1B AND "colorectal cancer"'; top 8 with PMIDs:
> PMID 41796348 (2026): Harnessing the LncRNA CCAT2 role in gastric cancer: from molecular insights to clinical implications.
> PMID 40498368 (2025): CCAT2 role in gastrointestinal cancer progression and metastasis: a novel target for therapeutic strategies.
> PMID 35812248 (2022): Genome-Wide Association and Transcriptome-Wide Association Studies Identify Novel Susceptibility Genes Contributing to Colorectal Cancer.
> PMID 35987910 (2022): Transposon-activated POU5F1B promotes colorectal cancer growth and metastasis.
> PMID 39284974 (2024): Systematic prioritization of functional variants and effector genes underlying colorectal cancer risk.
> PMID 39921239 (2025): System genetic analysis of intestinal cancer and periodontitis development as influenced by aging and diabesity using Collaborative Cross mice.
> PMID 36103972 (2022): Long non-coding RNA colon cancer-associated transcript 2: role and function in human cancers.
> PMID 34594420 (2021): Repurposing non-invasive prenatal testing data: Population study of single nucleotide variants associated with colorectal cancer and Lynch syndrome.

<a id="e06a"></a>**E06a** literature_search, Europe PMC abstract, PMID 35812248 (https://europepmc.org/article/MED/35812248; retrieved 2026-10-25T16:33:56+00:00)

> In the post-GWAS analyses, we first identified new genome-wide significant associations: three genomic risk loci were identified at 8q24.21 (rs6983267, P = 6.98 × 10-12), 15q13.3 (rs58658771, P = 1.40 × 10-10), and 18q21.1 (rs6507874, P = 1.91 × 10-14).

<a id="e06b"></a>**E06b** literature_search, Europe PMC abstract, PMID 35812248 (https://europepmc.org/article/MED/35812248; retrieved 2026-10-25T16:33:56+00:00)

> In addition, the TWAS also identified four loci statistically significantly associated with CRC risk, largely explained by expression regulation, including six candidate genes (DUSP10, POU5F1B, C11orf53, COLCA1, COLCA2, and GREM1-AS1).

<a id="e06c"></a>**E06c** literature_search, Europe PMC abstract, PMID 35987910 (https://europepmc.org/article/MED/35987910; retrieved 2026-10-25T16:33:56+00:00)

> Correlating this observation, we demonstrate that POU5F1B fosters the proliferation and metastatic potential of CRC cells.

<a id="e07"></a>**E07** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> QBiC-SELEX screen of chr8:127401060:G>T: 997 models scored, 421 pass the gate (Bonferroni 0.05/997, p < 5.02e-05, |z| > 4.05), in 348 CIS-BP groups. Expression context: DepMap line ACH-000971. Groups shown: 10; dropped because no TF in the group reaches 1 TPM: 79 (C2H2 ZF, 1 model z -47.51, C2H2 ZF, 1 model z 44.45, IRF, 2 models z 24.49, Nuclear receptor, 1 model z 21.74, C2H2 ZF, 1 model z -14.52). predicted_effect > 0 means the alternate allele binds more strongly. In vitro binding only: expression and chromatin decide whether a change matters.

<a id="e08"></a>**E08** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G372 (Nuclear receptor, 1 model): best model TLX_NA_Lib1_NA_bhimsaria2023_0(2)_2_7mer (own model of NR2E1), z 53.69, effect 1.968 (alt binds more); 1 passing models (1 with the best model's sign). Passing members: NR2E1 z 53.69. TFs this group covers (own and CIS-BP-mapped models): HNF4A 2.95 TPM, HNF4G 2.24 TPM, NR2E1 0.0 TPM; best model's site strength: ref 96.7th, alt 99.6th percentile of its k-mer coefficients.

<a id="e09"></a>**E09** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G521 (C2H2 ZF, 1 model): best model ZNF493_FL_TG40NTCTTGC_YWRA_jolma2025_0_2_7mer (own model of ZNF493), z -34.16, effect -0.598 (alt binds less); 1 passing models (1 with the best model's sign). Passing members: ZNF493 z -34.16. TFs this group covers (own and CIS-BP-mapped models): ZNF493 1.33 TPM; best model's site strength: ref 100.0th, alt 88.9th percentile of its k-mer coefficients.

<a id="e10"></a>**E10** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G071 (C2H2 ZF, 2 models): best model GFI1B_eDBD_TTCTCA40NCCT_KR_yin2017_0_3_7mer (own model of GFI1B), z -31.27, effect -2.144 (alt binds less); 2 passing models (2 with the best model's sign). Passing members: GFI1B z -31.27, GFI1 z -29.52. TFs this group covers (own and CIS-BP-mapped models): GFI1 2.9 TPM, GFI1B 0.05 TPM; best model's site strength: ref 99.9th, alt 99.6th percentile of its k-mer coefficients.

<a id="e11"></a>**E11** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G101 (T-box, 2 models): best model TBX19_eDBD_TCTTGT40NCAG_KP_yin2017_0_4_7mer (own model of TBX19), z 26.18, effect 4.18 (alt binds more); 2 passing models (2 with the best model's sign). Passing members: TBX19 z 26.18, TBXT z 11.73. TFs this group covers (own and CIS-BP-mapped models): TBX19 1.92 TPM, TBXT 0.0 TPM; best model's site strength: ref 79.0th, alt 99.9th percentile of its k-mer coefficients.

<a id="e12"></a>**E12** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G404 (C2H2 ZF, 1 model): best model ZBTB43_eDBD_TACGGT40NTAC_KR_yin2017_0_3_7mer (own model of ZBTB43), z -23.26, effect -1.724 (alt binds less); 1 passing models (1 with the best model's sign). Passing members: ZBTB43 z -23.26. TFs this group covers (own and CIS-BP-mapped models): ZBTB43 8.32 TPM; best model's site strength: ref 99.8th, alt 87.9th percentile of its k-mer coefficients.

<a id="e13"></a>**E13** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G233 (CCCH ZF, 1 model): best model MBNL2_FL_TCTAAG40NTTA_KZ_yin2017_0_4_7mer (own model of MBNL2), z -22.42, effect -2.708 (alt binds less); 1 passing models (1 with the best model's sign). Passing members: MBNL2 z -22.42. TFs this group covers (own and CIS-BP-mapped models): MBNL2 26.09 TPM; best model's site strength: ref 99.1th, alt 51.1th percentile of its k-mer coefficients.

<a id="e14"></a>**E14** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G002 (Nuclear receptor, 29 models): best model NR2F6_FL_TGCCTC40NCAA_KV_yin2017_0_4_7mer (own model of NR2F6), z 20.82, effect 1.92 (alt binds more); 11 passing models (9 with the best model's sign); members disagree on direction. Passing members: NR2F6 z 20.82, NR2C1 z 7.56, THRA z 7.37, NR2C2 z -6.01, NR4A1 z 6.0 (+6 more). TFs this group covers (own and CIS-BP-mapped models): NR2F2 61.74 TPM, PPARG 47.9 TPM, ESRRA 38.54 TPM, NR1D2 37.06 TPM, NR2F6 37.02 TPM, RARG 31.32 TPM, NR2F1 28.42 TPM, NR2C2 22.6 TPM, NR1H2 20.86 TPM, PPARD 20.8 TPM (+28 more); best model's site strength: ref 98.6th, alt 100.0th percentile of its k-mer coefficients.

<a id="e15"></a>**E15** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G413 (C2H2 ZF, 1 model): best model ZBTB8A_DBD_GG40NGGTTTA_YWEA_jolma2025_0_2_7mer (own model of ZBTB8A), z -19.7, effect -0.603 (alt binds less); 1 passing models (1 with the best model's sign). Passing members: ZBTB8A z -19.7. TFs this group covers (own and CIS-BP-mapped models): ZBTB8A 6.4 TPM; best model's site strength: ref 97.8th, alt 62.5th percentile of its k-mer coefficients.

<a id="e16"></a>**E16** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G037 (Nuclear receptor, 3 models): best model ESRRG_FL_TGAGCT40NGCA_KW_yin2017_0_3_7mer (own model of ESRRG), z 19.58, effect 0.719 (alt binds more); 2 passing models (2 with the best model's sign). Passing members: ESRRG z 19.58, ESRRB z 7.9. TFs this group covers (own and CIS-BP-mapped models): ESRRA 38.54 TPM, ESRRB 0.41 TPM, ESR2 0.23 TPM, ESR1 0.0 TPM, ESRRG 0.0 TPM; best model's site strength: ref 97.9th, alt 99.0th percentile of its k-mer coefficients.

<a id="e17"></a>**E17** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G077 (AT hook, 2 models): best model SETBP1_DBD2_TC40NGGCTGT_YWHA_jolma2025_0_4_7mer (own model of SETBP1), z -16.06, effect -0.331 (alt binds less); 1 passing models (1 with the best model's sign). Passing members: SETBP1 z -16.06. TFs this group covers (own and CIS-BP-mapped models): HMGA1 1349.55 TPM, HMGA2 125.72 TPM, SRCAP 32.16 TPM, ASH1L 18.03 TPM, SETBP1 0.01 TPM; best model's site strength: ref 95.5th, alt 68.2th percentile of its k-mer coefficients.

<a id="e18"></a>**E18** qbic_tf_detail, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> {"tf":"TCF7L2","symbol":"TCF7L2","via":"hgnc_symbol","notes":[],"coverage":"mapped","variant":"chr8:127401060:G>T","gate_p":5.02e-05,"models":[{"model":"LEF1_FL_TAGTCG40NAGA_KZ_yin2017_0_3_7mer","mapping":"CIS-BP (LEF1)","group":"G041 HMG/Sox, 3 models","quality":0.63,"effect":-0.47,"z":-4.66,"p":3.2e-06,"rank_abs_z":"351/997","passed_gate":true,"site_strength":{"ref_percentile":98.8,"alt_percentile":98.4,"k":7}},{"model":"TCF7_eDBD_TCGGAC40NCCA_KS_yin2017_0_3_7mer","mapping":"CIS-BP (TCF7)","group":"G041 HMG/Sox, 3 models","quality":0.732,"effect":-0.229,"z":-4.59,"p":4.4e-06,"rank_abs_z":"367/997","passed_gate":true,"site_strength":{"ref_percentile":96.9,"alt_percentile":99.2,"k":7}},{"model":"TCF7L1_eDBD_TTGGCA40NTCG_KW_yin2017_0_3_7mer","mapping":"CIS-BP (TCF7L1)","group":"G041 HMG/Sox, 3 models","quality":0.602,"effect":-0.275,"z":-3.47,"p":0.00052,"rank_abs_z":"486/997","passed_gate":false,"site_strength":{"ref_percentile":83.5,"alt_percentile":92.1,"k":7}}]}

<a id="e19"></a>**E19** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-25T16:35:30+00:00)

> 1 ENCODE TCF7L2 ChIP-seq peaks contain chr8:127401060:G>T in biosamples matching 'HCT116': biosamples HCT116; experiments ENCSR000EUV.

<a id="e20"></a>**E20** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr8_127401060_G_T_b38&datasetId=gtex_v8; retrieved 2026-10-25T16:35:30+00:00)

> 2 significant GTEx v8 single-tissue eQTLs for chr8_127401060_G_T_b38. NES is the effect of the alt allele (T) relative to ref (G).
> CASC8 in Whole_Blood: NES -0.32, p 6.3e-10
> POU5F1B in Colon_Transverse: NES +0.20, p 8.2e-06
