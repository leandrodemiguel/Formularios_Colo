import streamlit as st
from login import (
    login,
    logout
)
from db import (
    # crear_tabla,
    obtener_cursos,
    insertar_datos_prueba
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

# Login
if "autenticado" not in st.session_state:
    st.session_state["autenticado"] = False

if not st.session_state["autenticado"]:
    login()
    st.stop()

# Botón de cerrar sesión
# Nota: en donde pongamos esta función va a aparecer el botón.
logout()

# Crear la tabla si no existe
# crear_tabla()

# Título de la sección del formulario
st.title("📋 Carga de planillas de firmas")

# Cargamos el formulario de ingreso de datos
formulario()

# Divisor
st.divider()

# Mostrar los datos cargados
st.subheader("📄 Registros existentes")

cursos = obtener_cursos()

if cursos:

    df = dataview(cursos)

    # Divisor
    st.divider()

    # Bloque de edición de registros
    with st.expander("Editar registros"):
        dataeditor(df)

else:
    st.info("No hay registros cargados todavía.")

# Divisor
st.divider()

with st.expander("Testing"):

    basedeprueba = st.button("Generar base de datos de prueba")

    if basedeprueba:
        insertar_datos_prueba()