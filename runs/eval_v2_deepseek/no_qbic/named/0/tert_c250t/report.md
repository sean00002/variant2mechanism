# TERT promoter C250T and Glioblastoma, melanoma, bladder

Configuration `no_qbic`, named mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.05 over 10 model calls; 241 s.

Variant `chr5:1295135:G>A` (somatic); expression context: DepMap:subtype=Glioblastoma (median of 54 lines).

## Ranked chains

### 1. H0_no_TF_mediated_effect: No TF-mediated allelic effect at C250T (p = 0.45)

Null chain: no TF-mediated effect of this variant.

Predictions: No reproducible allele-specific TF occupancy at chr5:1295135 in the relevant cancer cell context.; TERT expression differences, if present, are driven by a linked variant, another base, or a passenger/hotspot effect rather than a TF binding change at this nucleotide.; The active promoter cCRE signal reflects the general TERT promoter region but not an allelic TF effect at this base.

Falsified if: An allele-specific TF binding difference at this exact base is demonstrated in glioblastoma or another matched cell type.; The alt allele changes TERT expression in a TF-dependent manner at this nucleotide.; A linked causal variant is excluded and this base itself drives the phenotype.

### 2. H1_GABPA_ETS_TERT_activation: GABPA binds the C250T-created ETS site and activates TERT (p = 0.42)

TF GABPA (QBiC-SELEX coverage own_model), alt allele binds more; element active promoter-like cCRE EH38E3622530; gene TERT; cell type Glioblastoma.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | GABPA is the leading ETS-family candidate to bind the alt A allele more strongly: C250T creates a de novo ETS motif, and GABPA/GABPB1 have been reported to activate the mutant TERT promoter in glioblastoma and bladder cancer. GABPA is expressed in DepMap glioblastoma lines, but GABPA ChIP peaks containing this variant are only in non-glioblastoma ENCODE biosamples, and no GABPA QBiC-SELEX model is provided, so alt-A preference is inferred rather than directly measured. | missing | [E16b](#e16b), [E18k](#e18k), [E11](#e11), [E04](#e04) |
| element | The variant lies in the promoter-like cCRE EH38E3622530 with DNase, H3K27ac, and H3K4me3 signal, consistent with an active promoter element; the z-scores are maxima over ENCODE biosamples, not glioblastoma-specific. | supported | [E03](#e03) |
| gene | TERT is the nearest gene, 0 kb from its TSS, and the variant is annotated as upstream of TERT in a TERT promoter regulatory feature. | supported | [E01](#e01), [E02](#e02) |
| cell_type | Glioblastoma is a plausible matched context because GABPA is expressed in DepMap glioblastoma lines and GABPA/GABPB1 have been implicated at the mutant TERT promoter in glioblastoma and bladder cancer. | supported | [E11](#e11), [E18k](#e18k) |
| phenotype | If alt-enhanced GABPA binding activates this promoter, it should increase TERT/telomerase; GABPA/GABPB1 activation of the mutant TERT promoter and telomerase has been reported in these tumors, and TERT promoter mutations are a primary cause of telomerase reactivation. | weak | [E18k](#e18k), [E16f](#e16f), [E16g](#e16g) |

Predictions: Recombinant GABPA/GABPB1 or allele-specific GABPA ChIP shows stronger binding to the alt A allele at chr5:1295135.; GABPA or GABPB1 knockdown reduces TERT expression or C250T reporter activity in glioblastoma cells.; The alt allele increases TERT expression in a GABPA-dependent manner in C250T-heterozygous cancer cells.

Falsified if: Allele-specific GABPA ChIP, EMSA, or reporter assay shows no alt-A preference at chr5:1295135.; GABPA or GABPB1 knockdown does not reduce TERT expression or mutant TERT promoter activity in C250T-containing glioblastoma cells.; GABPA occupancy at this base is not detectable in glioblastoma despite an active local promoter.

### 3. H4_ETS1_NFkB_TERT_activation: ETS1 with non-canonical NF-kB binds the C250T ETS site and activates TERT (p = 0.08)

TF ETS1 (QBiC-SELEX coverage own_model), alt allele binds more; element active promoter-like cCRE EH38E3622530; gene TERT; cell type Glioblastoma.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | ETS1 is an alternative ETS-family candidate because C250T creates an ETS motif and C250T mutant TERT promoter activation has been reported to involve ETS1/2 together with non-canonical NF-kB signalling. No ETS1 QBiC-SELEX model or matched glioblastoma ChIP occupancy at this base is provided, so alt-A preference is literature/motif-inferred and weak. | missing | [E18](#e18), [E18j](#e18j), [E16b](#e16b) |
| element | The variant lies in the active promoter-like cCRE EH38E3622530 marked by DNase, H3K27ac, and H3K4me3. | supported | [E03](#e03) |
| gene | TERT is the nearest promoter-proximal gene, 0 kb from its TSS, with the variant upstream of TERT. | supported | [E01](#e01), [E02](#e02) |
| cell_type | The glioblastoma context for ETS1 is not directly established by the provided expression or occupancy data; this chain relies on broader TERT/cancer literature and is therefore weaker than H1 at the cell-type step. | missing | [E15](#e15) |
| phenotype | If ETS1/NF-kB cooperatively activates the C250T promoter, alt-enhanced ETS1 binding should raise TERT/telomerase and support tumor proliferation. | weak | [E18j](#e18j), [E16f](#e16f) |

Predictions: Allele-specific ETS1 ChIP shows stronger binding to the alt A allele at this base.; Non-canonical NF-kB inhibition reduces TERT expression specifically in C250T mutant cells.; ETS1 knockdown reduces C250T mutant TERT promoter activity.

Falsified if: Allele-specific ETS1 ChIP or EMSA shows no alt-A preference at this base.; Non-canonical NF-kB inhibition does not reduce C250T-dependent TERT expression.; ETS1 perturbation does not affect mutant TERT promoter activity in C250T cells.

### 4. H5_ETV5_MAX_TERT_activation: ETV5/MAX binds the C250T ETS site and activates TERT (p = 0.05)

TF ETV5 (QBiC-SELEX coverage own_model), alt allele binds more; element active promoter-like cCRE EH38E3622530; gene TERT; cell type Glioblastoma.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | ETV5 is a third ETS-family candidate: ETV5 and MAX have been reported to synergistically activate hTERT through composite Ets/E-box motifs. However, no ETV5 QBiC-SELEX model, ETV5 ChIP peak over this variant, or ETV5 expression in glioblastoma is provided; MAX is expressed in glioblastoma and bound elsewhere near this variant, so this chain is speculative and weak. | missing | [E18d](#e18d), [E18e](#e18e), [E05](#e05), [E04](#e04) |
| element | The variant lies in the active promoter-like cCRE EH38E3622530. | supported | [E03](#e03) |
| gene | TERT is the nearest gene, 0 kb from the TSS, and the variant is upstream of TERT. | supported | [E01](#e01), [E02](#e02) |
| cell_type | MAX is expressed in DepMap glioblastoma lines, but ETV5 expression and occupancy in glioblastoma are not provided; the cell-type link is incomplete and relies on the ETV5/MAX literature in other cells. | missing | [E05](#e05), [E18e](#e18e) |
| phenotype | If ETV5/MAX cooperatively activates hTERT at this promoter, alt-enhanced ETV5 binding should increase TERT/telomerase and support tumor cell proliferation. | weak | [E18e](#e18e), [E16f](#e16f) |

Predictions: ETV5 binds the alt A allele more strongly in an allele-specific assay at this base.; ETV5 or MAX knockdown reduces TERT expression in C250T mutant cells.; The C250T allele shows an ETV5/MAX-dependent composite ETS/E-box response.

Falsified if: ETV5 does not bind the ref/alt alleles differentially at this base.; ETV5 or MAX perturbation does not change TERT expression in C250T cells.; The variant does not contribute to an ETS/E-box composite response at the TERT promoter.

## Prediction matrix

| Test | Cost | Separates top two | H0_no_TF_mediated_effect | H1_GABPA_ETS_TERT_activation | H4_ETS1_NFkB_TERT_activation | H5_ETV5_MAX_TERT_activation |
| --- | --- | --- | --- | --- | --- | --- |
| Allele-specific EMSA with recombinant GABPA/GABPB1 on ref G and alt A oligos | low | yes | ref and alt oligos show equal or no GABPA/GABPB1 shift | alt A gives stronger GABPA/GABPB1 shift than ref G | no GABPA-specific allelic shift expected; GABPA is not the named TF | no GABPA-specific allelic shift expected; GABPA is not the named TF |
| Allele-specific GABPA ChIP-qPCR in C250T-heterozygous glioblastoma cells | medium | yes | no reproducible allele-specific GABPA occupancy | GABPA ChIP is stronger on the alt A allele at chr5:1295135 | no GABPA allelic preference; ETS1, not GABPA, is the predicted binder | no GABPA allelic preference; ETV5, not GABPA, is the predicted binder |
| GABPA or GABPB1 knockdown followed by TERT qPCR in C250T glioblastoma cells | medium | yes | GABPA/GABPB1 knockdown does not change TERT expression | GABPA or GABPB1 knockdown reduces TERT expression | GABPA/GABPB1 knockdown has little effect; NF-kB/ETS1 axis is required instead | GABPA/GABPB1 knockdown has little effect; ETV5/MAX axis is required instead |
| Allele-specific ETS1 ChIP-qPCR or ETS1 knockdown in C250T glioblastoma cells | medium | no | no reproducible allele-specific ETS1 occupancy | no ETS1 allelic preference or ETS1 dependence | ETS1 ChIP is stronger on alt A and ETS1 knockdown reduces TERT | no ETS1 allelic preference or ETS1 dependence |
| Non-canonical NF-kB inhibition in C250T glioblastoma cells with TERT readout | low | no | no allele-specific TF effect to inhibit | little or no NF-kB dependence of C250T TERT expression | non-canonical NF-kB inhibition reduces C250T-dependent TERT expression | little or no NF-kB dependence of C250T TERT expression |
| ETV5 or MAX knockdown followed by TERT qPCR in C250T glioblastoma cells | medium | no | ETV5/MAX perturbation has no allele-specific effect | ETV5/MAX perturbation has little effect on TERT | ETV5/MAX perturbation has little effect on TERT | ETV5 or MAX knockdown reduces TERT expression |

## Next experiment

Allele-specific EMSA using recombinant GABPA/GABPB1 on ref G versus alt A oligos at chr5:1295135; this is the cheapest test that separates the top two chains, H1_GABPA_ETS_TERT_activation versus H0_no_TF_mediated_effect.

## Investigate calls

- literature_search({"query": "TERT promoter C250T GABPA ETS motif allele-specific binding"})
- literature_search({"query": "TERT promoter mutation C250T AP-1 JUN BHLHE40 binding"})
- literature_search({"query": "TERT promoter -146 C>T C250T creates ETS binding site reporter luciferase"})

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
> PMID 42804732 (2026): SNP rs2853669 potentially elevates the risk of glioblastoma development and leads to worse prognosis when in cis with mutant TERT promoter in a Japanese cohort.
> PMID 42807929 (2026): USP10 stabilizes FOXM1 through KAT5-mediated acetylation to suppress cell senescence and promote melanoma malignant progression.
> PMID 42859331 (2026): CDKN2A deletion associated with poor prognosis in patients with TERT promoter wild-type, IDH wild-type glioblastoma.

<a id="e16"></a>**E16** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TERT%20promoter%20C250T%20GABPA%20ETS%20motif%20allele-specific%20binding&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T02:24:26+00:00)

> Europe PMC: 27 hits for 'TERT promoter C250T GABPA ETS motif allele-specific binding'; top 8 with PMIDs:
> PMID 39557834 (2024): Mechanistic basis of atypical TERT promoter mutations.
> PMID 40822359 (2025): AURKB and PI3K/AKT/mTOR pathways converge to regulate &lt;i&gt;TERT&lt;/i&gt; expression.
> PMID 41639451 (2026): Regulatory grammar in human promoters uncovered by MPRA-based deep learning.
> PMID 36713366 (2022): <i>TERT</i> promoter mutations and methylation for telomerase activation in urothelial carcinomas: New mechanistic insights and clinical significance.
> PMID 38033865 (2023): Reactivation of telomerase reverse transcriptase expression in cancer: the role of TERT promoter mutations.
> PMID 36394204 (2022): Thyroid carcinoma-featured telomerase activation and telomere maintenance: Biology and translational/clinical significance.
> PMID 38285162 (2024): Mechanisms of telomere maintenance and associated therapeutic vulnerabilities in malignant gliomas.
> PMID 40272676 (2025): TERT Amplification a Risk Stratification Marker in Papillary Thyroid Carcinoma, Significantly Correlated with Tumor Recurrence and Survival.

<a id="e16a"></a>**E16a** literature_search, Europe PMC abstract, PMID 39557834 (https://europepmc.org/article/MED/39557834; retrieved 2026-10-26T02:24:26+00:00)

> Here, we show that atypical TERTp mutations arise secondary to canonical TERTp mutations in a two-step process.

<a id="e16b"></a>**E16b** literature_search, Europe PMC abstract, PMID 39557834 (https://europepmc.org/article/MED/39557834; retrieved 2026-10-26T02:24:26+00:00)

> Canonical TERTp mutations create de novo binding sites for ETS family transcription factors that induce favourable conditions for DNA damage formation by UV light, thus creating a hotspot effect but only after a first mutational hit.

<a id="e16c"></a>**E16c** literature_search, Europe PMC abstract, PMID 40822359 (https://europepmc.org/article/MED/40822359; retrieved 2026-10-26T02:24:26+00:00)

> Further analyses using quantitative PCR, immunoprecipitation (IP), and chromatin IP in thyroid cell models revealed that although both TERTp MUT and wild-type promoters are governed by these pathways, distinct factors mediate each mechanism.

<a id="e16d"></a>**E16d** literature_search, Europe PMC abstract, PMID 40822359 (https://europepmc.org/article/MED/40822359; retrieved 2026-10-26T02:24:26+00:00)

> Specifically, AURKB, via REST, is recruited to TERTp MUT by TRIM28.

<a id="e16e"></a>**E16e** literature_search, Europe PMC abstract, PMID 36713366 (https://europepmc.org/article/MED/36713366; retrieved 2026-10-26T02:24:26+00:00)

> Recent mechanistic explorations have revealed important roles for TERT promoter mutations and aberrant methylation in activation of TERT transcription and telomerase in UCs.

<a id="e16f"></a>**E16f** literature_search, Europe PMC abstract, PMID 38033865 (https://europepmc.org/article/MED/38033865; retrieved 2026-10-26T02:24:26+00:00)

> Point mutations in the core promoter region of the telomerase reverse transcriptase (TERT) gene have been found to occur at high frequencies in several tumour types and considered a primary cause of telomerase reactivation in cancer cells.

<a id="e16g"></a>**E16g** literature_search, Europe PMC abstract, PMID 38033865 (https://europepmc.org/article/MED/38033865; retrieved 2026-10-26T02:24:26+00:00)

> These mutations promote TERT gene expression by multiple mechanisms, including the generation of novel binding sites for nuclear transcription factors, displacement of negative regulators from DNA G-quadruplexes, recruitment of epigenetic activators and disruption of long-range interactions between TERT locus and telomeres.

<a id="e16h"></a>**E16h** literature_search, Europe PMC abstract, PMID 36394204 (https://europepmc.org/article/MED/36394204; retrieved 2026-10-26T02:24:26+00:00)

> The genomic alterations of the TERT loci including TERT promoter's gain-of-function mutations, copy number gain, fusion and rearrangements, have recently been identified in TCs as mechanisms to induce TERT expression and to activate telomerase.

<a id="e16i"></a>**E16i** literature_search, Europe PMC abstract, PMID 40272676 (https://europepmc.org/article/MED/40272676; retrieved 2026-10-26T02:24:26+00:00)

> TERT amplification correlated with TERTp mutations in PTC (P = 0.0313) and PIK3CA mutations in ATC (P = 0.0272).

<a id="e17"></a>**E17** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TERT%20promoter%20mutation%20C250T%20AP-1%20JUN%20BHLHE40%20binding&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T02:24:36+00:00)

> Europe PMC: 1 hits for 'TERT promoter mutation C250T AP-1 JUN BHLHE40 binding'; top 0 with PMIDs:

<a id="e18"></a>**E18** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TERT%20promoter%20-146%20C%3ET%20C250T%20creates%20ETS%20binding%20site%20reporter%20luciferase&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T02:24:37+00:00)

> Europe PMC: 9 hits for 'TERT promoter -146 C>T C250T creates ETS binding site reporter luciferase'; top 8 with PMIDs:
> PMID 38241433 (2024): High UV damage and low repair, but not cytosine deamination, stimulate mutation hotspots at ETS binding sites in melanoma.
> PMID 41303422 (2025): Telomere Maintenance and Oncogenesis.
> PMID 33375021 (2020): Co-Occurrence of Hotspot Point Mutation and Novel Deletion Mutation of <i>TERT</i> Promoter in Solid Variant Papillary Thyroid Carcinoma in a Patient with Synchronous Esophageal Cancer.
> PMID 32518154 (2020): ETS variant transcription factor 5 and c-Myc cooperate in derepressing the human telomerase gene promoter via composite ETS/E-box motifs.
> PMID 35927480 (2022): PROBER identifies proteins associated with programmable sequence-specific DNA in living cells.
> PMID 30010853 (2018): TERT promoter mutations are associated with poor prognosis and cell immortalization in meningioma.
> PMID 26389665 (2015): Non-canonical NF-κB signalling and ETS1/2 cooperatively drive C250T mutant TERT promoter activation.
> PMID 31802036 (2020): GABPA is a master regulator of luminal identity and restrains aggressive diseases in bladder cancer.

<a id="e18a"></a>**E18a** literature_search, Europe PMC abstract, PMID 38241433 (https://europepmc.org/article/MED/38241433; retrieved 2026-10-26T02:24:37+00:00)

> Noncoding mutation hotspots have been identified in melanoma and many of them occur at the binding sites of E26 transformation-specific (ETS) proteins; however, their formation mechanism and functional impacts are not fully understood.

<a id="e18b"></a>**E18b** literature_search, Europe PMC abstract, PMID 38241433 (https://europepmc.org/article/MED/38241433; retrieved 2026-10-26T02:24:37+00:00)

> Finally, we analyzed a subset of frequently mutated promoters, including the ribosomal protein genes RPL13A and RPS20, and found that mutations in the ETS motif can significantly reduce the promoter activity.

<a id="e18c"></a>**E18c** literature_search, Europe PMC abstract, PMID 33375021 (https://europepmc.org/article/MED/33375021; retrieved 2026-10-26T02:24:37+00:00)

> Two substitution mutations, C228T (c.1-124C>T) and C250T (c.1-146C>T), make up most of the mutations and occur in a mutually exclusive manner.

<a id="e18d"></a>**E18d** literature_search, Europe PMC abstract, PMID 32518154 (https://europepmc.org/article/MED/32518154; retrieved 2026-10-26T02:24:37+00:00)

> Here, we report that the ETS family protein ETS variant transcription factor 5 (ETV5) mediates epidermal growth factor (EGF)-induced hTERT expression in MCF10A cells.

<a id="e18e"></a>**E18e** literature_search, Europe PMC abstract, PMID 32518154 (https://europepmc.org/article/MED/32518154; retrieved 2026-10-26T02:24:37+00:00)

> Using chromatinized bacterial artificial chromosome (BAC) reporters in human fibroblasts, we found that ETV5 and c-Myc/MYC-associated factor X (MAX) synergistically activate the hTERT promoter via two identical, but inverted, composite Ets/E-box motifs enclosing the core promoter.

<a id="e18f"></a>**E18f** literature_search, Europe PMC abstract, PMID 35927480 (https://europepmc.org/article/MED/35927480; retrieved 2026-10-26T02:24:37+00:00)

> PROBER identified alterations in regulator associations due to cancer hotspot mutations in the hTERT promoter, indicating that these mutations increase promoter association with specific gene activators.

<a id="e18g"></a>**E18g** literature_search, Europe PMC abstract, PMID 30010853 (https://europepmc.org/article/MED/30010853; retrieved 2026-10-26T02:24:37+00:00)

> From 110 meningioma patients, 128 tissue samples were analyzed for the TERT promoter mutations C228T and C250T by direct sequencing.

<a id="e18h"></a>**E18h** literature_search, Europe PMC abstract, PMID 30010853 (https://europepmc.org/article/MED/30010853; retrieved 2026-10-26T02:24:37+00:00)

> Impact of the E-twenty-six (ETS) transcription factor inhibitor YK-4-279 on cell viability and TERT promoter activity was analyzed.

<a id="e18i"></a>**E18i** literature_search, Europe PMC abstract, PMID 26389665 (https://europepmc.org/article/MED/26389665; retrieved 2026-10-26T02:24:37+00:00)

> The recent discovery of two prevalent somatic mutations-C250T and C228T-in the TERT promoter in various cancers has provided insight into a plausible mechanism of TERT reactivation.

<a id="e18j"></a>**E18j** literature_search, Europe PMC abstract, PMID 26389665 (https://europepmc.org/article/MED/26389665; retrieved 2026-10-26T02:24:37+00:00)

> Although the two hotspot mutations create a similar binding motif for E-twenty-six (ETS) transcription factors, we show that they are functionally distinct, in that the C250T unlike the C228T TERT promoter is driven by non-canonical NF-κB signalling.

<a id="e18k"></a>**E18k** literature_search, Europe PMC abstract, PMID 31802036 (https://europepmc.org/article/MED/31802036; retrieved 2026-10-26T02:24:37+00:00)

> TERT promoter mutations occur in the majority of glioblastoma, bladder cancer (BC), and other malignancies while the ETS family transcription factors GABPA and its partner GABPB1 activate the mutant TERT promoter and telomerase in these tumors.
