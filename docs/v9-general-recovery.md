# Evidence views, variant identity and recovery checks

This revision addresses the failure modes seen in the two 10 November development checks. It contains no variant,
TF, target gene or primary-paper lookup table. The agent inputs remain coordinates, alleles and origin only.

`evidence_view.py` renders bounded detail plus a scope-grouped index from the complete evidence store. Grouping is
for presentation: it does not alter record independence, candidate eligibility, assessments or the saved graph.
The local `evidence_inspect` tool retrieves original records by ID or by a text filter and page offset. A large
pending-adoption list uses the same bounded view. Index omission is explicitly labelled and is never a rejection.

Europe PMC searches with a truncated broad result set can interleave relevance and citation-order results under
the same query. The extra request is bounded, recorded and supplies discovery pointers only. Citation frequency
does not change evidence strength. The existing review-to-primary citation workflow remains available.

`variant_identity.py` obtains NCBI RefSNP primary chromosome placements through the existing HTTP client during
variant annotation, using an exact-allele rsID identified by VEP. A GRCh38 placement must match the input position,
reference and alternate allele before another assembly placement is usable. Other alternate alleles at the same
rsID, alternate loci, patches and mismatching or ambiguous placements are excluded. Only filtered identity
metadata reaches the agent, not clinical annotations, gene assertions or paper citations from the RefSNP response.

Literature extraction recognises explicit adjacent article-local definitions such as `chr7:2345778 C>T (C87T)`.
It does not infer aliases from proximity or prior knowledge. Conflicting definitions remain unresolved. A verified
experiment retains its paper notation; a separate provenance object records any unique build/strand mapping to
the case. When an article does not state a build, that omission is retained, and only one matching primary-assembly
placement can be used. This is deliberately a bounded SNV implementation, not a universal HGVS resolver.

The effect-allele field requires a single allele. A mutation pair is not silently converted into an effect allele.
For a defined mutant-versus-wild-type assay, the mutation's alternate base can ground an extracted effect allele.
An ambiguous direction remains unspecified. Reporter-scoped claims can be retained independently; a reporter is
at most indirect support for a claim explicitly asserting endogenous regulatory activity. Agent instructions ask
for the narrower claim and keep the endogenous link unresolved rather than substituting endpoints.

CIViC browse queries now request the `name` field of alias objects and normalise the returned aliases before
matching. Both browse and variant-detail queries were checked against the public API. Errors and missing data
continue to create no biological negative evidence.

Offline validation covers invented mutation aliases, competing variants, wrong alternate alleles, unsupported
assemblies, strand conversion, reporter scope, compact-view accessibility, discovery ranking diversity and alias
objects. Existing cache-dependent tests now explicitly simulate absent pages or the absent modern query when
testing those conditions, so adding live cache entries does not invalidate their premise.

Final validation passed 906 v9 tests and 204 legacy tests (1,110 unique tests); the real-cluster test was skipped.
Six mock-cluster tests initially used system Python without pandas and passed with the project Python on PATH. The intermediate live rs12740374 check exposed
a mismatch between compact views and mandatory per-record adoption. The final revision bounds the mandatory queue
to six review groups, preserving every other observation as pending. It also preserves all returned paper IDs when
shortening search metadata, and escapes untrusted text in the compact index. The implementation was frozen again for one new
rs12740374 check and one new TERT check under the cumulative $5 development ceiling, retaining the
existing model-call and tool caps. Previous graphs and gold labels are preserved. These known positive cases are
development checks, not a validated benchmark or a controlled ablation of individual repairs.

## Final frozen reruns

Both runs found a key primary study, but neither new run retained a literature experiment or supported molecular
claim. rs12740374 read Musunuru et al. (2010), then rejected two extractions for a non-verbatim passage and a quote
over 600 characters. It repeatedly reread another abstract instead of repairing the original source. TERT read
Bell et al. (2015), but did not connect G228A/G250A shorthand to the case and incorrectly described unresolved
identities as different variants. The NCBI placements and CIViC browse retrieval worked; the identity decision loop
remains incomplete. These are failures of end-to-end recovery despite passing component tests.

Final runs: `dev11_rs12740374_general_recovery_20261110` (18 model calls, $0.035150) and
`dev12_tert_c228t_general_recovery_20261110` (17 calls, $0.042411). Both stopped at the model-call reservation guard.
The failed intermediate run is preserved as `dev10_rs12740374_general_recovery_20261110`. This task used $0.101298
in total; the shared ledger is $0.566387 of the $5 ceiling, with no reservations remaining. Earlier graphs and gold
labels match their original hashes.

The next change should route extraction failures back to their exact source and keep unresolved identity separate
from verified difference. Source sentence/span selection, paper-scoped observations pending identity mapping,
and a no-new-information check on repeated reads address the observed failures without a biological lookup table.
These recommendations were not implemented between the final two runs.

The portable report is `demo/v9/recovery-check-20261110/index.html`. It includes before/after summaries, source-linked
claim diagrams, refusal reasons, failed intermediate results, and budget/test audits.
