# Dataset: Titanic

## 📊 Información General

- **Fuente**: Kaggle - Titanic: Machine Learning from Disaster
- **URL**: https://www.kaggle.com/c/titanic/data
- **Licencia**: Dominio Público
- **Tamaño Total**: ~91KB

## 📁 Archivos

### train.csv (60KB)
Dataset de entrenamiento con información de 891 pasajeros.

**Columnas principales**:
- `PassengerId`: ID único del pasajero
- `Survived`: 0 = No sobrevivió, 1 = Sobrevivió (variable objetivo)
- `Pclass`: Clase del ticket (1, 2, 3)
- `Name`: Nombre del pasajero
- `Sex`: Género (male/female)
- `Age`: Edad en años
- `SibSp`: Número de hermanos/cónyuges a bordo
- `Parch`: Número de padres/hijos a bordo
- `Ticket`: Número de ticket
- `Fare`: Tarifa pagada
- `Cabin`: Número de cabina
- `Embarked`: Puerto de embarque (C=Cherbourg, Q=Queenstown, S=Southampton)

### test.csv (28KB)
Dataset de prueba con 418 pasajeros (sin la columna Survived).

### gender_submission.csv (3.2KB)
Archivo de ejemplo para submissions en formato Kaggle.

## 🎯 Uso en el Curso

- **Unidad 0 - Elementos Iniciales**: Introducción a Python, Pandas y manipulación de datos
- **Práctica 0**: Ejercicios básicos de carga y exploración de datos

## 💡 Ejemplo de Uso

```python
import pandas as pd
from pathlib import Path

# Cargar datos
DATA_DIR = Path('..') / 'data' / 'shared' / 'titanic'
df_train = pd.read_csv(DATA_DIR / 'train.csv')
df_test = pd.read_csv(DATA_DIR / 'test.csv')

# Exploración básica
print(df_train.info())
print(df_train.describe())
print(df_train.head())
```

## 📚 Recursos Adicionales

- [Titanic Data Dictionary](https://www.kaggle.com/c/titanic/data)
- [Tutorial de Kaggle](https://www.kaggle.com/c/titanic/overview)
