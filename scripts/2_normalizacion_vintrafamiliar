#LOS DATOS ESTÁN BIEN, SOLO VOY A CAMBIARLE EL NOMBRE A LAS COLUMNAS

import pandas as pd

data_vintrafamiliar=pd.read_csv('data\osb_saludmental-vintrafamiliar.csv', delimiter=',', encoding='UTF-8-SIG')
data_vintrafamiliar=(
    data_vintrafamiliar.rename(columns={'grupoedad': 'grupoEdad', 'NOMBRE_LOCALIDAD': 'localidad', 'NOMBREUPZ': 'nombreUPZ', 'tipoaseguramiento': 'tipoAseguramiento', 'entidadadministradora': 'entidadAdministradora', 'relacion_agresor': 'relacionAgresor', 'orientacion_sexual': 'orientacionSexual', 'pais_procedencia': 'paisProcedencia', 'ciclo_vital': 'cicloVital', 'estado_civil': 'estadoCivil', 'nivel_educativo': 'nivelEducativo', 'agresor_consumospa': 'agresorConsumoSPA', 'victima_consumospa': 'victimaConsumoSPA', 'lugocurrenciaemocional': 'lugarOcurrenciaEmocional', 'lugocurrenciafisica': 'lugarOcurrenciaFisica', 'lugocurrenciasexual': 'lugarOcurrenciaSexual', 'lugocurrenciaeconomica': 'lugarOcurrenciaEconomica', 'lugocurrencianegligencia': 'lugarOcurrenciaNegligencia', 'lugocurrenciaabandono': 'lugarOcurrenciaAbandono'})
    .copy()    
)

data_vintrafamiliar.to_csv('outputs/osb_saludmental-vintrafamiliar.csv', index=False)