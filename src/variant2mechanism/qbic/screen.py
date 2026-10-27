"""The QBiC-SELEX screen: gate, groups, expression filter, ranking (spec 1, section 8.1). Deterministic code.

The gate is Bonferroni over the models scored for one variant (p < 0.05 / 997, |z| > 4.05). Passing models are
grouped by CIS-BP specificity; a group survives the expression filter if any TF mapped to it has TPM >= min_tpm in
the context. Groups are ranked by their best |z|.
"""

from dataclasses import dataclass
from typing import Protocol

import numpy as np
import pandas as pd
from scipy.stats import norm

NOTES = ["predicted_effect > 0 means the alternate allele binds more strongly.",
         "In vitro binding only: expression and chromatin decide whether a change matters."]


class Lookup(Protocol):
    """What the screen needs from the registry (the real one, or a stand-in in tests)."""
    cognate_tf: dict[str, str]
    quality: dict[str, dict]
    # optional: own_model {symbol: model id}; with it, each TF a group covers is marked "own" or "mapped"

    def group_of_model(self, model_id: str) -> dict: ...


@dataclass
class ScreenSettings:
    alpha: float = 0.05
    min_tpm: float = 1.0
    top_groups: int = 10
    delta: float = 0.0
    max_tfs: int = 10
    max_members: int = 5


def gate(scores: pd.DataFrame, n_models: int, s: ScreenSettings) -> tuple[pd.DataFrame, float, float]:
    """Passing rows sorted by |z|, plus the p and |z| thresholds."""
    p_thr = s.alpha / n_models
    z_thr = float(norm.isf(p_thr / 2))
    ok = scores[scores.status == "ok"].copy()
    ok["abs_z"] = ok.z.abs()
    if s.delta > 0:       # minimum-effect test: z = (|effect| - delta) / SE, SE = |effect / z|
        se = (ok.effect / ok.z).abs().replace([np.inf], np.nan)
        z_min = (ok.effect.abs() - s.delta) / se
        ok["gate_z"] = z_min.fillna(0.0)
        passed = ok[ok.gate_z > z_thr]
    else:
        passed = ok[ok.p < p_thr]
    return passed.sort_values("abs_z", ascending=False), p_thr, z_thr


def direction(effect: float) -> str:
    return "alt binds more" if effect > 0 else "alt binds less"


def screen_rows(scores: pd.DataFrame, lookup: Lookup, n_models: int, expression=None, context: str | None = None,
                site=None, settings: ScreenSettings | None = None) -> dict:
    """Screen one variant's per-model rows (columns model, effect, z, p, status).

    `expression` has `parse(text)` and `tf_expression(symbols, ctx)`; `site(model_id)` returns site strength.
    """
    s = settings or ScreenSettings()
    if scores.z.isna().all():
        raise ValueError("These rows have no statistics; the screen needs a run with --compute-stats.")
    passed, p_thr, z_thr = gate(scores, n_models, s)
    ctx = expression.parse(context) if expression is not None else None
    filtering = ctx is not None and ctx.kind != "none"
    own = getattr(lookup, "own_model", None)

    def tf_entry(t: str, **extra) -> dict:
        return {"tf": t, **extra, **({"model": "own" if own.get(t) else "mapped"} if own is not None else {})}

    groups: dict[str, dict] = {}
    for r in passed.itertuples(index=False):
        g = lookup.group_of_model(r.model)
        rec = groups.setdefault(g["id"], {"group": g, "members": []})
        rec["members"].append(r)

    kept, dropped = [], []
    for gid, rec in groups.items():
        g, members = rec["group"], rec["members"]
        best = members[0]
        same = int(sum(bool(np.sign(m.effect) == np.sign(best.effect)) for m in members))
        tfs = list(g["tfs"])
        expr = expression.tf_expression(tfs, ctx) if filtering else {}
        expressed = [t for t in tfs if (expr.get(t, {}).get("tpm") or 0) >= s.min_tpm]
        out = {"group": gid, "label": g["label"], "n_models_in_group": len(g["models"]),
               "best_model": best.model, "best_tf": lookup.cognate_tf.get(best.model),
               "z": round(float(best.z), 2), "effect": round(float(best.effect), 3), "direction": direction(best.effect),
               "n_pass": len(members), "n_same_sign": same, "mixed_directions": same != len(members),
               "members": [{"model": m.model, "tf": lookup.cognate_tf.get(m.model), "effect": round(float(m.effect), 3),
                            "z": round(float(m.z), 2), "p": float(f"{m.p:.2g}"),
                            "quality": lookup.quality.get(m.model, {}).get("cross_exp_pearsonr")}
                           for m in members[: s.max_members]],
               "_abs_z": abs(float(best.z))}
        if len(members) > s.max_members:
            out["more_members"] = len(members) - s.max_members
        if filtering:
            ranked = sorted(tfs, key=lambda t: -(expr.get(t, {}).get("tpm") or -1))
            out["tfs"] = [tf_entry(t, tpm=expr.get(t, {}).get("tpm"), rank=expr.get(t, {}).get("rank_among_tfs"))
                          for t in ranked[: s.max_tfs]]
            out["n_tfs_expressed"] = len(expressed)
        else:
            out["tfs"] = [tf_entry(t) for t in tfs[: s.max_tfs]]
        if len(tfs) > s.max_tfs:
            out["more_tfs"] = len(tfs) - s.max_tfs
        (kept if (not filtering or expressed) else dropped).append(out)

    kept.sort(key=lambda x: -x["_abs_z"])
    dropped.sort(key=lambda x: -x["_abs_z"])
    top = kept[: s.top_groups]
    if site is not None:
        for g in top:
            try:
                g["site_strength"] = site(g["best_model"])
            except Exception as e:  # weights missing locally: report, do not fail the screen
                g["site_strength"] = {"error": str(e)[:120]}
    for g in kept + dropped:
        g.pop("_abs_z")
    return {
        "n_models_scored": int((scores.status == "ok").sum()),
        "n_pass": int(len(passed)),
        "threshold": {"p": float(f"{p_thr:.3g}"), "abs_z": round(z_thr, 2), "rule": f"Bonferroni {s.alpha}/{n_models}"
                      + (f", minimum effect {s.delta}" if s.delta > 0 else "")},
        "context": ctx.describe() if ctx is not None else "none: expression filter skipped",
        "n_groups_pass": len(groups),
        "groups": top,
        "n_groups_not_shown": max(0, len(kept) - s.top_groups),
        "dropped_by_expression": {"count": len(dropped),
                                  "top": [{"group": d["group"], "label": d["label"], "z": d["z"]} for d in dropped[:5]]},
        "notes": NOTES,
    }


# -- screen v2: occupancy first (spec 3, section 2) -------------------------------------------------------------

OCCUPIED = ("bound_here", "bound_elsewhere")
NO_PEAK = ("No ENCODE TF ChIP-seq peak contains this variant in any biosample; QBiC-SELEX changes below have no "
           "occupancy support.")


@dataclass
class ScreenV2Settings:
    alpha: float = 0.05
    min_tpm: float = 1.0
    max_occupied: int = 10
    max_unknown: int = 5
    strong_site_pct: float = 97.5     # the site-strength rule for occupied TFs (26 Oct 2026)


def screen_v2(scores: pd.DataFrame, reg, n_models: int, expression=None, context: str | None = None,
              occupancy=None, site=None, settings: ScreenV2Settings | None = None, exclude: set | None = None) -> dict:
    """Per TF with QBiC-SELEX coverage, its own or mapped model with the largest |z|; candidates are the occupied
    TFs (bound here, then bound elsewhere; within each, a strong site first, then by |z|) and expressed TFs ENCODE
    never assayed whose best model passes the gate. `occupancy` has `tf_class(symbol)` and `detail(symbol)`; without
    it every TF's occupancy is unknown. A strong site: the better allele's best k-mer over the variant reaches
    `strong_site_pct` of the best model's coefficients; without `site`, or when it fails, no TF is demoted.
    The count of models passing Bonferroni is kept only as a diagnostic (`n_pass`)."""
    s = settings or ScreenV2Settings()
    if scores.z.isna().all():
        raise ValueError("These rows have no statistics; the screen needs a run with --compute-stats.")
    passed, p_thr, z_thr = gate(scores, n_models, ScreenSettings(alpha=s.alpha))
    ok = scores[scores.status == "ok"]
    by_model = {r.model: r for r in ok.itertuples(index=False) if r.z == r.z}
    ctx = expression.parse(context) if expression is not None else None
    filtering = ctx is not None and ctx.kind != "none"
    tfs = sorted((set(reg.own_model) | set(reg.mapped_models)) - (exclude or set()))
    expr = expression.tf_expression(tfs, ctx) if filtering else {}
    rows = []
    for tf in tfs:
        own = reg.own_model.get(tf)
        models = [(own, "own")] if own else []
        models += [(m, "mapped") for m in reg.mapped_models.get(tf, []) if m != own]
        scored = [(m, kind) for m, kind in models if m in by_model]
        if not scored:
            continue
        best, kind = max(scored, key=lambda mk: abs(by_model[mk[0]].z))
        r = by_model[best]
        e = expr.get(tf, {})
        tpm = e.get("tpm")
        occ = occupancy.detail(tf) if occupancy is not None else {"occupancy": "unknown"}
        rows.append({"tf": tf, "group": reg.group_of_model(best)["label"],
                     "coverage": "own_model" if own else "mapped", "best_model": best, "best_model_kind": kind,
                     "best_model_tf": reg.cognate_tf.get(best), "z": round(float(r.z), 2),
                     "effect": round(float(r.effect), 3), "p": float(f"{r.p:.2g}"),
                     "allele_binding_more": "alt" if r.effect > 0 else "ref",
                     "passes_gate": bool(abs(r.z) > z_thr), "tpm": tpm, "rank": e.get("rank_among_tfs"),
                     "n_tfs": e.get("n_tfs"),
                     "expressed": (not filtering) or tpm is None or tpm >= s.min_tpm, **occ})
    def add_site(r: dict) -> None:
        try:
            r["site_strength"] = site(r["best_model"])
        except Exception as e:  # weights missing locally: report, do not fail the screen
            r["site_strength"] = {"error": str(e)[:120]}

    unknown_class = "not_assayed" if occupancy is not None else "unknown"
    occupied = [r for r in rows if r["occupancy"] in OCCUPIED and r["expressed"]]
    if site is not None:                # every occupied TF, so a strong site below the top 10 by |z| can move up
        for r in occupied:
            add_site(r)
            st = r["site_strength"]
            if "ref_percentile" in st:
                r["strong_site"] = max(st["ref_percentile"], st["alt_percentile"]) >= s.strong_site_pct
    occupied.sort(key=lambda r: (OCCUPIED.index(r["occupancy"]), r.get("strong_site") is False, -abs(r["z"]),
                                 -(r["tpm"] or 0)))
    unknown = sorted((r for r in rows if r["occupancy"] == unknown_class and r["expressed"] and r["passes_gate"]),
                     key=lambda r: -abs(r["z"]))
    shown_occ, shown_unk = occupied[: s.max_occupied], unknown[: s.max_unknown]
    if site is not None:
        for r in shown_unk:
            add_site(r)
    counts = {"occupied": len(occupied), "unknown": len(unknown),
              "occupied_strong_site": sum(1 for r in occupied if r.get("strong_site")),
              "occupied_not_expressed": sum(1 for r in rows if r["occupancy"] in OCCUPIED and not r["expressed"]),
              "unbound_assayed_here": sum(1 for r in rows if r["occupancy"] == "unbound_assayed_here"),
              "unbound_assayed_elsewhere": sum(1 for r in rows if r["occupancy"] == "unbound_assayed_elsewhere"),
              "tfs_scored": len(rows)}
    return {"n_models_scored": int((scores.status == "ok").sum()), "n_pass": int(len(passed)),
            "gate": {"abs_z": round(z_thr, 2), "p": float(f"{p_thr:.3g}"), "rule": f"Bonferroni {s.alpha}/{n_models}"},
            "context": ctx.describe() if ctx is not None else "none: expression filter skipped",
            "occupancy_available": occupancy is not None,
            "nothing_occupied": occupancy is not None and not getattr(occupancy, "peaks", True),
            "strong_site_pct": s.strong_site_pct if site is not None else None,
            "no_strong_site": bool(occupied) and all(r.get("strong_site") is False for r in occupied),
            "occupied": shown_occ, "unknown": shown_unk, "counts": counts}
