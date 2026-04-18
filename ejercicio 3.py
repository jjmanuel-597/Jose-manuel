"""🟡 NIVEL INTERMEDIO 🟡

3. Verificador de números primos 🔢
Enunciado: Pedir un número entero y determinar si es primo.
Requerimientos: 
- Iterar con un for.
- Usar break al encontrar un divisor.
- Aprovechar la estructura for...else de Python.
"""
numero = int(input("Ingrese un número entero: "))
if numero < 2:
    print(f"{numero} no es un número primo.")
else:
    for divisor in range(2, int(numero**0.5) + 1):
        if numero % divisor == 0:
            print(f"{numero} no es un número primo.")
            break
    else:
        print(f"{numero} es un número primo.")
