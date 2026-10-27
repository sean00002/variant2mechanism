# TERT promoter C228T and Glioblastoma, melanoma, bladder

Configuration `no_qbic`, named mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.04 over 9 model calls; 142 s.

Variant `chr5:1295113:G>A` (somatic); expression context: DepMap:subtype=Glioblastoma (median of 54 lines).

## Ranked chains

### 1. H1_GABPA_activating: GABPA binds the alt allele and activates TERT (p = 0.50)

TF GABPA (QBiC-SELEX coverage own_model), alt allele binds more; element TERT promoter; gene TERT; cell type Glioblastoma.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | GABPA is proposed to bind the alt A allele more strongly because TERT promoter mutations create a de novo ETS motif (E16a) and the GABP tetramer is reported to be responsible for promoter activation across recurrent TERTp mutations (E16b); GABPB1, the GABP co-factor, is also detected at the variant-containing element in ENCODE (E04). GABPA is chosen over other ETS factors because E16b specifically implicates the GABP tetramer. No QBiC-SELEX model/evidence is provided for GABPA, and ENCODE GABPA peaks containing the variant are only in non-glioblastoma biosamples (E17), so allele-specific GABPA occupancy at this base in glioblastoma is not directly shown. | weak | [E04](#e04), [E16a](#e16a), [E16b](#e16b), [E17](#e17) |
| element | The variant lies within cCRE EH38E3622530, a promoter-like (PLS) element with DNase, H3K27ac and H3K4me3 signal upstream of TERT (E01, E03). | supported | [E01](#e01), [E03](#e03) |
| gene | The element is annotated as the TERT promoter, and TERT is the nearest protein-coding gene, 0 kb from its TSS (E01, E02, E03). | supported | [E01](#e01), [E02](#e02), [E03](#e03) |
| cell_type | In the glioblastoma DepMap expression context, GABPA is expressed (15.52 TPM, rank 303/1626) (E11), and GABPB1 is detected at the variant-containing element in ENCODE (E04), but no glioblastoma GABPA ChIP peak contains the variant (E17). Thus glioblastoma occupancy is inferred from expression plus literature, not directly demonstrated. | weak | [E04](#e04), [E11](#e11), [E17](#e17) |
| phenotype | GABP-dependent activation of mutant TERT promoter is reported (E16b), and TERT/telomerase is associated with glioblastoma, melanoma and bladder cancer in the literature (E15); however, TERT is not commonly essential in CNS lines by DepMap CRISPR (E18), so a direct proliferation/survival phenotype in glioblastoma is plausible but not established. | weak | [E15](#e15), [E16b](#e16b), [E18](#e18) |

Predictions: Allele-specific GABPA ChIP-qPCR or GABPA EMSA in glioblastoma cells shows alt > ref binding at chr5:1295113.; The alt allele increases TERT reporter activity and TERT mRNA in disease-relevant cells.; GABPA/GABPB1 knockdown or ETS-motif mutation reduces the alt-allele-specific TERT effect.

Falsified if: Allele-specific GABPA occupancy at chr5:1295113 is not detectable in glioblastoma cells.; The alt allele does not increase TERT reporter activity or endogenous TERT expression in disease-relevant cells.; GABPA/GABPB1 knockdown or ETS-motif mutation does not reduce the alt-allele-specific TERT effect.

### 2. H4_null_no_TF_effect: No TF-mediated allelic effect at this base (p = 0.35)

Null chain: no TF-mediated effect of this variant.

Predictions: Allele-specific reporter or EMSA assays in glioblastoma cells show no alt-versus-ref difference at this base.; TERT expression associates with a linked causal variant or another promoter alteration rather than this base.; No disease-cell TF occupancy difference is found at chr5:1295113.

Falsified if: Allele-specific GABPA or other TF occupancy is demonstrated in disease-relevant cells.; The alt allele increases TERT reporter activity in a TF-binding-site-dependent manner.; Knockdown or editing of the candidate TF reduces the alt-allele-specific TERT effect.

### 3. H2_JUN_alternative: JUN binds the alt allele and activates TERT (p = 0.10)

TF JUN (QBiC-SELEX coverage own_model), alt allele binds more; element TERT promoter; gene TERT; cell type Glioblastoma.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | JUN is an alternative AP-1 factor proposed to bind the alt A allele more strongly at this promoter. No QBiC-SELEX model/evidence is provided for JUN, and ENCODE JUN peaks containing the variant are only in other biosamples such as A549 (E06); E04 also states that no ENCODE biosample matches the glioblastoma expression context, so glioblastoma JUN occupancy at the variant is not directly shown. | weak | [E04](#e04), [E06](#e06) |
| element | The variant lies within cCRE EH38E3622530, a promoter-like (PLS) element with DNase, H3K27ac and H3K4me3 signal upstream of TERT (E01, E03). | supported | [E01](#e01), [E03](#e03) |
| gene | The element is annotated as the TERT promoter, and TERT is the nearest protein-coding gene, 0 kb from its TSS (E01, E02, E03). | supported | [E01](#e01), [E02](#e02), [E03](#e03) |
| cell_type | JUN is highly expressed in glioblastoma (91.65 TPM, rank 16/1626) (E06), but ENCODE JUN peaks at the variant are only from other biosamples, not glioblastoma (E04, E06). | weak | [E04](#e04), [E06](#e06) |
| phenotype | If JUN occupied the alt allele, it could increase TERT expression, but the literature evidence is only general TERT/telomerase association with these cancers (E15), and TERT is not commonly essential in CNS lines by DepMap CRISPR (E18); no JUN-specific allele-dependent TERT phenotype is shown. | weak | [E15](#e15), [E18](#e18) |

Predictions: JUN ChIP-qPCR or EMSA in glioblastoma cells shows alt > ref binding at chr5:1295113.; JUN knockdown reduces TERT expression or TERT reporter activity from the alt allele.; GABPA/GABPB1 knockdown or ETS-site mutation does not abolish the alt-allele-specific TERT effect, whereas JUN perturbation does.

Falsified if: JUN does not occupy the variant-containing element in glioblastoma cells.; JUN binding is not allele-specific for alt over ref.; JUN knockdown does not change TERT expression or the alt-allele reporter effect.

### 4. H3_EGR1_alternative: EGR1 binds the alt allele and activates TERT (p = 0.05)

TF EGR1 (QBiC-SELEX coverage own_model), alt allele binds more; element TERT promoter; gene TERT; cell type Glioblastoma.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | EGR1 is an alternative zinc-finger factor proposed to bind the alt A allele more strongly at this GC-rich promoter. No QBiC-SELEX model/evidence is provided for EGR1, and ENCODE EGR1 peaks containing the variant are only in HepG2, Ishikawa and K562, not glioblastoma (E07); E04 states that no ENCODE biosample matches the expression context, so glioblastoma EGR1 occupancy is not directly shown. | weak | [E04](#e04), [E07](#e07) |
| element | The variant lies within cCRE EH38E3622530, a promoter-like (PLS) element with DNase, H3K27ac and H3K4me3 signal upstream of TERT (E01, E03). | supported | [E01](#e01), [E03](#e03) |
| gene | The element is annotated as the TERT promoter, and TERT is the nearest protein-coding gene, 0 kb from its TSS (E01, E02, E03). | supported | [E01](#e01), [E02](#e02), [E03](#e03) |
| cell_type | EGR1 is expressed in glioblastoma (28.32 TPM, rank 151/1626) (E07), but ENCODE EGR1 peaks at the variant are only from other biosamples, not glioblastoma (E04, E07). | weak | [E04](#e04), [E07](#e07) |
| phenotype | If EGR1 occupied the alt allele, it could increase TERT expression, but the literature evidence is only general TERT/telomerase association with these cancers (E15), and TERT is not commonly essential in CNS lines by DepMap CRISPR (E18); no EGR1-specific allele-dependent TERT phenotype is shown. | weak | [E15](#e15), [E18](#e18) |

Predictions: EGR1 ChIP-qPCR or EMSA in glioblastoma cells shows alt > ref binding at chr5:1295113.; EGR1 knockdown reduces TERT expression or TERT reporter activity from the alt allele.; The alt-allele effect is EGR1-site dependent and separable from GABPA/ETS dependence.

Falsified if: EGR1 does not occupy the variant-containing element in glioblastoma cells.; EGR1 binding is not allele-specific for alt over ref.; EGR1 perturbation does not alter TERT expression or reporter activity.

## Prediction matrix

| Test | Cost | Separates top two | H1_GABPA_activating | H4_null_no_TF_effect | H2_JUN_alternative | H3_EGR1_alternative |
| --- | --- | --- | --- | --- | --- | --- |
| Ref-vs-alt TERT promoter luciferase reporter in a glioblastoma cell line | low | yes | alt increases TERT reporter activity | no alt-vs-ref reporter difference | alt increases TERT reporter activity via JUN if H2 is true | alt increases TERT reporter activity via EGR1 if H3 is true |
| GABPA EMSA with ref and alt oligos at chr5:1295113 | low | yes | alt > ref GABPA binding | no alt-vs-ref GABPA occupancy difference | no allele-specific GABPA binding required | no allele-specific GABPA binding required |
| CRISPR base editing of chr5:1295113 in disease-relevant cells with TERT readout | high | yes | editing alt to ref reduces GABPA-dependent TERT activity | no TERT effect; linked variant explains association | editing alt to ref reduces JUN-dependent TERT activity | editing alt to ref reduces EGR1-dependent TERT activity |
| GABPA/GABPB1 knockdown or ETS-site mutation in the ref-vs-alt TERT reporter assay | high | yes | GABPA/GABPB1 knockdown or ETS-motif mutation reduces alt-specific TERT activity | no alt-specific activity to reduce | GABPA/GABPB1 knockdown or ETS-motif mutation does not reduce alt-specific TERT activity | GABPA/GABPB1 knockdown or ETS-motif mutation does not reduce alt-specific TERT activity |
| JUN ChIP-qPCR and JUN knockdown in glioblastoma cells | high | no | no required allele-specific JUN effect | no alt-vs-ref JUN occupancy or effect | alt > ref JUN binding and JUN knockdown reduces alt-specific TERT activity | no required allele-specific JUN effect |
| EGR1 ChIP-qPCR and EGR1 knockdown in glioblastoma cells | high | no | no required allele-specific EGR1 effect | no alt-vs-ref EGR1 occupancy or effect | no required allele-specific EGR1 effect | alt > ref EGR1 binding and EGR1 knockdown reduces alt-specific TERT activity |

## Next experiment

The single cheapest experiment separating the top two chains (H1_GABPA_activating and H4_null_no_TF_effect) is a ref-vs-alt TERT promoter luciferase reporter assay in a glioblastoma cell line. H1 predicts the alt allele increases reporter activity; the null predicts no alt-vs-ref difference. It does not by itself prove GABPA, so a positive result should be followed by GABPA/GABPB1 knockdown or ETS-motif mutation, but it is the lowest-cost discriminator between the top two chains.

## Investigate calls

- literature_search({"query": "GABPA TERT promoter mutation ETS binding site allele-specific"})
- chip_peaks({"biosample": "glioblastoma", "tf": "GABPA"})
- gene_dependency({"gene": "TERT"})

## Flags

- quote_rejected: PMID 41744838: not an exact substring of the abstract

Citation support: 1.00 of links cite only evidence that passed every check.

## Evidence

<a id="e01"></a>**E01** variant_annotation, Ensembl VEP (GRCh38) (https://rest.ensembl.org/vep/human/region/5:1295113-1295113:1/A?content-type=application/json&Conservation=1; retrieved 2026-10-25T11:57:36+00:00)

> Variant chr5:1295113:G>A (GRCh38), allele string G/A
> Known IDs: rs1242535815
> Most severe consequence: upstream_gene_variant
> Regulatory features: ENSR5_832QG promoter
> GERP conservation score at the site: -7.45
> Transcript consequences: TERT (upstream_gene_variant)

<a id="e02"></a>**E02** nearest_genes, Ensembl overlap (protein_coding) (https://rest.ensembl.org/overlap/region/human/5:295113-2295113?feature=gene;biotype=protein_coding;content-type=application/json; retrieved 2026-10-25T11:57:33+00:00)

> 23 protein-coding genes within 1000 kb of chr5:1295113:G>A, by distance to TSS:
> TERT: 0.0 kb from TSS (upstream, strand -1)
> CLPTM1L: 50.0 kb from TSS (downstream, strand -1)
> SLC6A18: 69.7 kb from TSS (downstream, strand +1)
> SLC6A19: 93.5 kb from TSS (downstream, strand +1)
> SLC12A7: 138.9 kb from TSS (upstream, strand -1)
> SLC6A3: 150.4 kb from TSS (downstream, strand -1)
> LPCAT1: 229.2 kb from TSS (downstream, strand -1)
> NKD2: 287.1 kb from TSS (downstream, strand +1)
> TRIP13: 402.3 kb from TSS (downstream, strand +1)
> BRD9: 402.3 kb from TSS (upstream, strand -1)

<a id="e03"></a>**E03** ccre_lookup, ENCODE v4 cCRE registry (ENCFF420VPZ) and SCREEN (https://screen-beta-api.wenglab.org/dataws/cre_table; retrieved 2026-10-25T11:57:31+00:00)

> The variant lies in cCRE EH38E3622530 (PLS: promoter-like), chr5:1294945-1295294.
> SCREEN: 3 cCREs within 500 bp (max z-score across ENCODE biosamples):
> EH38E3622530 PLS (contains the variant): DNase z 4.8, H3K27ac z 4.2, H3K4me3 z 4.5, CTCF z 2.0; nearby genes TERT, MIR4457, CLPTM1L
> EH38E3622531 pELS: DNase z 3.9, H3K27ac z 4.3, H3K4me3 z 4.4, CTCF z 2.8; nearby genes TERT, MIR4457, CLPTM1L
> EH38E3622529 pELS: DNase z 3.7, H3K27ac z 4.1, H3K4me3 z 4.6, CTCF z 2.0; nearby genes TERT, MIR4457, CLPTM1L
> Biosample-specific z-scores are not in this call; the values above are maxima over biosamples.

<a id="e04"></a>**E04** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> ENCODE TF ChIP-seq at chr5:1295113:G>A: 121 peaks contain the variant, from 54 factors in 21 biosamples. No ENCODE biosample matches the expression context, so no peak counts as bound here. cCRE class at the variant: PLS. Bound factors outside the TF model collection (co-factors, Pol II, and TFs with no binding model; signs of an active element, not TF candidates): ARID4A, BCL3, DMAP1, EZH2, EZH2phosphoT487, GABPB1, HDAC1, HDAC2, HDAC6, HNRNPK, IKZF1, KDM4A (+21 more). Bound, expressed TFs with a binding model: 20; listed one per row: MAX, JUN, EGR1, BHLHE40, E2F4, E2F6, GABPA, ZNF687, CTCF, NR2C1; also bound: ZNF143, SP2, TGIF2, MNT, ZBTB7A, E2F5, ZBTB26, KLF12, ZNF48, ZIC2. Bound but below 1 TPM: ZFHX2. Assayed with no peak here: 0 TFs in the matching biosample, 552 only elsewhere; never assayed: 536.

<a id="e05"></a>**E05** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> MAX: bound elsewhere. 13 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: A549, HCT116, HepG2, Ishikawa, K562, MCF-7 (+2 more) (e.g. ENCSR000BLP). 58.6 TPM in DepMap:subtype=Glioblastoma (median of 54 lines), rank 48 of 1626 TFs.

<a id="e06"></a>**E06** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> JUN: bound elsewhere. 11 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: A549 (e.g. ENCSR022WVP). 91.65 TPM in DepMap:subtype=Glioblastoma (median of 54 lines), rank 16 of 1626 TFs.

<a id="e07"></a>**E07** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> EGR1: bound elsewhere. 3 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: HepG2, Ishikawa, K562 (e.g. ENCSR000BNE). 28.32 TPM in DepMap:subtype=Glioblastoma (median of 54 lines), rank 151 of 1626 TFs.

<a id="e08"></a>**E08** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> BHLHE40: bound elsewhere. 2 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: GM12878 (e.g. ENCSR000DZJ). 68.33 TPM in DepMap:subtype=Glioblastoma (median of 54 lines), rank 33 of 1626 TFs.

<a id="e09"></a>**E09** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> E2F4: bound elsewhere. 2 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: GM12878, HepG2 (e.g. ENCSR000DYY). 58.31 TPM in DepMap:subtype=Glioblastoma (median of 54 lines), rank 49 of 1626 TFs.

<a id="e10"></a>**E10** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> E2F6: bound elsewhere. 2 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: A549, K562 (e.g. ENCSR000BLI). 17.63 TPM in DepMap:subtype=Glioblastoma (median of 54 lines), rank 267 of 1626 TFs.

<a id="e11"></a>**E11** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> GABPA: bound elsewhere. 2 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: HepG2, SK-N-SH (e.g. ENCSR000BJK). 15.52 TPM in DepMap:subtype=Glioblastoma (median of 54 lines), rank 303 of 1626 TFs.

<a id="e12"></a>**E12** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> ZNF687: bound elsewhere. 2 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: HepG2 (e.g. ENCSR647PSR). 10.74 TPM in DepMap:subtype=Glioblastoma (median of 54 lines), rank 436 of 1626 TFs.

<a id="e13"></a>**E13** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> CTCF: bound elsewhere. 1 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: DOHH2 (e.g. ENCSR084RDK). 26.45 TPM in DepMap:subtype=Glioblastoma (median of 54 lines), rank 163 of 1626 TFs.

<a id="e14"></a>**E14** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> NR2C1: bound elsewhere. 1 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: GM12878 (e.g. ENCSR784VIQ). 18.52 TPM in DepMap:subtype=Glioblastoma (median of 54 lines), rank 251 of 1626 TFs.

<a id="e15"></a>**E15** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TERT%20AND%20%28%22glioblastoma%22%20OR%20%22melanoma%22%20OR%20%22bladder%22%29&format=json&pageSize=8&resultType=core; retrieved 2026-10-25T11:57:36+00:00)

> Europe PMC: 23888 hits for 'TERT AND ("glioblastoma" OR "melanoma" OR "bladder")'; top 7 with PMIDs:
> PMID 41744838 (2026): Telomerase Activity in Melanoma: Impact on Cancer Cell Proliferation Kinetics, Tumor Progression, and Clinical Therapeutic Strategies-A Scoping Review.
> PMID 42577103 (2026): Familial melanoma: genetic, clinical, and dermoscopic insights and follow-up.
> PMID 42722679 (2026): Developing neoantigen cancer vaccines: where are we now?
> PMID 42741698 (2026): Melanoma of unknown primary with solitary lesions to the prostate and lung uncovered after simple prostatectomy.
> PMID 42804732 (2026): SNP rs2853669 potentially elevates the risk of glioblastoma development and leads to worse prognosis when in cis with mutant TERT promoter in a Japanese cohort.
> PMID 42807929 (2026): USP10 stabilizes FOXM1 through KAT5-mediated acetylation to suppress cell senescence and promote melanoma malignant progression.
> PMID 42859331 (2026): CDKN2A deletion associated with poor prognosis in patients with TERT promoter wild-type, IDH wild-type glioblastoma.

<a id="e16"></a>**E16** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=GABPA%20TERT%20promoter%20mutation%20ETS%20binding%20site%20allele-specific&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T02:23:58+00:00)

> Europe PMC: 88 hits for 'GABPA TERT promoter mutation ETS binding site allele-specific'; top 8 with PMIDs:
> PMID 40513567 (2025): The immortality mechanism of TERT promoter mutant cancers is self-reinforcing and reversible.
> PMID 40822359 (2025): AURKB and PI3K/AKT/mTOR pathways converge to regulate &lt;i&gt;TERT&lt;/i&gt; expression.
> PMID 39557834 (2024): Mechanistic basis of atypical TERT promoter mutations.
> PMID 37918959 (2023): E4F1 and ZNF148 are transcriptional activators of the -57A &gt; C and wild-type &lt;i&gt;TERT&lt;/i&gt; promoter.
> PMID 41639451 (2026): Regulatory grammar in human promoters uncovered by MPRA-based deep learning.
> PMID 38033865 (2023): Reactivation of telomerase reverse transcriptase expression in cancer: the role of TERT promoter mutations.
> PMID 40359938 (2025): Reannotation of cancer mutations based on expressed RNA transcripts reveals functional non-coding mutations in melanoma.
> PMID 40241101 (2025): The ability of anexelekto (AXL) expression and TERT promoter mutation to predict radioiodine-refractory differentiated thyroid carcinoma.

<a id="e16a"></a>**E16a** literature_search, Europe PMC abstract, PMID 40513567 (https://europepmc.org/article/MED/40513567; retrieved 2026-10-26T02:23:58+00:00)

> TERT promoter (TERTp) mutations create a de novo E26 transformation-specific (ETS) transcription factor binding motif.

<a id="e16b"></a>**E16b** literature_search, Europe PMC abstract, PMID 40513567 (https://europepmc.org/article/MED/40513567; retrieved 2026-10-26T02:23:58+00:00)

> Here, we analyzed 53 cell lines representing 16 cancer types and 6 recurrent TERTp mutations and found that the GA-binding protein (GABP) tetramer is responsible for promoter activation in all cases.

<a id="e17"></a>**E17** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-25T11:58:44+00:00)

> No ENCODE GABPA ChIP-seq peak contains chr5:1295113:G>A in biosamples matching 'glioblastoma'. Absence can also mean no GABPA experiment in that biosample. In other biosamples, 2 GABPA peaks do contain the variant: HepG2, SK-N-SH (experiments ENCSR000BJK, ENCSR000BTG).

<a id="e18"></a>**E18** gene_dependency, DepMap CRISPRGeneEffect (Biomni copy) and CRISPRInferredCommonEssentials (Public 26Q3) (local files; retrieved local)

> DepMap CRISPR gene effect for TERT (0 = no effect, -1 = median common-essential; < -0.5 called dependent). CNS/Brain lineage, 50 lines: median -0.00, 2% dependent. All 1183 lines: median -0.02, 1% dependent.
