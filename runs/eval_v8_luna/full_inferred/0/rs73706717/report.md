# rs73706717 and Colorectal cancer (8q24) (v8, full, masked, seed 0)

Context: DepMap:subtype=Colon Adenocarcinoma (median of 66 lines) (cancer subtype: 'Colorectal cancer (8q24)' matches the DepMap Oncotree subtype 'Colon Adenocarcinoma' (66 lines)).

**Verdict: no mechanism.** a molecular effect is possible, but the variant has no association with the disease (common variant (MAF 0.024): neither the GWAS Catalog nor Open Targets lists an association with Colorectal cancer (8q24)).

- TF mechanism: mechanism (HNF4A meets every check)
- Target gene: POU5F1B (indirect: Open Targets L2G 0.83)
- Disease link: no association (common variant (MAF 0.024): neither the GWAS Catalog nor Open Targets lists an association with Colorectal cancer (8q24))

Cost $0.012 over 6 model calls; 135 s.

## Chains

| Rank | Chain | TF | Gene | Binding | Cell type | Element | Gene link | Disease | Status |
|---|---|---|---|---|---|---|---|---|---|
| 1 | H1 (F1) | HNF4A | POU5F1B | direct | direct | direct | indirect | contradicted | kept |
| 2 | H2 (F2) | SOX9 | POU5F1B | direct | direct | direct | indirect | contradicted | kept |
| 3 | H3 (F3) | VDR | POU5F1B | supporting | direct | direct | indirect | contradicted | kept |
| 4 | H4 (F4) | JUND | POU5F1B | supporting | direct | direct | indirect | contradicted | kept |
| 5 | H5 (F5) | CTCF | POU5F1B | supporting | direct | direct | indirect | contradicted | kept |

## Family screen

- F1 Nuclear receptor, 29 models: named HNF4A (z -15.02); ChIP tier here 1, anywhere 1
- F2 HMG/Sox, 18 models: named SOX9 (z -10.49); ChIP tier here 1, anywhere 1
- F3 Nuclear receptor, 3 models: named VDR (z -9.23); ChIP tier here 2, anywhere 1
- F4 bZIP, 3 models: named JUND (z -8.92); ChIP tier here 2, anywhere 1
- F5 C2H2 ZF, 1 model: named CTCF (z 8.21); ChIP tier here 2, anywhere 1
- F6 HMG/Sox, 3 models: named TCF7L2 (z -8.8); ChIP tier here 2, anywhere 2
- F7 C2H2 ZF, 6 models: named KLF5 (z -7.81); ChIP tier here 2, anywhere 2
- F8 C2H2 ZF, 5 models: named SP1 (z -7.07); ChIP tier here 2, anywhere 2
- F9 Homeodomain, 3 models: named CDX2 (z -4.87); ChIP tier here 2, anywhere 2
- F10 C2H2 ZF, 1 model: named ZNF263 (z -20.79); ChIP tier here 3, anywhere 1
- F11 SMAD, 2 models: named SMAD5 (z 13.37); ChIP tier here 3, anywhere 1
- F12 Homeodomain, 81 models: named HOXA9 (z -11.66); ChIP tier here 3, anywhere 1

## Next experiment

Use an isogenic T/C allele-swap in a relevant colon cancer cell model, then measure allele-specific occupancy for the prioritized TF candidates and expression of POU5F1B plus the other linked genes. This would test whether the predicted binding difference produces a cis-regulatory effect and identify its target.

## Flags

- none
