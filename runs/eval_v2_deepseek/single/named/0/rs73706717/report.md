# rs73706717 and Colorectal cancer (8q24)

Configuration `single`, named mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.01 over 1 model calls; 29 s.

Variant `chr8:127401265:T>C` (germline); expression context: DepMap:ACH-000971 (HCT 116).

## Ranked chains

### 1. H1: TCF7L2 binds alt C more at the 8q24 enhancer and increases MYC (p = 0.50)

TF TCF7L2 (QBiC-SELEX coverage mapped), alt allele binds more; element 8q24.21 colorectal cancer enhancer near rs6983267; gene MYC; cell type HCT116 colorectal carcinoma.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | TCF7L2 binds the alt C allele more strongly than the ref T allele. TCF7L2 is the best-supported Wnt effector at the 8q24.21 CRC enhancer; the variant is ~57 bp from rs6983267 in a known TCF7L2-bound enhancer, and the T>C change is predicted to alter a TCF/LEF site. No QBiC-SELEX model is supplied for this exact variant here, so this is a motif- and locus-biology-based selection, not a direct affinity measurement. | missing | none |
| element | rs73706717 lies in a distal 8q24 enhancer that is active in colorectal cancer cells and can be occupied by TCF7L2; the C allele increases TCF7L2 occupancy at this element. | missing | none |
| gene | The 8q24 enhancer regulates MYC, the principal target gene in this locus; increased TCF7L2 occupancy at the C allele increases MYC transcription. | missing | none |
| cell_type | HCT116 colorectal carcinoma cells have active Wnt/TCF7L2 signaling and open chromatin at the 8q24.21 enhancer, making this a relevant cell context. | missing | none |
| phenotype | Higher TCF7L2 binding at the alt C allele increases MYC expression and colorectal cancer risk, assuming TCF7L2 acts as an activator in this enhancer context. | missing | none |

Predictions: Allele-specific TCF7L2 ChIP shows C > T occupancy at rs73706717.; The C allele increases enhancer reporter activity in HCT116 cells.; MYC expression is higher on the C allele or in C-bearing enhancer reporter cells.; The C allele is the risk-associated allele in this model.

Falsified if: TCF7L2 binds equally to T and C alleles in a direct binding assay.; Allele-specific TCF7L2 ChIP shows no occupancy over rs73706717.; The C allele does not change enhancer activity or MYC expression in HCT116-derived assays.

### 2. H0: Null: no TF-mediated effect of rs73706717; signal is linked to rs6983267 or another causal variant (p = 0.30)

Null chain: no TF-mediated effect of this variant.

Predictions: No allele-specific TF occupancy at rs73706717.; No allele-specific enhancer reporter difference for rs73706717 alone.; No allele-specific MYC expression difference after controlling for rs6983267.; The CRC association tracks rs6983267 or another linked variant rather than rs73706717.

Falsified if: Allele-specific TCF7L2 or other TF occupancy is detected at rs73706717 independent of rs6983267.; A reporter carrying only the rs73706717 T vs C alleles shows a reproducible allelic difference.; Conditioning on rs6983267 leaves an independent rs73706717 effect on MYC or CRC risk.

### 3. H2: TCF7L2 binds ref T more and represses or fails to activate MYC (p = 0.10)

TF TCF7L2 (QBiC-SELEX coverage mapped), ref allele binds more; element 8q24.21 colorectal cancer enhancer near rs6983267; gene MYC; cell type HCT116 colorectal carcinoma.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | TCF7L2 binds the ref T allele more strongly than the alt C allele; the T>C change disrupts a TCF/LEF-related site in the 8q24 enhancer. This is the opposite allelic direction from H1 and is kept as a lower-probability competitor because the exact motif orientation and sequence context are not supplied. | missing | none |
| element | The variant sits in the 8q24 enhancer, and the ref T allele preserves higher TCF7L2 occupancy and enhancer output. | missing | none |
| gene | TCF7L2 occupancy at the ref T allele modulates MYC; if TCF7L2 is repressive or if the enhancer is already saturated, the net effect on MYC may be lower or unchanged. | missing | none |
| cell_type | HCT116 has active Wnt/TCF7L2 signaling, so allele-specific TCF7L2 occupancy can be tested in this cell type. | missing | none |
| phenotype | The ref T allele is associated with the disease-risk direction through altered TCF7L2 occupancy and MYC regulation; the alt C allele isprotective or less risky in this model. | missing | none |

Predictions: Allele-specific TCF7L2 ChIP shows T > C occupancy at rs73706717.; The T allele changes enhancer reporter activity more than C.; MYC expression tracks the T allele in this model.; The T allele is the risk-associated allele.

Falsified if: Direct binding assays show C > T or equal TCF7L2 binding.; Allele-specific TCF7L2 ChIP shows C > T occupancy.; Reporter assays show C, not T, drives higher enhancer activity.

### 4. H3: MYC/MAX binds alt C more at an E-box in the 8q24 enhancer (p = 0.10)

TF MYC (QBiC-SELEX coverage not_in_coverage), alt allele binds more; element 8q24.21 colorectal cancer enhancer near rs6983267; gene MYC; cell type HCT116 colorectal carcinoma.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | MYC, acting as a MYC/MAX heterodimer, binds the alt C allele more strongly than ref T at a variant E-box-like site in the 8q24 enhancer. This is a lower-probability alternative because MYC is the locus target and E-box motifs can be altered by T>C, but no occupancy evidence for MYC over this exact base is supplied. | missing | none |
| element | The variant lies in the 8q24 enhancer, and the C allele creates or strengthens a MYC/MAX-bound E-box that modulates enhancer activity. | missing | none |
| gene | MYC binding at its own 8q24 enhancer contributes to MYC autoregulation; the C allele increases this feedback and raises MYC expression. | missing | none |
| cell_type | HCT116 colorectal carcinoma cells express MYC and have active 8q24 enhancer chromatin, so MYC occupancy can be tested there. | missing | none |
| phenotype | Higher MYC/MAX occupancy at the C allele increases MYC expression and colorectal cancer risk. | missing | none |

Predictions: MYC ChIP shows C > T occupancy at rs73706717.; TCF7L2 ChIP shows no allele bias at this base.; The C allele increases enhancer reporter activity in a MYC-dependent manner.; MYC expression is higher on the C allele.

Falsified if: MYC ChIP shows no occupancy or no allele bias over rs73706717.; TCF7L2, not MYC, shows the allele-specific occupancy.; The C allele does not alter MYC expression or enhancer activity.

## Prediction matrix

| Test | Cost | Separates top two | H1 | H0 | H2 | H3 |
| --- | --- | --- | --- | --- | --- | --- |
| allele-specific TCF7L2 occupancy | low | yes | C > T occupancy | no allele-specific occupancy | T > C occupancy |  |

## Next experiment

Competitive EMSA with recombinant TCF7L2 and T vs C probes (or, if occupancy is required, allele-specific TCF7L2 ChIP-qPCR in a heterozygous CRC line). If the C probe shifts more, H1 is supported; if binding is equal or absent, H0 is favored.

## Flags

- none

## Evidence
