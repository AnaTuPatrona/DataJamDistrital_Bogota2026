from pathlib import Path
import pandas as pd
import re
import unicodedata

try:
    import chardet
except ImportError:
    chardet = None
import warnings

warnings.filterwarnings(
    "ignore",
    category=SyntaxWarning
)
warnings.filterwarnings("ignore")

# ============================================================
# CONFIGURACIÓN
# ============================================================

BASE_DIR = Path("../data")
OUTPUT_DIR = Path("../outputs")

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

FILE_PATTERN = r"^llamadas123_.*\d{4}\.csv$"

DATE_COLUMN = "FECHA_INICIO_DESPLAZAMIENTO_MOVIL"
LOCALITY_ID_COLUMN = "CODIGO_LOCALIDAD"
LOCALITY_NAME_COLUMN = "LOCALIDAD"

CSV_SEPARATOR = ";"

OUTPUT_FILE = OUTPUT_DIR / "llamadas123_consolidado_limpio.csv"


# ============================================================
# DETECCIÓN Y LECTURA ROBUSTA DE ENCODING
# ============================================================

def detectar_encoding(path):
    """
    Detecta el encoding real del archivo sin usar reemplazos silenciosos.

    Prioridad:
    1. UTF-8 / UTF-8-SIG si el archivo es UTF-8 válido.
    2. chardet para archivos heredados (por ejemplo MacRoman/cp1252).
    3. Fallback a MacRoman.
    """
    contenido = path.read_bytes()

    if contenido.startswith(b"\xef\xbb\xbf"):
        return "utf-8-sig"

    try:
        contenido.decode("utf-8")
        return "utf-8"
    except UnicodeDecodeError:
        pass

    if chardet is not None:
        deteccion = chardet.detect(contenido)
        encoding = deteccion.get("encoding")

        if encoding:
            normalizados = {
                "ascii": "utf-8",
                "utf-8-sig": "utf-8-sig",
                "utf-8": "utf-8",
                "windows-1252": "cp1252",
                "iso-8859-1": "latin1",
                "macroman": "macroman",
                "macintosh": "macroman",
            }

            return normalizados.get(
                encoding.lower(),
                encoding
            )

    return "macroman"


def leer_csv(path):
    """
    Lee el CSV usando primero el encoding detectado y luego
    alternativas conocidas.

    No usa encoding_errors='replace' porque eso puede ocultar
    un encoding incorrecto y corromper caracteres.
    """
    encoding_detectado = detectar_encoding(path)

    candidatos = [
        encoding_detectado,
        "utf-8-sig",
        "utf-8",
        "macroman",
        "cp1252",
        "latin1",
    ]

    candidatos = list(dict.fromkeys(candidatos))

    errores = []

    for encoding in candidatos:
        try:
            df = pd.read_csv(
                path,
                sep=CSV_SEPARATOR,
                encoding=encoding,
                dtype=str,
                on_bad_lines="warn"
            )

            print(
                f"[OK] {path.name} leido correctamente con {encoding}"
            )

            return df

        except (UnicodeDecodeError, UnicodeError) as error:
            errores.append(
                f"{encoding}: {type(error).__name__}: {error}"
            )

        except Exception as error:
            errores.append(
                f"{encoding}: {type(error).__name__}: {error}"
            )

    detalle = "\n".join(
        f"  - {error}"
        for error in errores
    )

    raise Exception(
        f"No fue posible leer {path.name}.\n"
        f"Intentos realizados:\n{detalle}"
    )


# ============================================================
# BÚSQUEDA DE ARCHIVOS
# ============================================================

def encontrar_archivos():
    if not BASE_DIR.exists():
        raise FileNotFoundError(
            f"No existe la carpeta de datos: {BASE_DIR.resolve()}"
        )

    regex = re.compile(
        FILE_PATTERN,
        re.IGNORECASE
    )

    archivos = [
        archivo
        for archivo in BASE_DIR.iterdir()
        if archivo.is_file()
        and regex.fullmatch(archivo.name)
    ]

    if not archivos:
        raise Exception(
            f"No existen archivos compatibles en {BASE_DIR.resolve()}"
        )

    return sorted(archivos)


# ============================================================
# VALIDACIONES
# ============================================================

def validar_columnas(df, archivo):
    requeridas = {
        DATE_COLUMN,
        LOCALITY_ID_COLUMN,
        LOCALITY_NAME_COLUMN
    }

    faltantes = requeridas - set(df.columns)

    if faltantes:
        raise Exception(
            f"El archivo {archivo.name} no contiene las "
            f"columnas requeridas: {sorted(faltantes)}"
        )


def validar_estructura(dataframes):
    columnas_base = set(
        dataframes[0][1].columns
    )

    for nombre, df in dataframes:
        diferencia = (
            columnas_base
            ^
            set(df.columns)
        )

        if diferencia:
            raise Exception(
                f"Diferencia estructural en {nombre}. "
                f"Columnas diferentes: {sorted(diferencia)}"
            )


# ============================================================
# LIMPIEZA DE TEXTO
# ============================================================

def limpiar_texto(valor):
    if pd.isna(valor):
        return pd.NA

    valor = unicodedata.normalize(
        "NFKC",
        str(valor)
    )

    reemplazos = {
        "¤": "ñ",
        "¥": "Ñ",
        "Ã±": "ñ",
        "Ã‘": "Ñ",
        "â€“": "-",
        "–": "-",
        "—": "-"
    }

    for viejo, nuevo in reemplazos.items():
        valor = valor.replace(
            viejo,
            nuevo
        )

    return valor.strip()


def normalizar_columnas(df):
    df.columns = (
        df.columns
        .str.strip()
        .str.upper()
        .str.replace(
            " ",
            "_"
        )
    )

    return df


def normalizar_dataset(df):
    df = normalizar_columnas(df)

    columnas_texto = (
        df.select_dtypes(
            include=["object", "string"]
        )
        .columns
    )

    for columna in columnas_texto:
        df[columna] = (
            df[columna]
            .apply(limpiar_texto)
            .str.upper()
        )

    df = df.replace(
        r"^\s*$",
        pd.NA,
        regex=True
    )

    registros_inicio = len(df)

    df = df.drop_duplicates()

    registros_fin = len(df)

    print(
        f"Duplicados eliminados: "
        f"{registros_inicio - registros_fin}"
    )

    return df


# ============================================================
# VARIABLES TEMPORALES
# ============================================================

def agregar_variables_fecha(df):
    """
    Los archivos contienen más de un formato de fecha:
      - 2025-03-01 00:02:33
      - 1/03/2026 0:08

    format='mixed' permite interpretar ambos formatos dentro
    de la misma columna.
    """
    df[DATE_COLUMN] = pd.to_datetime(
        df[DATE_COLUMN],
        errors="coerce",
        format="mixed",
        dayfirst=True
    )

    fechas_invalidas = (
        df[DATE_COLUMN]
        .isna()
        .sum()
    )

    print(
        f"Fechas invalidas encontradas: "
        f"{fechas_invalidas}"
    )

    df["MES"] = (
        df[DATE_COLUMN]
        .dt.month
    )

    df["AÑO"] = (
        df[DATE_COLUMN]
        .dt.year
    )

    return df


# ============================================================
# NORMALIZACIÓN DEL ID DE LOCALIDAD
# ============================================================

def normalizar_codigo_localidad(df):
    """
    Conserva códigos numéricos de localidad como enteros.

    Valores textuales como SIN_D o FUERA_DE_BOGOTA pasan a
    <NA> sin eliminar la fila.
    """
    codigos_originales = df[LOCALITY_ID_COLUMN].copy()

    df[LOCALITY_ID_COLUMN] = (
        pd.to_numeric(
            df[LOCALITY_ID_COLUMN],
            errors="coerce"
        )
        .astype("Int64")
    )

    invalidos = (
        codigos_originales.notna()
        &
        df[LOCALITY_ID_COLUMN].isna()
    )

    cantidad_invalidos = int(
        invalidos.sum()
    )

    print(
        f"Codigos de localidad no numericos "
        f"convertidos a NA: {cantidad_invalidos}"
    )

    return df


# ============================================================
# PROCESO ETL
# ============================================================

def ejecutar_etl():
    archivos = encontrar_archivos()

    print()
    print(
        f"Archivos encontrados: {len(archivos)}"
    )
    print()

    dataframes = []

    for archivo in archivos:
        df = leer_csv(
            archivo
        )

        validar_columnas(
            df,
            archivo
        )

        df["ARCHIVO_ORIGEN"] = archivo.name

        dataframes.append(
            (
                archivo.name,
                df
            )
        )

    validar_estructura(
        dataframes
    )

    consolidado = pd.concat(
        [
            df
            for _, df in dataframes
        ],
        ignore_index=True
    )

    print()
    print(
        f"Registros iniciales: {len(consolidado)}"
    )

    consolidado = normalizar_dataset(
        consolidado
    )

    consolidado = agregar_variables_fecha(
        consolidado
    )

    consolidado = normalizar_codigo_localidad(
        consolidado
    )

    consolidado.to_csv(
        OUTPUT_FILE,
        sep=CSV_SEPARATOR,
        encoding="utf-8-sig",
        index=False
    )

    print()
    print(
        "========================="
    )
    print(
        "ETL FINALIZADO"
    )
    print(
        "========================="
    )
    print(
        f"Registros finales: {len(consolidado)}"
    )
    print(
        f"Archivo generado: {OUTPUT_FILE}"
    )


# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":
    ejecutar_etl()