from pathlib import Path

import pytest
import yaml
from pydantic import ValidationError

from fieldwise.config import FieldConfig, load_field

FIELD_YAML = Path(__file__).resolve().parents[1] / "field.yaml"


def load_raw() -> dict:
    """field.yaml as a plain dictionary, so a test can break a copy of it."""
    return yaml.safe_load(FIELD_YAML.read_text(encoding="utf-8"))


def test_real_field_loads():
    field = load_field(FIELD_YAML)
    assert len(field.wells) >= 6
    assert field.reservoir.p_res_psia == pytest.approx(4000)


def test_typo_in_key_fails():
    data = load_raw()
    data["reservoir"]["p_res_pisa"] = data["reservoir"].pop("p_res_psia")
    with pytest.raises(ValidationError):
        FieldConfig.model_validate(data)


def test_water_cut_above_one_fails():
    data = load_raw()
    data["wells"][0]["wc_frac"] = 30  # meant 0.30
    with pytest.raises(ValidationError):
        FieldConfig.model_validate(data)


def test_duplicate_well_name_fails():
    data = load_raw()
    data["wells"][1]["name"] = data["wells"][0]["name"]
    with pytest.raises(ValidationError):
        FieldConfig.model_validate(data)


def test_negative_skin_allowed():
    data = load_raw()
    data["wells"][0]["skin"] = -2  # a stimulated well is valid
    FieldConfig.model_validate(data)  # must not raise