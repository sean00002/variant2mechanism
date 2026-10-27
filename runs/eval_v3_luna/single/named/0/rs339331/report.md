# rs339331 and Prostate cancer (6q22)

Configuration `single`, named mode, seed 0. Models: generator openai/gpt-6-luna, critic openai/gpt-6-luna, summariser openai/gpt-6-luna. Cost $0.00 over 1 model calls; 60 s.

Variant `chr6:116888889:T>C` (germline); expression context: DepMap:ACH-000977 (LNCaP clone FGC).

## Ranked chains

### 1. H1: The T allele strengthens HOXB13 binding and RFX6 enhancer activity (p = 0.54)

TF HOXB13 (QBiC-SELEX coverage own_model), ref allele binds more; element A regulatory element within the RFX6 locus containing rs339331; gene RFX6; cell type Androgen-responsive prostate luminal epithelial cells, including LNCaP.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The ref T allele is hypothesized to bind HOXB13 more strongly than alt C. HOXB13 is the leading candidate based on prior reports concerning this locus; no occupancy or QBiC-SELEX result is supplied here to establish the allele effect. | missing | none |
| element | The rs339331-containing sequence acts as a regulatory element whose activity is increased by stronger HOXB13 binding. | missing | none |
| gene | The element increases RFX6 expression. | missing | none |
| cell_type | This regulatory effect occurs in androgen-responsive prostate luminal epithelial cells such as LNCaP. | missing | none |
| phenotype | Increased RFX6 expression in prostate cells contributes to increased prostate cancer susceptibility. | missing | none |

Predictions: In heterozygous cells, HOXB13 occupancy at rs339331 is enriched on the T allele.; The T allele is associated with greater enhancer activity and RFX6 expression than the C allele in prostate cells.

Falsified if: A well-powered allele-specific HOXB13 occupancy assay shows no T-allele enrichment or shows greater occupancy on C.; The rs339331 alleles have no reproducible difference in enhancer activity or RFX6 expression in relevant prostate cells.

### 2. H0: No TF-mediated effect of rs339331 (p = 0.35)

Null chain: no TF-mediated effect of this variant.

Predictions: There is no reproducible allele-specific TF occupancy or regulatory effect attributable to rs339331.; Any prostate cancer association at the locus is due to linkage with another causal variant, a non-TF mechanism, or chance.

Falsified if: Editing rs339331 alone reproducibly changes TF occupancy and enhancer activity in relevant prostate cells, with a corresponding change in target-gene expression.

### 3. H2: The C allele changes FOXA1 binding and alters RFX6 regulation (p = 0.11)

TF FOXA1 (QBiC-SELEX coverage own_model), alt allele binds more; element A regulatory element within the RFX6 locus containing rs339331; gene RFX6; cell type Androgen-responsive prostate luminal epithelial cells, including LNCaP.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | As an alternative to the HOXB13 model, the alt C allele is hypothesized to bind FOXA1 more strongly; this is speculative, and no FOXA1 occupancy or QBiC-SELEX result is supplied here. | missing | none |
| element | Allele-dependent FOXA1 binding changes the activity of the rs339331-containing regulatory element. | missing | none |
| gene | The altered element changes RFX6 expression. | missing | none |
| cell_type | The effect occurs in androgen-responsive prostate luminal epithelial cells such as LNCaP. | missing | none |
| phenotype | The resulting change in RFX6 expression modifies prostate cancer susceptibility. | missing | none |

Predictions: In heterozygous cells, FOXA1 occupancy at rs339331 is enriched on the C allele, without the T-specific HOXB13 enrichment predicted by H1.; The C allele produces a FOXA1-dependent change in enhancer activity and RFX6 expression.

Falsified if: Allele-specific assays show no C-enriched FOXA1 occupancy or show stronger FOXA1 occupancy on T.; FOXA1 perturbation does not affect the allele-dependent enhancer or RFX6 expression difference.

## Prediction matrix

| Test | Cost | Separates top two | H1 | H0 | H2 |
| --- | --- | --- | --- | --- | --- |
| Allele-specific HOXB13 CUT&RUN-qPCR across rs339331 in heterozygous LNCaP cells | medium | yes | HOXB13 occupancy is enriched on the ref T allele. | No reproducible allele-specific HOXB13 occupancy is expected. | No T-enriched HOXB13 occupancy is expected; FOXA1, rather than HOXB13, is the proposed allele-sensitive TF. |

## Next experiment

Perform allele-specific HOXB13 CUT&RUN-qPCR across rs339331 in heterozygous LNCaP cells. T-enriched occupancy would support the leading HOXB13 chain over the null; no allele-specific enrichment would weaken it. If LNCaP is not heterozygous at this site, use matched T/C isogenic cells.

## Flags

- none

## Evidence
