#este script es con el objetivo de eliminar la información geografica de los datasets de la secretaría de la mujer (guardada en otro csv que se hace con otro script), así como cambiar la nomenclatura de las columnas para que sean la misma

import pandas as pd
import geopandas as gpd
import os
from pathlib import Path
import warnings

warnings.filterwarnings(
    "ignore",
    category=SyntaxWarning
)
warnings.filterwarnings("ignore")


#IMPORTACIÓN GEOJSON

#delitos sexuales
delitossexuales_062025=gpd.read_file('../data/delitossexuales_062025.geojson')
delitossexuales_092025=gpd.read_file('../data/delitossexuales_092025.geojson')
delitossexuales_122025=gpd.read_file('../data/delitossexuales_122025.geojson')
delitossexuales_032026=gpd.read_file('../data/delitossexuales032026.geojson')

#duplas
duplas_032025=gpd.read_file('../data/duplas_032025.geojson')
duplas_062025=gpd.read_file('../data/duplas_062025.geojson')
duplas_092025=gpd.read_file('../data/duplas_092025.geojson')
duplas_122025=gpd.read_file('../data/duplas122025.geojson')
duplas_032026=gpd.read_file('../data/duplas032026.geojson')

#linea púrpura
lineapurpura_032025=gpd.read_file('../data/lineapurpura_032025.geojson')
lineapurpura_062025=gpd.read_file('../data/lineapurpura_062025.geojson')
lineapurpura_092025=gpd.read_file('../data/lineapurpura_092025.geojson')
lineapurpura_122025=gpd.read_file('../data/lineapurpura122025.geojson')
lineapurpura_032026=gpd.read_file('../data/lineapurpura032026.geojson')

#riesgo feminicidio
riesgofeminicidio_062025=gpd.read_file(Path(r'../data/riesgofeminicidio_062025.geojson'))
riesgofeminicidio_092025=gpd.read_file(Path(r'../data/riesgofeminicidio_092025.geojson'))
riesgofeminicidio_122025=gpd.read_file(Path(r'../data/riesgofeminicidio_122025.geojson'))
riesgofeminicidio_032026=gpd.read_file(Path(r'../data/riesgofeminicidio032026.geojson'))


#NORMALIZAR columna de periodo (para que solo sea tipo datetime64[ms])

#marzo de 2025
duplas_032025["Fecha"] = duplas_032025["Fecha"].dt.tz_localize(None)
lineapurpura_032025["Fecha"] = lineapurpura_032025["Fecha"].dt.tz_localize(None)

#junio 2025
delitossexuales_062025["Fecha"] = delitossexuales_062025["Fecha"].dt.tz_localize(None)
duplas_062025["Fecha"] = duplas_062025["Fecha"].dt.tz_localize(None)
lineapurpura_062025["Fecha"] = lineapurpura_062025["Fecha"].dt.tz_localize(None)
riesgofeminicidio_062025["Fecha"] = riesgofeminicidio_062025["Fecha"].dt.tz_localize(None)

#septiembre 2025
delitossexuales_092025["Fecha"] = delitossexuales_092025["Fecha"].dt.tz_localize(None)
duplas_092025["Fecha"] = duplas_092025["Fecha"].dt.tz_localize(None)
lineapurpura_092025["Fecha"] = lineapurpura_092025["Fecha"].dt.tz_localize(None)
riesgofeminicidio_092025["Fecha"] = riesgofeminicidio_092025["Fecha"].dt.tz_localize(None)

#diciembre 2025
delitossexuales_122025["Fecha"] = delitossexuales_122025["Fecha"].dt.tz_localize(None)
duplas_122025["Fecha"] = duplas_122025["Fecha"].dt.tz_localize(None)
lineapurpura_122025["Fecha"] = lineapurpura_122025["Fecha"].dt.tz_localize(None)
riesgofeminicidio_122025["Fecha"] = riesgofeminicidio_122025["Fecha"].dt.tz_localize(None)

#marzo 2026
delitossexuales_032026["Fecha"] = delitossexuales_032026["Fecha"].dt.tz_localize(None)
duplas_032026["Fecha"] = duplas_032026["Fecha"].dt.tz_localize(None)
lineapurpura_032026["Fecha"] = lineapurpura_032026["Fecha"].dt.tz_localize(None)
riesgofeminicidio_032026["Fecha"] = riesgofeminicidio_032026["Fecha"].dt.tz_localize(None)

#CAMBIAR nombres de las columnas

#delitos sexuales
delitossexuales_062025=(
    delitossexuales_062025[['Localidad', 'TotalDelit', 'PDelitoSex', 'PobMujeres', 'TaDelitoSe', 'Fecha']]
    .rename(columns={'TotalDelit': 'Total', 'PDelitoSex': 'Porcentaje', 'TaDelitoSe': 'Tasa'})
    .copy()    
)

delitossexuales_092025=(
    delitossexuales_092025[['Localidad', 'TotalDelit', 'PDelitoSex', 'PobMujeres', 'TaDelitoSe', 'Fecha']]
    .rename(columns={'TotalDelit': 'Total', 'PDelitoSex': 'Porcentaje', 'TaDelitoSe': 'Tasa'})
    .copy()    
)

delitossexuales_122025=(
    delitossexuales_122025[['Localidad', 'TotalDelitoSexual', 'PDelitoSexual', 'PobMujeres', 'TaDelitoSexual', 'Fecha']]
    .rename(columns={'TotalDelitoSexual': 'Total', 'PDelitoSexual': 'Porcentaje', 'TaDelitoSexual': 'Tasa'})
    .copy()    
)

delitossexuales_032026=(
    delitossexuales_032026[['Localidad', 'TotalDelitoSexual', 'PDelitoSexual', 'PobMujeres', 'TaDelitoSexual', 'Fecha']]
    .rename(columns={'TotalDelitoSexual': 'Total', 'PDelitoSexual': 'Porcentaje', 'TaDelitoSexual': 'Tasa'})
    .copy()    
)

#duplas
duplas_032025=(
    duplas_032025[['Localidad', 'TAtencione', 'TAtencio_1', 'Fecha']]
    .rename(columns={'TAtencione': 'TotalAtenciones' ,'TAtencio_1': 'TotalAtenciones_Publico'})
    .copy()    
)

duplas_062025=(
    duplas_062025[['Localidad', 'TAtencione', 'TAtencio_1', 'Fecha']]
    .rename(columns={'TAtencione': 'TotalAtenciones' ,'TAtencio_1': 'TotalAtenciones_Publico'})
    .copy()    
)

duplas_092025=(
    duplas_092025[['Localidad', 'TAtencione', 'TAtencio_1', 'Fecha']]
    .rename(columns={'TAtencione': 'TotalAtenciones' ,'TAtencio_1': 'TotalAtenciones_Publico'})
    .copy()    
)

duplas_122025=(
    duplas_122025[['Localidad', 'TAtenciones_Duplas', 'TAtenciones_DuplasPublico', 'Fecha']]
    .rename(columns={'TAtenciones_Duplas': 'TotalAtenciones' ,'TAtenciones_DuplasPublico': 'TotalAtenciones_Publico'})
    .copy()    
)

duplas_032026=(
    duplas_032026[['Localidad', 'TAtenciones_Duplas', 'TAtenciones_DuplasPublico', 'Fecha']]
    .rename(columns={'TAtenciones_Duplas': 'TotalAtenciones' ,'TAtenciones_DuplasPublico': 'TotalAtenciones_Publico'})
    .copy()    
)

#linea púrpura
lineapurpura_032025=(
    lineapurpura_032025[['Localidad', 'TAtencione', 'Fecha']]
    .rename(columns={'TAtencione': 'TotalAtenciones'})
    .copy()    
)

lineapurpura_062025=(
    lineapurpura_062025[['Localidad', 'TAtencione', 'Fecha']]
    .rename(columns={'TAtencione': 'TotalAtenciones'})
    .copy()    
)

lineapurpura_092025=(
    lineapurpura_092025[['Localidad', 'TAtencione', 'Fecha']]
    .rename(columns={'TAtencione': 'TotalAtenciones'})
    .copy()    
)

lineapurpura_122025=(
    lineapurpura_122025[['Localidad', 'TAtenciones_LPD', 'Fecha']]
    .rename(columns={'TAtenciones_LPD': 'TotalAtenciones'})
    .copy()
)

lineapurpura_032026=(
    lineapurpura_032026[['Localidad', 'TAtenciones_LPD', 'Fecha']]
    .rename(columns={'TAtenciones_LPD': 'TotalAtenciones'})
    .copy()
)

#riesgo de feminicidio
riesgofeminicidio_062025=(
    riesgofeminicidio_062025[['Localidad', 'TRiesgoFem', 'PRiesgoFem', 'PobMujeres', 'TaRiesgoFe', 'Fecha']]
    .rename(columns={'TRiesgoFem': 'Total', 'PRiesgoFem': 'Porcentaje', 'TaRiesgoFe': 'Tasa'})
    .copy()    
)

riesgofeminicidio_092025=(
    riesgofeminicidio_092025[['Localidad', 'TRiesgoFem', 'PRiesgoFem', 'PobMujeres', 'TaRiesgoFe', 'Fecha']]
    .rename(columns={'TRiesgoFem': 'Total', 'PRiesgoFem': 'Porcentaje', 'TaRiesgoFe': 'Tasa'})
    .copy()    
)

riesgofeminicidio_122025=(
    riesgofeminicidio_122025[['Localidad', 'TRiesgoFeminicidio', 'PRiesgoFeminicidio', 'PobMujeres', 'TaRiesgoFemicidio', 'Fecha']]
    .rename(columns={'TRiesgoFeminicidio': 'Total', 'PRiesgoFeminicidio': 'Porcentaje', 'TaRiesgoFemicidio': 'Tasa'})
    .copy()    
)

riesgofeminicidio_032026=(
    riesgofeminicidio_032026[['Localidad', 'TRiesgoFeminicidio', 'PRiesgoFeminicidio', 'PobMujeres', 'TaRiesgoFemicidio', 'Fecha']]
    .rename(columns={'TRiesgoFeminicidio': 'Total', 'PRiesgoFeminicidio': 'Porcentaje', 'TaRiesgoFemicidio': 'Tasa'})
    .copy()    
)

#UNIR los dataframes

#delitos sexuales
delitossexuales=pd.concat([delitossexuales_062025, delitossexuales_092025, delitossexuales_122025, delitossexuales_032026], ignore_index=True)

#duplas
duplas=pd.concat([duplas_032025, duplas_062025, duplas_092025, duplas_122025, duplas_032026], ignore_index=True)

#linea púrpura
lineapurpura=pd.concat([lineapurpura_032025, lineapurpura_062025, lineapurpura_092025, lineapurpura_122025, lineapurpura_032026], ignore_index=True)

#riesgo de feminicidio
riesgofeminicidio=pd.concat([riesgofeminicidio_062025, riesgofeminicidio_092025, riesgofeminicidio_122025, riesgofeminicidio_032026], ignore_index=True)


#CAMBIAR EL CODIGO DE LOCALIDAD POR EL NOMBRE

#hacer un diccionario de localidades en base al archivo localidades_con_nombres.geojson
gdf_localidades = gpd.read_file('../outputs/localidades_con_nombres.geojson')
mapa_codigos = dict(zip(gdf_localidades['codigo_localidad'], gdf_localidades['localidad'])) #el mapa de códigos, ahí la variable es bastante explicita

#cambiar el tipo de dato de Localidad de object a int y mapear
delitossexuales['Localidad']=delitossexuales['Localidad'].astype('int').map(mapa_codigos)
duplas['Localidad']=duplas['Localidad'].astype('int').map(mapa_codigos)
lineapurpura['Localidad']=lineapurpura['Localidad'].astype('int').map(mapa_codigos)
riesgofeminicidio['Localidad']=riesgofeminicidio['Localidad'].astype('int').map(mapa_codigos)

#ver resultado para ver si la embarré en algo o k
print(delitossexuales)
print(duplas)
print(lineapurpura)
print(riesgofeminicidio)

#GUARDAR EN OUTPUTS
delitossexuales.to_csv('../outputs/delitossexuales.csv', index=False)
duplas.to_csv('../outputs/duplas.csv', index=False)
lineapurpura.to_csv('../outputs/lineapurpura.csv', index=False)
riesgofeminicidio.to_csv('../outputs/riesgofeminicidio.csv', index=False)

