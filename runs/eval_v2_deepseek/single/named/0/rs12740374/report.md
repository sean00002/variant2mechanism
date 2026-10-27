# rs12740374 and LDL cholesterol, myocardial infarction (1p13)

Configuration `single`, named mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.00 over 1 model calls; 43 s.

Variant `chr1:109274968:G>T` (germline); expression context: DepMap:ACH-000625 (Hep 3B2.1-7).

## Ranked chains

### 1. C1: Alt T creates a hepatocyte CEBPA site that raises SORT1 and lowers LDL/MI risk (p = 0.55)

TF CEBPA (QBiC-SELEX coverage own_model), alt allele binds more; element 1p13 hepatocyte enhancer; gene SORT1; cell type hepatocyte.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | Alt T binds CEBPA more strongly than ref G; the alt allele creates a C/EBP-family motif. CEBPA is chosen over related C/EBP factors from hepatic expression and published C/EBP occupancy at this 1p13 element. No QBiC-SELEX model is supplied, so this is not based on another TF's SELEX change. | missing | none |
| element | The variant lies in a hepatocyte regulatory element/enhancer in the 1p13 locus, not a coding change; the alt allele increases element activity. | missing | none |
| gene | The alt allele increases SORT1 transcript levels in hepatocytes. | missing | none |
| cell_type | The effect occurs in hepatocytes, the liver cell type relevant to LDL clearance (Hep3B/HepG2 context). | missing | none |
| phenotype | Higher hepatic SORT1 lowers circulating LDL-C and lowers myocardial-infarction risk. | missing | none |

Predictions: CEBPA ChIP at rs12740374 is higher on alt T than ref G in hepatocytes; SORT1 expression is higher from the alt T haplotype in hepatocytes; alt T is associated with lower LDL-C and lower MI risk

Falsified if: CEBPA ChIP shows no alt-specific enrichment while CEBPB does; SORT1 expression is not allele-specific in hepatocytes; the alt allele is not associated with lower LDL-C after controlling for LD

### 2. C4: Null: no TF-mediated allelic effect of rs12740374 (p = 0.20)

Null chain: no TF-mediated effect of this variant.

Predictions: No allele-specific CEBPA or CEBPB occupancy at rs12740374 in hepatocytes; No allele-specific SORT1 or CELSR2 expression attributable to this variant; Any association with LDL-C/MI is explained by LD with another causal variant or by no allelic effect

Falsified if: allele-specific CEBPA/CEBPB occupancy and allele-specific SORT1 expression persist after controlling for linked variants; CRISPR editing of rs12740374 alone changes SORT1 expression and LDL-C in a hepatocyte model

### 3. C2: Alt T creates a hepatocyte CEBPB site that raises SORT1 and lowers LDL/MI risk (p = 0.15)

TF CEBPB (QBiC-SELEX coverage own_model), alt allele binds more; element 1p13 hepatocyte enhancer; gene SORT1; cell type hepatocyte.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | Alt T binds CEBPB more strongly than ref G; CEBPB shares the C/EBP motif with CEBPA and is expressed in hepatocytes, so it is a competing family member. No QBiC-SELEX model is supplied. | missing | none |
| element | The variant lies in a hepatocyte regulatory element/enhancer in the 1p13 locus; the alt allele increases element activity. | missing | none |
| gene | The alt allele increases SORT1 transcript levels in hepatocytes. | missing | none |
| cell_type | The effect occurs in hepatocytes, the relevant liver cell type for LDL clearance. | missing | none |
| phenotype | Higher hepatic SORT1 lowers circulating LDL-C and lowers myocardial-infarction risk. | missing | none |

Predictions: CEBPB ChIP at rs12740374 is higher on alt T than ref G in hepatocytes; SORT1 expression is higher from the alt T haplotype in hepatocytes; alt T is associated with lower LDL-C and lower MI risk

Falsified if: CEBPA ChIP shows alt-specific enrichment while CEBPB does not; CEBPB knockdown does not reduce the alt-specific element or SORT1 effect; SORT1 expression is not allele-specific in hepatocytes

### 4. C3: Alt T binds CEBPA but the element acts on CELSR2 rather than SORT1 (p = 0.10)

TF CEBPA (QBiC-SELEX coverage own_model), alt allele binds more; element 1p13 regulatory element; gene CELSR2; cell type hepatocyte.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | Alt T binds CEBPA more strongly than ref G via a created C/EBP motif; CEBPA is the hepatic C/EBP-family candidate. No QBiC-SELEX model is supplied. | missing | none |
| element | The variant lies in a regulatory element in the 1p13 locus; the alt allele changes element activity. | missing | none |
| gene | The element acts on CELSR2 rather than SORT1, changing CELSR2 transcript levels. | missing | none |
| cell_type | The effect occurs in hepatocytes. | missing | none |
| phenotype | Altered CELSR2 in hepatocytes changes LDL-C and myocardial-infarction risk. | missing | none |

Predictions: CEBPA ChIP at rs12740374 is higher on alt T than ref G; CELSR2 expression is allele-specific in hepatocytes; SORT1 expression is not allele-specific at this variant

Falsified if: SORT1, not CELSR2, shows allele-specific expression in hepatocytes; CEBPA occupancy does not track the alt allele; CELSR2 perturbation does not affect LDL-C in relevant models

## Prediction matrix

| Test | Cost | Separates top two | C1 | C4 | C2 | C3 |
| --- | --- | --- | --- | --- | --- | --- |
| CEBPA occupancy at rs12740374 | low | yes | alt > ref |  | no alt bias |  |
| CEBPB occupancy at rs12740374 | low | yes | no alt bias |  | alt > ref |  |

## Next experiment

Allele-specific ChIP-qPCR for CEBPA and CEBPB at rs12740374 in Hep3B cells (or supershift EMSA with Hep3B nuclear extract and anti-CEBPA vs anti-CEBPB antibodies if ChIP is not feasible).

## Flags

- none

## Evidence
