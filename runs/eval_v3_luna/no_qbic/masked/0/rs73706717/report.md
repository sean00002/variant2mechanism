# rs73706717 and Colorectal cancer (8q24)

Configuration `no_qbic`, masked mode, seed 0. Models: generator openai/gpt-6-luna, critic openai/gpt-6-luna, summariser openai/gpt-6-luna. Cost $0.01 over 7 model calls; 136 s.

Variant `chr8:127401265:T>C` (germline); expression context: DepMap:ACH-000971 (HCT 116).

## Ranked chains

### 1. H0: No TF-mediated effect of this variant (p = 0.90)

Null chain: no TF-mediated effect of this variant.

Predictions: The variant has no material TF-mediated effect on colorectal cancer; any association could reflect linkage or another mechanism.; Isogenic T-to-C editing will not produce a reproducible TF-dependent change in enhancer output or target-gene expression.

Falsified if: Isogenic editing shows a reproducible allelic regulatory effect that depends on a TF at this site and alters a relevant target gene.

### 2. H1: TCF7L2 binding on C increases POU5F1B expression (p = 0.04)

TF TCF7L2 (QBiC-SELEX coverage mapped), alt allele binds more; element The variant lies in enhancer-like cCRE EH38E3858447; whether this element is active in HCT116 is unestablished.; gene POU5F1B; cell type HCT116.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | This hypothesis proposes that alt C binds TCF7L2 more strongly than ref T; TCF7L2 is prioritized over other candidates because it is occupied at the site and expressed in HCT116, but no allele-specific binding or QBiC-SELEX model/result is provided to support this direction. | weak | [E04](#e04), [E05](#e05) |
| element | The variant lies within pELS cCRE EH38E3858447, although the reported chromatin maxima do not establish HCT116-specific activity. | supported | [E03](#e03) |
| gene | POU5F1B is a candidate, not a demonstrated target of this element; proximity and gene-level CRC evidence do not establish this variant-to-gene link, and no significant GTEx eQTL or CRC GWAS association is reported. | weak | [E01](#e01), [E02](#e02), [E15](#e15), [E16](#e16), [E17](#e17), [E18a](#e18a), [E18b](#e18b), [E18c](#e18c), [E19](#e19), [E20](#e20), [E21](#e21) |
| cell_type | HCT116 is a candidate context because TCF7L2 occupancy and expression are reported there, but a variant-dependent effect in these cells is not shown. | supported | [E04](#e04), [E05](#e05) |
| phenotype | If this chain raises POU5F1B in colorectal cells, it could promote cancer-associated phenotypes; the cited study does not connect those effects to this variant or TCF7L2. | supported | [E18a](#e18a), [E18b](#e18b) |

Predictions: Allele-specific TCF7L2 occupancy is higher on C than T in HCT116.; The C allele increases TCF7L2-dependent enhancer output and POU5F1B expression; reducing TCF7L2 activity removes the allelic difference.

Falsified if: Allele-specific assays show no greater TCF7L2 occupancy on C, or show greater occupancy on T.; A controlled allelic assay finds no TCF7L2-dependent difference in enhancer output or POU5F1B expression.

### 3. H3: SP1 binding on T increases POU5F1B expression (p = 0.04)

TF SP1 (QBiC-SELEX coverage own_model), ref allele binds more; element The variant lies in enhancer-like cCRE EH38E3858447; whether this element is active in HCT116 is unestablished.; gene POU5F1B; cell type HCT116.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | This hypothesis proposes that ref T binds SP1 more strongly than alt C; SP1 is prioritized because it is occupied at the site and expressed in HCT116, but no allele-specific binding or QBiC-SELEX model/result is provided to support this direction. | weak | [E04](#e04), [E06](#e06) |
| element | The variant lies within pELS cCRE EH38E3858447, although the reported chromatin maxima do not establish HCT116-specific activity. | supported | [E03](#e03) |
| gene | POU5F1B is a candidate, not a demonstrated target of this element; proximity and gene-level CRC evidence do not establish this variant-to-gene link, and no significant GTEx eQTL or CRC GWAS association is reported. | weak | [E01](#e01), [E02](#e02), [E15](#e15), [E16](#e16), [E17](#e17), [E18a](#e18a), [E18b](#e18b), [E18c](#e18c), [E19](#e19), [E20](#e20), [E21](#e21) |
| cell_type | HCT116 is a candidate context because SP1 occupancy and expression are reported there, but a variant-dependent effect in these cells is not shown. | supported | [E04](#e04), [E06](#e06) |
| phenotype | If this chain raises POU5F1B in colorectal cells, it could promote cancer-associated phenotypes; the cited study does not connect those effects to this variant or SP1. | supported | [E18a](#e18a), [E18b](#e18b) |

Predictions: Allele-specific SP1 occupancy is higher on T than C in HCT116.; The T allele increases SP1-dependent enhancer output and POU5F1B expression; reducing SP1 activity removes the allelic difference.

Falsified if: Allele-specific assays show no greater SP1 occupancy on T, or show greater occupancy on C.; A controlled allelic assay finds no SP1-dependent difference in enhancer output or POU5F1B expression.

### 4. H2: TCF7L2 binding on C represses POU5F1B expression (p = 0.02)

TF TCF7L2 (QBiC-SELEX coverage mapped), alt allele binds more; element The variant lies in enhancer-like cCRE EH38E3858447; whether this element is active in HCT116 is unestablished.; gene POU5F1B; cell type HCT116.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | This hypothesis proposes that alt C binds TCF7L2 more strongly than ref T; TCF7L2 is prioritized over other candidates because it is occupied at the site and expressed in HCT116, but no allele-specific binding or QBiC-SELEX model/result is provided to support this direction. | weak | [E04](#e04), [E05](#e05) |
| element | The variant lies within pELS cCRE EH38E3858447, although the reported chromatin maxima do not establish HCT116-specific activity. | supported | [E03](#e03) |
| gene | POU5F1B is a candidate, not a demonstrated target of this element; proximity and gene-level CRC evidence do not establish this variant-to-gene link, and no significant GTEx eQTL or CRC GWAS association is reported. | weak | [E01](#e01), [E02](#e02), [E15](#e15), [E16](#e16), [E17](#e17), [E18a](#e18a), [E18b](#e18b), [E18c](#e18c), [E19](#e19), [E20](#e20), [E21](#e21) |
| cell_type | HCT116 is a candidate context because TCF7L2 occupancy and expression are reported there, but variant-dependent repression in these cells is not shown. | supported | [E04](#e04), [E05](#e05) |
| phenotype | This chain predicts that reduced POU5F1B would reduce cancer-associated phenotypes, but the cited study reports effects of increased POU5F1B and does not test reduction or this variant. | weak | [E18a](#e18a), [E18b](#e18b) |

Predictions: Allele-specific TCF7L2 occupancy is higher on C than T in HCT116.; The C allele reduces TCF7L2-dependent enhancer output and POU5F1B expression; reducing TCF7L2 activity removes the allelic difference.

Falsified if: Allele-specific assays show no greater TCF7L2 occupancy on C, or show greater occupancy on T.; A controlled allelic assay finds no TCF7L2-dependent difference in enhancer output or POU5F1B expression, or finds that C increases rather than reduces expression.

## Prediction matrix

| Test | Cost | Separates top two | H0 | H1 | H3 | H2 |
| --- | --- | --- | --- | --- | --- | --- |
| Paired T- and C-allele enhancer reporter in HCT116, measured with control versus TCF7L2 depletion | medium | yes | No reproducible allele-dependent, TCF7L2-dependent reporter difference. | C reporter output exceeds T; TCF7L2 depletion removes or reduces the difference. | T reporter output exceeds C; the difference depends on SP1 rather than TCF7L2. | C reporter output is below T; TCF7L2 depletion removes or reduces the difference. |
| Allele-specific TCF7L2 and SP1 occupancy assay in HCT116 | medium | no | No reproducible allele-specific occupancy difference expected. | TCF7L2 occupancy is greater on C than T. | SP1 occupancy is greater on T than C. | TCF7L2 occupancy is greater on C than T. |
| Isogenic T-to-C editing in HCT116 followed by TF occupancy and POU5F1B expression measurements | high | no | No reproducible edit-associated TF-dependent occupancy or POU5F1B expression change. | C increases TCF7L2 occupancy and POU5F1B expression. | Changing T to C reduces SP1 occupancy and POU5F1B expression. | C increases TCF7L2 occupancy and reduces POU5F1B expression. |

## Next experiment

Run the paired T- and C-allele enhancer reporter in HCT116 with and without TCF7L2 depletion. It is the least costly proposed functional test of the top two chains: H1 predicts a C-dependent, TCF7L2-dependent increase in reporter output, whereas H0 predicts no such effect. A positive result would still require endogenous validation.

## Investigate calls

- eqtl_lookup({"tissue": "Colon - Transverse"})
- gene_disease({"gene": "POU5F1B"})
- literature_search({"query": "chr8:127401265 T C TCF7L2 SP1 colorectal cancer allele-specific enhancer"})

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

<a id="e19"></a>**E19** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr8_127401265_T_C_b38&datasetId=gtex_v8; retrieved 2026-10-26T02:23:32+00:00)

> 0 significant GTEx v8 single-tissue eQTLs for chr8_127401265_T_C_b38 in tissues matching 'Colon - Transverse'. NES is the effect of the alt allele (C) relative to ref (T).

<a id="e20"></a>**E20** gene_disease, Open Targets Platform (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-26T02:23:32+00:00)

> Open Targets: POU5F1B and colorectal cancer (MONDO_0005575), overall score 0.54; by evidence type: genetic_association 0.87, literature 0.18, rna_expression 0.14

<a id="e21"></a>**E21** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=chr8%3A127401265%20T%20C%20TCF7L2%20SP1%20colorectal%20cancer%20allele-specific%20enhancer&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T20:25:07+00:00)

> Europe PMC: 0 hits for 'chr8:127401265 T C TCF7L2 SP1 colorectal cancer allele-specific enhancer'; top 0 with PMIDs:
