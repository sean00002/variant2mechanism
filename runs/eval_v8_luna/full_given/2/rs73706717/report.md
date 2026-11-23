# rs73706717 and Colorectal cancer (8q24) (v8, full, masked, seed 2)

Context: DepMap:ACH-000971 (HCT 116) (given: given with the case).

**Verdict: no mechanism.** a molecular effect is possible, but the variant has no association with the disease (common variant (MAF 0.024): neither the GWAS Catalog nor Open Targets lists an association with Colorectal cancer (8q24)).

- TF mechanism: mechanism (TCF7L2 meets every check)
- Target gene: POU5F1B (indirect: Open Targets L2G 0.83)
- Disease link: no association (common variant (MAF 0.024): neither the GWAS Catalog nor Open Targets lists an association with Colorectal cancer (8q24))

Cost $0.012 over 6 model calls; 159 s.

## Chains

| Rank | Chain | TF | Gene | Binding | Cell type | Element | Gene link | Disease | Status |
|---|---|---|---|---|---|---|---|---|---|
| 1 | H2 (F2) | TCF7L2 | POU5F1B | supporting | direct | supporting | indirect | contradicted | kept |
| 2 | H1 (F1) | CTCF | POU5F1B | supporting | direct | supporting | indirect | contradicted | kept |
| 3 | H3 (F3) | SP1 | POU5F1B | supporting | direct | supporting | indirect | contradicted | kept |
| 4 | H4 (F4) | ZNF263 | POU5F1B | supporting | supporting | supporting | indirect | contradicted | kept |
| 5 | H5 (F5) | NR2F2 | POU5F1B | indirect | supporting | supporting | indirect | contradicted | kept |

## Family screen

- F1 C2H2 ZF, 1 model: named CTCF (z 8.21); ChIP tier here 2, anywhere 1
- F2 HMG/Sox, 3 models: named TCF7L2 (z -8.8); ChIP tier here 2, anywhere 2
- F3 C2H2 ZF, 5 models: named SP1 (z -7.07); ChIP tier here 2, anywhere 2
- F4 C2H2 ZF, 1 model: named ZNF263 (z -20.79); ChIP tier here 3, anywhere 1
- F5 Nuclear receptor, 29 models: named NR2F2 (z -15.02); ChIP tier here 3, anywhere 1
- F6 SMAD, 2 models: named SMAD3 (z 13.37); ChIP tier here 3, anywhere 1
- F7 Nuclear receptor, 4 models: named NR3C1 (z -12.32); ChIP tier here 3, anywhere 1
- F8 Homeodomain, 81 models: named HOXA9 (z -11.66); ChIP tier here 3, anywhere 1
- F9 HMG/Sox, 18 models: named SOX9 (z -10.49); ChIP tier here 3, anywhere 1
- F10 Nuclear receptor, 3 models: named VDR (z -9.23); ChIP tier here 3, anywhere 1
- F11 bZIP, 3 models: named JUNB (z -8.92); ChIP tier here 3, anywhere 1
- F12 Homeodomain, 4 models: named HOXB13 (z -8.04); ChIP tier here 3, anywhere 1

## Next experiment

In an appropriate colorectal context, perform allele-specific CTCF, TCF7L2, and SP1 occupancy assays at the variant, then use allele-specific element perturbation or CRISPR base editing to test effects on POU5F1B expression and chromatin contact. The new peaks do not resolve allele-specific binding or the element-to-gene link, so the next experiment is unchanged.

## Flags

- none
