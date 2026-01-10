-- IMPORTANTE! Si vas a pasar a supabase acordate de tener instalado psycopg2-binary:
-- pip install psycopg2-binary

--
-- TABLAS
--

-- Para crear la tabla (si es que no existe)

create table cursos (
    id serial primary key,
    nombre_del_curso text not null,
    nombre_del_docente text not null,
    apellido_del_docente text not null,
    fecha_inicio date,
    fecha_fin date,
    horario text,
    lugar text,
    comentarios text,
    codigo_pdf text unique
);
