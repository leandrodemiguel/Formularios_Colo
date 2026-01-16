import streamlit as st
from loginlogic import (
    logout
)
from db import (
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
    formulario("firmas")

    # Divisor
    st.divider()

    # Mostrar los datos cargados
    st.subheader("📄 Registros existentes")

    data = obtener_cursos()
    # cursos = ""

    if data:

        df = dataview(data, "firmas")

        st.write("Tipo columna:", df['fecha'].dtype)
        st.write("Primeros 3 valores:", df['fecha'].head(3).tolist())
        st.write("¿Hay NaN?", df['fecha'].isna().sum())

        # Divisor
        st.divider()

        # Bloque de edición de registros
        with st.expander("Editar registros"):
            dataeditor(df, "firmas")

    else:
        st.info("No hay registros cargados todavía.")

else:
    st.write("No tenés acceso a esta página")