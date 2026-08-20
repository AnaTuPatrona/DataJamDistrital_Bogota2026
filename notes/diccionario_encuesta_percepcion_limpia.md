# Diccionario de datos — `Encuesta_percepcion_limpia_v3.csv`

Encuesta Distrital de Percepción y Cultura Ciudadana — Bogotá  
Eje temático: **Violencia contra la mujer**

- Total de registros (personas encuestadas): **13082**
- Total de variables: **81**
- Fuente del texto de preguntas y opciones: `20260331_diccionario_base_ano_movil_2025.xlsx` (hoja *Diccionario de datos*)
- Fuente de los resultados/conteos: `Encuesta_percepcion_limpia_v3.csv`

## Historial de cambios

- **`codigo_localidad`** (antes `Cod_Locali`): se conserva como llave numérica de cruce (1–19) contra `localidades_con_nombres.geojson` y registros administrativos.
- **`codigo_UPL`** (antes `Cod_UPL`, nueva en esta versión): se conserva como llave alfanumérica de cruce (ej. `UPL20`), en vez de eliminarse. 30 valores únicos, 0 nulos.
- **`A3`, `A4`, `A5`**: tamaño del hogar, menores y mayores de 18. Validado `A3 = A4 + A5` en el 100% de registros.
- **`Ax401`**: filtro maestro de victimización. Verificado: los 11,094 `NaN` de `Jx402` coinciden exactamente con `Ax401 = 2` (No víctima) — un `NaN` en `Jx402` es "no aplica", no falta de respuesta.
- **`Jx402` / `Jx403` (etiqueta corregida):** `Jx402` = ¿fue víctima de violencia intrafamiliar?; `Jx403` = de quienes respondieron Sí en Jx402, ¿denunció ese delito? No se refieren a periodos de tiempo distintos.

## Cómo buscar un resultado específico

1. Ubica el **ID de la variable** en el [Índice de secciones](#índice-de-secciones), o busca (`Ctrl+F`) por el texto de la pregunta.
2. Cada variable muestra:
   - **Pregunta**: el texto exacto tal como se hizo en la encuesta.
   - **Opciones de respuesta**: el código numérico y su etiqueta (ej. `1. Hombre`, `2. Mujer`).
   - **Resultados**: cuántas personas (y qué porcentaje del total) respondieron cada opción, calculado directamente sobre `Encuesta_percepcion_limpia_v3.csv`.
3. Para replicar cualquier resultado en Python:
```python
import pandas as pd
df = pd.read_csv('Encuesta_percepcion_limpia_v3.csv')
df['ID_DE_LA_VARIABLE'].value_counts(dropna=False, normalize=False)
```
4. Para ver resultados en porcentaje directamente:
```python
df['ID_DE_LA_VARIABLE'].value_counts(dropna=False, normalize=True) * 100
```
5. Para cruzar una variable por localidad, UPL o fecha:
```python
df.groupby('Localidad')['ID_DE_LA_VARIABLE'].value_counts(normalize=True)
df.groupby('codigo_UPL')['ID_DE_LA_VARIABLE'].mean()
df.groupby('Fecha')['ID_DE_LA_VARIABLE'].mean()   # útil para indicadores numéricos continuos
```
6. Para filtrar correctamente `Jx402` usando el filtro maestro `Ax401`:
```python
df_con_delito = df[df['Ax401'] == 1]
df_con_delito['Jx402'].value_counts(dropna=False)
```

## Índice de secciones

- [Geografía y tiempo](#geografia-y-tiempo)
- [Composición del hogar](#composicion-del-hogar)
- [Perfil sociodemográfico](#perfil-sociodemografico)
- [Roles de género y distribución de tareas domésticas](#roles-de-genero-y-distribucion-de-tareas-domesticas)
- [Victimización: filtro maestro y violencia intrafamiliar](#victimizacion:-filtro-maestro-y-violencia-intrafamiliar)
- [Acoso sexual, violencia intrafamiliar y contra la mujer (presenciados por lugar)](#acoso-sexual-violencia-intrafamiliar-y-contra-la-mujer-presenciados-por-lugar)
- [Percepción de seguridad](#percepcion-de-seguridad)
- [Inclusión, diversidad y confianza ciudadana](#inclusion-diversidad-y-confianza-ciudadana)
- [Salud mental (escala GAD-7)](#salud-mental-escala-gad-7)
- [Factores de expansión](#factores-de-expansion)

## Geografía y tiempo

### `Fecha`
**Pregunta:** Año y mes según el periodo de recolección de cada una de las encuestas.

**Tipo:** entrada libre / geográfica. Las opciones mostradas son los valores reales que existen en la base.

**Opciones de respuesta (valores reales encontrados):**
  - 2025-01-01
  - 2025-02-01
  - 2025-03-01
  - 2025-04-01
  - 2025-05-01
  - 2025-06-01
  - 2025-07-01
  - 2025-08-01
  - 2025-09-01
  - 2025-10-01
  - 2025-11-01
  - 2025-12-01

**Resultados (base limpia, n=13082):**
  - **2025-01-01** → 742 respuestas (5.7%)
  - **2025-02-01** → 697 respuestas (5.3%)
  - **2025-03-01** → 1265 respuestas (9.7%)
  - **2025-04-01** → 1647 respuestas (12.6%)
  - **2025-05-01** → 1142 respuestas (8.7%)
  - **2025-06-01** → 1084 respuestas (8.3%)
  - **2025-07-01** → 1083 respuestas (8.3%)
  - **2025-08-01** → 1084 respuestas (8.3%)
  - **2025-09-01** → 1083 respuestas (8.3%)
  - **2025-10-01** → 1083 respuestas (8.3%)
  - **2025-11-01** → 1086 respuestas (8.3%)
  - **2025-12-01** → 1086 respuestas (8.3%)

### `SectorUPL`
**Pregunta:** Sector UPL correspondiente a donde fue realizada la encuesta.

**Tipo:** entrada libre / geográfica. Las opciones mostradas son los valores reales que existen en la base.

**Opciones de respuesta (valores reales encontrados):**
  - Sector Centro Ampliado
  - Sector Noroccidente
  - Sector Norte
  - Sector Occidente
  - Sector Sur Occidente
  - Sector Sur Oriente

**Resultados (base limpia, n=13082):**
  - **Sector Centro Ampliado** → 2538 respuestas (19.4%)
  - **Sector Noroccidente** → 1127 respuestas (8.6%)
  - **Sector Norte** → 1509 respuestas (11.5%)
  - **Sector Occidente** → 1886 respuestas (14.4%)
  - **Sector Sur Occidente** → 2987 respuestas (22.8%)
  - **Sector Sur Oriente** → 3035 respuestas (23.2%)

### `Localidad`
**Pregunta:** Nombre de la localidad correspondiente a donde fue realizada la encuesta.

**Tipo:** entrada libre / geográfica. Las opciones mostradas son los valores reales que existen en la base.

**Opciones de respuesta (valores reales encontrados):**
  - Antonio Nariño
  - Barrios Unidos
  - Bosa
  - Chapinero
  - Ciudad Bolívar
  - Engativá
  - Fontibón
  - Kennedy
  - La Candelaria
  - Los Mártires
  - Puente Aranda
  - Rafael Uribe Uribe
  - San Cristóbal
  - Santa Fe
  - Suba
  - Teusaquillo
  - Tunjuelito
  - Usaquén
  - Usme

**Resultados (base limpia, n=13082):**
  - **Antonio Nariño** → 246 respuestas (1.9%)
  - **Barrios Unidos** → 270 respuestas (2.1%)
  - **Bosa** → 1250 respuestas (9.6%)
  - **Chapinero** → 296 respuestas (2.3%)
  - **Ciudad Bolívar** → 858 respuestas (6.6%)
  - **Engativá** → 1232 respuestas (9.4%)
  - **Fontibón** → 654 respuestas (5.0%)
  - **Kennedy** → 1737 respuestas (13.3%)
  - **La Candelaria** → 151 respuestas (1.2%)
  - **Los Mártires** → 239 respuestas (1.8%)
  - **Puente Aranda** → 378 respuestas (2.9%)
  - **Rafael Uribe Uribe** → 716 respuestas (5.5%)
  - **San Cristóbal** → 732 respuestas (5.6%)
  - **Santa Fe** → 300 respuestas (2.3%)
  - **Suba** → 1802 respuestas (13.8%)
  - **Teusaquillo** → 335 respuestas (2.6%)
  - **Tunjuelito** → 308 respuestas (2.4%)
  - **Usaquén** → 834 respuestas (6.4%)
  - **Usme** → 744 respuestas (5.7%)

### `codigo_localidad`
**Pregunta:** Código de la localidad correspondiente a donde fue realizada la encuesta.

**Tipo:** llave de cruce. No se traduce a etiqueta de texto; úsala para validar cruces con otras fuentes administrativas o geoespaciales.

**Valores reales encontrados (19 distintos):**
  - 1
  - 2
  - 3
  - 4
  - 5
  - 6
  - 7
  - 8
  - 9
  - 10
  - 11
  - 12
  - 13
  - 14
  - 15
  - 16
  - 17
  - 18
  - 19

**Resultados (base limpia, n=13082):**
  - **1** → 834 respuestas (6.4%)
  - **2** → 296 respuestas (2.3%)
  - **3** → 300 respuestas (2.3%)
  - **4** → 732 respuestas (5.6%)
  - **5** → 744 respuestas (5.7%)
  - **6** → 308 respuestas (2.4%)
  - **7** → 1250 respuestas (9.6%)
  - **8** → 1737 respuestas (13.3%)
  - **9** → 654 respuestas (5.0%)
  - **10** → 1232 respuestas (9.4%)
  - **11** → 1802 respuestas (13.8%)
  - **12** → 270 respuestas (2.1%)
  - **13** → 335 respuestas (2.6%)
  - **14** → 239 respuestas (1.8%)
  - **15** → 246 respuestas (1.9%)
  - **16** → 378 respuestas (2.9%)
  - **17** → 151 respuestas (1.2%)
  - **18** → 716 respuestas (5.5%)
  - **19** → 858 respuestas (6.6%)

### `Unidad_de_Planeamiento_Local_UPL`
**Pregunta:** Nombre de la UPL correspondiente a donde fue realizada la encuesta.

**Tipo:** entrada libre / geográfica. Las opciones mostradas son los valores reales que existen en la base.

**Opciones de respuesta (valores reales encontrados):**
  - Arborizadora
  - Barrios Unidos
  - Bosa
  - Britalia
  - Centro Histórico
  - Chapinero
  - Edén
  - Engativá
  - Fontibón
  - Kennedy
  - Lucero
  - Niza
  - Patio Bonito
  - Porvenir
  - Puente Aranda
  - Rafael Uribe
  - Restrepo
  - Rincón de Suba
  - Salitre
  - San Cristóbal
  - Suba
  - Tabora
  - Teusaquillo
  - Tibabuyes
  - Tintal
  - Toberín
  - Torca
  - Tunjuelito
  - Usaquén
  - Usme - Entrenubes

**Resultados (base limpia, n=13082):**
  - **Arborizadora** → 482 respuestas (3.7%)
  - **Barrios Unidos** → 270 respuestas (2.1%)
  - **Bosa** → 701 respuestas (5.4%)
  - **Britalia** → 343 respuestas (2.6%)
  - **Centro Histórico** → 690 respuestas (5.3%)
  - **Chapinero** → 296 respuestas (2.3%)
  - **Edén** → 579 respuestas (4.4%)
  - **Engativá** → 527 respuestas (4.0%)
  - **Fontibón** → 365 respuestas (2.8%)
  - **Kennedy** → 592 respuestas (4.5%)
  - **Lucero** → 376 respuestas (2.9%)
  - **Niza** → 332 respuestas (2.5%)
  - **Patio Bonito** → 387 respuestas (3.0%)
  - **Porvenir** → 357 respuestas (2.7%)
  - **Puente Aranda** → 378 respuestas (2.9%)
  - **Rafael Uribe** → 756 respuestas (5.8%)
  - **Restrepo** → 569 respuestas (4.3%)
  - **Rincón de Suba** → 440 respuestas (3.4%)
  - **Salitre** → 494 respuestas (3.8%)
  - **San Cristóbal** → 497 respuestas (3.8%)
  - **Suba** → 313 respuestas (2.4%)
  - **Tabora** → 500 respuestas (3.8%)
  - **Teusaquillo** → 335 respuestas (2.6%)
  - **Tibabuyes** → 374 respuestas (2.9%)
  - **Tintal** → 371 respuestas (2.8%)
  - **Toberín** → 394 respuestas (3.0%)
  - **Torca** → 32 respuestas (0.2%)
  - **Tunjuelito** → 308 respuestas (2.4%)
  - **Usaquén** → 408 respuestas (3.1%)
  - **Usme - Entrenubes** → 616 respuestas (4.7%)

### `codigo_UPL`
**Pregunta:** Código de la UPL correspondiente a donde fue realizada la encuesta.

**Tipo:** llave de cruce. No se traduce a etiqueta de texto; úsala para validar cruces con otras fuentes administrativas o geoespaciales.

**Valores reales encontrados (30 distintos):**
  - UPL03
  - UPL04
  - UPL05
  - UPL07
  - UPL08
  - UPL09
  - UPL10
  - UPL11
  - UPL12
  - UPL13
  - UPL14
  - UPL15
  - UPL16
  - UPL17
  - UPL18
  - UPL19
  - UPL20
  - UPL21
  - UPL22
  - UPL23
  - UPL24
  - UPL25
  - UPL26
  - UPL27
  - UPL28
  - UPL29
  - UPL30
  - UPL31
  - UPL32
  - UPL33

**Resultados (base limpia, n=13082):**
  - **UPL03** → 482 respuestas (3.7%)
  - **UPL04** → 376 respuestas (2.9%)
  - **UPL05** → 616 respuestas (4.7%)
  - **UPL07** → 32 respuestas (0.2%)
  - **UPL08** → 343 respuestas (2.6%)
  - **UPL09** → 313 respuestas (2.4%)
  - **UPL10** → 374 respuestas (2.9%)
  - **UPL11** → 527 respuestas (4.0%)
  - **UPL12** → 365 respuestas (2.8%)
  - **UPL13** → 371 respuestas (2.8%)
  - **UPL14** → 387 respuestas (3.0%)
  - **UPL15** → 357 respuestas (2.7%)
  - **UPL16** → 579 respuestas (4.4%)
  - **UPL17** → 701 respuestas (5.4%)
  - **UPL18** → 592 respuestas (4.5%)
  - **UPL19** → 308 respuestas (2.4%)
  - **UPL20** → 756 respuestas (5.8%)
  - **UPL21** → 497 respuestas (3.8%)
  - **UPL22** → 569 respuestas (4.3%)
  - **UPL23** → 690 respuestas (5.3%)
  - **UPL24** → 296 respuestas (2.3%)
  - **UPL25** → 408 respuestas (3.1%)
  - **UPL26** → 394 respuestas (3.0%)
  - **UPL27** → 332 respuestas (2.5%)
  - **UPL28** → 440 respuestas (3.4%)
  - **UPL29** → 500 respuestas (3.8%)
  - **UPL30** → 494 respuestas (3.8%)
  - **UPL31** → 378 respuestas (2.9%)
  - **UPL32** → 335 respuestas (2.6%)
  - **UPL33** → 270 respuestas (2.1%)

## Composición del hogar

### `A3`
**Pregunta:** 3. ¿Cuántas personas conforman su hogar?

**Tipo:** variable numérica continua. No tiene opciones categóricas fijas.

**Resultados (resumen estadístico):**
  - n válidos: 13082
  - Media: 2.57
  - Mínimo: 1.00
  - Máximo: 12.00
  - Desviación estándar: 1.30
  - Sin dato / NaN: 0

### `A4`
**Pregunta:** 4. ¿Cuántas personas de su hogar tienen menos de 18 años?

**Tipo:** variable numérica continua. No tiene opciones categóricas fijas.

**Resultados (resumen estadístico):**
  - n válidos: 13082
  - Media: 0.54
  - Mínimo: 0.00
  - Máximo: 7.00
  - Desviación estándar: 0.83
  - Sin dato / NaN: 0

### `A5`
**Pregunta:** 5.  ¿Cuántas  personas tienen 18 años cumplidos o más?

**Tipo:** variable numérica continua. No tiene opciones categóricas fijas.

**Resultados (resumen estadístico):**
  - n válidos: 13082
  - Media: 2.03
  - Mínimo: 1.00
  - Máximo: 9.00
  - Desviación estándar: 1.00
  - Sin dato / NaN: 0

## Perfil sociodemográfico

### `A6x2`
**Pregunta:** 2. Parentesco con el jefe del hogar

**Opciones de respuesta:**
  - 1. Cónyuge
  - 2. Hija (o)
  - 3. Nuera /yerno
  - 4. Nieta (o)
  - 5. Padre / madre
  - 6. Suegra (o)
  - 7. Hermana (o)
  - 8. Cuñada (o)
  - 9. Pariente
  - 10. No pariente
  - 11. Hogar unipersonal
  - 0. Jefe del hogar

**Resultados (base limpia, n=13082):**
  - **1. Cónyuge** → 2399 respuestas (18.3%)
  - **2. Hija (o)** → 1343 respuestas (10.3%)
  - **3. Nuera /yerno** → 49 respuestas (0.4%)
  - **4. Nieta (o)** → 85 respuestas (0.6%)
  - **5. Padre / madre** → 346 respuestas (2.6%)
  - **6. Suegra (o)** → 33 respuestas (0.3%)
  - **7. Hermana (o)** → 247 respuestas (1.9%)
  - **8. Cuñada (o)** → 17 respuestas (0.1%)
  - **9. Pariente** → 117 respuestas (0.9%)
  - **10. No pariente** → 62 respuestas (0.5%)
  - **11. Hogar unipersonal** → 0 respuestas (0.0%)
  - **0. Jefe del hogar** → 8384 respuestas (64.1%)

### `A6x3`
**Pregunta:** Edad de la persona.

**Tipo:** variable numérica continua. No tiene opciones categóricas fijas.

**Resultados (resumen estadístico):**
  - n válidos: 13082
  - Media: 49.59
  - Mínimo: 18.00
  - Máximo: 99.00
  - Desviación estándar: 17.83
  - Sin dato / NaN: 0

### `C1`
**Pregunta:** C. ¿Cuál es el nivel educativo más alto que usted ha alcanzado?

**Opciones de respuesta:**
  - 1. Ninguno
  - 2. Primaria
  - 3. Básica secundaria
  - 4. Media
  - 5. Técnica/tecnológica
  - 6. Profesional
  - 7. Postgrado

**Resultados (base limpia, n=13082):**
  - **1. Ninguno** → 240 respuestas (1.8%)
  - **2. Primaria** → 2326 respuestas (17.8%)
  - **3. Básica secundaria** → 1539 respuestas (11.8%)
  - **4. Media** → 3158 respuestas (24.1%)
  - **5. Técnica/tecnológica** → 2372 respuestas (18.1%)
  - **6. Profesional** → 2622 respuestas (20.0%)
  - **7. Postgrado** → 825 respuestas (6.3%)

### `D1`
**Pregunta:** D. Sexo al nacer

**Opciones de respuesta:**
  - 1. Hombre
  - 2. Mujer
  - 3. Intersexual

**Resultados (base limpia, n=13082):**
  - **1. Hombre** → 5618 respuestas (42.9%)
  - **2. Mujer** → 7457 respuestas (57.0%)
  - **3. Intersexual** → 7 respuestas (0.1%)

### `E1`
**Pregunta:** E. ¿Usted se reconoce como?

**Opciones de respuesta:**
  - 1. Hombre
  - 2. Mujer
  - 3. Mujer trans
  - 4. Hombre trans
  - 5. Otro
  - 99. No responde

**Resultados (base limpia, n=13082):**
  - **1. Hombre** → 5283 respuestas (40.4%)
  - **2. Mujer** → 7761 respuestas (59.3%)
  - **3. Mujer trans** → 13 respuestas (0.1%)
  - **4. Hombre trans** → 4 respuestas (0.0%)
  - **5. Otro** → 10 respuestas (0.1%)
  - **99. No responde** → 11 respuestas (0.1%)

### `E1x1`
**Pregunta:** ¿Otra cuál?

**Tipo:** entrada libre / geográfica. Las opciones mostradas son los valores reales que existen en la base.

**Opciones de respuesta (valores reales encontrados):**
  - Fuerte
  - GAY
  - Gay
  - Gey
  - HETEROSEXUAL
  - Homosexual
  - LESBIANA
  - Lesbiana
  - No binario
  - Sin dato / NaN

**Resultados (base limpia, n=13082):**
  - **Fuerte** → 1 respuestas (0.0%)
  - **GAY** → 2 respuestas (0.0%)
  - **Gay** → 1 respuestas (0.0%)
  - **Gey** → 1 respuestas (0.0%)
  - **HETEROSEXUAL** → 1 respuestas (0.0%)
  - **Homosexual** → 1 respuestas (0.0%)
  - **LESBIANA** → 1 respuestas (0.0%)
  - **Lesbiana** → 1 respuestas (0.0%)
  - **No binario** → 1 respuestas (0.0%)
  - **Sin dato / NaN** → 13072 respuestas (99.9%)

### `G1`
**Pregunta:** G. ¿Cuál es su estado civil?

**Opciones de respuesta:**
  - 1. Soltera / o / e
  - 2. Casada / o / e
  - 3. Unión libre (no está casada / o/ e . Y vive en pareja hace dos años o más)
  - 4. No está casada / o / e. Y vive en pareja hace menos de dos años
  - 5. Divorciada / o / e o separada / o / e
  - 6. Viuda / o / e

**Resultados (base limpia, n=13082):**
  - **1. Soltera / o / e** → 4124 respuestas (31.5%)
  - **2. Casada / o / e** → 2711 respuestas (20.7%)
  - **3. Unión libre (no está casada / o/ e . Y vive en pareja hace dos años o más)** → 2812 respuestas (21.5%)
  - **4. No está casada / o / e. Y vive en pareja hace menos de dos años** → 60 respuestas (0.5%)
  - **5. Divorciada / o / e o separada / o / e** → 2150 respuestas (16.4%)
  - **6. Viuda / o / e** → 1225 respuestas (9.4%)

### `H1`
**Pregunta:** H. Según el recibo o servicio de energía eléctrica  ¿cuál es el estrato de esta vivienda?

**Opciones de respuesta:**
  - 1. 1
  - 2. 2
  - 3. 3
  - 4. 4
  - 5. 5
  - 6. 6
  - 7. No tiene servicio
  - 99. No informa

**Resultados (base limpia, n=13082):**
  - **1. 1** → 1327 respuestas (10.1%)
  - **2. 2** → 5355 respuestas (40.9%)
  - **3. 3** → 4540 respuestas (34.7%)
  - **4. 4** → 1448 respuestas (11.1%)
  - **5. 5** → 248 respuestas (1.9%)
  - **6. 6** → 131 respuestas (1.0%)
  - **7. No tiene servicio** → 18 respuestas (0.1%)
  - **99. No informa** → 15 respuestas (0.1%)

### `C303`
**Pregunta:** 303. ¿Usted se considera pobre?

**Opciones de respuesta:**
  - 1. Sí
  - 2. No

**Resultados (base limpia, n=13082):**
  - **1. Sí** → 2241 respuestas (17.1%)
  - **2. No** → 10841 respuestas (82.9%)

### `sexo_jefe`
**Pregunta:** Sexo del jefe de hogar

**Opciones de respuesta:**
  - 1. Hombre
  - 2. Mujer
  - 3. Intersexual

**Resultados (base limpia, n=13082):**
  - **1. Hombre** → 6548 respuestas (50.1%)
  - **2. Mujer** → 6530 respuestas (49.9%)
  - **3. Intersexual** → 4 respuestas (0.0%)

## Roles de género y distribución de tareas domésticas

### `Ax201`
**Pregunta:** a. Limpieza general de la casa

**Opciones de respuesta:**
  - 1. El /la jefe/a de hogar
  - 2. El/la cónyuge o pareja del jefe de hogar
  - 3. Ambos cónyuges o pareja
  - 4. Todos los miembros del hogar
  - 5. Otros miembros del hogar (incluyendo hijos, otros familiares, etc.)
  - 6. Servicio contratado (p.ej., limpieza, niñera)
  - 7. Otro familiar o pariente que ayude con las tareas del hogar pero que no vive en la vivienda
  - 8. No se realiza

**Resultados (base limpia, n=13082):**
  - **1. El /la jefe/a de hogar** → 5214 respuestas (39.9%)
  - **2. El/la cónyuge o pareja del jefe de hogar** → 1381 respuestas (10.6%)
  - **3. Ambos cónyuges o pareja** → 2012 respuestas (15.4%)
  - **4. Todos los miembros del hogar** → 2885 respuestas (22.1%)
  - **5. Otros miembros del hogar (incluyendo hijos, otros familiares, etc.)** → 460 respuestas (3.5%)
  - **6. Servicio contratado (p.ej., limpieza, niñera)** → 944 respuestas (7.2%)
  - **7. Otro familiar o pariente que ayude con las tareas del hogar pero que no vive en la vivienda** → 179 respuestas (1.4%)
  - **8. No se realiza** → 7 respuestas (0.1%)

### `Bx201`
**Pregunta:** b. Mantenimiento y reparaciones del hogar

**Opciones de respuesta:**
  - 1. El /la jefe/a de hogar
  - 2. El/la cónyuge o pareja del jefe de hogar
  - 3. Ambos cónyuges o pareja
  - 4. Todos los miembros del hogar
  - 5. Otros miembros del hogar (incluyendo hijos, otros familiares, etc.)
  - 6. Servicio contratado (p.ej., limpieza, niñera)
  - 7. Otro familiar o pariente que ayude con las tareas del hogar pero que no vive en la vivienda
  - 8. No se realiza

**Resultados (base limpia, n=13082):**
  - **1. El /la jefe/a de hogar** → 4999 respuestas (38.2%)
  - **2. El/la cónyuge o pareja del jefe de hogar** → 745 respuestas (5.7%)
  - **3. Ambos cónyuges o pareja** → 950 respuestas (7.3%)
  - **4. Todos los miembros del hogar** → 1381 respuestas (10.6%)
  - **5. Otros miembros del hogar (incluyendo hijos, otros familiares, etc.)** → 433 respuestas (3.3%)
  - **6. Servicio contratado (p.ej., limpieza, niñera)** → 3200 respuestas (24.5%)
  - **7. Otro familiar o pariente que ayude con las tareas del hogar pero que no vive en la vivienda** → 592 respuestas (4.5%)
  - **8. No se realiza** → 782 respuestas (6.0%)

### `Cx201`
**Pregunta:** c. Lavado de ropa

**Opciones de respuesta:**
  - 1. El /la jefe/a de hogar
  - 2. El/la cónyuge o pareja del jefe de hogar
  - 3. Ambos cónyuges o pareja
  - 4. Todos los miembros del hogar
  - 5. Otros miembros del hogar (incluyendo hijos, otros familiares, etc.)
  - 6. Servicio contratado (p.ej., limpieza, niñera)
  - 7. Otro familiar o pariente que ayude con las tareas del hogar pero que no vive en la vivienda
  - 8. No se realiza

**Resultados (base limpia, n=13082):**
  - **1. El /la jefe/a de hogar** → 5378 respuestas (41.1%)
  - **2. El/la cónyuge o pareja del jefe de hogar** → 1730 respuestas (13.2%)
  - **3. Ambos cónyuges o pareja** → 1850 respuestas (14.1%)
  - **4. Todos los miembros del hogar** → 2813 respuestas (21.5%)
  - **5. Otros miembros del hogar (incluyendo hijos, otros familiares, etc.)** → 413 respuestas (3.2%)
  - **6. Servicio contratado (p.ej., limpieza, niñera)** → 711 respuestas (5.4%)
  - **7. Otro familiar o pariente que ayude con las tareas del hogar pero que no vive en la vivienda** → 160 respuestas (1.2%)
  - **8. No se realiza** → 27 respuestas (0.2%)

### `Dx201`
**Pregunta:** d. Planchar

**Opciones de respuesta:**
  - 1. El /la jefe/a de hogar
  - 2. El/la cónyuge o pareja del jefe de hogar
  - 3. Ambos cónyuges o pareja
  - 4. Todos los miembros del hogar
  - 5. Otros miembros del hogar (incluyendo hijos, otros familiares, etc.)
  - 6. Servicio contratado (p.ej., limpieza, niñera)
  - 7. Otro familiar o pariente que ayude con las tareas del hogar pero que no vive en la vivienda
  - 8. No se realiza

**Resultados (base limpia, n=13082):**
  - **1. El /la jefe/a de hogar** → 2067 respuestas (15.8%)
  - **2. El/la cónyuge o pareja del jefe de hogar** → 787 respuestas (6.0%)
  - **3. Ambos cónyuges o pareja** → 640 respuestas (4.9%)
  - **4. Todos los miembros del hogar** → 984 respuestas (7.5%)
  - **5. Otros miembros del hogar (incluyendo hijos, otros familiares, etc.)** → 197 respuestas (1.5%)
  - **6. Servicio contratado (p.ej., limpieza, niñera)** → 681 respuestas (5.2%)
  - **7. Otro familiar o pariente que ayude con las tareas del hogar pero que no vive en la vivienda** → 89 respuestas (0.7%)
  - **8. No se realiza** → 7637 respuestas (58.4%)

### `Ex201`
**Pregunta:** e. Cocinar

**Opciones de respuesta:**
  - 1. El /la jefe/a de hogar
  - 2. El/la cónyuge o pareja del jefe de hogar
  - 3. Ambos cónyuges o pareja
  - 4. Todos los miembros del hogar
  - 5. Otros miembros del hogar (incluyendo hijos, otros familiares, etc.)
  - 6. Servicio contratado (p.ej., limpieza, niñera)
  - 7. Otro familiar o pariente que ayude con las tareas del hogar pero que no vive en la vivienda
  - 8. No se realiza

**Resultados (base limpia, n=13082):**
  - **1. El /la jefe/a de hogar** → 5737 respuestas (43.9%)
  - **2. El/la cónyuge o pareja del jefe de hogar** → 1727 respuestas (13.2%)
  - **3. Ambos cónyuges o pareja** → 2040 respuestas (15.6%)
  - **4. Todos los miembros del hogar** → 2292 respuestas (17.5%)
  - **5. Otros miembros del hogar (incluyendo hijos, otros familiares, etc.)** → 473 respuestas (3.6%)
  - **6. Servicio contratado (p.ej., limpieza, niñera)** → 507 respuestas (3.9%)
  - **7. Otro familiar o pariente que ayude con las tareas del hogar pero que no vive en la vivienda** → 164 respuestas (1.3%)
  - **8. No se realiza** → 142 respuestas (1.1%)

### `Fx201`
**Pregunta:** f. Compras del supermercado

**Opciones de respuesta:**
  - 1. El /la jefe/a de hogar
  - 2. El/la cónyuge o pareja del jefe de hogar
  - 3. Ambos cónyuges o pareja
  - 4. Todos los miembros del hogar
  - 5. Otros miembros del hogar (incluyendo hijos, otros familiares, etc.)
  - 6. Servicio contratado (p.ej., limpieza, niñera)
  - 7. Otro familiar o pariente que ayude con las tareas del hogar pero que no vive en la vivienda
  - 8. No se realiza

**Resultados (base limpia, n=13082):**
  - **1. El /la jefe/a de hogar** → 5471 respuestas (41.8%)
  - **2. El/la cónyuge o pareja del jefe de hogar** → 627 respuestas (4.8%)
  - **3. Ambos cónyuges o pareja** → 3338 respuestas (25.5%)
  - **4. Todos los miembros del hogar** → 2823 respuestas (21.6%)
  - **5. Otros miembros del hogar (incluyendo hijos, otros familiares, etc.)** → 440 respuestas (3.4%)
  - **6. Servicio contratado (p.ej., limpieza, niñera)** → 112 respuestas (0.9%)
  - **7. Otro familiar o pariente que ayude con las tareas del hogar pero que no vive en la vivienda** → 203 respuestas (1.6%)
  - **8. No se realiza** → 68 respuestas (0.5%)

### `Gx201`
**Pregunta:** g. Pago de facturas y Planear/hacer el presupuesto del hogar

**Opciones de respuesta:**
  - 1. El /la jefe/a de hogar
  - 2. El/la cónyuge o pareja del jefe de hogar
  - 3. Ambos cónyuges o pareja
  - 4. Todos los miembros del hogar
  - 5. Otros miembros del hogar (incluyendo hijos, otros familiares, etc.)
  - 6. Servicio contratado (p.ej., limpieza, niñera)
  - 7. Otro familiar o pariente que ayude con las tareas del hogar pero que no vive en la vivienda
  - 8. No se realiza

**Resultados (base limpia, n=13082):**
  - **1. El /la jefe/a de hogar** → 6231 respuestas (47.6%)
  - **2. El/la cónyuge o pareja del jefe de hogar** → 623 respuestas (4.8%)
  - **3. Ambos cónyuges o pareja** → 2921 respuestas (22.3%)
  - **4. Todos los miembros del hogar** → 2395 respuestas (18.3%)
  - **5. Otros miembros del hogar (incluyendo hijos, otros familiares, etc.)** → 498 respuestas (3.8%)
  - **6. Servicio contratado (p.ej., limpieza, niñera)** → 77 respuestas (0.6%)
  - **7. Otro familiar o pariente que ayude con las tareas del hogar pero que no vive en la vivienda** → 265 respuestas (2.0%)
  - **8. No se realiza** → 72 respuestas (0.6%)

### `Hx201`
**Pregunta:** h. Cuidado de los niños

**Opciones de respuesta:**
  - 1. El /la jefe/a de hogar
  - 2. El/la cónyuge o pareja del jefe de hogar
  - 3. Ambos cónyuges o pareja
  - 4. Todos los miembros del hogar
  - 5. Otros miembros del hogar (incluyendo hijos, otros familiares, etc.)
  - 6. Servicio contratado (p.ej., limpieza, niñera)
  - 7. Otro familiar o pariente que ayude con las tareas del hogar pero que no vive en la vivienda
  - 8. No se realiza

**Resultados (base limpia, n=13082):**
  - **1. El /la jefe/a de hogar** → 1373 respuestas (10.5%)
  - **2. El/la cónyuge o pareja del jefe de hogar** → 414 respuestas (3.2%)
  - **3. Ambos cónyuges o pareja** → 1151 respuestas (8.8%)
  - **4. Todos los miembros del hogar** → 684 respuestas (5.2%)
  - **5. Otros miembros del hogar (incluyendo hijos, otros familiares, etc.)** → 229 respuestas (1.8%)
  - **6. Servicio contratado (p.ej., limpieza, niñera)** → 140 respuestas (1.1%)
  - **7. Otro familiar o pariente que ayude con las tareas del hogar pero que no vive en la vivienda** → 256 respuestas (2.0%)
  - **8. No se realiza** → 571 respuestas (4.4%)
  - **Sin dato / NaN** → 8264 respuestas (63.2%)

### `Ix201`
**Pregunta:** i. Ayuda con las tareas escolares de los niños

**Opciones de respuesta:**
  - 1. El /la jefe/a de hogar
  - 2. El/la cónyuge o pareja del jefe de hogar
  - 3. Ambos cónyuges o pareja
  - 4. Todos los miembros del hogar
  - 5. Otros miembros del hogar (incluyendo hijos, otros familiares, etc.)
  - 6. Servicio contratado (p.ej., limpieza, niñera)
  - 7. Otro familiar o pariente que ayude con las tareas del hogar pero que no vive en la vivienda
  - 8. No se realiza

**Resultados (base limpia, n=13082):**
  - **1. El /la jefe/a de hogar** → 1297 respuestas (9.9%)
  - **2. El/la cónyuge o pareja del jefe de hogar** → 443 respuestas (3.4%)
  - **3. Ambos cónyuges o pareja** → 939 respuestas (7.2%)
  - **4. Todos los miembros del hogar** → 530 respuestas (4.1%)
  - **5. Otros miembros del hogar (incluyendo hijos, otros familiares, etc.)** → 274 respuestas (2.1%)
  - **6. Servicio contratado (p.ej., limpieza, niñera)** → 50 respuestas (0.4%)
  - **7. Otro familiar o pariente que ayude con las tareas del hogar pero que no vive en la vivienda** → 181 respuestas (1.4%)
  - **8. No se realiza** → 1104 respuestas (8.4%)
  - **Sin dato / NaN** → 8264 respuestas (63.2%)

### `Jx201`
**Pregunta:** j. Cuidado de personas mayores o dependientes

**Opciones de respuesta:**
  - 1. El /la jefe/a de hogar
  - 2. El/la cónyuge o pareja del jefe de hogar
  - 3. Ambos cónyuges o pareja
  - 4. Todos los miembros del hogar
  - 5. Otros miembros del hogar (incluyendo hijos, otros familiares, etc.)
  - 6. Servicio contratado (p.ej., limpieza, niñera)
  - 7. Otro familiar o pariente que ayude con las tareas del hogar pero que no vive en la vivienda
  - 8. No se realiza

**Resultados (base limpia, n=13082):**
  - **1. El /la jefe/a de hogar** → 674 respuestas (5.2%)
  - **2. El/la cónyuge o pareja del jefe de hogar** → 109 respuestas (0.8%)
  - **3. Ambos cónyuges o pareja** → 414 respuestas (3.2%)
  - **4. Todos los miembros del hogar** → 616 respuestas (4.7%)
  - **5. Otros miembros del hogar (incluyendo hijos, otros familiares, etc.)** → 422 respuestas (3.2%)
  - **6. Servicio contratado (p.ej., limpieza, niñera)** → 111 respuestas (0.8%)
  - **7. Otro familiar o pariente que ayude con las tareas del hogar pero que no vive en la vivienda** → 338 respuestas (2.6%)
  - **8. No se realiza** → 3029 respuestas (23.2%)
  - **Sin dato / NaN** → 7369 respuestas (56.3%)

### `Ax202`
**Pregunta:** 202. ¿Cómo afecta la anterior distribución de tareas domésticas y de cuidado en el bienestar de su hogar? Por favor elija una de las frases que le voy a leer.

**Opciones de respuesta:**
  - 1. Garantiza el bienestar y la  salud de todos los miembros de la familia.
  - 2. Fomenta la armonía familiar.
  - 3. No tiene una influencia clara en nuestro bienestar.
  - 4. Causa cierto estrés o descontento en algunos miembros de la familia.
  - 5. Genera conflictos serios o mucho estrés entre los miembros de mi hogar.
  - 6. No estoy seguro/a de la influencia en nuestro bienestar.

**Resultados (base limpia, n=13082):**
  - **1. Garantiza el bienestar y la  salud de todos los miembros de la familia.** → 4454 respuestas (34.0%)
  - **2. Fomenta la armonía familiar.** → 6365 respuestas (48.7%)
  - **3. No tiene una influencia clara en nuestro bienestar.** → 1031 respuestas (7.9%)
  - **4. Causa cierto estrés o descontento en algunos miembros de la familia.** → 884 respuestas (6.8%)
  - **5. Genera conflictos serios o mucho estrés entre los miembros de mi hogar.** → 129 respuestas (1.0%)
  - **6. No estoy seguro/a de la influencia en nuestro bienestar.** → 219 respuestas (1.7%)

### `ind_distribuciontareas_202`
**Pregunta:** Impacto de la distribución de tareas domésticas y de cuidado en el bienestar familiar.

**Opciones de respuesta:**
  - 1. Impacto positivo
  - 2. Impacto neutro
  - 3. Impacto negativo

**Resultados (base limpia, n=13082):**
  - **1. Impacto positivo** → 10819 respuestas (82.7%)
  - **2. Impacto neutro** → 1250 respuestas (9.6%)
  - **3. Impacto negativo** → 1013 respuestas (7.7%)

## Victimización: filtro maestro y violencia intrafamiliar

### `Ax401`
**Pregunta:** 401. ¿Durante este año, usted o algún miembro del hogar, ha sido víctima de algún delito en la ciudad de Bogotá?

**Opciones de respuesta:**
  - 1. Sí
  - 2. No

**Resultados (base limpia, n=13082):**
  - **1. Sí** → 1988 respuestas (15.2%)
  - **2. No** → 11094 respuestas (84.8%)

### `Jx402`
**Pregunta:** j. Violencia intrafamiliar (¿fue víctima de este delito?)

**Opciones de respuesta:**
  - 1. Sí
  - 2. No

**Resultados (base limpia, n=13082):**
  - **1. Sí** → 24 respuestas (0.2%)
  - **2. No** → 1964 respuestas (15.0%)
  - **Sin dato / NaN** → 11094 respuestas (84.8%)

### `Jx403`
**Pregunta:** j. Violencia intrafamiliar (¿denunció este delito?)

**Opciones de respuesta:**
  - 1. Sí
  - 2. No

**Resultados (base limpia, n=13082):**
  - **1. Sí** → 17 respuestas (0.1%)
  - **2. No** → 7 respuestas (0.1%)
  - **Sin dato / NaN** → 13058 respuestas (99.8%)

## Acoso sexual, violencia intrafamiliar y contra la mujer (presenciados por lugar)

### `Kx404_1`
**Pregunta:** k. Acoso sexual (Silbidos, comentarios sexuales, etc.) (En su residencia u otra residencia)

**Opciones de respuesta:**
  - 0. No
  - 1. Si

**Resultados (base limpia, n=13082):**
  - **0. No** → 12925 respuestas (98.8%)
  - **1. Si** → 157 respuestas (1.2%)

### `Kx404_2`
**Pregunta:** k. Acoso sexual (Silbidos, comentarios sexuales, etc.) (En la cuadra, conjunto, barrio)

**Opciones de respuesta:**
  - 0. No
  - 1. Si

**Resultados (base limpia, n=13082):**
  - **0. No** → 12356 respuestas (94.5%)
  - **1. Si** → 726 respuestas (5.5%)

### `Kx404_3`
**Pregunta:** k. Acoso sexual (Silbidos, comentarios sexuales, etc.) (En otro espacio público)

**Opciones de respuesta:**
  - 0. No
  - 1. Si

**Resultados (base limpia, n=13082):**
  - **0. No** → 11688 respuestas (89.3%)
  - **1. Si** → 1394 respuestas (10.7%)

### `Kx404_4`
**Pregunta:** k. Acoso sexual (Silbidos, comentarios sexuales, etc.) (En el transporte público)

**Opciones de respuesta:**
  - 0. No
  - 1. Si

**Resultados (base limpia, n=13082):**
  - **0. No** → 11944 respuestas (91.3%)
  - **1. Si** → 1138 respuestas (8.7%)

### `Kx404_5`
**Pregunta:** k. Acoso sexual (Silbidos, comentarios sexuales, etc.) (En el lugar de trabajo)

**Opciones de respuesta:**
  - 0. No
  - 1. Si

**Resultados (base limpia, n=13082):**
  - **0. No** → 12907 respuestas (98.7%)
  - **1. Si** → 175 respuestas (1.3%)

### `Kx404_6`
**Pregunta:** k. Acoso sexual (Silbidos, comentarios sexuales, etc.) (No afrontó la situación)

**Opciones de respuesta:**
  - 0. No
  - 1. Si

**Resultados (base limpia, n=13082):**
  - **0. No** → 2489 respuestas (19.0%)
  - **1. Si** → 10593 respuestas (81.0%)

### `Lx404_1`
**Pregunta:** l. Presenció casos de violencia intrafamiliar (En su residencia u otra residencia)

**Opciones de respuesta:**
  - 0. No
  - 1. Si

**Resultados (base limpia, n=13082):**
  - **0. No** → 12792 respuestas (97.8%)
  - **1. Si** → 290 respuestas (2.2%)

### `Lx404_2`
**Pregunta:** l. Presenció casos de violencia intrafamiliar (En la cuadra, conjunto, barrio)

**Opciones de respuesta:**
  - 0. No
  - 1. Si

**Resultados (base limpia, n=13082):**
  - **0. No** → 11871 respuestas (90.7%)
  - **1. Si** → 1211 respuestas (9.3%)

### `Lx404_3`
**Pregunta:** l. Presenció casos de violencia intrafamiliar (En otro espacio público)

**Opciones de respuesta:**
  - 0. No
  - 1. Si

**Resultados (base limpia, n=13082):**
  - **0. No** → 12078 respuestas (92.3%)
  - **1. Si** → 1004 respuestas (7.7%)

### `Lx404_4`
**Pregunta:** l. Presenció casos de violencia intrafamiliar (En el transporte público)

**Opciones de respuesta:**
  - 0. No
  - 1. Si

**Resultados (base limpia, n=13082):**
  - **0. No** → 12824 respuestas (98.0%)
  - **1. Si** → 258 respuestas (2.0%)

### `Lx404_5`
**Pregunta:** l. Presenció casos de violencia intrafamiliar (En el lugar de trabajo)

**Opciones de respuesta:**
  - 0. No
  - 1. Si

**Resultados (base limpia, n=13082):**
  - **0. No** → 12974 respuestas (99.2%)
  - **1. Si** → 108 respuestas (0.8%)

### `Lx404_6`
**Pregunta:** l. Presenció casos de violencia intrafamiliar (No afrontó la situación)

**Opciones de respuesta:**
  - 0. No
  - 1. Si

**Resultados (base limpia, n=13082):**
  - **0. No** → 2168 respuestas (16.6%)
  - **1. Si** → 10914 respuestas (83.4%)

### `Mx404_1`
**Pregunta:** m. Presenció casos de violencia contra la mujer (En su residencia u otra residencia)

**Opciones de respuesta:**
  - 0. No
  - 1. Si

**Resultados (base limpia, n=13082):**
  - **0. No** → 12797 respuestas (97.8%)
  - **1. Si** → 285 respuestas (2.2%)

### `Mx404_2`
**Pregunta:** m. Presenció casos de violencia contra la mujer (En la cuadra, conjunto, barrio)

**Opciones de respuesta:**
  - 0. No
  - 1. Si

**Resultados (base limpia, n=13082):**
  - **0. No** → 11943 respuestas (91.3%)
  - **1. Si** → 1139 respuestas (8.7%)

### `Mx404_3`
**Pregunta:** m. Presenció casos de violencia contra la mujer (En otro espacio público)

**Opciones de respuesta:**
  - 0. No
  - 1. Si

**Resultados (base limpia, n=13082):**
  - **0. No** → 11843 respuestas (90.5%)
  - **1. Si** → 1239 respuestas (9.5%)

### `Mx404_4`
**Pregunta:** m. Presenció casos de violencia contra la mujer (En el transporte público)

**Opciones de respuesta:**
  - 0. No
  - 1. Si

**Resultados (base limpia, n=13082):**
  - **0. No** → 12677 respuestas (96.9%)
  - **1. Si** → 405 respuestas (3.1%)

### `Mx404_5`
**Pregunta:** m. Presenció casos de violencia contra la mujer (En el lugar de trabajo)

**Opciones de respuesta:**
  - 0. No
  - 1. Si

**Resultados (base limpia, n=13082):**
  - **0. No** → 12933 respuestas (98.9%)
  - **1. Si** → 149 respuestas (1.1%)

### `Mx404_6`
**Pregunta:** m. Presenció casos de violencia contra la mujer (No afrontó la situación)

**Opciones de respuesta:**
  - 0. No
  - 1. Si

**Resultados (base limpia, n=13082):**
  - **0. No** → 2457 respuestas (18.8%)
  - **1. Si** → 10625 respuestas (81.2%)

### `Nx404_1`
**Pregunta:** n. Presenció casos de violencia contra niños, niñas y adolescentes (NNA) (En su residencia u otra residencia)

**Opciones de respuesta:**
  - 0. No
  - 1. Si

**Resultados (base limpia, n=13082):**
  - **0. No** → 12894 respuestas (98.6%)
  - **1. Si** → 188 respuestas (1.4%)

### `Nx404_2`
**Pregunta:** n. Presenció casos de violencia contra niños, niñas y adolescentes (NNA) (En la cuadra, conjunto, barrio)

**Opciones de respuesta:**
  - 0. No
  - 1. Si

**Resultados (base limpia, n=13082):**
  - **0. No** → 12313 respuestas (94.1%)
  - **1. Si** → 769 respuestas (5.9%)

### `Nx404_3`
**Pregunta:** n. Presenció casos de violencia contra niños, niñas y adolescentes (NNA) (En otro espacio público)

**Opciones de respuesta:**
  - 0. No
  - 1. Si

**Resultados (base limpia, n=13082):**
  - **0. No** → 12205 respuestas (93.3%)
  - **1. Si** → 877 respuestas (6.7%)

### `Nx404_4`
**Pregunta:** n. Presenció casos de violencia contra niños, niñas y adolescentes (NNA) (En el transporte público)

**Opciones de respuesta:**
  - 0. No
  - 1. Si

**Resultados (base limpia, n=13082):**
  - **0. No** → 12799 respuestas (97.8%)
  - **1. Si** → 283 respuestas (2.2%)

### `Nx404_5`
**Pregunta:** n. Presenció casos de violencia contra niños, niñas y adolescentes (NNA) (En el lugar de trabajo)

**Opciones de respuesta:**
  - 0. No
  - 1. Si

**Resultados (base limpia, n=13082):**
  - **0. No** → 12950 respuestas (99.0%)
  - **1. Si** → 132 respuestas (1.0%)

### `Nx404_6`
**Pregunta:** n. Presenció casos de violencia contra niños, niñas y adolescentes (NNA) (No afrontó la situación)

**Opciones de respuesta:**
  - 0. No
  - 1. Si

**Resultados (base limpia, n=13082):**
  - **0. No** → 1712 respuestas (13.1%)
  - **1. Si** → 11370 respuestas (86.9%)

## Percepción de seguridad

### `F405`
**Pregunta:** 405. ¿Qué tan seguro se siente usted caminando solo por su barrio de día

**Opciones de respuesta:**
  - 1. Muy inseguro
  - 2. Inseguro/a
  - 3. Ni seguro ni inseguro
  - 4. Seguro/a
  - 5. Muy seguro/a
  - 6. Nunca sale solo/a de día

**Resultados (base limpia, n=13082):**
  - **1. Muy inseguro** → 515 respuestas (3.9%)
  - **2. Inseguro/a** → 2023 respuestas (15.5%)
  - **3. Ni seguro ni inseguro** → 2749 respuestas (21.0%)
  - **4. Seguro/a** → 6829 respuestas (52.2%)
  - **5. Muy seguro/a** → 770 respuestas (5.9%)
  - **6. Nunca sale solo/a de día** → 196 respuestas (1.5%)

### `G406`
**Pregunta:** 406. ¿Qué tan seguro se siente usted caminando solo por su barrio de noche

**Opciones de respuesta:**
  - 1. Muy inseguro
  - 2. Inseguro/a
  - 3. Ni seguro ni inseguro
  - 4. Seguro/a
  - 5. Muy seguro/a
  - 6. Nunca sale solo/a de noche

**Resultados (base limpia, n=13082):**
  - **1. Muy inseguro** → 2222 respuestas (17.0%)
  - **2. Inseguro/a** → 3298 respuestas (25.2%)
  - **3. Ni seguro ni inseguro** → 2233 respuestas (17.1%)
  - **4. Seguro/a** → 2238 respuestas (17.1%)
  - **5. Muy seguro/a** → 264 respuestas (2.0%)
  - **6. Nunca sale solo/a de noche** → 2827 respuestas (21.6%)

### `IPS_dia`
**Pregunta:** Percepción promedio de la seguridad al caminar de día por su barrio.

**Tipo:** variable numérica continua. No tiene opciones categóricas fijas.

**Resultados (resumen estadístico):**
  - n válidos: 12886
  - Media: 3.41
  - Mínimo: 1.00
  - Máximo: 5.00
  - Desviación estándar: 0.96
  - Sin dato / NaN: 196

### `IPS_noche`
**Pregunta:** Percepción promedio de la seguridad al caminar de noche por su barrio.

**Tipo:** variable numérica continua. No tiene opciones categóricas fijas.

**Resultados (resumen estadístico):**
  - n válidos: 10255
  - Media: 2.51
  - Mínimo: 1.00
  - Máximo: 5.00
  - Desviación estándar: 1.13
  - Sin dato / NaN: 2827

### `IPSJ_A`
**Pregunta:** Percepción promedio sobre la rapidez de las autoridades ante incidentes de seguridad que ocurren en el barrio.

**Tipo:** variable numérica continua. No tiene opciones categóricas fijas.

**Resultados (resumen estadístico):**
  - n válidos: 12460
  - Media: 2.58
  - Mínimo: 1.00
  - Máximo: 5.00
  - Desviación estándar: 1.05
  - Sin dato / NaN: 622

### `IPSJ_C`
**Pregunta:** Percepción promedio sobre la disponibilidad y facilidad de acceso a la información y los medios para denunciar delitos.

**Tipo:** variable numérica continua. No tiene opciones categóricas fijas.

**Resultados (resumen estadístico):**
  - n válidos: 11904
  - Media: 2.86
  - Mínimo: 1.00
  - Máximo: 5.00
  - Desviación estándar: 1.08
  - Sin dato / NaN: 1178

### `IPSJ_E`
**Pregunta:** Percepción promedio de la aplicación de justicia sobre quienes cometen delitos.

**Tipo:** variable numérica continua. No tiene opciones categóricas fijas.

**Resultados (resumen estadístico):**
  - n válidos: 12776
  - Media: 2.13
  - Mínimo: 1.00
  - Máximo: 5.00
  - Desviación estándar: 0.87
  - Sin dato / NaN: 306

## Inclusión, diversidad y confianza ciudadana

### `Dx704`
**Pregunta:** d. En la ciudad las personas son incluyentes y respetan la diversidad (cultural, étnica, socioeconómica, orientación sexual, etc.)

**Opciones de respuesta:**
  - 1. Totalmente en desacuerdo
  - 2. En desacuerdo
  - 3. Ni de acuerdo. Ni en desacuerdo
  - 4. De acuerdo
  - 5. Totalmente de acuerdo
  - 99. Ns/Nr

**Resultados (base limpia, n=13082):**
  - **1. Totalmente en desacuerdo** → 811 respuestas (6.2%)
  - **2. En desacuerdo** → 4490 respuestas (34.3%)
  - **3. Ni de acuerdo. Ni en desacuerdo** → 3187 respuestas (24.4%)
  - **4. De acuerdo** → 4176 respuestas (31.9%)
  - **5. Totalmente de acuerdo** → 264 respuestas (2.0%)
  - **99. Ns/Nr** → 154 respuestas (1.2%)

### `ICG_D`
**Pregunta:** Percepción promedio sobre el respeto de los ciudadanos hacia la inclusión y la diversidad.

**Tipo:** variable numérica continua. No tiene opciones categóricas fijas.

**Resultados (resumen estadístico):**
  - n válidos: 12928
  - Media: 2.89
  - Mínimo: 1.00
  - Máximo: 5.00
  - Desviación estándar: 1.00
  - Sin dato / NaN: 154

### `Bx704`
**Pregunta:** b. Confío en que mis vecinos me ayudarían ante cualquier problema o necesidad

**Opciones de respuesta:**
  - 1. Totalmente en desacuerdo
  - 2. En desacuerdo
  - 3. Ni de acuerdo. Ni en desacuerdo
  - 4. De acuerdo
  - 5. Totalmente de acuerdo
  - 99. Ns/Nr

**Resultados (base limpia, n=13082):**
  - **1. Totalmente en desacuerdo** → 970 respuestas (7.4%)
  - **2. En desacuerdo** → 3608 respuestas (27.6%)
  - **3. Ni de acuerdo. Ni en desacuerdo** → 2498 respuestas (19.1%)
  - **4. De acuerdo** → 5110 respuestas (39.1%)
  - **5. Totalmente de acuerdo** → 726 respuestas (5.5%)
  - **99. Ns/Nr** → 170 respuestas (1.3%)

### `ICG_B`
**Pregunta:** Confianza promedio en la ayuda que brindarían los vecinos ante cualquier problema o necesidad.

**Tipo:** variable numérica continua. No tiene opciones categóricas fijas.

**Resultados (resumen estadístico):**
  - n válidos: 12912
  - Media: 3.08
  - Mínimo: 1.00
  - Máximo: 5.00
  - Desviación estándar: 1.09
  - Sin dato / NaN: 170

## Salud mental (escala GAD-7)

### `Ax102`
**Pregunta:** a. ¿Sensación de nerviosismo, de ansiedad, de tener los nervios de punta?

**Opciones de respuesta:**
  - 0. Ningún día
  - 1. Varios días
  - 2. Más de la mitad de los días
  - 3. Casi todos los días

**Resultados (base limpia, n=13082):**
  - **0. Ningún día** → 9420 respuestas (72.0%)
  - **1. Varios días** → 2884 respuestas (22.0%)
  - **2. Más de la mitad de los días** → 406 respuestas (3.1%)
  - **3. Casi todos los días** → 372 respuestas (2.8%)

### `Bx102`
**Pregunta:** b. ¿Incapacidad de evadir o controlar sus preocupaciones?

**Opciones de respuesta:**
  - 0. Ningún día
  - 1. Varios días
  - 2. Más de la mitad de los días
  - 3. Casi todos los días

**Resultados (base limpia, n=13082):**
  - **0. Ningún día** → 10524 respuestas (80.4%)
  - **1. Varios días** → 2040 respuestas (15.6%)
  - **2. Más de la mitad de los días** → 334 respuestas (2.6%)
  - **3. Casi todos los días** → 184 respuestas (1.4%)

### `Cx102`
**Pregunta:** c. ¿Preocupación excesiva por diferentes cosas o situaciones?

**Opciones de respuesta:**
  - 0. Ningún día
  - 1. Varios días
  - 2. Más de la mitad de los días
  - 3. Casi todos los días

**Resultados (base limpia, n=13082):**
  - **0. Ningún día** → 9037 respuestas (69.1%)
  - **1. Varios días** → 3201 respuestas (24.5%)
  - **2. Más de la mitad de los días** → 526 respuestas (4.0%)
  - **3. Casi todos los días** → 318 respuestas (2.4%)

### `Dx102`
**Pregunta:** d. ¿Dificultad para relajarse?

**Opciones de respuesta:**
  - 0. Ningún día
  - 1. Varios días
  - 2. Más de la mitad de los días
  - 3. Casi todos los días

**Resultados (base limpia, n=13082):**
  - **0. Ningún día** → 9989 respuestas (76.4%)
  - **1. Varios días** → 2332 respuestas (17.8%)
  - **2. Más de la mitad de los días** → 484 respuestas (3.7%)
  - **3. Casi todos los días** → 277 respuestas (2.1%)

### `Ex102`
**Pregunta:** e. ¿Tan intranquilo, inquieto o agitado que le resulta difícil quedarse quieto?

**Opciones de respuesta:**
  - 0. Ningún día
  - 1. Varios días
  - 2. Más de la mitad de los días
  - 3. Casi todos los días

**Resultados (base limpia, n=13082):**
  - **0. Ningún día** → 9499 respuestas (72.6%)
  - **1. Varios días** → 2711 respuestas (20.7%)
  - **2. Más de la mitad de los días** → 540 respuestas (4.1%)
  - **3. Casi todos los días** → 332 respuestas (2.5%)

### `Fx102`
**Pregunta:** f. ¿Que se enfada o irrita con facilidad?

**Opciones de respuesta:**
  - 0. Ningún día
  - 1. Varios días
  - 2. Más de la mitad de los días
  - 3. Casi todos los días

**Resultados (base limpia, n=13082):**
  - **0. Ningún día** → 8790 respuestas (67.2%)
  - **1. Varios días** → 3257 respuestas (24.9%)
  - **2. Más de la mitad de los días** → 631 respuestas (4.8%)
  - **3. Casi todos los días** → 404 respuestas (3.1%)

### `Gx102`
**Pregunta:** g. ¿Miedo o susto, como si algo malo pudiera suceder?

**Opciones de respuesta:**
  - 0. Ningún día
  - 1. Varios días
  - 2. Más de la mitad de los días
  - 3. Casi todos los días

**Resultados (base limpia, n=13082):**
  - **0. Ningún día** → 10401 respuestas (79.5%)
  - **1. Varios días** → 2158 respuestas (16.5%)
  - **2. Más de la mitad de los días** → 337 respuestas (2.6%)
  - **3. Casi todos los días** → 186 respuestas (1.4%)

### `A101`
**Pregunta:** 101. ¿Usted considera que su estado de salud actual es …?

**Opciones de respuesta:**
  - 1. Muy malo
  - 2. Malo
  - 3. Regular
  - 4. Bueno
  - 5. Muy bueno
  - 99. Ns/Nr

**Resultados (base limpia, n=13082):**
  - **1. Muy malo** → 112 respuestas (0.9%)
  - **2. Malo** → 573 respuestas (4.4%)
  - **3. Regular** → 3224 respuestas (24.6%)
  - **4. Bueno** → 7469 respuestas (57.1%)
  - **5. Muy bueno** → 1700 respuestas (13.0%)
  - **99. Ns/Nr** → 4 respuestas (0.0%)

### `ind_salud_101`
**Pregunta:** Indicador de percepción del estado de salud

**Tipo:** variable numérica continua. No tiene opciones categóricas fijas.

**Resultados (resumen estadístico):**
  - n válidos: 13082
  - Media: 0.70
  - Mínimo: 0.00
  - Máximo: 1.00
  - Desviación estándar: 0.46
  - Sin dato / NaN: 0

### `ind_salud_102`
**Pregunta:** Escala del Trastorno de Ansiedad Generalizada (GAD-7)

**Opciones de respuesta:**
  - 0. No se aprecia ansiedad
  - 1. Se aprecian síntomas de ansiedad leves
  - 2. Se aprecian síntomas de ansiedad moderados
  - 3. Se aprecian síntomas de ansiedad severos

**Resultados (base limpia, n=13082):**
  - **0. No se aprecia ansiedad** → 10440 respuestas (79.8%)
  - **1. Se aprecian síntomas de ansiedad leves** → 1876 respuestas (14.3%)
  - **2. Se aprecian síntomas de ansiedad moderados** → 588 respuestas (4.5%)
  - **3. Se aprecian síntomas de ansiedad severos** → 178 respuestas (1.4%)

## Factores de expansión

### `fexp_calp_anu`
**Pregunta:** Factor de expansión calibrado bimestral para personas.

**Tipo:** variable numérica continua. No tiene opciones categóricas fijas.

**Resultados (resumen estadístico):**
  - n válidos: 13082
  - Media: 467.08
  - Mínimo: 2.64
  - Máximo: 7490.93
  - Desviación estándar: 451.05
  - Sin dato / NaN: 0

### `fexp_calh_anu`
**Pregunta:** Factor de expansión calibrado bimestral para hogares

**Tipo:** variable numérica continua. No tiene opciones categóricas fijas.

**Resultados (resumen estadístico):**
  - n válidos: 13082
  - Media: 221.02
  - Mínimo: 2.55
  - Máximo: 2805.14
  - Desviación estándar: 179.43
  - Sin dato / NaN: 0
