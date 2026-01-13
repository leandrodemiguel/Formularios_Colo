import streamlit as st
from login import (
    logout
)
from db import (
    # crear_tabla,
    obtener_cursos,
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
    st.title("📋 Carga de planillas de firmas")

    # Cargamos el formulario de ingreso de datos
    formulario()

    # Divisor
    st.divider()

    # Mostrar los datos cargados
    st.subheader("📄 Registros existentes")

    cursos = obtener_cursos()
    # cursos = ""

    if cursos:

        df = dataview(cursos)

        # Divisor
        st.divider()

        # Bloque de edición de registros
        with st.expander("Editar registros"):
            dataeditor(df)

    else:
        st.info("No hay registros cargados todavía.")

else:
    st.write("No tenés acceso a esta página")