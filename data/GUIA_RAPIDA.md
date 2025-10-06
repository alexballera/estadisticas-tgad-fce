# 🚀 Guía Rápida: Uso de Datasets

## Para Estudiantes

### Opción 1: Usar el Dataset Loader (Más Fácil) ⭐

```python
# En cualquier notebook
import sys
sys.path.append('../data')  # Ajustar según ubicación
from dataset_loader import get_loader

loader = get_loader()

# Cargar datasets predefinidos
df_titanic = loader.load_titanic('train')
df_bank = loader.load_bank()
df_financial = loader.load_financial(2018)
df_credit = loader.load_credit_card()

# Ver todos los datasets disponibles
loader.list_datasets()
```

### Opción 2: Rutas Directas

```python
import pandas as pd

# Desde notebooks en unidades (0_Elementos_iniciales/, 1_Probabilidad/, etc.)
df = pd.read_csv('../data/shared/titanic/train.csv')

# Desde notebooks en practicas/ 
df = pd.read_csv('../../data/shared/titanic/train.csv')
```

### Opción 3: Usar Path (Más Robusto)

```python
from pathlib import Path
import pandas as pd

DATA_DIR = Path('..') / 'data'
df = pd.read_csv(DATA_DIR / 'shared' / 'titanic' / 'train.csv')
```

## Datasets Disponibles

| Dataset | Ubicación | Tamaño | Uso |
|---------|-----------|--------|-----|
| **Titanic** | `data/shared/titanic/` | 91KB | Intro Python/Pandas |
| **Banking** | `data/shared/banking/` | 4.9MB | Marketing bancario |
| **Financial** | `data/shared/financial/` | 39MB | Series temporales |
| **Credit Card** | `data/shared/otros/` | 5.3MB | Default predicción |

## ⚠️ Notas Importantes

1. **Datasets grandes NO están en Git**: Si clonaste recientemente, puede que no tengas los archivos de datos. Ver opciones en `data/README.md`

2. **Delimitadores especiales**:
   - Banking: usa `sep=';'` 
   - Credit Card: usa `header=1`

3. **Google Colab**: Si usas Colab, sube los datasets manualmente o usa las rutas específicas de Colab

## 📚 Documentación Completa

- **data/README.md**: Guía completa de datasets
- **data/shared/[dataset]/README.md**: Info específica de cada dataset
- **data/MIGRACION.md**: Cómo se organizaron los datos

## 🆘 Ayuda

¿No encuentras un dataset?
1. Revisa `data/shared/` - deberían estar ahí
2. Consulta `data/README.md` para opciones de descarga
3. Contacta al equipo docente
