import pandas as pd
import pytest
from qbic_fixtures import MODELS

from variant2mechanism.qbic.cache import CacheImportError, QbicCache, settings_hash

KEY = "chr5:1295113:G>A"


def rows(models, key=KEY, stats=True):
    df = pd.DataFrame({"variant_key": key, "ref_sequence": "A" * 21, "alt_sequence": "C" * 21, "model": models,
                       "predicted_effect": 0.5, "qbic_status": "ok"})
    if stats:
        df["z_score"], df["p_value"] = 5.0, 1e-7
    return df


def test_complete_import_is_cached(small_cfg):
    c = QbicCache(small_cfg)
    c.import_results({"run_id": "r1"}, rows(MODELS), {KEY}, stats=True)
    assert c.cached([KEY]) == {KEY}
    assert len(c.scores(KEY)) == 2


def test_import_missing_a_model_is_rejected(small_cfg):
    c = QbicCache(small_cfg)
    with pytest.raises(CacheImportError):
        c.import_results({"run_id": "r1"}, rows(MODELS[:1]), {KEY}, stats=True)
    assert c.cached([KEY]) == set()


def test_incomplete_variant_is_not_cached(small_cfg):
    import sqlite3
    c = QbicCache(small_cfg)
    with sqlite3.connect(c.path) as con:
        con.execute("INSERT INTO scores VALUES (?,?,?,?,?,?,?,?)",
                    [settings_hash(small_cfg, True), KEY, MODELS[0], 0.1, 1.0, 0.3, "ok", "r0"])
    assert c.cached([KEY]) == set()
    with pytest.raises(KeyError):
        c.scores(KEY)


def test_settings_change_is_a_miss(small_cfg):
    c = QbicCache(small_cfg)
    c.import_results({"run_id": "r1"}, rows(MODELS), {KEY}, stats=True)
    small_cfg["cluster"]["genome_fai_md5"] = "0" * 32
    assert c.cached([KEY]) == set()
    assert QbicCache(small_cfg).cached([KEY], stats=False) == set()


def test_stats_rows_need_finite_z(small_cfg):
    df = rows(MODELS)
    df.loc[0, "z_score"] = float("nan")
    with pytest.raises(CacheImportError, match="non-finite"):
        QbicCache(small_cfg).import_results({"run_id": "r1"}, df, {KEY}, stats=True)


def test_unknown_status_rejected(small_cfg):
    df = rows(MODELS)
    df.loc[0, "qbic_status"] = "weird"
    with pytest.raises(CacheImportError, match="unknown qbic_status"):
        QbicCache(small_cfg).import_results({"run_id": "r1"}, df, {KEY}, stats=True)
