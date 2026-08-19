
from pathlib import Path
import csv

# En Google Colab puedes dejar los archivos en /content.
BASE = Path("../data/encuestaBienal")
OUT = Path("../outputs")

DATA_PATH = BASE / "datos_respuestas_consolidados.csv"
VARIABLES_PATH = BASE / "variables_consolidados.csv"
LABELS_PATH = BASE / "Eriquetas_respuestas_consolidados.csv"
OUTPUT_PATH = OUT / "dataset_encuesta_limpio.csv"

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

def read_dicts(path):
    with path.open("r", encoding="cp1252", newline="") as f:
        return list(csv.DictReader(f, delimiter=";"))

variables = read_dicts(VARIABLES_PATH)
labels = read_dicts(LABELS_PATH)

var_meta = {
    row["codigo_variable"]: row
    for row in variables
    if row.get("codigo_variable")
}

label_maps = {}
for row in labels:
    question = row["etiqueta_pregunta"].strip()
    code = row["codigo_respuesta"].strip()
    label = row["etiqueta_respuesta"].strip()
    label_maps.setdefault(question, {})[code] = label

labelable = []
for col in SELECTED_COLUMNS:
    meta = var_meta.get(col)
    if not meta:
        continue

    question = meta.get("pregunta", "").strip()

    if (
        question in label_maps
        and col not in {"D3", "FACTOR"}
        and meta.get("en_cubo", "").strip() != "0"
    ):
        labelable.append(col)

with DATA_PATH.open("r", encoding="cp1252", newline="") as src:
    reader = csv.DictReader(src, delimiter=";")

    missing = [
        col for col in SELECTED_COLUMNS
        if col not in (reader.fieldnames or [])
    ]
    if missing:
        raise ValueError(
            "Estas columnas del compilado maestro no aparecen en datos:\n"
            + "\n".join(missing)
        )

    output_headers = []
    for col in SELECTED_COLUMNS:
        output_headers.append(col)
        if col in labelable:
            output_headers.append(f"{col}_etiqueta")

    with OUTPUT_PATH.open(
        "w", encoding="utf-8-sig", newline=""
    ) as dst:
        writer = csv.DictWriter(
            dst,
            fieldnames=output_headers,
            delimiter=","
        )
        writer.writeheader()

        rows_written = 0

        for row in reader:
            out = {}

            for col in SELECTED_COLUMNS:
                value = (row.get(col) or "").strip()

                if col == "FACTOR" and value:
                    value = value.replace(",", ".")

                out[col] = value

                if col in labelable:
                    question = var_meta[col]["pregunta"].strip()
                    out[f"{col}_etiqueta"] = (
                        label_maps.get(question, {}).get(value, "")
                        if value else ""
                    )

            writer.writerow(out)
            rows_written += 1

print("ETL finalizado")
print(f"Filas procesadas: {rows_written}")
print(f"Columnas maestras: {len(SELECTED_COLUMNS)}")
print(f"Columnas con etiqueta añadida: {len(labelable)}")
print(f"Archivo generado: {OUTPUT_PATH}")

# Validaciones rápidas
assert "CX" not in SELECTED_COLUMNS
assert "CY" not in SELECTED_COLUMNS
assert "V1" in SELECTED_COLUMNS
assert "FACTOR" in SELECTED_COLUMNS