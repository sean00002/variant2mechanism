# rs56007086 and Breast cancer (16q12) (v8, full, masked, seed 0)

Context: DepMap:subtype=Breast Invasive Ductal Carcinoma (median of 32 lines) (cancer subtype: 'Breast cancer (16q12)' matches the DepMap Oncotree subtype 'Breast Invasive Ductal Carcinoma' (32 lines)).

**Verdict: no mechanism.** a molecular effect is possible, but the variant has no association with the disease (common variant (MAF 0.0486): neither the GWAS Catalog nor Open Targets lists an association with Breast cancer (16q12)).

- TF mechanism: mechanism (ESR1 meets every check)
- Target gene: TOX3 (indirect: TOX3 is the nearest gene or overlaps the variant)
- Disease link: no association (common variant (MAF 0.0486): neither the GWAS Catalog nor Open Targets lists an association with Breast cancer (16q12))

Cost $0.011 over 6 model calls; 133 s.

## Chains

| Rank | Chain | TF | Gene | Binding | Cell type | Element | Gene link | Disease | Status |
|---|---|---|---|---|---|---|---|---|---|
| 1 | H1 (F1) | ESR1 | TOX3 | direct | direct | indirect | indirect | contradicted | kept |
| 2 | H2 (F2) | ESR1 | TOX3 | direct | direct | indirect | indirect | contradicted | kept |
| 3 | H4 (F3) | FOXA1 | TOX3 | supporting | direct | indirect | indirect | contradicted | kept |
| 4 | H5 (F4) | NR3C1 | TOX3 | supporting | direct | indirect | indirect | contradicted | kept |
| 5 | H3 (F5) | GATA3 | TOX3 | supporting | direct | indirect | indirect | contradicted | kept |

## Family screen

- F1 Nuclear receptor, 3 models: named ESR1 (z 11.04); ChIP tier here 1, anywhere 1
- F2 Nuclear receptor, 29 models: named ESRRA (z 10.89); ChIP tier here 1, anywhere 1
- F3 Forkhead, 4 models: named FOXA1 (z 6.27); ChIP tier here 2, anywhere 1
- F4 Nuclear receptor, 4 models: named NR3C1 (z -5.03); ChIP tier here 2, anywhere 1
- F5 GATA, 6 models: named GATA3 (z 8.32); ChIP tier here 2, anywhere 2
- F6 C2H2 ZF, 5 models: named SP3 (z 14.89); ChIP tier here 3, anywhere 1
- F7 bZIP, 2 models: named CREB1 (z 13.51); ChIP tier here 3, anywhere 1
- F8 TEA, 4 models: named TEAD3 (z 12.64); ChIP tier here 3, anywhere 1
- F9 HMG/Sox, 3 models: named TCF7L2 (z 12.52); ChIP tier here 3, anywhere 1
- F10 bZIP, 1 model: named XBP1 (z 12.04); ChIP tier here 3, anywhere 1
- F11 bZIP, 3 models: named ATF2 (z 10.73); ChIP tier here 3, anywhere 1
- F12 bHLH, 2 models: named BHLHE40 (z 10.51); ChIP tier here 3, anywhere 1

## Next experiment

In an appropriate ER-positive breast cancer model such as MCF-7, test the alleles directly with matched G>A and G>G sequence reporters or an isogenic edit, measuring allele-specific occupancy for ESR1, GATA3, and FOXA1 and expression of candidate nearby genes including TOX3. TF perturbation alongside the allele comparison would help distinguish occupancy from causal regulatory effects.

## Flags

- none
