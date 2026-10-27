# rs73706717 and Colorectal cancer (8q24)

Configuration `single`, named mode, seed 0. Models: generator openai/gpt-6-luna, critic openai/gpt-6-luna, summariser openai/gpt-6-luna. Cost $0.00 over 1 model calls; 56 s.

Variant `chr8:127401265:T>C` (germline); expression context: DepMap:ACH-000971 (HCT 116).

## Ranked chains

### 1. H0: Null: no TF-mediated effect of rs73706717 (p = 0.70)

Null chain: no TF-mediated effect of this variant.

Predictions: The T and C alleles will not show a reproducible, functionally relevant difference in TF binding caused by this base; any CRC association could instead reflect linkage to another variant or no causal effect.

Falsified if: Precise editing of rs73706717 reproducibly changes TF occupancy and cis MYC regulation in colorectal cells, with the effect dependent on the implicated TF.

### 2. H1: Candidate TCF7L2-dependent MYC enhancer effect (p = 0.14)

TF TCF7L2 (QBiC-SELEX coverage mapped), alt allele binds more; element A candidate cis-regulatory element near MYC; gene MYC; cell type Colorectal epithelial cells, including HCT 116.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | Hypothesis: the C allele binds TCF7L2 more strongly than the T allele. TCF7L2 is a plausible CRC-context candidate, but no occupancy or QBiC-SELEX result for this site is available here, so the direction is untested. | missing | none |
| element | The variant acts in a candidate cis-regulatory element that can influence MYC. | missing | none |
| gene | The element increases MYC expression when TCF7L2 binding is greater. | missing | none |
| cell_type | The proposed effect occurs in colorectal epithelial cells, with HCT 116 as a testable context. | missing | none |
| phenotype | Higher MYC activity in colorectal epithelium could increase CRC susceptibility. | missing | none |

Predictions: Allele-specific binding assays will show greater TCF7L2 binding to C than T.; Editing T to C will increase TCF7L2 occupancy and MYC expression; reducing TCF7L2 will attenuate the expression difference.

Falsified if: A suitably sensitive assay finds no C-over-T TCF7L2 binding difference.; Precise allele editing produces no TCF7L2-dependent change in MYC regulation.

### 3. H2: Candidate HNF4A-dependent MYC enhancer effect (p = 0.09)

TF HNF4A (QBiC-SELEX coverage own_model), ref allele binds more; element A candidate cis-regulatory element near MYC; gene MYC; cell type Colorectal epithelial cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | Hypothesis: the T allele binds HNF4A more strongly than the C allele. HNF4A is a candidate because of its role in intestinal epithelial gene regulation; no occupancy or QBiC-SELEX result for this site is available here. | missing | none |
| element | The variant acts in a candidate cis-regulatory element that can influence MYC. | missing | none |
| gene | Greater HNF4A binding increases MYC expression through this element. | missing | none |
| cell_type | The proposed effect occurs in colorectal epithelial cells with HNF4A activity. | missing | none |
| phenotype | A resulting increase in MYC activity could increase CRC susceptibility. | missing | none |

Predictions: Allele-specific assays will show greater HNF4A binding to T than C, rather than the C-over-T TCF7L2 pattern proposed in H1.; Editing C to T will increase HNF4A occupancy and HNF4A-dependent MYC expression.

Falsified if: HNF4A does not occupy the region in the relevant cells or shows no T-over-C binding difference.; Allele editing produces no HNF4A-dependent change in MYC regulation.

### 4. H3: Candidate JUN-dependent enhancer effect (p = 0.07)

TF JUN (QBiC-SELEX coverage own_model), alt allele binds more; element A candidate cis-regulatory element near MYC; gene MYC; cell type Colorectal epithelial cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | Hypothesis: the C allele binds JUN more strongly than the T allele. JUN is a candidate stress-responsive regulator, but no occupancy or QBiC-SELEX result for this site is available here. | missing | none |
| element | The variant acts in a candidate cis-regulatory element that can influence MYC. | missing | none |
| gene | Greater JUN binding increases MYC expression through this element. | missing | none |
| cell_type | The proposed effect occurs in colorectal epithelial cells under conditions with JUN activity. | missing | none |
| phenotype | A resulting increase in MYC activity could increase CRC susceptibility. | missing | none |

Predictions: Allele-specific assays will show greater JUN binding to C; JUN perturbation, rather than TCF7L2 or HNF4A perturbation, will remove the allele-dependent MYC effect.

Falsified if: JUN does not occupy the region or shows no C-over-T binding difference.; Allele editing produces no JUN-dependent change in MYC regulation.

## Prediction matrix

| Test | Cost | Separates top two | H0 | H1 | H2 | H3 |
| --- | --- | --- | --- | --- | --- | --- |
| Low-cost electrophoretic mobility shift assay using matched T- and C-allele probes and recombinant TCF7L2; compare allele-specific complexes, with specificity controls. | low | yes | No reproducible TCF7L2-specific difference between the two probes; this would be consistent with the null, though it would not rule out other mechanisms. | A reproducibly stronger TCF7L2-specific complex with the C probe than the T probe. | No predicted TCF7L2-specific C-over-T difference; this assay does not directly test the HNF4A model. | No predicted TCF7L2-specific C-over-T difference; this assay does not directly test the JUN model. |

## Next experiment

Run the low-cost TCF7L2 allele-specific mobility shift assay described above to distinguish the leading null hypothesis from the leading candidate chain. A positive result would test differential binding only, not endogenous occupancy, MYC regulation, or disease causality.

## Flags

- none

## Evidence
