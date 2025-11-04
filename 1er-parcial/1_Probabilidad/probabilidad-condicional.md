# Guía: Probabilidad Condicional vs Intersección

## Introducción

Una de las confusiones más comunes en probabilidad es distinguir entre **probabilidad condicional** y **probabilidad de intersección**. Esta guía te ayudará a identificar las palabras clave en los enunciados para interpretar correctamente qué tipo de probabilidad se está describiendo.

## Definiciones Fundamentales

### Probabilidad Condicional: P(B|A)
- **Definición**: La probabilidad de que ocurra el evento B, **dado que** ya sabemos que ocurrió el evento A.
- **Fórmula**: P(B|A) = P(A ∩ B) / P(A)
- **Interpretación**: "De los casos donde A es verdadero, ¿qué porcentaje también cumple B?"

### Probabilidad de Intersección: P(A ∩ B)
- **Definición**: La probabilidad de que ocurran **ambos** eventos A y B simultáneamente.
- **Fórmula**: P(A ∩ B) = P(B|A) × P(A) = P(A|B) × P(B)
- **Interpretación**: "¿Qué porcentaje del total cumple tanto A como B?"

### Probabilidad Total
- **Definición**: Permite calcular la probabilidad de un evento B considerando todas las posibles causas.
- **Fórmula**: P(B) = Σ P(B|Aᵢ) × P(Aᵢ)
- **Uso**: Fundamental para problemas con múltiples escenarios o causas.

## Diferencia Clave

**P(B|A) = 0.25** significa:
> "**Dado que** el televisor es de marca 1, la probabilidad de que necesite reparación es 25%"

**P(A ∩ B) = 0.125** significa:
> "La probabilidad de que un televisor **aleatorio** sea de marca 1 **Y** necesite reparación es 12.5%"

## Palabras Clave para Identificar Probabilidad Condicional

### ✅ Indican probabilidad condicional:

- **"El X% de los [grupo específico]"**
  - Ejemplo: "El 25% de los televisores **de marca 1** necesita reparación"
  
- **"Entre los [grupo específico]"**
  - Ejemplo: "Entre los estudiantes **de ingeniería**, el 30% reprueba matemáticas"
  
- **"Dado que [condición]"**
  - Ejemplo: "Dado que es **de marca 1**, la probabilidad de reparación es 25%"
  
- **"Sabiendo que [condición]"**
  - Ejemplo: "Sabiendo que es **estudiante de medicina**, el 40% estudia en privada"
  
- **"De los que son [condición]"**
  - Ejemplo: "De los que son **mayores de 30 años**, el 60% tiene casa propia"

### ❌ Indicarían intersección:

- **"El X% del total"**
  - Ejemplo: "El 12.5% **del total** son de marca 1 y necesitan reparación"
  
- **"El X% de toda la población"**
  - Ejemplo: "El 15% **de toda la población** estudia ingeniería y reprueba matemáticas"
  
- **"La probabilidad de que sea [condición A] y [condición B]"**
  - Ejemplo: "La probabilidad de que sea de marca 1 **y** necesite reparación es 12.5%"

## Ejemplo Práctico: Televisores

### Enunciado Original:
*"Se sabe que el 25% de los televisores de marca 1 necesita reparación estando en garantía, mientras que los porcentajes correspondientes a las marcas 2 y 3 son 20% y 10% respectivamente."*

### Análisis Semántico:
- **"de los televisores de marca 1"** → Indica subgrupo específico
- **"de marca 1"** → Define la condición (A₁)
- Esta es claramente una **probabilidad condicional**: P(B|A₁) = 0.25

### Datos del Problema:
- P(A₁) = 0.50 (50% son marca 1)
- P(A₂) = 0.30 (30% son marca 2)  
- P(A₃) = 0.20 (20% son marca 3)
- P(B|A₁) = 0.25 (25% de marca 1 necesita reparación)
- P(B|A₂) = 0.20 (20% de marca 2 necesita reparación)
- P(B|A₃) = 0.10 (10% de marca 3 necesita reparación)

### Cálculos Paso a Paso:

**1. Intersecciones (Probabilidades Conjuntas):**
- P(A₁ ∩ B) = P(B|A₁) × P(A₁) = 0.25 × 0.50 = 0.125
- P(A₂ ∩ B) = P(B|A₂) × P(A₂) = 0.20 × 0.30 = 0.06
- P(A₃ ∩ B) = P(B|A₃) × P(A₃) = 0.10 × 0.20 = 0.02

**2. Probabilidad Total:**
P(B) = P(A₁ ∩ B) + P(A₂ ∩ B) + P(A₃ ∩ B) = 0.125 + 0.06 + 0.02 = 0.205

**Interpretación**: El 20.5% de todos los televisores necesitará reparación.

## Ejemplo Numérico Concreto

Imagina 1000 televisores:
- 500 son marca 1, 300 marca 2, 200 marca 3
- De los 500 de marca 1: 125 necesitan reparación (25%)
- De los 300 de marca 2: 60 necesitan reparación (20%)
- De los 200 de marca 3: 20 necesitan reparación (10%)

**Verificación:**
- P(A₁ ∩ B) = 125/1000 = 0.125 ✓
- P(B) = (125 + 60 + 20)/1000 = 205/1000 = 0.205 ✓

## Ejemplo 2: Análisis de Estudiantes

### Enunciado:
*"En una universidad, el 40% de los estudiantes son de ingeniería, el 35% de medicina y el 25% de derecho. Se sabe que el 15% de los estudiantes de ingeniería tienen beca, el 20% de los de medicina y el 10% de los de derecho."*

### Análisis Semántico:
- **"de los estudiantes de ingeniería"** → Probabilidad condicional
- **"de los de medicina"** → Probabilidad condicional
- **"de los de derecho"** → Probabilidad condicional

### Solución:
**Datos:**
- P(Ing) = 0.40, P(Med) = 0.35, P(Der) = 0.25
- P(Beca|Ing) = 0.15, P(Beca|Med) = 0.20, P(Beca|Der) = 0.10

**¿Cuál es la probabilidad de que un estudiante tenga beca?**
P(Beca) = P(Beca|Ing)×P(Ing) + P(Beca|Med)×P(Med) + P(Beca|Der)×P(Der)
P(Beca) = 0.15×0.40 + 0.20×0.35 + 0.10×0.25 = 0.06 + 0.07 + 0.025 = 0.155

**Respuesta**: 15.5% de los estudiantes tienen beca.

## Regla Práctica para Identificar

**Pregúntate siempre:**
> ¿El porcentaje se calcula sobre un subgrupo específico o sobre el total?

- **Subgrupo específico** → Probabilidad condicional P(B|A)
- **Total de la población** → Intersección P(A ∩ B) (si menciona dos condiciones simultáneas)

## Consejos para Exámenes

1. **Subrayar las palabras clave** en el enunciado
2. **Identificar el conjunto de referencia** (¿sobre qué población se calcula el porcentaje?)
3. **Distinguir entre "dado que" y "y"**
4. **Recordar**: Las probabilidades condicionales pueden ser mayores que las intersecciones
5. **Verificar**: Las probabilidades de eventos mutuamente excluyentes deben sumar 1

## Errores Comunes

1. **Confundir P(B|A) con P(A ∩ B)**
2. **No identificar correctamente el conjunto de referencia**
3. **Olvidar que P(A) debe ser > 0 para que P(B|A) esté definida**
4. **No verificar que todas las causas posibles sumen 100%**

## Fórmulas de Referencia

- **Probabilidad condicional**: P(B|A) = P(A ∩ B) / P(A)
- **Intersección**: P(A ∩ B) = P(B|A) × P(A)
- **Probabilidad total**: P(B) = Σ P(B|Aᵢ) × P(Aᵢ)
- **Independencia**: P(B|A) = P(B) ⟺ A y B son independientes

---

*Recuerda: La clave está en identificar correctamente el conjunto de referencia en el enunciado.*
