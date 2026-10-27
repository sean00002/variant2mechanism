import pytest

from variant2mechanism.cli import build_parser


def test_parser_accepts_documented_commands():
    p = build_parser()
    assert p.parse_args(["run", "--case", "tert_c228t", "--config", "full"]).case == "tert_c228t"
    assert p.parse_args(["eval", "--pilot"]).pilot
    grid = p.parse_args(["eval", "--grid", "named", "--configs", "single", "no_qbic", "--concurrency", "1"])
    assert grid.configs == ["single", "no_qbic"] and grid.concurrency == 1
    assert p.parse_args(["qbic", "import", "20261025T091500Z-3f9a1c"]).run_id.endswith("3f9a1c")


def test_parser_rejects_unknown_config():
    with pytest.raises(SystemExit):
        build_parser().parse_args(["run", "--case", "x", "--config", "grid"])
