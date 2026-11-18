from dataclasses import dataclass
import math
from fieldwise import units

# Frozen so a downstream unit can’t change a stream that another part of the field still uses.
@dataclass(frozen=True)  
class Stream:
    """Oil, water and gas flowing at one point in the field.
    Rates at standard conditions (14.696 psia, 60 °F)
    """

    q_oil_stbd: float
    q_water_bwpd: float
    q_gas_mscfd: float
    p_psia: float
    t_degf: float
    fluid: dict | None = None

    def __post_init__(self):
        if self.q_oil_stbd < 0:
            raise ValueError(
                f"Oil rate must be non-negative, got {self.q_oil_stbd} STB/d."
            )
        if self.q_water_bwpd < 0:
            raise ValueError(
                f"Water flow rate must be non-negative, got {self.q_water_bwpd} BWPD."
            )
        if self.q_gas_mscfd < 0:
            raise ValueError(
                f"Gas flow rate must be non-negative, got {self.q_gas_mscfd} Mscfd."
            )
        if self.p_psia <= 0:
            raise ValueError(f"Pressure must be positive, got {self.p_psia} psia.")
        if self.t_degf <= -units.DEGR_OFFSET:  # Absolute zero in Fahrenheit
            raise ValueError(
                f"Temperature must be above absolute zero, got {self.t_degf} degF."
            )

    @property
    def q_liquid_bpd(self) -> float:
        """Calculate the total liquid flow rate in barrels per day."""
        return self.q_oil_stbd + self.q_water_bwpd

    @property
    def water_cut_frac(self) -> float:
        """Calculate the water cut as a fraction of total liquid flow."""
        total_liquid = self.q_liquid_bpd
        if total_liquid == 0:
            return float("nan")  # Undefined water cut if no liquid is produced
        return self.q_water_bwpd / total_liquid

    @property
    def gor_scf_per_stb(self) -> float:
        """Calculate the Gas-Oil Ratio (GOR) in standard cubic feet per stock tank barrel."""
        if self.q_oil_stbd == 0 and self.q_gas_mscfd == 0:
            return float("nan")  # Undefined GOR if no oil and no gas is produced
        if self.q_oil_stbd == 0:
            return math.inf  # Infinite GOR if no oil is produced
        return (
            units.mscfd_to_scfd(self.q_gas_mscfd) / self.q_oil_stbd
        )  # Convert mscfd to scf and divide by stb
