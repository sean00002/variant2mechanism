# rs11629191 and Breast cancer

Configuration `single`, named mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.00 over 1 model calls; 26 s.

Variant `chr14:55887040:C>T` (germline); expression context: DepMap:ACH-000019 (MCF7).

## Ranked chains

### 1. H0: Null: no TF-mediated allelic effect at rs11629191 (p = 0.40)

Null chain: no TF-mediated effect of this variant.

Predictions: No allele-specific transcription factor binding at rs11629191 in MCF7 or relevant breast cells.; Any breast cancer association is explained by linkage disequilibrium with a nearby causal variant, not by this variant itself.

Falsified if: Allele-specific binding of a specific TF at rs11629191 is demonstrated, and the variant-containing element shows allele-dependent enhancer activity.; A reporter assay shows that the rs11629191 alleles differentially affect expression in a TF-dependent manner.

### 2. H1: FOXA1 binds the alt allele more strongly at a distal enhancer regulating PELI2 (p = 0.30)

TF FOXA1 (stated coverage not_checked; registry own_model), alt allele binds more; element candidate distal enhancer at chr14:55887040; gene PELI2; cell type MCF7 breast cancer epithelial cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The alt T allele creates or strengthens a FOXA1 binding site, so FOXA1 binds the alt allele more strongly than the ref C allele. | missing | none |
| element | rs11629191 lies in a candidate distal enhancer that is active in MCF7 breast cancer cells. | missing | none |
| gene | This enhancer regulates PELI2 expression, with the alt allele increasing PELI2 transcription. | missing | none |
| cell_type | FOXA1 is expressed in MCF7 breast cancer epithelial cells, where the enhancer is active. | missing | none |
| phenotype | Increased FOXA1-dependent PELI2 expression promotes breast cancer risk or progression. | missing | none |

Predictions: FOXA1 ChIP-qPCR or EMSA shows stronger binding to the alt T allele than to the ref C allele.; An allele-specific reporter in MCF7 shows higher activity for the alt allele, and FOXA1 knockdown reduces this difference.; PELI2 expression correlates with the alt allele in MCF7 or breast tissue.

Falsified if: FOXA1 binds both alleles equally, or binds the ref C allele more strongly.; The alt allele does not increase reporter activity in MCF7, or the effect is not FOXA1-dependent.

### 3. H2: TFAP2C binds the alt allele more strongly at an enhancer regulating PELI2 (p = 0.12)

TF TFAP2C (stated coverage not_checked; registry own_model), alt allele binds more; element candidate distal enhancer at chr14:55887040; gene PELI2; cell type MCF7 breast cancer epithelial cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The alt T allele creates or strengthens a TFAP2C binding site, so TFAP2C binds the alt allele more strongly than the ref C allele. | missing | none |
| element | rs11629191 lies in a candidate distal enhancer active in MCF7 breast cancer cells. | missing | none |
| gene | This enhancer regulates PELI2 expression, with the alt allele increasing PELI2 transcription. | missing | none |
| cell_type | TFAP2C is expressed in MCF7 breast cancer epithelial cells and can act at breast-cancer enhancers. | missing | none |
| phenotype | Increased TFAP2C-dependent PELI2 expression promotes breast cancer risk or progression. | missing | none |

Predictions: TFAP2C ChIP-qPCR or EMSA shows stronger binding to the alt T allele than to the ref C allele.; TFAP2C knockdown reduces the alt-allele-specific reporter activity in MCF7.; PELI2 expression is higher with the alt allele in TFAP2C-expressing breast cells.

Falsified if: TFAP2C binds both alleles equally or prefers the ref C allele.; The alt allele effect on reporter activity is unchanged by TFAP2C depletion.

### 4. H3: GATA3 binds the ref allele more strongly and loss of binding increases risk (p = 0.10)

TF GATA3 (stated coverage not_checked; registry own_model), ref allele binds more; element candidate distal enhancer at chr14:55887040; gene PELI2; cell type MCF7 breast cancer epithelial cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The ref C allele preserves a GATA3 binding site, so GATA3 binds the ref allele more strongly than the alt T allele. | missing | none |
| element | rs11629191 lies in a candidate distal enhancer active in MCF7 breast cancer cells. | missing | none |
| gene | GATA3 binding at this enhancer represses or buffers PELI2 expression, so the alt allele increases PELI2. | missing | none |
| cell_type | GATA3 is expressed in MCF7 breast cancer epithelial cells and contributes to breast epithelial enhancer regulation. | missing | none |
| phenotype | Loss of GATA3-mediated repression and increased PELI2 expression promote breast cancer risk or progression. | missing | none |

Predictions: GATA3 ChIP-qPCR or EMSA shows stronger binding to the ref C allele than to the alt T allele.; The alt allele increases reporter activity in MCF7, and GATA3 overexpression reduces this increase.; GATA3 depletion raises PELI2 expression, mimicking the alt allele.

Falsified if: GATA3 binds both alleles equally or prefers the alt T allele.; GATA3 overexpression does not repress the element or does not alter PELI2 expression.

### 5. H4: ESR1 binds the alt allele more strongly at an enhancer regulating PELI2 (p = 0.08)

TF ESR1 (stated coverage not_checked; registry own_model), alt allele binds more; element candidate distal enhancer at chr14:55887040; gene PELI2; cell type MCF7 breast cancer epithelial cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The alt T allele creates or strengthens an ESR1 binding site, so ESR1 binds the alt allele more strongly than the ref C allele. | missing | none |
| element | rs11629191 lies in a candidate distal enhancer active in MCF7 breast cancer cells. | missing | none |
| gene | ESR1 binding at this enhancer increases PELI2 expression. | missing | none |
| cell_type | MCF7 cells express ESR1 and use estrogen-receptor-dependent enhancers. | missing | none |
| phenotype | Increased ESR1-dependent PELI2 expression promotes breast cancer risk or progression. | missing | none |

Predictions: ESR1 ChIP-qPCR or EMSA shows stronger binding to the alt T allele than to the ref C allele.; The alt-allele reporter effect in MCF7 is estrogen-dependent and reduced by ESR1 knockdown or antagonist treatment.; PELI2 expression is higher with the alt allele in ESR1-positive breast cells.

Falsified if: ESR1 binds both alleles equally or prefers the ref C allele.; The alt-allele reporter effect is unchanged by ESR1 depletion or estrogen deprivation.

## Prediction matrix

| Test | Cost | Separates top two | H0 | H1 | H2 | H3 | H4 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Allele-specific FOXA1 ChIP-qPCR or EMSA at rs11629191 in MCF7 cells | low | yes | No allele-specific FOXA1 binding is detected at rs11629191. | FOXA1 binds the alt T allele more strongly than the ref C allele. |  |  |  |
| Allele-specific TFAP2C ChIP-qPCR or EMSA at rs11629191 in MCF7 cells | low | no | No allele-specific TFAP2C binding is detected. |  | TFAP2C binds the alt T allele more strongly than the ref C allele. |  |  |
| Allele-specific luciferase reporter for rs11629191 in MCF7 cells with FOXA1 knockdown | medium | yes | The two alleles show no reproducible difference in reporter activity. | The alt allele increases reporter activity and FOXA1 knockdown reduces the allelic difference. |  |  |  |

## Next experiment

Run allele-specific FOXA1 ChIP-qPCR or EMSA at rs11629191 in MCF7 cells; this is the cheapest test that directly separates the top non-null FOXA1 chain from the null by asking whether FOXA1 binding is stronger on the alt T allele.

## Flags

- none

## Evidence
