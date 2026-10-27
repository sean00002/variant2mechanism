# TERT promoter C250T and Glioblastoma, melanoma, bladder

Configuration `full`, named mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.04 over 7 model calls; 115 s.

Variant `chr5:1295135:G>A` (somatic); expression context: DepMap:subtype=Glioblastoma (median of 54 lines).

## QBiC-SELEX screen

477 of 997 models pass the gate. Top groups: Ets, 18 models (best ETV5, z 167.5); Ets, 4 models (best ELF3, z 114.84); Ets, 1 model (best SPDEF, z 78.05); MBD; CxxC ZF, 1 model (best MBD1, z -41.31); C2H2 ZF, 1 model (best ZNF654, z -35.62).

## Ranked chains

### 1. H1_GABPA_ETS_activation: GABPA ETS-site gain at the TERT promoter increases TERT (p = 0.44)

TF GABPA (stated coverage own_model; registry own_model), alt allele binds more; element TERT promoter; gene TERT; cell type Glioblastoma.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | GABPA (HGNC symbol GABPA; QBiC-SELEX own model in Ets group G003) is predicted to bind the alt A allele more strongly than the ref G allele. GABPA is a passing own-model member with the same alt-more sign as the group best model ETV5 and is expressed in the glioblastoma DepMap context. ENCODE GABPA ChIP-seq peaks contain chr5:1295135 in HepG2 and SK-N-SH, supporting cellular occupancy at this site, but these peaks do not establish allele specificity, and no glioblastoma GABPA ChIP is provided. | weak | [E05](#e05), [E06](#e06), [E16](#e16) |
| element | The variant lies within the promoter-like cCRE EH38E3622530 and the TERT promoter regulatory feature ENSR5_832QG, so a binding change here can alter a TERT promoter element. | supported | [E01](#e01), [E03](#e03) |
| gene | TERT is the nearest gene at 0.0 kb from its TSS, and the variant is annotated as a TERT upstream_gene_variant in the TERT promoter. | supported | [E01](#e01), [E02](#e02) |
| cell_type | The provided expression context is DepMap glioblastoma; GABPA is expressed in that context, but the available GABPA ChIP peaks are in HepG2 and SK-N-SH, not glioblastoma, so glioblastoma-specific occupancy is not directly shown. | weak | [E05](#e05), [E16](#e16) |
| phenotype | Predicted only: if the alt allele increases GABPA occupancy and GABPA activates TERT, TERT promoter activity and telomerase would increase, favoring TERT-promoter-mutant cancers. No provided evidence directly tests this phenotypic step. | missing | none |

Predictions: Allele-specific GABPA ChIP-qPCR/ddPCR at chr5:1295135 in a heterozygous glioblastoma line will show stronger GABPA occupancy on the alt A allele than the ref G allele.; GABPA depletion or inhibition will reduce TERT expression/telomerase preferentially in alt-allele-carrying glioblastoma cells.; Base editing only chr5:1295135:G>A will change TERT promoter activity in a GABPA-dependent manner.

Falsified if: Allele-specific GABPA ChIP in a heterozygous glioblastoma line does not enrich the alt A allele over ref G at chr5:1295135.; GABPA depletion or inhibition does not reduce TERT expression/telomerase in alt-allele-carrying glioblastoma cells.; Base editing only chr5:1295135:G>A shows no GABPA-dependent change in TERT promoter activity.

### 2. H5_null: No TF-mediated effect of this variant (p = 0.36)

Null chain: no TF-mediated effect of this variant.

Predictions: No named TF will show reproducible allele-specific binding at chr5:1295135 in relevant cells beyond in vitro motif predictions.; Editing only this base will not change TERT promoter activity; any signal will track a linked variant or broader haplotype.; The variant will behave as a passenger or hotspot-associated change without a direct TF-mediated allelic effect.

Falsified if: Allele-specific ChIP or a reporter/base-editing assay shows a reproducible TF-dependent difference between ref and alt at this base.; CRISPR base editing of only chr5:1295135 changes TERT expression in relevant cells.; A linked causal variant is excluded and the alt allele itself has a direct functional effect.

### 3. H2_ETV5_ETS_activation: ETV5 ETS-site gain at the TERT promoter increases TERT (p = 0.09)

TF ETV5 (stated coverage own_model; registry own_model), alt allele binds more; element TERT promoter; gene TERT; cell type Glioblastoma.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | ETV5 (HGNC symbol ETV5; QBiC-SELEX own model in Ets group G003) is the best model in the shared Ets group and is predicted to bind the alt A allele more strongly than ref G (z 167.5, effect +2.421). ETV5 is expressed in the glioblastoma DepMap context, but no ENCODE ETV5 ChIP-seq peak containing chr5:1295135 is provided, so cellular occupancy is not supported. | weak | [E05](#e05), [E06](#e06), [E17](#e17) |
| element | The variant lies within the TERT promoter-like cCRE EH38E3622530, so an ETV5 binding change here could in principle alter promoter activity. | supported | [E01](#e01), [E03](#e03) |
| gene | TERT is 0.0 kb from its TSS and the variant is a TERT upstream_gene_variant, assigning the element to TERT. | supported | [E01](#e01), [E02](#e02) |
| cell_type | ETV5 is expressed in the DepMap glioblastoma context, but direct glioblastoma ETV5 ChIP at this site is not provided. | weak | [E05](#e05), [E06](#e06) |
| phenotype | Predicted only: if ETV5 gains binding on the alt allele and activates TERT, TERT expression and telomerase would increase. No provided evidence directly tests this phenotypic step. | missing | none |

Predictions: ETV5 ChIP-qPCR at chr5:1295135 in relevant cells will show ETV5 occupancy and stronger binding on the alt allele.; ETV5 knockdown will reduce TERT expression preferentially in alt-allele-carrying cells.; The ETV5 motif model will fit the alt allele better than the ref allele.

Falsified if: ETV5 ChIP in relevant cells does not occupy chr5:1295135 or does not show alt-specific binding.; ETV5 depletion does not affect TERT expression/telomerase in alt-allele-carrying cells.; GABPA or another Ets factor fully explains allele-specific occupancy at this site.

### 4. H3_ELF1_ETS_activation: ELF1 ETS-site gain at the TERT promoter increases TERT (p = 0.08)

TF ELF1 (stated coverage own_model; registry own_model), alt allele binds more; element TERT promoter; gene TERT; cell type Glioblastoma.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | ELF1 (HGNC symbol ELF1; QBiC-SELEX own model in Ets group G003) is a passing member of the same alt-more Ets group as ETV5 and is expressed in the glioblastoma DepMap context. This is an in vitro binding prediction; no ELF1 ChIP at this site is provided. | weak | [E05](#e05), [E06](#e06) |
| element | The variant lies within the TERT promoter-like cCRE EH38E3622530, so an ELF1 binding change here could alter promoter activity. | supported | [E01](#e01), [E03](#e03) |
| gene | TERT is 0.0 kb from its TSS and the variant is a TERT upstream_gene_variant, assigning the element to TERT. | supported | [E01](#e01), [E02](#e02) |
| cell_type | ELF1 is expressed in the DepMap glioblastoma context, but direct glioblastoma ELF1 ChIP at this site is not provided. | weak | [E05](#e05), [E06](#e06) |
| phenotype | Predicted only: if ELF1 gains binding on the alt allele and activates TERT, TERT expression and telomerase would increase. No provided evidence directly tests this phenotypic step. | missing | none |

Predictions: ELF1 ChIP-qPCR at chr5:1295135 in relevant cells will show ELF1 occupancy and stronger binding on the alt allele.; ELF1 knockdown will reduce TERT expression preferentially in alt-allele-carrying cells.; ELF1 binding at the TERT promoter will be allele-specific in a reporter assay.

Falsified if: ELF1 ChIP at chr5:1295135 does not show alt-specific occupancy.; ELF1 depletion does not affect TERT expression/telomerase in relevant cells.; The allele-specific Ets occupancy is better explained by GABPA or ETV5.

### 5. H4_MBD1_repressor_loss: MBD1 repressor-site loss at the TERT promoter increases TERT (p = 0.03)

TF MBD1 (stated coverage own_model; registry own_model), ref allele binds more; element TERT promoter; gene TERT; cell type Glioblastoma.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | MBD1 (HGNC symbol MBD1; QBiC-SELEX own model, group G229) is predicted to bind the ref G allele more strongly than the alt A allele (z -41.31, effect -1.236). MBD1 is expressed in the glioblastoma DepMap context, but no ENCODE MBD1 ChIP-seq peak containing chr5:1295135 is provided, so cellular occupancy is not supported. | weak | [E05](#e05), [E09](#e09), [E18](#e18) |
| element | The variant lies within the TERT promoter-like cCRE EH38E3622530, so loss of a repressive factor here could in principle alter promoter activity. | supported | [E01](#e01), [E03](#e03) |
| gene | TERT is 0.0 kb from its TSS and the variant is a TERT upstream_gene_variant, assigning the element to TERT. | supported | [E01](#e01), [E02](#e02) |
| cell_type | MBD1 is expressed in the DepMap glioblastoma context, but direct glioblastoma MBD1 ChIP at this site is not provided. | weak | [E05](#e05), [E09](#e09) |
| phenotype | Predicted only: if MBD1 represses TERT and loses binding on the alt allele, TERT expression and telomerase would increase. No provided evidence directly tests MBD1 repression at this promoter or this phenotypic step. | missing | none |

Predictions: MBD1 ChIP-qPCR at chr5:1295135 will show stronger MBD1 occupancy on the ref G allele than the alt A allele.; MBD1 depletion will increase TERT expression in cells carrying the ref allele or blunt the alt-vs-ref difference.; The alt allele will reduce an MBD1-associated repressive chromatin signature at the TERT promoter.

Falsified if: MBD1 ChIP at chr5:1295135 does not show stronger binding on the ref G allele than the alt A allele.; MBD1 depletion does not increase TERT expression or does so independently of this allele.; The alt allele increases TERT by gaining an activator site rather than by losing a repressor site.

## Prediction matrix

| Test | Cost | Separates top two | H1_GABPA_ETS_activation | H5_null | H2_ETV5_ETS_activation | H3_ELF1_ETS_activation | H4_MBD1_repressor_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Allele-specific GABPA ChIP-qPCR/ddPCR at chr5:1295135 in a heterozygous glioblastoma line | medium | yes | GABPA occupancy is higher on the alt A allele than the ref G allele at chr5:1295135. | No reproducible allele-specific binding by GABPA or any named TF at this base. | No GABPA allele-specific enrichment; if anything, ETV5 rather than GABPA would carry the allelic effect. | No GABPA allele-specific enrichment; ELF1 would be the predicted allele-specific factor. | No GABPA allele-specific enrichment; MBD1 would be predicted to prefer the ref allele. |
| ETV5 ChIP-qPCR at chr5:1295135 in glioblastoma cells | medium | no | No ETV5 occupancy or no alt-specific ETV5 binding at the variant. | No allele-specific ETV5 binding at this base. | ETV5 occupies chr5:1295135 and binds the alt allele more strongly than ref. | No ETV5 allele-specific enrichment; ELF1 would be the predicted factor. | No ETV5 allele-specific enrichment; MBD1 would be predicted to prefer ref. |
| ELF1 ChIP-qPCR at chr5:1295135 in glioblastoma cells | medium | no | No ELF1 allele-specific enrichment; GABPA remains the preferred Ets factor. | No allele-specific ELF1 binding at this base. | No ELF1 allele-specific enrichment; ETV5 remains the preferred Ets factor. | ELF1 occupies chr5:1295135 and binds the alt allele more strongly than ref. | No ELF1 allele-specific enrichment; MBD1 would be predicted to prefer ref. |
| MBD1 ChIP-qPCR at chr5:1295135 in glioblastoma cells | medium | no | No MBD1 ref-allele enrichment; GABPA activation remains the preferred model. | No allele-specific MBD1 binding at this base. | No MBD1 ref-allele enrichment; ETV5 activation remains possible. | No MBD1 ref-allele enrichment; ELF1 activation remains possible. | MBD1 occupies chr5:1295135 and binds the ref G allele more strongly than the alt A allele. |
| CRISPR base editing of only chr5:1295135:G>A in a heterozygous glioblastoma line, then measure TERT expression/telomerase | high | yes | Base editing only C250T increases TERT promoter activity/telomerase in a GABPA-dependent way. | Base editing only C250T does not change TERT promoter activity/telomerase; any signal tracks a linked variant or haplotype. | Base editing only C250T increases TERT promoter activity/telomerase in an ETV5-dependent way. | Base editing only C250T increases TERT promoter activity/telomerase in an ELF1-dependent way. | Base editing only C250T increases TERT promoter activity/telomerase by relieving MBD1 repression. |

## Next experiment

GABPA allele-specific ChIP-qPCR or ChIP-ddPCR at chr5:1295135 in a heterozygous glioblastoma cell line, comparing GABPA occupancy on the alt A allele versus the ref G allele; cost medium. This directly separates the top chain H1_GABPA_ETS_activation (alt > ref GABPA occupancy) from H5_null (no named-TF allele-specific binding).

## Investigate calls

- chip_peaks({"biosample": null, "tf": "GABPA"})
- chip_peaks({"biosample": null, "tf": "ETV5"})
- chip_peaks({"biosample": null, "tf": "MBD1"})

## Flags

- quote_rejected: PMID 41744838: not an exact substring of the abstract

Citation support: 0.80 of links cite only evidence that passed every check.

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

<a id="e05"></a>**E05** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> QBiC-SELEX screen of chr5:1295135:G>A: 997 models scored, 477 pass the gate (Bonferroni 0.05/997, p < 5.02e-05, |z| > 4.05), in 350 CIS-BP groups. Expression context: DepMap subtype median Glioblastoma. Groups shown: 10; dropped because no TF in the group reaches 1 TPM: 77 (C2H2 ZF, 1 model z -27.15, C2H2 ZF, 1 model z -21.76, bHLH, 1 model z -21.51, Homeodomain, 1 model z -19.2, Myb/SANT, 1 model z -18.88). Passing groups ranked below the ones shown: 263. In the group rows, 'own model' means the TF has its own QBiC-SELEX model and 'mapped' that it is covered only through CIS-BP-mapped models of related TFs. A TF not named in any group row may still have its own model, even one that passes the gate: look it up with qbic_tf_detail before stating its coverage or a QBiC-SELEX direction for it. predicted_effect > 0 means the alternate allele binds more strongly. In vitro binding only: expression and chromatin decide whether a change matters.

<a id="e06"></a>**E06** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G003 (Ets, 18 models): best model ETV5_NA_TGCACT20NGA_ESAF_yang2017_1_3_6mer (own model of ETV5), z 167.5, effect 2.421 (alt binds more); 18 passing models (18 with the best model's sign). Passing members: ETV5 z 167.5, ELF1 z 164.23, ELF4 z 110.16, GABPA z 71.32, ELK4 z 62.15 (+13 more). TFs this group covers: ETS1 (own model) 61.01 TPM, ERF (own model) 39.81 TPM, ELK3 (own model) 30.24 TPM, ELK1 (own model) 26.81 TPM, ETV5 (own model) 22.15 TPM, ETS2 (own model) 21.07 TPM, ELF2 (own model) 18.42 TPM, ELF1 (own model) 17.41 TPM, GABPA (own model) 15.52 TPM, ELF4 (own model) 15.44 TPM (+15 more); best model's site strength: ref 94.8th, alt 99.9th percentile of its k-mer coefficients.

<a id="e07"></a>**E07** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G020 (Ets, 4 models): best model ELF3_NA_TCCGTG20NTGC_ESY_yang2017_0_4_7mer (own model of ELF3), z 114.84, effect 5.168 (alt binds more); 4 passing models (4 with the best model's sign). Passing members: ELF3 z 114.84, ELF5 z 107.44, ETV7 z 49.98, ETV6 z 46.24. TFs this group covers: ERF (own model) 39.81 TPM, ELF2 (own model) 18.42 TPM, ELF1 (own model) 17.41 TPM, ELF4 (own model) 15.44 TPM, ETV6 (own model) 5.65 TPM, ELF3 (own model) 0.47 TPM, ETV7 (own model) 0.31 TPM, EHF (mapped) 0.17 TPM, SPI1 (own model) 0.05 TPM, ELF5 (own model) 0.03 TPM (+1 more); best model's site strength: ref 99.3th, alt 100.0th percentile of its k-mer coefficients.

<a id="e08"></a>**E08** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G345 (Ets, 1 model): best model SPDEF_NA_TCATTG20NCG_ESAD_yang2017_0_3_7mer (own model of SPDEF), z 78.05, effect 2.184 (alt binds more); 1 passing models (1 with the best model's sign). Passing members: SPDEF z 78.05. TFs this group covers: ELF2 (own model) 18.42 TPM, ELF1 (own model) 17.41 TPM, ELF4 (own model) 15.44 TPM, SPDEF (own model) 0.05 TPM; best model's site strength: ref 99.2th, alt 100.0th percentile of its k-mer coefficients.

<a id="e09"></a>**E09** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G229 (MBD; CxxC ZF, 1 model): best model MBD1_FL_TG40NTGATCT_YWQA_jolma2025_0_3_7mer (own model of MBD1), z -41.31, effect -1.236 (alt binds less); 1 passing models (1 with the best model's sign). Passing members: MBD1 z -41.31. TFs this group covers: MBD1 (own model) 31.48 TPM; best model's site strength: ref 100.0th, alt 98.6th percentile of its k-mer coefficients.

<a id="e10"></a>**E10** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G557 (C2H2 ZF, 1 model): best model ZNF654_DBD_AG40NTGGCTA_YWIA_jolma2025_0_4_7mer (own model of ZNF654), z -35.62, effect -0.857 (alt binds less); 1 passing models (1 with the best model's sign). Passing members: ZNF654 z -35.62. TFs this group covers: ZNF654 (own model) 6.42 TPM; best model's site strength: ref 100.0th, alt 99.1th percentile of its k-mer coefficients.

<a id="e11"></a>**E11** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G620 (C2H2 ZF, 1 model): best model ZNF92_FL_TC40NAATCTC_YWIA_jolma2025_0_3_7mer (own model of ZNF92), z -33.21, effect -0.623 (alt binds less); 1 passing models (1 with the best model's sign). Passing members: ZNF92 z -33.21. TFs this group covers: ZNF92 (own model) 9.63 TPM; best model's site strength: ref 100.0th, alt 99.7th percentile of its k-mer coefficients.

<a id="e12"></a>**E12** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G409 (C2H2 ZF, 1 model): best model ZBTB5_FL_GA40NACTTTG_YWQA_jolma2025_0_2_7mer (own model of ZBTB5), z -24.38, effect -0.68 (alt binds less); 1 passing models (1 with the best model's sign). Passing members: ZBTB5 z -24.38. TFs this group covers: ZBTB5 (own model) 7.43 TPM; best model's site strength: ref 100.0th, alt 99.5th percentile of its k-mer coefficients.

<a id="e13"></a>**E13** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G066 (EBF1, 2 models): best model EBF1_NA_TATAAG20NCG_AC_jolma2013_1_3_7mer (own model of EBF1), z -24.35, effect -0.646 (alt binds less); 1 passing models (1 with the best model's sign). Passing members: EBF1 z -24.35. TFs this group covers: EBF1 (own model) 3.13 TPM, EBF4 (own model) 2.58 TPM, EBF2 (mapped) 0.02 TPM, EBF3 (mapped) 0.01 TPM; best model's site strength: ref 99.9th, alt 99.7th percentile of its k-mer coefficients.

<a id="e14"></a>**E14** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G612 (C2H2 ZF, 1 model): best model ZNF845_DBD2_GC40NAGAGTT_YWIA_jolma2025_0_3_7mer (own model of ZNF845), z -24.25, effect -0.358 (alt binds less); 1 passing models (1 with the best model's sign). Passing members: ZNF845 z -24.25. TFs this group covers: ZNF845 (own model) 3.41 TPM; best model's site strength: ref 100.0th, alt 99.2th percentile of its k-mer coefficients.

<a id="e15"></a>**E15** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G575 (C2H2 ZF, 1 model): best model ZNF706_FL_CT40NTCTAGT_YWSA_jolma2025_0_3_7mer (own model of ZNF706), z -23.53, effect -0.618 (alt binds less); 1 passing models (1 with the best model's sign). Passing members: ZNF706 z -23.53. TFs this group covers: ZNF706 (own model) 81.43 TPM; best model's site strength: ref 100.0th, alt 99.4th percentile of its k-mer coefficients.

<a id="e16"></a>**E16** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-25T17:27:26+00:00)

> 2 ENCODE GABPA ChIP-seq peaks contain chr5:1295135:G>A: biosamples HepG2, SK-N-SH; experiments ENCSR000BJK, ENCSR000BTG.

<a id="e17"></a>**E17** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-26T00:38:43+00:00)

> No ENCODE ETV5 ChIP-seq peak contains chr5:1295135:G>A. Absence can also mean no ETV5 experiment in that biosample. 0 peaks lie within 100 bp without containing it.

<a id="e18"></a>**E18** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-26T01:44:17+00:00)

> No ENCODE MBD1 ChIP-seq peak contains chr5:1295135:G>A. Absence can also mean no MBD1 experiment in that biosample. 0 peaks lie within 100 bp without containing it.
