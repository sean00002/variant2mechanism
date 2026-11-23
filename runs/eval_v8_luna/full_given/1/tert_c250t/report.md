# TERT promoter C250T and Glioblastoma, melanoma, bladder (v8, full, masked, seed 1)

Context: DepMap:subtype=Glioblastoma (median of 54 lines) (given: given with the case).

**Verdict: mechanism.** E2F1 meets every check.

- TF mechanism: mechanism (E2F1 meets every check)
- Target gene: TERT (direct: the variant is in the TERT promoter)
- Disease link: not testable (somatic variant: v2m has no tumour recurrence data)

Cost $0.008 over 3 model calls; 125 s.

## Chains

| Rank | Chain | TF | Gene | Binding | Cell type | Element | Gene link | Disease | Status |
|---|---|---|---|---|---|---|---|---|---|
| 1 | H1 (F1) | E2F1 | TERT | supporting | direct | supporting | direct | untested | kept |
| 2 | H3 (F3) | SKI | TERT | supporting | supporting | supporting | direct | untested | kept |
| 3 | H4 (F4) | ZBTB7A | TERT | supporting | supporting | supporting | direct | untested | kept |
| 4 | H5 (F5) | NR3C1 | TERT | supporting | supporting | supporting | direct | untested | kept |
| 5 | H2 (F2) | ETS1 | TERT | indirect | supporting | supporting | direct | untested | kept |

## Family screen

- F1 E2F, 4 models: named E2F1 (z -5.4); ChIP tier here 2, anywhere 2
- F2 Ets, 18 models: named ETS1 (z 167.5); ChIP tier here 3, anywhere 1
- F3 Unknown, 1 model: named SKI (z -17.92); ChIP tier here 3, anywhere 1
- F4 C2H2 ZF, 1 model: named ZBTB7A (z -10.91); ChIP tier here 3, anywhere 1
- F5 Nuclear receptor, 4 models: named NR3C1 (z 7.78); ChIP tier here 3, anywhere 1
- F6 C2H2 ZF, 5 models: named SP3 (z -7.5); ChIP tier here 3, anywhere 1
- F7 bZIP, 3 models: named JUN (z 5.17); ChIP tier here 3, anywhere 1
- F8 Ets, 4 models: named ERF (z 114.84); ChIP tier here 3, anywhere 2
- F9 Ets, 1 model: named ELF2 (z 78.05); ChIP tier here 3, anywhere 2
- F10 C2H2 ZF, 6 models: named KLF6 (z -15.38); ChIP tier here 3, anywhere 2
- F11 Nuclear receptor, 29 models: named NR1H2 (z 15.31); ChIP tier here 3, anywhere 2
- F12 Unknown, 1 model: named SAFB (z -14.52); ChIP tier here 3, anywhere 2

## Next experiment

In a glioblastoma model such as U-87MG, introduce the G>A allele and the reciprocal correction with isogenic base editing. Measure TERT expression and allele-specific E2F1 occupancy; this would test whether the variant changes transcription in a context where E2F1 occupancy is observed.

## Flags

- none
