"""Enunciado: Procesa una lista de tuplas (Nombre, Edad) y clasifica en Menor, Adulto o Mayor.
Requerimientos: Desempaqueta la tupla en un for y usa una estructura múltiple if-elif-else."""
    
personas = [("Alice", 17), ("Bob", 25), ("Charlie", 70)]
for nombre, edad in personas:
    if edad < 18:
        categoria = "Menor"
    elif 18 <= edad < 65:
        categoria = "Adulto"
    else:
        categoria = "Mayor"
    print(f"{nombre} es un {categoria}.")
