# rs73706717 and Colorectal cancer (8q24)

Configuration `full`, masked mode, seed 0. Models: generator openai/gpt-6-luna, critic openai/gpt-6-luna, summariser openai/gpt-6-luna. Cost $0.01 over 6 model calls; 108 s.

Variant `chr8:127401265:T>C` (germline); expression context: DepMap:ACH-000971 (HCT 116).

## QBiC-SELEX screen (occupancy first)

Occupied candidates: TCF7L2 (bound here, z -8.8, weak site); SP1 (bound here, z -7.07, weak site); NFIC (bound elsewhere, z 24.28); NFIA (bound elsewhere, z 24.28); HNF1B (bound elsewhere, z -23.93); CTCF (bound elsewhere, z 8.21); CEBPB (bound elsewhere, z -6.94); TFAP4 (bound elsewhere, z 0.51, no clear allelic change); NR2F2 (bound elsewhere, z -15.02, weak site); NR2F6 (bound elsewhere, z -15.02, weak site). Occupancy unknown: ZBTB22 (z -33.75); NR1H3 (z -15.02); TET3 (z 14.12); NR1D2 (z -13.82); NR4A2 (z -13.82). Diagnostic, not shown to the model: 307 of 997 models pass Bonferroni.

## Ranked chains

### 1. H0: Null: no TF-mediated effect of this variant (p = 0.66)

Null chain: no TF-mediated effect of this variant.

Predictions: The T and C alleles show no reproducible, variant-dependent difference in occupancy of the candidate TFs or in expression of a linked gene.; Any colorectal-cancer association, if present, arises from another linked variant or another mechanism.

Falsified if: Isogenic T-to-C editing reproducibly changes occupancy of a TF at this site and changes a linked gene's expression in a manner rescued by perturbing that TF.

### 2. H1: TCF7L2 binding may be modestly reduced on the C allele (p = 0.17)

TF TCF7L2 (QBiC-SELEX coverage mapped), ref allele binds more; element EH38E3858447; gene POU5F1B; cell type HCT116.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | TCF7L2 is expressed and has a ChIP-seq peak over the variant in HCT116, but the ref-favored QBiC-SELEX result comes from a TCF7-mapped model, not a TCF7L2-specific model; the modeled site is weak, so this is indirect evidence for a TCF7L2 allelic effect and the peak may reflect another site in the element. | weak | [E05](#e05), [E19](#e19), [E20](#e20), [E35](#e35) |
| element | The variant lies in pELS cCRE EH38E3858447, although the available activity-score maxima do not establish activity in HCT116. | supported | [E03](#e03) |
| gene | POU5F1B is a candidate target based on proximity and gene-level CRC evidence, but the low-PIP credible sets concern non-CRC traits and no significant GTEx eQTL or enhancer-to-gene link is reported. | weak | [E02](#e02), [E16](#e16), [E17](#e17), [E37](#e37) |
| cell_type | HCT116 is a plausible context because TCF7L2 occupancy over the variant and expression are reported there; allele-specific occupancy has not been demonstrated. | supported | [E05](#e05), [E20](#e20) |
| phenotype | POU5F1B has some gene-level CRC plausibility, but the evidence does not establish that this variant changes POU5F1B or affects CRC risk. | weak | [E15](#e15), [E18a](#e18a), [E18b](#e18b), [E18c](#e18c), [E37](#e37) |

Predictions: If TCF7L2 occupies the variant-centered site in HCT116, T should show greater TCF7L2 occupancy than C; this prediction is uncertain because the QBiC-SELEX model is TCF7-mapped and the modeled site is weak.; Any variant-dependent POU5F1B expression effect attributed to this chain should depend on TCF7L2; the direction of the expression change is not determined by the binding result.

Falsified if: A sensitive allele-specific assay finds no T-versus-C TCF7L2 occupancy difference under conditions with confirmed TCF7L2 occupancy.; A variant-dependent POU5F1B expression difference persists after TCF7L2 perturbation.

### 3. H2: SP1 binding may be modestly reduced on the C allele (p = 0.11)

TF SP1 (QBiC-SELEX coverage own_model), ref allele binds more; element EH38E3858447; gene POU5F1B; cell type HCT116.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | SP1 is expressed and has a ChIP-seq peak over the variant in HCT116, but the ref-favored QBiC-SELEX result uses an SP3-mapped model rather than an SP1-specific model; the modeled site is weak, so the result is indirect for SP1 and the peak may reflect another site in the element. | weak | [E06](#e06), [E19](#e19), [E21](#e21) |
| element | The variant lies in pELS cCRE EH38E3858447, while the reported activity-score maxima do not confirm activity in HCT116. | supported | [E03](#e03) |
| gene | POU5F1B is a candidate target based on proximity and gene-level CRC evidence, but the low-PIP credible sets concern non-CRC traits and no significant GTEx eQTL or enhancer-to-gene link is reported. | weak | [E02](#e02), [E16](#e16), [E17](#e17), [E37](#e37) |
| cell_type | HCT116 is a plausible context because SP1 occupancy over the variant and expression are reported there; allele-specific occupancy has not been demonstrated. | supported | [E06](#e06), [E21](#e21) |
| phenotype | POU5F1B has some gene-level CRC plausibility, but the evidence does not establish that this variant changes POU5F1B or affects CRC risk. | weak | [E15](#e15), [E18a](#e18a), [E18b](#e18b), [E18c](#e18c), [E37](#e37) |

Predictions: If SP1 binds the variant-centered site in HCT116, T should show greater SP1 occupancy than C; this prediction is uncertain because the displayed QBiC-SELEX model is SP3-mapped and the site is weak.; Any variant-dependent POU5F1B expression effect attributed to this chain should depend on SP1 rather than TCF7L2; the direction of the expression change is not determined by binding.

Falsified if: A sensitive allele-specific assay finds no T-versus-C SP1 occupancy difference under conditions with confirmed SP1 occupancy.; A variant-dependent POU5F1B expression difference persists after SP1 perturbation.

### 4. H3: NFIC binding may be stronger on the C allele, with relevant-cell occupancy unresolved (p = 0.06)

TF NFIC (QBiC-SELEX coverage own_model), alt allele binds more; element EH38E3858447; gene POU5F1B; cell type HCT116.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | QBiC-SELEX predicts stronger binding to C using an NFIB-mapped model, not an NFIC-specific model; the modeled site is strong, but the reported NFIC peak over the variant is from HepG2, so NFIC occupancy at this site in HCT116 is not established. | weak | [E19](#e19), [E22](#e22) |
| element | The variant lies in pELS cCRE EH38E3858447, but the available activity-score maxima do not establish activity in HCT116. | supported | [E03](#e03) |
| gene | POU5F1B is a candidate target based on proximity and gene-level CRC evidence, but the low-PIP credible sets concern non-CRC traits and no significant GTEx eQTL or enhancer-to-gene link is reported. | weak | [E02](#e02), [E16](#e16), [E17](#e17), [E37](#e37) |
| cell_type | HCT116 is a possible context because NFIC is expressed there, but its occupancy over the variant in HCT116 is unresolved; the absence of an ENCODE experiment in that biosample is not evidence for or against occupancy. | weak | [E22](#e22), [E36](#e36) |
| phenotype | POU5F1B has some gene-level CRC plausibility, but the evidence does not establish an NFIC-mediated variant effect on POU5F1B or CRC risk. | weak | [E15](#e15), [E18a](#e18a), [E18b](#e18b), [E18c](#e18c), [E37](#e37) |

Predictions: If NFIC occupies the variant-centered site in HCT116, C should show greater NFIC occupancy than T; the binding prediction is indirect because it uses an NFIB-mapped model.; Any variant-dependent POU5F1B expression effect attributed to this chain should depend on NFIC in a cell context where NFIC occupies the site; the direction of the expression change is not determined by binding.

Falsified if: A sensitive assay confirms NFIC occupancy in relevant cells but finds no greater occupancy on C than T.; A variant-dependent POU5F1B expression difference persists after NFIC perturbation.

## Prediction matrix

| Test | Cost | Separates top two | H0 | H1 | H2 | H3 |
| --- | --- | --- | --- | --- | --- | --- |
| Allele-specific TCF7L2 CUT&RUN or ChIP-qPCR at the variant in HCT116 | medium | yes | No reproducible T-versus-C occupancy difference attributable to the variant. | Greater TCF7L2 occupancy on T than C, if TCF7L2 binds the variant-centered site. | No required TCF7L2 allelic difference; any effect should instead track SP1. | No required TCF7L2 allelic difference; any effect should instead track NFIC. |
| Allele-specific SP1 CUT&RUN or ChIP-qPCR at the variant in HCT116 | medium | no | No reproducible T-versus-C occupancy difference attributable to the variant. | No required SP1 allelic difference; any effect should instead track TCF7L2. | Greater SP1 occupancy on T than C, if SP1 binds the variant-centered site. | No required SP1 allelic difference; any effect should instead track NFIC. |
| Measure NFIC occupancy and allele-specific binding at the variant in HCT116 | medium | no | No reproducible variant-dependent NFIC occupancy difference. | No required NFIC allelic difference; any effect should instead track TCF7L2. | No required NFIC allelic difference; any effect should instead track SP1. | NFIC occupancy is detected, with greater occupancy on C than T. |
| Isogenic T-to-C editing in HCT116, followed by POU5F1B expression measurement and candidate-TF perturbation | high | yes | No reproducible allele-dependent POU5F1B expression change rescued by perturbing one of the proposed TFs. | A variant-dependent POU5F1B expression change that depends on TCF7L2; its direction is not predicted. | A variant-dependent POU5F1B expression change that depends on SP1; its direction is not predicted. | A variant-dependent POU5F1B expression change that depends on NFIC; its direction is not predicted. |

## Next experiment

Run a low-cost allele-specific EMSA using T- and C-containing probes with HCT116 nuclear extract and a TCF7L2 supershift or antibody competition. Greater T-probe binding that is specifically attributable to TCF7L2 would support H1 over the null; no allele difference would favor the null, though this in vitro test would not establish a target-gene or disease effect.

## Refinement rounds

Stopped: round 1 left the top chain and the grades of its links unchanged.

### Round 1

- qbic_tf_detail({"tf": "TCF7L2"}) for H1.binding, ran as [E35](#e35). Expected: If the detail confirms the prediction is only from a TCF7-mapped model, H1.binding remains weak; if it provides a TCF7L2-specific model with the same ref-favored direction, H1.binding gains support and H1 rises.
- chip_peaks({"tf": "NFIC", "biosample": "HCT116"}) for H3.cell_type, ran as [E36](#e36) (no experiment). Expected: If an NFIC peak contains the variant in HCT116, H3.cell_type gains support and H3 becomes more competitive; if no peak is found, H3.cell_type remains weak and H3 falls.
- gene_disease({"gene": "POU5F1B"}) for H1.phenotype, ran as [E37](#e37). Expected: If Open Targets shows CRC-specific gene-disease evidence, the POU5F1B phenotype link gains support across chains using this target; if evidence is absent or unrelated to CRC, the link remains weak and the null gains relative weight.

- Result of qbic_tf_detail({"tf":"TCF7L2"}): E35 reports that the significant ref-favored result is from a TCF7-mapped model; the other mapped models do not pass the detection gate. It does not provide a TCF7L2-specific model. (as expected: yes)
- Result of chip_peaks({"tf":"NFIC","biosample":"HCT116"}): E36 reports no NFIC ChIP-seq experiment in HCT116. This is not a negative occupancy result and does not change the evidence for or against H3 occupancy in HCT116. (as expected: unclear)
- Result of gene_disease({"gene":"POU5F1B"}): E37 reports an Open Targets colorectal-cancer overall score of 0.54, with genetic_association the strongest evidence type (0.87); this adds gene-level CRC plausibility but does not establish this variant's mechanism or effect. (as expected: yes)

Chains after revision: null 0.66; TCF7L2 0.17; SP1 0.11; NFIC 0.06. Link grades changed: none.

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

<a id="e35"></a>**E35** qbic_tf_detail, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> {"tf":"TCF7L2","symbol":"TCF7L2","via":"hgnc_symbol","notes":[],"coverage":"mapped","variant":"chr8:127401265:T>C","gate_p":5.02e-05,"models":[{"model":"LEF1_FL_TAGTCG40NAGA_KZ_yin2017_0_3_7mer","mapping":"CIS-BP (LEF1)","group":"G041 HMG/Sox, 3 models","quality":0.63,"effect":-0.306,"z":-2.77,"p":0.0056,"rank_abs_z":"461/997","passed_gate":false,"site_strength":{"ref_percentile":81.3,"alt_percentile":95.3,"k":7}},{"model":"TCF7_eDBD_TCGGAC40NCCA_KS_yin2017_0_3_7mer","mapping":"CIS-BP (TCF7)","group":"G041 HMG/Sox, 3 models","quality":0.732,"effect":-0.429,"z":-8.8,"p":1.4e-18,"rank_abs_z":"66/997","passed_gate":true,"site_strength":{"ref_percentile":90.0,"alt_percentile":87.2,"k":7}},{"model":"TCF7L1_eDBD_TTGGCA40NTCG_KW_yin2017_0_3_7mer","mapping":"CIS-BP (TCF7L1)","group":"G041 HMG/Sox, 3 models","quality":0.602,"effect":-0.242,"z":-3.57,"p":0.00036,"rank_abs_z":"359/997","passed_gate":false,"site_strength":{"ref_percentile":84.6,"alt_percentile":58.3,"k":7}}]}

<a id="e36"></a>**E36** chip_peaks, ENCODE experiment search (https://www.encodeproject.org/search/?type=Experiment&assay_title=TF+ChIP-seq&status=released&assembly=GRCh38&format=json&limit=all&field=target.label&field=biosample_ontology.term_name&field=accession; retrieved local)

> ENCODE has no NFIC ChIP-seq experiment in biosamples matching 'HCT116', so this says nothing about NFIC occupancy there, for or against. ENCODE assayed NFIC in: GM12878, HepG2, Ishikawa, K562, SK-N-SH.

<a id="e37"></a>**E37** gene_disease, Open Targets Platform (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-26T02:23:32+00:00)

> Open Targets: POU5F1B and colorectal cancer (MONDO_0005575), overall score 0.54; by evidence type: genetic_association 0.87, literature 0.18, rna_expression 0.14
