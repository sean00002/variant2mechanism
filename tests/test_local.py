"""The local backend, with the real qbic-selex on the packaged example models and a tiny test genome."""

import random
import subprocess
from pathlib import Path

import pysam
import pytest
from qbic_fixtures import EXAMPLES, MODELS

from variant2mechanism.qbic.backend import BackendError, JobFailed, get_backend
from variant2mechanism.qbic.local import LocalBackend, md5_file
from variant2mechanism.qbic.variants import Variant

EXAMPLE_COVS = Path("~/.cache/variant2mechanism/qbic_examples/example_covs").expanduser()


@pytest.fixture
def local_cfg(small_cfg, tmp_path):
    rng = random.Random(7)
    seq = "".join(rng.choice("ACGT") for _ in range(200))
    fa = tmp_path / "genome" / "test.fa"
    fa.parent.mkdir()
    fa.write_text(">chr5\n" + seq + "\n")
    pysam.faidx(str(fa))
    small_cfg["cluster"] = {**small_cfg["cluster"], "genome_fai_md5": md5_file(Path(str(fa) + ".fai"))}
    small_cfg["local"] = {"qbic_selex": "qbic-selex", "model_dir": str(EXAMPLES), "cov_dir": str(EXAMPLE_COVS),
                          "genome": str(fa), "workers": 2, "device": "cpu", "jobs_dir": str(tmp_path / "jobs")}
    small_cfg["qbic"] = {"backend": "local"}
    small_cfg.seq = seq
    return small_cfg


def snvs(seq):
    out = []
    for pos in (50, 120):
        ref = seq[pos - 1]
        out.append(Variant.make("chr5", pos, ref, "A" if ref != "A" else "C"))
    return out


def test_factory(local_cfg):
    assert isinstance(get_backend(local_cfg), LocalBackend)
    with pytest.raises(BackendError):
        get_backend(local_cfg, "nope")


def test_effects_only_run_fills_the_cache(local_cfg):
    b = LocalBackend(local_cfg)
    vs = snvs(local_cfg.seq)
    run_id = b.run(vs, stats=False)
    run = b.load_run(run_id)
    assert run["rows_imported"] == 4 and set(run["task_seconds"]) == {"00", "01"}
    assert len(run["effect_checks"]) == 3 and max(c["diff"] for c in run["effect_checks"]) < 1e-4
    assert b.cache.cached([v.key() for v in vs], stats=False) == {v.key() for v in vs}
    assert b.run(vs, stats=False) is None                    # second time: a cache hit, nothing runs


def test_genome_index_must_match_the_cluster(local_cfg):
    local_cfg["cluster"]["genome_fai_md5"] = "0" * 32
    with pytest.raises(BackendError, match="differs from the cluster"):
        LocalBackend(local_cfg).run(snvs(local_cfg.seq), stats=False)


def test_missing_covariances_reported(local_cfg, tmp_path):
    local_cfg["local"]["cov_dir"] = str(tmp_path / "none")
    with pytest.raises(BackendError, match="covariances not found"):
        LocalBackend(local_cfg).run(snvs(local_cfg.seq), stats=True)


def test_failed_chunk_gives_log_tail(local_cfg):
    def runner(argv, cwd, stdout, stderr):
        if "models_01.txt" in argv:
            stdout.write("ModelInputError: something broke\n")
            return subprocess.CompletedProcess(argv, 1)
        return subprocess.run(argv, cwd=cwd, stdout=stdout, stderr=stderr)
    with pytest.raises(JobFailed, match="something broke"):
        LocalBackend(local_cfg, runner=runner).run(snvs(local_cfg.seq), stats=False)


@pytest.mark.skipif(not EXAMPLE_COVS.is_dir(), reason="needs qbic-selex download examples in ~/.cache")
def test_statistics_run_with_example_covariances(local_cfg):
    b = LocalBackend(local_cfg)
    vs = snvs(local_cfg.seq)
    b.run(vs, stats=True)
    df = b.cache.scores(vs[0].key(), stats=True)
    assert sorted(df.model) == sorted(MODELS) and df.z.notna().all() and df.p.between(0, 1).all()
