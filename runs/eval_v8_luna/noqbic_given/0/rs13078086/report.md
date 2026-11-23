# rs13078086 and Colorectal cancer (v8, no_qbic, masked, seed 0)

Context: DepMap:ACH-000971 (HCT 116) (given: given with the case).

**Verdict: no mechanism.** every chain was eliminated.

- TF mechanism: no mechanism (every chain was eliminated)
- Target gene: None (None: no chain)
- Disease link: no association (common variant (MAF 0.1652): neither the GWAS Catalog nor Open Targets lists an association with Colorectal cancer)

Cost $0.006 over 4 model calls; 106 s.

## Chains

| Rank | Chain | TF | Gene | Binding | Cell type | Element | Gene link | Disease | Status |
|---|---|---|---|---|---|---|---|---|---|
| - | H1 (F1) | JUNB | PYDC2 | indirect | supporting | contradicted | indirect | contradicted | eliminated: element: the variant is not in a cCRE and no TF is bound there in the context |
| - | H2 (F2) | BATF3 | PYDC2 | indirect | supporting | contradicted | indirect | contradicted | eliminated: element: the variant is not in a cCRE and no TF is bound there in the context |

## Family screen

- F1 bZIP, 3 models: named JUNB; ChIP tier here 3, anywhere 2
- F2 bZIP, 2 models: named BATF3; ChIP tier here 3, anywhere 2

## Next experiment

No change: test allele-specific JUNB and BATF3 occupancy at the locus in HCT 116, followed by TF perturbation and measurement of candidate-element activity and PYDC2 expression.

## Flags

- none
