"""loop.py: the fill going back for articles where its leading chains tie or are weakest.

The articles are the synthetic ones of the literature tests (invented text, test-only identifiers) on the
development variant rs1427407; the graph is the fill tests' evidence bundle. No model is called: a scripted
transport answers the reader by the article its packet names and the planner by its role line. No test here reaches
a provider or the network.
"""

from pathlib import Path
from types import SimpleNamespace
from typing import Any

import pytest

from variant2mechanism.v9 import commands, fill, joiner, loop, reader
from variant2mechanism.v9 import literature as lit
from variant2mechanism.v9 import roles as R
from variant2mechanism.v9 import table as T
from variant2mechanism.v9.graph import ClaimGraph, SymbolResolver

from . import test_literature_fakes as fakes
from .test_fill import bundle_graph
from .test_reader import (
    CASES,
    DELETION,
    EMSA,
    KNOCKDOWN,
    OTHER,
    REPORTER,
    REVIEW,
    RSID,
    TAL1_EMSA,
    UNNAMED,
    VARIANTS,
    Model,
    read_records,
    reading,
)

CITING, CITING_PMID = "PMC9000011", "90000011"            # the synthetic review that cites VARIANTS
PLANNER = "Role: planner"                                  # what every planner packet starts with
REPLIES = {CASES: reading(KNOCKDOWN, DELETION), VARIANTS: reading(EMSA, REPORTER)}
SYMBOLS = SymbolResolver({s: (s, f"HGNC:{i}") for i, s in enumerate(("GATA1", "TAL1", "GENE1", "BCL11A"), 1)})


ASSAYS = "(" + " OR ".join(reader.ASSAY_WORDS) + ")"


def with_tf(tf: str) -> str:
    return f'"{RSID}" AND "{tf}" AND {ASSAYS}'


def pair(tf: str, gene: str = "GENE1") -> str:
    """The joiner's search for one TF and one gene."""
    return joiner.join_query([tf], gene)[0]


class Open(fakes.FakeHttp):
    """Europe PMC as the tests need it: a search nobody scripted lists nothing, as a real one would for a query
    with no hit. `asked` keeps every search query in the order made."""

    def __init__(self, routes: dict[str, Any]):
        super().__init__(routes)
        self.asked: list[str] = []

    def get(self, url: str, **kw: Any):
        if url.startswith(lit.EPMC_REST + "/search"):
            self.asked.append(url)
            self.routes.setdefault(url, fakes.search_response([]))
        return super().get(url, **kw)


def setup(cfg, tmp: Path, first: list[str], later: dict[str, list[str]], replies: dict[str, dict] | None = None,
          *, planner: bool = False, **settings: Any):
    """A fill with the reader and the loop: `first` are the articles the first search lists, `later` maps a query
    of the loop to the articles it lists."""
    routes, rec = fakes.routes(), fakes.records()
    rec[CITING] = {**rec[REVIEW], "id": CITING_PMID, "pmid": CITING_PMID, "pmcid": CITING, "isOpenAccess": "Y",
                   "doi": "10.5555/v2m.test.11", "title": "Invented enhancer variants in erythroid cells: a review."}
    routes[lit.metadata_url(CITING, None)] = fakes.search_response([rec[CITING]])
    routes[lit.fulltext_url(CITING)] = fakes.text("oa_review_cites.xml")
    queries = reader.queries(RSID)
    routes[lit.search_url(queries[0], reader.SEARCH_RESULTS)] = fakes.search_response([rec[p] for p in first])
    routes[lit.search_url(queries[1], reader.SEARCH_RESULTS)] = fakes.search_response([])
    for query, listed in later.items():
        routes[lit.search_url(query, loop.ACTION_RESULTS)] = fakes.search_response([rec[p] for p in listed])
    http = Open(routes)
    model = Model(cfg, tmp, replies if replies is not None else REPLIES)
    runner = fakes.runner(http, tmp / "run", fulltext_soft=60, fulltext_hard=60)
    caller = R.RoleCaller(model.client, cfg)
    graph = bundle_graph()
    graph.resolver = SYMBOLS
    again = loop.Loop(caller if planner else None, **settings)
    return graph, reader.Reader(caller, runner), again, model, http


def cells(table: T.Table) -> dict[tuple[str, str, str], tuple]:
    """A table by what it says, whatever ids its claims got: each claim's three cells, and the chains in order."""
    return {(c.step, c.part, c.label): tuple((lane, c.cells[lane].state,
                                              sum(r.stance != "beside" for r in c.cells[lane].records))
                                             for lane in T.LANE_KEYS) for c in table.claims.values()}


def chains(table: T.Table) -> list[tuple[int, int, str]]:
    return [(c.rank, c.ties, c.title) for c in table.chains]


# --- gaps and the menu ------------------------------------------------------------------------------------------------

def test_the_gaps_are_the_first_chains_weak_claims_weakest_first(v9_cfg, tmp_path):
    graph, read, _, _, _ = setup(v9_cfg, tmp_path, [CASES], {})
    f = fill.Fill(graph, None, read)
    with graph.batch():
        f.attach()
    read.run(graph)
    before = (len(graph.claims), len(graph.events), graph.version)
    table = loop.Loop.preview(f)
    assert (len(graph.claims), len(graph.events), graph.version) == before          # a preview keeps nothing
    gaps = loop.find_gaps(table)
    assert [(g.kind, g.slot, g.state) for g in gaps] == [
        ("join", "join", "1 pair(s)"),
        ("weak", "activity.allele", "none"), ("weak", "binding.allele", "prediction"),
        ("weak", "gene.allele", "association"), ("weak", "trait.allele", "association"),
        ("weak", "trait.premise", "association")]
    # the first chain pairs a TF with a gene, and no record on file says the two belong together
    assert gaps[0].names == (("G001 (TFX) → GENE1", ("GENE1", "TFX")),)
    assert gaps[2].names == (("G001 (TFX)", ("TFX",)),) and gaps[1].names == ()
    # with a trait given, the way from the gene to the trait comes first among the weak claims
    assert [g.slot for g in loop.find_gaps(table, trait_given=True)][1:3] == ["trait.allele", "trait.premise"]
    menu = loop.build_menu(graph, gaps, read.articles, done=set(), followed=set())
    assert [(e.kind, e.gaps, [s.query for s in e.searches]) for e in menu] == [
        ("join", ["G1"], [pair("TFX")]),
        ("named", ["G3"], [with_tf("TFX")]), ("named", ["G4", "G6"], [with_tf("GENE1")])]
    assert menu[0].searches[0].join == ("GENE1", ("TFX",))
    # a search that was run is not offered again, and an entry with nothing left is not listed
    ran = {pair("TFX"), with_tf("TFX")}
    assert [e.kind for e in loop.build_menu(graph, gaps, read.articles, done=ran, followed=set())] == ["named"]
    assert loop.build_menu(graph, gaps, read.articles, done={*ran, with_tf("GENE1")}, followed=set()) == []


def table_of(*binding: tuple[str, list[str]]) -> T.Table:
    """A table whose chains tie for first and differ in the TF: one chain per (label, TFs)."""
    table = T.Table(case_id="X", variant="GRCh38:2:60490908:T:G")
    empty = {lane: T.Cell(state="nothing_found") for lane in T.LANE_KEYS}
    for key, slot in T.SLOTS.items():
        if key != "binding.allele":
            table.claims[key] = T.TableClaim(id=key, step=slot.step, part=slot.part, text=slot.text, label="shared",
                                             names={}, graph_claims=["C1"], cells=empty, strongest="assay")
    for label, tfs in binding:
        ident = f"binding.allele:{label}"
        table.claims[ident] = T.TableClaim(id=ident, step="binding", part="allele", text="", label=label,
                                           names={"tfs": tfs}, graph_claims=["C2"], cells=empty,
                                           strongest="prediction")
        table.chains.append(T.TableChain(rank=1, ties=len(binding), title=f"{label} → GENE1",
                                         claims={k: (ident if k == "binding.allele" else k) for k in T.SLOT_KEYS}))
    return table


def test_a_tie_is_one_action_over_every_tied_candidate(v9_cfg, tmp_path):
    graph, read, _, _, _ = setup(v9_cfg, tmp_path, [], {})
    many = [f"TF{i}" for i in range(100)]
    gaps = loop.find_gaps(table_of(("G1 (GATA1)", ["GATA1"]), ("G2 (TAL1, TAL2)", ["TAL1", "TAL2"]), ("G3", many)))
    assert [(g.kind, g.slot) for g in gaps] == [("tie", "binding.allele")]          # a tied claim is not also weak
    assert "3 chains tie for first and differ in the transcription factor" in gaps[0].text
    (entry,) = loop.build_menu(graph, gaps, [], done=set(), followed=set())
    assert entry.kind == "candidates" and [s.label for s in entry.searches][:2] == ["G1 (GATA1)", "G2 (TAL1, TAL2)"]
    assert entry.searches[1].query == f'"{RSID}" AND ("TAL1" OR "TAL2") AND {ASSAYS}'
    # a group with more names than one query holds is searched by as many as fit, and its label says how many
    group = entry.searches[2].query.split(" AND ")[1]
    searched = group.count(" OR ") + 1
    assert 20 < searched < 100 and entry.searches[2].label == f"G3 (first {searched} of its 100 names)"
    assert all(len(s.query) <= lit.QUERY_LIMIT for s in entry.searches)
    # a gene with no symbol is named by a database id, which no article writes: it is not searched for
    gaps = loop.find_gaps(table_of(("ENSG00000233953", ["ENSG00000233953"]), ("G1 (GATA1)", ["GATA1"])))
    (entry,) = loop.build_menu(graph, gaps, [], done=set(), followed=set())
    assert [s.label for s in entry.searches] == ["G1 (GATA1)"]


def test_a_tie_too_wide_to_search_alike_is_searched_for_no_candidate(v9_cfg, tmp_path, monkeypatch):
    graph, read, again, _, http = setup(v9_cfg, tmp_path, [], {}, dry=True)
    tied = [(f"G{i} (TF{i})", [f"TF{i}"]) for i in range(loop.TIE_SEARCHES + 1)]
    wide = table_of(*tied)
    # the first chain's own TF is in place by nothing, and its gene is named: a weak claim and a pair for every chain
    wide.claims["binding.premise"] = wide.claims["binding.premise"].model_copy(
        update={"names": {"tfs": ["TF0"]}, "strongest": "none", "label": "G0 (TF0)"})
    wide.claims["gene.allele"] = wide.claims["gene.allele"].model_copy(update={"names": {"genes": ["GENE1"]}})
    gaps = loop.find_gaps(wide)
    assert [(g.kind, g.slot) for g in gaps] == [("tie", "binding.allele"), ("join", "join"), ("weak", "binding.premise")]
    told = f"More than {loop.TIE_SEARCHES} are tied, so they are not searched for one by one"
    assert gaps[0].text.endswith(told) and len(gaps[0].names) == loop.TIE_SEARCHES + 1
    assert gaps[1].text.endswith(f"More than {loop.JOIN_PAIRS} pairs, so they are not searched for one by one")
    # every candidate or none: a search for the first chain's TF alone, by name or as a pair, would favour it
    assert gaps[2].names == ()
    assert loop.build_menu(graph, gaps, [], done=set(), followed=set()) == []
    # with one candidate fewer each is searched, the same search for each, and so is each pair
    fewer = table_of(*tied[:-1])
    fewer.claims["gene.allele"] = wide.claims["gene.allele"]
    menu = loop.build_menu(graph, loop.find_gaps(fewer), [], done=set(), followed=set())
    assert [(e.kind, len(e.searches)) for e in menu] == [("join", loop.JOIN_PAIRS), ("candidates", loop.TIE_SEARCHES)]
    # a run on the wide tie makes no search, stops, and its report says why
    monkeypatch.setattr(loop.Loop, "preview", staticmethod(lambda fill: wide))
    done = again.run(SimpleNamespace(graph=graph, reader=read))
    assert (done["stop"], done["searches"], http.asked) == ("empty_menu", 0, [])
    many = loop.TIE_SEARCHES + 1
    assert done["rounds"][0]["text"] == (f"nothing on the menu; {many} tied candidates are too many to search for one "
                                         f"by one; {many} pairs of TF and gene are too many to search for one by one")
    assert "It was a dry run, and there was nothing to search for." in loop.report_view(graph)["lead"]


# --- the rounds --------------------------------------------------------------------------------------------------------

def test_the_loop_reads_what_a_gap_search_finds_and_stops_when_a_round_changes_nothing(v9_cfg, tmp_path):
    graph, read, again, model, http = setup(v9_cfg, tmp_path, [CASES], {with_tf("TFX"): [VARIANTS, CASES]})
    counts = fill.run(graph, None, read, loop=again)
    done = counts["loop"]
    assert (done["planner"], done["rounds_run"], done["stop"]) == ("code", 2, "no_change")
    first, second = done["rounds"]
    # round 1: both searches ran; one listed an article not on file, which was read and filed
    assert [(e["for"], e["listed"], e["new"], e["read"], e["filed"]) for e in first["effort"]] == [
        ("G001 (TFX) → GENE1", 0, 0, 0, 0), ("G001 (TFX)", 2, 1, 1, 2), ("GENE1", 0, 0, 0, 0)]
    assert first["plan"]["by"] == "code" and first["changed"]["any"] and first["changed"]["leaders_changed"]
    assert first["changed"]["cells"] == [
        "TF binding: the alleles differ (GATA1), literature: no such claim to supports (1)",
        "Regulatory activity: the alleles differ (EH38E0000001), literature: nothing found to supports (1)"]
    assert first["text"] == ("1 pair(s) of TF and gene searched, 2 search(es) for what a weak claim names: 1 new "
                             "article(s) listed, 1 read, 2 experiment(s) filed; 2 cell(s) changed; the first chains "
                             "changed")
    # round 2 worked on the new first chain, found nothing new, and that ended the loop
    assert second["changed"] == {**second["changed"], "any": False, "cells": []}
    assert all(e["new"] == 0 for e in second["effort"])
    assert (done["new_articles"], done["articles_read"], done["filed"], done["cells_changed"]) == (1, 1, 2, len(
        first["changed"]["cells"]))
    assert done["leaders_before"] == ["G001 (TFX) → GENE1"] and done["leaders_after"] != done["leaders_before"]
    # the reading's own count now holds the article the loop read, and the table quotes that count
    assert (counts["reading"]["found"], counts["reading"]["read"], counts["reading"]["accepted"]) == (2, 2, 4)
    row = next(r for r in counts["reading"]["articles"] if r["label"] == VARIANTS)
    assert row["loop"] == {"round": 1, "action": "named", "for": "G001 (TFX)"}
    assert "2 of 2 articles found were read" in T.to_markdown(T.from_graph(graph), [])
    # how many of the filed experiments count for a claim, by what the search was for
    assert done["counted"] == {"named: G001 (TFX)": 2}
    assert "The loop then went back for evidence: in 2 round(s) it read 1 more article(s)" in graph.result.summary
    assert done["model_calls"] == 0 and len(model.packets) == 2                       # two readings, no planner
    # the report says what each round did and what every search came to
    view = loop.report_view(graph)
    assert view["effort"][:2] == [
        ["1", "G001 (TFX) → GENE1", "the TF changed and the gene read out", "0", "0", "0", "0", "", "0"],
        ["1", "G001 (TFX)", "the variant with what a weak claim names", "2", "1", "1", "2", "2", ""]]
    assert "the loop ran 2 round(s): code took its own menu in order" in view["lead"]
    assert "It read 1 more article(s), from which 2 experiment(s) were filed: 2 count for a claim." in view["lead"]
    assert view["moved"].startswith("First before: G001 (TFX) → GENE1. First after: GATA1 → GENE1")
    from variant2mechanism.v9 import report
    extras = report.table_extras(graph)
    assert "Going back for evidence" in "\n".join(report._loop_markdown(extras)) and "loop-h" in report._loop_html(extras)
    assert loop.report_view(bundle_graph()) is None                                   # no loop, no section


def test_the_table_is_the_one_a_single_pass_over_the_same_articles_gives(v9_cfg, tmp_path):
    graph, read, again, model, _ = setup(v9_cfg, tmp_path / "a", [CASES], {with_tf("TFX"): [VARIANTS]})
    fill.run(graph, None, read, loop=again)
    plain, read2, _, model2, _ = setup(v9_cfg, tmp_path / "b", [CASES, VARIANTS], {})
    fill.run(plain, None, read2)
    looped, once = T.from_graph(graph), T.from_graph(plain)
    assert chains(looped) == chains(once)
    assert {k: v for k, v in cells(looped).items()} == {k: v for k, v in cells(once).items()}
    assert T.check(looped, graph) == []
    # the reader stays blind: the request for the article the loop found is the one a plain run sends
    packet = next(p for p in model.packets if VARIANTS in p)
    assert packet == next(p for p in model2.packets if VARIANTS in p) and "TFX" not in packet.split("<data>")[0]


def test_the_cap_on_a_round_cuts_every_search_alike(v9_cfg, tmp_path):
    graph, read, again, _, _ = setup(v9_cfg, tmp_path, [], {"q1": [VARIANTS, OTHER], "q2": [UNNAMED, VARIANTS]},
                                     round_articles=1)
    f = fill.Fill(graph, None, read)
    read.run(graph)
    entry = loop.Entry(1, "candidates", ["G1"], "two tied candidates",
                       [loop.Search("A", "q1"), loop.Search("B", "q2")])
    effort, rows = again._act(f, [entry], 1)
    # read in turn: the first article of each search before the second of any; one listed twice is read once
    assert [r["label"] for r in rows] == [VARIANTS, UNNAMED, OTHER]
    assert [(e["for"], e["listed"], e["new"], e.get("shared", 0)) for e in effort] == [("A", 2, 2, 0), ("B", 2, 1, 1)]
    assert [r["status"] for r in rows] == ["read", "over_cap", "over_cap"]            # the cap is one reading
    assert rows[1]["why"] == rows[2]["why"] == "the round's cap on articles"
    assert len(next(r for r in rows if r["label"] == VARIANTS)["found_by"]) == 2      # both searches listed it


def test_a_review_is_followed_to_what_it_cites_where_it_speaks_of_the_variant(v9_cfg, tmp_path):
    graph, read, again, model, http = setup(v9_cfg, tmp_path, [CASES, CITING], {})
    counts = fill.run(graph, None, read, loop=again)
    first = counts["loop"]["rounds"][0]
    follow = next(e for e in first["menu"] if e["kind"] == "follow")
    assert follow["reviews"] == [CITING]
    row = next(e for e in first["effort"] if e["action"] == "follow")
    # the paragraph that names the variant cites two works; one has an identifier and is not on file
    assert (row["for"], row["listed"], row["new"], row["read"]) == (CITING, 2, 1, 1)
    rows = {r["label"]: r for r in counts["reading"]["articles"]}
    assert rows[CITING]["status"] == "review" and rows[CITING]["followed"] == 1       # still never read as a record
    assert rows[VARIANTS]["loop"]["action"] == "follow" and rows[VARIANTS]["status"] == "read"
    assert OTHER not in rows                                # cited in a paragraph that does not name the variant
    assert not any(CITING in p for p in model.packets)      # the review's text is never sent to the model
    # a review is followed once
    assert not any(e["kind"] == "follow" for r in counts["loop"]["rounds"][1:] for e in r["menu"])


def test_an_article_found_under_a_catalogue_name_is_read_by_that_name(v9_cfg, tmp_path):
    from .test_fill import code_call
    from .test_fill_sources import SHORT, SHORT_PMID, SHORT_REPORTER
    graph, read, again, model, http = setup(v9_cfg, tmp_path, [CASES], {},
                                            {**REPLIES, SHORT: reading(SHORT_REPORTER)}, max_rounds=1)
    short = {**fakes.records()[CASES], "id": SHORT_PMID, "pmid": SHORT_PMID, "pmcid": SHORT,
             "doi": "10.5555/v2m.test.9", "title": "An invented enhancer mutation changes reporter activity."}
    http.routes[lit.metadata_url(SHORT, None)] = fakes.search_response([short])
    http.routes[lit.fulltext_url(SHORT)] = fakes.text("oa_shorthand.xml")
    http.routes[lit.search_url(f'"T908G" AND {ASSAYS}', loop.ACTION_RESULTS)] = fakes.search_response([short])
    # a catalogue lists the shorthand for this variant and verified it by position
    code_call(graph, "civic_lookup", observations=[{"record": "variant_alias_identity", "status": "verified_same",
                                                    "case_key": graph.case.variant.key, "aliases": ["T908G"],
                                                    "gene": "BCL11A"}])
    assert loop.other_names(graph) == ["T908G"]
    counts = fill.run(graph, None, read, loop=again)
    first = counts["loop"]["rounds"][0]
    assert [(e["action"], e["for"], e["new"], e["read"], e["filed"]) for e in first["effort"]
            if e["action"] == "other_names"] == [("other_names", "T908G", 1, 1, 1)]
    row = next(r for r in counts["reading"]["articles"] if r["label"] == SHORT)
    assert (row["status"], row["aliases"], row["loop"]["action"]) == ("read", ["T908G"], "other_names")
    # the article never writes the rsID: its passages were chosen by the catalogue's name, and the model was told
    told = next(p for p in model.packets if SHORT in p)
    assert "- a catalogue lists it under these names: T908G" in told and "[sec1.1/p1]" in told
    assert not any("a catalogue lists it" in p for p in model.packets if CASES in p)   # the first reading is as before
    # the variant's term in the other searches holds the catalogue's name too
    assert f'("{RSID}" OR "T908G") AND "TFX" AND {ASSAYS}' in again.done


def test_a_dry_run_lists_what_a_round_would_read_and_reads_nothing(v9_cfg, tmp_path):
    graph, read, again, model, _ = setup(v9_cfg, tmp_path, [CASES], {with_tf("TFX"): [VARIANTS]}, dry=True)
    counts = fill.run(graph, None, read, loop=again)
    done = counts["loop"]
    assert (done["rounds_run"], done["stop"], done["new_articles"], done["articles_read"]) == (1, "dry_run", 1, 0)
    row = next(r for r in counts["reading"]["articles"] if r["pmcid"] == VARIANTS)
    assert (row["status"], row["why"]) == ("over_cap", "a dry run: listed, not read")
    assert len(model.packets) == 1 and not [e for e in read_records(graph) if "90000008" in e.source_ids[0]]


def test_a_dry_run_reads_what_is_saved_and_goes_on_past_a_reading_that_is_not(v9_cfg, tmp_path):
    from variant2mechanism.v9.replay import ReplayMiss
    graph, read, again, model, _ = setup(v9_cfg, tmp_path, [CASES, VARIANTS], {}, dry=True)
    sent = model.send

    def offline(body: dict) -> dict:                        # the reading of CASES is saved; that of VARIANTS is not
        if VARIANTS in body["messages"][-1]["content"]:
            raise ReplayMiss("no cached reply")
        return sent(body)

    model.client._transport = offline
    read.keep_going = True                                  # what a dry run sets (commands.fill_graph)
    counts = fill.run(graph, None, read, loop=again)
    rows = {r["label"]: (r["status"], r["why"]) for r in counts["reading"]["articles"] if r.get("label")}
    assert rows[CASES] == ("read", "") and rows[VARIANTS] == ("failed", "replay_miss")
    assert counts["reading"]["stopped"] is None and counts["loop"]["stop"] == "dry_run"


# --- the planner -------------------------------------------------------------------------------------------------------

def plan(*picks: int, proposals: tuple = (), note: str = "It may fill the weakest claim.") -> dict:
    return {"picks": [{"action": n, "why": "it serves the weakest claim"} for n in picks],
            "proposals": [{"kind": k, "name": n, "why": "remembered"} for k, n in proposals], "note": note}


def test_the_planner_picks_from_the_menu_and_what_it_remembers_is_only_a_search_term(v9_cfg, tmp_path):
    replies = {**REPLIES, PLANNER: plan(3, proposals=(("tf", "gata1"), ("gene", "NOTAGENE"),
                                                      ("variant_name", "T908G")))}
    graph, read, again, model, http = setup(v9_cfg, tmp_path, [CASES], {with_tf("GATA1"): [VARIANTS]}, replies,
                                            planner=True, max_rounds=1)
    counts = fill.run(graph, None, read, loop=again)
    done = counts["loop"]
    (first,) = done["rounds"]
    assert (done["planner"], first["plan"]["by"], done["stop"]) == ("model", "planner", "rounds")
    assert [p["action"] for p in first["plan"]["picks"]] == [3]                       # the planner's pick, not code's
    # a TF is kept under its approved symbol, a name that is no gene is dropped, another name of the variant kept
    assert [(p["kind"], p["name"]) for p in first["plan"]["proposals"]] == [("tf", "GATA1"), ("variant_name", "T908G")]
    assert [(p["name"], p["dropped"]) for p in first["plan"]["dropped"]] == [("NOTAGENE", "not an approved gene symbol")]
    assert done["from_memory"] == [{"round": 1, "kind": "tf", "name": "GATA1"},
                                   {"round": 1, "kind": "variant_name", "name": "T908G"}]
    # what ran: the picked entry and the search for what was remembered; never the entry it did not pick
    assert [(e["action"], e["for"], e.get("from_memory", False)) for e in first["effort"]] == [
        ("named", "GENE1", False), ("proposed", "GATA1 (from memory)", True)]
    assert with_tf("TFX") not in again.done and with_tf("GATA1") in again.done
    row = next(r for r in counts["reading"]["articles"] if r["label"] == VARIANTS)
    assert row["loop"] == {"round": 1, "action": "proposed", "for": "GATA1 (from memory)", "from_memory": True}
    # the planner saw the table, the gaps and the menu, and no article text
    packet = next(p for p in model.packets if p.startswith(PLANNER))
    assert "Gaps (code lists them; you add none)" in packet and '3. [G4, G6]' in packet
    assert "2-fold higher" not in packet and "<data>" not in packet
    assert (done["model_calls"], model.packets.count(packet)) == (1, 1)
    # the article that names GATA1 was read by the same blind request, and its record is what states the claim
    assert any(c.relation == "alters_binding" and "GATA1" in c.assertion_text for c in graph.claims.values())


def test_a_remembered_name_with_no_article_behind_it_leaves_no_trace(v9_cfg, tmp_path):
    replies = {**REPLIES, PLANNER: plan(proposals=(("tf", "TAL1"),), note="TAL1 binds here.")}
    graph, read, again, model, _ = setup(v9_cfg, tmp_path / "a", [CASES], {}, replies, planner=True)
    counts = fill.run(graph, None, read, loop=again)
    plain, read2, _, _, _ = setup(v9_cfg, tmp_path / "b", [CASES], {})
    fill.run(plain, None, read2)
    done = counts["loop"]
    assert done["from_memory"] == [{"round": 1, "kind": "tf", "name": "TAL1"}] and done["stop"] == "no_change"
    assert done["rounds"][0]["effort"] == [{**done["rounds"][0]["effort"][0], "for": "TAL1 (from memory)",
                                            "listed": 0, "new": 0, "read": 0, "filed": 0, "from_memory": True}]
    assert cells(T.from_graph(graph)) == cells(T.from_graph(plain)) and chains(T.from_graph(graph)) == chains(
        T.from_graph(plain))
    assert not any("TAL1" in c.assertion_text for c in graph.claims.values())


def test_a_plan_that_breaks_its_form_is_sent_back_once_and_then_code_plans(v9_cfg, tmp_path):
    replies = {**REPLIES, PLANNER: plan(9)}                 # no such menu number, in the reply and in its repair
    graph, read, again, model, _ = setup(v9_cfg, tmp_path, [CASES], {with_tf("TFX"): [VARIANTS]}, replies,
                                         planner=True, max_rounds=1)
    counts = fill.run(graph, None, read, loop=again)
    first = counts["loop"]["rounds"][0]
    assert first["plan"]["by"] == "code" and "the planner gave no usable plan (invalid_output)" in first["plan"]["note"]
    assert counts["loop"]["planner_failures"] == 1
    assert [e["for"] for e in first["effort"]] == ["G001 (TFX) → GENE1", "G001 (TFX)", "GENE1"]
    assert "picks must be menu numbers (1, 2, 3)" in model.corrections[0]


def test_what_the_planner_proposes_is_screened():
    graph = bundle_graph()
    graph.resolver = SYMBOLS
    names = [loop.Proposal(kind="variant_name", name=n, why="") for n in ("T908G", "c.-58A>C", "C228T", "rs123")]
    kept, dropped = loop.screen(graph, names)
    assert [p["name"] for p in kept] == ["T908G", "c.-58A>C"]                         # T>G, on either strand
    assert all("base change" in p["dropped"] for p in dropped) and len(dropped) == 2
    assert loop.other_names(graph, ["T908G", "T 908 G", "C228T", "x" * 60]) == ["T908G"]
    check = loop.checked([loop.Entry(1, "named", [], ""), loop.Entry(2, "named", [], "")])
    for bad, why in ((plan(1, 1), "once"), (plan(3), "menu numbers"),
                     (plan(proposals=(("tf", "A"),) * 4), "at most 3 proposals"),
                     (plan(proposals=(("tf", "x" * 41),)), "1 to 40 characters")):
        with pytest.raises(ValueError, match=why):
            check(loop.RoundPlan(**bad))
    assert check(loop.RoundPlan(**plan())).picks == []                                # picking nothing is allowed


# --- which TF and gene belong together ---------------------------------------------------------------------------------

def test_an_experiment_that_changed_a_tf_and_read_out_a_gene_is_flagged_as_a_join():
    from variant2mechanism.v9.chain import JOIN_FLAG

    def flags(x: dict, **filed: Any) -> dict:
        record = SimpleNamespace(**{"evidence_class": "perturbation", "allele": None, "about_tfs": ["GATA1"],
                                    "about_genes": ["BCL11A"], "result_kind": "effect", "data": {}, **filed})
        return reader.reader_flags(reader.ReadExperiment(**x), record)

    assert flags(KNOCKDOWN) == {JOIN_FLAG: {"tfs": ["GATA1"], "genes": ["BCL11A"]}}
    # the flag holds approved symbols where the article's name has one, so no symbol table is needed to read it
    named = SimpleNamespace(evidence_class="perturbation", allele=None, about_tfs=["gata-1"], about_genes=["Bcl11a"],
                            result_kind="effect", data={})
    known = {"GATA-1": ("GATA1", "HGNC:1"), "BCL11A": ("BCL11A", "HGNC:2")}
    assert reader.reader_flags(reader.ReadExperiment(**KNOCKDOWN), named, lambda n: known.get(n.upper()))[
        JOIN_FLAG] == {"tfs": ["GATA1"], "genes": ["BCL11A"]}
    assert flags(KNOCKDOWN, about_genes=["GATA1", "BCL11A"])[JOIN_FLAG]["genes"] == ["BCL11A"]
    # not a join: the TF's own RNA, a readout that is no gene product, a measured null, an unclear result, and an
    # experiment that changed something other than a TF
    for x, filed in (({}, {"about_genes": ["GATA1"]}), ({"endpoint": "cell proliferation"}, {}),
                     ({}, {"result_kind": "null_in_assessed_scope"}), ({"unclear": True}, {}),
                     ({"manipulated": "element"}, {})):
        assert JOIN_FLAG not in flags({**KNOCKDOWN, **x}, **filed)


def test_a_join_breaks_a_tie_between_equal_chains_and_never_outranks_a_stronger_one(v9_cfg, tmp_path):
    from variant2mechanism.v9.chain import JOIN_FLAG, JOIN_RULE, RANK_RULE, chain_view

    replies = {VARIANTS: reading(EMSA, TAL1_EMSA), CASES: reading(KNOCKDOWN, DELETION)}
    graph, read, _, _, _ = setup(v9_cfg, tmp_path, [CASES, VARIANTS], {}, replies)
    fill.run(graph, None, read)
    (knockdown,) = [e for e in read_records(graph) if JOIN_FLAG in e.data]
    assert knockdown.data[JOIN_FLAG] == {"tfs": ["GATA1"], "genes": ["BCL11A"]}
    ranked = chain_view(graph)["ranked"]
    by_title = {c["title"]: c for c in ranked["chains"]}
    # GATA1 and TAL1 hold the same kinds of evidence. For BCL11A the knock-down puts GATA1 first ...
    gata, tal = by_title["GATA1 → BCL11A"], by_title["TAL1 → BCL11A"]
    assert gata["joined"] == [knockdown.evidence_id] and tal["joined"] == []
    assert (gata["ties"], tal["ties"]) == (1, 1) and tal["rank"] == gata["rank"] + 1
    assert gata["strength"] == tal["strength"]              # nothing but the join separates them
    # ... and for GENE1, which no such experiment names, they still tie for first: a join never outranks a chain
    # with stronger evidence
    assert ranked["leaders"] == 2 and {c["title"] for c in ranked["chains"][:2]} == {"GATA1 → GENE1", "TAL1 → GENE1"}
    assert ranked["rule"] == RANK_RULE + JOIN_RULE and "join" not in ranked
    assert [c.joined for c in T.from_graph(graph).chains if c.title == "GATA1 → BCL11A"] == [[knockdown.evidence_id]]
    # the order can be read from the saved graph alone: a copy without the symbol table gives the same chains
    from variant2mechanism.v9.graph import ClaimGraph as Saved
    again = chain_view(Saved.from_json(graph.to_json()))["ranked"]
    assert [(c["title"], c["rank"], c["joined"]) for c in again["chains"]] == [
        (c["title"], c["rank"], c["joined"]) for c in ranked["chains"]]
    # had the experiment read out GENE1, the tie for first would be broken, and the answer says by what
    knockdown.data[JOIN_FLAG]["genes"].append("GENE1")
    ranked = chain_view(graph)["ranked"]
    assert (ranked["leaders"], ranked["chains"][0]["title"]) == (1, "GATA1 → GENE1")
    assert "changed this chain's TF and saw its gene change" in ranked["join"] and "before 1 chain(s)" in ranked["join"]
    assert "The TF and the gene belong together: 1 experiment(s)" in T.to_markdown(T.from_graph(graph), [])
    # a result the article calls unclear joins nothing
    knockdown.data["unclear_result"] = True
    assert chain_view(graph)["ranked"]["leaders"] == 2


def test_without_a_flagged_experiment_the_order_and_its_rule_are_what_they_were(v9_cfg, tmp_path):
    from variant2mechanism.v9.chain import RANK_RULE, chain_view
    graph, read, _, _, _ = setup(v9_cfg, tmp_path, [VARIANTS], {}, {VARIANTS: reading(EMSA)})
    fill.run(graph, None, read)
    ranked = chain_view(graph)["ranked"]
    assert ranked["rule"] == RANK_RULE and not any("joined" in c for c in ranked["chains"])
    assert "belong together" not in T.to_markdown(T.from_graph(graph), [])


# --- the joiner ---------------------------------------------------------------------------------------------------------

JOINED, JOINED_PMID = "PMC9000012", "90000012"            # the synthetic article on GATA1, TAL1 and GENE1


def joined(tf: str, first: int, direction: str, **more: Any) -> dict:
    return {"location": f"sec1.1/p{first}", "first_sentence": 1, "last_sentence": 1, "organism": "human",
            "tissue_or_cell": "K562 cells", "tf": tf, "gene": "GENE1", "intervention": f"siRNA knockdown of {tf}",
            "endpoint": "GENE1 mRNA by qPCR", "result": f"GENE1 mRNA after {tf} knockdown", "direction": direction,
            "unclear": False, **more}


def join_setup(cfg, tmp: Path, by_tf: dict[str, list[dict]], **settings: Any):
    """A tie between GATA1 and TAL1 for GENE1 (each has an allele-resolved binding assay), and a search of the
    joiner that lists, for each pair, the article in which both TFs were knocked down. `by_tf`: what the scripted
    joiner returns when it reads the article for that TF's pair."""
    replies = {**{f"- transcription factor: {tf}": {"experiments": found, "note": "It knocks two factors down."}
                  for tf, found in by_tf.items()},
               VARIANTS: reading(EMSA, TAL1_EMSA), CASES: reading(DELETION)}
    graph, read, again, model, http = setup(cfg, tmp, [CASES, VARIANTS], {}, replies, **settings)
    record = {**fakes.records()[CASES], "id": JOINED_PMID, "pmid": JOINED_PMID, "pmcid": JOINED,
              "doi": "10.5555/v2m.test.12", "title": "GATA1 knockdown lowers GENE1 expression."}
    http.routes[lit.metadata_url(JOINED, None)] = fakes.search_response([record])
    http.routes[lit.fulltext_url(JOINED)] = fakes.text("oa_join.xml")
    for tf in ("GATA1", "TAL1"):                            # both pairs' searches list the one article
        http.routes[lit.search_url(pair(tf), joiner.JOIN_RESULTS)] = fakes.search_response([record])
    return graph, read, again, model, http


def test_the_joiners_search_names_the_tf_and_the_gene_in_a_title_or_abstract():
    query, held = joiner.join_query(["CEBPA", "CEBPB"], "SORT1")
    assert query.startswith('(TITLE_ABS:"CEBPA" OR TITLE_ABS:"CEBPB") AND TITLE_ABS:"SORT1" AND (knockdown OR ')
    assert held == 2 and len(query) <= lit.QUERY_LIMIT
    query, held = joiner.join_query([f"TF{i}" for i in range(200)], "SORT1")           # a large group: what fits
    assert 5 < held < 200 and len(query) <= lit.QUERY_LIMIT


def test_the_joiner_reads_an_article_that_never_names_the_variant_and_breaks_the_tie(v9_cfg, tmp_path):
    from variant2mechanism.v9.chain import JOIN_FLAG
    graph, read, again, model, http = join_setup(v9_cfg, tmp_path, {"GATA1": [joined("GATA1", 1, "decreases")],
                                                                  "TAL1": [joined("TAL1", 2, "no_change")]})
    counts = fill.run(graph, None, read, loop=again)
    done = counts["loop"]
    first = done["rounds"][0]
    # the gap, and the action that serves it: one search for each pair of the tied chains
    assert [(g["kind"], g["state"]) for g in first["gaps"]][:2] == [("tie", "2 chains tie"), ("join", "2 pair(s)")]
    # the one article is listed for both pairs and read for each: equal effort
    assert [(e["for"], e["listed"], e["new"], e["read"], e["filed"], e["joins"])
            for e in first["effort"] if e["action"] == "join"] == [
        ("GATA1 → GENE1", 1, 1, 1, 1, 1), ("TAL1 → GENE1", 1, 1, 1, 1, 0)]
    # the model was told the pair and shown the passages that name both, and nothing about the variant
    told, other = [p for p in model.packets if p.startswith("Role: joiner")]
    assert "- transcription factor: GATA1" in told and "- gene: GENE1" in told and RSID not in told
    assert "[sec1.1/p1]" in told and "[sec1.1/p2]" not in told and "[sec2/p1]" not in told   # never the retelling
    assert "- transcription factor: TAL1" in other and "[sec1.1/p2]" in other and "[sec1.1/p1]" not in other
    # two records, filed by the reader's own checks: a knock-down that lowered the gene, and a measured null
    filed = [e for e in read_records(graph) if e.source_ids[0].endswith(JOINED_PMID)]
    assert [(e.about_tfs, e.about_genes, e.about_variants, e.evidence_class, JOIN_FLAG in e.data) for e in filed] == [
        (["GATA1"], ["GENE1"], [], "perturbation", True), (["TAL1"], ["GENE1"], [], "perturbation", False)]
    assert filed[0].experiment.passage.startswith("siRNA knockdown of GATA1 in K562 cells lowered GENE1 mRNA")
    assert filed[1].result_kind == "null_in_assessed_scope"                             # a null joins nothing
    # the tie is broken: the chain of the TF and the gene that the experiment names comes first
    assert done["leaders_before"] == ["GATA1 → GENE1", "TAL1 → GENE1"] and done["leaders_after"] == ["GATA1 → GENE1"]
    assert (done["joins"], done["pairs_joined"], done["pairs_searched"]) == (1, ["GATA1 → GENE1"], 2)
    assert "the order of chains changed; the first chains changed" in first["text"]
    assert "1 of them join a TF and a gene" in first["text"]
    table = T.from_graph(graph)
    assert [(c.rank, c.ties, c.title, c.joined) for c in table.chains[:2]] == [
        (1, 1, "GATA1 → GENE1", [filed[0].evidence_id]), (2, 1, "TAL1 → GENE1", [])]
    assert T.check(table, graph) == [] and "belong together: 1 experiment(s)" in T.to_markdown(table, [])
    assert "changed this chain's TF and saw its gene change" in graph.result.summary
    assert "1 show a first chain's TF acting on its gene" in loop.report_view(graph)["lead"]
    # no cell counts a join: the eight claims of the two chains hold what they held
    plain, read2, _, _, _ = setup(v9_cfg, tmp_path / "plain", [CASES, VARIANTS], {},
                                  {VARIANTS: reading(EMSA, TAL1_EMSA), CASES: reading(DELETION)})
    fill.run(plain, None, read2)
    once = cells(T.from_graph(plain))
    assert {k: v for k, v in cells(table).items() if k in once} == once
    # a second round finds the pair joined and does not search it again
    assert not any(e["for"] == "GATA1 → GENE1" for r in done["rounds"][1:] for e in r["effort"])


def test_a_join_needs_sentences_of_the_article_and_a_dry_run_reads_none(v9_cfg, tmp_path):
    # a reply that points outside what was shown is sent back once and then refused: nothing is filed, nothing joins
    wrong = {**joined("GATA1", 1, "decreases"), "location": "sec9/p9"}
    graph, read, again, model, _ = join_setup(v9_cfg, tmp_path / "a", {"GATA1": [wrong], "TAL1": []}, max_rounds=1)
    counts = fill.run(graph, None, read, loop=again)
    assert counts["loop"]["joins"] == 0 and counts["loop"]["leaders_after"] == counts["loop"]["leaders_before"]
    assert any("is not the location id of a passage shown" in c for c in model.corrections)
    graph, read, again, model, _ = join_setup(v9_cfg, tmp_path / "b", {"GATA1": [joined("GATA1", 1, "decreases")]},
                                              dry=True)
    counts = fill.run(graph, None, read, loop=again)
    row = next(e for e in counts["loop"]["rounds"][0]["effort"] if e["for"] == "GATA1 → GENE1")
    assert (row["listed"], row["new"], row["read"]) == (1, 1, 0) and not any(p.startswith("Role: joiner")
                                                                             for p in model.packets)


# --- settings ----------------------------------------------------------------------------------------------------------

def test_the_loop_needs_the_reader_and_a_dry_run_plans_by_code():
    def args(**kw):
        return SimpleNamespace(**{"loop": None, "loop_dry": False, "loop_rounds": None, "loop_articles": None, **kw})

    assert commands.loop_settings(args(), True) is None
    assert commands.loop_settings(args(loop="model"), True) == {"planner": "model", "rounds": 3, "articles": 10,
                                                                "dry": False}
    dry = commands.loop_settings(args(loop="model", loop_dry=True, loop_rounds=1), True)
    assert dry == {"planner": "code", "rounds": 1, "articles": 10, "dry": True}
    assert commands.loop_room(dry) == 1 * (10 + loop.FOLLOW_REVIEWS)
    for bad, why in ((args(loop="code"), "needs --read"), (args(loop_dry=True), "need --loop"),
                     (args(loop="code", loop_rounds=0), "at least 1")):
        with pytest.raises(ValueError, match=why):
            commands.loop_settings(bad, bad.loop != "code" or bad.loop_rounds == 0)
    parts = fill.manifest_parts({"driver": fill.READER_DRIVER, "loop": {"rounds": [1], "stop": "rounds"}},
                                loop=loop.manifest_parts(None, loop.Loop()))
    assert parts["loop"]["planner"] == "code" and parts["counts"]["loop"] == {"stop": "rounds"}
    assert loop.manifest_parts(None, loop.Loop())["actions"] == list(loop.KINDS)


def test_a_graph_scratch_block_always_puts_the_graph_back():
    graph = ClaimGraph(bundle_graph().case)
    before = (len(graph.events), graph.version)
    with graph.scratch():
        graph.log("collect_facts", "code", "something that will not be kept")
        assert len(graph.events) == before[0] + 1
    assert (len(graph.events), graph.version) == before
    with pytest.raises(RuntimeError, match="inside a batch"), graph.batch(), graph.scratch():
        pass
