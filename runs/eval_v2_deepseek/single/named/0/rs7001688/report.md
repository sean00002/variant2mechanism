# rs7001688 and LDL cholesterol

Configuration `single`, named mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.00 over 1 model calls; 39 s.

Variant `chr8:57573391:G>T` (germline); expression context: DepMap:ACH-000625 (Hep 3B2.1-7).

## Ranked chains

### 1. C4: Null: no TF-mediated allelic effect at rs7001688 (p = 0.45)

Null chain: no TF-mediated effect of this variant.

Predictions: No allele-specific TF occupancy at rs7001688 in Hep 3B2.1-7.; No allele-specific enhancer activity for rs7001688.; Any LDL association is due to a linked causal variant, not rs7001688 itself.

Falsified if: A robust allele-specific TF occupancy and enhancer activity at rs7001688 is demonstrated in hepatocytes.; Allele-specific CYP7A1 regulation is shown to depend on rs7001688.

### 2. C1: HNF4A-dependent liver enhancer at CYP7A1 (p = 0.30)

TF HNF4A (QBiC-SELEX coverage own_model), ref allele binds more; element None; gene CYP7A1; cell type hepatocyte (Hep 3B2.1-7).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | HNF4A binds the ref G allele more strongly than alt T at rs7001688. HNF4A is selected as a liver-enriched TF relevant to CYP7A1 regulation; no QBiC-SELEX model or occupancy evidence is supplied in this no-evidence case, so this is a motif/literature-based hypothesis only. | missing | none |
| element | The variant sits in a hepatocyte regulatory element; the ref G allele increases HNF4A-dependent enhancer activity. | missing | none |
| gene | The element regulates CYP7A1, the nearby cholesterol/bile-acid gene; the ref G allele increases CYP7A1 expression. | missing | none |
| cell_type | This occurs in Hep 3B2.1-7 hepatocyte-like cells, where HNF4A and CYP7A1 are expressed. | missing | none |
| phenotype | Increased CYP7A1 lowers hepatic cholesterol and plasma LDL cholesterol; thus the ref G allele is predicted to associate with lower LDL. | missing | none |

Predictions: Allele-specific HNF4A occupancy at rs7001688 in Hep 3B2.1-7: ref G > alt T.; Reporter assay in Hep 3B2.1-7: ref G allele has higher enhancer activity than alt T.; CYP7A1 expression is higher with the ref G allele in hepatocyte context.

Falsified if: No allele-specific HNF4A binding at rs7001688 in hepatocyte nuclear extract or ChIP.; The variant does not alter enhancer activity in Hep 3B2.1-7.; CYP7A1 expression is not allele-dependently regulated in hepatocytes.

### 3. C2: SREBF2 sterol-response element mechanism (p = 0.15)

TF SREBF2 (QBiC-SELEX coverage own_model), alt allele binds more; element None; gene CYP7A1; cell type hepatocyte (Hep 3B2.1-7).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | SREBF2 binds the alt T allele more strongly than ref G at rs7001688. SREBF2 is chosen as the cholesterol-axis TF; no QBiC-SELEX model or occupancy evidence is supplied, so this is speculative. | missing | none |
| element | The variant lies in a sterol-responsive regulatory element; the alt T allele increases SREBF2-dependent element activity. | missing | none |
| gene | The element modulates CYP7A1 expression; alt T increases SREBF2-mediated repression of CYP7A1. | missing | none |
| cell_type | This occurs in Hep 3B2.1-7 hepatocytes with active SREBF2 cholesterol regulation. | missing | none |
| phenotype | Reduced CYP7A1 raises hepatic cholesterol and plasma LDL cholesterol; thus alt T is predicted to associate with higher LDL. | missing | none |

Predictions: Allele-specific SREBF2 occupancy at rs7001688 in Hep 3B2.1-7: alt T > ref G.; Sterol-responsive reporter activity is higher for alt T than ref G.; CYP7A1 expression is lower with alt T under sterol-replete conditions.

Falsified if: No allele-specific SREBF2 binding at rs7001688.; The element does not respond to sterol/SREBF2 perturbation.; CYP7A1 expression is not altered by SREBF2 knockdown in hepatocytes.

### 4. C3: CEBPB liver enhancer mechanism (p = 0.10)

TF CEBPB (QBiC-SELEX coverage own_model), alt allele binds more; element None; gene CYP7A1; cell type hepatocyte (Hep 3B2.1-7).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | CEBPB binds the alt T allele more strongly than ref G at rs7001688. CEBPB is chosen as a liver-expressed enhancer TF; no QBiC-SELEX model or occupancy evidence is supplied, so this is speculative. | missing | none |
| element | The variant lies in a CEBPB-responsive hepatocyte enhancer; alt T increases enhancer activity. | missing | none |
| gene | The enhancer increases CYP7A1 expression; alt T is predicted to increase CYP7A1 transcription. | missing | none |
| cell_type | This occurs in Hep 3B2.1-7 hepatocytes, which support CEBPB-dependent enhancer activity. | missing | none |
| phenotype | Increased CYP7A1 lowers plasma LDL cholesterol; thus alt T is predicted to associate with lower LDL. | missing | none |

Predictions: Allele-specific CEBPB occupancy at rs7001688 in Hep 3B2.1-7: alt T > ref G.; Reporter activity is higher for alt T than ref G in hepatocytes.; CYP7A1 expression is higher with alt T.

Falsified if: No allele-specific CEBPB binding at rs7001688.; CEBPB knockdown does not alter the element's activity.; CYP7A1 expression is not allele-dependent.

## Prediction matrix

| Test | Cost | Separates top two | C4 | C1 | C2 | C3 |
| --- | --- | --- | --- | --- | --- | --- |
| Allele-specific HNF4A occupancy at rs7001688 | low | yes | no allele difference | ref G > alt T | no or weak allele difference for HNF4A | no or weak allele difference for HNF4A |

## Next experiment

The top two hypotheses are C4 (probability 0.45) and C1 (probability 0.30). The single cheapest experiment to separate them is an allele-specific HNF4A EMSA or HNF4A ChIP-qPCR at rs7001688 in Hep 3B2.1-7 cells. If HNF4A shows ref G > alt T allele-specific occupancy, C1 is supported; if there is no allele-specific HNF4A binding, C4 remains favored.

## Flags

- none

## Evidence
