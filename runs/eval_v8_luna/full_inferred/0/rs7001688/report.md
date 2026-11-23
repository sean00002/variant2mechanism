# rs7001688 and LDL cholesterol (v8, full, masked, seed 0)

Context: none (none: eQTL tissue: no GTEx eQTL; active element: no active core biosample maps to an expression context).

**Verdict: no mechanism.** no chain meets the minimum; the top chain (REL) fails: ChIP-seq.

- TF mechanism: no mechanism (no chain meets the minimum; the top chain (REL) fails: ChIP-seq)
- Target gene: FAM110B (indirect: FAM110B is the nearest gene or overlaps the variant)
- Disease link: no association (common variant (MAF 0.4595): neither the GWAS Catalog nor Open Targets lists an association with LDL cholesterol)

Cost $0.010 over 6 model calls; 122 s.

## Chains

| Rank | Chain | TF | Gene | Binding | Cell type | Element | Gene link | Disease | Status |
|---|---|---|---|---|---|---|---|---|---|
| 1 | H1 (F1) | REL | FAM110B | indirect | untested | indirect | indirect | contradicted | kept |
| 2 | H3 (F3) | ASH1L | FAM110B | indirect | untested | indirect | indirect | contradicted | kept |
| 3 | H4 (F4) | ZNF580 | FAM110B | indirect | untested | indirect | indirect | contradicted | kept |
| 4 | H5 (F5) | NME2 | FAM110B | indirect | untested | indirect | indirect | contradicted | kept |
| - | H2 (F2) | CASZ1 | FAM110B | indirect | untested | contradicted | indirect | contradicted | eliminated: element: the variant is not in a cCRE and no TF is bound there in the context |

## Family screen

- F1 Rel, 1 model: named REL (z 33.95); ChIP tier here 3, anywhere 3
- F2 C2H2 ZF, 1 model: named CASZ1 (z 32.75); ChIP tier here 3, anywhere 3
- F3 AT hook, 2 models: named ASH1L (z 29.74); ChIP tier here 3, anywhere 3
- F4 C2H2 ZF, 1 model: named ZNF580 (z -29.06); ChIP tier here 3, anywhere 3
- F5 Unknown, 1 model: named NME2 (z 28.95); ChIP tier here 3, anywhere 3
- F6 C2H2 ZF, 1 model: named ZNF230 (z 26.94); ChIP tier here 3, anywhere 3
- F7 E2F, 4 models: named E2F1 (z 25.88); ChIP tier here 3, anywhere 3
- F8 C2H2 ZF, 1 model: named ZNF384 (z -24.76); ChIP tier here 3, anywhere 3
- F9 BED ZF, 1 model: named SCAND3 (z 24.73); ChIP tier here 3, anywhere 3
- F10 TEA, 4 models: named TEAD1 (z 23.14); ChIP tier here 3, anywhere 3
- F11 Unknown, 1 model: named SNAPC5 (z 22.9); ChIP tier here 3, anywhere 3
- F12 Unknown, 1 model: named PURB (z -21.63); ChIP tier here 3, anywhere 3

## Next experiment

No chain is currently supported as causal. Test the allele-specific binding predictions in vitro, then assess variant function with an allele-specific reporter or endogenous variant perturbation in a relevant hepatocyte model, measuring candidate regulatory effects and gene expression before assigning a target gene or LDL mechanism.

## Flags

- none
