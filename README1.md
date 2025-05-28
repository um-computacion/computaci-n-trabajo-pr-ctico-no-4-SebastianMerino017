# Trabajo Práctico 4: Recursividad


# Informacion del alumno
Autor: Sebastian Merino
Legajo: 63284

# Descripción General
Este repositorio contiene implementaciones de funciones matemáticas comunes utilizando enfoques iterativos y recursivos, además de una función para aplanar estructuras de datos anidadas. El proyecto fue desarrollado siguiendo la metodología TDD (Test-Driven Development).

# Estructura del Proyecto
proyecto-algoritmos/
├── factorial.py           # Implementaciones de factorial
├── test_factorial.py      # Pruebas para factorial
├── fibonacci.py           # Implementaciones de fibonacci
├── test_fibonacci.py      # Pruebas para fibonacci
├── flatten.py             # Implementación de aplanar listas
├── test_flatten.py        # Pruebas para aplanar listas
└── README.md              # Este archivo


## Etapa 1: Factorial

# Descripción del Problema
El factorial de un número entero positivo n, denotado como n!, es el producto de todos los números enteros positivos menores o iguales a n.
Fórmula: n! = n × (n-1) × (n-2) × ... × 2 × 1

# Implementaciones
Versión Iterativa: Utiliza un bucle for para calcular el producto
Versión Recursiva: Utiliza la definición matemática recursiva

# Instrucciones de Ejecución
Ejecutar pruebas del factorial
python -m unittest test_factorial.py

Ejecutar todas las pruebas con más detalle
python -m unittest test_factorial.py -v

## Ejemplos de uso
from factorial import factorial_iterative, factorial_recursive

# Ejemplo con la versión iterativa
resultado1 = factorial_iterative(5)
print(f"5! (iterativo) = {resultado1}")  # Output: 120

# Ejemplo con la versión recursiva
resultado2 = factorial_recursive(5)
print(f"5! (recursivo) = {resultado2}")  # Output: 120

# Casos especiales
print(f"0! = {factorial_iterative(0)}")  # Output: 1
print(f"1! = {factorial_iterative(1)}")  # Output: 1


## Etapa 2: Fibonacci

# Descripción del Problema
La secuencia de Fibonacci es una serie de números donde cada número es la suma de los dos anteriores.

# Definición:
F(0) = 0
F(1) = 1
F(n) = F(n-1) + F(n-2) para n > 1

# Implementaciones
Versión Iterativa: Más eficiente, O(n) tiempo y O(1) espacio
Versión Recursiva: Más intuitiva pero menos eficiente, O(2^n) tiempo

# Instrucciones de Ejecución
Ejecutar pruebas de fibonacci
python -m unittest test_fibonacci.py

Ejecutar con detalle
python -m unittest test_fibonacci.py -v

# Ejemplos de uso
from fibonacci import fibonacci_iterative, fibonacci_recursive

# Secuencia de Fibonacci hasta el índice 10
for i in range(11):
    fib_iter = fibonacci_iterative(i)
    fib_rec = fibonacci_recursive(i)
    print(f"F({i}) = {fib_iter} (ambos métodos dan el mismo resultado)")

# Ejemplo específico
print(f"El 10mo número de Fibonacci es: {fibonacci_iterative(10)}")  # Output: 55


## Etapa 3: Aplanar Listas

# Descripción del Problema
Implementar una función recursiva que convierta listas anidadas de cualquier profundidad en una lista plana (un solo nivel).

# Casos de Uso Soportados
Listas simples: [1, 2, 3, 4]
Listas anidadas: [1, [2, 3], [4, [5, 6]]]
Estructuras mixtas: [1, (2, 3), {'a': 4, 'b': 5}, [6, [7, 8]]]

# Instrucciones de Ejecución
Ejecutar pruebas de flatten
python -m unittest test_flatten.py

Ejecutar con detalle
python -m unittest test_flatten.py -v

# Ejemplos de uso
from flatten import flatten_list

# Caso 1: Lista simple
lista1 = [1, 2, 3, 4]
resultado1 = flatten_list(lista1)
print(f"Lista simple: {lista1}")
print(f"Resultado: {resultado1}")
# Output: [1, 2, 3, 4]

# Caso 2: Lista con listas anidadas
lista2 = [1, [2, 3], [4, [5, 6]]]
resultado2 = flatten_list(lista2)
print(f"Lista anidada: {lista2}")
print(f"Resultado: {resultado2}")
# Output: [1, 2, 3, 4, 5, 6]

# Caso 3: Lista con diferentes estructuras
lista3 = [1, (2, 3), {'a': 4, 'b': 5}, [6, [7, 8]]]
resultado3 = flatten_list(lista3)
print(f"Lista mixta: {lista3}")
print(f"Resultado: {resultado3}")
# Output: [1, 2, 3, 'a', 4, 'b', 5, 6, 7, 8]

