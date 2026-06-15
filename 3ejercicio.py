"""Enunciado: De una lista mixta de números, extrae solo los estrictamente positivos a una nueva lista.
Requerimientos: Itera con un for, evalúa con un if y > y usa .append()."""

# Lista mixta de números
numeros_mixtos = [3, -1, 0, 5, -2, 8, -4, 7]
# Lista para almacenar los números estrictamente positivos
numeros_positivos = []
# Iterar sobre cada número en la lista mixta
for numero in numeros_mixtos:
    # Evaluar si el número es estrictamente positivo
    if numero > 0:
        numeros_positivos.append(numero)  # Agregar el número a la lista de positivos
# Imprimir la lista de números estrictamente positivos
print("Números estrictamente positivos:", numeros_positivos)