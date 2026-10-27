# TERT promoter C228T and Glioblastoma, melanoma, bladder

Configuration `single`, named mode, seed 0. Models: generator openai/gpt-6-luna, critic openai/gpt-6-luna, summariser openai/gpt-6-luna. Cost $0.00 over 1 model calls; 48 s.

Variant `chr5:1295113:G>A` (somatic); expression context: DepMap:subtype=Glioblastoma (median of 54 lines).

## Ranked chains

### 1. H1: The alternate allele creates a GABPA-dependent TERT promoter site (p = 0.68)

TF GABPA (QBiC-SELEX coverage own_model), alt allele binds more; element TERT promoter; gene TERT; cell type Glioblastoma cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | GABPA is the leading candidate because TERT promoter hotspot mutations are known to create ETS-family binding sites with reported GABP involvement; the alternate G>A allele is expected to bind GABPA more strongly, but no case-specific occupancy or QBiC-SELEX result is supplied. | missing | none |
| element | The variant changes a cis-regulatory site in the TERT promoter. | missing | none |
| gene | GABPA binding at the altered promoter increases TERT transcription. | missing | none |
| cell_type | In glioblastoma cells, increased TERT transcription could support telomerase activity. | missing | none |
| phenotype | Increased telomerase activity could contribute to glioblastoma development or maintenance. | missing | none |

Predictions: The alternate promoter allele shows greater GABPA occupancy than the reference allele.; A mutant-versus-reference TERT promoter reporter effect is reduced by GABPA depletion.

Falsified if: In an informative glioblastoma model, the alternate allele shows no increase in GABPA occupancy and the promoter effect is not reduced by GABPA depletion.

### 2. H3: Null: no TF-mediated effect of this variant (p = 0.20)

Null chain: no TF-mediated effect of this variant.

Predictions: The alternate allele has no reproducible TF-dependent effect on TERT promoter activity in a relevant model.; Any association with disease could reflect another causal event, linkage, or a non-causal passenger mutation.

Falsified if: The alternate allele reproducibly increases TERT expression in a relevant model, with the effect dependent on binding of a specific TF.

### 3. H2: An alternate-allele ETS1 site increases TERT transcription (p = 0.12)

TF ETS1 (QBiC-SELEX coverage own_model), alt allele binds more; element TERT promoter; gene TERT; cell type Glioblastoma cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | ETS1 is a lower-priority ETS-family alternative to GABPA; the alternate allele is expected to strengthen its binding based on the created ETS-like motif, but no case-specific occupancy or QBiC-SELEX result is supplied. | missing | none |
| element | The variant changes a cis-regulatory site in the TERT promoter. | missing | none |
| gene | ETS1 binding at the altered promoter increases TERT transcription. | missing | none |
| cell_type | In glioblastoma cells, increased TERT transcription could support telomerase activity. | missing | none |
| phenotype | Increased telomerase activity could contribute to glioblastoma development or maintenance. | missing | none |

Predictions: The alternate promoter allele shows greater ETS1 occupancy than the reference allele.; A mutant-versus-reference TERT promoter reporter effect persists after GABPA depletion but is reduced by ETS1 depletion.

Falsified if: ETS1 depletion does not affect the mutant promoter effect, while GABPA depletion abolishes it.

## Prediction matrix

| Test | Cost | Separates top two | H1 | H3 | H2 |
| --- | --- | --- | --- | --- | --- |
| Compare matched reference and mutant TERT promoter reporters in a glioblastoma line, with and without GABPA depletion. | medium | yes | The mutant reporter has higher activity, and the increase is reduced by GABPA depletion. | There is no reproducible mutant-versus-reference activity difference. | The mutant reporter has higher activity, but the increase persists after GABPA depletion. |
| Measure allele-specific GABPA occupancy at the endogenous TERT promoter in a mutation-positive glioblastoma model. | medium | yes | GABPA occupancy is enriched on the alternate allele. | No reproducible alternate-allele GABPA enrichment is expected. | No specific alternate-allele GABPA enrichment is expected. |
| Compare matched reference and mutant TERT promoter reporters with and without ETS1 depletion. | medium | no | The mutant reporter effect is not specifically dependent on ETS1. | There is no reproducible mutant-versus-reference activity difference. | The mutant reporter has higher activity, and the increase is reduced by ETS1 depletion. |

## Next experiment

Run the matched reference-versus-mutant TERT promoter reporter in a glioblastoma line with and without GABPA depletion. It is the most direct proposed test of the leading GABPA chain against the null: a mutant-specific increase that depends on GABPA supports H1, whereas no reproducible allele effect supports H3.

## Flags

- none

## Evidence
