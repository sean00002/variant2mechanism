# TERT promoter C250T and Glioblastoma, melanoma, bladder

Configuration `full`, named mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.04 over 9 model calls; 135 s.

Variant `chr5:1295135:G>A` (somatic); expression context: DepMap:subtype=Glioblastoma (median of 54 lines).

## QBiC-SELEX screen (occupancy first)

Occupied candidates: GABPA (bound elsewhere, z 167.5); KLF12 (bound elsewhere, z -15.38); NR2C1 (bound elsewhere, z 15.31); TGIF2 (bound elsewhere, z -12.19); ZNF143 (bound elsewhere, z -11.71); ZBTB7A (bound elsewhere, z -10.91); SP2 (bound elsewhere, z -9.83); EGR1 (bound elsewhere, z -8.0); BHLHE40 (bound elsewhere, z -7.34); E2F4 (bound elsewhere, z -5.4). Occupancy unknown: ETV2 (z 167.5); ETV3 (z 167.5); FLI1 (z 167.5); ZNF92 (z -33.21); EBF4 (z -24.35). Diagnostic, not shown to the model: 477 of 997 models pass Bonferroni.

## Ranked chains

### 1. chain_1: GABPA alt-gaining ETS site activates TERT (p = 0.45)

TF GABPA (QBiC-SELEX coverage own_model), alt allele binds more; element The variant lies in promoter-like cCRE EH38E3622530 with DNase, H3K27ac and H3K4me3 signal, consistent with an active TERT upstream promoter element, although the cCRE z-scores are maxima over ENCODE biosamples rather than glioblastoma-specific.; gene TERT; cell type Glioblastoma, with relevance to melanoma and bladder cancer.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | GABPA binds the alt allele more strongly. The GABPA own QBiC-SELEX model gives alt effect +4.05 (z 71.32; E32), and the shared Ets model also gives alt-gaining binding (E17). GABPA ENCODE peaks contain the variant in HepG2 and SK-N-SH (E33), but E04 states that no ENCODE biosample matches the glioblastoma expression context, so disease-context occupancy is not established. I choose GABPA over ETV2/ETV3/FLI1 because GABPA has an own QBiC model and some ChIP occupancy, whereas those rely on an ETV5-mapped model and have unknown occupancy. | weak | [E32](#e32), [E17](#e17), [E33](#e33), [E04](#e04) |
| element | The variant is in a promoter-like cCRE with active chromatin marks, so an allele-specific TF change could alter promoter activity. | supported | [E03](#e03) |
| gene | TERT is the nearest coding gene at 0.0 kb and the variant is annotated as a TERT upstream promoter variant, making TERT the target gene. | supported | [E01](#e01), [E02](#e02) |
| cell_type | Glioblastoma is a relevant context because GABPA is expressed at 15.52 TPM in DepMap glioblastoma lines and TERT promoter mutations are reported in glioblastoma; this supports disease context, not GABPA occupancy in that context. | supported | [E17](#e17), [E15](#e15) |
| phenotype | Predicted phenotype: alt-enhanced GABPA binding increases TERT promoter activity and telomerase, supporting tumor maintenance. General TERT promoter mutation literature supports novel TF-site/TERT activation (E34d), but a pooled screen reported no detected ETS-factor dependency for TPMs (E34b), so the phenotype is a model prediction rather than demonstrated. | weak | [E34d](#e34d), [E34b](#e34b), [E15](#e15) |

Predictions: Alt allele shows stronger GABPA ChIP/CUT&RUN signal at this base in a relevant cell type.; Alt allele increases TERT reporter activity in glioblastoma cells in a GABPA-dependent manner.; GABPA knockdown reduces the alt-dependent TERT increase.

Falsified if: Allele-specific GABPA occupancy or a ref/alt TERT reporter assay in glioblastoma cells fails to show alt-enhanced GABPA binding or GABPA-dependent TERT activation.; The alt allele does not increase TERT expression or telomerase activity in a relevant cell type.; GABPA is not expressed or not bound at this element in the disease-relevant cell type.

### 2. chain_4: Null: no TF-mediated effect of this base (p = 0.40)

Null chain: no TF-mediated effect of this variant.

Predictions: No allele-specific TF occupancy at this exact base in disease-relevant cells.; Disease association is explained by a linked causal variant, recurrent somatic mutational hotspot/passenger status, or no allelic TF effect.; TERT activation, if present, is not mediated by a TF binding change at this base.

Falsified if: Allele-specific TF occupancy and reporter assays in relevant cells show that this base directly changes TF binding and TERT expression.; A linked causal variant is excluded and the C250T base itself is shown to be functional.

### 3. chain_2: ETV3 alt-gaining Ets site activates TERT, weak because the model is shared and occupancy is unknown (p = 0.08)

TF ETV3 (QBiC-SELEX coverage own_model), alt allele binds more; element The variant lies in the TERT promoter-like cCRE EH38E3622530.; gene TERT; cell type Glioblastoma.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | ETV3 binds the alt allele more strongly in the shared ETV5-mapped Ets QBiC-SELEX model (effect +2.421, z 167.5; E28). ETV3 occupancy at this site is unknown because ENCODE never assayed ETV3, and the model is not ETV3-specific, so this binding evidence is weak. | weak | [E28](#e28) |
| element | The variant is in an active promoter-like cCRE, so an ETV3 site change could affect promoter output. | supported | [E03](#e03) |
| gene | TERT is the nearest gene and the variant is annotated as a TERT upstream promoter variant. | supported | [E01](#e01), [E02](#e02) |
| cell_type | Glioblastoma is a plausible context because ETV3 is expressed at 8.69 TPM in DepMap glioblastoma lines and TERT promoter mutations occur in glioblastoma. | supported | [E28](#e28), [E15](#e15) |
| phenotype | Predicted phenotype: alt-enhanced ETV3 binding would increase TERT transcription and telomerase activity. No direct ETV3-C250T perturbation evidence is cited, and the shared ETV5-mapped model makes this a weak prediction. | weak | [E34d](#e34d), [E15](#e15) |

Predictions: ETV3 ChIP or allele-specific binding assay shows alt-enhanced occupancy at this base in glioblastoma cells.; ETV3 depletion reduces alt-dependent TERT expression.; ETV3 binding correlates with TERT expression in relevant tumor cells.

Falsified if: ETV3 is not expressed or not bound at the TERT promoter in glioblastoma cells.; Allele-specific assays show no ETV3 occupancy difference at this base.; Alt-dependent TERT activation remains after ETV3 depletion.

### 4. chain_3: Loss of KLF12 repressor on the alt allele derepresses TERT, speculative (p = 0.07)

TF KLF12 (QBiC-SELEX coverage own_model), ref allele binds more; element The variant lies in the TERT promoter-like cCRE EH38E3622530.; gene TERT; cell type Glioblastoma, but KLF12 relevance is weak because expression is low.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | KLF12 binds the ref allele more strongly in QBiC-SELEX (effect -0.439, z -15.38; E18). The best model is KLF5-mapped and KLF12 ChIP is only in HepG2, so factor-specific disease-relevant occupancy is weak. | weak | [E18](#e18), [E04](#e04) |
| element | The variant is in an active promoter-like cCRE, so loss of a repressive TF site could change promoter activity. | supported | [E03](#e03) |
| gene | TERT is the nearest gene and is annotated as the upstream promoter target. | supported | [E01](#e01), [E02](#e02) |
| cell_type | KLF12 relevance to glioblastoma is weak: it is expressed at only 4.47 TPM in DepMap glioblastoma lines, and no disease-context occupancy is shown. | weak | [E18](#e18) |
| phenotype | Speculative phenotype: if KLF12 represses TERT, then the alt allele losing KLF12 binding would derepress TERT and increase telomerase activity. No direct evidence shows KLF12 represses TERT. | missing | none |

Predictions: KLF12 ChIP signal is stronger on the ref allele at this base.; KLF12 knockdown increases TERT expression.; The alt allele shows reduced KLF12 occupancy and increased TERT reporter activity.

Falsified if: KLF12 is not expressed or not bound at the TERT promoter in glioblastoma cells.; Alt allele does not reduce KLF12 occupancy at this base.; KLF12 loss does not derepress TERT in relevant cells.

## Prediction matrix

| Test | Cost | Separates top two | chain_1 | chain_4 | chain_2 | chain_3 |
| --- | --- | --- | --- | --- | --- | --- |
| Allele-specific GABPA ChIP-qPCR or CUT&RUN at C250T in a glioblastoma line heterozygous for the mutation (ref/alt discrimination). | high | yes | Alt allele has stronger GABPA occupancy at this base. | No allele-specific GABPA occupancy at this base. | Ets occupancy may be alt-enhanced, but GABPA-specific binding is not required by this model; GABPA signal alone does not support chain_2. | No GABPA occupancy difference; KLF12 is instead stronger on the ref allele. |
| Ref/alt TERT promoter luciferase reporter (or MPRA) in glioblastoma cells, with and without GABPA knockdown. | medium | yes | Alt allele increases TERT reporter activity; the increase is reduced by GABPA knockdown/CRISPRi. | No reproducible alt-dependent increase in TERT reporter activity at this base. | Alt allele increases reporter activity, but GABPA knockdown has little effect; ETV3 knockdown reduces it. | Alt allele increases reporter activity through loss of KLF12 repression; GABPA knockdown has little effect and KLF12 knockdown increases the ref reporter. |
| GABPA CRISPRi/knockdown followed by TERT expression and telomerase activity in a TERT promoter-mutant glioblastoma line. | medium | yes | GABPA depletion lowers TERT expression in TERT promoter-mutant glioblastoma cells. | No change with GABPA depletion, as expected if this base has no TF-mediated effect. | No change with GABPA depletion; ETV3 depletion lowers TERT. | No change with GABPA depletion; KLF12 depletion raises TERT. |
| ETV3 knockdown/CRISPRi in the same TERT promoter-mutant glioblastoma cell system. | medium | no | No change in TERT expression or reporter activity after ETV3 depletion. | No change after ETV3 depletion. | ETV3 depletion reduces the alt-dependent TERT increase. | No change after ETV3 depletion. |
| Allele-specific KLF12 ChIP plus KLF12 knockdown in the glioblastoma reporter system. | medium | no | No allele-specific KLF12 occupancy and no KLF12-dependent change in TERT reporter activity. | No allele-specific KLF12 occupancy and no KLF12-dependent TERT change. | No allele-specific KLF12 occupancy and no KLF12-dependent change in TERT reporter activity. | KLF12 occupies the ref allele more strongly; KLF12 knockdown increases TERT expression or ref reporter activity. |
| Deep sequencing of the TERT promoter and flanking region in tumors, plus mutational-signature analysis, to test linkage and passenger status of C250T. | low | no | C250T usually occurs without a linked functional promoter variant and is not explained by a passenger signature alone. | A linked causal variant or recurrent passenger/hotspot mechanism explains the association; C250T itself need not be functional. | C250T usually occurs without a linked functional promoter variant and is not explained by a passenger signature alone. | C250T usually occurs without a linked functional promoter variant and is not explained by a passenger signature alone. |

## Next experiment

Ref/alt TERT promoter luciferase reporter (or MPRA) in a glioblastoma cell line, with and without GABPA knockdown: it is the cheapest assay that separates alt-dependent TERT promoter activity (chain_1) from no allelic effect at this base (chain_4); adding GABPA knockdown then distinguishes chain_1 from the other TF chains.

## Investigate calls

- qbic_tf_detail({"tf": "GABPA"})
- chip_peaks({"biosample": null, "tf": "GABPA"})
- literature_search({"query": "TERT promoter C250T GABPA ETS binding site allele-specific glioblastoma"})

## Flags

- quote_rejected: PMID 41744838: not an exact substring of the abstract

Citation support: 0.93 of links cite only evidence that passed every check.

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
> PMID 42804732 (2026): SNP rs2853669 potentially elevates the risk of glioblastoma development and leads to worse prognosis when in cis with mutant TERT promoter in a Japanese cohort.
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

<a id="e32"></a>**E32** qbic_tf_detail, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> {"tf":"GABPA","symbol":"GABPA","via":"hgnc_symbol","notes":[],"coverage":"own_model","variant":"chr5:1295135:G>A","gate_p":5.02e-05,"models":[{"model":"GABPA_FL_TC40NGCGATT_YWL_jolma2025_0_2_7mer","mapping":"own","group":"G003 Ets, 18 models","quality":0.658,"effect":4.05,"z":71.32,"p":0.0,"rank_abs_z":"7/997","passed_gate":true,"site_strength":{"ref_percentile":96.3,"alt_percentile":99.8,"k":7}},{"model":"ELF1_FL_TATGAC40NTCA_KW_yin2017_0_2_7mer","mapping":"CIS-BP (ELF1)","group":"G003 Ets, 18 models","quality":0.615,"effect":3.222,"z":164.23,"p":0.0,"rank_abs_z":"2/997","passed_gate":true,"site_strength":{"ref_percentile":96.6,"alt_percentile":100.0,"k":7}},{"model":"ELF2_eDBD_TGAAAT40NCAA_KR_yin2017_0_4_7mer","mapping":"CIS-BP (ELF2)","group":"G003 Ets, 18 models","quality":0.896,"effect":6.017,"z":54.18,"p":0.0,"rank_abs_z":"9/997","passed_gate":true,"site_strength":{"ref_percentile":98.8,"alt_percentile":100.0,"k":7}},{"model":"ELF4_eDBD_TGCGGT40NTCA_KAN_yin2017_0_4_7mer","mapping":"CIS-BP (ELF4)","group":"G003 Ets, 18 models","quality":0.732,"effect":4.814,"z":110.16,"p":0.0,"rank_abs_z":"4/997","passed_gate":true,"site_strength":{"ref_percentile":98.0,"alt_percentile":100.0,"k":7}},{"model":"ELK1_NA_TCGGAA20NAGT_ESAG_yang2017_1_3_7mer","mapping":"CIS-BP (ELK1)","group":"G003 Ets, 18 models","quality":0.779,"effect":2.107,"z":20.4,"p":1.6e-92,"rank_abs_z":"34/997","passed_gate":true,"site_strength":{"ref_percentile":92.4,"alt_percentile":99.9,"k":7}},{"model":"ELK3_FL_TTCGAA40NGAC_KX_yin2017_0_4_7mer","mapping":"CIS-BP (ELK3)","group":"G003 Ets, 18 models","quality":0.841,"effect":2.718,"z":34.59,"p":3.1e-262,"rank_abs_z":"16/997","passed_gate":true,"site_strength":{"ref_percentile":94.0,"alt_percentile":100.0,"k":7}},{"model":"ELK4_FL_TCCGCC40NTCA_KAE_yin2017_0_3_7mer","mapping":"CIS-BP (ELK4)","group":"G003 Ets, 18 models","quality":0.921,"effect":3.594,"z":62.15,"p":0.0,"rank_abs_z":"8/997","passed_gate":true,"site_strength":{"ref_percentile":70.7,"alt_percentile":99.6,"k":7}},{"model":"ERF_NA_TCAGAG20NCG_ESW_yang2017_1_4_7mer","mapping":"CIS-BP (ERF)","group":"G003 Ets, 18 models","quality":0.729,"effect":0.529,"z":19.81,"p":2.3e-87,"rank_abs_z":"36/997","passed_gate":true,"site_strength":{"ref_percentile":99.5,"alt_percentile":99.7,"k":7}},{"model":"ERG_NA_TCTACA20NCAG_ESAG_yang2017_1_4_7mer","mapping":"CIS-BP (ERG)","group":"G003 Ets, 18 models","quality":0.881,"effect":2.441,"z":24.39,"p":2e-131,"rank_abs_z":"22/997","passed_gate":true,"site_strength":{"ref_percentile":98.7,"alt_percentile":99.8,"k":7}},{"model":"ETS1_NA_TGTAAA20NGA_ESAF_yang2017_0_4_7mer","mapping":"CIS-BP (ETS1)","group":"G003 Ets, 18 models","quality":0.873,"effect":1.226,"z":25.6,"p":1.5e-144,"rank_abs_z":"20/997","passed_gate":true,"site_strength":{"ref_percentile":99.6,"alt_percentile":100.0,"k":7}}],"n_models_trimmed":8}

<a id="e33"></a>**E33** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-25T17:27:26+00:00)

> 2 ENCODE GABPA ChIP-seq peaks contain chr5:1295135:G>A: biosamples HepG2, SK-N-SH; experiments ENCSR000BJK, ENCSR000BTG.

<a id="e34"></a>**E34** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TERT%20promoter%20C250T%20GABPA%20ETS%20binding%20site%20allele-specific%20glioblastoma&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T13:10:14+00:00)

> Europe PMC: 30 hits for 'TERT promoter C250T GABPA ETS binding site allele-specific glioblastoma'; top 8 with PMIDs:
> PMID 40822359 (2025): AURKB and PI3K/AKT/mTOR pathways converge to regulate &lt;i&gt;TERT&lt;/i&gt; expression.
> PMID 37741952 (2023): Pooled genetic screens to identify vulnerabilities in TERT-promoter-mutant glioblastoma.
> PMID 36713366 (2022): <i>TERT</i> promoter mutations and methylation for telomerase activation in urothelial carcinomas: New mechanistic insights and clinical significance.
> PMID 38033865 (2023): Reactivation of telomerase reverse transcriptase expression in cancer: the role of TERT promoter mutations.
> PMID 38285162 (2024): Mechanisms of telomere maintenance and associated therapeutic vulnerabilities in malignant gliomas.
> PMID 40272676 (2025): TERT Amplification a Risk Stratification Marker in Papillary Thyroid Carcinoma, Significantly Correlated with Tumor Recurrence and Survival.
> PMID 35903534 (2022): TERT Promoter Mutations and Telomerase in Melanoma.
> PMID 34395278 (2021): Clinical Application of <i>TERT</i> Promoter Mutations in Urothelial Carcinoma.

<a id="e34a"></a>**E34a** literature_search, Europe PMC abstract, PMID 37741952 (https://europepmc.org/article/MED/37741952; retrieved 2026-10-26T13:10:14+00:00)

> Here we used pooled CRISPR/Cas9-based approaches to identify vulnerabilities associated with telomerase reverse transcriptase (TERT) promoter mutations (TPMs) found in >80% of glioblastomas.

<a id="e34b"></a>**E34b** literature_search, Europe PMC abstract, PMID 37741952 (https://europepmc.org/article/MED/37741952; retrieved 2026-10-26T13:10:14+00:00)

> However, we could not detect dependencies on either TERT itself or on an E-twenty six transcription (ETS) factor known to activate TPMs.

<a id="e34c"></a>**E34c** literature_search, Europe PMC abstract, PMID 38033865 (https://europepmc.org/article/MED/38033865; retrieved 2026-10-26T13:10:14+00:00)

> Point mutations in the core promoter region of the telomerase reverse transcriptase (TERT) gene have been found to occur at high frequencies in several tumour types and considered a primary cause of telomerase reactivation in cancer cells.

<a id="e34d"></a>**E34d** literature_search, Europe PMC abstract, PMID 38033865 (https://europepmc.org/article/MED/38033865; retrieved 2026-10-26T13:10:14+00:00)

> These mutations promote TERT gene expression by multiple mechanisms, including the generation of novel binding sites for nuclear transcription factors, displacement of negative regulators from DNA G-quadruplexes, recruitment of epigenetic activators and disruption of long-range interactions between TERT locus and telomeres.

<a id="e34e"></a>**E34e** literature_search, Europe PMC abstract, PMID 35903534 (https://europepmc.org/article/MED/35903534; retrieved 2026-10-26T13:10:14+00:00)

> A growing number of recent studies suggest that the most common mutations in the TERT promoter (ATG start site -124C>T and -146C>T) are associated with increased TERT mRNA expression, telomerase activity, telomere length, and poor prognosis.
