# import sqlite3
from datetime import datetime, timedelta
import random
from pdfid import generar_codigo_curso
import psycopg2
import streamlit as st

# DB_NAME = "data/planillasfirmas.db"

def get_connection():
    return psycopg2.connect(
        host= st.secrets["db_host"],
        port= st.secrets["db_port"],
        user= st.secrets["db_user"],
        password= st.secrets["db_password"],
        dbname= st.secrets["db_name"]
    )

def insertar_curso(nombre_del_curso, codigo_pdf, nombre_del_docente, apellido_del_docente, fecha_inicio, fecha_fin, horario, lugar, comentarios):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO planillasfirmas (nombre_del_curso, codigo_pdf, nombre_del_docente, apellido_del_docente, fecha_inicio, fecha_fin, horario, lugar, comentarios)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (nombre_del_curso, codigo_pdf, nombre_del_docente, apellido_del_docente, fecha_inicio, fecha_fin, horario, lugar, comentarios))
    conn.commit()
    conn.close()


def eliminar_curso(id_curso):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM planillasfirmas WHERE id = %s", (id_curso,))
    conn.commit()
    conn.close()


def actualizar_curso(id_curso, nombre_del_curso, nombre_del_docente, apellido_del_docente, fecha_inicio, fecha_fin, horario, lugar, comentarios):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE planillasfirmas
        SET nombre_del_curso = %s, 
            nombre_del_docente = %s, 
            apellido_del_docente = %s, 
            fecha_inicio = %s, 
            fecha_fin = %s, 
            horario = %s, 
            lugar = %s, 
            comentarios = %s
        WHERE id = %s
    """, (nombre_del_curso, nombre_del_docente, apellido_del_docente, fecha_inicio, fecha_fin, horario, lugar, comentarios, id_curso))
    conn.commit()
    conn.close()


def obtener_cursos():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nombre_del_curso, codigo_pdf, nombre_del_docente, apellido_del_docente, fecha_inicio, fecha_fin, horario, lugar, comentarios FROM planillasfirmas ORDER BY id DESC")
    datos = cursor.fetchall()
    conn.close()
    return datos

# ------------------------------------------------- /-\*/-\ ------------------------------------------------- #

def insertar_datos_prueba():
    conn = get_connection()
    cursor = conn.cursor()

    cursos = [
        "Python Inicial", "Python Avanzado", "Excel Básico", "Excel Intermedio",
        "Diseño Gráfico", "Marketing Digital", "Redacción Profesional",
        "Introducción a la Programación", "Bases de Datos", "Desarrollo Web",
        "Gestión de Proyectos", "Fotografía", "Edición de Video",
        "Seguridad Informática", "Soporte Técnico", "Administración",
        "Contabilidad", "Trabajo en Equipo", "Comunicación Efectiva",
        "Creatividad e Innovación"
    ]

    docentes = [
        ("Lucía", "Gómez"), ("Juan", "Pérez"), ("Ana", "Martínez"),
        ("Pedro", "López"), ("Carla", "Sánchez"), ("Mario", "Fernández"),
        ("Elena", "Ramírez"), ("Sofía", "Torres"), ("Diego", "García"),
        ("Laura", "Hernández")
    ]

    lugares = [
        "Aula 1", "Aula 2", "Aula 3", "Sala de Informática",
        "Laboratorio", "Aula Virtual", "Auditorio"
    ]

    for i in range(50):
        # curso = cursos[i]
        curso = random.choice(cursos)
        codigo_pdf = generar_codigo_curso()
        nombre_docente, apellido_docente = random.choice(docentes)

        fecha_inicio = datetime(1994, 1, 1) + timedelta(days=random.randint(0, 11315))
        fecha_fin = fecha_inicio + timedelta(days=random.randint(5, 30))

        horario = random.choice(["08:00-10:00", "10:00-12:00", "14:00-16:00", "18:00-20:00"])
        lugar = random.choice(lugares)
        comentarios = random.choice(["", "Curso intensivo", "Requiere PC", "Material incluido"])

        cursor.execute("""
            INSERT INTO keepalive (
                nombre_del_curso, codigo_pdf, nombre_del_docente, apellido_del_docente,
                fecha_inicio, fecha_fin, horario, lugar, comentarios
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            curso, codigo_pdf, nombre_docente, apellido_docente,
            fecha_inicio.date(), fecha_fin.date(), horario, lugar, comentarios
        ))

    conn.commit()
    conn.close()
    print("Datos de prueba insertados correctamente.")

def obtener_datos_keepalive():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nombre_del_curso, codigo_pdf, nombre_del_docente, apellido_del_docente, fecha_inicio, fecha_fin, horario, lugar, comentarios FROM planillasfirmas ORDER BY id DESC")
    datos = cursor.fetchall()
    conn.close()
    return datos