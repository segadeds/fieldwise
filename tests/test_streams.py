import pytest
import math
import dataclasses
from fieldwise.streams import Stream


def test_liquid_rate():
    s = Stream(
        q_oil_stbd=1000.0,
        q_water_bwpd=500.0,
        q_gas_mscfd=600.0,
        p_psia=1500.0,
        t_degf=100.0,
        fluid=None,
    )
    assert s.q_liquid_bpd == pytest.approx(1500.0)
    assert s.water_cut_frac == pytest.approx(0.3333, abs=1e-4)
    assert s.gor_scf_per_stb == pytest.approx(600.0, abs=1e-4)


def test_gor():
    s = Stream(
        q_oil_stbd=0.0,
        q_water_bwpd=500.0,
        q_gas_mscfd=600.0,
        p_psia=1500.0,
        t_degf=100.0,
        fluid=None,
    )
    assert s.water_cut_frac == pytest.approx(1.0, abs=1e-4)
    assert math.isinf(s.gor_scf_per_stb)


def test_zero_oil_water_cut():
    s = Stream(
        q_oil_stbd=0.0,
        q_water_bwpd=0.0,
        q_gas_mscfd=600.0,
        p_psia=1500.0,
        t_degf=100.0,
        fluid=None,
    )
    assert math.isnan(s.water_cut_frac)
    assert math.isinf(s.gor_scf_per_stb)


def test_negative_oil_rejected():
    with pytest.raises(ValueError):
        Stream(
            q_oil_stbd=-500.0,
            q_water_bwpd=500.0,
            q_gas_mscfd=600.0,
            p_psia=1500.0,
            t_degf=100.0,
        )


def test_zero_pressure_rejected():
    with pytest.raises(ValueError):
        Stream(
            q_oil_stbd=1000.0,
            q_water_bwpd=500.0,
            q_gas_mscfd=600.0,
            p_psia=0.0,
            t_degf=100.0,
        )


def test_stream_is_frozen():
    s = Stream(
        q_oil_stbd=1000.0,
        q_water_bwpd=500.0,
        q_gas_mscfd=600.0,
        p_psia=1500.0,
        t_degf=100.0,
        fluid=None,
    )
    with pytest.raises(dataclasses.FrozenInstanceError):
        s.p_psia = 500.0


def test_shut_in_gor_is_nan():
    s = Stream(
        q_oil_stbd=0.0, q_water_bwpd=0.0, q_gas_mscfd=0.0, p_psia=1500.0, t_degf=100.0
    )
    assert math.isnan(s.gor_scf_per_stb)
