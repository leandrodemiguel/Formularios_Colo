import streamlit as st

st.set_page_config(layout="wide")

pg = st.navigation([
    st.Page("login.py", title="🔐 Login"),
    st.Page("pages/planillasfirmas.py", title="📋 Carga de planillas de firmas"),
    st.Page("pages/tester.py", title="🖥️ Consola de testeo"),
])

pg.run()
