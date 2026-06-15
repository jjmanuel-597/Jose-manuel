"""Enunciado: Analiza un párrafo y cuenta cuántas veces se repite cada palabra (ignorando mayúsculas).
Requerimientos: Usa .split(), y un bucle for para llenar un diccionario usando condicionales o el operador in."""

def contar_palabras(parrafo):
    palabras = parrafo.lower().split()  # Convertir a minúsculas y dividir el párrafo en palabras
    conteo = {}
    for palabra in palabras:
        if palabra in conteo:
            conteo[palabra] += 1  # Incrementar el conteo si la palabra ya está en el diccionario
        else:
            conteo[palabra] = 1  # Agregar la palabra al diccionario con un conteo inicial de 1
    return conteo
# Ejemplo de uso
parrafo = "Hola mundo. Hola a todos. El mundo es grande."
resultado = contar_palabras(parrafo)
print(resultado)  # {'hola': 2, 'mundo.': 1, 'a': 1, 'todos.': 1, 'el': 1, 'mundo': 1, 'es': 1, 'grande.': 1}
