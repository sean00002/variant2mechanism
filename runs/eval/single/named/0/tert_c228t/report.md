# TERT promoter C228T and Glioblastoma, melanoma, bladder

Configuration `single`, named mode, seed 0. Models: generator claude-opus-5, critic claude-sonnet-5-5, summariser claude-haiku-5-5. Cost $0.12 over 1 model calls; 55 s.

Variant `chr5:1295113:G>A` (somatic); expression context: DepMap:subtype=Glioblastoma (median of 54 lines).

## Ranked chains

### 1. H1: C228T creates a de novo ETS site bound by the GABPA/GABPB1 tetramer, driving TERT reactivation (p = 0.60)

TF GABPA (stated coverage not_checked; registry own_model), alt allele binds more; element TERT core promoter, ~124 bp upstream of ATG (C228T site, chr5:1295113); gene TERT; cell type Glioblastoma tumour cells / glioma stem cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The alt (A on plus strand; C>T on the TERT minus strand) allele generates a new 5'-GGAA-3' ETS core; among ETS factors the GABPA/GABPB1 heterotetramer is selected because it uniquely requires two GGAA sites in the correct spacing (the new site plus the native ETS site ~19 bp away) and because GABPA is well expressed in glioblastoma lines; no QBiC-SELEX lookup was performed, so coverage is unverified. | missing | none |
| element | The site lies inside the TERT core promoter, a compact element that controls TERT transcription initiation; gain of the ETS site converts an otherwise silent promoter into an active one with gain of H3K4me2/3 and Pol II on the mutant allele. | missing | none |
| gene | TERT is the direct and essentially only target of this promoter; mutant-allele-specific transcription raises TERT mRNA several-fold over the near-zero level in normal brain. | missing | none |
| cell_type | Glioblastoma cells (and melanoma, bladder urothelium) lack ALT and depend on telomerase; GABPB1L is expressed in these tumours, making the mechanism cell-type permissive. | missing | none |
| phenotype | Restored telomerase activity prevents telomere attrition and crisis, permitting unlimited proliferation and tumour progression. | missing | none |

Predictions: Allele-specific GABPA/GABPB1 ChIP-seq signal at chr5:1295113 confined to the mutant allele; Knockdown of GABPB1L (not GABPB1S) selectively reduces TERT expression in C228T lines but not in TERT-wild-type lines; Mutating the native upstream ETS site abolishes the gain conferred by C228T in a reporter, because tetramer formation needs both sites; GABPA CRISPRi/degron reduces TERT mRNA within hours in C228T lines

Falsified if: GABPA/GABPB1 ChIP shows no allele-biased occupancy at the site in C228T-positive lines; GABPA or GABPB1L depletion leaves TERT mRNA unchanged in C228T lines; Reporter activity gained by C228T is unaffected by destroying the partner native ETS site

### 2. H4: Null: no TF-mediated effect of this specific base change (p = 0.22)

Null chain: no TF-mediated effect of this variant.

Predictions: TERT mRNA and telomerase activity are indistinguishable between isogenic C228T-edited and parental cells; Reporter assays show no allele difference for the 228 position; Any TERT expression in mutant tumours tracks with amplification, methylation or other cis events rather than with the C228T allele

Falsified if: Isogenic knock-in of C228T into TERT-silent cells raises TERT expression and telomerase activity; Allele-specific TERT transcription from the mutant allele is demonstrated in heterozygous tumours

### 3. H2: The new GGAA site is bound by ETS1, which activates TERT (p = 0.10)

TF ETS1 (stated coverage not_checked; registry own_model), alt allele binds more; element TERT core promoter C228T site; gene TERT; cell type Glioblastoma tumour cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | ETS1 is chosen from the same GGAA-binding specificity group because it is highly expressed in glioma and melanoma and binds single GGAA sites as a monomer, not requiring a partner site; coverage not checked. | missing | none |
| element | ETS1 occupancy at the new site nucleates activation of the TERT core promoter. | missing | none |
| gene | TERT transcription increases on the mutant allele. | missing | none |
| cell_type | ETS1 is abundant in glioblastoma and in MAPK-driven melanoma, where TERT promoter mutations are most frequent. | missing | none |
| phenotype | Telomerase reactivation supports replicative immortality. | missing | none |

Predictions: ETS1 ChIP-seq shows allele-specific occupancy at the mutant site; GABPA does not; ETS1 knockdown lowers TERT mRNA in C228T lines while GABPB1L knockdown does not; A single isolated GGAA site in a minimal reporter is sufficient for activation, independent of the native upstream ETS site

Falsified if: ETS1 depletion does not change TERT expression in C228T lines; ETS1 ChIP shows no signal at the TERT promoter

### 4. H3: A ternary complex factor (ELK4/ELK1 family) occupies the new site downstream of MAPK signalling (p = 0.08)

TF ELK4 (stated coverage not_checked; registry own_model), alt allele binds more; element TERT core promoter C228T site; gene TERT; cell type Glioblastoma tumour cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | Within the GGAA specificity group, ELK4 (and ELK1) are selected because TCFs are MAPK-responsive, matching the strong co-occurrence of TERT promoter mutations with BRAF/RAS-activated tumours; coverage not checked. | missing | none |
| element | Phospho-ELK4 at the new ETS site converts the TERT core promoter into a MAPK-responsive element. | missing | none |
| gene | TERT expression becomes dependent on ERK pathway activity in mutant cells. | missing | none |
| cell_type | Glioblastoma lines with RTK/RAS pathway activation provide the required ERK input. | missing | none |
| phenotype | Sustained telomerase activity enables immortalisation and is MEK-inhibitor sensitive. | missing | none |

Predictions: MEK inhibition sharply reduces TERT mRNA in C228T lines but not in TERT-wild-type lines; ELK1/ELK4 ChIP shows mutant-allele-specific binding; Serum stimulation acutely induces TERT from the mutant allele

Falsified if: MEK inhibition leaves mutant-allele TERT transcription intact; No ELK1/ELK4 occupancy detectable at the TERT promoter

## Prediction matrix

| Test | Cost | Separates top two | H1 | H4 | H2 | H3 |
| --- | --- | --- | --- | --- | --- | --- |
| Re-analyse existing GABPA, GABPB1 and ETS1 ChIP-seq from C228T-positive glioblastoma/melanoma lines for allele-specific reads at chr5:1295113 | existing data | yes | GABPA/GABPB1 reads are mutant-allele biased | No allele bias for any ETS factor | ETS1 reads are mutant-allele biased; GABPA is not | Neither; ELK1/ELK4 signal instead |
| siRNA/CRISPRi knockdown of GABPB1L vs ETS1 vs ELK4, measuring TERT mRNA in C228T and wild-type lines | low | yes | GABPB1L loss selectively lowers TERT in mutant lines | No knockdown changes TERT selectively in mutant lines | ETS1 loss lowers TERT in mutant lines | ELK4 loss (or MEK inhibition) lowers TERT |
| Luciferase reporter with C228T alone vs C228T plus destruction of the native upstream ETS site | low | yes | Gain requires both sites (tetramer dependence) | No gain from C228T in any configuration | Single new site suffices | Single site suffices and gain is serum/ERK dependent |
| Isogenic CRISPR knock-in of C228T into a TERT-silent primary cell line; measure TERT mRNA, telomerase and telomere length | high | no | TERT induced, GABP-dependent | No change | TERT induced, ETS1-dependent | TERT induced, MAPK-dependent |

## Next experiment

Mine existing GABPA/GABPB1 and ETS1 ChIP-seq datasets from C228T-heterozygous glioblastoma or melanoma lines for allele-specific reads over chr5:1295113; this costs nothing new and directly distinguishes GABP (H1) from ETS1 (H2), while absence of any allele-biased ETS occupancy would support the null.

## Flags

- none

## Evidence
