# rs73706717 and Colorectal cancer (8q24)

Configuration `full`, named mode, seed 0. Models: generator openai/gpt-6-luna, critic openai/gpt-6-luna, summariser openai/gpt-6-luna. Cost $0.01 over 8 model calls; 252 s.

Variant `chr8:127401265:T>C` (germline); expression context: DepMap:ACH-000971 (HCT 116).

## QBiC-SELEX screen (occupancy first)

Occupied candidates: TCF7L2 (bound here, z -8.8, weak site); SP1 (bound here, z -7.07, weak site); NFIC (bound elsewhere, z 24.28); NFIA (bound elsewhere, z 24.28); HNF1B (bound elsewhere, z -23.93); CTCF (bound elsewhere, z 8.21); CEBPB (bound elsewhere, z -6.94); TFAP4 (bound elsewhere, z 0.51, no clear allelic change); NR2F2 (bound elsewhere, z -15.02, weak site); NR2F6 (bound elsewhere, z -15.02, weak site). Occupancy unknown: ZBTB22 (z -33.75); NR1H3 (z -15.02); TET3 (z 14.12); NR1D2 (z -13.82); NR4A2 (z -13.82). Diagnostic, not shown to the model: 307 of 997 models pass Bonferroni.

## Ranked chains

### 1. H4: No TF-mediated effect of rs73706717 (p = 0.62)

Null chain: no TF-mediated effect of this variant.

Predictions: There is no reproducible allele-specific TF occupancy or regulatory effect of this base in relevant colorectal cells.; Any disease association, if present, is due to another linked variant or a mechanism other than TF-mediated activity of rs73706717.; The pELS annotation and ChIP peaks may reflect element activity or occupancy unrelated to an allelic effect at this nucleotide.

Falsified if: Isogenic allele editing reproducibly changes allele-specific TF occupancy at this base and changes expression of a gene linked to the element.

### 2. H1: TCF7L2 binding change at the pELS element may affect POU5F1B (p = 0.18)

TF TCF7L2 (QBiC-SELEX coverage mapped), ref allele binds more; element EH38E3858447; gene POU5F1B; cell type HCT116.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | TCF7L2 is a plausible factor because it is expressed and has a ChIP-seq peak over the variant in HCT116. A QBiC-SELEX model mapped from TCF7 predicts stronger binding to ref T, but the predicted site is weak and this is not a TCF7L2-specific model; the allelic effect remains uncertain. | weak | [E05](#e05), [E20](#e20) |
| element | The variant lies in pELS cCRE EH38E3858447, but the reported activity scores are maxima across biosamples and do not establish activity in HCT116 or an allele-dependent change in element activity. | supported | [E01](#e01), [E03](#e03) |
| gene | POU5F1B is a candidate target because it is relatively close and is listed among the cCRE's nearby genes; no direct link from this element to POU5F1B is shown. | weak | [E02](#e02), [E03](#e03) |
| cell_type | HCT116 is a plausible context: TCF7L2 occupancy over the variant and TCF7L2 expression are reported in this line. | supported | [E05](#e05), [E20](#e20) |
| phenotype | If this element changes POU5F1B expression, it could affect colon-cancer cellular traits, but the evidence does not show that rs73706717 does so or that it is associated with colorectal cancer risk. | weak | [E18b](#e18b), [E37](#e37), [E15](#e15), [E17](#e17) |

Predictions: In informative HCT116 TCF7L2 ChIP reads, the variant-bearing site should show ref-favored allelic occupancy; this prediction is uncertain because the mapped model describes a weak site.; If the variant acts through this element, editing it or perturbing the element may alter POU5F1B expression; the direction of the expression change is not determined by binding direction alone.; The chain predicts a TCF7L2-specific allele effect, unlike the SP1 and NFIC chains.

Falsified if: Informative allele-specific TCF7L2 occupancy assays show no ref-favored binding, especially after confirming the variant is present in the assayed cells.; Element perturbation or isogenic editing has no reproducible effect on POU5F1B, while a different target responds specifically.

### 3. H5: NFIC binding gain at the pELS element may affect POU5F1B (p = 0.12)

TF NFIC (QBiC-SELEX coverage own_model), alt allele binds more; element EH38E3858447; gene POU5F1B; cell type HCT116.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | NFIC is a provisional candidate: it is expressed, and a QBiC-SELEX model mapped from NFIB predicts substantially stronger binding to alt C at a strong site. NFIC occupancy over the variant is reported in HepG2, not HCT116; the model and occupancy therefore do not establish an NFIC effect in the colorectal cell context. | weak | [E04](#e04), [E22](#e22) |
| element | The variant lies in pELS cCRE EH38E3858447, but the reported activity scores are maxima across biosamples and do not establish activity in HCT116 or an allele-dependent change in element activity. | supported | [E01](#e01), [E03](#e03) |
| gene | POU5F1B is a candidate target because it is relatively close and is listed among the cCRE's nearby genes; no direct link from this element to POU5F1B is shown. | weak | [E02](#e02), [E03](#e03) |
| cell_type | HCT116 expresses NFIC, but the supplied occupancy evidence for NFIC at this site is from HepG2 rather than HCT116, so occupancy in the proposed colorectal context is unestablished. | supported | [E22](#e22) |
| phenotype | If this element changes POU5F1B expression, it could affect colon-cancer cellular traits, but the evidence does not show that rs73706717 does so or that it is associated with colorectal cancer risk. | weak | [E18b](#e18b), [E37](#e37), [E15](#e15), [E17](#e17) |

Predictions: If NFIC occupies this site in HCT116, allele-specific assays should favor alt C; the chain predicts an alt-favored NFIC effect, unlike H1 and H3.; This chain predicts NFIC occupancy at the variant in HCT116, which is not established by the supplied data.; If the variant acts through this element, editing it or perturbing the element may alter POU5F1B expression; the direction of the expression change is not determined by binding direction alone.

Falsified if: NFIC occupancy is absent at the site in HCT116 under conditions with adequate assay sensitivity.; Allele-specific NFIC assays show no alt-favored occupancy, or isogenic editing and element perturbation show no reproducible effect on POU5F1B.

### 4. H3: SP1 binding change at the pELS element may affect POU5F1B (p = 0.08)

TF SP1 (QBiC-SELEX coverage own_model), ref allele binds more; element EH38E3858447; gene POU5F1B; cell type HCT116.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | SP1 is a plausible factor because it is expressed and has a ChIP-seq peak over the variant in HCT116. A QBiC-SELEX model mapped from SP3 predicts stronger binding to ref T, but the predicted site is weak and the model does not establish an SP1-specific allelic effect. | weak | [E06](#e06), [E21](#e21) |
| element | The variant lies in pELS cCRE EH38E3858447, but the reported activity scores are maxima across biosamples and do not establish activity in HCT116 or an allele-dependent change in element activity. | supported | [E01](#e01), [E03](#e03) |
| gene | POU5F1B is a candidate target because it is relatively close and is listed among the cCRE's nearby genes; no direct link from this element to POU5F1B is shown. | weak | [E02](#e02), [E03](#e03) |
| cell_type | HCT116 is a plausible context: SP1 occupancy over the variant and SP1 expression are reported in this line. | supported | [E06](#e06), [E21](#e21) |
| phenotype | If this element changes POU5F1B expression, it could affect colon-cancer cellular traits, but the evidence does not show that rs73706717 does so or that it is associated with colorectal cancer risk. | weak | [E18b](#e18b), [E37](#e37), [E15](#e15), [E17](#e17) |

Predictions: In informative HCT116 SP1 ChIP reads, the variant-bearing site should show ref-favored allelic occupancy; this prediction is uncertain because the mapped model describes a weak site.; If the variant acts through this element, editing it or perturbing the element may alter POU5F1B expression; the direction of the expression change is not determined by binding direction alone.; The chain predicts an SP1-specific allele effect, rather than the TCF7L2-specific effect predicted by H1 or the alt-favored NFIC effect predicted by H5.

Falsified if: Informative allele-specific SP1 occupancy assays show no ref-favored binding, especially after confirming the variant is present in the assayed cells.; Element perturbation or isogenic editing has no reproducible effect on POU5F1B, while a different target responds specifically.

## Prediction matrix

| Test | Cost | Separates top two | H4 | H1 | H5 | H3 |
| --- | --- | --- | --- | --- | --- | --- |
| Reanalyze available HCT116 TCF7L2 ChIP-seq reads for allelic imbalance at rs73706717, conditional on informative coverage and a heterozygous genotype. | existing data | yes | No reproducible allelic imbalance is expected. | Ref T-enriched TCF7L2 reads at the variant would support this chain; no imbalance would weaken it. | No TCF7L2-specific ref enrichment is predicted; this chain instead predicts alt-favored NFIC occupancy if NFIC occupies the site. | No TCF7L2-specific ref enrichment is predicted; SP1-specific allelic imbalance would instead support H3. |
| Measure allele-specific SP1 and NFIC occupancy at the variant in HCT116 using targeted CUT&RUN or ChIP, with genotype and input controls. | medium | no | No reproducible allele-specific occupancy for these factors is expected. | No SP1- or NFIC-specific allelic effect is required; H1 predicts ref-favored TCF7L2 occupancy. | Alt-favored NFIC occupancy supports H5; absence of NFIC occupancy in HCT116 weakens it. | Ref-favored SP1 occupancy supports H3. |
| Perturb EH38E3858447 in HCT116 and measure POU5F1B expression, with a non-targeting control and a local-element control. | medium | yes | No reproducible POU5F1B response is expected. | A reproducible POU5F1B response supports a regulatory role for the element, though it does not alone identify TCF7L2 or prove an allelic effect. | A reproducible POU5F1B response supports a regulatory role for the element, though it does not alone identify NFIC or prove an allelic effect. | A reproducible POU5F1B response supports a regulatory role for the element, though it does not alone identify SP1 or prove an allelic effect. |

## Next experiment

Cheapest first test: reanalyze existing HCT116 TCF7L2 ChIP-seq reads for allelic imbalance at rs73706717, provided the sample is heterozygous and reads cover the site. Ref-enriched reads would support H1 over the null; balanced reads would weaken H1. If the existing data are not informative, use targeted allele-specific TCF7L2 occupancy assays in genotyped HCT116 cells.

## Investigate calls

- literature_search({"query": "rs73706717 POU5F1B colorectal cancer enhancer regulatory variant"})
- literature_search({"query": "rs73706717 MYC colorectal cancer enhancer regulatory variant"})
- gene_disease({"gene": "POU5F1B"})

## Flags

- literature_fallback: no hits for 'rs73706717 AND POU5F1B AND "colorectal cancer"'; dropped the rsID

Citation support: 1.00 of links cite only evidence that passed every check.

## Evidence

<a id="e01"></a>**E01** variant_annotation, Ensembl VEP (GRCh38) (https://rest.ensembl.org/vep/human/region/8:127401265-127401265:1/C?content-type=application/json&Conservation=1; retrieved 2026-10-26T02:21:56+00:00)

> Variant chr8:127401265:T>C (GRCh38), allele string T/C
> Known IDs: rs73706717
> Most severe consequence: non_coding_transcript_exon_variant
> Regulatory features: ENSR8_CGMBX enhancer
> GERP conservation score at the site: -2.8
> Transcript consequences: CASC8 (intron_variant, non_coding_transcript_variant); CCAT2 (non_coding_transcript_exon_variant); PCAT1 (intron_variant, non_coding_transcript_variant); POU5F1B (intron_variant); PCAT1 (downstream_gene_variant)

<a id="e02"></a>**E02** nearest_genes, Ensembl overlap (protein_coding) (https://rest.ensembl.org/overlap/region/human/8:126401265-128401265?feature=gene;biotype=protein_coding;content-type=application/json; retrieved 2026-10-26T02:21:59+00:00)

> 3 protein-coding genes within 1000 kb of chr8:127401265:T>C, by distance to TSS:
> POU5F1B: 79.1 kb from TSS (in gene body, strand +1)
> MYC: 334.2 kb from TSS (upstream, strand +1)
> LRATD2: 842.8 kb from TSS (upstream, strand -1)

<a id="e03"></a>**E03** ccre_lookup, ENCODE v4 cCRE registry (ENCFF420VPZ) and SCREEN (https://screen-beta-api.wenglab.org/dataws/cre_table; retrieved 2026-10-26T02:21:42+00:00)

> The variant lies in cCRE EH38E3858447 (pELS: proximal enhancer-like), chr8:127401053-127401303.
> SCREEN: 3 cCREs within 500 bp (max z-score across ENCODE biosamples):
> EH38E3858447 pELS (contains the variant): DNase z 5.2, H3K27ac z 4.8, H3K4me3 z 1.5, CTCF z 4.1; nearby genes CCAT2, PCAT1, POU5F1B
> EH38E3858448 pELS: DNase z 5.2, H3K27ac z 4.8, H3K4me3 z 1.5, CTCF z 2.2; nearby genes CCAT2, PCAT1, POU5F1B
> EH38E3858446 pELS: DNase z 4.9, H3K27ac z 4.8, H3K4me3 z 1.5, CTCF z 5.5; nearby genes CCAT2, PCAT1, POU5F1B
> Biosample-specific z-scores are not in this call; the values above are maxima over biosamples.

<a id="e04"></a>**E04** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> ENCODE TF ChIP-seq at chr8:127401265:T>C: 149 peaks contain the variant, from 83 factors in 25 biosamples. In the matching biosample HCT116: 3 peaks from 3 factors. cCRE class at the variant: pELS. Bound factors outside the TF model collection (co-factors, Pol II, and TFs with no binding model; signs of an active element, not TF candidates): ASH2L, CHD4, EP300, HDAC1, HDAC2, HMGXB4, KDM1A, KDM6A, LCORL, LIN54, MED1, MED13 (+26 more). Bound, expressed TFs with a binding model: 40; listed one per row: TCF7L2, SP1, CTCF, CEBPB, MYBL2, NR2C2, TFAP4, ISL2, NR2F2, ERF; also bound: NR2F6, NFIC, ELF1, ZNF317, NFIL3, ZBTB7B, KLF16, PITX1, JUNB, SKI, CREM, RXRB, ATF2, ZNF609, ZNF280D, ZNF12, AHDC1, ZNF652, PHF21A, ETS1, NFIA, NR3C1, BCL6, PRDM10, HOXA3, HNF4A, MNX1, HNF1B, ZNF362, FOXA1. Bound but below 1 TPM: FOXA2, HNF1A, ONECUT1, SOX6, TBX2. Assayed with no peak here: 11 TFs in the matching biosample, 517 only elsewhere; never assayed: 536.

<a id="e05"></a>**E05** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> TCF7L2: bound here. 4 ENCODE ChIP-seq peak(s) contain the variant, in the matching biosample HCT116; also in HepG2 (e.g. ENCSR000EUV). 63.61 TPM in DepMap:ACH-000971 (HCT 116), rank 53 of 1626 TFs.

<a id="e06"></a>**E06** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> SP1: bound here. 2 ENCODE ChIP-seq peak(s) contain the variant, in the matching biosample HCT116; also in HepG2 (e.g. ENCSR000BSF). 38.96 TPM in DepMap:ACH-000971 (HCT 116), rank 118 of 1626 TFs.

<a id="e07"></a>**E07** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> CTCF: bound elsewhere. 34 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: A549, C4-2B, Panc1, RWPE2, adrenal gland, astrocyte (+13 more) (e.g. ENCSR173IEA). 50.0 TPM in DepMap:ACH-000971 (HCT 116), rank 78 of 1626 TFs.

<a id="e08"></a>**E08** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> CEBPB: bound elsewhere. 3 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: HepG2 (e.g. ENCSR000BQI). 13.15 TPM in DepMap:ACH-000971 (HCT 116), rank 408 of 1626 TFs.

<a id="e09"></a>**E09** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> MYBL2: bound elsewhere. 2 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: HepG2 (e.g. ENCSR581KCO). 67.51 TPM in DepMap:ACH-000971 (HCT 116), rank 46 of 1626 TFs.

<a id="e10"></a>**E10** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> NR2C2: bound elsewhere. 2 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: HepG2 (e.g. ENCSR559ZKI). 22.6 TPM in DepMap:ACH-000971 (HCT 116), rank 244 of 1626 TFs.

<a id="e11"></a>**E11** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> TFAP4: bound elsewhere. 2 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: HepG2 (e.g. ENCSR587BVQ). 19.72 TPM in DepMap:ACH-000971 (HCT 116), rank 283 of 1626 TFs.

<a id="e12"></a>**E12** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> ISL2: bound elsewhere. 2 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: HepG2 (e.g. ENCSR492IHH). 2.77 TPM in DepMap:ACH-000971 (HCT 116), rank 862 of 1626 TFs.

<a id="e13"></a>**E13** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> NR2F2: bound elsewhere. 1 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: HepG2 (e.g. ENCSR000BVM). 61.74 TPM in DepMap:ACH-000971 (HCT 116), rank 58 of 1626 TFs.

<a id="e14"></a>**E14** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> ERF: bound elsewhere. 1 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: HepG2 (e.g. ENCSR159DQO). 46.58 TPM in DepMap:ACH-000971 (HCT 116), rank 90 of 1626 TFs.

<a id="e15"></a>**E15** gwas_lookup, GWAS Catalog REST v2 (https://www.ebi.ac.uk/gwas/rest/api/v2/associations?rs_id=rs73706717&size=100; retrieved 2026-10-26T02:21:56+00:00)

> 0 GWAS Catalog associations for rs73706717, strongest first:

<a id="e16"></a>**E16** finemap_lookup, Open Targets Platform (credible sets, L2G) (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-26T02:21:56+00:00)

> 2 credible sets contain 8_127401265_T_C: 2 GWAS, 0 molecular QTL.
> GWAS prostate-specific antigen (PSA, maximum, inv-norm transforme: PIP 0.04; L2G POU5F1B 0.83
> GWAS Urinary incontinence (PheCode 599.4): PIP 0.04; L2G POU5F1B 0.78
> Best L2G gene scores across these sets: POU5F1B 0.83

<a id="e17"></a>**E17** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr8_127401265_T_C_b38&datasetId=gtex_v8; retrieved 2026-10-26T02:23:32+00:00)

> 0 significant GTEx v8 single-tissue eQTLs for chr8_127401265_T_C_b38. NES is the effect of the alt allele (C) relative to ref (T).

<a id="e18"></a>**E18** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=POU5F1B%20AND%20%22colorectal%20cancer%22&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T02:21:59+00:00)

> Europe PMC: 150 hits for 'POU5F1B AND "colorectal cancer"'; top 8 with PMIDs:
> PMID 42465001 (2026): Circ_0075829 affects POU5F1B expression through sponging miR-576-3p to promote growth, invasion, and angiogenesis of colon cancer cells.
> PMID 41993623 (2026): Tailorable porous collagen hydrogels as a physiologically relevant platform for extrachromosomal DNA-associated colorectal cancer research.
> PMID 41796348 (2026): Harnessing the LncRNA CCAT2 role in gastric cancer: from molecular insights to clinical implications.
> PMID 41930642 (2026): Systematic Identification and Characterization of Causal Risk Genes Implicated in Colorectal Cancer by Integrating GWAS, eQTL, and mQTL Data.
> PMID 42686757 (2026): Phase separation of ecDNA condensates establishes in-trans contact domains that boost selective MYC regulatory interactions.
> PMID 40506516 (2025): Association between methylation quantitative trait loci and colorectal cancer risk, survival and cancer recurrence.
> PMID 41144378 (2025): Integrative GWAS and RNA-Seq analysis for target identification and virtual drug screening in colorectal cancer.
> PMID 41196428 (2025): Combined CHK1 and PD-L1 blockade as a novel therapeutic strategy against stemness and immunosuppression in ovarian cancer.

<a id="e18a"></a>**E18a** literature_search, Europe PMC abstract, PMID 42465001 (https://europepmc.org/article/MED/42465001; retrieved 2026-10-26T02:21:59+00:00)

> Circ_0075829 acted as a molecular sponge for microRNA-576-3p (miR-576-3p), thereby upregulating the expression of POU class 5 homeobox 1B (POU5F1B) in colon cancer cells.

<a id="e18b"></a>**E18b** literature_search, Europe PMC abstract, PMID 42465001 (https://europepmc.org/article/MED/42465001; retrieved 2026-10-26T02:21:59+00:00)

> Collectively, circ_0075829 promotes proliferation, invasion, and angiogenesis, while inhibiting apoptosis in colon cancer by modulating POU5F1B levels through miR-576-3p sponging.

<a id="e18c"></a>**E18c** literature_search, Europe PMC abstract, PMID 41930642 (https://europepmc.org/article/MED/41930642; retrieved 2026-10-26T02:21:59+00:00)

> A few potential regulatory influences on CRC development associated with genes and variants, such as POU5F1B and rs10797801, were identified.

<a id="e18d"></a>**E18d** literature_search, Europe PMC abstract, PMID 40506516 (https://europepmc.org/article/MED/40506516; retrieved 2026-10-26T02:21:59+00:00)

> Four regions mapped to POU5F1B, POU2AF2 (c11orf53)/POU2AF3 (COLCA2), GREM1 and CABLES2 were previously identified.

<a id="e19"></a>**E19** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> QBiC-SELEX screen of chr8:127401265:T>C, one line per TF, each with the TF's own or CIS-BP-mapped model of largest |z|. Candidates are TFs whose ENCODE ChIP-seq peaks contain the variant and that are expressed (DepMap line ACH-000971), bound here before bound elsewhere, then a strong site before a weak one, then by |z|; then expressed TFs ENCODE never assayed whose best model passes the gate (occupancy unknown). Shown: 10 of 40 occupied (6 with a strong site), 5 of 103 with unknown occupancy. Left out: 11 TFs assayed in the matching biosample and 517 assayed only elsewhere, none with a peak here; 5 bound but below 1 TPM. The gate (|z| > 4.05, Bonferroni over 997 models) marks a change QBiC-SELEX detects; it says nothing about occupancy. Effect > 0 means the alternate allele binds more strongly. In vitro binding only. Site strength is the better allele's best k-mer over the variant, as a percentile of the best model's k-mers; a strong site reaches the 97.5th. At a weak site the ChIP peak more likely reflects another site in the element.

<a id="e20"></a>**E20** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> TCF7L2 (HMG/Sox, 3 models; QBiC-SELEX coverage: mapped models only): best model TCF7_eDBD_TCGGAC40NCCA_KS_yin2017_0_3_7mer (a CIS-BP-mapped model of TCF7), z -8.8, effect -0.429: ref allele binds more (|z| above the gate), but between weak k-mers. 63.61 TPM, rank 53 of 1626 TFs in DepMap:ACH-000971 (HCT 116). Occupancy: bound here: ENCODE ChIP-seq peak over the variant in HCT116, e.g. ENCSR000EUV. Best model's site strength: ref 90.0th, alt 87.2th percentile of its k-mer coefficients: a weak site (neither allele reaches the 97.5th), so the ChIP peak more likely reflects another site in the element.

<a id="e21"></a>**E21** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> SP1 (C2H2 ZF, 5 models; QBiC-SELEX coverage: own model): best model SP3_eDBD_TTCACC40NGCT_KR_yin2017_0_3_7mer (a CIS-BP-mapped model of SP3), z -7.07, effect -0.298: ref allele binds more (|z| above the gate), but between weak k-mers. 38.96 TPM, rank 118 of 1626 TFs in DepMap:ACH-000971 (HCT 116). Occupancy: bound here: ENCODE ChIP-seq peak over the variant in HCT116, e.g. ENCSR000BSF. Best model's site strength: ref 90.4th, alt 75.6th percentile of its k-mer coefficients: a weak site (neither allele reaches the 97.5th), so the ChIP peak more likely reflects another site in the element.

<a id="e22"></a>**E22** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> NFIC (SMAD, 4 models; QBiC-SELEX coverage: own model): best model NFIB_NA_TCATCA20NCG_ESAD_yang2017_0_3_7mer (a CIS-BP-mapped model of NFIB), z 24.28, effect 1.783: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 36.29 TPM, rank 137 of 1626 TFs in DepMap:ACH-000971 (HCT 116). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in HepG2, e.g. ENCSR000BQX. Best model's site strength: ref 96.3th, alt 99.5th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e23"></a>**E23** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> NFIA (SMAD, 4 models; QBiC-SELEX coverage: own model): best model NFIB_NA_TCATCA20NCG_ESAD_yang2017_0_3_7mer (a CIS-BP-mapped model of NFIB), z 24.28, effect 1.783: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 7.07 TPM, rank 616 of 1626 TFs in DepMap:ACH-000971 (HCT 116). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in HepG2, e.g. ENCSR226QQM. Best model's site strength: ref 96.3th, alt 99.5th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e24"></a>**E24** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> HNF1B (Homeodomain, 3 models; QBiC-SELEX coverage: own model): best model HMBOX1_eDBD_TGGCTC40NCGC_KAN_yin2017_1_2_7mer (a CIS-BP-mapped model of HMBOX1), z -23.93, effect -0.32: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 2.08 TPM, rank 929 of 1626 TFs in DepMap:ACH-000971 (HCT 116). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in HepG2, e.g. ENCSR127XTZ. Best model's site strength: ref 100.0th, alt 67.8th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e25"></a>**E25** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> CTCF (C2H2 ZF, 1 model; QBiC-SELEX coverage: own model): best model CTCF_FL_TG40NCTGTGG_YWL_jolma2025_0_3_7mer (its own model), z 8.21, effect 0.902: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 50.0 TPM, rank 78 of 1626 TFs in DepMap:ACH-000971 (HCT 116). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in A549, C4-2B, Panc1, RWPE2, adrenal gland (+14 more), e.g. ENCSR173IEA. Best model's site strength: ref 98.8th, alt 99.4th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e26"></a>**E26** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> CEBPB (bZIP, 3 models; QBiC-SELEX coverage: own model): best model CEBPB_eDBD_TATAAA40NACG_KAN_yin2017_0_4_7mer (its own model), z -6.94, effect -0.844: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 13.15 TPM, rank 408 of 1626 TFs in DepMap:ACH-000971 (HCT 116). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in HepG2, e.g. ENCSR000BQI. Best model's site strength: ref 98.2th, alt 73.1th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e27"></a>**E27** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> TFAP4 (bHLH, 1 model; QBiC-SELEX coverage: own model): best model TFAP4_NA_TCACGT20NGCA_ESAC_yang2017_0_3_7mer (its own model), z 0.51, effect 0.042: alt allele binds slightly more; occupied, no clear allelic change (|z| below the gate). 19.72 TPM, rank 283 of 1626 TFs in DepMap:ACH-000971 (HCT 116). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in HepG2, e.g. ENCSR587BVQ. Best model's site strength: ref 98.2th, alt 96.4th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e28"></a>**E28** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> NR2F2 (Nuclear receptor, 29 models; QBiC-SELEX coverage: own model): best model NR1H3_DBD_TGAGCG40NTTG_KY_nitta2015_2_3_7mer (a CIS-BP-mapped model of NR1H3), z -15.02, effect -0.286: ref allele binds more (|z| above the gate), but between weak k-mers. 61.74 TPM, rank 58 of 1626 TFs in DepMap:ACH-000971 (HCT 116). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in HepG2, e.g. ENCSR000BVM. Best model's site strength: ref 95.9th, alt 60.2th percentile of its k-mer coefficients: a weak site (neither allele reaches the 97.5th), so the ChIP peak more likely reflects another site in the element.

<a id="e29"></a>**E29** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> NR2F6 (Nuclear receptor, 29 models; QBiC-SELEX coverage: own model): best model NR1H3_DBD_TGAGCG40NTTG_KY_nitta2015_2_3_7mer (a CIS-BP-mapped model of NR1H3), z -15.02, effect -0.286: ref allele binds more (|z| above the gate), but between weak k-mers. 37.02 TPM, rank 133 of 1626 TFs in DepMap:ACH-000971 (HCT 116). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in HepG2, e.g. ENCSR798IJO. Best model's site strength: ref 95.9th, alt 60.2th percentile of its k-mer coefficients: a weak site (neither allele reaches the 97.5th), so the ChIP peak more likely reflects another site in the element.

<a id="e30"></a>**E30** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> ZBTB22 (C2H2 ZF, 1 model; QBiC-SELEX coverage: own model): best model ZBTB22_eDBD_TGCCTC40NCAA_KP_yin2017_0_4_7mer (its own model), z -33.75, effect -1.962: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 3.74 TPM, rank 794 of 1626 TFs in DepMap:ACH-000971 (HCT 116). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 99.8th, alt 92.4th percentile of its k-mer coefficients.

<a id="e31"></a>**E31** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> NR1H3 (Nuclear receptor, 29 models; QBiC-SELEX coverage: own model): best model NR1H3_DBD_TGAGCG40NTTG_KY_nitta2015_2_3_7mer (its own model), z -15.02, effect -0.286: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 11.39 TPM, rank 459 of 1626 TFs in DepMap:ACH-000971 (HCT 116). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 95.9th, alt 60.2th percentile of its k-mer coefficients.

<a id="e32"></a>**E32** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> TET3 (CxxC, 2 models; QBiC-SELEX coverage: own model): best model CXXC4_FL_GG40NTAGTTT_YWKC_jolma2025_0_4_7mer (a CIS-BP-mapped model of CXXC4), z 14.12, effect 0.794: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 10.17 TPM, rank 497 of 1626 TFs in DepMap:ACH-000971 (HCT 116). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 87.7th, alt 96.6th percentile of its k-mer coefficients.

<a id="e33"></a>**E33** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> NR1D2 (Nuclear receptor, 29 models; QBiC-SELEX coverage: own model): best model NR2C1_eDBD_TATTCA40NAGT_KT_yin2017_0_3_7mer (a CIS-BP-mapped model of NR2C1), z -13.82, effect -0.705: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 37.06 TPM, rank 132 of 1626 TFs in DepMap:ACH-000971 (HCT 116). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 97.3th, alt 92.0th percentile of its k-mer coefficients.

<a id="e34"></a>**E34** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> NR4A2 (Nuclear receptor, 29 models; QBiC-SELEX coverage: own model): best model NR2C1_eDBD_TATTCA40NAGT_KT_yin2017_0_3_7mer (a CIS-BP-mapped model of NR2C1), z -13.82, effect -0.705: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 7.19 TPM, rank 611 of 1626 TFs in DepMap:ACH-000971 (HCT 116). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 97.3th, alt 92.0th percentile of its k-mer coefficients.

<a id="e35"></a>**E35** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=rs73706717%20POU5F1B%20colorectal%20cancer%20enhancer%20regulatory%20variant&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T13:39:58+00:00)

> Europe PMC: 0 hits for 'rs73706717 POU5F1B colorectal cancer enhancer regulatory variant'; top 0 with PMIDs:

<a id="e36"></a>**E36** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=rs73706717%20MYC%20colorectal%20cancer%20enhancer%20regulatory%20variant&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T13:39:59+00:00)

> Europe PMC: 1 hits for 'rs73706717 MYC colorectal cancer enhancer regulatory variant'; top 1 with PMIDs:
> PMID 22429595 (2012): Characterization of the colorectal cancer-associated enhancer MYC-335 at 8q24: the role of rs67491583.

<a id="e36a"></a>**E36a** literature_search, Europe PMC abstract, PMID 22429595 (https://europepmc.org/article/MED/22429595; retrieved 2026-10-26T13:39:59+00:00)

> In our previous work, we showed that the colorectal cancer (CRC) risk variant rs6983267 at 8q24 resides within a TCF4 binding site at the MYC-335 enhancer, with the risk allele G having a stronger binding capacity and Wnt responsiveness.

<a id="e36b"></a>**E36b** literature_search, Europe PMC abstract, PMID 22429595 (https://europepmc.org/article/MED/22429595; retrieved 2026-10-26T13:39:59+00:00)

> In this study, rs67491583 was identified as another functional variant in the CRC-associated enhancer MYC-335, but further studies are needed to establish the role of rs67491583 in the colorectal cancer predisposition of African Americans.

<a id="e37"></a>**E37** gene_disease, Open Targets Platform (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-26T02:23:32+00:00)

> Open Targets: POU5F1B and colorectal cancer (MONDO_0005575), overall score 0.54; by evidence type: genetic_association 0.87, literature 0.18, rna_expression 0.14
