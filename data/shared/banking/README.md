# Dataset: Banking Marketing

## 📊 Información General

- **Fuente**: UCI Machine Learning Repository
- **Descripción**: Datos relacionados con campañas de marketing directo de una institución bancaria portuguesa
- **Tipo**: Clasificación binaria
- **Tamaño Total**: ~4.9MB

## 📁 Archivos

### bank.csv (451KB)
Versión reducida del dataset con subset de observaciones.

### bank-full.csv (4.4MB)
Dataset completo con todas las observaciones.

## 📋 Descripción de Variables

**Variables de entrada (atributos del cliente)**:
- `age`: Edad (numérico)
- `job`: Tipo de trabajo (categórico)
- `marital`: Estado civil (categórico)
- `education`: Nivel educativo (categórico)
- `default`: Tiene crédito en default? (binario)
- `balance`: Balance promedio anual (numérico)
- `housing`: Tiene préstamo hipotecario? (binario)
- `loan`: Tiene préstamo personal? (binario)

**Variables relacionadas con el último contacto**:
- `contact`: Tipo de comunicación de contacto (categórico)
- `day`: Último día de contacto del mes (numérico)
- `month`: Último mes de contacto del año (categórico)
- `duration`: Duración del último contacto en segundos (numérico)

**Otras variables**:
- `campaign`: Número de contactos realizados durante esta campaña (numérico)
- `pdays`: Días transcurridos desde el último contacto de campaña anterior (numérico)
- `previous`: Número de contactos antes de esta campaña (numérico)
- `poutcome`: Resultado de la campaña de marketing anterior (categórico)

**Variable objetivo**:
- `y`: ¿El cliente suscribió un depósito a plazo? (binario: "yes", "no")

## 🎯 Uso en el Curso

- **Práctica 0**: Carga de datos con delimitador específico (`;`)
- **Unidad 0**: Exploración y análisis de datos categóricos y numéricos

## 💡 Ejemplo de Uso

```python
import pandas as pd
from pathlib import Path

# Cargar datos (importante: usar sep=';')
DATA_DIR = Path('..') / 'data' / 'shared' / 'banking'
df = pd.read_csv(DATA_DIR / 'bank.csv', sep=';')

# Exploración
print(df.info())
print(df['y'].value_counts())  # Distribución de la variable objetivo

# Versión completa
df_full = pd.read_csv(DATA_DIR / 'bank-full.csv', sep=';')
print(f"Bank reducido: {df.shape}, Bank completo: {df_full.shape}")
```

## 📚 Recursos Adicionales

- [UCI ML Repository - Bank Marketing](https://archive.ics.uci.edu/ml/datasets/Bank+Marketing)
- Paper: S. Moro, P. Cortez and P. Rita. "A Data-Driven Approach to Predict the Success of Bank Telemarketing." Decision Support Systems, Elsevier, 62:22-31, June 2014

## ⚠️ Notas Importantes

- **Separador**: Este dataset usa `;` como separador, no coma
- **Encoding**: Verificar encoding si hay problemas con caracteres especiales
- La variable `duration` no debe usarse para predicción realista (solo se conoce después del contacto)
