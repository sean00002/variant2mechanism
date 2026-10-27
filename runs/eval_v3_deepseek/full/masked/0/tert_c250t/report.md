# TERT promoter C250T and Glioblastoma, melanoma, bladder

Configuration `full`, masked mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.02 over 9 model calls; 153 s.

Variant `chr5:1295135:G>A` (somatic); expression context: DepMap:subtype=Glioblastoma (median of 54 lines).

## QBiC-SELEX screen (occupancy first)

Occupied candidates: GABPA (bound elsewhere, z 167.5); KLF12 (bound elsewhere, z -15.38); NR2C1 (bound elsewhere, z 15.31); TGIF2 (bound elsewhere, z -12.19); ZNF143 (bound elsewhere, z -11.71); ZBTB7A (bound elsewhere, z -10.91); SP2 (bound elsewhere, z -9.83); EGR1 (bound elsewhere, z -8.0); BHLHE40 (bound elsewhere, z -7.34); E2F4 (bound elsewhere, z -5.4). Occupancy unknown: ETV2 (z 167.5); ETV3 (z 167.5); FLI1 (z 167.5); ZNF92 (z -33.21); EBF4 (z -24.35). Diagnostic, not shown to the model: 477 of 997 models pass Bonferroni.

## Ranked chains

### 1. H0: Null: no TF-mediated allelic effect at this base (p = 0.49)

Null chain: no TF-mediated effect of this variant.

Predictions: No allele-specific TF binding or activity at chr5:1295135:G>A after controlling for linked variants.; Any TERT association is explained by a nearby causal variant or by passenger mutation status rather than this base.

Falsified if: Allele-specific TF ChIP or reporter assays demonstrate a reproducible allelic effect at this exact base in a relevant cell type.; A linked causal variant is excluded and the single-base change itself alters TERT promoter activity.

### 2. H1: GABPA gain-of-binding at the TERT promoter (p = 0.26)

TF GABPA (QBiC-SELEX coverage own_model), alt allele binds more; element Active promoter-like cCRE; gene TERT; cell type Glioblastoma, melanoma, and bladder cancer.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The alt A allele is predicted to bind GABPA more strongly than ref G. This is supported by the GABPA own QBiC-SELEX model (alt effect +4.05, z 71.32; alt site 99.8th vs ref 96.3rd percentile), and by Ets-family mapped models with the same direction. GABPA ChIP peaks over this base only in HepG2/SK-N-SH, not in a glioblastoma-matching biosample, so occupancy in the disease context is not established. | weak | [E33](#e33), [E17](#e17), [E32](#e32), [E04](#e04) |
| element | The variant lies in a promoter-like cCRE, EH38E3622530, with DNase, H3K27ac, and H3K4me3 signals consistent with an active promoter element. | supported | [E03](#e03), [E01](#e01) |
| gene | TERT is the nearest gene, 0 kb from its TSS, and the variant is annotated as a TERT upstream gene variant. | supported | [E01](#e01), [E02](#e02) |
| cell_type | GABPA is expressed in DepMap glioblastoma context, and TERT is a disease-relevant gene across glioblastoma, melanoma, and bladder cancer, although the disease links are broad. | weak | [E17](#e17), [E15](#e15) |
| phenotype | If GABPA activates TERT at this promoter, the alt allele would increase TERT expression and promote tumor phenotypes. This activator role at TERT is not directly shown by the available evidence. | missing | [E33](#e33), [E15](#e15) |

Predictions: Allele-specific GABPA ChIP or reporter assays would show alt > ref activity at this base in a relevant cellular context.; GABPA depletion would reduce TERT expression when the alt allele is present.; The alt allele would increase TERT promoter activity in a GABPA-dependent manner.

Falsified if: Allele-specific GABPA ChIP in a relevant heterozygous disease-model cell line shows no alt > ref occupancy over this base.; A TERT promoter reporter with the G and A alleles shows no alt-specific increase in the relevant cellular context.; GABPA perturbation does not change TERT expression in an allele-dependent manner.

### 3. H2: ZNF143 loss-of-repressor binding at the TERT promoter (p = 0.10)

TF ZNF143 (QBiC-SELEX coverage own_model), ref allele binds more; element Active promoter-like cCRE; gene TERT; cell type Glioblastoma, melanoma, and bladder cancer.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The ref G allele is predicted to bind ZNF143 more strongly than alt A. QBiC-SELEX supports this (effect -0.649, z -11.71; ref site 100.0th vs alt 98.4th percentile), but ZNF143 has an ENCODE peak over this base only in GM12878, not in the disease context. | weak | [E21](#e21), [E04](#e04) |
| element | The variant lies in a promoter-like active cCRE, making allele-specific repressor loss at a promoter plausible. | supported | [E03](#e03), [E01](#e01) |
| gene | TERT is the nearest gene and is annotated as the affected upstream gene. | supported | [E01](#e01), [E02](#e02) |
| cell_type | ZNF143 is expressed in DepMap glioblastoma context, and TERT is broadly relevant to the listed cancers. | weak | [E21](#e21), [E15](#e15) |
| phenotype | If ZNF143 represses TERT at this promoter, loss of ZNF143 binding on the alt allele would derepress TERT and promote disease. The available ZNF143/TERT literature search did not directly establish this repressor role. | missing | [E34](#e34), [E21](#e21), [E15](#e15) |

Predictions: Allele-specific ZNF143 ChIP would show ref > alt occupancy at this base in relevant cells.; The alt allele would increase TERT reporter activity if ZNF143 is a repressor.; ZNF143 knockdown or overexpression would modulate TERT in the predicted repressive direction.

Falsified if: Allele-specific ZNF143 ChIP in a relevant background shows no ref > alt occupancy at this base.; The alt allele does not reduce ZNF143-dependent repression of a TERT reporter.; ZNF143 acts as an activator rather than a repressor of TERT in the relevant context.

### 4. H3: TGIF2 loss-of-repressor binding at the TERT promoter (p = 0.08)

TF TGIF2 (QBiC-SELEX coverage own_model), ref allele binds more; element Active promoter-like cCRE; gene TERT; cell type Glioblastoma, melanoma, and bladder cancer.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The ref G allele is predicted to bind TGIF2 more strongly than alt A. QBiC-SELEX supports this (effect -1.113, z -12.19; ref site 98.3rd vs alt 71.5th percentile), but TGIF2 has an ENCODE peak over this base only in HepG2, not in the disease context. | weak | [E20](#e20), [E04](#e04) |
| element | The variant is in an active promoter-like cCRE, so allele-specific loss of a repressor could affect promoter output. | supported | [E03](#e03), [E01](#e01) |
| gene | TERT is the nearest gene and the variant is upstream of TERT. | supported | [E01](#e01), [E02](#e02) |
| cell_type | TGIF2 is expressed in glioblastoma DepMap data, and TERT is broadly relevant to the listed cancers. | weak | [E20](#e20), [E15](#e15) |
| phenotype | If TGIF2 represses TERT, the alt allele would reduce TGIF2 binding and increase TERT expression. No direct evidence shows TGIF2 represses TERT. | missing | [E20](#e20), [E15](#e15) |

Predictions: TGIF2 ChIP would show ref > alt at this base in a relevant cell type.; The alt allele would increase TERT reporter activity when TGIF2 is present.; TGIF2 perturbation would change TERT expression in the direction predicted for a repressor.

Falsified if: TGIF2 occupancy at this base is not allele-specific in relevant cells.; The alt allele does not relieve TGIF2-dependent repression of TERT.; TGIF2 does not bind or regulate TERT in the relevant cellular context.

### 5. H4: NR2C1 gain-of-activator binding at the TERT promoter (p = 0.07)

TF NR2C1 (QBiC-SELEX coverage own_model), alt allele binds more; element Active promoter-like cCRE; gene TERT; cell type Glioblastoma, melanoma, and bladder cancer.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The alt A allele is predicted to bind NR2C1 more strongly than ref G. QBiC-SELEX supports this (effect +1.182, z 15.31; alt site 99.2nd vs ref 98.3rd percentile), but NR2C1 has an ENCODE peak over this base only in GM12878, not in the disease context. | weak | [E19](#e19), [E04](#e04) |
| element | This base lies in a promoter-like cCRE with active chromatin marks, consistent with a regulatory element that could respond to NR2C1. | supported | [E03](#e03), [E01](#e01) |
| gene | TERT is the nearest gene, 0 kb from the TSS, and is annotated as upstream of TERT. | supported | [E01](#e01), [E02](#e02) |
| cell_type | NR2C1 is expressed in glioblastoma DepMap data, and TERT is broadly relevant to glioblastoma, melanoma, and bladder cancer. | weak | [E19](#e19), [E15](#e15) |
| phenotype | If NR2C1 activates TERT at this promoter, the alt allele would increase TERT expression. No direct evidence shows NR2C1 activates TERT. | missing | [E19](#e19), [E15](#e15) |

Predictions: Allele-specific NR2C1 ChIP would show alt > ref occupancy at this base.; The alt allele would increase TERT reporter activity in an NR2C1-dependent manner.; NR2C1 knockdown would reduce TERT expression in a relevant cellular model.

Falsified if: NR2C1 ChIP-seq in a relevant background shows no allele-specific occupancy at this base.; NR2C1 does not activate TERT in reporter assays.; The alt allele does not increase NR2C1-dependent TERT expression.

## Prediction matrix

| Test | Cost | Separates top two | H0 | H1 | H2 | H3 | H4 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Allele-specific GABPA ChIP-qPCR in a heterozygous glioblastoma cell line at chr5:1295135 | medium | yes | no allele-specific GABPA occupancy | alt > ref GABPA occupancy at the variant | no GABPA allele-specific occupancy | no GABPA allele-specific occupancy | no GABPA allele-specific occupancy |
| Dual-allele TERT promoter luciferase reporter in glioblastoma cells, with and without GABPA perturbation | low | yes | ref = alt reporter activity | alt > ref TERT reporter activity, reduced by GABPA loss | alt > ref only if ZNF143 represses TERT; not GABPA-dependent | alt > ref only if TGIF2 represses TERT; not GABPA-dependent | alt > ref only if NR2C1 activates TERT; not GABPA-dependent |
| GABPA CRISPRi or knockdown in a heterozygous glioblastoma line followed by allele-specific TERT expression | high | yes | no allelic change in TERT expression | GABPA loss reduces TERT expression preferentially from the alt allele | no GABPA-dependent allelic change in TERT expression | no GABPA-dependent allelic change in TERT expression | no GABPA-dependent allelic change in TERT expression |
| Allele-specific ZNF143 ChIP-qPCR in a relevant heterozygous cell line | medium | no | no allele-specific ZNF143 occupancy | no ZNF143 allele-specific occupancy | ref > alt ZNF143 occupancy at the variant | no ZNF143 allele-specific occupancy | no ZNF143 allele-specific occupancy |
| Allele-specific TGIF2 ChIP-qPCR in a relevant heterozygous cell line | medium | no | no allele-specific TGIF2 occupancy | no TGIF2 allele-specific occupancy | no TGIF2 allele-specific occupancy | ref > alt TGIF2 occupancy at the variant | no TGIF2 allele-specific occupancy |
| Allele-specific NR2C1 ChIP-qPCR in a relevant heterozygous cell line | medium | no | no allele-specific NR2C1 occupancy | no NR2C1 allele-specific occupancy | no NR2C1 allele-specific occupancy | no NR2C1 allele-specific occupancy | alt > ref NR2C1 occupancy at the variant |

## Next experiment

Dual-allele TERT promoter luciferase reporter assay in a glioblastoma cell line, comparing ref G and alt A at chr5:1295135, with a secondary GABPA perturbation arm. This is the cheapest test that separates the top two chains H1 and H0: H1 predicts alt-specific activity, whereas H0 predicts no allelic difference. If positive, follow with allele-specific GABPA ChIP to establish TF specificity.

## Investigate calls

- chip_peaks({"tf": "GABPA", "biosample": "glioblastoma"})
- qbic_tf_detail({"tf": "GABPA"})
- literature_search({"query": "ZNF143 TERT promoter repression"})

## Flags

- quote_rejected: PMID 41744838: not an exact substring of the abstract

Citation support: 1.00 of links cite only evidence that passed every check.

## Evidence

<a id="e01"></a>**E01** variant_annotation, Ensembl VEP (GRCh38) (https://rest.ensembl.org/vep/human/region/5:1295135-1295135:1/A?content-type=application/json&Conservation=1; retrieved 2026-10-25T17:26:00+00:00)

> Variant chr5:1295135:G>A (GRCh38), allele string G/A
> Known IDs: rs1561215364
> Most severe consequence: upstream_gene_variant
> Regulatory features: ENSR5_832QG promoter
> GERP conservation score at the site: -4.69
> Transcript consequences: TERT (upstream_gene_variant)

<a id="e02"></a>**E02** nearest_genes, Ensembl overlap (protein_coding) (https://rest.ensembl.org/overlap/region/human/5:295135-2295135?feature=gene;biotype=protein_coding;content-type=application/json; retrieved 2026-10-25T17:25:54+00:00)

> 23 protein-coding genes within 1000 kb of chr5:1295135:G>A, by distance to TSS:
> TERT: 0.0 kb from TSS (upstream, strand -1)
> CLPTM1L: 50.0 kb from TSS (downstream, strand -1)
> SLC6A18: 69.8 kb from TSS (downstream, strand +1)
> SLC6A19: 93.5 kb from TSS (downstream, strand +1)
> SLC12A7: 138.9 kb from TSS (upstream, strand -1)
> SLC6A3: 150.4 kb from TSS (downstream, strand -1)
> LPCAT1: 229.1 kb from TSS (downstream, strand -1)
> NKD2: 287.1 kb from TSS (downstream, strand +1)
> TRIP13: 402.3 kb from TSS (downstream, strand +1)
> BRD9: 402.3 kb from TSS (upstream, strand -1)

<a id="e03"></a>**E03** ccre_lookup, ENCODE v4 cCRE registry (ENCFF420VPZ) and SCREEN (https://screen-beta-api.wenglab.org/dataws/cre_table; retrieved 2026-10-25T17:25:50+00:00)

> The variant lies in cCRE EH38E3622530 (PLS: promoter-like), chr5:1294945-1295294.
> SCREEN: 3 cCREs within 500 bp (max z-score across ENCODE biosamples):
> EH38E3622530 PLS (contains the variant): DNase z 4.8, H3K27ac z 4.2, H3K4me3 z 4.5, CTCF z 2.0; nearby genes TERT, MIR4457, CLPTM1L
> EH38E3622531 pELS: DNase z 3.9, H3K27ac z 4.3, H3K4me3 z 4.4, CTCF z 2.8; nearby genes TERT, MIR4457, CLPTM1L
> EH38E3622529 pELS: DNase z 3.7, H3K27ac z 4.1, H3K4me3 z 4.6, CTCF z 2.0; nearby genes TERT, MIR4457, CLPTM1L
> Biosample-specific z-scores are not in this call; the values above are maxima over biosamples.

<a id="e04"></a>**E04** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> ENCODE TF ChIP-seq at chr5:1295135:G>A: 113 peaks contain the variant, from 47 factors in 22 biosamples. No ENCODE biosample matches the expression context, so no peak counts as bound here. cCRE class at the variant: PLS. Bound factors outside the TF model collection (co-factors, Pol II, and TFs with no binding model; signs of an active element, not TF candidates): ARID4A, BCL3, DMAP1, EZH2, EZH2phosphoT487, GABPB1, HDAC1, HNRNPK, IKZF1, KDM4A, LIN54, MAZ (+16 more). Bound, expressed TFs with a binding model: 18; listed one per row: MAX, JUN, BHLHE40, E2F4, EGR1, CTCF, GABPA, ZNF687, NR2C1, ZNF143; also bound: SP2, TGIF2, MNT, ZBTB7A, E2F5, ZBTB26, KLF12, ZNF48. Bound but below 1 TPM: ZFHX2. Assayed with no peak here: 0 TFs in the matching biosample, 554 only elsewhere; never assayed: 536.

<a id="e05"></a>**E05** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> MAX: bound elsewhere. 12 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: A549, HCT116, HepG2, Ishikawa, K562, NB4 (+1 more) (e.g. ENCSR000BLP). 58.6 TPM in DepMap:subtype=Glioblastoma (median of 54 lines), rank 48 of 1626 TFs.

<a id="e06"></a>**E06** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> JUN: bound elsewhere. 11 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: A549 (e.g. ENCSR022WVP). 91.65 TPM in DepMap:subtype=Glioblastoma (median of 54 lines), rank 16 of 1626 TFs.

<a id="e07"></a>**E07** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> BHLHE40: bound elsewhere. 2 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: GM12878 (e.g. ENCSR000DZJ). 68.33 TPM in DepMap:subtype=Glioblastoma (median of 54 lines), rank 33 of 1626 TFs.

<a id="e08"></a>**E08** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> E2F4: bound elsewhere. 2 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: GM12878, HepG2 (e.g. ENCSR000DYY). 58.31 TPM in DepMap:subtype=Glioblastoma (median of 54 lines), rank 49 of 1626 TFs.

<a id="e09"></a>**E09** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> EGR1: bound elsewhere. 2 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: HepG2, Ishikawa (e.g. ENCSR000BSQ). 28.32 TPM in DepMap:subtype=Glioblastoma (median of 54 lines), rank 151 of 1626 TFs.

<a id="e10"></a>**E10** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> CTCF: bound elsewhere. 2 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: DOHH2, endodermal cell (e.g. ENCSR084RDK). 26.45 TPM in DepMap:subtype=Glioblastoma (median of 54 lines), rank 163 of 1626 TFs.

<a id="e11"></a>**E11** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> GABPA: bound elsewhere. 2 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: HepG2, SK-N-SH (e.g. ENCSR000BJK). 15.52 TPM in DepMap:subtype=Glioblastoma (median of 54 lines), rank 303 of 1626 TFs.

<a id="e12"></a>**E12** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> ZNF687: bound elsewhere. 2 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: HepG2 (e.g. ENCSR647PSR). 10.74 TPM in DepMap:subtype=Glioblastoma (median of 54 lines), rank 436 of 1626 TFs.

<a id="e13"></a>**E13** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> NR2C1: bound elsewhere. 1 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: GM12878 (e.g. ENCSR784VIQ). 18.52 TPM in DepMap:subtype=Glioblastoma (median of 54 lines), rank 251 of 1626 TFs.

<a id="e14"></a>**E14** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> ZNF143: bound elsewhere. 1 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: GM12878 (e.g. ENCSR936XTK). 15.92 TPM in DepMap:subtype=Glioblastoma (median of 54 lines), rank 297 of 1626 TFs.

<a id="e15"></a>**E15** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TERT%20AND%20%28%22glioblastoma%22%20OR%20%22melanoma%22%20OR%20%22bladder%22%29&format=json&pageSize=8&resultType=core; retrieved 2026-10-25T11:57:36+00:00)

> Europe PMC: 23888 hits for 'TERT AND ("glioblastoma" OR "melanoma" OR "bladder")'; top 7 with PMIDs:
> PMID 41744838 (2026): Telomerase Activity in Melanoma: Impact on Cancer Cell Proliferation Kinetics, Tumor Progression, and Clinical Therapeutic Strategies-A Scoping Review.
> PMID 42577103 (2026): Familial melanoma: genetic, clinical, and dermoscopic insights and follow-up.
> PMID 42722679 (2026): Developing neoantigen cancer vaccines: where are we now?
> PMID 42741698 (2026): Melanoma of unknown primary with solitary lesions to the prostate and lung uncovered after simple prostatectomy.
> PMID 42804732 (2026): SNP rs[masked] potentially elevates the risk of glioblastoma development and leads to worse prognosis when in cis with mutant TERT promoter in a Japanese cohort.
> PMID 42807929 (2026): USP10 stabilizes FOXM1 through KAT5-mediated acetylation to suppress cell senescence and promote melanoma malignant progression.
> PMID 42859331 (2026): CDKN2A deletion associated with poor prognosis in patients with TERT promoter wild-type, IDH wild-type glioblastoma.

<a id="e16"></a>**E16** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> QBiC-SELEX screen of chr5:1295135:G>A, one line per TF, each with the TF's own or CIS-BP-mapped model of largest |z|. Candidates are TFs whose ENCODE ChIP-seq peaks contain the variant and that are expressed (DepMap subtype median Glioblastoma), bound here before bound elsewhere, then a strong site before a weak one, then by |z|; then expressed TFs ENCODE never assayed whose best model passes the gate (occupancy unknown). Shown: 10 of 18 occupied (14 with a strong site), 5 of 145 with unknown occupancy. Left out: 0 TFs assayed in the matching biosample and 554 assayed only elsewhere, none with a peak here; 1 bound but below 1 TPM. The gate (|z| > 4.05, Bonferroni over 997 models) marks a change QBiC-SELEX detects; it says nothing about occupancy. Effect > 0 means the alternate allele binds more strongly. In vitro binding only. Site strength is the better allele's best k-mer over the variant, as a percentile of the best model's k-mers; a strong site reaches the 97.5th. At a weak site the ChIP peak more likely reflects another site in the element.

<a id="e17"></a>**E17** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> GABPA (Ets, 18 models; QBiC-SELEX coverage: own model): best model ETV5_NA_TGCACT20NGA_ESAF_yang2017_1_3_6mer (a CIS-BP-mapped model of ETV5), z 167.5, effect 2.421: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 15.52 TPM, rank 303 of 1626 TFs in DepMap:subtype=Glioblastoma (median of 54 lines). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in HepG2, SK-N-SH, e.g. ENCSR000BJK. Best model's site strength: ref 94.8th, alt 99.9th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e18"></a>**E18** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> KLF12 (C2H2 ZF, 6 models; QBiC-SELEX coverage: own model): best model KLF5_eDBD_TAACGC40NGTG_KS_yin2017_0_4_7mer (a CIS-BP-mapped model of KLF5), z -15.38, effect -0.439: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 4.47 TPM, rank 787 of 1626 TFs in DepMap:subtype=Glioblastoma (median of 54 lines). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in HepG2, e.g. ENCSR552YWL. Best model's site strength: ref 99.9th, alt 98.9th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e19"></a>**E19** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> NR2C1 (Nuclear receptor, 29 models; QBiC-SELEX coverage: own model): best model RORC_NA_Lib1_NA_bhimsaria2023_0(3)_3_7mer (a CIS-BP-mapped model of RORC), z 15.31, effect 1.182: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 18.52 TPM, rank 251 of 1626 TFs in DepMap:subtype=Glioblastoma (median of 54 lines). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in GM12878, e.g. ENCSR784VIQ. Best model's site strength: ref 98.3th, alt 99.2th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e20"></a>**E20** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> TGIF2 (Homeodomain, 9 models; QBiC-SELEX coverage: own model): best model PKNOX2_eDBD_TAACGT40NGAT_KAN_yin2017_0_4_7mer (a CIS-BP-mapped model of PKNOX2), z -12.19, effect -1.113: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 10.31 TPM, rank 452 of 1626 TFs in DepMap:subtype=Glioblastoma (median of 54 lines). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in HepG2, e.g. ENCSR993LMB. Best model's site strength: ref 98.3th, alt 71.5th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e21"></a>**E21** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> ZNF143 (C2H2 ZF, 2 models; QBiC-SELEX coverage: own model): best model ZNF143_NA_TGCAAG20NCG_V_jolma2013_0_3_7mer (its own model), z -11.71, effect -0.649: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 15.92 TPM, rank 297 of 1626 TFs in DepMap:subtype=Glioblastoma (median of 54 lines). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in GM12878, e.g. ENCSR936XTK. Best model's site strength: ref 100.0th, alt 98.4th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e22"></a>**E22** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> ZBTB7A (C2H2 ZF, 1 model; QBiC-SELEX coverage: own model): best model ZBTB7A_eDBD_TTTGCT40NCGT_KR_yin2017_0_4_7mer (its own model), z -10.91, effect -0.707: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 8.49 TPM, rank 531 of 1626 TFs in DepMap:subtype=Glioblastoma (median of 54 lines). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in K562, e.g. ENCSR000BME. Best model's site strength: ref 99.9th, alt 99.9th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e23"></a>**E23** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> SP2 (C2H2 ZF, 1 model; QBiC-SELEX coverage: own model): best model SP2_eDBD_TCATGT40NCTG_KV_yin2017_0_4_7mer (its own model), z -9.83, effect -0.269: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 15.49 TPM, rank 305 of 1626 TFs in DepMap:subtype=Glioblastoma (median of 54 lines). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in HepG2, e.g. ENCSR946RZN. Best model's site strength: ref 100.0th, alt 99.7th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e24"></a>**E24** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> EGR1 (C2H2 ZF, 4 models; QBiC-SELEX coverage: own model): best model EGR3_NA_TCATGC20NGTA_ESZ_yang2017_0_4_7mer (a CIS-BP-mapped model of EGR3), z -8.0, effect -0.422: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 28.32 TPM, rank 151 of 1626 TFs in DepMap:subtype=Glioblastoma (median of 54 lines). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in HepG2, Ishikawa, e.g. ENCSR000BSQ. Best model's site strength: ref 99.8th, alt 99.7th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e25"></a>**E25** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> BHLHE40 (bHLH, 2 models; QBiC-SELEX coverage: own model): best model BHLHE40_eDBD_TTAGTG40NACC_KR_yin2017_0_3_7mer (its own model), z -7.34, effect -0.318: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 68.33 TPM, rank 33 of 1626 TFs in DepMap:subtype=Glioblastoma (median of 54 lines). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in GM12878, e.g. ENCSR000DZJ. Best model's site strength: ref 99.6th, alt 93.6th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e26"></a>**E26** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> E2F4 (E2F, 4 models; QBiC-SELEX coverage: own model): best model E2F3_NA_TTACAT20NACA_ESAF_yang2017_0_4_7mer (a CIS-BP-mapped model of E2F3), z -5.4, effect -0.455: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 58.31 TPM, rank 49 of 1626 TFs in DepMap:subtype=Glioblastoma (median of 54 lines). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in GM12878, HepG2, e.g. ENCSR000DYY. Best model's site strength: ref 99.5th, alt 99.4th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e27"></a>**E27** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> ETV2 (Ets, 18 models; QBiC-SELEX coverage: own model): best model ETV5_NA_TGCACT20NGA_ESAF_yang2017_1_3_6mer (a CIS-BP-mapped model of ETV5), z 167.5, effect 2.421: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 1.4 TPM, rank 1063 of 1626 TFs in DepMap:subtype=Glioblastoma (median of 54 lines). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 94.8th, alt 99.9th percentile of its k-mer coefficients.

<a id="e28"></a>**E28** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> ETV3 (Ets, 18 models; QBiC-SELEX coverage: own model): best model ETV5_NA_TGCACT20NGA_ESAF_yang2017_1_3_6mer (a CIS-BP-mapped model of ETV5), z 167.5, effect 2.421: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 8.69 TPM, rank 521 of 1626 TFs in DepMap:subtype=Glioblastoma (median of 54 lines). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 94.8th, alt 99.9th percentile of its k-mer coefficients.

<a id="e29"></a>**E29** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> FLI1 (Ets, 18 models; QBiC-SELEX coverage: own model): best model ETV5_NA_TGCACT20NGA_ESAF_yang2017_1_3_6mer (a CIS-BP-mapped model of ETV5), z 167.5, effect 2.421: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 4.71 TPM, rank 767 of 1626 TFs in DepMap:subtype=Glioblastoma (median of 54 lines). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 94.8th, alt 99.9th percentile of its k-mer coefficients.

<a id="e30"></a>**E30** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> ZNF92 (C2H2 ZF, 1 model; QBiC-SELEX coverage: own model): best model ZNF92_FL_TC40NAATCTC_YWIA_jolma2025_0_3_7mer (its own model), z -33.21, effect -0.623: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 9.63 TPM, rank 481 of 1626 TFs in DepMap:subtype=Glioblastoma (median of 54 lines). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 100.0th, alt 99.7th percentile of its k-mer coefficients.

<a id="e31"></a>**E31** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> EBF4 (EBF1, 2 models; QBiC-SELEX coverage: own model): best model EBF1_NA_TATAAG20NCG_AC_jolma2013_1_3_7mer (a CIS-BP-mapped model of EBF1), z -24.35, effect -0.646: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 2.58 TPM, rank 952 of 1626 TFs in DepMap:subtype=Glioblastoma (median of 54 lines). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 99.9th, alt 99.7th percentile of its k-mer coefficients.

<a id="e32"></a>**E32** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-25T17:27:26+00:00)

> No ENCODE GABPA ChIP-seq peak contains chr5:1295135:G>A in biosamples matching 'glioblastoma'. Absence can also mean no GABPA experiment in that biosample. In other biosamples, 2 GABPA peaks do contain the variant: HepG2, SK-N-SH (experiments ENCSR000BJK, ENCSR000BTG).

<a id="e33"></a>**E33** qbic_tf_detail, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> {"tf":"GABPA","symbol":"GABPA","via":"hgnc_symbol","notes":[],"coverage":"own_model","variant":"chr5:1295135:G>A","gate_p":5.02e-05,"models":[{"model":"GABPA_FL_TC40NGCGATT_YWL_jolma2025_0_2_7mer","mapping":"own","group":"G003 Ets, 18 models","quality":0.658,"effect":4.05,"z":71.32,"p":0.0,"rank_abs_z":"7/997","passed_gate":true,"site_strength":{"ref_percentile":96.3,"alt_percentile":99.8,"k":7}},{"model":"ELF1_FL_TATGAC40NTCA_KW_yin2017_0_2_7mer","mapping":"CIS-BP (ELF1)","group":"G003 Ets, 18 models","quality":0.615,"effect":3.222,"z":164.23,"p":0.0,"rank_abs_z":"2/997","passed_gate":true,"site_strength":{"ref_percentile":96.6,"alt_percentile":100.0,"k":7}},{"model":"ELF2_eDBD_TGAAAT40NCAA_KR_yin2017_0_4_7mer","mapping":"CIS-BP (ELF2)","group":"G003 Ets, 18 models","quality":0.896,"effect":6.017,"z":54.18,"p":0.0,"rank_abs_z":"9/997","passed_gate":true,"site_strength":{"ref_percentile":98.8,"alt_percentile":100.0,"k":7}},{"model":"ELF4_eDBD_TGCGGT40NTCA_KAN_yin2017_0_4_7mer","mapping":"CIS-BP (ELF4)","group":"G003 Ets, 18 models","quality":0.732,"effect":4.814,"z":110.16,"p":0.0,"rank_abs_z":"4/997","passed_gate":true,"site_strength":{"ref_percentile":98.0,"alt_percentile":100.0,"k":7}},{"model":"ELK1_NA_TCGGAA20NAGT_ESAG_yang2017_1_3_7mer","mapping":"CIS-BP (ELK1)","group":"G003 Ets, 18 models","quality":0.779,"effect":2.107,"z":20.4,"p":1.6e-92,"rank_abs_z":"34/997","passed_gate":true,"site_strength":{"ref_percentile":92.4,"alt_percentile":99.9,"k":7}},{"model":"ELK3_FL_TTCGAA40NGAC_KX_yin2017_0_4_7mer","mapping":"CIS-BP (ELK3)","group":"G003 Ets, 18 models","quality":0.841,"effect":2.718,"z":34.59,"p":3.1e-262,"rank_abs_z":"16/997","passed_gate":true,"site_strength":{"ref_percentile":94.0,"alt_percentile":100.0,"k":7}},{"model":"ELK4_FL_TCCGCC40NTCA_KAE_yin2017_0_3_7mer","mapping":"CIS-BP (ELK4)","group":"G003 Ets, 18 models","quality":0.921,"effect":3.594,"z":62.15,"p":0.0,"rank_abs_z":"8/997","passed_gate":true,"site_strength":{"ref_percentile":70.7,"alt_percentile":99.6,"k":7}},{"model":"ERF_NA_TCAGAG20NCG_ESW_yang2017_1_4_7mer","mapping":"CIS-BP (ERF)","group":"G003 Ets, 18 models","quality":0.729,"effect":0.529,"z":19.81,"p":2.3e-87,"rank_abs_z":"36/997","passed_gate":true,"site_strength":{"ref_percentile":99.5,"alt_percentile":99.7,"k":7}},{"model":"ERG_NA_TCTACA20NCAG_ESAG_yang2017_1_4_7mer","mapping":"CIS-BP (ERG)","group":"G003 Ets, 18 models","quality":0.881,"effect":2.441,"z":24.39,"p":2e-131,"rank_abs_z":"22/997","passed_gate":true,"site_strength":{"ref_percentile":98.7,"alt_percentile":99.8,"k":7}},{"model":"ETS1_NA_TGTAAA20NGA_ESAF_yang2017_0_4_7mer","mapping":"CIS-BP (ETS1)","group":"G003 Ets, 18 models","quality":0.873,"effect":1.226,"z":25.6,"p":1.5e-144,"rank_abs_z":"20/997","passed_gate":true,"site_strength":{"ref_percentile":99.6,"alt_percentile":100.0,"k":7}}],"n_models_trimmed":8}

<a id="e34"></a>**E34** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=ZNF143%20TERT%20promoter%20repression&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T20:34:06+00:00)

> Europe PMC: 11 hits for 'ZNF143 TERT promoter repression'; top 8 with PMIDs:
> PMID 40328728 (2025): Transposable elements as genome regulators in normal and malignant haematopoiesis.
> PMID 36769179 (2023): Mechanisms of Interaction between Enhancers and Promoters in Three <i>Drosophila</i> Model Systems.
> PMID 35121955 (2020): Illuminating the noncoding genome in cancer.
> PMID 35740532 (2022): Super-Enhancers, Phase-Separated Condensates, and 3D Genome Organization in Cancer.
> PMID 34771690 (2021): A Focus on Regulatory Networks Linking MicroRNAs, Transcription Factors and Target Genes in Neuroblastoma.
> PMID 33514712 (2021): H3K27me3-rich genomic regions can function as silencers to repress gene expression via chromatin interactions.
> PMID 29458419 (2018): Insights about genome function from spatial organization of the genome.
> PMID 33585251 (2020): MYCN Function in Neuroblastoma Development.
