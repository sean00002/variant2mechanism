# rs1421085 and Obesity (FTO)

Configuration `no_qbic`, named mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.05 over 10 model calls; 219 s.

Variant `chr16:53767042:T>C` (germline); expression context: GTEx:Adipose - Subcutaneous (proxy for preadipocytes).

## Ranked chains

### 1. ARID5B_loss_IRX3_IRX5: ARID5B loss at the dELS derepresses IRX3/IRX5 in preadipocytes (p = 0.55)

TF ARID5B (stated coverage not_checked; registry not_in_coverage), ref allele binds more; element dELS EH38E3181208; gene IRX3/IRX5; cell type Adipose - subcutaneous / preadipocytes.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | ARID5B binds the ref T allele more strongly than the alt C allele. E07d reports that the T-to-C change disrupts a conserved ARID5B repressor motif, and E07e places ARID5B in the rs1421085-IRX3/IRX5 pathway. Direct allele-specific ARID5B ChIP or MPRA is not in the supplied evidence. | weak | [E07d](#e07d), [E07e](#e07e) |
| element | rs1421085 lies in the distal enhancer-like cCRE EH38E3181208 (dELS). | supported | [E03](#e03) |
| gene | The dELS is a candidate regulator of IRX3/IRX5 in adipocytes: E07d reports derepression doubles IRX3 and IRX5 during early adipocyte differentiation; E07a shows deletion of the conserved CRM modulates Irx3/Irx5 in mice; E02 places IRX3 520.4 kb away and does not list IRX5. E08 found no significant bulk subcutaneous adipose eQTL, so a bulk eQTL is not required and the link remains context-dependent. | supported | [E07d](#e07d), [E07a](#e07a), [E02](#e02), [E08](#e08) |
| cell_type | The relevant context is subcutaneous adipose/pre-adipocytes. E07d, E07a, and E07c support adipocyte/pre-adipocyte differentiation and IRX3 browning biology, although GTEx subcutaneous adipose is only a proxy. | weak | [E07d](#e07d), [E07a](#e07a), [E07c](#e07c) |
| phenotype | Alt C reduces ARID5B repression, increases IRX3/IRX5, impairs thermogenesis, and increases obesity risk. E07d/E07e support a pro-obesity direction; E06d supports C-allele association with overweight/obesity; E06b/E06c support rs1421085-obesity association but do not harmonize allele direction; E04 reports effect allele T and is discordant, so it is not used alone to assign direction. | weak | [E07d](#e07d), [E07e](#e07e), [E06b](#e06b), [E06c](#e06c), [E06d](#e06d), [E04](#e04) |

Predictions: Allele-specific ARID5B binding is higher on ref T than on alt C at rs1421085.; Alt C increases IRX3 and IRX5 expression during preadipocyte differentiation.; The dELS contacts IRX3/IRX5 promoters in adipocyte chromatin.; ARID5B knockdown or knockout mimics the alt C allele.

Falsified if: No allele-specific ARID5B binding at rs1421085 is found after controlling for linked variants.; Alt C does not increase IRX3 or IRX5 expression in preadipocytes.; No chromatin contact connects the dELS to IRX3/IRX5 in adipocytes.; The C allele is not trait-increasing after careful harmonization of E04/E06.

### 2. null: No TF-mediated allelic effect; association reflects linked or locus-level effect (p = 0.25)

Null chain: no TF-mediated effect of this variant.

Predictions: No allelic TF-binding difference at rs1421085.; The GWAS signal is explained by a linked causal variant, FTO-locus haplotype, or passenger association rather than this base.; Editing rs1421085 alone would not change enhancer activity or target-gene expression.; E08 found no significant subcutaneous adipose eQTL for this variant, consistent with no simple bulk eQTL effect.

Falsified if: Allele-specific TF binding at rs1421085 changes enhancer activity after controlling for linked variants.; CRISPR editing of rs1421085 alone changes a target gene in adipocytes.; Conditional analysis shows the obesity signal is not explained by a linked variant or FTO-locus haplotype effect.

### 3. CTCF_insulator_FTO: CTCF insulator/loop alteration at the FTO locus (p = 0.10)

TF CTCF (stated coverage not_checked; registry own_model), ref allele binds more; element dELS EH38E3181208 or nearby CTCF cCRE EH38E3181207; gene FTO; cell type Adipose - subcutaneous / preadipocytes.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | CTCF binding at rs1421085 itself is not shown. E03 reports only that the nearby cCRE EH38E3181207 has CTCF z 1.5, not at the variant and not allele-specifically. | missing | [E03](#e03) |
| element | rs1421085 lies in dELS EH38E3181208, and nearby EH38E3181207 has CTCF z 1.5. | supported | [E03](#e03) |
| gene | L2G assigns the locus to FTO with score 0.99, and FTO is 65.3 kb away. This is statistical assignment, not evidence that this dELS regulates FTO via CTCF or insulator/loop changes. | weak | [E05](#e05), [E02](#e02) |
| cell_type | No adipose/pre-adipocyte CTCF, chromatin-loop, or enhancer-activity evidence is supplied. | missing | none |
| phenotype | rs1421085 is associated with obesity/BMI, but there is no evidence that an altered CTCF insulator or loop mediates the association. | weak | [E04](#e04), [E06b](#e06b), [E06c](#e06c) |

Predictions: Allele-specific CTCF ChIP at the variant region.; Chromatin-loop changes between the dELS and FTO or other target promoters.; CTCF depletion alters target-gene expression in adipocytes.

Falsified if: No CTCF ChIP signal is found at rs1421085.; CTCF binding is not allele-specific.; No chromatin loop connects the variant region to FTO or another obesity-relevant gene.; CTCF perturbation does not affect the target gene in adipocytes.

### 4. CEBPB_alt_gain_FTO: Alt-allele gain of an adipocyte CEBPB enhancer site (p = 0.10)

TF CEBPB (stated coverage not_checked; registry own_model), alt allele binds more; element dELS EH38E3181208; gene FTO; cell type Adipose - subcutaneous / preadipocytes.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | CEBPB binding at rs1421085 is not shown in the supplied evidence; no CEBPB ChIP, allele-specific binding, MPRA, reporter, or perturbation data are available. | missing | none |
| element | rs1421085 lies in the distal enhancer-like cCRE EH38E3181208 (dELS). | supported | [E03](#e03) |
| gene | L2G assigns the locus to FTO with score 0.99, but there is no evidence that this dELS regulates FTO or that CEBPB mediates the effect. | weak | [E05](#e05) |
| cell_type | No adipocyte/pre-adipocyte CEBPB occupancy or activity evidence is supplied. | missing | none |
| phenotype | rs1421085 is associated with obesity/BMI, but there is no evidence for an adipocyte CEBPB enhancer mechanism or for the direction of CEBPB binding/activity. | weak | [E04](#e04), [E06b](#e06b), [E06c](#e06c) |

Predictions: Alt C increases CEBPB ChIP at the dELS.; Alt C increases enhancer activity in adipocytes.; CEBPB knockdown reduces the alt-allele enhancer effect.

Falsified if: No allele-specific CEBPB binding is found at the dELS.; CEBPB perturbation does not change the target gene.; The alt allele does not increase enhancer activity in adipocytes.

## Prediction matrix

| Test | Cost | Separates top two | ARID5B_loss_IRX3_IRX5 | null | CTCF_insulator_FTO | CEBPB_alt_gain_FTO |
| --- | --- | --- | --- | --- | --- | --- |
| Allele-specific ARID5B binding at rs1421085 (EMSA/MPRA or ARID5B ChIP-qPCR with ref vs alt) in preadipocyte nuclear context | medium | yes | Ref T binds ARID5B more strongly than alt C. | No allelic difference in ARID5B binding. | No ARID5B allelic difference; CTCF is not the tested TF. | No ARID5B allelic difference. |
| CRISPR/Cas9 edit of rs1421085 T>C alone in subcutaneous preadipocytes, then measure IRX3/IRX5 during differentiation | high | yes | C allele increases IRX3 and IRX5. | No change in IRX3/IRX5 attributable to the single edit. | No IRX3/IRX5 change; possible FTO/loop change if the CTCF model is correct. | No IRX3/IRX5 change; possible FTO/enhancer change if the CEBPB model is correct. |
| Allele-specific expression/eQTL for IRX3/IRX5 in preadipocytes or fractionated adipose | medium | yes | C allele associates with higher IRX3/IRX5 in preadipocyte context. | No ASE/eQTL; E08 already found no significant bulk subcutaneous adipose eQTL. | No IRX3/IRX5 ASE; FTO/loop not necessarily tested. | No IRX3/IRX5 ASE; FTO/enhancer not necessarily tested. |

## Next experiment

The single cheapest experiment that separates the top two chains is an allele-specific ARID5B binding assay using ref and alt rs1421085 oligos (EMSA or MPRA) with preadipocyte nuclear extract or recombinant ARID5B. The ARID5B chain predicts stronger binding to ref T than alt C; the null predicts no allelic difference. Cost: medium.

## Investigate calls

- literature_search({"query": "rs1421085 ARID5B allele-specific binding preadipocyte enhancer IRX3 IRX5"})
- eqtl_lookup({"tissue": "Adipose - Subcutaneous"})
- tf_expression({"context": "Adipose - Subcutaneous", "tf": "ARID5B"})

## Flags

- tool_failed: E09 tf_expression: local DepMap/GTEx lookup failed: Unknown expression context 'Adipose - Subcutaneous'. Use DepMap:<ModelID>, DepMap:subtype=<Oncotree subtype>, GTEx:<tissue> or 

Citation support: 0.80 of links cite only evidence that passed every check.

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

<a id="e04"></a>**E04** gwas_lookup, GWAS Catalog REST v2 (https://www.ebi.ac.uk/gwas/rest/api/v2/associations?rs_id=rs1421085&size=100; retrieved 2026-10-25T17:29:17+00:00)

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

<a id="e05"></a>**E05** finemap_lookup, Open Targets Platform (credible sets, L2G) (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-25T17:29:10+00:00)

> 1701 credible sets contain 16_53767042_T_C: 200 GWAS, 0 molecular QTL.
> GWAS Body mass index (BMI, minimum, inv-normal transformed): PIP 0.85; L2G FTO 0.99, RPGRIP1L 0.20, CHD9 0.06
> GWAS Body mass index: PIP 0.80; L2G FTO 0.99, RPGRIP1L 0.25
> GWAS Impedance of leg left (UKB data field 23108): PIP 0.67; L2G FTO 0.99, RPGRIP1L 0.20
> GWAS Diabetes mellitus (PheCode 250): PIP 0.46; L2G FTO 0.99, RPGRIP1L 0.20, CHD9 0.06
> GWAS Impedance of leg left (UKB data field 23108): PIP 0.46; L2G FTO 0.99, RPGRIP1L 0.20
> GWAS Leg fat free mass left (UKB data field 23117): PIP 0.41; L2G FTO 0.99, RPGRIP1L 0.21, CHD9 0.07
> Best L2G gene scores across these sets: FTO 0.99, RPGRIP1L 0.36, CHD9 0.16

<a id="e06"></a>**E06** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=rs1421085%20AND%20FTO%20AND%20%22obesity%22&format=json&pageSize=8&resultType=core; retrieved 2026-10-25T17:29:18+00:00)

> Europe PMC: 653 hits for 'rs1421085 AND FTO AND "obesity"'; top 8 with PMIDs:
> PMID 42440472 (2026): A Rapid Genotyping Assay for &lt;i&gt;FTO&lt;/i&gt; and &lt;i&gt;PPAR-γ&lt;/i&gt; Nutrigenetic Variants in Thai Adults with Overweight/Obesity.
> PMID 41862896 (2026): Impact of fat mass and obesity-associated (FTO) gene variants on adult obesity and overweight: a comprehensive meta-analysis.
> PMID 41591493 (2026): Obesity-related RNA m&lt;sup&gt;6&lt;/sup&gt;A demethylase gene FTO rs1421085 is associated with neuroticism in a longitudinal birth cohort study.
> PMID 42197023 (2026): Associations Between FTO rs9939609 Genotype, Physical Activity, and Dietary Behaviors in Young Adults.
> PMID 42757464 (2026): Demethylase FTO attenuates atherosclerotic plaque via upregulating ABCA1 and ABCG1 expression by targeting ATG5.
> PMID 42299366 (2026): Hepatogenomics of MAFLD in Asian Population: Genetic Polymorphisms and Pathway-Based Insights.
> PMID 42534632 (2025): Genetic Polymorphisms Associated with Obesity in Southeast Asian Populations: A Systematic Review without Meta-Analysis.
> PMID 42245481 (2026): FTO in cardiovascular diseases: mechanisms, context dependence, and translational opportunities.

<a id="e06a"></a>**E06a** literature_search, Europe PMC abstract, PMID 42440472 (https://europepmc.org/article/MED/42440472; retrieved 2026-10-25T17:29:18+00:00)

> The aim of this study is to develop, validate, and apply a cost-effective 4-plex high-resolution melting (HRM) assay for simultaneous detection of FTO (rs9939609 and rs1421085) and PPAR-γ (rs1801282 and rs3856806) variants using standard laboratory equipment.

<a id="e06b"></a>**E06b** literature_search, Europe PMC abstract, PMID 41862896 (https://europepmc.org/article/MED/41862896; retrieved 2026-10-25T17:29:18+00:00)

> In the obesity group, the rs1421085 exhibited the strongest effect, with an odds ratio (OR) of 2.16 (95% CI: 1.58–2.95).

<a id="e06c"></a>**E06c** literature_search, Europe PMC abstract, PMID 41862896 (https://europepmc.org/article/MED/41862896; retrieved 2026-10-25T17:29:18+00:00)

> This meta-analysis provides strong evidence that FTO polymorphisms, particularly rs1421085 and rs9939609, are significantly associated with increased susceptibility to obesity in adults, while their impact on overweight is comparatively weaker.

<a id="e06d"></a>**E06d** literature_search, Europe PMC abstract, PMID 41591493 (https://europepmc.org/article/MED/41591493; retrieved 2026-10-25T17:29:18+00:00)

> Based on findings that experimental manipulation of the RNA m6A methylation in animal experiments can affect anxiety, and given that the C-allele of FTO rs1421085 had a significant association with indicators of overweight and obesity in our previous study, we have examined the possible association of FTO rs1421085 genotype with neuroticism in the same longitudinally observed sample.

<a id="e06e"></a>**E06e** literature_search, Europe PMC abstract, PMID 41591493 (https://europepmc.org/article/MED/41591493; retrieved 2026-10-25T17:29:18+00:00)

> Conclusively, an overweight and obesity-related variant of FTO, the gene encoding an RNA m6A demethylase, was associated with lower neuroticism, this association being subject to gender and cohort effects.

<a id="e06f"></a>**E06f** literature_search, Europe PMC abstract, PMID 42534632 (https://europepmc.org/article/MED/42534632; retrieved 2026-10-25T17:29:18+00:00)

> LEP variants were not significantly associated with obesity in Malaysians, and FTO variants showed mixed results, with rs9939609 (OR = 3.72, P = 0.009) and rs1421085 (OR = 3.22, P < 0.001) variants being associated with obesity and higher body mass index (BMI) in Indonesians, but no significant findings in Malaysians.

<a id="e07"></a>**E07** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=rs1421085%20ARID5B%20allele-specific%20binding%20preadipocyte%20enhancer%20IRX3%20IRX5&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T01:39:13+00:00)

> Europe PMC: 16 hits for 'rs1421085 ARID5B allele-specific binding preadipocyte enhancer IRX3 IRX5'; top 8 with PMIDs:
> PMID 42877975 (2026): Human Genetics of Adipose Dysfunction: Genomic Mechanisms and Therapeutic Opportunities in Cardiometabolic Disease.
> PMID 36882962 (2023): Technologies, strategies, and cautions when deconvoluting genome-wide association signals: FTO in focus.
> PMID 34290091 (2021): Linking the &lt;i&gt;FTO&lt;/i&gt; obesity rs1421085 variant circuitry to cellular, metabolic, and organismal phenotypes in vivo.
> PMID 37465124 (2023): Molecular and cellular regulation of thermogenic fat.
> PMID 33919522 (2021): Genetic Variants in Transcription Factor Binding Sites in Humans: Triggered by Natural Selection and Triggers of Diseases.
> PMID 33776928 (2021): <i>IRX3</i> Overexpression Enhances <i>Ucp1</i> Expression <i>In Vivo</i>.
> PMID 26287746 (2015): FTO Obesity Variant Circuitry and Adipocyte Browning in Humans.
> PMID 26557137 (2015): Commentary: FTO obesity variant circuitry and adipocyte browning in humans. [no abstract]

<a id="e07a"></a>**E07a** literature_search, Europe PMC abstract, PMID 34290091 (https://europepmc.org/article/MED/34290091; retrieved 2026-10-26T01:39:13+00:00)

> We engineered a deletion of the rs1421085 conserved cis-regulatory module (CRM) in mice and confirmed in vivo that the CRM modulates Irx3 and Irx5 gene expression and mitochondrial function in adipocytes.

<a id="e07b"></a>**E07b** literature_search, Europe PMC abstract, PMID 34290091 (https://europepmc.org/article/MED/34290091; retrieved 2026-10-26T01:39:13+00:00)

> Together, our data establish cross-species conservation of the rs1421085 regulatory circuitry at the molecular, cellular, metabolic, and organismal level, revealing previously unknown contextual dependence of the variant's action.

<a id="e07c"></a>**E07c** literature_search, Europe PMC abstract, PMID 33776928 (https://europepmc.org/article/MED/33776928; retrieved 2026-10-26T01:39:13+00:00)

> Meanwhile, we and others recently demonstrated that IRX3 knockdown impaired the browning program of primary preadipocytes in vitro.

<a id="e07d"></a>**E07d** literature_search, Europe PMC abstract, PMID 26287746 (https://europepmc.org/article/MED/26287746; retrieved 2026-10-26T01:39:13+00:00)

> The rs1421085 T-to-C single-nucleotide variant disrupts a conserved motif for the ARID5B repressor, which leads to derepression of a potent preadipocyte enhancer and a doubling of IRX3 and IRX5 expression during early adipocyte differentiation.

<a id="e07e"></a>**E07e** literature_search, Europe PMC abstract, PMID 26287746 (https://europepmc.org/article/MED/26287746; retrieved 2026-10-26T01:39:13+00:00)

> Our results point to a pathway for adipocyte thermogenesis regulation involving ARID5B, rs1421085, IRX3, and IRX5, which, when manipulated, had pronounced pro-obesity and anti-obesity effects.

<a id="e08"></a>**E08** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr16_53767042_T_C_b38&datasetId=gtex_v8; retrieved 2026-10-25T17:30:38+00:00)

> 0 significant GTEx v8 single-tissue eQTLs for chr16_53767042_T_C_b38 in tissues matching 'Adipose - Subcutaneous'. NES is the effect of the alt allele (C) relative to ref (T).

<a id="e09"></a>**E09** tf_expression (failed), local DepMap/GTEx (; retrieved local)

> local DepMap/GTEx lookup failed: Unknown expression context 'Adipose - Subcutaneous'. Use DepMap:<ModelID>, DepMap:subtype=<Oncotree subtype>, GTEx:<tissue> or none.
