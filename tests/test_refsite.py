from pathlib import Path

import pytest
import qbic_selex

from variant2mechanism.qbic.refsite import _model, model_path, site_strength

EXAMPLES = Path(qbic_selex.__file__).parent / "examples" / "example_models"
GABPA = "GABPA_FL_TC40NGCGATT_YWL_jolma2025_0_2_7mer"


def test_percentiles_in_range():
    ref = "CCCGGAGGGGCTGGGCCGGGG"      # arbitrary 21-bp sequence
    alt = ref[:10] + "A" + ref[11:]
    r = site_strength(GABPA, ref, alt, weights_dir=EXAMPLES)
    assert 0 <= r["ref_percentile"] <= 100 and 0 <= r["alt_percentile"] <= 100 and r["k"] == 7


def test_top_kmer_gives_100():
    model, _ = _model(str(model_path(GABPA, EXAMPLES)))
    top = max(model.complete, key=model.complete.get)
    seq = "A" * 7 + top + "A" * 7     # top 7-mer covers index 10
    assert site_strength(GABPA, seq, seq, weights_dir=EXAMPLES)["ref_percentile"] == 100.0


def test_unknown_model():
    with pytest.raises(KeyError):
        model_path("NOPE_model", EXAMPLES)
