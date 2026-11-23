# rs642961 and Cleft lip (IRF6) (v8, full, masked, seed 0)

Context: GTEx:Nerve - Tibial (eQTL tissue: the variant's strongest GTEx eQTL is for SYT14 in Nerve - Tibial (p 6.7e-20)).

**Verdict: mechanism.** TFAP2E meets every check.

- TF mechanism: mechanism (TFAP2E meets every check)
- Target gene: IRF6 (supporting: eQTL for IRF6 in Brain_Cerebellum (another tissue))
- Disease link: supported (Open Targets credible set: Orofacial clefts (PIP 0.05); 1 matching association(s) in all)

Cost $0.011 over 5 model calls; 126 s.

## Chains

| Rank | Chain | TF | Gene | Binding | Cell type | Element | Gene link | Disease | Status |
|---|---|---|---|---|---|---|---|---|---|
| 1 | H3 (F1) | TFAP2E | IRF6 | indirect | supporting | indirect | supporting | direct | kept |
| 2 | H4 (F2) | ZNF76 | IRF6 | indirect | supporting | indirect | supporting | direct | kept |
| 3 | H2 (F4) | TEAD1 | IRF6 | indirect | supporting | indirect | supporting | direct | kept |
| - | H1 (F3) | ETS2 | IRF6 | indirect | supporting | contradicted | supporting | direct | eliminated: element: inactive (Low-DNase) in tibial nerve, and no TF bound there |
| - | H5 (F5) | ERF | IRF6 | indirect | supporting | contradicted | supporting | direct | eliminated: element: inactive (Low-DNase) in tibial nerve, and no TF bound there |

## Family screen

- F1 AP-2, 4 models: named TFAP2E (z 23.98); ChIP tier here 3, anywhere 1
- F2 C2H2 ZF, 2 models: named ZNF76 (z -15.44); ChIP tier here 3, anywhere 1
- F3 Ets, 18 models: named ETS2 (z 77.65); ChIP tier here 3, anywhere 2
- F4 TEA, 4 models: named TEAD1 (z -40.19); ChIP tier here 3, anywhere 2
- F5 Ets, 4 models: named ERF (z 14.54); ChIP tier here 3, anywhere 2
- F6 Nuclear receptor, 29 models: named NR4A1 (z -11.81); ChIP tier here 3, anywhere 2
- F7 IRF, 1 model: named IRF2 (z -11.55); ChIP tier here 3, anywhere 2
- F8 GATA, 6 models: named GATA2 (z 7.89); ChIP tier here 3, anywhere 2
- F9 bHLH, 1 model: named MAX (z -6.99); ChIP tier here 3, anywhere 2
- F10 bZIP, 6 models: named MAFK (z -6.9); ChIP tier here 3, anywhere 2
- F11 C2H2 ZF, 6 models: named KLF2 (z 5.4); ChIP tier here 3, anywhere 2
- F12 bZIP, 3 models: named JUNB (z 4.9); ChIP tier here 3, anywhere 2

## Next experiment

In a relevant cranial neural crest or early facial-development model, test the A and G alleles with an allele-specific reporter or endogenous base-editing assay, measuring IRF6 and other candidate-gene expression; pair this with TF occupancy or perturbation assays for the leading TF candidates.

## Flags

- none
