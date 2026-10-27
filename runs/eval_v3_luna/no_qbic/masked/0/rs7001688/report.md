# rs7001688 and LDL cholesterol

Configuration `no_qbic`, masked mode, seed 0. Models: generator openai/gpt-6-luna, critic openai/gpt-6-luna, summariser openai/gpt-6-luna. Cost $0.01 over 8 model calls; 143 s.

Variant `chr8:57573391:G>T` (germline); expression context: DepMap:ACH-000625 (Hep 3B2.1-7).

## Ranked chains

### 1. H0: No TF-mediated effect of this variant (p = 0.95)

Null chain: no TF-mediated effect of this variant.

Predictions: The variant has no consequential allele-specific TF-mediated effect; any LDL-C association is due to another variant or mechanism, or the variant has no effect on LDL-C.; The variant does not reproducibly alter CTCF occupancy or expression of either CYP7A1 or FAM110B in relevant liver cells.

Falsified if: In relevant liver cells, the variant reproducibly changes allele-specific TF occupancy and variant editing changes a target gene in a way that supports a linked LDL-C effect.

### 2. H1: Hypothetical CTCF effect on CYP7A1 regulation (p = 0.04)

TF CTCF (QBiC-SELEX coverage own_model), alt allele binds more; element A possible CTCF-associated element overlapping the variant; its regulatory function in liver cells is unestablished.; gene CYP7A1; cell type Hep 3B2.1-7.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | This low-confidence subhypothesis assigns stronger CTCF binding to T than G. No QBiC-SELEX allele-effect result for CTCF is supplied, and the ChIP evidence shows occupancy only in LNCaP, not the matching HepG2 biosample; the direction is not supported by the evidence. | missing | [E04](#e04), [E05](#e05) |
| element | The variant overlaps a CTCF ChIP peak in LNCaP, but no cCRE overlaps it and this does not establish a functional regulatory element in liver cells. | weak | [E03](#e03), [E05](#e05) |
| gene | CYP7A1 is a distant candidate, about 927 kb away; no evidence connects this site to its regulation. The variant annotation is also inconsistent, reporting intronic consequence but no transcript consequences and describing the site as intergenic. | weak | [E01](#e01), [E02](#e02) |
| cell_type | Hep 3B2.1-7 is the proposed context and expresses CTCF, but matching HepG2 ChIP-seq has no peak at the variant; occupancy or activity in this context is not established. | supported | [E04](#e04), [E05](#e05) |
| phenotype | CYP7A1 has a plausible connection to LDL-C: cited mouse studies report that restoring CYP7A1 can reduce plasma LDL-C and that CYP7A1 mediates an LDL-C effect. This does not connect this variant or a regulatory effect at this site to LDL-C; the supplied Open Targets query reports no association with free cholesterol in large LDL. | supported | [E11](#e11), [E12e](#e12e), [E12f](#e12f) |

Predictions: In relevant liver cells, allele-specific CTCF occupancy at the variant is greater on T than G.; Editing the variant changes CYP7A1 expression, whereas it does not produce the FAM110B-specific expression effect predicted by H2.

Falsified if: A sufficiently powered allele-specific assay in relevant liver cells finds no T-over-G CTCF occupancy difference.; Variant editing has no reproducible effect on CYP7A1 expression.

### 3. H2: Hypothetical CTCF effect on FAM110B regulation (p = 0.01)

TF CTCF (QBiC-SELEX coverage own_model), alt allele binds more; element A possible CTCF-associated element overlapping the variant; its regulatory function in liver cells is unestablished.; gene FAM110B; cell type Hep 3B2.1-7.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | This low-confidence subhypothesis also assigns stronger CTCF binding to T than G. No QBiC-SELEX allele-effect result for CTCF is supplied, and the ChIP evidence shows occupancy only in LNCaP, not the matching HepG2 biosample; the direction is not supported by the evidence. | missing | [E04](#e04), [E05](#e05) |
| element | The variant overlaps a CTCF ChIP peak in LNCaP, but no cCRE overlaps it and this does not establish a functional regulatory element in liver cells. | weak | [E03](#e03), [E05](#e05) |
| gene | FAM110B is about 421 kb away and is a candidate based on proximity. A literature search found a study of variants associated with differential cardiovascular event reduction by pravastatin, but this does not establish regulation of FAM110B by this site or an LDL-C mechanism. | weak | [E02](#e02), [E09](#e09) |
| cell_type | Hep 3B2.1-7 is the proposed context and expresses CTCF, but matching HepG2 ChIP-seq has no peak at the variant; occupancy or activity in this context is not established. | supported | [E04](#e04), [E05](#e05) |
| phenotype | The supplied FAM110B literature result concerns differential cardiovascular event reduction by pravastatin, not a demonstrated FAM110B-to-LDL-C mechanism or an effect of this variant. | missing | [E09](#e09) |

Predictions: In relevant liver cells, allele-specific CTCF occupancy at the variant is greater on T than G.; Variant editing changes FAM110B expression, whereas it does not produce the CYP7A1-specific expression effect predicted by H1.

Falsified if: A sufficiently powered allele-specific assay in relevant liver cells finds no T-over-G CTCF occupancy difference.; Variant editing has no reproducible effect on FAM110B expression.

## Prediction matrix

| Test | Cost | Separates top two | H0 | H1 | H2 |
| --- | --- | --- | --- | --- | --- |
| Measure allele-specific CTCF occupancy at the variant in a relevant liver-cell model, using targeted CUT&RUN or ChIP-qPCR. | low | yes | Predicts no consequential allele-specific CTCF occupancy difference. | Predicts greater CTCF occupancy on T than G. | Predicts greater CTCF occupancy on T than G. |
| Edit the variant in an appropriate liver-cell model and measure CYP7A1 and FAM110B expression. | medium | no | Predicts no reproducible variant-dependent effect on either gene. | Predicts a reproducible CYP7A1 expression effect. | Predicts a reproducible FAM110B expression effect. |
| Test whether variant editing changes an LDL-related cellular phenotype, alongside gene-expression measurements. | high | no | Predicts no reproducible variant-dependent LDL-related effect. | Predicts an LDL-related effect accompanied by a CYP7A1 expression change. | Predicts an LDL-related effect accompanied by a FAM110B expression change. |

## Next experiment

Perform targeted allele-specific CTCF CUT&RUN or ChIP-qPCR at the variant in a relevant liver-cell model. It is the cheapest listed test that separates the two highest-probability chains, H0 and H1.

## Investigate calls

- eqtl_lookup({"tissue": "Liver"})
- gene_disease({"gene": "CYP7A1"})
- literature_search({"query": "CYP7A1 LDL cholesterol"})

## Flags

- none

Citation support: 1.00 of links cite only evidence that passed every check.

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

<a id="e04"></a>**E04** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> ENCODE TF ChIP-seq at chr8:57573391:G>T: 1 peaks contain the variant, from 1 factors in 1 biosamples. In the matching biosample HepG2 (HepG2 stands in for Hep 3B2.1-7 (both liver cancer lines)): 0 peaks from 0 factors. No cCRE contains the variant. Bound factors outside the TF model collection (co-factors, Pol II, and TFs with no binding model; signs of an active element, not TF candidates): none. Bound, expressed TFs with a binding model: 1; listed one per row: CTCF. Assayed with no peak here: 382 TFs in the matching biosample, 190 only elsewhere; never assayed: 536.

<a id="e05"></a>**E05** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> CTCF: bound elsewhere. 1 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: LNCAP (e.g. ENCSR673WZL). 32.01 TPM in DepMap:ACH-000625 (Hep 3B2.1-7), rank 162 of 1626 TFs.

<a id="e06"></a>**E06** gwas_lookup, GWAS Catalog REST v2 (https://www.ebi.ac.uk/gwas/rest/api/v2/associations?rs_id=rs7001688&size=100; retrieved 2026-10-25T17:33:20+00:00)

> 0 GWAS Catalog associations for rs7001688, strongest first:

<a id="e07"></a>**E07** finemap_lookup, Open Targets Platform (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-25T17:33:20+00:00)

> Open Targets has no record of 8_57573391_G_T.

<a id="e08"></a>**E08** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr8_57573391_G_T_b38&datasetId=gtex_v8; retrieved 2026-10-25T17:34:31+00:00)

> 0 significant GTEx v8 single-tissue eQTLs for chr8_57573391_G_T_b38. NES is the effect of the alt allele (T) relative to ref (G).

<a id="e09"></a>**E09** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=FAM110B%20AND%20%22ldl%20cholesterol%22&format=json&pageSize=8&resultType=core; retrieved 2026-10-25T17:33:21+00:00)

> Europe PMC: 1 hits for 'FAM110B AND "ldl cholesterol"'; top 1 with PMIDs:
> PMID 22666496 (2012): Genome-wide study of gene variants associated with differential cardiovascular event reduction by pravastatin therapy.

<a id="e10"></a>**E10** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr8_57573391_G_T_b38&datasetId=gtex_v8; retrieved 2026-10-25T17:34:31+00:00)

> 0 significant GTEx v8 single-tissue eQTLs for chr8_57573391_G_T_b38 in tissues matching 'Liver'. NES is the effect of the alt allele (T) relative to ref (G).

<a id="e11"></a>**E11** gene_disease, Open Targets Platform (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-25T17:34:31+00:00)

> Open Targets: no association between CYP7A1 and free cholesterol in large LDL measurement (EFO_0022176).

<a id="e12"></a>**E12** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=CYP7A1%20LDL%20cholesterol&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T20:24:27+00:00)

> Europe PMC: 3955 hits for 'CYP7A1 LDL cholesterol'; top 6 with PMIDs:
> PMID 42754810 (2026): CRISPR/dCas9-induced upregulation of endogenous apolipoprotein A1 and paraoxonase 1 genes reduces the aortic lipid deposits in apoE&lt;sup&gt;-/-&lt;/sup&gt; mice.
> PMID 42650834 (2026): Freeze-Dried &lt;i&gt;Poecilobdella manillensis&lt;/i&gt; Powder Regulates Cholesterol Homeostasis to Alleviate Hyperlipidemia.
> PMID 42796552 (2026): Modulation of Hepatic Cholesterol-Related Pathways by &lt;i&gt;Ophiocordyceps sinensis&lt;/i&gt; and Coenzyme Q10 in a Sequential Gut-Liver In Vitro Model.
> PMID 42397177 (2026): HDAC9 promotes atherosclerosis by suppressing CYP7A1 and impairing hepatic cholesterol excretion.
> PMID 42721809 (2026): Thermosonication-induced structural remodeling of faba bean protein: Improved functionality, digestibility, and cholesterol metabolism regulation for cardiovascular health.
> PMID 42819684 (2026): &lt;i&gt;Lactobacillus plantarum&lt;/i&gt; and &lt;i&gt;Bacillus licheniformis&lt;/i&gt; Ameliorate High-Carbohydrate-High-Fat-Induced Glycolipid Disorders in Common Carp in Association With the Gut Microbiota and Bile Acid Axis.

<a id="e12a"></a>**E12a** literature_search, Europe PMC abstract, PMID 42754810 (https://europepmc.org/article/MED/42754810; retrieved 2026-10-26T20:24:27+00:00)

> These mice also exhibited high levels of hepatic, gallbladder and feces cholesterol, in part due to the upregulation of hepatic scavenger receptor class-B1, cholesterol 7-alpha-hydroxylase, and ATP-binding cassette sub-family-G-member-8 transporter.

<a id="e12b"></a>**E12b** literature_search, Europe PMC abstract, PMID 42650834 (https://europepmc.org/article/MED/42650834; retrieved 2026-10-26T20:24:27+00:00)

> FDPMP administration significantly improved serum lipid profiles by reducing triglycerides, total cholesterol, and low-density lipoprotein cholesterol, while increasing high-density lipoprotein cholesterol levels.

<a id="e12c"></a>**E12c** literature_search, Europe PMC abstract, PMID 42650834 (https://europepmc.org/article/MED/42650834; retrieved 2026-10-26T20:24:27+00:00)

> Mechanistically, FDPMP restored cholesterol homeostasis through dual regulation of cholesterol metabolism, characterized by upregulation of cholesterol 7α-hydroxylase (CYP7A1) to promote bile acid-mediated cholesterol excretion, alongside downregulation of 3-hydroxy-3-methylglutaryl-CoA reductase (HMGCR) and synthase (HMGCS1) to inhibit cholesterol biosynthesis.

<a id="e12d"></a>**E12d** literature_search, Europe PMC abstract, PMID 42796552 (https://europepmc.org/article/MED/42796552; retrieved 2026-10-26T20:24:27+00:00)

> These functional outcomes were accompanied by coordinated changes in protein abundance: a decrease in sterol regulatory element-binding protein 2 (SREBP-2), 3-hydroxy-3-methylglutaryl-CoA reductase (HMGR), and proprotein convertase subtilisin/kexin type 9 (PCSK9) levels, alongside increased low-density lipoprotein receptor (LDLR), cytochrome P450 family 7 subfamily A member 1 (CYP7A1), and ATP-binding cassette transporter A1 (ABCA1) expression.

<a id="e12e"></a>**E12e** literature_search, Europe PMC abstract, PMID 42397177 (https://europepmc.org/article/MED/42397177; retrieved 2026-10-26T20:24:27+00:00)

> Pharmacological inhibition of HDAC9 (TMP195) or liver-targeted AAV8-shHdac9 knockdown restored CYP7A1 expression, reduced plasma LDL-C, and attenuated aortic plaque burden in HFD-fed ApoE-/- mice.

<a id="e12f"></a>**E12f** literature_search, Europe PMC abstract, PMID 42397177 (https://europepmc.org/article/MED/42397177; retrieved 2026-10-26T20:24:27+00:00)

> Mechanistically, HDAC9 transcriptionally represses Cyp7a1, as the cholesterol-lowering effect of Hdac9 knockdown was abolished by concomitant Cyp7a1 silencing.

<a id="e12g"></a>**E12g** literature_search, Europe PMC abstract, PMID 42721809 (https://europepmc.org/article/MED/42721809; retrieved 2026-10-26T20:24:27+00:00)

> The expression analyses further confirmed that UH-FPI upregulated the expression of cholesterol efflux-related proteins (ABCG5 and ABCG8), hepatic cholesterol metabolism regulators (LXR-α, CYP7A1, and LDL-R), and downregulated the expression of the intestinal cholesterol uptake-related protein NPC1L1 upon normalization with the HF group.
