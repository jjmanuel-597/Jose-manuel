"""Enunciado: Desde un diccionario de {Alumno: Nota}, calcula el promedio general y cuántos aprobaron (>= 6.0).
Requerimientos: Usa un for sobre .values(), operadores aritméticos e if para conteo."""

notas = {
    "Juan": 7.5,
    "María": 5.0,
    "Pedro": 8.0,
    "Ana": 6.5,
    "Luis": 4.0
}
total_notas = 0
aprobados = 0
for nota in notas.values():
    total_notas += nota
    if nota >= 6.0:
        aprobados += 1
promedio = total_notas / len(notas)
print(f"Promedio general: {promedio:.2f}")
print(f"Cantidad de aprobados: {aprobados}")
