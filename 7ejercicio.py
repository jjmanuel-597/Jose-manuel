"""Enunciado: Escribe una función que determine si un número es primo o no.
Requerimientos: Crea una función, usa un bucle for y el operador de módulo % para buscar divisores."""

def es_primo(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
# Ejemplo de uso
numero = 17
if es_primo(numero):
    print(f"{numero} es un número primo.")
else:    print(f"{numero} no es un número primo.")
