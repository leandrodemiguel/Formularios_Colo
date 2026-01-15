import streamlit as st

# Para hacer el wide. Funciona bien:
# st.set_page_config(layout="wide")

pg = st.navigation([
    st.Page("login.py", title="🔐 Login"),
    st.Page("pages/planillasfirmas.py", title="📋 Carga de planillas de firmas"),
    st.Page("pages/nominas.py", title="📋 Carga de nóminas"),
    st.Page("pages/equivalencias.py", title="📋 Carga de equivalencias"),
    st.Page("pages/tester.py", title="🖥️ Consola de testeo")
])

pg.run()
