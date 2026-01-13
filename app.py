import streamlit as st
from login import (
    login,
)

st.set_page_config(layout="wide")

pg = st.navigation([
    st.Page("pages/app.py", title="Login"),
    st.Page("pages/planillasfirmas.py", title="📋 Carga de planillas de firmas"),
    st.Page("pages/tester.py", title="Consola de testeo"),
])

pg.run()


# Login
if "autenticado" not in st.session_state:
    st.session_state["autenticado"] = False

if not st.session_state["autenticado"]:
    # usuario = login() # Esto lo usaría si pudiera usar el return.
                        # No lo puedo usar porque los re-runs borran los return (no tienen persistencia).
    login()
    st.stop()

if st.session_state["autenticado"]:
    st.switch_page("pages/planillasfirmas.py")
