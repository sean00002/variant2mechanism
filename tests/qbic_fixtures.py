"""Shared set-up for the QBiC-SELEX backend tests: a small config on the packaged example models."""

import copy
import os
from pathlib import Path

import pytest
import qbic_selex

from variant2mechanism.config import Config, load_config

EXAMPLES = Path(qbic_selex.__file__).parent / "examples" / "example_models"
MODELS = ["ETV4_eDBD_TTTGCC40NTGA_KS_yin2017_0_4_7mer", "GABPA_FL_TC40NGCGATT_YWL_jolma2025_0_2_7mer"]
FAKE = Path(__file__).parent / "fake_cluster"
REMOTE = "/remote/jobs"


@pytest.fixture
def small_cfg(tmp_path) -> Config:
    cfg = Config(copy.deepcopy(dict(load_config())))
    (tmp_path / "models.txt").write_text("# test list\n" + "\n".join(MODELS) + "\n")
    cfg["data"] = {**cfg["data"], "model_list": str(tmp_path / "models.txt"), "weights_dir": str(EXAMPLES)}
    cfg["cache"] = {**cfg["cache"], "db": str(tmp_path / "cache" / "qbic.sqlite"),
                    "log": str(tmp_path / "runs" / "qbic_calls.jsonl")}
    cfg["cluster"] = {**cfg["cluster"], "jobs_dir": REMOTE}
    cfg["slurm"] = {**cfg["slurm"], "poll_seconds": 0, "model_chunks": 2}
    return cfg


@pytest.fixture
def fake_cluster(tmp_path, monkeypatch):
    root = tmp_path / "remote_jobs"
    root.mkdir()
    for name in ("ssh", "sbatch", "squeue", "sacct"):
        os.chmod(FAKE / name, 0o755)
    monkeypatch.setenv("FAKE_ROOT", str(root))
    monkeypatch.setenv("FAKE_REMOTE", REMOTE)
    monkeypatch.setenv("FAKE_BIN", str(FAKE))
    monkeypatch.setenv("FAKE_WEIGHTS", str(EXAMPLES))
    monkeypatch.setenv("FAKE_MASTER", "0")
    for var in ("FAKE_DOWN", "FAKE_FAIL_TASK", "FAKE_DROP_MODEL"):
        monkeypatch.delenv(var, raising=False)
    (tmp_path / "running").write_text("2")

    class Fake:
        ssh = str(FAKE / "ssh")
        calls_file = tmp_path / "ssh_calls.jsonl"

        @staticmethod
        def calls():
            import json
            if not Fake.calls_file.exists():
                return []
            return [json.loads(x) for x in Fake.calls_file.read_text().splitlines()]

        @staticmethod
        def running(value):
            (tmp_path / "running").write_text(str(value))

    return Fake


@pytest.fixture
def agent_cfg(small_cfg, tmp_path) -> Config:
    """small_cfg with its own budget file and HTTP/model caches, for agent tests."""
    small_cfg["budget_usd"] = {**small_cfg["budget_usd"], "state_file": str(tmp_path / "state" / "budget.json")}
    small_cfg["tools"] = {**small_cfg["tools"], "http_cache": str(tmp_path / "cache" / "http")}
    return small_cfg
