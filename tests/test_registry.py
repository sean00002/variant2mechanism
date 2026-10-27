import pytest

pytestmark = pytest.mark.data


@pytest.fixture(scope="module")
def reg():
    from variant2mechanism.qbic.registry import get_registry
    return get_registry()


@pytest.fixture(scope="module")
def groups(reg):
    from variant2mechanism.qbic.registry import compute_groups
    reg._groups = compute_groups(reg, 0.5)
    return reg._groups


def tfs_of(reg, group):
    return sorted(reg.cognate_tf[m] for m in group["models"])


def test_experiment_label_resolves(reg):
    r = reg.resolve_tf("Tcfap2a")
    assert (r["status"], r["symbol"], r["via"]) == ("ok", "TFAP2A", "qbic_label")
    assert reg.coverage("TFAP2A")["own_model"] == "TCFAP2A_NA_TGATCC20NCG_ESP_yang2017_0_4_7mer"
    assert reg.resolve_tf("T")["symbol"] == "TBXT"
    assert reg.resolve_tf("NURR1")["symbol"] == "NR4A2"
    assert reg.resolve_tf("gabpa")["symbol"] == "GABPA"


def test_tcf4_is_tcf4_with_a_note(reg):
    r = reg.resolve_tf("TCF4")
    assert (r["symbol"], r["via"]) == ("TCF4", "hgnc_symbol")
    assert any("TCF7L2" in n for n in r["notes"])


def test_tcf7l2_is_mapped_through_one_group_of_three(reg, groups):
    cov = reg.coverage("TCF7L2")
    assert cov["status"] == "mapped" and cov["own_model"] is None
    assert sorted(reg.cognate_tf[m] for m in cov["mapped_models"]) == ["LEF1", "TCF7", "TCF7L1"]
    (g,) = reg.groups_of_tf("TCF7L2")
    assert tfs_of(reg, g) == ["LEF1", "TCF7", "TCF7L1"]


def test_gold_set_groups(reg, groups):
    assert reg.coverage("GABPA")["status"] == "tf"
    assert len(reg.group_of_model(reg.own_model["GABPA"])["models"]) == 18
    assert tfs_of(reg, reg.group_of_model(reg.own_model["HOXB13"])) == ["HOXA13", "HOXB13", "HOXC13", "HOXD13"]
    g1, g3 = reg.group_of_model(reg.own_model["GATA1"]), reg.group_of_model(reg.own_model["GATA3"])
    assert g1["id"] == g3["id"] and len(g1["models"]) == 6
    assert len(reg.group_of_model(reg.own_model["CEBPA"])["models"]) == 3


def test_not_in_coverage(reg):
    for tf in ("ARID5B", "TAL1"):
        assert reg.coverage(tf) == {"status": "not_in_coverage", "own_model": None, "mapped_models": []}


def test_group_counts(groups):
    assert groups["summary"] == {"n_groups": 631, "n_singletons": 525, "largest": [81, 29]}
    multi = [g for g in groups["groups"] if len(g["dbd_labels"]) > 1]
    assert {frozenset(g["dbd_labels"]) for g in multi} == {frozenset({"Ets", "Ets; AT hook"}),
                                                            frozenset({"Paired box", "Homeodomain; Paired box"})}


@pytest.mark.parametrize("name,expected", [("NRF2", ["GABPA", "NFE2L2"]), ("NF-E1", ["GATA1", "YY1"])])
def test_shared_alias_is_ambiguous(reg, name, expected):
    r = reg.resolve_tf(name)
    assert r["status"] == "ambiguous" and r["symbol"] is None
    assert [c["symbol"] for c in r["candidates"]] == expected


def test_unknown_name(reg):
    assert reg.resolve_tf("NOTAGENE123")["status"] == "unknown_name"


def test_committed_groups_json_matches(reg, groups):
    import json

    from variant2mechanism.config import load_config
    path = load_config().path("cache", "groups")
    assert json.loads(path.read_text())["summary"] == groups["summary"]
