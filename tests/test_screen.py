import json

import numpy as np
import pandas as pd
import pytest
from scipy.stats import norm

from variant2mechanism.qbic.expression import Expression
from variant2mechanism.qbic.screen import ScreenSettings, screen_rows
from variant2mechanism.qbic.tools import fit

N = 997
THR = 0.05 / N


class FakeLookup:
    """Models m0..m{n}; groups given as {group_id: ([models], [tfs])}."""

    def __init__(self, groups):
        self.groups = {gid: {"id": gid, "label": f"Fam {gid}, {len(ms)} models", "models": ms, "tfs": tfs}
                       for gid, (ms, tfs) in groups.items()}
        self.by_model = {m: g for g in self.groups.values() for m in g["models"]}
        self.cognate_tf = {m: f"TF_{m}" for m in self.by_model}
        self.quality = {m: {"cross_exp_pearsonr": 0.8} for m in self.by_model}

    def group_of_model(self, model_id):
        return self.by_model[model_id]


def rows(spec, n_total=N):
    """spec: {model: p (signed: negative p means a negative effect)}; the rest are null rows."""
    recs = []
    for m, sp in spec.items():
        p = abs(sp)
        z = float(norm.isf(p / 2)) * np.sign(sp)
        recs.append({"model": m, "effect": 0.1 * z, "z": z, "p": p, "status": "ok"})
    for i in range(n_total - len(spec)):
        recs.append({"model": f"null{i}", "effect": 0.01, "z": 0.5, "p": 0.6, "status": "ok"})
    return pd.DataFrame(recs)


def expression(tpm):
    """tpm: {tf: TPM} for one DepMap line ACH-1."""
    df = pd.DataFrame([tpm], index=["ACH-1"])
    return Expression(df, pd.Series({"ACH-1": "X"}), pd.DataFrame(index=list(tpm)), set(tpm))


def lookup_with_nulls(groups, n_nulls):
    lk = FakeLookup(groups)
    for i in range(n_nulls):
        lk.by_model[f"null{i}"] = {"id": f"N{i}", "label": "null", "models": [f"null{i}"], "tfs": []}
    return lk


def test_gate_just_above_and_below_threshold():
    lk = lookup_with_nulls({"A": (["a"], ["TA"]), "B": (["b"], ["TB"])}, N)
    out = screen_rows(rows({"a": THR * 0.99, "b": THR * 1.01}), lk, N)
    assert out["n_pass"] == 1 and [g["best_model"] for g in out["groups"]] == ["a"]
    assert out["threshold"]["abs_z"] == pytest.approx(4.05, abs=0.01)
    assert out["context"] == "none: expression filter skipped"


def test_grouping_best_model_and_mixed_directions():
    lk = lookup_with_nulls({"E": (["e1", "e2", "e3"], ["T1", "T2"]), "F": (["f1"], ["T3"])}, N)
    out = screen_rows(rows({"e1": 1e-9, "e2": 1e-12, "e3": -1e-7, "f1": 1e-8}), lk, N)
    g = out["groups"][0]
    assert g["group"] == "E" and g["best_model"] == "e2" and g["n_pass"] == 3
    assert g["n_same_sign"] == 2 and g["mixed_directions"] is True and g["direction"] == "alt binds more"
    assert out["groups"][1]["mixed_directions"] is False


def test_group_kept_if_any_tf_expressed():
    lk = lookup_with_nulls({"K": (["k"], ["LOW", "HIGH"]), "D": (["d"], ["OFF"])}, N)
    ex = expression({"LOW": 0.2, "HIGH": 1.0, "OFF": 0.5})
    out = screen_rows(rows({"k": 1e-9, "d": 1e-12}), lk, N, ex, "DepMap:ACH-1 (line)")
    assert [g["group"] for g in out["groups"]] == ["K"]
    assert out["groups"][0]["tfs"][0] == {"tf": "HIGH", "tpm": 1.0, "rank": 1}
    assert out["dropped_by_expression"]["count"] == 1 and out["dropped_by_expression"]["top"][0]["group"] == "D"


def test_context_none_skips_filter():
    lk = lookup_with_nulls({"D": (["d"], ["OFF"])}, N)
    out = screen_rows(rows({"d": 1e-12}), lk, N, expression({"OFF": 0.0}), "none (no tissue)")
    assert [g["group"] for g in out["groups"]] == ["D"] and out["dropped_by_expression"]["count"] == 0


def test_top_ten_cut_and_order():
    groups = {f"G{i:02d}": ([f"m{i}"], [f"T{i}"]) for i in range(14)}
    lk = lookup_with_nulls(groups, N)
    spec = {f"m{i}": 10.0 ** -(6 + i) for i in range(14)}
    out = screen_rows(rows(spec), lk, N, settings=ScreenSettings(top_groups=10))
    assert len(out["groups"]) == 10 and out["n_groups_not_shown"] == 4
    assert out["groups"][0]["group"] == "G13"      # largest |z| first


def test_no_statistics_refused():
    df = rows({"a": 1e-9}).assign(z=np.nan, p=np.nan)
    with pytest.raises(ValueError, match="statistics"):
        screen_rows(df, lookup_with_nulls({"A": (["a"], ["TA"])}, N), N)


def test_minimum_effect_margin():
    lk = lookup_with_nulls({"A": (["a"], ["TA"])}, N)
    df = rows({"a": 1e-9})      # z about 6.1, effect about 0.61, SE 0.1
    assert screen_rows(df, lk, N, settings=ScreenSettings(delta=0.0))["n_pass"] == 1
    assert screen_rows(df, lk, N, settings=ScreenSettings(delta=0.3))["n_pass"] == 0   # (0.61-0.3)/0.1 = 3.1


def test_fit_keeps_result_small():
    groups = [{"group": f"G{i}", "label": "x" * 40, "members": [{"model": "m" * 50}] * 5,
               "tfs": [{"tf": "t" * 10, "tpm": 1.0}] * 10} for i in range(10)]
    out = fit({"n_pass": 50, "groups": groups})
    assert len(json.dumps(out, separators=(",", ":"))) <= 3000
    assert out["groups"][0]["more_members"] >= 1
