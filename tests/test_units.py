import pytest

from fieldwise.units import (
    api_to_sg,
    bbl_to_ft3,
    bbl_to_m3,
    degc_to_degf,
    degf_to_degc,
    degf_to_degr,
    degr_to_degf,
    ft_to_m,
    kpa_to_psi,
    m_to_ft,
    mscfd_to_scfd,
    psi_to_kpa,
    psia_to_psig,
    psig_to_psia,
    sg_to_api,
)


def test_psia_to_psig():
    assert psia_to_psig(29.392) == pytest.approx(14.696)


def test_psig_to_psia():
    assert psig_to_psia(150) == pytest.approx(164.696)


def test_psi_to_kpa():
    assert psi_to_kpa(2000) == pytest.approx(13789.514)


def test_kpa_to_psi():
    assert kpa_to_psi(13789.514) == pytest.approx(2000)


def test_degf_to_degr():
    assert degf_to_degr(32) == pytest.approx(491.67)


def test_degr_to_degf():
    assert degr_to_degf(491.67) == pytest.approx(32)


def test_degf_to_degc():
    assert degf_to_degc(32) == pytest.approx(0)


def test_degc_to_degf():
    assert degc_to_degf(0) == pytest.approx(32)


def test_ft_to_m():
    assert ft_to_m(5280) == pytest.approx(1609.344)


def test_sg_to_api():
    assert sg_to_api(1.0) == pytest.approx(10)


def test_api_to_sg():
    assert api_to_sg(32) == pytest.approx(0.8654, abs=1e-4)


def test_bbl_to_ft3():
    assert bbl_to_ft3(1) == pytest.approx(5.61458333333)


def test_bbl_to_m3():
    assert bbl_to_m3(1) == pytest.approx(0.158987294928)


def test_mscfd_to_scfd():
    assert mscfd_to_scfd(600) == pytest.approx(600000)


def test_api_to_sg_rejects_100_api():
    with pytest.raises(ValueError):
        api_to_sg(100)


def test_round_trip_ft_m():
    assert m_to_ft(ft_to_m(1234.5)) == pytest.approx(1234.5)


def test_round_trip_psia_psig():
    assert psia_to_psig(psig_to_psia(150)) == pytest.approx(150)


def test_round_trip_api_sg():
    assert sg_to_api(api_to_sg(32)) == pytest.approx(32)
