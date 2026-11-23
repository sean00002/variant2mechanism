# rs12740374 and LDL cholesterol, myocardial infarction (1p13) (v8, no_qbic, masked, seed 0)

Context: DepMap:ACH-000625 (Hep 3B2.1-7) (given: given with the case).

**Verdict: mechanism.** HNF4A meets every check.

- TF mechanism: mechanism (HNF4A meets every check)
- Target gene: SORT1 (direct: eQTL for SORT1 in Liver (NES +1.27))
- Disease link: supported (GWAS Catalog: low density lipoprotein cholesterol (LDLC, maximum, inv-norm transformed) (p 4.0e-164); 107 matching association(s) in all)

Cost $0.014 over 5 model calls; 173 s.

## Chains

| Rank | Chain | TF | Gene | Binding | Cell type | Element | Gene link | Disease | Status |
|---|---|---|---|---|---|---|---|---|---|
| 1 | H2 (F2) | HNF4A | SORT1 | direct | direct | direct | direct | direct | kept |
| 2 | H3 (F3) | HNF4G | SORT1 | direct | direct | direct | direct | direct | kept |
| 3 | H5 (F5) | SOX13 | SORT1 | direct | direct | direct | direct | direct | kept |
| 4 | H4 (F4) | PPARG | SORT1 | supporting | direct | direct | direct | direct | kept |
| - | H1 (F1) | GABPA | SORT1 | direct | direct | direct | direct | direct | eliminated: critic, on tested-negative evidence E25: The tested-negative HepG2 result reports no GABPA ChIP-seq peak containing the variant, contradicting GABPA occupancy at the variant in the matched cell type required by this candidate mechanism. |

## Family screen

- F1 Ets, 18 models: named GABPA; ChIP tier here 1, anywhere 1
- F2 Nuclear receptor, 1 model: named HNF4A; ChIP tier here 1, anywhere 1
- F3 Nuclear receptor, 2 models: named HNF4G; ChIP tier here 1, anywhere 1
- F4 Nuclear receptor, 29 models: named PPARG; ChIP tier here 1, anywhere 1
- F5 HMG/Sox, 18 models: named SOX13; ChIP tier here 1, anywhere 1
- F6 SMAD, 4 models: named NFIC; ChIP tier here 1, anywhere 1
- F7 C2H2 ZF, 5 models: named SP1; ChIP tier here 1, anywhere 1
- F8 Forkhead, 1 model: named FOXP1; ChIP tier here 1, anywhere 1
- F9 Forkhead, 10 models: named FOXP4; ChIP tier here 1, anywhere 1
- F10 Forkhead, 2 models: named FOXK2; ChIP tier here 1, anywhere 1
- F11 bZIP, 2 models: named CREM; ChIP tier here 1, anywhere 1
- F12 Forkhead, 4 models: named FOXO1; ChIP tier here 1, anywhere 1

## Next experiment

In HepG2, perform allele-resolved editing of the variant or an allele-specific enhancer assay at EH38E1374646 while perturbing HNF4A, with SORT1 expression as a readout; include HNF4G perturbation as a comparator to distinguish the competing nuclear-receptor candidates.

## Flags

- none
