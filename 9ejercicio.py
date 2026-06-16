"""Enunciado: Muestra por consola las tablas de multiplicar del 1 al 5.
Requerimientos: Usa bucles for anidados y el operador de multiplicación *."""

for i in range(1, 6):
    print(f"Tabla de multiplicar del {i}:")
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
    print() 
