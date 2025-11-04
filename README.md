# Estadística I - TGAD FCE UBA

Este repositorio contiene el material completo del curso **Estadística I** de la **Tecnicatura en Gestión y Análisis de Datos** de la **Facultad de Ciencias Económicas** de la **Universidad de Buenos Aires** (Cátedra Bianco).

## 🎯 Enfoque Dual de Herramientas

Este curso utiliza un **enfoque dual** que combina:

- **🐍 Python**: Para análisis estadístico programático, visualización de datos y notebooks interactivos
- **🧮 HP Prime**: Para verificación de cálculos, trabajo manual y comprensión conceptual de operaciones matemáticas

Esta metodología permite a los estudiantes desarrollar tanto habilidades de programación como competencias en el uso de herramientas matemáticas especializadas.

## 📚 Contenido del Curso

El curso está organizado en **dos parciales académicos**, cada uno con múltiples unidades temáticas que incluyen notebooks interactivos de Jupyter combinando teoría, ejemplos prácticos y ejercicios:

### 📋 Primer Parcial

- **0. Elementos Iniciales** - Introducción a Python, Google Colab y el repositorio
- **1. Probabilidad** - Conceptos básicos de probabilidad y aplicaciones
- **2. Variables Aleatorias Discretas** - Distribuciones discretas y sus propiedades
- **3. Variables Aleatorias Continuas** - Distribuciones continuas y análisis
- **4. Variables Aleatorias Bidimensionales** - Análisis conjunto de variables
- **5. Estadística Descriptiva** - Medidas de tendencia central y dispersión

### 📋 Segundo Parcial

- **6. Muestreo e Intervalos de Confianza** - Técnicas de muestreo y estimación
- **7. Test de Hipótesis** - Pruebas estadísticas y toma de decisiones
- **8. Regresión Lineal** - Modelos de regresión y predicción
- **9. Números Índice** - Cálculo y análisis de índices

## 🛠️ Requisitos

- **Python 3.7+**
- **Jupyter Notebook** o **Google Colab**
- Librerías: `numpy`, `pandas`, `matplotlib`, `scipy`, `seaborn`
- **HP Prime** (calculadora física o emulador virtual) *[Opcional para verificación]*

## � Recursos Educativos

### Datasets

El proyecto utiliza una **estructura centralizada de datasets** en la carpeta `data/`:

- **`data/shared/`**: Datasets compartidos entre múltiples unidades (Titanic, Financial, Banking, etc.)
- **Otras carpetas**: Créalas según necesites para datasets específicos de temas

📖 **Consulta [data/README.md](data/README.md)** para documentación completa de todos los datasets disponibles.

**Nota importante**: Los datasets grandes (>1MB) no están versionados en Git. Consulta la documentación para opciones de descarga.

### Guías de Referencia

En la carpeta `guides/` encontrarás:

- **`Guia_Conjuntos_Python.ipynb`**: Guía completa de operaciones con conjuntos en Python

### Documentación HP Prime

En la carpeta `hp-prime/` encontrarás:

- **`docs/`**: Guías específicas y documentación técnica
- **`manuales/`**: Manuales oficiales y guías de usuario en PDF

## 🚀 Cómo Usar este Repositorio

### 📂 Navegación por la Nueva Estructura

El repositorio está organizado según la **estructura académica del curso**:

- **`1er-parcial/`**: Contiene las unidades 0-5 (Elementos iniciales hasta Estadística Descriptiva)
- **`2do-parcial/`**: Contiene las unidades 6-9 (Muestreo hasta Números Índice)

Esta organización refleja la división natural del curso y facilita el estudio progresivo por parciales.

### 🛠️ Configuración Inicial

1. **Clonar el repositorio:**

   ```bash
   git clone https://github.com/alexballera/EstadisticaI.git
   cd EstadisticaI
   ```

2. **Crear entorno virtual (recomendado):**

   ```bash
   python -m venv estadistica_env
   source estadistica_env/bin/activate  # Linux/Mac
   # estadistica_env\Scripts\activate    # Windows
   ```

3. **Instalar dependencias:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Ejecutar Jupyter:**

   ```bash
   ./start_jupyter.sh
   ```

   O manualmente:

   ```bash
   source .venv/bin/activate
   jupyter notebook --ip=0.0.0.0 --port=8888
   ```

5. **Acceder desde el navegador:** <http://localhost:8888>

6. **Alternativamente**, puedes abrir los notebooks directamente en **Google Colab**.

## 📁 Estructura del Proyecto

```text
EstadisticaI/
├── 1er-parcial/                   # 📋 Primer Parcial Académico
│   ├── 0_Elementos_iniciales/     # Introducción y fundamentos
│   ├── 1_Probabilidad/            # Conceptos básicos de probabilidad
│   ├── 2_VA_discretas/            # Variables aleatorias discretas
│   ├── 3_VA_continuas/            # Variables aleatorias continuas
│   ├── 4_VA_bidimensionales/      # Análisis conjunto de variables
│   └── 5_Descriptiva/             # Estadística descriptiva
├── 2do-parcial/                   # 📋 Segundo Parcial Académico
│   ├── 6_Muestreo_e_IC/          # Muestreo e intervalos de confianza
│   ├── 7_Test_de_Hipotesis/      # Pruebas de hipótesis
│   ├── 8_Regresion_Lineal/       # Modelos de regresión
│   └── 9_Numeros_Indice/         # Números índice
├── data/                          # 📊 Datasets centralizados
│   ├── shared/                    # Datasets compartidos
│   │   ├── titanic/              # Dataset Titanic
│   │   ├── financial/            # Datos financieros
│   │   ├── banking/              # Datos bancarios
│   │   └── otros/                # Otros datasets
│   ├── README.md                 # Documentación de datasets
│   ├── GUIA_RAPIDA.md           # Guía rápida de uso
│   └── dataset_loader.py        # Helper para carga de datos
├── practicas/                     # Prácticas y ejercicios por tema
│   ├── practica0/
│   ├── practica1-probabilidad/
│   ├── practica2-va-discretas/
│   ├── practica3-va-continuas/
│   ├── practica4-va-bidimensionales/
│   ├── practica5-descriptivas/
│   ├── practica6-muestreo-ic/
│   ├── practica7-test-de-hipotesis/
│   ├── practica8-regresiones/
│   ├── practica9-numeros-indice/
│   └── parciales/                # Examenes parciales
│       ├── primero/
│       └── segundo/
├── guias/                         # Guías de referencia
│   └── Guia_Conjuntos_Python.ipynb
├── hp-prime/                      # Documentación HP Prime
│   ├── docs/                      # Guías específicas
│   └── manuales/                  # Manuales oficiales
├── fuentes/                       # Material de referencia bibliográfica
├── .github/                       # Configuración GitHub
├── AGENTS.md                      # Instrucciones para asistentes IA
├── requirements.txt              # Dependencias Python
├── start_jupyter.sh              # Script de inicio
├── .gitignore
└── README.md
```

## 🎯 Objetivos de Aprendizaje

Al completar este curso, los estudiantes serán capaces de:

- Aplicar conceptos fundamentales de probabilidad y estadística
- Utilizar Python para análisis estadístico y programación
- Manejar la calculadora HP Prime para verificación y cálculos matemáticos
- Interpretar y visualizar datos estadísticos
- Realizar pruebas de hipótesis y análisis de regresión
- Construir y analizar números índice
- Integrar herramientas digitales y analógicas en el análisis estadístico

## � Metodología de Trabajo

### 📚 Progresión Recomendada

1. **Primer Parcial** (`1er-parcial/`):
   - Comienza con `0_Elementos_iniciales/` para familiarizarte con las herramientas
   - Progresa secuencialmente a través de las unidades 1-5
   - Practica con los ejercicios correspondientes en `practicas/`

2. **Segundo Parcial** (`2do-parcial/`):
   - Continúa con las unidades 6-9 una vez dominado el primer parcial
   - Utiliza el conocimiento previo como base para conceptos más avanzados

### 🔧 Enfoque Pedagógico

1. **Estudio Teórico**: Revisión de conceptos en los notebooks
2. **Práctica en Python**: Implementación de algoritmos y análisis
3. **Verificación con HP Prime**: Validación de resultados y comprensión conceptual
4. **Ejercicios Integrados**: Problemas que combinan ambas herramientas

## �👥 Contribuciones

Este material es de uso académico. Para sugerencias o correcciones, por favor abre un issue o envía un pull request.

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo [LICENSE](LICENSE) para más detalles.

## 📧 Contacto

### Cátedra Bianco - TGAD FCE UBA

---

*Material desarrollado para la Tecnicatura en Gestión y Análisis de Datos de la Facultad de Ciencias Económicas de la Universidad de Buenos Aires.*
