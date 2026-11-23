# rs73706717 and Colorectal cancer (8q24) (v8, no_qbic, masked, seed 0)

Context: DepMap:ACH-000971 (HCT 116) (given: given with the case).

**Verdict: no mechanism.** a molecular effect is possible, but the variant has no association with the disease (common variant (MAF 0.024): neither the GWAS Catalog nor Open Targets lists an association with Colorectal cancer (8q24)).

- TF mechanism: mechanism (TCF7L2 meets every check)
- Target gene: POU5F1B (indirect: Open Targets L2G 0.83)
- Disease link: no association (common variant (MAF 0.024): neither the GWAS Catalog nor Open Targets lists an association with Colorectal cancer (8q24))

Cost $0.012 over 6 model calls; 155 s.

## Chains

| Rank | Chain | TF | Gene | Binding | Cell type | Element | Gene link | Disease | Status |
|---|---|---|---|---|---|---|---|---|---|
| 1 | H2 (F2) | TCF7L2 | POU5F1B | supporting | direct | supporting | indirect | contradicted | kept |
| 2 | H1 (F1) | CTCF | POU5F1B | supporting | direct | supporting | indirect | contradicted | kept |
| 3 | H3 (F3) | SP1 | POU5F1B | supporting | direct | supporting | indirect | contradicted | kept |
| 4 | H4 (F4) | DRAP1 | POU5F1B | supporting | supporting | supporting | indirect | contradicted | kept |
| 5 | H5 (F5) | HOXA9 | POU5F1B | untested | supporting | supporting | indirect | contradicted | kept |

## Family screen

- F1 C2H2 ZF, 1 model: named CTCF; ChIP tier here 2, anywhere 1
- F2 HMG/Sox, 3 models: named TCF7L2; ChIP tier here 2, anywhere 2
- F3 C2H2 ZF, 5 models: named SP1; ChIP tier here 2, anywhere 2
- F4 Unknown, 1 model: named DRAP1; ChIP tier here 3, anywhere 1
- F5 Homeodomain, 18 models: named HOXA9; ChIP tier here 3, anywhere 1
- F6 Homeodomain, 81 models: named MSX1; ChIP tier here 3, anywhere 1
- F7 Ets, 18 models: named EHF; ChIP tier here 3, anywhere 1
- F8 Nuclear receptor, 2 models: named NR2F2; ChIP tier here 3, anywhere 1
- F9 Nuclear receptor, 29 models: named PPARG; ChIP tier here 3, anywhere 1
- F10 SMAD, 2 models: named SMAD3; ChIP tier here 3, anywhere 1
- F11 HMG/Sox, 18 models: named SOX9; ChIP tier here 3, anywhere 1
- F12 C2H2 ZF, 1 model: named ZNF263; ChIP tier here 3, anywhere 1

## Next experiment

Precisely base-edit the T>C variant in isogenic HCT116 cells and measure allele-dependent expression of POU5F1B and other plausible linked genes; pair this with targeted TCF7L2, SP1, and CTCF occupancy or perturbation assays to test which, if any, mediates the effect.

## Flags

- none
