# TERT promoter C228T and Glioblastoma, melanoma, bladder (v8, no_qbic, masked, seed 0)

Context: DepMap:subtype=Glioblastoma (median of 54 lines) (given: given with the case).

**Verdict: mechanism.** E2F1 meets every check.

- TF mechanism: mechanism (E2F1 meets every check)
- Target gene: TERT (direct: the variant is in the TERT promoter)
- Disease link: not testable (somatic variant: v2m has no tumour recurrence data)

Cost $0.008 over 3 model calls; 127 s.

## Chains

| Rank | Chain | TF | Gene | Binding | Cell type | Element | Gene link | Disease | Status |
|---|---|---|---|---|---|---|---|---|---|
| 1 | H1 (F1) | E2F1 | TERT | supporting | direct | supporting | direct | untested | kept |
| 2 | H4 (F4) | RELA | TERT | supporting | supporting | supporting | direct | untested | kept |
| 3 | H5 (F5) | SP1 | TERT | supporting | supporting | supporting | direct | untested | kept |
| 4 | H2 (F2) | JUN | TERT | indirect | supporting | supporting | direct | untested | kept |
| 5 | H3 (F3) | ETS1 | TERT | indirect | supporting | supporting | direct | untested | kept |

## Family screen

- F1 E2F, 4 models: named E2F1; ChIP tier here 2, anywhere 1
- F2 bZIP, 3 models: named JUN; ChIP tier here 3, anywhere 1
- F3 Ets, 18 models: named ETS1; ChIP tier here 3, anywhere 1
- F4 Rel, 1 model: named RELA; ChIP tier here 3, anywhere 1
- F5 C2H2 ZF, 5 models: named SP3; ChIP tier here 3, anywhere 1
- F6 Ets, 4 models: named ERF; ChIP tier here 3, anywhere 1
- F7 C2H2 ZF, 2 models: named KLF10; ChIP tier here 3, anywhere 1
- F8 Nuclear receptor, 4 models: named NR3C1; ChIP tier here 3, anywhere 1
- F9 Runt, 2 models: named RUNX1; ChIP tier here 3, anywhere 1
- F10 Ets, 1 model: named ELF2; ChIP tier here 3, anywhere 1
- F11 Unknown, 1 model: named SKI; ChIP tier here 3, anywhere 1
- F12 C2H2 ZF, 1 model: named KLF13; ChIP tier here 3, anywhere 1

## Next experiment

In a glioblastoma model, test allele-specific E2F1 and SP1 occupancy at the variant, then perturb the candidate TF or edit the variant and measure TERT expression. Include the nearby lncRNA transcript to distinguish target-gene effects.

## Flags

- none
