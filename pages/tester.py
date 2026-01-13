import streamlit as st
from login import (
    logout
)
from db import (
    # crear_tabla,
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

    tester = obtener_datos_keepalive()
    # tester = ""

    basedeprueba = st.button("Generar base de datos de prueba")

    if basedeprueba:
        insertar_datos_prueba()
        st.success('datos escritos correctamente.')

    st.write("Exploramos los datos de testeo:")
    dftest = dataview(tester)

else:
    st.write("No tenés acceso a esta página")