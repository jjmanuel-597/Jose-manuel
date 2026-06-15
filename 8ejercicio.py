"""Enunciado: Encuentra los elementos comunes entre dos listas sin incluir duplicados.
Requerimientos: Convierte las listas a set y usa el operador de intersección &."""

lista1 = [1, 2, 3, 4, 5, 5]
lista2 = [4, 5, 6, 7, 8, 8]
comunes = set(lista1) & set(lista2)
print(f"Elementos comunes: {comunes}")
