# rs11629191 and Breast cancer (v8, no_qbic, masked, seed 0)

Context: DepMap:ACH-000019 (MCF7) (given: given with the case).

**Verdict: no mechanism.** every chain was eliminated.

- TF mechanism: no mechanism (every chain was eliminated)
- Target gene: None (None: no chain)
- Disease link: no association (common variant (MAF 0.2736): neither the GWAS Catalog nor Open Targets lists an association with Breast cancer)

Cost $0.005 over 4 model calls; 78 s.

## Chains

| Rank | Chain | TF | Gene | Binding | Cell type | Element | Gene link | Disease | Status |
|---|---|---|---|---|---|---|---|---|---|
| - | H1 (F1) | CTCF | ENSG00000259868 | indirect | supporting | contradicted | untested | contradicted | eliminated: element: the variant is not in a cCRE and no TF is bound there in the context |

## Family screen

- F1 C2H2 ZF, 1 model: named CTCF; ChIP tier here 3, anywhere 2

## Next experiment

Test the C/T alleles in a validated allele-comparative CTCF binding assay, then assess allele-specific CTCF occupancy and regulatory effect in MCF7; the negative ChIP-seq result makes the in-cell follow-up especially important.

## Flags

- tool_failed: E15 gene_disease: Open Targets lookup failed: no Ensembl ID for ENSG00000259868
