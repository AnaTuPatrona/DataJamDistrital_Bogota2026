# Hallazgos del Tableau y plan de recreación en ArcGIS StoryMaps

**Proyecto:** DataJam Distrital Bogotá 2026 — violencia contra las mujeres  
**Fecha de esta revisión:** 23 de noviembre de 2026  
**Evento:** 3 de diciembre de 2026  
**Duración prevista:** aproximadamente 10 minutos  
**Estado:** datos y siete recursos verificados; borrador con portada, apertura y cuatro escenas de Sidecar, incluidos ranking, dispersión y mapa interactivo. Ana Laura terminó manualmente las vistas del mapa según el filtro. Pendientes: prueba de gráfico vinculado, cierre, créditos y revisión final.

**Actualización de trabajo:** las secciones 2–7 describen el Tableau original y el diagnóstico inicial. La **sección 14** registra la verificación posterior y la versión que se utilizará para recrearlo. En esa versión, el cambio de al menos cuatro puestos corresponde a **12 de 19 localidades**, no a 13; la referencia administrativa es **enero–marzo de 2026** y la encuesta sigue siendo la de **2025**.

## 1. Encargo y decisiones de alcance

La referencia visual definitiva es **`C:/Users/Ana_L/Downloads/visual_presentación.twbx`**, junto con las dos capturas adjuntas. No se tomaron como referencia las versiones de Tableau ni las imágenes antiguas guardadas dentro del proyecto.

La presentación debe centrarse en **las fuentes de datos, la pregunta del proyecto y los hallazgos**, evitando explicar código, modelos o procedimientos estadísticos al público. Se mantendrán **tonos violetas**, de acuerdo con la preferencia de Ana Laura y su relación con la identidad de la Secretaría Distrital de la Mujer.

Ana Laura confirmó que **no han realizado cambios desde la DataJam**. Por tanto, la presentación no debe afirmar que desde entonces se incorporaron datos, se validaron resultados con entidades o se ampliaron las funcionalidades. La adaptación a StoryMaps será una nueva forma de comunicar el trabajo existente. Los próximos pasos deben presentarse como propuestas, no como actividades ya ejecutadas.

El proyecto obtuvo el **segundo lugar** en la DataJam, según la información proporcionada por Ana Laura.

### Material revisado

| Material | Uso en esta revisión |
|---|---|
| `visual_presentación.twbx`, en Descargas | Estructura, fórmulas, hojas, parámetros y acciones del visual definitivo. |
| Dos capturas adjuntas | Composición visible, título, tarjetas, colores y selector del mapa. |
| `../README.md` | Contexto del proyecto, equipo e inventario de fuentes. |
| `../docs/supuestos.md` | Definiciones, decisiones, límites y resultados documentados. |
| Tablas de `outputs` | Verificación de cifras y preparación de materiales de recreación. |
| Archivos originales de `../data` y script de geometrías | Comprobación de fechas y procedencia cartográfica. |
| Documentación oficial de Esri y fichas oficiales de Bogotá | Viabilidad de montaje y comprobación del significado de las fuentes. |

**Alcance de la auditoría:** se leyó el XML del `.twb` contenido en el paquete `.twbx` y se contrastó con los CSV del proyecto. **No se consultaron directamente los extractos `.hyper`**. Por ello, esta revisión no acredita una igualdad fila por fila entre cada extracto empaquetado y cada CSV. No se reejecutó el procesamiento ni se modificaron los archivos originales.

## 2. Qué contiene realmente el archivo de Tableau

El paquete incluye un libro `.twb` y **cuatro extractos `.hyper`**. El libro contiene **15 hojas**, tres dashboards y un objeto de historia.

### Dashboards e historia

| Nombre | Contenido | Tratamiento propuesto |
|---|---|---|
| **Bogotá mide su cobertura contra los casos que ya vio** | `H1a`, `H1b`, `H1c`, `H1d`, `Mapa`, `Rankings`, `Cuadrantes`. | **Es el dashboard principal que muestran las capturas y el que hay que recrear.** |
| **Por qué callan** | `Carga de cuidado`, `Modelos`, `Normas`, `Perfil de localidad`. | Material complementario; no incorporarlo automáticamente a una charla de 10 minutos. Su título también requiere cautela: la encuesta no identifica una tasa de silencio. |
| **Ranking de prioridad para la próxima infraestructura de atención y cuidado** | `Evolución`, `Franja horaria`, `Mapa`, `Prioridad`. | Material complementario; no convertirlo en recomendaciones definitivas de inversión. |
| **Historia 1** | Objeto de tipo historia de Tableau. | Su existencia no equivale a tener una historia creada en ArcGIS StoryMaps. |

Las 15 hojas son: `Carga de cuidado`, `Cuadrantes`, `Evolución`, `Franja horaria`, `H1a`, `H1b`, `H1c`, `H1d`, `Mapa`, `Metodología`, `Modelos`, `Normas`, `Perfil de localidad`, `Prioridad` y `Rankings`.

El dashboard principal usa **tamaño automático**, no un lienzo fijo de presentación. Su fondo está definido como **`#f3ebf3`**, con áreas de gráficos blancas. En el libro aparecen las familias tipográficas `Tableau Light` y `Segoe UI Variable Small Semibol`. En StoryMaps habrá que usar una tipografía disponible con apariencia y legibilidad equivalentes.

### Composición visible que debe conservarse conceptualmente

1. Título general.
2. Tarjetas de cifras destacadas en la parte superior.
3. Mapa de localidades a la izquierda.
4. Comparación de posiciones de cobertura a la derecha del mapa.
5. Dispersión territorial en la parte inferior.
6. Texto que explica cómo leer la dispersión.
7. Selector del indicador del mapa y leyenda de color.

En StoryMaps conviene repartir estas piezas en escenas sucesivas: una pantalla tan densa como la original resulta difícil de leer durante una exposición. La adaptación debe conservar **la pregunta, las comparaciones y la identidad violeta**, no necesariamente las mismas posiciones en píxeles.

## 3. Auditoría de las cuatro tarjetas

### 3.1 Tarjeta «Solo 20,1 % de las personas que ven violencia contra una mujer actúa»

**Cálculo encontrado:** `AVG(TAC_M)`, es decir, promedio simple de los indicadores de las 19 localidades.

| Medida | Valor verificado |
|---|---:|
| Promedio simple territorial | 20,113106 % |
| Valor mostrado, redondeado | 20,1 % |
| Estimación ponderada con los registros de la encuesta | 18,777262 %, aproximadamente 18,8 % |

**Problema:** la frase del dashboard usa un denominador que la encuesta no permite observar. La medida identifica a quienes **presenciaron y afrontaron** violencia contra una mujer. No permite separar a quienes presenciaron y no actuaron de quienes no presenciaron.

**Redacción que conserva la cifra del adjunto:**

> En promedio entre las 19 localidades, el 20,1 % de las personas reportó haber presenciado y afrontado violencia contra una mujer.

**Alternativa para hablar de la población representada por la encuesta:**

> El 18,8 % de las personas representadas por la encuesta reportó haber presenciado y afrontado violencia contra una mujer.

No mezclar ambas formas de agregación. Tampoco llamar a esta cifra prevalencia de violencia, porcentaje de víctimas o porcentaje de testigos que actúan.

### 3.2 Tarjeta «13 de 19 localidades cambian 4 o más puestos»

**Cálculo encontrado:** conteo de localidades distintas con `ABS(delta_rank) >= 4`.

El resultado **13 de 19** se reproduce con las tablas originales y también después de corregir el universo del ranking para que ambas columnas usen las mismas 19 localidades. Sin embargo, cambia la composición exacta de ese grupo.

**Problema detectado:** Sumapaz tiene cero casos en el denominador administrativo y una razón infinita. En la tabla original recibe el primer puesto administrativo y desplaza una posición a las otras localidades, aunque no dispone de comparación basada en encuesta.

**Corrección preparada:** ordenar ambas razones de mayor a menor únicamente entre las 19 localidades con encuesta y valores finitos. Los puestos deben ir de **1 a 19**, no hasta 20.

| Ejemplo | Puesto administrativo corregido | Puesto con referencia poblacional |
|---|---:|---:|
| Teusaquillo | 1 | 15 |
| Chapinero | 2 | 16 |
| Fontibón | 6 | 1 |
| La Candelaria | 19 | 9 |

**Límite:** esta es una comparación entre dos medidas sobre el análisis original; **no es un antes y después en el tiempo**. Además, los resultados de cobertura siguen sujetos a la revisión de periodos descrita en la sección 6.

### 3.3 Tarjeta «2,874 sobre 5. Así califica Bogotá el acceso a los medios para denunciar»

**Cálculo encontrado:** `AVG(IPSJ_C_prom)`, otro promedio simple de localidades.

| Medida | Valor verificado |
|---|---:|
| Promedio simple territorial | 2,874127753 sobre 5 |
| Promedio ponderado de respuestas válidas de la encuesta | 2,854492181 sobre 5 |

**Redacción propuesta para mantener el visual:**

> 2,874 sobre 5: calificación promedio entre localidades del acceso a la información y a los medios para denunciar delitos.

La pregunta se refiere a **delitos en general**. Es percepción de acceso, no tasa de denuncia, calidad del servicio ni valoración exclusiva de las rutas de violencia contra las mujeres. Para una cifra ponderada de ciudad correspondería mostrar aproximadamente **2,85 sobre 5**.

### 3.4 Tarjeta «En 1,000 de los hogares el trabajo doméstico y de cuidado recae en una sola mujer»

**Error confirmado en la configuración:** la hoja `H1d` filtra `dimension = carga_cuidado` y `categoria = Carga concentrada en mujer` antes de calcular la razón entre esa categoría y el conjunto de categorías de cuidado. El filtro restringe también el denominador, de modo que numerador y denominador quedan iguales.

El valor **1,000** corresponde al número decimal **1**, equivalente al 100 %; no significa mil hogares y no es un resultado válido sobre todos los hogares.

Al dividir la población expandida de la categoría femenina entre todas las categorías de cuidado se obtiene **22,542192 %**. Pero no basta con sustituir la tarjeta por ese porcentaje:

- Los pesos utilizados representan personas; no se verificó un estimador de hogares.
- La exportación agrupa tres categorías, mientras la documentación describe una clasificación más detallada.
- Concentración del cuidado no demuestra que absolutamente todas las tareas recaigan en una sola mujer.

**Decisión recomendada:** retirar esta tarjeta del relato principal hasta revisar su definición. Mantener tres cifras centrales es preferible a introducir una cuarta con una unidad incorrecta.

## 4. Qué hay que recrear en cada visual

### 4.1 Mapa de localidades y selector

El mapa representa polígonos de localidades y utiliza el parámetro **`p_Indicador_Mapa`**. Su opción inicial es **Necesidad No Atendida**.

| Opción del selector original | Medida activa del Tableau | Recreación y lectura correcta |
|---|---|---|
| Necesidad No Atendida | Promedio de `INA` | Índice relativo, no número ni porcentaje de mujeres sin atención. Su valor depende de pesos analíticos y de la cobertura provisional. |
| Violencia visible y afrontada | Promedio de `TAC_M` × 100 | Porcentaje de personas que presenciaron y afrontaron violencia contra una mujer. |
| Acceso a la denuncia | Promedio de `IPSJ_C_prom` | Puntaje de percepción de 1 a 5; valores altos significan mayor acceso percibido. |
| Cobertura real | Promedio de `RC_real` | Renombrar a **Cobertura estimada** o **Atención frente al volumen mínimo estimado**. |
| Cobertura administrativa | Promedio de `RC_admin` | Atenciones por registro de riesgo de feminicidio; no por cualquier caso de violencia. |
| Carga de cuidado en mujeres | Suma condicionada de `valor` en la tabla desagregada, multiplicada por 100 | No migrar al relato principal hasta verificar unidad, categorías y comportamiento al relacionar tablas. |

**Precisión importante:** aunque `pct_carga_mujer` está vacío en la tabla ancha, el cálculo activo más reciente del selector utiliza la tabla desagregada. El campo vacío, por sí solo, no prueba que la opción activa del mapa esté vacía. El motivo para dejarla pendiente es la definición y agregación no suficientemente conciliadas.

El campo activo de color es un **valor enmascarado**: solo devuelve un resultado si `publicable` y `en_encuesta` son verdaderos. Sumapaz debe conservarse geográficamente, pero sin estimación de encuesta; no debe aparecer como cero.

La leyenda **2,6241–3,2155** visible en la captura corresponde al **acceso percibido que colorea los círculos de la dispersión**, no al INA del mapa. En StoryMaps cada visual debe tener su propia leyenda y unidad.

El mapa del libro también tiene un filtro ligado al parámetro de cantidad de localidades, cuyo valor actual es **19**. No conviene trasladar ese filtro sin revisión: podría ocultar polígonos sin datos que deberían verse en gris.

### 4.2 Gráfico de cambio de posiciones

Es un diagrama de pendientes con dos columnas: cobertura administrativa y cobertura denominada «real» en el original. Cada línea corresponde a una localidad.

**Recrear específicamente:**

- Dos ejes de puestos con el número 1 arriba y el 19 abajo.
- Una línea por localidad y nombres legibles en sus extremos.
- Puestos recalculados sobre el mismo universo territorial.
- Destacar Teusaquillo, Chapinero y Fontibón como ejemplos narrativos.
- Explicar que un puesto más alto representa mayor razón de atención, no mayor necesidad.
- Indicar que no se trata de evolución temporal.

En el Tableau, el color y tamaño de las marcas del ranking se vinculan al **semáforo de necesidad**: sin dato; bajo, medio, alto y crítico, con cortes del INA en 25, 50 y 75. No representan población. Estos cortes son decisiones de clasificación, no umbrales clínicos ni normativos.

Para la exposición se propone simplificar el énfasis visual a unas pocas localidades. La imagen preparada es una **adaptación editorial**, no una copia píxel por píxel de todos los tamaños del original.

### 4.3 Gráfico de dispersión o cuadrantes

| Elemento | Configuración encontrada |
|---|---|
| Cada punto | Una localidad con ambas medidas disponibles. |
| Eje horizontal | `AVG(RC_real)`: atenciones por cada 1.000 mujeres del volumen mínimo estimado. |
| Eje vertical | `AVG(TAC_M)`, mostrado como porcentaje. |
| Tamaño del punto | `AVG(pob_mujeres)`: población femenina de la localidad. |
| Color del punto | `AVG(IPSJ_C_prom)`: acceso percibido a la denuncia. |
| Texto | Nombre de la localidad. |
| Línea vertical | Mediana territorial de cobertura: **135,883598**. |
| Línea horizontal | Mediana territorial de violencia visible y afrontada: **20,428921 %**. |

El rótulo «20 %» de la captura redondea demasiado la línea: para la nueva versión conviene **20,4 %**, y **135,9** para la mediana de cobertura.

La definición de cuadrantes considera «alto» estar **en o sobre** la mediana. Las líneas son referencias relativas a estas 19 localidades, no metas de política pública.

**Cambios de redacción recomendados:**

| Rótulo original | Rótulo descriptivo propuesto |
|---|---|
| Demanda desatendida | Mayor violencia visible / menor atención relativa |
| Zona de captura | Mayor violencia visible / mayor atención relativa |
| Zona opaca | Menor violencia visible / menor atención relativa |
| Sobreoferta relativa | Menor violencia visible / mayor atención relativa |

Una posición en el gráfico no demuestra que sobren recursos, que el sistema esté funcionando bien ni cuántas personas estén desatendidas. Además, la información de violencia visible interviene en el denominador de la cobertura: **los dos ejes no son independientes**. No usar la pendiente de la nube como prueba causal de una falla institucional.

### 4.4 Interacciones del dashboard original

El libro tiene acciones de selección desde **Mapa**, **Rankings** y **Cuadrantes** hacia otras vistas del dashboard. Las definiciones de esas acciones excluyen las cuatro tarjetas `H1a`–`H1d`, sugiriendo que las cifras superiores deben mantener el contexto general.

También permanecen filtros de acciones guardados en algunas hojas, incluidas tarjetas. Es una configuración que requiere prueba en la interfaz de Tableau para determinar su comportamiento exacto; no se verificó cada clic del dashboard en ejecución.

**Comportamiento objetivo para StoryMaps:** seleccionar una localidad debe resaltarla y mostrar sus datos, sin cambiar silenciosamente las cifras generales ni recalcular las medianas de referencia. Los rangos y las medianas deben conservar la base de 19 localidades.

No se debe prometer que las imágenes estáticas tendrán los filtros cruzados del Tableau. Para interacción mapa–dispersión se propone un mapa web con gráfico vinculado; el ranking puede mantenerse como imagen. Si se exige equivalencia exacta de todos los filtros, hará falta una aplicación embebida adicional y probarla dentro de StoryMaps.

## 5. Qué significan los indicadores y qué archivos los sostienen

| Concepto | Definición de trabajo | Archivos principales |
|---|---|---|
| Violencia visible y afrontada | Proporción ponderada de personas que reportan haber presenciado y afrontado violencia contra una mujer. | `encuesta_percepcion_legible.csv`; `fact_indicadores_localidad.csv`. |
| Acceso percibido | Calificación de información y medios para denunciar delitos, escala 1–5. | Los mismos archivos de encuesta e indicadores. |
| Oferta registrada | Suma de valores de Línea Púrpura y Duplas en los cortes seleccionados por el proyecto. Su interpretación temporal está pendiente. | `lineapurpura.csv`; `duplas.csv`. |
| Referencia administrativa | Registros de mujeres valoradas en riesgo de feminicidio; no todo tipo de violencia. | `riesgofeminicidio.csv`. |
| Cobertura administrativa | Oferta registrada dividida entre la referencia administrativa. | `RC_admin` en `fact_indicadores_localidad.csv`. |
| Cobertura estimada | Oferta registrada dividida entre el volumen mínimo estimado de mujeres que presenciaron y afrontaron violencia, por 1.000. | `RC_real` y `vol_afronto_mujeres`. |
| Necesidad no atendida | Índice relativo que combina violencia visible, barreras y menor cobertura. | `INA`; `ina_localidad.csv`; escenarios en `dim_parametros_ina.csv`. |
| Geografía y nombres | 20 localidades; 19 con encuesta. | `localidades_bogota.geojson`; `dim_localidad.csv`. |

En la metodología, la cobertura estimada se describe como una **cota superior de cobertura** bajo los supuestos del proyecto: utiliza un volumen mínimo observable y no toda la necesidad existente. No equivale al porcentaje de víctimas atendidas. Las unidades de las fuentes tampoco son intercambiables: atenciones, valoraciones de riesgo y personas que reportan experiencias son cosas distintas.

La ponderación documentada del INA es **40 % violencia visible, 30 % barreras y 30 % menor cobertura**, combinando posiciones relativas. Los pesos son decisiones explícitas del análisis. Hay cuatro escenarios: equilibrado, prioridad a violencia visible, prioridad a barrera de denuncia y prioridad a déficit de cobertura. Estos parámetros pertenecen al libro completo, pero no es necesario mostrarlos en la exposición principal.

### Campos vacíos y cálculos heredados

En la tabla ancha revisada están completamente vacíos `IPSJ_C_ic_inf`, `IPSJ_C_ic_sup`, `IBA`, `pct_carga_mujer`, `gad7_mod_sev` y `pobreza_subjetiva`. En la dimensión territorial también está vacío `pob_total_expandida`. No deben convertirse en ceros ni ofrecerse como filtros funcionales.

El INA ya calculado sí existe, pero **no puede reconstruirse de forma autónoma con el campo IBA vacío de esa tabla**. Para recalcularlo habrá que volver a su fuente y procedimiento documentados.

El libro contiene cálculos antiguos y versiones nuevas con nombres parecidos. Por ejemplo, un selector heredado usa «Barrera para denunciar», mientras el activo usa «Acceso a la denuncia». También existe una etiqueta de intervalo `C8` incompleta y otro cálculo de intervalo más completo. Su presencia no demuestra un defecto visible si no están utilizados. La migración debe tomar los campos efectivamente usados por cada hoja, no copiar toda la lista indiscriminadamente.

Se conserva el inventario completo de fórmulas extraídas en `auditoria/auditoria_dashboard.json`, apartado `calculos_tableau`.

## 6. Hallazgo prioritario: posible suma de cortes acumulados

El análisis original suma los cortes **junio, septiembre y diciembre de 2025 y marzo de 2026**. Las cifras de las fuentes evolucionan así:

| Serie | Marzo 2025 | Junio 2025 | Septiembre 2025 | Diciembre 2025 | Marzo 2026 |
|---|---:|---:|---:|---:|---:|
| Línea Púrpura | 9.155 | 18.397 | 27.946 | 35.693 | 8.252 |
| Duplas | 377 | 1.079 | 2.171 | 3.149 | 624 |
| Riesgo de feminicidio | No revisado en ese corte | 1.161 | 1.997 | 2.766 | 784 |

El crecimiento durante 2025 y el reinicio en 2026 es **fuertemente compatible con acumulación dentro de cada año**. La ficha oficial vigente de Línea Púrpura describe un periodo del **1 de enero al 30 de junio de 2026**. Los GeoJSON locales contienen una fecha de cierre, pero no una fecha inicial que permita confirmar por sí sola el significado de cada corte histórico. [Fuente oficial: Línea Púrpura](https://datosabiertos.bogota.gov.co/dataset/total-de-atenciones-por-linea-purpura-en-bogota-d-c-por-localidad).

**Lo que se sabe:** el procesamiento suma varios cortes y hay evidencia de posible solapamiento.  
**Lo que aún falta:** confirmar la cobertura temporal de cada archivo histórico y de cada fuente. No corresponde afirmar que todos los archivos históricos son acumulados solo por el patrón numérico.

Si junio, septiembre y diciembre son acumulados desde enero, sumarlos cuenta parte de los mismos periodos varias veces. Por eso:

- **97.311** es una suma de cortes del análisis original; no un total conciliado de atenciones en periodos independientes.
- **6.708** es la suma administrativa utilizada originalmente; tampoco debe presentarse como un número verificado de personas distintas.
- Esto puede afectar oferta, registros administrativos, ambas coberturas, posiciones, cuadrantes e INA.
- No afecta directamente a los indicadores obtenidos exclusivamente de la encuesta, como TAC y acceso percibido.
- El error de la tarjeta de cuidado y el ranking infinito de Sumapaz son problemas independientes.

### Cómo resolverlo antes de tratar las coberturas como resultados definitivos

1. Registrar, para cada recurso histórico, fecha inicial, fecha final, unidad de conteo y carácter acumulado o periódico.
2. Elegir una ventana comparable entre Línea Púrpura, Duplas y riesgo de feminicidio.
3. Si son acumulados, usar cortes o diferencias compatibles con esa ventana; no sumar acumulados sin descontar solapamientos.
4. Revisar revisiones retrospectivas y posibles diferencias negativas antes de convertir acumulados en incrementos.
5. Recalcular coberturas, rangos, medianas e INA en archivos nuevos y contrastarlos con el Tableau original.
6. Actualizar conjuntamente las cifras, los textos, los mapas y las leyendas.

**Hasta resolverlo:** los materiales de cobertura deben identificarse como **reproducción del análisis original con validación temporal pendiente**. La corrección del universo de 19 localidades no resuelve este segundo problema.

## 7. Fuentes que sí conviene contar en la presentación

| Fuente | Qué aporta | Referencia para créditos |
|---|---|---|
| Encuesta Distrital de Percepción 2025, Secretaría Distrital de Planeación | 13.082 respuestas; 19 localidades y 30 UPL urbanas. Experiencias reportadas y percepciones. | [Presentación institucional de resultados](https://bogota.gov.co/mi-ciudad/planeacion/encuesta-de-percepcion-2025-asi-percibe-la-ciudadania-bogota). No se localizó un enlace verificable al microdato exacto `base_ano_movil_2025.csv`; identificar también el archivo del proyecto. |
| Línea Púrpura, Secretaría Distrital de la Mujer | Atenciones iniciales por localidad; no personas únicas ni denuncias. | [Ficha oficial](https://datosabiertos.bogota.gov.co/dataset/total-de-atenciones-por-linea-purpura-en-bogota-d-c-por-localidad). |
| Duplas de Atención Psicosocial, Secretaría Distrital de la Mujer | Atenciones iniciales por localidad. | [Ficha oficial](https://datosabiertos.bogota.gov.co/dataset/total-de-atenciones-de-duplas-en-bogota-d-c-por-localidad). |
| Mujeres valoradas en riesgo de feminicidio, Secretaría Distrital de la Mujer / información médico-legal | Referencia de riesgo registrado. No son feminicidios ocurridos ni todos los casos de violencia. | [Ficha oficial](https://datosabiertos.bogota.gov.co/dataset/cifras-de-mujeres-valoradas-en-riesgo-de-feminicidio-en-bogota-d-c-segun-localidad). |
| Geometría de localidades | Localización territorial del análisis. | El script del proyecto obtiene la geometría de `data/duplas_062025.geojson`. Citar la capa distrital de Duplas y la adaptación cartográfica del equipo. No atribuirla a una descarga independiente que no se hizo. |

La Encuesta Bienal, las llamadas 123, los delitos sexuales y otros registros forman parte del proyecto amplio o de otros dashboards. No deben presentarse como si todos alimentaran cada cifra del dashboard central. La bitácora documenta que malnutrición y consumo problemático de sustancias fueron descartados del análisis propuesto, aunque aparezcan en el inventario general del README.

## 8. Cómo recrearlo en ArcGIS StoryMaps

### 8.1 Arquitectura propuesta

Usar **una historia de ArcGIS StoryMaps** con portada, fuentes, cifras, escenas de mapas y gráficos, y cierre. El bloque **Sidecar** permite alternar un panel narrativo y un panel visual, y configurar vistas o acciones de mapa. Es adecuado para repartir el dashboard en un recorrido que se pueda presentar oralmente. [Documentación oficial de Sidecar](https://doc.esri.com/en/arcgis-storymaps/latest/author-and-share/add-sidecars.html).

| Pieza original | Qué se recrea | Cómo |
|---|---|---|
| Título y contexto | Pregunta central, segundo lugar y autores | Portada y apertura breve. |
| Tarjetas | Tres cifras con universo y unidad explícitos | Bloques de texto o infografía; no capturas con letra pequeña. |
| Mapa | Localidades, selección y cinco indicadores conciliados o identificados como provisionales | Mapa web de ArcGIS; capa con los indicadores y ventanas emergentes. |
| Selector | Cambiar la lectura territorial | Capas o vistas del mapa y acciones en Sidecar. No prometer el mismo menú desplegable de Tableau. |
| Rankings | Dos columnas y 19 líneas con rótulos | PNG de alta resolución como primera implementación; la imagen no tendrá filtros. |
| Dispersión | Dos ejes, puntos, referencias y lectura territorial | Gráfico de Map Viewer vinculado al mapa si la cuenta y la interfaz lo permiten; PNG como alternativa de presentación. |
| Explicaciones | Una idea por escena | Párrafos cortos junto al visual correspondiente. |
| Metodología extensa | Procedencia y límites indispensables | Fuentes y notas al final; detalle completo en este documento de trabajo. |

StoryMaps dispone de gráficos nativos de barras, columnas, líneas, áreas y anillos. La dispersión no se construye con ese mismo bloque; Map Viewer dispone de gráficos de dispersión. Las imágenes preparadas permiten conservar el aspecto cuando un detalle no tenga equivalencia en el gráfico nativo. [Gráficos en StoryMaps](https://doc.esri.com/en/arcgis-storymaps/latest/author-and-share/add-charts.html), [gráficos de Map Viewer](https://www.esri.com/arcgis-blog/products/arcgis-online/analytics/map-viewer-charts-frequently-asked-questions-faqs).

La documentación vigente de Sidecar contempla **gráficos vinculados**: seleccionar elementos de un gráfico puede resaltar entidades del mapa. Esta integración debe probarse en la cuenta disponible; no se ha comprobado todavía con el gráfico de este proyecto. [Gráficos vinculados en Sidecar](https://doc.esri.com/en/arcgis-storymaps/latest/author-and-share/add-sidecars.html).

### 8.2 Datos para el mapa

Está preparada una capa con **20 polígonos en EPSG:4326**, sin respuestas individuales: `datos/localidades_storymaps.geojson`. Los indicadores no disponibles se conservan como `null`; el CSV equivalente usa celdas vacías.

| Campo preparado | Uso en ArcGIS |
|---|---|
| `codigo_localidad`, `nombre_localidad` | Identificación y título de ventana emergente. |
| `en_encuesta` | Explicar disponibilidad y evitar imputar cero. |
| `violencia_visible_pct` | Mapa porcentual y eje vertical de la dispersión. Ya está expresado de 0 a 100: no multiplicar otra vez. |
| `acceso_denuncia` | Mapa de acceso y color de la dispersión. |
| `cobertura_estimada` | Mapa y eje horizontal de la dispersión. |
| `cobertura_admin` | Mapa administrativo; razón no finita de Sumapaz convertida a nulo. |
| `necesidad_no_atendida` | INA recalculado para enero–marzo de 2026, con encuesta de 2025. |
| `rango_admin_19`, `rango_estimado_19`, `cambio_puestos_19` | Comparación coherente sobre 19 localidades. |
| `poblacion_mujeres` | Tamaño de puntos, si el gráfico admite esa codificación. |
| `estado_datos` | Mensaje de disponibilidad; no sustituye la advertencia sobre periodos administrativos. |

La capa usa los conteos de **enero–marzo de 2026**: 8.876 atenciones y 784 registros de riesgo en las 20 localidades. La encuesta sigue siendo de 2025. Las columnas originales se conservan como respaldo en la tabla de reconciliación, no como valores vigentes del mapa.

### 8.3 Pasos concretos de montaje

1. **Crear el mapa web.** Agregar `localidades_storymaps.geojson` desde Map Viewer y guardar el mapa. La modalidad de carga y la posibilidad de alojar una capa dependen de los permisos de la cuenta. [Agregar capas desde archivos](https://doc.esri.com/en/arcgis-online/latest/create-maps/add-layers-from-file.html).
2. **Configurar cinco lecturas.** INA, violencia visible, acceso, cobertura estimada y cobertura administrativa. Conservar una leyenda propia y la unidad de cada una; utilizar gris para ausencia de datos.
3. **Configurar ventanas emergentes.** Mostrar localidad, valor y unidad, definición breve y condición de disponibilidad. Evitar abreviaturas como `RC_real`, fórmulas o nombres de campos frente al público.
4. **Configurar la dispersión.** Eje X=`cobertura_estimada`; eje Y=`violencia_visible_pct`; guías en **12,0738** y **20,4289** en la versión conciliada. Mantener referencias fijas del conjunto de 19 localidades. Verificar qué opciones de tamaño, color y rótulos permite la interfaz; si no conserva la lectura, usar la imagen y el mapa interactivo por separado.
5. **Crear la historia.** Portada, breve explicación de fuentes y un Sidecar con las escenas del recorrido. Incorporar el mapa guardado mediante el selector de mapas de StoryMaps. [Agregar mapas](https://doc.esri.com/en/arcgis-storymaps/latest/author-and-share/add-maps.html).
6. **Añadir rankings e imágenes.** Usar los archivos finales indicados en el inventario, con pies de figura y textos alternativos. No usar versiones antiguas de `outputs/tableau`.
7. **Aplicar el tema violeta.** Mantener el fondo lila claro, texto oscuro y gráficos de contraste suficiente. No se ha verificado un manual oficial de marca; la paleta propuesta es una adaptación del dashboard, no una identidad institucional certificada.
8. **Comprobar el recorrido.** Revisar legibilidad en pantalla de presentación y móvil, navegación, leyendas, selección, nombres de localidades y conservación de nulos.
9. **Verificar acceso de la audiencia antes de publicar.** La historia, el mapa y las capas deben tener permisos compatibles. El estado de publicación se decide después de revisar el contenido y resolver o declarar las limitaciones.

### 8.4 Propuesta de color

| Función | Color propuesto |
|---|---|
| Fondo general | `#F3EBF3`, tomado del Tableau |
| Títulos y énfasis | Violeta profundo `#57245F` |
| Escala de valores | Lila claro `#E7C5E1` a ciruela `#754078` |
| Texto principal | Gris violáceo oscuro `#302A34` |
| Paneles de gráficos | Blanco `#FFFFFF` |
| Sin datos | Gris `#D8D5DB` |

Un tono intenso debe significar **mayor valor**, no automáticamente «peor». Por ejemplo, un acceso percibido mayor tiene una lectura diferente de una necesidad mayor. Las leyendas y títulos deben hacerlo explícito.

## 9. Recorrido propuesto de 10 minutos

| Tiempo | Escena | Mensaje principal | Recurso |
|---|---|---|---|
| 0:00–0:45 | Pregunta de apertura | ¿Cambia la lectura de la atención cuando miramos más allá de los casos registrados? | Portada y Bogotá. |
| 0:45–2:00 | Fuentes | Registros institucionales y encuesta muestran partes distintas del problema. | Tarjetas de fuentes y alcance territorial. |
| 2:00–3:15 | Lo visible es una parte | 20,1 % como promedio de localidades; 2,874/5 de acceso percibido, con etiquetas correctas. | Cifras y mapa de encuesta. |
| 3:15–5:15 | Cambio de posiciones | 12 de 19 localidades cambian al menos cuatro puestos; ejemplos de Teusaquillo, Chapinero y Antonio Nariño. | Rankings conciliados de enero–marzo de 2026. |
| 5:15–7:30 | Lectura territorial | Cómo leer cada punto y qué preguntas abre la comparación. | Dispersión y mapa. |
| 7:30–9:00 | Cambiar la mirada | Recorrido breve por acceso, violencia visible y necesidad relativa. | Acciones de mapa; no recorrer todos los indicadores sin explicación. |
| 9:00–10:00 | Aporte y continuidad | Integración de miradas; límites; próximos pasos propuestos. No atribuir avances inexistentes desde la DataJam. | Cierre y fuentes. |

La conciliación administrativa quedó resuelta con el trimestre común documentado en la sección 14. El recorrido debe conservar la diferencia entre registros de 2026 y encuesta de 2025, sin presentar estas razones como porcentajes efectivos de mujeres atendidas.

## 10. Hallazgos complementarios que no conviene exagerar

La documentación reporta una asociación entre concentración femenina del cuidado y menor acceso percibido, pero no respalda convertirla en una afirmación causal como «el cuidado impide denunciar». Los mecanismos específicos de afrontamiento y mediación por confianza vecinal no quedaron sostenidos como se esperaba.

La no injerencia no emergió en la Encuesta Bienal como un factor independiente y puro. Por ello, no presentar «la no injerencia es la causa principal» como hallazgo confirmado.

Con 19 localidades, los rankings son comparaciones descriptivas. No deben convertirse automáticamente en un orden definitivo de inversión ni en conclusiones sobre personas individuales.

## 11. Materiales que ya quedaron preparados

Todos están dentro de `outputs/storymaps_preparacion`. Son materiales locales de trabajo; **no acreditan una publicación en ArcGIS**.

| Archivo | Contenido y estado |
|---|---|
| `auditoria/auditoria_dashboard.json` | Cifras comprobadas, fórmulas extraídas, rankings originales y corregidos, alertas. |
| `textos_storymaps.txt` y `textos_storymaps_2026t1.txt` | Textos de montaje con cifras conciliadas, fuentes y límites; ocho escenas más créditos. |
| `notas_exposicion_10_minutos.txt` | Intervenciones orales y pausas distribuidas en diez minutos; pendiente ensayo con la historia montada. |
| `datos/localidades_storymaps.geojson` | Capa territorial de 20 localidades con indicadores agregados y nulos explícitos. |
| `datos/indicadores_storymaps.csv` | Tabla equivalente para consultar o reutilizar. |
| `recursos/01_mapa_ina.png` | INA recalculado, con periodo y alcance explícitos. |
| `recursos/02_rankings.png` | Comparación de rangos recalculados entre 19 localidades. |
| `recursos/03_dispersion.png` | Dispersión con unidades y medianas precisas. |
| `recursos/04_mapa_acceso.png` | Acceso percibido a la denuncia. |
| `recursos/05_mapa_violencia.png` | Violencia visible y afrontada. |
| `recursos/06_mapa_cobertura_estimada.png` | Cobertura estimada para enero–marzo de 2026, con referencia poblacional de 2025. |
| `recursos/07_mapa_cobertura_administrativa.png` | Razón administrativa del trimestre común de enero–marzo de 2026. |
| `guia_recursos.json` | Inventario de activos, pies de figura, textos alternativos y campos. |
| `produccion/generar_recursos.py` y `auditoria/auditar.py` | Soporte reproducible de la preparación; no forman parte de la presentación pública. |

Existen archivos gráficos intermedios con otros nombres dentro de `recursos`. Para el montaje se deben usar los **siete nombres de esta tabla**, que corresponden al inventario vigente. La revisión visual final en StoryMaps y en la pantalla de presentación aún está pendiente.

## 12. Pendientes y criterios para dar por terminada la recreación

| Pendiente | Qué permitiría cerrarlo |
|---|---|
| Interpretación temporal de los cortes | Resuelta para la ventana elegida; evidencia y excepción de diciembre de Duplas en sección 14. |
| Cifras de cobertura y prioridad | Recalculadas y verificadas; falta cotejarlas después del montaje en la cuenta. |
| Tarjeta y mapa de cuidado | Revisar categoría, unidad y ponderación; mientras tanto, no incorporarlos al núcleo. |
| Interacciones | Se eligió mapa interactivo con imágenes: no hay selección cruzada en StoryMaps. Las cifras y medianas permanecen fijas. Las cinco acciones del mapa están en revisión final. |
| Montaje en cuenta | Historia, mapa y capa guardados; cuatro escenas, cinco acciones de mapa, cierre y fuentes incorporados. Revisión final en curso. |
| Guion final | Textos y notas preparados; falta ensayo completo con la historia montada. |
| Publicación | Historia en borrador; mapa y capa con acceso de propietario. El tema violeta fue publicado de forma privada para aplicarlo. Falta definir acceso de la audiencia. |

La recreación estará terminada cuando exista una historia guardada y revisada que conserve los tres visuales centrales, use violetas, explique correctamente las unidades, mantenga Sumapaz sin imputación, distinga resultados firmes de provisionales y permita presentar el proyecto en aproximadamente diez minutos.

## 13. Lista de tareas paso por paso y estado de avance

Esta lista será el registro de avance del trabajo. Las tareas pendientes quedan **sin indicación de estado**. Las tareas comenzadas llevan **(EN PROCESO)** y las terminadas llevan **(FINALIZADAS)**, al lado de su descripción. El estado de una tarea principal solo pasará a finalizada cuando se hayan cerrado todas sus subtareas aplicables. Preparar un borrador o un archivo local no equivale a terminar su montaje y verificación en StoryMaps.

El orden siguiente organiza la ejecución. Si una revisión cambia una cifra, se actualizarán también los textos y visuales que dependan de ella antes de cerrar las tareas correspondientes.

1. **Fijar el alcance y las referencias de la presentación** (FINALIZADAS)

   - **1.1. Identificar el Tableau adjunto y las dos capturas como la referencia visual definitiva** (FINALIZADAS)
   - **1.2. Revisar el README y la bitácora de supuestos para entender la pregunta, las fuentes y los límites del proyecto** (FINALIZADAS)
   - **1.3. Registrar la duración aproximada de 10 minutos, la preferencia por violetas y el enfoque en fuentes y hallazgos** (FINALIZADAS)
   - **1.4. Dejar documentado que no hubo cambios del proyecto desde la DataJam y evitar atribuir avances inexistentes** (FINALIZADAS)

2. **Auditar la estructura y los cálculos del Tableau definitivo** (FINALIZADAS)

   - **2.1. Identificar dashboards, hojas, parámetros, fórmulas y acciones de selección en el libro empaquetado** (FINALIZADAS)
   - **2.2. Contrastar las cuatro tarjetas principales con los CSV y documentar sus unidades y formas de agregación** (FINALIZADAS)
   - **2.3. Identificar el error de la tarjeta de cuidado y el efecto de Sumapaz sobre el ranking administrativo** (FINALIZADAS)
   - **2.4. Documentar las medidas del mapa, la dispersión, sus medianas y las diferencias entre las leyendas** (FINALIZADAS)
   - **2.5. Guardar los hallazgos, las fórmulas extraídas y los límites de la auditoría en este documento y en el archivo de respaldo** (FINALIZADAS)

3. **Resolver la interpretación temporal de los registros administrativos** (FINALIZADAS)

   - **3.1. Comparar los totales de los cortes disponibles y localizar evidencia de posible acumulación anual** (FINALIZADAS)
   - **3.2. Verificar en los metadatos históricos de Línea Púrpura, Duplas y riesgo de feminicidio si cada corte es acumulado o corresponde a un periodo independiente** (FINALIZADAS)
   - **3.3. Registrar la fecha inicial, la fecha final y la unidad de conteo de cada recurso utilizado** (FINALIZADAS)
   - **3.4. Definir una ventana temporal comparable y el tratamiento de posibles solapamientos entre cortes** (FINALIZADAS)
   - **3.5. Si los metadatos no permiten resolverlo, documentar exactamente qué sigue incierto y mantener las comparaciones afectadas como reproducción provisional del análisis original** (FINALIZADAS)

4. **Consolidar las cifras y definiciones que se usarán en la historia** (FINALIZADAS)

   - **4.1. Verificar el 20,1 % y el 2,874/5 como promedios entre localidades, distinguiéndolos de los promedios ponderados de ciudad** (FINALIZADAS)
   - **4.2. Recalcular los rangos del análisis original usando las mismas 19 localidades con valores comparables** (FINALIZADAS)
   - **4.3. Ajustar, si corresponde tras la tarea 3, los conteos, las coberturas, los rankings, las medianas, los cuadrantes y el INA en archivos nuevos** (FINALIZADAS)
   - **4.4. Verificar que tarjetas, mapa, rankings y dispersión usen la misma versión de los datos y el mismo universo territorial** (FINALIZADAS)
   - **4.5. Cerrar las etiquetas públicas: personas que presenciaron y afrontaron, acceso percibido, atenciones y cobertura estimada; excluir la tarjeta de cuidado mientras su definición siga pendiente** (FINALIZADAS)

5. **Preparar y verificar la capa de datos para ArcGIS** (FINALIZADAS)

   - **5.1. Crear una primera capa GeoJSON de 20 localidades y su tabla CSV equivalente con datos agregados** (FINALIZADAS)
   - **5.2. Conservar valores ausentes como nulos y convertir la razón infinita de Sumapaz en un valor no disponible** (FINALIZADAS)
   - **5.3. Actualizar la capa y la tabla con las cifras y el estado de validación que resulten de las tareas 3 y 4** (FINALIZADAS)
   - **5.4. Verificar geometrías, códigos, nombres, unidades, valores finitos y ausencia de duplicados por localidad** (FINALIZADAS)
   - **5.5. Comprobar que los campos destinados a ventanas emergentes no presenten sumas provisionales como totales definitivos** (FINALIZADAS)

6. **Cerrar el guion narrativo de aproximadamente 10 minutos** (FINALIZADAS)

   - **6.1. Preparar un primer borrador de textos y una distribución de tiempos por escena** (FINALIZADAS)
   - **6.2. Ajustar el relato a apertura, fuentes, cifras de encuesta, comparación de posiciones, lectura territorial y cierre** (FINALIZADAS)
   - **6.3. Incorporar las cifras definitivas o las advertencias de provisionalidad que correspondan, sin convertir la exposición en una explicación técnica** (FINALIZADAS)
   - **6.4. Redactar los textos visibles, los pies de figura y las notas de exposición, diferenciando lo que se leerá en pantalla de lo que se explicará oralmente** (FINALIZADAS)
   - **6.5. Presentar los próximos pasos como propuestas y dejar explícito el aporte del proyecto existente, sin inventar una evolución posterior a la DataJam** (FINALIZADAS)

7. **Terminar los recursos visuales y sus versiones de respaldo** (FINALIZADAS)

   - **7.1. Generar una primera versión de los cinco mapas, el gráfico de rankings y la dispersión en tonos violetas** (FINALIZADAS)
   - **7.2. Preparar un inventario con nombres de archivo, pies de figura y textos alternativos** (FINALIZADAS)
   - **7.3. Actualizar los gráficos que cambien al conciliar los datos y comprobar que coincidan con la capa final** (FINALIZADAS)
   - **7.4. Revisar visualmente rótulos, tamaños, contraste, leyendas, unidades y posibles superposiciones o recortes** (FINALIZADAS)
   - **7.5. Identificar claramente los archivos finales para el montaje y conservar copias estáticas de respaldo para la exposición** (FINALIZADAS)

8. **Comprobar las funciones disponibles en la cuenta de ArcGIS** (FINALIZADAS)

   - **8.1. Abrir StoryMaps y verificar que la sesión iniciada por Ana Laura permite acceder al contenido de la cuenta** (FINALIZADAS)
   - **8.2. Comprobar si la cuenta permite crear historias, guardar mapas y agregar la capa preparada** (FINALIZADAS)
   - **8.3. Comprobar la disponibilidad de gráficos de Map Viewer, gráficos vinculados y acciones de mapa en Sidecar** (FINALIZADAS)
   - **8.4. Definir la implementación disponible: mapa y gráfico vinculados cuando sea posible, o mapa interactivo acompañado por imágenes cuando no lo sea** (FINALIZADAS)

9. **Construir el mapa web de localidades** (FINALIZADAS)

   - **9.1. Cargar la capa verificada y guardar el mapa con un nombre identificable del proyecto** (FINALIZADAS)
   - **9.2. Configurar las cinco lecturas: necesidad no atendida, violencia visible y afrontada, acceso percibido, cobertura estimada y cobertura administrativa** (FINALIZADAS)
   - **9.3. Aplicar escalas violetas, leyendas con unidades y gris para indicadores sin datos** (FINALIZADAS)
   - **9.4. Configurar ventanas emergentes con nombre de localidad, valor, unidad, definición breve y alcance del dato** (FINALIZADAS)
   - **9.5. Verificar que Sumapaz siga visible como territorio, sin atribuirle estimaciones de encuesta ni cobertura infinita** (FINALIZADAS)

10. **Recrear la comparación de posiciones, la dispersión y las interacciones** (FINALIZADAS)

    - **10.1. Incorporar el ranking de 19 localidades con nombres legibles y ejemplos destacados; explicar que compara dos medidas, no dos momentos** (FINALIZADAS)
    - **10.2. Configurar la dispersión con cobertura estimada en el eje horizontal y violencia visible y afrontada en el vertical** (FINALIZADAS)
    - **10.3. Incorporar las medianas correspondientes a la versión final de datos y explicar que no son metas de política pública** (FINALIZADAS)
    - **10.4. Reproducir color por acceso y tamaño por población cuando la herramienta lo permita; documentar cualquier simplificación visual necesaria** (FINALIZADAS)
    - **10.5. Probar el resaltado o selección de localidades entre mapa y gráfico, manteniendo fijas las cifras generales y la base territorial de comparación** (FINALIZADAS)

11. **Montar la historia completa en StoryMaps** (FINALIZADAS)

    - **11.1. Crear la portada con título, subtítulo, equipo, referencia a la DataJam y fecha del evento** (FINALIZADAS)
    - **11.2. Incorporar la pregunta central, las fuentes y las tres cifras principales con sus etiquetas corregidas** (FINALIZADAS)
    - **11.3. Construir las escenas de Sidecar e insertar el mapa, los rankings y la dispersión en el orden del guion** (FINALIZADAS)
    - **11.4. Configurar las acciones que permitan cambiar de indicador o recorrer localidades sin saturar la presentación** (FINALIZADAS)
    - **11.5. Añadir el cierre, los próximos pasos propuestos, los créditos, las fuentes enlazadas y los límites relevantes** (FINALIZADAS)
    - **11.6. Aplicar el tema violeta, una tipografía legible y textos alternativos; guardar la historia** (FINALIZADAS)

12. **Revisar, ensayar y entregar la versión preparada para el evento** (EN PROCESO)

    - **12.1. Recorrer toda la historia y cotejar cada cifra, etiqueta, fuente y localidad con los archivos finales** (EN PROCESO)
    - **12.2. Probar navegación, mapas, selección, leyendas e imágenes en pantalla amplia y móvil** (EN PROCESO)
    - **12.3. Revisar que las advertencias temporales sigan visibles donde sean necesarias y que ningún gráfico sugiera causalidad o prevalencia total** (EN PROCESO)
    - **12.4. Ensayar el recorrido de aproximadamente 10 minutos y ajustar la cantidad de texto y ejemplos al tiempo disponible** (EN PROCESO)
    - **12.5. Verificar el guardado, entregar el enlace de la historia y organizar los recursos de respaldo** (EN PROCESO)
    - **12.6. Definir el acceso para la audiencia y, si se solicita publicar, comprobar los permisos de historia, mapa y capas y verificar el enlace de lectura**
    - **12.7. Actualizar esta lista con el estado real de cada tarea y dejar registrados los pendientes que no se hayan resuelto** (EN PROCESO)

## 14. Verificación posterior y versión de trabajo para StoryMaps

### 14.1 Resultado de la consulta del historial oficial

Se consultó directamente la API pública de Datos Abiertos Bogotá y su historial de revisiones, conservando copias de las respuestas en `auditoria/fuentes_temporales`. Esto permitió consultar descripciones anteriores, no solamente la ficha vigente.

Las revisiones históricas describen los cortes de **junio y septiembre de 2025 como periodos desde enero hasta el corte**, en las tres fuentes. También describen expresamente **enero–marzo de 2026** para Línea Púrpura, Duplas y riesgo de feminicidio. Por tanto, la suma original de junio, septiembre y diciembre no debe interpretarse como una suma de trimestres independientes.

| Fuente | Periodo elegido y confirmado | Revisión histórica que lo describe | Identificador de la revisión |
|---|---|---|---|
| Línea Púrpura | 1 de enero–31 de marzo de 2026 | 3 de agosto de 2026 | `a77e2233-76fe-45a4-8855-4a500686c08e` |
| Duplas | 1 de enero–31 de marzo de 2026 | 3 de agosto de 2026 | `8503d7f6-1575-4bc8-8ce1-c6a24e918e5d` |
| Riesgo de feminicidio | Enero–marzo de 2026 | 3 de agosto de 2026 | `4ed96a55-6612-4056-942f-88d64a247051` |

Las evidencias están en los historiales públicos de [Línea Púrpura](https://datosabiertos.bogota.gov.co/api/3/action/package_activity_list?id=7fe534b6-b90e-4aa0-8bd2-086957b97b57&limit=100&include_data=true), [Duplas](https://datosabiertos.bogota.gov.co/api/3/action/package_activity_list?id=421e2e59-19fb-43f7-be61-674e402c1808&limit=100&include_data=true) y [riesgo de feminicidio](https://datosabiertos.bogota.gov.co/api/3/action/package_activity_list?id=94a36c8e-8a4f-46b7-b75a-00e5c9668ddf&limit=100&include_data=true). Las fechas de estas revisiones son fechas de edición del catálogo, no fechas de ocurrencia de las atenciones.

**Excepción documentada:** no se encontró una descripción histórica explícita de enero–diciembre de 2025 para el archivo de Duplas de diciembre. El paquete cartográfico oficial de ese corte incluye un archivo de metadatos vacío. No se da por verificado ese intervalo; ese corte queda **fuera de la nueva comparación**. Las descripciones de diciembre de Línea Púrpura y riesgo sí indican enero–diciembre de 2025.

También se descargaron las copias oficiales de los tres GeoJSON de marzo de 2026 para cotejarlas con las del proyecto. Los **20 conjuntos de propiedades por archivo coinciden exactamente**. Los archivos no tienen el mismo hash binario, por lo que la comprobación se refiere a sus propiedades y valores, no a una identidad de todos sus bytes o geometrías. Los datos usados para recalcular siguen siendo los archivos originales del proyecto.

### 14.2 Decisión de periodo y alcance

La versión de StoryMaps utilizará **enero–marzo de 2026**, el corte más reciente ya presente en el proyecto con intervalo común explícito en las tres fuentes. Se toma cada corte una sola vez. No se añadieron los datos nuevos de junio o septiembre de 2026 que actualmente ofrece el portal.

La encuesta sigue correspondiendo al **año 2025**. Esta diferencia se indicará en el relato y en los gráficos: se comparan atenciones del primer trimestre de 2026 con una referencia poblacional de encuesta de 2025. La razón resultante no representa una probabilidad de atención ni un porcentaje efectivo de víctimas atendidas durante un mismo intervalo.

Esta decisión corrige la agregación temporal y fija una ventana distinta de la suma original. Por ello, los valores nuevos no deben interpretarse como una caída temporal de la atención frente al número antiguo.

### 14.3 Resultados recalculados

| Elemento | Versión original | Versión para StoryMaps |
|---|---:|---:|
| Ventana administrativa | Suma de cortes solapados de 2025 y marzo de 2026 | Enero–marzo de 2026, sin sumar cortes |
| Atenciones de Línea Púrpura, 20 localidades | 90.288 en la suma original | 8.252 |
| Atenciones de Duplas, 20 localidades | 7.023 en la suma original | 624 |
| Atenciones combinadas, 20 localidades | 97.311 en la suma original | 8.876 |
| Registros de riesgo, 20 localidades | 6.708 en la suma original | 784 |
| Atenciones combinadas en las 19 localidades comparables | — | 8.872 |
| Promedio territorial de violencia visible y afrontada | 20,1 % | 20,1 % |
| Promedio territorial de acceso percibido | 2,874/5 | 2,874/5 |
| Localidades que cambian al menos cuatro puestos | 13 de 19 | **12 de 19** |
| Mediana de cobertura estimada | 135,8836 | **12,0738** atenciones por cada 1.000 mujeres del volumen mínimo estimado |
| Mediana de violencia visible y afrontada | 20,4289 % | 20,4289 % |

Las cuatro atenciones que diferencian el total de 20 localidades del de 19 corresponden a Sumapaz. Se conservan en el total administrativo, pero no se incorpora Sumapaz a los rankings con encuesta.

Los ejemplos del ranking también cambian: **Teusaquillo pasa del puesto 4 al 17; Chapinero, del 5 al 18; y Antonio Nariño, del 11 al 1**. Estos movimientos comparan las dos razones en la nueva ventana; no son cambios en el tiempo. Fontibón pasa del 3 al 2, por lo que ya no conviene usarla como ejemplo principal de una gran divergencia.

El INA se recalculó con los mismos pesos del proyecto. Su componente de barreras se recuperó de `ina_localidad.csv`, que sí contiene `IBA_promedio`; el vacío de la tabla ancha no se sustituyó por cero. No se añadieron atenciones de Duplas Público, para conservar la definición de oferta del análisis original.

### 14.4 Respaldo de la verificación

| Archivo | Contenido |
|---|---|
| `auditoria/verificacion_periodos.csv` y `.json` | Inventario de los 14 archivos administrativos originales, sus cortes, unidades, totales, recursos oficiales y evidencia histórica disponible. |
| `auditoria/fuentes_temporales/*_ckan.json` | Fichas públicas consultadas directamente. |
| `auditoria/fuentes_temporales/*_historial.json` | Revisiones históricas utilizadas para verificar los intervalos. |
| `auditoria/fuentes_temporales/comprobacion_archivos_marzo2026.json` | Comparación de propiedades y hashes entre los archivos locales y oficiales de marzo. |
| `datos/indicadores_reconciliados_2026t1.csv` y `.json` | Indicadores recalculados, conservando columnas de referencia de la versión original. |
| `auditoria/resumen_reconciliacion_2026t1.json` | Totales, medianas, cifras principales, rankings y decisión de periodo. |

Los archivos originales de `outputs` y `data`, el Tableau adjunto y su auditoría inicial se conservan sin sobrescribir. Los siete recursos de montaje, la capa, la tabla, sus pies de figura, los textos y las notas ya usan esta versión. Las versiones previas están en `version_original_preconciliacion`.

### 14.5 Revisión local final y restricción de fuentes

Las 16 comprobaciones de `auditoria/verificacion_resultados_2026t1.json` resultaron correctas: coincidencia de capa y tabla, 20 códigos únicos, 19 rangos comparables, conteos, medianas, 12 cambios de al menos cuatro puestos, nulos de Sumapaz y concordancia con los CSV del proyecto. La revisión geométrica cubre estructura, cierre de anillos y coordenadas; no constituye una nueva auditoría topológica.

Se revisaron visualmente los siete recursos finales: nombres, contraste, escalas y rótulos. Se corrigió la superposición de la mediana horizontal con las marcas del eje y se conservaron pies de figura con los periodos. La inspección dentro de StoryMaps y en móvil sigue pendiente.

Por instrucción de Ana Laura, **desde este punto no se harán nuevas búsquedas ni consultas de fuentes**. Se trabajará con los archivos, evidencias y enlaces ya disponibles. El acceso a la cuenta de StoryMaps se utilizará para el montaje autorizado, no para ampliar la investigación.

### 14.6 Regla de continuidad solicitada

Ana Laura indicó: usar los restablecimientos cuando quede **10 % o menos del límite** y, cuando quede **un solo restablecimiento**, detener la tarea en curso y registrar aquí el punto de detención. La sesión no expone un contador consultable de límite restante ni de restablecimientos disponibles; no se afirmará haber aplicado ese umbral sin una señal verificable del sistema. Si esa señal aparece, se anotarán la tarea activa, lo guardado y el siguiente paso antes de detenerse.

Estado actual: no se ha recibido una señal verificable de que quede un solo restablecimiento. Continúa el montaje. El editor de StoryMaps ya permite iniciar una historia; su pantalla anterior ocultaba las opciones porque el tamaño de ventana era insuficiente.

### 14.7 Montaje guardado en ArcGIS

- [Capa alojada de localidades e indicadores](https://edx-esri-co.maps.arcgis.com/home/item.html?id=1ccea30704a1457d9667231d2fc8a166): creada con los datos conciliados; acceso de propietario al crearla.
- [Mapa de atención y violencia visible](https://edx-esri-co.maps.arcgis.com/apps/mapviewer/index.html?webmap=afcf0361006e430084b9bf171bdefba2): guardado con el INA en escala violeta, valores ausentes identificados y ventanas emergentes que explican las cinco medidas, sus unidades y periodos. Se verificó la consulta de Usme. Las cinco vistas y la integración con la historia ya están incorporadas; su revisión final continúa.




Las cinco vistas del mapa quedaron guardadas con escalas violetas, etiquetas públicas y valores ausentes en gris. Se verificó la ventana de Sumapaz sin estimaciones ni infinito. La dispersión nativa incluye 19 puntos, ejes, medianas fijas y tamaño por población femenina. Se seleccionó Santa Fe y se confirmó su consulta. En esta versión interactiva se usa un solo violeta; la imagen de respaldo conserva además el color por acceso percibido. La selección dentro de StoryMaps todavía debe probarse.


**Avance del 23 de noviembre de 2026:**

- [Historia en edición](https://storymaps.arcgis.com/stories/d8fe4e13f51c42c3b4a7617e04907871/edit): borrador guardado con título, subtítulo, autores, fuentes, tres cifras corregidas y primeras escenas de Sidecar. Mapa de violencia visible y ranking insertados sin recorte y con textos alternativos.
- [Tema violeta](https://storymaps.arcgis.com/themes/72da125bfd4d417d9e8285826d572a85/edit): aplicado a la historia. Fondo lila claro y acentos violetas; tema disponible solo para el propietario.
- La historia, el mapa y la capa no se han publicado para una audiencia abierta. La publicación de la historia y la revisión de accesos para el evento siguen pendientes.
- La dispersión y el mapa interactivo ya están insertados. Continúan el cierre, los créditos y la revisión en pantalla amplia y móvil. No se han consultado nuevas fuentes.
**Actualización solicitada por Ana Laura, 23 de noviembre de 2026:**

- Ana Laura informó que terminó manualmente las vistas del mapa según el filtro. La tarea **11.4 queda (FINALIZADAS)** con esa autoría explícita. Su funcionamiento se revisará en la tarea 12.2; no se rehace esta configuración.
- Las cuatro escenas de Sidecar ya contienen: violencia visible, comparación de posiciones, dispersión y mapa interactivo. La tarea **11.3 queda (FINALIZADAS)**. Las tres imágenes están ajustadas sin recorte y con texto alternativo.
- Se confirmó en la interfaz la disponibilidad de **Linked chart (Beta)** y de acciones de mapa; la tarea 8.3 queda finalizada. Falta probar la vinculación efectiva entre la dispersión y el mapa (10.5) y cerrar la implementación elegida (8.4).
- Antes de la intervención manual había quedado un párrafo fuera del Sidecar con el texto repetido «Las diferencias tienen territorio». Se revisará el estado actual y, si sigue allí, se usará ese espacio para el cierre de la historia.
- Siguiente paso: revisar la versión actual guardada, respetar las vistas configuradas por Ana Laura y continuar con gráfico vinculado, cierre, fuentes y comprobación final.
**Cierre del montaje y decisión de interactividad:**

- Se comprobó que las cinco acciones configuradas por Ana Laura están guardadas. La vista de cobertura estimada dibuja el territorio completo y mantiene Sumapaz en gris.
- La opción «Linked chart (Beta)» observada anteriormente no aparece en el menú actual, ni en la vista inicial ni al activar cobertura estimada. La prueba de la tarea 10.5 se cierra con esta limitación: **no se implementa selección cruzada en StoryMaps**. La selección en Map Viewer sí fue probada anteriormente. No se atribuye a la historia una interacción que no ofrece.
- Implementación final elegida (8.4): mapa interactivo con cinco acciones y ventanas emergentes, acompañado por imágenes de ranking y dispersión que preservan nombres, tamaño, color y medianas. Las cifras generales y los gráficos permanecen fijos al cambiar la vista del mapa.
- Se añadieron el cierre, los próximos pasos como propuestas, los límites de interpretación, autores y cuatro fuentes con enlaces a las páginas ya conocidas. Se simplificaron las nueve etiquetas de navegación para evitar títulos truncados.
- Las tareas de montaje 8, 10 y 11 están finalizadas con la limitación de vinculación documentada. Comienza la revisión completa de la tarea 12. El ensayo oral del equipo y la elección de acceso público no se dan por realizados.