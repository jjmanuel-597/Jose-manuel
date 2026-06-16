"""Enunciado: De una lista mixta de números, extrae solo los estrictamente positivos a una nueva lista.
Requerimientos: Itera con un for, evalúa con un if y > y usa .append()."""


numeros_mixtos = [3, -1, 0, 5, -2, 8, -4, 7]

numeros_positivos = []

for numero in numeros_mixtos:
   
    if numero > 0:
        numeros_positivos.append(numero)  

print("Números estrictamente positivos:", numeros_positivos)
