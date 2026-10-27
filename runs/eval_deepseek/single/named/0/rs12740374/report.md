# rs12740374 and LDL cholesterol, myocardial infarction (1p13)

Configuration `single`, named mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.01 over 2 model calls; 54 s.

Variant `chr1:109274968:G>T` (germline); expression context: DepMap:ACH-000625 (Hep 3B2.1-7).

## Ranked chains

### 1. chain1: CEBPA-SORT1 hepatocyte enhancer (p = 0.55)

TF CEBPA (stated coverage not_checked; registry own_model), alt allele binds more; element hepatocyte enhancer; gene SORT1; cell type hepatocyte.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | CEBPA (HGNC:CEBPA) binds the alt T allele of rs12740374 more strongly than the ref G allele, creating/strengthening a C/EBP site; QBiC-SELEX coverage is not_checked because no QBiC-SELEX evidence is supplied. CEBPA is chosen as the hepatic C/EBP-family member from prior literature/expression context, not from QBiC-SELEX. | missing | none |
| element | The rs12740374-containing sequence acts as a hepatocyte enhancer whose activity is higher on the alt T allele. | missing | none |
| gene | Higher enhancer activity increases SORT1 transcription. | missing | none |
| cell_type | This occurs in hepatocytes, consistent with the Hep 3B2.1-7 expression context. | missing | none |
| phenotype | Increased hepatic SORT1 lowers LDL cholesterol and myocardial infarction risk. | missing | none |

Predictions: alt T allele binds CEBPA more strongly than ref G; alt T increases enhancer activity in hepatocytes; alt T increases SORT1 mRNA in hepatocytes; alt T lowers LDL cholesterol and MI risk

Falsified if: No allele-specific CEBPA binding at rs12740374; No alt-T-dependent enhancer activity; No SORT1 expression difference in hepatocytes

### 2. null: Null: no TF-mediated effect of rs12740374 (p = 0.25)

Null chain: no TF-mediated effect of this variant.

Predictions: No allele-specific TF binding at rs12740374; No allele-specific enhancer activity or target-gene expression after controlling for linked variants; The 1p13 association is explained by a linked causal variant or by no direct allelic effect

Falsified if: Allele-specific CEBPA or CEBPB binding is demonstrated at rs12740374; Allele-specific SORT1 or PSRC1 expression is demonstrated in hepatocytes

### 3. chain2: CEBPB-SORT1 hepatocyte enhancer (p = 0.10)

TF CEBPB (stated coverage not_checked; registry own_model), alt allele binds more; element hepatocyte enhancer; gene SORT1; cell type hepatocyte.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | CEBPB (HGNC:CEBPB) binds the alt T allele of rs12740374 more strongly than the ref G allele; QBiC-SELEX coverage is not_checked because no QBiC-SELEX evidence is supplied. | missing | none |
| element | The rs12740374-containing sequence acts as a hepatocyte enhancer whose activity is higher on the alt T allele. | missing | none |
| gene | Higher enhancer activity increases SORT1 transcription. | missing | none |
| cell_type | This occurs in hepatocytes, consistent with the Hep 3B2.1-7 expression context. | missing | none |
| phenotype | Increased hepatic SORT1 lowers LDL cholesterol and myocardial infarction risk. | missing | none |

Predictions: alt T allele binds CEBPB more strongly than ref G; alt T increases enhancer activity in hepatocytes; alt T increases SORT1 mRNA in hepatocytes; alt T lowers LDL cholesterol and MI risk

Falsified if: No allele-specific CEBPB binding at rs12740374; CEBPA, not CEBPB, accounts for the allele-specific binding; No SORT1 expression difference in hepatocytes

### 4. chain3: CEBPA-PSRC1 hepatocyte enhancer (p = 0.10)

TF CEBPA (stated coverage not_checked; registry own_model), alt allele binds more; element hepatocyte enhancer; gene PSRC1; cell type hepatocyte.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | CEBPA (HGNC:CEBPA) binds the alt T allele of rs12740374 more strongly than the ref G allele; QBiC-SELEX coverage is not_checked because no QBiC-SELEX evidence is supplied. | missing | none |
| element | The rs12740374-containing sequence acts as a hepatocyte enhancer whose activity is higher on the alt T allele. | missing | none |
| gene | Higher enhancer activity increases PSRC1 transcription. | missing | none |
| cell_type | This occurs in hepatocytes, consistent with the Hep 3B2.1-7 expression context. | missing | none |
| phenotype | Altered hepatic PSRC1 expression lowers LDL cholesterol and myocardial infarction risk. | missing | none |

Predictions: alt T allele binds CEBPA more strongly than ref G; alt T increases enhancer activity in hepatocytes; alt T changes PSRC1 mRNA rather than SORT1 mRNA; alt T lowers LDL cholesterol and MI risk through PSRC1

Falsified if: No allele-specific CEBPA binding at rs12740374; SORT1, not PSRC1, mediates the expression effect; No PSRC1 expression difference in hepatocytes

## Prediction matrix

| Test | Cost | Separates top two | chain1 | null | chain2 | chain3 |
| --- | --- | --- | --- | --- | --- | --- |
| allele-specific EMSA supershift with anti-CEBPA vs anti-CEBPB at rs12740374 | low | yes | alt T probe supershifts with anti-CEBPA but not anti-CEBPB |  | alt T probe supershifts with anti-CEBPB but not anti-CEBPA |  |
| alt T increases enhancer reporter activity | low | no | alt T > ref G reporter activity | no allele-specific reporter activity | alt T > ref G reporter activity | alt T > ref G reporter activity |
| allele-specific SORT1 mRNA expression in Hep 3B2.1-7 | medium | no | alt T increases SORT1 mRNA | no SORT1 mRNA difference | alt T increases SORT1 mRNA | no SORT1 mRNA difference |

## Next experiment

allele-specific EMSA with Hep 3B2.1-7 nuclear extract and anti-CEBPA vs anti-CEBPB supershift

## Flags

- none

## Evidence
