# rs13078086 and Colorectal cancer (v8, full, masked, seed 1)

Context: DepMap:ACH-000971 (HCT 116) (given: given with the case).

**Verdict: no mechanism.** every chain was eliminated.

- TF mechanism: no mechanism (every chain was eliminated)
- Target gene: None (None: no chain)
- Disease link: no association (common variant (MAF 0.1652): neither the GWAS Catalog nor Open Targets lists an association with Colorectal cancer)

Cost $0.007 over 4 model calls; 121 s.

## Chains

| Rank | Chain | TF | Gene | Binding | Cell type | Element | Gene link | Disease | Status |
|---|---|---|---|---|---|---|---|---|---|
| - | H1 (F1) | EBF4 | PYDC2 | indirect | supporting | contradicted | indirect | contradicted | eliminated: element: the variant is not in a cCRE and no TF is bound there in the context |
| - | H2 (F2) | ZNF696 | PYDC2 | indirect | supporting | indirect | indirect | contradicted | eliminated: critic, on tested-negative evidence E27: E27 is a tested-negative result for the shared PYDC2-to-colorectal-cancer link, contradicting the phenotype arm required by this causal chain. |
| - | H3 (F3) | TFAP2E | PYDC2 | indirect | supporting | indirect | indirect | contradicted | eliminated: critic, on tested-negative evidence E27: E27 is a tested-negative result for the shared PYDC2-to-colorectal-cancer link, contradicting the phenotype arm required by this causal chain. |
| - | H4 (F4) | ZNF343 | PYDC2 | indirect | supporting | contradicted | indirect | contradicted | eliminated: element: the variant is not in a cCRE and no TF is bound there in the context |
| - | H5 (F5) | EHF | PYDC2 | indirect | supporting | contradicted | indirect | contradicted | eliminated: element: the variant is not in a cCRE and no TF is bound there in the context |

## Family screen

- F1 EBF1, 2 models: named EBF4 (z -60.28); ChIP tier here 3, anywhere 3
- F2 C2H2 ZF, 1 model: named ZNF696 (z 23.6); ChIP tier here 3, anywhere 3
- F3 AP-2, 4 models: named TFAP2E (z -18.37); ChIP tier here 3, anywhere 3
- F4 C2H2 ZF, 1 model: named ZNF343 (z 15.69); ChIP tier here 3, anywhere 3
- F5 Ets, 18 models: named EHF (z 13.11); ChIP tier here 3, anywhere 3
- F6 RFX, 4 models: named RFX2 (z -12.18); ChIP tier here 3, anywhere 3
- F7 C2H2 ZF, 1 model: named ZNF174 (z 11.98); ChIP tier here 3, anywhere 3
- F8 RFX, 2 models: named RFX5 (z -11.73); ChIP tier here 3, anywhere 3
- F9 C2H2 ZF, 1 model: named ZNF668 (z 10.82); ChIP tier here 3, anywhere 3
- F10 Unknown, 1 model: named TMF1 (z 10.65); ChIP tier here 3, anywhere 3
- F11 C2H2 ZF, 1 model: named ZNF518B (z 9.32); ChIP tier here 3, anywhere 3
- F12 SAND, 2 models: named SP140L (z 9.01); ChIP tier here 3, anywhere 3

## Next experiment

In HCT 116, introduce the two alleles by isogenic genome editing and measure allele-dependent occupancy of the nominated factor(s) together with expression of PYDC2 and nearby genes. This would test whether the predicted binding differences have endogenous regulatory consequences.

## Flags

- none
