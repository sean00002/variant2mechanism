# rs11629191 and Breast cancer

Configuration `no_qbic`, named mode, seed 0. Models: generator claude-opus-5, critic claude-sonnet-5-5, summariser claude-haiku-5-5. Cost $0.45 over 7 model calls; 145 s.

Variant `chr14:55887040:C>T` (germline); expression context: DepMap:ACH-000019 (MCF7).

## Ranked chains

### 1. H1: No TF-mediated effect: non-functional, non-conserved passenger or tag for a linked variant elsewhere (p = 0.72)

Null chain: no TF-mediated effect of this variant.

Predictions: No allele-specific reporter/MPRA activity for the 200 bp window around chr14:55887040 in MCF7; No allelic imbalance in ATAC-seq or any TF ChIP-seq at this site in breast cells; No breast eQTL for PELI2, KTN1 or any neighbour, consistent with E09; Any future association in this region maps to a different, linked variant, e.g. inside EH38E1716463

Falsified if: Reproducible allele-specific MPRA/reporter effect for C vs T in a breast cell line; Demonstrated allele-specific binding of a named TF at this exact site (ChIP, footprint, EMSA); A fine-mapped breast cancer credible set places high PIP on rs11629191

### 2. H3: Ref C allele retains a GATA3 site in a weak, unannotated element; loss on alt T alters a distal target (p = 0.09)

TF GATA3 (stated coverage not_checked; registry own_model), ref allele binds more; element Unannotated non-cCRE sequence at chr14:55887040, 1868 bp from dELS EH38E1716463; gene KTN1; cell type Luminal ER+ breast epithelium (MCF7).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | GATA3 is proposed to bind the ref C allele more strongly, the T substitution degrading a GATA core/flank; GATA3 is chosen within the GATA family only because it is the dominant luminal breast factor, and no QBiC-SELEX, motif or ChIP evidence was available, so coverage is not_checked and this link is unsupported | missing | none |
| element | No cCRE overlaps the site and GERP is -3.12, so any element here is weak and unannotated; the evidence is compatible with, but does not support, a regulatory element | missing | [E01](#e01), [E03](#e03) |
| gene | KTN1 is the second-nearest protein-coding TSS at 328 kb; assignment rests on distance alone, and no breast eQTL supports it | missing | [E02](#e02), [E09](#e09) |
| cell_type | Any GATA3-dependent effect would be restricted to luminal ER+ cells such as MCF7; GATA3 expression in MCF7 was not looked up here | missing | none |
| phenotype | A modest KTN1 expression change would weakly affect breast cancer risk; no GWAS association exists for this variant, so phenotype support is absent | missing | [E04](#e04) |

Predictions: GATA3 ChIP-seq in MCF7 shows a peak at this site with reads preferentially carrying C; EMSA shows reduced nuclear complex with the T probe, competed by a GATA oligo; KTN1, not PELI2, tracks genotype in sensitive allele-specific expression assays

Falsified if: QBiC-SELEX shows no GATA-family binding change for this 12-mer; No GATA3 ChIP-seq peak within 100 bp in MCF7; CRISPRi/deletion of the site leaves KTN1 unchanged in MCF7

### 3. H5: Alt T alters an ESR1-associated distal element regulating the local lncRNA ENSG00000259868 (p = 0.08)

TF ESR1 (stated coverage not_checked; registry own_model), alt allele binds more; element Unannotated sequence near dELS EH38E1716463 within the PELI2/KTN1 interval; gene ENSG00000259868 (local non-coding transcript implicated by the only QTL signal for this variant); cell type ER+ breast epithelium (MCF7).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | ESR1 is proposed to bind the alt T allele more strongly via a half-ERE; ESR1 is a single gene so no within-group choice is needed, but no QBiC-SELEX, motif or ChIP evidence for ESR1 at this site was available, so coverage is not_checked and the direction is unsupported | missing | none |
| element | The site has no cCRE overlap and no regulatory annotation; the nearest dELS is 1868 bp away | missing | [E01](#e01), [E03](#e03) |
| gene | The only credible set containing this variant is a molecular QTL for ENSG00000259868, making that transcript the single data-supported candidate target, although the PIP is 0.03 and the tissue is brain nucleus accumbens, not breast | weak | [E05](#e05) |
| cell_type | An ESR1-dependent effect would be restricted to ER+ cells such as MCF7; the reported QTL is in brain, which is inconsistent with ER+-restricted action | missing | [E05](#e05) |
| phenotype | A change in this non-coding transcript could in principle modulate breast cancer risk, but no GWAS association and no breast eQTL support this | missing | [E04](#e04), [E09](#e09) |

Predictions: ENSG00000259868, not PELI2 or KTN1, shows allele-specific expression in heterozygotes; ESR1 ChIP/CUT&RUN in estrogen-stimulated MCF7 shows T-biased signal at the site; Effect appears only after estrogen stimulation

Falsified if: QBiC-SELEX shows no nuclear-receptor-group binding change for this 12-mer; ESR1 CUT&RUN in E2-treated MCF7 shows no signal at the site; ENSG00000259868 shows no genotype-dependent expression in any tissue with adequate power

### 4. H2: Alt T creates a forkhead (FOXA1) site in a weak distal element acting on PELI2 (p = 0.06)

TF FOXA1 (stated coverage not_checked; registry own_model), alt allele binds more; element Unannotated distal sequence ~1.9 kb from dELS EH38E1716463; gene PELI2; cell type Luminal ER+ breast epithelium (MCF7).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The C>T change is proposed to strengthen an A/T-rich forkhead-like core so that alt T binds FOXA1 more strongly; FOXA1 was chosen among forkhead factors as the dominant pioneer factor in MCF7, but ENCODE ChIP-seq shows no FOXA1 peak containing or within 100 bp of the variant in MCF-7, which argues against this link, and no QBiC-SELEX lookup was made | missing | [E07](#e07) |
| element | The variant overlaps no cCRE and no regulatory feature; the nearest dELS is 1868 bp away, so a pioneer-factor-opened weak element is speculative | missing | [E01](#e01), [E03](#e03) |
| gene | PELI2 is the nearest protein-coding TSS at 230.8 kb, but there is no breast eQTL for it at this variant | missing | [E02](#e02), [E09](#e09) |
| cell_type | Any effect would need FOXA1-positive luminal cells such as MCF7; no MCF7 occupancy at this site was detected | missing | [E07](#e07) |
| phenotype | PELI2 appears as a prognostic gene in papillary thyroid carcinoma, not breast cancer, and no GWAS signal exists for this variant, so phenotype support is absent | missing | [E06a](#e06a), [E04](#e04) |

Predictions: A FOXA1 ChIP experiment specifically in this region (or FOXA1 CUT&RUN) would show low but T-biased signal; Reporter with T allele more active than C only in FOXA1-expressing cells; PELI2 allele-specific expression in heterozygous luminal lines

Falsified if: QBiC-SELEX shows no forkhead-group binding change for this 12-mer; FOXA1 CUT&RUN in MCF7 again shows no signal at the site; No PELI2 genotype-dependent expression in breast samples

### 5. H4: Alt T strengthens a CTCF anchor, altering insulation in the PELI2/KTN1 interval (p = 0.05)

TF CTCF (stated coverage not_checked; registry own_model), alt allele binds more; element Candidate CTCF anchor outside annotated cCREs; gene PELI2; cell type MCF7 (CTCF occupancy largely cell-type invariant).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | CTCF was proposed to bind the alt T allele more strongly, but ENCODE ChIP-seq shows no CTCF peak containing the variant in MCF-7 and none within 100 bp, and no QBiC-SELEX lookup was made, so this link is contradicted by the available data | missing | [E08](#e08) |
| element | No cCRE, including no CTCF-only cCRE, overlaps the site, and conservation is low | missing | [E01](#e01), [E03](#e03) |
| gene | A boundary change would in principle redistribute contacts toward PELI2 at 230.8 kb, but only distance data exist and there is no breast eQTL | missing | [E02](#e02), [E09](#e09) |
| cell_type | CTCF sites are mostly shared across cell types, so absence in MCF7 argues the site is not a CTCF anchor anywhere | missing | [E08](#e08) |
| phenotype | No GWAS association and only a low-PIP brain eQTL for a different gene; no support for a breast cancer effect | missing | [E04](#e04), [E05](#e05) |

Predictions: CTCF/RAD21 ChIP in other cell types would still show a peak at the site; Allele-specific Hi-C/Micro-C boundary difference between homozygotes; Effect detectable across many cell types, unlike H2/H3/H5

Falsified if: No CTCF peak within 500 bp in any ENCODE biosample; No CTCF core motif on either allele; Allele-specific contact mapping shows no boundary change

## Prediction matrix

| Test | Cost | Separates top two | H1 | H3 | H5 | H2 | H4 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| QBiC-SELEX lookup of the 12-mer at chr14:55887040 (all TF groups, both directions) | existing data | yes | No significant binding change for any group, or changes only in groups not expressed in breast | Significant GATA-group loss on alt T (ref binds more) | Significant nuclear-receptor/half-ERE group gain on alt T | Significant forkhead-group gain on alt T | Significant CTCF-group gain on alt T |
| FOXA1 ChIP-seq peak overlap in MCF-7 (E07) | existing data | no | No peak (observed) | No FOXA1 peak required | FOXA1 co-binding often accompanies ESR1; absence weakens H5 | Peak expected; none observed, weakening H2 | No peak required |
| CTCF ChIP-seq peak overlap in MCF-7 (E08) | existing data | no | No peak (observed) | No peak required | No peak required | No peak required | Peak expected; none observed, strongly weakening H4 |
| GTEx breast mammary eQTL for PELI2/KTN1 (E09) | existing data | no | No significant eQTL (observed) | KTN1 eQTL expected; none observed | Effect on ENSG00000259868, not tested for breast here | PELI2 eQTL expected; none observed | PELI2 eQTL expected; none observed |
| GATA3 CUT&RUN in MCF7 with allele-specific read counting at chr14:55887040 | medium | yes | No signal above background; no allelic bias | Signal present with C-biased reads | No GATA3 signal, or signal only after estrogen with ESR1 | No GATA3 signal | No GATA3 signal |
| MPRA/luciferase of the 200 bp C and T windows in MCF7 (±estrogen) | medium | yes | No activity and no allelic difference | C allele more active (or more repressive) than T | T allele more active only after estrogen stimulation | T allele more active than C | No enhancer activity difference (insulation not captured in episomal assay) |
| CRISPRi/deletion of the site in MCF7, RNA-seq of PELI2, KTN1, ENSG00000259868 | high | yes | No gene changes | KTN1 changes | ENSG00000259868 changes | PELI2 changes | PELI2 changes with altered local contacts |

## Next experiment

Run the QBiC-SELEX lookup for the 12-mer centred on chr14:55887040 (C vs T) across all TF groups. It is existing data, costs nothing, and directly separates the null (no significant binding change in any breast-expressed group) from H3 (GATA-group loss on alt T), while simultaneously grading H2, H4 and H5. If no group shows a significant change, probability mass moves further to H1.

## Investigate calls

- chip_peaks({"tf": "FOXA1", "biosample": "MCF-7"})
- chip_peaks({"tf": "CTCF", "biosample": "MCF-7"})
- eqtl_lookup({"tissue": "Breast - Mammary Tissue"})

## Flags

- literature_fallback: no hits for 'rs11629191 AND PELI2 AND "breast cancer"'; dropped the rsID

Citation support: 0.85 of links cite only evidence that passed every check.

## Evidence

<a id="e01"></a>**E01** variant_annotation, Ensembl VEP (GRCh38) (https://rest.ensembl.org/vep/human/region/14:55887040-55887040:1/T?content-type=application/json&Conservation=1; retrieved 2026-10-25T17:32:49+00:00)

> Variant chr14:55887040:C>T (GRCh38), allele string C/T
> Known IDs: rs11629191
> Most severe consequence: intron_variant
> Regulatory features: none
> GERP conservation score at the site: -3.12
> Transcript consequences: none (intergenic)

<a id="e02"></a>**E02** nearest_genes, Ensembl overlap (protein_coding) (https://rest.ensembl.org/overlap/region/human/14:54887040-56887040?feature=gene;biotype=protein_coding;content-type=application/json; retrieved 2026-10-25T17:32:40+00:00)

> 14 protein-coding genes within 1000 kb of chr14:55887040:C>T, by distance to TSS:
> PELI2: 230.8 kb from TSS (upstream, strand +1)
> KTN1: 328.0 kb from TSS (downstream, strand +1)
> TBPL2: 430.3 kb from TSS (upstream, strand -1)
> ATG14: 475.2 kb from TSS (upstream, strand -1)
> TMEM260: 601.3 kb from TSS (upstream, strand +1)
> CHMP4BP1: 615.7 kb from TSS (downstream, strand +1)
> FBXO34: 615.7 kb from TSS (downstream, strand +1)
> DLGAP5: 695.4 kb from TSS (upstream, strand -1)
> LGALS3: 765.7 kb from TSS (downstream, strand +1)
> MAPK1IP1L: 835.4 kb from TSS (downstream, strand +1)

<a id="e03"></a>**E03** ccre_lookup, ENCODE v4 cCRE registry (ENCFF420VPZ) and SCREEN (https://screen-beta-api.wenglab.org/dataws/cre_table; retrieved 2026-10-25T17:32:13+00:00)

> No cCRE overlaps the variant; nearest is EH38E1716463 (dELS) 1868 bp away.
> SCREEN: 0 cCREs within 500 bp (max z-score across ENCODE biosamples):
> Biosample-specific z-scores are not in this call; the values above are maxima over biosamples.

<a id="e04"></a>**E04** gwas_lookup, GWAS Catalog REST v2 (https://www.ebi.ac.uk/gwas/rest/api/v2/associations?rs_id=rs11629191&size=100; retrieved 2026-10-25T17:32:50+00:00)

> 0 GWAS Catalog associations for rs11629191, strongest first:

<a id="e05"></a>**E05** finemap_lookup, Open Targets Platform (credible sets, L2G) (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-25T17:32:49+00:00)

> 1 credible sets contain 14_55887040_C_T: 0 GWAS, 1 molecular QTL.
> eqtl for ENSG00000259868 (gtex-v10_ge_brain_nucleus_accumbens_ensg0000025986): PIP 0.03

<a id="e06"></a>**E06** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=PELI2%20AND%20%22breast%20cancer%22&format=json&pageSize=8&resultType=core; retrieved 2026-10-25T17:32:50+00:00)

> Europe PMC: 178 hits for 'PELI2 AND "breast cancer"'; top 7 with PMIDs:
> PMID 41023515 (2025): Pellino ubiquitin ligases: double-edged swords in hematologic malignancies-from oncogenic stabilizers to therapeutic vulnerabilities.
> PMID 41331176 (2025): Construction and validation of risk models of prognostic genes associated with parthanatos in papillary thyroid carcinoma based on bioinformatics.
> PMID 40362379 (2025): &lt;i&gt;O&lt;/i&gt;-Desmethyltramadol Enhanced Anti-Cancer Efficacy over Tramadol Through Non-μ-Opioid Receptor and Differential Cellular Contexts of Human Breast Cancer Cells.
> PMID 42757486 (2026): Pemetrexed increases BRCA1 protein stability and sensitizes TNBC cells to radiotherapy.
> PMID 42734444 (2027): Anesthesia inhalation agent sevoflurane induces perioperative cognitive impairment: Apelin/early growth response 1 axis induces ferritinophagy and exacerbates ferroptosis.
> PMID 41079921 (2025): PRMT1/PRMT5-Mediated Differential Arginine Methylation of CRIP1 Promotes the Recurrence of Small Cell Lung Cancer after Chemotherapy.
> PMID 42380137 (2026): HOXC9 accelerates esophageal squamous cell carcinoma progression via OTUD1-FABP5-mediated lipid metabolic reprogramming.

<a id="e06a"></a>**E06a** literature_search, Europe PMC abstract, PMID 41331176 (https://europepmc.org/article/MED/41331176; retrieved 2026-10-25T17:32:50+00:00)

> ResultsSeven prognostic genes (TSHZ3, SERGEF, AKAP12, SGPP2, ASGR1, AK1, PELI2) were identified.

<a id="e07"></a>**E07** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-26T00:28:52+00:00)

> No ENCODE FOXA1 ChIP-seq peak contains chr14:55887040:C>T in biosamples matching 'MCF-7'. Absence can also mean no FOXA1 experiment in that biosample. 0 peaks lie within 100 bp without containing it.

<a id="e08"></a>**E08** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-26T00:28:52+00:00)

> No ENCODE CTCF ChIP-seq peak contains chr14:55887040:C>T in biosamples matching 'MCF-7'. Absence can also mean no CTCF experiment in that biosample. 0 peaks lie within 100 bp without containing it.

<a id="e09"></a>**E09** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr14_55887040_C_T_b38&datasetId=gtex_v8; retrieved 2026-10-25T17:34:02+00:00)

> 0 significant GTEx v8 single-tissue eQTLs for chr14_55887040_C_T_b38 in tissues matching 'Breast - Mammary Tissue'. NES is the effect of the alt allele (T) relative to ref (C).
