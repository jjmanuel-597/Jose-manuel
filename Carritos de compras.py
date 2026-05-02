def mostrar_menu():
    """
    Muestra el menú de opciones al usuario.
    """
    print("\n" + "="*30)
    print("   🛒 MENÚ DE LA CESTA 🛒")
    print("="*30)
    print("1. AGREGAR un nuevo elemento   ➕")
    print("2. MOSTRAR la cesta          🧺")
    print("3. ELIMINAR un elemento      ❌")
    print("4. CALCULAR el total         💰")
    print("5. RENUNCIAR / Salir         👋")
    print("="*30)

def agregar_articulo(cesta):
    """
    Agrega un artículo y su precio a la cesta.
    """
    print("\n--- Agregar Nuevo Artículo ---")
    nombre = input("Introduce el nombre del artículo: ").strip()
    

    # Bucle para asegurar que el precio sea un número válido sin try/except
    while True:
        precio_str = input(f"Introduce el precio de '{nombre}': ").strip()
        # Validar si la entrada es un número flotante positivo
        if precio_str.replace('.', '', 1).isdigit():
            precio = float(precio_str)
            if precio >= 0:
                break
            else:
                print("⚠️ Error: El precio no puede ser negativo. Inténtalo de nuevo.")
        else:
            print("⚠️ Error: Por favor, introduce un número válido para el precio.")

    articulo = {"nombre": nombre, "precio": precio}
    cesta.append(articulo)
    print(f"✅ ¡'{nombre}' se ha añadido a la cesta!")

def mostrar_cesta(cesta):
    """
    Muestra todos los artículos en la cesta.
    """
    print("\n--- 🧺 Contenido de tu Cesta ---")
    if not cesta:
        print("Tu cesta está vacía. ¡Añade algo!")
    else:
        for i, articulo in enumerate(cesta, 1):
            # Se formatea el precio para mostrar siempre dos decimales
            print(f"{i}. {articulo['nombre']}: ${articulo['precio']:.2f}")
    print("---------------------------------")

def eliminar_articulo(cesta):
    """
    Elimina un artículo de la cesta seleccionado por el usuario.
    """
    print("\n--- Eliminar Artículo ---")
    if not cesta:
        print("No hay nada que eliminar. La cesta está vacía.")
        return

    mostrar_cesta(cesta) # Muestra los artículos para que el usuario elija cuál eliminar
    
    # Bucle para asegurar que el índice sea un número válido y esté en el rango, sin try/except
    while True:
        num_articulo_str = input("Introduce el número del artículo que quieres eliminar: ").strip()
        if num_articulo_str.isdigit():
            num_articulo = int(num_articulo_str)
            if 1 <= num_articulo <= len(cesta):
                articulo_eliminado = cesta.pop(num_articulo - 1)
                print(f"🗑️ ¡'{articulo_eliminado['nombre']}' ha sido eliminado de la cesta!")
                break
            else:
                print(f"⚠️ Error: El número debe estar entre 1 y {len(cesta)}.")
        else:
            print("⚠️ Error: Por favor, introduce un número válido.")

def calcular_total(cesta):
    """
    Calcula y muestra el precio total de todos los artículos en la cesta.
    """
    print("\n--- 💰 Total de la Compra ---")
    if not cesta:
        print("La cesta está vacía. El total es $0.00")
    else:
        total = sum(articulo['precio'] for articulo in cesta)
        print(f"El total de tu compra es: ${total:.2f}")
    print("----------------------------")

def main():
    """
    Función principal que ejecuta el programa del simulador de cesta.
    """
    cesta_de_compra = []
    
    print("¡Bienvenido al Simulador de Cesta de Compra!")

    while True:
        mostrar_menu()
        opcion = input("Elige una opción (1-5): ")

        if opcion == '1':
            agregar_articulo(cesta_de_compra)
        elif opcion == '2':
            mostrar_cesta(cestade_compra)
        elif opcion == '3':
            eliminar_producto(cesta_de_compra)
        elif opcion == '4':
            calcular_total(cesta_de_compra)
        elif opcion == '5':
            print("\n👋 ¡Gracias por usar el simulador! ¡Hasta pronto!")
            break
        else:
            print("\n⚠️ Opción no válida. Por favor, elige un número del 1 al 5.")
        
        # Pausa para que el usuario pueda leer el mensaje antes de volver al menú
        input("\nPresiona Enter para continuar...")

# Iniciar el programa
if __name__ == "__main__":
    main()

