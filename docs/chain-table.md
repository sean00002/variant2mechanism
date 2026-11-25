# The chain table

What a run hands back for one variant, fixed before any model is asked. A checker can test a table against this
page without knowing the right answer, so it also works for a variant nobody has studied.

## A chain is eight small claims

A chain is one route from the variant to a trait. It names a transcription factor (or a group of TFs that share a
QBiC-SELEX model), the element the variant lies in, a target gene and a trait. It has four steps, and each step is two
claims:

| Step | The alleles differ | The parts are in place |
|---|---|---|
| 1. TF binding | The two alleles differ in binding the TF. | The TF is present where it would act: expressed in the context, or bound at the site. |
| 2. Regulatory activity | The two alleles differ in the regulatory activity of the site. | The variant lies in a regulatory element. |
| 3. Target gene | The two alleles differ in the gene's RNA or protein. | The element regulates the gene. |
| 4. Trait | The two alleles differ in the trait. | The gene bears on the trait. |

The left column is about this variant's two alleles. Only a record that names this variant can fill it: a record
about a neighbouring variant, or about knocking down the TF or the gene, cannot. The right column is true or false
whatever the allele, so a record that names no variant can fill it.

Every chain has all eight claims, whether or not the run stated them. A claim nobody stated still names what the
chain names (its TF, the variant's element, its gene, its traits), so its cells say what was looked up for it and
what is on file. A claim that names nothing of a kind, such as the gene claims of a chain with no gene, is about
anything of that kind at the variant.

## Each claim has three cells

One cell per kind of record. The kind is how the workflow got the record, which is how it can be checked.

| Kind | A record is | Checked against |
|---|---|---|
| Database | a row a tool retrieved from a public resource, such as GTEx, the GWAS Catalog, ENCODE or Open Targets | the saved response |
| Model prediction | the output of a model, such as QBiC-SELEX or the Open Targets locus-to-gene score | the saved output |
| Literature | one experiment read from an article, with the sentence that states its result | the article's text |

What a language model remembers is never a record. It may propose a chain; every cell is filled from a source.

## Each cell is in one of six states

| State | Meaning |
|---|---|
| supports | at least one record of this kind supports the claim |
| disagrees | at least one record of this kind goes against the claim, and none supports it |
| both | records of this kind on both sides |
| nothing found | a source of this kind was asked and returned nothing that bears on the claim |
| not checked | a source of this kind exists and no answer for this claim is recorded |
| no source | the workflow has no source of this kind for this claim |

"Nothing found" and "not checked" are different findings and are never merged: missing data is not evidence against
a claim. A cell also lists the records that stand beside the claim without counting (the same experiment in another
cell type, an experiment that deletes the region and so compares no alleles, an expression level too low to call the
TF expressed) and the records set aside, each with the reason.

Every counted record keeps the kind of evidence it is: an edit or perturbation, an assay that compares the alleles,
an association, or a prediction. The size of an effect, a z-score, a ChIP signal or an expression level is never part
of a cell's state. A prediction that goes against a claim is shown as disagreeing and never lowers the claim.

## The rules a table must pass

1. **Shape.** Every chain has its four steps, each with both claims; every claim has three cells; every cell is in one of the six states.
2. **Records.** A cell that reports support or disagreement cites its records, and no other cell counts any. Each record is in the run's files, of the cell's kind, and from a source the map lists for that cell.
3. **This variant.** A record counted for a claim that the alleles differ names this variant.
4. **Looked.** "Nothing found" cites a lookup that completed. "No source" appears only where the map has no source, or says why this claim has none.
5. **Nothing left unjudged.** No record on file that names the claim's TF, element, gene or trait is left without a judgement: it is counted in the cell, listed beside it, or set aside with a reason.
6. **Quoted.** A literature record carries the passage it was read from and the article it came from.

## Which source fills which cell

| Claim | Database | Model prediction | Literature |
|---|---|---|---|
| TF binding: alleles differ | `adastra_asb` | `qbic_inventory`, `qbic_tf_detail` | articles |
| TF binding: in place | `chip_occupancy`, `tf_occupancy_set`, `tf_expression`, `tf_expression_set`, `depmap_context` | no source | articles |
| Regulatory activity: alleles differ | `adastra_asb`, `udacha_asa`, `mavedb_reporter` | no source | articles |
| Regulatory activity: in place | `ccre_overlap`, `screen_online`, `variant_annotation` | no source | articles |
| Target gene: alleles differ | `ccre_overlap`, `gtex_eqtl`, `protein_qtl_sets`, `credible_sets_l2g`, `credible_sets_all` | no source | articles |
| Target gene: in place | `ccre_overlap` | no source | articles |
| Trait: alleles differ | `gwas_associations`, `tumour_recurrence`, `civic_lookup`, `credible_sets_l2g`, `credible_sets_all` | no source | articles |
| Trait: in place | `depmap_context`, `credible_sets_l2g`, `credible_sets_all`, `gene_disease` | `credible_sets_l2g`, `credible_sets_all` | articles |

Eighteen of the 24 cells have a source today. A new source enters as an adapter and one row of this map (`SOURCES`
in `src/variant2mechanism/v9/table.py`); nothing else changes. A row says which of a tool's records it means, by
what a record names: a credible set names a trait and no gene, and its colocalisation with a gene's QTL names both.

A record counts once per fact it states:

- The variant's own eQTL fills "the alleles differ in the gene's RNA or protein" and not also "the element
  regulates the gene".
- A claim about a gene's RNA takes a colocalising expression or splicing QTL. A colocalising protein QTL is often
  a trans effect on a protein encoded elsewhere, so it only fills "the gene bears on the trait". A protein QTL
  counts for the gene itself only through `protein_qtl_sets`, below, and only when the protein is the gene's own.
- `adastra_asb` reads ADASTRA (release 6.1), which pools each protein's ChIP-seq experiments and calls whether
  the reads over a variant favour one allele. It gives one record per protein that passes ADASTRA's own 5% FDR,
  counted as a measurement in cells, like allele-specific ChIP read from an article. A protein that was tested and
  did not pass is listed and is no record, and a variant with no entry is "nothing found": ADASTRA can only call a
  variant in a cell that is heterozygous for it. Which claim a record fills depends on what the protein is
  (`v9/proteins.py`):
  - **A transcription factor** (on the Lambert 2018 census of human TFs, or with a QBiC-SELEX model): "the alleles
    differ in binding the TF", whatever ADASTRA's motif column says. An imbalance in a TF's reads does not show
    that the TF reads the variant (a neighbouring factor gives the same picture), so the record says when the TF's
    own motif does not agree. The motif column is not used as a filter: it is one motif scan, and it reports "no
    hit" for TFs whose QBiC-SELEX prediction favours the same allele as the reads.
  - **A protein that does not bind DNA itself** (BRD4, β-catenin): "the alleles differ in the regulatory activity
    of the site". Its reads show the state of the site and name no TF that reads the variant, so it enters no
    chain as a TF.

  The same sorting applies to allele-specific ChIP read from an article. Every record says that the call compares
  two haplotypes, so another variant inside the bound region could cause the imbalance.
- `gene_disease` reads Open Targets' evidence for a gene and a trait source by source. The GWAS credible sets that
  Open Targets assigns to the gene are left out, because they can be the very association under study; so are
  text-mined co-occurrence and drugs in development. A mouse knockout matched to the disease by phenotype
  similarity is filed as an inference, not as an experiment that measured the trait.

Four sources were added on 24 November 2026 (`v9/fill_sources.py`). Each is asked about the variant itself, and
each is run by a public institute, a consortium or the field's own repository:

- `udacha_asa` reads UDACHA, the chromatin-accessibility counterpart of ADASTRA: DNase-seq, ATAC-seq and FAIRE-seq
  reads over a variant in cells heterozygous for it, pooled per cell type. A record says that the state of the site
  differs between the alleles in that cell type. It names no protein, so it fills "the alleles differ in the
  regulatory activity of the site" and no TF's claim. One record per cell type and assay that passes 5% FDR, the
  level used for ADASTRA; UDACHA's own flag is set at 10%, and a call between the two is listed and is no record.
  A variant with no entry is "nothing found".
- `mavedb_reporter` reads MaveDB, where saturation-mutagenesis reporter assays are deposited. Such an assay
  measured every single-base change in an element, so a variant inside one has a measurement of its exact
  substitution. The variant is looked up by its ClinGen allele identifier. A record needs the set's own p-value
  below 1e-5 and at least ten barcodes, the significance level and the inclusion rule of the study that deposited
  these sets; a measurement that does not pass is listed and is no record. The record states no direction: the
  set's log2 effect is against the sequence the study mutagenised, which need not carry the reference allele.
  MaveDB holds about twenty well-known elements, so most variants have no measurement.
- `protein_qtl_sets` asks Open Targets for the credible sets of protein QTLs that hold the variant. Open Targets
  says of each whether the protein is encoded near the signal. A cis set states a claim of its own, "the two
  alleles differ in the level of the gene's protein", scoped to where the protein was measured (blood plasma for
  the most part), and makes that gene a candidate. The claim is left unassessed, as an eQTL in an unstated tissue
  is: plasma is not where the variant acts, so the record counts as an association and decides nothing about the
  order of tied chains. A trans set is listed and is no record.
- `tumour_recurrence` asks cBioPortal for the tumours of one cohort (MSK-IMPACT 2017, 10,945 tumours sequenced
  with a gene panel) that carry this exact substitution. One record per cancer type in which it was called in the
  tumours of at least two patients, with the counts. A count is not a test, and the record says so. The cohort is
  on GRCh37, so the variant needs a GRCh37 placement on file; an inherited variant returns nothing, which says
  nothing.

Protein names written with a Greek letter (AP-2α, C/EBPβ, PPARγ) now resolve to a gene. Articles name a protein
that way, the name was no gene symbol, and the record stayed under a TF no chain names. The HGNC table lists such
names as aliases; one resolves only when exactly one gene lists it. A bare family name (AP-2) is still not
resolved, because it names no single gene.

## What the table does not decide

- **The order of chains.** Chains are ordered by their weakest link, using the kind of evidence only
  (`v9/chain.py`). Chains that tie on every link are then ordered by two yes-or-no questions about the TF, which
  only break ties and remove nothing:
  1. **A strong prediction.** The QBiC-SELEX change is large for that TF group, and a ChIP-seq peak lies over the
     variant. "Large" means |z| of the group's strongest model is at or above the 90th percentile of the same
     value over a background of 21.8 million unlabelled variants (`qbic/background.py`). Each group has its own
     cut-off, because a group's value is the largest |z| among its models: the cut-off is 33.7 for the 81
     homeodomain models and has a median of 8.5 for a group of one model. The significance gate cannot do this
     job: the median model passes it at 36% of background variants.
  2. **A record of the TF in place.** A ChIP-seq peak over the variant, and expression in the stated context,
     never the size of the signal or the level.
  3. **A record that the TF acts on the gene** (since 25 November 2026, in runs read by the reader's format 6). A
     chain pairs a TF with a gene, and nothing above says that the two belong together. An experiment that
     changed a TF and saw another gene's RNA or protein change is flagged when it is filed, and the chain of
     that TF and that gene comes before an otherwise equal chain with no such record. Such a record comes from
     an article that names the variant, read by the reader, or from any article on that TF and gene, read by
     the joiner (below). It shows the TF acting on the gene somewhere, not that it does so through this
     variant, so it never moves a chain past one with stronger evidence. Not flagged: a measured null, a result
     the article calls unclear, a readout that is no gene product, and a "gene" that is the TF itself. Names are
     resolved to approved symbols when the record is filed, so the order can be read from a saved graph alone.
     A run with no such record is ordered exactly as before.

  A TF with no model, a prediction below its group's cut-off, or a TF never assayed by ChIP-seq stays in the list.
  The table changes no order.
- **Claims that are not a step.** A TF said to regulate a gene, or a claim about another variant, is listed beside
  the table.

## Filling the table by code alone

```bash
v2m v9 fill --variant chr1:109274968:G>T --origin germline --out <a new folder>
```

No model is called. Code collects what its sources hold at the variant, states a claim for everything a record can
count for, and links every record through the claim graph's gates (`v9/fill.py`):

| Claim | Code states it for |
|---|---|
| TF binding: alleles differ | every group of TFs with a QBiC-SELEX prediction past the gate; every TF with an allele-specific binding call in ADASTRA |
| TF binding: in place | a TF of such a group with a ChIP-seq peak over the variant; with a context in the request, a TF expressed in it |
| Regulatory activity: alleles differ | the variant's site, where ADASTRA holds allele-specific reads of a protein that does not bind DNA itself, UDACHA holds allele-specific reads of open chromatin, or MaveDB holds a reporter assay that measured this substitution |
| Regulatory activity: in place | the element a registry places the variant in |
| Target gene: alleles differ | every gene with an eQTL of this variant, or a colocalising expression or splicing QTL; every gene whose own protein has a QTL with this variant in its credible set |
| Target gene: in place | a gene that changed when the variant's element was perturbed |
| Trait: alleles differ | every trait term with an association or a credible set of this variant; for a somatic mutation, every cancer type in which it was called in the tumours of two patients or more |
| Trait: in place | a candidate gene with a record linking it to such a trait |

- Three database sources compare the two alleles' regulatory activity: ADASTRA's reads of a protein that does not
  bind DNA itself, UDACHA's reads of open chromatin, and a reporter assay in MaveDB that measured the
  substitution. Where a variant has such a record, code states the claim for the variant's site; elsewhere the
  cell reads "nothing found".
- A claim that the alleles differ states no direction. The records say which allele, so a measurement in the other
  direction is still a record that they differ.
- Expression counts as "expressed" at 1 TPM or more, the usual convention for a detected transcript. A lower
  level is listed beside the claim and is evidence of nothing. Without a context in the request, expression is not
  looked up.
- A chain with a predicted link is still an answer. The result says which links are measured, associated, predicted
  or empty.

The run folder holds the bundle, the reports and the table (`table.json`, `table.md`). A table filled this way
passes every rule above: each record is counted, listed beside a claim or set aside with the graph's reason.

## Filling the literature column: the reader

```bash
v2m v9 fill --variant chr1:109274968:G>T --origin germline --read --out <a new folder>
```

`--read` adds one model role, the reader (`v9/reader.py`), and it is the only model call of the run. Every other
stage is code, so each can be counted and replayed:

| Stage | Who | What happens |
|---|---|---|
| Find | code | Europe PMC is searched for the variant's rsIDs: once in titles and abstracts, once anywhere together with an assay word. LitVar is asked for the articles that name the variant under any spelling, together with an assay word |
| Choose | code | reviews are left out; an article whose retrieved text does not name the variant is not sent to the model; the passages shown are the abstract, those that name the variant and, for an article about it, its results, up to 30,000 characters |
| Read | model | one reading per article, each article once: the model returns the experiments the article reports, each with the family of its assay |
| File | code | code copies the sentences the model pointed to and checks every field against the text; what passes is a record |
| Link | code | code decides which claims a record bears on, through the claim graph's gates |

- **The model points, code quotes.** Each passage is shown with a location id and numbered sentences. An experiment
  names a location and a run of at most four sentences (600 characters), and code copies that stretch. A quotation
  is the article's own text by construction. A reply that points to a longer stretch, or outside what was shown,
  is sent back once with the numbers; what still breaks a limit is refused. Nothing else is sent back, so a model
  cannot bend a record until it passes.
- **The model names the family of each assay, and code's own reading decides wherever it has one.** The families
  are a binding assay, a reporter, ChIP, a perturbation, allele-specific expression, or other. Where code
  recognises the assay in the description (EMSA, luciferase, ChIP, CRISPR, a knockdown), that is the class kept.
  The model's label fills only what code cannot read ("allele editing", "immunoprecipitation followed by allele
  quantification"), and the record says so.
- **Two yes-or-no answers only the reader can give, each of which can only take a record out of the count.**
  Whether what was compared differs at more variants than this one (risk and non-risk haplotype constructs): then
  only allele-specific expression, an association, may count for a claim about this variant's alleles. And whether
  the article itself calls the difference not significant, a trend or inconsistent: it then counts for nothing.
  A record whose description says the article names no assay is refused: it is a statement, not an experiment.
- **Every article the three searches list is read** (up to 30). A reading costs about a sixth of a cent.
- **Articles that write the variant another way.** A search for an rsID lists only articles that write the rsID,
  and a somatic promoter mutation is mostly written by an HGVS name or a shorthand. LitVar normalises the
  spellings to one entry, and the reader asks PubTator, the text-mining service LitVar is built on, for that
  entry's articles in its relevance order (the first ten). An article only LitVar listed is read with the spellings
  it uses: code asks PubTator how that article writes the variant, chooses the passages by those spellings too,
  and tells the model what they are. An article Europe PMC listed is read exactly as before.
- **An article's own name for a mutation counts under two checks.** A record names its variant by an rsID, by a
  position, or by a shorthand that the article or a catalogue ties to a position. Articles on a somatic mutation
  write none of these: 16 experiments on TERT C228T were refused because the article writes "−124C>T". In an
  article only LitVar listed, a record may now name the variant as the article does, where the quotation or its
  paragraph, heading or caption writes that name. It counts as the variant when both checks pass, and code makes
  both: PubTator ties that name to the variant's rsID in that same article, and the base change the name writes
  is the variant's, reference to alternate, on one strand or the other ("−124C>T" is G>A on the forward strand).
  The record's allele is placed on the forward strand, and the experiment record keeps the article's notation.
  Not taken: a variant whose alleles are each other's complements (A/T, C/G), since the change reads the same on
  both strands; a name that is not written where the result is, even when the article names no other variant; an
  allele that is not a base of the name; a record that also names another variant. Text mining can tie a name to
  the wrong variant, and one wrong single-base change in six would pass the second check, so the table prints
  with each such record that it was identified by name, and whether the name stands in the quotation.
- **The model reads without knowing what the run hopes to find.** The request holds the variant and the article and
  nothing else: no claim, no candidate TF or gene. One article and one variant always give one request, so a reply
  is the same in every run and replays from the response cache.
- **Code decides what an experiment bears on**, by what it manipulated and what it read out:

| Experiment | Claim it can count for |
|---|---|
| alleles compared in a binding assay, or allele-specific ChIP reads of a TF | TF binding: alleles differ |
| allele-specific ChIP reads of a protein that does not bind DNA itself | Regulatory activity: alleles differ |
| ChIP at the variant's site | TF binding: in place |
| alleles compared in a reporter, or an allele edit read out as activity | Regulatory activity: alleles differ |
| an allele edit read out as a gene's RNA | Target gene: alleles differ |
| the two alleles' transcripts compared in heterozygous cells (allele-specific expression) | Target gene: alleles differ, as an association |
| the element perturbed, a gene's RNA read out | Target gene: in place |
| an allele edit read out as a trait | Trait: alleles differ |
| the gene perturbed, a trait read out | Trait: in place |

- Only an experiment that compares the alleles counts for a claim that they differ. ChIP at the site, or the region
  tested in a reporter as one construct, shows that the TF or the activity is there: it is set aside for the claim
  that the alleles differ, with that reason.
- An edit the record gives as an exchange of alleles is taken as one, unless its description or its quotation
  speaks of a cut, an indel, a deletion or a disruption: that perturbs the site, whatever the record calls it, so
  it is judged as a test of the element. The reader is told to file a cut as a change to the element; this rule
  catches the ones it does not.
- Allele-specific expression counts as an association, like an eQTL of the variant: the transcripts of the two
  alleles in the same cells compare the two haplotypes, not this variant alone.
- An article's name for a TF or gene that today names one gene and once named another states nothing about
  either. TCF4 was the symbol of TCF7L2 and TCF3 that of TCF7L1, so "TCF4" in a paper on Wnt signalling is not
  today's TCF4. The HGNC table lists 229 such names (pseudogenes aside); code cannot tell which gene an article
  means, so the record is set aside with that reason.
- A quotation that cites earlier work ("as previously described", "et al.") is still the article's own result
  when it points to one of the article's figures or tables; without such a pointer it is filed as a retelling,
  which counts for nothing.
- A claim is stated for an experiment only if the graph accepts the link. A TF knockdown offered as a test of an
  element, or an assay of a neighbouring variant, states nothing and is listed as set aside with the reason.
- A measured null counts against a claim only in the claim's exact scope. Elsewhere it is listed beside the claim,
  and no claim is stated for a null alone.
- A literature cell reads "nothing found" on the strength of the articles that were read. Its note says how many
  of those found that was, and how many experiments the model returned that did not pass code's checks: those are
  counted nowhere, so the note keeps "nothing found" from hiding one. A search that did not complete, an article
  that could not be retrieved and a reply that failed leave the cell "not checked".
- What code cannot name it does not find: an article that calls the variant by a shorthand only (a promoter
  mutation known by its position in an older assembly) is not listed by a search for its rsID.

`scripts/v9_fill_suite.py --read --budget-usd <cap>` runs the suite with the reader, and
`scripts/v9_chain_table.py` then reports what became of every article found: read, not naming the variant, a review,
not retrievable, failed, or beyond the cap, with the experiments returned and filed.

## A second reading: the critic

```bash
v2m v9 fill --variant chr1:109274968:G>T --origin germline --read --critic --out <a new folder>
```

`--critic` adds a second model role (`v9/critic.py`). The reader is one model reading an article once, and code's
checks on what it returns are checks of form: the quotation is the article's own text, the TF is named in the
paragraph, the assay is of a known family. Whether the quoted sentences show what a claim states is a judgement
code cannot make. The critic is a second, independent reading of exactly that.

| Stage | Who | What happens |
|---|---|---|
| Choose | code | before any experiment is linked, code works out which experiments stand alone: the only one counted for, or the only one counted against, some claim. Only those are sent |
| Ask | code | for each, code lists the claims it counts the experiment for or against, each as one sentence |
| Check | model | one call per experiment: a second model, from another provider than the reader's, is shown the variant, the paragraph as numbered sentences with the quotation marked, the paragraphs on either side as context, and those claims. It answers for each: shown, not shown (with a fault from a fixed list) or cannot tell. With "shown" it may name further sentences of the paragraph as the ones that state the result |
| Act | code | a claim answered "not shown" does not get the record, which is listed as set aside with the critic's reason. Sentences the critic names are copied by code, and the table quotes them with the record. Every other answer, and no answer, leaves the record where code put it |

What follows from that design:

- Only an answer that can change a cell is paid for. Taking the one record out of a cell changes the cell;
  taking out one of several changes nothing. In the first run, which read every record, 15 of the 58 counted
  records stood alone, and the one cell that changed was one of those. When an answer takes a record out of a
  claim and so leaves another record alone there, that one is read too. The run reports how many records were
  alone and not read; it should be none.
- The critic can take a record out of the count, or point to where its result stands. No answer of its adds a
  record, a claim or a link, so a critic that errs on the lenient side leaves the table exactly as the reader and
  code made it.
- The model points, code quotes, as with the reader. When a quotation stops a sentence short of the result, the
  critic names the sentences by number and code copies that stretch of the paragraph, within the reader's own
  limits (four consecutive sentences, 600 characters). The record in the run's files keeps the reader's quotation;
  the table shows the longer one for that claim and says so beside it. A result stated only in a neighbouring
  paragraph does not count and cannot be named.
- It sees the article's text and the claims, and nothing of the reader's reading: no field of the experiment, no
  direction, no note. It judges the text, not the first model's account of it.
- A claim that would have been stated for that one record alone is not stated, so the answer never holds a claim
  with nothing behind it.
- "Cannot tell" and "no answer" (a failed call, a provider refusal, a record beyond the cap) leave the record
  counted, and the report says so beside its quotation. Nothing is asked twice.
- The critic's model is set in `config.yaml` (`v9.critic`) apart from the reader's, and comes from another
  provider: two readings by one model share its blind spots. A packet depends on the record and its claims only,
  so a saved run replays from the response cache.
- The faults it may name: the result is about another factor, gene, region or trait; what was compared is not the
  two alleles of this variant alone; the article reports no clear result of the kind the record was counted as;
  the sentence states a finding with no experiment behind it; the result is retold or a hypothesis.

`scripts/v9_critic_check.py` runs the critic over the records a saved run counts, without changing the run. It is
how the critic is developed (on variants outside the evaluated cases) and tested: `--alone` keeps the records a
fill would send; `--decoys` adds claims whose TF or gene the paragraph never names, which a critic that reads the
text must answer "not shown"; `--audit` scores its answers against an audit of one run's records (`eval/critic_audit_20261117.json`: 5 of 44 counted records
were wrong). The instructions were written by someone who knew those five errors, so that test says whether the
critic applies the rule, not whether it would find a new kind of error.

What those checks found on 22 November 2026, with Claude Sonnet 5.5 at low effort (101 paid calls, 50 cents):

| Check | What was read | What the critic did |
|---|---|---|
| Variants outside the evaluated cases, with decoys (`runs/critic_dev_20261122_b`) | 31 counted records: 34 claims, and 25 decoy claims | "Not shown" for all 25 decoys, "shown" for all 34 real claims. For 6 claims it named further sentences as the ones that state the result. Three of those are records its first version had rejected because the quotation stopped short of the result |
| The audited run (`runs/critic_test_20261122_b`) | 44 counted records, 5 of them wrong by the audit | It took out 4 of the 5 and none of the other 39. The fifth quoted a comparison of two haplotypes; the critic kept it and quoted the two later sentences of the same paragraph, which report constructs that differ at the one variant |
| The evaluated cases, inside the fill (`runs/fill_reader_critic_v2_20261122`) | 60 counted records, 20 of them alone behind a claim | It read the 20: 29 of 30 claims shown, one "cannot tell", none taken out, no quotation extended. No cell differs from the run without a critic |

So with today's reader the critic changes nothing in the tables of the evaluated cases. What it adds there is a second
reading on file beside each record that carries a cell alone. On records from the older reader it removes the known
errors and repairs quotations that stop short.

The critic's instructions are the same text in every call, and most of what a call sends. They go to the provider's
prompt cache (`agent/anthropic_api.py`), which brings a call from about one cent to about half a cent.

## Reading a tie: the judge

```bash
v2m v9 fill --variant chr3:12344838:C>T --origin germline --read --judge --out <a new folder>
```

Chains are ordered by the kinds of evidence behind their claims, and many variants end with several chains tied
for first: the same kinds of record stand behind every claim of each. `--judge` adds a model role for that case
only (`v9/judge.py`).

A cell counts an experiment only for the claim it tests, and some experiments test no single claim. An article on
rs4684847 reports that "PRRX1 silencing was sufficient to revert the risk allelic suppression" of PPARG2: a TF is
removed and the difference between the alleles goes away. The record names one of the tied TFs and is on file with
its quotation, yet no cell may count it, because an experiment that changes a TF does not compare the alleles'
binding. Whether such an experiment ties a TF or a gene to this variant's site is a reading of its text, which code
cannot do.

| Stage | Who | What happens |
|---|---|---|
| Find | code | the chains that share the first rank, and what they differ in: a TF (or a group of TFs that share a binding model), a target gene, or both. Each one is a candidate |
| Gather | code | for each candidate, the experiments read from articles that name it, less those counted for or against one of its own claims. A candidate with none is not asked about, and a tie with none makes no call |
| Read | model | one packet for the tie: the variant, the candidates, and each paragraph once, as numbered sentences, with the records that rest on it. The second model answers for each candidate: shown (an experiment ties it to the site, and the basis says whether the alleles were compared), against (such an experiment changed nothing), not shown or cannot tell. With shown or against it names the records, and the sentences that state the result when a quotation stops short |
| Repeat | code | every packet also lists one made-up candidate, a TF or gene that no paragraph names, under the first candidate's records. The packet is sent twice: the real candidates first and the made-up one last, then the made-up one first and the real ones in the opposite order. An answer is kept only when both readings give it, and nothing is kept from a tie in which a reading ties the made-up candidate to the site |
| Write | code | the answers go under the tie, in the run's answer and in its report, each with the quotations it rests on, which code copied |

What follows from that design:

- It changes nothing that counts. The cells, the ranks and the number of tied chains stay as code made them. A
  judge that errs changes one sentence under the tie and the quotations beside it.
- Each candidate is judged on its own records. The instructions forbid ranking the candidates and weighing effect
  sizes, p-values or the number of records, and code reads each answer as a yes or a no. A candidate nobody has
  studied has no records and loses nothing: it stays tied.
- It is asked twice because a model that is shown a list tends to favour what comes first: in development the
  candidate listed first was twice given a "shown" its records did not bear out. A candidate the two readings
  disagree on is reported as such, and nothing is said to point to it. The made-up candidate gives every real one a
  second position to be read in, even when a tie has only one, and it is a check on each reading: a model that
  accepts it has not read the names.
- The reply gives the reason before the answer. Asked for the answer first, the model once answered "shown" and
  then wrote a reason that said the opposite.
- A sentence pointer that code cannot copy costs only the pointer: the answer is kept with the record's own
  quotation.
- Records and candidates are numbered inside the packet, so a request does not depend on how a run numbered its
  evidence, and a saved run replays from the response cache.
- It sees the articles' text and nothing of the reader's reading.
- The judge runs on the second model (`v9.critic` in `config.yaml`), on a client of its own. A failed call, a
  refusal or a reply the cache cannot give back leaves the tie as it was, and the run says so.

`scripts/v9_judge_check.py` runs the judge over the ties of saved runs, without changing them: the judge changes
no cell, so what it would say inside a fill can be had from the saved run. `--decoys` reads each tie once more
with every real candidate renamed to a TF or gene no paragraph names; a judge that reads the text ties none of
those to the site. The instructions were developed on variants outside the evaluated cases.

What the paid checks found on 22 November 2026, with Claude Sonnet 5.5 at low effort (43 paid calls, 35 cents,
31 of them spent in development):

| Set | Ties for first | With experiments to read | Points to | Points away from | Not shown | Undecided | Made-up candidate turned down |
|---|---|---|---|---|---|---|---|
| 8 variants outside the evaluated cases, final protocol (`runs/judge_dev_20261122_e`) | 4 | 3 ties, 5 candidates | PRRX1 at rs4684847, KITLG at rs12821256 | none | PPARG at rs4684847 | at rs9349379, PHACTR1 (the two readings disagreed) and TBC1D7 (cannot tell) | 6 of 6 readings |
| The 15 evaluated cases, run once (`runs/judge_15_20261122`) | 10 | 4 ties, 4 candidates | the C/EBP group at rs12740374 | none | TOX3 at rs4784227, the LEF1 and TCF7 group at rs6983267 | IRF6 at rs642961 (cannot tell) | 8 of 8 readings |

On the 15 all four answers were the same in both orders. At rs12740374 twelve TF groups tie, and the judge points
to one of them from two sentences of one article: a dominant negative C/EBP "significantly reduced differences in
haplotype-specific expression", and adding C/EBPα "restored the haplotype-specific effect". Those experiments
compared haplotypes, and the judge's reason says so.

Development changed the protocol four times before it was frozen, each time for a fault a run had shown:

- A decoy run found the judge accepting a renamed candidate while noting that the article names another factor: it
  trusted code's list of which record names which candidate. The instructions now tell it to find the candidate in
  the paragraph itself, and to use only the candidate's own paragraphs. After that 5 of 5 decoys were turned down.
- The candidate listed first was twice given a "shown" its records did not bear out, and the two-order rule dropped
  both. A tie with one candidate had no such protection, which is why every packet now carries a made-up one.
- One answer said "shown" beside a reason that said the opposite, in both orders, so the rule did not catch it.
  The reply now gives the reason first.
- A pointer to more sentences than code may copy made a whole reading fail. It now costs only the pointer.

What the judge still misses, as development showed. It reads a paragraph without its neighbours, so a result whose
comparison is described in the paragraph before can look undecided (PHACTR1: one reading said "cannot tell", the
other "against"). A gene named by an isoform is not matched to its gene (the PPARG2 experiments are not PPARG's
records). Both errors lose an answer; neither puts a wrong one under a tie.

## Under the table: the numbers and the gaps

The report shows two more things under the first chain's table (`v9/report.py`). Both are display only: they were
added after the scoring, and they change no cell, no rank and no saved run.

**The numbers behind the cells.** One row for each source behind each cell, with what it returned: the FDR and the
number of experiments of an allele-specific binding call, the z and p of a QBiC-SELEX prediction and whether it is
in the top 10% for its TF group, the effect size and p of an eQTL, the fine-mapping probability of a credible set,
the probability of a shared causal variant of a colocalisation, a locus-to-gene score.

- Code copies every number from the saved record. No model types one.
- Several records of one source give the lowest and the highest value. A range says what is on file without picking
  a best record.
- The numbers are shown and never ranked on. A chain's place rests on the kind of evidence under each claim.
- A literature row gives the number of experiments and articles. The sentences stay in the quotations.

**What would fill the gaps.** For each claim of the first chain that no measurement supports, the kind of record
that would, taken from the table's own rule for which record counts for which claim.

| Claim | Suggested when | What is suggested |
|---|---|---|
| TF binding: alleles differ | no measurement | a binding assay with both alleles, or ChIP reads counted by allele |
| TF binding: in place | nothing | ChIP for the TF; a cell context for the run, so that expression is looked up |
| Regulatory activity: alleles differ | no measurement | a reporter assay with both alleles, or an allele edit read out as activity; a model run, once a model predicts activity |
| Regulatory activity: in place | nothing | an accessibility or histone-mark assay at the site |
| Target gene: alleles differ | no measurement | an allele edit read out as RNA |
| Target gene: in place | nothing | the element silenced or deleted, the gene's RNA read out |
| Trait: alleles differ | nothing | an association; for a somatic mutation, a source of recurrence in tumours, which is not connected yet |
| Trait: in place | nothing or a prediction | the gene perturbed, the trait or a cell behaviour read out |

- Code writes each suggestion, with the names the run has on file: the TF, the alleles, the element, the gene, and
  the cell lines where a ChIP-seq peak lies over the variant. No model writes one, and nothing suggested is run.
- A tie for first comes first, with what would separate it. Then the weakest claims: those with nothing, then those
  with a prediction, then those with an association.
- When chains tie, a suggestion names every tied TF or gene, never the first chain's alone.

## Going back for evidence: the loop

The fill looks everything up once. `v2m v9 fill --read --loop model` adds a loop that goes back for articles where
the leading chains tie or are weakest (`v9/loop.py`). It was added on 25 November 2026, after the scoring. It has
been tested with scripted models, dry-run on 23 variants, and run with a model on 8 variants outside the test set
([`report.md`](report.md) has those runs). Eight variants are too few to measure it.

| Stage | Who | What happens |
|---|---|---|
| Gaps | code | Reads them from the table: a tie for first, a TF and a gene of the first chains that nothing joins, then the first chain's claims that nothing supports, that are predicted only, that are associated only |
| Menu | code | Lists what could be done about them this round, each entry with the searches it would run |
| Plan | planner model, or code | Picks menu entries (at most 4), each with a reason. In the baseline arm code takes the menu in its own order |
| Act | code, the reader and the joiner | Runs the searches. The reader reads the new articles exactly as it read the first ones; the joiner reads the articles found for a TF and a gene |
| Look | code | Builds the table again without keeping it, and sees which cells and ranks changed |
| Stop | code | After 3 rounds, when a round changes nothing, when the menu is empty, or when reading has to stop |

- **Where it sits.** Between the first reading and the linking of what was read. A round only adds articles and the
  records filed from them. The table that is kept is built once, afterwards, by the same code as without a loop,
  so it is the table a single pass over the same articles would give. A test checks exactly that.
- **What is on the menu.** Each action is a search and a reading.

| Action | For which gap | What it searches |
|---|---|---|
| `candidates` | a tie | the variant's names with each tied TF or gene and an assay word, the same search for each |
| `join` | a TF and gene that nothing joins | the TF and the gene in a title or abstract with a word for a perturbation; the variant is not part of it |
| `named` | a weak claim that names a TF or a gene | the variant's names with that name and an assay word |
| `other_names` | any | the variant under names that are not rsIDs and write its own base change: text-mined spellings, a catalogue's aliases, names the planner proposed |
| `follow` | any | nothing: it opens the reviews on file and takes the articles they cite in the paragraphs that name the variant |
| `proposed` | any | the variant's names with a TF or gene the planner remembers, and an assay word |

- **The variant's names in a search** are its rsIDs, the spellings text mining found in the articles read, and the
  aliases a catalogue verified by position. A name from the planner's memory is searched under `other_names` only.
  A gene that has no symbol is named by a database id, which no article writes, so it is not searched for.
- **Reading what a search finds.** An article the loop found may never write the rsID. Its passages are chosen by
  the rsID, by the spellings text mining ties to the variant in that article, and by the catalogue's names, and
  the model is told the last two. Whether a record filed under such a name is the variant is still decided by
  the identity rules: the catalogue's verified shorthand, or the two checks on a text-mined name. An article of
  the first reading is read exactly as before.

- **What the planner may do.** It sees the table, the gaps, the menu and what earlier rounds did, and no article
  text. It returns menu numbers. It may also propose up to 3 names from memory: a TF, a gene, or another name of
  the variant. A proposal is a search term and nothing else. A TF or gene must be an approved symbol, another name
  must write the variant's own base change, and each is marked "from memory" wherever it is shown. A remembered
  answer with no article behind it leaves no trace in the table, which a test checks.
- **What keeps it honest.**
  - The reader stays blind. Its request holds the article and the variant, never the gap, the candidate or the
    search that found the article. A test compares the request with the one a run without the loop sends.
  - Equal effort. A tie is one action over every tied candidate, and the new articles are read in turn, one
    candidate after another, so the cap on a round cuts every candidate alike. A tie of more than 24 candidates
    is searched for none of them, and so are more than 24 pairs of TF and gene: a random variant ties hundreds of
    TFs on a prediction alone, and a search for the first of them only would favour it.
  - Effort is reported. For every search the report gives how many articles it listed, how many were new, how
    many were read, how many experiments were filed and how many of those count for a claim.
  - Nothing is removed. A record against a claim is filed and shown as before.
- **The joiner** (`v9/joiner.py`) is the one role that reads articles which never name the variant: a TF acts on a
  gene whatever variant one asks about. For every pair of TF and gene in the first chains it searches the same way,
  keeps the passages that name both, and has a model return the experiments in which the TF was changed and the
  gene's RNA or protein measured. The model is told the pair, since it must know what to look for. It returns
  pointers to sentences, and code copies them and checks every field as it does for the reader. A result that
  found no change is filed as a null and joins nothing. An article listed for two pairs is read for each.
- **A join follows the literature's attention.** A well-studied TF has more such articles than an obscure one.
  The report lists, for every pair, how many articles were listed and read.
- **Caps.** 3 rounds, 10 new articles a round for the reader and 6 for the joiner, 5 articles a search (3 for a
  pair), 4 reviews a round and 5 citations a review, and at most 24 tied candidates and 24 pairs, each searched
  for all or for none.
- **A dry run** (`--loop-dry`) plans the first round, runs its searches and reads nothing. No model is sent
  anything, so it costs nothing and shows what a round would read.
- **Not built yet.** Reading on in a paragraph when a record was cut short, widening a lookup to more tissues, and
  any action that costs more than a reading (a model run, a cluster job). An article found under a name from the
  planner's memory is read only if it also writes the rsID, a text-mined spelling or a catalogue's name. A
  catalogue's name in HGVS form ("-146C>T") is searched for and passages are chosen by it, but a record that names
  the variant only that way is still refused: of a catalogue's names only the shorthand ("C250T") identifies it.
- **What it cannot show.** On a well-known variant the planner remembers the answer and then finds its papers.
  Such a variant shows that evidence is found and filed correctly. It does not show discovery.

## Scored once against the gold cases

The pipeline was frozen on 23 November 2026 and its 15 tables were scored once. The freeze is the hash of every
file a run executes and of the 15 tables (`eval/fill_freeze_20261123.json`; `scripts/v9_freeze.py check` lists
anything that has changed since). The sources added on 24 November changed those files, so the check now lists
them: the score below is of the frozen version, and the additions are not scored. The scoring rule was written before any table was scored and is the docstring of
`scripts/v9_table_score.py`. The output is `runs/score_fill_20261123`.

```bash
python scripts/v9_table_score.py --runs runs/fill_reader_critic_judge_20261122_b --out <a new folder> \
    --freeze eval/fill_freeze_20261123.json
```

A case's answer is the set of chains tied for first. Names are matched by the gold specification's own rules.
Every component has two numbers. "Named" counts a case when a first-ranked chain names the gold answer. "Share" is
the matching candidates over the candidates in the tie, summed over cases: what drawing one candidate from each tie
would get. Both are given again with the judge's answers applied. Direction and context are not scored, and the six
controls get no score.

| Component | Cases it applies to | Named | Share | Named, with the judge | Share, with the judge |
|---|---|---|---|---|---|
| TF, as the member | 9 | 0 | 0.00 | 0 | 0.00 |
| TF, as its group | 8 | 7 | 3.95 | 7 | 4.86 |
| TF, as its family | 8 | 7 | 4.28 | 7 | 4.86 |
| Target gene | 9 | 6 | 4.58 | 6 | 4.58 |
| TF group and gene in one chain | 9 | 4 | 2.25 | 4 | 3.17 |
| Trait | 9 | 7 | 7.00 | 7 | 7.00 |

Two of the nine (rs12740374 and TERT C228T) were used while the earlier engine was built. Without them the judge
changes no number:

| Component | Cases it applies to | Named | Share |
|---|---|---|---|
| TF, as the member | 7 | 0 | 0.00 |
| TF, as its group | 6 | 5 | 3.36 |
| TF, as its family | 6 | 5 | 3.36 |
| Target gene | 7 | 5 | 3.58 |
| TF group and gene in one chain | 7 | 3 | 2.17 |
| Trait | 7 | 6 | 6.00 |

Case by case ("4 of 8": four of the eight tied candidates match):

| Case | Chains tied for first | TF, as its group | Target gene | Both in one chain | Trait |
|---|---|---|---|---|---|
| TERT C228T | 8 | 4 of 8 | 0 of 1 | 0 of 8 | no |
| TERT C250T | 11 | 4 of 11 | 0 of 1 | 0 of 11 | no |
| rs6983267 | 2 | 1 of 2 | 0 of 1 | 0 of 2 | yes |
| rs4784227 | 6 | 1 of 2 | 1 of 3 | 1 of 6 | yes |
| rs339331 | 1 | 1 of 1 | 1 of 1 | 1 of 1 | yes |
| rs2168101 | 1 | 1 of 1 | 1 of 1 | 1 of 1 | yes |
| rs12740374 | 12 | 1 of 12; with the judge 1 of 1 | 1 of 1 | 1 of 12; with the judge 1 of 1 | yes |
| rs1421085 | 12 | does not apply | 1 of 1 | 0 of 12 | yes |
| rs642961 | 4 | 0 of 1 | 1 of 4 | 0 of 4 | yes |

What the numbers say:

- Two cases have one leading chain (rs339331, rs2168101), and in both it names the gold TF group, gene and trait.
  Both have a paper with allele-level experiments that is indexed under the rsID.
- The gold TF's group is in the leading tie in 7 of 8 cases, usually beside others: 3.95 of 8 by share.
- The gold TF itself is never named. TFs that share a QBiC-SELEX model are one candidate, and an experiment that
  names one member is filed under the group.
- The judge adds 0.92 to two rows, all of it at rs12740374, a case the earlier engine was built on. On the seven
  others it read three ties, pointed to nothing and changed nothing.
- The trait number is generous. A chain lists every trait a source ties to the variant, and one match counts.

Why each miss happened, read from the saved tables after the scoring:

- **TERT promoter, both cases.** The literature search uses the rsID alone (rs1242535815, rs1561215364). The
  papers on these mutations call them C228T and C250T, so the search found four articles for one case (three on
  circulating tumour DNA and an annotation database; no experiment passed code's checks) and none for the other. No
  database the fill asks holds a somatic mutation, so no chain names a gene or a trait. The first chain has 3 of 8
  claims with support, as a control has.
- **MYC at rs6983267.** No record of any kind says the alleles differ in MYC. One article reports that CCAT2, a
  transcript that contains the variant, is expressed more from the G allele (PMID 23796952), so the leading chains
  name CCAT2. The first chain that names MYC is at rank 1,045.
- **AP-2α at rs642961.** The reader filed the article's mobility-shift experiment under the name the article uses,
  "AP-2α" (PMID 18836445). Nothing maps that name to TFAP2A, so the experiment and the QBiC-SELEX prediction for
  the AP-2 group sit on two candidates. The article's name leads, the group is at rank 6, and the rule counts a
  miss at every TF level.
- **ARID5B at rs1421085.** No QBiC-SELEX model covers it and no filed record names it.

Counts that need no label, for all 15:

| Set | Cases | Claims of the first chain with support, mean of 8 | Cases whose first chain has a measured allele claim |
|---|---|---|---|
| Gold | 9 | 5.9 | 7 |
| Near-miss controls | 3 | 4.7 | 1 |
| Random controls | 3 | 1.7 | 0 |

A measured allele claim rests on an assay or an edit, not only on an association or a prediction. It separates the
sets better than the count of supported claims does. The two gold cases without one are the TERT cases. The one
control with one is rs56007086, which lies in the same element as rs4784227: ADASTRA records ChIP-seq reads of ESR1
that favour one allele there (FDR 0.0006). That is a measurement and not an error, and the chain stops at it: no
gene and no trait are named.

Against the earlier engine, which was frozen and run once on the same 15 on 14 November. Its evaluator scored the
hypotheses each run stood behind: TF group 2 of 8, target gene 6 of 9, trait 0 of 9, and three gold cases ended
with no supported explanation. A hand count of its first-ranked chains, ties counted and never scripted, gave the
TF or its group in 7 of 9, the gene in 8 of 9 and both in 6 of 9. By "named" the fill gives 7 of 9, 6 of 9 and
4 of 9. So the fill names no more gold answers than the engine's chains did, and two genes fewer: the engine let a
model propose TERT from memory, and the fill names only what a source names. What the fill adds is the evidence
under each claim, which the labels do not measure.

What this test is and is not:

- It is not blind. The gold answers were known while the pipeline was designed, and TERT C250T, which counts among
  the seven, has the same promoter, TF and gene as TERT C228T.
- The gold specification is unreviewed, so every number is provisional.
- Nine cases: one case is 11 points. No statistical claim is made.
- From here the 15 are development data for anything changed because of these results. A new test needs variants
  that nobody here has looked at.

## Reading a run of the claim-graph engine

The engine's chain view has five links; with its location and factor-context claims they are the eight claims:

| Table claim | In the chain view | Graph relations |
|---|---|---|
| TF binding: alleles differ | TF binding link | `alters_binding` |
| TF binding: in place | context of the factor | `occupies`, `expressed_in` |
| Regulatory activity: alleles differ | regulatory activity link | `alters_regulatory_activity` |
| Regulatory activity: in place | location | `overlaps` |
| Target gene: alleles differ | target gene link | `associated_with_expression`, `alters_rna` |
| Target gene: in place | target gene link | `regulates` (element to gene) |
| Trait: alleles differ | variant to trait link | `associated_with_trait`, `causal_at_locus`; `contributes_to_trait` and `affects_process` said of the variant |
| Trait: in place | gene to trait link | `contributes_to_trait`, `affects_process` said of a gene |

`scripts/v9_chain_table.py` reads saved runs into tables, checks them and writes the counts:

```bash
python scripts/v9_chain_table.py --runs <a folder of saved runs> --out <a new folder>
```

It reads the saved graphs only: no model call, no network and no gold label. A cell holds the records the graph's
gates accepted as links, and for the binding claim the QBiC-SELEX inventory's items for the factor. A record the run
retrieved and never judged for a claim is counted as unjudged, never attached.
