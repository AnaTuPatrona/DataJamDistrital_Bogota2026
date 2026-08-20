from pathlib import Path
import pandas as pd
import re
import unicodedata


# ============================================================
# CONFIGURACIÓN
# ============================================================

BASE_DIR = Path("../data")
OUTPUT_DIR = Path("../outputs")

OUTPUT_DIR.mkdir(exist_ok=True)

FILE_PATTERN = r"^llamadas123_.*\d{4}.*\.csv$"

DATE_COLUMN = "FECHA_INICIO_DESPLAZAMIENTO_MOVIL"

LOCALITY_ID_COLUMN = "CODIGO_LOCALIDAD"
LOCALITY_NAME_COLUMN = "LOCALIDAD"

CSV_SEPARATOR = ";"

OUTPUT_FILE = OUTPUT_DIR / "llamadas123_consolidado_limpio.csv"



# ============================================================
# DETECCIÓN Y LECTURA ROBUSTA DE ENCODING
# ============================================================

def leer_csv(path):

    encodings = [
        "utf-8-sig",
        "utf-8",
        "cp1252",
        "latin1",
        "ISO-8859-1",
        "macroman"
    ]


    ultimo_error = None


    for encoding in encodings:

        try:

            df = pd.read_csv(
                path,
                sep=CSV_SEPARATOR,
                encoding=encoding,
                dtype=str,
                on_bad_lines="warn"
            )


            print(
                f"✓ {path.name} leído con {encoding}"
            )


            return df


        except Exception as error:

            ultimo_error = error


    raise Exception(
        f"No se pudo leer {path.name}: {ultimo_error}"
    )



# ============================================================
# BUSQUEDA ARCHIVOS
# ============================================================

def encontrar_archivos():

    regex = re.compile(
        FILE_PATTERN,
        re.IGNORECASE
    )


    archivos = [
        archivo
        for archivo in BASE_DIR.iterdir()
        if archivo.is_file()
        and regex.match(archivo.name)
    ]


    if not archivos:
        raise Exception(
            "No existen archivos compatibles"
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
            f"""
            Archivo:
            {archivo.name}

            Columnas faltantes:
            {faltantes}
            """
        )



def validar_estructura(dataframes):

    columnas_base = set(
        dataframes[0][1].columns
    )


    for nombre, df in dataframes:

        diferencia = (
            columnas_base ^
            set(df.columns)
        )


        if diferencia:

            raise Exception(
                f"""
                Diferencia estructural:

                Archivo:
                {nombre}

                Columnas:
                {diferencia}
                """
            )



# ============================================================
# LIMPIEZA TEXTO
# ============================================================

def limpiar_texto(valor):

    if pd.isna(valor):
        return pd.NA


    valor = str(valor)


    # elimina caracteres invisibles
    valor = unicodedata.normalize(
        "NFKC",
        valor
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
            include="object"
        )
        .columns
    )


    for columna in columnas_texto:

        df[columna] = (

            df[columna]
            .apply(limpiar_texto)
            .str.upper()
        )


    # Vacíos como null

    df = df.replace(
        r"^\s*$",
        pd.NA,
        regex=True
    )


    # eliminar duplicados

    inicial = len(df)

    df = df.drop_duplicates()

    print(
        f"Duplicados eliminados: {inicial-len(df)}"
    )


    return df



# ============================================================
# VARIABLES TEMPORALES
# ============================================================

def agregar_variables_fecha(df):


    df[DATE_COLUMN] = pd.to_datetime(

        df[DATE_COLUMN],

        errors="coerce",

        dayfirst=True
    )


    invalidas = (

        df[DATE_COLUMN]
        .isna()
        .sum()
    )


    if invalidas:

        print(
            f"Fechas inválidas: {invalidas}"
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
# ETL
# ============================================================

def ejecutar_etl():


    archivos = encontrar_archivos()


    print(
        f"""
        Archivos encontrados:
        {len(archivos)}
        """
    )


    dataframes = []


    for archivo in archivos:


        df = leer_csv(
            archivo
        )


        validar_columnas(
            df,
            archivo
        )


        # trazabilidad

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


    print(
        f"Registros iniciales: {len(consolidado)}"
    )


    consolidado = normalizar_dataset(
        consolidado
    )


    consolidado = agregar_variables_fecha(
        consolidado
    )


    # asegurar localidad como referencia directa

    consolidado[LOCALITY_ID_COLUMN] = (
        consolidado[LOCALITY_ID_COLUMN]
        .astype("Int64")
    )


    consolidado.to_csv(

        OUTPUT_FILE,

        sep=";",

        encoding="utf-8-sig",

        index=False

    )


    print(
        """
        =========================
        ETL FINALIZADO
        =========================
        """
    )


    print(
        f"Registros finales: {len(consolidado)}"
    )


    print(
        f"Archivo generado: {OUTPUT_FILE}"
    )



if __name__ == "__main__":

    ejecutar_etl()