import streamlit as st
from loginlogic import (
    logout
)
from db import (
    obtener_nomina,
)
from form import (
    formulario
)
from dataview import (
    dataview
)
from edits import (
    dataeditor
)

usuario = st.session_state["usuario"]

if (usuario == st.secrets["auth_user1"] or usuario == st.secrets["auth_user2"] or usuario == st.secrets["auth_user3"]):

    # Datos básicos del login
    st.write("Usuario: " + usuario) # Lo escribimos para los tests. Luego borrar esta línea.

    # Botón de cerrar sesión
    # Nota: en donde pongamos esta función va a aparecer el botón.
    logout()


    # Arranca la app:

    # Título de la sección del formulario
    st.title("📋 Carga de nóminas")

    # Cargamos el formulario de ingreso de datos
    formulario("nominas")

    # Divisor
    st.divider()

    # Mostrar los datos cargados
    st.subheader("📄 Registros existentes")

    data = obtener_nomina()
    # cursos = ""

    if data:

        df = dataview(data, "nominas")

        # Divisor
        st.divider()

        # Bloque de edición de registros
        with st.expander("Editar registros"):
            dataeditor(df)

    else:
        st.info("No hay registros cargados todavía.")

else:
    st.write("No tenés acceso a esta página")