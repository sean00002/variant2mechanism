# TERT promoter C228T and Glioblastoma, melanoma, bladder

Configuration `full`, named mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.04 over 8 model calls; 128 s.

Variant `chr5:1295113:G>A` (somatic); expression context: DepMap:subtype=Glioblastoma (median of 54 lines).

## QBiC-SELEX screen (occupancy first)

Occupied candidates: GABPA (bound elsewhere, z 166.19); ZIC2 (bound elsewhere, z -20.85); CTCF (bound elsewhere, z -14.7); ZBTB7A (bound elsewhere, z -14.11); NR2C1 (bound elsewhere, z -10.53); E2F4 (bound elsewhere, z 5.78); E2F6 (bound elsewhere, z 5.78); E2F5 (bound elsewhere, z 5.78); EGR1 (bound elsewhere, z -3.42, no clear allelic change); JUN (bound elsewhere, z 3.26, no clear allelic change). Occupancy unknown: ETV2 (z 166.19); ETV3 (z 166.19); FLI1 (z 166.19); TFAP2A (z -36.84); TFAP2C (z -36.84). Diagnostic, not shown to the model: 310 of 997 models pass Bonferroni.

## Ranked chains

### 1. H1: GABPA binds the C228T alt allele and activates TERT in glioblastoma (p = 0.57)

TF GABPA (QBiC-SELEX coverage own_model), alt allele binds more; element TERT promoter cCRE EH38E3622530; gene TERT; cell type Glioblastoma.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | GABPA binds the alt A allele more strongly than the ref G allele at chr5:1295113. GABPA's own QBiC-SELEX model shows an alt increase (effect +4.01, z 68.47), and additional Ets models show the same direction. GABPA ChIP-seq peaks over the variant are reported in HepG2/SK-N-SH, and literature reports GABPA/GABPB1 activation of the mutant TERT promoter in glioblastoma. Direct GABPA occupancy in a glioblastoma biosample is still not shown in the provided ENCODE data. | weak | [E34](#e34), [E32](#e32), [E33e](#e33e), [E04](#e04) |
| element | The variant lies in promoter-like cCRE EH38E3622530 within the TERT promoter, an active promoter element. | supported | [E01](#e01), [E03](#e03) |
| gene | This promoter element is at the TERT TSS (0.0 kb upstream; TERT upstream_gene_variant). | supported | [E01](#e01), [E02](#e02) |
| cell_type | Glioblastoma is the relevant context: GABPA is expressed in DepMap glioblastoma lines (15.52 TPM), and literature places GABPA/GABPB1 at the mutant TERT promoter in glioblastoma. | supported | [E17](#e17), [E33e](#e33e), [E33f](#e33f) |
| phenotype | GABPA/GABPB1 activation of the mutant TERT promoter increases telomerase; GABPA depletion or GABPB1 knockdown inhibits telomerase and tumorigenic potential of glioblastoma cells, and TERT promoter mutations mark poor prognosis. | supported | [E33e](#e33e), [E33f](#e33f), [E33a](#e33a) |

Predictions: Allele-specific GABPA ChIP in glioblastoma cells should show higher GABPA occupancy on the alt allele.; TERT mRNA or telomerase activity should be higher on the alt allele, and GABPA knockdown should reduce alt-driven TERT expression.; A GABPA ChIP-seq peak over chr5:1295113 should be detectable in matching glioblastoma biosamples.

Falsified if: GABPA binding at this base is not allele-specific in glioblastoma cells.; The alt allele does not increase TERT expression, or the effect persists after GABPA depletion.; GABPA is not expressed or cannot occupy the TERT promoter in the relevant glioblastoma context.

### 2. H5: No TF-mediated allelic effect at this base (p = 0.22)

Null chain: no TF-mediated effect of this variant.

Predictions: There is no allele-specific TF occupancy or allele-specific reporter activity at chr5:1295113 in the relevant cells.; Any TERT association is due to a linked causal variant, a passenger mutation, or another mechanism not mediated by a TF binding this base.; TERT expression is not allele-specific at this position in glioblastoma cells.

Falsified if: Allele-specific GABPA or another Ets-factor binding at chr5:1295113 is demonstrated in glioblastoma cells.; The alt allele increases TERT expression in an allele-specific reporter assay, and the effect is abolished by mutating the TF site or depleting the TF.

### 3. H3: CTCF binds the ref allele more strongly and loss of a repressive CTCF site on the alt allele derepresses TERT (p = 0.09)

TF CTCF (QBiC-SELEX coverage own_model), ref allele binds more; element TERT promoter cCRE EH38E3622530; gene TERT; cell type Glioblastoma.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | CTCF binds the ref G allele more strongly than the alt A allele; the CTCF own QBiC-SELEX model shows ref preference (z -14.7, effect -1.719). The only ENCODE CTCF peak over this variant is in DOHH2, not glioblastoma. | weak | [E19](#e19), [E13](#e13), [E04](#e04) |
| element | The variant lies in promoter-like cCRE EH38E3622530 in the TERT promoter. | supported | [E01](#e01), [E03](#e03) |
| gene | The element is immediately upstream of TERT, 0 kb from the TSS. | supported | [E01](#e01), [E02](#e02) |
| cell_type | CTCF is expressed in glioblastoma DepMap lines (26.45 TPM), but CTCF occupancy at this promoter in glioblastoma is not shown. | weak | [E19](#e19), [E04](#e04) |
| phenotype | If CTCF repressed TERT at this promoter, reduced CTCF binding on the alt allele could derepress TERT and promote disease; there is no direct evidence for CTCF repression here. | missing | none |

Predictions: CTCF ChIP should show higher ref-allele occupancy at chr5:1295113 in a cell type where CTCF binds this promoter.; If CTCF is repressive, the alt allele should increase TERT expression when CTCF is present.; CTCF knockdown or mutation of the CTCF site should mimic the alt allele.

Falsified if: CTCF does not occupy the TERT promoter in glioblastoma cells.; CTCF binding is not allele-specific at this base.; CTCF acts as an activator rather than a repressor at this promoter, reversing the predicted direction.

### 4. H2: ETV3, another Ets factor, binds the alt allele and activates TERT (p = 0.06)

TF ETV3 (QBiC-SELEX coverage own_model), alt allele binds more; element TERT promoter cCRE EH38E3622530; gene TERT; cell type Glioblastoma.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | ETV3 is a candidate Ets factor that would bind the alt A allele more strongly, based on a CIS-BP-mapped ETV5 Ets model (z 166.19, effect 2.121 alt). ETV3 has no ENCODE ChIP occupancy over this variant, and the mapped model is shared with other Ets factors, so this is weak and cannot distinguish ETV3 from GABPA. | weak | [E28](#e28) |
| element | The variant lies in promoter-like cCRE EH38E3622530 in the TERT promoter. | supported | [E01](#e01), [E03](#e03) |
| gene | The element is 0 kb from the TERT TSS and is annotated as a TERT upstream promoter variant. | supported | [E01](#e01), [E02](#e02) |
| cell_type | ETV3 is expressed at low level in glioblastoma DepMap lines (8.69 TPM), but no occupancy or TERT-promoter activity is shown in this context. | weak | [E28](#e28) |
| phenotype | If ETV3 occupied the alt allele, increased ETV3-driven TERT transcription could contribute to disease; this is speculative because occupancy is not shown. | missing | none |

Predictions: ETV3 ChIP in glioblastoma cells should show allele-specific occupancy at chr5:1295113.; ETV3 knockdown should reduce alt-driven TERT expression if this chain is correct.; The alt allele should increase ETV3-dependent reporter activity through the Ets motif.

Falsified if: ETV3 does not occupy the TERT promoter in glioblastoma cells.; ETV3 depletion does not affect TERT expression from the alt allele.; The allelic effect is fully explained by GABPA rather than ETV3.

### 5. H4: TFAP2A binds the ref allele more strongly and loss of TFAP2A binding on the alt allele increases TERT (p = 0.06)

TF TFAP2A (QBiC-SELEX coverage own_model), ref allele binds more; element TERT promoter cCRE EH38E3622530; gene TERT; cell type Glioblastoma.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | TFAP2A binds the ref G allele more strongly than the alt A allele; a CIS-BP-mapped TFAP2E AP-2 model shows ref preference (z -36.84, effect -1.289). TFAP2A occupancy over this variant is not shown, and the mapped model is shared with TFAP2C. | weak | [E30](#e30) |
| element | The variant lies in promoter-like cCRE EH38E3622530 in the TERT promoter. | supported | [E01](#e01), [E03](#e03) |
| gene | The element is 0 kb from the TERT TSS. | supported | [E01](#e01), [E02](#e02) |
| cell_type | TFAP2A is expressed in glioblastoma DepMap lines (9.65 TPM), but its occupancy at this promoter is not established. | weak | [E30](#e30) |
| phenotype | If TFAP2A repressed TERT, alt-mediated loss of TFAP2A binding could increase TERT expression and contribute to disease; this is speculative without occupancy data. | missing | none |

Predictions: TFAP2A ChIP should show ref-allele-preferential binding at chr5:1295113 if it occupies this site.; The alt allele should increase TERT expression if TFAP2A is a repressor at this promoter.; TFAP2A knockdown should increase TERT expression from the ref allele.

Falsified if: TFAP2A does not occupy the TERT promoter in glioblastoma cells.; TFAP2A binding is not allele-specific at this base.; TFAP2A activates rather than represses TERT, reversing the predicted direction.

## Prediction matrix

| Test | Cost | Separates top two | H1 | H5 | H3 | H2 | H4 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Query existing GABPA ChIP-seq in a glioblastoma cell line (e.g. U-87MG) for a peak over chr5:1295113; if present, allele-specific GABPA ChIP-qPCR | existing data | yes | A GABPA peak is present over the variant, and allele-specific ChIP shows alt > ref. | No GABPA peak and no allele-specific GABPA occupancy. | No GABPA peak or allele effect; CTCF hypothesis not tested. | No GABPA peak or allele effect; ETV3 remains untested. | No GABPA peak or allele effect; TFAP2A hypothesis not tested. |
| Allele-specific TERT promoter reporter in glioblastoma cells with GABPA knockdown | medium | yes | Alt allele increases reporter activity, and GABPA knockdown reduces alt-driven activity. | No allele-specific reporter difference. | Alt allele increases reporter activity via loss of CTCF; CTCF manipulation modulates it. | Alt allele increases reporter activity, but GABPA knockdown does not reduce it; ETV3 knockdown would. | Alt allele increases reporter activity via loss of TFAP2A; TFAP2A manipulation modulates it. |
| CTCF ChIP-qPCR allele-specific at chr5:1295113 in glioblastoma cells | medium | no | No CTCF allele-specific occupancy or no CTCF peak. | No CTCF allele-specific occupancy or no CTCF peak. | CTCF occupancy is higher on the ref allele. | No CTCF allele-specific occupancy or no CTCF peak. | No CTCF allele-specific occupancy or no CTCF peak. |
| TFAP2A ChIP-qPCR allele-specific at chr5:1295113 in glioblastoma cells | medium | no | No TFAP2A allele-specific occupancy or no TFAP2A peak. | No TFAP2A allele-specific occupancy or no TFAP2A peak. | No TFAP2A allele-specific occupancy or no TFAP2A peak. | No TFAP2A allele-specific occupancy or no TFAP2A peak. | TFAP2A occupancy is higher on the ref allele. |
| ETV3 ChIP-qPCR allele-specific at chr5:1295113 in glioblastoma cells | medium | no | No ETV3 allele-specific occupancy or no ETV3 peak. | No ETV3 allele-specific occupancy or no ETV3 peak. | No ETV3 allele-specific occupancy or no ETV3 peak. | ETV3 occupancy is higher on the alt allele. | No ETV3 allele-specific occupancy or no ETV3 peak. |

## Next experiment

Query existing GABPA ChIP-seq in a glioblastoma line (e.g. U-87MG) for a peak over chr5:1295113 and, if present, perform allele-specific GABPA ChIP-qPCR. A peak with alt > ref supports H1; absence kills H1 and leaves the null H5 standing. This is the cheapest test that separates the top two chains.

## Investigate calls

- chip_peaks({"tf": "GABPA", "biosample": null})
- literature_search({"query": "TERT promoter C228T allele-specific GABPA binding glioblastoma reporter luciferase"})
- qbic_tf_detail({"tf": "GABPA"})

## Flags

- quote_rejected: PMID 41744838: not an exact substring of the abstract

Citation support: 0.85 of links cite only evidence that passed every check.

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

> 2 ENCODE GABPA ChIP-seq peaks contain chr5:1295113:G>A: biosamples HepG2, SK-N-SH; experiments ENCSR000BJK, ENCSR000BTG.

<a id="e33"></a>**E33** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TERT%20promoter%20C228T%20allele-specific%20GABPA%20binding%20glioblastoma%20reporter%20luciferase&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T13:10:10+00:00)

> Europe PMC: 9 hits for 'TERT promoter C228T allele-specific GABPA binding glioblastoma reporter luciferase'; top 6 with PMIDs:
> PMID 40822359 (2025): AURKB and PI3K/AKT/mTOR pathways converge to regulate &lt;i&gt;TERT&lt;/i&gt; expression.
> PMID 34944589 (2021): <i>TERT</i> Promoter Mutations Increase Sense and Antisense Transcription from the <i>TERT</i> Promoter.
> PMID 31802036 (2020): GABPA is a master regulator of luminal identity and restrains aggressive diseases in bladder cancer.
> PMID 33832990 (2021): Interpretation of allele-specific chromatin accessibility using cell state-aware deep learning.
> PMID 31285550 (2019): Mechanisms underlying the activation of TERT transcription and telomerase activity in human cancer: old actors and new players.
> PMID 31903880 (2020): Telomere-related Markers for Cancer.

<a id="e33a"></a>**E33a** literature_search, Europe PMC abstract, PMID 40822359 (https://europepmc.org/article/MED/40822359; retrieved 2026-10-26T13:10:10+00:00)

> Telomere length maintenance, critical for cancer progression, can be driven by TERT promoter mutations (TERTp MUT ), which are markers of poor prognosis across multiple cancers.

<a id="e33b"></a>**E33b** literature_search, Europe PMC abstract, PMID 40822359 (https://europepmc.org/article/MED/40822359; retrieved 2026-10-26T13:10:10+00:00)

> Here, we identified previously uncharacterized pathways regulating TERTp MUT activity by inserting a luciferase reporter downstream of TERTp MUT in SW1736 anaplastic thyroid cancer cells via CRISPR-Cas9, generating SW1736TERT/LUC, and screening a 218-kinase inhibitor library.

<a id="e33c"></a>**E33c** literature_search, Europe PMC abstract, PMID 34944589 (https://europepmc.org/article/MED/34944589; retrieved 2026-10-26T13:10:10+00:00)

> They generate a novel Ets/TCF binding site.

<a id="e33d"></a>**E33d** literature_search, Europe PMC abstract, PMID 34944589 (https://europepmc.org/article/MED/34944589; retrieved 2026-10-26T13:10:10+00:00)

> We compared sense and antisense transcription of a panel of TERT promoter-luciferase vectors harboring the -124C>T and -146C>T mutations alone or together.

<a id="e33e"></a>**E33e** literature_search, Europe PMC abstract, PMID 31802036 (https://europepmc.org/article/MED/31802036; retrieved 2026-10-26T13:10:10+00:00)

> TERT promoter mutations occur in the majority of glioblastoma, bladder cancer (BC), and other malignancies while the ETS family transcription factors GABPA and its partner GABPB1 activate the mutant TERT promoter and telomerase in these tumors.

<a id="e33f"></a>**E33f** literature_search, Europe PMC abstract, PMID 31802036 (https://europepmc.org/article/MED/31802036; retrieved 2026-10-26T13:10:10+00:00)

> GABPA depletion or the disruption of the GABPA/GABPB1 complex by knocking down GABPB1 was shown to inhibit telomerase, thereby eliminating the tumorigenic potential of glioblastoma cells.

<a id="e33g"></a>**E33g** literature_search, Europe PMC abstract, PMID 33832990 (https://europepmc.org/article/MED/33832990; retrieved 2026-10-26T13:10:10+00:00)

> We detect hundreds to thousands of allele-specific chromatin accessibility variants (ASCAVs) in each melanoma genome, of which 15%-20% can be explained by gains or losses of transcription factor binding sites.

<a id="e33h"></a>**E33h** literature_search, Europe PMC abstract, PMID 33832990 (https://europepmc.org/article/MED/33832990; retrieved 2026-10-26T13:10:10+00:00)

> Finally, by augmenting the DeepMEL2 model with ChIP-seq data for GABPA, the TERT promoter mutation, as well as additional ETS motif gains, can be identified with high confidence.

<a id="e33i"></a>**E33i** literature_search, Europe PMC abstract, PMID 31285550 (https://europepmc.org/article/MED/31285550; retrieved 2026-10-26T13:10:10+00:00)

> In this review article, we summarize critical mechanisms activating TERT transcription, with special emphases on the contribution of TERT promoter mutations and structural alterations at the TERT locus, and briefly discuss the underlying implications of these genomic events-driven TERT hyperactivity in cancer initiation/progression and potential clinical applications as well.

<a id="e34"></a>**E34** qbic_tf_detail, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> {"tf":"GABPA","symbol":"GABPA","via":"hgnc_symbol","notes":[],"coverage":"own_model","variant":"chr5:1295113:G>A","gate_p":5.02e-05,"models":[{"model":"GABPA_FL_TC40NGCGATT_YWL_jolma2025_0_2_7mer","mapping":"own","group":"G003 Ets, 18 models","quality":0.658,"effect":4.01,"z":68.47,"p":0.0,"rank_abs_z":"5/997","passed_gate":true,"site_strength":{"ref_percentile":96.3,"alt_percentile":99.8,"k":7}},{"model":"ELF1_FL_TATGAC40NTCA_KW_yin2017_0_2_7mer","mapping":"CIS-BP (ELF1)","group":"G003 Ets, 18 models","quality":0.615,"effect":2.514,"z":124.32,"p":0.0,"rank_abs_z":"2/997","passed_gate":true,"site_strength":{"ref_percentile":92.6,"alt_percentile":100.0,"k":7}},{"model":"ELF2_eDBD_TGAAAT40NCAA_KR_yin2017_0_4_7mer","mapping":"CIS-BP (ELF2)","group":"G003 Ets, 18 models","quality":0.896,"effect":4.515,"z":35.9,"p":2.7e-282,"rank_abs_z":"15/997","passed_gate":true,"site_strength":{"ref_percentile":97.8,"alt_percentile":100.0,"k":7}},{"model":"ELF4_eDBD_TGCGGT40NTCA_KAN_yin2017_0_4_7mer","mapping":"CIS-BP (ELF4)","group":"G003 Ets, 18 models","quality":0.732,"effect":3.97,"z":85.47,"p":0.0,"rank_abs_z":"3/997","passed_gate":true,"site_strength":{"ref_percentile":97.0,"alt_percentile":100.0,"k":7}},{"model":"ELK1_NA_TCGGAA20NAGT_ESAG_yang2017_1_3_7mer","mapping":"CIS-BP (ELK1)","group":"G003 Ets, 18 models","quality":0.779,"effect":1.363,"z":12.45,"p":1.4e-35,"rank_abs_z":"63/997","passed_gate":true,"site_strength":{"ref_percentile":98.2,"alt_percentile":99.4,"k":7}},{"model":"ELK3_FL_TTCGAA40NGAC_KX_yin2017_0_4_7mer","mapping":"CIS-BP (ELK3)","group":"G003 Ets, 18 models","quality":0.841,"effect":2.56,"z":31.23,"p":4.6e-214,"rank_abs_z":"16/997","passed_gate":true,"site_strength":{"ref_percentile":98.2,"alt_percentile":100.0,"k":7}},{"model":"ELK4_FL_TCCGCC40NTCA_KAE_yin2017_0_3_7mer","mapping":"CIS-BP (ELK4)","group":"G003 Ets, 18 models","quality":0.921,"effect":3.273,"z":56.2,"p":0.0,"rank_abs_z":"7/997","passed_gate":true,"site_strength":{"ref_percentile":92.2,"alt_percentile":99.6,"k":7}},{"model":"ERF_NA_TCAGAG20NCG_ESW_yang2017_1_4_7mer","mapping":"CIS-BP (ERF)","group":"G003 Ets, 18 models","quality":0.729,"effect":0.63,"z":23.53,"p":2.2e-122,"rank_abs_z":"23/997","passed_gate":true,"site_strength":{"ref_percentile":96.9,"alt_percentile":99.7,"k":7}},{"model":"ERG_NA_TCTACA20NCAG_ESAG_yang2017_1_4_7mer","mapping":"CIS-BP (ERG)","group":"G003 Ets, 18 models","quality":0.881,"effect":2.323,"z":22.12,"p":2e-108,"rank_abs_z":"26/997","passed_gate":true,"site_strength":{"ref_percentile":98.2,"alt_percentile":99.8,"k":7}},{"model":"ETS1_NA_TGTAAA20NGA_ESAF_yang2017_0_4_7mer","mapping":"CIS-BP (ETS1)","group":"G003 Ets, 18 models","quality":0.873,"effect":1.97,"z":40.46,"p":0.0,"rank_abs_z":"12/997","passed_gate":true,"site_strength":{"ref_percentile":98.7,"alt_percentile":100.0,"k":7}}],"n_models_trimmed":8}
