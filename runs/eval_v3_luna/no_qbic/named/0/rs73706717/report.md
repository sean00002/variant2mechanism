# rs73706717 and Colorectal cancer (8q24)

Configuration `no_qbic`, named mode, seed 0. Models: generator openai/gpt-6-luna, critic openai/gpt-6-luna, summariser openai/gpt-6-luna. Cost $0.01 over 9 model calls; 169 s.

Variant `chr8:127401265:T>C` (germline); expression context: DepMap:ACH-000971 (HCT 116).

## Ranked chains

### 1. H0: No TF-mediated effect of rs73706717 (p = 0.84)

Null chain: no TF-mediated effect of this variant.

Predictions: Editing T to C will not reproducibly cause a TF-dependent change in occupancy, enhancer output, or expression of a disease-relevant gene.; Any disease association, if established, will be attributable to another variant or mechanism rather than a TF-mediated effect of this base.

Falsified if: In an appropriate colorectal model, editing this base reproducibly changes allele-specific TF occupancy and enhancer output, with a corresponding target-gene expression change.

### 2. H1: TCF7L2-mediated effect on POU5F1B (p = 0.08)

TF TCF7L2 (QBiC-SELEX coverage mapped), alt allele binds more; element EH38E3858447; gene POU5F1B; cell type HCT 116.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | TCF7L2 occupies the variant and is expressed in HCT116. I nominate it because this is direct matching-cell occupancy evidence, not because its peak count exceeds SP1's. Alt-C-greater binding is a testable direction for this chain, not an observed result; no TCF7L2 QBiC-SELEX model or allele-specific occupancy result is supplied. | weak | [E04](#e04), [E05](#e05) |
| element | The variant lies in pELS cCRE EH38E3858447, with enhancer-associated marks reported as maxima across biosamples; HCT116-specific enhancer activity is not established. | supported | [E01](#e01), [E03](#e03) |
| gene | POU5F1B is a candidate target based on proximity and the cCRE's nearby-gene annotation; gene-level colorectal-cancer evidence makes it relevant to investigate, but does not show that this element regulates it. No significant eQTL or molecular QTL for this variant is reported. | supported | [E02](#e02), [E03](#e03), [E16](#e16), [E17](#e17), [E19](#e19), [E20](#e20) |
| cell_type | HCT116 is a plausible context because TCF7L2 occupancy at the variant and expression in this cell line are reported. | supported | [E05](#e05) |
| phenotype | A POU5F1B expression change could be relevant to colorectal cancer, but the cited gene-level evidence does not connect this variant or TCF7L2 to the phenotype. No GWAS Catalog association for this variant is reported. | supported | [E15](#e15), [E18a](#e18a), [E18b](#e18b), [E20](#e20) |

Predictions: Relative to ref-T, alt-C will show greater TCF7L2 occupancy at this site; this direction is a hypothesis, not supported by the supplied allele-specific evidence.; If this chain is correct, perturbing the variant or its cCRE will produce a reproducible POU5F1B expression effect; the direction of that expression effect is not specified by the evidence.

Falsified if: A sufficiently powered allele-specific assay shows no alt-C increase in TCF7L2 occupancy, or variant/cCRE perturbation has no effect on POU5F1B expression while showing a reproducible effect on another proposed target.

### 3. H3: SP1-mediated effect on POU5F1B (p = 0.05)

TF SP1 (QBiC-SELEX coverage own_model), ref allele binds more; element EH38E3858447; gene POU5F1B; cell type HCT 116.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | SP1 occupies the variant and is expressed in HCT116. I nominate it because of this direct matching-cell evidence; ref-T-greater binding is a testable direction for this chain, not an observed result. No SP1 QBiC-SELEX model or allele-specific occupancy result is supplied. | weak | [E04](#e04), [E06](#e06) |
| element | The variant lies in pELS cCRE EH38E3858447, with enhancer-associated marks reported as maxima across biosamples; HCT116-specific enhancer activity is not established. | supported | [E01](#e01), [E03](#e03) |
| gene | POU5F1B is a candidate target based on proximity and the cCRE's nearby-gene annotation, and has gene-level colorectal-cancer evidence; neither establishes regulation by this cCRE. No significant eQTL or molecular QTL for this variant is reported. | supported | [E02](#e02), [E03](#e03), [E16](#e16), [E17](#e17), [E19](#e19), [E20](#e20) |
| cell_type | HCT116 is a plausible context because SP1 occupancy at the variant and expression in this cell line are reported. | supported | [E06](#e06) |
| phenotype | A POU5F1B expression change could be relevant to colorectal cancer, but the supplied gene-level evidence does not implicate SP1 or this variant in that effect. | supported | [E15](#e15), [E18a](#e18a), [E18b](#e18b), [E20](#e20) |

Predictions: Relative to alt-C, ref-T will show greater SP1 occupancy at this site; this direction is a hypothesis, not supported by the supplied allele-specific evidence.; If this chain is correct, variant or cCRE perturbation will produce a reproducible POU5F1B expression effect, and the effect will depend on SP1.

Falsified if: A sufficiently powered allele-specific assay shows no ref-T increase in SP1 occupancy, or SP1 perturbation does not alter a variant-dependent POU5F1B response.

### 4. H2: TCF7L2-mediated effect on MYC (p = 0.03)

TF TCF7L2 (QBiC-SELEX coverage mapped), alt allele binds more; element EH38E3858447; gene MYC; cell type HCT 116.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | TCF7L2 occupies the variant and is expressed in HCT116. Alt-C-greater binding is a testable direction for this chain, not an observed result; no TCF7L2 QBiC-SELEX model or allele-specific occupancy result is supplied. | weak | [E04](#e04), [E05](#e05) |
| element | The variant lies in pELS cCRE EH38E3858447, but the reported chromatin-mark maxima do not establish HCT116-specific enhancer activity. | supported | [E01](#e01), [E03](#e03) |
| gene | MYC is within 1 Mb, making it a possible distal candidate, but the cCRE's listed nearby genes do not include MYC and no supplied evidence connects this element to MYC. | supported | [E02](#e02), [E03](#e03) |
| cell_type | HCT116 is a plausible context because TCF7L2 occupancy at the variant and expression in this cell line are reported. | supported | [E05](#e05) |
| phenotype | A variant-to-cCRE-to-MYC effect on colorectal cancer is a possibility to test, but the supplied evidence does not demonstrate that chain or a colorectal-cancer association for this variant. | missing | [E15](#e15), [E16](#e16), [E17](#e17), [E19](#e19) |

Predictions: Relative to ref-T, alt-C will show greater TCF7L2 occupancy at this site; this direction is a hypothesis, not supported by the supplied allele-specific evidence.; If this chain is correct, variant or cCRE perturbation will affect MYC expression; an effect limited to POU5F1B would not support this target assignment.

Falsified if: A sufficiently powered allele-specific assay shows no alt-C increase in TCF7L2 occupancy, or variant/cCRE perturbation has no effect on MYC expression while showing a reproducible effect on another proposed target.

## Prediction matrix

| Test | Cost | Separates top two | H0 | H1 | H3 | H2 |
| --- | --- | --- | --- | --- | --- | --- |
| Measure allele-specific TCF7L2 occupancy by ChIP-qPCR with amplicon sequencing in heterozygous HCT116 cells, using matched input to control allelic imbalance. | low | yes | No reproducible allele-specific TCF7L2 occupancy. | Greater occupancy on alt-C than ref-T. | No required allele-specific TCF7L2 occupancy; this chain instead predicts a ref-T advantage for SP1. | Greater occupancy on alt-C than ref-T. |
| Measure allele-specific SP1 occupancy by ChIP-qPCR with amplicon sequencing in heterozygous HCT116 cells, using matched input. | low | no | No reproducible allele-specific SP1 occupancy. | No required allele-specific SP1 occupancy. | Greater occupancy on ref-T than alt-C. | No required allele-specific SP1 occupancy. |
| Create isogenic T-to-C and C-to-T edits in HCT116 cells and measure TCF7L2/SP1 occupancy, enhancer output, and POU5F1B and MYC expression. | high | no | No reproducible variant-dependent TF occupancy, enhancer-output, or target-expression change. | Alt-C increases TCF7L2 occupancy and editing changes enhancer output and POU5F1B expression. | Ref-T increases SP1 occupancy and editing changes enhancer output and POU5F1B expression. | Alt-C increases TCF7L2 occupancy and editing changes enhancer output and MYC expression. |

## Next experiment

The cheapest proposed test separating the two highest-probability chains (H0 and H1) is allele-specific TCF7L2 ChIP-qPCR with amplicon sequencing in heterozygous HCT116 cells and matched input. It tests the predicted alt-C occupancy advantage against the null prediction of no reproducible allelic imbalance; first confirm that the cells are heterozygous at rs73706717.

## Investigate calls

- eqtl_lookup({"tissue": "Colon - Sigmoid"})
- gene_disease({"gene": "POU5F1B"})
- literature_search({"query": "rs73706717 colorectal cancer functional enhancer allele-specific"})

## Flags

- literature_fallback: no hits for 'rs73706717 AND POU5F1B AND "colorectal cancer"'; dropped the rsID

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

> A few potential regulatory influences on CRC development associated with genes and variants, such as POU5F1B and rs10797801, were identified.

<a id="e18d"></a>**E18d** literature_search, Europe PMC abstract, PMID 40506516 (https://europepmc.org/article/MED/40506516; retrieved 2026-10-26T02:21:59+00:00)

> Four regions mapped to POU5F1B, POU2AF2 (c11orf53)/POU2AF3 (COLCA2), GREM1 and CABLES2 were previously identified.

<a id="e19"></a>**E19** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr8_127401265_T_C_b38&datasetId=gtex_v8; retrieved 2026-10-26T02:23:32+00:00)

> 0 significant GTEx v8 single-tissue eQTLs for chr8_127401265_T_C_b38 in tissues matching 'Colon - Sigmoid'. NES is the effect of the alt allele (C) relative to ref (T).

<a id="e20"></a>**E20** gene_disease, Open Targets Platform (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-26T02:23:32+00:00)

> Open Targets: POU5F1B and colorectal cancer (MONDO_0005575), overall score 0.54; by evidence type: genetic_association 0.87, literature 0.18, rna_expression 0.14

<a id="e21"></a>**E21** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=rs73706717%20colorectal%20cancer%20functional%20enhancer%20allele-specific&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T13:30:22+00:00)

> Europe PMC: 1 hits for 'rs73706717 colorectal cancer functional enhancer allele-specific'; top 1 with PMIDs:
> PMID 22429595 (2012): Characterization of the colorectal cancer-associated enhancer MYC-335 at 8q24: the role of rs67491583.
