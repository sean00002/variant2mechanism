"""The joiner: evidence that a chain's transcription factor and its target gene belong together.

Why: a chain is assembled from claims that share a name. The variant's claims about a TF and its claims about a gene
are joined into one chain for every TF and every gene, so a tie between twelve TFs and three genes is thirty-six
chains with the same evidence, and nothing says which TF goes with which gene. One kind of experiment does: the TF
is knocked down, knocked out or overexpressed and the gene's RNA or protein changes. Articles that name the variant
hold a few such experiments (the reader files them, and chain.py puts the joined chain first among equals). Most
are in articles that never name the variant, because a TF acts on a gene whatever variant one is asking about. The
joiner goes and reads those.

    find      code searches Europe PMC for each pair: the TF (any member of its group) and the gene in a title or
              abstract, with a word for a perturbation; the same search for every pair
    choose    code keeps the passages that name the TF and the gene, and the abstract
    read      a model reads one article for one pair and returns the experiments in which the TF was changed and
              the gene's product was measured
    file      code copies the sentences it pointed to and checks every field, exactly as for the reader
    join      chain.py puts a chain whose TF and gene such a record names before an otherwise equal chain

- A join is a statement about a TF and a gene, not about the variant. It shows that the TF acts on the gene
  somewhere; it does not show that it does so through this variant's site. So it only ever breaks a tie: it never
  moves a chain past one with stronger evidence on a link, and no cell of the table counts it.
- The model is told the pair, because it has to know what to look for. What keeps that honest: every pair of the
  leading chains gets the same search and its articles are read in turn; the model returns pointers to sentences,
  never a verdict; a result that found no change is filed as one; and a pair with no experiment behind it stays
  as it was.
- A well-studied TF has more such articles than an obscure one. The tie-break inherits that attention, which is
  why the report lists, for every pair, how many articles were listed and read.
"""

from collections.abc import Sequence
from typing import Any

from ..agent.schemas import SchemaCheckError
from . import literature as L
from . import reader as RD
from .chain import JOIN_FLAG
from .graph import ClaimGraph
from .roles import GUARD, Strict, fence, prompt
from .schemas import Direction, ToolCall, ToolRequest

JOINER_FORMAT = 1
JOIN_RESULTS = 3                   # articles one pair's search lists
JOIN_CHARS = 15_000                # characters of one article's passages in one packet
JOIN_PURPOSE = "the joiner: articles in which a chain's TF was changed and its gene read out"
JOIN_READ_PURPOSE = "the joiner: the article's text, for one reading"
# A perturbation of a TF, as titles and abstracts name one.
PERTURBATION_WORDS = ("knockdown", '"knock-down"', "siRNA", "shRNA", "knockout", '"knock-out"', "CRISPRi",
                      "overexpression", "silencing", "depletion")
STATUSES = ("read", "no_mention", "review", "unreadable", "failed", "over_cap")


class JoinExperiment(Strict):
    location: str
    first_sentence: int
    last_sentence: int
    organism: str
    tissue_or_cell: str
    tf: str
    gene: str
    intervention: str
    endpoint: str
    result: str
    direction: Direction
    unclear: bool


class JoinReading(Strict):
    experiments: list[JoinExperiment]
    note: str


def system_prompt() -> str:
    return prompt("joiner_system")


def join_query(tfs: Sequence[str], gene: str) -> tuple[str, int]:
    """The search for one pair, and how many of the TF's names it holds: the TF (any name) and the gene in a title
    or abstract, with a word for a perturbation. Names are taken in order while the query fits."""
    words = "(" + " OR ".join(PERTURBATION_WORDS) + ")"
    used: list[str] = []
    for name in tfs:
        trial = " OR ".join(f'TITLE_ABS:"{n}"' for n in [*used, name])
        if len(f'({trial}) AND TITLE_ABS:"{gene}" AND {words}') > L.QUERY_LIMIT:
            break
        used.append(name)
    used = used or list(tfs[:1])
    named = " OR ".join(f'TITLE_ABS:"{n}"' for n in used)
    return f'({named}) AND TITLE_ABS:"{gene}" AND {words}', len(used)


def choose(article: L.Article, tfs: Sequence[str], gene: str) -> tuple[list[L.ArticleSection], int]:
    """The passages one call shows, in document order, and how many passages name both the TF and the gene: the
    abstract, then every passage outside a retelling section that names a TF of the pair and the gene, up to
    JOIN_CHARS characters. Empty when no such passage exists: there is nothing a join could be read from."""
    tf_patterns = [L._term_pattern(n) for n in tfs]
    gene_pattern = L._term_pattern(gene)
    sections = article.sections

    def both(text: str) -> bool:
        folded = L.normalise_for_match(text).casefold()
        return bool(gene_pattern.search(folded)) and any(p.search(folded) for p in tf_patterns)

    told = {i for i, s in enumerate(sections) if L._retold(s, "") is not None}
    hits = [i for i, s in enumerate(sections) if both(f"{s.heading} {s.text}")]
    reported = [i for i in hits if i not in told or sections[i].location.startswith("abstract/")]
    if not reported:
        return [], len(hits)
    abstract = [i for i, s in enumerate(sections) if s.location.startswith("abstract/")]
    chosen: list[int] = []
    used = 0
    for i in dict.fromkeys([*abstract, *reported]):
        size = len(sections[i].text)
        if used + size <= JOIN_CHARS:
            chosen.append(i)
            used += size
    return [sections[i] for i in sorted(chosen)], len(hits)


def packet(article: L.Article, chosen: Sequence[L.ArticleSection], label: str, tfs: Sequence[str], gene: str) -> str:
    """What one call reads: the pair, the article's identifiers and the chosen passages. It names no variant, no
    trait and nothing else of the run, so one article and one pair always give one request."""
    where = f"{article.journal} {article.year or ''}".strip()
    names = ", ".join(tfs[:30]) + (f" and {len(tfs) - 30} more" if len(tfs) > 30 else "")
    lines = [
        "Role: joiner; stage: read one article for one pair",
        "",
        "The pair",
        f"- transcription factor: {fence(label)}" + (f" (any one of: {fence(names)})" if len(tfs) > 1 else ""),
        f"- gene: {fence(gene)}",
        "",
        f"Article: {fence(article.title)}",
        f"- {', '.join(article.source_ids())}" + (f"; {fence(where)}" if where else "")
        + (f"; publication type: {fence(article.publication_type)}" if article.publication_type else ""),
        "- access: " + ("full text" if article.access == "full_text" else
                        "abstract only (methods, controls and full results were not retrieved)"),
        f"- passages shown: {len(chosen)} of {len(article.sections)}",
        "",
        "<data>",
        RD.render(chosen),
        "</data>",
        "",
        "Return the experiments of this article in which the factor was changed and a product of the gene was "
        "measured, as your instructions say. Point to each result by the location id in square brackets and the "
        "numbers of its first and last sentence.",
    ]
    return "\n".join(lines)


def as_read(x: JoinExperiment) -> RD.ReadExperiment:
    """A returned join as the reader's experiment, so that the same code files it: a perturbation of a TF with a
    gene read out, about no variant and no element."""
    return RD.ReadExperiment(
        location=x.location, first_sentence=x.first_sentence, last_sentence=x.last_sentence, organism=x.organism,
        tissue_or_cell=x.tissue_or_cell, treatment="", genotype_or_allele="", assay="perturbation",
        intervention=x.intervention, endpoint=x.endpoint, comparator="", result=x.result, direction=x.direction,
        about_tfs=[x.tf], about_genes=[x.gene], about_elements=[], about_traits=[], about_variants=[],
        manipulated="tf", compared_allele=None, authors_hypothesis_vs_result="result", scope_does_not_test="",
        haplotype=False, unclear=x.unclear)


class Joiner:
    """One run's joins (see the module docstring). It works beside a reader: the reader's model caller makes the
    calls, its runner fetches the articles, and its filing code files what comes back."""

    def __init__(self, reader: RD.Reader):
        self.reader = reader
        self.articles: list[dict[str, Any]] = []
        self.searches: list[ToolCall] = []

    def known(self, found: dict[str, Any], pair: str) -> bool:
        """Whether an article is on file already for this pair: the reader listed it (its experiments on the TF and
        the gene are then filed already), or this pair's search listed it in an earlier round. An article listed
        for two pairs is read for each, with the passages that name that pair."""
        ids = RD._ids(found)
        return bool(ids) and (self.reader.known(found) is not None
                              or any(ids & set(r["ids"]) and r["join"]["pair"] == pair for r in self.articles))

    def search(self, graph: ClaimGraph, label: str, tfs: Sequence[str], gene: str,
               round_no: int) -> tuple[ToolCall, list[dict[str, Any]], int, int]:
        """One pair's search: the call, the rows of the articles not on file, how many it listed and how many of
        the TF's names the query held."""
        query, held = join_query(tfs, gene)
        call = self.reader.runner.run(ToolRequest(tool=L.SEARCH_TOOL, purpose=JOIN_PURPOSE,
                                                  params={"query": query, "max_results": JOIN_RESULTS}),
                                      graph.case, graph, "code")
        self.searches.append(call)
        rows, listed = [], 0
        for found in call.observations if call.execution_status == "success" else []:
            ids = RD._ids(found)
            if not ids:
                continue
            listed += 1
            if self.known(found, label) or any(r["ids"] & ids for r in rows):
                continue
            rows.append({"ids": ids, "pmid": found.get("pmid"), "pmcid": found.get("pmcid"), "doi": found.get("doi"),
                         "title": found.get("title") or "", "publication_type": found.get("publication_type") or "",
                         "found_by": [call.tool_call_id], "status": "over_cap", "why": "",
                         "join": {"round": round_no, "pair": label, "tfs": list(tfs), "gene": gene}})
        return call, rows, listed, held

    def _read(self, graph: ClaimGraph, row: dict[str, Any]) -> None:
        """One article for one pair: fetch, choose, one model call, file. The row records what happened."""
        reader, pair = self.reader, row["join"]
        if L._REVIEW.search(row["publication_type"] or ""):
            row.update(status="review", why="indexed as a review")
            return
        fetched = reader._fetch(graph, row)
        if fetched is None:
            return
        call, article = fetched
        row.update(article=article.key, access=article.access, title=row["title"] or article.title)
        if article.is_review:
            row.update(status="review", why="a review article")
            return
        shown, named = choose(article, pair["tfs"], pair["gene"])
        row.update(passages=len(article.sections), passages_naming=named, passages_shown=len(shown))
        if not shown:
            row.update(status="no_mention", why="no passage that reports results names both the TF and the gene")
            return
        sent = reader.roles.client.calls

        def pointers(reading: JoinReading) -> JoinReading:
            """Send a first reply back once when it points where code cannot copy from (as the reader does)."""
            if reader.roles.client.calls - sent == 1:
                problems = RD.pointer_problems(
                    RD.ArticleReading(experiments=[as_read(x) for x in reading.experiments], note=""), shown)
                if problems:
                    raise SchemaCheckError(RD.correction(problems))
            return reading

        label = f"{pair['pair']}"
        out = reader.roles.join(system_prompt(), packet(article, shown, label.split(" → ")[0], pair["tfs"],
                                                        pair["gene"]), JoinReading, pointers)
        graph.set_model_usage(reader.roles.calls_used, reader.roles.cost_usd)
        if out is None:
            kind = reader.roles.failures[-1]["kind"] if reader.roles.failures else "failed"
            row.update(status="failed", why=kind)
            if reader.roles.replay_miss and reader.keep_going:
                reader.roles.replay_miss = False
            elif reader.roles.replay_miss:
                reader.stopped = "cache_miss"
            elif reader.roles.currency_exhausted:
                reader.stopped = "budget_currency"
            return
        accepted = [eid for i, x in enumerate(out.experiments)
                    if (eid := reader._file(graph, as_read(x), i, article, call, shown))]
        accepted = list(dict.fromkeys(accepted))
        joins = [e for e in accepted if isinstance(graph.evidence[e].data.get(JOIN_FLAG), dict)]
        row.update(status="read", why="", experiments=len(out.experiments), accepted=accepted, joins=joins,
                   refused=len(out.experiments) - len(accepted), note=" ".join(out.note.split())[:RD.NOTE_LIMIT])

    def read_more(self, graph: ClaimGraph, rows: Sequence[dict[str, Any]], cap: int, *,
                  reading: bool = True) -> list[dict[str, Any]]:
        """The articles the pairs' searches listed, in the order given, at most `cap` sent to the model. With
        `reading` False nothing is fetched or sent (a dry run). Returns the rows, closed."""
        roles = self.reader.roles
        roles.set_limits(roles.max_calls + GUARD * max(cap, 0), 0)
        sent = 0
        for row in rows:
            self.articles.append(row)
            if not reading:
                row.update(status="over_cap", why="a dry run: listed, not read")
            elif self.reader.stopped or sent >= cap:
                row["why"] = (f"reading stopped: {self.reader.stopped}" if self.reader.stopped else
                              "the round's cap on articles")
            else:
                before = roles.calls_used
                self._read(graph, row)
                sent += roles.calls_used > before or row["status"] == "failed"
            row["ids"] = sorted(row["ids"])
            row["label"] = row.get("article") or row["pmcid"] or (f"PMID:{row['pmid']}" if row["pmid"] else row["doi"])
            graph.log("collect_facts", "code",
                      f"the joiner: {row['label']} for {row['join']['pair']}: {row['status']}"
                      + (f" ({row['why']})" if row["why"] else "")
                      + (f"; {row.get('experiments', 0)} experiment(s) returned, {len(row.get('accepted', []))} "
                         f"filed, {len(row.get('joins', []))} of them a join" if row["status"] == "read" else ""),
                      target_ids=[t for t in [row.get("read")] if t], evidence_ids=row.get("accepted", []),
                      details={"joiner": {k: v for k, v in row.items() if k != "note"}})
        return list(rows)

    def summary(self) -> dict[str, Any]:
        rows = self.articles
        counts = {key: sum(r["status"] == key for r in rows) for key in STATUSES}
        return {"format": JOINER_FORMAT, "searches": len(self.searches), "found": len(rows), **counts,
                "experiments": sum(r.get("experiments", 0) for r in rows),
                "accepted": len({e for r in rows for e in r.get("accepted", [])}),
                "joins": len({e for r in rows for e in r.get("joins", [])}),
                "pairs_joined": sorted({r["join"]["pair"] for r in rows if r.get("joins")}),
                "articles": rows}


def manifest_parts() -> dict[str, Any]:
    """What a run with the joiner records as its settings: its prompt and output schema by hash, and its caps."""
    import hashlib
    import json

    from ..agent.llm import strict_schema
    schema = json.dumps(strict_schema(JoinReading), sort_keys=True).encode()
    return {"joiner_format": JOINER_FORMAT, "join_results": JOIN_RESULTS, "join_chars": JOIN_CHARS,
            "perturbation_words": list(PERTURBATION_WORDS),
            "prompt_sha256": hashlib.sha256(system_prompt().encode()).hexdigest(),
            "schema_sha256": hashlib.sha256(schema).hexdigest()}
