"""Enunciado: Suma dos matrices 3x3 elemento por elemento y crea una matriz resultado.
Requerimientos: Emplea listas de listas, bucles for anidados e indexación doble [i][j]."""

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

resultado = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
for i in range(3):
    for j in range(3):
        resultado[i][j] = A[i][j] + B[i][j]

print("Matriz A:")
for fila in A:
    print(fila)
print("\nMatriz B:")
for fila in B:
    print(fila)
print("\nMatriz Resultado (A + B):")
for fila in resultado:
    print(fila)
