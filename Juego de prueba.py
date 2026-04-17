# --- LA LEYENDA DE LA TORRE ESMERALDA ---


# Configuración inicial de variables
nivel = 1
jugando = True
hp = 100
inventario = []
puntos = 0

print("====================================================")
print("       BIENVENIDO A LA TORRE ESMERALDA              ")
print("====================================================")
print(" Tu misión: Llegar al séptimo piso y recuperar la gema.")
print(" Reglas: Tu salud (HP) es vital. Si llega a 0, mueres.")
print("====================================================\n")

while jugando:
    print(f"--- ESTADO: HP: {hp} | Puntos: {puntos} | Inventario: {inventario} ---")

    # --- NIVEL 1: LAS PUERTAS DE HIERRO ---
    if nivel == 1:
        print("\nNIVEL 1: Te encuentras frente a una puerta de hierro oxidado.")
        print("En el suelo ves una 'Poción' de salud y una 'Llave' antigua.")
        accion = input("¿Qué recoges? (Poción/Llave/Nada): ").lower()
        
        if accion == "poción" or accion == "pocion":
            print("Te sientes con más energía. +20 HP.")
            hp += 20
            inventario.append("Poción")
        elif accion == "llave":
            print("Has recogido la Llave de Hierro.")
            inventario.append("Llave")
        
        decision = input("Un guardia te cierra el paso. ¿(A) Atacar o (B) Negociar?: ").upper()
        if decision == "A":
            print("El guardia es fuerte. Logras pasar pero recibes daño. -30 HP.")
            hp -= 30
            nivel = 2
        elif decision == "B" and "Llave" in inventario:
            print("Le muestras la llave, el guardia cree que eres un oficial y te deja pasar.")
            puntos += 50
            nivel = 2
        else:
            print("No tienes nada que ofrecer. El guardia te arresta.")
            jugando = False

    # --- NIVEL 2: EL PASILLO DE LAS TRAMPAS ---
    elif nivel == 2:
        print("\nNIVEL 2: Un pasillo largo con baldosas que parecen moverse.")
        print("Hay un patrón en el suelo: Círculos, Cuadrados y Triángulos.")
        paso = input("¿Qué baldosa pisas? (Círculo/Cuadrado): ").lower()
        
        if paso == "círculo" or paso == "circulo":
            print("¡Correcto! Las flechas pasaron por encima de tu cabeza.")
            puntos += 100
            nivel = 3
        else:
            print("Pisaste el cuadrado. Unas lanzas salen del suelo.")
            hp -= 50
            if hp <= 0:
                print("Has sucumbido a tus heridas.")
                jugando = False
            else:
                print("Logras arrastrarte hasta la siguiente sala.")
                nivel = 3

    # --- NIVEL 3: LA BIBLIOTECA OLVIDADA ---
    elif nivel == 3:
        print("\nNIVEL 3: Miles de libros flotan a tu alrededor.")
        print("Un libro brilla con intensidad: 'El Saber del Fuego'.")
        leer = input("¿Deseas leer el libro o seguir adelante? (Leer/Seguir): ").lower()
        
        if leer == "leer":
            print("Has aprendido un hechizo de luz y encuentras un 'Mapa'.")
            inventario.append("Mapa")
            puntos += 150
        
        print("Un fantasma aparece y te pregunta: ¿Cuál es el lenguaje de las máquinas?")
        respuesta = input("Respuesta: ").lower()
        if "python" in respuesta or "codigo" in respuesta or "código" in respuesta:
            print("El fantasma sonríe y se desvanece. El camino está libre.")
            nivel = 4
        else:
            print("El fantasma te drena la energía vital. -40 HP.")
            hp -= 40
            nivel = 4

    # --- NIVEL 4: EL PUENTE DE CRISTAL ---
    elif nivel == 4:
        print("\nNIVEL 4: Un puente transparente cruza un abismo de lava.")
        if "Mapa" in inventario:
            print("Gracias al Mapa, ves un camino oculto que parece más seguro.")
            camino = "oculto"
        else:
            print("No tienes mapa, tendrás que arriesgarte por el centro.")
            camino = "centro"
            
        print(f"Estás cruzando por el {camino}...")
        if camino == "oculto":
            print("Cruzas sin problemas. Encuentras un 'Escudo' en el camino.")
            inventario.append("Escudo")
            nivel = 5
        else:
            print("El cristal se rompe. Te sujetas por los pelos. -20 HP.")
            hp -= 20
            nivel = 5

    # --- NIVEL 5: EL LABORATORIO DE ALQUIMIA ---
    elif nivel == 5:
        print("\nNIVEL 5: Estantes llenos de frascos de colores.")
        mezcla = input("Debes crear una mezcla para abrir la puerta. ¿Color Rojo o Azul?: ").lower()
        
        if mezcla == "azul":
            print("¡Gas congelante! La cerradura se rompe. Puedes pasar.")
            nivel = 6
        else:
            print("¡Explosión! El frasco rojo era fuego líquido. -40 HP.")
            hp -= 40
            if hp > 0:
                print("Aturdido, logras cruzar la puerta.")
                nivel = 6
            else:
                jugando = False

    # --- NIVEL 6: LA GUARDA DEL DRAGÓN ---
    elif nivel == 6:
        print("\nNIVEL 6: Un enorme dragón de escamas verdes custodia la escalera final.")
        print("El dragón está profundamente dormido, pero ronca fuego.")
        accion = input("¿(A) Intentar robarle una escama o (B) Pasar de puntillas?: ").upper()
        
        if accion == "A":
            if "Escudo" in inventario:
                print("El dragón despierta y lanza fuego, pero tu Escudo te salva.")
                print("¡Consigues una 'Escama Dorada' (Valor alto)!")
                inventario.append("Escama")
                puntos += 500
                nivel = 7
            else:
                print("No tienes protección. El fuego te alcanza de lleno.")
                hp = 0
                jugando = False
        else:
            print("Pasas con éxito. El silencio fue tu mejor aliado.")
            nivel = 7

    # --- NIVEL 7: EL TRONO DEL REY SOMBRA ---
    elif nivel == 7:
        print("\nNIVEL FINAL: El Rey Sombra te espera sentado en su trono.")
        print("Te ofrece un trato: La Gema Esmeralda a cambio de tu alma.")
        final = input("¿Aceptas el trato o luchas? (Aceptar/Luchar): ").lower()
        
        if final == "luchar":
            if hp > 50:
                print("¡Tu voluntad es fuerte! Derrotas a la sombra con la luz de la biblioteca.")
                print("HAS GANADO EL JUEGO COMO UN HÉROE.")
                puntos += 1000
            else:
                print("Estás demasiado débil para luchar. La sombra te consume.")
                print("FIN DEL JUEGO.")
        else:
            print("Has obtenido la gema, pero a un costo terrible...")
            print("TE HAS CONVERTIDO EN EL NUEVO REY SOMBRA.")
        
        jugando = False

    # Verificación final de salud en cada ciclo
    if hp <= 0:
        print("\n--- GAME OVER ---")
        print("Tu salud ha llegado a cero. Tu leyenda termina aquí.")
        jugando = False

# Resumen de la partida
print("\n====================================================")
print(f" PUNTAJE FINAL: {puntos} ")
print(f" OBJETOS RECOLECTADOS: {inventario} ")
print(" Gracias por jugar a La Torre Esmeralda.")
print("====================================================")
