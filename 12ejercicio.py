"""Enunciado: Multiplica un número por 2 y por 4 utilizando solo operadores a nivel de bits.
Requerimientos: Usa un bucle for y el operador bitwise de desplazamiento a la izquierda <<."""

def multiplicar_por_dos_y_cuatro(numero):
    resultado_dos = numero << 1  
    resultado_cuatro = numero << 2  
    return resultado_dos, resultado_cuatro

numero = 5
resultado_dos, resultado_cuatro = multiplicar_por_dos_y_cuatro(numero)
print(f"{numero} multiplicado por 2 es: {resultado_dos}")  
print(f"{numero} multiplicado por 4 es: {resultado_cuatro}") 
