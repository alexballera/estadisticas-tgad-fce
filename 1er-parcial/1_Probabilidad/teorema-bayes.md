# Guía: Teorema de Bayes

## Introducción

El **Teorema de Bayes** es una herramienta fundamental en probabilidad que nos permite "invertir" probabilidades condicionales. Es especialmente útil cuando conocemos la probabilidad de un efecto dada una causa, pero necesitamos la probabilidad de la causa dado el efecto.

## Definición Fundamental

### ¿Qué es el Teorema de Bayes?

El **Teorema de Bayes** nos permite calcular P(A|B) cuando conocemos P(B|A), P(A) y P(B).

### Fórmula del Teorema de Bayes

**P(A|B) = [P(B|A) × P(A)] / P(B)**

### Componentes de la Fórmula:

- **P(A|B)**: Probabilidad **a posteriori** (lo que queremos encontrar)
- **P(B|A)**: Probabilidad de la evidencia dado el evento (verosimilitud)
- **P(A)**: Probabilidad **a priori** del evento
- **P(B)**: Probabilidad total de la evidencia (denominador normalizador)

### Fórmula Extendida con Probabilidad Total:

**P(A|B) = [P(B|A) × P(A)] / [Σ P(B|Aᵢ) × P(Aᵢ)]**

## Identificación Semántica: Cuándo Usar Bayes

### ✅ Palabras clave que indican uso de Bayes:

- **"Si [resultado], ¿cuál es la probabilidad de que [causa]?"**
  - Ejemplo: "Si el televisor es defectuoso, ¿cuál es la probabilidad de que sea marca 1?"

- **"Dado que [efecto ocurrió], ¿probabilidad de [causa específica]?"**
  - Ejemplo: "Dado que la prueba es positiva, ¿probabilidad de tener la enfermedad?"

- **"¿De dónde proviene más probablemente [el resultado]?"**
  - Ejemplo: "¿De qué máquina proviene más probablemente el producto defectuoso?"

- **"¿Cuál es la causa más probable de [el efecto]?"**
  - Ejemplo: "¿Cuál es la marca más probable del televisor defectuoso?"

### ❌ NO es Bayes cuando:

- **Preguntan por P(B|A) directamente** (ya lo conoces)
- **Preguntan por probabilidad total** (usa fórmula de probabilidad total)
- **No hay "inversión" de la condicional**

## Ejemplo 1: Televisores Defectuosos

### Enunciado:
*"Una empresa vende televisores de 3 marcas: 50% marca 1, 30% marca 2, 20% marca 3. Se sabe que el 25% de los televisores de marca 1 necesita reparación, el 20% de marca 2 y el 10% de marca 3. Si un cliente vuelve con un televisor defectuoso, ¿cuál es la probabilidad de que sea de marca 1?"*

### Análisis Semántico:
- **"Si un cliente vuelve con un televisor defectuoso"** → Tenemos la evidencia (efecto)
- **"¿cuál es la probabilidad de que sea de marca 1?"** → Buscamos la causa
- **Estructura**: "Si [efecto], ¿probabilidad de [causa]?" → **BAYES**

### Datos del Problema:
- P(A₁) = 0.50, P(A₂) = 0.30, P(A₃) = 0.20 (probabilidades a priori)
- P(D|A₁) = 0.25, P(D|A₂) = 0.20, P(D|A₃) = 0.10 (verosimilitudes)

### Solución Paso a Paso:

**Paso 1: Calcular P(D) - Probabilidad total**
P(D) = P(D|A₁)×P(A₁) + P(D|A₂)×P(A₂) + P(D|A₃)×P(A₃)
P(D) = 0.25×0.50 + 0.20×0.30 + 0.10×0.20 = 0.125 + 0.06 + 0.02 = 0.205

**Paso 2: Aplicar Bayes**
P(A₁|D) = [P(D|A₁) × P(A₁)] / P(D) = [0.25 × 0.50] / 0.205 = 0.125 / 0.205 ≈ 0.610

### Visualización con 10,000 Televisores:

**📊 Distribución por Marca:**
- **Marca 1**: 10,000 × 0.50 = **5,000 televisores**
- **Marca 2**: 10,000 × 0.30 = **3,000 televisores**
- **Marca 3**: 10,000 × 0.20 = **2,000 televisores**

**🔧 Televisores Defectuosos:**
- **Marca 1 defectuosos**: 5,000 × 0.25 = **1,250 televisores**
- **Marca 2 defectuosos**: 3,000 × 0.20 = **600 televisores**
- **Marca 3 defectuosos**: 2,000 × 0.10 = **200 televisores**
- **Total defectuosos**: 1,250 + 600 + 200 = **2,050 televisores**

### 📊 Matriz de Confusión para Marca 1:

| | **Defectuoso** | **No Defectuoso** | **Total** |
|---|---|---|---|
| **Marca 1** | **VP = 1,250** <br> *Verdaderos Positivos* | **VN = 3,750** <br> *Verdaderos Negativos* | **5,000** |
| **Otras Marcas** | **FP = 800** <br> *Falsos Positivos* | **FN = 4,200** <br> *Falsos Negativos* | **5,000** |
| **Total** | **2,050** | **7,950** | **10,000** |

### 🎯 Métricas para Marca 1:

| **Métrica** | **Fórmula** | **Cálculo** | **Resultado** | **Interpretación** |
|-------------|-------------|-------------|---------------|-------------------|
| **🎯 Valor Predictivo Positivo** <br> ***(ESTO ES BAYES)*** | **VP/(VP+FP)** | **1,250/(1,250+800)** | **61%** | **Si es defectuoso, ¿qué % es marca 1?** |
| **Sensibilidad** <br> *(de Marca 1)* | VP/(VP+VN) | 1,250/(1,250+3,750) | **25%** | De marca 1, ¿qué % es defectuoso? |
| **Especificidad** <br> *(para Marca 1)* | FN/(FN+FP) | 4,200/(4,200+800) | **84%** | De otras marcas, ¿qué % no es defectuoso? |

**Interpretación**: Si un televisor es defectuoso, hay **61%** de probabilidad de que sea marca 1.

**🔍 Observación clave**: Aunque marca 1 tiene solo 25% de defectuosos, al ser la marca más vendida (50%), contribuye con más defectuosos totales (1,250 de 2,050 = 61%).

## Ejemplo 2: Pruebas Médicas (Explicación Detallada)

### Enunciado:
*"Una prueba médica detecta correctamente una enfermedad en el 95% de los casos (sensibilidad). La probabilidad de falso positivo es 2% (especificidad = 98%). Si la enfermedad afecta al 1% de la población, ¿cuál es la probabilidad de tener la enfermedad si la prueba da positivo?"*

### Análisis Semántico:
- **"si la prueba da positivo"** → Tenemos la evidencia
- **"¿probabilidad de tener la enfermedad?"** → Buscamos la causa
- **Estructura clásica de diagnóstico** → **BAYES**

### Definición de Eventos:
- **E**: Tener la enfermedad
- **E^C**: NO tener la enfermedad (estar sano)
- **T+**: Prueba da resultado positivo
- **T-**: Prueba da resultado negativo

### Interpretación de los Datos:
- **P(E) = 0.01** → **Prevalencia**: Solo 1 de cada 100 personas tiene la enfermedad
- **P(E^C) = 0.99** → **99 de cada 100 personas están sanas**
- **P(T+|E) = 0.95** → **Sensibilidad**: Si tienes la enfermedad, la prueba la detecta en 95% de los casos
- **P(T+|E^C) = 0.02** → **Falso positivo**: Si estás sano, la prueba incorrectamente dice que estás enfermo en 2% de los casos

### Visualización con 10,000 Personas:

Imaginemos una población de **10,000 personas**:

**📊 Distribución de la Enfermedad:**
- **Enfermos**: 10,000 × 0.01 = **100 personas**
- **Sanos**: 10,000 × 0.99 = **9,900 personas**

**🔬 Resultados de las Pruebas:**

**De las 100 personas ENFERMAS:**
- **Positivos correctos**: 100 × 0.95 = **95 personas** (verdaderos positivos)
- **Negativos incorrectos**: 100 × 0.05 = **5 personas** (falsos negativos)

**De las 9,900 personas SANAS:**
- **Positivos incorrectos**: 9,900 × 0.02 = **198 personas** (falsos positivos)
- **Negativos correctos**: 9,900 × 0.98 = **9,702 personas** (verdaderos negativos)

### Tabla de Resultados:

| Estado Real | Prueba + | Prueba - | Total |
|-------------|----------|----------|-------|
| **Enfermo** | 95       | 5        | 100   |
| **Sano**    | 198      | 9,702    | 9,900 |
| **Total**   | **293**  | 9,707    | 10,000|

### 📊 Cuadro de Métricas Diagnósticas

#### **Matriz de Confusión y Terminología:**

| | **Prueba Positiva** | **Prueba Negativa** |
|---|---|---|
| **Realmente Enfermo** | **VP = 95** <br> *Verdaderos Positivos* | **FN = 5** <br> *Falsos Negativos* |
| **Realmente Sano** | **FP = 198** <br> *Falsos Positivos* | **VN = 9,702** <br> *Verdaderos Negativos* |

#### **Métricas Estadísticas Importantes:**

| **Métrica** | **Fórmula** | **Cálculo** | **Resultado** | **Interpretación** |
|-------------|-------------|-------------|---------------|-------------------|
| **Sensibilidad** <br> *(Recall, TPR)* | VP/(VP+FN) | 95/(95+5) | **95%** | De los enfermos, ¿qué % detecta? |
| **Especificidad** <br> *(TNR)* | VN/(VN+FP) | 9,702/(9,702+198) | **98%** | De los sanos, ¿qué % identifica correctamente? |
| **Valor Predictivo Positivo** <br> *(Precisión, PPV)* | VP/(VP+FP) | 95/(95+198) | **32.4%** | Si la prueba es +, ¿qué % está realmente enfermo? |
| **Valor Predictivo Negativo** <br> *(NPV)* | VN/(VN+FN) | 9,702/(9,702+5) | **99.9%** | Si la prueba es -, ¿qué % está realmente sano? |
| **Exactitud** <br> *(Accuracy)* | (VP+VN)/Total | (95+9,702)/10,000 | **97.97%** | ¿Qué % de diagnósticos son correctos? |
| **Prevalencia** | (VP+FN)/Total | (95+5)/10,000 | **1%** | ¿Qué % de la población tiene la enfermedad? |

#### **Interpretación de cada métrica:**

**🎯 Sensibilidad (95%)**: *"Si tienes la enfermedad, la prueba la detectará en 95% de los casos"*
- **Alta sensibilidad** = Pocos falsos negativos
- **Importante cuando**: No queremos perder casos reales

**🎯 Especificidad (98%)**: *"Si estás sano, la prueba lo confirmará en 98% de los casos"*
- **Alta especificidad** = Pocos falsos positivos  
- **Importante cuando**: No queremos alarmar a personas sanas

**🎯 Valor Predictivo Positivo (32.4%)**: *"Si tu prueba es positiva, solo hay 32.4% de chance de que realmente tengas la enfermedad"*
- **ESTA ES LA RESPUESTA DE BAYES**
- Depende mucho de la prevalencia de la enfermedad

**🎯 Valor Predictivo Negativo (99.9%)**: *"Si tu prueba es negativa, hay 99.9% de chance de que realmente estés sano"*
- Muy alto porque la enfermedad es muy rara

**🎯 Exactitud/Accuracy (97.97%)**: *"La prueba da el diagnóstico correcto en casi 98% de los casos"*
- Puede ser engañosa en enfermedades raras
- Alta porque hay muchos verdaderos negativos

#### **🔍 Observaciones Clave:**

1. **Paradoja de la Prevalencia**: Cuando una enfermedad es muy rara, incluso pruebas excelentes tienen bajo valor predictivo positivo

2. **Trade-off Sensibilidad vs Especificidad**: Generalmente, mejorar una empeora la otra

3. **Dependencia de la Prevalencia**: Los valores predictivos cambian según qué tan común sea la enfermedad en la población

4. **Accuracy puede engañar**: En enfermedades muy raras, la accuracy puede ser alta simplemente porque la mayoría está sana

### Solución Paso a Paso:

**Paso 1: Calcular P(T+) - Total de pruebas positivas**
P(T+) = P(T+|E)×P(E) + P(T+|E^C)×P(E^C)
P(T+) = 0.95×0.01 + 0.02×0.99 = 0.0095 + 0.0198 = 0.0293

**En números concretos**: 95 + 198 = **293 personas** tienen prueba positiva

**Paso 2: Aplicar Bayes**
P(E|T+) = [P(T+|E) × P(E)] / P(T+) = [0.95 × 0.01] / 0.0293 ≈ 0.324

**En números concretos**: De las 293 personas con prueba positiva, solo 95 están realmente enfermas
**Probabilidad**: 95/293 = 0.324 = **32.4%**

### ¿Por qué este resultado es tan contraintuitivo?

**🎯 La clave está en los números absolutos:**

- **Verdaderos positivos**: 95 personas
- **Falsos positivos**: 198 personas
- **Total positivos**: 293 personas

**¡Los falsos positivos (198) son el DOBLE que los verdaderos positivos (95)!**

### ¿Por qué hay tantos falsos positivos?

1. **La enfermedad es MUY RARA** (solo 1%)
2. **Hay MUCHAS personas sanas** (99% = 9,900 personas)
3. **Incluso un pequeño % de error** (2%) en 9,900 personas = 198 falsos positivos
4. **Los falsos positivos superan a los verdaderos positivos**

### Interpretación Final:

**Si tu prueba sale positiva**, la probabilidad de que realmente tengas la enfermedad es solo **32.4%**.

**¿Esto significa que la prueba es mala?** ¡NO! La prueba es excelente:
- Detecta 95% de los casos reales
- Solo se equivoca 2% de las veces con personas sanas

**El problema es la BAJA PREVALENCIA** de la enfermedad.

### Lección Importante:

Este ejemplo muestra por qué los médicos a menudo piden **pruebas confirmatorias** cuando una primera prueba sale positiva, especialmente para enfermedades raras.

## Ejemplo 3: Control de Calidad

### Enunciado:
*"Una fábrica tiene 3 máquinas: A produce 50% con 2% defectuosos, B produce 30% con 3% defectuosos, C produce 20% con 1% defectuosos. Si se encuentra un producto defectuoso, ¿cuál es la probabilidad de que venga de la máquina B?"*

### Análisis Semántico:
- **"Si se encuentra un producto defectuoso"** → Evidencia
- **"¿probabilidad de que venga de máquina B?"** → Causa específica
- **Patrón de diagnóstico industrial** → **BAYES**

### Solución:

**Datos:**
- P(A) = 0.50, P(B) = 0.30, P(C) = 0.20
- P(D|A) = 0.02, P(D|B) = 0.03, P(D|C) = 0.01

**Cálculo:**
P(D) = 0.02×0.50 + 0.03×0.30 + 0.01×0.20 = 0.01 + 0.009 + 0.002 = 0.021

P(B|D) = [P(D|B) × P(B)] / P(D) = [0.03 × 0.30] / 0.021 = 0.009 / 0.021 ≈ 0.429

### Visualización con 10,000 Productos:

**📊 Distribución por Máquina:**
- **Máquina A**: 10,000 × 0.50 = **5,000 productos**
- **Máquina B**: 10,000 × 0.30 = **3,000 productos**
- **Máquina C**: 10,000 × 0.20 = **2,000 productos**

**⚠️ Productos Defectuosos:**
- **Máquina A defectuosos**: 5,000 × 0.02 = **100 productos**
- **Máquina B defectuosos**: 3,000 × 0.03 = **90 productos**
- **Máquina C defectuosos**: 2,000 × 0.01 = **20 productos**
- **Total defectuosos**: 100 + 90 + 20 = **210 productos**

### 📊 Matriz de Confusión para Máquina B:

| | **Defectuoso** | **No Defectuoso** | **Total** |
|---|---|---|---|
| **Máquina B** | **VP = 90** <br> *Verdaderos Positivos* | **VN = 2,910** <br> *Verdaderos Negativos* | **3,000** |
| **Otras Máquinas** | **FP = 120** <br> *Falsos Positivos* | **FN = 6,880** <br> *Falsos Negativos* | **7,000** |
| **Total** | **210** | **9,790** | **10,000** |

### 🎯 Métricas para Máquina B:

| **Métrica** | **Fórmula** | **Cálculo** | **Resultado** | **Interpretación** |
|-------------|-------------|-------------|---------------|-------------------|
| **🎯 Valor Predictivo Positivo** <br> ***(ESTO ES BAYES)*** | **VP/(VP+FP)** | **90/(90+120)** | **42.9%** | **Si es defectuoso, ¿qué % viene de máquina B?** |
| **Sensibilidad** <br> *(de Máquina B)* | VP/(VP+VN) | 90/(90+2,910) | **3%** | De máquina B, ¿qué % es defectuoso? |
| **Especificidad** <br> *(para Máquina B)* | FN/(FN+FP) | 6,880/(6,880+120) | **98.3%** | De otras máquinas, ¿qué % no es defectuoso? |

**Respuesta**: **42.9%** de probabilidad de que venga de la máquina B.

**🔍 Observación clave**: Aunque máquina B tiene la mayor tasa de defectos (3%), no produce la mayoría de defectuosos porque produce menos volumen que máquina A.

## Ejemplo 4: Análisis de Email Spam

### Enunciado:
*"Un filtro de spam clasifica emails: 2% de emails son spam, 98% legítimos. El filtro detecta correctamente 90% del spam y marca incorrectamente como spam el 1% de emails legítimos. Si un email es marcado como spam, ¿cuál es la probabilidad de que realmente sea spam?"*

### Análisis Semántico:
- **"Si un email es marcado como spam"** → Evidencia del clasificador
- **"¿probabilidad de que realmente sea spam?"** → Causa real
- **Problema de clasificación** → **BAYES**

### Solución:

**Eventos:**
- S: Email es spam
- M: Email marcado como spam

**Datos:**
- P(S) = 0.02, P(S^C) = 0.98
- P(M|S) = 0.90, P(M|S^C) = 0.01

**Cálculo:**
P(M) = 0.90×0.02 + 0.01×0.98 = 0.018 + 0.0098 = 0.0278

P(S|M) = [0.90 × 0.02] / 0.0278 = 0.018 / 0.0278 ≈ 0.647

### Visualización con 10,000 Emails:

**📧 Distribución Real:**
- **Spam real**: 10,000 × 0.02 = **200 emails**
- **Legítimos reales**: 10,000 × 0.98 = **9,800 emails**

**🔍 Lo que hace el Filtro:**

**De los 200 emails QUE SON SPAM:**
- **Marcados como spam**: 200 × 0.90 = **180 emails** (verdaderos positivos)
- **Marcados como legítimos**: 200 × 0.10 = **20 emails** (falsos negativos)

**De los 9,800 emails QUE SON LEGÍTIMOS:**
- **Marcados como legítimos**: 9,800 × 0.99 = **9,702 emails** (verdaderos negativos)
- **Marcados como spam**: 9,800 × 0.01 = **98 emails** (falsos positivos)

### 📊 Matriz de Confusión para el Filtro de Spam:

| | **Marcado como SPAM** | **Marcado como LEGÍTIMO** | **Total** |
|---|---|---|---|
| **Realmente SPAM** | **VP = 180** <br> *Verdaderos Positivos* | **FN = 20** <br> *Falsos Negativos* | **200** |
| **Realmente LEGÍTIMO** | **FP = 98** <br> *Falsos Positivos* | **VN = 9,702** <br> *Verdaderos Negativos* | **9,800** |
| **Total** | **278** | **9,722** | **10,000** |

### 🎯 Métricas del Filtro de Spam:

| **Métrica** | **Fórmula** | **Cálculo** | **Resultado** | **Interpretación** |
|-------------|-------------|-------------|---------------|-------------------|
| **Sensibilidad** <br> *(Recall, TPR)* | VP/(VP+FN) | 180/(180+20) | **90%** | De los spam reales, ¿qué % detecta? |
| **Especificidad** <br> *(TNR)* | VN/(VN+FP) | 9,702/(9,702+98) | **99%** | De los legítimos, ¿qué % identifica correctamente? |
| **🎯 Valor Predictivo Positivo** <br> ***(ESTO ES BAYES)*** | **VP/(VP+FP)** | **180/(180+98)** | **64.7%** | **Si es marcado como spam, ¿qué % es realmente spam?** |
| **Valor Predictivo Negativo** <br> *(NPV)* | VN/(VN+FN) | 9,702/(9,702+20) | **99.8%** | Si es marcado como legítimo, ¿qué % es realmente legítimo? |
| **Exactitud** <br> *(Accuracy)* | (VP+VN)/Total | (180+9,702)/10,000 | **98.82%** | ¿Qué % de clasificaciones son correctas? |

**Resultado**: **64.7%** de probabilidad de que sea realmente spam.

**🔍 Observación clave**: Aunque el filtro es muy bueno (90% sensibilidad, 99% especificidad), solo 64.7% de los emails marcados como spam son realmente spam, debido a la baja prevalencia del spam (2%).

## Pasos Sistemáticos para Resolver Problemas con Bayes

### 1. **Identificación del Problema**
- ¿Te dan el efecto y preguntan por la causa?
- ¿Hay estructura "Si [resultado], ¿probabilidad de [origen]?"

### 2. **Definir Eventos Claramente**
- Causa: A₁, A₂, A₃, ... (mutuamente excluyentes y exhaustivos)
- Efecto: B

### 3. **Recopilar Datos**
- P(A₁), P(A₂), P(A₃), ... (probabilidades a priori)
- P(B|A₁), P(B|A₂), P(B|A₃), ... (verosimilitudes)

### 4. **Calcular Probabilidad Total**
- P(B) = Σ P(B|Aᵢ) × P(Aᵢ)

### 5. **Aplicar Bayes**
- P(Aᵢ|B) = [P(B|Aᵢ) × P(Aᵢ)] / P(B)

### 6. **Interpretar en Contexto**
- ¿Qué significa el resultado en términos del problema original?

## Errores Comunes

### 1. **Confundir P(A|B) con P(B|A)**
- **Error**: Pensar que son iguales
- **Realidad**: Generalmente son muy diferentes

### 2. **Olvidar Calcular P(B)**
- **Error**: Intentar aplicar Bayes sin el denominador
- **Solución**: Siempre calcular la probabilidad total primero

### 3. **No Considerar Todas las Causas**
- **Error**: Omitir causas posibles
- **Solución**: Verificar que P(A₁) + P(A₂) + ... = 1

### 4. **Malinterpretar Prevalencia**
- **Error**: No considerar cuán rara es la condición
- **Solución**: Prestar atención especial a las probabilidades a priori

### 5. **Confundir Sensibilidad y Especificidad**
- **Sensibilidad**: P(Positivo|Enfermo)
- **Especificidad**: P(Negativo|Sano) = 1 - P(Positivo|Sano)

## Aplicaciones Prácticas

### Diagnóstico Médico
- Interpretar resultados de pruebas
- Evaluar probabilidades de enfermedades

### Control de Calidad
- Identificar fuentes de defectos
- Optimizar procesos de producción

### Clasificación y Filtrado
- Detección de spam
- Reconocimiento de patrones

### Investigación Criminal
- Análisis de evidencia
- Probabilidades de culpabilidad

## Fórmulas de Referencia

- **Teorema de Bayes**: P(A|B) = [P(B|A) × P(A)] / P(B)
- **Forma extendida**: P(A|B) = [P(B|A) × P(A)] / [Σ P(B|Aᵢ) × P(Aᵢ)]
- **Probabilidad total**: P(B) = Σ P(B|Aᵢ) × P(Aᵢ)
- **Odds posteriores**: P(A|B)/P(A^C|B) = [P(B|A)/P(B|A^C)] × [P(A)/P(A^C)]

---

*Recuerda: Bayes es la herramienta para "dar vuelta" la probabilidad condicional cuando necesitas ir del efecto a la causa.*
