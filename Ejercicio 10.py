# 10 Progrrama para verificar entre 3 numeros cual es el mayor

num1 = float(input("Introduce el primer numero: "))

num2 = float(input("Introduce el segundo numero: "))

num3 = float(input("Introduce el tercer numero: "))

if num1 >= num2 and num1 >= num3:

    print("El numero mayor es:", num1)

    Mayor = num1

elif num2 >= num1 and num2 >= num3:

   Mayor = num2

else:

    Mayor = num3

print(f"El numero mayor es: {Mayor}")     