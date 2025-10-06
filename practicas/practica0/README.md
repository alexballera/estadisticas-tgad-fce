# Práctica 0 - Elementos Iniciales

## 📁 Datasets Utilizados

Esta práctica utiliza datasets compartidos ubicados en la carpeta centralizada `data/shared/`.

### Datasets Disponibles

#### 1. Titanic
- **Ubicación**: `../../data/shared/titanic/`
- **Archivos**: train.csv, test.csv, gender_submission.csv
- **Uso**: Introducción a Pandas y exploración de datos

#### 2. Banking Data
- **Ubicación**: `../../data/shared/banking/`
- **Archivos**: bank.csv, bank-full.csv
- **Uso**: Manejo de delimitadores personalizados (`;`)

#### 3. Financial Data
- **Ubicación**: `../../data/shared/financial/`
- **Archivos**: 2014-2018_Financial_Data.csv (5 archivos)
- **Uso**: Carga de datasets grandes

#### 4. Credit Card Default
- **Ubicación**: `../../data/shared/otros/`
- **Archivo**: default of credit card clients.xls
- **Uso**: Carga de archivos Excel

## 💡 Cómo Usar los Datasets

```python
import pandas as pd
from pathlib import Path

# Definir directorio base
DATA_DIR = Path('../../data')

# Cargar datasets
df_titanic = pd.read_csv(DATA_DIR / 'shared' / 'titanic' / 'train.csv')
df_bank = pd.read_csv(DATA_DIR / 'shared' / 'banking' / 'bank.csv', sep=';')
df_credit = pd.read_excel(DATA_DIR / 'shared' / 'otros' / 'default of credit card clients.xls', header=1)
```

## 📚 Documentación

Para más información sobre cada dataset, consulta los README en cada carpeta:
- [Titanic README](../../data/shared/titanic/README.md)
- [Banking README](../../data/shared/banking/README.md)
- [Financial README](../../data/shared/financial/README.md)
- [Credit Card README](../../data/shared/otros/README.md)

## ⚠️ Nota sobre Datasets Locales

Los datasets grandes **no están versionados en Git**. Si no tienes los archivos localmente:

1. **Opción 1**: Descargar desde las fuentes originales (ver READMEs)
2. **Opción 2**: Solicitar al equipo docente
3. **Opción 3**: Usar Google Colab (los archivos pueden cargarse allí)

---

Los archivos que anteriormente estaban en esta carpeta ahora están organizados en `data/shared/` para evitar duplicación y facilitar su uso en todo el curso.
