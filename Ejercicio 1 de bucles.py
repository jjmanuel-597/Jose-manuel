"""🟢 NIVEL FÁCIL 🟢

1. Acumulador con interrupción ➕
Enunciado: Desarrollar un programa que pida números enteros para sumarlos. El programa debe detenerse y mostrar el resultado total SOLAMENTE cuando se ingrese un 0.
Requerimientos: 
- Usar bucle while.
- Usar break para salir con el 0.
"""



total = 0
while True:
    numero = int(input("Ingrese un número entero (0 para finalizar): "))
    if numero == 0:
        break
    total += numero
print(f"El resultado total es: {total}")

