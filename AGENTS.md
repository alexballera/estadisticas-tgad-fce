# Instrucciones para Agentes de IA - Estadística I (TGAD FCE-UBA)

## Instrucción Principal
**SIEMPRE responde en español latinoamericano.** Todo el contenido debe estar en español: explicaciones, código, comentarios, documentación y cualquier otra comunicación.

## Contexto del Proyecto

Este repositorio contiene Jupyter Notebooks y materiales de apoyo para la materia Estadística I (Cátedra Bianco, TGAD, FCE UBA). Está organizado por temas, con cada carpeta representando una unidad del curso y conteniendo uno o más notebooks con teoría, ejemplos y ejercicios.

## Estructura y convenciones

- **Carpetas**: Cada carpeta numerada (por ejemplo, `1 Probabilidad/`, `2 VA discretas/`) corresponde a una unidad temática. La carpeta `0 Elementos iniciales/` contiene materiales introductorios.
- **Notebooks**: Todo el contenido está en archivos `.ipynb`. Cada notebook es auto-contenido para su tema, con código, explicaciones y ejercicios.
- **Sin scripts de build o tests**: Es un proyecto educativo basado en notebooks. No existen scripts automatizados de construcción ni pruebas.
- **Sin dependencias externas asumidas**: Los notebooks están pensados para ejecutarse en entornos estándar de Jupyter/Colab. Si se requiere un paquete, debe incluirse el comando de instalación en una celda (por ejemplo, `!pip install numpy`).
- **Idioma**: La mayoría del contenido y los comentarios están en español.

## Patrones clave

- **Aprendizaje interactivo**: Los notebooks combinan código, markdown y ejercicios. Las explicaciones preceden a las celdas de código. Las salidas se muestran en línea.
- **Nomenclatura**: Los notebooks comienzan con el prefijo `TGAD_` y describen su contenido (por ejemplo, `TGAD_Estadística_Clase_U1_con_Python.ipynb`).
- **Sin importaciones entre notebooks**: Cada notebook es independiente; no asumas módulos o scripts compartidos.
- **PDFs**: Algunas carpetas incluyen PDFs con teoría o instrucciones.

## Herramientas de cálculo

Este proyecto utiliza **dos herramientas principales** para cálculos y verificación:

### **Python**

- **Uso principal**: Notebooks interactivos con código, ejemplos y ejercicios
- **Librerías típicas**: NumPy, SciPy, Matplotlib, pandas para análisis estadístico
- **Teoría de conjuntos**: Se usa la estructura nativa `set` de Python para operaciones con conjuntos
- **Ubicación**: Todo el código ejecutable está en los archivos `.ipynb`

### **HP Prime**

- **Uso complementario**: Verificación de cálculos de probabilidades, estadísticas y teoría de conjuntos
- **Entorno**: Calculadora gráfica HP Prime (física o emulador) en modo CAS
- **Operaciones**: Cálculos exactos, verificación de resultados, trabajo con conjuntos
- **Documentación**: Carpeta `hp-prime/` contiene manuales y guías específicas
- **Guías disponibles**: `guides/` incluye guías rápidas para conjuntos en HP Prime

Al desarrollar contenido, considera ambas herramientas y proporciona ejemplos o verificaciones cuando sea relevante.

## Guía para agentes de IA

- Al agregar contenido nuevo, respeta la estructura y nomenclatura existente.
- Prefiere el español para nuevas explicaciones, comentarios y nombres de variables.
- Si agregas código a un notebook, asegúrate de que sea autoexplicativo e incluye contexto en markdown.
- **Considera ambas herramientas**: Al desarrollar ejercicios o ejemplos, proporciona soluciones tanto en Python como referencias para HP Prime cuando sea apropiado.
- **Teoría de conjuntos**: Utiliza las guías específicas disponibles en `guides/` para operaciones con conjuntos.
- No agregues scripts de build, CI/CD o automatización de tests salvo que se solicite explícitamente.
- Usa los notebooks existentes como referencia de estilo y estructura.

## Archivos y carpetas clave

- `0 Elementos iniciales/`: Materiales y guías introductorias.
- `1 Probabilidad/` a `9 Numeros Indice/`: Unidades temáticas con notebooks.
- `hp-prime/`: Documentación, manuales y guías para calculadora HP Prime.
- `guides/`: Guías rápidas de referencia (Python sets, HP Prime conjuntos, etc.).
- `README.md`: Descripción breve del proyecto y contexto.

---
Para más detalles, revisa los notebooks de cada unidad. Ante la duda, iguala el estilo y estructura de los materiales existentes.
