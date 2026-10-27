# rs1421085 and Obesity (FTO)

Configuration `full`, named mode, seed 0. Models: generator claude-opus-5, critic claude-sonnet-5-5, summariser claude-haiku-5-5. Cost $0.65 over 7 model calls; 165 s.

Variant `chr16:53767042:T>C` (germline); expression context: GTEx:Adipose - Subcutaneous (proxy for preadipocytes).

## QBiC-SELEX screen

425 of 997 models pass the gate. Top groups: Nuclear receptor, 3 models (best ESRRG, z 62.01); Homeodomain, 9 models (best PKNOX2, z 54.71); Nuclear receptor, 29 models (best NR4A3, z 32.74); Forkhead, 10 models (best FOXL1, z -32.62); bZIP, 3 models (best NFE2L3, z 28.3).

## Ranked chains

### 1. H5: Null: rs1421085 has no TF-mediated effect of its own; it tags the causal variant within the large FTO intron-1 haplotype (p = 0.34)

Null chain: no TF-mediated effect of this variant.

Predictions: MPRA/allelic reporter shows no significant T vs C activity difference; Denser fine-mapping moves the credible-set peak to a neighbouring variant (PIP here only 0.41-0.85); No molecular QTL is assigned to this variant in any tissue (0 of 1701 credible sets; 0 adipose eQTLs); No TF shows reproducible allele-specific binding at this base

Falsified if: Single-base editing in an isogenic background changes IRX3/IRX5 or FTO expression; A named TF shows reproducible allele-specific binding at this exact position

### 2. H1: The ref T allele preserves an ARID5B repressor site that the alt C disrupts; de-repression of the FTO intron-1 enhancer raises IRX3/IRX5 in adipocyte progenitors and shifts them from beige to white fat (p = 0.30)

TF ARID5B (stated coverage not_in_coverage; registry not_in_coverage), ref allele binds more; element dELS enhancer EH38E3181208 (chr16:53766999-53767220) in FTO intron 1; gene IRX3; cell type Adipocyte progenitors / preadipocytes (subcutaneous adipose).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | ARID5B is predicted to bind the conserved ref T allele more strongly and to lose binding on alt C. A qbic_tf_detail lookup shows ARID5B is not_in_coverage in QBiC-SELEX, so no QBiC z-score or direction can be cited for it, and no other group's binding change is used as a proxy for ARID5B. The only supporting evidence here is modest conservation at the site (GERP 2.55); the direction rests on prior literature on this locus, not on evidence in this dossier. | missing | [E18](#e18), [E01](#e01) |
| element | The variant lies inside a distal enhancer-like cCRE (EH38E3181208). The DNase/H3K27ac z-scores quoted in SCREEN belong to the neighbouring cCRE EH38E3181207 and are maxima across biosamples, so adipose-progenitor activity of the variant's own element is not demonstrated here. | weak | [E03](#e03) |
| gene | The proposed target is IRX3 (520 kb away), acting by long-range contact rather than on FTO itself. This dossier gives no support for IRX3: L2G scores FTO 0.99 and gives IRX3 nothing, and there are no molecular QTLs; the absence of any adipose eQTL for FTO at this variant is at least consistent with the effect not being a simple local FTO eQTL. | missing | [E05](#e05), [E02](#e02), [E19](#e19) |
| cell_type | The expression context scored is bulk GTEx subcutaneous adipose used as a preadipocyte proxy; nothing here shows progenitor-specific activity, and ARID5B expression was not retrieved. | missing | [E07](#e07) |
| phenotype | The variant has an extremely strong, T-risk-allele obesity/BMI association with secondary T2D and HbA1c signals; a progenitor beige-to-white shift is one mechanism compatible with that, but is not evidenced here. | weak | [E04](#e04), [E06b](#e06b), [E06c](#e06c), [E06e](#e06e) |

Predictions: ARID5B EMSA/ChIP in preadipocytes shows stronger binding to T than to C at this exact base; Base editing C>T in risk-allele preadipocytes lowers IRX3/IRX5 and raises UCP1/thermogenic genes; Promoter-capture Hi-C or CRISPRi in preadipocytes links this element to IRX3/IRX5, not FTO; FTO mRNA in adipose is unchanged by genotype (consistent with E19)

Falsified if: ARID5B shows no allelic binding difference at this site; Perturbation of the element changes FTO but not IRX3/IRX5; The element is inactive in adipose-progenitor chromatin

### 3. H2: Alt C allele creates an ESRR half-site bound by ESRRA, activating the intron-1 enhancer (p = 0.15)

TF ESRRA (stated coverage own_model; registry own_model), alt allele binds more; element dELS enhancer EH38E3181208 in FTO intron 1; gene FTO; cell type Subcutaneous adipose / preadipocytes.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | QBiC group G037 predicts a large alt gain (best model ESRRG, z 62.01, effect +2.149; site 94.0th to 99.7th percentile), with all 3 passing models agreeing in sign. ESRRA is chosen within the group only because it is the sole well-expressed member in subcutaneous adipose (34.08 TPM, own model) while ESRRG/ESRRB are near zero; ESRRA's own z (17.39) is the lowest of the passing members, so the TF choice is expression-based and weak. | weak | [E08](#e08), [E07](#e07) |
| element | The variant sits in a dELS cCRE; the SCREEN activity numbers are for the adjacent cCRE and are cross-biosample maxima, so adipose activity of this element is not shown. | weak | [E03](#e03) |
| gene | FTO is the top L2G gene for credible sets containing this variant (0.99), but L2G is a locus-level score and does not show that this enhancer regulates FTO; no adipose eQTL for FTO is detected at this variant. | weak | [E05](#e05), [E19](#e19) |
| cell_type | ESRRA is expressed in bulk subcutaneous adipose (34.08 TPM); occupancy in preadipocytes is not demonstrated. | weak | [E08](#e08) |
| phenotype | Altered FTO dosage in adipose could change energy balance, matching the strong BMI/obesity association; no evidence here connects FTO expression to the phenotype. | weak | [E04](#e04), [E06c](#e06c) |

Predictions: ESRRA ChIP-seq in adipose/preadipocytes shows an allele-biased peak favouring C; ESRRA knockdown abolishes the allelic difference in a reporter; Allelic reporter activity is higher for C than T

Falsified if: No ESRRA occupancy at this element; Reporter activity is higher for T; ESRRA perturbation leaves element activity genotype-independent

### 4. H3: Alt C allele creates a TALE-homeodomain site (TGIF1/TGIF2 specificity) that represses the enhancer (p = 0.14)

TF TGIF1 (stated coverage own_model; registry own_model), alt allele binds more; element dELS enhancer EH38E3181208 in FTO intron 1; gene IRX3; cell type Subcutaneous adipose / preadipocytes.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | QBiC group G008 (TALE homeodomain) predicts the largest consistent alt gain among expressed groups (best model PKNOX2, z 54.71, effect +3.047; 9/9 models same sign; 95.5th to 99.7th percentile). The group names a shared specificity, not one TF; TGIF1 is chosen as the most expressed covered member in adipose (13.07 TPM, own model) with TGIF2 (11.62 TPM, z 42.72) a close alternative. TGIF1's own z and sign are not shown in the group row, so the within-group assignment remains uncertain. | weak | [E09](#e09), [E07](#e07) |
| element | The gained site lies in a dELS cCRE; adipose-specific activity of this element is not established by the SCREEN maxima cited. | weak | [E03](#e03) |
| gene | TGIF proteins are TGF-beta pathway corepressors, so gained binding would be expected to damp this element rather than activate it; the long-range target is proposed to be IRX3/IRX5, which has no L2G or eQTL support here (L2G favours FTO; no adipose eQTL at this variant). | missing | [E02](#e02), [E05](#e05), [E19](#e19) |
| cell_type | TALE factors (TGIF1/2, MEIS1/2/3, PKNOX1) are all expressed in subcutaneous adipose, so the context is plausible; no preadipocyte-specific data are cited. | weak | [E09](#e09) |
| phenotype | A change in progenitor enhancer output could alter fat storage and body mass, consistent with the BMI/obesity association. | weak | [E04](#e04), [E06b](#e06b) |

Predictions: TGIF1/TGIF2 ChIP or EMSA shows C-preferential occupancy at this base; Knockdown of expressed TALE factors removes the allelic difference only in C-carrying cells; Reporter effect of C is repressive despite gained binding

Falsified if: No TALE-family occupancy at the element; Allelic effect persists after knockdown of all expressed TALE factors; Per-TF QBiC lookup shows TGIF1 does not gain binding on alt

### 5. H4: Alt allele strengthens a nuclear-receptor half-site bound by PPARG during adipogenesis (p = 0.07)

TF PPARG (stated coverage own_model; registry own_model), alt allele binds more; element dELS enhancer EH38E3181208 in FTO intron 1; gene FTO; cell type Differentiating adipocytes (subcutaneous adipose).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | QBiC group G002 predicts increased alt binding at an already very strong site (best model NR4A3, z 32.74, effect +2.426; ref 99.6th to alt 100.0th percentile), but members disagree on direction and PPARG's own z and sign are not shown. PPARG was chosen on expression (111.14 TPM, own model) and prior role, which is a weak basis. Factorbook shows no ENCODE PPARG ChIP-seq peak containing or within 100 bp of the variant, which argues against occupancy (though a relevant biosample may be missing). | weak | [E10](#e10), [E20](#e20), [E07](#e07) |
| element | The variant is in a dELS cCRE, the class PPARG typically occupies, but no PPARG peak is observed there. | weak | [E03](#e03), [E20](#e20) |
| gene | FTO is the top L2G gene (0.99), yet there is no adipose eQTL for FTO at this variant, so enhancer-to-FTO regulation is unsupported. | weak | [E05](#e05), [E19](#e19) |
| cell_type | PPARG is highly expressed in bulk subcutaneous adipose; the chain requires differentiating adipocytes, which the expression context does not resolve. | weak | [E10](#e10) |
| phenotype | Altered adipogenic gene dosage would change adiposity and downstream glycaemic traits associated with this variant. | weak | [E04](#e04) |

Predictions: PPARG ChIP-seq in differentiated primary adipocytes shows an allele-biased peak here despite its absence in ENCODE; Allelic effect appears only after adipogenic induction; Rosiglitazone amplifies the allelic difference

Falsified if: No PPARG binding at the element in adipocyte ChIP-seq (already supported by E20); Allelic reporter difference is identical before and after differentiation

## Prediction matrix

| Test | Cost | Separates top two | H5 | H1 | H2 | H3 | H4 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Allele-specific ARID5B EMSA/ChIP at chr16:53767042 in human preadipocytes | medium | yes | No allelic difference for any TF, including ARID5B | Stronger ARID5B binding to T than C | No ARID5B allelic difference | No ARID5B allelic difference | No ARID5B allelic difference |
| Allelic reporter / MPRA of the 200 bp element (T vs C) in preadipocytes | medium | yes | No significant difference between alleles | C allele more active (repressor lost) | C allele more active (activator gained) | C allele less active (repressor gained) | C allele more active only after adipogenic induction |
| GTEx adipose eQTL lookup for FTO/IRX3/IRX5/RPGRIP1L (existing, E19) | existing data | no | No eQTL; consistent | No FTO eQTL expected; consistent (IRX3 effect would be progenitor-restricted) | Predicts an FTO eQTL; none observed, disfavoured | No FTO eQTL expected; consistent | Predicts an FTO eQTL; none observed, disfavoured |
| ENCODE/Factorbook PPARG ChIP-seq peak overlap (existing, E20) | existing data | no | No peak; consistent | No PPARG peak needed; consistent | No PPARG peak needed; consistent | No PPARG peak needed; consistent | Predicts PPARG occupancy; none found, disfavoured |
| CRISPR base editing C>T at this single base in isogenic risk-allele preadipocytes, then RT-qPCR of FTO, IRX3, IRX5, UCP1 | high | yes | No expression change for any gene | IRX3/IRX5 fall, UCP1 rises, FTO unchanged | FTO falls, IRX3/IRX5 unchanged | IRX3/IRX5 rise (repression relieved on T) | FTO changes only in differentiated cells |
| QBiC-SELEX per-TF lookup of ARID5B coverage (existing, E18) | existing data | yes | Consistent with no predicted ARID5B effect | not_in_coverage: no QBiC support available for ARID5B direction | Irrelevant | Irrelevant | Irrelevant |

## Next experiment

Run an allelic luciferase reporter / small MPRA of the 200 bp EH38E3181208 element (T vs C, both orientations) in human subcutaneous preadipocytes. It is the cheapest assay that distinguishes the top two chains: H1 predicts a reproducible allelic activity difference (C more active, repressor lost), while H5 (null) predicts no difference; a positive result also sets the direction needed to adjudicate H2/H3.

## Investigate calls

- qbic_tf_detail({"tf": "ARID5B"})
- eqtl_lookup({"tissue": "Adipose - Subcutaneous"})
- chip_peaks({"tf": "PPARG", "biosample": null})

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

> QBiC-SELEX screen of chr16:53767042:T>C: 997 models scored, 425 pass the gate (Bonferroni 0.05/997, p < 5.02e-05, |z| > 4.05), in 275 CIS-BP groups. Expression context: GTEx tissue median Adipose - Subcutaneous. Groups shown: 10; dropped because no TF in the group reaches 1 TPM: 53 (CUT; Homeodomain, 3 models z -47.91, C2H2 ZF, 1 model z -42.95, Homeodomain, 2 models z -30.65, C2H2 ZF, 2 models z 21.18, Homeodomain; POU, 1 model z -19.44). Passing groups ranked below the ones shown: 212. In the group rows, 'own model' means the TF has its own QBiC-SELEX model and 'mapped' that it is covered only through CIS-BP-mapped models of related TFs. A TF not named in any group row may still have its own model, even one that passes the gate: look it up with qbic_tf_detail before stating its coverage or a QBiC-SELEX direction for it. predicted_effect > 0 means the alternate allele binds more strongly. In vitro binding only: expression and chromatin decide whether a change matters.

<a id="e08"></a>**E08** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G037 (Nuclear receptor, 3 models): best model ESRRG_FL_TGAGCT40NGCA_KW_yin2017_0_3_7mer (own model of ESRRG), z 62.01, effect 2.149 (alt binds more); 3 passing models (3 with the best model's sign). Passing members: ESRRG z 62.01, ESRRB z 25.92, ESRRA z 17.39. TFs this group covers: ESRRA (own model) 34.08 TPM, ESR1 (own model) 2.07 TPM, ESR2 (mapped) 0.83 TPM, ESRRB (own model) 0.16 TPM, ESRRG (own model) 0.06 TPM; best model's site strength: ref 94.0th, alt 99.7th percentile of its k-mer coefficients.

<a id="e09"></a>**E09** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G008 (Homeodomain, 9 models): best model PKNOX2_eDBD_TAACGT40NGAT_KAN_yin2017_0_4_7mer (own model of PKNOX2), z 54.71, effect 3.047 (alt binds more); 9 passing models (9 with the best model's sign). Passing members: PKNOX2 z 54.71, TGIF2 z 42.72, MEIS3 z 40.95, TGIF2LX z 36.97, MEIS2 z 35.14 (+4 more). TFs this group covers: TGIF1 (own model) 13.07 TPM, TGIF2 (own model) 11.62 TPM, MEIS3 (own model) 9.23 TPM, PKNOX1 (own model) 7.35 TPM, MEIS2 (own model) 5.53 TPM, MEIS1 (own model) 4.65 TPM, PKNOX2 (own model) 2.8 TPM, TGIF2LX (own model) 0.0 TPM, TGIF2LY (own model) 0.0 TPM; best model's site strength: ref 95.5th, alt 99.7th percentile of its k-mer coefficients.

<a id="e10"></a>**E10** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G002 (Nuclear receptor, 29 models): best model NR4A3_DBD_TTCGTA20NTA_KH_nitta2015_1_3_7mer (own model of NR4A3), z 32.74, effect 2.426 (alt binds more); 19 passing models (18 with the best model's sign); members disagree on direction. Passing members: NR4A3 z 32.74, NR2C1 z 21.97, NR5A1 z 21.36, NR4A1 z 16.25, NR4A2 z 15.74 (+14 more). TFs this group covers: NR4A1 (own model) 139.74 TPM, NR1D1 (own model) 118.5 TPM, PPARG (own model) 111.14 TPM, NR2F2 (own model) 101.24 TPM, NR1H2 (mapped) 73.96 TPM, RXRB (own model) 63.05 TPM, NR1H3 (own model) 53.67 TPM, THRA (own model) 41.46 TPM, RXRA (own model) 39.73 TPM, RARA (own model) 37.57 TPM (+28 more); best model's site strength: ref 99.6th, alt 100.0th percentile of its k-mer coefficients.

<a id="e11"></a>**E11** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G007 (Forkhead, 10 models): best model FOXL1_NA_TGCTCG20NCTC_ESW_yang2017_0_2_7mer (own model of FOXL1), z -32.62, effect -1.076 (alt binds less); 7 passing models (6 with the best model's sign); members disagree on direction. Passing members: FOXL1 z -32.62, FOXC2 z -16.49, FOXG1 z -15.83, FOXC1 z -15.51, FOXF1 z 7.79 (+2 more). TFs this group covers: FOXJ3 (own model) 33.71 TPM, FOXJ2 (own model) 24.29 TPM, FOXC1 (own model) 22.42 TPM, FOXP4 (mapped) 20.41 TPM, FOXP1 (own model) 14.95 TPM, FOXK2 (mapped) 13.86 TPM, FOXK1 (own model) 10.32 TPM, FOXS1 (mapped) 4.39 TPM, FOXF2 (mapped) 3.25 TPM, FOXC2 (own model) 3.09 TPM (+18 more); best model's site strength: ref 99.9th, alt 98.9th percentile of its k-mer coefficients.

<a id="e12"></a>**E12** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G043 (bZIP, 3 models): best model NFE2L3_FL_TACGAG20NAGC_KH_nitta2015_1_3_7mer (own model of NFE2L3), z 28.3, effect 1.411 (alt binds more); 2 passing models (2 with the best model's sign). Passing members: NFE2L3 z 28.3, NFE2L1 z 8.62. TFs this group covers: NFE2L1 (own model) 185.6 TPM, NFE2L2 (mapped) 65.58 TPM, NFE2L3 (own model) 8.21 TPM, NFE2 (own model) 0.6 TPM; best model's site strength: ref 96.9th, alt 99.7th percentile of its k-mer coefficients.

<a id="e13"></a>**E13** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G033 (bZIP, 3 models): best model ATF2_eDBD_TGAACC40NCCA_KP_yin2017_0_3_7mer (own model of ATF2), z 28.08, effect 1.047 (alt binds more); 3 passing models (3 with the best model's sign). Passing members: ATF2 z 28.08, CREB5 z 27.01, ATF7 z 10.29. TFs this group covers: ATF7 (own model) 38.23 TPM, ATF2 (own model) 26.88 TPM, CREB5 (own model) 6.45 TPM, ATF7-NPFF (mapped); best model's site strength: ref 98.6th, alt 99.9th percentile of its k-mer coefficients.

<a id="e14"></a>**E14** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G022 (Forkhead, 4 models): best model FOXB1_NA_TGAGCA30NCGA_ESAI_yang2017_0_4_7mer (own model of FOXB1), z -23.72, effect -1.232 (alt binds less); 4 passing models (4 with the best model's sign). Passing members: FOXB1 z -23.72, FOXA1 z -13.3, FOXA3 z -8.79, FOXA2 z -7.96. TFs this group covers: FOXS1 (mapped) 4.39 TPM, FOXA3 (own model) 0.06 TPM, FOXA1 (own model) 0.05 TPM, FOXA2 (own model) 0.0 TPM, FOXB1 (own model) 0.0 TPM, FOXB2 (mapped) 0.0 TPM; best model's site strength: ref 99.8th, alt 99.0th percentile of its k-mer coefficients.

<a id="e15"></a>**E15** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G048 (Homeodomain, 3 models): best model SIX1_eDBD_TTAACC40NCTA_KQ_yin2017_0_4_7mer (own model of SIX1), z -22.75, effect -0.856 (alt binds less); 3 passing models (3 with the best model's sign). Passing members: SIX1 z -22.75, SIX2 z -19.68, SIX4 z -8.7. TFs this group covers: SIX5 (mapped) 16.4 TPM, SIX1 (own model) 8.49 TPM, SIX2 (own model) 5.54 TPM, SIX4 (own model) 0.69 TPM; best model's site strength: ref 99.8th, alt 99.0th percentile of its k-mer coefficients.

<a id="e16"></a>**E16** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G009 (Paired box, 8 models): best model PAX7_FL_TCGTTT40NGTC_KAF_yin2017_0_4_7mer (own model of PAX7), z 22.55, effect 1.934 (alt binds more); 8 passing models (8 with the best model's sign). Passing members: PAX7 z 22.55, PAX3 z 16.01, PAX9 z 15.43, PAX8 z 15.39, PAX2 z 12.88 (+3 more). TFs this group covers: PAX8 (own model) 2.24 TPM, PAX3 (own model) 0.4 TPM, PAX9 (own model) 0.14 TPM, PAX5 (own model) 0.04 TPM, PAX1 (own model) 0.03 TPM, PAX2 (own model) 0.01 TPM, PAX6 (own model) 0.01 TPM, PAX4 (own model) 0.0 TPM, PAX7 (own model) 0.0 TPM; best model's site strength: ref 90.7th, alt 99.7th percentile of its k-mer coefficients.

<a id="e17"></a>**E17** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G162 (Unknown, 1 model): best model DACH1_FL_TG40NTGTGTT_YWO_jolma2025_0_3_7mer (own model of DACH1), z 21.79, effect 0.795 (alt binds more); 1 passing models (1 with the best model's sign). Passing members: DACH1 z 21.79. TFs this group covers: DACH1 (own model) 6.37 TPM; best model's site strength: ref 86.1th, alt 99.9th percentile of its k-mer coefficients.

<a id="e18"></a>**E18** qbic_tf_detail, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> {"tf":"ARID5B","symbol":"ARID5B","via":"hgnc_symbol","notes":[],"coverage":"not_in_coverage"}

<a id="e19"></a>**E19** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr16_53767042_T_C_b38&datasetId=gtex_v8; retrieved 2026-10-25T17:30:38+00:00)

> 0 significant GTEx v8 single-tissue eQTLs for chr16_53767042_T_C_b38 in tissues matching 'Adipose - Subcutaneous'. NES is the effect of the alt allele (C) relative to ref (T).

<a id="e20"></a>**E20** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-25T22:29:26+00:00)

> No ENCODE PPARG ChIP-seq peak contains chr16:53767042:T>C. Absence can also mean no PPARG experiment in that biosample. 0 peaks lie within 100 bp without containing it.
