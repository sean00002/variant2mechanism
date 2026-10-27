"""`qbic_screen` and `qbic_tf_detail`: JSON in, JSON out, never raising into the agent loop (spec 1, 8.2)."""

import json
import logging

from ..config import Config, load_config
from .cache import QbicCache
from .screen import ScreenSettings, ScreenV2Settings, screen_rows, screen_v2
from .variants import Variant, VariantError, strand_precheck

log = logging.getLogger(__name__)

MAX_CHARS = 3000

QBIC_SCREEN = {
    "name": "qbic_screen",
    "description": ("Screen one SNV (GRCh38, 1-based, plus-strand alleles) against all 997 QBiC-SELEX primary TF models. "
                    "Returns the TF groups whose binding the variant changes significantly (Bonferroni across models), "
                    "with direction, z-score, the TFs each group covers and their expression in the given context. "
                    "predicted_effect > 0 means the alternate allele binds more strongly. In vitro binding only: "
                    "expression and chromatin decide whether a change matters."),
}
QBIC_TF_DETAIL = {
    "name": "qbic_tf_detail",
    "description": ("Look up what QBiC-SELEX predicts for one named TF at one SNV, including old or ambiguous names. "
                    "Says whether the TF has its own model, is covered through CIS-BP-mapped models, or is not in "
                    "coverage."),
}


class QbicTools:
    def __init__(self, cfg: Config | None = None, registry=None, expression=None, site=None, cluster=None):
        self.cfg = cfg or load_config()
        self._registry, self._expression, self._site, self._cluster = registry, expression, site, cluster
        self.cache = QbicCache(self.cfg)
        sc = self.cfg["screen"]
        self.settings = ScreenSettings(alpha=float(sc["alpha"]), min_tpm=float(sc["min_tpm"]),
                                       top_groups=int(sc["top_groups"]), delta=float(sc["delta"]))

    # lazy defaults, so tests can pass stand-ins and nothing heavy loads until needed
    @property
    def registry(self):
        if self._registry is None:
            from .registry import get_registry
            self._registry = get_registry()
        return self._registry

    @property
    def expression(self):
        if self._expression is None:
            from .expression import get_expression
            self._expression = get_expression()
        return self._expression

    def site(self, model_id: str, key: str) -> dict:
        ref, alt = self.cache.sequences(key, stats=True)
        if self._site is not None:
            return self._site(model_id, ref, alt)
        from .refsite import site_strength
        return site_strength(model_id, ref, alt, self.cfg.path("data", "weights_dir"))

    # -- scores --------------------------------------------------------------------------------------------

    def _scores(self, v: Variant):
        """Cached rows with statistics; on a miss, a cluster job only if config allows it, else an error."""
        key = v.key()
        if key in self.cache.cached([key], stats=True):
            self.cache.log_call([key], hit=True)
            return self.cache.scores(key, stats=True), None
        hint = strand_precheck(v)
        if hint:
            return None, {"error": hint, "fix": "Resubmit with plus-strand alleles."}
        if not self.cfg["cache"].get("allow_miss_jobs"):
            self.cache.log_call([key], hit=False)
            return None, {"error": f"{key} has no cached QBiC-SELEX statistics.",
                          "fix": "Run QBiC-SELEX for this variant first (scripts/prefetch.py), or set cache.allow_miss_jobs."}
        from .backend import BackendError, get_backend
        try:
            (self._cluster or get_backend(self.cfg)).run([v], stats=True)
        except BackendError as e:
            return None, {"error": f"QBiC-SELEX cluster run failed: {str(e)[:400]}",
                          "fix": f"Check the {self.cfg['qbic']['backend']} QBiC-SELEX backend (for slurm: ssh -fN {self.cfg['cluster']['host']}), or import the run later."}
        return self.cache.scores(key, stats=True), None

    # -- tools ---------------------------------------------------------------------------------------------

    def qbic_screen(self, chrom, pos, ref, alt, expression_context=None, compact: bool = True) -> dict:
        """compact=True trims to about 3,000 characters for a single tool reply; the screen stage passes False
        because it stores each group as its own evidence row, so all top groups survive."""
        try:
            v = Variant.make(chrom, pos, ref, alt)
        except VariantError as e:
            return {"error": str(e), "fix": "Give one SNV: GRCh38, 1-based, plus-strand alleles."}
        try:
            scores, err = self._scores(v)
            if err:
                return err
            reg = self.registry
            out = screen_rows(scores, reg, len(self.cache.models), self.expression, expression_context,
                              site=lambda m: self.site(m, v.key()), settings=self.settings)
            out = {"variant": v.key(), **out}
            return fit(out) if compact else out
        except Exception as e:  # never raise into the agent loop
            log.exception("qbic_screen failed")
            return {"error": f"{type(e).__name__}: {str(e)[:300]}", "fix": "Check the expression context or the cache."}

    def qbic_screen_v2(self, chrom, pos, ref, alt, expression_context=None, occupancy=None) -> dict:
        """Screen v2 (spec 3): per TF, occupancy first. `occupancy` comes from context/occupancy.py (None when that
        lookup failed: then every TF's occupancy is unknown)."""
        from ..context.occupancy import NOT_SEQUENCE_SPECIFIC
        try:
            v = Variant.make(chrom, pos, ref, alt)
        except VariantError as e:
            return {"error": str(e), "fix": "Give one SNV: GRCh38, 1-based, plus-strand alleles."}
        try:
            scores, err = self._scores(v)
            if err:
                return err
            sc = self.cfg["screen"]
            out = screen_v2(scores, self.registry, len(self.cache.models), self.expression, expression_context,
                            occupancy, site=lambda m: self.site(m, v.key()),
                            settings=ScreenV2Settings(alpha=float(sc["alpha"]), min_tpm=float(sc["min_tpm"]),
                                                      strong_site_pct=float(sc["strong_site_pct"])),
                            exclude=NOT_SEQUENCE_SPECIFIC)
            return {"variant": v.key(), **out}
        except Exception as e:  # never raise into the agent loop
            log.exception("qbic_screen_v2 failed")
            return {"error": f"{type(e).__name__}: {str(e)[:300]}", "fix": "Check the expression context or the cache."}

    def qbic_tf_detail(self, chrom, pos, ref, alt, tf) -> dict:
        try:
            v = Variant.make(chrom, pos, ref, alt)
        except VariantError as e:
            return {"error": str(e), "fix": "Give one SNV: GRCh38, 1-based, plus-strand alleles."}
        try:
            reg = self.registry
            name = reg.resolve_tf(tf)
            if name["status"] != "ok":
                return {"tf": tf, "status": name["status"], "candidates": name["candidates"], "notes": name["notes"]}
            sym = name["symbol"]
            cov = reg.coverage(sym)
            head = {"tf": tf, "symbol": sym, "via": name["via"], "notes": name["notes"], "coverage": cov["status"]}
            if cov["status"] == "not_in_coverage":
                return head
            scores, err = self._scores(v)
            if err:
                return {**head, **err}
            ok = scores[scores.status == "ok"].copy()
            ok["abs_z"] = ok.z.abs()
            ok["rank"] = ok.abs_z.rank(ascending=False, method="min").astype(int)
            p_thr = self.settings.alpha / len(self.cache.models)
            models = ([cov["own_model"]] if cov["own_model"] else []) + [m for m in cov["mapped_models"]
                                                                         if m != cov["own_model"]]
            rows = []
            for m in models:
                r = ok[ok.model == m]
                g = reg.group_of_model(m)
                rec = {"model": m, "mapping": "own" if m == cov["own_model"] else f"CIS-BP ({reg.cognate_tf.get(m)})",
                       "group": f"{g['id']} {g['label']}",
                       "quality": reg.quality.get(m, {}).get("cross_exp_pearsonr")}
                if r.empty:
                    st = scores.loc[scores.model == m, "status"]
                    rec["status"] = st.iloc[0] if len(st) else "not_scored"
                else:
                    r = r.iloc[0]
                    rec.update({"effect": round(float(r.effect), 3), "z": round(float(r.z), 2),
                                "p": float(f"{r.p:.2g}"), "rank_abs_z": f"{int(r['rank'])}/{len(ok)}",
                                "passed_gate": bool(r.p < p_thr)})
                    try:
                        rec["site_strength"] = self.site(m, v.key())
                    except Exception as e:
                        rec["site_strength"] = {"error": str(e)[:100]}
                rows.append(rec)
            return fit({**head, "variant": v.key(), "gate_p": float(f"{p_thr:.3g}"), "models": rows})
        except Exception as e:
            log.exception("qbic_tf_detail failed")
            return {"error": f"{type(e).__name__}: {str(e)[:300]}", "fix": "Check the TF name or the cache."}


def fit(out: dict, limit: int = MAX_CHARS) -> dict:
    """Trim lists (members, then TFs, then groups or models) until the JSON is under `limit` characters."""
    def size():
        return len(json.dumps(out, separators=(",", ":")))

    items = out.get("groups") or out.get("models") or []
    for key, floor in (("members", 2), ("tfs", 4), ("members", 1), ("tfs", 2)):
        for g in items:
            if size() <= limit:
                return out
            if isinstance(g.get(key), list) and len(g[key]) > floor:
                g[f"more_{key}"] = g.get(f"more_{key}", 0) + len(g[key]) - floor
                g[key] = g[key][:floor]
    list_key = "groups" if "groups" in out else "models"
    while size() > limit and len(out.get(list_key, [])) > 1:
        out[list_key].pop()
        out[f"n_{list_key}_trimmed"] = out.get(f"n_{list_key}_trimmed", 0) + 1
    return out
