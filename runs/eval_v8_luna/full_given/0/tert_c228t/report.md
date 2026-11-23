# TERT promoter C228T and Glioblastoma, melanoma, bladder (v8, full, masked, seed 0)

Context: DepMap:subtype=Glioblastoma (median of 54 lines) (given: given with the case).

**Verdict: mechanism.** E2F1 meets every check.

- TF mechanism: mechanism (E2F1 meets every check)
- Target gene: TERT (direct: the variant is in the TERT promoter)
- Disease link: not testable (somatic variant: v2m has no tumour recurrence data)

Cost $0.000 over 3 model calls; 8 s.

## Chains

| Rank | Chain | TF | Gene | Binding | Cell type | Element | Gene link | Disease | Status |
|---|---|---|---|---|---|---|---|---|---|
| 1 | H1 (F1) | E2F1 | TERT | supporting | direct | supporting | direct | untested | kept |
| 2 | H3 (F5) | ZBTB7A | TERT | supporting | supporting | supporting | direct | untested | kept |
| 3 | H2 (F2) | ETS1 | TERT | indirect | supporting | supporting | direct | untested | kept |
| 4 | H4 (F3) | ERF | TERT | indirect | supporting | supporting | direct | untested | kept |
| 5 | H5 (F4) | ELF2 | TERT | indirect | supporting | supporting | direct | untested | kept |

## Family screen

- F1 E2F, 4 models: named E2F1 (z 5.78); ChIP tier here 2, anywhere 1
- F2 Ets, 18 models: named ETS1 (z 166.19); ChIP tier here 3, anywhere 1
- F3 Ets, 4 models: named ERF (z 70.12); ChIP tier here 3, anywhere 1
- F4 Ets, 1 model: named ELF2 (z 47.58); ChIP tier here 3, anywhere 1
- F5 C2H2 ZF, 1 model: named ZBTB7A (z -14.11); ChIP tier here 3, anywhere 1
- F6 Unknown, 1 model: named SKI (z -13.66); ChIP tier here 3, anywhere 1
- F7 C2H2 ZF, 5 models: named SP3 (z 11.81); ChIP tier here 3, anywhere 1
- F8 Homeodomain, 3 models: named SIX5 (z 8.12); ChIP tier here 3, anywhere 1
- F9 Nuclear receptor, 4 models: named NR3C1 (z 6.5); ChIP tier here 3, anywhere 1
- F10 AP-2, 4 models: named TFAP2A (z -36.84); ChIP tier here 3, anywhere 2
- F11 C2H2 ZF, 4 models: named ZIC1 (z -20.85); ChIP tier here 3, anywhere 2
- F12 C2H2 ZF, 1 model: named CTCF (z -14.7); ChIP tier here 3, anywhere 2

## Next experiment

In U-87 MG cells, perform allele-specific occupancy testing at the endogenous locus (CUT&RUN or ChIP for E2F1 and ETS1, with an allele-discriminating readout), paired with isogenic G>A editing and TERT expression measurement. This would test the predicted binding direction and whether either factor links the variant to TERT regulation.

## Flags

- none
