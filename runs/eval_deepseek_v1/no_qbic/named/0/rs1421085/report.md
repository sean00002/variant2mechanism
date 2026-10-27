# rs1421085 and Obesity (FTO)

Configuration `no_qbic`, named mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.04 over 9 model calls; 304 s.

Variant `chr16:53767042:T>C` (germline); expression context: GTEx:Adipose - Subcutaneous (proxy for preadipocytes).

## Ranked chains

### 1. C4: Null: linked causal variant or no TF-mediated allelic effect (p = 0.55)

Null chain: no TF-mediated effect of this variant.

Predictions: No allele-specific TF occupancy at rs1421085 in adipose cells.; No allele-specific enhancer reporter activity in adipose cells.; The GWAS signal is explained by a linked causal variant or by regulatory variation not mediated by this base.; E07 finding no significant subcutaneous adipose eQTL and E08 finding no ARID5B ChIP peak in subcutaneous adipose are consistent with the null, although neither absence is proof.

Falsified if: Allele-specific TF binding and allele-specific enhancer activity are demonstrated in adipocytes.; Conditioning on linked variants does not remove the rs1421085 signal.; A molecular QTL or reporter assay shows a direct allelic effect of this base.

### 2. C1: ARID5B loss on the C allele derepresses IRX3/IRX5 (p = 0.22)

TF ARID5B (stated coverage not_checked; registry not_in_coverage), ref allele binds more; element dELS enhancer EH38E3181208 in an FTO intron; gene IRX3/IRX5 (long-range); cell type subcutaneous adipose / preadipocyte.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | ARID5B is proposed to bind the ref T allele more strongly than the alt C allele; the C allele is proposed to disrupt an ARID5B motif. No direct allele-specific binding, QBiC-SELEX, ChIP, or reporter evidence is supplied for this claim. E08 reports no ARID5B ChIP-seq peak in subcutaneous adipose, although absence can reflect no experiment in that biosample. | missing | none |
| element | The variant lies in the distal enhancer-like cCRE EH38E3181208 (dELS), so it could alter enhancer activity. E01 annotates the variant only as an intron variant with no regulatory features, and E03 gives maximum z-scores across biosamples rather than adipose-specific activity. | weak | [E03](#e03) |
| gene | The proposed long-range target is IRX3, with possible IRX5 involvement. E02 gives only distance to IRX3 and does not mention IRX5; E05 L2G favors FTO (0.99), not IRX3/IRX5; E07 reports no significant subcutaneous adipose eQTL for this variant. No chromatin-contact or perturbation evidence links this enhancer to IRX3/IRX5. | missing | [E02](#e02), [E05](#e05), [E07](#e07) |
| cell_type | The relevant context is proposed to be subcutaneous adipose tissue or preadipocytes. No supplied evidence ID shows ARID5B expression, enhancer activity, or IRX3/IRX5 regulation specifically in that context; E03 reports only maxima across ENCODE biosamples. | missing | none |
| phenotype | The locus is strongly associated with obesity/BMI. E06d reports that the C allele was associated with overweight/obesity in prior work, so the proposed mechanism is that reduced ARID5B binding on C derepresses IRX3/IRX5 and raises obesity risk. E04 lists T as the catalog effect allele but gives no trait-increasing sign, so the allele direction is not fully resolved by E04 alone. | weak | [E04](#e04), [E06b](#e06b), [E06c](#e06c), [E06d](#e06d) |

Predictions: Allele-specific ARID5B occupancy is higher on T than C at rs1421085 in preadipocytes.; An allele-specific enhancer reporter in adipose cells shows higher activity for C than T if ARID5B is a repressor.; IRX3 and/or IRX5 expression is higher on the C allele in adipose cells.; CRISPRi of EH38E3181208 or ARID5B knockdown changes IRX3/IRX5 or thermogenic gene expression.

Falsified if: Allele-specific ARID5B binding is absent in preadipocytes.; The enhancer reporter shows no T-vs-C difference in adipose cells.; IRX3/IRX5 expression or thermogenic genes do not respond to ARID5B or enhancer perturbation.; Chromatin-contact assays do not link EH38E3181208 to IRX3/IRX5 in adipose cells.

### 3. C2: ARID5B allelic occupancy changes FTO dosage (p = 0.18)

TF ARID5B (stated coverage not_checked; registry not_in_coverage), ref allele binds more; element dELS enhancer EH38E3181208 in an FTO intron; gene FTO; cell type subcutaneous adipose / preadipocyte.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | ARID5B is proposed to bind the ref T allele more strongly than the alt C allele. This is a motif-based proposal only; no direct allele-specific binding evidence is supplied. E08 found no ARID5B ChIP-seq peak in subcutaneous adipose, with the caveat that absence can mean no ARID5B experiment in that biosample. | missing | none |
| element | The variant lies in dELS enhancer EH38E3181208 within the FTO gene body, so it could alter an FTO-associated enhancer. E01 calls the variant an intron variant with no regulatory features, while E03 directly annotates the cCRE. | weak | [E03](#e03) |
| gene | FTO is the L2G-preferred target: E02 places the variant in the FTO gene body, and E05 gives FTO a strong L2G score of 0.99. However, E07 reports no significant subcutaneous adipose eQTL for this variant, and no chromatin-contact or perturbation evidence directly links EH38E3181208 to FTO expression. | weak | [E02](#e02), [E05](#e05), [E07](#e07) |
| cell_type | The proposed context is subcutaneous adipose tissue or preadipocytes. No supplied evidence ID demonstrates ARID5B occupancy or enhancer activity in that cell type; the case expression context alone is not molecular evidence. | missing | none |
| phenotype | The locus is strongly associated with obesity/BMI, and E06d reports the C allele as associated with overweight/obesity. The proposed chain is that reduced ARID5B binding on C changes FTO dosage and adipocyte biology, but the direction of any FTO expression change and its causal effect on obesity are not established by the supplied evidence. E04 lists T as the catalog effect allele without a sign. | weak | [E04](#e04), [E06b](#e06b), [E06c](#e06c), [E06d](#e06d) |

Predictions: Allele-specific ARID5B occupancy is higher on T than C at rs1421085 in preadipocytes.; FTO expression or FTO promoter contact differs by allele in adipose cells.; An allele-specific enhancer reporter in adipose cells is sensitive to the T/C difference.

Falsified if: No allele-specific ARID5B binding is detected.; FTO expression or enhancer-promoter contact is unchanged by the enhancer allele.; Adipose allele-specific expression or eQTL assays show no FTO effect.; The FTO L2G signal is fully explained by linkage to another causal variant.

### 4. C3: ARID5B allelic occupancy changes RPGRIP1L (p = 0.05)

TF ARID5B (stated coverage not_checked; registry not_in_coverage), ref allele binds more; element dELS enhancer EH38E3181208 in an FTO intron; gene RPGRIP1L; cell type subcutaneous adipose / preadipocyte.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | ARID5B is proposed to bind the ref T allele more strongly than the alt C allele, as a motif-based proposal without direct binding data in this evidence set. No QBiC-SELEX screen row or QBiC detail for ARID5B was supplied. | missing | none |
| element | The variant lies in the distal enhancer-like cCRE EH38E3181208 (dELS). E03 supports the element annotation; E01 reports no regulatory features and an intron-variant consequence. | weak | [E03](#e03) |
| gene | RPGRIP1L is a nearby protein-coding gene with a secondary L2G score in E05. E02 gives only distance, E05 strongly favors FTO over RPGRIP1L, and E07 reports no significant subcutaneous adipose eQTL for this variant. No evidence shows this enhancer targets RPGRIP1L. | weak | [E02](#e02), [E05](#e05), [E07](#e07) |
| cell_type | The proposed context is subcutaneous adipose tissue or preadipocytes, but no cited evidence shows RPGRIP1L regulation or ARID5B activity in that context. | missing | none |
| phenotype | The locus is associated with obesity/BMI, and E06d reports the C allele as associated with overweight/obesity. The proposed RPGRIP1L-mediated contribution to obesity is not supported by direct molecular or perturbation evidence. | weak | [E04](#e04), [E06b](#e06b), [E06c](#e06c), [E06d](#e06d) |

Predictions: RPGRIP1L expression differs by allele in adipose cells.; EH38E3181208 contacts the RPGRIP1L promoter in adipose cells.; ARID5B perturbation changes RPGRIP1L expression.

Falsified if: RPGRIP1L expression is unchanged by the allele in adipose cells.; No allele-specific ARID5B binding or enhancer activity is seen.; Chromatin-contact assays do not link EH38E3181208 to RPGRIP1L in adipose cells.; RPGRIP1L perturbation does not affect adipocyte phenotypes.

## Prediction matrix

| Test | Cost | Separates top two | C4 | C1 | C2 | C3 |
| --- | --- | --- | --- | --- | --- | --- |
| Allele-specific ARID5B binding assay (EMSA/SPR with recombinant ARID5B, or allele-specific ARID5B ChIP-qPCR in heterozygous preadipocytes) at rs1421085 | low | yes | No allele-specific ARID5B binding. | ARID5B binds T more strongly than C. | ARID5B binds T more strongly than C. | ARID5B binds T more strongly than C. |
| Allele-specific enhancer reporter (luciferase or MPRA) for EH38E3181208 in subcutaneous preadipocytes/adipocytes | medium | yes | No allele-specific enhancer activity. | C allele has higher enhancer activity than T if ARID5B represses. | C allele has higher enhancer activity than T if ARID5B represses. | C allele has higher enhancer activity than T if ARID5B represses. |
| Adipose allele-specific expression or eQTL/ASE assay for IRX3, IRX5, FTO, and RPGRIP1L | medium | yes | No allele-specific expression for these genes. | C allele increases IRX3 and/or IRX5 expression. | C allele changes FTO expression. | C allele changes RPGRIP1L expression. |
| Chromatin-contact assay (4C/Hi-C) from EH38E3181208 in subcutaneous adipose or preadipocytes | high | yes | No specific enhancer-promoter contact consistent with a direct allelic mechanism. | EH38E3181208 contacts IRX3/IRX5 in adipose cells. | EH38E3181208 contacts the FTO promoter in adipose cells. | EH38E3181208 contacts the RPGRIP1L promoter in adipose cells. |
| ARID5B knockdown or CRISPRi of EH38E3181208 in preadipocytes with target-gene and thermogenic readouts | high | yes | No ARID5B-dependent or enhancer-dependent change. | ARID5B knockdown or enhancer CRISPRi changes IRX3/IRX5 and thermogenic genes. | ARID5B knockdown or enhancer CRISPRi changes FTO expression. | ARID5B knockdown or enhancer CRISPRi changes RPGRIP1L expression. |

## Next experiment

Allele-specific ARID5B binding assay (EMSA/SPR with recombinant ARID5B or allele-specific ARID5B ChIP-qPCR in heterozygous subcutaneous preadipocytes) at rs1421085; this is the cheapest direct test separating the top two chains C4 and C1.

## Investigate calls

- eqtl_lookup({"tissue": "Adipose - Subcutaneous"})
- chip_peaks({"biosample": "subcutaneous adipose", "tf": "ARID5B"})
- literature_search({"query": "rs1421085 ARID5B IRX3 IRX5 enhancer adipocyte"})

## Flags

- none

Citation support: 0.60 of links cite only evidence that passed every check.

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

> ObjectivesThe aim of this study is to develop, validate, and apply a cost-effective 4-plex high-resolution melting (HRM) assay for simultaneous detection of FTO (rs9939609 and rs1421085) and PPAR-γ (rs1801282 and rs3856806) variants using standard laboratory equipment.

<a id="e06b"></a>**E06b** literature_search, Europe PMC abstract, PMID 41862896 (https://europepmc.org/article/MED/41862896; retrieved 2026-10-25T17:29:18+00:00)

> In the obesity group, the rs1421085 exhibited the strongest effect, with an odds ratio (OR) of 2.16 (95% CI: 1.58–2.95).

<a id="e06c"></a>**E06c** literature_search, Europe PMC abstract, PMID 41862896 (https://europepmc.org/article/MED/41862896; retrieved 2026-10-25T17:29:18+00:00)

> CONCLUSION: This meta-analysis provides strong evidence that FTO polymorphisms, particularly rs1421085 and rs9939609, are significantly associated with increased susceptibility to obesity in adults, while their impact on overweight is comparatively weaker.

<a id="e06d"></a>**E06d** literature_search, Europe PMC abstract, PMID 41591493 (https://europepmc.org/article/MED/41591493; retrieved 2026-10-25T17:29:18+00:00)

> Based on findings that experimental manipulation of the RNA m6A methylation in animal experiments can affect anxiety, and given that the C-allele of FTO rs1421085 had a significant association with indicators of overweight and obesity in our previous study, we have examined the possible association of FTO rs1421085 genotype with neuroticism in the same longitudinally observed sample.

<a id="e06e"></a>**E06e** literature_search, Europe PMC abstract, PMID 41591493 (https://europepmc.org/article/MED/41591493; retrieved 2026-10-25T17:29:18+00:00)

> Statistically significant assocation between the FTO rs1421085 genotype and neuroticism emerged by age 25, with an additive effect of each T-allele.

<a id="e06f"></a>**E06f** literature_search, Europe PMC abstract, PMID 42534632 (https://europepmc.org/article/MED/42534632; retrieved 2026-10-25T17:29:18+00:00)

> LEP variants were not significantly associated with obesity in Malaysians, and FTO variants showed mixed results, with rs9939609 (OR = 3.72, P = 0.009) and rs1421085 (OR = 3.22, P < 0.001) variants being associated with obesity and higher body mass index (BMI) in Indonesians, but no significant findings in Malaysians.

<a id="e07"></a>**E07** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr16_53767042_T_C_b38&datasetId=gtex_v8; retrieved 2026-10-25T17:30:38+00:00)

> 0 significant GTEx v8 single-tissue eQTLs for chr16_53767042_T_C_b38 in tissues matching 'Adipose - Subcutaneous'. NES is the effect of the alt allele (C) relative to ref (T).

<a id="e08"></a>**E08** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-25T17:30:39+00:00)

> No ENCODE ARID5B ChIP-seq peak contains chr16:53767042:T>C in biosamples matching 'subcutaneous adipose'. Absence can also mean no ARID5B experiment in that biosample. 0 peaks lie within 100 bp without containing it.

<a id="e09"></a>**E09** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=rs1421085%20ARID5B%20IRX3%20IRX5%20enhancer%20adipocyte&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T00:21:07+00:00)

> Europe PMC: 49 hits for 'rs1421085 ARID5B IRX3 IRX5 enhancer adipocyte'; top 8 with PMIDs:
> PMID 42877975 (2026): Human Genetics of Adipose Dysfunction: Genomic Mechanisms and Therapeutic Opportunities in Cardiometabolic Disease.
> PMID 42299366 (2026): Hepatogenomics of MAFLD in Asian Population: Genetic Polymorphisms and Pathway-Based Insights.
> PMID 39965570 (2025): An evolving understanding of multiple causal variants underlying genetic association signals.
> PMID 41273414 (2026): Bridging the variant-to-function gap in type 2 diabetes: advances and challenges.
> PMID 42589667 (2026): Functional Annotation of GWAS Loci Using Public Transcriptome and Epigenome Datasets Reveals Non-Coding Genes and Regulatory Elements Which May Contribute to BMI.
> PMID 36882962 (2023): Technologies, strategies, and cautions when deconvoluting genome-wide association signals: FTO in focus.
> PMID 37200795 (2023): <i>FTO</i> Gene Polymorphisms at the Crossroads of Metabolic Pathways of Obesity and Epigenetic Influences.
> PMID 37034418 (2022): Systematic assays and resources for the functional annotation of non-coding variants.

<a id="e09a"></a>**E09a** literature_search, Europe PMC abstract, PMID 36882962 (https://europepmc.org/article/MED/36882962; retrieved 2026-10-26T00:21:07+00:00)

> By reviewing studies of the FTO locus in the genetic etiology of obesity, we wish to highlight advances in the field fueled by the evolution of technical and analytic strategies in assessing the molecular bases for genetic associations.

<a id="e09b"></a>**E09b** literature_search, Europe PMC abstract, PMID 36882962 (https://europepmc.org/article/MED/36882962; retrieved 2026-10-26T00:21:07+00:00)

> Particular attention is drawn to extrapolating experimental findings from animal models and cell types to humans, as well as technical aspects used to identify long-range DNA interactions and their biological relevance with regard to the associated trait.
