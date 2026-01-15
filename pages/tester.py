import streamlit as st
from loginlogic import (
    logout
)
from db import (
    insertar_datos_prueba,
    obtener_datos_keepalive
)
from dataview import (
    dataview
)

# La variable usuario va a dictaminar quién ve cada sección.
usuario = st.session_state["usuario"]

# Esto solo lo ve el usuario 1 (Leandro)
if (usuario == st.secrets["auth_user1"]):

    # Datos básicos del login
    st.write("Usuario: " + usuario) # Lo escribimos para los tests. Luego borrar esta línea.

    # Botón de cerrar sesión
    # Nota: en donde pongamos esta función va a aparecer el botón.
    logout()

    # Arranca la app:

    data = obtener_datos_keepalive()
    # tester = ""

    basedeprueba = st.button("Generar datos de testeo")

    if basedeprueba:
        insertar_datos_prueba()
        st.success('datos escritos correctamente.')

    st.write("Exploramos los datos de testeo:")
    dftest = dataview(data, "firmas") # Usamos el mismo dataview que las planillas de firmas.

else:
    st.write("No tenés acceso a esta página")