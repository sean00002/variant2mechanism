# rs73706717 and Colorectal cancer (8q24)

Configuration `full`, masked mode, seed 0. Models: generator openai/gpt-6-luna, critic openai/gpt-6-luna, summariser openai/gpt-6-luna. Cost $0.03 over 13 model calls; 255 s.

Variant `chr8:127401265:T>C` (germline); expression context: DepMap:ACH-000971 (HCT 116).

## QBiC-SELEX screen (occupancy first)

Occupied candidates: TCF7L2 (bound here, z -8.8, weak site); SP1 (bound here, z -7.07, weak site); NFIC (bound elsewhere, z 24.28); NFIA (bound elsewhere, z 24.28); HNF1B (bound elsewhere, z -23.93); CTCF (bound elsewhere, z 8.21); CEBPB (bound elsewhere, z -6.94); TFAP4 (bound elsewhere, z 0.51, no clear allelic change); NR2F2 (bound elsewhere, z -15.02, weak site); NR2F6 (bound elsewhere, z -15.02, weak site). Occupancy unknown: ZBTB22 (z -33.75); NR1H3 (z -15.02); TET3 (z 14.12); NR1D2 (z -13.82); NR4A2 (z -13.82). Diagnostic, not shown to the model: 307 of 997 models pass Bonferroni.

## Ranked chains

### 1. H0: Null: no TF-mediated effect of this variant (p = 0.78)

Null chain: no TF-mediated effect of this variant.

Predictions: The T and C alleles will not produce a reproducible TF-dependent regulatory difference attributable to this base.; Any colorectal-cancer relevance may arise through another variant or mechanism; the supplied evidence does not establish a colorectal-cancer effect of this variant.

Falsified if: An allele-dependent regulatory effect is reproducibly shown and depends on a TF whose binding or activity is altered by this base.

### 2. H1: Possible TCF7L2-mediated effect; predicted binding is stronger on T (p = 0.16)

TF TCF7L2 (QBiC-SELEX coverage mapped), ref allele binds more; element EH38E3858447; gene POU5F1B; cell type HCT116.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | TCF7L2 is expressed and has a ChIP-seq peak overlapping the variant in HCT116. A TCF7-mapped, not TCF7L2-specific, QBiC-SELEX model predicts stronger binding to ref T than alt C; the modeled site is weak, and the peak may reflect binding elsewhere in the element rather than at this base. | weak | [E05](#e05), [E20](#e20), [E39](#e39) |
| element | The variant lies in pELS cCRE EH38E3858447, but the reported activity scores are maxima across biosamples and do not establish activity in HCT116. | supported | [E03](#e03) |
| gene | POU5F1B is a candidate target based on proximity and low-PIP prioritization for other traits, but no supplied evidence links this element to POU5F1B or shows a variant-dependent expression effect; GTEx reports no significant eQTL. | weak | [E02](#e02), [E16](#e16), [E17](#e17) |
| cell_type | HCT116 is a plausible context because TCF7L2 expression and a peak overlapping the variant are reported there; allele-specific occupancy and occupancy at the variant base itself have not been established. | supported | [E05](#e05), [E20](#e20) |
| phenotype | POU5F1B has gene-level colorectal-cancer association evidence, but the supplied evidence does not connect this variant or a TCF7L2-mediated effect to colorectal-cancer risk. | supported | [E36](#e36), [E15](#e15) |

Predictions: If TCF7L2 binds the variant base in HCT116, T should show greater occupancy than C; this binding prediction does not determine the direction of transcriptional activity.; A variant-dependent regulatory effect attributed to TCF7L2 should diminish when TCF7L2 is depleted.

Falsified if: With confirmed TCF7L2 occupancy at the variant base, repeated allele-specific assays show no T-versus-C occupancy difference.; A reproducible variant-dependent regulatory effect persists unchanged after TCF7L2 depletion.

### 3. H4: Possible CTCF-mediated effect with predicted stronger binding on C; HCT116 occupancy is not reported (p = 0.04)

TF CTCF (QBiC-SELEX coverage own_model), alt allele binds more; element EH38E3858447; gene POU5F1B; cell type HCT116.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | CTCF has an expressed, strong-site QBiC-SELEX model predicting stronger binding to alt C. ENCODE reports variant-overlapping CTCF peaks in other biosamples, but none in HCT116; the new HCT116 search likewise reports no such peak. | weak | [E07](#e07), [E25](#e25), [E41](#e41) |
| element | The variant lies in pELS cCRE EH38E3858447, and CTCF is among the biosample-maximal scores; activity in HCT116 is not established. | supported | [E03](#e03) |
| gene | POU5F1B is a candidate based on proximity and low-PIP prioritization for other traits, but the evidence does not establish a CTCF-dependent connection from this element to POU5F1B. | weak | [E02](#e02), [E16](#e16), [E17](#e17) |
| cell_type | HCT116 is speculative for this chain: CTCF is expressed there, but no variant-overlapping CTCF peak is reported in that biosample. | weak | [E07](#e07), [E25](#e25), [E41](#e41) |
| phenotype | POU5F1B has gene-level colorectal-cancer association evidence, but no supplied evidence connects this variant or a CTCF-mediated effect to colorectal-cancer risk. | supported | [E36](#e36), [E15](#e15) |

Predictions: If CTCF occupies the variant in a relevant context, C should show greater CTCF binding than T.; A variant-dependent regulatory or chromatin effect attributed to CTCF should diminish after CTCF depletion; the binding prediction alone does not determine transcriptional direction.

Falsified if: With confirmed CTCF occupancy at the variant in a relevant context, repeated allele-specific assays show no greater occupancy on C than T.; A reproducible variant-dependent regulatory effect persists unchanged after CTCF depletion.

### 4. H3: Possible NFIC-mediated gain of binding on C; relevant-cell occupancy is unconfirmed (p = 0.02)

TF NFIC (QBiC-SELEX coverage own_model), alt allele binds more; element EH38E3858447; gene POU5F1B; cell type HCT116.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | An NFIB-mapped QBiC-SELEX model predicts stronger binding to alt C at a strong modeled site, but it is not an NFIC-specific model. NFIC occupancy overlapping the variant is reported in HepG2, not HCT116. | weak | [E22](#e22), [E35](#e35) |
| element | The variant lies in pELS cCRE EH38E3858447; biosample-maximal scores do not confirm activity in HCT116. | supported | [E03](#e03) |
| gene | POU5F1B is a candidate based on proximity and low-PIP prioritization for other traits, but an enhancer-to-gene connection and a variant-dependent expression effect are not established. | weak | [E02](#e02), [E16](#e16), [E17](#e17) |
| cell_type | HCT116 is speculative for this chain: NFIC is expressed there, but no matching-biosample peak overlapping the variant is reported; the reported NFIC peak is from HepG2. | weak | [E04](#e04), [E22](#e22), [E35](#e35) |
| phenotype | POU5F1B has gene-level colorectal-cancer association evidence, but no supplied evidence connects this variant or an NFIC-mediated effect to colorectal-cancer risk. | supported | [E36](#e36), [E15](#e15) |

Predictions: If NFIC occupies the variant in a relevant cell context, C should show greater NFIC binding than T.; An NFIC-dependent regulatory effect should require NFIC occupancy and diminish after NFIC depletion.

Falsified if: NFIC occupancy is confirmed in a relevant context, but repeated allele-specific assays show no greater occupancy on C than T.; A reproducible variant-dependent regulatory effect persists unchanged after NFIC depletion.

## Prediction matrix

| Test | Cost | Separates top two | H0 | H1 | H4 | H3 |
| --- | --- | --- | --- | --- | --- | --- |
| Test matched T- and C-allele EH38E3858447 reporters in HCT116, with and without TCF7L2 depletion. | medium | yes | No reproducible allele-dependent reporter difference attributable to this base. | A reporter difference is expected; if TCF7L2 mediates it, the difference should diminish after TCF7L2 depletion. The direction of reporter activity is not determined by the binding prediction. | No TCF7L2-dependent allele difference is specifically predicted; a CTCF-dependent effect would require separate testing. | No TCF7L2-dependent allele difference is specifically predicted; an NFIC-dependent difference would require separate testing. |
| Measure allele-specific TCF7L2 occupancy at the edited locus in HCT116, for example by targeted CUT&RUN or CUT&Tag. | medium | no | No reproducible T-versus-C occupancy difference attributable to the variant. | If TCF7L2 binds the variant base, occupancy should be greater on T than C. | No TCF7L2-specific allelic difference is predicted. | No TCF7L2-specific allelic difference is predicted. |
| Test NFIC occupancy and allele-specific binding at the edited locus in a relevant colorectal-cell context. | medium | no | No reproducible NFIC-dependent allelic binding difference attributable to the variant. | No NFIC-specific effect is predicted. | No NFIC-specific effect is predicted. | If NFIC occupies the site, binding should be greater on C than T. |
| Test CTCF occupancy and allele-specific binding at the edited locus in HCT116. | medium | no | No reproducible CTCF-dependent allelic binding difference attributable to the variant. | No CTCF-specific effect is predicted. | If CTCF occupies the site, binding should be greater on C than T. | No CTCF-specific effect is predicted. |

## Next experiment

Run the matched-allele EH38E3858447 reporter assay in HCT116 with and without TCF7L2 depletion. It is the lowest-cost proposed functional test of the two highest-probability chains: H1 predicts an allele-dependent effect that is reduced by TCF7L2 depletion, whereas H0 predicts no reproducible allele-dependent effect attributable to this base.

## Refinement rounds

Stopped: round limit (3).

### Round 1

- chip_peaks({"tf": "NFIC", "biosample": "HCT116"}) for H3.binding, ran as [E35](#e35). Expected: If NFIC ChIP-seq peaks contain the variant in HCT116, H3.binding and H3.cell_type gain occupancy support and H3 rises; if no peak is found, the HCT116 occupancy gap remains and H3 falls.
- gene_disease({"gene": "POU5F1B"}) for H1.phenotype, ran as [E36](#e36). Expected: If Open Targets shows colorectal-cancer association evidence for POU5F1B, H1.phenotype gains support and H1 rises modestly; if it shows no relevant association, the phenotype link remains weak.
- literature_search({"query": "POU5F1B colorectal cancer regulatory variant enhancer"}) for H1.gene, ran as [E37](#e37). Expected: If the literature reports direct evidence linking this element or a nearby regulatory variant to POU5F1B in colorectal cells, H1.gene gains support and H1 rises; if results only provide broad candidate-gene context or unrelated mechanisms, the link remains weak.

- Result of chip_peaks({"tf":"NFIC","biosample":"HCT116"}): E35 reports no NFIC ChIP-seq peak containing the variant in matching-biosample HCT116; the single reported overlapping NFIC peak is in HepG2. The evidence notes that absence may also reflect no NFIC experiment in HCT116. (as expected: yes)
- Result of gene_disease({"gene":"POU5F1B"}): E36 gives POU5F1B an Open Targets colorectal-cancer overall score of 0.54, with genetic-association evidence 0.87, literature 0.18, and RNA-expression evidence 0.14. This is gene-level support, not evidence that this variant acts through POU5F1B. (as expected: yes)
- Result of literature_search({"query":"POU5F1B colorectal cancer regulatory variant enhancer"}): E37 reports broad literature on POU5F1B and cancer and a study prioritizing CRC functional variants and target genes, but no direct evidence linking this element or a nearby regulatory variant to POU5F1B in colorectal cells. (as expected: yes)

Chains after revision: null 0.55; TCF7L2 0.25; SP1 0.16; NFIC 0.04. Link grades changed: H1.phenotype: weak → supported, H2.binding: supported → weak, H2.phenotype: weak → supported, H3.phenotype: weak → supported.

### Round 2

- qbic_tf_detail({"tf": "SP1"}) for H2.binding, ran as [E38](#e38). Expected: If an SP1-specific model independently predicts stronger binding to ref T, H2.binding becomes better supported and H2 gains ground against H1; if only the SP3-mapped result is available or the SP1-specific prediction is weak, H2 remains indirect and falls relative to H1.
- qbic_tf_detail({"tf": "TCF7L2"}) for H1.binding, ran as [E39](#e39). Expected: If a TCF7L2-specific model supports stronger binding to ref T, H1.binding is strengthened; if support is only from a mapped model or is inconsistent, H1 loses ground relative to H2.
- literature_search({"query": "chr8:127401265 POU5F1B colorectal cancer regulatory variant enhancer"}) for H1.gene, ran as [E40](#e40). Expected: If the search finds direct evidence connecting this variant or its element to POU5F1B in colorectal cells, H1.gene strengthens and the POU5F1B-target chains gain support; if not, the target-gene link remains speculative.

- Result of qbic_tf_detail({"tf":"SP1"}): The SP1-specific model predicts essentially no allelic change (effect -0.007, z -0.11, below the detection gate). The stronger ref-binding predictions come from SP3- and SP9-mapped models, not the SP1-specific model. (as expected: yes)
- Result of qbic_tf_detail({"tf":"TCF7L2"}): The TCF7L2-specific model is unavailable. A TCF7-mapped model predicts stronger ref binding, but the site is weak; LEF1- and TCF7L1-mapped models also give sub-gate predictions. This leaves the TCF7L2-specific inference indirect. (as expected: yes)
- Result of literature_search({"query":"chr8:127401265 POU5F1B colorectal cancer regulatory variant enhancer"}): The search returned no hits directly connecting this variant or its element to POU5F1B in colorectal cells. (as expected: yes)

Chains after revision: null 0.70; TCF7L2 0.19; CTCF 0.09; NFIC 0.03. Link grades changed: H1.binding: supported → weak, H1.gene: weak → supported, H2.binding: weak → absent, H2.cell_type: supported → absent, H2.element: supported → absent, H2.gene: weak → absent, H2.phenotype: supported → absent, H3.cell_type: weak → supported, H3.gene: weak → supported, H4.binding: absent → weak, H4.cell_type: absent → supported, H4.element: absent → supported, H4.gene: absent → supported, H4.phenotype: absent → supported.

### Round 3

- chip_peaks({"tf": "CTCF", "biosample": "HCT116"}) for H4.binding, ran as [E41](#e41). Expected: If a CTCF peak contains the variant in HCT116, this strengthens the occupancy support for the predicted alt-C binding effect and raises H4.binding; if none is reported, H4 remains weak and the HCT116 chain loses support.
- literature_search({"query": "chr8:127401265 T>C colorectal cancer POU5F1B functional enhancer allele-specific"}) for H1.gene, ran as [E42](#e42). Expected: If this finds variant-specific evidence linking the element to POU5F1B or a functional effect in colorectal cells, H1.gene strengthens and the non-null chain gains support; if not, the gene link remains unestablished.

- Result of chip_peaks(tf=CTCF, biosample=HCT116) for H4.binding: E41 reports no CTCF ChIP-seq peak containing the variant in HCT116; variant-overlapping peaks are reported only in other biosamples. (as expected: yes)
- Result of literature_search(query=chr8:127401265 T>C colorectal cancer POU5F1B functional enhancer allele-specific) for H1.gene: E42 reports zero literature hits for the query; no variant-specific enhancer-to-POU5F1B or allele-specific functional evidence was found. (as expected: yes)

Chains after revision: null 0.78; TCF7L2 0.16; CTCF 0.04; NFIC 0.02. Link grades changed: H1.gene: supported → weak, H3.cell_type: supported → weak, H3.gene: supported → weak, H4.cell_type: supported → weak, H4.gene: supported → weak.

## Flags

- none

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

> A few potential regulatory influences on CRC development associated with genes and variants, such as POU5F1B and rs[masked], were identified.

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

<a id="e35"></a>**E35** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-26T13:23:02+00:00)

> No ENCODE NFIC ChIP-seq peak contains chr8:127401265:T>C in biosamples matching 'HCT116'. Absence can also mean no NFIC experiment in that biosample. In other biosamples, 1 NFIC peaks do contain the variant: HepG2 (experiments ENCSR000BQX).

<a id="e36"></a>**E36** gene_disease, Open Targets Platform (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-26T02:23:32+00:00)

> Open Targets: POU5F1B and colorectal cancer (MONDO_0005575), overall score 0.54; by evidence type: genetic_association 0.87, literature 0.18, rna_expression 0.14

<a id="e37"></a>**E37** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=POU5F1B%20colorectal%20cancer%20regulatory%20variant%20enhancer&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T20:33:36+00:00)

> Europe PMC: 41 hits for 'POU5F1B colorectal cancer regulatory variant enhancer'; top 8 with PMIDs:
> PMID 41796348 (2026): Harnessing the LncRNA CCAT2 role in gastric cancer: from molecular insights to clinical implications.
> PMID 42686757 (2026): Phase separation of ecDNA condensates establishes in-trans contact domains that boost selective MYC regulatory interactions.
> PMID 41993623 (2026): Tailorable porous collagen hydrogels as a physiologically relevant platform for extrachromosomal DNA-associated colorectal cancer research.
> PMID 42704849 (2026): Large-scale pleiotropic analysis across cancers reveals shared genetic mechanisms and identifies novel functional genes.
> PMID 42562996 (2026): Functional roles and clinical implications of pseudogenes signatures as emerging biomarkers in cancer.
> PMID 40498368 (2025): CCAT2 role in gastrointestinal cancer progression and metastasis: a novel target for therapeutic strategies.
> PMID 39284974 (2024): Systematic prioritization of functional variants and effector genes underlying colorectal cancer risk.
> PMID 38902506 (2024): Hidden secrets of the cancer genome: unlocking the impact of non-coding mutations in gene regulatory elements.

<a id="e37a"></a>**E37a** literature_search, Europe PMC abstract, PMID 42704849 (https://europepmc.org/article/MED/42704849; retrieved 2026-10-26T20:33:36+00:00)

> Through pairwise pleiotropic analysis, we identified 75 243 significant pleiotropic single nucleotide polymorphisms (SNPs) across 372 cancer pairs, among which 3472 were lead SNPs with potential regulatory functions.

<a id="e37b"></a>**E37b** literature_search, Europe PMC abstract, PMID 42704849 (https://europepmc.org/article/MED/42704849; retrieved 2026-10-26T20:33:36+00:00)

> Notably, genes such as TERT (5p15.33), POU5F1B (8q24.21), and FANCA (16q24.3) exhibited widespread pleiotropy across multiple cancer types.

<a id="e37c"></a>**E37c** literature_search, Europe PMC abstract, PMID 39284974 (https://europepmc.org/article/MED/39284974; retrieved 2026-10-26T20:33:36+00:00)

> Here, we perform statistical fine-mapping incorporating tissue-specific epigenetic annotations and massively parallel reporter assays to systematically prioritize functional variants for each CRC risk locus.

<a id="e37d"></a>**E37d** literature_search, Europe PMC abstract, PMID 39284974 (https://europepmc.org/article/MED/39284974; retrieved 2026-10-26T20:33:36+00:00)

> We link these variants to 208 target genes by analyzing colon-specific quantitative trait loci and implementing the activity-by-contact model, which integrates epigenomic features and Micro-C data, to predict enhancer-gene connections.

<a id="e38"></a>**E38** qbic_tf_detail, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> {"tf":"SP1","symbol":"SP1","via":"hgnc_symbol","notes":[],"coverage":"own_model","variant":"chr8:127401265:T>C","gate_p":5.02e-05,"models":[{"model":"SP1_eDBD_TCTCTA40NCAC_KV_yin2017_0_3_7mer","mapping":"own","group":"G015 C2H2 ZF, 5 models","quality":0.891,"effect":-0.007,"z":-0.11,"p":0.91,"rank_abs_z":"975/997","passed_gate":false,"site_strength":{"ref_percentile":97.2,"alt_percentile":97.4,"k":7}},{"model":"SP3_eDBD_TTCACC40NGCT_KR_yin2017_0_3_7mer","mapping":"CIS-BP (SP3)","group":"G015 C2H2 ZF, 5 models","quality":0.813,"effect":-0.298,"z":-7.07,"p":1.5e-12,"rank_abs_z":"117/997","passed_gate":true,"site_strength":{"ref_percentile":90.4,"alt_percentile":75.6,"k":7}},{"model":"SP4_NA_TTATGT20NGTA_ESAE_yang2017_0_3_7mer","mapping":"CIS-BP (SP4)","group":"G015 C2H2 ZF, 5 models","quality":0.825,"effect":-0.111,"z":-2.06,"p":0.04,"rank_abs_z":"566/997","passed_gate":false,"site_strength":{"ref_percentile":65.1,"alt_percentile":79.1,"k":7}},{"model":"SP8_NA_TGCTCG20NCTC_ESY_yang2017_0_4_7mer","mapping":"CIS-BP (SP8)","group":"G015 C2H2 ZF, 5 models","quality":0.672,"effect":-0.048,"z":-0.66,"p":0.51,"rank_abs_z":"848/997","passed_gate":false,"site_strength":{"ref_percentile":88.7,"alt_percentile":84.7,"k":7}},{"model":"SP9_eDBD_TACCGA40NATA_KP_yin2017_0_4_7mer","mapping":"CIS-BP (SP9)","group":"G015 C2H2 ZF, 5 models","quality":0.936,"effect":-0.485,"z":-6.42,"p":1.3e-10,"rank_abs_z":"143/997","passed_gate":true,"site_strength":{"ref_percentile":70.8,"alt_percentile":67.5,"k":7}}]}

<a id="e39"></a>**E39** qbic_tf_detail, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> {"tf":"TCF7L2","symbol":"TCF7L2","via":"hgnc_symbol","notes":[],"coverage":"mapped","variant":"chr8:127401265:T>C","gate_p":5.02e-05,"models":[{"model":"LEF1_FL_TAGTCG40NAGA_KZ_yin2017_0_3_7mer","mapping":"CIS-BP (LEF1)","group":"G041 HMG/Sox, 3 models","quality":0.63,"effect":-0.306,"z":-2.77,"p":0.0056,"rank_abs_z":"461/997","passed_gate":false,"site_strength":{"ref_percentile":81.3,"alt_percentile":95.3,"k":7}},{"model":"TCF7_eDBD_TCGGAC40NCCA_KS_yin2017_0_3_7mer","mapping":"CIS-BP (TCF7)","group":"G041 HMG/Sox, 3 models","quality":0.732,"effect":-0.429,"z":-8.8,"p":1.4e-18,"rank_abs_z":"66/997","passed_gate":true,"site_strength":{"ref_percentile":90.0,"alt_percentile":87.2,"k":7}},{"model":"TCF7L1_eDBD_TTGGCA40NTCG_KW_yin2017_0_3_7mer","mapping":"CIS-BP (TCF7L1)","group":"G041 HMG/Sox, 3 models","quality":0.602,"effect":-0.242,"z":-3.57,"p":0.00036,"rank_abs_z":"359/997","passed_gate":false,"site_strength":{"ref_percentile":84.6,"alt_percentile":58.3,"k":7}}]}

<a id="e40"></a>**E40** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=chr8%3A127401265%20POU5F1B%20colorectal%20cancer%20regulatory%20variant%20enhancer&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T22:18:05+00:00)

> Europe PMC: 0 hits for 'chr8:127401265 POU5F1B colorectal cancer regulatory variant enhancer'; top 0 with PMIDs:

<a id="e41"></a>**E41** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-26T13:23:02+00:00)

> No ENCODE CTCF ChIP-seq peak contains chr8:127401265:T>C in biosamples matching 'HCT116'. Absence can also mean no CTCF experiment in that biosample. In other biosamples, 34 CTCF peaks do contain the variant: A549, C4-2B, Panc1, RWPE2, adrenal gland, astrocyte, brain, breast epithelium, endothelial cell, epithelial cell of prostate, esophagus squamous epithelium, excitatory neuron, left lung, mesothelial cell of epicardium, middle frontal area 46, stomach, testis, thoracic aorta, tibial nerve (experiments ENCSR031PXV, ENCSR037GKL, ENCSR073BPG, ENCSR130TQM, ENCSR173IEA, ENCSR188XCX).

<a id="e42"></a>**E42** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=chr8%3A127401265%20T%3EC%20colorectal%20cancer%20POU5F1B%20functional%20enhancer%20allele-specific&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T22:19:33+00:00)

> Europe PMC: 0 hits for 'chr8:127401265 T>C colorectal cancer POU5F1B functional enhancer allele-specific'; top 0 with PMIDs:
