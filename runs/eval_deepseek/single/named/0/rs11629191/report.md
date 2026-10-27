# rs11629191 and Breast cancer

Configuration `single`, named mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.00 over 1 model calls; 27 s.

Variant `chr14:55887040:C>T` (germline); expression context: DepMap:ACH-000019 (MCF7).

## Ranked chains

### 1. H0: Null: no TF-mediated allelic effect at rs11629191 (p = 0.45)

Null chain: no TF-mediated effect of this variant.

Predictions: No reproducible allele-specific TF binding at rs11629191 in MCF7.; No rs11629191-dependent enhancer activity difference in MCF7.; The breast-cancer association at this locus is explained by a linked causal variant or by chance/passenger status.

Falsified if: Allele-specific TF binding and enhancer activity are reproducibly detected for rs11629191 itself in MCF7.; An allelic swap at rs11629191 changes expression of a nearby gene in MCF7.

### 2. H1: FOXA1 binds the alt T allele in a breast-cancer enhancer (p = 0.22)

TF FOXA1 (stated coverage not_checked; registry own_model), alt allele binds more; element MCF7-active enhancer containing rs11629191; gene nearest expressed gene at the KTN1/PELI2 locus; cell type MCF7 breast cancer cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The alt T allele creates a stronger FOXA1 binding site than the ref C allele. | missing | none |
| element | rs11629191 lies in an enhancer that is active in MCF7 and whose activity is modulated by FOXA1 binding. | missing | none |
| gene | This enhancer regulates the nearest expressed gene at the KTN1/PELI2 locus. | missing | none |
| cell_type | MCF7 cells express FOXA1 and the target gene and have an active chromatin state at this element. | missing | none |
| phenotype | Altered FOXA1-dependent target-gene expression changes breast-cancer risk or tumor phenotype. | missing | none |

Predictions: FOXA1 ChIP or EMSA shows stronger binding to the T allele.; The T allele increases FOXA1-dependent reporter activity in MCF7.; FOXA1 knockdown or CRISPR perturbation reduces the allelic expression effect.

Falsified if: FOXA1 binds equally to both alleles or preferentially to the C allele.; The variant does not lie in an active MCF7 enhancer.; FOXA1 perturbation does not affect the nearby target gene.

### 3. H2: ESR1 binds the ref C allele in an estrogen-responsive enhancer (p = 0.15)

TF ESR1 (stated coverage not_checked; registry own_model), ref allele binds more; element estrogen-responsive enhancer containing rs11629191; gene nearest expressed gene at the KTN1/PELI2 locus; cell type MCF7 breast cancer cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The ref C allele binds ESR1 more strongly than the alt T allele. | missing | none |
| element | rs11629191 lies in an estrogen-responsive enhancer active in MCF7. | missing | none |
| gene | ESR1 binding at this element regulates the nearest expressed gene at the KTN1/PELI2 locus. | missing | none |
| cell_type | MCF7 cells are estrogen-receptor-positive and express the target gene. | missing | none |
| phenotype | Altered ESR1-dependent target expression contributes to breast-cancer risk or phenotype. | missing | none |

Predictions: ESR1 ChIP or EMSA shows stronger binding to the C allele.; Estrogen treatment changes enhancer activity and target-gene expression in an allele-specific manner.; ESR1 depletion reduces the effect.

Falsified if: ESR1 binds equally to both alleles or preferentially to the T allele.; The element is not estrogen-responsive in MCF7.; ESR1 depletion does not affect the target gene.

### 4. H3: GATA3 binds the ref C allele in a luminal enhancer (p = 0.10)

TF GATA3 (stated coverage not_checked; registry own_model), ref allele binds more; element GATA3-bound luminal enhancer containing rs11629191; gene nearest expressed gene at the KTN1/PELI2 locus; cell type MCF7 breast cancer cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The ref C allele creates a stronger GATA3 binding site than the alt T allele. | missing | none |
| element | rs11629191 lies in a GATA3-bound enhancer active in luminal breast cancer cells. | missing | none |
| gene | GATA3 binding at this enhancer regulates the nearest expressed gene at the KTN1/PELI2 locus. | missing | none |
| cell_type | MCF7 cells express GATA3 and have a luminal enhancer landscape at this locus. | missing | none |
| phenotype | Altered GATA3-dependent target expression affects breast-cancer risk or differentiation. | missing | none |

Predictions: GATA3 ChIP or EMSA shows stronger binding to the C allele.; The C allele increases GATA3-dependent reporter activity.; GATA3 depletion changes target-gene expression.

Falsified if: GATA3 binds equally to both alleles or preferentially to the T allele.; The element is not GATA3-bound or active in MCF7.; GATA3 depletion does not affect the target gene.

### 5. H4: RELA/NF-kB binds the alt T allele in an inflammatory enhancer (p = 0.08)

TF RELA (stated coverage not_checked; registry own_model), alt allele binds more; element NF-kB-responsive enhancer containing rs11629191; gene nearest expressed gene at the KTN1/PELI2 locus; cell type MCF7 breast cancer cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The alt T allele creates a stronger RELA/NF-kB binding site than the ref C allele. | missing | none |
| element | rs11629191 lies in an NF-kB-responsive enhancer active in MCF7. | missing | none |
| gene | RELA binding at this enhancer regulates the nearest expressed gene at the KTN1/PELI2 locus. | missing | none |
| cell_type | MCF7 cells have NF-kB signaling and express the target gene. | missing | none |
| phenotype | Altered NF-kB-dependent target expression contributes to breast-cancer risk or inflammatory phenotype. | missing | none |

Predictions: RELA ChIP or EMSA shows stronger binding to the T allele.; NF-kB stimulation increases T-allele reporter activity.; RELA knockdown reduces the effect.

Falsified if: RELA binds equally to both alleles or preferentially to the C allele.; The element is not NF-kB-responsive in MCF7.; RELA knockdown does not affect the target gene.

## Prediction matrix

| Test | Cost | Separates top two | H0 | H1 | H2 | H3 | H4 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Allele-specific EMSA using recombinant FOXA1 and rs11629191 C/T probes | low | yes | No differential FOXA1 binding between the C and T alleles | The T allele binds FOXA1 more strongly than the C allele |  |  |  |

## Next experiment

Run an allele-specific EMSA with recombinant FOXA1 and rs11629191 C/T probes to test the top non-null chain against the null.

## Flags

- none

## Evidence
