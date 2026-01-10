import streamlit as st
import time
from datetime import date
from db import (
    insertar_curso
)
from pdfid import (
    generar_codigo_curso
)

def formulario():
    """Esta función carga el formulario de ingreso de datos"""

    # Inicializar contador de formularios
    if "form_key_cursos" not in st.session_state:
        st.session_state.form_key_cursos = 0

    if "form_key_editar" not in st.session_state:
        st.session_state.form_key_editar = 0

    # Formulario de ingreso de datos
    with st.form(f"form_alta_de_cursos_{st.session_state.form_key_cursos}"):
        nombre_del_curso = st.text_input("Nombre del Curso")
        nombre_del_docente = st.text_input("Nombre del docente")
        apellido_del_docente = st.text_input("Apellido del docente")
        fecha_inicio = st.date_input(
            "Inicio del curso",
            min_value=date(1980, 1, 1),
            max_value=date.today().replace(year=date.today().year + 5)
            )
        fecha_fin = st.date_input(
            "Fin del curso",
            min_value=date(1980, 1, 1),
            max_value=date.today().replace(year=date.today().year + 5)
            )
        horario = st.text_input("Horario del curso")
        lugar = st.text_input("Lugar de realización del curso")
        comentarios = st.text_input("Información adicional / Comentarios")
        submitted = st.form_submit_button("Guardar")

        codigo_pdf = generar_codigo_curso()

        if submitted:
            if nombre_del_curso:
                insertar_curso(nombre_del_curso,
                               codigo_pdf,
                               nombre_del_docente,
                               apellido_del_docente,
                               fecha_inicio, fecha_fin,
                               horario,
                               lugar,
                               comentarios)
                st.success(f'Curso "{nombre_del_curso}" guardado correctamente.')
                # st.success(f'Curso cargado correctamente. Código para el PDF: **{codigo_pdf}**')
                # time.sleep(5)
                time.sleep(0.5)
                st.session_state.form_key_cursos += 1 # Incrementar el key para forzar reinicio del formulario
                st.rerun()
            else:
                st.warning("Por favor, completá el nombre del curso.")