# rs7001688 and LDL cholesterol

Configuration `no_qbic`, named mode, seed 0. Models: generator claude-opus-5, critic claude-sonnet-5-5, summariser claude-haiku-5-5. Cost $0.44 over 7 model calls; 137 s.

Variant `chr8:57573391:G>T` (germline); expression context: DepMap:ACH-000625 (Hep 3B2.1-7).

## Ranked chains

### 1. H1: Null: rs7001688 has no TF-mediated regulatory effect (p = 0.72)

Null chain: no TF-mediated effect of this variant.

Predictions: No allele-specific reporter, ATAC or ChIP signal at chr8:57573391 in hepatocyte models (Hep 3B2.1-7, HepG2).; No liver eQTL for FAM110B, CYP7A1 or any other gene is attributable to this variant, consistent with E07.; No GWAS credible set for LDL cholesterol contains this variant (E04, E05).; Base editing or deletion of the 50 bp around the site in hepatocytes changes no neighbouring transcript.

Falsified if: A reproducible allele-specific regulatory effect (MPRA or luciferase, or allele-specific ChIP/ATAC) is shown for G vs T at this position.; Fine-mapping places rs7001688 in an LDL credible set with non-trivial posterior probability.; CRISPR perturbation of the site alters expression of a lipid-relevant gene in hepatocytes.

### 2. H3: FOXA2 forkhead site created by the T allele, acting on FAM110B (p = 0.11)

TF FOXA2 (stated coverage not_checked; registry own_model), alt allele binds more; element Unannotated candidate element at chr8:57573391 (no overlapping cCRE, E03); gene FAM110B; cell type Hepatocyte (Hep 3B2.1-7).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The T (alt) allele is proposed to create a forkhead-like core; FOXA2 is named within the forkhead family as the hepatic pioneer factor, but this choice rests on background knowledge, not on cited data. No QBiC-SELEX lookup for FOXA2 was performed, so coverage is not_checked, and no ChIP evidence at this site was supplied (E08 covers HNF4A only). | missing | none |
| element | A pioneer factor could act on a closed, registry-absent element; E03 shows no cCRE within 500 bp, which is compatible with but does not support a cryptic element. | missing | [E01](#e01), [E03](#e03) |
| gene | FAM110B is the nearest protein-coding gene at 420.6 kb (E02) and appears in one statin-response genome-wide study (E06), but the variant is not an eQTL for it in any GTEx tissue (E07). | missing | [E02](#e02), [E06](#e06), [E07](#e07) |
| cell_type | Effect would be confined to FOXA2-positive hepatocytes; no expression evidence was supplied for the Hep 3B2.1-7 context. | missing | none |
| phenotype | Gain of FOXA2 binding would raise FAM110B expression and modestly shift plasma LDL; no cited evidence connects FAM110B expression to LDL at this variant (E04, E05 show no association records). | missing | [E04](#e04), [E05](#e05) |

Predictions: ATAC/DNase footprint or open-chromatin signal appears preferentially on T-allele haplotypes.; FOXA2 (or FOXA1) ChIP-seq in HepG2/liver shows a peak within 100 bp of the variant.; MPRA shows T > G activity, the opposite direction to H2 and H4.; FAM110B, not CYP7A1, responds to CRISPRi of the element.

Falsified if: No forkhead core is created by G>T on either strand in a motif scan or QBiC model.; FOXA2/FOXA1 ChIP-seq in liver or HepG2 shows no peak within 1 kb.; FAM110B expression is unchanged by allele or by deletion of the element.

### 3. H4: CEBPB bZIP site lost on the T allele in a hepatic element near EH38E3835076 (p = 0.10)

TF CEBPB (stated coverage not_checked; registry own_model), ref allele binds more; element Candidate hepatic element within the 1.5 kb window containing the CA-H3K4me3 cCRE EH38E3835076; gene FAM110B; cell type Hepatocyte (Hep 3B2.1-7).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The G allele is proposed to support a C/EBP half-site; CEBPB is chosen within the C/EBP group on hepatocyte-expression grounds that are not evidenced here. No QBiC-SELEX lookup was done, so coverage is not_checked, and no ChIP evidence for CEBPB at this site was supplied. | missing | none |
| element | The only nearby annotation is a CA-H3K4me3 cCRE 1544 bp away; the variant itself overlaps no cCRE and is non-conserved (GERP 0.27), so the element assignment is speculative. | missing | [E01](#e01), [E03](#e03) |
| gene | FAM110B is the nearest gene at 420.6 kb (E02); no eQTL supports the link (E07). | missing | [E02](#e02), [E07](#e07) |
| cell_type | Hepatocyte context as supplied (Hep 3B2.1-7); no expression data cited. | missing | none |
| phenotype | Loss of CEBPB binding on T would reduce element activity and FAM110B expression with a small upward LDL shift; no association evidence exists for this variant (E04, E05). | missing | [E04](#e04), [E05](#e05) |

Predictions: CEBPB ChIP-seq peak in HepG2 or liver overlapping the variant, allele-biased toward G.; Allelic reporter difference appears only under C/EBP-activating conditions (e.g. IL-6 or dexamethasone).; Any signal localises to the 1.5 kb window around EH38E3835076 rather than to the variant base alone.

Falsified if: CEBPB ChIP-seq shows no occupancy in liver or hepatoma lines.; Condition-dependent reporter assays show no allelic difference under C/EBP activation.

### 4. H2: HNF4A DR1 site in a cryptic hepatic enhancer acting on CYP7A1 (p = 0.07)

TF HNF4A (stated coverage not_checked; registry own_model), ref allele binds more; element Putative distal hepatic element at chr8:57573391, absent from the ENCODE cCRE registry (E03); gene CYP7A1; cell type Hepatocyte (Hep 3B2.1-7, DepMap ACH-000625).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The G (ref) allele is proposed to carry a DR1-like nuclear-receptor motif bound by HNF4A, with T disrupting it. No QBiC-SELEX model was retrieved for HNF4A, so coverage is not_checked; the only direct test available, ENCODE ChIP-seq in HepG2, shows no HNF4A peak containing the variant and none within 100 bp (E08), which argues against this link. | missing | [E08](#e08) |
| element | No cCRE overlaps the variant and none lies within 500 bp (nearest CA-H3K4me3 element 1544 bp away), so any enhancer would have to be unannotated; the site is also poorly conserved (GERP 0.27, E01). | missing | [E01](#e01), [E03](#e03) |
| gene | CYP7A1 is the nearest bile-acid/LDL gene at 926.8 kb (E02); no eQTL supports this link, since the variant has zero significant GTEx v8 eQTLs in any tissue (E07), and Open Targets shows no CYP7A1 association with a large-LDL cholesterol trait (E09). | missing | [E02](#e02), [E07](#e07), [E09](#e09) |
| cell_type | Any effect would be hepatocyte-restricted; the supplied context is Hep 3B2.1-7, but no expression evidence for HNF4A or CYP7A1 in this line was provided. | missing | none |
| phenotype | Less HNF4A binding on T would lower CYP7A1 transcription and raise plasma LDL; no cited evidence links this variant to LDL (E04, E05 show no association records). | missing | [E04](#e04), [E05](#e05) |

Predictions: HNF4A ChIP-seq in primary hepatocytes or liver tissue (not just HepG2) would show a peak at the site, higher on G.; Promoter-capture Hi-C in liver shows contact between chr8:57.57 Mb and the CYP7A1 promoter.; Reporter activity in Hep 3B2.1-7 is lower for T than G, and the difference is abolished by HNF4A knockdown.

Falsified if: HNF4A ChIP-seq in liver tissue also shows no occupancy at this position (already negative in HepG2, E08).; No chromatin contact between the variant and CYP7A1 is detected.; Luciferase/MPRA shows equal G and T activity.

## Prediction matrix

| Test | Cost | Separates top two | H1 | H3 | H4 | H2 |
| --- | --- | --- | --- | --- | --- | --- |
| QBiC-SELEX detail lookup for FOXA2, CEBPB and HNF4A at chr8:57573391 (coverage and predicted allelic binding change) | existing data | yes | No TF group shows a significant allelic binding change, or the TFs are not in coverage so no claim can be made | Forkhead group including FOXA2 predicted to bind T more strongly | C/EBP group including CEBPB predicted to bind G more strongly | HNF4A (own model or CIS-BP-mapped) predicted to bind G more strongly |
| Factorbook/ENCODE ChIP-seq peak lookup for FOXA2 and FOXA1 in HepG2 and liver | existing data | yes | No peak contains the variant | FOXA2/FOXA1 peak contains or lies within 100 bp of the variant | No FOXA peak; a CEBPB peak may be present instead | No FOXA peak needed; HNF4A already negative in HepG2 (E08) |
| Factorbook/ENCODE ChIP-seq peak lookup for CEBPB in HepG2 | existing data | no | No peak | No peak required | CEBPB peak overlapping or adjacent to the variant | No peak required |
| Cross-tissue eQTL re-query (GTEx liver, eQTLGen, liver-specific sQTL) for the variant | existing data | yes | No significant eQTL in any tissue, as already seen in GTEx v8 (E07) | Liver eQTL for FAM110B with T raising expression | Liver eQTL for FAM110B with T lowering expression | Liver eQTL for CYP7A1 with T lowering expression |
| Allelic luciferase/MPRA of a 200 bp window around chr8:57573391 in Hep 3B2.1-7 | medium | yes | No activity above background and no G-vs-T difference | Activity with T > G | G > T only under C/EBP-activating stimulus (IL-6) | Enhancer activity with G > T |
| CRISPRi tiling of the element plus RNA-seq in Hep 3B2.1-7 | high | yes | No neighbouring gene changes | FAM110B decreases | FAM110B decreases, stimulus-dependent | CYP7A1 decreases |
| Fine-mapping / conditional analysis of LDL GWAS in the 8p12 window | existing data | yes | Variant absent from all LDL credible sets (consistent with E04, E05) | Variant in a credible set tied to a FAM110B-region signal | Variant in a credible set tied to a FAM110B-region signal | Variant in a credible set tied to a CYP7A1-region signal |

## Next experiment

Run a QBiC-SELEX detail lookup at chr8:57573391 for FOXA2 (and, in the same call set, CEBPB and HNF4A): it is existing-data cost, establishes true coverage instead of not_checked, and directly tests the only remaining non-null claim with meaningful probability (H3, gain of a forkhead site on T) against the null H1. If no forkhead group shows an allelic binding change, H3 collapses and H1 absorbs its weight; if it does, the next step is the free Factorbook FOXA2/FOXA1 peak lookup in HepG2 and liver.

## Investigate calls

- eqtl_lookup({"tissue": null})
- chip_peaks({"tf": "HNF4A", "biosample": "HepG2"})
- gene_disease({"gene": "CYP7A1"})

## Flags

- literature_fallback: no hits for 'rs7001688 AND FAM110B AND "ldl cholesterol"'; dropped the rsID

Citation support: 0.67 of links cite only evidence that passed every check.

## Evidence

<a id="e01"></a>**E01** variant_annotation, Ensembl VEP (GRCh38) (https://rest.ensembl.org/vep/human/region/8:57573391-57573391:1/T?content-type=application/json&Conservation=1; retrieved 2026-10-25T17:33:20+00:00)

> Variant chr8:57573391:G>T (GRCh38), allele string G/T
> Known IDs: rs7001688
> Most severe consequence: intron_variant
> Regulatory features: none
> GERP conservation score at the site: 0.267
> Transcript consequences: none (intergenic)

<a id="e02"></a>**E02** nearest_genes, Ensembl overlap (protein_coding) (https://rest.ensembl.org/overlap/region/human/8:56573391-58573391?feature=gene;biotype=protein_coding;content-type=application/json; retrieved 2026-10-25T17:32:33+00:00)

> 5 protein-coding genes within 1000 kb of chr8:57573391:G>T, by distance to TSS:
> FAM110B: 420.6 kb from TSS (upstream, strand +1)
> BPNT2: 579.5 kb from TSS (upstream, strand -1)
> UBXN2B: 838.0 kb from TSS (upstream, strand +1)
> CYP7A1: 926.8 kb from TSS (downstream, strand -1)
> SDCBP: 979.5 kb from TSS (upstream, strand +1)

<a id="e03"></a>**E03** ccre_lookup, ENCODE v4 cCRE registry (ENCFF420VPZ) and SCREEN (https://screen-beta-api.wenglab.org/dataws/cre_table; retrieved 2026-10-25T17:32:27+00:00)

> No cCRE overlaps the variant; nearest is EH38E3835076 (CA-H3K4me3) 1544 bp away.
> SCREEN: 0 cCREs within 500 bp (max z-score across ENCODE biosamples):
> Biosample-specific z-scores are not in this call; the values above are maxima over biosamples.

<a id="e04"></a>**E04** gwas_lookup, GWAS Catalog REST v2 (https://www.ebi.ac.uk/gwas/rest/api/v2/associations?rs_id=rs7001688&size=100; retrieved 2026-10-25T17:33:20+00:00)

> 0 GWAS Catalog associations for rs7001688, strongest first:

<a id="e05"></a>**E05** finemap_lookup, Open Targets Platform (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-25T17:33:20+00:00)

> Open Targets has no record of 8_57573391_G_T.

<a id="e06"></a>**E06** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=FAM110B%20AND%20%22ldl%20cholesterol%22&format=json&pageSize=8&resultType=core; retrieved 2026-10-25T17:33:21+00:00)

> Europe PMC: 1 hits for 'FAM110B AND "ldl cholesterol"'; top 1 with PMIDs:
> PMID 22666496 (2012): Genome-wide study of gene variants associated with differential cardiovascular event reduction by pravastatin therapy.

<a id="e07"></a>**E07** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr8_57573391_G_T_b38&datasetId=gtex_v8; retrieved 2026-10-25T17:34:31+00:00)

> 0 significant GTEx v8 single-tissue eQTLs for chr8_57573391_G_T_b38. NES is the effect of the alt allele (T) relative to ref (G).

<a id="e08"></a>**E08** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-26T00:31:22+00:00)

> No ENCODE HNF4A ChIP-seq peak contains chr8:57573391:G>T in biosamples matching 'HepG2'. Absence can also mean no HNF4A experiment in that biosample. 0 peaks lie within 100 bp without containing it.

<a id="e09"></a>**E09** gene_disease, Open Targets Platform (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-25T17:34:31+00:00)

> Open Targets: no association between CYP7A1 and free cholesterol in large LDL measurement (EFO_0022176).
