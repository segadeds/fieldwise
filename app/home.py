"""FIELDWISE app: home page. Run with:  uv run streamlit run app/Home.py"""

import streamlit as st

st.set_page_config(page_title="FIELDWISE", page_icon="🛢️", layout="wide")

st.title("FIELDWISE")
st.subheader("A digital twin of a fictional oil field")

st.warning(
    "**Disclaimer:** FIELDWISE is an educational model of a **fictional** field. "
    "All data is synthetic or from the public Equinor Volve dataset. It is a "
    "learning tool and must not be used for design, operational or investment "
    "decisions."
)

st.markdown(
    """
This twin is built over 26 weeks as a production-engineering learning project.
Each module adds one part of the physics and one page to this app.

| Module | Page | Status |
|---|---|---|
| M0 Foundations | Field overview | ✅ |
| M1 Fluids / PVT | Fluid lab | coming |
| M2 Wells and nodal analysis | Well performance | coming |
| M3 Chokes, gathering, facility | Facility | coming |
| M4 Time and surveillance | Surveillance | coming |
| M5 Artificial lift | Artificial lift | coming |
| M6 Control room | Control room | coming |

Use the menu on the left to open a page.
"""
)