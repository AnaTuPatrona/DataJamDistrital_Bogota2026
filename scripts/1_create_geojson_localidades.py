#este script es con el objetivo de hacer una tabla la cual normalice el area de las localidades, junto con el código y el nombre que tienen. Esto con el objetivo de perminirnos omitir la información geografica de los geojson, identificando la zona unicamente por el id/nombre

import pandas as pd
import geopandas as gpd
import os

#sacar los datos del code y nombre de la localidad en base a un dataset de las llamadas del 123
data_nombre_localidades = pd.read_csv('data\llamadas123_dic2025.csv', delimiter=';', encoding='MacRoman', decimal=',')
data_localidades = (
    data_nombre_localidades[['CODIGO_LOCALIDAD', 'LOCALIDAD']]
    .rename(columns=str.lower) #volver columnas en minusculas
    .copy()
)
data_localidades = data_localidades.drop_duplicates() #mantener solo elementos únicos
data_localidades = data_localidades[data_localidades['localidad'] != 'SIN_D'] #quitar del dataframe el elemento que es "SIN_D", ya que ese no figura en el mapa
data_localidades['codigo_localidad']=data_localidades['codigo_localidad'].astype(int) #solo por si acaso el tipo de dato de codigo_localidad NO es int, se convierte a int
data_localidades['localidad'] = data_localidades['localidad'].str.title() #para hacer que dejen de estar todas las letras en mayusculas

data_localidades.loc[len(data_localidades)] = { #añade a Sumapaz, que no está por defecto
    'codigo_localidad': 20,
    'localidad': 'Sumapaz'
}

print(data_localidades.head())

#sacar los datos del code y poligono de las localidades en base a un dataset de duplas
mapa_localidades=gpd.read_file('data\duplas_062025.geojson')
poligono_localidades=(
    mapa_localidades[['Localidad', 'Shape_Leng', 'Shape_Area', 'geometry']]
    .rename(columns={'Localidad': 'codigo_localidad'}) #cambio el nombre acá para poder hacer un left join de manera sencilla
    .copy()    
)
poligono_localidades=poligono_localidades.drop_duplicates(subset='codigo_localidad') #mantener valores únicos en base al code de la localidad
poligono_localidades['codigo_localidad']=poligono_localidades['codigo_localidad'].astype(int) #el codigo de localidad por alguna razón era tipo object, entonces lo cambio a int
print(poligono_localidades.head())


#acá ya se hace el left join de los nombres de las localidades y su poligono en base a codigo_localidad
localidades_geo=poligono_localidades.merge(
    data_localidades,
    on='codigo_localidad',
    how='left'
)

localidades_geo = gpd.GeoDataFrame( #este es para que se mantenga como un geodataframe, que lo necesito para hacer el visual jeje
    localidades_geo,
    geometry='geometry',
    crs=poligono_localidades.crs
)
print(localidades_geo.head())

#exportar resultado como geojson
localidades_geo.to_file('outputs/localidades_con_nombres.geojson', driver='GeoJSON')