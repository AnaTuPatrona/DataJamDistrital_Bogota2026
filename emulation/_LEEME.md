# Datos reales de la Fase 7

Los nueve CSV de esta carpeta fueron sincronizados desde `outputs/` y corresponden a las tablas reales exportadas por `scripts/notebooks/07_exportacion.ipynb`.

Las cifras sí son resultados del análisis. Para el tablero, use estas tablas como fuentes de datos y el GeoJSON real `outputs/localidades_bogota.geojson`.

---

## Contenido

Los archivos contienen las filas territoriales y analíticas completas generadas por la Fase 7. La documentación metodológica está en `docs/supuestos.md`.

| Archivo | Corresponde a |
|---|---|
| `dim_localidad.csv` | T1 — dimensión maestra |
| `fact_indicadores_localidad.csv` | T2 — indicadores por localidad |
| `fact_series_trimestral.csv` | T3 — series por corte |
| `fact_encuesta_desagregada.csv` | T4 — desagregaciones |
| `fact_bienal_items.csv` | T5 — ítems normativos |
| `fact_modelo_coeficientes.csv` | T6 — coeficientes de los modelos |
| `fact_llamadas123_agregado.csv` | T7 — llamadas 123 |
| `dim_parametros_ina.csv` | T10 — escenarios del INA |
| `dim_glosario.csv` | T9 — glosario y tooltips |

El geojson no se replica: use `outputs/localidades_con_nombres.geojson`, que ya trae `codigo_localidad` y `localidad`.

## Localidades

| Código | Localidad | Para qué sirve |
|---|---|---|
| 19 | Ciudad Bolívar | Caso crítico: INA 87,3 · cuadrante *Demanda desatendida* · Δ ranking **+6** |
| 11 | Suba | Población grande, bien cubierta: cuadrante *Zona de captura* · Δ ranking +1 |
| 17 | La Candelaria | **`publicable = 0`** (CV 0,341) · intervalos anchos · Δ ranking **−4** |

Ciudad Bolívar y La Candelaria tienen Δ de signo opuesto, así que el gráfico de pendiente muestra cruce.

## Diferencia con el esquema del plan

`fact_modelo_coeficientes.csv` separa los modelos M1–M3 y deja vacíos los campos de odds ratio cuando no aplican.

M1 y M3 son modelos lineales, mientras M2 es logístico. Por tanto, el odds ratio solo aplica a M2; los gráficos deben usar referencia 0 para efectos lineales y referencia 1 para OR.

## Notas técnicas

- Codificación **UTF-8 con BOM** en las exportaciones de la Fase 7 para conservar las tildes.
- Separador coma en todos los archivos. Ojo: `outputs/llamadas123_consolidado_limpio.csv` usa punto y coma.
- Decimales con punto.
- `publicable`, `en_encuesta` y `significativo` son enteros 0/1: conviértalos a dimensión en Tableau o los sumará.
- Las celdas vacías son nulos reales, no cadenas vacías.
