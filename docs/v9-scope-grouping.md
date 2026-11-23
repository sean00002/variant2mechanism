# Scope-aware hypotheses and claim refinement

Hypothesis identity now uses the mechanism class and the exact set of required claim ids. The graph already
deduplicates claims by participants, relation, allele frame and context; phenotype labels and elements therefore
remain part of identity instead of disappearing from a coarse TF/gene signature. Genotype is included in the
context key. A title, endpoint summary or hypothesis-level context is not a substitute for scoped claims.

An exact duplicate reuses the existing hypothesis and explicitly retains any new optional claims. A `decide`
event records the merge and added ids. Repeating an already validated evidence link acknowledges the existing
link without adding evidence or changing its version, assessment, rationale or limitations. Different stance or
applicability still follows the normal checked revision path.

Scope relationships are derived from the graph and exported as `claim_refinements`. They are visible in agent
packets and HTML reports. They are never biological evidence, entailment, or permission to transfer an assessment:

| Relationship | Meaning and conservative boundary |
| --- | --- |
| `equivalent_scope` | Same participants, relation, allele frame and normalised context. Can occur with separately recorded phenotype annotations. |
| `specifies_scope` | The same assertion gains a stated context. The unspecified parent was not a universal claim. |
| `narrower_scope_than` | A registry-known biosample belongs to the explicitly recorded organ scope, with matching species, condition and genotype. This describes scope containment, not universal biological effects. |
| `related_scope` | Different scopes or shared phenotype annotations, without a proven subset relationship. Population nesting is not guessed from trait-name substrings or a shared ontology id. |

Full source trait labels are retained. For example, a general trait label and the same measurement in a disease
population can form related branches. Unless the population relationship is independently established, that is
`related_scope`, not a certified population subset. Mean and maximum measurements also remain separate.

`hypothesis_families` groups connected related branches for browsing. These are scope families, not TF
DNA-binding-domain families. They neither merge hypotheses nor alter active slots, rankings, evidence independence,
support or rejection. Each branch keeps its claims, evidence and disposition. A contradiction in a matched cell
context can reject that claim's hypothesis while leaving a different context unresolved. An identical rejected
claim cannot be revived by renaming it or adding a canonical id.

The derived views are recomputed when loading/exporting a graph; supplied view fields are not trusted. Historical
run files are not rewritten. Their persisted old signature is retained for history, but operational identity
checks derive the scoped signature from their required claims.
Replaying pre-scope demo exports honestly reports new derived fields and signature strings as differences. The
production replay comparator remains strict; compatibility tests verify that the retained demos have no other
scientific changes. New-format replay remains deterministic.

Validation uses synthetic trait/population cases, not a variant-specific rule. An additional offline diagnostic
loads the previous rs1427407 graph, retains the orphan C5 in a new deferred branch, and checks that all 12 previously
unadopted observations become represented. That diagnostic does not alter the saved run or imply new biological
support. Live rerun results and remaining limitations are recorded separately in the HTML comparison report.
