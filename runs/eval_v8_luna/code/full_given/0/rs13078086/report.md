# rs13078086 and Colorectal cancer (v8, full, masked, seed None)

Context: DepMap:ACH-000971 (HCT 116) (given: given with the case).

**Verdict: no mechanism.** no chain meets the minimum; the top chain (ZNF696) fails: ChIP-seq.

- TF mechanism: no mechanism (no chain meets the minimum; the top chain (ZNF696) fails: ChIP-seq)
- Target gene: PYDC2 (indirect: PYDC2 is the nearest gene or overlaps the variant)
- Disease link: no association (common variant (MAF 0.1652): neither the GWAS Catalog nor Open Targets lists an association with Colorectal cancer)

Cost $0.000 over 0 model calls; 1 s.

## Chains

| Rank | Chain | TF | Gene | Binding | Cell type | Element | Gene link | Disease | Status |
|---|---|---|---|---|---|---|---|---|---|
| 1 | H2 (F2) | ZNF696 | PYDC2 | indirect | supporting | indirect | indirect | contradicted | kept |
| 2 | H3 (F3) | TFAP2E | PYDC2 | indirect | supporting | indirect | indirect | contradicted | kept |
| - | H1 (F1) | EBF4 | PYDC2 | indirect | supporting | contradicted | indirect | contradicted | eliminated: element: the variant is not in a cCRE and no TF is bound there in the context |
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

none

## Flags

- none
