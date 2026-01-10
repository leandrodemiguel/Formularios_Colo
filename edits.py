import streamlit as st
import pandas as pd
import time
from datetime import date
from db import (
    eliminar_curso,
    actualizar_curso
)

def dataeditor(df):
    # 🔧 Selección para editar o eliminar
    st.subheader("✏️ Editar o eliminar registro")

    # Bloque para inicializar contador de input (en el que se coloca el ID del registro a anotar)
    if "limpiar_id" not in st.session_state:
        st.session_state.limpiar_id = False

    if st.session_state.limpiar_id:
        st.session_state.id_edicion = ""
        st.session_state.limpiar_id = False

    # Acá viene el input:
    id_input = st.text_input("Ingresá el ID del curso a editar o eliminar", key="id_edicion")

    # Acá arranca la lógica de la interfaz para editar y para borrar:
    if id_input:
        # Validar que el ID sea numérico
        if id_input.isdigit():
            id_ingresado = int(id_input)
            curso_filtrado = df[df["ID"] == id_ingresado]

            if not curso_filtrado.empty:
                curso = curso_filtrado.iloc[0]

                with st.form(f"form_editar_cursos_{st.session_state.form_key_editar}"):
                    nuevo_nombre_del_curso = st.text_input("Nombre del Curso", curso["Nombre del Curso"])
                    nuevo_nombre_del_docente = st.text_input("Nombre del docente", curso["Nombre del docente"])
                    nuevo_apellido_del_docente = st.text_input("Apellido del docente", curso["Apellido del docente"])
                    nueva_fecha_inicio = st.date_input(
                        "Inicio del curso",
                        value = pd.to_datetime(curso["Inicio del curso"]),
                        min_value=date(1980, 1, 1),
                        max_value=date.today().replace(year=date.today().year + 5)
                        )
                    nueva_fecha_fin = st.date_input(
                        "Fin del curso",
                        value = pd.to_datetime(curso["Fin del curso"]),
                        min_value=date(1980, 1, 1),
                        max_value=date.today().replace(year=date.today().year + 5)
                        )
                    nuevo_horario = st.text_input("Horario del curso", curso["Horario del curso"])
                    nuevo_lugar = st.text_input("Lugar de realización del curso", curso["Lugar de realización del curso"])
                    nuevos_comentarios = st.text_input("Información adicional / Comentarios", curso["Información adicional / Comentarios"])

                    col1, col2 = st.columns(2)
                    with col1:
                        guardar = st.form_submit_button("💾 Guardar cambios")
                    with col2:
                        borrar = st.form_submit_button("🗑️ Eliminar registro")

                    if guardar:
                        actualizar_curso(id_ingresado,
                                        nuevo_nombre_del_curso,
                                        nuevo_nombre_del_docente,
                                        nuevo_apellido_del_docente,
                                        nueva_fecha_inicio,
                                        nueva_fecha_fin,
                                        nuevo_horario,
                                        nuevo_lugar,
                                        nuevos_comentarios)
                        st.success(f'Curso "{nuevo_nombre_del_curso}" actualizado correctamente.')
                        time.sleep(0.5)
                        st.session_state.form_key_editar += 1 # Incrementar el key para forzar reinicio del formulario
                        st.session_state.limpiar_id = True  # marcar para limpiar en el próximo ciclo
                        st.rerun()

                    if borrar:
                        eliminar_curso(id_ingresado)
                        st.warning(f"Curso con ID {id_ingresado} eliminado.")
                        time.sleep(0.5)
                        st.session_state.form_key_editar += 1 # Incrementar el key para forzar reinicio del formulario
                        st.session_state.limpiar_id = True  # marcar para limpiar en el próximo ciclo
                        st.rerun()
            else:
                st.warning(f"No existe un curso con ID {id_ingresado}.")
        else:
            st.warning("Por favor, ingresá un número válido de ID.")
    # else:
    #     st.info("Ingresá un ID para editar o eliminar un registro.")