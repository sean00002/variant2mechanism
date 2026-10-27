# rs2168101 and Neuroblastoma (LMO1)

Configuration `single`, named mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.00 over 1 model calls; 16 s.

Variant `chr11:8233861:C>A` (germline); expression context: DepMap:ACH-000149 (SK-N-SH).

## Ranked chains

### 1. C1: GATA2 alt-binding enhancer activation (p = 0.42)

TF GATA2 (QBiC-SELEX coverage own_model), alt allele binds more; element LMO1 enhancer; gene LMO1; cell type neuroblastoma/sympathetic neural crest.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | GATA2 binds the alt A allele more strongly than ref C; no QBiC-SELEX data are supplied in this prompt, so this is based on GATA motif logic and GATA2 neuroblastoma enhancer biology. | missing | none |
| element | The alt A allele creates or strengthens a functional GATA2-responsive element in the LMO1 regulatory region. | missing | none |
| gene | Increased GATA2 occupancy at this element increases LMO1 expression. | missing | none |
| cell_type | This occurs in SK-N-SH-like sympathetic neuroblastoma cells, where LMO1 is expressed and GATA2 is relevant. | missing | none |
| phenotype | Higher LMO1 expression increases neuroblastoma risk or aggressiveness. | missing | none |

Predictions: Allele-specific GATA2 ChIP-qPCR shows more GATA2 on alt A than ref C at rs2168101.; LMO1 enhancer reporter is more active with alt A than ref C in SK-N-SH.; GATA2 knockdown reduces LMO1 expression in cells carrying alt A.

Falsified if: Alt A does not increase GATA2 occupancy at rs2168101 in SK-N-SH or other sympathetic neuroblastoma cells.; The rs2168101 alt allele does not increase LMO1 enhancer reporter activity or endogenous LMO1 expression.; Conditioning on a linked variant abolishes the rs2168101 association.

### 2. C4: No TF-mediated allelic effect (p = 0.35)

Null chain: no TF-mediated effect of this variant.

Predictions: No allele-specific TF occupancy at rs2168101.; No allele-specific LMO1 enhancer reporter difference.; The association is explained by a linked causal variant, a passenger event at a mutational hotspot, or no allelic effect.

Falsified if: Allele-specific GATA2 or GATA3 occupancy and allele-specific LMO1 enhancer activity are reproducibly detected.; Conditioning on a linked variant does not explain the association.; Perturbing GATA2 or GATA3 changes LMO1 expression in an rs2168101 allele-dependent manner.

### 3. C2: GATA3 alt-binding enhancer activation (p = 0.13)

TF GATA3 (QBiC-SELEX coverage own_model), alt allele binds more; element LMO1 enhancer; gene LMO1; cell type neuroblastoma/sympathetic neural crest.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | GATA3, a related GATA-family TF, binds the alt A allele more strongly than ref C; no QBiC-SELEX data are supplied in this prompt, so this is motif-based and GATA3 is included because related TFs share specificity. | missing | none |
| element | The alt A allele creates or strengthens a functional GATA3-responsive element in the LMO1 regulatory region. | missing | none |
| gene | Increased GATA3 occupancy at this element increases LMO1 expression. | missing | none |
| cell_type | This occurs in SK-N-SH-like sympathetic neuroblastoma cells. | missing | none |
| phenotype | Higher LMO1 expression increases neuroblastoma risk or aggressiveness. | missing | none |

Predictions: Allele-specific GATA3 ChIP-qPCR shows more GATA3 on alt A than ref C at rs2168101.; GATA3 knockdown reduces LMO1 expression in cells carrying alt A more than GATA2 knockdown.; GATA3 supershift, not GATA2 supershift, changes the allele-specific EMSA band.

Falsified if: GATA3 does not occupy rs2168101 in SK-N-SH or other neuroblastoma cells.; GATA3 knockdown, but not GATA2 knockdown, changes LMO1 expression from the alt allele.; GATA2, not GATA3, is the predominant factor at this element.

### 4. C3: GATA2 alt-binding repressive/context-dependent effect (p = 0.10)

TF GATA2 (QBiC-SELEX coverage own_model), alt allele binds more; element LMO1 regulatory element, context-dependent repressive or competitive effect; gene LMO1; cell type neuroblastoma/sympathetic neural crest.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | GATA2 binds the alt A allele more strongly than ref C; no QBiC-SELEX data are supplied in this prompt. GATA2 is considered because the allele is predicted to alter a GATA motif. | missing | none |
| element | The alt A allele creates a GATA2-bound element that is repressive or competes with an activating element in this context. | missing | none |
| gene | Increased GATA2 occupancy at this element decreases LMO1 expression. | missing | none |
| cell_type | This repressive effect occurs in SK-N-SH-like sympathetic neuroblastoma cells. | missing | none |
| phenotype | Lower LMO1 expression would be protective or alter neuroblastoma differentiation, depending on context. | missing | none |

Predictions: Allele-specific GATA2 ChIP-qPCR shows more GATA2 on alt A.; LMO1 enhancer reporter is less active with alt A than ref C in SK-N-SH.; GATA2 knockdown increases LMO1 expression in cells carrying alt A.

Falsified if: Alt A increases rather than decreases LMO1 expression in allele-matched reporter and endogenous-expression assays.; GATA2 occupancy is absent or not allele-specific at rs2168101.; The variant has no effect on LMO1 expression after GATA2 perturbation.

## Prediction matrix

| Test | Cost | Separates top two | C1 | C4 | C2 | C3 |
| --- | --- | --- | --- | --- | --- | --- |
| Allele-specific ChIP-qPCR for GATA2 and GATA3 at rs2168101 in SK-N-SH or another heterozygous sympathetic neuroblastoma line, with genotype-matched input. | low | yes | GATA2 ChIP-qPCR signal enriched on alt A | No allele-specific GATA2 or GATA3 occupancy | GATA3 ChIP-qPCR signal enriched on alt A | GATA2 ChIP-qPCR signal enriched on alt A, but reporter activity lower for alt A |

## Next experiment

Cheapest single experiment separating the top two chains: allele-specific ChIP-qPCR for GATA2 versus GATA3 at rs2168101 in SK-N-SH or another heterozygous neuroblastoma cell line. C1 predicts GATA2 enrichment on alt A; C2 predicts GATA3 enrichment on alt A; C4 predicts no allele-specific enrichment.

## Flags

- none

## Evidence
