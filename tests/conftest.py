import os
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[1]
DATA = REPO / "data"
DATA_READY = (DATA / "TableS5_model_to_tfs_mapping.csv").exists() and (DATA / "reference").is_dir()


def pytest_collection_modifyitems(config, items):
    skips = {
        "data": (not DATA_READY, "needs the data/ folder"),
        "cluster": (os.environ.get("QBIC_CLUSTER") != "1", "set QBIC_CLUSTER=1 to run cluster tests"),
        "live": (os.environ.get("V2M_LIVE") != "1", "set V2M_LIVE=1 to run live tests"),
    }
    for item in items:
        for mark, (skip, reason) in skips.items():
            if skip and mark in item.keywords:
                item.add_marker(pytest.mark.skip(reason=reason))


from qbic_fixtures import agent_cfg, fake_cluster, small_cfg  # noqa: E402,F401  (shared fixtures)
