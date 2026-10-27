# rs339331 and Prostate cancer (6q22)

Configuration `single`, named mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.00 over 1 model calls; 41 s.

Variant `chr6:116888889:T>C` (germline); expression context: DepMap:ACH-000977 (LNCaP clone FGC).

## Ranked chains

### 1. C1: HOXB13 binds the rs339331 ref-T allele more strongly and activates RFX6 in prostate cells (p = 0.45)

TF HOXB13 (stated coverage not_checked; registry own_model), ref allele binds more; element prostate enhancer at 6q22; gene RFX6; cell type LNCaP clone FGC (ACH-000977).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | HOXB13 binds the rs339331 ref T allele more strongly than the alt C allele at the 6q22 locus. | missing | none |
| element | rs339331 lies in a prostate-cell enhancer/regulatory element whose output is altered by allele-specific HOXB13 occupancy. | missing | none |
| gene | The rs339331 enhancer regulates RFX6, the nearby 6q22 target gene. | missing | none |
| cell_type | This occurs in LNCaP clone FGC (DepMap ACH-000977), a prostate cancer cell line with HOXB13 activity. | missing | none |
| phenotype | Higher HOXB13 occupancy on the ref T allele increases RFX6 expression and contributes to prostate cancer risk at 6q22. | missing | none |

Predictions: HOXB13 ChIP at rs339331 is higher on the ref T allele than the alt C allele.; An rs339331 ref-T enhancer reporter is more active than the alt-C reporter in LNCaP cells and this difference is HOXB13-dependent.; RFX6 expression is higher in prostate cells carrying the ref T allele or after HOXB13 overexpression.; The ref T allele is associated with higher prostate cancer risk at 6q22.

Falsified if: No reproducible allele-specific HOXB13 binding at rs339331 is found.; The ref-T reporter is not more active than the alt-C reporter in LNCaP cells.; RFX6 expression is not affected by HOXB13 or by the rs339331 allele.

### 2. C4: No TF-mediated allelic effect of rs339331; the association reflects a linked causal variant or passenger signal (p = 0.35)

Null chain: no TF-mediated effect of this variant.

Predictions: No reproducible allele-specific TF binding at rs339331 is found.; The rs339331 ref and alt enhancer reporters show no allele-specific activity difference in LNCaP cells.; RFX6 expression is not allele-specifically affected by rs339331.; The prostate cancer association at 6q22 is explained by a linked causal variant or by a passenger signal.

Falsified if: A reproducible allele-specific TF binding and enhancer/RFX6 effect at rs339331 is demonstrated in prostate cells.

### 3. C2: HOXB13 binds the rs339331 ref-T allele more strongly and represses RFX6 in prostate cells (p = 0.15)

TF HOXB13 (stated coverage not_checked; registry own_model), ref allele binds more; element prostate enhancer at 6q22; gene RFX6; cell type LNCaP clone FGC (ACH-000977).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | HOXB13 binds the rs339331 ref T allele more strongly than the alt C allele at the 6q22 locus. | missing | none |
| element | rs339331 lies in a prostate-cell enhancer/regulatory element whose output is altered by allele-specific HOXB13 occupancy. | missing | none |
| gene | The rs339331 enhancer regulates RFX6, the nearby 6q22 target gene. | missing | none |
| cell_type | This occurs in LNCaP clone FGC (DepMap ACH-000977), a prostate cancer cell line with HOXB13 activity. | missing | none |
| phenotype | Higher HOXB13 occupancy on the ref T allele represses RFX6 expression and contributes to prostate cancer risk at 6q22. | missing | none |

Predictions: HOXB13 ChIP at rs339331 is higher on the ref T allele than the alt C allele.; An rs339331 ref-T enhancer reporter is less active than the alt-C reporter in LNCaP cells and this difference is HOXB13-dependent.; RFX6 expression is lower in prostate cells carrying the ref T allele or after HOXB13 overexpression.; The ref T allele is associated with altered prostate cancer risk at 6q22.

Falsified if: No reproducible allele-specific HOXB13 binding at rs339331 is found.; The ref-T reporter is more active, not less active, than the alt-C reporter in LNCaP cells.; RFX6 expression is not affected by HOXB13 or by the rs339331 allele.

### 4. C3: FOXA1 binds the rs339331 alt-C allele more strongly and alters RFX6 in prostate cells (p = 0.05)

TF FOXA1 (stated coverage not_checked; registry own_model), alt allele binds more; element prostate enhancer at 6q22; gene RFX6; cell type LNCaP clone FGC (ACH-000977).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | FOXA1 binds the rs339331 alt C allele more strongly than the ref T allele at the 6q22 locus. | missing | none |
| element | rs339331 lies in a prostate-cell enhancer/regulatory element whose output is altered by allele-specific FOXA1 occupancy. | missing | none |
| gene | The rs339331 enhancer regulates RFX6, the nearby 6q22 target gene. | missing | none |
| cell_type | This occurs in LNCaP clone FGC (DepMap ACH-000977), a prostate cancer cell line with FOXA1 activity. | missing | none |
| phenotype | Higher FOXA1 occupancy on the alt C allele alters RFX6 expression and contributes to prostate cancer risk at 6q22. | missing | none |

Predictions: FOXA1 ChIP at rs339331 is higher on the alt C allele than the ref T allele.; An rs339331 alt-C enhancer reporter is more active than the ref-T reporter in LNCaP cells and this difference is FOXA1-dependent.; RFX6 expression is higher in prostate cells carrying the alt C allele or after FOXA1 overexpression.; The alt C allele is associated with altered prostate cancer risk at 6q22.

Falsified if: No reproducible allele-specific FOXA1 binding at rs339331 is found.; The alt-C reporter is not more active than the ref-T reporter in LNCaP cells.; RFX6 expression is not affected by FOXA1 or by the rs339331 allele.

## Prediction matrix

| Test | Cost | Separates top two | C1 | C4 | C2 | C3 |
| --- | --- | --- | --- | --- | --- | --- |
| Allele-specific HOXB13 ChIP at rs339331 | low | no | ref T > alt C | no allele difference | ref T < alt C |  |

## Next experiment

Allele-specific enhancer reporter assay in LNCaP clone FGC (DepMap ACH-000977): clone the rs339331 ref-T and alt-C enhancer upstream of a minimal promoter/luciferase, transfect into LNCaP cells with and without HOXB13 knockdown, and measure luciferase. A ref-T > alt-C, HOXB13-dependent reporter difference supports C1; a ref-T < alt-C difference supports C2; no allele-specific or HOXB13-dependent difference supports the null C4.

## Flags

- none

## Evidence
