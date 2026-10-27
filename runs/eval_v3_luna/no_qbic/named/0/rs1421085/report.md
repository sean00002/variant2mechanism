# rs1421085 and Obesity (FTO)

Configuration `no_qbic`, named mode, seed 0. Models: generator openai/gpt-6-luna, critic openai/gpt-6-luna, summariser openai/gpt-6-luna. Cost $0.01 over 8 model calls; 155 s.

Variant `chr16:53767042:T>C` (germline); expression context: GTEx:Adipose - Subcutaneous (proxy for preadipocytes).

## Ranked chains

### 1. H1: No demonstrated TF-mediated effect (p = 0.90)

Null chain: no TF-mediated effect of this variant.

Predictions: The available evidence does not establish that this substitution changes binding of a TF in relevant adipose-lineage cells. The obesity association could reflect another mechanism or a linked causal change.; Deletion of the broader conserved regulatory module can affect Irx3 and Irx5 in mice, but that result does not establish an allele-specific TF effect of rs1421085.

Falsified if: A relevant adipose-lineage assay shows allele-specific occupancy of a TF at rs1421085 and a corresponding allele-dependent regulatory output.

### 2. H2: Weak, unverified JUN-dependent regulatory hypothesis (p = 0.05)

TF JUN (QBiC-SELEX coverage own_model), ref allele binds more; element The variant lies in a distal enhancer-like cCRE within a conserved cis-regulatory module; activity in the relevant human adipose-lineage context is not established.; gene IRX3/IRX5; cell type Adipocytes; the supporting perturbation evidence is from mice, and JUN occupancy in human adipose-lineage cells is not shown..

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | JUN is included only as a weak candidate: it is expressed and has a variant-overlapping peak in HepG2, but no matching adipose peak is reported. This hypothesis provisionally predicts stronger binding to ref T; no allele-specific QBiC-SELEX result is provided, so that direction is unverified. The evidence does not prioritize JUN over other detected TFs. | missing | [E04](#e04), [E05](#e05), [E19](#e19) |
| element | The variant lies in the distal enhancer-like cCRE EH38E3181208. A deletion of the rs1421085 conserved cis-regulatory module affects Irx3 and Irx5 in mice, but neither result establishes adipose-specific activity of this human element. | supported | [E03](#e03), [E21a](#e21a) |
| gene | IRX3 and IRX5 are candidate regulatory targets because deletion of the module altered their expression in mice; this does not show that JUN mediates the effect or that the variant allele regulates either gene. FTO remains a strong locus-to-gene candidate, but a JUN-to-FTO link is not shown. | supported | [E02](#e02), [E16](#e16), [E21a](#e21a) |
| cell_type | Adipocytes are a plausible context for the broader module because its deletion affected adipocyte phenotypes in mice. JUN occupancy at the variant in relevant adipose-lineage cells has not been demonstrated. | supported | [E05](#e05), [E19](#e19), [E21a](#e21a), [E21b](#e21b) |
| phenotype | The variant is associated with obesity, and module deletion affects obesity-relevant mouse phenotypes, but the evidence does not connect JUN binding or a JUN-mediated regulatory direction to the human association. | supported | [E15](#e15), [E16](#e16), [E21b](#e21b) |

Predictions: In relevant adipose-lineage cells, JUN should occupy the site and show greater occupancy on T than C; this is a testable assumption, not an observed result.; If this chain is correct, JUN perturbation should alter an allele-dependent regulatory output from the module, potentially involving IRX3 or IRX5.

Falsified if: JUN is not detectably bound at the site in relevant adipose-lineage cells, or allele-specific assays show no T-versus-C occupancy difference.; JUN perturbation produces no allele-dependent change in the regulatory output of the module.

### 3. H3: Weak, unverified KLF6-dependent regulatory hypothesis (p = 0.05)

TF KLF6 (QBiC-SELEX coverage own_model), ref allele binds more; element The variant lies in a distal enhancer-like cCRE within a conserved cis-regulatory module; activity in the relevant human adipose-lineage context is not established.; gene IRX3/IRX5; cell type Adipocytes; the supporting perturbation evidence is from mice, and KLF6 occupancy in human adipose-lineage cells is not shown..

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | KLF6 is included only as a weak candidate: it is expressed and has a variant-overlapping peak in HepG2, but no matching adipose peak is reported. This hypothesis provisionally predicts stronger binding to ref T; no allele-specific QBiC-SELEX result is provided, so that direction is unverified. The evidence does not prioritize KLF6 over other detected TFs. | missing | [E04](#e04), [E06](#e06), [E20](#e20) |
| element | The variant lies in the distal enhancer-like cCRE EH38E3181208. A deletion of the rs1421085 conserved cis-regulatory module affects Irx3 and Irx5 in mice, but neither result establishes adipose-specific activity of this human element. | supported | [E03](#e03), [E21a](#e21a) |
| gene | IRX3 and IRX5 are candidate regulatory targets because deletion of the module altered their expression in mice; this does not show that KLF6 mediates the effect or that the variant allele regulates either gene. FTO remains a strong locus-to-gene candidate, but a KLF6-to-FTO link is not shown. | supported | [E02](#e02), [E16](#e16), [E21a](#e21a) |
| cell_type | Adipocytes are a plausible context for the broader module because its deletion affected adipocyte phenotypes in mice. KLF6 occupancy at the variant in relevant adipose-lineage cells has not been demonstrated. | supported | [E06](#e06), [E20](#e20), [E21a](#e21a), [E21b](#e21b) |
| phenotype | The variant is associated with obesity, and module deletion affects obesity-relevant mouse phenotypes, but the evidence does not connect KLF6 binding or a KLF6-mediated regulatory direction to the human association. | supported | [E15](#e15), [E16](#e16), [E21b](#e21b) |

Predictions: In relevant adipose-lineage cells, KLF6 should occupy the site and show greater occupancy on T than C; this is a testable assumption, not an observed result.; If this chain is correct, KLF6 perturbation should alter an allele-dependent regulatory output from the module, potentially involving IRX3 or IRX5.

Falsified if: KLF6 is not detectably bound at the site in relevant adipose-lineage cells, or allele-specific assays show no T-versus-C occupancy difference.; KLF6 perturbation produces no allele-dependent change in the regulatory output of the module.

## Prediction matrix

| Test | Cost | Separates top two | H1 | H2 | H3 |
| --- | --- | --- | --- | --- | --- |
| Allele-specific JUN CUT&RUN in heterozygous human adipose-lineage preadipocytes, with reads assigned to T and C | medium | yes | No reproducible JUN occupancy at the site or no T-versus-C occupancy imbalance. | JUN occupies the site and occupancy is greater on T than C. | No JUN occupancy imbalance is required; this chain instead predicts a KLF6-specific effect. |
| Allele-specific KLF6 CUT&RUN in heterozygous human adipose-lineage preadipocytes, with reads assigned to T and C | medium | no | No reproducible KLF6 occupancy at the site or no T-versus-C occupancy imbalance. | No KLF6 occupancy imbalance is required; this chain instead predicts a JUN-specific effect. | KLF6 occupies the site and occupancy is greater on T than C. |
| Perturb JUN and KLF6 separately in variant-genotyped adipose-lineage cells, then measure allele-dependent expression of IRX3 and IRX5 | high | yes | No reproducible allele-dependent regulatory effect attributable to either TF. | JUN perturbation changes an allele-dependent IRX3/IRX5 output; KLF6 perturbation does not show the predicted specific effect. | KLF6 perturbation changes an allele-dependent IRX3/IRX5 output; JUN perturbation does not show the predicted specific effect. |

## Next experiment

The cheapest direct test separating the top two hypotheses is allele-specific JUN CUT&RUN in heterozygous human adipose-lineage preadipocytes, with targeted sequencing across rs1421085. H1 predicts no reproducible T-versus-C occupancy imbalance; H2 predicts greater JUN occupancy on T.

## Investigate calls

- chip_peaks({"tf": "JUN", "biosample": "adipose"})
- chip_peaks({"tf": "KLF6", "biosample": "adipose"})
- literature_search({"query": "rs1421085 FTO enhancer adipocyte perturbation target gene ARID5B IRX3 IRX5"})

## Flags

- none

Citation support: 1.00 of links cite only evidence that passed every check.

## Evidence

<a id="e01"></a>**E01** variant_annotation, Ensembl VEP (GRCh38) (https://rest.ensembl.org/vep/human/region/16:53767042-53767042:1/C?content-type=application/json&Conservation=1; retrieved 2026-10-25T17:38:25+00:00)

> Variant chr16:53767042:T>C (GRCh38), allele string T/C
> Known IDs: rs1421085
> Most severe consequence: intron_variant
> Regulatory features: none
> GERP conservation score at the site: 2.55
> Transcript consequences: FTO (intron_variant, NMD_transcript_variant); FTO (intron_variant); FTO (intron_variant, non_coding_transcript_variant)

<a id="e02"></a>**E02** nearest_genes, Ensembl overlap (protein_coding) (https://rest.ensembl.org/overlap/region/human/16:52767042-54767042?feature=gene;biotype=protein_coding;content-type=application/json; retrieved 2026-10-25T17:38:17+00:00)

> 7 protein-coding genes within 1000 kb of chr16:53767042:T>C, by distance to TSS:
> RPGRIP1L: 63.1 kb from TSS (upstream, strand -1)
> FTO: 65.3 kb from TSS (in gene body, strand +1)
> AKTIP: 262.6 kb from TSS (upstream, strand -1)
> RBL2: 333.1 kb from TSS (downstream, strand +1)
> IRX3: 520.4 kb from TSS (downstream, strand -1)
> CHD9: 712.1 kb from TSS (downstream, strand +1)
> CHD9NB: 714.1 kb from TSS (upstream, strand -1)

<a id="e03"></a>**E03** ccre_lookup, ENCODE v4 cCRE registry (ENCFF420VPZ) and SCREEN (https://screen-beta-api.wenglab.org/dataws/cre_table; retrieved 2026-10-25T17:29:02+00:00)

> The variant lies in cCRE EH38E3181208 (dELS: distal enhancer-like), chr16:53766999-53767220.
> SCREEN: 1 cCREs within 500 bp (max z-score across ENCODE biosamples):
> EH38E3181207 dELS: DNase z 3.5, H3K27ac z 3.2, H3K4me3 z 1.5, CTCF z 1.5; nearby genes RPGRIP1L, FTO, AC007497.1
> Biosample-specific z-scores are not in this call; the values above are maxima over biosamples.

<a id="e04"></a>**E04** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> ENCODE TF ChIP-seq at chr16:53767042:T>C: 39 peaks contain the variant, from 37 factors in 4 biosamples. No ENCODE biosample matches the expression context, so no peak counts as bound here. cCRE class at the variant: dELS. Bound factors outside the TF model collection (co-factors, Pol II, and TFs with no binding model; signs of an active element, not TF candidates): ASH2L, DMAP1, EHMT2, EP300, HBP1, IKZF5, KAT2B, LCORL, MED1, POLR2AphosphoS5, RBFOX2, RNF219 (+6 more). Bound, expressed TFs with a binding model: 16; listed one per row: JUN, KLF6, USF2, HMG20B, ATF3, MAX, SP1, TEAD1, ZGPAT, GATAD2A; also bound: PHF21A, ZNF335, FOXP1, ZNF449, ZNF280D, ZNF48. Bound but below 1 TPM: HNF1A, MIXL1, ONECUT1. Assayed with no peak here: 0 TFs in the matching biosample, 554 only elsewhere; never assayed: 536.

<a id="e05"></a>**E05** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> JUN: bound elsewhere. 1 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: HepG2 (e.g. ENCSR747VUU). 442.88 TPM in GTEx:Adipose - Subcutaneous (proxy for preadipocytes), rank 3 of 1631 TFs.

<a id="e06"></a>**E06** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> KLF6: bound elsewhere. 1 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: HepG2 (e.g. ENCSR757EKM). 247.5 TPM in GTEx:Adipose - Subcutaneous (proxy for preadipocytes), rank 11 of 1631 TFs.

<a id="e07"></a>**E07** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> USF2: bound elsewhere. 1 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: HepG2 (e.g. ENCSR145QNL). 114.23 TPM in GTEx:Adipose - Subcutaneous (proxy for preadipocytes), rank 31 of 1631 TFs.

<a id="e08"></a>**E08** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> HMG20B: bound elsewhere. 1 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: HepG2 (e.g. ENCSR925QAW). 84.43 TPM in GTEx:Adipose - Subcutaneous (proxy for preadipocytes), rank 51 of 1631 TFs.

<a id="e09"></a>**E09** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> ATF3: bound elsewhere. 1 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: HCT116 (e.g. ENCSR000BUG). 57.63 TPM in GTEx:Adipose - Subcutaneous (proxy for preadipocytes), rank 88 of 1631 TFs.

<a id="e10"></a>**E10** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> MAX: bound elsewhere. 1 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: HepG2 (e.g. ENCSR168DYA). 41.99 TPM in GTEx:Adipose - Subcutaneous (proxy for preadipocytes), rank 141 of 1631 TFs.

<a id="e11"></a>**E11** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> SP1: bound elsewhere. 1 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: HCT116 (e.g. ENCSR000BSF). 41.01 TPM in GTEx:Adipose - Subcutaneous (proxy for preadipocytes), rank 145 of 1631 TFs.

<a id="e12"></a>**E12** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> TEAD1: bound elsewhere. 1 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: HepG2 (e.g. ENCSR497JLX). 40.88 TPM in GTEx:Adipose - Subcutaneous (proxy for preadipocytes), rank 148 of 1631 TFs.

<a id="e13"></a>**E13** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> ZGPAT: bound elsewhere. 1 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: HepG2 (e.g. ENCSR704IGU). 30.27 TPM in GTEx:Adipose - Subcutaneous (proxy for preadipocytes), rank 211 of 1631 TFs.

<a id="e14"></a>**E14** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> GATAD2A: bound elsewhere. 1 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: HepG2 (e.g. ENCSR925BFV). 25.37 TPM in GTEx:Adipose - Subcutaneous (proxy for preadipocytes), rank 260 of 1631 TFs.

<a id="e15"></a>**E15** gwas_lookup, GWAS Catalog REST v2 (https://www.ebi.ac.uk/gwas/rest/api/v2/associations?rs_id=rs1421085&size=100; retrieved 2026-10-25T17:29:17+00:00)

> 100 GWAS Catalog associations for rs1421085, strongest first:
> Body mass index (BMI, mean, inv-normal transformed): p 9.9e-324, effect allele T, risk-allele frequency 0.669, PMID 39024449
> Body mass index (BMI, maximum, inv-normal transformed): p 9.9e-324, effect allele T, risk-allele frequency 0.669, PMID 39024449
> What is your weight? (pounds, inv-normal transformed): p 9.9e-324, effect allele T, risk-allele frequency 0.5909, PMID 39024449
> Weight (mean, inv-normal transformed): p 2.0e-300, effect allele T, risk-allele frequency 0.669, PMID 39024449
> Obesity (PheCode 278.1): p 6.0e-291, effect allele T, risk-allele frequency 0.593, PMID 39024449
> Body mass index (BMI, minimum, inv-normal transformed): p 2.0e-277, effect allele T, risk-allele frequency 0.669, PMID 39024449
> Overweight, obesity and other hyperalimentation (PheCode 278): p 4.0e-246, effect allele T, risk-allele frequency 0.5927, PMID 39024449
> Body shape phenotype PC1: p 2.0e-241, effect allele T, risk-allele frequency 0.596423, PMID 38640244
> Type 2 diabetes (PheCode 250.2): p 4.0e-211, effect allele T, risk-allele frequency 0.5926, PMID 39024449
> Diabetes mellitus (PheCode 250): p 8.0e-207, effect allele T, risk-allele frequency 0.5926, PMID 39024449
> Hemoglobin A1c (HbA1c, maximum, inv-norm transformed): p 8.0e-195, effect allele T, risk-allele frequency 0.5901, PMID 39024449
> Hemoglobin A1c (HbA1c, mean, inv-norm transformed): p 1.0e-185, effect allele T, risk-allele frequency 0.5901, PMID 39024449

<a id="e16"></a>**E16** finemap_lookup, Open Targets Platform (credible sets, L2G) (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-25T17:29:10+00:00)

> 1701 credible sets contain 16_53767042_T_C: 200 GWAS, 0 molecular QTL.
> GWAS Body mass index (BMI, minimum, inv-normal transformed): PIP 0.85; L2G FTO 0.99, RPGRIP1L 0.20, CHD9 0.06
> GWAS Body mass index: PIP 0.80; L2G FTO 0.99, RPGRIP1L 0.25
> GWAS Impedance of leg left (UKB data field 23108): PIP 0.67; L2G FTO 0.99, RPGRIP1L 0.20
> GWAS Diabetes mellitus (PheCode 250): PIP 0.46; L2G FTO 0.99, RPGRIP1L 0.20, CHD9 0.06
> GWAS Impedance of leg left (UKB data field 23108): PIP 0.46; L2G FTO 0.99, RPGRIP1L 0.20
> GWAS Leg fat free mass left (UKB data field 23117): PIP 0.41; L2G FTO 0.99, RPGRIP1L 0.21, CHD9 0.07
> Best L2G gene scores across these sets: FTO 0.99, RPGRIP1L 0.36, CHD9 0.16

<a id="e17"></a>**E17** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr16_53767042_T_C_b38&datasetId=gtex_v8; retrieved 2026-10-25T17:30:38+00:00)

> 2 significant GTEx v8 single-tissue eQTLs for chr16_53767042_T_C_b38. NES is the effect of the alt allele (C) relative to ref (T).
> FTO in Muscle_Skeletal: NES +0.14, p 7.5e-08
> IRX3 in Pancreas: NES +0.37, p 8.3e-06

<a id="e18"></a>**E18** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=rs1421085%20AND%20FTO%20AND%20%22obesity%22&format=json&pageSize=8&resultType=core; retrieved 2026-10-25T17:29:18+00:00)

> Europe PMC: 653 hits for 'rs1421085 AND FTO AND "obesity"'; top 8 with PMIDs:
> PMID 42440472 (2026): A Rapid Genotyping Assay for &lt;i&gt;FTO&lt;/i&gt; and &lt;i&gt;PPAR-γ&lt;/i&gt; Nutrigenetic Variants in Thai Adults with Overweight/Obesity.
> PMID 41862896 (2026): Impact of fat mass and obesity-associated (FTO) gene variants on adult obesity and overweight: a comprehensive meta-analysis.
> PMID 41591493 (2026): Obesity-related RNA m&lt;sup&gt;6&lt;/sup&gt;A demethylase gene FTO rs1421085 is associated with neuroticism in a longitudinal birth cohort study.
> PMID 42197023 (2026): Associations Between FTO rs9939609 Genotype, Physical Activity, and Dietary Behaviors in Young Adults.
> PMID 42757464 (2026): Demethylase FTO attenuates atherosclerotic plaque via upregulating ABCA1 and ABCG1 expression by targeting ATG5.
> PMID 42299366 (2026): Hepatogenomics of MAFLD in Asian Population: Genetic Polymorphisms and Pathway-Based Insights.
> PMID 42534632 (2025): Genetic Polymorphisms Associated with Obesity in Southeast Asian Populations: A Systematic Review without Meta-Analysis.
> PMID 42245481 (2026): FTO in cardiovascular diseases: mechanisms, context dependence, and translational opportunities.

<a id="e18a"></a>**E18a** literature_search, Europe PMC abstract, PMID 42440472 (https://europepmc.org/article/MED/42440472; retrieved 2026-10-25T17:29:18+00:00)

> The aim of this study is to develop, validate, and apply a cost-effective 4-plex high-resolution melting (HRM) assay for simultaneous detection of FTO (rs9939609 and rs1421085) and PPAR-γ (rs1801282 and rs3856806) variants using standard laboratory equipment.

<a id="e18b"></a>**E18b** literature_search, Europe PMC abstract, PMID 41862896 (https://europepmc.org/article/MED/41862896; retrieved 2026-10-25T17:29:18+00:00)

> In the obesity group, the rs1421085 exhibited the strongest effect, with an odds ratio (OR) of 2.16 (95% CI: 1.58–2.95).

<a id="e18c"></a>**E18c** literature_search, Europe PMC abstract, PMID 41862896 (https://europepmc.org/article/MED/41862896; retrieved 2026-10-25T17:29:18+00:00)

> This meta-analysis provides strong evidence that FTO polymorphisms, particularly rs1421085 and rs9939609, are significantly associated with increased susceptibility to obesity in adults, while their impact on overweight is comparatively weaker.

<a id="e18d"></a>**E18d** literature_search, Europe PMC abstract, PMID 41591493 (https://europepmc.org/article/MED/41591493; retrieved 2026-10-25T17:29:18+00:00)

> Based on findings that experimental manipulation of the RNA m6A methylation in animal experiments can affect anxiety, and given that the C-allele of FTO rs1421085 had a significant association with indicators of overweight and obesity in our previous study, we have examined the possible association of FTO rs1421085 genotype with neuroticism in the same longitudinally observed sample.

<a id="e18e"></a>**E18e** literature_search, Europe PMC abstract, PMID 41591493 (https://europepmc.org/article/MED/41591493; retrieved 2026-10-25T17:29:18+00:00)

> Conclusively, an overweight and obesity-related variant of FTO, the gene encoding an RNA m6A demethylase, was associated with lower neuroticism, this association being subject to gender and cohort effects.

<a id="e18f"></a>**E18f** literature_search, Europe PMC abstract, PMID 42534632 (https://europepmc.org/article/MED/42534632; retrieved 2026-10-25T17:29:18+00:00)

> FTO variants showed mixed results, with rs9939609 (OR = 3.72, P = 0.009) and rs1421085 (OR = 3.22, P < 0.001) variants being associated with obesity and higher body mass index (BMI) in Indonesians, but no significant findings in Malaysians.

<a id="e19"></a>**E19** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-26T02:29:32+00:00)

> No ENCODE JUN ChIP-seq peak contains chr16:53767042:T>C in biosamples matching 'adipose'. Absence can also mean no JUN experiment in that biosample. In other biosamples, 1 JUN peaks do contain the variant: HepG2 (experiments ENCSR747VUU).

<a id="e20"></a>**E20** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-26T13:25:56+00:00)

> No ENCODE KLF6 ChIP-seq peak contains chr16:53767042:T>C in biosamples matching 'adipose'. Absence can also mean no KLF6 experiment in that biosample. In other biosamples, 1 KLF6 peaks do contain the variant: HepG2 (experiments ENCSR757EKM).

<a id="e21"></a>**E21** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=rs1421085%20FTO%20enhancer%20adipocyte%20perturbation%20target%20gene%20ARID5B%20IRX3%20IRX5&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T13:25:56+00:00)

> Europe PMC: 13 hits for 'rs1421085 FTO enhancer adipocyte perturbation target gene ARID5B IRX3 IRX5'; top 8 with PMIDs:
> PMID 42877975 (2026): Human Genetics of Adipose Dysfunction: Genomic Mechanisms and Therapeutic Opportunities in Cardiometabolic Disease.
> PMID 42299366 (2026): Hepatogenomics of MAFLD in Asian Population: Genetic Polymorphisms and Pathway-Based Insights.
> PMID 41273414 (2026): Bridging the variant-to-function gap in type 2 diabetes: advances and challenges.
> PMID 39965570 (2025): An evolving understanding of multiple causal variants underlying genetic association signals.
> PMID 34290091 (2021): Linking the &lt;i&gt;FTO&lt;/i&gt; obesity rs1421085 variant circuitry to cellular, metabolic, and organismal phenotypes in vivo.
> PMID 35377406 (2022): The importance of considering regulatory domains in genome-wide analyses - the nearest gene is often wrong!
> PMID 38317953 (2024): <i>N</i><sup><i>6</i></sup>-methyladenosine modification in ischemic stroke: Functions, regulation, and therapeutic potential.
> PMID 35409166 (2022): FTO m6A Demethylase in Obesity and Cancer: Implications and Underlying Molecular Mechanisms.

<a id="e21a"></a>**E21a** literature_search, Europe PMC abstract, PMID 34290091 (https://europepmc.org/article/MED/34290091; retrieved 2026-10-26T13:25:56+00:00)

> We engineered a deletion of the rs1421085 conserved cis-regulatory module (CRM) in mice and confirmed in vivo that the CRM modulates Irx3 and Irx5 gene expression and mitochondrial function in adipocytes.

<a id="e21b"></a>**E21b** literature_search, Europe PMC abstract, PMID 34290091 (https://europepmc.org/article/MED/34290091; retrieved 2026-10-26T13:25:56+00:00)

> The CRM affects molecular and cellular phenotypes in an adipose depot-dependent manner and affects organismal phenotypes that are relevant for obesity, including decreased high-fat diet-induced weight gain, decreased whole-body fat mass, and decreased skin fat thickness.
