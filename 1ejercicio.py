"""Enunciado: Crea un programa que pida un número entero y determine si es par o impar.
Requerimientos: Usa input(), el operador de módulo (%) y una estructura condicional if-else"""

# Solicitar al usuario que ingrese un número entero
numero = int(input("Ingrese un número entero: "))
# Verificar si el número es par o impar utilizando el operador de módulo
if numero % 2 == 0:
    print(f"El número {numero} es par.")
else:    print(f"El número {numero} es impar.")
