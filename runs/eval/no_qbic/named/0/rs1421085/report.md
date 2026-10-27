# rs1421085 and Obesity (FTO)

Configuration `no_qbic`, named mode, seed 0. Models: generator claude-opus-5, critic claude-sonnet-5-5, summariser claude-haiku-5-5. Cost $0.51 over 8 model calls; 151 s.

Variant `chr16:53767042:T>C` (germline); expression context: GTEx:Adipose - Subcutaneous (proxy for preadipocytes).

## Ranked chains

### 1. H4: Null: rs1421085 is a tag for another causal variant in the FTO intron-1 LD block, with no TF-mediated effect of its own (p = 0.47)

Null chain: no TF-mediated effect of this variant.

Predictions: Isogenic editing of rs1421085 alone produces no expression or chromatin change.; No allele-specific protein binding is detectable at the site in any nuclear extract; QBiC-SELEX returns no appreciable allelic score difference.; Deeper fine-mapping shifts the credible-set peak to a neighbouring variant; current PIPs are only 0.41-0.85 and no molecular QTL credible set contains the variant.; No adipose eQTL for FTO, IRX3, IRX5 or RPGRIP1L is found, consistent with the current GTEx null.

Falsified if: Isogenic single-base editing changes target-gene expression or adipocyte phenotype.; Allele-specific ChIP, EMSA or reporter assays show a reproducible effect at this base.; Fine-mapping resolves the signal to rs1421085 with PIP near 1.

### 2. H1: An AT-rich-binding ARID-family repressor (ARID5B) binds the ref T allele; loss on the C allele derepresses a long-range enhancer acting on IRX3/IRX5 in adipocyte progenitors (p = 0.33)

TF ARID5B (stated coverage not_checked; registry not_in_coverage), ref allele binds more; element dELS cCRE EH38E3181208 in FTO intron 1 (chr16:53766999-53767220); gene IRX3 (and IRX5); cell type Adipocyte progenitors / preadipocytes (subcutaneous adipose as proxy).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | ARID5B is proposed to bind the ref T allele more strongly at this AT-rich site, with reduced occupancy on the alt C allele. There is no supporting binding evidence in hand: no QBiC-SELEX model has been looked up (coverage not_checked), and Factorbook shows no ENCODE ARID5B peak containing or within 100 bp of the variant, though that absence may simply reflect no ARID5B experiment in the relevant biosample (E08). The TF name and the direction are therefore hypotheses to be tested, not evidence-backed claims; the only site-level facts are that it is an intronic base of moderate conservation (GERP 2.55) in an enhancer-like cCRE. | missing | [E01](#e01), [E03](#e03), [E08](#e08) |
| element | The variant lies within cCRE EH38E3181208, annotated distal enhancer-like; the quoted DNase z 3.5 / H3K27ac z 3.2 values belong to the neighbouring cCRE EH38E3181207 and are maxima across biosamples, so adipose-specific activity of the variant's own element is not shown. | weak | [E03](#e03) |
| gene | IRX3 is 520 kb away in the same interval and is proposed as a long-range target; this rests only on distance (E02), since Open Targets lists no molecular QTL credible sets and assigns L2G to FTO (0.99) with IRX3 absent (E05), and no contact, eQTL or perturbation data link the element to IRX3/IRX5. | missing | [E02](#e02), [E05](#e05), [E07](#e07) |
| cell_type | Subcutaneous adipose is the assayed context and body-composition/impedance traits map here, but no preadipocyte-specific data are cited; the cell-type assignment is an inference. | weak | [E04](#e04), [E05](#e05) |
| phenotype | The variant is robustly associated with BMI, obesity and secondary glycaemic traits with the T allele as the reported effect allele (E04, E06b, E06c); the proposed thermogenic/lipid-storage mechanism downstream of IRX3/IRX5 is not supported by any cited evidence. | weak | [E04](#e04), [E06b](#e06b), [E06c](#e06c) |

Predictions: A QBiC-SELEX lookup returns an ARID5B own or mapped model with a T-preferring score at this site.; Allele-specific ARID5B ChIP or EMSA in preadipocyte nuclear extract shows stronger binding to T.; Isogenic C-to-T editing in adipocyte progenitors lowers IRX3/IRX5 mRNA with no change in FTO mRNA.; Adipose eQTL/chromatin-contact data, when available, link this element to IRX3/IRX5 rather than FTO.

Falsified if: No allelic difference in nuclear protein binding at this base in adipose-lineage extract.; Editing the base changes FTO but not IRX3/IRX5.; ARID5B is not expressed in adipose progenitors.; QBiC-SELEX shows no ARID5B-like specificity change at this site.

### 3. H2: The same enhancer-level binding change acts locally on FTO itself (p = 0.14)

TF ARID5B (stated coverage not_checked; registry not_in_coverage), ref allele binds more; element Intronic dELS cCRE EH38E3181208 within FTO intron 1; gene FTO; cell type Subcutaneous adipose tissue.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | Same unverified ARID5B claim as H1: ref T binds more, alt C less. No QBiC-SELEX lookup has been done (not_checked) and no ENCODE ARID5B peak overlaps the site (E08). | missing | [E01](#e01), [E03](#e03), [E08](#e08) |
| element | The element sits 65 kb into the FTO gene body and is annotated enhancer-like; looping to the FTO promoter is assumed, not shown, as no contact data are cited. | weak | [E02](#e02), [E03](#e03) |
| gene | Open Targets L2G gives FTO 0.99 across credible sets, but this is a statistical prioritisation that favours the host gene, and there are 0 molecular QTL credible sets; GTEx reports no significant adipose eQTL for this variant. | weak | [E05](#e05), [E07](#e07) |
| cell_type | Subcutaneous adipose is the stated expression context; no cited evidence shows adipose-specific FTO regulation by this element. | missing | [E05](#e05), [E07](#e07) |
| phenotype | Genome-wide significant BMI, weight and obesity associations exist (E04, E06c), but no evidence shows FTO dosage mediates them or in which direction. | weak | [E04](#e04), [E06c](#e06c) |

Predictions: Isogenic editing of the base changes FTO mRNA in adipose-lineage cells.; A deeper adipose/preadipocyte eQTL dataset reveals an FTO eQTL colocalising with the BMI signal, despite the current null in GTEx v8.; Chromatin contacts from the element go preferentially to the FTO promoter rather than IRX3.

Falsified if: No FTO expression difference by genotype in adipose or preadipocytes after editing.; Contact maps show the element skips the FTO promoter.; Editing changes IRX3/IRX5 only.

### 4. H3: A CUT-homeodomain factor (CUX1) binds the alt C allele more and alters RPGRIP1L (p = 0.06)

TF CUX1 (stated coverage not_checked; registry own_model), alt allele binds more; element Intronic dELS cCRE EH38E3181208; the adjacent cCRE EH38E3181207 is annotated with RPGRIP1L among its nearby genes; gene RPGRIP1L; cell type Hypothalamic neurons (adipose only as assayed proxy).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | CUX1 is a speculative choice of CUT-homeodomain factor said to bind the alt C allele more strongly. No cited evidence names CUX1, no QBiC-SELEX lookup has been made (not_checked), and the direction opposes H1/H2 without support. | missing | [E03](#e03) |
| element | SCREEN lists RPGRIP1L among genes near the adjacent cCRE EH38E3181207, not the variant's own cCRE; this is proximity annotation, not a regulatory link. | weak | [E03](#e03) |
| gene | RPGRIP1L lies 63 kb from its TSS and has the second-best but much weaker L2G score (0.20-0.36 versus FTO 0.99); no eQTL supports it. | weak | [E02](#e02), [E05](#e05), [E07](#e07) |
| cell_type | No cited evidence bears on hypothalamic neurons or cilia; this claim rests on outside knowledge and is unsupported here. | missing | none |
| phenotype | BMI and obesity associations (E04) and a neuroticism association with additive T-allele effect (E06d) exist, but neither is connected by evidence to RPGRIP1L or leptin signalling. | weak | [E04](#e04), [E06d](#e06d) |

Predictions: Allele-specific reporter activity differs in neuronal but not adipocyte cells.; RPGRIP1L expression differs by genotype in brain or ciliated cells.; CUX1 knockdown abolishes the allelic reporter difference.; A QBiC-SELEX lookup shows a CUT-homeodomain specificity gain on the C allele.

Falsified if: No RPGRIP1L expression difference by genotype in any tissue.; The allelic effect is adipose-restricted and tracks IRX3/IRX5 or FTO.; QBiC-SELEX shows the C allele loses rather than gains binding.

## Prediction matrix

| Test | Cost | Separates top two | H4 | H1 | H2 | H3 |
| --- | --- | --- | --- | --- | --- | --- |
| QBiC-SELEX detail lookup for ARID5B (and for CUT-homeodomain/CUX1) at chr16:53767042 T>C | existing data | yes | No appreciable allelic score difference for any covered TF, or the site is not in coverage | ARID5B own or mapped model present, with T allele scoring higher (loss of binding on C) | Same as H1: T-preferring ARID-family score | CUT-homeodomain specificity gains score on the C allele; ARID signal absent or weak |
| tf_expression of ARID5B in GTEx Adipose - Subcutaneous | existing data | no | Expression uninformative; no prediction | ARID5B expressed at appreciable level in adipose | ARID5B expressed in adipose | Expression of ARID5B is irrelevant; CUX1 expressed broadly including brain |
| eQTL lookup across tissues for FTO, IRX3, IRX5, RPGRIP1L (beyond the adipose null in E07) | existing data | yes | No eQTL in any tissue, consistent with E07 | IRX3/IRX5 effect in adipose-lineage or preadipocyte data | FTO effect in adipose | RPGRIP1L effect, preferentially in brain |
| Allele-specific EMSA / allelic reporter (MPRA) of the 200 bp element in preadipocytes | medium | yes | No reproducible allelic difference in binding or reporter output | T allele binds more protein; C allele shows higher reporter output (repressor loss) | T allele binds more protein; allelic reporter difference in adipocyte cells | C allele binds more protein; difference appears in neuronal, not adipocyte, cells |
| Isogenic CRISPR C-to-T conversion in human adipocyte progenitors with RNA-seq | high | yes | No expression or chromatin change at any candidate gene | IRX3/IRX5 fall; FTO unchanged | FTO changes; IRX3/IRX5 unchanged | No adipocyte change; effect only in neuronal models on RPGRIP1L |
| ARID5B ChIP-seq in preadipocytes (addressing the E08 absence, which may reflect no experiment) | medium | yes | No peak or no allelic bias | Peak over the element, allele-biased toward T | Peak over the element, allele-biased toward T | No ARID5B peak |

## Next experiment

Run the QBiC-SELEX detail lookup for ARID5B (and the CUT-homeodomain group) at chr16:53767042 T>C. It uses existing data at essentially no cost, resolves the coverage status that is currently not_checked for every chain, and gives the first direct test of whether any TF has an allelic binding difference at this base: a T-preferring ARID5B score supports H1 over the null H4, while no appreciable allelic score difference leaves H4 dominant.

## Investigate calls

- eqtl_lookup({"tissue": "Adipose - Subcutaneous"})
- chip_peaks({"tf": "ARID5B", "biosample": null})
- literature_search({"query": "rs1421085 ARID5B IRX3 IRX5 enhancer adipocyte"})

## Flags

- none

Citation support: 0.93 of links cite only evidence that passed every check.

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

<a id="e07"></a>**E07** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr16_53767042_T_C_b38&datasetId=gtex_v8; retrieved 2026-10-25T17:30:38+00:00)

> 0 significant GTEx v8 single-tissue eQTLs for chr16_53767042_T_C_b38 in tissues matching 'Adipose - Subcutaneous'. NES is the effect of the alt allele (C) relative to ref (T).

<a id="e08"></a>**E08** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-25T17:30:39+00:00)

> No ENCODE ARID5B ChIP-seq peak contains chr16:53767042:T>C. Absence can also mean no ARID5B experiment in that biosample. 0 peaks lie within 100 bp without containing it.

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

<a id="e09a"></a>**E09a** literature_search, Europe PMC abstract, PMID 42877975 (https://europepmc.org/article/MED/42877975; retrieved 2026-10-26T00:21:07+00:00)

> We highlight variant-to-function strategies to resolve causal pathways and discuss emerging scalable approaches to accelerate biological learning from genetic discovery and translate these insights into adipose-directed therapeutics for cardiometabolic disease.

<a id="e09b"></a>**E09b** literature_search, Europe PMC abstract, PMID 41273414 (https://europepmc.org/article/MED/41273414; retrieved 2026-10-26T00:21:07+00:00)

> Genome-wide association studies have identified over 1200 loci associated with type 2 diabetes, yet only a modest proportion of disease heritability has been explained, and most risk variants lie in non-coding regions, complicating biological interpretation.
