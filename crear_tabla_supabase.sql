-- IMPORTANTE! Si vas a pasar a supabase acordate de tener instalado psycopg2-binary:
-- pip install psycopg2-binary

------------------------------------------------- /-\*/-\ -------------------------------------------------

-- Para crear la tabla "planillasfirmas"

create table planillasfirmas (
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

------------------------------------------------- /-\*/-\ -------------------------------------------------

-- Para crear la tabla "planillasnominas"

create table planillasnominas (
    id serial primary key,
    nombre_del_curso text not null,
    fecha_inicio date,
    fecha_fin date,
    creditos int,
    lugar text,
    comentarios text,
    codigo_pdf text unique
);

------------------------------------------------- /-\*/-\ -------------------------------------------------

-- Para crear la tabla "planillasequivalencias"

create table planillasequivalencias (
    id serial primary key,
    nombre_del_curso text not null,
    creditos int,
    codigoinap text,
    comentarios text,
    codigo_pdf text unique
);

------------------------------------------------- /-\*/-\ -------------------------------------------------

-- Para crear la tabla "keepalive"

create table keepalive (
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