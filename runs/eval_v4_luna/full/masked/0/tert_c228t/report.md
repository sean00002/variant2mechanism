# TERT promoter C228T and Glioblastoma, melanoma, bladder

Configuration `full`, masked mode, seed 0. Models: generator openai/gpt-6-luna, critic openai/gpt-6-luna, summariser openai/gpt-6-luna. Cost $0.02 over 14 model calls; 256 s.

Variant `chr5:1295113:G>A` (somatic); expression context: DepMap:subtype=Glioblastoma (median of 54 lines).

## QBiC-SELEX screen (occupancy first)

Occupied candidates: GABPA (bound elsewhere, z 166.19); ZIC2 (bound elsewhere, z -20.85); CTCF (bound elsewhere, z -14.7); ZBTB7A (bound elsewhere, z -14.11); NR2C1 (bound elsewhere, z -10.53); E2F4 (bound elsewhere, z 5.78); E2F6 (bound elsewhere, z 5.78); E2F5 (bound elsewhere, z 5.78); EGR1 (bound elsewhere, z -3.42, no clear allelic change); JUN (bound elsewhere, z 3.26, no clear allelic change). Occupancy unknown: ETV2 (z 166.19); ETV3 (z 166.19); FLI1 (z 166.19); TFAP2A (z -36.84); TFAP2C (z -36.84). Diagnostic, not shown to the model: 310 of 997 models pass Bonferroni.

## Ranked chains

### 1. H0: No TF-mediated effect of this variant (p = 0.90)

Null chain: no TF-mediated effect of this variant.

Predictions: The variant has no TF-mediated allelic effect; any disease association could reflect a linked change, background, or another process.; In a relevant model, precise editing may produce no reproducible allele-specific TF occupancy or regulatory change.

Falsified if: In a relevant cellular model, precise editing of this base reproducibly changes TF occupancy and produces an allele-dependent regulatory effect.

### 2. H1: Alt-increased ETS-family binding may affect TERT regulation (p = 0.04)

TF GABPA (QBiC-SELEX coverage own_model), alt allele binds more; element The variant lies in promoter-like cCRE EH38E3622530, but its activity in glioblastoma is not established.; gene TERT is the nearest annotated TSS, but regulation of TERT by this cCRE is unproven.; cell type Glioblastoma is the stated expression context; GABPA occupancy at the variant is not established there..

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | QBiC-SELEX predicts stronger in-vitro binding to alt using an ETV5-mapped ETS model shared by related factors. GABPA is expressed and has variant-overlapping peaks only in other biosamples; no peak was found in U-87 MG, so GABPA-specific occupancy in this glioblastoma model is unestablished. | weak | [E04](#e04), [E11](#e11), [E17](#e17), [E32](#e32), [E38](#e38) |
| element | The variant lies in a promoter-like cCRE with active-chromatin marks, but the reported marks are maxima across biosamples, not glioblastoma-specific measurements. | supported | [E03](#e03) |
| gene | TERT is the nearest annotated TSS, but neither proximity nor the absence of a significant brain-cortex eQTL demonstrates that this cCRE regulates TERT; the literature search returned no variant-specific functional result. | weak | [E01](#e01), [E02](#e02), [E36](#e36), [E40](#e40), [E40a](#e40a) |
| cell_type | GABPA is expressed in the stated glioblastoma context, but there is no matching-context ChIP peak at the variant, including in U-87 MG. | supported | [E04](#e04), [E11](#e11), [E32](#e32), [E38](#e38) |
| phenotype | TERT promoter alterations are relevant background in glioblastoma and melanoma, but the evidence does not link this variant or GABPA binding to a disease phenotype and provides no specific support for bladder cancer. | missing | [E15a](#e15a), [E15e](#e15e), [E15h](#e15h) |

Predictions: In an active glioblastoma model carrying both alleles, GABPA occupancy should be greater on alt than ref if GABPA is responsible for the ETS-family in-vitro signal.; If the variant has a regulatory effect through GABPA, that effect should be reduced by GABPA depletion; the direction of any TERT-expression change is not established.

Falsified if: A sensitive allele-resolved assay in an active, relevant model finds no greater GABPA occupancy on alt than ref.; Precise editing produces no reproducible GABPA-dependent regulatory effect in a model where the element is active.

### 3. H2: Reduced CTCF binding may affect local TERT regulation (p = 0.04)

TF CTCF (QBiC-SELEX coverage own_model), ref allele binds more; element The variant lies in promoter-like cCRE EH38E3622530, but its activity in glioblastoma is not established.; gene TERT is the nearest annotated TSS, but regulation of TERT by this cCRE is unproven.; cell type Glioblastoma is the stated expression context; CTCF occupancy at the variant is not established there..

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | CTCF's own QBiC-SELEX model predicts stronger in-vitro binding to ref. CTCF has a variant-overlapping peak in another biosample and is expressed in the glioblastoma context, but occupancy in glioblastoma is unestablished. | weak | [E04](#e04), [E13](#e13), [E19](#e19), [E33](#e33) |
| element | The variant lies in a promoter-like cCRE with active-chromatin marks, but the reported marks are maxima across biosamples, not glioblastoma-specific measurements. | supported | [E03](#e03) |
| gene | TERT is the nearest annotated TSS, but neither proximity nor the absence of a significant brain-cortex eQTL demonstrates that this cCRE regulates TERT; the literature search returned no variant-specific functional result. | weak | [E01](#e01), [E02](#e02), [E36](#e36), [E40](#e40), [E40a](#e40a) |
| cell_type | CTCF is expressed in the stated glioblastoma context, but no matching-context ChIP peak establishes occupancy at this site. | supported | [E04](#e04), [E13](#e13), [E33](#e33) |
| phenotype | TERT promoter alterations are relevant background in glioblastoma and melanoma, but the evidence does not link this variant or CTCF binding to a disease phenotype and provides no specific support for bladder cancer. | missing | [E15a](#e15a), [E15e](#e15e), [E15h](#e15h) |

Predictions: If CTCF occupies this base in an active glioblastoma model, occupancy should be greater on ref than alt.; If the variant has a regulatory effect through CTCF, that effect should be reduced by CTCF depletion; the direction of any TERT-expression change is not established.

Falsified if: A sensitive allele-resolved assay in an active, relevant model finds no greater CTCF occupancy on ref than alt.; Precise editing produces no reproducible CTCF-dependent regulatory effect in a model where the element is active.

### 4. H3: Alt-increased E2F-family binding may affect TERT regulation (p = 0.03)

TF E2F4 (QBiC-SELEX coverage own_model), alt allele binds more; element The variant lies in promoter-like cCRE EH38E3622530, but its activity in glioblastoma is not established.; gene TERT is the nearest annotated TSS, but regulation of TERT by this cCRE is unproven.; cell type Glioblastoma is the stated expression context; E2F4 occupancy at the variant is not established there..

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | QBiC-SELEX predicts a modest increase in in-vitro binding to alt using an E2F1-mapped model; the same prediction is assigned to E2F4, E2F5, and E2F6. E2F4 peaks overlap the site only in other biosamples, and none was found in U-87 MG, so E2F4-specific occupancy in glioblastoma is unestablished. | weak | [E04](#e04), [E09](#e09), [E22](#e22), [E23](#e23), [E24](#e24), [E35](#e35), [E39](#e39) |
| element | The variant lies in a promoter-like cCRE with active-chromatin marks, but the reported marks are maxima across biosamples, not glioblastoma-specific measurements. | supported | [E03](#e03) |
| gene | TERT is the nearest annotated TSS, but neither proximity nor the absence of a significant brain-cortex eQTL demonstrates that this cCRE regulates TERT; the literature search returned no variant-specific functional result. | weak | [E01](#e01), [E02](#e02), [E36](#e36), [E40](#e40), [E40a](#e40a) |
| cell_type | E2F4 is expressed in the stated glioblastoma context, but no matching-context ChIP peak establishes occupancy at this site, including in U-87 MG. | supported | [E04](#e04), [E09](#e09), [E35](#e35), [E39](#e39) |
| phenotype | TERT promoter alterations are relevant background in glioblastoma and melanoma, but the evidence does not link this variant or E2F4 binding to a disease phenotype and provides no specific support for bladder cancer. | missing | [E15a](#e15a), [E15e](#e15e), [E15h](#e15h) |

Predictions: If E2F4 is responsible for the in-vitro E2F-family signal and occupies this base in an active glioblastoma model, occupancy should be greater on alt than ref.; If the variant has a regulatory effect through E2F4, that effect should be reduced by E2F4 depletion; the direction of any TERT-expression change is not established.

Falsified if: A sensitive allele-resolved assay in an active, relevant model finds no greater E2F4 occupancy on alt than ref.; Precise editing produces no reproducible E2F4-dependent regulatory effect in a model where the element is active.

## Prediction matrix

| Test | Cost | Separates top two | H0 | H1 | H2 | H3 |
| --- | --- | --- | --- | --- | --- | --- |
| In an active glioblastoma model, perform allele-resolved CUT&RUN for GABPA and CTCF after precise isogenic editing to ref or alt. | medium | yes | No reproducible allele-specific occupancy difference attributable to the edited base. | GABPA occupancy is greater on alt than ref. | CTCF occupancy is greater on ref than alt. | Neither GABPA nor CTCF shows the predicted causal allele-specific occupancy; E2F4 would require a separate assay. |
| Precisely edit ref and alt in an active glioblastoma model, then assay TERT expression with and without depletion of GABPA, CTCF, or E2F4. | high | yes | No reproducible edit-dependent TERT-expression change, or no TF-depletion interaction. | An edit-dependent TERT-expression change is reduced by GABPA depletion; its direction is not specified. | An edit-dependent TERT-expression change is reduced by CTCF depletion; its direction is not specified. | An edit-dependent TERT-expression change is reduced by E2F4 depletion; its direction is not specified. |
| Measure allele-specific E2F4 occupancy in an active glioblastoma model after precise isogenic editing. | medium | no | No reproducible allele-specific E2F4 occupancy difference attributable to the edited base. | No E2F4-specific alt-increased occupancy is required. | No E2F4-specific alt-increased occupancy is required. | E2F4 occupancy is greater on alt than ref. |

## Next experiment

The cheapest direct discriminator for the top two non-null chains is targeted allele-resolved CUT&RUN for GABPA and CTCF in an active glioblastoma model after precise isogenic editing. H1 predicts greater GABPA occupancy on alt; H2 predicts greater CTCF occupancy on ref. A null-like result would leave both unsupported.

## Refinement rounds

Stopped: round limit (3).

### Round 1

- chip_peaks({"tf": "GABPA", "biosample": "glioblastoma"}) for H1.binding, ran as [E32](#e32). Expected: If GABPA has variant-overlapping peaks in a glioblastoma biosample, H1.binding gains context-matched occupancy support and H1 rises; if none are found, its binding claim remains based on indirect occupancy evidence.
- chip_peaks({"tf": "CTCF", "biosample": "glioblastoma"}) for H2.binding, ran as [E33](#e33). Expected: If CTCF has variant-overlapping peaks in a glioblastoma biosample, H2.binding gains context-matched occupancy support and H2 rises; if none are found, H2 remains weakly supported by other-biosample occupancy and in-vitro binding predictions.
- literature_search({"query": "chr5:1295113 G>A TERT promoter glioblastoma melanoma"}) for H1.phenotype, ran as [E34](#e34). Expected: If the search finds variant-specific functional or disease evidence, it could strengthen or redirect the phenotype link; if it finds only general TERT-promoter literature, the current phenotype rationale remains nonspecific.

- Result of chip_peaks({"tf":"GABPA","biosample":"glioblastoma"}): E32 reports no GABPA peak in a matching glioblastoma biosample; two overlapping peaks are reported in HepG2 and SK-N-SH. (as expected: yes)
- Result of chip_peaks({"tf":"CTCF","biosample":"glioblastoma"}): E33 reports no CTCF peak in a matching glioblastoma biosample; one overlapping peak is reported in DOHH2. (as expected: yes)
- Result of literature_search({"query":"chr5:1295113 G>A TERT promoter glioblastoma melanoma"}): E34 found no reported variant-specific functional or disease evidence in the listed results; the cited material is not specific to this variant. (as expected: yes)

Chains after revision: null 0.83; CTCF 0.07; GABPA 0.06; E2F4 0.04. Link grades changed: H1.gene: supported → weak, H1.phenotype: supported → weak, H2.gene: supported → weak, H2.phenotype: supported → weak, H3.gene: supported → weak, H3.phenotype: supported → weak.

### Round 2

- chip_peaks({"tf": "E2F4", "biosample": "glioblastoma"}) for H3.binding, ran as [E35](#e35). Expected: If variant-overlapping E2F4 ChIP peaks are found in a glioblastoma biosample, H3.binding gains relevant occupancy support and H3 rises; if none are found, the current occupancy limitation remains.
- eqtl_lookup({"tissue": "Brain - Cortex"}) for H1.gene, ran as [E36](#e36). Expected: If this variant is associated with TERT expression in brain cortex, H1.gene gains direct regulatory support and H1 rises; if no relevant eQTL is returned, the cCRE-to-TERT link remains unestablished.
- gene_disease({"gene": "TERT"}) for H1.phenotype, ran as [E37](#e37). Expected: If Open Targets reports strong TERT association with glioblastoma, melanoma, or bladder cancer, H1.phenotype gains disease-gene support; absent or weak associations leave the broad disease relevance unchanged.

- Result of chip_peaks({"tf":"E2F4","biosample":"glioblastoma"}): E35 reports no variant-overlapping E2F4 peak in a matching glioblastoma biosample; the reported peaks are from GM12878 and HepG2. (as expected: yes)
- Result of eqtl_lookup({"tissue":"Brain - Cortex"}): E36 reports zero significant GTEx v8 single-tissue eQTLs for this variant in Brain - Cortex, so the cCRE-to-TERT link remains unestablished. (as expected: yes)
- Result of gene_disease({"gene":"TERT"}): E37 reports that the Open Targets lookup failed; it provides no interpretable disease-association result. (as expected: unclear)

Chains after revision: null 0.86; GABPA 0.06; CTCF 0.05; E2F4 0.03. Link grades changed: H1.gene: weak → supported, H2.gene: weak → supported, H3.gene: weak → supported.

### Round 3

- chip_peaks({"tf": "GABPA", "biosample": "U-87 MG"}) for H1.binding, ran as [E38](#e38). Expected: A variant-overlapping GABPA peak in U-87 MG would add glioblastoma-model occupancy evidence to the alt-increased QBiC-SELEX prediction and strengthen H1.binding; no peak would leave occupancy unestablished and H1 weak.
- chip_peaks({"tf": "E2F4", "biosample": "U-87 MG"}) for H3.binding, ran as [E39](#e39). Expected: A variant-overlapping E2F4 peak in U-87 MG would add glioblastoma-model occupancy evidence to the alt-increased QBiC-SELEX prediction and strengthen H3.binding; no peak would further limit the occupancy case.
- literature_search({"query": "chr5:1295113 G>A TERT promoter glioblastoma reporter MPRA CRISPR"}) for H1.gene, ran as [E40](#e40). Expected: Variant-specific functional evidence showing that this site regulates TERT would strengthen the gene link and H1; evidence for another target or no variant-specific functional result would leave the TERT link unsupported or weaken it.

- Result of chip_peaks for GABPA in U-87 MG (H1.binding): E38 reports no variant-overlapping GABPA peak in U-87 MG; peaks are reported only in HepG2 and SK-N-SH. This leaves GABPA occupancy in the model unestablished. (as expected: yes)
- Result of chip_peaks for E2F4 in U-87 MG (H3.binding): E39 reports no variant-overlapping E2F4 peak in U-87 MG; peaks are reported only in GM12878 and HepG2. This further limits the occupancy case. (as expected: yes)
- Result of Literature search for chr5:1295113 G>A, TERT promoter, glioblastoma, reporter, MPRA, or CRISPR (H1.gene): E40 returned no variant-specific functional result; the quoted literature describes general MPRA methods rather than testing this variant or establishing a TERT link. (as expected: yes)

Chains after revision: null 0.90; GABPA 0.04; CTCF 0.04; E2F4 0.03. Link grades changed: H1.gene: supported → weak, H1.phenotype: weak → missing, H2.gene: supported → weak, H2.phenotype: weak → missing, H3.gene: supported → weak, H3.phenotype: weak → missing.

## Flags

- tool_failed: E37 gene_disease: Open Targets lookup failed: no disease matches 'Glioblastoma, melanoma, bladder'

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
> PMID 42804732 (2026): SNP rs[masked] potentially elevates the risk of glioblastoma development and leads to worse prognosis when in cis with mutant TERT promoter in a Japanese cohort.
> PMID 42807929 (2026): USP10 stabilizes FOXM1 through KAT5-mediated acetylation to suppress cell senescence and promote melanoma malignant progression.
> PMID 42859331 (2026): CDKN2A deletion associated with poor prognosis in patients with TERT promoter wild-type, IDH wild-type glioblastoma.

<a id="e15a"></a>**E15a** literature_search, Europe PMC abstract, PMID 41744838 (https://europepmc.org/article/MED/41744838; retrieved 2026-10-25T11:57:36+00:00)

> A major molecular feature of melanoma is abnormal telomerase activation; this is most often caused by telomerase reverse transcriptase (TERT) promoter mutations, which occur in 50-82% of cases and are the most common noncoding alteration in this cancer.

<a id="e15b"></a>**E15b** literature_search, Europe PMC abstract, PMID 41744838 (https://europepmc.org/article/MED/41744838; retrieved 2026-10-25T11:57:36+00:00)

> Conclusions: Understanding both telomere-dependent and -independent TERT functions is essential for developing effective biomarkers and therapies that overcome resistance and slow melanoma progression.

<a id="e15c"></a>**E15c** literature_search, Europe PMC abstract, PMID 42577103 (https://europepmc.org/article/MED/42577103; retrieved 2026-10-25T11:57:36+00:00)

> The genetic landscape of familial melanoma is heterogeneous.

<a id="e15d"></a>**E15d** literature_search, Europe PMC abstract, PMID 42577103 (https://europepmc.org/article/MED/42577103; retrieved 2026-10-25T11:57:36+00:00)

> CDKN2A and CDK4 mutations act through UV-dependent and cell cycle disruption pathways, while BAP1, POT1, and TERT mutations are considered UV-independent.

<a id="e15e"></a>**E15e** literature_search, Europe PMC abstract, PMID 42804732 (https://europepmc.org/article/MED/42804732; retrieved 2026-10-25T11:57:36+00:00)

> Mutations in the telomerase reverse transcriptase (TERT) promoter region (TPM), particularly C228T and C250T, are common in IDH-wildtype glioblastoma (GBM).

<a id="e15f"></a>**E15f** literature_search, Europe PMC abstract, PMID 42804732 (https://europepmc.org/article/MED/42804732; retrieved 2026-10-25T11:57:36+00:00)

> The rs[masked] C allele may increase GBM susceptibility and, when in cis with TPM, is associated with reduced TERT expression and poorer prognosis, underscoring its biological and clinical significance in TPM-mutant GBM.

<a id="e15g"></a>**E15g** literature_search, Europe PMC abstract, PMID 42807929 (https://europepmc.org/article/MED/42807929; retrieved 2026-10-25T11:57:36+00:00)

> Additionally, loss of either USP10 or FOXM1 suppresses the expression of the downstream target Telomerase reverse transcriptase (TERT), triggering cellular senescence.

<a id="e15h"></a>**E15h** literature_search, Europe PMC abstract, PMID 42859331 (https://europepmc.org/article/MED/42859331; retrieved 2026-10-25T11:57:36+00:00)

> TERT promoter (TERTp) mutations are among the most frequent molecular alterations in isocitrate dehydrogenase (IDH) wild-type glioblastoma (GBM), yet the molecular profiles and prognostic implications associated with TERTp status remain incompletely characterized.

<a id="e15i"></a>**E15i** literature_search, Europe PMC abstract, PMID 42859331 (https://europepmc.org/article/MED/42859331; retrieved 2026-10-25T11:57:36+00:00)

> The prognostic relevance of CDKN2A deletion may vary according to TERTp status, particularly for OS.

<a id="e16"></a>**E16** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> QBiC-SELEX screen of chr5:1295113:G>A, one line per TF, each with the TF's own or CIS-BP-mapped model of largest |z|. Candidates are TFs whose ENCODE ChIP-seq peaks contain the variant and that are expressed (DepMap subtype median Glioblastoma), bound here before bound elsewhere, then a strong site before a weak one, then by |z|; then expressed TFs ENCODE never assayed whose best model passes the gate (occupancy unknown). Shown: 10 of 20 occupied (15 with a strong site), 5 of 111 with unknown occupancy. Left out: 0 TFs assayed in the matching biosample and 552 assayed only elsewhere, none with a peak here; 1 bound but below 1 TPM. The gate (|z| > 4.05, Bonferroni over 997 models) marks a change QBiC-SELEX detects; it says nothing about occupancy. Effect > 0 means the alternate allele binds more strongly. In vitro binding only. Site strength is the better allele's best k-mer over the variant, as a percentile of the best model's k-mers; a strong site reaches the 97.5th. At a weak site the ChIP peak more likely reflects another site in the element.

<a id="e17"></a>**E17** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> GABPA (Ets, 18 models; QBiC-SELEX coverage: own model): best model ETV5_NA_TGCACT20NGA_ESAF_yang2017_1_3_6mer (a CIS-BP-mapped model of ETV5), z 166.19, effect 2.121: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 15.52 TPM, rank 303 of 1626 TFs in DepMap:subtype=Glioblastoma (median of 54 lines). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in HepG2, SK-N-SH, e.g. ENCSR000BJK. Best model's site strength: ref 97.1th, alt 99.3th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e18"></a>**E18** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> ZIC2 (C2H2 ZF, 4 models; QBiC-SELEX coverage: mapped models only): best model ZIC4_eDBD_TGCGTA40NTCA_KT_yin2017_1_3_7mer (a CIS-BP-mapped model of ZIC4), z -20.85, effect -0.916: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 3.7 TPM, rank 852 of 1626 TFs in DepMap:subtype=Glioblastoma (median of 54 lines). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in HEK293, e.g. ENCSR728MWW. Best model's site strength: ref 99.8th, alt 97.4th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e19"></a>**E19** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> CTCF (C2H2 ZF, 1 model; QBiC-SELEX coverage: own model): best model CTCF_FL_TG40NCTGTGG_YWL_jolma2025_0_3_7mer (its own model), z -14.7, effect -1.719: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 26.45 TPM, rank 163 of 1626 TFs in DepMap:subtype=Glioblastoma (median of 54 lines). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in DOHH2, e.g. ENCSR084RDK. Best model's site strength: ref 99.8th, alt 97.0th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e20"></a>**E20** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> ZBTB7A (C2H2 ZF, 1 model; QBiC-SELEX coverage: own model): best model ZBTB7A_eDBD_TTTGCT40NCGT_KR_yin2017_0_4_7mer (its own model), z -14.11, effect -0.826: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 8.49 TPM, rank 531 of 1626 TFs in DepMap:subtype=Glioblastoma (median of 54 lines). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in K562, e.g. ENCSR000BME. Best model's site strength: ref 99.9th, alt 99.9th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e21"></a>**E21** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> NR2C1 (Nuclear receptor, 29 models; QBiC-SELEX coverage: own model): best model FXR_NA_Lib1_NA_bhimsaria2023_0(3)_3_7mer (a CIS-BP-mapped model of NR1H4), z -10.53, effect -0.434: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 18.52 TPM, rank 251 of 1626 TFs in DepMap:subtype=Glioblastoma (median of 54 lines). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in GM12878, e.g. ENCSR784VIQ. Best model's site strength: ref 97.7th, alt 97.9th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e22"></a>**E22** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> E2F4 (E2F, 4 models; QBiC-SELEX coverage: own model): best model E2F1_NA_CAATT14N_ESU_yang2017_0_4_7mer (a CIS-BP-mapped model of E2F1), z 5.78, effect 0.464: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 58.31 TPM, rank 49 of 1626 TFs in DepMap:subtype=Glioblastoma (median of 54 lines). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in GM12878, HepG2, e.g. ENCSR000DYY. Best model's site strength: ref 98.9th, alt 99.5th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e23"></a>**E23** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> E2F6 (E2F, 4 models; QBiC-SELEX coverage: mapped models only): best model E2F1_NA_CAATT14N_ESU_yang2017_0_4_7mer (a CIS-BP-mapped model of E2F1), z 5.78, effect 0.464: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 17.63 TPM, rank 267 of 1626 TFs in DepMap:subtype=Glioblastoma (median of 54 lines). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in A549, K562, e.g. ENCSR000BLI. Best model's site strength: ref 98.9th, alt 99.5th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e24"></a>**E24** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> E2F5 (E2F, 4 models; QBiC-SELEX coverage: mapped models only): best model E2F1_NA_CAATT14N_ESU_yang2017_0_4_7mer (a CIS-BP-mapped model of E2F1), z 5.78, effect 0.464: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 6.91 TPM, rank 605 of 1626 TFs in DepMap:subtype=Glioblastoma (median of 54 lines). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in HepG2, e.g. ENCSR486JYI. Best model's site strength: ref 98.9th, alt 99.5th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e25"></a>**E25** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> EGR1 (C2H2 ZF, 4 models; QBiC-SELEX coverage: own model): best model EGR4_NA_TGCGCC20NCGC_Y_jolma2013_1_4_7mer (a CIS-BP-mapped model of EGR4), z -3.42, effect -0.541: ref allele binds slightly more; occupied, no clear allelic change (|z| below the gate). 28.32 TPM, rank 151 of 1626 TFs in DepMap:subtype=Glioblastoma (median of 54 lines). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in HepG2, Ishikawa, K562, e.g. ENCSR000BNE. Best model's site strength: ref 99.5th, alt 99.6th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e26"></a>**E26** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> JUN (bZIP, 3 models; QBiC-SELEX coverage: own model): best model JUND_eDBD_TCTCTA40NCAC_KS_yin2017_0_4_7mer (a CIS-BP-mapped model of JUND), z 3.26, effect 0.185: alt allele binds slightly more; occupied, no clear allelic change (|z| below the gate). 91.65 TPM, rank 16 of 1626 TFs in DepMap:subtype=Glioblastoma (median of 54 lines). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in A549, e.g. ENCSR022WVP. Best model's site strength: ref 98.5th, alt 94.9th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

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

<a id="e32"></a>**E32** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-25T11:58:44+00:00)

> No ENCODE GABPA ChIP-seq peak contains chr5:1295113:G>A in biosamples matching 'glioblastoma'. Absence can also mean no GABPA experiment in that biosample. In other biosamples, 2 GABPA peaks do contain the variant: HepG2, SK-N-SH (experiments ENCSR000BJK, ENCSR000BTG).

<a id="e33"></a>**E33** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-26T22:04:25+00:00)

> No ENCODE CTCF ChIP-seq peak contains chr5:1295113:G>A in biosamples matching 'glioblastoma'. Absence can also mean no CTCF experiment in that biosample. In other biosamples, 1 CTCF peaks do contain the variant: DOHH2 (experiments ENCSR084RDK).

<a id="e34"></a>**E34** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=chr5%3A1295113%20G%3EA%20TERT%20promoter%20glioblastoma%20melanoma&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T20:27:02+00:00)

> Europe PMC: 3 hits for 'chr5:1295113 G>A TERT promoter glioblastoma melanoma'; top 2 with PMIDs:
> PMID 40097403 (2025): Multi-omic analysis of SDHB-deficient pheochromocytomas and paragangliomas identifies metastasis and treatment-related molecular profiles.
> PMID 40841759 (2025): Leveraging sequences missing from the human genome to diagnose cancer.

<a id="e34a"></a>**E34a** literature_search, Europe PMC abstract, PMID 40097403 (https://europepmc.org/article/MED/40097403; retrieved 2026-10-26T20:27:02+00:00)

> TERT and ATRX-alterations are associated with metastatic PCPG and these tumours have an increased mutation load, and distinct transcriptional and telomeric features.

<a id="e34b"></a>**E34b** literature_search, Europe PMC abstract, PMID 40841759 (https://europepmc.org/article/MED/40841759; retrieved 2026-10-26T20:27:02+00:00)

> By testing various promoters or over 9000 candidate enhancer sequences with massively parallel reporter assays, we show that neomers can identify cancer-associated mutations that alter regulatory activity.

<a id="e35"></a>**E35** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-26T13:31:14+00:00)

> No ENCODE E2F4 ChIP-seq peak contains chr5:1295113:G>A in biosamples matching 'glioblastoma'. Absence can also mean no E2F4 experiment in that biosample. In other biosamples, 2 E2F4 peaks do contain the variant: GM12878, HepG2 (experiments ENCSR000DYY, ENCSR924LSO).

<a id="e36"></a>**E36** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr5_1295113_G_A_b38&datasetId=gtex_v8; retrieved 2026-10-26T20:18:37+00:00)

> 0 significant GTEx v8 single-tissue eQTLs for chr5_1295113_G_A_b38 in tissues matching 'Brain - Cortex'. NES is the effect of the alt allele (A) relative to ref (G).

<a id="e37"></a>**E37** gene_disease (failed), Open Targets (; retrieved local)

> Open Targets lookup failed: no disease matches 'Glioblastoma, melanoma, bladder'

<a id="e38"></a>**E38** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-25T11:58:44+00:00)

> No ENCODE GABPA ChIP-seq peak contains chr5:1295113:G>A in biosamples matching 'U-87 MG'. Absence can also mean no GABPA experiment in that biosample. In other biosamples, 2 GABPA peaks do contain the variant: HepG2, SK-N-SH (experiments ENCSR000BJK, ENCSR000BTG).

<a id="e39"></a>**E39** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-26T13:31:14+00:00)

> No ENCODE E2F4 ChIP-seq peak contains chr5:1295113:G>A in biosamples matching 'U-87 MG'. Absence can also mean no E2F4 experiment in that biosample. In other biosamples, 2 E2F4 peaks do contain the variant: GM12878, HepG2 (experiments ENCSR000DYY, ENCSR924LSO).

<a id="e40"></a>**E40** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=chr5%3A1295113%20G%3EA%20TERT%20promoter%20glioblastoma%20reporter%20MPRA%20CRISPR&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T22:07:02+00:00)

> Europe PMC: 2 hits for 'chr5:1295113 G>A TERT promoter glioblastoma reporter MPRA CRISPR'; top 1 with PMIDs:
> PMID 40841759 (2025): Leveraging sequences missing from the human genome to diagnose cancer.

<a id="e40a"></a>**E40a** literature_search, Europe PMC abstract, PMID 40841759 (https://europepmc.org/article/MED/40841759; retrieved 2026-10-26T22:07:02+00:00)

> By testing various promoters or over 9000 candidate enhancer sequences with massively parallel reporter assays, we show that neomers can identify cancer-associated mutations that alter regulatory activity.
