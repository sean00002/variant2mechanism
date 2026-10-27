# TERT promoter C250T and Glioblastoma, melanoma, bladder

Configuration `full`, named mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.05 over 9 model calls; 123 s.

Variant `chr5:1295135:G>A` (somatic); expression context: DepMap:subtype=Glioblastoma (median of 54 lines).

## QBiC-SELEX screen (occupancy first)

Occupied candidates: GABPA (bound elsewhere, z 167.5); KLF12 (bound elsewhere, z -15.38); NR2C1 (bound elsewhere, z 15.31); TGIF2 (bound elsewhere, z -12.19); ZNF143 (bound elsewhere, z -11.71); ZBTB7A (bound elsewhere, z -10.91); SP2 (bound elsewhere, z -9.83); EGR1 (bound elsewhere, z -8.0); BHLHE40 (bound elsewhere, z -7.34); CTCF (bound elsewhere, z 6.62). Occupancy unknown: ETV2 (z 167.5); ETV3 (z 167.5); FLI1 (z 167.5); ZNF92 (z -33.21); EBF4 (z -24.35). Diagnostic, not shown to the model: 477 of 997 models pass Bonferroni.

## Ranked chains

### 1. GABPA_alt_activation: GABPA binding at the alt allele activates TERT (p = 0.56)

TF GABPA (QBiC-SELEX coverage own_model), alt allele binds more; element None; gene TERT; cell type None.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | GABPA is predicted to bind the alt A allele more strongly. GABPA has its own QBiC-SELEX model at this base with an alt-favoring change (effect 4.05, z 71.32; E33), and a second shared ETS model also favors alt (E17). GABPA is expressed in glioblastoma (15.52 TPM; E17), and ENCODE GABPA peaks contain the variant only in other biosamples, HepG2 and SK-N-SH, not glioblastoma (E32; E17). No ENCODE biosample matches the glioblastoma expression context (E04), so occupancy at this base in the disease context is not demonstrated. GABPA is preferred over FLI1/ETV2/ETV3 because it has an own-model QBiC-SELEX result, higher glioblastoma expression, and literature support for GABP at mutant TERT promoters (E33, E17, E34); the other ETS factors rely only on the shared ETV5-mapped model. | weak | [E33](#e33), [E17](#e17), [E32](#e32), [E04](#e04), [E34](#e34) |
| element | The variant lies in the active promoter-like cCRE EH38E3622530 (PLS) with DNase, H3K27ac and H3K4me3 signal and in the annotated TERT promoter. The cCRE activity z-scores are maxima over ENCODE biosamples, not glioblastoma-specific. | supported | [E01](#e01), [E03](#e03) |
| gene | The element is immediately upstream of TERT (0 kb from the TERT TSS), so an allelic change in TF binding at this base is predicted to alter TERT transcription. | supported | [E01](#e01), [E02](#e02) |
| cell_type | Glioblastoma is a plausible expression context because GABPA is expressed in glioblastoma lines and the element has promoter-like marks, but direct GABPA occupancy at this base in glioblastoma is not shown; ENCODE has no matching glioblastoma GABPA ChIP signal at the variant (E32), and the cCRE marks are not biosample-specific for glioblastoma. | weak | [E03](#e03), [E04](#e04), [E17](#e17), [E32](#e32) |
| phenotype | If alt-enhanced GABPA binding activates the TERT promoter, increased TERT/telomerase activity is predicted to promote TERT promoter mutant cancers. Literature includes a study on GABP coupling oncogene signaling to telomere regulation in TERT promoter mutant cancer (E34), and generic TERT-disease literature links TERT to glioblastoma/melanoma (E15). Direct C250T-specific allele assays are not provided, and bladder-cancer support is not direct in the cited titles. | weak | [E34](#e34), [E15](#e15), [E33](#e33) |

Predictions: Allele-specific GABPA ChIP in a C250T-heterozygous glioblastoma cell line shows more GABPA on the alt A allele than on the ref G allele at this base.; An alt-allele TERT promoter reporter shows higher activity than the ref allele, and GABPA knockdown reduces this difference.; GABPA depletion reduces TERT expression preferentially in cells carrying the alt allele.

Falsified if: Allele-specific GABPA ChIP in a C250T-heterozygous glioblastoma line shows no alt>ref occupancy at this base.; GABPA knockdown or depletion does not reduce alt-associated TERT expression or reporter activity.; The alt allele does not increase TERT expression in an allele-specific, GABPA-dependent manner in glioblastoma cells.

### 2. null_no_TF_effect: Null: no TF-mediated allelic effect at this base (p = 0.31)

Null chain: no TF-mediated effect of this variant.

Predictions: No allele-specific TF occupancy at this base explains the disease association.; The association is due to a linked causal variant, a passenger mutation at a mutational hotspot, or no relevant allelic effect in glioblastoma.; TERT expression is not consistently altered by this base in an allele-specific manner beyond linked variant effects.

Falsified if: Allele-specific TF ChIP or reporter assays demonstrate a reproducible alt>ref or ref>alt effect at this base in glioblastoma cells.; The alt allele changes TERT expression in an allele-specific manner in a relevant cell type.; Fine-mapping excludes a linked causal variant and supports this base as the functional variant.

### 3. KLF12_ref_repressor_loss: Loss of KLF12 repressor binding on the alt allele (p = 0.06)

TF KLF12 (QBiC-SELEX coverage own_model), ref allele binds more; element None; gene TERT; cell type None.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | KLF12 is predicted to bind the ref G allele more strongly, but the evidence is weak. QBiC-SELEX detects a ref-favoring change (z -15.38, effect -0.439; E18), yet the best model is a CIS-BP-mapped KLF5 model rather than a KLF12-specific model. ENCODE KLF12 occupancy over the variant is only in HepG2, not glioblastoma (E18), and KLF12 is expressed at a low level in glioblastoma lines (4.47 TPM, rank 787; E18). | weak | [E18](#e18) |
| element | The variant lies in the active promoter-like cCRE EH38E3622530 (PLS) and in the annotated TERT promoter; activity marks are maxima over biosamples, not glioblastoma-specific. | supported | [E01](#e01), [E03](#e03) |
| gene | The element is immediately upstream of TERT (0 kb from the TERT TSS), placing a predicted KLF12 site in the TERT promoter region. | supported | [E01](#e01), [E02](#e02) |
| cell_type | KLF12 cell-type support is weak: KLF12 is expressed in glioblastoma lines but at low level, and its only occupancy evidence over this variant is from HepG2; no glioblastoma KLF12 occupancy is shown. | weak | [E18](#e18), [E04](#e04) |
| phenotype | If KLF12 normally repressed TERT, loss of KLF12 binding on the alt allele could derepress TERT and promote tumor growth. However, no cited evidence establishes that KLF12 represses TERT, so this phenotype step is speculative. | missing | none |

Predictions: Allele-specific KLF12 ChIP shows stronger KLF12 binding on the ref G allele than on the alt A allele.; KLF12 knockdown increases TERT expression.; The alt allele increases TERT reporter activity specifically when KLF12 is present.

Falsified if: Allele-specific KLF12 ChIP does not show ref>alt binding at this base in a relevant cell type.; KLF12 depletion does not increase TERT expression.; The alt allele does not derepress TERT in a KLF12-dependent manner.

### 4. NR2C1_alt_activation: NR2C1 binding at the alt allele activates TERT (p = 0.04)

TF NR2C1 (QBiC-SELEX coverage own_model), alt allele binds more; element None; gene TERT; cell type None.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | NR2C1 is predicted to bind the alt A allele more strongly, but the evidence is weak. QBiC-SELEX detects an alt-favoring change (z 15.31, effect 1.182; E19), yet the best model is a CIS-BP-mapped RORC model, not a clearly NR2C1-specific model. ENCODE NR2C1 occupancy over the variant is only in GM12878, not glioblastoma (E19). NR2C1 is expressed in glioblastoma lines (18.52 TPM, rank 251; E19). | weak | [E19](#e19) |
| element | The variant lies in the active promoter-like cCRE EH38E3622530 (PLS) and in the annotated TERT promoter; activity marks are maxima over biosamples, not glioblastoma-specific. | supported | [E01](#e01), [E03](#e03) |
| gene | The element is immediately upstream of TERT (0 kb from the TERT TSS), placing a predicted NR2C1 site in the TERT promoter region. | supported | [E01](#e01), [E02](#e02) |
| cell_type | NR2C1 cell-type support is weak: NR2C1 is expressed in glioblastoma lines, but its occupancy evidence over this variant is from GM12878 only; no glioblastoma NR2C1 occupancy or function at this element is demonstrated. | weak | [E19](#e19), [E04](#e04) |
| phenotype | If NR2C1 activated the TERT promoter, alt-enhanced NR2C1 binding could increase TERT expression and promote tumor growth. However, no cited evidence establishes that NR2C1 activates TERT, so this phenotype step is speculative. | missing | none |

Predictions: Allele-specific NR2C1 ChIP shows stronger NR2C1 binding on the alt A allele than on the ref G allele in glioblastoma cells.; NR2C1 knockdown reduces TERT expression preferentially from the alt allele.; The alt allele increases TERT reporter activity in an NR2C1-dependent manner.

Falsified if: Allele-specific NR2C1 ChIP does not show alt>ref binding at this base in glioblastoma cells.; NR2C1 depletion does not reduce mutant TERT expression.; The alt allele does not increase TERT in an NR2C1-dependent manner.

### 5. FLI1_alt_ETS_alternative: Alternative ETS factor FLI1 binds the alt allele (p = 0.03)

TF FLI1 (QBiC-SELEX coverage own_model), alt allele binds more; element None; gene TERT; cell type None.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | FLI1 is predicted to bind the alt A allele more strongly only through the shared ETV5-mapped ETS QBiC-SELEX model (z 167.5, effect 2.421; E29). This model is identical for GABPA/ETV2/ETV3/FLI1 and does not distinguish FLI1 from other ETS factors. FLI1 has unknown ENCODE occupancy at this base and low glioblastoma expression (4.71 TPM, rank 767; E29). | weak | [E29](#e29), [E04](#e04) |
| element | The variant lies in the active promoter-like cCRE EH38E3622530 (PLS) and in the annotated TERT promoter; activity marks are maxima over biosamples, not glioblastoma-specific. | supported | [E01](#e01), [E03](#e03) |
| gene | The element is immediately upstream of TERT (0 kb from the TERT TSS), so an alt-favoring ETS site here could affect TERT transcription. | supported | [E01](#e01), [E02](#e02) |
| cell_type | FLI1 cell-type support is weak: FLI1 is expressed at low level in glioblastoma lines, has unknown occupancy at this base, and no glioblastoma FLI1 ChIP evidence is given. | weak | [E29](#e29), [E04](#e04) |
| phenotype | If FLI1 activated the TERT promoter, alt-enhanced FLI1 binding could increase TERT expression and promote tumor growth. However, no cited evidence establishes that FLI1 activates TERT, so this phenotype step is speculative. | missing | none |

Predictions: Allele-specific FLI1 ChIP shows stronger FLI1 binding on the alt A allele than on the ref G allele in glioblastoma cells.; FLI1 knockdown reduces TERT expression in cells carrying the alt allele.; The alt allele increases ETS-dependent TERT reporter activity that is not explained by GABPA.

Falsified if: No ETS-family occupancy is detected at this base in glioblastoma cells.; FLI1 is not expressed or not bound at this promoter in glioblastoma cells.; The alt allele does not increase TERT in an ETS-dependent manner.

## Prediction matrix

| Test | Cost | Separates top two | GABPA_alt_activation | null_no_TF_effect | KLF12_ref_repressor_loss | NR2C1_alt_activation | FLI1_alt_ETS_alternative |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Allele-specific GABPA ChIP-qPCR or GABPA ChIP-seq with allele counts in a C250T-heterozygous glioblastoma cell line | low | yes | Alt>ref GABPA occupancy at chr5:1295135 in C250T-heterozygous glioblastoma cells. | No allele-specific GABPA occupancy at this base. | No GABPA allele-specific effect is required; KLF12 ref>alt would be a separate prediction. | No GABPA allele-specific effect is required; NR2C1 alt>ref would be a separate prediction. | No GABPA-specific allele effect is required, though shared ETS signal might be seen. |
| GABPA knockdown plus allele-specific TERT reporter or TERT expression assay in glioblastoma cells | medium | yes | GABPA knockdown reduces alt-driven TERT expression/reporter activity; alt>ref reporter difference is GABPA-dependent. | No GABPA-dependent allele-specific TERT effect. | No GABPA-dependent TERT effect required; KLF12 knockdown, if anything, increases TERT. | No GABPA-dependent TERT effect required; NR2C1 knockdown reduces alt-driven TERT. | GABPA knockdown alone may not abolish the effect if FLI1 acts through the same ETS site. |
| Allele-specific KLF12 ChIP in a relevant cell type | medium | no | No KLF12 ref>alt binding is required. | No allele-specific KLF12 occupancy at this base. | KLF12 ChIP is stronger on the ref G allele than on the alt A allele. | No KLF12 allele-specific binding is required. | No KLF12 allele-specific binding is required. |
| Allele-specific NR2C1 ChIP in glioblastoma cells | medium | no | No NR2C1 alt>ref binding is required. | No allele-specific NR2C1 occupancy at this base. | No NR2C1 alt>ref binding is required. | NR2C1 ChIP is stronger on the alt A allele than on the ref G allele. | No NR2C1 alt>ref binding is required. |
| Allele-specific FLI1 ChIP and FLI1 knockdown in glioblastoma cells | medium | no | No FLI1 alt>ref binding is required. | No allele-specific FLI1 occupancy at this base. | No FLI1 alt>ref binding is required. | No FLI1 alt>ref binding is required. | FLI1 ChIP is stronger on the alt A allele than on the ref G allele, and FLI1 knockdown reduces TERT. |
| Base editing or fine-mapping at chr5:1295135 to test whether this base itself drives allele-specific TERT expression | high | yes | Editing or fine-mapping supports this base as functional; GABPA-dependent alt effect remains. | Little or no allele-specific TERT effect when only this base is edited, or evidence that a linked variant explains the association. | Editing supports this base but not necessarily KLF12; KLF12-specific effect would need separate ChIP. | Editing supports this base but not necessarily NR2C1; NR2C1-specific effect would need separate ChIP. | Editing supports this base but not necessarily FLI1; FLI1-specific effect would need separate ChIP. |

## Next experiment

The single cheapest experiment that separates the top two chains is allele-specific GABPA ChIP-qPCR (or GABPA ChIP-seq with allele counts) in a C250T-heterozygous glioblastoma cell line, comparing GABPA occupancy on the alt A versus ref G allele at chr5:1295135. It directly tests the GABPA_alt_activation binding prediction against the null no-TF-effect prediction at low cost.

## Investigate calls

- chip_peaks({"biosample": "glioblastoma", "tf": "GABPA"})
- qbic_tf_detail({"tf": "GABPA"})
- literature_search({"query": "TERT promoter C250T GABPA ETS binding glioblastoma"})

## Flags

- quote_rejected: PMID 41744838: not an exact substring of the abstract
- quote_rejected: PMID 37741952: not an exact substring of the abstract

Citation support: 0.85 of links cite only evidence that passed every check.

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

> QBiC-SELEX screen of chr5:1295135:G>A, one line per TF, each with the TF's own or CIS-BP-mapped model of largest |z|. Candidates are TFs whose ENCODE ChIP-seq peaks contain the variant and that are expressed (DepMap subtype median Glioblastoma), bound here before bound elsewhere, then by |z|; then expressed TFs ENCODE never assayed whose best model passes the gate (occupancy unknown). Shown: 10 of 18 occupied, 5 of 145 with unknown occupancy. Left out: 0 TFs assayed in the matching biosample and 554 assayed only elsewhere, none with a peak here; 1 bound but below 1 TPM. The gate (|z| > 4.05, Bonferroni over 997 models) marks a change QBiC-SELEX detects; it says nothing about occupancy. Effect > 0 means the alternate allele binds more strongly. In vitro binding only.

<a id="e17"></a>**E17** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> GABPA (Ets, 18 models; QBiC-SELEX coverage: own model): best model ETV5_NA_TGCACT20NGA_ESAF_yang2017_1_3_6mer (a CIS-BP-mapped model of ETV5), z 167.5, effect 2.421: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 15.52 TPM, rank 303 of 1626 TFs in DepMap:subtype=Glioblastoma (median of 54 lines). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in HepG2, SK-N-SH, e.g. ENCSR000BJK. Best model's site strength: ref 94.8th, alt 99.9th percentile of its k-mer coefficients.

<a id="e18"></a>**E18** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> KLF12 (C2H2 ZF, 6 models; QBiC-SELEX coverage: own model): best model KLF5_eDBD_TAACGC40NGTG_KS_yin2017_0_4_7mer (a CIS-BP-mapped model of KLF5), z -15.38, effect -0.439: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 4.47 TPM, rank 787 of 1626 TFs in DepMap:subtype=Glioblastoma (median of 54 lines). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in HepG2, e.g. ENCSR552YWL. Best model's site strength: ref 99.9th, alt 98.9th percentile of its k-mer coefficients.

<a id="e19"></a>**E19** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> NR2C1 (Nuclear receptor, 29 models; QBiC-SELEX coverage: own model): best model RORC_NA_Lib1_NA_bhimsaria2023_0(3)_3_7mer (a CIS-BP-mapped model of RORC), z 15.31, effect 1.182: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 18.52 TPM, rank 251 of 1626 TFs in DepMap:subtype=Glioblastoma (median of 54 lines). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in GM12878, e.g. ENCSR784VIQ. Best model's site strength: ref 98.3th, alt 99.2th percentile of its k-mer coefficients.

<a id="e20"></a>**E20** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> TGIF2 (Homeodomain, 9 models; QBiC-SELEX coverage: own model): best model PKNOX2_eDBD_TAACGT40NGAT_KAN_yin2017_0_4_7mer (a CIS-BP-mapped model of PKNOX2), z -12.19, effect -1.113: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 10.31 TPM, rank 452 of 1626 TFs in DepMap:subtype=Glioblastoma (median of 54 lines). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in HepG2, e.g. ENCSR993LMB. Best model's site strength: ref 98.3th, alt 71.5th percentile of its k-mer coefficients.

<a id="e21"></a>**E21** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> ZNF143 (C2H2 ZF, 2 models; QBiC-SELEX coverage: own model): best model ZNF143_NA_TGCAAG20NCG_V_jolma2013_0_3_7mer (its own model), z -11.71, effect -0.649: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 15.92 TPM, rank 297 of 1626 TFs in DepMap:subtype=Glioblastoma (median of 54 lines). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in GM12878, e.g. ENCSR936XTK. Best model's site strength: ref 100.0th, alt 98.4th percentile of its k-mer coefficients.

<a id="e22"></a>**E22** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> ZBTB7A (C2H2 ZF, 1 model; QBiC-SELEX coverage: own model): best model ZBTB7A_eDBD_TTTGCT40NCGT_KR_yin2017_0_4_7mer (its own model), z -10.91, effect -0.707: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 8.49 TPM, rank 531 of 1626 TFs in DepMap:subtype=Glioblastoma (median of 54 lines). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in K562, e.g. ENCSR000BME. Best model's site strength: ref 99.9th, alt 99.9th percentile of its k-mer coefficients.

<a id="e23"></a>**E23** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> SP2 (C2H2 ZF, 1 model; QBiC-SELEX coverage: own model): best model SP2_eDBD_TCATGT40NCTG_KV_yin2017_0_4_7mer (its own model), z -9.83, effect -0.269: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 15.49 TPM, rank 305 of 1626 TFs in DepMap:subtype=Glioblastoma (median of 54 lines). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in HepG2, e.g. ENCSR946RZN. Best model's site strength: ref 100.0th, alt 99.7th percentile of its k-mer coefficients.

<a id="e24"></a>**E24** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> EGR1 (C2H2 ZF, 4 models; QBiC-SELEX coverage: own model): best model EGR3_NA_TCATGC20NGTA_ESZ_yang2017_0_4_7mer (a CIS-BP-mapped model of EGR3), z -8.0, effect -0.422: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 28.32 TPM, rank 151 of 1626 TFs in DepMap:subtype=Glioblastoma (median of 54 lines). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in HepG2, Ishikawa, e.g. ENCSR000BSQ. Best model's site strength: ref 99.8th, alt 99.7th percentile of its k-mer coefficients.

<a id="e25"></a>**E25** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> BHLHE40 (bHLH, 2 models; QBiC-SELEX coverage: own model): best model BHLHE40_eDBD_TTAGTG40NACC_KR_yin2017_0_3_7mer (its own model), z -7.34, effect -0.318: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 68.33 TPM, rank 33 of 1626 TFs in DepMap:subtype=Glioblastoma (median of 54 lines). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in GM12878, e.g. ENCSR000DZJ. Best model's site strength: ref 99.6th, alt 93.6th percentile of its k-mer coefficients.

<a id="e26"></a>**E26** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> CTCF (C2H2 ZF, 1 model; QBiC-SELEX coverage: own model): best model CTCF_FL_TG40NCTGTGG_YWL_jolma2025_0_3_7mer (its own model), z 6.62, effect 0.752: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 26.45 TPM, rank 163 of 1626 TFs in DepMap:subtype=Glioblastoma (median of 54 lines). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in DOHH2, endodermal cell, e.g. ENCSR084RDK. Best model's site strength: ref 97.2th, alt 97.0th percentile of its k-mer coefficients.

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

<a id="e34"></a>**E34** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TERT%20promoter%20C250T%20GABPA%20ETS%20binding%20glioblastoma&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T02:35:35+00:00)

> Europe PMC: 52 hits for 'TERT promoter C250T GABPA ETS binding glioblastoma'; top 8 with PMIDs:
> PMID 40822359 (2025): AURKB and PI3K/AKT/mTOR pathways converge to regulate &lt;i&gt;TERT&lt;/i&gt; expression.
> PMID 37741952 (2023): Pooled genetic screens to identify vulnerabilities in TERT-promoter-mutant glioblastoma.
> PMID 38033865 (2023): Reactivation of telomerase reverse transcriptase expression in cancer: the role of TERT promoter mutations.
> PMID 36713366 (2022): <i>TERT</i> promoter mutations and methylation for telomerase activation in urothelial carcinomas: New mechanistic insights and clinical significance.
> PMID 38392213 (2024): Prevalence of <i>TERT</i> Promoter Mutations in Orbital Solitary Fibrous Tumors.
> PMID 38285162 (2024): Mechanisms of telomere maintenance and associated therapeutic vulnerabilities in malignant gliomas.
> PMID 36130485 (2022): GABP couples oncogene signaling to telomere regulation in TERT promoter mutant cancer.
> PMID 40272676 (2025): TERT Amplification a Risk Stratification Marker in Papillary Thyroid Carcinoma, Significantly Correlated with Tumor Recurrence and Survival.
