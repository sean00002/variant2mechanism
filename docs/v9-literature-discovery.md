# Literature discovery and mechanistic resolution

The development run on 9 November 2026 searched for a variant together with specific assays, showed a top-five
review-only list, then tried to follow a review reference that the reader had discarded. Subsequent queries added
more assay terms and still missed the primary study. This is a retrieval failure, not evidence against a mechanism.

The repair is general and does not encode variant, factor, gene or paper identities:

- Search lists default to ten records, still bounded by the existing character and request limits. When every
  returned paper is indexed as a review, the adapter makes at most one additional query excluding indexed reviews,
  retains one review as a citation pointer, and records the exact query, result and failure status. This is triage;
  a non-review tag does not certify an experimental study. Searches do not create evidence.
- The coordinator starts with a broad observed variant/locus query. Assay, factor and tissue terms are added only
  to answer specific gaps. Reviews are useful pointers, not substitutes for primary results.
- JATS bibliography references and paragraph-level xref/rid links are retained separately from extractable article
  sections. A read shows up to eight relevant references within a 3,000-character allowance inside the existing
  14,000-character read limit. Reference labels, actual XML ids, titles and structured PMID/PMC/DOI identifiers are
  preserved. Missing identifiers stay missing; agents can search an exact title/DOI. A citation to a paragraph does
  not prove support for each sentence. A reference cannot be extracted as an experiment from its citing article.
- New citation pointers count as discovery progress; rephrasing focus around the same pointer does not.
- Planning, investigation and audit packets explicitly distinguish variant localisation, allele-to-element activity,
  candidate molecular changes and mediation. Region deletion is not an allele swap; ordinary ChIP is not an allelic
  binding experiment. A measured activity effect may remain a coarse supported claim with its molecular explanation
  unresolved. TF binding is optional. Gap reminders neither create claims nor alter support, scores or disposition.

This does not guarantee exhaustive retrieval, validate all citations or establish mediation from a binding result.
Bibliographies may lack identifiers or full text, article indexing may be incomplete, and model decisions remain
stochastic. A single development rerun is a demonstration, not a benchmark. Existing model, tool, full-text and
currency limits stay unchanged; QBiC remains the only prediction model.

API and format references: [Europe PMC REST](https://dev.europepmc.org/RestfulWebService) and
[NLM JATS rid](https://jats.nlm.nih.gov/archiving/tag-library/1.2/attribute/rid.html).

The first live check of this repair exposed two additional failure paths: a PMC ref-list can occur inside a body
section, and a found-but-unread primary paper can disappear from the coordinator's next packet when only the
investigator's summary is retained. The parser now traverses main-article bibliography entries in either location
(excluding sub-articles/responses) and accepts typed external identifier links as well as pub-id elements. The
coordinator and literature investigator also receive a bounded, deduplicated list of unread full-text leads derived
from their existing tool observations. Leads retire after a successful full-text read; abstract-only access does
not pretend the body was read. These pointers carry no support score and create no biological evidence.
