# rs1421085 and Obesity (FTO)

Configuration `full`, named mode, seed 0. Models: generator claude-opus-5, critic claude-sonnet-5-5, summariser claude-haiku-5-5. Cost $0.67 over 8 model calls; 190 s.

Variant `chr16:53767042:T>C` (germline); expression context: GTEx:Adipose - Subcutaneous (proxy for preadipocytes).

## QBiC-SELEX screen

425 of 997 models pass the gate. Top groups: Nuclear receptor, 3 models (best ESRRG, z 62.01); Homeodomain, 9 models (best PKNOX2, z 54.71); Nuclear receptor, 29 models (best NR4A3, z 32.74); Forkhead, 10 models (best FOXL1, z -32.62); bZIP, 3 models (best NFE2L3, z 28.3).

## Ranked chains

### 1. H1: Ref T preserves an ARID5B repressor motif in the FTO intron-1 enhancer; alt C disrupts it, derepressing IRX3/IRX5 and shifting adipocytes from beige to white (p = 0.58)

TF ARID5B (stated coverage not_in_coverage; registry not_in_coverage), ref allele binds more; element dELS cCRE EH38E3181208 in FTO intron 1 (chr16:53766999-53767220), the rs1421085 conserved cis-regulatory module; gene IRX3; cell type Adipocyte progenitor / beige adipocyte, subcutaneous adipose.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | ARID5B is not in QBiC-SELEX coverage (E18), so no QBiC binding change can be cited for it; instead, published work states that the T-to-C change interrupts a conserved ARID5B repressor motif, i.e. the ref T allele supports binding and the alt C does not (E20a). The site is modestly conserved (GERP 2.55, E01), consistent with a functional motif. I do not cite any other TF's QBiC score as evidence for ARID5B. | weak | [E18](#e18), [E20a](#e20a), [E01](#e01) |
| element | The variant lies inside a distal enhancer-like cCRE (EH38E3181208); the quoted DNase/H3K27ac z-scores are maxima over biosamples and belong to the neighbouring EH38E3181207, so adipose-specific activity is not shown by ENCODE here. Independent evidence that this sequence is a functional cis-regulatory module comes from mouse deletion of the rs1421085 CRM (E20c). | weak | [E03](#e03), [E20c](#e20c) |
| gene | Deletion of the rs1421085 CRM in mice changes Irx3 and Irx5 expression and adipocyte mitochondrial function (E20c), and IRX3 overexpression raises Ucp1 (E20d, E20e), so IRX3/IRX5 ~520 kb away (E02) are the mechanistic targets even though L2G assigns FTO 0.99 and IRX3 no score (E05) and no adipose eQTL exists for any gene at this variant (E19: FTO in muscle, IRX3 in pancreas only, both alt-increasing). | weak | [E20c](#e20c), [E20d](#e20d), [E20e](#e20e), [E02](#e02), [E05](#e05), [E19](#e19) |
| cell_type | The effect is observed in human abdominal subcutaneous-derived beige adipocytes and adipocyte progenitors; bulk GTEx subcutaneous adipose is used only as an expression proxy, which is a limitation. | weak | [E20a](#e20a), [E20b](#e20b) |
| phenotype | Loss of ARID5B repression raises IRX3/IRX5 and lowers thermogenic gene expression (UCP1, PM20D1, CIDEA) and proton-leak respiration in CC carriers (E20b), reducing energy expenditure and producing the very strong BMI/obesity and downstream T2D/HbA1c associations (E04, E06b, E06c). Note a direction discrepancy: GWAS Catalog lists T as the effect allele (E04) whereas the functional literature identifies C as the obesity-risk allele (E20b); the catalog allele annotation at this locus should not be taken at face value. | weak | [E20b](#e20b), [E04](#e04), [E06b](#e06b), [E06c](#e06c) |

Predictions: EMSA/allele-specific ARID5B ChIP in preadipocytes shows stronger occupancy on T than on C; Isogenic C-to-T editing at this single base lowers IRX3/IRX5 and raises UCP1/mitochondrial respiration in adipocytes; ARID5B knockdown in TT cells phenocopies the CC state (higher IRX3/IRX5, lower UCP1); Allelic luciferase/MPRA: C shows higher enhancer activity than T in preadipocytes, and the difference is lost on ARID5B knockdown; FTO mRNA in subcutaneous adipose is not consistently genotype-dependent (consistent with E19 showing no adipose eQTL)

Falsified if: ARID5B binds both alleles equally, or ARID5B knockdown does not change IRX3/IRX5; Single-base C-to-T editing leaves IRX3/IRX5 and thermogenic genes unchanged; CRM deletion changes FTO but not IRX3/IRX5 in adipocytes

### 2. H5: Null: no TF-mediated effect of rs1421085 itself; the signal is carried by a linked variant in the strong intron-1/intron-2 LD block (p = 0.22)

Null chain: no TF-mediated effect of this variant.

Predictions: Fine-mapping PIP stays well below 1 (0.41-0.85 as observed) and conditioning on a neighbouring SNP (e.g. rs9939609) removes the rs1421085 signal; No allele-specific EMSA, ChIP or MPRA difference for T vs C in preadipocytes; No adipose molecular QTL for this variant (consistent with 0 molecular QTL credible sets and only muscle/pancreas eQTLs)

Falsified if: Isogenic single-base editing of rs1421085 alone changes IRX3/IRX5 or thermogenic gene expression; Allele-specific ChIP, EMSA or MPRA shows a reproducible T vs C difference

### 3. H2: Alt C creates a stronger TALE-homeodomain (TGIF1/TGIF2/MEIS) site that activates the intron-1 enhancer (p = 0.11)

TF TGIF1 (stated coverage mapped; registry own_model), alt allele binds more; element dELS cCRE EH38E3181208 in FTO intron 1; gene IRX3; cell type Subcutaneous adipose / preadipocyte.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | QBiC group G008 (TALE homeodomain) shows a large, fully consistent alt-allele gain across 9 models (best model PKNOX2 own model, z 54.71, effect +3.05; site 95.5th to 99.7th percentile). The group names a shared specificity, not one TF; I pick TGIF1 because it is the most expressed covered member in subcutaneous adipose (13.07 TPM), with TGIF2 (11.62), MEIS3 (9.23) and PKNOX1 (7.35) nearly as plausible. This is an in vitro prediction only. | weak | [E09](#e09) |
| element | The gained site falls in a distal enhancer-like cCRE that mouse CRM deletion shows is a functional regulatory module, though ENCODE gives no adipose-specific signal here. | weak | [E03](#e03), [E20c](#e20c) |
| gene | The CRM regulates IRX3/IRX5 (E20c); L2G instead favours FTO (0.99) and there is no adipose eQTL for either gene (E19), so the gene link rests on the mouse CRM result, not on this variant's own QTL. | weak | [E20c](#e20c), [E05](#e05), [E19](#e19) |
| cell_type | TGIF1/TGIF2/MEIS factors are expressed in bulk subcutaneous adipose at the listed TPMs; no preadipocyte footprint or occupancy data is cited. | weak | [E09](#e09) |
| phenotype | If a gained TALE activator site raises enhancer output and IRX3/IRX5, the C allele would lower thermogenesis and raise BMI, matching the reported lower thermogenic capacity of CC carriers (E20b) and the locus BMI/obesity signal (E04). | weak | [E20b](#e20b), [E04](#e04) |

Predictions: TGIF1/TGIF2 or MEIS ChIP in preadipocytes shows allele-biased occupancy favouring C; Knockdown of TGIF1/TGIF2 (not ARID5B) abolishes the allelic reporter difference; A TALE-family footprint is detectable at this site in adipose DNase data

Falsified if: No TALE-family occupancy or footprint at the site in adipose cells; TALE knockdown leaves allelic enhancer activity unchanged while ARID5B knockdown abolishes it

### 4. H3: Alt C strengthens an ERR half-site bound by ESRRA, altering oxidative-program enhancer output (p = 0.09)

TF ESRRA (stated coverage mapped; registry own_model), alt allele binds more; element dELS cCRE EH38E3181208 in FTO intron 1; gene IRX3; cell type Subcutaneous adipose / preadipocyte.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | QBiC group G037 gives the strongest signal in the screen (best model ESRRG own model, z 62.01, effect +2.15; all 3 models same sign; site 94.0th to 99.7th percentile). Within this shared ERR specificity only ESRRA is appreciably expressed in subcutaneous adipose (34.08 TPM vs ESRRG 0.06, ESRRB 0.16), so ESRRA is the named TF; it is covered through a mapped model (z 17.39), not its own best model. Prediction only, no occupancy data. | weak | [E08](#e08) |
| element | The created half-site lies in a distal enhancer-like cCRE shown by mouse deletion to be a functional CRM; ENCODE biosample-specific adipose signal is not available. | weak | [E03](#e03), [E20c](#e20c) |
| gene | The CRM modulates IRX3/IRX5 (E20c); ESRRA regulation of these genes is not demonstrated, and no adipose eQTL exists (E19). | weak | [E20c](#e20c), [E19](#e19), [E05](#e05) |
| cell_type | ESRRA is well expressed in bulk subcutaneous adipose (34.08 TPM); preadipocyte occupancy is not shown. | weak | [E08](#e08) |
| phenotype | If ERR binding on C alters enhancer output toward IRX3/IRX5 and away from thermogenesis, it would reproduce the lower thermogenic capacity of CC adipocytes and the BMI/HbA1c associations. | weak | [E20b](#e20b), [E04](#e04) |

Predictions: ESRRA ChIP-seq shows allele-biased occupancy at chr16:53767042 favouring C; ESRRA knockdown or inverse agonist removes the allelic reporter difference; Allelic effect is larger in differentiated, mitochondria-rich adipocytes than in progenitors

Falsified if: ESRRA shows no occupancy at this cCRE in any biosample; Reporter activity is unchanged by ESRRA perturbation but changed by ARID5B knockdown

## Prediction matrix

| Test | Cost | Separates top two | H1 | H5 | H2 | H3 |
| --- | --- | --- | --- | --- | --- | --- |
| Allelic EMSA with preadipocyte nuclear extract plus ARID5B supershift/competition (T vs C probe) | low | yes | T probe forms an ARID5B-containing complex absent or much weaker on C | No reproducible allelic difference in complex formation | Extra complex on C, not supershifted by ARID5B antibody | Extra complex on C, not supershifted by ARID5B antibody |
| Allelic luciferase/MPRA of the 200 bp cCRE in human preadipocytes | low | yes | C > T activity; difference lost on ARID5B knockdown | No allelic difference | C > T activity; difference lost on TGIF1/TGIF2 knockdown | C > T activity; difference lost on ESRRA knockdown |
| Isogenic single-base CRISPR conversion (CC to TT) in primary human adipocyte progenitors, then IRX3/IRX5, UCP1 and respiration | high | yes | TT lowers IRX3/IRX5, raises UCP1 and proton-leak respiration | No change in IRX3/IRX5, UCP1 or respiration | Same directional change, but TALE knockdown rather than ARID5B knockdown abolishes it | Same directional change, abolished by ESRRA perturbation |
| ARID5B ChIP-seq/ChIP-qPCR in heterozygous preadipocytes, allele-specific read counting | medium | yes | Peak at the cCRE with T-biased reads | No ARID5B peak or no allelic bias | No ARID5B peak or no allelic bias | No ARID5B peak or no allelic bias |
| ESRRA and TGIF1/MEIS ChIP at chr16:53767042 in adipose-lineage cells | medium | no | No requirement for these peaks; allelic effect persists after their knockdown | Peaks may exist but show no allelic bias | TALE peak with C-biased occupancy | ESRRA peak with C-biased occupancy |
| Adipose - Subcutaneous eQTL lookup for FTO/IRX3/RPGRIP1L (existing GTEx v8) | existing data | no | No bulk adipose eQTL expected (effect confined to progenitor/beige subpopulation) - matches E19 | No adipose eQTL - matches E19 | Same as H1; no discriminating expectation | Same as H1; no discriminating expectation |

## Next experiment

Allelic EMSA on the 25-30 bp T vs C oligo with human preadipocyte nuclear extract, including an ARID5B antibody supershift and cold-competitor controls: low cost, and it directly separates H1 (T-specific ARID5B complex) from the null H5 (no allelic difference), while a C-specific non-ARID5B complex would instead favour H2/H3.

## Investigate calls

- qbic_tf_detail({"tf": "ARID5B"})
- eqtl_lookup({"tissue": null})
- literature_search({"query": "rs1421085 ARID5B IRX3 IRX5 adipocyte browning"})

## Flags

- coverage_misstated: H2: stated mapped, registry says own_model for TGIF1
- coverage_misstated: H3: stated mapped, registry says own_model for ESRRA

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

> CONCLUSION: This meta-analysis provides strong evidence that FTO polymorphisms, particularly rs1421085 and rs9939609, are significantly associated with increased susceptibility to obesity in adults, while their impact on overweight is comparatively weaker.

<a id="e06d"></a>**E06d** literature_search, Europe PMC abstract, PMID 41591493 (https://europepmc.org/article/MED/41591493; retrieved 2026-10-25T17:29:18+00:00)

> Statistically significant assocation between the FTO rs1421085 genotype and neuroticism emerged by age 25, with an additive effect of each T-allele.

<a id="e06e"></a>**E06e** literature_search, Europe PMC abstract, PMID 42534632 (https://europepmc.org/article/MED/42534632; retrieved 2026-10-25T17:29:18+00:00)

> FTO variants showed mixed results, with rs9939609 (OR = 3.72, P = 0.009) and rs1421085 (OR = 3.22, P < 0.001) variants being associated with obesity and higher body mass index (BMI) in Indonesians, but no significant findings in Malaysians.

<a id="e07"></a>**E07** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> QBiC-SELEX screen of chr16:53767042:T>C: 997 models scored, 425 pass the gate (Bonferroni 0.05/997, p < 5.02e-05, |z| > 4.05), in 275 CIS-BP groups. Expression context: GTEx tissue median Adipose - Subcutaneous. Groups shown: 10; dropped because no TF in the group reaches 1 TPM: 53 (CUT; Homeodomain, 3 models z -47.91, C2H2 ZF, 1 model z -42.95, Homeodomain, 2 models z -30.65, C2H2 ZF, 2 models z 21.18, Homeodomain; POU, 1 model z -19.44). predicted_effect > 0 means the alternate allele binds more strongly. In vitro binding only: expression and chromatin decide whether a change matters.

<a id="e08"></a>**E08** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G037 (Nuclear receptor, 3 models): best model ESRRG_FL_TGAGCT40NGCA_KW_yin2017_0_3_7mer (own model of ESRRG), z 62.01, effect 2.149 (alt binds more); 3 passing models (3 with the best model's sign). Passing members: ESRRG z 62.01, ESRRB z 25.92, ESRRA z 17.39. TFs this group covers (own and CIS-BP-mapped models): ESRRA 34.08 TPM, ESR1 2.07 TPM, ESR2 0.83 TPM, ESRRB 0.16 TPM, ESRRG 0.06 TPM; best model's site strength: ref 94.0th, alt 99.7th percentile of its k-mer coefficients.

<a id="e09"></a>**E09** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G008 (Homeodomain, 9 models): best model PKNOX2_eDBD_TAACGT40NGAT_KAN_yin2017_0_4_7mer (own model of PKNOX2), z 54.71, effect 3.047 (alt binds more); 9 passing models (9 with the best model's sign). Passing members: PKNOX2 z 54.71, TGIF2 z 42.72, MEIS3 z 40.95, TGIF2LX z 36.97, MEIS2 z 35.14 (+4 more). TFs this group covers (own and CIS-BP-mapped models): TGIF1 13.07 TPM, TGIF2 11.62 TPM, MEIS3 9.23 TPM, PKNOX1 7.35 TPM, MEIS2 5.53 TPM, MEIS1 4.65 TPM, PKNOX2 2.8 TPM, TGIF2LX 0.0 TPM, TGIF2LY 0.0 TPM; best model's site strength: ref 95.5th, alt 99.7th percentile of its k-mer coefficients.

<a id="e10"></a>**E10** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G002 (Nuclear receptor, 29 models): best model NR4A3_DBD_TTCGTA20NTA_KH_nitta2015_1_3_7mer (own model of NR4A3), z 32.74, effect 2.426 (alt binds more); 19 passing models (18 with the best model's sign); members disagree on direction. Passing members: NR4A3 z 32.74, NR2C1 z 21.97, NR5A1 z 21.36, NR4A1 z 16.25, NR4A2 z 15.74 (+14 more). TFs this group covers (own and CIS-BP-mapped models): NR4A1 139.74 TPM, NR1D1 118.5 TPM, PPARG 111.14 TPM, NR2F2 101.24 TPM, NR1H2 73.96 TPM, RXRB 63.05 TPM, NR1H3 53.67 TPM, THRA 41.46 TPM, RXRA 39.73 TPM, RARA 37.57 TPM (+28 more); best model's site strength: ref 99.6th, alt 100.0th percentile of its k-mer coefficients.

<a id="e11"></a>**E11** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G007 (Forkhead, 10 models): best model FOXL1_NA_TGCTCG20NCTC_ESW_yang2017_0_2_7mer (own model of FOXL1), z -32.62, effect -1.076 (alt binds less); 7 passing models (6 with the best model's sign); members disagree on direction. Passing members: FOXL1 z -32.62, FOXC2 z -16.49, FOXG1 z -15.83, FOXC1 z -15.51, FOXF1 z 7.79 (+2 more). TFs this group covers (own and CIS-BP-mapped models): FOXJ3 33.71 TPM, FOXJ2 24.29 TPM, FOXC1 22.42 TPM, FOXP4 20.41 TPM, FOXP1 14.95 TPM, FOXK2 13.86 TPM, FOXK1 10.32 TPM, FOXS1 4.39 TPM, FOXF2 3.25 TPM, FOXC2 3.09 TPM (+18 more); best model's site strength: ref 99.9th, alt 98.9th percentile of its k-mer coefficients.

<a id="e12"></a>**E12** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G043 (bZIP, 3 models): best model NFE2L3_FL_TACGAG20NAGC_KH_nitta2015_1_3_7mer (own model of NFE2L3), z 28.3, effect 1.411 (alt binds more); 2 passing models (2 with the best model's sign). Passing members: NFE2L3 z 28.3, NFE2L1 z 8.62. TFs this group covers (own and CIS-BP-mapped models): NFE2L1 185.6 TPM, NFE2L2 65.58 TPM, NFE2L3 8.21 TPM, NFE2 0.6 TPM; best model's site strength: ref 96.9th, alt 99.7th percentile of its k-mer coefficients.

<a id="e13"></a>**E13** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G033 (bZIP, 3 models): best model ATF2_eDBD_TGAACC40NCCA_KP_yin2017_0_3_7mer (own model of ATF2), z 28.08, effect 1.047 (alt binds more); 3 passing models (3 with the best model's sign). Passing members: ATF2 z 28.08, CREB5 z 27.01, ATF7 z 10.29. TFs this group covers (own and CIS-BP-mapped models): ATF7 38.23 TPM, ATF2 26.88 TPM, CREB5 6.45 TPM, ATF7-NPFF; best model's site strength: ref 98.6th, alt 99.9th percentile of its k-mer coefficients.

<a id="e14"></a>**E14** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G022 (Forkhead, 4 models): best model FOXB1_NA_TGAGCA30NCGA_ESAI_yang2017_0_4_7mer (own model of FOXB1), z -23.72, effect -1.232 (alt binds less); 4 passing models (4 with the best model's sign). Passing members: FOXB1 z -23.72, FOXA1 z -13.3, FOXA3 z -8.79, FOXA2 z -7.96. TFs this group covers (own and CIS-BP-mapped models): FOXS1 4.39 TPM, FOXA3 0.06 TPM, FOXA1 0.05 TPM, FOXA2 0.0 TPM, FOXB1 0.0 TPM, FOXB2 0.0 TPM; best model's site strength: ref 99.8th, alt 99.0th percentile of its k-mer coefficients.

<a id="e15"></a>**E15** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G048 (Homeodomain, 3 models): best model SIX1_eDBD_TTAACC40NCTA_KQ_yin2017_0_4_7mer (own model of SIX1), z -22.75, effect -0.856 (alt binds less); 3 passing models (3 with the best model's sign). Passing members: SIX1 z -22.75, SIX2 z -19.68, SIX4 z -8.7. TFs this group covers (own and CIS-BP-mapped models): SIX5 16.4 TPM, SIX1 8.49 TPM, SIX2 5.54 TPM, SIX4 0.69 TPM; best model's site strength: ref 99.8th, alt 99.0th percentile of its k-mer coefficients.

<a id="e16"></a>**E16** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G009 (Paired box, 8 models): best model PAX7_FL_TCGTTT40NGTC_KAF_yin2017_0_4_7mer (own model of PAX7), z 22.55, effect 1.934 (alt binds more); 8 passing models (8 with the best model's sign). Passing members: PAX7 z 22.55, PAX3 z 16.01, PAX9 z 15.43, PAX8 z 15.39, PAX2 z 12.88 (+3 more). TFs this group covers (own and CIS-BP-mapped models): PAX8 2.24 TPM, PAX3 0.4 TPM, PAX9 0.14 TPM, PAX5 0.04 TPM, PAX1 0.03 TPM, PAX2 0.01 TPM, PAX6 0.01 TPM, PAX4 0.0 TPM, PAX7 0.0 TPM; best model's site strength: ref 90.7th, alt 99.7th percentile of its k-mer coefficients.

<a id="e17"></a>**E17** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G162 (Unknown, 1 model): best model DACH1_FL_TG40NTGTGTT_YWO_jolma2025_0_3_7mer (own model of DACH1), z 21.79, effect 0.795 (alt binds more); 1 passing models (1 with the best model's sign). Passing members: DACH1 z 21.79. TFs this group covers (own and CIS-BP-mapped models): DACH1 6.37 TPM; best model's site strength: ref 86.1th, alt 99.9th percentile of its k-mer coefficients.

<a id="e18"></a>**E18** qbic_tf_detail, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> {"tf":"ARID5B","symbol":"ARID5B","via":"hgnc_symbol","notes":[],"coverage":"not_in_coverage"}

<a id="e19"></a>**E19** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr16_53767042_T_C_b38&datasetId=gtex_v8; retrieved 2026-10-25T17:30:38+00:00)

> 2 significant GTEx v8 single-tissue eQTLs for chr16_53767042_T_C_b38. NES is the effect of the alt allele (C) relative to ref (T).
> FTO in Muscle_Skeletal: NES +0.14, p 7.5e-08
> IRX3 in Pancreas: NES +0.37, p 8.3e-06

<a id="e20"></a>**E20** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=rs1421085%20ARID5B%20IRX3%20IRX5%20adipocyte%20browning&format=json&pageSize=8&resultType=core; retrieved 2026-10-25T17:39:45+00:00)

> Europe PMC: 34 hits for 'rs1421085 ARID5B IRX3 IRX5 adipocyte browning'; top 8 with PMIDs:
> PMID 36882962 (2023): Technologies, strategies, and cautions when deconvoluting genome-wide association signals: FTO in focus.
> PMID 37416800 (2023): Human abdominal subcutaneous-derived active beige adipocytes carrying <i>FTO</i> rs1421085 obesity-risk alleles exert lower thermogenic capacity.
> PMID 37200795 (2023): <i>FTO</i> Gene Polymorphisms at the Crossroads of Metabolic Pathways of Obesity and Epigenetic Influences.
> PMID 38674326 (2024): Interaction Effects of <i>FTO</i> and <i>MC4R</i> Polymorphisms on Total Body Weight Loss, Post-Surgery Weight, and Post-Body Mass Index after Bariatric Surgery.
> PMID 34290091 (2021): Linking the &lt;i&gt;FTO&lt;/i&gt; obesity rs1421085 variant circuitry to cellular, metabolic, and organismal phenotypes in vivo.
> PMID 37554175 (2023): Studies on the fat mass and obesity-associated (FTO) gene and its impact on obesity-associated diseases.
> PMID 37465124 (2023): Molecular and cellular regulation of thermogenic fat.
> PMID 33776928 (2021): <i>IRX3</i> Overexpression Enhances <i>Ucp1</i> Expression <i>In Vivo</i>.

<a id="e20a"></a>**E20a** literature_search, Europe PMC abstract, PMID 37416800 (https://europepmc.org/article/MED/37416800; retrieved 2026-10-25T17:39:45+00:00)

> The rs1421085 T-to-C single-nucleotide polymorphism (SNP) of the human FTO gene interrupts a conserved motif for ARID5B repressor, resulting in adipocyte type shift from beige to white.

<a id="e20b"></a>**E20b** literature_search, Europe PMC abstract, PMID 37416800 (https://europepmc.org/article/MED/37416800; retrieved 2026-10-25T17:39:45+00:00)

> Active beige adipocytes carrying FTO CC had lower thermogenic gene (e.g., UCP1, PM20D1, CIDEA) expression and thermogenesis measured by proton leak respiration as compared to TT carriers.

<a id="e20c"></a>**E20c** literature_search, Europe PMC abstract, PMID 34290091 (https://europepmc.org/article/MED/34290091; retrieved 2026-10-25T17:39:45+00:00)

> We engineered a deletion of the rs1421085 conserved cis-regulatory module (CRM) in mice and confirmed in vivo that the CRM modulates Irx3 and Irx5 gene expression and mitochondrial function in adipocytes.

<a id="e20d"></a>**E20d** literature_search, Europe PMC abstract, PMID 33776928 (https://europepmc.org/article/MED/33776928; retrieved 2026-10-25T17:39:45+00:00)

> The Iroquois homeobox 3 (IRX3) gene was recently reported to be a functional downstream target of a common polymorphism in the FTO gene, which encodes an obesity-associated protein; however, the role of IRX3 in energy expenditure remains unclear.

<a id="e20e"></a>**E20e** literature_search, Europe PMC abstract, PMID 33776928 (https://europepmc.org/article/MED/33776928; retrieved 2026-10-25T17:39:45+00:00)

> After acute cold exposure or CL316,243 stimulation, brown/beige tissue hIRX3-overexpressing mice showed an increase in Ucp1 expression.
