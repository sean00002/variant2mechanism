# rs13078086 and Colorectal cancer

Configuration `single`, named mode, seed 0. Models: generator claude-opus-5, critic claude-sonnet-5-5, summariser claude-haiku-5-5. Cost $0.12 over 1 model calls; 54 s.

Variant `chr3:191441666:T>G` (germline); expression context: DepMap:ACH-000971 (HCT 116).

## Ranked chains

### 1. H4: Null: no TF-mediated effect of this variant; it tags a different causal variant or is neutral (p = 0.50)

Null chain: no TF-mediated effect of this variant.

Predictions: No allelic difference in reporter assays or in TF ChIP allelic imbalance; Fine-mapping credible set shifts to a nearby variant in strong LD; No allele-specific expression of local genes in heterozygous colon tissue

Falsified if: Reproducible allele-specific reporter activity or allele-specific TF occupancy at this exact position; MPRA emVar signal for rs13078086 in colon cells

### 2. H1: Alt G creates a GC-box that gains KLF5/SP-family binding at a CCDC50-region enhancer (p = 0.18)

TF KLF5 (stated coverage not_checked; registry own_model), alt allele binds more; element Putative intronic/intergenic enhancer at chr3:191.44 Mb within or near CCDC50; gene CCDC50; cell type Colonic epithelial cells (modelled by HCT 116).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The T>G substitution raises local GC content and can complete a GC-box/CACCC-like element, so the alt allele is bound more strongly by KLF/SP-family zinc fingers; within this specificity group KLF5 is chosen because it is the KLF most highly expressed in colonic epithelium and colorectal cancer lines such as HCT 116. | missing | none |
| element | The variant lies in a candidate cis-regulatory element (open chromatin / H3K27ac-marked enhancer) active in colonic epithelium, not in a protein-coding exon. | missing | none |
| gene | That element loops to and regulates CCDC50, the nearest expressed gene at the locus. | missing | none |
| cell_type | KLF5 is abundant in proliferating intestinal crypt epithelium and in HCT 116, so the allelic difference is realised in that cell type. | missing | none |
| phenotype | Increased KLF5-driven expression of the target gene supports crypt progenitor proliferation and modestly increases colorectal cancer risk. | missing | none |

Predictions: Alt allele shows higher reporter activity in HCT 116 and higher KLF5 ChIP/CUT&RUN signal; KLF5 knockdown collapses the allelic reporter difference; Effect is epithelial-specific, absent in lymphoblastoid cells

Falsified if: No KLF/SP footprint or ChIP signal over the variant in colon epithelial cells; QBiC/SELEX shows no KLF-family score gain for alt G; Reporter shows ref > alt or no difference

### 3. H2: Ref T preserves a TCF7L2 Wnt-response element; alt G disrupts it (p = 0.17)

TF TCF7L2 (stated coverage not_checked; registry mapped), ref allele binds more; element Wnt-responsive enhancer at chr3:191.44 Mb; gene CCDC50; cell type Colorectal adenocarcinoma epithelium (HCT 116, beta-catenin activated).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The TCF/LEF consensus (CTTTG(T/A)(T/A)) is T-rich, so a T>G change at such a position lowers predicted affinity; TCF7L2 is chosen from the TCF/LEF specificity group because it is the dominant family member in colonic epithelium and HCT 116. | missing | none |
| element | The variant sits in an enhancer carrying clustered TCF/LEF motifs typical of colorectal Wnt-response elements. | missing | none |
| gene | The enhancer contacts CCDC50 (or, alternatively, the more distal FGF12) and sets its basal expression. | missing | none |
| cell_type | Constitutive Wnt/beta-catenin signalling in colonic adenoma and carcinoma cells makes TCF7L2 occupancy functionally consequential there. | missing | none |
| phenotype | Altered Wnt target dosage shifts crypt stem-cell dynamics and changes colorectal cancer risk. | missing | none |

Predictions: TCF7L2 ChIP-seq peak over the variant in HCT 116 with allelic imbalance favouring T; Reporter activity drops with alt allele and is beta-catenin dependent; Effect lost upon TCF7L2 knockdown or Wnt inhibition

Falsified if: No TCF7L2 ChIP signal at the locus in colorectal lines; No TCF/LEF motif match on either strand around the variant; Reporter difference unaffected by Wnt pathway manipulation

### 4. H3: Ref T supports a CDX2 homeodomain site controlling an intestinal enhancer (p = 0.15)

TF CDX2 (stated coverage not_checked; registry own_model), ref allele binds more; element Intestine-specific enhancer at chr3:191.44 Mb; gene FGF12; cell type Intestinal epithelial cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | CDX/caudal-type homeodomain sites are A/T-rich (TTTAT core), so alt G is predicted to reduce binding; within the CDX specificity group CDX2 is chosen because it is the intestine-restricted member expressed in colon and HCT 116, whereas CDX1 is lower and CDX4 absent. | missing | none |
| element | The variant lies within an A/T-rich intestinal enhancer bound by CDX2/HNF4A-type lineage factors. | missing | none |
| gene | The element acts over a longer range on FGF12 rather than the nearest gene. | missing | none |
| cell_type | CDX2 is an intestinal master regulator, limiting the effect to colonic epithelium. | missing | none |
| phenotype | Weakened CDX2-dependent enhancer activity blunts differentiation programmes and slightly raises colorectal cancer risk. | missing | none |

Predictions: CDX2 CUT&RUN shows ref-preferential occupancy; Allelic effect present in colon lines but not in non-intestinal cells; CRISPRi of the element lowers FGF12, not CCDC50

Falsified if: No CDX2 binding at the variant; CRISPRi of the element changes CCDC50 only; No A/T-rich homeodomain motif at the site

## Prediction matrix

| Test | Cost | Separates top two | H4 | H1 | H2 | H3 |
| --- | --- | --- | --- | --- | --- | --- |
| Allele-specific reporter (MPRA or luciferase) of the 200 bp element, both alleles, in HCT 116 | low | yes | no allelic difference | alt > ref activity | ref > alt activity, Wnt-dependent | ref > alt activity, intestine-restricted |
| KLF5 and TCF7L2 ChIP-seq / CUT&RUN in HCT 116 with allelic read counting at the heterozygous site | medium | yes | no peak or no allelic bias | KLF5 peak, alt-biased reads | TCF7L2 peak, ref-biased reads | neither factor bound |
| QBiC-SELEX / PWM scoring of the 21 bp window for KLF, TCF/LEF and CDX models | existing data | yes | no significant score change for any family | KLF/SP score gain on alt | TCF/LEF score loss on alt | CDX score loss on alt |
| CRISPRi tiling of the element in HCT 116 with RNA readout of CCDC50 and FGF12 | medium | no | no gene responds | CCDC50 down | CCDC50 down | FGF12 down |
| Fine-mapping plus colon eQTL/ASE at the locus in existing cohorts | existing data | no | another LD variant carries the signal; no ASE | rs13078086 in credible set with local eQTL | rs13078086 in credible set with local eQTL | credible set with FGF12 eQTL |

## Next experiment

Run the free computational step first (QBiC-SELEX/PWM scoring of the 21 bp window for KLF/SP, TCF/LEF and CDX models) and then, as the cheapest wet experiment, a dual-allele luciferase/MPRA reporter of the element in HCT 116: the direction of the allelic difference (alt > ref vs ref > alt vs none) separates H1 from H2 and both from the null.

## Flags

- none

## Evidence
