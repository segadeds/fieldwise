# FIELDWISE Learning Log

## Week 1: How an oil field produces

**Source:** Guo, Lyons & Ghalambor, *Petroleum Production Engineering* (1st ed., 2007), Ch. 1, sections 1.1–1.9, and Economides et al., *Petroleum Production Systems* (2nd ed.), Ch. 1. Confirm the chapter numbers against your editions.
**Status:** Learning exercise only. The FIELDWISE twin is not a design tool.

---

## 1. The big picture

A production engineer's job is to get as much oil and gas out as possible, at a reasonable cost.

The fluid follows this path:

**Reservoir → Well → Wellhead → Gathering → Separator → Export**

Each step changes the pressure, temperature or composition of the fluid. The twin will model these steps one at a time.

---

## 2. Reservoir

A reservoir is rock that holds hydrocarbons (HC) and lets them flow. Sandstone and carbonates often do both. Shale has some porosity, so it can hold oil, but its permeability is very low, so the oil cannot flow out easily.

**How we find it:** well logs and seismic surveys give clues about likely zones before drilling. Logs are clues, not proof.
- **Resistivity log:** salty water conducts electricity well, so it reads low resistivity. Hydrocarbons read high resistivity. Fresh water also reads high, so a high reading is not always HC.
- **SP (spontaneous potential) log:** it deflects from the shale baseline when it passes permeable rock like sandstone. It shows where fluid can flow, not whether that fluid is HC.

**Five things to know about any reservoir:**

| Term | Plain meaning | Typical unit |
|---|---|---|
| Porosity (φ) | Share of the rock that is empty space (pores). The pores can hold oil, gas or water. | fraction (0 to 1) or % |
| Permeability (k) | How easily fluid flows through the pores. High porosity does not guarantee high permeability. | md (millidarcy) |
| Thickness / pay height (h) | How thick the productive rock is. | ft |
| Saturation (S) | Share of the pore space filled by each fluid. | fraction |
| Areal extent (A) | How much ground area the reservoir covers. | acres |

**Saturation:** Pores usually hold more than one fluid. Saturations add up to 1: `So + Sw + Sg = 1` (oil, water, gas). Knowing the saturation before development tells you how much of the pore space is actually oil.

**Two kinds of water:**
- **Connate water** was trapped in the pores when the rock formed. It sits with the oil in the same reservoir and mostly cannot be produced.
- **An aquifer** is a large, separate body of water-filled rock next to the reservoir. It can push oil toward the wells (water drive).

**Original oil in place:** area is one input. You need all of these together:

```
N_stb = 7758 * A_acres * h_ft * phi * (1 - Sw) / Bo_rb_per_stb
```

- 7758 converts acre-ft to barrels.
- `Bo` is the oil formation volume factor: reservoir barrels per stock-tank barrel (oil shrinks as it comes to the surface).
- **Assumption:** the reservoir is a simple block with uniform properties. Real reservoirs are not.

---

## 3. Well

Wells are drilled down to the reservoir depth. They can be vertical or horizontal, and a field can have many.

- **Casing:** steel pipe cemented into the hole. It is run in stages and each stage supports the next.
- **Intermediate string:** optional. Only needed when extra formations must be protected or isolated.
- **Production casing and tubing:** the last stage, which reaches the reservoir. The fluid flows up the tubing.

**Completion types:** open hole, slotted liner, gravel pack, and cemented casing with perforations.

---

## 4. Well productivity

The productivity index (J) tells you how much a well produces for each psi of pressure drop.

```
J = q / (P - Pwf)
```

| Symbol | Meaning | Unit |
|---|---|---|
| J | productivity index | STB/D/psi |
| q | flow rate | STB/D |
| P | average reservoir pressure | psi |
| Pwf | flowing bottomhole pressure | psi |
| P − Pwf | drawdown | psi |

J belongs to the reservoir and the well. It depends on things like permeability (k) and pay height (h). Lowering Pwf makes the drawdown bigger, so the **rate q goes up**, but J stays the same. What production engineers optimise is the rate, by managing Pwf.

**J is constant only when:**
- One fluid phase is flowing (no free gas).
- Flow has settled (pseudo-steady state).
- Pwf stays **above** the bubble point.

Below the bubble point the line curves, so you use an IPR curve instead (for example Vogel).

Reservoir pressure is roughly constant only over short times. It falls as the field is depleted, unless water or gas injection supports it.

**Bubble point:**
- Above the bubble point, all the gas is dissolved in the oil. The oil is *undersaturated*.
- Below it, gas comes out of the oil. There is free gas in the reservoir and the oil is *saturated*.

**GOR (gas-oil ratio, in scf/STB) by fluid type:**
- Gas wells: above 100,000 scf/STB
- Condensate wells: 5,000 to 100,000 scf/STB
- Oil wells: below 5,000 scf/STB

These cut-offs are rules of thumb and differ between books. Fluids are also classed by more than GOR. Check the table in your book and note the page.

---

## 5. Wellhead

The wellhead holds the valves that control flow. This is a concept summary; real sites follow their own written procedures and permits to work.

Flow path through the tree: **master valve → wing valve → choke → flowline**.

- **Master valve:** isolates the well from the surface.
  - To open: check that the downstream valves are open. Open the master valve a little and wait until the hissing stops, which means the pressure has equalised. Then open it fully.
  - Shut down in the opposite order.
- **Swab valve:** at the top of the tree. It gives a straight path down into the well for wireline or coiled-tubing work (for example fishing).
- **Needle valve:** a small valve where a pressure gauge is connected, used to read or bleed pressure.
- **Wing / flow valve:** on the side of the tree. The flow leaves the tree here and then passes through the choke, which sits just after it.

---

## 6. Choke

The choke is a narrow opening that limits flow and sets the rate.

- **Size:** given in 64ths of an inch. A "32/64" choke is 0.5 in.
- **Where:** at the surface, or at the bottom of the well (bottomhole).

A choke raises Pwf, so the drawdown gets smaller and the rate goes down. Chokes are used to *control* the rate and to protect the well, for example to limit sand production or water coning.

A bottomhole choke moves the pressure drop and the cooling down into the warm part of the well, which lowers the hydrate risk at surface. Its drawback is that it is hard to change, so the surface choke is the usual choice.

**Why the heater goes on first:** when gas expands across the choke, it gets cold (Joule-Thomson cooling). Cold gas with water under pressure can form **hydrates**, ice-like solids that block the line. Oil can also drop **wax** when it cools. The heater, upstream of the choke, keeps the fluid warm enough to avoid both.

---

## 7. Gathering, separator, export

After the choke, the fluid goes through the inlet manifold, the separator and other equipment. They process and handle the fluids before export.

---

## 8. The production system as one pressure chain (Guo Ch. 1)

### 8.1 The pressure chain

```
Reservoir pressure (P) → Bottomhole pressure (Pwf) → Wellhead pressure (Pwh) → Separator pressure (Psep)
   highest                                                                          lowest
```

**Why the oil flows at all:** fluid always moves from high pressure to low pressure. The reservoir pressure is the "push", and the separator pressure is the "back-pressure" at the end of the line. The total pressure available to move the oil is **P − Psep**.

**What sets the rate:** every part of the system uses up some of that pressure. The well settles at the one rate where all the pressure drops added together equal exactly P − Psep. If you change any one part (a bigger choke, a lower separator pressure, damaged rock), the rate moves to a new balance. This is the idea behind nodal analysis (Module 2) and the network solve (Module 3).

### 8.2 Where the pressure gets used up

| Part | What causes the pressure drop |
|---|---|
| Reservoir rock and near-wellbore | Friction as fluid squeezes through the pores toward the well. Damage near the well (skin) adds extra loss. |
| Tubing | Mostly the **weight of the fluid column** that must be lifted to surface, plus friction against the pipe wall. In oil wells the weight part is usually the bigger one. |
| Choke | A deliberate, sharp drop through a small opening, used to control the rate. |
| Flowline to the separator | Friction along the pipe, plus any uphill sections. |

### 8.3 Units (Guo section 1.9)

Production engineering mostly uses **oilfield (US) units**: psi, °F, ft, bbl, STB/d, scf, cp. The textbook correlations are published in these units, so FIELDWISE uses them too, with the unit in every variable name.

| Item | Meaning | Why it matters |
|---|---|---|
| **psia vs psig** | psia is absolute pressure (measured from vacuum). psig is gauge pressure (measured from the atmosphere). `psia = psig + 14.696` | Correlations need **psia**. A gauge reads psig. Mixing them gives about a 15 psi error, which is large at low pressures such as separators. |
| **°F vs °R** | °R (Rankine) is absolute temperature. `°R = °F + 459.67` | Gas equations (PV = ZnRT) need absolute temperature. Using °F in them gives wrong answers. |
| **Standard conditions** | 14.696 psia and 60 °F | A "stock-tank barrel" or "standard cubic foot" only means something at a stated pressure and temperature, because gas volume changes with both. |

**Assumptions to remember:**
- `psia = psig + 14.696` uses standard atmospheric pressure. Real atmospheric pressure varies a little with elevation and weather.
- Some regions and contracts use 14.65 or 14.73 psia as the standard pressure. Always check which one a data source uses.

