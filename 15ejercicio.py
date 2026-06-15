"""Enunciado: Suma dos matrices 3x3 elemento por elemento y crea una matriz resultado.
Requerimientos: Emplea listas de listas, bucles for anidados e indexación doble [i][j]."""

# Definir las matrices A y B
A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
B = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]
# Crear una matriz resultado inicializada con ceros
resultado = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
# Sumar las matrices A y B elemento por elemento
for i in range(3):
    for j in range(3):
        resultado[i][j] = A[i][j] + B[i][j]
# Imprimir la matriz resultado
print("Matriz A:")
for fila in A:
    print(fila)
print("\nMatriz B:")
for fila in B:
    print(fila)
print("\nMatriz Resultado (A + B):")
for fila in resultado:
    print(fila)
