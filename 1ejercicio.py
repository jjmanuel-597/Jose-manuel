"""Enunciado: Crea un programa que pida un número entero y determine si es par o impar.
Requerimientos: Usa input(), el operador de módulo (%) y una estructura condicional if-else"""

numero = int(input("Ingrese un número entero: "))

if numero % 2 == 0:
    print(f"El número {numero} es par.")
else:    print(f"El número {numero} es impar.")
