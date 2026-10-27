# TERT promoter C228T and Glioblastoma, melanoma, bladder

Configuration `full`, masked mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.03 over 10 model calls; 256 s.

Variant `chr5:1295113:G>A` (somatic); expression context: DepMap:subtype=Glioblastoma (median of 54 lines).

## QBiC-SELEX screen (occupancy first)

Occupied candidates: GABPA (bound elsewhere, z 166.19); ZIC2 (bound elsewhere, z -20.85); CTCF (bound elsewhere, z -14.7); ZBTB7A (bound elsewhere, z -14.11); NR2C1 (bound elsewhere, z -10.53); E2F4 (bound elsewhere, z 5.78); E2F6 (bound elsewhere, z 5.78); E2F5 (bound elsewhere, z 5.78); EGR1 (bound elsewhere, z -3.42, no clear allelic change); JUN (bound elsewhere, z 3.26, no clear allelic change). Occupancy unknown: ETV2 (z 166.19); ETV3 (z 166.19); FLI1 (z 166.19); TFAP2A (z -36.84); TFAP2C (z -36.84). Diagnostic, not shown to the model: 310 of 997 models pass Bonferroni.

## Ranked chains

### 1. GABPA_ETS_alt: GABPA/ETS site creation at the TERT promoter (p = 0.62)

TF GABPA (QBiC-SELEX coverage own_model), alt allele binds more; element TERT promoter PLS EH38E3622530; gene TERT; cell type Glioblastoma (DepMap context).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | GABPA binds the alt A allele more strongly than ref G at this base. GABPA's own QBiC-SELEX model gives effect +4.01, z 68.47, above the gate, and E17 reports a mapped ETS model with effect +2.121, z 166.19, also alt-binding; the alt site reaches a strong percentile. GABPA is the best-supported ETS candidate because it is expressed in glioblastoma at 15.52 TPM, has ENCODE ChIP peaks over this base only in non-matching biosamples HepG2 and SK-N-SH, and literature identifies GABPA/GABP tetramers at mutant TERT promoter ETS motifs. ETV2, ETV3 and FLI1 share an ETS model but have unknown occupancy and lower expression. No glioblastoma ENCODE GABPA peak over this base is shown, so disease-context occupancy is inferred rather than directly demonstrated. | weak | [E33](#e33), [E17](#e17), [E32](#e32), [E04](#e04), [E11](#e11), [E34d](#e34d), [E34e](#e34e), [E34k](#e34k), [E27](#e27), [E28](#e28), [E29](#e29) |
| element | The variant lies in promoter-like cCRE EH38E3622530, a PLS at the TERT upstream promoter with active promoter chromatin marks DNase, H3K27ac and H3K4me3. | supported | [E03](#e03), [E01](#e01) |
| gene | The element is 0.0 kb from the TERT transcription start site and is annotated as a TERT upstream/promoter variant; TERT is the nearest gene. | supported | [E02](#e02), [E01](#e01) |
| cell_type | TERT promoter mutations and GABPA/GABPB1-dependent TERT activation are established in glioblastoma and bladder cancer; TERT is also relevant in melanoma, although melanoma-specific GABPA evidence at this base is limited. | supported | [E34k](#e34k), [E34f](#e34f), [E15](#e15), [E34a](#e34a) |
| phenotype | Alt A is predicted to strengthen a GABPA/ETS site and increase TERT transcription and telomerase, promoting tumor maintenance or progression. This is supported by GABP-dependent activation of mutant TERT promoters and by GABPA/GABPB1 knockdown inhibiting telomerase and tumorigenicity in glioblastoma, but no supplied evidence tests this exact allele's effect on TERT expression, telomerase or disease. | weak | [E34d](#e34d), [E34e](#e34e), [E34k](#e34k), [E34l](#e34l), [E17](#e17), [E33](#e33) |

Predictions: Allele-specific GABPA ChIP at this base shows higher GABPA occupancy on alt A than ref G in a TERT-expressing glioblastoma line heterozygous at the variant.; An isolated alt-A vs ref-G TERT reporter, or endogenous knock-in, increases TERT mRNA or telomerase activity; GABPA or GABPB1 knockdown reduces the alt-specific increase.; The alt allele retains an effect after controlling for linked canonical TERT promoter mutations and tracks with GABPA/GABPB1 dependence.

Falsified if: No alt-specific GABPA occupancy is detected at this base in a TERT-expressing glioblastoma, melanoma or bladder cancer cell line.; Isolated alt A vs ref G does not change TERT reporter, mRNA or telomerase activity when linked variants are controlled.; GABPA or GABPB1 knockdown, or ETS-motif disruption, does not reduce the alt-specific TERT signal.

### 2. null_linked_or_passenger: No TF-mediated effect; linked causal variant or passenger mutation (p = 0.25)

Null chain: no TF-mediated effect of this variant.

Predictions: No allele-specific GABPA, TFAP2A or CTCF occupancy at this exact base in disease-relevant cells after controlling for linked variants.; Any association with TERT expression or disease is explained by another linked TERT promoter mutation, a nearby causal variant, or this site being a passenger in a mutational hotspot.; Isolated alt A vs ref G does not change TERT reporter, mRNA or telomerase activity.

Falsified if: Allele-specific GABPA, TFAP2A or CTCF binding at this base is validated in a disease-relevant cell line.; Isolated alt A vs ref G changes TERT reporter, mRNA or telomerase activity after controlling for linked variants.

### 3. TFAP2A_ref_repressor: TFAP2A loss-of-repressor at the TERT promoter (p = 0.08)

TF TFAP2A (QBiC-SELEX coverage own_model), ref allele binds more; element TERT promoter PLS EH38E3622530; gene TERT; cell type Glioblastoma (DepMap context).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | TFAP2A binds the ref G allele more strongly than alt A in QBiC-SELEX: effect -1.289, z -36.84, above the gate, with a strong site. TFAP2A is expressed at 9.65 TPM in glioblastoma; TFAP2C shares the same AP-2 model and is lower expressed. Neither has ENCODE occupancy over this base, so this is a motif-based candidate with unknown occupancy. | weak | [E30](#e30), [E31](#e31) |
| element | The variant lies in the active TERT promoter PLS EH38E3622530, so an AP-2 site change could in principle affect promoter activity. | supported | [E03](#e03), [E01](#e01) |
| gene | The element is at the TERT transcription start site, making TERT the direct candidate target gene. | supported | [E02](#e02), [E01](#e01) |
| cell_type | TERT is relevant in glioblastoma, melanoma and bladder cancer, but there is no TFAP2A-specific disease evidence for this base. | weak | [E15](#e15), [E34k](#e34k) |
| phenotype | Speculative only: if TFAP2A represses TERT, the alt A allele would reduce TFAP2A binding, relieve repression and increase TERT. No supplied evidence shows TFAP2A represses TERT or that this allele changes TERT expression or disease. | missing | none |

Predictions: Ref G shows more TFAP2A ChIP at this base than alt A in a TFAP2A-expressing disease-relevant cell line.; If TFAP2A represses TERT, alt A should de-repress TERT and increase TERT reporter or mRNA; TFAP2A overexpression should lower TERT more strongly on ref G than on alt A.; TFAP2A knockdown should increase TERT expression at this promoter.

Falsified if: TFAP2A does not occupy the TERT promoter at this base in disease-relevant cells.; Alt A does not change TERT expression or telomerase activity.; TFAP2A does not repress TERT in reporter assays, or TFAP2A knockdown does not increase TERT.

### 4. CTCF_ref_architectural: CTCF loss at an insulator/architectural site (p = 0.05)

TF CTCF (QBiC-SELEX coverage own_model), ref allele binds more; element TERT promoter PLS EH38E3622530; gene TERT; cell type Glioblastoma (DepMap context).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | CTCF binds the ref G allele more strongly than alt A in QBiC-SELEX: effect -1.719, z -14.7, above the gate, with a strong site. CTCF is expressed at 26.45 TPM in glioblastoma and has one ENCODE peak over this variant only in DOHH2, not in a matching disease context; the cCRE has only a low CTCF z-score of 2.0. This is a motif-based candidate without disease-relevant occupancy. | weak | [E19](#e19), [E13](#e13), [E03](#e03), [E04](#e04) |
| element | The variant lies in the TERT promoter PLS with low CTCF cCRE signal and a predicted CTCF site change, but an insulator or architectural function at this promoter is not established. | weak | [E03](#e03), [E19](#e19) |
| gene | The element is at the TERT transcription start site, so altered CTCF binding could in principle affect TERT promoter contacts, but no supplied evidence shows CTCF-dependent TERT regulation at this base. | weak | [E02](#e02), [E01](#e01) |
| cell_type | TERT is relevant in glioblastoma, melanoma and bladder cancer, but there is no CTCF-specific disease evidence for this base. | weak | [E15](#e15) |
| phenotype | Speculative only: alt A would reduce CTCF binding and potentially disrupt a promoter-proximal insulator or chromatin contact, permitting increased TERT expression. No supplied evidence shows altered CTCF binding, chromatin contacts, TERT expression, telomerase activity or disease for this allele. | missing | none |

Predictions: Ref G shows more CTCF ChIP at this base than alt A in a CTCF-expressing disease-relevant cell line.; Alt A reduces CTCF binding and alters TERT promoter-enhancer contacts or chromatin architecture.; CTCF depletion mimics the alt A allele's effect on TERT expression.

Falsified if: CTCF does not occupy this base in disease-relevant cells.; Alt A does not change CTCF binding or TERT promoter-enhancer contacts.; CTCF depletion does not mimic the alt allele's effect on TERT.

## Prediction matrix

| Test | Cost | Separates top two | GABPA_ETS_alt | null_linked_or_passenger | TFAP2A_ref_repressor | CTCF_ref_architectural |
| --- | --- | --- | --- | --- | --- | --- |
| Allele-specific GABPA ChIP-qPCR at chr5:1295113 in a TERT-expressing glioblastoma line heterozygous G/A | medium | yes | Alt A shows higher GABPA occupancy than ref G at this base. | No GABPA occupancy over this base, or no alt-vs-ref difference. | No GABPA allelic difference is expected because this chain does not invoke GABPA. | No GABPA allelic difference is expected because this chain does not invoke GABPA. |
| Isolated alt-A vs ref-G TERT promoter reporter in a glioblastoma line, controlling linked variants | medium | yes | Alt A increases TERT reporter activity; GABPA or GABPB1 knockdown reduces the alt-specific increase. | No alt-vs-ref difference in TERT reporter activity when linked variants are controlled. | Alt A may increase TERT if TFAP2A represses TERT and its ref site is lost; TFAP2A knockdown should increase TERT. | Alt A may increase TERT if CTCF normally insulates/represses; CTCF depletion should mimic alt A. |
| GABPA or GABPB1 knockdown, or ETS-motif disruption, in the allele-specific TERT reporter | medium | yes | Knockdown or motif disruption reduces the alt-specific TERT signal. | No allele-specific TERT signal to knock down. | No GABPA/GABPB1 dependence; any alt effect should track TFAP2A, not GABPA. | No GABPA/GABPB1 dependence; any alt effect should track CTCF/chromatin architecture. |
| Allele-specific TFAP2A ChIP at chr5:1295113 in TFAP2A-expressing disease-relevant cells | medium | no | No TFAP2A allelic difference is expected because this chain invokes GABPA. | No TFAP2A occupancy or no allelic difference at this base. | Ref G shows higher TFAP2A occupancy than alt A. | No TFAP2A allelic difference is expected because this chain invokes CTCF. |
| Allele-specific CTCF ChIP at chr5:1295113 in CTCF-expressing disease-relevant cells | medium | no | No CTCF allelic difference is expected because this chain invokes GABPA. | No CTCF occupancy or no allelic difference at this base. | No CTCF allelic difference is expected because this chain invokes TFAP2A. | Ref G shows higher CTCF occupancy than alt A at this base. |
| Conditional association or fine-mapping after controlling for linked canonical TERT promoter mutations | high | yes | This base retains an independent alt-A effect after conditioning on linked TERT promoter mutations. | The association is explained by a linked causal TERT promoter mutation or passenger status; no independent effect at this base. | Any signal at this base is not independent of linked variants; TFAP2A effect would also need to survive conditioning. | Any signal at this base is not independent of linked variants; CTCF effect would also need to survive conditioning. |

## Next experiment

allele-specific GABPA ChIP-qPCR at chr5:1295113 in a TERT-expressing glioblastoma line heterozygous G/A (or another GABPA-expressing heterozygous line), comparing alt A vs ref G immunoprecipitated DNA. Cost: low-medium. The GABPA chain predicts alt > ref GABPA occupancy; the null predicts no allele-specific GABPA occupancy at this base.

## Investigate calls

- chip_peaks({"tf": "GABPA", "biosample": "Glioblastoma"})
- qbic_tf_detail({"tf": "GABPA"})
- literature_search({"query": "TERT promoter allele-specific GABPA ETS luciferase reporter glioblastoma"})

## Flags

- quote_rejected: PMID 41744838: not an exact substring of the abstract

Citation support: 0.87 of links cite only evidence that passed every check.

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

> No ENCODE GABPA ChIP-seq peak contains chr5:1295113:G>A in biosamples matching 'Glioblastoma'. Absence can also mean no GABPA experiment in that biosample. In other biosamples, 2 GABPA peaks do contain the variant: HepG2, SK-N-SH (experiments ENCSR000BJK, ENCSR000BTG).

<a id="e33"></a>**E33** qbic_tf_detail, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> {"tf":"GABPA","symbol":"GABPA","via":"hgnc_symbol","notes":[],"coverage":"own_model","variant":"chr5:1295113:G>A","gate_p":5.02e-05,"models":[{"model":"GABPA_FL_TC40NGCGATT_YWL_jolma2025_0_2_7mer","mapping":"own","group":"G003 Ets, 18 models","quality":0.658,"effect":4.01,"z":68.47,"p":0.0,"rank_abs_z":"5/997","passed_gate":true,"site_strength":{"ref_percentile":96.3,"alt_percentile":99.8,"k":7}},{"model":"ELF1_FL_TATGAC40NTCA_KW_yin2017_0_2_7mer","mapping":"CIS-BP (ELF1)","group":"G003 Ets, 18 models","quality":0.615,"effect":2.514,"z":124.32,"p":0.0,"rank_abs_z":"2/997","passed_gate":true,"site_strength":{"ref_percentile":92.6,"alt_percentile":100.0,"k":7}},{"model":"ELF2_eDBD_TGAAAT40NCAA_KR_yin2017_0_4_7mer","mapping":"CIS-BP (ELF2)","group":"G003 Ets, 18 models","quality":0.896,"effect":4.515,"z":35.9,"p":2.7e-282,"rank_abs_z":"15/997","passed_gate":true,"site_strength":{"ref_percentile":97.8,"alt_percentile":100.0,"k":7}},{"model":"ELF4_eDBD_TGCGGT40NTCA_KAN_yin2017_0_4_7mer","mapping":"CIS-BP (ELF4)","group":"G003 Ets, 18 models","quality":0.732,"effect":3.97,"z":85.47,"p":0.0,"rank_abs_z":"3/997","passed_gate":true,"site_strength":{"ref_percentile":97.0,"alt_percentile":100.0,"k":7}},{"model":"ELK1_NA_TCGGAA20NAGT_ESAG_yang2017_1_3_7mer","mapping":"CIS-BP (ELK1)","group":"G003 Ets, 18 models","quality":0.779,"effect":1.363,"z":12.45,"p":1.4e-35,"rank_abs_z":"63/997","passed_gate":true,"site_strength":{"ref_percentile":98.2,"alt_percentile":99.4,"k":7}},{"model":"ELK3_FL_TTCGAA40NGAC_KX_yin2017_0_4_7mer","mapping":"CIS-BP (ELK3)","group":"G003 Ets, 18 models","quality":0.841,"effect":2.56,"z":31.23,"p":4.6e-214,"rank_abs_z":"16/997","passed_gate":true,"site_strength":{"ref_percentile":98.2,"alt_percentile":100.0,"k":7}},{"model":"ELK4_FL_TCCGCC40NTCA_KAE_yin2017_0_3_7mer","mapping":"CIS-BP (ELK4)","group":"G003 Ets, 18 models","quality":0.921,"effect":3.273,"z":56.2,"p":0.0,"rank_abs_z":"7/997","passed_gate":true,"site_strength":{"ref_percentile":92.2,"alt_percentile":99.6,"k":7}},{"model":"ERF_NA_TCAGAG20NCG_ESW_yang2017_1_4_7mer","mapping":"CIS-BP (ERF)","group":"G003 Ets, 18 models","quality":0.729,"effect":0.63,"z":23.53,"p":2.2e-122,"rank_abs_z":"23/997","passed_gate":true,"site_strength":{"ref_percentile":96.9,"alt_percentile":99.7,"k":7}},{"model":"ERG_NA_TCTACA20NCAG_ESAG_yang2017_1_4_7mer","mapping":"CIS-BP (ERG)","group":"G003 Ets, 18 models","quality":0.881,"effect":2.323,"z":22.12,"p":2e-108,"rank_abs_z":"26/997","passed_gate":true,"site_strength":{"ref_percentile":98.2,"alt_percentile":99.8,"k":7}},{"model":"ETS1_NA_TGTAAA20NGA_ESAF_yang2017_0_4_7mer","mapping":"CIS-BP (ETS1)","group":"G003 Ets, 18 models","quality":0.873,"effect":1.97,"z":40.46,"p":0.0,"rank_abs_z":"12/997","passed_gate":true,"site_strength":{"ref_percentile":98.7,"alt_percentile":100.0,"k":7}}],"n_models_trimmed":8}

<a id="e34"></a>**E34** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TERT%20promoter%20allele-specific%20GABPA%20ETS%20luciferase%20reporter%20glioblastoma&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T20:33:18+00:00)

> Europe PMC: 16 hits for 'TERT promoter allele-specific GABPA ETS luciferase reporter glioblastoma'; top 8 with PMIDs:
> PMID 40822359 (2025): AURKB and PI3K/AKT/mTOR pathways converge to regulate &lt;i&gt;TERT&lt;/i&gt; expression.
> PMID 40513567 (2025): The immortality mechanism of TERT promoter mutant cancers is self-reinforcing and reversible.
> PMID 40359938 (2025): Reannotation of cancer mutations based on expressed RNA transcripts reveals functional non-coding mutations in melanoma.
> PMID 36114166 (2022): Conserved features of TERT promoter duplications reveal an activation mechanism that mimics hotspot mutations in cancer.
> PMID 38902506 (2024): Hidden secrets of the cancer genome: unlocking the impact of non-coding mutations in gene regulatory elements.
> PMID 34944589 (2021): <i>TERT</i> Promoter Mutations Increase Sense and Antisense Transcription from the <i>TERT</i> Promoter.
> PMID 33832990 (2021): Interpretation of allele-specific chromatin accessibility using cell state-aware deep learning.
> PMID 31802036 (2020): GABPA is a master regulator of luminal identity and restrains aggressive diseases in bladder cancer.

<a id="e34a"></a>**E34a** literature_search, Europe PMC abstract, PMID 40822359 (https://europepmc.org/article/MED/40822359; retrieved 2026-10-26T20:33:18+00:00)

> Telomere length maintenance, critical for cancer progression, can be driven by TERT promoter mutations (TERTp MUT ), which are markers of poor prognosis across multiple cancers.

<a id="e34b"></a>**E34b** literature_search, Europe PMC abstract, PMID 40822359 (https://europepmc.org/article/MED/40822359; retrieved 2026-10-26T20:33:18+00:00)

> Here, we identified previously uncharacterized pathways regulating TERTp MUT activity by inserting a luciferase reporter downstream of TERTp MUT in SW1736 anaplastic thyroid cancer cells via CRISPR-Cas9, generating SW1736TERT/LUC, and screening a 218-kinase inhibitor library.

<a id="e34c"></a>**E34c** literature_search, Europe PMC abstract, PMID 40513567 (https://europepmc.org/article/MED/40513567; retrieved 2026-10-26T20:33:18+00:00)

> TERT promoter (TERTp) mutations create a de novo E26 transformation-specific (ETS) transcription factor binding motif.

<a id="e34d"></a>**E34d** literature_search, Europe PMC abstract, PMID 40513567 (https://europepmc.org/article/MED/40513567; retrieved 2026-10-26T20:33:18+00:00)

> Here, we analyzed 53 cell lines representing 16 cancer types and 6 recurrent TERTp mutations and found that the GA-binding protein (GABP) tetramer is responsible for promoter activation in all cases.

<a id="e34e"></a>**E34e** literature_search, Europe PMC abstract, PMID 36114166 (https://europepmc.org/article/MED/36114166; retrieved 2026-10-26T20:33:18+00:00)

> Beyond the two most common point mutations, which selectively recruit the ETS factor GABP to activate TERT, the significance of other variants is unknown.

<a id="e34f"></a>**E34f** literature_search, Europe PMC abstract, PMID 36114166 (https://europepmc.org/article/MED/36114166; retrieved 2026-10-26T20:33:18+00:00)

> The duplications recruit a GABP tetramer by virtue of the native ETS motif and its precisely spaced duplicated counterpart, activate the promoter and are clonal in a TERT expressing multifocal glioblastoma.

<a id="e34g"></a>**E34g** literature_search, Europe PMC abstract, PMID 34944589 (https://europepmc.org/article/MED/34944589; retrieved 2026-10-26T20:33:18+00:00)

> They generate a novel Ets/TCF binding site.

<a id="e34h"></a>**E34h** literature_search, Europe PMC abstract, PMID 34944589 (https://europepmc.org/article/MED/34944589; retrieved 2026-10-26T20:33:18+00:00)

> We compared sense and antisense transcription of a panel of TERT promoter-luciferase vectors harboring the -124C>T and -146C>T mutations alone or together.

<a id="e34i"></a>**E34i** literature_search, Europe PMC abstract, PMID 33832990 (https://europepmc.org/article/MED/33832990; retrieved 2026-10-26T20:33:18+00:00)

> We detect hundreds to thousands of allele-specific chromatin accessibility variants (ASCAVs) in each melanoma genome, of which 15%-20% can be explained by gains or losses of transcription factor binding sites.

<a id="e34j"></a>**E34j** literature_search, Europe PMC abstract, PMID 33832990 (https://europepmc.org/article/MED/33832990; retrieved 2026-10-26T20:33:18+00:00)

> Finally, by augmenting the DeepMEL2 model with ChIP-seq data for GABPA, the TERT promoter mutation, as well as additional ETS motif gains, can be identified with high confidence.

<a id="e34k"></a>**E34k** literature_search, Europe PMC abstract, PMID 31802036 (https://europepmc.org/article/MED/31802036; retrieved 2026-10-26T20:33:18+00:00)

> TERT promoter mutations occur in the majority of glioblastoma, bladder cancer (BC), and other malignancies while the ETS family transcription factors GABPA and its partner GABPB1 activate the mutant TERT promoter and telomerase in these tumors.

<a id="e34l"></a>**E34l** literature_search, Europe PMC abstract, PMID 31802036 (https://europepmc.org/article/MED/31802036; retrieved 2026-10-26T20:33:18+00:00)

> GABPA depletion or the disruption of the GABPA/GABPB1 complex by knocking down GABPB1 was shown to inhibit telomerase, thereby eliminating the tumorigenic potential of glioblastoma cells.
