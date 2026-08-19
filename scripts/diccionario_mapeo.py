# -*- coding: utf-8 -*-
"""
Diccionario de mapeo generado a partir de:
  - 20260331_diccionario_base_ano_movil_2025.xlsx (preguntas y opciones oficiales)
  - Seleccionados_encuesta_distrital_de_percepcion.txt (columnas seleccionadas)
Traduce Encuesta_percepcion_limpia.csv a nombres de columna y etiquetas legibles.
"""

RENAME_MAP = {
    "Fecha": "Fecha",
    "SectorUPL": "SectorUPL",
    "Localidad": "Localidad",
    "Unidad_de_Planeamiento_Local_UPL": "Unidad_de_Planeamiento_Local_UPL",
    "A6x2": "2. Parentesco con el jefe del hogar",
    "A6x3": "Edad de la persona.",
    "C1": "C. ¿Cuál es el nivel educativo más alto que usted ha alcanzado?",
    "D1": "D. Sexo al nacer",
    "E1": "E. ¿Usted se reconoce como?",
    "E1x1": "¿Otra cuál?",
    "G1": "G. ¿Cuál es su estado civil?",
    "H1": "H. Según el recibo o servicio de energía eléctrica  ¿cuál es el estrato de esta vivienda?",
    "C303": "303. ¿Usted se considera pobre?",
    "sexo_jefe": "Sexo del jefe de hogar",
    "Ax201": "a. Limpieza general de la casa",
    "Bx201": "b. Mantenimiento y reparaciones del hogar",
    "Cx201": "c. Lavado de ropa",
    "Dx201": "d. Planchar",
    "Ex201": "e. Cocinar",
    "Fx201": "f. Compras del supermercado",
    "Gx201": "g. Pago de facturas y Planear/hacer el presupuesto del hogar",
    "Hx201": "h. Cuidado de los niños",
    "Ix201": "i. Ayuda con las tareas escolares de los niños",
    "Jx201": "j. Cuidado de personas mayores o dependientes",
    "Ax202": "202. ¿Cómo afecta la anterior distribución de tareas domésticas y de cuidado en el bienestar de su hogar? Por favor elija una de las frases que le voy a leer.",
    "ind_distribuciontareas_202": "Impacto de la distribución de tareas domésticas y de cuidado en el bienestar familiar.",
    "Jx402": "j. Violencia intrafamiliar (delito sufrido - este año)",
    "Jx403": "j. Violencia intrafamiliar (delito sufrido - año anterior)",
    "Kx404_1": "k. Acoso sexual (Silbidos, comentarios sexuales, etc.) (En su residencia u otra residencia)",
    "Kx404_2": "k. Acoso sexual (Silbidos, comentarios sexuales, etc.) (En la cuadra, conjunto, barrio)",
    "Kx404_3": "k. Acoso sexual (Silbidos, comentarios sexuales, etc.) (En otro espacio público)",
    "Kx404_4": "k. Acoso sexual (Silbidos, comentarios sexuales, etc.) (En el transporte público)",
    "Kx404_5": "k. Acoso sexual (Silbidos, comentarios sexuales, etc.) (En el lugar de trabajo)",
    "Kx404_6": "k. Acoso sexual (Silbidos, comentarios sexuales, etc.) (No afrontó la situación)",
    "Lx404_1": "l. Presenció casos de violencia intrafamiliar (En su residencia u otra residencia)",
    "Lx404_2": "l. Presenció casos de violencia intrafamiliar (En la cuadra, conjunto, barrio)",
    "Lx404_3": "l. Presenció casos de violencia intrafamiliar (En otro espacio público)",
    "Lx404_4": "l. Presenció casos de violencia intrafamiliar (En el transporte público)",
    "Lx404_5": "l. Presenció casos de violencia intrafamiliar (En el lugar de trabajo)",
    "Lx404_6": "l. Presenció casos de violencia intrafamiliar (No afrontó la situación)",
    "Mx404_1": "m. Presenció casos de violencia contra la mujer (En su residencia u otra residencia)",
    "Mx404_2": "m. Presenció casos de violencia contra la mujer (En la cuadra, conjunto, barrio)",
    "Mx404_3": "m. Presenció casos de violencia contra la mujer (En otro espacio público)",
    "Mx404_4": "m. Presenció casos de violencia contra la mujer (En el transporte público)",
    "Mx404_5": "m. Presenció casos de violencia contra la mujer (En el lugar de trabajo)",
    "Mx404_6": "m. Presenció casos de violencia contra la mujer (No afrontó la situación)",
    "Nx404_1": "n. Presenció casos de violencia contra niños, niñas y adolescentes (NNA) (En su residencia u otra residencia)",
    "Nx404_2": "n. Presenció casos de violencia contra niños, niñas y adolescentes (NNA) (En la cuadra, conjunto, barrio)",
    "Nx404_3": "n. Presenció casos de violencia contra niños, niñas y adolescentes (NNA) (En otro espacio público)",
    "Nx404_4": "n. Presenció casos de violencia contra niños, niñas y adolescentes (NNA) (En el transporte público)",
    "Nx404_5": "n. Presenció casos de violencia contra niños, niñas y adolescentes (NNA) (En el lugar de trabajo)",
    "Nx404_6": "n. Presenció casos de violencia contra niños, niñas y adolescentes (NNA) (No afrontó la situación)",
    "F405": "405. ¿Qué tan seguro se siente usted caminando solo por su barrio de día",
    "G406": "406. ¿Qué tan seguro se siente usted caminando solo por su barrio de noche",
    "IPS_dia": "Percepción promedio de la seguridad al caminar de día por su barrio.",
    "IPS_noche": "Percepción promedio de la seguridad al caminar de noche por su barrio.",
    "IPSJ_A": "Percepción promedio sobre la rapidez de las autoridades ante incidentes de seguridad que ocurren en el barrio.",
    "IPSJ_C": "Percepción promedio sobre la disponibilidad y facilidad de acceso a la información y los medios para denunciar delitos.",
    "IPSJ_E": "Percepción promedio de la aplicación de justicia sobre quienes cometen delitos.",
    "Dx704": "d. En la ciudad las personas son incluyentes y respetan la diversidad (cultural, étnica, socioeconómica, orientación sexual, etc.)",
    "ICG_D": "Percepción promedio sobre el respeto de los ciudadanos hacia la inclusión y la diversidad.",
    "Bx704": "b. Confío en que mis vecinos me ayudarían ante cualquier problema o necesidad",
    "ICG_B": "Confianza promedio en la ayuda que brindarían los vecinos ante cualquier problema o necesidad.",
    "Ax102": "a. ¿Sensación de nerviosismo, de ansiedad, de tener los nervios de punta?",
    "Bx102": "b. ¿Incapacidad de evadir o controlar sus preocupaciones?",
    "Cx102": "c. ¿Preocupación excesiva por diferentes cosas o situaciones?",
    "Dx102": "d. ¿Dificultad para relajarse?",
    "Ex102": "e. ¿Tan intranquilo, inquieto o agitado que le resulta difícil quedarse quieto?",
    "Fx102": "f. ¿Que se enfada o irrita con facilidad?",
    "Gx102": "g. ¿Miedo o susto, como si algo malo pudiera suceder?",
    "A101": "101. ¿Usted considera que su estado de salud actual es …?",
    "ind_salud_101": "Indicador de percepción del estado de salud",
    "ind_salud_102": "Escala del Trastorno de Ansiedad Generalizada (GAD-7)",
    "fexp_calp_anu": "Factor de expansión calibrado bimestral para personas.",
    "fexp_calh_anu": "Factor de expansión calibrado bimestral para hogares"
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
        "1": "Sí",
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
    "Jx402": {
        "1": "Sí",
        "2": "No"
    },
    "Jx403": {
        "1": "Sí",
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
