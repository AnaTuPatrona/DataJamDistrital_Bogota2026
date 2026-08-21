# ⚠️ DATOS SINTÉTICOS — NO USAR EN LA ENTREGA

Los nueve CSV de esta carpeta son **inventados**. Existen solo para maquetar el tablero de Tableau mientras el análisis real está en curso.

**Ninguna cifra de aquí es un resultado.** Antes de entregar, repunte todas las fuentes del libro a `outputs/tableau/` y verifique que las tarjetas coincidan con el notebook (V-12 en `docs/supuestos.md`).

---

## Contenido

Todos los archivos tienen **3 registros**, encabezado aparte. Los nombres de columna son exactamente los del esquema T1–T10 del plan analítico, de modo que al cambiar la fuente a los datos reales el libro no debería romperse.

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

## Qué hacer cuando el esqueleto ya funcione

Con 3 registros por archivo hay cuatro cosas que **no** se pueden probar todavía. Cuando el tablero ya tenga forma, extienda a mano:

**1 · Localidad sin encuesta.** Pegue esta fila al final de `dim_localidad.csv`:

```
20,Sumapaz,No aplica,1788,0,0
```

y esta en `fact_indicadores_localidad.csv`:

```
20,,,,,,,,,,,,,,,,,,,38,2125.3,3,167.8,12.67,,7,,,,,,,0,,0
```

Es el caso que más rompe tableros: debe verse en el mapa con patrón o gris y tooltip explicativo, **nunca como cero**.

**2 · Series temporales.** `fact_series_trimestral.csv` trae una sola combinación (Ciudad Bolívar, Línea Púrpura, 3 cortes). Duplique las filas cambiando `codigo_localidad` e `indicador` para probar los pequeños múltiplos y el filtro de indicador.

**3 · Escenarios del INA.** `dim_parametros_ina.csv` solo tiene *Equilibrado*. Al seleccionar otro escenario en el parámetro, las hojas quedarán vacías — eso es esperado y conviene verlo, porque revela cómo se comporta el tablero sin datos. Para probar el cambio de ranking, duplique el bloque con los otros tres nombres de escenario, alterando `INA_escenario` y `rank_escenario`.

**4 · Mapa de calor normativo.** `fact_bienal_items.csv` tiene un ítem por factor en una sola localidad. Para que el patrón territorial se vea, replique los tres ítems en las localidades 11 y 17.

## Diferencia con el esquema del plan

`fact_modelo_coeficientes.csv` incluye tres columnas que el plan no contemplaba: `tipo` (*lineal* / *logistico*), `variable_dependiente`, y `coeficiente` con sus intervalos, además de `odds_ratio`.

El motivo: M1 y M3 son modelos lineales sobre `IPSJ_C` e `ICG_B`, donde el *odds ratio* no aplica y viene vacío. El *forest plot* debe separar por `tipo` en paneles distintos y usar línea de referencia en **0** para los lineales y en **1** para los logísticos. Las tres filas incluidas cubren los tres casos: lineal significativo, lineal no significativo tras Benjamini-Hochberg, y logístico significativo.

## Notas técnicas

- Codificación **UTF-8 sin BOM**. Si Tableau muestra mal las tildes, reabra y guarde como *UTF-8 con BOM*.
- Separador coma en todos los archivos. Ojo: `outputs/llamadas123_consolidado_limpio.csv` usa punto y coma.
- Decimales con punto.
- `publicable`, `en_encuesta` y `significativo` son enteros 0/1: conviértalos a dimensión en Tableau o los sumará.
- Las celdas vacías son nulos reales, no cadenas vacías.
