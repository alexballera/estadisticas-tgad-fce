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

### Distribución Hipergeométrica H(N, K, n)

La HP Prime **no tiene una función nativa**. Debemos crearla.

- **N:** tamaño total de la población.
- **K:** número de elementos "exitosos" en la población.
- **n:** tamaño de la muestra extraída.
- **k:** número de "éxitos" en la muestra.

- **Función Personalizada para P(X = k):**
  Define esta función una vez en el modo CAS:
  ```cas
  Hypergeo(N, K, n, k) := (COMB(K,k) * COMB(N-K,n-k)) / COMB(N,n)
  ```
  - **Enunciado:** En una caja hay 50 fusibles (N=50), de los cuales 10 son defectuosos (K=10). Si se selecciona una muestra aleatoria de 5 fusibles (n=5), ¿cuál es la probabilidad de que **exactamente 2** de ellos sean defectuosos (k=2)?
    ```cas
    Hypergeo(50, 10, 5, 2)
    
    // Resultado: ≈ 0.2098
    ```

- **Probabilidad Acumulada P(X ≤ k):**
  Para calcular la probabilidad acumulada, usa la función `SUM` directamente con la función `Hypergeo` que ya definiste.
  - **Enunciado:** Con los mismos datos (N=50, K=10, n=5), ¿cuál es la probabilidad de encontrar **2 o menos** fusibles defectuosos (k≤2)?
  ```cas
  SUM(Hypergeo(50, 10, 5, j), j, 0, 2)
  
  // Resultado: ≈ 0.9517
  ```

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
