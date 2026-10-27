# rs7001688 and LDL cholesterol

Configuration `single`, named mode, seed 0. Models: generator claude-opus-5, critic claude-sonnet-5-5, summariser claude-haiku-5-5. Cost $0.12 over 1 model calls; 50 s.

Variant `chr8:57573391:G>T` (germline); expression context: DepMap:ACH-000625 (Hep 3B2.1-7).

## Ranked chains

### 1. H4: Null: no TF-mediated effect of rs7001688; the association is carried by a linked causal variant or is a passenger (p = 0.48)

Null chain: no TF-mediated effect of this variant.

Predictions: Fine-mapping places the credible-set posterior on a different variant in LD; No allelic difference in reporter assays or ChIP allelic imbalance at rs7001688; Base editing of rs7001688 alone in Hep3B changes no nearby gene's expression

Falsified if: Reporter or CRISPR editing of rs7001688 alone reproducibly changes expression of a nearby gene; Clear allele-specific TF binding is demonstrated at this position

### 2. H1: Ref G preserves an HNF4A half-site in a hepatocyte enhancer driving PLAG1/CHCHD7; alt T weakens it and lowers expression (p = 0.22)

TF HNF4A (stated coverage not_checked; registry own_model), ref allele binds more; element Putative liver enhancer at chr8:57.57Mb within the PLAG1/CHCHD7/MOS/RPS20 interval; gene PLAG1; cell type Hepatocyte (modelled by Hep 3B2.1-7, DepMap ACH-000625).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The G allele completes a DR1-like nuclear-receptor motif (AGGTCA-like half-site) bound by HNF4A; the T allele disrupts the core and reduces predicted affinity. HNF4A is chosen within the HNF4/NR2F specificity group because HNF4A is the dominant family member expressed in hepatocytes. | missing | none |
| element | The variant lies in a non-coding, likely enhancer-like region active in liver; loss of the HNF4A site reduces enhancer output. | missing | none |
| gene | The enhancer contacts the PLAG1/CHCHD7 promoter region, so the alt allele lowers PLAG1 expression in liver. | missing | none |
| cell_type | Effect is hepatocyte-restricted because HNF4A occupancy at this element requires liver-specific factor availability. | missing | none |
| phenotype | Altered PLAG1-dependent transcriptional program changes hepatic lipoprotein handling, shifting plasma LDL cholesterol. | missing | none |

Predictions: HNF4A ChIP-seq in HepG2/Hep3B shows a peak overlapping the variant with allelic imbalance favouring G; HNF4A knockdown in Hep3B reduces reporter activity of the G allele specifically; eQTL for PLAG1 or CHCHD7 in liver with G associated with higher expression

Falsified if: No HNF4A ChIP signal or open chromatin at the site in liver cells; Luciferase reporter shows no allelic difference, or T > G; HNF4A knockdown leaves allelic reporter difference intact

### 3. H2: Alt T creates a CEBPB site that increases repressive/activating occupancy at a liver element, altering local gene expression (p = 0.17)

TF CEBPB (stated coverage not_checked; registry own_model), alt allele binds more; element Same chr8:57.57Mb non-coding element; gene CHCHD7; cell type Hepatocyte (Hep 3B2.1-7).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The T allele generates a TTGC-containing bZIP half-site matching the C/EBP specificity group; CEBPB is chosen over CEBPA/CEBPD because it is robustly expressed in Hep3B and in adult liver and has the broadest ChIP-seq footprint there. | missing | none |
| element | Gained C/EBP occupancy changes the regulatory output of this element in liver. | missing | none |
| gene | Nearest promoter affected is CHCHD7/PLAG1 bidirectional region; expression shifts with genotype. | missing | none |
| cell_type | CEBPB is highly active in hepatocytes, confining the effect to liver. | missing | none |
| phenotype | Changed hepatic expression alters LDL receptor pathway flux and plasma LDL cholesterol. | missing | none |

Predictions: EMSA with Hep3B nuclear extract shows a new CEBP-family complex on the T probe, supershifted by anti-CEBPB; CEBPB ChIP-qPCR enrichment at the locus is genotype-dependent; Reporter shows T > G activity

Falsified if: No gained complex on the T probe; CEBPB knockdown does not change allelic reporter difference; Reporter shows G > T

### 4. H3: A FOXA pioneer site is altered, changing chromatin accessibility of the element in liver (p = 0.13)

TF FOXA2 (stated coverage not_checked; registry own_model), ref allele binds more; element chr8:57.57Mb liver-accessible region; gene PENK/MOS-proximal regulatory domain (nearest expressed liver gene in the TAD); cell type Hepatocyte (Hep 3B2.1-7).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The G allele supports a forkhead core (TGTTT-like); the T allele degrades it. FOXA2 is selected from the FOXA specificity group because FOXA1/FOXA2/FOXA3 share the motif but FOXA2 is the most highly expressed forkhead pioneer factor in hepatocyte lines. | missing | none |
| element | FOXA2 acts as a pioneer; weaker binding reduces nucleosome displacement and accessibility of the element. | missing | none |
| gene | Reduced accessibility lowers transcription of the nearest liver-expressed gene in the same contact domain. | missing | none |
| cell_type | Pioneer-dependent accessibility is liver-specific. | missing | none |
| phenotype | Downstream change in hepatic lipid gene expression shifts LDL cholesterol. | missing | none |

Predictions: ATAC-seq in heterozygous liver shows allelic imbalance in accessibility favouring G; FOXA2 ChIP shows allele-biased binding; Effect persists after HNF4A or CEBPB knockdown

Falsified if: No allelic accessibility imbalance; FOXA2 ChIP shows no binding at the element

## Prediction matrix

| Test | Cost | Separates top two | H4 | H1 | H2 | H3 |
| --- | --- | --- | --- | --- | --- | --- |
| Allele-specific luciferase reporter of the ~500 bp element (G vs T) in Hep 3B2.1-7 | low | yes | No allelic difference | G > T activity | T > G activity | G > T, but modest in episomal context |
| EMSA with Hep3B nuclear extract plus supershift using anti-HNF4A and anti-CEBPB | low | yes | No allele-specific complex | G probe complex supershifted by anti-HNF4A | T probe complex supershifted by anti-CEBPB | Complex not shifted by either antibody |
| ChIP-seq allelic imbalance in heterozygous liver/HepG2 for HNF4A, CEBPB, FOXA2 | existing data | yes | No peak or no imbalance | HNF4A reads biased to G | CEBPB reads biased to T | FOXA2 reads biased to G |
| CRISPR base editing of rs7001688 in Hep3B followed by RNA-seq of the 1 Mb window | high | yes | No expression change | PLAG1 down with T | CHCHD7 up with T | Broad accessibility-linked decrease with T |
| Statistical fine-mapping of the LDL locus with liver eQTL colocalisation | existing data | no | Another LD variant carries the signal | rs7001688 in credible set, colocalises with PLAG1 eQTL | rs7001688 in credible set, colocalises with CHCHD7 eQTL | rs7001688 in credible set, weak eQTL |

## Next experiment

Run the allele-specific luciferase reporter (G vs T element) in Hep 3B2.1-7: it is cheap and directly distinguishes the null (no allelic difference) from H1 (G > T), the current top two, while also flagging H2 if T > G.

## Flags

- none

## Evidence
