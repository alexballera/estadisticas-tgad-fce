# Dataset: Financial Data (2014-2018)

## 📊 Información General

- **Descripción**: Datos financieros de empresas para análisis de series temporales
- **Periodo**: 2014-2018 (5 años)
- **Tamaño Total**: ~39MB

## 📁 Archivos

- `2014_Financial_Data.csv` (6.9MB)
- `2015_Financial_Data.csv` (7.5MB)
- `2016_Financial_Data.csv` (8.1MB)
- `2017_Financial_Data.csv` (8.3MB)
- `2018_Financial_Data.csv` (8.2MB)

## 🎯 Uso en el Curso

- **Práctica 0**: Carga y exploración de datasets de gran tamaño
- **Análisis de series temporales**: Evolución de métricas financieras

## 💡 Ejemplo de Uso

```python
import pandas as pd
from pathlib import Path

# Cargar datos de un año específico
DATA_DIR = Path('..') / 'data' / 'shared' / 'financial'
df_2018 = pd.read_csv(DATA_DIR / '2018_Financial_Data.csv')

# Cargar todos los años y combinar
years = range(2014, 2019)
dfs = []
for year in years:
    df = pd.read_csv(DATA_DIR / f'{year}_Financial_Data.csv')
    df['year'] = year
    dfs.append(df)

df_all = pd.concat(dfs, ignore_index=True)
print(df_all.shape)
```

## 📝 Notas

- Datasets grandes: considerar usar `chunksize` o `usecols` para optimizar memoria
- Revisar tipos de datos antes de cargar para optimizar rendimiento
