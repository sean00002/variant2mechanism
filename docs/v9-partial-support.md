# Partial support and recoverable investigator updates

The report now distinguishes molecular findings from completion and ranking of a declared hypothesis.
`resolution.support_summary` derives its view from the saved graph and appears in HTML, Markdown, engine metrics
and the critic's final packet. A live, supported, case-variant molecular claim needs an exact/proxy direct support
link from more than prediction or annotation. Optional claims count as molecular findings. Required-link completion
is scoped to the hypothesis's stated endpoint; a molecular-only hypothesis never establishes disease mediation by
that label. The existing winner/comparison rules and stored outcome enum are unchanged. Historical runs can be
rendered under this view without changing their evidence, hypotheses or original outcome.

Literature-investigator response validation now separates envelope errors (unknown questions/tool references, malformed JSON)
from semantic errors in individual claim updates. Envelope errors still reject the response. Invalid proposals and
updates depending on their uncreated local claims are individually refused and logged. Each extracted experiment
still passes the existing passage, assay, variant, context and direction verification before becoming evidence;
valid sibling updates still pass the graph's own gates. The question becomes deferred with precise repair feedback,
and unadopted evidence remains in the existing adoption queue. The bounded processing-retry rule also recognises
these semantic-update failures. No factor type, allele direction or biological conclusion is silently corrected.

The demonstration uses two new single-case development runs, with only coordinates/alleles and origin supplied,
under the existing release profile and shared $0.50 development ceiling. Gold labels and evaluator notes never
enter engine requests. The earlier rs1427407 run is retained and re-rendered, not presented as a new live rerun.
The gold specification remains unreviewed; the demo is a component-level engineering check, not a validated benchmark.

Computational-investigator validation retains its existing whole-response repair and version checks; it does not extract literature experiments.

The completed three-case report is in `demo/v9/three-case-demo-20261110/index.html`. The historical rs1427407 graph
has supported optional binding claims C8/C9. The new rs12740374 run stopped at a currency-reservation guard after
collecting 1,013 evidence records, without reading the expected primary study. The new TERT run reached a primary
reporter study but could not join its local mutation shorthand to article coordinates and a verified case mapping;
no molecular evidence was accepted. These are recovery failures, not evidence against either mechanism. No
between-run production changes or successful-only retries were made.

The final suite passed 1,098 tests (1 deselected); both new runs cost $0.107888 in total, bringing shared development
spend to $0.465089 of $0.50. Prior graphs, configuration and gold labels were unchanged. The next priorities are
bounded evidence views preserving all raw records, source-backed variant aliases with build/strand mapping,
assay-scoped claim refinement, and the observed CIViC schema mismatch. These follow-ups are not implemented here.
