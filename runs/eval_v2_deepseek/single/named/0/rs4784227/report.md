# rs4784227 and Breast cancer (16q12)

Configuration `single`, named mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.01 over 2 model calls; 55 s.

Variant `chr16:52565276:C>T` (germline); expression context: DepMap:ACH-000019 (MCF7).

## Ranked chains

### 1. C1: FOXA1 binds the alt T allele more and activates a TOX3 enhancer (p = 0.35)

TF FOXA1 (QBiC-SELEX coverage own_model), alt allele binds more; element rs4784227 FOXA1-bound enhancer; gene TOX3; cell type MCF7 mammary epithelial.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | FOXA1 binds the alt T allele more strongly than ref C. FOXA1 is chosen from prior 16q12.1 breast-cancer literature; no ChIP, expression, or QBiC-SELEX evidence was supplied for this case, and FOXA1 has no QBiC-SELEX model/evidence here. | missing | none |
| element | rs4784227 lies in a FOXA1-bound regulatory element/enhancer; the T allele creates a stronger FOXA1 site. | missing | none |
| gene | The FOXA1-bound enhancer increases TOX3 expression. | missing | none |
| cell_type | The effect occurs in MCF7 mammary epithelial cells, the supplied expression context. | missing | none |
| phenotype | Higher TOX3 expression increases breast cancer risk at 16q12. | missing | none |

Predictions: Allele-specific FOXA1 ChIP in MCF7 shows higher FOXA1 occupancy on T than C at rs4784227.; A C-vs-T enhancer reporter in MCF7 shows higher activity for T.; TOX3 expression is higher with the T allele in MCF7/breast models.; The T allele is associated with increased breast cancer risk.

Falsified if: FOXA1 ChIP is not higher on T than C.; The T allele does not increase enhancer reporter activity.; TOX3 expression is not higher with T.

### 2. C2: FOXA1 binds the ref C allele more and represses TOX3; T loses repression (p = 0.30)

TF FOXA1 (QBiC-SELEX coverage own_model), ref allele binds more; element rs4784227 FOXA1-bound silencer; gene TOX3; cell type MCF7 mammary epithelial.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | FOXA1 binds the ref C allele more strongly than alt T. FOXA1 is chosen as the same locus candidate; no ChIP, expression, or QBiC-SELEX evidence was supplied, and FOXA1 has no QBiC-SELEX model/evidence here. | missing | none |
| element | rs4784227 lies in a FOXA1-bound silencer/repressive element; the C allele creates a stronger FOXA1 site. | missing | none |
| gene | FOXA1 represses TOX3; loss of the C-allele site on T increases TOX3 expression. | missing | none |
| cell_type | The repressive FOXA1 effect occurs in MCF7 mammary epithelial cells. | missing | none |
| phenotype | Derepressed TOX3 increases breast cancer risk at 16q12. | missing | none |

Predictions: Allele-specific FOXA1 ChIP in MCF7 shows higher FOXA1 occupancy on C than T.; A C-vs-T enhancer reporter shows lower activity for C if FOXA1 is repressive.; TOX3 expression is higher with T because the repressive C site is lost.; The T allele is associated with increased breast cancer risk.

Falsified if: FOXA1 ChIP is higher on T than C or shows no allelic difference.; The C allele does not repress enhancer reporter activity.; TOX3 expression is not higher with T.

### 3. NULL: Null: no TF-mediated effect of rs4784227 (p = 0.25)

Null chain: no TF-mediated effect of this variant.

Predictions: No allele-specific TF ChIP difference at rs4784227.; No C-vs-T enhancer reporter difference in MCF7.; TOX3 expression is not associated with rs4784227 after controlling for linked variants.; The 16q12 risk signal is driven by a linked causal variant or another mechanism.

Falsified if: A reproducible allele-specific TF occupancy and enhancer/reporter effect is shown for rs4784227.; TOX3 expression tracks rs4784227 independently of linked variants.

### 4. C3: GATA3 binds the alt T allele more and activates TOX3 (p = 0.10)

TF GATA3 (QBiC-SELEX coverage own_model), alt allele binds more; element rs4784227 GATA3-bound enhancer; gene TOX3; cell type MCF7 mammary epithelial.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | GATA3 binds the alt T allele more strongly than ref C. GATA3 is a competing breast-lineage TF; no ChIP, expression, or QBiC-SELEX evidence was supplied, and GATA3 has no QBiC-SELEX model/evidence here. | missing | none |
| element | rs4784227 lies in a GATA3-bound enhancer; the T allele creates a stronger GATA3 site. | missing | none |
| gene | The GATA3-bound enhancer increases TOX3 expression. | missing | none |
| cell_type | The effect occurs in MCF7 mammary epithelial cells. | missing | none |
| phenotype | Higher TOX3 expression increases breast cancer risk at 16q12. | missing | none |

Predictions: Allele-specific GATA3 ChIP in MCF7 shows higher GATA3 occupancy on T than C.; FOXA1 ChIP shows no allele-specific difference at rs4784227.; GATA3 knockdown reduces T-allele enhancer reporter activity.; The T allele is associated with increased breast cancer risk.

Falsified if: GATA3 ChIP is not higher on T than C.; GATA3 knockdown does not affect the T-allele reporter.; FOXA1, not GATA3, shows allele-specific occupancy.

## Prediction matrix

| Test | Cost | Separates top two | C1 | C2 | NULL | C3 |
| --- | --- | --- | --- | --- | --- | --- |
| Allele-specific FOXA1 ChIP in MCF7 | medium | yes | FOXA1 occupancy T > C | FOXA1 occupancy C > T | No FOXA1 allelic difference |  |
| EMSA with recombinant FOXA1, C vs T probes | low | yes | T probe shifts more than C | C probe shifts more than T | No differential shift |  |
| C-vs-T enhancer reporter in MCF7 | medium | yes | T reporter higher than C | C reporter lower/repressive, T higher | No allele-specific difference |  |
| Allele-specific GATA3 ChIP in MCF7 | medium | no | No GATA3 allelic difference, FOXA1 difference present | No GATA3 allelic difference, FOXA1 opposite difference present | No GATA3 allelic difference | GATA3 occupancy T > C |
| TOX3 expression by rs4784227 allele in MCF7 | low | no | T allele higher TOX3 | T allele higher TOX3 due to loss of repression | No independent allelic association | T allele higher TOX3 |

## Next experiment

EMSA with recombinant FOXA1 and matched C vs T probes centered on rs4784227; stronger T shift supports C1, stronger C shift supports C2, and no differential shift argues against both.

## Flags

- none

## Evidence
