# -*- coding: utf-8 -*-
"""
Diccionario de mapeo generado a partir de:
  - 20260331_diccionario_base_ano_movil_2025.xlsx (preguntas, opciones y reglas de validacion oficiales)
  - base_ano_movil_2025.csv (dataset crudo, para verificar existencia real de columnas)

Cambios respecto a la version anterior:
  - Se agrego Ax401 (filtro maestro de victimizacion): permite diferenciar un NaN real
    (no aplica porque nadie en el hogar fue victima de ningun delito) de un NaN por no respuesta.
  - Se agregaron A3, A4, A5 (tamano del hogar, menores de 18, mayores de 18): denominador
    natural para indices de cuidado y control de tamano del hogar.
  - Cod_Locali se renombra a codigo_localidad (NO se elimina): es la llave de cruce contra
    localidades_con_nombres.geojson (codigo_localidad) y llamadas123_consolidado_limpio.csv
    (CODIGO_LOCALIDAD). Cruzar solo por nombre de texto (Localidad) es fragil por
    inconsistencias de mayusculas/tildes.
  - Jx402 / Jx403: Jx402 = fue victima del delito (Si/No); Jx403 = denuncio el delito (Si/No),
    solo aplica a quienes respondieron Si en Jx402. NO representa "ano anterior".
  - C303, Ax401, Jx402, Jx403: se estandarizo "Si"/"No" SIN tilde en "Si", para quedar
    cohesionado con el resto de variables binarias del diccionario (Kx404_*, Lx404_*,
    Mx404_*, Nx404_*), que ya usaban "Si"/"No" sin tilde. Antes estas cuatro variables
    quedaban como "Sí"/"No" (con tilde), lo cual generaba inconsistencia de codificacion
    dentro del mismo dataset legible.
"""

RENAME_MAP = {

}

VALUE_MAPS = {
    "A6x2": {
        "1": "Cónyuge",
        "2": "Hija (o)",
        "3": "Nuera /yerno",
        "4": "Nieta (o)",
        "5": "Padre / madre",
        "6": "Suegra (o)",
        "7": "Hermana (o)",
        "8": "Cuñada (o)",
        "9": "Pariente",
        "10": "No pariente",
        "11": "Hogar unipersonal",
        "0": "Jefe del hogar"
    },
    "C1": {
        "1": "Ninguno",
        "2": "Primaria",
        "3": "Básica secundaria",
        "4": "Media",
        "5": "Técnica/tecnológica",
        "6": "Profesional",
        "7": "Postgrado"
    },
    "D1": {
        "1": "Hombre",
        "2": "Mujer",
        "3": "Intersexual"
    },
    "E1": {
        "1": "Hombre",
        "2": "Mujer",
        "3": "Mujer trans",
        "4": "Hombre trans",
        "5": "Otro",
        "99": "No responde"
    },
    "G1": {
        "1": "Soltera / o / e",
        "2": "Casada / o / e",
        "3": "Unión libre (no está casada / o/ e . Y vive en pareja hace dos años o más)",
        "4": "No está casada / o / e. Y vive en pareja hace menos de dos años",
        "5": "Divorciada / o / e o separada / o / e",
        "6": "Viuda / o / e"
    },
    "H1": {
        "1": "1",
        "2": "2",
        "3": "3",
        "4": "4",
        "5": "5",
        "6": "6",
        "7": "No tiene servicio",
        "99": "No informa"
    },
    "C303": {
        "1": "Si",
        "2": "No"
    },
    "sexo_jefe": {
        "1": "Hombre",
        "2": "Mujer",
        "3": "Intersexual"
    },
    "Ax201": {
        "1": "El /la jefe/a de hogar",
        "2": "El/la cónyuge o pareja del jefe de hogar",
        "3": "Ambos cónyuges o pareja",
        "4": "Todos los miembros del hogar",
        "5": "Otros miembros del hogar (incluyendo hijos, otros familiares, etc.)",
        "6": "Servicio contratado (p.ej., limpieza, niñera)",
        "7": "Otro familiar o pariente que ayude con las tareas del hogar pero que no vive en la vivienda",
        "8": "No se realiza"
    },
    "Bx201": {
        "1": "El /la jefe/a de hogar",
        "2": "El/la cónyuge o pareja del jefe de hogar",
        "3": "Ambos cónyuges o pareja",
        "4": "Todos los miembros del hogar",
        "5": "Otros miembros del hogar (incluyendo hijos, otros familiares, etc.)",
        "6": "Servicio contratado (p.ej., limpieza, niñera)",
        "7": "Otro familiar o pariente que ayude con las tareas del hogar pero que no vive en la vivienda",
        "8": "No se realiza"
    },
    "Cx201": {
        "1": "El /la jefe/a de hogar",
        "2": "El/la cónyuge o pareja del jefe de hogar",
        "3": "Ambos cónyuges o pareja",
        "4": "Todos los miembros del hogar",
        "5": "Otros miembros del hogar (incluyendo hijos, otros familiares, etc.)",
        "6": "Servicio contratado (p.ej., limpieza, niñera)",
        "7": "Otro familiar o pariente que ayude con las tareas del hogar pero que no vive en la vivienda",
        "8": "No se realiza"
    },
    "Dx201": {
        "1": "El /la jefe/a de hogar",
        "2": "El/la cónyuge o pareja del jefe de hogar",
        "3": "Ambos cónyuges o pareja",
        "4": "Todos los miembros del hogar",
        "5": "Otros miembros del hogar (incluyendo hijos, otros familiares, etc.)",
        "6": "Servicio contratado (p.ej., limpieza, niñera)",
        "7": "Otro familiar o pariente que ayude con las tareas del hogar pero que no vive en la vivienda",
        "8": "No se realiza"
    },
    "Ex201": {
        "1": "El /la jefe/a de hogar",
        "2": "El/la cónyuge o pareja del jefe de hogar",
        "3": "Ambos cónyuges o pareja",
        "4": "Todos los miembros del hogar",
        "5": "Otros miembros del hogar (incluyendo hijos, otros familiares, etc.)",
        "6": "Servicio contratado (p.ej., limpieza, niñera)",
        "7": "Otro familiar o pariente que ayude con las tareas del hogar pero que no vive en la vivienda",
        "8": "No se realiza"
    },
    "Fx201": {
        "1": "El /la jefe/a de hogar",
        "2": "El/la cónyuge o pareja del jefe de hogar",
        "3": "Ambos cónyuges o pareja",
        "4": "Todos los miembros del hogar",
        "5": "Otros miembros del hogar (incluyendo hijos, otros familiares, etc.)",
        "6": "Servicio contratado (p.ej., limpieza, niñera)",
        "7": "Otro familiar o pariente que ayude con las tareas del hogar pero que no vive en la vivienda",
        "8": "No se realiza"
    },
    "Gx201": {
        "1": "El /la jefe/a de hogar",
        "2": "El/la cónyuge o pareja del jefe de hogar",
        "3": "Ambos cónyuges o pareja",
        "4": "Todos los miembros del hogar",
        "5": "Otros miembros del hogar (incluyendo hijos, otros familiares, etc.)",
        "6": "Servicio contratado (p.ej., limpieza, niñera)",
        "7": "Otro familiar o pariente que ayude con las tareas del hogar pero que no vive en la vivienda",
        "8": "No se realiza"
    },
    "Hx201": {
        "1": "El /la jefe/a de hogar",
        "2": "El/la cónyuge o pareja del jefe de hogar",
        "3": "Ambos cónyuges o pareja",
        "4": "Todos los miembros del hogar",
        "5": "Otros miembros del hogar (incluyendo hijos, otros familiares, etc.)",
        "6": "Servicio contratado (p.ej., limpieza, niñera)",
        "7": "Otro familiar o pariente que ayude con las tareas del hogar pero que no vive en la vivienda",
        "8": "No se realiza"
    },
    "Ix201": {
        "1": "El /la jefe/a de hogar",
        "2": "El/la cónyuge o pareja del jefe de hogar",
        "3": "Ambos cónyuges o pareja",
        "4": "Todos los miembros del hogar",
        "5": "Otros miembros del hogar (incluyendo hijos, otros familiares, etc.)",
        "6": "Servicio contratado (p.ej., limpieza, niñera)",
        "7": "Otro familiar o pariente que ayude con las tareas del hogar pero que no vive en la vivienda",
        "8": "No se realiza"
    },
    "Jx201": {
        "1": "El /la jefe/a de hogar",
        "2": "El/la cónyuge o pareja del jefe de hogar",
        "3": "Ambos cónyuges o pareja",
        "4": "Todos los miembros del hogar",
        "5": "Otros miembros del hogar (incluyendo hijos, otros familiares, etc.)",
        "6": "Servicio contratado (p.ej., limpieza, niñera)",
        "7": "Otro familiar o pariente que ayude con las tareas del hogar pero que no vive en la vivienda",
        "8": "No se realiza"
    },
    "Ax202": {
        "1": "Garantiza el bienestar y la  salud de todos los miembros de la familia.",
        "2": "Fomenta la armonía familiar.",
        "3": "No tiene una influencia clara en nuestro bienestar.",
        "4": "Causa cierto estrés o descontento en algunos miembros de la familia.",
        "5": "Genera conflictos serios o mucho estrés entre los miembros de mi hogar.",
        "6": "No estoy seguro/a de la influencia en nuestro bienestar."
    },
    "ind_distribuciontareas_202": {
        "1": "Impacto positivo",
        "2": "Impacto neutro",
        "3": "Impacto negativo"
    },
    "Ax401": {
        "1": "Si",
        "2": "No"
    },
    "Jx402": {
        "1": "Si",
        "2": "No"
    },
    "Jx403": {
        "1": "Si",
        "2": "No"
    },
    "Kx404_1": {
        "0": "No",
        "1": "Si"
    },
    "Kx404_2": {
        "0": "No",
        "1": "Si"
    },
    "Kx404_3": {
        "0": "No",
        "1": "Si"
    },
    "Kx404_4": {
        "0": "No",
        "1": "Si"
    },
    "Kx404_5": {
        "0": "No",
        "1": "Si"
    },
    "Kx404_6": {
        "0": "No",
        "1": "Si"
    },
    "Lx404_1": {
        "0": "No",
        "1": "Si"
    },
    "Lx404_2": {
        "0": "No",
        "1": "Si"
    },
    "Lx404_3": {
        "0": "No",
        "1": "Si"
    },
    "Lx404_4": {
        "0": "No",
        "1": "Si"
    },
    "Lx404_5": {
        "0": "No",
        "1": "Si"
    },
    "Lx404_6": {
        "0": "No",
        "1": "Si"
    },
    "Mx404_1": {
        "0": "No",
        "1": "Si"
    },
    "Mx404_2": {
        "0": "No",
        "1": "Si"
    },
    "Mx404_3": {
        "0": "No",
        "1": "Si"
    },
    "Mx404_4": {
        "0": "No",
        "1": "Si"
    },
    "Mx404_5": {
        "0": "No",
        "1": "Si"
    },
    "Mx404_6": {
        "0": "No",
        "1": "Si"
    },
    "Nx404_1": {
        "0": "No",
        "1": "Si"
    },
    "Nx404_2": {
        "0": "No",
        "1": "Si"
    },
    "Nx404_3": {
        "0": "No",
        "1": "Si"
    },
    "Nx404_4": {
        "0": "No",
        "1": "Si"
    },
    "Nx404_5": {
        "0": "No",
        "1": "Si"
    },
    "Nx404_6": {
        "0": "No",
        "1": "Si"
    },
    "F405": {
        "1": "Muy inseguro",
        "2": "Inseguro/a",
        "3": "Ni seguro ni inseguro",
        "4": "Seguro/a",
        "5": "Muy seguro/a",
        "6": "Nunca sale solo/a de día"
    },
    "G406": {
        "1": "Muy inseguro",
        "2": "Inseguro/a",
        "3": "Ni seguro ni inseguro",
        "4": "Seguro/a",
        "5": "Muy seguro/a",
        "6": "Nunca sale solo/a de noche"
    },
    "Dx704": {
        "1": "Totalmente en desacuerdo",
        "2": "En desacuerdo",
        "3": "Ni de acuerdo. Ni en desacuerdo",
        "4": "De acuerdo",
        "5": "Totalmente de acuerdo",
        "99": "Ns/Nr"
    },
    "Bx704": {
        "1": "Totalmente en desacuerdo",
        "2": "En desacuerdo",
        "3": "Ni de acuerdo. Ni en desacuerdo",
        "4": "De acuerdo",
        "5": "Totalmente de acuerdo",
        "99": "Ns/Nr"
    },
    "Ax102": {
        "0": "Ningún día",
        "1": "Varios días",
        "2": "Más de la mitad de los días",
        "3": "Casi todos los días"
    },
    "Bx102": {
        "0": "Ningún día",
        "1": "Varios días",
        "2": "Más de la mitad de los días",
        "3": "Casi todos los días"
    },
    "Cx102": {
        "0": "Ningún día",
        "1": "Varios días",
        "2": "Más de la mitad de los días",
        "3": "Casi todos los días"
    },
    "Dx102": {
        "0": "Ningún día",
        "1": "Varios días",
        "2": "Más de la mitad de los días",
        "3": "Casi todos los días"
    },
    "Ex102": {
        "0": "Ningún día",
        "1": "Varios días",
        "2": "Más de la mitad de los días",
        "3": "Casi todos los días"
    },
    "Fx102": {
        "0": "Ningún día",
        "1": "Varios días",
        "2": "Más de la mitad de los días",
        "3": "Casi todos los días"
    },
    "Gx102": {
        "0": "Ningún día",
        "1": "Varios días",
        "2": "Más de la mitad de los días",
        "3": "Casi todos los días"
    },
    "A101": {
        "1": "Muy malo",
        "2": "Malo",
        "3": "Regular",
        "4": "Bueno",
        "5": "Muy bueno",
        "99": "Ns/Nr"
    },
    "ind_salud_102": {
        "0": "No se aprecia ansiedad",
        "1": "Se aprecian síntomas de ansiedad leves",
        "2": "Se aprecian síntomas de ansiedad moderados",
        "3": "Se aprecian síntomas de ansiedad severos"
    }
}

TIPOS = {
    "Fecha": "texto_libre",
    "SectorUPL": "texto_libre",
    "Localidad": "texto_libre",
    "Unidad_de_Planeamiento_Local_UPL": "texto_libre",
    "codigo_localidad": "llave_codigo",
    "A3": "continua",
    "A4": "continua",
    "A5": "continua",
    "A6x2": "categorica",
    "A6x3": "continua",
    "C1": "categorica",
    "D1": "categorica",
    "E1": "categorica",
    "E1x1": "texto_libre",
    "G1": "categorica",
    "H1": "categorica",
    "C303": "categorica",
    "sexo_jefe": "categorica",
    "Ax201": "categorica",
    "Bx201": "categorica",
    "Cx201": "categorica",
    "Dx201": "categorica",
    "Ex201": "categorica",
    "Fx201": "categorica",
    "Gx201": "categorica",
    "Hx201": "categorica",
    "Ix201": "categorica",
    "Jx201": "categorica",
    "Ax202": "categorica",
    "ind_distribuciontareas_202": "categorica",
    "Ax401": "categorica",
    "Jx402": "categorica",
    "Jx403": "categorica",
    "Kx404_1": "categorica",
    "Kx404_2": "categorica",
    "Kx404_3": "categorica",
    "Kx404_4": "categorica",
    "Kx404_5": "categorica",
    "Kx404_6": "categorica",
    "Lx404_1": "categorica",
    "Lx404_2": "categorica",
    "Lx404_3": "categorica",
    "Lx404_4": "categorica",
    "Lx404_5": "categorica",
    "Lx404_6": "categorica",
    "Mx404_1": "categorica",
    "Mx404_2": "categorica",
    "Mx404_3": "categorica",
    "Mx404_4": "categorica",
    "Mx404_5": "categorica",
    "Mx404_6": "categorica",
    "Nx404_1": "categorica",
    "Nx404_2": "categorica",
    "Nx404_3": "categorica",
    "Nx404_4": "categorica",
    "Nx404_5": "categorica",
    "Nx404_6": "categorica",
    "F405": "categorica",
    "G406": "categorica",
    "IPS_dia": "continua",
    "IPS_noche": "continua",
    "IPSJ_A": "continua",
    "IPSJ_C": "continua",
    "IPSJ_E": "continua",
    "Dx704": "categorica",
    "ICG_D": "continua",
    "Bx704": "categorica",
    "ICG_B": "continua",
    "Ax102": "categorica",
    "Bx102": "categorica",
    "Cx102": "categorica",
    "Dx102": "categorica",
    "Ex102": "categorica",
    "Fx102": "categorica",
    "Gx102": "categorica",
    "A101": "categorica",
    "ind_salud_101": "continua",
    "ind_salud_102": "categorica",
    "fexp_calp_anu": "continua",
    "fexp_calh_anu": "continua"
}