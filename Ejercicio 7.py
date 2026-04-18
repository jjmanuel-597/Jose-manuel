#7 Programa para ver los dias de la semana 

dia = int(input("Introduce un numero del 1 al 7 para ver el dia de la semana: "))

if dia == 1 and  dia <= 7:

    print("El dia de la semana es: Lunes")  

elif dia == 2 and  dia <= 7:

    print("El dia de la semana es: Martes")    

elif dia == 3 and  dia <= 7:

    print("El dia de la semana es: Miercoles")

elif dia == 4 and  dia <= 7:

    print("El dia de la semana es: Jueves")

elif dia == 5 and  dia <= 7:

    print("El dia de la semana es: Viernes")

elif dia == 6 and  dia <= 7:

    print("El dia de la semana es: Sabado")

elif dia == 7 and  dia <= 7:

    print("El dia de la semana es: Domingo") 

else:

    print("El numero ingresado no es valido, por favor ingrese un numero del 1 al 7")