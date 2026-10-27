"""SQLite store of per-model QBiC-SELEX results (spec 1, section 5.2).

A variant counts as cached only when every model in the collection is present for its settings hash.
"""

import hashlib
import json
import sqlite3
import time
from datetime import UTC, datetime

import pandas as pd

from ..config import Config

SCHEMA = """
CREATE TABLE IF NOT EXISTS runs(run_id TEXT PRIMARY KEY, settings_hash TEXT, created_utc TEXT,
  slurm_job TEXT, partition TEXT, gres TEXT, device TEXT, stats INTEGER,
  n_variants INTEGER, n_models INTEGER, task_seconds TEXT, gpu_name TEXT, notes TEXT);
CREATE TABLE IF NOT EXISTS scores(settings_hash TEXT, variant_key TEXT, model TEXT,
  effect REAL, z REAL, p REAL, status TEXT, run_id TEXT,
  PRIMARY KEY(settings_hash, variant_key, model));
CREATE TABLE IF NOT EXISTS sequences(settings_hash TEXT, variant_key TEXT,
  ref_sequence TEXT, alt_sequence TEXT, PRIMARY KEY(settings_hash, variant_key));
"""

STATUSES = {"ok", "ref_mismatch", "chrom_not_found", "out_of_bounds", "invalid_allele", "missing_value",
            "contains_N", "invalid_sequence", "shorter_than_k"}


class CacheImportError(ValueError):
    """Raised when imported results are incomplete or inconsistent; nothing is written."""


def model_ids(cfg: Config) -> list[str]:
    lines = cfg.path("data", "model_list").read_text().splitlines()
    return sorted(x.strip() for x in lines if x.strip() and not x.startswith("#"))


def settings(cfg: Config, stats: bool) -> dict:
    return {"qbic_selex": "1.0.0", "zenodo_record": "23482275", "collection": "primary",
            "model_list_md5": hashlib.md5(cfg.path("data", "model_list").read_bytes()).hexdigest(),
            "genome_fai_md5": cfg.remote("cluster", "genome_fai_md5"), "context_length": 10, "stats": stats}


def settings_hash(cfg: Config, stats: bool) -> str:
    blob = json.dumps(settings(cfg, stats), sort_keys=True).encode()
    return hashlib.sha256(blob).hexdigest()[:16]


class QbicCache:
    def __init__(self, cfg: Config):
        self.cfg = cfg
        self.path = cfg.path("cache", "db")
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.models = model_ids(cfg)
        with self._connect() as con:
            con.executescript(SCHEMA)

    def _connect(self) -> sqlite3.Connection:
        return sqlite3.connect(self.path)

    def cached(self, keys: list[str], stats: bool = True) -> set[str]:
        """Keys with all models present for the settings hash."""
        h = settings_hash(self.cfg, stats)
        if not keys:
            return set()
        q = (f"SELECT variant_key, COUNT(*) FROM scores WHERE settings_hash=? AND variant_key IN "
             f"({','.join('?' * len(keys))}) GROUP BY variant_key")
        with self._connect() as con:
            counts = dict(con.execute(q, [h, *keys]).fetchall())
        return {k for k, n in counts.items() if n == len(self.models)}

    def scores(self, key: str, stats: bool = True) -> pd.DataFrame:
        h = settings_hash(self.cfg, stats)
        with self._connect() as con:
            df = pd.read_sql_query("SELECT model, effect, z, p, status, run_id FROM scores "
                                   "WHERE settings_hash=? AND variant_key=?", con, params=[h, key])
        if len(df) != len(self.models):
            raise KeyError(f"{key} is not cached with {'statistics' if stats else 'effects only'} "
                           f"({len(df)} of {len(self.models)} models)")
        return df

    def sequences(self, key: str, stats: bool = True) -> tuple[str, str]:
        h = settings_hash(self.cfg, stats)
        with self._connect() as con:
            row = con.execute("SELECT ref_sequence, alt_sequence FROM sequences WHERE settings_hash=? "
                              "AND variant_key=?", [h, key]).fetchone()
        if row is None:
            raise KeyError(f"no sequences cached for {key}")
        return row

    def import_results(self, run: dict, results: pd.DataFrame, expected_keys: set[str], stats: bool) -> int:
        """Validate (spec 1, 5.4, except the weight check, done by the caller) and import in one transaction."""
        check_results(results, expected_keys, set(self.models), stats)
        h = settings_hash(self.cfg, stats)
        rows = [(h, r.variant_key, r.model, _num(r.predicted_effect), _num(getattr(r, "z_score", None)),
                 _num(getattr(r, "p_value", None)), r.qbic_status, run["run_id"])
                for r in results.itertuples(index=False)]
        seqs = results.drop_duplicates("variant_key")[["variant_key", "ref_sequence", "alt_sequence"]]
        with self._connect() as con:
            con.execute("INSERT OR REPLACE INTO runs VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)", [
                run["run_id"], h, run.get("created_utc") or datetime.now(UTC).isoformat(timespec="seconds"),
                run.get("slurm_job"), run.get("partition"), run.get("gres"), run.get("device"), int(stats),
                len(expected_keys), len(self.models), json.dumps(run.get("task_seconds")), run.get("gpu_name"),
                run.get("notes")])
            con.executemany("INSERT OR REPLACE INTO scores VALUES (?,?,?,?,?,?,?,?)", rows)
            con.executemany("INSERT OR REPLACE INTO sequences VALUES (?,?,?,?)",
                            [(h, k, _str(r), _str(a)) for k, r, a in seqs.itertuples(index=False)])
        return len(rows)

    def runs(self) -> pd.DataFrame:
        with self._connect() as con:
            return pd.read_sql_query("SELECT * FROM runs ORDER BY created_utc", con)

    def log_call(self, keys: list[str], hit: bool, run_id: str | None = None, slurm_job: str | None = None,
                 wall_seconds: float | None = None):
        path = self.cfg.path("cache", "log")
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, "a") as f:
            f.write(json.dumps({"time": datetime.now(UTC).isoformat(timespec="seconds"), "variant_keys": keys,
                                "hit": hit, "run_id": run_id, "slurm_job": slurm_job,
                                "wall_seconds": None if wall_seconds is None else round(wall_seconds, 1)}) + "\n")


def check_results(df: pd.DataFrame, expected_keys: set[str], models: set[str], stats: bool) -> None:
    problems = []
    keys = set(df.variant_key)
    if keys != expected_keys:
        problems.append(f"variant keys differ from the submitted set: missing {sorted(expected_keys - keys)[:5]}, "
                        f"unexpected {sorted(keys - expected_keys)[:5]}")
    dup = df.duplicated(["variant_key", "model"]).sum()
    if dup:
        problems.append(f"{dup} duplicated (variant, model) pairs")
    if set(df.model) != models:
        problems.append(f"model set differs from the collection: missing {len(models - set(df.model))}, "
                        f"unexpected {sorted(set(df.model) - models)[:5]}")
    for k, n in df.groupby("variant_key").size().items():
        if n != len(models):
            problems.append(f"{k}: {n} of {len(models)} models")
            break
    bad = set(df.qbic_status) - STATUSES
    if bad:
        problems.append(f"unknown qbic_status values {sorted(bad)}")
    if stats:
        ok = df[df.qbic_status == "ok"]
        if "z_score" not in df or "p_value" not in df:
            problems.append("statistics requested but z_score/p_value columns are missing")
        elif not (pd.to_numeric(ok.z_score).notna().all() and pd.to_numeric(ok.p_value).notna().all()):
            problems.append("ok rows with non-finite z or p")
    if problems:
        raise CacheImportError("; ".join(problems))


def _num(x):
    try:
        x = float(x)
    except (TypeError, ValueError):
        return None
    return None if x != x else x


def _str(x):
    return x if isinstance(x, str) else None


def utc_stamp() -> str:
    return time.strftime("%Y%m%dT%H%M%SZ", time.gmtime())
