# Guía HP Prime: Variables Aleatorias Continuas

## Introducción

Esta guía explica cómo utilizar la calculadora HP Prime para trabajar con **Variables Aleatorias Continuas**, incluyendo el cálculo de funciones de densidad, distribución acumulada y probabilidades asociadas.

**💡 Modo recomendado:** Trabajar en vista **CAS** (Sistema Algebraico Computacional) para obtener resultados simbólicos exactos. Accede presionando la tecla `CAS`.

---

## 1. Funciones de Densidad de Probabilidad

### 1.1 Verificar que f(x) es una función de densidad válida

Una función f(x) es una función de densidad de probabilidad si:

- f(x) ≥ 0 para todo x
- ∫_{-∞}^{∞} f(x) dx = 1

**Sintaxis en HP Prime:**

```
# Definir la función de densidad
f(x) := expresión_de_x

# Verificar que la integral es 1
int(f(x), x, a, b)
```

**Ejemplo práctico:**

```
# Función f(x) = (3/26)x² para 1 ≤ x ≤ 3
f(x) := (3/26)*x^2

# Verificar integral
int(f(x), x, 1, 3)
```

**Resultado:** `1` ✓

---

## 2. Función de Distribución Acumulada F(x)

### 2.1 Definición y Cálculo

La función de distribución acumulada se define como:
**F(x) = P(X ≤ x) = ∫_{-∞}^{x} f(t) dt**

**Sintaxis en HP Prime:**

```
# Calcular F(x) para un intervalo específico
F(x) := int(f(t), t, límite_inferior, x)

# Simplificar la expresión resultante
simplify(F(x))
```

**Ejemplo paso a paso:**

```
# Definir f(x)
f(x) := (3/26)*x^2

# Calcular F(x) para 1 ≤ x ≤ 3
F(x) := int(f(t), t, 1, x)

# Simplificar
simplify(F(x))
```

**Resultado:** `(x³-1)/26`

### 2.2 Función F(x) por tramos

Para una función de densidad definida por tramos, F(x) también será por tramos:

```
F(x) = {
  0           si x < 1
  (x³-1)/26   si 1 ≤ x < 3  
  1           si x ≥ 3
}
```

### 2.3 Evaluación de F(x) en puntos específicos

```
# Ejemplos de evaluación
F(2)        # Para x = 2
F(2.5)      # Para x = 2.5  
F(3)        # Para x = 3
```

---

## 3. Cálculo de Probabilidades

### 3.1 Probabilidades Básicas

| Tipo de Probabilidad | Fórmula | Comando HP Prime |
|:---------------------|:--------|:-----------------|
| **P(X ≤ a)** | F(a) | `F(a)` |
| **P(X < a)** | F(a⁻) | `F(a)` (si F es continua) |
| **P(X ≥ a)** | 1 - F(a) | `1 - F(a)` |
| **P(X > a)** | 1 - F(a) | `1 - F(a)` |
| **P(a < X ≤ b)** | F(b) - F(a) | `F(b) - F(a)` |
| **P(a ≤ X ≤ b)** | F(b) - F(a⁻) | `F(b) - F(a)` |

### 3.2 Ejemplos Prácticos

**Ejemplo 1: P(X ≤ 2)**

```
F(2)
# o directamente:
(2^3-1)/26
```

**Resultado:** `7/26 ≈ 0.2692`

**Ejemplo 2: P(1.5 < X ≤ 2.5)**

```
F(2.5) - F(1.5)
# o paso a paso:
((2.5)^3-1)/26 - ((1.5)^3-1)/26
```

**Resultado:** `12.25/26 ≈ 0.4712`

**Ejemplo 3: P(X > 2)**

```
1 - F(2)
# o directamente:
1 - (2^3-1)/26
```

**Resultado:** `19/26 ≈ 0.7308`

---

## 4. Comandos Útiles Adicionales

### 4.1 Conversión entre Exacto y Aproximado

```
# Convertir resultado exacto a decimal
approx(7/26)              # → 0.269230769231

# Convertir decimal a fracción exacta
exact(0.2692)             # → 673/2500 (aproximación)
```

### 4.2 Resolución de Ecuaciones

```
# Encontrar valores de x para probabilidades específicas
solve(F(x) = 0.5, x)      # Encuentra la mediana
solve(F(x) = 0.25, x)     # Encuentra el primer cuartil
solve(F(x) = 0.75, x)     # Encuentra el tercer cuartil
```

### 4.3 Verificación de Propiedades

```
# Verificar que F es no decreciente
diff(F(x), x)             # La derivada debe ser ≥ 0

# Verificar continuidad
limit(F(x), x, punto, -1) # Límite por izquierda
limit(F(x), x, punto, 1)  # Límite por derecha
```

---

## 5. Distribuciones Continuas Estándar

### 5.1 Distribución Uniforme U(a,b)

#### 📋 **Definición y Propiedades**

Una variable aleatoria X sigue una **distribución uniforme continua** en el intervalo [a, b] si todos los valores en ese intervalo tienen la misma probabilidad de ocurrir.

**Notación:** X ~ U(a, b)

**Parámetros:**

- **a**: límite inferior del intervalo
- **b**: límite superior del intervalo (con b > a)

#### 📐 **Funciones principales**

**Función de densidad de probabilidad:**

```
f(x) := 1/(b-a)           # para a ≤ x ≤ b
        0                  # en otro caso
```

**Función de distribución acumulada:**

```
F(x) := 0                 # si x < a
        (x-a)/(b-a)       # si a ≤ x ≤ b
        1                 # si x > b
```

**Valor esperado (media):**

```
E(X) = (a+b)/2
```

**Varianza:**

```
V(X) = (b-a)²/12
```

**Desviación estándar:**

```
σ(X) = (b-a)/sqrt(12)
```

#### 🔧 **Implementación en HP Prime**

**Paso 1: Definir los parámetros**

```
# Asignar valores a los límites
a := límite_inferior
b := límite_superior
```

**Paso 2: Definir la función de densidad**

```
f(x) := 1/(b-a)
```

**Paso 3: Definir la función de distribución**

```
# Método 1: Directamente con la fórmula
F(x) := (x-a)/(b-a)

# Método 2: Usando integración (más general)
F(x) := int(f(t), t, a, x)
```

**Paso 4: Verificar que es función de densidad válida**

```
# La integral debe dar 1
int(f(x), x, a, b)        # Debe resultar: 1
```

#### 📊 **Cálculo de Probabilidades**

**Probabilidades básicas:**

```
# P(X ≤ c) para a ≤ c ≤ b
F(c)                      # → (c-a)/(b-a)

# P(X < c) - Para variables continuas es igual a P(X ≤ c)
F(c)                      # → (c-a)/(b-a)

# P(X ≥ c)
1 - F(c)                  # → (b-c)/(b-a)

# P(X > c) - Para variables continuas es igual a P(X ≥ c)
1 - F(c)                  # → (b-c)/(b-a)

# P(c₁ < X < c₂) con a ≤ c₁ < c₂ ≤ b
F(c₂) - F(c₁)            # → (c₂-c₁)/(b-a)

# P(c₁ ≤ X ≤ c₂)
F(c₂) - F(c₁)            # → (c₂-c₁)/(b-a)
```

#### 📈 **Estadísticos**

```
# Esperanza (Media)
media := (a+b)/2
simplify(media)

# Varianza
varianza := (b-a)^2/12
simplify(varianza)

# Desviación estándar
desv_std := sqrt(varianza)
simplify(desv_std)
```

#### 🎯 **Percentiles y Cuantiles**

Para encontrar el valor x tal que P(X ≤ x) = p:

```
# Resolver F(x) = p
solve((x-a)/(b-a) = p, x)

# Resultado: x = a + p*(b-a)
```

**Cuartiles:**

```
# Primer cuartil (Q1): p = 0.25
Q1 := a + 0.25*(b-a)

# Mediana (Q2): p = 0.5
Q2 := a + 0.5*(b-a)      # También es la media

# Tercer cuartil (Q3): p = 0.75
Q3 := a + 0.75*(b-a)
```

#### ✅ **Ejemplo completo genérico**

```
// Definir distribución uniforme U(a,b)
// Supongamos U(c, d) donde c y d son valores específicos

// Paso 1: Parámetros
a := c
b := d

// Paso 2: Función de densidad
f(x) := 1/(b-a)

// Paso 3: Función de distribución
F(x) := (x-a)/(b-a)

// Paso 4: Verificación
int(f(x), x, a, b)       // Debe dar 1

// Paso 5: Estadísticos
media := (a+b)/2
varianza := (b-a)^2/12
desv_std := sqrt((b-a)^2/12)

// Paso 6: Probabilidades (para valores específicos c₁, c₂)
F(c₁)                    // P(X ≤ c₁)
1 - F(c₂)                // P(X > c₂)
F(c₂) - F(c₁)           // P(c₁ < X < c₂)

// Paso 7: Cuantiles
solve(F(x) = 0.5, x)     // Mediana
solve(F(x) = 0.25, x)    // Q1
solve(F(x) = 0.75, x)    // Q3
```

#### 💡 **Propiedades especiales de la Uniforme**

1. **Propiedad de memoria inexistente**: A diferencia de la exponencial, la uniforme no tiene propiedad de falta de memoria.

2. **Simetría**: La distribución es simétrica alrededor de la media (a+b)/2.

3. **Probabilidad uniforme**:

   ```
   P(c₁ < X < c₂) = (c₂-c₁)/(b-a)
   ```

   Solo depende de la longitud del intervalo, no de su ubicación.

4. **Para cualquier punto individual**:

   ```
   P(X = k) = 0    # Para cualquier k ∈ [a,b]
   ```

#### ⚠️ **Casos especiales**

**Caso 1: Valores fuera del soporte**

```
# Para x < a
F(x) = 0

# Para x > b
F(x) = 1
```

**Caso 2: Probabilidades condicionales**

```
# P(X < c₂ | X > c₁) con a ≤ c₁ < c₂ ≤ b
P_cond := (F(c₂) - F(c₁))/(1 - F(c₁))
simplify(P_cond)
# Resultado: (c₂-c₁)/(b-c₁)
```

#### 📝 **Notas importantes**

- ✅ Siempre verificar que a < b
- ✅ Para variables continuas: P(X < c) = P(X ≤ c)
- ✅ Los resultados se pueden obtener en forma exacta (fracciones)
- ✅ Usar `simplify()` para expresiones más simples
- ✅ Usar `approx()` para convertir a decimal si es necesario

---

### 5.2 Distribución Exponencial Exp(λ)

⚠️ **La HP Prime NO tiene función nativa para la Exponencial.** Debes crearla manualmente.

**Parámetros:**
- **λ** (lambda): Tasa de ocurrencia por unidad de tiempo
- **Media**: E(X) = 1/λ
- **Varianza**: V(X) = 1/λ²

#### Crear Función Exponencial en CAS

**Método 1: Función de Probabilidad Acumulada (Recomendado)**

Define una función que calcule directamente P(X ≤ x):

```cas
Expon_CDF(lambda, x) := 1 - exp(-lambda*x)
```

**Uso:**
```cas
# Ejemplo: λ = 0.04, P(X < 10)
Expon_CDF(0.04, 10)

# Resultado: 0.3296799539643607 ≈ 0.3297
```

**Método 2: Definir funciones f(x) y F(x) separadas**

Si prefieres trabajar con la función de densidad y distribución por separado:

```cas
# Definir el parámetro
lambda := 0.04

# Función de densidad
f_expon(x) := lambda*exp(-lambda*x)

# Función de distribución acumulada
F_expon(x) := 1 - exp(-lambda*x)
```

**Uso:**
```cas
# P(X < 10)
F_expon(10)

# P(X > 10) = 1 - F(10)
1 - F_expon(10)

# P(5 < X < 15) = F(15) - F(5)
F_expon(15) - F_expon(5)
```

#### Modificar/Ver una Función CAS Existente

Si ya tienes `Expon_CDF` definida y quieres modificarla:

1. **Ver la definición actual:**
   ```cas
   Expon_CDF
   ```

2. **Redefinir:**
   ```cas
   Expon_CDF(lambda, x) := 1 - exp(-lambda*x)
   ```

3. **Eliminar:**
   ```cas
   PURGE(Expon_CDF)
   ```

#### Ejemplo Completo - Ejercicio 14

**Enunciado:** El tiempo de revisión de motores sigue una distribución exponencial con media de 25 minutos. ¿Cuál es la probabilidad de que el tiempo sea menor a 10 minutos?

**Solución:**

```cas
# Paso 1: Calcular λ
# Si media = 25 min, entonces λ = 1/25 = 0.04
lambda := 1/25

# Paso 2: Crear la función (si no existe)
Expon_CDF(lambda, x) := 1 - exp(-lambda*x)

# Paso 3: Calcular P(X < 10)
Expon_CDF(0.04, 10)
```

**Resultado:** `0.329679953964...` ≈ **0.3297** (32.97%)

**Verificación manual:**
```cas
# Cálculo directo de F(x) = 1 - e^(-λx)
1 - exp(-0.04*10)

# O más explícito
1 - exp(-0.4)
```

#### Propiedades Útiles de la Exponencial

```cas
# Media
media := 1/lambda

# Varianza
varianza := 1/(lambda^2)

# Desviación estándar
desv_std := 1/lambda

# Propiedad de falta de memoria: P(X > s+t | X > s) = P(X > t)
# P(X > t) = e^(-λt)
prob_mayor_t := exp(-lambda*t)
```

### 5.3 Distribución Normal N(μ,σ²)

La HP Prime tiene funciones integradas para la distribución normal:

```
# Función de distribución estándar N(0,1)
normald(z)                # P(Z ≤ z)

# Para N(μ,σ²), estandarizar primero:
z := (x - μ)/σ
normald(z)
```

---

## 6. Consejos y Buenas Prácticas

### ✅ **Ventajas de usar HP Prime para Variables Continuas:**

1. **Cálculo simbólico exacto** de integrales
2. **Resultados en fracciones** exactas en lugar de aproximaciones
3. **Verificación rápida** de cálculos manuales
4. **Capacidad gráfica** para visualizar funciones
5. **Resolución de ecuaciones** para encontrar percentiles

### 💡 **Consejos prácticos:**

1. **Siempre verificar** que ∫f(x)dx = 1 antes de proceder
2. **Usar `simplify()`** para obtener expresiones más simples
3. **Definir funciones** con `:=` para reutilizarlas
4. **Verificar límites** de F(x): F(-∞) = 0 y F(∞) = 1
5. **Usar `exact()`** cuando necesites fracciones exactas

### ⚠️ **Limitaciones:**

- No tiene funciones predefinidas para distribuciones continuas personalizadas
- Requiere definir manualmente las funciones f(x) y F(x)
- Los gráficos pueden requerir configuración manual de rangos

---

## 7. Ejercicios de Práctica

### Ejercicio 1: Distribución Triangular

Dada f(x) = 2x para 0 ≤ x ≤ 1:

1. Verificar que es función de densidad
2. Calcular F(x)
3. Encontrar P(X ≤ 0.5)

**Solución en HP Prime:**

```
f(x) := 2*x
int(f(x), x, 0, 1)        # Verificar = 1
F(x) := int(f(t), t, 0, x)
simplify(F(x))            # Resultado: x²
F(0.5)                    # Resultado: 1/4
```

### Ejercicio 2: Mediana

Para la función del ejercicio principal, encontrar la mediana.

**Solución:**

```
solve(F(x) = 0.5, x)      # Resolver (x³-1)/26 = 0.5
```

---

## Referencias

- Manual oficial HP Prime
- Documentación CAS integrada: `Help` → `CAS Commands`
- Para más funciones: `Toolbox` → `Math` → `Calculus`

---

**📚 Nota:** Esta guía complementa el trabajo realizado en Python y proporciona una herramienta adicional para verificación y cálculo exacto de problemas de variables aleatorias continuas.
