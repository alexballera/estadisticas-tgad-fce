# Migración a Estructura Centralizada de Datasets

## 📅 Fecha: Octubre 2024

## 🎯 Objetivo

Reorganizar los datasets del proyecto en una estructura centralizada para:
- Evitar duplicación de archivos
- Facilitar mantenimiento
- Mejorar la gestión en Git
- Documentar mejor cada dataset

## ✅ Cambios Realizados

### 1. Estructura Creada

```
data/
├── README.md                    # Documentación principal
├── dataset_loader.py           # Helper para cargar datasets
├── shared/                     # Datasets compartidos
│   ├── titanic/
│   │   ├── train.csv
│   │   ├── test.csv
│   │   ├── gender_submission.csv
│   │   └── README.md
│   ├── financial/
│   │   ├── 2014-2018_Financial_Data.csv (5 archivos)
│   │   └── README.md
│   ├── banking/
│   │   ├── bank.csv
│   │   ├── bank-full.csv
│   │   └── README.md
│   └── otros/
│       ├── default of credit card clients.xls
│       └── README.md
├── examples/                   # Para datasets pequeños < 1MB
│   └── .gitkeep
└── U0/ ... U9/                # Datasets específicos por unidad
    └── .gitkeep
```

### 2. Datasets Migrados

#### Desde `practicas/practica0/` a `data/shared/`:
- ✅ 2014-2018_Financial_Data.csv → financial/
- ✅ bank.csv, bank-full.csv → banking/
- ✅ default of credit card clients.xls → otros/
- ✅ test.csv, gender_submission.csv → titanic/

#### Desde `0_Elementos_iniciales/` a `data/shared/`:
- ✅ train.csv → titanic/

### 3. Archivos Actualizados

#### Notebooks
- ✅ `0_Elementos_iniciales/TGAD_Obtencion_de_datos_con_Python.ipynb`
  - bank.csv → ../data/shared/banking/bank.csv
  - default of credit card clients.xls → ../data/shared/otros/...
  - train.csv → ../data/shared/titanic/train.csv

#### Documentación
- ✅ `.gitignore` - Actualizado para excluir datos pero incluir READMEs
- ✅ `README.md` - Agregada sección de datasets
- ✅ `data/README.md` - Documentación completa de datasets
- ✅ `data/shared/*/README.md` - 4 READMEs específicos creados
- ✅ `practicas/practica0/README.md` - Referencias a nueva ubicación

#### Código
- ✅ `data/dataset_loader.py` - Helper para facilitar carga de datasets

### 4. Configuración Git

#### .gitignore actualizado:
```gitignore
# Excluir todos los datasets
*.csv
*.xlsx
*.xls

# EXCEPTO: datasets de ejemplo y READMEs
!data/examples/*.csv
!data/examples/*.xlsx
!example_data.csv
!data/**/README.md
!data/README.md
!data/**/.gitkeep
```

## 📊 Impacto

### Archivos Versionados (Solo estructura y docs):
- 16 archivos .gitkeep
- 6 archivos README.md
- 1 archivo dataset_loader.py
- **Total: ~15KB versionados**

### Archivos NO Versionados (Datos):
- 11 archivos de datos (CSV/XLS)
- **Total: ~50MB NO versionados**

## 🔄 Compatibilidad

### Notebooks que DEBEN actualizarse:
- ✅ `0_Elementos_iniciales/TGAD_Obtencion_de_datos_con_Python.ipynb` - **YA ACTUALIZADO**

### Notebooks que NO requieren cambios:
- Notebooks que generan datos sintéticos
- Notebooks que usan APIs externas
- Notebooks sin datasets

## 📝 Para Futuros Colaboradores

### Agregar un nuevo dataset:

1. **Colocar el archivo** en la ubicación apropiada:
   ```bash
   # Si es compartido
   cp mi_dataset.csv data/shared/[categoria]/
   
   # Si es específico de una unidad
   cp mi_dataset.csv data/U5/
   ```

2. **Crear/actualizar README**:
   ```bash
   # Editar data/shared/[categoria]/README.md
   # Actualizar data/README.md
   ```

3. **Usar en notebooks**:
   ```python
   # Opción 1: Usar el loader
   from dataset_loader import get_loader
   loader = get_loader()
   df = loader.load_custom('U5/mi_dataset.csv')
   
   # Opción 2: Ruta directa
   df = pd.read_csv('../data/U5/mi_dataset.csv')
   ```

4. **Commitear** (solo docs, no datos):
   ```bash
   git add data/U5/.gitkeep data/shared/*/README.md
   git commit -m "Add documentation for new dataset"
   ```

## 🔍 Verificación

### Verificar que la migración fue exitosa:

```bash
# 1. Verificar estructura
ls -la data/shared/

# 2. Verificar que datasets NO estén en staging
git status | grep -E "\.csv|\.xlsx|\.xls"
# Debe estar vacío o solo mostrar archivos en examples/

# 3. Verificar que READMEs SÍ estén en staging
git status | grep README.md
# Debe mostrar los READMEs

# 4. Probar carga de datos
python3 data/dataset_loader.py
```

## ⚠️ Notas Importantes

1. **Los archivos originales se COPIARON, no se movieron**: Los datasets originales aún están en `practicas/practica0/` y `0_Elementos_iniciales/`. Puedes eliminarlos después de verificar que todo funciona.

2. **Git no versionará los datasets grandes**: Esto es intencional para mantener el repositorio ligero.

3. **Paths de Google Colab**: Los notebooks que usan Google Colab (/content/, MyDrive/) NO fueron modificados ya que usan una estructura diferente.

## 🎓 Beneficios Obtenidos

✅ Organización clara y escalable
✅ Documentación completa de cada dataset
✅ Facilita colaboración (estructura vs datos)
✅ Reduce tamaño del repositorio
✅ Helper para carga consistente de datos
✅ Enseña buenas prácticas a estudiantes

---

*Migración completada: Octubre 2024*
