ATM_PSIA = 14.696
KPA_PER_PSI = 6.894757
DEGR_OFFSET = 459.67
FT3_PER_BBL = 5.614583333
M3_PER_BBL = 0.158987294928
M_PER_FT = 0.3048
SCF_PER_MSCF = 1000


def psig_to_psia(p_psig: float) -> float:
    """Convert gauge pressure to absolute pressure.

    psia = psig + ATM_PSIA
    Assumes standard atmospheric pressure (14.696 psia).
    """
    return p_psig + ATM_PSIA


def psia_to_psig(p_psia: float) -> float:
    """Convert absolute pressure to gauge pressure.

    psig = psia - ATM_PSIA
    Assumes standard atmospheric pressure (14.696 psia).
    """
    return p_psia - ATM_PSIA


def psi_to_kpa(p_psi: float) -> float:
    """Convert pressure to kilopascals.

    kPa = psi * 6.894757
    """
    return p_psi * KPA_PER_PSI


def kpa_to_psi(p_kpa: float) -> float:
    """Convert kilopascals to pressure.

    psi = kPa / 6.894757
    """
    return p_kpa / KPA_PER_PSI


def degf_to_degr(t_degf: float) -> float:
    """Convert degrees Fahrenheit to degrees Rankine.

    degR = degF + 459.67
    """
    return t_degf + DEGR_OFFSET


def degr_to_degf(t_degr: float) -> float:
    """Convert degrees Rankine to degrees Fahrenheit.

    degF = degR - 459.67
    """
    return t_degr - DEGR_OFFSET


def degf_to_degc(t_degf: float) -> float:
    """Convert degrees Fahrenheit to degrees Celsius.

    degC = (degF - 32) * 5/9
    """
    return (t_degf - 32) * 5 / 9


def degc_to_degf(t_degc: float) -> float:
    """Convert degrees Celsius to degrees Fahrenheit.

    degF = degC * 9/5 + 32
    """
    return t_degc * 9 / 5 + 32


def bbl_to_ft3(v_bbl: float) -> float:
    """Convert volume in barrels to volume in cubic feet.

    ft^3 = bbl * 5.614583
    """
    return v_bbl * FT3_PER_BBL


def ft3_to_bbl(v_ft3: float) -> float:
    """Convert volume in cubic feet to volume in barrels.

    bbl = ft^3 / 5.614583
    """
    return v_ft3 / FT3_PER_BBL


def bbl_to_m3(v_bbl: float) -> float:
    """Convert volume in barrels to volume in cubic meters.

    m^3 = bbl * 0.158987
    """
    return v_bbl * M3_PER_BBL


def m3_to_bbl(v_m3: float) -> float:
    """Convert volume in cubic meters to volume in barrels.

    bbl = m^3 / 0.158987
    """
    return v_m3 / M3_PER_BBL


def ft_to_m(l_ft: float) -> float:
    """Convert length in feet to length in meters.

    m = ft * 0.3048
    """
    return l_ft * M_PER_FT


def m_to_ft(l_m: float) -> float:
    """Convert length in meters to length in feet.

    ft = m / 0.3048
    """
    return l_m / M_PER_FT


def api_to_sg(api_deg: float) -> float:
    """Convert API gravity to specific gravity.

    sg = 141.5 / (api_deg + 131.5)
    """
    # API gravity is typically in the range of 5–70 °API for crude oil. 
    # Values outside this range may indicate an error or an unusual substance.
    # So we stop with an error rather than return a silently wrong answer.
    if api_deg < 5 or api_deg > 70:
        raise ValueError(
            f"API gravity {api_deg} is outside 5–70 °API (typical crude range)."
        )

    return 141.5 / (api_deg + 131.5)


def sg_to_api(sg: float) -> float:
    """Convert specific gravity to API gravity.

    api_deg = 141.5 / sg - 131.5
    """
    api_deg = 141.5 / sg - 131.5
    if api_deg < 5 or api_deg > 70:
        raise ValueError(
            f"Specific gravity {sg} is outside 5–70 °API (typical crude range)."
        )

    return api_deg


def mscfd_to_scfd(mscf_per_day: float) -> float:
    """Convert flow rate in thousand standard cubic feet per day to standard cubic feet per day.

    scfd = mscf/day * 1000
    """
    return mscf_per_day * SCF_PER_MSCF


def scfd_to_mscfd(scfd: float) -> float:
    """Convert flow rate in standard cubic feet per day to thousand standard cubic feet per day.

    mscf/day = scfd / 1000
    """
    return scfd / SCF_PER_MSCF
