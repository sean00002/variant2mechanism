"""Read-only QBiC-SELEX access for v9 (SPEC 13.2, 13.5): one variant's cached scores, per model and per model-sharing
group, without the side effects of the v8 path.

Why not QbicCache/QbicTools: QbicCache opens cache/qbic.sqlite read-write and creates tables, QbicTools appends to
runs/qbic_calls.jsonl on every hit and asks Ensembl outside the HTTP cache on a miss, and Registry.groups() can rewrite
cache/groups.json. Here the database is opened with mode=ro, groups.json is read with json, and a variant that is not
cached under the statistics settings hash is a cache miss ("precompute required"): no job, no network.

Three levels are kept apart (maps/qbic.md section 3):
- a model: one HT-SELEX k-mer model of the 997-model primary collection, with its own (cognate) TF and every TF that
  CIS-BP maps to it (Table S5);
- a model-sharing group (cache/groups.json): models whose mapped TF sets overlap (Jaccard >= 0.5); a group is not a
  biological family, and one family can span several groups (C/EBP: G035, G142, G143);
- the Lambert DBD label: the group's family label, shown and used for the neutral order.

Rules every output keeps:
- a CIS-BP-mapped model counts as the TF's own: the mapping is recorded as provenance ("own" or "cisbp") and nothing
  reads it to decide anything;
- no ordering by z: groups are listed by DBD label then group id, models by model id; the Bonferroni gate (the v8 rule,
  qbic.screen.gate) is a field, never a filter;
- a group's best model is its model with the largest |z|: the representative its row shows, never a rank between
  groups;
- the models of one group can disagree about the allele (at rs1427407, SPIB's model predicts more binding to G and
  SPI1's own model to T): gate_sides() splits a group's gate-passing models by that allele, so a prediction is only
  ever attributed to the TFs its own models map to;
- site strength is the summed score over every overlapping k-mer of the 21-bp context (v8/sitescore.py), computed only
  for the models asked about, cached in the run folder and shown, never used to order or filter.

Sign convention (qbic_selex.predict; checked in maps/qbic.md 2.2): effect = sum of the alt allele's k-mer coefficients
minus the ref allele's, so effect > 0 means the alt allele is predicted to bind more; z carries the effect's sign.
"""

import json
import os
import re
import sqlite3
from collections import Counter, defaultdict
from collections.abc import Iterable
from contextlib import closing
from dataclasses import dataclass, field
from functools import lru_cache
from pathlib import Path
from typing import Any, Literal

import pandas as pd

from ..config import Config
from ..qbic import screen
from ..qbic.cache import model_ids, settings, settings_hash
from ..qbic.registry import Registry, build_registry
from ..v8.sitescore import site_score
from .schemas import Variant

CONTEXT_INDEX = 10                                   # the variant base in QBiC-SELEX's 21-bp context
SITE_CACHE = Path("cache") / "qbic_site_strength.json"   # in the run folder
REGISTRY_FILES = (("data", "hgnc"), ("data", "table_s1"), ("data", "lambert"), ("data", "table_s5"),
                  ("data", "table_s6"), ("data", "table_s3"))
# HGNC roots that number the members of a domain-defined gene group in order of discovery (ZNF43, ZBTB33, THAP11):
# a shared root here says nothing about paralogy, so it never becomes a paralog stem.
SERIAL_ROOTS = frozenset({"ZNF", "ZFP", "ZSCAN", "ZKSCAN", "ZBTB", "ZBED", "ZMAT", "THAP", "PRDM", "CENP", "TIGD",
                          "MBD"})
SCORE_DEFINITION = ("effect = sum of the alt allele's k-mer coefficients minus the ref allele's over the 21-bp context "
                    "(effect > 0: alt predicted to bind more); z = effect / its standard error from the model's "
                    "coefficient covariance; p two-sided")
BindsMore = Literal["ref", "alt", "equal"]


def variant_key(variant: Variant) -> str:
    """The cache's variant key, e.g. chr1:109274968:G>T (v9 chromosomes carry no "chr")."""
    return f"chr{variant.chrom}:{variant.pos}:{variant.ref}>{variant.alt}"


def binds_more(effect: float | None) -> BindsMore | None:
    """The allele predicted to bind more (effect is alt minus ref), or None for a model that was not scored."""
    if effect is None:
        return None
    return "alt" if effect > 0 else "ref" if effect < 0 else "equal"


def _round(value: float | None, digits: int) -> float | None:
    return None if value is None else round(float(value), digits)


def _p(value: float | None) -> float | None:
    return None if value is None else float(f"{float(value):.3g}")


# --- shared, read-only reference data ---------------------------------------------------------------------------------

_REGISTRIES: dict[tuple[str, ...], Registry] = {}


def registry_for(cfg: Config) -> Registry:
    """The QBiC-SELEX registry (TF names, own and CIS-BP-mapped models, Lambert DBDs), built once per set of input
    files. build_registry only reads data/ tables."""
    key = tuple(str(cfg.path(*k)) for k in REGISTRY_FILES)
    if key not in _REGISTRIES:
        _REGISTRIES[key] = build_registry(cfg)
    return _REGISTRIES[key]


@lru_cache(maxsize=4)
def _read_groups(path: str, mtime_ns: int) -> dict:
    return json.loads(Path(path).read_text())


def load_groups(cfg: Config) -> dict:
    """cache/groups.json, read with json (never through Registry.groups(), which can rewrite it). Shared: do not
    mutate the returned object."""
    path = cfg.path("cache", "groups")
    return _read_groups(str(path), path.stat().st_mtime_ns)


def _base(symbol: str) -> str:
    """The symbol with one family index removed: a trailing -number (NKX2-8), else trailing digits (GCM2), else one
    trailing letter (CEBPA) when at least four characters remain to judge from."""
    for pattern in (r"-\d+$", r"\d+$"):
        if re.search(pattern, symbol):
            return re.sub(pattern, "", symbol)
    return symbol[:-1] if len(symbol) >= 4 and symbol[-1].isalpha() else symbol


def symbol_stems(symbols: Iterable[str]) -> dict[str, str]:
    """Each symbol's stem: its base when another symbol shares that base or is that base (CEBPA and CEBPB -> CEBP;
    SHOX2 -> SHOX because SHOX exists), else the symbol itself (EOMES, MYC)."""
    universe = set(symbols)
    bases = {s: _base(s) for s in universe}
    shared = Counter(b for s, b in bases.items() if b != s)
    return {s: b if b != s and len(b) >= 2 and (b in universe or shared[b] >= 2) else s for s, b in bases.items()}


def stems_of(groups_doc: dict) -> dict[str, str | None]:
    """Group id -> the symbol stem shared with another group of the same DBD label (CEBP for G035, G142 and G143), so
    paralog groups can be considered together; None when no stem is held by a strict majority of the group's members
    or no other group has it. A naming heuristic, shown beside the DBD label; serially numbered roots (ZNF, ZBTB, ...)
    never count."""
    groups = groups_doc["groups"]
    stems = symbol_stems(t for g in groups for t in g["tfs"])
    holders: dict[tuple[str, str], set[str]] = defaultdict(set)      # (stem, DBD label) -> groups with a member
    for g in groups:
        for tf in g["tfs"]:
            holders[(stems[tf], g["dbd"])].add(g["id"])
    out: dict[str, str | None] = {}
    for g in groups:
        counts = Counter(stems[tf] for tf in g["tfs"] if stems[tf] not in SERIAL_ROOTS)
        top = min(counts.items(), key=lambda kv: (-kv[1], kv[0]), default=None)
        majority = top is not None and top[1] * 2 > len(g["tfs"])
        out[g["id"]] = top[0] if majority and len(holders[(top[0], g["dbd"])]) > 1 else None
    return out


@lru_cache(maxsize=4)
def _stems_of_file(path: str, mtime_ns: int) -> dict[str, str | None]:
    return stems_of(_read_groups(path, mtime_ns))


def paralog_stems(cfg: Config) -> dict[str, str | None]:
    """stems_of() for config's cache/groups.json (computed once per file version). Shared: do not mutate."""
    path = cfg.path("cache", "groups")
    return _stems_of_file(str(path), path.stat().st_mtime_ns)


# --- one variant's scores ---------------------------------------------------------------------------------------------

@dataclass
class VariantScores:
    """The cached rows of one variant under the statistics settings hash, in model-id order."""
    key: str
    status: Literal["ok", "cache_miss", "not_applicable"]
    message: str = ""
    rows: list[dict] = field(default_factory=list)      # model, effect, z, p, status, run_id
    ref_sequence: str | None = None
    alt_sequence: str | None = None
    runs: list[dict] = field(default_factory=list)      # the QBiC-SELEX runs that produced the rows


@dataclass(frozen=True)
class Gate:
    p_threshold: float
    z_threshold: float
    passing: frozenset[str]


class QbicReader:
    """Read-only access to cache/qbic.sqlite and cache/groups.json for one configuration. `registry` and `groups`
    can be passed in (tests do, to change a mapping); by default they are the shared read-only copies."""

    def __init__(self, cfg: Config, registry: Registry | None = None, groups: dict | None = None):
        self.cfg = cfg
        self.db = cfg.path("cache", "db")
        self.settings = settings(cfg, stats=True)
        self.settings_hash = settings_hash(cfg, stats=True)
        self.models = model_ids(cfg)
        self.alpha = float(cfg["screen"]["alpha"])
        self.delta = float(cfg["screen"].get("delta", 0.0))
        self._registry = registry
        self._groups = groups
        self._stems: dict[str, str | None] | None = None

    @property
    def registry(self) -> Registry:
        if self._registry is None:
            self._registry = registry_for(self.cfg)
        return self._registry

    @property
    def groups(self) -> dict:
        if self._groups is None:
            self._groups = load_groups(self.cfg)
        return self._groups

    def stems(self) -> dict[str, str | None]:
        """Group id -> paralog stem, for this reader's groups document."""
        if self._stems is None:
            self._stems = stems_of(self._groups) if self._groups is not None else paralog_stems(self.cfg)
        return self._stems

    def group(self, group_id: str) -> dict | None:
        return next((g for g in self.groups["groups"] if g["id"] == group_id.strip().upper()), None)

    def group_of_model(self, model: str) -> dict:
        return self.groups["groups"][self.groups["model_to_group"][model]]

    def _connect(self) -> sqlite3.Connection:
        return sqlite3.connect(f"{self.db.resolve().as_uri()}?mode=ro", uri=True)

    # --- reading ---------------------------------------------------------------------------------------------------

    def scores(self, variant: Variant) -> VariantScores:
        """Every model's row for the variant, or a cache miss ("precompute required") when fewer than all models are
        cached under the statistics settings hash, or not_applicable when QBiC-SELEX scored none of them (the status
        it recorded, such as ref_mismatch, is the message)."""
        key = variant_key(variant)
        with closing(self._connect()) as con:
            rows = con.execute("SELECT model, effect, z, p, status, run_id FROM scores WHERE settings_hash=? AND "
                               "variant_key=? ORDER BY model", [self.settings_hash, key]).fetchall()
            seq = con.execute("SELECT ref_sequence, alt_sequence FROM sequences WHERE settings_hash=? AND "
                              "variant_key=?", [self.settings_hash, key]).fetchone()
            run_ids = sorted({r[5] for r in rows if r[5]})
            runs = con.execute(f"SELECT run_id, created_utc, slurm_job, partition, device, stats, n_variants, "
                               f"n_models FROM runs WHERE run_id IN ({','.join('?' * len(run_ids))}) ORDER BY run_id",
                               run_ids).fetchall() if run_ids else []
        names = ("model", "effect", "z", "p", "status", "run_id")
        records = [dict(zip(names, r, strict=True)) for r in rows]
        if {r["model"] for r in records} != set(self.models):
            return VariantScores(key, "cache_miss", f"precompute required: QBiC-SELEX statistics are not cached for "
                                 f"{key} under settings {self.settings_hash} ({len(records)} of {len(self.models)} "
                                 "models); v9 never launches a QBiC-SELEX job")
        run_names = ("run_id", "created_utc", "slurm_job", "partition", "device", "stats", "n_variants", "n_models")
        out = VariantScores(key, "ok", rows=records, ref_sequence=seq[0] if seq else None,
                            alt_sequence=seq[1] if seq else None,
                            runs=[dict(zip(run_names, r, strict=True)) for r in runs])
        if not any(r["status"] == "ok" for r in records):
            counts = Counter(r["status"] for r in records)
            out.status = "not_applicable"
            out.message = (f"QBiC-SELEX scored no model for {key}: "
                           + ", ".join(f"{s} ({n} models)" for s, n in sorted(counts.items())))
        return out

    def gate(self, scores: VariantScores) -> Gate:
        """The Bonferroni gate of qbic.screen.gate (alpha / 997 models; with config screen.delta > 0 its
        minimum-effect form). It decides which predictions are reported as directional Evidence, nothing else."""
        frame = pd.DataFrame(scores.rows, columns=["model", "effect", "z", "p", "status", "run_id"])
        frame[["effect", "z", "p"]] = frame[["effect", "z", "p"]].astype(float)
        passed, p_thr, z_thr = screen.gate(frame, len(self.models),
                                           screen.ScreenSettings(alpha=self.alpha, delta=self.delta))
        return Gate(p_threshold=float(p_thr), z_threshold=float(z_thr), passing=frozenset(passed["model"]))

    def provenance(self, scores: VariantScores | None = None) -> dict[str, Any]:
        """The model and score provenance a ToolCall's raw result carries (SPEC 13.5; maps/qbic.md section 9)."""
        out = {**self.settings, "settings_hash": self.settings_hash, "n_models": len(self.models),
               "score_definition": SCORE_DEFINITION, "gate": f"Bonferroni p < {self.alpha:g} / {len(self.models)}"}
        if scores is not None:
            out["runs"] = scores.runs
        return out

    def _model_row(self, row: dict, passing: frozenset[str]) -> dict[str, Any]:
        reg, m = self.registry, row["model"]
        g = self.group_of_model(m)
        maps_to = sorted(reg.model_tfs.get(m, ()))
        ok = row["status"] == "ok"
        effect = row["effect"] if ok else None
        z = row["z"] if ok else None
        return {"model": m, "status": row["status"], "effect": _round(effect, 4), "z": _round(z, 3),
                "p": _p(row["p"] if ok else None),
                "se": _round(abs(effect / z), 4) if ok and z not in (None, 0) else None,
                "binds_more": binds_more(effect), "passes_gate": m in passing, "cognate_tf": reg.cognate_tf.get(m),
                "maps_to": maps_to, "mapping": {tf: self._mapping(tf, [m]) for tf in maps_to},
                "group_id": g["id"], "group_label": g["label"], "dbd": g["dbd"],
                "quality": (reg.quality.get(m) or {}).get("cross_exp_pearsonr"), "run_id": row["run_id"]}

    def _mapping(self, tf: str, models: Iterable[str]) -> Literal["own", "cisbp"]:
        """"own" when the TF's cognate model is among the models, else "cisbp" (covered through a CIS-BP mapping)."""
        return "own" if self.registry.own_model.get(tf) in set(models) else "cisbp"

    def model_table(self, scores: VariantScores) -> list[dict[str, Any]]:
        """Every model's row with its registry fields, in model-id order (the raw table of qbic_inventory)."""
        passing = self.gate(scores).passing
        return [self._model_row(r, passing) for r in scores.rows]

    def inventory(self, scores: VariantScores) -> list[dict[str, Any]]:
        """One row per model-sharing group with any cached row, in the neutral order (Lambert DBD label, then group id),
        with exactly the keys of contract C2. Every group is listed, gate or not."""
        passing = self.gate(scores).passing
        by_model = {r["model"]: r for r in scores.rows}
        stems = self.stems()
        rows = []
        for g in self.groups["groups"]:
            cached = [by_model[m] for m in g["models"] if m in by_model]
            if not cached:
                continue
            scored = [r for r in cached if r["status"] == "ok" and r["z"] is not None]
            best = min(scored, key=lambda r: (-abs(r["z"]), r["model"]), default=None)
            n_pass = sum(r["model"] in passing for r in cached)
            rows.append({"group_id": g["id"], "group_label": g["label"], "dbd": g["dbd"],
                         "members": [{"tf": tf, "mapping": self._mapping(tf, g["models"])} for tf in sorted(g["tfs"])],
                         "paralog_stem": stems.get(g["id"]),
                         "best_model": best["model"] if best else None,
                         "binds_more": binds_more(best["effect"]) if best else None,
                         "z": _round(best["z"], 3) if best else None,
                         "effect": _round(best["effect"], 4) if best else None,
                         "p": _p(best["p"]) if best else None,
                         "n_pass": n_pass, "n_models": len(g["models"]), "passes_gate": n_pass > 0})
        return sorted(rows, key=lambda r: (r["dbd"].casefold(), r["group_id"]))

    def gate_sides(self, scores: VariantScores) -> dict[str, list[dict[str, Any]]]:
        """For each group with a model past the gate: its gate-passing models split by the allele they predict to bind
        more, one side per allele (ref, then alt; a group whose models agree has one). Each side has its models (model
        id order), its best model (largest |z|, ties by model id) with z, effect and p, the TFs those models map to
        (own or CIS-BP, Table S5, which names exactly the group's members) and each TF's mapping type among them. A
        side is what a prediction can be about: one TF's model never lends its allele to another TF."""
        passing = self.gate(scores).passing
        by_model = {r["model"]: r for r in scores.rows}
        out: dict[str, list[dict[str, Any]]] = {}
        for g in self.groups["groups"]:
            hits = [by_model[m] for m in sorted(g["models"]) if m in passing and m in by_model]
            sides = []
            for side in ("ref", "alt"):
                models = [r for r in hits if binds_more(r["effect"]) == side]
                if not models:
                    continue
                best = min(models, key=lambda r: (-abs(r["z"]), r["model"]))
                ids = [r["model"] for r in models]
                tfs = sorted({tf for m in ids for tf in self.registry.model_tfs.get(m, ())})
                sides.append({"binds_more": side, "models": ids, "best_model": best["model"],
                              "z": _round(best["z"], 3), "effect": _round(best["effect"], 4), "p": _p(best["p"]),
                              "tfs": tfs, "mapping": {tf: self._mapping(tf, ids) for tf in tfs}})
            if sides:
                out[g["id"]] = sides
        return out

    def detail(self, scores: VariantScores, *, tf: str | None = None, group: str | None = None) -> dict[str, Any]:
        """Every model of a TF (own and CIS-BP-mapped alike) or of a group, in model-id order. For a TF: its name
        resolution and coverage; a name that is unknown or ambiguous, or a TF with no model, gets no model rows."""
        passing = self.gate(scores).passing
        by_model = {r["model"]: r for r in scores.rows}
        reg = self.registry
        if tf is not None:
            name = reg.resolve_tf(tf)
            head: dict[str, Any] = {"query": {"tf": tf}, "resolution": {
                "status": name["status"], "symbol": name["symbol"], "via": name["via"], "notes": name["notes"],
                "candidates": [c["symbol"] for c in name["candidates"]]}}
            if name["status"] != "ok":
                return {**head, "models": []}
            cov = reg.coverage(name["symbol"])
            head["resolution"]["coverage"] = cov["status"]
            models = sorted({m for m in [cov["own_model"], *cov["mapped_models"]] if m})
        else:
            g = self.group(group or "")
            head = {"query": {"group": group}, "group": None if g is None else {
                "group_id": g["id"], "group_label": g["label"], "dbd": g["dbd"],
                "paralog_stem": self.stems().get(g["id"]),
                "members": [{"tf": t, "mapping": self._mapping(t, g["models"])} for t in sorted(g["tfs"])]}}
            models = sorted(g["models"]) if g is not None else []
        return {**head, "models": [self._model_row(by_model[m], passing) for m in models if m in by_model]}

    def site_strengths(self, scores: VariantScores, models: Iterable[str],
                       run_dir: str | Path | None = None) -> dict[str, dict]:
        """Summed site strength (v8/sitescore.py: ref and alt percentiles against random 21-mers) for the given
        models, cached in run_dir/cache/qbic_site_strength.json. Display only. A model whose weights are missing
        locally gets an {"error": ...} entry instead of failing the call."""
        wanted = sorted(set(models))
        if not (scores.ref_sequence and scores.alt_sequence):
            return {m: {"error": "no cached 21-bp context for this variant"} for m in wanted}
        path = Path(run_dir) / SITE_CACHE if run_dir is not None else None
        saved: dict[str, dict] = json.loads(path.read_text()) if path is not None and path.exists() else {}
        out, added = {}, False
        for m in wanted:
            key = f"{self.settings_hash}|{scores.key}|{m}"
            if key not in saved:
                try:
                    saved[key] = site_score(m, scores.ref_sequence, scores.alt_sequence)
                except Exception as e:  # missing or unreadable weights: shown, never a failed call
                    saved[key] = {"error": f"{type(e).__name__}: {str(e)[:120]}"}
                added = True
            out[m] = saved[key]
        if added and path is not None:
            path.parent.mkdir(parents=True, exist_ok=True)
            tmp = path.with_name(f"{path.name}.{os.getpid()}.tmp")
            tmp.write_text(json.dumps(saved, sort_keys=True, indent=1))
            os.replace(tmp, path)
        return out

    def reference_check(self, variant: Variant) -> dict[str, Any]:
        """The genome base at the position from a cached QBiC-SELEX 21-mer (index 10), whatever alleles were cached
        there, compared with the given ref: verified, mismatch, or unavailable when no context is cached here."""
        with closing(self._connect()) as con:
            seqs = con.execute("SELECT ref_sequence FROM sequences WHERE variant_key LIKE ?",
                               [f"chr{variant.chrom}:{variant.pos}:%"]).fetchall()
        bases = sorted({s[CONTEXT_INDEX].upper() for (s,) in seqs if s and len(s) == 2 * CONTEXT_INDEX + 1})
        if len(bases) != 1:
            note = ("no QBiC-SELEX context is cached at this position" if not bases else
                    f"cached contexts disagree ({', '.join(bases)})")
            return {"source": "qbic_21mer", "status": "unavailable", "note": note}
        return {"source": "qbic_21mer", "status": "verified" if bases[0] == variant.ref else "mismatch",
                "genome_base": bases[0], "given_ref": variant.ref}


_READERS: dict[tuple[str, ...], QbicReader] = {}


def reader_for(cfg: Config) -> QbicReader:
    """One reader per configuration's database, groups file and model list (they hold no open handle)."""
    key = (str(cfg.path("cache", "db")), str(cfg.path("cache", "groups")), str(cfg.path("data", "model_list")),
           str(cfg["screen"]["alpha"]), str(cfg["screen"].get("delta", 0.0)))
    if key not in _READERS:
        _READERS[key] = QbicReader(cfg)
    return _READERS[key]
