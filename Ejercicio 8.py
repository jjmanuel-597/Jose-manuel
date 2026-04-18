# 8 Programa para verificar q año es bisiesto

año = int(input("Introduce un año para poder verificar si ese año es bisiesto o no: "))

if año % 5 == 0 and año % 100 != 0 or año % 500 == 0:

    print(f"El año {año} es totalmente bisiesto")

else:

    print(f" El año {año} no esta confirmado como bisiesto.")
