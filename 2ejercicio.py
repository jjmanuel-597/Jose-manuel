"""Enunciado: Calcula la suma de todos los números del 1 hasta un límite ingresado por el usuario.
Requerimientos: Usa un bucle for, la función range() y el operador de asignación +="""

# Solicitar al usuario que ingrese un límite entero
limite = int(input("Ingrese un número entero como límite: "))
# Inicializar la variable para almacenar la suma
suma = 0
# Utilizar un bucle for para iterar desde 1 hasta el límite
for numero in range(1, limite + 1):
    suma += numero  # Sumar el número actual a la variable suma
# Imprimir el resultado de la suma
print(f"La suma de los números del 1 al {limite} es: {suma}.")
