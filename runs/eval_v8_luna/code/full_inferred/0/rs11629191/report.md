# rs11629191 and Breast cancer (v8, full, masked, seed None)

Context: DepMap:subtype=Breast Invasive Ductal Carcinoma (median of 32 lines) (cancer subtype: 'Breast cancer' matches the DepMap Oncotree subtype 'Breast Invasive Ductal Carcinoma' (32 lines)).

**Verdict: no mechanism.** no chain meets the minimum; the top chain (XBP1) fails: ChIP-seq.

- TF mechanism: no mechanism (no chain meets the minimum; the top chain (XBP1) fails: ChIP-seq)
- Target gene: PELI2 (indirect: PELI2 is the nearest gene or overlaps the variant)
- Disease link: no association (common variant (MAF 0.2736): neither the GWAS Catalog nor Open Targets lists an association with Breast cancer)

Cost $0.000 over 0 model calls; 1 s.

## Chains

| Rank | Chain | TF | Gene | Binding | Cell type | Element | Gene link | Disease | Status |
|---|---|---|---|---|---|---|---|---|---|
| 1 | H1 (F1) | XBP1 | PELI2 | indirect | supporting | indirect | indirect | contradicted | kept |
| 2 | H2 (F2) | CREB3 | PELI2 | indirect | supporting | indirect | indirect | contradicted | kept |
| 3 | H3 (F3) | SP140L | PELI2 | indirect | supporting | indirect | indirect | contradicted | kept |
| 4 | H4 (F4) | ATF2 | PELI2 | indirect | supporting | indirect | indirect | contradicted | kept |
| - | H5 (F5) | CXXC5 | PELI2 | indirect | supporting | contradicted | indirect | contradicted | eliminated: element: the variant is not in a cCRE and no TF is bound there in the context |

## Family screen

- F1 bZIP, 1 model: named XBP1 (z -91.69); ChIP tier here 3, anywhere 3
- F2 bZIP, 4 models: named CREB3 (z -76.89); ChIP tier here 3, anywhere 3
- F3 SAND, 2 models: named SP140L (z -57.31); ChIP tier here 3, anywhere 3
- F4 bZIP, 3 models: named ATF2 (z -49.19); ChIP tier here 3, anywhere 3
- F5 CxxC, 2 models: named CXXC5 (z -44.11); ChIP tier here 3, anywhere 3
- F6 Homeodomain, 9 models: named TGIF1 (z -38.69); ChIP tier here 3, anywhere 3
- F7 bZIP, 6 models: named MAFK (z -38.05); ChIP tier here 3, anywhere 3
- F8 bHLH, 1 model: named USF3 (z -37.78); ChIP tier here 3, anywhere 3
- F9 bZIP, 2 models: named CREB1 (z -37.47); ChIP tier here 3, anywhere 3
- F10 C2H2 ZF, 1 model: named ZBTB18 (z 33.3); ChIP tier here 3, anywhere 3
- F11 C2H2 ZF, 4 models: named EGR1 (z -30.48); ChIP tier here 3, anywhere 3
- F12 bZIP, 1 model: named MAFF (z -29.97); ChIP tier here 3, anywhere 3

## Next experiment

none

## Flags

- none
