# rs12740374 and LDL cholesterol, myocardial infarction (1p13)

Configuration `single`, named mode, seed 0. Models: generator claude-opus-5, critic claude-sonnet-5-5, summariser claude-haiku-5-5. Cost $0.12 over 1 model calls; 50 s.

Variant `chr1:109274968:G>T` (germline); expression context: DepMap:ACH-000625 (Hep 3B2.1-7).

## Ranked chains

### 1. H1: Alt T allele creates a C/EBP (CEBPB) site that activates the SORT1 liver enhancer, raising SORT1 and lowering LDL (p = 0.50)

TF CEBPB (stated coverage not_checked; registry own_model), alt allele binds more; element Liver enhancer within the 1p13 CELSR2/PSRC1/SORT1 locus containing rs12740374; gene SORT1; cell type Hepatocyte (modelled here by Hep 3B2.1-7).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The minor T allele generates a C/EBP-family recognition sequence, so the alt allele is bound more strongly than ref; within the C/EBP specificity group CEBPB is chosen because it is highly expressed in hepatocytes and hepatoma lines and has ChIP-seq occupancy at this locus in liver. | missing | none |
| element | The variant sits in a hepatocyte-active enhancer; creation of the C/EBP site increases enhancer activity on the alt allele. | missing | none |
| gene | Increased enhancer activity raises SORT1 transcription in cis (the locus is a strong liver eQTL for SORT1). | missing | none |
| cell_type | The effect is hepatocyte-restricted, matching liver-specific C/EBP activity and SORT1 expression. | missing | none |
| phenotype | Higher hepatic SORT1 increases clearance/reduced secretion of apoB-containing lipoproteins, lowering plasma LDL-C and myocardial infarction risk. | missing | none |

Predictions: Allele-specific C/EBP ChIP (CEBPB) in liver/HepG2-like cells shows preferential occupancy of the T allele; Luciferase reporter: T allele enhancer gives higher activity in hepatocytes, abolished by mutating the C/EBP core; CEBPB knockdown reduces SORT1 expression specifically on the T-allele background; CRISPR deletion of the element lowers SORT1 mRNA in hepatocytes but not in non-hepatic cells

Falsified if: No allelic difference in C/EBP binding by EMSA/ChIP; Reporter shows no T>G activity difference in hepatocytes; CEBPB depletion leaves SORT1 unchanged

### 2. H0: Null: rs12740374 has no TF-mediated allelic effect; association is driven by a linked variant in the 1p13 haplotype (p = 0.20)

Null chain: no TF-mediated effect of this variant.

Predictions: No allelic difference in reporter assay or allele-specific ChIP at this position; Base editing of rs12740374 alone in hepatocytes leaves SORT1 expression unchanged; Another variant on the haplotype shows the allelic activity

Falsified if: Single-base editing of rs12740374 changes SORT1 expression; Allele-specific TF binding is demonstrated at this position

### 3. H2: The created site is bound by a different C/EBP-group member, CEBPA, which drives the same SORT1 enhancer (p = 0.18)

TF CEBPA (stated coverage not_checked; registry own_model), alt allele binds more; element Same hepatocyte enhancer at rs12740374; gene SORT1; cell type Hepatocyte.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The alt T allele creates the shared C/EBP motif; CEBPA is selected within the group as the dominant constitutive C/EBP in differentiated hepatocytes, which may matter more than CEBPB in vivo. | missing | none |
| element | CEBPA binding to the alt allele activates the enhancer. | missing | none |
| gene | SORT1 transcription increases in cis. | missing | none |
| cell_type | Restricted to hepatocytes where CEBPA is abundant; hepatoma lines with low CEBPA would show a weaker effect. | missing | none |
| phenotype | Higher SORT1 lowers LDL-C and MI risk. | missing | none |

Predictions: CEBPA knockdown, not CEBPB knockdown, abolishes the allelic difference; Allelic effect is weaker in hepatoma lines with low CEBPA and restored by CEBPA re-expression; CEBPA ChIP shows T-allele-preferential binding

Falsified if: CEBPA depletion has no effect on SORT1 while CEBPB depletion does; CEBPA ChIP shows no occupancy at the element

### 4. H3: Alt allele increases binding of a hepatic nuclear receptor/HNF factor rather than C/EBP, altering SORT1 (p = 0.07)

TF HNF4A (stated coverage not_checked; registry own_model), alt allele binds more; element Hepatocyte regulatory element at rs12740374; gene SORT1; cell type Hepatocyte.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The sequence change could instead improve an HNF4A half-site; HNF4A is chosen among liver nuclear receptors because it is the dominant hepatocyte regulator with widespread enhancer occupancy. | missing | none |
| element | HNF4A binding raises element activity on the alt allele. | missing | none |
| gene | SORT1 expression increases in cis. | missing | none |
| cell_type | Effect limited to HNF4A-expressing hepatocytes. | missing | none |
| phenotype | Raised SORT1 lowers plasma LDL-C and MI risk. | missing | none |

Predictions: HNF4A ChIP shows allele-preferential binding at the element; HNF4A knockdown abolishes the allelic reporter difference while C/EBP knockdown does not; Mutating a predicted HNF4A half-site, not the C/EBP core, removes the allelic effect

Falsified if: No HNF4A occupancy at the element; Mutating the C/EBP core alone abolishes the allelic effect

### 5. H4: Alt allele acts through a repressor whose binding is lost, with the net effect on a neighbouring gene (CELSR2/PSRC1) rather than SORT1 (p = 0.05)

TF CEBPB (stated coverage not_checked; registry own_model), ref allele binds more; element 1p13 element at rs12740374 acting on the CELSR2/PSRC1 promoter region; gene CELSR2; cell type Hepatocyte.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | Alternatively the ref G allele is the better-bound state for a C/EBP-like repressive isoform (e.g. LIP form of CEBPB), so binding is lost on the alt allele. | missing | none |
| element | Loss of repressor binding de-represses the element on the alt allele. | missing | none |
| gene | The de-repressed element acts mainly on CELSR2/PSRC1, which are also strong eQTL targets at this locus. | missing | none |
| cell_type | Effect confined to liver where the locus is active. | missing | none |
| phenotype | Altered CELSR2/PSRC1 levels change hepatic lipoprotein handling and LDL-C. | missing | none |

Predictions: Allele-specific expression at the locus is seen for CELSR2/PSRC1 but not SORT1; SORT1 knockdown does not reproduce the lipid phenotype in hepatocyte models; Reporter shows higher activity for alt via loss of a repressor footprint

Falsified if: Enhancer deletion changes only SORT1 and not CELSR2/PSRC1; Allele-specific binding is gain, not loss, on the alt allele

## Prediction matrix

| Test | Cost | Separates top two | H1 | H0 | H2 | H3 | H4 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Allele-specific luciferase reporter of the ~500 bp element (G vs T) in Hep 3B2.1-7 hepatocytes, with and without mutation of the created C/EBP core | low | no | T > G activity; abolished by C/EBP core mutation | No allelic difference | T > G activity; abolished by C/EBP core mutation (indistinguishable here) | T > G activity but unaffected by C/EBP core mutation | T > G via loss of repression; direction may invert in repressor-high conditions |
| Parallel siRNA knockdown of CEBPB vs CEBPA in hepatocytes, measuring endogenous SORT1 and allelic reporter activity | low | yes | CEBPB knockdown reduces SORT1/allelic effect | No allelic effect to modulate | CEBPA knockdown reduces SORT1/allelic effect | Neither knockdown changes the effect | Knockdown raises target expression (de-repression) |
| Allele-specific ChIP-qPCR for CEBPB, CEBPA and HNF4A in heterozygous liver cells | medium | yes | CEBPB T-allele biased | No allelic bias | CEBPA T-allele biased | HNF4A T-allele biased | G-allele biased occupancy |
| Base editing of rs12740374 G>T in an isogenic hepatocyte line and RNA-seq of SORT1/CELSR2/PSRC1 | high | no | SORT1 up | No expression change | SORT1 up | SORT1 up | CELSR2/PSRC1 changed, SORT1 unchanged |

## Next experiment

Side-by-side siRNA knockdown of CEBPB versus CEBPA in Hep 3B2.1-7 cells carrying the allelic reporter (and measuring endogenous SORT1): it is cheap and is the single test that distinguishes H1 from H2, while a complete absence of any allelic effect would also support the null.

## Flags

- none

## Evidence
