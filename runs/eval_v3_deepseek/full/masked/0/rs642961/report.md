# rs642961 and Cleft lip (IRF6)

Configuration `full`, masked mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.02 over 9 model calls; 424 s.

Variant `chr1:209815925:A>G` (germline); expression context: none.

## QBiC-SELEX screen (occupancy first)

Occupied candidates: ZNF687 (bound elsewhere, z -0.21, no clear allelic change, weak site). Occupancy unknown: ETV2 (z 77.65); ETV3 (z 77.65); ETV3L (z 77.65); FEV (z 77.65); FLI1 (z 77.65). Diagnostic, not shown to the model: 222 of 997 models pass Bonferroni.

## Ranked chains

### 1. H5: No TF-mediated allelic effect; linked causal variant or passenger (p = 0.74)

Null chain: no TF-mediated effect of this variant.

Predictions: No allele-specific TF binding or enhancer-activity difference at this exact base in disease-relevant cells.; Any cleft-lip association is explained by linkage disequilibrium with another variant.; The strong Ets QBiC-SELEX prediction is not occupied in vivo, and the occupied ZNF687 site shows no clear allelic change.

Falsified if: Allele-specific Ets or other TF binding and enhancer activity are demonstrated at this base in oral/craniofacial cells.; CRISPR editing of this base changes IRF6 or another cleft-lip gene in a disease-relevant cell type.

### 2. H1: FLI1 binding at the alt allele alters IRF6 dosage in oral epithelium (p = 0.17)

TF FLI1 (QBiC-SELEX coverage own_model), alt allele binds more; element EH38E2863563 dELS; gene IRF6; cell type oral/craniofacial epithelial cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | FLI1 has its own QBiC-SELEX model: the alt G allele is predicted to bind more strongly than ref A (z 13.73, effect +0.906; alt 98.7th vs ref 90.1st percentile). ENCODE has no FLI1 ChIP-seq peak containing the variant in any biosample, and FLI1 expression in GTEx minor salivary gland is modest (8.27 TPM, 51.9th percentile), so occupancy at this base is not established. | weak | [E17](#e17), [E18](#e18), [E19](#e19) |
| element | The variant lies in EH38E2863563, a distal enhancer-like cCRE with DNase and H3K27ac marks, consistent with an active enhancer. | supported | [E01](#e01), [E03](#e03), [E04](#e04) |
| gene | IRF6 is the nearest TSS, 9.7 kb away, and is a cleft-lip L2G gene; IRF6 also has a brain eQTL at this variant (alt G NES -0.62), but no enhancer-target assay or oral epithelial eQTL is given. | weak | [E02](#e02), [E07](#e07), [E08](#e08) |
| cell_type | FLI1 is expressed in GTEx minor salivary gland, a craniofacial/secretory tissue, but no oral epithelial expression, matched ENCODE biosample, or ChIP data are provided, so the cell-type link remains inferred. | weak | [E19](#e19) |
| phenotype | The cleft GWAS association is weak (p 2e-6) and its effect allele is A; the IRF6 brain eQTL has alt G lowering IRF6. A simple alt-G/FLI1-to-IRF6 cleft model therefore has unresolved or opposite direction and needs oral-cell functional evidence. | weak | [E06](#e06), [E07](#e07), [E08](#e08), [E09](#e09) |

Predictions: Allele-specific FLI1 ChIP enrichment at the alt G allele in oral epithelial cells.; Ref/alt reporter shows the alt G allele changes enhancer activity and IRF6 expression in oral epithelial cells.; The effect depends on the Ets motif.

Falsified if: No allele-specific FLI1 binding at this base in disease-relevant cells.; The alt G allele does not change enhancer activity or IRF6 expression in oral epithelial cells.; IRF6 is not the target gene of this enhancer in craniofacial epithelium.

### 3. H2: ETV2-like Ets binding at the alt allele affects UTP25 (p = 0.05)

TF ETV2 (QBiC-SELEX coverage own_model), alt allele binds more; element EH38E2863563 dELS; gene UTP25; cell type craniofacial epithelial or endothelial cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | ETV2 has no independent QBiC-SELEX model at this site; the prediction uses a CIS-BP-mapped ETV5 Ets model, which favors the alt G allele (z 77.65, effect +1.32). ETV2 occupancy is unknown because ENCODE never assayed ETV2 here, so this is not ETV2-specific evidence. | weak | [E12](#e12), [E10](#e10) |
| element | The variant is in EH38E2863563, a dELS with active enhancer marks. | supported | [E01](#e01), [E03](#e03), [E04](#e04) |
| gene | UTP25 is 12 kb from the variant and has the highest L2G score (0.75), but there is no UTP25 eQTL or enhancer-target assay; literature search hits are not direct functional evidence. | weak | [E02](#e02), [E07](#e07), [E09](#e09) |
| cell_type | An ETV2-driven mechanism would require ETV2 expression in craniofacial epithelial or endothelial cells; expression and occupancy are not shown in this case. | missing | none |
| phenotype | Altered UTP25 dosage in craniofacial cells could contribute to cleft lip, but the cleft association is weak and indirect, and no UTP25 dosage or functional enhancer evidence is provided. | weak | [E06](#e06), [E09](#e09) |

Predictions: ETV2 ChIP occupancy or allele-specific ETV2 binding in a disease-relevant cell type.; UTP25 expression change in oral/craniofacial cells from the alt G allele.; The Ets motif is required for the UTP25 effect.

Falsified if: No ETV2 expression or occupancy in craniofacial cells.; The alt allele does not change UTP25 expression in relevant cells.; UTP25 is not regulated by this enhancer.

### 4. H4: ZNF687 occupancy at the variant has a weak allele-specific effect (p = 0.04)

TF ZNF687 (QBiC-SELEX coverage own_model), ref allele binds more; element EH38E2863563 dELS; gene IRF6; cell type GM12878 lymphoblastoid cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | ZNF687 has the only ENCODE ChIP-seq peak over the variant, in GM12878. Its own QBiC-SELEX model shows a tiny ref-favoring change below the gate (z -0.21, effect -0.013) and a weak site, so allele-specific ZNF687 binding is not established. | weak | [E05](#e05), [E11](#e11), [E10](#e10) |
| element | The variant lies in the EH38E2863563 dELS active enhancer-like element. | supported | [E01](#e01), [E03](#e03) |
| gene | IRF6 is the nearest TSS and a cleft-lip L2G gene, but no ZNF687-IRF6 target evidence is given. | weak | [E02](#e02), [E07](#e07) |
| cell_type | The only direct occupancy evidence is in GM12878 lymphoblastoid cells, which are not the disease-relevant craniofacial cell type. | supported | [E05](#e05) |
| phenotype | A ZNF687-mediated effect on IRF6 and cleft lip is possible but weak, because the allelic QBiC effect is negligible and the disease-relevant cell type is not matched. | weak | [E06](#e06), [E09](#e09) |

Predictions: Allele-specific ZNF687 ChIP imbalance in GM12878 or another ZNF687-expressing cell type.; The effect is small and would require a strong reporter or CRISPR validation.; No strong Ets-like effect should be assigned to ZNF687.

Falsified if: No allele-specific ZNF687 occupancy at this base.; ZNF687 does not regulate IRF6 in relevant cells.; The QBiC-SELEX effect remains below the gate and no functional enhancer change is seen.

## Prediction matrix

| Test | Cost | Separates top two | H5 | H1 | H2 | H4 |
| --- | --- | --- | --- | --- | --- | --- |
| Allele-specific FLI1 ChIP-qPCR at chr1:209815925 in oral epithelial cells | medium | yes | no allelic imbalance | alt G shows higher FLI1 enrichment than ref A | no FLI1 enrichment; ETV2 not tested by this assay | no FLI1 enrichment |
| Ref/alt enhancer reporter in an oral epithelial cell line | medium | yes | no difference between ref and alt | alt G changes enhancer activity | alt G changes activity via an Ets motif | negligible or no change |
| CRISPR edit the variant in oral epithelial cells and measure IRF6 and UTP25 | high | yes | no change | IRF6 expression changes | UTP25 expression changes | no change |
| Existing ENCODE FLI1 ChIP-seq across all biosamples | existing data | no | no FLI1 peak | a peak would be possible if FLI1 were assayed in a relevant biosample | no FLI1 peak | no FLI1 peak |
| ZNF687 allele-specific ChIP in GM12878 | medium | no | no allelic imbalance | no ZNF687 allelic imbalance | no ZNF687 allelic imbalance | ref A shows more ZNF687 binding than alt G |

## Next experiment

Ref/alt enhancer reporter assay in an oral epithelial cell line; if activity differs, follow with FLI1 ChIP-qPCR and Ets-motif mutation to test whether FLI1 mediates the allelic effect.

## Investigate calls

- qbic_tf_detail({"tf": "FLI1"})
- chip_peaks({"tf": "FLI1", "biosample": null})
- tf_expression({"tf": "FLI1", "context": "GTEx:Minor Salivary Gland"})

## Flags

- quote_rejected: PMID 42873673: not an exact substring of the abstract

Citation support: 0.93 of links cite only evidence that passed every check.

## Evidence

<a id="e01"></a>**E01** variant_annotation, Ensembl VEP (GRCh38) (https://rest.ensembl.org/vep/human/region/1:209815925-209815925:1/G?content-type=application/json&Conservation=1; retrieved 2026-10-25T17:29:41+00:00)

> Variant chr1:209815925:A>G (GRCh38), allele string A/G
> Known IDs: rs642961
> Most severe consequence: regulatory_region_variant
> Regulatory features: ENSR1_B3JM9C enhancer
> GERP conservation score at the site: 0.516
> Transcript consequences: none (intergenic)

<a id="e02"></a>**E02** nearest_genes, Ensembl overlap (protein_coding) (https://rest.ensembl.org/overlap/region/human/1:208815925-210815925?feature=gene;biotype=protein_coding;content-type=application/json; retrieved 2026-10-25T17:29:25+00:00)

> 13 protein-coding genes within 1000 kb of chr1:209815925:A>G, by distance to TSS:
> IRF6: 9.7 kb from TSS (upstream, strand -1)
> ENSG00000289700: 9.7 kb from TSS (upstream, strand -1)
> UTP25: 12.0 kb from TSS (upstream, strand +1)
> C1orf74: 31.3 kb from TSS (upstream, strand -1)
> TRAF3IP3: 60.4 kb from TSS (downstream, strand +1)
> SYT14: 85.0 kb from TSS (upstream, strand +1)
> HSD11B1: 129.8 kb from TSS (downstream, strand +1)
> G0S2: 140.5 kb from TSS (downstream, strand +1)
> LAMB3: 162.8 kb from TSS (upstream, strand -1)
> CAMK1G: 232.2 kb from TSS (downstream, strand +1)

<a id="e03"></a>**E03** ccre_lookup, ENCODE v4 cCRE registry (ENCFF420VPZ) and SCREEN (https://screen-beta-api.wenglab.org/dataws/cre_table; retrieved 2026-10-25T17:29:16+00:00)

> The variant lies in cCRE EH38E2863563 (dELS: distal enhancer-like), chr1:209815915-209816264.
> SCREEN: 2 cCREs within 500 bp (max z-score across ENCODE biosamples):
> EH38E2863563 dELS (contains the variant): DNase z 5.3, H3K27ac z 5.0, H3K4me3 z 2.4, CTCF z 1.5; nearby genes IRF6, UTP25, C1orf74
> EH38E2863562 dELS: DNase z 3.2, H3K27ac z 4.9, H3K4me3 z 1.9, CTCF z 1.5; nearby genes IRF6, UTP25, C1orf74
> Biosample-specific z-scores are not in this call; the values above are maxima over biosamples.

<a id="e04"></a>**E04** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> ENCODE TF ChIP-seq at chr1:209815925:A>G: 15 peaks contain the variant, from 6 factors in 6 biosamples. No ENCODE biosample matches the expression context, so no peak counts as bound here. cCRE class at the variant: dELS. Bound factors outside the TF model collection (co-factors, Pol II, and TFs with no binding model; signs of an active element, not TF candidates): DPF2, MYC, POLR2A, POLR2AphosphoS5, STAT3. Bound, expressed TFs with a binding model: 1; listed one per row: ZNF687. Assayed with no peak here: 0 TFs in the matching biosample, 572 only elsewhere; never assayed: 536.

<a id="e05"></a>**E05** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> ZNF687: bound elsewhere. 1 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: GM12878 (e.g. ENCSR859FDL). expression not filtered (no expression data for this context).

<a id="e06"></a>**E06** gwas_lookup, GWAS Catalog REST v2 (https://www.ebi.ac.uk/gwas/rest/api/v2/associations?rs_id=rs642961&size=100; retrieved 2026-10-25T17:29:42+00:00)

> 8 GWAS Catalog associations for rs642961, strongest first:
> Systolic blood pressure: p 6.0e-12, effect allele G, risk-allele frequency NR, PMID 38689001
> Hypertension: p 2.0e-08, effect allele A, risk-allele frequency 0.1951, PMID 33230300
> Pulse pressure: p 1.0e-07, effect allele G, risk-allele frequency NR, PMID 38689001
> Diastolic blood pressure: p 3.0e-07, effect allele G, risk-allele frequency NR, PMID 38689001
> Orofacial clefts: p 2.0e-06, effect allele A, risk-allele frequency NR, PMID 19270707

<a id="e07"></a>**E07** finemap_lookup, Open Targets Platform (credible sets, L2G) (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-25T17:29:41+00:00)

> 18 credible sets contain 1_209815925_A_G: 14 GWAS, 4 molecular QTL.
> GWAS Systolic blood pressure: PIP 0.10; L2G TRAF3IP3 0.11, IRF6 0.11, UTP25 0.10
> GWAS Systolic blood pressure: PIP 0.09; L2G IRF6 0.67, UTP25 0.14, TRAF3IP3 0.08
> GWAS Systolic blood pressure, combined automated + manual reading: PIP 0.05; L2G IRF6 0.13, UTP25 0.10, C1orf74 0.10
> GWAS Orofacial clefts: PIP 0.05; L2G IRF6 0.16, TRAF3IP3 0.12, C1orf74 0.10
> GWAS Systolic blood pressure: PIP 0.05; L2G IRF6 0.13, C1orf74 0.09, UTP25 0.08
> GWAS Systolic blood pressure (MTAG): PIP 0.05; L2G IRF6 0.17, C1orf74 0.09, UTP25 0.08
> eqtl for TRAF3IP3 (blueprint_tx_monocyte_enst00000460314): PIP 0.04
> eqtl for TRAF3IP3 (twinsuk_tx_blood_enst00000367023): PIP 0.02
> eqtl for TRAF3IP3 (twinsuk_exon_blood_ensg00000009790_15_1_209782056_): PIP 0.02
> eqtl for TRAF3IP3 (schmiedel_2018_exon_treg_naive_ensg00000009790_15_): PIP 0.02
> Best L2G gene scores across these sets: UTP25 0.75, IRF6 0.67, TRAF3IP3 0.53, C1orf74 0.10

<a id="e08"></a>**E08** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr1_209815925_A_G_b38&datasetId=gtex_v8; retrieved 2026-10-25T22:31:38+00:00)

> 15 significant GTEx v8 single-tissue eQTLs for chr1_209815925_A_G_b38. NES is the effect of the alt allele (G) relative to ref (A).
> SYT14 in Nerve_Tibial: NES -0.50, p 6.7e-20
> DIEXF in Cells_Cultured_fibroblasts: NES -0.23, p 1.9e-14
> DIEXF in Artery_Tibial: NES -0.23, p 1.2e-10
> TRAF3IP3 in Whole_Blood: NES +0.24, p 5.9e-10
> IRF6 in Brain_Cerebellum: NES -0.62, p 2.2e-07
> DIEXF in Whole_Blood: NES -0.15, p 2.9e-07
> SYT14 in Brain_Hippocampus: NES +0.53, p 3.3e-07
> DIEXF in Adipose_Subcutaneous: NES -0.20, p 7.5e-07
> SYT14 in Brain_Spinal_cord_cervical_c-1: NES +0.72, p 2.7e-06
> DIEXF in Lung: NES -0.11, p 3.2e-06
> IRF6 in Brain_Cerebellar_Hemisphere: NES -0.61, p 3.3e-06
> DIEXF in Brain_Frontal_Cortex_BA9: NES +0.35, p 4.6e-06
> DIEXF in Brain_Cortex: NES +0.33, p 7.0e-06
> DIEXF in Adipose_Visceral_Omentum: NES -0.16, p 2.5e-05
> C1orf74 in Whole_Blood: NES +0.15, p 8.6e-05

<a id="e09"></a>**E09** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=UTP25%20AND%20%22cleft%20lip%22&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T20:21:47+00:00)

> Europe PMC: 7 hits for 'UTP25 AND "cleft lip"'; top 6 with PMIDs:
> PMID 42873673 (2026): Genetic Heterogeneity in Cleft Lip and/or Palate With Alveolar Cleft: A Targeted Analysis of NHEK-Active Enhancer Variants.
> PMID 41075272 (2025): Genetic heterogeneity and homogeneity among orofacial cleft subtypes: genome-wide association studies in the cleft collective.
> PMID 37161310 (2023): A Variant in the <i>IRF6</i> Promoter Associated with the Risk for Orofacial Clefting.
> PMID 40670354 (2025): Identification of functional non-coding variants associated with orofacial cleft.
> PMID 33987535 (2021): Wavelet Screening identifies regions highly enriched for differentially methylated loci for orofacial clefts.
> PMID 30760477 (2019): Wnt signaling in orofacial clefts: crosstalk, pathogenesis and models.

<a id="e10"></a>**E10** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> QBiC-SELEX screen of chr1:209815925:A>G, one line per TF, each with the TF's own or CIS-BP-mapped model of largest |z|. Candidates are TFs whose ENCODE ChIP-seq peaks contain the variant and that are expressed (none: expression filter skipped), bound here before bound elsewhere, then a strong site before a weak one, then by |z|; then expressed TFs ENCODE never assayed whose best model passes the gate (occupancy unknown). Shown: 1 of 1 occupied (0 with a strong site), 5 of 249 with unknown occupancy. Left out: 0 TFs assayed in the matching biosample and 572 assayed only elsewhere, none with a peak here. The gate (|z| > 4.05, Bonferroni over 997 models) marks a change QBiC-SELEX detects; it says nothing about occupancy. Effect > 0 means the alternate allele binds more strongly. In vitro binding only. Site strength is the better allele's best k-mer over the variant, as a percentile of the best model's k-mers; a strong site reaches the 97.5th. At a weak site the ChIP peak more likely reflects another site in the element. No occupied TF has a strong site at the variant.

<a id="e11"></a>**E11** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> ZNF687 (C2H2 ZF, 1 model; QBiC-SELEX coverage: own model): best model ZNF687_FL_TA40NGTTAGC_YWL_jolma2025_0_3_7mer (its own model), z -0.21, effect -0.013: ref allele binds slightly more; occupied, no clear allelic change (|z| below the gate). expression not filtered. Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in GM12878, e.g. ENCSR859FDL. Best model's site strength: ref 92.7th, alt 88.6th percentile of its k-mer coefficients: a weak site (neither allele reaches the 97.5th), so the ChIP peak more likely reflects another site in the element.

<a id="e12"></a>**E12** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> ETV2 (Ets, 18 models; QBiC-SELEX coverage: own model): best model ETV5_NA_TGCACT20NGA_ESAF_yang2017_1_3_6mer (a CIS-BP-mapped model of ETV5), z 77.65, effect 1.32: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). expression not filtered. Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 65.0th, alt 99.2th percentile of its k-mer coefficients.

<a id="e13"></a>**E13** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> ETV3 (Ets, 18 models; QBiC-SELEX coverage: own model): best model ETV5_NA_TGCACT20NGA_ESAF_yang2017_1_3_6mer (a CIS-BP-mapped model of ETV5), z 77.65, effect 1.32: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). expression not filtered. Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 65.0th, alt 99.2th percentile of its k-mer coefficients.

<a id="e14"></a>**E14** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> ETV3L (Ets, 18 models; QBiC-SELEX coverage: mapped models only): best model ETV5_NA_TGCACT20NGA_ESAF_yang2017_1_3_6mer (a CIS-BP-mapped model of ETV5), z 77.65, effect 1.32: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). expression not filtered. Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 65.0th, alt 99.2th percentile of its k-mer coefficients.

<a id="e15"></a>**E15** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> FEV (Ets, 18 models; QBiC-SELEX coverage: own model): best model ETV5_NA_TGCACT20NGA_ESAF_yang2017_1_3_6mer (a CIS-BP-mapped model of ETV5), z 77.65, effect 1.32: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). expression not filtered. Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 65.0th, alt 99.2th percentile of its k-mer coefficients.

<a id="e16"></a>**E16** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> FLI1 (Ets, 18 models; QBiC-SELEX coverage: own model): best model ETV5_NA_TGCACT20NGA_ESAF_yang2017_1_3_6mer (a CIS-BP-mapped model of ETV5), z 77.65, effect 1.32: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). expression not filtered. Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 65.0th, alt 99.2th percentile of its k-mer coefficients.

<a id="e17"></a>**E17** qbic_tf_detail, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> {"tf":"FLI1","symbol":"FLI1","via":"hgnc_symbol","notes":[],"coverage":"own_model","variant":"chr1:209815925:A>G","gate_p":5.02e-05,"models":[{"model":"FLI1_NA_TAGGAT20NAGT_AC_jolma2013_0_3_7mer","mapping":"own","group":"G003 Ets, 18 models","quality":0.864,"effect":0.906,"z":13.73,"p":6.3e-43,"rank_abs_z":"35/997","passed_gate":true,"site_strength":{"ref_percentile":90.1,"alt_percentile":98.7,"k":7}},{"model":"ELF1_FL_TATGAC40NTCA_KW_yin2017_0_2_7mer","mapping":"CIS-BP (ELF1)","group":"G003 Ets, 18 models","quality":0.615,"effect":0.239,"z":7.62,"p":2.6e-14,"rank_abs_z":"79/997","passed_gate":true,"site_strength":{"ref_percentile":92.4,"alt_percentile":97.9,"k":7}},{"model":"ELF2_eDBD_TGAAAT40NCAA_KR_yin2017_0_4_7mer","mapping":"CIS-BP (ELF2)","group":"G003 Ets, 18 models","quality":0.896,"effect":1.749,"z":14.38,"p":7.1e-47,"rank_abs_z":"32/997","passed_gate":true,"site_strength":{"ref_percentile":93.6,"alt_percentile":99.5,"k":7}},{"model":"ELF4_eDBD_TGCGGT40NTCA_KAN_yin2017_0_4_7mer","mapping":"CIS-BP (ELF4)","group":"G003 Ets, 18 models","quality":0.732,"effect":1.252,"z":16.42,"p":1.5e-60,"rank_abs_z":"25/997","passed_gate":true,"site_strength":{"ref_percentile":70.9,"alt_percentile":97.3,"k":7}},{"model":"ELK1_NA_TCGGAA20NAGT_ESAG_yang2017_1_3_7mer","mapping":"CIS-BP (ELK1)","group":"G003 Ets, 18 models","quality":0.779,"effect":0.448,"z":4.22,"p":2.5e-05,"rank_abs_z":"211/997","passed_gate":true,"site_strength":{"ref_percentile":66.4,"alt_percentile":97.4,"k":7}},{"model":"ELK3_FL_TTCGAA40NGAC_KX_yin2017_0_4_7mer","mapping":"CIS-BP (ELK3)","group":"G003 Ets, 18 models","quality":0.841,"effect":1.11,"z":12.98,"p":1.5e-38,"rank_abs_z":"38/997","passed_gate":true,"site_strength":{"ref_percentile":78.9,"alt_percentile":98.9,"k":7}},{"model":"ELK4_FL_TCCGCC40NTCA_KAE_yin2017_0_3_7mer","mapping":"CIS-BP (ELK4)","group":"G003 Ets, 18 models","quality":0.921,"effect":1.362,"z":17.75,"p":1.8e-70,"rank_abs_z":"20/997","passed_gate":true,"site_strength":{"ref_percentile":69.3,"alt_percentile":99.9,"k":7}},{"model":"ERF_NA_TCAGAG20NCG_ESW_yang2017_1_4_7mer","mapping":"CIS-BP (ERF)","group":"G003 Ets, 18 models","quality":0.729,"effect":0.234,"z":8.25,"p":1.6e-16,"rank_abs_z":"70/997","passed_gate":true,"site_strength":{"ref_percentile":91.2,"alt_percentile":99.7,"k":7}},{"model":"ERG_NA_TCTACA20NCAG_ESAG_yang2017_1_4_7mer","mapping":"CIS-BP (ERG)","group":"G003 Ets, 18 models","quality":0.881,"effect":1.053,"z":11.1,"p":1.2e-28,"rank_abs_z":"48/997","passed_gate":true,"site_strength":{"ref_percentile":85.0,"alt_percentile":99.4,"k":7}},{"model":"ETS1_NA_TGTAAA20NGA_ESAF_yang2017_0_4_7mer","mapping":"CIS-BP (ETS1)","group":"G003 Ets, 18 models","quality":0.873,"effect":1.634,"z":27.66,"p":2.2e-168,"rank_abs_z":"11/997","passed_gate":true,"site_strength":{"ref_percentile":80.1,"alt_percentile":99.6,"k":7}}],"n_models_trimmed":8}

<a id="e18"></a>**E18** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-26T20:42:12+00:00)

> No ENCODE FLI1 ChIP-seq peak contains chr1:209815925:A>G. Absence can also mean no FLI1 experiment in that biosample. 0 peaks lie within 100 bp without containing it.

<a id="e19"></a>**E19** tf_expression, DepMap expression / GTEx v8 medians (local files; retrieved local)

> FLI1 in GTEx tissue median Minor Salivary Gland: 8.27 TPM, rank 573 of 1631 TFs (1 = highest); this context is at the 51.9th percentile of FLI1 across all GTEx tissues.
