# TERT promoter C228T and Glioblastoma, melanoma, bladder

Configuration `no_qbic`, masked mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.02 over 8 model calls; 207 s.

Variant `chr5:1295113:G>A` (somatic); expression context: DepMap:subtype=Glioblastoma (median of 54 lines).

## Ranked chains

### 1. null: No TF-mediated effect of this variant (p = 0.45)

Null chain: no TF-mediated effect of this variant.

Predictions: The variant does not alter any TF binding at this base; TERT expression is not allele-dependent; Any disease association is due to a linked causal variant or a passenger mutation

Falsified if: Allele-specific TF binding or TERT expression is demonstrated in disease-relevant cells; The variant is shown to be the causal TERT promoter mutation rather than a passenger

### 2. chain_1: GABPA binds the alt allele and activates TERT (p = 0.40)

TF GABPA (QBiC-SELEX coverage own_model), alt allele binds more; element promoter; gene TERT; cell type glioblastoma/melanoma.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | GABPA is the leading ETS-family candidate: E04 lists GABPA among expressed TFs with a binding model found at this element in other biosamples, and E16 shows no GABPA peak in glioblastoma; no QBiC-SELEX model is available. The alt-A allele is inferred to bind GABPA more strongly because TERT is on the minus strand (E02), so the plus-strand G>A is a C>T change on the gene strand, the common TERT promoter mutation class (E15d), which is expected to create an ETS site; direct allele-specific occupancy is not shown. | missing | [E02](#e02), [E04](#e04), [E15d](#e15d), [E16](#e16) |
| element | E01 and E03 place the variant in the TERT promoter-like PLS EH38E3622530 with active chromatin marks; this supports promoter element localization, but not allele-specific activity. | supported | [E01](#e01), [E03](#e03) |
| gene | TERT is the nearest gene at 0 kb (E02), and TERT promoter mutations of this class are common in IDH-wildtype glioblastoma (E15d); this variant's direct effect on TERT is not demonstrated. | weak | [E02](#e02), [E15d](#e15d) |
| cell_type | TERT promoter mutations and telomerase activation are established in melanoma and glioblastoma (E15a, E15d, E15g), making these disease contexts plausible. | weak | [E15a](#e15a), [E15d](#e15d), [E15g](#e15g) |
| phenotype | Higher TERT/telomerase activity is associated with tumor progression in melanoma and glioblastoma (E15a, E15b, E15d, E15g); variant-specific causality is not shown. | weak | [E15a](#e15a), [E15b](#e15b), [E15d](#e15d), [E15g](#e15g) |

Predictions: The alt-A allele increases GABPA binding at this site; The alt-A allele increases TERT expression in relevant cells; GABPA depletion reduces TERT expression

Falsified if: The alt-A allele does not increase GABPA binding at this site; TERT expression is not allele-dependent in relevant cells; GABPA knockdown does not reduce TERT expression

### 3. chain_3: MAX binds the alt allele and activates TERT (p = 0.10)

TF MAX (QBiC-SELEX coverage own_model), alt allele binds more; element promoter; gene TERT; cell type glioblastoma/melanoma.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | MAX is expressed in glioblastoma (rank 48; E05) and has 13 ENCODE peaks containing this variant in other biosamples (E05), but no glioblastoma-matching peak, no QBiC-SELEX model, and no allele-specific assay are available; alt-A binding by MAX is therefore speculative. | missing | [E04](#e04), [E05](#e05) |
| element | The variant is in the TERT promoter-like PLS EH38E3622530 with active chromatin marks (E01, E03), consistent with a regulatory element, but allele-specific MAX activity is not shown. | supported | [E01](#e01), [E03](#e03) |
| gene | TERT is the nearest gene at 0 kb (E02), and TERT promoter mutations are common in IDH-wildtype glioblastoma (E15d); a direct MAX effect on this variant is not demonstrated. | weak | [E02](#e02), [E15d](#e15d) |
| cell_type | TERT promoter mutations and telomerase activation are relevant in melanoma and glioblastoma (E15a, E15d, E15g), making a TERT-regulatory mechanism plausible in these contexts. | weak | [E15a](#e15a), [E15d](#e15d), [E15g](#e15g) |
| phenotype | TERT/telomerase activity is associated with tumor progression in melanoma and glioblastoma (E15a, E15b, E15d, E15g); this chain's variant-specific MAX effect is unproven. | weak | [E15a](#e15a), [E15b](#e15b), [E15d](#e15d), [E15g](#e15g) |

Predictions: The alt-A allele increases MAX binding at this site; MAX depletion reduces TERT expression; The variant alters an E-box-like element

Falsified if: MAX does not occupy this site in relevant cells; The alt-A allele does not alter MAX binding; MAX depletion does not affect TERT expression

### 4. chain_2: GABPA binds the alt allele but represses TERT (p = 0.05)

TF GABPA (QBiC-SELEX coverage own_model), alt allele binds more; element promoter; gene TERT; cell type glioblastoma.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | GABPA is the leading ETS-family candidate and is inferred to bind the alt-A allele more strongly via the TERT promoter hotspot-like C>T change, but no QBiC-SELEX model or allele-specific occupancy assay is available; E04 lists GABPA among expressed TFs with binding elsewhere and E16 confirms no glioblastoma GABPA peak. | missing | [E02](#e02), [E04](#e04), [E15d](#e15d), [E16](#e16) |
| element | The variant lies in the TERT promoter-like PLS EH38E3622530 with active chromatin marks (E01, E03), so it could mediate repressive as well as activating TF effects; this is not demonstrated. | supported | [E01](#e01), [E03](#e03) |
| gene | TERT is the proximal target (E02); a masked cis SNP C allele has been associated with reduced TERT expression in TERT promoter-mutant glioblastoma (E15e), but this has not been shown for the present alt-A allele. | weak | [E02](#e02), [E15e](#e15e) |
| cell_type | TERT promoter-mutant glioblastoma is a relevant context (E15d), and a cis variant has been linked to altered TERT expression and prognosis in that setting (E15e), but not specifically for this allele. | weak | [E15d](#e15d), [E15e](#e15e) |
| phenotype | A masked cis SNP C allele with reduced TERT expression has been associated with poorer prognosis in TERT promoter-mutant glioblastoma (E15e), and TERT promoter status is prognostically relevant (E15g); this is not established for the present variant. | weak | [E15e](#e15e), [E15g](#e15g) |

Predictions: The alt-A allele increases GABPA binding; The alt-A allele lowers TERT expression; GABPA depletion increases TERT expression

Falsified if: The alt-A allele increases TERT expression; GABPA loss decreases rather than increases TERT expression; No allele-specific effect on TERT is observed

## Prediction matrix

| Test | Cost | Separates top two | null | chain_1 | chain_3 | chain_2 |
| --- | --- | --- | --- | --- | --- | --- |
| Allele-specific EMSA with recombinant GABPA on ref-G versus alt-A probes | low | yes | no GABPA allele-specific binding difference | alt-A probe binds GABPA more strongly than ref-G |  |  |
| Allele-specific GABPA ChIP-qPCR in a heterozygous TERT-expressing glioblastoma line | medium | yes | no allele-specific GABPA occupancy | alt-A allele shows more GABPA occupancy |  |  |
| TERT promoter reporter or MPRA with ref-G versus alt-A in glioblastoma cells | medium | yes | no allele-specific reporter activity | alt-A increases TERT reporter activity |  |  |
| Allele-specific TERT expression in heterozygous tumor cells | medium | yes | no allele-specific TERT expression | alt-A is associated with higher TERT expression |  |  |
| GABPA knockdown in TERT-expressing glioblastoma cells followed by TERT qPCR | medium | yes | no change in TERT expression | GABPA loss reduces TERT expression |  |  |

## Next experiment

Allele-specific EMSA with recombinant GABPA and ref-G versus alt-A probes

## Investigate calls

- chip_peaks({"tf": "GABPA", "biosample": "glioblastoma"})
- eqtl_lookup({"tissue": "Brain - Cortex"})
- literature_search({"query": "GABPA TERT promoter variant allele-specific binding glioblastoma"})

## Flags

- quote_rejected: PMID 40513567: not an exact substring of the abstract

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

> Understanding both telomere-dependent and -independent TERT functions is essential for developing effective biomarkers and therapies that overcome resistance and slow melanoma progression.

<a id="e15c"></a>**E15c** literature_search, Europe PMC abstract, PMID 42577103 (https://europepmc.org/article/MED/42577103; retrieved 2026-10-25T11:57:36+00:00)

> CDKN2A and CDK4 mutations act through UV-dependent and cell cycle disruption pathways, while BAP1, POT1, and TERT mutations are considered UV-independent.

<a id="e15d"></a>**E15d** literature_search, Europe PMC abstract, PMID 42804732 (https://europepmc.org/article/MED/42804732; retrieved 2026-10-25T11:57:36+00:00)

> Mutations in the telomerase reverse transcriptase (TERT) promoter region (TPM), particularly C228T and C250T, are common in IDH-wildtype glioblastoma (GBM).

<a id="e15e"></a>**E15e** literature_search, Europe PMC abstract, PMID 42804732 (https://europepmc.org/article/MED/42804732; retrieved 2026-10-25T11:57:36+00:00)

> The rs[masked] C allele may increase GBM susceptibility and, when in cis with TPM, is associated with reduced TERT expression and poorer prognosis, underscoring its biological and clinical significance in TPM-mutant GBM.

<a id="e15f"></a>**E15f** literature_search, Europe PMC abstract, PMID 42807929 (https://europepmc.org/article/MED/42807929; retrieved 2026-10-25T11:57:36+00:00)

> Additionally, loss of either USP10 or FOXM1 suppresses the expression of the downstream target Telomerase reverse transcriptase (TERT), triggering cellular senescence.

<a id="e15g"></a>**E15g** literature_search, Europe PMC abstract, PMID 42859331 (https://europepmc.org/article/MED/42859331; retrieved 2026-10-25T11:57:36+00:00)

> TERT promoter (TERTp) mutations are among the most frequent molecular alterations in isocitrate dehydrogenase (IDH) wild-type glioblastoma (GBM), yet the molecular profiles and prognostic implications associated with TERTp status remain incompletely characterized.

<a id="e15h"></a>**E15h** literature_search, Europe PMC abstract, PMID 42859331 (https://europepmc.org/article/MED/42859331; retrieved 2026-10-25T11:57:36+00:00)

> Among 112 patients, 70 (62.5%) harbored TERTp mutations.

<a id="e16"></a>**E16** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-25T11:58:44+00:00)

> No ENCODE GABPA ChIP-seq peak contains chr5:1295113:G>A in biosamples matching 'glioblastoma'. Absence can also mean no GABPA experiment in that biosample. In other biosamples, 2 GABPA peaks do contain the variant: HepG2, SK-N-SH (experiments ENCSR000BJK, ENCSR000BTG).

<a id="e17"></a>**E17** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr5_1295113_G_A_b38&datasetId=gtex_v8; retrieved 2026-10-26T20:18:37+00:00)

> 0 significant GTEx v8 single-tissue eQTLs for chr5_1295113_G_A_b38 in tissues matching 'Brain - Cortex'. NES is the effect of the alt allele (A) relative to ref (G).

<a id="e18"></a>**E18** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=GABPA%20TERT%20promoter%20variant%20allele-specific%20binding%20glioblastoma&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T20:18:37+00:00)

> Europe PMC: 46 hits for 'GABPA TERT promoter variant allele-specific binding glioblastoma'; top 8 with PMIDs:
> PMID 40513567 (2025): The immortality mechanism of TERT promoter mutant cancers is self-reinforcing and reversible.
> PMID 40822359 (2025): AURKB and PI3K/AKT/mTOR pathways converge to regulate &lt;i&gt;TERT&lt;/i&gt; expression.
> PMID 38033865 (2023): Reactivation of telomerase reverse transcriptase expression in cancer: the role of TERT promoter mutations.
> PMID 37918959 (2023): E4F1 and ZNF148 are transcriptional activators of the -57A &gt; C and wild-type &lt;i&gt;TERT&lt;/i&gt; promoter.
> PMID 38902506 (2024): Hidden secrets of the cancer genome: unlocking the impact of non-coding mutations in gene regulatory elements.
> PMID 40359938 (2025): Reannotation of cancer mutations based on expressed RNA transcripts reveals functional non-coding mutations in melanoma.
> PMID 36114166 (2022): Conserved features of TERT promoter duplications reveal an activation mechanism that mimics hotspot mutations in cancer.
> PMID 36713366 (2022): <i>TERT</i> promoter mutations and methylation for telomerase activation in urothelial carcinomas: New mechanistic insights and clinical significance.
