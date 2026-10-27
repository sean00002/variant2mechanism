# TERT promoter C228T and Glioblastoma, melanoma, bladder

Configuration `full`, named mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.04 over 10 model calls; 105 s.

Variant `chr5:1295113:G>A` (somatic); expression context: DepMap:subtype=Glioblastoma (median of 54 lines).

## QBiC-SELEX screen (occupancy first)

Occupied candidates: GABPA (bound elsewhere, z 166.19); ZIC2 (bound elsewhere, z -20.85); CTCF (bound elsewhere, z -14.7); ZBTB7A (bound elsewhere, z -14.11); NR2C1 (bound elsewhere, z -10.53); TGIF2 (bound elsewhere, z -7.74); E2F4 (bound elsewhere, z 5.78); E2F6 (bound elsewhere, z 5.78); E2F5 (bound elsewhere, z 5.78); KLF12 (bound elsewhere, z 5.16). Occupancy unknown: ETV2 (z 166.19); ETV3 (z 166.19); FLI1 (z 166.19); TFAP2A (z -36.84); TFAP2C (z -36.84). Diagnostic, not shown to the model: 310 of 997 models pass Bonferroni.

## Ranked chains

### 1. H1_GABPA: GABPA/ETS alt-gain activates TERT (p = 0.72)

TF GABPA (QBiC-SELEX coverage own_model), alt allele binds more; element TERT promoter PLS cCRE EH38E3622530; gene TERT; cell type Glioblastoma / TERT-expressing cancer cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | GABPA binds the alt A allele more strongly. GABPA has its own QBiC-SELEX model at this base with an alt-gain (effect +4.01, z 68.47; E33), and published work identifies a de novo ETS motif and the GABP tetramer as the activator at mutant TERT promoters (E34a, E34b, E34e). Caveat: no ENCODE ChIP-seq peak over this exact base is from a glioblastoma or otherwise matching biosample (E04); GABPA peaks over the variant are only from other biosamples (E11). | supported | [E33](#e33), [E34a](#e34a), [E34b](#e34b), [E34e](#e34e), [E04](#e04), [E11](#e11) |
| element | The variant lies in promoter-like cCRE EH38E3622530 with active chromatin marks (DNase, H3K27ac, H3K4me3) and dense TF occupancy; Ensembl independently annotates a TERT promoter regulatory feature. Caveat: E03 z-scores are maxima over ENCODE biosamples, not glioblastoma-specific. | supported | [E03](#e03), [E04](#e04), [E01](#e01) |
| gene | The cCRE is 0 kb from the TERT TSS and the variant is annotated as a TERT upstream_gene_variant in the TERT promoter, making TERT the direct target gene. | supported | [E02](#e02), [E01](#e01) |
| cell_type | GABPA is expressed in DepMap glioblastoma lines (15.52 TPM, rank 303/1626; E17), and GABP-dependent TERT promoter activation has been reported across TERTp-mutant cancer cell lines (E34b), although the provided ChIP data do not include a matched glioblastoma biosample (E04). | weak | [E17](#e17), [E34b](#e34b), [E04](#e04) |
| phenotype | Alt-enhanced GABP/ETS binding at the TERT promoter increases TERT transcription and telomerase activity: GABP tetramer is reported to be responsible for promoter activation at recurrent TERTp mutations, and its assembly at the promoter is associated with TERT reactivation and hTERT hyperactivation. | supported | [E34b](#e34b), [E34e](#e34e), [E34c](#e34c) |

Predictions: Allele-specific GABPA ChIP or CUT&RUN shows alt > ref occupancy at C228T in a heterozygous glioblastoma line; Alt TERT promoter reporter has higher activity than ref in glioblastoma cells; GABPA knockdown lowers TERT expression and removes the alt-specific expression excess

Falsified if: Allele-specific GABPA ChIP or CUT&RUN does not show alt > ref occupancy at C228T in a TERT-expressing glioblastoma line; Alt and ref TERT promoter reporters show equal activity in glioblastoma cells; GABPA knockdown does not reduce TERT expression or does not remove the alt-specific excess

### 2. H0_null: No TF-mediated allelic effect (p = 0.20)

Null chain: no TF-mediated effect of this variant.

Predictions: No allele-specific TF occupancy at this base in a relevant cell type; Alt and ref TERT promoter reporters show equal activity; Any disease association is explained by a linked causal variant, a mutational hotspot/passenger effect, or no allelic effect

Falsified if: Allele-specific GABPA/ETS ChIP or CUT&RUN and an alt-vs-ref TERT reporter show a reproducible TF-mediated effect at this base in a relevant cell type; Base editing of C228T from alt to ref changes TERT expression independent of linked variants

### 3. H2_ETV3: ETV3/ETS alt-gain activates TERT (p = 0.08)

TF ETV3 (QBiC-SELEX coverage own_model), alt allele binds more; element TERT promoter PLS cCRE EH38E3622530; gene TERT; cell type Glioblastoma / TERT-expressing cancer cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | ETV3's best QBiC-SELEX model predicts that the alt A allele binds more strongly (effect +2.121, z 166.19; E28), but that model is a CIS-BP-mapped ETV5 model shared identically with other ETS paralogs, so this is family-level ETS evidence rather than ETV3-specific evidence. ETV3 occupancy at this base is unknown because ENCODE never assayed ETV3; no ChIP peak is available. | weak | [E28](#e28) |
| element | The variant lies in promoter-like cCRE EH38E3622530 with active chromatin marks and dense TF occupancy, consistent with a functional TERT promoter element; E03 z-scores are maxima over biosamples, not glioblastoma-specific. | supported | [E03](#e03), [E04](#e04), [E01](#e01) |
| gene | The element is 0 kb from the TERT TSS and the variant is annotated as a TERT upstream_gene_variant in the TERT promoter, making TERT the direct target. | supported | [E02](#e02), [E01](#e01) |
| cell_type | ETV3 is expressed at a modest level in DepMap glioblastoma lines (8.69 TPM, rank 521/1626; E28), so the cell type is permissive, but no ETV3-specific disease or occupancy data are provided. | weak | [E28](#e28) |
| phenotype | If ETV3 rather than GABPA occupied the alt-gained ETS site, it could increase TERT expression, but no ETV3-specific occupancy, perturbation, or TERT-output evidence supports this chain. | missing | none |

Predictions: ETV3 ChIP or CUT&RUN shows alt > ref occupancy at C228T in a TERT-expressing glioblastoma line; ETV3 knockdown reduces TERT expression or alt-specific reporter activity; GABPA knockdown does not fully explain the allele-specific TERT effect

Falsified if: ETV3 ChIP does not occupy the variant allele-specifically in glioblastoma cells; ETV3 depletion does not reduce TERT expression or reporter activity; GABPA, not ETV3, accounts for all allele-specific ETS occupancy and TERT activation

## Prediction matrix

| Test | Cost | Separates top two | H1_GABPA | H0_null | H2_ETV3 |
| --- | --- | --- | --- | --- | --- |
| Allele-specific GABPA ChIP-qPCR or CUT&RUN at C228T in a heterozygous glioma line | medium | yes | alt > ref GABPA occupancy at C228T | equal or no allele-specific occupancy | no GABPA-specific alt > ref occupancy; an ETV3 ChIP would be needed to test H2 |
| Alt-vs-ref TERT promoter luciferase reporter in glioblastoma cells | low | yes | alt reporter > ref reporter | alt reporter = ref reporter | alt reporter > ref reporter if ETV3 can use the site |
| GABPA knockdown in a C228T-heterozygous glioblastoma line with allele-specific TERT expression readout | medium | yes | TERT expression falls and the alt-specific excess is lost | no change in TERT expression | TERT expression is unchanged or the alt-specific excess persists |
| ETV3 ChIP-qPCR at C228T in a TERT-expressing glioblastoma line | medium | no | no ETV3-specific alt enrichment | equal or no allele-specific occupancy | alt > ref ETV3 occupancy at C228T |
| Base editing C228T from alt to ref in a heterozygous glioblastoma line | high | yes | TERT expression and telomerase activity decrease | no change | little or no decrease if ETV3 is not the driver |

## Next experiment

Alt-vs-ref TERT promoter luciferase reporter in a glioblastoma line: H1 predicts alt > ref activity; H0 predicts equal activity. This is the cheapest test separating the top two chains, though it does not by itself prove GABPA is the factor.

## Investigate calls

- literature_search({"query": "TERT promoter C228T -124G>A ETS GABPA allele-specific binding reporter glioblastoma"})
- qbic_tf_detail({"tf": "GABPA"})
- literature_search({"query": "GABP TERT promoter mutation creates ETS binding site telomerase reactivation"})

## Flags

- quote_rejected: PMID 41744838: not an exact substring of the abstract
- quote_rejected: PMID 40822359: not an exact substring of the abstract

Citation support: 0.90 of links cite only evidence that passed every check.

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

<a id="e16"></a>**E16** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> QBiC-SELEX screen of chr5:1295113:G>A, one line per TF, each with the TF's own or CIS-BP-mapped model of largest |z|. Candidates are TFs whose ENCODE ChIP-seq peaks contain the variant and that are expressed (DepMap subtype median Glioblastoma), bound here before bound elsewhere, then by |z|; then expressed TFs ENCODE never assayed whose best model passes the gate (occupancy unknown). Shown: 10 of 20 occupied, 5 of 111 with unknown occupancy. Left out: 0 TFs assayed in the matching biosample and 552 assayed only elsewhere, none with a peak here; 1 bound but below 1 TPM. The gate (|z| > 4.05, Bonferroni over 997 models) marks a change QBiC-SELEX detects; it says nothing about occupancy. Effect > 0 means the alternate allele binds more strongly. In vitro binding only.

<a id="e17"></a>**E17** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> GABPA (Ets, 18 models; QBiC-SELEX coverage: own model): best model ETV5_NA_TGCACT20NGA_ESAF_yang2017_1_3_6mer (a CIS-BP-mapped model of ETV5), z 166.19, effect 2.121: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 15.52 TPM, rank 303 of 1626 TFs in DepMap:subtype=Glioblastoma (median of 54 lines). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in HepG2, SK-N-SH, e.g. ENCSR000BJK. Best model's site strength: ref 97.1th, alt 99.3th percentile of its k-mer coefficients.

<a id="e18"></a>**E18** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> ZIC2 (C2H2 ZF, 4 models; QBiC-SELEX coverage: mapped models only): best model ZIC4_eDBD_TGCGTA40NTCA_KT_yin2017_1_3_7mer (a CIS-BP-mapped model of ZIC4), z -20.85, effect -0.916: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 3.7 TPM, rank 852 of 1626 TFs in DepMap:subtype=Glioblastoma (median of 54 lines). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in HEK293, e.g. ENCSR728MWW. Best model's site strength: ref 99.8th, alt 97.4th percentile of its k-mer coefficients.

<a id="e19"></a>**E19** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> CTCF (C2H2 ZF, 1 model; QBiC-SELEX coverage: own model): best model CTCF_FL_TG40NCTGTGG_YWL_jolma2025_0_3_7mer (its own model), z -14.7, effect -1.719: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 26.45 TPM, rank 163 of 1626 TFs in DepMap:subtype=Glioblastoma (median of 54 lines). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in DOHH2, e.g. ENCSR084RDK. Best model's site strength: ref 99.8th, alt 97.0th percentile of its k-mer coefficients.

<a id="e20"></a>**E20** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> ZBTB7A (C2H2 ZF, 1 model; QBiC-SELEX coverage: own model): best model ZBTB7A_eDBD_TTTGCT40NCGT_KR_yin2017_0_4_7mer (its own model), z -14.11, effect -0.826: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 8.49 TPM, rank 531 of 1626 TFs in DepMap:subtype=Glioblastoma (median of 54 lines). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in K562, e.g. ENCSR000BME. Best model's site strength: ref 99.9th, alt 99.9th percentile of its k-mer coefficients.

<a id="e21"></a>**E21** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> NR2C1 (Nuclear receptor, 29 models; QBiC-SELEX coverage: own model): best model FXR_NA_Lib1_NA_bhimsaria2023_0(3)_3_7mer (a CIS-BP-mapped model of NR1H4), z -10.53, effect -0.434: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 18.52 TPM, rank 251 of 1626 TFs in DepMap:subtype=Glioblastoma (median of 54 lines). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in GM12878, e.g. ENCSR784VIQ. Best model's site strength: ref 97.7th, alt 97.9th percentile of its k-mer coefficients.

<a id="e22"></a>**E22** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> TGIF2 (Homeodomain, 9 models; QBiC-SELEX coverage: own model): best model PKNOX1_FL_TCGTCC40NGCC_KW_yin2017_0_4_7mer (a CIS-BP-mapped model of PKNOX1), z -7.74, effect -0.218: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 10.31 TPM, rank 452 of 1626 TFs in DepMap:subtype=Glioblastoma (median of 54 lines). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in HepG2, e.g. ENCSR993LMB. Best model's site strength: ref 96.9th, alt 94.4th percentile of its k-mer coefficients.

<a id="e23"></a>**E23** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> E2F4 (E2F, 4 models; QBiC-SELEX coverage: own model): best model E2F1_NA_CAATT14N_ESU_yang2017_0_4_7mer (a CIS-BP-mapped model of E2F1), z 5.78, effect 0.464: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 58.31 TPM, rank 49 of 1626 TFs in DepMap:subtype=Glioblastoma (median of 54 lines). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in GM12878, HepG2, e.g. ENCSR000DYY. Best model's site strength: ref 98.9th, alt 99.5th percentile of its k-mer coefficients.

<a id="e24"></a>**E24** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> E2F6 (E2F, 4 models; QBiC-SELEX coverage: mapped models only): best model E2F1_NA_CAATT14N_ESU_yang2017_0_4_7mer (a CIS-BP-mapped model of E2F1), z 5.78, effect 0.464: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 17.63 TPM, rank 267 of 1626 TFs in DepMap:subtype=Glioblastoma (median of 54 lines). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in A549, K562, e.g. ENCSR000BLI. Best model's site strength: ref 98.9th, alt 99.5th percentile of its k-mer coefficients.

<a id="e25"></a>**E25** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> E2F5 (E2F, 4 models; QBiC-SELEX coverage: mapped models only): best model E2F1_NA_CAATT14N_ESU_yang2017_0_4_7mer (a CIS-BP-mapped model of E2F1), z 5.78, effect 0.464: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 6.91 TPM, rank 605 of 1626 TFs in DepMap:subtype=Glioblastoma (median of 54 lines). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in HepG2, e.g. ENCSR486JYI. Best model's site strength: ref 98.9th, alt 99.5th percentile of its k-mer coefficients.

<a id="e26"></a>**E26** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> KLF12 (C2H2 ZF, 6 models; QBiC-SELEX coverage: own model): best model KLF3_FL_TTATGG40NCCA_KAF_yin2017_0_4_7mer (a CIS-BP-mapped model of KLF3), z 5.16, effect 0.337: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 4.47 TPM, rank 787 of 1626 TFs in DepMap:subtype=Glioblastoma (median of 54 lines). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in HepG2, e.g. ENCSR552YWL. Best model's site strength: ref 89.0th, alt 92.0th percentile of its k-mer coefficients.

<a id="e27"></a>**E27** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> ETV2 (Ets, 18 models; QBiC-SELEX coverage: own model): best model ETV5_NA_TGCACT20NGA_ESAF_yang2017_1_3_6mer (a CIS-BP-mapped model of ETV5), z 166.19, effect 2.121: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 1.4 TPM, rank 1063 of 1626 TFs in DepMap:subtype=Glioblastoma (median of 54 lines). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 97.1th, alt 99.3th percentile of its k-mer coefficients.

<a id="e28"></a>**E28** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> ETV3 (Ets, 18 models; QBiC-SELEX coverage: own model): best model ETV5_NA_TGCACT20NGA_ESAF_yang2017_1_3_6mer (a CIS-BP-mapped model of ETV5), z 166.19, effect 2.121: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 8.69 TPM, rank 521 of 1626 TFs in DepMap:subtype=Glioblastoma (median of 54 lines). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 97.1th, alt 99.3th percentile of its k-mer coefficients.

<a id="e29"></a>**E29** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> FLI1 (Ets, 18 models; QBiC-SELEX coverage: own model): best model ETV5_NA_TGCACT20NGA_ESAF_yang2017_1_3_6mer (a CIS-BP-mapped model of ETV5), z 166.19, effect 2.121: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 4.71 TPM, rank 767 of 1626 TFs in DepMap:subtype=Glioblastoma (median of 54 lines). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 97.1th, alt 99.3th percentile of its k-mer coefficients.

<a id="e30"></a>**E30** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> TFAP2A (AP-2, 4 models; QBiC-SELEX coverage: own model): best model TFAP2E_FL_TCAAAC40NAAC_KW_yin2017_1_3_7mer (a CIS-BP-mapped model of TFAP2E), z -36.84, effect -1.289: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 9.65 TPM, rank 479 of 1626 TFs in DepMap:subtype=Glioblastoma (median of 54 lines). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 99.5th, alt 96.5th percentile of its k-mer coefficients.

<a id="e31"></a>**E31** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> TFAP2C (AP-2, 4 models; QBiC-SELEX coverage: own model): best model TFAP2E_FL_TCAAAC40NAAC_KW_yin2017_1_3_7mer (a CIS-BP-mapped model of TFAP2E), z -36.84, effect -1.289: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 6.49 TPM, rank 631 of 1626 TFs in DepMap:subtype=Glioblastoma (median of 54 lines). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 99.5th, alt 96.5th percentile of its k-mer coefficients.

<a id="e32"></a>**E32** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TERT%20promoter%20C228T%20-124G%3EA%20ETS%20GABPA%20allele-specific%20binding%20reporter%20glioblastoma&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T02:34:30+00:00)

> Europe PMC: 13 hits for 'TERT promoter C228T -124G>A ETS GABPA allele-specific binding reporter glioblastoma'; top 8 with PMIDs:
> PMID 40822359 (2025): AURKB and PI3K/AKT/mTOR pathways converge to regulate &lt;i&gt;TERT&lt;/i&gt; expression.
> PMID 34944589 (2021): <i>TERT</i> Promoter Mutations Increase Sense and Antisense Transcription from the <i>TERT</i> Promoter.
> PMID 31802036 (2020): GABPA is a master regulator of luminal identity and restrains aggressive diseases in bladder cancer.
> PMID 31285550 (2019): Mechanisms underlying the activation of TERT transcription and telomerase activity in human cancer: old actors and new players.
> PMID 33832990 (2021): Interpretation of allele-specific chromatin accessibility using cell state-aware deep learning.
> PMID 31903880 (2020): Telomere-related Markers for Cancer.
> PMID 26941407 (2016): Understanding TERT Promoter Mutations: A Common Path to Immortality.
> PMID 27028424 (2016): Telomerase reactivation in cancers: Mechanisms that govern transcriptional activation of the wild-type vs. mutant TERT promoters.

<a id="e33"></a>**E33** qbic_tf_detail, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> {"tf":"GABPA","symbol":"GABPA","via":"hgnc_symbol","notes":[],"coverage":"own_model","variant":"chr5:1295113:G>A","gate_p":5.02e-05,"models":[{"model":"GABPA_FL_TC40NGCGATT_YWL_jolma2025_0_2_7mer","mapping":"own","group":"G003 Ets, 18 models","quality":0.658,"effect":4.01,"z":68.47,"p":0.0,"rank_abs_z":"5/997","passed_gate":true,"site_strength":{"ref_percentile":96.3,"alt_percentile":99.8,"k":7}},{"model":"ELF1_FL_TATGAC40NTCA_KW_yin2017_0_2_7mer","mapping":"CIS-BP (ELF1)","group":"G003 Ets, 18 models","quality":0.615,"effect":2.514,"z":124.32,"p":0.0,"rank_abs_z":"2/997","passed_gate":true,"site_strength":{"ref_percentile":92.6,"alt_percentile":100.0,"k":7}},{"model":"ELF2_eDBD_TGAAAT40NCAA_KR_yin2017_0_4_7mer","mapping":"CIS-BP (ELF2)","group":"G003 Ets, 18 models","quality":0.896,"effect":4.515,"z":35.9,"p":2.7e-282,"rank_abs_z":"15/997","passed_gate":true,"site_strength":{"ref_percentile":97.8,"alt_percentile":100.0,"k":7}},{"model":"ELF4_eDBD_TGCGGT40NTCA_KAN_yin2017_0_4_7mer","mapping":"CIS-BP (ELF4)","group":"G003 Ets, 18 models","quality":0.732,"effect":3.97,"z":85.47,"p":0.0,"rank_abs_z":"3/997","passed_gate":true,"site_strength":{"ref_percentile":97.0,"alt_percentile":100.0,"k":7}},{"model":"ELK1_NA_TCGGAA20NAGT_ESAG_yang2017_1_3_7mer","mapping":"CIS-BP (ELK1)","group":"G003 Ets, 18 models","quality":0.779,"effect":1.363,"z":12.45,"p":1.4e-35,"rank_abs_z":"63/997","passed_gate":true,"site_strength":{"ref_percentile":98.2,"alt_percentile":99.4,"k":7}},{"model":"ELK3_FL_TTCGAA40NGAC_KX_yin2017_0_4_7mer","mapping":"CIS-BP (ELK3)","group":"G003 Ets, 18 models","quality":0.841,"effect":2.56,"z":31.23,"p":4.6e-214,"rank_abs_z":"16/997","passed_gate":true,"site_strength":{"ref_percentile":98.2,"alt_percentile":100.0,"k":7}},{"model":"ELK4_FL_TCCGCC40NTCA_KAE_yin2017_0_3_7mer","mapping":"CIS-BP (ELK4)","group":"G003 Ets, 18 models","quality":0.921,"effect":3.273,"z":56.2,"p":0.0,"rank_abs_z":"7/997","passed_gate":true,"site_strength":{"ref_percentile":92.2,"alt_percentile":99.6,"k":7}},{"model":"ERF_NA_TCAGAG20NCG_ESW_yang2017_1_4_7mer","mapping":"CIS-BP (ERF)","group":"G003 Ets, 18 models","quality":0.729,"effect":0.63,"z":23.53,"p":2.2e-122,"rank_abs_z":"23/997","passed_gate":true,"site_strength":{"ref_percentile":96.9,"alt_percentile":99.7,"k":7}},{"model":"ERG_NA_TCTACA20NCAG_ESAG_yang2017_1_4_7mer","mapping":"CIS-BP (ERG)","group":"G003 Ets, 18 models","quality":0.881,"effect":2.323,"z":22.12,"p":2e-108,"rank_abs_z":"26/997","passed_gate":true,"site_strength":{"ref_percentile":98.2,"alt_percentile":99.8,"k":7}},{"model":"ETS1_NA_TGTAAA20NGA_ESAF_yang2017_0_4_7mer","mapping":"CIS-BP (ETS1)","group":"G003 Ets, 18 models","quality":0.873,"effect":1.97,"z":40.46,"p":0.0,"rank_abs_z":"12/997","passed_gate":true,"site_strength":{"ref_percentile":98.7,"alt_percentile":100.0,"k":7}}],"n_models_trimmed":8}

<a id="e34"></a>**E34** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=GABP%20TERT%20promoter%20mutation%20creates%20ETS%20binding%20site%20telomerase%20reactivation&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T02:34:39+00:00)

> Europe PMC: 24 hits for 'GABP TERT promoter mutation creates ETS binding site telomerase reactivation'; top 8 with PMIDs:
> PMID 40513567 (2025): The immortality mechanism of TERT promoter mutant cancers is self-reinforcing and reversible.
> PMID 41872659 (2026): Type 2 Diabetes From the Perspective of Telomere Biology.
> PMID 40822359 (2025): AURKB and PI3K/AKT/mTOR pathways converge to regulate &lt;i&gt;TERT&lt;/i&gt; expression.
> PMID 41303422 (2025): Telomere Maintenance and Oncogenesis.
> PMID 39141194 (2024): Novel method for detecting frequent TERT promoter hot spot mutations in bladder cancer samples.
> PMID 35568649 (2022): Emerging mechanisms of telomerase reactivation in cancer.
> PMID 38902506 (2024): Hidden secrets of the cancer genome: unlocking the impact of non-coding mutations in gene regulatory elements.
> PMID 33758097 (2021): Cancer-specific loss of <i>TERT</i> activation sensitizes glioblastoma to DNA damage.

<a id="e34a"></a>**E34a** literature_search, Europe PMC abstract, PMID 40513567 (https://europepmc.org/article/MED/40513567; retrieved 2026-10-26T02:34:39+00:00)

> TERT promoter (TERTp) mutations create a de novo E26 transformation-specific (ETS) transcription factor binding motif.

<a id="e34b"></a>**E34b** literature_search, Europe PMC abstract, PMID 40513567 (https://europepmc.org/article/MED/40513567; retrieved 2026-10-26T02:34:39+00:00)

> Here, we analyzed 53 cell lines representing 16 cancer types and 6 recurrent TERTp mutations and found that the GA-binding protein (GABP) tetramer is responsible for promoter activation in all cases.

<a id="e34c"></a>**E34c** literature_search, Europe PMC abstract, PMID 35568649 (https://europepmc.org/article/MED/35568649; retrieved 2026-10-26T02:34:39+00:00)

> Mutations in the promoter of human telomerase reverse transcriptase (hTERT) result in hyperactivation of hTERT.

<a id="e34d"></a>**E34d** literature_search, Europe PMC abstract, PMID 35568649 (https://europepmc.org/article/MED/35568649; retrieved 2026-10-26T02:34:39+00:00)

> Initially, the mutations were understood to reactivate hTERT by generating novel E26 transformation-specific (ETS) binding sites.

<a id="e34e"></a>**E34e** literature_search, Europe PMC abstract, PMID 33758097 (https://europepmc.org/article/MED/33758097; retrieved 2026-10-26T02:34:39+00:00)

> TERT promoter mutations create a binding site for a GA binding protein (GABP) transcription factor complex, whose assembly at the promoter is associated with TERT reactivation and telomere maintenance.
