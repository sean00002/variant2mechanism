# rs12740374 and LDL cholesterol, myocardial infarction (1p13)

Configuration `single`, named mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.01 over 2 model calls; 67 s.

Variant `chr1:109274968:G>T` (germline); expression context: DepMap:ACH-000625 (Hep 3B2.1-7).

## Ranked chains

### 1. H1: CEBPA binds the alt T allele and activates SORT1 in hepatocytes (p = 0.46)

TF CEBPA (stated coverage not_checked; registry own_model), alt allele binds more; element Hepatocyte-active enhancer-like element at rs12740374; gene SORT1; cell type Hepatocyte (Hep3B2.1-7).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The alt T allele at rs12740374 binds CEBPA more strongly than the ref G allele. | missing | none |
| element | rs12740374 lies in a hepatocyte-active enhancer-like element whose activity is higher on the T allele. | missing | none |
| gene | The rs12740374 enhancer regulates SORT1 expression, with the T allele increasing SORT1 in hepatocytes. | missing | none |
| cell_type | The effect is operative in hepatocytes, consistent with Hep3B2.1-7 expression context. | missing | none |
| phenotype | Altered hepatocyte SORT1 expression changes plasma LDL cholesterol and myocardial infarction risk. | missing | none |

Predictions: Alt T allele binds CEBPA more strongly than ref G at rs12740374 in Hep3B.; The rs12740374 T allele increases enhancer/reporter activity in hepatocytes.; T-allele increased CEBPA binding increases SORT1 expression in hepatocytes.; CEBPA knockdown reduces T-allele reporter activity and SORT1 expression in Hep3B.

Falsified if: CEBPA does not bind the T allele more than G in Hep3B.; CEBPA knockdown does not reduce T-allele reporter activity or SORT1 expression.

### 2. H0: Null: no TF-mediated effect of rs12740374 (p = 0.26)

Null chain: no TF-mediated effect of this variant.

Predictions: No allele-specific TF binding at rs12740374.; No allele-specific enhancer activity attributable to rs12740374.; Any SORT1/LDL/MI association is due to a linked causal variant or another mechanism.

Falsified if: Allele-specific C/EBP binding and an rs12740374-dependent enhancer/SORT1 effect are demonstrated.

### 3. H2: CEBPB binds the alt T allele and activates SORT1 in hepatocytes (p = 0.20)

TF CEBPB (stated coverage not_checked; registry own_model), alt allele binds more; element Hepatocyte-active enhancer-like element at rs12740374; gene SORT1; cell type Hepatocyte (Hep3B2.1-7).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The alt T allele at rs12740374 binds CEBPB more strongly than the ref G allele. | missing | none |
| element | rs12740374 lies in a hepatocyte-active enhancer-like element whose activity is higher on the T allele. | missing | none |
| gene | The rs12740374 enhancer regulates SORT1 expression, with the T allele increasing SORT1 in hepatocytes. | missing | none |
| cell_type | The effect is operative in hepatocytes, consistent with Hep3B2.1-7 expression context. | missing | none |
| phenotype | Altered hepatocyte SORT1 expression changes plasma LDL cholesterol and myocardial infarction risk. | missing | none |

Predictions: Alt T allele binds CEBPB more strongly than ref G at rs12740374 in Hep3B.; The rs12740374 T allele increases enhancer/reporter activity in hepatocytes.; T-allele increased CEBPB binding increases SORT1 expression in hepatocytes.; CEBPB knockdown reduces T-allele reporter activity and SORT1 expression in Hep3B.

Falsified if: CEBPB does not bind the T allele more than G in Hep3B.; CEBPB knockdown does not reduce T-allele reporter activity or SORT1 expression.

### 4. H3: CEBPD binds the alt T allele and activates SORT1 in hepatocytes (p = 0.08)

TF CEBPD (stated coverage not_checked; registry own_model), alt allele binds more; element Hepatocyte-active enhancer-like element at rs12740374; gene SORT1; cell type Hepatocyte (Hep3B2.1-7).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The alt T allele at rs12740374 binds CEBPD more strongly than the ref G allele. | missing | none |
| element | rs12740374 lies in a hepatocyte-active enhancer-like element whose activity is higher on the T allele. | missing | none |
| gene | The rs12740374 enhancer regulates SORT1 expression, with the T allele increasing SORT1 in hepatocytes. | missing | none |
| cell_type | The effect is operative in hepatocytes, consistent with Hep3B2.1-7 expression context. | missing | none |
| phenotype | Altered hepatocyte SORT1 expression changes plasma LDL cholesterol and myocardial infarction risk. | missing | none |

Predictions: Alt T allele binds CEBPD more strongly than ref G at rs12740374 in Hep3B.; The rs12740374 T allele increases enhancer/reporter activity in hepatocytes.; T-allele increased CEBPD binding increases SORT1 expression in hepatocytes.; CEBPD knockdown reduces T-allele reporter activity and SORT1 expression in Hep3B.

Falsified if: CEBPD does not bind the T allele more than G in Hep3B.; CEBPD knockdown does not reduce T-allele reporter activity or SORT1 expression.

## Prediction matrix

| Test | Cost | Separates top two | H1 | H0 | H2 | H3 |
| --- | --- | --- | --- | --- | --- | --- |
| Anti-CEBPA ChIP-qPCR at rs12740374 in Hep3B | low | yes |  |  |  |  |
| Anti-CEBPB ChIP-qPCR at rs12740374 in Hep3B | low | yes |  |  |  |  |
| Allele-specific EMSA supershift with anti-CEBPA vs anti-CEBPB in Hep3B extract | low | yes |  |  |  |  |
| siCEBPA vs siCEBPB in Hep3B T-allele reporter | medium | yes |  |  |  |  |

## Next experiment

Allele-specific EMSA with Hep3B nuclear extract using ref-G and alt-T oligos, followed by anti-CEBPA versus anti-CEBPB supershift; this separates the top two TF chains.

## Flags

- none

## Evidence
