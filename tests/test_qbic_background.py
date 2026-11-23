"""The packaged QBiC-SELEX background: per-group cut-offs for a "large" prediction."""

import hashlib

from variant2mechanism.qbic import background


def test_the_table_is_the_one_the_summary_names_and_covers_every_group():
    cutoffs = background.group_cutoffs()
    info = background.summary()
    assert len(cutoffs) == 631 and all(value > 0 for value in cutoffs.values())
    assert hashlib.md5(background.TABLE.read_bytes()).hexdigest() == info["table_md5"]
    assert info["variants_tallied"] == 21772794 and info["table"] == background.TABLE.name
    assert sum(info["base_changes"].values()) == info["variants_tallied"]


def test_a_group_of_many_models_needs_a_larger_z_than_a_group_of_one():
    """The group's value is the largest |z| among its models, so the cut-off grows with the group's size. One cut-off
    for all groups would call nearly every variant large for the 81 homeodomain models."""
    cutoffs = background.group_cutoffs()
    assert cutoffs["G001"] > 30 > sorted(cutoffs.values())[len(cutoffs) // 2] > 4.054925


def test_in_top_share_is_a_yes_a_no_or_unknown():
    cutoff = background.group_cutoffs()["G001"]
    assert background.in_top_share("G001", cutoff) is True and background.in_top_share("G001", -cutoff) is True
    assert background.in_top_share("G001", cutoff - 0.01) is False
    assert background.in_top_share("G001", None) is None and background.in_top_share("no such group", 99.0) is None
