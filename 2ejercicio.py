"""Enunciado: Calcula la suma de todos los números del 1 hasta un límite ingresado por el usuario.
Requerimientos: Usa un bucle for, la función range() y el operador de asignación +="""

limite = int(input("Ingrese un número entero como límite: "))

suma = 0

for numero in range(1, limite + 1):
    suma += numero  

print(f"La suma de los números del 1 al {limite} es: {suma}.")
