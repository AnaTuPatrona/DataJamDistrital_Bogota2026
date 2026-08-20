"""
Genera un diccionario de preguntas + variables para el dataset limpio.

Entradas esperadas en /content:
  - preguntas_consolidados.csv
  - variables_consolidados.csv

Salida:
  - diccionario_preguntas_variables.csv

El diccionario se mantiene separado del dataset de respuestas.
La llave principal es la columna `variable`, por ejemplo P11.2, P53.10, D3, V1.

Esto evita repetir el enunciado de cada pregunta miles de veces en el CSV
de respuestas y permite hacer JOIN cuando los datos se transformen a formato largo.
"""

from pathlib import Path
import csv

import warnings

warnings.filterwarnings(
    "ignore",
    category=SyntaxWarning
)
warnings.filterwarnings("ignore")

BASE = Path("../data/encuestaBienal")
OUT = Path("../outputs")

PREGUNTAS_PATH = BASE / "preguntas_consolidados.csv"
VARIABLES_PATH = BASE / "variables_consolidados.csv"
OUTPUT_PATH = BASE / "diccionario_preguntas_variables.csv"

SELECTED_COLUMNS = (
    ["encuestado_id", "ID", "Sector", "Seccion", "Manzana", "V1", "V2",
     "P2", "P3", "P7", "P8", "P9"]
    + [f"P10.{i}" for i in range(1, 12)]
    + [f"P11.{i}" for i in range(1, 5)]
    + [f"P12.{i}" for i in range(1, 7)]
    + ["P37"]
    + [f"P51.{i}" for i in range(1, 5)]
    + ["P53.2", "P53.6", "P53.10", "P53.11", "P53.12", "P53.13"]
    + ["P54", "P63", "P65.5", "P65.6", "P66.1", "P66.8",
       "P72.10", "P72.11", "P72.12", "P72.13", "P72.14",
       "P73", "P74", "P75", "P75.1", "P77",
       "D1", "D2", "D3", "D3_1", "D4", "D5", "D7", "D8", "D8.1",
       "D9", "D10"]
    + [f"D11.{i}" for i in range(1, 10)]
    + ["D11.11", "D12"]
    + [f"D12.{i}" for i in range(1, 12)]
    + ["D13", "D14", "FACTOR"]
)

# Nombres según la hoja de secciones revisada en el proceso.
# Si después exportas la hoja `secciones` a CSV, este mapa puede
# reemplazarse por una lectura automática.
SECTION_NAMES = {
    "1": "Sociodemográfico / Identificación",
    "2": "Ubicación / Hogar",
    "3": "Inclusión e Identidad",
    "4": "Equidad de género",
    "5": "Ambiente",
    "6": "Cultura Política y Ciudadana",
    "7": "Convivencia y Cultura de Paz",
    "8": "Espacio Público",
    "9": "Arte, Cultura y Patrimonio",
    "10": "Actividad Física y Deporte",
    "99": "Registro / Técnico",
}

def read_semicolon(path):
    with path.open("r", encoding="cp1252", newline="") as f:
        return list(csv.DictReader(f, delimiter=";"))

preguntas = read_semicolon(PREGUNTAS_PATH)
variables = read_semicolon(VARIABLES_PATH)

pregunta_por_indice = {
    row["indice_pregunta"].strip(): row
    for row in preguntas
    if row.get("indice_pregunta")
}

variable_por_codigo = {
    row["codigo_variable"].strip(): row
    for row in variables
    if row.get("codigo_variable")
}

missing = [
    variable for variable in SELECTED_COLUMNS
    if variable not in variable_por_codigo
]
if missing:
    raise ValueError(
        "Variables del compilado maestro no encontradas:\n"
        + "\n".join(missing)
    )

rows = []

for variable in SELECTED_COLUMNS:
    v = variable_por_codigo[variable]
    indice = v.get("indice_pregunta", "").strip()
    p = pregunta_por_indice.get(indice, {})

    num_seccion = (
        p.get("num_seccion", "").strip()
        or v.get("num_seccion", "").strip()
    )

    rows.append({
        "variable": variable,
        "pregunta_codigo": (
            p.get("etiqueta_1", "").strip()
            or v.get("pregunta", "").strip()
        ),
        "pregunta_nombre": p.get("nombre", "").strip(),
        "enunciado_pregunta": p.get("enunciado_1", "").strip(),
        "numero_seccion": num_seccion,
        "seccion": SECTION_NAMES.get(num_seccion, ""),
        "tipo_variable": v.get("tipo", "").strip(),
        "titulo_variable": v.get("titulo", "").strip(),
        "enunciado_subvariable": v.get("enunciado_2", "").strip(),
        "etiqueta_corta": v.get("etiqueta_corta", "").strip(),
        "en_cubo": v.get("en_cubo", "").strip(),
        "unidad_medida": v.get("unidad_medida", "").strip(),
    })

fieldnames = [
    "variable",
    "pregunta_codigo",
    "pregunta_nombre",
    "enunciado_pregunta",
    "numero_seccion",
    "seccion",
    "tipo_variable",
    "titulo_variable",
    "enunciado_subvariable",
    "etiqueta_corta",
    "en_cubo",
    "unidad_medida",
]

with OUTPUT_PATH.open(
    "w", encoding="utf-8-sig", newline=""
) as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print("Diccionario generado correctamente")
print(f"Variables documentadas: {len(rows)}")
print(f"Archivo: {OUTPUT_PATH}")

# Ejemplo opcional con pandas:
#
# respuestas = pd.read_csv("/content/dataset_encuesta_limpio.csv")
# diccionario = pd.read_csv("/content/diccionario_preguntas_variables.csv")
#
# # Para unir el diccionario conviene pasar las respuestas a formato largo:
# respuestas_long = respuestas.melt(
#     id_vars=["encuestado_id", "ID", "V1", "V1_etiqueta"],
#     var_name="variable",
#     value_name="respuesta"
# )
#
# enriquecido = respuestas_long.merge(
#     diccionario,
#     on="variable",
#     how="left"
# )