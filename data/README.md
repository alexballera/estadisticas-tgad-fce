# Datasets - Estadística I (TGAD FCE-UBA)

Esta carpeta contiene todos los datasets utilizados en el curso, organizados de manera centralizada para facilitar su uso y mantenimiento.

## 📁 Estructura

```
data/
├── shared/              # Datasets compartidos entre unidades
│   ├── titanic/        # Dataset Titanic (Kaggle)
│   ├── financial/      # Datos financieros 2014-2018
│   ├── banking/        # Datos bancarios
│   └── otros/          # Otros datasets compartidos
│
├── README.md           # Documentación principal
├── GUIA_RAPIDA.md      # Guía de inicio rápido
├── MIGRACION.md        # Registro del proceso de migración
└── dataset_loader.py   # Helper para carga fácil de datasets
```

**Nota**: Si necesitas agregar datasets específicos de una unidad, créalos directamente en carpetas dentro de `data/` según necesites (ej: `data/unidad5/`, `data/regresion/`, etc.)

## 🎯 Uso en Notebooks

### Opción 1: Usando el Dataset Loader (Recomendado)

```python
import sys
sys.path.append('../data')  # Ajustar según ubicación del notebook
from dataset_loader import get_loader

# Crear loader
loader = get_loader()

# Cargar datasets fácilmente
df_titanic = loader.load_titanic('train')
df_bank = loader.load_bank()
df_financial = loader.load_financial(2018)
df_credit = loader.load_credit_card()

# Listar todos los datasets disponibles
loader.list_datasets()
```

### Opción 2: Usando rutas relativas directamente

```python
import pandas as pd
from pathlib import Path

# Definir directorio base de datos
DATA_DIR = Path('..') / 'data'  # Desde notebooks en unidades
# DATA_DIR = Path('../..') / 'data'  # Desde notebooks en practicas/

# Cargar dataset compartido
df = pd.read_csv(DATA_DIR / 'shared' / 'titanic' / 'train.csv')

# Si creas datasets específicos, créalos en subcarpetas dentro de data/
# Ejemplo: data/regresion/mi_dataset.csv
df = pd.read_csv(DATA_DIR / 'regresion' / 'mi_dataset.csv')
```

## 📊 Datasets Disponibles

### Shared (Compartidos)

#### 1. Titanic
- **Ubicación**: `data/shared/titanic/`
- **Archivos**: train.csv (60KB), test.csv (28KB), gender_submission.csv (3.2KB)
- **Descripción**: Datos de pasajeros del Titanic
- **Fuente**: Kaggle - Titanic Competition
- **Usado en**: Unidad 0 (Introducción Python/Pandas)

#### 2. Financial Data (2014-2018)
- **Ubicación**: `data/shared/financial/`
- **Archivos**: 2014_Financial_Data.csv (6.9MB), 2015_Financial_Data.csv (7.5MB), 2016_Financial_Data.csv (8.1MB), 2017_Financial_Data.csv (8.3MB), 2018_Financial_Data.csv (8.2MB)
- **Tamaño Total**: ~39MB
- **Descripción**: Datos financieros de empresas
- **Usado en**: Práctica 0

#### 3. Banking Data
- **Ubicación**: `data/shared/banking/`
- **Archivos**: bank.csv (451KB), bank-full.csv (4.4MB)
- **Descripción**: Datos de campañas de marketing bancario
- **Usado en**: Práctica 0, Unidad 0

#### 4. Credit Card Default
- **Ubicación**: `data/shared/otros/`
- **Archivo**: default of credit card clients.xls (5.3MB)
- **Descripción**: Datos de incumplimiento de tarjetas de crédito
- **Usado en**: Práctica 0, Unidad 0

## ⚙️ Gestión de Datasets

### Para Estudiantes

Los datasets grandes (> 1MB) **no están versionados en Git** para mantener el repositorio ligero.

**Opción 1**: Usar los datasets ya disponibles en tu copia local (si hiciste fork o clone después de la reorganización)

**Opción 2**: Descargar desde las fuentes originales:
- Titanic: https://www.kaggle.com/c/titanic/data
- Banking: UCI ML Repository

**Opción 3**: Solicitar datasets al equipo docente

### Para Mantener el Repositorio

Los datasets están excluidos en `.gitignore`, pero la estructura de carpetas y READMEs sí están versionados.

## 📝 Agregar Nuevos Datasets

1. **Colocar el archivo** en la carpeta apropiada:
   - Si se usa en múltiples unidades → `data/shared/[categoria]/`
   - Si es específico de un tema → Crear carpeta en `data/[tema]/` (ej: `data/regresion/`)
   - Si es pequeño (<1MB) y de ejemplo → `data/shared/ejemplos/`

2. **Documentar** en el README de la carpeta correspondiente

3. **Actualizar** este README principal

4. **Verificar** que el `.gitignore` excluya archivos grandes

## 🔗 Enlaces Útiles

- [Kaggle Datasets](https://www.kaggle.com/datasets)
- [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/index.php)
- [Google Dataset Search](https://datasetsearch.research.google.com/)

---

*Última actualización: Octubre 2024*
