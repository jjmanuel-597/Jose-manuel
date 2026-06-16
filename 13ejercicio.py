"""Enunciado: Analiza un párrafo y cuenta cuántas veces se repite cada palabra (ignorando mayúsculas).
Requerimientos: Usa .split(), y un bucle for para llenar un diccionario usando condicionales o el operador in."""

def contar_palabras(parrafo):
    palabras = parrafo.lower().split() 
    conteo = {}
    for palabra in palabras:
        if palabra in conteo:
            conteo[palabra] += 1 
        else:
            conteo[palabra] = 1 
    return conteo

parrafo = "Hola mundo. Hola a todos. El mundo es grande."
resultado = contar_palabras(parrafo)
print(resultado) 
