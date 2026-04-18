""" Simulador de acceso 🔐
Enunciado: Crear un login con contraseña ("python123"). El usuario tiene solo 3 intentos.
Requerimientos: 
- Usar while con contador.
- Salir con break si la contraseña es correcta, de lo contrario, bloquear al tercer intento fallido.
"""
intentos = 0
while intentos < 3:
    contraseña = input("Ingrese la contraseña: ")
    if contraseña == "python123":
        print("¡Acceso concedido!")
        break
    else:
        intentos += 1
        print(f"Contraseña incorrecta. Intento {intentos}/3.")
else:
    print("Acceso bloqueado. Demasiados intentos fallidos.")