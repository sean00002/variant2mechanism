# rs34768248 and Glioblastoma, melanoma, bladder (v8, full, masked, seed None)

Context: DepMap:subtype=Glioblastoma (median of 54 lines) (given: given with the case).

**Verdict: no mechanism.** a molecular effect is possible, but the variant has no association with the disease (common variant (MAF 0.0271): neither the GWAS Catalog nor Open Targets lists an association with Glioblastoma, melanoma, bladder).

- TF mechanism: mechanism (TCF3 meets every check)
- Target gene: TERT (direct: the variant is in the TERT promoter)
- Disease link: no association (common variant (MAF 0.0271): neither the GWAS Catalog nor Open Targets lists an association with Glioblastoma, melanoma, bladder)

Cost $0.000 over 0 model calls; 1 s.

## Chains

| Rank | Chain | TF | Gene | Binding | Cell type | Element | Gene link | Disease | Status |
|---|---|---|---|---|---|---|---|---|---|
| 1 | H3 (F3) | TCF3 | TERT | indirect | supporting | indirect | direct | contradicted | kept |
| - | H1 (F1) | ETS1 | TERT | indirect | supporting | contradicted | direct | contradicted | eliminated: element: the variant is not in a cCRE and no TF is bound there in the context |
| - | H2 (F2) | RUNX1 | TERT | supporting | supporting | contradicted | direct | contradicted | eliminated: element: the variant is not in a cCRE and no TF is bound there in the context |
| - | H4 (F4) | NKRF | TERT | indirect | supporting | contradicted | direct | contradicted | eliminated: element: the variant is not in a cCRE and no TF is bound there in the context |
| - | H5 (F5) | KLF6 | TERT | indirect | supporting | contradicted | direct | contradicted | eliminated: element: the variant is not in a cCRE and no TF is bound there in the context |

## Family screen

- F1 Ets, 18 models: named ETS1 (z -14.14); ChIP tier here 3, anywhere 1
- F2 Runt, 2 models: named RUNX1 (z -5.7); ChIP tier here 3, anywhere 1
- F3 bHLH, 3 models: named TCF3 (z 87.39); ChIP tier here 3, anywhere 2
- F4 Unknown, 1 model: named NKRF (z -12.31); ChIP tier here 3, anywhere 2
- F5 C2H2 ZF, 6 models: named KLF6 (z -11.26); ChIP tier here 3, anywhere 2
- F6 E2F, 4 models: named E2F4 (z -9.62); ChIP tier here 3, anywhere 2
- F7 C2H2 ZF, 2 models: named ZNF76 (z 7.89); ChIP tier here 3, anywhere 2
- F8 Nuclear receptor, 29 models: named NR1H2 (z 7.56); ChIP tier here 3, anywhere 2
- F9 bHLH, 2 models: named SREBF1 (z 7.43); ChIP tier here 3, anywhere 2
- F10 C2H2 ZF, 1 model: named SNAI2 (z 6.75); ChIP tier here 3, anywhere 2
- F11 C2H2 ZF, 1 model: named ZNF800 (z 6.43); ChIP tier here 3, anywhere 2
- F12 bZIP, 2 models: named CREB1 (z 6.24); ChIP tier here 3, anywhere 2

## Next experiment

none

## Flags

- none
