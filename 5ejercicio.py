"""Enunciado: El programa tiene un número secreto del 1 al 10. El usuario debe adivinarlo pidiendo intentos hasta lograrlo.
Requerimientos: Usa un bucle while controlado por el operador de diferencia !=."""

import random
numero_secreto = random.randint(1, 10)
intento = 0 
while intento != numero_secreto:
    intento = int(input("Adivina el número secreto (entre 1 y 10): "))
print("¡Felicidades! Has adivinado el número secreto:", numero_secreto)
