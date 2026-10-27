import numpy as np
import pandas as pd
import pytest

from variant2mechanism.qbic.expression import ContextError, Expression, tpm_from_log


@pytest.fixture
def expr():
    log = pd.DataFrame({"TF_A": [np.log2(11), np.log2(3), np.log2(5)], "TF_B": [0.0, 1.0, np.log2(2.5)],
                        "NOTTF": [5.0, 5.0, 5.0]}, index=["ACH-1", "ACH-2", "ACH-3"])
    depmap = pd.DataFrame(tpm_from_log(log.to_numpy()), index=log.index, columns=log.columns)
    subtype = pd.Series({"ACH-1": "Glioblastoma", "ACH-2": "Glioblastoma", "ACH-3": "Melanoma"})
    gtex = pd.DataFrame({"Liver": [2.0, 0.5], "Brain - Caudate (basal ganglia)": [1.0, 4.0]}, index=["TF_A", "TF_B"])
    return Expression(depmap, subtype, gtex, {"TF_A", "TF_B"})


def test_log2_tpm_plus_one():
    assert tpm_from_log(np.log2(11.0)) == pytest.approx(10.0)
    assert tpm_from_log(0.0) == 0.0


def test_depmap_line(expr):
    r = expr.tf_expression(["TF_A", "TF_B"], "DepMap:ACH-1 (line one)")
    assert r["TF_A"]["tpm"] == 10.0 and r["TF_A"]["rank_among_tfs"] == 1 and r["TF_A"]["n_tfs"] == 2
    assert r["TF_A"]["percentile_across_contexts"] == 100.0
    assert r["TF_B"]["tpm"] == 0.0 and r["TF_B"]["rank_among_tfs"] == 2


def test_subtype_median_and_n_lines(expr):
    r = expr.tf_expression(["TF_A"], "DepMap:subtype=Glioblastoma (median of 2 lines)")
    assert r["TF_A"]["tpm"] == 6.0 and r["TF_A"]["n_lines"] == 2     # median of 10 and 2


def test_gtex_tissue_with_brackets_in_its_name(expr):
    assert expr.tf_expression(["TF_B"], "GTEx:Brain - Caudate (basal ganglia)")["TF_B"]["tpm"] == 4.0
    assert expr.tf_expression(["TF_A"], "GTEx:Liver (proxy for hepatocytes)")["TF_A"]["tpm"] == 2.0


def test_none_skips(expr):
    assert expr.parse("none (no matching tissue)").kind == "none"
    assert expr.parse("").kind == "none"
    assert expr.tf_expression(["TF_A"], None)["TF_A"]["tpm"] is None


@pytest.mark.parametrize("ctx", ["DepMap:ACH-999", "DepMap:subtype=Nothing", "GTEx:Moon", "CCLE:HCT116"])
def test_unknown_context_is_a_clear_error(expr, ctx):
    with pytest.raises(ContextError):
        expr.parse(ctx)


@pytest.mark.data
def test_real_glioblastoma_median():
    from variant2mechanism.qbic.expression import get_expression
    r = get_expression().tf_expression(["GABPA"], "DepMap:subtype=Glioblastoma (median of 54 lines)")
    assert r["GABPA"]["n_lines"] == 54 and r["GABPA"]["tpm"] > 1
    assert r["GABPA"]["n_tfs"] > 1500
