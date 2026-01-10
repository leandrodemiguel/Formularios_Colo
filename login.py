import streamlit as st

def login():
    st.title("🔐 Acceso al aplicativo")

    usuario = st.text_input("Usuario")
    contraseña = st.text_input("Contraseña", type="password")

    if st.button("Ingresar"):
        if (
            usuario == st.secrets["auth_user"]
            and contraseña == st.secrets["auth_password"]
        ):
            st.session_state["autenticado"] = True
            st.rerun()
        else:
            st.error("Usuario o contraseña incorrectos")

def logout():
    if st.button("Cerrar sesión"):
        st.session_state["autenticado"] = False
        st.rerun()