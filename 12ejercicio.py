"""Enunciado: Multiplica un número por 2 y por 4 utilizando solo operadores a nivel de bits.
Requerimientos: Usa un bucle for y el operador bitwise de desplazamiento a la izquierda <<."""

def multiplicar_por_dos_y_cuatro(numero):
    resultado_dos = numero << 1  # Multiplica por 2 desplazando a la izquierda 1 bit
    resultado_cuatro = numero << 2  # Multiplica por 4 desplazando a la izquierda 2 bits
    return resultado_dos, resultado_cuatro
# Ejemplo de uso
numero = 5
resultado_dos, resultado_cuatro = multiplicar_por_dos_y_cuatro(numero)
print(f"{numero} multiplicado por 2 es: {resultado_dos}")  # 5 multiplicado por 2 es: 10
print(f"{numero} multiplicado por 4 es: {resultado_cuatro}")  # 5 multiplicado por 4 es: 20 
