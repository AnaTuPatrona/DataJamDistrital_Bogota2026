# Bitácora de supuestos y decisiones metodológicas

**Proyecto:** DataJam Distrital Bogotá 2026 — Línea temática Mujer
**Equipo:** Siseven Larpsito Sahur Devs
**Última actualización:** 2026-08-20

---

## Cómo usar este archivo

Este documento cumple tres funciones y las tres importan en la sustentación:

1. **Preregistro.** La Sección 1 fija las hipótesis, las variables dependientes y los criterios de significancia **antes** de correr ningún modelo. Es la evidencia de que no hubo *p-hacking*.
2. **Bitácora.** La Sección 2 registra cada decisión metodológica con su justificación y su fecha.
3. **Control de verificaciones.** La Sección 3 lista las comprobaciones pendientes; ninguna fase avanza con una verificación en rojo.

**Regla de oro:** si durante el análisis se toma una decisión que no está aquí, se escribe aquí antes de continuar. Si un resultado obliga a cambiar algo preregistrado, **no se borra el registro original**: se añade una entrada nueva explicando qué cambió y por qué.

---

# 1. PREREGISTRO

> Congelado antes de ejecutar cualquier modelo. Cualquier desviación posterior se documenta en la Sección 2 como enmienda numerada.

## 1.1 Hipótesis y signos esperados

| ID | Hipótesis | Variable dependiente | Predictor de interés | Signo esperado |
|---|---|---|---|---|
| **H1′** | La cobertura institucional aparente y la real divergen; la divergencia es mayor donde peor se percibe el acceso a denunciar | `Δ_rank` (rank_real − rank_admin) | `IPSJ_C_prom` | **Negativo** |
| **H1′-b** | La divergencia es mayor donde hay menor confianza vecinal | `Δ_rank` | `ICG_B_prom` | **Negativo** |
| **H1′-c** | El sistema no escala con el riesgo registrado | `RC_real` | `tasa_admin` | **Negativo** |
| **H-A (M1)** | La concentración femenina del cuidado se asocia con menor acceso percibido a la denuncia | `IPSJ_C` | `ICC_mujer` y su interacción con `D1` | **Negativo** |
| **H-A (M2)** | …y con menor probabilidad de afrontar violencia presenciada | `afronto_M` | `ICC_mujer × D1` | **OR < 1** |
| **H-A (M3)** | La confianza vecinal media entre carga de cuidado y afrontamiento | `ICG_B` | `ICC_mujer`, `TAC` local | Por determinar |
| **H-B** | La no-injerencia, no los roles tradicionales, acompaña la baja tasa de afrontamiento | `TAC_M` por localidad | Factor 3 (no-injerencia) vs. Factor 1 (roles) | **F3 significativo, F1 no** |
| **H-B-val** | Validación interna con la otra encuesta | `TAC_M` | `ICG_B` | **Positivo** |

## 1.2 Controles fijados de antemano

Todos los modelos individuales incluyen: `C303` (pobreza subjetiva), `H1` (estrato, categórica), `A6x3` y su cuadrado (edad), `D1` (sexo), `sexo_jefe`, `A4` (menores en el hogar), `ind_salud_102` (GAD-7) y efectos fijos de `codigo_localidad`.

**No se añadirán controles adicionales después de ver los resultados.** Si alguno resulta necesario, se documenta como enmienda.

## 1.3 Criterios de decisión

| Criterio | Umbral | Consecuencia si no se cumple |
|---|---|---|
| Significancia individual | p < 0,05 tras corrección Benjamini-Hochberg | El coeficiente se reporta como no significativo, no se reinterpreta |
| Significancia territorial (n=19) | ρ de Spearman ≥ 0,46 (valor crítico al 5%) | La correlación se reporta como no concluyente |
| Robustez *leave-one-out* | El signo se mantiene en las 19 iteraciones | El resultado se degrada de "hallazgo" a "exploración" |
| Publicación de un estimador por localidad | n muestral ≥ 30 **y** CV ≤ 30% | La celda se marca "estimación no publicable"; no se oculta ni se imputa |
| Poder para modelar una variable binaria | ≥ 150 casos positivos | Se descarta esa variable como dependiente |

## 1.4 Escenarios de refutación aceptados

1. **H1′ refutada** si ρ(rank_admin, rank_real) > 0,85 con IC que excluye 0,6. Se reporta: *el sistema distrital está mejor calibrado de lo que sugiere la teoría del subregistro*.
2. **H-A refutada** si `ICC_mujer` no es significativa sobre `IPSJ_C` tras BH. H1′ sobrevive como diagnóstico descriptivo, sin mecanismo individual.
3. **H-B refutada** si el análisis factorial arroja un solo factor con alfa alto: "el machismo" sería unidimensional y la distinción carecería de sustento.

> Los tres escenarios se presentarán en la sustentación si ocurren. Un hallazgo nulo bien documentado es un resultado, no un fracaso.

---

# 2. BITÁCORA DE DECISIONES

## D-01 · `Jx402` y `Jx403` no son modelables
**Fecha:** 2026-08-20 · **Estado:** cerrada

`Jx402 = 1` arroja **24 casos** sobre 13.082 (0,2%); `Jx403` se reparte en 17 "Sí" y 7 "No". Con 24 casos en 19 localidades el chequeo *go/no-go* (mínimo 150) falla.

**Decisión:** no se usan como variable dependiente, ni como denominador, ni para estimación territorial. Se reportan únicamente como descriptivo de ciudad.

**Advertencia obligatoria al citarlos:** que 17 de 24 hayan denunciado (71%) **no** estima la tasa de denuncia de Bogotá. Es sesgo de selección: quien admite violencia intrafamiliar ante un encuestador dentro de su vivienda es desproporcionadamente quien ya denunció.

## D-02 · Interpretación del bloque 404
**Fecha:** 2026-08-20 · **Estado:** **cerrada — confirmada por V-01 con observación**

`Mx404_6` ("No afrontó la situación") marca "Sí" en 10.625 registros (81,2%). Si significara "presenció y no afrontó", ocho de cada diez bogotanos habrían presenciado violencia contra una mujer, lo cual es implausible.

**Interpretación adoptada:** `_6 = 1` agrupa a quien no presenció con quien presenció y calló, **sin posibilidad de separarlos**. Solo `_6 = 0` es interpretable, como afrontamiento efectivo.

**Confirmación empírica (V-01, ejecutada 2026-08-20):**

| Chequeo | K | L | M | N | Veredicto |
|---|---|---|---|---|---|
| Frecuencias vs. diccionario | ✓ | ✓ | ✓ | ✓ | Coinciden al registro |
| Cobertura (`_6 = 0` ⇒ algún lugar) | 0 | 0 | 0 | 0 | **Sin excepciones** |
| Exclusividad (`_6 = 1` ⇒ ningún lugar) | 19 | 15 | 17 | 16 | 0,11%–0,15% de la muestra |
| Marcas por persona | 1,44 | 1,32 | 1,31 | 1,31 | Respuesta múltiple confirmada |

**El resultado decisivo es la cobertura: cero excepciones en los cuatro bloques.** Ningún registro tiene `_6 = 0` sin marcar al menos un lugar, lo que demuestra que `_6` y las marcas de lugar son complementarias por diseño: `_6 = 1 − 1[algún lugar]`.

Las 15–19 violaciones de exclusividad no refutan la interpretación: si `_1..5` midieran "dónde presenció" con `_6` independiente, se esperarían 2.500–3.000 solapamientos sobre 10.625 marcas, no 17. La magnitud observada corresponde a inconsistencia de captura.

**Conclusión:** D-02 se sostiene. La TAC se construye como está definida en D-03.

**Hallazgo lateral aprovechable:** el acoso sexual se afronta en 1,44 espacios por persona frente a 1,32 de la violencia intrafamiliar. El acoso está más disperso territorialmente; la violencia intrafamiliar, más concentrada. Alimenta el gráfico 2 y la diferenciación de rutas de atención.

## D-16 · Tratamiento de los registros que violan la exclusividad del bloque 404
**Fecha:** 2026-08-20 · **Estado:** cerrada · **Depende de:** D-02, V-01

67 registros en total (19 K · 15 L · 17 M · 16 N) presentan simultáneamente `_6 = 1` y al menos una marca de lugar.

**Decisión:** se recodifican como **afrontamiento** (`afronto = 1`), privilegiando la marca de lugar sobre la casilla residual.

**Justificación doble:**

1. Una marca de lugar es información afirmativa y específica; `_6` es la opción residual. Ante contradicción, prevalece la más informativa.
2. Es la opción **conservadora respecto a la propia hipótesis**: eleva la TAC en lugar de reducirla — en el bloque M, de 18,78% a 18,91%. Adoptar la codificación que debilita ligeramente el argumento propio es defendible en sustentación; la contraria no lo es.

**Impacto:** ≤ 0,13 puntos porcentuales en cualquier indicador. Irrelevante para los resultados, pero se documenta y se menciona en la hoja de metodología del dashboard.

## D-03 · Eliminación del Índice de Silencio (ITS)
**Fecha:** 2026-08-20 · **Estado:** cerrada · **Depende de:** D-02

Consecuencia directa de D-02: una tasa definida como *silencio ÷ exposición* no tiene denominador observable.

**Reemplazo:** **TAC — Tasa de Afrontamiento Ciudadano** = Σ w · afronto_M ⁄ Σ w, donde `afronto_M = 1` si `Mx404_6 = 0`.

**Límite que debe declararse en toda presentación:** la TAC mide simultáneamente cuánta violencia hay visible y cuánta ciudadanía actúa, y no las separa. Opera como **cota inferior de la exposición**. Redacción obligatoria: *"al menos el X% presenció y afrontó una situación de violencia contra una mujer"*. Prohibido: *"el X% está expuesto a violencia"*.

## D-04 · Codificación de los nulos de `Jx402`
**Fecha:** 2026-08-20 · **Estado:** cerrada

El diccionario de la v3 documenta que los 11.094 nulos de `Jx402` coinciden exactamente con `Ax401 = 2`.

**Decisión:** un nulo es "no aplica" (el hogar no fue víctima de ningún delito) y se recodifica a `0`. **No se corre análisis de sensibilidad** con codificación alternativa: la validación del filtro maestro lo vuelve innecesario. Esta decisión revierte la que figuraba en la versión anterior del plan, cuando `Ax401` no estaba disponible.

## D-05 · Unidad de conglomerado
**Fecha:** 2026-08-20 · **Estado:** cerrada

`DIRECTORIO_MZ` (manzana) no está en la base publicada y era la unidad primaria de muestreo.

**Decisión:** usar `codigo_UPL` como conglomerado (30 grupos) y `codigo_localidad` como estrato. Treinta conglomerados están en el límite inferior aceptable, de modo que se aplica corrección de muestras pequeñas (`use_correction=True`) y se declara en la metodología del dashboard.

**Robustez asociada:** reestimar con `SectorUPL` (6 grupos) para verificar que los errores estándar no dependan de la elección.

## D-06 · Universo territorial de 19 localidades
**Fecha:** 2026-08-20 · **Estado:** cerrada

`codigo_localidad` en la encuesta tiene 19 valores: Sumapaz no fue encuestada. Los registros administrativos cubren 20.

**Decisión:** todos los rankings, correlaciones y cuadrantes se calculan sobre las 19 localidades encuestadas. Sumapaz se reporta aparte, con `RC_admin` únicamente. La dimensión maestra lleva una bandera `en_encuesta` para impedir que entre como cero. **Nunca se imputa.**

## D-07 · `IPSJ_C` como variable dependiente principal de H-A
**Fecha:** 2026-08-20 · **Estado:** cerrada · **Depende de:** D-01

Perdida `Jx403`, la barrera de denuncia se mide con `IPSJ_C` — acceso percibido a la información y los medios para denunciar delitos, escala 1–5, n = 11.904, media 2,86.

**Justificación:** captura el mismo constructo (fricción en el acceso a la ruta), con 496 veces más observaciones, y es previo al hecho victimizante en lugar de posterior, lo que reduce el sesgo de selección de D-01.

**Interacción obligatoria:** `ICC_mujer × D1`. La hipótesis es sobre mujeres sobrecargadas, no sobre hogares sobrecargados; sin la interacción el coeficiente no responde la pregunta planteada.

## D-08 · `ICG_B` como proxy de no-injerencia
**Fecha:** 2026-08-20 · **Estado:** cerrada

*"Confío en que mis vecinos me ayudarían ante cualquier problema o necesidad"*, n = 12.912, media 3,08.

**Decisión:** se incorpora como medida de norma comunitaria **dentro de la Encuesta de Percepción**, de modo que H-B deja de depender exclusivamente de la Bienal y pasa a tener validación cruzada entre dos muestras independientes.

**Límite:** mide confianza en recibir ayuda, no disposición a darla. Es un proxy, y así debe nombrarse.

## D-09 · Supuesto de heteronormatividad en el ICC
**Fecha:** 2026-08-20 · **Estado:**  **abierta — requiere V-04**

Al identificar el sexo del responsable principal del cuidado: si la categoría modal es "El/la cónyuge o pareja del jefe de hogar", se infiere su sexo como el complemento de `sexo_jefe`.

**Es un supuesto fuerte.** Debe reportarse qué porcentaje de los casos depende de él. Si supera el 25% de la muestra analítica, correr el modelo también con esos casos excluidos y comparar.

## D-10 · Tratamiento de las tareas del bloque 201
**Fecha:** 2026-08-20 · **Estado:** cerrada

Frecuencias problemáticas: `Dx201` (planchar) tiene 58,4% de "No se realiza"; `Hx201` e `Ix201` tienen 63,2% de nulos y `Jx201` 56,3%, correspondientes a hogares sin menores o sin personas mayores.

**Decisiones:**
- El conjunto de tareas efectivas T_e excluye "No se realiza" y los nulos
- Se excluyen del ICC los hogares con |T_e| < 5, reportando cuántos son
- El Índice de Cuidado Directo (ICD) se calcula solo sobre el ≈36% de hogares con cuidado observable, y **nunca se compara su media con la del ICC general**

## D-11 · Recodificación del estrato
**Fecha:** 2026-08-20 · **Estado:** cerrada

`H1` se trata como **categórica**, no continua: la distancia entre estrato 1 y 2 no equivale a la de 5 a 6. Los estratos 5 (1,9%) y 6 (1,0%) se agrupan para evitar celdas vacías. "No tiene servicio" y "No informa" (33 casos) forman una categoría propia, no se eliminan.

## D-12 · Pesos del INA
**Fecha:** 2026-08-20 · **Estado:** cerrada

`INA = 0,40 · pct(TAC_M) + 0,30 · pct(IBA) + 0,30 · pct(−RC_real)`

**Los pesos son arbitrarios y se declara que lo son.** Mitigación: se precalculan 3–5 escenarios de ponderación y se exponen como parámetro interactivo en el dashboard, invitando explícitamente al jurado a mover la ponderación y observar la estabilidad del ranking.

## D-13 · Datasets descartados
**Fecha:** 2026-08-20 · **Estado:** cerrada

| Dataset | Razón del descarte |
|---|---|
| `osb_malnutricion18_64` | Serie desde 2011, sin ventana común con el resto. "Exceso de peso" no es proxy válido de pobreza en Bogotá |
| `osb_saludmental-consumoabusivo_spageneral` | Mide demanda de tratamiento notificada, no prevalencia de consumo. Sustituido por `P53.12`/`P53.13` y `P65.5`/`P65.6` de la Bienal, que son percepción del entorno a nivel individual |

## D-14 · No se usan modelos de IA
**Fecha:** 2026-08-20 · **Estado:** cerrada

Con n=19 a nivel territorial, cualquier modelo de aprendizaje automático sobreajusta y no es defendible. **Es una decisión metodológica deliberada y se declara como tal en el formulario y en el dashboard**, no una omisión por falta de tiempo.

## D-15 · Relaciones, no *joins*, en Tableau
**Fecha:** 2026-08-20 · **Estado:** cerrada

Las tablas de hechos tienen granularidades distintas (localidad, localidad × trimestre, localidad × ítem). Un *join* físico duplicaría filas e inflaría todas las medidas. Se usan relaciones con cardinalidad declarada explícitamente.

---

# 3. VERIFICACIONES PENDIENTES

> Ninguna fase avanza con una verificación en rojo. Actualizar el estado y pegar el resultado al ejecutarla.

| ID | Verificación | Fase | Criterio de aprobación | Estado | Resultado |
|---|---|---|---|---|---|
| **V-01** | Exclusividad del bloque 404: tabular `Mx404_6` contra el máximo de `Mx404_1..5` | 1.4 | **Cero** registros con `_6 = 1` y alguna marca en `_1..5`. Si aparece alguno, D-02 se revisa antes de seguir | **amarillo** | **Ejecutada 2026-08-20.** Frecuencias y cobertura ✓ (0 huecos en K/L/M/N). Exclusividad: 19·15·17·16 violaciones = 0,11–0,15%, atribuidas a captura. **D-02 se confirma**; los 67 registros se resuelven en D-16. Detalle en `outputs/v01_verificacion_bloque404.csv` |
| **V-02** | Filtro maestro: `df[df.Ax401 == "No"].Jx402.isna().all()` y conteo de nulos = 11.094 | 1.2 | Ambas verdaderas | **verde** | **Ejecutada 2026-08-20.** `df[df.Ax401=="No"].Jx402.isna().all()` → `True`. `df.Jx402.isna().sum()` → 11.094. Ambas condiciones se cumplen exactamente (Paso 1.2, `01_preparacion.ipynb`). Nota: el criterio original en esta tabla usaba el código numérico `Ax401 == 2`, obsoleto desde que se tradujo a `"Si"/"No"`; se corrige aquí. |
| **V-03** | Factores de expansión: suma de `fexp_calp_anu` contra población adulta proyectada de Bogotá | 1.7 | Diferencia ≤ 15%. Si no, revisar si el factor es bimestral y requiere promediarse | rojo | *(pendiente)* |
| **V-04** | Peso del supuesto heteronormativo (D-09) | 2.5 | Reportar el %. Si > 25%, correr variante excluyendo esos casos | **verde** | **Ejecutada 2026-08-20.** 1.067 de 6.396 casos con sexo determinado (16,7%) dependen del complemento de `sexo_jefe` para inferir el sexo del responsable principal vía la categoría 'cónyuge'. Por debajo del umbral del 25% — **no se requiere correr la variante de exclusión**. Adicionalmente, 0 de esos casos tienen `sexo_jefe="Intersexual"`, por lo que ninguno quedó sin poder resolverse por complemento no definible (Paso 2.5, `02_indices.ipynb`). |
| **V-05** | Integridad de llaves: filas no emparejadas al unir cada fuente con `dim_localidad` | 1.5 | Cero, salvo Sumapaz en fuentes de encuesta | rojo | *(pendiente)* |
| **V-06** | Rangos de los índices construidos: HHI ∈ [1/7, 1], TAC ∈ [0,1], ICC ∈ [0,1] | 2 | Ningún valor fuera de rango teórico | rojo | *(pendiente)* |
| **V-07** | Alfa de Cronbach del IBA (`IPSJ_A`, `IPSJ_C`, `IPSJ_E`) | 2.13 | Si α < 0,60, **no promediar**: usar `IPSJ_C` sola | rojo | *(pendiente)* |
| **V-08** | Idoneidad factorial de la Bienal: KMO y Bartlett | 4.2 | KMO > 0,60 y Bartlett p < 0,05. Si no, reportar ítems individuales sin factorizar | rojo | *(pendiente)* |
| **V-09** | Localidades que incumplen el criterio de publicación (n<30 o CV>30%) | 5.2 | Si son más de cinco para un indicador, agregar ese indicador por `SectorUPL` | rojo | *(pendiente)* |
| **V-10** | Cuadre de totales: `fact_series_trimestral` contra los CSV originales de `/outputs` | 7 | Coincidencia exacta | rojo | *(pendiente)* |
| **V-11** | Codificación: todos los CSV exportados abren en Tableau con las tildes intactas | 7 | Inspección visual de `dim_localidad` | rojo | *(pendiente)* |
| **V-12** | Consistencia notebook ↔ dashboard: las cuatro tarjetas del D1 contra los valores del notebook | Tableau | Coincidencia exacta | rojo | *(pendiente)* |

**Leyenda:** rojo pendiente · amarillo ejecutada con observaciones · verde aprobada

---

# 4. LIMITACIONES DECLARADAS

> Estas cinco frases van íntegras en la hoja de metodología del dashboard y en la sustentación. Declararlas nosotros es más fuerte que dejar que las descubra el jurado.

1. **El análisis territorial se apoya en 19 unidades.** Los rankings de localidad son una herramienta de priorización, no una prueba estadística. Los intervalos de confianza se reportan y las localidades con intervalos solapados no se ordenan entre sí.

2. **Los modelos son asociativos, no causales.** No hay diseño experimental, variación exógena ni instrumento. Un coeficiente significativo indica asociación condicional, no efecto.

3. **La TAC es una cota inferior de la exposición.** Mide violencia presenciada y afrontada. Las personas que presenciaron y no actuaron no son distinguibles de quienes no presenciaron nada.

4. **La victimización directa por violencia intrafamiliar no es modelable** con esta fuente: 24 casos positivos. Se reporta como descriptivo, con su sesgo de selección explícito.

5. **Los errores estándar se clusterizan por UPL, no por manzana**, porque el identificador de manzana no está en la base publicada. Con 30 conglomerados se aplica corrección de muestras pequeñas.

---

# 5. ENMIENDAS AL PREREGISTRO

## Paso 1.3 — Restricción de `Jx402` (registrado 2026-08-20)

`Jx402` tiene **24 casos positivos** de 13.082 personas encuestadas (0,2%).
El chequeo *go/no-go* de la Fase 3 (mínimo 150 positivos) **falla**. El análisis procede por
la rama alternativa: `IPSJ_C` y la Tasa de Afrontamiento Ciudadano (TAC) como variables
dependientes, en lugar de `Jx402`/`Jx403`.

`Jx403` se distribuye en **17 Sí / 7 No**, calculado únicamente como descriptivo,
**etiquetado como NO inferencial**. No se usa como variable dependiente, ni como denominador
de ningún indicador, ni se reporta como estimación de la tasa de denuncia de Bogotá.

Nota cualitativa (mencionable en sustentación, siempre con esta advertencia): que 17 de 24
víctimas (71%) hayan denunciado no refuta el subregistro — lo confirma por otra vía, ya que
quien admite violencia intrafamiliar ante un encuestador dentro de su propia vivienda es
desproporcionadamente quien ya denunció (sesgo de selección).

## Paso 1.4 — Semántica del bloque 404, variable M (registrado 2026-08-20)

Verificaciones empíricas sobre `Mx404_1..6` (n=13082):
1. Proporción de `Mx404_6 == "Si"` = 0.8122 (≈ 0,812)
2. `n(Mx404_6 == "No")` = 2457
3. Exclusividad confirmada: 0 registros con `Mx404_6="Si"` y marca simultánea en `Mx404_1..5`

**Conclusión:** `_6 = "Si"` no distingue entre no haber presenciado y haber presenciado sin
actuar; solo `_6 = "No"` es interpretable, como afrontamiento efectivo. Por lo tanto:

- El Índice de Silencio (ITS) queda eliminado del plan: no tiene denominador observable.
- Se define la **TAC — Tasa de Afrontamiento Ciudadano** = proporción de personas con
  `Mx404_6 = "No"` (2457 positivos), directamente observable y usada como cota
  inferior de la exposición.

## Paso 1.4b — Análisis de sensibilidad de la TAC, parte 1: magnitud (registrado 2026-08-20)

Se identificaron 17 registros (0,13% de n=13.082) donde `Mx404_6="Si"` coexiste con al
menos una marca en `Mx404_1..5`, violando la exclusividad esperada. Diagnóstico:

- Sin patrón por opción específica marcada (`_1` a `_5` distribuidos 1–5 casos c/u).
- Sin patrón geográfico (13 localidades distintas, máx. 3 casos c/u) ni temporal
  (10 de 12 meses).
- Magnitud casi idéntica y consistente en los bloques hermanos: `Kx404`=19,
  `Lx404`=15, `Mx404`=17, `Nx404`=16 (todos en el rango 0,11%–0,15% de n=13.082).

Esto es consistente con un patrón sistemático de bajo nivel del instrumento (posible
traslape semántico de la opción `_6`), no con un error de captura localizado.

**Dos versiones construidas para análisis de sensibilidad posterior:**
- `TAC_A_original`: 2457 positivos (0.1878), tal como se definió en el Paso 1.4.
- `TAC_B_recodificada`: 2474 positivos (0.1891), donde los 17 casos con
  acción concreta declarada en `_1..5` se recodifican a `_6="No"` (la acción concreta
  manda sobre la ambigüedad de `_6`).
- Diferencia: 17 casos (0,130 pp) — marginal frente al tamaño de muestra.

**Pendiente:** la validación de robustez vía correlación con `ICG_B` (parte 2 de este
paso) requiere la Encuesta Bienal, que aún no se ha cargado ni cruzado. `ICG_B` NUNCA
se une a este `df` a nivel de fila — la Bienal y la Encuesta de Percepción no comparten
unidad de análisis individual. Esa validación se hará agregando ambas fuentes por
`codigo_localidad` en una fase posterior, no aquí.

Se usa `TAC_A_original` como definición principal en el resto del análisis de la Fase 1,
por ser la más directamente trazable a la pregunta del cuestionario. `TAC_B_recodificada`
queda disponible para la prueba de robustez cuando exista `ICG_B` agregado por localidad.

## Paso 1.4c — Reconciliación: Paso 1.4b vs. D-16 (registrado 2026-08-20)

El Paso 1.4b (arriba) dejó registrado que se usaría `TAC_A_original` (2.457 positivos,
0,1878) como definición principal, con `TAC_B_recodificada` (2.474, 0,1891) disponible
solo para prueba de robustez.

**Esa afirmación queda superada por D-16** (Sección 2 de este documento), que decidió
recodificar los 67 registros del bloque completo (19 K · 15 L · 17 M · 16 N) como
`afronto = 1`, privilegiando la marca de lugar sobre la casilla residual `_6`. La
variable `afronto_M` finalmente construida en el pipeline usa esta recodificación:
media 0,1891 sobre 13.082 — que coincide con `TAC_B_recodificada`, no con
`TAC_A_original`.

**Definición final vigente:** `afronto_M = 1` si `Mx404_6 == "No"` **o** si
`Mx404_6 == "Si"` con marca simultánea en `Mx404_1..5` (recodificado). Esta es la
definición usada en `afronto_M`, `afronto_K`, `afronto_L`, `afronto_N` y en la TAC
reportada en Fase 3. `TAC_A_original` (sin recodificar) queda documentada como
comparador de sensibilidad, no como definición principal — corrigiendo lo escrito en
el Paso 1.4b.

No se borra el Paso 1.4b: esta entrada deja constancia del cambio, según la Regla de
oro de la Sección 0 de este documento.

## Paso 1.4c — Cierre de la sensibilidad A-vs-B; reconciliación con D-16 (registrado 2026-08-20)

El Paso 1.4b dejó registrado `TAC_A_original` (2.457 positivos, 0,1878) como definición
principal, con `TAC_B_recodificada` (2.474, 0,1891) como comparador de sensibilidad
pendiente de validar contra `ICG_B`.

**Esa afirmación queda superada por D-16** (Sección 2 de este documento), que resolvió
la ambigüedad de los 67 registros del bloque completo (19 K · 15 L · 17 M · 16 N)
recodificándolos como `afronto = 1`, con justificación propia e independiente de
`ICG_B`. La variable `afronto_M` finalmente construida en el pipeline (media 0,1891
sobre 13.082) coincide con `TAC_B_recodificada`, no con `TAC_A_original`.

**Se cierra la comparación de sensibilidad A-vs-B contra ICG_B como innecesaria:**
`TAC_A_original` y `TAC_B_recodificada` fueron columnas exploratorias creadas solo en
memoria en este notebook, nunca persistidas a disco. El notebook de Fase 2/3 recarga
el CSV original desde cero y no las tiene disponibles. Como D-16 ya zanjó cuál
definición usar —con su propia justificación, no supeditada a esta comparación—, no se
exportan ni se reconstruyen. `Jx402`/pipeline sigue usando exclusivamente `afronto_M`
(= `TAC_B_recodificada`) de aquí en adelante.

**Queda pendiente, y es lo que realmente importa:** la validación preregistrada
**H-B-val** (`TAC_M` correlaciona positivo con `ICG_B`) debe correrse en el notebook
de Fase 2/3, con la definición final de `afronto_M` ya construida ahí (D-16), una vez
`ICG_B` esté disponible. Ver Paso 2.x en el notebook correspondiente para el resultado.

No se borra el Paso 1.4b: esta entrada deja constancia del cambio y de por qué se cierra
sin ejecutar, según la Regla de oro de este documento.

## Paso 1.5 — Construcción de `dim_localidad` (registrado 2026-08-20)

Se construyó `dim_localidad` con 20 filas (`codigo_localidad` 1–20, `nombre_oficial`,
`nombre_norm`, `sector_upl`, `en_encuesta`, `PobMujeres`), usando `normalizar()` =
`unidecode().upper().strip()` con espacios múltiples colapsados.

**Codificación confirmada empíricamente:** se cruzó `codigo_localidad` de la Encuesta de
Percepción contra su propia columna `Localidad` (texto) y coincide exactamente con la
codificación DANE estándar asumida (1=Usaquén ... 19=Ciudad Bolívar, 20=Sumapaz). No se
asumió a ciegas — se verificó código por código.

**`en_encuesta`:** única localidad marcada `False` es Sumapaz (código 20), como se esperaba.

**`PobMujeres`:** extraída de `riesgofeminicidio.csv`, corte más reciente (2026-03-31),
sin faltantes en las 20 localidades.

**Verificación cruzada de las 6 fuentes contra `dim_localidad`:**

| Fuente | Resultado |
|---|---|
| `riesgofeminicidio.csv` | OK — 0 no coincidencias |
| `duplas.csv` | OK — 0 no coincidencias |
| `lineapurpura.csv` | OK — 0 no coincidencias |
| `delitossexuales.csv` | OK — 0 no coincidencias |
| `llamadas123_consolidado_limpio.csv` | OK — 0 no coincidencias (tras corregir separador `;` y encoding) |
| Encuesta de Percepción (`df`) | OK — solo Sumapaz ausente, tolerado por diseño |

**Excepción documentada — `llamadas123_consolidado_limpio.csv`:** 222 registros
(0.42% de 52717) tienen `CODIGO_LOCALIDAD` nulo tras la
conversión numérica. Se excluyen de toda agregación territorial (Nivel 2 de la jerarquía
de integración) por no tener llave de cruce válida contra `dim_localidad`. No se imputan.
Su magnitud (<0,5%) se considera marginal frente al volumen total del dataset.

**Nota técnica:** `llamadas123_consolidado_limpio.csv` usa separador `;` (no `,`) y
codificación con BOM (`utf-8-sig`) — debe cargarse con `sep=";"` explícito o las 13
columnas colapsan en una sola.

## Paso 1.6 — Diseño muestral: estrato y conglomerado (registrado 2026-08-20)

**Decisión:** se fija `codigo_UPL` como unidad de conglomerado (30
grupos) y `codigo_localidad` como estrato (19 grupos, sobre las
19 localidades encuestadas).

**Motivo:** la encuesta no trae identificador de manzana ni de UPZ (se eliminó
`DIRECTORIO_MZ` en el ETL por no ser un identificador reutilizable de conglomerado
espacial estable), y `codigo_UPL` es el nivel geográfico más fino disponible que agrupa
personas por cercanía real dentro de una misma localidad. Usar `codigo_localidad` como
conglomerado en vez de estrato sería demasiado grueso (perdería variación intra-localidad
en los errores estándar); usar `codigo_UPL` como estrato sería excesivamente granular
para los modelos con efectos fijos de localidad que se van a estimar en la Fase 3.

**Advertencia de tamaño de muestra:** 30 conglomerados
está en el límite inferior aceptable para inferencia con errores estándar robustos
clusterizados (la literatura recomienda ≥30–50 clusters para que la asintótica de
White/Huber-clusterizado sea confiable). Tamaño de conglomerado: media
436.1, rango [32, 756].

**Mitigación:** se usará corrección de muestras pequeñas en todos los modelos con errores
estándar clusterizados por `codigo_UPL`, vía `cov_kwds={'use_correction': True}`
(statsmodels), que aplica el factor de corrección G/(G-1) · (N-1)/(N-k) sobre la matriz
de covarianza cluster-robusta. Esta decisión se reporta explícitamente en cualquier tabla
de resultados de la Fase 3 (regresión logística de H-A), con una nota al pie indicando
que los ICs pueden ser algo anticonservadores dado el número de conglomerados.

**Ponderación:** toda estimación agregada usa `fexp_calp_anu` (personas) o
`fexp_calh_anu` (hogares) según corresponda — nunca conteos crudos sin ponderar para
estimaciones poblacionales, solo para descriptivos exploratorios ya identificados como
tales (ej. Pasos 1.3, 1.4, 1.4b).

## Paso 1.7 — Validación de factores de expansión (registrado 2026-08-20)

**Población adulta de Bogotá de referencia:** 6,201,042
(orden de magnitud declarado: 6-7 millones). Tolerancia aceptada: 15%.

**Interpretación A (suma directa, 12 meses):** 6,110,290
→ diferencia relativa 1.5% (dentro de tolerancia)

**Interpretación B (bimestral, promedio de la suma entre los 6
bimestres del año móvil):** 1,018,382
→ diferencia relativa 83.6% (FALLA tolerancia)

**Método adoptado:** `suma_directa_por_localidad`. Suma total final: 6,110,290
(diferencia relativa 1.5%).

**Regla operativa para el resto del pipeline:** toda estimación poblacional agregada
(por localidad, UPL, o total ciudad) que use `fexp_calp_anu` debe replicar este mismo
método — sumar directamente, sin promediar por bimestre.
Aplicar el método incorrecto no aplica en este caso.

## Gráfico de control 1 — Población femenina expandida vs. oficial (registrado 2026-08-20)

Comparación por localidad entre `PobMujeres` (oficial, `riesgofeminicidio.csv`, corte
2026-03-31) y la población femenina estimada desde la Encuesta de Percepción
(suma de `fexp_calp_anu` para `D1 == "Mujer"`, agrupada por `codigo_localidad`).

**Propósito:** control de calidad interno del factor de expansión a nivel de localidad
(no solo a nivel ciudad, como en el Paso 1.7). No se incluye en el dashboard de Tableau —
es un diagnóstico de proceso, guardado en `docs/grafico_control_1_pobmujeres.png`.

**Resultado:** 12 localidad(es) exceden ±15% de diferencia: Antonio Nariño, Los Mártires, Barrios Unidos, Teusaquillo, Tunjuelito, Puente Aranda, Rafael Uribe Uribe, Usme, Usaquén, Ciudad Bolívar, Bosa, Suba. Investigar antes de usar estimaciones de localidad específicas de estas zonas con alta confianza.

Diferencia relativa promedio (valor absoluto) entre localidades: 17.3%.

## Gráfico de control 1 — Diagnóstico de discrepancias por localidad (registrado 2026-08-20)

A nivel ciudad, la población femenina expandida desde la encuesta (adultos, `fexp_calp_anu`)
difiere -16.3% de `PobMujeres` oficial (todas las edades). A nivel localidad, 12 de 19
exceden ±15% de diferencia (todas subestiman).

**Hipótesis descartadas por falta de correlación:**
- Proporción de menores en el hogar (proxy de estructura etaria): correlación 0.023 con
  `diff_pct` — no explica la variación entre localidades.
- Tamaño de muestra por localidad: correlación -0.172 con `|diff_pct|` — débil, solo
  visible en los extremos (las 3 localidades de menor `n`: La Candelaria, Los Mártires,
  Antonio Nariño, concentran los errores más extremos en ambas direcciones).

**Conclusión:** la discrepancia responde a una combinación de (1) un componente
sistemático de ciudad, consistente con que `PobMujeres` incluye todas las edades mientras
la encuesta solo mide población adulta (18+), y (2) ruido muestral que se amplifica en
localidades con `n` bajo. No se identifica un error del factor de expansión ni del
pipeline de limpieza — el Paso 1.7 ya confirmó que la suma total del factor es correcta
(1.5% de diferencia contra la población adulta oficial de Bogotá, 6.201.042).

**Regla operativa:** los indicadores basados en la Encuesta de Percepción para
**Los Mártires, Antonio Nariño, Barrios Unidos y La Candelaria** deben reportarse con una
nota de precaución adicional por bajo tamaño muestral (n entre 151 y 270), siguiendo el
mismo criterio ya aplicado a Sumapaz. El resto de localidades (n≥296) se consideran
confiables para estimación, con el entendido de que cualquier tasa que use `PobMujeres`
(todas las edades) como denominador administrativo y un numerador derivado de la encuesta
(solo adultos) tiene un descalce conceptual de denominador que debe declararse en el
dashboard, no ocultarse.

## Paso 2.2 — Tareas efectivas y exclusión por información insuficiente (registrado 2026-08-20)

Nota de unidad de análisis: `DIRECTORIO_HOG` fue eliminado en el ETL original, por lo que
no existe identificador de hogar independiente del respondiente. Se trata cada fila de
`df` como un "hogar" a efectos del ICC — el respondiente reporta sobre la distribución
de tareas de su propio hogar, y no hay forma de agregar múltiples respondientes al mismo
hogar en esta base.

`T_e` = tareas del bloque 201 donde la respuesta no es nula ni "No se realiza".
Se excluyen filas con `|T_e| < 5` (información insuficiente).

**Excluidos:** 60 de 13082 (0.46%).
Base resultante para el ICC: 13022 filas.

## Paso 2.4 — Índice de Herfindahl de concentración del cuidado, HHI (registrado 2026-08-20)

`HHI = Σ_k (n_k / |T_e|)²`, calculado sobre las 13022 filas que pasaron el
filtro de `|T_e| ≥ 5` (Paso 2.2), con 7 categorías de responsable (Paso 2.3).

**Rango teórico:** [0.1429, 1.0000]. Rango observado:
[0.1837, 1.0000] — dentro del rango teórico, validado.

**Distribución:** media 0.6955, mediana 0.7222,
desviación estándar 0.2465.

**Casos de concentración total (HHI=1.0):** 4162
(32.0% de la base filtrada).

**Nota metodológica importante:** el HHI, tal como está definido aquí, es **agnóstico
respecto de quién concentra** — un hogar donde "El/la jefe/a de hogar" hace todo tiene el
mismo HHI=1.0 que uno donde "Servicio contratado" hace todo. Para la Hipótesis H-A
(concentración FEMENINA del cuidado como barrera de acceso a la denuncia), el HHI por sí
solo NO es la variable independiente — se necesita un paso adicional que identifique el
sexo de quien concentra (cruzando con `sexo_jefe` para las categorías "jefe/a" y "cónyuge"),
antes de poder interpretar el HHI como una medida de carga femenina de cuidado específicamente.

## Paso 2.5 — Responsable principal (k*) y determinación de sexo (registrado 2026-08-20)

`k* = argmax_k(n_k)` por fila, sobre las 7 categorías de responsable. Empates se marcan
explícitamente como "Empate — no determinable", sin resolución arbitraria por orden de
columna: **799** filas (6.14%).

**Distribución de k\*:**
- El/la jefe/a de hogar: 5.329 (40,7%)
- Todos los miembros del hogar: 2.444
- Ambos cónyuges o pareja: 2.283
- El/la cónyuge o pareja: 1.067
- Empate — no determinable: 799
- Servicio contratado: 542
- Otros miembros del hogar: 402
- Familiar externo: 156

**Regla de determinación de sexo:**
- `k*="jefe/a de hogar"` → sexo = `sexo_jefe` directo. **5329** casos
  (40.9%), sin supuesto adicional.
- `k*="cónyuge"` → sexo = complemento de `sexo_jefe` (supuesto de heteronormatividad).
  **1067** casos (8.2%). Ningún caso con
  `sexo_jefe="Intersexual"` cayó en esta rama (0 casos), así que no hubo que descartar
  ninguno por complemento no definible.
- Cualquier otro `k*` (incl. empates) → "No determinable".

**Total con sexo determinado (Hombre/Mujer/Intersexual):** 6396
(49.1% de 13022).
De ellos, **16.7%** (1067 de 6396)
depende del supuesto de heteronormatividad — no son un dato directo de la encuesta.

**Total "No determinable":** 6626 (50.9%).
Nota: esta cifra YA incluye los 799 empates (no se suman aparte).

**Distribución del sexo determinado:** Mujer 4484
(70.1% de los determinables),
Hombre 1909
(29.8%),
Intersexual 3.

**Limitación declarada:** casi la mitad de la base (50.9%)
queda sin responsable principal de sexo determinable — sobre todo por reparto compartido
("Todos los miembros", "Ambos cónyuges"), que en sí mismo es información válida (ausencia
de concentración individual) pero no sirve para H-A, que requiere identificar una persona
concentradora. El 16.7% de los casos SÍ determinables depende del
supuesto de heteronormatividad; se recomienda repetir los modelos de la Fase 3 excluyendo
estos casos como análisis de sensibilidad.

## Paso 2.5 (adenda) — Composición del sexo determinado y sesgo de selección potencial (registrado 2026-08-20)

**Composición del subconjunto con sexo determinado** (n=6396):
- Mujer: 4484 (70.1%)
- Hombre: 1909 (29.8%)
- Intersexual: 3

La mujer es responsable principal en 70.1% de los casos donde el responsable
es identificable — consistente con la hipótesis general del proyecto sobre concentración
femenina del trabajo de cuidado.

**Advertencia de sesgo de selección declarada de antemano:** el subconjunto analizable
para H-A (6396 de 13022, 49.1%) **no es una
muestra aleatoria** del total. Queda excluido el 50.9% de los casos donde el
cuidado se reparte sin una persona concentradora única ("Todos los miembros del hogar",
"Ambos cónyuges o pareja", empates), que en sí mismo es información sustantiva (ausencia
de concentración) pero no es utilizable para identificar el sexo de un responsable
principal.

**Implicación:** es plausible que el subconjunto "determinable" esté sesgado hacia hogares
con división de tareas más tradicional/menos igualitaria — precisamente los hogares donde
SÍ existe una persona que concentra el cuidado son los que producen un `k*` no compartido.
Hogares más igualitarios en la distribución de tareas (que podrían tener perfiles
sociodemográficos distintos — mayor estrato, parejas más jóvenes, etc.) tienden a caer en
"No determinable" por reparto compartido, y quedan fuera del análisis de H-A.

**Consecuencia para la interpretación de resultados:** cualquier hallazgo de H-A (efecto de
la concentración de cuidado sobre `IPSJ_C` o la TAC) debe leerse como válido para el
subconjunto de hogares con responsable de cuidado identificable, no como representativo
de la población general de Bogotá. Esto se declara explícitamente en la Fase 3, no se
extrapola sin esta salvedad.

**Diagnóstico exploratorio realizado** (perfil determinable vs. no determinable):
                    n  pct_pobre_subjetivo
es_determinable                           
False            6626                 13.0
True             6396                 21.3

Se recomienda revisar si esta diferencia de perfil es sistemática (ej. vía estrato `H1`
o pobreza subjetiva `C303`) antes de interpretar los coeficientes de H-A en la Fase 3, y
mencionar esta limitación en la sustentación como una de las razones por las que H-A se
declaró como hipótesis de *soporte individual*, no como prueba poblacional generalizable.

## Paso 2.7 — Variable categórica de comunicación (registrado 2026-08-20)

Se construyó `carga_cuidado_categoria` según la regla del enunciado, con una 4ª categoría
explícita para un caso borde no cubierto por las 3 reglas originales:

| Categoría | Criterio | n | % |
|---|---|---|---|
| Carga concentrada en mujer | ICC_mujer ≥ 0,50 | 3585 | 27.5% |
| Carga concentrada en hombre | HHI ≥ 0,50 ∧ responsable=Hombre | 1713 | 13.2% |
| Carga compartida | HHI < 0,50 | 3218 | 24.7% |
| **Concentrada, responsable no determinable** *(añadida)* | HHI ≥ 0,50 ∧ responsable ∉ {Mujer, Hombre} | 4506 | 34.6% |

**Por qué se añadió la 4ª categoría:** las 3 reglas originales dejan un vacío lógico —
`HHI ≥ 0,50` con responsable "No determinable" (empates, o `k*` en categorías compartidas
como "Ambos cónyuges"/"Todos los miembros" que igual concentran ≥50% del HHI) no cumple
ninguna de las 3 condiciones originales. Forzarlo silenciosamente a "compartida" sería
incorrecto (HHI alto = SÍ hay concentración), y forzarlo a "mujer" u "hombre" inventaría
un sexo no determinado. Se prefiere una 4ª categoría explícita y minoritaria antes que
ocultar el caso dentro de una de las 3 originales.

**Uso en dashboard:** esta variable es la que se usará para el Gráfico 1 y cualquier
visual de "quién carga el cuidado" — se recomienda mostrar las 4 categorías o, si el
espacio del dashboard lo exige, fusionar la 4ª dentro de "Carga compartida" con una nota
al pie que aclare la diferencia conceptual (concentración existe, pero no en una persona
de sexo identificable).

## Gráfico 1 (dashboard) — Distribución de HHI por sexo del responsable principal (registrado 2026-08-20)

**Estadísticos** (n=6393 con sexo determinado):

| Sexo | Media HHI | Mediana HHI | n | % con HHI≥0,50 |
|---|---|---|---|---|
| Mujer | 0,728 | 0,755 | 4.484 | 80,0% |
| Hombre | 0,832 | 1,000 | 1.909 | 89,7% |

**Hallazgo — no confundir con la hipótesis principal del proyecto:** cuando el hombre
es responsable principal, concentra las tareas de cuidado en mayor grado que cuando lo
es la mujer (mediana 1,00 vs. 0,76). Esto es un hallazgo *condicional* — mide intensidad
de concentración dado que ya se es el responsable, no la probabilidad de llegar a serlo.

**No contradice H-A:** la evidencia central de H-A no es la intensidad de concentración
por sexo, sino la **prevalencia**: 4.484 mujeres son responsables principales frente a
1.909 hombres (2,35× más mujeres), documentado en el Paso 2.5. Son dos preguntas
distintas — "¿quién llega a concentrar el cuidado?" (mayoritariamente mujeres) vs.
"¿cuánto concentra quien ya lo hace?" (más intenso en hombres, posiblemente porque los
hombres que terminan siendo responsable único de cuidado en este contexto lo hacen en
hogares con menos alternativas de reparto — hipótesis no verificada aquí, requeriría
análisis adicional).

**Título del dashboard elegido para evitar esta confusión:** *"Cuando el hombre asume la
responsabilidad principal del cuidado, la concentra más"* — describe el hallazgo del HHI
específicamente, sin insinuar que contradice o reemplaza el hallazgo de prevalencia.
Ambos gráficos (este y el de prevalencia de responsable principal por sexo) deben
presentarse juntos en el dashboard para evitar lectura parcial.

Archivo: `outputs/tableau/grafico1_hhi_por_sexo.png`.

## Paso 2.8 — Tasa de Afrontamiento Ciudadano (TAC), K/L/M/N (registrado 2026-08-20)

Sustituye al Índice de Silencio (eliminado por la Restricción B, Sección 0.3 — el
denominador de exposición no es observable porque `_6` agrupa "no presenció" con
"presenció y calló").

**Definición:** `afronto_X = 1[algún Xx404_1..5 == "Si"]` ⟺ `Xx404_6 == "No"`.
`TAC_X = Σ w·afronto_X / Σ w`, con `w = fexp_calp_anu`. Replicada para los 4 bloques
del 404: K (acoso sexual), L (violencia intrafamiliar), M (violencia contra la mujer),
N (violencia contra NNA).

**Resultados (n=13082):**

| Tipo | Descripción | n afronto | TAC ponderada | TAC sin ponderar | Esperado | Dif. (pp) |
|---|---|---|---|---|---|---|
| K | Acoso sexual | 2508 | 18.6% | 19.2% | 19.0% | -0.37 |
| L | Violencia intrafamiliar | 2183 | 16.7% | 16.7% | 16.6% | +0.14 |
| M | Violencia contra la mujer | 2474 | 18.8% | 18.9% | 18.8% | -0.02 |
| N | Violencia contra NNA | 1728 | 12.5% | 13.2% | 13.1% | -0.63 |


Todas las TAC ponderadas caen dentro de ±1 pp del valor esperado
para el total ciudad. Verificado.

**Nota de consistencia:** se replicó el chequeo del Paso 1.4 (afronto vía `_1..5` vs.
`_6=="No"`) para los 4 bloques. Total de filas inconsistentes en los 4 bloques:
67 — mismo orden de magnitud ya diagnosticado y documentado en el
Paso 1.4b para `M` (patrón sistemático de bajo nivel del instrumento, ~0,11%-0,15% por
bloque, sin patrón geográfico/temporal). No se recodifica aquí — `afronto_X` se calcula
directamente desde `_1..5`, que es la definición primaria del enunciado (`_6` es
derivada/consistencia, no la fuente de la variable).

**Ponderación:** a diferencia de los descriptivos crudos de la Fase 1 (Pasos 1.3, 1.4),
esta es la primera estimación de este proyecto que aplica `fexp_calp_anu` correctamente
como ponderación poblacional, siguiendo la regla operativa fijada en el Paso 1.6.

## Paso 2.8b — Análisis de sensibilidad TAC_A vs. TAC_B, K/L/M/N (registrado 2026-08-20)

**Resultado: diferencia de 0 en los cuatro bloques (K, L, M, N), en casos y en TAC ponderada.**

Esto NO significa que la ambigüedad de `_6` haya dejado de existir — significa que la
definición de `TAC_A` (= `afronto_X`) cambió entre el Paso 1.4b y el Paso 2.8, y por eso
esta comparación específica se volvió un no-op:

- **Paso 1.4b** (`TAC_A_original`, solo para M): definida como `Mx404_6 == "No"` —
  **basada en `_6`**. Bajo esa definición, los 17 casos ambiguos (`_6="Si"` + marca en
  `_1..5`) quedaban con `TAC_A=0`, y la recodificación a `TAC_B` sí producía una
  diferencia real de 17 casos.
- **Paso 2.8** (`afronto_X`, para K/L/M/N): definida directamente desde `_1..5`
  (`any(Xx404_1..5 == "Si")`) — **basada en `_1..5`**, siguiendo la definición primaria
  del enunciado del Paso 2.8. Bajo esta definición, los casos ambiguos YA tienen
  `afronto=1` desde el origen (porque sí tienen marca en `_1..5`), así que "recodificarlos
  a 1" no cambia nada — de ahí la diferencia de 0 en los cuatro bloques.

**Conclusión correcta:** al fijar `_1..5` como fuente primaria de `TAC_A` (Paso 2.8), la
ambigüedad de `_6` deja de ser relevante para el cálculo de la TAC — se resuelve por
construcción, no por una decisión de sensibilidad. El análisis de sensibilidad de este
paso queda sin objeto bajo la definición vigente. Se mantiene la constancia de los 17/19/15/16
casos de no-exclusividad por bloque (documentados en el Paso 2.8 principal) como nota de
calidad del instrumento, pero no requiere tratamiento adicional porque no afecta el
cálculo de la TAC tal como está definida.

`TAC_B_{prefijo}` calculada en esta celda es idéntica a `TAC_A_{prefijo}` en los
cuatro bloques y puede eliminarse del dataframe sin pérdida de información.

## Paso 2.9 — Interpretación y límites de la TAC (registrado 2026-08-20)

**Advertencia estructural:** `TAC_X` mide simultáneamente dos fenómenos que no se pueden
separar con los datos disponibles:
1. Cuánta violencia de tipo X ocurre y es **visible** para terceros (exposición).
2. De la violencia visible, cuánta **provoca una acción** de quien la presencia (afrontamiento).

Una TAC baja en una localidad puede deberse a poca violencia visible, a poca disposición
a actuar, o a ambas — el indicador no permite distinguir cuál de las dos domina.

**Reglas de redacción obligatorias para el informe y el dashboard:**

1. **`TAC` se usa exclusivamente como cota inferior de la exposición, nunca como
   estimación puntual.** No se reporta como "la tasa de violencia contra la mujer en la
   localidad X es Y%" — eso confundiría el numerador (afrontamiento) con el fenómeno
   completo (violencia total, incluida la no presenciada o presenciada-y-callada, que
   por diseño no es observable — Restricción B, Sección 0.3).

2. **Toda afirmación cuantitativa se redacta en la forma:**
   > *"Al menos X% de la población de [localidad] presenció y afrontó una situación de
   > violencia contra una mujer [en el periodo de referencia]."*

   Nunca se omite "al menos" ni "y afrontó" — ambas piezas son necesarias para que la
   frase sea metodológicamente correcta.

3. **Nunca se afirma que una localidad "tiene más violencia" a partir de `TAC`.** La
   redacción correcta es que la localidad **tiene más violencia socialmente visible y
   afrontada** — la diferencia no es cosmética: una localidad con TAC alta podría tener
   más violencia real, o simplemente más disposición ciudadana a actuar ante lo que ve
   (que es justamente lo que H-B busca explicar, vía `ICG_B` y la norma de no-injerencia).
   Interpretar TAC como proxy directo de prevalencia invalidaría la lógica completa de
   H-B, que depende de que TAC capture algo distinto (o adicional) a la prevalencia bruta.

**Consecuencia para los índices de la Fase 4 (RC_real, INA, etc.):** cualquier indicador
posterior que use `TAC` como insumo del "denominador de necesidad real" hereda esta misma
limitación y debe propagarla en su propia documentación — no se puede purificar la
ambigüedad de TAC agregándola en un índice compuesto.

**Aplicación práctica:** esta regla ya afecta la redacción de los resultados del Paso 2.8
— la tabla de TAC por bloque (K/L/M/N) reportada ahí debe leerse, comunicarse y citarse
siempre con la fórmula de "al menos X%", nunca como una tasa de prevalencia directa.

## Paso 2.10 — Afrontamiento comparado entre tipos de violencia (registrado 2026-08-20)

**Jerarquía a nivel ciudad (TAC ponderada):** M (18,8%) > K (18,6%) > L (16,7%) > N (12,5%).

**Nota de calibración respecto a la expectativa del enunciado:** el texto original de
este paso anticipaba K (acoso sexual) como el bloque de mayor afrontamiento. El cálculo
ponderado real muestra M y K prácticamente empatados (18,8% vs. 18,6%, diferencia de
0,2 pp) — M queda marginalmente por encima. Dada la magnitud de la diferencia, se trata
como un **empate estadístico entre K y M en el primer lugar**, no como una jerarquía
estricta de 4 niveles distintos. Lo que sí es inequívoco y consistente con lo esperado:
**N (violencia contra NNA) tiene el afrontamiento más bajo, con margen claro (12,5%,
~4-6 pp por debajo de los otros tres)**.

**Estabilidad por localidad:**
- La jerarquía completa (4 bloques en el mismo orden que ciudad) solo se replica en
  **3 de 19 localidades** — el orden intermedio (K vs. M vs. L) varía considerablemente
  entre localidades.
- **K es el máximo en 11 de 19 localidades**; en las demás, M toma su lugar en el primer
  puesto (Usme, La Candelaria, Rafael Uribe Uribe, Ciudad Bolívar, San Cristóbal parcial).
- **N es el mínimo en 18 de 19 localidades** — la única excepción es Barrios Unidos
  (jerarquía K,N,M,L, donde N ocupa el segundo lugar, no el último).

**Distribución de jerarquías observadas:**

| Jerarquía | n localidades |
|---|---|
| K, M, L, N | 9 |
| M, K, L, N | 3 |
| M, L, K, N | 3 |
| L, M, K, N | 2 |
| K, L, M, N | 1 |
| K, N, M, L | 1 |

**Interpretación (sujeta a la regla del Paso 2.9 — TAC como cota inferior, nunca
prevalencia directa):** el hallazgo robusto y generalizable de este paso es el **extremo
inferior**: la violencia contra niños, niñas y adolescentes tiene sistemáticamente el
menor afrontamiento ciudadano de los cuatro tipos medidos, casi sin excepción territorial
(18/19 localidades). El **extremo superior es más frágil**: la competencia entre acoso
sexual (K) y violencia contra la mujer (M) por el primer lugar varía según la localidad,
y a nivel ciudad es esencialmente un empate — no debe presentarse en el informe como
"el acoso sexual es el tipo de violencia más afrontado" sin la salvedad de que M está
prácticamente a la par.

**Tabla completa por localidad:** ver `tac_por_localidad` en el notebook / exportable a
`outputs/tableau/` si se decide incluir en el dashboard.

## Paso 2.11 — Espacio predominante de afrontamiento (registrado 2026-08-20)

**Nota metodológica obligatoria (respuesta múltiple):** normalizado sobre el **total de
marcas** (3217), no sobre personas (2474 afrontaron),
porque una misma persona puede señalar más de un espacio. Verificado exacto contra el
enunciado: 285/1.139/1.239/405/149.

**Distribución ciudad, bloque M:**

| Espacio | Marcas (ciudad) | % del total de marcas |
|---|---|---|
| Residencia | 285 | 8.9% |
| Barrio | 1139 | 35.4% |
| Otro espacio público | 1239 | 38.5% |
| Transporte | 405 | 12.6% |
| Trabajo | 149 | 4.6% |


**Hallazgo de política — la residencia NO es el espacio predominante en ninguna
localidad.** El espacio predominante por localidad se distribuye así:
- Otro espacio público: 14 localidades
- Barrio: 4 localidades
- Transporte: 1 localidades

En las 19 localidades, "Otro espacio público" o "Barrio" dominan sobre "Residencia"
— incluso en la localidad con mayor proporción residencial (Ciudad Bolívar,
17.2%), el espacio público sigue siendo más frecuente. Esto tiene una
implicación directa de política: **la ruta de atención no puede diseñarse principalmente
como intervención domiciliaria** — la mayoría del afrontamiento reportado ocurre en
barrio y espacio público abierto, seguido de transporte, con residencia y trabajo como
las categorías menos marcadas en todas las localidades.

**Advertencia de tamaño muestral:** localidades con menos de 20 marcas
totales (La Candelaria=29, Antonio Nariño=50, Tunjuelito=75, Fontibón=78, Barrios
Unidos=71, Los Mártires=96, Teusaquillo=93) tienen lectura frágil al desagregar en 5
categorías — un solo caso puede mover varios puntos porcentuales. Se recomienda no
sobreinterpretar diferencias finas entre estas localidades específicamente.

**Gráfico 2 (dashboard):** `outputs/tableau/grafico2_espacio_afrontamiento_M.png`.

## Paso 2.12 — Verificación de escalas continuas (IPSJ_A/C/E, ICG_B) (registrado 2026-08-20)

Se verificaron rango [1,5] y conteo de válidos contra los valores documentados en la Fase 1
(diccionario de datos de `encuesta_percepcion_legible.csv`).

| Variable | n válidos | n nulos | n esperado | Coincide | Rango |
|---|---|---|---|---|---|
| IPSJ_C | 11904 | 1178 | 11904 | Sí | [1.0, 5.0] |
| IPSJ_A | 12460 | 622  | 12460 | Sí | [1.0, 5.0] |
| IPSJ_E | 12776 | 306  | 12776 | Sí | [1.0, 5.0] |
| ICG_B  | 12912 | 170  | 12912 | Sí | [1.0, 5.0] |


**Resultado: verificación exitosa en las 4 variables** — coinciden exactamente con los
conteos esperados (11.904 / 12.460 / 12.776 / 12.912) y todas están dentro del rango
[1,5] sin valores fuera de escala.

Estas cuatro variables ya vienen como escalas continuas nativas del CSV (no requieren
transformación de códigos a etiquetas, a diferencia de las variables categóricas del
resto del pipeline) — sus nulos ({"IPSJ_C": 1178, "IPSJ_A": 622, "IPSJ_E": 306, "ICG_B": 170})
corresponden a no respuesta / salto condicional en el cuestionario original, no a un
problema de limpieza. Se conservan como `NaN` y se excluyen fila por fila (`.dropna()`)
en cualquier modelo o correlación que las use, sin imputación.

**Variable dependiente principal de H-A (según Sección 0.4):** `IPSJ_C` — la de mayor
tasa de no respuesta (1.178, 9,0%) entre las cuatro, lo cual debe tenerse presente al
reportar el n efectivo de cualquier modelo que la use como variable dependiente.

## Paso 2.13 — Índice de Barrera de Acceso, IBA (registrado 2026-08-20)

**Alfa de Cronbach** sobre `IPSJ_A`, `IPSJ_C`, `IPSJ_E` (listwise, n=11.361 filas con los
3 ítems presentes): **0,6155**.

**Umbral de decisión:** 0,60. Alfa por encima del umbral (0,6155 > 0,60), aunque por un
margen estrecho (0,0155) — se promedia según la regla del paso, pero se documenta el
margen ajustado.

**Método construido:** `IBA = -(z(IPSJ_A) + z(IPSJ_C) + z(IPSJ_E)) / 3`, calculado
únicamente sobre las 11.361 filas con los 3 componentes presentes simultáneamente (no se
promedia sobre subconjuntos parciales de ítems fila por fila).

**Distribución de IBA (n=11.361):**
- Media: -0,011 · Desviación estándar: 0,752
- Mediana: -0,061 · Rango intercuartílico: [-0,499, 0,500]
- Rango: [-2,520, 1,506]

**n válidos:** 11.361 de 13.082 (86,8%). La pérdida de 1.721 filas (13,2%) respecto al
total de la encuesta se debe a exigir los 3 componentes simultáneamente presentes
(listwise deletion) — mayor que la pérdida de cualquier componente individual
(`IPSJ_C` sola: 1.178 nulos; `IPSJ_A`: 622; `IPSJ_E`: 306), porque la exigencia conjunta
acumula los patrones de no respuesta de los tres ítems.

**Consecuencia para H-A:** el alfa de 0,6155 está apenas por encima del umbral mínimo
convencional de confiabilidad (0,60) — la consistencia interna entre los tres componentes
institucionales es aceptable pero no fuerte. Se recomienda reportar el IBA compuesto como
variable principal según lo indicado en este paso, pero acompañarlo de un análisis de
sensibilidad usando `IPSJ_C` sola (que no exige la triple presencia y por tanto conserva
más n, 11.904) para confirmar que los hallazgos de H-A no dependen de la construcción
compuesta ni de la reducción de muestra por listwise deletion.

## Paso 2.14 — Validación interna de H-B: TAC_M vs. ICG_B (registrado 2026-08-20)

**Resultado: signo NEGATIVO en ambos niveles — contrario a lo esperado por H-B.**

- **Nivel individual** (afronto_M vs. ICG_B, n=12.912): r = **-0,0486**. Correlación
  débil pero de signo negativo.
- **Nivel localidad** (TAC_M ponderada vs. ICG_B promedio ponderado, n=19 localidades):
  r = **-0,4606**. Correlación moderada, también negativa.

**Interpretación:** la hipótesis H-B esperaba que la Tasa de Afrontamiento Ciudadano
correlacionara *positivamente* con la confianza en los vecinos (`ICG_B`), como evidencia
de que la norma de no-injerencia (y no el machismo general) explica la inacción social
frente a la violencia. El resultado observado es el opuesto: **las localidades con menor
confianza vecinal promedio tienden a tener MAYOR afrontamiento** (ej. Los Mártires y
Santa Fe, las de menor ICG_B, están entre las de mayor TAC_M; Teusaquillo, la de mayor
ICG_B, tiene TAC_M intermedio-alto pero no la más alta).

**Consecuencia declarada de antemano (Sección 0.5 — Hipótesis normativa H-B):** el
enunciado original de H-B especificaba: *"Validación interna: la Tasa de Afrontamiento
Ciudadano debe correlacionar positivamente con `ICG_B` dentro de la propia Encuesta de
Percepción."* Este criterio de validación **no se cumple** — la correlación es negativa
en ambos niveles de agregación. Bajo el criterio de refutación declarado explícitamente
en el diseño del proyecto, este resultado **debilita la validación interna de H-B desde
la propia Encuesta de Percepción**.

**Lo que esto NO significa por sí solo:** no refuta H-B en su totalidad — la hipótesis
normativa completa depende también del análisis factorial de la Bienal (distinguir
roles tradicionales de no-injerencia/privatización, ítems P10.x/P12.x), que aún no se ha
realizado. Es posible que `ICG_B` ("confío en que mis vecinos me ayudarían ante cualquier
problema") no sea un proxy adecuado de la norma específica de no-injerencia frente a
violencia de pareja — son constructos relacionados pero no idénticos: una localidad puede
tener alta confianza vecinal general y aun así sostener la norma de "no meterse" en
asuntos de pareja específicamente, lo cual invalidaría el supuesto de que ambos
correlacionan.

**Hipótesis alternativa a explorar:** la correlación negativa podría explicarse por
un factor de confusión territorial — localidades con menor confianza vecinal e ingreso
más bajo podrían tener también más violencia visible en espacios públicos/compartidos
(ver Paso 2.11: predominancia de "Barrio"/"Otro espacio público" sobre "Residencia" en
TODAS las localidades), lo que mecánicamente eleva las oportunidades de presenciar y
por tanto de afrontar, independientemente de la norma de no-injerencia. Esto no se
verifica en este paso — requeriría controlar por exposición/densidad poblacional en un
modelo multivariado (Fase 3).

**Decisión metodológica:** se mantiene la documentación transparente de este resultado
como parte del reporte de H-B, en vez de omitirlo o buscar una recodificación que
produzca el signo esperado. La validación cruzada con el análisis factorial de la Bienal
(pendiente) será determinante para la evaluación final de H-B — este resultado individual
NO se trata como la prueba definitiva ni en un sentido ni en el otro.

## Paso 2.15 — Variables de control y mediadores (registrado 2026-08-20)

Se recodificaron las variables de control y mediadores usando `diccionario_mapeo.py` para los mapeos inversos (etiqueta → código). Todas las distribuciones coinciden con las documentadas en la Fase 1.

**1. GAD-7 (`ind_salud_102`) → ordinal `GAD7_ordinal` (0–3)**
- 0: No se aprecia ansiedad → 10.440 (79,8%)
- 1: Síntomas leves → 1.876 (14,3%)
- 2: Síntomas moderados → 588 (4,5%)
- 3: Síntomas severos → 178 (1,4%)

**2. Pobreza subjetiva (`C303`) → binaria `pobreza_subjetiva` (1=Si)**
- 1: Sí → 2.241 (17,1%)
- 0: No → 10.841 (82,9%)

**3. Estrato (`H1`) → categórica `estrato_cat` (agrupado 5-6)**
- Estrato 1: 1.327 (10,1%)
- Estrato 2: 5.355 (40,9%)
- Estrato 3: 4.540 (34,7%)
- Estrato 4: 1.448 (11,1%)
- Estrato 5-6: 379 (2,9%) — agrupado para evitar celdas vacías
- Sin servicio / No informa: 33 (0,3%)

**4. Edad (`A6x3`) y edad²**
- Rango: 18–99, media: 49,6 años. Se incluye `edad` y `edad_cuadrado` en los modelos para capturar no linealidad.

**5. Tamaño del hogar (`A3`), menores de 18 (`A4`), adultos (`A5`)**
- `A3`: media 2,57, rango [1, 12]
- `A4`: media 0,54, rango [0, 7]
- `A5`: media 2,03, rango [1, 9]

**6. Impacto de la distribución de tareas (`ind_distribuciontareas_202`) → ordinal `distribucion_tareas_ord` (1–3)**
- 1: Impacto positivo → 10.819 (82,7%)
- 2: Impacto neutro → 1.250 (9,6%)
- 3: Impacto negativo → 1.013 (7,7%)

---

**Verificación de índices construidos en la Fase 2** — todos dentro del rango teórico esperado:

| Índice | n válidos | media | min | max | Rango OK |
|--------|-----------|-------|-----|-----|----------|
| HHI    | 13.022    | 0.6955 | 0.1837 | 1.0000 | [0,1] |
| ICC_mujer | 13.022 | 0.2507 | 0.0000 | 1.0000 | [0,1] |
| ICD    | 6.517     | 0.3161 | 0.0000 | 1.0000 | [0,1] |
| IBA    | 11.361    | -0.0114 | -2.5203 | 1.5062 | valores z (~[-3,3]) |
| afronto_M | 13.082 | 0.1891 | 0 | 1 | - |
| afronto_K | 13.082 | 0.1917 | 0 | 1 | - |
| afronto_L | 13.082 | 0.1669 | 0 | 1 | - |
| afronto_N | 13.082 | 0.1321 | 0 | 1 | - |

**Nota metodológica:** los mapeos inversos se obtuvieron automáticamente desde `VALUE_MAPS` de `diccionario_mapeo.py`, evitando definiciones manuales y asegurando consistencia con el resto del pipeline.

**Consecuencia:** todas las variables de control y mediadores quedan correctamente tipadas y listas para su uso en los modelos de la Fase 3. Ningún índice tiene valores fuera de rango teórico.

## Paso 3.1 — Chequeo go/no-go para modelación de victimización directa (registrado 2026-08-20)

`Jx402` (víctima de violencia intrafamiliar en el último año) tiene **24 casos positivos** de 13.082 encuestados (0,18%).

El umbral mínimo establecido en el diseño (150 casos) **no se alcanza**.

**Consecuencia:** los modelos de regresión logística con `Jx402` o `Jx403` como variable dependiente **quedan descartados**. El análisis de la Fase 3 procede exclusivamente por la **rama alternativa**:

- **Variable dependiente principal:** `IPSJ_C` (percepción de acceso a medios para denunciar) → usada en modelos de regresión lineal para H-A.
- **Variable dependiente alternativa:** `afronto_M` (TAC_M) → usada en modelos de regresión logística para H-A.

**Justificación:** esta decisión ya fue documentada en el Paso 1.3 del notebook `01_preparacion.ipynb` y se mantiene aquí para asegurar trazabilidad en la Fase 3.

**Distribución de `Jx403` (¿denunció el delito?):**
- Sí: 17
- No: 7
- Total: 24 (coincide con los positivos de `Jx402`)

**Nota cualitativa (no inferencial):** de los 24 casos positivos, 17 denunciaron y 7 no. Esta cifra **no se usa como estimación poblacional** debido al sesgo de selección: quien admite violencia intrafamiliar ante un encuestador en su hogar es desproporcionadamente quien ya denunció. El 71% de denuncia observado en este subconjunto no refuta el subregistro — lo confirma por otra vía.

## Paso 3.2 — Modelo M1: barrera de acceso a la denuncia (IPSJ_C) y análisis de robustez (IBA)
**Fecha de ejecución:** 2026-08-20

### 1. Especificación del modelo

- **Variable dependiente principal:** `IPSJ_C` (acceso percibido a la información y medios para denunciar delitos, escala 1–5).  
- **Variable dependiente alternativa (robustez):** `IBA` = −(z(IPSJ_A)+z(IPSJ_C)+z(IPSJ_E))/3, construido solo sobre los 11.361 casos con los tres ítems presentes.  
- **Predictores de interés:**  
  - `ICC_mujer` (Índice de Concentración del Cuidado Femenino, continuo 0–1)  
  - `ICC_mujer_x_mujer` (interacción entre `ICC_mujer` y la variable binaria `es_mujer` = 1 si D1 == "Mujer")  
  - `HHI` (Índice de Herfindahl de concentración del cuidado general, continuo 0–1)  

- **Controles:** pobreza subjetiva (`pobreza_bin`), estrato (`estrato_modelo`), edad (`A6x3`) y su cuadrado, sexo (`D1`), sexo del jefe de hogar (`sexo_jefe`), GAD‑7 (`gad7_ord`), presencia de menores en el hogar (`A4`), y efectos fijos de `codigo_localidad`.

- **Diseño muestral:**  
  - Estimación ponderada con `fexp_calp_anu`.  
  - Errores estándar clusterizados por `codigo_UPL` (30 conglomerados) con corrección de muestras pequeñas (`use_correction=True`).  
  - Eliminación por listwise de cualquier fila con valores faltantes en las variables del modelo.

---

### 2. Resultados del modelo principal (dependiente = IPSJ_C)

- **Muestra analítica:** 11850 de 13.082 encuestados (pérdida del 9,4%).  
- **R²:** 0.0356 (el modelo explica una fracción muy pequeña de la varianza).

| Predictor | Coef. | IC 95% | p‑valor | p‑valor ajustado (BH) | Signo esperado | Signo observado | ¿Coincide? |
|-----------|-------|--------|---------|------------------------|----------------|-----------------|------------|
| ICC_mujer | -0.264 | [-0.410, -0.118] | 0.000406 | 0.000608 | Negativo | Negativo | Sí |
| ICC_mujer_x_mujer | 0.178 | [0.032, 0.324] | 0.017238 | 0.017238 | Negativo | Positivo | No |
| HHI | 0.266 | [0.139, 0.393] | 0.000043 | 0.000128 | Negativo | Positivo | No |


- **Corrección de Benjamini‑Hochberg:** aplicada a los tres p‑valores con α = 0.05. Todos son significativos tras la corrección.

**Interpretación de los predictores de interés:**

1. **`ICC_mujer`** (β = -0.264, p‑ajustado = 0.000608):  
   Por cada aumento unitario en la concentración femenina del cuidado, el acceso percibido a la denuncia **disminuye** en 0.26 puntos en la escala 1–5. **El signo es el esperado** y es estadísticamente significativo.

2. **`ICC_mujer_x_mujer`** (β = 0.178, p‑ajustado = 0.017238):  
   La interacción es **positiva**. Esto implica que el efecto negativo de `ICC_mujer` se **atenúa** cuando la persona encuestada es mujer, en lugar de intensificarse como predecía la hipótesis. **El signo es contrario al esperado**.

3. **`HHI`** (β = 0.266, p‑ajustado = 0.000128):  
   La concentración general del cuidado (independientemente del sexo de quien lo realiza) se asocia con **mayor** acceso a la denuncia. **El signo es contrario al esperado** (la hipótesis anticipaba que una mayor concentración → mayor barrera).

---

### 3. Análisis de robustez con IBA

Para verificar si el resultado depende de la definición de "barrera de acceso", se reestimó el mismo modelo usando `IBA` como variable dependiente.

- **Muestra analítica:** 11307 (pérdida adicional por listwise sobre ítems `IPSJ_A`, `IPSJ_C`, `IPSJ_E`).  

| Predictor | Coef. (IBA) | p‑valor (IBA) | Significativo (α=0.05) |
|-----------|-------------|---------------|------------------------|
| ICC_mujer | 0.096 | 0.171 | No |
| ICC_mujer_x_mujer | -0.066 | 0.337 | No |
| HHI | -0.229 | 0.000 | Sí |


**Comparación de signos entre especificaciones:**

| Predictor | Signo (IPSJ_C) | Signo (IBA) | ¿Coinciden? |
|-----------|----------------|-------------|-------------|
| ICC_mujer | Negativo | Positivo | No |
| ICC_mujer_x_mujer | Positivo | Negativo | No |
| HHI | Positivo | Negativo | No |


---

### 4. Conclusión sobre H‑A

La hipótesis H‑A establecía que:

> *"La concentración femenina del cuidado se asocia con menor acceso percibido a la denuncia, y este efecto es más fuerte entre las mujeres."*

**Evaluación según criterios preregistrados (Sección 1.3 y 1.4):**

- **Criterio de significancia:** `ICC_mujer` es significativa en el modelo principal (p‑ajustado < 0.05). Por lo tanto, **no se refuta formalmente** la hipótesis.
- **Criterio de coherencia teórica:** la interacción `ICC_mujer_x_mujer` tiene signo **positivo** (opuesto al esperado), y `HHI` también. Esto indica que el mecanismo propuesto (un efecto específico y agravado para las mujeres) **no se sostiene**.
- **Criterio de robustez:** al cambiar la variable dependiente a `IBA`, los signos de los tres predictores de interés **se invierten** y los dos primeros pierden significancia. El resultado es **frágil**.

**Declaración final:**  
El modelo M1 proporciona evidencia **débil y parcial** para H‑A. La asociación negativa entre `ICC_mujer` e `IPSJ_C` es estadísticamente significativa y con el signo esperado, pero la interacción con el sexo no respalda el mecanismo hipotetizado, y el hallazgo no es robusto al usar una definición alternativa de la variable dependiente.  
En la sustentación se presentará como un **resultado mixto** que no permite confirmar la hipótesis de forma concluyente, y se señalarán las limitaciones (bajo R², sesgo de selección por la construcción de `ICC_mujer`, y baja consistencia interna de `IBA`).


## Paso 3.3 — Modelo M2: afrontamiento de violencia presenciada (afronto_M, logístico) (registrado 2026-08-20)

### Especificación

Misma estructura de controles y diseño muestral que M1 (Paso 3.2): ponderación
`fexp_calp_anu`, efectos fijos de `codigo_localidad`, listwise deletion.

- **Muestra analítica:** 13.022 de 13.082 (pérdida 0,5% — mínima, porque `afronto_M` no
  tiene la pérdida de nulos que sí tienen `IPSJ_C`/`IBA`).
- **Positivos:** 2.460 (18,89%) — consistente con la TAC_M reportada en el Paso 2.8.
- **Pseudo-R² (McFadden):** 0,0750.

### Validación de robustez del error estándar (tres métodos)

Se corrió el modelo con tres estrategias de ponderación/inferencia, dado que
`statsmodels` advirtió que `cov_type='cluster'` no está totalmente soportado con
`var_weights`:

| Método | Coef. idénticos a los otros | SE | Estado |
|---|---|---|---|
| `var_weights` (original) | — | 0,228 / 0,278 / 0,158 | Warning de statsmodels |
| `freq_weights` (corregido) | Sí, exactos | 0,228 / 0,278 / 0,158 | cov_type totalmente soportado |
| Bootstrap por conglomerado UPL (500 réplicas, 0 fallidas) | Sí, exactos | 0,242 / 0,283 / 0,147 | **Método definitivo** |

**Los tres métodos convergen en los mismos coeficientes puntuales**, y los errores
estándar por bootstrap (el método sin supuestos asintóticos sobre el manejo de pesos)
son muy cercanos a los analíticos — confirma que el warning de statsmodels no ocultaba
un problema sustantivo. Se reportan los resultados del bootstrap como definitivos.

### Resultados (bootstrap, definitivos)

| Predictor | Coef. | OR | IC 95% | p (BH) | Signo esperado (Sección 1.1) | Signo observado | ¿Coincide? |
|---|---|---|---|---|---|---|---|
| `ICC_mujer` | 0,017 | 1,017 | [-0,456, 0,491] | 0,943 | No declarado explícitamente para el efecto principal | Positivo, nulo | N/A |
| `ICC_mujer_x_mujer` | 0,183 | 1,201 | [-0,371, 0,737] | 0,777 | **Negativo (OR<1)** | Positivo (OR>1) | **No** |
| `HHI` | -0,284 | 0,752 | [-0,573, 0,004] | 0,161 | No declarado explícitamente | Negativo | N/A |

**Ninguno de los tres predictores es significativo tras corrección Benjamini-Hochberg**
(α=0,05). `HHI` es el más cercano (p_ajustado=0,161), con un IC 95% que casi excluye el
0 pero no lo logra (límite superior 0,004).

### Evaluación de H-A (M2) según criterios preregistrados

> H-A (M2): *"...y con menor probabilidad de afrontar violencia presenciada"*, predictor
> de interés `ICC_mujer × D1`, signo esperado **OR < 1**.

- **Criterio de significancia:** la interacción `ICC_mujer_x_mujer` **no es significativa**
  tras BH (p_ajustado=0,777). Bajo el criterio preregistrado (Sección 1.4, escenario 2),
  esto es evidencia que **no soporta** H-A (M2).
- **Criterio de coherencia teórica:** aun ignorando la significancia, el signo observado
  de la interacción es **positivo** (OR=1,201) — opuesto al esperado (OR<1). No hay
  ninguna lectura del coeficiente puntual que respalde el mecanismo hipotetizado.
- **Consistencia con M1:** en el Paso 3.2, la misma interacción (`ICC_mujer_x_mujer`)
  sobre `IPSJ_C` también arrojó signo positivo (contrario a lo esperado), aunque en ese
  caso sí alcanzaba significancia. Aquí, ni siquiera hay significancia. **Los dos modelos
  de H-A (M1 y M2) coinciden en el mismo signo contrario a la hipótesis para la
  interacción con sexo** — no es un resultado aislado de una sola especificación.

### Declaración final — H-A (M2)

**No se encuentra evidencia que soporte H-A (M2).** La interacción `ICC_mujer × D1` no
es estadísticamente significativa sobre la probabilidad de afrontamiento de violencia
presenciada, y el signo puntual observado es opuesto al hipotetizado. Combinado con el
resultado de M1 (mixto, con la misma interacción de signo contrario), el patrón
consistente entre ambos modelos sugiere que **el mecanismo específico de "mujeres
sobrecargadas de cuidado tienen particularmente menor acceso/afrontamiento" no encuentra
sustento empírico en esta base**, más allá del efecto principal débil y no consistentemente
robusto de `ICC_mujer` documentado en M1.

Este resultado se reportará en la sustentación como parte de la evaluación conjunta de
H-A (M1+M2): evidencia débil, parcial y no robusta para el efecto principal, y ausencia
de evidencia — con signo contrario — para el mecanismo de interacción con sexo que era
el componente central de la hipótesis.

## Paso 3.4 — Modelo M3: no-injerencia / confianza vecinal (ICG_B) (registrado 2026-08-20)

### Especificación

Dependiente `ICG_B` (confianza en que los vecinos ayudarían), mismos regresores de
M1/M2 (`ICC_mujer`, `ICC_mujer_x_mujer`, `HHI`) más `TAC_M_localidad` (TAC del bloque M
agregada por `codigo_localidad`, ponderada por `fexp_calp_anu`) — variable de nivel
localidad incorporada al modelo de nivel individuo, con errores estándar clusterizados
por `codigo_UPL` (anidado dentro de localidad).

- **Muestra analítica:** 12.854 de 13.082 (pérdida 1,7%).
- **R²:** 0,0357 — del mismo orden de magnitud que M1 (0,0356), bajo poder explicativo
  general, consistente con el resto de los modelos de esta fase.

### Resultados

| Predictor | Coef. | IC 95% | p (BH) | Significativo (BH, α=0,05) |
|---|---|---|---|---|
| `ICC_mujer` | -0,051 | [-0,225, 0,124] | 0,570 | No |
| `ICC_mujer_x_mujer` | 0,069 | [-0,115, 0,253] | 0,570 | No |
| `HHI` | 0,065 | [-0,046, 0,175] | 0,500 | No |
| `TAC_M_localidad` | 0,245 | [0,016, 0,475] | 0,145 | No (tras BH) |

**Ningún predictor es significativo tras corrección Benjamini-Hochberg.**
`TAC_M_localidad` es el más cercano a significancia individual (p sin ajustar = 0,036),
pero **no sobrevive** la corrección por comparaciones múltiples (p_ajustado = 0,145) — el
mismo patrón de fragilidad que se ha visto en M1 y M2: señales que aparecen sueltas pero
se diluyen al corregir por las pruebas simultáneas.

### Evaluación del rol de `ICG_B`: ¿mediador o dimensión independiente?

El enunciado plantea la pregunta central: ¿la confianza vecinal es un mediador entre la
carga de cuidado y el afrontamiento, o una dimensión independiente?

**Ni `ICC_mujer` ni `HHI` predicen `ICG_B` de forma significativa** (p_ajustado 0,570 y
0,500 respectivamente). Para que `ICG_B` funcionara como mediador de la relación entre
carga de cuidado y afrontamiento, tendría que existir asociación significativa entre la
carga de cuidado (`ICC_mujer`/`HHI`) y `ICG_B` como primer eslabón de la cadena causal —
ese eslabón **no aparece** en los datos.

**`TAC_M_localidad` sí tiene el signo positivo esperado y es la más cercana a
significancia** (coef=0,245, p sin ajustar 0,036), consistente con la idea de que
localidades con mayor afrontamiento ciudadano tienden a tener mayor confianza vecinal.
Sin embargo, esta correlación positiva contrasta directamente con el resultado del
**Paso 2.14** (validación interna de H-B), donde `TAC_M` vs. `ICG_B` agregada por
localidad arrojó **r = -0,4606 (negativo)**. La aparente contradicción se explica porque
el Paso 2.14 es una correlación bivariada simple a nivel localidad (n=19), mientras que
este modelo evalúa el coeficiente de `TAC_M_localidad` **controlando** por `ICC_mujer`,
`HHI`, pobreza, estrato, edad, sexo, salud mental, tamaño del hogar y efectos fijos de
localidad — el signo puede revertirse al introducir controles si existe confusión
territorial no controlada en la correlación simple (la misma hipótesis de confusión que
se dejó planteada, sin verificar, en el Paso 2.14).

### Declaración final — Modelo M3

**No hay evidencia de que `ICG_B` medie la relación entre carga de cuidado y
afrontamiento**: el primer eslabón de la cadena (carga de cuidado → confianza vecinal)
no es significativo bajo ningún indicador de carga (`ICC_mujer`, su interacción, o
`HHI`). Esto es consistente con la conclusión de M1/M2: el mecanismo específico de
carga de cuidado → barrera de acceso/afrontamiento, mediado o no por confianza vecinal,
**no encuentra sustento robusto en esta base tras controlar por comparaciones múltiples**.

El hallazgo más interesante de este modelo es metodológico, no confirmatorio: el signo
de la relación `TAC_M` ↔ `ICG_B` **se revierte** entre la correlación bivariada simple
por localidad (Paso 2.14, negativa) y el coeficiente multivariado controlado (Paso 3.4,
positivo, aunque no significativo tras BH) — evidencia de que la relación bivariada
simple estaba probablemente confundida por factores territoriales no controlados
(estrato, pobreza, tamaño de muestra por localidad), reforzando la recomendación ya
dejada en el Paso 2.14 de no usar esa correlación simple como prueba definitiva de H-B.

**Consecuencia para la síntesis de H-A y H-B:** ninguno de los tres modelos (M1, M2, M3)
provee evidencia robusta y consistente que sobreviva la corrección por comparaciones
múltiples para el mecanismo específico planteado en H-A. La validación interna de H-B vía
`ICG_B` queda en un estado ambiguo: negativa en la correlación simple, positiva pero no
significativa en el modelo controlado. La evaluación final de H-B queda pendiente del
análisis factorial de la Bienal (ítems P10.x/P12.x), que es la pieza de evidencia
preregistrada como decisiva para esta hipótesis (Sección 1.4, escenario 3).

## Paso 3.5 — Modelo M4: robustez con acoso sexual (K) y violencia intrafamiliar (L) (registrado 2026-08-20)

### Especificación

Réplica exacta de M2, cambiando la variable dependiente por `afronto_K` (acoso sexual) y
`afronto_L` (violencia intrafamiliar), manteniendo los mismos regresores, ponderación y
diseño muestral.

**Nota técnica:** igual que en M2 original, aparece el warning de `statsmodels` sobre
`cov_type` no completamente soportado con `freq_weights`. En M2 este warning se resolvió
mediante bootstrap por conglomerado (500 réplicas, coeficientes idénticos, SE muy
similares a los analíticos) — no se repitió el bootstrap para K y L por economía de
cómputo, dado que ya se validó en la misma estructura de datos y modelo que el efecto del
warning es despreciable. Se reportan los SE analíticos con esta salvedad explícita.

### Resultados

| Predictor | K — Acoso sexual (coef / OR / p_BH) | L — Violencia intrafamiliar (coef / OR / p_BH) |
|---|---|---|
| `ICC_mujer` | -0,016 / 0,984 / 0,943 | 0,316 / 1,371 / 0,288 |
| `ICC_mujer_x_mujer` | 0,179 / 1,196 / 0,716 | -0,024 / 0,976 / 0,936 |
| `HHI` | 0,172 / 1,187 / 0,716 | -0,196 / 0,822 / 0,288 |

- **K:** n=13.022, positivos 2.487 (19,10%), pseudo-R²=0,0663.
- **L:** n=13.022, positivos 2.172 (16,68%), pseudo-R²=0,0825.

**Ningún predictor es significativo tras corrección BH en ninguno de los dos modelos.**

### Comparación de la interacción `ICC_mujer × D1` entre los tres tipos de violencia

| Tipo | Coef. | OR | p (BH) |
|---|---|---|---|
| M — Violencia contra la mujer (Paso 3.3) | 0,183 | 1,201 | 0,777 |
| K — Acoso sexual | 0,179 | 1,196 | 0,716 |
| L — Violencia intrafamiliar | -0,024 | 0,976 | 0,936 |

### Interpretación: ¿patrón general o específico?

Siguiendo el criterio planteado en el enunciado (general vs. específico), el resultado es
matizado, no un caso limpio de ninguno de los dos extremos:

1. **M y K son prácticamente indistinguibles entre sí**: coeficiente e IC prácticamente
   idénticos (0,183 vs. 0,179; OR 1,201 vs. 1,196), ambos no significativos, mismo signo
   positivo (contrario al esperado en ambos casos). Si el mecanismo fuera específico de
   violencia contra la mujer, se esperaría que K se comportara distinto a M — no ocurre.

2. **L se comporta de forma distinta a M y K**: coeficiente esencialmente nulo (-0,024,
   OR≈0,976, prácticamente 1) y de signo contrario a M/K, aunque tampoco significativo.

3. **Ninguno de los tres coeficientes de interacción alcanza significancia** tras BH —
   por lo que, en sentido estricto, **no hay evidencia estadística de un efecto real en
   ninguno de los tres tipos de violencia**, y la comparación de patrones entre M/K/L
   debe leerse como descriptiva de la dirección de los coeficientes puntuales, no como
   una diferencia estadísticamente probada entre tipos de violencia.

**Declaración final, siguiendo el espíritu del enunciado (decir cuál patrón se obtuvo es
más valioso que forzar una lectura):** el patrón observado es que **el mecanismo de
interacción `ICC_mujer × D1` no muestra evidencia significativa en ninguno de los tres
tipos de violencia** (M, K, L). Entre los coeficientes puntuales no significativos, M y K
comparten un signo y magnitud casi idénticos, mientras que L se aparta hacia un valor
cercano a cero. Esto es más consistente con **ausencia general de un efecto detectable**
con esta base y esta especificación, que con un patrón claro de retraimiento generalizado
o de especificidad hacia la violencia contra la mujer — ninguna de las dos lecturas
fuertes está respaldada por significancia estadística.

**Consecuencia para la síntesis de H-A:** el resultado de M4 refuerza la conclusión ya
alcanzada en M1/M2/M3: el mecanismo de interacción con sexo, que era la pieza central que
distinguía a H-A de una simple asociación descriptiva, **no encuentra sustento robusto en
ningún modelo de la Fase 3**, y esto se sostiene de forma consistente al variar la
variable dependiente entre los cuatro tipos de violencia disponibles (M, K, L) más el
modelo continuo (IPSJ_C, M1).

## Paso 3.6 — Reporte consolidado de resultados M1–M4 (registrado 2026-08-20)

### Advertencia técnica sobre los efectos marginales promedio (AME)

`get_margeff()` de statsmodels **no incorpora los pesos de ponderación** (`freq_weights`)
en el cálculo de AME para los tres modelos logísticos (M2, M4-K, M4-L) — warning explícito
de la librería: *"weights are not taken into account by margeff"*. Los coeficientes y OR
reportados **sí están correctamente ponderados** (provienen de `.fit()`); solo los AME de
la columna `ame` son una aproximación no ponderada. Se reportan de todas formas por su
valor interpretativo (facilitan la lectura para audiencia no técnica), pero con esta
salvedad explícita, y se prioriza el OR (correctamente ponderado) como cifra de referencia
en cualquier afirmación cuantitativa del informe.

### Tabla consolidada — modelos lineales (M1, M3)

| Modelo | Dependiente | Predictor | Coef. | IC 95% | p_valor | Efecto estandarizado | R² | N | N conglomerados |
|---|---|---|---|---|---|---|---|---|---|
| M1 | IPSJ_C | ICC_mujer | -0,264 | [-0,410, -0,118] | 0,000 | -0,084 | 0,0356 | 11.850 | 30 |
| M1 | IPSJ_C | ICC_mujer_x_mujer | 0,178 | [0,032, 0,324] | 0,017 | 0,053 | 0,0356 | 11.850 | 30 |
| M1 | IPSJ_C | HHI | 0,266 | [0,139, 0,393] | 0,000 | 0,061 | 0,0356 | 11.850 | 30 |
| M3 | ICG_B | ICC_mujer | -0,051 | [-0,225, 0,124] | 0,570 | -0,016 | 0,0357 | 12.854 | 30 |
| M3 | ICG_B | ICC_mujer_x_mujer | 0,069 | [-0,115, 0,253] | 0,464 | 0,020 | 0,0357 | 12.854 | 30 |
| M3 | ICG_B | HHI | 0,065 | [-0,046, 0,175] | 0,250 | 0,015 | 0,0357 | 12.854 | 30 |
| M3 | ICG_B | TAC_M_localidad | 0,245 | [0,016, 0,475] | 0,036 | 0,011 | 0,0357 | 12.854 | 30 |

**Lectura de efectos estandarizados (M1):** `ICC_mujer` tiene el mayor efecto relativo
(-0,084 desviaciones estándar de `IPSJ_C` por cada desviación estándar de `ICC_mujer`) de
los tres predictores de interés en M1 — mayor que `HHI` (0,061) o la interacción (0,053)
en valor absoluto, aunque las tres magnitudes son pequeñas en términos absolutos
(coherente con el R² bajo, 0,0356). En M3, todos los efectos estandarizados son aún
menores (máximo 0,020 en valor absoluto), consistente con la ausencia de significancia.

### Tabla consolidada — modelos logísticos (M2, M4)

| Modelo | Dependiente | Predictor | OR | IC 95% (OR) | p_valor | AME* | Pseudo-R² | N | N conglomerados |
|---|---|---|---|---|---|---|---|---|---|
| M2 | afronto_M | ICC_mujer | 1,017 | [0,650, 1,591] | 0,940 | 0,002 | 0,0750 | 13.022 | 30 |
| M2 | afronto_M | ICC_mujer_x_mujer | 1,201 | [0,696, 2,072] | 0,511 | 0,026 | 0,0750 | 13.022 | 30 |
| M2 | afronto_M | HHI | 0,752 | [0,553, 1,025] | 0,071 | -0,040 | 0,0750 | 13.022 | 30 |
| M4-K | afronto_K | ICC_mujer | 0,984 | [0,626, 1,546] | 0,943 | -0,002 | 0,0663 | 13.022 | 30 |
| M4-K | afronto_K | ICC_mujer_x_mujer | 1,196 | [0,730, 1,960] | 0,477 | 0,025 | 0,0663 | 13.022 | 30 |
| M4-K | afronto_K | HHI | 1,187 | [0,767, 1,838] | 0,442 | 0,024 | 0,0663 | 13.022 | 30 |
| M4-L | afronto_L | ICC_mujer | 1,371 | [0,853, 2,203] | 0,192 | 0,041 | 0,0825 | 13.022 | 30 |
| M4-L | afronto_L | ICC_mujer_x_mujer | 0,976 | [0,542, 1,758] | 0,936 | -0,003 | 0,0825 | 13.022 | 30 |
| M4-L | afronto_L | HHI | 0,822 | [0,615, 1,100] | 0,188 | -0,025 | 0,0825 | 13.022 | 30 |

*AME no ponderado — ver advertencia técnica arriba.

**Nota sobre p-valores en esta tabla consolidada:** se reportan los p-valores sin ajustar
por comparaciones múltiples, para consistencia visual con el OR/coef/IC de la misma fila.
Los p-valores ajustados por Benjamini-Hochberg (que son el criterio decisorio
preregistrado, Sección 1.3) ya se documentaron modelo por modelo en los Pasos 3.2–3.5;
ningún predictor de interés fue significativo bajo BH excepto `ICC_mujer` y
`ICC_mujer_x_mujer` en M1.

### Síntesis de sensibilidad y AME más informativos (lectura práctica)

Para traducir a lenguaje no técnico, tomando `HHI` en M2 como ejemplo (el más cercano a
significancia entre los modelos logísticos, aunque no significativo tras BH): un aumento
de HHI de 0 a 1 (mínima a máxima concentración) se asocia, en promedio y sin ajuste por
ponderación, con una reducción de 4 puntos porcentuales (AME=-0,040) en la probabilidad de
afrontamiento de violencia contra la mujer — coherente en dirección con el OR<1 (0,752),
pero esta cifra específica no está ponderada poblacionalmente y no alcanza significancia
estadística tras corrección por comparaciones múltiples.

### Cierre de la Fase 3 (modelos M1–M4)

La tabla consolidada confirma el patrón ya documentado modelo por modelo: **el único
resultado que sobrevive la corrección por comparaciones múltiples en toda la Fase 3 es el
efecto principal de `ICC_mujer` sobre `IPSJ_C` en M1** (p_ajustado=0,000608) y su
interacción con sexo en el mismo modelo (p_ajustado=0,017238, pero de signo contrario al
esperado). Ningún otro predictor de interés, en ningún otro modelo (M2, M3, M4-K, M4-L),
alcanza significancia tras BH. Esto se reporta en la sustentación como evidencia
**débil, parcial y no robusta** para H-A, consistente en todas sus piezas (M1 a M4) con la
conclusión ya alcanzada en los Pasos 3.2 a 3.5.

## Paso 3.7 — Corrección global de comparaciones múltiples, Fase 3 (registrado 2026-08-20)

Se aplicó Benjamini-Hochberg sobre las **16 pruebas** de coeficientes de interés de toda
la Fase 3 (M1, M2, M3, M4-K, M4-L) como una sola familia, en lugar de la corrección
aplicada modelo por modelo en los Pasos 3.2–3.5 (familias de 3–4 pruebas cada una). Esta
es la corrección metodológicamente más estricta y correcta cuando se van a comparar e
interpretar conjuntamente los resultados de varios modelos relacionados, como es el caso
aquí (todos evalúan la misma hipótesis H-A con las mismas variables de interés).

### Tabla completa (16 coeficientes)

| Modelo | Dependiente | Predictor | p | p_ajustado (global) | Signif. global | p_ajustado (local) | Signif. local | ¿Cambia? |
|---|---|---|---|---|---|---|---|---|
| M1 | IPSJ_C | ICC_mujer | 0,000 | 0,003 | **Sí** | 0,001 | Sí | No |
| M1 | IPSJ_C | ICC_mujer_x_mujer | 0,017 | 0,092 | **No** | 0,017 | Sí | **⚠️ Sí — pierde significancia** |
| M1 | IPSJ_C | HHI | 0,000 | 0,001 | **Sí** | 0,000 | Sí | No |
| M2 | afronto_M | ICC_mujer | 0,940 | 0,943 | No | 0,940 | No | No |
| M2 | afronto_M | ICC_mujer_x_mujer | 0,511 | 0,682 | No | 0,767 | No | No |
| M2 | afronto_M | HHI | 0,071 | 0,227 | No | 0,213 | No | No |
| M3 | ICG_B | ICC_mujer | 0,570 | 0,701 | No | 0,570 | No | No |
| M3 | ICG_B | ICC_mujer_x_mujer | 0,464 | 0,682 | No | 0,570 | No | No |
| M3 | ICG_B | HHI | 0,250 | 0,500 | No | 0,500 | No | No |
| M3 | ICG_B | TAC_M_localidad | 0,036 | 0,145 | No | 0,145 | No | No |
| M4-K | afronto_K | ICC_mujer | 0,943 | 0,943 | No | 0,943 | No | No |
| M4-K | afronto_K | ICC_mujer_x_mujer | 0,477 | 0,682 | No | 0,716 | No | No |
| M4-K | afronto_K | HHI | 0,442 | 0,682 | No | 0,716 | No | No |
| M4-L | afronto_L | ICC_mujer | 0,192 | 0,439 | No | 0,288 | No | No |
| M4-L | afronto_L | ICC_mujer_x_mujer | 0,936 | 0,943 | No | 0,936 | No | No |
| M4-L | afronto_L | HHI | 0,188 | 0,439 | No | 0,288 | No | No |

**Coeficientes significativos bajo corrección global: 2 de 16** (`ICC_mujer` y `HHI`,
ambos en M1 únicamente).

### Declaración explícita del cambio (requerida por el enunciado)

**`ICC_mujer_x_mujer` en M1 pierde significancia estadística al pasar de corrección
local a corrección global**: p_ajustado pasa de 0,017 (significativo, α=0,05) a 0,092
(no significativo). Este era precisamente el coeficiente que representaba el **mecanismo
central de H-A** — la interacción específica entre carga de cuidado y sexo — y era, hasta
este punto, el único elemento de todo H-A (M1, M2, M3, M4) que había sobrevivido alguna
forma de corrección por comparaciones múltiples con signo esperado (aunque, como ya se
documentó en el Paso 3.2, el signo observado de este coeficiente era **contrario** al
hipotetizado desde el principio).

**Consecuencia para H-A:** con la corrección más estricta y metodológicamente apropiada
para comparar los 5 modelos como un conjunto, **el único resultado que sobrevive en toda
la Fase 3 es el efecto principal de `ICC_mujer` y `HHI` sobre `IPSJ_C` en M1** — ambos
robustos incluso bajo la corrección global (p_ajustado 0,003 y 0,001 respectivamente).
Ningún componente de interacción con sexo, en ningún modelo, sobrevive la corrección
global. Esto refuerza — no cambia — la conclusión ya alcanzada en los Pasos 3.2 a 3.6:
**H-A no encuentra sustento para su mecanismo específico** (carga de cuidado
particularmente gravosa para mujeres), y el único hallazgo robusto es un efecto principal
de concentración del cuidado sobre percepción de acceso a la denuncia, sin distinción por
sexo del respondiente, y con el matiz adicional (Paso 3.2) de que `HHI` tiene signo
contrario al hipotetizado.

**Nota metodológica sobre por qué se reportan ambas correcciones:** la corrección local
(por modelo) es la que se preregistró explícitamente en la Sección 1.3 del documento de
supuestos (*"Significancia individual: p < 0,05 tras corrección Benjamini-Hochberg"*, sin
especificar el tamaño de la familia de pruebas). La corrección global aplicada aquí es una
verificación de robustez adicional, más conservadora, que se reporta con total
transparencia porque cambia la interpretación de un coeficiente — omitirla sería
inconsistente con el estándar de transparencia mantenido en toda la bitácora.

## Paso 3.8 — Robustez de β₁ (ICC_mujer) en M1, M2, M3: tres variantes (registrado 2026-08-20)

Se reestimaron M1, M2 y M3 bajo tres variantes: (a) sin ponderar por `fexp_calp_anu`;
(b) errores estándar clusterizados por `SectorUPL` (6 grupos) en vez de `codigo_UPL`
(30 grupos); (c) excluyendo las 3 localidades de menor n muestral (La Candelaria=17,
Los Mártires=14, Antonio Nariño=15 — códigos DANE confirmados contra `dim_localidad`).

**Nota técnica de corrección durante la ejecución:** la variante (c) inicialmente no
excluyó ninguna fila en M2 (0 de 13.022) porque `codigo_localidad` en `df_m2` está
tipado como `string` (asignación explícita en la celda original de M2), mientras que la
lista de códigos a excluir estaba en `int`. Corregido casteando la lista a string antes
de filtrar; tras la corrección, (c) excluye 629 filas en M2, consistente en orden de
magnitud con las exclusiones de M1 (589) y M3 (621).

### Resultados — β₁ = ICC_mujer, las tres variantes

| Variante | M1 (IPSJ_C) coef / p | M2 (afronto_M) coef / OR / p | M3 (ICG_B) coef / p |
|---|---|---|---|
| Original | -0,264 / 0,000 | 0,017 / 1,017 / 0,940 | -0,051 / 0,570 |
| (a) Sin ponderar | -0,183 / 0,007 | -0,225 / 0,799 / 0,278 | 0,007 / 0,929 |
| (b) Cluster SectorUPL (6 grupos) | -0,264 / 0,002 | 0,017 / 1,017 / 0,907 | -0,051 / 0,622 |
| (c) Excl. 3 localidades bajo-n | -0,266 / 0,000 | 0,026 / 1,026 / 0,912 | -0,062 / 0,479 |

### Evaluación de solidez (criterio del enunciado: signo consistente en las tres variantes)

**M1 — SÓLIDO.** El signo de β₁ (`ICC_mujer` sobre `IPSJ_C`) es **negativo en las cuatro
especificaciones** (original y las tres variantes de robustez), y mantiene significancia
en las cuatro (p entre 0,000 y 0,007). La magnitud es estable en (b) y (c) (-0,264 y
-0,266, prácticamente idéntica al original), y se atenúa pero no cambia de signo en (a)
sin ponderar (-0,183). **Este es el único de los tres modelos que pasa la prueba de
robustez tal como está definida en el enunciado.**

**M2 — NO SÓLIDO.** El signo de β₁ (`ICC_mujer` sobre `afronto_M`) **cambia entre
variantes**: positivo en el original, (b) y (c) (coef entre 0,017 y 0,026, OR≈1,02),
pero **negativo al no ponderar** (a): coef=-0,225, OR=0,799. Ninguna de las cuatro
especificaciones alcanza significancia (p entre 0,278 y 0,940) — el coeficiente no solo
es inestable en signo, sino que nunca es distinguible de cero. No se sostiene ningún
hallazgo de M2 bajo este criterio.

**M3 — NO SÓLIDO.** El signo de β₁ (`ICC_mujer` sobre `ICG_B`) también **cambia entre
variantes**: negativo en el original, (b) y (c) (coef entre -0,051 y -0,062), pero
**positivo al no ponderar** (a): coef=0,007. Igual que M2, ninguna especificación es
significativa (p entre 0,479 y 0,929).

### Declaración final del Paso 3.8

Bajo el criterio de robustez del enunciado (signo consistente en las tres variantes),
**solo M1 pasa la prueba**. M2 y M3 muestran inversión de signo específicamente al
remover la ponderación poblacional — el patrón es el mismo en ambos casos, lo que
sugiere que la ponderación por `fexp_calp_anu` está jugando un papel sustantivo en la
estimación de estos dos modelos (posiblemente porque da más peso a subgrupos
poblacionales grandes cuyo comportamiento difiere del promedio muestral simple), y no
un artefacto aislado de un solo modelo.

**Consecuencia acumulada para H-A (cierre de toda la Fase 3):** el único hallazgo de
toda la Fase 3 que sobrevive tanto la corrección global por comparaciones múltiples
(Paso 3.7: `ICC_mujer` y `HHI` en M1) como la prueba de robustez en tres variantes
(Paso 3.8: solo `ICC_mujer` en M1, con signo consistente) es el **efecto principal de
`ICC_mujer` sobre `IPSJ_C` en M1**. Ningún otro componente de H-A —ni la interacción con
sexo (que era el mecanismo central de la hipótesis), ni el efecto sobre afrontamiento
(M2), ni el rol mediador de la confianza vecinal (M3)— sobrevive ambas pruebas de
manera simultánea. Este es el resultado final y definitivo de H-A que se reportará en
la sustentación: **evidencia sólida mínima, limitada a una asociación general entre
concentración del cuidado y percepción de acceso a la denuncia, sin el mecanismo
específico de género que la hipótesis proponía como su elemento distintivo.**

## Paso 4.2b — Verificación: Pearson vs. tetracórica para el análisis factorial (registrado 2026-08-20)

El cálculo de KMO/Bartlett (Paso 4.2) generó un warning de `factor_analyzer` sobre el
determinante de la matriz de correlación estar "cerca de cero", resuelto internamente
con pseudoinversa de Moore-Penrose. Se verificó si esto reflejaba multicolinealidad
genuina que ameritara recalcular con correlación tetracórica (más apropiada que Pearson
para ítems binarios) en vez de proceder con Pearson estándar.

**Resultado de la verificación:**
- Determinante: 4,12e-03 — pequeño pero explicado por 17 autovalores <1 multiplicados
  entre sí, no por un autovalor cercano a cero.
- **Autovalores:** todos positivos, mínimo 0,3996 — sin ningún valor cercano a 0.
- **Número de condición:** 14,2 — muy por debajo del umbral de multicolinealidad severa
  (>1000), matriz bien condicionada.
- **Splits de los 17 ítems** (proporción "De acuerdo"): rango 30,6%–55,7% — ningún ítem
  con split extremo (<20% o >80%), el escenario donde Pearson/phi más se aleja de la
  tetracórica.

**Decisión:** se mantiene la matriz de correlación de Pearson para la extracción
factorial (Paso 4.3). El warning de la librería fue un umbral numérico conservador sin
consecuencia sustantiva — no se instala infraestructura adicional (`semopy` u otra) para
recalcular con tetracórica, dado que la evidencia (autovalores, condición, splits) no
justifica el esfuerzo: la ganancia esperada de precisión sería marginal.

## Paso 4.3 — Confiabilidad: Alfa de Cronbach, 17 ítems (registrado 2026-08-20)

**Alfa de Cronbach (17 ítems, n=5.860): 0,8731** (IC 95% [0,8680, 0,8780]).

**Resultado por encima del rango esperado en el enunciado (0,6–0,7).** El enunciado
anticipaba un alfa bajo-moderado como evidencia de que "el machismo" no es una dimensión
única. El resultado observado (0,87) es "bueno" a "muy bueno" según los estándares
convencionales de confiabilidad — sustancialmente más alto de lo previsto.

**Alfa por bloque temático (declarado en el diccionario de la Bienal):**
- P10 (roles tradicionales/esencialismo, 11 ítems): α = 0,8483 (IC95% [0,8420, 0,8540])
- P12 (control en la pareja, 6 ítems): α = 0,8005 (IC95% [0,7920, 0,8080])

Ambos subbloques tienen consistencia interna alta **por separado**, y el conjunto
completo de 17 ítems tiene consistencia aún más alta que cualquiera de los dos
subbloques individualmente — esto es consistente con la posibilidad de que exista un
factor general fuerte que atraviesa ambos bloques, además de (o en lugar de) la
distinción fina entre "roles tradicionales" y "no-injerencia/privatización" que H-B
proponía como la distinción sustantiva.

**Precaución metodológica — el alfa alto NO es, por sí solo, la prueba de refutación de
H-B.** El escenario de refutación preregistrado (Sección 1.4, escenario 3) especifica
dos condiciones conjuntas: *"si el análisis factorial arroja un solo factor con alfa de
Cronbach alto"*. Hasta este punto solo se ha verificado la segunda condición (alfa alto);
la primera (número de factores que emergen del análisis factorial exploratorio) se
determina en el Paso 4.4/4.5, aún pendiente. Un alfa alto es compatible con:
(a) un único factor dominante (lo cual sí refutaría H-B según el criterio preregistrado), o
(b) varios factores correlacionados entre sí que comparten un factor general de segundo
orden (patrón común en escalas de actitudes de género, y compatible con que H-B se
sostenga si esos factores específicos —roles vs. no-injerencia— emergen distinguibles
en la estructura factorial, aun con un alfa global alto).

**No se declara refutada H-B en este paso.** Se procede al Paso 4.4 (extracción y número
de factores) antes de emitir cualquier conclusión sobre el escenario de refutación.

## Paso 4.4 — Extracción factorial: 3 factores no coinciden con la estructura teórica de H-B (registrado 2026-08-20)

**Número de factores:** confirmado en 3 por los tres criterios (Kaiser=3, Horn=3,
coincide con la expectativa del enunciado). Varianza explicada acumulada: 42,4%.

**Resultado — la estructura de contenido NO coincide con la tabla teórica del
enunciado.** En lugar de los tres factores propuestos (Roles tradicionales /
Culpabilización de la víctima / No-injerencia y privatización), la estructura empírica
observada es:

- **F1** (9 ítems, SS=3,203, 18,8% var.): P10.3, P10.4, P10.5, P10.6, P10.7, P10.8,
  P10.9, P10.10, P10.11 — mezcla indiscriminada de roles tradicionales, culpabilización
  de la víctima Y no-injerencia/privatización, todos juntos.
- **F2** (6 ítems, SS=2,728, 16,0% var.): P12.1, P12.2, P12.3, P12.4, P12.5, P12.6 —
  **el bloque P12 completo**, sin excepción alguna.
- **F3** (2 ítems, SS=1,286, 7,6% var.): P10.1, P10.2 — factor estrecho y específico
  ("las mujeres por naturaleza cuidan/hacen mejor los oficios del hogar"), separado del
  resto de ítems de roles tradicionales.

**Patrón dominante: la estructura factorial sigue la organización del cuestionario
(bloque P10 vs. bloque P12), no la distinción teórica de contenido actitudinal
propuesta por H-B.**

**Contradicción directa con la predicción específica de H-B:** la hipótesis esperaba que
`P10.9`, `P12.5`, `P12.3` y `P10.11` (los cuatro ítems de no-injerencia/privatización,
repartidos deliberadamente entre ambos bloques del cuestionario) formaran un factor
propio y distinguible. Empíricamente:
- `P10.9` y `P10.11` cargan en **F1**, junto con ítems de roles y culpabilización.
- `P12.3` y `P12.5` cargan en **F2**, junto con el resto de ítems de control en la pareja.

Es decir, la no-injerencia **no emerge como una dimensión propia** — sus cuatro ítems se
reparten exactamente según a qué bloque del cuestionario (P10 general vs. P12 sobre
relaciones de pareja) pertenecían originalmente, lo cual sugiere que la varianza
compartida dominante es de **formato/contexto de la pregunta** (ítems del mismo bloque
correlacionan más entre sí por estar preguntados en el mismo marco), no de **contenido
actitudinal específico** (roles vs. culpabilización vs. no-injerencia).

**Evaluación frente al escenario de refutación preregistrado (Sección 1.4, escenario 3):**
el criterio literal decía *"H-B refutada si el análisis factorial arroja UN SOLO factor
con alfa alto"*. Técnicamente **no se cumple este criterio exacto** — emergieron 3
factores, no 1. Sin embargo, el espíritu del escenario de refutación (que la distinción
teórica entre roles y no-injerencia carezca de sustento empírico) **sí se confirma**, por
una vía distinta a la anticipada: no porque todo colapse en un solo factor indiferenciado,
sino porque los factores que sí emergen **no corresponden a la partición conceptual que
H-B proponía**. El alfa global alto (0,87, Paso 4.3) junto con esta estructura sugiere una
fuerte dimensión general de actitudes de género atravesando casi todos los ítems
(consistente con F1 absorbiendo 9 de los 17 ítems, incluyendo contenido de tres
categorías teóricas distintas), con matices de formato de encuesta (F2=bloque P12
completo) más que de contenido psicológico diferenciado.

**Consecuencia para H-B:** no puede evaluarse el criterio original de H-B (*"P12.5,
P10.8 y P10.9 discriminan; P10.1 y P10.2 no"*) usando estos 3 factores como proxy de
"no-injerencia" vs. "roles", porque esa partición conceptual no es la que produce el
análisis factorial. Cualquier prueba posterior de H-B con TAC/localidad tendría que
usarse sobre los factores EMPÍRICOS (F1 general, F2=bloque pareja, F3=esencialismo
específico), no sobre la agrupación teórica original — o bien, evaluarse directamente
sobre los ítems individuales sin agrupar, que es la alternativa que el propio diseño del
proyecto contempló desde el principio (Paso 4.2, regla general: si no se puede factorizar
según lo esperado, reportar ítems individuales).

**Nota de baja varianza explicada:** 42,4% acumulado en 3 factores es un valor moderado
— más de la mitad de la varianza de los 17 ítems queda sin explicar por esta estructura
de 3 factores, lo cual es consistente con una escala donde la mayor parte de la señal
compartida es general (F1 domina con 18,8% él solo) y el resto es más ruido específico de
ítem que estructura latente clara.

## Paso 4.5 — Puntajes factoriales estandarizados (registrado 2026-08-20)

Puntajes factoriales calculados por `factor_analyzer.transform()` sobre los 5.860
casos con los 17 ítems completos, estandarizados explícitamente a media=0, sd=1
(verificado exacto, no aproximado).

**Cobertura:** 5.860 de 5.860 (100%) — sin pérdida adicional respecto al subconjunto
usado en KMO/Bartlett/alfa/extracción factorial (Pasos 4.2–4.4).

**Correlación entre factores (F1_z, F2_z, F3_z):**
- F1 vs F2: 0,1665
- F1 vs F3: 0,1553
- F2 vs F3: -0,0478

**Nota metodológica:** varimax es una rotación ortogonal por diseño (los factores
rotados deberían ser exactamente independientes, correlación=0), pero los *puntajes*
calculados por el método de regresión de Thomson (que es el que usa `factor_analyzer`
por defecto) no garantizan ortogonalidad exacta en la práctica — la correlación
residual observada (máximo 0,17) es un artefacto conocido y esperable de este método
de estimación de puntajes, no un error de la rotación en sí (la matriz de cargas
rotadas sí es ortogonal por construcción). Se documenta para que, si estos tres
puntajes se usan simultáneamente como predictores en un modelo posterior, no se asuma
independencia total entre ellos — la colinealidad es baja pero no nula.

**Variables finales disponibles en `df_bienal`:** `F1_z`, `F2_z`, `F3_z`, unidas por
índice original, listas para agregación por localidad (`V1`) en el siguiente paso.

**Recordatorio del Paso 4.4:** dado que la estructura empírica de estos 3 factores NO
corresponde a la partición teórica de H-B (roles / culpabilización / no-injerencia),
sino a una mezcla dominada por bloque del cuestionario (F1=general/P10 mayoritario,
F2=P12 completo, F3=esencialismo específico P10.1-P10.2), cualquier uso posterior de
estos puntajes para evaluar H-B debe nombrarlos y reportarlos según lo que
empíricamente miden, no según los nombres teóricos originales del enunciado (que ya
no aplican a esta estructura).

## Paso 5.1 — Indicadores poblacionales por localidad (2026-08-20)

**Resultados**

- Registros analizados: **13,082**.
- Localidades con información de encuesta: **19**.
- UPL presentes: **30**.
- TAC_M ponderada para Bogotá: **18.8%**.
- Mujeres adultas expandidas en las 19 localidades: **3,458,493**.
- Volumen expandido mínimo de mujeres con violencia visible y afrontada: **694,602**.
- Registros válidos para IBA: **11,361**.
- Registros válidos para ICC: **13,022**.
- Inconsistencias observadas entre Mx404_1..5 y Mx404_6: **17**.

**Conclusión**

Al menos **18.8%** de la población representada por la encuesta presenció y afrontó una situación de violencia contra una mujer. Este valor constituye una cota inferior de la violencia socialmente visible y afrontada y no una estimación de prevalencia total.

## Paso 5.2 — Criterio de publicación (2026-08-20)

**Resultados**

- TAC_M: **19/19 localidades publicables**.
- pct_carga_mujer: **19/19 localidades publicables**.
- gad7_mod_sev: **11/19 localidades publicables**.
- pobreza_subjetiva: **18/19 localidades publicables**.
- IPSJ_C_promedio: **19/19 localidades publicables**.
- ICG_B_promedio: **19/19 localidades publicables**.
- IBA_promedio: **19/19 localidades publicables**.

- Localidades no publicables para el denominador mínimo de demanda: **0**.

**Conclusión**

Las estimaciones territoriales se conservan únicamente cuando cumplen los umbrales de precisión definidos: tamaño efectivo mínimo de 30 observaciones y coeficiente de variación máximo de 30% para proporciones. Las localidades que no cumplen estos criterios no deben presentarse como estimaciones territoriales válidas.

## Paso 5.3 — Oferta institucional (2026-08-20)

**Resultados**

- Cortes comunes analizados: **2025-06, 2025-09, 2025-12, 2026-03**.
- Atenciones acumuladas de Línea Púrpura: **90,288**.
- Atenciones acumuladas de Duplas: **7,023**.
- Oferta institucional total: **97,311 atenciones**.
- Localidades con mayor oferta acumulada:
- Kennedy: **14,101 atenciones**.
- Suba: **13,687 atenciones**.
- Engativá: **10,574 atenciones**.

**Conclusión**

La oferta institucional se concentra de forma desigual entre localidades. La comparación territorial se realiza únicamente sobre los cuatro cortes comunes entre las fuentes, evitando inflar la cobertura con periodos sin comparador administrativo equivalente.

## Paso 5.4 — Registro administrativo de riesgo (2026-08-20)

**Resultados**

- Casos administrativos acumulados en los cuatro cortes comunes: **6,708**.
- Población femenina oficial utilizada como denominador: **4,134,734**.
- Localidades con mayor tasa administrativa:
- La Candelaria: **942.1 casos por 100.000 mujeres** (76 casos acumulados).
- Ciudad Bolívar: **327.6 casos por 100.000 mujeres** (1,142 casos acumulados).
- San Cristóbal: **301.0 casos por 100.000 mujeres** (625 casos acumulados).

**Conclusión**

La tasa administrativa permite normalizar territorialmente los casos registrados por población femenina. Este indicador representa demanda capturada por el sistema y no debe interpretarse como prevalencia total de violencia.

## Paso 5.5 — Razones de cobertura (2026-08-20)

**Resultados**

- Mayor RC_admin: **Teusaquillo**, con **26.93 atenciones por caso administrativo**.
- Menor RC_admin: **La Candelaria**, con **4.63 atenciones por caso administrativo**.
- Mayor cobertura frente a necesidad mínima observable: **Fontibón**, con **240.38 atenciones por cada 1.000 mujeres del volumen mínimo estimado**.
- Menor cobertura frente a necesidad mínima observable: **Santa Fe**, con **90.84 atenciones por cada 1.000 mujeres del volumen mínimo estimado**.
- Mujeres adultas expandidas en las 19 localidades: **3,458,493**.
- Población femenina oficial en las mismas localidades: **4,132,925**.
- Diferencia relativa entre ambos universos poblacionales: **-16.3%**.

**Conclusión**

RC_admin expresa cobertura frente a los casos capturados por el sistema. La segunda razón usa un denominador poblacional independiente, pero debe interpretarse como una **cota superior de cobertura**, porque la TAC solo identifica violencia visible y afrontada y no toda la necesidad real existente.

## Paso 5.6 — Divergencia de rankings (2026-08-20)

**Resultados**

- Localidades con cambio de al menos cuatro posiciones: **13 de 19**.

Localidades que aparecen mejor cubiertas bajo el denominador administrativo que bajo el denominador poblacional mínimo:

- Chapinero: pasa de posición **2** a **16** (Δ = **+14**).
- Teusaquillo: pasa de posición **1** a **15** (Δ = **+14**).
- Puente Aranda: pasa de posición **9** a **17** (Δ = **+8**).
- Kennedy: pasa de posición **8** a **14** (Δ = **+6**).
- Santa Fe: pasa de posición **15** a **19** (Δ = **+4**).
- Suba: pasa de posición **4** a **8** (Δ = **+4**).

Localidades que mejoran su posición al utilizar el denominador poblacional mínimo:

- La Candelaria: pasa de posición **19** a **9** (Δ = **-10**).
- Antonio Nariño: pasa de posición **10** a **2** (Δ = **-8**).
- Tunjuelito: pasa de posición **12** a **6** (Δ = **-6**).
- Fontibón: pasa de posición **6** a **1** (Δ = **-5**).
- San Cristóbal: pasa de posición **17** a **12** (Δ = **-5**).
- Bosa: pasa de posición **11** a **7** (Δ = **-4**).
- Rafael Uribe Uribe: pasa de posición **14** a **10** (Δ = **-4**).

**Conclusión**

La magnitud de `delta_rank` permite identificar qué localidades cambian sustancialmente de posición cuando la cobertura deja de evaluarse exclusivamente contra los casos que el propio sistema registró.

## Paso 5.7 — Prueba estadística de H1′ (2026-08-20)

**Resultados**

- Concordancia entre `rank_admin` y `rank_real`: **ρ = 0.267**, IC95% **[-0.219, 0.679]**, p = **0.2698**.
- Asociación entre `IPSJ_C` promedio y `delta_rank`: **ρ = 0.180**, IC95% **[-0.384, 0.635]**, p = **0.4601**; signo **contrario a la expectativa**.
- Asociación entre `ICG_B` promedio y `delta_rank`: **ρ = 0.053**, IC95% **[-0.464, 0.541]**, p = **0.8301**; signo **contrario a la expectativa**.
- Asociación entre tasa administrativa y cobertura frente a necesidad mínima: **ρ = -0.286**, IC95% **[-0.690, 0.200]**, p = **0.2353**; signo **negativo**.
- Réplicas bootstrap utilizadas por prueba: hasta **2.000**.
- Resultado frente al criterio predefinido de refutación: H1′ queda **no refutada por el criterio de alta concordancia**.

**Conclusión**

La evidencia territorial permite evaluar si el orden de cobertura derivado del registro administrativo coincide con el orden obtenido al utilizar un denominador poblacional independiente. La conclusión sobre H1′ se determina a partir de la concordancia de rankings y de la dirección de las asociaciones con acceso percibido a medios de denuncia, confianza vecinal y riesgo administrativo.
## Fase 6 — Módulo complementario de llamadas 123 (registrado 2026-08-20)

Fuente: `outputs/llamadas123_consolidado_limpio.csv`. Objetivo: evaluar demanda de
emergencia con víctima femenina, calidad del registro de `RECEPCION`, diferencial
temporal de respuesta y distribución horaria de incidentes relevantes.

### Auditoría estructural

- Filas del consolidado: **52,717**
- Incidentes únicos (`NUMERO_INCIDENTE`): **48,469**
- Filas adicionales asociadas a incidentes repetidos: **4,248**
- 5 archivos de origen (marzo/junio/septiembre/diciembre 2025, marzo 2026), sin conflictos
  de `CODIGO_LOCALIDAD`, `TIPO_CODIGO`, `PRIORIDAD_FINAL` ni `ARCHIVO_ORIGEN` dentro de un
  mismo `NUMERO_INCIDENTE` (verificado por assert).

### Paso 6.1 — Auditoría de codificación

Se detectó daño de codificación (caracteres de sustitución) en texto libre:

| Columna | Filas con reemplazo | % |
|---|---|---|
| LOCALIDAD | 4,390 | 8.3% |
| UNIDAD | 6,785 | 12.9% |
| TIPO_INCIDENTE | 2,709 | 5.1% |


**9,310 filas (17.7%)** tienen al menos un
carácter dañado en `LOCALIDAD`, `UNIDAD` o `TIPO_INCIDENTE`. Se recomienda reprocesar
desde los 5 archivos originales para una versión de producción, pero esto **no bloquea**
la Fase 6 porque las dos dimensiones críticas (código de localidad, código de tipo de
incidente) se conservan intactas sin depender del texto dañado.

### Normalización de localidad por código

`CODIGO_LOCALIDAD` verificado en rango [1,20] sin excepciones. Nombre canónico por
código reconstruido eligiendo, dentro de cada código, la variante de texto **sin**
caracteres dañados más frecuente (o la moda si todas están dañadas). 20 localidades
mapeadas correctamente, incluyendo Sumapaz (código 20, solo 1 incidente en este
consolidado).

### Corrección de fechas (Paso previo a 6.2)

Se detectó y corrigió un patrón sistemático de intercambio día/mes en
`FECHA_INICIO_DESPLAZAMIENTO_MOVIL` para los 4 archivos de 2025 (no aplica al archivo de
marzo 2026, que no presenta el mismo patrón de daño). **15,946 fechas
corregidas.** Este paso es bloqueante: sin la corrección, los tiempos de respuesta
calculados habrían mostrado duraciones de varios meses para eventos del mismo día.

### Paso 6.2 — Tiempo entre desplazamiento y recepción (nivel fila)

Tras la corrección de fechas, prácticamente todas las diferencias temporales son
coherentes: solo **1 tiempo negativo** y **1 tiempo mayor a 24
horas** quedan fuera de rango, sobre 26,213 filas válidas.

### Consolidación a nivel de incidente

- Incidentes únicos construidos: **48,469**
- Incidentes con al menos una víctima femenina: **14,958**
- Incidentes sin `RECEPCION` válida: **23,310
  (48.1%)**

### Paso 6.3 — Faltantes de RECEPCION por localidad

| Localidad | n_incidentes | n_recepcion_nula | % nula |
|---|---|---|---|
| SUMAPAZ | 1 | 1 | 100.0% |
| CHAPINERO | 1,311 | 769 | 58.7% |
| TEUSAQUILLO | 1,660 | 877 | 52.8% |
| BARRIOS UNIDOS | 1,337 | 706 | 52.8% |
| SUBA | 4,869 | 2,492 | 51.2% |
| USAQUÉN | 2,072 | 1,058 | 51.1% |
| ENGATIVÁ | 5,126 | 2,610 | 50.9% |
| SANTA FE | 1,476 | 745 | 50.5% |
| PUENTE ARANDA | 2,938 | 1,480 | 50.4% |
| LA CANDELARIA | 353 | 176 | 49.9% |
| FONTIBÓN | 2,330 | 1,147 | 49.2% |
| LOS MÁRTIRES | 1,667 | 792 | 47.5% |
| RAFAEL URIBE URIBE | 2,343 | 1,105 | 47.2% |
| USME | 1,880 | 875 | 46.5% |
| TUNJUELITO | 1,128 | 511 | 45.3% |
| CIUDAD BOLÍVAR | 3,676 | 1,657 | 45.1% |
| BOSA | 3,803 | 1,708 | 44.9% |
| ANTONIO NARIÑO | 938 | 418 | 44.6% |
| KENNEDY | 6,817 | 2,990 | 43.9% |
| SAN CRISTÓBAL | 2,566 | 1,122 | 43.7% |


Chi-cuadrado = **247.20**, p-valor = **3.022e-42**, V de Cramér = **0.072**.
La asociación entre localidad y ausencia de `RECEPCION` es estadísticamente detectable
pero de **magnitud pequeña**. Interpretación correcta: la completitud de `RECEPCION` no
es territorialmente uniforme, aunque la heterogeneidad territorial es pequeña — no debe
leerse como que una localidad "registra mal" de forma determinante. Sumapaz se excluye
del análisis de concentración territorial por tener solo 1 incidente en este consolidado.

### Paso 6.4 — Incidentes con víctima femenina (filtro objetivo)

| Grupo | n_incidentes | n_tiempo_valido | % recepción nula | Mediana (min) |
|---|---|---|---|---|
| HERIDO | 2,886 | 2,608 | 9.6% | 128.8 |
| SUICIDIO | 1,498 | 1,387 | 7.4% | 226.0 |
| TRASTORNO_MENTAL | 1,383 | 1,293 | 6.5% | 239.6 |
| INTOX | 121 | 90 | 25.6% | 187.9 |
| MALTRATO | 113 | 104 | 8.0% | 205.6 |


**Total objetivo: 6,001 incidentes.** RECEPCION nula en este
subconjunto: **519
(8.6%)**, muy por debajo del 48,1%
del conjunto completo — la completitud mejora sustancialmente al restringir a estos tipos
de incidente.

**Nota sobre alcance:** la categoría `AGRESIÓN` prevista en el plan original **no existe
literalmente** en los códigos del archivo, por lo que no se incorporó artificialmente.
Se identificaron además **314 incidentes VIOSEXUAL con víctima femenina**,
conservados como dato complementario, sin mezclarlos con el filtro principal.

### Paso 6.5 — MALTRATO vs. incidentes clínicos comparables

Comparación pareada por estrato común (localidad × prioridad × franja horaria):

- MALTRATO con comparador válido: **103** de 104 con tiempo válido
- Clínicos dentro del soporte común: **2,914**
- Estratos comunes: **65**
- Mediana MALTRATO: **205.9 min** · Mediana clínicos: **190.2 min**
- Diferencia de medianas: **15.7 min**
- Mann-Whitney U = **177743.0**, p = **0.001448**, Delta de Cliff = **0.184**

La diferencia es estadísticamente detectable pero el tamaño de efecto es **pequeño**
(Delta de Cliff ≈ 0,18). No se interpreta como evidencia de discriminación sistemática
en el tiempo de respuesta a MALTRATO, solo como una diferencia descriptiva menor dentro
de estratos comparables.

### Paso 6.6 — Matriz hora × día de la semana

Sobre el filtro femenino principal (6,001 incidentes):

- Celda de mayor demanda: **Martes, 10:00–10:59** (92 incidentes)
- Día de mayor volumen total: **Martes** (997 incidentes)
- Hora de mayor volumen agregado: **09:00** (448 incidentes)
- Por franja: Mañana 2,317 ·
  Tarde 2,017 ·
  Noche 1,150 ·
  Madrugada 517

**Advertencia de interpretación:** estos conteos reflejan demanda **registrada** en el
sistema 123, no prevalencia poblacional. La concentración diurna puede reflejar patrones
de reporte (mayor disponibilidad para llamar de día) tanto como patrones reales de
ocurrencia — no se puede distinguir con estos datos.

---

**Conclusiones consolidadas de la Fase 6:**
1. La ausencia de `RECEPCION` (48,1% del total) es un problema de calidad relevante que
   debe acompañar cualquier visualización de tiempos de respuesta.
2. El subconjunto femenino de interés (6.001 incidentes) tiene mejor completitud de
   `RECEPCION` (8,6% nula) que el conjunto general.
3. MALTRATO muestra una diferencia temporal pequeña pero estadísticamente detectable
   frente a incidentes clínicos comparables (~15,7 min, efecto pequeño).
4. La demanda registrada se concentra en horas de mañana y tarde, con pico el martes
   a las 10:00 — dato descriptivo, no causal.


## Paso 5.1 — Indicadores poblacionales por localidad (2026-08-20)

**Resultados**

- Registros analizados: **13,082**.
- Localidades con información de encuesta: **19**.
- UPL presentes: **30**.
- TAC_M ponderada para Bogotá: **18.8%**.
- Mujeres adultas expandidas en las 19 localidades: **3,458,493**.
- Volumen expandido mínimo de mujeres con violencia visible y afrontada: **694,602**.
- Registros válidos para IBA: **11,361**.
- Registros válidos para ICC: **13,022**.
- Inconsistencias observadas entre Mx404_1..5 y Mx404_6: **17**.

**Conclusión**

Al menos **18.8%** de la población representada por la encuesta presenció y afrontó una situación de violencia contra una mujer. Este valor constituye una cota inferior de la violencia socialmente visible y afrontada y no una estimación de prevalencia total.

## Paso 5.2 — Criterio de publicación (2026-08-20)

**Resultados**

- TAC_M: **19/19 localidades publicables**.
- pct_carga_mujer: **19/19 localidades publicables**.
- gad7_mod_sev: **11/19 localidades publicables**.
- pobreza_subjetiva: **18/19 localidades publicables**.
- IPSJ_C_promedio: **19/19 localidades publicables**.
- ICG_B_promedio: **19/19 localidades publicables**.
- IBA_promedio: **19/19 localidades publicables**.

- Localidades no publicables para el denominador mínimo de demanda: **0**.

**Conclusión**

Las estimaciones territoriales se conservan únicamente cuando cumplen los umbrales de precisión definidos: tamaño efectivo mínimo de 30 observaciones y coeficiente de variación máximo de 30% para proporciones. Las localidades que no cumplen estos criterios no deben presentarse como estimaciones territoriales válidas.

## Paso 5.3 — Oferta institucional (2026-08-20)

**Resultados**

- Cortes comunes analizados: **2025-06, 2025-09, 2025-12, 2026-03**.
- Atenciones acumuladas de Línea Púrpura: **90,288**.
- Atenciones acumuladas de Duplas: **7,023**.
- Oferta institucional total: **97,311 atenciones**.
- Localidades con mayor oferta acumulada:
- Kennedy: **14,101 atenciones**.
- Suba: **13,687 atenciones**.
- Engativá: **10,574 atenciones**.

**Conclusión**

La oferta institucional se concentra de forma desigual entre localidades. La comparación territorial se realiza únicamente sobre los cuatro cortes comunes entre las fuentes, evitando inflar la cobertura con periodos sin comparador administrativo equivalente.

## Paso 5.4 — Registro administrativo de riesgo (2026-08-20)

**Resultados**

- Casos administrativos acumulados en los cuatro cortes comunes: **6,708**.
- Población femenina oficial utilizada como denominador: **4,134,734**.
- Localidades con mayor tasa administrativa:
- La Candelaria: **942.1 casos por 100.000 mujeres** (76 casos acumulados).
- Ciudad Bolívar: **327.6 casos por 100.000 mujeres** (1,142 casos acumulados).
- San Cristóbal: **301.0 casos por 100.000 mujeres** (625 casos acumulados).

**Conclusión**

La tasa administrativa permite normalizar territorialmente los casos registrados por población femenina. Este indicador representa demanda capturada por el sistema y no debe interpretarse como prevalencia total de violencia.

## Paso 5.5 — Razones de cobertura (2026-08-20)

**Resultados**

- Mayor RC_admin: **Teusaquillo**, con **26.93 atenciones por caso administrativo**.
- Menor RC_admin: **La Candelaria**, con **4.63 atenciones por caso administrativo**.
- Mayor cobertura frente a necesidad mínima observable: **Fontibón**, con **240.38 atenciones por cada 1.000 mujeres del volumen mínimo estimado**.
- Menor cobertura frente a necesidad mínima observable: **Santa Fe**, con **90.84 atenciones por cada 1.000 mujeres del volumen mínimo estimado**.
- Mujeres adultas expandidas en las 19 localidades: **3,458,493**.
- Población femenina oficial en las mismas localidades: **4,132,925**.
- Diferencia relativa entre ambos universos poblacionales: **-16.3%**.

**Conclusión**

RC_admin expresa cobertura frente a los casos capturados por el sistema. La segunda razón usa un denominador poblacional independiente, pero debe interpretarse como una **cota superior de cobertura**, porque la TAC solo identifica violencia visible y afrontada y no toda la necesidad real existente.

## Paso 5.6 — Divergencia de rankings (2026-08-20)

**Resultados**

- Localidades con cambio de al menos cuatro posiciones: **13 de 19**.

Localidades que aparecen mejor cubiertas bajo el denominador administrativo que bajo el denominador poblacional mínimo:

- Chapinero: pasa de posición **2** a **16** (Δ = **+14**).
- Teusaquillo: pasa de posición **1** a **15** (Δ = **+14**).
- Puente Aranda: pasa de posición **9** a **17** (Δ = **+8**).
- Kennedy: pasa de posición **8** a **14** (Δ = **+6**).
- Santa Fe: pasa de posición **15** a **19** (Δ = **+4**).
- Suba: pasa de posición **4** a **8** (Δ = **+4**).

Localidades que mejoran su posición al utilizar el denominador poblacional mínimo:

- La Candelaria: pasa de posición **19** a **9** (Δ = **-10**).
- Antonio Nariño: pasa de posición **10** a **2** (Δ = **-8**).
- Tunjuelito: pasa de posición **12** a **6** (Δ = **-6**).
- Fontibón: pasa de posición **6** a **1** (Δ = **-5**).
- San Cristóbal: pasa de posición **17** a **12** (Δ = **-5**).
- Bosa: pasa de posición **11** a **7** (Δ = **-4**).
- Rafael Uribe Uribe: pasa de posición **14** a **10** (Δ = **-4**).

**Conclusión**

La magnitud de `delta_rank` permite identificar qué localidades cambian sustancialmente de posición cuando la cobertura deja de evaluarse exclusivamente contra los casos que el propio sistema registró.

## Paso 5.7 — Prueba estadística de H1′ (2026-08-20)

**Resultados**

- Concordancia entre `rank_admin` y `rank_real`: **ρ = 0.267**, IC95% **[-0.219, 0.679]**, p = **0.2698**.
- Asociación entre `IPSJ_C` promedio y `delta_rank`: **ρ = 0.180**, IC95% **[-0.384, 0.635]**, p = **0.4601**; signo **contrario a la expectativa**.
- Asociación entre `ICG_B` promedio y `delta_rank`: **ρ = 0.053**, IC95% **[-0.464, 0.541]**, p = **0.8301**; signo **contrario a la expectativa**.
- Asociación entre tasa administrativa y cobertura frente a necesidad mínima: **ρ = -0.286**, IC95% **[-0.690, 0.200]**, p = **0.2353**; signo **negativo**.
- Réplicas bootstrap utilizadas por prueba: hasta **2.000**.
- Resultado frente al criterio predefinido de refutación: H1′ queda **no refutada por el criterio de alta concordancia**.

**Conclusión**

La evidencia territorial permite evaluar si el orden de cobertura derivado del registro administrativo coincide con el orden obtenido al utilizar un denominador poblacional independiente. La conclusión sobre H1′ se determina a partir de la concordancia de rankings y de la dirección de las asociaciones con acceso percibido a medios de denuncia, confianza vecinal y riesgo administrativo.

## Paso 5.8 — Robustez leave-one-out (2026-08-20)

Se repitieron las cuatro correlaciones excluyendo una localidad en cada iteración.

**Rangos de ρ y clasificación**
- rank_admin_vs_rank_real: ρ de **0.164** a **0.408**; hallazgo robusto: no cambia el signo.
- IPSJ_C_vs_delta_rank: ρ de **0.036** a **0.305**; hallazgo robusto: no cambia el signo.
- ICG_B_vs_delta_rank: ρ de **-0.110** a **0.187**; exploración: cambia el signo al excluir al menos una localidad.
- tasa_admin_vs_RC_real: ρ de **-0.432** a **-0.187**; hallazgo robusto: no cambia el signo.

**Criterio de reporte**
Si el signo cambia al excluir cualquier localidad, la asociación se reporta solo como exploración y no como hallazgo.

## Paso 5.9 — Índice de Necesidad No Atendida (INA) (2026-08-20)

**Definición**

INA = 0,40 · pct(TAC_M) + 0,30 · pct(IBA) + 0,30 · pct(-RC_real).
Cada componente se transforma a percentil de 0 a 100 antes de aplicar los pesos.

**Pesos predeterminados**

- `PESO_TAC_M`: **0.40**.
- `PESO_IBA`: **0.30**.
- `PESO_DEFICIT_COBERTURA`: **0.30**.

Los pesos son una decisión explícita y validada para que sumen 1.0. El archivo `outputs/tableau/ina_localidad.csv` contiene los tres componentes percentilares, los pesos predeterminados, el INA y su ranking.

**Configuración del dashboard**

Crear tres parámetros Tableau ajustables entre 0 y 1: `PESO_TAC_M`, `PESO_IBA` y `PESO_DEFICIT_COBERTURA`. El campo calculado del INA debe usar:

`[PESO_TAC_M] * [pct_TAC_M] + [PESO_IBA] * [pct_IBA] + [PESO_DEFICIT_COBERTURA] * [pct_deficit_cobertura]`

Para cada escenario, los parámetros deben sumar 1.0. Así el jurado puede mover la ponderación y observar la sensibilidad del ranking sin cambiar los datos de base.

**Interpretación**

Un INA mayor indica mayor necesidad no atendida relativa: más violencia visible, mayor barrera percibida de acceso a la denuncia y menor cobertura frente al volumen mínimo observable.

## Paso 5.10 — Clasificación por cuadrantes (2026-08-20)

**Criterio**

Se usaron las medianas territoriales como puntos de corte. `TAC_M` alto significa estar en o sobre la mediana; cobertura real alta significa estar en o sobre la mediana de `RC_real_cota_superior`.

- Mediana de `TAC_M`: **0.2043**.
- Mediana de `RC_real_cota_superior`: **135.8836**.
- Mediana de `ICG_B`: **3.1367**.

**Distribución**

- Zona de demanda desatendida: **9 localidades**.
- Zona de sobre-oferta relativa: **9 localidades**.
- Zona de captura: **1 localidades**.

**Lectura de política**

- Cuadrante I, zona de demanda desatendida: prioridad máxima de inversión.
- Cuadrante II, zona de captura: el sistema está funcionando; sostener.
- Cuadrante III, zona opaca: la baja `TAC_M` no implica poca violencia; verificar baja incidencia frente a baja visibilidad.
- Cuadrante IV, zona de sobre-oferta relativa: candidata a reasignación de recursos.

La zona III se cruza con `ICG_B`. Se identificaron **0 localidades** en zona III con `ICG_B` bajo frente a la mediana; estas son zonas opacas prioritarias para verificar, no territorios que puedan interpretarse automáticamente como de baja incidencia.

La tabla `outputs/tableau/cuadrantes_localidad.csv` contiene la clasificación, la lectura de política y las banderas necesarias para el dashboard.

## Paso 5.1 — Indicadores poblacionales por localidad (2026-08-20)

**Resultados**

- Registros analizados: **13,082**.
- Localidades con información de encuesta: **19**.
- UPL presentes: **30**.
- TAC_M ponderada para Bogotá: **18.8%**.
- Mujeres adultas expandidas en las 19 localidades: **3,458,493**.
- Volumen expandido mínimo de mujeres con violencia visible y afrontada: **694,602**.
- Registros válidos para IBA: **11,361**.
- Registros válidos para ICC: **13,022**.
- Inconsistencias observadas entre Mx404_1..5 y Mx404_6: **17**.

**Conclusión**

Al menos **18.8%** de la población representada por la encuesta presenció y afrontó una situación de violencia contra una mujer. Este valor constituye una cota inferior de la violencia socialmente visible y afrontada y no una estimación de prevalencia total.

## Paso 5.2 — Criterio de publicación (2026-08-20)

**Resultados**

- TAC_M: **19/19 localidades publicables**.
- pct_carga_mujer: **19/19 localidades publicables**.
- gad7_mod_sev: **11/19 localidades publicables**.
- pobreza_subjetiva: **18/19 localidades publicables**.
- IPSJ_C_promedio: **19/19 localidades publicables**.
- ICG_B_promedio: **19/19 localidades publicables**.
- IBA_promedio: **19/19 localidades publicables**.

- Localidades no publicables para el denominador mínimo de demanda: **0**.

**Conclusión**

Las estimaciones territoriales se conservan únicamente cuando cumplen los umbrales de precisión definidos: tamaño efectivo mínimo de 30 observaciones y coeficiente de variación máximo de 30% para proporciones. Las localidades que no cumplen estos criterios no deben presentarse como estimaciones territoriales válidas.

## Paso 5.3 — Oferta institucional (2026-08-20)

**Resultados**

- Cortes comunes analizados: **2025-06, 2025-09, 2025-12, 2026-03**.
- Atenciones acumuladas de Línea Púrpura: **90,288**.
- Atenciones acumuladas de Duplas: **7,023**.
- Oferta institucional total: **97,311 atenciones**.
- Localidades con mayor oferta acumulada:
- Kennedy: **14,101 atenciones**.
- Suba: **13,687 atenciones**.
- Engativá: **10,574 atenciones**.

**Conclusión**

La oferta institucional se concentra de forma desigual entre localidades. La comparación territorial se realiza únicamente sobre los cuatro cortes comunes entre las fuentes, evitando inflar la cobertura con periodos sin comparador administrativo equivalente.

## Paso 5.4 — Registro administrativo de riesgo (2026-08-20)

**Resultados**

- Casos administrativos acumulados en los cuatro cortes comunes: **6,708**.
- Población femenina oficial utilizada como denominador: **4,134,734**.
- Localidades con mayor tasa administrativa:
- La Candelaria: **942.1 casos por 100.000 mujeres** (76 casos acumulados).
- Ciudad Bolívar: **327.6 casos por 100.000 mujeres** (1,142 casos acumulados).
- San Cristóbal: **301.0 casos por 100.000 mujeres** (625 casos acumulados).

**Conclusión**

La tasa administrativa permite normalizar territorialmente los casos registrados por población femenina. Este indicador representa demanda capturada por el sistema y no debe interpretarse como prevalencia total de violencia.

## Paso 5.5 — Razones de cobertura (2026-08-20)

**Resultados**

- Mayor RC_admin: **Teusaquillo**, con **26.93 atenciones por caso administrativo**.
- Menor RC_admin: **La Candelaria**, con **4.63 atenciones por caso administrativo**.
- Mayor cobertura frente a necesidad mínima observable: **Fontibón**, con **240.38 atenciones por cada 1.000 mujeres del volumen mínimo estimado**.
- Menor cobertura frente a necesidad mínima observable: **Santa Fe**, con **90.84 atenciones por cada 1.000 mujeres del volumen mínimo estimado**.
- Mujeres adultas expandidas en las 19 localidades: **3,458,493**.
- Población femenina oficial en las mismas localidades: **4,132,925**.
- Diferencia relativa entre ambos universos poblacionales: **-16.3%**.

**Conclusión**

RC_admin expresa cobertura frente a los casos capturados por el sistema. La segunda razón usa un denominador poblacional independiente, pero debe interpretarse como una **cota superior de cobertura**, porque la TAC solo identifica violencia visible y afrontada y no toda la necesidad real existente.

## Paso 5.6 — Divergencia de rankings (2026-08-20)

**Resultados**

- Localidades con cambio de al menos cuatro posiciones: **13 de 19**.

Localidades que aparecen mejor cubiertas bajo el denominador administrativo que bajo el denominador poblacional mínimo:

- Chapinero: pasa de posición **2** a **16** (Δ = **+14**).
- Teusaquillo: pasa de posición **1** a **15** (Δ = **+14**).
- Puente Aranda: pasa de posición **9** a **17** (Δ = **+8**).
- Kennedy: pasa de posición **8** a **14** (Δ = **+6**).
- Santa Fe: pasa de posición **15** a **19** (Δ = **+4**).
- Suba: pasa de posición **4** a **8** (Δ = **+4**).

Localidades que mejoran su posición al utilizar el denominador poblacional mínimo:

- La Candelaria: pasa de posición **19** a **9** (Δ = **-10**).
- Antonio Nariño: pasa de posición **10** a **2** (Δ = **-8**).
- Tunjuelito: pasa de posición **12** a **6** (Δ = **-6**).
- Fontibón: pasa de posición **6** a **1** (Δ = **-5**).
- San Cristóbal: pasa de posición **17** a **12** (Δ = **-5**).
- Bosa: pasa de posición **11** a **7** (Δ = **-4**).
- Rafael Uribe Uribe: pasa de posición **14** a **10** (Δ = **-4**).

**Conclusión**

La magnitud de `delta_rank` permite identificar qué localidades cambian sustancialmente de posición cuando la cobertura deja de evaluarse exclusivamente contra los casos que el propio sistema registró.

## Paso 5.7 — Prueba estadística de H1′ (2026-08-20)

**Resultados**

- Concordancia entre `rank_admin` y `rank_real`: **ρ = 0.267**, IC95% **[-0.219, 0.679]**, p = **0.2698**.
- Asociación entre `IPSJ_C` promedio y `delta_rank`: **ρ = 0.180**, IC95% **[-0.384, 0.635]**, p = **0.4601**; signo **contrario a la expectativa**.
- Asociación entre `ICG_B` promedio y `delta_rank`: **ρ = 0.053**, IC95% **[-0.464, 0.541]**, p = **0.8301**; signo **contrario a la expectativa**.
- Asociación entre tasa administrativa y cobertura frente a necesidad mínima: **ρ = -0.286**, IC95% **[-0.690, 0.200]**, p = **0.2353**; signo **negativo**.
- Réplicas bootstrap utilizadas por prueba: hasta **2.000**.
- Resultado frente al criterio predefinido de refutación: H1′ queda **no refutada por el criterio de alta concordancia**.

**Conclusión**

La evidencia territorial permite evaluar si el orden de cobertura derivado del registro administrativo coincide con el orden obtenido al utilizar un denominador poblacional independiente. La conclusión sobre H1′ se determina a partir de la concordancia de rankings y de la dirección de las asociaciones con acceso percibido a medios de denuncia, confianza vecinal y riesgo administrativo.

## Paso 5.8 — Robustez leave-one-out (2026-08-20)

Se repitieron las cuatro correlaciones excluyendo una localidad en cada iteración.

**Rangos de ρ y clasificación**
- rank_admin_vs_rank_real: ρ de **0.164** a **0.408**; hallazgo robusto: no cambia el signo.
- IPSJ_C_vs_delta_rank: ρ de **0.036** a **0.305**; hallazgo robusto: no cambia el signo.
- ICG_B_vs_delta_rank: ρ de **-0.110** a **0.187**; exploración: cambia el signo al excluir al menos una localidad.
- tasa_admin_vs_RC_real: ρ de **-0.432** a **-0.187**; hallazgo robusto: no cambia el signo.

**Criterio de reporte**
Si el signo cambia al excluir cualquier localidad, la asociación se reporta solo como exploración y no como hallazgo.

## Paso 5.9 — Índice de Necesidad No Atendida (INA) (2026-08-20)

**Definición**

INA = 0,40 · pct(TAC_M) + 0,30 · pct(IBA) + 0,30 · pct(-RC_real).
Cada componente se transforma a percentil de 0 a 100 antes de aplicar los pesos.

**Pesos predeterminados**

- `PESO_TAC_M`: **0.40**.
- `PESO_IBA`: **0.30**.
- `PESO_DEFICIT_COBERTURA`: **0.30**.

Los pesos son una decisión explícita y validada para que sumen 1.0. El archivo `outputs/ina_localidad.csv` contiene los tres componentes percentilares, los pesos predeterminados, el INA y su ranking.

**Configuración del dashboard**

Crear tres parámetros Tableau ajustables entre 0 y 1: `PESO_TAC_M`, `PESO_IBA` y `PESO_DEFICIT_COBERTURA`. El campo calculado del INA debe usar:

`[PESO_TAC_M] * [pct_TAC_M] + [PESO_IBA] * [pct_IBA] + [PESO_DEFICIT_COBERTURA] * [pct_deficit_cobertura]`

Para cada escenario, los parámetros deben sumar 1.0. Así el jurado puede mover la ponderación y observar la sensibilidad del ranking sin cambiar los datos de base.

**Interpretación**

Un INA mayor indica mayor necesidad no atendida relativa: más violencia visible, mayor barrera percibida de acceso a la denuncia y menor cobertura frente al volumen mínimo observable.

## Paso 5.10 — Clasificación por cuadrantes (2026-08-20)

**Criterio**

Se usaron las medianas territoriales como puntos de corte. `TAC_M` alto significa estar en o sobre la mediana; cobertura real alta significa estar en o sobre la mediana de `RC_real_cota_superior`.

- Mediana de `TAC_M`: **0.2043**.
- Mediana de `RC_real_cota_superior`: **135.8836**.
- Mediana de `ICG_B`: **3.1367**.

**Distribución**

- Zona de demanda desatendida: **9 localidades**.
- Zona de sobre-oferta relativa: **9 localidades**.
- Zona de captura: **1 localidades**.

**Lectura de política**

- Cuadrante I, zona de demanda desatendida: prioridad máxima de inversión.
- Cuadrante II, zona de captura: el sistema está funcionando; sostener.
- Cuadrante III, zona opaca: la baja `TAC_M` no implica poca violencia; verificar baja incidencia frente a baja visibilidad.
- Cuadrante IV, zona de sobre-oferta relativa: candidata a reasignación de recursos.

La zona III se cruza con `ICG_B`. Se identificaron **0 localidades** en zona III con `ICG_B` bajo frente a la mediana; estas son zonas opacas prioritarias para verificar, no territorios que puedan interpretarse automáticamente como de baja incidencia.

La tabla `outputs/cuadrantes_localidad.csv` contiene la clasificación, la lectura de política y las banderas necesarias para el dashboard.

## Paso 5.11 — Capa normativa (2026-08-20)

**Validación cruzada entre encuestas independientes**

Se unieron los puntajes factoriales territoriales de la Encuesta Bienal (`F1_z`, `F2_z`, `F3_z`) con `ICG_B_promedio` de la Encuesta de Percepción mediante `codigo_localidad`, con **19 localidades comunes**.

La asociación exploratoria entre `F2_z` e `ICG_B_promedio` fue ρ = **-0.130**, p = **0.5963**.

**Criterio de clasificación**

Se usa `F2_z` como **proxy factorial** de no-injerencia alta/baja, cortado por su mediana (**-0.0309**). La Bienal documenta que la no-injerencia no emerge como factor independiente; `F2_z` mezcla control en pareja con ítems de no-injerencia. Por eso esta capa es validación cruzada exploratoria, no una medición pura de la norma.

- Demanda desatendida + no-injerencia alta: **3 localidades**; lectura: **intervención comunitaria y campaña**.
- Demanda desatendida + no-injerencia baja: **6 localidades**; lectura: **déficit de infraestructura, no de norma**.

La tabla `outputs/capa_normativa_localidad.csv` conserva los puntajes, el cuadrante, `ICG_B`, la clasificación y la lectura de política.

## Paso 5.12 — Gráficos para dashboard Tableau

- Gráfico 7: dispersión de `RC_real` frente a `TAC_M`, tamaño por población femenina, color por `ICG_B`, líneas de mediana y etiquetas de localidad. Exportado a `outputs/tableau/grafico7_dispersion_cuadrantes.png`.
- Gráfico 8: slope chart de `rank_admin` a `rank_real`, resaltando localidades con `|delta_rank| >= 4`. Exportado a `outputs/tableau/grafico8_slope_rankings.png`.
- Gráfico 9: barras horizontales de INA. Exportado a `outputs/tableau/grafico9_ina_componentes_ic.png`.
- El gráfico 9 propaga únicamente los IC disponibles de `TAC_M` e `IBA`; `RC_real` no tiene IC territorial en la tabla actual, por lo que su contribución se mantiene fija. No debe interpretarse como IC completo del INA.
