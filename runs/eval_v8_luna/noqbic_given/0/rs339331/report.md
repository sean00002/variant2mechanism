# rs339331 and Prostate cancer (6q22) (v8, no_qbic, masked, seed 0)

Context: DepMap:ACH-000977 (LNCaP clone FGC) (given: given with the case).

**Verdict: mechanism.** FOXA1 meets every check.

- TF mechanism: mechanism (FOXA1 meets every check)
- Target gene: RFX6 (indirect: Open Targets L2G 0.87)
- Disease link: supported (GWAS Catalog: Prostate cancer (p 5.0e-20); 33 matching association(s) in all)

Cost $0.010 over 5 model calls; 124 s.

## Chains

| Rank | Chain | TF | Gene | Binding | Cell type | Element | Gene link | Disease | Status |
|---|---|---|---|---|---|---|---|---|---|
| 1 | H1 (F2) | FOXA1 | RFX6 | direct | direct | supporting | indirect | direct | kept |
| 2 | H5 (F1) | NKX3-1 | RFX6 | direct | direct | supporting | indirect | direct | kept |
| 3 | H2 (F3) | HOXB13 | RFX6 | direct | direct | supporting | indirect | direct | kept |
| 4 | H3 (F4) | XBP1 | RFX6 | direct | direct | supporting | indirect | direct | kept |
| 5 | H4 (F5) | GATA2 | RFX6 | direct | direct | supporting | indirect | direct | kept |

## Family screen

- F1 Homeodomain, 2 models: named NKX3-1; ChIP tier here 1, anywhere 1
- F2 Forkhead, 4 models: named FOXA1; ChIP tier here 1, anywhere 1
- F3 Homeodomain, 4 models: named HOXB13; ChIP tier here 1, anywhere 1
- F4 bZIP, 1 model: named XBP1; ChIP tier here 1, anywhere 1
- F5 GATA, 6 models: named GATA2; ChIP tier here 1, anywhere 1
- F6 Nuclear receptor, 4 models: named AR; ChIP tier here 1, anywhere 1
- F7 Nuclear receptor, 29 models: named VDR; ChIP tier here 1, anywhere 1
- F8 Rel, 1 model: named RELA; ChIP tier here 1, anywhere 1
- F9 Nuclear receptor, 3 models: named NR1I3; ChIP tier here 1, anywhere 1
- F10 HMG/Sox, 18 models: named SOX12; ChIP tier here 3, anywhere 1
- F11 GATA, 1 model: named TRPS1; ChIP tier here 3, anywhere 1
- F12 Homeodomain, 9 models: named TGIF1; ChIP tier here 3, anywhere 2

## Next experiment

In LNCaP, perform allele-specific FOXA1, HOXB13, and XBP1 occupancy assays at the heterozygous site, then test the cCRE with allele-swapped reporter or CRISPR perturbation and measure RFX6 expression. This would test both the predicted C>T binding direction and the proposed regulatory target.

## Flags

- none
