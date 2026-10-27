# rs4784227 and Breast cancer (16q12)

Configuration `full`, named mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.02 over 7 model calls; 247 s.

Variant `chr16:52565276:C>T` (germline); expression context: DepMap:ACH-000019 (MCF7).

## QBiC-SELEX screen

290 of 997 models pass the gate. Top groups: bZIP, 6 models (best MAFG, z 71.57); C2H2 ZF, 1 model (best ZNF134, z 37.4); Homeodomain, 81 models (best LHX8, z 28.05); Rel, 4 models (best NFATC4, z -23.46); Homeodomain; POU, 1 model (best POU2F1, z 22.8).

## Ranked chains

### 1. H3: GATA3 binds the risk allele more strongly at the TOX3 enhancer (p = 0.37)

TF GATA3 (stated coverage own_model; registry own_model), alt allele binds more; element EH38E3180851; gene TOX3; cell type MCF7 breast cancer line.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | GATA3 binds the alt T allele of rs4784227 more strongly than the ref C allele in vitro: in QBiC-SELEX group G010 (GATA family), GATA3 has its own passing model with the same positive sign as the group best model (GATA3 z 10.91, effect +0.283, alt binds more). I choose GATA3 within the GATA family because it is by far the highest-expressed GATA member in MCF7 (346.04 TPM) and because 5 ENCODE GATA3 ChIP-seq peaks in MCF7 contain the variant (E20), establishing GATA3 occupancy at this element in the case cell type, although not allele specificity. | weak | [E17](#e17), [E07](#e07), [E20](#e20) |
| element | rs4784227 lies in the dELS EH38E3180851 / ENSR16_9QTBS enhancer with active chromatin marks, so allele-specific GATA3 binding could change enhancer activity; the site is not conserved (GERP -2). | supported | [E01](#e01), [E03](#e03) |
| gene | The element is best linked to TOX3: TOX3 is the nearest protein-coding gene and the top Open Targets L2G target (0.92-0.96) in breast cancer credible sets. | supported | [E02](#e02), [E05](#e05) |
| cell_type | MCF7 is a luminal breast cancer line with very high GATA3 expression (346.04 TPM), and GATA3 ChIP-seq peaks in MCF7 contain the variant, making GATA3 occupancy at this enhancer in this cell type directly supported. The cCRE annotation itself is ENCODE-wide rather than MCF7-specific. | supported | [E07](#e07), [E17](#e17), [E03](#e03), [E20](#e20) |
| phenotype | The strongest breast cancer GWAS associations list T as the risk allele, and GATA3 is a breast cancer lineage factor. If GATA3 binding at T changes TOX3 enhancer output, this could contribute to breast cancer risk; the direction of TOX3 change is not established by SELEX or by occupancy alone. | weak | [E04](#e04), [E05](#e05) |

Predictions: GATA3 ChIP in MCF7 will show occupancy at rs4784227 (already supported by E20) and allele-specific GATA3 ChIP will show stronger occupancy on the T allele than on the C allele.; GATA3 knockdown or CRISPRi will alter rs4784227 enhancer activity and/or TOX3 expression in MCF7.; The allele-specific GATA3 effect will be stronger in GATA3-high breast cancer cells than in GATA3-low cells.

Falsified if: GATA3 does not occupy the rs4784227 element in MCF7, contrary to the E20 ChIP peaks.; GATA3 binding is not allele-specific, or the T allele binds less GATA3.; GATA3 knockdown does not affect the enhancer or TOX3.

### 2. H5: Null: no TF-mediated allele-specific effect of rs4784227 (p = 0.31)

Null chain: no TF-mediated effect of this variant.

Predictions: No allele-specific TF occupancy at rs4784227 in breast cancer cells; GATA3 may occupy the element, as E20 shows, but equally on both alleles.; The rs4784227-containing enhancer has no allele-dependent reporter activity, or any allele effect is not mediated by the TFs tested here.; The breast cancer association is explained by a linked causal variant in LD, or rs4784227 is a passenger in a locus where another variant drives the effect.

Falsified if: Allele-specific ChIP or reporter assays show that rs4784227 itself changes enhancer activity.; A specific TF shows allele-specific binding at rs4784227 and knockdown of that TF changes TOX3 expression or enhancer output.; Fine-mapping excludes linked variants and leaves rs4784227 as the functional variant.

### 3. H1: MAFG binds the risk allele more strongly at the TOX3 enhancer (p = 0.13)

TF MAFG (stated coverage own_model; registry own_model), alt allele binds more; element EH38E3180851; gene TOX3; cell type MCF7 breast cancer line.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | MAFG binds the alt T allele of rs4784227 more strongly than the ref C allele in vitro: in QBiC-SELEX group G012, the MAFG own model is the best model (z 71.57, effect +2.788, alt binds more; site strength ref 97.6th to alt 100.0th percentile). I choose MAFG within the shared bZIP group because it has the strongest own-model signal in the group and is expressed in MCF7 (8.48 TPM), but no MAFG ChIP-seq peak in MCF7 contains the variant (E18; absence can also mean no MAFG experiment in that biosample). Thus the cellular occupancy claim is not established. | weak | [E08](#e08), [E07](#e07), [E18](#e18) |
| element | rs4784227 lies in the distal enhancer-like cCRE EH38E3180851 / ENSR16_9QTBS enhancer (dELS; DNase z 4.2, H3K27ac z 6.1), so allele-specific MAFG binding could alter enhancer activity. The site is not deeply conserved (GERP -2), so the enhancer annotation rather than conservation carries this part of the claim. | supported | [E01](#e01), [E03](#e03) |
| gene | The variant-bearing enhancer is most plausibly linked to TOX3: TOX3 is the nearest protein-coding gene at 17.5 kb, and Open Targets L2G assigns TOX3 0.92-0.96 in breast cancer credible sets. CASC16 is also at the locus, but the strongest L2G target is TOX3. | supported | [E02](#e02), [E05](#e05) |
| cell_type | MCF7 is the supplied breast cancer expression context, MAFG is expressed there at 8.48 TPM, and the element is an ENCODE dELS. However, the cCRE z-scores are maxima over ENCODE biosamples, and no MCF7 MAFG ChIP peak at the variant is reported. | weak | [E07](#e07), [E08](#e08), [E03](#e03), [E18](#e18) |
| phenotype | The strongest breast cancer GWAS associations list T as the risk allele at this locus, and GWAS/L2G evidence connects the locus to TOX3. If MAFG occupancy at the T allele changes TOX3 enhancer output, this is a candidate route to breast cancer risk; SELEX alone does not establish whether MAFG activates or represses the enhancer. | weak | [E04](#e04), [E05](#e05) |

Predictions: MAFG ChIP in MCF7 or breast epithelial cells will show occupancy at rs4784227 and stronger MAFG signal on the T allele than on the C allele, despite the current absence of an ENCODE MCF7 MAFG peak.; MAFG knockdown or overexpression will change activity of the rs4784227 enhancer reporter and/or TOX3 expression in a TOX3-linked manner.; GATA3 will occupy this element in MCF7 but MAFG, not GATA3, will be the allele-specific factor at rs4784227.

Falsified if: MAFG does not occupy the rs4784227 element in breast cancer cells.; Allele-specific MAFG binding is absent or opposite to the QBiC-SELEX prediction.; The rs4784227 element has no allele-dependent enhancer activity and no effect on TOX3 in a relevant cell type.

### 4. H2: MAFK is the expressed bZIP factor whose binding is altered (p = 0.11)

TF MAFK (stated coverage own_model; registry own_model), alt allele binds more; element EH38E3180851; gene TOX3; cell type MCF7 breast cancer line.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | MAFK binds the alt T allele of rs4784227 more strongly than the ref C allele in vitro: in QBiC-SELEX group G012, MAFK has its own passing model with the same positive sign as the group best model (MAFK z 48.84, alt binds more). I choose MAFK within the shared bZIP group because it is the highest-expressed group member in MCF7 (16.96 TPM). No MAFK ChIP-seq peak in MCF7 contains the variant; one MAFK peak in HepG2 does (E19). | weak | [E08](#e08), [E07](#e07), [E19](#e19) |
| element | The variant sits in the distal enhancer-like cCRE EH38E3180851 / ENSR16_9QTBS enhancer (dELS; DNase z 4.2, H3K27ac z 6.1), so an allele-specific MAFK binding change could affect enhancer activity; the site is not conserved (GERP -2). | supported | [E01](#e01), [E03](#e03) |
| gene | The enhancer's best-supported target is TOX3: TOX3 is 17.5 kb away and is the top Open Targets L2G gene (0.92-0.96) across breast cancer credible sets. | supported | [E02](#e02), [E05](#e05) |
| cell_type | MCF7 is a breast cancer expression context in which MAFK is well expressed (16.96 TPM), and the element is annotated as a dELS. The ENCODE cCRE z-scores are not MCF7-specific, and the only reported MAFK ChIP peak containing the variant is in HepG2, not MCF7. | weak | [E07](#e07), [E08](#e08), [E03](#e03), [E19](#e19) |
| phenotype | The strongest breast cancer GWAS associations list T as the risk allele, and the locus is linked to TOX3. If MAFK binding at the T allele alters TOX3 enhancer output, this could contribute to breast cancer risk; the SELEX data do not determine activation versus repression. | weak | [E04](#e04), [E05](#e05) |

Predictions: MAFK ChIP in MCF7 or breast cells will show allele-specific occupancy at rs4784227, stronger on T.; MAFK knockdown will alter the rs4784227 enhancer reporter or TOX3 expression, while MAFG knockdown will have little effect at this site.; The MAFK effect will be detectable in a cell type where MAFK is the dominant small MAF at this element.

Falsified if: MAFK does not occupy the locus or shows no allele-specific binding.; MAFG, not MAFK, is the factor whose knockdown changes enhancer activity or TOX3 expression.; The element has no allele-dependent activity in breast cancer cells.

### 5. H4: NFATC3 represses the enhancer and the risk allele reduces its binding (p = 0.08)

TF NFATC3 (stated coverage own_model; registry own_model), ref allele binds more; element EH38E3180851; gene TOX3; cell type MCF7 breast cancer line.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | NFATC3 binds the ref C allele more strongly than the alt T allele in vitro: in QBiC-SELEX group G026 (Rel family), NFATC3 has its own passing model with the group's negative sign (NFATC3 z -4.28, alt binds less). I choose NFATC3 within the Rel group because it is the highest-expressed Rel member in MCF7 (9.54 TPM). No NFATC3 ChIP evidence at this variant is supplied, and the NFATC3 SELEX signal is near the gate. | weak | [E11](#e11), [E07](#e07) |
| element | The variant is in the dELS EH38E3180851 / ENSR16_9QTBS enhancer, so allele-specific NFATC3 occupancy could modulate enhancer activity; the element is annotated as active chromatin but the site itself is not conserved (GERP -2). | supported | [E01](#e01), [E03](#e03) |
| gene | The enhancer is best linked to TOX3 by proximity and by Open Targets L2G (TOX3 0.92-0.96). | supported | [E02](#e02), [E05](#e05) |
| cell_type | MCF7 expresses NFATC3 at 9.54 TPM, higher than NFATC2 and NFATC4, so NFATC3 is the most plausible Rel family member in this expression context; the ENCODE cCRE z-scores are not MCF7-specific, and no NFATC3 ChIP at the variant is supplied. | weak | [E07](#e07), [E11](#e11), [E03](#e03) |
| phenotype | The strongest breast cancer GWAS associations list T as the risk allele. If NFATC3 represses the TOX3 enhancer, then the risk T allele's lower NFATC3 binding would derepress TOX3; this is a distinct direction of TOX3 change from the activator models. The repressor/derepression assumption is not directly supported. | weak | [E04](#e04), [E05](#e05) |

Predictions: NFATC3 ChIP will show stronger binding on the C allele than on the T allele at rs4784227.; NFATC3 knockdown will increase rs4784227 enhancer activity and/or TOX3 expression if NFATC3 is repressive.; The effect will be seen in MCF7 or other breast cells with detectable NFATC3.

Falsified if: NFATC3 does not occupy the locus in breast cancer cells.; NFATC3 binds the T allele more strongly, opposite to the QBiC-SELEX sign.; NFATC3 knockdown does not change enhancer activity or TOX3 expression.

## Prediction matrix

| Test | Cost | Separates top two | H3 | H5 | H1 | H2 | H4 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| GATA3 ChIP-qPCR at rs4784227 in MCF7 (occupancy only, no allele discrimination) | low | no | Strong GATA3 occupancy at the element, consistent with E20. | GATA3 may occupy the element, but equally on both alleles and without functional consequence. | GATA3 may occupy the element, but MAFG is the functional allele-specific factor; GATA3 occupancy is not the mechanism. | GATA3 may occupy the element, but MAFK is the functional allele-specific factor. | GATA3 may occupy the element, but NFATC3 is the functional allele-specific factor. |
| Allele-specific GATA3 ChIP in MCF7 (ChIP-BS or ChIP-qPCR with Sanger/allelic discrimination at rs4784227) | medium | yes | GATA3 occupancy is higher on the T allele than on the C allele. | No allele-specific GATA3 occupancy; occupancy, if present, is equal on C and T. | No T>C allele-specific GATA3 occupancy; MAFG, not GATA3, carries the allele effect. | No T>C allele-specific GATA3 occupancy; MAFK carries the allele effect. | No T>C allele-specific GATA3 occupancy; NFATC3 carries the opposite allele effect. |
| MAFG ChIP-qPCR at rs4784227 in MCF7 | low | no | Little or no allele-specific MAFG occupancy; GATA3 is the functional factor. | MAFG may occupy but without allele specificity or functional consequence. | MAFG occupies the element and binding is stronger on the T allele. | Little or no MAFG occupancy; MAFK is the functional bZIP factor. | Little or no allele-specific MAFG occupancy; NFATC3 is the functional factor. |
| MAFK ChIP-qPCR at rs4784227 in MCF7 | low | no | Little or no allele-specific MAFK occupancy; GATA3 is the functional factor. | MAFK may occupy but without allele specificity or functional consequence. | Little or no MAFK occupancy; MAFG is the functional bZIP factor. | MAFK occupies the element and binding is stronger on the T allele. | Little or no allele-specific MAFK occupancy; NFATC3 is the functional factor. |
| NFATC3 ChIP-qPCR at rs4784227 in MCF7 | low | no | Little or no allele-specific NFATC3 occupancy; GATA3 carries the allele effect. | No allele-specific NFATC3 occupancy or functional consequence. | Little or no allele-specific NFATC3 occupancy; MAFG carries the allele effect. | Little or no allele-specific NFATC3 occupancy; MAFK carries the allele effect. | NFATC3 occupies the element more strongly on the C allele than on the T allele. |
| Allele-specific enhancer reporter or MPRA with C vs T at rs4784227 in MCF7 or GATA3-high breast cancer cells | medium | yes | Allele-dependent enhancer activity, with the T allele changing output in a GATA3-dependent manner. | No allele-dependent enhancer activity for C vs T. | Allele-dependent enhancer activity in a MAFG-dependent manner; T allele changes output if MAFG is the relevant factor. | Allele-dependent enhancer activity in a MAFK-dependent manner; T allele changes output if MAFK is the relevant factor. | Allele-dependent enhancer activity, with the C allele changing output if NFATC3 is the repressive factor. |
| GATA3 knockdown or CRISPRi in MCF7 with rs4784227 enhancer activity and TOX3 expression readouts | medium | yes | GATA3 loss changes rs4784227 enhancer activity and/or TOX3 expression. | No GATA3-specific effect at this element; any TOX3 change is not mediated by rs4784227 allele-specific GATA3 binding. | No GATA3-specific effect on the rs4784227 enhancer or TOX3; MAFG-dependent effect if any. | No GATA3-specific effect on the rs4784227 enhancer or TOX3; MAFK-dependent effect if any. | No GATA3-specific effect; NFATC3-dependent derepression if any. |
| High-resolution fine-mapping/LD analysis to identify a linked causal variant at 16q12 | high | yes | rs4784227 remains the best functional candidate for GATA3 binding, not a linked variant. | A linked variant explains the association better than rs4784227 itself. | rs4784227 remains the best functional candidate for MAFG binding, not a linked variant. | rs4784227 remains the best functional candidate for MAFK binding, not a linked variant. | rs4784227 remains the best functional candidate for NFATC3 binding, not a linked variant. |

## Next experiment

Allele-specific GATA3 ChIP in MCF7 (ChIP-BS or ChIP-qPCR with Sanger/allelic discrimination at rs4784227), cost medium. It directly separates the top two chains, H3 and H5: H3 predicts stronger GATA3 occupancy on the T allele than on the C allele, while H5 predicts no allele-specific GATA3 occupancy even though GATA3 may occupy the element equally on both alleles. It is cheaper than reporter/perturbation or fine-mapping and is feasible because E20 already shows GATA3 ChIP peaks in MCF7 containing this variant.

## Investigate calls

- chip_peaks({"tf": "MAFG", "biosample": "MCF7"})
- chip_peaks({"tf": "MAFK", "biosample": "MCF7"})
- chip_peaks({"tf": "GATA3", "biosample": "MCF7"})

## Flags

- quote_rejected: PMID 41230718: not an exact substring of the abstract

Citation support: 1.00 of links cite only evidence that passed every check.

## Evidence

<a id="e01"></a>**E01** variant_annotation, Ensembl VEP (GRCh38) (https://rest.ensembl.org/vep/human/region/16:52565276-52565276:1/T?content-type=application/json&Conservation=1; retrieved 2026-10-25T17:26:24+00:00)

> Variant chr16:52565276:C>T (GRCh38), allele string C/T
> Known IDs: rs4784227
> Most severe consequence: intron_variant
> Regulatory features: ENSR16_9QTBS enhancer
> GERP conservation score at the site: -2
> Transcript consequences: CASC16 (intron_variant, non_coding_transcript_variant)

<a id="e02"></a>**E02** nearest_genes, Ensembl overlap (protein_coding) (https://rest.ensembl.org/overlap/region/human/16:51565276-53565276?feature=gene;biotype=protein_coding;content-type=application/json; retrieved 2026-10-25T17:25:47+00:00)

> 6 protein-coding genes within 1000 kb of chr16:52565276:C>T, by distance to TSS:
> TOX3: 17.5 kb from TSS (upstream, strand -1)
> CHD9NB: 487.6 kb from TSS (downstream, strand -1)
> CHD9: 489.7 kb from TSS (upstream, strand +1)
> RBL2: 868.7 kb from TSS (upstream, strand +1)
> AKTIP: 939.1 kb from TSS (downstream, strand -1)
> HNRNPA1L3: 1011.8 kb from TSS (downstream, strand +1)

<a id="e03"></a>**E03** ccre_lookup, ENCODE v4 cCRE registry (ENCFF420VPZ) and SCREEN (https://screen-beta-api.wenglab.org/dataws/cre_table; retrieved 2026-10-25T17:25:50+00:00)

> The variant lies in cCRE EH38E3180851 (dELS: distal enhancer-like), chr16:52565011-52565360.
> SCREEN: 1 cCREs within 500 bp (max z-score across ENCODE biosamples):
> EH38E3180851 dELS (contains the variant): DNase z 4.2, H3K27ac z 6.1, H3K4me3 z 1.8, CTCF z 1.9; nearby genes CASC16, TOX3, AC026462.5
> Biosample-specific z-scores are not in this call; the values above are maxima over biosamples.

<a id="e04"></a>**E04** gwas_lookup, GWAS Catalog REST v2 (https://www.ebi.ac.uk/gwas/rest/api/v2/associations?rs_id=rs4784227&size=100; retrieved 2026-10-25T17:26:28+00:00)

> 34 GWAS Catalog associations for rs4784227, strongest first:
> Breast cancer: p 2.0e-240, effect allele T, risk-allele frequency NR, PMID 32139696
> Postmenopausal breast cancer: p 5.0e-50, effect allele T, risk-allele frequency NR, PMID 38538606
> Breast cancer (estrogen-receptor negative): p 2.0e-26, effect allele T, risk-allele frequency 0.24, PMID 29058716
> Biological Mother:  Cancer, Breast: p 2.0e-25, effect allele C, risk-allele frequency 0.7783, PMID 39024449
> Breast cancer (estrogen-receptor positive): p 1.0e-13, effect allele T, risk-allele frequency 0.06, PMID 38741014
> Parkinson's disease: p 1.0e-10, effect allele T, risk-allele frequency 0.265, PMID 28892059
> Systolic blood pressure: p 1.0e-09, effect allele T, risk-allele frequency 0.2398, PMID 33230300
> BRCA1/2-negative high-risk breast cancer: p 2.0e-09, effect allele T, risk-allele frequency 0.26, PMID 30323354
> Pulse pressure: p 2.0e-08, effect allele T, risk-allele frequency 0.2354, PMID 33230300
> Cancer: p 3.0e-08, effect allele ?, risk-allele frequency NR, PMID 34290314

<a id="e05"></a>**E05** finemap_lookup, Open Targets Platform (credible sets, L2G) (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-25T17:26:25+00:00)

> 83 credible sets contain 16_52565276_C_T: 74 GWAS, 9 molecular QTL.
> GWAS Breast cancer: PIP 1.00; L2G TOX3 0.92
> GWAS Malignant neoplasm of breast, excluding all cancers (control: PIP 1.00; L2G TOX3 0.92
> GWAS Breast cancer: PIP 1.00; L2G TOX3 0.93
> GWAS Breast cancer (luminal A): PIP 1.00; L2G TOX3 0.92
> GWAS Malignant neoplasm of breast, ER-positive, excluding all can: PIP 1.00; L2G TOX3 0.92
> GWAS Breast cancer [female] (PheCode 174.1): PIP 1.00; L2G TOX3 0.92
> eqtl for ENSG00000285800 (gtex-v10_exon_brain_spinal_cord_ensg00000285800_1_): PIP 0.07
> eqtl for ENSG00000285800 (gtex-v10_ge_brain_hippocampus_ensg00000285800): PIP 0.06
> tuqtl for TOX3 (gtex-v10_txrev_brain_hippocampus_ensg00000103460_g): PIP 0.05
> eqtl for ENSG00000285800 (gtex-v10_ge_brain_spinal_cord_ensg00000285800): PIP 0.04
> tuqtl for TOX3 (gtex-v10_txrev_brain_substantia_nigra_ensg00000103): PIP 0.04
> eqtl for ENSG00000285800 (gtex-v10_exon_brain_hippocampus_ensg00000285800_1_): PIP 0.03
> Best L2G gene scores across these sets: TOX3 0.96

<a id="e06"></a>**E06** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=rs4784227%20AND%20TOX3%20AND%20%22breast%20cancer%22&format=json&pageSize=8&resultType=core; retrieved 2026-10-25T17:26:28+00:00)

> Europe PMC: 77 hits for 'rs4784227 AND TOX3 AND "breast cancer"'; top 8 with PMIDs:
> PMID 41230718 (2026): Cis-regulatory and long noncoding RNA alterations in breast cancer - current insights, biomarker utility, and the critical need for functional validation.
> PMID 40932605 (2025): Molecular signatures of breast cancer in the Iranian population: a review of cell growth and cell cycle regulators.
> PMID 42001218 (2026): Prioritizing context-specific genetic risk mechanisms in 11 solid cancers.
> PMID 36042591 (2022): Association between the rs4784227-CASC16 polymorphism and the risk of breast cancer: A meta-analysis.
> PMID 39777116 (2025): Identification of significant single-nucleotide polymorphisms associated with breast cancer recurrence and metastasis using GWAS.
> PMID 38741014 (2024): Genome-wide association analyses of breast cancer in women of African ancestry identify new susceptibility loci and improve risk prediction.
> PMID 39587695 (2024): The shared genetic landscape of polycystic ovary syndrome and breast cancer: convergence on ER + breast cancer but not ER- breast cancer.
> PMID 38902506 (2024): Hidden secrets of the cancer genome: unlocking the impact of non-coding mutations in gene regulatory elements.

<a id="e07"></a>**E07** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> QBiC-SELEX screen of chr16:52565276:C>T: 997 models scored, 290 pass the gate (Bonferroni 0.05/997, p < 5.02e-05, |z| > 4.05), in 173 CIS-BP groups. Expression context: DepMap line ACH-000019. Groups shown: 10; dropped because no TF in the group reaches 1 TPM: 53 (Homeodomain, 1 model z -49.09, bZIP, 1 model z 44.2, Homeodomain; POU, 2 models z 23.66, Homeodomain; POU, 1 model z 22.86, Homeodomain; POU, 1 model z 19.26). Passing groups ranked below the ones shown: 110. In the group rows, 'own model' means the TF has its own QBiC-SELEX model and 'mapped' that it is covered only through CIS-BP-mapped models of related TFs. A TF not named in any group row may still have its own model, even one that passes the gate: look it up with qbic_tf_detail before stating its coverage or a QBiC-SELEX direction for it. predicted_effect > 0 means the alternate allele binds more strongly. In vitro binding only: expression and chromatin decide whether a change matters.

<a id="e08"></a>**E08** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G012 (bZIP, 6 models): best model MAFG_eDBD_TTGTTC40NAAG_KN_yin2017_0_3_7mer (own model of MAFG), z 71.57, effect 2.788 (alt binds more); 6 passing models (6 with the best model's sign). Passing members: MAFG z 71.57, NRL z 52.25, MAFK z 48.84, MAFB z 47.42, MAF z 41.62 (+1 more). TFs this group covers: MAFK (own model) 16.96 TPM, MAFG (own model) 8.48 TPM, MAFB (own model) 3.09 TPM, MAFA (own model) 1.07 TPM, NRL (own model) 0.98 TPM, MAF (own model) 0.23 TPM; best model's site strength: ref 97.6th, alt 100.0th percentile of its k-mer coefficients.

<a id="e09"></a>**E09** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G441 (C2H2 ZF, 1 model): best model ZNF134_FL_AC40NTGTTAC_AATA_jolma2025_0_3_7mer (own model of ZNF134), z 37.4, effect 2.724 (alt binds more); 1 passing models (1 with the best model's sign). Passing members: ZNF134 z 37.4. TFs this group covers: ZNF134 (own model) 4.56 TPM; best model's site strength: ref 99.2th, alt 100.0th percentile of its k-mer coefficients.

<a id="e10"></a>**E10** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G001 (Homeodomain, 81 models): best model LHX8_FL_TTGCGA40NGTA_KW_yin2017_0_4_7mer (own model of LHX8), z 28.05, effect 2.175 (alt binds more); 59 passing models (46 with the best model's sign); members disagree on direction. Passing members: LHX8 z 28.05, BARHL2 z -27.02, BARX1 z -23.33, HOXA2 z 20.4, HMX1 z -20.39 (+54 more). TFs this group covers: MSX2 (own model) 17.65 TPM, LMX1B (own model) 11.66 TPM, BARX2 (own model) 6.62 TPM, ZFHX3 (own model) 5.13 TPM, DLX3 (own model) 4.42 TPM, HOXB7 (own model) 4.39 TPM, LHX1 (own model) 4.3 TPM, PITX1 (own model) 4.1 TPM, HOXC9 (own model) 3.41 TPM, LBX2 (own model) 2.97 TPM (+103 more); best model's site strength: ref 94.6th, alt 99.3th percentile of its k-mer coefficients.

<a id="e11"></a>**E11** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G026 (Rel, 4 models): best model NFATC4_eDBD_TAGGTA40NGAT_KAN_yin2017_0_4_7mer (own model of NFATC4), z -23.46, effect -1.044 (alt binds less); 3 passing models (3 with the best model's sign). Passing members: NFATC4 z -23.46, NFATC2 z -9.14, NFATC3 z -4.28. TFs this group covers: NFATC3 (own model) 9.54 TPM, NFATC2 (own model) 2.41 TPM, NFATC1 (own model) 1.66 TPM, NFATC4 (own model) 0.86 TPM; best model's site strength: ref 98.0th, alt 70.9th percentile of its k-mer coefficients.

<a id="e12"></a>**E12** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G285 (Homeodomain; POU, 1 model): best model POU2F1_NA_TCTTTC20NGA_ESAC_yang2017_1_2_7mer (own model of POU2F1), z 22.8, effect 0.903 (alt binds more); 1 passing models (1 with the best model's sign). Passing members: POU2F1 z 22.8. TFs this group covers: POU2F1 (own model) 3.33 TPM; best model's site strength: ref 86.5th, alt 98.9th percentile of its k-mer coefficients.

<a id="e13"></a>**E13** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G217 (CENPB, 1 model): best model JRK_DBD_CA40NAGCGTA_YWCB_jolma2025_0_3_7mer (own model of JRK), z -21.69, effect -0.43 (alt binds less); 1 passing models (1 with the best model's sign). Passing members: JRK z -21.69. TFs this group covers: JRK (own model) 4.89 TPM; best model's site strength: ref 99.8th, alt 88.4th percentile of its k-mer coefficients.

<a id="e14"></a>**E14** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G006 (Homeodomain, 11 models): best model TPRX1_DBD_TG40NGACCTT_YWCB_jolma2025_0_2_7mer (own model of TPRX1), z -21.39, effect -0.283 (alt binds less); 6 passing models (5 with the best model's sign); members disagree on direction. Passing members: TPRX1 z -21.39, OTX1 z -16.59, OTX2 z -12.55, CRX z -5.7, DPRX z -4.88 (+1 more). TFs this group covers: PITX1 (own model) 4.1 TPM, GSC (own model) 2.38 TPM, OTX1 (own model) 1.25 TPM, PITX2 (own model) 1.02 TPM, DMBX1 (own model) 0.2 TPM, VSX1 (own model) 0.09 TPM, PITX3 (own model) 0.02 TPM, GSC2 (own model) 0.01 TPM, VAX1 (own model) 0.01 TPM, CRX (own model) 0.0 TPM (+4 more); best model's site strength: ref 100.0th, alt 99.7th percentile of its k-mer coefficients.

<a id="e15"></a>**E15** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G354 (bHLH, 1 model): best model TFAP4_NA_TCACGT20NGCA_ESAC_yang2017_0_3_7mer (own model of TFAP4), z 19.55, effect 1.433 (alt binds more); 1 passing models (1 with the best model's sign). Passing members: TFAP4 z 19.55. TFs this group covers: TFAP4 (own model) 6.85 TPM; best model's site strength: ref 83.4th, alt 100.0th percentile of its k-mer coefficients.

<a id="e16"></a>**E16** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G401 (C2H2 ZF, 1 model): best model ZBTB37_eDBD_TATGTC40NGGA_KR_yin2017_0_4_7mer (own model of ZBTB37), z -19.38, effect -3.006 (alt binds less); 1 passing models (1 with the best model's sign). Passing members: ZBTB37 z -19.38. TFs this group covers: ZBTB37 (own model) 2.15 TPM; best model's site strength: ref 99.7th, alt 97.1th percentile of its k-mer coefficients.

<a id="e17"></a>**E17** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G010 (GATA, 6 models): best model GATA2_eDBD_TATGCA40NGAG_KR_yin2017_1_3_7mer (own model of GATA2), z 18.65, effect 0.283 (alt binds more); 6 passing models (6 with the best model's sign). Passing members: GATA2 z 18.65, GATA6 z 14.98, GATA1 z 12.45, GATA3 z 10.91, GATA4 z 8.04 (+1 more). TFs this group covers: GATA3 (own model) 346.04 TPM, GATA2 (own model) 12.69 TPM, GATA6 (own model) 0.86 TPM, GATA4 (own model) 0.45 TPM, GATA1 (own model) 0.02 TPM, GATA5 (own model) 0.0 TPM; best model's site strength: ref 92.3th, alt 98.6th percentile of its k-mer coefficients.

<a id="e18"></a>**E18** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-26T00:40:00+00:00)

> No ENCODE MAFG ChIP-seq peak contains chr16:52565276:C>T in biosamples matching 'MCF7'. Absence can also mean no MAFG experiment in that biosample. 0 peaks lie within 100 bp without containing it.

<a id="e19"></a>**E19** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-26T00:40:00+00:00)

> No ENCODE MAFK ChIP-seq peak contains chr16:52565276:C>T in biosamples matching 'MCF7'. Absence can also mean no MAFK experiment in that biosample. In other biosamples, 1 MAFK peaks do contain the variant: HepG2 (experiments ENCSR000EEB).

<a id="e20"></a>**E20** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-25T17:27:50+00:00)

> 5 ENCODE GATA3 ChIP-seq peaks contain chr16:52565276:C>T in biosamples matching 'MCF7': biosamples MCF-7; experiments ENCSR000BST, ENCSR000EWV, ENCSR423RTK. In other biosamples, 2 GATA3 peaks do contain the variant: A549, T47D (experiments ENCSR000BMX, ENCSR000BTI).
