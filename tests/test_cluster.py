import pytest

from variant2mechanism.cli import main as cli_main
from variant2mechanism.qbic.cluster import (
    FIX,
    Cluster,
    ClusterJobFailed,
    ClusterTimeout,
    ClusterUnavailable,
    chunk_models,
    make_run_id,
)
from variant2mechanism.qbic.variants import Variant

TERT = Variant.make("chr5", 1295113, "G", "A")
OTHER = Variant.make("chr8", 127401060, "G", "T")


def cluster(cfg, fake, **kw):
    return Cluster(cfg, ssh=fake.ssh, sleep=lambda s: None, **kw)


def test_run_id_and_chunks():
    rid = make_run_id(["b", "a"], now="20261025T091500Z")
    assert rid.startswith("20261025T091500Z-") and len(rid.split("-")[1]) == 6
    assert rid == make_run_id(["a", "b"], now="20261025T091500Z")
    assert chunk_models(list("abcde"), 2) == [["a", "c", "e"], ["b", "d"]]


def test_no_connection_gives_fix_text(small_cfg, fake_cluster, monkeypatch):
    monkeypatch.setenv("FAKE_MASTER", "255")
    monkeypatch.setenv("FAKE_DOWN", "1")
    with pytest.raises(ClusterUnavailable, match=f"ssh -fN {small_cfg['cluster']['host']}"):
        cluster(small_cfg, fake_cluster).run([TERT], stats=True)
    assert str(ClusterUnavailable(FIX)) == FIX


def test_end_to_end_with_stats(small_cfg, fake_cluster):
    c = cluster(small_cfg, fake_cluster)
    run_id = c.run([TERT, OTHER], stats=True)
    assert c.cache.cached([TERT.key(), OTHER.key()], stats=True) == {TERT.key(), OTHER.key()}
    calls = fake_cluster.calls()
    remote_calls = [a for a in calls if "-O" not in a]
    assert remote_calls and all(a[:2] == ["-o", "BatchMode=yes"] for a in remote_calls)   # argv without "ssh"
    assert any(a[-1].endswith("&& env -u SLURM_JOB_ID sbatch --parsable job.sbatch") for a in calls)
    run = c.load_run(run_id)
    assert run["slurm_job"] == "4242" and run["gpu_name"] == "FakeGPU 1"
    assert run["task_seconds"] == {"00": 3, "01": 3} and len(run["effect_checks"]) == 3
    assert c.cache.runs().run_id.tolist() == [run_id]


def test_cache_hit_makes_no_ssh_call(small_cfg, fake_cluster):
    cluster(small_cfg, fake_cluster).run([TERT], stats=True)
    n = len(fake_cluster.calls())
    assert cluster(small_cfg, fake_cluster).run([TERT], stats=True) is None
    assert len(fake_cluster.calls()) == n


def test_effects_only_does_not_satisfy_stats(small_cfg, fake_cluster):
    c = cluster(small_cfg, fake_cluster)
    c.run([TERT], stats=False)
    assert c.cache.cached([TERT.key()], stats=False) == {TERT.key()}
    assert c.cache.cached([TERT.key()], stats=True) == set()
    script = (fake_cluster.calls_file.parent / "remote_jobs").glob("*/job.sbatch")
    assert "--compute-stats" not in next(script).read_text()


def test_failed_task_gives_log_tail(small_cfg, fake_cluster, monkeypatch):
    monkeypatch.setenv("FAKE_FAIL_TASK", "1")
    with pytest.raises(ClusterJobFailed, match="covariance missing") as e:
        cluster(small_cfg, fake_cluster).run([TERT], stats=True)
    assert "tasks 01" in str(e.value)


def test_missing_model_is_rejected(small_cfg, fake_cluster, monkeypatch):
    from variant2mechanism.qbic.cache import CacheImportError
    monkeypatch.setenv("FAKE_DROP_MODEL", "ETV4_eDBD_TTTGCC40NTGA_KS_yin2017_0_4_7mer")
    c = cluster(small_cfg, fake_cluster)
    with pytest.raises(CacheImportError, match="model set differs"):
        c.run([TERT], stats=True)
    assert c.cache.cached([TERT.key()]) == set()


def test_timeout_then_import(small_cfg, fake_cluster, monkeypatch):
    fake_cluster.running("forever")
    small_cfg["slurm"]["timeout_hours"] = 0.001
    ticks = iter(range(0, 10_000, 5))
    c = cluster(small_cfg, fake_cluster, clock=lambda: next(ticks))
    with pytest.raises(ClusterTimeout) as e:
        c.run([TERT], stats=True)
    run_id = e.value.run_id
    assert f"v2m qbic import {run_id}" in str(e.value)
    assert c.cache.cached([TERT.key()]) == set()

    fake_cluster.running(1)
    monkeypatch.setattr("variant2mechanism.cli.get_backend", lambda: cluster(small_cfg, fake_cluster))
    assert cli_main(["qbic", "import", run_id]) == 0
    assert c.cache.cached([TERT.key()]) == {TERT.key()}


@pytest.mark.cluster
def test_real_effects_only_tert():
    c = Cluster()
    run_id = c.run([TERT], stats=False, partition="compsci", gres="", device="cpu", model_chunks=2)
    assert run_id is None or c.cache.cached([TERT.key()], stats=False) == {TERT.key()}
