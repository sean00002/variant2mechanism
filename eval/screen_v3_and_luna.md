# Screen v3 (the site-strength rule) and GPT-6 Luna

What is compared, how it is scored, and the results. Seed 0, all 15 cases, named mode except where section 7 adds
masked runs. Counts, not percentages. Tables made with `scripts/compare_screens.py` (sections 3 to 5) and
`scripts/qbic_value.py` (section 7); the earlier comparison is `eval/screen_v1_vs_v2.md`. Every run here has one
refinement round; the multi-round loop that followed is in `eval/multi_round_loop.md`.

## 1. What is compared

Every number comes from **runs**. A run is one case (a variant and its disease) under one configuration, one model
and one screen version. It returns a ranked list of **mechanism chains**. Each chain names a TF, the allele that binds
it more, the regulatory element, the target gene, the cell type and the phenotype, and carries a probability. One
chain is always the **null**: "no TF-mediated effect of this variant". The probabilities sum to 1, and the rank is the
order of probability.

Three comparisons are made:

1. **Screen versions, on DeepSeek V4.1 Flash, `full` only.** Same model and cases; what changes is what the QBiC-SELEX
   screen shows the model.
   - **v1** (spec 1): the models passing the Bonferroni gate, grouped by CIS-BP family, kept if a TF in the group is
     expressed, ranked by |z|. No occupancy.
   - **v2** (spec 3): occupancy first. TFs with an ENCODE ChIP-seq peak over the variant: bound in the matching cell
     type ("here") before other cell types ("elsewhere"), then by |z|. Then expressed TFs that ENCODE never assayed
     and whose best model passes the gate. Spec 3 also changed the prompts (the occupancy principle, the critic's
     binding rubric), the output schema and the evidence gathered, so **v1 against v2 compares that whole bundle**.
   - **v3**: v2 plus the site-strength rule (section 2). Nothing else changed, so **v2 against v3 isolates the rule**.
2. **Models, on screen v3, all configurations.** DeepSeek V4.1 Flash against GPT-6 Luna (`openai/gpt-6-luna`). Each
   model plays all three roles (generator, critic, literature summariser). Cases, prompts, tools and screen are the
   same. DeepSeek's `single` and `no_qbic` runs are its v2 runs: the screen enters only `full`, so their requests
   are identical.
3. **What QBiC-SELEX adds: `full` against `no_qbic`,** paired by case, for every run set in named mode, and for
   DeepSeek and Luna on screen v3 in masked mode (section 7).

### The three configurations: an ablation

| Configuration | What the model gets | What it measures |
|---|---|---|
| `single` | One call with the variant, alleles, disease and expression context. No tools, no evidence, no critic. | Memory alone |
| `no_qbic` | The evidence pipeline. Gathered context (variant annotation, nearest genes, ENCODE cCRE, ENCODE ChIP-seq occupancy, GWAS, fine-mapping, eQTLs for germline variants, literature with checked quotes), then chains, then a critic grades every link, then up to 3 tool calls the agent chooses, then revised chains and a regrade. | Evidence without QBiC-SELEX |
| `full` | `no_qbic` plus the QBiC-SELEX screen (a summary row and one row per listed TF) and a tool to ask QBiC-SELEX about any named TF. | What QBiC-SELEX adds |

**Named mode:** the model sees the rsID and the disease, so it can recall a published mechanism. `single` is
therefore a memory baseline, and a high score there says the answer is well known, not that the model reasoned to it.
Sections 2 to 6 use named runs only.

**Masked mode** (section 7 only): the variant's name is left out of the case header, and every rsID in the evidence
reaches the model as "rs[masked]", so it cannot look a published answer up by name. The position, alleles, disease,
expression context and the evidence about the locus (nearest genes, GWAS associations, literature on the region)
stay, so a famous locus can still be recognised; the TERT promoter is the clearest case.

### The cases

| Case | Class | Gold TF (allele binding more) | Expression context: matching ENCODE biosample |
|---|---|---|---|
| tert_c228t | TF case (cancer) | GABPA (alt) | DepMap glioblastoma lines (median of 54): none |
| tert_c250t | TF case (cancer) | GABPA (alt) | DepMap glioblastoma lines (median of 54): none |
| rs6983267 | TF case (cancer) | TCF7L2 (ref) | DepMap ACH-000971 (HCT 116): HCT116 |
| rs4784227 | TF case (cancer) | FOXA1 (alt) | DepMap ACH-000019 (MCF7): MCF-7 |
| rs339331 | TF case (cancer) | HOXB13 (ref) | DepMap ACH-000977 (LNCaP clone FGC): LNCaP |
| rs2168101 | TF case (cancer) | GATA3 (ref) | DepMap ACH-000149 (SK-N-SH): SK-N-SH |
| rs12740374 | TF case (other) | CEBPA (alt) | DepMap ACH-000625 (Hep 3B2.1-7): HepG2, a proxy |
| rs1421085 | TF case (other) | ARID5B (ref) | GTEx subcutaneous adipose (a proxy for preadipocytes): none |
| rs642961 | TF case (other) | TFAP2A (alt) | none (embryonic craniofacial tissue): none |
| rs13078086 | random control | none | DepMap ACH-000971: HCT116 |
| rs11629191 | random control | none | DepMap ACH-000019: MCF-7 |
| rs7001688 | random control | none | DepMap ACH-000625: HepG2 |
| rs73706717 | near-miss control (rs6983267's element) | none | DepMap ACH-000971: HCT116 |
| rs34768248 | near-miss control (the TERT promoter) | none | DepMap glioblastoma lines: none |
| rs56007086 | near-miss control (rs4784227's element) | none | DepMap ACH-000019: MCF-7 |

- **TF cases (9):** a published causal TF (the gold TF) and the allele it binds more.
- **Random controls (3):** common variants with no known TF mechanism. The right answer is the null.
- **Near-miss controls (3):** variants in the same element as a famous causal SNP, with no known effect of their own.
  They share that element's ChIP-seq peaks, so occupancy cannot tell them apart from the causal SNP: these are the
  hard controls.

### The metrics

| Metric | Definition |
|---|---|
| Gold TF ranked first | The rank-1 chain names the gold TF. The name must resolve to that one HGNC symbol; a family member does not count. |
| Gold TF in top 3 | A chain naming the gold TF is ranked 1 to 3. |
| Direction right | Of the runs that rank the gold TF at all, its chain names the right allele as binding more (`eval/direction_labels.csv`). |
| TF cases: null ranked first | The null is ranked first on a variant with a known mechanism: under-claiming. |
| Gold TF first in the screen | The gold TF heads the screen's occupied list. A property of the code, not of the model. |
| Controls: null ranked first | The null is ranked first, which is the right answer. |
| Controls: over-claiming | The probability left on TF chains, 1 − p(null). 0 is the ideal. |
| Answer in the evidence | A literature title or quote shown to the model names the gold TF: the evidence handed it the answer. |
| Agent asked a tool about the gold TF | One of its 3 chosen tool calls names the gold TF, a sign it already suspected it. |

**How big a difference has to be:** one seed per run, 9 TF cases, 3 + 3 controls. Two DeepSeek runs of the same grid
agreed on only 74% of the gold-TF-first verdicts, so a difference of one or two cases is within run-to-run noise. A
change counts as an effect here only when it follows a change in what the model was shown.

## 2. The site-strength rule (screen v3)

The rule (26 Oct 2026), in code only:

- Every occupied, expressed TF gets the site strength of its best model: the better allele's best k-mer over the
  variant, as a percentile of the model's 16,384 7-mer coefficients (994 of the 997 models are 7-mer models; 3 are
  6-mer models).
- A **strong site** reaches the 97.5th percentile. Using the better allele means creating a site (FOXA1 at rs4784227,
  GABPA at the TERT promoter) counts the same as breaking one (TCF7L2 at rs6983267).
- Within each occupancy class (bound here, then bound elsewhere), strong sites come first, then |z|.
- A weak-site TF stays listed. Its line says the change is between weak k-mers, and that the ChIP peak more likely
  reflects another site in the element. "QBiC-SELEX detects a change" needs both the gate and a strong site.
- The summary line explains the rule, and says when no occupied TF has a strong site.

Why 97.5: the score is the best of 14 overlapping 7-mers, so it runs high by chance. Over 60 randomly chosen models
with 150 random 21-bp sequences each, 42% of SNVs reach the 95th percentile, 24% the 97.5th and 15% the 98.5th. At
the 95th, nearly every listed TF counted as strong and the rule changed nothing. At the 98.5th, the causal TCF7L2 and
FOXA1 sites (both at 98.8) would pass by only 0.3.

**The cut-off was chosen after seeing the three near-miss pairs, so this rerun does not test it independently.**

What the rule did to the screens (the first four rows of the occupied list; S strong, w weak, "here" bound in the
matching cell type, gold TF in bold):

| Case | Screen v2 | Screen v3 |
|---|---|---|
| tert_c228t | **GABPA**, ZIC2, CTCF, ZBTB7A | **GABPA** S, ZIC2 S, CTCF S, ZBTB7A S |
| tert_c250t | **GABPA**, KLF12, NR2C1, TGIF2 | **GABPA** S, KLF12 S, NR2C1 S, TGIF2 S |
| rs6983267 | SRF here, SP1 here, **TCF7L2** here, JUND here | **TCF7L2** S here, SRF w here, SP1 w here, JUND w here |
| rs4784227 | GATA3 here, **FOXA1** here, NR2F2 here, TCF7L2 here | GATA3 S here, **FOXA1** S here, NR2F2 S here, TCF7L2 S here |
| rs339331 | PKNOX1 | PKNOX1 w |
| rs2168101 | GATA2 here, **GATA3** here, ZNF8 here, FOXJ3 here | GATA2 S here, **GATA3** S here, ZNF8 S here, FOXJ3 S here |
| rs12740374 | CEBPG here, **CEBPA** here, MLX here, GFI1 here | CEBPG S here, **CEBPA** S here, MLX S here, GFI1 S here |
| rs1421085 | ATF3, TEAD1, JUN, FOXP1 | ATF3 S, TEAD1 S, JUN S, FOXP1 S |
| rs642961 | ZNF687 | ZNF687 w |
| rs13078086 | none | none |
| rs11629191 | none | none |
| rs7001688 | CTCF | CTCF w |
| rs73706717 | TCF7L2 here, SP1 here, NFIC, NFIA | TCF7L2 w here, SP1 w here, NFIC S, NFIA S |
| rs34768248 | NKRF, NR2C2, ZNF800, CREB1 | NKRF S, CREB1 S, MAX S, ZBTB33 S |
| rs56007086 | TCF7L2 here, NR2F2 here, GATA3 here, SPDEF here | TCF7L2 S here, SPDEF S here, NR2F2 w here, GATA3 w here |

Only one gold TF moved: TCF7L2 at rs6983267, from third to first. HOXB13 and TFAP2A are in no occupied list (ENCODE
assayed HOXB13 only in other cell types, with no peak here, and never assayed TFAP2A), and ARID5B has no QBiC-SELEX
model, so no screen can list it. At the near-miss controls the parent
TF is labelled weak at rs73706717 (TCF7L2) and rs56007086 (FOXA1, fifth, not shown). But TCF7L2 still heads the list
at rs73706717, because "bound here" comes before site strength.

## 3. Results: screen versions, `full`

| | DeepSeek v1 | DeepSeek v2 | DeepSeek v3 | Luna v3 |
|---|---|---|---|---|
| Gold TF ranked first | 3 of 9 | 4 of 9 | 6 of 8 | 3 of 9 |
| Gold TF in top 3 | 7 of 9 | 9 of 9 | 7 of 8 | 7 of 9 |
| Direction right (when the gold TF is ranked) | 6 of 7 | 9 of 9 | 7 of 7 | 7 of 7 |
| TF cases: null ranked first (under-claiming) | 2 of 9 | 2 of 9 | 0 of 8 | 4 of 9 |
| Gold TF first in the screen's occupied list | n/a | 2 of 9 | 3 of 8 | 3 of 9 |
| Random controls: null ranked first | 3 of 3 | 2 of 2 | 3 of 3 | 3 of 3 |
| Random controls: over-claiming (mean) | 0.31 | 0.15 | 0.27 | 0.06 |
| Near-miss controls: null ranked first | 3 of 3 | 3 of 3 | 2 of 3 | 3 of 3 |
| Near-miss controls: over-claiming (mean) | 0.47 | 0.58 | 0.56 | 0.30 |
| Answer in the evidence (retrieval audit) | 3 of 9 | 7 of 9 | 6 of 8 | 5 of 9 |
| Agent asked a tool about the gold TF | 7 of 9 | 8 of 9 | 7 of 8 | 5 of 9 |
| Runs scored | 15 | 14 | 14 | 15 |
| Cost, total | $0.35 | $0.44 | $0.45 | $0.19 |

Missing runs: DeepSeek v2 lost rs13078086 and DeepSeek v3 lost rs2168101. In both, the critic left links ungraded
twice at regrade. A rerun would replay the cached answers, so they stay missing.

## 4. Results: DeepSeek against Luna, screen v3

| | DeepSeek single | Luna single | DeepSeek no_qbic | Luna no_qbic | DeepSeek full | Luna full |
|---|---|---|---|---|---|---|
| Gold TF ranked first | 6 of 9 | 9 of 9 | 5 of 9 | 3 of 9 | 6 of 8 | 3 of 9 |
| Gold TF in top 3 | 9 of 9 | 9 of 9 | 7 of 9 | 8 of 9 | 7 of 8 | 7 of 9 |
| Direction right (when the gold TF is ranked) | 7 of 9 | 8 of 9 | 7 of 7 | 6 of 8 | 7 of 7 | 7 of 7 |
| TF cases: null ranked first (under-claiming) | 2 of 9 | 0 of 9 | 4 of 9 | 5 of 9 | 0 of 8 | 4 of 9 |
| Random controls: null ranked first | 3 of 3 | 3 of 3 | 3 of 3 | 3 of 3 | 3 of 3 | 3 of 3 |
| Random controls: over-claiming (mean) | 0.55 | 0.40 | 0.07 | 0.02 | 0.27 | 0.06 |
| Near-miss controls: null ranked first | 0 of 3 | 3 of 3 | 3 of 3 | 3 of 3 | 2 of 3 | 3 of 3 |
| Near-miss controls: over-claiming (mean) | 0.70 | 0.34 | 0.37 | 0.25 | 0.56 | 0.30 |
| Answer in the evidence (retrieval audit) | 0 of 9 | 0 of 9 | 6 of 9 | 8 of 9 | 6 of 8 | 5 of 9 |
| Agent asked a tool about the gold TF | 0 of 9 | 0 of 9 | 7 of 9 | 9 of 9 | 7 of 8 | 5 of 9 |
| Runs scored | 15 | 15 | 15 | 15 | 14 | 15 |
| Cost, total | $0.06 | $0.03 | $0.44 | $0.18 | $0.45 | $0.19 |

## 5. Per-case answers

The top three chains of each run: TF, the allele said to bind more, and probability. The gold TF is in bold; the
null's probability is in brackets when the null is not in the top three.

### `full`

| Case | DeepSeek v2 | DeepSeek v3 | Luna v3 |
|---|---|---|---|
| tert_c228t | **GABPA** alt 0.72; null 0.20; ETV3 alt 0.08 | **GABPA** alt 0.57; null 0.22; CTCF ref 0.09 | null 0.60; **GABPA** alt 0.22; CTCF ref 0.10 |
| tert_c250t | **GABPA** alt 0.56; null 0.31; KLF12 ref 0.06 | **GABPA** alt 0.45; null 0.40; ETV3 alt 0.08 | null 0.58; **GABPA** alt 0.20; TGIF2 ref 0.12 |
| rs6983267 | null 0.40; **TCF7L2** ref 0.30; SRF ref 0.22 | **TCF7L2** ref 0.45; null 0.43; NR2F2 alt 0.07 | **TCF7L2** ref 0.45; null 0.36; SRF ref 0.12 |
| rs4784227 | GATA3 alt 0.37; **FOXA1** alt 0.33; null 0.30 | GATA3 alt 0.32; null 0.30; **FOXA1** alt 0.28 | GATA3 alt 0.38; **FOXA1** alt 0.27; null 0.27 |
| rs339331 | null 0.40; AR ref 0.28; **HOXB13** ref 0.22 | **HOXB13** ref 0.38; null 0.32; AR ref 0.22 | **HOXB13** ref 0.75; null 0.12; AR ref 0.08 |
| rs2168101 | GATA2 ref 0.58; null 0.25; **GATA3** ref 0.12 | failed | GATA2 ref 0.50; **GATA3** ref 0.28; null 0.22 |
| rs12740374 | CEBPG alt 0.35; null 0.32; **CEBPA** alt 0.25 | **CEBPA** alt 0.40; CEBPB alt 0.18; CEBPG alt 0.15 (null 0.15) | **CEBPA** alt 0.38; null 0.30; CEBPG alt 0.25 |
| rs1421085 | **ARID5B** ref 0.42; null 0.30; ATF3 alt 0.16 | **ARID5B** ref 0.40; null 0.35; ATF3 alt 0.15 | null 0.78; ATF3 alt 0.08; TEAD1 alt 0.08 |
| rs642961 | **TFAP2A** alt 0.60; ETV3 alt 0.25; null 0.15 | ETV3 alt 0.35; ETV2 alt 0.30; ETV3L alt 0.20 (null 0.15) | null 0.90; ETV2 alt 0.06; ETV3 alt 0.04 |
| rs13078086 | failed | null 0.72; TFAP2E ref 0.16; EBF4 ref 0.09 | null 0.95; TFAP2E ref 0.03; EBF4 ref 0.01 |
| rs11629191 | null 0.87; CREB3L4 ref 0.08; CREB3L2 ref 0.03 | null 0.60; CREB3L2 ref 0.24; CREB3L4 ref 0.16 | null 0.95; CREB3L4 ref 0.02; TGIF1 ref 0.01 |
| rs7001688 | null 0.82; NME2 alt 0.08; CASZ1 alt 0.06 | null 0.88; NME2 alt 0.07; CASZ1 alt 0.03 | null 0.93; NME2 alt 0.03; CASZ1 alt 0.03 |
| rs73706717 | null 0.45; TCF7L2 ref 0.30; SP1 ref 0.17 | null 0.36; TCF7L2 ref 0.26; SP1 ref 0.18 | null 0.62; TCF7L2 ref 0.18; NFIC alt 0.12 |
| rs34768248 | null 0.38; NKRF ref 0.30; CREB1 alt 0.18 | null 0.53; NKRF ref 0.26; CREB1 alt 0.14 | null 0.75; NKRF ref 0.15; CREB1 alt 0.10 |
| rs56007086 | null 0.43; SPDEF ref 0.40; TCF7L2 alt 0.17 | SPDEF ref 0.46; null 0.42; FOXA1 alt 0.07 | null 0.72; SPDEF ref 0.20; TCF7L2 alt 0.08 |

### `single` and `no_qbic`

| Case | DeepSeek single | Luna single | DeepSeek no_qbic | Luna no_qbic |
|---|---|---|---|---|
| tert_c228t | **GABPA** alt 0.50; null 0.25; ETS1 alt 0.15 | **GABPA** alt 0.68; null 0.20; ETS1 alt 0.12 | **GABPA** alt 0.50; null 0.35; JUN alt 0.10 | null 0.55; **GABPA** alt 0.40; MAX alt 0.05 |
| tert_c250t | **GABPA** alt 0.55; null 0.22; ETS1 alt 0.15 | **GABPA** alt 0.65; null 0.23; ETS1 alt 0.12 | null 0.45; **GABPA** alt 0.42; ETS1 alt 0.08 | null 0.60; **GABPA** alt 0.30; MAX alt 0.06 |
| rs6983267 | **TCF7L2** ref 0.55; **TCF7L2** ref 0.25; null 0.20 | **TCF7L2** ref 0.70; **TCF7L2** ref 0.17; null 0.13 | **TCF7L2** ref 0.36; null 0.35; SP1 alt 0.17 | null 0.62; **TCF7L2** ref 0.22; **TCF7L2** ref 0.10 |
| rs4784227 | **FOXA1** alt 0.35; **FOXA1** ref 0.30; null 0.25 | **FOXA1** alt 0.50; null 0.25; **FOXA1** alt 0.18 | **FOXA1** alt 0.45; null 0.40; GATA3 alt 0.15 | null 0.75; **FOXA1** ref 0.15; GATA3 alt 0.07 |
| rs339331 | null 0.40; **HOXB13** ref 0.35; **HOXB13** alt 0.15 | **HOXB13** ref 0.54; null 0.35; FOXA1 alt 0.11 | null 0.40; GATA2 alt 0.33; AR ref 0.27 | **HOXB13** ref 0.42; AR ref 0.33; null 0.25 |
| rs2168101 | GATA2 alt 0.42; null 0.35; **GATA3** alt 0.13 | **GATA3** alt 0.65; null 0.22; **GATA3** alt 0.08 | **GATA3** ref 0.58; null 0.28; GATA2 ref 0.14 | GATA2 ref 0.38; **GATA3** ref 0.33; null 0.29 |
| rs12740374 | **CEBPA** alt 0.55; null 0.20; CEBPB alt 0.15 | **CEBPA** alt 0.70; CEBPB alt 0.13; null 0.10 | **CEBPA** alt 0.62; null 0.24; **CEBPA** alt 0.08 | **CEBPA** alt 0.48; null 0.30; FOXA1 alt 0.13 |
| rs1421085 | null 0.55; **ARID5B** ref 0.25; **ARID5B** ref 0.12 | **ARID5B** ref 0.55; **ARID5B** ref 0.18; null 0.15 | null 0.55; **ARID5B** ref 0.25; JUN alt 0.20 | null 0.90; JUN ref 0.05; KLF6 ref 0.05 |
| rs642961 | **TFAP2A** ref 0.55; null 0.20; TFAP2C alt 0.15 | **TFAP2A** alt 0.68; null 0.24; **TFAP2A** alt 0.08 | null 0.44; ZNF687 ref 0.38; MYC ref 0.19 | **TFAP2A** ref 0.78; null 0.16; **TFAP2A** ref 0.03 |
| rs13078086 | null 0.38; CDX2 ref 0.24; TCF7L2 alt 0.15 | null 0.64; TCF7L2 alt 0.14; HNF4A ref 0.12 | null 0.94; CTCF ref 0.03; NFKB1 alt 0.02 | null 0.99; CTCF alt 0.00; CTCF ref 0.00 |
| rs11629191 | null 0.52; FOXA1 alt 0.25; CTCF ref 0.14 | null 0.55; ESR1 alt 0.20; FOXA1 ref 0.15 | null 0.95; FOXA1 alt 0.03; ESR1 ref 0.02 | null 0.99; ESR1 alt 0.00; FOXA1 ref 0.00 |
| rs7001688 | null 0.45; HNF4A ref 0.30; SREBF2 alt 0.15 | null 0.60; HNF4A alt 0.20; FOXA2 ref 0.12 | null 0.89; CTCF ref 0.07; CTCF alt 0.04 | null 0.96; CTCF alt 0.02; CTCF ref 0.02 |
| rs73706717 | TCF7L2 alt 0.50; null 0.30; TCF7L2 ref 0.10 | null 0.70; TCF7L2 alt 0.14; HNF4A ref 0.09 | null 0.46; TCF7L2 alt 0.31; SP1 alt 0.14 | null 0.84; TCF7L2 alt 0.08; SP1 ref 0.05 |
| rs34768248 | GATA2 alt 0.35; null 0.35; GABPA alt 0.20 | null 0.68; GABPA alt 0.16; SP1 ref 0.09 | null 0.86; CTCF ref 0.08; JUN alt 0.06 | null 0.90; JUN alt 0.04; CTCF alt 0.03 |
| rs56007086 | FOXA1 alt 0.40; null 0.25; GATA3 ref 0.15 | null 0.60; FOXA1 alt 0.20; GATA3 ref 0.12 | null 0.58; FOXA1 ref 0.24; GATA3 ref 0.18 | null 0.50; FOXA1 ref 0.22; GATA3 ref 0.20 |

## 6. What the results show

1. **The rule did its job in one case.** At rs6983267, TCF7L2 has the only strong site among the TFs bound in
   HCT116. It moved from third to first in the screen, and DeepSeek's answer moved with it: null 0.40 and TCF7L2
   0.30 became TCF7L2 0.45 and null 0.43, and SRF (now labelled weak) dropped out of the top three. Luna, which saw
   the same screen, also ranked TCF7L2 first.
2. **The rest of DeepSeek's v2-to-v3 change is noise.** In every other case that moved, the gold TF's place in the
   screen stayed the same: rs339331 and rs12740374 rose to first, rs642961 fell from first to absent, rs4784227 from
   second to third. Most margins are small: at rs4784227, GATA3, FOXA1 and the null sit within about 0.1 of each
   other in all three `full` runs.
3. **The near-miss controls did not improve on DeepSeek** (over-claiming 0.58 to 0.56; null first 3 of 3 to 2 of 3).
   At rs73706717 it still gave TCF7L2 0.26 and SP1 0.18, both labelled weak sites. At rs56007086 it ranked SPDEF (a
   strong site) above the null, 0.46 to 0.42. Weak-site TFs among its near-miss proposals: 5 of 10 (v2, read with the
   same cut-off: 3 of 8).
4. **The rule cannot touch the random controls,** which have at most one occupied TF each. DeepSeek's over-claiming
   there rose from 0.15 to 0.27 on screens that differ by one added sentence (rs11629191: null 0.87 in v2, 0.60 in
   v3): run-to-run noise.
5. **Luna is far more cautious at the controls.** In `full` its null probability is 0.93 to 0.95 at the random
   controls and 0.62 to 0.75 at the near-miss controls; it ranks the null first at all six. Weak-site TFs among its
   near-miss proposals: 2 of 7 (TCF7L2 and SP1 at rs73706717).
6. **Luna pays for that on the true cases.** With tools, it ranks the null first in 4 of 9 TF cases in `full` and 5
   of 9 in `no_qbic`. In `full` these are exactly the four TF cases with no matching ENCODE biosample: both TERT
   promoter mutations (null 0.60 and 0.58), rs1421085 (0.78) and rs642961 (0.90). With a matching biosample (5 cases)
   it never does. Its critic applies the binding rubric strictly. At C228T, GABPA's peaks "overlap the variant only in
   other biosamples; glioblastoma occupancy is not shown", and GABPA's best model there is a mapped ETV5 model. In
   `no_qbic` there is no QBiC-SELEX change at all, so binding can be weak at best.
7. **From memory alone, Luna names every gold TF.** In `single` it ranks the gold TF first in 9 of 9, each at 0.50 to
   0.70 (DeepSeek: 6 of 9). With evidence in front of it, Luna then argues itself down: at the TERT promoter, GABPA
   falls from 0.68 in `single` to 0.22 in `full`.
8. **Both models agree on three cases.** rs6983267, rs12740374 and rs339331 have the gold TF first in both `full`
   columns, all three with a matching ENCODE biosample. Luna is the more confident there (HOXB13 0.75 against
   DeepSeek's 0.38).
9. **Cost and reliability:** Luna's 45 runs cost $0.40, against $0.95 for DeepSeek's grid, and all 45 finished.
   Across the grid it had no rejected quotes (DeepSeek: 15) and cited no evidence ID that does not exist. Its 5 tool
   failures are Open Targets lookups given a string with several diseases in it ("LDL cholesterol, myocardial
   infarction").

## 7. Does QBiC-SELEX help?

**The comparison is `full` against `no_qbic`.** The model, cases, prompts, evidence, critic and tool budget are the
same; `full` adds only the QBiC-SELEX screen and the tool to ask QBiC-SELEX about a TF. Each case is compared with
itself. (`single` against `full` adds the whole evidence pipeline as well, so it cannot isolate QBiC-SELEX.)

Two things look like tests of QBiC-SELEX but are not:

- **Its own significance test.** At every variant, 209 to 569 of the 997 models pass the Bonferroni gate, the random
  controls included (209, 445 and 441). The models are precise, so modest changes clear the gate: passing it says the
  variant changes binding, not that the change matters.
- **The agent's p(null) on its own.** A screen that makes the agent name a TF more readily lowers p(null) at the TF
  cases, which looks like a gain, and at the controls, which is a loss. Here the two are read together, and as one
  number: the separation, the chance that a control's p(null) is above a TF case's (AUC; 1 is perfect, 0.5 chance).

### 7.1 The tool, with no model

How the gold TF ranks on QBiC-SELEX's predictions alone (each TF's best |z| over its own and mapped models; no
occupancy, no expression), and among the TFs with an ENCODE peak over the variant: in the screen v3 order, by |z|
alone, and by expression alone. These numbers are fixed, so there is no seed noise.

| Case | Gold TF | QBiC-SELEX alone: rank among all TFs | ENCODE class | TFs in that class | Screen v3 rank | Rank by \|z\| alone | Rank by expression alone |
|---|---|---|---|---|---|---|---|
| tert_c228t | GABPA | 1 of 1109 (\|z\| 166.2) | bound elsewhere | 20 | 1 | 1 | 10 |
| tert_c250t | GABPA | 1 of 1109 (\|z\| 167.5) | bound elsewhere | 18 | 1 | 1 | 9 |
| rs6983267 | TCF7L2 | 632 of 1109 (\|z\| 4.7) | bound here | 7 | 1 | 3 | 2 |
| rs4784227 | FOXA1 | 160 of 1109 (\|z\| 15.4) | bound here | 5 | 2 | 2 | 2 |
| rs339331 | HOXB13 | 1 of 1109 (\|z\| 103.5) | unbound, assayed elsewhere: not listed | | | | |
| rs2168101 | GATA3 | 7 of 1109 (\|z\| 56.1) | bound here | 10 | 2 | 1 | 3 |
| rs12740374 | CEBPA | 18 of 1109 (\|z\| 22.8) | bound here | 104 | 2 | 2 | 1 |
| rs1421085 | ARID5B | no QBiC-SELEX model | | | | | |
| rs642961 | TFAP2A | 33 of 1109 (\|z\| 24.0) | not assayed: not listed | | | | |

- **QBiC-SELEX alone** puts the gold TF first of 1,109 TFs at both TERT mutations and at rs339331, and in the top 33
  at 6 of the 8 cases it covers. Its weak cases are FOXA1 at rs4784227 (160th) and TCF7L2 at rs6983267 (632nd; |z|
  4.7, just over the gate of 4.05).
- **Among the TFs with an ENCODE peak over the variant,** the screen puts the gold TF first or second in all 6 cases
  it can list. A random order would rank them this well with probability 0.004 (Fisher's method over the six cases).
  Ranking by |z| alone, which leaves out the site rule chosen after seeing the data: 0.006. Ranking by expression
  instead: 0.09.
- **Occupancy first costs one case.** HOXB13 is QBiC-SELEX's top TF at rs339331, but ENCODE assayed HOXB13 only in
  cell types where it has no peak there, so screens v2 and v3 drop it. TFAP2A (33rd at rs642961, through the TFAP2B
  model) is cut by the 5-row limit on TFs ENCODE never assayed. ARID5B has no model.

The famous TF at each near-miss control and at its causal neighbour:

| Near-miss control | TF | Variant | ENCODE class | Best \|z\| (model) | Rank among all TFs | Better allele's site | Strong site |
|---|---|---|---|---|---|---|---|
| rs73706717 | TCF7L2 | rs6983267 | bound here | 4.7 (LEF1_FL_TAGTCG40NAGA_KZ_yin2017_0_3_7mer) | 632 of 1109 | 98.8th | yes |
| rs73706717 | TCF7L2 | rs73706717 | bound here | 8.8 (TCF7_eDBD_TCGGAC40NCCA_KS_yin2017_0_3_7mer) | 263 of 1109 | 90.0th | no |
| rs34768248 | GABPA | tert_c228t | bound elsewhere | 166.2 (ETV5_NA_TGCACT20NGA_ESAF_yang2017_1_3_6mer) | 1 of 1109 | 99.3th | yes |
| rs34768248 | GABPA | rs34768248 | unbound, assayed elsewhere | 14.1 (ETV5_NA_TGCACT20NGA_ESAF_yang2017_1_3_6mer) | 86 of 1109 | 94.8th | no |
| rs56007086 | FOXA1 | rs4784227 | bound here | 15.4 (FOXA2_eDBD_TTGCGA40NGTA_KT_yin2017_1_2_7mer) | 160 of 1109 | 98.8th | yes |
| rs56007086 | FOXA1 | rs56007086 | bound here | 6.3 (FOXA2_eDBD_TTGCGA40NGTA_KT_yin2017_1_2_7mer) | 692 of 1109 | 90.2th | no |

- The TCF7L2 and FOXA1 pairs share the TF's ChIP-seq peak, so occupancy cannot tell the two variants apart. GABPA has
  a peak over C228T but none over rs34768248.
- QBiC-SELEX separates the FOXA1 pair (|z| 15.4 against 6.3; the better allele's site at the 98.8th percentile
  against the 90.2th) and the GABPA pair (|z| 166 against 14).
- The TCF7L2 pair goes the wrong way on |z| (4.7 at the causal SNP, 8.8 at the near-miss). Only the site rule
  separates it (98.8th against 90.0th), and its cut-off was set after seeing these pairs.

### 7.2 The agent, named mode

Each cell is `no_qbic` → `full` over the cases both ran. DeepSeek v3's `no_qbic` runs are its v2 runs.

| `no_qbic` → `full`, named | Claude v1 | DeepSeek v1 | DeepSeek v2 | DeepSeek v3 | Luna v3 |
|---|---|---|---|---|---|
| TF cases compared | 9 | 9 | 9 | 8 | 9 |
| Gold TF ranked first | 7 → 7 | 5 → 3 | 5 → 4 | 4 → 6 | 3 → 3 |
| Gold TF in the top three | 9 → 9 | 7 → 7 | 7 → 9 | 6 → 7 | 8 → 7 |
| Gold TF is the top TF, null ignored | 8 → 8 | 6 → 4 | 7 → 5 | 6 → 6 | 7 → 5 |
| Top TF in the gold TF's motif family, null ignored | 8 → 8 | 7 → 5 | 7 → 6 | 6 → 6 | 8 → 6 |
| TF cases: null ranked first | 1 → 1 | 2 → 2 | 4 → 2 | 4 → 0 | 5 → 4 |
| TF cases: mean p(gold TF) | 0.54 → 0.46 | 0.39 → 0.24 | 0.36 → 0.39 | 0.33 → 0.38 | 0.36 → 0.29 |
| Random controls: mean p(null) | 0.73 → 0.67 | 0.87 → 0.69 | 0.92 → 0.84 | 0.93 → 0.73 | 0.98 → 0.94 |
| Near-miss controls: mean p(null) | none | 0.64 → 0.53 | 0.63 → 0.42 | 0.63 → 0.44 | 0.75 → 0.70 |
| Near-miss controls: mean p(the famous neighbour's TF) | none | 0.27 → 0.00 | 0.21 → 0.10 | 0.21 → 0.11 | 0.11 → 0.06 |
| Separation: AUC of p(null), controls against TF cases | 1.00 → 1.00 | 1.00 → 0.95 | 0.98 → 0.96 | 0.98 → 0.94 | 0.88 → 0.89 |
| Controls where p(null) fell / rose with QBiC-SELEX | 2 / 0 of 3 | 6 / 0 of 6 | 5 / 0 of 5 | 6 / 0 of 6 | 5 / 1 of 6 |
| p(null) lowered more at TF cases than at controls: share of pairs (permutation p) | 0.30 (p 0.855) | 0.27 (p 0.933) | 0.41 (p 0.709) | 0.28 (p 0.915) | 0.50 (p 0.511) |

- **The gold TF did not overtake other TFs.** With QBiC-SELEX it was the top TF (null ignored) as often or less
  often in every run set. Where "gold TF ranked first" rose (DeepSeek v3, 4 → 6), the null fell below it (null first
  4 → 0). In named mode the literature already names the gold TF in 6 to 8 of the 9 cases (section 4), and the
  screen adds TFs with the same or a larger change: paralogs (GATA2 at rs2168101, CEBPG at rs12740374) and a
  co-bound TF (GATA3 at rs4784227).
- **Every model claims more at the controls.** p(null) fell at 24 of the 26 paired controls and rose at one. At the
  random controls, every TF proposed in `full` came from the screen's list of expressed TFs that ENCODE never
  assayed and whose best model passes the gate: TFAP2E and EBF4 at rs13078086, CREB3L2 and CREB3L4 at rs11629191,
  NME2 and CASZ1 at rs7001688.
- **So no named run set passes the direct test** (last row, explained in 7.3). Adding QBiC-SELEX never lowered p(null)
  more at the TF cases than at the controls (0.27 to 0.50 of pairs); for Claude and DeepSeek it lowered it more at
  the controls.
- **QBiC-SELEX did lower the famous neighbour's TF at the near-miss controls,** the one thing only it can tell the
  agent there (DeepSeek v1 0.27 → 0.00, v3 0.21 → 0.11; Luna 0.11 → 0.06). But that probability went to other TFs
  on the screen, not to the null.
- **The separation is near its ceiling in named mode** (AUC 0.88 to 1.00 without QBiC-SELEX), so it has little room
  to show a gain; it fell slightly for DeepSeek.

### 7.3 The agent, masked mode

Masked runs on screen v3 for DeepSeek and Luna, `no_qbic` and `full`: 60 runs, all finished. Without the variant's
name, the model has to find the TF in the evidence, which is the job QBiC-SELEX is for.

The last row is the direct test of this section's question: did adding QBiC-SELEX lower p(null) more at the TF cases
than at the controls? It gives the share of (TF case, control) pairs where it did, and a one-sided p-value over all
5,005 ways of labelling 9 of the 15 cases as TF cases. This test was chosen after seeing Luna's masked results.

| `no_qbic` → `full`, masked | DeepSeek v3 | Luna v3 |
|---|---|---|
| TF cases compared | 9 | 9 |
| Gold TF ranked first | 2 → 3 | 0 → 1 |
| Gold TF in the top three | 6 → 5 | 3 → 6 |
| Gold TF is the top TF, null ignored | 5 → 4 | 2 → 3 |
| Top TF in the gold TF's motif family, null ignored | 5 → 5 | 3 → 4 |
| TF cases: null ranked first | 5 → 4 | 9 → 7 |
| TF cases: mean p(gold TF) | 0.30 → 0.26 | 0.04 → 0.17 |
| Random controls: mean p(null) | 0.94 → 0.70 | 0.90 → 0.92 |
| Near-miss controls: mean p(null) | 0.43 → 0.46 | 0.84 → 0.74 |
| Near-miss controls: mean p(the famous neighbour's TF) | 0.26 → 0.11 | 0.08 → 0.04 |
| Separation: AUC of p(null), controls against TF cases | 0.80 → 0.83 | 0.71 → 0.88 |
| Controls where p(null) fell / rose with QBiC-SELEX | 4 / 2 of 6 | 5 / 1 of 6 |
| p(null) lowered more at TF cases than at controls: share of pairs (permutation p) | 0.36 (p 0.813) | 0.93 (p 0.002) |

- **Luna: QBiC-SELEX separates the TF cases from the controls.** Without it, Luna ranks the null first at all 9 TF
  cases, and its mean p(null) there (0.79) is barely below the controls' (0.87): separation 0.71. With it, p(null)
  falls at every TF case, by 0.08 to 0.55 (mean 0.55), while at the controls it moves between -0.12 and +0.14 (mean
  0.83). It fell more at the TF case in 50 of the 54 pairs: p = 0.002, or 0.015 allowing for the 7 run sets tested.
  The gold TF reaches the top three in 6 cases instead of 3, and its mean probability rises from 0.04 to 0.17.
- **Luna's gold TF gains most where the screen lists it among TFs bound in the matching cell line** (p(gold TF), summed
  over its chains): TCF7L2 at rs6983267 (0.16 → 0.46, now first), CEBPA at rs12740374 (0 → 0.27), GATA3 at rs2168101
  (0.05 → 0.27) and FOXA1 at rs4784227 (0.14 → 0.28). It stays cautious: the null is still first in 7 of 9,
  including both TERT mutations (GABPA 0.07 and 0.17), where GABPA is bound only in other cell types.
- **DeepSeek: no gain.** Without the name it still recognises most of the famous loci from the position and the
  evidence: without QBiC-SELEX it already has the gold TF in the top three in 6 of 9. The screen raises p(gold TF)
  at C228T (GABPA 0.45 → 0.62) and rs6983267 (TCF7L2 0.36 → 0.58), but lowers it at C250T (GABPA 0.58 → 0.26) and
  rs2168101 (GATA3 0.40 → 0.08, behind GATA2 at 0.52). It also lowers p(null) at the random controls from 0.94 to
  0.70, again on the TFs ENCODE never assayed. Paired test: 0.36 of pairs (p 0.81).
- **Both models give the famous neighbour's TF less at the near-miss controls** (DeepSeek 0.26 → 0.11, Luna 0.08 →
  0.04), as in named mode. At rs56007086 both then name SPDEF, which has a strong site there (DeepSeek 0.34, above
  the null; Luna 0.28).
- **The three gold TFs the screen cannot list stay missing** in both models: HOXB13 at rs339331 (AR, PKNOX1 or
  HOXC6 instead), TFAP2A at rs642961 (FLI1, ETV2, ETV3) and ARID5B at rs1421085 (JUN, ATF3, TEAD1).
- **Reliability:** all 60 runs finished. DeepSeek had 18 rejected quotes and 3 tool failures; Luna had 2 tool
  failures.

The top three chains of each masked run (gold TF in bold; the null's probability in brackets when it is not in the
top three):

| Case | DeepSeek v3 no_qbic | DeepSeek v3 full | Luna v3 no_qbic | Luna v3 full |
|---|---|---|---|---|
| tert_c228t | null 0.45; **GABPA** alt 0.40; MAX alt 0.10 | **GABPA** alt 0.62; null 0.25; TFAP2A ref 0.08 | null 0.92; MAX alt 0.05; JUN ref 0.03 | null 0.78; CTCF ref 0.11; **GABPA** alt 0.07 |
| tert_c250t | **GABPA** alt 0.58; null 0.34; MAX alt 0.05 | null 0.49; **GABPA** alt 0.26; ZNF143 ref 0.10 | null 0.88; MAX alt 0.06; JUN ref 0.04 | null 0.61; **GABPA** alt 0.17; ZNF143 ref 0.12 |
| rs6983267 | null 0.40; **TCF7L2** ref 0.36; SP1 alt 0.14 | **TCF7L2** ref 0.58; null 0.31; NR2F2 alt 0.08 | null 0.62; **TCF7L2** alt 0.16; SP1 alt 0.14 | **TCF7L2** ref 0.46; null 0.37; SP1 ref 0.09 |
| rs4784227 | GATA3 alt 0.34; **FOXA1** alt 0.30; null 0.28 | GATA3 alt 0.46; **FOXA1** alt 0.28; null 0.21 | null 0.76; **FOXA1** alt 0.14; GATA3 alt 0.10 | GATA3 alt 0.30; **FOXA1** alt 0.28; null 0.27 |
| rs339331 | AR ref 0.47; null 0.41; AR ref 0.12 | null 0.46; AR ref 0.32; HOXC6 ref 0.14 | null 0.83; PKNOX1 alt 0.11; PKNOX1 ref 0.04 | null 0.72; PKNOX1 alt 0.15; HOXC6 ref 0.08 |
| rs2168101 | null 0.50; **GATA3** ref 0.40; GATA2 ref 0.10 | GATA2 ref 0.52; null 0.30; FOXJ3 alt 0.10 | null 0.86; GATA2 alt 0.06; **GATA3** alt 0.05 | null 0.31; GATA2 ref 0.30; **GATA3** ref 0.27 |
| rs12740374 | **CEBPA** alt 0.52; null 0.31; **CEBPA** alt 0.10 | **CEBPA** alt 0.50; null 0.20; CEBPG alt 0.18 | null 0.50; FOXA1 alt 0.20; FOXA1 alt 0.16 | null 0.35; **CEBPA** alt 0.27; KLF6 ref 0.17 |
| rs1421085 | null 0.42; JUN ref 0.27; KLF6 alt 0.23 | null 0.44; ATF3 alt 0.22; TEAD1 alt 0.12 | null 0.86; JUN alt 0.09; USF2 alt 0.05 | null 0.68; JUN alt 0.12; ATF3 alt 0.11 |
| rs642961 | null 0.58; ZNF687 ref 0.30; ZNF687 ref 0.12 | null 0.74; FLI1 alt 0.17; ETV2 alt 0.05 | null 0.90; ZNF687 alt 0.04; ZNF687 alt 0.04 | null 0.82; FLI1 alt 0.13; ETV3 alt 0.03 |
| rs13078086 | null 0.95; CTCF alt 0.03; RELA alt 0.02 | null 0.72; TFAP2E ref 0.12; EBF4 ref 0.08 | null 0.80; CTCF alt 0.10; CTCF ref 0.10 | null 0.94; TFAP2E ref 0.04; EBF4 ref 0.01 |
| rs11629191 | null 0.93; ESR1 alt 0.03; FOXA1 ref 0.03 | null 0.84; CREB3L4 ref 0.08; TGIF1 ref 0.04 | null 0.96; ESR1 alt 0.02; FOXA1 ref 0.02 | null 0.95; CREB3L4 ref 0.04; TGIF1 ref 0.01 |
| rs7001688 | null 0.95; CTCF alt 0.03; CTCF ref 0.02 | null 0.55; NME2 alt 0.22; CASZ1 alt 0.15 | null 0.95; CTCF alt 0.04; CTCF alt 0.01 | null 0.88; CASZ1 alt 0.07; NME2 alt 0.03 |
| rs73706717 | TCF7L2 alt 0.40; null 0.38; SP1 alt 0.22 | null 0.47; TCF7L2 ref 0.32; NFIC alt 0.13 | null 0.90; TCF7L2 alt 0.04; SP1 ref 0.04 | null 0.78; TCF7L2 ref 0.12; SP1 ref 0.08 |
| rs34768248 | null 0.48; MAX alt 0.22; JUN alt 0.18 | null 0.60; CREB1 alt 0.15; NKRF ref 0.09 | null 0.91; JUN alt 0.04; CTCF ref 0.03 | null 0.79; NKRF ref 0.12; CREB1 alt 0.06 |
| rs56007086 | null 0.43; FOXA1 alt 0.38; GATA3 ref 0.12 | SPDEF ref 0.34; null 0.32; TCF7L2 alt 0.23 | null 0.70; FOXA1 ref 0.18; GATA3 alt 0.08 | null 0.65; SPDEF ref 0.28; TCF7L2 alt 0.07 |

### 7.4 What this shows

1. **The test of QBiC-SELEX is `full` against `no_qbic`, scored at the TF cases and the controls together.** Asking
   only whether the null is rejected misleads both ways: QBiC-SELEX's own gate rejects "no change" at every variant,
   and an agent that names TFs more readily rejects the null at the controls too.
2. **On that test, QBiC-SELEX helps when the model cannot recall the answer and does not over-claim.** Masked Luna is
   the one run set where it shows: the null falls at every TF case and barely moves at the controls (p 0.002). In
   named mode, memory and the literature already supply the answer (Luna names every gold TF from memory alone), so
   QBiC-SELEX has nothing to add. DeepSeek recognises the famous loci even when masked, and over-claims.
3. **The tool carries more than the agents use.** QBiC-SELEX alone ranks the gold TF first of 1,109 TFs in 3 cases,
   and the screen puts it first or second among the bound TFs in all 6 cases it lists (p 0.004 against a random
   order). Masked, the agents rank the gold TF first in 1 (Luna) and 3 (DeepSeek) of the 9 cases.
4. **Where the signal is lost:**
   - The occupancy-first screen drops HOXB13, QBiC-SELEX's top TF at rs339331.
   - The 5-row limit drops TFAP2A.
   - Paralogs with the same motif (GATA2, CEBPG) share the gold TF's change.
   - The list of TFs ENCODE never assayed gives the agent candidates at every random control.
5. **This rests on one seed and 15 cases,** and the masked result on one model. The paired test was chosen after
   seeing the masked results.

## 8. What this suggests (not done)

- The site rule is principled and fixed the order at rs6983267. But on DeepSeek it does not stop the famous TF being
  proposed at its near-miss: with bound here first, a weak-site parent TF still heads the list. If the near-miss
  controls matter, the next levers are to put strong sites before the occupancy class, or to drop weak-site TFs from
  the candidate rows.
- Luna's null-first answers on the four cases with no matching ENCODE biosample come from the binding rubric: when no
  ENCODE cell type matches, binding can never reach "supported".
- Treat "unbound, assayed elsewhere" like "not assayed" when ENCODE never assayed the TF in the matching cell type.
  Binding is cell-type specific, and this rule drops HOXB13 at rs339331, where it is QBiC-SELEX's top TF.
- Apply the site rule to the TFs ENCODE never assayed as well, or show them only when no occupied TF has a strong
  site. At the random controls, every TF the agents proposed came from that list.
- A second masked seed on Luna (about $0.37) would show whether the masked result holds. Masked `single` on Luna
  (about $0.03) would show how much it recalls without the name.

## 9. Spend

- DeepSeek `full` rerun: $0.48, including the failed run. The DeepSeek eval cap was then raised from $3.50 to
  $3.90 for the masked grid, which cost $0.72. The DeepSeek eval budget stands at $3.63 of $3.90; the masked trial
  run cost $0.03 from the dev budget.
- GPT-6 Luna: $0.79 of its $2 budget: $0.03 for two trial runs (one named, one masked) in `runs/dev_v3_luna`, $0.40
  for the named grid and $0.37 for the masked grid.
- Run folders: `runs/eval_v3_deepseek` (named `full`; masked `no_qbic` and `full`) and `runs/eval_v3_luna` (named
  grid; masked `no_qbic` and `full`). Masked runs sit under `<config>/masked/0/`. Every earlier folder is kept.
