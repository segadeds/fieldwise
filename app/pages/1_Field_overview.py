"""Field overview: the field schematic and every well's inputs, read from field.yaml."""

from pathlib import Path

import pandas as pd
import streamlit as st

from fieldwise.config import load_field
from fieldwise.units import psig_to_psia

FIELD_YAML = Path(__file__).resolve().parents[2] / "field.yaml"

st.set_page_config(page_title="Field overview", page_icon="🛢️", layout="wide")
st.title("Field overview")
st.caption("Fictional teaching field. Not for design.")

field = load_field(FIELD_YAML)  # a typo in field.yaml stops the page with a clear error
res = field.reservoir
fac = field.facility

# --- Headline numbers ------------------------------------------------------
col1, col2, col3, col4 = st.columns(4)
col1.metric("Wells", len(field.wells))
col2.metric("Reservoir pressure", f"{res.p_res_psia:,.0f} psia")
col3.metric("Reservoir temperature", f"{res.t_res_degf:.0f} °F")
col4.metric(
    "Separator pressure",
    f"{fac.p_sep_psig:.0f} psig",
    help=f"= {psig_to_psia(fac.p_sep_psig):.1f} psia (assumes 14.696 psia atmosphere)",
)

# --- Schematic -------------------------------------------------------------
st.subheader("Schematic")
well_nodes = "\n".join(
    f'  "{w.name}" [shape=box, style=rounded];\n  reservoir -> "{w.name}";\n'
    f'  "{w.name}" -> manifold;'
    for w in field.wells
)
dot = f"""
digraph field {{
  rankdir=LR;
  node [fontname="Helvetica", fontsize=11];
  reservoir [label="Reservoir\\n{res.p_res_psia:,.0f} psia, {res.t_res_degf:.0f} °F\\n{res.api_deg:.0f} °API", shape=cylinder];
{well_nodes}
  manifold [label="Production\\nmanifold", shape=box];
  separator [label="HP separator\\n{fac.p_sep_psig:.0f} psig", shape=box3d];
  oil [label="Oil export\\npump → LACT → {fac.export_line_length_ft / 3280.84:.0f} km line", shape=note];
  gas [label="Gas sales", shape=note];
  water [label="Water disposal", shape=note];
  manifold -> separator;
  separator -> oil;
  separator -> gas;
  separator -> water;
}}
"""
st.graphviz_chart(dot)

# --- Well table ------------------------------------------------------------
st.subheader("Well inputs")
table = pd.DataFrame(
    [
        {
            "Well": w.name,
            "TVD (ft)": w.tvd_ft,
            "PI (STB/d/psi)": w.pi_stbd_per_psi,
            "Skin": w.skin,
            "Tubing ID (in)": w.tubing_id_in,
            "Water cut (%)": w.wc_frac * 100,
            "GOR (scf/STB)": w.gor_scf_per_stb,
        }
        for w in field.wells
    ]
)
st.dataframe(table, hide_index=True, width="stretch")

st.info(
    "Every value on this page comes from `field.yaml`. Change a number there, "
    "push, and this page changes."
)