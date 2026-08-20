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
**Fecha:** 2026-08-20 · **Estado:**  **abierta — requiere V-01**

`Mx404_6` ("No afrontó la situación") marca "Sí" en 10.625 registros (81,2%). Si significara "presenció y no afrontó", ocho de cada diez bogotanos habrían presenciado violencia contra una mujer, lo cual es implausible.

**Interpretación adoptada:** `_6 = 1` agrupa a quien no presenció con quien presenció y calló, **sin posibilidad de separarlos**. Solo `_6 = 0` es interpretable, como afrontamiento efectivo.

**Soporte aritmético:** 13.082 − 10.625 = 2.457 registros con `_6 = 0`; las marcas en `_1` a `_5` suman 3.217, es decir varias ubicaciones por persona. Consistente.

**Origen:** inferencia del equipo a partir de la regla de exclusividad del diccionario y de las frecuencias observadas. **No está confirmada contra el cuestionario original.** Ver V-01.

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
| **V-01** | Exclusividad del bloque 404: tabular `Mx404_6` contra el máximo de `Mx404_1..5` | 1.4 | **Cero** registros con `_6 = 1` y alguna marca en `_1..5`. Si aparece alguno, D-02 se revisa antes de seguir | rojo | *(pendiente)* |
| **V-02** | Filtro maestro: `df[df.Ax401 == 2].Jx402.isna().all()` y conteo de nulos = 11.094 | 1.2 | Ambas verdaderas | rojo | *(pendiente)* |
| **V-03** | Factores de expansión: suma de `fexp_calp_anu` contra población adulta proyectada de Bogotá | 1.7 | Diferencia ≤ 15%. Si no, revisar si el factor es bimestral y requiere promediarse | rojo | *(pendiente)* |
| **V-04** | Peso del supuesto heteronormativo (D-09) | 2.5 | Reportar el %. Si > 25%, correr variante excluyendo esos casos | rojo | *(pendiente)* |
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

> Cualquier cambio posterior al congelamiento de la Sección 1 se registra aquí. Formato: qué cambió, por qué, y si el cambio se decidió antes o después de ver el resultado afectado.

*(Sin enmiendas a la fecha.)*
