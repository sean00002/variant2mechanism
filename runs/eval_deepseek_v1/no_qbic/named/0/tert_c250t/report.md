# TERT promoter C250T and Glioblastoma, melanoma, bladder

Configuration `no_qbic`, named mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.04 over 8 model calls; 114 s.

Variant `chr5:1295135:G>A` (somatic); expression context: DepMap:subtype=Glioblastoma (median of 54 lines).

## Ranked chains

### 1. gabpa_ets_alt: GABPA binds the alt allele at a de novo ETS motif in the TERT promoter (p = 0.55)

TF GABPA (stated coverage not_checked; registry own_model), alt allele binds more; element TERT promoter PLS cCRE EH38E3622530; gene TERT; cell type TERT-expressing glioblastoma/melanoma tumor cells; GABPA is expressed in DepMap glioblastoma lines.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The alt A allele is proposed to create/strengthen an ETS motif at TERT promoter C250T, so GABPA binds the alt allele more strongly than ref G. GABPA ChIP-seq peaks contain this base in HepG2 and SK-N-SH (E05); C250T generates a novel Ets/TCF site (E07e); GABPA-augmented DeepMEL2 identifies the TERT promoter mutation and ETS motif gains (E07h); and GABPA/GABPB1 activate the mutant TERT promoter and telomerase in glioblastoma, with GABPA depletion inhibiting telomerase (E07i,E07j). Direct allele-specific GABPA binding at this exact base is not shown. QBiC-SELEX coverage is not_checked because no screen row or qbic_tf_detail lookup for GABPA is supplied. | weak | [E05](#e05), [E07e](#e07e), [E07h](#e07h), [E07i](#e07i), [E07j](#e07j) |
| element | The variant lies within the TERT promoter PLS cCRE EH38E3622530, so an allelic GABPA binding change would act on a TERT promoter element. | supported | [E01](#e01), [E03](#e03) |
| gene | The element's target gene is TERT because TERT is 0 kb from its TSS and the variant is annotated as a TERT upstream/promoter variant. | supported | [E01](#e01), [E02](#e02) |
| cell_type | The relevant cell types are TERT-expressing tumor cells; TERT promoter mutations are common in melanoma and IDH-wildtype glioblastoma, and GABPA is expressed in DepMap glioblastoma lines. Bladder cancer is in the disease scope but is not directly quoted in the supplied evidence. | supported | [E04a](#e04a), [E04d](#e04d), [E04g](#e04g), [E06](#e06), [E07i](#e07i) |
| phenotype | Higher TERT/telomerase activity from the alt allele is proposed to promote tumor cell proliferation/progression. TERT promoter mutations are associated with telomerase activation in melanoma and glioblastoma, and GABPA/GABPB1 activation of the mutant TERT promoter is linked to telomerase and tumorigenic potential in glioblastoma; however, the supplied evidence does not directly measure an allele-specific C250T effect on proliferation. | weak | [E04a](#e04a), [E04b](#e04b), [E07b](#e07b), [E07c](#e07c), [E07i](#e07i), [E07j](#e07j) |

Predictions: Allele-specific GABPA ChIP/CUT&RUN or reporter assays show alt > ref at this TERT promoter base.; GABPA/GABPB1 knockdown reduces TERT expression or telomerase activity preferentially in C250T-mutant cells.; Disrupting the ETS motif abolishes the alt-specific GABPA binding and TERT reporter effect.

Falsified if: Allele-specific GABPA ChIP/CUT&RUN or reporter assays show no alt > ref difference at the C250T base.; The alt allele binds GABPA less than the ref allele.; GABPA/GABPB1 depletion does not reduce TERT expression or telomerase activity in C250T-mutant glioblastoma cells.

### 2. null_no_tf_mediated_effect: No TF-mediated effect of this variant (p = 0.35)

Null chain: no TF-mediated effect of this variant.

Predictions: No allele-specific TF binding is detected at this exact base.; Any TERT expression difference is due to a linked causal variant, a passenger mutation, or no functional effect of this base.; Ref and alt reporter alleles show equal activity in the relevant cell types.

Falsified if: Allele-specific TF binding and allele-specific TERT reporter expression are demonstrated for the alt allele.; A linked causal variant is excluded and the C250T base itself changes TF binding and TERT expression.

### 3. ets1_ets_alt: ETS1 binds the alt allele at the TERT promoter C250T ETS-like motif (p = 0.10)

TF ETS1 (stated coverage not_checked; registry own_model), alt allele binds more; element TERT promoter PLS cCRE EH38E3622530; gene TERT; cell type TERT-expressing glioblastoma/melanoma tumor cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | ETS1 is a less likely alternative ETS factor: C250T generates a novel Ets/TCF binding site (E07e), which could in principle recruit ETS1, but no ETS1-specific ChIP, QBiC-SELEX, reporter, or expression evidence is supplied. QBiC-SELEX coverage is not_checked because no screen row or qbic_tf_detail lookup for ETS1 is supplied. | weak | [E07e](#e07e) |
| element | The variant lies within the TERT promoter PLS cCRE EH38E3622530, so an ETS1 allelic effect would operate on a TERT promoter element. | supported | [E01](#e01), [E03](#e03) |
| gene | The element's target gene is TERT because TERT is 0 kb from its TSS and the variant is annotated as a TERT upstream/promoter variant. | supported | [E01](#e01), [E02](#e02) |
| cell_type | The relevant cell types are TERT-expressing tumor cells; TERT promoter mutations are common in melanoma and IDH-wildtype glioblastoma. No supplied evidence shows ETS1 expression in these tumor cells. | weak | [E04a](#e04a), [E04d](#e04d), [E04g](#e04g) |
| phenotype | If ETS1 bound the alt allele more strongly, higher TERT/telomerase activity could promote tumor cell proliferation/progression; the supplied literature supports TERT promoter mutation/telomerase association in melanoma and glioblastoma but does not measure an ETS1-dependent allele-specific effect. | weak | [E04a](#e04a), [E04b](#e04b), [E07b](#e07b), [E07c](#e07c) |

Predictions: Allele-specific ETS1 ChIP/CUT&RUN or reporter assays show alt > ref at this TERT promoter base.; ETS1 knockdown reduces TERT expression preferentially from the alt allele.; The effect is independent of GABPA depletion, distinguishing ETS1 from GABPA.

Falsified if: ETS1 ChIP/CUT&RUN or allele-specific reporter assays show no alt > ref difference at this base.; ETS1 is not expressed in the relevant tumor cells and GABPA fully accounts for allele-specific binding at this site.; ETS1 depletion has no effect on TERT expression from the alt allele.

## Prediction matrix

| Test | Cost | Separates top two | gabpa_ets_alt | null_no_tf_mediated_effect | ets1_ets_alt |
| --- | --- | --- | --- | --- | --- |
| Allele-specific GABPA ChIP-qPCR/CUT&RUN at C250T in a GABPA-expressing glioblastoma line (ref vs alt) | low | yes | Alt allele shows higher GABPA enrichment than ref at the C250T base in GABPA-expressing glioblastoma cells. | No allele-specific TF binding at this exact base. | GABPA allelic enrichment is absent or not required; ETS1, not GABPA, is the relevant alt-specific factor. |
| GABPA/GABPB1 knockdown in C250T-heterozygous glioblastoma cells, measuring TERT/telomerase | low | no | GABPA/GABPB1 knockdown reduces TERT expression or telomerase activity in C250T-mutant glioblastoma cells. | No allele-specific dependence on GABPA/GABPB1 for the C250T effect. | GABPA/GABPB1 knockdown has little or no allele-specific effect; ETS1 knockdown is the relevant perturbation. |
| ETS1 knockdown in C250T-heterozygous glioblastoma cells, measuring allele-specific TERT expression | low | no | ETS1 knockdown does not preferentially reduce TERT from the alt allele. | No allele-specific ETS1-dependent effect. | ETS1 knockdown preferentially reduces TERT expression from the alt allele. |
| TERT promoter ref-vs-alt luciferase reporter in a GABPA-expressing glioblastoma line, with and without ETS motif mutation | low | yes | Alt > ref reporter activity, abolished by mutating the ETS motif. | Ref and alt reporter alleles show equal activity. | Alt > ref reporter activity, but the effect should track ETS1 rather than GABPA in perturbation assays. |

## Next experiment

Allele-specific GABPA ChIP-qPCR (or CUT&RUN-qPCR) at C250T in a GABPA-expressing glioblastoma line, comparing alt and ref allele enrichment; this is the cheapest direct test separating the GABPA chain from the null chain.

## Investigate calls

- chip_peaks({"biosample": null, "tf": "GABPA"})
- tf_expression({"context": "DepMap:subtype=Glioblastoma", "tf": "GABPA"})
- literature_search({"query": "TERT promoter C250T allele-specific reporter GABPA ETS binding glioblastoma"})

## Flags

- none

Citation support: 1.00 of links cite only evidence that passed every check.

## Evidence

<a id="e01"></a>**E01** variant_annotation, Ensembl VEP (GRCh38) (https://rest.ensembl.org/vep/human/region/5:1295135-1295135:1/A?content-type=application/json&Conservation=1; retrieved 2026-10-25T17:26:00+00:00)

> Variant chr5:1295135:G>A (GRCh38), allele string G/A
> Known IDs: rs1561215364
> Most severe consequence: upstream_gene_variant
> Regulatory features: ENSR5_832QG promoter
> GERP conservation score at the site: -4.69
> Transcript consequences: TERT (upstream_gene_variant)

<a id="e02"></a>**E02** nearest_genes, Ensembl overlap (protein_coding) (https://rest.ensembl.org/overlap/region/human/5:295135-2295135?feature=gene;biotype=protein_coding;content-type=application/json; retrieved 2026-10-25T17:25:54+00:00)

> 23 protein-coding genes within 1000 kb of chr5:1295135:G>A, by distance to TSS:
> TERT: 0.0 kb from TSS (upstream, strand -1)
> CLPTM1L: 50.0 kb from TSS (downstream, strand -1)
> SLC6A18: 69.8 kb from TSS (downstream, strand +1)
> SLC6A19: 93.5 kb from TSS (downstream, strand +1)
> SLC12A7: 138.9 kb from TSS (upstream, strand -1)
> SLC6A3: 150.4 kb from TSS (downstream, strand -1)
> LPCAT1: 229.1 kb from TSS (downstream, strand -1)
> NKD2: 287.1 kb from TSS (downstream, strand +1)
> TRIP13: 402.3 kb from TSS (downstream, strand +1)
> BRD9: 402.3 kb from TSS (upstream, strand -1)

<a id="e03"></a>**E03** ccre_lookup, ENCODE v4 cCRE registry (ENCFF420VPZ) and SCREEN (https://screen-beta-api.wenglab.org/dataws/cre_table; retrieved 2026-10-25T17:25:50+00:00)

> The variant lies in cCRE EH38E3622530 (PLS: promoter-like), chr5:1294945-1295294.
> SCREEN: 3 cCREs within 500 bp (max z-score across ENCODE biosamples):
> EH38E3622530 PLS (contains the variant): DNase z 4.8, H3K27ac z 4.2, H3K4me3 z 4.5, CTCF z 2.0; nearby genes TERT, MIR4457, CLPTM1L
> EH38E3622531 pELS: DNase z 3.9, H3K27ac z 4.3, H3K4me3 z 4.4, CTCF z 2.8; nearby genes TERT, MIR4457, CLPTM1L
> EH38E3622529 pELS: DNase z 3.7, H3K27ac z 4.1, H3K4me3 z 4.6, CTCF z 2.0; nearby genes TERT, MIR4457, CLPTM1L
> Biosample-specific z-scores are not in this call; the values above are maxima over biosamples.

<a id="e04"></a>**E04** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TERT%20AND%20%28%22glioblastoma%22%20OR%20%22melanoma%22%20OR%20%22bladder%22%29&format=json&pageSize=8&resultType=core; retrieved 2026-10-25T11:57:36+00:00)

> Europe PMC: 23888 hits for 'TERT AND ("glioblastoma" OR "melanoma" OR "bladder")'; top 7 with PMIDs:
> PMID 41744838 (2026): Telomerase Activity in Melanoma: Impact on Cancer Cell Proliferation Kinetics, Tumor Progression, and Clinical Therapeutic Strategies-A Scoping Review.
> PMID 42577103 (2026): Familial melanoma: genetic, clinical, and dermoscopic insights and follow-up.
> PMID 42722679 (2026): Developing neoantigen cancer vaccines: where are we now?
> PMID 42741698 (2026): Melanoma of unknown primary with solitary lesions to the prostate and lung uncovered after simple prostatectomy.
> PMID 42804732 (2026): SNP rs2853669 potentially elevates the risk of glioblastoma development and leads to worse prognosis when in cis with mutant TERT promoter in a Japanese cohort.
> PMID 42807929 (2026): USP10 stabilizes FOXM1 through KAT5-mediated acetylation to suppress cell senescence and promote melanoma malignant progression.
> PMID 42859331 (2026): CDKN2A deletion associated with poor prognosis in patients with TERT promoter wild-type, IDH wild-type glioblastoma.

<a id="e04a"></a>**E04a** literature_search, Europe PMC abstract, PMID 41744838 (https://europepmc.org/article/MED/41744838; retrieved 2026-10-25T11:57:36+00:00)

> A major molecular feature of melanoma is abnormal telomerase activation; this is most often caused by telomerase reverse transcriptase (TERT) promoter mutations, which occur in 50-82% of cases and are the most common noncoding alteration in this cancer.

<a id="e04b"></a>**E04b** literature_search, Europe PMC abstract, PMID 41744838 (https://europepmc.org/article/MED/41744838; retrieved 2026-10-25T11:57:36+00:00)

> Understanding both telomere-dependent and -independent TERT functions is essential for developing effective biomarkers and therapies that overcome resistance and slow melanoma progression.

<a id="e04c"></a>**E04c** literature_search, Europe PMC abstract, PMID 42577103 (https://europepmc.org/article/MED/42577103; retrieved 2026-10-25T11:57:36+00:00)

> CDKN2A and CDK4 mutations act through UV-dependent and cell cycle disruption pathways, while BAP1, POT1, and TERT mutations are considered UV-independent.

<a id="e04d"></a>**E04d** literature_search, Europe PMC abstract, PMID 42804732 (https://europepmc.org/article/MED/42804732; retrieved 2026-10-25T11:57:36+00:00)

> Mutations in the telomerase reverse transcriptase (TERT) promoter region (TPM), particularly C228T and C250T, are common in IDH-wildtype glioblastoma (GBM).

<a id="e04e"></a>**E04e** literature_search, Europe PMC abstract, PMID 42804732 (https://europepmc.org/article/MED/42804732; retrieved 2026-10-25T11:57:36+00:00)

> The rs2853669 C allele may increase GBM susceptibility and, when in cis with TPM, is associated with reduced TERT expression and poorer prognosis, underscoring its biological and clinical significance in TPM-mutant GBM.

<a id="e04f"></a>**E04f** literature_search, Europe PMC abstract, PMID 42807929 (https://europepmc.org/article/MED/42807929; retrieved 2026-10-25T11:57:36+00:00)

> Additionally, loss of either USP10 or FOXM1 suppresses the expression of the downstream target Telomerase reverse transcriptase (TERT), triggering cellular senescence.

<a id="e04g"></a>**E04g** literature_search, Europe PMC abstract, PMID 42859331 (https://europepmc.org/article/MED/42859331; retrieved 2026-10-25T11:57:36+00:00)

> TERT promoter (TERTp) mutations are among the most frequent molecular alterations in isocitrate dehydrogenase (IDH) wild-type glioblastoma (GBM), yet the molecular profiles and prognostic implications associated with TERTp status remain incompletely characterized.

<a id="e04h"></a>**E04h** literature_search, Europe PMC abstract, PMID 42859331 (https://europepmc.org/article/MED/42859331; retrieved 2026-10-25T11:57:36+00:00)

> Among 112 patients, 70 (62.5%) harbored TERTp mutations.

<a id="e05"></a>**E05** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-25T17:27:26+00:00)

> 2 ENCODE GABPA ChIP-seq peaks contain chr5:1295135:G>A: biosamples HepG2, SK-N-SH; experiments ENCSR000BJK, ENCSR000BTG.

<a id="e06"></a>**E06** tf_expression, DepMap expression / GTEx v8 medians (local files; retrieved local)

> GABPA in DepMap subtype median Glioblastoma: 15.52 TPM, rank 303 of 1626 TFs (1 = highest); this context is at the 58.4th percentile of GABPA across all DepMap lines; median of 54 lines.

<a id="e07"></a>**E07** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TERT%20promoter%20C250T%20allele-specific%20reporter%20GABPA%20ETS%20binding%20glioblastoma&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T00:28:38+00:00)

> Europe PMC: 14 hits for 'TERT promoter C250T allele-specific reporter GABPA ETS binding glioblastoma'; top 8 with PMIDs:
> PMID 40822359 (2025): AURKB and PI3K/AKT/mTOR pathways converge to regulate &lt;i&gt;TERT&lt;/i&gt; expression.
> PMID 38033865 (2023): Reactivation of telomerase reverse transcriptase expression in cancer: the role of TERT promoter mutations.
> PMID 34944589 (2021): <i>TERT</i> Promoter Mutations Increase Sense and Antisense Transcription from the <i>TERT</i> Promoter.
> PMID 31285550 (2019): Mechanisms underlying the activation of TERT transcription and telomerase activity in human cancer: old actors and new players.
> PMID 33832990 (2021): Interpretation of allele-specific chromatin accessibility using cell state-aware deep learning.
> PMID 31802036 (2020): GABPA is a master regulator of luminal identity and restrains aggressive diseases in bladder cancer.
> PMID 31903880 (2020): Telomere-related Markers for Cancer.
> PMID 26941407 (2016): Understanding TERT Promoter Mutations: A Common Path to Immortality.

<a id="e07a"></a>**E07a** literature_search, Europe PMC abstract, PMID 40822359 (https://europepmc.org/article/MED/40822359; retrieved 2026-10-26T00:28:38+00:00)

> Here, we identified previously uncharacterized pathways regulating TERTp MUT activity by inserting a luciferase reporter downstream of TERTp MUT in SW1736 anaplastic thyroid cancer cells via CRISPR-Cas9, generating SW1736TERT/LUC, and screening a 218-kinase inhibitor library.

<a id="e07b"></a>**E07b** literature_search, Europe PMC abstract, PMID 38033865 (https://europepmc.org/article/MED/38033865; retrieved 2026-10-26T00:28:38+00:00)

> Point mutations in the core promoter region of the telomerase reverse transcriptase (TERT) gene have been found to occur at high frequencies in several tumour types and considered a primary cause of telomerase reactivation in cancer cells.

<a id="e07c"></a>**E07c** literature_search, Europe PMC abstract, PMID 38033865 (https://europepmc.org/article/MED/38033865; retrieved 2026-10-26T00:28:38+00:00)

> These mutations promote TERT gene expression by multiple mechanisms, including the generation of novel binding sites for nuclear transcription factors, displacement of negative regulators from DNA G-quadruplexes, recruitment of epigenetic activators and disruption of long-range interactions between TERT locus and telomeres.

<a id="e07d"></a>**E07d** literature_search, Europe PMC abstract, PMID 34944589 (https://europepmc.org/article/MED/34944589; retrieved 2026-10-26T00:28:38+00:00)

> The two main TERT promoter mutations are C>T transitions located -146C>T and -124C>T upstream from the translational start site.

<a id="e07e"></a>**E07e** literature_search, Europe PMC abstract, PMID 34944589 (https://europepmc.org/article/MED/34944589; retrieved 2026-10-26T00:28:38+00:00)

> They generate a novel Ets/TCF binding site.

<a id="e07f"></a>**E07f** literature_search, Europe PMC abstract, PMID 31285550 (https://europepmc.org/article/MED/31285550; retrieved 2026-10-26T00:28:38+00:00)

> In this review article, we summarize critical mechanisms activating TERT transcription, with special emphases on the contribution of TERT promoter mutations and structural alterations at the TERT locus, and briefly discuss the underlying implications of these genomic events-driven TERT hyperactivity in cancer initiation/progression and potential clinical applications as well.

<a id="e07g"></a>**E07g** literature_search, Europe PMC abstract, PMID 33832990 (https://europepmc.org/article/MED/33832990; retrieved 2026-10-26T00:28:38+00:00)

> We detect hundreds to thousands of allele-specific chromatin accessibility variants (ASCAVs) in each melanoma genome, of which 15%-20% can be explained by gains or losses of transcription factor binding sites.

<a id="e07h"></a>**E07h** literature_search, Europe PMC abstract, PMID 33832990 (https://europepmc.org/article/MED/33832990; retrieved 2026-10-26T00:28:38+00:00)

> Finally, by augmenting the DeepMEL2 model with ChIP-seq data for GABPA, the TERT promoter mutation, as well as additional ETS motif gains, can be identified with high confidence.

<a id="e07i"></a>**E07i** literature_search, Europe PMC abstract, PMID 31802036 (https://europepmc.org/article/MED/31802036; retrieved 2026-10-26T00:28:38+00:00)

> TERT promoter mutations occur in the majority of glioblastoma, bladder cancer (BC), and other malignancies while the ETS family transcription factors GABPA and its partner GABPB1 activate the mutant TERT promoter and telomerase in these tumors.

<a id="e07j"></a>**E07j** literature_search, Europe PMC abstract, PMID 31802036 (https://europepmc.org/article/MED/31802036; retrieved 2026-10-26T00:28:38+00:00)

> GABPA depletion or the disruption of the GABPA/GABPB1 complex by knocking down GABPB1 was shown to inhibit telomerase, thereby eliminating the tumorigenic potential of glioblastoma cells.

<a id="e07k"></a>**E07k** literature_search, Europe PMC abstract, PMID 26941407 (https://europepmc.org/article/MED/26941407; retrieved 2026-10-26T00:28:38+00:00)

> It is becoming clear that TERT mutations occur early during cellular transformation, and activate the TERT promoter by recruiting transcription factors that do not normally regulate TERT gene expression.
