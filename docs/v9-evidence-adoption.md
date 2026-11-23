# Evidence adoption and ordinary branching in v9

The investigation can now revise its candidate mechanisms when an experiment concerns an entity outside the
current hypotheses. It does not need to reject every existing hypothesis before adding an alternative. An accepted
observation also remains visible until a claim represents it or the coordinator explicitly defers it or sets it aside.

## What changed

1. **Observations persist across planning rounds.** Previously, an unlinked result could disappear from a later
   planning packet once it was no longer new. `adoption.py` derives a review list from the graph and its event log.
   Planning, audit and final-comparison packets now include unresolved observations, including their source evidence.
   Investigator-created claims outside any hypothesis are shown to the planner when they link to these observations.
2. **A plan can add a hypothesis.** `new_hypotheses` contains a normal sketch plus `basis_evidence_ids`. At least one
   basis item must be linked to a new or reused claim with a non-context stance. The existing graph gates still check
   whether each link is valid. New hypotheses have origin `evidence_led`; their proposal event records their basis.
   A new claim can be investigated in the same plan using its temporary key.
3. **A summary change does not count as adopting evidence.** A `represented` decision requires an accepted
   non-context link to a named claim in a live hypothesis. A false declaration is refused and the observation stays
   visible. The coordinator can instead `defer` it with a reason and revisit trigger, or `set_aside` it with a reason.
   Neither action changes a claim's biological assessment. The event log preserves the decision.
4. **Rephrasing a literature query is not necessarily progress.** For questions consisting of full-text reads, the
   engine compares the actual returned passages and biological claim scopes. If the passages were already processed
   for the same scope, the question is deferred before another investigator call. Different focus words alone do not
   bypass this check. New passages or changed claim scopes remain eligible. A refused extraction gets one repair
   opportunity. Failed retrievals and abstract-only responses do not count as reading an article body.
5. **The audit has a separate call reserve.** The shipped configuration reserves four model sends for the closing
   audit, inside the existing 24-send ceiling. It retains the existing final-comparison reserve. This protects the
   audit from ordinary investigation calls; it cannot override a currency limit, wall-time limit or missing replay
   response. If investigation stops before adoption, unresolved observations remain visible to the critic and report.
6. **Reports expose unfinished adoption.** The gaps section identifies accepted observations without a non-context
   hypothesis link or an explicit decision. Metrics include `evidence_led_hypotheses`,
   `observations_awaiting_adoption` and `evidence_decisions` under `metrics.json`'s `engine` entry. The timeline
   retains adoption decisions and refusals.

## Example of the intended behaviour

Suppose the first hypothesis proposes variant → factor A binding → element activity → gene expression. A new assay
instead measures allele-specific occupancy of factor B. The investigator should describe that result in its actual
scope, creating a factor B claim if needed. The coordinator can then:

- Add a factor B branch using the occupancy evidence, retaining valid independent element/gene claims.
- Replace a factor A claim locally when evidence actually warrants replacement.
- Defer the new branch when active slots are full, with a revisit trigger.
- Set the observation aside when its variant, allele, experimental context or other scope does not apply.

Occupancy of B is not a contradiction of A merely because B is different. It also does not establish B-mediated
element activity or a disease effect. Those links remain separate, unresolved claims or explicitly named gaps.
Neither a QBiC gate nor a TF name determines whether the new branch is allowed.

## Bounds and scientific safeguards

The defaults allow two new hypotheses per plan and four evidence-led hypotheses across a run. Rejected and deferred
branches still count towards the run-wide allowance. There are still three ordinary active slots. Existing hypotheses
can be deferred to free a slot; failure to win a slot is not a refutation. Initial proposal and regeneration limits
retain their existing roles.

The adoption review list covers accepted observations such as binding, occupancy, perturbation, expression and
association results. It does not turn predictions, annotations, article mentions or authors' hypotheses into measured
results. Initial database facts remain in the original evidence bundle; they do not each create a mandatory review
item. Later observations and extracted experimental results can create review items.

Repeated extractions of the same passage can be grouped for review. This is **not evidence deduplication** and does
not claim that two experiments are independent or identical. Every evidence record keeps its provenance and scope.
A non-context link for a grouped observation does not automatically support every TF or downstream link mentioned in
that passage. Standard claim-level evidence checks and the critic still matter.

Deferral triggers are natural-language conditions for the coordinator to revisit, not a new automatic rule engine.
Earlier deferrals remain in packets. A deferred observation stays out of the mandatory pending list until it is
explicitly reconsidered; a genuinely different observation remains eligible for review.

Old scripted fixtures and their cached replays remain readable. Live planning must provide the new fields; omitting all of them cannot opt
out of evidence decisions. New prompts and schemas change model-cache keys, so an earlier live run is not expected
to replay exactly under the changed code. Its saved graph and report remain inspectable and unchanged.

## Verification and limits of the evidence

The focused tests use invented factors and scripted model responses, with network access blocked. They check:

- Branching while the old hypothesis remains viable, including renamed factors and reversed binding direction.
- Preservation of valid shared claims, correct evidence scope and the absence of an invented downstream conclusion.
- Active/run-wide limits, same-plan question references and provenance of the new branch.
- Rejection of summary-only adoption, missing decisions, unknown evidence and unsupported declarations of use.
- Persistent evidence visibility in planning, audit, final comparison and report gaps.
- Repeated-read suppression, new-passage/new-scope exceptions and bounded extraction repair.
- Protection of audit capacity within the unchanged model-call ceiling.

A local data regression also reads the saved rs1427407 development graph without changing it. Its E338/E339/E344
observations remain visible as a review group: a context-only link to an earlier TF claim does not adopt them as a
binding claim. No variant, gene, TF or gold-label exception was added to runtime code or prompts.

These tests establish that the workflow permits and tracks the correct operations. They do **not** demonstrate that
a language model consistently chooses the right revision or that biological accuracy improved. No paid model rerun
or cluster prediction was part of this implementation.

The next empirical comparison should run the same development input under the previous and current code, with the
same model, tool data and resource caps, writing to separate run folders. Check whether relevant observations become
appropriately scoped claims, whether valid earlier claims survive, whether unresolved links stay unresolved, how many
repeated reads occur, whether the audit runs, and total cost. Use at least a few repeated runs before claiming a
reliable improvement; retain wrong-context observations as negative controls. Do not tune the mechanism to a gold label.

## Running the checks

With the project's environment selected:

```sh
uv run pytest tests/v9/test_evidence_adoption.py tests/v9/test_read_progress.py -q
uv run pytest -q -m 'not live and not cluster'
uv run ruff check src/variant2mechanism/v9 tests/v9
```

The v9 tests redirect writable caches, budgets and run folders into test-specific temporary directories. Missing-cache
tests simulate the missing response explicitly, so a newly populated developer cache cannot change their outcome.
DNS resolution as well as network connections is blocked during v9 tests.

## Repairs after the first live pilot (9 November 2026)

One rs1427407 development rerun showed that the investigator did propose GATA1/TAL1 claims, but its entire answer
was rejected because it listed locally declared claim keys in `answer.claim_ids`. A repeat-read check then blocked
the retry despite that processing failure. A separate computational answer put evidence in new claims' `initial_links`,
which the investigator application path silently ignored. These are general interface failures, not TF-specific rules.

The subsequent repair accepts metadata references to claims declared in the same answer, applies investigator initial
links through the normal graph gates, and permits one bounded retry for an invalid structured answer. Code resolves a
missing assessment version only for a genuinely new claim created earlier in that same batch. An existing claim,
including one deduplicated through a local key, still requires its read version. Unknown keys and mismatched evidence
remain refused. Repeated processing failure remains an unresolved processing gap, not biological negative evidence.

The unedited saved literature response now passes offline and yields direct/exact GATA1 and TAL1 links with supported
assessments when the response requests them. Another extraction from the same answer remains refused by the passage
check. The saved computational response now attempts all 13 nested links; ten pass and three remain blocked by trait
name matching. This check uses in-memory copies of the completed graph, so duplicated existing claims still cannot
receive an assessment without the required version. The original live graph was not changed.

These post-pilot repairs have not yet been exercised by a second live run. Trait identity/ontology handling and the
Open Targets query-size error exposed by the pilot remain separate work. Do not reinterpret the failed live run as a
successful adoption result merely because its saved response can now be processed correctly offline.
# Trait identity and Open Targets query repair (9 November 2026)

Trait identity now normalises a small explicit set of UK/US spelling equivalents, punctuation and ontology-id
formats. It does not use fuzzy similarity or substring matching to attach evidence. Full source measurement and
population qualifiers remain part of phenotype identity: mean versus maximum, or different patient groups, remain
separate even when mapped to the same broad EFO term. A named phenotype still needs a matching source label; an
ontology id is not permission to attach a different phenotype. The shared agent rules request those full labels.
Conversely, an identical full source label is not rejected because one record omits an ontology annotation carried
by another: source mappings may contain both phenotype and population terms. They are not complete identity sets.
Retrieval queries can still search whole-word phrases, now with the same spelling normalisation.

The Open Targets query uses 25 credible sets per page (maximum three pages), with an explicit one-row locus page
filtered to the requested variant. This avoids multiplying a 1,000-set page by the default nested locus page and
the L2G/colocalisation subqueries. Coverage beyond 75 sets is explicitly incomplete. Each set still carries its
own PIP, L2G predictions and colocalisation results; their shared study provenance is preserved. The existing caps
of five L2G and three colocalisation rows are retained, and truncated nested lists are now reported as incomplete.
A missing gene in those lists is not a negative result. A later-page error preserves earlier evidence and records
the failure. No new prediction model, ontology service or model-call allowance is introduced.

