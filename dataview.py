import streamlit as st
import pandas as pd
import math

def dataview(data, tipoDeFormulario):

    if (tipoDeFormulario == "firmas"):
        # Para el formulario de firmas
        df = pd.DataFrame(data, columns=["ID",
                                            "Nombre del Curso",
                                            "Nombre del PDF",
                                            "Nombre del docente",
                                            "Apellido del docente",
                                            "Inicio del curso",
                                            "Fin del curso",
                                            "Horario del curso",
                                            "Lugar de realización del curso",
                                            "Información adicional / Comentarios"])
        # st.dataframe(df, use_container_width=True)

        # Convertimos fechas para poder filtrar por año fácilmente
        df["Inicio del curso"] = pd.to_datetime(df["Inicio del curso"], errors="coerce")
        df["Fin del curso"] = pd.to_datetime(df["Fin del curso"], errors="coerce")

        # --- FILTROS ---
        # Bloque para inicializar contador de input (en el que se coloca el ID del registro a anotar)
        if "limpiar_id_filtros" not in st.session_state:
            st.session_state.limpiar_id_filtros = False

        if st.session_state.limpiar_id_filtros:
            st.session_state.id_filtros_texto = ""
            st.session_state.id_filtros_anio = None
            st.session_state.limpiar_id_filtros = False

        # Inicializar valores anteriores
        if "busqueda_prev" not in st.session_state:
            st.session_state.busqueda_prev = ""
        if "anio_prev" not in st.session_state:
            st.session_state.anio_prev = None

        # with st.expander("🔍 Filtros de búsqueda", expanded=True):
        with st.expander("🔍 Filtros de búsqueda"):
            col1, col2, col3 = st.columns([2, 2, 1])

            with col1:
                busqueda = st.text_input(
                    "Buscar por nombre del curso o docente:",
                    placeholder="Ej: Python, Laura, Gómez...",
                    key="id_filtros_texto"
                ).strip().lower()

            with col2:
                anio = st.number_input(
                    "Filtrar por año:",
                    min_value=1990,
                    max_value=2100,
                    step=1,
                    value=None,
                    placeholder="Ej: 2024",
                    key="id_filtros_anio"
                )

            with col3:
                limpiar = st.button("Limpiar filtros")

        # Si cambia algún filtro, volver a la página 1
        if (
            busqueda != st.session_state.busqueda_prev or
            anio != st.session_state.anio_prev
        ):
            st.session_state.pagina = 1

        # Guardar valores actuales
        st.session_state.busqueda_prev = busqueda
        st.session_state.anio_prev = anio

        # Aplicamos filtros
        if limpiar:
            st.session_state.limpiar_id_filtros = True  # marcar para limpiar en el próximo ciclo
            st.rerun()

        if busqueda:
            df = df[
                df["Nombre del Curso"].str.contains(busqueda, case=False, na=False) |
                df["Nombre del docente"].str.contains(busqueda, case=False, na=False) |
                df["Apellido del docente"].str.contains(busqueda, case=False, na=False)
            ]

        if anio:
            df = df[
                (df["Inicio del curso"].dt.year == anio) |
                (df["Fin del curso"].dt.year == anio)
            ]

        # Configuración de la paginación por botones
        if "pagina" not in st.session_state:
            st.session_state.pagina = 1  # Página actual

        registros_por_pagina = 10
        total_paginas = max(1, math.ceil(len(df) / registros_por_pagina))

        # Calcular el rango de filas a mostrar
        inicio = (st.session_state.pagina - 1) * registros_por_pagina
        fin = inicio + registros_por_pagina

        # Antes de mostrar el dataframe, reconvertimos las fechas para que no muestre la hora
        df["Inicio del curso"] = pd.to_datetime(df["Inicio del curso"]).dt.date
        df["Fin del curso"] = pd.to_datetime(df["Fin del curso"]).dt.date

        # Mostrar la porción del dataframe que corresponde a una página
        st.dataframe(df.iloc[inicio:fin], use_container_width=True)

        if busqueda or anio:
            st.caption(f"Mostrando {len(df.iloc[inicio:fin])} de {len(df)} registros encontrados.")

        # Controles de paginación
        col1, col2, col3 = st.columns([1, 2, 1])
        with col1:
            if st.button("⬅️ Anterior") and st.session_state.pagina > 1:
                st.session_state.pagina -= 1
                st.rerun()
        with col3:
            if st.button("Siguiente ➡️") and st.session_state.pagina < total_paginas:
                st.session_state.pagina += 1
                st.rerun()
        with col2:
            st.html(f"<p style='text-align:center;'>Página {st.session_state.pagina} de {total_paginas}</p>")

        # Configuración de la paginación por input
        st.session_state.pagina = max(
            1,
            min(st.session_state.get("pagina", 1), total_paginas)
        )

        pagina = st.number_input(
            "Ir a página:",
            1,
            total_paginas,
            st.session_state.pagina,
            step=1
        )

        if pagina != st.session_state.pagina:
            st.session_state.pagina = pagina
            st.rerun()

        return df

    
    elif (tipoDeFormulario == "nominas"):
        # Para el formulario de nóminas
        df = pd.DataFrame(data, columns=["ID",
                                            "Nombre del Curso",
                                            "Nombre del PDF",
                                            "Inicio del curso",
                                            "Fin del curso",
                                            "Créditos del curso",
                                            "Lugar de realización del curso",
                                            "Información adicional / Comentarios"])
        # st.dataframe(df, use_container_width=True)

        # Convertimos fechas para poder filtrar por año fácilmente
        df["Inicio del curso"] = pd.to_datetime(df["Inicio del curso"], errors="coerce")
        df["Fin del curso"] = pd.to_datetime(df["Fin del curso"], errors="coerce")

        # --- FILTROS ---
        # Bloque para inicializar contador de input (en el que se coloca el ID del registro a anotar)
        if "limpiar_id_filtros" not in st.session_state:
            st.session_state.limpiar_id_filtros = False

        if st.session_state.limpiar_id_filtros:
            st.session_state.id_filtros_texto = ""
            st.session_state.id_filtros_anio = None
            st.session_state.limpiar_id_filtros = False

        # Inicializar valores anteriores
        if "busqueda_prev" not in st.session_state:
            st.session_state.busqueda_prev = ""
        if "anio_prev" not in st.session_state:
            st.session_state.anio_prev = None

        # with st.expander("🔍 Filtros de búsqueda", expanded=True):
        with st.expander("🔍 Filtros de búsqueda"):
            col1, col2, col3 = st.columns([2, 2, 1])

            with col1:
                busqueda = st.text_input(
                    "Buscar por nombre del curso o docente:",
                    placeholder="Ej: Python, Laura, Gómez...",
                    key="id_filtros_texto"
                ).strip().lower()

            with col2:
                anio = st.number_input(
                    "Filtrar por año:",
                    min_value=1990,
                    max_value=2100,
                    step=1,
                    value=None,
                    placeholder="Ej: 2024",
                    key="id_filtros_anio"
                )

            with col3:
                limpiar = st.button("Limpiar filtros")

        # Si cambia algún filtro, volver a la página 1
        if (
            busqueda != st.session_state.busqueda_prev or
            anio != st.session_state.anio_prev
        ):
            st.session_state.pagina = 1

        # Guardar valores actuales
        st.session_state.busqueda_prev = busqueda
        st.session_state.anio_prev = anio

        # Aplicamos filtros
        if limpiar:
            st.session_state.limpiar_id_filtros = True  # marcar para limpiar en el próximo ciclo
            st.rerun()

        if busqueda:
            df = df[
                df["Nombre del Curso"].str.contains(busqueda, case=False, na=False) |
                df["Nombre del docente"].str.contains(busqueda, case=False, na=False) |
                df["Apellido del docente"].str.contains(busqueda, case=False, na=False)
            ]

        if anio:
            df = df[
                (df["Inicio del curso"].dt.year == anio) |
                (df["Fin del curso"].dt.year == anio)
            ]

        # Configuración de la paginación por botones
        if "pagina" not in st.session_state:
            st.session_state.pagina = 1  # Página actual

        registros_por_pagina = 10
        total_paginas = max(1, math.ceil(len(df) / registros_por_pagina))

        # Calcular el rango de filas a mostrar
        inicio = (st.session_state.pagina - 1) * registros_por_pagina
        fin = inicio + registros_por_pagina

        # Antes de mostrar el dataframe, reconvertimos las fechas para que no muestre la hora
        df["Inicio del curso"] = pd.to_datetime(df["Inicio del curso"]).dt.date
        df["Fin del curso"] = pd.to_datetime(df["Fin del curso"]).dt.date

        # Mostrar la porción del dataframe
        st.dataframe(df.iloc[inicio:fin], use_container_width=True)

        if busqueda or anio:
            st.caption(f"Mostrando {len(df.iloc[inicio:fin])} de {len(df)} registros encontrados.")

        # Controles de paginación
        col1, col2, col3 = st.columns([1, 2, 1])
        with col1:
            if st.button("⬅️ Anterior") and st.session_state.pagina > 1:
                st.session_state.pagina -= 1
                st.rerun()
        with col3:
            if st.button("Siguiente ➡️") and st.session_state.pagina < total_paginas:
                st.session_state.pagina += 1
                st.rerun()
        with col2:
            st.html(f"<p style='text-align:center;'>Página {st.session_state.pagina} de {total_paginas}</p>")

        # Configuración de la paginación por input
        st.session_state.pagina = max(
            1,
            min(st.session_state.get("pagina", 1), total_paginas)
        )

        pagina = st.number_input(
            "Ir a página:",
            1,
            total_paginas,
            st.session_state.pagina,
            step=1
        )

        if pagina != st.session_state.pagina:
            st.session_state.pagina = pagina
            st.rerun()
            
        return df



    elif (tipoDeFormulario == "equivalencias"):
        # Para el formulario de equivalencias
        df = pd.DataFrame(data, columns=["ID",
                                            "Nombre del Curso",
                                            "Nombre del PDF",
                                            "Créditos del curso",
                                            "Código de INAP",
                                            "Información adicional / Comentarios"])
        # st.dataframe(df, use_container_width=True)

        # --- FILTROS ---
        # Bloque para inicializar contador de input (en el que se coloca el ID del registro a anotar)
        if "limpiar_id_filtros" not in st.session_state:
            st.session_state.limpiar_id_filtros = False

        if st.session_state.limpiar_id_filtros:
            st.session_state.id_filtros_texto = ""
            st.session_state.limpiar_id_filtros = False

        # Inicializar valores anteriores
        if "busqueda_prev" not in st.session_state:
            st.session_state.busqueda_prev = ""

        # with st.expander("🔍 Filtros de búsqueda", expanded=True):
        with st.expander("🔍 Filtros de búsqueda"):
            col1, col2, = st.columns([2, 1])

            with col1:
                busqueda = st.text_input(
                    "Buscar por nombre del curso:",
                    placeholder="Ej: Python, R, Stata...",
                    key="id_filtros_texto"
                ).strip().lower()

            with col2:
                limpiar = st.button("Limpiar filtros")

    # Si cambia algún filtro, volver a la página 1
        if (
            busqueda != st.session_state.busqueda_prev
        ):
            st.session_state.pagina = 1

        # Guardar valores actuales
        st.session_state.busqueda_prev = busqueda

        # Aplicamos filtros
        if limpiar:
            st.session_state.limpiar_id_filtros = True  # marcar para limpiar en el próximo ciclo
            st.rerun()

        if busqueda:
            df = df[
                df["Nombre del Curso"].str.contains(busqueda, case=False, na=False)
            ]

        # Configuración de la paginación por botones
        if "pagina" not in st.session_state:
            st.session_state.pagina = 1  # Página actual

        registros_por_pagina = 10
        total_paginas = max(1, math.ceil(len(df) / registros_por_pagina))

        # Calcular el rango de filas a mostrar
        inicio = (st.session_state.pagina - 1) * registros_por_pagina
        fin = inicio + registros_por_pagina

        # Acá no cambiamos el tema del formato de fecha porque NO hay campos de fecha en este formulario

        # Mostrar la porción del dataframe
        st.dataframe(df.iloc[inicio:fin], use_container_width=True)

        if busqueda:
            st.caption(f"Mostrando {len(df.iloc[inicio:fin])} de {len(df)} registros encontrados.")

        # Controles de paginación
        col1, col2, col3 = st.columns([1, 2, 1])
        with col1:
            if st.button("⬅️ Anterior") and st.session_state.pagina > 1:
                st.session_state.pagina -= 1
                st.rerun()
        with col3:
            if st.button("Siguiente ➡️") and st.session_state.pagina < total_paginas:
                st.session_state.pagina += 1
                st.rerun()
        with col2:
            st.html(f"<p style='text-align:center;'>Página {st.session_state.pagina} de {total_paginas}</p>")

        # Configuración de la paginación por input
        st.session_state.pagina = max(
            1,
            min(st.session_state.get("pagina", 1), total_paginas)
        )

        pagina = st.number_input(
            "Ir a página:",
            1,
            total_paginas,
            st.session_state.pagina,
            step=1
        )

        if pagina != st.session_state.pagina:
            st.session_state.pagina = pagina
            st.rerun()
            
        return df