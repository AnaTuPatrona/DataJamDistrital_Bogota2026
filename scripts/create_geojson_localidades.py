import pandas as pd
import numpy as np

data_nombre_localidades = pd.read_csv('data\llamadas123_dic2025.csv', delimiter=';', encoding='MacRoman', decimal=',')
data_localidades = (
    data_nombre_localidades[['CODIGO_LOCALIDAD', 'LOCALIDAD']]
    .rename(columns=str.lower)
    .copy()
)
data_localidades = data_localidades.drop_duplicates()
data_localidades = data_localidades[data_localidades['localidad'] != 'SIN_D']
print(data_localidades.head())