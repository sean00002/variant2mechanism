# TERT promoter C250T and Glioblastoma, melanoma, bladder

Configuration `single`, named mode, seed 0. Models: generator claude-opus-5, critic claude-sonnet-5-5, summariser claude-haiku-5-5. Cost $0.15 over 1 model calls; 62 s.

Variant `chr5:1295135:G>A` (somatic); expression context: DepMap:subtype=Glioblastoma (median of 54 lines).

## Ranked chains

### 1. H1: C250T creates a de novo ETS site bound by GABPA/GABPB1, driving monoallelic TERT reactivation in glioblastoma (p = 0.62)

TF GABPA (stated coverage not_checked; registry own_model), alt allele binds more; element TERT core promoter, -250 bp from ATG (chr5:1295135); gene TERT; cell type Glioma stem/progenitor cells and glioblastoma tumour cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The alt (A on plus strand; C>T on the TERT-coding minus strand) allele generates a canonical 5'-GGAA-3' ETS core that is absent from the ref allele; among ETS factors the GABPA/GABPB1 heterotetramer is selected because it uniquely requires two ETS sites in the correct spacing, which the new site plus the native ETS site at -200 provides, and because GABPA is ubiquitously expressed in glioma lines. | missing | none |
| element | The new site lies in the TERT core promoter, which carries active-promoter chromatin marks and acquires H3K4me2/3 selectively on the mutant allele. | missing | none |
| gene | GABPA/GABPB1 recruitment activates transcription of TERT specifically from the mutant allele, giving modest but sufficient telomerase reactivation. | missing | none |
| cell_type | Glioblastoma cells (and melanoma, bladder urothelium) lack an alternative telomere-maintenance route and depend on this reactivation; GABPA is expressed in these cells. | missing | none |
| phenotype | Restored telomerase permits unlimited replicative capacity, enabling tumour outgrowth and conferring the poor prognosis associated with TERT promoter mutations in IDH-wildtype glioblastoma. | missing | none |

Predictions: GABPA and GABPB1 ChIP shows allele-specific occupancy at the mutant TERT promoter and no occupancy at wild-type promoters.; GABPA or GABPB1L knockdown selectively reduces TERT mRNA in C250T/C228T-mutant lines but not in TERT-promoter-wildtype lines.; Reporter assays with the mutant promoter lose activity when the created GGAA is scrambled or when the spacing to the native -200 ETS site is altered.

Falsified if: GABPA/GABPB1 ChIP shows no enrichment at the mutant allele.; GABPA knockdown leaves TERT expression unchanged in mutant lines while another ETS factor's knockdown does reduce it.

### 2. H2: The de novo ETS site is bound by ETS1 rather than GABPA (p = 0.13)

TF ETS1 (stated coverage not_checked; registry own_model), alt allele binds more; element TERT core promoter at chr5:1295135; gene TERT; cell type Glioblastoma cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The alt allele creates a GGAA core matching the ETS consensus; ETS1 is chosen within the ETS group because it is expressed in glioma and melanoma and has been reported to activate mutant TERT promoters downstream of MAPK signalling. | missing | none |
| element | The site sits in the TERT core promoter and becomes nucleosome-depleted on the mutant allele. | missing | none |
| gene | ETS1 binding increases TERT transcription from the mutant allele. | missing | none |
| cell_type | ETS1 levels are MAPK-dependent, so the effect is strongest in cells with active RAS/BRAF-MEK-ERK signalling, common in glioblastoma and melanoma. | missing | none |
| phenotype | Telomerase reactivation sustains proliferation and tumour growth. | missing | none |

Predictions: MEK inhibition lowers TERT mRNA in mutant lines proportionally to ETS1 activity, independently of GABPA levels.; ETS1 ChIP, not GABPA ChIP, shows allele-specific occupancy.; ETS1 knockdown reduces mutant-allele TERT expression.

Falsified if: ETS1 knockdown does not change TERT levels in mutant lines.; No ETS1 ChIP signal at the TERT promoter in mutant cells.

### 3. H3: The created site is bound by ELK4 (TCF subfamily) acting with serum-response signalling (p = 0.09)

TF ELK4 (stated coverage not_checked; registry own_model), alt allele binds more; element TERT core promoter at chr5:1295135; gene TERT; cell type Glioblastoma cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The alt allele creates a GGAA core compatible with TCF-subfamily ETS binding; ELK4 is chosen within this group because it is broadly expressed in glioma lines and binds single ETS sites without a partner. | missing | none |
| element | Binding occurs in the TERT core promoter immediately upstream of the transcription start site. | missing | none |
| gene | ELK4 recruitment raises TERT transcription from the mutant allele. | missing | none |
| cell_type | Effect requires ERK-phosphorylated ELK4, so it tracks with growth-factor signalling in glioblastoma cells. | missing | none |
| phenotype | Telomere maintenance supports continued tumour cell division. | missing | none |

Predictions: ELK4 knockdown reduces TERT in mutant but not wild-type lines.; Allele-specific ELK4 ChIP signal at the TERT promoter.; Single-site reporter (new GGAA only, native -200 site deleted) retains activity, unlike the GABPA model.

Falsified if: ELK4 depletion has no effect on TERT.; Activity of the mutant reporter strictly requires the second, native ETS site.

### 4. H4: The created site is bound by ELF1, which is the functional activator at the mutant promoter (p = 0.09)

TF ELF1 (stated coverage not_checked; registry own_model), alt allele binds more; element TERT core promoter at chr5:1295135; gene TERT; cell type Glioblastoma cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | ELF-subfamily factors prefer AGGAAGT-like sequences; the alt allele produces such a core, and ELF1 is chosen within the group for its high and near-universal expression in tumour lines. | missing | none |
| element | The site is within the TERT core promoter and gains accessibility on the mutant allele. | missing | none |
| gene | ELF1 occupancy increases TERT transcription from the mutant allele. | missing | none |
| cell_type | ELF1 is abundant in glioblastoma lines, so the effect does not depend on a signalling-regulated partner. | missing | none |
| phenotype | Sustained telomerase activity supports immortalisation and tumour progression. | missing | none |

Predictions: ELF1 ChIP shows allele-specific occupancy; GABPA does not.; ELF1 knockdown reduces TERT in mutant lines.; TERT levels correlate with ELF1 expression across mutant glioblastoma lines.

Falsified if: ELF1 depletion leaves TERT unchanged.; No ELF1 enrichment at the mutant promoter.

### 5. H5: Null: no TF-mediated effect of this specific base change (p = 0.07)

Null chain: no TF-mediated effect of this variant.

Predictions: Editing only this base into a TERT-promoter-wildtype glioblastoma line changes neither TERT mRNA nor telomerase activity.; Mutant and wildtype alleles show equal nascent TERT transcription in heterozygous lines.; No TF shows differential occupancy between alleles.

Falsified if: Single-base knock-in raises TERT expression or telomerase activity.; Allele-specific TERT expression is seen in heterozygous mutant tumours.

## Prediction matrix

| Test | Cost | Separates top two | H1 | H2 | H3 | H4 | H5 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| GABPA and GABPB1 ChIP-qPCR (or CUT&RUN) at the TERT promoter in a C250T-mutant versus promoter-wildtype glioblastoma line | low | yes | Strong mutant-specific GABPA and GABPB1 signal | No or weak GABPA signal; ETS1 signal instead | No GABPA signal | No GABPA signal | No allele-specific signal for any factor |
| siRNA/shRNA knockdown panel (GABPA, GABPB1, ETS1, ELK4, ELF1) with TERT RT-qPCR in mutant and wildtype lines | low | yes | GABPA/GABPB1 knockdown lowers TERT only in mutant lines | ETS1 knockdown lowers TERT | ELK4 knockdown lowers TERT | ELF1 knockdown lowers TERT | No knockdown changes mutant-specific TERT levels |
| Luciferase reporter with mutant promoter, with and without the native -200 ETS site, plus scrambled new GGAA | low | no | Activity needs both ETS sites (multimeric GABP requirement) | Single new site suffices | Single new site suffices | Single new site suffices | Mutant and reference reporters are equally active |
| CRISPR single-base knock-in of C250T into a TERT-promoter-wildtype line; measure allele-specific TERT and telomerase activity | medium | no | TERT up, telomerase restored | TERT up | TERT up | TERT up | No change |
| MEK inhibitor treatment of mutant lines with TERT RT-qPCR | low | yes | TERT largely unchanged | TERT falls (ETS1 is MAPK-dependent) | TERT falls (ELK4 is ERK-dependent) | TERT largely unchanged | No mutant-specific change |

## Next experiment

Run a single ChIP-qPCR/CUT&RUN panel for GABPA, GABPB1 and ETS1 at the TERT core promoter in one C250T-mutant and one promoter-wildtype glioblastoma line: mutant-specific GABPA+GABPB1 enrichment supports H1, while ETS1-only enrichment supports H2, and absence of any allele-specific occupancy supports the null.

## Flags

- none

## Evidence
