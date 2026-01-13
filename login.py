import streamlit as st

def login():
    st.title("🔐 Acceso al aplicativo")

    usuario = st.text_input("Usuario")
    contraseña = st.text_input("Contraseña", type="password")

    if st.button("Ingresar"):
        if (
            usuario == st.secrets["auth_user1"]
            and contraseña == st.secrets["auth_password1"]
        ):
            st.session_state["autenticado"] = True
            st.rerun()
        elif (
            usuario == st.secrets["auth_user2"]
            and contraseña == st.secrets["auth_password2"]
        ):
            st.session_state["autenticado"] = True
            st.rerun()
        elif (
            usuario == st.secrets["auth_user3"]
            and contraseña == st.secrets["auth_password3"]
        ):
            st.session_state["autenticado"] = True
            st.rerun()
        else:
            st.error("Usuario o contraseña incorrectos")

def logout():
    if st.button("Cerrar sesión"):
        st.session_state["autenticado"] = False
        st.rerun()