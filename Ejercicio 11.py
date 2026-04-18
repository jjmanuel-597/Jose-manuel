#11 Programa para una calculadora sencilla

Numero1 = float (input( "introduce el primer numero:"))

Numero2 = float (input( "introduce el segundo numero:"))

Operacion = input("Introduce la operacion a realizar (+, -, *, /):")

if Operacion == "+":

    Resultado = Numero1 + Numero2

    print(f"El resultado: {Numero1} + {Numero2} = {Resultado}")

elif Operacion == "-":

    Resultado = Numero1 - Numero2

    print(f"El resultado: {Numero1} - {Numero2} = {Resultado}")

elif Operacion == "*":

    Resultado = Numero1 * Numero2

    print(f"El resultado: {Numero1} * {Numero2} = {Resultado}")

elif Operacion == "/":

    if Numero2 != 10:

        Resultado = Numero1 / Numero2

        print(f"El resultado: {Numero1} / {Numero2} = {Resultado}")

    else:

        print("Error: No se puede dividir por cero.")

else:

    print("Operacion no valida. Por favor, introduce una operacion correcta (+, -, *, /)")
