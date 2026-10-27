# rs12740374 and LDL cholesterol, myocardial infarction (1p13)

Configuration `single`, named mode, seed 0. Models: generator openai/gpt-6-luna, critic openai/gpt-6-luna, summariser openai/gpt-6-luna. Cost $0.00 over 1 model calls; 52 s.

Variant `chr1:109274968:G>T` (germline); expression context: DepMap:ACH-000625 (Hep 3B2.1-7).

## Ranked chains

### 1. H1: T allele creates an activating CEBPA-dependent SORT1 enhancer (p = 0.70)

TF CEBPA (QBiC-SELEX coverage own_model), alt allele binds more; element The variant lies in a liver-active regulatory element whose activity is increased by CEBPA binding.; gene SORT1; cell type Hepatocytes.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The alt T allele is expected to bind CEBPA more strongly; CEBPA is favored over related C/EBP factors because it is the TF associated with the established rs12740374 mechanism. No QBiC-SELEX result or model status is available in the supplied case. | missing | none |
| element | The variant is in a regulatory element that can act as a liver enhancer, and stronger CEBPA binding on T is expected to increase its activity. | missing | none |
| gene | The enhancer increases SORT1 expression. | missing | none |
| cell_type | The regulatory effect occurs primarily in hepatocytes. | missing | none |
| phenotype | Increased hepatic SORT1 lowers circulating LDL cholesterol and is expected to reduce myocardial-infarction risk. | missing | none |

Predictions: In heterozygous hepatocytes, CEBPA occupancy at the variant should be greater on T than G.; Replacing G with T should increase SORT1 expression and reduce a measure of hepatic lipoprotein output.

Falsified if: There is no reproducible T-biased CEBPA occupancy in an appropriate hepatocyte context.; An endogenous G-to-T edit does not increase SORT1 expression.

### 2. H2: A related C/EBP factor, CEBPB, mediates the enhancer effect (p = 0.13)

TF CEBPB (QBiC-SELEX coverage own_model), alt allele binds more; element The variant is in a liver-active regulatory element whose activity is increased by CEBPB binding.; gene SORT1; cell type Hepatocytes.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The alt T allele is hypothesized to bind CEBPB more strongly; this is a competing possibility because related C/EBP factors can recognize similar sequences, but no QBiC-SELEX result or model status is available here. | missing | none |
| element | The variant-containing element acts as a liver enhancer when occupied by CEBPB. | missing | none |
| gene | The enhancer increases SORT1 expression. | missing | none |
| cell_type | The regulatory effect occurs primarily in hepatocytes. | missing | none |
| phenotype | Increased hepatic SORT1 lowers circulating LDL cholesterol and is expected to reduce myocardial-infarction risk. | missing | none |

Predictions: In heterozygous hepatocytes, CEBPB occupancy should be greater on T than G and more informative than CEBPA occupancy.; Reducing CEBPB should weaken the T-allele effect on SORT1 expression.

Falsified if: CEBPB shows no T-biased occupancy while CEBPA shows clear T-biased occupancy.; Reducing CEBPB does not alter the allele-dependent SORT1 response.

### 3. H0: Null: no TF-mediated effect of rs12740374 (p = 0.10)

Null chain: no TF-mediated effect of this variant.

Predictions: The variant will not show a reproducible allele-specific TF occupancy or endogenous regulatory effect; the association could reflect linkage or another explanation.

Falsified if: An endogenous allele swap produces a reproducible, allele-dependent TF occupancy change and corresponding expression change.

### 4. H3: CEBPA binds the T allele but represses SORT1 (p = 0.07)

TF CEBPA (QBiC-SELEX coverage own_model), alt allele binds more; element The variant-containing regulatory element acts as a CEBPA-dependent repressor of SORT1.; gene SORT1; cell type Hepatocytes.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The alt T allele is hypothesized to bind CEBPA more strongly; no QBiC-SELEX result or model status is available in the supplied case. | missing | none |
| element | At this element, increased CEBPA binding is hypothesized to reduce rather than increase regulatory activity. | missing | none |
| gene | The repressive element lowers SORT1 expression. | missing | none |
| cell_type | The regulatory effect occurs primarily in hepatocytes. | missing | none |
| phenotype | Lower hepatic SORT1 is hypothesized to raise LDL cholesterol and myocardial-infarction risk. | missing | none |

Predictions: T should show greater CEBPA occupancy than G, but endogenous T should reduce SORT1 expression.; A G-to-T edit should increase LDL-related lipoprotein output, opposite to H1.

Falsified if: A G-to-T edit increases SORT1 expression in hepatocytes.; The T allele does not show greater CEBPA occupancy in an appropriate hepatocyte context.

## Prediction matrix

| Test | Cost | Separates top two | H1 | H2 | H0 | H3 |
| --- | --- | --- | --- | --- | --- | --- |
| Allele-specific CUT&RUN-qPCR for CEBPA and CEBPB at the variant in heterozygous hepatocytes | low | yes | T-biased CEBPA occupancy, stronger than any T-biased CEBPB signal. | T-biased CEBPB occupancy, stronger than any T-biased CEBPA signal. | No reproducible allele-specific occupancy for either factor. | T-biased CEBPA occupancy; occupancy alone does not establish whether CEBPA activates or represses. |
| Endogenous G-to-T allele swap in a hepatocyte model followed by SORT1 expression measurement | medium | no | SORT1 expression increases. | SORT1 expression increases, with the response dependent on CEBPB. | No reproducible expression change. | SORT1 expression decreases. |

## Next experiment

Perform allele-specific CUT&RUN-qPCR for CEBPA and CEBPB at rs12740374 in heterozygous hepatocytes. It is the cheapest proposed test that distinguishes the leading CEBPA chain from the CEBPB alternative.

## Flags

- none

## Evidence
