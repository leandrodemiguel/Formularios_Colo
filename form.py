import streamlit as st
import time
from datetime import date
from db import (
    insertar_curso,
    insertar_nomina,
    insertar_equivalencias
)
from pdfid import (
    generar_codigo_curso
)

def formulario(tipoDeFormulario):
    """Esta función carga el formulario de ingreso de datos"""

    # Inicializar contador de formularios
    if "form_key_datainput" not in st.session_state:
        st.session_state.form_key_datainput = 0

    if "form_key_editar" not in st.session_state:
        st.session_state.form_key_editar = 0

    # Arranca el formulario
    if (tipoDeFormulario == "firmas"):
        # Formulario de ingreso de datos para firmas:
        with st.form(f"form_alta_de_cursos_{st.session_state.form_key_datainput}"):
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
            codigo_pdf = generar_codigo_curso()
            submitted = st.form_submit_button("Guardar")

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
                    st.session_state.form_key_datainput += 1 # Incrementar el key para forzar reinicio del formulario
                    st.rerun()
                else:
                    st.warning("Por favor, completá el nombre del curso.")


    elif (tipoDeFormulario == "nominas"):
        # Formulario de ingreso de datos para nóminas:
        with st.form(f"form_alta_de_nominas_{st.session_state.form_key_datainput}"):
            nombre_del_curso = st.text_input("Nombre del Curso")
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
            creditos = st.number_input("Cantidad de créditos otorgados")
            lugar = st.text_input("Lugar de realización del curso")
            comentarios = st.text_input("Información adicional / Comentarios")
            codigo_pdf = generar_codigo_curso()
            submitted = st.form_submit_button("Guardar")

            if submitted:
                if nombre_del_curso:
                    insertar_nomina(nombre_del_curso,
                                codigo_pdf,
                                fecha_inicio,
                                fecha_fin,
                                creditos,
                                lugar,
                                comentarios)
                    st.success(f'Nomina "{nombre_del_curso}" guardada correctamente.')
                    # st.success(f'Curso cargado correctamente. Código para el PDF: **{codigo_pdf}**')
                    # time.sleep(5)
                    time.sleep(0.5)
                    st.session_state.form_key_datainput += 1 # Incrementar el key para forzar reinicio del formulario
                    st.rerun()
                else:
                    st.warning("Por favor, completá el nombre del curso.")


    elif (tipoDeFormulario == "equivalencias"):
        # Formulario de ingreso de datos para equivalencias:
        with st.form(f"form_alta_de_equivalencias_{st.session_state.form_key_datainput}"):

            # nombre_del_curso, codigo_pdf, creditos, codigoinap, comentarios

            nombre_del_curso = st.text_input("Nombre del Curso")
            creditos = st.number_input("Cantidad de créditos otorgados")
            codigoinap = st.text_input("Código de INAP")
            comentarios = st.text_input("Información adicional / Comentarios")
            codigo_pdf = generar_codigo_curso()
            submitted = st.form_submit_button("Guardar")

            if submitted:
                if nombre_del_curso:
                    insertar_equivalencias(nombre_del_curso,
                                codigo_pdf,
                                creditos,
                                codigoinap,
                                comentarios)
                    st.success(f'Equivalencia "{nombre_del_curso}" guardada correctamente.')
                    # st.success(f'Curso cargado correctamente. Código para el PDF: **{codigo_pdf}**')
                    # time.sleep(5)
                    time.sleep(0.5)
                    st.session_state.form_key_datainput += 1 # Incrementar el key para forzar reinicio del formulario
                    st.rerun()
                else:
                    st.warning("Por favor, completá el nombre del curso.")