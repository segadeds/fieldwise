"""Load and check the Fieldwise field definition (field.yaml).

The file is checked the moment it is loaded. A typo, a missing key or an
impossible value stops the program with a clear message, instead of quietly
producing wrong numbers later in the twin.

All limits below are plausibility checks for a FICTIONAL teaching field.
They are not design limits.
"""

from pathlib import Path

import yaml
from pydantic import BaseModel, ConfigDict, Field, field_validator


class StrictModel(BaseModel):
    """Shared settings for every model in this file.

    extra="forbid": an unknown key (usually a typo) is an error, not ignored.
    frozen=True:    once loaded, the field definition cannot be changed by
                    accident while the twin runs (same idea as Stream).
    """

    model_config = ConfigDict(extra="forbid", frozen=True)


class Reservoir(StrictModel):
    """The reservoir and its fluid, at the datum depth."""

    api_deg: float = Field(ge=5, le=70)  # same range as units.api_to_sg
    gor_scf_per_stb: float = Field(ge=0)  # solution GOR, Rs
    p_res_psia: float = Field(gt=0)  # absolute pressure can't be zero or negative
    datum_tvd_ft: float = Field(gt=0)  # depth where p_res_psia applies
    t_res_degf: float = Field(gt=32, le=500)  # plausible reservoir temperatures
    gas_sg: float = Field(ge=0.55, le=1.5)  # air = 1.0; methane ~0.55 is the lightest


class Well(StrictModel):
    """One producing well."""

    name: str = Field(min_length=1)
    tvd_ft: float = Field(gt=0)
    pi_stbd_per_psi: float = Field(gt=0)  # measured PI, includes current skin
    skin: float = Field(ge=-7)  # negative = stimulated; below about -7 is unrealistic
    tubing_id_in: float = Field(gt=0)
    wc_frac: float = Field(ge=0, le=1)  # a fraction, not a percentage
    gor_scf_per_stb: float = Field(ge=0)


class Facility(StrictModel):
    """Surface facility settings."""

    p_sep_psig: float = Field(ge=0)  # gauge pressure, as read by an operator
    export_line_length_ft: float = Field(gt=0)


class FieldConfig(StrictModel):
    """The whole field. Named FieldConfig, not Field, to avoid clashing with
    pydantic's Field (the same name trap as in units.py)."""

    name: str = Field(min_length=1)
    reservoir: Reservoir
    wells: list[Well] = Field(min_length=1)  # at least one well
    facility: Facility

    @field_validator("wells")
    @classmethod
    def names_must_be_unique(cls, wells: list[Well]) -> list[Well]:
        """Two wells with the same name would be impossible to tell apart."""
        names = [well.name for well in wells]
        repeated = sorted({name for name in names if names.count(name) > 1})
        if repeated:
            raise ValueError(f"Well names must be unique; repeated: {repeated}")
        return wells


def load_field(path: str | Path) -> FieldConfig:
    """Read field.yaml and return the checked field definition.

    Raises pydantic.ValidationError if any key is missing, misspelled or
    outside its allowed range. The message names the exact key and value.
    """
    text = Path(path).read_text(encoding="utf-8")
    data = yaml.safe_load(text)  # safe_load only reads plain data, never runs code
    if data is None:
        raise ValueError(f"{path} is empty.")
    return FieldConfig.model_validate(data)