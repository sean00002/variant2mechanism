# rs7001688 and LDL cholesterol (v8, no_qbic, masked, seed 0)

Context: DepMap:ACH-000625 (Hep 3B2.1-7) (given: given with the case).

**Verdict: no mechanism.** every chain was eliminated.

- TF mechanism: no mechanism (every chain was eliminated)
- Target gene: None (None: no chain)
- Disease link: no association (common variant (MAF 0.4595): neither the GWAS Catalog nor Open Targets lists an association with LDL cholesterol)

Cost $0.004 over 4 model calls; 61 s.

## Chains

| Rank | Chain | TF | Gene | Binding | Cell type | Element | Gene link | Disease | Status |
|---|---|---|---|---|---|---|---|---|---|
| - | H1 (F1) | CTCF | FAM110B | indirect | supporting | contradicted | indirect | contradicted | eliminated: element: the variant is not in a cCRE and no TF is bound there in the context |

## Family screen

- F1 C2H2 ZF, 1 model: named CTCF; ChIP tier here 3, anywhere 2

## Next experiment

Create isogenic G and T alleles by endogenous base editing in Hep 3B2.1-7, then measure CTCF occupancy at the site (for example, by CUT&RUN) and expression of nearby candidate genes, including FAM110B. This would directly test allele-dependent occupancy and whether the variant affects a candidate target gene.

## Flags

- none
