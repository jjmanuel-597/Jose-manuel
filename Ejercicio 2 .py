"""Saltando múltiplos 🦘
Enunciado: Imprimir los números del 1 al 20, saltándose todos los que sean múltiplos de 3.
Requerimientos: 
- Usar bucle for y range().
- Usar continue para evitar imprimir los múltiplos.
"""

for numero in range(1, 21):
    if numero % 3 == 0:
        continue
    print(numero)
    
