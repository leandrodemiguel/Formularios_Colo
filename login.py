from loginlogic import (
    login,
)

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