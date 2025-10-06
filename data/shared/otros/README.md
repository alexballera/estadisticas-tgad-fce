# Dataset: Default of Credit Card Clients

## 📊 Información General

- **Fuente**: UCI Machine Learning Repository
- **Descripción**: Dataset sobre pagos por default de clientes de tarjetas de crédito en Taiwan
- **Tipo**: Clasificación binaria
- **Formato**: Microsoft Excel (.xls)
- **Tamaño**: 5.3MB

## 📁 Archivo

- `default of credit card clients.xls`

## 📋 Descripción de Variables

Este dataset contiene información sobre pagos por default, características demográficas, datos de crédito, historial de pagos y extractos de facturación de clientes de tarjetas de crédito en Taiwan desde abril de 2005 a septiembre de 2005.

**Variables principales**:
- `ID`: Identificador del cliente
- `LIMIT_BAL`: Monto del crédito otorgado
- `SEX`: Género (1 = male, 2 = female)
- `EDUCATION`: Nivel educativo (1 = graduate school, 2 = university, 3 = high school, 4 = others)
- `MARRIAGE`: Estado civil (1 = married, 2 = single, 3 = others)
- `AGE`: Edad en años
- `PAY_0` a `PAY_6`: Historial de pagos pasados (de abril a septiembre 2005)
- `BILL_AMT1` a `BILL_AMT6`: Monto del extracto de facturación
- `PAY_AMT1` a `PAY_AMT6`: Monto del pago anterior
- `default payment next month`: Variable objetivo (1 = yes, 0 = no)

## 🎯 Uso en el Curso

- **Práctica 0**: Carga de archivos Excel con Pandas
- **Unidad 0**: Manejo de archivos con encabezados múltiples

## 💡 Ejemplo de Uso

```python
import pandas as pd
from pathlib import Path

# Cargar datos (importante: usar header=1 para saltar primera fila)
DATA_DIR = Path('..') / 'data' / 'shared' / 'otros'
df = pd.read_excel(DATA_DIR / 'default of credit card clients.xls', header=1)

# Exploración
print(df.info())
print(df.columns)
print(df['default payment next month'].value_counts())

# Análisis básico
print(f"Total clientes: {len(df)}")
print(f"Tasa de default: {df['default payment next month'].mean():.2%}")
```

## ⚠️ Notas Importantes

- **Encabezado**: El archivo tiene información en la primera fila, usar `header=1` al cargar
- **Formato**: Archivo .xls (Excel antiguo), requiere `pd.read_excel()`
- **Librería necesaria**: `openpyxl` o `xlrd` debe estar instalada

```python
# Si hay error al leer el archivo:
# pip install openpyxl xlrd
```

## 📚 Recursos Adicionales

- [UCI ML Repository - Default of Credit Card Clients](https://archive.ics.uci.edu/ml/datasets/default+of+credit+card+clients)
- Paper: Yeh, I. C., & Lien, C. H. (2009). "The comparisons of data mining techniques for the predictive accuracy of probability of default of credit card clients." Expert Systems with Applications, 36(2), 2473-2480.
