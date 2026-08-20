from pathlib import Path
import pandas as pd
import re


# ============================================================
# CONFIGURACIÓN DEL DATASET
# ============================================================

BASE_DIR = Path("../data")
OUTPUT_DIR = Path("../outputs")


# Archivos aceptados
# Ejemplo:
# llamadas123_marzo2025.csv
# llamadas123_junio2025.csv
FILE_PATTERN = r"^llamadas123_.*\d{4}\.csv$"


# Columna principal de fecha
DATE_COLUMN = "FECHA_INICIO_DESPLAZAMIENTO_MOVIL"


# Separador CSV
CSV_SEPARATOR = ";"


# Archivo final
OUTPUT_FILE = OUTPUT_DIR / "llamadas123_consolidado_limpio.csv"



# ============================================================
# LECTURA DE ARCHIVOS
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
            "No se encontraron archivos compatibles"
        )


    return sorted(archivos)



def leer_csv(path):

    codificaciones = [

        "utf-8-sig",
        "cp1252",
        "latin1"

    ]


    for encoding in codificaciones:

        try:

            return pd.read_csv(

                path,

                sep=CSV_SEPARATOR,

                encoding=encoding

            )


        except UnicodeDecodeError:

            continue


    raise Exception(
        f"No fue posible leer {path.name}"
    )



# ============================================================
# VALIDACIONES
# ============================================================

def validar_columnas(df, archivo):

    if DATE_COLUMN not in df.columns:

        raise Exception(
            f"""
            El archivo {archivo.name}

            no contiene la columna requerida:

            {DATE_COLUMN}
            """
        )



def validar_estructura(dataframes):

    """
    dataframes tiene esta estructura:

    [
        ("archivo.csv", dataframe),
        ("archivo2.csv", dataframe)
    ]

    """

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
                f"""
                Diferencias encontradas en:

                {nombre}

                Columnas diferentes:

                {diferencia}
                """
            )



# ============================================================
# NORMALIZACIÓN
# ============================================================

def limpiar_caracteres(valor):

    if pd.isna(valor):

        return valor


    valor = str(valor)


    reemplazos = {

        "¤": "ñ",
        "¥": "Ñ",
        "Ã±": "ñ",
        "Ã‘": "Ñ",
        "–": "-",
        "—": "-"

    }


    for viejo, nuevo in reemplazos.items():

        valor = valor.replace(
            viejo,
            nuevo
        )


    return valor



def normalizar_texto(valor):

    if pd.isna(valor):

        return valor


    return (

        str(valor)

        .strip()

        .upper()

    )



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


    # Normalizar nombres columnas

    df = normalizar_columnas(df)



    # Normalizar campos texto

    columnas_texto = (

        df.select_dtypes(
            include="object"
        )
        .columns

    )


    for columna in columnas_texto:


        df[columna] = (

            df[columna]

            .apply(limpiar_caracteres)

            .apply(normalizar_texto)

        )



    # Convertir vacíos a nulos

    df = df.replace(

        r"^\s*$",

        pd.NA,

        regex=True

    )



    # Eliminar duplicados

    registros_inicio = len(df)


    df = df.drop_duplicates()


    registros_fin = len(df)


    print(
        f"Duplicados eliminados: {registros_inicio - registros_fin}"
    )


    return df



# ============================================================
# VARIABLES TEMPORALES
# ============================================================

def agregar_fecha_variables(df):


    df[DATE_COLUMN] = pd.to_datetime(

        df[DATE_COLUMN],

        errors="coerce"

    )


    fechas_invalidas = (

        df[DATE_COLUMN]

        .isna()

        .sum()

    )


    if fechas_invalidas:

        print(
            f"Fechas inválidas encontradas: {fechas_invalidas}"
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
# PROCESO ETL
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


        print(
            f"Leyendo: {archivo.name}"
        )


        df = leer_csv(
            archivo
        )


        validar_columnas(
            df,
            archivo
        )


        # Trazabilidad

        df["ARCHIVO_ORIGEN"] = archivo.name



        dataframes.append(

            (
                archivo.name,
                df
            )

        )



    # Validar que todos tengan misma estructura

    validar_estructura(
        dataframes
    )



    # Consolidar

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



    # Normalización

    consolidado = normalizar_dataset(

        consolidado

    )



    # Variables fecha

    consolidado = agregar_fecha_variables(

        consolidado

    )



    # Exportar

    consolidado.to_csv(

        OUTPUT_FILE,

        sep=CSV_SEPARATOR,

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



# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":

    ejecutar_etl()