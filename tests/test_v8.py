"""v8: ChIP grades, intake, the family screen, link tiers, ranking and the verdict, schemas, literature tags, and an
end-to-end run with a fake model (data-marked: it reads the local HTTP cache)."""

import json
from types import SimpleNamespace

import numpy as np
import pandas as pd
import pytest

from variant2mechanism.agent.schemas import SchemaCheckError
from variant2mechanism.context.base import ToolResult
from variant2mechanism.v8 import families as F
from variant2mechanism.v8 import tiers as T
from variant2mechanism.v8.chipgrade import Chip, name_match
from variant2mechanism.v8.intake import disease_line, minor_allele_frequency, trait_matches
from variant2mechanism.v8.pubtator import _papers, chain_tags
from variant2mechanism.v8.schemas import ChainV8, LinkV8, check_chains
from variant2mechanism.v8.sitescore import _sums, creates_site

STEPS = ["binding", "element", "gene", "cell_type", "phenotype"]


def test_biosample_names_match_without_false_friends():
    assert name_match("HCT116", "HCT-116")
    assert name_match("LNCaP", "LNCaP clone FGC")
    assert not name_match("HEL", "HeLa-S3")          # short names must be equal
    assert not name_match("", "HepG2")


def test_overlapping_kmer_sums_and_site_creation():
    coef = np.arange(16, dtype=float)                # k = 2: AA=0, AC=1, ..., TT=15
    x = np.array([[0, 1, 2]])                        # ACG -> AC (1) + CG (6)
    assert _sums(coef, x, 2).tolist() == [7.0]
    assert creates_site({"ref": 80.0, "alt": 99.0}, "alt")
    assert not creates_site({"ref": 92.0, "alt": 99.0}, "alt")
    assert not creates_site(None, "alt")


def chip_with(peaks, here=("HCT116",), encode=None, assayed=None):
    occ = SimpleNamespace(peaks_of=lambda tf: (encode or {}).get(tf, []), assayed=assayed or {})
    return Chip(100, peaks, occ, list(here))


def peak(tf, cell, d, window=50):
    return {"tf": tf, "biosample": cell, "summit_distance": d, "inside": True, "window": window, "dataset": "x"}


def test_chip_grades_here_and_anywhere():
    chip = chip_with([peak("TCF7L2", "HCT-116", 7), peak("TCF7", "HepG2", 30), peak("SP1", "HCT116", 63)],
                     encode={"SRF": [{"biosample": "HCT116"}]}, assayed={"SRF": {"HCT116"}})
    assert (chip.member("TCF7L2")["grade_here"], chip.member("TCF7L2")["grade_any"]) == (1, 1)
    assert (chip.member("TCF7")["grade_here"], chip.member("TCF7")["grade_any"]) == (3, 1)
    assert chip.member("SP1")["grade_here"] == 2                 # summit 63 bp: inside the extended peak only
    assert chip.member("SRF")["grade_here"] == 2 and chip.member("SRF")["encode_here"]
    assert chip.member("LEF1")["grade_any"] == 3


def test_traits_match_the_disease():
    assert trait_matches("Colorectal cancer or advanced adenoma", "Colorectal cancer (8q24)")
    assert trait_matches("LDL cholesterol levels", "LDL cholesterol, myocardial infarction (SORT1)")
    assert trait_matches("Body mass index", "Obesity (FTO)")
    assert not trait_matches("Prostate-specific antigen levels", "Colorectal cancer (8q24)")
    assert not trait_matches("Breast size", "Breast cancer (16q12)")


def tool(full, ok=True):
    return ToolResult("t", {}, "s", full, "src", "", "genetic", ok=ok)


def test_disease_line_states():
    va = tool([{"colocated_variants": [{"id": "rs1", "frequencies": {"T": {"gnomadg": 0.38}}}]}])
    gwas = tool([{"reported_trait": ["Colorectal cancer"], "p_value": 2e-122, "snp_allele": [{"effect_allele": "T"}]}])
    none = tool([])
    fm = tool({"gwas": [], "qtl": [], "best_l2g": {}})
    assert minor_allele_frequency(va.full, "T") == 0.38
    assert disease_line("germline", "Colorectal cancer", gwas, fm, va, "T")["state"] == "supported"
    assert disease_line("germline", "Colorectal cancer", none, fm, va, "T")["state"] == "no_association"
    rare = tool([{"colocated_variants": [{"id": "rs1", "frequencies": {"T": {"gnomadg": 0.001}}}]}])
    assert disease_line("germline", "Colorectal cancer", none, fm, rare, "T")["state"] == "not_testable"
    assert disease_line("somatic", "Glioblastoma", None, None, None, "T")["state"] == "not_testable"
    assert disease_line("germline", "X", tool(None, ok=False), tool(None, ok=False), va, "T")["state"] == "unknown"
    # one source empty and the other failed, or no frequency: unknown, never an absence that vetoes a mechanism
    down = tool(None, ok=False)
    assert disease_line("germline", "Colorectal cancer", none, down, va, "T")["state"] == "unknown"
    assert disease_line("germline", "Colorectal cancer", down, fm, va, "T")["state"] == "unknown"
    assert disease_line("germline", "Colorectal cancer", none, fm, tool([{}]), "T")["state"] == "unknown"
    assert disease_line("germline", "Colorectal cancer", gwas, down, va, "T")["state"] == "supported"


class FakeExpression:
    def __init__(self, tpm):
        self.tpm = tpm

    def tf_expression(self, tfs, ctx):
        return {t: {"tpm": self.tpm.get(t)} for t in tfs}


def screen_inputs():
    groups = {"groups": [{"id": "G1", "label": "HMG/Sox, 2 models", "models": ["m_lef1", "m_tcf7"],
                          "tfs": ["LEF1", "TCF7", "TCF7L2"]},
                         {"id": "G2", "label": "C2H2 ZF, 1 model", "models": ["m_sp"], "tfs": ["SP1", "SP3"]},
                         {"id": "G3", "label": "Homeodomain, 1 model", "models": ["m_hox"], "tfs": ["HOXB13"]}]}
    scores = pd.DataFrame([{"model": "m_lef1", "z": -4.7, "effect": -0.47, "status": "ok"},
                           {"model": "m_tcf7", "z": -4.2, "effect": -0.2, "status": "ok"},
                           {"model": "m_sp", "z": -9.0, "effect": -0.2, "status": "ok"},
                           {"model": "m_hox", "z": 100.0, "effect": 4.0, "status": "ok"}])
    reg = SimpleNamespace(cognate_tf={"m_lef1": "LEF1", "m_tcf7": "TCF7", "m_sp": "SP4", "m_hox": "HOXB13"})
    expr = FakeExpression({"LEF1": 0.04, "TCF7": 19.5, "TCF7L2": 63.6, "SP1": 39.0, "SP3": 62.7, "HOXB13": 0.1})
    chip = chip_with([peak("TCF7L2", "HCT116", 7), peak("TCF7", "HepG2", 7), peak("SP1", "HCT116", 63)])
    return groups, reg, scores, expr, chip


def test_family_screen_orders_by_chip_then_z_and_names_one_member():
    groups, reg, scores, expr, chip = screen_inputs()
    ctx = SimpleNamespace(kind="depmap_line")
    out = F.family_screen(groups, reg, scores, 4.05, expr, ctx, chip)
    fams = out["families"]
    assert [f["gid"] for f in fams] == ["G1", "G2"]          # HOXB13 is not expressed in the line: no candidate
    assert fams[0]["named"] == "TCF7L2" and fams[0]["binds_more"] == "ref"
    assert "LEF1" not in [m["tf"] for m in fams[0]["members"]]   # 0.04 TPM in a cell line
    assert fams[0]["fid"] == "F1" and fams[1]["named"] == "SP1"
    ablated = F.family_screen(groups, reg, scores, 4.05, expr, ctx, chip, drop={"TCF7L2"})
    assert ablated["families"][1]["named"] == "TCF7"          # the gold member is gone; its family stays
    no_ctx = F.family_screen(groups, reg, scores, 4.05, expr, None, chip)
    assert "G3" in [f["gid"] for f in no_ctx["families"]]     # no context: expression unknown, nothing dropped


def chain(cid, fid, tf, allele="ref", gene="MYC"):
    return ChainV8(id=cid, title=tf, family_id=fid, tf=tf, member_reason="", allele_binding_more=allele,
                   element="e", target_gene=gene, cell_type="c",
                   links=[LinkV8(step=s, claim=s, evidence_ids=["E01"]) for s in STEPS], predictions=[],
                   falsified_if=[])


def facts_for(fams, element=None, disease="supported"):
    return T.Facts(use_qbic=True, families=fams, element=element or {"in_ccre": True, "status": "active",
                                                                     "here": [("HCT116", "pELS")]},
                   disease={"state": disease, "reason": "r"}, promoter={"promoter_of": []},
                   links={"3d": [{"gene": "MYC", "method": "Intact-HiC", "biosample": "HCT116"}], "eqtl": [],
                          "crispr": []}, here_names=["HCT116"], l2g={"POU5F1B": 0.89})


def test_tiers_ranking_and_verdict():
    groups, reg, scores, expr, chip = screen_inputs()
    fams = F.family_screen(groups, reg, scores, 4.05, expr, SimpleNamespace(kind="depmap_line"), chip)["families"]
    facts = facts_for(fams)
    h1, h2 = chain("H1", "F1", "TCF7L2"), chain("H2", "F2", "SP1", gene="POU5F1B")
    t1, t2 = T.chain_tiers(facts, h1), T.chain_tiers(facts, h2)
    assert t1["binding"]["tier"] == 3 and t1["gene"]["tier"] == 2 and t1["element"]["tier"] == 3
    assert t2["binding"]["tier"] == 2 and t2["gene"]["tier"] == 1
    wrong = T.chain_tiers(facts, chain("H3", "F1", "TCF7L2", allele="alt"))
    assert wrong["binding"]["tier"] == -1
    tiers = {"H1": t1, "H2": t2}
    mins = {h.id: T.minimum(facts, h, tiers[h.id]) for h in (h1, h2)}
    ranked = T.rank([h2, h1], tiers, mins, {}, {"F1": 0, "F2": 1})
    assert [h.id for h in ranked] == ["H1", "H2"]
    v = T.verdict(ranked, mins, facts, 2)
    assert v["tf"]["verdict"] == "mechanism" and v["overall"]["verdict"] == "mechanism"
    v_noassoc = T.verdict(ranked, mins, facts_for(fams, disease="no_association"), 2)
    assert v_noassoc["tf"]["verdict"] == "mechanism" and v_noassoc["overall"]["verdict"] == "no mechanism"
    inactive = facts_for(fams, element={"in_ccre": False})
    ti = {h.id: T.chain_tiers(inactive, h) for h in (h1, h2)}
    elim = T.code_eliminations([h1, h2], ti)
    assert set(elim) == {"H1", "H2"}
    assert T.verdict([], {}, inactive, 2)["tf"]["verdict"] == "no mechanism"


def test_a_failed_ccre_lookup_is_never_a_contradiction():
    from variant2mechanism.v8.run import ccre_location
    local = {"accession": "EH38E1", "class": "dELS", "start": 1, "end": 300, "distance": 0}
    screen_down = ToolResult("ccre_lookup", {}, "SCREEN cre_table lookup failed: HTTP 403",
                             {"local": local, "screen_error": "HTTP 403"}, "s", "", "epigenomic", ok=False)
    assert ccre_location(screen_down) == (True, local)                  # the local registry still answered
    assert ccre_location(tool({"error": "x"}, ok=False)) == (False, None)
    groups, reg, scores, expr, chip = screen_inputs()
    fams = F.family_screen(groups, reg, scores, 4.05, expr, SimpleNamespace(kind="depmap_line"), chip)["families"]
    h1 = chain("H1", "F1", "TCF7L2")
    failed = facts_for(fams, element={"status": "failed", "in_ccre": False})
    tiers = {"H1": T.chain_tiers(failed, h1)}
    assert tiers["H1"]["element"]["tier"] == 0 and T.code_eliminations([h1], tiers) == {}
    bound = facts_for(fams, element={"status": "failed", "in_ccre": False, "bound_here": True})
    assert T.chain_tiers(bound, h1)["element"]["tier"] == 1
    absent = facts_for(fams, element={"status": "no_ccre", "in_ccre": False})
    assert T.chain_tiers(absent, h1)["element"]["tier"] == -1           # a real absence still counts against


def test_chain_checks():
    groups, reg, scores, expr, chip = screen_inputs()
    fams = F.family_screen(groups, reg, scores, 4.05, expr, SimpleNamespace(kind="depmap_line"), chip)["families"]
    assert len(check_chains([chain("H1", "F1", "TCF7L2"), chain("H2", "F2", "SP1")], fams, 2)) == 2
    with pytest.raises(SchemaCheckError, match="give member_reason"):
        check_chains([chain("H1", "F1", "TCF7"), chain("H2", "F2", "SP1")], fams, 2)
    with pytest.raises(SchemaCheckError, match="not a member"):
        check_chains([chain("H1", "F1", "GATA3"), chain("H2", "F2", "SP1")], fams, 2)
    with pytest.raises(SchemaCheckError, match="one chain per family"):
        check_chains([chain("H1", "F1", "TCF7L2"), chain("H2", "F1", "TCF7L2")], fams, 2)


def test_a_family_swap_keeps_its_reason():
    groups, reg, scores, expr, chip = screen_inputs()
    fams = F.family_screen(groups, reg, scores, 4.05, expr, SimpleNamespace(kind="depmap_line"), chip)["families"]
    why = "the SP family has the summit in the context"
    swapped = check_chains([chain("H1", "F2", "SP1").model_copy(update={"member_reason": why})], fams, 1, {"F1"})
    assert swapped[0].member_reason == why            # F2 replaced the F1 asked for: the reason says why
    asked = check_chains([chain("H1", "F2", "SP1").model_copy(update={"member_reason": why})], fams, 1, {"F2"})
    assert asked[0].member_reason == ""               # F2 was asked for and SP1 is code's member: no switch


def test_unknown_evidence_ids_are_refused_with_one_retry(agent_cfg):
    from fake_llm import message

    from variant2mechanism.agent.llm import LLMClient
    from variant2mechanism.v8.schemas import ChainsV8, CritiqueV8, check_critique
    groups, reg, scores, expr, chip = screen_inputs()
    fams = F.family_screen(groups, reg, scores, 4.05, expr, SimpleNamespace(kind="depmap_line"), chip)["families"]
    made_up = chain("H1", "F1", "TCF7L2")
    made_up.links[0].evidence_ids = ["E999"]
    with pytest.raises(SchemaCheckError, match="E999"):
        check_chains([made_up], fams, 1, known={"E01"})
    good = chain("H1", "F1", "TCF7L2")
    replies = [message(json.dumps({"chains": [c.model_dump() for c in (made_up,)]})),
               message(json.dumps({"chains": [good.model_dump()]}))]
    calls = []
    res = LLMClient(agent_cfg, transport=lambda p: (calls.append(p), replies.pop(0))[1]).call(
        "generator", "generate", "s", [{"role": "user", "content": "x"}], output_model=ChainsV8,
        check=lambda c: ChainsV8(chains=check_chains(c.chains, fams, 1, {"F1"}, {"E01"})))
    assert len(calls) == 2 and "E999" in calls[1]["messages"][-1]["content"]
    assert res.parsed.chains[0].links[0].evidence_ids == ["E01"]
    critique = CritiqueV8.model_validate({
        "grades": [{"hypothesis_id": "H1", "step": s, "status": "weak", "reason": "r"} for s in STEPS],
        "problems": [], "eliminations": [{"hypothesis_id": "H1", "evidence_ids": ["E777"], "reason": "r"}],
        "checks": [], "next_experiment": ""})
    with pytest.raises(SchemaCheckError, match="E777"):
        check_critique(critique, [good], {"E01"})
    assert check_critique(critique, [good]).eliminations[0].evidence_ids == ["E777"]   # no ledger given: no check


def test_pubtator_entities_and_chain_flags():
    doc = {"pmid": 19561607, "date": "2009-08-01T00:00:00Z", "journal": "Nat Genet", "passages": [
        {"infons": {"type": "title"}, "text": "The 8q24 variant rs6983267 interacts with MYC", "annotations": [
            {"infons": {"type": "Variant", "identifier": "tmVar:rs6983267;RS#:6983267"}, "text": "rs6983267"},
            {"infons": {"type": "Gene", "name": "MYC"}, "text": "MYC"}]},
        {"infons": {"type": "abstract"}, "text": "TCF7L2 binds the risk allele.", "annotations": [
            {"infons": {"type": "Gene", "name": "TCF7L2"}, "text": "TCF7L2"},
            {"infons": {"type": "Disease", "name": "Colorectal Neoplasms"}, "text": "colorectal cancer"}]}]}
    p = _papers([doc])["19561607"]
    assert p["variants"] == ["rs6983267"] and {"MYC", "TCF7L2"} <= set(p["genes"]) and p["year"] == "2009"
    tags = chain_tags(p, "rs6983267", ["TCF7L2"], ["MYC"], "Colorectal cancer")
    assert tags["flags"] == ["variant and TF", "complete chain"]
    assert chain_tags(p, "rs6983267", ["GATA3"], ["MYC"], "Colorectal cancer")["flags"] == []


class FakeLiteratureHttp:
    """PubTator3 up or down; Europe PMC up or down, with a 2026 paper that holds the answer, a 2005 one and one
    with no date."""

    def __init__(self, pubtator_ok=True, epmc_ok=True):
        self.pubtator_ok, self.epmc_ok, self.urls = pubtator_ok, epmc_ok, []

    def get(self, url, timeout=None, **kw):
        self.urls.append(url)
        down = SimpleNamespace(ok=False, data=None, url=url, retrieved_utc=None, error="HTTP 503", retryable=True)

        def ok(data):
            return SimpleNamespace(ok=True, data=data, url=url, retrieved_utc=None, error=None, retryable=False)
        if "pubtator3-api/search" in url:
            return ok({"count": 2, "total_pages": 1, "results": [{"pmid": 111, "date": "2026-03-01T00:00:00Z"},
                                                                 {"pmid": 222, "date": "2008-05-01T00:00:00Z"}]}) \
                if self.pubtator_ok else down
        if "pubtator3-api/publications/export" in url:
            return ok({"PubTator3": [{"pmid": 222, "date": "2008-05-01", "passages": [
                {"infons": {"type": "title"}, "text": "An old paper"}]}]})
        return ok({"hitCount": 3, "resultList": {"result": [
            {"pmid": "999", "title": "A 2026 paper that holds the answer", "firstPublicationDate": "2026-02-01",
             "pubYear": "2026"},
            {"pmid": "888", "title": "A 2005 paper", "firstPublicationDate": "2005-06-01", "pubYear": "2005"},
            {"pmid": "777", "title": "A paper with no date"}]}}) if self.epmc_ok else down


def test_the_literature_cutoff_holds_when_pubtator_fails():
    from variant2mechanism.context.literature import literature_search
    from variant2mechanism.v8.pubtator import pubtator_search
    up = pubtator_search(SimpleNamespace(http=FakeLiteratureHttp()), "GENE disease", before="2010-01-01")
    assert [p["pmid"] for p in up.full] == ["222"]
    http = FakeLiteratureHttp(pubtator_ok=False)
    fallback = pubtator_search(SimpleNamespace(http=http), "GENE disease", masked=True, before="2010-01-01")
    assert [p["pmid"] for p in fallback.full] == ["888"]          # the 2026 paper and the undated one are dropped
    assert "FIRST_PDATE%3A%5B1800-01-01%20TO%202009-12-31%5D" in http.urls[-1]
    assert fallback.summary.startswith("PubTator3 failed; Europe PMC instead.")
    both = pubtator_search(SimpleNamespace(http=FakeLiteratureHttp(False, False)), "GENE disease", before="2010-01-01")
    assert both.status == "failed"
    plain = literature_search(SimpleNamespace(http=FakeLiteratureHttp()), "GENE disease")   # no cut-off: the same
    assert plain.url.endswith("?query=GENE%20disease&format=json&pageSize=8&resultType=core")   # request as before
    assert [p["pmid"] for p in plain.full] == ["999", "888", "777"]


# -- an end-to-end run with a fake model (needs the local HTTP cache and data folder) -------------------------------


class FakeTransport8:
    """Answers each v8 schema: chains for the families the prompt asks for, grades with one check, then a regrade."""

    def __init__(self):
        self.calls = []

    def __call__(self, params):
        self.calls.append(params)
        title = params["response_format"]["json_schema"]["schema"].get("title")
        user = next(m["content"] for m in params["messages"] if m["role"] == "user")
        if title == "ChainsV8":
            import re
            rows = re.findall(r"- (F\d+) \(.*?\): code names ([A-Z0-9-]+)", user)
            out = {"chains": [chain(f"H{i}", fid, tf).model_dump() for i, (fid, tf) in enumerate(rows, 1)]}
        elif title == "CritiqueV8":
            ids = sorted(set(re.findall(r'"id":"(H\d+)"', user))) if (re := __import__("re")) else []
            first = sum(1 for c in self.calls if c["response_format"]["json_schema"]["schema"].get("title") == title) == 1
            out = {"grades": [{"hypothesis_id": h, "step": s, "status": "weak", "reason": "fake"} for h in ids
                              for s in STEPS], "problems": ["fake problem"], "eliminations": [],
                   "checks": ([{"tool": "gene_disease", "args_json": json.dumps({"gene": "MYC"}),
                                "resolves": "H1.phenotype", "why": "fake"}] if first else []),
                   "next_experiment": "an allele-specific EMSA"}
        elif title == "Quotes":
            out = {"quotes": []}
        elif title == "Comparison":
            out = {"winner": "neither", "reason": "fake", "evidence_ids": []}
        else:
            out = {"chains": [{"tf": "TCF7L2", "allele_binding_more": "ref", "target_gene": "MYC", "reason": "x"}]}
        return {"id": "fake", "model": "fake", "choices": [{"finish_reason": "stop", "message": {
            "role": "assistant", "content": json.dumps(out)}}], "usage": {"prompt_tokens": 1000, "completion_tokens": 200}}


@pytest.mark.data
def test_v8_run_end_to_end_with_a_fake_model(agent_cfg, tmp_path):
    from variant2mechanism.agent.case import load_gold_case
    from variant2mechanism.config import load_config
    from variant2mechanism.context.http import Http
    from variant2mechanism.qbic.tools import QbicTools
    from variant2mechanism.v8.run import run_case8
    real = load_config()
    cfg = agent_cfg
    cfg["v8"] = real["v8"]
    cfg["data"] = {**cfg["data"], "screen_dir": real["data"]["screen_dir"]}
    cfg["llm"] = {**cfg["llm"], "prices_per_mtok": {**cfg["llm"]["prices_per_mtok"], "fake": {"input": 1, "output": 1}}}
    http = Http(real.path("tools", "http_cache"), offline=True)
    t = FakeTransport8()
    r = run_case8(load_gold_case("rs6983267"), arm="full", masked=True, cfg=cfg, transport=t, http=http,
                  qbic=QbicTools(real), run_dir=tmp_path / "run")
    assert r["verdict"]["tf"]["verdict"] in ("mechanism", "undetermined", "no mechanism")
    assert r["chains"] and r["chains"][0]["tiers"]["binding"]["name"]
    assert [x["tool"] for x in r["lookups"]] == ["gene_disease"]
    assert (tmp_path / "run" / "report.html").exists()
    titles = [c["response_format"]["json_schema"]["schema"].get("title") for c in t.calls]
    assert titles.count("CritiqueV8") == 2 and "ChainsV8" in titles


def test_memory_test_prompts_exist():
    from variant2mechanism.v8.evaluation import ARMS
    from variant2mechanism.v8.run import PROMPTS, SINGLE_PROMPTS
    for system, task in SINGLE_PROMPTS.values():
        assert (PROMPTS / f"{system}.txt").exists() and (PROMPTS / f"{task}.txt").exists()
    assert ARMS["single_rules"]["prompts"] in SINGLE_PROMPTS and "prompts" not in ARMS["single"]
