# rs4784227 and Breast cancer (16q12)

Configuration `single`, named mode, seed 0. Models: generator claude-opus-5, critic claude-sonnet-5-5, summariser claude-haiku-5-5. Cost $0.14 over 1 model calls; 63 s.

Variant `chr16:52565276:C>T` (germline); expression context: DepMap:ACH-000019 (MCF7).

## Ranked chains

### 1. H1: Risk allele T creates a stronger forkhead site, increasing FOXA1 binding at the 16q12.1 TOX3 enhancer and raising TOX3 expression in luminal breast epithelium (p = 0.44)

TF FOXA1 (stated coverage not_checked; registry own_model), alt allele binds more; element Intergenic/intronic enhancer at chr16:52.56 Mb within the TOX3/CASC16 risk interval, active in ER+ luminal cells; gene TOX3; cell type Luminal (ER+) mammary epithelial cells, modelled by MCF7.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The T (risk) allele improves the match to a forkhead (FOX) core motif, so FOXA1 binds the T allele more strongly than the C allele; within the forkhead specificity group FOXA1 is chosen because it is the dominant, highly expressed pioneer forkhead factor in ER+ luminal breast cells (MCF7) and occupies this locus in ChIP-seq, unlike FOXA2/FOXO/FOXP members. | missing | none |
| element | The variant sits in a FOXA1/ER-bound distal enhancer that loops to the TOX3 promoter; stronger pioneer binding increases enhancer accessibility and activity on the risk haplotype. | missing | none |
| gene | Increased enhancer activity raises TOX3 expression (allele-specific expression favouring T has been reported at this locus). | missing | none |
| cell_type | The effect is restricted to luminal ER+ epithelium where FOXA1, GATA3 and ESR1 are co-expressed, consistent with the association being strongest for ER+ disease. | missing | none |
| phenotype | Altered TOX3 (a HMG-box chromatin protein) dosage changes luminal progenitor differentiation/survival programmes, modestly increasing ER+ breast cancer risk. | missing | none |

Predictions: FOXA1 ChIP or ChIP-allelic imbalance in heterozygous ER+ cells shows preferential pulldown of the T allele; FOXA1 knockdown abolishes the allelic difference in reporter/CRISPRi assays; EMSA with MCF7 nuclear extract gives a T-preferring complex supershifted by anti-FOXA1; TOX3 is the gene whose expression tracks genotype in ER+ tissue

Falsified if: No allelic imbalance in FOXA1 ChIP-seq across heterozygotes; Allelic reporter difference persists after FOXA1 depletion; Supershift identifies a non-forkhead factor

### 2. H4: Null: rs4784227 is not itself a TF-binding-altering causal variant (p = 0.30)

Null chain: no TF-mediated effect of this variant.

Predictions: No reproducible allelic imbalance in any TF ChIP at the site; No allelic difference in reporter or base-edited isogenic lines; A different variant in tight LD on the 16q12.1 haplotype shows the allelic enhancer effect

Falsified if: Base-edited isogenic clones differing only at rs4784227 show reproducible TOX3 expression and TF-occupancy differences

### 3. H2: The variant alters a GATA3 site, with the risk allele increasing GATA3 occupancy and TOX3 enhancer output (p = 0.14)

TF GATA3 (stated coverage not_checked; registry own_model), alt allele binds more; element Same 16q12.1 enhancer, which carries clustered GATA/FOX motifs in luminal cells; gene TOX3; cell type Luminal ER+ mammary epithelial cells (MCF7).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The T allele strengthens a GATA-like element; among GATA-group factors GATA3 is selected because it is the luminal-restricted GATA factor expressed in MCF7 and bound genome-wide with FOXA1/ESR1. | missing | none |
| element | GATA3 co-binds the same enhancer and is required for its activity, so an allelic gain of GATA3 binding raises enhancer strength. | missing | none |
| gene | Enhancer activation increases TOX3 (and possibly neighbouring CASC16) transcription. | missing | none |
| cell_type | GATA3 expression is confined to luminal epithelium, matching the ER+-specific association. | missing | none |
| phenotype | Higher TOX3 perturbs luminal lineage control and raises ER+ breast cancer risk. | missing | none |

Predictions: GATA3 ChIP shows allelic imbalance toward T while FOXA1 ChIP does not; GATA3 knockdown, not FOXA1 knockdown, removes the allelic reporter difference; Motif analysis scores the GATA change more strongly than the forkhead change

Falsified if: No GATA3 occupancy at the element; Allelic effect retained after GATA3 depletion

### 4. H3: The variant weakens a CTCF-anchored boundary/loop element, redistributing enhancer contacts within the 16q12.1 TAD (p = 0.12)

TF CTCF (stated coverage not_checked; registry own_model), ref allele binds more; element CTCF/cohesin-bound insulator in the TOX3/CASC16 interval; gene TOX3; cell type Mammary epithelial cells, including MCF7.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The C (non-risk) allele matches the CTCF core consensus better, so CTCF binds ref more strongly and binding is reduced on the risk haplotype. | missing | none |
| element | Loss of CTCF occupancy weakens a loop anchor, allowing distal luminal enhancers to contact the TOX3 promoter more freely. | missing | none |
| gene | Re-wired contacts raise TOX3 expression on the risk allele without a local change in enhancer strength. | missing | none |
| cell_type | Although CTCF is ubiquitous, the consequence is only seen where the relevant luminal enhancers are active. | missing | none |
| phenotype | Dysregulated TOX3 dosage contributes to ER+ breast cancer susceptibility. | missing | none |

Predictions: CTCF ChIP shows C-allele preference and a CTCF peak overlapping the variant; 4C/Hi-C shows genotype-dependent loop structure; Reporter assays in episomal context show no allelic difference (effect is chromatin-contextual)

Falsified if: No CTCF peak at the variant in breast cells; Episomal/STARR reporter shows a clear allelic difference in the FOXA1-dependent direction

### 5. H5: Risk allele increases binding of an ETS factor (ELF/EHF family) at the element, acting on CASC16/TOX3 (p = 0.00)

TF ELF3 (stated coverage not_checked; registry own_model), alt allele binds more; element Epithelial enhancer in the 16q12.1 interval; gene CASC16; cell type Mammary epithelial cells (MCF7).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The T allele could complete a GGAA ETS core; within the ETS epithelial group ELF3 is chosen as the epithelium-restricted member highly expressed in mammary luminal cells. | missing | none |
| element | ELF3 binding activates the nearby epithelial enhancer. | missing | none |
| gene | The primary transcriptional output is the lncRNA CASC16 rather than TOX3. | missing | none |
| cell_type | ELF3 expression is epithelium-specific, so the effect is confined to mammary epithelium. | missing | none |
| phenotype | Altered CASC16 levels modulate TOX3 regulation in cis and breast cancer risk. | missing | none |

Predictions: ELF3 ChIP shows T-allele preference; CASC16, not TOX3, is the eQTL target in breast tissue

Falsified if: No ETS motif match or ELF3 occupancy at the variant; TOX3 is the only genotype-associated transcript

## Prediction matrix

| Test | Cost | Separates top two | H1 | H4 | H2 | H3 | H5 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Allele-specific ChIP-seq/ChIP-qPCR for FOXA1, GATA3 and CTCF in heterozygous ER+ breast cells | medium | yes | FOXA1 reads favour T; GATA3/CTCF balanced or secondary | No imbalance for any factor | GATA3 reads favour T; FOXA1 balanced | CTCF reads favour C | No imbalance for these factors |
| EMSA with MCF7 nuclear extract using C and T probes, plus anti-FOXA1 and anti-GATA3 supershift | low | yes | T probe binds more; complex supershifted by anti-FOXA1 | No allelic difference in binding | T probe binds more; complex supershifted by anti-GATA3 | C probe binds more; neither antibody shifts | T probe binds more; neither antibody shifts |
| Luciferase reporter with C vs T element in MCF7, with and without FOXA1 or GATA3 siRNA | low | yes | T > C activity, lost on FOXA1 knockdown | No allelic difference | T > C activity, lost on GATA3 knockdown | No allelic difference episomally | T > C, unaffected by FOXA1/GATA3 knockdown |
| CRISPR base editing of rs4784227 in isogenic MCF7, then TOX3/CASC16 RT-qPCR | high | no | T clones show higher TOX3 | No expression change | T clones show higher TOX3 | T clones show higher TOX3 with altered local looping | CASC16 changes more than TOX3 |
| QBiC-SELEX lookup of FOXA1, GATA3 and CTCF models at this variant | existing data | yes | Forkhead model predicts gain of binding on T | No model predicts a meaningful change | GATA model predicts gain on T | CTCF model predicts loss on T | ETS model predicts gain on T |

## Next experiment

EMSA with MCF7 nuclear extract on matched C and T probes with anti-FOXA1 and anti-GATA3 supershifts: cheap, fast, and it directly distinguishes a FOXA1-driven T-preferring complex (H1) from a GATA3-driven one (H2), while a complete absence of allelic binding difference would support the null.

## Flags

- none

## Evidence
