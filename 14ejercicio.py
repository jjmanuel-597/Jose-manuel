"""Enunciado: Genera la serie de Fibonacci hasta N términos y guárdala en una lista.
Requerimientos: Usa un bucle while y la genial asignación múltiple de Python (a, b = b, a + b)."""

def fibonacci(n):
    serie = []
    a, b = 0, 1
    while len(serie) < n:
        serie.append(a)
        a, b = b, a + b  # Asignación múltiple para generar la serie
    return serie
# Ejemplo de uso
n = 10
resultado = fibonacci(n)
print(resultado)  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
