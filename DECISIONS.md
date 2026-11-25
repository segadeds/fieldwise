# Decisions

## D-001 Units
- oilfield units are used for this project: psi, °F, ft, bbl, STB/d, scf, cp.
- standard pressure and temperature conditions for this project are 14.696psia and 60F
- atmospheric pressure assumed for psig → psia is psia = psig + 14.696

## D-002 Steady state first
- a model with time is much harder to check. Building the steady-state field first means each piece (fluid, well, facility) is tested against a book example before time is added on top. Then, if something looks wrong in Module 4, you know the physics underneath was already right.

## D-003 
-The field values are fictional teaching values, not real data
-datum depth 9,000 ft; 4,000 ÷ 9,000 = 0.44 psi/ft, normal pressure
-temperature check: ~80 °F + 1.3 °F/100 ft × 9,000 ft ≈ 197 °F, so 200 °F fits
-the PI already includes skin (measured from a well test)
-W-6's high GOR assumes a small local gas cap. Not consistent with a fully undersaturated reservoir;    revisit in Module 1
-skin is limited to −7 or more: negative skin is allowed because a stimulated well flows better than an undamaged one, but values below about −7 aren't realistic

## D-004: 
Field extended to 7 wells. W-7 is a sand-prone well. Because of this, the plan's "six wells" checks become "seven wells".