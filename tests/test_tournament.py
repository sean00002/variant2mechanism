"""Pairwise comparison of chains: the Bradley-Terry fit and the null check the verdict uses."""

import pytest

from variant2mechanism.agent.stages.tournament import beats_null, bradley_terry


def test_consistent_wins_order_the_chains():
    games = [("H1", "H2", 1.0), ("H1", "H2", 1.0), ("H1", "H3", 1.0), ("H1", "H3", 1.0),
             ("H2", "H3", 1.0), ("H2", "H3", 1.0)]
    s = bradley_terry(["H1", "H2", "H3"], games)
    assert s["H1"] > s["H2"] > s["H3"] > 0 and sum(s.values()) == pytest.approx(1.0, abs=1e-3)


def test_ties_and_order_flips_leave_the_chains_equal():
    flips = [("H1", "H2", 1.0), ("H1", "H2", 0.0), ("H1", "H3", 0.5), ("H1", "H3", 0.5),
             ("H2", "H3", 1.0), ("H2", "H3", 0.0)]
    s = bradley_terry(["H1", "H2", "H3"], flips)
    assert max(s.values()) - min(s.values()) < 1e-3


def test_beats_null_needs_both_orders():
    t = {"matches": [{"pair": ["H1", "H3"], "scores": [1.0, 1.0]}, {"pair": ["H3", "H2"], "scores": [0.0, 1.0]}]}
    assert beats_null(t, "H1", "H3") is True
    assert beats_null(t, "H2", "H3") is False          # won one order only: a tie, not a win
    assert beats_null(None, "H1", "H3") is None and beats_null(t, "H4", "H3") is None
