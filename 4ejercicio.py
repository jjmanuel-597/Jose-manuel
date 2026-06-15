"""Enunciado: Cuenta cuántas vocales tiene una frase ingresada por el usuario.
Requerimientos: Recorre el string con un for, usa un if con el operador in y mantén un contador."""

frase = input("Ingrese una frase: ")
contador_vocales = 0
vocales = "aeiouAEIOU"
for letra in frase:
    if letra in vocales:
        contador_vocales += 1
print("La cantidad de vocales en la frase es:", contador_vocales)
