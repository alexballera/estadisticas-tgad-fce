# Guía Rápida HP Prime: Funciones Nativas de Probabilidad

## Introducción

Esta guía es una referencia directa para calcular probabilidades de **Variables Aleatorias Discretas y Continuas** utilizando las **funciones nativas** de la calculadora HP Prime.

**💡 Modo recomendado:** Trabajar en vista **CAS** para obtener resultados simbólicos y exactos.

---

## 1. Acceso a las Funciones de Probabilidad

La forma más directa de usar estas funciones es escribiendo su nombre en la línea de comandos del modo CAS. Alternativamente, se pueden encontrar en el menú de la calculadora:

- **Toolbox** → **Math** → **Probability** → **Densidad / Acumulada**

---

## 2. Variables Aleatorias Discretas

### Cómo Calcular Intervalos de Probabilidad (Reglas Generales)

Usa la función de distribución acumulada (la que termina en `_CDF`) como base para todos los cálculos de intervalos:

| Tipo de Probabilidad | Comando Genérico con la Función Acumulada (`Dist_CDF`) |
|:---------------------|:-----------------------------------------------------------|
| **P(X = k)**         | Usa la función de densidad específica (ej: `Binomial`, `Poisson`). |
| **P(X ≤ k)**         | `Dist_CDF(parámetros, k)`                                  |
| **P(X < k)**         | `Dist_CDF(parámetros, k-1)`                                |
| **P(X ≥ k)**         | `1 - Dist_CDF(parámetros, k-1)`                            |
| **P(X > k)**         | `1 - Dist_CDF(parámetros, k)`                              |
| **P(a ≤ X ≤ b)**     | `Dist_CDF(parámetros, b) - Dist_CDF(parámetros, a-1)`      |

### Distribución Binomial B(n, p)

- **n:** número de ensayos.
- **p:** probabilidad de éxito.

- **Probabilidad Puntual P(X = k):**
  - **Enunciado:** Se lanza una moneda 10 veces (n=10). La probabilidad de cara es 0.4 (p=0.4). ¿Cuál es la probabilidad de obtener **exactamente 3 caras** (k=3)?
  ```cas
  Binomial(10, 0.4, 3)
  
  // Resultado: ≈ 0.215
  ```

- **Probabilidad Acumulada P(X ≤ k):**
  - **Enunciado:** Con los mismos datos, ¿cuál es la probabilidad de obtener **3 caras o menos** (k≤3)?
  ```cas
  Binomial_CDF(10, 0.4, 3)
  
  // Resultado: ≈ 0.3823
  ```

### Distribución de Poisson Pois(λ)

- **λ:** número medio de ocurrencias en un intervalo.

- **Probabilidad Puntual P(X = k):**
  - **Enunciado:** Un centro de atención al cliente recibe un promedio de 2.5 llamadas por hora (λ=2.5). ¿Cuál es la probabilidad de recibir **exactamente 1 llamada** en una hora (k=1)?
  ```cas
  Poisson(2.5, 1)
  
  // Resultado: ≈ 0.2052
  ```

- **Probabilidad Acumulada P(X ≤ k):**
  - **Enunciado:** Con los mismos datos, ¿cuál es la probabilidad de recibir **3 llamadas o menos** (k≤3)?
  ```cas
  Poisson_CDF(2.5, 3)
  
  // Resultado: ≈ 0.7576
  ```

### Distribución Geométrica Geom(p)

- **p:** probabilidad de éxito en un ensayo.

- **Probabilidad Puntual P(X = k):** (Primer éxito en el k-ésimo ensayo)
  - **Enunciado:** La probabilidad de que un jugador enceste un tiro libre es 0.2 (p=0.2). ¿Cuál es la probabilidad de que su primer enceste ocurra en el **tercer intento** (k=3)?
  ```cas
  Geometric(0.2, 3)
  
  // Resultado: 0.128
  ```

- **Probabilidad Acumulada P(X ≤ k):**
  - **Enunciado:** Con los mismos datos, ¿cuál es la probabilidad de que el primer enceste ocurra en **5 intentos o menos** (k≤5)?
  ```cas
  Geometric_CDF(0.2, 5)
  
  // Resultado: 0.67232
  ```

### Distribución Hipergeométrica H(N, M, n)

La HP Prime **no tiene una función nativa**. Debemos crearla.

**Notación de la cátedra:**
- **N:** tamaño total de la población.
- **M:** número de elementos "exitosos" en la población (éxitos posibles).
- **n:** tamaño de la muestra extraída (sin reposición).
- **k:** número de "éxitos" en la muestra (variable aleatoria X).

**Fórmula:** 
$$P(X = k) = \frac{\binom{M}{k} \cdot \binom{N-M}{n-k}}{\binom{N}{n}}$$

**Orden de parámetros:** Primero los "totales" (N, n), luego los "éxitos" (M, k)

#### Crear la Función en HP Prime

**Método 1: Definición directa en CAS (Recomendado)**
```cas
Hypergeo(N, M, n, k) := (COMB(M,k) * COMB(N-M,n-k)) / COMB(N,n)
```

**Método 2: Usando el editor de programas**
1. Presiona `Shift` + `1` (Program)
2. Selecciona `New` y escribe el nombre: `Hypergeo`
3. Escribe el código:
```cas
EXPORT Hypergeo(N, M, n, k)
BEGIN
  RETURN (COMB(M,k) * COMB(N-M,n-k)) / COMB(N,n);
END;
```
4. Presiona `Check` para verificar
5. Presiona `ESC` para guardar

#### Modificar/Ver una Función CAS Existente

Si ya tienes la función definida con otros parámetros:

1. **Ver la definición actual:**
   - Entra a modo `CAS`
   - Escribe: `Hypergeo` (sin paréntesis)
   - Verás la definición actual

2. **Redefinir (más simple):**
   - En modo `CAS`, escribe la nueva definición:
     ```cas
     Hypergeo(N, M, n, k) := (COMB(M,k) * COMB(N-M,n-k)) / COMB(N,n)
     ```
   - Presiona `Enter` → se sobrescribe automáticamente

3. **Eliminar y recrear:**
   - En modo `CAS`, escribe: `PURGE(Hypergeo)`
   - Luego crea la nueva versión

#### Ejemplo de Uso

- **Enunciado:** En una caja hay 50 fusibles (N=50), de los cuales 10 son defectuosos (M=10). Si se selecciona una muestra aleatoria de 5 fusibles (n=5) sin reposición, ¿cuál es la probabilidad de que **exactamente 2** de ellos sean defectuosos (k=2)?
  
  **Solución:**
  ```cas
  Hypergeo(50, 10, 5, 2)
  
  // Resultado: ≈ 0.2098
  ```

#### Probabilidad Acumulada P(X ≤ k)

Para calcular la probabilidad acumulada, usa la función `SUM`:

- **Enunciado:** Con los mismos datos (N=50, M=10, n=5), ¿cuál es la probabilidad de encontrar **2 o menos** fusibles defectuosos (k≤2)?
  ```cas
  SUM(Hypergeo(50, 10, 5, j), j, 0, 2)
  
  // Resultado: ≈ 0.9517
  ```

**Nota:** El orden de los parámetros es importante: **N (población total), M (éxitos en población), n (muestra), k (éxitos en muestra)**

---

### Distribución Exponencial Exp(λ)

⚠️ **La HP Prime NO tiene función nativa para la Exponencial.** Debes crearla manualmente.

**Parámetros:**
- **λ** (lambda): Tasa de ocurrencia por unidad de tiempo
- **Media**: E(X) = 1/λ
- **Varianza**: V(X) = 1/λ²

**Fórmula:** 
$$F(x) = P(X \leq x) = 1 - e^{-\lambda x}$$

**Uso típico:** Tiempo hasta que ocurre un evento (variable continua)

#### Crear la Función en HP Prime

**Método 1: Definición directa en CAS (Recomendado)**
```cas
Expon_CDF(lambda, x) := 1 - exp(-lambda*x)
```

**Método 2: Usando funciones separadas**
```cas
# Definir el parámetro
lambda := 0.04

# Función de densidad (opcional)
f_expon(x) := lambda*exp(-lambda*x)

# Función de distribución acumulada
F_expon(x) := 1 - exp(-lambda*x)
```

#### Modificar/Ver una Función CAS Existente

1. **Ver la definición actual:**
   - Entra a modo `CAS`
   - Escribe: `Expon_CDF` (sin paréntesis)
   - Verás la definición actual

2. **Redefinir (más simple):**
   - En modo `CAS`, escribe la nueva definición:
     ```cas
     Expon_CDF(lambda, x) := 1 - exp(-lambda*x)
     ```
   - Presiona `Enter` → se sobrescribe automáticamente

3. **Eliminar y recrear:**
   - En modo `CAS`, escribe: `PURGE(Expon_CDF)`
   - Luego crea la nueva versión

#### Ejemplo de Uso

- **Enunciado:** El tiempo de revisión de motores sigue una distribución exponencial con media de 25 minutos (λ = 0.04). ¿Cuál es la probabilidad de que el tiempo sea **menor a 10 minutos**?
  
  **Solución:**
  ```cas
  Expon_CDF(0.04, 10)
  
  // Resultado: 0.3296799539643607 ≈ 0.3297
  ```

#### Cálculos Típicos con Exponencial

**P(X ≤ x):** Probabilidad acumulada
```cas
Expon_CDF(0.04, 10)
// Resultado: 0.3297
```

**P(X > x):** Complemento (propiedad de falta de memoria)
```cas
1 - Expon_CDF(0.04, 10)
// O directamente:
exp(-0.04*10)
// Resultado: 0.6703
```

**P(a < X < b):** Probabilidad en intervalo
```cas
Expon_CDF(0.04, 20) - Expon_CDF(0.04, 10)
// Resultado: P(10 < X < 20)
```

**Nota importante sobre probabilidad puntual:** 
- ⚠️ Para variables continuas, **P(X = x₀) = 0** siempre
- Solo tiene sentido calcular P(X ≤ x) o P(a < X < b)
- La función de densidad f(x) NO es una probabilidad, es una densidad

---

## 3. Variables Aleatorias Continuas

### Distribución Normal N(μ, σ²)

- **μ:** media de la población.
- **σ:** desviación estándar de la población.

- **Probabilidad Acumulada P(a ≤ X ≤ b):**
  - **Enunciado:** Los pesos de un producto siguen una distribución normal con media μ=10g y desviación estándar σ=2g. ¿Cuál es la probabilidad de que un producto pese **entre 8g y 12g**?
  ```cas
  Normal_CDF(10, 2, 8, 12)
  
  // Resultado: ≈ 0.6827
  ```
  - **Enunciado (P(X ≤ x)):** ¿Cuál es la probabilidad de que un producto pese **12g o menos**?
    ```cas
    Normal_CDF(10, 2, -∞, 12)
    
    // Resultado: ≈ 0.8413
    ```
  - **Enunciado (P(X ≥ x)):** ¿Cuál es la probabilidad de que un producto pese **11g o más**?
    ```cas
    Normal_CDF(10, 2, 11, ∞)
    
    // Resultado: ≈ 0.3085
    ```

### Distribución t de Student t(ν)

- **ν:** grados de libertad.

- **Probabilidad Acumulada P(a ≤ T ≤ b):**
  - **Enunciado:** Para una distribución t-Student con 10 grados de libertad (ν=10), ¿cuál es la probabilidad de que el valor de t se encuentre **entre -2.228 y 2.228**?
  ```cas
  Student_CDF(10, -2.228, 2.228)
  
  // Resultado: ≈ 0.95
  ```

### Distribución Chi-cuadrado χ²(ν)

- **ν:** grados de libertad.

- **Probabilidad Acumulada P(X ≤ x):**
  - **Enunciado:** Para una distribución Chi-cuadrado con 5 grados de libertad (ν=5), ¿cuál es la probabilidad de que el valor del estadístico sea **menor o igual a 11.07**?
  ```cas
  ChiSquare_CDF(5, 0, 11.07)
  
  // Resultado: ≈ 0.95
  ```

### Distribuciones sin Función Nativa (Uniforme, Exponencial)

Para estas distribuciones, debes usar sus fórmulas de densidad `f(x)` y acumulada `F(x)` directamente.

- **Uniforme U(a, b):**
  - `f(x) := 1/(b-a)`
  - `F(x) := (x-a)/(b-a)`
  - Probabilidad: `P(c ≤ X ≤ d) = F(d) - F(c)`

- **Exponencial Exp(λ):**
  - `f(x) := λ*exp(-λ*x)`
  - `F(x) := 1 - exp(-λ*x)`
  - Probabilidad: `P(X ≥ x) = 1 - F(x) = exp(-λ*x)`
